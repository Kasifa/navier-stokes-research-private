#!/usr/bin/env python3
"""Verify recorded source/review bytes only; not a mathematical proof checker."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/reverse/reconnection-preflight'
records = []

def add(path, expected, origin, size=None):
    p = Path(path)
    if not p.is_absolute():
        p = ROOT / p
    p = p.resolve()
    if not p.is_relative_to(ROOT):
        raise ValueError('Binding escapes scientific worktree')
    data = p.read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    ok = actual == expected and (size is None or len(data) == size)
    records.append({'path': str(p.relative_to(ROOT)), 'origin': origin,
                    'expected_sha256': expected, 'actual_sha256': actual,
                    'bytes': len(data), 'match': ok})

def walk(obj, origin):
    if isinstance(obj, dict):
        if {'path', 'sha256'} <= obj.keys():
            add(obj['path'], obj['sha256'], origin, obj.get('bytes'))
        for value in obj.values():
            walk(value, origin)
    elif isinstance(obj, list):
        for value in obj:
            walk(value, origin)

for name in ('theory/SOURCE_MANIFEST.json', 'numerics/source-hashes.json'):
    obj = json.loads((BASE / name).read_text())
    walk(obj, name)
    if name.startswith('numerics/'):
        for suffix, key in (('pdf', 'pdf'), ('txt', 'text')):
            add(BASE / f'numerics/kerr-1212.3829v2.{suffix}',
                obj[f'{key}_sha256'], name, obj[f'{key}_bytes'])

row = re.compile(r'\|\s*`([^`]+)`\s*\|\s*`([a-f0-9]{64})`\s*\|')
for name, expected_count, relative_base in (
    ('PREFLIGHT_REVIEW.md', 18, ROOT),
    ('STOKES_BASELINE_LEMMA.md', 5, BASE),
):
    text = (BASE / name).read_text()
    if '<!-- INPUT_HASH_TABLE -->' in text:
        raise ValueError('Unfinished review table')
    matches = row.findall(text)
    if len(matches) != expected_count:
        raise ValueError(f'{name}: expected {expected_count} bindings, got {len(matches)}')
    for path, digest in matches:
        add(relative_base / path, digest, name)

text = (BASE / 'SOURCE_ATTRIBUTION_LEMMA.md').read_text()
blocks = re.findall(r'```json\s*(.*?)\s*```', text, re.S)
if len(blocks) != 1:
    raise ValueError('Expected exactly one attribution input record')
obj = json.loads(blocks[0])
if len(obj['inputs']) != 2:
    raise ValueError('Changed attribution input schema')
walk(obj['inputs'], 'SOURCE_ATTRIBUTION_LEMMA.md')

result = {
    'scope': 'Actual source and review byte bindings; not mathematical validation',
    'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'review_sha256': hashlib.sha256((BASE / 'PREFLIGHT_REVIEW.md').read_bytes()).hexdigest(),
    'records_checked': len(records),
    'unique_files_checked': len({x['path'] for x in records}),
    'all_match': all(x['match'] for x in records),
    'records': records,
}
print(json.dumps(result, indent=2, ensure_ascii=False))
if not result['all_match']:
    raise SystemExit(1)
