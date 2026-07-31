# storm glass — how the weather states are built

Internal notes for whoever (Claude, future session) needs to add or adjust a
weather state in `storm/index.html`. Not linked from the site; a reference
for editing the code.

## The idea

Not one "more or less stormy" dial. Five distinct, named conditions — the
traditional storm-glass reading vocabulary — each a different *arrangement*
of the same four real ingredients. Every condition is one JS object in the
`RECIPES` map (`ORDER = ['sunny','warming','rain','storm','snow']`), read by
`renderRecipe()`, which paints onto a copy of the one fixed vessel photo.

The vessel photo (`storm-background.png`) never changes. Its own pixels are
scanned once (`buildProfile`) to find the true glass interior at every row
(`Y_TOP` = liquid line, `Y_BULB_BOT` = true bulb bottom, excluding the
foot/stem) — every zone below is clipped against that, so nothing can ever
draw outside the glass or bleed into the base, regardless of how the photo
itself is shaped.

## The four ingredients (real macro photos, not procedural drawing)

- `storm-tex-crystals.jpg` — one large, cleanly isolated snowflake/crystal.
  Cropped once to a clean 260×260 square (`bigData`, region `280,340,290,290`
  of the source), plus a horizontally mirrored copy (`altBigData`) so a
  second clump never has to reuse a visibly-identical shape.
- `storm-tex-smallcrystal.jpg` — a dense field of many small crystals.
  Stretched full-frame (`smallData`) for a granular, all-over dusting.
- `storm-tex-wisps.jpg` — vertical ice wisps/streaks. Stretched full-frame
  (`wispData`).
- `storm-tex-bubblesdense.jpg` / `storm-tex-bubblessparse.jpg` — bubbles at
  two densities. Stretched full-frame (`bubbleDenseData` / `bubbleSparseData`),
  and also sampled at small raw offsets for individual bubble clumps (see
  below) — different offsets into the same photo, so several clumps never
  repeat the same patch.

## Building blocks (recipe flags)

**Large flake clump(s)** — `bigAmt` (opacity), `bigReach` (size, fraction of
the 260px clump canvas), `useAltBig` (use the mirrored crop), `layered`
(blend both crops together for one denser clump — used by snow),
`extraFeathers` (add two smaller, dimmer offset clumps either side, so it
reads as branching rather than one sprite), `manyFlakes` (storm only — a
whole hand-placed pile of ~18 overlapping flakes low in the vessel; see the
`stack` array in `renderRecipe`, each entry a `{dx, dy, s, alt}` offset from
the main clump's position).

**Bubble clumps** — three patterns, all built from the same
`renderClumpZone` primitive (see below):
- `bubbleClumps` (rain) — one bold, well-defined dense-bubble mass low in
  the centre, plus five smaller loose sparse-bubble clumps scattered around.
- `smallBubbleCluster` (sunny, currently unused in favour of `spreadAmt`
  below, kept for reference) — a tight knot of ~5 tiny bubbles at the
  bottom centre only.
- `seltzer` (currently unused, kept for reference) — ~16 small bubble clumps
  spread pseudo-randomly (golden-ratio index trick, not `Math.random` — stays
  deterministic) across the *whole* water column. Turned out to read as "a
  few floating dots in clear water" rather than "fizzy," which is why storm
  and sunny both switched to `spreadAmt` instead for a true dense fill.

**Dense fizzy fill** — `spreadAmt` (the mechanic that ended up doing the most
work for storm and sunny): mixes the small-crystal texture and a bubble
texture (`spreadBubble: 'dense'|'sparse'`) across the *full width* of every
row, not as discrete clumps. `spreadBubbleOnly: true` drops the crystal
component (sunny — no crystal at all, bubbles only). `spreadTaper: true` +
`spreadTaperStart` (0–1, fraction down the water column where density starts
ramping up) makes it clear near the liquid line and rise into a dense mass
lower down — `spreadTaperStart: 0.3` (storm, full-height dense-to-clear
taper) vs `0.62` (sunny, density confined to roughly the bottom third).

**Top/bottom streaks** — `streakAmt`/`streakReach` (vertical wisps below the
liquid line), `streakCentered`/`streakSpread` (confine horizontally toward
the vessel's midline instead of full width — rain's "a couple of streaks in
the top centre"), `bottomStreakAmt`/`bottomStreakReach` (a second, separate
band of wisps near the base, sampled from a different texture offset so it
doesn't repeat — warming's flanking wisps).

**Old full-width bottom band** — `bottomAmt`/`bottomTex`/`bottomReach`: an
earlier mechanic (a flat band of one texture across the full width near the
bottom). Superseded by `spreadAmt` for anything that needs real density, but
still there and functional if a future state wants a plain flat wash.

## `renderClumpZone` — the shared clump renderer

Used for every discrete "blob" (crystal flake or bubble cluster) — a `clumps`
array of `{cx, size, botY, amtMul, tex, edge, floor, gamma, fadeMul, raw,
offX, offY}` objects, rendered by `renderClumpZone(clumps, globalAmt, y, l,
r, acc, noise)` once per row.

Two sampling modes:
- Normal (`raw` unset) — the clump's own texture is assumed pre-cropped to
  exactly `CLUMP` (260×260) and mapped onto the clump's actual on-canvas
  size. Used for crystal flakes (`bigData`/`altBigData`).
- `raw: true` — samples the shared full-frame texture directly at
  `offX`/`offY` plus the clump's own local coordinates, so several clumps
  can each show a different patch of one big bubble photo without tiling or
  repeating. Used for all bubble clumps.

Per-clump tuning, all fighting the same failure mode (see below):
- `floor` (default 0.12) — background-brightness cutoff before amplifying.
  The crystal photo's "empty" areas are near-black, but the *dense* bubble
  photo runs quite hazy/bright even where there's no bubble (median ~90/255)
  — needs a much harder floor (~0.34–0.46) or it tints the glass like a
  visible box.
- `gamma` — extra contrast exponent after the floor cut, so a source patch
  that's itself fairly uniform still separates into distinct blobs with
  visible gaps, instead of reading as one flat wash.
- `fadeMul` — controls how much of the clump's radius stays full-strength
  before the edge starts fading (`hFade = (1-distX)*fadeMul`, clamped).
  Higher (~1.8–2.1) = crisper edge, more of the interior stays flat.
  Lower (~1.3) = softer, rounder, more forgiving of an uneven source patch.
- `edge` — vertical feather width in px (via `zoneAlpha`).

### The recurring bug: clumps rendering as a hard rectangular box

Happened three separate times this build (rain's first bubble clumps, one of
the "scattered" clumps that had actually been wrong since rain and only
became obvious once storm's plainer background exposed it, and the seltzer
scatter). Root cause every time: the *source crop* sampled for that clump
happened to be almost uniformly bright across its whole window (a big
merged blob of bubbles filling the frame edge-to-edge), so no amount of
edge feathering can make a uniformly-bright interior look like anything but
a filled shape — feathering only softens the *boundary*, it can't recreate
texture that isn't in the source crop.

Fix is never "feather harder" — verify the actual source crop first:

```python
from PIL import Image
import numpy as np
img = Image.open('storm-tex-bubblessparse.jpg').convert('L')
arr = np.array(img)
block = arr[y:y+size, x:x+size]
print('mean', block.mean(), 'max', block.max(), 'frac>100', (block>100).mean())
```

Want a *low* mean (~15–35/255) with a *high* max (a real bright bubble
present) and a small `frac>100` (~0.02–0.08) — i.e. mostly dark with one or
two genuinely isolated bright spots, not a merged bright mass. A grid scan
(`for by in range(...): for bx in range(...): ...`) over the whole source
photo finds good candidates fast; screenshot-crop each candidate to confirm
visually before wiring it into a clump's `offX`/`offY`.

## The five current recipes (as of this write-up)

- **snow** — one large, dense layered clump (`layered: true` blends both
  flake crops) plus two extra branching feathers. No bubbles, no streaks.
- **warming** — a smaller centred flake, strong vertical wisps near the top,
  and a second smaller set of wisps near the base (different texture offset).
- **rain** — no crystal. A couple of streaks confined to the top centre
  (`streakCentered`), one bold dense-bubble mass at the bottom plus five
  loose sparse-bubble clumps scattered around it (`bubbleClumps`).
- **storm** — `spreadAmt` with `spreadTaper` fills the whole water column,
  clear near the top and dense/fizzy toward the bottom (`spreadTaperStart:
  0.3`), a big layered flake cluster, and `manyFlakes` piles ~18 more large
  flakes on top of that density. Important: the flake clumps' own opacity
  (`amtMul: 1`) has to clearly exceed the background fizz's peak
  (`spreadAmt: 0.62`, deliberately capped below 1) or the flakes wash out
  into the background — this was a real bug, not just a taste call.
- **sunny** — `spreadAmt` again, but `spreadBubbleOnly: true` (no crystal)
  and `spreadTaperStart: 0.62` so the dense bubble fizz is confined to
  roughly the bottom third, plus streaks spanning the top two-thirds
  (`streakReach: 0.66`, not centred — full width).

## Adding a sixth condition

1. Pick a name, add it to `ORDER` (also drives the live-weather mapping in
   `fetchWeather` and the key UI below — check both if the new state should
   be reachable live, not just manually).
2. Add a `RECIPES` entry using the building blocks above.
3. Add a key button (weather-icon SVG + label) — see the `#key` markup and
   `.keyItem` styling in `index.html`.
4. Iterate visually — screenshot loop:
   ```bash
   python3 -m http.server 8934   # from repo root, run_in_background:true
   ```
   `file://` triggers a canvas cross-origin taint error on `getImageData` in
   this sandbox — always test against `http://localhost:8934/storm/` instead.
   A small Playwright script (see any `verify-*-only.js` left in the
   scratchpad from past sessions) — uncheck `#chkLive`, click the relevant
   `.keyItem` (or, if still present, set `#conditionSlider`), screenshot.
5. If a reference photo exists, do a direct side-by-side crop comparison
   before calling it done — several rounds this build only converged once
   actual pixel-level comparison replaced eyeballing at a glance.
