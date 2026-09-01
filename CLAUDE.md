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

**Landing page:** `index.html` (titled *sagne*) — **five open shelves on a dark wall**, the
pieces standing face-front on them in mounts, the name of each type engraved on the brass
plate screwed to the board's front face. It replaced her apothecary **case** in Aug 2026,
which had replaced the flat card grid a few days before. Every position on it derives from one
table of measurements taken off the photograph itself. Change the picture and you change that
table; don't retype percentages by hand.

**Three pictures, one table.** `wall-desktop.jpg` (1896x1024), `wall-phone.jpg` (430x728) and
`wall-small.jpg` (324x600) — the same wall at three widths. Which pieces stand on which shelf
is written **once**, in `GEO.shelves`, and every one of the three reads it; the rest of a
skin is its own boards, card size and brass positions, in `SKINS` at the top of the script.
**Adding a piece is one line in `GEO.shelves` plus its card picture**, and all three sizes and
all twenty pieces' shelf tags follow. At the card size she approved, a shelf takes about ten
before it is tight; the fullest have five.

**Only the picture that is needed is fetched** — verified on the wire at 1440, 390 and 240,
one wall each. The markup must NOT name a wall in the `<img src>`: the browser would fetch that
one before the script had chosen, and you would be back to two on the wire. This is bowl's and
fireflies' lesson at landing-page scale.

**How each size behaves.** On a wide screen the wall **fills the window** and the surplus comes
off its **ends**, never its foot — the ends of the wall are bare and the floor is not, which is
why `tools/wall.py` adds 180 units of the wall's own plain surface at each end for the window
to take. On a phone the wall takes the full width and is allowed to **run past the bottom**,
which is the answer kaleidoscope, storm, chimes and ant all take. Measured: an ordinary phone
fits exactly with nothing below the fold; the 3in Jelly Star scrolls about 94px, **her call** —
the alternative was cards two thirds the size, and she chose the scroll.

**The pictures are built, not hand-made.** `python3 tools/wall.py <shelves photo> <blank plate>`
makes all three walls and the brass plate from her own photographs, so every step is recorded:
half the floor traded for wall at the top, the bays given the clean unshadowed wall from above
the top shelf, the colour matched to her cabinet's interior, the ends padded, and for the phones
a slice taken out of the **middle** so every board keeps both of its real ends. Her originals
(`sagnegalleryshelveswood.png`, `sagnebrassplateforfuckingreal.jpg`) are in her `daidle` folder.
The cabinet, `shelves-navy.jpg`, is still here and still needed — the wall's colour is matched
to it. `attic/museum-wall/cabinet-index.html` is the case's own page, kept as a record.

**Background, shelves, stands, cards — in that order.** Her words, and it is load-bearing. Each
board is drawn a **second** time over the cards (`.boardface`), so a stand's foot lands on the
wood and anything lower goes behind the shelf's front edge. Getting this wrong is what made the
stands read as standing *in front of* the shelves. The z-order is wall 0, boards 1, stands 2,
cards 3, brass 4, the dimming sheet 5 — and the sheet must be **above** the brass or the
off-shelves keep their names lit while their wood goes dark.

**Seats and plate nudges are per shelf.** These boards are shot nearly straight on, so there is
very little top surface for a foot to stand on: the top three sit right at the board's edge, the
lower two a shade into it (`seat` in the table). The plates are geometrically centred on their
boards and still don't *look* it, because a board's face isn't symmetric — so `railY` carries her
eye, shelf by shelf. Don't "correct" these to the arithmetic centre.

**One caution written down because it cost a day.** Give every board the same thickness and you
will be seating cards on a line that isn't the wood — three of these five are thinner than the
others, and the error is up to 6px, which reads as floating however you nudge it. The board rows
in `SKINS` are measured off each picture. If the picture changes, measure again.

**The brass is laid on, not photographed in.** The walnut case had its lettering engraved into
the picture; the wall carries her own plates as separate cut-outs — `shelfplate-<group>.png`
for the five groups, and `sagne-plate.png`, her blank brushed plate, for the name — with the names set over them in **Libre Baskerville 700**, her pick over
Cormorant: engraving wants even stroke weight, and Cormorant's hairlines vanish at the size a
shelf plate allows. **Each plate is cut to the length of its own word**, which is why `plateW`
is per shelf. Re-cutting is only needed if a group is renamed or the lettering resized; the
sheet of ten blank lengths she generated is in her `daidle` Drive folder. **`shelfplate-natura.png`
carried six rows of its own background above the plate**, opaque where the other four fade to
nothing, and stretched into a 22px-tall box that drew as a pale bar hanging over the plate —
on the case itself and on every page's plate popup, since all 20 pages use the same file. She
caught it on the popup. Cleared Aug 2026; the plate's own pixels weren't touched. If a plate is
ever re-cut, check the top rows are transparent before putting it in.

### The pages

Each linked piece now lives in its own folder as `<slug>/index.html`, served at the clean
address `/<slug>/` (e.g. `warmler.html` → `warmler/index.html`, live at `/warmler/`). A
`_redirects` file at the repo root forwards the old flat addresses (`/warmler.html`, etc.) to
the new ones, so existing bookmarks/links still work. Pages **not** on the landing page
(`candler_5.html`, `crystal.html`, `warmler-picker-concept.html`) are unaffected and remain
flat files at the repo root. The landing page links **20** pieces — the table below
lists all of them; if you add a piece, add its row here too, or a later session will not
know it exists.

**The Done column is the owner's call and nobody else's.** ✅ means she has said, in
her own words, that the piece is finished. It is not a claim that the code is good, that
the tests pass, or that a session ran out of things to fix — only she marks a piece done.
Never set it yourself, and never quietly unset it either: if a fault turns up in a piece
marked done, fix the fault and tell her, but leave the mark alone unless she takes it back.
A blank means only "she hasn't ruled on it yet", not that anything is wrong with it.

There are deliberately **no scores here.** Some pieces got one in conversation, but as she
put it, a score needs a field to score against — lamp, conometer and bowl aren't versions
of anything, so a number would be inventing a ranking she doesn't mean. The test that does
apply to every piece is the one further down this file: *does it behave like the real
thing?* That is a yes or a no.

**14 of the 20 are done.**

| File | On landing page? | Done? | What it is |
|------|:---:|:---:|------------|
| `index.html` | — | — | Landing page: the apothecary shelf ("sagne"), five shelves, all 20 pieces |
| `candler/index.html` | ✅ | ✅ | *Sagne Candle* — an interactive candle. `candler_5.html` is an alternate version (not linked)<br>**Done** — "as perfect as I can make it without overhauling the actual candle itself."<br>Aug 2026 it was the first piece put through her four-device test (Mac, Windows tablet,
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
through that test, and the standard for the ones that follow. |
| `roller/index.html` | ✅ | ✅ | *Roller* — a wooden tray you tilt to roll a small object around (sea-glass pebble, disc, or jellybean stone); tilt-controlled like `galileo`/`windower`'s location search but via device orientation or mouse<br>**Done**, pending her own testing of the bean's weave and the spin off a wall. Deliberately unscored: "there's other things like it, but none really do what it does."<br>**It did not tilt AT ALL on the Kindle** — her report, Aug 2026, and the cause was a missing
fallback rather than anything about tilt. The gate offers two ways in, the phone button and the
desktop one. Pressing the phone button turned device orientation on and **assumed it worked**, with
`return` before the pointer path was ever wired — so on a machine whose browser never fires
`deviceorientation` the tray had **no control whatever** and the only way out was reloading. A Kindle
Fire has an accelerometer and still may not fire it. It now waits 1.4s for a usable reading and, if
none comes, takes the listener off and uses the pointer instead. Measured on a browser that never
fires the event: **0 pixels moved under a finger drag before, 5293 after**.<br>Three
things Aug 2026, all hers, all after she had it in front of her.<br>**The speed slider was not a speed
slider.** It multiplied how hard tilt pushed and nothing else — not friction, not the wall bounce — so
once anything was moving it careered about at much the same rate wherever the slider sat. Measured
under a held full tilt: the pebble averaged **130px/s at the bottom of the range against 146 in the
middle**, eleven per cent, nothing anyone could feel, while its PEAKS moved two and a half times. She
asked for a speed slider so things could slide slower and it was reasonable to think there wasn't
one. What actually makes a thing slide slowly is the surface, so below the middle the tray now gets
draggier as well as gentler — the same friction raised to a higher power, which is what a shorter
settling distance is. Re-measured: pebble **73px/s** at 20, disc **48**, bean **63**, and the peaks
down by more.<br>**And it still read as not working, which took a second report to find**: *"the speed
slider doesn't appear to change much. maybe it hesitates before it starts? but it doesn't roll slower
in a noticeable way."* Both halves of that are one cause. Below the middle the PUSH was being reduced
as well as the drag raised — and a gentler shove still has to overcome the same stiction, so the
bottom of the range did not travel slowly, it **failed to set off**: measured under a gentle held
tilt, at slider 20 the pebble had moved **3px after 300ms, 9px after 600ms and 81px after three
seconds**, never reaching the wall at all. And from 60 upward everything looked much the same
(330, 338 and 360px at 300ms for 60, 100 and 220). A cliff, then a plateau. The push is left alone
below the middle now and the whole change lives in the friction, which does not bite until something
is already moving: at slider 20 it sets off at once (13px by 300ms, against 18 at slider 100) and
then crawls. **Peak speed across the slider is 220, 413, 600, 1378px/s at 20, 60, 100 and 220** —
monotonic and a 6.3x spread, against 56, 410, 564, 982 before. **At 100 the exponent is exactly 1 and nothing changes at all** — from the middle of
the slider upward the feel she already approved is identical, measured, which is the point of doing
it this way round rather than retuning the physics. The bottom of the range went from 20 to 10.<br>**The
dock spreads on a desktop.** Four groups stacked in a column 180px wide under a 640px tray on a
screen 1440 across, with the speed row lapping over the tray's own bottom edge. Side by side now, and
the dock stands 92px instead of 184, so it stops touching the tray. Gated on **width AND a fine
pointer**: the generated `touch-targets` block grows each slider by half the distance to its nearest
neighbour, measured on the stacked layout, so a coarse screen has to keep the layout those figures
came from — a Windows tablet in landscape is wide but coarse and keeps the column.<br>**The bean is
the most saturated of the three now, and shiny**, which is what she always wanted it to be and what
it was furthest from: it was pulled only 30–44% toward the tint from a pale cream stone, so cobalt
and black — the two she named — arrived as a dusty blue-grey and a dusty grey. Mixing harder is not
the answer; past about half, all three stops converge on the one tint and the bead goes flat. So the
bean stopped borrowing the stone's cream ramp and got **its own, built out of the tint**: a light
stop lifted toward white, the tint at full strength in the middle, a dark stop taken well down. Every
part of it is the colour and it still has real form. Gloss is three things at once and wants all
three — a long soft sheen down its length, ONE small hard specular where the light is (the tight
bright spot is what reads as wet; a big soft one only reads as pale), and a bounce light along the
shaded edge coming back up off the tray. The outline is the same dark at **half** strength: at full
it reads as a drawn line round the stone and turns the body polygon's facets into corners. The
`bean` numbers in the GLASS table are now unused and kept only so the table still reads one row per
colour. The pebble and the disc are untouched. |
| `lamp/index.html` | ✅ | ✅ | An oil lamp — trim the wick's shape and height, and the flame follows. **The fuel is built** (Aug 2026): it burns down, you cannot see how much is left, and you find out by tapping the copper base with a ten penny nail lying beside it<br>**Done** was given for the wick and flame; the nail and the fuel came after, so the mark predates them and she has not run the piece since.<br>**The
nail is hers.** *"we used to have an old copper based lamp like that, and my father kept a ten penny
nail on the shelf next to it for tapping."* So the level is not found by tapping the lamp with nothing
in particular — it is found with **a nail lying beside it**, which is how her family actually did it.
That is the whole interaction and it needs no instructions: a nail resting on the shelf is a thing a
curious person picks up, and a lamp is a thing they then tap. Her own photograph (`lampnail.jpg` in her
`daidle` Drive folder), cut off its ground to `lamp/lampnail.png`. **Cutting it took one wrong pass**:
the seed threshold that grows the mask was at 58, which is inside the photograph's own mirror
REFLECTION, so the flood ran straight from the nail into it and the cut came out with a dark ghost
attached. At 78 the reflection has no seed and the same flood gives a clean nail.<br>**A different
amount of oil every visit**, her call — *"that would be the most fun for whomever is interacting"* —
and it is also what a lamp found on a shelf actually is. **The burn follows the FLAME, not the slider** — her question, and the
answer was no until she asked it. Consumption was linear in the wick-HEIGHT slider alone: right
direction, wrong amount, and the shape slider left out of it entirely. Both figures are now read from
the very keyframes the renderer draws with, so the burn and the picture can never disagree, and the
measure is **height x width SQUARED** (a body of revolution about the wick) rather than height alone.
That distinction earns its place, because **trimming to a point makes the flame look bigger and makes
it smaller**: measured over twenty frames, a full flat wick draws 87x20px and 1157 lit pixels, a full
pointed one 115x12px and 929 — 32% taller, 40% narrower, a fifth less flame. Full lamp to out,
measured: **14.7 min** full and flat, **20.5** full and pointed, **36.0** low and flat, **54.1** low
and pointed. The honest limit, since this is a proxy and not the mechanism: a real lamp's rate is set
by how fast the wick draws fuel up and vaporises it, and this is tied to the flame instead — the
self-consistent choice for a piece where the flame is what you can see and what you adjust.<br>**The tap is steel on copper**: a hard pitchless contact tick first, because that is
what names two materials to the ear before any note has established, then the shell's own inharmonic
note. **STRUCK, not blown**, which is the easy thing to get backwards — blown across the top, more
liquid means a shorter air column and a HIGHER pitch; struck, the liquid mass-loads the walls and drags
it DOWN. Measured on the running page as it burned: **587Hz ringing 0.98s** at the start, 649 at 1.18s
two minutes later, **791 at 1.62s** nearly dry.<br>**The tap only worked on the LEFT of the base** — her report off the machines, Aug 2026. The nail's
facing was fixed: its point always faced right, so carried round to the far side of the lamp the point
faced *away* from the copper and the tip never met it. It turns in the hand now, to face whichever side
it is brought in from. The 40-unit hysteresis is load-bearing — flipping on the axis itself spins the
nail every time the hand crosses the middle of the lamp, which is most of the way to it. Measured, four
approaches (left and right, high and low): **two of four tapped before, four of four after**.<br>**And WHERE you tap earns its place**, which the old
note in the file had parked as optional. Below the oil line the wall is against the liquid and barely
rings — measured, **423Hz dead in 0.13s** against 587Hz for 0.98s higher up the same side. Four minutes
in the two taps came out **identical**, which is the oil having fallen past the lower one. The level
really can be found by running the nail down the side, the way you find it on a gas cylinder.<br>**The
end is her sequence, in her own words**: *"it should sputter and flicker when the fuel is very low. then
get shorter and weaker as it sputters more, then burn the wick down to ash, and go out."* The sputter
channel **falls fast and recovers slowly**, which is what reads as sputtering rather than as
flickering — don't make it symmetric. Measured over the last 100 seconds the flame's brightness runs
214, 190, 213, 204 … 151, 186, 161, 172, 141 … 77, 87, 73, 135 … 41, 15, 14, 8: dropping and catching,
dropping and catching, with the baseline sinking all the way. Then a grey ash stub and no flame.
**And there is an oil can in the corner opposite the music
button** — her ask, and it does two things at once: it takes the dead end out of a burnt-out lamp,
and it lets the tap be COMPARED, which is much the fastest way anybody will work out what the
tapping is for. Measured through one cycle: fresh 648Hz, burnt dry 790Hz ringing long, and after a
fill the same spot gives a dull **269Hz** knock because it is under the oil now. A can holds what a
can holds, so it goes in **nearly** full and not to a line. Filling a lamp that has gone out means
trimming the wick and putting a light to it, so the char eases away over about a second and the
flame comes up with it — 45 the instant it is filled, 164 half a second later, 216 after two.
**The pour is the one place on this page where the BLOWN rule is the right one**: the air column
above the oil shortens as it fills, so the gurgle RISES, where a struck lamp goes lower with more
oil. Both rules are in the piece and they are not the same rule. The can is in the corner rather
than the dock because the dock's height is what the lamp is centred against, so a fourth row there
would be paid for out of the lamp; measured, the can touches no control, not the music button, not
the nail and not the lamp, at 1440x900, 390, 320, 240x350, a Kindle and a 3in phone sideways. Drawn,
not an emoji — there is no oil can in Unicode and the nearest are an oil DRUM and a 2021 pouring
jug.<br>Two things came out of being able
to see the lamp UNLIT, which was never possible before. The photograph's own static wick is painted over
with a patch of glass cloned from higher up the same column, and as a **hard-edged rectangle its seam**
was invisible under a lit flame's glow and perfectly plain the moment the lamp could go out — the
*correct but reads as broken* class exactly. Feathered now, built once and cached rather than masked
every frame. And **the lamp is centred in the room the dock leaves** rather than in the whole page: it
used to run under the controls on a short screen, which cost only the base's shadow until there was a
nail down there to pick up. The nail clears the dock by 24px on a 240x350 phone, 59 on an ordinary one,
87 on a Kindle, 97 on a desktop; a 3in phone turned sideways is 180px tall and **scrolls**, which is the
answer she took for kaleidoscope and storm. The desktop lamp is a little larger as a result (443 -> 480
across), since it is no longer sized to leave room it never needed.<br>**The music button was lifted
clear of the whole dock on narrow screens, and that put it at 240px exactly on the nail's head.**
Measured, the only control it ever actually touched was the mute box at 240 and only by a few pixels;
from 320 up nothing overlapped at all. So the volume gives up a little length instead — the same trade
chladni's bottom row made — and the headphones stay in their corner. Worth remembering as the general
point: *the furniture gives way* can be paid for by the dock as well as by the button, and lifting the
button is not free once a piece has something of its own in that corner.<br>**The card was reshot**
Aug 2026: the old one predated the whole fuel system, so it showed a lamp with **no nail beside it** —
and the nail is now how anybody finds out the lamp has a level at all. Framed by measuring the lamp's
own painted extent and the nail's, so both are in shot and the oil can's corner button is not. |
| `warmler/index.html` | ✅ | ✅ | A warming plate with selectable metal **finishes** (brass, copper, aged brass/copper, gold, silver, diamond-plate). `warmler-picker-concept.html` is a finish-picker concept (not linked)<br>**Done** — through her four-device test Aug 2026 with nothing to repair: *"i honestly can't
find any fault with warmler. it's a simple twiddle toy, and now that we have the edge issues
worked out, it's fine on all four machines."* The edge issues were the two already fixed in the
site-wide sweeps — the music button sitting on the finish trigger at 390px, and the `<button>`
face showing behind `#finishTrigger`'s cut-out — so this is the first piece to pass on the
strength of work done before she ever opened it, rather than on repairs found by opening it. |
| `rain/index.html` | ✅ | ✅ | Rain on glass<br>**Done** — her call, Mon 24 Aug: *"as done as i can make it"*, and earlier the same
afternoon, *"as done as i can make it without an animating software"*. Read that qualifier as part of
the mark. It is not *"there is nothing more to want here"*; it is *"what is left wants a tool I
haven't got"*. So **don't propose rebuilding it** to chase the remainder, and don't read the tick as
an invitation to polish. **Through her four-device test** the same afternoon — *"i have tested it on
every machine"* — so it carries both marks.<br>**More area on the Jelly Star**, her ask off a later
pass. The pane was held to `70vw` with 22px of dark down either side and the dock carried a desktop's
padding. Below 320 the stage is padded to the band that is actually free — under the two brass discs,
above the dock — so the pane centres in THAT rather than in the whole screen, and can then take nearly
the full width without its top corners sliding under the discs, which is conometer's half-on rule.
Measured at 240x350: **168x211 to 206x210, 22% more glass**; 390 and up are identical. While there:
the headphones sat on the tilt slider, 15x31px of it covered, and the button cannot lift above this
dock without landing on the pane — so the dock gives way and reserves the corner instead, which is
fireflies' move, with the slider giving up the length it costs. |
| `ant/index.html` | ✅ |  | Ants<br>Swept Aug 2026 before her device testing, and two things were repaired. Its **seven
sliders were 3, 7, 9, 14, 18, 18 and 23px** under a thumb — the worst on the site — because the
touch-target generator had been compounding its own output; with that fixed they are 26–33.
And **turned sideways on a 3in phone it lost the top of its own dock**: 180px of screen against a
282px dock, with count, speed and light sitting ABOVE the top edge on a page that could not scroll
to them. It scrolls there now, which is the answer she took for kaleidoscope and storm; both
qualifiers on the rule are load-bearing (the same phone is 350px tall upright, where it all fits,
and a Kindle in landscape is 476 and never reaches it). The rule has to sit at the END of the
stylesheet: a media query adds no specificity and `#dock{position:fixed}` is declared later, so
placed earlier it silently loses.<br>**Known and NOT repaired, because it is hers**: on a 240x350
screen the dock is **315px of 350**, so the scene gets 35px and the music button — lifted by an
existing rule to clear a dock that no longer fits — ends up 7px off the top. Measured identical
before and after this sweep, so nothing here caused it. **Repaired Aug 2026 on her say-so** — *"you might as well fix ants
too"* — and it was the same two faults chimes had. At 240 a slider row wants 149px against the 211 the
dock has, so nothing could share a line and all eight rows stacked. The rows give up slider length
(120px to 58) and the object buttons a little size, and they pair two to a line: **315px to 136px**,
measured, and the same 136 at 240, 280 and 320. Above 320 nothing applies.<br>Underneath that, the
ground was centred in the whole SCREEN while the dock sat fixed across the bottom of it, so the scene
simply ran underneath — and still overlapped by 12px on an ordinary 390 phone. **The dock's height
changes with the width** (136 at 240, 282 at 360, 216 at 390, 172 at 430), so no fixed padding can be
right: it is measured and applied in `fitStage()`, as lamp does. The stage is padded to the band that
is actually free — under the two brass discs, above the dock — and the ground centres in that and is
capped to it. The cap only ever TIGHTENS, so a desktop keeps the sheet's own 56vh and is identical.
Measured clear at 240, 280, 320, 390, 600 and 1200.<br>And the `#music` rule that lifted the
headphones clear of the dock was still carrying **323px, the height of the dock it was written for** —
with the dock at 136 that put them 7px off the TOP of the screen, over the back disc. It is 146 now,
which is the dock's height plus a gap; **if the dock's height changes again, change this with it.**<br>**The speed slider got WORSE above halfway**, found Aug 2026 by measurement before she ever ran the
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
one line, and resets `straightTimer` or the old run turns it straight back into the wall.<br>**The
three objects are drawn, not emoji**, and there were two reasons. 🪨 and 🪵 both arrived in **2020**,
and the newest emoji her Kindle Fire is actually *proven* to render is **2017** — bowl's 🥣 and
candler's 🧘, both of which passed on it — so these were three years past anything demonstrated and
would have shown as empty boxes if missing. And `color:var(--brass)` never reached any of the three
anyway, because a colour emoji is a bitmap the font hands over whole and takes no colour from CSS:
musebox's white rabbit again. 🍃 renders everywhere and was drawn along with them, since two brass
outlines beside one green emoji is worse than either. |
| `windower/index.html` | ✅ | ✅ | A window onto the sky that follows the visitor's **local time & location** (uses geolocation + the clock)<br>**Done** once the sill light stopped being too bright on dull days and moonless nights.<br>Fourth piece
through her four-device test, Aug 2026. **`windower-frame.png`'s centre pane was cut out of a light
background** and kept a 3px white halo all the way round it — the same family of fault as the shelf plates,
and she spotted it as the same thing. Recoloured to the frame's own wood with the alpha ramp kept, inside and
out of the cut, so the pane's edge stays soft. The side panes were clean.<br>The layout on a Kindle or a 3in
phone ran 65–140px past the bottom of the page, taking the flag and half the controls with it, and both fixes
are hers. **The discs moved inside the window's own top corners** (they had been sitting half on it and half
off, and the room kept clear above them was room the piece could have used) — `position:absolute` there
rather than fixed, so if a screen still has to scroll they travel with the window instead of hanging over it,
and the rules are written `html #backlink` / `html #shelfdisc` **because the shelf disc's own block is
generated and sits at the end of the body, where a plain `#shelfdisc` rule loses to it on source order**.
And **the sill gives way**: the window box gets shorter and the frame is anchored to its top, so what is lost
is the sill rather than sky or proportion, and the light patch is masked to the same box so what's left of it
still catches the sun. A Kindle turned sideways needed one thing more — the chart is drawn at 78vw and so
grows with a wide screen however short it is, so in landscape under 560px tall it is capped by height
instead. All of it is held to `(pointer: coarse)`; the desktop layout is identical to the live site,
measured.<br>**The window shows the same slice of sky whatever shape it is** — about 100° either side of
south, mapped to a percentage of the opening, so on a phone the sun crosses a narrower window rather than
going behind the wall for part of the day. A real aperture that narrow would crop the sky instead of
squeezing it, and this was put to her as a fidelity question in Aug 2026. **Her ruling: it stands.** *"The
representation still appears to be what other people would be seeing outside. I'm okay with that."* Cropped
honestly, a phone would show an empty sky for hours at a stretch. Don't re-propose it. (The sun and the
hills are both percentages of the window, which is why they stay registered with each other at any shape —
including the shortened one; take height off the bottom only, below the hills, or that breaks.) |<br>Aug 2026 the
location flag moved up onto the line with the three tickboxes, her call. It had been on a line of its own
below them, and that line was what pushed the page 27px off the bottom of a 1440x900 laptop; it now fits
that screen exactly. A 1200x860 window is still 12px over — small, known, not chased. |
| `galileo/index.html` | ✅ | ✅ | A **Galileo thermometer** whose floats rise and sink with the visitor's **real local temperature** (open-meteo API); has a °C/°F toggle. Three instruments of different ranges, together reading 12–116°F<br>**Done** — "it needs no design changes, it covers a hell of a range, and i can't think of anything it needs to do that it doesn't."<br>Third piece through her four-device test, Aug 2026, and the fault was
that **a finger is not a pointer**. A float tapped on a touch screen was enlarged only while the finger was
held on it — and the finger then covered the very thing it had enlarged, so on the Kindle and the 3in phone
you could never actually see one. A tap now leaves it up; tap it again, tap a different float, or tap
anywhere else and it goes away. That last part is her rule for popups generally: *they go away if touched
again or if something around them is touched* — the flag's search closes the same way. The `pointerenter`
/`pointerleave` pair is **guarded to `pointerType === 'mouse'`**, because a touch raises those two as well
and unguarded they put the enlargement straight back down on release; don't remove the guard. The flag
itself and the line that answers it were 15px and 11px, which is a mouse dimension in the same way a 3px
slider is: under `(pointer: coarse)` they go to 22 and 15 with the field at 19. Desktop untouched.<br>Note
for anyone measuring this: **the floats' hit circles overlap**, so a tap lands on whichever is topmost, and
comparing "the hit circle I aimed at" with "the float that came up" will show a mismatch that isn't one.
Check `document.elementFromPoint` instead — the enlargement always belongs to the float actually under the
finger.<br>She then found the **floats puddling wrongly in the teardrop's base**, and the cause is worth
keeping: **the floor of a narrowing vessel is a bowl, not a plane.** Everything that sank came to rest on one
height, `lo`, the same all the way across — so five floats sat in a flat row out to a width the glass does not
have down there. What gives it away is the **tag**: a float is not a sphere, a metal tag hangs about two
thirds of a bulb-width below its centre, and by that depth the teardrop has closed in by another 40 units, so
the outer floats' tags hung straight through the glass. Swept across 14–118°F, **116 of 1015 placements had
some part of a float outside its vessel; it is 0 now**, with no float interpenetrating another in either
version. The depth a float can reach is now a function of how far out it sits.<br>One thing there is
delicately balanced. Among spots that settle equally deep the code prefers the one *resting against
something*, the glass included, and that is what stops the tube's twelve floats stacking into a tower up the
middle — its floor is flat, so every spot is the same depth and contact is the only thing left to choose by.
But on a curved floor a spot at the wall is genuinely higher, and the old slack (`bh*0.40`, 17.7 units) was
wide enough for it to win on contact — which perched the whole heap up the side of the bowl with clear glass
beneath it. **So the slack is now the flatness itself**: full where the floor is flat, strict where it curves.
Don't replace it with a constant in either direction — one value cannot serve both vessels. The tube's
arrangement is unchanged at every temperature bar 1–2 of 255 in the anti-aliasing. |
| `conometer/index.html` | ✅ | ✅ | A **pinecone hygrometer** — the pinecone opens (dry) and closes (wet) with the visitor's **real local humidity** (open-meteo API); has a live/manual toggle<br>**Done**.<br>Second piece through her four-device
test, Aug 2026. The picture is centred and grows with the screen, so on a short wide one its top corners
came up under the two brass discs and each disc sat **half on the photograph and half off it**. Her rule for
this, and it settles the general case: *half-on* is what reads as a mistake — wholly on or wholly off both
look deliberate. So on a 3in phone, where the discs sit entirely inside the picture, nothing was changed and
nothing should be: pushing them outside there would leave the picture too narrow to read, which is her call
and a good one. Where they did straddle an edge the picture's SIDES are trimmed to clear them, which costs a
tenth of the picture where clearing them vertically costs nearly a third.<br>Underneath that, the same fault
candler had: `html,body{height:100%}` with `overflow:hidden` is the whole screen with the browser's bar
counted as though it weren't there. On a Kindle that put the flag's own reply line under the bar — so you
could type a location in, and the piece would go and fetch it, and the line saying where it had gone was off
the screen. That is what "no location response" was. It lays out to `innerHeight` now, held steady while the
flag's field has focus. The flag also answers **Enter directly** rather than relying on the form submitting
itself: an on-screen keyboard is not a keyboard, and the Go key on some Android browsers leaves a one-field
form alone. **The same flag is on `galileo`, `windower`, `storm`, `pendulum`, `chimes` and `fireflies`, and
they have not had that line yet.** |
| `gyre/index.html` | ✅ | ✅ | Meshable **gears** you place and connect on a board, plus a signal-lamp piece whose lights are driven by the gear train. See `gears.md` for how the gear math/rendering works<br>**Done**.<br>Two of hers, Aug 2026.<br>**The parts stand in a column down the left on a screen wider than it is
tall.** The tray used to run across the top, which is the whole width of the board it exists to help
you fill; the room that frees is the point of the change. It falls back to the row when the column
would not fit — measured, a 3in phone sideways leaves a band of 156 units between the brass disc and
the dock against the 308 seven parts need, and both are pinned in SCREEN pixels so how much of the
BOARD they eat depends on the zoom below.<br>**And the board zooms out on a small screen.** The lamp
box is **353 board units** across and every gear is sized off one fixed `MODULE`, so on the Jelly
Star the box was **wider than the whole screen** (353 against 240) and a 40-tooth gear came out
227px. Scaling the lamp alone is not available: its two gears are deliberately built to the same
`MODULE` as every other gear so they can mesh with them, and shrinking one side of a mesh is not
something a mesh survives. So the whole board zooms together — `W`/`H` became board units,
`SCALE` stands between them and the screen, and the one place the pointer comes in divides by it.
Everything else on the page is written in board units and never learns the screen exists.
`SCALE=min(1, vw/620, vh/560)`, so it never zooms **in** and a desktop is pixel-identical. Lamp box
measured on screen: **353 -> 136px** at 240 wide, 221px at 390, unchanged at 1440. The horizontal
tray also drops below the two brass discs now: they are pinned in screen pixels, so zoomed out they
reached far enough down the board that the first gear sat under the back arrow and the lamp under the
shelf disc — the half-on-half-off reading her conometer rule calls a mistake. At full zoom that moves
the row 3px and nothing else.<br>Two tweaks of hers after seeing it: **the lamp stands at the head of
the menu** (the gears keep the order they were in behind it), and **the gears in the menu are graded by
size** (the menu only — the gears on the board are untouched). Each used to be scaled to FILL its own
slot, so an 8-tooth pinion and a 40-tooth wheel came out within a pixel of one another and the menu
told you nothing about what you were picking. **True proportion is the wrong answer here and was
tried**: at true proportion the smallest is 24% of the largest and on a zoomed-out board it came out
a speck. Her ruling — *"for this purpose clarity is paramount... split the difference a bit"* — so the
drawn size follows the **square root** of the true ratio, putting the smallest at 49% of the largest:
plainly the small one, plainly still a gear. Worth remembering as a general point: a menu is a
picture of what a thing is, not a scale drawing of it, and this site's usual instinct for fidelity is
the wrong instinct in a picker. The tap target is the slot and does not shrink with the drawing
either way, so the little ones are as easy to pick as the big ones. |
| `birds/index.html` | ✅ |  | **Birds** perched on wires strung between two poles against a sunset-sky photo; the wires sag realistically and dip under whichever bird is sitting on them<br>Swept Aug 2026. Its two sliders were **18px** under a thumb and are now 30. And below 300px the
headphones sat on the crow slider — measured, **23x30px of it at 240 and 3x30 at 280, clear from
300 up** — so the button lifts above the dock there, by the dock's own measured height (84px at
every width; change this with it if that changes). Otherwise clean: nothing below the fold at any
size, no console errors, and it fetches **one** background, picked by the time of day, not all four
— so its 6.7MB folder is only 3.0MB on the wire. |
| `bowl/index.html` | ✅ | ✅ | A still bowl of water for floating things on; has a breeze and an object picker<br>**Done**.<br>**Where it comes from, because it explains the piece.** Her grandmother used to set a bowl out and she would float the same objects in it — so what is inherited here is the **practice**, not the vessel: set a bowl out, choose things, float them. The ten bowls themselves are the opposite of a reconstruction. They are *"bowls we never had but i think are beautiful"* — stone, china, copper. Don't reduce the set to one "authentic" bowl on the grounds of provenance; the variety is the point and the memory is the gesture.<br>Aug 2026, found by measuring for a 3-inch phone: the dock is one row that never wrapped and wants **369px** laid out end to end, so on anything narrower the LAST thing in it — the flower, which is the whole object chooser — was pushed clean off the right edge, and with the page unable to scroll there was no way to reach it. It cleared a 390px phone by 22px, which is exactly why it looked perfect everywhere anyone had looked. Behind that sat a second fault: the chooser popup is a fixed 326px grid and hung 43px off **both** edges of a 240px screen, so fixing the button alone would only have revealed half the flowers. Below 379px the dock now wraps to two lines and the popup drops to three slightly smaller tiles; above it, nothing applies and the dock is pixel-identical at 390, 600 and 1200. The wrapped row is **right-aligned, not centred** — the music button is pinned in the bottom-left corner and a centred second row lands straight on top of it.<br>**It did not load on the Jelly Star** — her report, Aug 2026, and it was true in the
strongest sense. The ten bowl photographs are 1408x768 and about 1.5MB apiece, **15.7MB**
of them, and *nothing was drawn until every one had arrived*: the first `resize()` and the
first frame both sat behind one `Promise.all` over the lot. The picker made it worse, building
ten `<img>` thumbnails pointing at the same full-size files. Measured at 240x350 with the CPU
six times slower and the connection at 1.6Mbps: **the bowl had still not appeared after 100
seconds**, having pulled 21.5MB. Only the bowl on screen is loaded now; the other nine come in
behind the running piece **one at a time** (ten at once is worse on the machine that is already
struggling), a thumbnail's `src` is set only once its photograph is in the cache, and asking for
a bowl that has not arrived fetches it and takes it the moment it lands rather than swapping to
an empty bowl. **12.0s and 2.3MB** on the same simulated phone, and **she confirmed it on the real Jelly
Star** — *"bowl works fine now"* — so the simulation held. The other half of that fix was not bowl's
at all: see the shelf plates' cards above, which every page on the site was fetching on load. Worth
drawing the general lesson, since it took a report to find it — these pages had been swept for layout
faults several times and **nobody had ever measured what one of them FETCHES**. A sweep that only
looks at where things land cannot see 6MB queued in front of the piece.<br>**The object menu grew**,
her ask off the machines: *"the menu could pop up larger on both the jelly star and the kindle."* It
was a fixed 4x64 grid that dropped to 3x60 on a narrow screen and never grew for a wide one — so a
Kindle showed a laptop's tiles with a third of the room going spare. Measured: **66px at 240 (was 60),
72 at 390 (was 64), 92 on a Kindle (was 64, so +44%)**, and a desktop is untouched. Sizes are explicit
rather than fractional on purpose — a Fire tablet's browser is the oldest of her four and
`aspect-ratio` is not to be relied on there — and the rules sit at the END of the sheet, because a
media query adds no specificity and the base `.pickerOption` is declared below where they first
went.<br>**Her question, and the answer**: *"how are the stones removed? a second click on them?"* No —
each tile in the chooser carries its own **⊘** and a column of quantity dots; that is where things come
out. It was not discoverable because at 60px the ⊘ was too small to read, which the bigger tiles go
some way to fixing. Whether a second tap on the object itself should ALSO lift it out is a design call
and hers; it was put to her, and her answer came back: **yes.** A **tap** lifts a stone out;
a **drag** still moves it. The two gestures cannot be confused for one another and neither needs
explaining, which is the whole point. Six pixels of travel is the line between them, because a hand is
never perfectly still. The water is left rocking where the stone came out — the same splash ring a
dropped one makes, since a stone taken OUT of water disturbs it exactly as much as one put in. Before
this, nothing removed a stone at all: the only thing that ever did was the tenth pushing the first off
the end of the list. |
| `chimes/index.html` | ✅ |  | **Wind chimes** you build yourself — pick the rod material and the cord/chain, then hang them. Uses warmler's swatch-picker pattern<br>Sound was rebuilt Aug 2026 (struck on impact, real bar overtones, pitch by material).<br>**The set is TUNED now**, Aug 2026, and this was the answer to her *"probably accurate, but not
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
two.<br>**And each material is cut to its own lengths**, which was her follow-up question — *is that
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
on screen.<br>**And a rod-length slider beside the chain one**, her ask. With a tuned set it is a
**transpose**: the whole chime moves along the scale and stays in tune with itself, which is what a
smaller or larger set of the same design actually is. Short rods also hang higher and swing quicker,
so the meetings get busier as well as brighter — one control, both effects, which is exactly how she
described wanting it.<br>**And each material sounds like its own substance**, her third point. Two reasons it
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
beat the others don't have.<br>**Her verdict on all of that is in**, Aug 2026, and it covers the tuning,
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
same class of drift as the swatch and the three stale cards, in the notes rather than in the site.<br>**Measuring a sound out of this piece needs the simulation frozen
first** — `requestAnimationFrame` stubbed before the page script runs. An offline audio context's
clock does not advance until it renders, so every strike the rods make while the harness is setting
up lands at time zero and swamps the note under test. Three passes were wasted on that: it shows up
as every material decaying in the same ~1.9s, which is the pile-up's tail and not the material's.<br>Two things went in Aug 2026 after she watched it. The **hanger sways** — the whole set hangs off one ring, so it is a slow heavy pendulum of its own, its weight mostly the rods well below the bar, and the rods then hang from a *moving* support and are swung by it. What drives the sway is drag, and **drag goes as the square of the wind**, which is her own observation in one line: at a light air the lean is a tenth of a pixel and the bar looks nailed up; at full wind it is 3° (about 8px at the bar, twice that at the rod tips). There is no threshold in the code — the v-squared law is the whole of it, so don't add one.<br>Underneath that, a real fault: **the swing is solved in the convention `x = tie point + sin(angle)·length`, and canvas rotates the other way.** Every rod had been drawn with `rotate(+angle)`, so the contact test was watching the mirror image of the scene on the glass — measured at full wind, the two frames disagreed about who was touching on **43% of pair-frames**, rods passed clean through each other in silence, and it chimed with a plain gap showing. Now 0%. If you ever change how a rod is drawn or hit-tested, the minus sign in `ctx.rotate(-r.angle)` is load-bearing and so are the matching signs in `rodMidWorld` and `hitTestRod`.<br>**And it tangled, and stayed tangled** — her report, with a photograph of two long
rods lying across each other. Two faults in one, both in the contact test.<br>**A rod was a POINT, not a
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
— a knock near the tip turns a rod far more than the same knock at its throat.<br>**And the gap is
SIGNED now**, which is the "stays tangled" half. Rod i is tied to the bar to the left of rod j and
cannot get past it, but the test compared MAGNITUDES, so a crossed pair read as a comfortably
separated one and nothing ever pushed it back.<br>**Every pair is tested, not just neighbours**: a
long rod reaches past a short one entirely, so two rods with a stubby one between them meet at a
depth their neighbour never reaches, and an adjacent-only loop has no constraint linking them.
`touching` had to become a set of PAIRS rather than a flag per rod, or a rod resting on one neighbour
would have muted its strike against another. Interpenetration is **0%** now on both sets. It also
chimes *more*, which is the point: measured at full wind over 20s, the mixed set went from 210
oscillators to 312 and the default set from 264 to 330 — those were strikes that should always have
sounded and didn't, because the rods were passing through each other in silence.<br>**The hanger and
the cords are her own photographs now**, Aug 2026 — `chimerealhanger.jpg` and `chimehopefulsprite.jpg`
in her `daidle` Drive folder. What had been there was a brown gradient lozenge on two drawn strokes
with a stroked circle for a ring; it is a walnut bar on real chains off a real brass ring, and the
cords below it are real jute rope, real silver chain and a real black nylon cord.<br>**The hanger is cut
into TWO pieces and that is the whole trick.** The photograph carries **eight** eyelets screwed along
the bar's underside and the piece hangs **five to nine** rods, so a baked-in row could only ever be
right at one count. The eyelets are cut away into `chime-eyelet.png` and one is placed per rod, at the
tie point that rod actually hangs from — right at every count, and better than the picture, since an
eyelet is now always exactly where a cord leaves the bar. They hang clear below the wood, so lifting
them needed no repair to the bar; the cut is at y=635 of the original and not 637, because the eyelets'
stems reach two pixels into that line and left eight dark nicks along the bottom edge.<br>Every figure
in `HG` was **measured off the photograph** and is held in fractions of the bar's own width, so the
layout follows the picture rather than being typed. **The photograph's own proportions are shorter than
the drawn hanger was** — ring to eyelets 152px against 117 — and that is a real physical change, not a
cosmetic one: a shorter hanging assembly sways quicker, and a quicker-moving support throws the rods
harder. Measured at full wind over 20s, **636 oscillators to 684** on the default set and **696 to 828**
transposed. The **lean is unchanged**, which is what the physics says should happen — the balance point
is set by drag against gravity and not by the length — and it holds: **±4.23° before and ±4.29° after**,
over ~2,400 frames each. Measure the lean off the BAR's own top edge fitted across many columns; a
single-column probe catches the suspension chains instead and reports 18°.<br>**The cords are tiled, and
the tile is the whole problem.** The cord slider runs 40 to 170 against tiles of 18 to 41px, so every
cord is several repeats and a join that shows draws a ladder of rungs down the piece. Three things get
it invisible: the repeat is found to a hundredth of a pixel by correlation, the sheet's own lighting
fall-off along the run is divided out, and the ends are cross-faded. Measured on the rendered page at
the longest cord, the step across each join is **1.2 to 5.7 where the rope's own twist gives 7.9** at
its 95th percentile — the joins are quieter than the rope.<br>**The nylon cord was drawn pale cream and
its own swatch has always been black.** The picker showed a black glossy cord, the piece drew a
fibrous white string, and nobody had put the two side by side. The photograph settles it in the swatch's
favour.<br>**The rods are drawn, and mostly have to be.** A rod's length is its note — the lengths are
continuous and each material is cut to its own — so no set of photographed rods can stand in for them.
Both her parts sheets give four fixed lengths per material at **17–25px across**, where a walnut rod
wants **34** on a Retina screen; a photograph would have to be stretched to length *and* upscaled. This
was measured on both sheets, so it doesn't need measuring again.<br>**WOOD is the exception, and it is
hers**: *"the only thing that's not an improvement is the wood ones, the drawn wood doesn't hold up
convincingly."* She is right, and the reason draws the line for anything like it later — **brass and
silver are smooth cylinders, which shading does well; wood IS texture**, and a gradient with four grain
strokes over it reads as orange plastic. Draw what is smooth; photograph what is textured.<br>The way
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
the grain at draw size 3.85 against 3.93.<br>**The wood swatch was re-cut from the same walnut** at the
same time, framed like the other three. It had been a lighter wood, matching the drawn rod: swatch
luminance 92 against the new rod's 72. Left alone that would have been the same fault as the cord
swatch — the picker showing one thing and the piece another. 75 against 72 now. The old dead `chime-rod-*.png` sprites are still on
disk, unreferenced, as warmler's unused textures are.<br>**Noticed while measuring and NOT fixed**: on a
240x350 screen the dock's four rows swamp the chime entirely. It is identical before and after this
change, so it is hers to find on the Jelly Star — **and she found it**: *"chimes menu overruns the
chimes"*. Two things were wrong and both had to go. At 240px a dock row is 158px wide against 208px of
room, so nothing could share a line and all six pieces stacked — **212px of a 350px screen**. Below 320
the rows give up slider length (110px to 58) and pair up: swatches+count, cord+rod, wind. **132px, three
lines.** Above 320 nothing applies and the dock is identical.<br>Underneath that, the real fault: the
chime is drawn in its own units off `HANGER_W`, so it was drawn **full size behind the dock**. `SCALE`
now stands between those units and the screen exactly as **gyre's board** does — everything on the page
is written in units and never learns the screen exists, and the only two places the screen comes in (a
click on the canvas, and where the length popup is put) divide and multiply by it. It never zooms IN:
measured, **1440, 1200, 600 and 390 are all scale 1.000**, and 320 is 0.928, 240 is 0.390. `hangerTopY`
is held in SCREEN pixels (`TOP_GAP/SCALE`), or a zoomed-out chime hangs under the two brass discs —
gyre's own lesson. And sideways on a 3in phone the dock is 174px of 180, so that one **scrolls**, as
kaleidoscope, storm and ant do; the rule sits at the END of the stylesheet because a media query adds no
specificity and `#dock{position:fixed}` is declared above it.<br>**And the chain
it hangs BY**, her ask off the first look: *"the top ring is hanging from... nothing."* It was — the cut
stopped at the ring's top and the hook chain above it was thrown away. It is back, cut from the run above
the ring **in the same photograph**, so it is literally the same chain rather than a match for it. Only
57px of it exists and one repeat is 35.30px, so there is exactly one period plus enough overlap to
cross-fade; the repeat was found by minimising the wrap rather than by correlation, which is the more
reliable objective when there is barely more than one period to look at. Step across the join **0.27x an
ordinary row-to-row step**.<br>Two things about it are load-bearing. It is drawn **outside the lean**,
because the ring is the pivot and does not move — so the chime swings beneath a chain that stays put,
which is what a fixed pivot at the ring means and what it looks like. And it stops **inside the ring's top
brass** rather than at the ring's centre: the ring's hole is transparent in the cut-out, so a straight run
carried to the centre shows through it and reads as a chain passing BEHIND the ring instead of hooked on
to it.<br>**The card was
reshot** off the rebuilt piece — the old one predated even the DRAWN hanger, showing a curved dark bar
with a knot at the top and hammered flat rods, none of which the piece has had for some time. Framed by
measuring the chime's own painted extent in the shot rather than trusting a ratio, and **cropped** to
440x640 rather than squeezed into it, which is musebox's lesson. **Reshot again** once the hanging chain
went in, at her ask, so the card shows what the piece shows — and the framing is **unchanged**, which is
her correction and worth keeping: *"there was already space above the ring. just add chain to it."* The
first attempt made room for the chain by shrinking the chime, when the card had always carried 9% of its
height as empty sky above the ring; the chain fills that and costs the chime nothing. The subject is the
RING down to the rod tips, padded 30% and nudged 3% down — the same rule as the first card, and the
general point is that adding something to a piece is not automatically a reason to re-frame its card. |
| `chladni/index.html` | ✅ | ✅ | A **Chladni plate** — sand on metal, forming standing-wave patterns in response to sound<br>**Done**. Aug 2026 it was given **substances**, in
two families that are a real inversion of each other and not a recolour: heavy grains (sand, salt)
are thrown off the moving plate and pile on the **nodal lines**, while very fine powder (lycopodium,
fine flour) is too light to be thrown and is instead swept by the stirred air to the **antinodes**,
drawing the exact negative of the same figure. They're chosen on a **slider**, her call over a row of
swatches or tickboxes: the four are genuinely in an order — coarsest and heaviest to finest and
lightest — and that ordering is the physics. The notches are evenly spaced and **nothing marks where
the figure flips**; finding that is the point. The notches themselves are the grains, each at its own
size, colour and shape (sand rounded, salt square because halite is cubic, the powders an even veil),
the same move the chimes rods got. Emoji were considered for them and don't exist: 🧂 is the only one
of the four, sand and flour have only metaphors (desert, hourglass, sheaf), and there is no spore at
all — 🍄 is a fungus and lycopodium is a clubmoss.<br>The notches are **her photographs**, one of each
substance, cut from a sheet she made (`chladnithumbnails.jpg` and the three full-size tiles in her
`daidle` Drive folder). Two of her decisions about them: the lycopodium notch is deliberately the
**clubmoss plant**, not the powder, so that a curious person can cut the picture and search it — and
there is nothing to see in a photograph of spores anyway; and the sheet's lettering (FLOUR, SAND, SALT
— plus a PEBBLES tile Gemini added unasked, which she didn't want) all came off. The three other
notches are cropped into the **substance itself and not the tool that is in the shot with it**: at
40px, the full tiles read as a wooden scoop and a sieve rather than as salt and flour. Photographs
need the notches at 40px; at 26 they are four beige smudges.<br>**Getting a picture out of her Drive
is possible — don't conclude otherwise.** This session first decided it wasn't: the network is closed
to Google, and the Drive tool hands a file back as base64 text, which at 650KB looked far too big to
carry. It isn't. When a tool result is too big it is **spilled to a file** under the session's
`tool-results/` directory and the path is handed back instead — so `json.load` that file, `base64`
-decode its `content`, and write the bytes to disk. Nothing has to be retyped, and the size stops
mattering. Two things in there are worth knowing before touching
it: the powders carry a **pile of their own volume** (a coarse count per patch of plate, pushing back
only once a patch holds more than a few times an even spread) or every grain converges on one
infinitesimal point and it reads as a bare plate with dots on it; and the powders are deliberately
drawn with **bigger, softer, fainter** marks than the heavy families, because ten thousand particles
spread over a third of the plate have to stand for clumps of powder rather than single spores.<br>A
**cornflour suspension** would be a genuine third family — not a scatter of particles at all but a
connected shear-thickening layer, liquid on the nodal lines and locking into standing fingers and
persistent holes over the antinodes. It was raised and **parked**, her call: it needs to be drawn as a
fluid surface rather than as marks, and *"if it can't be rendered convincingly as a fluid, let's wait
until we have better tools."* Don't re-propose it as a fifth swatch on the existing renderer.<br>Aug 2026 the **pitch slider's pulse
came out**. Its knob glowed until a visitor first touched it, and the comment in the code said in as many
words that it "nudges a first-time visitor toward the control that actually changes the pattern" — which is
the exact thing the *Exploring is the point* rule below forbids. It predated the rule. Don't put it back.<br>Aug 2026, hers off the Kindle and the phone: **the microphone tickbox joins the sound
line** below 820px instead of having a line to itself for one 16px box. It belongs beside the
sound it is an alternative to — listening to the room rather than to the tone — and the plate
gets a line of height back. The pitch is not reordered; it simply becomes the first line once
the mic stops taking one, which is where the desktop has always put it. On a 3in screen the
joined row wanted 229px against the 226 it had, three pixels short, and wrapped straight back
to two lines, so below 320 the volume gives up a little length — the one thing in that row with
any to spare. Desktop unchanged. |
| `fireflies/index.html` | ✅ |  | A field at dusk where you place fireflies in the grass; real dusk-to-night sky, with bats about<br>**It was fetching all seven sky photographs on load — 7.6MB — which is bowl's fault at half bowl's
size**, and the general lesson bowl's row records: a sweep that only looks at where things land
cannot see megabytes queued in front of the piece. Only the stage the darkness slider is sitting on
is asked for now, and its neighbour for the cross-fade; the rest come in behind the running piece
**one at a time**, nearest-first, because seven at once is worse on the machine already struggling.
Moving the slider to a stage that has not arrived asks for it at once, and until it lands the
nearest stage that HAS arrived is shown — never the flat stand-in. Measured on a simulated Jelly
Star (240x350, CPU 6x slower, 1.6Mbps): the real sky is up at **11.4s having fetched 2.1MB, against
30.4s and 3.1MB in flight before**; the other five follow at 21.8, 26.8, 32.0, 37.5 and 43.0s. Only
cross-fade when BOTH stages are really present, or it dissolves between two skies that aren't
neighbours.<br>**THE SEVEN SKIES WERE TWO DIFFERENT PLACES**, her catch, Aug 2026: *"it should be the
same picture across all of them, just at varying stages of night."* She was right and it is
measurable — on the land alone, stages **0–3 agreed with each other at 0.99 and with 5–6 at 0.13**,
with stage 4 matching neither properly. So dragging the slider past about two thirds made the trees
pick themselves up and move: not night falling on a place, a cut to somewhere else. And it was not a
clean progression either — brightness ran 59, 58, 33, **41**, 23, 23, 15, so **stage 3 was brighter
than stage 2** and pushing toward darkness made it lighter at one point.<br>**Rebuilt from four
photographs of ONE field**, two of them hers shot to order the same afternoon (`fireflyfix1.jpg`,
`fireflyfix2.jpg` in her `daidle` folder). The brief that worked is musebox's lesson applied — *don't
repair a wrong picture, specify the right one* — and rather than ask for seven consistent frames
(which is what failed at nine for chimes) she was sent the three good existing frames as a
**reference** and asked for the same view at full night. Then, unprompted, the deep-twilight one as
well, which is the moment that cannot be derived: the glow still on the horizon while the first stars
are already up. **Verify a frame like this by searching for the best alignment of the treeline** —
fireflyfix1 came back at 0px across and 0px down, fireflyfix2 at 2px, against 0.13 for the wrong
field. Do it at FULL resolution: a coarse 480x300 comparison reported 8px of shift that was not
there.<br>The seven stages are eased blends between the nearest two anchors, then graded so the ground
falls at **every** step: 39.5, 30.1, 23.1, 18.2, 14.2, 10.5, 7.0. **The grade is a gamma and not a
multiply, deliberately** — a multiply dims the stars as much as the sky, where a gamma deepens shadows
and mid-tones and leaves bright points alone, which is what a darkening sky really does to a star
field: the stars do not dim, they emerge.<br>**And they are JPEGs now**, because a night photograph is
exactly what JPEG is for: **6.92MB to 0.70MB**, on the piece that was the slowest of the eight to
appear. Measured on the simulated Jelly Star it now shows in **2.1s having fetched 0.37MB, against
10.8s and 1.13MB**. Banding is the risk in a dark gradient and was checked — the longest run of one
identical value across a sky row is 12px of 963. The old PNGs are deleted (two of them were the wrong
field) and are in the history if ever wanted.<br>Its five sliders were **3, 4, 5, 19 and 20px** under a thumb — the wind one had no
rule at all — and are now 21–30. Still small and not repaired: its two tickboxes at 14px and its
location flag at 25x18, where galileo's was grown to 22x15 under `(pointer: coarse)`.<br>**And it is
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
per slider move instead of once per frame.<br>**This also settles the 43-versus-25 puzzle in the
paragraph above.** Both figures were honest and they were taken at different slider positions — one
landing on a stage, one between two. If a frame-rate figure is ever recorded for this piece again, say
where the slider was.<br>Two things about the cache are load-bearing. The key covers the screen size,
the DPR, the blend fraction **and which photograph is standing in** — the backfill swaps stages in as
they arrive, and without `base.src` in the key a stand-in sky would stick after the real one landed.
And it is drawn at `W*DPR` with the same `setTransform` the main canvas uses, or a Retina screen gets a
soft sky. Verified pixel-identical to the old drawing at darkness 0, 25, 66 and 90: **0.000% of sky
pixels differ by more than 2/255, worst 0**. Neither freezes; both read as less smooth.<br>**They
flew in the grass, in formation, and all on the same beat** — three faults, all hers, Aug 2026, found
by her watching it and none of them visible in a screenshot.<br>*"is it my imagination or do they stay
really low?"* It wasn't. `altFrac` runs 0 at the ceiling to 1 at the ground, the top of the near grass
sits at **0.45** of that band, and the preference was 0.58 at the default darkness — so the whole
population cruised **below** the blades. Measured by reading the fireflies' own positions out of the
running piece: **11.3% were above the top of the grass** and the median sat 65px inside it.<br>**And
the flash fired at the bottom of the dip**, though the line of comment above it said "flashing partway
up out of it". `sin(0.55·π)` is 0.988 — 99% of full dip. The swoop takes 2.2–3.4s and the light is
spent in about half a second, so weighted by brightness the firefly sat **72% of a dip below its
cruising height the whole time it was lit**, about 29px. At 0.78 that is 25%, ~10px, and the climb
while lit goes from ~9px to ~21px, so **the J gets deeper, not shallower**. Share of LIT fireflies
above the grass: **16.5% → 26.6% from the altitude alone → 57.0% with both.** Don't go past ~0.85 or
the light arrives after the climb is over.<br>**Her call on the height, off four rendered options:
the highest.** The ceiling went `horizonY()-55` → `-130`, so they can rise against the sky. That is
hers and it is not unfaithful — species differ, and the ones that flash up among and above the trees
are real; she had already confirmed the low flying itself is true to life, so what moved is the
ceiling, not the idea.<br>**"they all seem to be in such formation. real fireflies dip and loop and
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
doubles back 4.0 → 5.3 times a minute, highest reached 68% → 46% of the page.<br>**Measuring this
needs the fireflies read out of the page, not off the pixels, and that cost three wrong answers.**
Counting bright blobs in screenshots put the share above the grass anywhere between 12% and 38% for
the *same* build — the population's own random spread swamps the effect — and on that evidence the
flash fix was first reported as working, then as not working. A one-line `window.__probe` in a
throwaway copy gives exact positions and settles it. **Two traps in doing that**: `cp -al` hard-links
the file, so editing the "copy" edits the real one (it did); and keying a trail by its index in
`males` draws a straight line from one insect to another whenever the array is spliced — key on the
object.<br>**AND THERE WAS NO INSECT BETWEEN FLASHES AT ALL**, which is her sharpest catch on this
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
dusk, an unlit firefly stands out from the sky by **~17/255** against nothing before.<br>**This one is
not provable from a screenshot and three attempts at a before/after picture were misleading** — the
two builds put their fireflies in different places, other insects wander into a close crop, and a
still cannot show *following* something. Don't try to settle it that way. The useful number is that a
firefly covers only **50px between one flash and the next** (112px before the wander work, so that
change helped this rather than hurt it): there was never much ground to cover, and the only question
was whether anything was there to see.<br>**HOW it lights, which is hers off the machines**: *"do
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
(`flashT`) rather than the swoop's, because a hovering flash has no swoop running. |
| `kaleidoscope/index.html` | ✅ | ✅ | A tray of real photographed small objects — glass, gems, gears, beads — mirrored live. Place them, then turn the ring<br>Objects re-cropped and the desktop controls spread Aug 2026. The turning ring (top) is **drawn, not an image** — brass-bound wood with a grab knob, dimmed so it doesn't fight the mirrored view. **The tray ring (bottom) is deliberately left brighter than the scope ring** — her call: the bright one pulls the eye first and says *drop things here*, then you look up and the dim ring's view makes sense. Don't 'fix' the mismatch; it is the wordless instruction. **Done** — her verdict came on Mon 24 Aug,
after the ring drag was made a real turn and the card reshot: *"i have checked those on the machines
and they are great."* That closes the question this row had been carrying open.<br>**The ring drag was a sideways swipe, not a turn.** Aug 2026, her
report: *"the ring drag is.. terrible. on every machine. the first quarter turn or so works, then it
goes off the rails."* It was `turn += (clientX - lastX) * 0.012` — horizontal travel and nothing
else. Grab the knob at twelve o'clock, pull right, and it obeys; but the knob is now carrying round
toward three, and to keep following it your hand has to move DOWN, which has no sideways component
at all, so the ring stops dead. Round the bottom your hand is going LEFT and it turns backwards
under you. Measured before the fix, sweeping the pointer in a circle round the ring: hand at 30°
gave 58°, at 90° gave 116°, at 120° gave 100°, at 180° gave **0**, and a full circle of the hand
left the ring exactly where it started. Her "every machine" was the clue — the gesture the code
listened for and the gesture a bezel asks for only agree for about ninety degrees, and no device
could have made that better or worse. It reads the ANGLE swept about the ring's centre now, 1:1,
unwrapped across the ±π seam (without that it would snap a whole turn every lap) and ignored inside
a tenth of the radius (near the middle a hand that has barely moved has swept a huge angle, and it
would spin off a twitch). Verified 1:1 at every 30° of a full circle and back again, on desktop and
on touch.<br>**And the knob was decorative** — her report, Aug 2026: *"the ring is turnable, but the
knob itself has no hand option and no turn cue, which seems to defeat the point of there being a
knob."* The grip layer stands **13% proud** of the scope's own box so the knob can overhang the edge,
and it carries `pointer-events:none` — so the knob sat outside the only element that carries the turn.
Measured at 110% of the radius: the pointer landed on the page wrapper with `cursor:auto`, and a drag
begun **on the knob turned the ring not at all**. A pseudo-element on `#scopeWrap` reaches the grab out
over the whole grip ring; events on a pseudo-element target its host, so the existing `pointerdown`
picks them up unchanged and `ringAngle` measures from the same centre. Now: `cursor:grab` on the knob,
and a drag from it turns the ring. The ring also **brightens while the pointer is over it**, under
`(pointer: fine)` only — a finger has no hover. That is not a hint: nothing is explained and nothing
appears, it is the piece answering, which is the one thing the no-nudging rule does allow.<br>**The card was still the old look** — flat gold stripes and a sparse pattern, from
before the ring was redrawn as brass-bound wood with a grab knob and the objects re-cropped. Reshot
Aug 2026 with a spread of pieces on the tray at warm and cool hues, the tray and controls hidden so
only the scope is in frame, and the brass scaled to the card's full width by **measuring** the ring's
painted extent in the shot rather than trusting a ratio. Same 440x640 as the rest.<br>**The phone case was
broken and is now a drawer.** Four rows of pieces under a 400px scope came to 380px of controls on a screen
844 tall that does not scroll, so both sliders and every mirror button sat below the bottom edge and could
not be reached at all — worse than the 'bottom row under the fold' it was first reported as. On a phone the
pieces are now a small closed tray of 30px tiles taking 66px, and everything fits above the fold. Touch the
tray and it opens into a bottom drawer of 52px tiles, low enough that the scope and the dish are both still
in sight above it, so a piece is carried up out of the drawer onto the dish in one movement and the drawer
shuts itself when one lands (a miss leaves it out to try again). Two things there are load-bearing: the
phone `#controls` is a **column, not a wrapping row** — as a wrapping row it collapsed from two lines to one
when the palette left the flow and slid the dish out from under the thumb mid-carry — and `#leftCluster`
keeps a `min-height` of 66px for the same reason. The veil behind the drawer dims and deliberately does
**not** blur: you don't blur the thing someone is aiming at.<br>**That fix was measured at the phone's FULL height, which is
the trap this site has hit before.** At 240 the layout ran 158px past the bottom of a page that could
not scroll (20 controls unreachable, and the closed 7-column tray is itself 246px on a 240px screen);
at 320 it was 114px over. Both were caught, and a `max-width:379px` rule let the page scroll down
there. What that rule could not catch is that **an ordinary 390px phone was cut off too** — measured at
the height a browser actually leaves visible (664, not the device's 844), 89px of `#controls` hung off
the bottom, taking the mirror buttons and one slider with it, on a page that could not scroll to them.
Aug 2026 her ruling was simply **have it scroll**, and the width gate came off with it: `html,body` grow
to their own content at every width, and `#wrap` still carries `min-height:100dvh`, so a screen with
room to spare is the same fixed, unscrolling frame it always was. Verified: desktop at 1440 and 1280,
a Kindle upright and a tablet at 800 are **identical to the pixel and do not scroll**; 240, 320, 379,
390, a Kindle sideways and the 3in phone sideways all scroll and have everything reachable. The
`padding-bottom:96px` stays held to `max-width:379px` — only down there do the controls run the full
width and meet the corner music button, and applying it wider merely made a page that fitted scroll.
`#trayWrap` keeps `touch-action:none` at every width now, or dragging a piece about on the dish scrolls
the page underneath instead, and below 280 the tray drops to six columns. **A small-screen arrangement
is no longer owed**: scrolling is the answer she took, not a placeholder for one. |
| `moths/index.html` | ✅ |  | **Moths** losing their bearings on a hanging bulb. Not attraction — a moth holds a course by keeping a distant light at a fixed angle, and a near one wraps that course into a spiral. Three sliders: dusk→dark, bulb, how many. Colour is a readout of depth (dark in front of the glass, pale behind), from her own three-shade cut<br>Built Aug 2026 from her brief, then put right by her own watching of it — she found that the moths crowded the bulb and stayed (an absorbing state: all five reached it and none ever left), that moths in front of the lower glass came out grey rather than black, that they all flew alike, and that they never tilted or wavered. In **natura**, which is therefore a shelf of four |
| `musebox/index.html` | ✅ |  | A **music box** — set pins on the disc to write a tune<br>**The look question is SETTLED**, Aug 2026. She had said *"you did a lovely job
building it, but i'm not sure it's -beautiful-"* and thought she might bring pictures from Gemini to
rebuild it from. She did, it was rebuilt on them, and her verdict on the result is ***"to my eye, yes.
yes it is."*** That closes the only thing this row was carrying open. **It is not a Done mark** — she
has not run it on the four machines yet, and that is hers to give separately.<br>**The rebuild, and
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
is tilted, it is no good.<br>**Four assets, each of one thing**: `musedisc.jpg` (face-on, round, no
pins — kept as a JPEG and clipped to its circle when drawn, because as a PNG with an alpha cut it came
to 1.3MB, which is bowl's lesson about page weight), `museroom.jpg` (the empty room, walnut and the
same navy the case stands on), `musehand.png` (pivot found by locating its two rubies) and
`musepin.png` (one brass head from above). **The eight notes sit on eight of the disc's OWN engraved
circles** — measured, the engraving runs 117, 145, 176, 208, 240, 277, 309, 337 of a 378px radius,
exactly eight between the hub and the rim. Held as fractions of the radius, and `cellAt` finds the
NEAREST ring rather than dividing by a constant gap: real engraving is not evenly spaced and should
not be forced to be.<br>**The picture takes the shape of the screen**, her ask. The canvas keeps a
constant width in its own units so every measurement stays put; only its height and the disc's radius
follow. Measured: 1100x974 with a 960px picture on a desktop, 1100x1407 with a 358px picture on a 390
phone, and the disc goes from 55% of the picture's width to 88%. The table is never distorted — always
the same scale as the width — and the wall is drawn at its own scale with its top few rows stretched
to fill what is left above it, since stretching the whole gradient five times over would band it. A
3in phone and a phone sideways scroll, the answer she took for kaleidoscope and storm.<br>**The table was toned down**, her call on a note of mine: it was the warmest and
brightest thing in the frame and the disc is the subject, so it pulled the eye down and forward — the
same fault she named herself on musebox's white rabbit. Fifteen per cent of the saturation and twelve
of the lift come off the band below the table's front edge, and it is cooled a shade; the first two
rows are ramped so the edge does not gain a line of its own. Baked into `museroom.jpg` rather than
done per frame.<br>**The card
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
its flash smeared across the card.<br>**The sound was not touched and neither were the controls**, her call: *"leave off the
controls, as while they're decorative, they're not standard with all the other pieces."* Gemini's
sheets carried an icon strip, a second kind of marker and an extra square button; all of it is the
generator embellishing rather than a decision, and none of it came across.<br>Aug 2026 it got **four voices** at her ask, the
chime she already liked plus **piano, guitar and a Native American flute**, each built from how the
real instrument makes its sound rather than from a preset. A struck string is stiff, so the piano's
partials are stretched by n·√(1+Bn²) — that stretch is most of what makes a piano sound like a piano
and not an organ — with the hammer landing underneath as its own pitchless knock. A plucked string's
harmonics are set by WHERE it is plucked, sin(nπp)/n², so the guitar has real holes in its spectrum
at the pluck's own nodes (p=0.22, an ordinary picking position). A fipple flute gives a strong
fundamental, a soft second and almost nothing above, and the half that matters is **breath running
the whole length of the note** rather than only its start — that is what makes a flute sound blown
instead of struck — with a slow attack, a chiff at the front, and vibrato arriving only after the
note has settled, the way a player's does.<br>**Two of the four were wrong and she caught both**, Aug
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
third **0.067**, and the note's whole tail 1.29s against the piano's 1.57.<br>The flute's fault was
one number. Its second partial sat at **0.236** of the fundamental, a quarter of it, which is squarely
a horn; a duct blowing across an edge is very nearly a pure tone. **0.100** now, third 0.085 -> 0.025.
Two things underneath that are worth keeping. **The breath was doing the harmonics' job**: band-passed
at 2.1x the note with a tight Q it sat right on the second harmonic and reinforced the very thing that
made it a horn — it is at 6.2x and much broader now, so it is air rather than a pitched partial. And
the note got **a slow waver in loudness** as well as in pitch, since an amplitude that sits perfectly
flat is most of what reads as blown-by-a-machine; it **multiplies** the note rather than being added to
it, because added, the waver's own offset kept the gain off zero and the note could never actually
end (measured, its tail ran from 0.78s to 1.04 and would have gone on).<br>**Levels were re-checked
against the waveshaper, not just by ear.** The guitar's body peaks alone took a single note from 0.67
to **1.11** — into the limiter on its own, which is the one thing that shaper exists to avoid — so the
string's amplitude came down to 0.62 and a note now peaks at 0.641. The flute is the opposite trap: a
near-pure tone sums far more coherently than a complex one, so eight of them on one step rode the
ceiling for **1649 samples** where the old busier flute rode it for 994. At a fundamental of 0.44 it
is **865**, under the sound it replaces. Peaks stay at exactly 1.0 with nothing over on all four
voices.<br>**AND THEN SHE MOVED THE GUITAR INTO THE PIANO'S SLOT**, Aug 2026, which is the most
useful thing that happened to this piece's sound: *"the guitar now sounds like a much better piano.
the piano sounds like a synthesizer."* Both halves right, and the second the worse fault — so rather
than throw away a sound she liked, it took the slot it suited. Her instruction was *"whatever you do,
please use the current guitar for the piano going forward"*, and it went across **unchanged**. It is
deliberately NOT piano-ified: inharmonic partials, a longer ring and a felt thump instead of the click
are all the obvious next move and all of them would change the sound she just chose. Don't, unless she
asks.<br>**The real diagnosis was underneath both halves of that sentence, and it is the general
lesson: adding sine waves together is the right way to build a thing with a few MODES, and the wrong
way to build a STRING.** The chime is three bending modes and the flute is very nearly one tone, so
both are honestly built that way. But what makes a string a string is that its whole spectrum darkens
*continuously* as it rings, and with sines that has to be typed in rather than happening. Measured,
that is exactly what was absent: the old guitar's brightness ran **443Hz at the strike down to 264,
against a fundamental of 262** — very nearly a pure tone from the first instant, with no bite at
**all**. That flat, dark, perfectly smooth thing is what a synthesiser sounds like, and it is why both
voices read as one.<br>**So the guitar is a real string now.** A wave travels along it, reflects off
the bridge and the nut and comes back a little duller each time: a delay line one wavelength long, fed
back through a filter that takes the top off. Every harmonic and the entire brightness collapse fall
out of that for nothing, because it is what the object does. **The string is there TWICE** — a real one
vibrates in two planes at once which bleed into the bridge at different rates, and that is where a
plucked note's double decay and its faint beating both come from; one loop gives neither. Measured
after: **2043Hz down to 427**, rings 3.4s at C4, 2.2 at G4, 1.3 at E5.<br>**Web Audio cannot do this
live and that is a hard limit, not a preference**: a feedback loop through a `DelayNode` is stuck at
128 samples minimum, which is 2.9ms, so the highest note it could tune to is 344Hz. The box only ever
plays eight notes, so each string is worked out once and kept. That turns out to be the CHEAPEST voice
of the four to play — at 6x slower than a desktop the worst frame gap with the guitar chosen is
**188ms against the chime's 235**, because eight buffer sources are lighter than eight stacks of
oscillators. One string costs 149ms to make on that processor and eight cost 367, so only the note
being played is waited for and **the rest are made one at a time behind the running piece** — bowl's
and fireflies' bargain, for bowl's and fireflies' reason.<br>**Three things went wrong building it and
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
loop. Attack **3179Hz**.<br>**The honest limit on all of this: these were tuned by measurement because
I cannot hear them, and she can.** Every figure above says the guitar is now a string and not a stack
of sines, which is a real and checkable claim; whether it sounds like a *guitar* is hers alone, and
this was handed to her as rendered audio rather than as a chart for exactly that reason.<br>**Measuring these needs the functions pulled out of the file at test time** rather than
re-typed into a harness, or the harness and the page drift apart and the figures stop meaning
anything; and an `OfflineAudioContext`'s clock does not advance until it renders, so everything
scheduled at `currentTime` lands at zero together — which is what makes the eight-note pile-up easy to
measure and single notes easy to get wrong.<br>The icons are **drawn, not emoji**, deliberately: the
only flute emoji arrived in 2022 and a Kindle Fire would show an empty box where it should be.<br>**The
rabbit is grey.** Her call — white was the brightest thing on the page, brighter than the disc or the
brass, so the eye went to the tempo control before the music box. **It was greyed with a CSS filter and
that did not hold**: her report off the Windows tablet, *"the rabbit is still white"*. Windows draws
emoji as colour glyphs and will not put a filter over one, so the fix worked on the machine it was
written on and nowhere else. **The tortoise and the hare are drawn now**, in the same stroke and the
same `currentColor` as the four instruments beside them — which is the very reason those were drawn.
The general rule, and it is stronger than the site's usual emoji-over-text preference: **if an emoji's
COLOUR matters, it cannot be an emoji.** A filter over a colour glyph is a fix that only works where it
was written.<br>**And it was clipping.** Eight
rings can be pinned on one step, and eight notes together measured nearly **three times full scale**,
1.2% of samples squared off flat — a buzz over the note, and present long before the new voices. A
`DynamicsCompressorNode` is the obvious answer and is the WRONG tool: ~6ms of lookahead and gain
riding left the chime **silent for its first 5ms** where the live page is already at 93% of peak, and
moved the peak from 6ms out to 74. That is not a level change, it is taking the strike out of a
struck instrument — and it is only visible if you measure the attack envelope rather than the peak. A
**waveshaper** has no lookahead and no attack or release at all: this curve is exactly y=x up to 0.75
and bends only above it, so a single note passes through sample-for-sample unchanged and a pile-up is
rounded instead of squared. Eight notes now peak at exactly 1.0 with **zero** samples over, on all
four voices, and the chime's attack envelope is unchanged (peak at 5.8ms before and after).<br>The
page also **grows to its own content now**, as kaleidoscope does: the instrument row put the last 26px
of controls off the bottom of a 3in phone that could not scroll to them. Desktop, an ordinary phone
and a Kindle are unchanged and do not scroll. |
| `pendulum/index.html` | ✅ | ✅ | A **Foucault pendulum**, its swing slowly turning with the Earth; real-photo globe with a locator search<br>**Done** — precession, swing and pin ring all verified by measurement against the real physics.
Aug 2026 it was given a **real-world-time** checkbox (the clock face beside the ∞): ticked, the plane
precesses at the true Foucault rate off the actual clock — Earth's turn times sin(latitude) — and the
speed slider stands down. **It stores nothing.** The angle is a pure function of the clock and the
latitude, and so is the whole sand trace, so ticking it (or changing latitude, or resizing) recomputes
what the plate would have drawn since local midnight in one pass and lays it down. The honest caveat,
which is why it's a checkbox and not the default: at the true rate the turn is very nearly
imperceptible, the better part of a day for one rosette, and the trace comes out as swept ground
rather than separate lines because successive passes land 0.007° apart — closer than a grain is wide.
The swing itself stays exactly as lively as ever.<br>**The rate was wrong, and had been since the checkbox was added.** She suspected the
piece after real-time arrived and asked for it checked before running it on the machines; she was
right to, though not about what. `DAY=86400` — the **solar** day — was driving the precession, and
what a Foucault plane turns against is the **fixed stars**, so the day that governs it is the
**sidereal** one, 86164.0905s. It is why the textbook figure is 15.041°/hour and not a round 15.
Measured on the running page before the fix: a full turn at the pole took **24h 00m** against the
real **23h 56m 04s**, and every latitude ran **0.27% slow**. After: 23h 56m 04s exactly, and the
rate matches 15.041·sin(lat) at 90, 60, 51.5, 30, 0, −34 and −90°, with the sign right in both
hemispheres. Invisible to anyone watching — about a degree of lag after a whole day — and wrong all
the same, which is the standard this piece was signed off against. The same constant also drove the
manual speed-slider mode, so that is now right too.<br>**The hiccups she expected are not there**, and
that is measured rather than assumed. Ticking the box, moving latitude and resizing each re-derive
the whole rosette in one pass; worst frame gap on a desktop 73ms, and on a Kindle-speed CPU 129ms
when the box is ticked, 30–91ms otherwise — one hitch, at the moment you ask for it, never a freeze.
`rebuildRealTrace` clears its own pending flag on its first line, so it cannot run every frame, and
the rebuild is deferred while the globe is being dragged so it happens once on release. After all of
it the angle still equals the pure clock function, so nothing accumulates or drifts.<br>**"It looks as
if the line is moving like a clock hand, not responding to the swings."** Her report on the real-time
view, and the impression is right even though the swing under it is not: measured with the box
ticked, the bob travels its full 287px each way and passes the centre 6 times in 10s — a 3.4s period,
**identical to the ordinary mode**. What she was actually looking at is the swept sand. Since local
midnight the plane really has turned ~139°, so the plate really is worked across two opposite 139°
sectors — correct, and it reads as a pie chart, because a filled sector with a hard radial edge
creeping round a circle is the visual language of a clock hand.<br>The sand's own signature was the
part that was wrong. A swinging weight is slowest at the ends of its swing, so working goes as 1/v ∝
1/√(A²−r²): a hard pile-up at both turning points and a middle barely touched. The rebuild's gradient
ran **0.20 at the pivot to 0.44 at the rim — barely two to one, near enough a flat fill**. It now
follows the real curve, 0.085 to 0.527 (clamped, because the true curve is infinite at the turning
point), so the rim band is the brightest thing on the plate and the body is faint.<br>**A temporal
fade was tried and backed out, and it is worth knowing why before anyone tries it again**: fading the
sweep from settled at the far end to fresh at the leading edge takes ~18 stacked wedge fills at an
alpha of a few thousandths each, and the canvas **dithers alpha that low** — the whole region came
out crosshatched with stipple. Noise instead of sand is worse than the hard edge it was meant to
soften. Doing it properly wants an angular gradient (`createConicGradient`), which the older browsers
on her bench may not have; the way in, if it is ever wanted, is conic where it exists and the flat
fill where it doesn't.<br>**Still open, and hers**: whether the sector now reads as sand or still as a
dial. The geometry is honest — that ground really has been worked — so this is a question about the
look, not a fault to fix. Her word on the change was ***"it's better"*** — which is an improvement
banked and not a verdict, so **don't revert it and don't treat it as settled either**.<br>**"The line
moves AHEAD of the pendulum swing."** Her report on the speed-slider setting, Aug 2026. Measured, it
never does — the bob sits on that line to within **0.07° over 658 frames**. What runs ahead is the
**ratio**: the slider turns the plane without touching the swing, so at its default the plane turns
**1.87° per swing where in life it turns 0.009°**, and a rigid full-diameter line at constant
brightness is what made that read as a hand sweeping a dial. There is no way round the ratio — speed
the swing up too and it is a blur long before the turn is watchable; a real one is about one turn per
25,000 swings, which is why the honest setting is the clock face. So the LINE went instead, her call:
**a short trail behind the weight**, which is ground it has just crossed and so can never reach ahead
of it. Held to a fixed **length**, not a fixed time — the bob is nearly stationary at the ends of its
swing, which is exactly where the pins are and where the swing's direction most needs reading.<br>**And
the pins were the wrong way round**, which is what actually made the piece unreadable. A **fallen** pin
was drawn as a saturated brass bead at full opacity — the brightest thing on the plate after the bob —
and a **standing** one as a stroke at alpha 0.26. So a ring of bright beads sat over exactly the ground
the swing had already crossed and read as *the pins are still here*, the plain opposite of what the sand
beneath was saying. Nothing was wrong in the model. On a real ring it is the brass tops of the upright
pins that catch the light and the knocked ones that lie dark on the floor, and that is what it draws
now — **brightness and shape both**, an upright being a short stub with its head close in and a fallen
one a long shaft pushed well out with a dull head at the end. Her sentence is the general rule and
belongs beside *reads as broken*: ***"i get that it has to be true, and that's important, but if it's
incomprehensible to look at that doesn't teach anything."***<br>**The card was reshot**, and it was
worth doing because the old one was **a picture of the two faults she had just had fixed** — the
full-diameter line and the swept sand reading as a pie chart, with a slider left in the frame as well.
Anyone browsing the case was being shown the broken one.<br>**The honest trouble with a truthful
pendulum card, written down because it will come up again**: at the 40x53 the shelf's plate rows use,
the old card read clearly and the new one nearly vanished — the old was legible BECAUSE of the bug, a
flat-filled bright sector at full opacity, where the real rosette is thin lines kept faint on purpose
by the dwell curve. Running it longer barely helps: doubling the sand (60s to 120s of the ∞ trace)
doubled the lit pixels and changed almost nothing at thumbnail size. What did work was **cropping so
the plate fills the card edge to edge** rather than sitting at 79% of its width, which puts the rim
band — the brightest part, by the dwell curve — at the frame's own edges. Shot with ∞ ticked and the
speed at 100 for about two minutes, which is what gives a full rosette with pins still standing as
well as knocked. It is a quieter card than gyre's, and that is correct: it is a quieter piece, and the
loud version was the lie.<br>**The real-time tick was unreadable, and it is the white rabbit exactly**
— found Aug 2026 by sweeping for it rather than by her hitting it. The 🕰 showed ticked from unticked
through `color` and `filter:saturate()`, and **a colour emoji is a little bitmap the font hands over
whole**: it ignores `color` on *every* platform, and Windows ignores `filter` on it too. So the only
thing left saying whether the piece was running on the real clock was a faint glow — on a control that
carries state. The ∞ beside it is a plain text glyph and dimmed properly all along, so the two halves
of one control behaved differently and nobody noticed. It is a drawn mantel clock in `currentColor`
now, so the existing rules do what they always meant to; the glow became a `drop-shadow` since there is
no text left to shadow. **The colour is the cue and the glow only the flourish**, which is the way
round it should be — the reliable thing carries the state. |
| `storm/index.html` | ✅ | ✅ | A **storm glass** whose crystals form and clear with the visitor's real changing weather (open-meteo)<br>**Done**, and the piece that finishes instrumenta. Fifth through her four-device test, Aug 2026,
and four things came out of it.<br>**The needle lied whenever it had nothing to say.** Untranslated,
`#baro-needle-g` sits at x=0 in its own SVG — off the left-hand end of the printed scale, past
STORMY, below 950 — so between page load and open-meteo's first reply, and permanently whenever
the weather could not be reached at all, the dial showed a catastrophic low nobody had measured
while the readout beside it honestly said nothing. Correct underneath and a lie to look at, which
is the *reads as broken* class the standard below names. It is not drawn until it has a pressure
to point at, and the first placement suppresses the .9s sweep so it is never seen travelling up
from a position it was never at.<br>**The tendency is a mark now, not a sentence** — her call, and
the last prose on any piece. Chevrons pointing where the pressure is going, **one per rung of the
WMO tendency scale**: slowly, plain, rapidly, very rapidly, with a level bar for steady. Four, not
the three she first sketched — three would have had to merge two speeds of a real scale, and the
scale is the reason the readout is trustworthy. The words are still exact and still there: touch
the mark and it gives them, touch it again or anything around it and they go, which is galileo's
own rule for a popup. The steady bar cannot be read as the reading's own dash, since that shows
only when there is no pressure at all — and then the mark is off the page.<br>**The brass hand got
candler's pin treatment**, her own reminder that this was already settled: a transparent rect
inside the hand's `<g>`, no brass moved. Two things differ from a pin. The SVG is scaled to the
screen, so the rect is measured in the units that make it a real 44px wherever it is and
re-measured on resize; and on the 3in phone the whole dial is 39px tall, so it takes the dial's
full height and stops. Measured: 0x0 on desktop, 44x44 at 390 and on the Kindle, 36x39 on the 3in
phone, against brass of 11.2 / 7.3 / 4.5px. A tap still never moves the hand — only a drag — and
the drag keeps the offset it was taken hold of at, or a wide grab box would snap the hand out from
under a thumb.<br>**And the needle was swallowing the grab.** It is painted after the hand and its
stroke took pointer events, so a grab landing at the needle's own position never reached the hand —
which is exactly where the hand is meant to be parked, since setting it against the needle is the
whole use of the instrument. Half of the piece's one gesture was dead. The needle is a reading, not
a control, and takes nothing now.<br>**The 3in phone: the key was eating the piece.** Eight buttons,
each an icon *and* a 24px thumbnail of the glass, wrapped to three rows and took 169px of a 350px
screen — and `#scene-wrap`, an ordinary flex item, gave way to it and shrank to **13px across**.
Eight little glasses on screen, every one of them bigger than the real one. Below 380 the
thumbnails come off and the icons stay, four to a row: the thumbnail is the one genuinely redundant
thing at that size, since the glass itself is a tap away and changes instantly, and it was being
paid for out of the glass's own room. Nothing hidden, no new gesture, nothing to discover. Glass
13x22 -> 91x155 at 240x350; above 380 nothing applies and the page is pixel-identical, measured at
380 and 390.<br>**Sideways on that phone is 180px tall and no arrangement fits it** — the barometer
alone is 88px of it. That one is allowed to **scroll**, which is the answer she took for
kaleidoscope when content genuinely did not fit: the glass is held to a size rather than shrunk to
a sliver, and everything is reachable. The `(orientation: landscape)` qualifier on that rule is
load-bearing — the same phone is 350px tall in portrait, where the compact key already fits with
room to spare, and without it the rule set a page scrolling that didn't need to and pushed the
glass up under the two brass discs. A Kindle in landscape is 476 tall and never reaches it. |
| `crystal.html` | — | — | A crystal (not linked from the landing page) |
| `chest.html`, `chest-open.html` | — | — | Dead apothecary-chest drafts she turned down; kept as a record, not linked |

### The wall, and how it got there

The pieces are split into five groups: **instrumenta, tactilia, systema, natura,
phenomena**. Those are her words, off her own handwritten notes — *instrumenta*, not
"tools". Which piece belongs in which group is hers, and so is the list; don't reshuffle it.

**The order down the wall is hers and is not the order they were in on the case.** Top to
bottom: **tactilia, systema, natura, phenomena, instrumenta** — instrumenta at the foot because
that shelf sits in the darkest part of the picture and its cards are the darkest of the twenty,
so they show up better there. Within a shelf the order is hers too (moths, birds, ant, fireflies;
rain, pendulum, bowl, lamp, chladni), set by eye so the pale and dark cards alternate rather than
clumping at one end.

It began as an apothecary **chest** of drawers. Three chest variants were built and she
turned all three down — *"none of it feels right"*. The shelf was her idea instead: *"what
if we put 'sagne' in the oval, the cards lined up face front on each shelf, and the name of
the type on the plate?"* — and it worked first time. `chest.html` and `chest-open.html` are
those dead drafts; they are not linked from anywhere and are kept only as a record. Don't
build on them, and don't re-propose a chest.

The photograph is hers too. She generated the plain shelf, and the ornate one it borrows
from. Three things were done to it in Aug 2026, all of them recorded here because they are
invisible in the file: the shelf spacings were evened (100/185/175/170/131 -> roughly 152
each) by a piecewise vertical remap that moves only the back panel and leaves the boards
rigid; the sagne oval and the crown and plinth scrollwork were lifted off the ornate photo
and applied **as relief** — the carving's light and shade transferred onto this shelf's own
walnut, rather than the other photo's darker wood pasted over it; and the bottom shelf,
which had no vertical front edge at all, only a floor, had the fourth rail cloned down to
the floor line so its plate had something to sit on. The scripts that did all this are gone
with their scratchpad, so treat `shelves.jpg` as the source of truth.

**A card stands in a mount, not merely on the board.** Her idea, off a photograph of a real
display stand: an upright behind the card, an arm over its top edge, another taking its weight
underneath, on a base that bears on the board. It is drawn as one SVG rather than photographed,
so it stays crisp at every zoom, and it is what stops the cards reading as hovering a hair above
the shelf. The upright must stay **behind** the card — an absolutely positioned stand paints over
its own picture otherwise, and every card gets a black bar down the middle.

**The case was worked on to get there,** and none of it shows in the file: a fifth compartment
was spliced in (her generator gave four), cutting and rejoining inside the dark under a board
where a seam cannot show, then re-grading the whole case so the light still falls away top to
bottom; the panelled cupboard doors below were cut off at the counter's own front edge, her call;
a band of the case's own near-black was added below the counter for the **?** disc to sit on;
and the top compartment was compressed from 204 to 176 so the top of the unit comes down onto the
first shelf — also her call, *"it does a good job in drawing the eye down"*. The lit openings now
run 176, 176, 202, 202, 211: tactilia is held to 176 by a shadow cast under the first board, which
none of the others have, so **the top shelf is not the odd one even though it can look it**.

**There is light on the wall behind the case**, her ask, and it was needed for a reason
that is invisible until measured: the photograph's own surround is *darker* than the wall it
is laid on (2,5,13 against the wall's 16,21,33), so the case's outer edges had nothing to be
seen against and the whole unit read as a dark patch with no silhouette. The lift is about
5/255 at the sides. Two things about it are load-bearing. It must **not** be given
`z-index:-1` — html and body both carry the wall colour, and a body background paints *over*
a negative-z-index descendant, so the glow simply vanishes; being first in the stage and
unpositioned in z, it lands behind the frame on document order alone. And **the gradient has
to reach nothing before the box ends**: the first version's ellipse was wider than its own
element, so the paint was cut off with about 5% alpha still in it and drew a hard vertical
band down the wall, which she photographed. It fades with the case — away on a zoom, the way
the ground shadow does, and down to .15 behind the tray, or a halo hangs round a case
deliberately dimmed to almost nothing.

The **?** is a brass disc of hers (`shelfdisk.png`) with the question mark engraved into it,
sitting on that band of dark below the counter; the case stands on the floor of the page rather
than floating in the middle of it. The *sagne* oval is screwed **to the front face of the top
rail**, edge to edge on it — not floating in the shadow of the recess behind, which is where it
first went and which she caught.

**The favicon** is her own candle, cut off its ground and wrapped inside `favicon.svg`, so
every page that already links to that file picks it up without a reference changing. The
same cut-out makes `apple-touch-icon.png` and `icon-192/512.png` on the site's navy.

**No words on it that aren't cut into it.** The only lettering on the shelf is engraved
on the brass: *sagne* on the oval and the five group names on the plates. The card names that used to float over a piece on hover were removed Aug 2026 —
this site doesn't caption its objects — and so was the text **back** button; the way out
of a zoom is the plate of the shelf you're in, a tap on the dark around the case, or
Escape. The plate names size themselves to the height of the brass and sit centred in it — they
were tracked out across the width for a while, and it read as spaced-out rather than
engraved. The oval's
position comes from the brass measured out of the photograph by hue, not by eye. Don't add
a visible label to this page.

**The two sayings** the old flat landing page carried are still here, word for word, and
still only on request: *sagne* on the crown opens the "tools and toys for twiddling" one,
and the **?** on the plinth opens the "designed by one person" one. Aug 2026 she moved the
two sentences about the lack of text out of the **?** and onto the end of the *sagne* one:
they are a statement of what the site doesn't have, which is what that saying already is,
and the **?** is left as a plain colophon. Her answer to the worry that announcing "no
explanations" is itself an explanation: *"I don't think it's too ironic, considering it's
the only place there's an explanation for anything at all."* The case dims
behind whichever is open. They're the one exception to the rule above, because she asked
for them.

**Getting across, not just in and out.** Each piece carries two brass discs, both cut
from `shelfdisk.png`. Left is the way back (an arrow, to the case). Right brings out the
five shelf plates — the very plates off the case, each her own brass cut to its own name — and
rolling one unfolds that group's pieces beside it. A mouse hovers to unfold and clicks the
plate to go; a thumb taps once to unfold and twice to go, the same bargain the case itself
strikes. A plate links to `/index.html#<group>`, which opens the case already zoomed to
that shelf. **That block is generated** — run `python3 tools/shelf-tags.py` from the repo
root after changing the shelves table, and it rewrites the marked block on all 19 pages
from the table itself. Don't hand-edit between the `shelf-tags` markers; the next run
overwrites it.

**The twenty cards behind those plates are held back until a plate is opened, and that
is worth knowing because it was costing every page on the site.** They are 6.2MB of card
art and not one of them can be seen until the disc is pressed — but each page was
fetching all twenty on load, ahead of the piece's own assets. It surfaced as bowl not
loading at all on the 3in phone (its own bowl photograph was queued behind them), and it
was slowing down all nineteen. They are held behind `data-src` and swapped in when the
plates open. **`loading="lazy"` alone is not enough and was tried**: it is a heuristic,
not a promise — the same page deferred them on a throttled connection and fetched all
twenty on a fast one, because the browser's idea of "near the viewport" widens with
bandwidth. The attribute is still there as a second line for anything that scrolls them
into view another way.

**And the landing page's OWN twenty cards are small versions now** — the fault above, one
level up, on the one page where the cards cannot be deferred because they *are* the page.
Aug 2026, found by measuring what the front door fetches rather than by anyone reporting it.
The wall was sending the full card artwork — up to 756x1100, **5.99MB** — to draw a card at
**201x290 real pixels at the very largest**, measured across every screen from the 3in Jelly
Star to a 2560 desktop with hover's 1.14 included. About thirty times the picture any screen
could show, twenty times over. Measured on the simulated Jelly Star (240x350, 1.6Mbps, CPU
6x slower): the shelves themselves appeared at 0.7s and then **stood empty while the cards
trickled in until 25.9s**, the page settling at 35.2s. It is **4.3s and 6.8s now, on 1.30MB**.

The wall gets `<slug>-card-sm.jpg` from `python3 tools/card-thumbs.py` — 259KB for all
twenty — and the full artwork is fetched **on the first zoom of any kind**, which is the only
place a card is ever drawn at its own size (on a Retina Mac a zoomed shelf puts a card exactly
1:1 with its photograph). The shelf being opened comes first, then the rest **one at a time**,
because twenty at once is worse on the machine already struggling: bowl's and fireflies'
bargain, for bowl's and fireflies' reason. If a full picture fails to arrive the small one
simply stays — a slightly soft card beats a blank one.

Two things about it are load-bearing. **`CARD_ART` carries each picture's TRUE size and is
generated** (between the `card-art` markers — don't hand-edit; `tools/card-thumbs.py` rewrites
it): three places cap how far a card may be enlarged at its own pixels, and read off the small
version they would cap a zoom far too low. It is keyed off the picture's own **filename**, not
the piece's name, because candler's card is `candle-card.png` and the two do not always agree —
keying it by slug silently capped candler's zoom at the 640 fallback. And **the wall is not
softer for it**: measured per card at 390px@3x, mean difference 1.44/255 and sharpness
*up* 11.7%, because one clean Lanczos downscale beats the browser scaling 440px to 150 in a
single step. Verified pixel-identical (0/255, worst case) in all three zoomed states —
desktop shelf zoom, the phone tray, and a card held out of it.

**FIXED Aug 2026: the site no longer blocks on Google Fonts.** What it was, and why it went
unseen for so long, is below; `python3 tools/self-host-fonts.py` is what changed it. The four
families — Libre Baskerville, Cormorant Garamond, Jost and Spectral — are now the site's own,
24 woff2 files in `fonts/` at 617KB in total, latin and latin-ext only. Per page that is 20KB
where only Libre Baskerville is used and 119KB at galileo's worst, shared across pages after the
first. Measured on the landing page with that host hanging: **first paint 15.1s before, 88ms
after**; with it merely slow, 12.7s against 196ms. Verified that all four families really load and
apply rather than silently falling back to a system face.

**It moves two pieces by half a pixel**, and this was checked rather than assumed: galileo's
instrument column and conometer's scene sit 0.5px higher, because those two size themselves in
script at load and now do it with the real metrics already in hand. Measured with the button work
absent, so it is the fonts and nothing else. Nothing anywhere else on the site moves at all.

**If a face is ever added**, put it in the page as an `@import` as before and re-run the tool; it
fetches only what it hasn't got and rewrites from the same source.

**What it was, kept because the failure mode is the instructive part: the whole site blocked on Google Fonts.**
Every page links two stylesheets at `fonts.googleapis.com`, and a stylesheet is
render-blocking — so if that host is slow, throttled or unreachable, the page is a blank dark
rectangle until the request resolves or gives up. Measured in a sandbox where it is blocked:
**nothing at all happened for 12.5 seconds**, not the wall, not a plate, not one card, on
both the old page and the new. On an ordinary connection it answers in a moment and none of
this shows, which is exactly why it has never been seen. The fix, if it is ever wanted, is to
self-host the faces — which is what was done. The site now has no third-party dependency but the
weather API, and that one fails out loud by design where this one failed silently.

**Interaction.** On a touch screen it is three taps — shelf, then card, then open — because
a phone cannot show a card big enough to read; her idea, and the right one. With a fine
pointer a card opens on the first click instead, and the shelf zoom stays reachable from the
name plates. If you change the picture, the zoom transforms recompute themselves from the
measurement table; nothing there is hand-typed.

**The zoom fills the page, not the case.** Aug 2026, hers off the desktop — *"it needs to be
a **lot** bigger, and the other shelves need to be more greyed out."* The case is a tall
portrait box and a shelf is a wide landscape strip, so a shelf brought forward inside the
case's own outline could never use more than the case's width: 695px of a 1440 screen,
less than half of it. **The window widens on a zoom and the case keeps its own proportion
inside it** — `#case` is centred at its own width rather than filling `#frame`, which is
why widening the frame no longer stretches the photograph, and unzoomed the two are exactly
the same width so nothing moves. Measured at 1440x900: the cards spanned **639px and now
span 1285**, a card 102px tall against 205. Two ceilings hold it honest, the same two the
card zoom already keeps — never past the card art's own pixels, and never so far that the
shelf zoom starts doing the card zoom's job. **On a Retina Mac the first of those binds**
and a three-card shelf comes to 1112px rather than 1397, the card exactly 1:1 with its own
photograph; that is correct, not a shortfall.

**And then it ran off the right-hand edge of the screen**, her report Aug 2026 — *"the shelf
zoom is now off to the left and missing the right side"* — with a screen capture showing a
three-card shelf of which only two cards were on the page at all. The cause is the sentence
above, taken too literally: the zoom **widened the frame itself**, with a floor of the case's
own width. That floor was harmless while `#case` was as wide as the window — but the Mac fix
made the case `height / wallratio`, and on any ordinary desktop window that is **wider** than
the window, which is the whole point of it (the wall fills the window and the surplus comes
off its ends). So the floor pushed the frame past the screen every time, anchored at the left.
Measured at 1000x533, a shelf of three came out **1386px wide in a 1000px window** with its
third card entirely off the page; at 1440x900 the frame was **2340**, at 1920x1080 it was
2808. The two ceilings above were never reached, because the floor beat them.

**The frame stays at the window width now and only the SCALE follows.** What `zoomWidth`
returns was never a window — it is the width the shelf's cards are aimed at, and conflating
the two is the whole fault; the frame's `width` is no longer touched on a shelf zoom at all.
Measured after, on all five shelves at 1000x533, 1440x900 and 1600x1000: **nothing over
either edge, and the margins equal to the pixel** on both sides at every size. The un-zoomed
page is **pixel-identical** at both sizes. The cards do come out smaller than the broken
version drew them — that is the part that was off the screen.

**And the other four shelves go back as furniture, not as cards.** Dimming the off-shelf
cards alone (which is all it did) left four brightly lit empty shelves behind them — the
wood is most of what the eye sees. A near-black sheet is laid over the whole case with a
band cut out at the shelf in focus, so wood, brass and cards go back together. **The band's
top edge falls on the BOARD above, not in the compartment**: that board's front face carries
the plate of the shelf above, which hangs a little below its underside, so a band starting
at `ceil` alone put another shelf's name in the lit strip.

**A card stands on the board it can be SEEN to stand on.** Also hers, and the diagnosis is
hers: *"the top shelf looks as if the stands are hovering… the eye view only makes sense if
one is looking down on the shelf."* The eye is a little above the top board, so how much of
a board's lit top surface is visible grows all the way down the case — measured off the
photograph by luminance, **0px on instrumenta, 4 on tactilia, 29 on systema and natura, 40
on phenomena**. `seatBack` is a *projected* depth, so one constant of 10 put the top shelf's
stands 10px above a front edge with nothing behind it. It is **per shelf** now (`seat:` in
the table, `seatBack` the fallback), about a third of that shelf's own visible depth, which
on the top shelf is the lip itself. Un-zoomed, a pixel diff at 1440x900 shows exactly two
bands changed — the instrumenta cards and the tactilia cards — and a phone and a Kindle take
the tray rather than the zoom and are untouched.

**On a 3-inch screen the case's plates are unreadable — and it does not matter, which is a
correction to a measurement.** At 240x427 nothing is below the fold (the whole cabinet is on
screen with room above and below) but everything scales off the screen's WIDTH, so the engraved
plates come out **6px** tall and the cards 19x28. A session measured that and reported the case
as needing a small-screen arrangement. She then opened it on the actual phone and found the
opposite: **touching anywhere zooms to that shelf, and the zoomed tray plate fills the foot of
the screen and is perfectly readable** — her word for it was "awesome". The tiny plates on the
un-zoomed case are decoration at that size, not the way in; the way in is the card, and the card
works. Don't "fix" the 6px plates, and don't trust a static tap-target measurement on a page
whose whole interaction is a zoom.

**A `<button>` carries the browser's own button face** (`rgb(239,239,239)`), and four of them on
this site show a cut-out with transparent edges over it — so a pale rectangle sat behind the
brass. `#trayplate` here, warmler's `#finishTrigger`, and chimes' two `.matTrigger`s. She caught
it on the phone, on the zoomed shelf plate, where the transparent margin is widest; on the small
swatch triggers it was a faint rim nobody had noticed. It survived this long because the zoomed
view is mostly a TOUCH path — with a mouse a card opens on the first click, so a desktop session
rarely sees that plate at all. If you make a brass cut-out into a button, clear its
`background-color`.

**Live-data pieces** — `galileo`, `conometer`, `windower`, `storm` — read the visitor's
**geolocation** and call **public APIs** (`api.open-meteo.com`). If you edit these, keep that
working; don't break the geolocation or the fetch. **All four must fail out loud, and wordlessly.** They count
consecutive failures, ignore a single blip — open-meteo refreshes every ten minutes and one
miss is normal — and from the second show two marks at the top of the piece: an exclamation
inside a circle struck through with a bar (can't), and a turning circle beside it (going back
for it by itself). No sentence — that was the first version and she replaced it, rightly: the
old wording claimed it was "still trying quietly" while showing nothing that was trying. The
marks are generated — run `python3 tools/fetch-trouble.py`, don't hand-edit between the
`fetch-trouble` markers. A reply that arrives carrying no reading counts as a failure too. Going quiet instead would mean showing an old sky as though
it were the one outside, which is the exact promise this site makes not to break. Storm was
the one that didn't, until Aug 2026.

**The location flag answers Enter itself** on all seven pieces that carry one (`conometer`,
`galileo`, `windower`, `storm`, `pendulum`, `chimes`, `fireflies`). A one-field form submits on
Enter in a desktop browser, but the Go key on some Android keyboards leaves the form alone, so a
typed-in place did nothing and said nothing. The keydown handler prevents the key's own default,
which is what stops a browser that *does* submit from searching twice — measured, one geocode
call per Enter on all seven.

**Where the flag's reply landed under the browser's own bar.** `height:100%` with
`overflow:hidden` is the whole screen with the address bar counted as though it weren't there,
and the reply line is the last thing on the page — so on a Kindle you could type a location in,
the piece would go and fetch it, and the line saying where it had gone was off the screen. That
is what "no location response" turned out to be. `conometer`, `galileo` and `storm` now lay out
to `innerHeight`, held steady while a text field has focus so an on-screen keyboard can't resize
the piece under someone typing. **The other four don't need it and weren't touched**: `pendulum`,
`chimes` and `fireflies` anchor their docks with `position:fixed`, which a mobile browser keeps
inside the visible area on its own, and `windower` has no `overflow:hidden`, so its page simply
scrolls. Measured on all seven before and after; the desktop layout of every one is identical to
the pixel.

**Don't add a second weather provider as a failover.** It was considered and rejected: the
alternatives need an API key, and a key in a static page is readable by anyone and gets
rate-limited or revoked, which is a worse failure than the outage it insures against. Failing
honestly is the answer here, not a second source that can quietly disagree with the first. (These are also why a *faithful* Preview matters — a plain
screenshot can't show live weather.)

### Touch targets: a slider is a mouse dimension

**HER STANDING INSTRUCTION, Aug 2026, and it applies to work you have not been asked
about:** *"in future please make sure all small buttons and sliders are suitably (and
invisibly) fixed."* So this is not a job that waits to be raised with her. **Any piece
you touch, and any control you add, comes with a thumb-sized target already on it** —
and the parenthesis is the hard half. *Invisibly* means the painted thing does not move
or change by one pixel; a target that is easier to hit and looks even slightly different
has not met the instruction. Both generators below enforce that by measurement, and
`tools/touch-buttons.js` throws away its own rule rather than ship a visible one. If you
add a control by hand, run them.


Most of this site's sliders were painted as a **3px hairline**, which is right for a
mouse — a mouse is pixel-precise, and a hairline reads as elegant. A thumb is about 9mm
across: it can only catch the little knob, and it covers the whole track the moment it
lands. Aug 2026 every slider on the site was given a **body a thumb can catch, without
moving the painted line by a pixel**: padding grows the box, `background-clip:content-box`
keeps the paint in the middle strip, and a matching negative margin gives the space back so
nothing on the page shifts. It applies only under `@media (pointer: coarse)` — a desktop is
untouched.

That block is **generated** — run `node tools/touch-targets.js` (needs `playwright-core`
and the site served locally; see the header in the script). Don't hand-edit between the
`touch-targets` markers. Each slider grows only as far as **half the gap to its nearest
neighbour**, so no two ever overlap and steal each other's taps; the widths come from
measuring the real page at 390px, not from guessing. `chladni`'s notch slider is skipped —
its photographs already make it 46px.

**The generator is NOT idempotent unless you keep it that way, and getting this wrong is silent
and destructive.** Aug 2026 it was re-run and every page came out worse: the block from the last
run is *in the page*, and its negative margins are part of the computed style, so measuring on top
of them compounds them — padding stays 15px but `margin-top` goes −28 to −43 on a second run, −58
on a third, dragging every slider up the page. It also inflates the measured height, so a slider
already grown past the 40px cut-off is skipped and freezes at whatever it happened to be. The tool
now **removes its own `<style>` before measuring**, so a run starts from the page's own layout and
running twice gives the same answer as running once. The tell that it had happened at least once
already: the page's own slider margin recovers as **+2px** on every piece from a clean measurement,
and the blocks that were live recovered as **−13**.

**And re-running it now moves the painted line by 1–2px on pieces whose blocks were made the old
way.** That is the tool being right and the old blocks being wrong, but it is still a visible change
to signed-off work — so Aug 2026 the corrected blocks were applied to the **eight pieces she had not
yet tested** (`musebox`, `chimes`, `lamp`, `pendulum`, `birds`, `fireflies`, `moths`, `ant`) and the
twelve she had passed were deliberately left alone. Anyone re-running the tool will see those twelve
change; that is expected, and it is her call whether to take it. Measured before and after on all
four small screens: **dock heights are identical**, so the negative margins really do give the space
back and nothing was swamped.

Two things in there cost a pass each and will cost another if forgotten:

- **`border-radius` is measured off the outer box**, so padding eats the rounding off the
  painted strip and leaves the track with square ends. The fix is an elliptical radius that
  gives the vertical axis back exactly what the padding took.
- **CSS scales every radius down proportionally when they don't fit the box**, so a declared
  `4px` on a 4px-tall track is really 2px on screen — and `getComputedStyle` hands back the
  declared figure, not the drawn one. Clamp it to half the height first or the cap comes out
  a different shape from the one it replaced. Getting this wrong is visible: candler's track
  went from a round cap to a tapered one.

Verified by screenshotting every slider against a pristine copy of the site: **16 of 19 are
identical to the pixel**, and the other three differ by at most 5/255 in the dither of a
faint gradient. Nothing moved, nothing overlaps, and the desktop is byte-identical.

**What the corrected run actually fixed**, Aug 2026, measured at 390px under `(pointer: coarse)`:
`ant`'s seven sliders were **3, 7, 9, 14, 18, 18 and 23px** and are now 26–33; `fireflies`' five
were **3, 4, 5, 19, 20** and are now 21–30 (its wind slider had no rule at all); `birds`' two were
18 and are now 30. `moths` measured 44–45px before and after — it is the one that was given room
first, and it shows.

**The BUTTONS and tickboxes got the same treatment, Aug 2026** — `node tools/touch-buttons.js`,
the companion generator, run after she made the instruction above a standing one. **95 controls
across 19 of the 20 pieces**, every one now 40–44px where they had been 14–38. The smallest were
candler's three tickboxes at **15x15** — on the piece she uses daily in place of an alarm — musebox's
save and clear at 22x18, lamp's mute at 14x14 and roller's at 17x14.

**Two forms, and which one is used matters.** PAD grows the box with padding and hands the space
back with an equal negative margin; `position` is never touched. OVERLAY makes the host
`position:relative` and hangs an invisible `::after` off it — events on a pseudo-element target
their host, so the page's own handlers pick them up unchanged. PAD is tried first and OVERLAY only
where padding moves something; the run marks overlay rules with a `*`.

**OVERLAY has a cost that is easy to miss and cost a pass to find: making a static element
positioned lifts it ABOVE its static siblings in paint order.** On conometer that pushed the
live/manual toggle over the pinecone artwork and changed 14x19px of the humidity droplet — correct,
tiny, and exactly the kind of thing the parenthesis in her instruction forbids. conometer's toggle
goes in on PAD instead.

**So the tool verifies itself and throws its own work away.** Each rule is screenshotted against the
piece's own rendering and kept only if nothing changed. Three things about that check are
load-bearing, each learned by getting it wrong:

- **A frozen clock and a seeded PRNG are not enough.** candler's flame and lamp's differ from
  *themselves* between two identical loads. Compared byte for byte, every rule on those two failed
  and the run reported "nothing could be grown invisibly" — which was false. The piece is now shot
  three times with no rule applied; wherever any two disagree is the piece animating, and those
  pixels are masked out.
- **The mask needs a margin, and the margin is per piece.** The next frame's flame is not confined
  to the pixels the last three happened to disagree about. Measured on candler: 2 baselines, no
  margin → 31 pixels escape; 3 → 14; 3 with a 4px margin → 0, masking 0.99%. moths needs 10–30. So
  the tool takes one extra clean shot and uses the **smallest margin at which that shot comes back
  clean**, rather than one figure wide enough for the worst piece — which would quietly weaken the
  check on the other nineteen.
- **The masked share is reported per piece and is the figure to distrust first.** chladni masks
  20.5%, rain 15.7%, bowl 15.0%: their controls sit in docks clear of the animation so the check
  still covers them, but a wide mask means a weaker guarantee.

**`moths` is the one piece with no touch-button block, and it is not an oversight.** Its whole scene
moves and its controls run from the back disc at the top to the dock at the bottom, so the moths fly
straight through every one of them — there is no still region to compare. And the margin it needs
is not stable: measured across runs it wanted 10px once, then 20, then 30, so a pass at any fixed
figure is luck rather than proof. The tool refuses it and says so. **Don't "fix" this by widening
the mask until moths passes** — that is throwing away the guarantee to get a tick. If moths is ever
to be done, it needs a different kind of check (its scene is canvas-drawn, so a geometry-only proof
for PAD rules would be sound, since PAD cannot alter paint order), not a looser one.

**`chimes`' rod-material trigger was also dropped**, for the ordinary reason: its neighbour is too
close to grow into without stealing that neighbour's taps.

**`kaleidoscope` and `moths` had to be given room first** — their sliders sat 14px and 11px
apart, which leaves nothing to grow into. Both had space going spare on a phone, so the gaps
were opened (kaleidoscope's `.sliders` to 26px, moths' `#dock` to 26px). That one *is* a
visible change, unlike the rest of this.

**The music button and the docks fight over the bottom-left corner.** The player is `position:fixed` at
`left:18 bottom:16` on all 14 pages that carry it, and a piece's own dock runs the full width of the screen,
so on a narrow one they overlap — and the button wins, being the higher layer. Aug 2026 this was measured
and found on five pieces, two of them **on an ordinary 390px phone**: warmler's finish trigger (the whole
point of the piece) sat 17px under the headphones, and gyre's run toggle sat under them entirely. The fix is
that **the furniture gives way, not the piece**: a `@media` rule lifts `#music` to just above that dock,
by that dock's own measured height. Relocating it to the top-left was tried first and rejected — measured,
that corner is the artwork on ten of the fourteen (the scope ring on kaleidoscope, an icon button on
candler). If you change a dock's height, change the matching `#music{bottom:}` with it. gyre also needed its
dock to **wrap** below 380: the row wants 322px and never wrapped, so the toggle sat 41px off the left edge
of a 240px screen.

**candler's pins are the same fault in another shape.** A pin's picture is about 23 units
tall and a unit is roughly a pixel on a phone, so grabbing one asked for a thumb inside a
23px band — and a near miss doesn't do nothing, it puts a *new* pin on the candle. Each pin
now carries a transparent 44px-tall rect in its own `<g>`; nothing of it shows, and the grab
box went from 70x23 to 82x44. It has to be built inside `pinMarkup`, because `movePinTo`
rewrites the group's `innerHTML` from that function on every drag frame. It cannot swallow a
neighbour's taps that the picture wasn't already overlapping — two pins may legitimately sit
`MIN_PIN_GAP` apart, which is narrower than the pin image itself.

**The music player's track name** was revealed on `:hover`, so on a phone it never appeared
at all — and an invisible element sat there taking taps. It now simply shows while something
is playing (`#musicBtn.playing ~ #musicName`), on all 14 pages that carry the player. That is
not a caption on a piece: it is the visitor's own file's name, not the site's words.

### Asset naming conventions (follow these for any new asset)

- **Card previews** on the landing page: `<demo>-card.png` (e.g. `lamp-card.png`), each with
  a small `<demo>-card-sm.jpg` beside it for the un-zoomed wall. **Don't write the small one by
  hand** — `python3 tools/card-thumbs.py` builds all of them and rewrites the `card-art` block
  in `index.html`. Run it after adding or reshooting any card.
- **conometer** frames: `cone-01.png` … `cone-09.png`, plus `conometer-background.png`
  (frame 1 = fully open/dry, frame 9 = closed/wet).
- **galileo** floats: `floats/<color>.png` — `blue, aqua, green, yellow, orange, red, pink,
  purple, silver`.
- **warmler** finishes come in two files each: `warmler-plate-<finish>.png`,
  `warmler-swatch-<finish>.png` (finish = `brass, copper, aged-brass, aged-copper, gold, silver,
  diamond-plate`). Some `warmler-texture-<finish>.png` files exist on disk from an earlier pass
  but aren't referenced by the page — leave them alone, don't treat them as the convention.
- `favicon.svg` is the shared site icon and lives at the **repo root** (not inside any page's
  folder); pages that use it reference it as `../favicon.svg`. A few pieces (`galileo`,
  `windower`) have their own dedicated favicon instead, which lives inside that piece's folder.
- Each linked piece lives in its own folder as `<slug>/index.html`, with that piece's own assets
  **alongside it in the same folder** — reference them by plain relative path, no `../` needed
  (e.g. `warmler/index.html` refers to `warmler-plate-gold.png`, not `warmler/warmler-plate-gold.png`).
  Match the existing naming when adding new assets. Only the shared root-level files
  (`favicon.svg`, and links back to `index.html`) need the `../` prefix.

### On-page controls: emoji over text

For buttons/labels on a piece itself (not this chat) — save, clear, speed, etc. —
default to an emoji instead of a text word, unless the owner asks for text. Give it a
`title`/`aria-label` for accessibility even though there's no visible label. Matches the
existing tempo controls (🐢/🐇) and keeps pieces free of on-screen instructions.

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

**B. Netlify Deploy Preview — deliberately switched off.** Netlify can give every open pull
request its own hosted preview URL, but that means **two builds per change** (one for the PR
preview, one for the production merge) — and a run of small iterative edits burns build minutes
fast for no real benefit, since local screenshots already cover the review step.
> **Current settings (by design):** Deploy Previews → *"Don't deploy pull requests."* Branch
> deploys → *"Deploy only the production branch."* Together, the **only** thing that ever
> triggers a Netlify build is a merge to `main` — one build per **Do**, never more. Method A (the
> static picture) is the permanent Preview method here, not a fallback. Don't re-enable Deploy
> Previews or branch deploys without the owner's explicit request — it directly costs build
> minutes.

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
- **Netlify:** the **live site** deploys from `main`, and only from `main` — Deploy Previews and
  branch deploys are both switched off on purpose (see the Preview section), so PRs and
  work-branch pushes never trigger a build. The only build-triggering event is a merge to `main`,
  i.e. a **Do**. Don't change these Netlify settings without the owner's explicit say-so.
- A pull request is opened as part of **Do** (and merged). Don't open PRs for anything else.
- **Pushing** goes through the session's git proxy. A **403** on push means a permissions /
  re-auth problem, not a code problem — tell the owner in plain terms ("I've lost permission to
  save to the website — can you re-check my access?") and **don't hammer retries**.
- **If a Netlify deploy itself fails** (e.g. "unable to access repository"), that's a
  Netlify↔GitHub permissions/connection problem, not a code problem — same rule applies: explain
  it in plain terms once, don't loop on fixes yourself, and see the escalation guardrail below.

## Where the device testing has got to

**The programme is hers**: a Rocketbook page per piece, each tested for what it does on **all
settings and at all times of day**, on four machines — her Mac (*frelliple*), a **Windows tablet**,
a **Kindle Fire** and a **Unihertz Jelly Star** (a 3in phone, about 240px across). A piece is not
finished until she has run it on all four. Her words: *"I intend to finish every one of them to the
same standard."*

**Through as of Mon 24 Aug 2026: candler, conometer, galileo, windower, storm, warmler, chladni,
bowl, roller, kaleidoscope, gyre, rain** — her call on all twelve; every fault they turned up is fixed and live, and
the details are in each one's row above. The case itself was worked on the same day: light on the wall behind it, the
white cut line off all five plates, darker arrows in the two discs.

**Twelve through, eight to go**, by shelf: **instrumenta 5/5**, **tactilia 3/3**, phenomena 3/5
(`bowl`, `chladni`, `rain`), systema 1/3 (`gyre`, straight after its two changes — *"gyre works on
everything too"*), natura 0/4. The eight left are `musebox`, `chimes`, `lamp`, `pendulum`, `birds`,
`fireflies`, `moths`, `ant`. `chladni` and `bowl` cost one repair each on the afternoon of
the 24th — the microphone tickbox onto the sound line, and bowl not loading at all on the 3in phone.
Bowl's is the one to remember: it was **two** faults, and the larger belonged to every page on the
site rather than to bowl.

**Her order from here**: **instrumenta and tactilia are both finished** as of Mon 24 Aug — `storm`
closed the first, and `warmler`, `roller` and `kaleidoscope` the second. `bowl`, `chladni` and `rain` are
through off **phenomena**, which leaves `lamp` and `pendulum` there. In **systema**, `gyre` is through and
**`musebox` and `chimes` are repaired and waiting on her devices** — the last two pieces of the day's
work she has not yet run. Chimes needs its rods set to DIFFERENT LENGTHS or the tangle it was
reported for cannot appear at all. Then **natura**, which she expects to cost the most in repairs and
testing — and **it is last on purpose, not by accident**. Her reasoning, in her own words: she is
doing this *personally* over four machines, and she is *"deliberately leaving the 'slowest' ones for
last, so they don't get rushed and are tested in all states"*. All four natura pieces animate
continuously and three run on the clock — birds at sunset, fireflies from dusk to night, moths from
dusk to dark — so testing one is not a pass over its controls but sitting with it through its whole
cycle, on each machine. On a Kindle Fire the thing that bites an animated canvas is frame rate, which
is a fault class none of the pieces tested so far could expose. Budget it for watching rather than
repairing, **don't propose reordering the shelf to get a number up, and don't propose a shortcut
through natura**. The slowness is the test.

**Tue 25 Aug was a day of repairs and builds and she ran NOTHING on the machines**, so the count is
still twelve through. The eight that are left, and what state each is actually in:

- `musebox` — **rebuilt.** Her second set of Gemini pictures (four images, one object each, on plain
  black) replaced the whole look: the disc now stands on a table against the navy wall, the notes sit
  in eight of the photograph's own engraved rings, and the picture takes the shape of the screen. Her
  verdict on the look is in — *"to my eye, yes. yes it is."* — and the card is reshot. **She has now
  heard it on the tablet**, and two of the four voices were wrong: the guitar sounded like the piano
  (it very nearly was one, measured) and the flute like a horn. Both rebuilt Aug 2026, see the row
  above. The white rabbit she reported on the same pass is a drawn hare now. She has not run the
  piece over the four machines.
- `chimes` — tuned to real notes, each material cut to its own lengths, its own strike sound, a
  rod-length slider, and the tangle fixed. **And re-dressed in her own photographs** — the hanger,
  its chains, the eyelets and all three cords. **She has HEARD it** — Aug 2026, *"it sounds a great
  deal better"* — which is a verdict on the rebuilt sound and **not** a Done mark; she has still not
  run it over the four machines. Test it with the rods at DIFFERENT
  lengths or the tangle it was reported for cannot appear at all. Two things to watch for that are
  known and not repaired: on the 3in phone the dock swamps the piece entirely — **repaired Aug 2026
  off her report**, see the row above. The **wood** rods
  are her photographed walnut now, off her report; brass, silver and glass are still drawn, which
  is deliberate — they are smooth and shading does them well.
- `lamp` — **was a build and now is one.** Oil that burns down, her father's ten penny nail, the tap
  that finds the level, the sputter and the wick burning to ash, an oil can to fill it again, and a
  burn rate that follows the flame rather than the slider. Its ✅ was given for the wick and flame and
  predates every bit of that.
- `pendulum` — her two reports are fixed: the full-diameter line is now a short trail behind the
  weight, and the pins are the right way round (a fallen one was the brightest thing on the plate).
  Its ✅ predates the real-time checkbox as well.
- `birds`, `fireflies`, `moths`, `ant` — **untouched, and the big lift**, as above.

The general point, which cost a wrong guess once and is now demonstrated twice over: **"marked done"
does not mean "current".** A Done mark records what was true when it was given and does not follow
the piece forward — lamp's predates its whole fuel system, pendulum's predates the real-time
checkbox. Both still carry ✅, correctly, because only she takes a mark back.

### Three faults turned out to be systemic, so all sixteen untested pieces were swept for them

Measured on 21 Aug, before testing rather than after, so her device time goes on what a sweep cannot
see. **None of these four are fixed yet** — she asked for them to be ready to fix, and the offer
stands:

**One caution about how this was swept, because it caught me out.** The first pass laid each page out
at the device's FULL height and asked what fell below the visible line — which is exactly what the
trap does, but it cannot tell an unfixed page from a fixed one, since a page that measures
`innerHeight` would never have been that tall. Re-measured at the height a device actually leaves
visible, the four flags came apart:

| piece | at the true visible height | what it really is |
|---|---|---|
| `chladni` | was 36–101px under the bar on all four | **the trap. Fixed 21 Aug** — lays out to `innerHeight` now, and the plate is sized off the same figure or it stays scaled to a screen the visitor hasn't got. Desktop identical, measured. |
| `storm` | fits on all four | **nothing to do** — it got the `innerHeight` fix earlier the same day. The sweep flagged its own blind spot, not a fault. |
| `musebox` | fits, bar 24px on a Kindle sideways | **mild**: it already carries `min-height:100dvh` with a `100vh` fallback, and its page can scroll, so the tempo control is reachable. Left alone. |
| `kaleidoscope` | 63–167px over on three of the four | **not the trap — the design debt its own row describes.** The content genuinely does not fit; a proper small-screen arrangement is still owed and is her call, not a repair. |

`warmler`, `roller`, `gyre`, `chimes`, `birds`, `fireflies`, `moths`, `ant`, `lamp`, `rain`, `bowl`
and `pendulum` are clear on all four.

**White cut halos: none left.** Nine files flagged by a crude test, all innocent on inspection — the
pinecone frames do carry a pale rim but the cone sits on a photograph of straw, so nothing shows; the
chime rod's bright edge is the wood's own curve; the rest were masks, which are meant to be white.
That fault was confined to the shelf plates and windower's centre pane, both fixed.

**Mouse dimensions: one good surprise, one steady drip.** Galileo's press-and-hold float was the
**only** hover-only behaviour on the site — nothing else asks for a gesture a finger cannot perform.
What does recur is small targets: tickboxes and icon buttons at **14–29px** where a thumb wants about
40 (chladni's mic and sound boxes 16, lamp's mute 14, ant's food box 16, storm's live box 16,
musebox's save and clear 22x18, bowl's two pickers 29x21, roller's colour buttons 26). The sliders
measure 25–33px, but those are already grown as far as their neighbours allow by the `touch-targets`
pass, so they are at their limit rather than neglected.

### Blocked storage took four pieces down, two of them signed off

Aug 2026, found by loading every piece with its props taken away rather than by anyone hitting
it — the check roller's Kindle failure should have prompted and didn't. **`localStorage` does not
merely come back empty when a browser refuses it: it THROWS.** A private window does it, and so
does any browser set to block site data — a Fire tablet's Silk is exactly the sort that might.
Read unguarded at the top of a script, that one refusal takes the **whole piece** down: with site
data blocked, **`musebox`, `lamp`, `roller` and `storm` all came up blank**, and `roller` and
`storm` are both pieces she has passed on all four machines. `candler` had wrapped its own read in
a try/catch all along and survived, which is what the right answer looks like.

Every read and write now goes through a `readStore`/`writeStore` pair in each of the four. Verified
both ways: blocked, all four draw with no errors; working, every setting is still written and still
survives a reload (`sagne-muted`, `sagne-volume`, `sagne-musebox-voice`, `sagne-roller-glass`,
`sagne-storm-sethand`). **Losing the setting is nothing; losing the piece is everything** — and the
general point is the one bowl's row already makes about page weight: *these pages had been swept
for layout faults many times and nobody had ever asked what happens when something they lean on
says no.*

**Still open, both small:** `conometer` leaves a 6px sliver of disc proud of the picture on an
ordinary 390px phone (none of her four devices shows it, so it was left); and candler's "flashing
line" — the back disc, before it was pinned, sat in the flow inside the area the flame repaints, so
its edge was being re-rasterised every frame. It went with the fix; the diagnosis is inference, not
proof.

## The standard: does it behave like the real thing?

**Why it has to be true.** Hers, Aug 2026, and it is the reason the rest of this section exists:
***"tell me a kid won't look at a pine cone differently -after- they'd seen it be a slider for
humidity on their phone?"***

A pinecone on a forest floor is scenery. A pinecone someone has watched open and close with the
weather is an instrument, and every pinecone after that one is a hygrometer. And **the real
pinecone cannot teach this** — it takes hours, so nobody has ever learned it by watching. That is
not a substitute for the real thing; it is the real thing made legible, permanently, in the
visitor's own eyes.

About **eleven of the twenty** pieces are in that class: a real behaviour, present and all around,
invisible only because it runs too slowly or too rarely or too quietly to be attended to. A day
per turn of the pendulum, days for the storm glass's crystals, hours for a wick to burn down, a
whole afternoon for the sun to cross a window, a plate and a bow and a room for Chladni figures,
tubes cut and hung before a chime's tuning can be heard at all. The smaller half of the shelf is
sensorial twiddle and is honestly labelled as such — warmler is not trying to teach anyone what
warm brass feels like.

So the fidelity is **load-bearing rather than fussy**. If the pinecone opened at the wrong
humidity, or the plane turned at the solar rate instead of the sidereal one, a visitor would walk
away with a **false instrument installed** — and would carry it into every real pinecone and every
real sky afterwards. Getting it right is the whole permission to change how someone sees. That is
what every measured figure in the rows above is protecting.

This is the actual spec for every piece on this site, not a nice-to-have. The whole premise the
owner is offering a visitor is **touch this, see what happens — and trust that what happens is
what would happen in the real world.** A pin that doesn't land where a dropped pin would land, or
a gear ratio that doesn't actually change anything, isn't a polish issue — it's a broken physical
promise, and it matters more than it looks like it should.

That changes what "verify before claiming done" means here: don't just check that a change
*looks* right in a screenshot. Where a piece claims to model something physical (an object
falling, a ratio driving a speed, a shape changing a flame), check the actual behavior — pull
real numbers out of the running page (position, speed, whatever the claim is), not just an
eyeballed picture. A bug report on this site is really "this lied to me physically," and that's
the bar to hold your own testing to as well, not just the owner's.

### Being right is not enough if it reads as broken

Two different faults, and they are not worth the same. The owner's words: *"it's one thing
with candler's cup, which is 'invisibly' broken, and another with something that will just
look wrong even though it's right."*

The promise this site makes is to the **visitor's eye**. So a piece that is *correct* but
presents a state a visitor will read as a fault costs more than an ugly cut-out nobody can
see — even though the second is worse as code. Galileo had exactly this: three instruments
butted end to end left a 4°F band at each join where none of them had a gap to read, so it
sat there apparently doing nothing while being perfectly truthful. Correct, and no use.
**Fix that kind now.**

The hidden kind can wait — but **write down what is hiding it**, because that is what fails
silently later. Candler's cup and lip are badly-cut selections with squared-off edges, and
they are invisible only because a clipping rectangle is holding them so. The clip is
load-bearing. Move that piece's geometry without knowing it and the fault comes straight
back. "Invisibly broken" there means *conditionally* invisible, which is a parked problem,
not a solved one.

## The other half of the standard: what a piece costs to put down

The section above is the *instrument* half of the argument — the pinecone, the ones that
make a real behaviour legible. This is the half that explains the quiet ones, and without
it a session reads the shelf and concludes that `rain` and `warmler` are the slight pieces.
They are not. Her words, Aug 2026:

> *"rain does almost nothing. except the experience of watching drops gather and fall on
> glass does something to the human physical state. we're meant to get idly absorbed in
> such things, it's when creative thoughts happen and the internal dialogue stops."*

And the criterion that follows from it, which is the sharpest test on this site after
*does it behave like the real thing?* —

> *"a kid can play with that for half an hour and be reasonably amused without being
> overstimulated, emotionally manipulated, or distressed when told it's time to put it away."*

**Call it the exit cost, and check every piece against it.** Nearly everything else on a
tablet is built so that stopping is expensive: a streak to break, a level half-finished, an
autoplay three seconds into the next thing, a reward that lands just after the point where
someone would have stopped. The distress when a child is told to put it down is not a side
effect of those designs, it is the product working. **No piece on this site may have that
property.** `rain` has no state to lose — no score, no progress, nothing unfinished, nothing
taken away when the tablet goes down. That is a real, checkable property of a design and it
is rarer than the fidelity is. Anything proposed here that makes leaving cost something —
a streak, a saved run to finish, a thing that escalates, a payoff withheld until later — is
refused on this ground alone, whatever else recommends it.

**These are instruments she uses, not exhibits — and that is the reason for the whole
fidelity standard.** Aug 2026, unprompted: she uses the **candle timer all the time**, in
place of an ordinary alarm; she **checks the weather with `windower` and `galileo`**; she
sits and watches `bowl`, or leaves it idling while doing something else. So the insistence
everywhere in this file that a piece must be truthful is not a philosophical position. **She
is the first person a lying piece would mislead** — about the weather outside her own window.
Treat every piece as something in daily use by the person who commissioned it, and be
correspondingly careful; a session that reads this file as a description of artworks will be
less careful than it should be.

**And the candle-versus-alarm reasoning is worth having written down, because it is the exit
cost applied to time.** Her observation: the candle timer *"is so much less intrusive than a
normal alarm, and does not build the same tension."* That is a real mechanism, not a
preference. A countdown builds tension precisely because it is a **discrete number
approaching a threshold** — checkable, and therefore compulsively checked. A candle burning
down is **continuous and read at a glance**, with no moment visibly arriving. Same function,
opposite effect on the body of the person using it. Anything proposed for `candler` that
makes the remaining time more numeric, more prominent, or more alarming is working against
the reason she uses it. (Note this is exactly why the readout fix of Aug 2026 was worth
doing and stayed small: making the count *honest* is not the same as making it *louder*.)

**The plainest statement of the whole position is hers, about a six-year-old:** *"i'd rather
see a six year old picking things to float than getting wound up by angry birds."* **"Wound
up"** is the operative phrase. This is not an argument about screen time and it is not
nostalgia — it is about what state a child is in twenty minutes later, and the difference
between a thing that entertains and a thing that must agitate in order to keep entertaining.
One leaves a child choosing between a copper bowl and a stone one. The other leaves them
needing another go.

**Patience is not a filter, it is the thing being taught.** *"The way patience is learned is
by being given things that reward it."* So the objection that these pieces only reward
visitors who arrive patient has the cost the right way round: that is what teaching it looks
like from the inside, and the slowness is the lesson rather than the entry fee.

**Under that aim the twiddle pieces are the ENTRY, not the weak half.** Her hope for the
site is *"a toddler's tablet, instead of something loud and flashy."* A two-year-old will
not get `conometer`. They will get `warmler`, `rain`, `bowl`, `roller` and `kaleidoscope` —
the pieces that teach that touching a thing makes it answer, which is the whole prerequisite
for the instruments later. A session that ranks the shelf by cleverness has it backwards.
And there is a mechanism worth knowing in this: small children are not patient but they are
ferociously repetitive, returning to one thing dozens of times. Most apps answer that with
novelty, which is where the flashiness comes from. These answer it by being genuinely
different each visit — a different sky, different weather, a different amount of oil in the
lamp. Same object, new state. That rewards returning without escalating.

**The bar every piece has to clear, in her words:** *"anyone from a 4 year old to a 65 year
old Chinese engineer can immediately engage."* That is the universality test, and it is why
so many decisions in this file went the way they did — emoji or drawn glyphs instead of text
on the controls, no lettering on the shelf that is not engraved into brass, the fetch-trouble
marks being marks rather than a sentence, the icons drawn in `currentColor` rather than
borrowed from a font. **No piece may depend on reading, on a language, on a cultural
reference, or on knowing anything first.** If a control needs a word to be understood, it is
the wrong control.

**And note what "immediately" does and does not mean here, because it looks like it
contradicts the patience the rest of this section is about.** It does not. **Engagement is
immediate; comprehension is not.** Touch anything and it must answer at once — the ring
brightens, the card lifts, the sand moves, the tray tips. What takes patience is working out
what the answer *means*: that the sky is the real sky outside, that the cone is reading the
humidity, that the lamp will actually run out.

**But comprehension has to be REACHABLE, and that is a requirement rather than a hope.** Her
own qualifier, Aug 2026: *"comprehension doesn't have to be immediate, but it should be
accessible through a bit of twiddling. google can explain anything these days, and they're
all identifiable for the concepts or objects they are."* So there are exactly two routes in,
and every piece must offer at least one:

1. **Twiddling.** Working the controls has to be able to disclose the point on its own. This
   is why the lamp got an oil can — it makes the tap *comparable*, which is much the fastest
   way anybody works out what tapping is for — and why `conometer` and `storm` carry a
   live/manual toggle at all.
2. **Recognition, then a search.** The piece must look enough like the real object or the
   real phenomenon that a curious person can name it and go and find out. **That makes
   recognisability a design requirement, not an aesthetic accident** — the pinecone has to
   read as a pinecone, the storm glass as a storm glass, the Chladni plate as sand on metal.
   This is the same reasoning already recorded under *Exploring is the point*: the URLs are a
   hint, the location flag is itself the disclosure, and the site trusts curiosity and
   ever-present search engines to do the rest.

**So the failing case is a piece that is neither.** Not one that takes twenty minutes to
arrive — that is the design working. One where twiddling discloses nothing AND the thing on
screen cannot be named. That is the only version of "undiscoverable" this file treats as a
fault, and it is a real one, distinct from the nudging that is forbidden. **Fixing it is
never done with words.** It is done by making the object more like itself, or by giving the
controls something to compare.

**The distinction that keeps this from eating good work: refusing to explain is not the same
as refusing to be usable.** Bowl not loading at all on the Jelly Star was a broken door, not
a patience test. Chimes' dock swamping the piece asked nothing of anybody. A pin too small
to grab with a thumb taught nobody anything. The whole four-device programme is that second
category, and it is why the principle has not turned into an excuse. **Keep the line bright**
— the day it blurs is the day *"it is meant to be demanding"* starts covering for something
that is simply broken. Her own sharpest handling of it is `pendulum`: at the true Foucault
rate the turn is imperceptible, and the sped-up version exists anyway, as a choice, with the
honest one on a checkbox beside it. That was the principle held with judgement, not as a rule.

**On the "calm" sites, and why this is not one of them.** Her reading, and it is correct:
*"the 'calm' sites are all more about... selling a mood, not returning touch and sense
through a digital medium."* Rain-noise and lo-fi sites simulate a **feeling** — the calm is
the product. These pieces simulate a **behaviour**, truthfully, and the calm is a by-product
of the thing being real and taking its own time. A pinecone that opened at the wrong humidity
would still be soothing; it would just be a lie.

### A caution about asking an AI to rate this site

Aug 2026 she asked both Claude and Google's AI to rate sagne. Both scored it highly, both
said very little compares with it, both said the way to improve it further was to market it,
and both reached for **neal.fun** as the comparison. Treat all of that with suspicion, and
know why:

- **A session that has read this file is not an independent judge.** It has absorbed her
  reasoning and will hand it back as agreement.
- **The neal.fun comparison is by SHAPE, not intent** — one author, single pages, browser
  toys, no framework. But those pieces are built to produce a reaction and these are built
  to produce a noticing. Comparing by form flatters the site with the wrong compliment. The
  honest comparison set is mostly not on the web at all: the Exploratorium floor, Montessori
  sensorial materials, the demonstration apparatus in an old physics classroom.
- **"Market it" is what an AI says when it cannot find a fault.** And it carries a trap this
  file has already ruled on: any description good enough to make somebody click ("watch a
  pinecone respond to the humidity where you are") has already given away the discovery. That
  is the refused reference sheet wearing a different hat. Telling people the site *exists* is
  not the same as telling them what it does, and only the first is safe.
- **"Radical" and "rebellious" are the raters' words, not hers.** Worth deflating: none of
  this is radical as an idea. A spinning top has no exit cost either. What is unusual is only
  doing it *on a screen*, which is the one place the incentives run hard the other way. The
  site is not proposing something strange; it is declining to do the strange thing everyone
  else is doing.

What an AI session *can* judge here is the measurable half — whether the physics is right,
whether a fetch is wasteful, whether a target is too small for a thumb. Whether a piece is
beautiful is hers alone, which is why the Done marks are hers and why she was right about
the guitar when every number said it was fine.

## Exploring is the point — don't ever "help"

Her words, and they settle it: *"I want people to have to explore. I don't want things
explained. The point is to reward curiosity, not be led by the nose."* This is a design
decision, not an oversight, and it is the same one the **?** saying makes on the site
itself — *the author trusts curiosity and ever-present search engines to suffice where
clarity is needed.*

So: **never propose a hint, a tooltip, a first-run tip, an arrow pointing at the thing, a
"tap to begin", or any nudge whose job is to tell a visitor what to do.** That a gesture is
undiscoverable is not a bug to be reported here. A session that "notices" the shelf doesn't
announce that it zooms has noticed the point of it.

The line that *is* allowed: an object behaving like an object. A card that lifts as the
pointer crosses it, a thing that answers when touched — that's the piece being alive, and
the shelf already does it. That is not an explanation. The test is whether it *tells* or
merely *responds*.

**A reference sheet, teacher's notes or an aims list has been proposed and REFUSED — Aug
2026 — and the reasoning is written here so it is not proposed again.** It came up because
the site is meant, when it is finished, for Montessori and similar teaching, language-free
and international. From that a session (this one) reasoned that a guide choosing materials
cannot tell by looking which four pieces read the visitor's real weather, and offered a
one-page sheet listing them. **Being off-page is not a loophole**: a sheet gets forwarded,
quoted and pasted into a resource list, and then the first thing anybody ever reads about
sagne is the answer to its own question. It is a tooltip at a different URL.

Her answer, and it settles it: ***"it also -refreshes-, so the changes become obvious. the
whole point of this site is patience and curiosity being rewarded. why would i sell it out
there."*** Someone who stays with `windower` for twenty minutes watches the sky change. The
liveness discloses itself — it just costs the one thing the site is asking for. And of all
possible audiences, a Montessori guide is the one trained to sit with a material before
presenting it, so the site is aimed at precisely the people who will do the patient thing.

Two things she pointed out on the way, both correct, both worth keeping because they are
what makes the refusal safe rather than merely principled. **The URLs are a hint**: the two
pieces hardest to name by sight carry their own names in the address (`/chladni/`,
`/galileo/`), `/conometer/` is a portmanteau that gives the game away, and her coinages
carry a grammar — the *-er* in `windower`, `warmler`, `roller`, `candler` says "a thing that
does this" and the stem says what. **And the flag is already the disclosure**: it is on all
seven location-aware pieces, and pressing it opens a box asking where you are, which says
plainly that the piece cares. The fetch-trouble marks count for less, since they only show
when something has broken.

**And the rule does not stop at the edge of the site.** Aug 2026, asked whether she would
make the case for sagne being good for children: *"i don't plan on making any claims. you've
seen the wording and lack of on the site. i have no intention of departing from that on any
level. if anyone wants to put my stuff in that category, that's their call."* So **do not
draft her a tagline, a pitch, an about page, a description of what a piece teaches, or a
claim about its effect on anybody** — not for parents, not for teachers, not for an awards
entry, and not on the grounds that it would help the site reach people. A session asked to
help sagne find an audience will reach for exactly that and must not. Saying the site
*exists* is the only safe form; saying what it does is the refused sheet again. Where it gets
categorised, and by whom, is other people's business and she has accepted that it is slow and
out of her hands.

## Guardrails

- Keep each change **small and self-contained** — one idea at a time.
- **Preview → Do.** Never make a visual change live that the owner hasn't seen.
- **Do** and **Undo** both change the **real, live site** — treat them as the deliberate,
  owner-approved moments they are.
- **When to hand off to a human:** the trigger is **any sign of frustration** from the owner —
  not a count of attempts. Pure learning/curiosity ("what happened there?", "how does that
  work?") is fine to keep exploring together. But the moment frustration shows, even mildly,
  stop troubleshooting and say plainly: *"This one needs a hand — could you press **The Help
  Button** in your bookmarks bar?"* Don't offer another explanation or workaround first. To the
  owner, **Netlify + Claude Code + git are just "the box of stuff" behind the site** — never
  expect her to sort out which piece is misbehaving; that's not her job.
