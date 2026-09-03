# windower

The full record of this piece, moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short.
Everything here was written as it happened; the newest material is at the bottom. Read it before
touching `windower/index.html`.

A window onto the sky that follows the visitor's **local time & location** (uses geolocation + the clock)

**Done** once the sill light stopped being too bright on dull days and moonless nights.

Fourth piece
through her four-device test, Aug 2026. **`windower-frame.png`'s centre pane was cut out of a light
background** and kept a 3px white halo all the way round it — the same family of fault as the shelf plates,
and she spotted it as the same thing. Recoloured to the frame's own wood with the alpha ramp kept, inside and
out of the cut, so the pane's edge stays soft. The side panes were clean.

The layout on a Kindle or a 3in
phone ran 65–140px past the bottom of the page, taking the flag and half the controls with it, and both fixes
are hers. **The discs moved inside the window's own top corners** (they had been sitting half on it and half
off, and the room kept clear above them was room the piece could have used) — `position:absolute` there
rather than fixed, so if a screen still has to scroll they travel with the window instead of hanging over it,
and the rules are written `html #backlink` / `html #shelfdisc` **because the shelf disc's own block is
generated and sits at the end of the body, where a plain `#shelfdisc` rule loses to it on source order**.
And **the sill gives way**: the window box gets shorter and the frame is anchored to its top, so what is lost
is the sill rather than sky or proportion, and the light patch is masked to the same box so what's left of it
still catches the sun. A Kindle turned sideways needed one thing more — the chart is drawn at 78vw and so
grows with a wide screen however short it is, so in landscape under 560px tall it is capped by height
instead. All of it is held to `(pointer: coarse)`; the desktop layout is identical to the live site,
measured.

**The window shows the same slice of sky whatever shape it is** — about 100° either side of
south, mapped to a percentage of the opening, so on a phone the sun crosses a narrower window rather than
going behind the wall for part of the day. A real aperture that narrow would crop the sky instead of
squeezing it, and this was put to her as a fidelity question in Aug 2026. **Her ruling: it stands.** *"The
representation still appears to be what other people would be seeing outside. I'm okay with that."* Cropped
honestly, a phone would show an empty sky for hours at a stretch. Don't re-propose it. (The sun and the
hills are both percentages of the window, which is why they stay registered with each other at any shape —
including the shortened one; take height off the bottom only, below the hills, or that breaks.) |

Aug 2026 the
location flag moved up onto the line with the three tickboxes, her call. It had been on a line of its own
below them, and that line was what pushed the page 27px off the bottom of a 1440x900 laptop; it now fits
that screen exactly. A 1200x860 window is still 12px over — small, known, not chased.
