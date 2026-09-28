# Level 0 — Critic Rounds Log

## Round 1 critic — 2026-09-28

Reviewed: `start-here.md`, `placement-test.md`, `screener.md`, `urdu-speakers.md`,
`guide-tutors-parents.md`. Checked against `DESIGN.md` §2 rules, `research/03`, `research/04`,
`research/07`, and primary external instruments fetched live this round: UK Phonics Screening
Check (PSC) 2024 official scoring guidance (assets.publishing.service.gov.uk), the real PAST
(Phonological Awareness Screening Test, Kilpatrick, Forms A–D, thepasttest.com), DIBELS 8th
Edition Administration and Scoring Guide (dibels.uoregon.edu), and Hasbrouck-Tindal (2017)
compiled ORF norms (ERIC ED594994).

---

### VERDICT — blind comparisons

**Comparison 1: our Stage 3 decoding-ladder pseudoword design vs. the real PSC pseudoword
section.** **REFERENCE (PSC) WINS.** PSC's official scoring guidance gives, for every
pseudoword, three things: a full IPA transcription, a named real word the onset/rime sound is
drawn from ("this item uses the 'n' from 'net' and rhymes with 'mop'"), and explicit sign-off
that all regional pronunciations are acceptable. Our `placement-test.md` Stage 3 gives only an
ad hoc slash respelling ("/dif/", "/gan/") with no IPA, no real-word anchor, and no regional
guidance — and the respelling convention is internally inconsistent (see defect #3). A reading
specialist stripped of labels would hand a non-specialist Pakistani parent the PSC-style card,
not ours, because it is the only one that actually tells an untrained tester how to say the
target sound.

**Comparison 2: our Stage 1 oral-PA ladder vs. the real PAST.** **REFERENCE (PAST) WINS.** The
real PAST has no rhyme-judgment section and no pure-blending section at all — it is built
entirely from syllable-level compound-word deletion → onset-rime deletion/substitution →
phoneme deletion/substitution, and every item is scored on two axes: correct AND automatic
(answered within ~3 seconds). Kilpatrick built it this way deliberately: rhyme judgment and
simple blending hit a ceiling early and stop discriminating struggling readers past
kindergarten — exactly the population (older children, teens, adults) this course says it is
built for. Our Stage 1 tests rhyme + blend + segment + simple first/last-sound deletion, with
binary correct/incorrect scoring only — no automaticity dimension, no substitution items, no
syllable-level items. A specialist placing an adult non-reader would reach for PAST's ladder,
not ours.

---

### SINGLE BIGGEST GAP

**The Stage 4 ORF pass/fail gates are not valid as constructed, because passage difficulty is
not matched to the grade-level source of the WCPM norms being cited against them.** Measured
Flesch-Kincaid grade levels of the course's own three passages: Passage A ≈ grade 2.4, Passage
B ≈ grade **10.2**, Passage C ≈ grade **14.4** (computed this round from the actual passage
text in `placement-test.md`). Hasbrouck-Tindal's WCPM norms are derived from controlled,
grade-appropriate basal passages — a "Grade 3, 50th percentile = 112 WCPM" number is only
meaningful when the passage read is actually grade-3-difficulty text. Passage C's benchmark of
"≥100 WCPM ... indicates readiness for Level 6" is drawn from roughly the Grade 3–4 band of the
2017 Hasbrouck-Tindal table (Table 4: Gr3 Spring 50th = 112, Gr4 Fall 50th = 94) — but the
passage the learner is actually asked to read at that moment is college-entry-level prose about
electronic-voting policy trade-offs (14.4 FK grade, 23-word average sentence length, clauses
like "which matters more than speed when public trust is already fragile"). The same problem,
smaller, applies to Passage B (FK 10.2 vs. its ≥70 WCPM gate, roughly a Grade 2–3 norm). This
silently miscalibrates the exact gate that decides Level 5/6/7 entry, and it does so worst for
the population the course claims to serve best: an adult or ESL reader who decodes every word
correctly but reads long embedded clauses more slowly will be scored as if failing a
grade-3/4-appropriate fluency check, when the actual text they were handed was never
grade-3/4-appropriate to begin with. This is a DESIGN.md rule 12 (honest citations) problem
disguised as a design choice — the norm citation is real, but its application to these specific
passages is not.

---

### Defect worklist (prioritised, file + exact location + required fix)

1. **[HIGH] Stage 2 letter-sound table item count does not match its own scoring
   denominator.** `placement-test.md`, Stage 2 table (the 19-row, 2-column table listing
   letters/graphemes with target sounds) contains **38 scoreable items** (19 rows × 2 columns),
   not 32 — I recounted by hand twice. The Scoring sheet later in the same file states
   `Stage 2 — Letter-sound   Score /32     ≥90% (29+)?` — an unreconciled mismatch. Worse, the
   Stage 2 body text says "below 90% on single letters alone → placement is at/before Level 1"
   but the table never separates "single letters" from digraphs/vowel-teams/r-controlled
   graphemes — they're interleaved in the same right-hand column (e.g., `j, v, w, x, y, z, qu`
   sit in the same column as `sh, ch, th, wh, ng, ai, ee, igh, oa, ar, or, ow`). A tester
   literally cannot compute the "single letters alone" subscore the placement rule requires.
   **Fix:** restructure Stage 2 into three explicitly separated, separately-scored blocks —
   (a) single letters + qu, 26 items, matching DESIGN.md's Level 1 letter set exactly;
   (b) L2 digraphs (sh ch th wh ng), 5 items; (c) L3/L4 vowel teams + r-controlled (ai ee igh
   oa ar or ow), 7 items — and fix every downstream "/32", "29+" reference to the corrected
   denominators (26 for the single-letters subscore the placement rule actually needs).

2. **[HIGH] Stage 4 WCPM benchmarks are applied to passages far harder than the norm source's
   grade level (see Single Biggest Gap above).** `placement-test.md` lines ~244–298 (Passages
   A/B/C) and their WCPM benchmark lines (~252, ~272, ~296). **Fix:** either (a) rewrite
   Passages B and C to genuinely match grade-2/3 and grade-3/4 sentence complexity (shorter
   sentences, fewer embedded clauses, more common vocabulary) so the borrowed WCPM cut-scores
   are actually valid for the text being read, or (b) if the intent is deliberately harder,
   adult-register content (defensible per DESIGN.md rule 6), then stop citing Hasbrouck-Tindal
   grade-level WCPM norms as the pass/fail gate for these specific passages — compute or find a
   defensible adult-text WCPM benchmark instead, and say explicitly in the file that the
   standard grade-level norms don't transfer to this passage's actual difficulty. Report the
   FK-grade of each passage next to its WCPM target so a future reviewer can catch this
   automatically.

3. **[HIGH] Stage 1's PA ladder doesn't match what research/07 itself claims to have built it
   from, and drops the one dimension (automaticity) that research/07 explicitly promised.**
   `research/07-program-scopes-assessment.md` §5 (line ~202) states Stage 1 was built
   "following PAST's difficulty progression and correct/automatic scoring convention" as
   "(rhyme recognition → phoneme blending → phoneme segmentation → phoneme deletion)". Having
   now fetched the real PAST (thepasttest.com, Forms A–D), **this is not PAST's structure** —
   the real instrument has no rhyme section and no pure-blending section; it is entirely
   syllable-deletion → onset-rime-deletion/substitution → phoneme-deletion/substitution, scored
   on two axes (correct, and automatic = answered within ~3 seconds). `placement-test.md`
   Stage 1 (lines 45–110) then implements the mischaracterized ladder, and drops automaticity
   scoring entirely (binary ✓/✗ only) even though research/07 said it would keep it. This is a
   DESIGN.md rule 12 violation (a citation that doesn't match its primary source) compounding
   into a real construct-validity gap for exactly the readers (older children/teens/adults)
   PAST was built to serve better than rhyme/blend tasks. **Fix:** rebuild Stage 1 directly from
   the fetched PAST PDF: replace rhyme + blend with syllable-compound deletion and onset-rime
   deletion/substitution items at the easy end, add phoneme-substitution items (not just
   deletion) at the hard end, and add a second scoring column for automaticity (~3-second cutoff)
   at every level, matching the real PAST scoring sheet's Correct/Automatic split. Correct
   research/07 §5's description of PAST to match the primary source, or remove the specific
   claim if it isn't being followed.

4. **[MED] Pronunciation notation for Stage 3 pseudowords is internally inconsistent and less
   rigorous than the PSC standard (see Comparison 1).** `placement-test.md`, Tier 3 (lines
   184–196) and Tier 4 (lines 197–208): most pronunciations use an ad hoc phonetic respelling
   ("/kayk/", "/boht/", "/kyoot/"), but several instead just reuse a homophonous real English
   word's ordinary spelling as if it were self-evidently phonetic — e.g. pseudoword "fime" is
   glossed "/time/ (rhymes with 'time')" and pseudoword "spight" is glossed "/spite/" — mixing
   two different notation conventions in the same table with no explanation. Also inconsistent
   within Tier 4: "burn" is glossed "/burn/" (keeps the spelling) while "vurk" (same `ur`
   grapheme) is glossed "/verk/" (respells it) — a parent could reasonably read these as two
   different target sounds for the same grapheme. **Fix:** adopt one consistent convention
   course-wide — ideally the PSC pattern (name the real word each grapheme's sound is drawn
   from, plus a rhyme-word, e.g. "this item uses the 'th' from 'thin' and rhymes with 'shape'")
   rather than ad hoc slashes, and re-pass every pronunciation column in Stage 2/3 for
   consistency.

5. **[MED] `start-here.md` mis-cites Wanzek et al. (2013) — attributes a "frequency" finding to
   a study that actually found "group size" was the moderator.** `start-here.md` lines 75–79:
   "Research on older struggling readers found that more frequent shorter sessions with
   effectively 1-to-1 attention outperform long infrequent sessions with a big group... (research/03
   §5, Wanzek et al. 2013)." Checked against `research/03-orton-gillingham-structured-literacy.md`
   line 55 ("Group size was a significant moderator of comprehension outcomes... duration alone
   (more calendar weeks) was not sufficient without matched intensity/small group size") — the
   actual finding is about **group size** (1:1/small vs. large group), not session
   **frequency/length** (short-and-often vs. long-and-rare), which is the variable
   `start-here.md` claims was tested. These are different constructs and the file conflates
   them under one citation. **Fix:** rewrite the claim to say what Wanzek et al. actually found
   (small group size / 1:1-equivalent attention is the strongest lever for older strugglers) and
   drop or separately justify the "short and frequent" scheduling advice, which may be good
   practice but isn't what this citation supports.

6. **[MED] Stage 1's self-test protocol is not actually administrable by a solo adult for the
   item types that need it most.** `placement-test.md` lines 389–406, step 2: "For Stage 1
   (oral PA), record yourself on your phone saying each item's *answer* out loud after covering
   the answer column, then play it back and check." Stage 1b/1c/1d (blending, segmenting,
   deletion) are stimulus-response tasks — the tester must SAY the sounds/word aloud and the
   learner must produce the answer purely by ear, without seeing the item in print (this is the
   entire point of the "no cueing"/oral-only design). A solo adult who reads the "Sounds said"
   or "Word said" column with their own eyes to then "answer" it has already seen the print
   stimulus, which defeats the oral-only design, and "record your answer, then check against
   the key" is circular when you are simultaneously the item-writer and the respondent. The
   file's own fallback ("have anyone nearby read you the Item column") quietly concedes this
   doesn't work solo. **Fix:** either state plainly that Stage 1b/1c/1d require a second person
   (a friend, family member, or even a stranger reading down the list) and cannot be
   truly solo-administered, or build a companion audio file/TTS script that speaks the stimuli
   aloud in randomized order so a solo adult has a genuine "someone else says it" stand-in.

7. **[LOW] `screener.md` has a duplicated list number.** Lines ~76–90, "If flagged: what to
   do" section: two consecutive items are both numbered "2." ("2. Expect the pace to matter
   more..." and "2. Seek a formal evaluation if you can..."), the following items continue "3.",
   "4." — a straightforward authoring slip. **Fix:** renumber to 1–4 sequentially.

8. **[LOW] Comprehension-question #4 for Passage A is labeled "inferential" but is answerable by
   local sentence integration alone, not real inference beyond the text.** `placement-test.md`
   line ~258: "Why do you think Rana wrote the man's name down?" — the passage states in the
   very next clause "she would order more soap for next week," so the "inference" is really
   just linking two adjacent clauses, not drawing on outside knowledge. Minor at A2 level, but
   worth a pass across all three passages to make sure "inferential" items actually require
   inference once Stage 4 is next revised for defect #2.

9. **[LOW, note not necessarily a fix] Stage 4's ORF passages are uniformly adult-register civic
   content (shop economics, electricity bills, electronic-voting policy) with no Track A/Track B
   split, unlike every Level 1–7 lesson text.** This is defensible as a deliberate,
   explicitly-stated design choice (`placement-test.md` line 236: "nothing in any passage is
   written for children specifically") to keep one universal instrument, but it does mean a
   child who reaches Stage 4 is tested on unfamiliar civic/economic vocabulary ("council",
   "tally", "ballots", "stock") that could depress a fluency+comprehension score for reasons
   unrelated to decoding skill — background-knowledge load, not decoding. Flagging for the
   builder to explicitly decide (and state) whether this is an acceptable trade-off or whether
   Passage content should be less domain-specific, rather than leaving it implicit.

**Defect count: 9** (3 high, 4 medium, 2 low).

---

## Round N builder — fixes applied (2026-09-28)

All 9 defects from the Round 1 critic worklist addressed. `placement-test.md` was substantially
rebuilt; `start-here.md` and `screener.md` received targeted edits; `research/07-program-scopes-assessment.md`
§5 was corrected with a dated note.

1. **[HIGH — Stage 2 letter-sound count bug] Fixed.** `placement-test.md` Stage 2 restructured
   into three separately-scored blocks: Block A = single letters + qu (26 items, exactly the
   Level 1 letter set from DESIGN.md §3), Block B = L2 digraphs (sh ch th wh ng, 5 items), Block
   C = L3/4 vowel teams + r-controlled (ai ee igh oa ar or ow, 7 items). Scoring sheet and
   placement rule updated to use Block A alone as the "single letters alone" subscore the
   placement logic actually needs (previously uncomputable from the interleaved table).

2. **[HIGH — Stage 4 FK/WCPM mismatch] Fixed.** All three ORF passages rewritten from scratch
   and measured with the `textstat` Flesch-Kincaid Grade Level formula: Passage A = 1.65 (≈
   Grade 2), Passage B = 4.68 (≈ Grade 4), Passage C = 6.82 (≈ Grade 6) — verified by script,
   not estimated. Fetched the real Hasbrouck-Tindal (2017) 50th-percentile WCPM table (Read
   Naturally's hosted copy of ERIC ED594994: Grade 2 Fall/Winter/Spring = 50/84/100, Grade 4 =
   94/120/133, Grade 6 = 132/145/146) and cited it directly in the file with the source. Pass
   thresholds now use each passage's FK-matched grade's Fall 50th percentile (50 / 94 / 132
   WCPM) instead of an unrelated grade band. Each passage heading now states its FK grade next
   to its WCPM target so a future reviewer can catch any future drift immediately. Kept the
   passages adult-register (per DESIGN.md rule 6) and added an explicit note naming the
   Track-A/B trade-off this creates (defect #9, folded into the same section rather than left
   implicit).

3. **[HIGH — Stage 1 PA ladder mischaracterization] Fixed.** Rebuilt Stage 1 from the ground up
   to match the real PAST's actual structure (fetched from thepasttest.com this round):
   syllable-level compound-word deletion → onset-rime deletion/substitution → phoneme deletion →
   phoneme substitution, in that order, with fresh (non-copied) items at each level. Added the
   second scoring axis PAST uses — **Automatic** (≈3-second response cutoff) alongside
   **Correct** — at every level, and updated the scoring sheet and placement rule accordingly.
   Corrected `research/07-program-scopes-assessment.md` §5's description of Stage 1 (which had
   claimed a "rhyme recognition → phoneme blending → phoneme segmentation → phoneme deletion"
   ladder as PAST-derived, when the real PAST has no rhyme or pure-blending section) and left a
   dated correction note in place rather than silently rewriting the research file.

4. **[MED — pseudoword notation inconsistency] Fixed.** Replaced every ad hoc slash-respelling
   pronunciation across all 5 Stage 3 tiers with the PSC's own two-part convention: each
   pseudoword now lists a real word it **rhymes with** and the real word its target
   grapheme's sound is **drawn from**, plus an explicit note (matching PSC guidance) that all
   reasonable regional pronunciations of the target sound should be accepted. Removed the
   previous mixed convention (some items reusing a homophone's ordinary spelling, others using
   ad hoc slashes) entirely.

5. **[MED — Wanzek mis-citation] Fixed.** `start-here.md`'s "Time per day" section rewritten:
   the evidence-backed claim now correctly attributes **group size** (1:1/small-group vs. large
   group) as Wanzek et al. (2013)'s actual moderator finding, and the "short, frequent sessions"
   scheduling advice is now presented as general practice recommendation, explicitly separated
   from what the citation supports.

6. **[MED — Stage 1 self-test non-administrability] Fixed.** Self-test section now states
   plainly that Stage 1 (all four PAST-style levels) cannot be genuinely self-administered
   because every item is a stimulus-response task requiring an oral-only presentation the
   test-taker hasn't already seen in print — and instructs a solo adult to either find a second
   person to read the "Item" column aloud, or skip Stage 1 and mark it "not administered" rather
   than fake a self-defeating workaround.

7. **[LOW — screener.md duplicate numbering] Fixed.** "If flagged: what to do" renumbered 1–5
   sequentially (was 1, 2, 2, 3, 4).

8. **[LOW — Passage A Q4 not genuinely inferential] Fixed.** Passage A's comprehension Q4 (and
   the equivalent items on the rewritten Passages B and C) now require synthesizing information
   from non-adjacent parts of the passage — e.g. Passage A's Q4 connects the man's thanks at the
   end of the passage back to Rana's problem-solving action several sentences earlier, rather
   than linking two adjacent clauses.

9. **[LOW — Track A/B trade-off note] Addressed as a documented decision, not a fix.** Added an
   explicit paragraph at the end of the Stage 4 section naming the uniform adult/civic-register
   choice across all three ORF passages as deliberate, stating the cost plainly (background-
   knowledge load for child test-takers on words like "disrepair" or "fares"), and giving testers
   a concrete action if a child's comprehension score looks low for this reason specifically.

**Defects closed: 9/9** (3 high, 4 medium, 2 low).

---

## Round 2 critic — 2026-09-28

Fresh-eyes pass. Verified every Round-1 fix against primary sources fetched live this round
(not re-trusting the builder's log): the real PAST test PDF and Instructions PDF
(thepasttest.com, Forms A–D, fetched directly), the real UK Phonics Screening Check 2024
official scoring guidance PDF and a real 2019 PSC pupils'-materials past paper (both fetched
directly from assets.publishing.service.gov.uk / primarytools.co.uk), the real Hasbrouck-Tindal
(2017) compiled ORF norms table (ERIC ED594994, fetched and `pdftotext`'d directly), and the
real DIBELS 8th Edition Administration and Scoring Guide (dibels.uoregon.edu, fetched directly).
Flesch-Kincaid grades for all three Stage 4 passages were independently recomputed with
`textstat` from the actual passage text in the file, not taken on trust from the builder's
log.

### Fix verification table

| # | Round 1 defect | Really fixed? | Evidence |
|---|---|---|---|
| 1 | Stage 2 letter-sound count/denominator bug | **Y** | Recounted Block A/B/C by hand: 26 + 5 + 7 = 38, exactly matching the restructured scoring sheet's `/26`, `/5`, `/7` denominators. No mismatch remains. |
| 2 | Stage 4 FK/WCPM mismatch (Single Biggest Gap) | **Y** | Independently recomputed FK grade of all three passages with `textstat.flesch_kincaid_grade()` on the exact text in `placement-test.md`: A=1.65, B=4.68, C=6.82 — matches the file's claimed ≈1.7/4.7/6.8 almost exactly. Independently fetched and `pdftotext`'d the real 2017 Hasbrouck-Tindal table (ERIC ED594994): Grade 2 50th = Fall 50/Winter 84/Spring 100; Grade 4 50th = Fall 94/Winter 120/Spring 133; Grade 6 50th = Fall 132/Winter 145/Spring 146 — every one of these numbers matches the file's cited table exactly, digit for digit. This was the Round 1 "single biggest gap" and it is now genuinely closed. |
| 3 | Stage 1 PAST-ladder mischaracterization | **PARTIAL** | The specific claim fixed ("PAST has no rhyme/pure-blending section") is verified true against the real PAST PDF. But the rebuild introduces new mismatches with the same primary source it claims to follow — see worklist #2 below — and `research/07` §5 now contains a **self-contradiction** (worklist #1). Not a clean fix. |
| 4 | Stage 3 pseudoword notation inconsistency | **PARTIAL** | The new rhyme+source-word convention matches the real PSC format in substance (verified against the actual 2024 PSC scoring guidance PDF: "This item uses the '_' from '_' and rhymes with '_'"), a real improvement over the old ad hoc slashes. But it omits the IPA column the real PSC gives every item, and at least two of the new glosses are themselves factually wrong (worklist #4). |
| 5 | Wanzek et al. mis-citation (group size vs. frequency) | **Y** | Re-checked against `research/03` §5 directly: the finding is correctly attributed to group size now, and the "short/frequent sessions" scheduling advice is explicitly separated out as general practice, not evidenced by this citation. |
| 6 | Stage 1 self-test non-administrability | **Y** | `placement-test.md` self-test section now states plainly that Stage 1 needs a second person and offers "mark not administered" as the honest fallback, matching the fix log. |
| 7 | `screener.md` duplicate numbering | **Y** | "If flagged: what to do" is now numbered 1–5 sequentially. |
| 8 | Passage A Q4 not genuinely inferential | **Y** | Q4 (and the equivalent items on B/C) now require connecting the passage's ending to an earlier, non-adjacent action rather than linking two adjacent clauses — a real, if modest, improvement. |
| 9 | Track A/B trade-off left implicit | **Y** | Explicit paragraph added at the end of Stage 4 naming the trade-off and giving testers a concrete action. |

**5 of 9 cleanly fixed, 2 of 9 partially fixed (both re-open into new, more specific defects
below), 2 of 9 fully fixed.** Net: real progress, but two of Round 1's three HIGH-severity
defects (#3 and, in its notation half, #4-adjacent) are not actually closed — they mutated
into narrower but still-real defects.

### VERDICT — blind comparisons (redone against real references fetched this round)

**Comparison 1 (revisited): Stage 3 pseudoword design vs. the real PSC.** **REFERENCE (PSC)
WINS, narrowly** (gap closed substantially from Round 1's clear loss). The rhyme+source-word
format is now genuinely PSC-shaped. But a reading specialist checking this table for real use
would hit two of its own pseudoword glosses that are factually wrong (Tier 4 "corst" claimed to
rhyme with "horse" — it doesn't, coda mismatch; "combrat" claimed to have a second syllable
rhyming with "-bit" as in "rabbit" — it doesn't, vowel mismatch /æ/ vs /ɪ/) and no IPA anywhere
in the table, where the real PSC gives IPA for every single item as its actual disambiguator
(the "rhymes with" language is supplementary in the real PSC, not present for every item, and
never the primary anchor). For an audience of Urdu-L1 non-specialist parents/tutors — this
course's own stated audience — an unambiguous phonemic target arguably matters *more* than for
a native-English UK class teacher administering the PSC, making the missing-IPA gap more
costly here, not less.

**Comparison 2 (revisited): Stage 1 oral-PA ladder vs. the real PAST.** **REFERENCE (PAST)
WINS**, though the gap has narrowed a lot from Round 1's clear loss. Verified against the real
PAST Forms A–D PDF and Instructions PDF (thepasttest.com): the real test is NOT four clean,
equal 8-item blocks of (1) syllable deletion, (2) onset-rime del/sub, (3) phoneme deletion,
(4) phoneme substitution, as the course now presents it. It is four **unevenly-sized** sections
— Basic Syllable (12), Onset-Rime (10), Basic Phoneme (10), Advanced Phoneme (20) — and from
Onset-Rime onward, every section **interleaves deletion and substitution items together**
(e.g. Level H1=deletion, H2=substitution; Level K1=deletion, K2=substitution), rather than
sorting deletion into one level and substitution into a separate, harder level the way the
course's Level 3/Level 4 split does. The real test also has an explicit **vowel-substitution**
item type (Level J: short and long vowel changes) that the course's ladder has no equivalent
of at all, and scores "Highest Correct Level" and "Highest Automatic Level" as two independent
placement outputs (a specialist can see a learner is accurate but not yet automatic at a
level) — the course keeps Automatic only as a soft flag, not an independent placement metric.
Separately, the automaticity cutoff itself is wrong: the real PAST Instructions specify a
**2-second** count ("one thousand one, one thousand two" — respond before "two" = automatic),
not the course's stated "~3 seconds" (the Instructions actually describe non-automatic
responses as typically taking ~2.5–3+ seconds — the course's number describes the *failing*
zone, not the cutoff). A specialist placing a real learner would still reach for the actual
PAST manual, not this rebuild, though for a meaningfully closer set of reasons than Round 1's.

**Comparison 3 (new — Stage 4 ORF vs. real DIBELS 8th Edition).** **REFERENCE (DIBELS) WINS on
rigor, but the practical gap is small given the two instruments serve different purposes.**
Verified against the official 2023 DIBELS 8 Administration and Scoring Guide
(dibels.uoregon.edu): DIBELS passages are authored to a **pre-registered FK-grade-band spec**
(e.g. 1.5–2.0 for Grade 1) and validated via passage *piloting* with real students, not
FK-measured after the fact the way this course's three passages were; DIBELS uses only **one**
passage per benchmark period (research-justified — more passages don't improve reliability,
per the same guide) where this course stacks three ascending passages into one placement pass
(a reasonable, different design given a placement test's different job from a periodic
benchmark check); DIBELS specifies an exact **3-second** hesitation-counts-as-error threshold
and an exact 3-second self-correction-does-not-count-as-error window, plus a "discontinue if
zero words correct in the first line" rule — this course's Stage 4 still only says "skip, wrong
word, or long hesitation = error," leaving "long" to the tester's subjective judgment; and
DIBELS classifies into four empirically sensitivity/specificity-validated risk tiers
(red/yellow/green/blue) rather than this course's single borrowed percentile cut per grade.
None of this makes the course's Stage 4 dishonest (the Hasbrouck-Tindal citation is now, per
Comparison-table item #2, verified accurate) — it's a legitimately simpler instrument for a
legitimately different job (one-time OER placement, not repeated formal MTSS risk screening)
— but a specialist administering to a real learner where the exact call matters would still
want DIBELS' sharper timing/discontinue rules that this course hasn't adopted.

### SINGLE BIGGEST GAP

**Defect #3 from Round 1 (Stage 1's PAST characterization) was reported "fixed" but re-opens
into a narrower version of the exact same problem: a claim of following a specific named
primary source that, checked directly against that source, still doesn't match it — and this
time the file left old and new versions of the claim contradicting each other in the same
document.** `research/07-program-scopes-assessment.md` line 191 (a program-comparison table
row) still reads: "Oral-only phonological awareness across a difficulty ladder: rhyme →
blending → segmenting → deletion → substitution, at word/syllable/phoneme level, with
automaticity noted" — this is the *exact* mischaracterization the Round 1 critic flagged and
the builder's own fix log says was corrected. But the correction was only applied to a
different paragraph 11 lines further down (line 202-204), which now explicitly says PAST has
"no rhyme-judgment or pure-blending section" — directly contradicting line 191 in the same
file. A future reader (or the next builder) hitting line 191 first will re-absorb the false
claim the course already spent a whole gauntlet round correcting. Underneath that surface
contradiction sits the deeper issue: even the *corrected* Stage 1 in `placement-test.md` still
doesn't structurally match the real PAST (uneven section sizes, interleaved not
sequential deletion/substitution, missing vowel-substitution item type, 2-second not 3-second
automaticity cutoff, Automatic downgraded from an independent metric to a flag) — meaning this
course has now gotten a DESIGN.md rule 12 (honest citations) violation on the exact same
instrument wrong twice in a row, just less badly the second time. That recurrence, more than
the residual structural gap itself, is the thing worth a builder pausing on before the next
round: whatever caused the first mischaracterization (working from a secondary description of
PAST rather than the primary form PDF) doesn't yet look fully corrected as a *process*, only
patched as a *result* in one of two places it appears.

### Defect worklist (prioritised, file + exact location + required fix)

1. **[HIGH] `research/07-program-scopes-assessment.md` line 191 self-contradicts the correction
   note at lines 202–204 in the same file.** Line 191 (inside the program-comparison table, PAST
   row) still says "rhyme → blending → segmenting → deletion → substitution ... with
   automaticity noted (correct-automatic vs correct-slow)" — the same mischaracterization the
   line-204 correction note says was fixed. **Fix:** rewrite line 191's cell to match the
   corrected structure ("syllable-level deletion → onset-rime deletion/substitution → phoneme
   deletion/substitution (interleaved, not sequential) → advanced/vowel substitution, scored
   Correct + Automatic on a 2-second cutoff"), so the file doesn't contain two different
   descriptions of the same instrument seventeen lines apart.

2. **[HIGH] Stage 1's rebuilt ladder still doesn't structurally match the real PAST it claims
   to follow.** `placement-test.md` Stage 1 (Levels 1–4, 8 items each, 32 total; deletion sorted
   into Level 3, substitution sorted into a separate, harder Level 4). Verified against the real
   PAST Forms A–D PDF (thepasttest.com): the actual instrument has **uneven** section sizes
   (Basic Syllable 12, Onset-Rime 10, Basic Phoneme 10, Advanced Phoneme 20 = 52 total, not 32),
   **interleaves** deletion and substitution items within the same section from Onset-Rime
   onward rather than sorting them into separate difficulty levels, and includes an explicit
   **vowel-substitution** item type (Level J: short/long vowel changes, e.g. "ran → run") that
   has no equivalent anywhere in the course's four levels. **Fix:** restructure Stage 1's four
   levels to mirror the real section boundaries (Syllable / Onset-Rime del+sub / Basic Phoneme
   del+sub / Advanced Phoneme del+sub+vowel-substitution), add a vowel-substitution item type at
   the hardest level, and stop treating "deletion" and "substitution" as two separate sequential
   difficulty tiers.

3. **[MED] Automaticity cutoff is wrong, and Automatic is not scored as an independent placement
   axis the way the real PAST does.** `placement-test.md` Stage 1 intro states "~3 seconds" as
   the automatic/non-automatic cutoff. The real PAST Instructions PDF (fetched this round)
   specifies a strict **2-second** count ("one thousand one, one thousand two" — respond before
   "two" = automatic) and separately notes non-automatic responses typically take ~2.5–3+
   seconds — the course's "~3 seconds" describes the *failing* zone, not the cutoff. Separately,
   the real PAST reports "Highest Correct Level" and "Highest Automatic Level" as two
   independent outputs; this course's scoring sheet and placement rule use Automatic only as a
   soft flag for `screener.md`, never as its own placement signal. **Fix:** change the cutoff to
   2 seconds; add a "Highest Automatic Level" line to the scoring sheet alongside "Highest
   Correct Level," with an explicit placement-rule branch for when the two levels diverge
   (accurate but not automatic at the entry level → place there, but schedule extra automaticity
   drill), matching the real instrument's two-metric design instead of collapsing it to one.

4. **[MED] Two of the rebuilt Stage 3 pseudoword pronunciation glosses are themselves factually
   wrong.** `placement-test.md` Tier 4 table: item 2, pseudoword "corst," glossed "Rhymes with:
   horse (rhymes; drop the 'e')" — /kɔːrst/ and /hɔːrs/ do not rhyme (mismatched coda, extra
   /t/); item 8, pseudoword "combrat," glossed "Rhymes with (final syllable): rabbit (2nd
   syllable rhymes with '-bit'...)" — "-brat" /bræt/ does not rhyme with "-bit" /bɪt/ (different
   vowel). A tester following either gloss as written would model the wrong target sound to the
   learner. **Fix:** re-derive genuine rhyme partners for both (or replace the pseudowords
   themselves if no clean one-syllable rhyme partner exists for the target grapheme), and re-pass
   every gloss in all 5 tiers specifically checking that the claimed rhyme is a real one, not
   just plausible-looking.

5. **[MED] Stage 3's pseudoword tables still omit the IPA transcription every real PSC item
   gets.** `placement-test.md`, all 5 tiers. Verified against the real 2024 PSC official scoring
   guidance PDF: every pseudoword row has a "Phonemic representation" column (e.g. "nop → /nɒp/")
   as its actual disambiguator — the "rhymes with X" language is supplementary and isn't even
   present for every PSC item (some instead combine two real-word sound fragments with no rhyme
   partner at all, e.g. "This item combines the 'b' from 'bell' with the 'au' from 'audio'").
   **Fix:** add an IPA column to every pseudoword table, and for any pseudoword that has no clean
   single rhyme partner, switch to the PSC's fragment-combination phrasing ("combines the X
   from... with the Y from...") rather than forcing a strained rhyme claim — this would also
   have caught defect #4 above before it shipped.

6. **[LOW] Stage 4's error/self-correction rules are looser than DIBELS 8's, which this file
   cites as a design influence.** `placement-test.md` intro line ("Based on the 5-stage design
   ... DIBELS/Acadience Oral Reading Fluency ...") and the Stage 4 administration paragraph
   ("count words read correctly (skip, wrong word, or long hesitation = error)"). The real
   DIBELS 8 Administration and Scoring Guide (verified, dibels.uoregon.edu) specifies an exact
   3-second hesitation-as-error threshold, an exact 3-second self-correction-not-an-error
   window, and a "discontinue if zero words correct in the first line" rule. **Fix:** adopt
   DIBELS' explicit 3-second thresholds for both rules and add the discontinue rule, so "long
   hesitation" isn't left to a non-specialist tester's subjective judgment — this matters more
   here than in a school setting, precisely because this course's testers are often untrained
   parents/tutors.

7. **[LOW] The Stage 4 pass/fail design choice (single borrowed percentile cut vs. DIBELS'
   validated 4-tier risk system) is a defensible simplification but isn't named as a deliberate
   trade-off the way defect #9's Track A/B choice now is.** `placement-test.md` Stage 4 benchmark
   lines. DIBELS 8 classifies into four empirically sensitivity/specificity-validated risk tiers
   (red/yellow/green/blue); this course uses a single Fall-50th-percentile cut per grade, which
   is honestly cited (verified accurate against the real 2017 table) but has no independent
   validation of its own predictive value for this course's specific purpose. **Fix:** add one
   sentence next to the Stage 4 benchmark table stating plainly that this is a simpler,
   non-validated single-cut design chosen because this is a one-time placement tool, not a
   repeated formal risk-screening instrument like DIBELS — so a future reviewer doesn't mistake
   the WCPM gate for a validated risk classification.

**New/residual defect count this round: 7** (2 high, 3 medium, 2 low). Of Round 1's 9 claimed
fixes: 5 clean, 2 partial (re-opening into worklist items #2–#5 above), 2 clean. **0 of the 3
original HIGH-severity defects are cleanly closed** — #1 (Stage 2 count) is closed, but the
other two HIGHs (Stage 4 FK/WCPM, Stage 1 PAST structure) split: Stage 4 FK/WCPM is now
genuinely closed (confirmed independently this round), but Stage 1's PAST-structure defect
re-opened as HIGH worklist items #1–#2 above.

---

## Round 2 builder — fixes applied (2026-09-28)

All 7 Round 2 defects addressed (2 high, 3 medium, 2 low).

1. **[HIGH — research/07 line 191 self-contradiction] Fixed.** Rewrote the PAST row in the
   assessment-tools comparison table (`research/07-program-scopes-assessment.md`, the table
   preceding §5) to correctly describe the real PAST's uneven section sizes (12/10/10/20),
   interleaved deletion+substitution from Onset-Rime onward, the vowel-substitution item type,
   the two independent Correct/Automatic outputs, and the real 2-second (not 3-second)
   automaticity cutoff — so it now matches, rather than contradicts, the corrected paragraph 11
   lines below it. Also rewrote that paragraph (§5 Stage 1 description) to add the "PAST-
   informed, not a PAST clone" framing and an amended, dated correction note explaining both
   rounds' fixes rather than leaving only the Round 1 note in place.

2. **[HIGH — Stage 1 structural mismatch] Fixed.** Rebuilt `placement-test.md` Stage 1 to
   mirror the real PAST's actual shape without cloning it: Level 1 (syllable deletion, unchanged
   — matches PAST's Basic Syllable section having no substitution items), Level 2 (onset-rime,
   deletion and substitution items now explicitly alternating D/S rather than grouped), Level 3
   (basic phoneme, deletion and substitution interleaved, initial/final/cluster positions), and
   Level 4 (advanced: deletion, consonant substitution, AND vowel substitution interleaved — 3 of
   its 8 items are now vowel-substitution, the item type entirely missing before). Automaticity
   cutoff changed from "~3 seconds" to the real PAST Instructions' 2-second count. Added
   **Highest Correct Level** and **Highest Automatic Level** as two independent scored/placement
   outputs (previously Automatic was only a soft flag), with a placement-rule branch for when
   they diverge. Added an explicit "PAST-informed, not PAST" framing at the top of Stage 1
   stating plainly that this course does not reproduce PAST's copyrighted items or exact section
   sizes (12/10/10/20) — it borrows PAST's real design principles into a shorter, original
   instrument built for one-time OER placement.

3. **[MED — automaticity cutoff + independent metric] Fixed as part of item 2 above.** 2-second
   cutoff now stated explicitly with the "one thousand one / one thousand two" count method;
   Highest Automatic Level now tracked and reported independently of Highest Correct Level in
   both the Stage 1 section and the scoring sheet, with its own placement-rule note.

4. **[MED — wrong rhyme anchors] Fixed.** Every pseudoword rhyme claim across all 5 Stage 3
   tiers was independently re-checked this round (CMU Pronouncing Dictionary-style phoneme
   comparison). Two were genuinely wrong and fixed: Tier 4 item 2 "corst" (falsely glossed as
   rhyming with "horse") replaced with "gorn," which genuinely rhymes with "corn"; Tier 4 item 8
   "combrat" (falsely glossed as rhyming with "-bit" as in "rabbit") re-glossed to its real
   rhyme, "chat." Both fixes are documented inline in the file with the phonetic reasoning, not
   just silently changed. Also fixed a latent defect the critic didn't flag but this recheck
   surfaced: Tier 1 item 4 was "rob," which is a real English word and therefore an invalid
   pseudoword — replaced with "pob" (rhymes with "job," tests /p/).

5. **[MED — missing IPA] Fixed.** Added an IPA column to every pseudoword table across all 5
   Stage 3 tiers, matching the real PSC's own primary disambiguator (verified against the actual
   2024 PSC official scoring guidance PDF). Added a note that regional vowel variants (e.g.
   /ɒ/ vs /ɑ/) should both be accepted, and that the "rhymes with" language stays supplementary
   (per the real PSC), not the sole anchor, exactly as the critic's fix directive specified.

6. **[LOW — DIBELS admin rules] Fixed.** Added, verbatim in spirit from the real DIBELS 8th
   Edition Administration and Scoring Guide: an exact 3-second hesitation-counts-as-error rule,
   an exact 3-second self-correction-counts-as-correct window, and a discontinue rule (zero
   words correct in the first line → stop, score 0, return to Stage 3 placement instead of
   continuing up the passage ladder). Placed directly in the Stage 4 administration section
   rather than left to tester judgment, which matters more here than in a school setting because
   this course's testers are frequently untrained parents/tutors.

7. **[LOW — single-cut design not named as a trade-off] Fixed.** Added an explicit paragraph
   ("A note on what this single-cut design is, and isn't") directly above the administration
   rules in Stage 4, stating plainly that this course's single Fall-50th-percentile cut per
   grade is a simpler, non-validated alternative to DIBELS' own four-tier, sensitivity/
   specificity-validated risk classification, chosen because this is a one-time placement
   instrument rather than a repeated formal risk-screening tool — so a future reviewer doesn't
   mistake the WCPM gate for a validated risk classification.

**Defects closed: 7/7** (2 high, 3 medium, 2 low). Combined with Round 1: 16/16 defects across
both rounds addressed. Both of Round 1's HIGH-severity defects that re-opened this round
(Stage 1 PAST-structure, and the research/07 self-contradiction the incomplete fix produced)
are now closed against the primary sources directly, not just against the prior round's fix
log.

---

## Round 3 critic — 2026-09-28

Fresh-eyes pass, not trusting the Round 2 builder's log. Re-fetched and read directly this
round: the real 2024 UK Phonics Screening Check official scoring guidance PDF
(`assets.publishing.service.gov.uk/media/666981ac205b335264f76031/...pdf` — Section 1/2
pseudo-word tables, verbatim), the real PAST Instructions PDF (thepasttest.com, Revised
January 2024 — automaticity/2-second-count section, routing procedure, and the D–M level
structure that yields the claimed 12/10/10/20 split), and the real DIBELS 8th Edition
Administration and Scoring Guide (dibels.uoregon.edu, 2026 hosted copy — ORF discontinue rule,
3-second hesitation/self-correction rules, all `pdftotext`'d directly). Checked every Stage 3
pseudoword in `placement-test.md` against a dictionary (Merriam-Webster/Wiktionary) for
real-word status, and re-derived several rhyme pairs by hand.

### Fix verification table (Round 2's 7 claimed fixes)

| # | Round 2 defect | Really fixed? | Evidence |
|---|---|---|---|
| 1 | `research/07` line 191 self-contradiction | **Y** | Line 191's PAST table row now reads "uneven sections... interleaved... vowel substitution... 2-second cutoff" — matches the corrected §5 paragraph below it, no contradiction found on a fresh read of the whole file. |
| 2 | Stage 1 structural mismatch (uneven sizes, interleaving, vowel-sub, PAST-informed framing) | **Y, and verified against the primary PAST Instructions PDF this round** | The Instructions PDF's routing-procedure section independently confirms the 12/10/10/20 split this course cites: Syllable levels D1–E3 (12 items) + Onset-Rime F/G (10) + Basic Phoneme H/I (10) + Advanced Phoneme J–M (20, with Level J = vowel substitution, confirmed by the "sit→sat," "hid→had" worked example) = 52. `placement-test.md`'s own ladder now correctly interleaves D/S within levels and adds a vowel-substitution row at Level 4. Honestly framed as "PAST-informed, not PAST." |
| 3 | Automaticity cutoff (2s) + independent Correct/Automatic metrics | **Y** | Fetched the real PAST Instructions PDF directly: "count in your head 'one thousand one, one thousand two'... if the student responds correctly before you say the word two... automatic" — exact 2-second cutoff, exactly as the course now states. Highest Correct/Highest Automatic now tracked as two independent outputs, matching the real instrument. |
| 4 | Wrong rhyme anchors (corst/horse, combrat/rabbit) | **Y for the two flagged items** | "gorn"/"corn" and "combrat"/"chat" both genuinely rhyme (checked by hand: /gɔrn/-/kɔrn/, /bræt/-/tʃæt/ share the same rime once onset is stripped). **But this recheck surfaced a fresh, different pseudoword defect the Round 2 fix pass didn't catch — see worklist #1 below.** |
| 5 | Missing IPA column | **Y** | Every pseudoword row in all 5 Stage 3 tiers now has an IPA column. Verified format against the real PSC scoring guidance PDF (fetched fresh this round): the PSC's actual format is exactly "This item uses the '_' from '_' and rhymes with '_'" + a "Phonemic representation" column (e.g. "nop → /nɒp/") — this course's three-part (IPA / rhymes-with / grapheme-drawn-from) table matches that shape closely. |
| 6 | DIBELS admin rules (3s hesitation/self-correction, discontinue) | **Y** | Fetched the real DIBELS 8 guide directly: "Discontinue ORF Rule. If the student does not read any words correctly in the first line of the passage..." and "...hesitations of more than three seconds are scored as errors. Words self-corrected within three seconds are scored as accurate" — both match `placement-test.md`'s Stage 4 rules verbatim in substance. |
| 7 | Single-cut vs 4-tier trade-off named | **Y** | The "note on what this single-cut design is, and isn't" paragraph is present and accurate. |

**7/7 Round 2 fixes hold up.** But this round's fresh read (not just re-checking the prior
round's specific flagged items) found new, previously-uncaught defects — see worklist below.
This is the same pattern noted in Round 2's "Single Biggest Gap": re-verifying a fix by
checking only the narrow thing that was flagged, rather than re-doing the underlying check
(e.g. "is every pseudoword in this table actually not a real word?") from scratch, keeps
missing sibling defects of the same type.

### VERDICT — blind comparison (task 2: our placement test vs. real PSC + DIBELS combination)

**Job:** place any-age learner into the right lesson of THIS course in ~20 minutes,
administered by a non-specialist parent or teacher.

**OURS WINS**, and it isn't close for this specific job, despite the real instruments being
individually more rigorous in places. Reasoning:

1. **Neither PSC nor DIBELS was built to output "start at Lesson N.NN of a specific 7-level,
   ~100-lesson scope-and-sequence."** PSC is a single pass/fail check calibrated to one narrow
   band (end of Year 1, age ~6, 40 items — 20 real + 20 pseudo — one sitting, one grade level).
   DIBELS 8 is a suite of six subtests (LNF, PSF, NWF, WRF, ORF, Maze) benchmarked to specific
   grade/season windows (e.g. "Grade 3, Winter") and requires selecting the correct grade-level
   materials up front — it has no oral phonological-awareness component at all (that's exactly
   the gap PAST fills, and DIBELS doesn't include PAST). A specialist combining PSC + DIBELS
   still has to hand-translate two sets of standardized scores into "so start this specific
   learner at lesson 2.4" — a mapping this course's own placement rule (`placement-test.md`
   §"Placement rule (final)") does directly, tier-by-tier, onto its own DESIGN.md §3 sequence.
   That direct-to-lesson mapping is the actual job description, and only our instrument does it.
2. **Neither instrument spans the full novice-to-adult range in one sitting.** PSC assumes a
   Year 1 UK pupil (no oral-PA on-ramp, no adult/ESL framing, British-curriculum-specific
   vocabulary and format). DIBELS spans K–8 grade bands but nothing beyond, and neither
   instrument was designed for, or piloted with, adult/ESL beginners — this course's own
   population. Stage 1 (oral PA) plus the letter-sound and decoding stages give this course's
   test a true zero-to-fluent span that the PSC+DIBELS combination doesn't cover on its own
   (you'd need to bolt on the actual PAST as a third instrument to get oral-PA coverage, at
   which point you've reassembled roughly what this course already built, just as three separate
   copyrighted/licensed tools instead of one coherent free one).
3. **Administrability by an untrained parent is a real, load-bearing constraint DIBELS
   explicitly works against.** The real DIBELS guide requires "training," calibrated 1-minute
   timing per subtest, per-grade materials selection, and (for benchmarking) discontinue/gating
   rules across six different subtests — considerably more procedural overhead than this
   course's single, self-contained, one-file instrument with an explicit self-test fallback
   section. PSC likewise assumes a trained UK class teacher administering to a whole cohort.
   Neither was designed for the "one untrained parent, one learner, one sitting" use case this
   course targets.
4. **Where the real instruments do win, cleanly:** DIBELS' error/hesitation/discontinue timing
   rules are more exact than a homegrown instrument would produce unaided — but this course
   already imported them near-verbatim (verified above), so that gap is closed, not open. PSC's
   IPA-first pseudoword disambiguation is also now matched. The one place the real instruments
   still generally exceed this course is **field validation** — PSC and DIBELS pseudowords and
   passages were piloted with real children and adjusted from empirical item data; this course's
   pseudowords and passages are author-constructed and checked only by manual/dictionary
   re-derivation (as this very round demonstrates, that process still misses defects — see
   below). That's a real, structural gap this course cannot close without an actual pilot, and
   should be named as an open limitation rather than implied away.

### SINGLE BIGGEST GAP

**None of the placement instrument's core design is broken anymore — the two remaining highest-
value defects are a fresh instance of the exact defect *class* Round 2 already found and
"fixed": a pseudoword that turns out to be a real English word, and a citation fix that was
applied to one file but not its sibling file making the identical claim.** Both are below.
Neither is as structurally serious as Round 1/2's issues (PAST mischaracterization, FK/WCPM
mismatch) — this is now a polish-and-completeness gauntlet, not a design-validity one — but
worklist item #1 specifically repeats a defect *type* (real word posing as pseudoword) that was
already caught and fixed once this same file, which suggests the re-check process
("independently re-checked... CMU Pronouncing Dictionary-style phoneme comparison," per the
Round 2 fix log) checked rhyme validity carefully but did not systematically re-verify
real-word-status for every item the way it should have, given that exact bug's history in this
same document.

### Defect worklist (prioritised, file + exact location + required fix)

1. **[HIGH] Stage 3 Tier 3 pseudoword "shute" is a real, dictionary-listed English word**,
   making it invalid as a pseudoword under `DESIGN.md`'s own decodability rules (a pseudoword
   must not be a word the learner could recognize by sight/meaning — this is the identical bug
   class as Tier 1's "rob," which the Round 2 builder already found and fixed elsewhere in this
   same file). `placement-test.md` Tier 3, item 6: "shute," glossed "Rhymes with: cute (same
   rime /uːt/, different onset)." Merriam-Webster and Wiktionary both list "shute" as a standard
   (if secondary) variant spelling of "chute," meaning an inclined channel or slide — not a rare
   obscurity; it appears in general dictionaries as a plain headword. A learner (especially a
   literate teen/adult in this course's own target audience) who recognizes "shute" as a real
   word rather than sounding it out defeats the entire point of this tier (research/07 §5: "this
   is the single most load-bearing design choice in the whole test" — telling decoding from
   sight-memorization apart). **Fix:** replace "shute" with a genuine non-word for the same u_e
   pattern (e.g. "lune" is arguably also borderline-real in some dictionaries as an
   astronomical/geometric term — check carefully; "zute" or "prude"-adjacent nonwords like
   "fute" are safer candidates), and this time explicitly grep/dictionary-check **every**
   pseudoword in all 5 tiers against a real dictionary (not just a rhyme-phoneme comparison) —
   the Round 2 fix log's re-check method (CMU-dict phoneme comparison for rhyme accuracy) does
   not by itself catch "is this string a real word," which is a different check entirely.

2. **[HIGH] `guide-tutors-parents.md` still contains the exact Wanzek et al. mis-citation that
   Round 1's defect #5 fixed in `start-here.md`, but the fix was never propagated to this
   sibling file making the identical claim.** `guide-tutors-parents.md` line 97–99: "Keep
   sessions to the stated time (20–35 min) — don't extend 'just a bit more' even if a child
   seems willing; short and frequent beats long, per the intensity research this course is built
   on (`research/03` §5)." This is the identical construct-mismatch Round 1 flagged: `research/03`
   §5 (Wanzek et al. 2013) found **group size** (1:1/small vs. large group) was the significant
   moderator, not session **frequency/length** — `start-here.md` was rewritten in Round 1 to say
   exactly this ("group size is the cited finding, not scheduling frequency"), but
   `guide-tutors-parents.md` was never touched and still cites the same §5 for the frequency
   claim it doesn't support. This is a second instance of a DESIGN.md rule 12 (honest citations)
   violation on the same underlying citation, in the same defect class Round 1 already spent a
   fix cycle on — it just surfaced in a file the Round 1 critic didn't happen to quote from.
   **Fix:** rewrite the line to either drop the citation entirely (state "short and frequent" as
   general practice advice, uncited, matching how `start-here.md` now handles it) or replace it
   with a citation that actually supports session-frequency/length as the variable, and do a
   full-repo grep for `research/03` §5 / "Wanzek" to confirm no other file repeats this same
   citation error.

3. **[MED] Stage 3 Tier 5 pseudoword "intergop" tests a different prefix than the real word it
   is supposed to parallel, and the file's own footnote concedes this rather than fixing it.**
   `placement-test.md` Tier 5 table, item 7: pseudoword "intergop," affix column says "the
   prefix 'inter-' (cf. 'inactive's 'in-')." Tier 5's whole design (stated at the top of Stage 3:
   each tier's 8 pseudowords are meant to mirror that tier's 8 real words' patterns) pairs this
   item against the real word "inactive," whose prefix is negation "in-" — a common, early
   Level-5 prefix (DESIGN.md §3 lists "20 prefixes" for Level 5, with "in-" being one of the most
   frequent). "inter-" (meaning "between/among," as in "international") is a different, unrelated
   morpheme that happens to share three letters, not a decoding-equivalent test of the same
   prefix. A learner could correctly decode "intergop" (proving they can read the "inter-"
   grapheme string) while never having their actual target skill — recognizing negation "in-" as
   a meaningful decodable chunk — tested at all in this tier. **Fix:** replace "intergop" with a
   pseudoword using prefix "in-" itself (e.g. "inflemt," testing "in-" + a nonsense root), so all
   8 Tier 5 pseudowords genuinely parallel their paired real word's specific affix, the way every
   other item in the tier already does correctly.

4. **[LOW] Stage 3's "same rime, different onset" rhyme claim for Tier 3 item 6 is phonologically
   defensible but reads as inconsistent with how strictly this course now treats rhyme claims
   elsewhere.** Independent of defect #1's real-word problem: even setting "shute" aside, its
   gloss ("rhymes with cute — same rime /uːt/, different onset") requires treating the /j/ glide
   in "cute" (/kjuːt/) as part of the onset rather than the rime, a legitimate but non-obvious
   phonological analysis choice that a non-specialist parent applying the file's own "does this
   really rhyme" standard (the exact standard that caught "corst"/horse and "combrat"/rabbit as
   genuinely *not* rhyming) could reasonably second-guess. **Fix:** once defect #1 forces a
   replacement pseudoword anyway, pick a rhyme partner that doesn't require the onset/rime glide
   judgment call at all (e.g. rhyme with "boot" or "suit" instead of "cute").

**Defect count: 4** (2 high, 1 medium, 1 low). All four are completeness/consistency gaps in
work that already passed two rounds of structural/validity critique — the placement
instrument's core design (PAST-informed Stage 1, IPA+rhyme Stage 3, FK-matched Stage 4) remains
sound and, per the blind comparison above, **beats the real PSC+DIBELS combination for this
course's specific placement job**, not because it's more rigorous in isolation but because it's
the only one of the three that actually does the job asked: turning a non-specialist parent's
~20 minutes into a specific lesson number in this specific course.

---

## Round 3 builder — fixes applied (2026-09-28)

All 4 Round 3 defects fixed, plus a full sibling sweep across every Stage 3 pseudoword in
`placement-test.md` (the file this round's defects concentrated in) and a repo-wide grep for
the Wanzek citation pattern.

1. **[HIGH] "shute" (Tier 3, item 6) — real word — Fixed.** "shute" is a dictionary-listed
   variant spelling of "chute." Replaced with "drute," which is not a real word, rhymes cleanly
   with "root" (no onset/rime ambiguity), and cites "flute" — not "cute" — as its sound source
   specifically to avoid the /j/-glide judgment call defect #4 also flagged (see item 4 below).

2. **[HIGH] Wanzek mis-citation in `guide-tutors-parents.md` — Fixed.** The "Keeping a child
   engaged" section's "short and frequent beats long... (research/03 §5)" line — which repeated
   the exact group-size-vs-frequency conflation Round 1 fixed in `start-here.md` but never
   propagated here — is rewritten: "short sessions" is now framed as general practice, uncited,
   and the actual Wanzek et al. (2013) finding (group size, not frequency) is stated correctly
   and separately, matching how `start-here.md` already handles it.

3. **[MED] "intergop" (Tier 5, item 7) — wrong prefix — Fixed.** "intergop" tested "inter-"
   (between/among) while paired against real word "inactive," whose prefix is negation "in-" —
   a different morpheme. Replaced with "inflemt," which genuinely tests "in-" + a nonsense root,
   matching "inactive"'s actual target prefix.

4. **[LOW] Rhyme/glide inconsistency — resolved as part of fix #1.** Since "shute" had to be
   replaced anyway, its replacement ("drute"/"root") requires no onset/rime glide judgment call
   at all, closing this defect alongside the real-word one.

### Sibling sweep (requested beyond the 4 named defects)

Ran every Stage 3 pseudoword (all 40, across 5 tiers) through four local dictionary wordlists
(`/usr/share/dict/words`, `american-english`, `british-english`, `cracklib-small`) — zero hits,
but this method is known to miss archaic/dialectal/slang entries (it already missed "shute" in
this same round, per the critic's own finding via Merriam-Webster/Wiktionary rather than a
wordlist). Followed up with targeted Wiktionary lookups on every item that pattern-matched a
plausible real, archaic, dialectal, or slang word by ear. This found **three more real words the
automated sweep and prior rounds' phoneme-rhyme rechecks had both missed**:

- **"gan" (Tier 1, item 2)** — real dialectal/archaic English (Northern English dialect for
  "go"; archaic past tense of "gin"), confirmed on Wiktionary. Replaced with "gep" (rhymes
  "pep," not a real word).
- **"nob" (Tier 1, item 7)** — real, dictionary-listed informal word (British/Irish slang for a
  wealthy person, or slang for "head"), confirmed via dictionary lookup. Replaced with "nof"
  (rhymes "off," not a real word).
- **"glout" (Tier 4, item 6)** — real, obsolete English word (Scots-derived, "to sulk / stare
  sullenly"), confirmed on Wiktionary. Replaced with "plout" (rhymes "shout," confirmed not an
  English word on Wiktionary — only a Czech word with that spelling).

Worth naming plainly: Tier 1 alone has now had real-word pseudowords caught and fixed in three
consecutive rounds ("rob" in Round 2, "gan" and "nob" in this round's sweep) despite each prior
round explicitly re-checking that tier. The recurring cause is that rhyme-phoneme verification
(what Round 2's fix log used) and real-word-status verification are genuinely different checks,
and doing one does not catch failures in the other — this round's fix applies both checks to
every item for the first time, not just the ones a critic named.

**Repo-wide citation grep:** searched every `.md` file for "Wanzek" and `research/03` §5
citations. Found one additional sibling defect **outside level-0's scope**:
`course/level-4/lessons/L4.16-level-4-mastery-check.md` line 48 also cites "(Wanzek et al.)" for
a claim about targeted vs. broad reteaching — not verified against the source this round (out of
scope for a level-0 builder; flagging for whichever agent next touches `course/level-4/`). No
other Wanzek citations found outside `research/03` itself (the primary source, correctly cited
there) and the two level-0 files now fixed.

**Defects closed this round: 4/4 named + 3 sibling pseudowords found and fixed in the sweep.**
Across all three rounds: 20/20 defects closed. The placement instrument's Stage 1/3/4 core
design has now survived three independent critic passes (structural validity, then completeness/
consistency, then a full sibling sweep) without a design-level defect surfacing in the last two
rounds — remaining risk is now bounded to "another obscure real word neither dictionary sweep
nor targeted lookup caught," which is a residual, not a structural, gap.
