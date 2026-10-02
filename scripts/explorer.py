"""Render explorer.html: every NeurIPS 2026 paper with browsable tags.
Tags: research area (14, data/area_labels.json), sub-topic within the area (data/subtopic_labels.json),
keyword topic (regexes in scripts/topic_trends.py), presentation format and track (data/decisions.json),
this repo's interest categories (data/papers.json, data/opd_papers.json), and medical QA benchmarks used in experiments
(data/medqa_benchmark_papers.json, when present).
Needs data/raw/neurips2026_posters.json (scripts/fetch.sh) for titles, authors and abstracts."""
import json, re, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from topic_trends import T

A = json.load(open('data/raw/neurips2026_posters.json'))
AL = json.load(open('data/area_labels.json')); D = json.load(open('data/decisions.json'))
P = {p['id']: p['cats'] for p in json.load(open('data/papers.json'))}
if os.path.exists('data/opd_papers.json'):
    for p in json.load(open('data/opd_papers.json'))['papers']:
        P.setdefault(p['id'], []).append('opd')
ST = json.load(open('data/subtopic_labels.json'))
MB = {}
if os.path.exists('data/medqa_benchmark_papers.json'):
    MB = {r['id']: r['benchmarks_norm'] for r in json.load(open('data/medqa_benchmark_papers.json'))['papers'] if r['used_in_experiments']}
pid = lambda x: x['virtualsite_url'].rsplit('/', 1)[-1]

KO = {'A': 'LLM 추론·학습·RL 후처리', 'B': 'LLM 에이전트·도구·검색', 'C': '정렬·안전·해석', 'D': '효율 모델·시스템',
      'E': '멀티모달·비전-언어', 'F': '생성 모델', 'G': '컴퓨터 비전·3D', 'H': '강화학습·로보틱스', 'I': '학습 이론·최적화',
      'J': '확률·인과·통계', 'K': '의료·헬스케어', 'L': '과학·생물', 'M': '데이터셋·벤치마크', 'N': '기타 ML (그래프·시계열 등)'}
CATS = {'medical_qa': 'Medical QA', 'medical_rag': 'Medical RAG', 'medical_agent': 'Medical Agent', 'medical_llm': 'Medical LLM / VLM', 'rag': 'RAG', 'opd': 'On-policy·Self-distillation'}
topics = list(T); trx = [re.compile(v, re.I) for v in T.values()]
sub_vocab = []  # [area code, name]
sub_index = {}
for code in KO:
    for name in ST['vocab'][code]:
        sub_index[(code, name)] = len(sub_vocab); sub_vocab.append([code, name])
bench_vocab = sorted({b for v in MB.values() for b in v})
FMT = ['Oral', 'Spotlight', 'Poster', 'Accept', None]; TRK = ['Main', 'Evaluations & Datasets', 'Position', 'Journal', None]


def authors(s):
    names = [re.sub(r'\s*\(.*?\)\s*', '', a).strip() for a in re.split(r',\s*(?![^()]*\))', s)]
    names = [n for n in names if n]
    return ', '.join(names[:4]) + (f' 외 {len(names) - 4}명' if len(names) > 4 else '')


rows = []
for x in A:
    i = pid(x); text = x['name'] + ' ' + x['abstract']; d = D.get(i, {})
    code = AL['labels']['2026'][i]
    ab = ' '.join(x['abstract'].split())
    rows.append([i, ' '.join(x['name'].replace('$', '').split()), authors(x['speakers/authors']), ab[:420] + ('…' if len(ab) > 420 else ''),
                 FMT.index(d.get('decision')), TRK.index(d.get('track')), code,
                 [sub_index[(code, t)] for t in ST['labels'][i]], [k for k, r in enumerate(trx) if r.search(text)],
                 [list(CATS).index(c) for c in P.get(i, [])], [bench_vocab.index(b) for b in MB.get(i, [])]])
data = dict(rows=rows, areas=KO, subs=sub_vocab, topics=topics, cats=list(CATS.values()), fmts=['Oral', 'Spotlight', 'Poster', 'Accept (Position)', '정보 없음'],
            trks=['Main', 'Evaluations & Datasets', 'Position', 'Journal', '정보 없음'], benches=bench_vocab)
tpl = open('scripts/explorer_template.html').read()
open('explorer.html', 'w').write(tpl.replace('/*DATA*/null', json.dumps(data, ensure_ascii=False, separators=(',', ':'))))
print('explorer.html', len(rows), 'papers,', len(sub_vocab), 'sub-topics,', len(topics), 'keyword topics,', len(bench_vocab), 'benchmarks,',
      os.path.getsize('explorer.html') // 1024, 'KB')
