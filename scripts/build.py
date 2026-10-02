"""Render README.md and index.html from data/*.json and scripts/insights.py.
Usage (from repo root): python3 scripts/build.py"""
import json, re, sys, html, collections, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from insights import TREND_NOTES, NEXT_TOPICS, MEDQA_IDEAS, HIGHLIGHT_NOTES, MED_HIGHLIGHTS

P = json.load(open('data/papers.json'))
T = json.load(open('data/topic_trends.json'))
H = json.load(open('data/highlights.json'))
HT = json.load(open('data/highlight_topics.json'))

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
w('# NeurIPS 2026 — Medical QA · Medical RAG · Medical Agent · Medical LLM · RAG 논문 정리\n')
w(f'NeurIPS 2026 채택 논문 **{T["N2026"]:,}편** 중, 아래 다섯 주제 중 하나 이상을 핵심 기여로 다룬 논문 **{len(P)}편**을 모았다. '
  '키워드 트렌드 분석(2025 대비)과 다음 연구 주제 제안, Medical QA 연구 아이디어를 함께 정리했다.\n')
w('> 같은 내용을 검색·필터가 되는 페이지로 보려면 [`index.html`](index.html)을 브라우저로 열면 된다. NeurIPS 2026 전체의 Oral·Spotlight 논문은 [`HIGHLIGHTS.md`](HIGHLIGHTS.md)에 따로 정리했다.\n')
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
w('```bash\nbash scripts/fetch.sh            # neurips.cc에서 2025·2026 포스터 목록 다운로드 → data/raw/\npython3 scripts/candidates.py    # 1차 키워드 후보 (1,103편)\npython3 scripts/decisions.py     # Oral/Spotlight/Poster·트랙 병합 → data/decisions.json, papers.json 갱신\npython3 scripts/topic_trends.py  # 주제별 비율 → data/topic_trends.json\npython3 scripts/title_terms.py   # 제목 n-gram 증가 → data/title_terms.json\npython3 scripts/highlights.py    # 하이라이트 목록·주제별 비율 → data/highlights.json, data/highlight_topics.json\npython3 scripts/build.py         # README.md, HIGHLIGHTS.md, index.html 생성\n```\n')
w('LLM 분류 단계는 스크립트로 남기지 않았고, 그 결과가 `data/papers.json`의 `cats`, `rag_sub`, `summary_ko` 필드와 `data/highlight_labels.json`(하이라이트의 분야·요약)이다.\n')
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
w('| `index.html` | 검색·필터가 되는 단일 HTML 페이지 |')
open('README.md', 'w').write('\n'.join(md) + '\n')

# ---------------------------------------------------------------- HIGHLIGHTS.md
hm = []
w = hm.append
w('# NeurIPS 2026 하이라이트 (Oral · Spotlight) 논문\n')
w(f"발표 형식을 아는 {HT['n_known']:,}편 중 Oral {HT['n_oral']}편, Spotlight {HT['n_highlight'] - HT['n_oral']}편, 합계 **{HT['n_highlight']}편**. "
  f"{T['N2026'] - HT['n_known']:,}편은 neurips.cc 데이터에 형식이 없어 빠졌으므로 실제 하이라이트는 더 많을 수 있다. "
  '분야와 한 줄 요약은 초록을 읽고 LLM이 붙였다. 의료·RAG 관점의 해석은 [README](README.md#하이라이트-oral--spotlight)에 있다.\n')
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

# ---------------------------------------------------------------- index.html
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

page = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>NeurIPS 2026 Medical LLM·RAG</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {{
  color-scheme: light;
  --bg: #f7f6f3; --surface: #fcfcfb; --surface-2: #f0efeb; --line: #e2e0da;
  --ink: #0b0b0b; --ink-2: #52514e; --ink-3: #807e78;
  --accent: #2a78d6; --accent-soft: #e6f0fb;
  --series-1: #2a78d6; --series-2: #eb6834;
  --med: #1baf7a; --rag: #4a3aa7;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    color-scheme: dark;
    --bg: #121211; --surface: #1a1a19; --surface-2: #232321; --line: #33322f;
    --ink: #ffffff; --ink-2: #c3c2b7; --ink-3: #8f8d86;
    --accent: #3987e5; --accent-soft: #1d2a3a;
    --series-1: #3987e5; --series-2: #d95926;
    --med: #199e70; --rag: #9085e9;
  }}
}}
:root[data-theme="dark"] {{
  color-scheme: dark;
  --bg: #121211; --surface: #1a1a19; --surface-2: #232321; --line: #33322f;
  --ink: #ffffff; --ink-2: #c3c2b7; --ink-3: #8f8d86;
  --accent: #3987e5; --accent-soft: #1d2a3a;
  --series-1: #3987e5; --series-2: #d95926;
  --med: #199e70; --rag: #9085e9;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--bg); color: var(--ink); font: 15px/1.6 "IBM Plex Sans KR", system-ui, sans-serif; }}
a {{ color: var(--accent); text-decoration: none; }} a:hover {{ text-decoration: underline; }}
code {{ font-family: "IBM Plex Mono", monospace; font-size: .88em; background: var(--surface-2); padding: 1px 5px; border-radius: 4px; }}
.wrap {{ max-width: 1120px; margin: 0 auto; padding: 0 16px; }}
header.top {{ position: sticky; top: 0; z-index: 10; background: color-mix(in srgb, var(--bg) 88%, transparent); backdrop-filter: blur(8px); border-bottom: 1px solid var(--line); }}
header.top .wrap {{ display: flex; align-items: center; gap: 16px; height: 56px; }}
.brand {{ font-weight: 700; white-space: nowrap; }}
nav {{ display: flex; gap: 4px; overflow-x: auto; flex: 1; scrollbar-width: none; }}
nav a {{ color: var(--ink-2); padding: 6px 10px; border-radius: 6px; white-space: nowrap; font-size: 14px; }}
nav a:hover {{ background: var(--surface-2); text-decoration: none; color: var(--ink); }}
#theme {{ border: 1px solid var(--line); background: var(--surface); color: var(--ink-2); border-radius: 6px; padding: 4px 10px; cursor: pointer; font: inherit; font-size: 13px; }}
.hero {{ padding: 48px 0 24px; }}
.hero h1 {{ font-size: clamp(26px, 4vw, 38px); line-height: 1.25; margin: 0 0 12px; letter-spacing: -0.01em; }}
.hero p {{ color: var(--ink-2); max-width: 760px; margin: 0; }}
.stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin: 28px 0 8px; }}
.stat {{ text-align: left; background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 14px 16px; cursor: pointer; font: inherit; color: inherit; transition: border-color .15s; }}
.stat:hover {{ border-color: var(--accent); }}
.stat .num {{ display: block; font-size: 30px; font-weight: 700; font-variant-numeric: tabular-nums; }}
.stat .lbl {{ color: var(--ink-2); font-size: 13px; }}
.substat {{ color: var(--ink-3); font-size: 13px; margin-top: 8px; }}
section {{ padding: 36px 0; border-top: 1px solid var(--line); }}
section h2 {{ font-size: 22px; margin: 0 0 6px; }}
.lead {{ color: var(--ink-2); margin: 0 0 20px; max-width: 820px; }}
.controls {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin-bottom: 14px; }}
#q, #hq {{ flex: 1 1 260px; min-width: 0; padding: 9px 12px; border: 1px solid var(--line); border-radius: 8px; background: var(--surface); color: var(--ink); font: inherit; }}
select {{ padding: 8px 10px; border: 1px solid var(--line); border-radius: 8px; background: var(--surface); color: var(--ink); font: inherit; max-width: 100%; }}
.chips {{ display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 12px; }}
.chip {{ border: 1px solid var(--line); background: var(--surface); color: var(--ink-2); border-radius: 999px; padding: 5px 12px; cursor: pointer; font: inherit; font-size: 13px; }}
.chip span {{ color: var(--ink-3); margin-left: 4px; font-variant-numeric: tabular-nums; }}
.chip[aria-pressed="true"] {{ background: var(--accent-soft); border-color: var(--accent); color: var(--ink); }}
.count {{ color: var(--ink-3); font-size: 13px; margin-bottom: 8px; }}
.plist {{ display: flex; flex-direction: column; gap: 8px; }}
.paper {{ background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 12px 16px; }}
.paper .ttl {{ font-weight: 600; color: var(--ink); }}
.paper .sum {{ color: var(--ink-2); font-size: 14px; margin: 2px 0 6px; }}
.meta {{ display: flex; flex-wrap: wrap; gap: 6px; align-items: center; font-size: 12px; }}
.tag {{ border-radius: 4px; padding: 1px 7px; border: 1px solid var(--line); color: var(--ink-2); }}
.tag.m {{ border-color: var(--med); }} .tag.r {{ border-color: var(--rag); }}
.tag.dec {{ font-weight: 600; color: var(--ink); background: var(--surface-2); }}
.paper details {{ margin-top: 6px; font-size: 13.5px; color: var(--ink-2); }}
.paper summary {{ cursor: pointer; color: var(--ink-3); font-size: 12.5px; }}
.paper .auth {{ color: var(--ink-3); font-size: 12.5px; margin: 6px 0; }}
.legend {{ display: flex; gap: 16px; font-size: 13px; color: var(--ink-2); margin-bottom: 10px; }}
.legend i {{ display: inline-block; width: 12px; height: 12px; border-radius: 3px; vertical-align: -1px; margin-right: 6px; }}
.chart {{ background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 16px; position: relative; }}
.brow {{ display: grid; grid-template-columns: minmax(120px, 260px) 1fr 56px; gap: 10px; align-items: center; padding: 5px 4px; border-radius: 6px; outline: none; }}
.brow:hover, .brow:focus {{ background: var(--surface-2); }}
.bname {{ font-size: 13px; color: var(--ink-2); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
.bplot {{ display: flex; flex-direction: column; gap: 2px; }}
.bar {{ height: 8px; border-radius: 0 4px 4px 0; min-width: 2px; }}
.bar.y25 {{ background: var(--series-2); }} .bar.y26 {{ background: var(--series-1); }}
.bval {{ font-size: 13px; font-variant-numeric: tabular-nums; text-align: right; color: var(--ink); }}
#tip {{ position: fixed; pointer-events: none; background: var(--ink); color: var(--bg); font-size: 12.5px; padding: 6px 10px; border-radius: 6px; max-width: 320px; opacity: 0; transition: opacity .1s; z-index: 20; }}
.notes {{ padding-left: 18px; color: var(--ink-2); }} .notes li {{ margin: 6px 0; }} .notes strong {{ color: var(--ink); }}
table {{ width: 100%; border-collapse: collapse; font-size: 13.5px; }}
th, td {{ text-align: left; padding: 6px 8px; border-bottom: 1px solid var(--line); }}
th {{ color: var(--ink-3); font-weight: 500; }} td:not(:first-child), th:not(:first-child) {{ text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }}
.twocol {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px; }}
.tablebox {{ background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 12px 14px; overflow-x: auto; }}
.tablebox h3 {{ margin: 0 0 8px; font-size: 15px; }}
.ideas {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 14px; }}
.idea {{ background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 16px 18px; }}
.idea h3 {{ margin: 0 0 10px; font-size: 16px; display: flex; gap: 10px; align-items: baseline; }}
.idea .idx {{ font-family: "IBM Plex Mono", monospace; color: var(--accent); font-size: 13px; }}
.idea p {{ margin: 6px 0; font-size: 14px; color: var(--ink-2); }} .idea p b {{ color: var(--ink); margin-right: 4px; }}
.refs {{ display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; }}
.ref {{ font-size: 12px; border: 1px solid var(--line); border-radius: 4px; padding: 1px 7px; color: var(--ink-2); }}
.sub {{ font-size: 15px; margin: 18px 0 10px; }}
.tablebox summary {{ cursor: pointer; font-size: 14px; color: var(--ink-2); }}
.method {{ color: var(--ink-2); font-size: 14px; }} .method li {{ margin: 4px 0; }}
footer {{ color: var(--ink-3); font-size: 13px; padding: 28px 0 48px; border-top: 1px solid var(--line); }}
@media (max-width: 720px) {{
  .twocol {{ grid-template-columns: 1fr; }}
  .brow {{ grid-template-columns: 1fr 48px; }} .bname {{ grid-column: 1 / -1; white-space: normal; }}
  .ideas {{ grid-template-columns: 1fr; }}
  .brand {{ display: none; }}
}}
</style>
</head>
<body>
<header class="top"><div class="wrap">
  <div class="brand">NeurIPS 2026 · Med LLM/RAG</div>
  <nav><a href="#papers">논문</a><a href="#trends">트렌드</a><a href="#next">연구 주제</a><a href="#medqa">Medical QA 아이디어</a><a href="#highlights">하이라이트</a><a href="#method">방법</a></nav>
  <button id="theme" type="button" aria-label="테마 전환">테마</button>
</div></header>
<main class="wrap">
<div class="hero">
  <h1>NeurIPS 2026에서 의료 QA·RAG·에이전트·LLM과 RAG를 다룬 논문 {len(P)}편</h1>
  <p>채택 논문 {T["N2026"]:,}편의 제목·초록을 읽고 핵심 기여 기준으로 분류했다. 의료 관련 {n_med}편, RAG {counts["rag"]}편이며 한 논문이 여러 분류에 속할 수 있다. 카드를 누르면 해당 분류로 목록이 걸러진다.</p>
  <div class="stats">{stat_cards}</div>
  <div class="substat">RAG 세부 유형: {' · '.join(f'{n} {sub_counts[k]}' for k, n in SUBS)}</div>
</div>

<section id="papers">
  <h2>논문 목록</h2>
  <p class="lead">제목·저자·요약·초록에서 검색된다. 분류는 여러 개를 고르면 하나라도 해당하는 논문을 보여준다.</p>
  <div class="controls">
    <input id="q" type="search" placeholder="검색: 예) GraphRAG, chest X-ray, benchmark, 진단" aria-label="논문 검색">
    <select id="sub" aria-label="RAG 세부 유형"><option value="">RAG 유형 전체</option>{sub_opts}</select>
    <select id="dec" aria-label="발표 형식"><option value="">발표 형식 전체</option><option>Oral</option><option>Spotlight</option><option>Poster</option></select>
  </div>
  <div class="chips">{cat_chips}</div>
  <div class="count" id="count"></div>
  <div class="plist" id="plist"></div>
</section>

<section id="trends">
  <h2>키워드 트렌드 (2025 → 2026)</h2>
  <p class="lead">주제별 정규식이 제목+초록에 걸리는 논문의 <b>비율</b>을 2025({T["N2025"]:,}편)와 2026({T["N2026"]:,}편)에서 비교했다. 막대는 비율, 오른쪽 숫자는 비율의 배수. 키워드 매칭이라 다의어는 과대 집계될 수 있다.</p>
  <ul class="notes">{notes}</ul>
  <div class="chart" role="img" aria-label="성장률 상위 16개 주제의 2025년과 2026년 논문 비율 비교">
    <div class="legend"><span><i style="background:var(--series-2)"></i>2025 비율</span><span><i style="background:var(--series-1)"></i>2026 비율</span></div>
    {bars}
  </div>
  <div class="twocol">
    <div class="tablebox"><h3>전체 주제 표 (배수 내림차순)</h3><table><thead><tr><th>주제</th><th>2025</th><th>2026</th><th>배수</th></tr></thead><tbody>{trend_table}</tbody></table></div>
    <div class="tablebox"><h3>제목에 들어간 단어 (논문 수)</h3><table><thead><tr><th>단어</th><th>2025</th><th>2026</th></tr></thead><tbody>{term_table}</tbody></table></div>
  </div>
</section>

<section id="next">
  <h2>다음 연구 주제 제안</h2>
  <p class="lead">근거의 수치는 측정값이고, 아이디어는 그 수치와 논문 목록을 근거로 한 판단이다. 아래 링크는 출발점이 되는 NeurIPS 2026 논문.</p>
  <div class="ideas">{topics}</div>
</section>

<section id="medqa">
  <h2>Medical QA 쪽에서 해볼 만한 연구</h2>
  <p class="lead">'공백'은 이 목록의 의료 논문 {n_med}편과 RAG {counts["rag"]}편을 비교해 찾은 것이다. 다른 학회나 arXiv는 보지 않았으므로, 이 목록 안에서의 공백이다.</p>
  <div class="ideas">{medqa}</div>
</section>

<section id="highlights">
  <h2>하이라이트 (Oral · Spotlight) — NeurIPS 2026 전체 {HT["n_highlight"]}편</h2>
  <p class="lead">발표 형식을 아는 {HT["n_known"]:,}편 중 Oral {HT["n_oral"]}편, Spotlight {HT["n_highlight"] - HT["n_oral"]}편(기준선 {HT["base_rate"]}%). {T["N2026"] - HT["n_known"]:,}편은 형식 정보가 없어 빠졌으므로 실제 하이라이트는 더 많을 수 있다. 분야·요약은 초록을 읽고 LLM이 붙였다.</p>
  <ul class="notes">{hl_notes}</ul>
  <div class="twocol">
    <div><h3 class="sub">이 저장소 주제 안의 하이라이트 ({len(hl_scope)}편)</h3><div class="plist">{hl_cards(hl_scope)}</div></div>
    <div><h3 class="sub">의료가 핵심 응용인 하이라이트 ({len(hl_med)}편)</h3><div class="plist">{hl_cards(hl_med)}</div></div>
  </div>
  <details class="tablebox" style="margin-top:20px"><summary><b>주제별 하이라이트 비율</b> — 논문 40편 이상 주제, 기준선 {HT["base_rate"]}% (하이라이트가 한 자릿수인 주제가 많아 참고용)</summary>
    <table><thead><tr><th>주제</th><th>논문</th><th>하이라이트</th><th>비율</th><th>기준선 대비</th></tr></thead><tbody>{lift_table}</tbody></table></details>
  <h3 class="sub" style="margin-top:28px">전체 목록</h3>
  <div class="controls"><input id="hq" type="search" placeholder="하이라이트 검색: 제목·요약·저자" aria-label="하이라이트 검색">
    <select id="hdec" aria-label="형식"><option value="">Oral + Spotlight</option><option>Oral</option><option>Spotlight</option></select></div>
  <div class="chips">{area_chips}</div>
  <div class="count" id="hcount"></div>
  <div class="plist" id="hlist"></div>
</section>

<section id="method">
  <h2>어떻게 모았나</h2>
  <ol class="method">
    <li>neurips.cc 공식 다운로드의 2026 포스터 목록 {T["N2026"]:,}편(제목·저자·초록)을 원천으로 썼다.</li>
    <li>의료 용어 × LLM/에이전트 용어, 또는 retrieval/RAG/search 용어로 후보 1,103편을 뽑았다.</li>
    <li>후보 전부를 LLM이 읽고 핵심 기여 기준으로 분류했다. 제외된 논문 중 신호가 강한 167편은 초록 전문으로 재검토해 17편을 추가했고, 경계 사례 직접 확인으로 2편을 더하고 1편을 뺐다.</li>
    <li>발표 형식은 neurips.cc의 orals-posters JSON 두 스냅샷(받을 때마다 다른 일부만 담김)을 합쳐 붙였다. 전체 {T["N2026"]:,}편 중 {HT["n_known"]:,}편의 형식을 알고, 이 목록 {len(P)}편 중 {len(P) - n_dec}편은 모른다.</li>
    <li>한계: 사람 검수가 아닌 LLM 판독이고, 순수 검색·임베딩 논문과 LLM이 없는 의료 영상·EHR 모델은 제외했다.</li>
  </ol>
</section>
</main>
<footer><div class="wrap">데이터: neurips.cc NeurIPS 2025/2026 accepted posters. 생성: <code>scripts/build.py</code>.</div></footer>
<div id="tip" role="tooltip"></div>
<script>
const P = {json.dumps(papers_js, ensure_ascii=False)};
const H = {json.dumps(hl_js, ensure_ascii=False)};
const AREA = {json.dumps(AREA_KO, ensure_ascii=False)};
const CAT = {json.dumps(CAT_NAME, ensure_ascii=False)};
const SUB = {json.dumps(SUB_NAME, ensure_ascii=False)};
const $ = s => document.querySelector(s);
const esc = s => (s || '').replace(/[&<>"]/g, c => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]));
const sel = new Set();
function render() {{
  const q = $('#q').value.trim().toLowerCase(), sub = $('#sub').value, dec = $('#dec').value;
  const L = P.filter(p => (!sel.size || p.c.some(c => sel.has(c))) && (!sub || p.s === sub) && (!dec || p.d === dec)
    && (!q || (p.t + ' ' + p.a + ' ' + p.k + ' ' + p.ab).toLowerCase().includes(q)))
    .sort((a, b) => a.t.localeCompare(b.t));
  $('#count').textContent = L.length + '편 표시 중 (전체 ' + P.length + '편)';
  $('#plist').innerHTML = L.map(p => `<article class="paper">
    <a class="ttl" href="${{p.u}}" target="_blank" rel="noopener">${{esc(p.t)}}</a>
    <div class="sum">${{esc(p.k)}}</div>
    <div class="meta">${{p.c.map(c => `<span class="tag ${{c === 'rag' ? 'r' : 'm'}}">${{CAT[c]}}</span>`).join('')}}
      ${{p.s ? `<span class="tag r">${{SUB[p.s]}}</span>` : ''}}
      ${{p.d ? `<span class="tag ${{p.d !== 'Poster' ? 'dec' : ''}}">${{p.d}}</span>` : ''}}
      ${{p.tr ? `<span class="tag">${{p.tr}}</span>` : ''}}
      ${{p.o ? `<a href="${{p.o}}" target="_blank" rel="noopener">OpenReview</a>` : ''}}</div>
    <details><summary>초록·저자</summary><div class="auth">${{esc(p.a)}}</div>${{esc(p.ab)}}</details>
  </article>`).join('');
}}
function setCat(c, only) {{
  if (only) {{ sel.clear(); sel.add(c); }} else sel.has(c) ? sel.delete(c) : sel.add(c);
  document.querySelectorAll('.chip').forEach(b => b.setAttribute('aria-pressed', sel.has(b.dataset.cat)));
  render();
}}
document.querySelectorAll('.chip:not(.hchip)').forEach(b => b.onclick = () => setCat(b.dataset.cat));
const hsel = new Set();
function hrender() {{
  const q = $('#hq').value.trim().toLowerCase(), dec = $('#hdec').value;
  const L = H.filter(h => (!hsel.size || hsel.has(h.a)) && (!dec || h.d === dec) && (!q || (h.t + ' ' + h.k + ' ' + h.au).toLowerCase().includes(q)))
    .sort((a, b) => (a.d !== 'Oral') - (b.d !== 'Oral') || a.t.localeCompare(b.t));
  $('#hcount').textContent = L.length + '편 표시 중 (전체 ' + H.length + '편)';
  $('#hlist').innerHTML = L.map(h => `<article class="paper"><a class="ttl" href="${{h.u}}" target="_blank" rel="noopener">${{esc(h.t)}}</a>
    <div class="sum">${{esc(h.k)}}</div><div class="meta"><span class="tag dec">${{h.d}}</span><span class="tag">${{AREA[h.a]}}</span>${{h.tr ? `<span class="tag">${{h.tr}}</span>` : ''}}</div>
    <details><summary>저자</summary><div class="auth">${{esc(h.au)}}</div></details></article>`).join('');
}}
document.querySelectorAll('.hchip').forEach(b => b.onclick = () => {{
  hsel.has(b.dataset.area) ? hsel.delete(b.dataset.area) : hsel.add(b.dataset.area);
  b.setAttribute('aria-pressed', hsel.has(b.dataset.area)); hrender();
}});
['#hq', '#hdec'].forEach(s => $(s).addEventListener('input', hrender));
hrender();
document.querySelectorAll('.stat').forEach(b => b.onclick = () => {{ setCat(b.dataset.cat, true); $('#papers').scrollIntoView({{behavior: 'smooth'}}); }});
['#q', '#sub', '#dec'].forEach(s => $(s).addEventListener('input', render));
const tip = $('#tip');
document.querySelectorAll('.brow').forEach(r => {{
  const show = e => {{ tip.textContent = r.dataset.tip; tip.style.opacity = 1;
    const x = e.clientX ?? r.getBoundingClientRect().left, y = e.clientY ?? r.getBoundingClientRect().top;
    tip.style.left = Math.min(x + 12, innerWidth - 330) + 'px'; tip.style.top = (y + 14) + 'px'; }};
  r.addEventListener('mousemove', show); r.addEventListener('focus', show);
  r.addEventListener('mouseleave', () => tip.style.opacity = 0); r.addEventListener('blur', () => tip.style.opacity = 0);
}});
const root = document.documentElement;
try {{ const t = localStorage.getItem('theme'); if (t) root.dataset.theme = t; }} catch (e) {{}}
$('#theme').onclick = () => {{
  const dark = root.dataset.theme ? root.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
  root.dataset.theme = dark ? 'light' : 'dark';
  try {{ localStorage.setItem('theme', root.dataset.theme); }} catch (e) {{}}
}};
render();
</script>
</body>
</html>
'''
open('index.html', 'w').write(page)
print('README.md', len(md), 'lines; index.html', len(page) // 1024, 'KB;', len(P), 'papers')
