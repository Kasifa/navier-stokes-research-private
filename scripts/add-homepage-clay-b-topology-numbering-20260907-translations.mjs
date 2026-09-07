#!/usr/bin/env node

import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { readFile, writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { collectSiteStrings, containsChinese, extractProtectedTokens } from "./i18n-lib.mjs";

const root = resolve(import.meta.dirname, "..");
const publicRoot = resolve(root, "public");
const translationPath = resolve(root, "translations/en.json");
const bundlePath = resolve(publicRoot, "i18n-en.js");
const checkOnly = process.argv.includes("--check-only");
const prefix = "homepageclaybtopologynumbering20260907";

const local = new Map([
  ["我把已经完成的研究整理为两条路线。R0.1–R0.76L 是实线主序列；CB.1–CB.25 是相对独立的 Clay-B 路线，在单独泳道中仅以虚线表示内部章节顺序。两条路线之间不画任何连接边；它们研究同一个 PDE 问题，但这里不把策略转向表示成由 R0.76L 推出 Clay-B 的定理依赖。历史节点默认只显示阶段判断，最近公开笔记可直接打开原始记录。", "I organize the completed research into two routes. R0.1–R0.76L is the solid-line main sequence; CB.1–CB.25 is the relatively independent Clay-B route, with dashed links used only for its internal chapter order in a separate lane. No edge is drawn between the two routes. They study the same PDE problem, but the strategy change is not presented as a theorem-level implication from R0.76L to Clay-B. Historical nodes show only their stage judgments by default, and the latest public notes open directly."],
  ["虚线仅表示 Clay-B 内部章节顺序；R0 与 Clay-B 之间无连接边", "Dashed links show only the internal Clay-B chapter order; there is no edge between R0 and Clay-B"],
  ["这条路线与 R0 主序列共享三维 Navier–Stokes 的研究目标，但在此独立起线。R0 与 Clay-B 之间没有实线或虚线继承边；下方虚线只连接 Clay-B 内部已经发布的章节顺序。", "This route shares the three-dimensional Navier–Stokes research objective with the R0 main sequence, but starts independently here. There is no solid or dashed inheritance edge between R0 and Clay-B; the dashed links below connect only the published chapter order within Clay-B."],
  ["综述 v2.70 · 2026-09-07", "Review v2.70 · 2026-09-07"],
  ["文献综述 v2.70 · 2026-09-07", "Literature review v2.70 · 2026-09-07"],
  ["研究笔记总索引 · v2.70 · 2026-09-07", "Research-note master index · v2.70 · 2026-09-07"],
]);

function bundleTranslations(source) {
  const match = source.match(/Object\.freeze\((\{[\s\S]*\})\);\s*$/);
  assert.ok(match, "translation bundle format drift");
  return new Map(Object.entries(JSON.parse(match[1])));
}

function validateTranslation(source, en) {
  assert.ok(!containsChinese(en), "Chinese remains in translation: " + source);
  assert.deepEqual(extractProtectedTokens(en), extractProtectedTokens(source), "protected token drift: " + source);
}

process.chdir(root);
const [source, current, bundleSource] = await Promise.all([
  collectSiteStrings(publicRoot),
  readFile(translationPath, "utf8").then(JSON.parse),
  readFile(bundlePath, "utf8"),
]);
const legacy = bundleTranslations(bundleSource);
const rowPattern = new RegExp("^" + prefix + "\\d+$");

if (checkOnly) {
  const currentByZh = new Map(current.map((entry) => [entry.zh, entry]));
  assert.deepEqual(source.filter((entry) => !currentByZh.has(entry.zh)), [], "site still has untranslated Chinese strings");
  const rows = current.filter((entry) => rowPattern.test(entry.id));
  assert.ok(rows.length >= local.size, "topology translation inventory drift");
  for (const row of rows) validateTranslation(row.zh, row.en);
  const bundle = await readFile(bundlePath, "utf8");
  for (const marker of ["there is no edge between R0 and Clay-B", "CB.25 | Band activation at fixed energy"]) {
    assert.ok(bundle.includes(marker), "translation bundle drift: " + marker);
  }
} else {
  const base = current.filter((entry) => !rowPattern.test(entry.id));
  const currentByZh = new Map(base.map((entry) => [entry.zh, entry]));
  const missing = source.filter((entry) => !currentByZh.has(entry.zh));
  const additions = missing.map((entry, index) => {
    const en = local.get(entry.zh) ?? legacy.get(entry.zh);
    assert.equal(typeof en, "string", "missing local translation: " + entry.zh);
    validateTranslation(entry.zh, en);
    return { id: prefix + String(index + 1).padStart(3, "0"), ...entry, en };
  });
  assert.ok(additions.length >= local.size, "unexpectedly small translation delta");
  await writeFile(translationPath, JSON.stringify([...base, ...additions], null, 2) + "\n");
  const built = spawnSync(process.execPath, ["scripts/build-i18n.mjs", "translations/en.json"], { cwd: root, encoding: "utf8" });
  assert.equal(built.status, 0, built.stdout + "\n" + built.stderr);
}

process.stdout.write(JSON.stringify({
  release: "Homepage-ClayB-Topology-Numbering-20260907",
  translationPath: "LOCAL_DIRECT_NO_DGX",
  dgxUsed: false,
  applied: !checkOnly,
}, null, 2) + "\n");
