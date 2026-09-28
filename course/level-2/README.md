# Level 2 — Sounds Together

## Who this level is for

Anyone — age 5 or age 55 — who has finished **Level 1** and can, at ≥90% accuracy:
read and spell every single-letter sound taught there (`s a t p i n m d g o c k ck e u r
h b f l ff ll ss zz j v w x y z qu`), read CVC real and nonsense words, add the `-s`
plural, and read/recognize the Level 1 heart words (`a, I, the, is, to, of, and, was,
said, you, are, he, she, we, me, be, do, what, they, one, have, go, no, so`).

If a learner cannot do that yet, send them back to Level 1 — Level 2 assumes it as a
100% floor and every decodable text in this level is built on it. There is no
"catch-up inside the lesson" — see `course/level-0/placement-test.md`.

## What Level 2 adds

Single letters can only spell so many words. Level 2 teaches the **two- and
three-letter spelling teams** that unlock hundreds more real words without any new
vowel sounds: consonant digraphs (`sh ch tch th wh ng nk`), consonant blends (2- and
3-letter, at the start and end of words), the three inflected endings `-s/-es -ed
-ing/-er`, and the jump from one-syllable to two-syllable closed-syllable and
compound words (`rabbit, napkin, sunset`).

No new vowel sounds are introduced in this level — every vowel is still the same
short `a e i o u` from Level 1. That is deliberate: Level 2 is entirely about
**consonant teams and word endings**, so the only new load per lesson is the
consonant pattern itself.

## Entry requirement

Level 1 mastery check passed at ≥90% (real words + pseudowords + dictation). If a
learner scores 90%+ on **this level's own placement probe** (see
`course/level-0/placement-test.md`) they may skip directly to whichever lesson their
accuracy first drops below 90% — skip-ahead is always earned by a check, never
assumed by age or grade.

## Exit criteria (must hit ALL of these to move to Level 3)

1. Reads real words and pseudowords containing every grapheme below at ≥90% accuracy.
2. Reads CCVC and CVCC words (e.g. `stop, desk, blend, crisp`) and 3-letter-blend
   words (e.g. `string, scrap`) at ≥90%.
3. Reads closed-syllable 2-syllable words and compounds (e.g. `napkin, rabbit,
   sunset, catfish`) at ≥90%.
4. Spells (dictation) words using `-s/-es`, `-ed` (all three sounds), and `-ing/-er`
   correctly.
5. Reads all 29 Level 2 heart words on sight (plus all Level 1 heart words retained).
6. Comprehension: answers literal + one inferential question correctly on a Track A
   or Track B decodable text, AND participates in the Listen & Talk discussion
   (comprehension is tracked as its own metric — see DESIGN.md rule 8. A learner who
   decodes perfectly but cannot answer comprehension questions has **not** exited
   Level 2; go back to the Listen & Talk routine, not back to phonics).

If any single criterion is below 90%, do not advance — reteach the specific lesson
that introduced the failing pattern (see that lesson's Check step for the exact
reteach instruction) and re-test. Calendar time never overrides the gate (DESIGN.md
rule 4).

## Sequence table (exact order — do not reorder; decodability of every later lesson
depends on earlier ones)

This table and heart-word schedule are the **CANONICAL** Level 2 schedule from
DESIGN.md §3, enforced by `tools/decodable.py`'s `HEART` dict — every lesson's own
heart-word section and story text must match this table exactly (Round 1 gauntlet
defect: an earlier draft had each lesson teaching the *next* lesson's pair one
lesson early, which silently made every "new heart word" in the level premature).

| # | File | New grapheme(s) | New heart words | Fluency routine starts? |
|---|---|---|---|---|
| 2.1 | L2.01-sh.md | `sh` | says, for | — |
| 2.2 | L2.02-ch-tch.md | `ch, tch` | there, where | — |
| 2.3 | L2.03-th.md | `th` (voiced /ð/, unvoiced /θ/) | were, from | — |
| 2.4 | L2.04-wh.md | `wh` | come, some | — |
| 2.5 | L2.05-ng-nk.md | `ng, nk` | done, want | — |
| 2.6 | L2.06-initial-blends.md | `st sp sn sm sl sw sk sc bl cl fl gl pl br cr dr fr gr pr tr tw` | put, push | **Yes — model→echo→choral→independent starts here** |
| 2.7 | L2.07-final-blends.md | `-st -nd -nt -mp -sk -lt -ft -lk` | pull, full | continues |
| 2.8 | L2.08-three-letter-blends.md | `str spr scr spl squ shr thr` | who, could | continues |
| 2.9 | L2.09-s-es.md | `-s / -es` (plural + 3rd person) | would, should | continues |
| 2.10 | L2.10-ed.md | `-ed` (/t/ /d/ /ɪd/) | your, four | continues |
| 2.11 | L2.11-ing-er.md | `-ing, -er` (no base change) | many, any, her | continues |
| 2.12 | L2.12-compounds-2syllable.md | compound words + closed 2-syllable VC/CV | does, goes, two | continues |
| 2.13 | L2.13-review.md | cumulative review, no new grapheme | again, friend, because | continues |
| 2.14 | L2.14-mastery-check.md | — (assessment) | — | — |

**Heart-word schedule at a glance** (2 new per lesson through 2.10, then 2–3 per
lesson 2.11–2.13 to land exactly on Level 2's full list, per DESIGN.md's CANONICAL
schedule): says, for, there, where, were, from, come, some, done, want, put, push,
pull, full, who, could, would, should, your, four, many, any, her, does, goes, two,
again, friend, because — **29 words total**, 2.01–2.13, none new at 2.14. Every one
is taught as a **heart word**: sound out the regular part first, mark only the
truly irregular letters as "the heart part" to know by heart (research/05 §1,
"High-frequency words / heart words" — ~63% of common high-frequency words are
already phonetically regular in part; nothing here is rote whole-word drilling).

## Fluency routine (starts Lesson 2.06)

From L2.06 onward, the **Read it** step in every lesson adds a short fluency routine
before comprehension questions, because by then learners have enough decodable text
to make oral-reading practice worthwhile (research/05 §5b):

1. **Model** — tutor/parent/audio reads the Track A or B text aloud first, at a
   natural pace, so the learner hears the target prosody before attempting it.
2. **Echo** — learner repeats each phrase-cued chunk (marked with `/`) right after
   the model.
3. **Choral** — tutor and learner read the whole text together, out loud, at the
   same time.
4. **Independent** — learner reads the same text alone.

This is **not** a race for speed. Prosody (expression, phrasing) is checked
alongside accuracy — a learner who reads fast in a flat monotone has not "won"
fluency (research/05, Rasinski & Samuels: fluency = automaticity + pace + prosody,
not speed alone). Phrase-cue marks (`/`) are printed through 2.10 and then faded.

## Track A / Track B — same skill, two registers

Every decodable text in every lesson exists twice: **Track A** (child — home, school,
pets, play) and **Track B** (teen/adult — job, cash, bus, shop, rent, bills, the
clinic). Both tracks use **exactly the same taught graphemes and heart words** — an
adult learner is never handed a "the cat sat on the mat" text (DESIGN.md rule 6;
research/04 §5.2 and §3 "no visible child-coded material in the adult track").
Because Level 2 has not yet taught r-controlled vowels (`ar, er, ir, or, ur` — that's
Level 4), words like *car, market, work, turn, born* cannot appear yet in either
track even in the adult text — the adult register comes from **topic and sentence
content** (cash, rent, a shift, the bus, the boss), not from harder phonics.

## Decodability gate: the tool decides, not the writer (Round 1 gauntlet fix)

Every lesson's story text (the `>` blockquote lines in section 7 — comprehension
**questions live outside the blockquote**, never inside it, because they are asked
of the learner, not decoded by the learner) must clear
`python3 tools/decodable.py course/level-2/lessons/<file>.md` before it ships. A
Round 1 gauntlet critique found the hand-authored "Decodability audit" footers were
themselves wrong in multiple lessons — they missed real untaught words (`says`,
`for`) hiding in plain sight because those two words simply weren't on any heart-word
list at all, and over-flagged words that were actually fine. **The rule now: run the
tool, fix the text until it reports `untaught=` empty (or only genuine, deliberately
chosen pre-taught story words), and paste the tool's own output into the audit
section — never re-derive the audit by eye.**

**Hard cap on pre-taught exceptions:** at most **2** flagged pre-taught story words
per Track A text and **2** per Track B text. A lesson that needs more than that to
reach the ≥95% decodability target is not "under the ceiling with a note" — it gets
rewritten, not footnoted, until it's under the cap for real (Round 1 gauntlet defect
#13).

## Urdu-speaker notes carried in this level

- **L2.03 (`th`)** — Urdu has no interdental sounds; `/θ/` (think) and `/ð/` (this)
  get replaced with `/tʰ/` and `/d/`. Explicit tongue-position drill + minimal pairs
  (research/04 §6).
- **L2.06 and L2.08 (consonant blends)** — a documented transfer pattern for
  Urdu/Hindi-L1 speakers is inserting an extra vowel before an initial `s`-cluster
  ("school" said as "sakool"/"iskool"). This specific pattern is not in research/04's
  four numbered trouble spots, but it follows directly from research/01 point 8
  (English consonant clusters that don't exist the same way in the learner's L1 need
  explicit contrastive drilling) and is well documented in general Urdu/Hindi-English
  phonology — flagged here as a practical tutor tip, not a numbered research claim.
  Drill: say the whole cluster as one unbroken unit before the vowel, no sound
  in between (`st-` not `is-t-`).
- **L2.10 (`-ed`)** — the three-way sound split (`/t/ /d/ /ɪd/`) does not map onto
  any single Urdu spelling rule, so it needs to be taught as its own explicit,
  listen-and-sort skill rather than assumed obvious from print.

## Time

20–35 minutes per lesson (per DESIGN.md §4 template), self-paced — a learner or
tutor may split any lesson across two sittings; nothing is lost by pausing
(DESIGN.md rule 10).

## Files

```
README.md                          this file
lessons/L2.01-sh.md … L2.14-mastery-check.md
mastery-check.md                   the full Level 2 exit gate (real+pseudo+dictation
                                    +passage+comprehension, pass/fail routing)
```
