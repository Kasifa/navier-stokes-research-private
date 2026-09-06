#!/usr/bin/env python3
"""Deterministic record/provenance QA, not a PDE or novelty certificate."""
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "8aa141cac7027101f1bfc3301d18e1011e5040bb"
PREFIX = "research/clay_b_leray_paid_budget"
MAIN = PREFIX + "_20260907.md"
REPORT = PREFIX + "_report-source_20260907.md"
LEDGER = PREFIX + "_literature_ledger_20260907.json"
CHECKPOINT = "research/clay_b_active_checkpoint_20260906.json"
SCRIPT = "scripts/clay_b_leray_paid_budget_record_qa.py"
AGENTS_SHA = "80959a5c6d2db01543f8f1ae1ddc2e1ba7430c1b14d1b4ef658dcc965efecfab"
PAPER_SHA = "c9755ea86f93575cc96c28ac5b3caa1a059bddec2b58a448d09d9cc54d6431c5"

def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def valid_tags(value):
    return re.findall(r"\\tag\{LP\.(\d+)\}", value) == [str(i) for i in range(1, 15)]

def review_values_preserved(before, after):
    return all(after.get(k) == v for k, v in before.items() if "review" in k)

def ids(value):
    return [value["last_scientific_release"],
            value["previous_scientific_release"]["release_id"],
            *[r["release_id"] for r in value["earlier_scientific_releases"]]]

raws = {p: (ROOT / p).read_bytes() for p in (MAIN, REPORT, LEDGER, CHECKPOINT, SCRIPT)}
main = raws[MAIN].decode("utf-8")
report = raws[REPORT].decode("utf-8")
ledger = json.loads(raws[LEDGER])
current = json.loads(raws[CHECKPOINT])
before = json.loads(git("show", BASE + ":" + CHECKPOINT))
results = []

def check(name, value):
    results.append({"name": name, "passed": bool(value)})

check("UTF8_LF_single_final_newline",
      all(b"\r" not in b and b.endswith(b"\n") and not b.endswith(b"\n\n")
          for b in raws.values()))
check("fourteen_unique_ordered_LP_labels", valid_tags(main))
check("fourteen_display_math_pairs", main.count("\\[") == main.count("\\]") == 14)
check("plain_first_person_and_claim_boundary",
      all(x not in main + report for x in ("我们", "攻关", "主攻", "三重审计"))
      and all(x in main and x in report for x in ("OPEN", "NOT CLAY")))
check("five_unique_versioned_sources",
      len(ledger["sources"]) == len({x["id"] for x in ledger["sources"]}) == 5
      and all(x["url"].startswith("https://") and x["version"] and x["date"]
              for x in ledger["sources"]))
check("all_research_plan_steps_complete",
      all(s["status"] == "complete" for s in ledger["plan"]["steps"]))
check("internal_record_not_release",
      ledger["is_research_release"] is False
      and current["is_research_release"] is False
      and current["current_internal_work"]["handoff_sent"] is False)
old_review_keys = [k for k in before if "review" in k]
check("all_23_old_review_values_preserved",
      len(old_review_keys) == 23 and review_values_preserved(before, current))
check("one_new_review_only",
      len([k for k in current if "review" in k]) == 24
      and "leray_paid_budget_review" in current)
paper_raw = json.dumps(current["paper"], sort_keys=True).encode()
check("private_paper_parsed_value_and_exact_serialization",
      current["paper"] == before["paper"] and digest(paper_raw) == PAPER_SHA)
mutable = {"checkpoint_id", "status", "current_working_source",
           "current_working_sources", "current_question", "current_internal_work",
           "next_step"}
check("every_other_old_checkpoint_value_preserved",
      all(current.get(k) == v for k, v in before.items() if k not in mutable))
check("all_16_release_ids_and_order_preserved",
      ids(before) == ids(current) and len(ids(current)) == len(set(ids(current))) == 16)
historical = []
for row in ledger["local_provenance"]:
    b = (ROOT / row["path"]).read_bytes()
    historical.append({
        "path": row["path"],
        "raw_and_base_identical": b == git("show", BASE + ":" + row["path"]),
        "metadata_matches": digest(b) == row["sha256"] and len(b) == row["bytes"]
                            and b.count(b"\n") == row["lines"],
    })
check("six_historical_raw_base_bindings",
      len(historical) == 6 and all(x["raw_and_base_identical"] and x["metadata_matches"]
                                  for x in historical))
check("user_AGENTS_unchanged", digest((ROOT / "AGENTS.md").read_bytes()) == AGENTS_SHA)
modified = git("diff", "--name-only", "--diff-filter=M", BASE).decode().splitlines()
check("existing_tracked_changes_scoped",
      set(modified) <= {"AGENTS.md", CHECKPOINT})

# In-memory record/label negative controls. They do not mutate mathematical files,
# validate a PDE proof, or constitute a second mathematical implementation.
negative = []
negative.append({"name": "missing_LP14_rejected",
                 "passed": not valid_tags(main.replace("\\tag{LP.14}", ""))})
negative.append({"name": "duplicate_LP7_rejected",
                 "passed": not valid_tags(main + "\n\\tag{LP.7}")})
mutated = copy.deepcopy(current)
mutated[old_review_keys[0]] = "__changed__"
negative.append({"name": "changed_old_review_rejected",
                 "passed": not review_values_preserved(before, mutated)})
results.append({"name": "three_record_negative_controls",
                "passed": all(x["passed"] for x in negative)})

out = {
    "schema_version": 1,
    "scope": "Structural, preservation and raw Git provenance only; not mathematical proof, numerical PDE certificate, dual implementation, novelty or visual QA.",
    "base_commit": BASE,
    "status": "passed" if all(x["passed"] for x in results) else "failed",
    "checks": results,
    "negative_controls": negative,
    "historical_bindings": historical,
    "paper_serialization": "Python json.dumps(paper, sort_keys=True); ensure_ascii=True, separators=(', ', ': '); UTF-8; no appended newline",
    "paper_sha256": digest(paper_raw),
    "artifacts": [{"path": p, "bytes": len(b), "lines": b.count(b"\n"), "sha256": digest(b)}
                  for p, b in raws.items()],
}
print(json.dumps(out, ensure_ascii=False, indent=2))
raise SystemExit(0 if out["status"] == "passed" else 1)
