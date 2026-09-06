#!/usr/bin/env python3
"""Record/provenance checks only. No PDE proof or numerical certificate."""
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "ea68cfdd4d29c60aef4ebe052f160c7461bbd1b6"
MAIN = "research/clay_b_inverse_cascade_strategy_20260907.md"
LEDGER = "research/clay_b_inverse_cascade_strategy_ledger_20260907.json"
CP = "research/clay_b_active_checkpoint_20260906.json"
SCRIPT = "scripts/clay_b_inverse_cascade_strategy_record_qa.py"
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
    return re.findall(r"\\tag\{IS\.(\d+)\}", s) == [str(i) for i in range(1, 8)]

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
check("seven_ordered_IS_labels_and_display_pairs",
      tags(main) and main.count(r"\[") == main.count(r"\]") == 7)
check("plain_style_and_open_claims",
      all(x not in main for x in ("我们", "攻关", "主攻", "三重审计"))
      and all(x in main for x in ("OPEN", "NOT CLAY", "没有选定新的证明候选")))
check("versioned_sources_and_review_status",
      [(s["version"], s["date"]) for s in ledger["sources"]]
      == [("v1", "2025-09-23"), ("v2", "2026-01-12")]
      and ledger["review_status"] == "complete_scoped_nonauthor_review")
check("all_old_checkpoint_values_except_current_state_preserved",
      preserved(before, current))
check("24_old_review_values_and_one_new_review",
      len([k for k in before if "review" in k]) == 24
      and len([k for k in current if "review" in k]) == 25
      and "inverse_cascade_strategy_review" in current
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
check("ten_historical_raw_bindings",
      len(bindings) == 10 and all(b["raw_equals_base"] and b["metadata_matches"]
                                 for b in bindings))
check("internal_record_no_new_release",
      ledger["is_research_release"] is False and current["is_research_release"] is False
      and current["current_internal_work"]["handoff_sent"] is False
      and ledger["outputs"]["publication_handoff"] is False)
check("user_AGENTS_and_existing_tracked_scope",
      digest((ROOT / "AGENTS.md").read_bytes()) == AGENTS_SHA
      and set(git("diff", "--name-only", "--diff-filter=M", BASE).decode().splitlines())
      <= {"AGENTS.md", CP})
mutated = copy.deepcopy(current)
mutated["paper"] = {}
negative = [
    {"name": "missing_IS7_rejected", "passed": not tags(main.replace(r"\tag{IS.7}", ""))},
    {"name": "changed_private_paper_rejected", "passed": not preserved(before, mutated)},
]
check("two_in_memory_record_negative_controls", all(c["passed"] for c in negative))
out = {"schema_version": 1,
       "scope": "Structural labels, protected state and raw Git provenance only; not PDE proof, dual implementation, novelty, source-theorem certification or visual QA.",
       "base_commit": BASE,
       "status": "passed" if all(c["passed"] for c in checks) else "failed",
       "checks": checks, "negative_controls": negative, "historical_bindings": bindings,
       "paper_serialization": "Python json.dumps(paper, sort_keys=True), default ensure_ascii=True and separators; UTF8, no appended newline",
       "paper_sha256": digest(paper_raw),
       "artifacts": [{"path": p, "bytes": len(b), "lines": b.count(b"\n"), "sha256": digest(b)}
                     for p, b in raw.items()]}
print(json.dumps(out, ensure_ascii=False, indent=2))
raise SystemExit(0 if out["status"] == "passed" else 1)
