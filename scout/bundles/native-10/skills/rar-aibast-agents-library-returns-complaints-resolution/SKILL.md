---
name: "rar-aibast-agents-library-returns-complaints-resolution"
description: "Processes returns and complaints from a live simulated Dynamics 365 tenant's service cases, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/returns_complaints_resolution", "rar_sha256": "f6b9bf2368c1baef2175cac9019e0a2fd32622022307361d00f4cacb953e1635", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["returns", "complaints", "customer-service", "resolution", "retail"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/returns_complaints_resolution`. The original RAPP
agent is preserved byte-for-byte in `returns_complaints_resolution_agent.py` and in the RCI capsule.

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

Returns & Complaints Resolution Agent — a template you are meant to mutate.

Handles return processing, complaint classification, resolution
recommendation, and trend analysis for retail customer service operations.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live service cases over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="return_processing")
     — with network up, the queue is built from the tenant's live cases
     (e.g. CAS-260109 "Fabric sample colors differ from order" for
     Maple Thread Textiles). In this template a return/complaint is
     represented as a Dynamics case (incident).
  2. No network? Everything falls back to the embedded demo layer below
     (RETURN_REQUESTS / COMPLAINT_CATEGORIES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     RETURNS_COMPLAINTS_RESOLUTION_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from Zendesk/your OMS), or
     replace _fetch_collection() with your own service API. The fields the
     rest of the file needs are listed in _normalize_live_return() —
     purchase price and product SKU stay "n/a — enrichment seam" until
     you wire your order management system.

OPERATIONS
  return_processing | complaint_classification | resolution_recommendation
  | trend_analysis | escalation_snapshot | recovery_options |
  resolution_execution | follow_up_plan | quality_fraud_analysis |
  recovery_report
  kwargs: operation (required), return_id, complaint_text, key, user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "complaint_text": {
      "type": "string"
    },
    "key": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "return_processing",
        "complaint_classification",
        "resolution_recommendation",
        "trend_analysis",
        "escalation_snapshot",
        "recovery_options",
        "resolution_execution",
        "follow_up_plan",
        "quality_fraud_analysis",
        "recovery_report"
      ],
      "type": "string"
    },
    "return_id": {
      "type": "string"
    },
    "user_input": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `returns_complaints_resolution_agent.py` and embedded as the fenced Python below (sha256 f6b9bf2368c1baef…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `returns_complaints_resolution_agent.py` first:

```bash
python3 returns_complaints_resolution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 returns_complaints_resolution_agent.py   # or on stdin
python3 returns_complaints_resolution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Returns & Complaints Resolution Agent — a template you are meant to mutate.

Handles return processing, complaint classification, resolution
recommendation, and trend analysis for retail customer service operations.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live service cases over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="return_processing")
     — with network up, the queue is built from the tenant's live cases
     (e.g. CAS-260109 "Fabric sample colors differ from order" for
     Maple Thread Textiles). In this template a return/complaint is
     represented as a Dynamics case (incident).
  2. No network? Everything falls back to the embedded demo layer below
     (RETURN_REQUESTS / COMPLAINT_CATEGORIES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     RETURNS_COMPLAINTS_RESOLUTION_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from Zendesk/your OMS), or
     replace _fetch_collection() with your own service API. The fields the
     rest of the file needs are listed in _normalize_live_return() —
     purchase price and product SKU stay "n/a — enrichment seam" until
     you wire your order management system.

OPERATIONS
  return_processing | complaint_classification | resolution_recommendation
  | trend_analysis | escalation_snapshot | recovery_options |
  resolution_execution | follow_up_plan | quality_fraud_analysis |
  recovery_report
  kwargs: operation (required), return_id, complaint_text, key, user_input
"""

import sys
import os

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"),
)
from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timezone

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/returns_complaints_resolution",
    "version": "1.2.0",
    "display_name": "Returns & Complaints Resolution Agent",
    "description": (
        "Processes returns and complaints from a live simulated Dynamics 365 tenant's service cases, with an offline demo fallback."
    ),
    "author": "AIBAST",
    "tags": [
        "returns",
        "complaints",
        "customer-service",
        "resolution",
        "retail",
    ],
    "category": "retail_cpg",
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
#   export RETURNS_COMPLAINTS_RESOLUTION_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your service-desk client.
# Downstream code only needs the fields from _normalize_live_return().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "RETURNS_COMPLAINTS_RESOLUTION_DATA_URL",
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
            rows = json.loads(resp.read().decode("utf-8")).get("value", [])
    except Exception:
        rows = []
    _LIVE_CACHE[collection] = rows
    return rows


def _normalize_live_return(row):
    """Project a Dynamics case (incident) record onto the shape this agent
    uses — in this template a return/complaint IS a Dynamics case.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not available from the service desk
    alone' and the renderers label it as an enrichment seam."""
    return {
        "case_id": row.get("ticketnumber", row.get("incidentid", "")),
        "customer_name": row.get("customeridname", "Unknown"),
        "issue": row.get("title", "untitled"),
        "reason": row.get(
            "casetypecode@OData.Community.Display.V1.FormattedValue", "Unclassified"
        ),
        "channel": row.get(
            "caseorigincode@OData.Community.Display.V1.FormattedValue", "Unknown"
        ),
        "priority": row.get(
            "prioritycode@OData.Community.Display.V1.FormattedValue", "Normal"
        ),
        "status": row.get(
            "statecode@OData.Community.Display.V1.FormattedValue", "Active"
        ),
        "open": row.get("statecode") == 0,
        "age_days": _age_days(row.get("createdon")),
        "purchase_price": None,   # enrichment seam — wire your OMS
        "product_sku": None,      # enrichment seam
        "_live": True,
    }


def _age_days(iso_date):
    try:
        then = datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
        return max(0, (datetime.now(timezone.utc) - then).days)
    except (ValueError, TypeError):
        return 0


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback) — Return Requests
# ---------------------------------------------------------------------------

RETURN_REQUESTS = {
    "RET-4001": {
        "order_id": "ORD-88712",
        "customer_id": "CUST-2041",
        "customer_name": "Sarah Mitchell",
        "product": "Classic Denim Jacket",
        "sku": "SKU-1001",
        "purchase_price": 89.99,
        "purchase_date": "2026-02-14",
        "request_date": "2026-03-02",
        "reason": "wrong_size",
        "condition": "unworn_tags_attached",
        "channel": "online",
        "status": "pending_review",
        "notes": "Ordered size M, needs size L. Willing to exchange.",
    },
    "RET-4002": {
        "order_id": "ORD-89234",
        "customer_id": "CUST-3178",
        "customer_name": "James Kowalski",
        "product": "Smart Fitness Tracker",
        "sku": "SKU-1004",
        "purchase_price": 129.99,
        "purchase_date": "2026-01-20",
        "request_date": "2026-03-10",
        "reason": "defective",
        "condition": "non_functional",
        "channel": "in_store",
        "status": "approved",
        "notes": "Heart rate sensor stopped working after 3 weeks. Under warranty.",
    },
    "RET-4003": {
        "order_id": "ORD-87455",
        "customer_id": "CUST-1590",
        "customer_name": "Maria Chen",
        "product": "Premium Running Shoes",
        "sku": "SKU-1005",
        "purchase_price": 149.99,
        "purchase_date": "2026-02-28",
        "request_date": "2026-03-08",
        "reason": "not_as_described",
        "condition": "lightly_used",
        "channel": "online",
        "status": "pending_review",
        "notes": "Color shown online was navy but received was dark grey.",
    },
    "RET-4004": {
        "order_id": "ORD-90100",
        "customer_id": "CUST-4422",
        "customer_name": "David Okafor",
        "product": "Wireless Earbuds Pro",
        "sku": "SKU-1002",
        "purchase_price": 59.99,
        "purchase_date": "2026-03-01",
        "request_date": "2026-03-12",
        "reason": "changed_mind",
        "condition": "opened_unused",
        "channel": "online",
        "status": "pending_review",
        "notes": "Found a better deal elsewhere. Wants full refund.",
    },
    "RET-4005": {
        "order_id": "ORD-86321",
        "customer_id": "CUST-0887",
        "customer_name": "Linda Park",
        "product": "Leather Crossbody Bag",
        "sku": "SKU-1007",
        "purchase_price": 79.99,
        "purchase_date": "2025-12-18",
        "request_date": "2026-03-14",
        "reason": "defective",
        "condition": "damaged",
        "channel": "in_store",
        "status": "escalated",
        "notes": "Strap broke after normal use. Outside 60-day window but claims manufacturing defect.",
    },
    "RET-4006": {
        "order_id": "ORD-91005",
        "customer_id": "CUST-5610",
        "customer_name": "Robert Fernandez",
        "product": "UV Protection Sunglasses",
        "sku": "SKU-1008",
        "purchase_price": 44.99,
        "purchase_date": "2026-03-05",
        "request_date": "2026-03-15",
        "reason": "wrong_item",
        "condition": "unopened",
        "channel": "online",
        "status": "approved",
        "notes": "Received aviator style instead of ordered wayfarer style.",
    },
}

COMPLAINT_CATEGORIES = {
    "product_quality": {
        "label": "Product Quality",
        "severity_weight": 0.85,
        "avg_resolution_hours": 36,
        "escalation_rate": 0.15,
        "keywords": ["defective", "broken", "poor quality", "fell apart", "not durable"],
        "monthly_volume": 142,
    },
    "order_fulfillment": {
        "label": "Order Fulfillment",
        "severity_weight": 0.70,
        "avg_resolution_hours": 24,
        "escalation_rate": 0.08,
        "keywords": ["wrong item", "missing", "late delivery", "not received", "damaged in shipping"],
        "monthly_volume": 98,
    },
    "pricing_billing": {
        "label": "Pricing & Billing",
        "severity_weight": 0.65,
        "avg_resolution_hours": 18,
        "escalation_rate": 0.05,
        "keywords": ["overcharged", "wrong price", "coupon not applied", "double charged"],
        "monthly_volume": 67,
    },
    "service_experience": {
        "label": "Service Experience",
        "severity_weight": 0.60,
        "avg_resolution_hours": 48,
        "escalation_rate": 0.22,
        "keywords": ["rude staff", "long wait", "unhelpful", "no response", "poor communication"],
        "monthly_volume": 53,
    },
}

RESOLUTION_PLAYBOOKS = {
    "full_refund": {
        "label": "Full Refund",
        "applicable_reasons": ["defective", "wrong_item", "not_as_described"],
        "applicable_conditions": ["non_functional", "unopened", "damaged"],
        "max_days_since_purchase": 90,
        "cost_impact": "high",
        "csat_impact": "high",
        "steps": [
            "Verify purchase and return eligibility",
            "Approve full refund to original payment method",
            "Generate prepaid return shipping label",
            "Send confirmation email with refund timeline",
            "Process refund within 3-5 business days",
        ],
    },
    "exchange": {
        "label": "Product Exchange",
        "applicable_reasons": ["wrong_size", "wrong_item", "not_as_described"],
        "applicable_conditions": ["unworn_tags_attached", "unopened", "opened_unused"],
        "max_days_since_purchase": 60,
        "cost_impact": "medium",
        "csat_impact": "very_high",
        "steps": [
            "Confirm desired replacement item and availability",
            "Generate prepaid return label for original item",
            "Ship replacement item with expedited shipping",
            "Send tracking information for both shipments",
            "Follow up after delivery to confirm satisfaction",
        ],
    },
    "store_credit": {
        "label": "Store Credit",
        "applicable_reasons": ["changed_mind", "wrong_size"],
        "applicable_conditions": ["opened_unused", "lightly_used", "unworn_tags_attached"],
        "max_days_since_purchase": 45,
        "cost_impact": "low",
        "csat_impact": "moderate",
        "steps": [
            "Verify item condition meets return standards",
            "Issue store credit for full purchase amount plus 10% bonus",
            "Credit applied to customer loyalty account",
            "Send email with credit balance and expiration date",
        ],
    },
    "warranty_replacement": {
        "label": "Warranty Replacement",
        "applicable_reasons": ["defective"],
        "applicable_conditions": ["non_functional", "damaged"],
        "max_days_since_purchase": 365,
        "cost_impact": "medium",
        "csat_impact": "high",
        "steps": [
            "Verify product is within warranty period",
            "Collect defect documentation and photos",
            "Submit warranty claim to manufacturer",
            "Ship replacement from warranty stock",
            "Allow customer to keep defective unit or provide return label",
        ],
    },
    "partial_refund": {
        "label": "Partial Refund",
        "applicable_reasons": ["not_as_described", "changed_mind"],
        "applicable_conditions": ["lightly_used"],
        "max_days_since_purchase": 30,
        "cost_impact": "medium",
        "csat_impact": "moderate",
        "steps": [
            "Assess item condition and determine refund percentage",
            "Apply restocking fee if applicable (15% for opened items)",
            "Process partial refund to original payment method",
            "Notify customer of refund amount and timeline",
        ],
    },
}

TREND_DATA = {
    "months": ["2025-10", "2025-11", "2025-12", "2026-01", "2026-02", "2026-03"],
    "total_returns": [312, 345, 498, 387, 328, 360],
    "return_rate_pct": [4.1, 4.5, 6.2, 5.0, 4.3, 4.7],
    "top_return_reasons": {
        "wrong_size": [98, 112, 160, 125, 105, 115],
        "defective": [72, 68, 95, 82, 71, 78],
        "changed_mind": [65, 78, 130, 88, 70, 80],
        "not_as_described": [45, 52, 68, 55, 48, 52],
        "wrong_item": [32, 35, 45, 37, 34, 35],
    },
    "avg_resolution_hours": [28.5, 30.2, 38.7, 32.1, 27.8, 29.4],
    "csat_score": [4.1, 4.0, 3.6, 3.9, 4.2, 4.1],
    "refund_total_usd": [18720.00, 21450.00, 34200.00, 24800.00, 19650.00, 22100.00],
}

EVIDENCE_CAPABILITIES = {
    "escalation_snapshot": {
        "title": "Escalated Complaint Snapshot",
        "source_system": "Dynamics 365 Customer Service and Outlook",
        "write": False,
        "key_field": "case_id",
        "summary": (
            "Combines customer value, purchase history, support interactions, "
            "sentiment, and churn risk into an immediate-action snapshot."
        ),
        "record": {
            "case_id": "CASE-DAVID-CHEN",
            "customer": "David Chen; Diamond VIP; 47 purchases; $18,400 lifetime value",
            "issue": "ProBook Elite 15 display flickers and will not boot on day 3",
            "warranty": "Active 2-year standard warranty",
            "history": "45-minute hold with three transfers, followed by failed troubleshooting",
            "sentiment": "High frustration after two failed support calls",
            "churn_risk": "87%; immediate recovery action recommended",
        },
    },
    "recovery_options": {
        "title": "Customer-Value Recovery Options",
        "source_system": "Dynamics 365 Customer Service",
        "write": False,
        "key_field": "option_set_id",
        "summary": (
            "Compares resolution tiers by fulfillment speed, recovery cost, "
            "retention probability, and customer lifetime value."
        ),
        "record": {
            "option_set_id": "OPTIONS-DAVID-CHEN",
            "tier_1": "Elite Plus upgrade; same-day courier; $200 credit; 90-day extension; $540 cost",
            "tier_2": "Same-model replacement; 2-day shipping; $100 credit; $180 cost; 65% retention",
            "tier_3": "Same-model replacement; standard 5-day shipping; $0 incremental cost; 35% retention",
            "recommendation": "Tier 1 protects $18,400 lifetime value for $540, a 34:1 retention ROI",
        },
    },
    "resolution_execution": {
        "title": "Resolution Execution and Talking Points",
        "source_system": "Dynamics 365 Customer Service, Outlook, and Teams",
        "write": True,
        "key_field": "resolution_id",
        "summary": (
            "Prepares approved fulfillment, credit, return, and empathetic "
            "communication actions while keeping every external write simulated."
        ),
        "record": {
            "resolution_id": "RESOLUTION-DAVID-TIER1",
            "fulfillment": "Elite Plus upgrade prepared for same-day courier delivery at 4:30 PM",
            "credit": "$200 store credit and 90-day return extension prepared",
            "return": "Return label prepared for the defective laptop",
            "talking_points": "Apologize, acknowledge Diamond status, explain upgrade and speed, confirm credit, provide direct ownership",
            "execution_note": "Simulation only; no shipment, credit, label, or customer message is created",
        },
    },
    "follow_up_plan": {
        "title": "Service Recovery Follow-Up Plan",
        "source_system": "Dynamics 365 Customer Service and Outlook",
        "write": True,
        "key_field": "follow_up_id",
        "summary": (
            "Prepares structured post-resolution touchpoints and monitoring "
            "without scheduling messages or changing a customer record."
        ),
        "record": {
            "follow_up_id": "FOLLOWUP-DAVID-30D",
            "today": "Delivery confirmation at 18:00 and manager email at 19:00",
            "day_3": "Customer success call and NPS survey",
            "day_7": "Elite Plus tips and 25% accessory offer",
            "day_30": "Relationship health check and VIP appreciation invitation",
            "monitoring": "90-day ticket priority, churn-risk tracking, and purchase-behavior analysis",
            "execution_note": "Simulation only; no communication, task, or CRM update is scheduled",
        },
    },
    "quality_fraud_analysis": {
        "title": "SKU Quality and Return Fraud Analysis",
        "source_system": "Dynamics 365 Commerce and Customer Service",
        "write": False,
        "key_field": "analysis_id",
        "summary": (
            "Surfaces deterministic SKU-level defect and suspicious-return "
            "patterns for quality and loss-prevention review."
        ),
        "record": {
            "analysis_id": "ANALYSIS-PROBOOK-Q2",
            "quality_signal": "Display-failure returns reached 4.8%, above the 1.5% category baseline",
            "affected_batch": "ProBook Elite 15 batch PB15-0426; 23 related cases",
            "fraud_signal": "Three accounts share delivery addresses across seven high-value return requests",
            "recommended_actions": "Open supplier quality review; hold affected batch; route linked accounts to loss prevention",
            "decision_boundary": "Signals require human review; no return is denied automatically",
        },
    },
    "recovery_report": {
        "title": "Service Recovery Executive Report",
        "source_system": "Microsoft Teams",
        "write": True,
        "key_field": "report_id",
        "summary": (
            "Produces case and program economics with a simulated leadership "
            "distribution receipt."
        ),
        "record": {
            "report_id": "REPORT-RECOVERY-Q2",
            "case_result": "Resolved in 4 hours; $18,400 lifetime value protected for $540; 34:1 retention ROI",
            "program_metrics": "4.2-hour resolution; 94% retention; +47 NPS recovery; 76% six-month repeat purchase",
            "program_economics": "$127,000 quarterly investment; $4.8M protected revenue; $4.67M net value",
            "executive_summary": "Customer crisis converted into a loyalty recovery with structured 30-day follow-up",
            "distribution": "Prepared for leadership review in Microsoft Teams",
        },
    },
}

_EVIDENCE_KEY_PUNCTUATION = "-_.,:;()?!/#@+$%^&*=[]{}<>~`'\""


def _normalize_evidence_tokens(text):
    tokens = []
    for raw in str(text).split():
        cleaned = "".join(
            character.lower()
            for character in raw
            if character not in _EVIDENCE_KEY_PUNCTUATION
        )
        if cleaned:
            tokens.append(cleaned)
    return tokens


def _record_for_evidence_request(capability, key, user_input):
    record = capability["record"]
    key_field = capability["key_field"]
    if key:
        if str(record[key_field]).lower() == str(key).strip().lower():
            return "match", record
        return "not_found", None
    query_tokens = _normalize_evidence_tokens(user_input)
    key_tokens = _normalize_evidence_tokens(record[key_field])
    width = len(key_tokens)
    if width and any(
        query_tokens[index:index + width] == key_tokens
        for index in range(len(query_tokens) - width + 1)
    ):
        return "match", record
    return "summary", None


def _format_evidence_record(record):
    return "\n".join(
        f"- **{field.replace('_', ' ').title()}:** {value}"
        for field, value in record.items()
    )


# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------

def _days_since_purchase(ret):
    """Calculate days between purchase and return request (simplified)."""
    purchase_parts = ret["purchase_date"].split("-")
    request_parts = ret["request_date"].split("-")
    p_days = int(purchase_parts[0]) * 365 + int(purchase_parts[1]) * 30 + int(purchase_parts[2])
    r_days = int(request_parts[0]) * 365 + int(request_parts[1]) * 30 + int(request_parts[2])
    return r_days - p_days


def _classify_complaint(text):
    """Classify complaint text into a category based on keyword matching."""
    text_lower = text.lower()
    best_cat = "service_experience"
    best_score = 0
    for cat_id, cat in COMPLAINT_CATEGORIES.items():
        score = sum(1 for kw in cat["keywords"] if kw in text_lower)
        if score > best_score:
            best_score = score
            best_cat = cat_id
    return best_cat


def _recommend_resolution(ret):
    """Pick best resolution playbook for a return request."""
    reason = ret["reason"]
    condition = ret["condition"]
    days = _days_since_purchase(ret)
    best_match = None
    for pb_id, pb in RESOLUTION_PLAYBOOKS.items():
        if reason in pb["applicable_reasons"] and condition in pb["applicable_conditions"]:
            if days <= pb["max_days_since_purchase"]:
                if best_match is None or pb["csat_impact"] in ("very_high", "high"):
                    best_match = pb_id
    return best_match or "store_credit"


def _return_rate_trend():
    """Calculate return-rate trend direction."""
    rates = TREND_DATA["return_rate_pct"]
    recent_avg = sum(rates[-3:]) / 3
    earlier_avg = sum(rates[:3]) / 3
    if recent_avg < earlier_avg - 0.3:
        return "improving"
    elif recent_avg > earlier_avg + 0.3:
        return "worsening"
    return "stable"


# ---------------------------------------------------------------------------
# Agent Class
# ---------------------------------------------------------------------------

class ReturnsComplaintsResolutionAgent(BasicAgent):
    """Agent for automated returns processing and complaint resolution."""

    def __init__(self):
        self.name = "returns-complaints-resolution-agent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "return_processing",
                            "complaint_classification",
                            "resolution_recommendation",
                            "trend_analysis",
                            "escalation_snapshot",
                            "recovery_options",
                            "resolution_execution",
                            "follow_up_plan",
                            "quality_fraud_analysis",
                            "recovery_report",
                        ],
                    },
                    "return_id": {"type": "string"},
                    "complaint_text": {"type": "string"},
                    "key": {"type": "string"},
                    "user_input": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _live_return_queue(self, cases):
        """Case queue built from live tenant records (preferred online)."""
        open_cases = [c for c in cases if c["open"]]
        lines = [
            "# Return & Complaint Queue — Live Tenant Cases",
            "",
            f"Live records from {DATA_SOURCE_URL} (Aster Lane Office Systems).",
            "In this template a return/complaint is a Dynamics case. Pass",
            "`return_id` (e.g. RET-4001) for the embedded demo return view.",
            "",
            "| Case | Customer | Issue | Type | Priority | Channel | Age | Value |",
            "|------|----------|-------|------|----------|---------|-----|-------|",
        ]
        for c in sorted(open_cases, key=lambda x: x["case_id"]):
            price = (
                "n/a — enrichment seam"
                if c["purchase_price"] is None
                else f"${c['purchase_price']:.2f}"
            )
            lines.append(
                f"| {c['case_id']} | {c['customer_name']} | {c['issue']} "
                f"| {c['reason']} | {c['priority']} | {c['channel']} "
                f"| {c['age_days']}d | {price} |"
            )
        high = sum(1 for c in open_cases if c["priority"] == "High")
        lines.append("")
        lines.append(
            f"**Open cases:** {len(open_cases)} of {len(cases)} total | "
            f"**High priority:** {high}"
        )
        lines.append(
            "Purchase price and product SKU need your order management system — "
            "wire it at the LIVE DATA SEAM."
        )
        return "\n".join(lines)

    def _return_processing(self, **kwargs):
        return_id = kwargs.get("return_id")
        if return_id and return_id in RETURN_REQUESTS:
            returns = {return_id: RETURN_REQUESTS[return_id]}
        else:
            live = [_normalize_live_return(r) for r in _fetch_collection("incidents")]
            live = [c for c in live if c["case_id"]]
            if live:
                return self._live_return_queue(live)
            returns = RETURN_REQUESTS
        lines = ["# Return Processing Queue", ""]
        lines.append("| Return ID | Customer | Product | Reason | Condition | Days | Status |")
        lines.append("|-----------|----------|---------|--------|-----------|------|--------|")
        for rid, ret in returns.items():
            days = _days_since_purchase(ret)
            lines.append(
                f"| {rid} | {ret['customer_name']} | {ret['product']} "
                f"| {ret['reason'].replace('_', ' ')} | {ret['condition'].replace('_', ' ')} "
                f"| {days} | {ret['status'].replace('_', ' ')} |"
            )
        lines.append("")
        for rid, ret in returns.items():
            lines.append(f"### {rid} — {ret['product']}")
            lines.append("")
            lines.append(f"- **Order:** {ret['order_id']}")
            lines.append(f"- **Customer:** {ret['customer_name']} (`{ret['customer_id']}`)")
            lines.append(f"- **Purchase Date:** {ret['purchase_date']} | **Request Date:** {ret['request_date']}")
            lines.append(f"- **Channel:** {ret['channel']}")
            lines.append(f"- **Price:** ${ret['purchase_price']:.2f}")
            lines.append(f"- **Notes:** {ret['notes']}")
            lines.append("")
        pending = sum(1 for r in RETURN_REQUESTS.values() if r["status"] == "pending_review")
        total_value = sum(r["purchase_price"] for r in returns.values())
        lines.append(f"**Pending Reviews:** {pending} | **Queue Value:** ${total_value:,.2f}")
        return "\n".join(lines)

    def _complaint_classification(self, **kwargs):
        complaint_text = kwargs.get("complaint_text", "")
        lines = ["# Complaint Classification", ""]
        if complaint_text:
            cat_id = _classify_complaint(complaint_text)
            cat = COMPLAINT_CATEGORIES[cat_id]
            lines.append(f"**Input:** \"{complaint_text}\"")
            lines.append(f"**Classified As:** {cat['label']} (`{cat_id}`)")
            lines.append(f"**Severity Weight:** {cat['severity_weight']}")
            lines.append(f"**Avg Resolution Time:** {cat['avg_resolution_hours']}h")
            lines.append(f"**Escalation Rate:** {cat['escalation_rate']*100:.0f}%")
            lines.append("")
        lines.append("## Complaint Category Reference")
        lines.append("")
        lines.append("| Category | Monthly Volume | Severity | Avg Resolution | Escalation Rate |")
        lines.append("|----------|---------------|----------|----------------|-----------------|")
        total_volume = 0
        for cat_id, cat in COMPLAINT_CATEGORIES.items():
            total_volume += cat["monthly_volume"]
            lines.append(
                f"| {cat['label']} | {cat['monthly_volume']} "
                f"| {cat['severity_weight']:.2f} | {cat['avg_resolution_hours']}h "
                f"| {cat['escalation_rate']*100:.0f}% |"
            )
        lines.append("")
        lines.append(f"**Total Monthly Complaints:** {total_volume}")
        return "\n".join(lines)

    def _resolution_recommendation(self, **kwargs):
        return_id = kwargs.get("return_id")
        if return_id and return_id in RETURN_REQUESTS:
            returns = {return_id: RETURN_REQUESTS[return_id]}
        else:
            returns = {k: v for k, v in RETURN_REQUESTS.items() if v["status"] == "pending_review"}
        lines = ["# Resolution Recommendations", ""]
        for rid, ret in returns.items():
            rec_id = _recommend_resolution(ret)
            playbook = RESOLUTION_PLAYBOOKS[rec_id]
            lines.append(f"## {rid} — {ret['customer_name']}")
            lines.append("")
            lines.append(f"- **Product:** {ret['product']} (${ret['purchase_price']:.2f})")
            lines.append(f"- **Reason:** {ret['reason'].replace('_', ' ')}")
            lines.append(f"- **Recommended Resolution:** {playbook['label']}")
            lines.append(f"- **Cost Impact:** {playbook['cost_impact']} | **CSAT Impact:** {playbook['csat_impact']}")
            lines.append("")
            lines.append("**Resolution Steps:**")
            for i, step in enumerate(playbook["steps"], 1):
                lines.append(f"  {i}. {step}")
            lines.append("")
        lines.append("## Available Resolution Playbooks")
        lines.append("")
        for pb_id, pb in RESOLUTION_PLAYBOOKS.items():
            lines.append(f"- **{pb['label']}** (`{pb_id}`): Window {pb['max_days_since_purchase']}d, "
                         f"Cost: {pb['cost_impact']}, CSAT: {pb['csat_impact']}")
        return "\n".join(lines)

    def _trend_analysis(self, **kwargs):
        trend_dir = _return_rate_trend()
        lines = [
            "# Returns & Complaints Trend Analysis",
            "",
            f"**Overall Trend:** {trend_dir.upper()}",
            "",
            "## Monthly Returns Overview",
            "",
            "| Month | Total Returns | Return Rate | Avg Resolution | CSAT | Refund Total |",
            "|-------|--------------|-------------|----------------|------|--------------|",
        ]
        for i, month in enumerate(TREND_DATA["months"]):
            lines.append(
                f"| {month} | {TREND_DATA['total_returns'][i]} "
                f"| {TREND_DATA['return_rate_pct'][i]}% "
                f"| {TREND_DATA['avg_resolution_hours'][i]}h "
                f"| {TREND_DATA['csat_score'][i]}/5.0 "
                f"| ${TREND_DATA['refund_total_usd'][i]:,.2f} |"
            )
        lines.append("")
        lines.append("## Return Reasons Breakdown (Last 6 Months)")
        lines.append("")
        for reason, volumes in TREND_DATA["top_return_reasons"].items():
            total = sum(volumes)
            avg = round(total / len(volumes), 1)
            lines.append(f"- **{reason.replace('_', ' ').title()}:** {total} total, {avg} avg/month")
        lines.append("")
        total_refunded = sum(TREND_DATA["refund_total_usd"])
        lines.append(f"**Total Refunded (6 months):** ${total_refunded:,.2f}")
        lines.append("")
        lines.append("## Key Insights")
        lines.append("")
        lines.append("- Holiday season (Dec) drove a 44% spike in returns, primarily changed-mind returns")
        lines.append("- Wrong-size returns consistently highest — consider enhanced size guide implementation")
        lines.append("- Resolution time improved 8% over the period despite volume increases")
        lines.append("- CSAT recovered to 4.1 after post-holiday dip to 3.6")
        return "\n".join(lines)

    def _evidence_capability(self, capability_name, **kwargs):
        capability = EVIDENCE_CAPABILITIES[capability_name]
        lookup_status, record = _record_for_evidence_request(
            capability,
            kwargs.get("key", ""),
            kwargs.get("user_input", ""),
        )
        lines = [
            f"# {capability['title']}",
            "",
            capability["summary"],
            "",
            f"## {capability['source_system']} (synthetic demo data)",
            "",
        ]
        if lookup_status == "not_found":
            lines.append(
                f"No record matched the requested {capability['key_field']}. "
                "Not substituting another record."
            )
        else:
            selected = record or capability["record"]
            label = "Exact keyed record" if lookup_status == "match" else "Worked example"
            lines.extend([f"**{label}:**", _format_evidence_record(selected)])

        if capability["write"] and lookup_status == "match":
            receipt_key = record[capability["key_field"]]
            lines.extend([
                "",
                "## Simulated Write Receipt",
                "",
                "- **Action Status:** simulated",
                f"- **Receipt:** SIM-{capability_name.upper()}-{receipt_key}",
                f"- **Target System:** {capability['source_system']}",
                "- **External Changes:** none; no live fulfillment, credit, communication, or record update occurred",
            ])
        elif capability["write"]:
            lines.extend([
                "",
                "_Write-capable workflow; provide an exact key to generate a "
                "simulated receipt. No external system is modified._",
            ])
        else:
            lines.extend(["", "_Read-only; no external system is modified._"])
        return "\n".join(lines)

    def perform(self, **kwargs):
        operation = kwargs.get("operation", "return_processing")
        dispatch = {
            "return_processing": self._return_processing,
            "complaint_classification": self._complaint_classification,
            "resolution_recommendation": self._resolution_recommendation,
            "trend_analysis": self._trend_analysis,
            "escalation_snapshot": self._evidence_capability,
            "recovery_options": self._evidence_capability,
            "resolution_execution": self._evidence_capability,
            "follow_up_plan": self._evidence_capability,
            "quality_fraud_analysis": self._evidence_capability,
            "recovery_report": self._evidence_capability,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"Unknown operation `{operation}`. Valid: {', '.join(dispatch.keys())}"
        if operation in EVIDENCE_CAPABILITIES:
            return handler(operation, **kwargs)
        return handler(**kwargs)


# ---------------------------------------------------------------------------
# Main — exercise all operations
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = ReturnsComplaintsResolutionAgent()
    print("=" * 80)
    print("EMBEDDED DEMO RETURN (works offline)")
    print(agent.perform(operation="return_processing", return_id="RET-4001"))
    print("\n" + "=" * 80)
    print("LIVE TENANT CASE QUEUE (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="return_processing"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="complaint_classification", complaint_text="The product fell apart after one week, poor quality stitching"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="resolution_recommendation", return_id="RET-4001"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="trend_analysis"))
    print("=" * 80)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
