// Read-only source audit. This does not run Lean, Lake or any downloaded code.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const auditRoot = '/Users/kasifa/Documents/Math/tmp/wechat-openai-ns-20260909/formal-audit';
const root = path.join(auditRoot, 'snapshot');
const commitId = '8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538';
const commit = JSON.parse(fs.readFileSync(path.join(auditRoot, 'commit.json'), 'utf8'));
const tree = JSON.parse(fs.readFileSync(path.join(auditRoot, 'tree.json'), 'utf8'));
const digest = (data, algorithm = 'sha256') => crypto.createHash(algorithm).update(data).digest('hex');
const gitObject = (type, data) => digest(Buffer.concat([Buffer.from(`${type} ${data.length}\0`), data]), 'sha1');
if (commit.sha !== commitId || tree.truncated) throw Error('Unbound or truncated metadata');
const entries = new Map(tree.tree.map(x => [x.path, x]));

// Reconstruct every tree object from its immediate children and Git sort order.
const children = new Map();
for (const e of tree.tree) {
  const parent = path.posix.dirname(e.path);
  const key = parent === '.' ? '' : parent;
  if (!children.has(key)) children.set(key, []);
  children.get(key).push(e);
}
const checkTree = dir => {
  const list = children.get(dir) || [];
  const sortKey = e => Buffer.from(path.posix.basename(e.path) + (e.type === 'tree' ? '/' : ''));
  list.sort((a, b) => Buffer.compare(sortKey(a), sortKey(b)));
  const payload = Buffer.concat(list.map(e => {
    const sha = e.type === 'tree' ? checkTree(e.path) : e.sha;
    if (sha !== e.sha) throw Error(`Tree mismatch: ${e.path}`);
    return Buffer.concat([Buffer.from(`${e.mode.replace(/^0+/, '')} ${path.posix.basename(e.path)}\0`), Buffer.from(sha, 'hex')]);
  }));
  return gitObject('tree', payload);
};
const rootTree = checkTree('');
if (rootTree !== commit.commit.tree.sha) throw Error('Root tree mismatch');

const checked = new Map();
function readBound(relative) {
  if (checked.has(relative)) return checked.get(relative).text;
  const e = entries.get(relative), file = path.join(root, relative);
  if (!e || e.type !== 'blob' || fs.lstatSync(file).isSymbolicLink()) throw Error(`Invalid source: ${relative}`);
  const bytes = fs.readFileSync(file);
  if (gitObject('blob', bytes) !== e.sha || bytes.length !== e.size) throw Error(`Blob mismatch: ${relative}`);
  const value = { path: relative, git_blob: e.sha, sha256: digest(bytes), bytes: bytes.length, text: bytes.toString('utf8') };
  checked.set(relative, value);
  return value.text;
}

// Lexical comment removal, preserving newlines. Not a Lean parser or elaborator.
function removeComments(s) {
  let out = '', depth = 0, line = false, quoted = false;
  for (let i = 0; i < s.length; i++) {
    const pair = s.slice(i, i + 2), c = s[i];
    if (line) { if (c === '\n') { line = false; out += c; } else out += ' '; continue; }
    if (depth) {
      if (pair === '/-') { depth++; out += '  '; i++; }
      else if (pair === '-/') { depth--; out += '  '; i++; }
      else out += c === '\n' ? '\n' : ' ';
      continue;
    }
    if (quoted) {
      if (c === '\\') { out += '  '; i++; }
      else { if (c === '"') quoted = false; out += c === '\n' ? '\n' : ' '; }
      continue;
    }
    if (pair === '--') { line = true; out += '  '; i++; }
    else if (pair === '/-') { depth = 1; out += '  '; i++; }
    else if (c === '"') { quoted = true; out += ' '; }
    else out += c;
  }
  if (depth || quoted) throw Error('Unterminated comment/string');
  return out;
}

const visited = new Set(), external = new Set(), forbidden = [], pending = ['NavierStokes.ComparatorSolution'];
let totalLines = 0, totalBytes = 0;
while (pending.length) {
  const mod = pending.pop();
  if (visited.has(mod)) continue;
  visited.add(mod);
  const relative = mod.replaceAll('.', '/') + '.lean';
  const text = readBound(relative), code = removeComments(text);
  totalBytes += Buffer.byteLength(text);
  totalLines += text.split('\n').length - (text.endsWith('\n') ? 1 : 0);
  for (const m of code.matchAll(/^\s*(?:(?:public|meta)\s+)*import\s+([^\n]+)/gm)) {
    for (const dep of m[1].trim().split(/\s+/)) {
      if (!/^(?:NavierStokes|Mathlib)(?:\.[A-Za-z0-9_]+)*$/.test(dep)) throw Error(`Unclassified import: ${dep}`);
      if (dep.startsWith('Mathlib')) external.add(dep); else pending.push(dep);
    }
  }
  for (const m of code.matchAll(/\b(?:sorry|sorryAx|admit|axiom|unsafe|native_decide|run_tac|run_cmd)\b|#(?:eval|exec)|@\[(?:extern|implemented_by)/g)) {
    forbidden.push({ path: relative, token: m[0], line: code.slice(0, m.index).split('\n').length });
  }
}
const closureDigest = digest([...visited].sort().map(m => `${m}\0${entries.get(m.replaceAll('.', '/') + '.lean').sha}\n`).join(''));
const anchorNames = ['README.md', 'formalization.yaml', 'NavierStokes.lean', 'NavierStokes/ComparatorSolution.lean', 'NavierStokes/ComparatorDefinitions.lean', 'NavierStokes/ComparatorR3Theorem.lean', 'NavierStokes/ComparatorTheorem.lean', 'ComparatorChallenges/NavierStokes.lean', 'ComparatorChallenges/NavierStokes.json', 'ComparatorChallenges/README.md', 'lakefile.toml', 'lake-manifest.json', 'lean-toolchain'];
for (const file of anchorNames) readBound(file);
const challengeCode = removeComments(readBound('ComparatorChallenges/NavierStokes.lean'));
const result = {
  schema: 1, status: 'STATIC_SOURCE_AUDIT_ONLY', commit: commitId, reconstructed_tree: rootTree,
  snapshot: root, checked_blob_count: checked.size,
  solution_local_modules: visited.size, solution_local_lines: totalLines, solution_local_bytes: totalBytes,
  closure_module_blob_sha256: closureDigest, external_mathlib_import_count: external.size,
  external_dependency_closure_checked: false, reference_imported_by_solution: false,
  selected_token_scan_hits: forbidden,
  challenge_sorry_lines: [...challengeCode.matchAll(/\bsorry\b/g)].map(m => challengeCode.slice(0, m.index).split('\n').length),
  anchors: anchorNames.map(f => { const { text, ...meta } = checked.get(f); return meta; }),
  limits: ['Explicit lexical imports only; not a Lean parser or elaborator.', 'No Mathlib/Lean transitive implementation audit.', 'No compilation, kernel axiom extraction, Comparator or nanoda run.', 'Absence of selected source tokens is not proof or security certification.'],
};
process.stdout.write(JSON.stringify(result, null, 2) + '\n');
