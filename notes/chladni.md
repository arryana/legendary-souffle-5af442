# chladni

The full record of this piece, moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short.
Everything here was written as it happened; the newest material is at the bottom. Read it before
touching `chladni/index.html`.

A **Chladni plate** — sand on metal, forming standing-wave patterns in response to sound

**Done**. Aug 2026 it was given **substances**, in
two families that are a real inversion of each other and not a recolour: heavy grains (sand, salt)
are thrown off the moving plate and pile on the **nodal lines**, while very fine powder (lycopodium,
fine flour) is too light to be thrown and is instead swept by the stirred air to the **antinodes**,
drawing the exact negative of the same figure. They're chosen on a **slider**, her call over a row of
swatches or tickboxes: the four are genuinely in an order — coarsest and heaviest to finest and
lightest — and that ordering is the physics. The notches are evenly spaced and **nothing marks where
the figure flips**; finding that is the point. The notches themselves are the grains, each at its own
size, colour and shape (sand rounded, salt square because halite is cubic, the powders an even veil),
the same move the chimes rods got. Emoji were considered for them and don't exist: 🧂 is the only one
of the four, sand and flour have only metaphors (desert, hourglass, sheaf), and there is no spore at
all — 🍄 is a fungus and lycopodium is a clubmoss.

The notches are **her photographs**, one of each
substance, cut from a sheet she made (`chladnithumbnails.jpg` and the three full-size tiles in her
`daidle` Drive folder). Two of her decisions about them: the lycopodium notch is deliberately the
**clubmoss plant**, not the powder, so that a curious person can cut the picture and search it — and
there is nothing to see in a photograph of spores anyway; and the sheet's lettering (FLOUR, SAND, SALT
— plus a PEBBLES tile Gemini added unasked, which she didn't want) all came off. The three other
notches are cropped into the **substance itself and not the tool that is in the shot with it**: at
40px, the full tiles read as a wooden scoop and a sieve rather than as salt and flour. Photographs
need the notches at 40px; at 26 they are four beige smudges.

**Getting a picture out of her Drive
is possible — don't conclude otherwise.** This session first decided it wasn't: the network is closed
to Google, and the Drive tool hands a file back as base64 text, which at 650KB looked far too big to
carry. It isn't. When a tool result is too big it is **spilled to a file** under the session's
`tool-results/` directory and the path is handed back instead — so `json.load` that file, `base64`
-decode its `content`, and write the bytes to disk. Nothing has to be retyped, and the size stops
mattering. Two things in there are worth knowing before touching
it: the powders carry a **pile of their own volume** (a coarse count per patch of plate, pushing back
only once a patch holds more than a few times an even spread) or every grain converges on one
infinitesimal point and it reads as a bare plate with dots on it; and the powders are deliberately
drawn with **bigger, softer, fainter** marks than the heavy families, because ten thousand particles
spread over a third of the plate have to stand for clumps of powder rather than single spores.

A
**cornflour suspension** would be a genuine third family — not a scatter of particles at all but a
connected shear-thickening layer, liquid on the nodal lines and locking into standing fingers and
persistent holes over the antinodes. It was raised and **parked**, her call: it needs to be drawn as a
fluid surface rather than as marks, and *"if it can't be rendered convincingly as a fluid, let's wait
until we have better tools."* Don't re-propose it as a fifth swatch on the existing renderer.

Aug 2026 the **pitch slider's pulse
came out**. Its knob glowed until a visitor first touched it, and the comment in the code said in as many
words that it "nudges a first-time visitor toward the control that actually changes the pattern" — which is
the exact thing the *Exploring is the point* rule below forbids. It predated the rule. Don't put it back.

Aug 2026, hers off the Kindle and the phone: **the microphone tickbox joins the sound
line** below 820px instead of having a line to itself for one 16px box. It belongs beside the
sound it is an alternative to — listening to the room rather than to the tone — and the plate
gets a line of height back. The pitch is not reordered; it simply becomes the first line once
the mic stops taking one, which is where the desktop has always put it. On a 3in screen the
joined row wanted 229px against the 226 it had, three pixels short, and wrapped straight back
to two lines, so below 320 the volume gives up a little length — the one thing in that row with
any to spare. Desktop unchanged.
