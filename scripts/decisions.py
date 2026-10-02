"""Attach Oral/Spotlight/Poster decisions and track to each poster.
neurips.cc's orals-posters JSON returns a different partial subset on different days
(2026-10-01: 5,547 papers, 2026-10-02: 5,896). Merging the snapshots gives better coverage;
they agree on every paper present in both. Writes data/decisions.json keyed by poster id."""
import json, re, glob
n = lambda s: re.sub(r'\W+', '', s.lower())
U = {}
for f in sorted(glob.glob('data/raw/neurips2026_orals_posters*.json')):
    for x in json.load(open(f))['results']:
        U.setdefault(n(x['name']), x)
TR = {'Conference': 'Main', 'Evaluations_and_Datasets_Track': 'Evaluations & Datasets', 'Position_Paper_Track': 'Position'}
DEC = {'Accept (oral)': 'Oral', 'Accept (spotlight)': 'Spotlight', 'Accept (poster)': 'Poster', 'Accept': 'Accept'}
out = {}
for x in json.load(open('data/raw/neurips2026_posters.json')):
    m = U.get(n(x['name']))
    if not m:
        continue
    src = m.get('sourceurl') or ''
    track = next((v for k, v in TR.items() if src.endswith('/' + k)), 'Journal' if 'journal' in src else None)
    out[x['virtualsite_url'].rsplit('/', 1)[-1]] = dict(decision=DEC.get(m['decision']), track=track, openreview=m.get('paper_url') or None)
json.dump(out, open('data/decisions.json', 'w'), separators=(',', ':'))
from collections import Counter
print(len(out), 'of', len(json.load(open('data/raw/neurips2026_posters.json'))), Counter(v['decision'] for v in out.values()))
# refresh papers.json
P = json.load(open('data/papers.json'))
for p in P:
    d = out.get(p['id'])
    p['decision'], p['track'], p['openreview'] = (d['decision'], d['track'], d['openreview']) if d else (None, None, None)
json.dump(P, open('data/papers.json', 'w'), ensure_ascii=False, indent=1)
print('papers.json: decision known for', sum(p['decision'] is not None for p in P), 'of', len(P))
