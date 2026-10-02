# Medical QA benchmark full-text scan

Run from this directory with PyMuPDF installed (`pip install pymupdf`). Working files (PDF text, results) stay here and are gitignored.

1. `scan.py` — title → arXiv id through the arXiv search API, then PDF → text → benchmark-name search. arXiv started answering HTTP 429 after ~570 papers.
2. `scan2.py` — the same through OpenAlex (and Semantic Scholar with `USE_S2=1`). Both also answered 429 soon after.
3. `harvest.py` → `scan3.py` — what finished the job: bulk-download arXiv titles via OAI-PMH (sets cs, stat, since 2025-01-01; ~405k records), match titles locally, download PDFs.
4. `dossier.py` — per paper with a benchmark mention: abstract, opening, table captions and passages around every mention.
5. LLM agents read each dossier with `EXTRACT.md` (whether the benchmark was used in experiments, benchmarks, models, training, problem, method, headline numbers).
6. `verify.py` — keeps a number only if it occurs verbatim in the paper's full text. `assemble.py` writes `data/medqa_benchmark_papers.json`.
