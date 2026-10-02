"""Hand-written analysis rendered into README.md and interests.html by build.py.

`papers` entries are title substrings; build.py resolves each to exactly one paper in
data/papers.json and fails if a substring matches zero or several papers.
`evidence` sentences quote numbers from data/topic_trends.json, data/title_terms.json
or data/papers.json — build.py does not recompute them, so update both together.
"""

TREND_NOTES = [
    "**LLM 에이전트가 가장 크게 커진 분야다.** 14개 분야 중 'LLM 에이전트·도구·검색'만 비중이 2.99% → 6.83%로 두 배 넘게 커졌다. 키워드로 보면 LLM 용어와 agent/agentic이 함께 나오는 논문이 4.64% → 8.46%(×1.82). 그 안에서도 tool use·function calling(×3.8), deep research·search agent(×3.5), SWE·coding agent(×3.1), MCP(1편 → 17편)가 가장 빠르게 늘었다.",
    "**RL 후처리는 'RLVR + on-policy'로 수렴 중.** RLVR/verifiable reward ×2.9, GRPO ×1.7. 제목 기준으로는 `RLVR` 1편 → 20편, `on-policy distillation` 0편 → 18편, `credit assignment` 5편 → 22편.",
    "**'근거(evidence)와 감사(audit)'가 새 키워드.** 제목에 `evidence`가 들어간 논문이 5편 → 90편, `audit/auditing` 4편 → 55편, `diagnosing/diagnostic` 6편 → 52편. 정답률보다 *왜 맞았는지·어디서 틀렸는지*를 보는 논문이 늘었다.",
    "**신뢰성 축이 두 배.** LLM 불확실성·calibration ×2.3(107 → 386편), reward hacking·deception·sycophancy ×2.1, activation steering ×3.0(10 → 47편).",
    "**생성 모델은 flow matching(×1.9)·diffusion LM(×3.0)·world model(×1.7)로 이동.**",
    "**RAG는 정체, agentic search로 흡수 중.** 'RAG' 키워드 비율은 1.31% → 1.26%(×0.96)로 평탄하지만 deep research/search agent는 ×3.5. 이 저장소의 RAG 122편 중 31편이 agentic search 유형이다.",
    "**의료는 완만한 성장, Medical QA는 급증.** 의료·헬스케어 분야 비중 2.22% → 2.79%, 의료 용어와 LLM 용어가 함께 나오는 논문 76편 → 170편(비중 ×1.44), Medical QA 키워드 매칭은 6편 → 26편(×2.8).",
    "**하락 키워드.** in-context learning ×0.59, synthetic data ×0.64, (단어로서의) reasoning model/long CoT ×0.66, 3D Gaussian splatting ×0.68, differential privacy ×0.69, GNN ×0.72, federated learning ×0.73.",
]

NEXT_TOPICS = [
    {
        "title": "Agentic search의 과정 보상·credit assignment",
        "why": "RAG 122편 중 31편이 agentic search이고, 그중 다수가 outcome reward의 한계를 다룬다. 제목의 `credit assignment`는 5편 → 22편. 아직 '어떤 검색 단계가 답에 기여했는가'를 정의하는 방식이 논문마다 제각각이라 표준이 없다.",
        "idea": "검색 trajectory의 각 query/문서에 기여도를 주는 보상(정보 이득, counterfactual 제거, 근거 포함 여부)을 비교·통합하는 연구. 효율(검색 횟수·토큰) 제약을 같이 거는 버전이 차별점.",
        "papers": ["RICE-PO", "PiCA", "Beyond Outcome Rewards: Process-Aware", "Beyond Outcome Rewards: Step-Level", "CARD: Internalizing", "Search More, Think Less"],
    },
    {
        "title": "근거 귀속(attribution)과 감사 가능한 생성",
        "why": "제목 `evidence` 5 → 90편, `audit/auditing` 4 → 55편. 생성 결과를 근거 단위로 검증하는 연구가 RAG·VLM·의료에서 동시에 나오고 있다.",
        "idea": "claim 단위로 '이 문장은 이 근거에서 왔다'를 모델 내부 신호(attention head)와 외부 검증기로 이중 확인하고, 불일치 시 abstain하는 파이프라인.",
        "papers": ["Reading Attribution from Attention", "TRIDENT", "Deceptive Grounding", "MedVIGIL", "Cite What You Explore"],
    },
    {
        "title": "On-policy distillation / self-distillation으로 에이전트 압축",
        "why": "제목 `on-policy distillation` 0 → 18편, `self-distillation` 6 → 26편. 큰 에이전트의 다단계 행동을 작은 모델로 옮기는 수요(온프렘·비용)가 크다.",
        "idea": "툴 호출·검색을 포함한 agentic trajectory를 on-policy로 증류하되, 교사와 학생의 행동 분포 차이(어디서 검색을 멈추는가)를 명시적으로 맞추는 방법.",
        "papers": ["SD-Search", "Beyond Outcome Rewards: Step-Level", "Med-Agentic", "MedPsy"],
    },
    {
        "title": "에이전트 메모리와 self-evolving skill",
        "why": "제목 `agent memory` 0 → 18편, `skill(s)` 9 → 56편, `self-evolving` 4 → 27편. 'RAG로 충분한가, 별도 메모리가 필요한가'를 정면으로 다루는 논문이 등장했다.",
        "idea": "경험을 skill/메모리로 축적할 때 오래된·충돌하는 기억을 어떻게 폐기·갱신하는지(망각 정책)에 대한 연구. 의료처럼 지식이 바뀌는 도메인에서 특히 비어 있다.",
        "papers": ["RAG in a Trenchcoat", "MedMemoryBench", "Experience Makes Skillful", "LongMINT"],
    },
    {
        "title": "에이전트의 불확실성·선택적 응답",
        "why": "LLM 불확실성·calibration 키워드가 ×2.3(107 → 386편)으로 상위 성장. 단일 응답 calibration은 많지만 다단계 에이전트의 calibration(언제 멈추고 사람에게 넘길지)은 적다.",
        "idea": "다회 tool use 에이전트에서 단계별 위험을 누적해 conformal 방식으로 '넘김(defer)' 시점을 보장하는 방법.",
        "papers": ["Calibrating Agentic LLMs", "Selective Answering for Medical VQA", "Learning When to Collaborate", "MoBayes"],
    },
    {
        "title": "현실 환경 기반 장기(long-horizon) 벤치마크",
        "why": "제목 `long-horizon` 7 → 77편. 객관식 벤치마크 대신 EHR·워크플로 환경에서 수십 단계 작업을 평가하는 벤치마크가 빠르게 늘었다.",
        "idea": "벤치마크 자체보다, 이런 환경에서 실패 원인을 자동 분류(diagnosing)하고 그 분류를 학습 신호로 되돌리는 연구가 다음 단계로 보인다.",
        "papers": ["$\\chi$-Bench", "PhysicianBench", "MedFlowBench", "REAL-MED"],
    },
]

MEDQA_IDEAS = [
    {
        "title": "의료 agentic search + 과정 보상 (Medical Search-R1 계열)",
        "gap": "일반 RAG 122편 중 agentic search 31편인데, 의료 100편 중 agentic search를 다룬 것은 사실상 1편(임상 증례 검색). 일반 쪽 과정 보상 기법이 의료로 거의 옮겨지지 않았다.",
        "idea": "PubMed·가이드라인·증례 코퍼스를 검색하는 의료 QA 에이전트를 RL로 학습. 보상은 정답 + 근거 문서의 임상적 핵심 사실(atomic fact) 포함 여부 + 검색 비용.",
        "papers": ["Incentivizing Agentic Retrieval", "TraceDx", "PiCA", "RICE-PO"],
    },
    {
        "title": "근거 귀속이 검증되는 임상 QA",
        "gap": "Deceptive Grounding은 임상 RAG가 정답을 내면서도 엉뚱한 환자·약물 entity에 근거를 붙이는 실패를 보고했다. 의료 RAG는 이 저장소 기준 5편뿐이다.",
        "idea": "답의 각 claim을 EHR·문헌의 특정 구간에 연결하고, entity 일치까지 검증하는 attribution 평가·학습. 최소 근거 집합만 남기는 방식과 결합.",
        "papers": ["Deceptive Grounding", "Cite What You Explore", "Less Evidence, Better Answering", "EHRNote-ChatQA"],
    },
    {
        "title": "오도·충돌·구식 정보에 대한 강건성",
        "gap": "MedMisBench가 오도 맥락 취약성을 측정했지만, 일반 RAG의 knowledge-conflict 해결 기법(디코딩·표현 수준)은 의료에 적용되지 않았다. 의료 언급 논문 728편 중 지식 갱신·시간적 drift를 다룬 것은 3편.",
        "idea": "가이드라인 개정 전후 문서가 섞인 검색 결과에서 최신·고근거 수준 정보를 따르게 하는 conflict-aware 의료 RAG와 벤치마크.",
        "papers": ["MedMisBench", "Conflict-Suppressed RAG", "Mitigating Knowledge Conflicts", "ReCon"],
    },
    {
        "title": "선택적 응답·위험 통제 abstention",
        "gap": "의료 100편 중 abstain/selective를 다룬 것은 4편. 대부분 단일 턴 VQA이고, 다회 진단 대화나 에이전트 단위의 위험 보장은 드물다.",
        "idea": "claim 검증 기반 selective answering을 다회 진단 대화로 확장하고, conformal risk control로 오답률 상한을 보장.",
        "papers": ["Selective Answering for Medical VQA", "Calibrating Agentic LLMs", "MoBayes", "Learning When to Collaborate"],
    },
    {
        "title": "정보 탐색형(문진형) 대화 QA",
        "gap": "MCQ 정답률은 포화에 가깝고, 2026년에는 '무엇을 물어볼지'를 학습하는 연구가 여러 편 나왔다. 다만 질문 비용·환자 부담을 보상에 넣은 연구는 드물다.",
        "idea": "가상 환자 시뮬레이터 위에서 질문/검사의 정보 가치(value of information)와 비용을 함께 최적화하는 RL. 시뮬레이터의 현실성 평가 프로토콜을 함께 제시.",
        "papers": ["MedExAgent", "ProbMedTOD", "CoE-Agent", "A Stratified Multi-Rater"],
    },
    {
        "title": "의료 VQA의 시각 근거 의존성 (영상을 실제로 보는가)",
        "gap": "의료 VLM이 영상을 무시하고 텍스트 사전지식으로 답하는 문제를 다룬 논문이 여러 편 나왔다(MedVIGIL, MedVIGOR, CRAFT, CXR attribution 등). 반면 ECG를 다룬 의료 논문은 1편, 안저(fundus)는 2편으로 모달리티 편중이 크다.",
        "idea": "영상 제거·교란 counterfactual로 '시각 필요도'를 측정하고 학습 데이터 선별·보상에 반영. CXR 외 ECG·안저·CT로 확장하면 공백을 메운다.",
        "papers": ["MedVIGIL", "MedVIGOR", "Rethinking Visual Attribution", "CRAFT", "ViCoR", "ECG-Reasoning-Benchmark"],
    },
    {
        "title": "종단(longitudinal)·다중 검사 비교 QA",
        "gap": "제목 `longitudinal`이 1편 → 17편. 의료에서는 BrainTRACE(종단 MRI), RealICU(장기 ICU)가 있지만, 이전 검사와 비교해 변화를 묻는 영상 QA(예: CXR prior comparison)는 비어 있다.",
        "idea": "현재·과거 영상 쌍과 판독문으로 '변화'를 묻는 QA 벤치마크와, 이를 위한 시간 인식 VLM.",
        "papers": ["BrainTRACE", "RealICU", "EHRNote-ChatQA"],
    },
    {
        "title": "한국어·다국어 의료 면허 벤치마크",
        "gap": "일본 다직종 의료면허 VLM 벤치마크(JMed48k)가 채택됐다. 전체 9,094편 중 Korean을 언급한 논문은 3편이고, 그중 의료는 1편.",
        "idea": "한국 의사·간호·약사 국가시험의 이미지 포함 문항으로 VLM 벤치마크를 만들고, 언어 간 일관성(같은 문항을 한/영으로 물었을 때)을 평가. 문항 저작권 확인이 선결 과제.",
        "papers": ["JMed48k", "Medmarks"],
    },
    {
        "title": "과정 감독(process supervision) 기반 의료 추론 학습",
        "gap": "RLVR/GRPO는 전체적으로 급증했지만 의료 100편 중 RLVR/GRPO 언급은 5편이고, 과정 보상(process reward)을 쓴 의료 논문은 0편(일반 RAG 쪽은 4편).",
        "idea": "증례 보고서·가이드라인에서 단계별 임상 판단을 추출해 process reward로 쓰는 의료 추론 RL. 정답만 맞고 추론이 틀린 경우를 걸러내는 것이 목표.",
        "papers": ["CasePlay", "TraceDx", "Teach-to-Reason", "OpenMedReason", "CLR-voyance"],
    },
    {
        "title": "온프렘용 소형 의료 QA 모델 (agentic 능력 증류)",
        "gap": "병원 내부 배포는 데이터 반출이 어려워 소형 모델 수요가 크다. 2026년에 소형 의료 LM, 의료 VLM KV 압축, agentic 의료 추론 증류 논문이 따로따로 나왔지만, 이 목록 안에서 셋을 결합한 연구는 보이지 않는다.",
        "idea": "검색·툴 사용을 포함한 의료 에이전트 trajectory를 on-policy distillation으로 3–8B 모델에 옮기고, 성능·지연·개인정보 노출을 함께 평가.",
        "papers": ["Med-Agentic", "MedPsy", "TACT-KV", "SD-Search"],
    },
    {
        "title": "의료 지식베이스 오염(poisoning)·유출 방어",
        "gap": "일반 RAG에는 robustness-security 유형이 10편(poisoning·유출·프라이버시 포함) 있지만, 이 목록의 의료 논문 중 지식베이스 오염 공격·방어를 다룬 것은 없다.",
        "idea": "의료 지식그래프·가이드라인 코퍼스에 대한 표적 오염 공격과, 근거 수준·출처 신뢰도를 이용한 방어. 환자 기록 RAG의 멤버십 유출 측정 포함.",
        "papers": ["When Poison Meets Structure", "Exposing Private Corpus Leakage", "Privacy-Preserving Retrieval-Augmented", "Deceptive Grounding"],
    },
    {
        "title": "약물·안전 중심 QA",
        "gap": "약리 안전성(SafeDrug), 정신건강 지원(MindGuard, TherapyGym) 벤치마크가 나왔다. 상호작용·용량 같은 고위험 질의에 특화된 학습 방법은 아직 적다.",
        "idea": "고위험 질의를 자동 탐지해 검색·검증 경로를 강화하는 risk-adaptive QA. 안전 벤치마크를 학습 보상으로 쓰는 방법.",
        "papers": ["SafeDrug", "MindGuard", "TherapyGym"],
    },
]

# Highlights (Oral + Spotlight). Numbers come from data/highlight_topics.json.
HIGHLIGHT_NOTES = [
    "**빠르게 크는 주제의 하이라이트 비율은 약간 낮은 경향이 있지만 확정할 수준은 아니다.** 비중이 2배 이상 된 10개 주제를 묶으면 4.04%(841편 중 34편), 나머지는 5.42%(차이 검정 p ≈ 0.09). 주제별로는 tool use 2.63%, agent memory 2.33%, RAG 2.08%, RLVR 3.36%로 기준선 5.27%보다 낮지만, 표본이 작아 95% 구간이 대부분 기준선을 포함한다.",
    "**기준선보다 높은 쪽은 데이터 선별(10.0%), state space·linear attention(9.0%), 정형 수학·정리 증명(8.51%), 효율적 추론·overthinking(8.11%).** 다만 해당 하이라이트가 4–9편이라 우연 변동이 크다.",
    "**분야 단위로 보면 차이가 뚜렷하다.** 각 분야 논문 중 하이라이트 비율이 과학·생물 8.87%(95% 구간 6.8–11.5%), 학습 이론·최적화 7.99%(6.1–10.5%)로 기준선보다 높고, 의료·헬스케어는 1.94%(206편 중 4편, 0.8–4.9%)로 14개 분야 중 가장 낮다(`data/area_stats.json`).",
    "**의료 키워드(medical/clinical 등)가 나오는 논문의 하이라이트 비율은 3.36%(357편 중 12편)로 기준선보다 낮다.** 이 저장소의 의료 QA·RAG·에이전트 분류에서는 하이라이트가 0편이고, 의료 LLM/VLM에서 2편이 나왔다.",
]

# Highlights whose core application is medicine, picked by reading the abstracts
# (the keyword match finds 12, but 7 only mention healthcare as an example).
MED_HIGHLIGHTS = [
    "Incentivizing Medical Vision Capabilities",
    "CRAFT: Causal Responsibility",
    "STREAM: Stochastic Riemannian Flow Matching",
    "Entropy Minimization without Model Collapse",
    "What do EEG Foundation Models Capture",
]
