# gyre gear system — how it works

Reference notes for working on `gyre.html`'s gear engine. This covers the math, the object
model, the render pipeline, drag/drop + meshing, and the signal-lamp piece as a worked example
of building a new non-gear placeable on top of the same system.

Everything lives in one `<script>` block in `gyre.html`. There's no build step — it's a single
canvas 2D scene, redrawn every frame.

---

## 1. The tooth math

Three constants drive every gear's shape:

```js
const MODULE=5.4, ADD=MODULE, DED=1.25*MODULE;
const pitchR=N=>MODULE*N/2, outerR=N=>pitchR(N)+ADD;
```

- **`pitchR(N)`** — the *pitch radius*: the imaginary circle where two meshing gears' teeth
  actually make contact. This is the number that matters for spacing — **two gears mesh
  correctly when the distance between their centers equals `pitchR(a.N) + pitchR(b.N)`.**
  Nothing else.
- **`outerR(N)`** — pitch radius plus the addendum (`ADD`): the physical outer edge of the
  teeth. Used for drawing and for hit-testing (`outerR(g.N)` is a gear's click/drag radius),
  never for spacing.
- **`DED`** (dedendum) — how far the tooth root sits *inside* the pitch circle.
- **`MODULE`** is the one true source of tooth size for the whole scene. Every gear anywhere —
  tray, board, or the signal-lamp's internal gears — uses this same module, which is exactly
  why they all mesh with each other regardless of tooth count.

`gearOutline(c, N, wornTooth)` walks `N` teeth around the circle and traces the trapezoidal
tooth profile (root → tip → tip → root) using `pitch = 2π/N` as the angular step. `wornTooth`
is an optional tooth index rendered slightly shorter, for character (see §3).

**Hard-won gotcha:** tooth-to-tooth *spacing* along an edge (e.g. the signal-lamp's screw
thread ridges, or checking two gears' teeth actually interlock rather than clash) must be
measured at the **outer radius**, not the pitch radius — `2π·outerR(N)/N`, not `π·MODULE`.
The outer edge is the surface that actually makes contact.

**Second gotcha:** getting two gears' *center distance* right does not mean their teeth
interlock cleanly — that also depends on each gear's *rotational phase* at that angle. Two
gears at the exact correct distance can still have tooth-tip touching tooth-tip instead of
nesting into the gap. When you need to hand-tune a phase offset (like the signal-lamp's
`bigAngle=-0.113`, see §7), **do not just eyeball a screenshot** — render both tooth outlines
as polygons and check for actual overlap area across a sweep of angles (Shapely or equivalent).
A render can look "close enough" while still being in the worst part of the overlap curve.

---

## 2. The gear object

```js
let gears=[], idc=0;
const mk=(N,x,y,fixed)=>({id:idc++,N,x,y,angle:0,fixed:!!fixed});
```

A gear is just `{id, N, x, y, angle, fixed}` — teeth count, board position, current rotation,
and whether it's the fixed driver. `id` is a stable, ever-increasing counter, used as the seed
for that gear's individual sprite (see §3) — so a gear's specific scratches/patina/chipped
tooth never change once it exists, even though nothing about its rendering is stored.

`initGears()` hardcodes the starting layout: one fixed driver `D` (N=20, screen center) plus
three gears meshed onto it at exact `pitchR` sum distances, at fixed angles around it. This
only runs once (`inited` flag) and only ever produces this one starting shape — there's no
other special-casing for the driver elsewhere except: it never gets removed by dragging it to
the tray, and it's always `order[0]`/root of the mesh tree (see §5).

---

## 3. Rendering: two different gear renderers, on purpose

- **`gearBody(N, driver, dim)`** — flat, unmarked gradient fill. Used *only* for the tray
  icons. These are catalogue art, not real objects yet, so they don't get individual character.
- **`buildGearSprite(N, driver, seed)`** — the real thing. Builds an offscreen canvas once,
  draws the full gear with per-tooth directional shading, lathe-turned concentric tool marks,
  speckle, a patina/rust blotch, a specular hotspot, and a worn ring at the bore — all seeded
  from `mulberry32(seed)` so it's fixed forever for that specific gear. This is expensive to
  draw but only runs once per gear; the result is cached (`spriteCache`, keyed by `g.id`) and
  reused every frame via `getGearSprite(g)`.

**The 2x-supersampling gotcha (previously a shipped bug, PR #44):** `buildGearSprite`'s
offscreen canvas is built at `size = Math.ceil((Ra+4)*2)*2` with `c.scale(2,2)` applied before
drawing — i.e. the canvas pixel dimensions are **2x** the gear's true size, for antialiasing.
When drawing that sprite back onto the main canvas, you must draw it at **half** its raw pixel
size:

```js
ctx.drawImage(sp.canvas, -sp.half/2, -sp.half/2, sp.half, sp.half);   // correct — sp.half is size/2
```

Drawing it at `-sp.half, -sp.half, sp.size, sp.size` (the sprite's *full* raw pixel dimensions)
renders every gear at exactly 2x its true size — which still looks fine in isolation, but
silently breaks all the `pitchR`-based mesh-distance math, since the visual teeth no longer
match where the game thinks the gear's edge is. This shipped live once. If gears ever look like
they're overlapping or gapping despite the numbers checking out, check this line first.

`drawGear(g, dim)` draws a soft drop-shadow copy of the outline first (offset `(3, 4.5)`, black
35% alpha), then the real sprite, rotated by `g.angle`. `dim` desaturates/darkens a gear that
isn't currently part of the powered train (see §5) — the visual cue for "placed but idle."

---

## 4. The tray

```js
const TRAY=[8,12,16,22,30,40];
```

`layoutTray()` lays these out as evenly spaced slots along the top of the screen, plus one more
slot for the signal-lamp (`lampTrayRect`, always the last slot — see `n=TRAY.length+1`). Each
tray entry just remembers its center point and hit radius; picking a new gear/lamp from the
tray is handled entirely in the `pointerdown` handler (§6), which creates a brand new gear/lamp
object positioned at the cursor and immediately starts dragging it.

To add a new stock gear size: just add the tooth count to `TRAY`. Nothing else needs to change
— layout, tray icon rendering, and pickup all key off the array.

---

## 5. Meshing and the drive train

```js
function buildTrain(){
  const n=gears.length, adj=Array.from({length:n},()=>[]);
  for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){ const a=gears[i],b=gears[j];
    const d=Math.hypot(a.x-b.x,a.y-b.y), t=pitchR(a.N)+pitchR(b.N);
    if(Math.abs(d-t)<MESH_TOL){ adj[i].push(j); adj[j].push(i); } }
  const parent=new Array(n).fill(-2), order=[]; if(n){ parent[0]=-1; const q=[0];
    while(q.length){ const u=q.shift(); order.push(u); for(const v of adj[u]) if(parent[v]===-2){ parent[v]=u; q.push(v);} } }
  return {parent,order};
}
```

Run fresh every single frame (cheap — the gear counts here are always small). Two gears are
"meshed" purely by distance: if their center-to-center distance is within `MESH_TOL` (7px) of
`pitchR(a.N)+pitchR(b.N)`, they're connected. No angle/orientation check for plain gears — a
gear meshes with anything at the right distance, in any direction.

From that adjacency, a breadth-first search from `gears[0]` (**always the fixed driver** —
this is an assumption baked into the code, not just convention) produces:
- `order` — every gear reachable from the driver, in BFS order
- `parent[i]` — which gear drives gear `i`

Anything **not** in `order` is disconnected from the driver — physically present on the board,
but not part of a live train. `connected = new Set(order)` is checked everywhere that needs to
know "is this actually turning."

**Angle propagation**, once per frame, walking `order` (skipping the root, which is driven
directly by the speed slider):

```js
const conn=Math.atan2(g.y-p.y,g.x-p.x);
g.angle=-(p.N/g.N)*(p.angle-conn)+conn+Math.PI+Math.PI/g.N;
```

This is a *position* formula (computes `g.angle` fresh from `p.angle` every frame, not an
incremental velocity integration) — it's derived from: two meshing gears rotate in opposite
directions, at a rate inversely proportional to their tooth counts, and the tooth phase at the
contact point must line up (the `+Math.PI+Math.PI/g.N` term). Because this is recomputed from
scratch off `p.angle` every frame rather than integrated, a gear's angle only depends on its
mesh-parent's *current* angle and the constant connection geometry, and doesn't gradually
drift regardless of retiming, mesh changes mid-frame, etc.

`angVel[]` is the same propagation done for *angular velocity* rather than position — needed
because the signal-lamp (and any future piece driven by "whatever gear touches it") needs to
know a gear's instantaneous speed and direction, which you can't recover by diffing `angle`
across frames near a discontinuity (e.g. a gear getting connected/disconnected). `angVel[idx] =
-(p.N/g.N)*angVel[parent[idx]]`, with `angVel[order[0]] = speed*1.05` (or `0` if paused) as the
root case.

---

## 6. Drag, drop, and collision

`drag` is a single shared variable — only one thing (a gear or the lamp) can be dragged at a
time: `{kind:'gear'|'lamp', obj, ox, oy, ...}`. `ox,oy` is the cursor's offset from the
object's origin at pickup time, so the object doesn't jump to be centered under the cursor.

**Picking something up** (`pointerdown`) checks, in order: tray gear slots → the lamp tray slot
→ existing board gears (topmost/last-added first) → existing lamps. First hit wins and starts a
drag. Grabbing from the tray creates a brand new object at the cursor and drags *that*.

**While dragging** (`pointermove`): the object just follows the cursor 1:1 — `x=cursorX-ox`.
For gears, this is immediately followed by `resolveOverlap(g)`:

```js
function resolveOverlap(g){
  for(let iter=0; iter<4; iter++){ let moved=false;
    for(const o of gears){ if(o===g) continue;
      const minD=pitchR(g.N)+pitchR(o.N), dx=g.x-o.x, dy=g.y-o.y, d=Math.hypot(dx,dy);
      if(d<minD-0.01){ const a=d>1e-6?Math.atan2(dy,dx):Math.random()*Math.PI*2;
        g.x=o.x+Math.cos(a)*minD; g.y=o.y+Math.sin(a)*minD; moved=true; } }
    if(!moved) break; }
}
```

**This exists because gears used to be able to overlap** — before this was added, dragging
followed the cursor with zero collision, and the drop-time "snap to nearest mesh" logic (below)
only fires if you land *close* to a valid position; drop far from anywhere valid (e.g. dead
center on top of another gear) and it just stayed there, fully overlapping. `resolveOverlap`
runs continuously during the drag itself (not just at drop), pushing the gear radially outward
along the line between centers the moment it gets closer than `pitchR` sum to any other gear —
i.e. it can reach *exact meshing distance* (teeth touching) but never closer. The 4-iteration
loop handles being squeezed between multiple gears at once (resolving one collision can
introduce another). This intentionally does **not** apply to the lamp — the lamp's own solidity
isn't modeled; only gear-vs-gear overlap is prevented.

**Letting go** (`pointerup`/`pointercancel` → `endDrag`):
- Drop above `y=130` (the tray band) removes the object — except the fixed driver gear, which
  can never be deleted this way.
- Otherwise, look at every other gear, find the one whose required mesh distance is closest to
  actual distance, and if that error is under `SNAP_TOL` (18px, deliberately looser than
  `MESH_TOL`'s 7px — this is "close enough that snapping feels helpful," not "close enough to
  already be meshed"), nudge the dropped object to land at the *exact* correct distance and
  angle from that neighbor.

For the lamp, the same snap-on-drop logic exists but is measured from the **screw's tip**, not
the tile's center (see §7) — and a very-low-movement pointerup on the screw itself is treated as
a click-to-rotate instead of a drag (`moved<8 && drag.downOnScrew`).

---

## 7. The signal-lamp piece

The signal-lamp is a real-photo box (two colored lights + a screw) with two hand-drawn gears
inside it, meshed together, and a real-photo screw that's the tile's *only* external
connection point. It's a template for adding future non-round placeables to the board — read
this section before building another one.

### Two coordinate spaces

The photo asset (`gyre-lamp-box.png`) was built and measured against a specific reference
photo, at a scale (`LAMP_GS = 2.475`) chosen purely to make the box art and the gear art look
right together (see the sagne project chat history for how this number was arrived at — it was
tuned entirely by eye against reference photos, split the difference between two visually-tested
extremes, then adjusted twice more for centering and tightness). Nothing about `LAMP_GS` is
mechanically meaningful — it's a *rendering* scale factor, not a gear ratio.

Because of that, every position inside the lamp exists in **two parallel spaces**:

- **"Raw" space** (variable names ending `Raw`) — pixel coordinates in the box photo's own
  native resolution, at `LAMP_GS` scale. This is what you'd measure with a ruler on the photo
  itself, and what the drawing code uses directly (`drawLamp` does `ctx.scale(1/LAMP_GS,
  1/LAMP_GS)` once at the top, then everything inside is drawn in raw-photo pixels).
- **"True" board space** (variable names ending `True`) — the same point, divided by
  `LAMP_GS`, so it's in the same units as every other gear's `x`/`y`/`pitchR` on the board.
  Hit-testing and mesh-distance math (anything that has to interact with `gears[]`) must happen
  in *true* space, or a lamp piece will hit-test/mesh at the wrong physical size relative to
  everything else.

If you add a new raw-photo-derived measurement (a new hotspot, a new sub-part), decide up front
which space it belongs in and be explicit about it — mixing them silently is the single easiest
way to break this piece.

### Layout constants

```js
const LAMP_BIG_N=20, LAMP_SMALL_N=10, LAMP_GS=2.475;
const LB_bx0=114, LB_by0=93, LB_bw=987-114, LB_bh=772-93;   // box bounds, measured on the photo
```

`LB_bx0/y0/bw/bh` are the box's boundary as measured directly on the reference photo (the left
edge specifically had to be pulled in from an earlier attempt — the photo has a warm-toned
metal bevel between the wood table and the gray box face that reads as a stray sliver if the
crop mask is even a few pixels too generous). `LB_cx/LB_cy` — the box's own visual center —
becomes local `(0,0)` for everything else, so the whole assembly rotates around a sensible
point when the tile spins (see below).

The big gear's position, the small gear's position (derived from the big gear's position plus
the exact `pitchR` sum at a hand-picked `lampMeshAngle`), the screw's size (derived from the
small gear's `outerR`) and position, and the two jewel (light) positions are all computed once,
at load time, as constants — none of this is recomputed per-frame. Only *rotation angles*
(`bigAngle`, `smallAngle`, `phase`) and *facing* change at runtime.

### Facing and rotation

```js
let lampFacing = 0..3;  // stored on the lamp object
function lampFacingAngle(lamp){ return lamp.facing*Math.PI/2; }
```

Clicking the screw (a near-zero-movement pointerup where the pointerdown landed on the screw's
hit zone) increments `facing` by 1 (mod 4) — the *whole tile* (box, lights, both gears, screw)
rotates 90° as one rigid unit around the box's own center. This was a deliberate choice over
the alternative (keep the box/lights upright and only swing the screw+small-gear arm around a
pivot) — see the sagne chat history for the reasoning: rotating the whole tile needs zero extra
geometry, since a square rotated in place naturally cycles which edge the screw exits from.

`lampScrewWorld(lamp)` rotates the screw's local *true*-space offset by `facing`'s angle and
adds the lamp's board position — this is the function anything outside the lamp (mesh-distance
checks, drag-to-screw hit testing) uses to find out where the screw currently, physically is.

### Engagement (how it meshes with a real gear)

The screw is the tile's only mesh point. `LAMP_SCREW_ENGAGE_R` (derived from the screw/worm's
half-height, converted to true space) plays the same role a gear's own `pitchR` would in a
normal mesh check — required distance from a neighboring gear's center to the screw is
`pitchR(neighbor.N) + LAMP_SCREW_ENGAGE_R`.

```js
function lampEngagement(lamp, connected){
  const screwPos=lampScrewWorld(lamp);
  let best=-1, bestErr=1e9;
  for(let i=0;i<gears.length;i++){ const o=gears[i], reqD=pitchR(o.N)+LAMP_SCREW_ENGAGE_R;
    const e2=Math.abs(Math.hypot(screwPos.x-o.x,screwPos.y-o.y)-reqD); if(e2<bestErr){bestErr=e2;best=i;} }
  return (best>=0 && bestErr<MESH_TOL && connected.has(best)) ? best : -1;
}
```

Run every frame. The lamp only lights up / spins if its best-matching neighbor is **both**
within `MESH_TOL` (a real mesh, not just "nearby") **and** itself part of the live powered train
(`connected`, from `buildTrain()` — see §5). A screw touching an idle, disconnected gear stays
dark, same as a screw touching nothing.

### Driving the lamp's own animation

```js
const bigSpeed = ni>=0 ? -angVel[ni]*(gears[ni].N/LAMP_BIG_N) : 0;
lamp.bigAngle += bigSpeed*dt;
lamp.smallAngle -= (LAMP_BIG_N/LAMP_SMALL_N)*bigSpeed*dt;
lamp.phase -= outerR(LAMP_SMALL_N)*(LAMP_BIG_N/LAMP_SMALL_N)*bigSpeed*dt;
lamp.speed=bigSpeed; lamp.engaged=ni>=0;
```

Note the direction of the drive chain: **the outside gear drives the screw, the screw drives
the small gear, the small gear drives the big gear.** The lamp's own two internal gears never
touch anything outside the tile — only the screw does. `bigSpeed` here is really "how fast and
which way the *big* gear ends up turning," derived from the meshed neighbor's angular velocity
and the tooth-count ratio between them (as if the screw were a simple 1:1 relay — it isn't
modeled as a real worm gear, this is a deliberate simplification, see below). From there,
`smallAngle` and `phase` (the screw thread's scroll position) are both driven off `bigSpeed` at
their own correct ratios, same logic as §5's `angVel` propagation.

`lamp.speed` (signed) is what the light-glow code reads: sign picks red vs. blue, magnitude
(clamped) picks brightness. Idle/unmeshed is `speed=0` → no glow at all, drawn with the same
`dim` treatment as a disconnected gear.

**Known simplification, worth knowing about:** a real worm-and-wheel mechanism requires the
worm's axis to sit *perpendicular* to the wheel it drives (like a guitar tuning peg) — a worm
cannot mesh edge-to-edge with a spur gear the way two spur gears mesh with each other. This
piece deliberately does not model that; the screw-to-neighbor-gear relationship is treated as a
simple coplanar mesh for the sake of having *a* working connection point at all. If this ever
needs to be mechanically rigorous instead of "reads correctly to the eye," that relationship
needs rethinking from scratch.

### Rendering gotcha carried over from §3

The lamp's two internal gears are drawn from the exact same `buildGearSprite`/2x-supersampled
sprite system as every board gear, so the same `-sprite.half*LAMP_GS/2, ..., sprite.half*LAMP_GS`
scaling rule applies (the extra `*LAMP_GS` on top of the usual `/2` halving is because these
are drawn in *raw* photo space, not true board space — see the two-coordinate-space section
above).

### Assets required

`gyre-lamp-box.png` (box + both lights, no gears/screw baked in), `gyre-lamp-screw-capL.png`,
`gyre-lamp-screw-thread.png` (one tileable segment), `gyre-lamp-screw-capR.png`. All real
photos, not drawn. If these are ever regenerated, the raw-space constants in §7 (`LB_bx0` etc.,
`LAMP_CAPL_W`/`LAMP_THREAD_W`/`LAMP_CAPR_W`/`LAMP_PHOTO_H`) need to be re-measured against
the new asset's actual pixel dimensions — they are not derived from anything, they're
hand-measurements baked in as constants.

---

## 8. Debugging tips

- `window.__gyreDebug = () => ({...})`, temporarily attached at the bottom of the IIFE and
  removed again afterward, is a fast way to peek at/drive internal state (gear positions, lamp
  state, `lampScrewWorld`, etc.) from a Playwright script without adding permanent test hooks
  to the shipped file. Always remove it again before committing — check `git status`/`git diff`
  before pushing.
- When testing drag/drop or meshing behavior with a screenshot, watch out for **unrelated
  pieces sitting nearby in the same shot** — it's easy to end up with a demo gear from an
  earlier test step still on the board, visually confusing the exact thing you're trying to
  demonstrate. Move it off-screen (`g.x += 900` or similar) before the screenshot, or crop it
  out, rather than leaving ambiguous clutter in a shot meant to explain one specific thing.
- `requestAnimationFrame(tick)` must be the *first* call, not `tick()` — the animation loop
  passes a timestamp `t` as `tick`'s only argument, which becomes `lastT` on the first frame.
  Calling `tick()` directly (no arg) makes `t` (and therefore every derived delta/angle/phase)
  `NaN` on that first frame, and because most of this state is accumulated (`angle += ...`,
  `phase -= ...`) rather than recomputed fresh, **that one bad frame poisons every frame after
  it forever** — the piece will render as visually frozen and missing anything drawn through a
  tiling loop keyed off the poisoned value (a `NaN` loop bound never satisfies its comparison,
  so the loop body silently never runs — this is exactly how the signal-lamp's screw thread
  went completely missing the first time this bug was hit).
