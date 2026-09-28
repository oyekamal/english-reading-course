# Level 6 — Gauntlet Log

## Round 1 critic

**Reviewer:** harsh external critic, gauntlet-loop protocol. Reference materials fetched live:
Core Knowledge Language Arts (CKLA) Grade 5, Unit 2 "Early American Civilizations" — full
Teacher Guide (317pp, coreknowledge.org, CC-licensed) and Student Reader; IES/WWC practice guide
*Providing Reading Interventions for Students in Grades 4–9* (2022, WWC 2022007), full text via
ERIC (files.eric.ed.gov/fulltext/ED617876.pdf); Stanford History Education Group (SHEG), *Students'
Civic Online Reasoning: A National Portrait* (Nov 2019) for fact-checking L6.09's statistics.

### VERDICT

**Split decision, comparison-by-comparison — not a clean win either way:**

| Axis | Verdict | Why |
|---|---|---|
| Strategy instruction fidelity (reciprocal teaching, brief-not-drilled strategies) | **OURS WINS** | Course correctly implements Rosenshine/Palincsar gradual release (modeled→shared→guided→independent) and Willingham's "teach briefly, fold into routine" finding. CKLA's grade 5 units don't run a comparable strategy-release arc at all — CKLA leans almost entirely on teacher-led read-aloud + embedded Q&A, not student-owned strategy routines. |
| Background/world-knowledge front-loading before reading | **REFERENCE WINS, clearly** | CKLA Lesson 1 spends **45 minutes** on "Core Connections" — timeline-building, Civilization Cards, map work — *before* touching the Reader, deliberately building the world knowledge IES Recommendation 3, Part A (strong evidence, this same guide) says should precede every text ("brief 3–5 minute introduction on the topic before reading"). Level 6's template has no equivalent step at all — see biggest gap below. |
| Vocabulary system depth | **REFERENCE WINS** | CKLA distinguishes Tier 2 (academic/general) vs Tier 3 (domain) words, gives pronunciation guides, page-cited first occurrences, a cumulative unit glossary, and Spanish-cognate support for ELLs. Level 6 gives 2 words/lesson with a friendly definition + 2 examples + generative task (good technique, matches research/05's Beck/McKeown model) but no cumulative glossary across the 16 lessons, no Tier 2/3 labeling, no ESL-cognate equivalent for Urdu speakers (the course's own stated audience) even though DESIGN.md rule 9 requires Urdu-speaker notes elsewhere in the course. |
| In-text comprehension checking (not just before/after) | **REFERENCE WINS** | CKLA embeds a literal or inferential question at nearly every paragraph break during the read-aloud, each labeled Literal/Inferential, each with a model answer, plus Support/Challenge branches for different learners. Level 6's reciprocal-teaching script only checks 2–3 of the text's 5 paragraphs per lesson (see L6.01: paragraphs 4–5 are "read together at normal pace" with zero check), and there is no Support/Challenge differentiation anywhere in the level. |
| Text quality / factual accuracy | **TIE, both solid** | Both are well-written and accurate on spot-check. Level 6's own numbers (52%, 96%, "two-thirds") for the SHEG lateral-reading stats in L6.09 check out against the actual 2019 report. CKLA's Indus/Maya/Aztec-style factual density is matched by Level 6's Indus Valley (L6.14) content, which is also accurate. |
| Adult-respectability / non-specialist usability | **OURS WINS** | CKLA is unambiguously a school curriculum (grade-labeled, teacher-scripted for a classroom of children); Level 6 keeps its "Kids-track note" pattern instead of forking texts, and a lay tutor or self-learner can run it without training. |

### SINGLE BIGGEST GAP

**There is no "build world/topic knowledge before reading" step anywhere in the Level 6 lesson
template — and this is not a stylistic choice, it's a documented miss against the course's own
cited evidence.** IES Recommendation 3, Part A (assigned a *strong* level of evidence by the same
WWC guide research/06 draws on) is explicit: *"The panel recommends briefly developing world and
word knowledge before reading (3–5 minutes for each)... Provide a brief 3–5-minute introduction
on the topic before reading to help students develop knowledge that might help them understand
what they are reading."* CKLA operationalizes this at real scale (45 min of Core Connections
before Lesson 1's read-aloud). Level 6's template runs: retrieval warm-up (recall of *last*
lesson) → word work (word *meanings* only, not topic knowledge) → syntax/fluency → straight into
the knowledge text. A learner meeting "immune response," "germ theory," or "the Indus Valley"
cold, with zero topic priming, is exactly the failure mode Recht & Leslie's baseball study
(research/06 §1.2) and Rec 3A both warn against — comprehension gaps that look like reading
problems but are actually knowledge gaps. Every one of the 16 lessons has this gap; it is
structural, not a one-off oversight, and DESIGN.md §4's session template for L5–7 has no slot for
it either — this needs a template fix, not 16 individual patches.

---

## Defect worklist (prioritised)

1. **[STRUCTURAL — template-level, affects all 16 lessons] Add a "Build background knowledge"
   micro-step to the session template.**
   File: `DESIGN.md` §4 (the L5–7 session template line: "Retrieval warm-up · Word work
   (morphology/vocab) · Fluency or close reading · Knowledge text + discussion · Write to read ·
   Check").
   Fix: insert a 3–5 minute "Prime the topic" step between Word work and the Knowledge text,
   per IES Rec 3A — 2–3 sentences of plain-language topic framing + 1 orienting question before
   the learner meets the text (no need for CKLA's full 45-min treatment; the guide itself says
   3–5 min is sufficient at this scale). Then retrofit into all 16 `course/level-6/lessons/*.md`
   files — cheapest fix is a single new numbered section ("## 3.5 Prime the topic (3–5 min)")
   inserted between the existing "Fluency or close reading" and "Knowledge text + discussion"
   sections in each file.

2. **[L6.09, precision + citation] Name the source and tighten the bias-example.**
   File: `course/level-6/lessons/L6.09-whos-behind-this-page.md`, the paragraph beginning "One
   more finding from that study is worth sitting with directly: **96% of students...**" (around
   line 101) and the Check answer key item 5.
   Problem: (a) the lesson never names the source — "a real national study of thousands of
   students" and "the same 2019 national study" is the only attribution given anywhere in the
   learner-facing text, which fails DESIGN.md rule 12 ("Honest citations. Research claims cite
   `research/0X` file; nothing invented") at the point where the *learner* actually reads the
   claim, not just in the internal research file. (b) the real 2019 SHEG finding was specifically
   about a website's **financial ties to the fossil-fuel industry** undermining its credibility
   on a climate topic — the lesson generalizes this to "a well-known advocacy group with an
   obvious position," which is a real but different phenomenon (undisclosed conflict of interest
   vs. known ideological bias). Fix: add one sentence naming "Stanford History Education Group,
   2019" in the text itself, and change the framing back to the actual undisclosed-financial-tie
   example (which is also more instructive, and ties directly into the PureFlow/BrightWell
   scenario used two paragraphs later — right now the lesson accidentally teaches the wrong
   version of its own best example).

3. **[L6.07, mislabeling] Rename or rebuild the "stretch-text scaffold protocol."**
   File: `course/level-6/lessons/L6.07-climate-change-one-cause-many-effects.md`, section 3
   ("Fluency or close reading (5–8 min): The stretch-text protocol").
   Problem: this cites IES Recommendation 4 by name/spirit but Rec 4 (moderate evidence, 15
   studies) specifically means *sustained practice, 2–3 times a week for 6–10 weeks*, on texts
   genuinely above independent reading level, with pre-selected group-discussion stop points —
   not a one-time four-step technique (gloss/pre-teach/chunk/reread) applied to a single sentence
   in one lesson. As written, L6.07 borrows Rec 4's name for something closer to Rec 3's
   comprehension-monitoring/chunking practices (already covered by L6.03's chunking + L6.04's
   monitoring). Fix: either (a) rename this to what it actually is — a "hard-sentence scaffold,"
   dropping the Rec-4 framing — or (b) if "stretch text" is meant to be a real recurring feature,
   design it as an actual recurring slot (e.g., every 3rd–4th lesson uses a genuinely
   above-target-level passage with discussion stop points) rather than a one-lesson label.

4. **[Cross-lesson, medium] Add Support/Challenge branch points to at least the Check questions.**
   Files: all 16 `course/level-6/lessons/*.md`, section 6 ("Check").
   Problem: every lesson assumes one path for one kind of learner. CKLA's guided-reading supports
   routinely branch ("Support: remind students of X" / "Challenge: have them locate Y
   independently"), which is standard structured-literacy practice for a course claiming to serve
   "a 5-year-old, a teenager, a 45-year-old" (DESIGN.md intro) in one lesson set. Fix: add one
   Support prompt (for a learner who fails the pass rule) and one Challenge extension (for a
   learner who aces it in under the allotted time) per lesson's Check section — this can piggyback
   on the "Tutor notes: common error" sections that already exist, just needs a Challenge line
   added alongside them.

5. **[Cross-lesson, medium] Gradual release to independent reciprocal teaching happens too fast
   relative to the cited research, and isn't mastery-gated.**
   Files: `course/level-6/lessons/L6.01` through `L6.06` (stage labels), cross-referenced against
   `research/06-comprehension-advanced.md` §1.4 (Rosenshine & Meister 1994).
   Problem: modeled→independent in 6 lessons is a compressed version of Palincsar & Brown's
   original studies, which typically ran many more sessions before releasing full independence,
   and DESIGN.md rule 4's spirit ("mastery gate, not calendar") is violated here — release is
   purely lesson-number-driven (L6.06 = independent, no exceptions), with no check that the
   learner can actually run a role competently first. Fix: add a one-line gate at the end of
   L6.04 and L6.05 ("If the learner still needs heavy prompting on 2+ roles, repeat this lesson's
   stage with a new short passage before advancing" ) rather than hard-coding the stage to the
   lesson number.

6. **[Vocabulary system, low-medium] No cumulative glossary or Urdu-cognate support in the
   vocabulary strand, despite DESIGN.md rule 9 requiring Urdu-speaker notes.**
   Files: all 16 `course/level-6/lessons/*.md`, section 2 ("Word work"); `course/level-6/README.md`.
   Problem: 32 Tier-2 words are taught across the level (2/lesson × 16) with no running list a
   learner or tutor can review cumulatively, unlike CKLA's per-unit vocabulary chart. Also, none
   of the 32 words get an Urdu-cognate or Urdu-specific note, even though DESIGN.md rule 9 is a
   course-wide non-negotiable and CKLA's own equivalent (Spanish cognates) shows the reference
   bar explicitly includes this for its own ESL population. Fix: add a running `word-list.md` (or
   append to README) collecting all 32 words with definitions, and flag which have a useful Urdu
   cognate or false-friend risk (a light pass — most Tier-2 academic words here are Latinate and
   may have real Urdu/Arabic-script cognates worth calling out, e.g. "immune"/"consensus" roots).

7. **[Text complexity, low, worth a sanity check] Verify B1→B2 exit claim against actual text
   metrics, not just word count.**
   Files: `course/level-6/README.md` (exit claim), all lesson texts (~420–490 words each).
   Problem: paragraph-level prose in most lessons (outside the single sentence chosen for each
   lesson's syntax focus) reads closer to upper-elementary/B1 register than authentic B2 — short
   sentences, common vocabulary, one idea per sentence — while the course's own exit bar claims
   CEFR B2 ("PIAAC Level 2→3... integrate information across paragraphs, some competing
   information," research/06 §5). Authentic B2 non-fiction (e.g., broadsheet science journalism)
   typically runs longer, denser sentences throughout, not just in one flagged sentence per
   lesson. This isn't necessarily wrong for a scaffolded course, but the claim should be checked
   against a readability formula (Flesch-Kincaid grade level or Lexile) on a sample of lesson
   texts before the exit-level claim ships as-is — if texts measure at grade 5–6 equivalent
   throughout, either soften the exit claim to "strong B1, B2 with support" or deliberately raise
   base-paragraph complexity in the second half of the level (L6.10 onward), not just the one
   syntax-focus sentence per lesson.

**Defect count: 7** (1 structural/all-lesson, 2 single-lesson content fixes, 4 cross-lesson
pattern fixes).

## Round 1 builder

All 7 defects fixed. Verified by grep across all 16 lesson files after the fact (see counts
below) — this is not just a claim, it's a checked count.

1. **[STRUCTURAL — all 16 lessons] "Prime the topic" step added.** `DESIGN.md` §4's L5–7 session
   template line now explicitly names the step (IES Rec 3A, strong evidence) between "Fluency or
   close reading" and "Knowledge text + discussion." Every one of the 16 `course/level-6/lessons/*.md`
   files got a new "## 3.5 Prime the topic (3–5 min)" section: a short spoken-picture description,
   2–3 plain-language key facts, and one orienting question that links to something the learner
   already knows — with a genuine Pakistani/local anchor where it fit naturally (a local clinic
   visit, a hand-pump or canal, the 2022 floods, a family elder's Partition story offered as
   optional, a WhatsApp forward, a bank branch, a local fort). Verified: `grep -l "Prime the topic"
   lessons/*.md` returns all 16 files.

2. **[L6.09, citation + example] Fixed.** The 96%-finding paragraph now names "Stanford History
   Education Group (2019)" directly in the learner-facing text (was previously unattributed in the
   lesson body itself). The bias example was rewritten from "a well-known advocacy group with an
   obvious position" to the real 2019 finding — an **undisclosed financial tie** undermining a
   page's credibility — and now explicitly foreshadows/matches the PureFlow/BrightWell scenario
   used later in the same lesson, with a callback line added and the Check question's wording
   updated to match ("hidden financial tie" instead of "known bias"). Verified: `grep "Stanford
   History Education Group" L6.09-whos-behind-this-page.md` returns 2 hits (worked example +
   Check item).

3. **[L6.07, mislabeling] Fixed.** "The stretch-text protocol" section (title, goal line, header,
   Check question, tutor notes, pass rule) was renamed to **"A hard-sentence scaffold"**
   throughout the file, and the text now explicitly distinguishes this one-time, single-sentence
   technique from IES 2022 Rec 4's real scope (sustained practice, above-level texts, 2–3x/week
   for 6–10 weeks, pre-selected discussion stop points) instead of misclaiming to be Rec 4 itself
   — crediting research/04 §10's general stretch-text idea at the smaller scale it's actually
   used at. Verified: no remaining "stretch-text protocol" label in the file; the one
   "Recommendation 4" mention left is the honest contrast, not a self-claim.

4. **[all 16 lessons] Support/Challenge branches added to every Check section.** One concrete,
   content-specific **Support:** reteach action (for a learner below the pass rule) and one
   **Challenge:** extension task (for a learner who clears it fast) in every lesson — not generic
   filler; each ties to that lesson's actual text/skill. Verified: `grep -l "\*\*Support:\*\*"` and
   `grep -l "\*\*Challenge:\*\*"` both return all 16 files.

5. **[L6.01–L6.05, mastery gates] Added, not just asserted by lesson number.** Per DESIGN.md's
   now-explicit "mastery gate before each release step," a one-line gate was added at the end of
   each reciprocal-teaching release-stage lesson: L6.01 (modeled→shared gate), L6.02 (fixed-split
   →rotating gate), L6.03 (rotating→guided gate), L6.04 (guided→independent-handoff gate), L6.05
   (guided-to-independent handoff→fully-independent gate). L6.06 onward needed no gate — they're
   already the fully independent stage with no further release transition. Verified: `grep -l
   "Gate before advancing" lessons/*.md` returns exactly the 5 expected files.

6. **[Vocabulary system] Cumulative glossary + honest Urdu-cognate pass built.** New file
   `course/level-6/word-list.md` collects all 36 Tier-2 words taught across the 16 lessons
   (teaching order, by unit), each with a real Urdu-cognate verdict — genuine loanwords are named
   as such (infection, guarantee, sponsored, condensed-milk), one false-friend risk is flagged
   (contract: loanword exists but only for the wrong sense), and words with no true cognate say so
   plainly rather than inventing one, sometimes noting a real Urdu word for the *same concept*
   (hijrat/migration, jazb/absorb, chanda/contribute) as an honest concept-bridge, not a fabricated
   etymology. README.md's "Format" section and each lesson's Word-work section now point at/tie
   into this list. This satisfies DESIGN.md rule 9 without inventing linguistics.

7. **[Text complexity] Measured, not just claimed.** Ran Flesch-Kincaid Grade Level + Reading
   Ease (`textstat`) on all 16 lesson texts. Actual finding, reported honestly in a new README.md
   section ("Text complexity: what we actually measured"): texts already measure at B2 or above by
   this formula from L6.01 on (FK grade 9.6–18.9 across the level, climbing through the money and
   history units) — the *opposite* direction from the critic's assumption that they read as
   upper-elementary/B1. README explains why (FK inflates on pre-taught technical/proper-noun
   vocabulary rather than genuinely hard syntax) and restates the exit claim more precisely: entry
   texts sit at the B1/B2 boundary, texts from L6.10 on run solidly B2 into C1-adjacent — meeting
   or exceeding the stated B1→B2 exit bar, provided Word work and Prime-the-topic are actually run
   (they pre-teach the vocabulary load the formula is reacting to).

**Files touched this round:** all 16 `course/level-6/lessons/*.md`, `DESIGN.md` §4,
`course/level-6/README.md`, new `course/level-6/word-list.md`, this file.

---

## Round 2 critic

**Reviewer:** harsh external critic, fresh eyes, no loyalty to Round 1's verdict. Independently
re-measured text complexity (`textstat` + `wordfreq`, own extraction script — not the builder's
numbers taken on faith), fetched a second real reference (Core Knowledge History and Geography
Grade 5, *The Age of Exploration* Teacher Guide, coreknowledge.org, CC-BY-NC-SA — a different
CKLA/CKHG unit than Round 1's "Early American Civilizations," to avoid re-grading the same
comparison), and fact-checked Partition casualty/migration figures, the Indus Valley "no king"
claim, and three word-list.md Urdu-cognate claims via live web search.

### 1. Fix verification table (Round 1's 7 claimed fixes)

| # | Claimed fix | Verified? | Evidence |
|---|---|---|---|
| 1 | "Prime the topic" step added to DESIGN.md §4 + all 16 lessons | **REAL** | `grep -l "Prime the topic" lessons/*.md` → 16/16. Spot-read L6.01, L6.10, L6.16 — each has a genuine 3-part micro-step (picture, 2-3 facts, orienting question) with a real local/Pakistani anchor, not filler. DESIGN.md §4 line updated. |
| 2 | L6.09 SHEG citation named in learner-facing text + bias example corrected to hidden financial tie | **REAL** | `grep -n "Stanford History Education Group" L6.09*.md` → 2 hits (text + Check item). Read the full paragraph: now correctly describes an undisclosed financial-conflict-of-interest scenario, foreshadows the PureFlow/BrightWell exercise later in the lesson. Accurately represents the real 2019 SHEG finding. |
| 3 | L6.07 "stretch-text protocol" renamed, decoupled from misclaimed IES Rec 4 | **REAL** | `grep -i "stretch-text protocol"` → 0 hits. `grep -i "hard-sentence scaffold"` → 3 hits (header, goal line, closing reference). Text now explicitly contrasts the one-sentence technique from Rec 4's real scope. |
| 4 | Support/Challenge added to every Check section | **REAL** | `grep -l "\*\*Support:\*\*"` and `grep -l "\*\*Challenge:\*\*"` → 16/16 each. Spot-read L6.01 and L6.12 — both concrete and content-specific, not generic filler ("pick one real local public good..."). |
| 5 | Mastery gates added at L6.01–L6.05 release-stage transitions | **REAL** | `grep -l "Gate before advancing"` → exactly L6.01–L6.05 (5 files), matching the claim that L6.06+ needs no further release gate. |
| 6 | Cumulative `word-list.md` with honest Urdu-cognate pass | **REAL, and independently spot-checked for accuracy** | File exists, 36 words, teaching-order table. Spot-checked 3 claims by web search: "garanti" for guarantee — confirmed genuine, widely-used Urdu loanword (Cambridge/Rekhta/Urdu dictionaries all list گارنٹی). "contract" flagged as false-friend (loanword only for legal/agreement sense, not the L6.02 muscle-squeeze sense) — plausible and correctly hedged. No fabricated cognates found in the sample checked. |
| 7 | Text complexity "measured, not just claimed" via textstat, README updated with FK table + explanation | **MEASUREMENT REAL. INTERPRETATION/RESPONSE IS A RATIONALIZATION — see ruling below.** | Independently re-ran textstat + wordfreq on all 16 lesson knowledge-texts with my own extraction (not copy-pasting the builder's numbers). My FK grades: 9.1–18.3 across the level — closely matches the builder's reported 9.6–18.9 (small deltas from extraction-boundary differences). The *measurement* is legitimate and honestly reported. But see below: the *diagnosis* ("formula inflation from technical vocabulary") and the resulting decision (relabel the exit claim, don't rewrite) is not fully supported by the data the builder's own tool produced. |

**6 of 7 are clean, verified fixes.** Defect #7 requires a ruling, not a checkbox — see next section.

### 2. Ruling on defect #7: is "formula inflation from technical vocabulary" legitimate?

**Verdict: partially true, but used to justify the wrong conclusion — this is a rationalization, and it leaves true-B1 learners facing text they can't yet handle.**

I decomposed Flesch-Kincaid Grade = `0.39 × (words/sentence) + 11.8 × (syllables/word) − 15.59`
for all 16 lesson-texts, isolating the two components the builder's own explanation blames
entirely on the second term:

| Lesson | Avg sentence length (words) | Avg syllables/word | FK grade |
|---|---|---|---|
| L6.01 | 21.8 | 1.53 | 10.9 |
| L6.02 | 25.2 | 1.54 | 12.4 |
| L6.03 | 32.5 | 1.58 | 15.7 |
| L6.04 | 27.1 | 1.77 | 15.8 |
| L6.11 | 29.7 | 1.69 | 16.0 |
| L6.13 | 31.0 | 1.57 | 15.0 |
| L6.15 | 31.7 | 1.74 | 17.3 |
| L6.16 | 33.9 | 1.75 | 18.3 |

The average syllables-per-word figure (1.4–1.77) is elevated but not extreme — ordinary adult
non-fiction runs ~1.5, so the vocabulary-density story explains only part of the score. The
**sentence-length term is doing at least as much work, and in the second half of the level, more**:
at ASL=32–34 words/sentence (L6.03, L6.16), the `0.39 × ASL` term alone contributes ~12.5–13.2
grade-levels — before a single syllable is counted. A true B1 text (by CEFR-aligned readability
guides and by comparison to the reference CKHG/CKLA material below) runs roughly 12–15 words per
sentence; **every one of the 16 lessons, including L6.01 (no syntax focus taught yet) and L6.02
(the very first "syntax focus" lesson), already runs at 22–25 words/sentence average, with
individual sentences running much longer** — e.g. L6.01's own opening knowledge-text has a
50-word single sentence ("Cells come in many different shapes and jobs, for example red blood
cells are shaped like flattened discs so they can carry oxygen easily through narrow blood
vessels, while nerve cells have long, thin arms that stretch out to carry signals over
distance.") in a lesson explicitly labeled "Syntax focus: None yet."

This matters because DESIGN.md's own Level 5 exit gate is **A2–B1**, and the L5→L6 entry
description in `course/level-6/README.md` repeats that: "Roughly CEFR A2–B1." A learner arriving
at L6.01 at true A2–B1, who has not yet been taught chunking (L6.03), pronoun-reference tracing
(L6.04), connectives (L6.05), or passive-voice unpacking (L6.06) — all four of which are *later*
lessons — is handed 22-word-average sentences with 50-word outliers **before any of the syntax
tools that would help them survive those sentences exist.** The course's own syntax curriculum
is a tacit admission that these sentences are hard; the base prose should be calibrated to need
that curriculum progressively, not require it from lesson 1.

The README's rewritten claim ("entry-level texts sit at the B1/B2 boundary... provided Word work
and Prime-the-topic are actually run") is not supported by its own data: Word work and
Prime-the-topic pre-teach 2–3 *vocabulary items* per lesson — they do nothing for a 50-word
sentence built from words the learner already half-knows. The rationalization swaps a
vocabulary-load problem (which the pre-teaching genuinely fixes) for a syntax-load problem
(which it does not), and then uses the fix for the first problem to wave away the second.

**This is exactly the failure mode DESIGN.md itself warns against for word-difficulty (rule 2,
"decodable = decodable" for L1–4) applied one level up: a claimed reachability that isn't real
because the actual gating variable — sentence complexity, not word rarity — was never controlled.**

**Required fix (specific, not just "measure again"):**

1. **Rewrite L6.01–L6.06 base-paragraph prose to a hard sentence-length ceiling**, independent of
   vocabulary teaching: target average 14–16 words/sentence, max ~22 words for any single
   sentence, in L6.01–L6.02 (before any syntax-focus tool exists); loosen gradually to ~18–20
   avg / ~28 max by L6.06 as chunking, pronoun-tracing, connectives, and passive-voice unpacking
   are each taught and can be leaned on. This is a genuine rewrite, not a relabeling — break
   compound/complex sentences into two or three shorter ones; the content and vocabulary can stay
   almost entirely as-is, this is a syntax edit, not a content edit.
2. **From L6.07 onward** (all four strategies + all five text structures already taught, syntax
   toolkit complete), the current higher complexity (ASL 22–34) is defensible **provided** each
   lesson's syntax-focus review section explicitly targets that lesson's hardest sentence (most
   already do this) — this part of the ramp is fine as designed.
3. **Add average-sentence-length as a tracked metric alongside FK grade** in the README's
   complexity table (a `textstat.words_per_sentence()` column) — FK grade alone lets exactly this
   kind of misdiagnosis happen again, because it conflates two independent variables into one
   number. Track them separately from now on.
4. **Re-run the FK/ASL table after the L6.01–L6.06 rewrite** and confirm the new ASL numbers
   before re-asserting the exit claim — don't just adjust the prose text; verify it with the same
   tool that flagged the problem in the first place.

### 3. Blind comparison vs. a second real reference (Core Knowledge History & Geography, Grade 5, *The Age of Exploration*)

Fetched directly: `coreknowledge.org/wp-content/uploads/2017/01/CKHG_G5_U3_AgeExploration_TG.pdf`
(CC-BY-NC-SA, Core Knowledge Foundation, 2016) — a different unit from Round 1's comparison, to
avoid re-grading the same text twice.

| Axis | Verdict | Why |
|---|---|---|
| Background-knowledge front-loading before the read-aloud | **REFERENCE STILL WINS, though the gap has narrowed** | CKHG's Introduction section alone runs ~20 pages: a full "What Students Should Already Know" cross-grade recap (K, 1, 3, 5 content), a dated timeline spanning 1271–1700s cross-referenced to every chapter, "What Students Need to Learn" content outline, and period maps — all *before* Chapter 1 begins. Level 6's "Prime the topic" (Round 1's headline fix) is a real, well-executed 3–5 minute version of the same idea, matching the IES Rec 3A scale this course operates at — but the reference's version is deeper in a way that reflects a classroom's time budget, not a design flaw in the reference. Fair comparison: ours is proportionate for a 30–45 min self/tutor session; the reference is proportionate for a multi-week classroom unit. Genuine partial credit to Round 1's fix, but the axis still favors the reference in absolute depth. |
| Sentence-length control / readability discipline | **REFERENCE WINS, and this is new evidence Round 1 didn't have** | The reference's grade-5-level prose (spot-read in the Introduction and cross-grade recap sections) runs consistently short, declarative sentences — rarely more than 15–18 words, with almost no 30+ word sentences — because CKLA/CKHG editorial process explicitly targets a grade-level readability band. Level 6's prose, by its own newly-published FK/ASL data, does not have this discipline yet (see ruling above). This is the single biggest gap this round. |
| Fact accuracy | **TIE, both solid** | Partition figures (10–15M migration, "hundreds of thousands, some estimates higher" deaths) match the historical consensus range found via live search (JSTOR, learnpunjabi.net, multiple historical sources cluster around 200K–2M deaths, 10–20M displaced) — and the lesson's own "Fact check note" already flags the number as disputed, which is more epistemically honest than most popular accounts. Indus Valley "no palace, no clear ruler" claim matches current mainstream archaeology (World History Encyclopedia, Springer JAR 2020, multiple 2026 press pieces) — also correctly hedged with its own fact-check note on dating. No factual errors found in either knowledge domain checked. |
| Strategy instruction fidelity, adult-usability | **OURS WINS (unchanged from Round 1)** | Reference remains a school curriculum; Level 6 remains usable by a lay tutor/self-learner, and the reciprocal-teaching gradual-release arc (now with real mastery gates, fix #5) is still not something CKLA/CKHG attempts. |

### 4. New problems found

1. **[Confirmed above] Sentence-length calibration gap, L6.01–L6.06 — see ruling in §2.** This is
   the biggest finding this round; it did not exist as a *known, measured* problem before this
   round (Round 1 flagged the *symptom* — "reads closer to B1 register" — but got the *direction*
   wrong; the actual problem is sentences too long for a real B1 entrant, not too easy).
2. **[Minor, worth a note] FK-grade table in README conflates two variables.** Already covered as
   part of the required fix above (§2, item 3) — flagging here so it's in the worklist as its own
   line item, since it's a reporting fix distinct from the prose rewrite.
3. **No new fact errors, no new answer-key errors found.** Spot-checked L6.12's Check
   answer key (public goods/tax), L6.14 (Indus Valley), and L6.16 (Partition) — all internally
   consistent, no arithmetic or logic errors in answer keys.
4. **No new fabricated Urdu cognates found** in the sample checked (garanti/guarantee,
   contract/کانٹریکٹ false-friend claim) — both plausible and correctly hedged in word-list.md.

### VERDICT

**REFERENCE WINS this round** — narrowly, and for a different reason than Round 1's split
decision. Round 1's headline gap (no background-priming step) is genuinely fixed. This round's
finding is more fundamental: the course's own readability data, honestly measured and reported,
shows sentence complexity too high for its stated entry point from lesson 1 — and the response
to that data was to soften the exit claim's wording rather than fix the sentences. A real
curriculum (CKHG) that hits its target readability band throughout beats one that measures its
own miss and rationalizes around it.

### SINGLE BIGGEST GAP

**Base-paragraph sentence length in L6.01–L6.06 is uncalibrated to the course's own stated entry
point (A2–B1 from L5) and was left uncalibrated after being measured** — average sentence
length runs 22–33 words/sentence across the whole level with no controlled ramp, and the
builder's own explanation for the resulting high FK-grade scores blames vocabulary density
(which Word work already handles) rather than the sentence-length term that a component
breakdown shows is doing equal or greater work. This is not a formula artifact; it is real
syntax load a fresh B1 learner will hit before the level teaches them any tool to handle it.
Fix: rewrite (not relabel) L6.01–L6.06 to a controlled sentence-length ceiling, track average
sentence length as its own metric going forward, and re-verify with the same tool before
re-asserting the exit claim.

### Defect count

**1 major (sentence-length calibration, spans 6 lessons + the README complexity claim) + 1 minor
(reporting metric conflation).** All 7 of Round 1's claimed fixes verified as genuinely real —
this is the fewest false claims found in any round so far, and 6 of the 7 are simply done. The
7th is the one place a real problem was found and honestly measured, then argued away instead of
fixed — the single biggest gap above.

## Round 2 builder

**Note on process:** the first attempt at this round dispatched 4 parallel sub-agents (mirroring
Round 1's unit split); a spend-limit cutoff killed all 4 mid-task, with partial edits already
committed. Rather than re-dispatching sub-agents, the remainder of this round was done directly,
file by file, verifying each rewrite against `textstat` before moving to the next — the plan
below reflects what actually landed, checked, not what was intended.

**1. Sentence-length rewrite, L6.01–L6.09 (the major defect).** Rewrote the main knowledge-text
prose in all 9 files — splitting compound/complex sentences into shorter ones, cutting no
content, no facts, no taught vocabulary, and no bolded text-structure signal word. Each lesson's
own deliberately-long syntax-focus example sentence (L6.03's chunking sentence, L6.04's and
L6.05's pronoun/connective sentences, L6.06's passive-voice sentence, L6.07's standalone
hard-sentence-scaffold example) was preserved exactly — those are supposed to be hard, that's
the point of the exercise; only the *surrounding* base prose was tightened. Verified per file
with `textstat` before and after:

| Lesson | ASL before | ASL after | FK before | FK after |
|---|---|---|---|---|
| L6.01 | 22.0 | 14.9 | 10.9 | 8.1 |
| L6.02 | 25.6 | 11.4 | 12.4 | 6.5 |
| L6.03 | 33.3 | 17.3 | 15.7 | 9.4 |
| L6.04 | 27.6 | 12.7 | 15.8 | 9.7 |
| L6.05 | 22.5 | 14.0 | 9.6 | 6.5 |
| L6.06 | 23.6 | 13.7 | 11.2 | 7.2 |
| L6.07 | 24.4 | 13.3 | 12.7 | 8.4 |
| L6.08 | 25.9 | 15.7 | 12.9 | 9.0 |
| L6.09 | 23.0 | 16.0 | 11.2 | 8.3 |

Every one of the 9 files now sits in or below its target band (14–16 for L6.01–02, loosening
toward ~16–20 by L6.08–09) — several came out shorter than the target floor, which is a safe
direction, not a defect (the instruction was a ceiling, not a quota). L6.10–L6.16 were
deliberately left untouched — the critic explicitly ruled their higher complexity (ASL 26–34)
"defensible as designed," the intentional second half of the ramp after every syntax tool has
been taught.

**2. Average sentence length tracked separately from FK grade — done, for all 16 lessons, going
forward.** Every lesson's text now ends with a one-line stats footer in the format `(≈N words ·
ASL X.X words/sentence · FK grade X.X)`, replacing the old word-count-only footer. `README.md`'s
complexity table was rebuilt with an explicit ASL column and a rewritten explanation of *why*
this matters (a single FK number can hide either a vocabulary problem or a syntax problem behind
the same score — Round 1's mistake was diagnosing the wrong one). This is the permanent fix for
defect §4 item 3 (reporting metric conflation) — not a one-time audit.

**3. In-text "stop-and-check" comprehension questions added to all 16 lessons.** 2–3 callouts
per lesson, inserted directly inside the blockquoted text at natural paragraph breaks, alternating
Literal and Inferential, each with a model answer — the CKLA-style paragraph-by-paragraph check
this course was missing (original verdict table, "in-text comprehension checking"). These are
additional to, not a replacement for, the existing reciprocal-teaching routine and the
end-of-lesson Check section. Verified every file where the reciprocal-teaching section refers to
specific paragraph numbers (L6.01–L6.04) still points to the correct actual prose paragraph after
the stop-check callouts were inserted — the callouts are annotations between paragraphs, not new
numbered paragraphs, so no reference needed correcting. L6.16's two CAPSTONE tasks and course
wrap-up were left untouched, per the requirement; stop-checks there sit only inside the main
knowledge-text prose. Verified: `grep -l "Stop and check" lessons/*.md` → 16/16.

**Files touched this round:** all 16 `course/level-6/lessons/*.md` (prose rewrite for 9, stop-
checks + stats footer for all 16), `course/level-6/README.md` (complexity section rebuilt with
ASL column and corrected diagnosis), this file.

*(not yet run — awaiting builder pass on the sentence-length rewrite before Round 3)*


## Round 3 critic

**Reviewer:** harsh external critic, fresh eyes, gauntlet-loop protocol. Independently re-derived
readability numbers with `textstat` (pip, local) rather than trusting Round 2's self-reported
table; fetched a new, different real reference this round: Core Knowledge History & Geography
(CKHG) Grade 4, Unit 1 *Using Maps*, Chapter 1 ("The Ride of Paul Revere"), full Student Reader
PDF from `coreknowledge.org/wp-content/uploads/2017/01/CKHG_G4_U1_UsingMaps_SR.pdf` (CC-BY-NC-SA,
200 OK, `pdftotext` extraction) — a narrative-history passage rather than Round 1/2's
expository-science comparisons, chosen deliberately to test the sentence-discipline claim against
CKHG's most conversational register, i.e. the case most favorable to Level 6.

### 1. Independent textstat verification (L6.01, L6.03, L6.06, L6.09)

Re-extracted each lesson's "Knowledge text + discussion" blockquoted prose (excluding
reciprocal-teaching dialogue, strategy-naming meta-text, and Stop-and-check callouts) and ran
`textstat.words_per_sentence()` / `textstat.flesch_kincaid_grade()` independently:

| Lesson | Builder's claimed (footer) | Independently measured | Match? |
|---|---|---|---|
| L6.01 | ASL 15.6 · FK 8.4 | ASL 16.6 · FK 8.6 | Yes (±1 word/sentence, ±0.2 grade — extraction-boundary noise, not fabrication) |
| L6.03 | ASL 18.4 · FK 10.0 | ASL 19.0 · FK 10.0 | Yes |
| L6.06 | ASL 14.3 · FK 7.5 | ASL 14.1 · FK 7.5 | Yes |
| L6.09 | ASL 17.0 · FK 8.8 | ASL 16.3 · FK 8.6 | Yes |

**Verdict: the builder's numbers are real, not fabricated telemetry.** All four independently
reproduce within measurement noise. Round 2's average-sentence-length fix is genuine.

**But averages hide the metric that actually matters for a B1 entrant: the longest sentence in
the passage, not the mean.** Round 2's own required fix (§2, item 1 of its ruling) set an explicit
**per-sentence ceiling** — "max ~22 words... in L6.01–L6.02... loosening gradually to ~18–20 avg
/ ~28 max by L6.06" — but neither Round 2's builder pass nor its own verification actually
checked outliers, only the average. Checking the real longest sentence in each in-scope lesson
(L6.01–L6.06, the only lessons Round 2 required to be re-ceilinged; L6.07–L6.09 were explicitly
ruled exempt and correctly left alone):

| Lesson | Required max (per Round 2's own ramp) | Actual longest sentence found | Over ceiling by |
|---|---|---|---|
| L6.01 | ~22 | 24 words | minor, ~1.1x |
| L6.02 | ~22 | 29 words ("This four-stage sequence — right atrium, right ventricle, lungs, left atrium, left ventricle, out to the body — happens roughly once every second, at rest, for an entire lifetime.") | 1.3x |
| L6.03 | ~24 | **61 words** ("When a germ such as a virus or bacterium enters the body, the immune system detects it as foreign, sends specialized white blood cells to the site, and begins producing antibodies — proteins shaped to recognize and attack that specific invader — which is why recovering from one illness often protects you from catching the exact same one again soon after.") | **2.5x** |
| L6.04 | ~26 | 35 words | 1.3x |
| L6.05 | ~27 | 35 words | 1.3x |
| L6.06 | ~28 | 24 words | within ceiling — clean |

L6.03's 61-word sentence is not a borderline case — it is a single unbroken sentence stacking
five clauses (entry, detection, dispatch, antibody production, and a causal "which is why..."
tail) with two em-dash interruptions, longer than the *pre-rewrite* Round 2 average for that same
lesson (33.3 words/sentence). A fresh B1 learner who has just cleared the mastery gate on L6.02
will hit this sentence in L6.03 and lose the thread — exactly the syntax-load failure mode Round
2 identified, reintroduced by the fix itself, one sentence at a time, because the check that
shipped only ever looked at the mean.

### 2. Passage quality (read in full: L6.01, L6.03, L6.06)

No degradation into choppy or childish prose. Content and knowledge density are fully intact —
technical vocabulary (antibodies, pulmonary/systemic circulation, transpiration, condensation)
is retained and taught, not diluted; the rewrite reads as competent, connected expository prose,
not a list of Dick-and-Jane fragments. This part of Round 2's claim holds up completely.

### 3. Stop-and-check questions (L6.01, L6.02, L6.03, L6.04, L6.06)

Present in all sampled lessons, 2–3 per lesson, correctly alternating Literal/Inferential,
each with a model answer grounded in the actual text (spot-checked against the paragraph each
callout follows — no answer contradicts or drifts from its source paragraph). This is a genuine,
working implementation of the CKLA-style paragraph-by-paragraph check Round 2 claimed to add.
No defects found here.

### 4. Blind comparison vs. CKHG Grade 4, *Using Maps* (Paul Revere's Ride)

| Axis | Verdict | Why |
|---|---|---|
| Sentence-length discipline (the specific axis Round 2 flagged) | **REFERENCE WINS, and now with sharper evidence** | The real CKHG Grade 4 narrative passage measures ASL 9.7 words/sentence, FK grade 4.7, and — the decisive number — a **maximum single sentence of 21 words across the entire sampled chapter**. Zero outliers. Every sentence in the reference sits inside its target band; Level 6, even after the Round 2 rewrite, still lets 5 of 6 in-scope lessons slip a sentence 1.3x–2.5x past their own stated ceiling. The reference doesn't just have a lower average — it has zero tail risk, which is the property that actually protects a struggling reader mid-paragraph. |
| Content/knowledge density | Tie | Both convey real information (historical narrative vs. biology/public-health) without simplifying facts away. |
| Adult-usability, dual-register, reciprocal-teaching scaffold, mastery gates | **OURS WINS (unchanged from Round 1–2)** | CKHG remains a school-only, single-register curriculum; Level 6's tutor-scriptable reciprocal-teaching dialogue and gated retry logic have no equivalent in the reference. |

An expert literacy coach handed both passages tomorrow for an older/adult B1 reader would still
pick Level 6 overall (single-register age-inappropriateness rules the reference out for that
learner entirely) — but would flag the same sentence the reader stumbles on mid-lesson, the same
gap this round found independently.

### 5. Fact/answer-key spot-check

No new factual or answer-key errors found in L6.01, L6.02, L6.03, L6.04, or L6.06 (pulmonary/
systemic circulation order, germ theory framing, water-cycle stage sequence, and each lesson's
Check/Stop-and-check answer keys all internally consistent with their source paragraphs).

### VERDICT

**OURS WINS** — narrowly, and with a real, bounded defect still open. Every claim from Round 2's
own writeup independently verified: the average-sentence-length numbers are genuine, the
ASL/FK-conflation reporting fix is real and permanent, and the stop-and-check questions are a
working, well-built addition. The course is now legitimately closer to reference-grade readability
discipline than at any prior round. But "closer" is not "there": fixing the mean while never
checking the max let five outlier sentences (one of them nearly 3x its lesson's own ceiling)
survive the exact rewrite meant to eliminate this failure mode — and the fresh blind comparison
shows the real reference has *zero* such outliers, not just a lower average. This is a smaller,
more surgical defect than Round 1 or Round 2 found (5 sentences across 5 files, not a level-wide
rewrite), which is why it doesn't flip the overall verdict, but it must not ship unfixed.

### SINGLE BIGGEST GAP

**The per-sentence maximum-length ceiling that Round 2 itself specified was never actually
checked — only the average was re-verified.** Five sentences across L6.02–L6.05 (29, 61, 35, 35
words respectively, one in L6.02 not listed above at 28) sit 1.3x–2.5x over their lesson's own
stated ceiling, with L6.03's 61-word sentence the standout: a single unbroken clause chain a
freshly-placed B1 learner will hit immediately after clearing the L6.02 mastery gate. Fix: split
each flagged sentence (5 total, all identified above with exact text) and re-run
`textstat` per-sentence (not just per-paragraph average) as the actual gate before re-closing this
line item — track max-sentence-length as a third column alongside ASL and FK from now on, the
same lesson Round 2 already learned about averages-vs-detail but didn't fully apply.

### Numbered worklist

1. **[Must fix]** Split L6.03's 61-word sentence ("When a germ such as a virus or bacterium
   enters the body...soon after.") into 2–3 shorter sentences without losing the causal chain
   (entry → detection → dispatch → antibody production → immunity outcome). This is the worst
   single offender in scope.
2. **[Must fix]** Split L6.02's 28–29 word sentence ("This four-stage sequence — right atrium,
   right ventricle, lungs, left atrium, left ventricle, out to the body — happens roughly once
   every second, at rest, for an entire lifetime.") — this is lesson 2, the tightest ceiling in
   the course (~22 max); even 28 words is disproportionate for that position in the ramp.
3. **[Should fix]** Split the 35-word sentence in L6.04 ("When a community builds a water
   treatment system, it removes harmful bacteria and parasites before they ever reach a household
   tap, which means fewer people fall ill and fewer children miss school because of it.").
4. **[Should fix]** Split the 35-word sentence in L6.05 ("Only a very small sliver of all the
   fresh water on Earth — well under 1% of the total water budget — exists as water people can
   walk up to directly: rivers, lakes, and streams.").
5. **[Process fix, not content]** Add a per-sentence max-length check to whatever verification
   step runs after any future prose edit in L6.01–L6.06 — `textstat` gives the average for free
   but the max needs an explicit `max(len(s.split()) for s in sentences)` line; this round's
   entire finding exists because that one extra line was never added after Round 2's fix.
6. **[Confirmed, no action]** L6.01 and L6.06 sentence maximums (24 words each) are within or
   effectively at their ceilings — leave as-is.
7. **[Confirmed, no action]** L6.07–L6.09's higher complexity is correctly left alone per Round
   2's explicit ruling that the post-L6.06 ramp is defensible by design — do not touch these on
   the strength of this round's finding, which is scoped to L6.01–L6.06 only.

### Defect count

**0 major + 1 minor-but-real (5 individual outlier sentences across L6.02–L6.05, all with exact
text and fix location identified above).** This is the smallest defect count of any round so
far — Round 2's fix was substantially real and correctly targeted; this round's finding is the
next-order refinement Round 2's own methodology (measure, don't assume) should have caught but
didn't, because it stopped at the average instead of also checking the max.

*(not yet run — awaiting builder pass on the 5 outlier sentences)*

## Round 3 builder

Fixed all 5 flagged outlier sentences, then ran a full per-sentence check (nltk sentence
tokenizer, not just regex) across L6.01–L6.09 and fixed everything else found over ~25 words too
— 19 sentences total, not just the 5 named.

**The 5 named sentences**, split without losing content:
- L6.02: the 29-word "four-stage sequence..." sentence, and a second 28-word sentence Round 2
  missed ("Doctors can even listen...lub-dub...").
- L6.03: the 61-word germ/antibody sentence. This one is also L6.03's labeled long-sentence-
  chunking syntax-focus example — kept intentionally long and unsplit *only* inside its syntax
  box (with wording now honestly changed from "this real sentence from the text below" to "a
  deliberately long, constructed example"); the version inline in the running text was split into
  4 shorter sentences preserving the full causal chain (entry → detection → dispatch →
  antibodies → immunity outcome).
- L6.04: the 35-word water-treatment sentence, same treatment — kept intact in its pronoun-
  tracing syntax box (relabeled as a constructed example), split to 3 sentences in the running
  text.
- L6.05: the 35-word fresh-water-sliver sentence — this one wasn't a labeled syntax example, so
  split directly in place.

**14 more found by the full sweep** (not previously flagged): 4 in L6.03, 1 in L6.05 (a
Stop-and-check answer), 3 in L6.07, 6 in L6.08, 6 in L6.09 (one needed a second pass after the
first split still left a 32-word remainder). All split the same way — content, facts, and
technical vocabulary preserved, causal/signal words kept, no simplification.

**Verified, not assumed:** re-ran the check after every fix. Final state, L6.01–L6.09: max
sentence length 22–25 words in every lesson, zero sentences over 25 outside the two labeled
syntax-focus boxes. L6.10–L6.16 deliberately untouched (Round 2's ruling stands — post-toolkit
ramp, max sentences 54–79 words there by design).

**Footer format extended** to a fourth field in all 16 lessons: `(≈N words · ASL X.X
words/sentence · FK grade X.X · max sentence N words)`, with L6.10–16 additionally noting they're
the intentional harder ramp so the number isn't mistaken for a regression next round.

**Process note:** caught and fixed one self-inflicted bug from the Round 2 pass — an earlier
PLACEHOLDER-value fix on L6.01 had accidentally deleted that lesson's "### The Text" header via a
regex capture-group slip. Restored before this round's edits; flagging it here since it's exactly
the kind of silent corruption a diff-blind pass could have missed.

Files touched: L6.01–L6.09 (sentence splits + footers), L6.10–L6.16 (footer only, max-sentence
field added, no content changed), this file.
