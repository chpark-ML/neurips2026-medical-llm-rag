"""Build one compact dossier per paper whose full text mentions a medical QA benchmark:
abstract + opening of the paper + merged windows around every benchmark mention + table captions
that name a benchmark. Writes dossiers/<id>.txt and dossiers/index.jsonl."""
import json, re, os, gzip, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scan import BRX, HERE, REPO

A = {x['virtualsite_url'].rsplit('/', 1)[-1]: x for x in json.load(open(REPO + '/data/raw/neurips2026_posters.json'))}
OUTD = os.path.join(HERE, 'dossiers'); os.makedirs(OUTD, exist_ok=True)
W, CAP = 1100, 11000
idx = []
last = {}
for fn in ('results.jsonl', 'results2.jsonl', 'results3.jsonl'):
    if os.path.exists(os.path.join(HERE, fn)):
        for line in open(os.path.join(HERE, fn)):
            r = json.loads(line); last[r['id']] = r
for r in last.values():
    if not r.get('hits'):
        continue
    text = re.sub(r'[ \t]+', ' ', gzip.open(os.path.join(HERE, 'text', r['id'] + '.txt.gz'), 'rt').read())
    flat = re.sub(r'\s*\n\s*', ' ', text)
    spans = sorted((max(0, m.start() - W), m.end() + W) for rx in BRX.values() for m in rx.finditer(flat))
    merged = []
    for s, e in spans:
        if merged and s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    body, used = [], 0
    for s, e in merged:
        if used >= CAP:
            break
        chunk = flat[s:min(e, s + CAP - used)]; body.append('…' + chunk + '…'); used += len(chunk)
    caps = [m.group(0)[:400] for m in re.finditer(r'Table \d+[:.][^.]{0,380}', flat) if any(rx.search(m.group(0)) for rx in BRX.values())][:8]
    d = (f"ID: {r['id']}\nTITLE: {A[r['id']]['name']}\nARXIV: {r['arxiv_id']}\nBENCHMARK MENTIONS (count): "
         + ', '.join(f"{k} ({v['count']})" for k, v in r['hits'].items())
         + f"\n\nABSTRACT:\n{A[r['id']]['abstract']}\n\nOPENING OF PAPER:\n{flat[:2500]}\n\nTABLE CAPTIONS NAMING A BENCHMARK:\n"
         + '\n'.join(caps) + '\n\nPASSAGES AROUND BENCHMARK MENTIONS:\n' + '\n\n'.join(body))
    open(os.path.join(OUTD, r['id'] + '.txt'), 'w').write(d)
    idx.append(dict(id=r['id'], chars=len(d), benches=list(r['hits'])))
with open(os.path.join(OUTD, 'index.jsonl'), 'w') as f:
    for x in idx:
        f.write(json.dumps(x) + '\n')
print(len(idx), 'dossiers; mean chars', sum(x['chars'] for x in idx) // max(1, len(idx)))
