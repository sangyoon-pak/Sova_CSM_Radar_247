---
source: notebooklm_export
file_id: "050"
filename: "050_[AI Agent] Differentiators of Audience and Campaign Agents_Architecture.pdf.txt"
doc_type: "product_overview"
product: "AI Agent"
content_type: "pdf"
language: "en"
guide_summary: "The provided excerpts detail the sophisticated architecture and key differentiators of specialized AI Agents designed for marketing, focusing heavily on data governance and reliability. The system ensures data integrity through the **Data Quality Booster (DQB)** and utilizes **AEP** as a unified data lake, providing the Large Language Models (LLMs) a single, clean source of truth. To generate precise outcomes, the agents leverage **In-Context Learning/RAG** to incorporate customer context, unive"
guide_keywords: "Data Context Retrieval, Data Quality Assurance, Risk Mitigation Strategy, Agent Performance Testing, Agent Architecture Differentiators"
---

# 050 [AI Agent] Differentiators of Audience and Campaign Agents Architecture.pdf

Differentiators of Audience and Campaign 
Agents
User Profile 
Offline Event 
Online Event 
Product feed 
Campaign Setting 
Performance Data 
DQB 
AEP 
Customer data 
(1) DQB (Data Quality Booster) ensures data onboarded to the data lake is clean and meaningful, avoiding garbage-in-garbage-out. 
(2) AEP serves as a shared data lake among AIRIS, AIQUA, and BotBonnie, ensuring the LLM accesses a single source of truth without data latency. 
Differentiators Core model 
How does Audience Agent work? What Makes it Different?
LLMs 
User Profile 
Offline Event 
Online Event 
Product feed 
Campaign Setting 
Performance Data 
DQB 
Model Selector 
In-Context Learning/RAG 
AEP 
Differentiators Core model 
(1) Use In-Context Learning and RAG to help the LLM access and understand customer data context. 
(2) Model selector routes each user query to the most appropriate LLM model. 
How does Audience Agent work? What Makes it Different?
Techniques What is it? How does it work? Analogy Requires Model Training? 
Uses External Data? 
In-Context Learning 
Teaching the model a new task just by showing a few examples directly in the prompt—no retraining required. 
You paste example input-output pairs (like "cat ➔ 貓"), then add a new one and the model figures out how to respond based on those. 
Quick experiments or one-off recipes—no time for deep prep. 
No No 
Fine-Tuning Retraining the model's parameters on a specific dataset to specialize it further for your task. 
You provide lots of labeled data, and the model "learns" new patterns or knowledge that become part of its memory. 
Building a go-to specialist (e.g., gyoza-only chef). 
Yes No 
RAG (Retrieval- Augmented Generation) 
hybrid approach: Instead of relying only on what the model "remembers," it searches external data (like documents or databases) and combines those facts with its own generated text. 
When asked a question, the system first looks up relevant documents, then uses the model to summarize or answer using that information. 
Recipes needing fresh facts (e.g., No-pork restriction). 
Sometimes Yes 
In-Context Learning vs. Fine-Tuning vs. RAG 
LLMs 
User Profile 
Offline Event 
Online Event 
Product feed 
Campaign Setting 
Performance Data 
DQB 
Model Selector 
Expert Insights 
Universal Principles 
Industrial Best Practices 
Best Practices 
AI Prediction (configuration) 
In-Context Learning/RAG 
AI Prediction 
AEP 
Differentiators Core model 
(2) AI prediction models create more accurate segments for marketing scenarios. 
(1) Three-fold Best Practices - Expert Insights: Scenario-specific guidelines from trained data analysts 
- Universal Principles 
- Industry Best Practices from 145 AIQUA case playbooks 
How does Audience Agent work? What Makes it Different?
LLMs 
User Profile 
Offline Event 
Online Event 
Product feed 
Campaign Setting 
Performance Data 
DQB 
Model Selector 
Expert Insights 
Universal Principles 
Industrial Best Practices 
Best Practices 
AI Prediction (configuration) 
In-Context Learning/RAG 
AI Prediction 
Back-Testing 
AEP 
Differentiators Core model 
(1) Back-Testing: uses historical data to test performance before replying to users, e.g. best testing CVR with the segmentation conditions. 
How does Audience Agent work? What Makes it Different?
LLMs 
User Profile 
Offline Event 
Online Event 
Product feed 
Campaign Setting 
Performance Data 
DQB 
Model Selector 
Expert Insights 
Universal Principles 
Industrial Best Practices 
Best Practices 
AI Prediction (configuration) 
In-Context Learning/RAG 
AI Prediction 
Back-Testing 
AEP 
Hallucinations Reduction by Risk-Awareness 
Decisions 
StreamBench for Agent self-evolving 
Guardrails in every step 
Query 
Response 
Differentiators Core model 
Guardrails in every step to 1. Avoid agent provides PII to users 2. Avoid answer irrelevant questions 3. Avoid answer questions supposed to be answered by other agents. 
How does Audience Agent work? What Makes it Different?
LLMs 
User Profile 
Offline Event 
Online Event 
Product feed 
Campaign Setting 
Performance Data 
DQB 
Model Selector 
Expert Insights 
Universal Principles 
Industrial Best Practices 
Best Practices 
AI Prediction (configuration) 
In-Context Learning/RAG 
AI Prediction 
Back-Testing 
AEP 
Hallucinations Reduction by Risk-Awareness 
Decisions 
StreamBench for Agent self-evolving 
Guardrails in each step 
Query 
Response 
How does Audience Agent work? What Makes it Different? 
Differentiators Core model
Five Super Power Makes Appier's AI Agent Stand Out 
Data Quality Booster 
AI Prediction 
Best-Testing historical data 
Risk-Awareness Decisions 
Keep Self-evolving 
Avoid garbage in garbage out 
Users likely to purchase 
Self-evaluation before replying 
Reduce Hallucinations 
By StreamBench technique
LLMs 
User Profile 
Offline Event 
Online Event 
Product feed 
Campaign Setting 
Performance Data 
DQB 
Model Selector Image Generation 
(configuration) 
In-Context Learning/RAG 
Stock Image Generation model 
Back-Testing 
20+ Journey Templates 
AEP 
Hallucinations Reduction by Risk-Awareness 
Decisions 
StreamBench for Agent self-evolving 
Guardrails in each step 
Query 
Response 
How does Campaign Agent work? What Makes it Different? 
Differentiators Core model
APPENDIX
How does Campaign Agent work? Model training, understand and answer questions. 
Client's first-party data onboarded to 
the AQ/AR 
 
 
Client's historical campaign 
performance data 
User query 
LLM, not limited one model. (GPT, Gemini, 
Llama etc.) 
In context learning/RAG 
 
 
 
 
Risk-Aware Decision (reduce 
Hallucinations) Guardrails 
Response 
 
 
 
 
 
 
40+ Journey Map best practice
How does Audience Agent work? Model training, understand and answer questions. 
Client's first-party data onboarded to 
the AQ/AR 
 
 
Client's historical campaign 
performance data 
User query 
LLM, not limited one model. (GPT, Gemini, 
Llama etc.) 
In context learning/RAG 
 
 
 
 
Risk-Aware Decision (reduce 
Hallucinations), for most steps 
Response 
 
 
 
 
 
 
 
 
Back-testing 
Guardrails 1. 避免提供 PII 2. 避免回答不相關的問題 3. 如果問到其他 agent 才能回答的問題 etc. 4. 每次的回覆都會做 guardrails 
建議文案時，有作回測，過往發過的 50 個， 有哪些不是因為發送時間，或是折扣夠多， 減少 bias，而不只是因為成效好。 
量化的去看 quality 
groundedness, accuracy, risk 
 
 
Client's first-party data onboarded to 
the AQ/AR 
Pre-trained historical campaign data of all 
clients 
Client's historical campaign 
performance data 
User query 
LLM, not limited one model. (GPT, Gemini, 
Llama etc.) 
AI Models (Prediction) 
Risk-Aware Decision (reduce 
Hallucinations) Guardrails 
Response 
How does Audience Agent work? Model training, understand and answer questions. 
145 use cases 
In context learning 
Prompt engineering 
RAG 
General guideline 
Scenario-based
Workflow & Progress 
Retrieve best practice 
User rough intent 
Further gather intent and info based on the retrieved BP 
Generate Analysis Plan 
Data analysis (run query) 
Backtesting and validation (size, conversion) 
Pass 
Propose 3 cards with reasoning 
Fail Propose segment based on 
analysis plan 
Best Practices 
Universal Principles 
* Not scenario specific 
Expert Insights 
* = Deeper guidelines from DA * Scenario specific 
Industry Best Practices 
* = AQ case playbook (145 cases) * Only hardcode “3” cases 
If conflict: Highest priority 
Lowest priority 
As-is 
Implement this time 
Enhance this time 
Output more reasoning 
during tool call
 
Risk management: The most common issue in agents, which is faced by almost all vendors 
Risk Aware Decision - Introduction 
Hallucination / Risk 
Fact / Correct 
Policy adjustment (precision & recall) 
Hallucinations mitigation (the main risk) 
 Groundedness 
 Q3 goal: 90%, Q4 goal: 95% 
 Q3 progress: 83% → 93% ** 
 Approaches (keep imp.): Self reflection, two 
agents design, stage instruction 
Risk aware decision 
 Enable agent to quantify risks & 
uncertainties when making decision 
 Steps 
 Uncertainty & Risk quantification 
 Policy adjustment by risk level
