# Project TODO


### Agent utility / RAG

- [ ] literally every action card is generated as prodct/technical. I think we should redifine the types of cards. brainstorming is needed. .
1) external
- product-related technical issues/troubleshoot
- product-related queries 

2) Internal 
- ? 

- [ ] feedback to agent as persistent agent memory. 
1. verify and test the agent feedback memory part and do fine tuning ? Since this will be also part of the system prompt for agents, we are now collecting user's feedback from each of the action cards and run history for each agent run. 
2. [ ] We should be able to curate all the feedbacks for agent to understand by LLM first and let users also see the curated feedback on the UI, ideally on configure or you pick the best location. users can give feedbacks on the action card by words or clicking the like/dislike buttons on the run history. Users should be able to see what agent has curated of user's feedback on the UI on configure. this memory should be loaded from database. 
- [ ] how can we change the current agent prompt parts on configure more user friendly and easier to understand from the multi-agentic perspectives ? urrently it only shows what are the prompts for what but users can hardly understand which is for what agent or subagent. Do we need a diagram and differet user friendly workding ?
- [ ] after all update all the md files for the implemented architectures and flows.





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
