#!/usr/bin/env python3
"""Publish two approved complete readers from reviewed, immutable inputs."""
import hashlib,json,re,shutil,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/'research/results/research-results-launch-20260907'
VERSION='2.71'
CHECK='--check-only' in sys.argv
MANIFEST=json.loads((INPUT/'artifact-manifest.json').read_text())
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def dump(path,data):path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
def version(value):
    value=re.sub(r'data-site-version="\d+\.\d+"',f'data-site-version="{VERSION}"',value,count=1)
    value=re.sub(r'/(i18n-en|site-refresh)\.js\?v=\d+\.\d+',lambda m:f'/{m[1]}.js?v={VERSION}',value)
    value=re.sub(r'<strong>v\d+\.\d+</strong>网页版本',f'<strong>v{VERSION}</strong>网页版本',value,count=1)
    value=value.replace('综述 v2.70 · 2026-09-07','综述 v2.71 · 2026-09-07').replace('研究笔记总索引 · v2.70 · 2026-09-07','研究笔记总索引 · v2.71 · 2026-09-07')
    return value

for item in MANIFEST['files']:
    source=INPUT/'reader-assets'/Path(item['path']).relative_to('public')
    assert sha(source)==item['sha256'],item['path']+' editorial input changed'
    target=ROOT/item['path']
    if not CHECK:target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
    assert sha(target)==item['sha256'],item['path']+' public bytes changed'

if not CHECK:
    path=ROOT/'public/research-review.html';home=path.read_text()
    assert 'roadmap-collapse.' not in home,'Queued roadmap work must remain isolated'
    if 'id="frontier-results"' not in home:
        marker='<section class="route-overview independent-release-spotlight"'
        assert home.count(marker)==1
        home=home.replace(marker,(INPUT/'homepage-section.html').read_text()+marker,1)
    if '<a href="/results/">前沿成果</a>' not in home:
        home=home.replace('<a href="#route-map">研究路线</a>','<a href="#route-map">研究路线</a>\n        <a href="/results/">前沿成果</a>',1)
    if '/* frontier-results-layout */' not in home:
        home=home.replace('</head>','<style>/* frontier-results-layout */\n.frontier-results-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:32px;margin-top:26px}.frontier-results-grid article{border-top:1px solid var(--line);padding-top:20px;min-width:0}.frontier-results-grid h3{font-size:22px;line-height:1.4;margin:10px 0 16px}.frontier-results-grid p{font-size:16px;line-height:1.75;overflow-wrap:anywhere}@media(max-width:760px){.frontier-results-grid{grid-template-columns:1fr;gap:20px}}\n</style>\n</head>',1)
    path.write_text(version(home))
    for relative in ['public/literature-review.html','public/notes/index.html','public/notes/clay-b-frequency-activation-20260907.html']:
        path=ROOT/relative;path.write_text(version(path.read_text()))
    (ROOT/'VERSION').write_text(VERSION+'\n')
    path=ROOT/'public/site-version.json';site=json.loads(path.read_text());site.update(version=VERSION,frontierResultsIndex='/results/',frontierResultCount=2,frontierResultsPublication='ResearchResults-Launch-20260907',frontierReaderPdfPolicy='EXPLICIT_ENGLISH_PDF_FOR_APPROVED_PAPERS');dump(path,site)
    path=ROOT/'research/release-manifest.json';release=json.loads(path.read_text());release['siteVersion']=VERSION
    if release['latestPublication']['releaseId']!='research-results-launch-20260907':release['latestIndependentPublication']=release['latestPublication']
    release['latestPublication']={'schemaVersion':'independent-research-publication-v1','kind':'frontier-results-column','releaseId':'research-results-launch-20260907','displayReleaseId':'ResearchResults-Launch-20260907','html':'public/results/index.html','gate':'tests/research-results-launch-20260907-gate.test.mjs','publicationTest':'tests/research-results-launch-20260907-release.test.mjs','translationScript':'scripts/add-research-results-launch-20260907-translations.mjs','sourceCommits':MANIFEST['sourceBinding'],'approvedPaperCount':2,'pdfGenerated':False,'pdfPolicy':'COPY_VERIFIED_ENGLISH_PDFS_EXPLICIT_TWO_PAPER_EXCEPTION','advancesCanonicalR0Series':False,'recapRequired':False,'simulationRequired':False}
    release.update(frontierResultsIndex='/results/',frontierResultCount=2);dump(path,release)

home=(ROOT/'public/research-review.html').read_text()
assert home.count('id="frontier-results"')==1
assert home.count('class="route-overview independent-release-spotlight"')==1
assert 'roadmap-collapse.' not in home
assert all(p['title']['zh'] in home for p in MANIFEST['papers'])
assert (ROOT/'VERSION').read_text().strip()==VERSION
site=json.loads((ROOT/'public/site-version.json').read_text())
assert (site['latestRelease'],site['latestIndependentChapter'],site['frontierResultCount'])==('R0.76L','CB.25',2)
print(json.dumps({'release':'ResearchResults-Launch-20260907','mode':'check' if CHECK else 'apply','status':'PASS','approvedPapers':2,'filesBound':len(MANIFEST['files']),'pdfGeneration':False}))
