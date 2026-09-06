#!/usr/bin/env python3
"""Manifest and local archive only. No push, PDF conversion, or publication."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile

ROOT=Path(__file__).resolve().parents[1]
PAPER=ROOT.parent
REPO=ROOT.parents[2]
BASE='0a212f4e140e0c9875e740cb8ee23be32a5c05dd'
RELEASE='paper-heat-edge-v2-20260906'
MANIFEST=ROOT/'source-manifest.json'

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def git(*args):return subprocess.check_output(['git','-c','core.quotepath=false','-C',str(REPO),*args],text=True).strip()
def files():
    selected=[]
    for path in ROOT.rglob('*'):
        rel=path.relative_to(ROOT)
        if not path.is_file() or path==MANIFEST:continue
        if any(x in {'output','tmp','__pycache__'} for x in rel.parts) or path.suffix=='.pyc':continue
        selected.append(path)
    selected += [x for x in (PAPER/'v1/figures/heat-edge').iterdir() if x.is_file()]
    selected += [PAPER/'v1/checks/verify_algebra.py']
    return sorted(selected,key=lambda x:str(x.relative_to(PAPER)))

def inventory():
    return [{'path':str(p.relative_to(PAPER)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files()]

def verify():
    doc=json.loads(MANIFEST.read_text())
    if doc['files'] != inventory():raise SystemExit('FAIL: manifest and current file inventory differ')
    print(json.dumps({'status':'PASS','files':len(doc['files']),'manifest_sha256':sha(MANIFEST)}))
    return doc

def main():
    parser=argparse.ArgumentParser()
    mode=parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write-manifest',action='store_true')
    mode.add_argument('--verify-manifest',action='store_true')
    mode.add_argument('--freeze',action='store_true')
    a=parser.parse_args()
    if a.write_manifest:
        doc={'schema':'paper-research-freeze-source-v2','release_id':RELEASE,
             'source_baseline':BASE,'source_commit_binding':'output/release-receipt.json; produced after clean commit',
             'dependencies':[{'release':'near-edge-parabolic-v1','commit':BASE}],
             'files':inventory(),'self_exclusion':['v2/source-manifest.json','v2/output/','v2/tmp/'],
             'claim_boundary':{'proved':['quantitative uniform T and normalized U edge errors',
                 'profile criterion','fixed-data complete-interval first-kind shear realization',
                 'original-amplitude full-velocity rate, amplitude scaling and bounded-drift shape bound',
                 'abstract temporal N^(4/3) order witness'],
                 'literature':['near-edge Fourier scale','temporal upper inequality inputs','polynomial heat operation'],
                 'finite_computation':'Finite exact algebra and retained numerical figure; no continuum certification',
                 'open':['best error orders','arbitrary Jacobi parameters','matching general dynamic bounds','other bounded-drift profiles'],
                 'not_clay':True,'human_peer_review':False,'priority_verified':False},
             'figure_inventory':'v2/FIGURES.md','reader_pdf':'No new reader PDF; historical figure retained',
             'stage_review':'Yes: standalone manuscript repositioning and new theorem, without changing mainline roadmap',
             'publication':'Not performed; once-only return to fixed research task after freeze'}
        MANIFEST.write_text(json.dumps(doc,indent=2,ensure_ascii=False)+'\n')
        verify();return
    doc=verify()
    if a.verify_manifest:return
    if git('status','--porcelain'):
        raise SystemExit('FAIL: worktree contains uncommitted tracked or unignored files')
    commit=git('rev-parse','HEAD')
    subprocess.run(['git','-C',str(REPO),'merge-base','--is-ancestor',BASE,commit],check=True)
    changed=git('diff','--name-only',BASE,commit).splitlines()
    prefix=str(ROOT.relative_to(REPO))+'/'
    if any(not p.startswith(prefix) for p in changed):raise SystemExit('FAIL: change outside v2')
    out=ROOT/'output';out.mkdir(exist_ok=True)
    archive=out/(RELEASE+'-source.zip')
    payload=files()+[MANIFEST]
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for path in sorted(payload):
            name=str(path.relative_to(PAPER));info=zipfile.ZipInfo(name,date_time=(2026,9,6,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16
            z.writestr(info,path.read_bytes())
    with zipfile.ZipFile(archive) as z:
        assert len(z.namelist())==len(payload) and z.testzip() is None
        for path in payload:assert z.read(str(path.relative_to(PAPER)))==path.read_bytes()
    receipt={'release_id':RELEASE,'source_commit':commit,'branch':git('branch','--show-current'),
             'source_baseline':BASE,'worktree':str(REPO),'source_manifest_sha256':sha(MANIFEST),
             'archive':archive.name,'archive_sha256':sha(archive),'archive_files':len(payload),
             'status':'RESEARCH_COMPLETE_LOCAL_FROZEN','v1_changes':False,'push_or_publication':False,
             'reader_pdf_generated':False,'human_peer_review':False,
             'handoff_target':'019fb8c8-96a8-7320-bb59-3ab9e8b7e29e','handoff_policy':'once; registration by fixed research task'}
    (out/'release-receipt.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(receipt,ensure_ascii=False))

if __name__=='__main__':main()
