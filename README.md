# Read English — a free, research-backed reading course for any age

This course takes a learner from **not knowing a single letter** to **reading a policy paper critically** (CEFR C1 / PIAAC Level 4–5).

The same course works for:

- a 5-year-old
- a teenager who fell behind
- an adult learning to read for the first time
- an Urdu-first ESL learner

Learners are placed by skill, not by age. Every story comes in a **child** version and an **adult** version, and both teach exactly the same skill.

**Read it online:** https://oyekamal.github.io/english-reading-course/ (the whole course, the research and the build record in one page).

**Start here → [`course/level-0/start-here.md`](course/level-0/start-here.md)**, then take the [placement test](course/level-0/placement-test.md). It takes about 20 minutes and a parent can give it.

## The levels

| Level | Name | What you learn | Lessons | Ends at |
|---|---|---|---|---|
| 0 | [Start Here](course/level-0/start-here.md) | Placement test, reading-difficulty screener, tutor/parent guide, guide for Urdu speakers | — | Placed |
| 1 | [First Sounds](course/level-1/README.md) | Hearing sounds; every single letter; reading and spelling 3-letter words | 14 | Pre-A1 |
| 2 | [Sounds Together](course/level-2/README.md) | sh ch th wh ng nk, blends, -s -es -ed -ing, 2-syllable words | 14 | A1 |
| 3 | [Long Vowels](course/level-3/README.md) | Silent e, open syllables, y, soft c/g, ar, or, vowel teams | 18 | A1 |
| 4 | [The Full Code](course/level-4/README.md) | r-controlled vowels, oi/ou/aw, silent letters, -tion/-ture, syllable division, schwa, long words, first real-world texts | 16 | A1–A2 |
| 5 | [Word Power & Fluency](course/level-5/README.md) | Prefixes, suffixes, Greek/Latin roots, reading fluency, Readers Theatre, vocabulary | 16 | A2–B1 |
| 6 | [Reading to Learn](course/level-6/README.md) | Comprehension, text structure, reciprocal teaching, knowledge units (body, climate, money and government, Indus to Partition), checking sources | 16 | B1–B2 |
| 7 | [Advanced & Critical](course/level-7/README.md) | Reading history sources, science, arguments, contracts and data; lateral reading; synthesis; literature | 14 | C1–C2 |

## Why you can trust it

- **Built from the evidence, not from one program.** Seven research reports (`research/01`–`07`, about 28k words, all cited) reviewed synthetic phonics, analytic phonics, whole language, balanced literacy, Orton-Gillingham, adult and ESL literacy, fluency, vocabulary, morphology and comprehension. [`DESIGN.md`](DESIGN.md) records what we kept and dropped from each method, and why.
- **No guessing.** Learners are never told to "look at the picture" or "think what would make sense" to work out a word. The research rejects this three-cueing approach.
- **Decodable texts that really are decodable.** In Levels 1–4, every practice story uses only the sounds and spellings already taught. [`tools/decodable.py`](tools/decodable.py) checks this automatically.
- **Tested against the best real programs.** A separate, harsh critic agent compared each level blind against a published benchmark:
  - UFLI Foundations
  - the UK Phonics Screening Check and DIBELS 8
  - REWARDS and Rasinski's Fluency Development Lesson
  - Core Knowledge (CKLA)
  - Stanford's Reading Like a Historian and Civic Online Reasoning

  Each level was revised until ours won. The full record is in each level's `GAUNTLET.md`.

## Using it

- **Time:** short, frequent sessions of about 20–30 minutes, most days. Pausing never costs you progress.
- **Who teaches:** a parent, a tutor or a teacher. Adults from Level 5 on can also work alone.
- **Materials:** paper and a pencil. A phone for recording yourself helps.

## How this was made

This course was researched, written and reviewed by AI agents (Claude). A human, the repo owner, set the goal and made the key decisions. Every step is recorded here, so you can check the reasoning rather than trust it:

1. **Research** ([`research/`](research/)): seven parallel research agents, one per method or area. Each report lists what to keep, what to drop, and what's still contested, with citations and effect sizes.
2. **Design** ([`DESIGN.md`](DESIGN.md)): the research turned into one contract: a verdict on each method, 12 rules, the level table, the exact phonics sequence and the lesson template.
3. **Build:** one builder agent per level wrote the lessons to that contract.
4. **Gauntlet review** (`course/level-N/GAUNTLET.md`): for every level, a separate harsh critic fetched a real published program and compared it with ours blind. Then it listed every defect with an exact fix, the builder fixed them, and a fresh critic checked again. This repeated until ours won, taking 2–4 rounds per level. The logs keep every round, including the losses and the mistakes the critics caught: factual errors, nonsense words that turned out to be real words, and spellings used before they were taught.
5. **Consistency** ([`process/CONSISTENCY.md`](process/CONSISTENCY.md)): a final review of the joins between levels.

The timeline is in [`process/LOG.md`](process/LOG.md), and the status table is in [`process/PROGRESS.md`](process/PROGRESS.md).

**Limits.** The course has not yet been piloted with real learners, and the judges were AI critics working from real reference material. Please report problems or pilot results as GitHub issues.

## License

- **Course content, research and documentation:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You may use, adapt and share it, including commercially, with attribution.
- **Code in `tools/`:** MIT.

Reference programs quoted briefly in the review logs (UFLI Foundations, CKLA, DIBELS, the Phonics Screening Check and others) belong to their owners. They are excerpted only for comparison.

## Project files
`DESIGN.md` (the contract) · `research/` (evidence) · `course/` (the course) · `process/` (build log, status, consistency review, restart notes) · `tools/decodable.py` (decodability checker) · `tools/build_site.py` (builds `docs/index.html`)
