"""Render README.md, HIGHLIGHTS.md, data/papers.csv and interests.html from data/*.json and scripts/insights.py.
Usage (from repo root): python3 scripts/build.py"""
import json, re, os, sys, html, collections, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from insights import TREND_NOTES, NEXT_TOPICS, MEDQA_IDEAS, HIGHLIGHT_NOTES, MED_HIGHLIGHTS

P = json.load(open('data/papers.json'))
T = json.load(open('data/topic_trends.json'))
H = json.load(open('data/highlights.json'))
HT = json.load(open('data/highlight_topics.json'))
AS = json.load(open('data/area_stats.json'))

CATS = [
    ('medical_qa', 'Medical QA', '의료·임상·생의학 질의응답, medical VQA, 시험형 QA, 임상 추론 QA'),
    ('medical_rag', 'Medical RAG', '의료 도메인의 검색증강 생성·지식 검색'),
    ('medical_agent', 'Medical Agent', '의료 환경의 LLM/VLM 에이전트, 멀티에이전트 진단, 임상 워크플로 벤치마크'),
    ('medical_llm', 'Medical LLM / VLM', '의료용 언어·비전-언어 모델의 학습·정렬·안전·평가·리포트 생성'),
    ('rag', 'RAG', '모든 도메인의 RAG: 방법, GraphRAG, 멀티모달 RAG, 보안, 벤치마크, 효율, agentic search'),
]
CAT_NAME = {k: n for k, n, _ in CATS}
SUBS = [
    ('agentic-search', 'Agentic search / Deep research'), ('method', 'RAG 방법론'), ('graph-rag', 'GraphRAG / KG'),
    ('multimodal-rag', 'Multimodal RAG'), ('robustness-security', '강건성·보안·프라이버시'),
    ('benchmark-eval', '벤치마크·평가'), ('efficiency', '효율 (KV cache·압축·지연)'), ('other', '기타 (비텍스트 생성 등)'),
]
SUB_NAME = dict(SUBS)


def clean(t):
    t = t.replace('$\\chi$', 'χ').replace('$\\alpha$', 'α')
    return re.sub(r'\s+', ' ', t.replace('$', '')).strip()


def find(sub):
    m = [p for p in P if sub in p['title']]
    if len(m) != 1:
        sys.exit(f'insights.py reference {sub!r} matched {len(m)} papers')
    return m[0]


def short(p):
    head = clean(p['title']).split(':')[0]
    clash = sum(clean(q['title']).split(':')[0] == head for q in P) > 1
    return clean(p['title'])[:60] if clash else head


def by_cat(c):
    return [p for p in P if c in p['cats']]


counts = {k: len(by_cat(k)) for k, _, _ in CATS}
n_med = sum(any(c.startswith('medical') for c in p['cats']) for p in P)
sub_counts = collections.Counter(p['rag_sub'] for p in P if p['rag_sub'])
rows = T['rows']
rising = sorted([r for r in rows if r['growth']], key=lambda r: -r['growth'])
n_dec = sum(p['decision'] is not None for p in P)
hl_scope = [h for h in H if h['in_scope']]
hl_med = []
for sub in MED_HIGHLIGHTS:
    m = [h for h in H if h['title'].startswith(sub)]
    if len(m) != 1:
        sys.exit(f'MED_HIGHLIGHTS reference {sub!r} matched {len(m)} highlights')
    hl_med.append(m[0])
AREAS = [a for a, _ in collections.Counter(h['area'] for h in H).most_common()]
AREA_KO = {
    'LLM reasoning & RL post-training': 'LLM 추론·RL 후처리', 'LLM agents & tool use': 'LLM 에이전트·도구 사용',
    'Alignment, safety & interpretability': '정렬·안전·해석', 'Efficient models & systems': '효율 모델·시스템',
    'Multimodal & vision-language': '멀티모달·비전-언어', 'Generative models (diffusion, flow, image/video)': '생성 모델 (diffusion·flow·영상)',
    'Computer vision & 3D': '컴퓨터 비전·3D', 'Reinforcement learning, robotics & embodied': '강화학습·로보틱스·embodied',
    'Learning theory & optimization': '학습 이론·최적화', 'Probabilistic, causal & statistical ML': '확률·인과·통계 ML',
    'Science, health & biology': '과학·의료·생물', 'Datasets, benchmarks & evaluation': '데이터셋·벤치마크·평가',
    'Other ML (graphs, time series, federated, etc.)': '기타 ML (그래프·시계열·연합학습 등)',
}
lift_rows = sorted([r for r in HT['topics'] if r['n'] >= 40], key=lambda r: -r['lift'])


def hl_table(lst, with_area=False):
    out = ['| # | 제목 | 한 줄 요약 | 형식 |' + (' 분야 |' if with_area else ''), '|---:|---|---|---|' + ('---|' if with_area else '')]
    for i, h in enumerate(lst, 1):
        t = clean(h['title']).replace('|', '\\|')
        out.append(f"| {i} | [{t}]({h['url']}) | {h['summary_ko'].replace('|', '/')} | {h['decision']} |" + (f" {AREA_KO[h['area']]} |" if with_area else ''))
    return '\n'.join(out)

# ---------------------------------------------------------------- README.md
md = []
w = md.append
w('# NeurIPS 2026 관심 분야 상세 리포트\n')
w('> 요약과 웹 페이지 링크는 [README](README.md)에 있다. 이 문서는 표와 목록을 모두 담은 상세판이다.\n')
w(f'NeurIPS 2026 채택 논문 **{T["N2026"]:,}편** 중, 아래 다섯 주제 중 하나 이상을 핵심 기여로 다룬 논문 **{len(P)}편**을 모았다. '
  '키워드 트렌드 분석(2025 대비)과 다음 연구 주제 제안, Medical QA 연구 아이디어를 함께 정리했다.\n')
w('> **웹 페이지 (휴대폰에서도 열림)** — 네 페이지는 서로 독립적이다.\n>\n> - [관심 분야 리포트](https://chpark-ml.github.io/neurips2026-medical-llm-rag/interests.html): 학회 전체 → 분야 → 트렌드 → 의료·RAG 순서의 분석, 관심 분야 216편, on-policy·self-distillation 74편, 의료 QA 벤치마크 실험 논문, 하이라이트, 연구 제안\n> - [NeurIPS 2026 논문 탐색기](https://chpark-ml.github.io/neurips2026-medical-llm-rag/explorer.html): 학회 전체 9,094편을 분야·세부 주제(212개)·키워드·발표 형식·트랙으로 걸러 보기 (관심 분야와 무관한 전체 보기)\n> - [Medical QA 연구 지도](https://chpark-ml.github.io/neurips2026-medical-llm-rag/medical_qa.html): Medical QA 논문 30편을 큰 갈래 5개 → 세부 갈래 11개로 나눈 연구 흐름\n> - [On-policy·Self-distillation 연구 지도](https://chpark-ml.github.io/neurips2026-medical-llm-rag/opsd.html): 74편을 큰 갈래 6개 → 세부 갈래 20개로 나눈 연구 흐름\n>\n> NeurIPS 2026 전체의 Oral·Spotlight 논문은 [`HIGHLIGHTS.md`](HIGHLIGHTS.md)에 분야별로 정리했다.\n')
w('## 한눈에 보기\n')
w('| 분류 | 편수 | 기준 |\n|---|---:|---|')
for k, n, desc in CATS:
    w(f'| {n} | {counts[k]} | {desc} |')
w(f'| **의료 관련 전체 (위 4개 의료 분류의 합집합)** | **{n_med}** | |')
w(f'| **전체 (중복 제거)** | **{len(P)}** | 한 논문이 여러 분류에 속할 수 있어 분류별 합계보다 작다 |\n')
w('RAG 122편의 세부 유형:\n')
w('| RAG 유형 | 편수 |\n|---|---:|')
for k, n in SUBS:
    w(f'| {n} | {sub_counts[k]} |')
w('')
w('## 어떻게 모았나 (그리고 한계)\n')
w(f'1. **원천 데이터**: neurips.cc 공식 다운로드(`/Downloads/2026`)의 포스터 목록 {T["N2026"]:,}편(제목·저자·초록). 비교용 2025년 목록 {T["N2025"]:,}편. 2026 목록은 Main·Evaluations & Datasets·Position·Journal 트랙을 포함한다.')
w('2. **1차 후보 추출**: 의료 용어 × LLM/에이전트 용어, 또는 retrieval/RAG/search 용어가 제목·초록에 있는 논문 1,103편 (`scripts/candidates.py`).')
w('3. **분류**: 후보 1,103편 전부의 제목·초록을 LLM(Claude)이 읽고 핵심 기여 기준으로 분류. 지나가듯 언급하거나 RAG를 baseline으로만 쓴 논문은 제외. 이어 제외된 논문 중 신호가 강한 167편을 초록 전문으로 다시 읽는 2차 재검토로 17편을 추가했고, 경계 사례는 직접 읽어 2편을 더하고 1편을 뺐다.')
w(f'4. **발표 형식(Oral/Spotlight/Poster)과 트랙**은 neurips.cc의 orals-posters JSON에서 붙였다. 이 JSON은 받을 때마다 일부만 담겨 있어(2026-10-01 5,547편, 10-02 5,896편) 두 스냅샷을 합쳤고, 그래도 이 목록 {len(P)}편 중 {len(P) - n_dec}편은 발표 형식을 알 수 없다(`scripts/decisions.py`).\n')
w('5. **분야 분포**: 2026년 9,094편과 2025년 5,860편 전부에 LLM이 제목만 보고 14개 분야 중 하나를 배정했다(`scripts/area_prompt.md`, 약 1,000편씩 14묶음). 묶음마다 분야 비중이 조금씩 달라서, 그 흩어짐으로 오차를 어림하고 오차의 두 배보다 큰 변화만 증가·감소로 본다(`scripts/areas.py`). 검증으로, 위 의료 논문 100편 중 87편이 의료·헬스케어로 배정됐다.')
w('6. **키워드 정규식**: MCP, LLM 불확실성·calibration, LLM 에이전트, activation steering은 다른 뜻까지 잡던 정규식을 좁혔다(예: `calibrat` 단독 → LLM 용어가 함께 있어야 매칭).\n')
w('**한계**: 분류는 사람 검수가 아닌 LLM 판독이라 경계 사례(예: 단백질 언어모델 + retrieval, 의료가 여러 응용 중 하나인 논문)는 기준에 따라 달라질 수 있다. 순수 검색·임베딩 논문(생성 없음)과 LLM이 없는 의료 영상·EHR 예측 모델은 의도적으로 제외했다. 한 줄 요약은 초록 기반 자동 요약이다.\n')

def paper_table(lst):
    out = ['| # | 제목 | 한 줄 요약 | 분류 | 발표 |', '|---:|---|---|---|---|']
    for i, p in enumerate(sorted(lst, key=lambda p: clean(p['title']).lower()), 1):
        t = clean(p['title']).replace('|', '\\|')
        tags = ', '.join(CAT_NAME[c] for c in p['cats'])
        dec = p['decision'] or ''
        if dec in ('Oral', 'Spotlight'):
            dec = f'**{dec}**'
        out.append(f"| {i} | [{t}]({p['url']}) | {p['summary_ko'].replace('|', '/')} | {tags} | {dec} |")
    return '\n'.join(out)

KO_AREA = {'A': 'LLM 추론·학습·RL 후처리', 'B': 'LLM 에이전트·도구·검색', 'C': '정렬·안전·해석', 'D': '효율 모델·시스템', 'E': '멀티모달·비전-언어',
           'F': '생성 모델', 'G': '컴퓨터 비전·3D', 'H': '강화학습·로보틱스', 'I': '학습 이론·최적화', 'J': '확률·인과·통계',
           'K': '의료·헬스케어', 'L': '과학·생물', 'M': '데이터셋·벤치마크', 'N': '기타 ML (그래프·시계열 등)'}
w('## 학회 전체는 어떻게 나뉘나 (14개 분야)\n')
w(f"모든 논문의 분야 비중(전체 중 %)을 2025년과 비교했다. '변화'는 오차(±2 표준오차)보다 큰 경우에만 숫자로 적었다. 하이라이트 비율은 발표 형식을 아는 {AS['known']:,}편 기준이고, 기준선은 {AS['base_rate']}%다. 더 자세한 그림은 [관심 분야 리포트](https://chpark-ml.github.io/neurips2026-medical-llm-rag/interests.html#l1).\n")
w('| 분야 | 2025 비중 | 2026 비중 (편수) | 변화 | 하이라이트 비율 (95% 구간) |\n|---|---:|---:|---:|---:|')
for a in AS['areas']:
    ch = f"{a['diff_pp']:+.1f}%p" if a['clear_change'] else '비슷'
    w(f"| {KO_AREA[a['code']]} | {a['share2025']}% | {a['share2026']}% ({a['n2026']:,}) | {ch} | {a['hl_rate']}% ({a['hl_ci'][0]}–{a['hl_ci'][1]}%) |")
w('')
w('- 확실히 커진 분야는 LLM 에이전트·도구·검색(비중 ×2.3)이고, 의료·헬스케어도 작게 늘었다. 컴퓨터 비전·3D, 학습 이론, 기타 ML은 편수는 늘었지만 비중은 줄었다.')
w('- 하이라이트 비율은 과학·생물과 학습 이론이 기준선보다 높고, 의료·헬스케어가 가장 낮다. "데이터셋·벤치마크" 분야는 묶음 사이 편차가 커서(2.3–10.5%) 해석하지 않는다.\n')
RF = json.load(open('data/research_flows.json'))
w('## 관심 분야별 연구 흐름\n')
w('각 분야의 논문을 읽고 여러 논문이 함께 움직이는 방향과 그 방향이 붙잡은 문제를 한 줄씩 적었다. 괄호의 편수는 그 흐름에 주로 속하는 논문 수를 판독으로 어림한 값이고, 링크는 대표 논문이다. RAG와 의료 세 분야는 위 216편 목록, LLM 에이전트와 LLM은 학회 전체에서 해당 분야로 배정된 논문이 대상이다.\n')
for key in ['rag', 'agent', 'llm', 'medical_qa', 'medical_llm', 'medical_agent']:
    t = RF[key]
    w(f"### {t['title']} ({t['n']}편 · {t['scope']})\n")
    w(f"{t['summary_ko']}\n")
    for f in t['flows']:
        refs_ = ', '.join(f"[{r['short']}]({r['url']})" for r in f['refs'])
        w(f"- {f['line_ko']} (약 {f['n_approx']}편) — {refs_}")
    rest = t['n'] - sum(f['n_approx'] for f in t['flows'])
    if rest > 0:
        w(f"- 나머지 약 {rest}편은 위 흐름 어디에도 주로 속하지 않는 작은 주제들이다.")
    w('')
MB_PATH = 'data/medqa_benchmark_papers.json'
MB = json.load(open(MB_PATH)) if os.path.exists(MB_PATH) else None
# Papers whose main target is medical QA: extractor role 'main', plus EHRNote-ChatQA (a clinical QA benchmark paper the
# extractor marked 'analysis' only because it uses EHRNoteQA as a single-turn reference).
MAIN_EXTRA = {'139551'}
mb_main = [p for p in MB['papers'] if p['used_in_experiments'] and (p['role'] == 'main' or p['id'] in MAIN_EXTRA)] if MB else []
fmt_res = lambda r: f"{r['benchmark']}: {r['value']}" + (f" (vs {r['compared_to']} {r['compared_value']})" if r.get('compared_value') else '')
if MB:
    cov = MB['coverage']; used = [p for p in MB['papers'] if p['used_in_experiments']]; cited = [p for p in MB['papers'] if not p['used_in_experiments']]
    esc_md = lambda t: (t or '').replace('|', '/')
    w(f"## Medical QA 벤치마크로 실험한 논문 ({len(used)}편)\n")
    w(f"MedQA·MedMCQA·MedXpertQA·PubMedQA·VQA-RAD·SLAKE 같은 **기존 공개 의료 QA 벤치마크로 직접 실험한** NeurIPS 2026 논문이다. 논문이 새로 만든 벤치마크만 쓴 경우는 넣지 않았다(아래 표의 '자체 벤치마크'에 따로 적었다).\n")
    w(f"**찾은 방법과 범위**: LLM·VLM을 다루는 논문 등 후보 {cov['pool']:,}편의 arXiv 판을 찾아 본문에서 벤치마크 이름 {len(MB['benchmarks_searched'])}종을 검색했다. 본문을 읽은 것은 {cov['fulltext']:,}편이고, **{cov['not_found']:,}편은 arXiv 판을 찾지 못해 확인하지 못했다**(OpenReview는 자동 다운로드를 막는다). 본문에 이름이 나온 {cov['fulltext_with_mention']}편을 LLM이 읽어 실험에 썼는지 판정했고, 성능 수치는 본문에 그대로 있는 값만 남겼다(검증된 수치 {cov['results_verified']}개). 그래서 이 목록은 '전부'가 아니라 **본문을 확인할 수 있었던 논문 중 전부**다. 파이프라인은 `scripts/medqa_bench/`에 있다.\n")
    w(f'### Medical QA가 주 타깃인 논문 ({len(mb_main)}편)\n')
    w(f'위 {len(used)}편 중 대부분은 여러 도메인을 평가하는 일반 LLM 논문이고, 의료 QA 자체를 풀려는 논문은 아래 {len(mb_main)}편이다. 대표 성능은 논문이 보고한 값이며, 괄호는 그 논문 안의 비교 대상이다(논문끼리는 비교할 수 없다).\n')
    w('| 논문 | 벤치마크 | 모델 | 학습 | 문제 정의 | 제안 방법 | 대표 성능 |\n|---|---|---|---|---|---|---|')
    for p in mb_main:
        w(f"| [{esc_md(p['title'])}]({p['url']}) | {', '.join(p['benchmarks_norm'])} | {esc_md(', '.join(p['models'][:3]))} | {p['training']} | {esc_md(p['problem_ko'])} | {esc_md(p['method_ko'])} | {esc_md('<br>'.join(fmt_res(r) for r in p['results'][:3]))} |")
    w('')
    w('### 전체 목록\n')
    w('| # | 논문 | 벤치마크 | 모델 | 학습 | 문제 정의 | 제안 방법 |\n|---:|---|---|---|---|---|---|')
    for k, p in enumerate(used, 1):
        w(f"| {k} | [{esc_md(p['title'])}]({p['url']}) | {', '.join(p['benchmarks_norm'])} | {esc_md(', '.join(p['models'][:4]))} | {p['training']} | {esc_md(p['problem_ko'])} | {esc_md(p['method_ko'])} |")
    w('')
    w('### 성능 비교\n')
    w('각 논문이 보고한 대표 수치다. **논문마다 모델·프롬프트·평가 분할·지표가 달라 논문끼리 숫자를 직접 비교하면 안 된다.** 같은 행의 "비교 대상"과의 차이만 그 논문 안에서 의미가 있다.\n')
    w('| 벤치마크 | 논문 | 모델 | 설정 | 지표 | 값 | 비교 대상 | 비교 값 |\n|---|---|---|---|---|---:|---|---:|')
    rows = sorted(((r['benchmark'], p, r) for p in used for r in p['results']), key=lambda t: (t[0].lower(), t[1]['title'].lower()))
    for b, p, r in rows:
        w(f"| {esc_md(b)} | [{esc_md(p['title'].split(':')[0])}]({p['url']}) | {esc_md(r.get('model'))} | {esc_md(r.get('setting'))} | {esc_md(r.get('metric'))} | {esc_md(r.get('value'))} | {esc_md(r.get('compared_to'))} | {esc_md(r.get('compared_value'))} |")
    w('')
    w(f"<details><summary>본문에 벤치마크 이름은 나오지만 실험에는 쓰지 않은 논문 {len(cited)}편</summary>\n")
    w('| 논문 | 자체 벤치마크 | 비고 |\n|---|---|---|')
    for p in cited:
        w(f"| [{esc_md(p['title'])}]({p['url']}) | {esc_md(p['own_benchmark'])} | {esc_md(p['override'] or p['method_ko'])} |")
    w('\n</details>\n')
    if MB['abstract_only']:
        w(f"초록에는 벤치마크 이름이 나오지만 arXiv 판을 찾지 못해 본문을 확인하지 못한 논문 {len(MB['abstract_only'])}편: " + ', '.join(f"[{esc_md(x['title'].split(':')[0])}]({x['url']}) ({', '.join(x['benchmarks_in_abstract'])})" for x in MB['abstract_only']) + '\n')
w('## 논문 목록\n')
for k, n, desc in CATS[:4]:
    w(f'### {n} ({counts[k]}편)\n')
    w(f'{desc}. 다른 분류와 겹치는 논문은 양쪽에 모두 나온다.\n')
    w(paper_table(by_cat(k)) + '\n')
w(f'### RAG ({counts["rag"]}편)\n')
for k, n in SUBS:
    lst = [p for p in P if p['rag_sub'] == k]
    w(f'#### {n} ({len(lst)}편)\n')
    w(paper_table(lst) + '\n')

w('## 키워드 트렌드 분석 (NeurIPS 2025 → 2026)\n')
w(f'방법: 주제별 정규식이 제목+초록에 걸리는 논문 비율을 2025({T["N2025"]:,}편)와 2026({T["N2026"]:,}편)에서 각각 계산하고, 비율의 배수(2026 비율 ÷ 2025 비율)를 성장으로 봤다. 정규식은 `scripts/topic_trends.py`에 있다. 키워드 매칭이라 한 단어가 여러 뜻으로 쓰이는 경우(예: calibration)는 과대 집계될 수 있다.\n')
mp = AS['med_llm_pool']
w(f"### 의료 × LLM 논문 안에서 커진 주제\n")
w(f"의료 용어와 LLM 용어가 함께 나오는 논문({mp['n2025']}편 → {mp['n2026']}편) 안에서 각 주제를 다루는 논문의 비율. 같은 키워드 규칙을 두 해에 똑같이 적용했다.\n")
w('| 주제 | 2025 | 2026 |\n|---|---:|---:|')
for t in AS['med_themes']:
    w(f"| {t['theme']} | {t['share2025']}% ({t['n2025']}) | {t['share2026']}% ({t['n2026']}) |")
w('')
w('### 요약\n')
for n_ in TREND_NOTES:
    w(f'- {n_}')
w('')
w('### 성장 상위 20개 주제\n')
w('| 주제 | 2025 편수 (비율) | 2026 편수 (비율) | 배수 |\n|---|---:|---:|---:|')
for r in rising[:20]:
    w(f"| {r['topic']} | {r['n2025']} ({r['share2025']}%) | {r['n2026']} ({r['share2026']}%) | ×{r['growth']} |")
w('\n### 비율이 줄어든 주제 (하위 10개)\n')
w('| 주제 | 2025 편수 (비율) | 2026 편수 (비율) | 배수 |\n|---|---:|---:|---:|')
for r in rising[-10:][::-1]:
    w(f"| {r['topic']} | {r['n2025']} ({r['share2025']}%) | {r['n2026']} ({r['share2026']}%) | ×{r['growth']} |")
w('\n### 제목에 등장한 신규·급증 단어\n')
w('제목에 해당 단어가 들어간 논문 수.\n')
w('| 단어 | 2025 | 2026 |\n|---|---:|---:|')
for t in T['title_terms']:
    w(f"| `{t['term']}` | {t['n2025']} | {t['n2026']} |")
w('')

def refs(lst):
    return ', '.join(f"[{short(find(s))}]({find(s)['url']})" for s in lst)

w('## 다음 연구 주제 제안 (일반)\n')
w('트렌드 수치는 측정값이고, "아이디어"는 그 수치와 논문 목록을 근거로 한 판단이다.\n')
for i, x in enumerate(NEXT_TOPICS, 1):
    w(f"### {i}. {x['title']}\n")
    w(f"- **근거**: {x['why']}")
    w(f"- **아이디어**: {x['idea']}")
    w(f"- **관련 NeurIPS 2026 논문**: {refs(x['papers'])}\n")
w('## Medical QA 쪽에서 해볼 만한 연구\n')
w(f'아래 "공백"은 이 저장소의 의료 논문 {n_med}편과 RAG {counts["rag"]}편을 비교해 찾은 것이다. 편수는 측정값이고, 공백이라는 판단은 이 목록 안에서의 판단이다(다른 학회·arXiv는 보지 않았다).\n')
for i, x in enumerate(MEDQA_IDEAS, 1):
    w(f"### {i}. {x['title']}\n")
    w(f"- **공백**: {x['gap']}")
    w(f"- **아이디어**: {x['idea']}")
    w(f"- **출발점 논문**: {refs(x['papers'])}\n")
w('## 하이라이트 (Oral · Spotlight)\n')
w(f"발표 형식을 아는 {HT['n_known']:,}편 중 Oral {HT['n_oral']}편, Spotlight {HT['n_highlight'] - HT['n_oral']}편, 합계 **{HT['n_highlight']}편({HT['base_rate']}%)**이 하이라이트다. "
  f"나머지 {T['N2026'] - HT['n_known']:,}편은 형식을 알 수 없어(Journal·Position 트랙 포함) 실제 하이라이트는 이보다 많을 수 있다. 전체 {HT['n_highlight']}편을 분야별로 정리한 목록은 [`HIGHLIGHTS.md`](HIGHLIGHTS.md)에 있다.\n")
w(f'### 이 저장소 주제 안의 하이라이트 ({len(hl_scope)}편)\n')
w(hl_table(hl_scope) + '\n')
w(f'### 의료가 핵심 응용인 하이라이트 ({len(hl_med)}편, LLM 여부 무관)\n')
w('초록을 읽고 골랐다. 의료 키워드가 걸리는 하이라이트는 12편이지만 7편은 의료를 예시로만 언급한다.\n')
w(hl_table(hl_med, True) + '\n')
w('### 주제별 하이라이트 비율\n')
for n_ in HIGHLIGHT_NOTES:
    w(f'- {n_}')
w('')
w(f"주제 정규식은 트렌드 분석과 같고, 발표 형식을 아는 논문이 40편 이상인 주제만 실었다. 기준선은 {HT['base_rate']}%. 하이라이트 편수가 한 자릿수인 주제가 많아 비율 차이는 참고용이다.\n")
w('| 주제 | 논문 수 | 하이라이트 | 비율 | 기준선 대비 |\n|---|---:|---:|---:|---:|')
for r in lift_rows:
    w(f"| {r['topic']} | {r['n']} | {r['highlights']} | {r['rate']}% | ×{r['lift']} |")
w('')
w('## 재현\n')
w('```bash\nbash scripts/fetch.sh            # neurips.cc에서 2025·2026 포스터 목록 다운로드 → data/raw/\npython3 scripts/candidates.py    # 1차 키워드 후보 (1,103편)\npython3 scripts/decisions.py     # Oral/Spotlight/Poster·트랙 병합 → data/decisions.json, papers.json 갱신\npython3 scripts/topic_trends.py  # 주제별 비율 → data/topic_trends.json\npython3 scripts/title_terms.py   # 제목 n-gram 증가 → data/title_terms.json\npython3 scripts/highlights.py    # 하이라이트 목록·주제별 비율 → data/highlights.json, data/highlight_topics.json\npython3 scripts/areas.py         # 14개 분야 비중·하이라이트 비율, 의료×LLM 주제 변화 → data/area_stats.json\npython3 scripts/explorer.py      # explorer.html 생성 (전체 9,094편 태그 탐색)\npython3 scripts/branchmap.py     # medical_qa.html, opsd.html 생성 (갈래 지도)\npython3 scripts/build.py         # README.md, HIGHLIGHTS.md, interests.html 생성\n```\n')
w('LLM 분류 단계는 스크립트로 남기지 않았고, 그 결과가 `data/papers.json`의 `cats`, `rag_sub`, `summary_ko` 필드, `data/highlight_labels.json`(하이라이트의 분야·요약), `data/area_labels.json`(전체 논문의 분야)이다.\n')
w('## 파일\n')
w('| 파일 | 내용 |\n|---|---|')
w('| `data/papers.json` | 216편: 제목, 저자, 초록, NeurIPS 페이지 URL, OpenReview URL(있으면), 발표 형식, 트랙, 분류, 한 줄 요약 |')
w('| `data/papers.csv` | 위와 같되 초록 제외 |')
w('| `data/topic_trends.json` | 주제별 2025/2026 편수·비율·배수, 제목 단어 집계 |')
w('| `data/title_terms.json` | 제목 n-gram 중 증가율 상위 |')
w('| `HIGHLIGHTS.md` | NeurIPS 2026 전체 Oral·Spotlight 논문, 분야별 |')
w('| `data/highlights.json` | 하이라이트 논문: 제목, 저자, URL, 형식, 트랙, 분야, 한 줄 요약, 이 저장소 분류(해당 시) |')
w('| `data/highlight_topics.json` | 주제별·분류별 하이라이트 비율 |')
w('| `data/decisions.json` | 포스터 id별 발표 형식·트랙·OpenReview URL (7,882편) |')
w('| `data/dataset_track_stats.json` | Evaluations & Datasets 트랙과 Main 트랙의 의료 논문 수·비율, 해당 논문 id, 판정 규칙 |')
w('| `data/medqa_benchmark_papers.json` | 의료 QA 벤치마크 본문 검색·판정 결과: 논문별 벤치마크, 모델, 학습 여부, 문제·방법, 검증된 성능 수치, 검색 범위 |')
w('| `data/opd_papers.json` | on-policy·self-distillation 논문(유형, 설정, 한 줄 요약, 발표 형식), 연구 흐름, 집계 |')
w('| `data/research_flows.json` | 관심 분야별 연구 흐름 한 줄 요약, 흐름별 어림 편수, 대표 논문(제목·URL) |')
w('| `data/area_labels.json` | 2025·2026 전체 논문의 분야 코드(14개)와 배정 묶음 번호 |')
w('| `data/area_stats.json` | 분야별 비중·변화·오차·하이라이트 비율, 의료×LLM 주제 변화, 트랙·형식 분포 |')
w('| `medical_qa.html` / `opsd.html` | 주제별 연구 갈래 지도: 큰 갈래(무엇에서 무엇으로 옮겨가는지, 왜) → 세부 갈래 → 논문 ([Medical QA](https://chpark-ml.github.io/neurips2026-medical-llm-rag/medical_qa.html), [OPSD](https://chpark-ml.github.io/neurips2026-medical-llm-rag/opsd.html)) |')
w('| `data/branch_medical_qa.json`, `data/branch_opsd.json` | 갈래 지도 데이터: LLM이 초록을 전부 읽고 나눈 갈래·세부 갈래와 논문 배치 |')
w('| `explorer.html` | 전체 9,094편 태그 탐색기: 분야 → 세부 주제, 키워드 주제, 발표 형식, 트랙으로 필터 ([열기](https://chpark-ml.github.io/neurips2026-medical-llm-rag/explorer.html)) |')
w('| `data/subtopic_labels.json` | 분야별 세부 주제 212개와 논문별 세부 주제 1–2개 (LLM이 제목·초록 앞부분으로 배정, `scripts/subtopic_prompt.md`) |')
w('| `interests.html` | 관심 분야 리포트: 학회 전체 → 분야 → 트렌드 → 의료·RAG 순서의 분석, 216편 목록, on-policy·self-distillation, 의료 QA 벤치마크 실험 논문, 하이라이트 405편, 연구 제안 ([열기](https://chpark-ml.github.io/neurips2026-medical-llm-rag/interests.html)) |')
open('REPORT.md', 'w').write('\n'.join(md) + '\n')

# ---------------------------------------------------------------- README.md (short)
BASE = 'https://chpark-ml.github.io/neurips2026-medical-llm-rag'
OPN = len(json.load(open('data/opd_papers.json'))['papers'])
ar = {a['code']: a for a in AS['areas']}
mth = {t['theme']: t for t in AS['med_themes']}
DS = json.load(open('data/dataset_track_stats.json'))
rm = []
r = rm.append
r('# NeurIPS 2026 — 의료 QA·RAG·에이전트·LLM 논문 정리\n')
r(f'NeurIPS 2026 채택 논문 {T["N2026"]:,}편을 분야·주제로 나누고, 의료 QA·의료 RAG·의료 에이전트·의료 LLM·RAG·on-policy/self-distillation 논문을 골라 정리했다.\n')
r('## 웹 페이지\n')
r('휴대폰에서도 열린다. 네 페이지는 서로 독립적이다.\n')
r('| 페이지 | 내용 |\n|---|---|')
r(f'| [관심 분야 리포트]({BASE}/interests.html) | 학회 전체 → 분야 → 트렌드 → 의료·RAG 순서의 분석, 관심 분야 논문 목록, 하이라이트, 연구 제안 |')
r(f'| [논문 탐색기]({BASE}/explorer.html) | 전체 {T["N2026"]:,}편을 분야·세부 주제(212개)·키워드·발표 형식으로 걸러 보기 |')
r(f'| [Medical QA 연구 지도]({BASE}/medical_qa.html) | Medical QA 논문을 갈래로 나눈 연구 흐름 |')
r(f'| [On-policy·Self-distillation 연구 지도]({BASE}/opsd.html) | OPD·OPSD 논문을 갈래로 나눈 연구 흐름 |')
r('')
r('## 숫자로 보기\n')
r('| 항목 | 편수 |\n|---|---:|')
r(f'| NeurIPS 2026 전체 | {T["N2026"]:,} |')
r(f'| 관심 분야 (의료 {n_med} · RAG {counts["rag"]}, 일부 겹침) | {len(P)} |')
r(f'| On-policy·Self-distillation | {OPN} |')
if MB:
    r(f"| 기존 의료 QA 벤치마크로 실험 (그중 의료 QA가 주 타깃) | {len([p for p in MB['papers'] if p['used_in_experiments']])} ({len(mb_main)}) |")
r(f'| Oral·Spotlight (발표 형식을 아는 {HT["n_known"]:,}편 중) | {HT["n_highlight"]} |')
r('')
r('## 주요 관찰\n')
r(f"- **LLM 에이전트만 크게 커졌다.** 14개 분야 중 'LLM 에이전트·도구·검색'의 비중이 {ar['B']['share2025']}% → {ar['B']['share2026']}%로 오차를 넘어 늘어난 유일한 큰 변화다.")
r(f"- **의료는 작고 하이라이트가 적다.** 의료·헬스케어 분야는 {ar['K']['share2026']}%이고, Oral·Spotlight 비율이 {ar['K']['hl_rate']}%({ar['K']['highlights']}/{ar['K']['known']}편)로 14개 분야 중 가장 낮다(학회 기준선 {AS['base_rate']}%).")
r(f"- **의료는 데이터셋 트랙에 몰린다.** Evaluations & Datasets 트랙 {DS['ed']}편 중 {DS['ed_med']}편({DS['ed_rate']}%)이 의료로, Main 트랙({DS['main_rate']}%)의 약 {DS['ed_rate'] / DS['main_rate']:.0f}배다. 그중 {DS['ed_med_llm_bench']}편이 의료 LLM 벤치마크다.")
r(f"- **의료 LLM 연구의 질문이 '근거'로 옮겨갔다.** 의료×LLM 논문 중 근거·귀속·환각을 다루는 비율이 {mth['근거·귀속·환각']['share2025']}% → {mth['근거·귀속·환각']['share2026']}%, 검색(RAG)은 {mth['검색 (RAG)']['share2025']}% → {mth['검색 (RAG)']['share2026']}%.")
r("- **RAG는 agentic search로 흡수되는 중이다.** 'RAG'라는 말을 쓰는 논문 비중은 그대로(×0.96)인데 deep research·search agent는 ×3.5.")
if MB:
    r(f"- **MedQA 류 벤치마크 실험 논문 {len([p for p in MB['papers'] if p['used_in_experiments']])}편 중 대부분은 일반 LLM 논문이다.** 의료 QA 자체를 목표로 한 것은 {len(mb_main)}편이다.")
r('')
r('## 파일\n')
r('| 파일 | 내용 |\n|---|---|')
r('| [`REPORT.md`](REPORT.md) | 상세판: 분야·트렌드 표, 관심 분야별 연구 흐름, 216편·의료 QA 벤치마크 논문 목록과 성능 표, 연구 제안 |')
r('| [`HIGHLIGHTS.md`](HIGHLIGHTS.md) | 학회 전체 Oral·Spotlight 405편, 분야별 |')
r('| `interests.html`, `explorer.html`, `medical_qa.html`, `opsd.html` | 위 웹 페이지의 원본 |')
r('| `data/` | 모든 집계와 분류 결과 (JSON·CSV). 파일별 설명은 REPORT.md 끝에 있다 |')
r('| `scripts/` | 데이터 수집·분류·집계·페이지 생성 코드 |')
r('')
r('## 어떻게 만들었나\n')
r(f'- 원천: neurips.cc 공식 포스터 목록(2026 {T["N2026"]:,}편, 2025 {T["N2025"]:,}편)과 발표 형식 정보, 공개된 arXiv 본문.')
r('- 분야·세부 주제·관심 분야 분류와 한 줄 요약은 LLM이 제목·초록(일부는 본문)을 읽고 붙였다. 사람이 검수하지 않았다.')
r('- 트렌드는 주제별 키워드 정규식으로 센 비율이고, 하이라이트 비율에는 95% 신뢰구간을 함께 봤다.')
r('- 의료 QA 벤치마크 실험 여부는 arXiv 본문을 읽어 판정했고, 성능 수치는 본문에 그대로 있는 값만 남겼다. arXiv 판이 없는 논문은 확인하지 못했다.')
r('')
r('## 재현\n')
r('```bash\nbash scripts/fetch.sh && python3 scripts/decisions.py && python3 scripts/topic_trends.py && python3 scripts/highlights.py && python3 scripts/areas.py\npython3 scripts/build.py && python3 scripts/explorer.py && python3 scripts/branchmap.py\n```\n')
r('LLM 판독 단계의 결과는 `data/`에 저장돼 있어, 위 명령만으로 페이지와 문서를 다시 만들 수 있다. 의료 QA 벤치마크 본문 검색은 `scripts/medqa_bench/`에 따로 있다.\n')
open('README.md', 'w').write('\n'.join(rm) + '\n')

# ---------------------------------------------------------------- HIGHLIGHTS.md
hm = []
w = hm.append
w('# NeurIPS 2026 하이라이트 (Oral · Spotlight) 논문\n')
w(f"발표 형식을 아는 {HT['n_known']:,}편 중 Oral {HT['n_oral']}편, Spotlight {HT['n_highlight'] - HT['n_oral']}편, 합계 **{HT['n_highlight']}편**. "
  f"{T['N2026'] - HT['n_known']:,}편은 neurips.cc 데이터에 형식이 없어 빠졌으므로 실제 하이라이트는 더 많을 수 있다. "
  '분야와 한 줄 요약은 초록을 읽고 LLM이 붙였다. 의료·RAG 관점의 해석은 [REPORT](REPORT.md#하이라이트-oral--spotlight)에 있다.\n')
w('| 분야 | Oral | Spotlight | 합계 |\n|---|---:|---:|---:|')
for a in AREAS:
    o = sum(h['area'] == a and h['decision'] == 'Oral' for h in H); t_ = sum(h['area'] == a for h in H)
    w(f'| [{AREA_KO[a]}](#{re.sub(r"[^0-9a-z가-힣 -]", "", AREA_KO[a].lower()).replace(" ", "-")}) | {o} | {t_ - o} | {t_} |')
w('')
for a in AREAS:
    lst = sorted([h for h in H if h['area'] == a], key=lambda h: (h['decision'] != 'Oral', clean(h['title']).lower()))
    w(f'## {AREA_KO[a]}\n')
    w(hl_table(lst) + '\n')
open('HIGHLIGHTS.md', 'w').write('\n'.join(hm) + '\n')

# ---------------------------------------------------------------- papers.csv
import csv
with open('data/papers.csv', 'w', newline='') as f:
    cw = csv.writer(f)
    cw.writerow(['id', 'title', 'categories', 'rag_subtype', 'decision', 'track', 'summary_ko', 'url', 'openreview', 'authors'])
    for p in P:
        cw.writerow([p['id'], clean(p['title']), ';'.join(p['cats']), p['rag_sub'] or '', p['decision'] or '', p['track'] or '', p['summary_ko'], p['url'], p['openreview'] or '', p['authors']])

# ---------------------------------------------------------------- interests.html helpers
def mdinline(s):
    s = html.escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'\*(.+?)\*', r'<em>\1</em>', s)
    return re.sub(r'`(.+?)`', r'<code>\1</code>', s)

def ref_html(lst):
    return ''.join(f'<a class="ref" href="{find(s)["url"]}" target="_blank" rel="noopener">{html.escape(short(find(s)))}</a>' for s in lst)

papers_js = [dict(id=p['id'], t=clean(p['title']), a=p['authors'], ab=p['abstract'], u=p['url'], o=p['openreview'], d=p['decision'], tr=p['track'], c=p['cats'], s=p['rag_sub'], k=p['summary_ko']) for p in P]
chart_rows = rising[:16]
maxshare = max(max(r['share2025'], r['share2026']) for r in chart_rows)

stat_cards = ''.join(f'<button class="stat" data-cat="{k}"><span class="num">{counts[k]}</span><span class="lbl">{n}</span></button>' for k, n, _ in CATS)
bars = ''.join(
    f'<div class="brow" tabindex="0" data-tip="{html.escape(r["topic"])}: 2025 {r["n2025"]}편 ({r["share2025"]}%) → 2026 {r["n2026"]}편 ({r["share2026"]}%), ×{r["growth"]}">'
    f'<div class="bname">{html.escape(r["topic"])}</div><div class="bplot">'
    f'<div class="bar y25" style="width:{r["share2025"]/maxshare*100:.2f}%"></div>'
    f'<div class="bar y26" style="width:{r["share2026"]/maxshare*100:.2f}%"></div></div>'
    f'<div class="bval">×{r["growth"]}</div></div>' for r in chart_rows)
trend_table = ''.join(f'<tr><td>{html.escape(r["topic"])}</td><td>{r["n2025"]} ({r["share2025"]}%)</td><td>{r["n2026"]} ({r["share2026"]}%)</td><td>×{r["growth"]}</td></tr>' for r in rising)
term_table = ''.join(f'<tr><td><code>{html.escape(t["term"])}</code></td><td>{t["n2025"]}</td><td>{t["n2026"]}</td></tr>' for t in T['title_terms'])
notes = ''.join(f'<li>{mdinline(n_)}</li>' for n_ in TREND_NOTES)
topics = ''.join(f'<article class="idea"><h3><span class="idx">{i:02d}</span>{html.escape(x["title"])}</h3><p><b>근거</b> {mdinline(x["why"])}</p><p><b>아이디어</b> {mdinline(x["idea"])}</p><div class="refs">{ref_html(x["papers"])}</div></article>' for i, x in enumerate(NEXT_TOPICS, 1))
medqa = ''.join(f'<article class="idea"><h3><span class="idx">{i:02d}</span>{html.escape(x["title"])}</h3><p><b>공백</b> {mdinline(x["gap"])}</p><p><b>아이디어</b> {mdinline(x["idea"])}</p><div class="refs">{ref_html(x["papers"])}</div></article>' for i, x in enumerate(MEDQA_IDEAS, 1))
sub_opts = ''.join(f'<option value="{k}">{n} ({sub_counts[k]})</option>' for k, n in SUBS)
hl_js = [dict(t=clean(h['title']), u=h['url'], d=h['decision'], a=h['area'], k=h['summary_ko'], au=h['authors'], tr=h['track']) for h in H]
hl_notes = ''.join(f'<li>{mdinline(n_)}</li>' for n_ in HIGHLIGHT_NOTES)
def hl_cards(lst):
    return ''.join(f'<article class="paper"><a class="ttl" href="{h["url"]}" target="_blank" rel="noopener">{html.escape(clean(h["title"]))}</a><div class="sum">{html.escape(h["summary_ko"])}</div><div class="meta"><span class="tag dec">{h["decision"]}</span><span class="tag">{AREA_KO[h["area"]]}</span>' + ''.join(f'<span class="tag {"r" if c == "rag" else "m"}">{CAT_NAME[c]}</span>' for c in h['in_scope']) + '</div></article>' for h in lst)
area_chips = ''.join(f'<button class="chip hchip" data-area="{html.escape(a)}" aria-pressed="false">{AREA_KO[a]} <span>{sum(h["area"] == a for h in H)}</span></button>' for a in AREAS)
lift_table = ''.join(f'<tr><td>{html.escape(r["topic"])}</td><td>{r["n"]}</td><td>{r["highlights"]}</td><td>{r["rate"]}%</td><td>×{r["lift"]}</td></tr>' for r in lift_rows)
cat_chips = ''.join(f'<button class="chip" data-cat="{k}" aria-pressed="false">{n} <span>{counts[k]}</span></button>' for k, n, _ in CATS)

# ---------------------------------------------------------------- interests.html
CLIP_JS = r'''<script>
(() => {
document.querySelectorAll('.clip').forEach(clip => {
  const btn = clip.nextElementSibling;
  if (!btn || !btn.classList.contains('cliptog')) return;
  const items = () => clip.querySelectorAll('.paper, tbody tr').length;
  const update = () => {
    clip.classList.toggle('over', clip.scrollHeight > 470);
    btn.hidden = !(clip.scrollHeight > 470);
    const unit = clip.querySelector('tbody') ? '개' : '편';
    btn.textContent = clip.classList.contains('open') ? '목록 접기' : `목록 펼치기 (${items()}${unit})`;
  };
  btn.addEventListener('click', () => {
    const opening = !clip.classList.contains('open');
    clip.classList.toggle('open');
    update();
    if (!opening) clip.scrollIntoView({block: 'start', behavior: 'smooth'});
  });
  new MutationObserver(update).observe(clip, {childList: true, subtree: true});
  update();
});
})();
</script>'''
# The top-down report (scripts/atlas.py data + scripts/interests_template.html) with the 216-paper list,
# keyword-trend detail, the full highlight list and the idea sections slotted into it.
from atlas import atlas_data
IDX_CSS = """
.stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; }
.stat { text-align: left; background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 14px 16px; cursor: pointer; font: inherit; color: inherit; }
.stat:hover { border-color: var(--accent); }
.stat .num { display: block; font-size: 28px; font-weight: 700; font-variant-numeric: tabular-nums; }
.stat .lbl { color: var(--ink-2); font-size: 13px; }
.controls { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
#q, #hq, #oq, #bq { flex: 1 1 260px; min-width: 0; padding: 9px 12px; border: 1px solid var(--line); border-radius: 8px; background: var(--surface); color: var(--ink); font: inherit; }
.controls select { padding: 8px 10px; border: 1px solid var(--line); border-radius: 8px; background: var(--surface); color: var(--ink); font: inherit; max-width: 100%; }
.chips { display: flex; flex-wrap: wrap; gap: 6px; }
.chip { border: 1px solid var(--line); background: var(--surface); color: var(--ink-2); border-radius: 999px; padding: 5px 12px; cursor: pointer; font: inherit; font-size: 13px; }
.chip span { color: var(--ink-3); margin-left: 4px; font-variant-numeric: tabular-nums; }
.chip[aria-pressed="true"] { background: var(--accent-soft); border-color: var(--accent); color: var(--ink); }
.count { color: var(--ink-3); font-size: 13px; }
.plist { display: flex; flex-direction: column; gap: 8px; }
.paper { background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 12px 16px; }
.paper .ttl { font-weight: 600; color: var(--ink); text-decoration: none; }
.paper .ttl:hover { text-decoration: underline; }
.paper .sum { color: var(--ink-2); font-size: 14px; margin: 2px 0 6px; }
.meta { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; font-size: 12px; }
.tag { border-radius: 4px; padding: 1px 7px; border: 1px solid var(--line); color: var(--ink-2); }
.tag.m { border-color: var(--med); } .tag.r { border-color: var(--rag); }
.tag.dec { font-weight: 600; color: var(--ink); background: var(--surface-2); }
.paper details { margin-top: 6px; font-size: 13.5px; color: var(--ink-2); }
.paper summary { cursor: pointer; color: var(--ink-3); font-size: 12.5px; }
.paper .auth { color: var(--ink-3); font-size: 12.5px; margin: 6px 0; }
.chart { background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 16px; }
.brow { display: grid; grid-template-columns: minmax(120px, 260px) 1fr 56px; gap: 10px; align-items: center; padding: 5px 4px; border-radius: 6px; outline: none; }
.brow:hover, .brow:focus { background: var(--surface-2); }
.bname { font-size: 13px; color: var(--ink-2); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.bplot { display: flex; flex-direction: column; gap: 2px; }
.bplot .bar { height: 8px; border-radius: 0 4px 4px 0; min-width: 2px; }
.bplot .bar.y25 { background: var(--series-2); } .bplot .bar.y26 { background: var(--series-1); }
.bval { font-size: 13px; font-variant-numeric: tabular-nums; text-align: right; color: var(--ink); }
.notes { padding-left: 18px; margin: 0; color: var(--ink-2); max-width: 82ch; } .notes li { margin: 6px 0; } .notes strong { color: var(--ink); }
.twocol { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: start; }
.twocol > * { min-width: 0; }
.tablebox { background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 12px 14px; overflow-x: auto; }
.tablebox h3 { margin: 0 0 8px; font-size: 15px; }
.tablebox summary { cursor: pointer; font-size: 14px; color: var(--ink-2); }
.tablebox table { width: 100%; border-collapse: collapse; font-size: 13.5px; }
.tablebox th, .tablebox td { text-align: left; padding: 6px 8px; border-bottom: 1px solid var(--line); }
.tablebox td:not(:first-child), .tablebox th:not(:first-child) { text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }
.ideas { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 14px; }
.idea { background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 16px 18px; }
.idea h3 { margin: 0 0 10px; font-size: 16px; display: flex; gap: 10px; align-items: baseline; }
.idea .idx { font-family: var(--f-mono); color: var(--accent); font-size: 13px; }
.idea p { margin: 6px 0; font-size: 14px; color: var(--ink-2); } .idea p b { color: var(--ink); margin-right: 4px; }
.refs { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; }
.ref { font-size: 12px; border: 1px solid var(--line); border-radius: 4px; padding: 1px 7px; color: var(--ink-2); text-decoration: none; }
.method { color: var(--ink-2); font-size: 14px; margin: 0; padding-left: 20px; } .method li { margin: 4px 0; max-width: 90ch; }
/* long lists open folded so the sections below stay reachable */
.clip { max-height: 460px; overflow: hidden; position: relative; }
.clip.open { max-height: none; }
.clip.over:not(.open)::after { content: ""; position: absolute; left: 0; right: 0; bottom: 0; height: 90px; background: linear-gradient(to bottom, transparent, var(--bg)); pointer-events: none; }
.cliptog { align-self: center; margin-top: 4px; padding: 8px 18px; border-radius: 999px; border: 1px solid var(--accent); background: var(--surface); color: var(--accent); font: 500 13.5px var(--f-body); cursor: pointer; }
.cliptog:hover { background: var(--accent-soft); }
@media (max-width: 720px) {
  .twocol { grid-template-columns: 1fr; }
  .brow { grid-template-columns: 1fr 48px; } .bname { grid-column: 1 / -1; white-space: normal; }
  .ideas { grid-template-columns: 1fr; }
}
"""
lvl = lambda tag, id_, title, lead, body: (f'<section class="lvl" id="{id_}"><div class="lvl-head"><span class="lvl-tag">{tag}</span><h2>{title}</h2><p>{lead}</p></div>{body}</section>')
sec_trends = lvl('L2+', 'trends', '키워드 트렌드 상세 (2025 → 2026)',
    f'주제별 정규식이 제목+초록에 걸리는 논문의 비율을 2025({T["N2025"]:,}편)와 2026({T["N2026"]:,}편)에서 비교했다. 막대는 비율, 오른쪽 숫자는 비율의 배수다. 키워드 매칭이라 다의어는 과대 집계될 수 있다.',
    f'<ul class="notes">{notes}</ul><div class="chart" role="img" aria-label="성장률 상위 16개 주제의 2025년과 2026년 논문 비율 비교">'
    f'<div class="legend"><span><i style="width:12px;height:12px;border-radius:3px;background:var(--series-2)"></i>2025 비율</span><span><i style="width:12px;height:12px;border-radius:3px;background:var(--series-1)"></i>2026 비율</span></div>{bars}</div>'
    f'<div class="twocol"><details class="tablebox"><summary><b>전체 주제 표</b> (배수 내림차순, {len(rising)}개)</summary><table><thead><tr><th>주제</th><th>2025</th><th>2026</th><th>배수</th></tr></thead><tbody>{trend_table}</tbody></table></details>'
    f'<div class="tablebox"><h3>제목에 들어간 단어 (논문 수)</h3><table><thead><tr><th>단어</th><th>2025</th><th>2026</th></tr></thead><tbody>{term_table}</tbody></table></div></div>')
sec_papers = lvl('216', 'papers', '관심 분야 논문 216편',
    f'제목·초록을 읽고 핵심 기여 기준으로 고른 논문이다(의료 관련 {n_med}편, RAG {counts["rag"]}편, 일부 겹침). 카드를 누르면 그 분류만 보이고, 검색은 제목·저자·요약·초록 전체를 본다.',
    f'<div class="stats">{stat_cards}</div><p class="muted">RAG 세부 유형: {" · ".join(f"{n} {sub_counts[k]}" for k, n in SUBS)}</p>'
    f'<div class="controls"><input id="q" type="search" placeholder="검색: 예) GraphRAG, chest X-ray, benchmark, 진단" aria-label="논문 검색">'
    f'<select id="sub" aria-label="RAG 세부 유형"><option value="">RAG 유형 전체</option>{sub_opts}</select>'
    f'<select id="dec" aria-label="발표 형식"><option value="">발표 형식 전체</option><option>Oral</option><option>Spotlight</option><option>Poster</option></select></div>'
    f'<div class="chips">{cat_chips}</div><div class="count" id="count"></div><div class="clip"><div class="plist" id="plist"></div></div><button class="cliptog" type="button" hidden></button>')
OP = json.load(open('data/opd_papers.json'))
op_types = {'on-policy': 'On-policy distillation (외부 교사)', 'both': 'On-policy self-distillation', 'self': 'Self-distillation (자기 롤아웃 외)'}
op_flows = ''.join(f"<li>{html.escape(f['line_ko'])} <span class=\"muted\">(약 {f['n_approx']}편)</span> — " + ', '.join(f'<a href="{r["url"]}" target="_blank" rel="noopener">{html.escape(r["short"])}</a>' for r in f['refs']) + '</li>' for f in OP['flows'])
op_set_chips = ''.join(f'<button class="chip ochip" data-k="{html.escape(k)}" aria-pressed="false">{html.escape(k)} <span>{v}</span></button>' for k, v in OP['stats']['by_setting'])
op_type_opts = ''.join(f'<option value="{k}">{v} ({OP["stats"]["by_type"].get(k, 0)})</option>' for k, v in op_types.items())
ost = OP['stats']
sec_opd = lvl('OPD', 'opd', f"On-policy · Self-distillation ({ost['n']}편)",
    f"학생 모델이 직접 만든 출력에 교사가 신호를 주는 on-policy distillation과, 모델이 자기 자신(이전·힌트를 받은·더 긴 추론의 자신)을 교사로 쓰는 self-distillation 연구다. 학회 전체 {T['N2026']:,}편에서 키워드로 후보 {ost['candidates']}편을 뽑고 초록을 읽어 {ost['n']}편을 골랐다. 고전적인 오프라인 지식 증류와 비전 자기지도학습의 self-distillation은 뺐다.",
    f'<div class="big"><div><b>{ost["title_opd"][0]} → {ost["title_opd"][1]}</b><span>제목에 on-policy distillation이 들어간 논문 (2025 → 2026)</span></div>'
    f'<div><b>{ost["title_sd"][0]} → {ost["title_sd"][1]}</b><span>제목에 self-distillation이 들어간 논문 (2025 → 2026)</span></div>'
    f'<div><b>{ost["hl"]}/{ost["known"]}편</b><span>Oral·Spotlight (형식을 아는 논문 기준, {ost["hl_rate"]}%, 학회 기준선 {HT["base_rate"]}%)</span></div></div>'
    f'<p>{html.escape(OP["summary_ko"])}</p><ul class="notes">{op_flows}</ul>'
    f'<div class="controls"><input id="oq" type="search" placeholder="검색: 제목·요약·저자" aria-label="on-policy·self-distillation 논문 검색">'
    f'<select id="otype" aria-label="유형"><option value="">유형 전체</option>{op_type_opts}</select></div>'
    f'<div class="chips">{op_set_chips}</div><div class="count" id="ocount"></div><div class="clip"><div class="plist" id="olist"></div></div><button class="cliptog" type="button" hidden></button>')
OP_JS = """<script>
(() => {
const O = __O__, TY = __TY__;
const $ = s => document.querySelector(s);
const esc = s => (s || '').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const sel = new Set();
function render() {
  const q = $('#oq').value.trim().toLowerCase(), ty = $('#otype').value;
  const L = O.filter(p => (!sel.size || sel.has(p.setting)) && (!ty || p.type === ty) && (!q || (p.title + ' ' + p.summary_ko + ' ' + p.authors).toLowerCase().includes(q)))
    .sort((a, b) => ((a.decision === 'Oral' || a.decision === 'Spotlight') ? 0 : 1) - ((b.decision === 'Oral' || b.decision === 'Spotlight') ? 0 : 1) || a.title.localeCompare(b.title));
  $('#ocount').textContent = L.length + '편 표시 중 (전체 ' + O.length + '편)';
  $('#olist').innerHTML = L.map(p => `<article class="paper"><a class="ttl" href="${p.url}" target="_blank" rel="noopener">${esc(p.title)}</a>
    <div class="sum">${esc(p.summary_ko)}</div><div class="meta"><span class="tag r">${TY[p.type]}</span><span class="tag">${esc(p.setting)}</span>
    ${p.decision && p.decision !== 'Poster' ? `<span class="tag dec">${p.decision}</span>` : ''}</div>
    <details><summary>저자</summary><div class="auth">${esc(p.authors)}</div></details></article>`).join('');
}
document.querySelectorAll('.ochip').forEach(b => b.onclick = () => { sel.has(b.dataset.k) ? sel.delete(b.dataset.k) : sel.add(b.dataset.k); b.setAttribute('aria-pressed', sel.has(b.dataset.k)); render(); });
['#oq', '#otype'].forEach(s => $(s).addEventListener('input', render));
render();
})();
</script>"""
OP_JS = OP_JS.replace('__O__', json.dumps(OP['papers'], ensure_ascii=False)).replace('__TY__', json.dumps(op_types, ensure_ascii=False))
sec_mb, MB_JS = '', ''
if MB:
    cov = MB['coverage']; mb_used = [p for p in MB['papers'] if p['used_in_experiments']]
    bcount = collections.Counter(b for p in mb_used for b in p['benchmarks_norm'])
    mb_chips = ''.join(f'<button class="chip bchip" data-k="{html.escape(b)}" aria-pressed="false">{html.escape(b)} <span>{n}</span></button>' for b, n in bcount.most_common())
    tr_opts = ''.join(f'<option>{html.escape(t)}</option>' for t, _ in collections.Counter(p['training'] for p in mb_used).most_common())
    sec_mb = lvl('QA', 'medqa-bench', f'Medical QA 벤치마크로 실험한 논문 ({len(mb_used)}편)',
        f"MedQA·MedMCQA·MedXpertQA·VQA-RAD 같은 기존 공개 의료 QA 벤치마크로 직접 실험한 논문이다. 논문이 새로 만든 벤치마크만 쓴 경우는 뺐다. 후보 {cov['pool']:,}편 중 arXiv 판으로 본문을 읽은 {cov['fulltext']:,}편에서 찾았고, {cov['not_found']:,}편은 arXiv 판이 없어 확인하지 못했다. 그래서 이 목록은 본문을 확인할 수 있었던 논문 중 전부다.",
        f'<div class="big"><div><b>{len(mb_used)}편</b><span>기존 의료 QA 벤치마크로 실험</span></div><div><b>{cov["fulltext_with_mention"]}편</b><span>본문에 벤치마크 이름이 나옴 (LLM이 실험 여부 판정)</span></div>'
        f'<div><b>{cov["fulltext"]:,} / {cov["pool"]:,}</b><span>본문을 읽은 후보 / 전체 후보</span></div><div><b>{cov["results_verified"]}개</b><span>본문에서 그대로 확인된 성능 수치</span></div></div>'
        f'<div class="sub"><h3>Medical QA가 주 타깃인 논문 ({len(mb_main)}편)</h3><p class="muted">{len(mb_used)}편 중 대부분은 여러 도메인을 평가하는 일반 LLM 논문이다. 의료 QA 자체를 풀려는 논문은 아래 {len(mb_main)}편이다. 성능 괄호는 그 논문 안의 비교 대상이다.</p><div class="plist">'
        + ''.join(f'<article class="paper"><a class="ttl" href="{p["url"]}" target="_blank" rel="noopener">{html.escape(p["title"])}</a><div class="sum"><b>문제</b> {html.escape(p["problem_ko"])}<br><b>방법</b> {html.escape(p["method_ko"])}<br><b>모델</b> {html.escape(", ".join(p["models"][:4]))}</div><div class="meta">' + ''.join(f'<span class="tag m">{html.escape(b)}</span>' for b in p['benchmarks_norm']) + f'<span class="tag dec">{html.escape(p["training"])}</span></div>' + (f'<ul class="notes" style="margin-top:6px;font-size:13px">' + ''.join(f'<li>{html.escape(fmt_res(r))}</li>' for r in p['results']) + '</ul>' if p['results'] else '') + '</article>' for p in mb_main)
        + '</div></div><h3 class="subh" style="margin:8px 0 0">전체 ' + str(len(mb_used)) + '편</h3>'
        f'<div class="controls"><input id="bq" type="search" placeholder="검색: 제목·모델·방법" aria-label="벤치마크 논문 검색"><select id="btr" aria-label="학습 여부"><option value="">학습 여부 전체</option>{tr_opts}</select></div>'
        f'<div class="chips">{mb_chips}</div><div class="count" id="bcount"></div><div class="clip"><div class="plist" id="blist"></div></div><button class="cliptog" type="button" hidden></button>'
        f'<div class="sub"><h3>성능 비교</h3><p class="muted">각 논문이 보고한 대표 수치다. 논문마다 모델·프롬프트·평가 분할·지표가 달라 논문끼리 직접 비교하면 안 되고, 같은 행의 비교 대상과의 차이만 그 논문 안에서 의미가 있다. 위에서 벤치마크를 고르면 이 표도 걸러진다.</p>'
        f'<div class="clip"><div class="tablebox"><table><thead><tr><th>벤치마크</th><th>논문</th><th>모델</th><th>설정</th><th>값</th><th>비교 대상</th><th>비교 값</th></tr></thead><tbody id="bres"></tbody></table></div></div><button class="cliptog" type="button" hidden></button></div>')
    MB_JS = """<script>
(() => {
const B = __B__;
const $ = s => document.querySelector(s);
const esc = s => (s || '').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const sel = new Set();
function render() {
  const q = $('#bq').value.trim().toLowerCase(), tr = $('#btr').value;
  const L = B.filter(p => (!sel.size || p.benchmarks_norm.some(b => sel.has(b))) && (!tr || p.training === tr)
    && (!q || (p.title + ' ' + p.models.join(' ') + ' ' + p.method_ko + ' ' + p.problem_ko).toLowerCase().includes(q)));
  $('#bcount').textContent = L.length + '편 표시 중 (전체 ' + B.length + '편)';
  $('#blist').innerHTML = L.map(p => `<article class="paper"><a class="ttl" href="${p.url}" target="_blank" rel="noopener">${esc(p.title)}</a>
    <div class="sum"><b>문제</b> ${esc(p.problem_ko)}<br><b>방법</b> ${esc(p.method_ko)}</div>
    <div class="meta">${p.benchmarks_norm.map(b => `<span class="tag m">${esc(b)}</span>`).join('')}<span class="tag dec">${esc(p.training)}</span>
    ${p.decision && p.decision !== 'Poster' ? `<span class="tag dec">${p.decision}</span>` : ''}</div>
    <details><summary>모델 · 다른 데이터셋</summary><div class="auth">모델: ${esc(p.models.join(', ') || '—')}<br>다른 데이터셋: ${esc(p.other_datasets.join(', ') || '—')}</div></details></article>`).join('');
  const rows = L.flatMap(p => p.results.filter(r => !sel.size || [...sel].some(b => (r.benchmark || '').toLowerCase().includes(b.toLowerCase().split(' ')[0]))).map(r => [r, p]))
    .sort((a, b) => (a[0].benchmark || '').localeCompare(b[0].benchmark || ''));
  $('#bres').innerHTML = rows.map(([r, p]) => `<tr><td>${esc(r.benchmark)}</td><td><a href="${p.url}" target="_blank" rel="noopener">${esc(p.title.split(':')[0])}</a></td><td>${esc(r.model)}</td><td>${esc(r.setting)}${r.metric ? ' · ' + esc(r.metric) : ''}</td><td>${esc(r.value)}</td><td>${esc(r.compared_to)}</td><td>${esc(r.compared_value)}</td></tr>`).join('') || '<tr><td colspan="7">해당 수치 없음</td></tr>';
}
document.querySelectorAll('.bchip').forEach(b => b.onclick = () => { sel.has(b.dataset.k) ? sel.delete(b.dataset.k) : sel.add(b.dataset.k); b.setAttribute('aria-pressed', sel.has(b.dataset.k)); render(); });
['#bq', '#btr'].forEach(s => $(s).addEventListener('input', render));
render();
})();
</script>""".replace('__B__', json.dumps(mb_used, ensure_ascii=False))
hl_more = (f'<div class="sub"><h3>NeurIPS 2026 전체 하이라이트 {HT["n_highlight"]}편</h3>'
    f'<p class="muted">발표 형식을 아는 {HT["n_known"]:,}편 중 Oral {HT["n_oral"]}편, Spotlight {HT["n_highlight"] - HT["n_oral"]}편(기준선 {HT["base_rate"]}%). {T["N2026"] - HT["n_known"]:,}편은 형식 정보가 없어 빠졌으므로 실제 하이라이트는 더 많을 수 있다. 분야·요약은 초록을 읽고 LLM이 붙였다.</p>'
    f'<ul class="notes">{hl_notes}</ul>'
    f'<details class="tablebox"><summary><b>주제별 하이라이트 비율</b> — 논문 40편 이상 주제, 기준선 {HT["base_rate"]}% (하이라이트가 한 자릿수인 주제가 많아 참고용)</summary>'
    f'<table><thead><tr><th>주제</th><th>논문</th><th>하이라이트</th><th>비율</th><th>기준선 대비</th></tr></thead><tbody>{lift_table}</tbody></table></details>'
    f'<div class="controls"><input id="hq" type="search" placeholder="하이라이트 검색: 제목·요약·저자" aria-label="하이라이트 검색">'
    f'<select id="hdec" aria-label="형식"><option value="">Oral + Spotlight</option><option>Oral</option><option>Spotlight</option></select></div>'
    f'<div class="chips">{area_chips}</div><div class="count" id="hcount"></div><div class="clip"><div class="plist" id="hlist"></div></div><button class="cliptog" type="button" hidden></button></div>')
sec_ideas = (lvl('제안', 'next', '다음 연구 주제 제안', '근거의 수치는 측정값이고, 아이디어는 그 수치와 논문 목록을 근거로 한 판단이다. 링크는 출발점이 되는 NeurIPS 2026 논문이다.', f'<div class="ideas">{topics}</div>')
    + lvl('제안', 'medqa', 'Medical QA 쪽에서 해볼 만한 연구', f"'공백'은 이 목록의 의료 논문 {n_med}편과 RAG {counts['rag']}편을 비교해 찾은 것이다. 다른 학회나 arXiv는 보지 않았으므로 이 목록 안에서의 공백이다.", f'<div class="ideas">{medqa}</div>'))
sec_method = lvl('방법', 'method', '어떻게 모았나', '이 페이지의 수치와 분류는 모두 아래 방식으로 만들었다.', f"""<ol class="method">
<li>neurips.cc 공식 다운로드의 2026 포스터 목록 {T["N2026"]:,}편(제목·저자·초록)과 비교용 2025년 {T["N2025"]:,}편을 원천으로 썼다.</li>
<li>분야: 모든 논문에 LLM이 제목만 보고 14개 분야 중 하나를 배정했다. 묶음 사이 편차로 오차를 어림해, 오차의 두 배보다 큰 변화만 증가·감소로 표시했다.</li>
<li>트렌드 주제: 정규식 {len(rising)}개(<code>scripts/topic_trends.py</code>). MCP·LLM 불확실성·LLM 에이전트·activation steering은 다른 뜻까지 잡지 않도록 좁혔다.</li>
<li>관심 분야 216편: 의료 용어 × LLM 용어, 또는 검색 용어로 후보 1,103편을 뽑고, 후보 전부를 LLM이 읽어 핵심 기여 기준으로 분류했다. 제외된 논문 중 신호가 강한 167편은 초록 전문으로 재검토해 17편을 추가했고, 경계 사례 직접 확인으로 2편을 더하고 1편을 뺐다.</li>
<li>발표 형식: neurips.cc의 orals-posters JSON 두 스냅샷(받을 때마다 다른 일부만 담김)을 합쳤다. 전체 {T["N2026"]:,}편 중 {HT["n_known"]:,}편의 형식을 알고, 216편 중 {len(P) - n_dec}편은 모른다.</li>
<li>한계: 사람 검수가 아닌 LLM 판독이고, 순수 검색·임베딩 논문과 LLM이 없는 의료 영상·EHR 모델은 216편에서 제외했다.</li>
</ol>""")
IDX_JS = """<script>
(() => {
const P = __P__, H = __H__, AREA = __AREA__, CAT = __CAT__, SUB = __SUB__;
const $ = s => document.querySelector(s);
const esc = s => (s || '').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const sel = new Set();
function render() {
  const q = $('#q').value.trim().toLowerCase(), sub = $('#sub').value, dec = $('#dec').value;
  const L = P.filter(p => (!sel.size || p.c.some(c => sel.has(c))) && (!sub || p.s === sub) && (!dec || p.d === dec)
    && (!q || (p.t + ' ' + p.a + ' ' + p.k + ' ' + p.ab).toLowerCase().includes(q))).sort((a, b) => a.t.localeCompare(b.t));
  $('#count').textContent = L.length + '편 표시 중 (전체 ' + P.length + '편)';
  $('#plist').innerHTML = L.map(p => `<article class="paper"><a class="ttl" href="${p.u}" target="_blank" rel="noopener">${esc(p.t)}</a>
    <div class="sum">${esc(p.k)}</div><div class="meta">${p.c.map(c => `<span class="tag ${c === 'rag' ? 'r' : 'm'}">${CAT[c]}</span>`).join('')}
    ${p.s ? `<span class="tag r">${SUB[p.s]}</span>` : ''}${p.d ? `<span class="tag ${p.d !== 'Poster' ? 'dec' : ''}">${p.d}</span>` : ''}
    ${p.tr ? `<span class="tag">${p.tr}</span>` : ''}${p.o ? `<a href="${p.o}" target="_blank" rel="noopener">OpenReview</a>` : ''}</div>
    <details><summary>초록·저자</summary><div class="auth">${esc(p.a)}</div>${esc(p.ab)}</details></article>`).join('');
}
function setCat(c, only) {
  if (only) { sel.clear(); sel.add(c); } else sel.has(c) ? sel.delete(c) : sel.add(c);
  document.querySelectorAll('.chip:not(.hchip)').forEach(b => b.setAttribute('aria-pressed', sel.has(b.dataset.cat)));
  render();
}
document.querySelectorAll('.chip:not(.hchip)').forEach(b => b.onclick = () => setCat(b.dataset.cat));
document.querySelectorAll('.stat').forEach(b => b.onclick = () => { setCat(b.dataset.cat, true); $('#plist').scrollIntoView({behavior: 'smooth'}); });
['#q', '#sub', '#dec'].forEach(s => $(s).addEventListener('input', render));
const hsel = new Set();
function hrender() {
  const q = $('#hq').value.trim().toLowerCase(), dec = $('#hdec').value;
  const L = H.filter(h => (!hsel.size || hsel.has(h.a)) && (!dec || h.d === dec) && (!q || (h.t + ' ' + h.k + ' ' + h.au).toLowerCase().includes(q)))
    .sort((a, b) => (a.d !== 'Oral') - (b.d !== 'Oral') || a.t.localeCompare(b.t));
  $('#hcount').textContent = L.length + '편 표시 중 (전체 ' + H.length + '편)';
  $('#hlist').innerHTML = L.map(h => `<article class="paper"><a class="ttl" href="${h.u}" target="_blank" rel="noopener">${esc(h.t)}</a>
    <div class="sum">${esc(h.k)}</div><div class="meta"><span class="tag dec">${h.d}</span><span class="tag">${AREA[h.a]}</span>${h.tr ? `<span class="tag">${h.tr}</span>` : ''}</div>
    <details><summary>저자</summary><div class="auth">${esc(h.au)}</div></details></article>`).join('');
}
document.querySelectorAll('.hchip').forEach(b => b.onclick = () => {
  hsel.has(b.dataset.area) ? hsel.delete(b.dataset.area) : hsel.add(b.dataset.area);
  b.setAttribute('aria-pressed', hsel.has(b.dataset.area)); hrender();
});
['#hq', '#hdec'].forEach(s => $(s).addEventListener('input', hrender));
const tip = $('#tip');
document.querySelectorAll('.brow').forEach(r => {
  const show = e => { tip.textContent = r.dataset.tip; tip.style.opacity = 1;
    const b = r.getBoundingClientRect(), x = e && e.clientX != null ? e.clientX : b.left, y = e && e.clientY != null ? e.clientY : b.top;
    tip.style.left = Math.max(8, Math.min(x + 12, innerWidth - 330)) + 'px'; tip.style.top = (y + 14) + 'px'; };
  r.addEventListener('mousemove', show); r.addEventListener('focus', () => show());
  r.addEventListener('mouseleave', () => tip.style.opacity = 0); r.addEventListener('blur', () => tip.style.opacity = 0);
});
render(); hrender();
})();
</script>"""
for k, v in {'__P__': papers_js, '__H__': hl_js, '__AREA__': AREA_KO, '__CAT__': CAT_NAME, '__SUB__': SUB_NAME}.items():
    IDX_JS = IDX_JS.replace(k, json.dumps(v, ensure_ascii=False))
page = open('scripts/interests_template.html').read()
for k, v in {'/*INDEX_CSS*/': IDX_CSS, '<!--TRENDS-->': sec_trends, '<!--PAPERS-->': sec_papers + sec_opd + sec_mb, '<!--HL_MORE-->': hl_more,
             '<!--IDEAS-->': sec_ideas, '<!--METHOD-->': sec_method, '<!--INDEX_JS-->': IDX_JS + OP_JS + MB_JS + CLIP_JS}.items():
    assert page.count(k) == 1, k
    page = page.replace(k, v)
page = page.replace('/*DATA*/null', json.dumps(atlas_data(), ensure_ascii=False))
open('interests.html', 'w').write(page)
print('REPORT.md', len(md), 'lines; README.md', len(rm), 'lines; interests.html', len(page) // 1024, 'KB;', len(P), 'papers')
