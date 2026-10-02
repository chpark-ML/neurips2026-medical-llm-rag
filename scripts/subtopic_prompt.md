You are building browsing tags for NeurIPS 2026 papers in one research area: AREA_NAME (N_PAPERS papers).

Input: DIR/input.tsv — lines "id<TAB>title<TAB>first 300 characters of the abstract". Read EVERY line with the Read tool (chunks of ~150 lines). Judge by reading; do not tag with a keyword script.

Step 1. Define 8–15 sub-topics that together cover this area's papers well. Each sub-topic is a short English noun phrase a researcher would search for (2–4 words, e.g. "Diffusion sampling acceleration", "Gaussian splatting", "Federated learning"). Make them specific enough to be useful but each should hold at least ~15 papers. Add one sub-topic "Other" for papers that fit none.
Step 2. Give every paper 1 or 2 sub-topics (the best fit first).

Keep every intermediate file only inside DIR (other agents run in parallel). Write DIR/tags.tsv with one line per input line, same order: "id<TAB>tag1" or "id<TAB>tag1;tag2", ids copied verbatim from the input. Write DIR/vocab.json as {"subtopics": ["...", ...]} (the exact tag strings used, including "Other").
Validate with python3: tags.tsv has the same number of lines and the same ids in the same order as input.tsv, every tag is in vocab.json, each line has 1–2 tags. Reply with the sub-topic list and the count of papers per sub-topic (counting the first tag only).
