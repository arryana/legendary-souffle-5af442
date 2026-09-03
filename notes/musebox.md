# musebox

The full record of this piece, moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short.
Everything here was written as it happened; the newest material is at the bottom. Read it before
touching `musebox/index.html`.

A **music box** — set pins on the disc to write a tune

**The look question is SETTLED**, Aug 2026. She had said *"you did a lovely job
building it, but i'm not sure it's -beautiful-"* and thought she might bring pictures from Gemini to
rebuild it from. She did, it was rebuilt on them, and her verdict on the result is ***"to my eye, yes.
yes it is."*** That closes the only thing this row was carrying open. **It is not a Done mark** — she
has not run it on the four machines yet, and that is hers to give separately.

**The rebuild, and
the hour it cost first.** Her first sheet was the assembled instrument photographed standing at an
ANGLE, so its outline is an ellipse, with pins already set in the disc and a hand across it. An hour
went on trying to repair that — fitting ellipses, cleaning the pins out in polar coordinates, cloning
a stray button off the walnut — and the result was, her words, *"weirdly oval"* and *"sad and fucked
up"*. Then she asked for **clear worded instructions for Gemini instead**, they took five minutes, and
the next set worked first time with no surgery at all. **That is the lesson and it belongs at the top
of this row: when a supplied picture is wrong for the job, say so and specify the right one. Do not
repair it.** The instructions that worked asked for four separate images, each with ONE object in it,
dead face-on, on plain pure black, nothing else in the frame — and for the disc, explicitly no pins
and no hand. The one test to apply to what comes back is: *is it face-on and perfectly round?* If it
is tilted, it is no good.

**Four assets, each of one thing**: `musedisc.jpg` (face-on, round, no
pins — kept as a JPEG and clipped to its circle when drawn, because as a PNG with an alpha cut it came
to 1.3MB, which is bowl's lesson about page weight), `museroom.jpg` (the empty room, walnut and the
same navy the case stands on), `musehand.png` (pivot found by locating its two rubies) and
`musepin.png` (one brass head from above). **The eight notes sit on eight of the disc's OWN engraved
circles** — measured, the engraving runs 117, 145, 176, 208, 240, 277, 309, 337 of a 378px radius,
exactly eight between the hub and the rim. Held as fractions of the radius, and `cellAt` finds the
NEAREST ring rather than dividing by a constant gap: real engraving is not evenly spaced and should
not be forced to be.

**The picture takes the shape of the screen**, her ask. The canvas keeps a
constant width in its own units so every measurement stays put; only its height and the disc's radius
follow. Measured: 1100x974 with a 960px picture on a desktop, 1100x1407 with a 358px picture on a 390
phone, and the disc goes from 55% of the picture's width to 88%. The table is never distorted — always
the same scale as the width — and the wall is drawn at its own scale with its top few rows stretched
to fill what is left above it, since stretching the whole gradient five times over would band it. A
3in phone and a phone sideways scroll, the answer she took for kaleidoscope and storm.

**The table was toned down**, her call on a note of mine: it was the warmest and
brightest thing in the frame and the disc is the subject, so it pulled the eye down and forward — the
same fault she named herself on musebox's white rabbit. Fifteen per cent of the saturation and twelve
of the lift come off the band below the table's front edge, and it is cooled a shade; the first two
rows are ramped so the edge does not gain a line of its own. Baked into `museroom.jpg` rather than
done per frame.

**The card
was reshot** off the rebuilt piece and **cropped** to 440x640 rather than squeezed into it — squashing
a taller frame into the card makes the disc oval again, which is the one thing the rebuild exists to
avoid. **Reframed Aug 2026** — hers: *"it's weirdly low, i don't mind there being more wood visible to
center it better."* Measured, the disc's centre sat **60% down the card** with the table a bare 8% strip
along the bottom; it is **50%** now and the disc is **exactly the size it was** (386px against 387), so
the whole change is where it sits. **What centring a circle in a 440x640 frame costs is table**, and
there is only as much table as the piece draws — the room photograph gives a band of 99 rows however
tall the canvas is, so the wood is stretched 1.53x and the wall above by the same trick the piece
itself uses when its wall runs taller than the photograph. **The front edge of the table then has to
fall into shadow**, and this is the part to remember: at full brightness the new wood was the brightest
thing on the card and pulled the eye down and forward — *the exact fault she had fixed on this piece
once already*, in the note above about toning the table down, reappearing the moment the table got
bigger. It falls to 66% at the very front, which is also what the near edge of a table lit from behind
actually does. **And a tune is pinned on it**: the disc's own default is only eight pins and reads
sparse at the size a shelf card is, so the shot seeds sixteen through `localStorage` — as the old card
had. **Stop the disc before the shutter** (`#stopbox`), or a note struck as the shot is taken leaves
its flash smeared across the card.

**The sound was not touched and neither were the controls**, her call: *"leave off the
controls, as while they're decorative, they're not standard with all the other pieces."* Gemini's
sheets carried an icon strip, a second kind of marker and an extra square button; all of it is the
generator embellishing rather than a decision, and none of it came across.

Aug 2026 it got **four voices** at her ask, the
chime she already liked plus **piano, guitar and a Native American flute**, each built from how the
real instrument makes its sound rather than from a preset. A struck string is stiff, so the piano's
partials are stretched by n·√(1+Bn²) — that stretch is most of what makes a piano sound like a piano
and not an organ — with the hammer landing underneath as its own pitchless knock. A plucked string's
harmonics are set by WHERE it is plucked, sin(nπp)/n², so the guitar has real holes in its spectrum
at the pluck's own nodes (p=0.22, an ordinary picking position). A fipple flute gives a strong
fundamental, a soft second and almost nothing above, and the half that matters is **breath running
the whole length of the note** rather than only its start — that is what makes a flute sound blown
instead of struck — with a slow attack, a chiff at the front, and vibrato arriving only after the
note has settled, the way a player's does.

**Two of the four were wrong and she caught both**, Aug
2026: *"the guitar sounds like the piano, not a guitar. the flute is okay, but sounds more like a horn
than a flute."* Both were right, and the guitar one is measurable to the point of being embarrassing —
**its harmonic profile was very nearly the piano's**: second partial 0.323 against the piano's 0.344,
third 0.122 against 0.175. Built from the same parts in the same way, the only thing separating them
was which partials were loud, and they were barely separated on that either. What actually tells a
pluck from a strike is three things, and this had none of them. **A plucked string does not fade
smoothly** — it vibrates in two planes that bleed into the bridge at different rates, so it drops fast
and then hangs on, where one smooth exponential over 2.2s is a piano's shape exactly. **A guitar is a
box**, and there was no box at all: no air resonance in the belly, no soundboard. **And the brightness
should collapse** — the high partials go in a fraction of a second while the fundamental rings on, and
they were fading at much the same rate, which reads as sustained. Measured after: second **0.211**,
third **0.067**, and the note's whole tail 1.29s against the piano's 1.57.

The flute's fault was
one number. Its second partial sat at **0.236** of the fundamental, a quarter of it, which is squarely
a horn; a duct blowing across an edge is very nearly a pure tone. **0.100** now, third 0.085 -> 0.025.
Two things underneath that are worth keeping. **The breath was doing the harmonics' job**: band-passed
at 2.1x the note with a tight Q it sat right on the second harmonic and reinforced the very thing that
made it a horn — it is at 6.2x and much broader now, so it is air rather than a pitched partial. And
the note got **a slow waver in loudness** as well as in pitch, since an amplitude that sits perfectly
flat is most of what reads as blown-by-a-machine; it **multiplies** the note rather than being added to
it, because added, the waver's own offset kept the gain off zero and the note could never actually
end (measured, its tail ran from 0.78s to 1.04 and would have gone on).

**Levels were re-checked
against the waveshaper, not just by ear.** The guitar's body peaks alone took a single note from 0.67
to **1.11** — into the limiter on its own, which is the one thing that shaper exists to avoid — so the
string's amplitude came down to 0.62 and a note now peaks at 0.641. The flute is the opposite trap: a
near-pure tone sums far more coherently than a complex one, so eight of them on one step rode the
ceiling for **1649 samples** where the old busier flute rode it for 994. At a fundamental of 0.44 it
is **865**, under the sound it replaces. Peaks stay at exactly 1.0 with nothing over on all four
voices.

**AND THEN SHE MOVED THE GUITAR INTO THE PIANO'S SLOT**, Aug 2026, which is the most
useful thing that happened to this piece's sound: *"the guitar now sounds like a much better piano.
the piano sounds like a synthesizer."* Both halves right, and the second the worse fault — so rather
than throw away a sound she liked, it took the slot it suited. Her instruction was *"whatever you do,
please use the current guitar for the piano going forward"*, and it went across **unchanged**. It is
deliberately NOT piano-ified: inharmonic partials, a longer ring and a felt thump instead of the click
are all the obvious next move and all of them would change the sound she just chose. Don't, unless she
asks.

**The real diagnosis was underneath both halves of that sentence, and it is the general
lesson: adding sine waves together is the right way to build a thing with a few MODES, and the wrong
way to build a STRING.** The chime is three bending modes and the flute is very nearly one tone, so
both are honestly built that way. But what makes a string a string is that its whole spectrum darkens
*continuously* as it rings, and with sines that has to be typed in rather than happening. Measured,
that is exactly what was absent: the old guitar's brightness ran **443Hz at the strike down to 264,
against a fundamental of 262** — very nearly a pure tone from the first instant, with no bite at
**all**. That flat, dark, perfectly smooth thing is what a synthesiser sounds like, and it is why both
voices read as one.

**So the guitar is a real string now.** A wave travels along it, reflects off
the bridge and the nut and comes back a little duller each time: a delay line one wavelength long, fed
back through a filter that takes the top off. Every harmonic and the entire brightness collapse fall
out of that for nothing, because it is what the object does. **The string is there TWICE** — a real one
vibrates in two planes at once which bleed into the bridge at different rates, and that is where a
plucked note's double decay and its faint beating both come from; one loop gives neither. Measured
after: **2043Hz down to 427**, rings 3.4s at C4, 2.2 at G4, 1.3 at E5.

**Web Audio cannot do this
live and that is a hard limit, not a preference**: a feedback loop through a `DelayNode` is stuck at
128 samples minimum, which is 2.9ms, so the highest note it could tune to is 344Hz. The box only ever
plays eight notes, so each string is worked out once and kept. That turns out to be the CHEAPEST voice
of the four to play — at 6x slower than a desktop the worst frame gap with the guitar chosen is
**188ms against the chime's 235**, because eight buffer sources are lighter than eight stacks of
oscillators. One string costs 149ms to make on that processor and eight cost 367, so only the note
being played is waited for and **the rest are made one at a time behind the running piece** — bowl's
and fireflies' bargain, for bowl's and fireflies' reason.

**Three things went wrong building it and
every one would go wrong again.** (1) **It came out 13 to 54 cents FLAT** — 54 being more than a
quarter-tone, which on a box tuned to real notes is the one fault that cannot stand, and the same fault
chimes' whole row is about. What sets the pitch is the WHOLE LOOP and the loop filter has a delay of
its own, `(1-br)` of a sample; leave it out and the note is flat by more the higher it goes. Within a
cent on all eight now. (2) **Seeded with noise it was a banjo.** The textbook plucked string is
demonstrated with a noise burst, which is a flat spectrum, leaving only the comb the pluck point cuts
to shape it — measured, the **third partial came out 2.94x the fundamental**. The pitch was still
right and the ear still heard C4; it was simply thin and nasal. A real pluck pulls the string into a
**triangle** with its corner at the finger and lets go, and that shape's own spectrum is
sin(n·π·p)/n² — the holes AND the steep fall, from one shape, because it is what the string is doing.
Now [1, 0.26, 0.11, 0.02]. (3) **And then it was too dull**, because a triangle falls away as 1/n²:
brightness 599Hz where a pluck wants nearer 1500. The bite of a pluck is **not the string** — it is the
nail or pick leaving it, a scrape heard directly, so it goes in FRONT of the note rather than into the
loop. Attack **3179Hz**.

**The honest limit on all of this: these were tuned by measurement because
I cannot hear them, and she can.** Every figure above says the guitar is now a string and not a stack
of sines, which is a real and checkable claim; whether it sounds like a *guitar* is hers alone, and
this was handed to her as rendered audio rather than as a chart for exactly that reason.

**Measuring these needs the functions pulled out of the file at test time** rather than
re-typed into a harness, or the harness and the page drift apart and the figures stop meaning
anything; and an `OfflineAudioContext`'s clock does not advance until it renders, so everything
scheduled at `currentTime` lands at zero together — which is what makes the eight-note pile-up easy to
measure and single notes easy to get wrong.

The icons are **drawn, not emoji**, deliberately: the
only flute emoji arrived in 2022 and a Kindle Fire would show an empty box where it should be.

**The
rabbit is grey.** Her call — white was the brightest thing on the page, brighter than the disc or the
brass, so the eye went to the tempo control before the music box. **It was greyed with a CSS filter and
that did not hold**: her report off the Windows tablet, *"the rabbit is still white"*. Windows draws
emoji as colour glyphs and will not put a filter over one, so the fix worked on the machine it was
written on and nowhere else. **The tortoise and the hare are drawn now**, in the same stroke and the
same `currentColor` as the four instruments beside them — which is the very reason those were drawn.
The general rule, and it is stronger than the site's usual emoji-over-text preference: **if an emoji's
COLOUR matters, it cannot be an emoji.** A filter over a colour glyph is a fix that only works where it
was written.

**And it was clipping.** Eight
rings can be pinned on one step, and eight notes together measured nearly **three times full scale**,
1.2% of samples squared off flat — a buzz over the note, and present long before the new voices. A
`DynamicsCompressorNode` is the obvious answer and is the WRONG tool: ~6ms of lookahead and gain
riding left the chime **silent for its first 5ms** where the live page is already at 93% of peak, and
moved the peak from 6ms out to 74. That is not a level change, it is taking the strike out of a
struck instrument — and it is only visible if you measure the attack envelope rather than the peak. A
**waveshaper** has no lookahead and no attack or release at all: this curve is exactly y=x up to 0.75
and bends only above it, so a single note passes through sample-for-sample unchanged and a pile-up is
rounded instead of squared. Eight notes now peak at exactly 1.0 with **zero** samples over, on all
four voices, and the chime's attack envelope is unchanged (peak at 5.8ms before and after).

The
page also **grows to its own content now**, as kaleidoscope does: the instrument row put the last 26px
of controls off the bottom of a 3in phone that could not scroll to them. Desktop, an ordinary phone
and a Kindle are unchanged and do not scroll.
