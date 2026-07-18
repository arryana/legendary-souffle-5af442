# CLAUDE.md — the "sagne" site

This file tells Claude Code how to work on this site. Read it first, every session.

---

## Who you're helping, and how to talk

- The owner is **non-technical** and works **only through Claude Code chat**. There is no
  local editor, no terminal on their side, no GitHub UI. You are the whole interface.
- The whole workflow reduces to two words: **"Do"** (make my change real, on the live site)
  and **"Undo"** (take the last one back). Before every **Do** there's a **Preview** to look at
  first (a picture today; a live link once Netlify previews are enabled — see below). So:
  **Preview → Do → (or Undo).**
- **No jargon in chat.** Don't say "commit", "branch", "merge", "PR", "rebase". Say things like
  "Here's a **Preview** — want me to **Do** it (make it live)?" All the git machinery lives in
  this file and stays invisible to the owner.
- For anything **visual**, let them **see it before it's live** (that's what Preview is for).
  A non-technical owner can't read a diff.
- Keep replies short and concrete. After any change, end with the options in plain words:
  **Preview** · **Do** (make it live) · **Undo**.

---

## What this site is

**sagne** is a small collection of beautifully-made, standalone interactive web pieces —
ambient "instruments" and decorative toys. Each page is a **single self-contained HTML file**
with its own image assets. There is **no build step, no framework, no `package.json`** — just
plain HTML + CSS + JavaScript. Editing = changing those files directly.

**Hosting:** the site is on **Netlify**, which **auto-deploys the live site from the `main`
branch**. That's the key fact behind everything below: **a change is only live once it's on
`main`.** Until then it's a private draft.

**Landing page:** `index.html` (titled *sagne*) — a dark, elegant grid of cards, each linking
to one piece.

### The pages

| File | On landing page? | What it is |
|------|:---:|------------|
| `index.html` | — | Landing page: the card grid ("sagne") |
| `candler.html` | ✅ | *Sagne Candle* — an interactive candle. `candler_5.html` is an alternate version (not linked) |
| `acorn.html` | ✅ | An acorn resting on wood, interactive |
| `lamp.html` | ✅ | An oil lamp |
| `warmler.html` | ✅ | A warming plate with selectable metal **finishes** (brass, copper, aged brass/copper, gold, silver, diamond-plate). `warmler-picker-concept.html` is a finish-picker concept (not linked) |
| `rain.html` | ✅ | Rain on glass |
| `ant.html` | ✅ | Ants |
| `windower.html` | ✅ | A window onto the sky that follows the visitor's **local time & location** (uses geolocation + the clock) |
| `galileo.html` | ✅ | A **Galileo thermometer** whose floats rise and sink with the visitor's **real local temperature** (open-meteo API); has a °C/°F toggle |
| `conometer.html` | ✅ | A **pinecone hygrometer** — the pinecone opens (dry) and closes (wet) with the visitor's **real local humidity** (open-meteo API); has a live/manual toggle |
| `crystal.html` | — | A crystal (not linked from the landing page) |

**Live-data pieces** — `galileo`, `conometer`, `windower` — read the visitor's **geolocation**
and call **public APIs** (`api.open-meteo.com`). If you edit these, keep that working; don't
break the geolocation or the fetch. (These are also why a *faithful* Preview matters — a plain
screenshot can't show live weather.)

### Asset naming conventions (follow these for any new asset)

- **Card previews** on the landing page: `<demo>-card.png` (e.g. `lamp-card.png`).
- **conometer** frames: `cone-01.png` … `cone-09.png`, plus `conometer-background.png`
  (frame 1 = fully open/dry, frame 9 = closed/wet).
- **galileo** floats: `floats/<color>.png` — `blue, aqua, green, yellow, orange, red, pink,
  purple, silver`.
- **warmler** finishes come in three files each:
  `warmler-plate-<finish>.png`, `warmler-swatch-<finish>.png`, `warmler-texture-<finish>.png`
  (finish = `brass, copper, aged-brass, aged-copper, gold, silver, diamond-plate`).
- `favicon.svg` is the site icon.
- Reference assets by **relative path** (they sit next to the HTML). Match the existing naming
  when adding new ones.

---

## The three actions: Preview → Do → Undo

Everything the owner does is one of these three words. Keep the git details hidden; just use the
words.

### 🔍 Preview — see the change before it's live

**What it means to the owner:** "show me what it'll look like, before it touches my real site."

There are two ways to Preview. **The picture works today; the live link needs a one-time setup.**

**A. Static picture — works now, the current default.** A real Chromium is pre-installed. Render
the changed page and screenshot it, **including a phone width (390px)** — mobile matters on this
site — then send it with `SendUserFile`. A before/after pair is ideal.
```bash
SC="<scratchpad>"; cd "$SC" && npm init -y >/dev/null 2>&1 && npm install playwright-core >/dev/null 2>&1
# shot.js: chromium under /opt/pw-browsers/<version>/chrome-linux/chrome, args ['--no-sandbox'],
#          context viewport {width:390,height:844} for phone; ~1200 wide for desktop
node "$SC/shot.js" /home/user/legendary-souffle-5af442/index.html "$SC/preview.png"
```
A picture can't show motion or live data — but it's honest about layout and appearance and needs
nothing set up. (For a non-visual change like this file, Preview doesn't really apply — just
explain what changed and offer **Do**.)

**B. Netlify Deploy Preview — the real thing, once enabled.** When enabled, every open pull
request gets its own hosted URL (e.g. `deploy-preview-12--<site>.netlify.app`), separate from the
live site, where *everything* works — fonts, live weather, geolocation. Usage:
```bash
# after pushing the branch, open the PR — that's what triggers the preview build:
#   create_pull_request  base=main  head=$BRANCH
#   then: pull_request_read (get_status / get_check_runs) → find the "netlify/…/deploy-preview"
#         entry and give its target_url to the owner (build takes ~1–2 min).
```
> **Status (as of this writing): NOT enabled for this repo.** A test PR produced no Netlify
> status at all, so deploy previews aren't wired up yet. To turn them on, the **owner** connects
> the repo in the Netlify dashboard (**Site configuration → Build & deploy → Continuous
> deployment**, via the Netlify GitHub App) and enables **Deploy Previews** for pull requests.
> Once that's done, method B becomes the default and method A stays as the instant fallback.

### ✅ Do — make the change live

**What it means to the owner:** "put it on my real website."

Only act on an **explicit "Do"** from the owner, after they've had a Preview. This changes the
live site — it's their call.

**Exact steps (for Claude):**
```bash
BRANCH=claude/test-file-repo-root-f9duia
# If the edits aren't committed yet, start from the live state and commit them:
git fetch origin main
git checkout -B "$BRANCH" origin/main   # (or: git reset --mixed origin/main to keep in-progress edits)
git add -A && git commit -m "Short, plain description of the change"
git push -u origin "$BRANCH"
# Publish it:
#   create_pull_request  base=main  head=$BRANCH   (title = the plain description)
#     — if a preview PR from method B is already open, just reuse it (skip to merge)
#   merge_pull_request   (method: merge)
git fetch origin main   # confirm the change landed on main
```
Netlify redeploys the live site from `main` (~1–2 minutes). Tell the owner plainly: *"Done —
it's live."* Then remind them **Undo** is available if they change their mind.

### ↩ Undo — take the last change back

**What it means to the owner:** "put the site back the way it was before the last change."

This matches how they think about it: **sync with the live site → reverse the last change → send
that reversal to the live site.**

**Exact steps (for Claude) — when the last change is already live:**
```bash
BRANCH=claude/test-file-repo-root-f9duia
git fetch origin main
git checkout -B "$BRANCH" origin/main
git log origin/main --oneline -6            # find what "the last change" was
git revert --no-edit <sha-of-last-change>   # a new "undo" change; never rewrites history
#   if the last change is a merge commit:   git revert --no-edit -m 1 <merge-sha>
git push -u origin "$BRANCH"
# create_pull_request  base=main  head=$BRANCH   (title: "Undo: <what it was>")
# merge_pull_request
git fetch origin main   # confirm
```
**If the last change was never made live** (still just a draft / an open PR the owner decided
against): there's nothing on the live site to reverse — close the PR and discard the local edits
(`git restore .`). Tell the owner it's been dropped.

Undo is the safety net — run it as soon as the owner says "Undo", and always **report what you
undid** in one sentence.

---

## Branch & deploy notes (background for Claude)

- **Work branch:** `claude/test-file-repo-root-f9duia` — the authoritative branch. Do all work
  here. Never push to another branch without the owner's explicit OK.
  - `claude/repo-contents-h8pt8t` is a **specialist support branch** (help brought in for
    specific tasks), not the main line of work — don't build on it by default.
- Every **Do** merges the change into `main`, so **start each new change fresh from `main`** (as
  shown above) rather than building on old branch history.
- **Netlify:** the **live site** deploys from `main`. **Deploy Previews** on pull requests are
  **not enabled yet** (see the Preview section) — until they are, Preview = the static picture.
- A pull request is opened as part of **Do** (and merged) — or during **Preview** method B once
  that's enabled. Don't open PRs for anything else.
- **Pushing** goes through the session's git proxy. A **403** on push means a permissions /
  re-auth problem, not a code problem — tell the owner in plain terms ("I've lost permission to
  save to the website — can you re-check my access?") and **don't hammer retries**.

## Guardrails

- Keep each change **small and self-contained** — one idea at a time.
- **Preview → Do.** Never make a visual change live that the owner hasn't seen.
- **Do** and **Undo** both change the **real, live site** — treat them as the deliberate,
  owner-approved moments they are.
