
### UI
 
- EN/KR layout is different.  
- env var setup for required API keys. Should be the first landing page for users to land with instructions as for how to set up the agent first ! 
- On the first landing page, also we need a section for users to set up agent LLM models for each agent call given the current codebase.  all the LLM calls from each agent should be able to be configured by users themselves after setting the LLM provider's API. AFAIK, we have one main agent and subagents for doc retrieval, embedding, websearch etc ? 
- make the list of RC documents uploaded and RC URL loaded as shrinkable so that you can see more. Also you should be able to select all to delete for convience. 
- we should be able to delete RC documets upload and RC URL loaded in bulk by checkbox. 
- we should be able to delete action cards in bulk by checkbox. 
- Lets also include some good fancy logo for this Sova on the landing page and other pages on top next to the name of the agent. - CSM Radar Agent 24/7. Best if we can have an animated logo rather than static
- system time to set by users on the UI.
- change the font to fit this agent AI solution more. 






## Agent Utility 
### Action dashboard/action cards : 

- we have deployed for agent's self-evolution by users feedback on history. I think we should do that on the actionboard. Can we shift from users clicking likes/dislikes but actually give feedback to the agent in text by users themselves ? is this an ideal agent architecture ?
-  agent is creating redundant task for the same email thread when probing.. If it is the same email thread but updated as with newer email message, we should just update on the same task thread on the dashboard. Maybe we can tell if it is the same but extended card thread by email title. 
- for the task cards on the actionboard, we should also include who is the client or at least client email domain so that we will know. + We should include the title of email thread
- users should be able to change the status and view/sort  (in progress, completed, not started)





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


