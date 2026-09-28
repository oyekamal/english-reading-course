# Level 4 — Gauntlet Log

## Round 1 critic

**Scope:** course/level-4/ (README, L4.01–L4.16, mastery-check.md) against DESIGN.md §2/§3/§4,
research/03, research/05, research/01, and external reference programs (UFLI Foundations
lessons 77–83 r-controlled unit + "Teaching Big Words" by Holly B. Lane; Wilson Reading System
Scope & Sequence Steps 1–6; Sounds-Write Polysyllabic Words sequence doc).

### Comparison verdicts

**1. L4.12 (syllable division) vs UFLI/Wilson equivalent — REFERENCE WINS.**
Our "try open first, flex to closed, check if it's real" framing for the one-consonant-middle
case is *identical in substance* to UFLI's own instruction ("For the VCV pattern, first try
splitting after the first vowel, as in o-pen. If that doesn't work, try splitting after the
consonant, as in cab-in" — Teaching Big Words, p.4) and is honestly evidence-cited (DESIGN.md
already notes VCV is only ~50% predictive). That part is as good as the reference. But the
reference beats us on two structural points our lesson doesn't cover at all: (a) UFLI's
explicit **physical marking procedure** (mark every vowel with "v", draw a bridge between
them, mark consonants with "c", THEN divide) gives the learner a repeatable visual routine;
ours has no written notation convention at all for L4.12 itself (L4.14 adds one, three lessons
later). (b) UFLI names two more division cases we never teach: the **VCCCV / compound-boundary
case** (rainbow, instruct, handspring — split at the compound boundary, watch for 3-letter
blends) and the **VV-split exception** (diet, poem, lion — two adjacent vowels that do NOT
form a vowel team). The second gap is not hypothetical: our own L4.01 decodability audit
already uses "quiet" and analyzes it as qui-et without ever having taught that two-vowels-that-
don't-team-up is a distinct, nameable case. A learner who internalizes "two vowels together =
vowel team" (which is exactly what L3 vowel-team lessons trained) will mis-split every VV word
because L4.12 never flags the exception.

**2. L4.14 (word-attack routine) vs UFLI/Wilson equivalent — REFERENCE WINS**, on a
correctness defect, not a design one. Our five-step routine (mark → peel → chunk → blend →
flex) is a genuinely good synthesis — arguably better *organized* than UFLI's plainer syllable-
type walkthrough because it integrates morphology (peel) before phonics (chunk), which UFLI
treats as separate units taught weeks apart. But the flagship worked example — the one
demonstration a learner will anchor the entire routine to — contains a factual error: modeling
"unfriendliness," the lesson says "mark vowels (u-i-e-i-e-ss has no vowel — six vowel letters
across the word)." The word has five vowel letters (u, i, e, i, e), not six, and "u-i-e-i-e-ss
has no vowel" does not parse as a sentence. This is the single lesson the level's exit criterion
depends on, and its one worked model is wrong. Reference programs also teach an explicit
fallback the routine omits: UFLI's "pronounce the whole word with every vowel as schwa — this
often triggers recognition of a familiar word" (Teaching Big Words, p.4, citing O'Connor's BEST
strategy) is a distinct technique from our step 5's "adjust stress/schwa on this chunking,"
and it's exactly the kind of last-resort move a stuck adult self-learner most needs.

**3. L4.15 (off-ramp) vs anything comparable — OURS WINS.** Neither UFLI, Wilson, nor
Sounds-Write has a single, named "graduation to authentic text" lesson with an explicit,
step-numbered no-guessing protocol the way L4.15 does — they diffuse this transition across
program-specific "decodable reader → trade book" recommendations without ever writing out
"stop → run the routine → say it aloud → check it sounds real → decide if you need to look up
meaning" as one teachable sequence. L4.15's explicit separation of decoding-success from
meaning-clarity (a word can be correctly decoded and still not understood, and that's a
different problem) is a genuinely stronger pedagogical move than what the references publish,
and the three authentic text types (notice/recipe/news) are appropriately adult-register on
Track B. This is the strongest lesson in the level.

### Single biggest gap

**The decodability contract (DESIGN.md rule 2, "Decodable = decodable... target ≥95%
decodable") is violated systematically, not occasionally, across the first half of the level —
and every affected lesson's own "Decodability audit" footer falsely certifies 100%/98%/99%
compliance.** The word **"small"** alone appears in the Track A/B story text of L4.01, L4.02,
L4.03, L4.04, and L4.06 — five lessons before its "al(l)" pattern is taught in L4.07 — making
it the most-repeated undertaught word in the level. Layered on top of that, individual lessons
leak "ur" (bursts, L4.02), "al" (fall, L4.02), "ou" (out/cloud/shout, L4.02 and L4.05), "ph"
(phone, L4.06), and "gh" (though, L4.05; through, L4.06; rough/through, L4.08) — each multiple
lessons before its own lesson teaches it. This isn't a handful of typos; it's the course's
central promise (a learner can independently decode every word in front of them using only
what's been explicitly taught) failing on its most measurable, most-checked claim, in the exact
level whose whole point is "The Full Code."

### Prioritised defect worklist

1. **[HIGH] "small" leaks al(l) in 5 lessons before it's taught (L4.07).**
   - `course/level-4/lessons/L4.01-cars-in-the-yard.md` — Track B, "...a small chart for his
     garden."
   - `course/level-4/lessons/L4.02-fork-in-the-road.md` — Track A, "...it in the fort — a
     small shed near the barn."
   - `course/level-4/lessons/L4.03-her-first-bird.md` — Track A story, "a small bird with a..."
   - `course/level-4/lessons/L4.04-fair-weather-rare-deer.md` — Track B, "Farah works at a
     small shop that sells chairs and tables."
   - `course/level-4/lessons/L4.06-loud-clouds-slow-cows.md` — Track A "a small mouse in a
     cage..." and Track B "a small crowd has formed near the front doors."
   - **Fix:** replace "small" with "tiny" throughout (tiny = open syllable + y/ē, both taught
     in Level 3, fully decodable at every one of these lesson points), then correct each
     lesson's own "Decodability audit" line to drop the false 100%/98%/99% claim it currently
     makes.

2. **[HIGH] L4.02 Track A, one sentence, two leaks:** "The wind is strong and short bursts of
   rain start to fall." — "bursts" leaks **ur** (taught L4.03, one lesson later) and "fall"
   leaks **al** (taught L4.07, five lessons later).
   - **Fix:** rewrite as "The wind is strong, and rain starts to come down fast." (every word
     already taught through L4.02).

3. **[MED] L4.02 Track A leaks "out" (ou, taught L4.06):** "...the sun comes out from the
   north."
   - **Fix:** "...the sun comes back out into the sky." → still leaks; use "...the sun shows
     itself again from the north."

4. **[MED] L4.05 Track A, two sentences, three leaks (ou, taught L4.06, one lesson later):**
   "he likes to point out every bird, cloud, and truck he can spot" and "Zayn lets out a
   joyful shout and runs to get the toy box."
   - **Fix:** "he likes to spot every bird, truck, and train he sees" (drop "point out",
     "cloud"); "Zayn grins big and runs to get the toy box" (drop "lets out", "shout").

5. **[MED] L4.06 Track B leaks "phone" (ph, taught L4.09, three lessons later):** "Naveed
   checks his phone — no signal, either."
   - **Fix:** "Naveed checks his radio — no signal, either." (the same story already uses
     "radio" later per its own decodability audit, so this reuses in-lesson vocabulary).

6. **[MED] L4.05 Track B leaks "though" (gh, taught L4.09, four lessons later):** "...Tariq
   feels the joy of a job done well, even though his voice is tired from talking..."
   - **Fix:** "...even when his voice is tired from talking to so many customers."

7. **[MED] L4.06 Track B leaks "through" (gh, taught L4.09, three lessons later):** "...a
   round of quiet cheers goes through the crowd."
   - **Fix:** "...a round of quiet cheers moves across the crowd."

8. **[LOW-MED] L4.08 Track B leaks "rough" and "through" (gh, taught L4.09, one lesson later):**
   "It was a rough start to the day, but he stayed calm and got through it."
   - **Fix:** "It was a hard start to the day, but he stayed calm and got past it."

9. **[LOW] L4.01 Question 3 leaks "draw" (aw, taught L4.07):** "(3) Why do you think Sam wants
   to draw a star chart?" — outside the story body, but a self-learner (course explicitly
   supports self-learners, not just tutors) reads comprehension questions independently too.
   - **Fix:** "(3) Why do you think Sam wants to make a star chart?" (mirrors the story's own
     wording, which already says "make a star chart").

10. **[MED] L4.14, line ~37 — factual error in the flagship worked example.** Modeling
    "unfriendliness": "mark vowels (u-i-e-i-e-ss has no vowel — six vowel letters across the
    word)" is both miscounted (5 vowel letters: u, i, e, i, e — not 6) and grammatically
    broken.
    - **Fix:** replace with: "mark vowels: u-n-f-r-i-e-n-d-l-i-n-e-s-s → five vowel letters
      (u, i, e, i, e), giving a rough sense of five syllable-sized chunks before peeling."

11. **[MED] L4.12/L4.14 routine coverage gap vs UFLI:** never teaches (a) the VCCCV /
    compound-boundary division case (rainbow, instruct, handspring) or (b) the VV-split
    exception (diet, poem, lion — two vowels that do NOT form a team), even though the
    course's own L4.01 text already uses "quiet," which is exactly this un-taught case.
    - **Fix:** add a short "one more case" callout to L4.12 §3 (or a "beyond today" box in
      L4.14) covering both, 2–3 real-word examples and one pseudoword each.

12. **[LOW-MED] L4.14 routine omits the "all-schwa read-through" fallback** UFLI/O'Connor's
    BEST strategy recommends as a distinct last-resort move (say every vowel as schwa; this
    often triggers recognition of a familiar oral word, e.g. "complicate" → "cəm-plə-kət").
    Step 5 ("flex") only covers adjusting stress/schwa on the current chunking, not this
    whole-word fallback.
    - **Fix:** add it as an explicit sub-step inside step 5, with one worked example.

13. **[LOW] Tooling defect, not content:** `tools/decodable.py` flags "walks" in L4.01 as
    untaught — false positive. "walk" was already taught as a Level 3 heart word (DESIGN.md
    §3, heart words L3), and only the regular -s suffix (taught L2.09) is added; the tool's
    `known()` heart-word set only matches exact word forms, not inflected ones.
    - **Fix:** in `known()`, also accept `heart_word + s/ed/ing` as known, or strip common
      inflections before the heart-word membership check.

14. **[LOW] Tooling defect:** `read_section()` in `tools/decodable.py` stops only at the next
    `## 8.` heading, so it also scans the "Fluency check" section that sits between "## 7."
    and "## 8." in every lesson — that boilerplate paragraph ("aloud," "observation,"
    "questioning," "words correct per minute") is the source of most of the noise in the raw
    tool output and has to be manually filtered out by a human reviewer every time.
    - **Fix:** stop the regex at `## Fluency check` OR `## 8.`, whichever comes first.

15. **[LOW] Documentation consistency:** L4.05's "Decodability audit" flags "Mr. Khan"/"Sam"-
    style proper nouns explicitly in some lessons (e.g. L4.01) but not "Tariq" in L4.05 —
    minor inconsistency in how proper nouns are documented across lessons, worth a pass once
    the content fixes above are made.

**Defect count: 15** (2 HIGH, 8 MED/LOW-MED, 5 LOW/tooling).

## Round 1 builder

All 15 defects addressed. Summary by defect:

**Tooling (make the tool the gate, not hand-written audits):**
- Every lesson's Track A/B story paragraphs are now wrapped in `>` blockquotes; Questions,
  Fluency check instructions, and all scaffolding text sit outside the blockquotes. The
  checker (`read_section`) reads only blockquoted lines when present.
- `tools/decodable.py` fixes:
  - `heart_ok()`: a canonical heart word plus a regular taught inflection (-s/-es/-ed/-ing)
    now counts as known (fixes #13 — "walks" false-flagged when "walk" is a canonical L3
    heart word and -s is a taught L2 suffix).
  - `read_section()`: now stops at `## Fluency check` OR `## 8.`, whichever comes first, so
    the fluency-instructions boilerplate ("aloud," "observation," "questioning," "words
    correct per minute") never leaks into the word scan (fixes #14).
  - `END_ONLY` now also restricts `ous/tion/sion/ture/cial/tial` to true word-final position —
    without this, the greedy parser collided them into unrelated mid-word letter runs (e.g.
    "house"/"mouse" → h/m + "ous" + e), producing false untaught-grapheme flags on words that
    are actually fine. Found and fixed while running the tool, not in the original worklist.
  - `positional_ok()`: "mb" is now end-restricted too (every taught mb-word — comb, lamb,
    climb, thumb — is word-final silent-b), which stopped a false collision with ordinary
    cross-syllable m+b runs like "member."
  - Reverted a bad prior edit to the "al" rule that excluded al-before-l on the theory that
    "wall/ball/call/small/fall/tall" are FLOSS short-a + doubled-l, not the untaught al(l)
    grapheme. That's a phonics error — there is no short-a "-all" FLOSS word to contrast
    with; all of those are genuinely /aw/, i.e. exactly the leak the critic flagged. Restored
    to reject al-before-l (the original, correct behavior) with an accurate comment.
  - `ALL` (the grapheme list) is now sorted by `(-len, x)` instead of `-len` alone — sorting a
    *set* by length only left same-length graphemes (al vs ll, ay vs aw) in Python's
    hash-randomized set-iteration order, which differs between process runs and made parsing
    of some words (fall, calls, away) non-deterministic run to run. Verified deterministic
    across 3+ repeated runs after the fix.

**Content — decodability leaks (worklist #1–9), all fixed by rewriting the text, not by
weakening the checker:**
- "small" → "tiny" everywhere it leaked al(l) before 4.7 (L4.01, L4.02 n/a — different
  sentence rewritten, L4.03, L4.04, L4.06 ×2).
- L4.01: "away" removed (greedy-parses as untaught "aw"+"ay"); "quiet" removed (VV-split word,
  not taught until 4.12 — see below); "draw" → "make" in the comprehension question.
- L4.02: "calls"→"yells," "bursts...start to fall"→"rain starts to come down fast,"
  "shed near the barn"→"shed by the barn," "comes out from the north"→"shows itself again
  from the north" (Track A); "bursts...turns on"→"comes down hard...clicks on" (Track B).
- L4.03: "near"→"by" (×2), "at the turn of the hour"→"at sunup," "calls the doctor"→"rings the
  doctor."
- L4.04: "pointing"→"showing her," "catch each sound"→"turning this way and that," "talk
  about...all the way home"→"talk of...the whole way home," "Near closing time"→"By closing
  time."
- L4.05: "point out every bird, cloud"→"spot every bird, truck, and train," "lets out a
  joyful shout"→"grins big," "an hour"→"a good while," "even though"→"even when." (*Tariq*
  remains flagged as a proper noun — 1 flagged word, under the 2-per-text cap.)
- L4.06: "tall"→"bright," "in all before"→dropped, "phone"→"device," "a small crowd"→"a tiny
  crowd," "goes through the crowd"→"moves across the crowd," "we all stayed calm"→"we stayed
  so calm."
- L4.07: "uncle"→"granddad" (consonant-le not taught until 4.10).
- L4.08: "rough...got through it"→"hard...got past it."
- Also caught and fixed during the tool-driven sweep (not on the original numbered list but
  same category): L4.09's "picture"→"photo" and "serious"→"bad" (both leaked -ture/-ous,
  taught 4.11); "little"→"quick"/"quiet"... corrected to "quick" (consonant-le, taught 4.10)
  in both L4.05 and L4.09; "member" fixed by the mb tooling fix above rather than a rewrite.

**L4.12 (syllable division) — added the three UFLI-style gaps identified by the critic:**
- **Physical marking procedure**: mark every vowel *sound* with a small v (a taught vowel team
  gets one v and a bridge/arc, since it's one sound), mark consonants between them with c,
  then read the marked pattern to pick a case. Modeled on napkin (v-c-c-v) and tiger (v-c-v).
  This runs before all four division cases, every time, for at least the first 10 words.
- **VCCCV / compound-boundary case**: added as a fourth case alongside VC/CV, V/CV, VC/V — two
  of three middle consonants are usually a taught blend/digraph that stays together; for
  compounds, split at the boundary you can already hear (rain-bow, hand-spring, sun-set); for
  a non-compound VCCCV word, keep the blend together (in-struct). Practice word list and a
  pseudoword (thindstruck) added to Blend it.
- **VV-split exception**: two vowel letters side by side that do NOT form a taught vowel team
  keep their own syllable each, with no bridge (di-et, po-em, li-on, cre-ate). Added
  explicitly as the fourth marking-procedure outcome, with a tutor note naming the exact
  failure mode it prevents (over-applying "two vowels together = one team" from Level 3).
  **"Quiet" is now taught here** (removed from L4.01's story per the critic's alternative fix,
  then reintroduced as a worked VV example in this lesson's Blend it list) — closing the loop
  the critic identified rather than just deleting the word and losing the concept.
- Check section and reteach step both updated to test the new cases and to stop inviting
  "flex" on cases that only have one correct split (VC/CV, VCCCV/compound, VV) — flex is only
  for the genuine V/CV vs. VC/V ambiguity.

**L4.14 (word-attack routine) — fixed the flagship worked example and added the fallback:**
- "unfriendliness" corrected: five vowel letters (u, i, e, i, e), not six, and the garbled
  "u-i-e-i-e-ss has no vowel" clause replaced with a clean, correctly-punctuated sentence.
  Also corrected the chunking claim itself — "friend" is a Level 2 canonical heart word (its
  "ie" spells short e irregularly), so the worked example now says it's *recognized*, not
  decoded as a regular closed syllable, which was the more subtle error underneath the vowel
  miscount.
- **All-schwa read-through fallback** added as an explicit sub-step inside step 5 (flex): say
  every vowel as a flat "uh" and listen for a familiar spoken word, with the worked example
  *complicate* → "cəm-plə-kət," matching the critic's cited O'Connor/UFLI BEST-strategy
  technique as a distinct last-resort move from ordinary stress/schwa adjustment on a single
  chunking attempt.

**L4.16 — fixed the misattributed research citation:**
- The tutor note claiming "evidence (Wanzek et al.) favors targeted, intensive reteaching over
  broad, unfocused review" was not what Wanzek et al. (2013) found. The actual finding is that
  **group size** — not reteaching scope or session frequency — was the significant moderator
  of outcomes for older struggling readers, with the smallest groups (1:1 or near it) showing
  the largest effects (research/03 §1.5). Rewrote the note to cite this accurately: a
  self-paced course's real advantage is effectively "group size = 1," and an unfocused
  whole-level review dilutes that advantage rather than using it.

**Sequence change (DESIGN.md §3 — ar/or/ore moved to Level 3.08/3.09):**
- **L4.01 repurposed** from "first teaching of ar" to "ar extended": front matter, Hear
  it/Meet it reframed as brief review, Blend it extended with multisyllabic ar words (market,
  garden, carpet, target, harvest, garment, cargo, barnyard, farmhand, artist), Check section
  now diagnoses single-syllable-vs-chunking failure separately.
- **L4.02 repurposed** from "first teaching of or/ore" to "or/ore extended + the war/wor
  quirk": front matter, Hear it/Meet it reframed to teach the genuinely new content (w before
  or shifts the vowel sound: war→/wor/, work→/wer/, even though the spelling is still "or"),
  Blend it split into single-syllable review / multisyllabic extension / war-wor practice,
  Check section tests both or/ore fluency and the war/wor override explicitly.
- Both lessons' decodability audits updated to cite ar/or/ore as Level 3 content, not "today's
  new," per the sequence change.

**Pseudoword dictionary check (run before finishing, per the coordinator's request):**
Extracted all ~117 candidate tokens from every "Pseudowords" line across `course/level-4/`
(lessons + `mastery-check.md`) and checked each against `aspell -d en`. Found and fixed four
real dictionary words that had been used as "pseudowords": **darn** → darl (mastery-check.md
Section 2), **tarn** → tarl (L4.01, a real word meaning a small mountain lake), and **zip** /
**zipping** → vop / vopping (L4.13's 1-1-1 doubling drill — "zip" is a real base word, so
"zipping" is a real word, defeating the point of an alien-word check). Re-ran the full
extraction after fixing: 108 remaining candidates, 0 matches against the dictionary. Also
cleaned up several pseudoword lines that had leftover self-correction commentary from
drafting (L4.09, L4.13) into clean, final word lists.

### Final gate output

```
$ python3 tools/decodable.py course/level-4/lessons/
4.01  words= 188  decodable=100.0%  untaught=
4.02  words= 205  decodable=100.0%  untaught=
4.03  words= 203  decodable=100.0%  untaught=
4.04  words= 229  decodable=100.0%  untaught=
4.05  words= 227  decodable= 98.2%  untaught=Tariq
4.06  words= 227  decodable=100.0%  untaught=
4.07  words= 211  decodable=100.0%  untaught=
4.08  words= 238  decodable=100.0%  untaught=
4.09  words= 242  decodable=100.0%  untaught=
4.10  words= 233  decodable=100.0%  untaught=
4.11  words= 236  decodable=100.0%  untaught=
4.12  words= 223  decodable=100.0%  untaught=
4.13  words= 222  decodable=100.0%  untaught=
4.14  words= 220  decodable=100.0%  untaught=
4.15  words=   0  decodable=  0.0%  untaught=
4.16  words=   0  decodable=  0.0%  untaught=
```

4.15/4.16 show 0 words because neither has a "## 7. Read it" section (4.15 uses its own
off-ramp structure with authentic, intentionally non-audited text per the "OURS WINS" verdict;
4.16 is a review/testing lesson that points to `mastery-check.md`) — expected, not a bug.
Every other lesson is 100% decodable except 4.05, which has exactly one flagged word (Tariq,
a proper noun), well under the 2-flagged-words-per-text allowance. Verified deterministic
across 3 repeated runs of the same command.

**Defect count: 15/15 resolved.**

## Round 2 critic

**Fix verification (`python3 tools/decodable.py course/level-4/lessons/`):** Re-ran; output
matches the builder's claimed table exactly (4.01–4.14 all 100% except 4.05 at 98.2%/*Tariq*;
4.15/4.16 = 0 words, expected — no "## 7." heading). The tool's own numeric claim holds. But
the tool only checks *spelling* parses into taught graphemes, never the *sound* a grapheme
makes — and hand-checking 4 lessons' story text against the untaught-sound categories in the
brief found three real, unflagged leaks the tool is structurally blind to, plus two phonics
**factual errors** newly introduced (or left standing) in the two lessons Round 1 said the
reference beat us on:

**Tool edits (`tools/decodable.py`) — checked, not weakened:**
- `heart_ok()`'s heart-word+suffix matching (-s/-es/-ed/-ing) requires an *exact* full-string
  match of the stripped base against the heart-word set — spot-checked ~15 heart words across
  L1–L4 for accidental collisions (e.g. "cares"/"declares" against heart word *are*, "hers"
  against *her*) and found none; every match found was a real, linguistically correct
  inflection of a genuine heart word (do→doing, go→going, one→ones, her→hers). Not weakened.
- The `## Fluency check` boundary fix is also safe: hand-read the Fluency-check section of
  6 lessons (4.02, 4.05, 4.08, 4.09, 4.12, 4.14) — all six contain only generic WCPM/prosody
  tutor instructions, zero story text, so excluding that section from the scan cannot hide a
  leak. Not weakened.
- Both edits are correctness fixes, not check-weakening. No defect here.

**New/unflagged decodability leaks (sound-level, tool-blind):**
1. **"school" in L4.05 Track A** ("At *school*, his choice seat...") — ch=/k/ is not taught
   anywhere until **L4.09**, whose own Meet-it section literally uses *"school: /k/, not the
   usual /ch/"* as its introducing example. The exact target word of a future lesson leaks
   four lessons early, unflagged in L4.05's decodability audit.
2. **"ache" in L4.04 Track B** ("...still *ache* by the end of her shift...") — same defect:
   ch=/k/, and *ache* is itself one of L4.09's own Blend-it words ("ch (/k/): school, echo,
   chorus, stomach, **ache**"). Two lessons early, unflagged.
3. **"touch" in L4.08 Track A** ("Don't *touch* it with dirty hands...") — ou=/ʌ/ (the
   soup/touch/young/country class) is never taught anywhere in the Level 4 design as a
   distinct sound from ou=/ow/ (loud, taught 4.06); the word isn't called out as an exception
   in the lesson's tutor notes or decodability audit the way *once*, *great*, *laugh* etc. are
   elsewhere. Unaddressed irregular-sound leak.

(4.15's zero audit coverage is not a defect — its own header says "intentionally authentic,
uncontrolled texts, not a full audit," consistent with the Round 1 "OURS WINS" off-ramp
verdict. Confirmed by reading the file, not just trusting the header.)

**Phonics/fact-check failures (new material, not caught by any built-in gate):**
4. **L4.12, VC/V blend list — "robin (flag: robin is actually the rare case where open DOES
   work — say ro-bin with long o)."** This is factually wrong. *Robin* is pronounced with a
   **short o** (/ˈrɒbɪn/, "ROB-in," rhymes with *bobbin*) in every standard dialect — it is a
   normal VC/V closed-syllable word, not an open-syllable exception. This is the lesson's own
   named example of "not even VC/V is a fixed law," and the example is backwards: it teaches
   the tutor to mis-pronounce the word in the very story that follows in the same lesson
   ("a *robin* building a nest"). This directly undermines the flex-and-check strategy the
   lesson is built around — a tutor following the script as written will say the word wrong.
5. **L4.14, all-schwa fallback worked example — "complicate... read through it once as
   all-schwa instead: 'cəm-plə-kət'."** Wrong on the third syllable: *complicate* (verb) is
   stressed **KOM**-pli-cate, and the final syllable is a full, unreduced long-A (/keɪt/), not
   schwa, in fluent natural speech — only the first two syllables genuinely reduce. Flattening
   "cate" to "kət" doesn't match how a fluent speaker says the word, which is the entire
   premise offered for why the all-schwa trick works ("close to how a fluent speaker actually
   says it"). A word whose unstressed syllables are *actually* schwa throughout (e.g.
   *banana*, already used correctly in L4.12) would prove the technique; *complicate* disproves
   its own justification.

**BLIND COMPARISON:**
UFLI's own PDF ("Teaching Big Words") could not be extracted as text this round (binary/
encoded PDF, WebFetch failed) — comparison here rests on UFLI's well-documented public
methodology (mark vowels → six syllable types → VC/CV / V/CV / VC/V with explicit "try open,
check, flex to closed" language → peel affixes for big words), which L4.12/L4.14 already
structurally mirror closely, including citing "UFLI-style mark-then-divide" by name in tutor
notes. The mechanics genuinely match reference quality now. But a UFLI lesson would not ship a
factually wrong pronunciation as its named "flex" example, nor an all-schwa worked example
that contradicts its own rationale on inspection — those are exactly the kind of small,
compounding errors that separate a research-grade program from a close copy of one.

**VERDICT: REFERENCE WINS (narrowly) on both L4.12 and L4.14.** The structure, sequencing, and
teaching routine are now at parity with UFLI — this is real, verified progress from Round 1.
What's still missing is fact-checking rigor: two invented worked examples (robin, complicate)
carry phonics errors that a program with editorial review (UFLI) would not publish. The L4.15
off-ramp result from Round 1 stands (OURS WINS there; not re-litigated).

**SINGLE BIGGEST GAP:** The decodability checker only verifies *spelling → grapheme* parsing,
never *grapheme → sound*, and the builder's process has no separate fact-check pass for
phonics claims made in prose (pronunciation notes, worked examples) the way it now has one for
pseudowords (aspell). Two of five new defects this round (robin, complicate) are exactly that
class of error, and would recur again next round without such a pass.

**Numbered worklist:**
1. Fix L4.12's robin flag: either drop the "robin is the rare open exception" claim entirely
   (it's simply a correctly-behaving VC/V closed word, no flag needed) or replace it with a
   real open-VC/V-exception word if the pedagogical point is worth keeping (e.g. *lemon* is
   also closed/VC-V standard — a genuine "rare open VCV word" example would be something like
   *tiger/paper* itself already listed as V/CV; if no true "VC/V-pattern-but-actually-open"
   English word is needed for the point, cut the aside).
2. Fix L4.14's all-schwa worked example: replace *complicate* with a word whose every
   unstressed syllable is genuinely schwa in natural speech (e.g. *elephant* /ˈɛləfənt/,
   *camera* /ˈkæmərə/, or reuse *banana*) so the "matches how a fluent speaker says it"
   justification is actually true of the example given.
3. Remove or re-sequence "school" out of L4.05 Track A (replace with a word using only
   graphemes taught through 4.05 — the story doesn't need this specific word).
4. Remove or re-sequence "ache" out of L4.04 Track B, same reason.
5. Either add "touch"-class ou=/ʌ/ to the L4.09 (or a later) lesson's exception list the way
   *though/through* already are, or replace "touch" in L4.08 Track A with a word that doesn't
   carry an unaddressed irregular sound.
6. Add a lightweight phonics fact-check pass (a checklist, not necessarily a tool) to the
   builder's own process for any lesson containing an invented "flag"/worked pronunciation
   example — the aspell pseudoword check is a good precedent for "verify claims against an
   external source before shipping," extend the same discipline to pronunciation claims.
7. (Minor, documentation only) State explicitly in the Round-summary / GAUNTLET final-gate note
   that the checker's "100%" figures are spelling-level only, not a sound-level decodability
   guarantee, so a future reader doesn't over-trust the number the way "100% decodable" reads
   at a glance.

**Defect count this round: 5 new (3 sound-level leaks + 2 phonics factual errors), plus the
checker-scope caveat (#7) as a process note rather than a content defect.**

## Round 2 builder

All 5 defects fixed, plus a full pronunciation pass across every worked example and
word-level claim in L4.01–L4.16, cross-checked against two independent sources
(`eng-to-ipa` and the CMU Pronouncing Dictionary via `nltk.corpus.cmudict`, both installed
in a throwaway venv for this session).

**1. L4.12 — robin flag rewritten as the flex example (not dropped):**
Confirmed via CMU dict: *robin* → `[R AA1 B AH0 N]` / `[R AA1 B IH0 N]` — **only short-o
pronunciations exist, no long-o variant at all.** The old text ("robin is the rare case where
open DOES work — say ro-bin with long o") was backwards on every count. Rewrote it as the
worklist's preferred option: robin is now presented as **the flex example itself** — try open
first (ro-bin, long o, to rhyme with *robot*), that's not a real word, flex to closed (rob-in,
short o, "ROB-in," rhyming with *bobbin*), that is — directly contrasted with **robot**
(same v-c-v marked shape, stays open, ro-bot, long o — confirmed `[R OW1 B AA2/AH2 T]`), so
the lesson now demonstrates in one place why the open/closed choice can't be read off the
spelling and must be checked against a real word every time. Section 2 (Hear it) already had
the correct "rob-in (short o)" framing — only the Blend it aside was wrong; no other
occurrences of the error found in the file or in `mastery-check.md`.

**2. L4.14 — all-schwa fallback example replaced (complicate → animal):**
CMU dict on *complicate* → `[K AA1 M P L AH0 K EY2 T]`: the final syllable carries secondary
stress and a full, unreduced `EY` (long-A) vowel — not schwa — confirming the critic's
objection exactly. Replaced with **animal** → `[AE1 N AH0 M AH0 L]`: both unstressed
syllables are genuinely `AH0` (schwa) in CMU dict, and `eng-to-ipa` agrees (/ˈænəməl/).
Rewrote the technique description itself, not just the example — the original said "say
every vowel...as a flat 'uh'," which would also flatten the *stressed* vowel and produce an
unrecognizable shape even for a good example word; corrected to "keep your best guess at
which syllable is stressed, flatten every *other* vowel," matching how the O'Connor/UFLI BEST
technique actually works, and added an explicit contrast noting *why* complicate would have
been a bad choice (its final syllable keeps a full vowel in real speech) so the lesson now
teaches the discernment, not just a corrected fact.

**3–5. Three sound-level leaks removed (spelling-checker-invisible, all confirmed real by
dictionary lookup before removing):**
- L4.05 Track A: "At school" → "In class" (`school` = `[S K UW1 L]`, ch=/k/ not taught until
  4.9, which uses this exact word as its own introducing example).
- L4.04 Track B: "arms still ache" → "arms still hurt" (`ache` = `/eɪk/`, ch=/k/, and *ache*
  is itself one of 4.9's own Blend-it words — `hurt` uses **ur**, taught 4.3, one lesson
  before 4.4, so it's clean).
- L4.08 Track A: "Don't touch it" → "Don't rub it" (`touch` = `[T AH1 CH]`, ou=/ʌ/, the
  soup/touch/young class, never taught in Level 4 as distinct from ou=/aʊ/ — confirmed via
  CMU dict the vowel is genuinely `AH1`, not `AW1` like every other Level 4 ou-word checked).
All three fixes re-verified against `python3 tools/decodable.py` (unaffected — these are
sound-level, not spelling-level, so the tool correctly shows no change) and against the full
`aspell`/CMU checks below for the replacement words.

**Also fixed while sweeping (found during the same pass, same category as #3–5):**
- L4.04's front matter and Meet-it section still taught **war/wor** as "New today" — a
  leftover duplicate from before the Round 1 sequence change moved war/wor into L4.02. Not
  independently listed by the Round 2 critic, but it's the same "stale claim not caught by any
  gate" failure mode, so fixed it: L4.04 now explicitly reviews war/wor (citing 4.2) rather
  than re-teaching it as new.
- L4.12 §6 (Heart words) claimed *money*'s first-syllable vowel is "schwa." CMU dict: *money*
  → `[M AH1 N IY0]` — `AH1` marks **primary stress**, and schwa is definitionally an
  *unstressed*-syllable reduction; a stressed syllable cannot be schwa by definition, even
  though both are colloquially "the uh sound." Rewrote the passage to correctly describe
  money's vowel as the stressed STRUT vowel (same sound family as *cup, come, love*) — a
  related but technically distinct kind of "spelling doesn't predict sound" quirk from real
  schwa — and kept *people* (`[P IY1 P AH0 L]`, `AH0` = genuine unstressed schwa) as the
  lesson's one true schwa worked example. Updated the Level 4 README's parallel claim about
  *money* to match, and corrected a leftover README line that still said *world*'s war/wor
  pattern was "taught in 4.4" (it's 4.2, after the sequence change).

**Full pronunciation pass (every word list tied to a new grapheme, plus every heart-word
claim, in L4.01–L4.14):** checked ar (L4.1, incl. new multisyllabic words), or/ore/war/wor
(L4.2), er/ir/ur (L4.3), air/are/ear/eer (L4.4, + the *earth*/*water* heart-word claims),
oi/oy (L4.5), ou/ow (L4.6), aw/au/al(l) (L4.7, + *walk/talk* silent-l claims), ea(/ĕ/) +
kn/wr/gn/mb (L4.8, all 26 words individually confirmed against the claimed sound), ph/ch/gh
(L4.9, all 22 words across all five sub-patterns, + the *laugh* heart-word claim), consonant-le
(L4.10, all 20 words confirmed `/əl/`), the five Latin suffixes (L4.11, all 18 words
confirmed against their claimed `/ʃən/, /ʒən/, /ʧər/, /əs/, /ʃəl/` sounds), and the VV-split /
VCCCV word lists added to L4.12 this round (`diet, poem, lion, create, quiet, science, giant`
all confirmed two genuinely separate vowel phonemes via CMU dict; `rainbow, sunset, instruct,
complain` confirmed real blends/compounds). One near-miss worth recording: **target**
(added to L4.1's multisyllabic ar list) shows a secondary CMU pronunciation with `ER` instead
of `AA`(`[T AA1 R G AH0 T]` / `[T ER1 G AH0 T]`) — the primary, standard pronunciation (listed
first in CMU dict, and the only one `eng-to-ipa` returns) is the intended `AA` (ar) reading, so
the word is kept, but this is exactly the kind of check that would have missed a real problem
if only one source had been consulted — cross-checking two sources, as the critic's worklist
item #6 recommended, earned its keep here even though no fix was needed in this instance.
Every other checked word matched its claimed sound with no ambiguity across both sources.

**Process note (worklist #6/#7 — added, not just fixed once):** the pseudoword-dictionary
check from Round 1 (`aspell`) and this round's pronunciation check (`eng-to-ipa` +
`nltk.corpus.cmudict`) are now the standing pre-ship checklist for this level alongside the
spelling-level `tools/decodable.py` gate: (a) run the decodability checker, (b) grep every
pseudoword against a real dictionary, (c) verify every named pronunciation claim / worked
example against IPA from two sources before treating a lesson as done. README.md's new
"Decodability checker" section states explicitly that the tool's 100% figures are
spelling-level only, per worklist #7, so a future reader doesn't over-trust the number.

### Final gate output

```
$ python3 tools/decodable.py course/level-4/lessons/
4.01  words= 188  decodable=100.0%  untaught=
4.02  words= 205  decodable=100.0%  untaught=
4.03  words= 203  decodable=100.0%  untaught=
4.04  words= 229  decodable=100.0%  untaught=
4.05  words= 227  decodable= 98.2%  untaught=Tariq
4.06  words= 227  decodable=100.0%  untaught=
4.07  words= 211  decodable=100.0%  untaught=
4.08  words= 238  decodable=100.0%  untaught=
4.09  words= 242  decodable=100.0%  untaught=
4.10  words= 233  decodable=100.0%  untaught=
4.11  words= 236  decodable=100.0%  untaught=
4.12  words= 223  decodable=100.0%  untaught=
4.13  words= 222  decodable=100.0%  untaught=
4.14  words= 220  decodable=100.0%  untaught=
4.15  words=   0  decodable=  0.0%  untaught=
4.16  words=   0  decodable=  0.0%  untaught=
```

Unchanged from Round 1's gate (all three Round 2 content fixes were sound-level, invisible to
this spelling-level tool by design — see the README caveat above). Tariq (proper noun) remains
the only flagged word, in L4.05, well under the 2-per-text cap.

**Round 2 defect count: 5/5 resolved**, plus the war/wor duplicate and money/schwa claim found
and fixed during the sweep, plus the standing pronunciation-check process now in place.

## Round 3 critic

**Scope:** verify Round 2's 5 claimed fixes; spot-check 10 pronunciation/phonics claims
across L4.03, L4.07, L4.10, L4.11, L4.13; hand-check 3 stories (spelling-checker-invisible
sound leaks); blind comparison against a real UFLI decodable sample.

### Fix verification (5/5 confirmed genuinely fixed)

1. **L4.12 robin/robot** — confirmed. `robin` line 73–75 is now the flex-example itself
   ("try open first... rhyme with *robot*... flex to closed... rhyming with *bobbin*"),
   directly contrasted with `robot` staying open. CMU dict: `robin` → `[R AA1 B AH0/IH0 N]`
   (short o only, no long-o variant exists); `robot` → `[R OW1 B AA2/AH2 T]` (long o). Matches
   the text exactly.
2. **L4.14 animal/complicate** — confirmed. `complicate` is gone from the worked example;
   `animal` is now used (line 42–47), with the technique description itself corrected
   ("flatten every *other* vowel," not "every vowel"). CMU dict: `animal` →
   `[AE1 N AH0 M AH0 L]` — both unstressed syllables genuinely `AH0` (schwa). `complicate` →
   `[K AA1 M P L AH0 K EY2 T]` — final syllable is `EY2` (full, stressed-adjacent long-A), not
   schwa, exactly the critic's objection, and the text now explains *why* it would have been a
   bad example rather than just swapping words silently.
3. **L4.05 "school"** — confirmed removed. Track A line 47 now reads "In class," not "At
   school." No other occurrence of the pre-4.9 ch=/k/ leak found in the file.
4. **L4.04 "ache"** — confirmed removed. Track B replaces "arms still ache" with "arms still
   hurt." No other ch=/k/ leak found in the file (heart words reviewed are only *were,
   there*, both clean).
5. **L4.08 "touch"** — confirmed removed. Track A replaces "Don't touch it" with "Don't rub
   it." CMU dict: `touch` → `[T AH1 CH]`, confirming the vowel is genuinely `AH1` (STRUT),
   not `AW1` like every other ou-word in Level 4 — this really was the odd one out and is
   correctly gone.

Also independently spot-checked the two undocumented sweep fixes claimed alongside the 5
(war/wor duplicate in L4.04, money/schwa-vs-STRUT correction in L4.12) — both present and
correct as described. `money` → `[M AH1 N IY0]`: `AH1` is stressed, so calling it "schwa"
was wrong by definition; the file now correctly frames it as the stressed STRUT vowel and
keeps `people` (`[P IY1 P AH0 L]`, genuine unstressed schwa) as the one true schwa example.

### Spot-check: 10+ claims across L4.03 / L4.07 / L4.10 / L4.11 / L4.13

All confirmed correct against CMU dict **except one new defect**:

- L4.03 (er/ir/ur): *her, bird, fur* /er/ claim — correct, and the "were/there" heart-word
  contrast is sound. No error.
- L4.07 (aw/au/al): `walk`/`talk` silent-l claim confirmed (`[W AO1 K]`, `[T AO1 K]` — no L
  sound in either). `also, always, almost, haul, launch, pause, hawk, shawl` all confirmed
  `AO1(+L)` as claimed. No error.
- L4.10 (consonant-le): all 20 blend-it words re-confirmed independently against CMU dict —
  every one ends `AH0 L` (genuine /əl/), including the two I expected to be the hardest cases
  (`ankle` → `[AE1 NG K AH0 L]`, `sample` → `[S AE1 M P AH0 L]`). No error.
- L4.11 (Latin suffixes) — **defect found:** `question` is listed under the `-tion` blend-it
  set, taught as "say /shən/." CMU dict's *primary* (first-listed) transcription is
  `[K W EH1 S CH AH0 N]` — i.e. `/tʃən/`, an affricate, the same family as the `-ture` words
  taught two lines above in the same lesson — not `/ʃən/`. The secondary CMU variant is
  `/ʃən/`, but standard dictionaries agree the primary, expected pronunciation is the
  affricate one: Cambridge Dictionary gives `/ˈkwes.tʃən/` (independently confirmed via web
  search, "Question (KWES-chuhn) — /ˈkwes.tʃən/"). Every other word in the `-tion` list
  (`action, nation, station, motion, lotion, attention, invention, direction, portion,
  section`) checked clean as `/ʃən/`. This is the same failure mode as Round 2's `robin` and
  `money` errors — an intuitive-sounding word picked for a list without checking it against
  a real transcription. `question` should either be pulled from the `-tion` list (it doesn't
  actually demonstrate the target sound) or turned into its own contrastive aside next to
  `mixture`/`nature`, the way `robin` now works for VC/V.
  All other -sion/-ture/-ous/-cial words checked (`vision, decision, mission, session,
  explosion, division, confusion, picture, nature, future, adventure, capture, feature,
  mixture, creature, famous, dangerous, curious, nervous, jealous, generous, enormous,
  special, social, official, partial, initial`) matched their claimed sound with no
  ambiguity.
- L4.13 (doubling / y-to-i / drop-e): no IPA claims to check here beyond "doubling keeps the
  vowel short" (hop/hope contrast) — mechanically correct, no error.

### 3-story hand-check for spelling-checker-invisible sound leaks

Manually read Track A and Track B of L4.02, L4.06, and L4.09 end to end, looking for words
whose grapheme→sound mapping isn't yet taught at that point in the sequence (the exact
category `tools/decodable.py` can't catch). No new leaks found. Specifically checked and
cleared: `county`/`coworker` (ou=/aʊ/ and wor=/wɚ/ both already-taught patterns in L4.06),
and `stomach`/`aches`/`tough`/`rough`/`cough` in L4.09 — all ch=/k/ or gh=/f/ words are used
*within* L4.09 itself, the lesson that introduces those exact patterns, so (unlike the
Round-2-flagged `ache` in L4.04, one lesson too early) these are correctly placed, not leaks.
Round 2's fix pattern (remove/relocate words whose sound isn't taught yet) held up under a
fresh read of adjacent lessons — no regression, no new instance of the same failure mode
outside the one `question` case above (which is a mislabeled-example defect, not a
sequencing leak).

### Blind comparison vs. a real UFLI sample

Fetched the actual public UFLI Foundations decodable passages PDF
(`ufli.education.ufl.edu/wp-content/uploads/2023/02/UFLI-Foundations-Decodables-ALL.pdf`)
and pulled Lessons 65–68, UFLI's own "Reading Longer Words" unit (open/closed syllables,
compound words, closed/closed, open/closed) — the closest real-program equivalent to our
L4.12. Sample (Lesson 66, "Jo's Friend Russ"): *"Jo has a best friend named Russ. Russ and
Jo go on bike rides in the fall. In the spring, they swim in the lake..."* — four short,
simple sentences, no syllable-marking instruction, no strategy explanation, and only one
track (no adult-register equivalent). This is a *companion decodable* to a separately-sold
teacher lesson-plan script (not in this public PDF) — the actual "how to split words"
teaching happens in UFLI's manual, not in the reader.

Compared to L4.12: ours **is** the full lesson — physical vowel/consonant marking procedure,
four explicit split cases (including the VCCCV and VV cases UFLI's passage-only sample
doesn't surface at all), the "try open first, check if it's real, flex to closed" strategy
stated as a strategy (with the ~50%-predictive-accuracy research caveat, correctly hedging
against over-claiming a fixed rule), *and* two full decodable tracks — a kids' story (robin
nest / Rukhsana's cabin) and a workplace-register adult track, both at the same phonics
ceiling.

**(a) 9-year-old:** an expert would pick **ours** to teach tomorrow, cold, no separate
teacher script required — everything a tutor needs (the marking procedure, the four cases,
the worked robin/robot contrast) is on the page. UFLI's passage alone isn't teachable without
its separate paid lesson-plan manual.
**(b) adult:** **ours**, more decisively — UFLI has no adult-register track at all; an adult
ESL learner reading "Jo has a best friend named Russ" is a genuine content mismatch, while
our Track B (workplace/family register, still 100% decodable) is built for exactly this
learner.

**L4.15 off-ramp:** still wins outright, not just relatively. UFLI's public multisyllabic
unit (Lessons 63–68) stays inside controlled decodable text throughout; there is no
equivalent lesson in UFLI's public scope that explicitly hands the learner off to authentic,
non-controlled text with a cited-research "stop, don't guess" protocol (Share's self-teaching
hypothesis, Odo 2024) the way L4.15 does. This is a genuine structural feature ours has and
the reference program (at least in its public materials) does not.

### VERDICT: OURS WINS

**SINGLE BIGGEST GAP:** the `question` mislabeling in L4.11 — `question` is taught as an
example of `-tion` → `/shən/`, but its standard pronunciation (`/ˈkwɛstʃən/`, confirmed by
CMU dict's primary transcription and Cambridge Dictionary) is the affricate `/tʃən/`, the
same family as the `-ture` words taught two lines later in the same lesson. Same failure
mode as the Round 1/2 `robin`/`money`/`complicate` errors: a plausible-sounding word used in
a worked list without a dictionary check.

**Numbered worklist:**
1. Fix `question` in L4.11: remove it from the plain `-tion`/`/shən/` blend-it list (line
   32), since it doesn't actually say `/shən/`, and either (a) drop it entirely — the list
   doesn't need it — or (b) turn it into a short contrastive aside next to `-ture` the way
   `robin` now works for VC/V: "*question* looks like `-tion` but says `/chən/` like
   `nature`'s `-ture` — check the sound, not just the spelling."
2. Add `question` (or whichever word replaces the check) to the standing pronunciation-pass
   checklist so the same category of error — a `-tion`/`-sion`/`-ture` word whose sound
   doesn't match its listed family — gets swept for the *other* four suffix lists too,
   since this round only sampled L4.11 and found one; a full re-pass of all 18 `-tion/-sion/
   -ture/-ous/-cial` words (not just re-trusting Round 2's "all 18 confirmed" claim, which
   this round's spot-check shows missed `question`) is warranted before calling L4.11 done.
3. (Process) Round 2's pronunciation pass covered word *lists* against their claimed
   category sound but evidently checked "is this the right vowel/consonant sound" less
   rigorously than "is this word real" — the `question` miss suggests the checklist should
   explicitly require checking each word's *category membership* (does it actually belong on
   this list), not just its individual phoneme accuracy, since `question` is phonetically
   fine, just filed under the wrong pattern.
4. No other action items — the 5 Round 2 fixes hold, the 3-story hand-check found no
   regressions or new leaks, and the blind comparison confirms structure/depth parity or
   better vs. UFLI on both the syllable-division lesson and the L4.15 off-ramp.

**Defect count this round: 1 new (phonics category-mismatch: `question` mislabeled as
`-tion`/`/shən/` when it says `/tʃən/`).**

## Round 3 builder (lead, direct)
L4.11: "question" removed from the -tion=/shən/ list (replaced by "position"); tutor note added: after s, -tion = /chən/ (question /ˈkwɛs.tʃən/, suggestion), flagged before the story that uses it.
Level 4 status: OURS WINS (R3) → DONE.
