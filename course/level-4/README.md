# Level 4 — The Full Code

**Who this is for:** anyone who has completed Levels 1–3 (or placed in here via the Level 0
placement test): all single letters; digraphs (sh, ch, tch, th, wh, ng, nk); initial/final/
3-letter blends; -s/-es, -ed, -ing, -er, compound words, closed 2-syllable words; VCe (a_e,
i_e, o_e, u_e, e_e) + drop-e; open syllables (he, go, ro-bot); y as /ē/ /ī/; soft c/g + -ce
-ge -dge; **ar (3.08); or, ore (3.09)**; vowel teams ai ay, ee ea(/ē/), oa ow(/ō/) oe, igh ie,
ue ew ui(/oo/), oo (both sounds); -ild -ind -old -ost; and all Level 1–3 heart words (see list
in `mastery-check.md`). Level 4 extends ar and or/ore to multisyllabic words (4.1, 4.2) rather
than teaching them fresh — see the sequence table below.

**Anchor level:** A1/A2. **Lessons:** 16 (4.1–4.16). **Time:** 20–35 min/lesson, most
learners near-daily.

## What Level 4 covers

R-controlled vowels (ar and or/ore extended from Level 3 to multisyllabic words; er/ir/ur,
air/are/ear/eer + war/wor are new), diphthongs (oi/oy,
ou/ow), the aw/au/al(l) family, less-common vowel spellings and silent letters (ea/ĕ, kn,
wr, gn, mb), ph/gh and the two sounds of ch, consonant-le, the big Latin suffix family
(-tion, -sion, -ture, -ous, -cial/-tial), syllable division as a flexible strategy, schwa,
suffix spelling rules (1-1-1 doubling, y→i, drop-e review), the full multisyllabic word-attack
routine, and the **off-ramp**: the first authentic, non-decodable texts a learner meets, plus
a no-guessing protocol for unknown words. This is the last level built entirely from
tightly-controlled decodable text (rule 2, DESIGN.md) — Level 5 moves to wide reading.

## Exit criterion

Reads/spells multisyllabic pseudowords (e.g., *contramble*, *fenscription*) at ≥90% using
the word-attack routine, AND reads an ungraded simple authentic text (a real notice, a recipe,
a short news paragraph) applying the "stop, don't guess" unknown-word protocol correctly.
Full instrument: `mastery-check.md`.

## Sequence (master sequence — do not reorder; each lesson assumes every earlier one)

| # | Title | New pattern(s) |
|---|---|---|
| 4.1 | Cars in the Yard | ar (extended from 3.08 to multisyllabic words) |
| 4.2 | The Fork in the Road | or, ore (extended from 3.09) + war/wor quirk (new) |
| 4.3 | Her First Bird | er, ir, ur |
| 4.4 | Fair Weather, Rare Deer | air, are, ear, eer (+ war, wor) |
| 4.5 | The Noisy Boy | oi, oy |
| 4.6 | Loud Clouds, Slow Cows | ou, ow (/ow/) |
| 4.7 | Paw, Pause, and the Mall | aw, au, al(l) |
| 4.8 | Bread and Silent Letters | ea (/ĕ/), other alternates; kn, wr, gn, mb |
| 4.9 | Phones, Photos, and Ghosts | ph, ch (/k/, /sh/), gh |
| 4.10 | Little Candle, Little Table | consonant-le |
| 4.11 | A Nation's Vision | -tion, -sion, -ture, -ous, -cial/-tial |
| 4.12 | Breaking Words Apart | syllable division (VC/CV, V/CV, VC/V) + schwa |
| 4.13 | Running, Happier, Hoping | suffix spelling rules |
| 4.14 | The Word-Attack Routine | multisyllabic word attack (mark → peel → chunk → blend → flex) |
| 4.15 | Reading the Real World | off-ramp: authentic text + the no-guessing protocol |
| 4.16 | Level 4 Mastery Check | full review + the mastery instrument |

## Heart words introduced in Level 4

Level 4 leans on morphology and syllable-type decoding rather than new irregular words, so
very few new heart words are needed. **money**'s stressed first-syllable vowel is spelled "o"
but sounds like the short "uh" in *cup/come* (not schwa, technically — schwa is specifically
an *unstressed*-syllable sound, and money's first syllable is stressed — but the same "the
spelling doesn't predict the sound" idea applies) — revisited in 4.12 alongside the true schwa
concept so the learner sees both the real schwa example (**people**'s unstressed second
syllable, genuinely schwa) and this related-but-distinct irregular-vowel case side by side.
**world** is NOT a new heart word: it was already fully decodable from the **wor** pattern
taught in 4.2 (moved there from 4.4 after the ar/or/ore-into-Level-3 sequence change). No
other new heart words
are required in Level 4.

## Track A / Track B

Every decodable text in every lesson appears twice: **Track A** (child: family, pets, school,
play) and **Track B** (adult: work, money, transport, forms, health, the news) — same target
graphemes, same review words, same difficulty, never child-coded content in Track B.

## Files

```
README.md            this file
lessons/L4.01-cars-in-the-yard.md ... L4.16-mastery-check-lesson.md
mastery-check.md      standalone testing instrument (real + pseudo + multisyllabic + passage)
GAUNTLET.md           critic rounds log (Round 1 + Round 2 fixes, defect worklists)
```

## Decodability checker (`tools/decodable.py`)

Every lesson's Track A/B story text is gated by `python3 tools/decodable.py
course/level-4/lessons/` before it ships (see GAUNTLET.md for the full defect history and
current clean output). **Important scope caveat:** the checker verifies *spelling → grapheme*
parsing only — every word's letters must parse into graphemes taught so far — it has no model
of which *sound* a grapheme makes at a given word. A "100% decodable" result means every word
is *spelled* with only taught patterns; it is not an automatic guarantee that every word's
*sound* has been taught (e.g. ch=/k/ in "school"/"ache" parses fine on spelling alone well
before 4.9 actually teaches that sound — this exact class of leak was caught by hand in Round
2, not by the tool). Sound-level correctness for story text is a human review step; pseudoword
realness is checked separately against a real dictionary (`aspell`); pronunciation claims in
worked examples (e.g. "robin is short-o," "animal's unstressed vowels are schwa") are checked
against IPA transcriptions (`eng-to-ipa` and/or the CMU Pronouncing Dictionary) before
shipping — see GAUNTLET.md Round 2 builder for the process this now follows.
