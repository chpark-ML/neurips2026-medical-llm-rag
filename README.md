# NeurIPS 2026 — 의료 QA·RAG·에이전트·LLM 논문 정리

NeurIPS 2026 채택 논문 9,094편을 분야·주제로 나누고, 의료 QA·의료 RAG·의료 에이전트·의료 LLM·RAG·on-policy/self-distillation 논문을 골라 정리했다.

## 웹 페이지

휴대폰에서도 열린다. 다섯 페이지는 서로 독립적이다.

| 페이지 | 내용 |
|---|---|
| [관심 분야 리포트](https://chpark-ml.github.io/neurips2026-medical-llm-rag/interests.html) | 학회 전체 → 분야 → 트렌드 → 의료·RAG 순서의 분석, 관심 분야 논문 목록, 하이라이트, 연구 제안 |
| [논문 탐색기](https://chpark-ml.github.io/neurips2026-medical-llm-rag/explorer.html) | 전체 9,094편을 분야·세부 주제(212개)·키워드·발표 형식으로 걸러 보기 |
| [Medical QA 연구 지도](https://chpark-ml.github.io/neurips2026-medical-llm-rag/medical_qa.html) | Medical QA 논문을 갈래로 나눈 연구 흐름 |
| [On-policy·Self-distillation 연구 지도](https://chpark-ml.github.io/neurips2026-medical-llm-rag/opsd.html) | OPD·OPSD 논문을 갈래로 나눈 연구 흐름 |
| [데이터셋 트랙 의료 논문](https://chpark-ml.github.io/neurips2026-medical-llm-rag/med_datasets.html) | Evaluations & Datasets 트랙의 의료 논문 60편을 데이터·평가 종류별 갈래로 정리 |

## 숫자로 보기

| 항목 | 편수 |
|---|---:|
| NeurIPS 2026 전체 | 9,094 |
| 관심 분야 (의료 100 · RAG 122, 일부 겹침) | 216 |
| On-policy·Self-distillation | 74 |
| 기존 의료 QA 벤치마크로 실험 (그중 의료 QA가 주 타깃) | 51 (10) |
| Oral·Spotlight (발표 형식을 아는 7,688편 중) | 405 |

## 주요 관찰

- **LLM 에이전트만 크게 커졌다.** 14개 분야 중 'LLM 에이전트·도구·검색'의 비중이 2.99% → 6.83%로 오차를 넘어 늘어난 유일한 큰 변화다.
- **의료는 작고 하이라이트가 적다.** 의료·헬스케어 분야는 2.79%이고, Oral·Spotlight 비율이 1.94%(4/206편)로 14개 분야 중 가장 낮다(학회 기준선 5.27%).
- **의료는 데이터셋 트랙에 몰린다.** Evaluations & Datasets 트랙 852편 중 60편(7.0%)이 의료로, Main 트랙(2.3%)의 약 3배다. 그중 28편이 의료 LLM 벤치마크다.
- **의료 LLM 연구의 질문이 '근거'로 옮겨갔다.** 의료×LLM 논문 중 근거·귀속·환각을 다루는 비율이 22.4% → 47.1%, 검색(RAG)은 3.9% → 16.5%.
- **RAG는 agentic search로 흡수되는 중이다.** 'RAG'라는 말을 쓰는 논문 비중은 그대로(×0.96)인데 deep research·search agent는 ×3.5.
- **MedQA 류 벤치마크 실험 논문 51편 중 대부분은 일반 LLM 논문이다.** 의료 QA 자체를 목표로 한 것은 10편이다.

## 파일

| 파일 | 내용 |
|---|---|
| [`REPORT.md`](REPORT.md) | 상세판: 분야·트렌드 표, 관심 분야별 연구 흐름, 216편·의료 QA 벤치마크 논문 목록과 성능 표, 연구 제안 |
| [`HIGHLIGHTS.md`](HIGHLIGHTS.md) | 학회 전체 Oral·Spotlight 405편, 분야별 |
| `interests.html`, `explorer.html`, `medical_qa.html`, `opsd.html`, `med_datasets.html` | 위 웹 페이지의 원본 |
| `data/` | 모든 집계와 분류 결과 (JSON·CSV). 파일별 설명은 REPORT.md 끝에 있다 |
| `scripts/` | 데이터 수집·분류·집계·페이지 생성 코드 |

## 어떻게 만들었나

- 원천: neurips.cc 공식 포스터 목록(2026 9,094편, 2025 5,860편)과 발표 형식 정보, 공개된 arXiv 본문.
- 분야·세부 주제·관심 분야 분류와 한 줄 요약은 LLM이 제목·초록(일부는 본문)을 읽고 붙였다. 사람이 검수하지 않았다.
- 트렌드는 주제별 키워드 정규식으로 센 비율이고, 하이라이트 비율에는 95% 신뢰구간을 함께 봤다.
- 의료 QA 벤치마크 실험 여부는 arXiv 본문을 읽어 판정했고, 성능 수치는 본문에 그대로 있는 값만 남겼다. arXiv 판이 없는 논문은 확인하지 못했다.

## 재현

```bash
bash scripts/fetch.sh && python3 scripts/decisions.py && python3 scripts/topic_trends.py && python3 scripts/highlights.py && python3 scripts/areas.py
python3 scripts/build.py && python3 scripts/explorer.py && python3 scripts/branchmap.py
```

LLM 판독 단계의 결과는 `data/`에 저장돼 있어, 위 명령만으로 페이지와 문서를 다시 만들 수 있다. 의료 QA 벤치마크 본문 검색은 `scripts/medqa_bench/`에 따로 있다.

