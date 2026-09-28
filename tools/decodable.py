#!/usr/bin/env python3
"""Decodability check for L1–L4 lessons: every word in the "Read it" section must parse
into graphemes taught so far (DESIGN.md §3 master sequence) or be a taught heart word.

usage: python3 tools/decodable.py course/level-1/lessons/L1.05-*.md   (or a level dir)
# ponytail: greedy longest-grapheme parse, ignores which *sound* a grapheme makes
# (e.g. "has" passes on s). Good enough to catch untaught spellings; a human still checks sounds.
"""
import re, sys, pathlib

# cumulative graphemes introduced per lesson; "a_e" style = split digraph (VCe)
SEQ = {
 "1.02": "s a t", "1.03": "p i n", "1.04": "m d", "1.05": "g o", "1.06": "c k ck",
 "1.07": "e u", "1.08": "r h", "1.09": "b f l", "1.10": "ff ll ss zz", "1.11": "j v w",
 "1.12": "x y z qu",
 "2.01": "sh", "2.02": "ch tch", "2.03": "th", "2.04": "wh", "2.05": "ng nk",
 "2.10": "ed", "2.11": "ing er",
 "3.01": "a_e", "3.02": "i_e", "3.03": "o_e u_e e_e", "3.07": "ce ge dge",
 "3.08": "ar", "3.09": "or ore",
 "3.10": "ai ay", "3.11": "ee ea", "3.12": "oa ow oe", "3.13": "igh ie", "3.14": "ue ew ui",
 "3.15": "oo", "4.03": "er ir ur", "4.04": "air are ear eer",
 "4.05": "oi oy", "4.06": "ou", "4.07": "aw au al", "4.08": "kn wr gn mb",
 "4.09": "ph gh", "4.10": "le", "4.11": "tion sion ture ous cial tial",
}
HEART = {  # mirrors DESIGN.md §3 CANONICAL heart-word schedule
 "1.02": "a I", "1.03": "the is", "1.04": "to of", "1.05": "and was", "1.06": "said you",
 "1.07": "are he", "1.08": "she we", "1.09": "me be", "1.10": "do what", "1.11": "they one",
 "1.12": "have go", "1.13": "no so",
 "2.01": "says for", "2.02": "there where", "2.03": "were from", "2.04": "come some",
 "2.05": "done want", "2.06": "put push", "2.07": "pull full", "2.08": "who could",
 "2.09": "would should", "2.10": "your four", "2.11": "many any her", "2.12": "does goes two",
 "2.13": "again friend because",
 "3.01": "once only", "3.02": "very every", "3.03": "great eye", "3.04": "busy people",
 "3.05": "water laugh", "3.06": "walk talk", "3.07": "buy answer", "3.08": "whole earth",
}

def known(lesson):
    g, h = set(), set()
    for k, v in SEQ.items():
        if k <= lesson: g |= set(v.split())
    for k, v in HEART.items():
        if k <= lesson: h |= {w.lower() for w in v.split()}
    if lesson >= "2.06": g |= set()  # blends are just letters
    if lesson >= "3.05": g.add("OPEN")   # open syllables: single vowel = long, ok
    if lesson >= "3.06": g.add("y"); g.add("YVOWEL")
    return g, h

def heart_ok(word, h):
    """A taught heart word, or that heart word plus a regular taught inflection
    (-s/-es/-ed/-ing), still counts as known (fix: defect worklist #13 — 'walks' was
    flagged even though 'walk' is a canonical L3 heart word and -s is a taught L2 suffix)."""
    w = word.lower()
    if w in h: return True
    for suf in ("ing", "es", "ed", "s"):
        if w.endswith(suf) and w[:-len(suf)] in h:
            return True
    return False

# fix: sorting a *set* by length alone leaves same-length graphemes (e.g. "al" vs "ll", "ay"
# vs "aw") in Python's hash-randomized set-iteration order, which differs between process
# runs (PYTHONHASHSEED is per-process by default) — the exact same word could parse two
# different ways, and therefore pass or fail the decodability gate, on two different
# invocations of the same command. Sorting on (-len, x) makes tie-breaking alphabetical and
# fully deterministic (Round 1 builder fix — this is what caused inconsistent scratch-test
# results for "fall"/"calls" while debugging the al(l) defect above).
ALL = sorted({x for v in SEQ.values() for x in v.split() if len(x) > 1 and "_" not in x},
             key=lambda x: (-len(x), x))

# fix: "ous/tion/sion/ture/cial/tial" are word-final suffix graphemes; without restricting
# them to true word-end position, the greedy parser collides them into unrelated mid-word
# letter runs (e.g. "house"/"mouse" -> h/m + "ous" + e) and produces a false untaught-
# grapheme flag. Same fix applies to "mb" below (positional_ok): every taught mb-word
# (comb, lamb, climb, thumb...) is word-final silent-b, so "mb" is now end-restricted too —
# this correctly stops it from colliding with ordinary cross-syllable m+b runs like
# "member" or "chamber", which just fall back to two known single letters.
END_ONLY = {"ce", "ge", "dge", "ed", "ing", "le", "ous", "tion", "sion", "ture", "cial", "tial"}

def positional_ok(x, w, i):
    # ponytail: suffix-like graphemes only count at word end; al only before l/k/t; gn at edges;
    # mb (silent-b) only at word end, matching every taught example (comb, lamb, climb...)
    end = i + len(x)
    if x in ("ed", "ing") and (i < 3 or not re.search(r"[aeiouy]", w[:i])):
        return False  # "red", "sing", "string" = base word, not a suffix
    if x in END_ONLY: return end == len(w) or (x in ("ed", "ing") and w[end:] in ("s",))
    # fix: a previous version of this line excluded al-before-l on the theory that
    # "wall/ball/call/small/fall/tall" are L1.10 FLOSS short-a + doubled-l, not the L4.07
    # al(l) grapheme. That is a phonics error, not a code style choice: FLOSS doubling
    # (bell, doll, off, buzz) doubles a consonant AFTER a genuinely short vowel; there is no
    # short-a "-all" FLOSS word in English to contrast with — "wall/call/fall/small/tall" are
    # all /aw/, i.e. exactly the untaught-until-4.07 al(l) grapheme the critic flagged as
    # leaking. Restored to the original "lkt" rule (Round 1 builder fix).
    if x == "al": return end < len(w) and w[end] in "lkt"
    if x == "gn": return i == 0 or end == len(w)
    if x == "mb": return end == len(w)
    return True

def graphemes(word):
    """Greedy parse over the FULL code; VCe marked as 'a_e' etc."""
    w, out = word.lower(), []
    m = re.search(r"([aeiou])([bcdfgklmnprstvz])e(s|d)?$", w)
    if m and m.group(3) == "s" and re.search(r"(s|x|z|sh|ch)es$", w):
        m = None  # "buses", "boxes" = base + es, not VCe
    if m and not re.search(r"[aeiou]{2}[bcdfgklmnprstvz]e", w) and len(w) > 3:
        out.append(m.group(1) + "_e"); w = w[:m.start()] + m.group(1) + m.group(2)
    i = 0
    while i < len(w):
        for x in ALL:
            if w.startswith(x, i) and positional_ok(x, w, i):
                out.append(x); i += len(x); break
        else:
            out.append(w[i]); i += 1
    return out

def parses(word, g):
    # y as a vowel (my, by, happy) = L3.06; before that only word-initial consonant y (yes, yell)
    if "YVOWEL" not in g and "y" in word.lower()[1:]:
        return False
    return all(x in g or (len(x) == 1) for x in graphemes(word)) and \
        all(ch in g or not ch.isalpha() for ch in word.lower() if ch not in "".join(x for x in graphemes(word) if len(x) > 1))

def read_section(text):
    # fix: defect worklist #14 — stop at "## Fluency check" too, not just the next "## 8."
    # heading, so the fluency-instructions boilerplate never leaks into the word scan.
    m = re.search(r"#+\s*7\.?[^\n]*\n(.*?)(?=\n#+\s*Fluency check|\n#+\s*8\.?|\Z)", text, re.S)
    return m.group(1) if m else ""

def check(path):
    lesson = re.search(r"L(\d)\.(\d\d)", path.name)
    lvl = re.search(r"level-(\d)", str(path))
    if lesson:
        lid = f"{lesson.group(1)}.{lesson.group(2)}"
        sec = read_section(path.read_text())
    elif path.name == "mastery-check.md" and lvl:
        lid = f"{lvl.group(1)}.99"   # whole level taught; scan every blockquote in the file
        sec = path.read_text()
    else:
        return None
    g, h = known(lid)
    quoted = "\n".join(l[1:] for l in sec.splitlines() if l.startswith(">"))
    sec = quoted or sec  # ponytail: texts in > blockquotes are the reader-facing lines
    # drop question/instruction lines and markdown noise; keep story lines
    words = re.findall(r"[A-Za-z']+", re.sub(r"\*\*.*?\*\*|`.*?`|\(.*?\)", " ", sec))
    bad = sorted({w for w in words if not heart_ok(w, h) and not parses(w, g)})
    ok = sum(1 for w in words if heart_ok(w, h) or parses(w, g))
    pct = 100 * ok / len(words) if words else 0
    return lid, len(words), pct, bad

if __name__ == "__main__":
    assert parses("sat", {"s", "a", "t"}) and not parses("ship", {"s", "i", "p"})
    assert parses("get", set("get")) and parses("sing", set("sing")|{"ng"})
    assert parses("string", set("string")|{"ng"}) and parses("buses", set("buse"))
    assert not parses("my", set("my")) and parses("yes", set("yes")) and parses("my", set("my")|{"YVOWEL"})
    assert not parses("some", set("somebcdt")) and not parses("walk", set("walk")) and not parses("park", set("park"))
    assert parses("ship", {"s", "h", "i", "p", "sh"}) and parses("cake", {"c", "k", "a_e", "a"}) and parses("cakes", {"c","k","a_e","a","s"})
    files = []
    for a in sys.argv[1:]:
        p = pathlib.Path(a)
        files += sorted(p.rglob("L*.md")) + sorted(p.rglob("mastery-check.md")) if p.is_dir() else [p]
    for f in files:
        r = check(f)
        if r:
            lid, n, pct, bad = r
            print(f"{lid}  words={n:4d}  decodable={pct:5.1f}%  untaught={' '.join(bad[:25])}")
