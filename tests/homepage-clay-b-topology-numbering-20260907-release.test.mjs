import test from "node:test";
import assert from "node:assert/strict";
import { access, readFile } from "node:fs/promises";
import { resolve } from "node:path";

const root = resolve(import.meta.dirname, "..");
const text = (path) => readFile(resolve(root, path), "utf8");
const chapters = [
  ["clay-b-two-scale-20260905", "CB.1"], ["clay-b-signed-scale-20260905", "CB.2"],
  ["clay-b-physical-adjoint-20260906", "CB.3"], ["clay-b-window-localisation-20260906", "CB.4"],
  ["clay-b-plateau-history-20260906", "CB.5"], ["clay-b-concentration-limits-20260906", "CB.6"],
  ["clay-b-pressure-geometry-20260906", "CB.7"], ["clay-b-pressure-quotient-20260906", "CB.8"],
  ["clay-b-pressure-work-window-20260906", "CB.9"], ["clay-b-bad-time-net-work-20260906", "CB.10"],
  ["clay-b-pressure-test-coupling-20260906", "CB.11"], ["clay-b-lagged-pressure-reduction-20260906", "CB.12"],
  ["clay-b-recent-source-screen-20260906", "CB.13"], ["clay-b-pressure-mechanism-screen-20260906", "CB.14"],
  ["clay-b-ancient-constant-screen-20260906", "CB.15"], ["clay-b-fixed-history-screen-20260906", "CB.16"],
  ["clay-b-euler-compactness-screen-20260906", "CB.17"], ["clay-b-energy-atom-cost-screen-20260906", "CB.18"],
  ["clay-b-common-adjoint-screen-20260906", "CB.19"], ["clay-b-adjoint-weak-trace-screen-20260906", "CB.20"],
  ["clay-b-convex-pressure-trace-20260906", "CB.21"], ["clay-b-same-parent-residual-20260906", "CB.22"],
  ["clay-b-signed-mixed-pressure-20260907", "CB.23"], ["clay-b-source-enstrophy-20260907", "CB.24"],
  ["clay-b-frequency-activation-20260907", "CB.25"],
];

test("roadmap has no R0-to-Clay-B edge and uses dashed links only inside Clay-B", async () => {
  const home = await text("public/research-review.html");
  const r0 = home.indexOf('class="route-tree r0-route-tree"');
  const boundary = home.indexOf('class="tree-row r0-public-boundary-row"', r0);
  const divider = home.indexOf('class="route-lane-divider"', boundary);
  const clay = home.indexOf('class="route-tree clay-b-route-tree"', divider);
  assert.ok(r0 < boundary && boundary < divider && divider < clay);
  assert.match(home, /\.route-legend-mark\.independent[\s\S]*?border-top: 2px dashed/);
  assert.match(home, /R0 与 Clay-B 之间没有实线或虚线继承边/);
  assert.match(home, /NO R0→CLAY-B EDGE · DASHED LINKS ONLY INSIDE CB\.1–CB\.25/);
  assert.match(home, /\.clay-b-route-tree \.tree-row::before[\s\S]*?border-left-style: dashed/);
  assert.equal((home.match(/class="route-overview independent-release-spotlight"/g) ?? []).length, 1);
  assert.ok(home.includes('/notes/clay-b-frequency-activation-20260907.html'));
});

test("all Clay-B browser titles and index rows use one CB.n scheme", async () => {
  const index = await text("public/notes/index.html");
  for (const [slug, chapter] of chapters) {
    const note = await text(`public/notes/${slug}.html`);
    assert.match(note, new RegExp(`<title>${chapter.replace('.', '\\.') }｜[^<]+</title>`));
    const row = index.match(new RegExp(`data-note="${slug}"([\\s\\S]*?)</li>`));
    assert.ok(row, slug);
    assert.ok(row[1].includes(`class="note-code">${chapter} ·`), chapter);
    assert.equal(row[1].includes(`<h3>${chapter}｜`), false, `duplicate ${chapter}`);
  }
});

test("maintenance release preserves endpoints and creates no new reader PDF", async () => {
  const [site, manifest] = await Promise.all([
    text("public/site-version.json").then(JSON.parse), text("research/release-manifest.json").then(JSON.parse),
  ]);
  assert.equal(site.version, "2.70");
  assert.equal(site.latestRelease, "R0.76L");
  assert.equal(site.latestIndependentChapter, "CB.25");
  assert.equal(site.roadmapTopology, "R0_SOLID_CB_DASHED_NO_INTERLANE_EDGE");
  assert.equal(site.independentChapterTitlePolicy, "CB.n_PREFIXED");
  assert.equal(manifest.siteVersion, "2.70");
  assert.equal(manifest.latestCompletedRelease, "r076l");
  for (const [slug, chapter] of chapters.slice(1)) {
    await assert.rejects(access(resolve(root, `public/notes/${slug}.pdf`)), undefined, chapter);
  }
  await access(resolve(root, "public/notes/clay-b-two-scale-20260905.pdf"));
});
