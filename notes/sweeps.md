# Site-wide sweeps: the innerHeight trap, halos, mouse dimensions, blocked storage

Moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short. Written as it happened; read it
when working on this part of the site.

### Three faults turned out to be systemic, so all sixteen untested pieces were swept for them

Measured on 21 Aug, before testing rather than after, so her device time goes on what a sweep cannot
see. **None of these four are fixed yet** — she asked for them to be ready to fix, and the offer
stands:

**One caution about how this was swept, because it caught me out.** The first pass laid each page out
at the device's FULL height and asked what fell below the visible line — which is exactly what the
trap does, but it cannot tell an unfixed page from a fixed one, since a page that measures
`innerHeight` would never have been that tall. Re-measured at the height a device actually leaves
visible, the four flags came apart:

| piece | at the true visible height | what it really is |
|---|---|---|
| `chladni` | was 36–101px under the bar on all four | **the trap. Fixed 21 Aug** — lays out to `innerHeight` now, and the plate is sized off the same figure or it stays scaled to a screen the visitor hasn't got. Desktop identical, measured. |
| `storm` | fits on all four | **nothing to do** — it got the `innerHeight` fix earlier the same day. The sweep flagged its own blind spot, not a fault. |
| `musebox` | fits, bar 24px on a Kindle sideways | **mild**: it already carries `min-height:100dvh` with a `100vh` fallback, and its page can scroll, so the tempo control is reachable. Left alone. |
| `kaleidoscope` | 63–167px over on three of the four | **not the trap — the design debt its own row describes.** The content genuinely does not fit; a proper small-screen arrangement is still owed and is her call, not a repair. |

`warmler`, `roller`, `gyre`, `chimes`, `birds`, `fireflies`, `moths`, `ant`, `lamp`, `rain`, `bowl`
and `pendulum` are clear on all four.

**White cut halos: none left.** Nine files flagged by a crude test, all innocent on inspection — the
pinecone frames do carry a pale rim but the cone sits on a photograph of straw, so nothing shows; the
chime rod's bright edge is the wood's own curve; the rest were masks, which are meant to be white.
That fault was confined to the shelf plates and windower's centre pane, both fixed.

**Mouse dimensions: one good surprise, one steady drip.** Galileo's press-and-hold float was the
**only** hover-only behaviour on the site — nothing else asks for a gesture a finger cannot perform.
What does recur is small targets: tickboxes and icon buttons at **14–29px** where a thumb wants about
40 (chladni's mic and sound boxes 16, lamp's mute 14, ant's food box 16, storm's live box 16,
musebox's save and clear 22x18, bowl's two pickers 29x21, roller's colour buttons 26). The sliders
measure 25–33px, but those are already grown as far as their neighbours allow by the `touch-targets`
pass, so they are at their limit rather than neglected.

### Blocked storage took four pieces down, two of them signed off

Aug 2026, found by loading every piece with its props taken away rather than by anyone hitting
it — the check roller's Kindle failure should have prompted and didn't. **`localStorage` does not
merely come back empty when a browser refuses it: it THROWS.** A private window does it, and so
does any browser set to block site data — a Fire tablet's Silk is exactly the sort that might.
Read unguarded at the top of a script, that one refusal takes the **whole piece** down: with site
data blocked, **`musebox`, `lamp`, `roller` and `storm` all came up blank**, and `roller` and
`storm` are both pieces she has passed on all four machines. `candler` had wrapped its own read in
a try/catch all along and survived, which is what the right answer looks like.

Every read and write now goes through a `readStore`/`writeStore` pair in each of the four. Verified
both ways: blocked, all four draw with no errors; working, every setting is still written and still
survives a reload (`sagne-muted`, `sagne-volume`, `sagne-musebox-voice`, `sagne-roller-glass`,
`sagne-storm-sethand`). **Losing the setting is nothing; losing the piece is everything** — and the
general point is the one bowl's row already makes about page weight: *these pages had been swept
for layout faults many times and nobody had ever asked what happens when something they lean on
says no.*

**Still open, both small:** `conometer` leaves a 6px sliver of disc proud of the picture on an
ordinary 390px phone (none of her four devices shows it, so it was left); and candler's "flashing
line" — the back disc, before it was pinned, sat in the flow inside the area the flame repaints, so
its edge was being re-rasterised every frame. It went with the fix; the diagnosis is inference, not
proof.


**What that conometer line actually means, run down 4 Sep 2026** because she asked and the sentence
above could not be decoded from itself. The shelf disc is `position:fixed` at the window's top right
on all twenty pages, at `opacity:.55`. Conometer's picture is sized to the window, so as the window
shortens the picture's top edge climbs until it meets the disc. Measured at 390 wide: at 844 the disc
sits clear on the dark wall; at 780 the picture laps 9px over its foot; from about 740 down the disc
is wholly over the photograph, and at 664 it also overhangs the picture's right edge by 4px.
**The disc stays fully tappable at every height** (five sample points, all hitting it). What changes
is contrast: against the bright straw the disc alters its own patch of screen by **7.6–8.6** average
levels against **21–25** on the dark wall — about a third as present. Looked at rather than measured,
**it still reads**: the rim and the arrow hold, because the disc already carries its own
`drop-shadow(rgba(0,0,0,.65) 0 1px 3px)`. So it is washed out, not lost, and it is cosmetic.
**Swept all twenty pieces for the same collision**: only `candler`, `warmler`, `lamp` and `conometer`
put the disc over a picture at all, and the first three do it at *every* height and hold 41–50 levels
of contrast — **and she has passed candler and warmler on all four machines**, which is the evidence
that a disc lying on a picture is fine in itself. Conometer is the only one where the background is
bright enough to wash it. **Left alone, and here is the case for leaving it**: the disc's CSS is
inside the generated `shelf-tags` block, so any change to it goes through `tools/shelf-tags.py` and
lands on all twenty pages, twelve of which she has already passed — a wide risk for a cosmetic fault
in a band of window heights none of her four devices occupies. If it is ever to be fixed, the lever
is the resting `opacity`, not the shadow (the shadow is already there); `.85` was tried and is
crisper but changes every page's disc, so it wants her eye first. **Put to her with the three
pictures on 4 Sep 2026 and closed: *"yeah, i think it's probably left better as it is"*.** So this
is now her call rather than an open item, and it should not come back as a proposal.
