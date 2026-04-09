
### UI
 
- **Done (iteration)**: Warmer Notion-like neutrals (`#fbfbfa` / `#37352f`), blue primary `#2383e2`, sage assistant bubbles, peach accent on hero; softer section titles (no harsh all-caps); nav/pill styling toned down.
- **Done**: Enter sends from composer; **IME-safe** (`isComposing` / `keyCode 229`) so Korean composition does not swallow Enter; capture phase so the event is not lost.
- **Done**: **UI language** `EN | 한국어` (saved in `localStorage` `ui_locale`). Affects labels, buttons, empty states, confirms only — **not** assistant message bodies (those still follow user query language via backend). Tooltip clarifies this distinction.
- Optional next: refine remaining English-only alerts (e.g. cron delete confirm), localize maintenance stats line, optional web font.




### Agent Utility 
- Build a notification pipeline (decide channels and triggers) so the system can notify when drafts are ready or when errors occur.

- need to handle the language dynamically. when asked in korean, doc retrieve can retrieve the data regardless of the language but output should be in the language it was asked in (both email probe and user <> interaction, the final output should be in the language the query is asked in)

- Shifting from email drafting agent to proactive assistant CSM agent. I badly want this agent to do this and also have UI/UX reflect this design flow too. 
1) periodically probe inbox and analyse the queries (cron jobs)
2) Agent should be able to sense if there are emails that come from the clients asking about what to do with appier product. If agent senses that it is appier product related client questions, it should be able to search through the docs and list up all the relevant information and actions item for CSM to review. Agent should be proactively also trying to answer the questions if they can as part of the process. Currently, it focuses too much on drafting email. But it should actually help take next actions based on the email. This agent should only help when asked to draft the email
3) Agent should be able to nofify the CSM. I think the best way is to notify CSM through the web browser push. I have web push notification muted still, I can tell if there is something on my email inbox on the top of the browser tab with the number within parenthesis (). 

- cron job can be either set by users asking agent to set the cron job itself or users can manually set cron jobs on the UI e.g) I want you to probe email every 3 hours and get back to me with the drafted version of action items with the relevant documents that could answers the client email inquries. 
- move the agent software using from docs from /data to upload completely for retrieval pipeline. 




## wrap-up 
- appier related documents should not be exposed on the repo
- any important variables (API tokens etc) should not be exposed on the repo.
- update the md files that shows how to install this software package including external dependencies that requires users to install and configure such as API tokens, gogcli, and open router part. Include general guide line if openrouter is not an option for some users.  
- update the md files as for how the retrieval works and why this way can be business critical and sustainable. 
- update the md files as for how the agent self evolves. 
- the UI should include what this software is all about and what it is aiming to do to help CSM concisely can take reference from md files. 
- should include how to install all the dependencies and set variables (e.g API keys) on the MD file.  
- pack up the code to run in the container. 

- update the md files as for how the agent self evolves.  


