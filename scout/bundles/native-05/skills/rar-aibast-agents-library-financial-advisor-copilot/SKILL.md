---
name: "rar-aibast-agents-library-financial-advisor-copilot"
description: "Reviews advisory client books from a live simulated Dynamics 365 tenant (contacts as clients), with portfolio demos and an offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/financial_advisor_copilot", "rar_sha256": "5c6c283b2e847401d4ab91916ecfebf5cd0bffefbfb47ef3a45eee548511b32c", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["advisor", "portfolio", "investment", "compliance", "financial-services", "branch-banking", "advisory"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/financial_advisor_copilot`. The original RAPP
agent is preserved byte-for-byte in `financial_advisor_copilot_agent.py` and in the RCI capsule.

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

Financial Advisor Copilot Agent — a template you are meant to mutate.

Assists financial advisors with client reviews, portfolio summaries,
investment recommendations, and compliance checks. In this template a CRM
contact is an advisory client — the tenant has no native portfolio entity,
so the client book comes from contacts and balances stay an enrichment
seam until you wire your custodian.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `client_review` operation pulls live
     contact records over real HTTP from the globally hosted Static
     Dynamics 365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="client_review")
     and look for Marcus Webb, the Bluegrass Credit Union contact.
  2. No network? Everything falls back to the embedded demo layer below
     (CLIENT_PORTFOLIOS / COMPLIANCE_RULES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     FINANCIAL_ADVISOR_COPILOT_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your book-of-business
     system), or replace _fetch_collection() with your own client. The
     fields the rest of the file needs are listed in
     _normalize_live_client() — fields rendered "n/a — enrichment seam"
     (assets, age, risk profile) are where you wire your custodian and
     planning platform.

OPERATIONS
  client_review | portfolio_summary | recommendation_engine
  | compliance_check | branch_intake | advisory_education | account_opening
  | financial_planning | advisor_handoff
  kwargs: operation (required), client_id, user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "client_id": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "client_review",
        "portfolio_summary",
        "recommendation_engine",
        "compliance_check",
        "branch_intake",
        "advisory_education",
        "account_opening",
        "financial_planning",
        "advisor_handoff"
      ],
      "type": "string"
    },
    "user_input": {
      "description": "Optional free-text request. Include a record key (e.g. INT4101, EDU529, APP529A, PLN18YR, HOFF7001) for an exact keyed lookup; omit for a summary of all records.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `financial_advisor_copilot_agent.py` and embedded as the fenced Python below (sha256 5c6c283b2e847401…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `financial_advisor_copilot_agent.py` first:

```bash
python3 financial_advisor_copilot_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 financial_advisor_copilot_agent.py   # or on stdin
python3 financial_advisor_copilot_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Financial Advisor Copilot Agent — a template you are meant to mutate.

Assists financial advisors with client reviews, portfolio summaries,
investment recommendations, and compliance checks. In this template a CRM
contact is an advisory client — the tenant has no native portfolio entity,
so the client book comes from contacts and balances stay an enrichment
seam until you wire your custodian.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `client_review` operation pulls live
     contact records over real HTTP from the globally hosted Static
     Dynamics 365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="client_review")
     and look for Marcus Webb, the Bluegrass Credit Union contact.
  2. No network? Everything falls back to the embedded demo layer below
     (CLIENT_PORTFOLIOS / COMPLIANCE_RULES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     FINANCIAL_ADVISOR_COPILOT_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your book-of-business
     system), or replace _fetch_collection() with your own client. The
     fields the rest of the file needs are listed in
     _normalize_live_client() — fields rendered "n/a — enrichment seam"
     (assets, age, risk profile) are where you wire your custodian and
     planning platform.

OPERATIONS
  client_review | portfolio_summary | recommendation_engine
  | compliance_check | branch_intake | advisory_education | account_opening
  | financial_planning | advisor_handoff
  kwargs: operation (required), client_id, user_input
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json as _json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/financial_advisor_copilot",
    "version": "1.2.0",
    "display_name": "Financial Advisor Copilot Agent",
    "description": "Reviews advisory client books from a live simulated Dynamics 365 tenant (contacts as clients), with portfolio demos and an offline fallback.",
    "author": "AIBAST",
    "tags": ["advisor", "portfolio", "investment", "compliance", "financial-services", "branch-banking", "advisory"],
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
#   export FINANCIAL_ADVISOR_COPILOT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM/custodian client. Downstream
# code only needs the fields produced by _normalize_live_client().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "FINANCIAL_ADVISOR_COPILOT_DATA_URL",
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


def _normalize_live_client(row):
    """Project a Dynamics contact onto the client shape this agent uses.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not knowable from the CRM alone' and the
    renderers label it as an enrichment seam."""
    return {
        "name": row.get("fullname", "Unknown"),
        "advisor": row.get("owneridname", ""),
        "household": row.get("parentcustomeridname") or "",
        "risk_profile": None,   # enrichment seam — wire your planning platform
        "age": None,            # enrichment seam
        "total_assets": None,   # enrichment seam — wire your custodian
        "last_review": str(row.get("modifiedon", ""))[:10],
        "_live": True,
    }


def _live_clients():
    """contact-keyed dict of live tenant advisory clients; {} when offline."""
    rows = _fetch_collection("contacts")
    if not rows:
        return {}
    return {
        f"CLI-{str(row.get('contactid', ''))[:8]}": _normalize_live_client(row)
        for row in rows
        if row.get("fullname")
    }


def _seam(value, formatter=str):
    """None = the CRM alone can't know this (enrichment seam)."""
    return "n/a — enrichment seam" if value is None else formatter(value)


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

CLIENT_PORTFOLIOS = {
    "CLI-3001": {
        "name": "Robert & Susan Whitfield",
        "advisor": "James Morrison, CFP",
        "risk_profile": "moderate",
        "age": 58,
        "retirement_target": 67,
        "total_assets": 1850000,
        "holdings": {
            "US Equities": {"value": 555000, "allocation": 30.0, "target": 35.0},
            "International Equities": {"value": 185000, "allocation": 10.0, "target": 15.0},
            "Fixed Income": {"value": 647500, "allocation": 35.0, "target": 30.0},
            "Real Estate (REITs)": {"value": 185000, "allocation": 10.0, "target": 10.0},
            "Alternatives": {"value": 92500, "allocation": 5.0, "target": 5.0},
            "Cash & Equivalents": {"value": 185000, "allocation": 10.0, "target": 5.0},
        },
        "annual_income": 285000,
        "annual_contributions": 45000,
        "last_review": "2024-12-15",
    },
    "CLI-3002": {
        "name": "Angela Martinez",
        "advisor": "James Morrison, CFP",
        "risk_profile": "aggressive",
        "age": 34,
        "retirement_target": 60,
        "total_assets": 420000,
        "holdings": {
            "US Equities": {"value": 210000, "allocation": 50.0, "target": 45.0},
            "International Equities": {"value": 84000, "allocation": 20.0, "target": 20.0},
            "Fixed Income": {"value": 42000, "allocation": 10.0, "target": 10.0},
            "Emerging Markets": {"value": 50400, "allocation": 12.0, "target": 15.0},
            "Alternatives": {"value": 21000, "allocation": 5.0, "target": 5.0},
            "Cash & Equivalents": {"value": 12600, "allocation": 3.0, "target": 5.0},
        },
        "annual_income": 145000,
        "annual_contributions": 24000,
        "last_review": "2025-01-20",
    },
    "CLI-3003": {
        "name": "William Chen Trust",
        "advisor": "Patricia Lane, CFA",
        "risk_profile": "conservative",
        "age": 72,
        "retirement_target": 0,
        "total_assets": 4200000,
        "holdings": {
            "US Equities": {"value": 630000, "allocation": 15.0, "target": 15.0},
            "International Equities": {"value": 210000, "allocation": 5.0, "target": 5.0},
            "Fixed Income": {"value": 1890000, "allocation": 45.0, "target": 45.0},
            "Municipal Bonds": {"value": 840000, "allocation": 20.0, "target": 20.0},
            "Real Estate (REITs)": {"value": 210000, "allocation": 5.0, "target": 5.0},
            "Cash & Equivalents": {"value": 420000, "allocation": 10.0, "target": 10.0},
        },
        "annual_income": 0,
        "annual_contributions": 0,
        "last_review": "2025-02-10",
    },
}

INVESTMENT_RECOMMENDATIONS = {
    "moderate": [
        {"action": "Rebalance to target allocation", "rationale": "Drift from target exceeds 3% in multiple asset classes"},
        {"action": "Reduce cash overweight", "rationale": "Excess cash drag on returns; deploy to equities"},
        {"action": "Increase international exposure", "rationale": "Underweight vs target; diversification benefit"},
    ],
    "aggressive": [
        {"action": "Increase emerging markets allocation", "rationale": "Below target; favorable long-term growth outlook"},
        {"action": "Consider small-cap tilt", "rationale": "Long time horizon supports higher-volatility allocations"},
        {"action": "Build cash reserve to target 5%", "rationale": "Slightly underweight cash for opportunistic rebalancing"},
    ],
    "conservative": [
        {"action": "Maintain current allocation", "rationale": "Portfolio aligned with targets; no rebalancing needed"},
        {"action": "Review bond duration", "rationale": "Consider shortening duration if rate hikes expected"},
        {"action": "Tax-loss harvesting review", "rationale": "Identify unrealized losses for year-end tax planning"},
    ],
}

COMPLIANCE_RULES = {
    "reg_bi": {"name": "Regulation Best Interest", "description": "Ensure recommendations are in client's best interest", "applies_to": "all"},
    "form_crs": {"name": "Form CRS Delivery", "description": "Relationship summary delivered at account opening and annually", "applies_to": "all"},
    "suitability": {"name": "Suitability Obligation", "description": "Investment recommendations suitable for client profile", "applies_to": "all"},
    "concentration_limit": {"name": "Concentration Limit", "description": "No single position exceeds 10% of portfolio", "applies_to": "all"},
    "senior_investor": {"name": "Senior Investor Protection", "description": "Enhanced protections for clients age 65+", "applies_to": "seniors"},
}


# ---------------------------------------------------------------------------
# Branch banking & advisory capabilities (v1.1.0)
#
# Five backward-compatible operations sourced from the
# branch-banking-advisory spec. Each capability carries its spec response,
# knowledge, exactly three synthetic records, an exact lookup key, and
# write/generative metadata. Operations support an optional `user_input`:
# supplying a record key performs an exact keyed lookup; omitting it returns
# a useful no-input summary of all records. Write capabilities emit a
# simulated receipt only — no live system mutation occurs.
# ---------------------------------------------------------------------------

BRANCH_BANKING_CAPABILITIES = {
    "branch_intake": {
        "name": "Branch Intake and Verification",
        "description": "Automates customer intake, identity verification, and service routing to coordinate branch check-in and balance team workloads.",
        "source_system": "Dynamics 365 CRM",
        "write": True,
        "generative": False,
        "key_field": "intake_id",
        "response": "I can check in the customer, confirm identity verification, and route them to the correct specialist.",
        "knowledge": [
            "The Financial Advisor Agent automates check-in, identity verification, and service routing (demo 00:00:45-00:00:49).",
            "Intake coordination improves service speed and balances team workloads for a mid-sized credit union (one-pager, Opportunity).",
            "Identity verification and routing remove slow, multi-system check-in steps that undermined trust and satisfaction (demo 00:00:16-00:00:26).",
        ],
        "records": [
            {"intake_id": "INT4101", "customer": "Marisol Vega", "branch": "Lakeshore Community Credit Union", "service": "Education savings consultation", "verification": "ID verified", "route_to": "Financial Advisor"},
            {"intake_id": "INT4102", "customer": "Darnell Brooks", "branch": "Lakeshore Community Credit Union", "service": "Loan inquiry", "verification": "Pending document", "route_to": "Loan Officer"},
            {"intake_id": "INT4103", "customer": "Priya Nair", "branch": "Riverbend Federal Credit Union", "service": "Account opening", "verification": "ID verified", "route_to": "Branch Banker"},
        ],
    },
    "advisory_education": {
        "name": "Advisory Product Education",
        "description": "Guides customers and bankers through advisory and product education, explaining plan basics, state benefits, contribution rules, and investment structures in plain language.",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": True,
        "key_field": "topic_id",
        "response": "I can explain the plan in plain language, including state benefits, contribution rules, and investment structures so it maps to your family's goals.",
        "knowledge": [
            "The agent walks a customer through 529 plan basics in plain language, state benefits, contribution rules, and investment structures (demo 00:01:08-00:01:16).",
            "Education helps a customer quickly see what matches her family's goals before meeting an advisor (demo 00:01:16-00:01:19).",
            "The credit union used the agent to guide bankers through account opening and investment services (one-pager, How the Agent helped).",
        ],
        "records": [
            {"topic_id": "EDU529", "topic": "529 plan basics", "summary": "Plain-language overview of 529 education savings plans", "state_benefit": "State tax deduction available", "contribution_rule": "Annual gift-tax exclusion applies", "audience": "Families"},
            {"topic_id": "EDUIRA", "topic": "Roth IRA basics", "summary": "Overview of Roth IRA saving and withdrawals", "state_benefit": "Tax-free qualified withdrawals", "contribution_rule": "Annual contribution limit applies", "audience": "Individuals"},
            {"topic_id": "EDUCUST", "topic": "Custodial account basics", "summary": "Overview of UTMA custodial accounts", "state_benefit": "Gift-tax considerations apply", "contribution_rule": "Irrevocable gift to the minor", "audience": "Parents"},
        ],
    },
    "account_opening": {
        "name": "Account Opening and Application",
        "description": "Opens accounts by preparing the application, autofilling information, and completing identity and eligibility checks to remove slow manual steps for the customer and advisor.",
        "source_system": "Dynamics 365 ERP",
        "write": True,
        "generative": False,
        "key_field": "application_id",
        "response": "I can prepare the application, autofill the information from the customer profile, and complete the identity and eligibility checks before submission.",
        "knowledge": [
            "The customer provides her details and asks the agent to open the 529 account (demo 00:01:29-00:01:34).",
            "The agent prepares the application, autofills information, and completes identity and eligibility checks (demo 00:01:35-00:01:42).",
            "Automating these steps removes slow manual steps for both the customer and the advisor (demo 00:01:42-00:01:46).",
        ],
        "records": [
            {"application_id": "APP529A", "customer": "Marisol Vega", "product": "529 education savings account", "autofill": "Completed from profile", "eligibility": "Passed identity and eligibility checks", "status": "Ready to submit"},
            {"application_id": "APP529B", "customer": "Priya Nair", "product": "529 education savings account", "autofill": "Partially completed", "eligibility": "Awaiting SSN confirmation", "status": "On hold"},
            {"application_id": "APPIRAC", "customer": "Darnell Brooks", "product": "Roth IRA account", "autofill": "Completed from profile", "eligibility": "Passed identity checks", "status": "Ready to submit"},
        ],
    },
    "financial_planning": {
        "name": "Financial Planning and Risk Assessment",
        "description": "Models future college costs, explores contribution scenarios, and provides a risk-aligned investment approach and research to support clarity without replacing professional guidance.",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": True,
        "key_field": "scenario_id",
        "response": "I can model future college costs, explore contribution scenarios, and suggest a risk-aligned approach for clarity, without replacing professional guidance.",
        "knowledge": [
            "When she has a planning question, the agent models future college costs and explores contribution scenarios (demo 00:01:46-00:01:54).",
            "With goals and time horizon captured, the agent provides a risk-aligned investment approach to consider, supporting clarity without replacing professional guidance (demo 00:02:01-00:02:10).",
            "The credit union used the agent to provide real-time risk assessments and financial research (one-pager, How the Agent helped).",
        ],
        "records": [
            {"scenario_id": "PLN18YR", "goal": "Fund a 4-year degree in 18 years", "projected_cost": "$180,000 projected", "monthly_contribution": "$450 monthly suggested", "risk_profile": "Moderate risk-aligned mix"},
            {"scenario_id": "PLN10YR", "goal": "Fund college in 10 years", "projected_cost": "$140,000 projected", "monthly_contribution": "$820 monthly suggested", "risk_profile": "Conservative risk-aligned mix"},
            {"scenario_id": "PLN05YR", "goal": "Fund tuition in 5 years", "projected_cost": "$90,000 projected", "monthly_contribution": "$1,300 monthly suggested", "risk_profile": "Low risk-aligned mix"},
        ],
    },
    "advisor_handoff": {
        "name": "Advisor Handoff and Follow-up Scheduling",
        "description": "Schedules a follow-up meeting with a specialist in Microsoft Teams and transfers case notes, risk data, and conversation history so the advisor has full context.",
        "source_system": "Dynamics 365 CRM",
        "write": True,
        "generative": False,
        "key_field": "handoff_id",
        "response": "I can schedule the follow-up meeting with the specialist in Microsoft Teams and transfer the case notes, risk data, and conversation history to the advisor.",
        "knowledge": [
            "To finish up, the agent schedules a follow-up meeting with an educational planning specialist in Microsoft Teams (demo 00:02:10-00:02:17).",
            "The agent passes along the full context to the advisor and helps the customer leave feeling supported and confident about next steps (demo 00:02:17-00:02:24).",
            "The credit union used the agent to transfer case notes, risk data, and conversation history to advisors (one-pager, How the Agent helped).",
        ],
        "records": [
            {"handoff_id": "HOFF7001", "customer": "Marisol Vega", "specialist": "Education Planning Specialist", "meeting": "Microsoft Teams follow-up scheduled", "context": "Case notes and risk data transferred"},
            {"handoff_id": "HOFF7002", "customer": "Darnell Brooks", "specialist": "Lending Specialist", "meeting": "Microsoft Teams follow-up scheduled", "context": "Loan inquiry context transferred"},
            {"handoff_id": "HOFF7003", "customer": "Priya Nair", "specialist": "Retirement Specialist", "meeting": "Microsoft Teams follow-up pending", "context": "Investment profile transferred"},
        ],
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _field_label(field):
    """Human-readable label for a record field name."""
    return field.replace("_", " ").title()


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


def _match_record(capability, user_input):
    """Return the uniquely matched record for a complete normalized key."""
    if not user_input:
        return None
    key_field = capability["key_field"]
    matches = [
        record for record in capability["records"]
        if _contains_normalized_key(user_input, record[key_field])
    ]
    return matches[0] if len(matches) == 1 else None

def _allocation_drift(holdings):
    """Calculate max allocation drift from target."""
    max_drift = 0
    for asset, data in holdings.items():
        drift = abs(data["allocation"] - data["target"])
        if drift > max_drift:
            max_drift = drift
    return round(max_drift, 1)


def _years_to_retirement(client):
    """Calculate years remaining to retirement."""
    if client["retirement_target"] == 0:
        return 0
    return max(0, client["retirement_target"] - client["age"])


def _compliance_flags(client):
    """Check for compliance issues."""
    flags = []
    for asset, data in client["holdings"].items():
        if data["allocation"] > 50:
            flags.append(f"Concentration risk: {asset} at {data['allocation']}%")
    if client["age"] >= 65:
        flags.append("Senior investor protections apply")
    drift = _allocation_drift(client["holdings"])
    if drift > 5:
        flags.append(f"Allocation drift of {drift}% exceeds threshold")
    return flags


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class FinancialAdvisorCopilotAgent(BasicAgent):
    """Financial advisor copilot agent."""

    def __init__(self):
        self.name = "FinancialAdvisorCopilotAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Financial Advisor Copilot Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "client_review",
                            "portfolio_summary",
                            "recommendation_engine",
                            "compliance_check",
                            "branch_intake",
                            "advisory_education",
                            "account_opening",
                            "financial_planning",
                            "advisor_handoff",
                        ],
                    },
                    "client_id": {"type": "string"},
                    "user_input": {
                        "type": "string",
                        "description": "Optional free-text request. Include a record key (e.g. INT4101, EDU529, APP529A, PLN18YR, HOFF7001) for an exact keyed lookup; omit for a summary of all records.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "client_review")
        dispatch = {
            "client_review": self._client_review,
            "portfolio_summary": self._portfolio_summary,
            "recommendation_engine": self._recommendation_engine,
            "compliance_check": self._compliance_check,
        }
        handler = dispatch.get(operation)
        if handler:
            return handler(**kwargs)
        if operation in BRANCH_BANKING_CAPABILITIES:
            return self._branch_capability(**kwargs)
        return f"**Error:** Unknown operation `{operation}`."

    def _client_review(self, **kwargs) -> str:
        live = _live_clients()
        if live:
            lines = ["# Client Review Summary (live tenant)\n"]
            lines.append("| Client | Advisor | Household / Employer | Risk | Assets | Last Review |")
            lines.append("|---|---|---|---|---|---|")
            for cid, c in live.items():
                lines.append(
                    f"| {c['name']} ({cid}) | {c['advisor']} | {c['household'] or '—'} "
                    f"| {_seam(c['risk_profile'], lambda v: v.title())} "
                    f"| {_seam(c['total_assets'], lambda v: f'${v:,.0f}')} | {c['last_review']} |"
                )
            lines.append(f"\n**Clients:** {len(live)}")
            lines.append("**Total AUM:** n/a — enrichment seam (wire your custodian)")
            lines.append(
                "\n_Source: live Static Dynamics 365 tenant — CRM contacts "
                "reinterpreted as advisory clients. Risk, age, and assets are "
                "enrichment seams._"
            )
            return "\n".join(lines)

        lines = ["# Client Review Summary\n"]
        lines.append("| Client | Advisor | Risk | Assets | Age | Retirement In | Last Review |")
        lines.append("|---|---|---|---|---|---|---|")
        for cid, c in CLIENT_PORTFOLIOS.items():
            yrs = _years_to_retirement(c)
            ret_str = f"{yrs} yrs" if yrs > 0 else "Retired"
            lines.append(
                f"| {c['name']} ({cid}) | {c['advisor']} | {c['risk_profile'].title()} "
                f"| ${c['total_assets']:,.0f} | {c['age']} | {ret_str} | {c['last_review']} |"
            )
        total_aum = sum(c["total_assets"] for c in CLIENT_PORTFOLIOS.values())
        lines.append(f"\n**Total AUM:** ${total_aum:,.0f}")
        lines.append(f"**Clients:** {len(CLIENT_PORTFOLIOS)}")
        lines.append("\n_Source: embedded demo layer (offline fallback)._")
        return "\n".join(lines)

    def _portfolio_summary(self, **kwargs) -> str:
        client_id = kwargs.get("client_id", "CLI-3001")
        client = CLIENT_PORTFOLIOS.get(client_id, list(CLIENT_PORTFOLIOS.values())[0])
        drift = _allocation_drift(client["holdings"])
        lines = [f"# Portfolio Summary: {client['name']}\n"]
        lines.append(f"- **Risk Profile:** {client['risk_profile'].title()}")
        lines.append(f"- **Total Assets:** ${client['total_assets']:,.0f}")
        lines.append(f"- **Annual Contributions:** ${client['annual_contributions']:,.0f}")
        lines.append(f"- **Max Allocation Drift:** {drift}%\n")
        lines.append("## Holdings\n")
        lines.append("| Asset Class | Value | Current % | Target % | Drift |")
        lines.append("|---|---|---|---|---|")
        for asset, data in client["holdings"].items():
            d = round(data["allocation"] - data["target"], 1)
            sign = "+" if d > 0 else ""
            lines.append(
                f"| {asset} | ${data['value']:,.0f} | {data['allocation']}% "
                f"| {data['target']}% | {sign}{d}% |"
            )
        return "\n".join(lines)

    def _recommendation_engine(self, **kwargs) -> str:
        client_id = kwargs.get("client_id", "CLI-3001")
        client = CLIENT_PORTFOLIOS.get(client_id, list(CLIENT_PORTFOLIOS.values())[0])
        recs = INVESTMENT_RECOMMENDATIONS.get(client["risk_profile"], [])
        lines = [f"# Investment Recommendations: {client['name']}\n"]
        lines.append(f"**Risk Profile:** {client['risk_profile'].title()}")
        lines.append(f"**Years to Retirement:** {_years_to_retirement(client) or 'Retired'}\n")
        lines.append("## Recommendations\n")
        for i, rec in enumerate(recs, 1):
            lines.append(f"### {i}. {rec['action']}\n")
            lines.append(f"**Rationale:** {rec['rationale']}\n")
        lines.append("## Rebalancing Trades\n")
        lines.append("| Asset Class | Current | Target | Action | Est. Amount |")
        lines.append("|---|---|---|---|---|")
        for asset, data in client["holdings"].items():
            diff_pct = data["target"] - data["allocation"]
            if abs(diff_pct) >= 1.0:
                amount = abs(diff_pct / 100 * client["total_assets"])
                action = "Buy" if diff_pct > 0 else "Sell"
                lines.append(f"| {asset} | {data['allocation']}% | {data['target']}% | {action} | ${amount:,.0f} |")
        return "\n".join(lines)

    def _compliance_check(self, **kwargs) -> str:
        lines = ["# Compliance Check Report\n"]
        lines.append("## Regulatory Requirements\n")
        lines.append("| Rule | Description | Applies To |")
        lines.append("|---|---|---|")
        for rule_id, rule in COMPLIANCE_RULES.items():
            lines.append(f"| {rule['name']} | {rule['description']} | {rule['applies_to'].title()} |")
        lines.append("\n## Client Compliance Status\n")
        for cid, c in CLIENT_PORTFOLIOS.items():
            flags = _compliance_flags(c)
            status = "Issues Found" if flags else "Compliant"
            lines.append(f"### {c['name']} ({cid}) — {status}\n")
            if flags:
                for f in flags:
                    lines.append(f"- **Flag:** {f}")
            else:
                lines.append("- No compliance issues detected")
            lines.append("")
        return "\n".join(lines)

    # -- Branch banking & advisory operations (v1.1.0) --------------------

    def _branch_capability(self, **kwargs) -> str:
        operation = kwargs.get("operation")
        capability = BRANCH_BANKING_CAPABILITIES[operation]
        user_input = (kwargs.get("user_input") or "").strip()
        record = _match_record(capability, user_input)
        if record is not None:
            return self._capability_detail(capability, record)
        if user_input:
            return (
                f"# {capability['name']}\n\n"
                f"No exact normalized `{capability['key_field']}` matched the request."
            )
        return self._capability_summary(capability)

    def _metadata_block(self, capability) -> str:
        return (
            f"**Source System:** {capability['source_system']}  |  "
            f"**Write:** {'Yes' if capability['write'] else 'No'}  |  "
            f"**Generative:** {'Yes' if capability['generative'] else 'No'}"
        )

    def _knowledge_block(self, capability) -> list:
        lines = ["## Knowledge\n"]
        for item in capability["knowledge"]:
            lines.append(f"- {item}")
        return lines

    def _write_receipt(self, capability, record) -> str:
        key = record[capability["key_field"]]
        return "\n".join([
            "## Simulated Write Receipt\n",
            f"- **Receipt ID:** SIM-{key}",
            f"- **Target System:** {capability['source_system']}",
            f"- **Reference Key:** {key}",
            "- **Status:** Simulated — no live system mutation performed",
        ])

    def _capability_detail(self, capability, record) -> str:
        key_field = capability["key_field"]
        lines = [f"# {capability['name']}\n"]
        lines.append(capability["response"] + "\n")
        lines.append(f"## Record: {record[key_field]}\n")
        for field, value in record.items():
            lines.append(f"- **{_field_label(field)}:** {value}")
        lines.append("")
        lines.append(self._metadata_block(capability))
        lines.append("")
        lines.extend(self._knowledge_block(capability))
        if capability["write"]:
            lines.append("")
            lines.append(self._write_receipt(capability, record))
        return "\n".join(lines)

    def _capability_summary(self, capability) -> str:
        records = capability["records"]
        key_field = capability["key_field"]
        lines = [f"# {capability['name']}\n"]
        lines.append(capability["response"] + "\n")
        lines.append(f"_No record key supplied — showing all {len(records)} records._\n")
        headers = list(records[0].keys())
        lines.append("| " + " | ".join(_field_label(h) for h in headers) + " |")
        lines.append("|" + "---|" * len(headers))
        for record in records:
            lines.append("| " + " | ".join(str(record[h]) for h in headers) + " |")
        lines.append("")
        lines.append(self._metadata_block(capability))
        lines.append("")
        lines.extend(self._knowledge_block(capability))
        lines.append("")
        if capability["write"]:
            lines.append(
                f"_Provide a {_field_label(key_field)} to generate a simulated write "
                f"receipt (no live mutation)._"
            )
        else:
            lines.append(
                f"_Provide a {_field_label(key_field)} for an exact keyed lookup of a single record._"
            )
        return "\n".join(lines)

if __name__ == "__main__":
    agent = FinancialAdvisorCopilotAgent()
    print("=" * 80)
    print("LIVE TENANT CLIENT BOOK (contacts fetched over HTTP; falls back offline)")
    print(agent.perform(operation="client_review"))
    print("\n" + "=" * 80 + "\n")
    print("EMBEDDED DEMO PORTFOLIO (works offline)")
    print(agent.perform(operation="portfolio_summary", client_id="CLI-3001"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="recommendation_engine", client_id="CLI-3002"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="compliance_check"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="branch_intake", user_input="Check in intake INT4101 and route the customer"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="advisory_education", user_input="Explain topic EDU529 for a family"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="account_opening", user_input="Open the account for application APP529A"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="financial_planning", user_input="Model scenario PLN18YR"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="advisor_handoff"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
