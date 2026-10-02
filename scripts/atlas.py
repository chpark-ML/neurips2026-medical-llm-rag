"""Data for the top-down part of interests.html (all 9,094 papers -> areas -> topics -> medical / RAG subset).
build.py calls atlas_data(). Inputs: data/area_stats.json (scripts/areas.py), data/topic_trends.json, data/highlight_topics.json,
data/papers.json, data/highlights.json, data/area_labels.json."""
import json, re, collections


def atlas_data():
    AS = json.load(open('data/area_stats.json')); TT = json.load(open('data/topic_trends.json'))
    HT = json.load(open('data/highlight_topics.json')); P = json.load(open('data/papers.json'))
    H = json.load(open('data/highlights.json')); AL = json.load(open('data/area_labels.json'))['labels']['2026']

    KO = {'A': 'LLM 추론·학습·RL 후처리', 'B': 'LLM 에이전트·도구·검색', 'C': '정렬·안전·해석', 'D': '효율 모델·시스템',
          'E': '멀티모달·비전-언어', 'F': '생성 모델', 'G': '컴퓨터 비전·3D', 'H': '강화학습·로보틱스', 'I': '학습 이론·최적화',
          'J': '확률·인과·통계', 'K': '의료·헬스케어', 'L': '과학·생물', 'M': '데이터셋·벤치마크', 'N': '기타 ML (그래프·시계열 등)'}
    LABEL = {'MCP (Model Context Protocol)': 'MCP', 'Tool use / function calling': 'Tool use', 'Deep research / search agents': 'Deep research',
             'Software engineering agents': 'SWE agents', 'Diffusion language models': 'Diffusion LM', 'Steering / activation editing': 'Activation steering',
             'Reinforcement learning w/ verifiable rewards (RLVR)': 'RLVR', 'Uncertainty / calibration (LLM)': 'LLM 불확실성', 'Reward hacking / deception': 'Reward hacking',
             'LLM agents / agentic': 'LLM agents', 'Agent memory': 'Agent memory', 'Interpretability / SAE': 'SAE·해석', 'Vision-language-action (VLA) / embodied': 'VLA',
             'Data selection / curation': '데이터 선별', 'State space / linear attention': 'SSM·linear attn', 'Formal math / theorem proving': '정리 증명',
             'Overthinking / efficient reasoning': '효율적 추론', '3D Gaussian splatting': '3DGS', 'Medical / clinical': '의료 키워드',
             'Multimodal LLM (MLLM/VLM)': 'MLLM', 'Benchmark / evaluation papers': '벤치마크', 'KV cache / long-context efficiency': 'KV cache',
             'Mixture of Experts': 'MoE', 'Personalization': '개인화', 'In-context learning': 'ICL', 'Reasoning models / long CoT': 'Long CoT',
             'Synthetic data': '합성 데이터', 'Graph neural networks': 'GNN', 'Federated learning': 'Federated', 'Differential privacy': 'DP',
             'Multi-agent systems': 'Multi-agent', 'Knowledge distillation': 'Distillation', 'Video generation': 'Video gen', 'Causal inference': 'Causal',
             'Time series foundation models': 'Time series', 'Protein / molecule': 'Protein·molecule'}

    areas = [dict(code=a['code'], name=KO[a['code']], n26=a['n2026'], n25=a['n2025'], s26=a['share2026'], s25=a['share2025'], growth=a['growth'],
                  diff=a['diff_pp'], se=a['se_pp'], clear=a['clear_change'], known=a['known'], hl=a['highlights'], oral=a['orals'], rate=a['hl_rate'])
             for a in AS['areas']]
    tr = {r['topic']: r for r in TT['rows']}
    topics, mcp = [], None
    for h in HT['topics']:
        t = tr[h['topic']]
        row = dict(topic=h['topic'], label=LABEL.get(h['topic'], h['topic']), s25=t['share2025'], s26=t['share2026'], growth=t['growth'],
                   n2025=t['n2025'], n2026=t['n2026'], known=h['n'], hl=h['highlights'], rate=h['rate'])
        if h['topic'].startswith('MCP'):
            mcp = row
        if h['n'] >= 40 and t['growth']:
            topics.append(row)

    M = [p for p in P if any(c.startswith('medical') for c in p['cats'])]; RG = [p for p in P if 'rag' in p['cats']]
    txt = lambda p: p['title'] + ' ' + p['abstract']
    MODS = {'EHR·임상 노트·ICU': r'\bEHRs?\b|electronic health|clinical notes?|\bICU\b', '병리': r'patholog|histolog|whole[- ]slide', '약물': r'\bdrug|pharmac|medication',
            '정신건강·상담': r'mental health|psychiatr|counsel|therap', '흉부 X선': r'chest X-?ray|\bCXR\b|radiograph', 'MRI': r'\bMRI\b|magnetic resonance',
            'CT': r'\bCT\b|computed tomography', 'ECG·EEG': r'\bECG\b|\bEEG\b|electrocardio', '내시경·수술': r'endoscop|surg', '안저·망막': r'fundus|retina'}
    modc = [(k, sum(1 for p in M if re.search(v, txt(p), re.I))) for k, v in MODS.items()]
    bench_med = sum(1 for p in M if re.search(r'bench|benchmark|dataset|evaluat|arena|testbed|gym', p['title'], re.I))


    def card(h):
        return dict(t=h['title'].replace('$\\chi$', 'χ').replace('$', ''), u=h['url'], d=h['decision'], k=h['summary_ko'], a=h['area'], s=h['in_scope'])


    MEDH = ['Incentivizing Medical Vision Capabilities', 'CRAFT: Causal Responsibility', 'STREAM: Stochastic Riemannian Flow Matching',
            'Entropy Minimization without Model Collapse', 'What do EEG Foundation Models Capture']
    data = dict(n6=AS['n2026'], n5=AS['n2025'], known=AS['known'], base=AS['base_rate'], n_hl=HT['n_highlight'], n_oral=HT['n_oral'],
                tracks=AS['tracks'], formats=AS['formats'], areas=areas, topics=topics, mcp=mcp,
                med_pool=[AS['med_llm_pool']['n2025'], AS['med_llm_pool']['n2026']],
                med_themes=[[t['theme'], t['n2025'], t['share2025'], t['n2026'], t['share2026']] for t in AS['med_themes']],
                n_med=len(M), n_rag=len(RG), cats=collections.Counter(c for p in P for c in p['cats']),
                subs=collections.Counter(p['rag_sub'] for p in RG), modc=modc, bench_med=bench_med,
                hl_scope=[card(h) for h in H if h['in_scope']],
                hl_med=[card(next(h for h in H if h['title'].startswith(s))) for s in MEDH],
                ex={c: [card(h) for h in H if h['decision'] == 'Oral' and AL.get(h['id']) == c][:6] for c in 'BAC'}, area_names=KO)
    return data
