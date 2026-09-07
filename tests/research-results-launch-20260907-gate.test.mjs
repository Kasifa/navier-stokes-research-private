// Preserve the latest scientific gate. This column packages existing papers;
// the publication checks do not claim a new proof or scientific certificate.
import './clay-b-frequency-activation-20260907-gate.test.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const root=new URL('../',import.meta.url);
test('approved two-paper assets are exact and preserve their source identities',async()=>{
 const m=JSON.parse(await readFile(new URL('research/results/research-results-launch-20260907/artifact-manifest.json',root),'utf8'));
 assert.equal(m.papers.length,2);
 assert.equal(m.sourceBinding['heat-edge'],'9ff88b3455894a2ac27bbcec8ecd669435a58a4f');
 assert.equal(m.sourceBinding['projected-lamb'],'f799b7cd619f71a585c6d59d8c83cad1a61480b5');
 for(const f of m.files) {const bytes=await readFile(new URL(f.path,root));assert.equal(createHash('sha256').update(bytes).digest('hex'),f.sha256,f.path);assert.equal(bytes.length,f.bytes);}
 for(const lang of ['en','zh']) {const a=JSON.parse(await readFile(new URL(`research/results/research-results-launch-20260907/audits/math-audit-${lang}.json`,root),'utf8'));assert.equal(a.displays,92);assert.equal(a.body_inline,227);assert.deepEqual(a.mismatches,[]);}
});
