# Demo seed emails (inbox probe)

**Eight** **fictional** messages for populating a test Gmail inbox before a **Scan inbox** / probe demo. No real customer or vendor data. Paste into new mail in your test account (or forward into the slice matched by your probe query).

**Usage:** Send from different external/internal personas so the probe sees varied threads. **Expected category** is a rough target for dashboard triage (the model may differ).

**Note:** Messages **6–8** are longer or Korean on purpose. **§6** is written in the same *shape* as a local QA fixture (`data/reports/fixtures/client_query_kr_full.txt` in this repo)—event-stream API + custom event + campaign trigger questions—but uses **neutral** product/endpoint names for demos (**not** copied vendor text).

---

## 1 — client_technical (API timeout)

**Expected category (rough):** `client_technical`

**Subject:** REST API returns 504 on `/v1/events/export` after 120s

**From:** Jordan Lee &lt;jordan.lee@northwind-retail.example&gt;  
**To:** you@yourcompany.com

**Body:**

```
Hi team,

We're integrating the Events Export API (doc version 3.2). For tenant `acme-4482`, calls to
GET /v1/events/export?start=2025-11-01&end=2025-11-30 consistently time out with HTTP 504
after ~120 seconds. Smaller date ranges work.

Can someone confirm whether this is a known platform limit or if we need a background job / chunked export?

Thanks,
Jordan
Northwind Retail | Data Engineering
```

---

## 2 — client_non_technical (renewal / contract)

**Expected category (rough):** `client_non_technical`

**Subject:** Renewal quote for FY26 — need alignment before board review

**From:** Maria Santos &lt;maria.santos@contoso-health.example&gt;  
**To:** you@yourcompany.com

**Body:**

```
Hello,

Our FY25 enterprise agreement ends March 31. Procurement asked for a single-page summary of
renewal pricing and any minimum seat changes before our board slot on Feb 12.

Who is the right person to send the draft order form and SLA terms?

Best regards,
Maria Santos
Director of Operations, Contoso Health
```

---

## 3 — internal (quota / platform alert)

**Expected category (rough):** `internal` (or filtered by guardrails; may not become a customer card)

**Subject:** [AUTOMATED] Workspace 7712 — 90% of monthly API quota consumed

**From:** platform-alerts@yourcompany.internal  
**To:** you@yourcompany.com

**Body:**

```
Alert: Tenant workspace 7712 has used 90% of the monthly API quota (period ending 2025-12-01).
No customer-facing incident. Ops: consider capacity follow-up with account team.

Reference: quota_job_id=Q-99821
```

---

## 4 — client_technical (webhook retries)

**Expected category (rough):** `client_technical`

**Subject:** Webhook delivery failing with signature mismatch

**From:** Alex Patel &lt;alex.patel@fabric-logistics.example&gt;  
**To:** you@yourcompany.com

**Body:**

```
Team,

We enabled outbound webhooks to https://hooks.fabric-logistics.example/sova/v1 with secret `whsec_***`.
Every POST from your environment fails our HMAC check. Payloads look valid JSON.

Please confirm:
- signing base string (raw body vs canonicalized)
- clock skew tolerance

We need this live by Friday for our pilot.

Alex Patel
Fabric Logistics | Integrations
```

---

## 5 — informational / low intent (newsletter)

**Expected category (rough):** informational only / unlikely CSM card

**Subject:** Q1 Industry Digest — trends in customer success tooling

**From:** newsletter@industry-roundup.example  
**To:** you@yourcompany.com

**Body:**

```
Hi,

This week: consolidation in CS platforms, AI-assisted triage benchmarks, and three case studies.
Unsubscribe: https://industry-roundup.example/u/

— Industry Roundup Editorial
```

---

## 6 — client_technical (event stream + campaign trigger, long QA)

**Expected category (rough):** `client_technical`

**Subject:** Event stream ingest OK in logs — custom event missing from campaign trigger dropdown?

**From:** Casey Ng &lt;casey.ng@rivermart-digital.example&gt;  
**To:** you@yourcompany.com

**Body:**

```
Hello,

We've followed your integration guide for streaming user events into OmniEngage.

Understood flow (please confirm):

1. Our pricing service computes discount eligibility and selects users.
2. We POST to your Stream Data endpoint with a custom event name `catalog_price_drop`
   and parameters: product_name, sku, old_price, new_price, deep_link, segment_tier.
3. In OmniEngage we create a campaign with trigger type = that event and use the
   parameters in message templates (e.g. {{event.product_name}}).

Endpoint we are using:
  POST https://api.omni-engage.example/v1/clients/stream
Auth: appId + appSecret in JSON body
User key: identifier "loyalty_id" with SHA-512 hash of our internal customer id
Device field: we send "android" | "ios" | "web" depending on the last active channel.

Open questions:

1. Is that POST the same as the "Event Upload API" in the PDF, or is there a separate
   upload path we should use for production?

2. Test calls return 200 and we see the event in Console → Settings → Recent activity,
   but when creating a campaign → Trigger rules, `catalog_price_drop` does not appear
   in the event dropdown. Is there a propagation delay or a toggled "register custom event" step?

3. For push campaigns (Android/iOS), must device always be "android"/"ios", or can we
   send "web" and still target mobile pushes?

4. For audience rules that reference segment_tier (e.g. VIP), if we send one stream row
   for a single loyalty_id, does the campaign fan out to all VIP users or only that user?
   Do we need one POST per recipient when the audience is large?

5. Docs mention 50 requests/second. If we must send one user per request at peak, is there
   a batch or bulk endpoint we should use instead?

Thanks,
Casey Ng
Integrations | Rivermart Digital
```

---

## 7 — client_technical (이벤트 스트림·트리거, 한국어)

**Expected category (rough):** `client_technical`

**Subject:** 커스텀 이벤트 `inventory_restocked` 전송은 되는데 캠페인 트리거 목록에 안 보입니다

**From:** 개발팀 김도윤 &lt;doyun.kim@hanaro-shop.example&gt;  
**To:** you@yourcompany.com

**Body:**

```
안녕하세요, 담당자님

한가로마트 온라인몰 개발 김도윤입니다.

다음 흐름으로 연동 중입니다.

1. WMS 재고 변경 시 회원별로 추천 대상을 계산
2. POST https://api.nexus-cdp.example/stream/events 로 커스텀 이벤트 inventory_restocked 전송
   (user_key: 회원번호 해시, device: android|ios|web, 파라미터: sku_name, qty, aisle_code)
3. Nexus CDP에서 해당 이벤트를 트리거로 캠페인 생성 예정

확인 부탁드립니다:

- 위 엔드포인트가 문서상 "이벤트 업로드 API"와 동일한지요? 별도 URL이 있다면 공유 부탁드립니다.
- 테스트 전송 후 콘솔 > 활동에서는 수신 확인되나, 캠페인 생성 > 트리거 선택 목록에
  inventory_restocked 가 나타나지 않습니다. 반영 시간이 필요한지, 콘솔에서 등록 단계가
  빠졌는지 알려 주세요.
- 푸시 캠페인만 대상입니다. device를 web으로 보내도 동일하게 트리거되는지,
  반드시 android/ios로 보내야 하는지 확인 부탁드립니다.
- 대량 회원에게 동시에 발송해야 할 때, 요청 한 건에 여러 user를 넣을 수 있는지요?
  초당 호출 한도도 함께 안내 부탁드립니다.

감사합니다.
김도윤
한가로마트 | 커머스 개발
```

---

## 8 — client_non_technical (도입 검토 미팅, 한국어)

**Expected category (rough):** `client_non_technical`

**Subject:** 3분기 OKR 정리 전에 솔루션 도입 일정만 먼저 맞추고 싶습니다

**From:** 이서연 &lt;seoyeon.lee@bluepine-corp.example&gt;  
**To:** you@yourcompany.com

**Body:**

```
안녕하세요,

블루파인 기획 이서연입니다.

경영진 보고(7월 셋째 주) 전에 "도입 범위·예상 일정·계약 조건 요약" 한 장짜리로만이라도
정리해야 해서 연락드렸습니다. 기술 옵션 깊게는 다음 단계에서 해도 되고요.

- 견적/번들(좌석·API 호출) 대략 범위
- 파일럿 8주안에 가능한지, 안 되면 현실적인 착수 시점

가능하시면 이번 주 금요일 오전 중 30분 통화 가능할까요?

감사합니다.
이서연
블루파인㈜ 디지털전략팀
```
