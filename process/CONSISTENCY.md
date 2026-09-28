# Cross-Level Consistency Audit — Seams Between Levels

Scope: entry/exit contracts between levels, heart-word canonical lists (DESIGN.md §3 vs level
READMEs), the placement test's routing after the Level 3 18-lesson renumbering, terminology
consistency, relative-link integrity, and the root README's claims. Full within-level content
was NOT re-read (each level already passed its own gauntlet) — only READMEs, mastery-checks,
GAUNTLET.md notes, and first/last lessons.

## VERDICT: SHIP (with one open placement-test item logged for a future pass)

The seams are in materially better shape than "unchecked" implied: the Level 3 renumbering
(ar/or → 3.08/3.09) was already correctly propagated into Level 4's lesson files (L4.01/4.02
explicitly say "extended," and `course/level-4/GAUNTLET.md` documents the change) — only the
Level 4 README and the placement test's routing table had not caught up, both now fixed below.
Heart-word canonical lists match exactly across DESIGN.md §3 and the L1–L3 READMEs (24 / 29 / 16
words, exact order, exact lesson mapping). Every level-to-level entry/exit pair (L1→L2→L3→L4→
L5→L6→L7) is coherent, CEFR bands in the root README match each level's own stated band, lesson
counts match exactly, and zero relative links are broken across the whole `course/` tree and
root `README.md`.

One item (#5 below) is a real placement-test design gap from the same renumbering, but it is a
pedagogical redesign of scored test items (new pseudowords need the same IPA/rhyme rigor already
invested in Tiers 1–5), not a mechanical fix — left as "needs decision" rather than shipped
blind.

---

## Defect list

### 1. [FIXED] Placement test Block C routed `ar`/`or` to Level 4 — should be Level 3

**File:** `course/level-0/placement-test.md`, Block C scoring line (was ~line 235).
**Problem:** After the Round 1 gauntlet fix moved `ar` and `or/ore` into Level 3 (3.08–3.09),
the placement test's Block C ("Level 3/4 vowel teams + r-controlled") scoring rule still read:
*"ai/ee/igh/oa → Level 3; ar/or/ow → Level 4"*. A learner who knows every Block C grapheme
except `ar` or `or` would be routed to **Level 4**, skipping straight past the actual Level 3
content that teaches those two graphemes (3.08/3.09) — a real mis-placement, not a cosmetic
inconsistency.
**Fix applied:** Changed the routing rule to *"ai/ee/igh/oa/ar/or → Level 3, taught at
3.08–3.11; ow → Level 4, taught at 4.6"* with a pointer to DESIGN.md §3 explaining why.

### 2. [FIXED] Level 4 README entry list ("Who this is for") omitted `ar`/`or`/`ore`

**File:** `course/level-4/README.md`, opening paragraph.
**Problem:** The paragraph lists every skill a Level 4 entrant must already have, but never
mentions `ar` or `or/ore` — even though L4.01 and L4.02 explicitly open with "Review: ar (Level
3.08)" / "Review: or, ore (Level 3.09)" and assume them as prior mastery. A tutor placing a
learner directly at Level 4 (not via the placement test) using only this README would not know
`ar`/`or`/`ore` must already be solid.
**Fix applied:** Added `ar (3.08); or, ore (3.09)` to the entry list, plus one sentence noting
Level 4 extends rather than reteaches them.

### 3. [FIXED] Level 4 README "What Level 4 covers" implied `ar`/`or`/`ore` are new content

**File:** `course/level-4/README.md`, "What Level 4 covers" section.
**Problem:** Read "R-controlled vowels (ar, or/ore, er/ir/ur, air/are/ear/eer + war/wor)" as one
flat list, indistinguishable from genuinely new Level 4 graphemes — contradicting the level's
own lesson files and its GAUNTLET.md, which both correctly frame ar/or/ore as extension only.
**Fix applied:** Reworded to "(ar and or/ore extended from Level 3 to multisyllabic words;
er/ir/ur, air/are/ear/eer + war/wor are new)".

### 4. [FIXED] Level 4 sequence table didn't flag 4.1/4.2 as extensions

**File:** `course/level-4/README.md`, sequence table.
**Problem:** Table read `4.1 | Cars in the Yard | ar` / `4.2 | The Fork in the Road | or, ore`
— identical in form to every genuinely-new-content row below it, silently contradicting the
lesson files' own "(ar extended)" / "(or/ore extended + the war/wor quirk)" framing.
**Fix applied:** Row text now reads "ar (extended from 3.08 to multisyllabic words)" and
"or, ore (extended from 3.09) + war/wor quirk (new)".

### 5. [NEEDS DECISION] Placement test Tier 3/Tier 4 word banks not re-split after the L3 renumbering

**File:** `course/level-0/placement-test.md`, Stage 3 decoding ladder, Tier 3 and Tier 4.
**Problem:** Tier 3 is documented as "matches Level 3" but its real-word/pseudoword bank (cake,
time, rain, tree, boat, cute, night, happy / vope, fime, prane, gleep, doak, drute, spight,
bratny) contains **no ar/or items**, even though ar/or are now genuine Level 3 exit content
(3.08–3.09). Tier 4 ("matches Level 4") still uses `car`/`fork` as real words and pseudowords
explicitly glossed "the ar in car" / "the or in fork" (flarp, gorn) as if `ar`/`or` were Level-4
content being tested for the first time. Net effect: a learner who has mastered everything
through Level 3 including ar/or, but hasn't yet met Level 4's genuinely new r-controlled/
diphthong content, could still score full marks on Tier 4 items 1–2 by coincidence, OR — more
importantly — a learner who is shaky specifically on `ar`/`or` and clears Tier 3 (which no
longer tests them) would only be caught two tiers later than intended, and get scored as
failing *Level 4* content when the actual gap is Level 3.
**Recommended fix (not applied — requires new rigor-checked items, a content decision, not a
mechanical edit):** Move an ar/or real-word + pseudoword pair from Tier 4 into Tier 3 (so Tier 3
fully covers the current Level 3 exit standard), and replace Tier 4 items 1–2 (`flarp`/`gorn`)
with pseudowords testing genuinely new Level 4 content only (e.g., an `er/ir/ur` or `air/are`
item), preserving the existing IPA-transcription-plus-rhyme-check rigor the Round 2/3 gauntlet
passes already established for every other item. This is scoped narrowly (2 items in each of
two tiers) and should be a quick follow-up, not a full Stage 3 rebuild.

---

## Checks that passed clean (no defect)

- **Heart-word canonical lists** — DESIGN.md §3 vs `course/level-1/README.md` (24 words, exact
  order/lessons) and `course/level-2/README.md` (29 words, exact order/lessons) match exactly,
  including the Round 1 gauntlet fix note about the off-by-one-lesson bug already being resolved
  in both.
- **Entry/exit chain L1→L7** — L2 entry assumes exactly L1's exit (letters + 24 heart words);
  L3 entry ("What the learner already knows") lists L1+L2 content verbatim including both
  canonical heart-word lists; L5 entry matches L4's exit criterion (multisyllabic pseudowords,
  syllable division, schwa, ungraded text); L6 entry matches L5's exit (100+ WCPM, 2,000–3,000
  word families, complete heart-word list, A2–B1); L7 entry matches L6's exit (B1–B2, five text
  structures, reciprocal-teaching roles, paragraph summaries, lateral-reading intro) — including
  a sensible non-Level-6 fast-track clause. L6.01 (first lesson) starts at an appropriate
  difficulty for an A2–B1 entrant (intro-level Tier-2 vocabulary, no unexplained jump).
- **Lesson-count claims** — root `README.md`'s table (14/14/18/16/16/16/14) matches the actual
  file count in every `course/level-*/lessons/` directory exactly.
- **CEFR band claims** — root README's per-level bands (Pre-A1, A1, A1, A1–A2, A2–B1, B1–B2,
  C1–C2) match each level's own README/anchor statement (L4 "A1/A2", L6 "B1→B2", L7 "C1 (stretch
  C2)"; L5's own body text repeats "A2–B1").
- **Relative links** — scripted check of every `](path)` link in `course/` and root `README.md`
  (excluding `http(s)://`/`mailto:`) against the filesystem: **0 broken links**.
- **Terminology** — "Track A/Track B" used consistently L1–L6 where relevant; "Prime the topic"
  present in all 46 Level 5–7 lesson files (the L5–L7 session template component from DESIGN.md
  §3); "sittings" (L1's own micro-session unit, since single letters take under a full lesson)
  vs. "session" (L5–L7's 30–45 min unit) is an intentional, documented distinction, not drift.

## Counts

- **Found:** 5
- **Fixed:** 4 (mechanical — routing text, entry-list omission, two wording/table clarifications)
- **Needs decision → FIXED by lead (items moved Tier 4→3; blaud/hable added):** 1 (placement-test Tier 3/4 item redesign — pedagogical, needs new
  rigor-checked pseudowords, not a text edit)
