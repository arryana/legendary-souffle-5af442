# bowl

The full record of this piece, moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short.
Everything here was written as it happened; the newest material is at the bottom. Read it before
touching `bowl/index.html`.

A still bowl of water for floating things on; has a breeze and an object picker

**Done**.

**Where it comes from, because it explains the piece.** Her grandmother used to set a bowl out and she would float the same objects in it — so what is inherited here is the **practice**, not the vessel: set a bowl out, choose things, float them. The ten bowls themselves are the opposite of a reconstruction. They are *"bowls we never had but i think are beautiful"* — stone, china, copper. Don't reduce the set to one "authentic" bowl on the grounds of provenance; the variety is the point and the memory is the gesture.

Aug 2026, found by measuring for a 3-inch phone: the dock is one row that never wrapped and wants **369px** laid out end to end, so on anything narrower the LAST thing in it — the flower, which is the whole object chooser — was pushed clean off the right edge, and with the page unable to scroll there was no way to reach it. It cleared a 390px phone by 22px, which is exactly why it looked perfect everywhere anyone had looked. Behind that sat a second fault: the chooser popup is a fixed 326px grid and hung 43px off **both** edges of a 240px screen, so fixing the button alone would only have revealed half the flowers. Below 379px the dock now wraps to two lines and the popup drops to three slightly smaller tiles; above it, nothing applies and the dock is pixel-identical at 390, 600 and 1200. The wrapped row is **right-aligned, not centred** — the music button is pinned in the bottom-left corner and a centred second row lands straight on top of it.

**It did not load on the Jelly Star** — her report, Aug 2026, and it was true in the
strongest sense. The ten bowl photographs are 1408x768 and about 1.5MB apiece, **15.7MB**
of them, and *nothing was drawn until every one had arrived*: the first `resize()` and the
first frame both sat behind one `Promise.all` over the lot. The picker made it worse, building
ten `<img>` thumbnails pointing at the same full-size files. Measured at 240x350 with the CPU
six times slower and the connection at 1.6Mbps: **the bowl had still not appeared after 100
seconds**, having pulled 21.5MB. Only the bowl on screen is loaded now; the other nine come in
behind the running piece **one at a time** (ten at once is worse on the machine that is already
struggling), a thumbnail's `src` is set only once its photograph is in the cache, and asking for
a bowl that has not arrived fetches it and takes it the moment it lands rather than swapping to
an empty bowl. **12.0s and 2.3MB** on the same simulated phone, and **she confirmed it on the real Jelly
Star** — *"bowl works fine now"* — so the simulation held. The other half of that fix was not bowl's
at all: see the shelf plates' cards above, which every page on the site was fetching on load. Worth
drawing the general lesson, since it took a report to find it — these pages had been swept for layout
faults several times and **nobody had ever measured what one of them FETCHES**. A sweep that only
looks at where things land cannot see 6MB queued in front of the piece.

**The object menu grew**,
her ask off the machines: *"the menu could pop up larger on both the jelly star and the kindle."* It
was a fixed 4x64 grid that dropped to 3x60 on a narrow screen and never grew for a wide one — so a
Kindle showed a laptop's tiles with a third of the room going spare. Measured: **66px at 240 (was 60),
72 at 390 (was 64), 92 on a Kindle (was 64, so +44%)**, and a desktop is untouched. Sizes are explicit
rather than fractional on purpose — a Fire tablet's browser is the oldest of her four and
`aspect-ratio` is not to be relied on there — and the rules sit at the END of the sheet, because a
media query adds no specificity and the base `.pickerOption` is declared below where they first
went.

**Her question, and the answer**: *"how are the stones removed? a second click on them?"* No —
each tile in the chooser carries its own **⊘** and a column of quantity dots; that is where things come
out. It was not discoverable because at 60px the ⊘ was too small to read, which the bigger tiles go
some way to fixing. Whether a second tap on the object itself should ALSO lift it out is a design call
and hers; it was put to her, and her answer came back: **yes.** A **tap** lifts a stone out;
a **drag** still moves it. The two gestures cannot be confused for one another and neither needs
explaining, which is the whole point. Six pixels of travel is the line between them, because a hand is
never perfectly still. The water is left rocking where the stone came out — the same splash ring a
dropped one makes, since a stone taken OUT of water disturbs it exactly as much as one put in. Before
this, nothing removed a stone at all: the only thing that ever did was the tenth pushing the first off
the end of the list.
