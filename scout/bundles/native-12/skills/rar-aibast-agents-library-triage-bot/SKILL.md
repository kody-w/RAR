---
name: "rar-aibast-agents-library-triage-bot"
description: "Classifies live D365 cases and ServiceNow-shaped ITSM incidents, comparing classifier verdicts to live desk priorities; routes and hands off; offline-safe."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/triage_bot", "rar_sha256": "c8e84498bbdc7aa20908a1d3e920e10f04e0808ed64bf5439c4e0df88102bfff", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.2.0", "author": "AIBAST", "tags": ["triage", "classification", "routing", "priority", "handoff"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/triage_bot`. The original RAPP
agent is preserved byte-for-byte in `triage_bot_agent.py` and in the RCI capsule.

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

Triage Bot Agent — a template you are meant to mutate.

Classifies incoming inquiries, routes them to teams, assesses priority,
and generates handoff summaries. The keyword classifier and the
impact/urgency matrix run against REAL case records, so classification
output changes when the source system changes.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     sibling systems (synthetic data, no credentials, works anywhere):
       CRM — the Static Dynamics 365 tenant (Aster Lane Office Systems):
         https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       ITSM — the Static ITSM desk (real ServiceNow Table-API shape,
       30 INC records):
         https://kody-w.github.io/static-itsm/api/now/table/
     Try: perform(operation="classify_inquiry")
     — classifies the tenant's real seeded CRM cases AND cross-checks
     the live ITSM desk: the keyword classifier runs over each real
     incident short_description and its verdict is compared to the
     desk's live ServiceNow priority (e.g. INC0010001 "Benefits portal
     login failures during open enrollment" -> Technical Support,
     agrees with live P1-Critical).
  2. No network? Everything falls back to the embedded demo layer below
     (_SAMPLE_INQUIRIES / _ROUTING_RULES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     TRIAGE_BOT_DATA_URL to any OData-shaped endpoint and
     TRIAGE_BOT_ITSM_URL to any ServiceNow Table-API-shaped endpoint,
     or replace the fetchers with your ticketing client. The fields
     the rest of the file needs are listed in _normalize_live_inquiry()
     — customer tier is labeled "n/a — enrichment seam"; wire your
     account-tiering data there.

OPERATIONS
  classify_inquiry | route_request | priority_assessment
  | handoff_summary
  kwargs: operation (required)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The triage operation to perform",
      "enum": [
        "classify_inquiry",
        "route_request",
        "priority_assessment",
        "handoff_summary"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `triage_bot_agent.py` and embedded as the fenced Python below (sha256 c8e84498bbdc7aa2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `triage_bot_agent.py` first:

```bash
python3 triage_bot_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 triage_bot_agent.py   # or on stdin
python3 triage_bot_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Triage Bot Agent — a template you are meant to mutate.

Classifies incoming inquiries, routes them to teams, assesses priority,
and generates handoff summaries. The keyword classifier and the
impact/urgency matrix run against REAL case records, so classification
output changes when the source system changes.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     sibling systems (synthetic data, no credentials, works anywhere):
       CRM — the Static Dynamics 365 tenant (Aster Lane Office Systems):
         https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       ITSM — the Static ITSM desk (real ServiceNow Table-API shape,
       30 INC records):
         https://kody-w.github.io/static-itsm/api/now/table/
     Try: perform(operation="classify_inquiry")
     — classifies the tenant's real seeded CRM cases AND cross-checks
     the live ITSM desk: the keyword classifier runs over each real
     incident short_description and its verdict is compared to the
     desk's live ServiceNow priority (e.g. INC0010001 "Benefits portal
     login failures during open enrollment" -> Technical Support,
     agrees with live P1-Critical).
  2. No network? Everything falls back to the embedded demo layer below
     (_SAMPLE_INQUIRIES / _ROUTING_RULES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     TRIAGE_BOT_DATA_URL to any OData-shaped endpoint and
     TRIAGE_BOT_ITSM_URL to any ServiceNow Table-API-shaped endpoint,
     or replace the fetchers with your ticketing client. The fields
     the rest of the file needs are listed in _normalize_live_inquiry()
     — customer tier is labeled "n/a — enrichment seam"; wire your
     account-tiering data there.

OPERATIONS
  classify_inquiry | route_request | priority_assessment
  | handoff_summary
  kwargs: operation (required)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/triage_bot",
    "version": "1.2.0",
    "display_name": "Triage Bot",
    "description": "Classifies live D365 cases and ServiceNow-shaped ITSM incidents, comparing classifier verdicts to live desk priorities; routes and hands off; offline-safe.",
    "author": "AIBAST",
    "tags": ["triage", "classification", "routing", "priority", "handoff"],
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
#   export TRIAGE_BOT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your ticketing client.
# Downstream code only needs the fields produced by
# _normalize_live_inquiry().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "TRIAGE_BOT_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
# Sibling system: the Static ITSM desk — real ServiceNow Table API
# shape ({"result": [...]}, INC numbers, coded state/priority). Point
# at your own instance:
#   export TRIAGE_BOT_ITSM_URL=https://your-instance/api/now/table
ITSM_SOURCE_URL = os.environ.get(
    "TRIAGE_BOT_ITSM_URL",
    "https://kody-w.github.io/static-itsm/api/now/table",
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
            rows = json.loads(resp.read().decode("utf-8")).get("value", [])
    except Exception:
        rows = []
    _LIVE_CACHE[collection] = rows
    return rows


def _fetch_itsm_table(table, timeout=6):
    """Sibling fetcher for the ServiceNow-shaped ITSM desk. Same rules
    as _fetch_collection — lazy, one bounded GET, [] on ANY failure —
    but parses the Table API envelope {"result": [...]} and caches in
    _LIVE_CACHE keyed by full URL."""
    url = f"{ITSM_SOURCE_URL}/{table}.json"
    if url in _LIVE_CACHE:
        return _LIVE_CACHE[url]
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "rapp-agent-template/1.0"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            rows = json.loads(resp.read().decode("utf-8")).get("result", [])
    except Exception:
        rows = []
    _LIVE_CACHE[url] = rows
    return rows


# ServiceNow incident coded values -> labels (Table API returns codes).
_SN_STATE = {"1": "New", "2": "In Progress", "3": "On Hold",
             "6": "Resolved", "7": "Closed", "8": "Canceled"}
_SN_PRIORITY = {"1": "P1-Critical", "2": "P2-High",
                "3": "P3-Medium", "4": "P4-Low"}

# Which live ServiceNow priorities each classifier verdict would expect.
# Used to grade the classifier against the desk's own triage decision.
_CATEGORY_EXPECTED_SN_PRIORITY = {
    "technical_support": ("1", "2"),
    "security": ("1", "2"),
    "billing": ("2", "3"),
    "sales": ("3", "4"),
    "account_management": ("3", "4"),
    "feature_request": ("3", "4"),
}


# Dynamics case priority -> impact/urgency, a deliberately simple stated
# mapping: High -> high/high, Normal -> medium/medium, Low -> low/low.
_PRIORITY_TO_IMPACT_URGENCY = {
    "High": ("high", "high"),
    "Normal": ("medium", "medium"),
    "Low": ("low", "low"),
}


def _normalize_live_inquiry(row):
    """Project a Dynamics case record onto the inquiry shape this agent
    uses. THIS is the contract your replacement data source must meet —
    a dict with these keys. The classification and confidence are
    COMPUTED by this agent's keyword classifier over the real title and
    description; None/'n/a' fields are enrichment seams."""
    priority = row.get("prioritycode@OData.Community.Display.V1.FormattedValue", "Normal")
    impact, urgency = _PRIORITY_TO_IMPACT_URGENCY.get(priority, ("medium", "medium"))
    text = f"{row.get('title', '')}. {row.get('description', '')}".strip()
    classified_as, confidence = _classify_inquiry(text)
    return {
        "id": row.get("ticketnumber", row.get("incidentid", "")),
        "text": text,
        "customer": row.get("customeridname", "Unknown"),
        "tier": None,  # enrichment seam — wire your account-tiering data
        "impact": impact,
        "urgency": urgency,
        "classified_as": classified_as,
        "confidence": confidence,
        "_live": True,
    }


def _live_inquiries():
    """Live open tenant cases as inquiries; [] when offline."""
    rows = _fetch_collection("incidents")
    return [
        _normalize_live_inquiry(r)
        for r in rows
        if r.get("statecode") == 0 and r.get("title")
    ]


def _inquiry_pool():
    """Live inquiries when reachable, embedded demo inquiries otherwise.
    Returns (inquiries, is_live)."""
    live = _live_inquiries()
    if live:
        return live, True
    return _SAMPLE_INQUIRIES, False


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_INQUIRY_CATEGORIES = {
    "technical_support": {"label": "Technical Support", "description": "Product issues, bugs, performance problems", "team": "Technical Support", "avg_handle_min": 25, "sla_hours": 4},
    "billing": {"label": "Billing & Payments", "description": "Invoices, payment issues, plan changes", "team": "Billing Team", "avg_handle_min": 15, "sla_hours": 8},
    "sales": {"label": "Sales Inquiry", "description": "Pricing, demos, new purchases", "team": "Sales Team", "avg_handle_min": 20, "sla_hours": 2},
    "account_management": {"label": "Account Management", "description": "Renewals, upgrades, account changes", "team": "Account Management", "avg_handle_min": 30, "sla_hours": 8},
    "feature_request": {"label": "Feature Request", "description": "New feature suggestions, enhancements", "team": "Product Team", "avg_handle_min": 10, "sla_hours": 72},
    "security": {"label": "Security Concern", "description": "Security incidents, compliance, data privacy", "team": "Security Team", "avg_handle_min": 35, "sla_hours": 1},
}

_ROUTING_RULES = {
    "technical_support": {"primary_team": "Technical Support", "escalation_team": "Engineering", "auto_assign": True, "skill_required": "product_knowledge", "after_hours": "On-Call Engineer"},
    "billing": {"primary_team": "Billing Team", "escalation_team": "Finance", "auto_assign": True, "skill_required": "billing_systems", "after_hours": "Billing Queue"},
    "sales": {"primary_team": "Sales Team", "escalation_team": "Sales Management", "auto_assign": False, "skill_required": "sales_qualification", "after_hours": "Lead Queue"},
    "account_management": {"primary_team": "Account Management", "escalation_team": "VP Customer Success", "auto_assign": True, "skill_required": "account_strategy", "after_hours": "CSM Queue"},
    "feature_request": {"primary_team": "Product Team", "escalation_team": "Product Management", "auto_assign": False, "skill_required": "product_strategy", "after_hours": "Product Backlog"},
    "security": {"primary_team": "Security Team", "escalation_team": "CISO", "auto_assign": True, "skill_required": "security_ops", "after_hours": "Security On-Call"},
}

_PRIORITY_MATRIX = {
    "impact_high_urgency_high": {"priority": "P1-Critical", "response_min": 15, "resolution_hours": 1, "auto_escalate": True},
    "impact_high_urgency_medium": {"priority": "P2-High", "response_min": 30, "resolution_hours": 4, "auto_escalate": False},
    "impact_high_urgency_low": {"priority": "P3-Medium", "response_min": 60, "resolution_hours": 8, "auto_escalate": False},
    "impact_medium_urgency_high": {"priority": "P2-High", "response_min": 30, "resolution_hours": 4, "auto_escalate": False},
    "impact_medium_urgency_medium": {"priority": "P3-Medium", "response_min": 60, "resolution_hours": 8, "auto_escalate": False},
    "impact_medium_urgency_low": {"priority": "P4-Low", "response_min": 120, "resolution_hours": 24, "auto_escalate": False},
    "impact_low_urgency_high": {"priority": "P3-Medium", "response_min": 60, "resolution_hours": 8, "auto_escalate": False},
    "impact_low_urgency_medium": {"priority": "P4-Low", "response_min": 120, "resolution_hours": 24, "auto_escalate": False},
    "impact_low_urgency_low": {"priority": "P5-Informational", "response_min": 240, "resolution_hours": 72, "auto_escalate": False},
}

_HANDOFF_TEMPLATES = {
    "technical_escalation": {
        "template_name": "Technical Escalation", "sections": ["Customer Information", "Issue Description", "Steps Taken", "Environment Details", "Business Impact", "Recommended Next Steps"],
    },
    "management_escalation": {
        "template_name": "Management Escalation", "sections": ["Customer Information", "Account Value", "Issue History", "Customer Sentiment", "Risk Assessment", "Recommended Action"],
    },
    "cross_team": {
        "template_name": "Cross-Team Handoff", "sections": ["Customer Information", "Original Category", "Reason for Transfer", "Context Summary", "Outstanding Questions"],
    },
}

_SAMPLE_INQUIRIES = [
    {"id": "INQ-T001", "text": "Our entire sales team can't access the platform. Getting 500 errors for the past 30 minutes.", "customer": "Meridian Corp", "tier": "Enterprise", "impact": "high", "urgency": "high", "classified_as": "technical_support", "confidence": 0.97},
    {"id": "INQ-T002", "text": "I'd like to understand the pricing for your Analytics Pro module for 200 users.", "customer": "New Prospect", "tier": "Unknown", "impact": "low", "urgency": "medium", "classified_as": "sales", "confidence": 0.94},
    {"id": "INQ-T003", "text": "We received a duplicate invoice for November. Can you check?", "customer": "Atlas Digital", "tier": "Mid-Market", "impact": "medium", "urgency": "low", "classified_as": "billing", "confidence": 0.96},
    {"id": "INQ-T004", "text": "We noticed unauthorized API calls from an unknown IP. Need immediate investigation.", "customer": "BlueHorizon Health", "tier": "Enterprise", "impact": "high", "urgency": "high", "classified_as": "security", "confidence": 0.99},
]


# ═══════════════════════════════════════════════════════════════
# HELPERS — real computation, live or embedded inputs
# ═══════════════════════════════════════════════════════════════

def _classify_inquiry(text):
    text_lower = text.lower()
    if any(w in text_lower for w in ["error", "not working", "can't access", "bug", "crash", "failing", "failure", "downtime", "cannot be opened"]):
        return "technical_support", 0.95
    if any(w in text_lower for w in ["pricing", "demo", "purchase", "quote"]):
        return "sales", 0.92
    if any(w in text_lower for w in ["invoice", "payment", "billing", "charge", "transaction"]):
        return "billing", 0.94
    if any(w in text_lower for w in ["security", "unauthorized", "breach", "privacy"]):
        return "security", 0.97
    if any(w in text_lower for w in ["feature", "enhancement", "wish", "suggestion"]):
        return "feature_request", 0.88
    return "account_management", 0.75


def _assess_priority(impact, urgency):
    key = f"impact_{impact}_urgency_{urgency}"
    return _PRIORITY_MATRIX.get(key, _PRIORITY_MATRIX["impact_medium_urgency_medium"])


def _itsm_crosscheck_section(limit=10):
    """Markdown section that runs THIS agent's keyword classifier over
    the live ITSM desk's real incident short_descriptions and compares
    each verdict to the desk's live ServiceNow priority. One line when
    the desk is offline."""
    rows = _fetch_itsm_table("incident")
    if not rows:
        return ("**ITSM Desk Cross-Check:** desk unreachable — live "
                "ServiceNow-shaped section skipped\n")
    active = [r for r in rows if r.get("active") == "true"][:limit]
    agree = 0
    table = ""
    for r in active:
        text = f"{r.get('short_description', '')}. {r.get('description', '')}".strip()
        cat, conf = _classify_inquiry(text)
        pri = str(r.get("priority", ""))
        ok = pri in _CATEGORY_EXPECTED_SN_PRIORITY.get(cat, ())
        agree += 1 if ok else 0
        table += (
            f"| {r.get('number', '')} "
            f"| {str(r.get('short_description', ''))[:42]} "
            f"| {_INQUIRY_CATEGORIES[cat]['label']} ({conf:.0%}) "
            f"| {_SN_PRIORITY.get(pri, pri)} "
            f"| {_SN_STATE.get(str(r.get('state', '')), r.get('state', ''))} "
            f"| {'agrees' if ok else 'differs'} |\n"
        )
    return (
        f"**ITSM Desk Cross-Check (LIVE ServiceNow-shaped incidents — "
        f"classifier verdict vs the desk's own priority; agrees on "
        f"{agree} of {len(active)}):**\n\n"
        f"| Number | Short Description | Classifier Verdict | Live Priority | Live State | Verdict vs Desk |\n"
        f"|---|---|---|---|---|---|\n"
        f"{table}"
    )


def _pool_source_line(is_live):
    if is_live:
        return "Inquiry source: LIVE open cases from the Aster Lane Dynamics 365 tenant"
    return "Inquiry source: embedded demo layer (simulated — live tenant unreachable)"


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class TriageBotAgent(BasicAgent):
    """
    Inquiry triage and routing agent.

    Operations:
        classify_inquiry    - classify an inquiry by category
        route_request       - determine routing for an inquiry
        priority_assessment - assess priority based on impact/urgency
        handoff_summary     - generate a handoff summary for escalation
    """

    def __init__(self):
        self.name = "TriageBotAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "classify_inquiry", "route_request",
                            "priority_assessment", "handoff_summary",
                        ],
                        "description": "The triage operation to perform",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "classify_inquiry")
        dispatch = {
            "classify_inquiry": self._classify_inquiry_op,
            "route_request": self._route_request,
            "priority_assessment": self._priority_assessment,
            "handoff_summary": self._handoff_summary,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler()

    def _classify_inquiry_op(self):
        inquiries, is_live = _inquiry_pool()
        rows = ""
        for inq in inquiries[:15]:
            cat = _INQUIRY_CATEGORIES[inq["classified_as"]]
            rows += f"| {inq['id']} | {inq['text'][:45]}... | {cat['label']} | {inq['confidence']:.0%} | {inq['customer']} |\n"
        more = f"(showing 15 of {len(inquiries)})\n" if len(inquiries) > 15 else ""
        cat_rows = ""
        for key, cat in _INQUIRY_CATEGORIES.items():
            cat_rows += f"| {cat['label']} | {cat['description'][:40]} | {cat['team']} | {cat['sla_hours']}h |\n"
        return (
            f"**Inquiry Classification Results** (classifier runs over the real record text)\n\n"
            f"| ID | Inquiry | Category | Confidence | Customer |\n|---|---|---|---|---|\n"
            f"{rows}{more}\n"
            f"**Category Definitions:**\n\n"
            f"| Category | Description | Team | SLA |\n|---|---|---|---|\n"
            f"{cat_rows}\n"
            f"{_itsm_crosscheck_section()}\n"
            f"{_pool_source_line(is_live)}\n"
            f"Source: [Classification Engine + Case Queue + ITSM Desk]\nAgents: TriageBotAgent"
        )

    def _route_request(self):
        inquiries, is_live = _inquiry_pool()
        route_rows = ""
        for cat_key, rule in _ROUTING_RULES.items():
            cat = _INQUIRY_CATEGORIES[cat_key]
            auto = "Yes" if rule["auto_assign"] else "No"
            route_rows += f"| {cat['label']} | {rule['primary_team']} | {rule['escalation_team']} | {auto} | {rule['after_hours']} |\n"
        sample = inquiries[0]
        sample_route = _ROUTING_RULES[sample["classified_as"]]
        return (
            f"**Routing Configuration**\n\n"
            f"| Category | Primary Team | Escalation | Auto-Assign | After Hours |\n|---|---|---|---|---|\n"
            f"{route_rows}\n"
            f"**Example Routing: {sample['id']}**\n"
            f"- Inquiry: {sample['text'][:50]}...\n"
            f"- Route to: {sample_route['primary_team']}\n"
            f"- Skill required: {sample_route['skill_required']}\n"
            f"- Auto-assign: {'Yes' if sample_route['auto_assign'] else 'No'}\n\n"
            f"{_pool_source_line(is_live)}\n"
            f"Source: [Routing Engine]\nAgents: TriageBotAgent"
        )

    def _priority_assessment(self):
        inquiries, is_live = _inquiry_pool()
        priority_rows = ""
        for key, p in _PRIORITY_MATRIX.items():
            parts = key.split("_")
            impact = parts[1]
            urgency = parts[3]
            auto = "Yes" if p["auto_escalate"] else "No"
            priority_rows += f"| {impact.title()} | {urgency.title()} | {p['priority']} | {p['response_min']}m | {p['resolution_hours']}h | {auto} |\n"
        sample_rows = ""
        for inq in inquiries[:10]:
            p = _assess_priority(inq["impact"], inq["urgency"])
            sample_rows += f"| {inq['id']} | {inq['impact'].title()} | {inq['urgency'].title()} | {p['priority']} | {p['response_min']}m |\n"
        return (
            f"**Priority Assessment**\n\n"
            f"**Assessed Inquiries** (impact/urgency derived from the case priority — High=high/high, Normal=medium/medium, Low=low/low):\n\n"
            f"| ID | Impact | Urgency | Priority | Response Time |\n|---|---|---|---|---|\n"
            f"{sample_rows}\n"
            f"**Priority Matrix:**\n\n"
            f"| Impact | Urgency | Priority | Response | Resolution | Auto-Escalate |\n|---|---|---|---|---|---|\n"
            f"{priority_rows}\n"
            f"{_pool_source_line(is_live)}\n"
            f"Source: [Priority Engine]\nAgents: TriageBotAgent"
        )

    def _handoff_summary(self):
        inquiries, is_live = _inquiry_pool()
        high = [i for i in inquiries if i["impact"] == "high"]
        inq = high[0] if high else inquiries[0]
        p = _assess_priority(inq["impact"], inq["urgency"])
        route = _ROUTING_RULES[inq["classified_as"]]
        template = _HANDOFF_TEMPLATES["technical_escalation"]
        sections = "\n".join(f"- {s}" for s in template["sections"])
        tier = inq["tier"] if inq.get("tier") else "n/a — enrichment seam"
        return (
            f"**Handoff Summary: {inq['id']}**\n\n"
            f"**Customer:** {inq['customer']} ({tier})\n"
            f"**Category:** {_INQUIRY_CATEGORIES[inq['classified_as']]['label']}\n"
            f"**Priority:** {p['priority']}\n\n"
            f"**Issue:** {inq['text']}\n\n"
            f"**Routing:**\n"
            f"- Assigned to: {route['primary_team']}\n"
            f"- Escalation path: {route['escalation_team']}\n"
            f"- Response SLA: {p['response_min']} minutes\n"
            f"- Resolution SLA: {p['resolution_hours']} hours\n"
            f"- Auto-escalate: {'Yes' if p['auto_escalate'] else 'No'}\n\n"
            f"**Handoff Template:** {template['template_name']}\n"
            f"**Sections:**\n{sections}\n\n"
            f"{_pool_source_line(is_live)}\n"
            f"Source: [Triage Engine + Routing]\nAgents: TriageBotAgent"
        )


if __name__ == "__main__":
    agent = TriageBotAgent()
    print("=" * 60)
    print("EMBEDDED DEMO INQUIRY (works offline)")
    demo = _SAMPLE_INQUIRIES[0]
    demo_cat, demo_conf = _classify_inquiry(demo["text"])
    print(
        f"{demo['id']} ({demo['customer']}): \"{demo['text'][:60]}...\" -> "
        f"{_INQUIRY_CATEGORIES[demo_cat]['label']} ({demo_conf:.0%})"
    )
    print()
    print("=" * 60)
    print("LIVE CRM CASES + LIVE ITSM DESK CROSS-CHECK (both fetched")
    print("over HTTP; the classifier runs over real ServiceNow-shaped")
    print("incident short_descriptions and its verdict is graded")
    print("against each incident's live priority; falls back offline)")
    print(agent.perform(operation="classify_inquiry"))
    print()
    print("=" * 60)
    print(agent.perform(operation="priority_assessment"))
    print()
    print("=" * 60)
    print(agent.perform(operation="handoff_summary"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
