#!/usr/bin/env python3
"""Verify stored input bytes. This does not verify mathematics or NS dynamics."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
BASE = Path(__file__).resolve().parent
COUNTS = {}
FAILURES = []
PATHS = set()


def verify(path, digest, size, origin):
    target = (ROOT / path).resolve()
    if not target.is_relative_to(ROOT):
        raise ValueError('Input outside the reverse scientific worktree')
    raw = target.read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    COUNTS[origin] = COUNTS.get(origin, 0) + 1
    PATHS.add(path)
    if actual != digest or (size is not None and len(raw) != size):
        FAILURES.append(dict(path=path, expected=digest, actual=actual,
                             expected_bytes=size, actual_bytes=len(raw), origin=origin))


def walk(obj, origin):
    if isinstance(obj, dict):
        if {'path', 'sha256'} <= obj.keys():
            verify(obj['path'], obj['sha256'], obj.get('bytes'), origin)
        for value in obj.values():
            walk(value, origin)
    elif isinstance(obj, list):
        for value in obj:
            walk(value, origin)


for filename, minimum in [('sources/source-hashes.json', 9),
                          ('root-review-inputs.json', 19)]:
    walk(json.loads((BASE / filename).read_text(encoding='utf-8')), filename)
    if COUNTS.get(filename, 0) < minimum:
        raise ValueError('Incomplete input manifest: ' + filename)

pattern = re.compile(r'\|\s*`([^`]+)`\s*\|(?:[^\n|]*\|)?\s*`([0-9a-f]{64})`\s*\|')
for filename, number in [('ANALYTIC_PREFLIGHT.md', 3),
                         ('ANALYTIC_INDEPENDENT_REVIEW.md', 4),
                         ('FIRST_RESPONSE_BUDGET.md', 5),
                         ('HYBRID_DERIVATION.md', 3),
                         ('HYBRID_INDEPENDENT_REVIEW.md', 5),
                         ('RESIDUAL_COST_PREFLIGHT.md', 2),
                         ('COST_INDEPENDENT_REVIEW.md', 4)]:
    rows = pattern.findall((BASE / filename).read_text(encoding='utf-8'))
    if len(rows) != number:
        raise ValueError(f'Incomplete input table: {filename}: {len(rows)}')
    for path, digest in rows:
        verify(path, digest, None, filename)

static_runs = []
for filename in ['backend-probe-independent-run.json', 'backend-probe-run.json']:
    run = json.loads((BASE / filename).read_text(encoding='utf-8'))
    if run['status'] != 'STATIC_KERNEL_DIAGNOSTIC_NOT_NS_TRAJECTORY' or run['result'] != 'PASS':
        raise ValueError('Static kernel diagnostic failed: ' + filename)
    if not all(run['checks'].values()) or run['config']['time_steps'] != 0:
        raise ValueError('Unexpected static diagnostic scope: ' + filename)
    digest = hashlib.sha256(json.dumps(run['config'], sort_keys=True,
                                     separators=(',', ':')).encode()).hexdigest()
    if digest != run['config_sha256']:
        raise ValueError('Static configuration binding mismatch: ' + filename)
    for path, digest in run['source_sha256'].items():
        verify(str(Path(path).relative_to(ROOT)), digest, None, filename)
    static_runs.append(run)

# Compare deterministic static diagnostics; observed time and memory may differ.
static_equal = all(static_runs[0][key] == static_runs[1][key]
                   for key in ['config', 'checks', 'N_definition_max_error', 'static_cases'])
if not static_equal:
    FAILURES.append(dict(reason='Independent and root static outputs differ'))

result = dict(scope='Actual byte verification only; not mathematical recomputation',
              checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              counts=COUNTS, total=sum(COUNTS.values()), unique_files=len(PATHS),
              independent_and_root_static_diagnostics_equal=static_equal,
              all_match=not FAILURES, failures=FAILURES)
print(json.dumps(result, indent=2))
if FAILURES:
    raise SystemExit(1)
