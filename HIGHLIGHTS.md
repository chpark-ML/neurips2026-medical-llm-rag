# NeurIPS 2026 하이라이트 (Oral · Spotlight) 논문

발표 형식을 아는 7,688편 중 Oral 118편, Spotlight 287편, 합계 **405편**. 1,406편은 neurips.cc 데이터에 형식이 없어 빠졌으므로 실제 하이라이트는 더 많을 수 있다. 분야와 한 줄 요약은 초록을 읽고 LLM이 붙였다. 의료·RAG 관점의 해석은 [REPORT](REPORT.md#하이라이트-oral--spotlight)에 있다.

| 분야 | Oral | Spotlight | 합계 |
|---|---:|---:|---:|
| [학습 이론·최적화](#학습-이론최적화) | 16 | 44 | 60 |
| [과학·의료·생물](#과학의료생물) | 14 | 32 | 46 |
| [컴퓨터 비전·3D](#컴퓨터-비전3d) | 11 | 28 | 39 |
| [정렬·안전·해석](#정렬안전해석) | 12 | 25 | 37 |
| [기타 ML (그래프·시계열·연합학습 등)](#기타-ml-그래프시계열연합학습-등) | 7 | 29 | 36 |
| [생성 모델 (diffusion·flow·영상)](#생성-모델-diffusionflow영상) | 5 | 29 | 34 |
| [멀티모달·비전-언어](#멀티모달비전-언어) | 9 | 21 | 30 |
| [강화학습·로보틱스·embodied](#강화학습로보틱스embodied) | 11 | 14 | 25 |
| [데이터셋·벤치마크·평가](#데이터셋벤치마크평가) | 10 | 14 | 24 |
| [확률·인과·통계 ML](#확률인과통계-ml) | 5 | 17 | 22 |
| [LLM 에이전트·도구 사용](#llm-에이전트도구-사용) | 10 | 11 | 21 |
| [효율 모델·시스템](#효율-모델시스템) | 5 | 14 | 19 |
| [LLM 추론·RL 후처리](#llm-추론rl-후처리) | 3 | 9 | 12 |

## 학습 이론·최적화

| # | 제목 | 한 줄 요약 | 형식 |
|---:|---|---|---|
| 1 | [Do We Need Asynchronous SGD? On the Near-Optimality of Synchronous Methods](https://neurips.cc/virtual/2026/poster/155336) | 동기식 SGD가 이질적 환경에서 거의 최적임을 증명 | Oral |
| 2 | [FLIP: Fast and Accurate Global Lipschitz Estimation for Large Feedforward Networks](https://neurips.cc/virtual/2026/poster/152411) | 대형 피드포워드 망의 전역 Lipschitz 상수를 빠르게 추정하는 FLIP | Oral |
| 3 | [Follow the Regularized Leader Does Not Converge in Constrained Optimization](https://neurips.cc/virtual/2026/poster/150986) | 제약 최적화에서 FTRL이 수렴하지 않을 수 있음을 증명 | Oral |
| 4 | [Free Decompression with Algebraic Spectral Curves](https://neurips.cc/virtual/2026/poster/155558) | 대수적 스펙트럼 곡선으로 행렬 크기 간 스펙트럼을 외삽하는 free decompression | Oral |
| 5 | [From Average Sensitivity to Small-Loss Regret Bounds under Random-Order Model](https://neurips.cc/virtual/2026/poster/154659) | random-order 모델에서 average sensitivity로부터 small-loss regret bound 도출 | Oral |
| 6 | [Learning Reveals Invisible Structure in Low-Rank RNNs](https://neurips.cc/virtual/2026/poster/152289) | 저랭크 RNN 학습 동역학을 loss-visible/invisible overlap으로 이론 분석 | Oral |
| 7 | [MaxSketch: Robust Distinct Counting in Streams via Random Projections](https://neurips.cc/virtual/2026/poster/155987) | 랜덤 프로젝션 기반 강건한 스트림 distinct counting MaxSketch | Oral |
| 8 | [Prediction Under Imperfect Compression: A Theory of Approximate MDL](https://neurips.cc/virtual/2026/poster/150363) | 근사 MDL 하에서도 순차 예측이 신뢰 가능한 조건의 이론 | Oral |
| 9 | [Query Lower Bounds for Diffusion Sampling](https://neurips.cc/virtual/2026/poster/151581) | 확산 모델 샘플링의 score query 하한 Ω(√d) 증명 | Oral |
| 10 | [Reference-Guided Training: Adaptive Gradient Scaling via Per-Sample Loss Comparisons](https://neurips.cc/virtual/2026/poster/148399) | 참조 모델과의 샘플별 손실 비교로 gradient를 적응적으로 스케일링 | Oral |
| 11 | [Scale-Sensitive Shattering: Learnability and Evaluability at Optimal Scale](https://neurips.cc/virtual/2026/poster/149340) | fat-shattering 기반 최적 스케일 학습가능성과 uniform convergence | Oral |
| 12 | [Surprises in Proper Positive-Only Learning](https://neurips.cc/virtual/2026/poster/148778) | positive-only 학습에서 proper 학습의 특성화와 분리 결과 | Oral |
| 13 | [The Power of a Random Sample in Online Algorithms](https://neurips.cc/virtual/2026/poster/152757) | 랜덤 샘플을 활용하는 온라인 알고리즘 ORS 모델과 secretary 문제 | Oral |
| 14 | [The Sign Code: The Hidden Binary Nature of Deep Networks](https://neurips.cc/virtual/2026/poster/155585) | 심층 네트워크의 sign code가 분류를 좌우함을 분석 | Oral |
| 15 | [The Stability of Online Algorithms in Performative Prediction](https://neurips.cc/virtual/2026/poster/151725) | performative prediction에서 no-regret 알고리즘의 안정 수렴 | Oral |
| 16 | [Uniform-in-Time Weak Propagation of Chaos in Shallow Neural Networks](https://neurips.cc/virtual/2026/poster/154794) | 얕은 신경망의 uniform-in-time weak propagation of chaos | Oral |
| 17 | [(Strongly) Replicable Distribution Testers imply High Probability Distribution Testers](https://neurips.cc/virtual/2026/poster/150921) | replicable 분포 검정기가 고확률 검정기를 함의함을 증명 | Spotlight |
| 18 | [A Solvable Model of Chain-of-Thought in In-Context Learning](https://neurips.cc/virtual/2026/poster/154777) | ICL에서 CoT 깊이에 따른 일반화를 정확히 풀어낸 이론 모델 | Spotlight |
| 19 | [AMUSE: Anytime Muon with Stable Gradient Evaluation](https://neurips.cc/virtual/2026/poster/152756) | Muon과 Schedule-Free 평균화를 결합한 스케줄 불필요 옵티마이저 AMUSE | Spotlight |
| 20 | [Behavior Cloning is Not All You Need: The Optimality of On-Policy Distillation for Noisy Expert Feedback](https://neurips.cc/virtual/2026/poster/150673) | 노이즈 있는 전문가에서 on-policy distillation이 BC보다 우월함을 증명 | Spotlight |
| 21 | [Consistent Geometric Deep Learning via Hilbert Bundles and Cellular Sheaves](https://neurips.cc/virtual/2026/poster/153249) | Hilbert bundle과 cellular sheaf 기반 무한차원 신호용 기하 딥러닝 일관성 이론 | Spotlight |
| 22 | [Decomposing and Reshaping Scaling Laws through Token Learning Times](https://neurips.cc/virtual/2026/poster/152417) | 토큰 학습 시간 분포로 스케일링 법칙을 분해하고 재구성 | Spotlight |
| 23 | [Diagonalizing the Softmax: Hadamard Initialization for Tractable Cross-Entropy Dynamics](https://neurips.cc/virtual/2026/poster/152327) | Hadamard 초기화로 cross-entropy 동역학을 풀어낸 neural collapse 이론 | Spotlight |
| 24 | [Fast and slow gradient descent dynamics of logistic regression through weak alignment](https://neurips.cc/virtual/2026/poster/152237) | 로지스틱 회귀 경사하강법의 max-margin 약한 정렬 속도 이론 | Spotlight |
| 25 | [Fast Rates for Offline Contextual Bandits with Forward-KL Regularization under Single-Policy Concentrability](https://neurips.cc/virtual/2026/poster/149055) | forward-KL 정규화 오프라인 컨텍스추얼 밴딧의 fast rate 증명 | Spotlight |
| 26 | [First-Token Attraction in Mamba Dynamics](https://neurips.cc/virtual/2026/poster/149171) | Mamba 동역학에서 첫 토큰이 후속 토큰을 끌어당기는 현상 이론 분석 | Spotlight |
| 27 | [Foundations of Categorical Equivariant Deep Learning](https://neurips.cc/virtual/2026/poster/150485) | 군에서 변환 범주로 확장한 범주적 등변 딥러닝 기초 이론 | Spotlight |
| 28 | [Free Heavy-Tailed Lunch for Muon: A Theoretical Justification of Empirical Success](https://neurips.cc/virtual/2026/poster/155600) | Muon 등 비유클리드 옵티마이저의 heavy-tailed 잡음 하 최적 샘플 복잡도 이론 분석 | Spotlight |
| 29 | [How Can SignSGD Outperform SGD? A Functional Scaling Law Perspective](https://neurips.cc/virtual/2026/poster/150706) | functional scaling law로 signSGD가 SGD를 능가하는 조건 분석 | Spotlight |
| 30 | [Improved Leverage Score Sampling for Constrained Active Linear Regression](https://neurips.cc/virtual/2026/poster/155618) | 제약 능동 선형회귀를 위한 ellipsoid 정규화 leverage score 샘플링 | Spotlight |
| 31 | [Improved Regret Analysis For Parallel Gaussian Process Bandit Optimization](https://neurips.cc/virtual/2026/poster/153555) | 병렬 GP bandit 최적화의 batch 크기 의존 없는 개선 regret 분석 | Spotlight |
| 32 | [Is Dimensionality a Barrier for Retrieval Models?](https://neurips.cc/virtual/2026/poster/148654) | 임베딩 차원이 검색 모델의 장벽이 아닌 이유를 margin 이론으로 규명 | Spotlight |
| 33 | [Large language models suffer from a curse of ambiguity](https://neurips.cc/virtual/2026/poster/150511) | 다음 토큰 분포가 모호할수록 학습이 어려운 'ambiguity의 저주' 이론 분석 | Spotlight |
| 34 | [Learning to Price with Persuasion](https://neurips.cc/virtual/2026/poster/154117) | 정보 설계와 메커니즘 설계를 결합한 설득 기반 가격 책정의 학습 이론 | Spotlight |
| 35 | [Mildly Overparameterized ReLU Networks on Orthogonal Data: Incremental Learning and Implicit Bias](https://neurips.cc/virtual/2026/poster/149598) | 직교 데이터에서 ReLU 망의 incremental learning과 implicit bias 증명 | Spotlight |
| 36 | [Nearly Optimal Fixed-Confidence Best-Arm Identification with 1-Bit Feedback](https://neurips.cc/virtual/2026/poster/155304) | 1-bit 피드백 하 고정 신뢰도 best-arm identification의 준최적 알고리즘 | Spotlight |
| 37 | [On the Complexity of Discounted Robust MDPs with L_p Uncertainty Sets](https://neurips.cc/virtual/2026/poster/149658) | L_p 불확실성 집합 robust MDP의 정책 반복 복잡도와 하한 분석 | Spotlight |
| 38 | [On the Depth of Monotone ReLU Neural Networks and ICNNs](https://neurips.cc/virtual/2026/poster/152162) | 단조 ReLU 망과 ICNN의 표현에 필요한 깊이 하한 증명 | Spotlight |
| 39 | [On the Nonlinearity of Learning Rate Scaling for LLM Training](https://neurips.cc/virtual/2026/poster/155689) | LLM 학습률 스케일링의 비선형성과 effective learning rate 분석 | Spotlight |
| 40 | [Optimal Rates for Adaptive Private k-PCA](https://neurips.cc/virtual/2026/poster/152628) | 적응적 차분 프라이버시 k-PCA의 최적 샘플 복잡도 알고리즘 | Spotlight |
| 41 | [Optimal Rates for Pure \varepsilon-Differentially Private Stochastic Convex Optimization with Heavy Tails](https://neurips.cc/virtual/2026/poster/148362) | heavy-tail 기울기 하 pure DP 볼록 최적화의 최적 rate 규명 | Spotlight |
| 42 | [Optimal Recalibration of an Online Predictor](https://neurips.cc/virtual/2026/poster/153807) | 온라인 예측기 재보정의 최적 rate 알고리즘과 하한 | Spotlight |
| 43 | [Point-to-Manifold Geometry: Flexibly Overcoming the Curse of Dimensionality in Neural Computational Units](https://neurips.cc/virtual/2026/poster/152082) | point-to-manifold 거리를 쓰는 Generative Matching Unit의 표현력 이론 | Spotlight |
| 44 | [Polynomial-Time Algorithm for Thiele Voting Rules with Voter Interval Preferences](https://neurips.cc/virtual/2026/poster/148977) | voter interval 선호에서 Thiele 투표 규칙의 다항시간 알고리즘 | Spotlight |
| 45 | [Polynomial-Time Robust Multiclass Linear Classification under Gaussian Marginals](https://neurips.cc/virtual/2026/poster/153425) | 가우시안 하 다중클래스 선형 분류기의 다항시간 강건 학습 | Spotlight |
| 46 | [Proper Agnostic Learning of Functions of Halfspaces](https://neurips.cc/virtual/2026/poster/151228) | 반공간 함수 클래스의 proper agnostic 학습 효율 알고리즘 | Spotlight |
| 47 | [Recursively Trained Diffusion Models: Limiting Collapse Distribution and Spectral Characterization](https://neurips.cc/virtual/2026/poster/152379) | 재귀 학습된 확산 모델의 극한 분포와 스펙트럼 특성 이론 | Spotlight |
| 48 | [Regret–Oracle Complexity Tradeoffs in Agnostic Online Learning](https://neurips.cc/virtual/2026/poster/148781) | agnostic 온라인 학습의 regret–oracle complexity trade-off | Spotlight |
| 49 | [Requential Coding: Measuring Model Compressibility by Coding Data Instead of Parameters](https://neurips.cc/virtual/2026/poster/150681) | 데이터를 코딩해 모델 압축성을 재는 requential coding과 PAC-Bayes 일반화 bound | Spotlight |
| 50 | [Selectivity Makes State-Space Models Universal Sequence Approximators](https://neurips.cc/virtual/2026/poster/150042) | 선택적 SSM(Mamba)이 보편 시퀀스 근사기임을 증명 | Spotlight |
| 51 | [SOC-ICNN: From Polyhedral to Conic Geometry for Learning Convex Surrogate Functions](https://neurips.cc/virtual/2026/poster/150828) | SOCP 기반으로 표현력을 확장한 input convex neural network | Spotlight |
| 52 | [Sparse Updates Generalize Better Than Optimization: Stability Analysis for Randomized Subspace Descent](https://neurips.cc/virtual/2026/poster/148588) | randomized subspace descent의 안정성 기반 일반화 분석 | Spotlight |
| 53 | [Testable Learning of General Halfspaces under Massart Noise](https://neurips.cc/virtual/2026/poster/153845) | Massart 잡음 하 일반 halfspace의 testable learning 알고리즘 | Spotlight |
| 54 | [The Long-Run Distribution of Regularized Learning in Non-Concave Games: A Large Deviations Approach](https://neurips.cc/virtual/2026/poster/154101) | 비볼록 게임에서 정규화 학습의 장기 분포 large deviations 분석 | Spotlight |
| 55 | [The Multiscale Single-Index Model: A Toy Model for Hierarchical Feature Learning](https://neurips.cc/virtual/2026/poster/152129) | 계층적 특징 학습의 장난감 모델 Multiscale Single-Index Model | Spotlight |
| 56 | [The Symmetries of Three-Layer ReLU Networks](https://neurips.cc/virtual/2026/poster/150294) | 3층 ReLU 네트워크의 파라미터 대칭성 완전 특성화 | Spotlight |
| 57 | [Toward Minimal-dimensional Convex Calibrated Surrogate Losses for Classification with Rejection](https://neurips.cc/virtual/2026/poster/150329) | 거절 옵션 분류의 최소 차원 convex calibrated surrogate loss | Spotlight |
| 58 | [Two Speeds of Learning: A Representation-Readout Decomposition of Grokking and Double Descent](https://neurips.cc/virtual/2026/poster/153791) | grokking과 double descent의 representation-readout 분해 | Spotlight |
| 59 | [Understanding Sample Efficiency in Predictive Coding](https://neurips.cc/virtual/2026/poster/155323) | predictive coding의 sample efficiency를 target alignment로 분석 | Spotlight |
| 60 | [𝑓-Differential Privacy Filters: Validity and Approximate Solutions](https://neurips.cc/virtual/2026/poster/156133) | f-DP 필터의 유효성 조건과 근사 해법 분석 | Spotlight |

## 과학·의료·생물

| # | 제목 | 한 줄 요약 | 형식 |
|---:|---|---|---|
| 1 | [A multi-scale information geometry reveals the structure of mutual information in neural populations](https://neurips.cc/virtual/2026/poster/154781) | 신경 집단 코드의 상호정보량을 드러내는 다중 스케일 정보 기하 | Oral |
| 2 | [BrainWorld: A Structural-Prior-Conditioned Generative Model for Whole-Brain 4D fMRI Dynamics](https://neurips.cc/virtual/2026/poster/155412) | 구조 MRI를 조건으로 전뇌 4D fMRI 동역학을 생성하는 BrainWorld | Oral |
| 3 | [Breakeven complexity: A new perspective on neural partial differential equation solvers](https://neurips.cc/virtual/2026/poster/148644) | 신경 PDE 솔버의 end-to-end 비용을 따지는 breakeven complexity 지표 | Oral |
| 4 | [C3P: Contrastive promoter-protein pretraining yields representations capturing bacterial gene regulation](https://neurips.cc/virtual/2026/poster/156046) | 프로모터-단백질 대조 사전학습으로 박테리아 유전자 조절 표현 학습 | Oral |
| 5 | [CausalBind: Causal Modeling and Learning for Protein-Molecule Virtual Screening](https://neurips.cc/virtual/2026/poster/151296) | 희소 상호작용 인과 모델로 단백질-분자 가상 스크리닝 일반화 향상 | Oral |
| 6 | [Compact SO(3) Equivariant Atomistic Foundation Models via Structural Pruning](https://neurips.cc/virtual/2026/poster/154865) | 구조적 가지치기로 SO(3) 등변 원자 파운데이션 모델을 경량화 | Oral |
| 7 | [Decomposing Earth Embeddings with Sparse Autoencoders](https://neurips.cc/virtual/2026/poster/150168) | 희소 오토인코더로 지구 관측 임베딩을 해석 가능한 특징으로 분해 | Oral |
| 8 | [DIAGNO: Diagonal Spherical Neural Operators for Heterogeneous Earth Dynamics Modeling](https://neurips.cc/virtual/2026/poster/154008) | 구면 스펙트럼 대각 상호작용으로 지구 동역학을 예측하는 DIAGNO | Oral |
| 9 | [Learning Sparse Semantic-Cortical Atoms for Multisubject Naturalistic fMRI Encoding](https://neurips.cc/virtual/2026/poster/151712) | 다중 피험자 fMRI 인코딩을 위한 sparse semantic-cortical atom 학습 | Oral |
| 10 | [Mechanism-Aware Ensemble Conditioning for Data-Limited Emulation of Extreme Events](https://neurips.cc/virtual/2026/poster/151389) | 앙상블 기하 조건화로 데이터 부족 하 극단 사건 에뮬레이션 개선 | Oral |
| 11 | [MindAlign: Bridging EEG, Vision, and Language for Zero-Shot Visual Decoding](https://neurips.cc/virtual/2026/poster/149255) | EEG-이미지-텍스트 대조 정렬로 zero-shot 시각 디코딩 수행 | Oral |
| 12 | [Neural population tuning statistics as priors for multitask generalization](https://neurips.cc/virtual/2026/poster/153194) | 신경 집단 tuning 통계를 다중 과제 일반화의 prior로 연결하는 이론 | Oral |
| 13 | [Polar Transformers: SO(2)^K-Equivariant Angular Attention for Cryo-EM Image-Set Processing](https://neurips.cc/virtual/2026/poster/156031) | SO(2)^K 등변 각도 어텐션으로 cryo-EM 이미지 집합 처리 | Oral |
| 14 | [Unlocking Volition: Proactive Intention Decoding via Interpretable Graph Learning of Multi-Region ECoG](https://neurips.cc/virtual/2026/poster/153824) | 해석 가능한 그래프 학습으로 다영역 ECoG 의도 사전 디코딩 | Oral |
| 15 | [A meshfree exterior calculus for generalizable and data-efficient learning of physics from point clouds](https://neurips.cc/virtual/2026/poster/154490) | 포인트 클라우드 물리 학습을 위한 meshfree exterior calculus와 MEEC-Net | Spotlight |
| 16 | [Binding Mode Matters: Hotspot-Aware Drug Discovery via Explorative Preferences](https://neurips.cc/virtual/2026/poster/153924) | 핫스팟 인식 다목적 RL로 다양한 결합 모드의 분자를 설계하는 BindMol | Spotlight |
| 17 | [Colour me shocked: Exact Molecular Hessians from MLIPs in O(N) time using sparse differentiation!](https://neurips.cc/virtual/2026/poster/151062) | 희소 자동미분으로 MLIP의 정확한 Hessian을 O(N)에 계산 | Spotlight |
| 18 | [CrystalREPA: Transferring Physical Priors from Universal MLIPs to Crystal Generative Models](https://neurips.cc/virtual/2026/poster/154603) | 범용 MLIP의 물리 사전지식을 결정 생성 모델에 전이하는 CrystalREPA | Spotlight |
| 19 | [Deep Generative Models for Phylogenetic Inference with Complex Evolutionary Processes](https://neurips.cc/virtual/2026/poster/151547) | 이산 확산 모델로 복잡한 진화 과정의 계통수를 추론하는 생성 모델 | Spotlight |
| 20 | [Fast Reconstruction of Exact Maxwell Dynamics from Sparse Data](https://neurips.cc/virtual/2026/poster/148197) | 맥스웰 방정식의 정확해 뉴런으로 희소 데이터에서 전자기장 복원 | Spotlight |
| 21 | [FETTUCCINE: Fast and efficient brain-to-text decoding on mobile devices](https://neurips.cc/virtual/2026/poster/150728) | 모바일 기기에서 동작하는 빠른 뇌-텍스트 디코딩 FETTUCCINE | Spotlight |
| 22 | [Few-Step Cofolding with All-Atom Flow Maps](https://neurips.cc/virtual/2026/poster/151026) | all-atom flow map 증류로 단백질 cofolding을 few-step으로 수행 | Spotlight |
| 23 | [Fluxtrapolation: A benchmark on extrapolating ecosystem fluxes](https://neurips.cc/virtual/2026/poster/139401) | 생태계 플럭스 외삽을 위한 분포 이동 벤치마크 FLUXtrapolation | Spotlight |
| 24 | [Generating Physically Consistent Molecules with Energy-Based Models](https://neurips.cc/virtual/2026/poster/152559) | 에너지 기반 모델 EBMol로 물리적으로 일관된 3D 분자 생성 | Spotlight |
| 25 | [GeoWind2Plan: Mission-Time 3D Urban Wind Prediction for Energy-Efficient UAV Planning](https://neurips.cc/virtual/2026/poster/149346) | 도시 3D 바람 예측과 에너지 효율적 UAV 경로 계획 프레임워크 | Spotlight |
| 26 | [GOLD: Geometric Optimized Latent Diffusion for Structure-Aware RNA Inverse Folding](https://neurips.cc/virtual/2026/poster/153434) | RNA 역접힘을 위한 구조 인식 잠재 확산 모델 GOLD | Spotlight |
| 27 | [Learned Lagrangian Models of PDEs via Euler–Lagrange Residual Minimization](https://neurips.cc/virtual/2026/poster/151132) | Euler-Lagrange 잔차 최소화로 학습된 Lagrangian으로 PDE 예측 | Spotlight |
| 28 | [Learning Discrete Riemannian Metrics for Physical Fields with Cochain-Frame Equivariance](https://neurips.cc/virtual/2026/poster/150499) | 위상과 기하를 분리한 Riemannian Hodge message passing 물리장 서로게이트 | Spotlight |
| 29 | [Measuring Robustness and Efficiency in a Connectome-Constrained Fly Visual System Model on a Collision-Detection Task](https://neurips.cc/virtual/2026/poster/149010) | 커넥톰 제약 초파리 시각 모델의 강건성과 효율성을 충돌 감지로 평가 | Spotlight |
| 30 | [MechParser: A Vision-Language Framework for Parsing Chemical Reaction Mechanism Diagrams](https://neurips.cc/virtual/2026/poster/151799) | 화학 반응 메커니즘 다이어그램을 SM-SMARTS로 파싱하는 VLM MechParser | Spotlight |
| 31 | [MICE: Multi-animal Interaction Context Encoder — A Hierarchical Foundation Model for Mouse Behavior](https://neurips.cc/virtual/2026/poster/150591) | 다중 개체 상호작용을 인코딩하는 마우스 행동 foundation model MICE | Spotlight |
| 32 | [Modeling the Vividness of Imagined Natural Scenes Reveals a Model-Common Image-Level Component in Vision Models](https://neurips.cc/virtual/2026/poster/151888) | 상상 이미지 선명도 판단을 예측해 비전 모델의 공통 성분 발견 | Spotlight |
| 33 | [mRNABench: A curated benchmark for mature mRNA property and function prediction](https://neurips.cc/virtual/2026/poster/139560) | 성숙 mRNA 속성·기능 예측 벤치마크 mRNABench | Spotlight |
| 34 | [Neural‑Visual Decoding via Cognitive‑guided Adaptive Blurring and Information‑Constrained Alignment](https://neurips.cc/virtual/2026/poster/154463) | 인지 기반 적응적 블러링으로 EEG 시각 디코딩 성능 향상 | Spotlight |
| 35 | [Normative Networks for Source Separation via Local Plasticity and Dendritic Computation](https://neurips.cc/virtual/2026/poster/148835) | 국소 가소성과 수상돌기 계산으로 구현되는 생물학적 블라인드 소스 분리 네트워크 | Spotlight |
| 36 | [OceanCBM: A Concept Bottleneck Model for Mechanistic Interpretability in Ocean Forecasting](https://neurips.cc/virtual/2026/poster/150573) | 물리 개념 병목으로 해석 가능한 해양 예측 모델 OceanCBM | Spotlight |
| 37 | [OpenWhistle: A Large-Scale Longitudinal Dataset and Benchmark of Bottlenose Dolphin Vocalizations](https://neurips.cc/virtual/2026/poster/139275) | 병코돌고래 휘파람 대규모 종단 데이터셋과 벤치마크 OpenWhistle | Spotlight |
| 38 | [Planning as Dynamics Relaxation: Hippocampal Recurrent Network Realizes Optimal Goal-Directed Navigation](https://neurips.cc/virtual/2026/poster/150211) | 해마 순환망의 이완 동역학이 최적 목표 지향 내비게이션을 구현함을 증명 | Spotlight |
| 39 | [Reconstructing the Vocal Tract with Differentiable Acoustic Simulation](https://neurips.cc/virtual/2026/poster/151084) | 미분가능 음향 시뮬레이터로 음성에서 성도 형상 복원 | Spotlight |
| 40 | [Scaling Genomic Language Modeling with Unified Corpus and Evaluation in Bacteria](https://neurips.cc/virtual/2026/poster/139114) | 박테리아 유전체 언어모델용 대규모 코퍼스 BacCorpus와 벤치마크 BacBench | Spotlight |
| 41 | [StomataBench: Measuring Taxonomic Generalization in Stomatal Detection](https://neurips.cc/virtual/2026/poster/139110) | 기공(stomata) 검출 분류군 일반화 벤치마크 StomataBench | Spotlight |
| 42 | [TagBO: LLM-Driven Task-Aware Graph Bayesian Optimization for Scientific Discovery](https://neurips.cc/virtual/2026/poster/148670) | LLM 관계 사전을 쓰는 그래프 베이지안 최적화로 과학적 발견 TagBO | Spotlight |
| 43 | [Targeted Review for AI-Assisted Biodiversity Surveys: Active Continuous-Score Occupancy Modeling](https://neurips.cc/virtual/2026/poster/155443) | 생태학 점유 모델링에서 전문가 검토 대상을 능동 선택하는 ACORN | Spotlight |
| 44 | [The Neural Race Model](https://neurips.cc/virtual/2026/poster/152312) | 자극 조건부 neural SDE로 지각 의사결정 반응시간을 모델링 | Spotlight |
| 45 | [ViroGym: Realistic Large-Scale Benchmarks for Evaluating Viral Proteins](https://neurips.cc/virtual/2026/poster/139039) | 바이러스 단백질 variant 효과 예측용 pLM 벤치마크 ViroGym | Spotlight |
| 46 | [What do EEG Foundation Models Capture from Human Brain Signals?](https://neurips.cc/virtual/2026/poster/150770) | EEG 파운데이션 모델이 포착하는 임상 특징 분석 | Spotlight |

## 컴퓨터 비전·3D

| # | 제목 | 한 줄 요약 | 형식 |
|---:|---|---|---|
| 1 | [Beyond Family Labels: A Taxonomic Ornstein-Uhlenbeck Prior for Avian 3D Shape Recovery](https://neurips.cc/virtual/2026/poster/151996) | 분류학 OU 사전분포로 조류 3D 형상 복원의 미관측 종 일반화 개선 | Oral |
| 2 | [Can We Model the Artifacts Explicitly? Disentangle Artifacts via Pairwise Edit Relations for Image Manipulation Localization](https://neurips.cc/virtual/2026/poster/155638) | 쌍별 편집 관계로 아티팩트를 명시적으로 분리하는 이미지 조작 위치 추정 | Oral |
| 3 | [Certifiably Optimal Robust Angular Synchronization](https://neurips.cc/virtual/2026/poster/153331) | 로버스트 각도 동기화를 전역 최적으로 인증하는 branch-and-bound 알고리즘 | Oral |
| 4 | [Consistent 3D Surface Flow Model with Global State](https://neurips.cc/virtual/2026/poster/148758) | 전역 잠재 상태와 flow matching으로 임의 해상도 3D 표면을 복원하는 Surflo | Oral |
| 5 | [Déjà View: Looping Transformers for Multi-View 3D Reconstruction](https://neurips.cc/virtual/2026/poster/154303) | 루프 트랜스포머로 파라미터 효율적인 다중 뷰 3D 재구성을 하는 DéjàView | Oral |
| 6 | [Non-Colliding Biometric Identities for Digital Entities: Geometry, Capacity, and Million-Scale Virtual Identity Provisioning](https://neurips.cc/virtual/2026/poster/153119) | 실제 신원과 충돌하지 않는 가상 얼굴 신원 대규모 생성 및 프로비저닝 | Oral |
| 7 | [SAM 3D Animal: Promptable Animal 3D Reconstruction from Images in the Wild](https://neurips.cc/virtual/2026/poster/155674) | 프롬프트 기반 다중 동물 단일 이미지 3D 복원 SAM 3D Animal | Oral |
| 8 | [Shaping Useful Noise: Energy Distributions Predict Visual Pretraining Quality](https://neurips.cc/virtual/2026/poster/153569) | 에너지 분포 거리 Eld로 합성 데이터의 시각 사전학습 품질 예측 | Oral |
| 9 | [TransmissiveGS: Residual-Guided Disentangled Gaussian Splatting for Transmissive Scene Reconstruction and Rendering](https://neurips.cc/virtual/2026/poster/155367) | 투과 장면용 이중 Gaussian 분리 재구성 TransmissiveGS | Oral |
| 10 | [Trellis4D: Complex 4D Mesh Generation](https://neurips.cc/virtual/2026/poster/153899) | 복잡한 위상 변화를 다루는 비디오-to-4D 메쉬 생성 Trellis4D | Oral |
| 11 | [Video Forensic Self-Descriptions: Leveraging Temporally Distributed Forensic Microstructures for Zero-Shot Detection of AI-Generated Videos](https://neurips.cc/virtual/2026/poster/149484) | 시간적 포렌식 미세구조로 AI 생성 비디오 제로샷 탐지 | Oral |
| 12 | [3R-Adapter: Retrieval, Rewiring, and Refinement for Efficient Adaptation of 3D Reconstruction Model](https://neurips.cc/virtual/2026/poster/155977) | 3D 재구성 모델의 장기꼬리 상황 적응을 위한 관계 구조 복원 PEFT, 3R-Adapter | Spotlight |
| 13 | [AdapToPASS: Ambiguity-aware Adaptive Spherical Transformer for Panoramic Semantic Segmentation](https://neurips.cc/virtual/2026/poster/151962) | 모호성 인지 적응형 구면 Transformer로 파노라마 시맨틱 분할 강건성 향상 | Spotlight |
| 14 | [ClusterSplat: Semantic Cluster Selection for 3D Visual Grounding in Gaussian Splatting](https://neurips.cc/virtual/2026/poster/152567) | 3DGS 3D 시각 그라운딩을 클러스터 선택으로 재정의한 ClusterSplat | Spotlight |
| 15 | [Complexity Aware Continuous Level of Details for Gaussian Splatting](https://neurips.cc/virtual/2026/poster/155902) | 이미지 복잡도를 활용한 Gaussian Splatting 연속 LOD 방법 | Spotlight |
| 16 | [Cross-order Consensus Graph Matching](https://neurips.cc/virtual/2026/poster/153663) | 1차 노드와 2차 엣지 할당을 결합한 Cross-order Consensus 그래프 매칭 | Spotlight |
| 17 | [Deformable 2D Gaussian Splatting](https://neurips.cc/virtual/2026/poster/153737) | 학습 가능한 좌표 재매핑으로 Gibbs 아티팩트를 줄인 Deformable 2DGS | Spotlight |
| 18 | [GramStatTexNet: Efficient, Interpretable, and Neuro-Inspired Texture Analysis-by-Synthesis](https://neurips.cc/virtual/2026/poster/155778) | Gabor 필터와 Gram 상관을 결합한 해석 가능한 텍스처 합성 GramStatTexNet | Spotlight |
| 19 | [How Far Is Too Far? Object Recognition Declines Monotonically with Semantic Distance](https://neurips.cc/virtual/2026/poster/148472) | 객체-배경 의미 거리에 따라 인식 정확도가 단조 감소함을 보이는 벤치마크 | Spotlight |
| 20 | [MACRO: Training-free Multi-plane Attention for Closeup Render Optimization](https://neurips.cc/virtual/2026/poster/152798) | 3DGS 클로즈업 렌더링을 위한 training-free 멀티플레인 어텐션 MACRO | Spotlight |
| 21 | [MolmoMotion: Forecasting Point Trajectories in 3D with Language Instruction](https://neurips.cc/virtual/2026/poster/149894) | 언어 지시 기반 3D 점 궤적 예측 모델 MolmoMotion과 데이터셋 | Spotlight |
| 22 | [MonoChunk3D: Monocular Online 3D Instance Segmentation with Persistent Instance States](https://neurips.cc/virtual/2026/poster/155123) | 지속 인스턴스 상태를 쓰는 단안 온라인 3D 인스턴스 분할 | Spotlight |
| 23 | [MoSE3: Learning World-Space SE(3) at Every Pixel](https://neurips.cc/virtual/2026/poster/155847) | 단안 비디오에서 픽셀별 world-space SE(3) 운동을 예측하는 MoSE3 | Spotlight |
| 24 | [Natural Jammers: When Non-Robust Features Become Antagonistic](https://neurips.cc/virtual/2026/poster/149318) | 비강건 특징이 clean 이미지에서 모델을 오도하는 Natural Jammers 규명 | Spotlight |
| 25 | [Noise-Regularized Training for Learned Image Compression](https://neurips.cc/virtual/2026/poster/152186) | 입력 노이즈 정규화로 학습 이미지 압축의 BD-rate 개선 | Spotlight |
| 26 | [On the Relaxation of Conditional Independence Assumption for Image Segmentation](https://neurips.cc/virtual/2026/poster/154387) | 조건부 독립 가정을 완화해 Dice/IoU를 직접 최적화하는 분할 추론 | Spotlight |
| 27 | [Parabolic Position Encoding: Vision-Centric, Principled, Extrapolatable, General](https://neurips.cc/virtual/2026/poster/151484) | 비전 토큰을 위한 외삽 가능한 포물선 위치 인코딩 PaPE | Spotlight |
| 28 | [PGGT-Loc: Primitive-Grounded Geometry Transformer for Feed-Forward Camera Localization](https://neurips.cc/virtual/2026/poster/152738) | 평면 지도 primitive에 접지해 feed-forward 카메라 위치 추정 | Spotlight |
| 29 | [Point4D: Long-range 4D Motion Reconstruction](https://neurips.cc/virtual/2026/poster/155736) | 장기 비디오의 밀집 3D 궤적을 추정하는 feed-forward 4D 복원 Point4D | Spotlight |
| 30 | [Representation Rigidity in Face Embeddings: Orthogonal Identifiability and Backfill-Free Compatibility](https://neurips.cc/virtual/2026/poster/151431) | 얼굴 임베딩의 Procrustes rigidity로 backfill 없는 모델 업그레이드 호환 | Spotlight |
| 31 | [SIGMA: Semantic-Difference Instruction-Grounding Mask Annotator for Text-Driven Image Manipulation Localization](https://neurips.cc/virtual/2026/poster/151764) | 편집 이미지 쌍에서 마스크를 자동 생성하는 조작 영역 탐지 어노테이터 SIGMA | Spotlight |
| 32 | [TailCon: Mitigating Tail Signal Erosion through Memory Consolidation for Long-Tailed Recognition](https://neurips.cc/virtual/2026/poster/155753) | memory consolidation으로 tail signal 소실을 완화하는 long-tailed 인식 | Spotlight |
| 33 | [The Surprising Effectiveness of Video Diffusion Models for Hand Motion Reconstruction](https://neurips.cc/virtual/2026/poster/149266) | 비디오 확산 모델 표현을 활용한 egocentric 양손 4D 모션 복원 ViDiHand | Spotlight |
| 34 | [Trainable Topology Supervision under Structurally Unreliable Pseudo Supervision](https://neurips.cc/virtual/2026/poster/150633) | 구조적으로 불안정한 pseudo 라벨 하 학습 가능 topology 감독 | Spotlight |
| 35 | [TTB: Test-time MLP Baking for Efficient Rendering of Decoder-only View Synthesis Models](https://neurips.cc/virtual/2026/poster/154935) | MLP baking으로 decoder-only view synthesis 렌더링 가속 TTB | Spotlight |
| 36 | [Unified Forensic Preference Learning for Generalizable Synthetic Image Detection](https://neurips.cc/virtual/2026/poster/150807) | MLLM 포렌식 선호 학습으로 일반화 가능한 합성 이미지 탐지 UniFPL | Spotlight |
| 37 | [VLSplat: Vision-Language Guided Object-Centric 3D Gaussian Splatting via Scene Graph](https://neurips.cc/virtual/2026/poster/148647) | 장면 그래프 기반 객체 중심 3D Gaussian Splatting 시맨틱 lifting | Spotlight |
| 38 | [World Motion Models: Flexible Sequence Modeling of SE(3) Trajectories](https://neurips.cc/virtual/2026/poster/149768) | SE(3) 궤적 시퀀스 생성 모델 World Motion Models | Spotlight |
| 39 | [World Tracing: Pixel-Aligned Geometry Beyond the Visible](https://neurips.cc/virtual/2026/poster/149437) | 픽셀 정렬 다층 기하로 가려진 영역까지 완성하는 World Tracing | Spotlight |

## 정렬·안전·해석

| # | 제목 | 한 줄 요약 | 형식 |
|---:|---|---|---|
| 1 | [Catch-Only-One: Non-Transferable Examples for Model-Specific Authorization](https://neurips.cc/virtual/2026/poster/151014) | 지정 모델만 해독 가능한 비전이 가능 예제(NTE)로 모델별 데이터 사용 권한 통제 | Oral |
| 2 | [CLIOPATRA: Extracting Private Information from LLM Insights](https://neurips.cc/virtual/2026/poster/152543) | Clio 같은 LLM 인사이트 시스템에서 개인정보를 추출하는 공격 CLIOPATRA | Oral |
| 3 | [CURE: Counterfactual Unsafe-token Re-masking for Diffusion Large Language Model Test-time Alignment](https://neurips.cc/virtual/2026/poster/151876) | 확산 언어모델에서 위험 토큰을 재마스킹하는 테스트 시점 안전 정렬 CURE | Oral |
| 4 | [DD-CAM: Minimal Sufficient Explanations for Vision Models Using Delta Debugging](https://neurips.cc/virtual/2026/poster/151520) | Delta debugging으로 비전 모델의 최소 충분 설명을 찾는 DD-CAM | Oral |
| 5 | [Geometry-Aware Similarity Metrics for Neural Representations on Riemannian and Statistical Manifolds](https://neurips.cc/virtual/2026/poster/150840) | 리만 기하로 신경 표현의 내재적 기하를 비교하는 metric similarity analysis | Oral |
| 6 | [IDEA: Unwrapping Visual Black-box Models by Interaction Decomposition](https://neurips.cc/virtual/2026/poster/151393) | 개념과 문맥의 상호작용을 uniqueness/redundancy/synergy로 분해하는 설명 기법 | Oral |
| 7 | [Learning interpretable Schur forms of recurrent weight matrices](https://neurips.cc/virtual/2026/poster/155071) | Riemannian 최적화로 순환 가중치의 해석 가능한 Schur form을 찾는 SchurMO | Oral |
| 8 | [Learning to Audit ML Models with Theory of Mind](https://neurips.cc/virtual/2026/poster/155783) | 마음 이론 기반 RL로 ML 모델 오류를 자동 감사하는 RLAuditor | Oral |
| 9 | [LITMUS: Benchmarking Behavioral Jailbreaks of LLM Agents in Real OS Environments](https://neurips.cc/virtual/2026/poster/150415) | 실제 OS 환경에서 LLM 에이전트의 행동 jailbreak를 평가하는 LITMUS | Oral |
| 10 | [LoRAcles: Self-Supervised Weight-Space Interpretability at Scale](https://neurips.cc/virtual/2026/poster/154333) | LoRA 가중치를 입력받아 파인튜닝 행동을 설명하는 weight-space 해석 LoRAcles | Oral |
| 11 | [Neural Chameleons: Language Models Can Learn to Hide Their Thoughts from Unseen Activation Monitors](https://neurips.cc/virtual/2026/poster/148241) | LLM이 미지의 activation monitor를 회피하도록 학습될 수 있음을 보임 | Oral |
| 12 | [The Algorithm Is Not the Behavior: Learned Priors Override Look-Ahead in a Chess-Playing Neural Network](https://neurips.cc/virtual/2026/poster/152268) | Leela Chess Zero에서 학습된 prior가 look-ahead를 덮어쓰는 현상 분석 | Oral |
| 13 | [A Mechanistic Investigation of Theory of Mind in a Large Language Model](https://neurips.cc/virtual/2026/poster/148276) | LLM의 마음이론 능력이 범용적 표상-현실 불일치 감지 메커니즘임을 규명 | Spotlight |
| 14 | [Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning](https://neurips.cc/virtual/2026/poster/152173) | Theory-of-Mind 추론으로 악의적 LLM 에이전트를 감시하는 Agent-ToM | Spotlight |
| 15 | [Anchoring Adversarial Trajectories to Data Manifolds: A Bilevel Transfer Optimization Framework](https://neurips.cc/virtual/2026/poster/153364) | 데이터 매니폴드에 궤적을 고정하는 이중수준 최적화 기반 전이 적대 공격 | Spotlight |
| 16 | [Beyond Linear Activation Steering: Invertible Latent Transformations for Controlling LLM Behavior](https://neurips.cc/virtual/2026/poster/148807) | 가역 잠재 변환으로 LLM 행동을 제어하는 비선형 activation steering INNSteer | Spotlight |
| 17 | [CHORD: Cross-Model Hallucination Detection via Relational Graph Discrimination](https://neurips.cc/virtual/2026/poster/153626) | 관계 그래프 판별로 모델 간 전이 가능한 환각 탐지를 수행하는 CHORD | Spotlight |
| 18 | [CRAFT: Causal Responsibility and Failure Tracing in Medical Vision Language Models](https://neurips.cc/virtual/2026/poster/149960) | 의료 VLM의 중재/제동 실패를 담당하는 attention head를 인과적으로 규명한 CRAFT | Spotlight |
| 19 | [Do Thinking Tokens Help with Safety?](https://neurips.cc/virtual/2026/poster/150945) | 추론 모델의 thinking 토큰이 안전성에 도움이 되는지 분석 | Spotlight |
| 20 | [Don't Lose Focus: Activation Steering via Key-Orthogonal Projections](https://neurips.cc/virtual/2026/poster/154186) | key-orthogonal 투영으로 attention 재라우팅을 막는 activation steering SKOP | Spotlight |
| 21 | [Evaluation Awareness in Language Models Has Limited Effect on Behaviour](https://neurips.cc/virtual/2026/poster/148437) | 평가 인식 언급이 LLM 행동에 미치는 영향이 제한적임을 실험으로 확인 | Spotlight |
| 22 | [Expected Harm: Rethinking Safety Evaluation of (Mis)Aligned LLMs](https://neurips.cc/virtual/2026/poster/139760) | 실행 가능성을 반영한 Expected Harm으로 LLM 안전 평가를 재고 | Spotlight |
| 23 | [fmxcoders: Factorized Masked Crosscoders for Cross-Layer Feature Discovery](https://neurips.cc/virtual/2026/poster/154897) | 분해된 마스크 크로스코더로 층 간 특징을 발견하는 fmxcoders | Spotlight |
| 24 | [Hyperbolic Concept Bottleneck Models](https://neurips.cc/virtual/2026/poster/151003) | 쌍곡 공간 entailment cone 기반 계층 인식 Concept Bottleneck Model | Spotlight |
| 25 | [Inference-time Alignment via Sparse Junction Steering](https://neurips.cc/virtual/2026/poster/155775) | 고엔트로피 분기점에서만 개입하는 희소 inference-time alignment | Spotlight |
| 26 | [Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples](https://neurips.cc/virtual/2026/poster/154663) | LLM 사전학습 포이즈닝은 모델 크기와 무관하게 거의 일정한 문서 수로 충분 | Spotlight |
| 27 | [Political Neutrality as Balanced Approval: A Large-Scale Human Evaluation of AI Responses](https://neurips.cc/virtual/2026/poster/139670) | 양측 승인 균형으로 AI 정치적 중립성을 정의하고 대규모 인간 평가 | Spotlight |
| 28 | [Predicting Human-Gain Curves under Local Proxy Optimization from Repeated Ratings](https://neurips.cc/virtual/2026/poster/150880) | 반복 인간 평가로 proxy 최적화 시 인간 이득 곡선을 예측 | Spotlight |
| 29 | [Rethinking LLM Fine-Tuning via Weight Space Reparameterization: Preserving Safety during Downstream Adaptation](https://neurips.cc/virtual/2026/poster/153897) | 가중치 공간 재파라미터화로 파인튜닝 중 안전성 보존 (WSR-Tune) | Spotlight |
| 30 | [Safety Reconstructed: Generative Modeling via Masked Diffusion Builds Strong Safety Guardrails](https://neurips.cc/virtual/2026/poster/149672) | 마스크 확산 LM 기반 생성형 safety guard LLaDA Guard | Spotlight |
| 31 | [Structure vs. Chaos: Asymmetric Entropic Optimization for Enforcing Instruction Hierarchy](https://neurips.cc/virtual/2026/poster/150200) | 은닉 상태 엔트로피로 instruction hierarchy 위반을 탐지·교정하는 AEO | Spotlight |
| 32 | [The Curse of Multiple Mediators: Hidden Interaction Effects in Activation Patching](https://neurips.cc/virtual/2026/poster/154497) | activation patching의 다중 매개자 상호작용 효과 분석 | Spotlight |
| 33 | [The End Justifies the Mean: Linear Ranking Rules for Proportional Sequential Decisions](https://neurips.cc/virtual/2026/poster/154572) | 비례적 순차 결정을 위한 선형 랭킹 규칙 angular mean | Spotlight |
| 34 | [Theoretical Limits of Language Model Alignment](https://neurips.cc/virtual/2026/poster/153597) | KL 예산 하 언어모델 정렬의 정보이론적 한계 | Spotlight |
| 35 | [UniReFP: Robust Unified Fingerprinting for Vision Models against Cross-Task Repurposing Attacks](https://neurips.cc/virtual/2026/poster/149011) | cross-task 재목적화 공격에 강건한 비전 모델 fingerprinting UniReFP | Spotlight |
| 36 | [Unlearning That Lasts: Utility-Preserving, Robust, and Almost Irreversible Forgetting in LLMs](https://neurips.cc/virtual/2026/poster/149440) | JSD 기반 LLM unlearning JensUn과 평가 데이터셋 LPF | Spotlight |
| 37 | [Weakly Supervised Concept Learning for Interpreting and Attributing LVLM Predictions](https://neurips.cc/virtual/2026/poster/153732) | LVLM 예측을 해석하는 약지도 개념 벡터 학습 TGCL | Spotlight |

## 기타 ML (그래프·시계열·연합학습 등)

| # | 제목 | 한 줄 요약 | 형식 |
|---:|---|---|---|
| 1 | [AdaSRU: Adaptive Source-Free Recommendation Unlearning via Gradient-Constrained Optimization](https://neurips.cc/virtual/2026/poster/154534) | 원본 데이터 없이 gradient 제약 최적화로 추천 모델을 언러닝하는 AdaSRU | Oral |
| 2 | [Graph Cascades: Contagion-Based Mesoscopic Rewiring for Structure-Aware Graph Machine Learning](https://neurips.cc/virtual/2026/poster/155097) | 전염 기반 mesoscopic rewiring으로 GNN/Graph Transformer 성능 향상 | Oral |
| 3 | [LLM-Enhanced Random Forests in Orthogonal Hyperbolic Subspaces for Tabular Learning](https://neurips.cc/virtual/2026/poster/154957) | LLM 추론과 쌍곡 부분공간을 활용한 tabular 랜덤 포레스트 HOT | Oral |
| 4 | [Mitigating Confidence Miscalibration in Open-World Semi-Supervised Learning](https://neurips.cc/virtual/2026/poster/153397) | open-world 준지도 학습에서 신뢰도 오보정 완화 OpenMCM | Oral |
| 5 | [Releasing Anchors from Cross-View Correspondence: Probabilistic Multi-View Anchor Graph Clustering](https://neurips.cc/virtual/2026/poster/154593) | 정렬 불필요 확률적 multi-view anchor graph 클러스터링 | Oral |
| 6 | [Spectral Energy Allocation Enables Source-Free Domain Adaptation in Time Series Forecasting](https://neurips.cc/virtual/2026/poster/154914) | 시계열 예측 source-free 도메인 적응을 위한 Spectral Energy Allocation | Oral |
| 7 | [TiRex-2: Generalizing TiRex to Multivariate Data and Streaming](https://neurips.cc/virtual/2026/poster/151700) | 멀티변량·스트리밍을 지원하는 xLSTM 시계열 파운데이션 모델 TiRex-2 | Oral |
| 8 | [A Graph Foundation Model for Unified Clustering](https://neurips.cc/virtual/2026/poster/154668) | 비지도 통합 그래프 클러스터링을 위한 그래프 파운데이션 모델 GFM-UC | Spotlight |
| 9 | [Beyond Coordinates: Encoding Graph Structure via Contextual Distribution and Relational Similarity](https://neurips.cc/virtual/2026/poster/148246) | 맥락 분포와 관계 유사도로 그래프 구조를 인코딩하는 프레임워크 | Spotlight |
| 10 | [Beyond Linear Decoders: Dynamic Expert-Coupled Optimal Decoding for Time Series Forecasting](https://neurips.cc/virtual/2026/poster/153816) | OT 기반 동적 전문가 라우팅 디코더로 시계열 예측 성능 향상 | Spotlight |
| 11 | [Boosting Graph Contrastive Learning via Manifold-Guided Representation Disentanglement](https://neurips.cc/virtual/2026/poster/151362) | 매니폴드 유도 표현 분리로 그래프 대조학습을 개선하는 MGRD | Spotlight |
| 12 | [Budgeting Discretion: Theory and Evidence on Street-Level Decision-Making](https://neurips.cc/virtual/2026/poster/153217) | 일선 관료의 재량권을 제한 예산 동적 할당으로 모델링한 이론과 실증 | Spotlight |
| 13 | [Casper: A Projection-Based Neurosymbolic Layer for Scalable & Guaranteed Constraint Satisfaction](https://neurips.cc/virtual/2026/poster/149782) | 폐형 투영으로 제약 만족을 보장하는 뉴로심볼릭 레이어 Casper | Spotlight |
| 14 | [CLEAR: Complementary Tripartite Play with Bayesian Calibration for Semi-Supervised Edge Classification](https://neurips.cc/virtual/2026/poster/153511) | 베이지안 보정과 3자 협력으로 준지도 엣지 분류를 수행하는 CLEAR | Spotlight |
| 15 | [Complexity-Aware LoRA Aggregation for Modality-Heterogeneous Federated Person Re-identification](https://neurips.cc/virtual/2026/poster/151019) | 복잡도 인지 LoRA 집계로 모달리티 이질적 연합 Re-ID 수행 | Spotlight |
| 16 | [DDGE: Disentangled Dirichlet Geodesic Evaluation for Robust Few-Shot Learning](https://neurips.cc/virtual/2026/poster/151036) | Dirichlet 측지 거리로 노이즈에 강한 few-shot 학습을 수행하는 DDGE | Spotlight |
| 17 | [Entropy Minimization without Model Collapse: Mitigating Prediction Bias in Medical Imaging](https://neurips.cc/virtual/2026/poster/149828) | 예측 편향을 줄여 엔트로피 최소화의 모델 붕괴를 막는 의료영상 TTA | Spotlight |
| 18 | [ExtrapAir: Air Quality Inference at Unmonitored Locations via Weather-Bridged Spatial Attention](https://neurips.cc/virtual/2026/poster/154246) | 기상 변수를 매개로 미관측 지점의 대기질을 추정하는 ExtrapAir | Spotlight |
| 19 | [FedSOUL: Federated Continual Unlearning via Spectral Orthogonality](https://neurips.cc/virtual/2026/poster/153586) | 스펙트럼 직교성으로 연합 연속 언러닝을 수행하는 FedSOUL | Spotlight |
| 20 | [FiTS: Interpretable Spiking Neurons via Frequency Selectivity and Temporal Shaping](https://neurips.cc/virtual/2026/poster/148427) | 주파수 선택성과 시간 형성으로 해석 가능한 스파이킹 뉴런 FiTS | Spotlight |
| 21 | [Mitigating Over-squashing without Rewiring: A Sheaf Effective Resistance Perspective](https://neurips.cc/virtual/2026/poster/150297) | sheaf effective resistance로 rewiring 없이 GNN over-squashing 완화 | Spotlight |
| 22 | [MT-CC: Multi-Group Temperature Scaling for Asymmetric Calibration Behavior in Class-Incremental Learning](https://neurips.cc/virtual/2026/poster/148768) | 클래스 증분 학습의 비대칭 보정을 위한 다중 그룹 temperature scaling | Spotlight |
| 23 | [NLD4CO: Neural Langevin Dynamics for Combinatorial Optimization](https://neurips.cc/virtual/2026/poster/149843) | 신경 Langevin 동역학으로 조합 최적화 문제를 해결하는 NLD4CO | Spotlight |
| 24 | [Paloma: Phase-Conditioned Residual Modulation for Time Series Forecasting](https://neurips.cc/virtual/2026/poster/154087) | 위상 조건부 잔차 변조로 시계열 예측을 개선하는 Paloma | Spotlight |
| 25 | [Parallel-in-Time Training of Recurrent Neural Networks for Dynamical Systems Reconstruction](https://neurips.cc/virtual/2026/poster/148849) | 병렬 스캔 기반 RNN 학습으로 긴 시퀀스 동역학계 복원 | Spotlight |
| 26 | [Prospective Coding Improves Learning in Deep Continuous-Time Recurrent Networks](https://neurips.cc/virtual/2026/poster/153925) | prospective coding으로 깊은 연속시간 순환망의 학습 개선 | Spotlight |
| 27 | [RAMA: Resistance-Aware Multi-Hop Aggregation Graph Representation Learning for Robust Ethereum Account Classification](https://neurips.cc/virtual/2026/poster/154374) | 저항 거리 기반 multi-hop 집계 GNN으로 이더리움 계정 분류 | Spotlight |
| 28 | [Realism VS Accuracy: Event Sequence Forecasting from a Generative Modeling Perspective](https://neurips.cc/virtual/2026/poster/139504) | 이벤트 시퀀스 예측의 정확도 대 현실성 trade-off 벤치마크 | Spotlight |
| 29 | [Rubato: Signature Attention for Irregular Multivariate Time Series Forecasting](https://neurips.cc/virtual/2026/poster/153092) | 불규칙 다변량 시계열용 path signature 커널 attention Rubato | Spotlight |
| 30 | [Rubato: Transcribing Piano Music with Timestamps](https://neurips.cc/virtual/2026/poster/149838) | 오디오에서 타임스탬프 포함 피아노 악보를 전사하는 Rubato 모델 | Spotlight |
| 31 | [Spectral Reversal: Counteracting Singular Value Bias for Graph Prompting](https://neurips.cc/virtual/2026/poster/152228) | 특이값 편향을 뒤집는 spectral reverse 그래프 프롬프팅 | Spotlight |
| 32 | [TSQAgent: Rating Time Series Data Quality via Dedicated Agentic Reasoning](https://neurips.cc/virtual/2026/poster/150288) | 에이전트 추론으로 시계열 데이터 품질을 평가하는 TSQAgent와 TSQBench | Spotlight |
| 33 | [Uncertainty-Aware Probabilistic Constrained Clustering from Entangled Pairwise Supervision](https://neurips.cc/virtual/2026/poster/154307) | 얽힌 pairwise 감독에서의 확률적 constrained clustering | Spotlight |
| 34 | [Volatility-Whitened Probabilistic Residual Modeling for Long-Term Time Series Forecasting](https://neurips.cc/virtual/2026/poster/155322) | 변동성 whitening 확률 잔차 모델링 장기 시계열 예측 VolaRM | Spotlight |
| 35 | [Weisfeiler-Leman Is Incomplete on Simple Spectrum Graphs, so Canonicalize Them](https://neurips.cc/virtual/2026/poster/150655) | Weisfeiler-Leman 불완전성 증명과 simple-spectrum 그래프 canonicalization | Spotlight |
| 36 | [Winfree Oscillatory Neural Network](https://neurips.cc/virtual/2026/poster/150411) | Winfree 진동 신경망 WONN으로 ImageNet·Maze 추론 | Spotlight |

## 생성 모델 (diffusion·flow·영상)

| # | 제목 | 한 줄 요약 | 형식 |
|---:|---|---|---|
| 1 | [Generative Modeling via Drifting](https://neurips.cc/virtual/2026/poster/154240) | 분포를 학습 중 drift시켜 one-step 생성을 달성하는 Drifting Models (FID 1.54) | Oral |
| 2 | [ParetoSlider: Diffusion Models Post-Training for Continuous Reward Control](https://neurips.cc/virtual/2026/poster/154172) | 선호 가중치 조건화로 추론 시 보상 trade-off를 조절하는 확산 후학습 | Oral |
| 3 | [Representation Fréchet Loss for Visual Generation](https://neurips.cc/virtual/2026/poster/154990) | 표현 공간 Fréchet distance를 학습 손실로 사용하는 FD-Loss 생성 모델 후처리 | Oral |
| 4 | [Strong Stochastic Flow Maps](https://neurips.cc/virtual/2026/poster/149475) | SDE의 strong solution map을 학습하는 Strong Stochastic Flow Maps | Oral |
| 5 | [Tessellations of Semi-Discrete Flow Matching](https://neurips.cc/virtual/2026/poster/153677) | semi-discrete flow matching의 종단 할당 영역 tessellation 기하 분석 | Oral |
| 6 | [Arena-T2I Hard: Benchmarking and Improving Faithfulness with Dependency-Aware Checklist Rewards](https://neurips.cc/virtual/2026/poster/151320) | T2I 충실도 벤치마크 Arena-T2I Hard와 의존성 인식 체크리스트 보상 | Spotlight |
| 7 | [Breaking the Uniformity Trap: Scaling Video Diffusion Model via SplitMoE](https://neurips.cc/virtual/2026/poster/152515) | 비디오 확산 모델을 위한 의미/범용 전문가 분리 SplitMoE | Spotlight |
| 8 | [City-RAG: Stepping Into a City via Spatially-Grounded Video Generation](https://neurips.cc/virtual/2026/poster/154638) | 지오 등록 데이터로 현실 도시를 근거로 한 비디오 생성 CityRAG | Spotlight |
| 9 | [Diff-CA: Separating Common and Salient Factors with Diffusion Models](https://neurips.cc/virtual/2026/poster/152753) | 확산 모델로 공통 요인과 고유 요인을 분리하는 대조 분석 Diff-CA | Spotlight |
| 10 | [Dream-Cubed: Controllable Generative Modeling in Minecraft by Training on Billions of Cubes](https://neurips.cc/virtual/2026/poster/139806) | 마인크래프트 복셀 월드 데이터셋과 3D 확산 생성 모델 Dream-Cubed | Spotlight |
| 11 | [Efficient Adjoint Matching for Fine-tuning Diffusion Models](https://neurips.cc/virtual/2026/poster/148733) | 선형 base drift 재정식화로 Adjoint Matching을 효율화한 확산 미세조정 EAM | Spotlight |
| 12 | [Flow Matching Reinforcement Learning via SDE Inference](https://neurips.cc/virtual/2026/poster/153016) | SDE 추론으로 flow matching 모델에 RL을 적용하는 통합 이론 프레임워크 | Spotlight |
| 13 | [Flow-DPPO: Divergence Proximal Policy Optimization for Flow Matching Models](https://neurips.cc/virtual/2026/poster/150977) | 비율 클리핑 대신 divergence 제약을 쓰는 flow matching RL Flow-DPPO | Spotlight |
| 14 | [From Next-Token to Next-Block: A Principled Adaptation Path for Diffusion LLMs](https://neurips.cc/virtual/2026/poster/152123) | AR 모델을 block-diffusion LLM으로 적응시키는 context-causal 경로와 NBDIFF-7B | Spotlight |
| 15 | [GenRM-Flow: Generators are Process-aware Reward Models in Flow Matching](https://neurips.cc/virtual/2026/poster/151044) | 선호 튜닝된 비디오 생성기를 flow matching 속도 오차 기반 reward model로 활용 | Spotlight |
| 16 | [Improving the Diffusability of Motion Tokenizer](https://neurips.cc/virtual/2026/poster/150734) | 스펙트럼 불일치를 줄여 text-to-motion 잠재 확산용 토크나이저 개선 | Spotlight |
| 17 | [L2P: Unlocking Latent Potential for Pixel Generation](https://neurips.cc/virtual/2026/poster/153588) | 사전학습 LDM 지식을 픽셀 공간 확산 모델로 전이하는 L2P | Spotlight |
| 18 | [Mesh BDF: Barycentric Dominance Field for 3D Native Mesh Generation](https://neurips.cc/virtual/2026/poster/154136) | 연속 barycentric dominance field로 확산 기반 3D 메시 생성 | Spotlight |
| 19 | [PixelPonder: Dynamic Patch Adaptation for Enhanced Multi-Conditional Text-to-Image Generation](https://neurips.cc/virtual/2026/poster/153024) | 패치 단위 적응적 조건 선택의 다중 조건 text-to-image 생성 | Spotlight |
| 20 | [Reasoning with Undecoded Tokens in Diffusion Language Models](https://neurips.cc/virtual/2026/poster/152594) | 확산 언어모델의 undecoded token을 latent token으로 활용한 추론 개선 | Spotlight |
| 21 | [Seed-Your-Motion: Householder Orthogonal Noise for Motion-Controllable Video Diffusion Models](https://neurips.cc/virtual/2026/poster/150697) | Householder 직교 노이즈로 모션 제어 가능한 비디오 확산 | Spotlight |
| 22 | [Solaris: Building a Multiplayer Video World Model in Minecraft](https://neurips.cc/virtual/2026/poster/148491) | Minecraft 멀티플레이어 비디오 월드 모델 Solaris | Spotlight |
| 23 | [Spherical Flows for Sampling Categorical Data](https://neurips.cc/virtual/2026/poster/148878) | von Mises-Fisher 구면 flow로 범주형 데이터 생성 | Spotlight |
| 24 | [STREAM: Stochastic Riemannian Flow Matching with Anisotropic Decoder for Digital Histopathology Image Generation](https://neurips.cc/virtual/2026/poster/149538) | 리만 flow matching으로 병리 조직 이미지 생성 STREAM | Spotlight |
| 25 | [The Invisible Hand of Physics: When Video Diffusion Models Know More Than They Show](https://neurips.cc/virtual/2026/poster/149891) | 비디오 확산 모델이 내부적으로 물리적 타당성을 인코딩함을 프로빙 | Spotlight |
| 26 | [The Value of Covariance Matching in Gaussian DDPMs and the Lanczos Sampler](https://neurips.cc/virtual/2026/poster/148184) | Gaussian DDPM 공분산 매칭과 Lanczos 샘플러 | Spotlight |
| 27 | [Toward Semantically-Consistent Tuning-Free Customization for Rectified Flow Transformers](https://neurips.cc/virtual/2026/poster/152751) | Rectified flow transformer의 의미 일관적 tuning-free 맞춤 생성 | Spotlight |
| 28 | [UDT: Reconciling U-Nets and Diffusion Transformers with Data-Adaptive Token Reduction](https://neurips.cc/virtual/2026/poster/155440) | 데이터 적응형 토큰 병합 U-Net 확산 트랜스포머 UDT | Spotlight |
| 29 | [UltraDiff:Transferring High-Fidelity Priors to Compressed Latent Spaces for High-resolution Image Generation](https://neurips.cc/virtual/2026/poster/150314) | f8 prior를 f32 잠재공간으로 증류하는 고해상도 생성 UltraDiff | Spotlight |
| 30 | [What kills v-prediction? A Patch-wise PCA Perspective on Pixel-Space Flow Matching](https://neurips.cc/virtual/2026/poster/154141) | 픽셀 공간 flow matching에서 v-prediction 실패 원인 PCA 분석 | Spotlight |
| 31 | [What Makes a Good Path? Factoring Manifold Support and Path Geometry](https://neurips.cc/virtual/2026/poster/149855) | 확산 prior와 기하 prior를 분리한 다양체 경로 geodesic force matching | Spotlight |
| 32 | [When Policy Entropy Constraint Fails: Preserving Diversity in Flow-based RLHF via Perceptual Entropy](https://neurips.cc/virtual/2026/poster/155843) | flow 기반 RLHF의 다양성 붕괴를 perceptual entropy로 방지 | Spotlight |
| 33 | [WTF?! Simulation-Free Reinforcement Learning with Wasserstein-Tilted Flow Maps](https://neurips.cc/virtual/2026/poster/150454) | Wasserstein-tilted flow map으로 simulation-free 생성 flow RL 파인튜닝 | Spotlight |
| 34 | [X2HDR: HDR Image Generation in a Perceptually Uniform Space](https://neurips.cc/virtual/2026/poster/148447) | perceptually uniform 공간에서 확산 모델 HDR 이미지 생성 X2HDR | Spotlight |

## 멀티모달·비전-언어

| # | 제목 | 한 줄 요약 | 형식 |
|---:|---|---|---|
| 1 | [Behavioral Geometric Supervision Aligns Video Foundation Models with Human Social Perception](https://neurips.cc/virtual/2026/poster/149277) | 행동 기하 지도로 비디오 파운데이션 모델을 인간 사회 지각에 정렬 | Oral |
| 2 | [Binding Multiple Modalities via Multimodal Wasserstein Barycenter](https://neurips.cc/virtual/2026/poster/149098) | Wasserstein barycenter로 다중 모달리티를 정렬하는 BaryBind | Oral |
| 3 | [Clarification as Supervision: Reinforcement Learning for Vision-Language Interfaces](https://neurips.cc/virtual/2026/poster/152087) | 명확화 요청을 감독으로 삼는 비전-언어 인터페이스 강화학습 AC-RL | Oral |
| 4 | [GeoSym127K: Scalable Symbolically-verifiable Synthesis for Multimodal Geometric Reasoning](https://neurips.cc/virtual/2026/poster/139481) | 기호적으로 검증 가능한 기하 추론 멀티모달 데이터셋 GeoSym127K 합성 | Oral |
| 5 | [Incentivizing Medical Vision Capabilities from Large-Scale Multimodal Pre-training](https://neurips.cc/virtual/2026/poster/156128) | 6천만 쌍 의료 영상-텍스트 사전학습 후 RL로 의료 VLM 성능 도출 | Oral |
| 6 | [LatentUM: Unleashing the Potential of Interleaved Cross-Modal Reasoning via a Latent-Space Unified Model](https://neurips.cc/virtual/2026/poster/151424) | 공유 잠재 공간에서 교차 모달 추론을 수행하는 통합 모델 LatentUM | Oral |
| 7 | [SALART-VQA: Diagnosing Whether VLMs Understand Salient Artifacts in Generated Images](https://neurips.cc/virtual/2026/poster/139139) | 생성 이미지의 salient artifact를 VLM이 이해하는지 진단하는 SalArt-VQA | Oral |
| 8 | [They Can See It but not Say It: Iterative Self Knowledge Re-expression in Visual Reasoning Relative Pose Identification](https://neurips.cc/virtual/2026/poster/151372) | VLM의 상대 자세 식별 편향을 줄이는 반복 debiasing SKR-ID | Oral |
| 9 | [Thinking with Images as Continuous Policy: Numerical Visual Chain-of-Thought](https://neurips.cc/virtual/2026/poster/150085) | 연속 좌표 행동공간 기반 수치적 visual chain-of-thought NV-CoT | Oral |
| 10 | [AdaCodec: A Predictive Visual Code for Video MLLMs](https://neurips.cc/virtual/2026/poster/148821) | 비디오 MLLM용 예측 기반 시각 코드 AdaCodec으로 토큰 예산을 대폭 절감 | Spotlight |
| 11 | [BEAKER: An Expert-Curated Benchmark for Embodied Brains in Self-Driving Chemical Laboratories](https://neurips.cc/virtual/2026/poster/139293) | 자율 화학 실험실용 MLLM 구체화 능력 평가 벤치마크 BEAKER | Spotlight |
| 12 | [Before Words, Beyond Speech: Evaluating Nonverbal Social Reasoning in Early Childhood](https://neurips.cc/virtual/2026/poster/139741) | 유아기 비언어 사회 추론을 평가하는 비디오 벤치마크 NEST | Spotlight |
| 13 | [DeltaPrompts: Escaping the Zero-Delta Trap in Multimodal Distillation](https://neurips.cc/virtual/2026/poster/153494) | 교사-학생 답변 발산이 큰 프롬프트로 VLM 증류를 개선하는 DeltaPrompts | Spotlight |
| 14 | [MinerU2.5-Pro: Pushing the Limit of Document Parsing via a Calibrated Evaluation-Data Flywheel](https://neurips.cc/virtual/2026/poster/139545) | 평가-데이터 flywheel로 문서 파싱 성능을 끌어올린 MinerU2.5-Pro | Spotlight |
| 15 | [OmniGF: A Dual-Branch Vision-Language Framework for Unified Gaze Following](https://neurips.cc/virtual/2026/poster/155919) | VLM 기반 이중 브랜치 다인 시선 추적 통합 프레임워크 OmniGF | Spotlight |
| 16 | [OneCanvas: 3D Scene Understanding via Panoramic Reprojection](https://neurips.cc/virtual/2026/poster/148266) | 파노라마 재투영으로 VLM의 3D 장면 이해를 수행하는 OneCanvas | Spotlight |
| 17 | [P^3-VLM: A Point-based Alternative for Grounded 3D Vision-Language Models](https://neurips.cc/virtual/2026/poster/151816) | 바운딩 박스 shortcut 없이 점 프롬프트로 접지하는 3D VLM P3-VLM | Spotlight |
| 18 | [ProCLIP: Progressive Vision-Language Alignment via LLM-based Embedder](https://neurips.cc/virtual/2026/poster/151998) | LLM 임베더를 CLIP에 점진 정렬해 장문·다국어 지원하는 ProCLIP | Spotlight |
| 19 | [ROSE: Risk-Aware Orthogonal Subspace Navigation for Lifelong Knowledge Editing in Multimodal Large Language Models](https://neurips.cc/virtual/2026/poster/155206) | MLLM 평생 지식 편집을 위한 risk-aware 직교 부분공간 ROSE | Spotlight |
| 20 | [Scaling Laws for Multimodal Data Mixtures](https://neurips.cc/virtual/2026/poster/148475) | 텍스트·비전·오디오 멀티모달 데이터 혼합 scaling law | Spotlight |
| 21 | [SceneBind: Binding What and Where Across Vision, Audio, and Language](https://neurips.cc/virtual/2026/poster/153396) | 비전·오디오·언어를 묶는 의미-공간 omni-modal 표현 SceneBind | Spotlight |
| 22 | [SceneScaffold: Active Scene-State Construction for Unified 3D Scene Understanding](https://neurips.cc/virtual/2026/poster/154773) | 역할 인식 scene-state 구성으로 통합 3D 장면 이해 (3D-LMM) | Spotlight |
| 23 | [Self-Rewarded Multimodal Coherent Reasoning Across Diverse Visual Domains](https://neurips.cc/virtual/2026/poster/149029) | 라벨 없는 자기참조 보상으로 멀티모달 추론 일관성 정렬 SR-MCR | Spotlight |
| 24 | [Strong Helps Weak: Directional Cross-Modal Alignment Transfer in Multi-modal LLMs](https://neurips.cc/virtual/2026/poster/153529) | 강한 모달리티에서 약한 모달리티로 정렬을 전이하는 MLLM 병합 DCAT | Spotlight |
| 25 | [Text as Partial Constraint: Core–Residual Alignment for Robust Vision–Language Learning](https://neurips.cc/virtual/2026/poster/148465) | 캡션을 부분 제약으로 보는 core-residual 비전-언어 정렬 | Spotlight |
| 26 | [The Design Space of Tri-Modal Masked Diffusion Models](https://neurips.cc/virtual/2026/poster/153185) | 텍스트·이미지·오디오 tri-modal masked diffusion 모델 설계 공간 | Spotlight |
| 27 | [The Value of Being Wrong: Self-Mined Visual In-Context Learning from Errors](https://neurips.cc/virtual/2026/poster/151028) | VLM 자체 오류를 demonstration으로 쓰는 visual ICL SMILE | Spotlight |
| 28 | [Tune-Up Open-Weight CLIP: Optimization Framework for Self-Supervised Fine-tuning of CLIP](https://neurips.cc/virtual/2026/poster/154261) | 오픈 가중치 CLIP의 self-supervised 파인튜닝 TuneCLIP | Spotlight |
| 29 | [UGGRH: Unsupervised Generative Completion and Graph-attention Refinement for Incomplete Cross-modal Hashing](https://neurips.cc/virtual/2026/poster/154876) | 불완전 cross-modal hashing을 위한 생성적 보완과 graph attention | Spotlight |
| 30 | [Uncovering and Shaping the Latent Representation of 3D Scene Topology in Vision-Language Models](https://neurips.cc/virtual/2026/poster/148612) | VLM 내부의 3D 장면 위상 표현 발견과 Dirichlet 정규화 | Spotlight |

## 강화학습·로보틱스·embodied

| # | 제목 | 한 줄 요약 | 형식 |
|---:|---|---|---|
| 1 | [Can In-Context Learning Support Intrinsic Curiosity?](https://neurips.cc/virtual/2026/poster/151481) | in-context learning이 내재적 호기심 보상을 지원할 수 있는지 이론적으로 분석 | Oral |
| 2 | [Coordination Connectivity: Shared Initialization Shapes the Joint-Policy Landscape in MARL](https://neurips.cc/virtual/2026/poster/154512) | MARL에서 공유 초기화가 joint-policy 지형을 결정함을 보인 coordination connectivity | Oral |
| 3 | [Emergence of Physical Intelligence via Controllable Information Production](https://neurips.cc/virtual/2026/poster/152582) | 제어 가능한 정보 생산(CIP)에 기반한 내재 동기 프레임워크 | Oral |
| 4 | [HABIT: Human-Aware Behavior and Interaction Training Dataset for Robot Manipulation](https://neurips.cc/virtual/2026/poster/139828) | 사람이 있는 환경의 로봇 조작 시연 데이터셋 HABIT | Oral |
| 5 | [Language-Conditioned World Modeling for Visual Navigation](https://neurips.cc/virtual/2026/poster/154464) | 언어 조건 시각 내비게이션 데이터셋과 world model 기반 정책 학습 | Oral |
| 6 | [PhaseLoRA: Control-Regime-Conditioned Low-Rank Adaptation for Continuous-Action Vision-Language-Action Policies](https://neurips.cc/virtual/2026/poster/151017) | 제어 단계별 조건화 LoRA로 VLA 정책을 효율적으로 적응 | Oral |
| 7 | [Proactive Instance Navigation with Comparative Judgment for Ambiguous User Queries](https://neurips.cc/virtual/2026/poster/153423) | 후보 풀을 구분하는 질문으로 모호한 인스턴스 내비게이션 수행 | Oral |
| 8 | [Resilience Matters for Embodied Agents System: New Metrics, Systematic Evaluation, and Optimization](https://neurips.cc/virtual/2026/poster/148940) | 임바디드 에이전트 시스템의 resilience 평가 지표와 최적화 | Oral |
| 9 | [SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators](https://neurips.cc/virtual/2026/poster/149981) | 시각 보정 에피소드로 제로샷 시뮬레이터가 되는 로봇 월드 모델 SyncWorld | Oral |
| 10 | [Training Generalizable Collaborative Agents via Strategic Risk Aversion](https://neurips.cc/virtual/2026/poster/151685) | 전략적 위험 회피로 일반화 가능한 협력 MARL 에이전트 학습 | Oral |
| 11 | [Unifying Goal-Conditioned RL and Unsupervised Skill Learning via Control-Maximization](https://neurips.cc/virtual/2026/poster/153300) | control maximization으로 목표조건 RL과 비지도 스킬 학습 통합 | Oral |
| 12 | [Adaptive Stepsizes for Eligibility Traces in Deep Reinforcement Learning](https://neurips.cc/virtual/2026/poster/153394) | 딥 RL에서 eligibility trace에 적응형 벡터 스텝사이즈를 도입한 스트리밍 알고리즘 | Spotlight |
| 13 | [Addressing Exogenous Variability in Cooperative Multi-Agent Reinforcement Learning](https://neurips.cc/virtual/2026/poster/149019) | 외생 변동 하에서 협력적 MARL을 위한 ED-POMDP 정식화와 LEICA 알고리즘 | Spotlight |
| 14 | [Closed Loop Dynamic Driving Data Mixture for Real-Synthetic Co-Training](https://neurips.cc/virtual/2026/poster/149779) | 폐루프 데이터 혼합 최적화로 자율주행 실제-합성 공동학습을 개선하는 AutoScale | Spotlight |
| 15 | [Distributionally Robust Domain Randomization with Learned Risk-Sensitive Dynamics Samplers](https://neurips.cc/virtual/2026/poster/150440) | 위험 민감 동역학 샘플러로 분포적 강건 domain randomization 수행 | Spotlight |
| 16 | [Fast-WAM: Do World Action Models Need Test-time Future Imagination?](https://neurips.cc/virtual/2026/poster/149922) | 테스트 시 미래 상상 없이도 강한 World Action Model Fast-WAM | Spotlight |
| 17 | [Local Guidance, Global Impact: Gaussian-Reshaped Trust Region Unlocks Behavior Transitions](https://neurips.cc/virtual/2026/poster/155658) | 비정상 환경에서 Gaussian trust region으로 PPO 행동 전환 개선 | Spotlight |
| 18 | [Localized Dynamics-Aware Domain Adaption for Off-Dynamics Offline Reinforcement Learning](https://neurips.cc/virtual/2026/poster/151978) | 국소 동역학 불일치 기반 데이터 선택의 off-dynamics 오프라인 RL | Spotlight |
| 19 | [Provably Safe, Yet Performant Reinforcement Learning](https://neurips.cc/virtual/2026/poster/152935) | 학습된 백업 정책과 미분가능 projection으로 증명 가능한 안전 RL | Spotlight |
| 20 | [Revisiting Embodied Chain-of-Thought for Generalizable Robot Manipulation](https://neurips.cc/virtual/2026/poster/156114) | 대규모 embodied CoT 코퍼스와 CoT-dropout VLA 모델 ERVLA | Spotlight |
| 21 | [ROTATE: Regret-driven Open-ended Training for Ad Hoc Teamwork](https://neurips.cc/virtual/2026/poster/150582) | 적대적 팀원 생성으로 ad hoc teamwork를 학습하는 ROTATE | Spotlight |
| 22 | [Tactile MNIST: Benchmarking Active Tactile Perception](https://neurips.cc/virtual/2026/poster/139796) | 능동 촉각 인식 벤치마크 Tactile MNIST | Spotlight |
| 23 | [Towards Convergence of PPO: An Approximate Descent Approach](https://neurips.cc/virtual/2026/poster/155526) | PPO clipped actor update의 수렴성을 근사 하강으로 분석 | Spotlight |
| 24 | [When Does Non-Uniform Replay Matter in Reinforcement Learning?](https://neurips.cc/virtual/2026/poster/153281) | off-policy RL에서 non-uniform replay가 유효한 조건 분석 | Spotlight |
| 25 | [Whole-Body Compliant Control via Learned Force-Regulation Modules](https://neurips.cc/virtual/2026/poster/154032) | 학습된 force-regulation 모듈로 휴머노이드 전신 compliant 제어 | Spotlight |

## 데이터셋·벤치마크·평가

| # | 제목 | 한 줄 요약 | 형식 |
|---:|---|---|---|
| 1 | [ALTER: An Allen's Algebra-Based Evaluation Framework for Temporal Reasoning of LLMs](https://neurips.cc/virtual/2026/poster/139265) | Allen 구간 대수 기반 LLM 시간 추론 평가 프레임워크 ALTER | Oral |
| 2 | [Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs](https://neurips.cc/virtual/2026/poster/138960) | LLM 벤치마크의 건강도를 정량화하는 Benchmark Health Index | Oral |
| 3 | [DD-Ranking: Rethinking the Evaluation of Dataset Distillation](https://neurips.cc/virtual/2026/poster/139355) | 데이터셋 증류 평가의 공정성을 재검토한 DD-Ranking 프레임워크 | Oral |
| 4 | [Evaluating Neural Data Tokenizers: A Framework for Assessing Learned Representations of Spiking Activity](https://neurips.cc/virtual/2026/poster/139125) | 스파이킹 신경 활동 토크나이저를 평가하는 프레임워크와 벤치마크 | Oral |
| 5 | [GenAI Evaluation Results are Largely Artifacts of Evaluation Design Choices: Evidence from Audit Studies of Resume Screening](https://neurips.cc/virtual/2026/poster/138976) | 이력서 스크리닝 편향 평가 결과가 실험 설계 선택에 크게 좌우됨을 보임 | Oral |
| 6 | [HearSayBench: Can LLMs Navigate from Abstract Human Rights to Lived Lives?](https://neurips.cc/virtual/2026/poster/139278) | 인권 맥락의 현실적 제약 추론을 평가하는 LLM 벤치마크 HearSayBench | Oral |
| 7 | [Leaderboard Hacking: Preference-Based Model Evaluations are Vulnerable to Manipulation](https://neurips.cc/virtual/2026/poster/152085) | Arena식 선호 기반 LLM 리더보드의 조작 취약성 분석 | Oral |
| 8 | [LittleLearner: Language Models Under Pedagogically-Controlled Knowledge Exposure](https://neurips.cc/virtual/2026/poster/148220) | 초등 수준 지식만 담은 88B 토큰 코퍼스와 LittleLearner 모델 | Oral |
| 9 | [MLS-Bench: A Holistic and Rigorous Assessment of AI Systems on Building Better AI](https://neurips.cc/virtual/2026/poster/139626) | AI가 새로운 ML 방법을 발명할 수 있는지 평가하는 MLS-Bench | Oral |
| 10 | [Offloading Score: Measuring AI Reliance through Counterfactual Workflows](https://neurips.cc/virtual/2026/poster/139388) | 반사실 워크플로로 AI 도구 의존도를 측정하는 offloading score | Oral |
| 11 | [Are LLM Safety Judges Policy-Invariant? A Three-Principle Stress-Test](https://neurips.cc/virtual/2026/poster/139215) | LLM 안전 심판이 정책 문구 변화에 불변인지 검증하는 스트레스 테스트 | Spotlight |
| 12 | [Beyond Downstream Scores: Controlled Diagnostics for Point-Cloud Self-Supervised Learning Evaluation](https://neurips.cc/virtual/2026/poster/139098) | 포인트 클라우드 SSL 평가를 위한 통제된 진단 프로토콜 | Spotlight |
| 13 | [Do Image Editing Models Understand Lighting?](https://neurips.cc/virtual/2026/poster/139308) | 이미지 편집 모델이 실제 조명을 이해하는지 평가하는 3DLP 벤치마크 | Spotlight |
| 14 | [Doomed to Re-Annotate, Forever: The ImageNet Story](https://neurips.cc/virtual/2026/poster/139569) | ImageNet-1k 검증셋을 처음부터 재주석한 ReImageNet | Spotlight |
| 15 | [EVALUATION CARDS: An Interpretive Layer for AI Evaluation Reporting](https://neurips.cc/virtual/2026/poster/139130) | AI 평가 결과 보고를 통합하는 Evaluation Cards 해석 계층 | Spotlight |
| 16 | [IndustryCode: A Benchmark for Industry Code Generation](https://neurips.cc/virtual/2026/poster/139055) | 다양한 산업 도메인·언어를 아우르는 코드 생성 벤치마크 IndustryCode | Spotlight |
| 17 | [InSpect: A Curated Natural History Collection Dataset for Insect Specimen Understanding](https://neurips.cc/virtual/2026/poster/139783) | 곤충 표본 인식 및 해부학적 부위 분할 데이터셋 InSpect | Spotlight |
| 18 | [KnowVis: A Dual-View Benchmark for Diagnosing World-Knowledge Grounding in Text-to-Image Models](https://neurips.cc/virtual/2026/poster/139323) | T2I 모델의 세계 지식 grounding을 진단하는 벤치마크 KnowVis | Spotlight |
| 19 | [Large Language Model Selection with Limited Annotations](https://neurips.cc/virtual/2026/poster/139074) | 제한된 라벨로 최적 LLM을 고르는 능동 모델 선택 Select-LLM | Spotlight |
| 20 | [Object Detection Benchmarks are Incomplete: The Role of Label Errors and Annotation Uncertainty](https://neurips.cc/virtual/2026/poster/139282) | 객체 검출 벤치마크의 누락 라벨을 재주석하고 불확실성 인식 벤치마크 구축 | Spotlight |
| 21 | [OTel: Open Telco AI Datasets, Benchmarks, and Models](https://neurips.cc/virtual/2026/poster/139129) | 통신 도메인 AI용 오픈 데이터셋, 벤치마크, 사후학습 모델 OTel | Spotlight |
| 22 | [PULSE: A Synchronized Five-Modality Dataset for Sensorimotor Coordination in Long-Horizon Daily Activities](https://neurips.cc/virtual/2026/poster/139681) | PULSE 다섯 모달리티 동기화 장기 일상활동 sensorimotor 데이터셋과 벤치마크 | Spotlight |
| 23 | [SLAyiNG: A Diverse and Community-validated Dataset of Queer Slang](https://neurips.cc/virtual/2026/poster/138946) | 커뮤니티 검증된 퀴어 슬랭 데이터셋 SLAyiNG과 언어 편향 분석 | Spotlight |
| 24 | [The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality](https://neurips.cc/virtual/2026/poster/139445) | LLM 사실성을 종합 평가하는 FACTS Leaderboard | Spotlight |

## 확률·인과·통계 ML

| # | 제목 | 한 줄 요약 | 형식 |
|---:|---|---|---|
| 1 | [Exact Gaussian Moment Matching for Residual Networks: a Second-Order Method](https://neurips.cc/virtual/2026/poster/155943) | 잔차 신경망에서 가우시안 모멘트를 정확히 전파하는 2차 방법 | Oral |
| 2 | [Filtered Conformal Ellipsoids for Graph-Native Time Series](https://neurips.cc/virtual/2026/poster/155800) | 그래프 시계열을 위한 필터링 기반 conformal 타원체 예측 집합 | Oral |
| 3 | [Impossibility of Distribution-Free Predictive Inference for Individual Treatment Effects](https://neurips.cc/virtual/2026/poster/149451) | 개별 처치효과에 대한 distribution-free 예측 추론의 불가능성 증명 | Oral |
| 4 | [probly: Uncertainty-Aware Machine Learning](https://neurips.cc/virtual/2026/poster/139766) | 불확실성 인지 ML을 위한 모듈형 파이썬 패키지 probly | Oral |
| 5 | [Testable and Actionable Calibration for Full Swap Regret](https://neurips.cc/virtual/2026/poster/148311) | swap regret에 대해 actionable하고 testable한 보정 지표 SCDL | Oral |
| 6 | [Calibration without Ground Truth](https://neurips.cc/virtual/2026/poster/152525) | 정답 라벨 없이 약한 참조 모델로 강한 모델을 보정하는 후처리 프레임워크 | Spotlight |
| 7 | [Causal Discovery over Clusters of Variables in Non-Markovian Systems](https://neurips.cc/virtual/2026/poster/152473) | 비마르코프 시스템에서 변수 클러스터 간 인과 발견 알고리즘 | Spotlight |
| 8 | [Corrected Integrated Laplace Approximation for Bayesian Inference in Latent Gaussian Models](https://neurips.cc/virtual/2026/poster/154255) | 잠재 가우시안 모델의 ILA 오차를 importance sampling으로 보정 | Spotlight |
| 9 | [Environment-Robust Representation Learning with Empirical Bayes](https://neurips.cc/virtual/2026/poster/151010) | Empirical Bayes로 환경 변화에 강건한 표현을 학습 | Spotlight |
| 10 | [FMMI: Flow Matching Mutual Information Estimation](https://neurips.cc/virtual/2026/poster/148155) | normalizing flow로 상호정보량을 추정하는 FMMI | Spotlight |
| 11 | [Learning Gaussian Conditional Distributions using Neural Ratio Estimation is Hard](https://neurips.cc/virtual/2026/poster/149465) | Neural Ratio Estimation이 가우시안 조건분포 학습에서 비효율적임을 증명 | Spotlight |
| 12 | [Nearly Optimal Robust Covariance and Scatter Matrix Estimation Beyond Gaussians](https://neurips.cc/virtual/2026/poster/149150) | 타원 분포에 대한 준최적 강건 공분산/산란 행렬 추정 | Spotlight |
| 13 | [Neural Dual Bounds: Valid-by-Construction JGLP Warm-Starts for MAP and Constrained MAP](https://neurips.cc/virtual/2026/poster/150753) | 신경망으로 MAP 추론 상계의 warm-start를 만드는 Neural Dual Bounds | Spotlight |
| 14 | [On the Tightness and Computational Tractability of Higher-Dimensional Confidence Sequences](https://neurips.cc/virtual/2026/poster/154185) | 고차원 confidence sequence의 tight하고 계산 가능한 외부 근사 | Spotlight |
| 15 | [Optimal Subgroup Discovery at Every Support Threshold](https://neurips.cc/virtual/2026/poster/149258) | 지지도 임계값 전 구간에서 KL 최적 subgroup을 찾는 이론과 알고리즘 | Spotlight |
| 16 | [Post-ADC Inference: Valid Inference After Active Data Collection](https://neurips.cc/virtual/2026/poster/151721) | 능동 데이터 수집 이후에도 유효한 선택적 추론 프레임워크 | Spotlight |
| 17 | [Reconciling Causality and Non-Equilibrium Thermodynamics with Hamiltonian Causal Models](https://neurips.cc/virtual/2026/poster/150701) | 해밀토니안 인과 모델로 인과성과 비평형 열역학 통합 | Spotlight |
| 18 | [Robust Satisficing Ensemble: Scalable Model Aggregation Under Distribution Shifts](https://neurips.cc/virtual/2026/poster/149478) | 분포 이동에 강건한 robust satisficing 앙상블 RSE | Spotlight |
| 19 | [Sort, Partition, Randomize: Optimal Binary Hypothesis Testing under Local Differential Privacy](https://neurips.cc/virtual/2026/poster/152035) | 국소 차분 프라이버시 하 최적 이진 가설검정 메커니즘 구조(SPR) | Spotlight |
| 20 | [The Score Kalman Filter](https://neurips.cc/virtual/2026/poster/149695) | score matching과 Stein 항등식 기반 비선형 필터 Score Kalman Filter | Spotlight |
| 21 | [Two Phase Rapid Simulation Based Inference with Differentiable Simulators](https://neurips.cc/virtual/2026/poster/153417) | Schrödinger bridge 기반 두 단계 simulation-based inference RSBI | Spotlight |
| 22 | [What the Geometry of Good Models Tells Us](https://neurips.cc/virtual/2026/poster/155858) | 노이즈가 Rashomon set과 단순 모델 존재를 유도하는 기하 분석 | Spotlight |

## LLM 에이전트·도구 사용

| # | 제목 | 한 줄 요약 | 형식 |
|---:|---|---|---|
| 1 | [AgentAbstain: Do LLM Agents Know When Not to Act?](https://neurips.cc/virtual/2026/poster/139558) | LLM 에이전트가 행동을 멈춰야 할 때를 아는지 평가하는 AgentAbstain 벤치마크 | Oral |
| 2 | [APS: Bias-Controlled Adaptive Prototype Simulation for Population-Scale LLM Agents](https://neurips.cc/virtual/2026/poster/149524) | 인구 규모 LLM 에이전트 시뮬레이션을 프로토타입 기반으로 확장하는 APS | Oral |
| 3 | [Can LLM Agents Respond to Disasters? Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations](https://neurips.cc/virtual/2026/poster/139774) | 재난 대응 지리공간 추론 에이전트 벤치마크 DORA | Oral |
| 4 | [Computer Use at the Edge of the Statistical Precipice](https://neurips.cc/virtual/2026/poster/151946) | 컴퓨터 사용 에이전트 평가의 통계적 함정과 DigiWorld 벤치마크 | Oral |
| 5 | [ExComm: Exploration-Stage Communication for Error-Resilient Agentic Test-Time Scaling](https://neurips.cc/virtual/2026/poster/154319) | 탐색 단계 통신으로 오류 전파를 막는 에이전트 test-time scaling ExComm | Oral |
| 6 | [Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing](https://neurips.cc/virtual/2026/poster/152494) | 가설 검정 신뢰성을 위해 RL로 학습한 LLM 에이전트 Fisher-R1과 P-Bench | Oral |
| 7 | [Inductive Deductive Synthesis: Enabling AI to Generate Formally Verified Systems](https://neurips.cc/virtual/2026/poster/150230) | 구현과 증명을 함께 합성해 검증된 분산 시스템을 생성하는 에이전트 IDS | Oral |
| 8 | [Self-Programmed Execution for Language-Model Agents](https://neurips.cc/virtual/2026/poster/155631) | 모델 출력 자체가 오케스트레이터 프로그램인 self-programmed execution | Oral |
| 9 | [SMART: Scalable Multi-Agent Role-conditioned Teaming via LLM-free Tree Search](https://neurips.cc/virtual/2026/poster/149874) | LLM 없는 MCTS로 대규모 에이전트 풀에서 역할별 팀 구성 SMART | Oral |
| 10 | [Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents](https://neurips.cc/virtual/2026/poster/154927) | 형식 검증된 계획과 런타임 강제로 안전한 LLM 에이전트 Soteria | Oral |
| 11 | [Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction](https://neurips.cc/virtual/2026/poster/155649) | 임베딩 검색 대신 grep 등 터미널 도구로 코퍼스를 직접 탐색하는 에이전트 검색 DCI | Spotlight |
| 12 | [ECHO: Terminal Agents Learn World Models for Free](https://neurips.cc/virtual/2026/poster/154932) | 터미널 관측 토큰 예측 보조 손실로 CLI 에이전트 RL을 개선하는 ECHO | Spotlight |
| 13 | [Embedded-Arena: Building Hardware-in-the-Loop Coding Agents to Run AI on Microcontrollers](https://neurips.cc/virtual/2026/poster/149789) | 실제 하드웨어 피드백으로 MCU용 AI를 최적화하는 코딩 에이전트 아레나 | Spotlight |
| 14 | [ExperiGen: Agentic Hypothesis Discovery from Observational Data](https://neurips.cc/virtual/2026/poster/149912) | 관측 데이터에서 통계적으로 검증된 가설을 찾는 2-에이전트 ExperiGen | Spotlight |
| 15 | [Knowing When to Ask: Segment-Level Credit Assignment for LLM Tool Use](https://neurips.cc/virtual/2026/poster/149224) | segment 단위 credit assignment로 도구 호출 시점을 학습하는 CARL | Spotlight |
| 16 | [Mecha-nudges for Machines](https://neurips.cc/virtual/2026/poster/156000) | AI 에이전트의 선택을 유도하는 환경 변화(mecha-nudge)를 bit 단위로 측정 | Spotlight |
| 17 | [NeSyKC: Neurosymbolic Knowledge Compilation For Lifelong Learning Embodied Agents](https://neurips.cc/virtual/2026/poster/156109) | 선언적 지식을 절차적 지식으로 컴파일하는 평생학습 임바디드 에이전트 | Spotlight |
| 18 | [Norm Enforcement for AI Agents: Robustly Shaping Behavior in Multi-Agent Systems](https://neurips.cc/virtual/2026/poster/151090) | LLM 에이전트 다중 환경에서 악용에 강한 규범 집행 메커니즘 설계 | Spotlight |
| 19 | [RAOP: Step-Level Resource Orchestration for LLM Agents across Edge and Cloud](https://neurips.cc/virtual/2026/poster/152497) | 엣지-클라우드 LLM 에이전트 단계별 자원 오케스트레이션 RAOP (GRPO) | Spotlight |
| 20 | [SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://neurips.cc/virtual/2026/poster/151264) | frozen 에이전트를 위한 스킬 문서 텍스트 공간 최적화 SkillOpt | Spotlight |
| 21 | [VisInteract: Towards Dynamic Interactive Text-to-Visualization under Imperfect Queries](https://neurips.cc/virtual/2026/poster/148995) | 불완전 질의 하 대화형 Text-to-Vis 벤치마크와 Vis-MCTS | Spotlight |

## 효율 모델·시스템

| # | 제목 | 한 줄 요약 | 형식 |
|---:|---|---|---|
| 1 | [Bridging Compute- and Data-Optimal Pretraining](https://neurips.cc/virtual/2026/poster/155350) | compute-optimal과 data-optimal을 잇는 Compute-Data 스케일링 법칙 | Oral |
| 2 | [Felid: A Flexible and Efficient Design for Transformer Fine-Tuning over Encrypted Data](https://neurips.cc/virtual/2026/poster/148321) | 암호화 데이터 위 트랜스포머 파인튜닝을 8배 빠르게 하는 FHE 설계 Felid | Oral |
| 3 | [Fractional State Space Transition for Long Sequence Modeling](https://neurips.cc/virtual/2026/poster/150427) | 분수 동역학 기반 멱법칙 장기 기억의 SSM 아키텍처 FRAC | Oral |
| 4 | [HeMeR: Heterogeneous Memory Reconciliation for Embodied Agents via Structured KV Reuse](https://neurips.cc/virtual/2026/poster/148497) | 구조적 KV 재사용으로 임바디드 에이전트 메모리 추론을 가속하는 HeMeR | Oral |
| 5 | [Pruning and Distilling Mixture-of-Experts into Dense Language Models](https://neurips.cc/virtual/2026/poster/150472) | MoE 모델을 가지치기·증류로 dense 언어 모델로 변환 | Oral |
| 6 | [A Bitter Lesson for Data Filtering](https://neurips.cc/virtual/2026/poster/155947) | 대규모 연산 환경에서는 데이터 필터링이 불필요하며 저품질 데이터도 성능을 높임을 보인 스케일링 연구 | Spotlight |
| 7 | [Basis-Mediated Bilinear Attention: A New Method for Greatly Reducing Query--Key Pathway Parameters](https://neurips.cc/virtual/2026/poster/154941) | Query-Key 경로 파라미터를 최대 95% 줄이는 Basis-Mediated Bilinear Attention | Spotlight |
| 8 | [Beyond Selection: Token Parameterization for Extreme Visual Token Compression](https://neurips.cc/virtual/2026/poster/151663) | 파라미터화 관점의 극단적 시각 토큰 압축 코더 Braco | Spotlight |
| 9 | [Breaking Information Islands in Sparse Tuning via Small-World Connectivity](https://neurips.cc/virtual/2026/poster/155451) | small-world 연결성으로 information island를 깨는 희소 파인튜닝 SWIFT | Spotlight |
| 10 | [CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection](https://neurips.cc/virtual/2026/poster/153990) | chunked prefill 가속을 위한 Block-Union KV 선택 CompactAttention | Spotlight |
| 11 | [D-PACE: Dynamic Position-Aware Cross-Entropy for Parallel Speculative Drafting](https://neurips.cc/virtual/2026/poster/152718) | 기대 수락 길이에서 유도한 위치별 가중 손실로 병렬 speculative drafting 개선 | Spotlight |
| 12 | [Exact Flow Linear Attention: Exact Solution from Continuous-Time Dynamics](https://neurips.cc/virtual/2026/poster/154073) | delta-rule 선형 어텐션을 연속시간 정확해로 푸는 Exact Flow Linear Attention | Spotlight |
| 13 | [FeatCal: Feature Calibration for Post-Merging Models](https://neurips.cc/virtual/2026/poster/152364) | 특징 드리프트를 줄이는 모델 병합 후 레이어별 보정 FeatCal | Spotlight |
| 14 | [Grid Games: The Power Of Multiple Grids for Quantizing Large Language Models](https://neurips.cc/virtual/2026/poster/153337) | 다중 4-bit grid 선택으로 LLM 양자화 정확도를 높이는 Grid Games | Spotlight |
| 15 | [nnTrace: Detecting and Localizing Silent Bugs in Distributed Training](https://neurips.cc/virtual/2026/poster/154832) | 분산 학습의 silent bug를 탐지·위치 추적하는 차분 테스트 시스템 nnTrace | Spotlight |
| 16 | [Orthrus: Memory-Efficient Parallel Token Generation via Dual-View Diffusion](https://neurips.cc/virtual/2026/poster/150719) | dual-view 확산으로 무손실 병렬 토큰 생성을 달성하는 Orthrus | Spotlight |
| 17 | [Quantile Benchmarking Heterogeneous Web Corpora in Open LLM Pretraining](https://neurips.cc/virtual/2026/poster/149953) | 웹 코퍼스 quantile benchmarking으로 open LLM 사전학습 top-p 혼합 비율 결정 | Spotlight |
| 18 | [Reinforced Fast Weights via Next-Sequence Prediction](https://neurips.cc/virtual/2026/poster/154908) | fast weight 모델에 next-sequence prediction과 GRPO를 적용한 ReFINE | Spotlight |
| 19 | [TreeGraft: Adaptive Multi-Drafter Grafting for Tree-Based Speculative Decoding](https://neurips.cc/virtual/2026/poster/151038) | 다중 drafter를 접목하는 tree 기반 speculative decoding TreeGraft | Spotlight |

## LLM 추론·RL 후처리

| # | 제목 | 한 줄 요약 | 형식 |
|---:|---|---|---|
| 1 | [Escaping the Cognitive Well: Efficient Competition Math with Off-the-Shelf Models](https://neurips.cc/virtual/2026/poster/150429) | Cognitive Well을 피하는 추론 파이프라인으로 저비용 IMO급 수학 풀이 | Oral |
| 2 | [Nemotron-Cascade: Scaling Cascaded Reinforcement Learning for General-Purpose Reasoning Models](https://neurips.cc/virtual/2026/poster/155022) | 도메인별 순차 RL로 범용 추론 모델을 만드는 Nemotron-Cascade | Oral |
| 3 | [Quantized Reasoning Models Think They Need to Think Longer, but They Do Not](https://neurips.cc/virtual/2026/poster/151668) | 양자화된 추론 모델의 overthinking 오류 분석과 training-free logit penalty | Oral |
| 4 | [A Theoretical Analysis of Test-Driven Code Generation](https://neurips.cc/virtual/2026/poster/149483) | 테스트 기반 코드 생성의 선택 및 backprompting에 대한 이론적 분석 | Spotlight |
| 5 | [Backtracking with Linear-in-Depth Search-Space Growth: Width-Limited Tree Search for Large Language Models](https://neurips.cc/virtual/2026/poster/155253) | 선형 깊이 성장의 Width-Limited Tree Search로 LLM 추론 시간 탐색 개선 | Spotlight |
| 6 | [FrontierSmith: Synthesizing Open-Ended Coding Problems at Scale](https://neurips.cc/virtual/2026/poster/151843) | 닫힌형 코딩 문제를 open-ended 문제로 진화시켜 LLM 코더를 학습하는 FrontierSmith | Spotlight |
| 7 | [G-Zero: Self-Play for Open-Ended Generation from Zero Data](https://neurips.cc/virtual/2026/poster/152249) | 검증기 없이 hint 기반 내재 보상으로 LLM이 자기 진화하는 G-Zero | Spotlight |
| 8 | [MUX: Continuous Reasoning via Multiplexed Tokens](https://neurips.cc/virtual/2026/poster/151022) | 추론 토큰을 연속 multiplexed 잠재 토큰으로 증류하는 MUX | Spotlight |
| 9 | [Negative-Only Policy Optimization for One-Sided Verifiable Rewards](https://neurips.cc/virtual/2026/poster/152610) | 한쪽만 검증 가능한 보상에서 negative만 억제하는 NOPO | Spotlight |
| 10 | [Self-Distilled RLVR](https://neurips.cc/virtual/2026/poster/152431) | RLVR에 self-distillation 토큰 단위 신호를 결합한 RLSD | Spotlight |
| 11 | [STAR-Math: Multi-Agent Mathematical Reasoning under Persistent Meta-Strategic Supervision](https://neurips.cc/virtual/2026/poster/150935) | 메타 전략 감독을 갖춘 멀티에이전트 수학 추론 STAR-Math | Spotlight |
| 12 | [The Master Key Hypothesis: Unlocking Cross-Model Capability Transfer via Linear Subspace Alignment](https://neurips.cc/virtual/2026/poster/152307) | 선형 부분공간 정렬로 모델 간 추론 능력을 전이하는 UNLOCK | Spotlight |

