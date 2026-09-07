#!/usr/bin/env python3
"""Version the approved strategy maintenance; leave scientific artifacts intact."""
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
VERSION='2.72';ID='strategy-topology-dual-track-20260907';CHECK='--check-only' in sys.argv
def dump(path,obj):path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
if not CHECK:
    for relative in ['public/research-review.html','public/literature-review.html','public/notes/index.html','public/notes/clay-b-frequency-activation-20260907.html']:
        path=ROOT/relative;s=path.read_text()
        s=re.sub(r'data-site-version="\d+\.\d+"',f'data-site-version="{VERSION}"',s,count=1)
        s=re.sub(r'/(i18n-en|site-refresh)\.js\?v=\d+\.\d+',lambda m:f'/{m[1]}.js?v={VERSION}',s)
        s=re.sub(r'<strong>v\d+\.\d+</strong>网页版本',f'<strong>v{VERSION}</strong>网页版本',s,count=1)
        s=s.replace('综述 v2.71 · 2026-09-07','综述 v2.72 · 2026-09-07').replace('研究笔记总索引 · v2.71 · 2026-09-07','研究笔记总索引 · v2.72 · 2026-09-07')
        path.write_text(s)
    (ROOT/'VERSION').write_text(VERSION+'\n')
    for relative in ['public/site-version.json','research/release-manifest.json']:
        path=ROOT/relative;data=json.loads(path.read_text())
        data['version' if path.name=='site-version.json' else 'siteVersion']=VERSION
        data.update(roadmapTopology='DUAL_OBJECTIVE_GROUPS_SHARED_DOTTED_HISTORY_NO_INTERLANE_DEPENDENCY',roadmapPreviewSteps=4,researchExecutionState='BOTH_DIRECTIONS_PAUSED')
        if path.name=='release-manifest.json':
            if data['latestPublication']['releaseId']!=ID:data['latestFrontierPublication']=data['latestPublication']
            data['latestPublication']={'schemaVersion':'independent-research-publication-v1','kind':'site-maintenance','releaseId':ID,'displayReleaseId':'StrategyTopology-DualTrack-20260907','html':'public/research-review.html','gate':f'tests/{ID}-gate.test.mjs','publicationTest':f'tests/{ID}-release.test.mjs','translationScript':f'scripts/add-{ID}-translations.mjs','pdfGenerated':False,'advancesCanonicalR0Series':False,'recapRequired':False,'simulationRequired':False,'researchResumed':False,'preservesFrontierResults':True}
        dump(path,data)
home=(ROOT/'public/research-review.html').read_text()
for marker in ['id="strategy-overview"','id="strategy-forward"','id="strategy-reverse"','/roadmap-collapse.js','/roadmap-collapse.css','id="frontier-results"']:
    assert marker in home,marker
assert home.count('class="route-overview independent-release-spotlight"')==1
assert 'strategy-topology-translations.js' not in home,'Use the central translation bundle only'
assert (ROOT/'VERSION').read_text().strip()==VERSION
site=json.loads((ROOT/'public/site-version.json').read_text())
assert (site['latestRelease'],site['latestIndependentChapter'],site['frontierResultCount'])==('R0.76L','CB.25',2)
assert site['researchExecutionState']=='BOTH_DIRECTIONS_PAUSED'
print(json.dumps({'status':'PASS','release':ID,'mode':'check' if CHECK else 'apply','newPdf':False,'researchResumed':False}))
