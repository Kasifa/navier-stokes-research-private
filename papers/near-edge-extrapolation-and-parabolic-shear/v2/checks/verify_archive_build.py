#!/usr/bin/env python3
"""Rebuild exactly the compile payload from an extracted local ZIP, to XDV."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
import zipfile

ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('--engine',required=True)
p.add_argument('--reference-build',type=Path,required=True)
a=p.parse_args()
items=[ROOT/'main.tex',ROOT/'references.bib',ROOT/'main.bbl']
items+=sorted((ROOT/'sections').glob('*.tex'))
items+=[ROOT.parent/'v1/figures/heat-edge/figure.pdf']
d=Path(tempfile.mkdtemp(prefix='paper-edge-v2-source-build-'))
zpath=d/'source.zip'
with zipfile.ZipFile(zpath,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for f in items:z.write(f,str(f.relative_to(ROOT.parent)))
with zipfile.ZipFile(zpath) as z:
    assert z.testzip() is None
    z.extractall(d/'extract')
work=d/'extract/v2';build=work/'build';build.mkdir()
cmd=[a.engine,'--only-cached','--outfmt','xdv','--keep-logs','--keep-intermediates','--outdir',str(build),'main.tex']
r=subprocess.run(cmd,cwd=work,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
(ROOT/'logs/archive-build-command.log').write_text(r.stdout)
assert r.returncode==0,r.stdout
for f in items:assert f.read_bytes()==(d/'extract'/f.relative_to(ROOT.parent)).read_bytes()
log=(build/'main.log').read_text();blg=(build/'main.blg').read_text()
flags=re.findall(r'^.*(?:Overfull|Undefined control|Missing character|LaTeX Warning|Package .* Warning|^!).*$',log,re.M)
flags+=re.findall(r'^.*(?:Warning--|error message).*$' ,blg,re.M)
assert not flags,flags
same={name:(build/name).read_bytes()==(a.reference_build/name).read_bytes() for name in ['main.aux','main.bbl','main.xdv']}
assert same['main.aux'] and same['main.bbl'],same
assert not (build/'main.pdf').exists()
result={'status':'PASS','engine':subprocess.check_output([a.engine,'--version'],text=True).strip(),
        'output_format':'XDV; no reader PDF','sources_compared':len(items),'source_bytes_equal':True,
        'same_as_reference':same,'pages':int(re.search(r'Output written on main\.xdv \((\d+) pages',log).group(1)),
        'blocking_warnings':flags,'build_directory':str(build),'network_resources':'only-cached',
        'source_hashes':{str(f.relative_to(ROOT.parent)):hashlib.sha256(f.read_bytes()).hexdigest() for f in items},
        'boundary':'Local source rebuild, not a remote arXiv test or visual manuscript review'}
(ROOT/'audits/archive-build.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='source_hashes'}))
