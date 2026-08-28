---
name: "rar-aibast-agents-library-customer-360"
description: "Builds unified customer profiles and timelines from a live simulated Dynamics 365 tenant (accounts, cases, emails), with an offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/customer_360", "rar_sha256": "1207a85d5c8291b3e542573f45a0335c6cc24085bf1215e3ff2d9048d5756294", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["customer-360", "unified-profile", "health-score", "next-best-action", "crm"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/customer_360`. The original RAPP
agent is preserved byte-for-byte in `customer_360_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Customer 360 Agent — a template you are meant to mutate.

Provides unified customer profiles by merging CRM, support, and billing
data, with interaction timelines, health scores, and next-best-action
recommendations. In this template the 360 view is assembled from real
tenant entities: an account plus its cases, and the email threads that
regard those cases.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `unified_profile` operation pulls live
     account and case records over real HTTP from the globally hosted
     Static Dynamics 365 tenant (Aster Lane Office Systems — synthetic
     data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="unified_profile",
                  customer_id="Riverbend Medical Group")
     — its two open cases (prior auth SLA, intake form sync) drive the
     live health score. `interaction_timeline` weaves in the real email
     activity regarding those cases.
  2. No network? Everything falls back to the embedded demo layer below
     (_CUSTOMER_PROFILES / _INTERACTION_LOGS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CUSTOMER_360_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from your CDP), or replace
     _fetch_collection() with your own clients. The fields the rest of
     the file needs are listed in _normalize_live_customer() — fields
     rendered "n/a — enrichment seam" (ARR, contract, CSM) are where you
     wire billing and success platforms.

OPERATIONS
  unified_profile | interaction_timeline | health_score | next_best_action
  kwargs: operation (required), customer_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 'CUST-3001')",
      "type": "string"
    },
    "operation": {
      "description": "The customer 360 operation to perform",
      "enum": [
        "unified_profile",
        "interaction_timeline",
        "health_score",
        "next_best_action"
      ],
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_360_agent.py` and embedded as the fenced Python below (sha256 1207a85d5c8291b3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_360_agent.py` first:

```bash
python3 customer_360_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 customer_360_agent.py   # or on stdin
python3 customer_360_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Customer 360 Agent — a template you are meant to mutate.

Provides unified customer profiles by merging CRM, support, and billing
data, with interaction timelines, health scores, and next-best-action
recommendations. In this template the 360 view is assembled from real
tenant entities: an account plus its cases, and the email threads that
regard those cases.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `unified_profile` operation pulls live
     account and case records over real HTTP from the globally hosted
     Static Dynamics 365 tenant (Aster Lane Office Systems — synthetic
     data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="unified_profile",
                  customer_id="Riverbend Medical Group")
     — its two open cases (prior auth SLA, intake form sync) drive the
     live health score. `interaction_timeline` weaves in the real email
     activity regarding those cases.
  2. No network? Everything falls back to the embedded demo layer below
     (_CUSTOMER_PROFILES / _INTERACTION_LOGS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CUSTOMER_360_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from your CDP), or replace
     _fetch_collection() with your own clients. The fields the rest of
     the file needs are listed in _normalize_live_customer() — fields
     rendered "n/a — enrichment seam" (ARR, contract, CSM) are where you
     wire billing and success platforms.

OPERATIONS
  unified_profile | interaction_timeline | health_score | next_best_action
  kwargs: operation (required), customer_id
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json as _json
import urllib.request

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/customer_360",
    "version": "1.1.0",
    "display_name": "Customer 360",
    "description": "Builds unified customer profiles and timelines from a live simulated Dynamics 365 tenant (accounts, cases, emails), with an offline fallback.",
    "author": "AIBAST",
    "tags": ["customer-360", "unified-profile", "health-score", "next-best-action", "crm"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export CUSTOMER_360_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CDP/CRM clients. Downstream
# code only needs the fields produced by _normalize_live_customer().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "CUSTOMER_360_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
_LIVE_CACHE = {}


def _fetch_collection(collection, timeout=6):
    """One bounded GET per collection per process. Returns [] on ANY
    failure — offline, DNS, bad JSON — so the demo layer takes over."""
    if collection in _LIVE_CACHE:
        return _LIVE_CACHE[collection]
    try:
        req = urllib.request.Request(
            f"{DATA_SOURCE_URL}/{collection}.json",
            headers={"User-Agent": "rapp-agent-template/1.0"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            rows = _json.loads(resp.read().decode("utf-8")).get("value", [])
    except Exception:
        rows = []
    _LIVE_CACHE[collection] = rows
    return rows


def _normalize_live_customer(row, incidents):
    """Project a Dynamics account + its cases onto the profile shape this
    agent uses. THIS is the contract your replacement data source must
    meet — a dict with these keys. None means 'not knowable from the CRM
    alone' and the renderers label it as an enrichment seam."""
    name = row.get("name", "Unknown")
    cases = [i for i in incidents if i.get("customeridname") == name]
    open_cases = [i for i in cases if i.get("statecode") == 0]
    high_priority_open = [i for i in open_cases if i.get("prioritycode") == 1]
    return {
        "name": name,
        "segment": None,          # enrichment seam — wire your CDP
        "industry": row.get("industrycode", "Unknown"),
        "arr": None,              # enrichment seam — wire your billing system
        "primary_contact": row.get("primarycontactidname", ""),
        "account_manager": row.get("owneridname", ""),
        "csm": None,              # enrichment seam — wire your success platform
        "contract_end": None,     # enrichment seam
        "city": f"{row.get('address1_city', '?')}, {row.get('address1_stateorprovince', '?')}",
        "total_cases": len(cases),
        "open_cases": len(open_cases),
        "high_priority_open": len(high_priority_open),
        "case_titles": [c.get("title", "") for c in cases],
        "_live": True,
    }


def _live_customers():
    """name-keyed dict of live tenant customers; {} when offline."""
    rows = _fetch_collection("accounts")
    if not rows:
        return {}
    incidents = _fetch_collection("incidents")
    return {
        row["name"].lower(): _normalize_live_customer(row, incidents)
        for row in rows
        if row.get("name")
    }


def _live_health(cust):
    """Health from real case signals: open and high-priority case load."""
    return max(
        20,
        100 - cust["open_cases"] * 15 - cust["high_priority_open"] * 10 - cust["total_cases"] * 2,
    )


def _seam(value, formatter=str):
    """None = the CRM alone can't know this (enrichment seam)."""
    return "n/a — enrichment seam" if value is None else formatter(value)


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_CUSTOMER_PROFILES = {
    "CUST-3001": {
        "name": "TechVantage Solutions", "segment": "Enterprise",
        "industry": "Technology", "arr": 185000, "mrr": 15417,
        "primary_contact": "Jennifer Walsh", "contact_email": "jennifer.walsh@techvantage.com",
        "account_manager": "Sarah Chen", "csm": "Mike Torres",
        "contract_start": "2023-06-15", "contract_end": "2026-06-14",
        "products": ["Enterprise Platform", "Analytics Pro", "Integration Hub", "Premium Support"],
        "employees_using": 420, "licenses_purchased": 500,
        "crm_data": {"lead_source": "Partner Referral", "deal_cycle_days": 62, "original_deal_size": 145000},
        "billing_data": {"payment_method": "ACH", "payment_terms": "Net 30", "last_payment": "2025-11-01", "outstanding_balance": 0, "lifetime_value": 462500},
        "support_data": {"total_tickets": 47, "open_tickets": 2, "avg_resolution_hours": 4.2, "csat_avg": 4.6, "escalations": 3},
    },
    "CUST-3002": {
        "name": "Greenridge Partners", "segment": "Mid-Market",
        "industry": "Financial Services", "arr": 72000, "mrr": 6000,
        "primary_contact": "David Park", "contact_email": "david.park@greenridge.com",
        "account_manager": "Tom Rivera", "csm": "Lisa Wong",
        "contract_start": "2024-01-10", "contract_end": "2025-01-09",
        "products": ["Core Platform", "Analytics Standard"],
        "employees_using": 85, "licenses_purchased": 100,
        "crm_data": {"lead_source": "Website", "deal_cycle_days": 45, "original_deal_size": 72000},
        "billing_data": {"payment_method": "Credit Card", "payment_terms": "Net 15", "last_payment": "2025-10-15", "outstanding_balance": 6000, "lifetime_value": 72000},
        "support_data": {"total_tickets": 18, "open_tickets": 4, "avg_resolution_hours": 8.7, "csat_avg": 3.8, "escalations": 2},
    },
    "CUST-3003": {
        "name": "BlueHorizon Health", "segment": "Enterprise",
        "industry": "Healthcare", "arr": 240000, "mrr": 20000,
        "primary_contact": "Dr. Maria Santos", "contact_email": "maria.santos@bluehorizon.org",
        "account_manager": "Sarah Chen", "csm": "Mike Torres",
        "contract_start": "2022-03-01", "contract_end": "2025-02-28",
        "products": ["Enterprise Platform", "Analytics Pro", "Security Suite", "Integration Hub", "Premium Support", "Training Package"],
        "employees_using": 1200, "licenses_purchased": 1500,
        "crm_data": {"lead_source": "Conference", "deal_cycle_days": 120, "original_deal_size": 180000},
        "billing_data": {"payment_method": "ACH", "payment_terms": "Net 45", "last_payment": "2025-11-05", "outstanding_balance": 0, "lifetime_value": 720000},
        "support_data": {"total_tickets": 92, "open_tickets": 1, "avg_resolution_hours": 3.1, "csat_avg": 4.8, "escalations": 1},
    },
}

_INTERACTION_LOGS = {
    "CUST-3001": [
        {"date": "2025-11-12", "type": "Support Ticket", "channel": "Portal", "summary": "Dashboard loading timeout - resolved with cache clear", "sentiment": "Neutral"},
        {"date": "2025-11-08", "type": "QBR Meeting", "channel": "Teams", "summary": "Quarterly business review - discussed expansion to APAC team", "sentiment": "Positive"},
        {"date": "2025-10-25", "type": "Support Ticket", "channel": "Email", "summary": "SSO integration issue post-update - escalated and resolved", "sentiment": "Frustrated"},
        {"date": "2025-10-15", "type": "Product Feedback", "channel": "In-App", "summary": "Requested advanced filtering in analytics module", "sentiment": "Positive"},
        {"date": "2025-10-01", "type": "Billing", "channel": "Portal", "summary": "Added 50 user licenses for Q4 onboarding", "sentiment": "Positive"},
    ],
    "CUST-3002": [
        {"date": "2025-11-10", "type": "Support Ticket", "channel": "Portal", "summary": "Report export failing for large date ranges", "sentiment": "Frustrated"},
        {"date": "2025-11-05", "type": "Support Ticket", "channel": "Email", "summary": "User access permissions not syncing with AD", "sentiment": "Frustrated"},
        {"date": "2025-10-28", "type": "CSM Check-in", "channel": "Phone", "summary": "Discussed adoption challenges, team training needed", "sentiment": "Concerned"},
        {"date": "2025-10-20", "type": "Billing", "channel": "Portal", "summary": "Late payment notice - payment received Oct 22", "sentiment": "Neutral"},
    ],
    "CUST-3003": [
        {"date": "2025-11-14", "type": "Renewal Discussion", "channel": "Teams", "summary": "Renewal meeting - expanding from 1500 to 2000 licenses", "sentiment": "Positive"},
        {"date": "2025-11-01", "type": "Executive Sponsor", "channel": "In-Person", "summary": "CIO dinner - strong relationship, considering additional modules", "sentiment": "Positive"},
        {"date": "2025-10-20", "type": "Product Feedback", "channel": "Email", "summary": "Requested HIPAA compliance reporting enhancements", "sentiment": "Positive"},
    ],
}

_HEALTH_SCORE_WEIGHTS = {
    "product_adoption": 0.25,
    "support_satisfaction": 0.20,
    "engagement_frequency": 0.20,
    "billing_health": 0.15,
    "relationship_strength": 0.20,
}

_NEXT_BEST_ACTIONS = {
    "high_health": [
        {"action": "Schedule expansion discussion", "priority": "Medium", "reason": "Strong health score indicates readiness for upsell"},
        {"action": "Invite to customer advisory board", "priority": "Low", "reason": "Champion potential for reference program"},
        {"action": "Share product roadmap preview", "priority": "Medium", "reason": "Deepen partnership and gather feedback"},
    ],
    "medium_health": [
        {"action": "Schedule adoption review", "priority": "High", "reason": "Usage below potential, identify barriers"},
        {"action": "Offer training session", "priority": "High", "reason": "Improve feature utilization"},
        {"action": "CSM check-in call", "priority": "Medium", "reason": "Proactive relationship maintenance"},
    ],
    "low_health": [
        {"action": "Executive escalation meeting", "priority": "Critical", "reason": "Churn risk - requires immediate attention"},
        {"action": "Create success plan", "priority": "Critical", "reason": "Define clear path to value realization"},
        {"action": "Resolve open support tickets", "priority": "High", "reason": "Outstanding issues impacting satisfaction"},
    ],
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _resolve_customer(query):
    """Embedded demo customers first, then the live tenant account roster."""
    if not query:
        return "CUST-3001"
    q = query.upper().strip()
    for key in _CUSTOMER_PROFILES:
        if key in q:
            return key
    q_lower = query.lower()
    for key, cust in _CUSTOMER_PROFILES.items():
        if q_lower in cust["name"].lower():
            return key
    live = _live_customers()
    for key in live:
        if q_lower in key:
            return key
    return "CUST-3001"


def _get_customer(cust_id):
    """Unified lookup: embedded demo customers first, then live tenant."""
    if cust_id in _CUSTOMER_PROFILES:
        return _CUSTOMER_PROFILES[cust_id]
    return _live_customers().get(cust_id) or _CUSTOMER_PROFILES["CUST-3001"]


def _compute_health_score(cust_id):
    cust = _CUSTOMER_PROFILES[cust_id]
    adoption = min(100, (cust["employees_using"] / cust["licenses_purchased"]) * 100 * 1.2)
    support_sat = cust["support_data"]["csat_avg"] / 5.0 * 100
    interactions = len(_INTERACTION_LOGS.get(cust_id, []))
    engagement = min(100, interactions * 20)
    billing = 100 if cust["billing_data"]["outstanding_balance"] == 0 else 60
    positive = sum(1 for i in _INTERACTION_LOGS.get(cust_id, []) if i["sentiment"] == "Positive")
    total_interactions = max(1, interactions)
    relationship = (positive / total_interactions) * 100
    w = _HEALTH_SCORE_WEIGHTS
    score = (adoption * w["product_adoption"] + support_sat * w["support_satisfaction"] +
             engagement * w["engagement_frequency"] + billing * w["billing_health"] +
             relationship * w["relationship_strength"])
    return round(score), {"adoption": round(adoption), "support": round(support_sat),
                           "engagement": round(engagement), "billing": round(billing),
                           "relationship": round(relationship)}


def _get_nba(health_score):
    if health_score >= 80:
        return _NEXT_BEST_ACTIONS["high_health"]
    elif health_score >= 60:
        return _NEXT_BEST_ACTIONS["medium_health"]
    return _NEXT_BEST_ACTIONS["low_health"]


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class Customer360Agent(BasicAgent):
    """
    Unified customer profile agent.

    Operations:
        unified_profile      - complete customer profile from all data sources
        interaction_timeline - chronological interaction history
        health_score         - compute and explain customer health score
        next_best_action     - recommend next actions based on health
    """

    def __init__(self):
        self.name = "Customer360Agent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "unified_profile", "interaction_timeline",
                            "health_score", "next_best_action",
                        ],
                        "description": "The customer 360 operation to perform",
                    },
                    "customer_id": {
                        "type": "string",
                        "description": "Customer ID (e.g. 'CUST-3001')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "unified_profile")
        cust_id = _resolve_customer(kwargs.get("customer_id", ""))
        dispatch = {
            "unified_profile": self._unified_profile,
            "interaction_timeline": self._interaction_timeline,
            "health_score": self._health_score,
            "next_best_action": self._next_best_action,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(cust_id)

    # ── unified_profile ────────────────────────────────────────
    def _unified_profile(self, cust_id):
        cust = _get_customer(cust_id)
        if cust.get("_live"):
            score = _live_health(cust)
            case_list = "\n".join(f"- {t}" for t in cust["case_titles"]) or "- No cases on record"
            return (
                f"**Customer 360: {cust['name']} (live tenant)**\n\n"
                f"| Field | Detail |\n|---|---|\n"
                f"| Segment | {_seam(cust['segment'])} |\n"
                f"| Industry | {cust['industry']} |\n"
                f"| ARR | {_seam(cust['arr'], lambda v: f'${v:,}')} |\n"
                f"| Health Score | {score}/100 (from live case signals) |\n"
                f"| Primary Contact | {cust['primary_contact']} |\n"
                f"| Account Manager | {cust['account_manager']} |\n"
                f"| CSM | {_seam(cust['csm'])} |\n"
                f"| Location | {cust['city']} |\n\n"
                f"**Support:** {cust['open_cases']} open of {cust['total_cases']} total cases "
                f"({cust['high_priority_open']} high priority)\n\n"
                f"**Cases:**\n{case_list}\n\n"
                f"_ARR, segment, contract, and CSM are enrichment seams — wire your "
                f"billing and success platforms._\n\n"
                f"Source: [live Static Dynamics 365 tenant — account + cases]\nAgents: Customer360Agent"
            )
        score, _ = _compute_health_score(cust_id)
        products_list = "\n".join(f"- {p}" for p in cust["products"])
        return (
            f"**Customer 360: {cust['name']}**\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Segment | {cust['segment']} |\n"
            f"| Industry | {cust['industry']} |\n"
            f"| ARR | ${cust['arr']:,} |\n"
            f"| Health Score | {score}/100 |\n"
            f"| Primary Contact | {cust['primary_contact']} |\n"
            f"| Account Manager | {cust['account_manager']} |\n"
            f"| CSM | {cust['csm']} |\n"
            f"| Contract | {cust['contract_start']} to {cust['contract_end']} |\n\n"
            f"**Products ({len(cust['products'])}):**\n{products_list}\n\n"
            f"**Usage:** {cust['employees_using']}/{cust['licenses_purchased']} licenses active ({cust['employees_using']/cust['licenses_purchased']*100:.0f}%)\n\n"
            f"**Support:** {cust['support_data']['open_tickets']} open tickets | CSAT {cust['support_data']['csat_avg']}/5.0 | Avg resolution: {cust['support_data']['avg_resolution_hours']}h\n\n"
            f"**Billing:** {cust['billing_data']['payment_method']} | {cust['billing_data']['payment_terms']} | LTV: ${cust['billing_data']['lifetime_value']:,}\n\n"
            f"Source: [CRM + Support + Billing + Product Usage]\nAgents: Customer360Agent"
        )

    # ── interaction_timeline ───────────────────────────────────
    def _interaction_timeline(self, cust_id):
        cust = _get_customer(cust_id)
        if cust.get("_live"):
            case_titles = set(cust["case_titles"])
            emails = [
                e for e in _fetch_collection("emails")
                if e.get("regardingobjectidname") in case_titles
            ]
            rows = []
            for e in emails:
                direction = "Outbound" if e.get("directioncode") else "Inbound"
                rows.append((
                    str(e.get("senton", ""))[:10],
                    f"| {str(e.get('senton', ''))[:10]} | Email ({direction}) | "
                    f"{e.get('subject', '')[:50]} | {e.get('regardingobjectidname', '')[:45]} "
                    f"| n/a — enrichment seam |"
                ))
            rows.sort(key=lambda r: r[0], reverse=True)
            table = "\n".join(r[1] for r in rows) or "| — | — | No email activity found | — | — |"
            return (
                f"**Interaction Timeline: {cust['name']} (live tenant)**\n\n"
                f"Email activities regarding this customer's {cust['total_cases']} case(s): {len(rows)}\n\n"
                f"| Date | Type | Subject | Regarding Case | Sentiment |\n|---|---|---|---|---|\n"
                f"{table}\n\n"
                f"_Sentiment is an enrichment seam — wire your sentiment model._\n\n"
                f"Source: [live Static Dynamics 365 tenant — emails regarding the "
                f"account's cases]\nAgents: Customer360Agent"
            )
        logs = _INTERACTION_LOGS.get(cust_id, [])
        timeline_rows = ""
        for log in logs:
            timeline_rows += f"| {log['date']} | {log['type']} | {log['channel']} | {log['summary'][:60]} | {log['sentiment']} |\n"
        sentiment_counts = {}
        for log in logs:
            sentiment_counts[log["sentiment"]] = sentiment_counts.get(log["sentiment"], 0) + 1
        sentiment_summary = " | ".join(f"{s}: {c}" for s, c in sentiment_counts.items())
        return (
            f"**Interaction Timeline: {cust['name']}**\n\n"
            f"Total Interactions: {len(logs)} | Sentiment: {sentiment_summary}\n\n"
            f"| Date | Type | Channel | Summary | Sentiment |\n|---|---|---|---|---|\n"
            f"{timeline_rows}\n\n"
            f"Source: [CRM + Support + Billing + CSM Notes]\nAgents: Customer360Agent"
        )

    # ── health_score ───────────────────────────────────────────
    def _health_score(self, cust_id):
        cust = _get_customer(cust_id)
        if cust.get("_live"):
            score = _live_health(cust)
            status = "Healthy" if score >= 80 else ("At Risk" if score >= 60 else "Critical")
            return (
                f"**Health Score: {cust['name']} (live tenant)**\n\n"
                f"**Overall Score: {score}/100 ({status})** — computed from live case signals\n\n"
                f"**Key Indicators:**\n"
                f"- Open cases: {cust['open_cases']} ({cust['high_priority_open']} high priority)\n"
                f"- Total cases on record: {cust['total_cases']}\n"
                f"- License utilization: n/a — enrichment seam\n"
                f"- CSAT / billing balance: n/a — enrichment seam\n\n"
                f"Source: [live Static Dynamics 365 tenant — case-signal model]\nAgents: Customer360Agent"
            )
        score, components = _compute_health_score(cust_id)
        comp_rows = ""
        for name, weight in _HEALTH_SCORE_WEIGHTS.items():
            comp_val = components.get(name.split("_")[0], components.get(name, 0))
            weighted = comp_val * weight
            comp_rows += f"| {name.replace('_', ' ').title()} | {comp_val}/100 | {weight:.0%} | {weighted:.1f} |\n"
        status = "Healthy" if score >= 80 else ("At Risk" if score >= 60 else "Critical")
        return (
            f"**Health Score: {cust['name']}**\n\n"
            f"**Overall Score: {score}/100 ({status})**\n\n"
            f"| Component | Score | Weight | Weighted |\n|---|---|---|---|\n"
            f"{comp_rows}\n"
            f"**Key Indicators:**\n"
            f"- License utilization: {cust['employees_using']}/{cust['licenses_purchased']} ({cust['employees_using']/cust['licenses_purchased']*100:.0f}%)\n"
            f"- Support CSAT: {cust['support_data']['csat_avg']}/5.0\n"
            f"- Open tickets: {cust['support_data']['open_tickets']}\n"
            f"- Outstanding balance: ${cust['billing_data']['outstanding_balance']:,}\n\n"
            f"Source: [Health Score Engine]\nAgents: Customer360Agent"
        )

    # ── next_best_action ───────────────────────────────────────
    def _next_best_action(self, cust_id):
        cust = _get_customer(cust_id)
        if cust.get("_live"):
            score = _live_health(cust)
            actions = _get_nba(score)
            action_rows = "".join(
                f"| {a['action']} | {a['priority']} | {a['reason']} |\n" for a in actions
            )
            return (
                f"**Next Best Actions: {cust['name']} (live tenant)**\n\n"
                f"Health Score: {score}/100 (live case signals) | "
                f"Segment: {_seam(cust['segment'])} | ARR: {_seam(cust['arr'])}\n\n"
                f"| Action | Priority | Rationale |\n|---|---|---|\n"
                f"{action_rows}\n"
                f"**Context:**\n"
                f"- Open cases: {cust['open_cases']} ({cust['high_priority_open']} high priority)\n"
                f"- Contract end: n/a — enrichment seam\n\n"
                f"Source: [live Static Dynamics 365 tenant + NBA rules]\nAgents: Customer360Agent"
            )
        score, _ = _compute_health_score(cust_id)
        actions = _get_nba(score)
        action_rows = ""
        for a in actions:
            action_rows += f"| {a['action']} | {a['priority']} | {a['reason']} |\n"
        return (
            f"**Next Best Actions: {cust['name']}**\n\n"
            f"Health Score: {score}/100 | Segment: {cust['segment']} | ARR: ${cust['arr']:,}\n\n"
            f"| Action | Priority | Rationale |\n|---|---|---|\n"
            f"{action_rows}\n"
            f"**Context:**\n"
            f"- Contract ends: {cust['contract_end']}\n"
            f"- Open tickets: {cust['support_data']['open_tickets']}\n"
            f"- Last interaction: {_INTERACTION_LOGS.get(cust_id, [{}])[0].get('date', 'N/A')}\n\n"
            f"Source: [NBA Engine + CRM + Health Score]\nAgents: Customer360Agent"
        )


if __name__ == "__main__":
    agent = Customer360Agent()
    print("=" * 60)
    print("EMBEDDED DEMO PROFILE (works offline)")
    print(agent.perform(operation="unified_profile", customer_id="CUST-3001"))
    print()
    print("=" * 60)
    print("LIVE TENANT PROFILE (account + cases fetched over HTTP; falls back offline)")
    print(agent.perform(operation="unified_profile", customer_id="Riverbend Medical Group"))
    print()
    print("=" * 60)
    print(agent.perform(operation="interaction_timeline", customer_id="Riverbend Medical Group"))
    print()
    for op in ["health_score", "next_best_action"]:
        print("=" * 60)
        print(agent.perform(operation=op, customer_id="CUST-3001"))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
