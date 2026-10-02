import json,re,collections
# curated topic lexicon: topic -> regex over title+abstract
T={
 'LLM agents / agentic':r'\bagent(s|ic)?\b',
 'Multi-agent systems':r'multi-?agent',
 'Reinforcement learning w/ verifiable rewards (RLVR)':r'\bRLVR\b|verifiable reward',
 'GRPO':r'\bGRPO\b',
 'Reasoning models / long CoT':r'reasoning model|long[- ]CoT|chain[- ]of[- ]thought|\bCoT\b',
 'Test-time scaling / compute':r'test[- ]time (scaling|compute)|inference[- ]time (scaling|compute)',
 'Overthinking / efficient reasoning':r'overthink|efficient reasoning|reasoning efficiency|adaptive thinking|token budget',
 'Diffusion language models':r'diffusion (large )?language model|\bdLLMs?\b|masked diffusion model',
 'Tool use / function calling':r'tool[- ](use|calling|learning|augmented)|function[- ]calling',
 'MCP (Model Context Protocol)':r'\bMCP\b|model context protocol',
 'Computer-use / GUI / web agents':r'\bGUI\b|computer[- ]use|web agent|browser agent|OS agent',
 'Software engineering agents':r'SWE-?bench|software engineering agent|coding agent|code agent',
 'Deep research / search agents':r'deep research|search agent|agentic search|search-r1',
 'RAG':r'retrieval[- ]augmented|\bRAG\b|\w+RAG\b',
 'Agent memory':r'(agent|long[- ]term|episodic) memory|memory (system|mechanism|bank|module)s? for (llm|agent)',
 'Self-evolving / self-improving':r'self[- ](evolv|improv)',
 'Reward models / LLM-as-a-judge':r'reward model|LLM[- ]as[- ]a[- ]judge|\bjudge model|generative verifier|process reward',
 'Process reward models (PRM)':r'process reward|\bPRMs?\b',
 'Hallucination':r'hallucinat',
 'Uncertainty / calibration (LLM)':r'uncertainty (quantification|estimation)|calibrat',
 'Jailbreak / red teaming':r'jailbreak|red[- ]team',
 'Interpretability / SAE':r'sparse autoencoder|\bSAEs?\b|mechanistic interpretab|circuit',
 'Steering / activation editing':r'steering vector|activation steering|representation engineering|\bsteer(ing)?\b',
 'Reward hacking / deception':r'reward hacking|deceptive|deception|sandbagging|scheming|sycophan',
 'Unlearning':r'unlearn',
 'Watermarking':r'watermark',
 'KV cache / long-context efficiency':r'KV[- ]cache|long[- ]context',
 'Speculative decoding':r'speculative decoding',
 'Quantization':r'quantiz',
 'Mixture of Experts':r'mixture[- ]of[- ]experts|\bMoE\b',
 'State space / linear attention':r'state[- ]space model|\bmamba\b|linear attention',
 'Vision-language-action (VLA) / embodied':r'vision[- ]language[- ]action|\bVLAs?\b|embodied',
 'World models':r'world model',
 'Video generation':r'video generation|video diffusion|text-to-video',
 'Flow matching':r'flow matching|rectified flow',
 '3D Gaussian splatting':r'gaussian splatting|\b3DGS\b',
 'Multimodal LLM (MLLM/VLM)':r'\bMLLMs?\b|multimodal large language|\bVLMs?\b|vision[- ]language model|\bLVLMs?\b',
 'Unified multimodal understanding+generation':r'unified (multimodal )?(model|understanding and generation)|any-to-any',
 'Scientific discovery / AI scientist':r'AI scientist|scientific discovery|automated research|research agent',
 'Formal math / theorem proving':r'theorem prov|\bLean\b|formal(ization| proof| math)',
 'Benchmark / evaluation papers':r'\bbenchmark\b',
 'Synthetic data':r'synthetic data',
 'Data selection / curation':r'data (selection|curation|mixture|filtering)',
 'Federated learning':r'federated',
 'Differential privacy':r'differential(ly)? priva',
 'Graph neural networks':r'graph neural|\bGNNs?\b',
 'Time series foundation models':r'time[- ]series',
 'Protein / molecule':r'protein|molecul',
 'Medical / clinical':r'\b(medical|clinical|healthcare|patients?|radiolog\w*|patholog\w*|EHR)\b',
 'Medical QA':r'(medical|clinical|biomedical)[- ](question|QA|VQA|exam)|MedQA|USMLE|MedMCQA|PubMedQA',
 'Causal inference':r'causal',
 'Continual learning':r'continual|lifelong',
 'Model merging':r'model merging|merg(e|ing) models',
 'Knowledge distillation':r'distill',
 'In-context learning':r'in[- ]context learning',
 'Personalization':r'personaliz',
 'Pluralistic / cultural alignment':r'pluralis|cultur',
 'Agent safety / guardrails':r'agent(ic)? safety|guardrail|prompt injection',
}
if __name__ == '__main__':
    a26=json.load(open('data/raw/neurips2026_posters.json')); a25=json.load(open('data/raw/neurips2025_posters.json'))
    def rate(D,rx):
        r=re.compile(rx,re.I); return sum(1 for x in D if r.search(x['name']+' '+x['abstract']))
    rows=[]
    for k,rx in T.items():
        c26=rate(a26,rx); c25=rate(a25,rx)
        p26=c26/len(a26)*100; p25=c25/len(a25)*100
        rows.append(dict(topic=k,n2026=c26,n2025=c25,share2026=round(p26,2),share2025=round(p25,2),growth=round(p26/p25,2) if p25 else None))
    rows.sort(key=lambda r:-(r['growth'] or 99))
    for r in rows: print(f"{r['topic'][:48]:48} 25:{r['n2025']:5} ({r['share2025']:5.2f}%) 26:{r['n2026']:5} ({r['share2026']:5.2f}%) x{r['growth']}")
    # title-only counts for terms quoted in the README notes
    TT={'evidence':r'\bevidence\b','audit / auditing':r'\baudit(s|ing|ed)?\b','diagnosing / diagnostic':r'\bdiagnos(ing|tic)\b',
     'long-horizon':r'long-horizon','longitudinal':r'\blongitudinal\b','credit assignment':r'credit assignment','agent memory':r'agent memory',
     'skill(s)':r'\bskills?\b','self-evolving':r'self-evolving','on-policy distillation':r'on-policy distillation','self-distillation':r'self-distillation','RLVR':r'\bRLVR\b'}
    def tcount(D,rx):
        r=re.compile(rx,re.I); return sum(1 for x in D if r.search(x['name']))
    title_terms=[dict(term=k,n2025=tcount(a25,rx),n2026=tcount(a26,rx)) for k,rx in TT.items()]
    for t in title_terms: print('title:',t)
    json.dump(dict(N2026=len(a26),N2025=len(a25),rows=rows,title_terms=title_terms),open('data/topic_trends.json','w'),indent=1)
