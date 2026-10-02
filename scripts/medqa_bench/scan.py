"""Find NeurIPS 2026 papers whose full text (arXiv version) mentions medical QA benchmarks.
Resumable: every processed paper is appended to results.jsonl; rerunning skips those ids.
arXiv asks for at most one request every 3 seconds; every request here goes through wait()."""
import json, re, os, sys, time, gzip, difflib, urllib.request, urllib.parse, urllib.error
import fitz

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
OUT = os.path.join(HERE, 'results.jsonl'); TXT = os.path.join(HERE, 'text'); os.makedirs(TXT, exist_ok=True)
UA = 'neurips2026-medical-llm-rag/0.1 (research survey; contact via github.com/chpark-ML)'

BENCH = {
    'MedQA': r'\bMedQA\b', 'MedMCQA': r'\bMedMCQA\b', 'MedXpertQA': r'\bMedXpert-?QA\b', 'PubMedQA': r'\bPubMedQA\b',
    'MMLU (medical)': r'\bMMLU[- ]?(?:Med(?:ical)?|clinical|Pro[- ]?Health)\b|MMLU[^.\n]{0,40}\b(?:clinical knowledge|medical genetics|college medicine|professional medicine)\b',
    'USMLE': r'\bUSMLE\b', 'MedBullets': r'\bMed[Bb]ullets\b', 'HealthBench': r'\bHealthBench\b', 'BioASQ': r'\bBioASQ\b',
    'MedExQA': r'\bMedExQA\b', 'HEAD-QA': r'\bHEAD-?QA\b', 'CMExam': r'\bCMExam\b', 'MedCalc-Bench': r'\bMedCalc(?:-?Bench)?\b',
    'MedConceptsQA': r'\bMedConceptsQA\b', 'AfriMed-QA': r'\bAfriMed-?QA\b', 'KorMedMCQA': r'\bKorMedMCQA\b', 'IgakuQA': r'\bIgakuQA\b',
    'MetaMedQA': r'\bMetaMedQA\b', 'MedHELM': r'\bMedHELM\b', 'MedAgentBench': r'\bMedAgentBench\b', 'AgentClinic': r'\bAgentClinic\b',
    'JAMA Clinical Challenge': r'\bJAMA Clinical Challenge\b', 'NEJM Image Challenge': r'\bNEJM\b[^.\n]{0,30}\bChallenge\b',
    'VQA-RAD': r'\bVQA-?RAD\b', 'SLAKE': r'\bSLAKE\b', 'PathVQA': r'\bPath-?VQA\b', 'PMC-VQA': r'\bPMC-?VQA\b',
    'OmniMedVQA': r'\bOmniMedVQA\b', 'MMMU (medical)': r'\bMMMU[^.\n]{0,30}\b(?:Health|Medicine|Med)\b|\bMMMU-Med\b',
    'MedFrameQA': r'\bMedFrameQA\b', 'GMAI-MMBench': r'\bGMAI-?MMBench\b', 'MedTrinity': r'\bMedTrinity\b',
}
BRX = {k: re.compile(v) for k, v in BENCH.items()}
STOP = set('a an the of for and in on with via to from by is are as at into towards toward beyond under over using through without when what how why do does can we our it be not your more less than vs'.split())
norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
last = [0.0]


def wait():
    d = time.time() - last[0]
    if d < 3.2:
        time.sleep(3.2 - d)
    last[0] = time.time()


def get(url, binary=False, tries=4):
    for k in range(tries):
        wait()
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            r = urllib.request.urlopen(req, timeout=60).read()
            return r if binary else r.decode('utf-8', 'replace')
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                time.sleep(30 * (k + 1)); continue
            if e.code == 404:
                return None
            time.sleep(10)
        except Exception:
            time.sleep(10)
    return None


def search(title):
    words = [w for w in re.findall(r'[a-z0-9]+', re.sub(r'\$[^$]*\$', ' ', title.lower())) if w not in STOP and len(w) > 2]
    best = (0.0, None, None)
    for ws in (words[:8], words[:4]):
        if not ws:
            continue
        q = ' AND '.join('ti:' + w for w in ws)
        xml = get('http://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': q, 'max_results': 5}))
        if xml is None:
            continue
        for e in re.findall(r'<entry>(.*?)</entry>', xml, re.S):
            t = re.sub(r'\s+', ' ', re.search(r'<title>(.*?)</title>', e, re.S).group(1)).strip()
            aid = re.search(r'<id>https?://arxiv.org/abs/([^<]+)</id>', e).group(1)
            sc = difflib.SequenceMatcher(None, norm(title), norm(t)).ratio()
            if sc > best[0]:
                best = (sc, aid, t)
        if best[0] >= 0.88:
            break
    return best


def scan_text(text):
    hits = {}
    flat = re.sub(r'\s+', ' ', text)
    for k, rx in BRX.items():
        ms = list(rx.finditer(flat))
        if ms:
            hits[k] = dict(count=len(ms), snippets=[flat[max(0, m.start() - 220):m.end() + 220] for m in ms[:4]])
    return hits


def main():
    A = json.load(open(REPO + '/data/raw/neurips2026_posters.json'))
    AL = json.load(open(REPO + '/data/area_labels.json'))['labels']['2026']
    P = {p['id'] for p in json.load(open(REPO + '/data/papers.json'))}
    pid = lambda x: x['virtualsite_url'].rsplit('/', 1)[-1]
    LLM = re.compile(r'\b(LLMs?|large language models?|language models?|MLLMs?|VLMs?|LVLMs?|vision[- ]language models?|reasoning models?|GPT-?\w*|chatbots?)\b', re.I)
    pool = [x for x in A if LLM.search(x['name'] + ' ' + x['abstract']) or AL.get(pid(x)) == 'K' or pid(x) in P]
    pool.sort(key=lambda x: (0 if (pid(x) in P or AL.get(pid(x)) == 'K') else 1, pid(x)))
    done = set()
    if os.path.exists(OUT):
        done = {json.loads(l)['id'] for l in open(OUT)}
    print(f'pool {len(pool)}, done {len(done)}', flush=True)
    for n, x in enumerate(pool, 1):
        i = pid(x)
        if i in done:
            continue
        rec = dict(id=i, title=x['name'], abstract_hits=sorted(k for k, rx in BRX.items() if rx.search(x['name'] + ' ' + x['abstract'])))
        sc, aid, at = search(x['name'])
        rec.update(arxiv_score=round(sc, 3), arxiv_title=at)
        if sc >= 0.88 and aid:
            rec['arxiv_id'] = aid
            pdf = get('https://export.arxiv.org/pdf/' + re.sub(r'v\d+$', '', aid), binary=True)
            if pdf and pdf[:4] == b'%PDF':
                try:
                    doc = fitz.open(stream=pdf, filetype='pdf')
                    text = '\n'.join(pg.get_text() for pg in doc)
                    rec['pages'] = doc.page_count
                    with gzip.open(os.path.join(TXT, i + '.txt.gz'), 'wt') as f:
                        f.write(text)
                    rec['hits'] = scan_text(text); rec['status'] = 'fulltext'
                except Exception as e:
                    rec['status'] = 'pdf_error'; rec['error'] = str(e)[:200]
            else:
                rec['status'] = 'download_failed'
        else:
            rec['status'] = 'no_arxiv_match'
        with open(OUT, 'a') as f:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
        if n % 25 == 0:
            print(f'{n}/{len(pool)} {time.strftime("%H:%M:%S")}', flush=True)
    open(os.path.join(HERE, 'DONE'), 'w').write(time.strftime('%F %T'))
    print('done', flush=True)


if __name__ == '__main__':
    main()
