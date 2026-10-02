"""Check extracted numbers against the paper text: a result is kept only if its value string
(and its compared_value, when given) occurs in the full text. Usage: verify.py extract/*.jsonl"""
import json, re, os, gzip, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__))


def present(v, text):
    v = (v or '').strip()
    if not v:
        return True
    core = re.sub(r'[%\s]', '', v)
    return bool(core) and re.search(r'(?<![\d.])' + re.escape(core) + r'(?![\d])', text) is not None


def main(paths):
    rows = []
    for p in paths:
        rows += [json.loads(l) for l in open(p) if l.strip()]
    tot = ok = 0
    for r in rows:
        f = os.path.join(HERE, 'text', r['id'] + '.txt.gz')
        text = re.sub(r'\s+', ' ', gzip.open(f, 'rt').read()) if os.path.exists(f) else ''
        for x in r.get('results', []):
            tot += 1
            x['verified'] = bool(text) and present(x.get('value'), text) and present(x.get('compared_value'), text)
            ok += x['verified']
    print(f'{len(rows)} papers, {sum(r["used_in_experiments"] for r in rows)} used in experiments, results verified {ok}/{tot}')
    return rows


if __name__ == '__main__':
    rows = main(sys.argv[1:] or sorted(glob.glob(os.path.join(HERE, 'extract', 'b*.jsonl'))))
    for r in rows:
        for x in r.get('results', []):
            if not x['verified']:
                print('  UNVERIFIED', r['id'], x)
