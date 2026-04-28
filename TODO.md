# Project TODO





### Foundations (from original backlog)



### Agent utility / RAG

- [ ] literally every action card is generated as prodct/technical. I don't think we should redifine the types of cards. brainstorming is needed. We are triggering search agent based on the action card category. I think agent should trigger the search agent as long as it is product-related.
1) external
- product-related technical issues/troubleshoot
- product-related queries 

2) Internal 

- [ ] now the agent only shows the current reasoning step with the traces below. can we switch to the most popular tracing way like cursor, chatgpt, gemini and etc where they show both real-time reasoning and the thoughts behind it each step with the dropdown ? I think we might have to review how the reasoning process works. we do not need to expose the internal system prompts or agent parsed input as 'users' but at least users need to know how the agent's reasoning process (output of each agent call) like cursor agent when interating on the chat. we should consider then the whole UI change to implement that. 
- [ ] still to verify the web search capability also verify openrouter web search. 
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
- [ ] ensure there is no Appier-internal-only documents in the public repo
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
