#!/usr/bin/env python3
"""Compare a clean archive build with the delivered local build."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from pypdf import PdfReader

parser = argparse.ArgumentParser()
parser.add_argument("clean_directory")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
clean = Path(args.clean_directory)
original = PdfReader(root / "tmp/build/main.pdf")
rebuilt = PdfReader(clean / "build/main.pdf")
same_text = [p.extract_text() for p in original.pages] == [p.extract_text() for p in rebuilt.pages]
log = (clean / "build/main.log").read_text()
warnings = bool(re.search(r"Overfull|undefined|Missing character|LaTeX Warning|Package .* Warning", log, re.I))
files = ["main.tex", "main.bbl", "references.bib", "figures/heat-edge/figure.pdf"]
files += [str(p.relative_to(root)) for p in sorted((root / "sections").glob("*.tex"))]
different = [p for p in files if (root / p).read_bytes() != (clean / p).read_bytes()]
render_history_available = (root / "tmp/render/page-01.png").exists() and (root / "tmp/render-final/page-01.png").exists()
same_first_twenty_renders = all(
    (root / f"tmp/render/page-{i:02d}.png").read_bytes()
    == (root / f"tmp/render-final/page-{i:02d}.png").read_bytes()
    for i in range(1, 21)
) if render_history_available else None
result = {
    "status": "PASS" if same_text and not warnings and not different and same_first_twenty_renders is not False else "FAIL",
    "source_files_compared": len(files),
    "different_source_files": different,
    "local_pages": len(original.pages),
    "clean_pages": len(rebuilt.pages),
    "pagewise_extracted_text_identical": same_text,
    "clean_build_warning_patterns": warnings,
    "previously_inspected_pages_1_to_20_pixel_identical_after_bibliography_change": same_first_twenty_renders,
    "final_page_21_review": "separate visual inspection required",
    "source_archive_sha256": hashlib.sha256((root / "output/arxiv-source.zip").read_bytes()).hexdigest(),
    "boundary": "A local Tectonic rebuild, not a test of the remote arXiv service.",
}
(root / "audits/reproducible-build.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
raise SystemExit(result["status"] != "PASS")
