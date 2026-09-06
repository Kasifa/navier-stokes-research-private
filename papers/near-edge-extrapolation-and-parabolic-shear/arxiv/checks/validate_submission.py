#!/usr/bin/env python3
"""Check submission closure, metadata and preservation of the frozen mathematics."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'source'
V2=ROOT.parent/'v2'
errors=[]
files=[Path('main.tex')]+sorted(p.relative_to(SRC) for p in (SRC/'sections').glob('*.tex'))
texts={str(p):(SRC/p).read_text() for p in files}
body='\n'.join(texts.values())
labels=re.findall(r'\\label\{([^}]+)\}',body)
refs=re.findall(r'\\(?:ref|eqref|pageref)\{([^}]+)\}',body)
cites=[x.strip() for group in re.findall(r'\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}',body) for x in group.split(',')]
keys=re.findall(r'@\w+\s*\{\s*([^,]+),',(SRC/'references.bib').read_text())
errors += ['duplicate label '+k for k,n in Counter(labels).items() if n!=1]
errors += ['missing reference '+k for k in set(refs)-set(labels)]
errors += ['missing citation '+k for k in set(cites)-set(keys)]
errors += ['uncited bibliography key '+k for k in set(keys)-set(cites)]
for name,t in texts.items():
    stack=[]
    for event,env in re.findall(r'\\(begin|end)\{([^}]+)\}',t):
        if event=='begin': stack.append(env)
        elif not stack or stack.pop()!=env: errors.append('environment mismatch '+name)
    if stack: errors.append('unclosed environment '+name)
    for raw in re.findall(r'\\(?:input|include)\{([^}]+)\}',t):
        target=SRC/(raw if Path(raw).suffix else raw+'.tex')
        if not target.is_file() or not target.resolve().is_relative_to(SRC): errors.append('input not closed '+raw)
    for raw in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',t):
        target=SRC/raw
        if not target.is_file() or not target.resolve().is_relative_to(SRC): errors.append('image not closed '+raw)
    if re.search(r'(?i)(TODO|FIXME|/Users/|/private/tmp/|source audit|research notes|first version|second version|No new reader)',t):
        errors.append('draft or local-history marker '+name)

# Prose and bibliography edits may not silently modify the mathematical core.
pattern=r'\\begin\{(theorem|lemma|proposition|corollary|definition|proof)\}(.*?)\\end\{\1\}'
core_count=0
display_count=0
core_hashes={}
for name,t in texts.items():
    old=(V2/name).read_text()
    a=re.findall(pattern,old,re.S);b=re.findall(pattern,t,re.S)
    if a!=b: errors.append('mathematical statement or proof changed '+name)
    core_count+=len(a)
    # Equation environments and bracket displays are preserved independently.
    pat=r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}(.*?)\\end\{\1\}|\\\[(.*?)\\\]'
    da=re.findall(pat,old,re.S);db=re.findall(pat,t,re.S)
    if da!=db: errors.append('displayed mathematics changed '+name)
    display_count+=len(da)
    core_hashes[name]=hashlib.sha256(json.dumps(b).encode()).hexdigest()

m=json.loads((ROOT/'metadata.json').read_text())
abstract=' '.join(re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}',texts['main.tex'],re.S).group(1).split()).replace("Erd\\'elyi",'Erdelyi')
if abstract!=m['abstract']: errors.append('abstract metadata differs from manuscript')
for k in ('title','authors','abstract','comments'):
    if not m[k].isascii(): errors.append('non-ASCII metadata '+k)
if len(abstract)>1920: errors.append('abstract longer than 1920 characters')
if any(m[k] for k in ('journal_ref','doi','report_no')): errors.append('unearned publication field')
if m['license_selection'] is not None: errors.append('license selected without author decision')
if 'PENDING' in m['comments']: errors.append('page count unresolved')
if ';' in m['msc_class']: errors.append('MSC must use comma separators')
form=(ROOT/'metadata.txt').read_text()
for label,key in [('Title','title'),('Authors','authors'),('Abstract','abstract'),('Comments','comments'),('MSC-class','msc_class')]:
    if label+':\n'+m[key] not in form: errors.append('paste-ready metadata differs: '+key)
if not (SRC/'main.bbl').is_file(): errors.append('missing main.bbl')
else:
    bblkeys=re.findall(r'\\bibitem(?:\[[\s\S]*?\])?\{([^}]+)\}',(SRC/'main.bbl').read_text())
    if set(bblkeys)!=set(cites): errors.append('BBL citation keys differ')
for p in SRC.rglob('*'):
    if not p.is_file(): continue
    rel=p.relative_to(SRC)
    if p.is_symlink() or not re.fullmatch(r'[A-Za-z0-9_./-]+',str(rel)): errors.append('unsafe filename '+str(rel))
    if any(x.startswith('.') or x=='__pycache__' for x in rel.parts): errors.append('hidden/generated file '+str(rel))
    if p.suffix in {'.aux','.log','.out','.xdv','.pyc','.fls','.blg'}: errors.append('build residue '+str(rel))
    if p.name=='main.pdf': errors.append('main PDF included in source upload')
if (SRC/'figures/heat-edge.pdf').read_bytes()!=(ROOT.parent/'v1/figures/heat-edge/figure.pdf').read_bytes():
    errors.append('scientific figure differs from frozen source')
old_plot=(ROOT.parent/'v1/figures/heat-edge/plot.py').read_text()
old_doc='difference.  The separate render.cjs converts the SVG to PDF and 600 dpi PNG.'
expected_plot=old_plot.replace(old_doc,"difference. The paper's vector PDF is supplied in figures/heat-edge.pdf.")
if (SRC/'anc/heat-edge/plot.py').read_text()!=expected_plot: errors.append('plot changes exceed documentation fix')
result={'status':'PASS' if not errors else 'FAIL','errors':errors,'tex_files':len(files),'labels':len(labels),'references':len(refs),'cited_keys':sorted(set(cites)),'core_statement_and_proof_blocks_unchanged':core_count,'display_math_blocks_unchanged':display_count,'core_block_sha256':core_hashes,'abstract_characters':len(abstract),'metadata_matches_manuscript':abstract==m['abstract'],'source_files':len([p for p in SRC.rglob('*') if p.is_file()])}
(ROOT/'audits/submission-validation.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='core_block_sha256'},indent=2))
sys.exit(bool(errors))
