# Placement Test — Full Instrument

Based on the 5-stage design in `research/07-program-scopes-assessment.md` §5, itself built from
CORE Phonics Survey, the real PAST (Phonological Awareness Screening Test, Kilpatrick,
thepasttest.com), the UK Phonics Screening Check (PSC) official scoring guidance, Really Great
Reading's Diagnostic Decoding Survey, DIBELS/Acadience Oral Reading Fluency, and Hasbrouck-Tindal
(2017) ORF norms. Total time: 15–20 minutes for a full profile, as little as 5 minutes for a
learner who is already a fluent decoder (early exit after Stage 3 or 4). Administer top-down;
**stop each stage-type and place at the first point accuracy drops below 90%** — this is the
placement rule (§7 below), never the point of total failure.

This test works for a 5-year-old or a 50-year-old, native speaker or Urdu/Punjabi/Pashto-first
learner. Nothing in it is child-coded.

**Round 1 gauntlet note (2026-09-28):** this file was rebuilt after a critic round found the
Stage 1 oral-PA ladder didn't match the real PAST's structure, the Stage 3 pseudoword notation
was inconsistent and less rigorous than the real PSC's, the Stage 2 letter-sound grid had a
scoring-denominator bug, and the Stage 4 passages' Flesch-Kincaid difficulty didn't match the
Hasbrouck-Tindal grade norms cited against them. All four were addressed in Round 1.

**Round 2 gauntlet note (2026-09-28):** a fresh critic pass, checking primary sources directly
again rather than trusting the Round 1 fix log, found the Round 1 fixes to Stage 1 and Stage 3
were each real but incomplete: Stage 1's ladder still didn't match PAST's actual section shape
(uneven sizes, interleaved deletion/substitution, a missing vowel-substitution item type, a
3-second cutoff where PAST specifies 2 seconds), and two of Stage 3's new PSC-style rhyme
glosses were themselves factually wrong ("corst"≠"horse," "combrat"≠"rabbit"), with no IPA
column despite that being the PSC's actual primary disambiguator. Both are now fixed below —
Stage 1 is explicitly **PAST-informed, not a PAST clone** (see that section for what that
means), and every Stage 3 rhyme claim was independently re-checked this round. Stage 4 also
gained DIBELS-style administration rules (3-second hesitation/self-correction windows, a
discontinue rule) it previously lacked. See `GAUNTLET.md` for the full defect list and
corresponding fix log for both rounds.

---

## Before you start

- One quiet room, no screen/picture prompts during the test (this measures decoding, not
  guessing from pictures — DESIGN.md rule 1).
- Paper and pencil for the tester (or the learner, for the self-test version).
- A phone with a stopwatch, for Stage 1's automaticity timing and Stage 4's fluency timing.
- Say to the learner: *"I'm going to ask you to do some sound games, then read some letters
  and words, and then read a short passage out loud. Some of the 'words' aren't real words —
  they're made-up. Just tell me the sounds you'd make if you saw them. There's no
  embarrassment here; this just tells us where to start."*

---

## Stage 0 — Intake screen (2 min)

Ask directly, and write down the answers — they change how you interpret everything after:

1. "Can you read any English at all — even a few letters or words?" (No → start Stage 1 as a
   pure oral test, expect to place in Level 1. Yes → continue.)
2. "Were you ever taught to read in a language other than English — for example, Urdu?" (This
   matters because a never-taught native-English child and an adult who is literate in Urdu
   but new to English are different problems — see `research/03` §6 and `urdu-speakers.md`.)
3. "Is English your first language?" (If not, also read `urdu-speakers.md` before finishing
   placement — it does not change the test, but changes what you watch for.)
4. "Did you always find learning any new language difficult, even before English — including,
   if applicable, your first language?" (A "yes" here is one screener flag — see
   `screener.md`. It does not stop the test.)

---

## Stage 1 — Oral phonological awareness (~5 min)

**PAST-informed, not PAST.** This ladder is inspired by the real PAST's (Phonological Awareness
Screening Test, Kilpatrick, Forms A–D, thepasttest.com) overall shape — checked directly against
the real PAST Forms A–D PDF and its Instructions PDF this round — but it is **not a
reproduction** of it. We do not copy PAST's copyrighted items, and we do not copy its exact
section sizes (the real PAST has uneven sections: Basic Syllable 12 items, Onset-Rime 10,
Basic Phoneme 10, Advanced Phoneme 20 — 52 total). This course's ladder is a shorter, original
instrument built for one-time OER placement rather than repeated formal diagnostic use, that
borrows four real, evidence-backed design features from PAST:

1. **No rhyme-judgment section, no pure phoneme-blending section.** Kilpatrick left these out
   deliberately — they hit a ceiling early and stop discriminating struggling readers past
   early kindergarten, which matters for this course's older-child/teen/adult audience.
2. **Deletion and substitution items interleaved within the same level**, not sorted into two
   separate sequential difficulty tiers — matching how the real PAST alternates them from
   Onset-Rime level onward.
3. **A vowel-substitution item type** at the hardest level (the real PAST's Level J), not just
   consonant substitution.
4. **Two independent scored outputs — Highest Correct Level and Highest Automatic Level** —
   not one collapsed into a soft flag of the other.

**Score every item on two axes:**
- **Correct** (✓/✗)
- **Automatic** — the learner responds **before you finish a silent 2-second count** ("one
  thousand one" — respond before "one thousand two" = automatic), matching the real PAST
  Instructions' exact cutoff (not the ~3 seconds a Round 1 draft of this file wrongly used —
  that number describes where *non-automatic* responses typically fall, not the cutoff itself).
  A slow-but-correct answer scores Correct but not Automatic — this matters because slow,
  effortful phonological processing is itself a signal, separate from accuracy (`research/03`
  §1 item 10 on adult dyslexia signs: "slow/effortful reading").

No print at all in this stage. Say each item aloud; the learner answers aloud.

### Level 1 — Syllable-level compound-word deletion (easiest)

Say: "Say [word]. Now say it again, but leave out [part]."

| # | Item | Answer |
|---|---|---|
| 1 | Say "cowboy." Now say it without "boy." | cow |
| 2 | Say "baseball." Now say it without "base." | ball |
| 3 | Say "sunlight." Now say it without "light." | sun |
| 4 | Say "toothbrush." Now say it without "tooth." | brush |
| 5 | Say "backpack." Now say it without "pack." | back |
| 6 | Say "rainbow." Now say it without "rain." | bow |
| 7 | Say "birthday." Now say it without "day." | birth |
| 8 | Say "notebook." Now say it without "book." | note |

### Level 2 — Onset-rime, deletion and substitution interleaved

Say: "Say [word]. Now say it without [sound]." or "Say [word]. Now say it again, but change
[sound] to [sound]." Items alternate type (D = deletion, S = substitution) as the real PAST
does from this level onward — do not sort them into separate blocks.

| # | Type | Item | Answer |
|---|---|---|---|
| 1 | D | Say "sun." Now say it without /s/. | un |
| 2 | S | Say "cat." Now say it again, but change /k/ to /r/. | rat |
| 3 | D | Say "big." Now say it without /b/. | ig |
| 4 | S | Say "hop." Now say it again, but change /h/ to /t/. | top |
| 5 | D | Say "map." Now say it without /m/. | ap |
| 6 | S | Say "run." Now say it again, but change /r/ to /f/. | fun |
| 7 | D | Say "pin." Now say it without /p/. | in |
| 8 | S | Say "sit." Now say it again, but change /s/ to /f/. | fit |

### Level 3 — Basic phoneme, deletion and substitution interleaved (initial/final position)

| # | Type | Item | Answer |
|---|---|---|---|
| 1 | D (initial) | Say "stop." Now say it without /s/. | top |
| 2 | S (initial) | Say "mop." Now say it again, but change /m/ to /t/. | top |
| 3 | D (final) | Say "hand." Now say it without /d/. | han |
| 4 | S (final) | Say "cat." Now say it again, but change the last sound to /p/. | cap |
| 5 | D (initial) | Say "smile." Now say it without /s/. | mile |
| 6 | S (final) | Say "bag." Now say it again, but change the last sound to /t/. | bat |
| 7 | D (cluster) | Say "trap." Now say it without /r/. | tap |
| 8 | S (initial) | Say "led." Now say it again, but change the first sound to /r/. | red |

### Level 4 — Advanced phoneme: deletion, consonant substitution, and vowel substitution interleaved (hardest)

This is where PAST's Level J (vowel substitution) sits — the hardest oral-PA skill, and the
item type Round 1's version was missing entirely.

| # | Type | Item | Answer |
|---|---|---|---|
| 1 | D (medial cluster) | Say "brand." Now say it without /r/. | band |
| 2 | **V** (vowel) | Say "bit." Now say it again, but change the middle sound to /a/. | bat |
| 3 | S (final consonant) | Say "top." Now say it again, but change the last sound to /n/. | ton |
| 4 | **V** (vowel) | Say "hop." Now say it again, but change the middle sound to /i/. | hip |
| 5 | D (medial cluster) | Say "plant." Now say it without the /n/ right before the final /t/. | plat |
| 6 | S (initial consonant) | Say "sit." Now say it again, but change the first sound to /h/. | hit |
| 7 | **V** (vowel) | Say "ten." Now say it again, but change the middle sound to /i/. | tin |
| 8 | S (final consonant) | Say "web." Now say it again, but change the last sound to /t/. | wet |

### Scoring and stopping rule

Score each level out of 8 for **Correct**, and separately out of 8 for **Automatic** (2-second
cutoff). Record **two independent results**: the **Highest Correct Level** reached (≥6/8
Correct) and the **Highest Automatic Level** reached (≥6/8 Automatic) — these can differ, and
both matter (a learner can be accurate at a level without being automatic there yet). Stop
administering further levels once a level scores below 6/8 Correct.

- Below 6/8 Correct on Level 1 (syllable deletion) → the learner needs oral sound-play work
  before anything else; start at Level 1.1's oral on-ramp and re-check weekly.
- Below 6/8 Correct on Level 2 or 3, Level 1 passed → oral PA work should run alongside early
  Level 1 lessons, not block them entirely, since some phoneme awareness typically develops
  through letter-sound instruction itself.
- Below 6/8 Correct on Level 4 only, Levels 1–3 passed → proceed straight to Stage 2; Level 4
  (including vowel substitution) is the hardest oral-PA skill and its absence alone does not
  block print-based placement.
- **Highest Automatic Level lower than Highest Correct Level** → not a placement blocker on its
  own, but a real, trackable signal (matching PAST's own two-output design): place the learner
  using the Correct level as normal, and schedule extra automaticity drill (quick daily
  repetition of that level's item type) alongside their regular lessons. Also log it on
  `screener.md` if the gap is large (2+ levels) or paired with other flags.

---

## Stage 2 — Letter-sound knowledge (~3 min)

**Restructured into three separately-scored blocks** so the placement rule's "single letters
alone" check is actually computable (Round 1 critic defect #1 — the previous single interleaved
table made this impossible). Show each letter/letter-pair on a plain card, no pictures. Ask:
"What sound does this make?" (not the letter name). Mark ✓/✗.

### Block A — Single letters + qu (26 items, matches the Level 1 letter set in `DESIGN.md` §3 exactly)

| Letter | Target sound | Letter | Target sound | Letter | Target sound |
|---|---|---|---|---|---|
| s | /s/ | i | /i/ | b | /b/ |
| a | /a/ | n | /n/ | f | /f/ |
| t | /t/ | m | /m/ | l | /l/ |
| p | /p/ | d | /d/ | j | /j/ |
| g | /g/ | o | /o/ | v | /v/ |
| c | /k/ | k | /k/ | w | /w/ |
| e | /e/ | u | /u/ | x | /ks/ |
| r | /r/ | h | /h/ | y | /y/ (consonant) |
| z | /z/ | qu | /kw/ | | |

**Score /26. This is the "single letters alone" subscore the placement rule uses.** Below 90%
(24/26) → placement is at or before Level 1, specifically at the first letter in the DESIGN.md
1.2–1.12 sequence that was missed.

### Block B — Level 2 digraphs (5 items, administer only if Block A ≥90%)

| Letters | Target sound |
|---|---|
| sh | /sh/ |
| ch | /ch/ |
| th | /th/ (either voiced or unvoiced accepted) |
| wh | /w/ (or /hw/) |
| ng | /ng/ |

**Score /5.** Below 90% (5/5, i.e. any miss) → placement is Level 2, at the first missed
digraph's lesson (2.1–2.5 in DESIGN.md).

### Block C — Level 3/4 vowel teams + r-controlled (7 items, administer only if Block B passes)

| Letters | Target sound |
|---|---|
| ai | /ay/ |
| ee | /ee/ |
| igh | /ie/ |
| oa | /oh/ |
| ar | /ar/ |
| or | /or/ |
| ow | /ow/ (as in "cow") or /oh/ (as in "snow") — either |

**Score /7.** Below 90% (7/7, i.e. any miss) → placement is Level 3 or 4 depending on which
grapheme was missed (ai/ee/igh/oa/ar/or → Level 3, taught at 3.08–3.11; ow → Level 4, taught
at 4.6 — since the Round 1 gauntlet fix moved `ar` and `or/ore` into Level 3 at 3.08–3.09,
see DESIGN.md §3) — continue to Stage 3 to pinpoint exactly where regardless.

---

## Stage 3 — Decoding ladder (~7 min)

The core of placement. Each tier has 8 real words + 8 pseudowords ("made-up words" — tell the
learner this explicitly and call them that, not "nonsense," which can feel mocking to an
adult). **Pseudowords matter as much as real words** — they are what tells you whether the
learner is actually decoding or has memorized some real words by sight without being able to
sound out a word they've never seen (research/07 §5 — this is the single most load-bearing
design choice in the whole test).

**Pronunciation notation, matching the real UK Phonics Screening Check (PSC) convention.** For
every pseudoword, this course gives: (a) an **IPA transcription** — the PSC's actual primary
disambiguator, present for every single item in its official scoring guidance — (b) a real word
it **rhymes with**, where a clean one-syllable rhyme partner exists (matching the PSC's
supplementary "rhymes with" language), and (c) the real word each target grapheme's sound is
**drawn from**. Where no clean rhyme partner exists, this course instead names the real words
each sound-fragment is drawn from, following the PSC's own fallback phrasing ("this item
combines the X from... with the Y from...") rather than forcing a strained rhyme claim. **Every
rhyme claim below has been independently re-checked this round** (CMU Pronouncing
Dictionary-style phoneme comparison) after a Round 2 critic found two of them factually wrong
("corst"≠"horse," "combrat"≠"rabbit" — both now fixed, see `GAUNTLET.md`). As with the PSC,
**all reasonable regional pronunciations of the target sound should be accepted** — this is not
a test of accent. IPA is given in a neutral broad transcription; where a vowel varies by
region (e.g. /ɒ/ in British "hot"-type words vs. /ɑ/ in most American varieties), either
pronunciation should be accepted.

Say: "Read this word. If it's not a real word, just tell me the sounds it would make."

### Tier 1 — matches Level 1 (CVC, single letters only)

**Real words:** cat, sun, big, hop, red, mud, sit, fan.

**Pseudowords:**

| # | Pseudoword | IPA | Rhymes with | Grapheme sound drawn from |
|---|---|---|---|---|
| 1 | dif | /dɪf/ | if | the /d/ in "dog" |
| 2 | gep | /gɛp/ | pep | the /g/ in "go" |
| 3 | lom | /lɒm/ (/lɑm/ US) | mom | the /l/ in "leg" |
| 4 | pob | /pɒb/ (/pɑb/ US) | job | the /p/ in "pig" |
| 5 | hig | /hɪg/ | big | the /h/ in "hat" |
| 6 | vun | /vʌn/ | sun | the /v/ in "van" |
| 7 | nof | /nɒf/ (/nɑf/ US) | off | the /n/ in "net" |
| 8 | zad | /zæd/ | sad | the /z/ in "zoo" |

*(Item 2 replaces "gan" — a Round 3 sweep finding: "gan" is a real dialectal/archaic English
word (Northern English dialect for "go"; archaic past tense of "gin"), listed on Wiktionary.
Replaced with "gep," which is not a real word. Item 4 replaces Round 1's "rob," which was
itself a real English word and so invalid as a pseudoword — a Round 2 fix. Item 7 replaces
Round 2's "nob" — a further Round 3 sweep finding: "nob" is a genuine, dictionary-listed
informal word (British/Irish slang for a wealthy person, or slang for "head"), the identical
defect class as "rob," "gan," and "shute." Replaced with "nof," which is not a real word. This
tier alone had three of these across three rounds — a pattern worth naming plainly in the
Round 3 builder log below rather than treating each as an isolated slip.)*

### Tier 2 — matches Level 2 (digraphs, blends, endings)

**Real words:** shop, chip, thin, whiz, sting, blast, crisp, stamp.

**Pseudowords:**

| # | Pseudoword | IPA | Rhymes with | Grapheme sound drawn from |
|---|---|---|---|---|
| 1 | shig | /ʃɪg/ | big | the /sh/ in "shop" |
| 2 | chob | /tʃɒb/ (/tʃɑb/ US) | job | the /ch/ in "chip" |
| 3 | thap | /θæp/ | cap | the /th/ in "thin" (unvoiced) |
| 4 | whef | /wɛf/ (or /hwɛf/) | deaf | the /w/ (or /hw/) in "whiz" |
| 5 | strin | /strɪn/ | pin | the /str/ blend in "string" |
| 6 | brof | /brɒf/ (/brɑf/ US) | off | the /br/ blend in "brand" |
| 7 | clant | /klænt/ | pant | the /cl/ blend in "clap" |
| 8 | stemp | /stɛmp/ | hemp | the /st/ blend in "stamp" |

### Tier 3 — matches Level 3 (VCe, open syllables, y as vowel, ar, or/ore, vowel teams)

**Real words:** cake, time, rain, tree, car, fork, night, happy.

**Pseudowords:**

| # | Pseudoword | IPA | Rhymes with | Grapheme sound drawn from |
|---|---|---|---|---|
| 1 | vope | /voʊp/ | hope | the o_e in "hope" |
| 2 | flarp | /flɑrp/ | sharp | the "ar" in "car" |
| 3 | prane | /preɪn/ | rain | the "ai" in "rain" |
| 4 | gorn | /gɔrn/ | corn | the "or" in "fork" |
| 5 | doak | /doʊk/ | soak | the "oa" in "boat" |
| 6 | drute | /druːt/ | root | the u_e in "flute" |
| 7 | spight | /spaɪt/ | night | the "igh" in "night" |
| 8 | bratny | /brætni/ | (final syllable rhymes with) "happy" | the final "y" (/i/) in "happy" |

*(Round 3 fix: item 6 was "shute" — a real, dictionary-listed variant spelling of "chute,"
invalid as a pseudoword by the same rule that caught Tier 1's "rob" in Round 2. Replaced with
"drute," which is not a real word, rhymes cleanly with "root" with no onset/rime ambiguity, and
uses "flute" — not "cute" — as its sound source specifically because "flute" has no /j/ glide
to argue about, unlike "cute"'s /kj-/ onset.)*

*(Consistency fix, after Level 3 moved ar/or/ore to 3.08–3.09: car/fork and flarp/gorn moved here from Tier 4, keeping the Round 2–3 verified items. Each pattern is still tested once: i_e by "time", ee by "tree", oa by "doak", u_e by "drute".)*

### Tier 4 — matches Level 4 (er/ir/ur, diphthongs, aw/au, consonant-le, syllable division)

**Real words:** germ, burn, point, shout, crawl, haul, table, picnic.

**Pseudowords:**

| # | Pseudoword | IPA | Rhymes with | Grapheme sound drawn from |
|---|---|---|---|---|
| 1 | blaud | /blɔd/ | fraud | the "au" in "haul" |
| 2 | hable | /ˈheɪ.bəl/ | table | the consonant-le in "table" |
| 3 | thirn | /θɝn/ | fern | the "ir" in "bird" |
| 4 | vurk | /vɝk/ | work | the "ur" in "burn" |
| 5 | spoin | /spɔɪn/ | coin | the "oi" in "point" |
| 6 | plout | /plaʊt/ | shout | the "ou" in "shout" |
| 7 | prawl | /prɔl/ | crawl | the "aw" in "crawl" |
| 8 | combrat | /kɒmbræt/ (/kɑmbræt/ US) | (final syllable rhymes with) "chat" | closed-syllable division as in "picnic" |

*(Consistency fix: ar/or items moved to Tier 3. Replaced with blaud and hable, both checked absent from /usr/share/dict/words and aspell. Round 2 fixes: item 2 was "corst," glossed as rhyming with "horse" — /kɔrst/ and /hɔrs/ do
not rhyme, mismatched coda. Replaced with "gorn," which genuinely rhymes with "corn." Item 8's
"combrat" was glossed as rhyming with "-bit" as in "rabbit" — /bræt/ and /bɪt/ do not rhyme,
different vowel. Its rhyme claim is now "chat," which is the real, checked rhyme for its
second syllable. Round 3 fix: item 6 was "glout" — a real, if obsolete, English word (Wiktionary:
Scots-derived, "to sulk, to stare sullenly"), the same defect class as "rob"/"gan"/"nob"/"shute."
Replaced with "plout," which is not a real word.)*

### Tier 5 — matches Level 5 (prefixes/suffixes, multisyllable morphology)

**Real words:** unhappy, redo, dislike, prewash, misplace, nonstop, inactive, submarine.

**Pseudowords:**

| # | Pseudoword | IPA | Rhymes with (final syllable) | Affix/root drawn from |
|---|---|---|---|---|
| 1 | unblick | /ʌnblɪk/ | trick | the prefix "un-" in "unhappy" |
| 2 | refarm | /riːfɑrm/ | farm (final syllable is literally "-farm") | the prefix "re-" in "redo" |
| 3 | distrunk | /dɪstrʌŋk/ | trunk | the prefix "dis-" in "dislike" |
| 4 | prevorn | /priːvɔrn/ | born | the prefix "pre-" in "prewash" |
| 5 | mislact | /mɪslækt/ | fact | the prefix "mis-" in "misplace" |
| 6 | nonfrent | /nɒnfrɛnt/ | rent | the prefix "non-" in "nonstop" |
| 7 | inflemt | /ɪnflɛmt/ | tempt (final syllable "-lemt"/-lɛmt/ rhymes with "-empt"/-ɛmt/) | the negation prefix "in-" in "inactive" |
| 8 | subvantic | /sʌbvæntɪk/ | frantic (both end "-antic"/-æntɪk/) | the prefix "sub-" in "submarine" |

*(Round 3 fix: item 7 was "intergop," which tested the unrelated prefix "inter-" (between/among,
as in "international") while being paired against the real word "inactive," whose prefix is
negation "in-" — a different morpheme that happens to share three letters. Replaced with
"inflemt," which genuinely tests "in-" + a nonsense root, matching what "inactive" actually
requires a learner to decode.)*

### Answer key / scoring

Score each tier out of 16 (8 real + 8 pseudo). **Enter the learner at the lowest tier where
they scored below 90% (≈14/16), even if a higher tier was passed** — never skip past a gap
(research/07 §5's explicit false-placement warning). If Tier 1 itself is below 90%, place at
Level 1 lesson 1.2 (after confirming Stage 1 oral PA is solid). If all 5 tiers clear 90%,
continue to Stage 4.

---

## Stage 4 — Oral reading fluency (timed, 1 min per passage, only if Tier 3+ cleared)

**Rewritten this round so passage difficulty actually matches the grade norms cited against it**
(Round 1 critic's "Single Biggest Gap" and defect #2). Each passage below was measured with the
Flesch-Kincaid Grade Level formula (`textstat` library) and targets roughly Grade 2, Grade 4,
and Grade 6 text difficulty respectively — the same grade bands the Hasbrouck-Tindal (2017) WCPM
norms below are drawn from. All three passages remain adult-respectful, age-neutral content
(no child-picture-book register) — see the note at the end of this section on that deliberate
trade-off.

### Real Hasbrouck-Tindal (2017) norms used (50th percentile WCPM, fetched this round from the
official Read Naturally-hosted table of the technical report, ERIC ED594994):

| Grade | Fall 50th | Winter 50th | Spring 50th |
|---|---|---|---|
| 2 | 50 | 84 | 100 |
| 4 | 94 | 120 | 133 |
| 6 | 132 | 145 | 146 |

Because this course is self-paced and not tied to a school calendar, **Fall 50th percentile is
used as the pass threshold below** — the most conservative (lowest) point in each grade's own
norm range, representing "has reached the *start* of that grade's typical fluency," not its
end-of-year mastery level. Winter/Spring values are given for context if you want a stricter
bar.

**A note on what this single-cut design is, and isn't:** this is a deliberately simpler design
than DIBELS 8's own four-tier risk classification (red/yellow/green/blue, each empirically
validated for sensitivity/specificity against later outcomes). This course uses one borrowed
percentile cut per grade instead — honestly cited against the real 2017 Hasbrouck-Tindal table
above, but **not independently validated as a risk classification in its own right**. That
trade-off is appropriate here because this is a one-time OER placement instrument, not a
repeated formal MTSS screening tool the way DIBELS is — but don't treat the WCPM gate below as
carrying DIBELS' own validated predictive weight.

**Administration rules (adopted from the real DIBELS 8th Edition Administration and Scoring
Guide, dibels.uoregon.edu, fetched and checked this round), because this course is often run by
untrained parents/tutors who need an exact rule, not a judgment call):**

- Administer the **lowest** passage first. Time exactly 1 minute.
- **3-second hesitation rule:** if the learner hesitates on a word for **3 full seconds**
  without attempting it, tell them the word, mark it as an error, and have them continue.
  Don't let "long hesitation" be a subjective judgment call — count an exact 3 seconds
  (silently count "one-Mississippi, two-Mississippi, three-Mississippi").
- **Self-correction rule:** if the learner misreads a word but corrects themselves **within 3
  seconds**, it counts as **correct**, not an error — this rewards genuine self-monitoring
  rather than penalizing it.
- **Error count:** a skipped word, a substituted wrong word, or a word that hit the 3-second
  hesitation rule above all count as one error each.
- **Discontinue rule:** if the learner gets **zero words correct in the entire first line** of
  a passage, stop the passage immediately, record a score of 0 for that passage, and do not
  move up to the next passage — this indicates the passage (and likely the whole Stage 4) is
  above the learner's current level; return to Stage 3's placement instead.
- If the passage is finished before 60 seconds, note the time and continue reading normally,
  then move to the next passage up.

### Passage A — FK grade ≈ 1.7 (targets the Grade 2 norm band), 95 words

> Rana works at a small shop by the market road. She opens the shop early, at eight each
> morning. She sells rice, tea, soap, and sugar to her neighbors. A man came in one day to
> buy some rice. He also wanted tea and a bar of soap. The shop had run out of soap that
> morning. Rana wrote his name down on a small list. She told him more soap would arrive next
> week. The man thanked her kindly and picked up his bag. Then he walked home slowly with his
> rice and tea.

**WCPM benchmark:** ≥50 WCPM (Grade 2 Fall 50th percentile) with few errors to move to Passage
B; below that, place fluency work at Level 3–4 alongside the learner's Stage 3 tier placement.

**Comprehension check (Passage A):**
1. (literal) Where does Rana work? — *At a small shop by the market road.*
2. (literal) What time does she open the shop? — *Eight each morning.*
3. (literal) What did the man want to buy? — *Rice, tea, and a bar of soap.*
4. (inferential) The man thanked Rana kindly even though the shop didn't have everything he
   wanted. What does this suggest about how Rana handled the situation? — *That she handled the
   shortage well — by writing his name down and promising more soap next week — so he still
   felt well-treated even though he didn't get everything he came for.* (This requires
   connecting his reaction at the end to her actions earlier in the passage, not just linking
   two adjacent sentences.)
5. (vocabulary) What does "arrive" mean in this passage? — *To come, or to get to a place.*

### Passage B — FK grade ≈ 4.7 (targets the Grade 4 norm band), 101 words

> Many families spend more money on power bills in the summer months. Fans and coolers have to
> run for many more hours each day. Food also spoils faster in the heat of the season. So
> people shop more often, buying smaller amounts each time. A shopkeeper in Multan said his cold
> drink sales grow every summer. His hot tea sales barely change during those same months. He
> now keeps extra bottled water and ice on hand at all times. Customers often ask for these two
> items early in the morning. They want them before the day grows too hot to bear.

**WCPM benchmark:** ≥94 WCPM (Grade 4 Fall 50th percentile) with few errors to move to Passage
C; below that, place fluency work at Level 5's fluency strand.

**Comprehension check (Passage B):**
1. (literal) Why do families spend more on power bills in summer? — *Fans and coolers run for
   more hours.*
2. (literal) What happens to the shopkeeper's cold drink sales in summer? — *They grow every
   summer.*
3. (literal) What two items does he keep extra stock of? — *Bottled water and ice.*
4. (inferential) The shopkeeper's hot tea sales "barely change" in summer while his cold drink
   sales grow. What does this suggest about what people want to drink when it's hot? — *That
   people switch toward cold drinks and away from hot tea specifically because of the heat —
   this is a pattern you infer from the contrast in his sales, not a sentence stated directly in
   the passage.*
5. (vocabulary) What does "spoils" mean in this passage? — *Goes bad; becomes unfit to eat.*

### Passage C — FK grade ≈ 6.8 (targets the Grade 6 norm band), 119 words

> A small town recently held a meeting about raising bus fares. Bus riders said fares were
> already too high for working families. Town leaders said the extra money was needed to buy
> new buses. They also wanted funds to fix roads that had fallen into disrepair. Some riders
> suggested a lower fare just for students and older riders. Others worried a fare hike would
> push people back toward using their own cars. More cars on the road could mean more traffic
> and more pollution downtown. The town leaders agreed to study both ideas before making a
> final choice. They promised to hold a second meeting once they gathered more information from
> nearby towns that had faced the same problem.

**WCPM benchmark:** ≥132 WCPM (Grade 6 Fall 50th percentile) with good accuracy and phrasing
indicates readiness for Level 6 material; below that, the learner's decoding has outpaced
fluency and Level 5's fluency strand is the right entry point even if Stage 3 tiers all passed.

**Comprehension check (Passage C):**
1. (literal) Why did the town hold a meeting? — *To discuss/debate raising bus fares.*
2. (literal) What two things did town leaders say the extra money was needed for? — *New buses
   and fixing roads.*
3. (literal) What alternative did some riders suggest instead of raising fares for everyone? —
   *A lower fare just for students and older riders.*
4. (inferential) Why were some people concerned that a fare increase would lead to "more traffic
   and more pollution downtown"? — *Because a higher fare might push some bus riders to start
   driving their own cars instead, putting more cars on the road — this connects the
   fare-hike-pushes-people-to-cars idea with the traffic/pollution sentence that follows it,
   rather than restating either sentence alone.*
5. (vocabulary) What does "disrepair" mean in this passage? — *In poor or damaged condition,
   needing repair.*

**On the lack of a Track A/Track B split at this stage:** unlike every Level 1–7 lesson, these
three passages are uniformly adult/civic-register content (a shop, household budgeting, town
governance) with no child-content parallel version. This is a deliberate trade-off, not an
oversight: it keeps one universal fluency instrument comparable across every learner rather than
needing two separately-normed passage sets. The cost, named plainly: a child reaching Stage 4
is tested on some unfamiliar civic/economic vocabulary ("council," "disrepair," "fares") that
could depress a fluency or comprehension score for reasons related to
background knowledge, not decoding skill. If a child scores low here specifically on the
comprehension questions while decoding the words accurately, treat that as a
background-knowledge gap to address directly (a quick two-sentence context-setting before the
passage, or moving that specific child to a Level 5/6 knowledge-building unit) rather than as a
comprehension-skill deficit.

---

## Stage 5 — this course adds no separate Stage 5

Note: `research/07` §5 describes an optional Stage 5 "brief comprehension check." In this
course, the comprehension check is built directly into each Stage 4 passage above (3 literal +
1 inferential + 1 vocabulary question per passage) rather than run as a separate stage, so
fluency and comprehension are scored together and a "decodes fluently but doesn't comprehend"
profile is caught at the same passage that revealed the fluency level.

---

## Scoring sheet

```
Learner name/ID: _______________   Date: _______________   Tester: _______________

Stage 0 — Intake
  Can read any English?          Y / N
  Prior reading instruction in another script?  Y / N   Which: _______
  English first language?        Y / N
  Language-learning difficulty history?  Y / N  (flag for screener.md if Y)

Stage 1 — Oral PA (PAST-informed, 2-sec automaticity cutoff)   Correct /8   Automatic /8
  Level 1 — syllable deletion                     ____          ____
  Level 2 — onset-rime, del+sub interleaved       ____          ____
  Level 3 — basic phoneme, del+sub interleaved    ____          ____
  Level 4 — advanced: del+sub+VOWEL sub interleaved ____        ____
  → Stop administering further levels once a level scores <6/8 Correct.
  Highest Correct Level reached:    ____  (≥6/8 Correct)
  Highest Automatic Level reached:  ____  (≥6/8 Automatic — may be lower than Correct)
  → If Automatic level < Correct level: not a placement blocker, but schedule automaticity
    drill and flag on screener.md if the gap is 2+ levels.

Stage 2 — Letter-sound (3 blocks)
  Block A — single letters + qu   Score /26     ≥90% (24+)?  Y / N
  Block B — L2 digraphs           Score /5      ≥90% (5/5)?  Y / N
  Block C — L3/4 vowel teams/r    Score /7      ≥90% (7/7)?  Y / N
  → "Single letters alone" placement check = Block A score only.

Stage 3 — Decoding ladder   Score /16 each tier   ≥90% (14+)?
  Tier 1 (L1 CVC)          ____   Y / N
  Tier 2 (L2 digraph/blend)____   Y / N
  Tier 3 (L3 VCe/vowel team)____  Y / N
  Tier 4 (L4 full code)______ Y / N
  Tier 5 (L5 morphology)   ____   Y / N
  → Placement tier = FIRST tier scoring below 90%.

Stage 4 — ORF (only if Tier 3+ passed)   [FK grade / Hasbrouck-Tindal Fall-50th benchmark]
  Passage A (FK≈1.7 / ≥50 WCPM):  WCPM ____  Errors ____  Comprehension ___/5
  Passage B (FK≈4.7 / ≥94 WCPM):  WCPM ____  Errors ____  Comprehension ___/5
  Passage C (FK≈6.8 / ≥132 WCPM): WCPM ____  Errors ____  Comprehension ___/5

PLACEMENT DECISION: Level ____  Lesson ____
Reasoning: _______________________________________________
```

---

## Placement rule (final)

**Place the learner at the first checkpoint — oral PA level (using Highest Correct Level), letter-
sound block, or decoding tier — where accuracy drops below 90% (below 6/8 Correct for Stage 1's
levels).** Never place at the point of total failure (too far back — wastes the learner's time
on what they already know), and never skip past a gap even if a later, harder skill was passed
(a common false-placement error — research/07 §5). Concretely:

- Stage 1 Level 1 (syllable deletion) <6/8 Correct → Level 1.1 (oral on-ramp), regardless of
  anything else.
- Stage 1 Level 2 or 3 <6/8 Correct, Level 1 passed → start Level 1.1 with extra oral-PA
  practice threaded through, rather than a hard block.
- Stage 1 Level 4 <6/8 Correct only, Levels 1–3 passed → proceed to Stage 2 as normal.
- Whenever Highest Automatic Level is lower than Highest Correct Level → placement itself still
  follows Highest Correct Level; add an automaticity drill for the gapped level(s) alongside
  whatever lesson the learner is placed into.
- Stage 2 Block A (single letters) <90% → Level 1, at the first letter lesson covering an
  unknown letter (see the Level 1 sequence in `DESIGN.md` §3).
- Stage 2 Block A passes but Block B (digraphs) fails → Level 2, at the first failed digraph's
  lesson.
- Stage 2 Blocks A–B pass but Block C fails → Level 3 or 4 depending on which grapheme missed.
- Stage 3 Tier 1 <90% → Level 1 (specific lesson = first CVC pattern not yet automatic).
- Stage 3 Tier 2 <90% (Tier 1 passed) → Level 2, first lesson covering the missed
  digraph/blend pattern.
- Stage 3 Tier 3 <90% (Tiers 1–2 passed) → Level 3, first lesson covering the missed pattern.
- Stage 3 Tier 4 <90% (Tiers 1–3 passed) → Level 4, first lesson covering the missed pattern.
- Stage 3 Tier 5 <90% (Tiers 1–4 passed) → Level 5, word-power strand start.
- All 5 tiers ≥90% but Stage 4 WCPM below the passage's benchmark → Level 5 fluency strand,
  even though decoding is solid — fluency and decoding are tracked and placed separately
  (DESIGN.md rule 8).
- All 5 tiers pass and Passage C clears ≥132 WCPM with good comprehension → Level 6 entry;
  administer Level 6/7 diagnostic (see that level's README) to place further.

---

## Self-test version (for an adult working alone)

1. Read Stage 0 to yourself and answer honestly.
2. **Stage 1 (oral PA) genuinely cannot be done alone.** Every item is a stimulus-response task
   where the tester says something aloud and the learner answers purely by ear, without seeing
   the item in print — that's the entire point of the oral-only design (no letters, no cueing
   from spelling). If you are both the item-writer and the only respondent, you cannot avoid
   having already seen the print stimulus, which defeats the test. **You need a second person
   for this stage** — a friend, family member, or anyone willing to read the "Item" column aloud
   to you in an order you haven't memorized. If truly nobody is available, skip straight to
   Stage 2 and treat Stage 1 as "not administered" rather than trying to fake a solo version of
   it — a missing data point is honest; a self-defeating substitute isn't.
3. For Stage 2 and Stage 3, write the letters/words on separate cards or a sheet, cover the
   answer column, read each one aloud into your phone's voice recorder, then play it back next
   to the answer key and mark each ✓/✗ yourself. Be honest — this only helps you if it's
   accurate; there's no one to perform for.
4. For Stage 4, use your phone's stopwatch, record your 1-minute reading, then count errors
   from the recording afterward (easier than trying to count while reading).
5. Use the same scoring sheet and placement rule above.

If a second person is available and you score below 6/8 Correct on Stage 1's Level 1 or 2
alone, start at Level 1.1 — that's an oral, no-print starting point, and it's common even for
adults who read some English already but were never taught the underlying sound system
explicitly.
