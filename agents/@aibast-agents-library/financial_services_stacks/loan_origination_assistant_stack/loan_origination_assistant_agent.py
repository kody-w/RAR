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
