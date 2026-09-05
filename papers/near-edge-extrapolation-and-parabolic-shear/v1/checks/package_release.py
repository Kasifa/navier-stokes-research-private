#!/usr/bin/env python3
"""Create deterministic archives and a non-self-referential SHA-256 source manifest."""
import hashlib
import json
import shutil
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parents[1]
output = root / "output"
(output / "pdf").mkdir(parents=True, exist_ok=True)
shutil.copy2(root / "tmp/build/main.pdf", output / "pdf/near-edge-parabolic-shear.pdf")
shutil.copy2(root / "tmp/build/main.bbl", root / "main.bbl")
essential = ["main.tex", "references.bib", "main.bbl", "figures/heat-edge/figure.pdf"]
essential += [str(p.relative_to(root)) for p in sorted((root / "sections").glob("*.tex"))]
payload = essential + ["README.md", "build.sh", "work-plan.md", "provenance.md", "supplementary-research.md", ".gitignore"]
for directory in ["audits", "literature", "checks", "figures/heat-edge", "history"]:
    payload += [str(p.relative_to(root)) for p in sorted((root / directory).rglob("*"))
                if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"]
payload = sorted(set(payload))
hashes = {p: hashlib.sha256((root / p).read_bytes()).hexdigest() for p in payload}
manifest = {
    "version": "1.0-local-review-2026-09-05",
    "algorithm": "SHA-256",
    "exclusions": ["source-manifest.json itself", "output archives", "derived PDF", "tmp"],
    "files": hashes,
}
(root / "source-manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
def archive(name, paths):
    dest = output / name
    with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for rel in sorted(paths):
            item = zipfile.ZipInfo(rel, (2026, 9, 5, 0, 0, 0))
            item.compress_type = zipfile.ZIP_DEFLATED
            item.external_attr = 0o100644 << 16
            z.writestr(item, (root / rel).read_bytes())
    return {"file": name, "entries": len(paths), "bytes": dest.stat().st_size,
            "sha256": hashlib.sha256(dest.read_bytes()).hexdigest()}
result = {
    "source": archive("arxiv-source.zip", essential),
    "research_package": archive("complete-research-package.zip", payload + ["source-manifest.json"]),
    "pdf": {"file": "pdf/near-edge-parabolic-shear.pdf",
            "sha256": hashlib.sha256((output / "pdf/near-edge-parabolic-shear.pdf").read_bytes()).hexdigest()},
    "note": "Packaging is not submission or publication.",
}
(output / "delivery-manifest.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
