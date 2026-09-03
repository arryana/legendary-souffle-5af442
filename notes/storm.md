# storm

The full record of this piece, moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short.
Everything here was written as it happened; the newest material is at the bottom. Read it before
touching `storm/index.html`.

A **storm glass** whose crystals form and clear with the visitor's real changing weather (open-meteo)

**Done**, and the piece that finishes instrumenta. Fifth through her four-device test, Aug 2026,
and four things came out of it.

**The needle lied whenever it had nothing to say.** Untranslated,
`#baro-needle-g` sits at x=0 in its own SVG — off the left-hand end of the printed scale, past
STORMY, below 950 — so between page load and open-meteo's first reply, and permanently whenever
the weather could not be reached at all, the dial showed a catastrophic low nobody had measured
while the readout beside it honestly said nothing. Correct underneath and a lie to look at, which
is the *reads as broken* class the standard below names. It is not drawn until it has a pressure
to point at, and the first placement suppresses the .9s sweep so it is never seen travelling up
from a position it was never at.

**The tendency is a mark now, not a sentence** — her call, and
the last prose on any piece. Chevrons pointing where the pressure is going, **one per rung of the
WMO tendency scale**: slowly, plain, rapidly, very rapidly, with a level bar for steady. Four, not
the three she first sketched — three would have had to merge two speeds of a real scale, and the
scale is the reason the readout is trustworthy. The words are still exact and still there: touch
the mark and it gives them, touch it again or anything around it and they go, which is galileo's
own rule for a popup. The steady bar cannot be read as the reading's own dash, since that shows
only when there is no pressure at all — and then the mark is off the page.

**The brass hand got
candler's pin treatment**, her own reminder that this was already settled: a transparent rect
inside the hand's `<g>`, no brass moved. Two things differ from a pin. The SVG is scaled to the
screen, so the rect is measured in the units that make it a real 44px wherever it is and
re-measured on resize; and on the 3in phone the whole dial is 39px tall, so it takes the dial's
full height and stops. Measured: 0x0 on desktop, 44x44 at 390 and on the Kindle, 36x39 on the 3in
phone, against brass of 11.2 / 7.3 / 4.5px. A tap still never moves the hand — only a drag — and
the drag keeps the offset it was taken hold of at, or a wide grab box would snap the hand out from
under a thumb.

**And the needle was swallowing the grab.** It is painted after the hand and its
stroke took pointer events, so a grab landing at the needle's own position never reached the hand —
which is exactly where the hand is meant to be parked, since setting it against the needle is the
whole use of the instrument. Half of the piece's one gesture was dead. The needle is a reading, not
a control, and takes nothing now.

**The 3in phone: the key was eating the piece.** Eight buttons,
each an icon *and* a 24px thumbnail of the glass, wrapped to three rows and took 169px of a 350px
screen — and `#scene-wrap`, an ordinary flex item, gave way to it and shrank to **13px across**.
Eight little glasses on screen, every one of them bigger than the real one. Below 380 the
thumbnails come off and the icons stay, four to a row: the thumbnail is the one genuinely redundant
thing at that size, since the glass itself is a tap away and changes instantly, and it was being
paid for out of the glass's own room. Nothing hidden, no new gesture, nothing to discover. Glass
13x22 -> 91x155 at 240x350; above 380 nothing applies and the page is pixel-identical, measured at
380 and 390.

**Sideways on that phone is 180px tall and no arrangement fits it** — the barometer
alone is 88px of it. That one is allowed to **scroll**, which is the answer she took for
kaleidoscope when content genuinely did not fit: the glass is held to a size rather than shrunk to
a sliver, and everything is reachable. The `(orientation: landscape)` qualifier on that rule is
load-bearing — the same phone is 350px tall in portrait, where the compact key already fits with
room to spare, and without it the rule set a page scrolling that didn't need to and pushed the
glass up under the two brass discs. A Kindle in landscape is 476 tall and never reaches it.
