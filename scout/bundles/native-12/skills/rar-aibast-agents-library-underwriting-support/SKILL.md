---
name: "rar-aibast-agents-library-underwriting-support"
description: "Evaluates underwriting queues from a live simulated Dynamics 365 tenant (quotes as submissions), with pricing demos and an offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/underwriting_support", "rar_sha256": "2687b8b34f22b99554c31a34d0cd9588fa27cf746c384603c8f14e07bef95d67", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["underwriting", "insurance", "risk", "pricing", "guidelines", "financial-services"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/underwriting_support`. The original RAPP
agent is preserved byte-for-byte in `underwriting_support_agent.py` and in the RCI capsule.

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

Underwriting Support Agent — a template you are meant to mutate.

Supports insurance underwriting with risk evaluation, pricing
recommendations, guideline checks, and exception reviews. In this template
an underwriting submission is represented as a Dynamics 365 quote — the
tenant has no native policy entity, so quotes awaiting approval stand in
for the submission queue (amounts are real, risk scores stay seams).

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `risk_evaluation` operation pulls live
     quote records over real HTTP from the globally hosted Static
     Dynamics 365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="risk_evaluation")
     and look for submission QUO-260105 (Willow Brook Legal) in the queue.
  2. No network? Everything falls back to the embedded demo layer below
     (APPLICATIONS / UNDERWRITING_GUIDELINES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     UNDERWRITING_SUPPORT_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your policy admin system),
     or replace _fetch_collection() with your own client. The fields the
     rest of the file needs are listed in _normalize_live_submission() —
     fields rendered "n/a — enrichment seam" (line of business, risk
     score) are where you wire your rating engine and loss-history feed.

OPERATIONS
  risk_evaluation | pricing_recommendation | guideline_check
  | exception_review | submission_intake | risk_assessment
  | pricing_guidance | coverage_structuring | compliance_authority
  | underwriting_summary
  kwargs: operation (required), application_id, user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "application_id": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "risk_evaluation",
        "pricing_recommendation",
        "guideline_check",
        "exception_review",
        "submission_intake",
        "risk_assessment",
        "pricing_guidance",
        "coverage_structuring",
        "compliance_authority",
        "underwriting_summary"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `underwriting_support_agent.py` and embedded as the fenced Python below (sha256 2687b8b34f22b995…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `underwriting_support_agent.py` first:

```bash
python3 underwriting_support_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 underwriting_support_agent.py   # or on stdin
python3 underwriting_support_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Underwriting Support Agent — a template you are meant to mutate.

Supports insurance underwriting with risk evaluation, pricing
recommendations, guideline checks, and exception reviews. In this template
an underwriting submission is represented as a Dynamics 365 quote — the
tenant has no native policy entity, so quotes awaiting approval stand in
for the submission queue (amounts are real, risk scores stay seams).

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `risk_evaluation` operation pulls live
     quote records over real HTTP from the globally hosted Static
     Dynamics 365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="risk_evaluation")
     and look for submission QUO-260105 (Willow Brook Legal) in the queue.
  2. No network? Everything falls back to the embedded demo layer below
     (APPLICATIONS / UNDERWRITING_GUIDELINES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     UNDERWRITING_SUPPORT_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your policy admin system),
     or replace _fetch_collection() with your own client. The fields the
     rest of the file needs are listed in _normalize_live_submission() —
     fields rendered "n/a — enrichment seam" (line of business, risk
     score) are where you wire your rating engine and loss-history feed.

OPERATIONS
  risk_evaluation | pricing_recommendation | guideline_check
  | exception_review | submission_intake | risk_assessment
  | pricing_guidance | coverage_structuring | compliance_authority
  | underwriting_summary
  kwargs: operation (required), application_id, user_input
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json as _json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/underwriting_support",
    "version": "1.2.0",
    "display_name": "Underwriting Support Agent",
    "description": "Evaluates underwriting queues from a live simulated Dynamics 365 tenant (quotes as submissions), with pricing demos and an offline fallback.",
    "author": "AIBAST",
    "tags": ["underwriting", "insurance", "risk", "pricing", "guidelines", "financial-services"],
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
#   export UNDERWRITING_SUPPORT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your policy-admin client. Downstream
# code only needs the fields produced by _normalize_live_submission().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "UNDERWRITING_SUPPORT_DATA_URL",
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


def _normalize_live_submission(row):
    """Project a Dynamics quote onto the submission shape this agent uses.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not knowable from the CRM alone' and the
    renderers label it as an enrichment seam."""
    state = row.get("statecode")
    status = {0: "under_review", 1: "approved", 2: "declined", 3: "closed"}.get(state, "under_review")
    return {
        "applicant": row.get("customeridname", "Unknown"),
        "line_of_business": None,  # enrichment seam — wire your policy admin system
        "coverage_requested": float(row.get("totalamount") or 0),
        "risk_score": None,        # enrichment seam — wire your rating engine
        "status": status,
        "underwriter": row.get("owneridname", ""),
        "_live": True,
    }


def _live_submissions():
    """quote-number-keyed dict of live tenant submissions; {} when offline."""
    rows = _fetch_collection("quotes")
    if not rows:
        return {}
    return {
        row.get("quotenumber", row.get("quoteid", "")): _normalize_live_submission(row)
        for row in rows
        if row.get("quotenumber") or row.get("quoteid")
    }


def _seam(value, formatter=str):
    """None = the CRM alone can't know this (enrichment seam)."""
    return "n/a — enrichment seam" if value is None else formatter(value)


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

APPLICATIONS = {
    "UW-2025-101": {
        "applicant": "Riverside Manufacturing Inc.",
        "line_of_business": "commercial_property",
        "coverage_requested": 5000000,
        "premium_indicated": 42500,
        "property_type": "manufacturing_facility",
        "construction": "fire_resistive",
        "year_built": 1998,
        "square_footage": 85000,
        "protection_class": 3,
        "loss_history": [
            {"year": 2022, "type": "fire", "amount": 125000, "status": "closed"},
            {"year": 2023, "type": "water_damage", "amount": 18500, "status": "closed"},
        ],
        "risk_score": 62,
        "status": "under_review",
        "underwriter": "Patricia Graham",
    },
    "UW-2025-102": {
        "applicant": "Sarah Mitchell",
        "line_of_business": "personal_auto",
        "coverage_requested": 500000,
        "premium_indicated": 2400,
        "vehicle": "2024 Toyota RAV4",
        "driver_age": 34,
        "driving_record": {"violations": 0, "accidents": 0, "years_licensed": 16},
        "credit_score": 745,
        "loss_history": [],
        "risk_score": 22,
        "status": "approved",
        "underwriter": "James Chen",
    },
    "UW-2025-103": {
        "applicant": "Downtown Medical Associates",
        "line_of_business": "professional_liability",
        "coverage_requested": 3000000,
        "premium_indicated": 67000,
        "specialty": "orthopedic_surgery",
        "practitioners": 6,
        "years_in_practice": 12,
        "claims_history": [
            {"year": 2021, "allegation": "surgical_complication", "amount": 450000, "status": "settled"},
            {"year": 2023, "allegation": "misdiagnosis", "amount": 0, "status": "dismissed"},
        ],
        "risk_score": 75,
        "status": "exception_review",
        "underwriter": "Patricia Graham",
    },
    "UW-2025-104": {
        "applicant": "Harbor View Restaurant Group",
        "line_of_business": "general_liability",
        "coverage_requested": 2000000,
        "premium_indicated": 18500,
        "business_type": "restaurant_chain",
        "locations": 4,
        "annual_revenue": 8500000,
        "employees": 120,
        "loss_history": [
            {"year": 2024, "type": "slip_and_fall", "amount": 35000, "status": "open"},
        ],
        "risk_score": 48,
        "status": "pending_info",
        "underwriter": "James Chen",
    },
}

UNDERWRITING_GUIDELINES = {
    "commercial_property": {
        "max_coverage": 25000000,
        "min_protection_class": 8,
        "max_building_age": 50,
        "max_loss_ratio": 60,
        "required_inspections": ["fire_protection", "electrical", "roof_condition"],
        "prohibited_risks": ["cannabis_operations", "fireworks_storage"],
    },
    "personal_auto": {
        "max_coverage": 1000000,
        "min_driver_age": 16,
        "max_violations_3yr": 3,
        "max_accidents_3yr": 2,
        "min_credit_score": 550,
        "required_documents": ["MVR", "prior_insurance_dec"],
    },
    "professional_liability": {
        "max_coverage": 10000000,
        "high_risk_specialties": ["neurosurgery", "orthopedic_surgery", "obstetrics"],
        "max_claims_5yr": 3,
        "min_years_practice": 3,
        "required_documents": ["CV", "board_certifications", "claims_history"],
    },
    "general_liability": {
        "max_coverage": 5000000,
        "max_loss_ratio": 65,
        "min_years_business": 2,
        "required_documents": ["financial_statements", "safety_program", "certificates_of_insurance"],
    },
}

PRICING_MODELS = {
    "commercial_property": {"base_rate_per_100": 0.85, "construction_factor": {"fire_resistive": 0.80, "masonry": 1.0, "frame": 1.35}, "protection_class_factor": {1: 0.75, 2: 0.80, 3: 0.90, 4: 1.0, 5: 1.10}},
    "personal_auto": {"base_premium": 1200, "age_factor": {16: 2.5, 25: 1.3, 30: 1.0, 50: 0.95, 65: 1.05}, "credit_factor": {800: 0.85, 700: 1.0, 600: 1.25, 500: 1.60}},
    "professional_liability": {"base_rate_per_practitioner": 8500, "specialty_factor": {"family_medicine": 0.60, "orthopedic_surgery": 2.10, "neurosurgery": 2.80, "obstetrics": 2.40}},
    "general_liability": {"base_rate_per_1000_revenue": 2.15, "industry_factor": {"restaurant_chain": 1.35, "office": 0.70, "retail": 1.10, "construction": 1.80}},
}

# ---------------------------------------------------------------------------
# Commercial underwriting capabilities (spec: commercial-underwriting)
#
# Added in v1.1.0. Each capability is a backward-compatible operation with an
# embedded response, grounded knowledge, exactly three synthetic records, a
# key field, and write/generative flags. Operations accept an optional
# `user_input`: an exact keyed lookup returns the matching full record; write
# operations return an explicit simulated receipt and perform no external
# mutation; missing/unmatched input returns a useful summary.
# ---------------------------------------------------------------------------

UNDERWRITING_CAPABILITIES = {
    "submission_intake": {
        "display_name": "Submission Intake and Validation",
        "description": "Reviews a new commercial submission, surfaces the applicant profile and industry context, and flags missing information before underwriting begins.",
        "response": "Here is the submission intake review with applicant profile, industry context, and any missing information flagged for attention.",
        "source_system": "Dynamics 365 CRM",
        "customer": "Summit Mutual Insurance",
        "write": False,
        "generative": True,
        "exact_key_required": True,
        "key_field": "submission_id",
        "knowledge": [
            "Applications previously required hours of manual review before an underwriter could act.",
            "The agent summarizes key submission data and validates missing information.",
            "It surfaces the applicant profile and industry context and flags missing information and risk factors so the underwriter knows exactly what needs attention.",
        ],
        "records": [
            {"submission_id": "SUB4412", "applicant": "Ironvale Logistics", "industry": "Freight and Trucking", "missing_item": "3-year loss runs", "status": "Intake review"},
            {"submission_id": "SUB4527", "applicant": "Cedarwood Foods Co", "industry": "Food Manufacturing", "missing_item": "Sprinkler certificate", "status": "Awaiting documents"},
            {"submission_id": "SUB4630", "applicant": "Northgate Robotics", "industry": "Industrial Automation", "missing_item": "None", "status": "Ready for review"},
        ],
    },
    "risk_assessment": {
        "display_name": "Risk Assessment and Scoring",
        "description": "Breaks a submission into clear risk dimensions such as financial strength, historical loss patterns, and operational factors, summarizing key strengths and concerns in a decision-ready view.",
        "response": "Here is the risk assessment broken into dimensions with scores, strengths, and concerns summarized for a decision-ready view.",
        "source_system": "Dynamics 365 Finance",
        "customer": "Summit Mutual Insurance",
        "write": False,
        "generative": True,
        "exact_key_required": True,
        "key_field": "risk_id",
        "knowledge": [
            "Underwriters previously identified risk factors inconsistently across submissions.",
            "The agent scores risk across hazard, financial stability, loss experience, and operations.",
            "It breaks the submission into clear risk dimensions like financial strength, historical loss patterns, and operational factors, summarizing key strengths and concerns in a concise, decision-ready view.",
        ],
        "records": [
            {"risk_id": "RSK7701", "applicant": "Ironvale Logistics", "dimension": "Financial strength", "score": "Moderate", "concern": "Thin operating margins"},
            {"risk_id": "RSK7802", "applicant": "Cedarwood Foods Co", "dimension": "Loss history", "score": "Elevated", "concern": "Two prior fire claims"},
            {"risk_id": "RSK7903", "applicant": "Northgate Robotics", "dimension": "Operations", "score": "Low", "concern": "Strong safety controls"},
        ],
    },
    "pricing_guidance": {
        "display_name": "Pricing Guidance",
        "description": "Provides scenario-based pricing guidance informed by risk characteristics and market context, applying standard rating adjustments to give the underwriter a strong starting point.",
        "response": "Here is scenario-based pricing guidance with recommended ranges and standard rating adjustments informed by risk and market context.",
        "source_system": "Dynamics 365 Finance",
        "customer": "Summit Mutual Insurance",
        "write": False,
        "generative": True,
        "exact_key_required": True,
        "key_field": "pricing_id",
        "knowledge": [
            "Pricing previously varied due to inconsistently applied rate adjustments.",
            "The agent recommends pricing ranges and applies standard adjustments through standardized rating factors.",
            "It provides scenario-based pricing guidance informed by risk characteristics and market context, giving the underwriter a strong starting point from which to make a professional judgement.",
        ],
        "records": [
            {"pricing_id": "PRC3310", "applicant": "Ironvale Logistics", "base_rate": "1.20", "adjustment": "+5% fleet age", "range": "42k-48k"},
            {"pricing_id": "PRC3420", "applicant": "Cedarwood Foods Co", "base_rate": "0.95", "adjustment": "+8% loss load", "range": "58k-66k"},
            {"pricing_id": "PRC3530", "applicant": "Northgate Robotics", "base_rate": "0.80", "adjustment": "-3% safety credit", "range": "31k-35k"},
        ],
    },
    "coverage_structuring": {
        "display_name": "Coverage Structuring",
        "description": "Proposes limits, deductibles, and endorsements aligned to the risk profile, identifying coverage needs and limitations so the underwriter can review and adjust before binding.",
        "response": "Here is a proposed coverage structure with limits, deductibles, and endorsements aligned to the risk profile for your review and adjustment.",
        "source_system": "Dynamics 365 CRM",
        "customer": "Summit Mutual Insurance",
        "write": False,
        "generative": True,
        "exact_key_required": True,
        "key_field": "coverage_id",
        "knowledge": [
            "Coverage recommendations previously required time-consuming guideline checks.",
            "The agent identifies coverage needs, limitations, and compliance considerations.",
            "When a coverage structure is needed, the agent proposes limits, deductibles, and endorsements aligned to the risk profile, which the underwriter can review, adjust, and collaborate on through Microsoft Teams before binding.",
        ],
        "records": [
            {"coverage_id": "COV5501", "applicant": "Ironvale Logistics", "limit": "2M/4M", "deductible": "25k", "endorsement": "Motor truck cargo"},
            {"coverage_id": "COV5602", "applicant": "Cedarwood Foods Co", "limit": "1M/2M", "deductible": "10k", "endorsement": "Spoilage coverage"},
            {"coverage_id": "COV5703", "applicant": "Northgate Robotics", "limit": "5M/5M", "deductible": "50k", "endorsement": "Product recall"},
        ],
    },
    "compliance_authority": {
        "display_name": "Authority and Compliance Validation",
        "description": "Validates authority thresholds and procedural requirements against guideline alignment, confirming whether a submission is ready to proceed or needs escalation.",
        "response": "Here is the authority and compliance check with threshold results and the disposition for whether to proceed or escalate.",
        "source_system": "Dynamics 365 Finance",
        "customer": "Summit Mutual Insurance",
        "write": False,
        "generative": False,
        "exact_key_required": True,
        "key_field": "authority_id",
        "knowledge": [
            "The agent strengthens compliance by checking authority limits and guideline alignment.",
            "It validates authority thresholds and procedural requirements, confirming whether the submission is ready to proceed or needs escalation.",
            "This validation is critical for avoiding last minute delays.",
        ],
        "records": [
            {"authority_id": "AUT9001", "applicant": "Ironvale Logistics", "limit_check": "Within authority", "requirement": "Signed application", "disposition": "Proceed"},
            {"authority_id": "AUT9002", "applicant": "Cedarwood Foods Co", "limit_check": "Exceeds authority", "requirement": "Manager sign-off", "disposition": "Escalate"},
            {"authority_id": "AUT9003", "applicant": "Northgate Robotics", "limit_check": "Within authority", "requirement": "Guideline attestation", "disposition": "Proceed"},
        ],
    },
    "underwriting_summary": {
        "display_name": "Underwriting Summary Compilation",
        "description": "Compiles a complete underwriting summary that captures rationale, coverage decisions, and notes in a consistent, audit-ready format.",
        "response": "Here is a complete underwriting summary capturing rationale, coverage decisions, and notes in a consistent, audit-ready format.",
        "source_system": "Dynamics 365 Finance",
        "customer": "Summit Mutual Insurance",
        "write": True,
        "generative": True,
        "exact_key_required": True,
        "key_field": "summary_id",
        "knowledge": [
            "By reducing evaluation time, the agent increases underwriting capacity, freeing time for complex cases.",
            "The agent compiles a complete underwriting summary that captures rationale, coverage decisions, and notes in a consistent, audit-ready format.",
            "With the underwriting support agent, teams can accelerate evaluations, improve pricing accuracy, and maintain compliance.",
        ],
        "records": [
            {"summary_id": "SUM2201", "applicant": "Ironvale Logistics", "decision": "Quote issued", "rationale": "Balanced risk priced with fleet load", "format": "Audit-ready"},
            {"summary_id": "SUM2302", "applicant": "Cedarwood Foods Co", "decision": "Escalated", "rationale": "Loss history above authority", "format": "Audit-ready"},
            {"summary_id": "SUM2403", "applicant": "Northgate Robotics", "decision": "Quote issued", "rationale": "Low risk with safety credits applied", "format": "Audit-ready"},
        ],
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _risk_tier(score):
    """Map risk score to tier."""
    if score <= 30:
        return "Preferred"
    elif score <= 55:
        return "Standard"
    elif score <= 75:
        return "Substandard"
    return "Decline"


def _guideline_check(app):
    """Check application against underwriting guidelines."""
    lob = app["line_of_business"]
    guidelines = UNDERWRITING_GUIDELINES.get(lob, {})
    violations = []
    if app["coverage_requested"] > guidelines.get("max_coverage", float("inf")):
        violations.append(f"Coverage ${app['coverage_requested']:,.0f} exceeds max ${guidelines['max_coverage']:,.0f}")
    if lob == "professional_liability":
        specialty = app.get("specialty", "")
        if specialty in guidelines.get("high_risk_specialties", []):
            violations.append(f"High-risk specialty: {specialty.replace('_', ' ').title()}")
        claims_count = len(app.get("claims_history", []))
        if claims_count > guidelines.get("max_claims_5yr", 99):
            violations.append(f"Claims count {claims_count} exceeds 5-year max of {guidelines['max_claims_5yr']}")
    if lob == "personal_auto":
        record = app.get("driving_record", {})
        if record.get("violations", 0) > guidelines.get("max_violations_3yr", 99):
            violations.append("Violation count exceeds guideline")
    return violations


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


def _match_capability_record(cap, user_input):
    """Return the uniquely matched record for a complete normalized key."""
    if not user_input:
        return None
    if not str(user_input).strip():
        return None
    matches = [
        record for record in cap["records"]
        if _contains_normalized_key(user_input, record[cap["key_field"]])
    ]
    return matches[0] if len(matches) == 1 else None


def _format_field(name):
    """Human-friendly label for a record field name."""
    return name.replace("_", " ").title()


def _render_capability_record(cap, record):
    """Render a single matched record as a full, decision-ready view."""
    key_field = cap["key_field"]
    lines = [f"# {cap['display_name']}: {record[key_field]}\n"]
    lines.append(cap["response"] + "\n")
    lines.append("## Record Detail\n")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    for field, value in record.items():
        lines.append(f"| {_format_field(field)} | {value} |")
    if cap["generative"]:
        applicant = record.get("applicant", record[key_field])
        lines.append("\n## Analysis\n")
        lines.append(
            f"Generated view for **{applicant}**: "
            + "; ".join(f"{_format_field(f)} = {v}" for f, v in record.items() if f != key_field)
            + "."
        )
    else:
        lines.append("\n## Validation Result\n")
        lines.append("Deterministic check — values reported exactly as recorded, no generative synthesis.")
    lines.append(f"\n_Source system: {cap['source_system']} · Customer: {cap['customer']}_")
    return "\n".join(lines)


def _render_write_receipt(cap, record, user_input):
    """Render an explicit simulated write receipt. No external mutation occurs."""
    key_field = cap["key_field"]
    lines = [f"# {cap['display_name']} — Simulated Write Receipt\n"]
    lines.append(cap["response"] + "\n")
    lines.append("> **Simulation only.** No external system was modified; this is a synthetic, in-memory receipt.\n")
    lines.append("## Receipt\n")
    lines.append("| Field | Value |")
    lines.append("|---|---|")
    lines.append(f"| Action | compile_and_record |")
    lines.append(f"| Status | simulated_committed |")
    lines.append(f"| Target System | {cap['source_system']} (not contacted) |")
    for field, value in record.items():
        lines.append(f"| {_format_field(field)} | {value} |")
    lines.append(f"\n_Customer: {cap['customer']} · External mutation performed: none_")
    return "\n".join(lines)


def _render_capability_summary(cap):
    """Render a useful summary of all records when no exact key is supplied."""
    key_field = cap["key_field"]
    lines = [f"# {cap['display_name']}\n"]
    lines.append(cap["response"] + "\n")
    lines.append(
        f"Provide a `user_input` containing a `{key_field}` value "
        f"(e.g. `{cap['records'][0][key_field]}`) for the full matching record. "
        "Showing all records:\n"
    )
    headers = list(cap["records"][0].keys())
    lines.append("| " + " | ".join(_format_field(h) for h in headers) + " |")
    lines.append("|" + "---|" * len(headers))
    for record in cap["records"]:
        lines.append("| " + " | ".join(str(record[h]) for h in headers) + " |")
    lines.append("\n## Knowledge\n")
    for item in cap["knowledge"]:
        lines.append(f"- {item}")
    flags = f"write={cap['write']} · generative={cap['generative']} · exact_key_required={cap['exact_key_required']}"
    lines.append(f"\n_Source system: {cap['source_system']} · Customer: {cap['customer']} · {flags}_")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class UnderwritingSupportAgent(BasicAgent):
    """Insurance underwriting support agent."""

    def __init__(self):
        self.name = "UnderwritingSupportAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Underwriting Support Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "risk_evaluation",
                            "pricing_recommendation",
                            "guideline_check",
                            "exception_review",
                            "submission_intake",
                            "risk_assessment",
                            "pricing_guidance",
                            "coverage_structuring",
                            "compliance_authority",
                            "underwriting_summary",
                        ],
                    },
                    "application_id": {"type": "string"},
                    "user_input": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "risk_evaluation")
        dispatch = {
            "risk_evaluation": self._risk_evaluation,
            "pricing_recommendation": self._pricing_recommendation,
            "guideline_check": self._guideline_check,
            "exception_review": self._exception_review,
        }
        handler = dispatch.get(operation)
        if handler:
            return handler(**kwargs)
        if operation in UNDERWRITING_CAPABILITIES:
            return self._run_capability(**kwargs)
        return f"**Error:** Unknown operation `{operation}`."

    def _run_capability(self, **kwargs) -> str:
        """Data-driven handler for spec-derived commercial underwriting capabilities."""
        operation = kwargs.get("operation")
        cap = UNDERWRITING_CAPABILITIES[operation]
        user_input = kwargs.get("user_input")
        record = _match_capability_record(cap, user_input)
        if record is None:
            if str(user_input or "").strip():
                return (
                    f"# {cap['display_name']}\n\n"
                    f"No exact normalized `{cap['key_field']}` matched the request."
                )
            return _render_capability_summary(cap)
        if cap["write"]:
            return _render_write_receipt(cap, record, user_input)
        return _render_capability_record(cap, record)

    def _risk_evaluation(self, **kwargs) -> str:
        live = _live_submissions()
        if live:
            lines = ["# Underwriting Risk Evaluation (live tenant)\n"]
            lines.append("| App ID | Applicant | LOB | Coverage | Risk Score | Underwriter | Status |")
            lines.append("|---|---|---|---|---|---|---|")
            for aid, app in live.items():
                lines.append(
                    f"| {aid} | {app['applicant']} "
                    f"| {_seam(app['line_of_business'], lambda v: v.replace('_', ' ').title())} "
                    f"| ${app['coverage_requested']:,.0f} | {_seam(app['risk_score'])} "
                    f"| {app['underwriter']} | {app['status'].replace('_', ' ').title()} |"
                )
            lines.append(
                "\n_Source: live Static Dynamics 365 tenant — quotes reinterpreted "
                "as underwriting submissions. LOB and risk score are enrichment "
                "seams (wire your rating engine and loss-history feed)._"
            )
            return "\n".join(lines)

        lines = ["# Underwriting Risk Evaluation\n"]
        lines.append("| App ID | Applicant | LOB | Coverage | Risk Score | Tier | Status |")
        lines.append("|---|---|---|---|---|---|---|")
        for aid, app in APPLICATIONS.items():
            tier = _risk_tier(app["risk_score"])
            lines.append(
                f"| {aid} | {app['applicant']} | {app['line_of_business'].replace('_', ' ').title()} "
                f"| ${app['coverage_requested']:,.0f} | {app['risk_score']} | {tier} | {app['status'].replace('_', ' ').title()} |"
            )
        lines.append("\n_Source: embedded demo layer (offline fallback)._")
        lines.append("\n## Risk Tier Definitions\n")
        lines.append("- **Preferred** (0-30): Best rates, minimal restrictions")
        lines.append("- **Standard** (31-55): Standard rates and terms")
        lines.append("- **Substandard** (56-75): Rate surcharge or coverage restrictions")
        lines.append("- **Decline** (76+): Outside risk appetite")
        return "\n".join(lines)

    def _pricing_recommendation(self, **kwargs) -> str:
        app_id = kwargs.get("application_id", "UW-2025-101")
        app = APPLICATIONS.get(app_id, list(APPLICATIONS.values())[0])
        tier = _risk_tier(app["risk_score"])
        lines = [f"# Pricing Recommendation: {app_id}\n"]
        lines.append(f"- **Applicant:** {app['applicant']}")
        lines.append(f"- **LOB:** {app['line_of_business'].replace('_', ' ').title()}")
        lines.append(f"- **Coverage:** ${app['coverage_requested']:,.0f}")
        lines.append(f"- **Indicated Premium:** ${app['premium_indicated']:,.0f}")
        lines.append(f"- **Risk Score:** {app['risk_score']} ({tier})\n")
        model = PRICING_MODELS.get(app["line_of_business"], {})
        lines.append("## Pricing Model Factors\n")
        for factor, values in model.items():
            if isinstance(values, dict):
                lines.append(f"### {factor.replace('_', ' ').title()}\n")
                for k, v in values.items():
                    lines.append(f"- {k}: {v}")
            else:
                lines.append(f"- **{factor.replace('_', ' ').title()}:** {values}")
        lines.append(f"\n## Loss History\n")
        losses = app.get("loss_history", app.get("claims_history", []))
        if losses:
            lines.append("| Year | Type/Allegation | Amount | Status |")
            lines.append("|---|---|---|---|")
            for loss in losses:
                loss_type = loss.get("type", loss.get("allegation", "N/A"))
                lines.append(f"| {loss['year']} | {loss_type.replace('_', ' ').title()} | ${loss['amount']:,.0f} | {loss['status'].title()} |")
        else:
            lines.append("No loss history.")
        return "\n".join(lines)

    def _guideline_check(self, **kwargs) -> str:
        lines = ["# Underwriting Guideline Check\n"]
        for aid, app in APPLICATIONS.items():
            violations = _guideline_check(app)
            lob = app["line_of_business"]
            guidelines = UNDERWRITING_GUIDELINES.get(lob, {})
            status = "Compliant" if not violations else "Exceptions Noted"
            lines.append(f"## {aid}: {app['applicant']} — {status}\n")
            lines.append(f"- **LOB:** {lob.replace('_', ' ').title()}")
            lines.append(f"- **Max Coverage:** ${guidelines.get('max_coverage', 0):,.0f}")
            if guidelines.get("required_documents"):
                lines.append(f"- **Required Documents:** {', '.join(guidelines['required_documents'])}")
            if guidelines.get("required_inspections"):
                lines.append(f"- **Required Inspections:** {', '.join(guidelines['required_inspections'])}")
            if violations:
                lines.append("\n**Violations:**\n")
                for v in violations:
                    lines.append(f"- {v}")
            lines.append("")
        return "\n".join(lines)

    def _exception_review(self, **kwargs) -> str:
        exceptions = {k: v for k, v in APPLICATIONS.items() if v["status"] == "exception_review"}
        lines = ["# Exception Review Queue\n"]
        if not exceptions:
            lines.append("No applications currently in exception review.")
            return "\n".join(lines)
        for aid, app in exceptions.items():
            tier = _risk_tier(app["risk_score"])
            violations = _guideline_check(app)
            lines.append(f"## {aid}: {app['applicant']}\n")
            lines.append(f"- **LOB:** {app['line_of_business'].replace('_', ' ').title()}")
            lines.append(f"- **Coverage:** ${app['coverage_requested']:,.0f}")
            lines.append(f"- **Premium:** ${app['premium_indicated']:,.0f}")
            lines.append(f"- **Risk Score:** {app['risk_score']} ({tier})")
            lines.append(f"- **Underwriter:** {app['underwriter']}\n")
            if violations:
                lines.append("### Guideline Exceptions\n")
                for v in violations:
                    lines.append(f"- {v}")
            lines.append("\n### Exception Decision Options\n")
            lines.append("1. **Approve with conditions** — Accept risk with additional terms")
            lines.append("2. **Approve with surcharge** — Accept at higher premium")
            lines.append("3. **Decline** — Risk outside appetite")
            lines.append("4. **Request additional information** — Need more underwriting data\n")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = UnderwritingSupportAgent()
    print("=" * 80)
    print("LIVE TENANT SUBMISSION QUEUE (quotes fetched over HTTP; falls back offline)")
    print(agent.perform(operation="risk_evaluation"))
    print("\n" + "=" * 80 + "\n")
    print("EMBEDDED DEMO PRICING (works offline)")
    print(agent.perform(operation="pricing_recommendation", application_id="UW-2025-103"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="guideline_check"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="exception_review"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="submission_intake", user_input="Review commercial submission SUB4412"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="compliance_authority", user_input="Check authority AUT9002"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="underwriting_summary", user_input="Compile the underwriting summary SUM2201"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="pricing_guidance"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
