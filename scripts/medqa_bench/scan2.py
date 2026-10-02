"""Second pass after arXiv's search API started refusing requests (HTTP 429).
Title -> arXiv id via OpenAlex, falling back to Semantic Scholar; PDF from export.arxiv.org.
Each service has its own throttle, and a small thread pool keeps all three busy.
Targets: pool papers not yet in results.jsonl, plus those results.jsonl marked no_arxiv_match.
Writes results2.jsonl (same record shape); a later record for an id supersedes an earlier one."""
import json, re, os, time, gzip, difflib, threading, urllib.request, urllib.parse, urllib.error
from concurrent.futures import ThreadPoolExecutor
import fitz
from scan import BRX, HERE, REPO, scan_text

OUT = os.path.join(HERE, 'results2.jsonl'); TXT = os.path.join(HERE, 'text')
UA = 'neurips2026-medical-llm-rag/0.1 (research survey; github.com/chpark-ML)'
norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())


class Throttle:
    def __init__(self, gap):
        self.gap, self.t, self.lock = gap, 0.0, threading.Lock()

    def wait(self):
        with self.lock:
            d = time.time() - self.t
            if d < self.gap:
                time.sleep(self.gap - d)
            self.t = time.time()


OA, S2, AX = Throttle(0.35), Throttle(3.2), Throttle(3.3)
wlock = threading.Lock()


def fetch(url, thr, binary=False, tries=4):
    for k in range(tries):
        thr.wait()
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=60).read()
            return r if binary else r.decode('utf-8', 'replace')
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(20 * (k + 1) if e.code in (429, 503) else 5)
        except Exception:
            time.sleep(5)
    return None


def openalex(title):
    q = urllib.parse.urlencode({'search': re.sub(r'[^\w\s-]', ' ', title), 'per-page': 5, 'select': 'title,locations'})
    js = fetch('https://api.openalex.org/works?' + q, OA)
    best = (0.0, None, None)
    for w in (json.loads(js).get('results', []) if js else []):
        ax = [l.get('landing_page_url') for l in (w.get('locations') or []) if 'arxiv.org/abs/' in (l.get('landing_page_url') or '')]
        sc = difflib.SequenceMatcher(None, norm(title), norm(w.get('title') or '')).ratio()
        if ax and sc > best[0]:
            best = (sc, ax[0].rsplit('/abs/', 1)[1], w.get('title'))
    return best


def s2(title):
    js = fetch('https://api.semanticscholar.org/graph/v1/paper/search/match?' + urllib.parse.urlencode({'query': title, 'fields': 'title,externalIds'}), S2)
    if not js:
        return (0.0, None, None)
    d = (json.loads(js).get('data') or [{}])[0]
    aid = (d.get('externalIds') or {}).get('ArXiv')
    sc = difflib.SequenceMatcher(None, norm(title), norm(d.get('title') or '')).ratio()
    return (sc, aid, d.get('title')) if aid else (0.0, None, None)


def work(x):
    i = x['virtualsite_url'].rsplit('/', 1)[-1]
    rec = dict(id=i, title=x['name'], abstract_hits=sorted(k for k, rx in BRX.items() if rx.search(x['name'] + ' ' + x['abstract'])))
    sc, aid, at = openalex(x['name']); src = 'openalex'
    if sc < 0.88 and os.environ.get('USE_S2') == '1':
        sc2, aid2, at2 = s2(x['name'])
        if sc2 > sc:
            sc, aid, at, src = sc2, aid2, at2, 's2'
    rec.update(arxiv_score=round(sc, 3), arxiv_title=at, lookup=src, s2_checked=os.environ.get('USE_S2') == '1')
    if sc >= 0.88 and aid:
        rec['arxiv_id'] = aid
        pdf = fetch('https://export.arxiv.org/pdf/' + re.sub(r'v\d+$', '', aid), AX, binary=True)
        if pdf and pdf[:4] == b'%PDF':
            try:
                doc = fitz.open(stream=pdf, filetype='pdf'); text = '\n'.join(pg.get_text() for pg in doc)
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
    with wlock:
        with open(OUT, 'a') as f:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')


def main():
    A = json.load(open(REPO + '/data/raw/neurips2026_posters.json'))
    AL = json.load(open(REPO + '/data/area_labels.json'))['labels']['2026']
    P = {p['id'] for p in json.load(open(REPO + '/data/papers.json'))}
    pid = lambda x: x['virtualsite_url'].rsplit('/', 1)[-1]
    LLM = re.compile(r'\b(LLMs?|large language models?|language models?|MLLMs?|VLMs?|LVLMs?|vision[- ]language models?|reasoning models?|GPT-?\w*|chatbots?)\b', re.I)
    pool = [x for x in A if LLM.search(x['name'] + ' ' + x['abstract']) or AL.get(pid(x)) == 'K' or pid(x) in P]
    first = {json.loads(l)['id']: json.loads(l)['status'] for l in open(os.path.join(HERE, 'results.jsonl'))}
    done2 = {json.loads(l)['id'] for l in open(OUT)} if os.path.exists(OUT) else set()
    if os.environ.get('USE_S2') == '1':  # slow pass: only papers every earlier lookup failed on
        last = {}
        for f in ('results.jsonl', 'results2.jsonl'):
            for l in open(os.path.join(HERE, f)):
                r = json.loads(l); last[r['id']] = r
        tried = {i for i, r in last.items() if r.get('lookup') == 's2' or r.get('s2_checked')}
        todo = [x for x in pool if last.get(pid(x), {}).get('status') == 'no_arxiv_match' and pid(x) not in tried]
    else:
        todo = [x for x in pool if pid(x) not in done2 and first.get(pid(x)) in (None, 'no_arxiv_match', 'download_failed', 'pdf_error')]
    print(f'pool {len(pool)}, first pass {len(first)}, todo {len(todo)}', flush=True)
    n = [0]
    def run(x):
        work(x); n[0] += 1
        if n[0] % 50 == 0:
            print(f'{n[0]}/{len(todo)} {time.strftime("%H:%M:%S")}', flush=True)
    with ThreadPoolExecutor(4) as ex:
        list(ex.map(run, todo))
    open(os.path.join(HERE, 'DONE3' if os.environ.get('USE_S2') == '1' else 'DONE2'), 'w').write(time.strftime('%F %T'))
    print('done', flush=True)


if __name__ == '__main__':
    main()
