# Project TODO

Last updated: 2026-04-16

Single checklist: **completed** work from the rebuild + **remaining** tasks (merged from the former `docs/IMPLEMENTATION_TODO_STATUS.md` and this file). For implementation detail, see paths in the completed section.

### to do Fix 
- [x] what is the best way to make use of the retrieved data after the initial run generating card ? if user asks an extensive question, agent should know about the data retrieved so that it can answers based on both retrieved information + email thread content. 
- [x] the thread time and action card time are not matched with the time set on configure. all the time related parts should be based on the single time set via configure. don't know why the time is all over the place on the thread and chatbox on workbench. 
- [ ] landing page requires instruction for cron jobs as well
- [ ] agent should be able to do probe mode [true] if user's prompt intent is to actually probe the inbox and make action cards. what is the best way to do that but not to trigger this that could cause unnecessary API cost ?


### Workbench / threads

- [ ] **Bulk select + bulk delete** for threads




### Foundations (from original backlog)

- [ ] Keep **search/retrieval** aligned with `docs/SEARCH_AGENT.md` as the foundation; extend features on top
- [ ] **Docs refresh**: architecture diagram (Users → Agent → subagents → RAG → answer); sync all `docs/*.md` with current code
- [ ] **Install guide**: external deps (API tokens, gog, OpenRouter), and alternatives if OpenRouter is not an option
- [ ] **Docs**: why retrieval is designed this way (business-critical / sustainable)
- [ ] **Docs**: self-evolution / learning from feedback


### Agent utility / RAG

- [ ] **Less-refined uploads** (PDF, noisy docs): expected behavior, limits, and UX messaging
- [ ] what is the best way to improve web search ? now currently once you upload a RC url, agent will trigger LLM to come up with 9 more sub url to search if I am right. I wonder how web search feature works differently for difference cases 1) when users decided to use openAI with the openAI API, and 2) when users decided to use openrouter for this case. 
- [ ] verify and test the agent feedback memory part and do fine tuning ? Since this will be also part of the system prompt for agents, we are now collecting user's feedback from each of the action cards and run history for each agent run. We should be able to curate all the feedbacks for agent to understand by LLM first and let users also see the curated feedback on the UI, ideally on configure ? 
- [ ] how do we change the current agent prompt finetune feature for users to understand from multi-agentic perspective ? currently it only shows what are the prompts for what but users can hardly understand which is for what agent or subagent. 
## docs
- [ ] I think we should show the agent architecture, that shows what are the flows and agent to agent or subagent working here end to end on the md file and links to configure where users can see and finetune. and linked this archicture document on where on the landing page tab


## Remaining — pre-distribution / distribution

### Pre-distribution

- [ ] No Appier-internal-only documents in the public repo
- [ ] Remove irrelevant scratch/test artifacts from the tree where appropriate
- [ ] **Knowledge base** content not pushed to public GitHub (`.gitignore` / policy); verify
- [ ] No secrets/tokens committed

### Distribution

- [ ] change the project folder name to Sova_CSM_Radar_247 when ready 
- [ ] **Host install** story: mac/linux/windows via venv + `run.py` (not container-first); `gog`/OAuth need a normal OS env (`docs/GMAIL_SETUP.md`)
- [ ] **Public docs UX**: canonical `docs/INSTALLATION.md`; README links; optional future docs site; landing links when published

### Post-distribution

- [ ] Landing links to **GitHub** guides once the repo is public
- [ ] Configure **gog** section links to the published GitHub doc page
- [ ] simple user-guide video that shows what it does. you can 


## Pointer

The former standalone file `docs/IMPLEMENTATION_TODO_STATUS.md` is merged here. See that path for a one-line redirect.
