# Candidate profile — Dhruv Singh (nickname: Bhidu)

Last updated: 2026-11-18
Source of truth for every resume, form answer and email. Only facts the candidate confirmed go here. Unknowns are marked **TODO**.
Sources: resume PDF (`inputs/Dhruv_resume_original.pdf`) and onboarding form answers (`inputs/dhruv-onboarding-answers.json`, 2026-11-18).

## Identity and contact
- Full name: Dhruv Singh
- Professional email (use on every portal): dhruvsingh1605@gmail.com
- Secondary email (only where an account already uses it): footballfreez11@gmail.com
- Phone: +91-7217861673
- Current city: Gurgaon
- Full postal address (for forms): 879, Chander Boys n Girls PG, Saraswati Vihar, New Maruti Housing Colony, Gurugram, Haryana, 122002
- Date of birth (for forms): 16 May 2003 (include in forms: yes)
- Gender (for forms): Male (include in forms: yes)
- Nationality / passport held: passport held: Yes. Nationality: **TODO** (assumed Indian, not stated)
- Work authorisation / needs sponsorship: needs sponsorship: Yes (confirmed by Dhruv 2026-11-18)

## Links
- LinkedIn: https://www.linkedin.com/in/dhruv-singh-78a503203
- GitHub: https://github.com/Dhruvsingh1605
- Portfolio / website: none
- Papers / patents: none

## Experience numbers (state exactly like this)
- Resume and forms headline figure: "18+ months" (chosen by Dhruv; true when internships are counted)
- Full-time experience for forms: 1.4 years (Dhruv's figure)
- Including internships for forms: 2.1 years (Dhruv's figure)
- **TODO CONFIRM:** the dates imply roughly 1.2 years full-time (Timble, Sep 2025 – now) and about 1.8 years with the two internships (about 7 months). Earlier in chat Dhruv said 1.3 years. Forms may be cross-checked against employer dates, so confirm the exact numbers.
- Current title (always use the latest): AI Engineer
- Team leadership: none stated

## Work experience (newest first)
### AI Engineer — Timble Technologies Pvt. Ltd (fintech company providing AI solutions to banks and NBFCs)
- Dates: Sep 2025 – Present | Gurgaon | Onsite | Full-time
- Primary work (built by Dhruv):
  - Bank Statement Analyzer: 10,000+ transactions/day, OCR + NLP pipelines; manual review -60%, credit turnaround -35%.
  - Neo4j Knowledge Graph engine for batch relationship mapping; Cypher queries and XGBoost/LSTM ensembles to detect AML patterns, round-tripping and fund trailing across multi-entity statements.
  - Django-based ML serving endpoints with A/B testing for model benchmarking; optimized AWS data pipelines with Docker to reduce inference latency.
  - **New (not yet on the resume):** realtime talking voice-calling agent for sales and marketing, with realtime tool calls and a TTS + STT transcription pipeline. No metrics given (**TODO** ask for any).
- Clients / domain: banks and NBFCs (client names may be mentioned freely, per Dhruv)

### MLOps Engineer — Dataviv Technologies Pvt. Ltd (AI edtech company, Gurugram)
- Dates: Jun 2025 – Sep 2025 | Gurgaon | Mode: **TODO** | **Internship** (per Dhruv)
- Bullets:
  - Real-time speech-to-speech system integrating STT, Llama 3 8B, TTS and Wav2Lip in a microservice architecture, deployed via REST API and WebRTC.
  - Sub-100ms latency via async pipelines, audio chunking and INT8/FP16 quantization (bitsandbytes + PEFT); inference cost -40% vs proprietary model alternatives.
  - Full MLOps lifecycle with MLflow, DVC, Docker and CI/CD for reproducible one-click deployments.
  - Async architecture with Redis Pub/Sub and FAISS vector search for context-aware LLM responses.
- Note: the resume says "LLaMA-3 7B"; Dhruv confirmed it was Llama 3 8B. Fix on the rebuilt resume.
- Stipend: **TODO**

### Machine Learning Engineer — Gfuture Tech Pvt. Ltd (AI and blockchain company, Ahmedabad)
- Dates: Jan 2025 – Apr 2025 | Ahmedabad | Mode: **TODO** | **Internship** (per Dhruv)
- Bullets:
  - AI medical assistant with Gemini 1.5 Flash, TensorFlow and Scikit-Learn, REST API deployment, benchmarked with a precision/recall/F1 evaluation suite.
  - Fine-tuned Qwen 2.5-Math with QLoRA and bitsandbytes quantization, improving mathematical reasoning accuracy on GSM8K and reducing inference overhead (no numbers available; keep the wording qualitative).
  - Automated ML pipelines with MLflow and Docker; deployment time -50%.
- Stipend: **TODO**

## Projects (outside work)
| Project | Role | Stack | Key metric | Link |
|---|---|---|---|---|
| LawYer: Advanced AI Legal Assistant (RAG + GraphRAG) | Builder | FAISS, LangChain, LLMs, MLflow | 50,000+ legal docs; hallucinations -30%; Precision@5 87% | https://github.com/Dhruvsingh1605/LawYer |

- LawYer bullets: RAG pipeline over 50,000+ legal documents (hallucinations -30% via factual grounding); hybrid retrieval (BM25 + vector) with Precision@5 87%; GraphRAG with entity-relation graphs for multi-hop reasoning; reranking, query rewriting and context optimization benchmarked with RAGAS.
- **Status: local only, NOT deployed.** Never describe LawYer as deployed, live or running in production in forms, emails or messages. The current resume says "production-grade"; reword on the rebuilt resume (e.g. "end-to-end RAG pipeline").

## Education
- B.Tech, Computer Science and Engineering — Parul Institute of Engineering and Technology — 2021–2025 — CGPA 7.68
- Roll / enrolment number (only if forms ask): **TODO** (the form field was filled with the college name instead)
- Class 12: 72.3% | Class 10: 75%

## Awards, publications, patents, certifications
- Certifications: Supervised Machine Learning (Coursera, Andrew Ng); Data Analysis with Python (FreeCodeCamp); Python Basic & Intermediate (HackerRank); Problem Solving (HackerRank)
- Awards / publications / patents: none

## Languages
- English: fluent (professional) | Hindi: fluent (native)

## Skills — honesty buckets
Dhruv marked ALL skills below as Confirmed on 2026-11-18, including the 16 I had flagged as doubtful (Kubernetes, Kafka, Airflow, DeepSpeed, GGUF/GPTQ, vLLM, SageMaker, GCP BigQuery/Vertex AI, WebRTC, Java, C, Guardrails, OpenCV, TensorFlow, Weights & Biases, Agentic Workflows). Recorded as he said. Be ready to defend each one in interviews; if any is shaky, move it to Limited here and the agent will keep it out of bullets.

### Confirmed hands-on (bullets, forms, emails OK)
- Languages: Python, SQL, Java, C
- LLM and NLP: RAG, GraphRAG, Prompt Engineering, Guardrails, LLM Evaluation (RAGAS), Agentic Workflows, LangChain, LlamaIndex, Semantic Search, BM25, Reranking
- Model training: QLoRA, LoRA, PEFT, bitsandbytes quantization, GGUF/GPTQ, DeepSpeed, mixed-precision training, distributed fine-tuning
- MLOps and infra: MLflow, DVC, Docker, Kubernetes, GitHub Actions CI/CD, FastAPI, Redis Pub/Sub, asyncio, WebRTC, FAISS, Weights & Biases
- Frameworks: PyTorch, TensorFlow, Hugging Face Transformers, Scikit-Learn, OpenCV, vLLM
- Cloud and data: AWS (S3, EC2, SageMaker), GCP (BigQuery, Vertex AI), MongoDB, PostgreSQL, Airflow, Kafka
- From experience bullets: OCR, Neo4j, Cypher, XGBoost, LSTM, Django, STT/TTS, Wav2Lip, Gemini 1.5 Flash, Qwen 2.5-Math, Llama 3
### Limited (Skills section only, never in bullets)
- none
### Never claim (not used; prepare an honest interview answer)
- none

## Framing notes
- Preferred framing of key projects: LawYer is a local project; call it an "end-to-end RAG pipeline", not "production" or "deployed".
- Things never to mention in applications: none specified
- Product/vendor names: brand names (Gemini, Llama, Qwen) are fine.
- Gfuture and Dataviv were internships. Title wording on the resume stays as Dhruv wrote it, but if a form asks employment type, answer "Internship".

## Headline metrics (quick lookup)
- Bank Statement Analyzer: 10,000+ transactions/day; manual review -60%; credit turnaround -35%
- Speech-to-speech: sub-100ms latency; inference cost -40%
- ML pipelines at Gfuture: deployment time -50%
- LawYer RAG: 50,000+ docs; hallucinations -30%; Precision@5 87%
