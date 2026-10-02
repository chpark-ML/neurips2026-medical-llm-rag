"""Area-level view: share of each of 14 research areas in 2025 and 2026, a noise estimate,
the Oral/Spotlight rate per area, and theme shifts inside medical x LLM papers.
Inputs: data/raw/neurips{2025,2026}_posters.json, data/area_labels.json (one area per paper,
assigned by an LLM from the title only; prompt in scripts/area_prompt.md), data/decisions.json.
Output: data/area_stats.json."""
import json, re, math, collections

A6 = json.load(open('data/raw/neurips2026_posters.json')); A5 = json.load(open('data/raw/neurips2025_posters.json'))
AL = json.load(open('data/area_labels.json')); D = json.load(open('data/decisions.json'))
pid = lambda x: x['virtualsite_url'].rsplit('/', 1)[-1]
CODES = AL['codes']; lab = AL['labels']; batch = AL['batch']


def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return [round((c - h) / d * 100, 2), round((c + h) / d * 100, 2)]


def se_of_share(yr, code):
    """Labels were assigned in batches of ~1,000 titles by separate LLM runs. The spread of an area's share
    across batches (labeler noise + alphabetical batch composition) gives a standard error for the share."""
    by = collections.defaultdict(list)
    for i, c in lab[yr].items():
        by[batch[yr][i]].append(c)
    sh = [L.count(code) / len(L) * 100 for L in by.values()]
    m = sum(sh) / len(sh)
    return (sum((x - m) ** 2 for x in sh) / (len(sh) - 1)) ** .5 / len(sh) ** .5


known = [x for x in A6 if D.get(pid(x), {}).get('decision') in ('Oral', 'Spotlight', 'Poster')]
is_hl = lambda x: D[pid(x)]['decision'] != 'Poster'
base = sum(map(is_hl, known)) / len(known) * 100
c6 = collections.Counter(lab['2026'][pid(x)] for x in A6); c5 = collections.Counter(lab['2025'][pid(x)] for x in A5)
areas = []
for k, name in CODES.items():
    kk = [x for x in known if lab['2026'][pid(x)] == k]; h = sum(map(is_hl, kk))
    s6, s5 = c6[k] / len(A6) * 100, c5[k] / len(A5) * 100
    se = (se_of_share('2026', k) ** 2 + se_of_share('2025', k) ** 2) ** .5
    areas.append(dict(code=k, name=name, n2025=c5[k], n2026=c6[k], share2025=round(s5, 2), share2026=round(s6, 2),
                      growth=round(s6 / s5, 2), diff_pp=round(s6 - s5, 2), se_pp=round(se, 2), clear_change=abs(s6 - s5) > 2 * se,
                      known=len(kk), highlights=h, orals=sum(D[pid(x)]['decision'] == 'Oral' for x in kk),
                      hl_rate=round(h / len(kk) * 100, 2), hl_ci=wilson(h, len(kk))))
areas.sort(key=lambda a: -a['n2026'])

# medical x LLM papers by keyword (same rule in both years), and the share of each theme inside them
MED = re.compile(r'\b(medic\w*|clinic\w*|health\s?care|healthcare|biomedic\w*|patients?|hospital\w*|EHRs?|electronic health|radiolog\w*|patholog\w*|physician\w*|doctors?|USMLE|MedQA|oncolog\w*|psychiatr\w*|mental health)\b', re.I)
LLM = re.compile(r'\b(LLMs?|large language models?|language models?|MLLMs?|VLMs?|LVLMs?|vision[- ]language models?)\b', re.I)
txt = lambda x: x['name'] + ' ' + x['abstract']
pool = {y: [x for x in A if MED.search(txt(x)) and LLM.search(txt(x))] for y, A in (('2025', A5), ('2026', A6))}
THEMES = {
    '근거·귀속·환각': r'evidence|grounding|attribution|hallucinat|faithful', '검색 (RAG)': r'retriev|\bRAG\b',
    '에이전트·멀티에이전트': r'\bagent(s|ic)?\b|multi-agent', '안전·신뢰': r'safety|\bsafe\b|trustworth|\brisk|harm',
    '추론 (reasoning)': r'reasoning', 'RL (GRPO·RLVR 등)': r'reinforcement learning|\bRL\b|GRPO|RLVR|policy optimization',
    '불확실성·abstain': r'uncertaint|calibrat|abstain|abstention|selective', '대화·문진': r'multi-turn|dialog|conversation|history taking|interview',
    '질의응답 (QA/VQA)': r'question[- ]answering|\bQA\b|\bVQA\b', '리포트 생성': r'report generation',
}
themes = []
for k, rx in THEMES.items():
    r = re.compile(rx, re.I)
    a = sum(1 for x in pool['2025'] if r.search(txt(x))); b = sum(1 for x in pool['2026'] if r.search(txt(x)))
    themes.append(dict(theme=k, n2025=a, n2026=b, share2025=round(a / len(pool['2025']) * 100, 1), share2026=round(b / len(pool['2026']) * 100, 1)))
r = re.compile(r'bench|benchmark|dataset', re.I)
a = sum(1 for x in pool['2025'] if r.search(x['name'])); b = sum(1 for x in pool['2026'] if r.search(x['name']))
themes.append(dict(theme='벤치마크 (제목)', n2025=a, n2026=b, share2025=round(a / len(pool['2025']) * 100, 1), share2026=round(b / len(pool['2026']) * 100, 1)))
themes.sort(key=lambda t: -(t['share2026'] - t['share2025']))

tracks = collections.Counter(str(D.get(pid(x), {}).get('track')) for x in A6)
formats = collections.Counter(str(D.get(pid(x), {}).get('decision')) for x in A6)
json.dump(dict(n2026=len(A6), n2025=len(A5), known=len(known), base_rate=round(base, 2), areas=areas,
               med_llm_pool=dict(n2025=len(pool['2025']), n2026=len(pool['2026']), share2025=round(len(pool['2025']) / len(A5) * 100, 2),
                                 share2026=round(len(pool['2026']) / len(A6) * 100, 2)),
               med_themes=themes, tracks=tracks, formats=formats),
          open('data/area_stats.json', 'w'), ensure_ascii=False, indent=1)
for a in areas:
    print(f"{a['code']} {a['name'][:40]:40} {a['share2025']:5.2f} -> {a['share2026']:5.2f} {'*' if a['clear_change'] else ' '} hl {a['highlights']}/{a['known']} {a['hl_rate']}% {a['hl_ci']}")
print('med pool', len(pool['2025']), len(pool['2026']))
