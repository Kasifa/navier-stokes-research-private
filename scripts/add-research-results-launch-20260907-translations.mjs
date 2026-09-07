import assert from 'node:assert/strict';
import {readFile,writeFile} from 'node:fs/promises';
import {spawnSync} from 'node:child_process';
import {resolve} from 'node:path';
import {collectSiteStrings,extractProtectedTokens} from './i18n-lib.mjs';
const root=resolve(import.meta.dirname,'..');
const input=resolve(root,'research/results/research-results-launch-20260907');
const current=JSON.parse(await readFile(resolve(root,'translations/en.json'),'utf8'));
const delta=JSON.parse(await readFile(resolve(input,'translations.json'),'utf8'));
const all=await collectSiteStrings(resolve(root,'public'));
const map=new Map(current.map(x=>[x.zh,x]));
const missing=all.filter(x=>!map.has(x.zh));
if(process.argv.includes('--check-only')) assert.equal(missing.length,0,JSON.stringify(missing));
else {
  for(const [i,row] of missing.entries()) {
    const en=delta[row.zh];assert.equal(typeof en,'string','Missing translation: '+row.zh);
    assert.deepEqual(extractProtectedTokens(en),extractProtectedTokens(row.zh));
    current.push({id:'researchresultslaunch20260907'+String(i+1).padStart(3,'0'),...row,en});
  }
  await writeFile(resolve(root,'translations/en.json'),JSON.stringify(current,null,2)+'\n');
  const result=spawnSync(process.execPath,['scripts/build-i18n.mjs','translations/en.json'],{cwd:root,encoding:'utf8'});assert.equal(result.status,0,result.stdout+result.stderr);
}
for(const lang of ['zh','en']) for(const slug of ['heat-evolved-chebyshev-edges','projected-lamb-heat-packing']) {
  const page=await readFile(resolve(root,'public/results',slug+'.html'),'utf8');
  assert.ok(page.includes(`main data-language="${lang}"`));
  assert.ok(page.includes(lang==='zh'?'摘要':'Abstract'));
}
console.log('PASS: complete independently reviewed bilingual readers and homepage translations; no DGX or machine translation call.');
