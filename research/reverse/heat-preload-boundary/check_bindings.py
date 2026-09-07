#!/usr/bin/env python3
"""Byte verification only; no numerical or mathematical certificate is claimed."""
from pathlib import Path
import hashlib, json, re
ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
counts={}
failures=[]

def verify(path,digest,size,origin):
    p=(ROOT/path).resolve()
    if not p.is_relative_to(ROOT):
        raise ValueError('Outside scientific worktree')
    data=p.read_bytes()
    actual=hashlib.sha256(data).hexdigest()
    counts[origin]=counts.get(origin,0)+1
    if actual!=digest or (size is not None and len(data)!=size):
        failures.append({'path':path,'expected':digest,'actual':actual,'origin':origin})

def walk(x,origin):
    if isinstance(x,dict):
        if {'path','sha256'}<=x.keys():
            verify(x['path'],x['sha256'],x.get('bytes'),origin)
        for v in x.values(): walk(v,origin)
    elif isinstance(x,list):
        for v in x: walk(v,origin)

for name,n in [('history-review-inputs.json',20),('history-search-manifest.json',283)]:
    walk(json.loads((BASE/name).read_text()),name)
    if counts.get(name)!=n: raise ValueError(f'Incomplete {name}')

pattern=re.compile(r'\|\s*`([^`]+)`\s*\|(?:[^\n|]*\|)?\s*`([0-9a-f]{64})`\s*\|')
for name,n in [('INDEPENDENT_REVIEW.md',7),('DERIVATION.md',3)]:
    rows=pattern.findall((BASE/name).read_text())
    if len(rows)!=n: raise ValueError(f'Incomplete {name}: {len(rows)}')
    for path,digest in rows: verify(path,digest,None,name)

result={'scope':'Actual byte checks; not mathematical recomputation',
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'independent_review_sha256':hashlib.sha256((BASE/'INDEPENDENT_REVIEW.md').read_bytes()).hexdigest(),
        'counts':counts,'total':sum(counts.values()),'all_match':not failures,'failures':failures}
print(json.dumps(result,ensure_ascii=False,indent=2))
if failures: raise SystemExit(1)
