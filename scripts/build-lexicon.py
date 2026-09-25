#!/usr/bin/env python3
"""Builds lexicon/us.json.gz and lexicon/gb.json.gz from misaki's gold and
silver pronunciation lists (hexgrad/misaki, Apache-2.0) at a pinned commit.
Reproducible: gzip with mtime 0, sorted keys, no whitespace."""
import gzip, io, json, sys, urllib.request
COMMIT = 'fba1236595f2d2bf21d414ba6e57d25256afada3'
BASE = f'https://raw.githubusercontent.com/hexgrad/misaki/{COMMIT}/misaki/data/'
for accent in ('us', 'gb'):
    data = {k[0]: json.load(urllib.request.urlopen(f'{BASE}{accent}_{k}.json')) for k in ('gold', 'silver')}
    raw = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
    buf = io.BytesIO()
    with gzip.GzipFile(fileobj=buf, mode='wb', compresslevel=9, mtime=0, filename='') as g:
        g.write(raw)
    open(f'lexicon/{accent}.json.gz', 'wb').write(buf.getvalue())
    print(accent, len(raw), len(buf.getvalue()))
