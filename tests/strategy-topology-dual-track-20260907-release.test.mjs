import './research-results-launch-20260907-release.test.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
const root=new URL('../',import.meta.url),get=p=>readFile(new URL(p,root),'utf8');
test('shared strategy preserves historical anchors, links, counts and approved results',async()=>{
 const home=await get('public/research-review.html');
 const base=JSON.parse(await get('research/site-maintenance/strategy-topology-dual-track-20260907/baseline.json'));
 const ids=[...home.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
 assert.equal(ids.length,new Set(ids).size);for(const id of base.ids)assert.ok(ids.includes(id),id);
 const hrefs=[...home.matchAll(/href="([^"]+)"/g)].map(m=>m[1]);for(const href of base.hrefs)assert.ok(hrefs.includes(href),href);
 const history=home.slice(home.indexOf('<section class="route-overview" id="route-map"'),home.indexOf('<div class="page-shell">'));
 assert.equal((history.match(/class="tree-row(?:[ "])/g)||[]).length,32);
 assert.equal((history.match(/<details\b/g)||[]).length,8);
 assert.equal((home.match(/class="strategy-direction"/g)||[]).length,2);
 assert.equal((home.match(/class="strategy-execution">方向已设立 · 研究暂停/g)||[]).length,2);
 for(const key of ['任意允许光滑初值','一个固定光滑初值','尚无公开冻结成果','候选不表示已启动','灰色点线只表示历史顺序','R0 与 CB 之间不添加依赖边'])assert.ok(home.includes(key),key);
 assert.equal((home.match(/id="frontier-results"/g)||[]).length,1);
 assert.equal((home.match(/class="route-overview independent-release-spotlight"/g)||[]).length,1);
});
test('four-step controls are accessible, deep-link aware and print-safe',async()=>{
 const css=await get('public/roadmap-collapse.css'),js=await get('public/roadmap-collapse.js'),strategy=await get('public/strategy-topology.css');
 for(const marker of ['Math.min(4, steps.length)','aria-expanded','aria-controls','hashchange','pageshow','beforeprint','afterprint','parent.open = true'])assert.ok(js.includes(marker),marker);
 assert.ok(css.includes('.route-fold-continuation'));assert.ok(css.includes('@media print'));assert.ok(css.includes('.tree-path:has(a)'));
 assert.doesNotMatch(css,/tree-node\s*>\s*p\s*~\s*p/);
 assert.ok(strategy.includes('border-left: 1px dotted var(--muted)'));
 const site=JSON.parse(await get('public/site-version.json'));assert.equal(site.roadmapPreviewSteps,4);assert.equal(site.researchExecutionState,'BOTH_DIRECTIONS_PAUSED');
});
