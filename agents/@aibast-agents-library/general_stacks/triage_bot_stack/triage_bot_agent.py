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
