# PROGRESS — live status (update after every agent finishes)

Last updated: 2026-09-28

## Phase status
- [x] Phase 1 — Research: 7 Sonnet agents, all done → `research/01`–`07`
- [x] Phase 2 — Synthesis → `DESIGN.md`
- [x] Phase 3 — Build + gauntlet loop per level: ALL 8 LEVELS WON
- [x] Phase 4 — Root README, cross-level consistency (SHIP, 5/5 fixed), artifact v2 https://claude.ai/artifact/4ucgFCvxmrRcYTbzYehX5F (rebuild: python3 tools/build_site.py, republish same URL). COMPLETE.

## Levels
| Level | Built? | Latest round | Verdict | Bar (reference the critic compares to) | Next action |
|---|---|---|---|---|---|
| 0 Start Here | yes | R3 builder: done | R3: OURS WINS (fixes applied, no R4 critic run yet) | UK Phonics Screening Check, PAST, DIBELS 8, Hasbrouck-Tindal 2017 | optional confirmation critic pass, else DONE |
| 1 First Sounds | ✅ DONE | R2 | OURS WINS vs UFLI (4 residual fixed) | UFLI Foundations lessons 1–34, Jolly Phonics groups 1–7 | wait for builder → critic |
| 2 Sounds Together | ✅ DONE | R3 | OURS WINS vs UFLI (decisive on adult track) | UFLI digraph/blend lessons, Read Write Inc Set 1 | wait for critic |
| 3 Long Vowels | ✅ DONE | R4 | OURS WINS overall (UFLI still slightly richer for kids-only) | UFLI VCe/vowel-team lessons, RWI Set 2/3 | wait → critic |
| 4 Full Code | ✅ DONE | R3 | OURS WINS vs UFLI (L4.12, L4.14, L4.15) | UFLI syllable/affix lessons, Wilson steps 1–6, Sounds-Write polysyllabic | wait → critic |
| 5 Word Power | ✅ DONE | R2 | OURS WINS both (REWARDS + Rasinski FDL) | REWARDS (Archer) multisyllabic, Wilson steps 7–12, Rasinski fluency | wait → critic |
| 6 Reading to Learn | ✅ DONE | R3 | OURS WINS vs CKLA/CKHG (19 long sentences split) | CKLA grade 4–5 unit, IES grades 4–9 guide | wait for critic |
| 7 Advanced | ✅ DONE | R3 | OURS WINS both (SHEG + COR), 0 defects | SHEG Reading Like a Historian + Civic Online Reasoning, CEFR C1 descriptors | wait → critic |

## Known issues / notes
- L2 decodability (tools/decodable.py, first real run): 75–93% per lesson vs the 95% target. Real misses include
  "Then/with" used in L2.02 before th (L2.03), "bank" before nk, "some/come" before heart-word lesson, vowel teams (week, seed, rain),
  r-controlled (for, first, morning). Feed this to the L2 critic/builder.
- L0 R1 biggest gap: ORF passages are far above the grade level of the WCPM norms they're scored against.
- L6 builder flagged facts to verify: biology figures, Mughal dates, Partition figures.
