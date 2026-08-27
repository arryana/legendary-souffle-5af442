# The museum wall — tried, and set down

**Aug 2026. Not live, not merged, not to be re-proposed.** This branch exists because she
asked for it to exist: *"please put all of this in a branch that we leave alone. i guess
remember it in case i ever get smarter."* It is a record of an attempt that did not work,
kept so the work isn't lost and so nobody starts it again from scratch without knowing how
it went.

**The landing page was never touched.** The apothecary case on `main` is untouched and was
untouched throughout — every picture below is a mock-up made in a scratchpad, never a page.

---

## What it was

Gemini made her an image she hadn't asked for and she couldn't get it out of her head: a
dark gallery wall, open wooden shelves, museum downlights, brass plaques. Her brief, in her
own words: *"the dramatic dark wall and open shelves, darker wood, with the museum lighting.
only with five evenly spaced shelves, so each can get its metal identifying tag."* The pull
was the museum-ness, and the wood — she missed the wood of the old walnut case but had
found it *"not as timeless or as understated"*.

She generated everything in `source/`: the wall at six shelves and at three, a long plain
version, two empty card stands, and two sets of brass tags for *sagne* and the **?**.

## What got built

`five-shelves-even.jpg` and `five-shelves-airy.jpg` — **the one thing here worth keeping.**
The wall reduced from six shelves to five, one board removed and the rest respaced, boards
kept rigid so no wood is stretched, each pool of light travelling with the board that casts
it. It works because of a piece of luck: she had photographed *the same wall twice*, once
with six shelves and once with three, same camera, same light. The three-shelf shot has
clean wall exactly where the six-shelf shot has boards, so the board that came out could be
patched with real wall rather than anything invented. If this is ever picked up again, that
pairing is why it was possible.

`tried/` — four mock-ups in the order they were made, so the shape of the failure is legible.

## Why it stopped

It never became beautiful, and four rounds of correction each made it worse in a new way.
Her words, in order: *"somehow it's awkward instead of beautiful"* → *"no. way worse."* →
*"it's just... confusing. i would immediately click away from that site"* → *"now it's all
just vague"* → *"i thought it would be beautiful but it's just shit."*

Her actual diagnosis, which is the useful part and should be taken over any of mine:

- *"look how nothing is clear and everything fights for space."*
- *"tell me what the bottom four cards even are just by looking at them. you can't. because
  who the fuck could. they're blurs."*
- *"if the lighting didn't suck and everything wasn't spaced wrong and blurred out, it
  wouldn't be half as ugly."*

She put a mock-up beside the live case to show it. The live case wins plainly: its cards are
more than twice the size, they carry no brass frame around them (two small dark clips, and
the card is the object), and its brass — the *sagne* oval, the group plates — is bright and
legible at a glance.

## Wrong turns, recorded so they aren't taken again

**Measuring was the wrong instrument.** This site's standard is to pull real numbers out of
a running piece, and it is right for fidelity — whether a plane turns at the sidereal rate.
It is not a test for beauty. Every measured correction here was true and made the picture
duller: the cards *were* filling four fifths of their bay where the case gives them half;
the lit wood *was* twice as bright as the cards, holding four fifths of the picture's
brightest pixels. Fixing both produced something she called vague. Optimising is not
composing.

**Three confident aesthetic claims were made and at least two were wrong.** They are named
here because they are the sort of thing that reads as fact in a transcript.
- *That the solid brass tags beat the framed ones, "because on a dark wall a dark centre
  reads as a hole."* Her own *sagne* oval is a dark ornate centre in a bright brass frame,
  and it is the most visible thing on the live site.
- *That the cards are the artwork and everything else is furniture competing with them.*
  Put to her; her answer was **"you're wrong. that's not what makes it ugly."**
- *That a row of sliders wouldn't have helped, because she'd be steering the same grid.*
  She then named three faults that are all sliders. It would have helped.

**The real method failure is hers to have named, and she named it**: *"we found out that i
can't do shit with images so i have to just say it's wrong, and hope for a fix. that's no
way to run a railroad."* She has the eye and no hands. Six rounds went on guessing what
"awkward" meant. A half-built adjuster — wall pre-rendered at five shelf spacings and two
lighting levels, meant to become a page with sliders for light, spacing and card size — is
in `tools/walls.py`; it was abandoned mid-build when she called the day off. **If this is
ever reopened, build that first and let her find the answer herself.** Do not open another
round of proposing.

## The standing instruction

Do not re-propose this, in this or any other form. It goes the way of the apothecary chest:
kept as a record, not built on. **Only she reopens it.**

---

# Second day (27 Aug 2026)

She reopened it herself, asking for one thing: the five-shelf wall with no light glare.
It went on for another eight rounds and ended the same way — *"this shit is going even
further off the rails and you keep getting 'bright ideas' instead of asking me."*

`tried/5` to `tried/8` are that day, in order.

## What "glared out" meant

She used the phrase three times over the two days. It was misread all three times, and
each misreading cost a round:

- read as *the lit wood outshines the cards* → the wood was measured and dimmed. She:
  *"now it's all just vague."*
- read as *the shelf lighting is too hot* → all the lamps and pools were removed, leaving
  only the ceiling soffit lights (`tried/6`). She: *"no. they're -glared out-. and i have
  said this before."*
- read as *a translucent film over the cards from a sloppy cut-out* → announced
  confidently as a found bug, then measured properly and it was false; the card centres
  render **pixel-identical** to her source files. Nothing was ever washing them out.

It meant **the brass frame around every card**. Each card sat inside a bright brass
picture frame, so twenty bright rings surrounded twenty dark pictures. Her live cabinet
holds a card with two small dark clips and no frame at all, and she had shown that in a
screen capture side by side. `tried/8` is the same picture with the frames taken off and
nothing else changed.

She had also said it at the very start, before anything was built: *"i imagine the stand
on the right without the lucite bar would be easier."* She wanted a stand. She got a frame.

## The standing instruction, sharpened

The rule at the top of this file — do not re-propose — still holds. Added to it, and it is
the more important half:

**When she says something is wrong, ask her what she means before building anything.**
Every round on both days was spent translating a plain sentence into a theory and acting on
the theory. She said *"nothing is clear and everything fights for space"*, *"they're
blurs"*, *"they're glared out"* — none of it needed interpreting, and interpreting it was
the whole failure. Her own summary, on day one: *"i have to just say it's wrong, and hope
for a fix. that's no way to run a railroad."*

If this is ever picked up, `tools/walls.py` still has the half-built adjuster. Build that
first. Do not open another round of proposing.
