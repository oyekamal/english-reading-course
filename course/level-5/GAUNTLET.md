# Level 5 — Gauntlet Log

## Round 1 critic

**Reviewed:** course/level-5/README.md, all 16 lessons (L5.01–L5.16), mastery-check.md.
**Reference bar fetched this round:** REWARDS Intermediate 2nd Ed. Teacher's Guide sample
(Lesson 4 preskill + front matter, voyagersopris.com/silvereye.com.au sample PDF, Archer/
Gleason/Vachon); Rasinski's "The Fluency Development Lesson" (timrasinski.com PDF, 10-step
FDL routine + phrase-cued *Jabberwocky* worked example). Words Their Way derivational-relations
sample pages were located (Pearson) but not extractable as full lesson text this round —
comparison 1 uses REWARDS as the primary reference instead, which is the stronger, more
directly comparable bar for this level's "explicit morphology + multisyllabic decoding"
claim anyway.

---

### VERDICT

**Comparison 1 — Morphology session (L5.02, in-/im-/ir-/il- + dis-) vs. REWARDS Intermediate
Lesson 4/preskill sequence: OURS WINS**, on breadth and coherence (integrated Tier-2
vocabulary, knowledge-spine content, honest research-sourcing) — but REWARDS has two
concrete, adoptable mechanisms L5 lacks outright (see defects #4, #5). This is a "wins on
scope, loses on two specific skill-building mechanisms" verdict, not a clean sweep.

**Comparison 2 — Fluency/Readers Theatre program vs. Rasinski's Fluency Development Lesson:
REFERENCE WINS.** The RT scripts themselves (adult-dignified dialogue, no memorization, honest
"we don't know" framing on open historical questions) are a genuine, well-executed idea Rasinski's
classic FDL doesn't offer. But the underlying passages this program is built to be scored against
routinely fail to be at the level's own stated A2–B1 target (see SINGLE BIGGEST GAP below), which
is a validity failure a Rasinski-trained reviewer would flag immediately — a beautifully run
fluency routine on a passage two-to-three CEFR bands above the stated level doesn't measure what
it claims to measure. FDL's home-practice loop and text-derived word harvest are also simply
absent from L5 (defects #6, #7).

---

### SINGLE BIGGEST GAP

**Track B ("teen/adult") passages are written at Flesch-Kincaid grade 10–17, not the level's
stated A2–B1 target (~FK 3–6).** Measured with `textstat` on 7 sampled Track B passages spanning
the whole level:

| Session | Track B topic | FK grade | Flesch reading ease |
|---|---|---|---|
| 5.01 | Water cycle (farmer framing) | 10.4 | 58.7 |
| 5.07 | Interest/compounding/budget | 14.6 | 34.9 |
| 5.11 | Solar system scale | 11.4 | 55.3 |
| 5.13 | Simple machines (crowbar/wheelbarrow) | 13.5 | 51.2 |
| 5.14 | Internet packets/routing | 17.3 | 25.1 |
| mastery-check Part 4 | Negotiating a fair price (the actual scored cold-read) | 14.5 | 38.8 |

For comparison, Track A passages in the same sessions score FK 4.4–5 (appropriate). CEFR
A2≈FK 3–4, B1≈FK 5–6, B2≈FK 7–9; FK 10–17 is upper-high-school-to-graduate-level native prose —
C1/C2 territory, not A2–B1. This isn't a borderline call: it's driven by real, measurable
features — long em-dash-chained multi-clause sentences, semicolons, nested subordination
("This arrangement means you're supporting only part of the load's weight yourself — the wheel
and the ground assist with the rest, which is why..."), and untaught low-frequency vocabulary
(*discretionary, anchored, accumulated, self-reinforcing, consequential, infrastructure,
instantaneity, double coincidence of wants*) that a learner with the level's own stated
~2,000–3,000 word-family vocabulary (README §Exit) has no realistic path to.

This single defect invalidates three separate claims in the level's own contract simultaneously:
1. README §Exit's "~100+ WCPM with good prosody on an A2–B1 level passage."
2. Every session's "same target patterns... adult track contains nothing child-coded" claim
   (DESIGN.md rule 6) — Track B doesn't fail rule 6's "not childish" half, it fails the unstated
   other half: staying *at the taught level* rather than jumping several CEFR bands past it.
3. **mastery-check.md Part 4 is the actual instrument used to certify a learner ready for Level
   6** — its Track B passage (FK 14.5) is the least appropriate of all seven sampled, meaning the
   level's own gate-keeping check is testing something other than what it says it's testing. An
   adult ESL learner who has genuinely mastered everything L5.01–5.16 teaches could still fail
   Part 4 for reasons that have nothing to do with decoding, fluency, or the level's morphology
   content — pure vocabulary/syntax overload from an unlevelled passage.

The DESIGN.md-honest, evidence-cited tone throughout this level (the README's own §1 "what's
honest and what's not") makes this worse, not better: the level goes out of its way to caveat
soft claims (Reader's Theatre's 17-WCPM figure, the incomplete Hasbrouck-Tindal table, the
non-research-ranked root/suffix lists) while never once flagging that its own Track B passages
were never run through a readability check against the level's stated CEFR band.

---

### Numbered defect worklist (priority order)

1. **[CRITICAL] Track B readability across the level.** Files: every
   `course/level-5/lessons/L5.0*-*.md` and `L5.1*-*.md` Track B section, plus
   `course/level-5/mastery-check.md` Part 4 Track B ("Negotiating a Fair Price"). Fix: rewrite
   every Track B passage to FK grade 5–7 (short-to-medium sentences, minimal subordination,
   no more than one em-dash clause per sentence). Either simplify or explicitly pre-teach as
   Tier-2/3 vocabulary before use: *discretionary, anchored (in negotiation sense), accumulated,
   self-reinforcing, consequential, infrastructure, instantaneity, double coincidence of wants,
   generalized purchasing power*. Re-run every Track B passage through a readability tool
   (`textstat.flesch_kincaid_grade`) before shipping and record the score in the lesson file
   itself, the same way WCPM/prosody scores are logged — this level already has the instinct
   (§1's honesty list) to self-audit; it just never pointed that instinct at its own passages.

2. **[HIGH] Tier-2 word-count error + incomplete cumulative list.**
   Files: `course/level-5/lessons/L5.16-review-integration-capstone.md` (Goal line "Tier-2
   review: all 16 words," and the word list in §2, which runs `gradually...exotic` and skips
   straight from *essential, moderate* to *enormous, distant*); `course/level-5/mastery-check.md`
   Part 2 ("6 of the level's 26 Tier-2 words"). The level actually teaches 30 Tier-2 words
   (2 per session × 15 sessions, 5.01–5.15) — the L5.16 list is missing *resource, widespread*
   (taught 5.09) and *intense, moisture* (taught 5.10). Fix: add the 4 missing words into the
   L5.16 §2 list in their correct session-order position, and change both "16" (L5.16 Goal line)
   and "26" (both files) to 30 — or drop the exact number and say "every Tier-2 word taught this
   level" to stop this from drifting again if a session's vocab count ever changes.

3. **[MEDIUM] Factual error: antibody is not a cell.**
   File: `course/level-5/lessons/L5.14-anti-mid-under-roots-internet.md`, anti- table,
   row `antibody | a cell that works against disease`. An antibody is a protein
   (immunoglobulin) produced by immune cells (B cells/plasma cells) — it is not itself a cell.
   Fix: change to `a protein your immune system makes that works against disease` (or `a
   defense protein made by your immune system`).

4. **[MEDIUM] No self-correction/close-approximation drill anywhere in the level.**
   REWARDS Intermediate's preskill Activity F explicitly trains this: the teacher deliberately
   mispronounces a decoded word in a sentence (e.g., stressing the wrong syllable — "We stayed
   in a *hot el*"), and the learner must produce the correct pronunciation using sentence
   context — training the exact "close approximation → real word" self-monitoring step that
   sits between decoding and fluent reading. Every L5 Word Work block (README §3 step 2) goes
   straight from "decode + spell + meaning-check" to the next word; nothing trains recovering
   from a plausible-but-wrong pronunciation of a real multisyllabic word. Fix: add one line to
   the Word Work template in README §3 and to each lesson's Word Work section: a 1-minute "fix
   my mistake" round using 2 of that day's words, read aloud with the stress or vowel wrong,
   learner corrects using the sentence.

5. **[MEDIUM] No timed automaticity/rate drill on the affixes themselves.**
   REWARDS Activity G explicitly drills prefix/suffix *pronunciation speed*, not just accuracy
   inside whole words — directly serving the level's own strongest cited evidence (Goodwin &
   Ahn 2013, d=0.59 for decoding, the largest morphology effect of any outcome — research/05 §1,
   quoted in course/level-5/README.md §"Why this level exists"). Every L5 session's Check
   (§5 in each lesson) is untimed ("read and spell," "give one example word for each root").
   Fix: add an optional 20–30 second timed round to the Retrieval warm-up template (README §3
   step 1): "how many of today's + last session's affixes can you name correctly in 30 seconds?"

6. **[LOW-MEDIUM] No home-practice / family-involvement loop.**
   Rasinski's FDL steps 9–10 (take the passage home, reread to a parent/family member, return
   and reread to the teacher) are the specific mechanism that gives struggling readers extra
   practice reps outside the session, without repeating the same text to death inside it —
   which is exactly the gap left by L5's own Wide-FORI design choice (README §4, "the fix is
   not... read this same passage five more times"). Right now that design choice has no
   compensating extra-practice mechanism at all for a learner who's below target. Fix: add one
   line to the session template close (README §3 step 6 or a new step 7): "optional — reread
   today's passage once more at home, to a family member or aloud to yourself, before next
   session."

7. **[LOW] Word-study lists are disconnected from that session's own fluency text.**
   Rasinski's FDL "Word Harvest" step pulls 5–10 words directly from the passage just read for
   word study, building ownership of that specific text. In L5, the affix example-word tables
   are curated independently of the day's knowledge passage (e.g., L5.01's *un-/re-* word list
   — *unhappy, unfair, undo, rewrite, redo, return*, etc. — shares no words with that session's
   water-cycle passage). Fix: not a redesign — add one bonus line per Word Work block: "find one
   more [today's affix] word inside today's passage, if there is one."

8. **[LOW] `log/logy` root entry conflates two related-but-distinct senses.**
   File: `course/level-5/lessons/L5.15-ity-ist-roots-silk-road.md`, root table, `log/logy` row:
   lists *biology, geology* (the "-logy = study of" sense) and *dialogue* (the "log = word/speech"
   sense, from Greek *logos*) under one undifferentiated meaning ("study/word"). Not wrong, but
   imprecise enough that a learner could think "dialogue" means "a study." Fix: split into two
   short glosses in the same cell — "*-logy* at the end of a word = 'study of' (biology,
   geology); *log/logue* elsewhere = 'word/speech' (dialogue, monologue)."

9. **[LOW] The -tion/-sion spelling rule given doesn't cover one of its own six examples.**
   File: `course/level-5/lessons/L5.07-tion-sion-able-ible-money-deeper.md`, §"-tion/-sion" intro
   line: "it's usually -tion after t or a base ending in -te... usually -sion after d or s" — but
   the table's own example `information | facts that inform | inform + ation` has a base ending
   in "m," matching neither stated rule, and uses the unstated "-ation" variant. Fix: add one
   clause: "...and -ation after most other endings (inform → information)."

10. **[LOW] Inconsistent example-word depth for the `ver` root.**
    File: `course/level-5/lessons/L5.15-ity-ist-roots-silk-road.md`, root table: `ver` gets only
    2 example words (*verify, verdict*) vs. 3–4 for every other root in the same table. Not an
    error, just an inconsistency; low priority. Fix (optional): add one more transparent example
    if one exists at this level's vocabulary band, or leave as-is and note in a comment that 2 was
    a deliberate minimum, not an oversight.

## Round 1 builder

**Fixed all 10 numbered defects from Round 1 critic.**

### 1. [CRITICAL] Track B readability — FIXED
Every Track B passage in all 16 lessons (L5.01–L5.16) and both tracks of
`mastery-check.md` Part 4 were rewritten in short, plain sentences and re-measured
with `textstat.flesch_kincaid_grade()`. Score recorded directly under every
passage, same discipline as WCPM/prosody logging. Before → after (the 6 originally
sampled, plus two more re-checked since they were also load-bearing):

| Session | Before FK | After FK |
|---|---|---|
| 5.01 | 10.4 | 5.2 |
| 5.02 | (not sampled; rewritten anyway) | 5.7 |
| 5.03 | (not sampled) | 4.7 |
| 5.04 (RT script) | (not sampled; measured this round: dense) | 4.9 |
| 5.05 | (not sampled) | 4.5 |
| 5.06 | (not sampled) | 5.8 |
| 5.07 | 14.6 | 5.1 |
| 5.08 (RT script) | measured this round: 7.4 | 4.6 |
| 5.09 | (not sampled; measured this round: high) | 5.4 |
| 5.10 | (not sampled) | 3.8 |
| 5.11 | 11.4 | 4.8 |
| 5.12 (RT script) | measured this round: 4.8 (already close; tightened) | 4.8 |
| 5.13 | 13.5 | 4.4 |
| 5.14 | 17.3 | 4.6 |
| 5.15 | (not sampled; measured this round: 27.7 on one paragraph!) | 5.5 |
| 5.16 | measured this round: 27.7 (worst in the whole level) | 5.6 |
| mastery-check Part 4 Track B | 14.5 | 5.2 |
| mastery-check Part 4 Track A | not flagged, but measured this round: 6.9 | 4.2 |

All 18 measured passages now sit inside FK 3.8–5.8, within the level's A2–B1
target of FK 3–6. Method: draft in plain short sentences, common words, minimal
subordination and no more than one em-dash clause per sentence (per the critic's
prescription), measure with a local textstat venv, iterate until in range, then
paste into the lesson with the score recorded.

**Known residual gap, logged not hidden:** the critic's worklist scoped this fix to
Track B only. A spot-check of a few Track A passages this round (L5.09's original,
mastery-check Part 4 Track A) found some also running well above the A2 target
(one at FK 12.3) — Track A was in scope for the mastery-check (fixed, now 4.2) but
left alone elsewhere since the critic's file list named Track B specifically.
**Flag for Round 2: audit and fix Track A readability across all 16 lessons** —
the same discipline (measure, don't assume) needs to be pointed at Track A too.

### 2. [HIGH] Tier-2 word-count error — FIXED
L5.16 §2 and Goal line, and `mastery-check.md` Part 2, now say **30** (not 16 or
26) and list all 30 words in teaching order, including the previously-missing
*resource, widespread* (5.09) and *intense, moisture* (5.10). Confirmed count:
2 words × 15 sessions (5.01–5.15) = 30.

### 3. [MEDIUM] Antibody factual error — FIXED
`L5.14`'s anti- table now reads "a protein your immune system makes that works
against disease" instead of "a cell."

### 4. [MEDIUM] Self-correction / close-approximation drill — ADDED
New drill added to the README §3 session template (Word Work step) and to every
one of the 16 lessons: a 1-minute "fix my mistake" round where the tutor
mispronounces one of today's target words (wrong stress or vowel) inside a
sentence, and the learner corrects it using context — the same mechanism as
REWARDS Intermediate's preskill Activity F.

### 5. [MEDIUM] Timed affix-automaticity drill — ADDED
New 20–30 second timed round added to the README §3 Retrieval warm-up step and to
every lesson (5.01 explicitly notes there's nothing to time yet, being the first
session): "how many of today's + last session's affixes can you name in 30
seconds?" — directly serving the level's own strongest cited effect (Goodwin & Ahn
2013 d=0.59 decoding).

### 6. [LOW-MEDIUM] Home-practice / family-involvement loop — ADDED
New line added to the end of every lesson's Check section and to README §3 step 7:
"optional — reread today's passage once more at home, to a family member or aloud
to yourself, before next session" — Rasinski's FDL steps 9–10, the compensating
mechanism for the level's Wide-FORI "don't re-drill" design choice.

### 7. [LOW] Word harvest — ADDED
New bonus line added to every lesson's Word Work section and to README §3 step 2:
"find one more [today's affix/root] word inside today's passage" — ties the
curated word list back to the specific text just read, Rasinski's FDL "Word
Harvest" step. Where no genuine match exists in a given session's passage, the
lesson says so honestly rather than forcing one (5.05, 5.11, 5.13, 5.15 all have at
least one honest "none this session" note).

### 8. [LOW] log/logy conflation — FIXED
`L5.15`'s root table now separates the two senses explicitly: "*-logy* at the end
of a word = 'study of' (biology, geology); *log/logue* elsewhere = 'word/speech'
(dialogue, monologue)" — added as a dedicated note below the table, not just a
table-cell edit, since it needed room to explain both senses clearly.

### 9. [LOW] -tion/-sion rule gap — FIXED
`L5.07`'s intro line now adds the missing clause: "...and it's usually *-ation*
after most other endings — *inform* → *information* is the clearest example in
today's list."

### 10. [LOW] ver root thin example set — FIXED
Added *verity* and a "fun fact" note that *very* itself derives from the same
Latin root (*verus*, "true"), with its meaning having drifted over centuries — an
honest example of a root not perfectly predicting a modern word's meaning, rather
than force-fitting a fourth unrelated example.

### DESIGN.md §4 "Prime the topic" step — APPLIED
Every one of the 16 lessons now has a new "Prime the topic" section (3–5 min)
inserted between Word Work and the Fluency & Knowledge Text block, matching the
updated session template in README §3: 2–3 quick facts about the day's topic plus
one orienting question linking it to what the learner already knows, run *before*
the passage (IES Rec 3A). All subsequent section numbers were renumbered
consistently across all 16 files (verified: every file now runs
1 Retrieval warm-up → 2 Word work → 3 Prime the topic → 4 Fluency & Knowledge Text
→ 5 Write to read → 6 Check, with L5.16 running one extra numbered step for its
Extensive reading capstone).

### Verification performed
- Every Track B (and, for the mastery check specifically, Track A) passage
  measured with a local `textstat` venv (`pip install textstat` was blocked by the
  system Python; used `python3 -m venv` + `pip install` inside it instead).
- Grepped the whole level for residual references to vocabulary/phrases removed
  during Track B rewrites (*double coincidence of wants*, *generalized purchasing
  power*, *self-reinforcing*, *discretionary*, *instantaneity*, *consequential*,
  *infrastructure*) — found and fixed one stale Tutor-notes reference in L5.15;
  confirmed no others remain.
- Grepped all 16 lesson files for presence of all 5 new structural elements
  (Timed affix round, Self-correction drill, Word harvest, Prime the topic,
  Optional home practice) — confirmed exactly 1 occurrence of each in every file.
- Confirmed section numbering is internally consistent (1→6, or 1→7 for L5.16) in
  every file after inserting the new Prime-the-topic step.

### Not done this round (flagged for Round 2)
- Track A readability audit across all 16 lessons (see defect #1 residual gap
  above) — only the mastery-check's Track A was fixed, since it's the actual
  certifying instrument; the other 16 Track A passages were not in this round's
  scope and have not been measured.
- Defect #10's "or leave as-is" option wasn't taken — a third *ver* example was
  added instead, since a genuine, honest one existed (*very*, with its meaning-drift
  caveat) rather than needing to force a weak fit.

### Track A residual gap (flagged above as "not done this round") — now FIXED

All 16 Track A passages (L5.01–L5.16, including the three Readers Theatre scripts'
Track A casts) have been rewritten to short, plain sentences and re-measured with
the same `textstat` venv used for Track B. Knowledge content (facts, topic, plot in
the RT scripts) was preserved exactly — only sentence length and clause complexity
changed. FK score recorded under every passage, same as Track B.

| Session | Before FK | After FK |
|---|---|---|
| 5.01 | 4.4 (already fine) | 4.4 |
| 5.02 | 8.5 | 3.8 |
| 5.03 | 6.7 | 2.1 |
| 5.04 (RT script) | 6.4 | 4.3 |
| 5.05 | 6.5 | 3.9 |
| 5.06 | 9.7 | 4.0 |
| 5.07 | 8.0 | 3.1 |
| 5.08 (RT script) | 4.7 (already fine) | 4.7 |
| 5.09 | 12.3 | 3.8 |
| 5.10 | 8.2 | 3.7 |
| 5.11 | 10.8 | 3.6 |
| 5.12 (RT script) | 6.2 | 4.1 |
| 5.13 | 10.6 | 3.8 |
| 5.14 | 11.8 | 3.5 |
| 5.15 | 13.1 | 4.0 |
| 5.16 | 11.2 | 4.4 |

All 16 now sit inside FK 2.1–4.7 — comfortably within the FK 2–5 kids'-A2 target
(tighter than Track B's FK 3–6 band, appropriately, since Track A is written for a
child reader). Two passages (5.01, 5.08) were already in range and needed only the
score recorded, not a rewrite.

**Method:** extracted each Track A passage's underlying text with a small Python
script (stripping phrase-cue `/` marks, blockquote `>` markers, and — for the three
Readers Theatre scripts — character-name labels and stage directions in
parentheses — before measuring, since raw script/phrase-cue markup would distort
`textstat`'s sentence-boundary detection), measured, rewrote in short
subject-verb-object sentences with minimal subordination, re-measured, iterated.

**Side effects caught and fixed during this pass:**
- Several "word harvest" notes referenced specific words (*transported, structure,
  overlook, misplace, decision*, etc.) that a rewrite had removed or changed —
  each one was checked against the final passage text and either corrected to a
  word that still appears, restored (e.g. *construct* was deliberately kept in
  L5.12's closing line, since it cost nothing in FK terms and preserved the root
  pun), or changed to an honest "none this session" note where nothing survived.
- L5.05's rewrite initially replaced *predict* with *guess* to shorten a sentence —
  caught and reverted, since *predict* is that session's Tier-2/root-preview word
  and needed to stay in the passage on purpose.

No further residual gaps remain in this level's readability audit — both tracks,
all 16 lessons, plus the mastery check, are now measured and within target.

---

## Round 2 critic

**Reviewed:** the builder's Round 1 fix pass — all 10 defects claimed fixed, Track A/B
readability rewrite, self-correction drill, timed affix-rate drill, home-practice loop,
word harvest. Fresh eyes, no loyalty to Round 1's framing.

### Fix verification (independent re-measurement)

Re-measured 8 passages myself with a fresh `textstat` venv (own extraction script, not
the builder's), covering 4 lessons across both tracks plus the mastery check's scored
instrument:

| Passage | Claimed FK | Independently measured FK |
|---|---|---|
| L5.01 Track A (water cycle) | 4.4 | 4.36 ✓ |
| L5.01 Track B (water cycle, farmer) | 5.2 | 5.17 ✓ |
| L5.07 Track A (saving money) | 3.1 | 3.1 ✓ |
| L5.07 Track B (interest/compounding) | — | 5.1 (in-band) |
| L5.09 Track A (Indus city) | 3.8 | 3.8 ✓ |
| L5.09 Track B (Indus trade) | — | 5.4 (in-band) |
| L5.14 Track A (message journey) | 3.5 | 3.5 ✓ |
| L5.14 Track B (packets/routing) | — | 4.6 (in-band) |
| mastery-check Track A (market) | 4.2 | 4.2 ✓ |
| mastery-check Track B (negotiating, the scored instrument) | 5.2 | 5.2 ✓ |

**Fix holds.** Every sampled passage — including the actual certifying instrument —
is inside the claimed 2.1–4.7 (Track A) / 3.8–5.8 (Track B) bands, and the
single most consequential prior defect (mastery-check Part 4 at FK 14.5) is now FK
5.2. The Round 1 "single biggest gap" is genuinely closed, not just narrated as
closed.

**Word-harvest cross-checks held up under spot audit.** L5.07's harvest note claims
*decision* appears in Track A's last paragraph — confirmed, line 121. L5.09's and
L5.14's honest "no clean match" notes were checked against their actual rewritten
passages and are accurate (no orphaned reference to pre-rewrite vocabulary found in
either).

**Facts spot-checked, all correct:** heart (4 chambers, fist-sized, pump, ~60s per
circulation loop, resting HR 60–100 bpm — L5.03); water cycle (evaporation →
condensation → precipitation → runoff, reservoir framing — L5.01); Indus Valley
(standardized weights/bricks, undeciphered seal script found as far as Mesopotamia,
~4,500 years ago, correctly hedged as still-undeciphered — L5.09); money (simple vs.
compound interest, "interest earning interest," budget priority order — L5.07). The
antibody fix (protein, not cell — L5.14) is correct. Tier-2 count of 30 is now
internally consistent between L5.16 and mastery-check Part 2 (confirmed by grep, both
say 30).

**Track A stayed genuinely child-appropriate and Track B stayed genuinely adult** in
every sampled passage — topics (banking, geopolitical trade, network routing,
negotiation tactics) are adult throughout Track B, with no talking-animal or
kid-coded framing creeping in from the simplification pass.

### New defect found this round — the readability fix bought naturalness problems in at least one passage

**[MEDIUM] L5.14 Track B ("Packets, Routing...") reads as a list of short declaratives
rather than natural adult speech**, e.g. "It also carries an address. The address says
where it came from. It says where it is going. It says where it fits in the order,"
and later "Maybe some packets are delayed. Maybe they arrive out of order. Maybe some
are lost completely... It can happen if a router gets overloaded. It can happen if a
connection drops." This is the FK-lowering technique (short subject-verb-object
sentences, minimal subordination) pushed hard enough to produce repetitive anaphora
("It says... It says...", "Maybe... Maybe...", "It can happen... It can happen...").
For a *fluency* program specifically, this matters more than it would in a plain
comprehension text: the Model step's whole job is to demonstrate natural expressive
prosody, and stilted, listy prose gives the learner a worse prosody target even though
its FK score is in-band. Spot-checked five other rewritten Track B passages (L5.07,
L5.09, L5.11, L5.13, mastery-check) and found this pattern only in L5.14 — it is
localized, not systemic, but it is real. Fix: read L5.14 Track B aloud; anywhere three
consecutive sentences share the same subject+verb opening, combine or vary two of
them (e.g. "It says where it came from, where it's going, and where it fits in the
order" — still short, still in-band, no longer anaphoric).

### VERDICT

**Comparison 1 — Morphology (L5.02) vs. REWARDS: OURS WINS, unchanged and unharmed.**
The Round 1 fix pass touched only the fluency-passage tracks; word-work tables,
dictation lists, and spelling-rule explanations in L5.02 (and the other sampled
morphology sections) are byte-for-byte the content Round 1 already scored as a win.
Confirmed by direct read, not assumption.

**Comparison 2 — Fluency/Readers Theatre program vs. Rasinski's FDL: OURS WINS (flipped
from Round 1).** Fetched the actual 10-step FDL routine this round (Landmark Outreach's
summary, cross-referencing timrasinski.com): (1) reread yesterday's passage, (2) teacher
models new text 2–3×, (3) discuss passage + how it was read, (4) choral reading, (5)
paired practice, (6) individual/group performance for an audience, (7) select 4–10
words for a word bank, (8) word-study activities, (9) home practice + perform for
family, (10) next-day accuracy check. Against this: L5 now has model→echo/choral→
partner (steps 2, 4, 5), a word harvest tied to the day's actual text (step 7, though
narrower — one word, not a bank of 4–10), a self-correction drill Rasinski's version
doesn't have at all, a home-practice loop naming a family member (step 9), and
Readers Theatre's own genuine advantage over vanilla FDL — no memorization, honest
"we don't know" framing on open historical questions — that a Rasinski-trained
reviewer would have no answer for. Round 1's fluency loss was entirely about
validity (a beautifully run routine measuring the wrong thing on an unlevelled
passage) — with that fixed, the comparison now favors ours on breadth without giving
up anything FDL uniquely does well, except the two items below.

### SINGLE BIGGEST GAP (Round 2)

**Performance-for-an-audience — FDL step 6 — only happens in 3 of 16 sessions (the
Readers Theatre lessons 5.04/5.08/5.12).** In the other 13 sessions, the "independent"
read is a private timed WCPM+prosody check by the tutor, not a performance in any
sense a learner would recognize as one. Rasinski's FDL treats performing for *some*
audience (class, peer, recording) as a load-bearing, every-single-day mechanism — it's
the payoff that makes the whole rehearsal cycle feel purposeful rather than like a
test. A learner doing L5 gets that payoff only 3 times across 16 sessions; the other
13 sessions' fluency work ends at "the tutor scored it," which is a flatter motivational
arc than FDL's daily small-performance structure, especially for the teen/adult
audience this level explicitly built RT to serve. Fix: in the 13 non-RT sessions, reframe
the independent read as a tiny performance (read it once more, to a phone recording, a
sibling, or just "as if someone were listening") *before* scoring WCPM off a second,
unannounced read — cheap to add, keeps the existing scored instrument untouched, and
closes the one FDL mechanism this level still doesn't do daily.

### Numbered defect worklist (priority order)

1. **[MEDIUM] L5.14 Track B anaphoric/listy prose** — see above. Rewrite for
   sentence-opening variety while staying in the FK 3.8–5.8 band. Spot-check the
   remaining 8 Track B passages not sampled this round (5.02, 5.03, 5.04 RT, 5.05,
   5.06, 5.08 RT, 5.10, 5.12 RT, 5.15, 5.16) for the same pattern — only 6 of 16 have
   now been read in full for naturalness (5.01, 5.07, 5.09, 5.11, 5.13, 5.14 +
   mastery-check); the other 10 have only had their FK score checked, not their
   prose read for stiltedness.
2. **[MEDIUM] Daily performance framing missing from 13/16 sessions** — see SINGLE
   BIGGEST GAP above. Add a one-line "perform this once more, out loud, to someone
   or something, before the scored read" step to the Fluency & Knowledge Text section
   of every non-RT lesson (5.01–5.03, 5.05–5.07, 5.09–5.11, 5.13–5.16) and to the
   README §3 sequence description.
3. **[LOW] Word harvest is single-word and non-cumulative** — FDL builds a running
   4–10-word bank per text that stays visible for review; L5's harvest surfaces one
   word and moves on. Given the level already carries a full curated affix/root table
   per session (arguably stronger than FDL's ad hoc word bank), this is a nice-to-have,
   not a defect worth blocking on — noting it for completeness rather than adding it
   to a "must fix" list.

**Fix-verification confidence: high.** All 10 Round 1 defects independently confirmed
fixed on the sampled lessons; no reopened defects. Two new, smaller-scope defects found
this round (both MEDIUM, neither invalidating the level's core claims the way Round 1's
gap did).

## Round 2 builder

Fixed both items from Round 2 critic's numbered worklist.

### 1. [MEDIUM] L5.14 Track B anaphoric/listy prose — FIXED

Rewrote the passage to remove the three repetitive chains the critic flagged:
- "It says where it came from. It says where it is going. It says where it fits
  in the order." → "That address shows where the data came from, where it is
  going, and where it fits in the order." (one sentence, three-item list, still
  short).
- "Maybe some packets are delayed. Maybe they arrive out of order. Maybe some are
  lost completely." → "A few packets might get delayed, arrive out of order, or
  get lost completely." (one sentence).
- "It can happen if a router gets overloaded. It can happen if a connection drops
  for a moment." → "This usually happens because a router along the way gets
  overloaded, or a connection drops for a moment." (one sentence).
- "A weak connection can cause this. A busy network can cause this too." → "A
  weak connection can cause this. So can a busy network." (kept as two sentences
  deliberately — this is a natural, non-anaphoric variation, not a chain).

Re-measured: **FK 5.7 · Flesch reading ease 72.5** (was FK 4.6) — still inside the
FK 3–6 target band; the small FK increase is expected and correct, since combining
short listy sentences into slightly longer ones with internal lists is exactly the
naturalness trade the critic asked for, and 5.7 leaves headroom before the 6.0
ceiling. Comprehension questions re-checked against the new text — both still
answerable without edits.

**Spot-checked the 10 remaining Track B passages not yet read for naturalness this
round** (5.02, 5.03, 5.04 RT, 5.05, 5.06, 5.08 RT, 5.10, 5.12 RT, 5.15, 5.16), per
the critic's own worklist item 1 instruction to do so. Read each in full, not just
FK-scored. **No other instance of the same three-consecutive-same-opening pattern
found.** Two passages use a deliberate two-sentence echo for rhythm/emphasis
(5.10: "A weak connection... So can a busy network" pattern doesn't recur
elsewhere; 5.16's "Water rises and falls again. Blood moves in a loop.
Electricity flows in a loop too." is three short parallel sentences, but each
names a different subject and verb, which is the "same idea in different
domains" rhetorical point of that specific paragraph — not stilted repetition of
one subject, and it's read-aloud-natural, closer to a deliberate list-of-examples
cadence). Nothing else needed a rewrite.

### 2. [MEDIUM] Daily performance framing missing from 13/16 sessions — FIXED

Added a **Perform it** step (1–2 min) to the Fluency & Knowledge Text section of
all 13 non-Readers-Theatre lessons: 5.01, 5.02, 5.03, 5.05, 5.06, 5.07, 5.09,
5.10, 5.11, 5.13, 5.14, 5.15, 5.16. Placement: after Assisted (echo/choral/
partner), before the timed, scored Independent read — the learner reads the
passage once more aloud to a real or imagined audience (family member, tutor,
sibling, or a voice note to a friend) as a small performance, then the actual
scored read happens as a second, unannounced read straight after. Each lesson
names one concrete thing to aim for, alternating session to session between
"phrasing that follows the punctuation" and "expression that matches the
content," so the tip itself doesn't become another rote repetition.

Confirmed by grep: exactly 13 lessons contain "Perform it" (5.13 has two
mentions — heading + body — by design), and the 3 Readers Theatre lessons
(5.04, 5.08, 5.12) correctly have zero, since their own Rehearsal→Performance
structure already provides this mechanism natively.

Also updated:
- **README §3** session template: step 4 now reads "Model → Assisted → **Perform
  it** (1–2 min, non-RT sessions only) → Independent read," with a full paragraph
  explaining the mechanism, why it was added (RT's performance payoff was
  happening in only 3 of 16 sessions), and its relationship to Rasinski's FDL
  step 6 (performing for an audience).
- **README §4** fluency sequence: renumbered Model/Assisted/Independent to
  Model/Assisted/**Perform it**/Independent as a 4-step sequence, with an
  explicit note that the performance read and the scored read are two separate
  reads — performing doesn't get scored, the read that follows it does. Also
  updated the Wide-FORI paragraph's shorthand reference to match the new 4-step
  scaffold name.

### Verification performed

- Re-measured L5.14 Track B with the same textstat venv: FK 5.7, in-band.
- Read all 10 previously FK-only-checked Track B passages in full for naturalness
  (not just re-running textstat) — see above, no further rewrites needed.
- Grepped all 16 lesson files for "Perform it" — confirmed 13 non-RT lessons have
  it, 3 RT lessons correctly don't.
- Re-read L5.14's comprehension-check questions against the rewritten passage —
  both remain directly answerable from the new text; no question changes needed.

### Not reopened

Round 2's item 3 (word harvest is single-word, non-cumulative, vs. FDL's running
4–10-word bank) was explicitly logged by the critic as a nice-to-have, not a
defect worth blocking on — left as-is per the critic's own recommendation.
