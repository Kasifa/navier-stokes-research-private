import assert from 'node:assert/strict';
import {readFile,writeFile} from 'node:fs/promises';
import {spawnSync} from 'node:child_process';
import {resolve} from 'node:path';
import {collectSiteStrings,extractProtectedTokens,containsChinese} from './i18n-lib.mjs';
const root=resolve(import.meta.dirname,'..');
const current=JSON.parse(await readFile(resolve(root,'translations/en.json'),'utf8'));
const delta=JSON.parse(await readFile(resolve(root,'research/site-maintenance/strategy-topology-dual-track-20260907/translations.json'),'utf8'));
const source=await collectSiteStrings(resolve(root,'public'));
const map=new Map(current.map(x=>[x.zh,x]));
const missing=source.filter(x=>!map.has(x.zh));
if(process.argv.includes('--check-only'))assert.deepEqual(missing,[],'Untranslated site strings');
else {
 for(const [i,row] of missing.entries()) {
  const en=delta[row.zh];assert.equal(typeof en,'string','Missing direct translation: '+row.zh);
  assert.equal(containsChinese(en),false);assert.deepEqual(extractProtectedTokens(en),extractProtectedTokens(row.zh),row.zh);
  current.push({id:'strategytopologydualtrack20260907'+String(i+1).padStart(3,'0'),...row,en});
 }
 await writeFile(resolve(root,'translations/en.json'),JSON.stringify(current,null,2)+'\n');
 const result=spawnSync(process.execPath,['scripts/build-i18n.mjs','translations/en.json'],{cwd:root,encoding:'utf8'});assert.equal(result.status,0,result.stdout+result.stderr);
}
const bundle=await readFile(resolve(root,'public/i18n-en.js'),'utf8');
for(const key of ['Direction established','Research paused','CB Research Record','R0 Research Record'])assert.ok(bundle.includes(key),key);
console.log('PASS direct bilingual strategy and archive prose; no DGX or machine translation.');
