# Level 3 — Long Vowels

**For:** anyone who has completed Level 1 (First Sounds) and Level 2 (Sounds Together) — child, teen, or adult, native speaker or Urdu-first ESL learner. If you are placing a learner directly into Level 3, first confirm the Level 2 exit check (CCVC/CVCC words + 2-syllable closed words ≥90%) — see `course/level-0/placement-test.md`.

## What the learner already knows (do not re-teach; assumed mastery)

**Letters/sounds:** all single consonants and short vowels (a e i o u), `ck`.
**Digraphs:** `sh ch tch th` (voiced *this* / unvoiced *thin*) `wh ng nk`.
**FLOSS:** `ff ll ss zz` (off, well, pass, buzz) + plural `-s`.
**Initial blends:** `st sp sn sm sl sw sk sc bl cl fl gl pl br cr dr fr gr pr tr tw`.
**Final blends:** `-st -nd -nt -mp -sk -lt -ft -lk`.
**3-letter blends:** `str spr scr spl squ shr thr`.
**Suffixes (no base-word change):** `-s/-es, -ed` (3 sounds: /t/ /d/ /ɪd/), `-ing`, `-er`.
**Word shapes:** compound words (sunset, backpack) and closed 2-syllable (VC/CV) words (rabbit, napkin, magnet).
**Heart words — Level 1:** a, I, the, is, to, of, and, was, said, you, are, he, she, we, me, be, do, what, they, one, have, go, no, so.
**Heart words — Level 2:** says, for, there, where, were, from, come, some, done, want, put, push, pull, full, who, could, would, should, your, four, many, any, her, does, goes, two, again, friend, because.

Every practice text in this level uses **only** the code above plus the new code and heart words taught up to that point in Level 3. See the **Decodability audit** at the end of every lesson for the exact list used.

## What Level 3 adds

Long-vowel spellings: vowel-consonant-e (VCe / "magic e" / silent-e) for all five vowels, open syllables, `y` as a vowel, soft c/g, **r-controlled `ar` and `or/ore`**, and the eight vowel-team families (`ai ay`, `ee ea`, `oa ow oe`, `igh ie`, `ue ew ui`, `oo`), plus the `-ild -ind -old -ost` closed-syllable exceptions. Level 3 is also where **flex-decoding** is introduced explicitly: several long-vowel spellings have two possible sounds (`ea`, `ow`, `oo`, `y`) or a spelling has two common patterns — the learner is taught to **try one sound, then the other, and check whether a real word results**. This is decoding self-correction, not picture/context guessing (see Rule 1, DESIGN.md).

**Round 1 gauntlet revision (this version):** `ar` and `or/ore` were moved to L3.08–3.09, *before* the vowel teams, matching UFLI Foundations (r-controlled lessons 77–83 precede the first vowel team at lesson 84) and Read Write Inc Set 2 (which interleaves `ar` into the same set as the early vowel teams). The previous ordering deferred all r-controlled vowels to Level 4 and could not keep everyday words like "park," "for," "start," and "her" out of natural sentences — the fix was reference-driven resequencing, not a rule exception. See `GAUNTLET.md` for the full critique and fix log.

## Exit standard

Reads and spells VCe, r-controlled, and vowel-team words at ≥90% accuracy (real + pseudowords), reads connected decodable text at approximately 40 WCPM-equivalent with acceptable phrasing, and can apply the flex-decode routine to a new vowel-team word without being told which sound to try. Full mastery check: `mastery-check.md`.

## Sequence (18 lessons, ~20–35 min each)

| # | Title | New code | New heart words |
|---|---|---|---|
| 3.01 | a_e | a_e (VCe) | once, only |
| 3.02 | i_e | i_e (VCe) | very, every |
| 3.03 | o_e, u_e, e_e | o_e, u_e, e_e (VCe) | great, eye |
| 3.04 | VCe + drop-e | drop-e suffixing rule (hope→hoping) | busy, people |
| 3.05 | Open syllables | single-letter long vowels (he, go, hi); V/CV two-syllable words (ro-bot, mu-sic) | water, laugh |
| 3.06 | y as a vowel | y = /ē/ (happy), y = /ī/ (my, fly) | walk, talk |
| 3.07 | Soft c, soft g | soft c (city, ice), soft g (gem, cage), -ce -ge -dge | buy, answer |
| 3.08 | ar | ar (/ar/, as in car, park, start) | whole, earth |
| 3.09 | or, ore | or (for, corn, short), ore (more, store, before) | — (all 16 done) |
| 3.10 | ai, ay | ai, ay (/ā/) | — |
| 3.11 | ee, ea | ee, ea (/ē/) | — |
| 3.12 | oa, ow, oe | oa, ow(/ō/), oe | — |
| 3.13 | igh, ie | igh, ie (/ī/) | — |
| 3.14 | ue, ew, ui | ue, ew, ui (/o͞o/) | — |
| 3.15 | oo (flex) | oo — moon /o͞o/ and book /o͝o/ | — |
| 3.16 | -ild -ind -old -ost | -ild -ind -old -ost | — |
| 3.17 | Review | — (cumulative practice, no new code) | — |
| 3.18 | Mastery check | — | — |

**Level 3 heart-word list, in teaching order (2 per lesson, complete by L3.08):** once, only, very, every, great, eye, busy, people, water, laugh, walk, talk, buy, answer, whole, earth.

## Decodability exceptions in this level

None. Every practice text in L3.01–3.18 is fully decodable from Level 1–2 code plus the Level 3 code and heart words taught up to that point — verified word-by-word with `tools/decodable.py` (`python3 tools/decodable.py course/level-3/lessons/` reports 100.0% for every lesson). The two exceptions carried by an earlier draft of this level are both resolved:

1. **`ar`/`or` words** ("park," "for," "start," "her," etc.) are no longer an exception — they are simply decodable from L3.08/3.09 onward, per the Round 1 resequence above. Before L3.08, they do not appear at all (confirmed by the checker).
2. **`for` and `her`** are now canonical Level 2 heart words (`2.01 says for`, `2.11 many any her`) — DESIGN.md was updated to add them, closing the gap an earlier draft of this level had flagged and recommended.

Every lesson's Decodability audit still narrates what was checked and fixed during drafting — kept as a trail of evidence, not because gaps remain.

## How to use a lesson

Each lesson file follows the fixed 9-step template from `DESIGN.md` §4: Warm-up → Hear it → Meet it → Blend it → Spell it → Heart word → Read it (Track A child + Track B adult) → Listen & Talk → Check. Every lesson ends with **Tutor notes** (common errors + corrections) and a **Decodability audit** (every grapheme/heart word used in the practice text, so a parent/tutor can verify nothing ungraded slipped in).

**Never cue.** If a learner is stuck on a word, the only prompt is: "Point to each part. What does it say? Blend it." Never "look at the picture" or "guess from the sentence." "Does that make sense?" is allowed only *after* the word has been decoded (DESIGN.md Rule 1).

## Fluency routine (every lesson, Step 7)

1. Tutor/audio **models** the text once, fluently.
2. Learner does **echo reading** (repeat after tutor, phrase by phrase) using the phrase-cued version (marked with `/`).
3. Learner reads it **independently** once, timed silently by the tutor (do not tell the learner they're being timed if it causes anxiety).
4. Tutor notes **WCPM** (words correct per minute) and one **prosody** observation (did they pause at commas/periods? read in phrases, not word-by-word?). Track both — never report one number as if it were the other (DESIGN.md Rule 8). There is no validated child/ESL WCPM norm table for Level 3 equivalent (~A1); use the learner's own prior lesson as the comparison point, not an external norm.

## Urdu-speaker notes used across this level

- English marks long/short vowel contrasts that Urdu does not write the same way inside a word (e.g., **ship /ɪ/ vs. sheep /iː/**, **full /ʊ/ vs. fool /uː/**) — these are separate phonemes in English that can sound like "the same vowel, just longer" to an Urdu-first ear. Practice minimal pairs explicitly at 3.15 (oo) and note the short/long vowel contrast again at 3.01–3.03 (VCe changes the vowel *sound*, not just its length).
- Urdu does not use silent letters the way English VCe does — the final "e" that is not pronounced (cape, not "ca-pe") is a genuinely new concept; name it explicitly every time: "the e is silent, it just tells the vowel to say its name."

## Files

```
README.md            this file
GAUNTLET.md           critic rounds log
lessons/L3.01-a_e.md … L3.18-mastery-check-lesson.md (18 lessons)
mastery-check.md      Level 3 exit assessment
```
