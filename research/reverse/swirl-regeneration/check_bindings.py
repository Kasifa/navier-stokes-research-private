#!/usr/bin/env python3
"""Verify actual review input bindings; this is not a mathematical certificate."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE = Path(__file__).resolve().parent
REVIEWS = (
    "REMAINDER_REVIEW.md",
    "CENTER_STRETCH_REVIEW.md",
    "SOURCE_HISTORY_REVIEW.md",
    "FINAL_REVIEW.md",
)


def digest(blob):
    return hashlib.sha256(blob).hexdigest()


def verify_record(rel, expected, expected_bytes=None):
    target = (ROOT / rel).resolve()
    target.relative_to(ROOT)
    actual_blob = target.read_bytes()
    actual = digest(actual_blob)
    if actual != expected or (expected_bytes is not None and len(actual_blob) != expected_bytes):
        raise ValueError(f"Stale binding: {rel}")
    return {"path": rel, "sha256": actual, "bytes": len(actual_blob)}


def main():
    result = {"scope": "REVIEW_INPUT_BYTES_ONLY_NOT_MATHEMATICAL_CERTIFICATE", "reviews": []}
    for name in REVIEWS:
        review = BASE / name
        blob = review.read_bytes()
        rows = []
        for line in blob.decode("utf-8").splitlines():
            cells = [cell.strip().strip("`") for cell in line.split("|")]
            paths = [cell for cell in cells if cell.startswith("research/")]
            hashes = [cell for cell in cells if re.fullmatch("[0-9a-f]{64}", cell)]
            if not paths or not hashes:
                continue
            if len(paths) != 1 or len(hashes) != 1:
                raise ValueError(f"Ambiguous binding in {name}: {line}")
            rel, expected = paths[0], hashes[0]
            rows.append(verify_record(rel, expected))
        corpora = []
        if name == "SOURCE_HISTORY_REVIEW.md":
            blocks = re.findall(r"```json\n(.*?)\n```", blob.decode("utf-8"), re.S)
            if len(blocks) != 1:
                raise ValueError("Expected one source-history JSON binding block")
            ledger = json.loads(blocks[0])
            if ledger["schema"] != "source-history-input-binding-v1":
                raise ValueError("Unrecognized source-history schema")
            rows.extend(verify_record(r["path"], r["sha256"], r["bytes"])
                        for r in ledger["directly_used_inputs"])
            selectors = {
                "public/notes/r0-{1..20}.html": [ROOT / f"public/notes/r0-{j}.html" for j in range(1, 21)],
                "research/r073*.md (top-level only)": list((ROOT / "research").glob("r073*.md")),
            }
            for corpus in ledger["search_corpora"]:
                records = []
                for path in sorted(selectors[corpus["selector"]]):
                    data = path.read_bytes()
                    records.append({"path": str(path.relative_to(ROOT)), "bytes": len(data), "sha256": digest(data)})
                encoded = json.dumps(records, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode()
                if (len(records) != corpus["files"] or
                        sum(r["bytes"] for r in records) != corpus["bytes"] or
                        digest(encoded) != corpus["manifest_sha256"]):
                    raise ValueError(f"Stale search corpus: {corpus['selector']}")
                corpora.append(corpus)
        if not rows:
            raise ValueError(f"No recognized bindings in {name}")
        result["reviews"].append({
            "review": str(review.relative_to(ROOT)),
            "sha256": digest(blob),
            "bindings": rows,
            "search_corpora_bytes_only": corpora,
        })
    result["status"] = "PASS"
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
