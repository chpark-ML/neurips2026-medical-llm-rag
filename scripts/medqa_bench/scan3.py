"""Third pass: match titles locally against the OAI-PMH harvest (arxiv_titles.jsonl), then download PDFs.
Targets: pool papers with no record yet, or whose latest record is no_arxiv_match / download_failed / pdf_error.
Writes results3.jsonl."""
import json, re, os, time, gzip, difflib, collections, urllib.request, urllib.error
import fitz
from scan import BRX, HERE, REPO, scan_text

OUT = os.path.join(HERE, 'results3.jsonl'); TXT = os.path.join(HERE, 'text')
UA = 'neurips2026-medical-llm-rag/0.1 (research survey; github.com/chpark-ML)'
norm = lambda s: re.sub(r'[^a-z0-9]', '', re.sub(r'\$[^$]*\$', '', s.lower()))
toks = lambda s: [w for w in re.findall(r'[a-z0-9]+', s.lower()) if len(w) > 3][:3]
last_t = [0.0]


def pdf_get(aid, tries=5):
    for k in range(tries):
        d = time.time() - last_t[0]
        if d < 3.3:
            time.sleep(3.3 - d)
        last_t[0] = time.time()
        try:
            return urllib.request.urlopen(urllib.request.Request('https://export.arxiv.org/pdf/' + aid, headers={'User-Agent': UA}), timeout=90).read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(int(e.headers.get('Retry-After') or 0) or 30 * (k + 1))
        except Exception:
            time.sleep(10)
    return None


def main():
    exact, by_tok = {}, collections.defaultdict(list)
    for l in open(os.path.join(HERE, 'arxiv_titles.jsonl')):
        r = json.loads(l); n = norm(r['title'])
        exact.setdefault(n, r['id'])
        t = toks(r['title'])
        if t:
            by_tok[t[0]].append((n, r['id'], r['title']))
    print('harvested titles', len(exact), flush=True)
    A = json.load(open(REPO + '/data/raw/neurips2026_posters.json'))
    AL = json.load(open(REPO + '/data/area_labels.json'))['labels']['2026']
    P = {p['id'] for p in json.load(open(REPO + '/data/papers.json'))}
    pid = lambda x: x['virtualsite_url'].rsplit('/', 1)[-1]
    LLM = re.compile(r'\b(LLMs?|large language models?|language models?|MLLMs?|VLMs?|LVLMs?|vision[- ]language models?|reasoning models?|GPT-?\w*|chatbots?)\b', re.I)
    pool = [x for x in A if LLM.search(x['name'] + ' ' + x['abstract']) or AL.get(pid(x)) == 'K' or pid(x) in P]
    last = {}
    for fn in ('results.jsonl', 'results2.jsonl', 'results3.jsonl'):
        if os.path.exists(os.path.join(HERE, fn)):
            for l in open(os.path.join(HERE, fn)):
                r = json.loads(l); last[r['id']] = r
    done3 = {json.loads(l)['id'] for l in open(OUT)} if os.path.exists(OUT) else set()
    todo = [x for x in pool if pid(x) not in done3 and last.get(pid(x), {}).get('status') in (None, 'no_arxiv_match', 'download_failed', 'pdf_error')]
    matched = 0
    plan = []
    for x in todo:
        n = norm(x['name']); aid, sc, at = exact.get(n), 1.0, None
        if not aid:
            t = toks(x['name']); best = (0.0, None, None)
            for cn, cid, ct in (by_tok.get(t[0], []) if t else []):
                if abs(len(cn) - len(n)) > 0.25 * len(n):
                    continue
                s = difflib.SequenceMatcher(None, n, cn).ratio()
                if s > best[0]:
                    best = (s, cid, ct)
            sc, aid, at = best
        plan.append((x, aid if sc >= 0.9 else None, round(sc, 3), at))
        matched += sc >= 0.9 and aid is not None
    print(f'todo {len(todo)}, matched locally {matched}', flush=True)
    for k, (x, aid, sc, at) in enumerate(plan, 1):
        i = pid(x)
        rec = dict(id=i, title=x['name'], abstract_hits=sorted(kk for kk, rx in BRX.items() if rx.search(x['name'] + ' ' + x['abstract'])),
                   arxiv_score=sc, arxiv_title=at, lookup='oai-harvest')
        if aid:
            rec['arxiv_id'] = aid
            pdf = pdf_get(aid)
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
        with open(OUT, 'a') as f:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
        if k % 50 == 0:
            print(f'{k}/{len(plan)} {time.strftime("%H:%M:%S")}', flush=True)
    open(os.path.join(HERE, 'DONE3'), 'w').write(time.strftime('%F %T'))
    print('done', flush=True)


if __name__ == '__main__':
    main()
