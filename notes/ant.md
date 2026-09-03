# ant

The full record of this piece, moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short.
Everything here was written as it happened; the newest material is at the bottom. Read it before
touching `ant/index.html`.

Ants

Swept Aug 2026 before her device testing, and two things were repaired. Its **seven
sliders were 3, 7, 9, 14, 18, 18 and 23px** under a thumb — the worst on the site — because the
touch-target generator had been compounding its own output; with that fixed they are 26–33.
And **turned sideways on a 3in phone it lost the top of its own dock**: 180px of screen against a
282px dock, with count, speed and light sitting ABOVE the top edge on a page that could not scroll
to them. It scrolls there now, which is the answer she took for kaleidoscope and storm; both
qualifiers on the rule are load-bearing (the same phone is 350px tall upright, where it all fits,
and a Kindle in landscape is 476 and never reaches it). The rule has to sit at the END of the
stylesheet: a media query adds no specificity and `#dock{position:fixed}` is declared later, so
placed earlier it silently loses.

**Known and NOT repaired, because it is hers**: on a 240x350
screen the dock is **315px of 350**, so the scene gets 35px and the music button — lifted by an
existing rule to clear a dock that no longer fits — ends up 7px off the top. Measured identical
before and after this sweep, so nothing here caused it. **Repaired Aug 2026 on her say-so** — *"you might as well fix ants
too"* — and it was the same two faults chimes had. At 240 a slider row wants 149px against the 211 the
dock has, so nothing could share a line and all eight rows stacked. The rows give up slider length
(120px to 58) and the object buttons a little size, and they pair two to a line: **315px to 136px**,
measured, and the same 136 at 240, 280 and 320. Above 320 nothing applies.

Underneath that, the
ground was centred in the whole SCREEN while the dock sat fixed across the bottom of it, so the scene
simply ran underneath — and still overlapped by 12px on an ordinary 390 phone. **The dock's height
changes with the width** (136 at 240, 282 at 360, 216 at 390, 172 at 430), so no fixed padding can be
right: it is measured and applied in `fitStage()`, as lamp does. The stage is padded to the band that
is actually free — under the two brass discs, above the dock — and the ground centres in that and is
capped to it. The cap only ever TIGHTENS, so a desktop keeps the sheet's own 56vh and is identical.
Measured clear at 240, 280, 320, 390, 600 and 1200.

And the `#music` rule that lifted the
headphones clear of the dock was still carrying **323px, the height of the dock it was written for** —
with the dock at 136 that put them 7px off the TOP of the screen, over the back disc. It is 146 now,
which is the dock's height plus a gap; **if the dock's height changes again, change this with it.**

**The speed slider got WORSE above halfway**, found Aug 2026 by measurement before she ever ran the
piece — and it is roller's fault in another shape. Ground covered in five seconds ran **1.33, 3.09,
4.46, 4.00, 3.62** per cent across the range: rising to the middle and then falling, so pushing it
past half made the ants *worse* at getting about. The cause is that **the edge of the tray was a
clamp and not a wall.** Every move was `Math.max(4, Math.min(W-4, ...))`, which pins an ant on the
border and leaves its heading still pointing into it, so it grinds along the edge until its run timer
happens to expire. At a walking pace an ant seldom reaches a wall and it never showed; wound up, they
get there ten times sooner and stay. Measured at full speed, **41.4% of all the movement on the page
was happening within a whisker of an edge** against 24% at the middle, and movement out in the open
collapsed from 13,030 pixels to 6,965. They turn away now, which is also simply what an ant does at
the edge of a tray: coverage **1.99, 4.74, 5.17, 5.98, 6.96** — rising the whole way, a 3.5x spread —
and edge-crowding at full speed down to **16.2%**. Three runs a setting at the top, because one run
each showed a dip that was only spread. The turn clears `climbing` and `onTwig` (an ant that has hit
the wall is not still crossing a twig), takes a shade of randomness or a corner ping-pongs it along
one line, and resets `straightTimer` or the old run turns it straight back into the wall.

**The
three objects are drawn, not emoji**, and there were two reasons. 🪨 and 🪵 both arrived in **2020**,
and the newest emoji her Kindle Fire is actually *proven* to render is **2017** — bowl's 🥣 and
candler's 🧘, both of which passed on it — so these were three years past anything demonstrated and
would have shown as empty boxes if missing. And `color:var(--brass)` never reached any of the three
anyway, because a colour emoji is a bitmap the font hands over whole and takes no colour from CSS:
musebox's white rabbit again. 🍃 renders everywhere and was drawn along with them, since two brass
outlines beside one green emoji is worse than either.

**Three of hers, Sep 2026, all from watching
it.** *"the ants shouldn't turn entirely purple when carrying lollipop back to the nest"* — a carrier
was painted purple all over as a state colour; it carries a **crumb of the sweet in its jaws** now, the
lollipop's own colours with one highlight, and is otherwise the same ant. *"all the ants move at the
same speed. none ever stop. they don't pause, wave around for a second, and take off in a different
direction. they don't pause, go a few steps, pause again."* Measured, every word was true: all twenty
within 0.5% of one pace, and **zero stops in twenty seconds** — the only pause in the piece was the beat
at an obstacle. Each ant has its own `pace` (0.72–1.28), a `surge` that wanders within a walk, and a
rest clock of its own (`startRest`/`endRest`): it stops, works its antennae over the ground at about
4Hz — **the antennae move now, walking and stopped, which is the difference between stopped and
frozen** — then carries on, turns off (60%), or takes a few steps and stops again (38%). Carriers stop
less, for less time, and keep their line home. About **one in five stopped at any moment**, 22 stops
an ant a minute; if that ever reads as too much or too little, the interval in `startRest` is the one
number. *"they also walk all over each other, and through each other."* They were points; **they are
bodies now** (`meetAnts`, `MEET_R`): two within a body of each other are eased apart, neither into an
obstacle, and if neither has just met someone they stop for a beat and the searching one turns off.
Ants up on a pebble or twig are on another level and are left out. **No greeting within 34px of the
nest** — the first version stopped every ant coming out of the nest to greet the others and heaped
them on the doorstep, caught in my own first screenshot; at the nest mouth they pour past. Deep
overlaps (centres under 3px apart) in 900 frames: **35 → 0**. Her verdict the same evening, on ants,
fireflies and moths together: ***"i would consider fireflies, moths, and ants all to be significantly
improved."*** Not a Done mark — she has not run any of the three over the four machines.
