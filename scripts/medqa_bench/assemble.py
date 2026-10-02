"""Combine scan results + extractions into REPO/data/medqa_benchmark_papers.json."""
import json, re, os, glob, collections, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scan import BRX, BENCH, HERE, REPO
from verify import main as verify

# Manual decisions on cases the extractors flagged as borderline (see conversation log):
OVERRIDE_FALSE = {
    '138960': 'HealthBench 점수를 모델 보고서에서 모아 분석할 뿐 모델을 직접 돌리지 않음',
}
A = {x['virtualsite_url'].rsplit('/', 1)[-1]: x for x in json.load(open(REPO + '/data/raw/neurips2026_posters.json'))}
D = json.load(open(REPO + '/data/decisions.json'))
P = {p['id']: p['cats'] for p in json.load(open(REPO + '/data/papers.json'))}
last = {}
for fn in ('results.jsonl', 'results2.jsonl', 'results3.jsonl'):
    if os.path.exists(os.path.join(HERE, fn)):
        for l in open(os.path.join(HERE, fn)):
            r = json.loads(l); last[r['id']] = r
ext = {r['id']: r for r in verify(sorted(glob.glob(os.path.join(HERE, 'extract', 'b_*.jsonl'))))}


def canon(names):
    out = []
    for n in names:
        hit = [k for k, rx in BRX.items() if rx.search(n)]
        if 'AgentClinic' in hit:  # AgentClinic-MedQA is the AgentClinic environment built on MedQA cases
            hit = ['AgentClinic']
        out += hit if hit else [n.strip()]
    return sorted(set(out))


papers = []
for i, e in ext.items():
    used = bool(e['used_in_experiments']) and i not in OVERRIDE_FALSE
    x = A[i]
    papers.append(dict(id=i, title=' '.join(x['name'].replace('$', '').split()), url=x['virtualsite_url'],
                       arxiv_id=last.get(i, {}).get('arxiv_id'), decision=D.get(i, {}).get('decision'), in_216=P.get(i, []),
                       used_in_experiments=used, override=OVERRIDE_FALSE.get(i), evidence='fulltext',
                       benchmarks=e.get('benchmarks', []) if used else [], benchmarks_norm=canon(e.get('benchmarks', [])) if used else [],
                       other_datasets=e.get('other_datasets', []) if used else [], models=e.get('models', []) if used else [],
                       training=e.get('training'), problem_ko=e.get('problem_ko'), method_ko=e.get('method_ko'), role=e.get('role') if used else None,
                       own_benchmark=e.get('own_benchmark', ''),
                       results=[r for r in e.get('results', []) if r.get('verified')] if used else []))
# papers we could not read in full but whose abstract names a benchmark
abstract_only = []
for i, r in last.items():
    if r.get('status') != 'fulltext' and r.get('abstract_hits'):
        x = A[i]
        abstract_only.append(dict(id=i, title=' '.join(x['name'].replace('$', '').split()), url=x['virtualsite_url'], benchmarks_in_abstract=r['abstract_hits']))
st = collections.Counter(r['status'] for r in last.values())
cov = dict(pool=len(last), fulltext=st['fulltext'], not_found=st['no_arxiv_match'], failed=st['download_failed'] + st['pdf_error'],
           fulltext_with_mention=sum(1 for r in last.values() if r.get('hits')), judged=len(ext),
           used=sum(p['used_in_experiments'] for p in papers), abstract_only=len(abstract_only),
           results_verified=sum(len(p['results']) for p in papers))
json.dump(dict(coverage=cov, benchmarks_searched=list(BENCH), papers=sorted(papers, key=lambda p: (not p['used_in_experiments'], p['title'].lower())),
               abstract_only=abstract_only), open(REPO + '/data/medqa_benchmark_papers.json', 'w'), ensure_ascii=False, indent=1)
print(cov)
print(collections.Counter(b for p in papers for b in p['benchmarks_norm']).most_common(20))
