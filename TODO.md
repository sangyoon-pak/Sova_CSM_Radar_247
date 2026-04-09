
### UI
 
- EN/KR layout is different.  




### Agent Utility 
- Build a notification pipeline (decide channels and triggers) so the system can notify when drafts are ready or when errors occur.

- need to handle the language dynamically. when asked in korean, doc retrieve can retrieve the data regardless of the language but output should be in the language it was asked in (both email probe and user <> interaction, the final output should be in the language the query is asked in)

- **In progress / shipped in code**: Proactive CSM assistant (not draft-first). System prompt + probe message now prioritize triage, product vs account classification, KB retrieval for product threads, **action items + suggested answers**; **full email drafts only on explicit user request**. **Action dashboard** is its own top-level UI tab (hash `#action-dashboard`), backed by `GET /dashboard/probe-runs` (filters, pagination). Thread probes can **Open thread**; every run has **View in Run history**. Auto-refresh every 60s while that tab is active.
- Shifting from email drafting agent to proactive assistant CSM agent (product vision). Remaining: richer structured dashboard rows, browser tab counts / push (see below).
1) periodically probe inbox and analyse the queries (cron jobs) — **cron still runs `PROBE_TRIGGER_MESSAGE`;** message now asks for a markdown **## CSM action board** section.
2) Agent should sense Appier-product client questions, search docs, list actions for CSM, suggest answers; **draft email only when asked** — **reflected in `EMAIL_AGENT_SYSTEM_TEMPLATE`.**
2-1) Actionable dashboard — **v1** on dedicated tab with server-filtered probe runs; redundant-email skip remains **prompt-driven**. Future: structured JSON rows per email, tab badge counts.
2-2) agent should take actions and brief csms depending on the default language set. we do have KR/EN to choose between on the UI but that is only for the front-end presentation. For example,  if the client query is in en, agent should brief in english. If it is korean,  agent should brief in korean  
2-3) we have deployed for agent's self-evolution by users feedback on history. I think we should do that on the actionboard.
2-4) agent is creating redundant task for the same email thread when probing.. If it is the same email thread but updated as with newer email message, we should just update on the same task thread on the dashboard. 
2-5) action dashboard still remains alive when user deletes the thread on workbench. this should be synced. 
2-6) for the task cards on the actionboard, we should also include who is the client or at least client email domain so that we will know. 




3) Agent should be able to nofify the CSM. I think the best way is to notify CSM through the web browser push. I have web push notification muted still, I can tell if there is something on my email inbox on the top of the browser tab with the number within parenthesis (). 

- cron job can be either set by users asking agent to set the cron job itself or users can manually set cron jobs on the UI e.g) I want you to probe email every 3 hours and get back to me with the drafted version of action items with the relevant documents that could answers the client email inquries. 
- move the agent software using from docs from /data to upload completely for retrieval pipeline. 




## wrap-up 
- appier related documents should not be exposed on the repo
- clean up the irrelevant files (test files, etc)
- do not push knowledge-base file to public github repo. mark it so that it won't be part of the push. 
- any important variables (API tokens etc) should not be exposed on the repo.
- update the md files that shows how to install this software package including external dependencies that requires users to install and configure such as API tokens, gogcli, and open router part. Include general guide line if openrouter is not an option for some users.  
- update the md files as for how the retrieval works and why this way can be business critical and sustainable. 
- update the md files as for how the agent self evolves. 
- the UI should include what this software is all about and what it is aiming to do to help CSM concisely can take reference from md files. 
- should include how to install all the dependencies and set variables (e.g API keys) on the MD file.  
- pack up the code to run in the container. 
- update the md files as for how the agent self evolves.  
-

