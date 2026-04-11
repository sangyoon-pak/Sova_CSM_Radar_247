
## UI
 
- make the list of RC documents uploaded and RC URL loaded as shrinkable so that you can see more. Also you should be able to select all to delete for convience. 
- we should be able to delete RC documets upload and RC URL loaded in bulk by checkbox. 
- we should be able to delete action cards in bulk by checkbox. 
- system time to set by users on the UI.
- change the font to fit this agent AI solution more. 
- all the action cards by default should be folded and expanded only when users click it 


### landing page   
- the next step should only show when APIS and Gog both are not set. Only goes away when both APIS and GOG are set. 
- landing page should be 2x2 grid layout 
- disclaimer to be included 
1) only agent is able to fetch from gmail inbox (gogcli). For other email service providers, it is up to users who want to develop the pipeline themselves. 
- the landing page should include what this software is all about and what it is aiming to do to help CSM concisely can take reference from md files. 
- **GitHub docs hub (follow-up):** Landing currently assumes the user has already cloned and run the server; it shows **Next steps** in-app and a link to `https://github.com/sangyoon-pak/email_draft_agent/tree/main/docs` (update `docsGithubRootLink` in `src/web/index.html` if the repo moves). Later work: publish a **GitHub Pages** (or docs site) mirror of `docs/*.md`, add **INSTALLATION**, architecture, and Gmail guides with stable URLs, and point the landing CTA / “full setup” link to that site instead of raw GitHub tree. Keep repo `docs/` as source of truth; CI or Mintlify optional.

### configure
- gog setup part should be linked to github page once the git repo is published. 






## Agent Utility 
### Rag
- currently the documents are scraped from the RC webpage in a structured manner (parsed into a markdown). what if users just upload less-refined pdf/docs files ? would that work too ? 

### Action dashboard/action cards : 

- we have deployed for agent's self-evolution by users feedback on history. I think we should do that on the actionboard. Can we shift from users clicking likes/dislikes but actually give feedback to the agent in text by users themselves ? is this an ideal agent architecture ?

- for the task cards on the actionboard, we should also include who is the client or at least client email domain so that we will know. + We should include the title of email thread
- users should be able to change the status and view/sort  (in progress, completed, not started)

### Cron Jobs

- cron job can be either set by users asking agent to set the cron job itself or users can manually set cron jobs on the UI e.g) I want you to probe email every 3 hours and get back to me with the drafted version of action items with the relevant documents that could answers the client email inquries. 
- current cron tab is not user friendly. cron jobs are to probe at a set interval by users. We should improve UI and functionaliy ?


### MD files
- Agent architecture diagram. Users -> Agent -> subagent (Rag architecture, subquery engines, reranking etc) -> final agent -> answer
- update all the md files up to date synced with the current codebase and architectures
- update the md files that shows how to install this software package including external dependencies that requires users to install and configure such as API tokens, gogcli, and open router part. Include general guide line if openrouter is not an option for some users.  
- update the md files as for how the retrieval works and why this way can be business critical and sustainable. 
- update the md files as for how the agent self evolves. 

### workbench
- should include the remaining top-up credit from the llm provider (openrouter, openAI)

## pre-distribution
- appier related documents should not be exposed on the repo
- clean up the irrelevant files (test files, etc)
- do not push knowledge-base file to public github repo. mark it so that it won't be part of the push. 
- any important variables (API tokens etc) should not be exposed on the repo.

## distribution
- make it available across mac/linux/windows via **host install** (venv + `run.py`); **not** container-first—`gog`/OAuth/keyring need a normal OS environment (see `docs/GMAIL_SETUP.md`).
- **Public docs UX:** one canonical **A–Z** is `docs/INSTALLATION.md` in-repo; expose it on **GitHub** (README link) and later a **docs website** so users who have not cloned yet can read install steps; wire landing + README to that site when ready (see landing page bullet above).



