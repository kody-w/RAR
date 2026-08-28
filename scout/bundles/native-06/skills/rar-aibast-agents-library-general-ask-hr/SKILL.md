---
name: "rar-aibast-agents-library-general-ask-hr"
description: "Answers HR policy, leave, and directory queries from a live simulated HRIS (workers, time off, benefits) joined to a D365 CRM, with offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/general_ask_hr", "rar_sha256": "282fc9a22522b758241ccc3bada4f76bb7f968e49ff3a54101325a4066e84faa", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.2.0", "author": "AIBAST", "tags": ["hr", "policy", "benefits", "leave", "directory", "general"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/general_ask_hr`. The original RAPP
agent is preserved byte-for-byte in `ask_hr_agent.py` and in the RCI capsule.

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

General Ask HR Agent — a template you are meant to mutate.

General-purpose HR assistant for policy lookups, benefits inquiries,
leave requests, and employee directory searches. In this template the
employee directory is backed by Dynamics 365 system users — the tenant
has no native HRIS entity, so the CRM user roster stands in for the org
directory (leave balances and benefits stay embedded demos).

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted systems (synthetic data, no credentials, works
     from anywhere):
       CRM  https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       HRIS https://kody-w.github.io/static-hris/api/v1/
     The HRIS is the real system of record: 25 workers (AL-00xx) with
     manager chains and levels, time-off requests with team-conflict
     detection, benefits enrollments from the Nov 3-17 2025 open
     enrollment, and compensation bands. The CRM joins in where the
     story connects (the open-enrollment backlog traces to CRM case
     CAS-260137 "benefits portal login failures").
     Try: perform(operation="leave_request", employee_name="Jamie Ortiz")
     to catch the live scheduling conflict — Jamie's pending TOR-1006
     overlaps Riley Chen's approved TOR-1005 on the same team.
  2. No network? Everything falls back to the embedded demo layer below
     (_POLICIES / _LEAVE_BALANCES / _ORG_DIRECTORY) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set ASK_HR_DATA_URL
     (CRM) and GENERAL_ASK_HR_HRIS_URL (HRIS) to your own endpoints, or
     replace _fetch_collection() with your clients. The fields the rest
     of the file needs are listed in _normalize_live_employee() /
     _normalize_hris_worker(). Per-worker salary deliberately does NOT
     exist in the HRIS — compensation answers come from bands only;
     individual pay is an enrichment seam (wire your payroll system).

OPERATIONS
  policy_lookup | benefits_inquiry | leave_request | employee_directory
  kwargs: operation (required), employee_name, policy_name

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "employee_name": {
      "description": "Employee name or ID for context",
      "type": "string"
    },
    "operation": {
      "description": "The HR operation to perform",
      "enum": [
        "policy_lookup",
        "benefits_inquiry",
        "leave_request",
        "employee_directory"
      ],
      "type": "string"
    },
    "policy_name": {
      "description": "Policy key to look up (e.g. 'remote_work', 'pto')",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ask_hr_agent.py` and embedded as the fenced Python below (sha256 282fc9a22522b758…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ask_hr_agent.py` first:

```bash
python3 ask_hr_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ask_hr_agent.py   # or on stdin
python3 ask_hr_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
General Ask HR Agent — a template you are meant to mutate.

General-purpose HR assistant for policy lookups, benefits inquiries,
leave requests, and employee directory searches. In this template the
employee directory is backed by Dynamics 365 system users — the tenant
has no native HRIS entity, so the CRM user roster stands in for the org
directory (leave balances and benefits stay embedded demos).

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted systems (synthetic data, no credentials, works
     from anywhere):
       CRM  https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       HRIS https://kody-w.github.io/static-hris/api/v1/
     The HRIS is the real system of record: 25 workers (AL-00xx) with
     manager chains and levels, time-off requests with team-conflict
     detection, benefits enrollments from the Nov 3-17 2025 open
     enrollment, and compensation bands. The CRM joins in where the
     story connects (the open-enrollment backlog traces to CRM case
     CAS-260137 "benefits portal login failures").
     Try: perform(operation="leave_request", employee_name="Jamie Ortiz")
     to catch the live scheduling conflict — Jamie's pending TOR-1006
     overlaps Riley Chen's approved TOR-1005 on the same team.
  2. No network? Everything falls back to the embedded demo layer below
     (_POLICIES / _LEAVE_BALANCES / _ORG_DIRECTORY) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set ASK_HR_DATA_URL
     (CRM) and GENERAL_ASK_HR_HRIS_URL (HRIS) to your own endpoints, or
     replace _fetch_collection() with your clients. The fields the rest
     of the file needs are listed in _normalize_live_employee() /
     _normalize_hris_worker(). Per-worker salary deliberately does NOT
     exist in the HRIS — compensation answers come from bands only;
     individual pay is an enrichment seam (wire your payroll system).

OPERATIONS
  policy_lookup | benefits_inquiry | leave_request | employee_directory
  kwargs: operation (required), employee_name, policy_name
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
    "name": "@aibast-agents-library/general_ask_hr",
    "version": "1.2.0",
    "display_name": "General Ask HR",
    "description": "Answers HR policy, leave, and directory queries from a live simulated HRIS (workers, time off, benefits) joined to a D365 CRM, with offline fallback.",
    "author": "AIBAST",
    "tags": ["hr", "policy", "benefits", "leave", "directory", "general"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# LIVE DATA SEAM — swap this for your real system
#
# TWO live sources, both synthetic OData-shaped JSON on GitHub Pages:
#   CRM  (Dynamics 365):  export ASK_HR_DATA_URL=...
#   HRIS (system of record for workers, time off, benefits, bands):
#         export GENERAL_ASK_HR_HRIS_URL=...
# or replace _fetch_collection() with your clients. Downstream code
# only needs the fields produced by _normalize_live_employee() and
# _normalize_hris_worker().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "ASK_HR_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
HRIS_SOURCE_URL = os.environ.get(
    "GENERAL_ASK_HR_HRIS_URL",
    "https://kody-w.github.io/static-hris/api/v1",
)
_LIVE_CACHE = {}


def _fetch_collection(collection, timeout=6, base_url=None):
    """One bounded GET per URL per process. Returns [] on ANY
    failure — offline, DNS, bad JSON — so the demo layer takes over."""
    url = f"{base_url or DATA_SOURCE_URL}/{collection}.json"
    if url in _LIVE_CACHE:
        return _LIVE_CACHE[url]
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "rapp-agent-template/1.0"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            rows = _json.loads(resp.read().decode("utf-8")).get("value", [])
    except Exception:
        rows = []
    _LIVE_CACHE[url] = rows
    return rows


def _fetch_hris(collection):
    """Fetch a collection from the sibling HRIS; [] when offline."""
    return _fetch_collection(collection, base_url=HRIS_SOURCE_URL)


def _normalize_live_employee(row):
    """Project a Dynamics system user onto the directory shape this agent
    uses. THIS is the contract your replacement data source must meet —
    a dict with these keys. None means 'not knowable from the CRM alone'
    and the renderers label it as an enrichment seam."""
    return {
        "id": f"emp-{str(row.get('systemuserid', ''))[:8]}",
        "name": row.get("fullname", "Unknown"),
        "title": row.get("title", ""),
        "department": row.get("businessunitidname", ""),
        "location": None,  # enrichment seam — wire your HRIS
        "manager": None,   # enrichment seam — wire your HRIS org chart
        "phone": None,     # enrichment seam
        "email": row.get("internalemailaddress", ""),
        "_live": True,
    }


def _live_directory():
    """List of live tenant employees (system users); [] when offline."""
    rows = _fetch_collection("systemusers")
    return [
        _normalize_live_employee(row)
        for row in rows
        if row.get("fullname") and not row.get("isdisabled")
    ]


def _normalize_hris_worker(row):
    """Project an HRIS worker onto the directory shape this agent uses.
    Unlike the CRM projection, the HRIS is a real system of record —
    location, manager, and phone are actual fields, not seams."""
    return {
        "id": row.get("worker_id", ""),
        "name": row.get("full_name", "Unknown"),
        "title": row.get("job_title", ""),
        "department": row.get("department_name", ""),
        "location": row.get("work_location") or None,
        "manager": row.get("manager_name") or None,
        "phone": row.get("work_phone") or None,
        "email": row.get("work_email", ""),
        "level": row.get("level", ""),
        "hire_date": row.get("hire_date", ""),
        "_live": True,
    }


def _hris_directory():
    """List of live HRIS workers (the org's system of record); []
    when offline."""
    return [
        _normalize_hris_worker(row)
        for row in _fetch_hris("workers")
        if row.get("full_name") and row.get("status") == "active"
    ]


def _tor_dates(req):
    return f"{req.get('start_date', '?')} to {req.get('end_date', '?')}"


def _seam(value):
    """None = the CRM alone can't know this (enrichment seam)."""
    return "n/a — enrichment seam" if value is None else str(value)


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_POLICIES = {
    "remote_work": {
        "title": "Remote Work Policy",
        "effective_date": "2025-01-15",
        "summary": "Employees may work remotely up to 3 days per week with manager approval.",
        "details": [
            "Eligible after 90-day probation period",
            "Core hours: 10 AM - 3 PM local time zone",
            "Home office stipend: $750 one-time for equipment",
            "Internet reimbursement: $50/month",
            "Must maintain secure VPN connection",
            "Quarterly in-office week required for all remote staff",
        ],
        "approver": "Direct Manager",
        "category": "Workplace Flexibility",
    },
    "pto": {
        "title": "Paid Time Off Policy",
        "effective_date": "2025-01-01",
        "summary": "PTO accrual based on tenure: 15 days (0-2 yr), 20 days (3-5 yr), 25 days (6+ yr).",
        "details": [
            "Accrual begins on first day of employment",
            "Maximum carryover: 5 days per calendar year",
            "Requests of 5+ consecutive days require 2 weeks notice",
            "Holiday blackout: Dec 20 - Jan 2 requires VP approval",
            "Unused PTO above carryover limit forfeited Dec 31",
            "Payout of accrued PTO upon separation",
        ],
        "approver": "Direct Manager",
        "category": "Time Off",
    },
    "expense_reimbursement": {
        "title": "Expense Reimbursement Policy",
        "effective_date": "2025-03-01",
        "summary": "Business expenses reimbursed within 30 days of submission with valid receipts.",
        "details": [
            "Submit via Concur within 60 days of expense",
            "Meals: $75/day domestic, $100/day international",
            "Flights: Economy class for trips under 6 hours",
            "Hotel: Up to $250/night domestic, $350/night international",
            "Manager approval for expenses over $500",
            "VP approval for expenses over $2,500",
        ],
        "approver": "Direct Manager / VP (over $2,500)",
        "category": "Finance",
    },
    "code_of_conduct": {
        "title": "Code of Conduct",
        "effective_date": "2024-06-01",
        "summary": "Standards of professional behavior, ethics, and compliance for all employees.",
        "details": [
            "Annual acknowledgment required by all employees",
            "Conflicts of interest must be disclosed to HR",
            "Gifts from vendors limited to $100 value",
            "Confidential information protected under NDA",
            "Harassment-free workplace with zero tolerance policy",
            "Report violations via ethics hotline or HR portal",
        ],
        "approver": "HR Department",
        "category": "Compliance",
    },
}

_BENEFIT_PLANS = {
    "medical_ppo": {
        "name": "Medical PPO Plan", "type": "Medical",
        "monthly_premium_employee": 185, "monthly_premium_family": 520,
        "deductible_individual": 500, "deductible_family": 1500,
        "oop_max_individual": 3500, "oop_max_family": 7000,
        "copay_primary": 25, "copay_specialist": 50,
        "network": "Blue Cross Blue Shield National",
    },
    "medical_hdhp": {
        "name": "High Deductible Health Plan", "type": "Medical",
        "monthly_premium_employee": 95, "monthly_premium_family": 310,
        "deductible_individual": 1600, "deductible_family": 3200,
        "oop_max_individual": 5000, "oop_max_family": 10000,
        "copay_primary": 0, "copay_specialist": 0,
        "network": "Blue Cross Blue Shield National",
        "hsa_employer_contribution": 750,
    },
    "dental": {
        "name": "Dental Plan", "type": "Dental",
        "monthly_premium_employee": 28, "monthly_premium_family": 85,
        "annual_max": 2000, "deductible": 50,
        "preventive_coverage": "100%", "basic_coverage": "80%",
        "major_coverage": "50%", "orthodontia_lifetime_max": 1500,
    },
    "vision": {
        "name": "Vision Plan", "type": "Vision",
        "monthly_premium_employee": 12, "monthly_premium_family": 35,
        "exam_copay": 10, "frames_allowance": 200,
        "contacts_allowance": 150, "frequency": "Every 12 months",
    },
    "retirement_401k": {
        "name": "401(k) Retirement Plan", "type": "Retirement",
        "employer_match": "100% of first 4%, 50% of next 2%",
        "max_match_percent": 5,
        "vesting_schedule": "3-year graded (33%/66%/100%)",
        "contribution_limit_2025": 23500,
        "catch_up_over_50": 7500,
    },
}

_LEAVE_BALANCES = {
    "emp-2001": {
        "employee_id": "emp-2001", "name": "Angela Martinez",
        "department": "Marketing", "hire_date": "2022-05-16",
        "vacation": 14.5, "sick": 7.0, "personal": 2.0,
        "accrual_rate_days_per_month": 1.67,
        "pending_requests": [
            {"dates": "Dec 23-27, 2025", "days": 3, "status": "Approved"},
        ],
    },
    "emp-2002": {
        "employee_id": "emp-2002", "name": "Brian Nguyen",
        "department": "Engineering", "hire_date": "2024-01-08",
        "vacation": 8.25, "sick": 5.0, "personal": 1.0,
        "accrual_rate_days_per_month": 1.25,
        "pending_requests": [],
    },
    "emp-2003": {
        "employee_id": "emp-2003", "name": "Carla Dubois",
        "department": "Finance", "hire_date": "2019-09-01",
        "vacation": 22.0, "sick": 10.0, "personal": 3.0,
        "accrual_rate_days_per_month": 2.08,
        "pending_requests": [
            {"dates": "Nov 25-29, 2025", "days": 5, "status": "Pending"},
        ],
    },
}

_ORG_DIRECTORY = [
    {"id": "emp-2001", "name": "Angela Martinez", "title": "Marketing Manager", "department": "Marketing", "location": "Austin, TX", "manager": "VP Marketing - Rachel Chen", "phone": "512-555-0147", "email": "angela.martinez@contoso.com"},
    {"id": "emp-2002", "name": "Brian Nguyen", "title": "Software Engineer II", "department": "Engineering", "location": "Seattle, WA", "manager": "Eng Director - Sam Patel", "phone": "206-555-0293", "email": "brian.nguyen@contoso.com"},
    {"id": "emp-2003", "name": "Carla Dubois", "title": "Senior Financial Analyst", "department": "Finance", "location": "New York, NY", "manager": "CFO - David Kim", "phone": "212-555-0381", "email": "carla.dubois@contoso.com"},
    {"id": "emp-2004", "name": "Derek Washington", "title": "HR Business Partner", "department": "Human Resources", "location": "Chicago, IL", "manager": "CHRO - Lisa Park", "phone": "312-555-0462", "email": "derek.washington@contoso.com"},
    {"id": "emp-2005", "name": "Elena Kowalski", "title": "Sales Director", "department": "Sales", "location": "Boston, MA", "manager": "CRO - James Mitchell", "phone": "617-555-0518", "email": "elena.kowalski@contoso.com"},
    {"id": "emp-2006", "name": "Frank O'Brien", "title": "IT Systems Administrator", "department": "IT", "location": "Denver, CO", "manager": "CTO - Maria Santos", "phone": "303-555-0674", "email": "frank.obrien@contoso.com"},
]


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _resolve_employee(query):
    if not query:
        return "emp-2001"
    q = query.lower().strip()
    for emp in _ORG_DIRECTORY:
        if q in emp["name"].lower() or q == emp["id"]:
            return emp["id"]
    return "emp-2001"


def _find_directory_entry(emp_id):
    for entry in _ORG_DIRECTORY:
        if entry["id"] == emp_id:
            return entry
    return _ORG_DIRECTORY[0]


def _calculate_annual_benefits_value(plan_key="medical_ppo"):
    med = _BENEFIT_PLANS[plan_key]
    dental = _BENEFIT_PLANS["dental"]
    vision = _BENEFIT_PLANS["vision"]
    ret = _BENEFIT_PLANS["retirement_401k"]
    employer_medical = med["monthly_premium_employee"] * 12 * 0.75
    employer_dental = dental["monthly_premium_employee"] * 12 * 0.80
    employer_vision = vision["monthly_premium_employee"] * 12 * 1.0
    employer_401k = 100000 * ret["max_match_percent"] / 100
    return {
        "medical": employer_medical,
        "dental": employer_dental,
        "vision": employer_vision,
        "retirement_match": employer_401k,
        "total": employer_medical + employer_dental + employer_vision + employer_401k,
    }


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class GeneralAskHRAgent(BasicAgent):
    """
    General-purpose HR assistant.

    Operations:
        policy_lookup       - search and display company policies
        benefits_inquiry    - show benefit plan details and comparisons
        leave_request       - check leave balances and submit requests
        employee_directory  - search the organizational directory
    """

    def __init__(self):
        self.name = "GeneralAskHRAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "policy_lookup", "benefits_inquiry",
                            "leave_request", "employee_directory",
                        ],
                        "description": "The HR operation to perform",
                    },
                    "employee_name": {
                        "type": "string",
                        "description": "Employee name or ID for context",
                    },
                    "policy_name": {
                        "type": "string",
                        "description": "Policy key to look up (e.g. 'remote_work', 'pto')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "policy_lookup")
        dispatch = {
            "policy_lookup": self._policy_lookup,
            "benefits_inquiry": self._benefits_inquiry,
            "leave_request": self._leave_request,
            "employee_directory": self._employee_directory,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(kwargs)

    # ── policy_lookup ──────────────────────────────────────────
    def _policy_lookup(self, params):
        policy_key = params.get("policy_name", "")
        if policy_key and policy_key in _POLICIES:
            pol = _POLICIES[policy_key]
            details = "\n".join(f"- {d}" for d in pol["details"])
            return (
                f"**{pol['title']}**\n\n"
                f"**Effective:** {pol['effective_date']} | **Category:** {pol['category']}\n\n"
                f"**Summary:** {pol['summary']}\n\n"
                f"**Details:**\n{details}\n\n"
                f"**Approver:** {pol['approver']}\n\n"
                f"Source: [HR Policy Portal]\nAgents: GeneralAskHRAgent"
            )
        rows = ""
        for key, pol in _POLICIES.items():
            rows += f"| {key} | {pol['title']} | {pol['category']} | {pol['effective_date']} |\n"
        return (
            f"**Company Policy Directory**\n\n"
            f"| Policy Key | Title | Category | Effective Date |\n|---|---|---|---|\n"
            f"{rows}\n"
            f"Specify a `policy_name` parameter to view full details.\n\n"
            f"Source: [HR Policy Portal]\nAgents: GeneralAskHRAgent"
        )

    # ── benefits_inquiry ───────────────────────────────────────
    def _live_benefits_section(self):
        """Live HRIS open-enrollment activity + compensation bands, with
        the CRM join where the story connects. '' when offline."""
        enrollments = _fetch_hris("benefits_enrollments")
        bands = _fetch_hris("compensation_bands")
        if not enrollments and not bands:
            return ""
        out = ""
        oe = [e for e in enrollments if e.get("open_enrollment_window")]
        if oe:
            rows = ""
            for e in sorted(oe, key=lambda x: x.get("enrolled_on", "")):
                rows += (
                    f"| {e.get('enrollment_number')} | {e.get('worker_name')} "
                    f"({e.get('worker_id')}) | {e.get('plan_name')} "
                    f"| {e.get('coverage_level', '').replace('_', ' ')} "
                    f"| {str(e.get('enrolled_on', ''))[:10]} "
                    f"| {e.get('status')} |\n"
                )
            out += (
                f"**Open Enrollment Activity (live HRIS — Nov 3-17, 2025 window):**\n\n"
                f"| Enrollment | Worker | Plan | Coverage | Enrolled | Status |\n"
                f"|---|---|---|---|---|---|\n"
                f"{rows}\n"
            )
            portal_case = next(
                (c for c in _fetch_collection("incidents")
                 if "benefits portal" in str(c.get("title", "")).lower()),
                None,
            )
            if portal_case:
                state = "resolved" if portal_case.get("statecode") == 1 else "open"
                out += (
                    f"**CRM join:** the {len(oe)} pending confirmations above trace "
                    f"to case {portal_case.get('ticketnumber')} "
                    f"\"{portal_case.get('title')}\" "
                    f"({portal_case.get('customeridname')}, {state} "
                    f"{str(portal_case.get('resolvedon') or portal_case.get('createdon', ''))[:10]}) "
                    f"— the benefits portal outage the service desk worked.\n\n"
                )
        if bands:
            band_rows = ""
            for b in bands:
                band_rows += (
                    f"| {b.get('level')} | {b.get('name')} "
                    f"| ${b.get('min_annual', 0):,} | ${b.get('mid_annual', 0):,} "
                    f"| ${b.get('max_annual', 0):,} | {b.get('workers_in_band', '')} |\n"
                )
            out += (
                f"**Compensation Bands (live HRIS):**\n\n"
                f"| Level | Band | Min | Mid | Max | Workers |\n"
                f"|---|---|---|---|---|---|\n"
                f"{band_rows}\n"
                f"Compensation questions are answered from band ranges ONLY — "
                f"per-worker salary does not exist in this HRIS and is an "
                f"enrichment seam (wire your payroll system).\n\n"
            )
        return out

    def _benefits_inquiry(self, params):
        med_rows = ""
        for key in ["medical_ppo", "medical_hdhp"]:
            p = _BENEFIT_PLANS[key]
            med_rows += (
                f"| {p['name']} | ${p['monthly_premium_employee']}/mo | "
                f"${p['deductible_individual']:,} | ${p['oop_max_individual']:,} | "
                f"${p['copay_primary']}/{p['copay_specialist']} |\n"
            )
        dental = _BENEFIT_PLANS["dental"]
        vision = _BENEFIT_PLANS["vision"]
        ret = _BENEFIT_PLANS["retirement_401k"]
        val = _calculate_annual_benefits_value()
        live_section = self._live_benefits_section()
        source = (
            "Benefits Portal + Insurance Carriers + Live Static HRIS"
            if live_section else "Benefits Portal + Insurance Carriers"
        )
        return (
            f"**Benefits Overview**\n\n"
            f"**Medical Plans:**\n\n"
            f"| Plan | Employee Premium | Deductible | OOP Max | Copay (PCP/Spec) |\n|---|---|---|---|---|\n"
            f"{med_rows}\n"
            f"**Dental:** {dental['name']} - ${dental['monthly_premium_employee']}/mo | "
            f"Preventive: {dental['preventive_coverage']} | Basic: {dental['basic_coverage']} | Major: {dental['major_coverage']}\n\n"
            f"**Vision:** {vision['name']} - ${vision['monthly_premium_employee']}/mo | "
            f"Exam: ${vision['exam_copay']} copay | Frames: ${vision['frames_allowance']} allowance\n\n"
            f"**Retirement:** {ret['name']}\n"
            f"- Employer match: {ret['employer_match']}\n"
            f"- Vesting: {ret['vesting_schedule']}\n"
            f"- 2025 contribution limit: ${ret['contribution_limit_2025']:,}\n\n"
            f"**Estimated Employer Contribution Value:**\n"
            f"- Medical: ${val['medical']:,.0f}/yr | Dental: ${val['dental']:,.0f}/yr | "
            f"Vision: ${val['vision']:,.0f}/yr | 401(k) Match: ${val['retirement_match']:,.0f}/yr\n"
            f"- **Total: ${val['total']:,.0f}/yr**\n\n"
            + live_section +
            f"Source: [{source}]\nAgents: GeneralAskHRAgent"
        )

    # ── leave_request ──────────────────────────────────────────
    def _live_leave_request(self, query):
        """Render a live HRIS time-off view for a real worker, including
        team-conflict detection. Returns None when offline or when the
        name is not an HRIS worker (embedded demo takes over)."""
        q = (query or "").lower().strip()
        if not q:
            return None
        workers = _hris_directory()
        tors = _fetch_hris("time_off_requests")
        if not workers or not tors:
            return None
        worker = next((w for w in workers if q in w["name"].lower()
                       or q == w["id"].lower()), None)
        if not worker:
            return None
        mine = [t for t in tors if t.get("worker_id") == worker["id"]]
        tor_by_number = {t.get("request_number"): t for t in tors}
        rows = ""
        for t in sorted(mine, key=lambda x: x.get("start_date", "")):
            flag = "CONFLICT" if t.get("team_conflict") else "-"
            rows += (
                f"| {t.get('request_number')} | {t.get('type', '')} "
                f"| {_tor_dates(t)} | {t.get('days', '')} "
                f"| {t.get('status', '')} | {flag} |\n"
            )
        if not rows:
            rows = "| None on record | - | - | - | - | - |\n"
        conflict_lines = ""
        for t in mine:
            if not t.get("team_conflict"):
                continue
            for other_num in t.get("conflicts_with", []):
                o = tor_by_number.get(other_num)
                if not o:
                    continue
                conflict_lines += (
                    f"- {t.get('request_number')} ({t.get('status')}, "
                    f"{worker['name']}, {_tor_dates(t)}) overlaps "
                    f"{other_num} ({o.get('status')}, {o.get('worker_name')}, "
                    f"{_tor_dates(o)}) on the {t.get('department_name')} team — "
                    f"approver {t.get('approver_name')} should resolve before "
                    f"approving.\n"
                )
        conflict_block = (
            f"**Team Scheduling Conflicts Detected:**\n{conflict_lines}\n"
            if conflict_lines else
            "**Team Scheduling Conflicts:** none detected for this worker.\n\n"
        )
        return (
            f"**Leave Overview: {worker['name']}** ({worker['id']}, live HRIS)\n"
            f"Department: {worker['department']} | Title: {worker['title']} "
            f"({worker['level']}) | Manager: {_seam(worker['manager'])} | "
            f"Hire Date: {worker['hire_date']}\n\n"
            f"| Leave Type | Available |\n|---|---|\n"
            f"| Vacation | n/a — enrichment seam (wire your absence module) |\n"
            f"| Sick Leave | n/a — enrichment seam |\n"
            f"| Personal | n/a — enrichment seam |\n\n"
            f"**Time-Off Requests (live HRIS):**\n\n"
            f"| Request | Type | Dates | Days | Status | Team Conflict |\n"
            f"|---|---|---|---|---|---|\n"
            f"{rows}\n"
            f"{conflict_block}"
            f"Source: [Live Static HRIS — workers + time_off_requests]\n"
            f"Agents: GeneralAskHRAgent"
        )

    def _leave_request(self, params):
        live = self._live_leave_request(params.get("employee_name", ""))
        if live:
            return live
        emp_id = _resolve_employee(params.get("employee_name", ""))
        bal = _LEAVE_BALANCES.get(emp_id)
        if not bal:
            bal = list(_LEAVE_BALANCES.values())[0]
        pending_rows = ""
        for req in bal["pending_requests"]:
            pending_rows += f"| {req['dates']} | {req['days']} days | {req['status']} |\n"
        if not pending_rows:
            pending_rows = "| None | - | - |\n"
        pol = _POLICIES["pto"]
        guidelines = "\n".join(f"- {d}" for d in pol["details"][:4])
        return (
            f"**Leave Balance: {bal['name']}**\n"
            f"Department: {bal['department']} | Hire Date: {bal['hire_date']}\n\n"
            f"| Leave Type | Available |\n|---|---|\n"
            f"| Vacation | {bal['vacation']} days |\n"
            f"| Sick Leave | {bal['sick']} days |\n"
            f"| Personal | {bal['personal']} days |\n"
            f"| Accrual Rate | {bal['accrual_rate_days_per_month']} days/month |\n\n"
            f"**Pending Requests:**\n\n"
            f"| Dates | Duration | Status |\n|---|---|---|\n"
            f"{pending_rows}\n"
            f"**PTO Guidelines:**\n{guidelines}\n\n"
            f"Source: [HRIS + Time Management]\nAgents: GeneralAskHRAgent"
        )

    # ── employee_directory ─────────────────────────────────────
    def _employee_directory(self, params):
        query = params.get("employee_name", "").lower().strip()
        hris = _hris_directory()
        live = [] if hris else _live_directory()
        directory = hris or live or _ORG_DIRECTORY
        if hris:
            source = (
                "live Static HRIS — workers collection, the org's system of "
                "record (manager chains, levels, locations are real fields)"
            )
        elif live:
            source = (
                "live Static Dynamics 365 tenant — system users reinterpreted as "
                "the employee directory; location/manager/phone are enrichment seams"
            )
        else:
            source = "embedded demo layer (offline fallback)"
        if query:
            matches = [e for e in directory if query in e["name"].lower() or query in e["department"].lower()]
        else:
            matches = directory
        if not matches:
            return f"**Employee Directory Search**\n\nNo results found for \"{query}\".\n\nSource: [{source}]\nAgents: GeneralAskHRAgent"
        rows = ""
        for e in matches:
            rows += f"| {e['name']} | {e['title']} | {e['department']} | {_seam(e['location'])} | {e['email']} |\n"
        detail = matches[0]
        extra_rows = ""
        if detail.get("level"):
            extra_rows += f"| Worker ID | {detail['id']} |\n| Level | {detail['level']} |\n"
        if detail.get("hire_date"):
            extra_rows += f"| Hire Date | {detail['hire_date']} |\n"
        return (
            f"**Employee Directory Search**\n"
            f"Results: {len(matches)} employee(s) found\n\n"
            f"| Name | Title | Department | Location | Email |\n|---|---|---|---|---|\n"
            f"{rows}\n"
            f"**Detail: {detail['name']}**\n\n"
            f"| Field | Value |\n|---|---|\n"
            f"| Title | {detail['title']} |\n"
            f"| Department | {detail['department']} |\n"
            f"| Location | {_seam(detail['location'])} |\n"
            f"| Manager | {_seam(detail['manager'])} |\n"
            f"| Phone | {_seam(detail['phone'])} |\n"
            f"| Email | {detail['email']} |\n"
            f"{extra_rows}\n"
            f"Source: [{source}]\nAgents: GeneralAskHRAgent"
        )


if __name__ == "__main__":
    agent = GeneralAskHRAgent()
    print("=" * 60)
    print("EMBEDDED DEMO LEAVE BALANCE (works offline)")
    print(agent.perform(operation="leave_request", employee_name="Angela Martinez"))
    print()
    print("=" * 60)
    print("LIVE HRIS DIRECTORY (workers fetched over HTTP; falls back to CRM, then offline)")
    print(agent.perform(operation="employee_directory", employee_name="Riley Chen"))
    print()
    print("=" * 60)
    print("LIVE HRIS TEAM-CONFLICT CATCH (TOR-1006 pending vs TOR-1005 approved)")
    print(agent.perform(operation="leave_request", employee_name="Jamie Ortiz"))
    print()
    print("=" * 60)
    print("LIVE HRIS OPEN ENROLLMENT + CRM CASE JOIN + COMP BANDS")
    print(agent.perform(operation="benefits_inquiry"))
    print()
    print("=" * 60)
    print(agent.perform(operation="policy_lookup"))
    print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
