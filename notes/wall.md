# The wall (landing page): how it got there, and everything learned building it

Moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short. Written as it happened; read it
when working on this part of the site.

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
