# galileo

The full record of this piece, moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short.
Everything here was written as it happened; the newest material is at the bottom. Read it before
touching `galileo/index.html`.

A **Galileo thermometer** whose floats rise and sink with the visitor's **real local temperature** (open-meteo API); has a °C/°F toggle. Three instruments of different ranges, together reading 12–116°F

**Done** — "it needs no design changes, it covers a hell of a range, and i can't think of anything it needs to do that it doesn't."

Third piece through her four-device test, Aug 2026, and the fault was
that **a finger is not a pointer**. A float tapped on a touch screen was enlarged only while the finger was
held on it — and the finger then covered the very thing it had enlarged, so on the Kindle and the 3in phone
you could never actually see one. A tap now leaves it up; tap it again, tap a different float, or tap
anywhere else and it goes away. That last part is her rule for popups generally: *they go away if touched
again or if something around them is touched* — the flag's search closes the same way. The `pointerenter`
/`pointerleave` pair is **guarded to `pointerType === 'mouse'`**, because a touch raises those two as well
and unguarded they put the enlargement straight back down on release; don't remove the guard. The flag
itself and the line that answers it were 15px and 11px, which is a mouse dimension in the same way a 3px
slider is: under `(pointer: coarse)` they go to 22 and 15 with the field at 19. Desktop untouched.

Note
for anyone measuring this: **the floats' hit circles overlap**, so a tap lands on whichever is topmost, and
comparing "the hit circle I aimed at" with "the float that came up" will show a mismatch that isn't one.
Check `document.elementFromPoint` instead — the enlargement always belongs to the float actually under the
finger.

She then found the **floats puddling wrongly in the teardrop's base**, and the cause is worth
keeping: **the floor of a narrowing vessel is a bowl, not a plane.** Everything that sank came to rest on one
height, `lo`, the same all the way across — so five floats sat in a flat row out to a width the glass does not
have down there. What gives it away is the **tag**: a float is not a sphere, a metal tag hangs about two
thirds of a bulb-width below its centre, and by that depth the teardrop has closed in by another 40 units, so
the outer floats' tags hung straight through the glass. Swept across 14–118°F, **116 of 1015 placements had
some part of a float outside its vessel; it is 0 now**, with no float interpenetrating another in either
version. The depth a float can reach is now a function of how far out it sits.

One thing there is
delicately balanced. Among spots that settle equally deep the code prefers the one *resting against
something*, the glass included, and that is what stops the tube's twelve floats stacking into a tower up the
middle — its floor is flat, so every spot is the same depth and contact is the only thing left to choose by.
But on a curved floor a spot at the wall is genuinely higher, and the old slack (`bh*0.40`, 17.7 units) was
wide enough for it to win on contact — which perched the whole heap up the side of the bowl with clear glass
beneath it. **So the slack is now the flatness itself**: full where the floor is flat, strict where it curves.
Don't replace it with a constant in either direction — one value cannot serve both vessels. The tube's
arrangement is unchanged at every temperature bar 1–2 of 255 in the anti-aliasing.
