# chimes

The full record of this piece, moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short.
Everything here was written as it happened; the newest material is at the bottom. Read it before
touching `chimes/index.html`.

**Wind chimes** you build yourself — pick the rod material and the cord/chain, then hang them. Uses warmler's swatch-picker pattern

Sound was rebuilt Aug 2026 (struck on impact, real bar overtones, pitch by material).

**The set is TUNED now**, Aug 2026, and this was the answer to her *"probably accurate, but not
beautiful — the reason windchimes are nice is because they're musical"*. She is right and it is a
**fidelity** point, not a compromise: the whole craft of a chime maker is cutting each tube to a
length that gives a wanted note, nearly always from a pentatonic, precisely so that no two tubes that
happen to strike together can sound wrong. Evenly spaced tubes with whatever pitches fall out is the
thing that is not real — and that is what this was. Measured, the default seven landed on C3 −16
cents, E3 −44, G#3 −27, C4 **+47**, F#4 −4, C5 **+49** and A5 −46: not one on a note, two within a
cent of a **quarter-tone** (the most dissonant place a pitch can sit), and the gaps between
neighbours widening from 3.7 semitones to 8.1. The physics is untouched — pitch still goes as 1/L²
and the lengths drawn are still the lengths that make those pitches — but the lengths are **chosen**
now: C3 D3 E3 G3 A3 C4 D4 for seven, every rod **0 cents** off, at every count from five to nine. The
per-rod popup snaps to the same cuts, so a rod set by hand is a note and not a quarter-tone between
two.

**And each material is cut to its own lengths**, which was her follow-up question — *is that
true for every instrument of the chimes?* It wasn't. Cutting all four to the same lengths left the
INTERVALS perfect everywhere (2,2,3,2,3,2 semitones in every material, so none of them ever sounded
sour) but only brass on real notes: wood came out 30 cents sharp, silver 30 flat and **glass 48
sharp**, a hair off a quarter-tone — in tune with itself and not with the world. A tube's pitch is
set by its length *and* by what it is made of, so a glass tube tuned to a note is a different length
from a brass one, and they are cut accordingly now: **every material 0 cents on every rod**. They
cannot all reach the same bottom note within a length a chime is allowed to be, and that is honest
too — brass and silver make C3, wood starts at E3 and glass at A3, which is why big brass sets are
deep and glass ones tinkly. Changing the rod material re-cuts the tubes rather than transposing them,
and the four sets come out at similar lengths (179–120, 158–106, 176–114, 171–111) so nothing jumps
on screen.

**And a rod-length slider beside the chain one**, her ask. With a tuned set it is a
**transpose**: the whole chime moves along the scale and stays in tune with itself, which is what a
smaller or larger set of the same design actually is. Short rods also hang higher and swing quicker,
so the meetings get busier as well as brighter — one control, both effects, which is exactly how she
described wanting it.

**And each material sounds like its own substance**, her third point. Two reasons it
didn't. A material is named in the first few HUNDREDTHS of a second — the contact noise of the strike
itself, before any note has established — and **only wood had one**; the metals and the glass began
with no transient at all, which is a synthesiser rather than an object being hit. And brass and
silver differed only in pitch and ring, making them one instrument at two heights: what separates
metals is how fast the HIGH modes die against the fundamental, how many there are, and the slow
warble a real tube gives from its two bending modes being slightly split. The mode ratios are the
free-free bar's own (1 : 2.756 : 5.404 : 8.933 : 13.34) and there were three of them — the fourth and
fifth are most of what reads as *clang*. Measured on the rendered notes: wood the dullest strike and
gone in **0.20s** with no upper partials at all; glass the brightest strike and the busiest, 5.6%;
silver the longest ring at **2.72s** and the purest, 1.2%; brass in between and warmer, 4.0%, with a
beat the others don't have.

**Her verdict on all of that is in**, Aug 2026, and it covers the tuning,
the per-material cuts and the strike together: ***"it sounds a great deal better."*** And then, asked what
the difference was: ***"before it was, 'what's that bloody racket'. now it's 'oh, my computer is playing
wind chimes!'"*** Keep that line, because it is the whole case for the tuning in one sentence and it
answers her own original complaint — *"probably accurate, but not beautiful — the reason windchimes are
nice is because they're musical."* An untuned set is not a worse wind chime, it is **not a wind chime**:
the thing a listener recognises is the pentatonic, not the tubes. That is why the tuning was argued here
as fidelity rather than as prettiness, and why the physics was left alone and only the lengths chosen. If
anyone is ever tempted to space the tubes evenly again, this is the sound they would be going back to.
Not a Done mark —
she has heard it, not yet run it over the four machines — but the sound question this row was carrying
open is closed. Worth noting how it surfaced: this file had said **"Unheard"** and she corrected it in
passing, having listened days earlier and been pulled into other repairs before she could say so. The
same class of drift as the swatch and the three stale cards, in the notes rather than in the site.

**Measuring a sound out of this piece needs the simulation frozen
first** — `requestAnimationFrame` stubbed before the page script runs. An offline audio context's
clock does not advance until it renders, so every strike the rods make while the harness is setting
up lands at time zero and swamps the note under test. Three passes were wasted on that: it shows up
as every material decaying in the same ~1.9s, which is the pile-up's tail and not the material's.

Two things went in Aug 2026 after she watched it. The **hanger sways** — the whole set hangs off one ring, so it is a slow heavy pendulum of its own, its weight mostly the rods well below the bar, and the rods then hang from a *moving* support and are swung by it. What drives the sway is drag, and **drag goes as the square of the wind**, which is her own observation in one line: at a light air the lean is a tenth of a pixel and the bar looks nailed up; at full wind it is 3° (about 8px at the bar, twice that at the rod tips). There is no threshold in the code — the v-squared law is the whole of it, so don't add one.

Underneath that, a real fault: **the swing is solved in the convention `x = tie point + sin(angle)·length`, and canvas rotates the other way.** Every rod had been drawn with `rotate(+angle)`, so the contact test was watching the mirror image of the scene on the glass — measured at full wind, the two frames disagreed about who was touching on **43% of pair-frames**, rods passed clean through each other in silence, and it chimed with a plain gap showing. Now 0%. If you ever change how a rod is drawn or hit-tested, the minus sign in `ctx.rotate(-r.angle)` is load-bearing and so are the matching signs in `rodMidWorld` and `hitTestRod`.

**And it tangled, and stayed tangled** — her report, with a photograph of two long
rods lying across each other. Two faults in one, both in the contact test.

**A rod was a POINT, not a
body.** The test compared the two rods' CENTRES, and when rods differ in length their centres hang at
quite different depths — so two rods can be lying right across one another while their centre points
are nowhere near. Measured on an arrangement of long and short rods at full wind: some pair was
passing clean through another on **96.7% of frames**, six pairs at once at worst, and the longest
tangle ran **14.7 seconds**. On the default set, where the rods are all much of a length, it never
happened once, which is exactly why it survived — *don't test this piece on the default rods alone*.
Two rods hanging in a row can only meet where they are at the same **depth**, and each is a straight
line from its own tie point, so the sideways gap across their shared depth band is linear in depth
and its smallest value is at one end of that band or the other: two evaluations find the contact
exactly. The lever arm is the distance down each rod to where they actually touch, not to its centre
— a knock near the tip turns a rod far more than the same knock at its throat.

**And the gap is
SIGNED now**, which is the "stays tangled" half. Rod i is tied to the bar to the left of rod j and
cannot get past it, but the test compared MAGNITUDES, so a crossed pair read as a comfortably
separated one and nothing ever pushed it back.

**Every pair is tested, not just neighbours**: a
long rod reaches past a short one entirely, so two rods with a stubby one between them meet at a
depth their neighbour never reaches, and an adjacent-only loop has no constraint linking them.
`touching` had to become a set of PAIRS rather than a flag per rod, or a rod resting on one neighbour
would have muted its strike against another. Interpenetration is **0%** now on both sets. It also
chimes *more*, which is the point: measured at full wind over 20s, the mixed set went from 210
oscillators to 312 and the default set from 264 to 330 — those were strikes that should always have
sounded and didn't, because the rods were passing through each other in silence.

**The hanger and
the cords are her own photographs now**, Aug 2026 — `chimerealhanger.jpg` and `chimehopefulsprite.jpg`
in her `daidle` Drive folder. What had been there was a brown gradient lozenge on two drawn strokes
with a stroked circle for a ring; it is a walnut bar on real chains off a real brass ring, and the
cords below it are real jute rope, real silver chain and a real black nylon cord.

**The hanger is cut
into TWO pieces and that is the whole trick.** The photograph carries **eight** eyelets screwed along
the bar's underside and the piece hangs **five to nine** rods, so a baked-in row could only ever be
right at one count. The eyelets are cut away into `chime-eyelet.png` and one is placed per rod, at the
tie point that rod actually hangs from — right at every count, and better than the picture, since an
eyelet is now always exactly where a cord leaves the bar. They hang clear below the wood, so lifting
them needed no repair to the bar; the cut is at y=635 of the original and not 637, because the eyelets'
stems reach two pixels into that line and left eight dark nicks along the bottom edge.

Every figure
in `HG` was **measured off the photograph** and is held in fractions of the bar's own width, so the
layout follows the picture rather than being typed. **The photograph's own proportions are shorter than
the drawn hanger was** — ring to eyelets 152px against 117 — and that is a real physical change, not a
cosmetic one: a shorter hanging assembly sways quicker, and a quicker-moving support throws the rods
harder. Measured at full wind over 20s, **636 oscillators to 684** on the default set and **696 to 828**
transposed. The **lean is unchanged**, which is what the physics says should happen — the balance point
is set by drag against gravity and not by the length — and it holds: **±4.23° before and ±4.29° after**,
over ~2,400 frames each. Measure the lean off the BAR's own top edge fitted across many columns; a
single-column probe catches the suspension chains instead and reports 18°.

**The cords are tiled, and
the tile is the whole problem.** The cord slider runs 40 to 170 against tiles of 18 to 41px, so every
cord is several repeats and a join that shows draws a ladder of rungs down the piece. Three things get
it invisible: the repeat is found to a hundredth of a pixel by correlation, the sheet's own lighting
fall-off along the run is divided out, and the ends are cross-faded. Measured on the rendered page at
the longest cord, the step across each join is **1.2 to 5.7 where the rope's own twist gives 7.9** at
its 95th percentile — the joins are quieter than the rope.

**The nylon cord was drawn pale cream and
its own swatch has always been black.** The picker showed a black glossy cord, the piece drew a
fibrous white string, and nobody had put the two side by side. The photograph settles it in the swatch's
favour.

**The rods are drawn, and mostly have to be.** A rod's length is its note — the lengths are
continuous and each material is cut to its own — so no set of photographed rods can stand in for them.
Both her parts sheets give four fixed lengths per material at **17–25px across**, where a walnut rod
wants **34** on a Retina screen; a photograph would have to be stretched to length *and* upscaled. This
was measured on both sheets, so it doesn't need measuring again.

**WOOD is the exception, and it is
hers**: *"the only thing that's not an improvement is the wood ones, the drawn wood doesn't hold up
convincingly."* She is right, and the reason draws the line for anything like it later — **brass and
silver are smooth cylinders, which shading does well; wood IS texture**, and a gradient with four grain
strokes over it reads as orange plastic. Draw what is smooth; photograph what is textured.

The way
round the resolution wall was not to use the parts sheets at all but **the hanger bar** — the same
walnut, in the same photograph, under the same light. A bar is a flat slat with the grain running along
it, lit from one edge, which is a wooden chime rod turned ninety degrees; turned that way its **126px
cross-section becomes the rod's width**, against the 34 a Retina screen wants. Four things had to be
done and each shows if it is skipped: the bar's lighting **along its own length** is divided out, or it
bands across every rod; the **evenest 420px** of the bar is used rather than all of it, measured at
0.92% residual wobble against 2.22% for the whole; the tile is **book-matched** — `[stretch | the same
stretch reversed]` — which makes the mirror join and the wrap **exactly zero** with no cross-fade and
doubles the repeat to 113px so the longest rod never shows a whole one; and **each rod carries its own
phase into that tile** (`texPhase`), because without it every rod shows the same figure at the same
height, which is the one thing that gives a tiled texture away — and rods really are cut from different
places in a plank. Quantised to 9KB from 50, measured invisible: max 14/255, and the roughness across
the grain at draw size 3.85 against 3.93.

**The wood swatch was re-cut from the same walnut** at the
same time, framed like the other three. It had been a lighter wood, matching the drawn rod: swatch
luminance 92 against the new rod's 72. Left alone that would have been the same fault as the cord
swatch — the picker showing one thing and the piece another. 75 against 72 now. The old dead `chime-rod-*.png` sprites are still on
disk, unreferenced, as warmler's unused textures are.

**Noticed while measuring and NOT fixed**: on a
240x350 screen the dock's four rows swamp the chime entirely. It is identical before and after this
change, so it is hers to find on the Jelly Star — **and she found it**: *"chimes menu overruns the
chimes"*. Two things were wrong and both had to go. At 240px a dock row is 158px wide against 208px of
room, so nothing could share a line and all six pieces stacked — **212px of a 350px screen**. Below 320
the rows give up slider length (110px to 58) and pair up: swatches+count, cord+rod, wind. **132px, three
lines.** Above 320 nothing applies and the dock is identical.

Underneath that, the real fault: the
chime is drawn in its own units off `HANGER_W`, so it was drawn **full size behind the dock**. `SCALE`
now stands between those units and the screen exactly as **gyre's board** does — everything on the page
is written in units and never learns the screen exists, and the only two places the screen comes in (a
click on the canvas, and where the length popup is put) divide and multiply by it. It never zooms IN:
measured, **1440, 1200, 600 and 390 are all scale 1.000**, and 320 is 0.928, 240 is 0.390. `hangerTopY`
is held in SCREEN pixels (`TOP_GAP/SCALE`), or a zoomed-out chime hangs under the two brass discs —
gyre's own lesson. And sideways on a 3in phone the dock is 174px of 180, so that one **scrolls**, as
kaleidoscope, storm and ant do; the rule sits at the END of the stylesheet because a media query adds no
specificity and `#dock{position:fixed}` is declared above it.

**And the chain
it hangs BY**, her ask off the first look: *"the top ring is hanging from... nothing."* It was — the cut
stopped at the ring's top and the hook chain above it was thrown away. It is back, cut from the run above
the ring **in the same photograph**, so it is literally the same chain rather than a match for it. Only
57px of it exists and one repeat is 35.30px, so there is exactly one period plus enough overlap to
cross-fade; the repeat was found by minimising the wrap rather than by correlation, which is the more
reliable objective when there is barely more than one period to look at. Step across the join **0.27x an
ordinary row-to-row step**.

Two things about it are load-bearing. It is drawn **outside the lean**,
because the ring is the pivot and does not move — so the chime swings beneath a chain that stays put,
which is what a fixed pivot at the ring means and what it looks like. And it stops **inside the ring's top
brass** rather than at the ring's centre: the ring's hole is transparent in the cut-out, so a straight run
carried to the centre shows through it and reads as a chain passing BEHIND the ring instead of hooked on
to it.

**The card was
reshot** off the rebuilt piece — the old one predated even the DRAWN hanger, showing a curved dark bar
with a knot at the top and hammered flat rods, none of which the piece has had for some time. Framed by
measuring the chime's own painted extent in the shot rather than trusting a ratio, and **cropped** to
440x640 rather than squeezed into it, which is musebox's lesson. **Reshot again** once the hanging chain
went in, at her ask, so the card shows what the piece shows — and the framing is **unchanged**, which is
her correction and worth keeping: *"there was already space above the ring. just add chain to it."* The
first attempt made room for the chain by shrinking the chime, when the card had always carried 9% of its
height as empty sky above the ring; the chain fills that and costs the chime nothing. The subject is the
RING down to the rod tips, padded 30% and nudged 3% down — the same rule as the first card, and the
general point is that adding something to a piece is not automatically a reason to re-frame its card.

**DONE — her call, 4 Sep 2026**, given for chimes and musebox together: *"barring adding my own
sounds at some point, i would consider both muse and chimes done."* This is the Done mark; the earlier
*"it sounds a great deal better"* was a verdict on the rebuilt sound and was explicitly not one.
**The caveat is a change she may still want, not an open fault**: her own recorded sounds in place of
the built ones. Don't treat it as a defect, and don't propose it back to her. **The mark does not
cover the four machines** — chimes has still not been run over them, and when it is, the rods must be
set to DIFFERENT LENGTHS or the tangle it was originally reported for cannot appear at all.
