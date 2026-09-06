#!/usr/bin/env python3
"""Fail-closed source and compilation-log checks; no PDF generation."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser()
p.add_argument('--build-dir', type=Path)
a = p.parse_args()
files = [ROOT/'main.tex'] + sorted((ROOT/'sections').glob('*.tex'))
texts = {str(f.relative_to(ROOT)): f.read_text() for f in files}
alltext = '\n'.join(texts.values())
labels = re.findall(r'\\label\{([^}]+)\}', alltext)
refs = re.findall(r'\\(?:eqref|ref|pageref)\{([^}]+)\}', alltext)
cites = [key.strip() for group in re.findall(r'\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}', alltext)
         for key in group.split(',')]
bib = (ROOT/'references.bib').read_text()
keys = re.findall(r'@\w+\s*\{\s*([^,]+),', bib)
errors = []
for label, n in Counter(labels).items():
    if n != 1: errors.append('duplicate label '+label)
for key, n in Counter(keys).items():
    if n != 1: errors.append('duplicate citation key '+key)
errors += ['unresolved reference '+x for x in sorted(set(refs)-set(labels))]
errors += ['unresolved citation '+x for x in sorted(set(cites)-set(keys))]
for name,text in texts.items():
    stack=[]
    for match in re.finditer(r'\\(begin|end)\{([^}]+)\}',text):
        kind,env=match.groups()
        if kind=='begin':stack.append(env)
        elif not stack or stack.pop()!=env:errors.append('environment mismatch '+name+':'+env)
    if stack:errors.append('unclosed environments '+name+':'+str(stack))
    for target in re.findall(r'\\input\{([^}]+)\}',text):
        if not (ROOT/(target+'.tex')).is_file():errors.append('missing input '+target)
    for target in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',text):
        if not (ROOT/target).is_file():errors.append('missing image '+target)
for path in sorted(ROOT.rglob('*')):
    if any(x in {'output','tmp','__pycache__'} for x in path.parts):continue
    if path.suffix not in {'.md','.tex','.bib','.py','.json','.sh'}:continue
    data=path.read_bytes()
    controls=[x for x in data if x<32 and x not in (9,10)]
    if controls:errors.append('ASCII control characters '+str(path.relative_to(ROOT)))
    if path.suffix=='.md' and b'\\)' in data and b'\\(' not in data:
        errors.append('unmatched inline math delimiters '+str(path.relative_to(ROOT)))
log_result=None
if a.build_dir:
    logfile=a.build_dir/'main.log';blg=a.build_dir/'main.blg';xdv=a.build_dir/'main.xdv'
    if not all(f.is_file() for f in [logfile,blg,xdv]):errors.append('missing compilation result')
    else:
        log=logfile.read_text();biblog=blg.read_text()
        flags=re.findall(r'^.*(?:Overfull|Undefined control|Missing character|LaTeX Warning|Package .* Warning|^!).*$',log,re.M)
        flags+=re.findall(r'^.*(?:Warning--|error message).*$' ,biblog,re.M)
        if flags:errors += flags
        page=re.search(r'Output written on main\.xdv \((\d+) pages',log)
        log_result={'output':'XDV only','pages':int(page.group(1)) if page else None,
                    'xdv_sha256':hashlib.sha256(xdv.read_bytes()).hexdigest(),
                    'log_sha256':hashlib.sha256(logfile.read_bytes()).hexdigest(),
                    'blocking_warnings':flags,'reader_pdf_generated':False,
                    'visual_manuscript_review':'not performed; source/XDV delivery, no reader PDF'}
        if (a.build_dir/'main.pdf').exists():errors.append('unexpected reader PDF')
result={'status':'PASS' if not errors else 'FAIL','errors':errors,
        'tex_sources':len(files),'labels':len(labels),'references':len(refs),
        'cited_keys':sorted(set(cites)),'uncited_bib_keys':sorted(set(keys)-set(cites)),
        'compilation':log_result,
        'source_sha256':{name:hashlib.sha256(text.encode()).hexdigest() for name,text in texts.items()}}
print(json.dumps(result,indent=2,ensure_ascii=False))
raise SystemExit(bool(errors))
