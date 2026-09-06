#!/usr/bin/env python3
"""Structural/provenance checks only; not a PDE or proof certificate."""
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "910e60d0c3e595331cdb4c2dd8e2a8d184f96b9a"
MAIN = "research/clay_b_vertical_pressure_test_20260907.md"
LEDGER = "research/clay_b_vertical_pressure_test_ledger_20260907.json"
CP = "research/clay_b_active_checkpoint_20260906.json"
SCRIPT = "scripts/clay_b_vertical_pressure_test_record_qa.py"
PAPER_SHA = "c9755ea86f93575cc96c28ac5b3caa1a059bddec2b58a448d09d9cc54d6431c5"
AGENTS_SHA = "80959a5c6d2db01543f8f1ae1ddc2e1ba7430c1b14d1b4ef658dcc965efecfab"

def digest(b):
    return hashlib.sha256(b).hexdigest()

def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])

def preserved(before, after):
    mutable = {"checkpoint_id", "status", "current_working_source",
               "current_working_sources", "current_question",
               "current_internal_work", "next_step"}
    return all(after.get(k) == v for k, v in before.items() if k not in mutable)

def tags(s):
    return re.findall(r"\\tag\{YT\.(\d+)\}", s) == [str(i) for i in range(1, 13)]

raw = {p: (ROOT / p).read_bytes() for p in (MAIN, LEDGER, CP, SCRIPT)}
main = raw[MAIN].decode()
ledger, current = json.loads(raw[LEDGER]), json.loads(raw[CP])
before = json.loads(git("show", BASE + ":" + CP))
checks = []

def check(name, value):
    checks.append({"name": name, "passed": bool(value)})

check("UTF8_LF_single_final_newline",
      all(b"\r" not in b and b.endswith(b"\n") and not b.endswith(b"\n\n")
          for b in raw.values()))
check("twelve_ordered_YT_labels_and_paired_displays",
      tags(main) and main.count(r"\[") == main.count(r"\]") > 12)
check("plain_style_and_scope_guards",
      all(x not in main for x in ("我们", "攻关", "主攻", "三重审计"))
      and all(x in main for x in ("OPEN / NOT CLAY", "完整父柱体", "固定内部图",
                                  "这个接口到此停止", "比较流")))
check("source_version_and_actual_review_status",
      len(ledger["sources"]) == 1
      and ledger["sources"][0]["arxiv"] == "2606.08352"
      and ledger["sources"][0]["version"] == "v1"
      and ledger["review_status"] == "complete_scoped_nonauthor_review"
      and ledger["review_failure_log"][0]["result"] == "no_review_output")
check("all_old_state_and_26_review_values_preserved",
      preserved(before, current)
      and len([k for k in before if "review" in k]) == 26
      and len([k for k in current if "review" in k]) == 27
      and "vertical_pressure_test_review" in current
      and all(current[k] == v for k, v in before.items() if "review" in k))
paper_raw = json.dumps(current["paper"], sort_keys=True).encode()
check("private_paper_and_16_release_identities",
      digest(paper_raw) == PAPER_SHA and current["paper"] == before["paper"]
      and len(current["earlier_scientific_releases"]) + 2 == 16
      and current["earlier_scientific_releases"] == before["earlier_scientific_releases"]
      and current["previous_scientific_release"] == before["previous_scientific_release"]
      and all(current[k] == before[k] for k in
              ("source_commit", "freeze_commit", "last_scientific_release",
               "last_handoff_receipt", "handoff_sent_once")))
bindings = []
for row in ledger["local_provenance"]:
    b = (ROOT / row["path"]).read_bytes()
    bindings.append({"path": row["path"],
                     "raw_equals_base": b == git("show", BASE + ":" + row["path"]),
                     "metadata_matches": len(b) == row["bytes"]
                     and b.count(b"\n") == row["lines"] and digest(b) == row["sha256"]})
check("six_historical_raw_bindings",
      len(bindings) == 6 and all(b["raw_equals_base"] and b["metadata_matches"]
                                for b in bindings))
check("internal_record_no_new_release_or_simulation",
      ledger["is_research_release"] is False and current["is_research_release"] is False
      and current["current_internal_work"]["handoff_sent"] is False
      and ledger["outputs"]["publication_handoff"] is False
      and ledger["outputs"]["simulation"] is False
      and ledger["outputs"]["DGX"] is False
      and ledger["outputs"]["new_reader_pdf"] is False)
check("user_AGENTS_and_existing_tracked_scope",
      digest((ROOT / "AGENTS.md").read_bytes()) == AGENTS_SHA
      and set(git("diff", "--name-only", "--diff-filter=M", BASE).decode().splitlines())
      <= {"AGENTS.md", CP})
mutated = copy.deepcopy(current)
mutated["paper"] = {}
negative = [
    {"name": "missing_YT10_rejected", "passed": not tags(main.replace(r"\tag{YT.10}", ""))},
    {"name": "changed_private_paper_rejected", "passed": not preserved(before, mutated)},
]
check("two_in_memory_record_negative_controls", all(c["passed"] for c in negative))
out = {"schema_version": 1,
       "scope": "Structural labels, protected state and raw Git provenance only; not mathematical proof, PDE simulation/certificate, dual implementation or novelty certification.",
       "base_commit": BASE,
       "status": "passed" if all(c["passed"] for c in checks) else "failed",
       "checks": checks, "negative_controls": negative, "historical_bindings": bindings,
       "paper_serialization": "Python json.dumps(paper, sort_keys=True), default ensure_ascii=True and separators; UTF8, no appended newline",
       "paper_sha256": digest(paper_raw),
       "artifacts": [{"path": p, "bytes": len(b), "lines": b.count(b"\n"), "sha256": digest(b)}
                     for p, b in raw.items()]}
print(json.dumps(out, ensure_ascii=False, indent=2))
raise SystemExit(0 if out["status"] == "passed" else 1)
