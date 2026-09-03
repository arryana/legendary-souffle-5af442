# gyre

The full record of this piece, moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short.
Everything here was written as it happened; the newest material is at the bottom. Read it before
touching `gyre/index.html`.

Meshable **gears** you place and connect on a board, plus a signal-lamp piece whose lights are driven by the gear train. See `gears.md` for how the gear math/rendering works

**Done**.

Two of hers, Aug 2026.

**The parts stand in a column down the left on a screen wider than it is
tall.** The tray used to run across the top, which is the whole width of the board it exists to help
you fill; the room that frees is the point of the change. It falls back to the row when the column
would not fit — measured, a 3in phone sideways leaves a band of 156 units between the brass disc and
the dock against the 308 seven parts need, and both are pinned in SCREEN pixels so how much of the
BOARD they eat depends on the zoom below.

**And the board zooms out on a small screen.** The lamp
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
the row 3px and nothing else.

Two tweaks of hers after seeing it: **the lamp stands at the head of
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
either way, so the little ones are as easy to pick as the big ones.
