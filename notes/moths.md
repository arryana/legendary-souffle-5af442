# moths

The full record of this piece, moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short.
Everything here was written as it happened; the newest material is at the bottom. Read it before
touching `moths/index.html`.

**Moths** losing their bearings on a hanging bulb. Not attraction — a moth holds a course by keeping a distant light at a fixed angle, and a near one wraps that course into a spiral. Three sliders: dusk→dark, bulb, how many. Colour is a readout of depth (dark in front of the glass, pale behind), from her own three-shade cut

Built Aug 2026 from her brief, then put right by her own watching of it — she found that the moths crowded the bulb and stayed (an absorbing state: all five reached it and none ever left), that moths in front of the lower glass came out grey rather than black, that they all flew alike, and that they never tilted or wavered. In **natura**, which is therefore a shelf of four

**The three shades were a straight line and should not have
been**, her correction Sep 2026: *"i meant for them to be white when they're 'behind' where the light
would cast brightly, and only black when between the viewer and the bulb. grey denotes distance from
the bulb and when to the front-but-side-not-quite-full-silhouette for black."* Three separate rules,
and one straight line from black to white across the sphere could serve none of them: a moth behind
read the same whether it was half a bulb-height out or three, because **there was no distance term at
all**, and the front was a plain ramp with no notion of what it was seen against.

**The first
attempt got the front backwards and she turned it down on sight.** Reading "only black when between
the viewer and the bulb" geometrically gives a narrow cone — the glass is 0.2 of a bulb-height across
— so the front was made to stay grey over most of its arc and blacken only near the axis. Shown a
moth at the bulb's shoulder rendered grey, her answer was ***"the one on the left is truer to the
human eye"*** — the left being the old straight line, which had it black. Then the reason, and it is
the whole of this piece's colour: ***"a person's eye is blinded to color when it's looking at that
much light, so even a partially-in-front-of looks black. but a moth at a distance -behind- the bulb
looks as grey as one close and to the side."***

**So the dark side is GLARE and not geometry, and
glare is measured on the SCREEN.** It is a thing the eye does with the picture, not a thing that
happens in the room: how far the moth is from the filament in pixels, against a radius that grows
with the bulb, so a lamp turned down dazzles nobody. Anything in front of the bulb anywhere in that
glare goes to silhouette; the same moth out in the dark sky is only a grey shape. **And the lit side
is DISTANCE**, falling to *nothing* rather than to a floor, because at nothing it is mid grey, which
is exactly what a moth at the side reads — her sentence, implemented literally. Measured on the
running piece: **behind and close 0.87 -> 0.90** (whiter), **behind and far 0.91 -> 0.71** (greying
out with distance), **in front and in the glare 0.28 -> 0.18**, **in front but out in the dark sky
0.22 -> 0.20** (all but unchanged, which is the point), and the sides unmoved at 0.5.

**Both
halves are scaled by how far round the moth is, and that is load-bearing.** Without it the glare
arrives at full strength the instant a moth crosses the bulb's own plane and the shade snaps from
0.50 to 0.12 in a single frame — a flicker, at the moment it is most watched. Written this way the
two branches meet at exactly mid grey and cannot do otherwise.

**The distance falloff is a square
law, not an inverse square**, which is a departure from the flight model beside it and was chosen by
looking: an inverse square does nearly all of its falling inside the first bulb-height, so it greyed
the moths in the thick of it — where she wants the white — and still had half its lift left at the
far edge, where she wants grey.

**And the shading was in ELEVEN STEPS**, her other question the
same evening: *"can it darken and lighten more than those shades? so it's a smooth transition?"* It
could not, and the cause was a cache — the tinted frames were kept in eleven levels, a jump of **25
in 255** at every one, which on a flat silhouette is a tread rather than a gradient. There are never
more than five moths on screen (the count slider stops at five), so each is tinted on the frame it is
drawn and the shade is exact. **Tint at the FRAME's own size, not at the size it will be drawn**: the
obvious saving is to tint small, and it is wrong twice over, because the sprite is then resampled
down before it is rotated and the main canvas is at the screen's own device pixels — measured **146
of 255** different along the wing edges at the drawn size, and still 110 at twice it. Measured, that
saving was inside the noise anyway: at a Kindle-shaped screen with the processor six times slower,
13.5fps before and 14.0 after; on a desktop, 60.1 both. Only at a 2200x1520 canvas *and* six times
slower did it cost about a tenth, which is a machine that does not exist.

**Comparing two builds
of this piece needs the randomness and the clock both seeded**, or the moths are simply somewhere
else in the two pictures and nothing can be read off them — fireflies' lesson. Seeding `Math.random`
and driving `requestAnimationFrame` off a stubbed `performance.now` puts the same moths in the same
places in both, and a pixel diff over the whole frame then shows only the colour.

**WHAT IS BEHIND THE BULB IS SEEN THROUGH THE GLARE; WHAT IS IN FRONT IS NOT.** Hers, Sep 2026:
*"there are still white moths flying 'in front' of the bulb."* Her quotes round *'in front'* are the
whole report, and the measurement says she was describing an appearance rather than a miscolouring:
**nothing actually in front is ever pale** — the brightest shade any moth with z<=0 reaches is
**0.483**, below mid grey — so the silhouette rule works exactly as written. Every pale moth she was
looking at was **behind** the bulb, and all 138 pale samples sat **within one bulb-height of the
filament on screen**, the brightest of them right on it. They are correctly shaded and they read as
being in front, because nothing in the picture says otherwise: the bulb's opaque glass only reaches
**0.084–0.232 bulb-heights** from the filament depending on direction, so a moth just outside that is
beside the bulb with no occlusion to place it — and **the shading alone cannot carry depth, because a
viewer does not know the rule.**

The missing cue is the one the eye actually uses, and it is the glare already written here for the
front: **a moth behind the bulb is seen THROUGH the dazzle and one in front is not.** So the glare
veils it, and how much goes with how **pale** it is — near a light that bright the eye keeps only the
strong contrasts, so a black moth stays a hard silhouette and a pale one is swallowed. That is why,
in life, the moths in front of a lamp are crisp black shapes and the ones behind it can barely be
made out. Scaling by the shade is not a tuning choice but what makes it **continuous**: at the sides
both branches are mid grey, so both take the same veil and there is no seam where the two rules meet.

Measured, how far a moth stands out from its surroundings (peak difference, 0–255):

| | glare | now | after |
|---|---|---|---|
| pale moth behind, right at the bulb | 0.60 | 198 | **113** |
| pale moth behind, a bulb-height out | 0.27 | 210 | 168 |
| pale moth behind, out in the dark sky | 0.16 | 219 | 193 |
| **black moth in front, right at the bulb** | 0.60 | **46** | **46** |

So it falls away with the glare, her *white when behind* survives out in the dark, and **the
silhouettes she ruled on are untouched**. `GLARE_VEIL=0.75`, chosen by rendering the same frozen
frame at 0.60, 0.75 and 0.90 and looking — at 0.90 the moth greys enough to start arguing with her
own rule. Frame rate at 6x slower with five moths **14.1fps**, against the 14.0 recorded above.

**Two wrong hypotheses were measured and dropped before this one, and both are worth not repeating**:
that a translucent bulb was letting moths show through it (its glass is **78.8% fully opaque**, and
the draw order is already behind → bulb → in front), and that the moth was drawn **brighter than the
bulb** (it peaks at **193** against the bulb's 255, so it is not).

**AND THE NEAREST FEW ARE HELD BACK**, hers, Sep 2026: *"the largest 'closest' moths are a bit too
big. instead of being clear they're a bit jarring."* Both halves are right and the measurement says
so — size really does track distance from the eye (**-0.88** in log terms) and the biggest-drawn tenth
really **are** the nearest tenth (61% overlap), so the readout works and it is the **amount** at the
top that overshoots. Over 60,000 samples a moth's drawn height runs 18px at the far end, **32 at the
median, 44 at the ninetieth** — and then the tail runs away to **97px, nearly a quarter of the bulb's
own height and three times the median**, when one strays to 2.13 bulb-heights from the eye where the
bulb sits at 5.2. It happens about **1% of the time**, which is exactly why it reads as a lurch rather
than as depth: rare, sudden, and far bigger than anything else on screen.

Standing further back (raising `FOCAL`) was measured as the alternative and is the more obviously
physical move, but it is much blunter — it compresses the whole range, weakens the depth readout
everywhere, and moves where every moth lands, to fix a 1% tail. **This is fireflies' soft ceiling
instead**, in the same shape and for the same reason: exactly y=x below the knee, so the median and
the ninetieth come back **unchanged at 30 and 39px** and only the excursions bend
(`NEAR_KNEE=1.15, NEAR_CEIL=1.55` on `q`). Measured after: biggest **73 → 55px** on the same sample,
**nothing at all over 60px** where 1.04% of the time was before, and size still tracks distance at
**-0.862** against -0.881. On the staged worst case, the near moth goes **81 → 51px** and the far one
is **22px in both**. Frame rate at 6x slower with five moths 13.5fps, unchanged.

**Don't reach for the `Math.max(0.35, ...)` clamp thinking it does this job** — it is there to stop a
divide by nothing and is never reached; the closest any moth ever came in 60,000 samples was 2.13.

**And don't trust a short sample for this.** The first run of 9,000 samples reported the biggest moth
at 52px and a 2.6x spread, and was simply too short to catch the tail — the real figures are 97px and
5.4x. The excursions are what she is complaining about, and they are precisely the part a quick
measurement misses; she had been watching it, which is why she saw them.

**Size shows how
far a moth is from the EYE, and it cannot show how far it is from the bulb** — her follow-up was
*"can you also alter the size of the moth on a scale to show its distance?"*, and the honest half of
the answer is that no perspective can do it: a moth far from the bulb is as likely to be right up in
front of you, where it is drawn huge, as at the back, where it is tiny. Two things were done that
could be. **The drawn size is the moth's true distance from the eye now, not its depth alone**: the
eye sits FOCAL bulb-heights this side of the filament, so a moth three out to one side is 6.0 away
where one at the bulb is 5.2, and a moth that far off the axis is also turned that far from square-on
and foreshortens by about as much again. Depth alone had the sign **backwards** — measured, a moth
further from the bulb was drawn slightly *bigger* (correlation **+0.11**); it is **-0.11** now. And
**the moths' own size spread was cut**, 0.70-1.36 to 0.80-1.22, because that spread was 0.191 in log
terms against distance's 0.176 — so how big a moth looked said more about which moth it was than
about how far away it was, and size could be read as neither. It is 0.122 against 0.176 now, and
distance leads. **The wingbeat's spread is untouched**: bigger wings beat slower, so beat used to be
worked back out of the size, and it is taken from a `heft` of its own now — narrowing the drawn size
would otherwise have flattened the beat with it. If she ever wants size to be *purely* distance, the
dial is that spread and taking it to nothing costs the moths being different animals.
