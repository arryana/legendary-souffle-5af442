#!/usr/bin/env python3
"""Bring the site's web fonts in-house, so no page waits on Google to draw.

    python3 tools/self-host-fonts.py           (from the repo root)

Why. Every page carried `@import url(https://fonts.googleapis.com/...)` inside its
own <style>. A stylesheet is render-blocking, and an @import is the worst kind --
it is not discovered until the sheet around it has been parsed, so it cannot even
be pre-connected. If that host is slow, throttled or blocked, the page is a blank
dark rectangle until the request resolves or gives up. Measured in a sandbox where
it is blocked: nothing at all appeared for 12.5 seconds -- not the wall, not a
plate, not one card. On an ordinary connection it answers in a moment, which is
exactly why this was never seen.

The site's only other outside dependency is the weather API, and that one fails
out loud by design. This one failed silently, which is the worse kind.

What it does: reads every Google Fonts URL in the repo, fetches the real CSS,
keeps the `latin` and `latin-ext` cuts (this site has no other), downloads the
woff2 files into fonts/, and rewrites each @import as local @font-face rules.
Re-runnable: it only fetches what it hasn't got, and rewrites from the same source.

If a face is ever added, add it to the page as an @import as before and re-run.
"""
import os, re, subprocess, sys, glob
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
FONTDIR = 'fonts'
KEEP = ('latin', 'latin-ext')          # the site is Latin-script only
UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/120.0 Safari/537.36')   # asks for woff2

IMPORT_RE = re.compile(
    r"@import\s+url\(\s*['\"]?(https://fonts\.googleapis\.com/css2\?[^'\")]+)['\"]?\s*\)\s*;")


def fetch(url):
    r = subprocess.run(['curl', '-sS', '-L', '--max-time', '60', '-A', UA, url],
                       capture_output=True)
    if r.returncode:
        sys.exit('could not fetch %s\n%s' % (url, r.stderr.decode()[:400]))
    return r.stdout.decode('utf-8', 'replace')


def faces(css):
    """The @font-face blocks, each tagged with the subset comment above it."""
    out, subset = [], None
    for chunk in re.split(r'(/\*\s*[\w-]+\s*\*/)', css):
        m = re.match(r'/\*\s*([\w-]+)\s*\*/', chunk.strip())
        if m:
            subset = m.group(1)
            continue
        for blk in re.findall(r'@font-face\s*\{[^}]*\}', chunk):
            out.append((subset, blk))
    return out


def field(blk, name):
    m = re.search(name + r'\s*:\s*([^;]+);', blk)
    return m.group(1).strip() if m else None


def main():
    pages = sorted(set(glob.glob('*.html')) | set(glob.glob('*/index.html')))
    urls = OrderedDict()
    for p in pages:
        for u in IMPORT_RE.findall(open(p, encoding='utf-8').read()):
            urls.setdefault(u, []).append(p)
    if not urls:
        print('no Google Fonts imports left — nothing to do'); return

    os.makedirs(FONTDIR, exist_ok=True)
    local_css = {}          # url -> the @font-face rules to put in its place
    downloaded = 0

    for url in urls:
        rules = []
        for subset, blk in faces(fetch(url)):
            if subset not in KEEP:
                continue
            fam = (field(blk, 'font-family') or '').strip('"\' ')
            wght = field(blk, 'font-weight') or '400'
            style = field(blk, 'font-style') or 'normal'
            src = field(blk, 'src') or ''
            m = re.search(r"url\((https://fonts\.gstatic\.com/[^)]+\.woff2)\)", src)
            if not m:
                continue
            name = '%s-%s%s-%s.woff2' % (
                fam.replace(' ', ''), wght, '' if style == 'normal' else 'i', subset)
            path = os.path.join(FONTDIR, name)
            if not os.path.exists(path):
                r = subprocess.run(['curl', '-sS', '-L', '--max-time', '60', '-A', UA,
                                    '-o', path, m.group(1)], capture_output=True)
                if r.returncode or not os.path.getsize(path):
                    sys.exit('could not download ' + m.group(1))
                downloaded += 1
            ur = field(blk, 'unicode-range')
            rules.append(
                "@font-face{font-family:'%s';font-style:%s;font-weight:%s;"
                "font-display:swap;src:url(__P__%s) format('woff2');%s}"
                % (fam, style, wght, name,
                   ('unicode-range:%s;' % ur) if ur else ''))
        if not rules:
            sys.exit('no usable faces found for ' + url)
        local_css[url] = rules

    for p in pages:
        src = open(p, encoding='utf-8').read()
        orig = src
        prefix = FONTDIR + '/' if '/' not in p else '../' + FONTDIR + '/'
        for url, rules in local_css.items():
            block = '\n  '.join(r.replace('__P__', prefix) for r in rules)
            src = src.replace(
                "@import url('%s');" % url, block).replace(
                '@import url("%s");' % url, block).replace(
                '@import url(%s);' % url, block)
        if src != orig:
            open(p, 'w', encoding='utf-8').write(src)
            print('  rewrote', p)

    left = sum(len(IMPORT_RE.findall(open(p, encoding='utf-8').read())) for p in pages)
    total = sum(os.path.getsize(f) for f in glob.glob(FONTDIR + '/*.woff2'))
    print('\n%d font files (%d new), %.0fKB total in %s/' %
          (len(glob.glob(FONTDIR + '/*.woff2')), downloaded, total / 1024, FONTDIR))
    print('Google Fonts imports still in the site: %d' % left)


if __name__ == '__main__':
    main()
