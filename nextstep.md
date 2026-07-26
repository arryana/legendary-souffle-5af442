# Getting started next time — a quick guide

This is a plain-language cheat sheet for working with Claude on the sagne website. Keep
it handy for your next session.

---

## 1. Starting a new session (on the Claude desktop app, Mac)

A **session** is just one ongoing conversation with Claude. Everything you and Claude say
and do in it piles up as you go — that's normal, but a very long session can get slow or
messy, the same way a phone call that's gone on for hours gets hard to keep track of.

**To start a fresh one:**
1. Open the Claude desktop app (the regular app window — not a black terminal screen).
2. Look for a **"New session"** (or **+**) button, usually near the top of the window.
3. Pick this website's project so Claude knows which files it's working with.
4. Just start typing what you want, the same way you would here.

Starting fresh doesn't erase anything — every change that's already been made **Do**ne is
saved on the real website, not in the conversation. Old sessions stay around too, so you
can always go back and look at one if you want to remember how something was done.

**Rule of thumb:** if you're starting a *new, separate* idea (a new piece, a different
kind of change), start a new session for it. If you're continuing the *same* piece of
work from a few minutes ago, just keep going in the one you're in.

---

## 2. What `CLAUDE.md` and `gears.md` are

Think of these as two different instruction sheets that live with the website's files:

- **`CLAUDE.md`** — this is Claude's rulebook for the whole site. It says things like "talk
  in plain words, no jargon," "always show a Preview before making something live," and
  "each piece lives in its own folder." Claude reads this **automatically, every single
  session** — you never have to mention it or remind Claude it exists.

- **`gears.md`** — this is much narrower: detailed technical notes just about how the
  **gyre** piece's spinning-gear animation works under the hood. It's only useful if
  someone (a future Claude, or a technical helper) needs to dig into that one piece's
  inner workings. You'll basically never need to think about this file day-to-day.

### `CLAUDE.md` files in general (a bigger idea than just this one file)

`CLAUDE.md` isn't a one-off — it's a general habit Claude Code follows everywhere, and
it's worth understanding the shape of it:

- **A `CLAUDE.md` can live in more than one place.** The one at the very top of the
  website's files (the one we've been talking about) applies to *everything*. But any
  folder can have its own `CLAUDE.md` too, with notes that only matter for what's inside
  that folder.
- **Claude always checks for them, automatically** — you never have to say "please read
  your instructions." It reads the top-level one every session, and if it's working
  inside a specific folder, it checks that folder for its own `CLAUDE.md` as well.
- **Think of it like sticky notes at different scales.** One big sticky note on the front
  door for "how this whole house works" (the root `CLAUDE.md`), and — if you ever wanted
  — a smaller sticky note inside one specific room for "this room also has a quirk you
  should know about."
- **This ties directly to today's folder change.** Now that every piece (warmler, lamp,
  galileo, etc.) lives in its own folder, each one *could* get its own small `CLAUDE.md`
  someday if a piece ever needed its own special notes — the same way `gears.md` holds
  gyre-specific notes today, just in the more standard/automatic form. Nothing like that
  exists yet, and you don't need to create one — this is just good to know the shape of,
  in case a piece ever gets complicated enough to want its own notes.

---

## 3. When these matter — and how it connects to what we did today

- **`CLAUDE.md` matters every time**, automatically. You don't opt into it — it's always
  in effect. It's *why* Claude offers Preview → Do → Undo, keeps changes small, and (as of
  today) knows that new pieces should go in their own folder rather than loose at the top
  level.

- **`gears.md` only matters if you're changing the gyre piece specifically**, and even
  then, only for the tricky internal mechanics — not for simple things like "change this
  color."

- **Plan mode** is the tool Claude uses for anything bigger than a small, simple tweak —
  a new feature, a change that touches many files, anything where there's more than one
  reasonable way to do it. In Plan mode, Claude looks around and writes down exactly what
  it intends to do *before* touching anything, and waits for you to approve it. That's the
  direct fix for the problem that started this whole conversation: a big change made by
  guessing-and-checking with expensive picture-by-picture iteration, instead of thinking it
  through once, in writing, first. Today's folder reorganization is a good example — Claude
  planned the whole thing, asked a few plain-language questions, and only then made the
  change.

  For small stuff (fix a typo, tweak one color, nudge some text) Claude will just show you
  a **Preview** and ask for a **Do** — no need for the longer Plan-mode process.

**In short:** you don't need to manage any of this yourself. Claude reads the rulebook
automatically, reaches for Plan mode on its own when a change is big enough to warrant it,
and always shows you Preview before Do. Your job stays the same two words: **Do** and
**Undo**.
