---
name: "rar-aibast-agents-library-loan-origination-assistant"
description: "Reviews loan pipelines from a live simulated Dynamics 365 tenant (opportunities as applications), with credit demos and an offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/loan_origination_assistant", "rar_sha256": "2ad6d00682c63994761dfa50167f9ad6457547ee7ac1b624d112f4391012513f", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["loan", "origination", "credit", "underwriting", "mortgage", "financial-services"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/loan_origination_assistant`. The original RAPP
agent is preserved byte-for-byte in `loan_origination_assistant_agent.py` and in the RCI capsule.

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

Loan Origination Assistant Agent — a template you are meant to mutate.

Supports loan application review, credit analysis, document verification,
and decision recommendations for lending operations. In this template an
in-flight loan application is represented as a Dynamics 365 opportunity —
the tenant has no native loan entity, so open opportunities stand in for
the origination pipeline (amounts are real, credit metrics stay seams).

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `application_review` operation pulls live
     opportunity records over real HTTP from the globally hosted Static
     Dynamics 365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="application_review")
     and look for the Bluegrass Credit Union application in the pipeline.
  2. No network? Everything falls back to the embedded demo layer below
     (LOAN_APPLICATIONS / APPROVAL_CRITERIA) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     LOAN_ORIGINATION_ASSISTANT_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your LOS), or replace
     _fetch_collection() with your own client. The fields the rest of the
     file needs are listed in _normalize_live_application() — fields
     rendered "n/a — enrichment seam" (loan type, credit score, LTV) are
     where you wire your loan origination system and credit bureau.

OPERATIONS
  application_review | credit_analysis | document_verification
  | decision_recommendation | application_intake | eligibility_assessment
  | credit_property | condition_tracking | loan_summary
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
        "application_review",
        "credit_analysis",
        "document_verification",
        "decision_recommendation",
        "application_intake",
        "eligibility_assessment",
        "credit_property",
        "condition_tracking",
        "loan_summary"
      ],
      "type": "string"
    },
    "user_input": {
      "description": "Optional free text for the newer spec operations; may name a record key (e.g. APP-40021) or borrower. Omit for a summary view.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `loan_origination_assistant_agent.py` and embedded as the fenced Python below (sha256 2ad6d00682c63994…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `loan_origination_assistant_agent.py` first:

```bash
python3 loan_origination_assistant_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 loan_origination_assistant_agent.py   # or on stdin
python3 loan_origination_assistant_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Loan Origination Assistant Agent — a template you are meant to mutate.

Supports loan application review, credit analysis, document verification,
and decision recommendations for lending operations. In this template an
in-flight loan application is represented as a Dynamics 365 opportunity —
the tenant has no native loan entity, so open opportunities stand in for
the origination pipeline (amounts are real, credit metrics stay seams).

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `application_review` operation pulls live
     opportunity records over real HTTP from the globally hosted Static
     Dynamics 365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="application_review")
     and look for the Bluegrass Credit Union application in the pipeline.
  2. No network? Everything falls back to the embedded demo layer below
     (LOAN_APPLICATIONS / APPROVAL_CRITERIA) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     LOAN_ORIGINATION_ASSISTANT_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your LOS), or replace
     _fetch_collection() with your own client. The fields the rest of the
     file needs are listed in _normalize_live_application() — fields
     rendered "n/a — enrichment seam" (loan type, credit score, LTV) are
     where you wire your loan origination system and credit bureau.

OPERATIONS
  application_review | credit_analysis | document_verification
  | decision_recommendation | application_intake | eligibility_assessment
  | credit_property | condition_tracking | loan_summary
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
    "name": "@aibast-agents-library/loan_origination_assistant",
    "version": "1.2.0",
    "display_name": "Loan Origination Assistant Agent",
    "description": "Reviews loan pipelines from a live simulated Dynamics 365 tenant (opportunities as applications), with credit demos and an offline fallback.",
    "author": "AIBAST",
    "tags": ["loan", "origination", "credit", "underwriting", "mortgage", "financial-services"],
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
#   export LOAN_ORIGINATION_ASSISTANT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your LOS client. Downstream code
# only needs the fields produced by _normalize_live_application().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "LOAN_ORIGINATION_ASSISTANT_DATA_URL",
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


def _normalize_live_application(row):
    """Project a Dynamics opportunity onto the loan-application shape this
    agent uses. THIS is the contract your replacement data source must
    meet — a dict with these keys. None means 'not knowable from the CRM
    alone' and the renderers label it as an enrichment seam."""
    state = row.get("statecode")
    status = {0: "underwriting", 1: "funded", 2: "declined"}.get(state, "underwriting")
    return {
        "applicant": row.get("parentaccountidname") or row.get("customeridname", "Unknown"),
        "purpose": row.get("name", ""),
        "loan_type": None,     # enrichment seam — wire your LOS product catalog
        "loan_amount": float(row.get("estimatedvalue") or 0),
        "ltv": None,           # enrichment seam — wire your appraisal feed
        "close_probability": row.get("closeprobability"),
        "status": status,
        "loan_officer": row.get("owneridname", ""),
        "_live": True,
    }


def _live_applications():
    """opportunity-keyed dict of live tenant loan applications; {} offline."""
    rows = _fetch_collection("opportunities")
    if not rows:
        return {}
    return {
        f"LA-{str(row.get('opportunityid', ''))[:8]}": _normalize_live_application(row)
        for row in rows
        if row.get("opportunityid")
    }


def _seam(value, formatter=str):
    """None = the CRM alone can't know this (enrichment seam)."""
    return "n/a — enrichment seam" if value is None else formatter(value)


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

LOAN_APPLICATIONS = {
    "LA-2025-4001": {
        "applicant": "Thomas & Rebecca Harper",
        "loan_type": "conventional_30yr",
        "purpose": "purchase",
        "property_address": "742 Evergreen Terrace, Springfield",
        "property_value": 485000,
        "loan_amount": 388000,
        "credit_score": 762,
        "annual_income": 142000,
        "monthly_debt": 1850,
        "employment_years": 8,
        "down_payment_pct": 20.0,
        "status": "underwriting",
        "loan_officer": "Diana Cruz",
    },
    "LA-2025-4002": {
        "applicant": "Kevin Nguyen",
        "loan_type": "fha_30yr",
        "purpose": "purchase",
        "property_address": "1200 Oak Park Ave, Unit 4B",
        "property_value": 275000,
        "loan_amount": 265375,
        "credit_score": 648,
        "annual_income": 68000,
        "monthly_debt": 890,
        "employment_years": 3,
        "down_payment_pct": 3.5,
        "status": "document_review",
        "loan_officer": "Mark Peterson",
    },
    "LA-2025-4003": {
        "applicant": "Westfield Properties LLC",
        "loan_type": "commercial_5yr",
        "purpose": "refinance",
        "property_address": "8800 Industrial Blvd",
        "property_value": 2400000,
        "loan_amount": 1680000,
        "credit_score": 0,
        "annual_income": 580000,
        "monthly_debt": 22000,
        "employment_years": 0,
        "down_payment_pct": 30.0,
        "status": "credit_review",
        "loan_officer": "Diana Cruz",
        "dscr": 1.42,
    },
    "LA-2025-4004": {
        "applicant": "Sandra Blake",
        "loan_type": "va_30yr",
        "purpose": "purchase",
        "property_address": "555 Freedom Way",
        "property_value": 340000,
        "loan_amount": 340000,
        "credit_score": 710,
        "annual_income": 95000,
        "monthly_debt": 650,
        "employment_years": 12,
        "down_payment_pct": 0.0,
        "status": "approved",
        "loan_officer": "Mark Peterson",
    },
}

APPROVAL_CRITERIA = {
    "conventional_30yr": {"min_credit": 620, "max_dti": 45, "min_down_pct": 5, "max_ltv": 95},
    "fha_30yr": {"min_credit": 580, "max_dti": 50, "min_down_pct": 3.5, "max_ltv": 96.5},
    "va_30yr": {"min_credit": 580, "max_dti": 60, "min_down_pct": 0, "max_ltv": 100},
    "commercial_5yr": {"min_credit": 0, "max_dti": 0, "min_down_pct": 20, "max_ltv": 80, "min_dscr": 1.25},
}

DOCUMENT_REQUIREMENTS = {
    "income": ["W-2 forms (last 2 years)", "Pay stubs (last 30 days)", "Tax returns (last 2 years)", "Employment verification letter"],
    "assets": ["Bank statements (last 2 months)", "Investment account statements", "Gift letter (if applicable)"],
    "property": ["Purchase agreement", "Appraisal report", "Title search", "Homeowners insurance quote"],
    "identity": ["Government-issued photo ID", "Social Security verification"],
    "fha_specific": ["FHA case number assignment", "HUD-1 settlement statement"],
    "va_specific": ["Certificate of Eligibility (COE)", "DD-214 or active duty proof"],
    "commercial_specific": ["Business tax returns (3 years)", "Profit & loss statement", "Rent roll", "Environmental Phase I"],
}

RATE_SHEET = {
    "conventional_30yr": {"rate": 6.875, "apr": 7.012, "points": 0.5},
    "fha_30yr": {"rate": 6.500, "apr": 7.250, "points": 0.0, "mip_upfront": 1.75, "mip_annual": 0.55},
    "va_30yr": {"rate": 6.250, "apr": 6.485, "points": 0.0, "funding_fee": 2.15},
    "commercial_5yr": {"rate": 7.500, "apr": 7.750, "points": 1.0},
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _calculate_dti(app):
    """Calculate debt-to-income ratio."""
    monthly_income = app["annual_income"] / 12
    if monthly_income == 0:
        return 0
    rate_info = RATE_SHEET.get(app["loan_type"], {})
    monthly_rate = rate_info.get("rate", 7.0) / 100 / 12
    n_payments = 360
    if "5yr" in app["loan_type"]:
        n_payments = 60
    if monthly_rate > 0:
        payment = app["loan_amount"] * (monthly_rate * (1 + monthly_rate) ** n_payments) / ((1 + monthly_rate) ** n_payments - 1)
    else:
        payment = app["loan_amount"] / n_payments
    total_debt = app["monthly_debt"] + payment
    return round((total_debt / monthly_income) * 100, 1)


def _calculate_ltv(app):
    """Calculate loan-to-value ratio."""
    if app["property_value"] == 0:
        return 0
    return round((app["loan_amount"] / app["property_value"]) * 100, 1)


def _eligibility_check(app):
    """Check application against approval criteria."""
    criteria = APPROVAL_CRITERIA.get(app["loan_type"], {})
    issues = []
    if criteria.get("min_credit") and app["credit_score"] < criteria["min_credit"]:
        issues.append(f"Credit score {app['credit_score']} below minimum {criteria['min_credit']}")
    dti = _calculate_dti(app)
    if criteria.get("max_dti") and dti > criteria["max_dti"]:
        issues.append(f"DTI {dti}% exceeds maximum {criteria['max_dti']}%")
    ltv = _calculate_ltv(app)
    if criteria.get("max_ltv") and ltv > criteria["max_ltv"]:
        issues.append(f"LTV {ltv}% exceeds maximum {criteria['max_ltv']}%")
    if criteria.get("min_dscr") and app.get("dscr", 0) < criteria["min_dscr"]:
        issues.append(f"DSCR {app.get('dscr', 0)} below minimum {criteria['min_dscr']}")
    return issues


# ---------------------------------------------------------------------------
# Spec-derived operations (v1.1.0)
# Reproduces the mortgage-origination guided demo workflow. Each operation maps
# to one external-spec agent and carries the actual spec response, knowledge
# bullets, source system, and three deterministic keyed records. Writes are
# simulated — receipts only, no state mutation.
# ---------------------------------------------------------------------------

SPEC_OPERATIONS = {
    "application_intake": {
        "title": "Loan Application Intake",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": False,
        "key_field": "application_id",
        "response": "Here is the intake evaluation for the requested application, including borrower details, documentation status, and outstanding items.",
        "knowledge": [
            "Intake evaluates a new application immediately and returns key borrower details and documentation status.",
            "The agent highlights what documentation is still needed so nothing stalls at intake.",
            "Auto-ingesting applications and organizing borrower documentation reduces manual document handling.",
        ],
        "records": [
            {"application_id": "APP-40021", "borrower": "Jordan Avery", "program": "Conventional 30-year fixed", "documents_received": 7, "documents_outstanding": 2, "missing_item": "Recent pay stub"},
            {"application_id": "APP-40022", "borrower": "Priya Nandakumar", "program": "FHA 30-year", "documents_received": 9, "documents_outstanding": 0, "missing_item": "None"},
            {"application_id": "APP-40023", "borrower": "Marcus Delacroix", "program": "VA 15-year", "documents_received": 5, "documents_outstanding": 3, "missing_item": "Homeowner insurance binder"},
        ],
    },
    "eligibility_assessment": {
        "title": "Loan Program Eligibility",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": False,
        "key_field": "eligibility_id",
        "response": "Here is the eligibility view comparing programs, rate and payment scenarios, with a clear recommendation.",
        "knowledge": [
            "The eligibility view compares programs, rate, and payment scenarios and provides a clear recommendation.",
            "It presents what once required multiple tools as a single decision-ready view.",
            "The recommendation makes it easy to see which product sets the borrower up for success.",
        ],
        "records": [
            {"eligibility_id": "ELIG-51001", "borrower": "Jordan Avery", "recommended_program": "Conventional 30-year fixed", "rate_percent": 6.5, "monthly_payment": 2140, "decision": "Recommended"},
            {"eligibility_id": "ELIG-51002", "borrower": "Priya Nandakumar", "recommended_program": "FHA 30-year", "rate_percent": 6.25, "monthly_payment": 1980, "decision": "Recommended"},
            {"eligibility_id": "ELIG-51003", "borrower": "Dana Okafor", "recommended_program": "Jumbo 30-year", "rate_percent": 6.9, "monthly_payment": 3560, "decision": "Conditional"},
        ],
    },
    "credit_property": {
        "title": "Credit and Property Evaluation",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": False,
        "key_field": "evaluation_id",
        "response": "Here is the credit and property evaluation covering credit summary, financial strength, and property valuation.",
        "knowledge": [
            "Deeper evaluation returns a concise credit and property picture with credit summary, financial strength, and property valuation.",
            "The picture helps the officer quickly validate risk and move forward with confidence.",
            "Pre-analyzing credit and property data surfaces risks and readiness signals early.",
        ],
        "records": [
            {"evaluation_id": "EVAL-62001", "borrower": "Jordan Avery", "credit_score": 742, "dti_ratio": "34%", "property_value": 415000, "risk_flag": "Low"},
            {"evaluation_id": "EVAL-62002", "borrower": "Priya Nandakumar", "credit_score": 705, "dti_ratio": "39%", "property_value": 388000, "risk_flag": "Moderate"},
            {"evaluation_id": "EVAL-62003", "borrower": "Dana Okafor", "credit_score": 688, "dti_ratio": "45%", "property_value": 690000, "risk_flag": "Elevated"},
        ],
    },
    "condition_tracking": {
        "title": "Underwriting Condition Tracking",
        "source_system": "Dynamics 365",
        "write": True,
        "generative": False,
        "key_field": "condition_id",
        "response": "Here are the outstanding conditions with due dates and next actions; updates are pushed through Dynamics 365 and Microsoft Teams.",
        "knowledge": [
            "The agent tracks every outstanding item with clear due dates and next actions.",
            "It pushes updates through Dynamics 365 and Microsoft Teams, streamlining documentation and team alignment.",
            "Automated condition tracking shortens closing timelines by managing underwriting conditions in real time.",
        ],
        "records": [
            {"condition_id": "COND-73001", "borrower": "Jordan Avery", "condition": "Provide updated pay stub", "due_date": "2026-07-22", "status": "Open", "next_action": "Request from borrower"},
            {"condition_id": "COND-73002", "borrower": "Priya Nandakumar", "condition": "Verify homeowner insurance", "due_date": "2026-07-19", "status": "In progress", "next_action": "Follow up with insurance agent"},
            {"condition_id": "COND-73003", "borrower": "Dana Okafor", "condition": "Clear title exception", "due_date": "2026-07-25", "status": "Open", "next_action": "Escalate to title company"},
        ],
    },
    "loan_summary": {
        "title": "Loan Processing Summary",
        "source_system": "Dynamics 365",
        "write": False,
        "generative": True,
        "key_field": "summary_id",
        "response": "Here is the compiled loan processing summary noting progress, remaining steps, and a projected timeline.",
        "knowledge": [
            "The agent compiles a loan processing summary noting progress, remaining steps, and a projected timeline.",
            "The summary gives a clear view of the loan process and next steps.",
            "It helps lenders accelerate cycle times and strengthen underwriting readiness.",
        ],
        "records": [
            {"summary_id": "SUM-84001", "borrower": "Jordan Avery", "progress": "70% complete", "remaining_steps": "Underwriting sign-off", "projected_close": "2026-08-05"},
            {"summary_id": "SUM-84002", "borrower": "Priya Nandakumar", "progress": "90% complete", "remaining_steps": "Final QC review", "projected_close": "2026-07-28"},
            {"summary_id": "SUM-84003", "borrower": "Dana Okafor", "progress": "55% complete", "remaining_steps": "Title clearance", "projected_close": "2026-08-15"},
        ],
    },
}

_CURRENCY_FIELDS = {"property_value", "monthly_payment"}


def _fmt_field_value(field, value):
    """Render a record field value for display."""
    if field in _CURRENCY_FIELDS and isinstance(value, (int, float)):
        return f"${value:,.0f}"
    return str(value)


def _normalized_lookup_tokens(value):
    """Normalize whitespace-delimited tokens without permitting embedded IDs."""
    normalized = []
    for token in str(value or "").casefold().split():
        cleaned = "".join(char for char in token if char.isalnum())
        if cleaned:
            normalized.append(cleaned)
    return normalized


def _contains_normalized_tokens(user_input, value):
    """Return True only when the complete value is a normalized token sequence."""
    query = _normalized_lookup_tokens(user_input)
    expected = _normalized_lookup_tokens(value)
    width = len(expected)
    return bool(width) and any(
        query[index:index + width] == expected
        for index in range(len(query) - width + 1)
    )


def _resolve_spec_record(spec, user_input):
    """Deterministically resolve a single record from free-text user_input.

    A record key or complete borrower name must match normalized token
    boundaries. Multiple candidate records are rejected as ambiguous.
    """
    if not user_input:
        return None
    key_field = spec["key_field"]
    matches = [
        record for record in spec["records"]
        if (
            _contains_normalized_tokens(user_input, record[key_field])
            or _contains_normalized_tokens(user_input, record["borrower"])
        )
    ]
    return matches[0] if len(matches) == 1 else None


def _render_spec_record_detail(spec, record):
    """Render the full detail block for a single resolved record."""
    lines = []
    for field, value in record.items():
        lines.append(f"- **{field.replace('_', ' ').title()}:** {_fmt_field_value(field, value)}")
    return "\n".join(lines)


def _render_spec_summary(spec):
    """Render a no-input summary table over all three records."""
    records = spec["records"]
    headers = list(records[0].keys())
    lines = ["| " + " | ".join(h.replace("_", " ").title() for h in headers) + " |"]
    lines.append("|" + "---|" * len(headers))
    for record in records:
        lines.append("| " + " | ".join(_fmt_field_value(h, record[h]) for h in headers) + " |")
    return "\n".join(lines)


def _render_write_receipt(spec, record):
    """Render a simulated (non-mutating) write-back receipt for write ops."""
    lines = ["## Write-Back Receipt (Simulated)\n"]
    lines.append(f"- **Target System:** {spec['source_system']} + Microsoft Teams")
    lines.append("- **Mode:** Simulated — no records were mutated.")
    if record is not None:
        lines.append(f"- **Condition:** {record['condition_id']} — {record['condition']}")
        lines.append(f"- **Would Push:** status `{record['status']}`, next action `{record['next_action']}`, due {record['due_date']}")
        lines.append(f"- **Recipients:** underwriting queue and borrower thread for {record['borrower']}")
    else:
        open_items = [r for r in spec["records"] if r["status"].lower() != "closed"]
        lines.append(f"- **Would Push:** {len(open_items)} outstanding condition update(s) to the underwriting queue")
        lines.append("- **Recipients:** loan team Microsoft Teams channel")
    lines.append("- **Result:** Receipt generated; persistence intentionally skipped in this environment.")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class LoanOriginationAssistantAgent(BasicAgent):
    """Loan origination assistant agent."""

    def __init__(self):
        self.name = "LoanOriginationAssistantAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Loan Origination Assistant Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "application_review",
                            "credit_analysis",
                            "document_verification",
                            "decision_recommendation",
                            "application_intake",
                            "eligibility_assessment",
                            "credit_property",
                            "condition_tracking",
                            "loan_summary",
                        ],
                    },
                    "application_id": {"type": "string"},
                    "user_input": {
                        "type": "string",
                        "description": "Optional free text for the newer spec operations; may name a record key (e.g. APP-40021) or borrower. Omit for a summary view.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "application_review")
        dispatch = {
            "application_review": self._application_review,
            "credit_analysis": self._credit_analysis,
            "document_verification": self._document_verification,
            "decision_recommendation": self._decision_recommendation,
        }
        handler = dispatch.get(operation)
        if handler:
            return handler(**kwargs)
        if operation in SPEC_OPERATIONS:
            return self._spec_operation(**kwargs)
        return f"**Error:** Unknown operation `{operation}`."

    def _application_review(self, **kwargs) -> str:
        live = _live_applications()
        if live:
            lines = ["# Loan Application Pipeline (live tenant)\n"]
            lines.append("| App ID | Applicant | Purpose | Type | Amount | LTV | Status | LO |")
            lines.append("|---|---|---|---|---|---|---|---|")
            for aid, app in live.items():
                lines.append(
                    f"| {aid} | {app['applicant']} | {app['purpose']} "
                    f"| {_seam(app['loan_type'])} | ${app['loan_amount']:,.0f} "
                    f"| {_seam(app['ltv'])} | {app['status'].title()} | {app['loan_officer']} |"
                )
            open_volume = sum(a["loan_amount"] for a in live.values() if a["status"] == "underwriting")
            lines.append(f"\n**Open Pipeline Volume:** ${open_volume:,.0f}")
            lines.append(f"**Applications:** {len(live)}")
            lines.append(
                "\n_Source: live Static Dynamics 365 tenant — opportunities "
                "reinterpreted as loan applications. Loan type, credit metrics, "
                "and LTV are enrichment seams (wire your LOS and credit bureau)._"
            )
            return "\n".join(lines)

        lines = ["# Loan Application Pipeline\n"]
        lines.append("| App ID | Applicant | Type | Amount | LTV | Status | LO |")
        lines.append("|---|---|---|---|---|---|---|")
        for aid, app in LOAN_APPLICATIONS.items():
            ltv = _calculate_ltv(app)
            lines.append(
                f"| {aid} | {app['applicant']} | {app['loan_type'].replace('_', ' ').title()} "
                f"| ${app['loan_amount']:,.0f} | {ltv}% | {app['status'].replace('_', ' ').title()} | {app['loan_officer']} |"
            )
        total_pipeline = sum(a["loan_amount"] for a in LOAN_APPLICATIONS.values())
        lines.append(f"\n**Pipeline Volume:** ${total_pipeline:,.0f}")
        lines.append(f"**Applications:** {len(LOAN_APPLICATIONS)}")
        lines.append("\n_Source: embedded demo layer (offline fallback)._")
        lines.append("\n## Rate Sheet\n")
        lines.append("| Product | Rate | APR | Points |")
        lines.append("|---|---|---|---|")
        for product, rate in RATE_SHEET.items():
            lines.append(f"| {product.replace('_', ' ').title()} | {rate['rate']}% | {rate['apr']}% | {rate['points']} |")
        return "\n".join(lines)

    def _credit_analysis(self, **kwargs) -> str:
        app_id = kwargs.get("application_id", "LA-2025-4001")
        app = LOAN_APPLICATIONS.get(app_id, list(LOAN_APPLICATIONS.values())[0])
        dti = _calculate_dti(app)
        ltv = _calculate_ltv(app)
        issues = _eligibility_check(app)
        lines = [f"# Credit Analysis: {app_id}\n"]
        lines.append(f"- **Applicant:** {app['applicant']}")
        lines.append(f"- **Loan Type:** {app['loan_type'].replace('_', ' ').title()}")
        lines.append(f"- **Credit Score:** {app['credit_score'] or 'N/A (Commercial)'}")
        lines.append(f"- **Annual Income:** ${app['annual_income']:,.0f}")
        lines.append(f"- **Monthly Debt:** ${app['monthly_debt']:,.0f}")
        lines.append(f"- **DTI Ratio:** {dti}%")
        lines.append(f"- **LTV Ratio:** {ltv}%")
        lines.append(f"- **Down Payment:** {app['down_payment_pct']}%")
        if app.get("dscr"):
            lines.append(f"- **DSCR:** {app['dscr']}")
        lines.append(f"- **Employment:** {app['employment_years']} years\n")
        criteria = APPROVAL_CRITERIA.get(app["loan_type"], {})
        lines.append("## Criteria Comparison\n")
        lines.append("| Metric | Actual | Required | Status |")
        lines.append("|---|---|---|---|")
        if criteria.get("min_credit"):
            met = "Pass" if app["credit_score"] >= criteria["min_credit"] else "Fail"
            lines.append(f"| Credit Score | {app['credit_score']} | >= {criteria['min_credit']} | {met} |")
        if criteria.get("max_dti"):
            met = "Pass" if dti <= criteria["max_dti"] else "Fail"
            lines.append(f"| DTI | {dti}% | <= {criteria['max_dti']}% | {met} |")
        met = "Pass" if ltv <= criteria.get("max_ltv", 100) else "Fail"
        lines.append(f"| LTV | {ltv}% | <= {criteria.get('max_ltv', 100)}% | {met} |")
        if issues:
            lines.append("\n## Issues\n")
            for issue in issues:
                lines.append(f"- {issue}")
        else:
            lines.append("\n**All criteria met.**")
        return "\n".join(lines)

    def _document_verification(self, **kwargs) -> str:
        app_id = kwargs.get("application_id", "LA-2025-4001")
        app = LOAN_APPLICATIONS.get(app_id, list(LOAN_APPLICATIONS.values())[0])
        lines = [f"# Document Verification: {app_id}\n"]
        lines.append(f"**Applicant:** {app['applicant']}")
        lines.append(f"**Loan Type:** {app['loan_type'].replace('_', ' ').title()}\n")
        categories = ["income", "assets", "property", "identity"]
        if "fha" in app["loan_type"]:
            categories.append("fha_specific")
        elif "va" in app["loan_type"]:
            categories.append("va_specific")
        elif "commercial" in app["loan_type"]:
            categories.append("commercial_specific")
        for cat in categories:
            docs = DOCUMENT_REQUIREMENTS.get(cat, [])
            lines.append(f"## {cat.replace('_', ' ').title()}\n")
            for doc in docs:
                lines.append(f"- [ ] {doc}")
            lines.append("")
        return "\n".join(lines)

    def _decision_recommendation(self, **kwargs) -> str:
        lines = ["# Loan Decision Recommendations\n"]
        for aid, app in LOAN_APPLICATIONS.items():
            dti = _calculate_dti(app)
            ltv = _calculate_ltv(app)
            issues = _eligibility_check(app)
            if not issues:
                decision = "Approve"
                rationale = "All underwriting criteria met"
            elif len(issues) == 1 and dti <= 50:
                decision = "Conditional Approve"
                rationale = f"Minor condition: {issues[0]}"
            else:
                decision = "Refer to Senior UW"
                rationale = "; ".join(issues)
            lines.append(f"## {aid}: {app['applicant']}\n")
            lines.append(f"- **Loan:** ${app['loan_amount']:,.0f} ({app['loan_type'].replace('_', ' ').title()})")
            lines.append(f"- **Credit/DTI/LTV:** {app['credit_score'] or 'N/A'} / {dti}% / {ltv}%")
            lines.append(f"- **Recommendation:** {decision}")
            lines.append(f"- **Rationale:** {rationale}\n")
        return "\n".join(lines)

    def _spec_operation(self, **kwargs) -> str:
        """Generic handler for the v1.1.0 spec-derived operations.

        Deterministic exact-key behavior over three synthetic records with an
        optional ``user_input``; renders a no-input summary when no key
        is supplied, and a simulated (non-mutating) write receipt for write ops.
        """
        operation = kwargs.get("operation")
        spec = SPEC_OPERATIONS[operation]
        user_input = kwargs.get("user_input") or kwargs.get(spec["key_field"])
        record = _resolve_spec_record(spec, user_input)

        lines = [f"# {spec['title']}\n"]
        lines.append(f"_{spec['response']}_\n")
        lines.append(f"**Source System:** {spec['source_system']}")
        mode_bits = []
        if spec["generative"]:
            mode_bits.append("generative")
        mode_bits.append("write-back" if spec["write"] else "read-only")
        lines.append(f"**Mode:** {', '.join(mode_bits)}\n")

        if record is not None:
            lines.append(f"## Record {record[spec['key_field']]}\n")
            lines.append(_render_spec_record_detail(spec, record))
        elif user_input:
            lines.append(
                f"No exact normalized `{spec['key_field']}` or complete borrower "
                "name matched the request, or the request was ambiguous."
            )
        else:
            lines.append("## Summary (no record key supplied)\n")
            lines.append(_render_spec_summary(spec))
            lines.append(
                f"\n_Provide a `user_input` naming a {spec['key_field'].replace('_', ' ')} "
                "to drill into a single record._"
            )

        lines.append("\n## Knowledge\n")
        for item in spec["knowledge"]:
            lines.append(f"- {item}")

        if spec["write"] and (record is not None or not user_input):
            lines.append("")
            lines.append(_render_write_receipt(spec, record))

        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = LoanOriginationAssistantAgent()
    print("=" * 80)
    print("LIVE TENANT PIPELINE (opportunities fetched over HTTP; falls back offline)")
    print(agent.perform(operation="application_review"))
    print("\n" + "=" * 80 + "\n")
    print("EMBEDDED DEMO CREDIT ANALYSIS (works offline)")
    print(agent.perform(operation="credit_analysis", application_id="LA-2025-4002"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="document_verification", application_id="LA-2025-4004"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="decision_recommendation"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="application_intake", user_input="Process new application APP-40021 and show its documentation status"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="eligibility_assessment", user_input="Show the eligibility view for ELIG-51002"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="credit_property", user_input="Give a deeper credit and property evaluation for EVAL-62003"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="condition_tracking", user_input="What conditions remain for COND-73001?"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="loan_summary"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/6286a7jVrYm+CpC1I+bmbLNUSTlwu1uTuI8zywXbM6kxHkQSeXNd2/qnIiwM9NVqAb64ERAIvdee43f+hYQO/7+JVrmshu//PyFFCjSsr/88CXNpmSs+rnq2uOxmT2rbJ1OdRe1p77qs7pqs+mUj11zik519cxOU9UsdTRn6YnZ26ipkumEYJfTnLVRO5/+0vV9N85LW83VsTE6fvu+rpLofcD01x9OazWXp2TM0mo+pVnTHQva9Phz6vL8fdgpj+o6jpLHT4dy2RY1fZ1NX37+H//zhy/V8fnLz3//ktTRdDz6Ih9KamNVVO2HdHKaqmk+lCCLrJ2P3XXUFseyfj9sbo/vfTbm3dgcj9IsP3399pcpq/MfTn/722ONxmL66+nH/+s0zePPv7Snrz/dsfLjgNN/nj4X/VRk819++fL9xS9ffjj98uUPhv46fvjxly9//V1MWk19NCflIeXvvz99//z51p9Pb81++vXf3/3wr9s/3flr1Eb1fvjg973/8uLfNqZdsjSHs359ZmOVfz3l9+1/+vrfhWRJNX1ql3TNsT79VzF/vuAPgv7x+8fySIc6Gw8vfXPYh7e/+/oPHq3yb6t//medxmxexvbby798j+0/bf09rFV7snSW/lXTWZO0BU21/lzepzVTnyW/ft/8Z8K/Ls9/+fK3v7Hj2I0//+1vJ6d9tN3a/uHY3/7+/fM/fvvply9f/nGkeHvk3pJ8FMuRp//tv52UKhm7qcvnk5V0y3wal3aumuyX9pfWLqvpdPzOZXacecRoquI6+7quH7t79iHoqKzTb/9PVMXRNP8YvWtj+rGu4jEad+Bd5792v9fQr9G3Ivrtp5N9yP36rj6ZpK7/0n5sf5/Zj9mUjc8DBeJ9zn48KunH94e3L3/7Xwv99WP/T/3+20fVH4vfupu0cEqiflrq7Ke3XV6ZtV+tSA5gyLYsWQ7RdZcceuTVgQc/HPZOXX2g0fz2wfSo6vrIlyO/5m7cP2Qffvr5Ley33347DC9/aT9hADl9wt0EHAu+q3P68cfDoAN/inL+pc2Ssjv9x9//8R+n/zr973Z9CH+foR8Gfo3CoaFoaerpSImP0jkCdIQ0i9KPKPz9H1/deohpjyT/rKvsc/OBfo8s/eZjiyd/hC/YKc4O3x5+bd6wWrXFqZp/Ogn56bu+x6HvVweOnspueoNqf1RY1ib7ITU6zPnuybabT9MRkSnffzgtU/Zx6m9HInyo2PyaHMt/Oym0fpq7rj7+eqv5sejY3LVH/dffM+Dz+SFk/I/pRH0T8dNJfefhqY/GqC/H6OsZefQZl248fdt+CI9O7YFz7RvVs7erPnLl0z3HosMzydeQ/viO+ekNHUdgp29nf6z56EN2d2R2Nv7STl8TPhrfoUi6Q5X9VCxVGrVJ9t+/ptRUdkudfvjv0PQt6WsU0q9R+cjBd285/aG5nL53l9NHezn9ssAghB5GHGb373542rvl4+Qme686DGyWw6bPlLaW/jNIH431D5B++grp31rid6g+fQPf07+A7zu5vyHq6Z8R9WjUh4vr4+s7Ub6jy3QkTPtZKd+VjQ6lqvbHryn0b1odS4+0etd4+/bwu43/c7v/vc3vX13xS/v25VcaUB472u709t0z+xR/SDoW/3Caurdm7emficLbtR+AcFjwKekPAPKdiZz+EjXd8q6qzxBH9XfHNdk8vpU7BO0HUkfN9NcPz/Oad7J5wTrZrKLLpM2ePM2UrDdaQz+dtCMhjsJ8nxd322ey1lExlVV/+u3fO+9vf4Dvfqnr6YMSfUX+P7rkHZfxyNV3Cn6iAm/b+ieP+kjeuosPnrN/lOzhYOud/clXQX/Kq8h3ip/k6HCClh/pcOD8/i656VsmTvvbbfO7aqI5+uFw/1dxbwe9nR/VR1at3fj4xufafS2zMfvrt25XznM//QwAjy7df1x/Kg6mtsQ/VR0wfWj3Y/pVrx8PvYCor4D3QcDz+hMMfJVgj/vP34nVd1f95/+eG70DX3fd4yN5386h6iUrxjem0p+xddqPqv5jfn5iwLe8+OktCj7Q50i5bH7b+H+f2Hf1H0l/VMKbUk6nN6l8l+V7Y9bEWZpm6QcFPdXRfvg2zupu/arTX2SNVH89Wp4s0J+U4AScjq+m5pLyr7Qp2KwpkH/95vu3yE9kaz/wLzm0L7PpW2J8MtsPJZGfTkr0OPB8fuPFeCTy/LFbFlz2xJA2ebJYUvnU5c2f5q8yPvTRTIET1A99fiUtS7BsUrV/fe/61THlt21HTE8ac4Tlx6mM+sO+Awv67oDbb3a9D/1MyO9Z1o3FD29o/uhb2fZO4mPjR4p8rJY1668fCw5EqKPkW7r/mmcHOfs16er6E3b/8tdPcv+x6U11krp6N8oPRD/wtU6/NcnpW9F9FfWB722WpZ91XVcfNXHE+Nf2SKSorl7Zr+9C+yMX/st353+K/ipqfPe+I2sOXtoC0bclWXtgQ/mBpm9o+OXL6S8fmDTvffYdQaajZI9vsu3+9a3GV4EfJfKB7Wv1+WH8xLM/4tP0UYofmfxVWLwcTl4+EOh3WvkW+e+VcLCMf+Hpx5M/Z+bH/v86/S/o9PHmj7KPmL/z7L9OR4EUVVzVByy9iVg2TW+5n6K+nntwxaNWD9g6nnRH8/gQMI9Hvbyr578+7P11Wo7+O+7vjZ+M9+c/gOFfxmxYDv+kR6b8kxbpB9MYD3X65WMmO5Dr6NNffm4P+Pzhy5GC2f/BJPfmEwfAHwz3Pf99VbfKPr7983HvJ++oHkIPJn2o/2bV3/V8v83a5RgB/8efQNJx0L8E4j0f/1kgPubmP43C8ebfo/CeZP80Cr+f+C0E7yf/FoK33/4Qgi/HLPxvNv7By4eR/zzVax8f3uR5zN4tepu/Y+1BwQ68es80f+AL//3UHE30HZuj7X+2stMj209/yX4qfnrD4I8oCMLQX9+gEHfHhHPIOHppU33KjU5fFT29vfqe4/9F20Pdb/nyjsTv4fndsC5+Ty9vw9585XNs//uXIweid9P5mgVfB5xj+THM/Di96R0A/QQeBx7fP2n68e7/8+jzdf+BoAcBPwTAUYqlIIgRcIIh1yuKY1CaRxcQwvD8erxDL/gFxbMMjxIoxmA0hSA4R5ErBELwBULyQ950wEaS/frOlOqtU5zHFziJoRzEieyKo9kFArEsvUJYfMnT7Epg1xi5XrLftx55kH419NOwtxe/T2EfhfBp79+/xBh6rOTRSSA/f2jg6lwjRIlN9NDYemJbP7lYSDqi28CjuO8WuCijC1/rwZ6tpnbRjQ9FLoFajm+EsDFd3wHQFi+BUGBAAegznxLEpJ/9gwU8bD2NGCMySLVTuTKEprBH9fsktEY7LgAbL/TLLq2Lk71QJZsVTX/hOgBACLGVSgioupU3McU+XuTj0iC3iS3SqZ7s9Sl7G+gADbHTinAOSotLztfrXpJUu2uXPFevxXqhFSTs8GdGTkGv3LjVpkPUohCdt/mpre8rcONjxeLjysAYVAlVajR3tFKLC3UhVB86TA8IiCTikbVbwrVVsNvSfFUh+KzpfrLfgwk1ksV4gUq25hSxiasgtg1BiHCooa8AX6ZrIcAvy18RvyJVdRF66lqcX20njTlMCgm/LCSpOhJVFqBDCYsTP10wUyK7reTHWXicSbLTiwTJNT3N21GLlWIyeLISr8b5gjaN8OK7TLgRVDgJBT5hhUbp15UIH6rev0A4ovC0bSPOt8ML+swQYIrvHIzArGNNMKMkMh2j9PPK+09NFAcsAeKbIBjzbUll6zHB9mvV3ZJvqIEp9ItiLdRYSpxAjdS93A+HUX068WTw4hq9ouxMu+xIoAqVMbZQwbRJh3K2IIF1iIH06yGCmKKfZSUmyRAAb7rY3zb+bq5F1pECTxH3Se3kjix9k3rcj1FNvV1Z9cKRhc/7103PkvtIYXKqCngLJrwHNeDq3e2ntylIWwWIbOfBUazPy6OqINJy5n6/LKjPxCp8jTNoog2aSXieLBhpTWQtEmeudCOrcM3kmkjeVZCL2nx41lNXLL1oUokT+eDuAOfHvWYYHYNu4mYUU4HHdqDFZHBHbnAO39JOT+gztQT58iqIeUVXaHL084sPXymhakKnHtQsS1Ba4kfmmVFZcDOOhKwS+ILI+1WzOwIvLppEvPAgyLUDObQhgR/Z9QFySHqVepZgzZZVdxxRE7RiC33xzFCwN0/iEBgW21cFtQqFGDTNrzG7XW2QOKdpvYVXqgQ8vLU5aiPpNabXit0d/3nREVHzblUKjNcHgBXJC1unUL9OfiY9ULEOqZyfKFuNtFEJvCOpAJ28Wp7DFWi/sMDLpSiNe5L6GXoCaP/aRqLawKMAi3rI/ac9QiT9QFqNe4z+rARn3kGmIKPQHK1lB1vWrGFtkM4uV/VpJh0byYxLk76GUvhZIQyf7c6mZGwDzhdeSIiK7Sdoew2828xDd55It3wJwCo0n6NfKuANJm8NRTX0c8WDPgIuKRXjnd7ZYC13i3mUbSCJEK4saaCzRlHnzJTm0njHSMGhDbnHkNnPyeo23iXXBm3afKxjkIIPQy1YSHnewjhpYdIvbnmT5qFyjSVfR4PawuSoByUeVzFEx6P1XL6SJrqV1UXqn4xmFuiMofxSJBxo8ebG0aJT7tABlWhRDAcCsRMFGcCrYCeHLM9OaM+R+lBbnaZyC3/6OW35ZjHIx9jBX8WCEe6oMCnMoHDWLmTkXX6JKrYGop4kXC44bDFf7YP33+Migp/LpmoeBur4ogYc1as6UPiJV6u52aCCr4xQek6adSQgGIwOTgBiAUdDXh+f3TNUPlzvGW+kjrwqU8OtW8h2CrKwd3hQXPt5lhzpyr6UQMca1sr6Cw4SskhO1yVW7/BL51PF3+HYjwW+K8PxSJiLrfNaQ3m0bHbgg4phDIYhk3my/pU4QzlPuWYFWtRALoaByfNtYw44mlPFo1iJZEhWvgM0zOFzL1B8XJi2n5ZDcfPhSsP5Dua7V6OIE5gQkgfqvZO7/YPCueCZeIHI8qH7NNVHyp1hqqaTyqMpi4ZEzlGunMgYnf0Qxkd94cZ0sySmF3USojfp8iIG3Oaxe6t4L4bQbclozG0xEBp1k43mL5JDtUmJ0pZO8E+FoFZysPkXrHeocS0peKXxK0JtZR1CiEAaYq8XLU0Z57mZG7TxANjSaDNTbleanTxLbVvXUHo+5HWAeXJXaLDy7hLQw+2loBggKNDEVbvQ3Lcp5vZrQADtmYSrCxI4U8nPrVysAMIB9t1hu7kDfVBbgvsFYauVGBjR3OuZ8aiVCuMhK/aENhZFUl7aFs/UVLKrxF5hnBDiuqxBslRUIDgIgbOyL0M7QOxKYR1fXIjtSD1MYR76GGtj23QyBbIQaqsK91RJ2QQxaNkw4qYNfnYNQPLgvFyhQPQuoJcil+gU1vIqZSc2tDepvDNlA/pQOadY2OPHeTIov3D4PvYP3dwruoi4NNHJ+BjKfEohliPLb+kTSPvJFFQDiTnTOmPl6ypxMlb6t0CxedE2df0VBrhyQR9HLx8xv6T7p1YGZ0+DB5L1nzkfkeY+C8uV8jrmKSjPx1nfwIfwnHlXdTQ1y9EXaT7wschiLWhE9yaoafvKYoJahLqxRbYIHkE8V/yyKvotXvSplPl0YrpLY9u9GnmLfQ1EtNHOC1jjPkSvXHHtO2B9GpI8M7M/VjEII91YBwzeuPm8YRbHAnPLyI996YB+3qmr2aZ6WeSGvcXCOAu4zqipy1nQMw2uw3W8n01fM9ZSArqLxFIPC0uBAxZ5g5ISBDNWy1ECXsFuzPyiAfssSX0prEx/Z8lhZTqaiPrQsrcFn7TGvmwjYreF1tHLE++8s04/jReme2F+XqVVNYpxdVGZs86FzsRMWo4363oD90jwA2PUHMUCGPRGkGBu+bZBbITk+sU4xyBg7hadWWMVGmtfUNY6BY26BS5WOJMWG3dhcZUqS808eoKyvd54O5CFhlVfzN0nnd6scLArHEajbu28rYrK0/ec4pZKrRqesCeoAJbWXFZo9O1sNnB2Ky8gb9nX1i3RizIzE6ZeUPJe4KjWFO4ZqWzf6ASpKKahWr0DHaodvLcsvj4WiNXxTqbx+Kwudi5oPhJoiUik3bRrI5vR5sTs5oNPfQXkXwYg6bvHQee7stoJSSITujE0o+2SPYBoXMDdRkkdp+BMujlTgEeaftWlOau6BLqv4qEka6f0kEVB6gV+N7CU7AsOp/uY2W/n2V+GO6qj92uvBWSWk91j2wXWSyiB1lBvTkCwImO5e806zaIq48Blw6LjpEjNOpcC7XWZygU3SwnSq9wZ4PWoK0w4+BhxM5VipmTiAovlmWQiGj1f2If3EFizWaiCTjZ3d8h7Fvhc8WJKdOSzVJcsXnUtzY7YuWisYmGZmrqu0VQn9SM09Jb0AIPCmw5lJeXiYwO87u4jnKBhl+C1kYR7MMQUsgphuM+3O4bbdk5SsUkDyJGMVIrbYSAu8TUf3TXHIeFKVbUdyqgxwtsOqRKYiQHYE8lOXigQqkKxiBR3ZQqDB4rohtJC1dR0oKZS6dxd8rWq47mvKW5t9/kSVmtbij7IiReTpFbRMI3iKgYIqc/9hTVh1QdIfiEyIFoy5JXoXswjsSKn83hZjnI297Flrl4On42xHDWQWydimvUM9pZzNGZIYSyexJqjQkJNp4wAI8Q2YxIan8cUnXDF1Med3NIqwEyKugbn843DccdrwqhTiUxdsYlqCdxTnOtdOyAp1h/D9ZrFLvPwQbHiW718rqwe4IEInHXSSu0qhCTDKqECDwYAvqbjM/WkwE2BHJmwa70JVmXqzPmVTSmK+ffzmRTgAdWB8nxGfAx6nMFrAUAoViETGx+Irk7rorMeE5WFYXM55ad0q2Jnwu/YaloyDZOpXCjIdB7mtH8sLw3mLcSr0mzFnpOmrYvpw04XxUs84JA1ATNw4Z07frbMMOGB/tGd21erTVcmMB4QiM5nBi7jbErWbAQoHqT5JzS20i29XpzxYEoYjqQq8pRd4A4d9kk3H7v6eEue4as/atflyJFlfoZS/eYKjUc8Oen2ulBBvW2gC49uvb/2eHKqfA3vBW2JvjFWQW23V93qjClsA700es58YrHE+4ppuwOKVxWJE05a2KhDPkbkhQ99nRV54+D+A8bN4ebK6Vjft6f/yhFRfl5Y6xyqfCwdjLpxKVm+Zc/M4YbNZUxWvS4zhM8y5zHu5k4gmd711iIBjbHkGsEWODGvMXzV88CWdMPMKC9vHb+OlvN5qF9HMBaCms+Lt8BIdvFkwB9cYMazwcXH0FmOHiSuG5gBRixTzYElluThWcvjpeEh4XB57hDZ29zQ3vObecGma1UjifDMVwk3jDOlZxkuHSgtZ3hVe+AwnEnKf4iFCo0QzFZLt5BAClmgdva2fMU2mcSNY2b1w9hIoH4o5FXWCmtn5hDUF6wyJbi14U2cEt/cAH1ZEuYI0HUjMtsvE4C7Rt5lLEYMUV/lumkTp1xFdAyZSl2GQXslXcND7W3vrvg8T5ztoyVCnrNx5gA5awMogYOdEu88GOEu4aGEIPQ3SR9S9EpI+rbhvU2JVGEbLEw3Eh0VYOnAWkMz1zOK1g9t5ea75wx8ksn7UkKGZQdqZhUIxTN2F7amtEa7lpYzc3+ijJ1mqh5cPA2xSXw7k/liR2ZGkybbCN76xEWjrsZHupu7hBRsiN1B9sKDabfUnFMoBNyu4baymMa6HWBIYZHbF8UoXreGsW1CZOLu9cjRcqHPqcYz9+JeyHD+4i7F3pagAvCuzFwInTvG05VdBPqSMA9nZHJ2oQBSSKEpqjEFgR1YJ+r7jEmiXCEUcbg1zDtHW+7aQxZ6kxzO1DCxqJ6EwtleGQACLTS7aRsn2ZkfqvdiYRSzDPM1fqpBp9ypGXU0634515ftRlR293oWHObPQtAST7qCthrEc4yP22y1Su5GUpd6kX2Aqr2DieV8DPUzKOmkxJeTbc7dAL1KTMWKOUAO3DDHu3qhLS2FlZJg9sawZhWf9iCt6I2+11yX68FASmB4QQxR7+6FRA08SZFp2xa7DT3DrMwis1CBB8ifbdM/45CPEwGKsUe/0Y0zRyqrk3RLCqtTy/OvMXsoqOZEuWdQ58fzCZvZ5K4ZjHCGq3amE7UvdeBdZFnzY+6yFmeYETWfdiTIII8VVeD+kB15DSW4IokiGFCAKahpHx1nGSjTqZ/tMrEZv0xhyQrhVBurqViMO3qUfdv4XqE9KCr7aCUZfVye8Nrn9OtBr/v9orjapEAHuyprJ79brRROY9LXHHh38d0bwvZJXRsEzgs3bGWIiLqzmETDFE1WHNfLDZbP4oiOYk1SDM+Tt+4mS6grHCODH6iacodhnySqGzaHrZ3tT5YShKcMOmRCE6sIA4/9MpgHaaPbilLrzFWnxE0vEuBhjyXZaTG1esps6PzSDFO67l2GLAcP7MAdrpmDqMma0sQkcszhehBnzJjgpgIJeqEHtwk54Fml4ajfa1ThfPJxroKwjNKQpQuZ3KlnB51BIMWScQqUiuak5NbatZFwa8qFDwInb2Xcd6uKEblpCy6JMIssNhv1Qujw3tGqqG+WSzmcSM7RgNbTRYa7vrDSJ262gnhAAg8QGc3qDh1vZ6BryFEvsZtPugpFqwxhL4Koi8+b8+K35P4yo9JFgyUh2mcFkxNgr1YOkxzkoWujMswmnwNSCSfwht4f1+hFGS3/aDomdUVtza/evTf9Im5gouooZ7TPCLg8ntRNZoBCh2HmEgbJat0DvGeaFpCjNo/l9F4r6T1GX0JqiK92iCy372tEfdRJG9MCF1zuDUfLaYiUkHI3mnv9QhSAeg5eca2zYBaAi9zRtM7AjyfjtMwNvNzKyqatEAjIifBXX8kEjcYpNLdtCkCteFtlS+eWLnEyS1Q1q+Qv92dBaUqBW5rC3NhWeAmzmnhndH/0mwEUotvcuFvAz/2armhMS6EQSMOgk+cHxTXBa9Ra/Wk8FzCFm8Hzm6G93eV+KmmTk0Gj9RBHgfyu8vrnooe8eGusShPgUPJ1R3spcQCQHpkDj1UNe13IoO7uXSVkEm9yeHvpU1EiXfMYaI+F5uuqbFzmrpOzBpf4TlVsNW5uifvEhbtkL6tYr5Qs8QghFncGpbDJhMp9Azyl5M1jQoa0C1ogRWU1ModPF1jObGJm7VYJtKoKCwQYRUHJiQJ/nX0QBg50wHpWlnHwdo9cghsohXSysgWfRqx5O4/tlL146dIrfZ/ceJzHh01uF7nthXFJTbcgDGkd11S4WHeD3S9lf4SHr9eySkvyldEhRhjt89XeKEMOV/T5nMd6rkLQ42PhAW7JlXTshmBticMpAFGEiHjhLGl5EYMYF+ym6MhC9LJGybF5gVQUFRaANCqHZPdla7Ni3qPSgLdzKJdYLOepqWXWPYWfKTM8g2tzEJuDXVjAmt2FJyOElIx2iZrT0xpd996yoY5+KimNMwIcn/doCHHNbJOywWg0S1fkrsW2+FrnbQKVzH9AlQTMk3RVpxrTVBGF1BWZkHuuRey6m9V23V5lwxf5hJSA1DLzMxucFBsNvkEozknjO1fJdrLw9yVk8VYz+1F2LtyoakPdCEZ4zgtkqA0bANwDlDnGiTokoy4viiCa5pgIHGEoF055gd3FpNRVuQeicJk6LNaqEuQM+zmnboPqdaaTXQlGd54EttttZRXGq9SUNLGyY515lR5Ttxt0aA6ZtDb+smlAgnK0R4lXieViKdgQj8s29bUUNt3b3aVeSaCDDVzR4Qu7IwbUtSQ1NvnSkOJgrcGdw6XmtVnlHr7gxatCthALFvAedpMVuv9se4yIz5cZxdsLfVQIkSX3DIZvVs7eFG3njNbMKoy+pBxS7wMXITx2Gx6R6TS9qLqbCUO2Euygu3jGovluaPBYy+vPeQaeeulDlGfidyy930ZDl/2OR5GLHNouLZ7n2XrxOeIvyaZDki+V+9O4t43cKBMY9Dy2SLneQekkoTCsY+lSs/cpCgdeCl6gmRqMqr4q/XaBRH0IOgzNr2KhFfDBWAdIR5v2bq0G46kp5beKZgTne8K5cFYWdOVMIdPAyZYSolgZWQiUKSb1brjQeuZnvkrJ/BPcHBFgPBTAll1PNEdAlso3lJ0MpVHFxW0Te1IE7lJyTBjSNTPbXaxB5Dw7RVKE1MPSopJT+NHpEjEU4NlWrH4N0aVgCTLv4CsVAYbvNh4Z1tdab2e9xsIVURsbuOWB66FWCce5iExJvgzn8+MW2vJZbZqjP5P0Hj5Q0NUC75XUe+X2eTX3Jv/S5Bih79VZTlKzL5E6YVbZ7Pdqd65kKvr7Dmc4rgFt4u+Qix4xwfOZLXecX0grfLmgPxHu2Bez47/bv9H0rdNxWJlh5wE72rcvtsXZSeAalgAjaUvokdgewYfQBayEy34vJc5NdtHXn0QIlo+s75I6eRYsSuxWlBTDgVz1oxmhsnghui8zWAeTybTyWcRjUmDdE6/uxAenOCMqAnLtiI3/khULhYCNeVrstfYPQmjfjqk/StwkKbHFNNN12iqHB6pY9p06ih+X0C7s27W9SyHabq5HqppEGHymlpSPcKiHMRPOItsQzgfyobE4+kVPt9PVz9R6IVOEQJ8v9BzFiO847dL1MwmFaC+t3dV+mtlNXRjQEtHWs9tnm8b6ta+aBGGs64WTNczvkrEnZuhxDQ62VbNpS3B9Q8/1A6tyD+zuB94h1XQvc4Ge8Mc01NOTOPpBYvh8sTVM6bbXm14EceHH/KtCD/i++fkI9UBkHWPmaxkEU/DBRt46YSDu9YCrSN2PIApzTAkCaOgYxWPNWvncgbLdPFPQte8xpk/3Pk9b7Hq+e1Y57T1SvJbaq5YBv9K6ihixLlbY2PO0ETAy1OvbnBWBLofoxZBs2l2CjdPmgozPXFH03oBqD8mlJea2KHmFopmLcil5g+yDnRMZ1Ezrw3i4aQK6fbPf+qgxXykkTK8WNbGQg3eUkySfmQpBUYbs4l88Cx5wQqsx0C0vL8YmMjVOctzjnNmy7mhb4Nm1u9mbdjnDXj9cVGVHgxtX4erENXV7dBoPxqKLJF0Q7PV0c4dd/GAsr0JNVYAfIJu9YxypX7btZlvh6i0dO8IQ4UL1MUiA6Sv20KbZFadiagtbUOkBI89aW+YtIJTzeb6PaXLW8zEEtKXJ+FmlbBUHZZ3DwMtSTlDVsVcONnsiRh89nx3aChvKNyarvEfevZ1yjlys27lVHQQxKfo6Xu7cI7kbZjvId0j1oTocx22FtiHqM3l7EXcMBHSXYQowGnUfVxAWobJXi9WPFlYXXtiartvTXSugZQ244RKF8JiW9xfZziPTXuJkNaJQiyx1uGkzxdFlkB0Yy16qQFiyVtx5rRZ7TGtEoAR5wSwelBA5znqdsA2jX3q+dRxfv2gqby6JskfaUzvavzJZNxPmnHUbDDfHCs6NKY3cdK8s5/58zIgjtLSNbgmy6BelqrgOv8pieCkLJI68lx7Q8sEVKFGmH/FtALvOvNDUawnOAnd9gYMxOmUX0g8VLZIH2ld5yUeeZunWa2TcK1OVmy+3tHTHB1zb8su6iAKiTtYV3vhA77IObpYhRgNQBfkCiipXFxjkdm7cIJGPCVHH/RXofCC6FmwpykafXUopiITImxZVz0iEF60SgnpbyCXCKl6WXeCB+GRmDQsa+KFMUX4P5Eqy5GMmyOSbopLzA7hbRyI5YZyW245023YFF2q2A8FjE2ijVPrCRlDF9OSdSm5YgE4amW/JrQ+cQmQgYkp1ZntOtuLCFFaxu0ursuw99pIX4xS583c9njeRrUzTIhDlqXq+UD8NgS8rUzmDpOHId93ClMc6CLHFzsmdUSJSQAurPHcFbaeIK7bQvNcITD0b7FGppO817HjMhQrDoOzO1d4loKx2x9SyjuxnM+QBIggAIIqI/4C9Ix+DqzDIDz1dLfvsbZtFbxeHWUecppy54jedb6oXhxEBXQ2uWU8Wv/dEiYEwuegKpoavBJLOYusUKC7Y7tHgU/XoVyF+ziXqPMYPJgOivoMQTa2bp+Nx+YCcM505WsjSIQcURBbg6QjcD15DZGXT9/yNMukx9FuQAIUYAvFwsMX8NmRkSEuQwtasKGSP1D7iUmKOIlmT2TEdg0aAWOOMJcd7NY6BbLvIyOEqCUOFAnRjaDOeK1PzTHthL83s0IlZZw6NPLZyx6jwHK8WAnsvurzkbID1th9dO+kw97V7sqdY+3QzbdmwbezsCXrj3HYXfoVRr6ohcQyAF+1lAET/uLOElUJmTUfuMcUXlfzAGFa+1JyJRqAvg/ZiA0p6XUbRH70zNwhaJqZHY2CwlXy0uhi4AVqNB3WBFQgd+md5bVFi8HLPch3L4G7pzdIhhemFPGIxwsSu9o1LWDINxZjrIQGSvYFFh9A1eYWsxyWs4nAyKDCJymoH7F426pUheDrFj6wSeqPPb2x86QxNoAy9tRRBhc1iuiM0HQWRqT8hj6ouLrpyA5bs25FPbMbliWELFMvz+jiajlvQGizYsJP1D612wGxrhbI+xucXbSq7TD3OmOAutUTV2eKVIEVtT+DuiEHMUXWMsIOkDzTZg7rPE8/7chcqd9WoWnLwqjIDcyKtc9fuKXWfXjq7w1N1fuFwfbSzO5uGPVmW0rMxDlC5ng1VyWmUK7lgDC1t6Lho7zA1Sl+gt+lxL76uasxHsLsv3oXY1RuYWuUFtPW89KiCOYaxsoVA37yo1DHcl9HNAvwyivHjdFwTF5HsNYgF79Tg3akcUSs42nhkmwLuXl/j8BZkVXFPnMqaYpEIG6oGpTbtKF1XulaIkgojiG2WV8y/KrtfveQecS81AuH1Odkzls05Kajic6ME5SX2TZQMZ3Teu8sCro55nmmBjzDG9nsH3Isze0Wn1+ZEbE0R5xcrHWMK3fW+OnR4z43EWA2Z9xB30Uv3YWbGpfceS4V1U2aFEg5ZEv3ibwEkb6g3LpVJ+90zRuYUWIYN4NntdibKF4jL2RAuL17dQuySoYSbhMVQ1sRTOFhlv7xw3g9D64BVgigBUnc7YbwGW5sSUQxCkU2nqDM98tlsEFjxlXvotgKGXKbRmuj74Ok3EWKdFORs1kWvr4pjwNxBveDFs0AMP+rqpWA25RQOMe6KpGAYVmPu6AmEDzLXx2ZCuK0192sV0/M9SYrp/FDDM2S7U82jal3ebp6SvBJn6BO1d7yzn4pqhNDYea9a/8mEJu/rOoENhCs13XNwn/RlppYgNhVlzOsdrHorYKrtMrDlrVc957XaQKjdEtXuiztRQ+qIyaHiQuTEzfuQYzWoGMSu+AcrmUkMvi/7JU0fomK8LCi8KFNAEAsDHJSz97yIIhzXnxrZZYFhko2otut7LsJpk93OUyKmpTOn6hXu3IuHBclMuAVD2R0eqqsjj0L6DJibvRg5qpK0WlZAz5czseozjWClFAnC7f4gnrOiYSFJgePwPL8Ap8EDoy5XlhzvttabxVUy4dEVMjUIOp3UaTMPdX/njSuj2w7EqiGyCrmXPMtKEz2IveX1vBxppQX6C37cCa8++OyY2PQqP2jCr11dceWs7fAzxqQNYzSRgXCkL6yaH2L4yj4Fj/RVH9F3aNNv/cB0dspKAlMetr5SGd3xOvRj7yyRQKoCZ1PQ11rXANZAO8G+YsmNtEqscEkRP6dycXVKPEHL5XnQ+iQGsB4GECmlVoG2tm4x5toY1RsrwfszAK4yQGteYbEmuUBCOdJeq0J05T9h3pAETTiQSOIeUZRcfVWoY7kugqmmBx6xDXmqsYYPlgW5aI7NRvMouVY7hEI7UOzIvTatVi83erjX3mJh98XHEN5t2pFzqMktUtRqHwx6s8emwUfWc8n8FmnT4FKW0lUyrHcHPYv7R3W0Bk8MuWMkb11ukEeRub1sLpuHqrhRV8nYbOtiX9uHtY3UWUB8MZAhbOV7tLxGWbLtJGG9HimB3LvHpCCgwT4uo8RrL8m9t5V01+yHUWPZg0rdgPcUsLjXTs/WB9+XKZmje5M5Q17QkR2S9845ycKDUEt9SQvBCHN6fX48krMXqujFb26PlUJkOEHCM+CJzVi7BZIduC1UTzkCdJBYS7CqeQp30xnFqvFcxVj27AWE6HOngotBefGdgtRzoGmiulKVfVVQnruoRxq4EsJboSDBA4g1jw2nuRGYdRXzRjIaxU3hL1rmEPeQK/gO8LAsRtwAd0o/GurnWDBJZwmPg30M1nqvBTicblVqVmMSQWItJB7PA3QAC2JTy9eAKVWHzaZqUm/KIOE0jck03pdQF0HFRj47vN4FV9zd9jkPx6RFFmNoloiuPd2KBe3nuQsJRkdUNwcrb876gwSIaW/sEM2/JOzq587TKgaYSjqDkrNHXJAc6Z57CwWEbdLTuELLlcB8F04sEM4RzDYlYl5DKqEYFlQcl8Acz+7hKrqcyxXgK7QH6ZsGR3DOq9lraBPe2TAoDNknnLOqCR2DmqHiZCyHuEddwgAfvEjygARgpr5LMZAQ+wyLh0XemIRz6zPamfaus3QPkdhtOgcod+u4voZFb2W74DWPiYKzVmmLzmSgVErWWCHygUl3D3cuZvFqTOs5wcy1zDsLMqmhd5qDifZWu8KBTinlRor+3Dvm9Ii1Z73vachIR0Xk12f6UBvpdfVSgz1ztnr0CR3g0+cFv96VCelDgKZ1CYAULzuPnTX5XJ25hKws5zAVQ0LaE2uSYs7nwWp3pbxuk0qkn/miGhoxBFIIoS0a47Is5VA75o8CkoL9SN2iINn7AB4gv4m8oeRQere8kcHHgkyHA9UKSTWL2HEUB6pJwz2vkcqh6yi8eo8928BTNK5lX8L1Wlxu9yvVJM/ztiSc1+J3mxMgF6fOPSfNMcgIILQ1Ruw/XzMm0T1KtRnBiatR+Dzf4erqqnFYQRl3mXBYzGpyg3ZFLnXcVZwZVlsYnp2AC7MddsfgHoEvCEsUJ/R5AU8eL+aCvzjNRy7tvgI5ylFqQc5x+yxmQ0cumRFO+QEfQauTQ5JoJPjgxKpCBbiUgB0hsX0QuTlKO0IfByFw1IV0YXALAylaiGmC+HnwpgGDq6OICC1pDD1j9d1yL76kIV4Bm0/MO4dGg3mD/7B714tMWZ7my/1S4Ci5DKstIkt1F8tU3mLnEU11ENbKtbXu/BUqW86mK3kbfI1/sUnYWEKsAHDoicjVLF0h1xTUZUe13oEeziNffgECDzTiXgqA5OQZA9AJbJQsSj0WhQ7yIZp1yG04axMU2xWuaLLCvq1g/AtQ+HXLsCjqiwfeNqs68rpsL3G7jT3t+Mm1Dczz0uTw2fFwfTdM4XF3SgR8ziq0wK6bD53cXBFyvnUgwipu1nqXMbNeTHXtwJi7tmoyKkbP0At5jpXbFbLja8jBF4FKZQWkU1faNt5nQ18vu4az4/3p2G5cGy1WkL2yS0Rmi13XuGdocApSTnNJT2+MaE+S14wZLG9ZH+K+7dq6F97q29p6WpigDGrBikYQOf/oAh1B+/zVmEq71XKpGEmLCri28zqcTTqXIl66mPuKu+79yGZZvASQB9FlM3ezpedOyzK7jT8xkL1cgPMYYbN28Ev4WgkF7mawelvKEIFk+c4bi1LdOMHN0gSQYRQhvQDt6gxyeAa5uim0bu5+A3ijOHLrFV1ZZLkKzQspKDBPUMm+uYwDxF4l0zc+5ADKFRxh9F1vev+rg2O4BHacuSbbBmSpFvvOhm/2jeHPNqdtBzSEYJ4uMNPtOX3fkkc+DZHQAJ1hxfB+yxK1fIYX3HwRibYsWUqsHK7L7dT2WJICCgCwCxAIAUy7nX9Wn7B+KYCFRvU1NHtJoyVR7aB8N84H2k+3GaMe8r0yCYSeHj58wyMtm5H7Y+XHlk+1/Izl19tDtbCUswlreCjno/v543p+PSUGNFHMZ+TpIY/mSEC5oj4rG8fwtqh3r+LuYwGKsksXQ60jftON1UOf3LwrlHsvvcgLrpTLvvJqp6452AH27RhISMIdoFuNx80qLXYQztSBjwK0h2yXjV5FH72yoQI7uweKdRUxBSzP20FIzPnhJlmTgGw99s9XDeeMKJIgA+rEjZsKuVbON5Ik//PLD1/ed9W+3lr6P7jn/r6/8f/bNZLPGx/d830jNMneN2fGLEp//jjr5/8TZf7nD1/GpDpU+bwkM9VL8e1KyZ9dkfnxLfPHP8j88Y9XZD7vvP2adO37QtG3C11zVLz/t44P3xyL/rD5+12n48PyvqS3jtX8ebnpiO1cHGd/uPdtXBXVP74vtlRJNr21/vi/DT4u+kA/wYfu//h/AU96i6zKRAAA -->
