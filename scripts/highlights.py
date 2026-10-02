"""Highlight (Oral + Spotlight) analysis.
Inputs: data/raw/neurips2026_posters.json, data/decisions.json (scripts/decisions.py),
data/highlight_labels.json (area + Korean summary per highlight, LLM-labeled), data/papers.json.
Outputs: data/highlights.json, data/highlight_topics.json."""
import json, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from topic_trends import T

A = json.load(open('data/raw/neurips2026_posters.json'))
D = json.load(open('data/decisions.json'))
L = {x['id']: x for x in json.load(open('data/highlight_labels.json'))}
P = {p['id']: p for p in json.load(open('data/papers.json'))}

pid = lambda x: x['virtualsite_url'].rsplit('/', 1)[-1]
known = [x for x in A if D.get(pid(x), {}).get('decision') in ('Oral', 'Spotlight', 'Poster')]
is_hl = lambda x: D[pid(x)]['decision'] in ('Oral', 'Spotlight')
hl = [x for x in known if is_hl(x)]
missing = [pid(x) for x in hl if pid(x) not in L]
if missing:
    sys.exit(f'highlight_labels.json lacks {len(missing)} highlights, e.g. {missing[:3]}')

out = []
for x in hl:
    i = pid(x); d = D[i]; p = P.get(i)
    out.append(dict(id=i, title=x['name'], authors=x['speakers/authors'], url=x['virtualsite_url'], openreview=d['openreview'],
                    decision=d['decision'], track=d['track'], area=L[i]['area'], summary_ko=L[i]['summary_ko'],
                    in_scope=p['cats'] if p else []))
out.sort(key=lambda r: (r['decision'] != 'Oral', r['area'], r['title'].lower()))
json.dump(out, open('data/highlights.json', 'w'), ensure_ascii=False, indent=1)

base = len(hl) / len(known)
rows = []
for k, rx in T.items():
    r = re.compile(rx, re.I)
    m = [x for x in known if r.search(x['name'] + ' ' + x['abstract'])]
    h = sum(is_hl(x) for x in m)
    rows.append(dict(topic=k, n=len(m), highlights=h, rate=round(h / len(m) * 100, 2) if m else None,
                     lift=round(h / len(m) / base, 2) if m else None))
cats = []
for c in ['medical_qa', 'medical_rag', 'medical_agent', 'medical_llm', 'rag']:
    m = [x for x in known if c in P.get(pid(x), {}).get('cats', [])]
    h = sum(is_hl(x) for x in m)
    cats.append(dict(cat=c, n=len(m), highlights=h, rate=round(h / len(m) * 100, 2) if m else None))
json.dump(dict(n_known=len(known), n_highlight=len(hl), n_oral=sum(D[pid(x)]['decision'] == 'Oral' for x in hl),
               base_rate=round(base * 100, 2), topics=rows, categories=cats),
          open('data/highlight_topics.json', 'w'), ensure_ascii=False, indent=1)
print(f'{len(hl)} highlights / {len(known)} papers with a decision = {base*100:.2f}%')
for r in sorted([r for r in rows if r['n'] >= 40], key=lambda r: -r['lift'])[:12]:
    print(f"  {r['topic'][:45]:45} n={r['n']:4} hl={r['highlights']:3} {r['rate']}% lift x{r['lift']}")
print(cats)
