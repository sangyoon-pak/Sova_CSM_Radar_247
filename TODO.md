# Project TODO





### Foundations (from original backlog)



### Agent utility / RAG

- [x] **Less-refined uploads** (PDF, noisy docs): expected behavior, limits, and UX messaging
- [ ] investigate why web search was not triggered. 


**backlog to run the agent ** : I ran a workbench thread that would trigger doc search. since I enabled web search always, it should have triggered web search but it did not trigger web search at all. can you investigate ? 


run history : 
4/24/2026, 4:34:15 PM · thread_message · completed
이거 고객에게 온 이메일 내용인데, 먼저 기술 내용좀 정리해줘. 

안녕하세요. 박상윤님
개발 담당자 김상오입니다.

  상세한 안내 감사합니다. 내용 검토 후 확인 사항 전달드립니다.

  이해한 프로세스

  1. 아모레 서버에서 가격 변동을 계산하고 대상 회원을 추출
  2. AIQUA API를 통해 대상 회원에게 tier_price_dropped 커스텀 이벤트를 전송
  3. AIQU
search_product_docs
Correct
Incorrect
Useful
Noisy
User prompt
이거 고객에게 온 이메일 내용인데, 먼저 기술 내용좀 정리해줘. 

안녕하세요. 박상윤님
개발 담당자 김상오입니다.

  상세한 안내 감사합니다. 내용 검토 후 확인 사항 전달드립니다.

  이해한 프로세스

  1. 아모레 서버에서 가격 변동을 계산하고 대상 회원을 추출
  2. AIQUA API를 통해 대상 회원에게 tier_price_dropped 커스텀 이벤트를 전송
  3. AIQUA에서 해당 이벤트를 트리거로 캠페인을 설정하고,
     이벤트 파라미터({{event.product_name}}, {{event.new_price}} 등)로
     메시지 동적 콘텐츠를 구성

  사용하려는 API 및 정보
 
   AIQUA로 데이터 스트리밍 (Stream Data to AIQUA)
  - 엔드포인트: POST https://api.quantumgraph.com/qga/clients-data/
  - 인증: appId, appSecret을 요청 body에 포함
  - 유저 
Final output
```markdown
고객이 요청한 기술적인 내용을 정리하면 다음과 같습니다:

### 고객의 요청 사항
1. **API 엔드포인트 확인**: 고객은 `/qga/clients-data/` 엔드포인트가 "Event Upload API"와 동일한지 확인을 요청했습니다. 만약 별도의 API가 있다면 스펙을 공유해달라고 요청했습니다. (출처: Uploaded: 055_aiqua_part_1.md — https://docs.aiqua.appier.com/ | line 861)
   
2. **이벤트 트리거 문제**: 고객은 `tier_price_dropped` 이벤트를 성공적으로 전송했으나, AIQUA 콘솔의 캠페인 생성 시 트리거 규칙의 이벤트 드롭다운 목록에 해당 이벤트가 나타나지 않는 문제를 보고했습니다. 별도의 설정이나 반영 시간이 필요한지 확인을 요청했습니다. (출처: Uploaded: 055_aiqua_part_1.md — https://docs.aiqua.appier.com/ | line 937)

3. **디바이스 값 확인**: 앱 푸시 캠페인에서 `tier_price_dropped` 이벤트를 트리거로 사용하려면 `device` 값을 "android" 또는 "ios"로 전송해야 하는지, "web"으로 전송해도 플랫폼 무관하게 트리거가 가능한지 확인을 요청했습니다. (출처: Uploaded: 055_aiqua_part_1.md — https://docs.aiqua.appier.com/ | line 2876)

4. **유저 행동 기반 트리거 캠페인 발송 방식**: "tier": "VIP"가 포함된 경우, 랜덤한 `user_id` 1개로 이벤트를 내면 "VIP" 그룹 전체에 발송되는지, 아니면 개별로 이벤트를 전송해야 하는지 확인을 요청했습니다. (출처: Uploaded: 055_aiqua_part_1.md — https://docs.aiqua.appier.com/ | line 172)

5. **티어 설정 방법**: 티어 설정 방법과 다양한 조합으로 지정 및 변경이 가능한지 확인을 요청했습니다. (출처: Uploaded: 055_aiqua_part_1.md — https://docs.aiqua.appier.com/ | line 668)

6. **API 호출 제한 및 복수 유저 전송 방법**: API 스펙상 요청 1건에 유저 1명만 지정 가능한 것으로 보이며, 초당 허용 호출수는 50건으로 확인되었습니다. 대상이 많을 경우에도 유저별로 개별 호출해야 하는지, 복수 유저를 한 번에 전송할 수 있는 방법이 있는지 확인을 요청했습니다. (출처: Uploaded: 055_aiqua_part_1.md — https://docs.aiqua.appier.com/ | line 875)

### 다음 단계
- **API 엔드포인트 확인**: AIQUA의 공식 문서를 통해 `/qga/clients-data/` 엔드포인트가 "Event Upload API"와 동일한지 확인하고, 필요시 별도의 API 스펙을 고객에게 공유합니다.
- **이벤트 트리거 문제 해결**: AIQUA의 이벤트 트리거 설정에 대한 문서를 검토하여 고객의 문제를 해결할 수 있는 방법을 제안합니다.
- **디바이스 값 확인**: AIQUA의 푸시 캠페인 관련 문서를 통해 `device` 값 설정에 대한 명확한 지침을 제공합니다.
- **유저 행동 기반 트리거 캠페인 발송 방식 확인**: AIQUA의 캠페인 발송 방식에 대한 문서를 검토하여 고객의 질문에 답변합니다.
- **티어 설정 방법 확인**: AIQUA의 티어 설정 관련 문서를 검토하여 고객의 질문에 답변합니다.
- **API 호출 제한 및 복수 유저 전송 방법 확인**: AIQUA의 API 호출 제한 및 복수 유저 전송 방법에 대한 문서를 검토하여 고객의 질문에 답변합니다.

### 참고 문서
- [AIQUA 공식 문서](https://docs.aiqua.appier.com/)

이 정보를 바탕으로 고객의 요청에 대한 답변을 준비할 수 있습니다. 추가적인 문서 검토가 필요할 수 있습니다. 



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
