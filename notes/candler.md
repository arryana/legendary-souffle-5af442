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

**Sep 2026 — the timer counted minimised time twice, and rang early for it.** She asked
whether candler keeps going and rings with the window minimised. The clock half was already
right and was built for exactly this: timer mode locks wind to zero, so the burn rate is
plain wall-clock time, `realTimerWaxFraction()` recomputes the level from `lightedAt`, and a
1s `setInterval` (plus a `visibilitychange` catch-up) fires the pins whether or not the
window is on screen. Nothing is ever lost while hidden.

The animation loop was the fault. A browser stops giving a hidden window frames altogether,
so the first frame back carries the whole time away as a single `dt` — and `tick()` was
subtracting that `dt` from `state.waxFraction` in timer mode as well, on top of the level
`checkPinAlarms()` had already set from the clock. The candle dropped to **twice** the
elapsed time for the moment before the next check corrected it, and the pin loop inside that
same frame read the doubled level. Measured on a 30-minute candle, minimised for the stated
time, level on the first frame back against the truth:

| away | true level | level on the first frame back | what happened |
|---|---|---|---|
| 30s | 0.9833 | 0.9667 | — |
| 5m | 0.8333 | 0.6667 | a pin due at 7½m rang on the spot, 2½m early |
| 20m | 0.3333 | 0 | candle out on the spot, both remaining pins rang at once |

Past the half-way point it also set `state.extinguished`, which `checkPinAlarms()` returns
early on — so the correction never came and the candle stayed out. On the alarm she uses
daily, **early** is the wrong direction to be wrong in.

Fixed by reading the level rather than accumulating it: in timer mode `tick()` now takes
`realTimerWaxFraction()`, the same wall-clock answer the 1s check uses, so the two cannot
disagree by construction. **Passive mode still accumulates** and must — its rate follows the
wind slider, so there is no wall-clock truth to read, and accumulating is also what keeps it
burning honestly through time the window was hidden (verified: 3s at wind 0.5 dropped
0.00317, exactly the 1.9x of the still-air 0.00167).

Re-measured after the fix: all three rows above land exactly on the truth, nothing fires
early, nothing extinguishes early. A pin genuinely due while away (due at 10m, window away
12m) still rings once on return, at the right level. Ordinary running is untouched — a pin
due in 60s rang at 60.37s (the 0.37 is the pin's own fall to the plate, which is what the
ring is the sound of), and a candle with 6s of wax left went out at 6.006s.

Two limits that are the browser's and not ours, worth knowing before anyone reports them as
faults: a page nobody is looking at gets its timers slowed, so after about five minutes
minimised the 1s check can drop to about once a minute and the ring can be **late** by that
much (never early, never lost — and the catch-up on `visibilitychange` means it rings the
instant you look at it); and a phone that has been switched away from or locked will
generally suspend the audio, so it will not sound until you come back. Not tested from here:
the headless browser is launched with background throttling disabled, and `bringToFront()`
never actually set `document.hidden` — which is why the fault was measured by reproducing
the frame gap directly (`lastT = performance.now() - gap`, then one `tick()`) rather than by
minimising anything.
