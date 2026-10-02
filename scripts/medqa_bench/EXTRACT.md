You extract structured facts from NeurIPS 2026 papers about their use of medical question-answering benchmarks.

Input: the dossier files listed in LIST_PATH (one path per line). Each dossier holds the paper's abstract, the opening of the paper, table captions that name a benchmark, and passages around every mention of a medical QA benchmark (MedQA, MedMCQA, MedXpertQA, PubMedQA, MMLU medical subsets, USMLE, MedBullets, HealthBench, VQA-RAD, SLAKE, PathVQA, PMC-VQA, OmniMedVQA, etc.). Read every dossier fully with the Read tool. If a dossier is not enough to decide, you may read the paper's full text with `python3 -c "import gzip;print(gzip.open('TEXT_DIR/<id>.txt.gz','rt').read()[START:END])"` for the part you need.

For each paper output one JSON object:
- "id": the ID line of the dossier, verbatim.
- "used_in_experiments": true only if the paper itself runs an experiment (evaluation, training, or analysis) on at least one EXISTING, previously published medical QA benchmark (MedQA, MedMCQA, VQA-RAD, SlideBench, ...). A benchmark the paper itself introduces does NOT count. false if existing benchmarks are only cited (related work, motivation, a list of prior benchmarks, a comparison table of datasets).
- "own_benchmark": name of a medical QA benchmark/dataset this paper newly introduces, or "" if none. Fill this regardless of used_in_experiments.
- "benchmarks": the existing medical QA benchmarks the paper actually ran experiments on (not its own new benchmark). Use the names as written in the paper.
- "other_datasets": other datasets used in the same experiments, at most 5 (e.g. training data, non-medical benchmarks). Empty list if none.
- "models": the main models evaluated or trained (base models of the proposed method first, then the most important baselines), at most 6, names as written (e.g. "Qwen2.5-7B-Instruct", "GPT-4o").
- "training": one of "학습함 (SFT)", "학습함 (RL)", "학습함 (SFT+RL)", "학습함 (사전학습)", "학습함 (기타)", "학습 없음 (prompting·agent·추론 기법)", "평가만 (벤치마크·분석)". Choose by what the paper's own method does.
- "problem_ko": one Korean sentence (≤ 80 characters): what problem the paper tackles.
- "method_ko": one Korean sentence (≤ 90 characters): what the paper proposes or does. For a benchmark/analysis paper, what it measures.
- "role": one of "main" (medical QA is the paper's main target), "one_of_several" (medical QA is one of several evaluation domains), "analysis" (benchmarks are used only to analyze or probe models).
- "results": up to 4 headline numbers on medical QA benchmarks, each {"benchmark", "model", "setting", "metric", "value", "compared_to", "compared_value"}. "value" and "compared_value" must be copied character for character from the dossier or full text (e.g. "78.4", "62.10%"). "setting" says what produced the value (e.g. "proposed method", "zero-shot baseline"). "compared_to" names the baseline the paper compares against (or "" if none). Only include a number you can see next to its benchmark name; if no number is visible, give an empty list. Never compute or round numbers.

Rules settled on earlier papers (apply them):
- A dataset the authors rebuilt from an existing benchmark (rewritten questions, new options, converted episodes) counts as their own benchmark, not as the existing one.
- Scores the paper quotes from other papers or technical reports do not count; the authors must run the model themselves.
- A paper that only analyses reported scores without running any model is used_in_experiments=false.

When used_in_experiments is false: set benchmarks, other_datasets, models and results to [] and role to null, but still fill own_benchmark, training, problem_ko and method_ko.

Write all objects, one JSON per line, with the Write tool to OUT_PATH. Then validate with python3 that every line parses and the ids match the dossiers. Reply with the count of papers, how many have used_in_experiments=true, and how many results you extracted.
