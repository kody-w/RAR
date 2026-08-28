---
name: "rar-aibast-agents-library-ai-customer-assistant"
description: "Handles customer inquiries and escalations from a live simulated Dynamics 365 tenant (cases as tickets), with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/ai_customer_assistant", "rar_sha256": "1008045bc23665d6fc31fd8bb4d4dbaf62a4f376d8d80deb916fd4431733fb9a", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["customer-service", "support", "knowledge-base", "escalation", "satisfaction", "case-management", "action-plan"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/ai_customer_assistant`. The original RAPP
agent is preserved byte-for-byte in `ai_customer_assistant_agent.py` and in the RCI capsule.

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

AI Customer Assistant Agent — a template you are meant to mutate.

AI-powered customer service assistant handling inquiries, knowledge base
searches, escalation routing, and satisfaction surveys. In this template a
customer inquiry is represented as a Dynamics 365 case — the live tenant's
service queue stands in for your ticketing system.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `handle_inquiry` operation resolves live
     case records over real HTTP from the globally hosted Static Dynamics
     365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="handle_inquiry",
                  inquiry_id="disputed card transaction")
     to pull Bluegrass Credit Union's live case.
  2. No network? Everything falls back to the embedded demo layer below
     (_INQUIRIES / _KB_ARTICLES) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     AI_CUSTOMER_ASSISTANT_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from Zendesk/ServiceNow), or
     replace _fetch_collection() with your own client. The fields the
     rest of the file needs are listed in _normalize_live_inquiry() —
     fields rendered "n/a — enrichment seam" (email, account tier,
     sentiment) are where you wire your CRM and sentiment model.

OPERATIONS
  handle_inquiry | knowledge_search | escalation_routing
  | satisfaction_survey | escalation_brief | escalation_action_plan
  | draft_customer_update | escalation_dashboard
  | resolution_recommendation | process_resolution | document_resolution
  kwargs: operation (required), inquiry_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "inquiry_id": {
      "description": "Inquiry ID (e.g. 'INQ-4001')",
      "type": "string"
    },
    "operation": {
      "description": "The customer service operation to perform",
      "enum": [
        "handle_inquiry",
        "knowledge_search",
        "escalation_routing",
        "satisfaction_survey",
        "escalation_brief",
        "escalation_action_plan",
        "draft_customer_update",
        "escalation_dashboard",
        "resolution_recommendation",
        "process_resolution",
        "document_resolution"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ai_customer_assistant_agent.py` and embedded as the fenced Python below (sha256 1008045bc23665d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ai_customer_assistant_agent.py` first:

```bash
python3 ai_customer_assistant_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ai_customer_assistant_agent.py   # or on stdin
python3 ai_customer_assistant_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
AI Customer Assistant Agent — a template you are meant to mutate.

AI-powered customer service assistant handling inquiries, knowledge base
searches, escalation routing, and satisfaction surveys. In this template a
customer inquiry is represented as a Dynamics 365 case — the live tenant's
service queue stands in for your ticketing system.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `handle_inquiry` operation resolves live
     case records over real HTTP from the globally hosted Static Dynamics
     365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="handle_inquiry",
                  inquiry_id="disputed card transaction")
     to pull Bluegrass Credit Union's live case.
  2. No network? Everything falls back to the embedded demo layer below
     (_INQUIRIES / _KB_ARTICLES) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     AI_CUSTOMER_ASSISTANT_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from Zendesk/ServiceNow), or
     replace _fetch_collection() with your own client. The fields the
     rest of the file needs are listed in _normalize_live_inquiry() —
     fields rendered "n/a — enrichment seam" (email, account tier,
     sentiment) are where you wire your CRM and sentiment model.

OPERATIONS
  handle_inquiry | knowledge_search | escalation_routing
  | satisfaction_survey | escalation_brief | escalation_action_plan
  | draft_customer_update | escalation_dashboard
  | resolution_recommendation | process_resolution | document_resolution
  kwargs: operation (required), inquiry_id
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
from datetime import datetime, timedelta
import json as _json
import urllib.request

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/ai_customer_assistant",
    "version": "1.2.0",
    "display_name": "AI Customer Assistant",
    "description": "Handles customer inquiries and escalations from a live simulated Dynamics 365 tenant (cases as tickets), with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["customer-service", "support", "knowledge-base", "escalation", "satisfaction", "case-management", "action-plan"],
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
#   export AI_CUSTOMER_ASSISTANT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your ticketing client. Downstream
# code only needs the fields produced by _normalize_live_inquiry().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "AI_CUSTOMER_ASSISTANT_DATA_URL",
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


def _normalize_live_inquiry(row):
    """Project a Dynamics case onto the inquiry shape this agent uses.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not knowable from the CRM alone' and the
    renderers label it as an enrichment seam."""
    priority = {1: "High", 2: "Medium", 3: "Low"}.get(row.get("prioritycode"), "Medium")
    status = {0: "Open", 1: "Resolved", 2: "Canceled"}.get(row.get("statecode"), "Open")
    return {
        "id": f"INQ-{str(row.get('incidentid', ''))[:8].upper()}",
        "customer": row.get("customeridname", "Unknown"),
        "contact": row.get("primarycontactidname") or row.get("customeridname", ""),
        "email": None,          # enrichment seam — wire your CRM contact record
        "channel": row.get("caseorigincode@OData.Community.Display.V1.FormattedValue", "Unknown"),
        "subject": row.get("title", "untitled"),
        "description": row.get("description", ""),
        "category": row.get("casetypecode@OData.Community.Display.V1.FormattedValue", "Technical Issue"),
        "priority": priority,
        "created_at": str(row.get("createdon", "")),
        "status": status,
        "account_tier": None,   # enrichment seam — wire your billing system
        "sentiment": None,      # enrichment seam — wire your sentiment model
        "_live": True,
    }


def _live_inquiries():
    """id-keyed dict of live tenant inquiries (cases); {} when offline."""
    rows = _fetch_collection("incidents")
    if not rows:
        return {}
    result = {}
    for row in rows:
        if row.get("incidentid"):
            inquiry = _normalize_live_inquiry(row)
            result[inquiry["id"]] = inquiry
    return result


def _seam(value):
    """None = the CRM alone can't know this (enrichment seam)."""
    return "n/a — enrichment seam" if value is None else str(value)


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_INQUIRIES = {
    "INQ-4001": {
        "id": "INQ-4001", "customer": "Acme Corp", "contact": "Lisa Park",
        "email": "lisa.park@acmecorp.com", "channel": "Live Chat",
        "subject": "Unable to generate monthly usage report",
        "description": "The export button on the analytics dashboard returns a 500 error when selecting date ranges longer than 30 days.",
        "category": "Technical Issue", "priority": "High",
        "created_at": "2025-11-14T09:23:00Z", "status": "Open",
        "account_tier": "Enterprise", "sentiment": "Frustrated",
    },
    "INQ-4002": {
        "id": "INQ-4002", "customer": "Bright Solutions", "contact": "Tom Reyes",
        "email": "tom.reyes@brightsol.com", "channel": "Email",
        "subject": "Pricing for additional user seats",
        "description": "We are expanding our team by 15 people next quarter and need pricing for additional seats on the Professional plan.",
        "category": "Billing & Pricing", "priority": "Medium",
        "created_at": "2025-11-14T10:05:00Z", "status": "Open",
        "account_tier": "Professional", "sentiment": "Neutral",
    },
    "INQ-4003": {
        "id": "INQ-4003", "customer": "Greenfield Inc", "contact": "Maria Santos",
        "email": "maria.santos@greenfield.io", "channel": "Phone",
        "subject": "SSO configuration not working after IdP migration",
        "description": "After migrating from Okta to Azure AD, SSO login redirects to a blank page. SAML assertion looks correct in dev tools.",
        "category": "Technical Issue", "priority": "Critical",
        "created_at": "2025-11-14T08:12:00Z", "status": "Open",
        "account_tier": "Enterprise", "sentiment": "Urgent",
    },
    "INQ-4004": {
        "id": "INQ-4004", "customer": "Summit Partners", "contact": "Jake Miller",
        "email": "jake.miller@summitpartners.com", "channel": "Support Portal",
        "subject": "Feature request: bulk user import via CSV",
        "description": "Currently we have to add users one at a time. We need CSV import capability for onboarding 200+ users.",
        "category": "Feature Request", "priority": "Low",
        "created_at": "2025-11-13T16:30:00Z", "status": "Open",
        "account_tier": "Professional", "sentiment": "Positive",
    },
}

_KB_ARTICLES = {
    "KB-101": {
        "id": "KB-101", "title": "How to Export Analytics Reports",
        "category": "Analytics", "relevance_score": 0.95,
        "summary": "Step-by-step guide for exporting usage and analytics reports in CSV, PDF, and Excel formats.",
        "resolution_steps": [
            "Navigate to Analytics > Reports",
            "Select date range (max 90 days per export)",
            "Choose format (CSV, PDF, Excel)",
            "Click Export and wait for download link via email",
        ],
        "last_updated": "2025-10-20", "views": 1247, "helpful_votes": 892,
    },
    "KB-102": {
        "id": "KB-102", "title": "SSO Configuration Guide (SAML 2.0)",
        "category": "Authentication", "relevance_score": 0.92,
        "summary": "Complete guide for configuring SAML-based SSO with supported identity providers.",
        "resolution_steps": [
            "Go to Admin > Security > SSO Settings",
            "Upload IdP metadata XML or enter values manually",
            "Set Assertion Consumer Service URL to https://app.example.com/sso/callback",
            "Map attributes: email, firstName, lastName, groups",
            "Test with SSO debug mode enabled before enforcing",
        ],
        "last_updated": "2025-11-01", "views": 2034, "helpful_votes": 1567,
    },
    "KB-103": {
        "id": "KB-103", "title": "User Management and Seat Licensing",
        "category": "Billing", "relevance_score": 0.88,
        "summary": "Overview of seat-based licensing, adding users, and managing subscriptions.",
        "resolution_steps": [
            "View current seat count in Admin > Billing > Subscription",
            "Click Add Seats to purchase additional licenses",
            "New seats are prorated for the current billing cycle",
            "Bulk provisioning available via SCIM for Enterprise plans",
        ],
        "last_updated": "2025-09-15", "views": 3421, "helpful_votes": 2890,
    },
    "KB-104": {
        "id": "KB-104", "title": "Known Issue: Report Export Timeout for Large Date Ranges",
        "category": "Analytics", "relevance_score": 0.97,
        "summary": "Export fails with 500 error for date ranges exceeding 60 days. Workaround and fix timeline available.",
        "resolution_steps": [
            "Split export into 30-day segments as a workaround",
            "Engineering fix scheduled for v3.8.2 (target: Dec 2025)",
            "Contact support if you need a one-time bulk export",
        ],
        "last_updated": "2025-11-10", "views": 456, "helpful_votes": 398,
    },
}

_ROUTING_RULES = {
    "Technical Issue": {
        "Critical": {"team": "Tier 2 Engineering", "sla_hours": 2, "auto_escalate": True},
        "High": {"team": "Tier 1 Technical Support", "sla_hours": 4, "auto_escalate": False},
        "Medium": {"team": "General Support", "sla_hours": 8, "auto_escalate": False},
        "Low": {"team": "General Support", "sla_hours": 24, "auto_escalate": False},
    },
    "Billing & Pricing": {
        "Critical": {"team": "Billing Escalations", "sla_hours": 2, "auto_escalate": True},
        "High": {"team": "Account Management", "sla_hours": 4, "auto_escalate": False},
        "Medium": {"team": "Account Management", "sla_hours": 8, "auto_escalate": False},
        "Low": {"team": "Self-Service Billing", "sla_hours": 24, "auto_escalate": False},
    },
    "Feature Request": {
        "Critical": {"team": "Product Management", "sla_hours": 8, "auto_escalate": False},
        "High": {"team": "Product Management", "sla_hours": 24, "auto_escalate": False},
        "Medium": {"team": "Product Backlog", "sla_hours": 72, "auto_escalate": False},
        "Low": {"team": "Product Backlog", "sla_hours": 168, "auto_escalate": False},
    },
}

_SATISFACTION_DATA = {
    "overall_csat": 4.3,
    "nps_score": 42,
    "response_time_avg_minutes": 12,
    "first_contact_resolution_rate": 0.78,
    "surveys": [
        {"inquiry_id": "INQ-3990", "score": 5, "comment": "Resolved quickly, great experience.", "date": "2025-11-13"},
        {"inquiry_id": "INQ-3988", "score": 4, "comment": "Helpful but took a while to connect.", "date": "2025-11-13"},
        {"inquiry_id": "INQ-3985", "score": 3, "comment": "Issue resolved but had to explain problem multiple times.", "date": "2025-11-12"},
        {"inquiry_id": "INQ-3982", "score": 5, "comment": "Agent was knowledgeable and proactive.", "date": "2025-11-12"},
        {"inquiry_id": "INQ-3979", "score": 2, "comment": "Still waiting for follow-up on my SSO issue.", "date": "2025-11-11"},
        {"inquiry_id": "INQ-3975", "score": 4, "comment": "Good resolution, would prefer faster initial response.", "date": "2025-11-11"},
    ],
    "trend": {"week_over_week": "+0.2", "month_over_month": "+0.1"},
}

_ESCALATION_CONTEXT = {
    "INQ-4001": {
        "issue": "Recurring monthly-report export failures",
        "interaction_history": "3 contacts in 14 days; workaround attempted twice",
        "detected_intents": ["report failure", "executive deadline", "service credit"],
        "risk_score": 82,
        "case_owner": "Priya Shah",
        "escalation_reason": "Recurring report-export failures are blocking the monthly executive review.",
        "business_impact": "Finance and operations cannot distribute the November usage report.",
        "customer_commitment": "Provide a workaround now and confirm the permanent-fix date.",
        "root_cause": "Large report exports exceed the synchronous processing timeout.",
        "engineering_work_item": "BUG-382",
        "policy_result": "Enterprise support policy permits a managed bulk export.",
        "similar_cases": 7,
        "retention_gesture": "One month of Analytics Pro service credit",
        "next_update": "2025-11-14T13:00:00Z",
        "actions": [
            ("Send the 30-day segmented-export workaround", "Priya Shah", "2025-11-14T10:30:00Z"),
            ("Run a one-time bulk export for Acme Corp", "Data Operations", "2025-11-14T12:00:00Z"),
            ("Confirm v3.8.2 release timing", "Engineering", "2025-11-14T12:30:00Z"),
        ],
    },
    "INQ-4002": {
        "issue": "Disputed charges for 15 user seats that were not activated",
        "interaction_history": "2 unresolved billing contacts in 9 days",
        "detected_intents": ["billing dispute", "refund request", "renewal risk"],
        "risk_score": 91,
        "case_owner": "Elena Garcia",
        "escalation_reason": "A billing dispute has remained unresolved through two prior contacts.",
        "business_impact": "The customer has paused its expansion and signaled renewal risk.",
        "customer_commitment": "Reverse the ineligible charge, apply a retention credit, and confirm corrected billing.",
        "root_cause": "A seat-expansion order posted before the activation workflow completed.",
        "engineering_work_item": "BILL-214",
        "policy_result": "Billing policy permits a refund for unactivated seats and a manager-approved 10% retention credit.",
        "similar_cases": 12,
        "retention_gesture": "10% service credit on the next invoice",
        "next_update": "2025-11-14T12:00:00Z",
        "actions": [
            ("Verify activation and invoice history", "Elena Garcia", "2025-11-14T10:30:00Z"),
            ("Prepare refund and retention credit", "Billing Operations", "2025-11-14T11:00:00Z"),
            ("Send confirmation and update the customer profile", "Elena Garcia", "2025-11-14T12:00:00Z"),
        ],
    },
    "INQ-4003": {
        "issue": "Enterprise-wide SSO failure after identity-provider migration",
        "interaction_history": "1 critical contact; prior migration advisory completed",
        "detected_intents": ["access outage", "identity migration", "executive escalation"],
        "risk_score": 96,
        "case_owner": "Marcus Lee",
        "escalation_reason": "Enterprise-wide SSO failure following an identity-provider migration.",
        "business_impact": "Employees cannot access production applications.",
        "customer_commitment": "Restore access or establish a safe temporary sign-in path within two hours.",
        "root_cause": "The migrated identity provider is sending an audience value that does not match the service-provider configuration.",
        "engineering_work_item": "INC-907",
        "policy_result": "Critical-incident policy permits a time-boxed break-glass sign-in path.",
        "similar_cases": 4,
        "retention_gesture": "Executive incident review and premium support extension",
        "next_update": "2025-11-14T10:00:00Z",
        "actions": [
            ("Validate SAML audience and ACS values with the customer", "Marcus Lee", "2025-11-14T09:00:00Z"),
            ("Enable a time-boxed break-glass sign-in policy", "Identity Operations", "2025-11-14T09:20:00Z"),
            ("Verify sign-in telemetry after configuration repair", "Tier 2 Engineering", "2025-11-14T09:45:00Z"),
        ],
    },
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _resolve_inquiry(query):
    """Embedded demo inquiries first, then the live tenant case queue
    (by live id or by a title substring, e.g. 'disputed card')."""
    if not query:
        return "INQ-4001"
    q = query.upper().strip()
    if q in _INQUIRIES:
        return q
    live = _live_inquiries()
    if q in live:
        return q
    matches = [
        key for key, inq in live.items()
        if query.lower().strip() in inq["subject"].lower()
    ]
    return matches[0] if len(matches) == 1 else None


def _get_inquiry(inq_id):
    """Unified lookup: embedded demo inquiries first, then live tenant."""
    if inq_id in _INQUIRIES:
        return _INQUIRIES[inq_id]
    return _live_inquiries().get(inq_id) or _INQUIRIES["INQ-4001"]


def _match_kb_articles(inquiry_id):
    inq = _get_inquiry(inquiry_id) if inquiry_id else {}
    subject = inq.get("subject", "").lower()
    matched = []
    for kb_id, article in _KB_ARTICLES.items():
        title_lower = article["title"].lower()
        if any(word in title_lower for word in subject.split() if len(word) > 3):
            matched.append(article)
    if not matched:
        matched = [list(_KB_ARTICLES.values())[0]]
    return sorted(matched, key=lambda a: a["relevance_score"], reverse=True)


def _get_routing(category, priority):
    cat_rules = _ROUTING_RULES.get(category, _ROUTING_RULES["Technical Issue"])
    return cat_rules.get(priority, cat_rules["Medium"])


def _compute_csat_breakdown():
    scores = [s["score"] for s in _SATISFACTION_DATA["surveys"]]
    dist = {i: scores.count(i) for i in range(1, 6)}
    promoters = sum(1 for s in scores if s >= 4)
    detractors = sum(1 for s in scores if s <= 2)
    total = len(scores)
    return dist, promoters, detractors, total


def _resolve_escalation(query):
    if not query:
        return "INQ-4002"
    resolved = _resolve_inquiry(query)
    return resolved if resolved in _ESCALATION_CONTEXT else None


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class AICustomerAssistantAgent(BasicAgent):
    """
    AI-powered customer service assistant.

    Operations:
        handle_inquiry       - triage and respond to a customer inquiry
        knowledge_search     - search knowledge base for relevant articles
        escalation_routing   - determine escalation path and SLA
        satisfaction_survey   - review CSAT scores and survey feedback
        escalation_brief      - consolidate an escalated case and its evidence
        escalation_action_plan - produce owned, time-bound resolution actions
        draft_customer_update - preview a grounded customer status update
        escalation_dashboard  - summarize the active escalation portfolio
        resolution_recommendation - recommend policy-aligned resolution actions
        process_resolution     - simulate approved refund and credit actions
        document_resolution    - simulate case closeout and profile update
    """

    def __init__(self):
        self.name = "AICustomerAssistantAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "handle_inquiry", "knowledge_search",
                            "escalation_routing", "satisfaction_survey",
                            "escalation_brief", "escalation_action_plan",
                            "draft_customer_update", "escalation_dashboard",
                            "resolution_recommendation", "process_resolution",
                            "document_resolution",
                        ],
                        "description": "The customer service operation to perform",
                    },
                    "inquiry_id": {
                        "type": "string",
                        "description": "Inquiry ID (e.g. 'INQ-4001')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "handle_inquiry")
        inq_id = _resolve_inquiry(kwargs.get("inquiry_id", ""))
        escalation_id = _resolve_escalation(kwargs.get("inquiry_id", ""))
        dispatch = {
            "handle_inquiry": self._handle_inquiry,
            "knowledge_search": self._knowledge_search,
            "escalation_routing": self._escalation_routing,
            "satisfaction_survey": self._satisfaction_survey,
            "escalation_brief": self._escalation_brief,
            "escalation_action_plan": self._escalation_action_plan,
            "draft_customer_update": self._draft_customer_update,
            "escalation_dashboard": self._escalation_dashboard,
            "resolution_recommendation": self._resolution_recommendation,
            "process_resolution": self._process_resolution,
            "document_resolution": self._document_resolution,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        if op in {
            "escalation_brief", "escalation_action_plan",
            "escalation_dashboard", "draft_customer_update",
            "resolution_recommendation", "process_resolution",
            "document_resolution",
        }:
            if escalation_id is None:
                return (
                    f"**Error:** Unknown or ineligible escalation inquiry_id "
                    f"`{kwargs.get('inquiry_id')}`. Available escalation IDs: "
                    f"{', '.join(sorted(_ESCALATION_CONTEXT))}."
                )
            return handler(escalation_id)
        if inq_id is None:
            return (
                f"**Error:** Unknown inquiry_id `{kwargs.get('inquiry_id')}`. "
                f"Available inquiry IDs: {', '.join(sorted(_INQUIRIES))}."
            )
        return handler(inq_id)

    # ── handle_inquiry ─────────────────────────────────────────
    def _handle_inquiry(self, inq_id):
        inq = _get_inquiry(inq_id)
        kb_matches = _match_kb_articles(inq_id)
        routing = _get_routing(inq["category"], inq["priority"])
        top_kb = kb_matches[0] if kb_matches else None
        kb_line = f"- Suggested Article: [{top_kb['id']}] {top_kb['title']} (relevance: {top_kb['relevance_score']:.0%})" if top_kb else "- No matching articles found"
        source = (
            "live Static Dynamics 365 tenant (case reinterpreted as inquiry)"
            if inq.get("_live") else "embedded demo layer (offline fallback)"
        )
        return (
            f"**Customer Inquiry: {inq['id']}**\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Customer | {inq['customer']} ({_seam(inq['account_tier'])}) |\n"
            f"| Contact | {inq['contact']} |\n"
            f"| Channel | {inq['channel']} |\n"
            f"| Category | {inq['category']} |\n"
            f"| Priority | {inq['priority']} |\n"
            f"| Sentiment | {_seam(inq['sentiment'])} |\n\n"
            f"**Subject:** {inq['subject']}\n\n"
            f"**Description:** {inq['description']}\n\n"
            f"**Recommended Response:**\n"
            f"{kb_line}\n"
            f"- Assigned Team: {routing['team']}\n"
            f"- SLA Target: {routing['sla_hours']} hours\n"
            f"- Auto-Escalate: {'Yes' if routing['auto_escalate'] else 'No'}\n\n"
            f"Source: [{source}]\nAgents: AICustomerAssistantAgent"
        )

    # ── knowledge_search ───────────────────────────────────────
    def _knowledge_search(self, inq_id):
        articles = _match_kb_articles(inq_id)
        inq = _get_inquiry(inq_id)
        rows = ""
        for a in articles:
            rows += f"| {a['id']} | {a['title']} | {a['relevance_score']:.0%} | {a['views']:,} |\n"
        top = articles[0] if articles else None
        steps = ""
        if top:
            steps = "\n".join(f"{i+1}. {s}" for i, s in enumerate(top["resolution_steps"]))
        return (
            f"**Knowledge Base Search Results**\n"
            f"Query: \"{inq['subject']}\"\n\n"
            f"| Article ID | Title | Relevance | Views |\n|---|---|---|---|\n"
            f"{rows}\n"
            f"**Top Match: {top['title'] if top else 'N/A'}**\n\n"
            f"**Summary:** {top['summary'] if top else 'N/A'}\n\n"
            f"**Resolution Steps:**\n{steps}\n\n"
            f"Last Updated: {top['last_updated'] if top else 'N/A'} | "
            f"Helpful Votes: {top['helpful_votes']:,} / {top['views']:,} views\n\n"
            f"Source: [Knowledge Base]\nAgents: AICustomerAssistantAgent"
        )

    # ── escalation_routing ─────────────────────────────────────
    def _escalation_routing(self, inq_id):
        inq = _get_inquiry(inq_id)
        routing = _get_routing(inq["category"], inq["priority"])
        all_routes = []
        for cat, priorities in _ROUTING_RULES.items():
            for pri, rule in priorities.items():
                all_routes.append(f"| {cat} | {pri} | {rule['team']} | {rule['sla_hours']}h |")
        route_rows = "\n".join(all_routes)
        return (
            f"**Escalation Routing: {inq['id']}**\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Category | {inq['category']} |\n"
            f"| Priority | {inq['priority']} |\n"
            f"| Assigned Team | {routing['team']} |\n"
            f"| SLA Target | {routing['sla_hours']} hours |\n"
            f"| Auto-Escalate | {'Yes' if routing['auto_escalate'] else 'No'} |\n\n"
            f"**Routing Matrix:**\n\n"
            f"| Category | Priority | Team | SLA |\n|---|---|---|---|\n"
            f"{route_rows}\n\n"
            f"Source: [Routing Engine + SLA Configuration]\nAgents: AICustomerAssistantAgent"
        )

    # ── satisfaction_survey ─────────────────────────────────────
    def _satisfaction_survey(self, inq_id):
        data = _SATISFACTION_DATA
        dist, promoters, detractors, total = _compute_csat_breakdown()
        survey_rows = ""
        for s in data["surveys"]:
            stars = "*" * s["score"]
            survey_rows += f"| {s['inquiry_id']} | {stars} ({s['score']}/5) | {s['comment'][:50]} | {s['date']} |\n"
        dist_rows = "\n".join(f"| {score} Star | {count} ({count/total*100:.0f}%) |" for score, count in sorted(dist.items(), reverse=True))
        return (
            f"**Customer Satisfaction Dashboard**\n\n"
            f"| Metric | Value |\n|---|---|\n"
            f"| Overall CSAT | {data['overall_csat']}/5.0 |\n"
            f"| NPS Score | {data['nps_score']} |\n"
            f"| Avg Response Time | {data['response_time_avg_minutes']} minutes |\n"
            f"| First Contact Resolution | {data['first_contact_resolution_rate']:.0%} |\n\n"
            f"**Score Distribution:**\n\n"
            f"| Rating | Count |\n|---|---|\n"
            f"{dist_rows}\n\n"
            f"**Recent Surveys:**\n\n"
            f"| Inquiry | Rating | Comment | Date |\n|---|---|---|---|\n"
            f"{survey_rows}\n"
            f"**Trends:** WoW {data['trend']['week_over_week']}, MoM {data['trend']['month_over_month']}\n\n"
            f"Source: [Survey Platform + CRM Analytics]\nAgents: AICustomerAssistantAgent"
        )

    def _escalation_brief(self, inq_id):
        inq = _get_inquiry(inq_id)
        ctx = _ESCALATION_CONTEXT[inq_id]
        kb = _match_kb_articles(inq_id)[0]
        routing = _get_routing(inq["category"], inq["priority"])
        return (
            f"**Customer Escalation Brief: {inq_id}**\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Customer | {inq['customer']} ({inq['account_tier']}) |\n"
            f"| Contact | {inq['contact']} via {inq['channel']} |\n"
            f"| Status | {inq['status']} / {inq['priority']} / {inq['sentiment']} |\n"
            f"| Escalation Owner | {ctx['case_owner']} |\n"
            f"| Assigned Team | {routing['team']} |\n"
            f"| SLA | {routing['sla_hours']} hours |\n"
            f"| Engineering Work Item | {ctx['engineering_work_item']} |\n"
            f"| Interaction History | {ctx['interaction_history']} |\n"
            f"| Detected Intents | {', '.join(ctx['detected_intents'])} |\n"
            f"| Escalation Risk | {ctx['risk_score']}/100 |\n"
            f"| Similar Cases | {ctx['similar_cases']} |\n"
            f"| Next Customer Update | {ctx['next_update']} |\n\n"
            f"**Escalation Reason:** {ctx['escalation_reason']}\n\n"
            f"**Business Impact:** {ctx['business_impact']}\n\n"
            f"**Root Cause:** {ctx['root_cause']}\n\n"
            f"**Intent Analysis:** {len(ctx['detected_intents'])} issues detected; "
            f"{inq['sentiment'].lower()} sentiment and {inq['priority'].lower()} urgency.\n\n"
            f"**Policy / Eligibility:** {ctx['policy_result']}\n\n"
            f"**Customer Commitment:** {ctx['customer_commitment']}\n\n"
            f"**Supporting Knowledge:** [{kb['id']}] {kb['title']}\n\n"
            f"Source: [Dynamics 365 Customer Service + Knowledge Base + Engineering Work Tracking]\n"
            f"Agents: AICustomerAssistantAgent"
        )

    def _escalation_action_plan(self, inq_id):
        ctx = _ESCALATION_CONTEXT[inq_id]
        rows = "\n".join(
            f"| {index} | {action} | {owner} | {due} | Planned |"
            for index, (action, owner, due) in enumerate(ctx["actions"], 1)
        )
        return (
            f"**Escalation Action Plan: {inq_id}**\n\n"
            f"| # | Action | Owner | Due (UTC) | Status |\n|---|---|---|---|---|\n"
            f"{rows}\n\n"
            f"**Next customer update:** {ctx['next_update']}\n"
            f"**Commitment:** {ctx['customer_commitment']}\n\n"
            f"This is a deterministic offline plan; no CRM, Teams, or engineering records were changed.\n\n"
            f"Source: [Dynamics 365 Customer Service + Microsoft Teams + Engineering Work Tracking]\n"
            f"Agents: AICustomerAssistantAgent"
        )

    def _draft_customer_update(self, inq_id):
        inq = _get_inquiry(inq_id)
        ctx = _ESCALATION_CONTEXT[inq_id]
        first_action = ctx["actions"][0][0]
        return (
            f"**Customer Update Draft: {inq_id}**\n\n"
            f"To: {inq['contact']} <{inq['email']}>\n"
            f"Subject: Update on {ctx['issue']}\n\n"
            f"Hello {inq['contact'].split()[0]},\n\n"
            f"I am {ctx['case_owner']}, and I am coordinating your escalation. "
            f"We understand the impact: {ctx['business_impact']} "
            f"Our current finding is that {ctx['root_cause'].lower()} "
            f"Our immediate next step is to {first_action.lower()} "
            f"We will provide the next update by {ctx['next_update']}.\n\n"
            f"Regards,\n{ctx['case_owner']}\n\n"
            f"**Preview only:** this operation does not send email or update the case.\n\n"
            f"Source: [Dynamics 365 Customer Service + Outlook]\nAgents: AICustomerAssistantAgent"
        )

    def _escalation_dashboard(self, inq_id):
        rows = []
        for case_id, ctx in sorted(_ESCALATION_CONTEXT.items()):
            inq = _INQUIRIES[case_id]
            routing = _get_routing(inq["category"], inq["priority"])
            rows.append(
                f"| {case_id} | {inq['customer']} | {inq['priority']} | {inq['sentiment']} "
                f"| {ctx['case_owner']} | {routing['team']} | {routing['sla_hours']}h "
                f"| {ctx['next_update']} |"
            )
        return (
            f"**Active Customer Escalations**\n\n"
            f"| Case | Customer | Priority | Sentiment | Owner | Team | SLA | Next Update |\n"
            f"|---|---|---|---|---|---|---|---|\n"
            f"{chr(10).join(rows)}\n\n"
            f"Active escalations: {len(rows)} | Critical: "
            f"{sum(_INQUIRIES[key]['priority'] == 'Critical' for key in _ESCALATION_CONTEXT)}\n\n"
            f"Source: [Dynamics 365 Customer Service + SLA Configuration]\n"
            f"Agents: AICustomerAssistantAgent"
        )

    def _resolution_recommendation(self, inq_id):
        ctx = _ESCALATION_CONTEXT[inq_id]
        return (
            f"**Resolution Recommendation: {inq_id}**\n\n"
            f"1. Resolve the root cause: {ctx['root_cause']}\n"
            f"2. Apply the eligible remedy: {ctx['policy_result']}\n"
            f"3. Offer the retention gesture: {ctx['retention_gesture']}.\n"
            f"4. Use the prepared talking points to acknowledge impact and confirm ownership.\n"
            f"5. Complete the follow-up actions by {ctx['next_update']}.\n\n"
            f"**Comparable evidence:** {ctx['similar_cases']} similar resolved cases support this playbook.\n\n"
            f"Source: [SharePoint Playbooks + Dynamics 365 Case History + Billing Policy]\n"
            f"Agents: AICustomerAssistantAgent"
        )

    def _process_resolution(self, inq_id):
        ctx = _ESCALATION_CONTEXT[inq_id]
        if inq_id == "INQ-4002":
            action = "Refund $1,875 for unactivated seats and apply a 10% next-invoice credit"
        else:
            action = f"Apply authorized remedy: {ctx['retention_gesture']}"
        return (
            f"**Simulated Resolution Receipt: {inq_id}**\n\n"
            f"- Action: {action}\n"
            f"- Policy check: Eligible\n"
            f"- Approval: Escalation manager approval assumed for preview\n"
            f"- Dynamics 365 status: Not written\n"
            f"- Billing status: Not written\n\n"
            f"Dry-run only; no refund, credit, or external mutation occurred.\n\n"
            f"Source: [Dynamics 365 CRM + Billing]\nAgents: AICustomerAssistantAgent"
        )

    def _document_resolution(self, inq_id):
        ctx = _ESCALATION_CONTEXT[inq_id]
        return (
            f"**Resolution Documentation Preview: {inq_id}**\n\n"
            f"- Root cause: {ctx['root_cause']}\n"
            f"- Resolution: {ctx['customer_commitment']}\n"
            f"- Similar-case link count: {ctx['similar_cases']}\n"
            f"- Product feedback: Prepared from recurring-case pattern\n"
            f"- Customer profile update: Prepared\n"
            f"- Outlook confirmation: Prepared for approval\n\n"
            f"No case, customer profile, product issue, or email was changed.\n\n"
            f"Source: [Dynamics 365 CRM + SharePoint + Outlook]\nAgents: AICustomerAssistantAgent"
        )


if __name__ == "__main__":
    agent = AICustomerAssistantAgent()
    print("=" * 60)
    print("EMBEDDED DEMO INQUIRY (works offline)")
    print(agent.perform(operation="handle_inquiry", inquiry_id="INQ-4001"))
    print()
    print("=" * 60)
    print("LIVE TENANT INQUIRY (case fetched over HTTP; falls back offline)")
    live_result = agent.perform(
        operation="handle_inquiry", inquiry_id="disputed card transaction"
    )
    if live_result.startswith("**Error:"):
        print("(offline — live tenant unreachable, embedded demo shown above)")
    else:
        print(live_result)
    print()
    for op in [
        "knowledge_search", "escalation_routing",
        "satisfaction_survey", "escalation_brief", "escalation_action_plan",
        "draft_customer_update", "escalation_dashboard",
        "resolution_recommendation", "process_resolution",
        "document_resolution",
    ]:
        print("=" * 60)
        print(agent.perform(operation=op, inquiry_id="INQ-4001"))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
