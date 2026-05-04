# Demo seed emails (inbox probe)

Five **fictional** messages for populating a test Gmail inbox before a **Scan inbox** / probe demo. No real customer or vendor data. Paste into new mail in your test account (or forward into the slice matched by your probe query).

**Usage:** Send from different external/internal personas so the probe sees varied threads. **Expected category** is a rough target for dashboard triage (the model may differ).

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
