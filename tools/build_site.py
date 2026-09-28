#!/usr/bin/env python3
"""Bundle the whole course (markdown) into one self-contained HTML reader: docs/index.html (GitHub Pages).
usage: python3 tools/build_site.py            → docs/index.html (full HTML document, for GitHub Pages)
       python3 tools/build_site.py --artifact F → F (page body only; claude.ai Artifacts add their own skeleton)
# ponytail: markdown rendered client-side by marked (cdnjs), so the page stays one file.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "index.html"   # served by GitHub Pages

LEVELS = [(0, "Start Here", "Placement"), (1, "First Sounds", "Pre-A1"), (2, "Sounds Together", "A1"),
          (3, "Long Vowels", "A1"), (4, "The Full Code", "A1–A2"), (5, "Word Power & Fluency", "A2–B1"),
          (6, "Reading to Learn", "B1–B2"), (7, "Advanced & Critical", "C1–C2")]

def title_of(p):
    for line in p.read_text().splitlines():
        if line.startswith("# "):
            return re.sub(r"[*_`]", "", line[2:]).strip()
    return p.stem

def doc(p, label=None):
    rel = p.relative_to(ROOT).as_posix()
    return {"id": rel.replace("/", "~"), "path": rel, "title": label or title_of(p), "md": p.read_text()}

groups = [{"name": "Course", "band": "", "docs": [doc(ROOT / "README.md", "About this course")]}]
for n, name, band in LEVELS:
    d = ROOT / "course" / f"level-{n}"
    docs = []
    if n == 0:
        for f in ["start-here", "placement-test", "screener", "guide-tutors-parents", "urdu-speakers"]:
            docs.append(doc(d / f"{f}.md"))
    else:
        docs.append(doc(d / "README.md", "Overview"))
        docs += [doc(p) for p in sorted((d / "lessons").glob("L*.md"))]
        docs += [doc(p) for p in sorted(d.glob("*.md")) if p.name not in ("README.md", "GAUNTLET.md")]
    groups.append({"name": f"Level {n} · {name}", "band": band, "docs": docs})
groups.append({"name": "Evidence", "band": "", "docs": [doc(ROOT / "DESIGN.md", "Design & evidence verdicts")] +
               [doc(p) for p in sorted((ROOT / "research").glob("*.md"))]})

proc = [doc(ROOT / "process" / "LOG.md", "Build timeline"), doc(ROOT / "process" / "CONSISTENCY.md", "Cross-level consistency review")]
proc += [doc(ROOT / "course" / f"level-{n}" / "GAUNTLET.md", f"Critic rounds · Level {n}") for n, _, _ in LEVELS]
groups.append({"name": "How it was built", "band": "", "docs": proc})

data = json.dumps(groups, ensure_ascii=False).replace("</", "<\\/")
body = (ROOT / "tools" / "site_template.html").read_text().replace("__DATA__", data)
if "--artifact" in sys.argv:
    OUT = pathlib.Path(sys.argv[sys.argv.index("--artifact") + 1]); page = body
else:
    page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '<meta name="description" content="A free, research-backed English reading course for any age, from first sounds to C1.">\n'
            '<style>html,body{margin:0}</style>\n</head>\n<body>\n' + body + '\n</body>\n</html>\n')
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(page)
n = sum(len(g["docs"]) for g in groups)
print(f"{OUT} — {n} pages, {OUT.stat().st_size/1e6:.1f} MB")
assert n > 100 and OUT.stat().st_size < 16e6
