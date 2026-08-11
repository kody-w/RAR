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
