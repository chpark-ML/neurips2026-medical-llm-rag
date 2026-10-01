"""Stage 1: keyword pre-filter. Writes data/candidates.jsonl (high recall, low precision).
Stage 2 (not scripted): every candidate's title+abstract was read and labeled by an LLM
(two passes, see README §방법). The labels live in data/papers.json."""
import json, re
d = json.load(open('data/raw/neurips2026_posters.json'))
MED = re.compile(r'\b(medic\w*|clinic\w*|health\s?care|healthcare|biomedic\w*|patients?|hospital\w*|EHRs?|electronic health|radiolog\w*|patholog\w*|physician\w*|doctors?|nurs(e|es|ing)|surg(ery|ical|eon)\w*|MedQA|PubMedQA|MedMCQA|USMLE|oncolog\w*|psychiatr\w*|mental health|diagnos(is|tic|es))\b', re.I)
LLM = re.compile(r'\b(LLMs?|large language models?|language models?|MLLMs?|VLMs?|vision[- ]language|multimodal large|agents?|agentic|question[- ]answering|QA|VQA|chatbots?|foundation models?|GPT|reasoning models?|RAG|retrieval)\b', re.I)
RET = re.compile(r'(retriev\w*|\bRAG\b|\w*RAG\b|knowledge[- ]augmented|search[- ]augmented|deep research|agentic search|search agents?|web search|search engine)', re.I)
n = 0
with open('data/candidates.jsonl', 'w') as f:
    for x in d:
        t = x['name'] + ' . ' + x['abstract']
        m = bool(MED.search(t) and LLM.search(t)); r = bool(RET.search(t))
        if m or r:
            n += 1
            f.write(json.dumps(dict(id=x['virtualsite_url'].rsplit('/', 1)[-1], title=x['name'], hint=('MED ' if m else '') + ('RET' if r else '')), ensure_ascii=False) + '\n')
print(len(d), 'papers ->', n, 'candidates')
