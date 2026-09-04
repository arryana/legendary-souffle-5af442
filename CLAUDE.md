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

**17 of the 20 are done.**

**Where the history lives.** This file is read at the start of every session, so it carries only
what every session must know: the rules, the things not to re-propose, and the state of each
piece in a line. **The full story of each piece is in `notes/<slug>.md`** — every measurement, every
wrong turn, every verdict of hers in her own words — and `notes/wall.md`, `notes/touch-targets.md`
and `notes/sweeps.md` carry the same for the landing page and the site-wide work. **Read a piece's
notes file before touching that piece.** When you write up new work, the story goes in the notes
file (newest at the bottom) and only the state line in the table below changes. Don't let this file
grow back. Her call, 3 Sep 2026: *"we can always cache it and use it for reference when necessary."*

| File | On landing page? | Done? | What it is, and where it stands |
|------|:---:|:---:|------------|
| `index.html` | — | — | Landing page: five shelves on a dark wall ("sagne"), all 20 pieces. `notes/wall.md` |
| `candler/index.html` | ✅ | ✅ | *Sagne Candle* — an interactive candle (`candler_5.html` is an unlinked alternate). **Done** and **tested on every machine**; the first piece through that test and the standard for the rest. She uses it daily in place of an alarm. `notes/candler.md` |
| `roller/index.html` | ✅ | ✅ | *Roller* — a wooden tray you tilt to roll a pebble, disc or jellybean stone. **Done**, **tested on every machine**. `notes/roller.md` |
| `lamp/index.html` | ✅ | ✅ | An oil lamp: trim the wick and the flame follows. The fuel that burns down, her father's ten penny nail for tapping the level, the sputter, and the oil can are Aug 2026 builds; the ✅ was given for wick and flame and predates all of it. Sep 2026: the nail is **held by the point and tapped with the head**, her family's way round, and the card is recentred on the lamp. Not run on the machines since. `notes/lamp.md` |
| `warmler/index.html` | ✅ | ✅ | A warming plate with selectable metal finishes (`warmler-picker-concept.html` is an unlinked concept). **Done**, **tested on every machine** with nothing to repair. `notes/warmler.md` |
| `rain/index.html` | ✅ | ✅ | Rain on glass. **Done** — *"as done as i can make it without an animating software"*: don't propose rebuilding it. **Tested on every machine**. `notes/rain.md` |
| `ant/index.html` | ✅ |  | Ants foraging on a tray, with a lollipop, pebble, leaf and twig. Sep 2026: a carrier holds a crumb rather than turning purple, each ant has its own pace and stops to antennate, and ants are bodies that give way; 4 Sep, off her report of a jerky halt, they run down into most stops and gather speed out of all of them. Her verdict on the first *"significantly improved"*; not run on the machines. `notes/ant.md` |
| `windower/index.html` | ✅ | ✅ | A window onto the real sky at the visitor's time and place, with real weather on request. **Done**, **tested on every machine**. Her ruling that a phone shows the same slice of sky stands; don't re-propose. `notes/windower.md` |
| `galileo/index.html` | ✅ | ✅ | A Galileo thermometer on the real local temperature, three instruments reading 12–116°F. **Done**, **tested on every machine**. `notes/galileo.md` |
| `conometer/index.html` | ✅ | ✅ | A pinecone hygrometer on the real local humidity, live/manual toggle. **Done**, **tested on every machine**. `notes/conometer.md` |
| `gyre/index.html` | ✅ | ✅ | Meshable gears on a board driving a signal lamp (`gears.md` has the maths). **Done**, **tested on every machine**. `notes/gyre.md` |
| `birds/index.html` | ✅ |  | Birds on sagging wires against a sunset sky. Swept Aug 2026, otherwise untouched; waiting on her machines. `notes/birds.md` |
| `bowl/index.html` | ✅ | ✅ | A bowl of water for floating things on; ten bowls, a breeze, an object picker. **Done**, **tested on every machine**. A tap lifts a stone out, a drag moves it. `notes/bowl.md` |
| `chimes/index.html` | ✅ | ✅ | Wind chimes you build: rod material, cord, count, length. Tuned to real notes, each material cut to its own lengths, her own photographed hanger and cords. **Done** 4 Sep 2026, *"barring adding my own sounds at some point"* — her own recordings are a change she may still want, not an open fault. Not run on the machines; test with the rods at DIFFERENT lengths. `notes/chimes.md` |
| `chladni/index.html` | ✅ | ✅ | A Chladni plate: sand, salt, lycopodium or flour on metal. **Done**, **tested on every machine**. A cornflour suspension is parked, her call; don't re-propose it on this renderer. `notes/chladni.md` |
| `fireflies/index.html` | ✅ | ✅ | A field at dusk where you place fireflies; real dusk-to-night sky, bats. Rebuilt entirely on her reports (she is remembering real ones; there are none in Scotland). **Done** 4 Sep 2026, after *"perfect. it's perfect."* on the look and behaviour and *"significantly improved"* on the Sep flash and grass work. Not run on the machines. **Read its notes before changing anything.** `notes/fireflies.md` |
| `kaleidoscope/index.html` | ✅ | ✅ | Real photographed objects on a tray, mirrored live; turn the ring. **Done**, **tested on every machine**. Scrolling is the small-screen answer she took. `notes/kaleidoscope.md` |
| `moths/index.html` | ✅ |  | Moths losing their bearings on a hanging bulb; shade is glare in front and distance behind. Built Aug 2026 from her brief, shading rules hers Sep 2026, verdict *"significantly improved"*; not run on the machines. The slowest piece on a Kindle-speed processor (about 14fps at 6x slower). `notes/moths.md` |
| `musebox/index.html` | ✅ | ✅ | A music box: set pins on the disc. Rebuilt on her Gemini pictures (*"to my eye, yes. yes it is."*); four voices, the guitar a real plucked string now in the piano's slot at her ask. **Done** 4 Sep 2026, *"barring adding my own sounds at some point"* — her own recordings are a change she may still want, not an open fault. Not run on the machines. `notes/musebox.md` |
| `pendulum/index.html` | ✅ | ✅ | A Foucault pendulum with a real-world-time checkbox (sidereal rate) and a locator globe. **Done**; the checkbox and the pin fix postdate the mark. Sep 2026 she ruled the real-time trace *"just looks like wedges"*, so the swept ground is scoured radially with a heaped lip at the turning points — her pick of three strengths, geometry untouched. It costs 16–67ms more at the two moments that rebuild the whole trace on a Kindle-speed processor (worst frame seen 167ms) — one hitch where you ask for it, never a freeze; an earlier "no slower" here was wrong and is corrected in the notes. Sep 2026 the ∞ became **her rake** and the speed slider got a fast-forward beside it, both her calls; **which way round a rake should read is still hers**. Her catch the same day: in real time the swept ground was laid ONCE, when the clock was ticked, and never grew — bare floor with bright threads on it, worst after a minimise. It follows the swing now; the fault predated the scouring. `notes/pendulum.md` |
| `storm/index.html` | ✅ | ✅ | A storm glass on the real changing weather, with a barometer. **Done**, **tested on every machine**; the piece that finished instrumenta. `notes/storm.md` |
| `crystal.html` | — | — | A crystal (not linked from the landing page) |
| `chest.html`, `chest-open.html` | — | — | Dead apothecary-chest drafts she turned down; kept as a record, not linked |

### The wall: the rules (the story is in `notes/wall.md`)

- **The five groups and the order down the wall are hers** — tactilia, systema, natura, phenomena,
  instrumenta, and the order within each shelf too. Don't reshuffle. Her words, *instrumenta*, not
  "tools". A chest of drawers was tried three ways and refused: don't re-propose one.
- **`shelves.jpg` is the source of truth** for the photograph; the scripts that made it are gone.
  `tools/wall.py` builds the three walls and the plate from her originals. Every position derives
  from one measurement table (`GEO`, `SKINS`); if the picture changes, measure again, don't retype.
- **A card stands in a drawn SVG mount**, and the upright must stay BEHIND the card or every card
  gets a black bar down it. Seats and plate nudges are per shelf and set by her eye; don't
  "correct" them to the arithmetic centre.
- **No words on the wall that aren't cut into brass.** No captions, no labels, no hover names, no
  text back button. The two sayings (*sagne* on the crown, **?** on the plinth) are the one
  exception, because she asked for them.
- **The shelf-disc block on every page is generated**: `python3 tools/shelf-tags.py` after changing
  the shelves table. Don't hand-edit between the `shelf-tags` markers.
- **The twenty cards behind the plates are held back** (`data-src`, swapped in when a plate opens);
  `loading="lazy"` alone was tried and is not enough. **The wall's own cards are the small
  `<slug>-card-sm.jpg` versions** from `python3 tools/card-thumbs.py`, which also rewrites the
  generated `card-art` block (true sizes, keyed by the picture's FILENAME). Run it after any card is
  reshot. Full art is fetched on the first zoom, one at a time.
- **Fonts are self-hosted** (`fonts/`, `python3 tools/self-host-fonts.py`). To add a face, put it in
  as an `@import` and re-run the tool. The site has no third-party dependency but the weather API.
- **Interaction**: touch is three taps (shelf, card, open); a fine pointer opens a card on one click.
  On a zoom the frame stays at the window width and only the scale follows; the other shelves go
  back under a dimming sheet cut out at the shelf in focus. On a 3in phone the un-zoomed plates are
  6px and **that is fine** — she tested it and the way in is the card. Don't "fix" it.
- **A `<button>` carries the browser's own grey face**: any brass cut-out made into a button needs
  its `background-color` cleared.
- **Live-data pieces** (`galileo`, `conometer`, `windower`, `storm`) read geolocation and call
  `api.open-meteo.com`. Keep both working. **They fail out loud and wordlessly**: two generated marks
  (`python3 tools/fetch-trouble.py`, don't hand-edit) from the second consecutive failure. **Don't
  add a second weather provider** — a key in a static page is a worse failure than an outage.
- **The location flag answers Enter itself** on all seven pieces that carry one, and `conometer`,
  `galileo` and `storm` lay out to `innerHeight`, held steady while a text field has focus.

### Touch targets: her standing instruction (the story is in `notes/touch-targets.md`)

*"in future please make sure all small buttons and sliders are suitably (and invisibly) fixed."*
**Any piece you touch, and any control you add, comes with a thumb-sized target already on it, and
the painted thing does not move or change by a pixel.** Two generators enforce that by measurement:

- **Sliders**: `node tools/touch-targets.js` (needs `playwright-core` and the site served locally).
  Applies only under `(pointer: coarse)`. Each slider grows only to half the gap to its neighbour.
  The tool removes its own block before measuring, so a re-run gives the same answer as one run;
  **re-running it moves the painted line 1–2px on the twelve pieces she passed** (their blocks were
  made the old way), which is expected and her call to take.
- **Buttons and tickboxes**: `node tools/touch-buttons.js`. Two forms, PAD and OVERLAY; each rule is
  screenshotted against the piece and thrown away if anything changed. **`moths` has no
  touch-button block on purpose** (its whole scene moves and no mask is stable); don't widen the
  mask until it passes. Chimes' rod-material trigger is dropped (its neighbour is too close).
- Don't hand-edit between the `touch-targets` or `touch-buttons` markers.
- **The music button and the docks fight over the bottom-left corner.** The furniture gives way,
  not the piece: a media rule lifts `#music` above a dock by that dock's measured height. **If you
  change a dock's height, change the matching `#music{bottom:}` with it** (ant's is 146, birds' 84).
- candler's pins carry a transparent 44px rect built inside `pinMarkup` (it is rewritten on every
  drag frame). The music player's track name shows while something is playing, not on hover.

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
a **Kindle Fire** and a **Unihertz Jelly Star** (a 3in phone, about 240px across). Her words:
*"I intend to finish every one of them to the same standard."*

**Call it "tested on every machine", which is her own phrase for it (4 Sep 2026), and keep it
separate from the Done column — they are two different things and conflating them confuses her.**
**Done** is her judgement that the piece itself is finished. **Tested on every machine** is whether
it has been run on all four. A piece can be one without the other, and five currently are: `lamp`,
`pendulum`, `musebox`, `chimes` and `fireflies` are all done and none has been tested on every
machine. When she comes to those five she is not judging whether they are any good — she has already
ruled — she is only checking they do not break on a small screen or a slow one. Say it her way in
chat: *"twelve tested on every machine, eight to go"*, not "through the four machines".

**Tested on every machine as of Mon 24 Aug 2026: candler, conometer, galileo, windower, storm,
warmler, chladni, bowl, roller, kaleidoscope, gyre, rain** — her call on all twelve; every fault they turned up is fixed and live, and
the details are in each one's `notes/` file. The case itself was worked on the same day: light on the wall behind it, the
white cut line off all five plates, darker arrows in the two discs.

**Twelve tested on every machine, eight to go**, by shelf: **instrumenta 5/5**, **tactilia 3/3**, phenomena 3/5
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
  piece on every machine.
- `chimes` — tuned to real notes, each material cut to its own lengths, its own strike sound, a
  rod-length slider, and the tangle fixed. **And re-dressed in her own photographs** — the hanger,
  its chains, the eyelets and all three cords. **She has HEARD it** — Aug 2026, *"it sounds a great
  deal better"* — which is a verdict on the rebuilt sound and **not** a Done mark; she has still not
  tested it on every machine. Test it with the rods at DIFFERENT
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


### What the sweeps found (the story is in `notes/sweeps.md`)

- **Measure a page at the height a device actually leaves visible, not its full height** —
  `height:100vh` with `overflow:hidden` counts the browser's own bar as though it weren't there.
  Kaleidoscope's small-screen answer is to scroll, her ruling, not a placeholder.
- **`localStorage` THROWS when a browser refuses it**, and read unguarded it takes the whole piece
  down. `musebox`, `lamp`, `roller` and `storm` go through a `readStore`/`writeStore` pair; wrap any
  new read the same way. Losing the setting is nothing; losing the piece is everything.
- No white cut halos are left. Small targets were all grown by the button generator.
- Still open, both small: conometer leaves a 6px sliver of disc proud of the picture on a 390px
  phone (none of her four devices shows it); candler's "flashing line" went with the back-disc
  fix, diagnosis inferred not proved.

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
