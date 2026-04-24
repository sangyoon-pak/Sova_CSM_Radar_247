# Project TODO





### Foundations (from original backlog)



### Agent utility / RAG

- [x] **Less-refined uploads** (PDF, noisy docs): expected behavior, limits, and UX messaging
- [ ] verify how action cards changed to completed works when the next probe comes. is it updated or agent only uppend it when it considers it updated thread by thread id and fingerprint ?  
- [ ] verify and test the agent feedback memory part and do fine tuning ? Since this will be also part of the system prompt for agents, we are now collecting user's feedback from each of the action cards and run history for each agent run. We should be able to curate all the feedbacks for agent to understand by LLM first and let users also see the curated feedback on the UI, ideally on configure ? 
- [ ] how do we change the current agent prompt finetune feature for users to understand from multi-agentic perspective ? currently it only shows what are the prompts for what but users can hardly understand which is for what agent or subagent. 
## docs
- [x] current architecture.md does not elaborate how the retrieval process (RAG, web search, subagentic scoring system, etc)
- [x] I think we should show the agent architecture, that shows what are the flows and agent to agent or subagent working here end to end on the md file and links to configure where users can see and finetune. and linked this archicture document on where on the landing page tab
- [x] Keep **search/retrieval** aligned with `docs/SEARCH_AGENT.md` as the foundation; extend features on top
- [x] **Docs refresh**: architecture diagram (Users → Agent → subagents → RAG → answer); sync all `docs/*.md` with current code
- [x] **Install guide**: external deps (API tokens, gog, OpenRouter), and alternatives if OpenRouter is not an option
- [x] **Docs**: why retrieval is designed this way (business-critical / sustainable)
- [x] **Docs**: self-evolution / learning from feedback



### Pre-distribution
- [ ] Final UI touch. both light and dark mode not too good for readability. Text and wordings is worth being refined. UI design could look better more with the enterprise feel. Run Trace part looks quite dev look and tacky. This requires UI enhancement. Also on the UI run trace part, still it says 'assistant'. this should change to 'Sova Agent' 
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
