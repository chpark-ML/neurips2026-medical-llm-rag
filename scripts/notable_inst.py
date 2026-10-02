"""Well-known institutions for the 'notable' section of med_datasets.html, and the rule that uses them.
A paper is selected when its FIRST or LAST author lists one of these institutions (the lead or, usually, the senior author)."""
import re

INST = [  # (display name, kind, pattern)
    ('Stanford', '대학', r'Stanford'), ('MIT', '대학', r'\bMIT\b|Massachusetts Institute of Technology'), ('Harvard', '대학', r'Harvard'),
    ('Carnegie Mellon', '대학', r'Carnegie Mellon|\bCMU\b'), ('UC Berkeley', '대학', r'Berkeley'), ('Princeton', '대학', r'Princeton'),
    ('Caltech', '대학', r'Caltech|California Institute of Technology'), ('Yale', '대학', r'\bYale\b'), ('Columbia', '대학', r'Columbia University'),
    ('Cornell', '대학', r'Cornell'), ('Univ. of Washington', '대학', r'University of Washington'), ('Johns Hopkins', '대학·병원', r'Johns Hopkins'),
    ('Duke', '대학', r'\bDuke\b'), ('UPenn', '대학', r'University of Pennsylvania|\bUPenn\b'), ('UChicago', '대학', r'University of Chicago'),
    ('UCLA', '대학', r'\bUCLA\b|University of California, Los Angeles'), ('UC San Diego', '대학', r'UC San Diego|University of California, San Diego|\bUCSD\b'),
    ('Univ. of Michigan', '대학', r'University of Michigan'), ('NYU', '대학', r'\bNYU\b|New York University'),
    ('Oxford', '대학', r'Oxford'), ('Cambridge', '대학', r'University of Cambridge'), ('Imperial College', '대학', r'Imperial College'),
    ('UCL', '대학', r'University College London|\bUCL\b'), ('ETH Zurich', '대학', r'\bETH\b|ETH Z'), ('EPFL', '대학', r'\bEPFL\b'),
    ('TU Munich', '대학', r'Technical University of Munich|Technische Universit\w+ M\w+nchen|\bTUM\b'),
    ('LMU Munich', '대학', r'Ludwig-Maximilians|\bLMU\b'), ('Max Planck', '연구소', r'Max Planck'),
    ('Univ. of Toronto', '대학', r'University of Toronto'), ('Vector Institute', '연구소', r'Vector Institute'), ('Mila', '연구소', r'\bMila\b'),
    ('McGill', '대학', r'McGill'), ('Tsinghua', '대학', r'Tsinghua'), ('Peking Univ.', '대학', r'Peking University'),
    ('Shanghai Jiao Tong', '대학', r'Shanghai Jiao Tong'), ('Zhejiang Univ.', '대학', r'Zhejiang University'), ('Fudan', '대학', r'Fudan'),
    ('Univ. of Tokyo', '대학', r'University of Tokyo'), ('KAIST', '대학', r'\bKAIST\b|Korea Advanced Institute of Science'),
    ('Seoul National Univ.', '대학', r'Seoul National University'), ('NUS', '대학', r'National University of Singapore|\bNUS\b'),
    ('HKUST', '대학', r'\bHKUST\b|Hong Kong University of Science'), ('HKU', '대학', r'University of Hong Kong'), ('CUHK', '대학', r'Chinese University of Hong Kong|\bCUHK\b'),
    ('RIKEN', '연구소', r'\bRIKEN\b'),
    ('Mayo Clinic', '병원', r'Mayo Clinic'), ('Mass General Brigham', '병원', r'Massachusetts General|Mass General|Brigham'),
    ('MD Anderson', '병원', r'MD Anderson'), ('Memorial Sloan Kettering', '병원', r'Memorial Sloan|\bMSK\b'), ('UCSF', '대학·병원', r'\bUCSF\b|University of California, San Francisco'),
    ('Cleveland Clinic', '병원', r'Cleveland Clinic'), ('Mount Sinai', '병원', r'Mount Sinai'), ('Charité', '병원', r'Charit'),
    ('Google / DeepMind', '기업', r'Google|DeepMind'), ('Microsoft', '기업', r'Microsoft'), ('Meta', '기업', r'\bMeta\b|\bFAIR\b'),
    ('OpenAI', '기업', r'OpenAI'), ('Anthropic', '기업', r'Anthropic'), ('NVIDIA', '기업', r'NVIDIA|Nvidia'), ('Apple', '기업', r'\bApple\b'),
    ('Amazon', '기업', r'Amazon'), ('IBM Research', '기업', r'\bIBM\b'), ('Alibaba', '기업', r'Alibaba'), ('Tencent', '기업', r'Tencent'),
    ('ByteDance', '기업', r'ByteDance'), ('Salesforce', '기업', r'Salesforce'), ('Samsung', '기업', r'Samsung'), ('Allen Institute for AI', '연구소', r'Allen Institute|\bAI2\b'),
]
RX = [(n, k, re.compile(p)) for n, k, p in INST]


def authors_with_affil(s):
    """Split 'Name (Affil), Name (Affil (Sub))' into [(name, affil)] respecting nested parentheses."""
    out, depth, name, aff = [], 0, '', ''
    for ch in s:
        if ch == '(':
            depth += 1
            if depth == 1:
                continue
        if ch == ')':
            depth -= 1
            if depth == 0:
                continue
        if depth >= 1:
            aff += ch
        elif ch == ',':
            if name.strip():
                out.append((name.strip(), aff.strip()))
            name, aff = '', ''
        else:
            name += ch
    if name.strip():
        out.append((name.strip(), aff.strip()))
    return out


def match(aff):
    return [(n, k) for n, k, r in RX if r.search(aff or '')]


def notable(authors_str):
    """Return dict(first=..., last=..., hits=[(role, author, inst, kind)]) or None if neither lead nor senior author matches."""
    au = authors_with_affil(authors_str)
    if not au:
        return None
    hits = []
    for role, (nm, aff) in (('제1저자', au[0]), ('교신·마지막 저자', au[-1])) if len(au) > 1 else (('제1저자', au[0]),):
        for inst, kind in match(aff):
            hits.append((role, nm, inst, kind))
    return dict(hits=hits, n_authors=len(au)) if hits else None
