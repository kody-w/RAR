"""
General Ask HR Agent — a template you are meant to mutate.

General-purpose HR assistant for policy lookups, benefits inquiries,
leave requests, and employee directory searches. In this template the
employee directory is backed by Dynamics 365 system users — the tenant
has no native HRIS entity, so the CRM user roster stands in for the org
directory (leave balances and benefits stay embedded demos).

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `employee_directory` operation pulls
     live system-user records over real HTTP from the globally hosted
     Static Dynamics 365 tenant (Aster Lane Office Systems — synthetic
     data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="employee_directory",
                  employee_name="Casey Rivera")
     to pull the live Support Specialist record.
  2. No network? Everything falls back to the embedded demo layer below
     (_POLICIES / _LEAVE_BALANCES / _ORG_DIRECTORY) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set ASK_HR_DATA_URL to
     any OData-shaped endpoint (your real Dynamics org, or JSON exported
     from Workday/BambooHR), or replace _fetch_collection() with your
     HRIS client. The fields the rest of the file needs are listed in
     _normalize_live_employee() — fields rendered "n/a — enrichment
     seam" (location, manager, phone) are where you wire your HRIS.

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
    "version": "1.1.0",
    "display_name": "General Ask HR",
    "description": "Answers HR policy, leave, and directory queries from a live simulated Dynamics 365 tenant (users as employees), with an offline fallback.",
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
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export ASK_HR_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your HRIS client. Downstream code
# only needs the fields produced by _normalize_live_employee().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "ASK_HR_DATA_URL",
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
            f"Source: [Benefits Portal + Insurance Carriers]\nAgents: GeneralAskHRAgent"
        )

    # ── leave_request ──────────────────────────────────────────
    def _leave_request(self, params):
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
        live = _live_directory()
        directory = live or _ORG_DIRECTORY
        source = (
            "live Static Dynamics 365 tenant — system users reinterpreted as "
            "the employee directory; location/manager/phone are enrichment seams"
            if live else "embedded demo layer (offline fallback)"
        )
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
            f"| Email | {detail['email']} |\n\n"
            f"Source: [{source}]\nAgents: GeneralAskHRAgent"
        )


if __name__ == "__main__":
    agent = GeneralAskHRAgent()
    print("=" * 60)
    print("EMBEDDED DEMO LEAVE BALANCE (works offline)")
    print(agent.perform(operation="leave_request", employee_name="Angela Martinez"))
    print()
    print("=" * 60)
    print("LIVE TENANT DIRECTORY (system users fetched over HTTP; falls back offline)")
    print(agent.perform(operation="employee_directory", employee_name="Casey Rivera"))
    print()
    for op in ["policy_lookup", "benefits_inquiry"]:
        print("=" * 60)
        print(agent.perform(operation=op))
        print()
