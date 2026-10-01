import json,re,collections
STOP=set('a an the of for and in on with via to from by is are as at its into towards toward beyond under over using through without when what how why do does can we our is it be not your more less than via vs one all new'.split())
def grams(D):
    c=collections.Counter()
    for x in D:
        w=[t for t in re.findall(r"[a-z][a-z0-9\-]+",x['name'].lower())]
        s=set()
        for n in (1,2,3):
            for i in range(len(w)-n+1):
                g=w[i:i+n]
                if g[0] in STOP or g[-1] in STOP: continue
                s.add(' '.join(g))
        c.update(s)
    return c
a26=json.load(open('data/raw/neurips2026_posters.json')); a25=json.load(open('data/raw/neurips2025_posters.json'))
c26=grams(a26); c25=grams(a25); N26=len(a26); N25=len(a25)
rows=[]
for g,n in c26.items():
    if n<15: continue
    p26=n/N26; p25=(c25.get(g,0)+1)/N25
    rows.append((p26/p25,g,n,c25.get(g,0)))
rows.sort(reverse=True)
out=[dict(term=g,n2026=n,n2025=m,ratio=round(r,2)) for r,g,n,m in rows[:80]]
for o in out[:80]: print(f"{o['term']:35} 25:{o['n2025']:4} 26:{o['n2026']:4} x{o['ratio']}")
top=[dict(term=g,n2026=n) for g,n in c26.most_common(400) if ' ' in g][:40]
print('--- top bigram+ 2026'); print(', '.join(f"{t['term']}({t['n2026']})" for t in top))
json.dump(dict(rising=out,top=top),open('data/title_terms.json','w'),indent=1)
