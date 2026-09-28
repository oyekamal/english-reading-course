# Level 2 — Gauntlet Log

## Round 1 critic

### VERDICT: REFERENCE WINS

On the one axis that cannot be fudged for a structured-literacy product —
**every word in a decodable text must actually be decodable** — UFLI Foundations
beats this draft of Level 2 as shipped. UFLI's Lesson 45 ("The Ship," `sh`) and
Lesson 52 ("Stink in the Bank," `nk`) decodable passages (fetched from
`ufli.education.ufl.edu/.../UFLI-Foundations-Decodables-ALL.pdf`) are tightly
built from only what has been taught up to that lesson, using a small, deliberately
managed recurring cast (Buzz, Mack, Rick, Hank, King, Ash) so new vocabulary load
stays near zero. This course's own pedagogy (heart-word method instead of rote
sight-word drilling, dual Track A/Track B register, explicit Urdu-interference
tips, embedded Tier-2 vocabulary + comprehension, a real fluency routine from
2.06 on) is **more ambitious and, where it's executed cleanly, better designed**
than UFLI's plainer approach — but the actual Level 2 texts do not currently
meet the "decodable = decodable" bar (DESIGN.md rule 2) they claim to meet, and
the self-authored "Decodability audit" footers that are supposed to prove it are
themselves unreliable. An expert reading specialist handed both lesson sets
tomorrow would pick UFLI's for a beginning Urdu-L1 or child learner precisely
*because* it can be trusted at face value; this course's Level 2 cannot yet be,
even though its underlying design is worth fixing rather than discarding.

### SINGLE BIGGEST GAP

**The level's own "Decodability audit" sections are not trustworthy, and two of
the most-used words in the entire level — "says" and "for" — are never once
taught or flagged, despite appearing in nearly every lesson from L2.02 onward
and despite both being standard, early-taught tricky/heart words in every
mainstream program checked** (UFLI teaches "for" freely from Lesson 51 on and
Letters & Sounds' Year 1 Common Exception Word list — the direct analogue of
this course's "heart word" — explicitly includes both "said" **and** "says"; see
`hollinswoodprimary.co.uk/media/2829/tricky-word-list.pdf`). This course already
heart-words the near-identical-shape sibling words "said" (Level 1), "goes,"
and "does" (Level 2) — it simply forgot "says," the single most common dialogue
tag in its own texts. "for" needs the r-controlled `or` this course defers to
Level 4.02, yet is used as a plain function word in almost every Track A/B text
starting at L2.01. Because neither omission was ever caught, every lesson's
claim of "100% decodable, no flags" or "~9X% decodable" is an undercount, and
the problem reaches all the way into the **Level 2 mastery-check gate passage
itself** (see #6 below) — meaning a learner could currently be failed, or
falsely passed, on Level-4-only content inside the instrument meant to certify
Level 2 mastery.

### Prioritised defect worklist

1. **`says` used untaught, unmarked, and unflagged in nearly every lesson.**
   Files: `L2.02` (×2 in-text), `L2.03` (×3), `L2.04` (×2), `L2.05` (×2),
   `L2.06` (×4), `L2.07` (×1), `L2.08` (×3), `L2.09` (×3), `L2.11` (×3),
   `L2.12` (×2) — section 7 blockquotes, listed plainly (no `*`/`(heart)`
   marker) in each lesson's own "Decodability audit." `says` is /sɛz/, not
   decodable from taught GPCs, and is absent from every Level 1 and Level 2
   heart-word list in DESIGN.md and each README.
   **Fix:** add `says` as a heart word — cheapest fix is pairing it with `said`
   retroactively at Level 1 (L1.06 or L1.09, both already teach a heart word),
   since it's needed for dialogue from Level 1 onward too; alternatively
   introduce it explicitly at L2.02 alongside `were/from` and mark it in every
   later lesson's heart-word recap. Either way, update all 10 affected lessons'
   "Decodability audit" sections to show it marked, and re-tally the percentages.

2. **`for` used untaught, unmarked, and unflagged as a plain function word
   throughout the level.** Confirmed present in reader-facing text (not just
   questions) in `L2.05` Track B, `L2.06` Track A/B, `L2.07` Track B (×3+),
   `L2.09` Track A/B (repeatedly), `L2.10` Track A/B, `L2.12` Track A/B,
   `L2.13` Track A/B. `for` requires the r-controlled `or` grapheme, not taught
   until L4.02 in this course's own master sequence.
   **Fix:** add `for` to the Level 1 heart-word list (it sits naturally beside
   `of`, already there) so it is legitimately available for the rest of the
   course, and retag every "no flags"/percentage line in the 9+ affected
   lessons that currently ignores it.

3. **Inconsistent flagging of the same recurring word across lessons —
   `home` and `first` are caught in some lessons and silently missed in
   others.** `home` (VCe, not taught until L3.01) is correctly flagged in
   `L2.07` Track B and `L2.09` Track B, but appears completely unflagged in
   `L2.04` Track B ("...to plan his bus home") and `L2.13` Track A ("...and
   went home, glad and full"). `first` (r-controlled `ir`, L4.03) is
   unflagged in `L2.04` Track A/B and `L2.07` Track B ("but first, the job").
   **Fix:** run a level-wide find for both words, decide once (heart-word,
   flagged pre-taught exception, or cut), and apply that decision everywhere
   the word occurs — not lesson-by-lesson improvisation.

4. **`about` used unflagged.** L2.04 Track A ("thinks about a moth"; "forgets
   all about the hat") and L2.05 Track A ("I will sing about a king"). Contains
   `ou`, not taught until L4.06. Not flagged in either lesson's audit.
   **Fix:** flag + pre-teach, or replace with an already-taught alternative
   phrasing ("thinks of a moth").

5. **`walk`/`walks` used in `L2.05` Track B ("Sam ... walks off") and treated
   as "plain `-s`, no flag" in that lesson's own audit** — but `walk` is
   explicitly scheduled as a **Level 3** heart word in DESIGN.md §3
   ("walk, talk" — L3.13), not yet taught anywhere the learner has reached at
   Level 2. This is a real sequencing violation dressed up as a non-issue by
   the audit's own wording.
   **Fix:** remove `walk(s)` from L2.05 Track B (e.g., "Sam heads off" or
   "Sam leaves"), or explicitly flag it as a pre-taught Level-3 exception like
   `busy`/`morning`/`shift` are elsewhere in the level.

6. **The Level 2 mastery-check gate passage itself contains an unflagged,
   untaught r-controlled word.** `course/level-2/mastery-check.md`, Component
   5 passage: "A rabbit ran past the bin... because it is not **hurting** us."
   `hurting` contains `ur` (r-controlled, L4.03) and is not flagged at all —
   the passage's only noted exception is `past`, which is actually **fully
   decodable already** (p + a + st, all taught by L2.07) and should not be
   flagged at all. The one real problem word in the highest-stakes text in the
   whole level was missed while a non-problem was flagged instead.
   **Fix:** replace `hurting` with an already-decodable word ("it is not a
   pest" / "it is not a bother" needs its own check, or simplest: "because it
   will not hurt us" still has the same `ur` — restructure the sentence
   entirely, e.g. "because it did not do a bad thing"), and drop the false
   `past` flag.

7. **Mastery-check Component 1 has an internal word-count contradiction and a
   failing pass threshold.** The heading reads "(one from every Level 2
   pattern, **24 words**)" but the list that follows has **28** words, and the
   footnote says "≥90% = at least 25 correct" — 25/28 = 89.3%, which is
   *below* 90%, not at or above it.
   **Fix:** correct the heading to 28 words and the threshold to "at least 26
   correct" (26/28 ≈ 92.9%), or trim the list to a number where the stated
   correct-count is genuinely ≥90%.

8. **Mastery-check Component 2 pseudoword list contains a real English word.**
   `splint` (a splint for a broken bone) is listed among "alien words — no
   meaning" pseudowords (`shob, chib, thron, whass, zink, strab, splint,
   thruv, fand, nusk, florbes, flisked`). A learner who recognises it as a
   real word breaks the point of the pseudoword measure.
   **Fix:** replace with a genuine nonce word, e.g. `splond` or `splunt`.

9. **Mastery-check Component 3 dictation sentence uses `busy`, a Level 3
   heart word (L3.13 in DESIGN.md), inside the Level 2 exit gate**, honestly
   footnoted as a "flagged pre-taught story word" with scoring carved out —
   but a pass/fail *gate* instrument should be built entirely from
   already-certified Level 1–2 content, not need its own footnoted exception.
   **Fix:** rewrite the dictation sentence with only Level 1–2 taught content
   and heart words, e.g. "My friend wanted to help because the shop was full."

10. **The hand-authored "Decodability audit" footer in every lesson is
    unreliable and cannot currently be trusted at face value** — it both
    misses real violations (items 1–6 above) and sometimes over-flags
    non-issues (item 6's `past`), with no consistent method behind which words
    get caught. Every "100% decodable, no flags" claim in the level (at least
    `L2.01` Track B, `L2.03` Track A, `L2.07` Track A) is currently false as
    written once `says`/`for` are counted.
    **Fix:** stop hand-authoring the audit prose from memory; regenerate it
    from a corrected `tools/decodable.py` run (see #11–12) and only add
    hand judgment on top of the tool's raw flag list, not instead of it.

11. **`tools/decodable.py`'s own `HEART` schedule is off by one lesson against
    the real Level 2 sequence**, e.g. tool key `"2.02"` holds `there where`,
    which the README and `L2.01-sh.md` actually introduce **at lesson 2.01**;
    `"2.03"` holds `were from`, introduced at 2.02; and so on through the
    2.05/2.06 split (tool combines `put push pull full` into one key when the
    real schedule is `put push`@2.05, `pull full`@2.06). This produces false
    positives such as the tool's own `2.01 ... untaught=Where there` result.
    **Fix:** correct every `HEART` key in `tools/decodable.py` to match the
    exact per-lesson introduction point in `course/level-2/README.md`'s
    "Heart-word schedule at a glance" table.

12. **`tools/decodable.py` mis-parses `all`/`wall` as the untaught `al`
    grapheme (Level 4.07) instead of the already-taught FLOSS `ll` doubling
    (Level 1.10)**, because both are 2-character candidates and the greedy
    parser tries `al` first when `positional_ok()` happens to pass. This
    pollutes the `untaught=` output for `L2.04` and `L2.13` with noise that
    could hide a real issue behind a false one.
    **Fix:** in `graphemes()`/`positional_ok()`, prefer an already-taught
    doubled-consonant match over an untaught longer-key match at the same
    position, or special-case `all/wall/ball`-shaped short words.

13. **No enforced ceiling for how undecodable a Track A/B text is allowed to
    be, only ad hoc "under the ceiling" prose per lesson.** By each lesson's
    own (undercounting) tally, `L2.04` Track B is ~93% and `L2.11` Track B is
    ~91% — already brushing the level's stated ≥95% target before `says`/`for`
    are even added back in; once they are, several Track B texts are likely
    closer to 85–90% real decodability. DESIGN.md and the README both state
    ≥95% as the target, but nothing in the level enforces a hard cap (e.g.
    "≤2 pre-taught exceptions per text, else rewrite") — the fallback is
    always "pre-teach as a whole-word story word," applied as many times as
    needed.
    **Fix:** add an explicit rule (DESIGN.md §2 or the Level 2 README) capping
    pre-taught exceptions per text (e.g. ≤2 in Track A, ≤3 in Track B) and
    require a rewrite, not another footnote, past that cap.

### What to hand back to the builder before Round 2

Fix items 1–2 first (they alone would move most lessons several points closer
to ≥95% and are one-line heart-word-list additions), then item 6 (the gate
passage is the highest-priority single file), then 7–9 (mechanical/measurement
bugs in the mastery-check instrument), then sweep 3–5 and 10–13. Re-run
`python3 tools/decodable.py course/level-2/lessons/` after 11–12 are fixed and
require every lesson to clear 95% for real before the next gauntlet round.

## Round 1 builder

Fixed all 13 numbered defects plus the two follow-on issues the fixes themselves
surfaced. Work was interrupted once by a spend-limit cutoff mid-lesson (L2.10) —
the partial edit was already committed to git (`git log --stat -- course/level-2`
shows the `partial:` commit), picked back up from there instead of redone.

**What changed:**

1–2 (`says`/`for` never taught, silently used everywhere). Fixed at the root: the
canonical heart-word schedule in DESIGN.md §3 now starts `2.01: says for` and
every later pair shifts one lesson later than the original draft (`2.02: there
where`, ... `2.11: many any her`, `2.12: does goes two`, `2.13: again friend
because` — `her` was added to 2.11 mid-fix once "her" turned out to be needed
constantly and irregular the same way `for`/`your`/`four` already were). Every
lesson's own §6 "Heart word(s)" section was rewritten to teach the *correct* pair
for its number, and every Track A/B story was rewritten around the real
cumulative heart-word set available at that lesson — not patched with a footnote.

3–6, 10 (inconsistent/wrong hand-audits; `home`/`first`/`about`/`walk(s)` leaking
in; the mastery-check gate passage's `hurting` missed while the fully-decodable
`past` was falsely flagged). All 14 lesson files' "Decodability audit" sections
were deleted and replaced with the literal output of
`python3 tools/decodable.py course/level-2/lessons/<file>.md`, plus a short human
note only where the tool's own known limitations needed explaining (see below) —
never a hand-written word-by-word tally again. The mastery-check Component 5
passage was rewritten (`buses`→`vans`, dropped a stray `small`/`shift`, "hurting"
→ "bad") and independently verified at 100% by running the tool against a temp
copy under a fake lesson number, since `mastery-check.md` doesn't match the
`L\d\.\d\d` filename pattern the tool scans directories for.

7–9 (mastery-check math/content bugs). Component 1 heading now says 28 (matching
its own list) and the threshold is ≥26/28 (≈92.9%), not the mathematically-false
≥25/28 (≈89.3%). Component 2's `splint` (a real word — a rigid support for a
broken bone) replaced with `splunt`. Component 3's dictation sentence no longer
uses `busy` (a Level 3 heart word); it uses `full` instead, already certified at
L2.07. Component 4's heart-word count and threshold were recomputed for the new
29-word canonical list (≥27/29).

11–12 (tool bugs). By the time this session resumed, `tools/decodable.py` had
already been corrected elsewhere (HEART schedule matches DESIGN.md exactly;
`ALL` is now sorted `(-len(x), x)` for deterministic tie-breaking instead of
hash-randomized set order; `positional_ok` keeps `al` gated on `wall/call/small`
being the real, untaught `/ɔː/` grapheme, not FLOSS doubling — an earlier attempt
in this same session to "fix" that as a false positive was itself wrong and got
reverted, correctly, by whoever picked the tool up next). Two smaller, genuine
tool quirks were found and are **documented, not silently patched around**,
because patching them looked more likely to introduce new false negatives than
to help:
  - Root words that happen to end in the letters `ing` (e.g. **string**) get
    misparsed as base+`-ing` and flagged as needing the L2.11 suffix early. Fix
    applied at the content layer: `string` stays in every isolated word/pseudoword
    list (correct, ungated practice) but was removed from connected story text
    before L2.11.
  - `-es` plurals whose base ends in a single `s`/`x`(excluded)/`z` right before
    the final vowel (`bus`→`buses`, not `box`→`boxes`, since `x` isn't in the
    VCe consonant class) get misread as the silent-e "VCe" pattern. Fix applied
    at the content layer: `buses` avoided in every connected story and in the
    mastery-check gate passage; `wishes/dishes/boxes/fixes/crashes/catches` carry
    the `-s/-es` teaching load instead, since digraph- or doubled-consonant
    endings don't collide with the VCe regex.
  Both are called out inline in the relevant lessons' audit sections so a future
  editor doesn't reintroduce `string`/`buses` into a story and wonder why the
  tool disagrees with them.

13 (no enforced ceiling on pre-taught exceptions). Added a new README.md section,
"Decodability gate: the tool decides, not the writer," stating the hard rule
going forward: ≤2 flagged words per Track A text, ≤2 per Track B text, else
rewrite, not footnote. Every lesson in this round shipped at 100% decodable
with zero flags, so the cap is currently unexercised but is now written down as
a real constraint rather than an ad hoc "under the ceiling" judgment call.

**Content mechanics used throughout the rewrite:** all replacement text stayed
inside DESIGN.md's non-negotiables — no r-controlled vowels (`ar/er/ir/or/ur`),
vowel teams, VCe, silent letters, or soft c/g anywhere in a Level 2 story;
`says`/`for`/`your`/`four`/`her`/`who`/`could`/`would`/`should` etc. carried as
heart words exactly as scheduled, never decoded; every Track A/B pair kept the
same register split (child home/play vs. adult job/cash/bus/shop) the level
already used, just re-plotted onto safe vocabulary.

**Pseudoword dictionary check** (explicit ask this round): every pseudoword in
every lesson's Blend-it and Check lists, plus the mastery-check's Component 2,
was grepped against `/usr/share/dict/words`. Two were real English words and
were replaced: `vang` (a real nautical term, a rope bracing a spar) → `zang` in
L2.05; `plonked` (real informal English, past tense of "plonk") → `flonked` in
L2.13. `splint` in the mastery-check (already caught by the critic as defect #8)
→ `splunt`. All three replacements re-checked against the dictionary: clean.

**Final verification — `python3 tools/decodable.py course/level-2/lessons/`:**

```
2.01  words=  98  decodable=100.0%  untaught=
2.02  words= 107  decodable=100.0%  untaught=
2.03  words=  99  decodable=100.0%  untaught=
2.04  words=  98  decodable=100.0%  untaught=
2.05  words=  96  decodable=100.0%  untaught=
2.06  words= 137  decodable=100.0%  untaught=
2.07  words= 111  decodable=100.0%  untaught=
2.08  words= 121  decodable=100.0%  untaught=
2.09  words= 102  decodable=100.0%  untaught=
2.10  words= 102  decodable=100.0%  untaught=
2.11  words=  92  decodable=100.0%  untaught=
2.12  words= 141  decodable=100.0%  untaught=
2.13  words= 218  decodable=100.0%  untaught=
2.14  words=   0  decodable=  0.0%  untaught=
```

(2.14 is the pointer-only mastery-check-day file with no section-7 story text of
its own — 0 words scanned is expected, not a failure; the real gate text lives in
`mastery-check.md` and was verified separately above at 100%, 87/87 words.)

Not touched this round, flagged for whoever runs Round 2: `tools/decodable.py`
is being edited by more than one process/session concurrently (visible from
"changed on disk since you last read it" notices and from the tool's own inline
`# fix:` comments crediting different rounds) — worth confirming there's a single
source of truth before the next gauntlet pass, or two builders' fixes could
silently race and revert each other again.

## Round 2 critic

### Fix verification

Ran `python3 tools/decodable.py course/level-2/lessons/` fresh: all 13 lessons
score 100.0% with empty `untaught=`, matching the builder's claimed final run
(L2.14 correctly shows `words=0` — pointer-only file, real gate text lives in
`mastery-check.md`). Confirmed by direct inspection, not just trusting the
printed log:

- **#1–2 (`says`/`for`)**: DESIGN.md §3 heart-word schedule now reads
  `2.01: says for`, and every lesson's own §6 "Heart word(s)" section teaches
  the correct pair for its number (checked all 13 lessons' §6 text in full,
  not just headings — every one of the 29 canonical L2 heart words is
  introduced exactly where the schedule says, with a real regular/irregular
  breakdown, not a stub). README.md's schedule table matches DESIGN.md
  verbatim. This is genuinely fixed, root-cause style, not patched over.
- **#3–5 (`home`/`first`/`about`/`walk`)**: grepped every lesson's §7 story
  text for these words plus a wider list (`ball, call, wall, small, tall,
  fall, around, along, above, awake, away, ago, happy, baby, funny, fly, cry,
  sky, try, shy, dry, why, how, now, down, town, cow, brown, found, old,
  cold, gold, find, mind, kind, most, post, host`) — zero hits anywhere in
  Level 2 connected text. Clean.
- **#6 (mastery-check `hurting`/false `past` flag)**: Component 5 passage
  rewritten, `hurting` is gone, `past` isn't used. Verified 100% via the
  tool's own graphemes/parses functions directly against the new passage
  text (not just trusting the builder's "verified separately" note) — see
  below, this component isn't actually clean for an unrelated reason.
- **#7–9 (mastery-check math/content)**: Component 1 now says "28 words" and
  lists 28; footnote correctly derives ≥26/28 (≈92.9%) as the real threshold.
  Component 2's `splint` → `splunt`, confirmed not a dictionary word. Component
  3's dictation sentence no longer contains `busy` — but see the new defect
  below, the replacement sentence isn't clean either. All arithmetic in
  Components 1/2/4 checks out on re-calculation.
- **#10–13 (tool bugs, audit provenance, ceiling rule)**: every lesson's
  "Decodability audit" section is now literal tool output plus a short human
  note, not hand-authored prose — confirmed by diffing the printed block
  against a live re-run for L2.08, L2.12, L2.13. `HEART`/`SEQ` in
  `tools/decodable.py` match DESIGN.md's schedule exactly. The `al`-before-
  `l/k/t` vs FLOSS-doubling fix is correctly reasoned (wall/call/small are
  real untaught `/ɔː/`, not short-vowel FLOSS) and the `(-len(x), x)`
  deterministic tie-break is a real fix for a real nondeterminism bug. A
  ≤2-flagged-words-per-track ceiling rule is now written into README.md.

**Round 1's 13 defects are genuinely fixed as claimed.** But hand-checking
the 4 required lessons (L2.01, L2.03, L2.06, L2.10) plus every other lesson's
§7 text and the full mastery-check for the specific sound-level leaks this
tool structurally cannot see turned up a new one, in the same
highest-stakes place Round 1 flagged before: the mastery-check gate.

### New defect found: `tools/decodable.py` cannot detect y-as-vowel leaks, and one made it into the gate itself

`tools/decodable.py`'s greedy parser falls back to single letters whenever no
taught multi-character grapheme matches (`graphemes()`'s `else: out.append(w[i])`),
and `parses()` treats **every** single letter as automatically valid
(`len(x) == 1` short-circuits the check) regardless of which *sound* that
letter is standing for in that word. `y` was taught in L1.12 as the
consonant /j/ ("yes"), so the tool silently accepts `y` in *any* position —
including word-final `y` saying /aɪ/ ("by," "my") or /iː/ ("happy"), which is
explicitly Level 3.06 content ("y as /ē/ and /ī/") not yet taught. Verified
directly against the tool's own functions:

```
>>> d.parses("By", g)   # g = known graphemes through L2.13
True   graphemes: ['b', 'y']
>>> d.parses("my", g)
True   graphemes: ['m', 'y']
```

This is the exact same *class* of bug as Round 1's `al`/FLOSS false-positive
fix, but running the other direction — a false *negative* that lets untaught
sound content through instead of wrongly flagging taught content. It reproduces
in real, currently-shipped connected text:

- `L2.08-three-letter-blends.md` — Track A: "**By** the end, / Sam is glad
  the job is done." Track B: "**By** the end of the week, the once-reluctant
  Bruno was trotting happily..."
- `L2.12-compounds-2syllable.md` — Track B: "**By** sunset, / the job is
  done..."
- `L2.13-review.md` — Track A: "...'I want to bring **my** pink rabbit,'"
  Track B: "'but **my** friend can help,'" and "**By** dusk, / the shop has a
  full stock..."

All four lessons' "Decodability audit" sections (which are now honest, literal
tool output per the Round 1 fix) correctly show `untaught=` empty for all of
these — because the tool itself cannot see the leak, not because a human
missed it. This is worse than a missed hand-check: it means the *newly
trusted* audit process from Round 1's fix #10 has a structural blind spot,
not just a one-off human error.

**It reaches the mastery-check gate exactly like Round 1's `hurting` did:**

- **Component 3 (Dictation), the replacement sentence added this round to fix
  defect #9**: *"**My** friend wanted to help because the shop was full."*
  — the very sentence written to remove the `busy` heart-word violation
  introduces a new, different violation in its first word.
- **Component 5 (Decoding passage)**: *"...**By** sunset, / the job was
  done..."* — same leak, in the level's single highest-stakes text, the one
  instrument meant to certify Level 2 mastery.

A learner tested on either component right now could be marked down for
mis-decoding a word ("by"/"my") that Level 2 never taught them the strategy
for (`y` as a long-vowel spelling isn't covered until L3.06) — precisely the
failure mode DESIGN.md rule 2 ("decodable = decodable") and Round 1's own
framing ("a learner could currently be failed... on Level-4-only content
inside the instrument meant to certify Level 2 mastery") were written to
prevent. The fact that this is a *narrower* recurrence (one grapheme class,
6 total occurrences across 3 lessons + 2 gate components, vs. Round 1's
sweep across nearly every lesson) is real progress, but the failure mode is
identical and it is again inside the gate.

### Blind comparison: L2.05 (ng/nk) vs. UFLI Lessons 51–52

Fetched the real UFLI passages via
`https://ufli.education.ufl.edu/wp-content/uploads/2023/02/UFLI-Foundations-Decodables-ALL.pdf`
(the round-1-cited URL 404s from a slightly different path; this one resolves)
— Lesson 51 "King and Ash Sing" and Lesson 52 "Stink in the Bank," the direct
ng/nk equivalent of this course's L2.05, next to `L2.05-ng-nk.md`'s Track A/B.

UFLI's texts have a small recurring cast and a real narrative arc with mild
tension and resolution: Hank searches methodically for a smell (checks his
desk, checks the fish tank, checks the back of the bank) before finding the
trash; King and Ash pick a song for King's mom and she reacts with delight at
the end. This course's Track A ("Min sings a song... Dad claps, and hangs a
pink hat on Min") and Track B ("Sam wants his job done fast... the king is
just junk") are decodable and readable but flatter — wanting an object and
getting it, with no search/complication step — and Track A's closing clause
("Dad claps, and hangs a pink hat on Min") reads slightly awkwardly compared
to UFLI's cleaner sentence rhythm. This is a real, if minor, prose-quality
gap, not close to disqualifying on its own — both are perfectly serviceable
decodables — but on pure craft an expert would nod at UFLI's tighter
storytelling first. Not counted as a numbered defect since DESIGN.md sets no
explicit narrative-arc bar; flagged for the builder's judgment on later
revision passes only.

### VERDICT: REFERENCE WINS (narrowly)

This course's design is still the more ambitious and, where clean, better
one — Round 1's assessment of the underlying pedagogy stands, and Round 1's
13 defects are genuinely fixed, not papered over. But the level still cannot
be trusted at face value on its own non-negotiable rule: the audit that is
supposed to prove "decodable = decodable" has a real, reproducible blind
spot, and — as happened in Round 1 — that blind spot's single worst instance
lands inside the mastery-check gate, in a sentence written *this round* to
fix a different gate defect. An expert handed both lesson sets today would
still pick UFLI's for a beginning Urdu-L1 or child learner on trust grounds
alone, though the gap is now much narrower than Round 1 (one grapheme class,
not a sweep) and this course's underlying design remains worth continuing to
fix rather than discarding.

### SINGLE BIGGEST GAP

`tools/decodable.py` treats every single-letter grapheme as automatically
taught regardless of which sound it represents in a given word, so it cannot
catch `y` doing untaught long-vowel duty (`by`, `my`) — and this exact leak is
now sitting inside both Component 3's dictation sentence and Component 5's
decoding passage in `course/level-2/mastery-check.md`, the two places this
project can least afford it.

### Prioritised defect worklist for Round 3

1. **Fix the mastery-check gate first (highest priority, mirrors Round 1's
   own escalation order).** `mastery-check.md` Component 3: rewrite "My
   friend wanted to help because the shop was full" to avoid word-initial
   `my` (e.g. "The rabbit ran because it was scared" needs its own check, or
   simplest: reorder around an already-certified opener, "A friend wanted to
   help because the shop was full"). Component 5: replace "By sunset," with
   an already-decodable connective ("When the shop shut," / "At six," /
   "When the job was done,").
2. **Sweep and fix the three lesson files.** `L2.08-three-letter-blends.md`
   (2 occurrences of "By"), `L2.12-compounds-2syllable.md` (1 occurrence of
   "By"), `L2.13-review.md` ("my" ×2, "By" ×1) — rewrite each sentence with
   already-taught vocabulary (e.g. "When the job was done," "At sunset,"
   "your friend"/"the friend" in place of "my friend," restructure the
   rabbit line to avoid "my pink rabbit," e.g. "the pink rabbit").
3. **Fix the tool's root cause, not just the content.** In
   `tools/decodable.py`, `y` needs to stop being an unconditionally-valid
   single letter. Concretely: track that `y` is only taught as consonant
   /j/ (word-initial, before a vowel: yes, yell, yak) until the lesson where
   `g.add("y")` currently fires (3.06); for lessons before 3.06, treat
   word-final `y` (or `y` not immediately followed by a vowel) as an
   *untaught* grapheme rather than a free single-letter pass — mirroring how
   `positional_ok()` already gates `al`/`gn`/`mb` by position. Re-run the
   existing `if __name__` assertions plus a new one (`assert not
   parses("by", {"b","y"})` before 3.06, `assert parses("yes", {"y","e","s"})`
   still holds) to lock the fix in.
4. **Re-run the full decodability check after 1–3** and require every lesson
   plus a standalone check of `mastery-check.md`'s Component 3 and 5 text to
   clear 100% *with the fixed tool*, not the current one, before the next
   round.
5. **Prose quality (non-blocking, optional polish):** consider giving L2.05's
   Track A/B (and similarly flat texts elsewhere) a small complication/search
   step before resolution, closer to UFLI's "Stink in the Bank" structure —
   not required by DESIGN.md, but would close the remaining craft gap an
   expert would notice in a side-by-side read.

## Round 2 builder (lead, direct)
Root cause fixed in tools/decodable.py: y-as-vowel (my, by) is now flagged before L3.06. Occurrences fixed: L2.08 "By the end"→"At the end"; L2.12 "By sunset"→"At sunset"; L2.13 My/my/By→His/the/his/At; mastery-check Component 3 "My friend"→"His friend", Component 5 "By sunset"→"At sunset". Also L3.03 "sat by the stove"→"sat next to the stove". Checker: L1–L3 all 100%.
Prose-arc polish (UFLI tighter narratives) noted as non-blocking → R3 critic decides.

## Round 3 critic

### Fix verification

- `python3 tools/decodable.py course/level-2/lessons/` → all 14 lesson files
  read, L2.01–L2.13 all `decodable=100.0%`, `untaught=` empty. `L2.14` (the
  stub lesson pointing at the real instrument) correctly shows `words=0` —
  it has no §7 text of its own by design.
- Grepped every occurrence of `my`/`by` across all Level 2 lesson files and
  `mastery-check.md`. All 6 occurrences the Round 2 builder claimed to fix
  are confirmed gone from every §7 "Read it" decoding section and from
  Components 3/5 of `mastery-check.md` (git-diffed `58339e6` to confirm each
  edit landed, not just claimed). Re-ran the tool's own
  `if __name__` assertion block — `assert not parses("my", ...)` /
  `parses("my", ...|{"YVOWEL"})` etc. still pass.
- Two remaining `by`/`my` hits were hand-checked and are **not** defects:
  `L2.08-three-letter-blends.md`'s "By the end of the week, the
  once-reluctant Bruno..." and `L2.03-th.md`'s "fix my bike, Grandpa" both
  sit inside "## 8. Listen & Talk (5 min)" — explicitly "Read aloud only,"
  out of `decodable.py`'s scan window (§7 only) and out of scope for
  DESIGN.md rule 2 by design (Listen & Talk is oral-language exposure,
  DESIGN.md rule 7). Round 2's own defect quote mislabeled this exact Bruno
  sentence as "Track B" text; it was never in the decoded track — the git
  diff shows only the genuine Track B line ("By the end, / Sam is glad...")
  was touched, correctly leaving the Listen & Talk passage alone.
- Hand-checked 3 other lessons' §7 text for the other leak classes named in
  the brief: no `all/ball/talk`-type `al` leaks (all `all/walk/old/cold/kind`
  hits outside `mastery-check.md` sit in tutor-notes prose or Listen & Talk,
  never in a decoded Track A/B line), no premature open-syllable `o`=/ō/ or
  schwa-heavy multisyllable words in decoding text before L2.12's compounds
  lesson introduces 2-syllable words at all. `mastery-check.md`'s own
  28-word/12-pseudoword/dictation/passage content hand-parses clean against
  the L2.01–L2.13 grapheme set.
- **New, smaller finding — a verification-process gap, not a content leak:**
  `mastery-check.md` is not itself inside `course/level-2/lessons/`, and its
  filename doesn't match `tools/decodable.py`'s `L(\d)\.(\d\d)` lesson-id
  regex, so `check()` silently returns `None` on it — running the tool
  directly against the file (`python3 tools/decodable.py
  course/level-2/mastery-check.md`) produces **zero output, not an error**.
  The one time this file's Component 5 passage was actually checked, per its
  own text (line 67–69), was by hand-copying it into a temp file "under the
  L2.13 lesson number" — a manual, undocumented, one-off workaround. Nothing
  stops the highest-stakes file in the level from drifting out of sync with
  the tool the course repeatedly cites as its proof of "decodable = decodable"
  the next time someone edits Component 3 or 5 text, exactly the failure mode
  that produced the Round 2 defect in this same file.

### Blind comparison: L2.06 (initial blends) vs. UFLI Lesson 36b

Fetched `UFLI-Foundations-Decodables-ALL.pdf` fresh (same URL Round 2 used)
and located UFLI's actual initial/final-blend passage — there is no
dedicated "initial blends" lesson number in UFLI's sequence; blends are
folded into "CCVC/CVCC advanced review" (Lessons 35c "Vlad the Crab," 36b
"Trip to the Pond") rather than getting their own decodable set like this
course's L2.06. Used 36b, the closer match to L2.06's word list:

> "Tim and his six dogs are on a trip to the pond. The dogs do flips in the
> mud and spin in the sand. Next, Tim and his six dogs jump in the pond for
> a swim. Tim said, 'I see a disk.' The dogs swim to get the disk. Tim and
> his dogs are wet. Drip! Drip! Drip! 'The trip to the pond was fun,' said
> Tim. 'Yip, Yip,' said the six dogs." (~72 words)

Next to L2.06's Track A (Min/pond/frog, 62 words) and Track B (Sam/shop, 72
words):

- **(a) 6-year-old:** a wash. UFLI's onomatopoeia ("Drip! Drip! Drip!,"
  "Yip, Yip") gives it a beat of sound-play and charm this course's Track A
  lacks — a small, real craft edge, same direction as Round 2's L2.05
  finding. But UFLI's passage also has zero narrative tension (dogs go to
  pond, get wet, the end) — no more of an "arc" than Track A's
  want-a-frog/settle-for-swimming beat. Neither text would make an expert
  hesitate to teach it tomorrow; this is a wash, not a UFLI win.
- **(b) adult beginner:** not close. UFLI has no adult register anywhere in
  this lesson (or, from the lesson-title sweep, anywhere in its Level-2-
  equivalent sequence) — "Trip to the Pond" is the *only* text UFLI offers a
  45-year-old ESL beginner at this decoding stage, and it is about six dogs
  jumping in mud. Handing that to an adult learner is a real dignity/
  engagement failure, not a neutral choice. This course's Track B ("Sam must
  push to get the shop's stock done... jots the stock on a pad... a big box
  hits the step") is genuinely adult workplace register, fully decodable at
  the same level, addressing exactly the population DESIGN.md rule 6 exists
  for and that UFLI's own published materials don't attempt to serve.

L2.06 also carries a specific, research-cited Urdu-L1 epenthesis drill
("sakool"/"iskool" for "school") and a full Tier-2 vocabulary block
("cautious," friendly definition, 2 examples, discussion questions) that
UFLI's decodables-only PDF has no equivalent of in the same document (UFLI
may cover vocabulary elsewhere in its full curriculum, not visible in this
PDF, so this is a same-artifact comparison, not a total-program one).

### VERDICT: OURS WINS

Round 2's REFERENCE WINS verdict rested entirely on a reproducible trust
failure — the tool's own certified "100% decodable" was provably false at
the exact place (the mastery gate) that can least afford it. That failure
is now genuinely fixed: `y`-as-vowel is correctly gated in the tool, all 6
cited occurrences are confirmed removed from every decoded section via git
diff (not just re-asserted by the builder), and a fresh hand-sweep for
other known leak classes (al/ball/talk, premature multisyllables, open-o)
found none. With the trust problem resolved, the two-register design (Track
B) and the Urdu-specific, research-cited tutor guidance are real, delivered
advantages this course has and UFLI's decodables-only PDF does not — UFLI
wins a narrow, non-blocking prose-craft point for young children and
nothing else. An expert handed both sets tomorrow would use UFLI only if
teaching exclusively young children and wanting battle-tested commercial
polish; for anyone including an adult learner in the room, or wanting the
Urdu-L1 support and vocabulary strand bundled in, this course is the better
choice as shipped.

### SINGLE BIGGEST GAP

`tools/decodable.py` has no way to check `mastery-check.md` — its filename
doesn't match the lesson-id regex the tool keys off, so pointing the tool at
it (directly or via the `lessons/` dir) produces silent zero output instead
of a real check, and the one verification this file's own text cites was a
manual temp-file workaround, not something CI or a future editor will
reliably repeat. The file that most needs an automated, repeatable
decodability gate is the one the tool structurally cannot run against.

### Prioritised worklist for Round 4 (polish, not blocking)

1. Give `tools/decodable.py` a way to check `mastery-check.md` directly and
   deterministically — e.g. a `--lesson-id 2.14` (or similar) CLI override
   so `python3 tools/decodable.py --lesson-id 2.14
   course/level-2/mastery-check.md` scans Components 3 and 5's actual text
   in place, without a hand-copied temp file. Re-verify Components 3/5 with
   it once it exists.
2. Consider folding `mastery-check.md` under `course/level-2/lessons/` (or
   giving the tool a config mapping non-`L*.md` gate files to their lesson
   id) so a plain `tools/decodable.py course/level-2/lessons/` sweep can
   never again silently skip the highest-stakes file, the same blind spot
   that let the Round 2 leak sit unnoticed in this exact file.
3. Optional prose polish (non-blocking, carried over from Round 2 note #5):
   give L2.06's Track A a small complication/resolution beat (e.g. does Min
   catch the frog or not) — UFLI's onomatopoeia-driven charm is matched, not
   exceeded, and a slightly more textured story would close even that gap.
4. No content or tool defects found this round beyond #1/#2 above — do not
   reopen the y-vowel fix or Round 1/2's 13+1 already-closed defects without
   new evidence.

## Round 3 builder (lead, direct)
tools/decodable.py now scans mastery-check.md (lesson id N.99 = whole level taught). L2 mastery-check: 100% (87 words). Level 2 status: OURS WINS (R3) → DONE.
