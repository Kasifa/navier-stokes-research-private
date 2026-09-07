#!/usr/bin/env python3
"""Normalize the two-lane roadmap and CB.1-CB.25 browser-title numbering."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

from generate_note_index import INDEPENDENT_CHAPTERS


ROOT = Path(__file__).resolve().parents[1]
VERSION = "2.70"
RELEASE_ID = "Homepage-ClayB-Topology-Numbering-20260907"
CHECK_ONLY = "--check-only" in sys.argv[1:]


def set_version(value: str, *, refresh: bool = False) -> str:
    value = re.sub(r'data-site-version="\d+\.\d+"', f'data-site-version="{VERSION}"', value, count=1)
    value = re.sub(r'/i18n-en\.js\?v=\d+\.\d+', f'/i18n-en.js?v={VERSION}', value, count=1)
    if refresh:
        value = re.sub(r'/site-refresh\.js\?v=\d+\.\d+', f'/site-refresh.js?v={VERSION}', value, count=1)
    return value


def normalize_note(value: str, chapter: str) -> str:
    value = set_version(value)
    match = re.search(r'<title>(.*?)</title>', value, flags=re.DOTALL)
    if match is None:
        raise RuntimeError(f"missing title for {chapter}")
    title = re.sub(r'^CB\.\d+｜', '', match.group(1).strip())
    return value[:match.start(1)] + f"{chapter}｜{title}" + value[match.end(1):]


def update_metadata(path: Path) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["version" if path.name == "site-version.json" else "siteVersion"] = VERSION
    payload["publishedDate"] = "2026-09-07"
    payload["roadmapTopology"] = "R0_SOLID_CB_DASHED_NO_INTERLANE_EDGE"
    payload["independentChapterTitlePolicy"] = "CB.n_PREFIXED"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def validate() -> None:
    home = (ROOT / "public/research-review.html").read_text(encoding="utf-8")
    required_home = [
        'class="route-tree r0-route-tree"',
        'class="route-lane-divider"',
        'class="route-tree clay-b-route-tree"',
        '.route-legend-mark.independent',
        'R0 与 Clay-B 之间无连接边',
        'R0 与 Clay-B 之间没有实线或虚线继承边',
        'NO R0→CLAY-B EDGE · DASHED LINKS ONLY INSIDE CB.1–CB.25',
        'border-left-style: dashed',
        'Clay-B 独立路线停在 CB.25',
    ]
    for marker in required_home:
        if marker not in home:
            raise RuntimeError(f"homepage topology marker missing: {marker}")
    r0 = home.index('class="route-tree r0-route-tree"')
    divider = home.index('class="route-lane-divider"', r0)
    clay_b = home.index('class="route-tree clay-b-route-tree"', divider)
    if not r0 < divider < clay_b:
        raise RuntimeError("roadmap lane order drift")
    if home.count('class="route-overview independent-release-spotlight"') != 1:
        raise RuntimeError("homepage must retain exactly one independent spotlight")
    if '/notes/clay-b-frequency-activation-20260907.html' not in home:
        raise RuntimeError("latest independent spotlight drift")
    if f'data-site-version="{VERSION}"' not in home or f'/i18n-en.js?v={VERSION}' not in home:
        raise RuntimeError("homepage version drift")

    for slug, chapter in INDEPENDENT_CHAPTERS.items():
        note = (ROOT / f"public/notes/{slug}.html").read_text(encoding="utf-8")
        if not re.search(rf'<title>{re.escape(chapter)}｜[^<]+</title>', note):
            raise RuntimeError(f"browser-title chapter number missing: {slug}")
        if f'data-site-version="{VERSION}"' not in note or f'/i18n-en.js?v={VERSION}' not in note:
            raise RuntimeError(f"note version drift: {slug}")

    index = (ROOT / "public/notes/index.html").read_text(encoding="utf-8")
    for slug, chapter in INDEPENDENT_CHAPTERS.items():
        row = re.search(rf'<li class="note-entry independent-entry" data-note="{re.escape(slug)}">([\s\S]*?)</li>', index)
        if row is None or f'class="note-code">{chapter} ·' not in row.group(1):
            raise RuntimeError(f"index chapter number missing: {chapter}")
        if re.search(rf'<h3>{re.escape(chapter)}｜', row.group(1)):
            raise RuntimeError(f"index duplicates chapter prefix: {chapter}")

    if (ROOT / "VERSION").read_text(encoding="utf-8").strip() != VERSION:
        raise RuntimeError("VERSION drift")
    site = json.loads((ROOT / "public/site-version.json").read_text(encoding="utf-8"))
    manifest = json.loads((ROOT / "research/release-manifest.json").read_text(encoding="utf-8"))
    for payload in (site, manifest):
        if payload.get("version", payload.get("siteVersion")) != VERSION:
            raise RuntimeError("site metadata version drift")
        if payload.get("roadmapTopology") != "R0_SOLID_CB_DASHED_NO_INTERLANE_EDGE":
            raise RuntimeError("roadmap topology metadata drift")
        if payload.get("independentChapterTitlePolicy") != "CB.n_PREFIXED":
            raise RuntimeError("chapter-title policy metadata drift")
    if site.get("latestIndependentChapter") != "CB.25" or site.get("nextIndependentChapter") != "CB.26":
        raise RuntimeError("independent endpoint drift")


if not CHECK_ONLY:
    home_path = ROOT / "public/research-review.html"
    home = set_version(home_path.read_text(encoding="utf-8"), refresh=True)
    home = re.sub(r'<strong>v\d+\.\d+</strong>网页版本', f'<strong>v{VERSION}</strong>网页版本', home, count=1)
    home = re.sub(r'<strong>\d{4}-\d{2}-\d{2}</strong>最近修订', '<strong>2026-09-07</strong>最近修订', home, count=1)
    home = re.sub(r'(?<!上次)综述 v\d+\.\d+ · \d{4}-\d{2}-\d{2}', f'综述 v{VERSION} · 2026-09-07', home, count=1)
    home_path.write_text(home, encoding="utf-8")

    literature_path = ROOT / "public/literature-review.html"
    literature = set_version(literature_path.read_text(encoding="utf-8"))
    literature = re.sub(r'(?<!上次)文献综述 v\d+\.\d+ · \d{4}-\d{2}-\d{2}', f'文献综述 v{VERSION} · 2026-09-07', literature, count=1)
    literature_path.write_text(literature, encoding="utf-8")

    for slug, chapter in INDEPENDENT_CHAPTERS.items():
        path = ROOT / f"public/notes/{slug}.html"
        path.write_text(normalize_note(path.read_text(encoding="utf-8"), chapter), encoding="utf-8")

    (ROOT / "VERSION").write_text(VERSION + "\n", encoding="utf-8")
    update_metadata(ROOT / "public/site-version.json")
    update_metadata(ROOT / "research/release-manifest.json")
    subprocess.run([sys.executable, "scripts/generate_note_index.py"], cwd=ROOT, check=True)

validate()
print(json.dumps({
    "schemaVersion": "homepage-clay-b-topology-numbering-generation-v1",
    "releaseId": RELEASE_ID,
    "status": "PASS",
    "mode": "check-only" if CHECK_ONLY else "apply",
    "siteVersion": VERSION,
    "r0Lane": "SOLID",
    "interlaneEdge": "NONE",
    "clayBInternalLinks": "DASHED",
    "numberedChapters": len(INDEPENDENT_CHAPTERS),
    "newReaderPdf": "OMITTED",
}, ensure_ascii=False))
