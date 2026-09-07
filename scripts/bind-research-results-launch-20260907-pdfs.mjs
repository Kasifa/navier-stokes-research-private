import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {resolve} from 'node:path';
const root=resolve(import.meta.dirname,'..');
const data=JSON.parse(await readFile(resolve(root,'research/results/research-results-launch-20260907/artifact-manifest.json'),'utf8'));
let count=0;
for(const file of data.files) {
  const bytes=await readFile(resolve(root,file.path));
  assert.equal(createHash('sha256').update(bytes).digest('hex'),file.sha256,file.path);
  if(file.path.endsWith('.pdf')) {assert.equal(bytes.subarray(0,5).toString(),'%PDF-');count++;}
}
assert.equal(count,5);
console.log('PASS: two verified English reader PDFs and three frozen scientific figure PDFs bound unchanged; no PDF authoring.');
