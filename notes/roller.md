# roller

The full record of this piece, moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short.
Everything here was written as it happened; the newest material is at the bottom. Read it before
touching `roller/index.html`.

*Roller* — a wooden tray you tilt to roll a small object around (sea-glass pebble, disc, or jellybean stone); tilt-controlled like `galileo`/`windower`'s location search but via device orientation or mouse

**Done**, pending her own testing of the bean's weave and the spin off a wall. Deliberately unscored: "there's other things like it, but none really do what it does."

**It did not tilt AT ALL on the Kindle** — her report, Aug 2026, and the cause was a missing
fallback rather than anything about tilt. The gate offers two ways in, the phone button and the
desktop one. Pressing the phone button turned device orientation on and **assumed it worked**, with
`return` before the pointer path was ever wired — so on a machine whose browser never fires
`deviceorientation` the tray had **no control whatever** and the only way out was reloading. A Kindle
Fire has an accelerometer and still may not fire it. It now waits 1.4s for a usable reading and, if
none comes, takes the listener off and uses the pointer instead. Measured on a browser that never
fires the event: **0 pixels moved under a finger drag before, 5293 after**.

Three
things Aug 2026, all hers, all after she had it in front of her.

**The speed slider was not a speed
slider.** It multiplied how hard tilt pushed and nothing else — not friction, not the wall bounce — so
once anything was moving it careered about at much the same rate wherever the slider sat. Measured
under a held full tilt: the pebble averaged **130px/s at the bottom of the range against 146 in the
middle**, eleven per cent, nothing anyone could feel, while its PEAKS moved two and a half times. She
asked for a speed slider so things could slide slower and it was reasonable to think there wasn't
one. What actually makes a thing slide slowly is the surface, so below the middle the tray now gets
draggier as well as gentler — the same friction raised to a higher power, which is what a shorter
settling distance is. Re-measured: pebble **73px/s** at 20, disc **48**, bean **63**, and the peaks
down by more.

**And it still read as not working, which took a second report to find**: *"the speed
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
it this way round rather than retuning the physics. The bottom of the range went from 20 to 10.

**The
dock spreads on a desktop.** Four groups stacked in a column 180px wide under a 640px tray on a
screen 1440 across, with the speed row lapping over the tray's own bottom edge. Side by side now, and
the dock stands 92px instead of 184, so it stops touching the tray. Gated on **width AND a fine
pointer**: the generated `touch-targets` block grows each slider by half the distance to its nearest
neighbour, measured on the stacked layout, so a coarse screen has to keep the layout those figures
came from — a Windows tablet in landscape is wide but coarse and keeps the column.

**The bean is
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
colour. The pebble and the disc are untouched.
