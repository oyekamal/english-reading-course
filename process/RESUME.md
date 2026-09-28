# RESUME — read this first if the session ended

If tokens run out or the session dies, a fresh Claude session can pick up from here.
Say: **"resume the english reading course from RESUME.md"**.

Everything important lives on disk and in git. Nothing depends on the old conversation.

## What this project is
A free, research-backed English reading course for ANY age (kids → adults, native + Urdu-first ESL),
from absolute beginner → advanced (CEFR C1 / PIAAC 4–5). Built with a **gauntlet loop**:
Sonnet builders write each level → a separate harsh Sonnet critic compares it (blind) against a real
published program + the research → builder fixes → repeat until the critic says OURS WINS.
Final output: markdown course in this repo + a published artifact page.

## Where things are
| Path | What |
|---|---|
| `research/01`–`07` | DEEP RESEARCH (done, ~28k words, cited). Never delete. |
| `DESIGN.md` | The contract: evidence verdicts, 12 rules, level table, master phonics sequence, lesson template |
| `course/level-N/` | Built levels. `GAUNTLET.md` in each = critic/builder rounds log |
| `tools/decodable.py` | Decodability checker for L1–L4 texts (`python3 tools/decodable.py course/level-2/lessons/`) |
| `PROGRESS.md` | Live status table — update after every agent finishes |
| `LOG.md` | Append-only timeline of every event (what happened, when) |

## How to resume
1. `cat PROGRESS.md` — see which levels are at which round.
2. `git log --oneline` — last checkpoint.
3. For any level whose builder finished but has no critic round → run the critic (prompt template below).
4. For any level whose last GAUNTLET.md entry is a critic with REFERENCE WINS → send the builder the worklist
   (a new builder agent: "read DESIGN.md + course/level-N/GAUNTLET.md, fix every defect in the latest critic round,
   append a '## Round N builder' section").
5. If a level folder is missing or has fewer lessons than DESIGN.md §3 says → rebuild it with a builder agent
   (prompt: read DESIGN.md + relevant research files, build course/level-N per the master sequence).
6. Loop until every level's latest critic says OURS WINS. Then: root README.md, the artifact, commit.

## Critic prompt template (Sonnet, general-purpose agent)
"You are a HARSH critic in a gauntlet loop. Praise is useless. Project: .
Contract: DESIGN.md. Under review: course/level-N/. STEP 1: fetch the REAL reference (see PROGRESS.md 'bar' column) —
actual published material, not descriptions (PDFs: curl + pdftotext). STEP 2: blind side-by-side on a comparable chunk —
which would an expert pick? STEP 3: audit every DESIGN.md §2 rule, accuracy, facts, decodability
(run tools/decodable.py for L1–L4), adult dignity, usability. OUTPUT: append '## Round N critic' to course/level-N/GAUNTLET.md:
VERDICT (OURS WINS / REFERENCE WINS), SINGLE BIGGEST GAP, numbered defect worklist with file + location + exact fix."

## Web search note
WebSearch has a shared per-session cap. Fallback: a DuckDuckGo search script (any web-search fallback works).

## HANDOFF SNAPSHOT — 2026-09-28 (session at 85% context)
Agents that were IN FLIGHT when this snapshot was written (they may have died with the session).
On resume, check each level's GAUNTLET.md: if the last section is the one listed as "running",
and it looks incomplete or missing, re-run that step.

| Level | In-flight step | If missing on resume, do this |
|---|---|---|
| 0 | Round 3 critic | run critic (template above; note "PAST-informed, not a PAST clone", judge the placement job vs PSC+DIBELS) |
| 1 | Round 1 builder (split lessons into 1-sound sittings + adult fast track, fix "car", Nat collision, align canonical heart words, clean checker) | new builder: fix latest critic worklist + those lead decisions |
| 2 | Round 1 builder (13 defects; canonical heart words incl. says/for/her; checker = gate) | new builder |
| 3 | Round 1 builder (NEW 18-lesson seq: ar 3.08, or 3.09 before vowel teams; canonical heart words; checker clean) | new builder, then R2 critic |
| 4 | Round 1 builder (15 defects; checker = gate; L4.12 VV split/VCCCV; L4.14 example fix) | new builder |
| 5 | Round 1 builder (10 defects; biggest = rewrite ALL Track B passages to FK 3–6) | new builder |
| 6 | Round 2 builder (rewrite L6.01–06 to 14–16 words/sentence; stop-and-check Qs) | new builder, then R3 critic |
| 7 | Round 2 builder (Palmes = present conflicting testimony; exact Adams quote; constructed labels; 2nd visual) | new builder, then R3 critic |

Lead decisions already made (don't re-litigate):
- The bar = synthesis of the research + best real program per level (not one org). Kamal chose output = markdown + artifact.
- Placement test = PAST-informed, NOT a PAST clone (copyright).
- L1 pace = 1 new sound per sitting, 3–5/week, mastery-gated; adults may combine sittings if Check ≥90%.
- Checker output (tools/decodable.py) is the decodability gate, not builders' self-audits. Story lines only in `>` blockquotes.
- Canonical heart-word schedule in DESIGN.md §3 (L2 has says, for, her).
- L5 merged fluency+knowledge passage per session: accepted.
- Exit rule per level = latest critic says OURS WINS on its blind comparisons.

After all levels win: write root README.md, run ONE cross-level consistency critic (sequence/heart words/levels
line up L0→L7), then publish the artifact (load artifact-design skill first; Kamal wants both markdown + artifact),
commit, and mark board task #111 done .
- L3 sequence changed: ar/or/ore moved to Level 3 (3.08/3.09) before vowel teams. Don't revert — matches UFLI + RWI.

## SPEND-LIMIT NOTE (2026-09-28)
All agents were killed by the individual spend limit once. Partial edits are committed.
Resume in waves of ≤4 agents. Wave 1 resumed: L0 (R3 fixes), L3 (R1 + resequence), L6 (R2), L7 (R2).
Wave 2 still to resume: L1 (R1), L2 (R1), L4 (R1 + ar/or repurpose), L5 (R1: Track B → FK 3–6).
Each builder: check git diff for what's done → continue → run checker → append GAUNTLET builder section.

## STATUS: COMPLETE (2026-09-28)
All 8 levels won their gauntlets; consistency pass SHIP. Artifact: https://claude.ai/artifact/4ucgFCvxmrRcYTbzYehX5F
To change anything: edit markdown → run tools/decodable.py (L1–L4) → python3 tools/build_site.py → republish same URL.
