# conometer

The full record of this piece, moved out of `CLAUDE.md` on 3 Sep 2026 so that file stays short.
Everything here was written as it happened; the newest material is at the bottom. Read it before
touching `conometer/index.html`.

A **pinecone hygrometer** — the pinecone opens (dry) and closes (wet) with the visitor's **real local humidity** (open-meteo API); has a live/manual toggle

**Done**.

Second piece through her four-device
test, Aug 2026. The picture is centred and grows with the screen, so on a short wide one its top corners
came up under the two brass discs and each disc sat **half on the photograph and half off it**. Her rule for
this, and it settles the general case: *half-on* is what reads as a mistake — wholly on or wholly off both
look deliberate. So on a 3in phone, where the discs sit entirely inside the picture, nothing was changed and
nothing should be: pushing them outside there would leave the picture too narrow to read, which is her call
and a good one. Where they did straddle an edge the picture's SIDES are trimmed to clear them, which costs a
tenth of the picture where clearing them vertically costs nearly a third.

Underneath that, the same fault
candler had: `html,body{height:100%}` with `overflow:hidden` is the whole screen with the browser's bar
counted as though it weren't there. On a Kindle that put the flag's own reply line under the bar — so you
could type a location in, and the piece would go and fetch it, and the line saying where it had gone was off
the screen. That is what "no location response" was. It lays out to `innerHeight` now, held steady while the
flag's field has focus. The flag also answers **Enter directly** rather than relying on the form submitting
itself: an on-screen keyboard is not a keyboard, and the Go key on some Android browsers leaves a one-field
form alone. **The same flag is on `galileo`, `windower`, `storm`, `pendulum`, `chimes` and `fireflies`, and
they have not had that line yet.**
