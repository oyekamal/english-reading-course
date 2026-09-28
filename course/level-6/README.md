# Level 6 — Reading to Learn

## Entry

You're ready for Level 6 when you've finished Level 5: you read connected text at roughly
100+ WCPM with normal expression (not word-by-word), you know 2,000–3,000 word families, your
heart-word list is complete, and you can decode a multisyllable word you've never seen using
the syllable-type/word-attack routine. Roughly CEFR A2–B1. If you're not sure, take the Level 5
mastery check first — Level 6 assumes decoding and basic fluency are no longer the bottleneck;
from here on, the work is almost entirely about understanding, remembering, and questioning what
you read, not about sounding words out.

## Exit — what "done" looks like

By the end of Level 6 you can:

- Read a genuinely complex non-fiction paragraph (CEFR B2) and explain what it's really saying,
  not just repeat words from it.
- Name **how** a piece of writing is organized — sequence, cause/effect, compare/contrast,
  problem/solution, or description — and use its signal words to help you understand it faster.
- Read several paragraphs and **connect** information across them, not just remember the last
  sentence you read (PIAAC Level 3 territory: "integrate information across paragraphs, some
  competing information" — research/06 §5).
- Run a shared close-reading routine on your own (predict, question, clarify, summarize) without
  someone else driving it.
- Notice a long, tangled sentence, a pronoun you've lost track of, a slippery "however," or a
  passive-voice sentence hiding who actually did something — and untangle it.
- Open a new tab and check who's behind a website or a claim before you believe it.
- Write a few honest sentences about what you just read — a summary, a response, a comparison.

That's roughly **CEFR B1→B2 / PIAAC Level 2→3** (research/06 §5's level-exit table). It is not
"advanced" yet — Level 7 is where you learn to read a contract, a research paper, or a
politician's argument with real skepticism. Level 6 is where reading stops being about the
words and starts being about the ideas.

## What's different about this level

Levels 1–5 were mostly about you and the page: can you decode it, can you say it smoothly, do
you know the words. From here, most of the work is about **the text's structure and your own
thinking** — which is why the research base shifts too (see `research/06` in full, and
`research/04` §6 for why this applies just as much to adult/ESL learners as to teenagers).
Four things carry the level:

1. **A few comprehension strategies, taught briefly, not drilled for months.** Question
   generation, summarizing, monitoring, clarifying/inference, and predicting each get one
   lesson of real, explicit teaching — then they disappear into ordinary reading. The
   research is blunt about this: strategy instruction has a real but small effect, and
   *drilling* it past the first lesson doesn't buy you more (research/06 §1.1, Willingham;
   Okkinga d=0.186–0.786 depending on measure). We spend the saved time on knowledge instead.
2. **Reciprocal teaching as the standing routine.** From L6.01 you'll learn 4 roles —
   Predictor, Questioner, Clarifier, Summarizer — first fully modeled by a tutor, then shared,
   then run by you alone. This one routine carries almost every close-reading session for the
   rest of the level (research/06 §1.4, Rosenshine & Meister 1994).
3. **Four knowledge units that build on each other**, each with 3–4 real, original,
   fact-checked texts: the human body & health, Earth/climate/water, how governments and money
   work, and a history thread (Indus Valley → Mughal era → Partition). Content-rich text sets
   like this are the single biggest lever for reading comprehension at the ceiling levels
   (research/06 §1.2, §2 rule 2) — a course that teaches "skills" on content-free passages
   plateaus here; one that builds real knowledge doesn't.
4. **One text set for everyone.** From this level on, a 14-year-old and a 45-year-old read the
   exact same text — the content (health, water, money, government, history) is naturally
   relevant to both. Where a strong young reader needs an age-appropriate angle, the lesson has
   a small "Kids-track note," not a rewritten text (DESIGN.md rule 6, extended: at this reading
   level, register differences matter less than they did for CVC decodables).

## Text complexity: what we actually measured (and got wrong once)

The B1→B2 exit claim above isn't just asserted — it was checked, twice, because the first check
was wrong about *why* the numbers looked the way they did.

**Round 1** ran every text through Flesch-Kincaid Grade Level and blamed the high scores on
domain vocabulary (technical/proper-noun words like "immune" or "civilisation" inflating the
syllable-count term) — true as far as it went, but incomplete. **Round 2** decomposed the
formula itself — `FK grade = 0.39 × (words/sentence) + 11.8 × (syllables/word) − 15.59` — and
found the **sentence-length term was doing equal or more work than the vocabulary term**,
especially in the early lessons: L6.01 opened at 22 words/sentence average, with individual
sentences running up to 50 words, *before the course had taught a single syntax tool* (chunking
doesn't arrive until L6.03, pronoun-tracing until L6.04). That's real syntax load a genuine B1
entrant hits cold — a different problem from vocabulary load, and one the Word-work/Prime-the-
topic steps do nothing to fix. Relabeling the exit claim instead of shortening the sentences was
a rationalization, not a fix, and the second round said so.

**The actual fix:** L6.01–L6.09 were rewritten — not relabeled — to a controlled sentence-length
ceiling (splitting compound/complex sentences into shorter ones, keeping every fact, every
signal word, every taught vocabulary word, and each lesson's own deliberately-long syntax-focus
example sentence exactly as designed). L6.10–L6.16 were left untouched, because their higher
complexity is the intentional second half of the ramp, arriving only after all 5 text structures,
all 6 strategies, and all 4 syntax tools have been taught. Average sentence length (ASL) is now
tracked as its own metric, separately from FK grade, for exactly this reason — a single number
had let two different problems hide behind each other.

Measured after the rewrite (`textstat`; ASL = words per sentence in the main knowledge text,
stop-and-check callouts excluded from the count):

| Lesson | Words | ASL (words/sentence) | FK grade | Reading ease |
|---|---|---|---|---|
| L6.01 | 493 | 14.9 | 8.1 | — |
| L6.02 | 446 | 11.4 | 6.5 | — |
| L6.03 | 423 | 17.3 | 9.4 | — |
| L6.04 | 446 | 12.7 | 9.7 | — |
| L6.05 | 560 | 14.0 | 6.5 | — |
| L6.06 | 442 | 13.7 | 7.2 | — |
| L6.07 | 457 | 13.3 | 8.4 | — |
| L6.08 | 460 | 15.7 | 9.0 | — |
| L6.09 | 578 | 16.0 | 8.3 | — |
| L6.10 | 568 | 25.9 | 12.0 | — |
| L6.11 | 578 | 27.3 | 15.1 | — |
| L6.12 | 585 | 26.6 | 13.3 | — |
| L6.13 | 572 | 29.1 | 14.6 | — |
| L6.14 | 576 | 20.8 | 11.4 | — |
| L6.15 | 610 | 28.3 | 15.5 | — |
| L6.16 | 509 | 30.4 | 16.7 | — |

(Reading Ease column intentionally left blank here — track FK grade and ASL going forward, per
Round 2's finding that a single blended number hides which variable is doing the work; recompute
Reading Ease from the same extraction if a future round wants it.)

Two honest findings now, not one rationalized one:

1. **The ramp is real and controlled.** ASL runs 11–17 words/sentence through L6.01–L6.09 (true
   B1-appropriate load, ramping gently upward as chunking, pronoun-tracing, connectives, and
   passive-voice unpacking are each taught and can be leaned on), then rises to 21–30
   words/sentence from L6.10 on, once every syntax tool exists. FK grade tracks the same shape:
   6–9 early, 11–17 late — roughly B1 at entry, B2 into C1-adjacent by the end, which is what the
   course actually claims.
2. **FK grade alone would still have hidden this.** A lesson can hit a "fine-looking" FK grade
   with either short-simple-sentences-plus-hard-words or long-sentences-plus-easy-words — two
   very different learner experiences. Tracking ASL separately is what makes the second one
   visible; that's now permanent practice for this level, not a one-time audit.

Net: the exit claim stands, and this time the sentences underneath it actually earned it — **entry
texts (L6.01–09) run true B1 sentence-length with taught vocabulary; L6.10–16 run solidly B2 into
C1-adjacent territory once every tool needed to handle that complexity has been taught.** The
Word-work and Prime-the-topic steps still matter for vocabulary load — they were never wrong,
just not sufficient on their own, which is the distinction Round 2 forced onto the record.

## The 16 sessions, in order

| # | Lesson | Text | Structure taught/reviewed | Strategy | Syntax focus |
|---|---|---|---|---|---|
| 1 | L6.01 | How Your Body Is Built | Description (teach) | Question generation (teach) | — |
| 2 | L6.02 | How Your Heart Keeps You Alive | Sequence (teach) | Summarizing + graphic organizer (teach) | — |
| 3 | L6.03 | Why We Get Sick — and How the Body Fights Back | Cause/effect (teach) | Monitoring/fix-up (teach) | Long-sentence chunking |
| 4 | L6.04 | Clean Water, Fewer Diseases | Problem/solution (teach) | Clarifying/inference (teach) | Pronoun reference |
| 5 | L6.05 | Salt Water and Fresh Water: Earth's Water Budget | Compare/contrast (teach) | Predicting (teach) | Connectives |
| 6 | L6.06 | The Water Cycle: A Journey With No End | Sequence (review) | folded in | Passive voice |
| 7 | L6.07 | Climate Change: One Cause, Many Effects | Cause/effect (review) | folded in | Stretch-text scaffold |
| 8 | L6.08 | Floods and Droughts | Problem/solution (review) | folded in | Review |
| 9 | L6.09 | Who's Behind This Page? | — | Lateral reading (mandatory module) | — |
| 10 | L6.10 | How Money Moves: Banks, Loans, and Interest | Description/sequence (review) | folded in | Long-sentence chunking (review) |
| 11 | L6.11 | How a Government Decides Where Money Goes | Sequence/cause-effect (review) | folded in | Connectives (review) |
| 12 | L6.12 | Taxes: Why We Pay Them and What They Buy | Problem/solution (review) | folded in | Pronoun reference (review) |
| 13 | L6.13 | Inflation: One Cause, Many Effects on Your Wallet | Cause/effect (review) | folded in | Passive voice (review) |
| 14 | L6.14 | The Indus Valley Civilisation | Description/sequence (review) | folded in | Review |
| 15 | L6.15 | From Mughal Court to Colonial Rule | Cause/effect/sequence (review) | folded in | Comprehensive review |
| 16 | L6.16 | Partition: One Decision, Two Countries | Cause/effect (review) | folded in | Review — CAPSTONE |

Units A–D (body/health, earth/water/climate, government/money, history) each end in a short
writing-to-read **synthesis** task comparing texts within that unit; L6.16 ends in a synthesis
across all four units plus a final applied lateral-reading task, and hands off to Level 7.

## Format

Each session is 30–45 minutes and follows the same seven-part shape (full template in
`DESIGN.md` §4): retrieval warm-up → word work (2–3 Tier-2 vocabulary words, each flagged for a
real Urdu loanword/cognate where one genuinely exists — see `word-list.md`) → fluency or close
reading (this is where the syntax focus lives) → **prime the topic** (3–5 min: plain-language
topic framing, 2–3 key facts, one orienting question linking to what the learner already knows,
with a local/Pakistani link where natural — IES Recommendation 3A, strong evidence) → the
knowledge text plus reciprocal-teaching discussion, gated before each release-stage advance in
L6.01–L6.05 → write-to-read → check (5 questions, answer key, pass rule, plus a Support prompt
for a learner who falls short and a Challenge extension for one who's ready to go further). Every
text is given in full, inline, in its lesson file — nothing else to fetch or print.

## Pacing and pause-safety

Same rules as every other level (see `course/level-0/start-here.md`): no penalty for stopping
and returning, no streaks, no age-gating. If you already know a lesson's content, take its
Check first; pass it, move on. Most learners will do one session most days; that's ~3–4 weeks
for the whole level at that pace, faster if you go daily, slower if you don't — there's no
clock here, only the mastery check.

## When you're done

Take `mastery-check.md` in this folder. It tests all five pieces at once — text-structure ID,
reciprocal-teaching application, syntax, a lateral-reading mini-task, and a knowledge check
across all four units — with a clear pass rule and what to review if you don't clear it the
first time. Passing it means you're ready for **Level 7: Advanced & Critical**.
