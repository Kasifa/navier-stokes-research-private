#!/usr/bin/env python3
"""Structural PDF/source checks and review contact sheets; not a proof checker."""
import argparse
import json
import re
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--pdf", default="tmp/build/main.pdf")
parser.add_argument("--log", default="tmp/build/main.log")
parser.add_argument("--render-dir")
parser.add_argument("--report", default="tmp/document-quality.json")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
from pypdf import PdfReader

texts = [root / "main.tex", *sorted((root / "sections").glob("*.tex"))]
source = "\n".join(p.read_text() for p in texts)
labels = re.findall(r"\\label\{([^}]+)\}", source)
refs = re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", source)
citation_groups = re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}", source)
citations = {key.strip() for group in citation_groups for key in group.split(",")}
bibkeys = set(re.findall(r"@\w+\{([^,]+),", (root / "references.bib").read_text()))
log = (root / args.log).read_text()
reader = PdfReader(root / args.pdf)
page_text = [page.extract_text() for page in reader.pages]
issues = []
if len(labels) != len(set(labels)):
    issues.append("duplicate TeX labels")
if set(refs) - set(labels):
    issues.append("missing labels: " + str(sorted(set(refs) - set(labels))))
if citations - bibkeys:
    issues.append("missing bibliography keys: " + str(sorted(citations - bibkeys)))
for pattern in [r"Overfull \\[hv]box", r"undefined", r"Missing character", r"LaTeX Warning", r"Package .* Warning"]:
    if re.search(pattern, log, re.I):
        issues.append("TeX log pattern: " + pattern)
for index, text in enumerate(page_text, 1):
    if len(text.strip()) < 30:
        issues.append(f"nearly blank page {index}")
    if "??" in text or "\ufffd" in text:
        issues.append(f"unresolved/corrupt text on page {index}")
for token in ["TODO", "TBD", "PLACEHOLDER", "citation needed"]:
    if token in source:
        issues.append("placeholder: " + token)
if reader.metadata.author != "C. K. Zeng":
    issues.append("author metadata mismatch")

contact_sheets = []
if args.render_dir:
    from PIL import Image, ImageDraw
    render_dir = root / args.render_dir
    pages = sorted(render_dir.glob("page-*.png"))
    if len(pages) != len(reader.pages):
        issues.append("rendered page count mismatch")
    for start in range(0, len(pages), 4):
        canvas = Image.new("RGB", (1240, 1770), "#dddddd")
        draw = ImageDraw.Draw(canvas)
        for local, path in enumerate(pages[start:start+4]):
            img = Image.open(path).convert("RGB")
            img.thumbnail((600, 840))
            x = 10 + (local % 2) * 620
            y = 26 + (local // 2) * 880
            canvas.paste(img, (x, y))
            draw.text((x, y - 18), f"Page {start+local+1}", fill="black")
        dest = render_dir / f"contact-{start+1:02d}-{min(start+4,len(pages)):02d}.png"
        canvas.save(dest)
        contact_sheets.append(str(dest.relative_to(root)))

result = {
    "scope": "structural checks; visual review is separate; no proof certification",
    "pages": len(reader.pages),
    "source_files": len(texts),
    "labels": len(labels),
    "cross_references": len(refs),
    "cited_sources": len(citations),
    "bib_entries": len(bibkeys),
    "issues": issues,
    "contact_sheets": contact_sheets,
    "verdict": "PASS" if not issues else "FAIL",
}
report = root / args.report
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
raise SystemExit(bool(issues))
