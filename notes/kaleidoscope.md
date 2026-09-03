# kaleidoscope

The full record of this piece, moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short.
Everything here was written as it happened; the newest material is at the bottom. Read it before
touching `kaleidoscope/index.html`.

A tray of real photographed small objects — glass, gems, gears, beads — mirrored live. Place them, then turn the ring

Objects re-cropped and the desktop controls spread Aug 2026. The turning ring (top) is **drawn, not an image** — brass-bound wood with a grab knob, dimmed so it doesn't fight the mirrored view. **The tray ring (bottom) is deliberately left brighter than the scope ring** — her call: the bright one pulls the eye first and says *drop things here*, then you look up and the dim ring's view makes sense. Don't 'fix' the mismatch; it is the wordless instruction. **Done** — her verdict came on Mon 24 Aug,
after the ring drag was made a real turn and the card reshot: *"i have checked those on the machines
and they are great."* That closes the question this row had been carrying open.

**The ring drag was a sideways swipe, not a turn.** Aug 2026, her
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
on touch.

**And the knob was decorative** — her report, Aug 2026: *"the ring is turnable, but the
knob itself has no hand option and no turn cue, which seems to defeat the point of there being a
knob."* The grip layer stands **13% proud** of the scope's own box so the knob can overhang the edge,
and it carries `pointer-events:none` — so the knob sat outside the only element that carries the turn.
Measured at 110% of the radius: the pointer landed on the page wrapper with `cursor:auto`, and a drag
begun **on the knob turned the ring not at all**. A pseudo-element on `#scopeWrap` reaches the grab out
over the whole grip ring; events on a pseudo-element target its host, so the existing `pointerdown`
picks them up unchanged and `ringAngle` measures from the same centre. Now: `cursor:grab` on the knob,
and a drag from it turns the ring. The ring also **brightens while the pointer is over it**, under
`(pointer: fine)` only — a finger has no hover. That is not a hint: nothing is explained and nothing
appears, it is the piece answering, which is the one thing the no-nudging rule does allow.

**The card was still the old look** — flat gold stripes and a sparse pattern, from
before the ring was redrawn as brass-bound wood with a grab knob and the objects re-cropped. Reshot
Aug 2026 with a spread of pieces on the tray at warm and cool hues, the tray and controls hidden so
only the scope is in frame, and the brass scaled to the card's full width by **measuring** the ring's
painted extent in the shot rather than trusting a ratio. Same 440x640 as the rest.

**The phone case was
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
**not** blur: you don't blur the thing someone is aiming at.

**That fix was measured at the phone's FULL height, which is
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
is no longer owed**: scrolling is the answer she took, not a placeholder for one.
