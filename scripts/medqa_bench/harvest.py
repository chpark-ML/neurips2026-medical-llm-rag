"""Harvest arXiv titles+ids via OAI-PMH (sets cs and stat, records changed since 2025-01-01) into
arxiv_titles.jsonl. Resumable: the last resumption token per set is kept in harvest_state.json."""
import json, os, re, time, html, urllib.request, urllib.parse, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'arxiv_titles.jsonl'); ST = os.path.join(HERE, 'harvest_state.json')
UA = 'neurips2026-medical-llm-rag/0.1 (research survey; github.com/chpark-ML)'
BASE = 'https://oaipmh.arxiv.org/oai?'
state = json.load(open(ST)) if os.path.exists(ST) else {}


def get(url):
    for k in range(8):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=120).read().decode('utf-8', 'replace')
        except urllib.error.HTTPError as e:
            wait = int(e.headers.get('Retry-After') or 0) or 30 * (k + 1)
            print('HTTP', e.code, 'wait', wait, flush=True); time.sleep(wait)
        except Exception as e:
            print('ERR', str(e)[:80], flush=True); time.sleep(20)
    raise SystemExit('giving up')


for s in ('cs', 'stat'):
    if state.get(s) == 'done':
        continue
    tok = state.get(s); n = 0
    while True:
        url = BASE + (urllib.parse.urlencode({'verb': 'ListRecords', 'resumptionToken': tok}) if tok else
                      urllib.parse.urlencode({'verb': 'ListRecords', 'metadataPrefix': 'oai_dc', 'set': s, 'from': '2025-01-01'}))
        x = get(url)
        recs = re.findall(r'<record>(.*?)</record>', x, re.S)
        with open(OUT, 'a') as f:
            for r in recs:
                ident = re.search(r'<identifier>oai:arXiv.org:([^<]+)</identifier>', r)
                title = re.search(r'<dc:title>(.*?)</dc:title>', r, re.S)
                if ident and title:
                    f.write(json.dumps(dict(id=ident.group(1), title=html.unescape(re.sub(r'\s+', ' ', title.group(1)).strip()))) + '\n')
        n += len(recs)
        m = re.search(r'<resumptionToken[^>]*>([^<]*)</resumptionToken>', x)
        tok = m.group(1).strip() if m else ''
        state[s] = tok or 'done'; json.dump(state, open(ST, 'w'))
        print(s, n, time.strftime('%H:%M:%S'), flush=True)
        if not tok:
            break
        time.sleep(3)
open(os.path.join(HERE, 'HARVEST_DONE'), 'w').write(time.strftime('%F %T'))
print('done', flush=True)
