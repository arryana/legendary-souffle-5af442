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

**Landing page:** `index.html` (titled *sagne*) — the **apothecary shelf**: a photograph of a
five-shelf case, the pieces standing face-front on the shelves, and the name of each type
engraved on the brass plate beneath it. It replaced the flat card grid in Aug 2026. Every
position on it derives from one table of measurements taken off the photograph itself
(`shelves.jpg`, 990x1088) — the interior opening, each shelf's surface and the plate on its
front rail. Change the picture and you change that table; don't retype percentages by hand.

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

**10 of the 20 are done.**

| File | On landing page? | Done? | What it is |
|------|:---:|:---:|------------|
| `index.html` | — | — | Landing page: the apothecary shelf ("sagne"), five shelves, all 20 pieces |
| `candler/index.html` | ✅ | ✅ | *Sagne Candle* — an interactive candle. `candler_5.html` is an alternate version (not linked)<br>**Done** — "as perfect as I can make it without overhauling the actual candle itself." |
| `roller/index.html` | ✅ | ✅ | *Roller* — a wooden tray you tilt to roll a small object around (sea-glass pebble, disc, or jellybean stone); tilt-controlled like `galileo`/`windower`'s location search but via device orientation or mouse<br>**Done**, pending her own testing of the bean's weave and the spin off a wall. Deliberately unscored: "there's other things like it, but none really do what it does." |
| `lamp/index.html` | ✅ | ✅ | An oil lamp — trim the wick's shape and height, and the flame follows. A fuel level you find by *tapping* the base is designed but not built; the note in the file records which way the pitch must go<br>**Done** as it stands — the tap-for-fuel idea is recorded as a future build, not a gap in it. |
| `warmler/index.html` | ✅ |  | A warming plate with selectable metal **finishes** (brass, copper, aged brass/copper, gold, silver, diamond-plate). `warmler-picker-concept.html` is a finish-picker concept (not linked) |
| `rain/index.html` | ✅ |  | Rain on glass |
| `ant/index.html` | ✅ |  | Ants |
| `windower/index.html` | ✅ | ✅ | A window onto the sky that follows the visitor's **local time & location** (uses geolocation + the clock)<br>**Done** once the sill light stopped being too bright on dull days and moonless nights. |
| `galileo/index.html` | ✅ | ✅ | A **Galileo thermometer** whose floats rise and sink with the visitor's **real local temperature** (open-meteo API); has a °C/°F toggle. Three instruments of different ranges, together reading 12–116°F<br>**Done** — "it needs no design changes, it covers a hell of a range, and i can't think of anything it needs to do that it doesn't." |
| `conometer/index.html` | ✅ | ✅ | A **pinecone hygrometer** — the pinecone opens (dry) and closes (wet) with the visitor's **real local humidity** (open-meteo API); has a live/manual toggle<br>**Done**. |
| `gyre/index.html` | ✅ | ✅ | Meshable **gears** you place and connect on a board, plus a signal-lamp piece whose lights are driven by the gear train. See `gears.md` for how the gear math/rendering works<br>**Done**. |
| `birds/index.html` | ✅ |  | **Birds** perched on wires strung between two poles against a sunset-sky photo; the wires sag realistically and dip under whichever bird is sitting on them |
| `bowl/index.html` | ✅ | ✅ | A still bowl of water for floating things on; has a breeze and an object picker<br>**Done**. |
| `chimes/index.html` | ✅ |  | **Wind chimes** you build yourself — pick the rod material and the cord/chain, then hang them. Uses warmler's swatch-picker pattern<br>Sound was rebuilt Aug 2026 (struck on impact, real bar overtones, pitch by material) — **awaiting her ears**, which is the only test that counts here. |
| `chladni/index.html` | ✅ | ✅ | A **Chladni plate** — sand on metal, forming standing-wave patterns in response to sound<br>**Done**. |
| `fireflies/index.html` | ✅ |  | A field at dusk where you place fireflies in the grass; real dusk-to-night sky, with bats about |
| `kaleidoscope/index.html` | ✅ |  | A tray of real photographed small objects — glass, gems, gears, beads — mirrored live. Place them, then turn the ring<br>Objects re-cropped and the desktop controls spread Aug 2026. The turning ring (top) is **drawn, not an image** — brass-bound wood with a grab knob, dimmed so it doesn't fight the mirrored view. **The tray ring (bottom) is deliberately left brighter than the scope ring** — her call: the bright one pulls the eye first and says *drop things here*, then you look up and the dim ring's view makes sense. Don't 'fix' the mismatch; it is the wordless instruction. **Awaiting her verdict**. |
| `moths/index.html` | ✅ |  | **Moths** losing their bearings on a hanging bulb. Not attraction — a moth holds a course by keeping a distant light at a fixed angle, and a near one wraps that course into a spiral. Three sliders: dusk→dark, bulb, how many. Colour is a readout of depth (dark in front of the glass, pale behind), from her own three-shade cut<br>Built Aug 2026 from her brief, then put right by her own watching of it — she found that the moths crowded the bulb and stayed (an absorbing state: all five reached it and none ever left), that moths in front of the lower glass came out grey rather than black, that they all flew alike, and that they never tilted or wavered. In **natura**, which is therefore a shelf of four |
| `musebox/index.html` | ✅ |  | A **music box** — set pins on the disc to write a tune |
| `pendulum/index.html` | ✅ | ✅ | A **Foucault pendulum**, its swing slowly turning with the Earth; real-photo globe with a locator search<br>**Done** — precession, swing and pin ring all verified by measurement against the real physics. |
| `storm/index.html` | ✅ |  | A **storm glass** whose crystals form and clear with the visitor's real changing weather (open-meteo) |
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

**A card stands on the board, not at the lip of it.** Aug 2026 the shelves were given
headroom: every one now has the same 132px between its ceiling and where a card's foot
lands, done by stretching the flat dark band of back panel inside each shelf while the
boards, rails, crown and plinth were carried across rigid. That took the photograph from
1088 to 1232 tall. A card's foot sits `seatBack` (8px) behind the front lip, so a sliver of the
lit top shows in front of it. That number is narrow on both sides: on the lip they read as
propped in front of the furniture, and 18px back they read as hovering above it. The
cards' shadow is a short contact one for the same reason. The three upper brass plates were in shadow and their
names couldn't be read, so a lit plate was set into each of those sockets. The **?** is a
brass disc of hers (`shelfdisk.png`) let into the middle of the plinth carving, with the
question mark engraved into it; the case stands on the floor of the page rather than
floating in the middle of it.

**The favicon** is her own candle, cut off its ground and wrapped inside `favicon.svg`, so
every page that already links to that file picks it up without a reference changing. The
same cut-out makes `apple-touch-icon.png` and `icon-192/512.png` on the site's navy.

**No words on it that aren't cut into it.** The only lettering on the shelf is engraved
into the photograph: *sagne* on the crown oval and the five group names on the brass
plates. The card names that used to float over a piece on hover were removed Aug 2026 —
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
five shelf plates — the very plates, each cut from its own place in `shelves.jpg` — and
rolling one unfolds that group's pieces beside it. A mouse hovers to unfold and clicks the
plate to go; a thumb taps once to unfold and twice to go, the same bargain the case itself
strikes. A plate links to `/index.html#<group>`, which opens the case already zoomed to
that shelf. **That block is generated** — run `python3 tools/shelf-tags.py` from the repo
root after changing the shelves table, and it rewrites the marked block on all 19 pages
from the table itself. Don't hand-edit between the `shelf-tags` markers; the next run
overwrites it.

**Interaction.** On a touch screen it is three taps — shelf, then card, then open — because
a phone cannot show a card big enough to read; her idea, and the right one. With a fine
pointer a card opens on the first click instead, and the shelf zoom stays reachable from the
name plates. If you change the picture, the zoom transforms recompute themselves from the
measurement table; nothing there is hand-typed.

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

**Don't add a second weather provider as a failover.** It was considered and rejected: the
alternatives need an API key, and a key in a static page is readable by anyone and gets
rate-limited or revoked, which is a worse failure than the outage it insures against. Failing
honestly is the answer here, not a second source that can quietly disagree with the first. (These are also why a *faithful* Preview matters — a plain
screenshot can't show live weather.)

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
