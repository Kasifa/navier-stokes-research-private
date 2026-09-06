#!/usr/bin/env python3
"""Package only upload inputs, then build that ZIP without the workspace sources."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import zipfile
from pypdf import PdfReader
import pdfplumber

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'source'
p=argparse.ArgumentParser()
p.add_argument('--pdflatex',default='pdflatex')
p.add_argument('--pdftoppm',default='pdftoppm')
a=p.parse_args()
sha=lambda f:hashlib.sha256(Path(f).read_bytes()).hexdigest()
subprocess.run([os.sys.executable,str(ROOT/'checks/validate_submission.py')],check=True,capture_output=True,text=True)
files=sorted(f for f in SRC.rglob('*') if f.is_file())
manifest={'research_source_commit':'ee014e3d8d332282b6e708aaa73dec23ed275b69','submission_main':'main.tex','files':{str(f.relative_to(SRC)):{'bytes':f.stat().st_size,'sha256':sha(f)} for f in files}}
(ROOT/'source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
archive=ROOT/'output/heat-edge-arxiv-source.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for f in files:
        info=zipfile.ZipInfo(str(f.relative_to(SRC)),date_time=(2026,9,6,0,0,0))
        info.compress_type=zipfile.ZIP_DEFLATED
        info.external_attr=0o100644<<16
        z.writestr(info,f.read_bytes())
clean=Path(tempfile.mkdtemp(prefix='arxiv-extracted-',dir=ROOT/'tmp'))
with zipfile.ZipFile(archive) as z:
    assert set(z.namelist())==set(manifest['files'])
    assert z.testzip() is None
    for name in z.namelist():
        assert not Path(name).is_absolute() and '..' not in Path(name).parts
    z.extractall(clean)
for name,record in manifest['files'].items():
    assert sha(clean/name)==record['sha256']
bbl_before=sha(clean/'main.bbl')
for i in range(1,4):
    with (clean/f'rebuild-pass-{i}.log').open('w') as out:
        subprocess.run([a.pdflatex,'-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-recorder','main.tex'],cwd=clean,stdout=out,stderr=subprocess.STDOUT,check=True)
assert sha(clean/'main.bbl')==bbl_before
log=(clean/'main.log').read_text()
warnings=re.findall(r'^.*(?:Overfull|Undefined control|Missing character|LaTeX Warning|Package .* Warning|^!).*$',log,re.M)
allowed='Package epstopdf Warning: Shell escape feature is not enabled.'
assert all(w.strip()==allowed for w in warnings),warnings
outside=[]
texroot=Path(a.pdflatex).resolve().parents[2] if Path(a.pdflatex).is_absolute() else None
for line in (clean/'main.fls').read_text().splitlines():
    if not line.startswith('INPUT '):continue
    path=Path(line[6:]);path=(clean/path).resolve() if not path.is_absolute() else path.resolve()
    if path.is_relative_to(clean):continue
    if texroot and path.is_relative_to(texroot):continue
    outside.append(str(path))
assert not outside,outside
reference=ROOT/'tmp/build/main.pdf'; rebuilt=clean/'main.pdf'
r=PdfReader(reference);rr=PdfReader(rebuilt)
assert len(r.pages)==len(rr.pages)==25
assert [x.extract_text() for x in r.pages]==[x.extract_text() for x in rr.pages]
assert r.metadata.title==json.loads((ROOT/'metadata.json').read_text())['title']
assert not r.is_encrypted
texts=[page.extract_text() or '' for page in r.pages]
assert all(len(t.strip())>20 and '??' not in t for t in texts)
assert '0009-0002-5402-3374' in texts[0]
with pdfplumber.open(reference) as book:
    offpage=[(i+1,c['text']) for i,page in enumerate(book.pages) for c in page.chars if c['x0'] < -1 or c['x1'] > page.width+1 or c['top'] < -1 or c['bottom'] > page.height+1]
assert not offpage,offpage
fonts={}
for page in r.pages:
    for ref in page['/Resources'].get('/Font',{}).values():
        font=ref.get_object()
        for child in font.get('/DescendantFonts',[font]):
            child=child.get_object();desc=child.get('/FontDescriptor');desc=desc.get_object() if desc else {}
            name=str(child.get('/BaseFont',font.get('/BaseFont','unknown')))
            fonts[name]=any(k in desc for k in ('/FontFile','/FontFile2','/FontFile3')) or child.get('/Subtype')=='/Type3'
assert all(fonts.values()),fonts
names=r.trailer['/Root'].get('/Names',{})
if hasattr(names,'get_object'): names=names.get_object()
assert '/JavaScript' not in names
for page in r.pages:
    for ann in page.get('/Annots',[]):
        ann=ann.get_object();action=ann.get('/A',{})
        if hasattr(action,'get_object'):action=action.get_object()
        assert action.get('/S') not in ('/JavaScript','/Launch')
render=clean/'render';render.mkdir()
subprocess.run([a.pdftoppm,'-r','105','-png',str(rebuilt),str(render/'page')],check=True,capture_output=True)
images=sorted(render.glob('page-*.png'));assert len(images)==25
assert all(f.read_bytes()==(ROOT/'tmp/final-render'/f.name).read_bytes() for f in images)
target=ROOT/'output/Heat-evolved-Chebyshev-edges-arxiv.pdf'
shutil.copy2(reference,target)
report={'status':'PASS','source_archive':archive.name,'source_archive_sha256':sha(archive),'source_files':len(files),'source_manifest_sha256':sha(ROOT/'source-manifest.json'),'pdf':target.name,'pdf_sha256':sha(target),'pdf_bytes':target.stat().st_size,'pages':25,'fonts_embedded':len(fonts),'no_blank_pages':True,'no_unresolved_reference_markers':True,'off_page_characters':offpage,'javascript_absent':True,'only_standard_tex_and_extracted_inputs':not outside,'used_supplied_bbl_without_bibtex':True,'page_text_identical':True,'all_25_page_renders_byte_identical':True,'allowed_engine_notice':warnings,'pdflatex':subprocess.check_output([a.pdflatex,'--version'],text=True).splitlines()[0],'texlive_scope':'Local TeX Live 2025 final repository; not arXiv 2025-08-03 exact snapshot','clean_build_directory':str(clean),'arxiv_upload_or_server_verification':False}
(ROOT/'audits/archive-build.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
