
## Solution Build MD file to build - Featured-based gaurdrailing for agent code build
1. Search Capability is based on docs/SEARCH_AGENT.md to build the features on top. This should be the very foundation for this agentic software. 
2. Some unfounded Agent behahaviours recurring that requires guirdrailing 
- Agent is not able to differentiate at times what are the CSM-related emails and create action cards for them or not. 
=> Maybe rather than hardcoding this, users should be able to give guidance on the UI so that agent can cater to users needs ?
- previously probed email is not part of action card creation although we deleted all the relevant backend data ? 
- on thread, even if threads are product-related thread, agent do not try to retrieve from uploaded documents. 

### MD files
- Agent architecture diagram. Users -> Agent -> subagent (Rag architecture, subquery engines, reranking etc) -> final agent -> answer
- update all the md files up to date synced with the current codebase and architectures
- update the md files that shows how to install this software package including external dependencies that requires users to install and configure such as API tokens, gogcli, and open router part. Include general guide line if openrouter is not an option for some users.  
- update the md files as for how the retrieval works and why this way can be business critical and sustainable. 
- update the md files as for how the agent self evolves. 

## UI
 - if openrouter is set via API, we should show the remaining credit balance on the top right corner regardless of different tabs. 
 - workbench thread time is not synced with the timezone set on configure. 
### landing page   


## Agent Utility 
### Rag
- 'API Push Campaign CID Inquiry' is not doing retrieval. why ? it called fetch_email_inbox but did not access RAG

- currently the documents are scraped from the RC webpage in a structured manner (parsed into a markdown). what if users just upload less-refined pdf/docs files ? would that work too ? 


### Action dashboard/action cards : 
- Quota exceeding notification email is only for the internal use. currently agent decides to delve into it and make a card. Maybe, it is because the product name mentioned. The content has no intent that requires CSM's action at all. how can we effectively and efficiently exlude it ? should work on query analysis sub agent ? 

- we have deployed for agent's self-evolution by users feedback on history. I think we should do that on the actionboard. Can we shift from users clicking likes/dislikes but actually give feedback to the agent in text by users themselves ? is this an ideal agent architecture ?

- action cards might not have all the retrieved data on the UI but it should have it as metadata so that when users ask more details, agent can directly answer

- for the task cards on the actionboard, we should also include who is the client or at least client email domain so that we will know. + We should include the title of email thread
- users should be able to change the status and view/sort  (in progress, completed, not started)

### Cron Jobs

- cron job can be either set by users asking agent to set the cron job itself or users can manually set cron jobs on the UI e.g) I want you to probe email every 3 hours and get back to me with the drafted version of action items with the relevant documents that could answers the client email inquries. 
- current cron tab is not user friendly. cron jobs are to probe at a set interval by users. We should improve UI and functionaliy ?




## pre-distribution
- appier related documents should not be exposed on the repo
- clean up the irrelevant files (test files, etc)
- do not push knowledge-base file to public github repo. mark it so that it won't be part of the push. 
- any important variables (API tokens etc) should not be exposed on the repo.

## distribution
- change the name to Sova - CSM - CSM Radar Agent 24/7 on the repository both on local and github
- make it available across mac/linux/windows via **host install** (venv + `run.py`); **not** container-first—`gog`/OAuth/keyring need a normal OS environment (see `docs/GMAIL_SETUP.md`).
- **Public docs UX:** one canonical **A–Z** is `docs/INSTALLATION.md` in-repo; expose it on **GitHub** (README link) and later a **docs website** so users who have not cloned yet can read install steps; wire landing + README to that site when ready (see landing page bullet above).

##post-distribution
- linked to github for users to go through the guide on the landing page once published
### configure
- gog setup part should be linked to github page once the git repo is published. 


