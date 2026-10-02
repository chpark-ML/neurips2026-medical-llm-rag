"""Render standalone branch-map pages: medical_qa.html and opsd.html.
Each page shows one topic's NeurIPS 2026 papers as a tree (topic -> branches -> sub-branches -> papers).
The tree (data/branch_<key>.json) was designed by an LLM reading every abstract; paper facts come from
data/papers.json, data/medqa_benchmark_papers.json, data/opd_papers.json and data/decisions.json.
The pages link only to neurips.cc / OpenReview, never to other pages of this repo."""
import json, html, sys

e = html.escape
TEX = {'\\chi': 'χ', '\\alpha': 'α', '\\beta': 'β', '\\delta': 'δ', '\\gamma': 'γ', '\\epsilon': 'ε', '\\lambda': 'λ', '\\pi': 'π', '\\phi': 'φ', '\\Phi': 'Φ', '\\mu': 'μ', '\\sigma': 'σ', '\\tau': 'τ'}


def clean(t):
    t = t or ''
    for k, v in TEX.items():
        t = t.replace(k, v)
    return ' '.join(t.replace('$', '').replace('{', '').replace('}', '').split())
P = {p['id']: p for p in json.load(open('data/papers.json'))}
MB = {p['id']: p for p in json.load(open('data/medqa_benchmark_papers.json'))['papers']}
OP = {p['id']: p for p in json.load(open('data/opd_papers.json'))['papers']}
D = json.load(open('data/decisions.json'))
OPTYPE = {'on-policy': 'On-policy distillation (외부 교사)', 'both': 'On-policy self-distillation', 'self': 'Self-distillation'}


def medqa_paper(i):
    p, m = P.get(i, {}), MB.get(i, {})
    tags = [('bench', b) for b in m.get('benchmarks_norm', [])]
    if m.get('own_benchmark'):
        tags.append(('own', '자체: ' + m['own_benchmark']))
    if m.get('training'):
        tags.append(('train', m['training']))
    return dict(title=p.get('title') or m.get('title'), url=p.get('url') or m.get('url'), summary=p.get('summary_ko') or m.get('method_ko'), tags=tags)


MDP = json.load(open('data/branch_med_datasets_papers.json')) if __import__('os').path.exists('data/branch_med_datasets_papers.json') else {}
A_TITLES = {}


def meddata_paper(i):
    m = MDP[i]; p = P.get(i)
    return dict(title=p['title'] if p else m.get('title'), url=p['url'] if p else f'https://neurips.cc/virtual/2026/poster/{i}',
                summary=m['summary_ko'], tags=[('kind', m['kind']), ('data', m['data_ko'])] + ([('in216', '관심 분야 216편에 포함')] if p else []))


def opsd_paper(i):
    p = OP[i]
    return dict(title=p['title'], url=p['url'], summary=p['summary_ko'], tags=[('type', OPTYPE[p['type']]), ('set', p['setting'])])


PAGES = {
    'medical_qa': dict(out='medical_qa.html', title='NeurIPS 2026 Medical QA 연구 지도', paper=medqa_paper,
                       kicker='NEURIPS 2026 · MEDICAL QA',
                       h1='Medical QA 연구는 어디로 가고 있나',
                       scope='의료·임상·생의학 질의응답(의료 VQA, 임상 추론 QA, 대화형 진단 포함)을 핵심 기여로 다룬 NeurIPS 2026 논문을 모았다. 제목·초록을 읽어 고른 Medical QA 논문과, 기존 의료 QA 벤치마크(MedQA·MedMCQA·VQA-RAD 등)로 실험하면서 의료 QA 자체를 목표로 한 논문을 합쳤다.',
                       legend=[('bench', '실험에 쓴 기존 벤치마크'), ('own', '논문이 새로 만든 벤치마크'), ('train', '학습 여부')]),
    'opsd': dict(out='opsd.html', title='NeurIPS 2026 On-policy·Self-distillation 연구 지도', paper=opsd_paper,
                 kicker='NEURIPS 2026 · ON-POLICY / SELF-DISTILLATION',
                 h1='On-policy·Self-distillation 연구는 어디로 가고 있나',
                 scope='학생 모델이 직접 만든 출력에 교사가 신호를 주는 on-policy distillation과, 모델이 자기 자신(정답·피드백·힌트를 본 자신, 이전의 자신)을 교사로 쓰는 self-distillation을 핵심 기여로 다룬 NeurIPS 2026 논문이다. 고전적인 오프라인 지식 증류와 비전 자기지도학습의 self-distillation은 뺐다.',
                 legend=[('type', '증류 유형'), ('set', '적용 분야')]),
    'med_datasets': dict(out='med_datasets.html', title='NeurIPS 2026 데이터셋 트랙 의료 논문', paper=meddata_paper,
                         kicker='NEURIPS 2026 · EVALUATIONS & DATASETS TRACK · MEDICAL',
                         h1='데이터셋 트랙의 의료 논문 60편',
                         scope='NeurIPS 2026 Evaluations & Datasets 트랙 852편 중 의료·헬스케어를 다룬 논문 60편(7.0%)이다. Main 트랙에서 의료 논문 비율은 2.3%로, 의료는 새 데이터와 평가를 내놓는 쪽에 상대적으로 몰려 있다. 의료 여부는 논문별 분야 라벨(의료·헬스케어)과 제목·초록 판독으로 정했고, 트랙 정보가 없는 논문 1,212편은 빠졌다.',
                         legend=[('kind', '논문 종류'), ('data', '데이터 (초록에 적힌 모달리티·규모)')]),
}


def render(key):
    cfg = PAGES[key]; T = json.load(open(f'data/branch_{key}.json'))
    ids = [i for b in T['branches'] for s in b['subs'] for i in s['papers']]
    total = len(ids) + len(T.get('unplaced', []))
    hl = [i for i in ids + [u['id'] for u in T.get('unplaced', [])] if D.get(i, {}).get('decision') in ('Oral', 'Spotlight')]
    nb = lambda b: sum(len(s['papers']) for s in b['subs'])
    maxb = max(nb(b) for b in T['branches'])
    # overview tree
    tree = ''
    for bi, b in enumerate(T['branches'], 1):
        subs = ''.join(f'<li><a href="#b{bi}s{si}"><span class="sn">{e(s["name_ko"])}</span><span class="sc">{len(s["papers"])}</span></a></li>' for si, s in enumerate(b['subs'], 1))
        tree += (f'<li class="br"><a class="bn" href="#b{bi}"><span class="bi">{bi}</span><span class="bt"><b>{e(b["name_ko"])}</b><span class="shift">{e(b["shift_ko"])}</span></span>'
                 f'<span class="bc"><span class="bar" style="width:{nb(b) / maxb * 100:.0f}%"></span><em>{nb(b)}편</em></span></a><ul class="subs">{subs}</ul></li>')
    # detail sections
    def card(i):
        p = cfg['paper'](i); dec = D.get(i, {}).get('decision')
        badge = f'<span class="dec {dec.lower()}">{dec}</span>' if dec in ('Oral', 'Spotlight') else ''
        tags = ''.join(f'<span class="tag {k}">{e(v)}</span>' for k, v in p['tags'])
        return f'<article class="paper"><div class="ph"><a href="{e(p["url"])}" target="_blank" rel="noopener">{e(clean(p["title"]))}</a>{badge}</div><p>{e(p["summary"] or "")}</p><div class="tags">{tags}</div></article>'
    secs = ''
    for bi, b in enumerate(T['branches'], 1):
        subs = ''.join(f'<div class="sub" id="b{bi}s{si}"><h3><span class="sid">{bi}.{si}</span>{e(s["name_ko"])} <span class="cnt">{len(s["papers"])}편</span></h3><p class="sd">{e(s["desc_ko"])}</p><div class="papers">{"".join(card(i) for i in s["papers"])}</div></div>'
                       for si, s in enumerate(b['subs'], 1))
        secs += (f'<section class="branch" id="b{bi}"><header><span class="bnum">{bi}</span><div><h2>{e(b["name_ko"])}</h2><p class="shiftbig">{e(b["shift_ko"])}</p></div></header>'
                 f'<p class="problem"><b>왜 이쪽으로 가나</b> {e(b["problem_ko"])}</p>{subs}</section>')
    if T.get('unplaced'):
        secs += '<section class="branch" id="other"><header><span class="bnum">·</span><div><h2>어느 갈래에도 두지 않은 논문</h2></div></header><div class="papers">' + ''.join(
            card(u['id']).replace('</p>', f'</p><p class="why">{e(u["reason"])}</p>', 1) for u in T['unplaced']) + '</div></section>'
    if key == 'med_datasets' and __import__('os').path.exists('data/med_datasets_notable.json'):
        NB = json.load(open('data/med_datasets_notable.json'))
        both = [x for x in NB['papers'] if x['tier'] == 'both']; one = [x for x in NB['papers'] if x['tier'] == 'one']
        def inst_line(x):
            l = ', '.join(x['lead']) or '—'; sr = ', '.join(x['senior']) or '—'
            return f'<p class="inst"><b>제1저자</b> {e(l)} · <b>마지막 저자</b> {e(sr)}</p>'
        cards = ''.join(card(x['id']).replace('<div class="tags">', inst_line(x) + '<div class="tags">', 1) for x in sorted(both, key=lambda x: clean(cfg['paper'](x['id'])['title']).lower()))
        ones = ''.join(f'<li><a href="{e(cfg["paper"](x["id"])["url"])}" target="_blank" rel="noopener">{e(clean(cfg["paper"](x["id"])["title"]))}</a> <span class="muted2">— {"제1저자 " + e(", ".join(x["lead"])) if x["lead"] else "마지막 저자 " + e(", ".join(x["senior"]))}</span></li>' for x in sorted(one, key=lambda x: clean(cfg['paper'](x['id'])['title']).lower()))
        secs += (f'<section class="branch notable" id="notable"><header><span class="bnum">★</span><div><h2>잘 알려진 기관이 이끈 연구 ({len(both)}편)</h2>'
                 f'<p class="shiftbig">제1저자와 마지막 저자가 모두 주요 대학·병원·기업 연구소 소속</p></div></header>'
                 f'<p class="problem"><b>고른 기준</b> 위 60편 중 제1저자(연구를 주도한 사람)와 마지막 저자(대개 책임 연구자)의 소속이 모두 아래 기관 목록에 있는 논문이다. 기관 목록은 세계적으로 알려진 대학, 대형 병원·의대, 빅테크 연구소로 정했다. 기관의 명성은 연구의 질을 보증하지 않고, 논문 자체의 품질은 따로 평가하지 않았다.</p>'
                 f'<div class="papers">{cards}</div>'
                 f'<div class="sub"><h3>한쪽 저자만 해당하는 논문 <span class="cnt">{len(one)}편</span></h3><p class="sd">제1저자나 마지막 저자 중 한 명만 목록의 기관 소속이다.</p><ul class="onelist">{ones}</ul></div>'
                 f'<details class="instlist"><summary>기관 목록 ({len(NB["institutions"])}곳)</summary><p>' + ' · '.join(f'{e(i["name"])}' for i in NB['institutions']) + '</p></details></section>')
    legend = ''.join(f'<span><span class="tag {k}">{e(v)}</span></span>' for k, v in cfg['legend'])
    if 'id="notable"' in secs:
        legend += ' · <a href="#notable">★ 잘 알려진 기관이 이끈 연구로 바로 가기</a>'
    page = (open('scripts/branchmap_template.html').read()
            .replace('{{TITLE}}', e(cfg['title'])).replace('{{KICKER}}', e(cfg['kicker'])).replace('{{H1}}', e(cfg['h1']))
            .replace('{{SUMMARY}}', e(T['summary_ko'])).replace('{{SCOPE}}', e(cfg['scope']))
            .replace('{{N}}', str(total)).replace('{{NB}}', str(len(T['branches']))).replace('{{NS}}', str(sum(len(b['subs']) for b in T['branches'])))
            .replace('{{NHL}}', str(len(hl))).replace('{{INSIGHT}}', e(T['insight_ko'])).replace('{{TREE}}', tree).replace('{{SECTIONS}}', secs).replace('{{LEGEND}}', legend))
    open(cfg['out'], 'w').write(page)
    print(cfg['out'], total, 'papers,', len(T['branches']), 'branches')


if __name__ == '__main__':
    for k in (sys.argv[1:] or PAGES):
        render(k)
