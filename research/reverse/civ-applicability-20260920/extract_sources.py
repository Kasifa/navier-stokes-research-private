"""Acquire two fixed primary HTML versions and retain their exact TeX alttext.

Bibliographic extraction only: no scientific computation or source verification.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.request import urlopen, Request
import datetime
import hashlib
import json


class Article(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.inside = False
        self.math = False
        self.ignored = None
        self.parts = []
        self.math_count = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'article' and 'ltx_document' in attrs.get('class', '').split():
            self.inside = True
        if not self.inside:
            return
        if tag in ('script', 'style'):
            self.ignored = tag
        if tag == 'math':
            assert not self.math
            assert attrs.get('alttext') is not None, 'Missing math alttext'
            self.parts.append(' $' + attrs['alttext'] + '$ ')
            self.math = True
            self.math_count += 1
        if tag in ('p', 'div', 'section', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'tr', 'br') and not self.math:
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag == 'math':
            self.math = False
        if tag == self.ignored:
            self.ignored = None
        if tag == 'article' and self.inside:
            self.inside = False
        if self.inside and not self.math and tag in ('p', 'div', 'section', 'li', 'tr'):
            self.parts.append('\n')

    def handle_data(self, text):
        if self.inside and not self.math and self.ignored is None:
            self.parts.append(text)


def record(path):
    raw = path.read_bytes()
    return {'path': str(path), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


base = Path('research/reverse/civ-applicability-20260920/sources')
base.mkdir(parents=True, exist_ok=True)
rows = []
for aid in ('2609.20803v1', '2609.20762v1'):
    url = 'https://arxiv.org/html/' + aid
    html = base / (aid + '.html')
    assert not html.exists(), 'Preserve existing source; do not silently redownload'
    with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=30) as response:
        raw = response.read()
    assert aid.encode() in raw
    html.write_bytes(raw)
    parser = Article()
    parser.feed(raw.decode('utf-8'))
    assert parser.math_count > 0 and not parser.math
    text = '\n'.join(' '.join(line.split()) for line in ''.join(parser.parts).splitlines() if line.strip()) + '\n'
    target = base / (aid + '.txt')
    target.write_text(text)
    rows.append({'arxiv': aid, 'url': url, 'acquired_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                 'html': record(html), 'text': {**record(target), 'lines': len(text.splitlines())},
                 'math_elements_preserved_as_TeX': parser.math_count})
manifest = {'scope': 'Primary source acquisition only, not mathematical verification',
            'extraction': 'Standard HTMLParser, full article.ltx_document; every math element replaced by exact alttext; article prose, proofs, appendices, references retained',
            'sources': rows}
(base / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(manifest, ensure_ascii=False))
