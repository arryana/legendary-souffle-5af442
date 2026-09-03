# pendulum

The full record of this piece, moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short.
Everything here was written as it happened; the newest material is at the bottom. Read it before
touching `pendulum/index.html`.

A **Foucault pendulum**, its swing slowly turning with the Earth; real-photo globe with a locator search

**Done** — precession, swing and pin ring all verified by measurement against the real physics.
Aug 2026 it was given a **real-world-time** checkbox (the clock face beside the ∞): ticked, the plane
precesses at the true Foucault rate off the actual clock — Earth's turn times sin(latitude) — and the
speed slider stands down. **It stores nothing.** The angle is a pure function of the clock and the
latitude, and so is the whole sand trace, so ticking it (or changing latitude, or resizing) recomputes
what the plate would have drawn since local midnight in one pass and lays it down. The honest caveat,
which is why it's a checkbox and not the default: at the true rate the turn is very nearly
imperceptible, the better part of a day for one rosette, and the trace comes out as swept ground
rather than separate lines because successive passes land 0.007° apart — closer than a grain is wide.
The swing itself stays exactly as lively as ever.

**The rate was wrong, and had been since the checkbox was added.** She suspected the
piece after real-time arrived and asked for it checked before running it on the machines; she was
right to, though not about what. `DAY=86400` — the **solar** day — was driving the precession, and
what a Foucault plane turns against is the **fixed stars**, so the day that governs it is the
**sidereal** one, 86164.0905s. It is why the textbook figure is 15.041°/hour and not a round 15.
Measured on the running page before the fix: a full turn at the pole took **24h 00m** against the
real **23h 56m 04s**, and every latitude ran **0.27% slow**. After: 23h 56m 04s exactly, and the
rate matches 15.041·sin(lat) at 90, 60, 51.5, 30, 0, −34 and −90°, with the sign right in both
hemispheres. Invisible to anyone watching — about a degree of lag after a whole day — and wrong all
the same, which is the standard this piece was signed off against. The same constant also drove the
manual speed-slider mode, so that is now right too.

**The hiccups she expected are not there**, and
that is measured rather than assumed. Ticking the box, moving latitude and resizing each re-derive
the whole rosette in one pass; worst frame gap on a desktop 73ms, and on a Kindle-speed CPU 129ms
when the box is ticked, 30–91ms otherwise — one hitch, at the moment you ask for it, never a freeze.
`rebuildRealTrace` clears its own pending flag on its first line, so it cannot run every frame, and
the rebuild is deferred while the globe is being dragged so it happens once on release. After all of
it the angle still equals the pure clock function, so nothing accumulates or drifts.

**"It looks as
if the line is moving like a clock hand, not responding to the swings."** Her report on the real-time
view, and the impression is right even though the swing under it is not: measured with the box
ticked, the bob travels its full 287px each way and passes the centre 6 times in 10s — a 3.4s period,
**identical to the ordinary mode**. What she was actually looking at is the swept sand. Since local
midnight the plane really has turned ~139°, so the plate really is worked across two opposite 139°
sectors — correct, and it reads as a pie chart, because a filled sector with a hard radial edge
creeping round a circle is the visual language of a clock hand.

The sand's own signature was the
part that was wrong. A swinging weight is slowest at the ends of its swing, so working goes as 1/v ∝
1/√(A²−r²): a hard pile-up at both turning points and a middle barely touched. The rebuild's gradient
ran **0.20 at the pivot to 0.44 at the rim — barely two to one, near enough a flat fill**. It now
follows the real curve, 0.085 to 0.527 (clamped, because the true curve is infinite at the turning
point), so the rim band is the brightest thing on the plate and the body is faint.

**A temporal
fade was tried and backed out, and it is worth knowing why before anyone tries it again**: fading the
sweep from settled at the far end to fresh at the leading edge takes ~18 stacked wedge fills at an
alpha of a few thousandths each, and the canvas **dithers alpha that low** — the whole region came
out crosshatched with stipple. Noise instead of sand is worse than the hard edge it was meant to
soften. Doing it properly wants an angular gradient (`createConicGradient`), which the older browsers
on her bench may not have; the way in, if it is ever wanted, is conic where it exists and the flat
fill where it doesn't.

**Still open, and hers**: whether the sector now reads as sand or still as a
dial. The geometry is honest — that ground really has been worked — so this is a question about the
look, not a fault to fix. Her word on the change was ***"it's better"*** — which is an improvement
banked and not a verdict, so **don't revert it and don't treat it as settled either**.

**"The line
moves AHEAD of the pendulum swing."** Her report on the speed-slider setting, Aug 2026. Measured, it
never does — the bob sits on that line to within **0.07° over 658 frames**. What runs ahead is the
**ratio**: the slider turns the plane without touching the swing, so at its default the plane turns
**1.87° per swing where in life it turns 0.009°**, and a rigid full-diameter line at constant
brightness is what made that read as a hand sweeping a dial. There is no way round the ratio — speed
the swing up too and it is a blur long before the turn is watchable; a real one is about one turn per
25,000 swings, which is why the honest setting is the clock face. So the LINE went instead, her call:
**a short trail behind the weight**, which is ground it has just crossed and so can never reach ahead
of it. Held to a fixed **length**, not a fixed time — the bob is nearly stationary at the ends of its
swing, which is exactly where the pins are and where the swing's direction most needs reading.

**And
the pins were the wrong way round**, which is what actually made the piece unreadable. A **fallen** pin
was drawn as a saturated brass bead at full opacity — the brightest thing on the plate after the bob —
and a **standing** one as a stroke at alpha 0.26. So a ring of bright beads sat over exactly the ground
the swing had already crossed and read as *the pins are still here*, the plain opposite of what the sand
beneath was saying. Nothing was wrong in the model. On a real ring it is the brass tops of the upright
pins that catch the light and the knocked ones that lie dark on the floor, and that is what it draws
now — **brightness and shape both**, an upright being a short stub with its head close in and a fallen
one a long shaft pushed well out with a dull head at the end. Her sentence is the general rule and
belongs beside *reads as broken*: ***"i get that it has to be true, and that's important, but if it's
incomprehensible to look at that doesn't teach anything."***

**The card was reshot**, and it was
worth doing because the old one was **a picture of the two faults she had just had fixed** — the
full-diameter line and the swept sand reading as a pie chart, with a slider left in the frame as well.
Anyone browsing the case was being shown the broken one.

**The honest trouble with a truthful
pendulum card, written down because it will come up again**: at the 40x53 the shelf's plate rows use,
the old card read clearly and the new one nearly vanished — the old was legible BECAUSE of the bug, a
flat-filled bright sector at full opacity, where the real rosette is thin lines kept faint on purpose
by the dwell curve. Running it longer barely helps: doubling the sand (60s to 120s of the ∞ trace)
doubled the lit pixels and changed almost nothing at thumbnail size. What did work was **cropping so
the plate fills the card edge to edge** rather than sitting at 79% of its width, which puts the rim
band — the brightest part, by the dwell curve — at the frame's own edges. Shot with ∞ ticked and the
speed at 100 for about two minutes, which is what gives a full rosette with pins still standing as
well as knocked. It is a quieter card than gyre's, and that is correct: it is a quieter piece, and the
loud version was the lie.

**The real-time tick was unreadable, and it is the white rabbit exactly**
— found Aug 2026 by sweeping for it rather than by her hitting it. The 🕰 showed ticked from unticked
through `color` and `filter:saturate()`, and **a colour emoji is a little bitmap the font hands over
whole**: it ignores `color` on *every* platform, and Windows ignores `filter` on it too. So the only
thing left saying whether the piece was running on the real clock was a faint glow — on a control that
carries state. The ∞ beside it is a plain text glyph and dimmed properly all along, so the two halves
of one control behaved differently and nobody noticed. It is a drawn mantel clock in `currentColor`
now, so the existing rules do what they always meant to; the glow became a `drop-shadow` since there is
no text left to shadow. **The colour is the cue and the glow only the flourish**, which is the way
round it should be — the reliable thing carries the state.
