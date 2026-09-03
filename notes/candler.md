# candler

The full record of this piece, moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short.
Everything here was written as it happened; the newest material is at the bottom. Read it before
touching `candler/index.html`.

*Sagne Candle* — an interactive candle. `candler_5.html` is an alternate version (not linked)

**Done** — "as perfect as I can make it without overhauling the actual candle itself."

Aug 2026 it was the first piece put through her four-device test (Mac, Windows tablet,
Kindle Fire, Jelly Star), and two faults under it accounted for most of what she found. **candler was the only
page on the site without the `#backlink{position:fixed;top:18px;left:22px}` rule** — the generated back-disc
block only says what the disc looks like and assumes the page already places it, so here the brass disc stood
in the page's own flow as a 38px-tall block at 0,0, shoving the whole candle down and pushing the last 38px of
the page off the bottom. That is why the readout line under the controls was invisible **on every device
including her Mac**, not just the small ones. And the page was `height:100vh` with `overflow:hidden`: on a
phone or tablet `100vh` is the whole screen *with the browser's own address bar counted as though it weren't
there*, and with nothing able to scroll, whatever lands under that bar is simply unreachable. On the Kindle
Fire that was both control pills — no menu at all — and on the 3in Jelly Star the second pill, which carries the
candle's size and type, so **no candle could be set**. It now lays out to `innerHeight`, which is the honest
number on every browser there is, old ones included; re-measured on resize and rotation but deliberately
**not while a pin's time field has focus**, because an on-screen keyboard shrinks `innerHeight` and would
collapse the candle under someone typing a time into it. Below 320px the first pill is also tightened, or the
snooze — last in the row once the timer is on — hangs 11px off the right-hand edge of a pill whose sideways
scrollbar is hidden. **She then re-ran the whole page on all four machines and passed it**: everything she
found is fixed and re-checked on the devices themselves, not in a screenshot. candler is the first piece
through that test, and the standard for the ones that follow.
