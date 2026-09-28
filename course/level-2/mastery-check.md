# Level 2 Mastery Check — "Sounds Together" exit gate

Administer this after `L2.13-review.md` scores ≥90%. This is the real gate into
Level 3 — score every component separately, and do not round up (DESIGN.md rule 4).
Never prompt with a picture, a guess, or "what would make sense" — every word is
sounded out (DESIGN.md rule 1). Zero penalty for stopping partway and resuming
later (DESIGN.md rule 10).

## Component 1 — Real words (one from every Level 2 pattern, 28 words)

`shop, wish, catch, much, think, that, when, which, king, bank, strap, string,
scrub, thrill, desk, gift, milk, nest, wishes, boxes, jumped, wanted, helper,
jumping, rabbit, napkin, sunset, catfish`

*(28 words listed — use all of them; ≥90% of 28 = 25.2, so the real threshold is
the next whole word up: ≥26 correct (26/28 ≈ 92.9%), not 25 — a Round 1 gauntlet
fix; 25/28 ≈ 89.3% is below 90%, not at or above it.)*

## Component 2 — Pseudowords ("alien words," one style per pattern family, 12 words)

`shob, chib, thron, whass, zink, strab, splunt, thruv, fand, nusk, florbes,
flisked`

*(12 words; ≥90% = at least 11 correct. Every item here was checked against a
dictionary word list to confirm none is a real English word — "splint" was in an
earlier draft and is a real word (a rigid support for a broken bone), which
defeats the point of a pseudoword item; replaced with "splunt," confirmed not a
real word.)*

## Component 3 — Dictation

Read each aloud once at natural pace; learner segments with fingers first, then
writes.
1. Sounds: `sh`, `str`, `-ed` (as /d/, e.g. in "grinned")
2. Words: `catches`, `helped`, `sunset`
3. Sentence: **"His friend wanted to help because the shop was full."**
   *(Round 1 gauntlet fix: the previous sentence used "busy," a Level 3 heart word
   [L3.04] — a pass/fail gate instrument should be built entirely from
   already-certified Level 1–2 content, not need its own footnoted exception.
   "full" is a Level 2 heart word [L2.07] and needs no carve-out.)*

**≥90% = at most 1 error across all dictation items (sounds + words + sentence
combined, excluding the flagged word above).**

## Component 4 — Heart words (all 29 from Level 2, on sight, ≤2 sec each)

`says, for, there, where, were, from, come, some, done, want, put, push, pull,
full, who, could, would, should, your, four, many, any, her, does, goes, two,
again, friend, because`

**≥90% of 29 = 26.1, so ≥27 of 29 read instantly on sight** (no sounding out
required — these are memorized by design; if a learner sounds one out successfully
that's fine too, but slow sounding-out of many heart words signals the heart-word
method from earlier lessons needs another pass, not more raw repetition).

## Component 5 — Decoding passage (read aloud, timed for information only — WCPM
is not a pass/fail criterion at Level 2; see note below)

> Sam and his friend had a shift at the shop. / They packed a backpack with a
> napkin and a gift. / "I want to fix the vans and check the stock," / Sam said. /
> His friend helped stack the boxes and scrub the mats. / A rabbit ran past the
> bin, / and Sam's friend grinned. / "Should we catch it?" / his friend asked. /
> "No, / let's just watch it," / Sam said, / "because it is not bad." / At
> sunset, / the job was done, / and Sam and his friend went back, / glad and
> full.

*(87 words, phrase-cued, cumulative across every Level 2 pattern.)* Verified with
`python3 tools/decodable.py` against a temp copy of this passage under the L2.13
lesson number: **100% decodable, `untaught=` empty.** (Round 1 gauntlet fix: the
previous version used "buses" — a known tool edge case where a base word ending in
a single `s` right before its `-es` vowel, e.g. bus→buses, gets misread as the
silent-e "VCe" pattern — and "hurting," a genuine untaught r-controlled `ur` word
that the old audit missed entirely while flagging the fully-decodable "past" by
mistake. "past" is `p-a-s-t`, all taught single letters, and was never a real
problem.)

**Decoding score: ≥90% of words read correctly without cueing.**
*(Note on rate: Hasbrouck & Tindal WCPM norms (research/05 §5a) are K-6 classroom
norms, not validated for adult/L2 learners — do not apply them as a pass/fail bar
here. Track rate informally as a baseline for Level 3's fluency work, and always
pair it with the prosody note below, never report rate alone (research/05 §5b).)*
**Prosody check (informal, not pass/fail yet — formal prosody scoring starts in
Level 5's fluency program):** did the learner pause at the `/` phrase marks and
use natural sentence intonation, or read in a flat word-by-word monotone? Note
which, for the tutor record — a learner who decodes at 95% in a flat monotone
still needs fluency-routine practice, not more phonics.

## Component 6 — Comprehension (scored SEPARATELY from decoding — DESIGN.md rule 8)

Ask after an independent read of the Component 5 passage:
1. *(literal)* What did Sam and his friend pack in the backpack?
2. *(literal)* What did Sam's friend do while Sam checked the vans?
3. *(inferential)* Why do you think Sam says "because it is not bad" instead of
   catching the rabbit?

**≥90% here would be a high bar for 3 questions (effectively requiring all 3) — use
a lower, explicit threshold instead: at least 2 of 3 correct, with the inferential
question (Q3) always discussed even if missed, never just marked wrong and
dropped.** A learner who gets both literal questions right but misses the
inferential one is not held back — flag it for extra "why do you think" practice
during Level 3 rather than blocking advancement on it alone.

## Pass / Fail routing

| Component | Threshold | If below threshold, reteach here first |
|---|---|---|
| 1. Real words | ≥26/28 | Identify which pattern family the misses cluster in; go to that lesson's own Check step reteach (see README.md sequence table for the file) |
| 2. Pseudowords | ≥11/12 | Same as above — pseudoword errors usually point at the same family as real-word errors |
| 3. Dictation | ≤1 error | Re-run L2.10 (`-ed`) if the error is on the `-ed` item; L2.09 (`-s/-es`) if on `catches`; L2.12 if on `sunset` |
| 4. Heart words | ≥27/29 | Re-run the specific lesson(s) that introduced the missed words (see README.md's heart-word schedule) using the heart-word method, not flashcard drilling |
| 5. Decoding passage | ≥90% words correct | If errors cluster on one pattern, reteach that lesson; if errors are scattered and low-confidence overall, repeat L2.13 (Review) in full before re-testing |
| 6. Comprehension | ≥2/3 | Do not reteach phonics for this — add 2–3 extra Listen & Talk sessions with explicit "why do you think" discussion practice, then re-ask |

**All six components at threshold → the learner starts Level 3 (`L3.01`).**
**Any component below threshold → reteach exactly that component's named lesson(s),
then re-test only that component** — never restart the whole mastery check from
Component 1, and never advance by calendar time instead of by this gate
(DESIGN.md rule 4).
