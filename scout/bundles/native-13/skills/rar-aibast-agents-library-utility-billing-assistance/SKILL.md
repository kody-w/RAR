---
name: "rar-aibast-agents-library-utility-billing-assistance"
description: "Answers billing inquiries and screens assistance from a live simulated Dynamics 365 tenant's utility cases, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/utility_billing_assistance", "rar_sha256": "fa45e49b921930efabef806a48d00870f16a15511df35aff72523f98715261ee", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["utility", "billing", "water", "payment", "assistance", "municipal", "leak-detection", "smart-meter"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/utility_billing_assistance`. The original RAPP
agent is preserved byte-for-byte in `utility_billing_assistance_agent.py` and in the RCI capsule.

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

Utility Billing Assistance Agent — a template you are meant to mutate.

Provides utility billing support including account inquiries, usage
analysis, payment plan management, and assistance program eligibility
for municipal utility departments.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live utility service cases over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="billing_inquiry")
     — with network up, the desk view surfaces the tenant's live
     billing/metering cases such as CAS-260129 "Meter reading anomalies
     across district seven" (Prairie Wind Energy Cooperative). In this
     template a billing/metering inquiry is represented as a Dynamics
     case (incident).
  2. No network? Everything falls back to the embedded demo layer below
     (UTILITY_ACCOUNTS / ASSISTANCE_PROGRAMS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     UTILITY_BILLING_ASSISTANCE_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your CIS), or
     replace _fetch_collection() with your own billing API. The fields
     the rest of the file needs are listed in
     _normalize_live_billing_case() — balances and usage stay
     "n/a — enrichment seam" until you wire your CIS/meter data.

OPERATIONS
  billing_inquiry | usage_analysis | payment_plan | assistance_programs
  | smart_meter_analysis and other evidence operations (see enum)
  kwargs: operation (required), account_id, key, user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "account_id": {
      "type": "string"
    },
    "key": {
      "description": "Exact record key advertised by the selected evidence operation.",
      "type": "string"
    },
    "operation": {
      "enum": [
        "billing_inquiry",
        "usage_analysis",
        "payment_plan",
        "assistance_programs",
        "smart_meter_analysis",
        "leak_adjustment",
        "assistance_eligibility",
        "assistance_enrollment",
        "repair_scheduling",
        "resolution_summary"
      ],
      "type": "string"
    },
    "user_input": {
      "description": "Natural-language request containing an exact advertised record key.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `utility_billing_assistance_agent.py` and embedded as the fenced Python below (sha256 fa45e49b921930ef…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `utility_billing_assistance_agent.py` first:

```bash
python3 utility_billing_assistance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 utility_billing_assistance_agent.py   # or on stdin
python3 utility_billing_assistance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Utility Billing Assistance Agent — a template you are meant to mutate.

Provides utility billing support including account inquiries, usage
analysis, payment plan management, and assistance program eligibility
for municipal utility departments.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live utility service cases over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="billing_inquiry")
     — with network up, the desk view surfaces the tenant's live
     billing/metering cases such as CAS-260129 "Meter reading anomalies
     across district seven" (Prairie Wind Energy Cooperative). In this
     template a billing/metering inquiry is represented as a Dynamics
     case (incident).
  2. No network? Everything falls back to the embedded demo layer below
     (UTILITY_ACCOUNTS / ASSISTANCE_PROGRAMS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     UTILITY_BILLING_ASSISTANCE_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your CIS), or
     replace _fetch_collection() with your own billing API. The fields
     the rest of the file needs are listed in
     _normalize_live_billing_case() — balances and usage stay
     "n/a — enrichment seam" until you wire your CIS/meter data.

OPERATIONS
  billing_inquiry | usage_analysis | payment_plan | assistance_programs
  | smart_meter_analysis and other evidence operations (see enum)
  kwargs: operation (required), account_id, key, user_input
"""

import sys
import os
import re

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timezone

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/utility_billing_assistance",
    "version": "1.2.0",
    "display_name": "Utility Billing Assistance Agent",
    "description": "Answers billing inquiries and screens assistance from a live simulated Dynamics 365 tenant's utility cases, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["utility", "billing", "water", "payment", "assistance", "municipal", "leak-detection", "smart-meter"],
    "category": "slg_government",
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
#   export UTILITY_BILLING_ASSISTANCE_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CIS client. Downstream code
# only needs the fields from _normalize_live_billing_case().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "UTILITY_BILLING_ASSISTANCE_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
_LIVE_CACHE = {}

# Case-title keywords that mark a tenant case as a utility-desk item.
_UTILITY_KEYWORDS = ("meter", "substation", "billing", "invoice", "utility", "outage")


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


def _normalize_live_billing_case(row):
    """Project a Dynamics case (incident) record onto the shape this agent
    uses — in this template a billing/metering inquiry IS a Dynamics
    case. THIS is the contract your replacement data source must meet —
    a dict with these keys. None means 'not available from the case
    system alone' and the renderers label it as an enrichment seam."""
    return {
        "case_id": row.get("ticketnumber", row.get("incidentid", "")),
        "customer": row.get("customeridname", "Unknown"),
        "subject": row.get("title", "untitled"),
        "priority": row.get(
            "prioritycode@OData.Community.Display.V1.FormattedValue", "Normal"
        ),
        "status": row.get(
            "statecode@OData.Community.Display.V1.FormattedValue", "Active"
        ),
        "channel": row.get(
            "caseorigincode@OData.Community.Display.V1.FormattedValue", "Unknown"
        ),
        "owner": row.get("owneridname", "Unassigned"),
        "age_days": _age_days(row.get("createdon")),
        "open": row.get("statecode") == 0,
        "balance_due": None,   # enrichment seam — wire your CIS
        "usage_kwh": None,     # enrichment seam — wire your meter data
        "_live": True,
    }


def _age_days(iso_date):
    try:
        then = datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
        return max(0, (datetime.now(timezone.utc) - then).days)
    except (ValueError, TypeError):
        return 0


def _live_billing_queue():
    """Live tenant cases whose titles look utility-desk-shaped."""
    queue = []
    for row in _fetch_collection("incidents"):
        title = str(row.get("title", "")).lower()
        if any(kw in title for kw in _UTILITY_KEYWORDS):
            case = _normalize_live_billing_case(row)
            if case["case_id"]:
                queue.append(case)
    return queue


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback) — Synthetic domain data
# ---------------------------------------------------------------------------

UTILITY_ACCOUNTS = {
    "ACCT-90001": {
        "customer": "Patricia Hernandez",
        "address": "1245 Cedar Lane",
        "account_type": "residential",
        "services": ["water", "sewer", "stormwater"],
        "status": "active",
        "balance_current": 127.45,
        "balance_past_due": 0.00,
        "autopay": True,
        "last_payment": {"date": "2025-02-15", "amount": 118.90},
    },
    "ACCT-90002": {
        "customer": "Green Valley Shopping Center",
        "address": "5600 Commerce Blvd",
        "account_type": "commercial",
        "services": ["water", "sewer", "stormwater", "fire_line"],
        "status": "active",
        "balance_current": 2845.60,
        "balance_past_due": 1420.30,
        "autopay": False,
        "last_payment": {"date": "2025-01-20", "amount": 2650.00},
    },
    "ACCT-90003": {
        "customer": "Robert & Linda Thompson",
        "address": "887 Willow Creek Dr",
        "account_type": "residential",
        "services": ["water", "sewer", "stormwater", "trash"],
        "status": "delinquent",
        "balance_current": 245.80,
        "balance_past_due": 489.20,
        "autopay": False,
        "last_payment": {"date": "2024-11-18", "amount": 135.00},
    },
    "ACCT-90004": {
        "customer": "Sunnyvale Elementary School",
        "address": "300 Education Way",
        "account_type": "institutional",
        "services": ["water", "sewer", "stormwater", "irrigation"],
        "status": "active",
        "balance_current": 1890.25,
        "balance_past_due": 0.00,
        "autopay": True,
        "last_payment": {"date": "2025-02-28", "amount": 1756.00},
    },
}

USAGE_HISTORY = {
    "ACCT-90001": [
        {"period": "2024-09", "water_gallons": 4200, "sewer_gallons": 3780, "amount": 98.50},
        {"period": "2024-10", "water_gallons": 3800, "sewer_gallons": 3420, "amount": 92.10},
        {"period": "2024-11", "water_gallons": 3100, "sewer_gallons": 2790, "amount": 84.30},
        {"period": "2024-12", "water_gallons": 2900, "sewer_gallons": 2610, "amount": 81.20},
        {"period": "2025-01", "water_gallons": 3000, "sewer_gallons": 2700, "amount": 82.90},
        {"period": "2025-02", "water_gallons": 3200, "sewer_gallons": 2880, "amount": 86.45},
    ],
    "ACCT-90003": [
        {"period": "2024-09", "water_gallons": 8500, "sewer_gallons": 7650, "amount": 145.20},
        {"period": "2024-10", "water_gallons": 9200, "sewer_gallons": 8280, "amount": 152.80},
        {"period": "2024-11", "water_gallons": 12400, "sewer_gallons": 11160, "amount": 198.50},
        {"period": "2024-12", "water_gallons": 14800, "sewer_gallons": 13320, "amount": 232.10},
        {"period": "2025-01", "water_gallons": 13200, "sewer_gallons": 11880, "amount": 215.40},
        {"period": "2025-02", "water_gallons": 11500, "sewer_gallons": 10350, "amount": 189.80},
    ],
}

RATE_STRUCTURES = {
    "water_residential": {
        "base_charge": 18.50,
        "tiers": [
            {"range": "0-3,000 gal", "rate_per_1000": 4.25},
            {"range": "3,001-6,000 gal", "rate_per_1000": 6.50},
            {"range": "6,001-10,000 gal", "rate_per_1000": 9.75},
            {"range": "Over 10,000 gal", "rate_per_1000": 14.00},
        ],
    },
    "water_commercial": {
        "base_charge": 45.00,
        "tiers": [
            {"range": "0-10,000 gal", "rate_per_1000": 5.80},
            {"range": "10,001-50,000 gal", "rate_per_1000": 5.25},
            {"range": "Over 50,000 gal", "rate_per_1000": 4.90},
        ],
    },
    "sewer": {"base_charge": 12.75, "rate_per_1000": 5.10},
    "stormwater": {"residential": 8.50, "commercial_per_eru": 8.50},
    "trash": {"residential": 22.00},
}

ASSISTANCE_PROGRAMS = {
    "LIHWAP": {
        "name": "Low-Income Household Water Assistance Program",
        "income_limit_pct_fpl": 150,
        "max_benefit": 1500,
        "eligibility": "Household income at or below 150% FPL",
        "documents_required": ["Proof of income", "Utility bill", "ID", "Household size verification"],
        "status": "accepting_applications",
    },
    "senior_discount": {
        "name": "Senior Citizen Rate Discount",
        "income_limit_pct_fpl": 200,
        "max_benefit": 0,
        "eligibility": "Age 65+ and income at or below 200% FPL",
        "documents_required": ["Proof of age", "Proof of income", "Utility account number"],
        "status": "accepting_applications",
        "discount_pct": 25,
    },
    "arrearage_forgiveness": {
        "name": "COVID-19 Arrearage Forgiveness Program",
        "income_limit_pct_fpl": 200,
        "max_benefit": 3000,
        "eligibility": "Past-due balance accrued during March 2020 - December 2023",
        "documents_required": ["Utility account statement", "Income verification"],
        "status": "limited_funds",
    },
    "payment_plan": {
        "name": "Extended Payment Arrangement",
        "income_limit_pct_fpl": 0,
        "max_benefit": 0,
        "eligibility": "Any customer with past-due balance over $100",
        "documents_required": ["Signed payment agreement"],
        "status": "always_available",
        "max_installments": 12,
    },
}

EVIDENCE_CAPABILITIES = {
    "smart_meter_analysis": {
        "display_name": "Smart Meter Anomaly and Leak Analysis",
        "source_system": "Dynamics 365 CRM and utility meter data",
        "key_field": "analysis_id",
        "write": False,
        "knowledge": [
            "Compares current consumption with the account's historical baseline.",
            "Uses hourly smart-meter readings to locate concentrated usage anomalies.",
            "Identifies leak-consistent patterns and explains the likely cause.",
        ],
        "records": [
            {
                "analysis_id": "METER-RES-782MD",
                "account_id": "RES-782MD",
                "current_usage": "22,000 gallons",
                "baseline_usage": "4,500 gallons",
                "increase": "389%",
                "anomaly_window": "March 10-13; 182 gallons/hour",
                "diagnosis": "Internal leak, likely toilet flapper",
            },
            {
                "analysis_id": "METER-ACCT-90001",
                "account_id": "ACCT-90001",
                "current_usage": "3,200 gallons",
                "baseline_usage": "3,400 gallons",
                "increase": "-6%",
                "anomaly_window": "None",
                "diagnosis": "Stable usage",
            },
            {
                "analysis_id": "METER-ACCT-90003",
                "account_id": "ACCT-90003",
                "current_usage": "11,500 gallons",
                "baseline_usage": "8,500 gallons",
                "increase": "35%",
                "anomaly_window": "Overnight continuous flow",
                "diagnosis": "Possible fixture leak",
            },
        ],
    },
    "leak_adjustment": {
        "display_name": "Municipal Leak Adjustment",
        "source_system": "Municipal billing system",
        "key_field": "adjustment_id",
        "write": True,
        "knowledge": [
            "Applies municipal policy consistently to excess consumption.",
            "Calculates water-only charges, sewer waivers, credits, and the revised bill.",
            "Creates a full audit trail and states repair-proof requirements.",
        ],
        "records": [
            {
                "adjustment_id": "ADJ-RES-782MD",
                "account_id": "RES-782MD",
                "policy": "Municipal Code 18.42 one-time leak adjustment",
                "excess_volume": "17,500 gallons",
                "credit": "$97.80",
                "new_bill": "$86.70",
                "condition": "Proof of repair within 30 days",
            },
            {
                "adjustment_id": "ADJ-ACCT-90003",
                "account_id": "ACCT-90003",
                "policy": "Residential verified-leak adjustment",
                "excess_volume": "3,000 gallons",
                "credit": "$28.35",
                "new_bill": "$217.45",
                "condition": "Licensed repair invoice within 30 days",
            },
            {
                "adjustment_id": "ADJ-ACCT-90002",
                "account_id": "ACCT-90002",
                "policy": "Commercial anomaly review",
                "excess_volume": "Pending verification",
                "credit": "$0.00",
                "new_bill": "$4,265.90",
                "condition": "Meter inspection required",
            },
        ],
    },
    "assistance_eligibility": {
        "display_name": "Assistance Eligibility Screening",
        "source_system": "Dynamics 365 CRM and assistance program rules",
        "key_field": "screening_id",
        "write": False,
        "knowledge": [
            "Screens household income against municipal and emergency assistance rules.",
            "Surfaces available credits, grants, discounts, and payment-plan options.",
            "Explains qualification and total potential financial relief.",
        ],
        "records": [
            {
                "screening_id": "SCREEN-RES-782MD",
                "account_id": "RES-782MD",
                "income": "$32,400 (68% AMI)",
                "eligible_programs": "LIWAP; LIHEAP emergency fund; 6-month payment plan",
                "potential_relief": "$350",
                "decision": "Qualifies",
            },
            {
                "screening_id": "SCREEN-ACCT-90003",
                "account_id": "ACCT-90003",
                "income": "142% FPL",
                "eligible_programs": "LIHWAP; extended payment arrangement",
                "potential_relief": "Up to $1,500",
                "decision": "Qualifies",
            },
            {
                "screening_id": "SCREEN-ACCT-90001",
                "account_id": "ACCT-90001",
                "income": "Not supplied",
                "eligible_programs": "Extended payment arrangement",
                "potential_relief": "Payment flexibility",
                "decision": "Income documentation required for other programs",
            },
        ],
    },
    "assistance_enrollment": {
        "display_name": "Payment Plan and Assistance Enrollment",
        "source_system": "Municipal billing system and customer portal",
        "key_field": "enrollment_id",
        "write": True,
        "knowledge": [
            "Configures a payment plan and initiates program enrollment in one workflow.",
            "Pre-fills application forms and lists the required income and residency documents.",
            "Sends forms with a portal link and a deterministic response deadline.",
        ],
        "records": [
            {
                "enrollment_id": "ENROLL-RES-782MD",
                "account_id": "RES-782MD",
                "payment_plan": "6 months at $14.45; 0% interest",
                "program": "LIWAP",
                "documents": "Pay stubs or tax return; lease or property deed",
                "deadline": "14 days",
                "status": "Application pre-filled",
            },
            {
                "enrollment_id": "ENROLL-ACCT-90003",
                "account_id": "ACCT-90003",
                "payment_plan": "12 months at $40.77",
                "program": "LIHWAP",
                "documents": "Proof of income; utility bill; ID; household size",
                "deadline": "14 days",
                "status": "Application pre-filled",
            },
            {
                "enrollment_id": "ENROLL-ACCT-90002",
                "account_id": "ACCT-90002",
                "payment_plan": "6 months at $236.72",
                "program": "Extended Payment Arrangement",
                "documents": "Signed payment agreement",
                "deadline": "10 days",
                "status": "Agreement generated",
            },
        ],
    },
    "repair_scheduling": {
        "display_name": "Conservation Repair Scheduling",
        "source_system": "Municipal field service schedule",
        "key_field": "repair_id",
        "write": True,
        "knowledge": [
            "Matches eligible residents with city-certified repair providers.",
            "Schedules a repair window and lists included conservation equipment.",
            "States program value and expected water savings.",
        ],
        "records": [
            {
                "repair_id": "REPAIR-RES-782MD",
                "account_id": "RES-782MD",
                "appointment": "Tuesday, April 2, 1:00-3:00 PM",
                "provider": "City Maintenance licensed plumber",
                "services": "Toilet flapper; faucet aerators; leak detection tablets; low-flow showerhead",
                "program_value": "$85",
                "estimated_savings": "6,000 gallons/month",
            },
            {
                "repair_id": "REPAIR-ACCT-90003",
                "account_id": "ACCT-90003",
                "appointment": "Thursday, April 4, 9:00-11:00 AM",
                "provider": "City Conservation Crew",
                "services": "Fixture inspection; leak repair kit",
                "program_value": "$75",
                "estimated_savings": "3,000 gallons/month",
            },
            {
                "repair_id": "REPAIR-ACCT-90001",
                "account_id": "ACCT-90001",
                "appointment": "Friday, April 5, 1:00-3:00 PM",
                "provider": "City Conservation Crew",
                "services": "Efficiency audit; faucet aerators",
                "program_value": "$40",
                "estimated_savings": "500 gallons/month",
            },
        ],
    },
    "resolution_summary": {
        "display_name": "Customer Resolution and Account Update",
        "source_system": "Dynamics 365 CRM and Microsoft Outlook",
        "key_field": "resolution_id",
        "write": True,
        "knowledge": [
            "Packages credits, payment plans, enrollment, and repair actions into one resolution.",
            "Updates the synthetic account audit summary and schedules follow-up.",
            "Creates a transparent customer communication for Outlook and portal delivery.",
        ],
        "records": [
            {
                "resolution_id": "RESOLVE-RES-782MD",
                "account_id": "RES-782MD",
                "actions": "$97.80 credit; payment plan; LIWAP pending; LIHEAP info; repair scheduled",
                "delivery": "Outlook email and postal mail",
                "follow_up": "30 days",
                "total_relief": "$347.80 plus future leak savings",
            },
            {
                "resolution_id": "RESOLVE-ACCT-90003",
                "account_id": "ACCT-90003",
                "actions": "$28.35 credit; payment plan; LIHWAP pending; repair scheduled",
                "delivery": "Outlook email and customer portal",
                "follow_up": "30 days",
                "total_relief": "Up to $1,528.35",
            },
            {
                "resolution_id": "RESOLVE-ACCT-90002",
                "account_id": "ACCT-90002",
                "actions": "Payment agreement generated; meter inspection requested",
                "delivery": "Outlook email",
                "follow_up": "10 days",
                "total_relief": "Pending inspection",
            },
        ],
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _calculate_water_bill(gallons, account_type):
    """Calculate water charges based on tiered rate structure."""
    if account_type == "commercial":
        rate_info = RATE_STRUCTURES["water_commercial"]
    else:
        rate_info = RATE_STRUCTURES["water_residential"]
    total = rate_info["base_charge"]
    remaining = gallons
    for tier in rate_info["tiers"]:
        range_str = tier["range"]
        if range_str.startswith("Over"):
            total += (remaining / 1000) * tier["rate_per_1000"]
            remaining = 0
        else:
            parts = range_str.replace(",", "").replace(" gal", "").split("-")
            low = int(parts[0])
            high = int(parts[1])
            tier_volume = min(remaining, high - low + 1)
            if tier_volume > 0:
                total += (tier_volume / 1000) * tier["rate_per_1000"]
                remaining -= tier_volume
        if remaining <= 0:
            break
    return round(total, 2)


def _usage_trend(account_id):
    """Analyze usage trend for an account."""
    history = USAGE_HISTORY.get(account_id, [])
    if len(history) < 2:
        return "insufficient_data"
    recent = history[-1]["water_gallons"]
    previous_avg = sum(h["water_gallons"] for h in history[:-1]) / (len(history) - 1)
    if recent > previous_avg * 1.20:
        return "significantly_increasing"
    elif recent > previous_avg * 1.05:
        return "slightly_increasing"
    elif recent < previous_avg * 0.80:
        return "significantly_decreasing"
    elif recent < previous_avg * 0.95:
        return "slightly_decreasing"
    return "stable"


def _evidence_capability(operation_name, **kwargs):
    """Return an offline capability summary or an exact synthetic record."""
    capability = EVIDENCE_CAPABILITIES[operation_name]
    key_field = capability["key_field"]
    selector = str(kwargs.get(key_field) or kwargs.get("key") or "").strip()
    user_input = str(kwargs.get("user_input", "")).strip()
    input_tokens = {
        token.casefold()
        for token in re.findall(r"[A-Za-z0-9]+(?:[-_][A-Za-z0-9]+)*", user_input)
    }

    record = None
    for candidate in capability["records"]:
        candidate_key = str(candidate[key_field])
        normalized_key = candidate_key.casefold()
        if selector and normalized_key == selector.casefold():
            record = candidate
            break
        if not selector and user_input and normalized_key in input_tokens:
            record = candidate
            break

    if selector or user_input:
        if record is None:
            available = ", ".join(str(item[key_field]) for item in capability["records"])
            return f"**Error:** No {key_field.replace('_', ' ')} matched. Available keys: {available}."
        lines = [f"# {capability['display_name']}: {record[key_field]}\n"]
        for field, value in record.items():
            lines.append(f"- **{field.replace('_', ' ').title()}:** {value}")
        lines.append(f"- **Source System:** {capability['source_system']}")
        if capability["write"]:
            lines.extend([
                "\n## Simulated Write Receipt\n",
                f"- **Receipt:** SIM-{operation_name.upper()}-{record[key_field]}",
                f"- **Action:** {capability['display_name']}",
                "- **Result:** Simulated only; no external system was modified.",
            ])
        return "\n".join(lines)

    lines = [f"# {capability['display_name']}\n"]
    lines.append(f"**Mode:** {'Simulated write' if capability['write'] else 'Read-only'}")
    lines.append(f"**Source System:** {capability['source_system']}\n")
    lines.append("## Capability\n")
    lines.extend(f"- {item}" for item in capability["knowledge"])
    lines.append("\n## Available Records\n")
    for item in capability["records"]:
        lines.append(f"- `{item[key_field]}`")
    lines.append(f"\nProvide `{key_field}` or `key` for an exact offline lookup.")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class UtilityBillingAssistanceAgent(BasicAgent):
    """Municipal utility billing assistance agent."""

    def __init__(self):
        self.name = "UtilityBillingAssistanceAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Utility Billing Assistance Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "billing_inquiry",
                            "usage_analysis",
                            "payment_plan",
                            "assistance_programs",
                            "smart_meter_analysis",
                            "leak_adjustment",
                            "assistance_eligibility",
                            "assistance_enrollment",
                            "repair_scheduling",
                            "resolution_summary",
                        ],
                    },
                    "account_id": {"type": "string"},
                    "key": {
                        "type": "string",
                        "description": "Exact record key advertised by the selected evidence operation.",
                    },
                    "user_input": {
                        "type": "string",
                        "description": "Natural-language request containing an exact advertised record key.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "billing_inquiry")
        dispatch = {
            "billing_inquiry": self._billing_inquiry,
            "usage_analysis": self._usage_analysis,
            "payment_plan": self._payment_plan,
            "assistance_programs": self._assistance_programs,
        }
        if operation in EVIDENCE_CAPABILITIES:
            return _evidence_capability(operation, **kwargs)
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        return handler(**kwargs)

    def _live_billing_inquiry(self, queue):
        """Utility desk queue from live tenant cases (preferred online)."""
        open_cases = [c for c in queue if c["open"]]
        lines = [
            "# Utility Service Desk — Live Tenant Cases\n",
            f"Live records from {DATA_SOURCE_URL} (Aster Lane Office Systems).",
            "In this template a billing/metering inquiry is a Dynamics case.",
            "Pass `account_id` (e.g. ACCT-90001) for the embedded demo view.\n",
            "| Case | Customer | Subject | Priority | Status | Channel | Age | Balance Due |",
            "|---|---|---|---|---|---|---|---|",
        ]
        for c in sorted(queue, key=lambda x: x["case_id"]):
            balance = (
                "n/a — enrichment seam"
                if c["balance_due"] is None
                else f"${c['balance_due']:,.2f}"
            )
            lines.append(
                f"| {c['case_id']} | {c['customer']} | {c['subject']} "
                f"| {c['priority']} | {c['status']} | {c['channel']} "
                f"| {c['age_days']}d | {balance} |"
            )
        lines.append("")
        lines.append(
            f"**Open utility cases:** {len(open_cases)} of {len(queue)} matched"
        )
        lines.append(
            "Balances and meter usage need your CIS/AMI system — wire it at "
            "the LIVE DATA SEAM."
        )
        return "\n".join(lines)

    def _billing_inquiry(self, **kwargs) -> str:
        account_id = kwargs.get("account_id")
        if not account_id:
            queue = _live_billing_queue()
            if queue:
                return self._live_billing_inquiry(queue)
        if account_id and account_id in UTILITY_ACCOUNTS:
            acct = UTILITY_ACCOUNTS[account_id]
            total_due = acct["balance_current"] + acct["balance_past_due"]
            lines = [f"# Billing Inquiry: {account_id}\n"]
            lines.append(f"- **Customer:** {acct['customer']}")
            lines.append(f"- **Address:** {acct['address']}")
            lines.append(f"- **Account Type:** {acct['account_type'].title()}")
            lines.append(f"- **Services:** {', '.join(s.replace('_', ' ').title() for s in acct['services'])}")
            lines.append(f"- **Status:** {acct['status'].title()}")
            lines.append(f"- **Current Charges:** ${acct['balance_current']:,.2f}")
            lines.append(f"- **Past Due:** ${acct['balance_past_due']:,.2f}")
            lines.append(f"- **Total Due:** ${total_due:,.2f}")
            lines.append(f"- **Auto-Pay:** {'Yes' if acct['autopay'] else 'No'}")
            lines.append(f"- **Last Payment:** ${acct['last_payment']['amount']:,.2f} on {acct['last_payment']['date']}")
            return "\n".join(lines)

        lines = ["# Utility Accounts Summary\n"]
        lines.append("| Account | Customer | Type | Current | Past Due | Status |")
        lines.append("|---|---|---|---|---|---|")
        for aid, acct in UTILITY_ACCOUNTS.items():
            lines.append(
                f"| {aid} | {acct['customer']} | {acct['account_type'].title()} "
                f"| ${acct['balance_current']:,.2f} | ${acct['balance_past_due']:,.2f} | {acct['status'].title()} |"
            )
        total_ar = sum(a["balance_current"] + a["balance_past_due"] for a in UTILITY_ACCOUNTS.values())
        lines.append(f"\n**Total Accounts Receivable:** ${total_ar:,.2f}")
        return "\n".join(lines)

    def _usage_analysis(self, **kwargs) -> str:
        account_id = kwargs.get("account_id", "ACCT-90001")
        history = USAGE_HISTORY.get(account_id, [])
        acct = UTILITY_ACCOUNTS.get(account_id, {})
        trend = _usage_trend(account_id)
        lines = [f"# Usage Analysis: {account_id}\n"]
        lines.append(f"**Customer:** {acct.get('customer', 'Unknown')}")
        lines.append(f"**Usage Trend:** {trend.replace('_', ' ').title()}\n")
        if history:
            lines.append("| Period | Water (gal) | Sewer (gal) | Amount |")
            lines.append("|---|---|---|---|")
            for h in history:
                lines.append(f"| {h['period']} | {h['water_gallons']:,} | {h['sewer_gallons']:,} | ${h['amount']:,.2f} |")
            avg_water = sum(h["water_gallons"] for h in history) / len(history)
            avg_bill = sum(h["amount"] for h in history) / len(history)
            lines.append(f"\n**Avg Monthly Water Usage:** {avg_water:,.0f} gallons")
            lines.append(f"**Avg Monthly Bill:** ${avg_bill:,.2f}")
        lines.append("\n## Rate Structure\n")
        for rate_name, rate_info in RATE_STRUCTURES.items():
            lines.append(f"### {rate_name.replace('_', ' ').title()}\n")
            if isinstance(rate_info, dict) and "tiers" in rate_info:
                lines.append(f"Base Charge: ${rate_info['base_charge']:,.2f}\n")
                for tier in rate_info["tiers"]:
                    lines.append(f"- {tier['range']}: ${tier['rate_per_1000']:,.2f}/1,000 gal")
            elif isinstance(rate_info, dict) and "base_charge" in rate_info:
                lines.append(f"Base: ${rate_info['base_charge']:,.2f}, Rate: ${rate_info.get('rate_per_1000', 0):,.2f}/1,000 gal")
            lines.append("")
        return "\n".join(lines)

    def _payment_plan(self, **kwargs) -> str:
        account_id = kwargs.get("account_id", "ACCT-90003")
        acct = UTILITY_ACCOUNTS.get(account_id, list(UTILITY_ACCOUNTS.values())[2])
        past_due = acct["balance_past_due"]
        lines = [f"# Payment Plan Options: {account_id}\n"]
        lines.append(f"**Customer:** {acct['customer']}")
        lines.append(f"**Past Due Balance:** ${past_due:,.2f}\n")
        if past_due > 0:
            lines.append("## Installment Options\n")
            lines.append("| Installments | Monthly Payment | Total |")
            lines.append("|---|---|---|")
            for months in [3, 6, 9, 12]:
                monthly = round(past_due / months, 2)
                lines.append(f"| {months} months | ${monthly:,.2f} | ${past_due:,.2f} |")
            lines.append("\n*Note: Current charges continue to accrue during payment plan.*\n")
        lines.append("## Payment Plan Requirements\n")
        pp = ASSISTANCE_PROGRAMS["payment_plan"]
        lines.append(f"- {pp['eligibility']}")
        lines.append(f"- Maximum installments: {pp['max_installments']}")
        lines.append(f"- Documents required: {', '.join(pp['documents_required'])}")
        return "\n".join(lines)

    def _assistance_programs(self, **kwargs) -> str:
        lines = ["# Utility Assistance Programs\n"]
        for prog_id, prog in ASSISTANCE_PROGRAMS.items():
            lines.append(f"## {prog['name']}\n")
            lines.append(f"- **Eligibility:** {prog['eligibility']}")
            if prog["max_benefit"] > 0:
                lines.append(f"- **Maximum Benefit:** ${prog['max_benefit']:,.0f}")
            if prog.get("discount_pct"):
                lines.append(f"- **Discount:** {prog['discount_pct']}%")
            lines.append(f"- **Status:** {prog['status'].replace('_', ' ').title()}")
            lines.append(f"- **Documents Required:**")
            for doc in prog["documents_required"]:
                lines.append(f"  - {doc}")
            lines.append("")
        lines.append("## Federal Poverty Level Reference (2025)\n")
        fpl_table = {1: 15650, 2: 21150, 3: 26650, 4: 32150, 5: 37650}
        lines.append("| Household Size | 100% FPL | 150% FPL | 200% FPL |")
        lines.append("|---|---|---|---|")
        for size, fpl in fpl_table.items():
            lines.append(f"| {size} | ${fpl:,} | ${int(fpl * 1.5):,} | ${fpl * 2:,} |")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = UtilityBillingAssistanceAgent()
    print("LIVE TENANT UTILITY CASES (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="billing_inquiry"))
    print("\n" + "=" * 80 + "\n")
    print("EMBEDDED DEMO ACCOUNT (works offline)")
    print(agent.perform(operation="billing_inquiry", account_id="ACCT-90002"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="usage_analysis", account_id="ACCT-90003"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="payment_plan", account_id="ACCT-90003"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="assistance_programs"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
