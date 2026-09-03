# Touch targets, the music button, and the generators

Moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short. Written as it happened; read it
when working on this part of the site.

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
