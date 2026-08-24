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

**Landing page:** `index.html` (titled *sagne*) — a **five-shelf case**, the pieces standing
face-front on the shelves in mounts, and the name of each type on the brass plate beneath it.
It replaced the flat card grid in Aug 2026. Every position on it derives from one table of
measurements taken off the photograph itself — the interior opening, each shelf's surface and
the rail its plate is screwed to. Change the picture and you change that table; don't retype
percentages by hand.

The case is **`shelves-navy.jpg`** (1024x1260), her dark cabinet, straight on. It replaced the
walnut apothecary shelf in Aug 2026 — her call: *"while the shelves we built are undoubtedly
beautiful, they're not as timeless or as understated."* `shelves.jpg`, the walnut one, is kept
as a record and is no longer referenced by anything.

**The brass is laid on, not photographed in.** The walnut case had its lettering engraved into
the picture; this one carries her own plates as separate cut-outs — `shelfplate-<group>.png`,
`shelfoval.png` — with the names set over them in **Libre Baskerville 700**, her pick over
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

**13 of the 20 are done.**

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
| `roller/index.html` | ✅ | ✅ | *Roller* — a wooden tray you tilt to roll a small object around (sea-glass pebble, disc, or jellybean stone); tilt-controlled like `galileo`/`windower`'s location search but via device orientation or mouse<br>**Done**, pending her own testing of the bean's weave and the spin off a wall. Deliberately unscored: "there's other things like it, but none really do what it does."<br>Three
things Aug 2026, all hers, all after she had it in front of her.<br>**The speed slider was not a speed
slider.** It multiplied how hard tilt pushed and nothing else — not friction, not the wall bounce — so
once anything was moving it careered about at much the same rate wherever the slider sat. Measured
under a held full tilt: the pebble averaged **130px/s at the bottom of the range against 146 in the
middle**, eleven per cent, nothing anyone could feel, while its PEAKS moved two and a half times. She
asked for a speed slider so things could slide slower and it was reasonable to think there wasn't
one. What actually makes a thing slide slowly is the surface, so below the middle the tray now gets
draggier as well as gentler — the same friction raised to a higher power, which is what a shorter
settling distance is. Re-measured: pebble **73px/s** at 20, disc **48**, bean **63**, and the peaks
down by more. **At 100 the exponent is exactly 1 and nothing changes at all** — from the middle of
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
| `lamp/index.html` | ✅ | ✅ | An oil lamp — trim the wick's shape and height, and the flame follows. A fuel level you find by *tapping* the base is designed but not built; the note in the file records which way the pitch must go<br>**Done** as it stands — the tap-for-fuel idea is recorded as a future build, not a gap in it. |
| `warmler/index.html` | ✅ | ✅ | A warming plate with selectable metal **finishes** (brass, copper, aged brass/copper, gold, silver, diamond-plate). `warmler-picker-concept.html` is a finish-picker concept (not linked)<br>**Done** — through her four-device test Aug 2026 with nothing to repair: *"i honestly can't
find any fault with warmler. it's a simple twiddle toy, and now that we have the edge issues
worked out, it's fine on all four machines."* The edge issues were the two already fixed in the
site-wide sweeps — the music button sitting on the finish trigger at 390px, and the `<button>`
face showing behind `#finishTrigger`'s cut-out — so this is the first piece to pass on the
strength of work done before she ever opened it, rather than on repairs found by opening it. |
| `rain/index.html` | ✅ |  | Rain on glass |
| `ant/index.html` | ✅ |  | Ants |
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
| `birds/index.html` | ✅ |  | **Birds** perched on wires strung between two poles against a sunset-sky photo; the wires sag realistically and dip under whichever bird is sitting on them |
| `bowl/index.html` | ✅ | ✅ | A still bowl of water for floating things on; has a breeze and an object picker<br>**Done**.<br>Aug 2026, found by measuring for a 3-inch phone: the dock is one row that never wrapped and wants **369px** laid out end to end, so on anything narrower the LAST thing in it — the flower, which is the whole object chooser — was pushed clean off the right edge, and with the page unable to scroll there was no way to reach it. It cleared a 390px phone by 22px, which is exactly why it looked perfect everywhere anyone had looked. Behind that sat a second fault: the chooser popup is a fixed 326px grid and hung 43px off **both** edges of a 240px screen, so fixing the button alone would only have revealed half the flowers. Below 379px the dock now wraps to two lines and the popup drops to three slightly smaller tiles; above it, nothing applies and the dock is pixel-identical at 390, 600 and 1200. The wrapped row is **right-aligned, not centred** — the music button is pinned in the bottom-left corner and a centred second row lands straight on top of it.<br>**It did not load on the Jelly Star** — her report, Aug 2026, and it was true in the
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
looks at where things land cannot see 6MB queued in front of the piece. |
| `chimes/index.html` | ✅ |  | **Wind chimes** you build yourself — pick the rod material and the cord/chain, then hang them. Uses warmler's swatch-picker pattern<br>Sound was rebuilt Aug 2026 (struck on impact, real bar overtones, pitch by material) — **awaiting her ears**, which is the only test that counts here.<br>Two things went in Aug 2026 after she watched it. The **hanger sways** — the whole set hangs off one ring, so it is a slow heavy pendulum of its own, its weight mostly the rods well below the bar, and the rods then hang from a *moving* support and are swung by it. What drives the sway is drag, and **drag goes as the square of the wind**, which is her own observation in one line: at a light air the lean is a tenth of a pixel and the bar looks nailed up; at full wind it is 3° (about 8px at the bar, twice that at the rod tips). There is no threshold in the code — the v-squared law is the whole of it, so don't add one.<br>Underneath that, a real fault: **the swing is solved in the convention `x = tie point + sin(angle)·length`, and canvas rotates the other way.** Every rod had been drawn with `rotate(+angle)`, so the contact test was watching the mirror image of the scene on the glass — measured at full wind, the two frames disagreed about who was touching on **43% of pair-frames**, rods passed clean through each other in silence, and it chimed with a plain gap showing. Now 0%. If you ever change how a rod is drawn or hit-tested, the minus sign in `ctx.rotate(-r.angle)` is load-bearing and so are the matching signs in `rodMidWorld` and `hitTestRod`.<br>**And it tangled, and stayed tangled** — her report, with a photograph of two long
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
sounded and didn't, because the rods were passing through each other in silence. |
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
| `fireflies/index.html` | ✅ |  | A field at dusk where you place fireflies in the grass; real dusk-to-night sky, with bats about |
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
on touch.<br>**The card was still the old look** — flat gold stripes and a sparse pattern, from
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
| `musebox/index.html` | ✅ |  | A **music box** — set pins on the disc to write a tune<br>**She is unconvinced it is finished** — not the behaviour but the look: *"you did a lovely job
building it, but i'm not sure it's -beautiful-"*, and she may bring pictures from Gemini to rebuild
it from. That is open, and nothing here settles it.<br>Aug 2026 it got **four voices** at her ask, the
chime she already liked plus **piano, guitar and a Native American flute**, each built from how the
real instrument makes its sound rather than from a preset. A struck string is stiff, so the piano's
partials are stretched by n·√(1+Bn²) — that stretch is most of what makes a piano sound like a piano
and not an organ — with the hammer landing underneath as its own pitchless knock. A plucked string's
harmonics are set by WHERE it is plucked, sin(nπp)/n², so the guitar has real holes in its spectrum
at the pluck's own nodes (p=0.22, an ordinary picking position). A fipple flute gives a strong
fundamental, a soft second and almost nothing above, and the half that matters is **breath running
the whole length of the note** rather than only its start — that is what makes a flute sound blown
instead of struck — with a slow attack, a chiff at the front, and vibrato arriving only after the
note has settled, the way a player's does.<br>The icons are **drawn, not emoji**, deliberately: the
only flute emoji arrived in 2022 and a Kindle Fire would show an empty box where it should be.<br>**The
rabbit is grey.** Her call — white was the brightest thing on the page, brighter than the disc or the
brass, so the eye went to the tempo control before the music box.<br>**And it was clipping.** Eight
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
it the angle still equals the pure clock function, so nothing accumulates or drifts. |
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

### The shelf, and how it got there

The pieces are split into five groups: **instrumenta, tactilia, systema, natura,
phenomena**. Those are her words, off her own handwritten notes — *instrumenta*, not
"tools". Which piece belongs in which group is hers, and so is the list; don't reshuffle it.

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

**Interaction.** On a touch screen it is three taps — shelf, then card, then open — because
a phone cannot show a card big enough to read; her idea, and the right one. With a fine
pointer a card opens on the first click instead, and the shelf zoom stays reachable from the
name plates. If you change the picture, the zoom transforms recompute themselves from the
measurement table; nothing there is hand-typed.

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

- **Card previews** on the landing page: `<demo>-card.png` (e.g. `lamp-card.png`).
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
bowl, roller, kaleidoscope, gyre** — her call on all eleven; every fault they turned up is fixed and live, and
the details are in each one's row above. The case itself was worked on the same day: light on the wall behind it, the
white cut line off all five plates, darker arrows in the two discs.

**Eleven through, nine to go**, by shelf: **instrumenta 5/5**, **tactilia 3/3**, systema 1/3
(`gyre`, straight after its two changes — *"gyre works on everything too"*), phenomena 2/5 (`bowl`
and `chladni`), natura 0/4. The nine left are `musebox`, `chimes`, `lamp`, `rain`, `pendulum`,
`birds`, `fireflies`, `moths`, `ant`. `chladni` and `bowl` cost one repair each on the afternoon of
the 24th — the microphone tickbox onto the sound line, and bowl not loading at all on the 3in phone.
Bowl's is the one to remember: it was **two** faults, and the larger belonged to every page on the
site rather than to bowl.

**Her order from here**: **instrumenta and tactilia are both finished** as of Mon 24 Aug — `storm`
closed the first, and `warmler`, `roller` and `kaleidoscope` the second. `bowl` and `chladni` are
through off **phenomena**, which leaves `lamp`, `rain` and `pendulum` there. In **systema**, `gyre` is through and
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

**What she expects from the nine still to run** (Mon 24 Aug, her own read — recorded because a
session that only counts ✅s will guess this wrong, as one did):
- `musebox`, `chimes` — **unguessable until she hears them.** Both were rebuilt by ear this month and
  sound is the one thing no measurement here settles.
- `lamp` — **may not be a test at all but a build.** The tap-the-base-for-fuel idea in its row is
  still unbuilt, and she may want it made before she calls the piece run.
- `pendulum` — **she doubts it, and the doubt is well founded.** Its ✅ was given for precession,
  swing and pin ring verified by measurement, and the **real-world-time checkbox came after that**, so
  the mark predates the feature. She expects hiccups. A Done mark records what was true when it was
  given; it does not follow the piece forward.
- `rain` — *"as done as i can make it without an animating software"*, so likely quick, and any
  remaining wish there is a tooling problem rather than a fault.
- `birds`, `fireflies`, `moths`, `ant` — **the big lift**, as above.

The general point, which cost a wrong guess: **"marked done and untouched today" does not mean
"quick".** Two of the four pieces that fitted that description are the ones she expects most work
from.

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

**Still open, both small:** `conometer` leaves a 6px sliver of disc proud of the picture on an
ordinary 390px phone (none of her four devices shows it, so it was left); and candler's "flashing
line" — the back disc, before it was pinned, sat in the flow inside the area the flame repaints, so
its edge was being re-rasterised every frame. It went with the fix; the diagnosis is inference, not
proof.

## The standard: does it behave like the real thing?

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
