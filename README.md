# NeurIPS 2026 — Medical QA · Medical RAG · Medical Agent · Medical LLM · RAG 논문 정리

NeurIPS 2026 채택 논문 **9,094편** 중, 아래 다섯 주제 중 하나 이상을 핵심 기여로 다룬 논문 **216편**을 모았다. 키워드 트렌드 분석(2025 대비)과 다음 연구 주제 제안, Medical QA 연구 아이디어를 함께 정리했다.

> 같은 내용을 검색·필터가 되는 페이지로 보려면 [`index.html`](index.html)을 브라우저로 열면 된다. NeurIPS 2026 전체의 Oral·Spotlight 논문은 [`HIGHLIGHTS.md`](HIGHLIGHTS.md)에 따로 정리했다.

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

**한계**: 분류는 사람 검수가 아닌 LLM 판독이라 경계 사례(예: 단백질 언어모델 + retrieval, 의료가 여러 응용 중 하나인 논문)는 기준에 따라 달라질 수 있다. 순수 검색·임베딩 논문(생성 없음)과 LLM이 없는 의료 영상·EHR 예측 모델은 의도적으로 제외했다. 한 줄 요약은 초록 기반 자동 요약이다.

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

### 요약

- **에이전트가 학회의 중심축이 됐다.** 초록에 agent/agentic이 나오는 논문 비율이 9.25% → 14.42% (2025 → 2026). 그 안에서도 tool use·function calling(×3.8), deep research·search agent(×3.5), SWE·coding agent(×3.1), MCP(1편 → 19편)가 가장 빠르게 늘었다.
- **RL 후처리는 'RLVR + on-policy'로 수렴 중.** RLVR/verifiable reward ×2.9, GRPO ×1.7. 제목 기준으로는 `RLVR` 1편 → 20편, `on-policy distillation` 0편 → 18편, `credit assignment` 5편 → 22편.
- **'근거(evidence)와 감사(audit)'가 새 키워드.** 제목에 `evidence`가 들어간 논문이 5편 → 90편, `audit/auditing` 4편 → 55편, `diagnosing/diagnostic` 6편 → 52편. 정답률보다 *왜 맞았는지·어디서 틀렸는지*를 보는 논문이 늘었다.
- **신뢰성 축이 두 배.** uncertainty/calibration ×2.1, reward hacking·deception·sycophancy ×2.1, activation steering ×2.0.
- **생성 모델은 flow matching(×1.9)·diffusion LM(×3.0)·world model(×1.7)로 이동.**
- **RAG는 정체, agentic search로 흡수 중.** 'RAG' 키워드 비율은 1.31% → 1.26%(×0.96)로 평탄하지만 deep research/search agent는 ×3.5. 이 저장소의 RAG 122편 중 31편이 agentic search 유형이다.
- **의료는 완만한 성장, Medical QA는 급증.** medical/clinical 언급 3.65% → 4.82%(×1.3), Medical QA 키워드 매칭은 6편 → 26편(×2.8).
- **하락 키워드.** in-context learning ×0.59, synthetic data ×0.64, (단어로서의) reasoning model/long CoT ×0.66, 3D Gaussian splatting ×0.68, differential privacy ×0.69, GNN ×0.72, federated learning ×0.73.

### 성장 상위 20개 주제

| 주제 | 2025 편수 (비율) | 2026 편수 (비율) | 배수 |
|---|---:|---:|---:|
| MCP (Model Context Protocol) | 1 (0.02%) | 19 (0.21%) | ×12.24 |
| Tool use / function calling | 24 (0.41%) | 141 (1.55%) | ×3.79 |
| Deep research / search agents | 10 (0.17%) | 55 (0.6%) | ×3.54 |
| Software engineering agents | 16 (0.27%) | 76 (0.84%) | ×3.06 |
| Diffusion language models | 23 (0.39%) | 108 (1.19%) | ×3.03 |
| Reinforcement learning w/ verifiable rewards (RLVR) | 31 (0.53%) | 141 (1.55%) | ×2.93 |
| Medical QA | 6 (0.1%) | 26 (0.29%) | ×2.79 |
| Uncertainty / calibration (LLM) | 210 (3.58%) | 694 (7.63%) | ×2.13 |
| Reward hacking / deception | 31 (0.53%) | 101 (1.11%) | ×2.1 |
| Steering / activation editing | 79 (1.35%) | 249 (2.74%) | ×2.03 |
| Flow matching | 79 (1.35%) | 231 (2.54%) | ×1.88 |
| World models | 65 (1.11%) | 174 (1.91%) | ×1.72 |
| GRPO | 90 (1.54%) | 237 (2.61%) | ×1.7 |
| Agent memory | 20 (0.34%) | 52 (0.57%) | ×1.68 |
| LLM agents / agentic | 542 (9.25%) | 1311 (14.42%) | ×1.56 |
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

- **근거**: uncertainty/calibration 키워드 ×2.1로 상위 성장. 단일 응답 calibration은 많지만 다단계 에이전트의 calibration(언제 멈추고 사람에게 넘길지)은 적다.
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

- **빠르게 크는 주제일수록 하이라이트 비율은 낮았다.** 전체 기준선 5.27%에 비해 tool use 2.63%(×0.50), agent memory 2.33%(×0.44), RAG 2.08%(×0.40), RLVR 3.36%(×0.64), activation steering 2.75%(×0.52). 논문이 몰리는 주제에서는 '같은 방향의 개선'만으로는 눈에 띄기 어렵다는 신호로 읽힌다(해석).
- **기준선보다 높은 쪽은 데이터 선별(10.0%, ×1.9), state space·linear attention(9.0%, ×1.71), 정형 수학·정리 증명(8.51%, ×1.62), 효율적 추론·overthinking(8.11%, ×1.54).** 다만 해당 하이라이트가 4–9편이라 우연 변동이 크다.
- **분야별로는 이론·최적화(60편)와 과학·의료·생물(46편)이 가장 많다.** Oral만 보면 이론·최적화 16편, 과학·의료·생물 14편, 정렬·안전·해석 12편 순.
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
| Benchmark / evaluation papers | 1327 | 65 | 4.9% | ×0.93 |
| Multimodal LLM (MLLM/VLM) | 640 | 31 | 4.84% | ×0.92 |
| Reward hacking / deception | 84 | 4 | 4.76% | ×0.9 |
| Flow matching | 190 | 9 | 4.74% | ×0.9 |
| Scientific discovery / AI scientist | 42 | 2 | 4.76% | ×0.9 |
| Protein / molecule | 212 | 10 | 4.72% | ×0.9 |
| Uncertainty / calibration (LLM) | 594 | 27 | 4.55% | ×0.86 |
| Jailbreak / red teaming | 66 | 3 | 4.55% | ×0.86 |
| Self-evolving / self-improving | 68 | 3 | 4.41% | ×0.84 |
| Knowledge distillation | 431 | 19 | 4.41% | ×0.84 |
| LLM agents / agentic | 1122 | 48 | 4.28% | ×0.81 |
| Deep research / search agents | 47 | 2 | 4.26% | ×0.81 |
| Causal inference | 387 | 16 | 4.13% | ×0.78 |
| Continual learning | 122 | 5 | 4.1% | ×0.78 |
| Reward models / LLM-as-a-judge | 137 | 5 | 3.65% | ×0.69 |
| Multi-agent systems | 222 | 8 | 3.6% | ×0.68 |
| Reinforcement learning w/ verifiable rewards (RLVR) | 119 | 4 | 3.36% | ×0.64 |
| KV cache / long-context efficiency | 207 | 7 | 3.38% | ×0.64 |
| Medical / clinical | 357 | 12 | 3.36% | ×0.64 |
| Hallucination | 155 | 5 | 3.23% | ×0.61 |
| Software engineering agents | 71 | 2 | 2.82% | ×0.53 |
| Steering / activation editing | 218 | 6 | 2.75% | ×0.52 |
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
python3 scripts/build.py         # README.md, HIGHLIGHTS.md, index.html 생성
```

LLM 분류 단계는 스크립트로 남기지 않았고, 그 결과가 `data/papers.json`의 `cats`, `rag_sub`, `summary_ko` 필드와 `data/highlight_labels.json`(하이라이트의 분야·요약)이다.

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
| `index.html` | 검색·필터가 되는 단일 HTML 페이지 |
