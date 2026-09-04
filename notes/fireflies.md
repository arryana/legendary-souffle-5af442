# fireflies

The full record of this piece, moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short.
Everything here was written as it happened; the newest material is at the bottom. Read it before
touching `fireflies/index.html`.

A field at dusk where you place fireflies in the grass; real dusk-to-night sky, with bats about

**It was fetching all seven sky photographs on load — 7.6MB — which is bowl's fault at half bowl's
size**, and the general lesson bowl's row records: a sweep that only looks at where things land
cannot see megabytes queued in front of the piece. Only the stage the darkness slider is sitting on
is asked for now, and its neighbour for the cross-fade; the rest come in behind the running piece
**one at a time**, nearest-first, because seven at once is worse on the machine already struggling.
Moving the slider to a stage that has not arrived asks for it at once, and until it lands the
nearest stage that HAS arrived is shown — never the flat stand-in. Measured on a simulated Jelly
Star (240x350, CPU 6x slower, 1.6Mbps): the real sky is up at **11.4s having fetched 2.1MB, against
30.4s and 3.1MB in flight before**; the other five follow at 21.8, 26.8, 32.0, 37.5 and 43.0s. Only
cross-fade when BOTH stages are really present, or it dissolves between two skies that aren't
neighbours.

**THE SEVEN SKIES WERE TWO DIFFERENT PLACES**, her catch, Aug 2026: *"it should be the
same picture across all of them, just at varying stages of night."* She was right and it is
measurable — on the land alone, stages **0–3 agreed with each other at 0.99 and with 5–6 at 0.13**,
with stage 4 matching neither properly. So dragging the slider past about two thirds made the trees
pick themselves up and move: not night falling on a place, a cut to somewhere else. And it was not a
clean progression either — brightness ran 59, 58, 33, **41**, 23, 23, 15, so **stage 3 was brighter
than stage 2** and pushing toward darkness made it lighter at one point.

**Rebuilt from four
photographs of ONE field**, two of them hers shot to order the same afternoon (`fireflyfix1.jpg`,
`fireflyfix2.jpg` in her `daidle` folder). The brief that worked is musebox's lesson applied — *don't
repair a wrong picture, specify the right one* — and rather than ask for seven consistent frames
(which is what failed at nine for chimes) she was sent the three good existing frames as a
**reference** and asked for the same view at full night. Then, unprompted, the deep-twilight one as
well, which is the moment that cannot be derived: the glow still on the horizon while the first stars
are already up. **Verify a frame like this by searching for the best alignment of the treeline** —
fireflyfix1 came back at 0px across and 0px down, fireflyfix2 at 2px, against 0.13 for the wrong
field. Do it at FULL resolution: a coarse 480x300 comparison reported 8px of shift that was not
there.

The seven stages are eased blends between the nearest two anchors, then graded so the ground
falls at **every** step: 39.5, 30.1, 23.1, 18.2, 14.2, 10.5, 7.0. **The grade is a gamma and not a
multiply, deliberately** — a multiply dims the stars as much as the sky, where a gamma deepens shadows
and mid-tones and leaves bright points alone, which is what a darkening sky really does to a star
field: the stars do not dim, they emerge.

**And they are JPEGs now**, because a night photograph is
exactly what JPEG is for: **6.92MB to 0.70MB**, on the piece that was the slowest of the eight to
appear. Measured on the simulated Jelly Star it now shows in **2.1s having fetched 0.37MB, against
10.8s and 1.13MB**. Banding is the risk in a dark gradient and was checked — the longest run of one
identical value across a sky row is 12px of 963. The old PNGs are deleted (two of them were the wrong
field) and are in the history if ever wanted.

Its five sliders were **3, 4, 5, 19 and 20px** under a thumb — the wind one had no
rule at all — and are now 21–30. Its two tickboxes at 14px and its location flag at 25x18 were left
small in that pass and **were grown on 31 Aug 2026** by `tools/touch-buttons.js` (*"Thumb-sized
targets on fireflies and kaleidoscope, verified invisible"*). Re-measured on a simulated touch phone
4 Sep 2026, the invisible targets are **bats 42x43, the flag 43x43, no-sound 36x41** against a
thumb's 44 — the painted controls are untouched at 14px and 25x18. **The no-sound box is at its
limit rather than neglected**: the 🔊 beside it takes the taps on its right and `#batCtrl` bounds it
on the left, which is the generator's own rule (each control reaches only half the gap to its
neighbour). The only way to the full 44 is to make the 🔊 part of the control, so tapping the speaker
mutes — a change of behaviour, not a repair, and hers to ask for. **The sentence this replaces said
both were unrepaired, and was three days out of date when it was written up.**

**And it is
one of the two that slow down on a Kindle-speed processor**: 60fps normally, 58 at 4x slower, **43
at 6x**. moths is the other, and worse. **THAT IS NO LONGER TRUE OF FIREFLIES, and the reason is worth
keeping** — Aug 2026, found by leaving it running rather than by looking at it. **The sky was being
composed from scratch on every frame to produce a picture that had not changed.** `drawSkyPhoto` drew
a full-size photograph scaled to the screen sixty times a second, and whenever the darkness slider sat
BETWEEN two of the seven stages it drew a **second** one over the top with an alpha — while `dark`
only ever changes when a hand moves the slider. Measured at 6x slower with nothing placed: squarely on
a stage **44–50fps**, anywhere between two **24–27**. Half the frame rate, and "between two" is nearly
the whole slider — **including its default of 66**, so every visitor landed on the slow path without
touching a thing. It is composed into its own canvas and blitted now: **59.6–60.1fps at every position
on the slider**, and still 58.5 with forty-five fireflies placed. The scaling and the blend happen once
per slider move instead of once per frame.

**This also settles the 43-versus-25 puzzle in the
paragraph above.** Both figures were honest and they were taken at different slider positions — one
landing on a stage, one between two. If a frame-rate figure is ever recorded for this piece again, say
where the slider was.

Two things about the cache are load-bearing. The key covers the screen size,
the DPR, the blend fraction **and which photograph is standing in** — the backfill swaps stages in as
they arrive, and without `base.src` in the key a stand-in sky would stick after the real one landed.
And it is drawn at `W*DPR` with the same `setTransform` the main canvas uses, or a Retina screen gets a
soft sky. Verified pixel-identical to the old drawing at darkness 0, 25, 66 and 90: **0.000% of sky
pixels differ by more than 2/255, worst 0**. Neither freezes; both read as less smooth.

**They
flew in the grass, in formation, and all on the same beat** — three faults, all hers, Aug 2026, found
by her watching it and none of them visible in a screenshot.

*"is it my imagination or do they stay
really low?"* It wasn't. `altFrac` runs 0 at the ceiling to 1 at the ground, the top of the near grass
sits at **0.45** of that band, and the preference was 0.58 at the default darkness — so the whole
population cruised **below** the blades. Measured by reading the fireflies' own positions out of the
running piece: **11.3% were above the top of the grass** and the median sat 65px inside it.

**And
the flash fired at the bottom of the dip**, though the line of comment above it said "flashing partway
up out of it". `sin(0.55·π)` is 0.988 — 99% of full dip. The swoop takes 2.2–3.4s and the light is
spent in about half a second, so weighted by brightness the firefly sat **72% of a dip below its
cruising height the whole time it was lit**, about 29px. At 0.78 that is 25%, ~10px, and the climb
while lit goes from ~9px to ~21px, so **the J gets deeper, not shallower**. Share of LIT fireflies
above the grass: **16.5% → 26.6% from the altitude alone → 57.0% with both.** Don't go past ~0.85 or
the light arrives after the climb is over.

**Her call on the height, off four rendered options:
the highest.** The ceiling went `horizonY()-55` → `-130`, so they can rise against the sky. That is
hers and it is not unfaithful — species differ, and the ones that flash up among and above the trees
are real; she had already confirmed the low flying itself is true to life, so what moved is the
ceiling, not the idea.

**"they all seem to be in such formation. real fireflies dip and loop and
wander."** Three causes, all shared state. Every firefly had **one preferred altitude with a narrow
uniform wobble**, so they stratified — and once the preference sits near the ceiling a symmetric
wobble CLIPS, and the clamp piles everyone who would have gone higher onto exactly one line. It is a
soft-edged spread now (three randoms averaged), **reflected** off the ceiling and floor rather than
clamped; **don't put the clamp back, the pile-up is the formation.** `steerPhase` advanced at a fixed
**0.5 for every firefly**, so the whole flock turned on one beat — per-firefly now, with its own turn
strength, big enough that `vx` reverses, which is what makes a loop. And the vertical was a single
slow sine plus a small fast one — a wave, which is what reads as mechanical — so it carries a second
sway at an unrelated rate (the two never come back into step) plus an **idle dip** every few seconds
that sometimes climbs instead. Measured over 30s per firefly: **own vertical range 74px → 173px**,
doubles back 4.0 → 5.3 times a minute, highest reached 68% → 46% of the page.

**Measuring this
needs the fireflies read out of the page, not off the pixels, and that cost three wrong answers.**
Counting bright blobs in screenshots put the share above the grass anywhere between 12% and 38% for
the *same* build — the population's own random spread swamps the effect — and on that evidence the
flash fix was first reported as working, then as not working. A one-line `window.__probe` in a
throwaway copy gives exact positions and settles it. **Two traps in doing that**: `cp -al` hard-links
the file, so editing the "copy" edits the real one (it did); and keying a trail by its index in
`males` draws a straight line from one insect to another whenever the array is spliced — key on the
object.

**AND THERE WAS NO INSECT BETWEEN FLASHES AT ALL**, which is her sharpest catch on this
piece and the plainest fault: *"you can more or less predict where they're going to light up next. at
dusk there's just a hint of a silhouette of them between flashes. but there's no.... path."*
`drawMales()` called `drawFlash` and nothing else, so a firefly existed only while lit — every flash
arrived unrelated to the last, and the anticipation, which is most of what makes watching them
enjoyable, could not exist. `LIGHT_FLOOR` was meant to leave one "just barely visible" and rendered at
about **3/255**. The insect is drawn now, and **which of the two things carries it depends on how much
light is left in the scene, which is what keeps it honest rather than a marker**: a dark speck —
the body, not a glow — strongest at dusk against a sky that still has light in it, weaker below the
horizon where it is against dark ground, and gone by full night, because at full dark you really
cannot see one between flashes; and the ember lifted to 0.07 for what is left after that. Measured at
dusk, an unlit firefly stands out from the sky by **~17/255** against nothing before.

**This one is
not provable from a screenshot and three attempts at a before/after picture were misleading** — the
two builds put their fireflies in different places, other insects wander into a close crop, and a
still cannot show *following* something. Don't try to settle it that way. The useful number is that a
firefly covers only **50px between one flash and the next** (112px before the wander work, so that
change helped this rather than hurt it): there was never much ground to cover, and the only question
was whether anything was there to see.

**HOW it lights, which is hers off the machines**: *"do
they only light up when traveling upward at the same angles?"* and then *"real ones light going up,
sometimes at a total hover, and sometimes going down"*. Both halves were right and the first was a
side effect of the flash being moved to 0.78 — there the rise is near its fastest (18–62px/s) while
`vx` is capped at 26, so the vertical dominated and **77% of flashes went within 30° of straight up**.
Two things fix it. The **J leans**, its own size and direction per firefly (`swoopLean`), added as a
velocity rather than an offset so the position stays continuous when the swoop ends — that tilts the
gesture without touching how HIGH it happens. And the flash now picks one of three ways: **rising**
(the J, the common one), a **total hover** with no swoop at all so the only vertical movement is its
own drift, or **on the way down** into the dip. Measured: **69% up, 12% hovering, 19% down**, against
99% up before, with the lit share above the grass unchanged at 99%. The flash keeps its own clock
(`flashT`) rather than the swoop's, because a hovering flash has no swoop running.

**Her verdict on
the whole of it: *"that's much, much, much better."*** Not a Done mark — she has not run it over the
four machines — but the piece is where she wants it. **And the general lesson of the day is in how
these four faults were found: every one of them came from her sitting and watching, and not one would
have shown in a screenshot or a sweep.** The measuring was worth doing — it proved each fix and caught
several of my own mistakes, including one I had introduced myself — but it kept pointing at the wrong
thing until she said what was actually wrong. A session that only measures will conclude this piece is
fine.

**THE TOP OF EVERY FLASH WAS WHITE**, hers, Sep 2026: *"when the firefly starts
flashing, the glow gets brighter than a real one does."* She was right, and the fault was the
renderer's rather than the model's. `drawFlash` lays down two layers with `lighter` — a glow and
a small hard lantern on top of it — and at full output they sum to about **1.9x what a screen can
show**. Everything past 255 is thrown away, and the first thing thrown away is the blue channel's
headroom, so the flash **lost its colour before it stopped getting brighter**. Measured over 200-odd
flash positions on ordinary sky (stars excluded — anything laid on a star clips whatever you do):
at the default darkness **67.6% of flashes clipped to pure white and at full night 100% did**, mean
blue 249 and 255. A white spark, where a real lantern is yellow-green at any brightness it reaches.

The fix is **musebox's waveshaper in another medium**, and for the same reason: a soft ceiling with
no lookahead, exactly y=x below the knee so everything she has already tuned down there passes
through untouched, bending only near the top (`KNEE=0.15, CEIL=0.44`). It is applied to the
**output** (`alpha*skyDim`) rather than to alpha, so it bites where the render is actually near the
ceiling and barely at dusk, where the sky is doing half the dimming already. The ember between
flashes (`LIGHT_FLOOR`) and the females' resting pulse both sit below the knee and came back
**byte-identical** — her tuning of those is untouched, which is the whole reason for a knee rather
than a scale factor. Clipping **0% at every position on the darkness slider**, mean blue back to
157-169.

**And it gave the swell back, which nobody had noticed was gone.** The flash's envelope rises to
full over 0.13s, but at full night the render already read **250 at alpha 0.60 and 255 at 1.00** —
so the top 40% of every flash was invisible and it **snapped on rather than growing**. Measured
after: 151, 181, 195, 204 across the same span, rising the whole way. Worth keeping as the general
point: **a piece that clips is not merely too bright, it is losing the top of whatever it is
doing** — the colour and the gesture both. Check any additive `lighter` glow on this site for it.

**A PERCHED FEMALE IS SEEN THROUGH THE GRASS, NOT OVER IT**, hers, Sep 2026: *"can you dim
the ones that are placed, in the grass? those are usually dimmer because they're not on top of the
grass."* That is a mechanism and not a level — a male flashing above the sward has nothing between
him and you, a female down among the blades has all of it — so it is keyed off **how far down the
meadow she sits** rather than a constant: near the bottom of the frame she is a few feet off with
sparse near blades in front, up by the horizon there is a whole field of it. Transmission runs
**0.68 at the horizon to 0.88 at the front**. The males are deliberately untouched: they fly above
the grass by design, that height is hers and set over several reports, and there is nothing in
front of them.

**The two numbers were chosen against the RENDER and not against the arithmetic, and the gap
between the two is the thing to remember.** `drawFlash`'s radius carries alpha in it — her own rule
that *"the size and the brightness are the same thing happening"* — so dimming a glow **shrinks**
it too and the visible loss compounds. The first attempt used 0.42–0.70, which sounds like a dim
and measured like an extinction: the resting glow, which is the whole of what you see when you put
one down, fell to **0.28–0.49 of its peak and 0.14–0.44 of its lit area**. Swept at one spot, the
resting glow renders at 0.86 of its area at 0.90 transmission, 0.71 at 0.85, 0.53 at 0.75 and 0.19
at 0.50 — so a factor read off the physics alone costs far more than it looks like it should.
At the numbers taken: resting glow **peak 0.52–0.78, area 0.47–0.71**; her answering flash, being
much brighter to start with, **peak 0.88–0.95, area 0.61–0.88**. Anyone retuning this should sweep
it and read the rendered figures.

**And it is floored well above nothing on purpose**: a placed firefly that cannot be found reads as
a firefly that was never placed, which is the *reads as broken* class, not fidelity.

**Measuring this needs the glows rendered directly, not read off the running piece** — three passes
were wasted before that. A box around a placed female catches whatever is behind her (a star can be
brighter than she is, and the far field is brighter than the near), and males and bats fly through
it: one pass reported the far glow *brighter* than the near, another reported a female 8.9x brighter
after a change that only dimmed her. Call `drawFlash` at the exact alphas `drawFemales` would use,
on a cleared sky, and diff against the same box with nothing drawn.

**WHY THIS PIECE IN PARTICULAR, and it should be read before touching it.** Aug 2026,
unprompted: ***"i really miss fireflies, living in scotland. it's nice to have digital ones. it
matters to me a lot that they're... authentic feeling."*** There are no fireflies in Scotland. This
is not a decorative toy and it is not a simulation exercise — it is a substitute for something she
cannot go outside and see, and the fidelity is the entire value of it. That is also why her reports
on it are so exact: she is not imagining what a firefly does, she is remembering one. *"like a model
train track"*, *"they're just black specks with a glowing end"*, *"barely see one at twenty feet in
the early dusk"* — every one of those was a correction to something measurably wrong, and none of
them could have come from the code. **Treat what she says about how they behave as the primary
source, and the measurements as the way of proving you have implemented it, never the other way
round.**

**Her verdict at the end of that evening: *"perfect. it's perfect."*** **It is NOT a Done
mark** — she has still not run fireflies over the four machines, and only she gives that. What it
settles is the look and the behaviour, after a rebuild done entirely on her reports: the height, the
flash timing, the scatter, the per-firefly rhythms, the turning radius, the round speck, the crab,
the surge, and the transparency ladder (0.55 solid → 0.46 → 0.34 translucent → **0.17**, each step
hers). If a later session is tempted to adjust any of it on the strength of a measurement, that is
the thing to weigh it against.
