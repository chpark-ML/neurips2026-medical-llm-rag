# NeurIPS 2026 관심 분야 상세 리포트

> 요약과 웹 페이지 링크는 [README](README.md)에 있다. 이 문서는 표와 목록을 모두 담은 상세판이다.

NeurIPS 2026 채택 논문 **9,094편** 중, 아래 다섯 주제 중 하나 이상을 핵심 기여로 다룬 논문 **216편**을 모았다. 키워드 트렌드 분석(2025 대비)과 다음 연구 주제 제안, Medical QA 연구 아이디어를 함께 정리했다.

> **웹 페이지 (휴대폰에서도 열림)** — 다섯 페이지는 서로 독립적이다.
>
> - [관심 분야 리포트](https://chpark-ml.github.io/neurips2026-medical-llm-rag/interests.html): 학회 전체 → 분야 → 트렌드 → 의료·RAG 순서의 분석, 관심 분야 216편, on-policy·self-distillation 74편, 의료 QA 벤치마크 실험 논문, 하이라이트, 연구 제안
> - [NeurIPS 2026 논문 탐색기](https://chpark-ml.github.io/neurips2026-medical-llm-rag/explorer.html): 학회 전체 9,094편을 분야·세부 주제(212개)·키워드·발표 형식·트랙으로 걸러 보기 (관심 분야와 무관한 전체 보기)
> - [Medical QA 연구 지도](https://chpark-ml.github.io/neurips2026-medical-llm-rag/medical_qa.html): Medical QA 논문 30편을 큰 갈래 5개 → 세부 갈래 11개로 나눈 연구 흐름
> - [On-policy·Self-distillation 연구 지도](https://chpark-ml.github.io/neurips2026-medical-llm-rag/opsd.html): 74편을 큰 갈래 6개 → 세부 갈래 20개로 나눈 연구 흐름
>
> NeurIPS 2026 전체의 Oral·Spotlight 논문은 [`HIGHLIGHTS.md`](HIGHLIGHTS.md)에 분야별로 정리했다.

## 한눈에 보기

| 분류 | 편수 | 기준 |
|---|---:|---|
| Medical QA | 25 | 의료·임상·생의학 질의응답, medical VQA, 시험형 QA, 임상 추론 QA |
| Medical RAG | 5 | 의료 도메인의 검색증강 생성·지식 검색 |
| Medical Agent | 26 | 의료 환경의 LLM/VLM 에이전트, 멀티에이전트 진단, 임상 워크플로 벤치마크 |
| Medical LLM / VLM | 70 | 의료용 언어·비전-언어 모델의 학습·정렬·안전·평가·리포트 생성 |
| RAG | 122 | 모든 도메인의 RAG: 방법, GraphRAG, 멀티모달 RAG, 보안, 벤치마크, 효율, agentic search |
| **의료 관련 전체 (위 4개 의료 분류의 합집합)** | **100** | |
| **전체 (중복 제거)** | **216** | 한 논문이 여러 분류에 속할 수 있어 분류별 합계보다 작다 |

RAG 122편의 세부 유형:

| RAG 유형 | 편수 |
|---|---:|
| Agentic search / Deep research | 31 |
| RAG 방법론 | 25 |
| GraphRAG / KG | 13 |
| Multimodal RAG | 10 |
| 강건성·보안·프라이버시 | 10 |
| 벤치마크·평가 | 17 |
| 효율 (KV cache·압축·지연) | 6 |
| 기타 (비텍스트 생성 등) | 10 |

## 어떻게 모았나 (그리고 한계)

1. **원천 데이터**: neurips.cc 공식 다운로드(`/Downloads/2026`)의 포스터 목록 9,094편(제목·저자·초록). 비교용 2025년 목록 5,860편. 2026 목록은 Main·Evaluations & Datasets·Position·Journal 트랙을 포함한다.
2. **1차 후보 추출**: 의료 용어 × LLM/에이전트 용어, 또는 retrieval/RAG/search 용어가 제목·초록에 있는 논문 1,103편 (`scripts/candidates.py`).
3. **분류**: 후보 1,103편 전부의 제목·초록을 LLM(Claude)이 읽고 핵심 기여 기준으로 분류. 지나가듯 언급하거나 RAG를 baseline으로만 쓴 논문은 제외. 이어 제외된 논문 중 신호가 강한 167편을 초록 전문으로 다시 읽는 2차 재검토로 17편을 추가했고, 경계 사례는 직접 읽어 2편을 더하고 1편을 뺐다.
4. **발표 형식(Oral/Spotlight/Poster)과 트랙**은 neurips.cc의 orals-posters JSON에서 붙였다. 이 JSON은 받을 때마다 일부만 담겨 있어(2026-10-01 5,547편, 10-02 5,896편) 두 스냅샷을 합쳤고, 그래도 이 목록 216편 중 34편은 발표 형식을 알 수 없다(`scripts/decisions.py`).

5. **분야 분포**: 2026년 9,094편과 2025년 5,860편 전부에 LLM이 제목만 보고 14개 분야 중 하나를 배정했다(`scripts/area_prompt.md`, 약 1,000편씩 14묶음). 묶음마다 분야 비중이 조금씩 달라서, 그 흩어짐으로 오차를 어림하고 오차의 두 배보다 큰 변화만 증가·감소로 본다(`scripts/areas.py`). 검증으로, 위 의료 논문 100편 중 87편이 의료·헬스케어로 배정됐다.
6. **키워드 정규식**: MCP, LLM 불확실성·calibration, LLM 에이전트, activation steering은 다른 뜻까지 잡던 정규식을 좁혔다(예: `calibrat` 단독 → LLM 용어가 함께 있어야 매칭).

**한계**: 분류는 사람 검수가 아닌 LLM 판독이라 경계 사례(예: 단백질 언어모델 + retrieval, 의료가 여러 응용 중 하나인 논문)는 기준에 따라 달라질 수 있다. 순수 검색·임베딩 논문(생성 없음)과 LLM이 없는 의료 영상·EHR 예측 모델은 의도적으로 제외했다. 한 줄 요약은 초록 기반 자동 요약이다.

## 학회 전체는 어떻게 나뉘나 (14개 분야)

모든 논문의 분야 비중(전체 중 %)을 2025년과 비교했다. '변화'는 오차(±2 표준오차)보다 큰 경우에만 숫자로 적었다. 하이라이트 비율은 발표 형식을 아는 7,688편 기준이고, 기준선은 5.27%다. 더 자세한 그림은 [관심 분야 리포트](https://chpark-ml.github.io/neurips2026-medical-llm-rag/interests.html#l1).

| 분야 | 2025 비중 | 2026 비중 (편수) | 변화 | 하이라이트 비율 (95% 구간) |
|---|---:|---:|---:|---:|
| 기타 ML (그래프·시계열 등) | 11.69% | 9.76% (888) | -1.9%p | 4.94% (3.62–6.7%) |
| 정렬·안전·해석 | 8.84% | 9.26% (842) | 비슷 | 6.35% (4.75–8.45%) |
| 강화학습·로보틱스 | 8.34% | 8.35% (759) | 비슷 | 4.39% (3.05–6.27%) |
| LLM 추론·학습·RL 후처리 | 8.86% | 8.29% (754) | 비슷 | 3.53% (2.34–5.28%) |
| 생성 모델 | 8.07% | 8.15% (741) | 비슷 | 5.36% (3.86–7.4%) |
| 학습 이론·최적화 | 9.81% | 7.7% (700) | -2.1%p | 7.99% (6.06–10.47%) |
| 컴퓨터 비전·3D | 9.88% | 7.55% (687) | -2.3%p | 5.72% (4.1–7.92%) |
| 과학·생물 | 6.91% | 7.18% (653) | 비슷 | 8.87% (6.79–11.5%) |
| LLM 에이전트·도구·검색 | 2.99% | 6.83% (621) | +3.8%p | 4.36% (2.92–6.45%) |
| 데이터셋·벤치마크 | 4.35% | 6.52% (593) | 비슷 | 4.66% (3.12–6.89%) |
| 효율 모델·시스템 | 6.19% | 6.43% (585) | 비슷 | 3.54% (2.25–5.52%) |
| 확률·인과·통계 | 5.77% | 6.05% (550) | 비슷 | 4.17% (2.71–6.35%) |
| 멀티모달·비전-언어 | 6.08% | 5.14% (467) | 비슷 | 5.51% (3.67–8.21%) |
| 의료·헬스케어 | 2.22% | 2.79% (254) | +0.6%p | 1.94% (0.76–4.89%) |

- 확실히 커진 분야는 LLM 에이전트·도구·검색(비중 ×2.3)이고, 의료·헬스케어도 작게 늘었다. 컴퓨터 비전·3D, 학습 이론, 기타 ML은 편수는 늘었지만 비중은 줄었다.
- 하이라이트 비율은 과학·생물과 학습 이론이 기준선보다 높고, 의료·헬스케어가 가장 낮다. "데이터셋·벤치마크" 분야는 묶음 사이 편차가 커서(2.3–10.5%) 해석하지 않는다.

## 관심 분야별 연구 흐름

각 분야의 논문을 읽고 여러 논문이 함께 움직이는 방향과 그 방향이 붙잡은 문제를 한 줄씩 적었다. 괄호의 편수는 그 흐름에 주로 속하는 논문 수를 판독으로 어림한 값이고, 링크는 대표 논문이다. RAG와 의료 세 분야는 위 216편 목록, LLM 에이전트와 LLM은 학회 전체에서 해당 분야로 배정된 논문이 대상이다.

### RAG (122편 · 216편 목록의 RAG)

RAG가 단발 검색에서 RL로 학습된 장기 agentic search·deep research로 이동하며, 멀티모달 확장과 신뢰성·보안·효율이 함께 과제로 부상

- 텍스트 RAG를 시각 문서·비디오·이미지 생성으로 넓히며, 시각 증거를 능동 탐색하는 multimodal search agent와 cross-modal 검색을 구축 (약 21편) — [OpenSearch-VL](https://neurips.cc/virtual/2026/poster/152165), [VSearcher](https://neurips.cc/virtual/2026/poster/149459), [DocAtlas](https://neurips.cc/virtual/2026/poster/148605), [BayesRAG](https://neurips.cc/virtual/2026/poster/154974)
- flat top-k 검색이 multi-hop bridge 증거를 놓쳐, KG·graph 구성, query 분해·반복 검증, retriever-free 탐색으로 증거 구조를 재설계 (약 17편) — [Hi-Q](https://neurips.cc/virtual/2026/poster/155067), [Learning Minimal Sufficient Evidence Graphs for GraphRAG …](https://neurips.cc/virtual/2026/poster/154710), [Foresight-over-Graph](https://neurips.cc/virtual/2026/poster/150820), [Geometric Gain Graph](https://neurips.cc/virtual/2026/poster/151572)
- outcome reward만으론 긴 검색 trajectory의 credit 배분이 어려워, process reward·self-distillation으로 search agent RL 개선 (약 15편) — [Beyond Outcome Rewards](https://neurips.cc/virtual/2026/poster/148305), [PiCA](https://neurips.cc/virtual/2026/poster/155622), [SD-Search](https://neurips.cc/virtual/2026/poster/155518), [Quest](https://neurips.cc/virtual/2026/poster/150926)
- 검색 문맥과 parametric 지식 충돌로 생기는 unfaithful 생성·hallucination을 decoding·representation 개입과 탐지·attribution으로 대응 (약 14편) — [Conflict-Suppressed RAG](https://neurips.cc/virtual/2026/poster/148415), [ReCon](https://neurips.cc/virtual/2026/poster/149688), [Beyond Uniform Detection](https://neurips.cc/virtual/2026/poster/155755), [Reading Attribution from Attention](https://neurips.cc/virtual/2026/poster/156092)
- 웹·코퍼스 의존이 공격면이 되어, search agent·GraphRAG 대상 poisoning·injection 공격과 방어, privacy 유출, GEO 조작을 분석 (약 13편) — [The Web Doesn't Sit Still](https://neurips.cc/virtual/2026/poster/149493), [When Poison Meets Structure](https://neurips.cc/virtual/2026/poster/152350), [Privacy-Preserving Retrieval-Augmented Generation with Pl…](https://neurips.cc/virtual/2026/poster/150803), [EcoGEO](https://neurips.cc/virtual/2026/poster/153813)
- 단일 정답 점수로는 deep research agent의 실패 원인을 알 수 없어, 실제 질의·live 갱신·trajectory 단위 진단 벤치마크를 구축 (약 12편) — [GISA](https://neurips.cc/virtual/2026/poster/139591), [MiroEval](https://neurips.cc/virtual/2026/poster/139149), [SciResearchBench](https://neurips.cc/virtual/2026/poster/139663), [RealDev-QA](https://neurips.cc/virtual/2026/poster/139440)
- 긴 검색 문맥의 prefill 비용과 latency를 줄이려 KV cache 재사용, latent space retrieval, 문맥 압축, speculative 실행을 도입 (약 11편) — [KVFocus](https://neurips.cc/virtual/2026/poster/149014), [MiniPIC](https://neurips.cc/virtual/2026/poster/151329), [LatentRAG](https://neurips.cc/virtual/2026/poster/153688), [OpticalRAG](https://neurips.cc/virtual/2026/poster/152209)
- flat RAG가 장기 agent 기억의 중복·시간 정보를 못 다뤄, 계층 구조·evidence-gap 추적·시간 인지 검색 memory와 그 평가를 제안 (약 6편) — [Beyond RAG for Agent Memory](https://neurips.cc/virtual/2026/poster/150607), [Knowing What is Missing](https://neurips.cc/virtual/2026/poster/149691), [RL-Guided Temporal Localization for Dual-Channel Retrieva…](https://neurips.cc/virtual/2026/poster/152090), [RAG in a Trenchcoat](https://neurips.cc/virtual/2026/poster/151457)
- 나머지 약 13편은 위 흐름 어디에도 주로 속하지 않는 작은 주제들이다.

### LLM 에이전트 (621편 · 학회 전체, 분야 "LLM 에이전트·도구·검색")

LLM agent 연구는 단발 tool call을 넘어 장기·실환경 workflow로 확장되며, 평가·RL 보상·memory·skill·안전을 trajectory 수준에서 다루는 쪽으로 이동

- 단일 task 성공률 benchmark가 실제 업무를 반영하지 못해, 전문 직무·장기 SWE·enterprise workflow를 실환경에서 재는 benchmark로 이동 (약 115편) — [Agents' Last Exam](https://neurips.cc/virtual/2026/poster/139517), [BankerToolBench](https://neurips.cc/virtual/2026/poster/139094), [SWE-Marathon](https://neurips.cc/virtual/2026/poster/139342), [SlopCodeBench](https://neurips.cc/virtual/2026/poster/138903)
- outcome reward만으로는 긴 multi-turn trajectory의 credit assignment가 어려워, step 단위 process reward·advantage 설계로 이동 (약 80편) — [Beyond Outcome Rewards](https://neurips.cc/virtual/2026/poster/148305), [PiCA](https://neurips.cc/virtual/2026/poster/155622), [Counterfactual Rollout Replay](https://neurips.cc/virtual/2026/poster/151386), [What Makes Two States the Same? Value-Aware State Matchin…](https://neurips.cc/virtual/2026/poster/152187)
- agent 수를 늘려도 성능이 보장되지 않아, MAS가 언제 이득인지 분석하고 topology·communication(latent 포함)을 최적화하는 방향으로 이동 (약 70편) — [The Illusion of Multi-Agent Advantage](https://neurips.cc/virtual/2026/poster/139826), [When Do Multi-Agent Systems Help? An Information Bottlene…](https://neurips.cc/virtual/2026/poster/153823), [FlowMAS](https://neurips.cc/virtual/2026/poster/152834), [CacheMAS](https://neurips.cc/virtual/2026/poster/154215)
- context window를 넘는 장기 상호작용에서 기억이 누락·오염되어, 무엇을 쓰고·갱신·검색할지 학습하는 agent memory와 진단 benchmark로 이동 (약 65편) — [MemSkill](https://neurips.cc/virtual/2026/poster/155719), [Memory-R2](https://neurips.cc/virtual/2026/poster/152449), [MEME](https://neurips.cc/virtual/2026/poster/138915), [Useful Memories Become Faulty When Continuously Updated b…](https://neurips.cc/virtual/2026/poster/148715)
- similarity top-k 검색이 multi-hop·지식 충돌에 약해, graph 구조·agentic 반복 검색·충돌 억제로 증거 선택을 정교화하는 RAG로 이동 (약 65편) — [Learning Minimal Sufficient Evidence Graphs for GraphRAG …](https://neurips.cc/virtual/2026/poster/154710), [Mitigating Knowledge Conflicts in Retrieval-Augmented Gen…](https://neurips.cc/virtual/2026/poster/148202), [Beyond Semantic Similarity](https://neurips.cc/virtual/2026/poster/155649), [LatentRAG](https://neurips.cc/virtual/2026/poster/153688)
- 수작업 prompt·harness·skill 설계가 병목이라, 실행 trace로부터 skill library와 harness를 스스로 생성·정제하는 self-evolving agent로 이동 (약 50편) — [SkillOS](https://neurips.cc/virtual/2026/poster/151446), [SkillForge](https://neurips.cc/virtual/2026/poster/151649), [AutoSaddler](https://neurips.cc/virtual/2026/poster/151256), [Hyperagents](https://neurips.cc/virtual/2026/poster/153670)
- task 성공만 보면 prompt injection·부수효과·은밀한 악의 행동을 놓쳐, 아키텍처 격리·runtime 감시·안전 benchmark로 대응하는 방향 (약 50편) — [CaMeLs Can Use Computers Too](https://neurips.cc/virtual/2026/poster/155134), [LITMUS](https://neurips.cc/virtual/2026/poster/150415), [MOSAIC-Bench](https://neurips.cc/virtual/2026/poster/139179), [Task Success Is Not Enough](https://neurips.cc/virtual/2026/poster/138911)
- 검증 가능한 학습 환경·task가 부족해, 임의 software·terminal·MCP·시뮬레이터로 verifiable 환경과 trajectory를 대규모 합성하는 방향 (약 40편) — [Gym-Anything](https://neurips.cc/virtual/2026/poster/150621), [SETA](https://neurips.cc/virtual/2026/poster/139707), [GenEnv](https://neurips.cc/virtual/2026/poster/152039), [Firefly](https://neurips.cc/virtual/2026/poster/155698)
- 나머지 약 86편은 위 흐름 어디에도 주로 속하지 않는 작은 주제들이다.

### LLM (754편 · 학회 전체, 분야 "LLM 추론·학습·RL 후처리")

LLM 연구는 RLVR/GRPO 기반 reasoning post-training을 축으로, 학습 신호의 밀도·효율·안정성과 추론 compute 최적화를 개선하는 방향으로 수렴 중

- 긴 CoT의 overthinking과 다중 샘플링 비용이 커, 길이 보상·early exit·적응적 샘플/검증 배분으로 test-time compute를 효율화 (약 85편) — [LEAD](https://neurips.cc/virtual/2026/poster/149222), [TERMINATOR](https://neurips.cc/virtual/2026/poster/148583), [Early Signals, Strong Decisions](https://neurips.cc/virtual/2026/poster/154126), [Prefill-Guided Trace Allocation for Sample-Efficient Test…](https://neurips.cc/virtual/2026/poster/154693)
- GRPO의 균일한 token advantage와 entropy collapse가 학습을 막아, token/step 단위 credit assignment와 탐색 제어로 RLVR 목적함수를 재설계 (약 70편) — [Credit Assignment with Resets in Language Model Reasoning](https://neurips.cc/virtual/2026/poster/151001), [STARE](https://neurips.cc/virtual/2026/poster/152111), [Learning to Explore with Parameter-Space Noise](https://neurips.cc/virtual/2026/poster/154785), [Unveiling Implicit Advantage Symmetry](https://neurips.cc/virtual/2026/poster/153467)
- fine-tuning이 기존 능력을 망각·간섭시켜, LoRA/PEFT 구조, model merging, continual 학습, knowledge editing으로 적응과 보존을 양립 (약 65편) — [AMARIS](https://neurips.cc/virtual/2026/poster/154547), [Estimating and Orthogonalizing Unknown Pre-training Gradi…](https://neurips.cc/virtual/2026/poster/152597), [Learning Rate Matters](https://neurips.cc/virtual/2026/poster/148585), [Norm Anchors Make Model Edits Last](https://neurips.cc/virtual/2026/poster/152750)
- 고품질 데이터가 compute보다 빨리 고갈되어, data-constrained scaling law·data mixing/selection·합성 데이터로 사전학습을 재설계 (약 55편) — [Bridging Compute- and Data-Optimal Pretraining](https://neurips.cc/virtual/2026/poster/155350), [Data-Constrained Language Model Pretraining](https://neurips.cc/virtual/2026/poster/149999), [CausalMix](https://neurips.cc/virtual/2026/poster/154762), [A Bitter Lesson for Data Filtering](https://neurips.cc/virtual/2026/poster/155947)
- 선호 라벨이 noisy·고비용이고 reward가 해킹되어, robust DPO/Nash 정렬·rubric 기반 reward·reward hacking 진단으로 정렬 신호를 개선 (약 55편) — [Correct, Route, Calibrate](https://neurips.cc/virtual/2026/poster/152258), [Robust Nash Alignment under Preference Uncertainty](https://neurips.cc/virtual/2026/poster/154554), [Not Every Rubric Teaches Equally](https://neurips.cc/virtual/2026/poster/155810), [Reward Hacking in Rubric-Based Reinforcement Learning](https://neurips.cc/virtual/2026/poster/154025)
- RLVR의 희소 보상을 보완하려 on-policy (self-)distillation으로 이동했고, 그 불안정성과 teacher 신호 품질 저하를 고치는 연구가 집중 (약 50편) — [KL for a KL](https://neurips.cc/virtual/2026/poster/149290), [Your Teacher Can’t Help You Here](https://neurips.cc/virtual/2026/poster/154216), [The Many Faces of On-Policy Distillation](https://neurips.cc/virtual/2026/poster/153073), [Self-Distilled RLVR](https://neurips.cc/virtual/2026/poster/152431)
- RL post-training이 새 추론 능력을 만드는지 기존 분포를 sharpen할 뿐인지 불명확해, 통제된 synthetic 환경과 mechanistic 분석으로 검증 (약 45편) — [How New Strategies Emerge in RL Post-Training](https://neurips.cc/virtual/2026/poster/151430), [The Reasoning Boundary Paradox](https://neurips.cc/virtual/2026/poster/150680), [Irreducible Supervision Enables Compositional Generalizat…](https://neurips.cc/virtual/2026/poster/149659), [How does RL Post-training Induce Skill Composition? A Cas…](https://neurips.cc/virtual/2026/poster/148203)
- rollout 생성이 RLVR 비용을 지배해, prompt 선택·curriculum·rollout 예산 배분과 off-policy 보정·비동기 시스템으로 학습을 효율화 (약 40편) — [Train at the Moving Edge](https://neurips.cc/virtual/2026/poster/149668), [DUET](https://neurips.cc/virtual/2026/poster/153196), [VESPO](https://neurips.cc/virtual/2026/poster/155242), [DORA](https://neurips.cc/virtual/2026/poster/154440)
- 나머지 약 289편은 위 흐름 어디에도 주로 속하지 않는 작은 주제들이다.

### Medical QA (25편 · 216편 목록)

시험형 정답 정확도를 넘어, 실제 임상 workflow·영상 근거·오도 맥락 하에서 근거에 기반한 신뢰 가능한 의료 추론을 평가하고 학습시키는 방향

- 고립된 2D 이미지 VQA로는 임상 판독을 못 재므로, 다중 시퀀스·3D·종단 MRI/유방촬영/병리 benchmark로 영상 근거 사용의 실패를 드러냄 (약 4편) — [BrainTRACE](https://neurips.cc/virtual/2026/poster/139162), [CardioLens](https://neurips.cc/virtual/2026/poster/139679), [MammoGPS](https://neurips.cc/virtual/2026/poster/138998), [VIPER](https://neurips.cc/virtual/2026/poster/139742)
- 정보가 미리 주어진 vignette 대신, 근거가 순차적으로 쌓이는 진단 trajectory·응급실·care pathway·다회차 EHR QA로 평가 이동 (약 4편) — [DDx-TRACE](https://neurips.cc/virtual/2026/poster/139550), [ER-Reason](https://neurips.cc/virtual/2026/poster/138971), [NPCBench](https://neurips.cc/virtual/2026/poster/139689), [EHRNote-ChatQA](https://neurips.cc/virtual/2026/poster/139551)
- 높은 정답률이 안전을 뜻하지 않아, 오도 맥락·깨진 영상 근거에서의 silent failure와 시각 붕괴를 측정하고 abstention·검증으로 보완 (약 4편) — [MedMisBench](https://neurips.cc/virtual/2026/poster/139561), [MedVIGIL](https://neurips.cc/virtual/2026/poster/139346), [Selective Answering for Medical VQA via Parallel Independ…](https://neurips.cc/virtual/2026/poster/150272), [Diagnosing and Repairing Visual Collapse in Compact Medic…](https://neurips.cc/virtual/2026/poster/149438)
- 전문가 라벨이 비싸 answer-level reward가 거칠어, case report self-play·self-evolving agent·논문 기반 추론 trace로 의료 추론 학습 (약 4편) — [CasePlay](https://neurips.cc/virtual/2026/poster/153097), [MedZERO](https://neurips.cc/virtual/2026/poster/155563), [Teach-to-Reason](https://neurips.cc/virtual/2026/poster/150121), [OpenMedReason](https://neurips.cc/virtual/2026/poster/139693)
- top-k 검색·답만으로는 검증이 어려워, 최소 충분 근거 선택·체계적 문헌 결론 합성·인용 기반 QA로 evidence-grounded 답변을 추구 (약 4편) — [Less Evidence, Better Answering](https://neurips.cc/virtual/2026/poster/152857), [Can AI Agents Synthesize Scientific Conclusions?](https://neurips.cc/virtual/2026/poster/139077), [MutQA](https://neurips.cc/virtual/2026/poster/139212)
- 기존 의료 benchmark가 포화·평면적이라, 대규모 open suite·graph 구조 지표·다직종 면허시험으로 평가 체계 자체를 재구성 (약 3편) — [Medmarks](https://neurips.cc/virtual/2026/poster/139434), [LG-Bench](https://neurips.cc/virtual/2026/poster/139764), [JMed48k](https://neurips.cc/virtual/2026/poster/139030)
- 나머지 약 2편은 위 흐름 어디에도 주로 속하지 않는 작은 주제들이다.

### Medical LLM / VLM (70편 · 216편 목록)

의료 LLM/VLM 연구는 시험형 정확도를 넘어, 실제 임상 workflow 평가·시각 근거 grounding·rubric 기반 RL·안전한 기권으로 이동 중

- 단일 이미지 VQA 정확도로는 실제 판독 능력을 못 재므로, 다중 시퀀스·종단·장시간 영상·병리 다중스케일 등 workflow형 VLM 벤치마크로 이동 (약 13편) — [CardioLens](https://neurips.cc/virtual/2026/poster/139679), [BrainTRACE](https://neurips.cc/virtual/2026/poster/139162), [MedHorizon](https://neurips.cc/virtual/2026/poster/139391), [PathView-Bench](https://neurips.cc/virtual/2026/poster/139172)
- 전문가 라벨 부족과 answer-level reward의 한계를 넘기 위해, rubric·self-play·distillation 기반 RL post-training으로 의료 추론 모델을 학습 (약 12편) — [CasePlay](https://neurips.cc/virtual/2026/poster/153097), [CLR-voyance ](https://neurips.cc/virtual/2026/poster/150688), [Incentivizing Medical Vision Capabilities from Large-Scal…](https://neurips.cc/virtual/2026/poster/156128), [TraceDx](https://neurips.cc/virtual/2026/poster/149401)
- 정적 시험형 QA가 실제 진료와 괴리되어, 정보 수집·믿음 갱신·종단 진료 경로를 실제 기록으로 평가하는 sequential 임상추론 벤치마크로 이동 (약 10편) — [ER-Reason](https://neurips.cc/virtual/2026/poster/138971), [DDx-TRACE](https://neurips.cc/virtual/2026/poster/139550), [RealICU](https://neurips.cc/virtual/2026/poster/138984), [NPCBench](https://neurips.cc/virtual/2026/poster/139689)
- 의료 VLM이 이미지를 무시하고 언어 prior로 답하는 문제를 attention head·residual 분석으로 진단하고, grounding 손실·데이터 선택·기권으로 교정 (약 9편) — [CRAFT](https://neurips.cc/virtual/2026/poster/149960), [Diagnosing and Repairing Visual Collapse in Compact Medic…](https://neurips.cc/virtual/2026/poster/149438), [MedVIGOR](https://neurips.cc/virtual/2026/poster/150235), [MedVIGIL](https://neurips.cc/virtual/2026/poster/139346)
- 보고서 생성의 hallucination·누락을 줄이려 diffusion planning·anomaly 증거 선택·preference optimization과 3D CT 표현 학습을 결합 (약 9편) — [Anchoring LLM-based Chest X-ray Report Generation via Dif…](https://neurips.cc/virtual/2026/poster/148935), [Glance Before You Tell](https://neurips.cc/virtual/2026/poster/149584), [Positive-Unlabeled Preference Optimization For Chest X-ra…](https://neurips.cc/virtual/2026/poster/154826), [SliceWorld](https://neurips.cc/virtual/2026/poster/150217)
- 정신건강 상담·임상 윤리에서 표면적 safety 점수로는 부족해, 임상가 기반 위험 분류·guardrail·오도 맥락 저항·LLM-judge 검증 체계를 구축 (약 7편) — [MindGuard](https://neurips.cc/virtual/2026/poster/138950), [TherapyGym](https://neurips.cc/virtual/2026/poster/139071), [MedMisBench](https://neurips.cc/virtual/2026/poster/139561), [Alignment Is Not Enough for Safe Medical LLM Evaluation](https://neurips.cc/virtual/2026/poster/140065)
- 고위험 임상 의사결정에서 근거 없는 확신을 막기 위해, calibration·Bayesian 사후추론·uncertainty routing으로 deferral 가능한 agent를 설계 (약 5편) — [Calibrating Agentic LLMs for Clinical Prediction](https://neurips.cc/virtual/2026/poster/149149), [MoBayes](https://neurips.cc/virtual/2026/poster/152953), [Teaching LLMs to Recommend and Defer in Underrepresented …](https://neurips.cc/virtual/2026/poster/154539), [Learning When to Collaborate](https://neurips.cc/virtual/2026/poster/148185)
- EHR·유전체 예측의 표현 설계 병목을 풀기 위해, LLM이 만든 rubric·rationale·온톨로지 임베딩을 하위 예측 모델의 입력·학습신호로 활용 (약 4편) — [LLMs can construct powerful representations and streamlin…](https://neurips.cc/virtual/2026/poster/153045), [On-Policy Hindsight Distillation for Early Risk Prediction](https://neurips.cc/virtual/2026/poster/153484), [SMI](https://neurips.cc/virtual/2026/poster/154857)
- 나머지 약 1편은 위 흐름 어디에도 주로 속하지 않는 작은 주제들이다.

### Medical Agent (26편 · 216편 목록)

의료 agent 연구는 정적 QA를 넘어 다회차 진단과 실제 시스템 workflow 실행으로 평가·학습을 옮기고, 배포 제약 속 신뢰성과 경험 기억을 함께 다룬다

- 정적 QA가 진료의 단계적 정보수집을 못 담아, patient simulator 기반 다회차 진단 환경과 RL로 질문·검사 정책을 학습하는 쪽으로 이동 (약 7편) — [MedExAgent](https://neurips.cc/virtual/2026/poster/149616), [TraceDx](https://neurips.cc/virtual/2026/poster/149401), [CoE-Agent](https://neurips.cc/virtual/2026/poster/155085), [ClinMAS](https://neurips.cc/virtual/2026/poster/139102)
- privacy·비용·small LLM·calibration 제약에서 multi-agent 협업이 불안정해, 선택적 routing·기여도 집계·handoff context 통제로 재설계 (약 5편) — [Learning When to Collaborate](https://neurips.cc/virtual/2026/poster/148185), [CoMMa](https://neurips.cc/virtual/2026/poster/153350), [Risk-Calibrated Context Selection for Healthcare Multi-Ag…](https://neurips.cc/virtual/2026/poster/154212), [Calibrating Agentic LLMs for Clinical Prediction](https://neurips.cc/virtual/2026/poster/149149)
- EHR·임상시험 분석이 암묵적 임상 semantics에서 깨지므로, 명세·skill·검증 단계를 갖춘 연구 자동화 agent와 벤치마크로 이동 (약 5편) — [M4Bench](https://neurips.cc/virtual/2026/poster/139625), [ProCARE](https://neurips.cc/virtual/2026/poster/149562), [TrialAgentBench](https://neurips.cc/virtual/2026/poster/139604), [BioXArena](https://neurips.cc/virtual/2026/poster/138952)
- 답 정확도만으로는 실무 수행력을 못 재므로, EHR API·MCP 도구·영상 viewer를 직접 조작하는 장기 workflow 실행·근거 검증 벤치마크로 이동 (약 4편) — [PhysicianBench](https://neurips.cc/virtual/2026/poster/139788), [χ-Bench](https://neurips.cc/virtual/2026/poster/139361), [REAL-MED](https://neurips.cc/virtual/2026/poster/139773), [MedFlowBench](https://neurips.cc/virtual/2026/poster/139506)
- 진료 경험이 누적되는 장기 사용에서 raw trace 기억이 취약해, skill memory·종단 episode 평가·memory saturation 벤치마크로 경험 축적을 다룸 (약 4편) — [Experience Makes Skillful](https://neurips.cc/virtual/2026/poster/150444), [MedEvoEval](https://neurips.cc/virtual/2026/poster/139548), [MedMemoryBench](https://neurips.cc/virtual/2026/poster/139145), [RealICU](https://neurips.cc/virtual/2026/poster/138984)
- 나머지 약 1편은 위 흐름 어디에도 주로 속하지 않는 작은 주제들이다.

## Medical QA 벤치마크로 실험한 논문 (51편)

MedQA·MedMCQA·MedXpertQA·PubMedQA·VQA-RAD·SLAKE 같은 **기존 공개 의료 QA 벤치마크로 직접 실험한** NeurIPS 2026 논문이다. 논문이 새로 만든 벤치마크만 쓴 경우는 넣지 않았다(아래 표의 '자체 벤치마크'에 따로 적었다).

**찾은 방법과 범위**: LLM·VLM을 다루는 논문 등 후보 3,478편의 arXiv 판을 찾아 본문에서 벤치마크 이름 32종을 검색했다. 본문을 읽은 것은 1,828편이고, **1,646편은 arXiv 판을 찾지 못해 확인하지 못했다**(OpenReview는 자동 다운로드를 막는다). 본문에 이름이 나온 79편을 LLM이 읽어 실험에 썼는지 판정했고, 성능 수치는 본문에 그대로 있는 값만 남겼다(검증된 수치 137개). 그래서 이 목록은 '전부'가 아니라 **본문을 확인할 수 있었던 논문 중 전부**다. 파이프라인은 `scripts/medqa_bench/`에 있다.

### Medical QA가 주 타깃인 논문 (10편)

위 51편 중 대부분은 여러 도메인을 평가하는 일반 LLM 논문이고, 의료 QA 자체를 풀려는 논문은 아래 10편이다. 대표 성능은 논문이 보고한 값이며, 괄호는 그 논문 안의 비교 대상이다(논문끼리는 비교할 수 없다).

| 논문 | 벤치마크 | 모델 | 학습 | 문제 정의 | 제안 방법 | 대표 성능 |
|---|---|---|---|---|---|---|
| [CLR-voyance : Reinforcing Open-Ended Reasoning for Inpatient Clinical Decision Support with Outcome-Aware Rubrics](https://neurips.cc/virtual/2026/poster/150688) | HealthBench, MedCalc-Bench, MedMCQA | Qwen3-8B, MedGemma-4B-IT, GPT-5 | 학습함 (RL) | 입원 환자 임상 추론은 부분 관찰 순차 결정인데 기존 평가·RL 보상은 이를 단순화하거나 미래를 누설한다. | 입원 경과를 과거/미래로 나눈 POMDP와 결과 기반 적응형 루브릭으로 Qwen3-8B·MedGemma-4B를 GRPO 학습한다. | MedMCQA: 67.0 (vs Qwen3-8B base 66.0)<br>MedMCQA: 61.0 (vs MG-4B base 54.5)<br>MedCalc: 46.0 (vs Qwen3-8B base 41.5) |
| [CRAFT: Causal Responsibility and Failure Tracing in Medical Vision Language Models](https://neurips.cc/virtual/2026/poster/149960) | ConflictMedQA, HealMed-VQA, PubMedQA, SLAKE, VQA-RAD | Hulu-Med 4B, Hulu-Med 7B, Hulu-Med 14B | 학습 없음 (prompting·agent·추론 기법) | 의료 VLM이 오도하는 텍스트에 시각 근거를 무시하거나 증거 부족에도 확신 답하는 원인을 규명한다. | 두 실패 모드를 일으키는 최소 인과 어텐션 헤드 집합을 찾아 제거해 재학습 없이 교정하는 CRAFT를 제안한다. | VQA-RAD: 15.38 (vs Baseline 33.33)<br>SLAKE: 65.15 (vs Baseline 37.88)<br>HealMed-VQA: 98.20 (vs Baseline 78.44) |
| [EHRNote-ChatQA: A Benchmark for Evidence-Grounded Multi-Turn Clinical Question Answering over Longitudinal Discharge Summaries](https://neurips.cc/virtual/2026/poster/139551) | EHRNoteQA | gpt-5.4, gemini-3-flash-preview, Qwen3-Next-80B-A3B-Instruct | 평가만 (벤치마크·분석) | 기존 임상 QA 벤치마크는 다중 퇴원요약에 대한 다회차·근거 기반 질의를 반영하지 못한다. | MIMIC-IV 퇴원요약 기반 다회차 근거 QA 벤치마크로 22개 LLM을 평가하고 단일턴 QA와 비교한다. | EHRNoteQA: 95.63 (vs EHRNote-ChatQA QA-level Content 98.33)<br>EHRNoteQA: 80.15 (vs EHRNote-ChatQA QA-level Content 27.05)<br>EHRNoteQA: 91.68 (vs EHRNote-ChatQA QA-level Content 31.56) |
| [Experience Makes Skillful: Enabling Generalizable Medical Agent Reasoning via Self-Evolving Skill Memory](https://neurips.cc/virtual/2026/poster/150444) | AgentClinic, HealthBench, LiveClin, LiveMedBench, MMMU, MMMU-Pro, MedJourney, MedXpertQA, MediQ | DeepSeek-V3.2, Qwen3.6-Plus, HuluMed-32B | 학습 없음 (prompting·agent·추론 기법) | 의료 에이전트의 기존 메모리는 원시 궤적을 저장해 중복·잡음이 많고 유용한 기억을 구분하지 못한다. | 상호작용 궤적을 구조화된 스킬로 증류하고 효용 기반 검색·관리로 가중치 갱신 없이 자기진화한다. | MedXpertQA: 35.68 (vs ReAct 33.51)<br>HealthBench: 27.65 (vs ReAct 19.06)<br>MMMU: 66.91 (vs ReAct 46.04) |
| [MedExAgent: Training LLM Agents to Ask, Examine, and Diagnose in Noisy Clinical Environments](https://neurips.cc/virtual/2026/poster/149616) | AgentClinic | Meditron3-8B, Aloe-Beta-70B, Qwen3-32B | 학습함 (SFT+RL) | 기존 의료 LLM 평가·진단법은 잡음 있는 대화형 문진·검사 과정을 단순화해 무시한다. | 진단을 POMDP와 잡음 모델로 정식화하고 SFT 후 DAPO로 문진·검사·진단 에이전트를 학습한다. | AgentClinic-MedQA: 0.378 (vs Aloe-Beta-70B 0.395)<br>AgentClinic-MedQA: 0.672 (vs Aloe-Beta-70B 0.684) |
| [Medmarks: A Comprehensive Open-Source LLM Benchmark Suite for Medical Tasks](https://neurips.cc/virtual/2026/poster/139434) | AgentClinic, HealthBench, MedBullets, MedCalc-Bench, MedConceptsQA, MedMCQA, MedQA, MedXpertQA, MetaMedQA, PubMedQA | Gemini 3 Pro Preview, GPT-5.1, GPT-5.2 | 평가만 (벤치마크·분석) | 기존 의료 LLM 벤치마크는 포화되었거나 비공개 데이터 의존·모델 범위가 부족하다. | 30개 공개 의료 벤치마크를 묶은 MEDMARKS로 61개 모델·71개 설정을 체계적으로 평가한다. | MedQA: 0.784<br>MedMCQA: 0.656<br>MedXpertQA: 0.236-0.237 |
| [MoBayes: A Modular Bayesian Framework for Separating Reasoning from Language in Conversational Clinical Decision Support](https://neurips.cc/virtual/2026/poster/152953) | AgentClinic | GPT-5.4-nano, Gemini 3.1 Flash Lite, Llama-4-Scout | 학습 없음 (prompting·agent·추론 기법) | 대화형 임상 의사결정 지원 LLM은 토큰 예측과 확률적 의사결정을 혼동해 사후확률 추적·보류가 어렵다. | LLM은 대화를 관찰로 파싱만 하고 베이지안 모듈이 사후 갱신·정보이득 질문·보류 결정을 수행한다. | AgentClinic-MedQA: 86.8 (vs SA Gemini 3.1 Pro (standalone doctor) 80.4)<br>AgentClinic-MedQA: 78 (vs SA Gemini 3.1 Pro (standalone doctor) 66)<br>AgentClinic-MedQA: 83 (vs MEDDxAgent (closed-world abl.) 89) |
| [OpenMedReason: Scientific Reasoning Supervision for Medical Vision–Language Models](https://neurips.cc/virtual/2026/poster/139693) | JAMA CC-MM, MedXpertQA, PMC-VQA, PathVQA, SLAKE, VQA-RAD | Qwen2.5-VL-7B, Lingshu 7B, OctoMed 7B | 학습함 (SFT+RL) | 의료 LVLM의 추론 지도 데이터가 합성 CoT 위주라 시각·임상 근거에 기반한 추론이 부족하다. | 과학 논문 기반 추론 흔적을 담은 45만 건 의료 VQA 코퍼스로 SFT·GRPO 학습하고 세부 벤치를 제시한다. | SLAKE: 85.10 (vs Qwen2.5-VL-7B (Base) 62.26)<br>VQA-RAD: 72.51 (vs Qwen2.5-VL-7B (Base) 67.13)<br>PathVQA: 64.10 (vs Qwen2.5-VL-7B (Base) 62.88) |
| [PathNavigate: A Training-Free Pathology Agent with Surprise-Guided Scan and Shared Slide Memory for Whole-Slide VQA](https://neurips.cc/virtual/2026/poster/154224) | PathMMU, SlideBench-BCNB, WSI-VQA | Patho-R1-7B, Qwen3.5-4B, PathAgent | 학습 없음 (prompting·agent·추론 기법) | 기가픽셀 WSI-VQA에서 질문 중심 후보 선택은 질문에 없는 결정적 형태학 소견을 놓치기 쉽다. | 저배율 스캔과 공유 온라인 메모리로 이상 영역 풀을 만든 뒤 PLIP로 재순위해 고배율 근거로 답한다. | SlideBench-BCNB: 59.42 (vs PathAgent 55.72)<br>WSI-VQA: 56.34 (vs PathAgent 33.88)<br>WSI-VQA: 61.00 (vs MedDr 46.86) |
| [Teach-to-Reason: Competition-Guided Reasoning with a Self-Improving Teacher](https://neurips.cc/virtual/2026/poster/150121) | Chest_X-Ray_PA, Covid19_heywhale, MIMIC-CXR-VQA, Medical-CXR-VQA, SLAKE, VQA-RAD | Qwen3-VL-Instruct 2B, Qwen3-VL-Instruct 4B | 학습함 (RL) | 흉부 X선 VQA에서 정답 수준 보상만으로는 CoT 품질 개선이 어렵고 그룹 이점이 0으로 붕괴한다. | 자기경쟁으로 강화되는 Teacher와 비교해 보상을 받는 Reasoner를 사례별 보상 설계로 GRPO 학습한다. | VQA-RAD: 46.96 (vs Base Model 40.37)<br>SLAKE: 64.92 (vs Base Model 58.11)<br>VQA-RAD: 43.18 (vs Base Model 31.69) |

### 전체 목록

| # | 논문 | 벤치마크 | 모델 | 학습 | 문제 정의 | 제안 방법 |
|---:|---|---|---|---|---|---|
| 1 | [AgentArk: Distilling Multi-Agent Intelligence into a Single LLM Agent](https://neurips.cc/virtual/2026/poster/149790) | MedMCQA | Qwen3-8B, Qwen3-32B, Llama3-8B-Instruct, Gemma-7B | 학습함 (SFT+RL) | 다중 에이전트 토론은 추론 성능이 높지만 계산 비용과 오류 전파 때문에 실제 배포가 어렵다. | 다중 에이전트 추론을 RSFT·데이터 증강·PRM 기반 과정 증류로 단일 모델 가중치에 증류한다. |
| 2 | [Agentic Multi-Turn Reasoning: A Fairness Approach](https://neurips.cc/virtual/2026/poster/149499) | MedQA | Qwen2.5-7B-Instruct, Qwen3.5-9B, Flow-GRPO, AgentFlow | 학습함 (RL) | 에이전트 학습에서 장기 신용 할당과 불균형 데이터 분포 문제가 있다 | 공정성 기반 다층 선호 최적화 Φ-MPO로 장기 추론과 데이터 불균형을 동시에 해결 |
| 3 | [Aligning Language Models with Selective Prediction](https://neurips.cc/virtual/2026/poster/148722) | MedQA | Qwen2.5-7B, Llama-3.1-8B | 학습함 (RL) | LLM 사후학습이 정확도·보정만 겨냥해 선택적 예측의 위험-커버리지 균형을 다루지 못함 | 위험-커버리지 곡선 면적(AURC)을 보상으로 직접 최적화하는 RL 정렬 RLSR 제안 |
| 4 | [ARC-Encoder: learning compressed text representations for large language models](https://neurips.cc/virtual/2026/poster/156755) | BioASQ, PubMedQA | Mistral 7B, Llama3.1 8B, Llama2 7B Chat, LLMLingua2 | 학습함 (기타) | 긴 컨텍스트로 늘어난 LLM 추론 비용을 디코더 수정 없이 줄이기 어려운 문제를 다룬다. | 컨텍스트를 연속 표현으로 압축해 디코더 토큰 임베딩을 대체하는 인코더 ARC-Encoder를 학습한다. |
| 5 | [Beyond LoRA vs. Full Fine-Tuning: Gradient-Guided Optimizer Routing for LLM Adaptation](https://neurips.cc/virtual/2026/poster/154880) | MedMCQA | Gemma-3-1B, Qwen2.5-1.5B, Qwen2.5-3B, Meta-Llama-3-8B | 학습함 (SFT) | LoRA와 전체 미세조정 중 어느 쪽이 나은지가 과제·모델마다 달라지는 문제를 다룬다. | 옵티마이저 수준에서 모듈별로 FFT와 LoRA 업데이트를 라우팅하는 MoLF와 메모리 절약형 MoLF-E를 제안한다. |
| 6 | [Beyond Raw Context Transfer: Representation-based Federated Retrieval-Augmented Generation](https://neurips.cc/virtual/2026/poster/150023) | PubMedQA, SLAKE | Qwen2.5-VL-7B, Qwen3-8B | 학습함 (기타) | 의료처럼 데이터가 분산·민감한 환경에서 원문 교환형 분산 RAG는 통신 비용과 프라이버시 위험이 크다. | 검색 결과를 압축 잠재 표현으로만 교환하고 연합 학습한 경량 프로젝터로 고정 LLM/VLM에 주입한다. |
| 7 | [BioXArena: Benchmarking LLM Agents on Multi-Modal Biomedical Machine Learning Tasks](https://neurips.cc/virtual/2026/poster/138952) | PMC-VQA, PathVQA, SLAKE | MLEvolve (Gemini-3.1-Pro), GPT-5.4, Claude Opus 4.6, Gemini-3.1-Pro | 평가만 (벤치마크·분석) | LLM 에이전트가 다중모달 생의학 데이터용 ML 모델 구축 코드를 작성하는지 평가할 벤치마크가 없다. | 9개 도메인 76개 과제의 BioXArena를 만들어 11개 에이전트 구성을 2시간·단일 GPU 환경에서 평가한다. |
| 8 | [CLR-voyance : Reinforcing Open-Ended Reasoning for Inpatient Clinical Decision Support with Outcome-Aware Rubrics](https://neurips.cc/virtual/2026/poster/150688) | HealthBench, MedCalc-Bench, MedMCQA | Qwen3-8B, MedGemma-4B-IT, GPT-5, MedGemma-27B | 학습함 (RL) | 입원 환자 임상 추론은 부분 관찰 순차 결정인데 기존 평가·RL 보상은 이를 단순화하거나 미래를 누설한다. | 입원 경과를 과거/미래로 나눈 POMDP와 결과 기반 적응형 루브릭으로 Qwen3-8B·MedGemma-4B를 GRPO 학습한다. |
| 9 | [Communication-Efficient LLM Adaptation over Decentralized GPU Meshes](https://neurips.cc/virtual/2026/poster/153942) | MedMCQA, MedQA | Llama-3.2-1B | 학습함 (SFT) | 저대역 인터넷 기반 분산 GPU 메시에서 LLM 적응 학습의 통신 병목 문제 | 활성값 마스킹 고속 회로와 비동기 앵커 사전 회로, 스펙트럴 보정 옵티마이저로 압축 학습 |
| 10 | [Conformal Selective Acting: Anytime-Valid Risk Control for RLVR-Trained LLMs](https://neurips.cc/virtual/2026/poster/148731) | HEAD-QA, MedQA, PubMedQA | Fleming-R1, Med42-8B, Qwen2.5-Math-7B, Llama-3.2-3B-Inst. | 학습 없음 (prompting·agent·추론 기법) | 온라인 갱신되는 RLVR 특화 LLM 배포에서 매 시점 유효한 선택적 위험 보장이 없다 | 임계값별 e-process를 유지해 anytime-pathwise 선택적 위험을 보장하는 래퍼 CSA를 제안 |
| 11 | [CRAFT: Causal Responsibility and Failure Tracing in Medical Vision Language Models](https://neurips.cc/virtual/2026/poster/149960) | ConflictMedQA, HealMed-VQA, PubMedQA, SLAKE, VQA-RAD | Hulu-Med 4B, Hulu-Med 7B, Hulu-Med 14B, InternVL3.5 4B | 학습 없음 (prompting·agent·추론 기법) | 의료 VLM이 오도하는 텍스트에 시각 근거를 무시하거나 증거 부족에도 확신 답하는 원인을 규명한다. | 두 실패 모드를 일으키는 최소 인과 어텐션 헤드 집합을 찾아 제거해 재학습 없이 교정하는 CRAFT를 제안한다. |
| 12 | [Decentralized Aggregation of LLM Predictions via Wagering Mechanisms](https://neurips.cc/virtual/2026/poster/150523) | MedMCQA, PubMedQA | Llama3-Aloe-8B, Gemma-2-9B, Llama3.1-8B, BioMistral-7B | 학습함 (기타) | 탈중앙 환경에서 여러 LLM 예측을 사적 정보 없이 가중 집계하기 어렵다 | 모델이 예측과 학습된 베팅을 보고하고 베팅을 가중치로 집계하는 WALLA 메커니즘 제안 |
| 13 | [Demystifying Numerical Errors in LLM Inference: Achieving Reproducible Inference for Mission-Critical Tasks with HEAL](https://neurips.cc/virtual/2026/poster/155629) | MedQA | Qwen3-8B, Qwen3-14B, Qwen3-32B, Llama-3.1-8B-Instruct | 학습 없음 (prompting·agent·추론 기법) | 이기종 GPU에서 16비트 LLM 추론 결과가 탐욕 디코딩에서도 재현되지 않는 문제를 다룬다. | QKV INT16 양자화와 16비트 텐서코어 오차 보정으로 FP32 수준 재현성을 내는 HEAL과 MCR-Bench를 제안한다. |
| 14 | [Efficiently Aligning Draft Models via Parameter- and Data-Efficient Adaptation](https://neurips.cc/virtual/2026/poster/153042) | MMLU, MedMCQA, MedQA, PubMedQA, USMLE | Meditron3-Qwen2.5-7B, Qwen2.5-7B, Qwen2.5-Math-7B, Qwen2.5-Coder-7B | 학습함 (기타) | 도메인 파인튜닝된 타깃 모델에서 추측 디코딩 드래프트 모델의 수락 길이가 급감하는 문제 | 공유·전용 전문가 분리 구조, 타깃 모델 기반 데이터 재생성, 샘플 선택으로 드래프트 모델을 효율 적응(EDA) |
| 15 | [EHRNote-ChatQA: A Benchmark for Evidence-Grounded Multi-Turn Clinical Question Answering over Longitudinal Discharge Summaries](https://neurips.cc/virtual/2026/poster/139551) | EHRNoteQA | gpt-5.4, gemini-3-flash-preview, Qwen3-Next-80B-A3B-Instruct, Llama-4-Scout-17B-16E-Instruct | 평가만 (벤치마크·분석) | 기존 임상 QA 벤치마크는 다중 퇴원요약에 대한 다회차·근거 기반 질의를 반영하지 못한다. | MIMIC-IV 퇴원요약 기반 다회차 근거 QA 벤치마크로 22개 LLM을 평가하고 단일턴 QA와 비교한다. |
| 16 | [Entropy Distribution as a Fingerprint for Hallucinations in Generative Models](https://neurips.cc/virtual/2026/poster/148328) | BioASQ | Llama-2-7B-Chat, Meta-Llama-3-8B-Instruct, Mistral-7B-Instruct-v0.3, Falcon-7B-Instruct | 학습 없음 (prompting·agent·추론 기법) | 기존 환각 탐지가 다중 샘플링이나 모델 내부 접근을 요구하는 문제 | 토큰 엔트로피 분포의 평균·최댓값을 보정 CDF로 결합한 단일 패스 탐지 점수 CES 제안 |
| 17 | [Experience Makes Skillful: Enabling Generalizable Medical Agent Reasoning via Self-Evolving Skill Memory](https://neurips.cc/virtual/2026/poster/150444) | AgentClinic, HealthBench, LiveClin, LiveMedBench, MMMU, MMMU-Pro, MedJourney, MedXpertQA, MediQ | DeepSeek-V3.2, Qwen3.6-Plus, HuluMed-32B, Lingshu-32B | 학습 없음 (prompting·agent·추론 기법) | 의료 에이전트의 기존 메모리는 원시 궤적을 저장해 중복·잡음이 많고 유용한 기억을 구분하지 못한다. | 상호작용 궤적을 구조화된 스킬로 증류하고 효용 기반 검색·관리로 가중치 갱신 없이 자기진화한다. |
| 18 | [Fix the Structural Bottleneck: Context Compression via Explicit Information Transmission](https://neurips.cc/virtual/2026/poster/152205) | BioASQ | Llama-3.2-1B-Base, Llama-3.2-3B-Base, ICAE, 500x | 학습함 (기타) | LLM 기반 문맥 압축기가 정보를 잘 보존하지 못해 전체 문맥보다 성능이 낮다 | 층별 특징을 선택하고 전역 수송 계획으로 압축 슬롯에 정보를 배분하는 ComprExIT 제안 |
| 19 | [Focal Reward: Balanced Reinforcement Learning under Rubric-Based Rewards](https://neurips.cc/virtual/2026/poster/150481) | HealthBench | Qwen2.5-7B-Instruct, Qwen3-8B, Qwen3-30B-A3B | 학습함 (RL) | 루브릭 기반 RL에서 기준별 보상 편중으로 일부 차원이 부실해진다 | 기준별 포화도를 추정해 가중치를 자동 재조정하는 Focal Reward 목적함수 제안 |
| 20 | [From Experts to Sub-experts: Fine-grained Parameter-Efficient Fine-Tuning for MoE LLMs](https://neurips.cc/virtual/2026/poster/155254) | MMedC, PubMedQA | OLMoE, Ling-mini-2.0 | 학습함 (SFT) | MoE LLM의 PEFT에서 전문가 단위 적응이 너무 거칠어 비효율적인 문제를 다룬다. | 전문가를 채널 그룹 서브전문가로 나눠 과제 관련 부분만 학습하는 NSFT와 학습률·그래디언트 스케일링을 제안한다. |
| 21 | [From Talking Words to Sharing Thoughts: Scalable Multi-LLM Aggregation via Structured Message Passing](https://neurips.cc/virtual/2026/poster/154681) | MedMCQA | Qwen2.5-7B-Instruct, Qwen2.5-Coder-7B-Instruct, Mathstral-7B-v0.1, Bio-Medical-Llama-3-8B | 학습 없음 (prompting·agent·추론 기법) | 다중 LLM 앙상블의 높은 호출 비용과 약한 모델에 의한 앵커 오염 문제를 다룬다. | LLM 출력 분포를 이분 팩터 그래프 위 메시지 패싱과 비대칭 감쇠로 통합해 추가 LLM 호출 없이 집계한다. |
| 22 | [Group Perspective Matters: Regulating Debate Relationships Can Mitigate Blind Conformity in Multi-Agent Debate](https://neurips.cc/virtual/2026/poster/154678) | MedXpertQA | Qwen3-8B, GPT-4o-mini, Claude-4.5-Sonnet, Gemini-3.1-Flash-Lite | 학습함 (RL) | 다중 에이전트 토론에서 소수 의견이 다수에 맹목적으로 동조하는 문제 | 합의·이견을 집단 증거로 정량화하고 두 RL 에이전트로 참조 상대와 생성 행동을 동적 조절(DEAR) |
| 23 | [InduceKV: Fixed-Footprint Continual Adaptation of Multimodal LLMs via Inducing KV Memories](https://neurips.cc/virtual/2026/poster/153680) | PathVQA, SLAKE, VQA-RAD | LLaVA-1.5, LLaVA-OneVision-4B | 학습함 (기타) | 고정 배포 메모리 예산 하에서 멀티모달 LLM을 지속 적응시키는 문제 | 선택된 학습 프리픽스를 KV 메모리로 저장하고 이중수준 선택으로 유도 집합을 구성하는 InduceKV 제안 |
| 24 | [INFUSER: Influence-Guided Self-Evolution Improves Reasoning](https://neurips.cc/virtual/2026/poster/153094) | MedQA, MedXpertQA | Qwen3-4B-Base, Qwen3-8B-Base, OLMo-3-7B-Instruct-SFT | 학습함 (RL) | 자기진화 추론 학습이 큐레이션 데이터나 난이도 휴리스틱 보상에 의존하는 문제 | 문서에서 문제를 만드는 생성기를 영향력 점수로 보상하고 DuGRPO로 생성기·풀이기를 공진화(INFUSER) |
| 25 | [Learning Evidence Highlighting for Frozen LLMs](https://neurips.cc/virtual/2026/poster/148164) | PubMedQA | Qwen3-14B, Qwen3-0.6B, Gemma3, Llama3 | 학습함 (RL) | LLM이 길고 잡음 많은 문맥 속 결정적 증거를 놓치는 문제 | 동결 Solver의 보상만으로 RL 학습한 Actor가 핵심 구간에 하이라이트 태그를 삽입하는 HiLight |
| 26 | [Learning to Follow In-Context Watermark Instructions via Self-Distillation](https://neurips.cc/virtual/2026/poster/150382) | BioASQ | Qwen3-14B, GPT-OSS-20B, GPT-5.4, Gemini-3-pro | 학습함 (SFT+RL) | LLM이 문맥 내 워터마크 지시를 답변 품질 저하 없이 따르는지 측정되지 않았다 | ICWBench를 만들고 로짓 섭동 자기증류와 검증기 보상 RL의 2단계 학습을 제안 |
| 27 | [Learning to Persuade Exposes How Easily LLMs Abandon Correct Beliefs](https://neurips.cc/virtual/2026/poster/148639) | MedQA | Qwen-2.5-7B-Instruct, Qwen-2.5-14B-Instruct, Llama-3.1-8B-Instruct, GPT-4o-mini | 학습함 (RL) | LLM이 단 한 번의 설득 논증에도 올바른 답을 쉽게 포기하는 취약성 | Persuadee의 답을 뒤집으면 보상하는 적대적 RL로 설득자 에이전트를 학습해 취약성을 노출 |
| 28 | [M^\star: Every Task Deserves Its Own Memory Harness](https://neurips.cc/virtual/2026/poster/155414) | HealthBench | GPT-5.4 Mini, GPT-5.3-Codex | 학습 없음 (prompting·agent·추론 기법) | LLM 에이전트의 메모리 하네스가 과제마다 달라야 하는데 고정 설계가 쓰이는 문제를 다룬다. | 메모리 하네스를 실행 가능한 파이썬 프로그램으로 보고 반성적 코드 진화로 과제별 최적 프로그램을 탐색한다. |
| 29 | [Measuring Black-Box Confidence via Reasoning Trajectories: Geometry, Coverage, and Verbalization](https://neurips.cc/virtual/2026/poster/155873) | MedQA, USMLE | Gemini 3.1 Pro, Claude Sonnet 4.6, GPT-5-mini | 학습 없음 (prompting·agent·추론 기법) | 텍스트 전용 API에서 CoT 추론의 신뢰도를 저비용으로 추정하기 어려운 문제를 다룬다. | CoT를 임베딩 궤적으로 보고 답 앵커로의 수렴을 1모수 소프트맥스로 측정해 커버리지·언어화 신뢰도와 융합한다. |
| 30 | [MedExAgent: Training LLM Agents to Ask, Examine, and Diagnose in Noisy Clinical Environments](https://neurips.cc/virtual/2026/poster/149616) | AgentClinic | Meditron3-8B, Aloe-Beta-70B, Qwen3-32B, HuatuoGPT-o1-70B | 학습함 (SFT+RL) | 기존 의료 LLM 평가·진단법은 잡음 있는 대화형 문진·검사 과정을 단순화해 무시한다. | 진단을 POMDP와 잡음 모델로 정식화하고 SFT 후 DAPO로 문진·검사·진단 에이전트를 학습한다. |
| 31 | [Medmarks: A Comprehensive Open-Source LLM Benchmark Suite for Medical Tasks](https://neurips.cc/virtual/2026/poster/139434) | AgentClinic, HealthBench, MedBullets, MedCalc-Bench, MedConceptsQA, MedMCQA, MedQA, MedXpertQA, MetaMedQA, PubMedQA | Gemini 3 Pro Preview, GPT-5.1, GPT-5.2, Grok 4 | 평가만 (벤치마크·분석) | 기존 의료 LLM 벤치마크는 포화되었거나 비공개 데이터 의존·모델 범위가 부족하다. | 30개 공개 의료 벤치마크를 묶은 MEDMARKS로 61개 모델·71개 설정을 체계적으로 평가한다. |
| 32 | [MindLoom: Composing Thought Modes for Frontier-Level Reasoning Data Synthesis](https://neurips.cc/virtual/2026/poster/155952) | MedQA | Qwen3-2507-4B, Qwen3-2507-8B, Qwen3.5-4B, Qwen3.5-9B | 학습함 (SFT) | 난이도 제어와 다양성을 갖춘 프런티어급 추론 데이터를 체계적으로 합성하기 어려운 문제를 다룬다. | 풀이를 사고 모드 사슬로 분해하고 검색된 사고 모드를 조합해 새 문제를 합성한 뒤 SFT 데이터로 쓴다. |
| 33 | [MoBayes: A Modular Bayesian Framework for Separating Reasoning from Language in Conversational Clinical Decision Support](https://neurips.cc/virtual/2026/poster/152953) | AgentClinic | GPT-5.4-nano, Gemini 3.1 Flash Lite, Llama-4-Scout, GPT-5.4 | 학습 없음 (prompting·agent·추론 기법) | 대화형 임상 의사결정 지원 LLM은 토큰 예측과 확률적 의사결정을 혼동해 사후확률 추적·보류가 어렵다. | LLM은 대화를 관찰로 파싱만 하고 베이지안 모듈이 사후 갱신·정보이득 질문·보류 결정을 수행한다. |
| 34 | [NeuronEye: Query-Guided Visual Concept Activation for Vision-Language Reasoning](https://neurips.cc/virtual/2026/poster/155426) | OmniMedVQA | Qwen2.5-VL-7B, LLaVA-1.6-7B | 학습함 (기타) | VLM의 밀집 은닉 상태에서 질의에 필요한 시각 증거를 분리·조절하기 어려운 문제를 다룬다. | 중간 표현에서 희소 개념 뉴런 어휘를 만들고 질의 관련 클러스터를 활성화해 시각 토큰에 주입하는 플러그인을 제안한다. |
| 35 | [OpenMedReason: Scientific Reasoning Supervision for Medical Vision–Language Models](https://neurips.cc/virtual/2026/poster/139693) | JAMA CC-MM, MedXpertQA, PMC-VQA, PathVQA, SLAKE, VQA-RAD | Qwen2.5-VL-7B, Lingshu 7B, OctoMed 7B, MedGemma 27B | 학습함 (SFT+RL) | 의료 LVLM의 추론 지도 데이터가 합성 CoT 위주라 시각·임상 근거에 기반한 추론이 부족하다. | 과학 논문 기반 추론 흔적을 담은 45만 건 의료 VQA 코퍼스로 SFT·GRPO 학습하고 세부 벤치를 제시한다. |
| 36 | [PAAC: Privacy-Aware Agentic Device-Cloud Collaboration](https://neurips.cc/virtual/2026/poster/149491) | MedQA | Qwen3-4B, Gemini 3 Flash, PAPILLON, PRISM | 학습 없음 (prompting·agent·추론 기법) | 클라우드 에이전트는 사용자 데이터를 노출하고 온디바이스 에이전트는 성능이 낮다 | 플래너-실행자 분리를 디바이스-클라우드 경계에 맞추고 타입 placeholder로 민감정보를 가리는 PAAC 제안 |
| 37 | [Pandora's AI Model Routing Box: Efficient Allocation with Costly Value Estimation](https://neurips.cc/virtual/2026/poster/148290) | BioASQ | Gemini-3.1-Flash-Lite, Gemini-2.5-Flash-Lite, Gemma3-4B | 학습함 (기타) | 모델 라우팅에서 전문가별 가치 추정 비용과 정확도 사이의 트레이드오프 | Pandora's Box로 정식화해 정보가치에 따라 고비용 추정기 호출을 결정하는 라우터 제안 |
| 38 | [PathNavigate: A Training-Free Pathology Agent with Surprise-Guided Scan and Shared Slide Memory for Whole-Slide VQA](https://neurips.cc/virtual/2026/poster/154224) | PathMMU, SlideBench-BCNB, WSI-VQA | Patho-R1-7B, Qwen3.5-4B, PathAgent, SlideChat | 학습 없음 (prompting·agent·추론 기법) | 기가픽셀 WSI-VQA에서 질문 중심 후보 선택은 질문에 없는 결정적 형태학 소견을 놓치기 쉽다. | 저배율 스캔과 공유 온라인 메모리로 이상 영역 풀을 만든 뒤 PLIP로 재순위해 고배율 근거로 답한다. |
| 39 | [Rational Tuning of LLM Cascades via Probabilistic Modeling](https://neurips.cc/virtual/2026/poster/156749) | MedMCQA | llama3.2-1b, llama3.1-8b, llama3.1-70b, llama3.1-405b | 학습 없음 (prompting·agent·추론 기법) | LLM 캐스케이드에서 모델 간 오류율 상호작용 때문에 신뢰도 임계값 조정이 어려운 문제를 다룬다. | LLM 연쇄의 결합 성능 분포를 마르코프-코퓰라 확률모형으로 모델링해 연속 최적화로 임계값을 조정한다. |
| 40 | [Recursive Multi-Agent Systems](https://neurips.cc/virtual/2026/poster/153292) | MedQA | Qwen3.5-4B, Qwen3.5-9B, Gemma3-4B-it, Llama3.2-3B-Instruct | 학습함 (기타) | 다중 에이전트 협업 자체를 재귀 계산으로 확장할 수 있는지의 문제 | 이종 에이전트를 잠재공간 RecursiveLink로 연결하고 내외부 루프로 공동 최적화하는 RecursiveMAS 제안 |
| 41 | [Rethinking Reward Models for Multi-Domain Test-Time Scaling](https://neurips.cc/virtual/2026/poster/156790) | MedQA | DeepSeek-R1-Distill-Qwen-14B, DeepSeek-R1-Distill-Llama-8B, Qwen3-8B, SmolLM3-3B | 학습함 (기타) | 수학 외 다중 도메인 테스트 시 스케일링에서 ORM과 PRM 중 어떤 보상모델이 나은지 불분명한 문제를 다룬다. | 판별·생성형 ORM/PRM 네 변형을 공통 프로토콜로 학습해 14개 도메인 Best-of-N 성능을 비교 평가한다. |
| 42 | [Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks](https://neurips.cc/virtual/2026/poster/153931) | HealthBench | Qwen3-4B, Llama3.1-8B, GPT-4o, Llama3.1-405B | 학습함 (RL) | 개방형 과제용 루브릭 생성이 커버리지·중복·방향 오류로 판정과 보상을 저하시키는 문제 | 루브릭을 재귀적으로 분해·필터링하고 상관 인지 가중치를 주는 RRD로 LLM 판정과 RFT 보상 개선 |
| 43 | [SCOPE: Self-Play via Co-Evolving Policies for Open-Ended Tasks](https://neurips.cc/virtual/2026/poster/148234) | HealthBench | Qwen2.5-7B-Instruct, Qwen3-8B, OLMo-3-7B-Instruct, DR Tulu | 학습함 (RL) | 개방형 과제의 셀프플레이 학습은 규칙 검증 정답이 없어 큐레이션 데이터·상위 모델 심판에 의존한다. | 과제 생성자와 해결자를 공진화시키고 고정된 초기 모델이 루브릭으로 채점하는 데이터 없는 셀프플레이를 제안한다. |
| 44 | [SkillGen: Verified Inference-Time Agent Skill Synthesis](https://neurips.cc/virtual/2026/poster/148850) | PubMedQA | Gemma-4-26B, Llama-3.1-8B, Qwen-2.5-7B, GPT-5.4-Mini | 학습 없음 (prompting·agent·추론 기법) | 고품질 에이전트 스킬이 여전히 수작업으로 작성된다 | 성공·실패 궤적의 대조 유도와 개입 기반 검증으로 단일 스킬을 자동 합성하는 SkillGen 제안 |
| 45 | [Strong Teacher Not Needed? On Distillation in LLM Pretraining](https://neurips.cc/virtual/2026/poster/153838) | MedMCQA, PubMedQA | 1.7B student (distillation pretraining), 0.7B teacher, 1.7B teacher, 3.8B teacher | 학습함 (사전학습) | LLM 사전학습 증류에서 강한 교사가 항상 더 나은 학생을 만드는지의 문제 | 교사·학생 크기와 토큰 수, 손실 혼합비를 바꿔 약→강·동급·강→약 증류 효과를 체계적으로 측정 |
| 46 | [Teach-to-Reason: Competition-Guided Reasoning with a Self-Improving Teacher](https://neurips.cc/virtual/2026/poster/150121) | Chest_X-Ray_PA, Covid19_heywhale, MIMIC-CXR-VQA, Medical-CXR-VQA, SLAKE, VQA-RAD | Qwen3-VL-Instruct 2B, Qwen3-VL-Instruct 4B | 학습함 (RL) | 흉부 X선 VQA에서 정답 수준 보상만으로는 CoT 품질 개선이 어렵고 그룹 이점이 0으로 붕괴한다. | 자기경쟁으로 강화되는 Teacher와 비교해 보상을 받는 Reasoner를 사례별 보상 설계로 GRPO 학습한다. |
| 47 | [Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck](https://neurips.cc/virtual/2026/poster/153345) | HealthBench | Qwen3.5-35B-A3B, Qwen3.5-9B, OLMo3, Skywork-Reward-V2-Llama-3.1-8B | 평가만 (벤치마크·분석) | 검증이 어려운 개방형 생성 과제에서 테스트타임 스케일링이 왜 잘 안 되는가 | 5개 TTS 기법을 연산량 정규화해 비교하고 탐색·활용으로 분해해 보상모델 선택 실패를 측정 |
| 48 | [Towards a Universal Causal Reasoner](https://neurips.cc/virtual/2026/poster/153248) | PubMedQA | Qwen3-4B, Qwen3-8B, Olmo-3-7B-Instruct, GPT-5.4-mini | 학습함 (SFT) | LLM의 일반화 가능한 인과 추론 학습용 데이터가 부족한 문제 | 18개 인과 질의 유형을 기호·코드·자연어로 생성하는 UniCo 데이터로 SFT해 인과 추론과 추론 충실도 향상 |
| 49 | [Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows](https://neurips.cc/virtual/2026/poster/153005) | MedQA | Qwen3-14B, KVLINK, CacheBlend, APE | 학습함 (SFT) | 병렬 에이전트 분기를 텍스트 연결로 합성해 구조를 잃고 prefill 비용이 크다 | 병렬 작업자의 KV 캐시를 보정해 합성기가 직접 소비하게 하는 Parallel-Synthesis 제안 |
| 50 | [Uncertainty Quantification for Multimodal Large Language Models with Incoherence-adjusted Semantic Volume](https://neurips.cc/virtual/2026/poster/152113) | VQA-RAD | Llava-v1.5-13b, Phi-4-multimodal-instruct, LLaVA-NeXT-Video-7b-hf | 학습 없음 (prompting·agent·추론 기법) | MLLM의 불확실성 지표가 모달리티 한정·외부 도구 의존·고비용이다 | 샘플 응답의 비일관성 보정 의미 부피로 불확실성을 재는 학습 불필요 UMPIRE 제안 |
| 51 | [Unveiling Implicit Advantage Symmetry: Why GRPO Struggles with Exploration and Difficulty Adaptation](https://neurips.cc/virtual/2026/poster/153467) | OmniMedVQA, PMC-VQA, PathVQA, SLAKE, VQA-RAD | Qwen2.5-VL-3B-Instruct, Qwen2.5-Math-7B, DeepSeek-R1-7B | 학습함 (RL) | GRPO의 그룹 상대 이점 추정에 내재한 대칭성이 탐색과 난이도 적응을 저해하는 문제 | 정답 궤적 이점을 비대칭 축소하고 쉬운→어려운 샘플로 초점을 옮기는 A-GRAE 제안 |

### 성능 비교

각 논문이 보고한 대표 수치다. **논문마다 모델·프롬프트·평가 분할·지표가 달라 논문끼리 숫자를 직접 비교하면 안 된다.** 같은 행의 "비교 대상"과의 차이만 그 논문 안에서 의미가 있다.

| 벤치마크 | 논문 | 모델 | 설정 | 지표 | 값 | 비교 대상 | 비교 값 |
|---|---|---|---|---|---:|---|---:|
| AgentClinic-MedQA | [MedExAgent](https://neurips.cc/virtual/2026/poster/149616) | MedExAgent-8B | proposed method (SFT + DAPO), OOD test | Acc (LLM-judge strict accuracy) | 0.378 | Aloe-Beta-70B | 0.395 |
| AgentClinic-MedQA | [MedExAgent](https://neurips.cc/virtual/2026/poster/149616) | MedExAgent-8B | proposed method (SFT + DAPO), OOD test | Sim (embedding cosine similarity) | 0.672 | Aloe-Beta-70B | 0.684 |
| AgentClinic-MedQA | [MoBayes](https://neurips.cc/virtual/2026/poster/152953) | GPT-5.4-nano | MOBAYES + GPT-5.4-nano sensor (n=50) | DHS | 86.8 | SA Gemini 3.1 Pro (standalone doctor) | 80.4 |
| AgentClinic-MedQA | [MoBayes](https://neurips.cc/virtual/2026/poster/152953) | Gemini 3.1 Flash Lite | MOBAYES + Gemini 3.1 Flash Lite sensor (n=50) | Top-1 accuracy | 78 | SA Gemini 3.1 Pro (standalone doctor) | 66 |
| AgentClinic-MedQA | [MoBayes](https://neurips.cc/virtual/2026/poster/152953) | gpt-5.4-nano | MOBAYES (n=100) | DHS | 83 | MEDDxAgent (closed-world abl.) | 89 |
| BioASQ | [ARC-Encoder](https://neurips.cc/virtual/2026/poster/156755) | Mistral 7B | proposed method (ARC4-EncoderM, 4x compression) | F1 | 75.6 | LLMLingua2 | 73.4 |
| BioASQ | [ARC-Encoder](https://neurips.cc/virtual/2026/poster/156755) | Llama3.1 8B | proposed method (ARC4-EncoderL, 4x compression) | F1 | 77.1 | open-book | 77.2 |
| BioASQ | [Entropy Distribution as a Fingerprint for Hallucinations in Generative Models](https://neurips.cc/virtual/2026/poster/148328) | open-weight models (median) | CES (proposed method) | AUROC | 0.592 | API models (median) | 0.694 |
| BioASQ | [Fix the Structural Bottleneck](https://neurips.cc/virtual/2026/poster/152205) | Llama-3.2-1B-Base | ComprExIT (out-of-domain) | F1 | 63.74 | ICAE | 54.09 |
| BioASQ | [Learning to Follow In-Context Watermark Instructions via Self-Distillation](https://neurips.cc/virtual/2026/poster/150382) | Qwen3-14B | proposed method (unseen domain) | TSP AUC | 0.941 | Base Qwen3-14B | 0.585 |
| BioASQ | [Learning to Follow In-Context Watermark Instructions via Self-Distillation](https://neurips.cc/virtual/2026/poster/150382) | Qwen3-14B | proposed method (unseen domain) | WIP AUC | 0.996 | Base Qwen3-14B | 0.502 |
| EHRNoteQA | [EHRNote-ChatQA](https://neurips.cc/virtual/2026/poster/139551) | gpt-5.4 | single-turn reference evaluation | accuracy (%) | 95.63 | EHRNote-ChatQA QA-level Content | 98.33 |
| EHRNoteQA | [EHRNote-ChatQA](https://neurips.cc/virtual/2026/poster/139551) | DeepSeek-R1-Distill-Qwen-7B | single-turn reference evaluation | accuracy (%) | 80.15 | EHRNote-ChatQA QA-level Content | 27.05 |
| EHRNoteQA | [EHRNote-ChatQA](https://neurips.cc/virtual/2026/poster/139551) | Ministral-3-14B-Instruct-2512 | single-turn reference evaluation | accuracy (%) | 91.68 | EHRNote-ChatQA QA-level Content | 31.56 |
| EHRNoteQA | [EHRNote-ChatQA](https://neurips.cc/virtual/2026/poster/139551) | medgemma-27b-it | single-turn reference evaluation | accuracy (%) | 91.06 | EHRNote-ChatQA QA-level Content | 87.76 |
| HealMed-VQA | [CRAFT](https://neurips.cc/virtual/2026/poster/149960) | Hulu-Med 4B | CRAFT brake head excision under visual degradation | UR (unknown rate) | 98.20 | Baseline | 78.44 |
| HealthBench | [CLR-voyance ](https://neurips.cc/virtual/2026/poster/150688) | Qwen3-8B | CLR-voyance-8B | score | 0.415 | Qwen3-8B base | 0.364 |
| HealthBench | [Experience Makes Skillful](https://neurips.cc/virtual/2026/poster/150444) | DeepSeek-V3.2 | SkeMex, offline in-domain | rubric score | 27.65 | ReAct | 19.06 |
| HealthBench | [Focal Reward](https://neurips.cc/virtual/2026/poster/150481) | Qwen2.5-7B-Instruct | Focal Reward (uniform) | score (%) | 42.16 | Static (prior) | 40.65 |
| HealthBench | [Focal Reward](https://neurips.cc/virtual/2026/poster/150481) | Qwen3-8B | Focal Reward (uniform) | score (%) | 48.81 | Static (prior) | 47.37 |
| HealthBench | [SCOPE](https://neurips.cc/virtual/2026/poster/148234) | Qwen3-8B | SCOPE iter3 | score | 28.1 | Qwen3-8B (base) | 25.9 |
| HealthBench | [SCOPE](https://neurips.cc/virtual/2026/poster/148234) | Qwen2.5-7B | SCOPE iter3 | score | 20.1 | GRPOdata | 20.7 |
| HealthBench | [SCOPE](https://neurips.cc/virtual/2026/poster/148234) | OLMo-3-7B | SCOPE iter3 | score | 21.2 | OLMo-3-7B (base) | 16.2 |
| HealthBench | [SCOPE](https://neurips.cc/virtual/2026/poster/148234) | SCOPE (Qwen3-8B) | proposed method, unified retrieval/judge reference evaluation | score | 28.1 | DR Tulu | 25.3 |
| HealthBench | [Test-Time Scaling in the Wild](https://neurips.cc/virtual/2026/poster/153345) | Qwen3.5-35B-A3B | Fusion, XHigh compute | realised quality score | 0.588 | BoN@1 single-sample baseline | 0.536 |
| HealthBench | [Test-Time Scaling in the Wild](https://neurips.cc/virtual/2026/poster/153345) | Qwen3.5-35B-A3B | BoN+Skywork, XHigh compute | realised quality score | 0.539 | BoN@1 single-sample baseline | 0.536 |
| HealthBench | [Test-Time Scaling in the Wild](https://neurips.cc/virtual/2026/poster/153345) | Qwen3.5-35B-A3B | Sequential Refinement, XHigh compute | realised quality score | 0.513 | BoN@1 single-sample baseline | 0.536 |
| HealthBench (Data) | [M^\star](https://neurips.cc/virtual/2026/poster/155414) | GPT-5.4 Mini | proposed method (MSTAR) | rubric score | 0.390 | GEPA + Vector Search | 0.327 |
| HealthBench (Data) | [M^\star](https://neurips.cc/virtual/2026/poster/155414) | GPT-5.4 Mini | No Memory baseline | rubric score | 0.242 |  |  |
| HealthBench (Emerg.) | [M^\star](https://neurips.cc/virtual/2026/poster/155414) | GPT-5.4 Mini | proposed method (MSTAR) | rubric score | 0.493 | Dynamic Cheatsheet | 0.487 |
| HealthBench-Hard | [Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks](https://neurips.cc/virtual/2026/poster/153931) | Qwen3-4B | RRDWU-rewarded RFT policy | Overall (%) | 61.7 | Base Model (pre-RFT) | 55.9 |
| HealthBench-Hard | [Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks](https://neurips.cc/virtual/2026/poster/153931) | Llama3.1-8B | RRDWU-rewarded RFT policy | Overall (%) | 49.3 | Base Model (pre-RFT) | 37.1 |
| HealthBench-Hard | [Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks](https://neurips.cc/virtual/2026/poster/153931) | Qwen3-4B | RRDWU-rewarded RFT policy | Overall (%) | 61.7 | Chasing the Tail | 58.7 |
| HuatuoGPT-Vision CT300 | [Unveiling Implicit Advantage Symmetry](https://neurips.cc/virtual/2026/poster/153467) | Qwen2.5-VL-3B-Instruct | Dr.GRPO + A-GRAE | Pass@1 | 73.6 | Dr.GRPO | 72.4 |
| HuatuoGPT-Vision MRI300 | [Unveiling Implicit Advantage Symmetry](https://neurips.cc/virtual/2026/poster/153467) | Qwen2.5-VL-3B-Instruct | GRPO + A-GRAE | Pass@1 | 88.2 | GRPO | 87.2 |
| HuatuoGPT-Vision Xray300 | [Unveiling Implicit Advantage Symmetry](https://neurips.cc/virtual/2026/poster/153467) | Qwen2.5-VL-3B-Instruct | GRPO + A-GRAE | Pass@1 | 71.3 | GRPO | 63.2 |
| HuatuoGPT-Vision Xray300 | [Unveiling Implicit Advantage Symmetry](https://neurips.cc/virtual/2026/poster/153467) | Qwen2.5-VL-3B-Instruct | Dr.GRPO + A-GRAE | Pass@1 | 72.0 | Dr.GRPO | 69.5 |
| MedCalc | [CLR-voyance ](https://neurips.cc/virtual/2026/poster/150688) | Qwen3-8B | CLR-voyance-8B (Qwen3-∆) | accuracy | 46.0 | Qwen3-8B base | 41.5 |
| MedCalc-Bench | [Medmarks](https://neurips.cc/virtual/2026/poster/139434) | 61 models (mean) | mean score across evaluated models (no calculator tool) | mean score | 0.439 |  |  |
| Medicine (VQA-RAD, PathVQA, SLAKE) | [InduceKV](https://neurips.cc/virtual/2026/poster/153680) | LLaVA-1.5 | INDUCEKV (matched), domain-incremental CIT | Med. Avg | 68.92 | SMoE | 67.70 |
| Medicine (VQA-RAD, PathVQA, SLAKE) | [InduceKV](https://neurips.cc/virtual/2026/poster/153680) | LLaVA-OV-4B | INDUCEKV (default), domain-incremental CIT | Med. Avg | 69.45 | SMoE | 67.70 |
| MedMCQA | [AgentArk](https://neurips.cc/virtual/2026/poster/149790) | Qwen3-8B | PAD distillation from Qwen3-32B (appendix table, medmcqa cell) | accuracy | 63.12 | original Qwen3-8B | 59.65 |
| MedMCQA | [AgentArk](https://neurips.cc/virtual/2026/poster/149790) | Qwen3-8B | PAD distillation from Qwen3-32B, AgentVerse protocol | accuracy | 59.78 | Single agent | 59.65 |
| MedMCQA | [AgentArk](https://neurips.cc/virtual/2026/poster/149790) | LLaMA3-8B-Instruct | RSFT distillation from Qwen3-32B (appendix table) | accuracy | 61.15 | original LLaMA3-8B-Instruct | 56.9 |
| MedMCQA | [Beyond LoRA vs. Full Fine-Tuning](https://neurips.cc/virtual/2026/poster/154880) | Qwen2.5-3B | proposed method (MoLF) | accuracy | 60.60 | FFT | 59.55 |
| MedMCQA | [Beyond LoRA vs. Full Fine-Tuning](https://neurips.cc/virtual/2026/poster/154880) | Qwen2.5-1.5B | proposed method (MoLF) | accuracy | 56.28 | FFT | 55.39 |
| MedMCQA | [Beyond LoRA vs. Full Fine-Tuning](https://neurips.cc/virtual/2026/poster/154880) | Qwen2.5-3B | LoRA (r = 128) | accuracy | 61.85 | FFT | 59.55 |
| MedMCQA | [CLR-voyance ](https://neurips.cc/virtual/2026/poster/150688) | Qwen3-8B | CLR-voyance-8B (Qwen3-∆, GRPO + DELLA-Linear merge) | accuracy | 67.0 | Qwen3-8B base | 66.0 |
| MedMCQA | [CLR-voyance ](https://neurips.cc/virtual/2026/poster/150688) | MedGemma-4B-IT | MG-B (GRPO + Breadcrumbs merge) | accuracy | 61.0 | MG-4B base | 54.5 |
| MedMCQA | [Communication-Efficient LLM Adaptation over Decentralized GPU Meshes](https://neurips.cc/virtual/2026/poster/153942) | Llama-3.2-1B | M95+AP (95% activation masking + Anchor Priors) | Acc. | 0.320 | Baseline (dense PP, uncompressed DP) | 0.330 |
| MedMCQA | [Decentralized Aggregation of LLM Predictions via Wagering Mechanisms](https://neurips.cc/virtual/2026/poster/150523) | 4 heterogeneous models | WALLA I | ACC | 81.17 | StackedGen | 82.66 |
| MedMCQA | [Efficiently Aligning Draft Models via Parameter- and Data-Efficient Adaptation](https://neurips.cc/virtual/2026/poster/153042) | Meditron3-Qwen2.5-7B | EDA (Ours), T=0, average acceptance length τ | average acceptance length τ | 4.30 | Full-FT | 3.97 |
| MedMCQA | [From Talking Words to Sharing Thoughts](https://neurips.cc/virtual/2026/poster/154681) | 7-8B expert ensemble | proposed method (Relational Aggregation) | accuracy | 62.83 | GoAMax | 60.04 |
| MedMCQA | [From Talking Words to Sharing Thoughts](https://neurips.cc/virtual/2026/poster/154681) | 7-8B expert ensemble | proposed method (Relational Aggregation) | accuracy | 62.83 | MoA | 54.94 |
| MedMCQA | [From Talking Words to Sharing Thoughts](https://neurips.cc/virtual/2026/poster/154681) | Bio-Medical-Llama-3-8B | single-agent expert | accuracy | 47.00 |  |  |
| MedMCQA | [Medmarks](https://neurips.cc/virtual/2026/poster/139434) | 61 models (mean) | mean score across evaluated models | mean score | 0.656 |  |  |
| MedMCQA | [Rational Tuning of LLM Cascades via Probabilistic Modeling](https://neurips.cc/virtual/2026/poster/156749) | Llama3 cascades | proposed method (Rational Tuning) | area under error-cost curve (lower is better) | 0.381 | Bayesian optimization | 0.389 |
| MedMCQA | [Rational Tuning of LLM Cascades via Probabilistic Modeling](https://neurips.cc/virtual/2026/poster/156749) | Llama3 cascades | proposed method (Rational Tuning), low-sample n ≤ 30 | area under error-cost curve (lower is better) | 0.399 | Bayesian optimization | 0.419 |
| MedMCQA | [Rational Tuning of LLM Cascades via Probabilistic Modeling](https://neurips.cc/virtual/2026/poster/156749) | gpt-4o | zero-shot single model | %Corr | 76.5 |  |  |
| MedMCQA | [Strong Teacher Not Needed? On Distillation in LLM Pretraining](https://neurips.cc/virtual/2026/poster/153838) | 1.7B student | distilled student (0.7B arch. 10B tokens teacher, α=0.2) | accuracy | 27.8 | standard pretrained student baseline | 24.5 |
| MedQA | [Agentic Multi-Turn Reasoning](https://neurips.cc/virtual/2026/poster/149499) | Qwen2.5-7B-Instruct | Φ-MPO | accuracy | 86.0 | Flow-GRPO | 80.0 |
| MedQA | [Agentic Multi-Turn Reasoning](https://neurips.cc/virtual/2026/poster/149499) | Qwen3.5-9B | Φ-MPO | accuracy | 90.0 |  |  |
| MedQA | [Aligning Language Models with Selective Prediction](https://neurips.cc/virtual/2026/poster/148722) | Qwen2.5-7B | RLSR (proposed method), target accuracy 75% | Test Acc. | 78.9% | RLCR | 72.2% |
| MedQA | [Aligning Language Models with Selective Prediction](https://neurips.cc/virtual/2026/poster/148722) | Qwen2.5-7B | RLSR (proposed method), validation set | AURC | 0.357 | RLCR | 0.361 |
| MedQA | [Communication-Efficient LLM Adaptation over Decentralized GPU Meshes](https://neurips.cc/virtual/2026/poster/153942) | Llama-3.2-1B | M95+AP (95% activation masking + Anchor Priors) | Acc. | 0.321 | Baseline (dense PP, uncompressed DP) | 0.280 |
| MedQA | [Communication-Efficient LLM Adaptation over Decentralized GPU Meshes](https://neurips.cc/virtual/2026/poster/153942) | Llama-3.2-1B | M90+AP (90% activation masking + Anchor Priors) | Acc. | 0.325 | Baseline (dense PP, uncompressed DP) | 0.280 |
| MedQA | [Conformal Selective Acting](https://neurips.cc/virtual/2026/poster/148731) | Fleming-R1 | CSA action rate at α⋆=0.20 | AR | 39.4% |  |  |
| MedQA | [Conformal Selective Acting](https://neurips.cc/virtual/2026/poster/148731) | Fleming-R1 | CSA selective risk at α⋆=0.20 | Risk | 11.4% |  |  |
| MedQA | [Efficiently Aligning Draft Models via Parameter- and Data-Efficient Adaptation](https://neurips.cc/virtual/2026/poster/153042) | Meditron3-Qwen2.5-7B | EDA (Ours), T=1, average acceptance length τ | average acceptance length τ | 3.25 | Full-FT | 2.72 |
| MedQA | [INFUSER](https://neurips.cc/virtual/2026/poster/153094) | Qwen3-4B-Base | INFUSER (mean over 3 seeds) | accuracy | 58.86 | Base | 55.46 |
| MedQA | [INFUSER](https://neurips.cc/virtual/2026/poster/153094) | Qwen3-8B-Base | INFUSER (mean over 3 seeds) | accuracy | 65.78 | Base | 64.18 |
| MedQA | [Learning to Persuade Exposes How Easily LLMs Abandon Correct Beliefs](https://neurips.cc/virtual/2026/poster/148639) | Persuader Qwen 7B (RL) vs Persuadee Qwen 7B | RL-trained Persuader | Persuasion Success Rate (%) | 90.5 | base Qwen 7B Persuader | 20.8 |
| MedQA | [Learning to Persuade Exposes How Easily LLMs Abandon Correct Beliefs](https://neurips.cc/virtual/2026/poster/148639) | Persuader Qwen 7B (RL) vs Persuadee gpt-4o-mini | RL-trained Persuader | Persuasion Success Rate (%) | 10.9 | base Qwen 7B Persuader | 0.6 |
| MedQA | [Learning to Persuade Exposes How Easily LLMs Abandon Correct Beliefs](https://neurips.cc/virtual/2026/poster/148639) | Persuader Qwen 7B (RL-cont) vs Persuadee gpt-4o-mini | continual RL training | Persuasion Success Rate (%) | 15.0 | Qwen 7B (RL) | 10.9 |
| MedQA | [Measuring Black-Box Confidence via Reasoning Trajectories](https://neurips.cc/virtual/2026/poster/155873) | Gemini 3.1 Pro | proposed method (Geo, blinded option-anchor) | selective-prediction AUC | 0.821 | No-Geo | 0.577 |
| MedQA | [Measuring Black-Box Confidence via Reasoning Trajectories](https://neurips.cc/virtual/2026/poster/155873) | Claude Sonnet 4.6 | proposed method (Geo, blinded option-anchor) | selective-prediction AUC | 0.753 | No-Geo | 0.519 |
| MedQA | [Measuring Black-Box Confidence via Reasoning Trajectories](https://neurips.cc/virtual/2026/poster/155873) | Gemini 3.1 Pro | geometric composite | AUC | 0.821 | DeBERTa-MNLI semantic entropy | 0.590 |
| MedQA | [Medmarks](https://neurips.cc/virtual/2026/poster/139434) | 61 models (mean) | mean score across evaluated models | mean score | 0.784 |  |  |
| MedQA | [MindLoom](https://neurips.cc/virtual/2026/poster/155952) | Qwen3-2507 4B | proposed method (MINDLOOM SFT), pass@1 | pass@1 (%) | 65.12 | Base | 62.69 |
| MedQA | [MindLoom](https://neurips.cc/virtual/2026/poster/155952) | Qwen3-2507 8B | proposed method (MINDLOOM SFT), pass@1 | pass@1 (%) | 70.77 | Base | 63.00 |
| MedQA | [MindLoom](https://neurips.cc/virtual/2026/poster/155952) | Qwen3.5 9B | proposed method (MINDLOOM SFT), pass@1 | pass@1 (%) | 86.80 | Base | 78.71 |
| MedQA | [MindLoom](https://neurips.cc/virtual/2026/poster/155952) | Qwen3.5 9B | proposed method (MINDLOOM SFT), pass@1 | pass@1 (%) | 86.80 | MegaScience | 81.30 |
| MedQA | [PAAC](https://neurips.cc/virtual/2026/poster/149491) | Qwen3-4B + Gemini 3 Flash | PAAC, average over P0/P1 | Acc. (%) | 88.2 | PAPILLON + ReAct | 78.2 |
| MedQA | [PAAC](https://neurips.cc/virtual/2026/poster/149491) | Qwen3-4B + Gemini 3 Flash | PAAC, P1 privacy level | Leak (%) | 18.4 | PAPILLON + ReAct | 45.5 |
| MedQA | [Recursive Multi-Agent Systems](https://neurips.cc/virtual/2026/poster/153292) | RecursiveMAS (Scaled agents) | RecursiveMAS, recursion round r=3 | accuracy (%) | 79.3 | TextGrad | 77.2 |
| MedQA | [Recursive Multi-Agent Systems](https://neurips.cc/virtual/2026/poster/153292) | RecursiveMAS (Scaled agents) | RecursiveMAS, recursion round r=3 | accuracy (%) | 79.3 | Single Agent (w/ Full-SFT) | 77.0 |
| MedQA | [Recursive Multi-Agent Systems](https://neurips.cc/virtual/2026/poster/153292) | RecursiveMAS (Scaled agents) | RecursiveMAS, recursion round r=1 | accuracy (%) | 78.2 | Recursive-TextMAS | 76.1 |
| MedQA | [Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows](https://neurips.cc/virtual/2026/poster/153005) | Qwen3-14B | Parallel-Synthesis | Accuracy | 83.58 | Text-Serialization | 82.72 |
| MedQA-200 subset | [Demystifying Numerical Errors in LLM Inference](https://neurips.cc/virtual/2026/poster/155629) | Qwen3-32B | H100 FP32 LayerCast ground truth | accuracy | 175/200 |  |  |
| MedQA-200 subset | [Demystifying Numerical Errors in LLM Inference](https://neurips.cc/virtual/2026/poster/155629) | Qwen3-14B | H100 FP32 LayerCast ground truth | accuracy | 161/200 |  |  |
| MedQA-200 subset | [Demystifying Numerical Errors in LLM Inference](https://neurips.cc/virtual/2026/poster/155629) | Llama-3.1-8B-Instruct | H100 FP32 LayerCast ground truth | accuracy | 137/200 |  |  |
| MedQA-USMLE | [Efficiently Aligning Draft Models via Parameter- and Data-Efficient Adaptation](https://neurips.cc/virtual/2026/poster/153042) | Meditron3-Qwen2.5-7B | EDA (Ours), T=0, average acceptance length τ | average acceptance length τ | 4.34 | Full-FT | 3.97 |
| MedXpertQA | [Experience Makes Skillful](https://neurips.cc/virtual/2026/poster/150444) | DeepSeek-V3.2 | SkeMex, offline in-domain (text) | accuracy | 35.68 | ReAct | 33.51 |
| MedXpertQA | [Experience Makes Skillful](https://neurips.cc/virtual/2026/poster/150444) | Qwen3.6-Plus | SkeMex, offline in-domain (multimodal) | accuracy | 54.73 | ReAct | 47.30 |
| MedXpertQA | [INFUSER](https://neurips.cc/virtual/2026/poster/153094) | Qwen3-4B-Base | INFUSER (mean over 3 seeds) | accuracy | 13.78 | Base | 13.02 |
| MedXpertQA | [INFUSER](https://neurips.cc/virtual/2026/poster/153094) | Qwen3-8B-Base | INFUSER (mean over 3 seeds) | accuracy | 15.25 | Base | 14.49 |
| MedXpertQA | [Medmarks](https://neurips.cc/virtual/2026/poster/139434) | 61 models (mean) | mean score across evaluated models | mean score | 0.236-0.237 |  |  |
| MedXpertQA | [OpenMedReason](https://neurips.cc/virtual/2026/poster/139693) | Qwen2.5-VL-7B | SFT + GRPO on OpenMedReason | accuracy (%) | 24.95 | Qwen2.5-VL-7B (Base) | 22.62 |
| MedXpertQA (Text) | [Group Perspective Matters](https://neurips.cc/virtual/2026/poster/154678) | Claude-4.5-Sonnet | DEAR (Ours) | Acc. | 40.0 | MAD | 35.0 |
| MedXpertQA (Text) | [Group Perspective Matters](https://neurips.cc/virtual/2026/poster/154678) | Gemini-3.1-Flash-Lite | DEAR (Ours) | Acc. | 59.0 | MAD | 54.0 |
| MedXpertQA (Text) | [Group Perspective Matters](https://neurips.cc/virtual/2026/poster/154678) | Gemini-3.1-Flash-Lite | DEAR (Ours) | Acc. | 59.0 | MAD-M2(S) | 55.0 |
| MIMIC-CXR-VQA | [Teach-to-Reason](https://neurips.cc/virtual/2026/poster/150121) | Qwen3-VL-Instruct 4B | T2R-R3 | accuracy | 28.04 | Base Model | 20.45 |
| MMedC | [From Experts to Sub-experts](https://neurips.cc/virtual/2026/poster/155254) | OLMoE | proposed method (NSFT-OLMoE) | accuracy | 45.81 | ESFT-OLMoE | 44.31 |
| MMedC | [From Experts to Sub-experts](https://neurips.cc/virtual/2026/poster/155254) | OLMoE | proposed method (NSFT-OLMoE) | accuracy | 45.81 | Full FT | 52.12 |
| MMMU | [Experience Makes Skillful](https://neurips.cc/virtual/2026/poster/150444) | DeepSeek-V3.2 | SkeMex, offline in-domain (Health & Medicine, multimodal) | accuracy | 66.91 | ReAct | 46.04 |
| OmniMedVQA-Mini | [NeuronEye](https://neurips.cc/virtual/2026/poster/155426) | Qwen2.5-VL-7B | proposed method (NeuronEye) | overall accuracy | 63.10% | Base Qwen2.5-VL | 65.30% |
| OmniMedVQA-Mini (Disease Diagnosis) | [NeuronEye](https://neurips.cc/virtual/2026/poster/155426) | Qwen2.5-VL-7B | proposed method (NeuronEye) | accuracy | 60.94% | Base Qwen2.5-VL | 63.74% |
| PathVQA | [OpenMedReason](https://neurips.cc/virtual/2026/poster/139693) | Qwen2.5-VL-7B | SFT + GRPO on OpenMedReason | accuracy (%) | 64.10 | Qwen2.5-VL-7B (Base) | 62.88 |
| PubMedQA | [ARC-Encoder](https://neurips.cc/virtual/2026/poster/156755) | Mistral 7B | proposed method (ARC4-EncoderM, 4x compression) | F1 | 76.6 | LLMLingua2 | 74.4 |
| PubMedQA | [ARC-Encoder](https://neurips.cc/virtual/2026/poster/156755) | Llama3.1 8B | proposed method (ARC4-EncoderL, 4x compression) | F1 | 81.1 | open-book | 84.0 |
| PubMedQA | [Beyond Raw Context Transfer](https://neurips.cc/virtual/2026/poster/150023) | Qwen3-8B | FedRepRAG (β = 0.1) | accuracy | 59.40 | Direct Inference | 54.00 |
| PubMedQA | [Beyond Raw Context Transfer](https://neurips.cc/virtual/2026/poster/150023) | Qwen3-8B | FedRepRAG (β = 0.5) | accuracy | 58.40 | Local IC-RAG | 15.40 |
| PubMedQA | [CRAFT](https://neurips.cc/virtual/2026/poster/149960) | Qwen3-4B | CRAFT, Prefix textual conflict (validation) | CFR (lower is better) | 23.59 | Baseline | 49.67 |
| PubMedQA | [Decentralized Aggregation of LLM Predictions via Wagering Mechanisms](https://neurips.cc/virtual/2026/poster/150523) | Aloe (4 homogeneous models, private contexts) | WALLA I | ACC | 87.00 | StackedGen | 87.76 |
| PubMedQA | [Efficiently Aligning Draft Models via Parameter- and Data-Efficient Adaptation](https://neurips.cc/virtual/2026/poster/153042) | Meditron3-Qwen2.5-7B | EDA (Ours), T=0, average acceptance length τ | average acceptance length τ | 4.03 | Full-FT | 3.86 |
| PubMedQA | [Learning Evidence Highlighting for Frozen LLMs](https://neurips.cc/virtual/2026/poster/148164) | Qwen3-14B (frozen Solver) | HiLight (proposed method) | Acc. | 0.940 | DSPy (MIPROv2) | 0.930 |
| PubMedQA | [Learning Evidence Highlighting for Frozen LLMs](https://neurips.cc/virtual/2026/poster/148164) | Qwen3-14B (frozen Solver) | HiLight (proposed method) | M-F1 | 0.821 | MI (manual instruction) | 0.776 |
| PubMedQA | [SkillGen](https://neurips.cc/virtual/2026/poster/148850) | Llama-3.1-8B | SkillGen skill-augmented | accuracy | 69.00% | no-skill baseline | 62.00% |
| PubMedQA | [SkillGen](https://neurips.cc/virtual/2026/poster/148850) | GPT-5.4-Mini | SkillGen skill-augmented | accuracy | 72.00% | no-skill baseline | 68.00% |
| PubMedQA | [Strong Teacher Not Needed? On Distillation in LLM Pretraining](https://neurips.cc/virtual/2026/poster/153838) | 1.7B student | distilled student (8.0B arch. 100B tokens teacher, α=0.8) | perplexity (lower is better) | 23.72 | standard pretrained student baseline | 24.77 |
| RFEval medical understanding (PubMedQA) | [Towards a Universal Causal Reasoner](https://neurips.cc/virtual/2026/poster/153248) | Qwen3-4B | Qwen3-4B + UNICO (SFT) | reasoning faithfulness (%) | 94.6 | Qwen3-4B base | 31.2 |
| RFEval medical understanding (PubMedQA) | [Towards a Universal Causal Reasoner](https://neurips.cc/virtual/2026/poster/153248) | Qwen3-8B | Qwen3-8B + UNICO (SFT) | reasoning faithfulness (%) | 90.5 | Qwen3-8B base | 47.4 |
| RFEval medical understanding (PubMedQA) | [Towards a Universal Causal Reasoner](https://neurips.cc/virtual/2026/poster/153248) | Olmo-3-7B-Instruct | Olmo-3-7B-Instruct + UNICO (SFT) | reasoning faithfulness (%) | 81.6 | Olmo-3-7B-Instruct base | 71.0 |
| SLAKE | [CRAFT](https://neurips.cc/virtual/2026/poster/149960) | Hulu-Med 4B | CRAFT brake head excision under visual degradation | UR (unknown rate) | 65.15 | Baseline | 37.88 |
| SLAKE | [OpenMedReason](https://neurips.cc/virtual/2026/poster/139693) | Qwen2.5-VL-7B | SFT + GRPO on OpenMedReason | accuracy (%) | 85.10 | Qwen2.5-VL-7B (Base) | 62.26 |
| SLAKE | [Teach-to-Reason](https://neurips.cc/virtual/2026/poster/150121) | Qwen3-VL-Instruct 4B | T2R-R2 | accuracy | 64.92 | Base Model | 58.11 |
| SLAKE-EN | [Beyond Raw Context Transfer](https://neurips.cc/virtual/2026/poster/150023) | Qwen2.5-VL-7B | FedRepRAG (β = 0.1) | accuracy | 63.71 | Direct Inference | 49.58 |
| SLAKE-EN | [Beyond Raw Context Transfer](https://neurips.cc/virtual/2026/poster/150023) | Qwen2.5-VL-7B | FedRepRAG (β = 0.5) | accuracy | 60.70 | Local IC-RAG | 54.19 |
| SlideBench-BCNB | [PathNavigate](https://neurips.cc/virtual/2026/poster/154224) | Patho-R1-7B + Qwen3.5-4B | PathNavigate (ours) | Overall accuracy | 59.42 | PathAgent | 55.72 |
| VQA-RAD | [CRAFT](https://neurips.cc/virtual/2026/poster/149960) | Hulu-Med 4B | CRAFT arbitration head excision, Prefix textual conflict | CFR (lower is better) | 15.38 | Baseline | 33.33 |
| VQA-RAD | [OpenMedReason](https://neurips.cc/virtual/2026/poster/139693) | Qwen2.5-VL-7B | SFT + GRPO on OpenMedReason | accuracy (%) | 72.51 | Qwen2.5-VL-7B (Base) | 67.13 |
| VQA-RAD | [Teach-to-Reason](https://neurips.cc/virtual/2026/poster/150121) | Qwen3-VL-Instruct 4B | T2R-R2 | accuracy | 46.96 | Base Model | 40.37 |
| VQA-RAD | [Teach-to-Reason](https://neurips.cc/virtual/2026/poster/150121) | Qwen3-VL-Instruct 2B | T2R-R3 | accuracy | 43.18 | Base Model | 31.69 |
| VQA-RAD | [Uncertainty Quantification for Multimodal Large Language Models with Incoherence-adjusted Semantic Volume](https://neurips.cc/virtual/2026/poster/152113) | Llava-v1.5-13b | UMPIRE uncertainty metric | AUROC | 80.7 | Eigen | 79.5 |
| VQA-RAD | [Uncertainty Quantification for Multimodal Large Language Models with Incoherence-adjusted Semantic Volume](https://neurips.cc/virtual/2026/poster/152113) | Llava-v1.5-13b | UMPIRE uncertainty metric | AURAC | 60.2 | Eigen | 58.6 |
| WSI-VQA | [PathNavigate](https://neurips.cc/virtual/2026/poster/154224) | Patho-R1-7B + Qwen3.5-4B | PathNavigate (ours) | Total accuracy | 56.34 | PathAgent | 33.88 |
| WSI-VQA | [PathNavigate](https://neurips.cc/virtual/2026/poster/154224) | Patho-R1-7B + Qwen3.5-4B | PathNavigate (ours) | Open accuracy | 61.00 | MedDr | 46.86 |

<details><summary>본문에 벤치마크 이름은 나오지만 실험에는 쓰지 않은 논문 28편</summary>

| 논문 | 자체 벤치마크 | 비고 |
|---|---|---|
| [\chi-Bench: Can AI Agents Automate End-to-End, Long-Horizon, Policy-Rich Healthcare Workflows?](https://neurips.cc/virtual/2026/poster/139361) | χ-Bench | 20개 의료 앱 시뮬레이터와 87개 MCP 도구로 장기 의료 워크플로 χ-Bench를 만들어 에이전트를 평가한다. |
| [Aligning Language Model Benchmarks with Pairwise Preferences](https://neurips.cc/virtual/2026/poster/139753) |  | 다운스트림 쌍대 선호에 맞춰 벤치마크 문항 가중치를 학습하는 벤치마크 정렬을 제안 |
| [Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs](https://neurips.cc/virtual/2026/poster/138960) |  | HealthBench 점수를 모델 보고서에서 모아 분석할 뿐 모델을 직접 돌리지 않음 |
| [Can AI Agents Synthesize Scientific Conclusions?](https://neurips.cc/virtual/2026/poster/139077) | SciConBench | 체계적 문헌고찰 기반 9.11K 문항 SciConBench와 누출 차단 평가 환경으로 에이전트를 평가한다. |
| [CardioLens: Revealing the Clinical Reality Gap of MLLMs via Multi-Sequence Cardiac MRI Evaluations](https://neurips.cc/virtual/2026/poster/139679) | CardioLens | 병원 다중시퀀스 CMR로 영상 이해·보고서 생성·질병 진단 3단계를 평가하는 테스트베드를 제안한다. |
| [DataComp-VLM: Improved open datasets for Vision-Language Models](https://neurips.cc/virtual/2026/poster/138991) |  | 160개 데이터셋·6T 토큰 풀로 DCVLM을 만들고 필터링·혼합 전략별로 VLM을 학습·평가한다. |
| [DDx-TRACE: A Benchmark for Medical Diagnostic Trajectories in VLMs](https://neurips.cc/virtual/2026/poster/139550) | DDx-TRACE | 숨겨진 영상 근거를 요청하며 감별진단을 갱신하는 신경영상 진단 궤적 벤치마크를 제안한다. |
| [ER-Reason: A Benchmark Dataset for LLM Clinical Reasoning in the Emergency Room](https://neurips.cc/virtual/2026/poster/138971) | ER-Reason | 응급실 실제 기록 25,174건과 SCT형 문항으로 ER-Reason을 만들어 LLM의 진단 신념 갱신을 평가한다. |
| [HelpBench: Assessing the Ability of LLMs to Provide Privacy, Safety, and Security Advice](https://neurips.cc/virtual/2026/poster/138892) |  | 실제 상황 450개 질문과 문항별 루브릭으로 HelpBench를 만들어 18개 LLM을 자동 채점기로 평가한다. |
| [Hi-Q: Hierarchical Evidence-guided Query Refinement for Multi-Hop Question Answering](https://neurips.cc/virtual/2026/poster/155067) |  | 증거 지지 여부에 따라 질의 노드를 해결하거나 이분 분해하며 질의 트리를 키우는 Hi-Q를 제안한다. |
| [Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking](https://neurips.cc/virtual/2026/poster/148222) |  | 총 평가 오차(TEE)로 불확실성을 분해하고 설계 연구로 평가 오차를 줄이는 방법을 제시 |
| [JMed48k: A Multi-Profession Japanese Medical Licensing Benchmark for Vision-Language Model Evaluation](https://neurips.cc/virtual/2026/poster/139030) | JMed48k | 일본 11개 의료 국가시험 48,862문항으로 JMed48k를 만들고 이미지 제거 감사로 21개 VLM을 평가한다. |
| [JudgmentBench: Comparing Rubric and Preference Evaluation for Quality Assessment](https://neurips.cc/virtual/2026/poster/139683) |  | 변호사 주석의 법률 벤치마크 JudgmentBench로 루브릭과 비교 판단의 품질 복원력을 비교 |
| [L2-Bench: An Evaluation Benchmark for Measuring LLM Capabilities in Second Language Education](https://neurips.cc/virtual/2026/poster/139497) |  | 전문가 검증 역량 분류체계와 루브릭 기반 L2-Bench로 LLM의 L2 교육 수행 능력을 측정 |
| [LLMs can construct powerful representations and streamline sample-efficient supervised learning](https://neurips.cc/virtual/2026/poster/153045) |  | LLM이 소수 예시로 전역 루브릭을 합성해 EHR 입력을 표준화된 표현으로 바꾸고 하류 모델을 학습한다. |
| [MedEvoEval: Evaluating Continual Evolution of Doctor Agents through Simulated Clinical Episodes](https://neurips.cc/virtual/2026/poster/139548) | MedEvoEval (MedEvoEval-MedQA-700) | 행동으로만 정보가 열리는 시뮬레이션 외래 에피소드로 에이전트의 과정·기억·전이·유지를 평가한다. |
| [MedFlowBench: Auditing Medical Agents in Full-Study Workflows](https://neurips.cc/virtual/2026/poster/139506) | MedFlowBench | 영상 뷰어를 조작해 전체 검사를 판독하고 검증 가능한 근거를 제출하는 에이전트 벤치마크를 제안한다. |
| [MedVIGIL: Evaluating Trustworthy Medical VLMs Under Broken Visual Evidence](https://neurips.cc/virtual/2026/poster/139346) | MedVIGIL | 방사선과 전문의가 만든 300사례 교란 프로브 MedVIGIL로 16개 VLM의 무성 실패를 감사한다. |
| [MentalHospital: A Virtual Environment for Evaluating Psychiatric Clinical Encounters](https://neurips.cc/virtual/2026/poster/149637) | MentalHospital | EHR 기반 표준화 환자로 S.O.A.P. 진료를 재현하고 전용 평가자 MentalEval로 LLM을 평가한다. |
| [MMFineReason: Closing the Multimodal Reasoning Gap via Open Data-Centric Methods](https://neurips.cc/virtual/2026/poster/139294) |  | Qwen3-VL로 증류한 180만 개 CoT 추론 데이터셋 MMFineReason을 구축해 Qwen3-VL을 SFT |
| [PathView-Bench: Can Multimodal Large Language Models Achieve Fine-grained Multiscale Understanding of Pathology Images?](https://neurips.cc/virtual/2026/poster/139172) | PathView-Bench | 23개 병리 영상 데이터셋으로 14개 VQA형 과제의 PathView-Bench를 만들어 18개 MLLM을 평가한다. |
| [PhysicianBench: Evaluating LLM Agents in Real-World EHR Environments](https://neurips.cc/virtual/2026/poster/139788) | PhysicianBench | 실제 EHR 환경과 FHIR API에서 100개 장기 의사 과제를 실행 검증으로 평가하는 벤치마크를 제안한다. |
| [RealICU: Do LLM Agents Understand Long-Context ICU Data? A Benchmark Beyond Behavior Imitation](https://neurips.cc/virtual/2026/poster/138984) | RealICU | 전체 경과를 본 사후 판단으로 라벨링한 RealICU와 구조화 메모리 에이전트 ICU-Evo를 제안한다. |
| [Soft Token Alignment for Cross-Lingual Reasoning](https://neurips.cc/virtual/2026/poster/149550) |  | 영어를 축으로 soft-token 표현을 언어 간 정렬하는 SFT 보조 목적함수 SOLAR 제안 |
| [Teaching LLMs to Recommend and Defer in Underrepresented Epilepsy Care](https://neurips.cc/virtual/2026/poster/154539) |  | 처방 오류를 프롬프트 메모리로 학습하는 Manana와 베이지안 프롬프트 평균으로 처방 예측·보류 신호를 낸다. |
| [Tracing the Cascade: A Topology-Aware Evaluation Framework for Scientific Agent Hallucinations](https://neurips.cc/virtual/2026/poster/139645) | SCHEMA (Protein Domain, PathVQA-Enhanced) | 개념 그래프 기반 위상 가중 환각 지표와 반사실 귀인으로 과학 에이전트 궤적을 평가 |
| [TSNBench: Benchmarking LLM Proficiency in Time-Sensitive Networking](https://neurips.cc/virtual/2026/poster/138953) |  | TSN 객관식 939문항과 최악지연 계산 100과제로 TSNBench를 만들어 16개 LLM을 평가한다. |
| [VIPER: An Expert-Curated Benchmark for Vision-Language Models in Veterinary Pathology](https://neurips.cc/virtual/2026/poster/139742) | VIPER | 수의병리 전문의가 검증한 랫드 H&E 이미지 기반 질문 1,251개로 16개 VLM을 평가한다. |

</details>

초록에는 벤치마크 이름이 나오지만 arXiv 판을 찾지 못해 본문을 확인하지 못한 논문 4편: [Learning When to Collaborate](https://neurips.cc/virtual/2026/poster/148185) (PMC-VQA, PathVQA, VQA-RAD), [MedPsy](https://neurips.cc/virtual/2026/poster/150557) (HealthBench), [Mining Logic under Uncertainty](https://neurips.cc/virtual/2026/poster/152179) (BioASQ), [Specialist Mediators](https://neurips.cc/virtual/2026/poster/148508) (PubMedQA)

## 논문 목록

### Medical QA (25편)

의료·임상·생의학 질의응답, medical VQA, 시험형 QA, 임상 추론 QA. 다른 분류와 겹치는 논문은 양쪽에 모두 나온다.

| # | 제목 | 한 줄 요약 | 분류 | 발표 |
|---:|---|---|---|---|
| 1 | [BrainTRACE: Tracing Longitudinal, Multimodal, and Volumetric Evidence in Brain MRI Clinical Reasoning](https://neurips.cc/virtual/2026/poster/139162) | 종단·다중시퀀스 뇌 MRI 임상추론 VQA 벤치마크 BrainTRACE | Medical QA, Medical LLM / VLM | Poster |
| 2 | [Can AI Agents Synthesize Scientific Conclusions?](https://neurips.cc/virtual/2026/poster/139077) | 체계적 문헌고찰 기반 과학적 결론 합성 에이전트 벤치마크 | Medical QA, RAG |  |
| 3 | [CardioLens: Revealing the Clinical Reality Gap of MLLMs via Multi-Sequence Cardiac MRI Evaluations](https://neurips.cc/virtual/2026/poster/139679) | 다중시퀀스 심장 MRI로 MLLM의 임상 격차를 평가하는 CardioLens | Medical QA, Medical LLM / VLM | Poster |
| 4 | [CasePlay: Self-Play Reinforcement Learning from Case Reports for Medical Reasoning](https://neurips.cc/virtual/2026/poster/153097) | 임상 증례 보고서 기반 자기대결 RL로 의료 추론 향상 CasePlay | Medical QA, Medical LLM / VLM | Poster |
| 5 | [DDx-TRACE: A Benchmark for Medical Diagnostic Trajectories in VLMs](https://neurips.cc/virtual/2026/poster/139550) | VLM의 신경영상 진단 궤적을 평가하는 벤치마크(DDx-TRACE) | Medical LLM / VLM, Medical QA | Poster |
| 6 | [Diagnosing and Repairing Visual Collapse in Compact Medical Multimodal LLMs](https://neurips.cc/virtual/2026/poster/149438) | 소형 의료 MLLM의 시각 붕괴 진단 및 복구(medical VQA) | Medical LLM / VLM, Medical QA | Poster |
| 7 | [EHRNote-ChatQA: A Benchmark for Evidence-Grounded Multi-Turn Clinical Question Answering over Longitudinal Discharge Summaries](https://neurips.cc/virtual/2026/poster/139551) | 퇴원 요약지 기반 근거 접지 다회전 임상 QA 벤치마크(EHRNote-ChatQA) | Medical QA |  |
| 8 | [ER-Reason: A Benchmark Dataset for LLM Clinical Reasoning in the Emergency Room](https://neurips.cc/virtual/2026/poster/138971) | 응급실 실제 기록 기반 LLM 임상 추론 벤치마크(ER-Reason) | Medical LLM / VLM, Medical QA | Poster |
| 9 | [JMed48k: A Multi-Profession Japanese Medical Licensing Benchmark for Vision-Language Model Evaluation](https://neurips.cc/virtual/2026/poster/139030) | 일본 의료면허 시험 기반 VLM 평가 벤치마크 JMed48k | Medical QA, Medical LLM / VLM | Poster |
| 10 | [Less Evidence, Better Answering: Gain-Aware Minimal Evidence Subset Selection for Medical QA](https://neurips.cc/virtual/2026/poster/152857) | 의료 QA를 위한 이득 인지 최소 증거 부분집합 선택 | Medical QA, Medical RAG, RAG | Poster |
| 11 | [LG-Bench: A Graph-Structured Evaluation Benchmark for Life Science](https://neurips.cc/virtual/2026/poster/139764) | 의학·생물·화학 객관식의 그래프 구조 생명과학 벤치마크 LG-Bench | Medical QA | Poster |
| 12 | [MammoGPS: A Benchmark for Visual Grounding, Perception, and Spatial Reasoning in Mammography](https://neurips.cc/virtual/2026/poster/138998) | 유방촬영 VLM 시각 근거·공간 추론 벤치마크 MammoGPS | Medical QA, Medical LLM / VLM | Poster |
| 13 | [Medmarks: A Comprehensive Open-Source LLM Benchmark Suite for Medical Tasks](https://neurips.cc/virtual/2026/poster/139434) | 30개 벤치마크로 구성된 오픈소스 의료 LLM 평가 스위트 | Medical LLM / VLM, Medical QA |  |
| 14 | [MedMisBench: Measuring Epistemic Resilience of LLMs Under Misleading Medical Context](https://neurips.cc/virtual/2026/poster/139561) | 오도하는 의료 맥락 하에서 LLM의 정답 유지 능력 측정 | Medical QA, Medical LLM / VLM | Poster |
| 15 | [MedVIGIL: Evaluating Trustworthy Medical VLMs Under Broken Visual Evidence](https://neurips.cc/virtual/2026/poster/139346) | 시각 증거가 깨진 상황에서 의료 VLM의 신뢰성 평가 | Medical QA, Medical LLM / VLM | Poster |
| 16 | [MedZERO: Self-Evolving Agents for Open-Ended Medical Reasoning Through Controlled Knowledge Accumulation](https://neurips.cc/virtual/2026/poster/155563) | 통제된 지식 축적으로 개방형 의료 추론을 자기진화하는 에이전트 | Medical LLM / VLM, Medical QA |  |
| 17 | [MutQA: A Cross-Validated Q&A Dataset for Genetic Mutations](https://neurips.cc/virtual/2026/poster/139212) | 유전자 변이 기능에 대한 PubMed 근거 기반 QA 데이터셋 MutQA | Medical QA | Poster |
| 18 | [NPCBench: A Clinical Apprenticeship Benchmark for Guideline-Constrained Care-Pathway Reasoning in Nasopharyngeal Carcinoma](https://neurips.cc/virtual/2026/poster/139689) | 비인두암 가이드라인 기반 진료경로 추론 벤치마크 | Medical LLM / VLM, Medical QA | Poster |
| 19 | [OpenMedReason: Scientific Reasoning Supervision for Medical Vision–Language Models](https://neurips.cc/virtual/2026/poster/139693) | 의료 VLM용 45만 건 과학적 추론 감독 코퍼스 OpenMedReason | Medical LLM / VLM, Medical QA | Poster |
| 20 | [PathNavigate: A Training-Free Pathology Agent with Surprise-Guided Scan and Shared Slide Memory for Whole-Slide VQA](https://neurips.cc/virtual/2026/poster/154224) | 병리 전체 슬라이드 VQA를 위한 무학습 탐색형 에이전트 | Medical Agent, Medical QA | Poster |
| 21 | [SafeDrug: A Benchmark Dataset for Safety-Critical Pharmacological Reasoning in LLMs](https://neurips.cc/virtual/2026/poster/139719) | 약리학 안전 추론을 평가하는 LLM 벤치마크 SafeDrug | Medical QA, Medical LLM / VLM |  |
| 22 | [Selective Answering for Medical VQA via Parallel Independent Claim Verification](https://neurips.cc/virtual/2026/poster/150272) | 병렬 독립 claim 검증으로 의료 VQA의 선택적 응답(abstain) 수행 | Medical QA, Medical LLM / VLM |  |
| 23 | [SynTeX-FL: Cross-Modal Text Transfer in Federated Learning for Medical Visual Question Answering](https://neurips.cc/virtual/2026/poster/152446) | 모달리티별 텍스트만 가진 기관 간 연합학습 의료 VQA 프레임워크 SynTeX-FL | Medical QA | Poster |
| 24 | [Teach-to-Reason: Competition-Guided Reasoning with a Self-Improving Teacher](https://neurips.cc/virtual/2026/poster/150121) | CXR VQA 추론 품질을 높이는 교사-추론자 경쟁 학습 Teach-to-Reason | Medical QA, Medical LLM / VLM | Poster |
| 25 | [VIPER: An Expert-Curated Benchmark for Vision-Language Models in Veterinary Pathology](https://neurips.cc/virtual/2026/poster/139742) | 수의 독성병리 VLM 평가용 전문가 큐레이션 벤치마크 VIPER | Medical QA, Medical LLM / VLM | Poster |

### Medical RAG (5편)

의료 도메인의 검색증강 생성·지식 검색. 다른 분류와 겹치는 논문은 양쪽에 모두 나온다.

| # | 제목 | 한 줄 요약 | 분류 | 발표 |
|---:|---|---|---|---|
| 1 | [Cite What You Explore: Budget-Aware LLM Reasoning over Medical KGs with Verifiable Evidence](https://neurips.cc/virtual/2026/poster/153952) | 의료 KG 위에서 예산 제약 하에 근거 인용 가능한 LLM 퇴원 후 위험 예측 | Medical RAG, RAG |  |
| 2 | [Deceptive Grounding: Entity Attribution Failure in Clinical Retrieval-Augmented Generation](https://neurips.cc/virtual/2026/poster/152927) | 임상 RAG에서 증거를 잘못된 개체에 귀속하는 기만적 접지 실패 분석 | Medical RAG, RAG | Poster |
| 3 | [Incentivizing Agentic Retrieval for Disease-Centric Clinical Case Search via Trajectory Memory](https://neurips.cc/virtual/2026/poster/149120) | 궤적 메모리 기반 에이전틱 임상 사례 검색 | Medical RAG, RAG | Poster |
| 4 | [Less Evidence, Better Answering: Gain-Aware Minimal Evidence Subset Selection for Medical QA](https://neurips.cc/virtual/2026/poster/152857) | 의료 QA를 위한 이득 인지 최소 증거 부분집합 선택 | Medical QA, Medical RAG, RAG | Poster |
| 5 | [MicroWorld: Empowering Multimodal Large Language Models to Bridge the Microscopic Domain Gap with Multimodal Attribute Graph](https://neurips.cc/virtual/2026/poster/151480) | 현미경 도메인용 멀티모달 속성 그래프 검색으로 MLLM 추론 강화 | RAG, Medical RAG | Poster |

### Medical Agent (26편)

의료 환경의 LLM/VLM 에이전트, 멀티에이전트 진단, 임상 워크플로 벤치마크. 다른 분류와 겹치는 논문은 양쪽에 모두 나온다.

| # | 제목 | 한 줄 요약 | 분류 | 발표 |
|---:|---|---|---|---|
| 1 | [A Stratified Multi-Rater Evaluation of LLM-Based Virtual Standardized Patients with a Deployed Data-Generation Platform](https://neurips.cc/virtual/2026/poster/139188) | LLM 기반 가상 표준화 환자(OSCE)의 다중 평가자 평가와 플랫폼 | Medical Agent | Poster |
| 2 | [BioXArena: Benchmarking LLM Agents on Multi-Modal Biomedical Machine Learning Tasks](https://neurips.cc/virtual/2026/poster/138952) | 다중모달 생의학 데이터에서 모델 구축 코드를 작성·학습하는 LLM 에이전트 BioML 벤치마크 (76 tasks) | Medical Agent | Poster |
| 3 | [Calibrating Agentic LLMs for Clinical Prediction](https://neurips.cc/virtual/2026/poster/149149) | 임상 예측용 에이전트 LLM의 보정(calibration) 개선 프레임워크 | Medical Agent, Medical LLM / VLM |  |
| 4 | [ClinMAS: A Knowledge-Grounded Multi-Agent Simulation Framework for Evaluating Clinical Reasoning in LLMs](https://neurips.cc/virtual/2026/poster/139102) | 지식 기반 멀티에이전트 시뮬레이션으로 LLM 임상 추론 평가(ClinMAS) | Medical Agent, Medical LLM / VLM | Poster |
| 5 | [CoE-Agent: Co-Evolving Patient-Doctor Agents via Interactive Policy Graph Optimization for Clinical Decision Making](https://neurips.cc/virtual/2026/poster/155085) | 환자-의사 에이전트 공진화로 임상 의사결정 학습(CoE-Agent) | Medical Agent | Poster |
| 6 | [CoMMa: Contribution-Aware Medical Multi-Agents for Decentralized Oncology Decision Support](https://neurips.cc/virtual/2026/poster/153350) | 분산 데이터 환경의 기여도 인지 종양학 의사결정 멀티에이전트(CoMMa) | Medical Agent, Medical LLM / VLM |  |
| 7 | [Experience Makes Skillful: Enabling Generalizable Medical Agent Reasoning via Self-Evolving Skill Memory](https://neurips.cc/virtual/2026/poster/150444) | 자기진화 스킬 메모리로 의료 에이전트 추론 일반화 | Medical Agent | Poster |
| 8 | [Learning When to Collaborate: Selective Multi-Agent Medical Reasoning via Uncertainty-Aware Routing](https://neurips.cc/virtual/2026/poster/148185) | 불확실성 라우팅 기반 선택적 멀티에이전트 의료 추론 SMART-Med | Medical Agent, Medical LLM / VLM | Poster |
| 9 | [M4Bench: Evaluating Procedural Specification for Clinical EHR Derivation Agents](https://neurips.cc/virtual/2026/poster/139625) | 임상 EHR 변수 도출 에이전트 평가 벤치마크 M4Bench | Medical Agent |  |
| 10 | [MedEvoEval: Evaluating Continual Evolution of Doctor Agents through Simulated Clinical Episodes](https://neurips.cc/virtual/2026/poster/139548) | 시뮬레이션 임상 에피소드로 의사 에이전트의 지속적 진화를 평가 | Medical Agent | Poster |
| 11 | [MedExAgent: Training LLM Agents to Ask, Examine, and Diagnose in Noisy Clinical Environments](https://neurips.cc/virtual/2026/poster/149616) | 잡음 있는 임상 환경에서 문진·검사·진단을 수행하는 LLM 에이전트 학습 | Medical Agent | Poster |
| 12 | [MedFlowBench: Auditing Medical Agents in Full-Study Workflows](https://neurips.cc/virtual/2026/poster/139506) | 전체 영상 스터디 워크플로우에서 의료 에이전트를 감사하는 벤치마크 | Medical Agent | Poster |
| 13 | [MedMemoryBench: Benchmarking Agent Memory in Personalized Healthcare](https://neurips.cc/virtual/2026/poster/139145) | 개인화 헬스케어 에이전트의 메모리를 평가하는 벤치마크 | Medical Agent | Poster |
| 14 | [MentalHospital: A Virtual Environment for Evaluating Psychiatric Clinical Encounters](https://neurips.cc/virtual/2026/poster/149637) | 정신과 임상 진료 전 과정을 시뮬레이션하는 LLM 평가 환경 | Medical Agent | Poster |
| 15 | [PathNavigate: A Training-Free Pathology Agent with Surprise-Guided Scan and Shared Slide Memory for Whole-Slide VQA](https://neurips.cc/virtual/2026/poster/154224) | 병리 전체 슬라이드 VQA를 위한 무학습 탐색형 에이전트 | Medical Agent, Medical QA | Poster |
| 16 | [PhysicianBench: Evaluating LLM Agents in Real-World EHR Environments](https://neurips.cc/virtual/2026/poster/139788) | EHR 환경에서 의사 업무를 수행하는 LLM 에이전트 벤치마크 | Medical Agent | Poster |
| 17 | [ProbMedTOD: A Bayesian Network Guided Task-Oriented Dialogue System for Patient History Taking](https://neurips.cc/virtual/2026/poster/154360) | 베이지안 네트워크 기반 환자 문진 과업지향 대화 시스템 | Medical Agent | Poster |
| 18 | [ProCARE: Real-World Study Automation via Profile-Grounded Evidence Contracts](https://neurips.cc/virtual/2026/poster/149562) | 의료 실세계 연구 분석을 자동화하는 LLM 에이전트 프레임워크 | Medical Agent | Poster |
| 19 | [Rare Disease Diagnosis Agent with Decoupled Workflows and Knowledge-Driven Self-Evaluation](https://neurips.cc/virtual/2026/poster/152822) | 소형 LLM용 희귀질환 진단 에이전트: 워크플로 분리와 지식 기반 자기평가 | Medical Agent | Poster |
| 20 | [REAL-MED: Benchmarking LLM Agents on Real-World Medical Tasks](https://neurips.cc/virtual/2026/poster/139773) | 실제 의료 업무 워크플로에서 LLM 에이전트를 평가하는 REAL-MED 벤치마크 | Medical Agent | Poster |
| 21 | [RealICU: Do LLM Agents Understand Long-Context ICU Data? A Benchmark Beyond Behavior Imitation](https://neurips.cc/virtual/2026/poster/138984) | ICU 장기 맥락 데이터에서 LLM 에이전트를 평가하는 사후 주석 벤치마크 RealICU | Medical Agent, Medical LLM / VLM | Poster |
| 22 | [Risk-Calibrated Context Selection for Healthcare Multi-Agent Handoff](https://neurips.cc/virtual/2026/poster/154212) | 의료 멀티에이전트 handoff에서 위험 보정된 최소 필요 컨텍스트 선택 ScopeSelect | Medical Agent | Poster |
| 23 | [SAGE: Evidence-First Biomarker Discovery through Multi-Agent Reasoning](https://neurips.cc/virtual/2026/poster/155210) | 병리 영상 바이오마커 발굴을 위한 근거 기반 멀티에이전트 시스템 SAGE | Medical Agent | Poster |
| 24 | [TraceDx: Criticality-Weighted Atomic Facts as a Training Signal for Sequential Clinical Diagnosis](https://neurips.cc/virtual/2026/poster/149401) | 순차적 임상 진단을 위한 핵심도 가중 원자 사실 학습 신호 TraceDx | Medical Agent, Medical LLM / VLM |  |
| 25 | [TrialAgentBench: Evaluating AI Agents for Clinical-Trial Analysis and Long-Horizon Drug-Development Decisions](https://neurips.cc/virtual/2026/poster/139604) | 임상시험 분석과 신약개발 의사결정 에이전트 벤치마크 TrialAgentBench | Medical Agent | Poster |
| 26 | [χ-Bench: Can AI Agents Automate End-to-End, Long-Horizon, Policy-Rich Healthcare Workflows?](https://neurips.cc/virtual/2026/poster/139361) | 정책 밀도 높은 헬스케어 워크플로우 자동화 에이전트 벤치마크 χ-Bench | Medical Agent | Poster |

### Medical LLM / VLM (70편)

의료용 언어·비전-언어 모델의 학습·정렬·안전·평가·리포트 생성. 다른 분류와 겹치는 논문은 양쪽에 모두 나온다.

| # | 제목 | 한 줄 요약 | 분류 | 발표 |
|---:|---|---|---|---|
| 1 | [A Multimodal Benchmark for Evaluating Cause-of-Death Inference Using Child Health and Mortality Data](https://neurips.cc/virtual/2026/poster/139715) | 아동 사망원인 추론을 위한 멀티모달 벤치마크와 LLM 임상추론 평가 | Medical LLM / VLM | Poster |
| 2 | [Aligning LLMs with Biomedical Knowledge using Balanced Fine-Tuning](https://neurips.cc/virtual/2026/poster/149582) | 생의학 지식 정렬을 위한 Balanced Fine-Tuning으로 LLM 후학습 | Medical LLM / VLM | Poster |
| 3 | [Alignment Is Not Enough for Safe Medical LLM Evaluation](https://neurips.cc/virtual/2026/poster/140065) | 의료 LLM-as-judge 평가의 정렬만으로는 부족함을 주장하는 입장 논문 | Medical LLM / VLM | Accept |
| 4 | [Anchoring LLM-based Chest X-ray Report Generation via Diffusion Language Planning](https://neurips.cc/virtual/2026/poster/148935) | 확산 언어모델 플래너로 흉부 X선 보고서 생성의 임상 충실도 향상 | Medical LLM / VLM | Poster |
| 5 | [ASSET: Acquisition-Sensitive Subspace Estimation for Test-Time Adaptation of Medical VLMs](https://neurips.cc/virtual/2026/poster/153026) | 촬영 조건 변화에 대한 의료 VLM의 테스트타임 적응 ASSET | Medical LLM / VLM | Poster |
| 6 | [BrainTRACE: Tracing Longitudinal, Multimodal, and Volumetric Evidence in Brain MRI Clinical Reasoning](https://neurips.cc/virtual/2026/poster/139162) | 종단·다중시퀀스 뇌 MRI 임상추론 VQA 벤치마크 BrainTRACE | Medical QA, Medical LLM / VLM | Poster |
| 7 | [Calibrating Agentic LLMs for Clinical Prediction](https://neurips.cc/virtual/2026/poster/149149) | 임상 예측용 에이전트 LLM의 보정(calibration) 개선 프레임워크 | Medical Agent, Medical LLM / VLM |  |
| 8 | [CardioLens: Revealing the Clinical Reality Gap of MLLMs via Multi-Sequence Cardiac MRI Evaluations](https://neurips.cc/virtual/2026/poster/139679) | 다중시퀀스 심장 MRI로 MLLM의 임상 격차를 평가하는 CardioLens | Medical QA, Medical LLM / VLM | Poster |
| 9 | [CasePlay: Self-Play Reinforcement Learning from Case Reports for Medical Reasoning](https://neurips.cc/virtual/2026/poster/153097) | 임상 증례 보고서 기반 자기대결 RL로 의료 추론 향상 CasePlay | Medical QA, Medical LLM / VLM | Poster |
| 10 | [ClinMAS: A Knowledge-Grounded Multi-Agent Simulation Framework for Evaluating Clinical Reasoning in LLMs](https://neurips.cc/virtual/2026/poster/139102) | 지식 기반 멀티에이전트 시뮬레이션으로 LLM 임상 추론 평가(ClinMAS) | Medical Agent, Medical LLM / VLM | Poster |
| 11 | [CLR-voyance : Reinforcing Open-Ended Reasoning for Inpatient Clinical Decision Support with Outcome-Aware Rubrics](https://neurips.cc/virtual/2026/poster/150688) | 결과 인지 루브릭 보상으로 입원 환자 임상 의사결정 추론 강화학습 | Medical LLM / VLM | Poster |
| 12 | [CoMMa: Contribution-Aware Medical Multi-Agents for Decentralized Oncology Decision Support](https://neurips.cc/virtual/2026/poster/153350) | 분산 데이터 환경의 기여도 인지 종양학 의사결정 멀티에이전트(CoMMa) | Medical Agent, Medical LLM / VLM |  |
| 13 | [CRAFT: Causal Responsibility and Failure Tracing in Medical Vision Language Models](https://neurips.cc/virtual/2026/poster/149960) | 의료 VLM의 시각-텍스트 중재 실패를 인과적으로 추적(CRAFT) | Medical LLM / VLM | **Spotlight** |
| 14 | [DDx-TRACE: A Benchmark for Medical Diagnostic Trajectories in VLMs](https://neurips.cc/virtual/2026/poster/139550) | VLM의 신경영상 진단 궤적을 평가하는 벤치마크(DDx-TRACE) | Medical LLM / VLM, Medical QA | Poster |
| 15 | [Diagnosing and Repairing Visual Collapse in Compact Medical Multimodal LLMs](https://neurips.cc/virtual/2026/poster/149438) | 소형 의료 MLLM의 시각 붕괴 진단 및 복구(medical VQA) | Medical LLM / VLM, Medical QA | Poster |
| 16 | [EasyLens: A Training-Free Plug-and-Play Subtle-Lesion Representation Amplifier for Medical Vision-Language Models](https://neurips.cc/virtual/2026/poster/151511) | 의료 VLM의 미세 병변 표현을 증폭하는 학습 불필요 플러그인(EasyLens) | Medical LLM / VLM |  |
| 17 | [ECG-Reasoning-Benchmark: A Benchmark for Evaluating Clinical Reasoning Capabilities in ECG Interpretation](https://neurips.cc/virtual/2026/poster/139595) | MLLM의 ECG 해석 단계별 임상 추론 능력 벤치마크 | Medical LLM / VLM |  |
| 18 | [EmoTrack: Robust Depression Tracking from Counseling Transcripts across Session Regimes](https://neurips.cc/virtual/2026/poster/152590) | 상담 전사로부터 LLM 기반 우울증(PHQ-8) 강건 추적(EmoTrack) | Medical LLM / VLM | Poster |
| 19 | [EndoSCOP-V: A Multi-Turn Video Understanding Evaluation Framework for Multimodal Models in Endoscopy Reporting and Clinical Reasoning](https://neurips.cc/virtual/2026/poster/138889) | 내시경 영상 보고 및 임상 추론용 다회전 MLLM 평가 프레임워크 | Medical LLM / VLM | Poster |
| 20 | [ER-Reason: A Benchmark Dataset for LLM Clinical Reasoning in the Emergency Room](https://neurips.cc/virtual/2026/poster/138971) | 응급실 실제 기록 기반 LLM 임상 추론 벤치마크(ER-Reason) | Medical LLM / VLM, Medical QA | Poster |
| 21 | [FOCUS: Benchmarking Retinal Model Generalization from Foundation Vision Encoders to Multimodal LLMs](https://neurips.cc/virtual/2026/poster/139808) | 망막 영상 파운데이션 인코더부터 MLLM까지 일반화 벤치마크(FOCUS) | Medical LLM / VLM | Poster |
| 22 | [Glance Before You Tell: Anomaly-Guided 3D Radiology Report Generation with Heat-Conduction Slice Encoders](https://neurips.cc/virtual/2026/poster/149584) | 이상 탐지 기반 3D 방사선 리포트 생성 HeatRAD | Medical LLM / VLM | Poster |
| 23 | [GLINT: Sparsely Gated Vision-Language Alignment for Fine-Grained Radiology Representations](https://neurips.cc/virtual/2026/poster/154081) | GLINT: 희소 게이트 정렬 기반 흉부 X-ray/CT 영상-언어 모델 | Medical LLM / VLM | Poster |
| 24 | [How to Train a Surgeon? Benchmarking Generalist Agents in Surgical Scene Understanding](https://neurips.cc/virtual/2026/poster/139078) | 수술 장면 이해를 위한 범용 MLLM 벤치마크 | Medical LLM / VLM | Poster |
| 25 | [Incentivizing Medical Vision Capabilities from Large-Scale Multimodal Pre-training](https://neurips.cc/virtual/2026/poster/156128) | 대규모 멀티모달 사전학습+RL의 의료 VLM HuatuoGPT-5 | Medical LLM / VLM | **Oral** |
| 26 | [JMed48k: A Multi-Profession Japanese Medical Licensing Benchmark for Vision-Language Model Evaluation](https://neurips.cc/virtual/2026/poster/139030) | 일본 의료면허 시험 기반 VLM 평가 벤치마크 JMed48k | Medical QA, Medical LLM / VLM | Poster |
| 27 | [Learning When to Collaborate: Selective Multi-Agent Medical Reasoning via Uncertainty-Aware Routing](https://neurips.cc/virtual/2026/poster/148185) | 불확실성 라우팅 기반 선택적 멀티에이전트 의료 추론 SMART-Med | Medical Agent, Medical LLM / VLM | Poster |
| 28 | [LLMs can construct powerful representations and streamline sample-efficient supervised learning](https://neurips.cc/virtual/2026/poster/153045) | LLM이 합성한 rubric으로 EHR 임상 과제 표현 학습 | Medical LLM / VLM | Poster |
| 29 | [Look Before You Leap: Self-Evolving Clinical Reasoning with Psychometric Preference Optimization for Radiology Report Generation](https://neurips.cc/virtual/2026/poster/154029) | 심리측정 선호 최적화로 자기진화 임상 추론 방사선 리포트 생성 | Medical LLM / VLM |  |
| 30 | [MammoGPS: A Benchmark for Visual Grounding, Perception, and Spatial Reasoning in Mammography](https://neurips.cc/virtual/2026/poster/138998) | 유방촬영 VLM 시각 근거·공간 추론 벤치마크 MammoGPS | Medical QA, Medical LLM / VLM | Poster |
| 31 | [Med-Agentic: Distilling Agentic Medical Reasoning with Internalized Meta-Capabilities](https://neurips.cc/virtual/2026/poster/153012) | 에이전트형 의료 추론을 내재화된 메타 역량으로 증류하는 방법 | Medical LLM / VLM | Poster |
| 32 | [MedHorizon: Towards Long-context Medical Video Understanding in the Wild](https://neurips.cc/virtual/2026/poster/139391) | 장시간 의료 영상(비디오) 이해를 위한 MLLM 벤치마크 | Medical LLM / VLM | Poster |
| 33 | [Medical LLMs as Medical World Models: Unified Policy-Dynamics Learning with Test-Time Search](https://neurips.cc/virtual/2026/poster/148462) | 의료 LLM을 정책-동역학 통합 학습과 테스트 시 탐색의 월드모델로 활용 | Medical LLM / VLM | Poster |
| 34 | [MedKIT: Evaluating Knowledge Integration and Generalization in Large Language Models](https://neurips.cc/virtual/2026/poster/138975) | 의료 지식 통합 및 전이 능력을 평가하는 벤치마크 MedKIT | Medical LLM / VLM | Poster |
| 35 | [Medmarks: A Comprehensive Open-Source LLM Benchmark Suite for Medical Tasks](https://neurips.cc/virtual/2026/poster/139434) | 30개 벤치마크로 구성된 오픈소스 의료 LLM 평가 스위트 | Medical LLM / VLM, Medical QA |  |
| 36 | [MedMisBench: Measuring Epistemic Resilience of LLMs Under Misleading Medical Context](https://neurips.cc/virtual/2026/poster/139561) | 오도하는 의료 맥락 하에서 LLM의 정답 유지 능력 측정 | Medical QA, Medical LLM / VLM | Poster |
| 37 | [MedPsy: State‑of‑the‑Art Small Medical Language Models for Efficient Edge Deployment](https://neurips.cc/virtual/2026/poster/150557) | 엣지 배포용 1.7B/4B 소형 의료 언어모델 MedPsy | Medical LLM / VLM | Poster |
| 38 | [MedVIGIL: Evaluating Trustworthy Medical VLMs Under Broken Visual Evidence](https://neurips.cc/virtual/2026/poster/139346) | 시각 증거가 깨진 상황에서 의료 VLM의 신뢰성 평가 | Medical QA, Medical LLM / VLM | Poster |
| 39 | [MedVIGOR: Visual Evidence Internalization for Observation-Driven Reasoning in Medical VLMs](https://neurips.cc/virtual/2026/poster/150235) | 의료 VLM이 시각 증거에 근거해 추론하도록 하는 학습 방법 | Medical LLM / VLM | Poster |
| 40 | [MedZERO: Self-Evolving Agents for Open-Ended Medical Reasoning Through Controlled Knowledge Accumulation](https://neurips.cc/virtual/2026/poster/155563) | 통제된 지식 축적으로 개방형 의료 추론을 자기진화하는 에이전트 | Medical LLM / VLM, Medical QA |  |
| 41 | [MindGuard: Guardrail Classifiers for Multi-Turn Mental Health Support](https://neurips.cc/virtual/2026/poster/138950) | 정신건강 상담 대화를 위한 가드레일 분류기와 위험 분류체계 | Medical LLM / VLM | Poster |
| 42 | [MoBayes: A Modular Bayesian Framework for Separating Reasoning from Language in Conversational Clinical Decision Support](https://neurips.cc/virtual/2026/poster/152953) | 임상 의사결정 지원 대화에서 추론과 언어를 분리하는 베이지안 프레임워크 | Medical LLM / VLM | Poster |
| 43 | [Multimodal LLMs Outperform Pathology Foundation Models in Cross-Domain Histological Similarity](https://neurips.cc/virtual/2026/poster/152201) | 범용 MLLM이 병리 파운데이션 모델보다 조직 유사도 판단에서 우수함을 보임 | Medical LLM / VLM | Poster |
| 44 | [Neural Signals Generate Clinical Notes in the Wild](https://neurips.cc/virtual/2026/poster/155381) | 장시간 EEG에서 임상 리포트를 생성하는 EEG-언어 파운데이션 모델 | Medical LLM / VLM | Poster |
| 45 | [NPCBench: A Clinical Apprenticeship Benchmark for Guideline-Constrained Care-Pathway Reasoning in Nasopharyngeal Carcinoma](https://neurips.cc/virtual/2026/poster/139689) | 비인두암 가이드라인 기반 진료경로 추론 벤치마크 | Medical LLM / VLM, Medical QA | Poster |
| 46 | [On-Policy Hindsight Distillation for Early Risk Prediction](https://neurips.cc/virtual/2026/poster/153484) | LLM 근거를 활용한 EHR 기반 만성질환 조기 위험 예측 증류 | Medical LLM / VLM |  |
| 47 | [OpenMedReason: Scientific Reasoning Supervision for Medical Vision–Language Models](https://neurips.cc/virtual/2026/poster/139693) | 의료 VLM용 45만 건 과학적 추론 감독 코퍼스 OpenMedReason | Medical LLM / VLM, Medical QA | Poster |
| 48 | [PathView-Bench: Can Multimodal Large Language Models Achieve Fine-grained Multiscale Understanding of Pathology Images?](https://neurips.cc/virtual/2026/poster/139172) | 병리 이미지의 다중 스케일 이해를 평가하는 MLLM 벤치마크 | Medical LLM / VLM | Poster |
| 49 | [Positive-Unlabeled Preference Optimization For Chest X-ray Report Generation](https://neurips.cc/virtual/2026/poster/154826) | 흉부 X선 리포트 생성을 위한 PU 선호 최적화 | Medical LLM / VLM | Poster |
| 50 | [RealICU: Do LLM Agents Understand Long-Context ICU Data? A Benchmark Beyond Behavior Imitation](https://neurips.cc/virtual/2026/poster/138984) | ICU 장기 맥락 데이터에서 LLM 에이전트를 평가하는 사후 주석 벤치마크 RealICU | Medical Agent, Medical LLM / VLM | Poster |
| 51 | [Rethinking Visual Attribution for Chest X-ray Reasoning in Large Vision Language Models](https://neurips.cc/virtual/2026/poster/151683) | 흉부 X-ray LVLM 시각 attribution의 인과 평가와 MedFocus 제안 | Medical LLM / VLM | Poster |
| 52 | [SafeDrug: A Benchmark Dataset for Safety-Critical Pharmacological Reasoning in LLMs](https://neurips.cc/virtual/2026/poster/139719) | 약리학 안전 추론을 평가하는 LLM 벤치마크 SafeDrug | Medical QA, Medical LLM / VLM |  |
| 53 | [Selective Answering for Medical VQA via Parallel Independent Claim Verification](https://neurips.cc/virtual/2026/poster/150272) | 병렬 독립 claim 검증으로 의료 VQA의 선택적 응답(abstain) 수행 | Medical QA, Medical LLM / VLM |  |
| 54 | [SliceWorld: A Predictive and Controllable World-State Model for CT Report Generation](https://neurips.cc/virtual/2026/poster/150217) | CT 보고서 생성을 위한 slice 단위 world-state 모델 SliceWorld | Medical LLM / VLM | Poster |
| 55 | [SMI: Semantic Medical ID for Hierarchy-Aware Concept Representation](https://neurips.cc/virtual/2026/poster/154857) | 의료 온톨로지로 계층 인식 임상 개념 임베딩을 만드는 Semantic Medical ID | Medical LLM / VLM | Poster |
| 56 | [SOAR: Semantic Organ-Aware Pretraining for 3D CT Image Understanding](https://neurips.cc/virtual/2026/poster/148421) | 3D CT 영상-언어 이해를 위한 장기 인식 사전학습 SOAR | Medical LLM / VLM | Poster |
| 57 | [TACT-KV: Tri-Axis Cosine Transform for Compressing Volumetric KV Caches in Medical VLMs](https://neurips.cc/virtual/2026/poster/153041) | 3D 의료 VLM의 KV 캐시를 3축 코사인 변환으로 압축하는 TACT-KV | Medical LLM / VLM |  |
| 58 | [TargetSage: Identifying Therapeutic Target Genes with Interpretable and Robust LLM Reasoning](https://neurips.cc/virtual/2026/poster/152330) | 생의학 문헌 기반 LLM 추론으로 치료 표적 유전자를 식별하는 TargetSage | Medical LLM / VLM |  |
| 59 | [Teach-to-Reason: Competition-Guided Reasoning with a Self-Improving Teacher](https://neurips.cc/virtual/2026/poster/150121) | CXR VQA 추론 품질을 높이는 교사-추론자 경쟁 학습 Teach-to-Reason | Medical QA, Medical LLM / VLM | Poster |
| 60 | [Teaching LLMs to Recommend and Defer in Underrepresented Epilepsy Care](https://neurips.cc/virtual/2026/poster/154539) | 우간다 소아 간질 진료에서 추천과 판단 보류를 학습하는 LLM | Medical LLM / VLM | Poster |
| 61 | [TherapyGym: Evaluating and Aligning Clinical Fidelity and Safety in Therapy Chatbots](https://neurips.cc/virtual/2026/poster/139071) | 심리치료 챗봇의 임상 충실도와 안전성 평가 및 정렬 프레임워크 TherapyGym | Medical LLM / VLM | Poster |
| 62 | [Towards Error-Free EHRs: Reasoning-Intensive Consistency Verification Between Clinical Notes and Structured Tables in Electronic Health Records](https://neurips.cc/virtual/2026/poster/139021) | 임상 노트와 EHR 표 간 일관성 검증용 추론 벤치마크 EHR-ReasonCon | Medical LLM / VLM | Poster |
| 63 | [Towards Understanding and Measuring Cognitive Atrophy in LLM Behaviour](https://neurips.cc/virtual/2026/poster/138990) | 정신건강 지원 LLM의 인지 위축 행동을 측정하는 벤치마크 | Medical LLM / VLM | Poster |
| 64 | [TraceDx: Criticality-Weighted Atomic Facts as a Training Signal for Sequential Clinical Diagnosis](https://neurips.cc/virtual/2026/poster/149401) | 순차적 임상 진단을 위한 핵심도 가중 원자 사실 학습 신호 TraceDx | Medical Agent, Medical LLM / VLM |  |
| 65 | [Urgency-Aware Autoregressive VLMs for Unanticipated Healthcare Occurrences](https://neurips.cc/virtual/2026/poster/149641) | 돌발 의료 사건에 대응하는 긴급도 인지 자기회귀 VLM | Medical LLM / VLM | Poster |
| 66 | [ViCoR: Estimating Visual Necessity via Counterfactual Residuals for Multimodal Medical Data Selection](https://neurips.cc/virtual/2026/poster/154516) | 시각적 필요성 기반 멀티모달 의료 VLM 학습 데이터 선별 ViCoR | Medical LLM / VLM | Poster |
| 67 | [VIPER: An Expert-Curated Benchmark for Vision-Language Models in Veterinary Pathology](https://neurips.cc/virtual/2026/poster/139742) | 수의 독성병리 VLM 평가용 전문가 큐레이션 벤치마크 VIPER | Medical QA, Medical LLM / VLM | Poster |
| 68 | [Visual Reinforcement Fine-Tuning via Bootstrapped Medical Reasoning](https://neurips.cc/virtual/2026/poster/150417) | 부트스트랩 의료 추론을 이용한 의료 MLLM 시각 강화 미세조정 | Medical LLM / VLM | Poster |
| 69 | [What Does the AI Doctor Value? Auditing Pluralism in the Clinical Ethics of Language Models](https://neurips.cc/virtual/2026/poster/155923) | LLM의 임상 윤리 가치 다원성을 감사하는 벤치마크와 프레임워크 | Medical LLM / VLM | Poster |
| 70 | [When Medical VLMs Stop Understanding: MedTEC-Bench for Probing Semantic Specificity](https://neurips.cc/virtual/2026/poster/139493) | 의료 VLM의 의미 특이성을 진단하는 MedTEC-Bench | Medical LLM / VLM | Poster |

### RAG (122편)

#### Agentic search / Deep research (31편)

| # | 제목 | 한 줄 요약 | 분류 | 발표 |
|---:|---|---|---|---|
| 1 | [Beyond Outcome Rewards: Process-Aware Optimization for Search Agents](https://neurips.cc/virtual/2026/poster/148305) | 검색 에이전트를 위한 과정 인지형 그룹 보상 최적화 PAGE | RAG |  |
| 2 | [Beyond Outcome Rewards: Step-Level Self-Distilled Policy Optimization for Deep Search Agents](https://neurips.cc/virtual/2026/poster/154780) | 증거 앵커 기반 스텝 단위 자기증류로 딥서치 에이전트 RL 학습 | RAG | Poster |
| 3 | [Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction](https://neurips.cc/virtual/2026/poster/155649) | 임베딩 없이 grep 등으로 코퍼스를 직접 탐색하는 에이전틱 검색 | RAG | **Spotlight** |
| 4 | [CARD: Internalizing Expert Critique into Reinforcement Learning for Deep Search](https://neurips.cc/virtual/2026/poster/152838) | 전문가 비평을 내재화하는 딥서치 강화학습 CARD | RAG | Poster |
| 5 | [DAGent: Evaluate-then-Grow Planning for Deep Research Agents](https://neurips.cc/virtual/2026/poster/150664) | 평가 후 확장 방식의 DAG 기반 딥리서치 에이전트 계획(DAGent) | RAG | Poster |
| 6 | [Deep Research as Rubric](https://neurips.cc/virtual/2026/poster/153645) | 다회 agentic search로 지식 기반 rubric을 구축해 GRPO 보상으로 쓰는 DR-rubric-8B | RAG | Poster |
| 7 | [FlyAOC: Evaluating Agentic Ontology Curation of Drosophila Scientific Knowledge Bases](https://neurips.cc/virtual/2026/poster/139748) | FlyAOC: 문헌 검색 기반 과학 지식베이스 온톨로지 큐레이션 에이전트 벤치마크 | RAG |  |
| 8 | [Gen-Searcher: Reinforcing Agentic Search for Image Generation](https://neurips.cc/virtual/2026/poster/153355) | 검색 증강 이미지 생성 에이전트 Gen-Searcher를 RL로 학습 | RAG | Poster |
| 9 | [Incentivizing Agentic Retrieval for Disease-Centric Clinical Case Search via Trajectory Memory](https://neurips.cc/virtual/2026/poster/149120) | 궤적 메모리 기반 에이전틱 임상 사례 검색 | Medical RAG, RAG | Poster |
| 10 | [InterLV-Search: Benchmarking Interleaved Multimodal Agentic Search](https://neurips.cc/virtual/2026/poster/139197) | 언어-비전 교차 멀티모달 에이전틱 검색 벤치마크 | RAG | Poster |
| 11 | [Knowledge-Graph Paths as Intermediate Supervision for Self-Evolving Search Agents](https://neurips.cc/virtual/2026/poster/156148) | 지식그래프 경로로 자기진화 검색 에이전트 학습 감독 | RAG | Poster |
| 12 | [LatentRAG: Latent Reasoning and Retrieval for Efficient Agentic RAG](https://neurips.cc/virtual/2026/poster/153688) | 잠재 추론·검색으로 효율적인 에이전틱 RAG (LatentRAG) | RAG | Poster |
| 13 | [OASES: Outcome-Aligned Search-Evaluation Co-Training for Agentic Search](https://neurips.cc/virtual/2026/poster/148732) | 결과 정렬 검색-평가 공동 학습으로 검색 에이전트 강화 | RAG |  |
| 14 | [OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents](https://neurips.cc/virtual/2026/poster/152165) | 프런티어급 멀티모달 검색 에이전트를 위한 오픈 레시피 | RAG | Poster |
| 15 | [OpenSearcher: Democratizing Deep Search through a Fully Offline Pipeline with Programmatic Verification](https://neurips.cc/virtual/2026/poster/152128) | 완전 오프라인 파이프라인으로 딥서치 에이전트 학습 데이터 합성 | RAG | Poster |
| 16 | [PatchScout: Thematic Web Data Collection via Information Foraging](https://neurips.cc/virtual/2026/poster/155418) | PatchScout: 정보 포리징 기반 멀티에이전트 주제별 웹 데이터 수집 | RAG |  |
| 17 | [PiCA: Pivot-Based Credit Assignment For Search Agentic Reinforcement Learning](https://neurips.cc/virtual/2026/poster/155622) | 검색 에이전트 RL을 위한 피벗 기반 크레딧 할당 | RAG | Poster |
| 18 | [Quest: Training Frontier Deep Research Agents with Fully Synthetic Tasks](https://neurips.cc/virtual/2026/poster/150926) | 합성 과제로 학습한 오픈 deep research 에이전트 Quest | RAG | Poster |
| 19 | [Retriever-Free Retrieval-Augmented Reasoning via Corpus-Traversing MCTS](https://neurips.cc/virtual/2026/poster/148700) | 별도 retriever 없이 코퍼스 탐색 MCTS로 검색증강 추론 FREESON | RAG | Poster |
| 20 | [REVERSE: Reinforcing Evidence Verification and Search for Agentic Image Geolocation](https://neurips.cc/virtual/2026/poster/154894) | 검색/증거 검증을 강화학습하는 에이전트형 이미지 지오로케이션 REVERSE | RAG | Poster |
| 21 | [RICE-PO: Turning Retrieval Interactions into Credit Signals for Reasoning Agents](https://neurips.cc/virtual/2026/poster/155818) | 검색 상호작용을 credit 신호로 바꾸는 추론 에이전트 최적화 RICE-PO | RAG | Poster |
| 22 | [SciResearchBench: Benchmarking AI Agents on Complex Scientific Literature Discovery](https://neurips.cc/virtual/2026/poster/139663) | 과학 문헌 탐색 AI 에이전트 벤치마크 SciResearchBench | RAG | Poster |
| 23 | [SCOPE: Self-Play via Co-Evolving Policies for Open-Ended Tasks](https://neurips.cc/virtual/2026/poster/148234) | 다중턴 검색으로 풀며 공진화하는 개방형 과제 self-play SCOPE | RAG | Poster |
| 24 | [SD-Search: Hindsight Self-Distillation for Search-Augmented Reasoning](https://neurips.cc/virtual/2026/poster/155518) | hindsight self-distillation으로 검색증강 추론의 step 수준 감독 SD-Search | RAG | Poster |
| 25 | [Search More, Think Less: Rethinking Long-Horizon Agentic Search for Efficiency and Generalization](https://neurips.cc/virtual/2026/poster/153611) | 병렬 증거 수집으로 효율적인 장기 agentic search SMTL | RAG | Poster |
| 26 | [Self Driving Datasets: From 20 Million Papers to Nuanced Biomedical Knowledge at Scale](https://neurips.cc/virtual/2026/poster/139739) | PubMed 22.5M편에서 구조화 데이터를 만드는 멀티에이전트 deep research Starling | RAG | Poster |
| 27 | [SlackBench: Benchmarking Agents on Collaborative Projects Grounded in Real Code Repositories](https://neurips.cc/virtual/2026/poster/139475) | 업무 대화와 코드 저장소를 가로지르는 에이전트 검색 벤치마크 SlackBench | RAG | Poster |
| 28 | [Towards On-Policy Data Evolution for Visual-Native Multimodal Deep Search Agents](https://neurips.cc/virtual/2026/poster/148687) | 시각 네이티브 멀티모달 딥서치 에이전트와 온폴리시 데이터 진화 | RAG | Poster |
| 29 | [VideoSailor: Navigating Video Deep Research via Trajectory-to-Policy Flywheel](https://neurips.cc/virtual/2026/poster/148818) | 영상 딥리서치를 위한 궤적-정책 플라이휠 에이전트 VideoSailor | RAG | Poster |
| 30 | [VSearcher: Long-Horizon Multimodal Search Agent via Reinforcement Learning](https://neurips.cc/virtual/2026/poster/149459) | 강화학습으로 학습한 장기 멀티모달 검색 에이전트 VSearcher | RAG |  |
| 31 | [Z-AXIS: From Deterministic Ground to Agentic Depth for Enterprise Evaluation](https://neurips.cc/virtual/2026/poster/150216) | 결정론적 근거 확보와 계층적 에이전트 deep research를 결합한 기업용 평가 시스템 Z-AXIS | RAG | Poster |

#### RAG 방법론 (25편)

| # | 제목 | 한 줄 요약 | 분류 | 발표 |
|---:|---|---|---|---|
| 1 | [Align-RAG: Alignment Is All You Need for TSFM In-Context Learning](https://neurips.cc/virtual/2026/poster/152416) | 시계열 파운데이션 모델용 학습 불필요 검색증강 예측 Align-RAG | RAG | Poster |
| 2 | [Autofocus Retrieval: An Effective Pipeline for Multi-Hop Question Answering With Semi-Structured Knowledge](https://neurips.cc/virtual/2026/poster/156757) | 반구조화 지식베이스 멀티홉 QA를 위한 구조+텍스트 검색 및 LLM 리랭킹 파이프라인 AF-Retriever | RAG |  |
| 3 | [Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation](https://neurips.cc/virtual/2026/poster/150607) | 에이전트 메모리용 계층 구조 분해·집계 검색 xMemory | RAG | Poster |
| 4 | [Beyond Raw Context Transfer: Representation-based Federated Retrieval-Augmented Generation](https://neurips.cc/virtual/2026/poster/150023) | 원문 대신 잠재 표현만 교환하는 프라이버시 보존 연합 RAG | RAG | Poster |
| 5 | [Conflict-Suppressed RAG: A Simple Decoding-Time Framework for Faithful Retrieval-Augmented Generation](https://neurips.cc/virtual/2026/poster/148415) | 파라메트릭-검색 지식 충돌을 억제하는 학습 불필요 디코딩 RAG(CSRAG) | RAG | Poster |
| 6 | [Differentiable Retrieval-Augmented Generation for Predicting Cellular Responses to Gene Perturbation](https://neurips.cc/virtual/2026/poster/152229) | 유전자 교란 세포 반응 예측을 위한 미분가능 RAG(PT-RAG) | RAG | Poster |
| 7 | [Epitope-Conditioned Nanobody CDR Design via Retrieval-Augmented Protein Language Models](https://neurips.cc/virtual/2026/poster/156094) | retrieval-augmented 단백질 언어모델로 에피토프 조건 나노바디 CDR 서열 생성 | RAG | Poster |
| 8 | [Gradient Boosted Trees for Retrieval-Augmented Generation](https://neurips.cc/virtual/2026/poster/153272) | gradient boosting을 쿼리 분해에 적용한 RAG (GBT-RAG) | RAG | Poster |
| 9 | [Hi-Q: Hierarchical Evidence-guided Query Refinement for Multi-Hop Question Answering](https://neurips.cc/virtual/2026/poster/155067) | 증거 기반 쿼리 정제를 통한 멀티홉 QA 검색 (Hi-Q) | RAG | Poster |
| 10 | [Improving Consistency in Retrieval Augmented Systems With Group Similarity Rewards](https://neurips.cc/virtual/2026/poster/150565) | 그룹 유사도 보상으로 RAG 출력 일관성 향상 | RAG | Poster |
| 11 | [Knowing What is Missing: Efficient Conversational Memory via Explicit Evidence-Gap Tracking](https://neurips.cc/virtual/2026/poster/149691) | MemR3: evidence-gap 상태 추적으로 토큰 효율적인 대화 메모리 검색 | RAG |  |
| 12 | [Latent Abstraction for Retrieval-Augmented Generation](https://neurips.cc/virtual/2026/poster/155353) | 잠재 추상화로 retriever-generator를 결합한 RAG (LAnR) | RAG | Poster |
| 13 | [Lean Refactor: Multi-Objective Controllable Proof Optimization via Agentic Strategy Search](https://neurips.cc/virtual/2026/poster/149326) | Lean Refactor: 전략 DB 검색 기반 Lean 증명 리팩토링 에이전트 | RAG | Poster |
| 14 | [Less Evidence, Better Answering: Gain-Aware Minimal Evidence Subset Selection for Medical QA](https://neurips.cc/virtual/2026/poster/152857) | 의료 QA를 위한 이득 인지 최소 증거 부분집합 선택 | Medical QA, Medical RAG, RAG | Poster |
| 15 | [LogicTree-RAG: Logic Tree-guided Retrieval-Augmented Generation for Long-form Patent Drafting](https://neurips.cc/virtual/2026/poster/153327) | 특허 초안 장문 생성을 위한 논리 트리 기반 RAG | RAG | Poster |
| 16 | [Machine Learning-Driven RAG System Design](https://neurips.cc/virtual/2026/poster/155514) | 대리모델로 RAG 설계 선택을 예측·최적화 | RAG | Poster |
| 17 | [ManipulationRAG: Retrieval-Augmented Fine-Grained Manipulation of Object Functional Parts](https://neurips.cc/virtual/2026/poster/151554) | ManipulationRAG: 검색한 조작 지식으로 diffusion 손 동작 생성을 보강 | RAG | Poster |
| 18 | [Mitigating Knowledge Conflicts in Retrieval-Augmented Generation via Inference-Time Representation Editing](https://neurips.cc/virtual/2026/poster/148202) | 표현 편집으로 RAG의 검색-파라메트릭 지식 충돌 완화 | RAG | Poster |
| 19 | [ReCon: Toward Balanced Learning under Inter-Context and Context-Memory Conflicts](https://neurips.cc/virtual/2026/poster/149688) | RAG의 컨텍스트 간/메모리 간 지식 충돌을 균형 있게 학습하는 RLVR ReCon | RAG | Poster |
| 20 | [Retrieval from Within: An Intrinsic Capability of Attention-Based Models](https://neurips.cc/virtual/2026/poster/154257) | 디코더 attention으로 내부 검색을 수행하는 통합 RAG 프레임워크 INTRA | RAG | Poster |
| 21 | [RL-Guided Temporal Localization for Dual-Channel Retrieval in Long-Horizon Agent Memory](https://neurips.cc/virtual/2026/poster/152090) | RL로 시간 구간을 찾는 장기 에이전트 메모리 이중채널 검색 TIDER | RAG | Poster |
| 22 | [RVR: Retrieve-Verify-Retrieve for Comprehensive Question Answering](https://neurips.cc/virtual/2026/poster/154429) | 검증기를 이용해 반복 검색으로 다중 정답 커버리지를 높이는 Retrieve-Verify-Retrieve 프레임워크 | RAG | Poster |
| 23 | [SAGE: Semantic Ambiguity Guided Capacity Expansion for Retrieval-Augmented Generation](https://neurips.cc/virtual/2026/poster/150303) | 의미 모호 영역에 scorer 용량을 확장하는 경량 RAG SAGE | RAG | Poster |
| 24 | [SEISMOS: A Statistical Signal Detection Framework for Semantic Chunking](https://neurips.cc/virtual/2026/poster/153238) | 통계적 신호 검출 기반 RAG용 시맨틱 청킹 SEISMOS | RAG | Poster |
| 25 | [ShiftRAG: Bypassing the Textual Bottleneck via Decoupled Learning and Continuous Soft Tokens](https://neurips.cc/virtual/2026/poster/150524) | soft token으로 검색 신호를 생성기에 전달하는 분리형 RAG ShiftRAG | RAG | Poster |

#### GraphRAG / KG (13편)

| # | 제목 | 한 줄 요약 | 분류 | 발표 |
|---:|---|---|---|---|
| 1 | [Cite What You Explore: Budget-Aware LLM Reasoning over Medical KGs with Verifiable Evidence](https://neurips.cc/virtual/2026/poster/153952) | 의료 KG 위에서 예산 제약 하에 근거 인용 가능한 LLM 퇴원 후 위험 예측 | Medical RAG, RAG |  |
| 2 | [CoRE-RL: Co-evolving Reasoning Trajectories and Evidence Subgraphs with Learned Evidence Projection](https://neurips.cc/virtual/2026/poster/151276) | 추론 중 증거 서브그래프를 공진화시키는 KGQA 프레임워크(CoRE-RL) | RAG | Poster |
| 3 | [CWAGraph: Retrieving What Was Never Explicitly Identified in Graph-Based RAG](https://neurips.cc/virtual/2026/poster/149212) | 폐쇄 세계 가정을 반영한 그래프 기반 RAG(CWAGraph) | RAG | Poster |
| 4 | [Efficient and Transferable Agentic Knowledge Graph RAG via Reinforcement Learning](https://neurips.cc/virtual/2026/poster/151304) | 강화학습으로 최적화한 효율적 에이전트형 KG-RAG(KG-R1) | RAG | Poster |
| 5 | [Foresight-over-Graph: Reasoning Beyond Local Horizons for Knowledge Base Question Answering](https://neurips.cc/virtual/2026/poster/150820) | 비근시적 전방 탐색으로 KBQA 증거 검색(Foresight-over-Graph) | RAG | Poster |
| 6 | [Geometric Gain Graph: Zero-Token Graph Construction for Multi-Hop RAG](https://neurips.cc/virtual/2026/poster/151572) | 추가 토큰 없이 그래프를 구성하는 멀티홉 RAG (Geometric Gain Graph) | RAG |  |
| 7 | [HiddenPathQA: A Benchmark for Knowledge Graph Question Answering When Questions Hide Their Paths](https://neurips.cc/virtual/2026/poster/139751) | HiddenPathQA: 질문이 KG 경로를 드러내지 않는 KGQA 벤치마크와 Holistic Path Selection | RAG | Poster |
| 8 | [Learning Minimal Sufficient Evidence Graphs for GraphRAG via Nash-Guided Optimization](https://neurips.cc/virtual/2026/poster/154710) | Nash 최적화로 최소 충분 증거 그래프를 학습하는 GraphRAG | RAG |  |
| 9 | [LP-RAG: Learning to Retrieve with Link Predictors](https://neurips.cc/virtual/2026/poster/149466) | 링크 예측기로 검색을 학습하는 그래프 RAG (LP-RAG) | RAG |  |
| 10 | [MicroWorld: Empowering Multimodal Large Language Models to Bridge the Microscopic Domain Gap with Multimodal Attribute Graph](https://neurips.cc/virtual/2026/poster/151480) | 현미경 도메인용 멀티모달 속성 그래프 검색으로 MLLM 추론 강화 | RAG, Medical RAG | Poster |
| 11 | [PatternBloom: Empowering Agentic RAG with Externalized RL-Distilled Graph Patterns](https://neurips.cc/virtual/2026/poster/152560) | RL로 증류한 그래프 패턴을 외부화한 에이전틱 RAG | RAG | Poster |
| 12 | [RAVEL: Rare Concept Generation and Editing via Graph-driven Relational Guidance](https://neurips.cc/virtual/2026/poster/150127) | 지식그래프 기반 RAG로 T2I 희귀 개념 생성/편집 개선 RAVEL | RAG | Poster |
| 13 | [Substrata: Know What You Don't Know](https://neurips.cc/virtual/2026/poster/152606) | 모르는 것을 인지하는 지식그래프 기반 RAG 프레임워크 Substrata | RAG | Poster |

#### Multimodal RAG (10편)

| # | 제목 | 한 줄 요약 | 분류 | 발표 |
|---:|---|---|---|---|
| 1 | [AgenticOCR: Parsing Only What You Need for Efficient Retrieval-Augmented Generation](https://neurips.cc/virtual/2026/poster/153107) | 시각 문서 RAG를 위해 질의 기반으로 필요한 영역만 OCR하는 AgenticOCR | RAG | Poster |
| 2 | [BayesRAG: Probabilistic Mutual Evidence Corroboration for Multimodal Retrieval-Augmented Generation](https://neurips.cc/virtual/2026/poster/154974) | 베이지안 증거 융합으로 텍스트-이미지 검색을 보정하는 멀티모달 RAG | RAG | Poster |
| 3 | [Beyond Visual Boundaries: Rethinking Scene Segmentation for Movie RAG](https://neurips.cc/virtual/2026/poster/139396) | 영화 RAG의 검색 단위로 서사 중심 장면 분할 데이터셋 제안 | RAG | Poster |
| 4 | [Bridging Modalities, Spanning Time: Structured Memory for Ultra-Long Agentic Video Reasoning](https://neurips.cc/virtual/2026/poster/156072) | 멀티모달 메모리 그래프 검색 기반 초장기 비디오 에이전트 추론 | RAG | Poster |
| 5 | [CAM: Question Answering on Entity-Centric Videos with Continuous Extraction and Adaptive Querying](https://neurips.cc/virtual/2026/poster/150537) | 지식그래프 메모리와 적응형 질의로 개체 중심 영상 QA | RAG | Poster |
| 6 | [City-RAG: Stepping Into a City via Spatially-Grounded Video Generation](https://neurips.cc/virtual/2026/poster/154638) | 지리 등록 데이터를 컨텍스트로 쓰는 공간 접지 도시 영상 생성(CityRAG) | RAG | **Spotlight** |
| 7 | [DocAtlas: Long-Document Understanding as Mutable-State Interaction](https://neurips.cc/virtual/2026/poster/148605) | 가변 상태 상호작용으로 긴 문서를 이해하는 에이전트형 시스템(DocAtlas) | RAG | Poster |
| 8 | [MMGraph-Agent: Agentic Multimodal RAG via Cache-Inspired Multimodal Knowledge HyperGraphs](https://neurips.cc/virtual/2026/poster/156108) | 캐시에서 착안한 멀티모달 지식 하이퍼그래프 기반 에이전틱 RAG | RAG | Poster |
| 9 | [MoRe-DVC: Motion Retrieval-Augmented Generation for Detailed Video Captioning](https://neurips.cc/virtual/2026/poster/152051) | 모션 검색 증강으로 상세 비디오 캡셔닝의 환각 감소 | RAG |  |
| 10 | [ReCoG: Relational Concept Graph for Training-Free Personalization](https://neurips.cc/virtual/2026/poster/149776) | 관계 그래프 기반 검색증강 VLM 개인화 ReCoG | RAG | Poster |

#### 강건성·보안·프라이버시 (10편)

| # | 제목 | 한 줄 요약 | 분류 | 발표 |
|---:|---|---|---|---|
| 1 | [Breadcrumbing Search Agents: Per-Turn Scheming Over Long-Horizon Trajectories](https://neurips.cc/virtual/2026/poster/150737) | 검색 결과 채널을 조작해 검색 에이전트를 장기 공격하는 방법 | RAG | Poster |
| 2 | [DECEIVE-AFC: Adversarial Claim Attacks against Search-Enabled LLM-based Fact-Checking Systems](https://neurips.cc/virtual/2026/poster/150419) | 검색 기반 LLM 팩트체킹에 대한 적대적 주장 공격(DECEIVE-AFC) | RAG | Poster |
| 3 | [EcoGEO: Trajectory-Aware Evidence Ecosystems for Web-Enabled LLM Search Agents](https://neurips.cc/virtual/2026/poster/153813) | 웹 검색 LLM 에이전트 궤적을 겨냥한 증거 생태계 GEO(EcoGEO) | RAG | Poster |
| 4 | [Exposing Private Corpus Leakage in Multimodal RAG](https://neurips.cc/virtual/2026/poster/154898) | 멀티모달 RAG의 검색 코퍼스 프라이버시 유출 노출 | RAG |  |
| 5 | [Privacy-Preserving Retrieval-Augmented Generation with Plausible Deniability](https://neurips.cc/virtual/2026/poster/150803) | 그럴듯한 부인가능성을 보장하는 프라이버시 보존 RAG | RAG |  |
| 6 | [Reasoning Poisoning: Utilizing Social-Engineering to Steer Chain-of-Thought](https://neurips.cc/virtual/2026/poster/151543) | 검색 컨텍스트 조작으로 추론 모델을 유도하는 Reasoning Poisoning 공격 | RAG |  |
| 7 | [Synthetic Web: Benchmarking Language Agents under Adversarial Search Ranking](https://neurips.cc/virtual/2026/poster/155345) | 적대적 검색 랭킹 하에서 웹 에이전트 강건성을 평가하는 Synthetic Web 벤치마크 | RAG |  |
| 8 | [The Web Doesn't Sit Still: Adversarial Self-Evolving Attacks on Search Agents](https://neurips.cc/virtual/2026/poster/149493) | 검색 에이전트에 대한 적대적 자기진화 공격 프레임워크 | RAG | Poster |
| 9 | [Train-free Data Poisoning Attack against Retrieval-augmented Diffusion Models](https://neurips.cc/virtual/2026/poster/153591) | 검색 증강 확산모델에 대한 무학습 데이터 포이즈닝 공격 | RAG | Poster |
| 10 | [When Poison Meets Structure: Topology-based Defense against Poisoning Attack on Graph-based Retrieval-Augmented Generation](https://neurips.cc/virtual/2026/poster/152350) | GraphRAG 포이즈닝에 대한 위상 기반 방어 | RAG |  |

#### 벤치마크·평가 (17편)

| # | 제목 | 한 줄 요약 | 분류 | 발표 |
|---:|---|---|---|---|
| 1 | [AgentHop: A Diagnostic Benchmark for Agentic Multi-Hop Scientific Question Answering](https://neurips.cc/virtual/2026/poster/139240) | 에이전트 다단계 과학 QA의 검색·합성·도구호출 실패를 진단하는 벤치마크 | RAG | Poster |
| 2 | [Can AI Agents Synthesize Scientific Conclusions?](https://neurips.cc/virtual/2026/poster/139077) | 체계적 문헌고찰 기반 과학적 결론 합성 에이전트 벤치마크 | Medical QA, RAG |  |
| 3 | [Can LLMs Take Retrieved Information with a Grain of Salt?](https://neurips.cc/virtual/2026/poster/148640) | 검색 문맥의 불확실성 표현에 LLM이 맞게 반응하는지 평가 | RAG | Poster |
| 4 | [Deceptive Grounding: Entity Attribution Failure in Clinical Retrieval-Augmented Generation](https://neurips.cc/virtual/2026/poster/152927) | 임상 RAG에서 증거를 잘못된 개체에 귀속하는 기만적 접지 실패 분석 | Medical RAG, RAG | Poster |
| 5 | [E-GEO: A Testbed for Generative Engine Optimization in E-Commerce](https://neurips.cc/virtual/2026/poster/139483) | 이커머스 생성형 엔진 최적화(GEO) 테스트베드(E-GEO) | RAG | Poster |
| 6 | [FACBench: A Benchmark for Formal-Anchor Collisions in Multilingual Mathematical Grounding](https://neurips.cc/virtual/2026/poster/139472) | retrieval-augmented 자동형식화에서 다국어 Lean 앵커 충돌을 평가하는 FACBench | RAG | Poster |
| 7 | [From Intent to Evidence: A Categorical Approach for Structural Evaluation of Deep Research Agents](https://neurips.cc/virtual/2026/poster/153875) | 범주론 기반 딥리서치 에이전트 구조적 평가 벤치마크 | RAG | Poster |
| 8 | [GISA: A Benchmark for General Information-Seeking Assistant](https://neurips.cc/virtual/2026/poster/139591) | 범용 정보탐색 검색 에이전트 벤치마크 GISA | RAG | Poster |
| 9 | [LongMINT: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems](https://neurips.cc/virtual/2026/poster/149299) | LongMINT: 간섭 하의 장기 에이전트 메모리/RAG 평가 벤치마크 | RAG | Poster |
| 10 | [MiroEval: Benchmarking Multimodal Deep Research Agents in Process and Outcome](https://neurips.cc/virtual/2026/poster/139149) | 멀티모달 딥리서치 에이전트의 과정과 결과를 평가하는 벤치마크 | RAG | Poster |
| 11 | [OmniMemBench: Towards Scalable Evaluation of Long-Term Omni-Modal Agent Memory](https://neurips.cc/virtual/2026/poster/138886) | OmniMemBench: 이미지/오디오/비디오 장기 메모리 및 RAG 검색 평가 | RAG | Poster |
| 12 | [RAG in a Trenchcoat: When Minimal Memory Is Enough for Agentic Systems, and When It Isn’t](https://neurips.cc/virtual/2026/poster/151457) | 최소 RAG 메모리 Bridge와 에이전트 메모리 평가 한계 분석 | RAG |  |
| 13 | [RealDev-QA: Trajectory-Level Diagnosis for Developer RAG Under Real-World Noises](https://neurips.cc/virtual/2026/poster/139440) | 노이즈 많은 개발자 질의용 RAG 궤적 진단 벤치마크 RealDev-QA | RAG | Poster |
| 14 | [RTCBench: Evaluating Tool Use of Large Language Models Beyond Oracle Access](https://neurips.cc/virtual/2026/poster/139584) | 도구 검색을 요구하는 검색증강 tool-calling 벤치마크 RTCBench | RAG | Poster |
| 15 | [SourceBench: Can AI Answers Reference Quality Web Sources?](https://neurips.cc/virtual/2026/poster/139217) | AI 답변이 인용한 웹 출처의 품질을 측정하는 SourceBench | RAG | Poster |
| 16 | [TopoGraphRAG-Bench: Evaluating Multimodal GraphRAG on Layout-Grounded Evidence Reasoning](https://neurips.cc/virtual/2026/poster/139025) | 레이아웃 기반 증거 추론을 평가하는 멀티모달 GraphRAG 벤치마크 | RAG | Poster |
| 17 | [When Does Graph Retrieval Become Answer-Supporting Evidence? A Diagnostic Audit of GraphRAG](https://neurips.cc/virtual/2026/poster/139414) | GraphRAG의 검색 증거가 답변 근거가 되는지 진단하는 감사 연구 | RAG | Poster |

#### 효율 (KV cache·압축·지연) (6편)

| # | 제목 | 한 줄 요약 | 분류 | 발표 |
|---:|---|---|---|---|
| 1 | [AgentKVShift: Efficient KV Cache Reuse for Agentic Memory Systems](https://neurips.cc/virtual/2026/poster/155404) | 에이전트 메모리 검색 결과의 KV 캐시 재사용을 보정하는 AgentKVShift | RAG | Poster |
| 2 | [Failure-Band Authorization for Filtered Retrieval](https://neurips.cc/virtual/2026/poster/153631) | RAG용 필터링 벡터 검색의 tail latency를 안정화하는 authorize/veto 컨트롤러 PACER | RAG | Poster |
| 3 | [KVFocus: A Perturbation-Theoretic Token-Risk Score for Selective KV Cache Reuse in RAG](https://neurips.cc/virtual/2026/poster/149014) | RAG의 선택적 KV 캐시 재사용을 위한 토큰 위험 점수 KVFocus | RAG | Poster |
| 4 | [MiniPIC: Flexible Position-Independent Caching in <100LOC](https://neurips.cc/virtual/2026/poster/151329) | RAG/에이전트 워크로드용 위치 독립 KV 캐싱을 100줄 미만으로 구현 | RAG | Poster |
| 5 | [OpticalRAG: Pixel-Space Compression for Token-Efficient Retrieval-Augmented Generation](https://neurips.cc/virtual/2026/poster/152209) | 문서를 픽셀 공간으로 압축해 토큰 효율적인 RAG 구현 | RAG | Poster |
| 6 | [SpecHop: Continuous Speculation for Accelerating Multi-Hop Retrieval Agents](https://neurips.cc/virtual/2026/poster/150381) | 멀티홉 검색 에이전트 지연을 줄이는 무손실 연속 speculation SpecHop | RAG | Poster |

#### 기타 (비텍스트 생성 등) (10편)

| # | 제목 | 한 줄 요약 | 분류 | 발표 |
|---:|---|---|---|---|
| 1 | [Beyond Uniform Detection: Adaptive Hallucination Detection for RAG Across Response Regimes](https://neurips.cc/virtual/2026/poster/155755) | 응답 유형별 신호를 달리 쓰는 RAG 환각 탐지기 ARGUS | RAG | Poster |
| 2 | [Data Auctions for Retrieval Augmented Generation](https://neurips.cc/virtual/2026/poster/154287) | RAG용 데이터 판매를 위한 경매 메커니즘 설계 | RAG | Poster |
| 3 | [Diagnosing and Repairing Citation Failures in Generative Engine Optimization](https://neurips.cc/virtual/2026/poster/153428) | 생성형 검색엔진에서 문서 인용 실패를 진단하고 수리하는 GEO | RAG | Poster |
| 4 | [How Much Evidence Should Retrieval-Augmented In-Context Learning Use Under Distribution Shift?](https://neurips.cc/virtual/2026/poster/149872) | 분포 이동 하에서 retrieval-augmented ICL의 증거 사용량 이론/진단 | RAG | Poster |
| 5 | [In-Context Optimization for Retrieval-Augmented Generation: A Gradient-Descent Perspective](https://neurips.cc/virtual/2026/poster/150330) | RAG를 in-context 최적화(경사하강) 관점으로 분석 | RAG | Poster |
| 6 | [Invisible Ink, Visible Lies: How Production Watermarking Causes LLMs to Hallucinate](https://neurips.cc/virtual/2026/poster/152321) | RAG 설정에서 워터마킹이 유발하는 환각 분석 | RAG | Poster |
| 7 | [Not All Gap Correction Helps: A Geometric View of External Information in LLM Inference](https://neurips.cc/virtual/2026/poster/153389) | ICL·RAG·메모리의 외부 정보가 LLM 추론에 미치는 영향의 기하학적 분석 | RAG | Poster |
| 8 | [Overthinking as a Symptom of Knowledge Conflict: Understanding and Detecting LLM's Hallucinations in Retrieval-Augmented Question Answering](https://neurips.cc/virtual/2026/poster/150716) | RAG 질의응답에서 과잉 사고와 지식 충돌 기반 환각 탐지 | RAG | Poster |
| 9 | [Reading Attribution from Attention: Evidence Heads as Latent Attribution Mechanisms in LLMs](https://neurips.cc/virtual/2026/poster/156092) | 멀티문서 QA에서 attention Evidence Head로 출처 attribution 추출 | RAG | Poster |
| 10 | [TRIDENT: Post-Selection Evidence Accountability for Token-Efficient RAG](https://neurips.cc/virtual/2026/poster/155841) | RAG 인용 검증의 선택 후 추론 보장과 토큰 효율화 TRIDENT | RAG | Poster |

## 키워드 트렌드 분석 (NeurIPS 2025 → 2026)

방법: 주제별 정규식이 제목+초록에 걸리는 논문 비율을 2025(5,860편)와 2026(9,094편)에서 각각 계산하고, 비율의 배수(2026 비율 ÷ 2025 비율)를 성장으로 봤다. 정규식은 `scripts/topic_trends.py`에 있다. 키워드 매칭이라 한 단어가 여러 뜻으로 쓰이는 경우(예: calibration)는 과대 집계될 수 있다.

### 의료 × LLM 논문 안에서 커진 주제

의료 용어와 LLM 용어가 함께 나오는 논문(76편 → 170편) 안에서 각 주제를 다루는 논문의 비율. 같은 키워드 규칙을 두 해에 똑같이 적용했다.

| 주제 | 2025 | 2026 |
|---|---:|---:|
| 근거·귀속·환각 | 22.4% (17) | 47.1% (80) |
| 검색 (RAG) | 3.9% (3) | 16.5% (28) |
| 에이전트·멀티에이전트 | 15.8% (12) | 26.5% (45) |
| 안전·신뢰 | 21.1% (16) | 28.8% (49) |
| 추론 (reasoning) | 40.8% (31) | 41.2% (70) |
| RL (GRPO·RLVR 등) | 10.5% (8) | 10.0% (17) |
| 불확실성·abstain | 18.4% (14) | 17.6% (30) |
| 대화·문진 | 11.8% (9) | 10.6% (18) |
| 질의응답 (QA/VQA) | 23.7% (18) | 21.8% (37) |
| 리포트 생성 | 6.6% (5) | 4.7% (8) |
| 벤치마크 (제목) | 25.0% (19) | 18.2% (31) |

### 요약

- **LLM 에이전트가 가장 크게 커진 분야다.** 14개 분야 중 'LLM 에이전트·도구·검색'만 비중이 2.99% → 6.83%로 두 배 넘게 커졌다. 키워드로 보면 LLM 용어와 agent/agentic이 함께 나오는 논문이 4.64% → 8.46%(×1.82). 그 안에서도 tool use·function calling(×3.8), deep research·search agent(×3.5), SWE·coding agent(×3.1), MCP(1편 → 17편)가 가장 빠르게 늘었다.
- **RL 후처리는 'RLVR + on-policy'로 수렴 중.** RLVR/verifiable reward ×2.9, GRPO ×1.7. 제목 기준으로는 `RLVR` 1편 → 20편, `on-policy distillation` 0편 → 18편, `credit assignment` 5편 → 22편.
- **'근거(evidence)와 감사(audit)'가 새 키워드.** 제목에 `evidence`가 들어간 논문이 5편 → 90편, `audit/auditing` 4편 → 55편, `diagnosing/diagnostic` 6편 → 52편. 정답률보다 *왜 맞았는지·어디서 틀렸는지*를 보는 논문이 늘었다.
- **신뢰성 축이 두 배.** LLM 불확실성·calibration ×2.3(107 → 386편), reward hacking·deception·sycophancy ×2.1, activation steering ×3.0(10 → 47편).
- **생성 모델은 flow matching(×1.9)·diffusion LM(×3.0)·world model(×1.7)로 이동.**
- **RAG는 정체, agentic search로 흡수 중.** 'RAG' 키워드 비율은 1.31% → 1.26%(×0.96)로 평탄하지만 deep research/search agent는 ×3.5. 이 저장소의 RAG 122편 중 31편이 agentic search 유형이다.
- **의료는 완만한 성장, Medical QA는 급증.** 의료·헬스케어 분야 비중 2.22% → 2.79%, 의료 용어와 LLM 용어가 함께 나오는 논문 76편 → 170편(비중 ×1.44), Medical QA 키워드 매칭은 6편 → 26편(×2.8).
- **하락 키워드.** in-context learning ×0.59, synthetic data ×0.64, (단어로서의) reasoning model/long CoT ×0.66, 3D Gaussian splatting ×0.68, differential privacy ×0.69, GNN ×0.72, federated learning ×0.73.

### 성장 상위 20개 주제

| 주제 | 2025 편수 (비율) | 2026 편수 (비율) | 배수 |
|---|---:|---:|---:|
| MCP (Model Context Protocol) | 1 (0.02%) | 17 (0.19%) | ×10.95 |
| Tool use / function calling | 24 (0.41%) | 141 (1.55%) | ×3.79 |
| Deep research / search agents | 10 (0.17%) | 55 (0.6%) | ×3.54 |
| Software engineering agents | 16 (0.27%) | 76 (0.84%) | ×3.06 |
| Diffusion language models | 23 (0.39%) | 108 (1.19%) | ×3.03 |
| Steering / activation editing | 10 (0.17%) | 47 (0.52%) | ×3.03 |
| Reinforcement learning w/ verifiable rewards (RLVR) | 31 (0.53%) | 141 (1.55%) | ×2.93 |
| Medical QA | 6 (0.1%) | 26 (0.29%) | ×2.79 |
| Uncertainty / calibration (LLM) | 107 (1.83%) | 386 (4.24%) | ×2.32 |
| Reward hacking / deception | 31 (0.53%) | 101 (1.11%) | ×2.1 |
| Flow matching | 79 (1.35%) | 231 (2.54%) | ×1.88 |
| LLM agents / agentic | 272 (4.64%) | 769 (8.46%) | ×1.82 |
| World models | 65 (1.11%) | 174 (1.91%) | ×1.72 |
| GRPO | 90 (1.54%) | 237 (2.61%) | ×1.7 |
| Agent memory | 20 (0.34%) | 52 (0.57%) | ×1.68 |
| Agent safety / guardrails | 20 (0.34%) | 46 (0.51%) | ×1.48 |
| Interpretability / SAE | 91 (1.55%) | 202 (2.22%) | ×1.43 |
| Knowledge distillation | 235 (4.01%) | 510 (5.61%) | ×1.4 |
| Self-evolving / self-improving | 38 (0.65%) | 82 (0.9%) | ×1.39 |
| KV cache / long-context efficiency | 115 (1.96%) | 248 (2.73%) | ×1.39 |

### 비율이 줄어든 주제 (하위 10개)

| 주제 | 2025 편수 (비율) | 2026 편수 (비율) | 배수 |
|---|---:|---:|---:|
| In-context learning | 81 (1.38%) | 74 (0.81%) | ×0.59 |
| Synthetic data | 168 (2.87%) | 167 (1.84%) | ×0.64 |
| Reasoning models / long CoT | 265 (4.52%) | 271 (2.98%) | ×0.66 |
| 3D Gaussian splatting | 83 (1.42%) | 87 (0.96%) | ×0.68 |
| Differential privacy | 65 (1.11%) | 70 (0.77%) | ×0.69 |
| Graph neural networks | 142 (2.42%) | 158 (1.74%) | ×0.72 |
| Federated learning | 95 (1.62%) | 108 (1.19%) | ×0.73 |
| Personalization | 87 (1.48%) | 100 (1.1%) | ×0.74 |
| Pluralistic / cultural alignment | 34 (0.58%) | 40 (0.44%) | ×0.76 |
| Data selection / curation | 60 (1.02%) | 72 (0.79%) | ×0.77 |

### 제목에 등장한 신규·급증 단어

제목에 해당 단어가 들어간 논문 수.

| 단어 | 2025 | 2026 |
|---|---:|---:|
| `evidence` | 5 | 90 |
| `audit / auditing` | 4 | 55 |
| `diagnosing / diagnostic` | 6 | 52 |
| `long-horizon` | 7 | 77 |
| `longitudinal` | 1 | 17 |
| `credit assignment` | 5 | 22 |
| `agent memory` | 0 | 18 |
| `skill(s)` | 9 | 56 |
| `self-evolving` | 4 | 27 |
| `on-policy distillation` | 0 | 18 |
| `self-distillation` | 6 | 26 |
| `RLVR` | 1 | 20 |

## 다음 연구 주제 제안 (일반)

트렌드 수치는 측정값이고, "아이디어"는 그 수치와 논문 목록을 근거로 한 판단이다.

### 1. Agentic search의 과정 보상·credit assignment

- **근거**: RAG 122편 중 31편이 agentic search이고, 그중 다수가 outcome reward의 한계를 다룬다. 제목의 `credit assignment`는 5편 → 22편. 아직 '어떤 검색 단계가 답에 기여했는가'를 정의하는 방식이 논문마다 제각각이라 표준이 없다.
- **아이디어**: 검색 trajectory의 각 query/문서에 기여도를 주는 보상(정보 이득, counterfactual 제거, 근거 포함 여부)을 비교·통합하는 연구. 효율(검색 횟수·토큰) 제약을 같이 거는 버전이 차별점.
- **관련 NeurIPS 2026 논문**: [RICE-PO](https://neurips.cc/virtual/2026/poster/155818), [PiCA](https://neurips.cc/virtual/2026/poster/155622), [Beyond Outcome Rewards: Process-Aware Optimization for Searc](https://neurips.cc/virtual/2026/poster/148305), [Beyond Outcome Rewards: Step-Level Self-Distilled Policy Opt](https://neurips.cc/virtual/2026/poster/154780), [CARD](https://neurips.cc/virtual/2026/poster/152838), [Search More, Think Less](https://neurips.cc/virtual/2026/poster/153611)

### 2. 근거 귀속(attribution)과 감사 가능한 생성

- **근거**: 제목 `evidence` 5 → 90편, `audit/auditing` 4 → 55편. 생성 결과를 근거 단위로 검증하는 연구가 RAG·VLM·의료에서 동시에 나오고 있다.
- **아이디어**: claim 단위로 '이 문장은 이 근거에서 왔다'를 모델 내부 신호(attention head)와 외부 검증기로 이중 확인하고, 불일치 시 abstain하는 파이프라인.
- **관련 NeurIPS 2026 논문**: [Reading Attribution from Attention](https://neurips.cc/virtual/2026/poster/156092), [TRIDENT](https://neurips.cc/virtual/2026/poster/155841), [Deceptive Grounding](https://neurips.cc/virtual/2026/poster/152927), [MedVIGIL](https://neurips.cc/virtual/2026/poster/139346), [Cite What You Explore](https://neurips.cc/virtual/2026/poster/153952)

### 3. On-policy distillation / self-distillation으로 에이전트 압축

- **근거**: 제목 `on-policy distillation` 0 → 18편, `self-distillation` 6 → 26편. 큰 에이전트의 다단계 행동을 작은 모델로 옮기는 수요(온프렘·비용)가 크다.
- **아이디어**: 툴 호출·검색을 포함한 agentic trajectory를 on-policy로 증류하되, 교사와 학생의 행동 분포 차이(어디서 검색을 멈추는가)를 명시적으로 맞추는 방법.
- **관련 NeurIPS 2026 논문**: [SD-Search](https://neurips.cc/virtual/2026/poster/155518), [Beyond Outcome Rewards: Step-Level Self-Distilled Policy Opt](https://neurips.cc/virtual/2026/poster/154780), [Med-Agentic](https://neurips.cc/virtual/2026/poster/153012), [MedPsy](https://neurips.cc/virtual/2026/poster/150557)

### 4. 에이전트 메모리와 self-evolving skill

- **근거**: 제목 `agent memory` 0 → 18편, `skill(s)` 9 → 56편, `self-evolving` 4 → 27편. 'RAG로 충분한가, 별도 메모리가 필요한가'를 정면으로 다루는 논문이 등장했다.
- **아이디어**: 경험을 skill/메모리로 축적할 때 오래된·충돌하는 기억을 어떻게 폐기·갱신하는지(망각 정책)에 대한 연구. 의료처럼 지식이 바뀌는 도메인에서 특히 비어 있다.
- **관련 NeurIPS 2026 논문**: [RAG in a Trenchcoat](https://neurips.cc/virtual/2026/poster/151457), [MedMemoryBench](https://neurips.cc/virtual/2026/poster/139145), [Experience Makes Skillful](https://neurips.cc/virtual/2026/poster/150444), [LongMINT](https://neurips.cc/virtual/2026/poster/149299)

### 5. 에이전트의 불확실성·선택적 응답

- **근거**: LLM 불확실성·calibration 키워드가 ×2.3(107 → 386편)으로 상위 성장. 단일 응답 calibration은 많지만 다단계 에이전트의 calibration(언제 멈추고 사람에게 넘길지)은 적다.
- **아이디어**: 다회 tool use 에이전트에서 단계별 위험을 누적해 conformal 방식으로 '넘김(defer)' 시점을 보장하는 방법.
- **관련 NeurIPS 2026 논문**: [Calibrating Agentic LLMs for Clinical Prediction](https://neurips.cc/virtual/2026/poster/149149), [Selective Answering for Medical VQA via Parallel Independent Claim Verification](https://neurips.cc/virtual/2026/poster/150272), [Learning When to Collaborate](https://neurips.cc/virtual/2026/poster/148185), [MoBayes](https://neurips.cc/virtual/2026/poster/152953)

### 6. 현실 환경 기반 장기(long-horizon) 벤치마크

- **근거**: 제목 `long-horizon` 7 → 77편. 객관식 벤치마크 대신 EHR·워크플로 환경에서 수십 단계 작업을 평가하는 벤치마크가 빠르게 늘었다.
- **아이디어**: 벤치마크 자체보다, 이런 환경에서 실패 원인을 자동 분류(diagnosing)하고 그 분류를 학습 신호로 되돌리는 연구가 다음 단계로 보인다.
- **관련 NeurIPS 2026 논문**: [χ-Bench](https://neurips.cc/virtual/2026/poster/139361), [PhysicianBench](https://neurips.cc/virtual/2026/poster/139788), [MedFlowBench](https://neurips.cc/virtual/2026/poster/139506), [REAL-MED](https://neurips.cc/virtual/2026/poster/139773)

## Medical QA 쪽에서 해볼 만한 연구

아래 "공백"은 이 저장소의 의료 논문 100편과 RAG 122편을 비교해 찾은 것이다. 편수는 측정값이고, 공백이라는 판단은 이 목록 안에서의 판단이다(다른 학회·arXiv는 보지 않았다).

### 1. 의료 agentic search + 과정 보상 (Medical Search-R1 계열)

- **공백**: 일반 RAG 122편 중 agentic search 31편인데, 의료 100편 중 agentic search를 다룬 것은 사실상 1편(임상 증례 검색). 일반 쪽 과정 보상 기법이 의료로 거의 옮겨지지 않았다.
- **아이디어**: PubMed·가이드라인·증례 코퍼스를 검색하는 의료 QA 에이전트를 RL로 학습. 보상은 정답 + 근거 문서의 임상적 핵심 사실(atomic fact) 포함 여부 + 검색 비용.
- **출발점 논문**: [Incentivizing Agentic Retrieval for Disease-Centric Clinical Case Search via Trajectory Memory](https://neurips.cc/virtual/2026/poster/149120), [TraceDx](https://neurips.cc/virtual/2026/poster/149401), [PiCA](https://neurips.cc/virtual/2026/poster/155622), [RICE-PO](https://neurips.cc/virtual/2026/poster/155818)

### 2. 근거 귀속이 검증되는 임상 QA

- **공백**: Deceptive Grounding은 임상 RAG가 정답을 내면서도 엉뚱한 환자·약물 entity에 근거를 붙이는 실패를 보고했다. 의료 RAG는 이 저장소 기준 5편뿐이다.
- **아이디어**: 답의 각 claim을 EHR·문헌의 특정 구간에 연결하고, entity 일치까지 검증하는 attribution 평가·학습. 최소 근거 집합만 남기는 방식과 결합.
- **출발점 논문**: [Deceptive Grounding](https://neurips.cc/virtual/2026/poster/152927), [Cite What You Explore](https://neurips.cc/virtual/2026/poster/153952), [Less Evidence, Better Answering](https://neurips.cc/virtual/2026/poster/152857), [EHRNote-ChatQA](https://neurips.cc/virtual/2026/poster/139551)

### 3. 오도·충돌·구식 정보에 대한 강건성

- **공백**: MedMisBench가 오도 맥락 취약성을 측정했지만, 일반 RAG의 knowledge-conflict 해결 기법(디코딩·표현 수준)은 의료에 적용되지 않았다. 의료 언급 논문 728편 중 지식 갱신·시간적 drift를 다룬 것은 3편.
- **아이디어**: 가이드라인 개정 전후 문서가 섞인 검색 결과에서 최신·고근거 수준 정보를 따르게 하는 conflict-aware 의료 RAG와 벤치마크.
- **출발점 논문**: [MedMisBench](https://neurips.cc/virtual/2026/poster/139561), [Conflict-Suppressed RAG](https://neurips.cc/virtual/2026/poster/148415), [Mitigating Knowledge Conflicts in Retrieval-Augmented Generation via Inference-Time Representation Editing](https://neurips.cc/virtual/2026/poster/148202), [ReCon](https://neurips.cc/virtual/2026/poster/149688)

### 4. 선택적 응답·위험 통제 abstention

- **공백**: 의료 100편 중 abstain/selective를 다룬 것은 4편. 대부분 단일 턴 VQA이고, 다회 진단 대화나 에이전트 단위의 위험 보장은 드물다.
- **아이디어**: claim 검증 기반 selective answering을 다회 진단 대화로 확장하고, conformal risk control로 오답률 상한을 보장.
- **출발점 논문**: [Selective Answering for Medical VQA via Parallel Independent Claim Verification](https://neurips.cc/virtual/2026/poster/150272), [Calibrating Agentic LLMs for Clinical Prediction](https://neurips.cc/virtual/2026/poster/149149), [MoBayes](https://neurips.cc/virtual/2026/poster/152953), [Learning When to Collaborate](https://neurips.cc/virtual/2026/poster/148185)

### 5. 정보 탐색형(문진형) 대화 QA

- **공백**: MCQ 정답률은 포화에 가깝고, 2026년에는 '무엇을 물어볼지'를 학습하는 연구가 여러 편 나왔다. 다만 질문 비용·환자 부담을 보상에 넣은 연구는 드물다.
- **아이디어**: 가상 환자 시뮬레이터 위에서 질문/검사의 정보 가치(value of information)와 비용을 함께 최적화하는 RL. 시뮬레이터의 현실성 평가 프로토콜을 함께 제시.
- **출발점 논문**: [MedExAgent](https://neurips.cc/virtual/2026/poster/149616), [ProbMedTOD](https://neurips.cc/virtual/2026/poster/154360), [CoE-Agent](https://neurips.cc/virtual/2026/poster/155085), [A Stratified Multi-Rater Evaluation of LLM-Based Virtual Standardized Patients with a Deployed Data-Generation Platform](https://neurips.cc/virtual/2026/poster/139188)

### 6. 의료 VQA의 시각 근거 의존성 (영상을 실제로 보는가)

- **공백**: 의료 VLM이 영상을 무시하고 텍스트 사전지식으로 답하는 문제를 다룬 논문이 여러 편 나왔다(MedVIGIL, MedVIGOR, CRAFT, CXR attribution 등). 반면 ECG를 다룬 의료 논문은 1편, 안저(fundus)는 2편으로 모달리티 편중이 크다.
- **아이디어**: 영상 제거·교란 counterfactual로 '시각 필요도'를 측정하고 학습 데이터 선별·보상에 반영. CXR 외 ECG·안저·CT로 확장하면 공백을 메운다.
- **출발점 논문**: [MedVIGIL](https://neurips.cc/virtual/2026/poster/139346), [MedVIGOR](https://neurips.cc/virtual/2026/poster/150235), [Rethinking Visual Attribution for Chest X-ray Reasoning in Large Vision Language Models](https://neurips.cc/virtual/2026/poster/151683), [CRAFT](https://neurips.cc/virtual/2026/poster/149960), [ViCoR](https://neurips.cc/virtual/2026/poster/154516), [ECG-Reasoning-Benchmark](https://neurips.cc/virtual/2026/poster/139595)

### 7. 종단(longitudinal)·다중 검사 비교 QA

- **공백**: 제목 `longitudinal`이 1편 → 17편. 의료에서는 BrainTRACE(종단 MRI), RealICU(장기 ICU)가 있지만, 이전 검사와 비교해 변화를 묻는 영상 QA(예: CXR prior comparison)는 비어 있다.
- **아이디어**: 현재·과거 영상 쌍과 판독문으로 '변화'를 묻는 QA 벤치마크와, 이를 위한 시간 인식 VLM.
- **출발점 논문**: [BrainTRACE](https://neurips.cc/virtual/2026/poster/139162), [RealICU](https://neurips.cc/virtual/2026/poster/138984), [EHRNote-ChatQA](https://neurips.cc/virtual/2026/poster/139551)

### 8. 한국어·다국어 의료 면허 벤치마크

- **공백**: 일본 다직종 의료면허 VLM 벤치마크(JMed48k)가 채택됐다. 전체 9,094편 중 Korean을 언급한 논문은 3편이고, 그중 의료는 1편.
- **아이디어**: 한국 의사·간호·약사 국가시험의 이미지 포함 문항으로 VLM 벤치마크를 만들고, 언어 간 일관성(같은 문항을 한/영으로 물었을 때)을 평가. 문항 저작권 확인이 선결 과제.
- **출발점 논문**: [JMed48k](https://neurips.cc/virtual/2026/poster/139030), [Medmarks](https://neurips.cc/virtual/2026/poster/139434)

### 9. 과정 감독(process supervision) 기반 의료 추론 학습

- **공백**: RLVR/GRPO는 전체적으로 급증했지만 의료 100편 중 RLVR/GRPO 언급은 5편이고, 과정 보상(process reward)을 쓴 의료 논문은 0편(일반 RAG 쪽은 4편).
- **아이디어**: 증례 보고서·가이드라인에서 단계별 임상 판단을 추출해 process reward로 쓰는 의료 추론 RL. 정답만 맞고 추론이 틀린 경우를 걸러내는 것이 목표.
- **출발점 논문**: [CasePlay](https://neurips.cc/virtual/2026/poster/153097), [TraceDx](https://neurips.cc/virtual/2026/poster/149401), [Teach-to-Reason](https://neurips.cc/virtual/2026/poster/150121), [OpenMedReason](https://neurips.cc/virtual/2026/poster/139693), [CLR-voyance ](https://neurips.cc/virtual/2026/poster/150688)

### 10. 온프렘용 소형 의료 QA 모델 (agentic 능력 증류)

- **공백**: 병원 내부 배포는 데이터 반출이 어려워 소형 모델 수요가 크다. 2026년에 소형 의료 LM, 의료 VLM KV 압축, agentic 의료 추론 증류 논문이 따로따로 나왔지만, 이 목록 안에서 셋을 결합한 연구는 보이지 않는다.
- **아이디어**: 검색·툴 사용을 포함한 의료 에이전트 trajectory를 on-policy distillation으로 3–8B 모델에 옮기고, 성능·지연·개인정보 노출을 함께 평가.
- **출발점 논문**: [Med-Agentic](https://neurips.cc/virtual/2026/poster/153012), [MedPsy](https://neurips.cc/virtual/2026/poster/150557), [TACT-KV](https://neurips.cc/virtual/2026/poster/153041), [SD-Search](https://neurips.cc/virtual/2026/poster/155518)

### 11. 의료 지식베이스 오염(poisoning)·유출 방어

- **공백**: 일반 RAG에는 robustness-security 유형이 10편(poisoning·유출·프라이버시 포함) 있지만, 이 목록의 의료 논문 중 지식베이스 오염 공격·방어를 다룬 것은 없다.
- **아이디어**: 의료 지식그래프·가이드라인 코퍼스에 대한 표적 오염 공격과, 근거 수준·출처 신뢰도를 이용한 방어. 환자 기록 RAG의 멤버십 유출 측정 포함.
- **출발점 논문**: [When Poison Meets Structure](https://neurips.cc/virtual/2026/poster/152350), [Exposing Private Corpus Leakage in Multimodal RAG](https://neurips.cc/virtual/2026/poster/154898), [Privacy-Preserving Retrieval-Augmented Generation with Plausible Deniability](https://neurips.cc/virtual/2026/poster/150803), [Deceptive Grounding](https://neurips.cc/virtual/2026/poster/152927)

### 12. 약물·안전 중심 QA

- **공백**: 약리 안전성(SafeDrug), 정신건강 지원(MindGuard, TherapyGym) 벤치마크가 나왔다. 상호작용·용량 같은 고위험 질의에 특화된 학습 방법은 아직 적다.
- **아이디어**: 고위험 질의를 자동 탐지해 검색·검증 경로를 강화하는 risk-adaptive QA. 안전 벤치마크를 학습 보상으로 쓰는 방법.
- **출발점 논문**: [SafeDrug](https://neurips.cc/virtual/2026/poster/139719), [MindGuard](https://neurips.cc/virtual/2026/poster/138950), [TherapyGym](https://neurips.cc/virtual/2026/poster/139071)

## 하이라이트 (Oral · Spotlight)

발표 형식을 아는 7,688편 중 Oral 118편, Spotlight 287편, 합계 **405편(5.27%)**이 하이라이트다. 나머지 1,406편은 형식을 알 수 없어(Journal·Position 트랙 포함) 실제 하이라이트는 이보다 많을 수 있다. 전체 405편을 분야별로 정리한 목록은 [`HIGHLIGHTS.md`](HIGHLIGHTS.md)에 있다.

### 이 저장소 주제 안의 하이라이트 (4편)

| # | 제목 | 한 줄 요약 | 형식 |
|---:|---|---|---|
| 1 | [Incentivizing Medical Vision Capabilities from Large-Scale Multimodal Pre-training](https://neurips.cc/virtual/2026/poster/156128) | 6천만 쌍 의료 영상-텍스트 사전학습 후 RL로 의료 VLM 성능 도출 | Oral |
| 2 | [CRAFT: Causal Responsibility and Failure Tracing in Medical Vision Language Models](https://neurips.cc/virtual/2026/poster/149960) | 의료 VLM의 중재/제동 실패를 담당하는 attention head를 인과적으로 규명한 CRAFT | Spotlight |
| 3 | [City-RAG: Stepping Into a City via Spatially-Grounded Video Generation](https://neurips.cc/virtual/2026/poster/154638) | 지오 등록 데이터로 현실 도시를 근거로 한 비디오 생성 CityRAG | Spotlight |
| 4 | [Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction](https://neurips.cc/virtual/2026/poster/155649) | 임베딩 검색 대신 grep 등 터미널 도구로 코퍼스를 직접 탐색하는 에이전트 검색 DCI | Spotlight |

### 의료가 핵심 응용인 하이라이트 (5편, LLM 여부 무관)

초록을 읽고 골랐다. 의료 키워드가 걸리는 하이라이트는 12편이지만 7편은 의료를 예시로만 언급한다.

| # | 제목 | 한 줄 요약 | 형식 | 분야 |
|---:|---|---|---|---|
| 1 | [Incentivizing Medical Vision Capabilities from Large-Scale Multimodal Pre-training](https://neurips.cc/virtual/2026/poster/156128) | 6천만 쌍 의료 영상-텍스트 사전학습 후 RL로 의료 VLM 성능 도출 | Oral | 멀티모달·비전-언어 |
| 2 | [CRAFT: Causal Responsibility and Failure Tracing in Medical Vision Language Models](https://neurips.cc/virtual/2026/poster/149960) | 의료 VLM의 중재/제동 실패를 담당하는 attention head를 인과적으로 규명한 CRAFT | Spotlight | 정렬·안전·해석 |
| 3 | [STREAM: Stochastic Riemannian Flow Matching with Anisotropic Decoder for Digital Histopathology Image Generation](https://neurips.cc/virtual/2026/poster/149538) | 리만 flow matching으로 병리 조직 이미지 생성 STREAM | Spotlight | 생성 모델 (diffusion·flow·영상) |
| 4 | [Entropy Minimization without Model Collapse: Mitigating Prediction Bias in Medical Imaging](https://neurips.cc/virtual/2026/poster/149828) | 예측 편향을 줄여 엔트로피 최소화의 모델 붕괴를 막는 의료영상 TTA | Spotlight | 기타 ML (그래프·시계열·연합학습 등) |
| 5 | [What do EEG Foundation Models Capture from Human Brain Signals?](https://neurips.cc/virtual/2026/poster/150770) | EEG 파운데이션 모델이 포착하는 임상 특징 분석 | Spotlight | 과학·의료·생물 |

### 주제별 하이라이트 비율

- **빠르게 크는 주제의 하이라이트 비율은 약간 낮은 경향이 있지만 확정할 수준은 아니다.** 비중이 2배 이상 된 10개 주제를 묶으면 4.04%(841편 중 34편), 나머지는 5.42%(차이 검정 p ≈ 0.09). 주제별로는 tool use 2.63%, agent memory 2.33%, RAG 2.08%, RLVR 3.36%로 기준선 5.27%보다 낮지만, 표본이 작아 95% 구간이 대부분 기준선을 포함한다.
- **기준선보다 높은 쪽은 데이터 선별(10.0%), state space·linear attention(9.0%), 정형 수학·정리 증명(8.51%), 효율적 추론·overthinking(8.11%).** 다만 해당 하이라이트가 4–9편이라 우연 변동이 크다.
- **분야 단위로 보면 차이가 뚜렷하다.** 각 분야 논문 중 하이라이트 비율이 과학·생물 8.87%(95% 구간 6.8–11.5%), 학습 이론·최적화 7.99%(6.1–10.5%)로 기준선보다 높고, 의료·헬스케어는 1.94%(206편 중 4편, 0.8–4.9%)로 14개 분야 중 가장 낮다(`data/area_stats.json`).
- **의료 키워드(medical/clinical 등)가 나오는 논문의 하이라이트 비율은 3.36%(357편 중 12편)로 기준선보다 낮다.** 이 저장소의 의료 QA·RAG·에이전트 분류에서는 하이라이트가 0편이고, 의료 LLM/VLM에서 2편이 나왔다.

주제 정규식은 트렌드 분석과 같고, 발표 형식을 아는 논문이 40편 이상인 주제만 실었다. 기준선은 5.27%. 하이라이트 편수가 한 자릿수인 주제가 많아 비율 차이는 참고용이다.

| 주제 | 논문 수 | 하이라이트 | 비율 | 기준선 대비 |
|---|---:|---:|---:|---:|
| Data selection / curation | 60 | 6 | 10.0% | ×1.9 |
| State space / linear attention | 100 | 9 | 9.0% | ×1.71 |
| Formal math / theorem proving | 47 | 4 | 8.51% | ×1.62 |
| Overthinking / efficient reasoning | 74 | 6 | 8.11% | ×1.54 |
| 3D Gaussian splatting | 75 | 6 | 8.0% | ×1.52 |
| Differential privacy | 52 | 4 | 7.69% | ×1.46 |
| Diffusion language models | 94 | 6 | 6.38% | ×1.21 |
| Vision-language-action (VLA) / embodied | 220 | 14 | 6.36% | ×1.21 |
| In-context learning | 63 | 4 | 6.35% | ×1.21 |
| Interpretability / SAE | 177 | 11 | 6.21% | ×1.18 |
| Unified multimodal understanding+generation | 52 | 3 | 5.77% | ×1.1 |
| Time series foundation models | 193 | 11 | 5.7% | ×1.08 |
| Unlearning | 54 | 3 | 5.56% | ×1.05 |
| Test-time scaling / compute | 91 | 5 | 5.49% | ×1.04 |
| Video generation | 165 | 9 | 5.45% | ×1.04 |
| GRPO | 207 | 11 | 5.31% | ×1.01 |
| Reasoning models / long CoT | 225 | 12 | 5.33% | ×1.01 |
| Graph neural networks | 136 | 7 | 5.15% | ×0.98 |
| World models | 140 | 7 | 5.0% | ×0.95 |
| Synthetic data | 141 | 7 | 4.96% | ×0.94 |
| Steering / activation editing | 41 | 2 | 4.88% | ×0.93 |
| Benchmark / evaluation papers | 1327 | 65 | 4.9% | ×0.93 |
| Multimodal LLM (MLLM/VLM) | 640 | 31 | 4.84% | ×0.92 |
| Reward hacking / deception | 84 | 4 | 4.76% | ×0.9 |
| Flow matching | 190 | 9 | 4.74% | ×0.9 |
| Scientific discovery / AI scientist | 42 | 2 | 4.76% | ×0.9 |
| Protein / molecule | 212 | 10 | 4.72% | ×0.9 |
| LLM agents / agentic | 643 | 29 | 4.51% | ×0.86 |
| Jailbreak / red teaming | 66 | 3 | 4.55% | ×0.86 |
| Self-evolving / self-improving | 68 | 3 | 4.41% | ×0.84 |
| Knowledge distillation | 431 | 19 | 4.41% | ×0.84 |
| Deep research / search agents | 47 | 2 | 4.26% | ×0.81 |
| Causal inference | 387 | 16 | 4.13% | ×0.78 |
| Continual learning | 122 | 5 | 4.1% | ×0.78 |
| Uncertainty / calibration (LLM) | 320 | 12 | 3.75% | ×0.71 |
| Reward models / LLM-as-a-judge | 137 | 5 | 3.65% | ×0.69 |
| Multi-agent systems | 222 | 8 | 3.6% | ×0.68 |
| Reinforcement learning w/ verifiable rewards (RLVR) | 119 | 4 | 3.36% | ×0.64 |
| KV cache / long-context efficiency | 207 | 7 | 3.38% | ×0.64 |
| Medical / clinical | 357 | 12 | 3.36% | ×0.64 |
| Hallucination | 155 | 5 | 3.23% | ×0.61 |
| Software engineering agents | 71 | 2 | 2.82% | ×0.53 |
| Tool use / function calling | 114 | 3 | 2.63% | ×0.5 |
| Mixture of Experts | 115 | 3 | 2.61% | ×0.5 |
| Agent memory | 43 | 1 | 2.33% | ×0.44 |
| Quantization | 173 | 4 | 2.31% | ×0.44 |
| Federated learning | 89 | 2 | 2.25% | ×0.43 |
| Computer-use / GUI / web agents | 46 | 1 | 2.17% | ×0.41 |
| RAG | 96 | 2 | 2.08% | ×0.4 |
| Personalization | 83 | 0 | 0.0% | ×0.0 |

## 재현

```bash
bash scripts/fetch.sh            # neurips.cc에서 2025·2026 포스터 목록 다운로드 → data/raw/
python3 scripts/candidates.py    # 1차 키워드 후보 (1,103편)
python3 scripts/decisions.py     # Oral/Spotlight/Poster·트랙 병합 → data/decisions.json, papers.json 갱신
python3 scripts/topic_trends.py  # 주제별 비율 → data/topic_trends.json
python3 scripts/title_terms.py   # 제목 n-gram 증가 → data/title_terms.json
python3 scripts/highlights.py    # 하이라이트 목록·주제별 비율 → data/highlights.json, data/highlight_topics.json
python3 scripts/areas.py         # 14개 분야 비중·하이라이트 비율, 의료×LLM 주제 변화 → data/area_stats.json
python3 scripts/explorer.py      # explorer.html 생성 (전체 9,094편 태그 탐색)
python3 scripts/branchmap.py     # medical_qa.html, opsd.html 생성 (갈래 지도)
python3 scripts/build.py         # README.md, HIGHLIGHTS.md, interests.html 생성
```

LLM 분류 단계는 스크립트로 남기지 않았고, 그 결과가 `data/papers.json`의 `cats`, `rag_sub`, `summary_ko` 필드, `data/highlight_labels.json`(하이라이트의 분야·요약), `data/area_labels.json`(전체 논문의 분야)이다.

## 파일

| 파일 | 내용 |
|---|---|
| `data/papers.json` | 216편: 제목, 저자, 초록, NeurIPS 페이지 URL, OpenReview URL(있으면), 발표 형식, 트랙, 분류, 한 줄 요약 |
| `data/papers.csv` | 위와 같되 초록 제외 |
| `data/topic_trends.json` | 주제별 2025/2026 편수·비율·배수, 제목 단어 집계 |
| `data/title_terms.json` | 제목 n-gram 중 증가율 상위 |
| `HIGHLIGHTS.md` | NeurIPS 2026 전체 Oral·Spotlight 논문, 분야별 |
| `data/highlights.json` | 하이라이트 논문: 제목, 저자, URL, 형식, 트랙, 분야, 한 줄 요약, 이 저장소 분류(해당 시) |
| `data/highlight_topics.json` | 주제별·분류별 하이라이트 비율 |
| `data/decisions.json` | 포스터 id별 발표 형식·트랙·OpenReview URL (7,882편) |
| `data/dataset_track_stats.json` | Evaluations & Datasets 트랙과 Main 트랙의 의료 논문 수·비율, 해당 논문 id, 판정 규칙 |
| `data/medqa_benchmark_papers.json` | 의료 QA 벤치마크 본문 검색·판정 결과: 논문별 벤치마크, 모델, 학습 여부, 문제·방법, 검증된 성능 수치, 검색 범위 |
| `data/opd_papers.json` | on-policy·self-distillation 논문(유형, 설정, 한 줄 요약, 발표 형식), 연구 흐름, 집계 |
| `data/research_flows.json` | 관심 분야별 연구 흐름 한 줄 요약, 흐름별 어림 편수, 대표 논문(제목·URL) |
| `data/area_labels.json` | 2025·2026 전체 논문의 분야 코드(14개)와 배정 묶음 번호 |
| `data/area_stats.json` | 분야별 비중·변화·오차·하이라이트 비율, 의료×LLM 주제 변화, 트랙·형식 분포 |
| `medical_qa.html` / `opsd.html` | 주제별 연구 갈래 지도: 큰 갈래(무엇에서 무엇으로 옮겨가는지, 왜) → 세부 갈래 → 논문 ([Medical QA](https://chpark-ml.github.io/neurips2026-medical-llm-rag/medical_qa.html), [OPSD](https://chpark-ml.github.io/neurips2026-medical-llm-rag/opsd.html)) |
| `data/branch_medical_qa.json`, `data/branch_opsd.json`, `data/branch_med_datasets.json` | 갈래 지도 데이터: LLM이 초록을 전부 읽고 나눈 갈래·세부 갈래와 논문 배치 |
| `data/branch_med_datasets_papers.json` | 데이터셋 트랙 의료 논문 60편의 종류·데이터 설명·한 줄 요약 (데이터 설명의 숫자는 초록과 대조함) |
| `explorer.html` | 전체 9,094편 태그 탐색기: 분야 → 세부 주제, 키워드 주제, 발표 형식, 트랙으로 필터 ([열기](https://chpark-ml.github.io/neurips2026-medical-llm-rag/explorer.html)) |
| `data/subtopic_labels.json` | 분야별 세부 주제 212개와 논문별 세부 주제 1–2개 (LLM이 제목·초록 앞부분으로 배정, `scripts/subtopic_prompt.md`) |
| `interests.html` | 관심 분야 리포트: 학회 전체 → 분야 → 트렌드 → 의료·RAG 순서의 분석, 216편 목록, on-policy·self-distillation, 의료 QA 벤치마크 실험 논문, 하이라이트 405편, 연구 제안 ([열기](https://chpark-ml.github.io/neurips2026-medical-llm-rag/interests.html)) |
