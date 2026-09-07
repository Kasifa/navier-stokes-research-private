import './clay-b-frequency-activation-20260907-release.test.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile,access,readdir} from 'node:fs/promises';
const root=new URL('../',import.meta.url);
const get=async p=>await readFile(new URL(p,root),'utf8');
const math=s=>[...s.matchAll(/<span class="math (?:inline|display)"[^>]*>([\s\S]*?)<\/span>/g)].map(x=>x[1]).sort();
test('both full bilingual readers preserve reviewed mathematics, labels, proofs and bibliography',async()=>{
 for(const [key,slug,displays,proofs,figures,bib] of [['heat-edge','heat-evolved-chebyshev-edges',139,18,1,10],['projected-lamb','projected-lamb-heat-packing',92,9,2,14]]) {
  const page=await get(`public/results/${slug}.html`);
  const contract=JSON.parse(await get(`research/results/research-results-launch-20260907/${key}-contract.json`));
  const ids=[...page.matchAll(/\bid="([^"]+)"/g)].map(x=>x[1]);assert.equal(new Set(ids).size,ids.length,'unique bilingual ids');
  for(const lang of ['zh','en']) {
   const main=page.match(new RegExp(`<main data-language="${lang}"[^>]*>([\\s\\S]*?)</main>`))[1];
   const fragment=await get(`research/results/research-results-launch-20260907/fragments/${key}.${lang}.html`);
   const abstract=await get(`research/results/research-results-launch-20260907/abstracts/${key}.${lang}.html`);
   assert.deepEqual(math(main),math(abstract+fragment),`${slug} ${lang} math unchanged`);
   assert.equal((main.match(/class="math display"/g)||[]).length,displays);
   assert.equal((main.match(/class="proof"/g)||[]).length,proofs);
   assert.equal((main.match(/<figure\b/g)||[]).length,figures);
   assert.equal((main.match(new RegExp(`<li id="${lang}-ref-`,'g'))||[]).length,bib);
   for(const label of contract.labels)assert.ok(ids.includes(lang+'-'+label),label);
   for(const ref of main.matchAll(/href="#([^"]+)"/g))assert.ok(ids.includes(ref[1]),ref[1]);
   for(const boundary of ['PROVED','FINITE','OPEN','NOT CLAY'])assert.ok(main.includes(boundary));
  }
  for(const ext of ['.pdf','-source.zip'])await access(new URL(`public/assets/papers/${slug}${ext}`,root));
  assert.doesNotMatch(page,/⟦display-|ZXQSEP|ZZNODE|暂无全文|coming soon/i);
 }
});
test('frontier index has exactly the approved two papers without changing historical counts',async()=>{
 const index=await get('public/results/index.html');const home=await get('public/research-review.html');const site=JSON.parse(await get('public/site-version.json'));
 assert.equal((index.match(/class="paper-card"/g)||[]).length,4);
 assert.equal((home.match(/id="frontier-results"/g)||[]).length,1);
 assert.ok(home.includes('href="/results/"'));assert.equal(site.frontierResultCount,2);
 assert.equal(site.latestRelease,'R0.76L');assert.equal(site.latestIndependentChapter,'CB.25');assert.equal(site.nextIndependentChapter,'CB.26');
 const notes=await readdir(new URL('public/notes/',root));assert.equal(notes.filter(x=>/^r0-[0-9a-z]+\.html$/.test(x)).length,266);assert.equal(notes.filter(x=>/^r0-[0-9a-z]+\.pdf$/.test(x)).length,223);
 assert.equal(site.newPdfPolicy,'NO_NEW_PDFS_FROM_CLAYB_SIGNED_SCALE_20260905');
 assert.doesNotMatch(home,/roadmap-collapse\./,'queued strategy changes cannot leak into this commit');
});
