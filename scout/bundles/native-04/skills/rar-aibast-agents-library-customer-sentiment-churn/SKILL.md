---
name: "rar-aibast-agents-library-customer-sentiment-churn"
description: "Scores churn risk and plans retention from a live simulated Dynamics 365 tenant (cases as sentiment signals), with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/customer_sentiment_churn", "rar_sha256": "196850ced898f6460b04bf9cf38f7cc8f5eb59f0a23c87a920a6b0fa42977c99", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["sentiment", "churn", "retention", "NPS", "analytics", "financial-services"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/customer_sentiment_churn`. The original RAPP
agent is preserved byte-for-byte in `customer_sentiment_churn_agent.py` and in the RCI capsule.

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

Customer Sentiment & Churn Agent — a template you are meant to mutate.

Analyzes customer sentiment, predicts churn risk, recommends retention
actions, and provides segment-level insights for financial institutions.
In this template an account is a customer relationship and a support case
is a complaint/sentiment signal — the tenant has no native NPS entity, so
case volume and priority stand in for dissatisfaction signals.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `churn_prediction` operation pulls live
     account and case records over real HTTP from the globally hosted
     Static Dynamics 365 tenant (Aster Lane Office Systems — synthetic
     data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="churn_prediction")
     and look for Bluegrass Credit Union's open "Disputed card
     transaction under investigation" case driving its risk score.
  2. No network? Everything falls back to the embedded demo layer below
     (CUSTOMER_INTERACTIONS / CHURN_INDICATORS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CUSTOMER_SENTIMENT_CHURN_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your case/survey system), or
     replace _fetch_collection() with your own client. The fields the rest
     of the file needs are listed in _normalize_live_customer() — fields
     rendered "n/a — enrichment seam" (NPS, transactions, digital
     engagement) are where you wire your survey and core banking systems.

OPERATIONS
  sentiment_dashboard | churn_prediction | retention_actions
  | segment_analysis | churn_risk_scoring | early_warning_signals
  | customer_snapshot | retention_strategy | retention_coordination
  kwargs: operation (required), customer_id, user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "sentiment_dashboard",
        "churn_prediction",
        "retention_actions",
        "segment_analysis",
        "churn_risk_scoring",
        "early_warning_signals",
        "customer_snapshot",
        "retention_strategy",
        "retention_coordination"
      ],
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_sentiment_churn_agent.py` and embedded as the fenced Python below (sha256 196850ced898f646…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_sentiment_churn_agent.py` first:

```bash
python3 customer_sentiment_churn_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 customer_sentiment_churn_agent.py   # or on stdin
python3 customer_sentiment_churn_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Customer Sentiment & Churn Agent — a template you are meant to mutate.

Analyzes customer sentiment, predicts churn risk, recommends retention
actions, and provides segment-level insights for financial institutions.
In this template an account is a customer relationship and a support case
is a complaint/sentiment signal — the tenant has no native NPS entity, so
case volume and priority stand in for dissatisfaction signals.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `churn_prediction` operation pulls live
     account and case records over real HTTP from the globally hosted
     Static Dynamics 365 tenant (Aster Lane Office Systems — synthetic
     data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="churn_prediction")
     and look for Bluegrass Credit Union's open "Disputed card
     transaction under investigation" case driving its risk score.
  2. No network? Everything falls back to the embedded demo layer below
     (CUSTOMER_INTERACTIONS / CHURN_INDICATORS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CUSTOMER_SENTIMENT_CHURN_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your case/survey system), or
     replace _fetch_collection() with your own client. The fields the rest
     of the file needs are listed in _normalize_live_customer() — fields
     rendered "n/a — enrichment seam" (NPS, transactions, digital
     engagement) are where you wire your survey and core banking systems.

OPERATIONS
  sentiment_dashboard | churn_prediction | retention_actions
  | segment_analysis | churn_risk_scoring | early_warning_signals
  | customer_snapshot | retention_strategy | retention_coordination
  kwargs: operation (required), customer_id, user_input
"""

import sys
import os
import hashlib

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json as _json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/customer_sentiment_churn",
    "version": "1.2.0",
    "display_name": "Customer Sentiment & Churn Agent",
    "description": "Scores churn risk and plans retention from a live simulated Dynamics 365 tenant (cases as sentiment signals), with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["sentiment", "churn", "retention", "NPS", "analytics", "financial-services"],
    "category": "financial_services",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ---------------------------------------------------------------------------
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export CUSTOMER_SENTIMENT_CHURN_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM/survey client. Downstream
# code only needs the fields produced by _normalize_live_customer().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "CUSTOMER_SENTIMENT_CHURN_DATA_URL",
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
    """Project a Dynamics account + its cases onto the customer shape this
    agent uses. THIS is the contract your replacement data source must meet
    — a dict with these keys. None means 'not knowable from the CRM alone'
    and the renderers label it as an enrichment seam."""
    name = row.get("name", "Unknown")
    cases = [i for i in incidents if i.get("customeridname") == name]
    open_cases = [i for i in cases if i.get("statecode") == 0]
    high_priority_open = [i for i in open_cases if i.get("prioritycode") == 1]
    return {
        "name": name,
        "segment": row.get("industrycode", "unknown"),
        "nps_score": None,                 # enrichment seam — wire your survey platform
        "monthly_transactions": None,      # enrichment seam — wire your core banking system
        "digital_engagement_score": None,  # enrichment seam
        "complaint_count_12m": len(cases),
        "open_cases": len(open_cases),
        "high_priority_open": len(high_priority_open),
        "top_signal": (open_cases[0].get("title") if open_cases else "No open cases"),
        "_live": True,
    }


def _live_customers():
    """account-number-keyed dict of live tenant customers; {} when offline."""
    rows = _fetch_collection("accounts")
    if not rows:
        return {}
    incidents = _fetch_collection("incidents")
    return {
        row.get("accountnumber", row.get("accountid", "")): _normalize_live_customer(row, incidents)
        for row in rows
        if row.get("name")
    }


def _live_churn_score(customer):
    """Churn risk from real case signals: open cases, high-priority open
    cases, and lifetime complaint volume. Real computation, live inputs."""
    return min(
        95,
        customer["open_cases"] * 18
        + customer["high_priority_open"] * 12
        + customer["complaint_count_12m"] * 4,
    )


def _seam(value):
    """None = the CRM alone can't know this (enrichment seam)."""
    return "n/a — enrichment seam" if value is None else str(value)


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

CUSTOMER_INTERACTIONS = {
    "CUST-8001": {
        "name": "Elizabeth Warren-Hayes",
        "segment": "affluent",
        "tenure_years": 12,
        "products": ["checking", "savings", "mortgage", "investment"],
        "nps_score": 9,
        "last_survey": "2025-02-01",
        "recent_interactions": [
            {"date": "2025-02-15", "channel": "branch", "type": "inquiry", "sentiment": "positive"},
            {"date": "2025-01-20", "channel": "phone", "type": "account_service", "sentiment": "neutral"},
        ],
        "monthly_transactions": 48,
        "digital_engagement_score": 72,
        "complaint_count_12m": 0,
    },
    "CUST-8002": {
        "name": "Marcus Johnson",
        "segment": "mass_market",
        "tenure_years": 3,
        "products": ["checking", "credit_card"],
        "nps_score": 4,
        "last_survey": "2025-01-15",
        "recent_interactions": [
            {"date": "2025-03-01", "channel": "phone", "type": "complaint", "sentiment": "negative"},
            {"date": "2025-02-10", "channel": "chat", "type": "fee_dispute", "sentiment": "negative"},
            {"date": "2025-01-25", "channel": "phone", "type": "complaint", "sentiment": "negative"},
        ],
        "monthly_transactions": 15,
        "digital_engagement_score": 35,
        "complaint_count_12m": 5,
    },
    "CUST-8003": {
        "name": "Priya Sharma",
        "segment": "emerging_affluent",
        "tenure_years": 5,
        "products": ["checking", "savings", "credit_card", "auto_loan"],
        "nps_score": 7,
        "last_survey": "2025-02-20",
        "recent_interactions": [
            {"date": "2025-02-28", "channel": "mobile", "type": "transfer", "sentiment": "neutral"},
            {"date": "2025-02-05", "channel": "email", "type": "inquiry", "sentiment": "positive"},
        ],
        "monthly_transactions": 32,
        "digital_engagement_score": 88,
        "complaint_count_12m": 1,
    },
    "CUST-8004": {
        "name": "Gerald Thompson",
        "segment": "mass_market",
        "tenure_years": 8,
        "products": ["checking"],
        "nps_score": 3,
        "last_survey": "2024-11-01",
        "recent_interactions": [
            {"date": "2024-12-15", "channel": "branch", "type": "withdrawal", "sentiment": "neutral"},
        ],
        "monthly_transactions": 4,
        "digital_engagement_score": 12,
        "complaint_count_12m": 2,
    },
    "CUST-8005": {
        "name": "Diana Castellano",
        "segment": "small_business",
        "tenure_years": 6,
        "products": ["business_checking", "business_credit", "merchant_services"],
        "nps_score": 6,
        "last_survey": "2025-01-10",
        "recent_interactions": [
            {"date": "2025-02-20", "channel": "phone", "type": "fee_dispute", "sentiment": "negative"},
            {"date": "2025-01-30", "channel": "branch", "type": "inquiry", "sentiment": "neutral"},
        ],
        "monthly_transactions": 120,
        "digital_engagement_score": 55,
        "complaint_count_12m": 3,
    },
}

CHURN_INDICATORS = {
    "low_nps": {"threshold": 5, "weight": 25, "description": "NPS score below 5 indicates detractor status"},
    "declining_transactions": {"threshold": 10, "weight": 20, "description": "Monthly transactions below segment average"},
    "high_complaints": {"threshold": 3, "weight": 20, "description": "3+ complaints in last 12 months"},
    "low_engagement": {"threshold": 30, "weight": 15, "description": "Digital engagement score below 30"},
    "single_product": {"threshold": 1, "weight": 10, "description": "Only one active product"},
    "stale_survey": {"threshold": 90, "weight": 10, "description": "Last survey response over 90 days ago"},
}

RETENTION_ACTIONS = {
    "fee_waiver": {"description": "Waive monthly maintenance fees for 6 months", "cost": 72, "success_rate": 45},
    "rate_upgrade": {"description": "Offer premium savings rate for 12 months", "cost": 150, "success_rate": 35},
    "personal_outreach": {"description": "Schedule call with relationship manager", "cost": 25, "success_rate": 55},
    "product_bundle": {"description": "Offer discounted product bundle with waived fees", "cost": 200, "success_rate": 60},
    "loyalty_bonus": {"description": "Credit loyalty bonus to account", "cost": 100, "success_rate": 50},
    "complaint_resolution": {"description": "Escalate to service recovery team", "cost": 50, "success_rate": 65},
}

SEGMENT_BENCHMARKS = {
    "affluent": {"avg_nps": 8.2, "avg_products": 4.1, "avg_tenure": 10, "avg_transactions": 55},
    "emerging_affluent": {"avg_nps": 7.0, "avg_products": 3.2, "avg_tenure": 5, "avg_transactions": 35},
    "mass_market": {"avg_nps": 6.5, "avg_products": 2.0, "avg_tenure": 4, "avg_transactions": 20},
    "small_business": {"avg_nps": 6.8, "avg_products": 3.0, "avg_tenure": 5, "avg_transactions": 90},
}


# ---------------------------------------------------------------------------
# Extended capability library (v1.1.0)
#
# Self-contained data for the five newer sentiment/churn capabilities derived
# from the external agent spec. Each entry carries the spec `response` line,
# the `knowledge` citations, three synthetic `records`, the exact-lookup
# `key_field`, and the `write`/`generative` flags. Nothing external is called:
# `write` capabilities return a simulated receipt only — no live mutations.
# ---------------------------------------------------------------------------

CAPABILITY_LIBRARY = {
    "churn_risk_scoring": {
        "display_name": "Churn Risk Scoring",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": False,
        "exact_key_required": True,
        "key_field": "account_id",
        "response": "Here is the sentiment-driven churn risk analysis across your customer base, prioritized by risk level and account value.",
        "knowledge": [
            "Analyze sentiment across all customer touchpoints (one-pager, Slide 1).",
            "Score churn risk by unifying sentiment, behavior, and all activity (one-pager, Slide 1).",
            "In moments the agent processes a large volume of diverse data and identifies customers with elevated churn risk with minimal effort (demo 00:00:52-00:01:01).",
            "The manager receives a prioritized list of high-risk accounts and key drivers, insights that used to be difficult to obtain (demo 00:01:01-00:01:08).",
        ],
        "records": [
            {"account_id": "ACCT7781", "customer": "Northwind Freight", "churn_risk": "High", "sentiment_score": "-0.62", "primary_driver": "Repeated billing disputes"},
            {"account_id": "ACCT4419", "customer": "Larkspur Retail", "churn_risk": "Medium", "sentiment_score": "-0.18", "primary_driver": "Slow support response"},
            {"account_id": "ACCT9903", "customer": "Cedarworks Manufacturing", "churn_risk": "Low", "sentiment_score": "0.34", "primary_driver": "Stable engagement"},
        ],
    },
    "early_warning_signals": {
        "display_name": "Early Warning Signals",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": False,
        "exact_key_required": True,
        "key_field": "signal_id",
        "response": "These are the early-warning signals and real-time alerts for your higher-risk customers, with the most critical conditions flagged first.",
        "knowledge": [
            "Detect early warning triggers in real time to enable timely, proactive intervention (one-pager, Slide 1).",
            "The agent highlights predictive signals affecting higher-risk customers and zeros in on the critical conditions (demo 00:01:12-00:01:21).",
            "The agent highlights real-time alerts and flags customers for urgent follow up so the manager can act before issues escalate (demo 00:01:21-00:01:28).",
        ],
        "records": [
            {"signal_id": "SIGNAL3310", "customer": "Northwind Freight", "indicator": "Login frequency dropped 40 percent", "severity": "Critical", "alert_status": "Real-time alert sent"},
            {"signal_id": "SIGNAL5582", "customer": "Larkspur Retail", "indicator": "Two escalated complaints in seven days", "severity": "Elevated", "alert_status": "Added to watchlist"},
            {"signal_id": "SIGNAL7048", "customer": "Beacon Logistics", "indicator": "Contract renewal overdue", "severity": "Critical", "alert_status": "Real-time alert sent"},
        ],
    },
    "customer_snapshot": {
        "display_name": "Customer 360 Snapshot",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": False,
        "exact_key_required": True,
        "key_field": "snapshot_id",
        "response": "Here is the consolidated customer snapshot bringing CRM and core banking context together into one decision-ready view.",
        "knowledge": [
            "The agent consolidates CRM and core banking data into a single customer snapshot, surfacing only the most relevant context (demo 00:01:31-00:01:39).",
            "Instead of playing detective across multiple systems, the manager gets a rapid decision-ready view with risks clearly defined (demo 00:01:40-00:01:48).",
            "Predict churn risk to pinpoint critical and high-risk customers (one-pager, Slide 1).",
        ],
        "records": [
            {"snapshot_id": "SNAP2205", "customer": "Northwind Freight", "relationship": "Commercial Lending", "balances": "4.2M deposits", "open_items": "3 open service tickets"},
            {"snapshot_id": "SNAP6613", "customer": "Larkspur Retail", "relationship": "Business Banking", "balances": "0.9M deposits", "open_items": "1 open service ticket"},
            {"snapshot_id": "SNAP8890", "customer": "Beacon Logistics", "relationship": "Treasury Services", "balances": "7.8M deposits", "open_items": "5 open service tickets"},
        ],
    },
    "retention_strategy": {
        "display_name": "Retention Strategy Generation",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": True,
        "exact_key_required": True,
        "key_field": "strategy_id",
        "response": "Here are tailored retention strategies for each customer, covering outreach approach, messaging, offers, and timing.",
        "knowledge": [
            "Generate targeted retention strategies and recommended outreach plans (one-pager, Slide 1).",
            "Generate tailored retention and outreach plans to speed up preparation workflows (one-pager, Slide 1).",
            "The agent generates tailored recommendations for each customer, including outreach approach, messaging, offers, and timing (demo 00:01:48-00:01:58).",
        ],
        "records": [
            {"strategy_id": "PLAN1120", "customer": "Northwind Freight", "outreach": "Executive outreach call", "offer": "Fee waiver plus dedicated relationship manager", "timing": "Within 48 hours"},
            {"strategy_id": "PLAN3345", "customer": "Larkspur Retail", "outreach": "Personalized email", "offer": "Loyalty rate offer", "timing": "This week"},
            {"strategy_id": "PLAN5567", "customer": "Beacon Logistics", "outreach": "In-person account review", "offer": "Treasury optimization package", "timing": "Next 5 business days"},
        ],
    },
    "retention_coordination": {
        "display_name": "Retention Coordination and Tracking",
        "source_system": "Dynamics 365 CRM",
        "write": True,
        "generative": False,
        "exact_key_required": True,
        "key_field": "task_id",
        "response": "I have coordinated and updated tracking for your priority retention tasks, flagging delays and escalating blockers in Microsoft Teams.",
        "knowledge": [
            "To wrap up the workflow, the agent automates coordination and tracking for the priority customers (demo 00:02:04-00:02:10).",
            "It surfaces updates, flags delays, and escalates blockers, keeping retention efforts on track (demo 00:02:10-00:02:16).",
            "The unified view of churn risk is delivered by connecting to Dynamics 365 and driving communication through Microsoft Teams (demo 00:00:28-00:00:33).",
        ],
        "records": [
            {"task_id": "TASK4401", "customer": "Northwind Freight", "action": "RM follow-up call", "status": "In progress", "tracking": "On track"},
            {"task_id": "TASK6622", "customer": "Larkspur Retail", "action": "Send loyalty offer", "status": "Delayed", "tracking": "Escalated to team lead"},
            {"task_id": "TASK8833", "customer": "Beacon Logistics", "action": "Schedule treasury review", "status": "Not started", "tracking": "Blocker flagged"},
        ],
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _churn_score(customer):
    """Calculate churn risk score (0-100)."""
    score = 0
    if customer["nps_score"] < CHURN_INDICATORS["low_nps"]["threshold"]:
        score += CHURN_INDICATORS["low_nps"]["weight"]
    if customer["monthly_transactions"] < CHURN_INDICATORS["declining_transactions"]["threshold"]:
        score += CHURN_INDICATORS["declining_transactions"]["weight"]
    if customer["complaint_count_12m"] >= CHURN_INDICATORS["high_complaints"]["threshold"]:
        score += CHURN_INDICATORS["high_complaints"]["weight"]
    if customer["digital_engagement_score"] < CHURN_INDICATORS["low_engagement"]["threshold"]:
        score += CHURN_INDICATORS["low_engagement"]["weight"]
    if len(customer["products"]) <= CHURN_INDICATORS["single_product"]["threshold"]:
        score += CHURN_INDICATORS["single_product"]["weight"]
    return min(100, score)


def _sentiment_breakdown():
    """Compute overall sentiment distribution."""
    sentiments = {"positive": 0, "neutral": 0, "negative": 0}
    total = 0
    for cust in CUSTOMER_INTERACTIONS.values():
        for interaction in cust["recent_interactions"]:
            sentiments[interaction["sentiment"]] += 1
            total += 1
    return sentiments, total


def _humanize(text):
    """Turn a snake_case field name into a Title Case label."""
    return text.replace("_", " ").title()


def _normalized_lookup_tokens(value):
    """Normalize whitespace-delimited tokens without permitting embedded IDs."""
    normalized = []
    for token in str(value or "").casefold().split():
        cleaned = "".join(char for char in token if char.isalnum())
        if cleaned:
            normalized.append(cleaned)
    return normalized


def _contains_normalized_key(user_input, key):
    """Return True only when the complete normalized key is a token sequence."""
    query = _normalized_lookup_tokens(user_input)
    expected = _normalized_lookup_tokens(key)
    width = len(expected)
    return bool(width) and any(
        query[index:index + width] == expected
        for index in range(len(query) - width + 1)
    )


def _find_record(entry, user_input):
    """Return the uniquely matched record for a complete normalized key."""
    if not user_input:
        return None
    matches = [
        record for record in entry["records"]
        if _contains_normalized_key(user_input, record[entry["key_field"]])
    ]
    return matches[0] if len(matches) == 1 else None


def _write_receipt(op_key, entry, record):
    """Simulated write receipt — no live system is mutated."""
    ref = record[entry["key_field"]]
    digest = hashlib.sha256(f"{op_key}|{ref}".encode("utf-8")).hexdigest()[:8].upper()
    lines = [
        "## Simulated Write Receipt",
        "",
        "> No live systems were modified. This is a simulated coordination receipt.",
        "",
        f"- **Receipt ID:** SIM-{digest}",
        f"- **{_humanize(entry['key_field'])}:** {ref}",
        f"- **Recorded status:** {record.get('status', 'n/a')}",
        f"- **Channel:** Microsoft Teams (simulated)",
        f"- **Mode:** dry-run (no live mutation)",
    ]
    return "\n".join(lines)


def _capability_report(op_key, **kwargs):
    """Deterministic handler for an extended capability.

    With a `user_input` that contains an exact key value, returns the detail
    for that single record (plus a simulated receipt for write capabilities).
    Without a matching key, returns a useful no-input summary of all records.
    """
    entry = CAPABILITY_LIBRARY[op_key]
    user_input = kwargs.get("user_input") or ""
    record = _find_record(entry, user_input)
    key_field = entry["key_field"]

    if record is not None:
        lines = [f"# {entry['display_name']}\n", f"_{entry['response']}_\n"]
        lines.append(f"## Record {record[key_field]}\n")
        for field, value in record.items():
            lines.append(f"- **{_humanize(field)}:** {value}")
        if entry["write"]:
            lines.append("")
            lines.append(_write_receipt(op_key, entry, record))
        return "\n".join(lines)

    if str(user_input).strip():
        return (
            f"# {entry['display_name']}\n\n"
            f"No exact normalized `{key_field}` matched the request."
        )

    lines = [f"# {entry['display_name']}\n", f"_{entry['response']}_\n"]
    lines.append(f"**Source system:** {entry['source_system']}  ")
    lines.append(f"**Write:** {'yes' if entry['write'] else 'no'}  ")
    lines.append(f"**Generative:** {'yes' if entry['generative'] else 'no'}  ")
    lines.append(
        f"**Exact key required:** {'yes' if entry['exact_key_required'] else 'no'} "
        f"(key: `{key_field}`)\n"
    )
    headers = list(entry["records"][0].keys())
    lines.append("| " + " | ".join(_humanize(h) for h in headers) + " |")
    lines.append("|" + "|".join("---" for _ in headers) + "|")
    for rec in entry["records"]:
        lines.append("| " + " | ".join(str(rec[h]) for h in headers) + " |")
    lines.append("\n## Knowledge\n")
    for item in entry["knowledge"]:
        lines.append(f"- {item}")
    lines.append(
        f"\n_Provide `user_input` containing a `{key_field}` value "
        f"(e.g. `{entry['records'][0][key_field]}`) for an exact record lookup._"
    )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class CustomerSentimentChurnAgent(BasicAgent):
    """Customer sentiment and churn prediction agent."""

    def __init__(self):
        self.name = "CustomerSentimentChurnAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Customer Sentiment & Churn Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "sentiment_dashboard",
                            "churn_prediction",
                            "retention_actions",
                            "segment_analysis",
                            "churn_risk_scoring",
                            "early_warning_signals",
                            "customer_snapshot",
                            "retention_strategy",
                            "retention_coordination",
                        ],
                    },
                    "customer_id": {"type": "string"},
                    "user_input": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "sentiment_dashboard")
        dispatch = {
            "sentiment_dashboard": self._sentiment_dashboard,
            "churn_prediction": self._churn_prediction,
            "retention_actions": self._retention_actions,
            "segment_analysis": self._segment_analysis,
            "churn_risk_scoring": self._churn_risk_scoring,
            "early_warning_signals": self._early_warning_signals,
            "customer_snapshot": self._customer_snapshot,
            "retention_strategy": self._retention_strategy,
            "retention_coordination": self._retention_coordination,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        return handler(**kwargs)

    def _sentiment_dashboard(self, **kwargs) -> str:
        sentiments, total = _sentiment_breakdown()
        avg_nps = sum(c["nps_score"] for c in CUSTOMER_INTERACTIONS.values()) / len(CUSTOMER_INTERACTIONS)
        lines = ["# Customer Sentiment Dashboard\n"]
        lines.append(f"**Average NPS:** {avg_nps:.1f}")
        lines.append(f"**Total Interactions Analyzed:** {total}\n")
        lines.append("## Sentiment Distribution\n")
        for sent, count in sentiments.items():
            pct = round((count / total) * 100, 1) if total else 0
            lines.append(f"- **{sent.title()}:** {count} ({pct}%)")
        lines.append("\n## Customer NPS Scores\n")
        lines.append("| Customer | Segment | NPS | Products | Complaints (12m) |")
        lines.append("|---|---|---|---|---|")
        for cid, c in CUSTOMER_INTERACTIONS.items():
            lines.append(
                f"| {c['name']} ({cid}) | {c['segment'].replace('_', ' ').title()} "
                f"| {c['nps_score']} | {len(c['products'])} | {c['complaint_count_12m']} |"
            )
        return "\n".join(lines)

    def _churn_prediction(self, **kwargs) -> str:
        live = _live_customers()
        if live:
            lines = ["# Churn Prediction Report (live tenant)\n"]
            lines.append("| Customer | Segment | Churn Score | NPS | Open Cases | Top Signal |")
            lines.append("|---|---|---|---|---|---|")
            ranked = sorted(live.items(), key=lambda kv: -_live_churn_score(kv[1]))
            at_risk = []
            for cid, c in ranked:
                score = _live_churn_score(c)
                risk = "High" if score >= 50 else "Medium" if score >= 25 else "Low"
                lines.append(
                    f"| {c['name']} ({cid}) | {c['segment']} | {score} ({risk}) "
                    f"| {_seam(c['nps_score'])} | {c['open_cases']} | {c['top_signal']} |"
                )
                if score >= 50:
                    at_risk.append((cid, c, score))
            if at_risk:
                lines.append("\n## High-Risk Customers\n")
                for cid, c, score in at_risk:
                    lines.append(f"### {c['name']} ({cid}) — Score: {score}\n")
                    lines.append(f"- Segment: {c['segment']}")
                    lines.append(f"- Open cases: {c['open_cases']} ({c['high_priority_open']} high priority)")
                    lines.append(f"- Top signal: {c['top_signal']}\n")
            lines.append(
                "\n_Source: live Static Dynamics 365 tenant — support cases "
                "reinterpreted as complaint/sentiment signals. NPS, transactions, "
                "and digital engagement are enrichment seams (wire your survey "
                "and core banking systems)._"
            )
            return "\n".join(lines)

        lines = ["# Churn Prediction Report\n"]
        lines.append("| Customer | Segment | Churn Score | NPS | Transactions | Complaints |")
        lines.append("|---|---|---|---|---|---|")
        at_risk = []
        for cid, c in CUSTOMER_INTERACTIONS.items():
            score = _churn_score(c)
            risk = "High" if score >= 50 else "Medium" if score >= 25 else "Low"
            lines.append(
                f"| {c['name']} ({cid}) | {c['segment'].replace('_', ' ').title()} "
                f"| {score} ({risk}) | {c['nps_score']} | {c['monthly_transactions']} | {c['complaint_count_12m']} |"
            )
            if score >= 50:
                at_risk.append((cid, c, score))
        if at_risk:
            lines.append("\n## High-Risk Customers\n")
            for cid, c, score in at_risk:
                lines.append(f"### {c['name']} ({cid}) — Score: {score}\n")
                lines.append(f"- Segment: {c['segment'].replace('_', ' ').title()}")
                lines.append(f"- Tenure: {c['tenure_years']} years")
                lines.append(f"- Products: {', '.join(c['products'])}")
                lines.append(f"- Recent sentiment: {c['recent_interactions'][-1]['sentiment'] if c['recent_interactions'] else 'N/A'}\n")
        lines.append("\n## Churn Indicators Reference\n")
        for ind_id, ind in CHURN_INDICATORS.items():
            lines.append(f"- **{ind_id.replace('_', ' ').title()}** (weight: {ind['weight']}): {ind['description']}")
        lines.append("\n_Source: embedded demo layer (offline fallback)._")
        return "\n".join(lines)

    def _retention_actions(self, **kwargs) -> str:
        lines = ["# Retention Action Recommendations\n"]
        lines.append("## Available Actions\n")
        lines.append("| Action | Description | Cost | Success Rate |")
        lines.append("|---|---|---|---|")
        for action_id, action in RETENTION_ACTIONS.items():
            lines.append(
                f"| {action_id.replace('_', ' ').title()} | {action['description']} "
                f"| ${action['cost']} | {action['success_rate']}% |"
            )
        lines.append("\n## Recommended Actions by Customer\n")
        for cid, c in CUSTOMER_INTERACTIONS.items():
            score = _churn_score(c)
            if score < 25:
                continue
            lines.append(f"### {c['name']} ({cid}) — Churn Score: {score}\n")
            if c["complaint_count_12m"] >= 3:
                lines.append(f"1. **Complaint Resolution** — {RETENTION_ACTIONS['complaint_resolution']['description']}")
            if c["nps_score"] < 5:
                lines.append(f"2. **Personal Outreach** — {RETENTION_ACTIONS['personal_outreach']['description']}")
            if len(c["products"]) <= 2:
                lines.append(f"3. **Product Bundle** — {RETENTION_ACTIONS['product_bundle']['description']}")
            else:
                lines.append(f"3. **Loyalty Bonus** — {RETENTION_ACTIONS['loyalty_bonus']['description']}")
            lines.append("")
        return "\n".join(lines)

    def _segment_analysis(self, **kwargs) -> str:
        lines = ["# Segment Analysis\n"]
        lines.append("## Segment Benchmarks\n")
        lines.append("| Segment | Avg NPS | Avg Products | Avg Tenure | Avg Transactions |")
        lines.append("|---|---|---|---|---|")
        for seg, bench in SEGMENT_BENCHMARKS.items():
            lines.append(
                f"| {seg.replace('_', ' ').title()} | {bench['avg_nps']} "
                f"| {bench['avg_products']} | {bench['avg_tenure']} yrs | {bench['avg_transactions']}/mo |"
            )
        segments = {}
        for cid, c in CUSTOMER_INTERACTIONS.items():
            seg = c["segment"]
            if seg not in segments:
                segments[seg] = []
            segments[seg].append(c)
        lines.append("\n## Current Customer Performance vs Benchmark\n")
        for seg, customers in segments.items():
            bench = SEGMENT_BENCHMARKS.get(seg, {})
            avg_nps = sum(c["nps_score"] for c in customers) / len(customers)
            avg_products = sum(len(c["products"]) for c in customers) / len(customers)
            lines.append(f"### {seg.replace('_', ' ').title()} ({len(customers)} customers)\n")
            lines.append(f"- NPS: {avg_nps:.1f} (benchmark: {bench.get('avg_nps', 'N/A')})")
            lines.append(f"- Products: {avg_products:.1f} (benchmark: {bench.get('avg_products', 'N/A')})")
            lines.append("")
        return "\n".join(lines)

    # -- Extended capabilities (v1.1.0) --------------------------------------

    def _churn_risk_scoring(self, **kwargs) -> str:
        return _capability_report("churn_risk_scoring", **kwargs)

    def _early_warning_signals(self, **kwargs) -> str:
        return _capability_report("early_warning_signals", **kwargs)

    def _customer_snapshot(self, **kwargs) -> str:
        return _capability_report("customer_snapshot", **kwargs)

    def _retention_strategy(self, **kwargs) -> str:
        return _capability_report("retention_strategy", **kwargs)

    def _retention_coordination(self, **kwargs) -> str:
        return _capability_report("retention_coordination", **kwargs)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = CustomerSentimentChurnAgent()
    print("=" * 80)
    print("EMBEDDED DEMO DASHBOARD (works offline)")
    print(agent.perform(operation="sentiment_dashboard"))
    print("\n" + "=" * 80 + "\n")
    print("LIVE TENANT CHURN PREDICTION (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="churn_prediction"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="retention_actions"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="segment_analysis"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
