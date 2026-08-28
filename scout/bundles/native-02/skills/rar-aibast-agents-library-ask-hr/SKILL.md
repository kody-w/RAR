---
name: "rar-aibast-agents-library-ask-hr"
description: "Answers time-off, benefits, and policy questions from a live simulated HRIS joined to a Dynamics 365 CRM, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/ask_hr", "rar_sha256": "2f0b974bef2289408e6732461e43c4a4b18bf7c549733e1b46b719888e057d51", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.3.0", "author": "AIBAST", "tags": ["hr", "human-resources", "benefits", "time-off", "employee-self-service"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/ask_hr`. The original RAPP
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

Ask HR Agent — a template you are meant to mutate.

AI-powered HR assistant for employee self-service: time-off requests,
benefits inquiries, parental leave guidance, and policy lookups.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted systems (synthetic data, no credentials, works
     from anywhere):
       CRM  https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       HRIS https://kody-w.github.io/static-hris/api/v1/
     The HRIS is the real system of record HR serves: 25 workers
     (AL-00xx) with manager chains and levels, time-off requests with
     team-conflict linkage, benefits enrollments from the Nov 3-17 2025
     open enrollment, and compensation bands. The CRM joins in where
     the story connects — the pending open-enrollment confirmations
     trace to CRM case CAS-260137 "benefits portal login failures".
     Try: perform(operation="leave_balance", employee_name="Jamie Ortiz")
     to catch the live scheduling conflict — Jamie's pending TOR-1006
     overlaps Riley Chen's approved TOR-1005 on the same team.
  2. No network? Everything falls back to the embedded demo layer below
     (_EMPLOYEES / _POLICIES) — the agent never crashes offline, and
     unknown names resolve to the demo employee Jordan Chen.
  3. Make it yours at the LIVE DATA SEAM below: set ASK_HR_DATA_URL
     (CRM) and ASK_HR_HRIS_URL (HRIS) to your own endpoints, or replace
     _fetch_collection() with a Workday / BambooHR client. Fields the
     rest of the file needs are listed in _normalize_live_employee() /
     _normalize_hris_worker(). Per-worker salary deliberately does NOT
     exist in the HRIS — compensation answers come from bands only;
     individual pay is an enrichment seam (wire payroll).

OPERATIONS
  leave_balance | submit_time_off | parental_leave | health_insurance
  | remote_work | benefits_summary
  kwargs: operation (required), employee_name, start_date, end_date,
          return_date, request_date, days, coverage_notes, submit

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "coverage_notes": {
      "description": "Optional project coverage notes for the manager",
      "type": "string"
    },
    "days": {
      "description": "Chargeable working days; when supplied, must exactly match the computed working days",
      "type": "number"
    },
    "employee_name": {
      "description": "Employee name (e.g. 'Jordan Chen')",
      "type": "string"
    },
    "end_date": {
      "description": "Requested time-off end date with explicit year (YYYY-MM-DD or Month D, YYYY)",
      "type": "string"
    },
    "operation": {
      "description": "The HR inquiry to handle",
      "enum": [
        "leave_balance",
        "submit_time_off",
        "parental_leave",
        "health_insurance",
        "remote_work",
        "benefits_summary"
      ],
      "type": "string"
    },
    "request_date": {
      "description": "Optional request submission date with explicit year for notice-policy evaluation",
      "type": "string"
    },
    "return_date": {
      "description": "Optional expected return date with explicit year",
      "type": "string"
    },
    "start_date": {
      "description": "Requested time-off start date with explicit year (YYYY-MM-DD or Month D, YYYY)",
      "type": "string"
    },
    "submit": {
      "description": "Submit immediately (default) or only prepare the request",
      "type": "boolean"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ask_hr_agent.py` and embedded as the fenced Python below (sha256 2f0b974bef228940…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ask_hr_agent.py` first:

```bash
python3 ask_hr_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ask_hr_agent.py   # or on stdin
python3 ask_hr_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Ask HR Agent — a template you are meant to mutate.

AI-powered HR assistant for employee self-service: time-off requests,
benefits inquiries, parental leave guidance, and policy lookups.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted systems (synthetic data, no credentials, works
     from anywhere):
       CRM  https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       HRIS https://kody-w.github.io/static-hris/api/v1/
     The HRIS is the real system of record HR serves: 25 workers
     (AL-00xx) with manager chains and levels, time-off requests with
     team-conflict linkage, benefits enrollments from the Nov 3-17 2025
     open enrollment, and compensation bands. The CRM joins in where
     the story connects — the pending open-enrollment confirmations
     trace to CRM case CAS-260137 "benefits portal login failures".
     Try: perform(operation="leave_balance", employee_name="Jamie Ortiz")
     to catch the live scheduling conflict — Jamie's pending TOR-1006
     overlaps Riley Chen's approved TOR-1005 on the same team.
  2. No network? Everything falls back to the embedded demo layer below
     (_EMPLOYEES / _POLICIES) — the agent never crashes offline, and
     unknown names resolve to the demo employee Jordan Chen.
  3. Make it yours at the LIVE DATA SEAM below: set ASK_HR_DATA_URL
     (CRM) and ASK_HR_HRIS_URL (HRIS) to your own endpoints, or replace
     _fetch_collection() with a Workday / BambooHR client. Fields the
     rest of the file needs are listed in _normalize_live_employee() /
     _normalize_hris_worker(). Per-worker salary deliberately does NOT
     exist in the HRIS — compensation answers come from bands only;
     individual pay is an enrichment seam (wire payroll).

OPERATIONS
  leave_balance | submit_time_off | parental_leave | health_insurance
  | remote_work | benefits_summary
  kwargs: operation (required), employee_name, start_date, end_date,
          return_date, request_date, days, coverage_notes, submit
"""

import sys, os
import json
import urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
from datetime import date, datetime, timedelta

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/ask_hr",
    "version": "1.3.0",
    "display_name": "Ask HR",
    "description": "Answers time-off, benefits, and policy questions from a live simulated HRIS joined to a Dynamics 365 CRM, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["hr", "human-resources", "benefits", "time-off", "employee-self-service"],
    "category": "human_resources",
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
#         export ASK_HR_HRIS_URL=...
# or replace _fetch_collection() with your clients. Downstream code
# only needs the fields produced by _normalize_live_employee() and
# _normalize_hris_worker().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "ASK_HR_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
HRIS_SOURCE_URL = os.environ.get(
    "ASK_HR_HRIS_URL",
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
            rows = json.loads(resp.read().decode("utf-8")).get("value", [])
    except Exception:
        rows = []
    _LIVE_CACHE[url] = rows
    return rows


def _fetch_hris(collection):
    """Fetch a collection from the sibling HRIS; [] when offline."""
    return _fetch_collection(collection, base_url=HRIS_SOURCE_URL)


def _normalize_live_employee(row):
    """Project a Dynamics system user onto the employee shape this agent
    uses. THIS is the contract your replacement data source must meet — a
    dict with these keys. None means 'not knowable from the directory
    record alone' and the renderer labels it as an enrichment seam (wire
    Workday / your HRIS for balances, plans, and manager chains)."""
    return {
        "id": row.get("systemuserid", "")[:8] or "live",
        "name": row.get("fullname", "Unknown"),
        "title": row.get("title") or "n/a",
        "email": row.get("internalemailaddress", ""),
        "department": None,     # enrichment seam — wire your HRIS org chart
        "manager": None,        # enrichment seam
        "leave_balance": None,  # enrichment seam — wire Workday absences
        "_live": True,
    }


def _live_directory():
    """name-keyed dict of live tenant employees; {} when offline."""
    return {
        row["fullname"].lower(): _normalize_live_employee(row)
        for row in _fetch_collection("systemusers")
        if row.get("fullname")
    }


def _normalize_hris_worker(row):
    """Project an HRIS worker onto the employee shape this agent uses.
    The HRIS is a real system of record — department, manager, hire
    date, and level are actual fields, not seams. Leave balances still
    live in the payroll/absence module (enrichment seam)."""
    return {
        "id": row.get("worker_id", ""),
        "name": row.get("full_name", "Unknown"),
        "title": row.get("job_title") or "n/a",
        "email": row.get("work_email", ""),
        "department": row.get("department_name") or None,
        "manager": row.get("manager_name") or None,
        "level": row.get("level", ""),
        "hire_date": row.get("hire_date", ""),
        "location": row.get("work_location", ""),
        "leave_balance": None,  # enrichment seam — wire your absence module
        "_live": True,
    }


def _hris_workers():
    """name-keyed dict of live HRIS workers; {} when offline."""
    return {
        row["full_name"].lower(): _normalize_hris_worker(row)
        for row in _fetch_hris("workers")
        if row.get("full_name") and row.get("status") == "active"
    }


def _tor_dates(req):
    return f"{req.get('start_date', '?')} to {req.get('end_date', '?')}"


def _live_team_conflicts(start_iso, end_iso):
    """Approved/pending live HRIS time-off requests overlapping the
    [start_iso, end_iso] date range (ISO strings). None when the HRIS
    is unreachable (caller keeps the offline wording)."""
    tors = _fetch_hris("time_off_requests")
    if not tors:
        return None
    overlaps = []
    for t in tors:
        if t.get("status") not in ("approved", "pending"):
            continue
        t_start, t_end = t.get("start_date", ""), t.get("end_date", "")
        if t_start and t_end and t_start <= end_iso and start_iso <= t_end:
            overlaps.append(t)
    return overlaps


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_EMPLOYEES = {
    "jordan": {
        "id": "emp-1001", "name": "Jordan Chen", "title": "Senior Product Manager",
        "department": "Product", "manager": "Sarah Johnson", "tenure_years": 3.5,
        "email": "jordan.chen@contoso.com",
        "start_date": "March 2022", "location": "Seattle, WA",
        "leave_balance": {
            "vacation": 15.5, "sick": 8.0, "personal": 3.0,
            "accrual_rate": 1.25,
        },
        "health_plan": {
            "plan": "PPO Family Plan", "monthly_premium": 450,
            "deductible_individual": 500, "deductible_family": 1500,
            "oop_max_individual": 3000, "oop_max_family": 6000,
            "dependents": ["Spouse"],
            "dental_premium": 42, "vision_premium": 12,
            "retirement_contribution": "8%", "retirement_match": "4%",
        },
        "parental_eligible": True,
        "remote_eligible": True,
    },
    "michael": {
        "id": "emp-1002", "name": "Michael Torres", "title": "Account Executive",
        "department": "Sales", "manager": "David Kim", "tenure_years": 1.2,
        "email": "michael.torres@contoso.com",
        "start_date": "January 2024", "location": "Austin, TX",
        "leave_balance": {
            "vacation": 10.0, "sick": 6.0, "personal": 2.0,
            "accrual_rate": 1.0,
        },
        "health_plan": {
            "plan": "HMO Individual", "monthly_premium": 220,
            "deductible_individual": 750, "deductible_family": None,
            "oop_max_individual": 4000, "oop_max_family": None,
            "dependents": [],
            "dental_premium": 42, "vision_premium": 12,
            "retirement_contribution": "6%", "retirement_match": "4%",
        },
        "parental_eligible": False,
        "remote_eligible": True,
    },
    "sarah": {
        "id": "emp-1003", "name": "Sarah Williams", "title": "Engineering Lead",
        "department": "Engineering", "manager": "Alex Rivera", "tenure_years": 5.0,
        "email": "sarah.williams@contoso.com",
        "start_date": "March 2022", "location": "Seattle, WA",
        "leave_balance": {
            "vacation": 22.0, "sick": 10.0, "personal": 3.0,
            "accrual_rate": 1.5,
        },
        "health_plan": {
            "plan": "PPO Family Plan", "monthly_premium": 450,
            "deductible_individual": 500, "deductible_family": 1500,
            "oop_max_individual": 3000, "oop_max_family": 6000,
            "dependents": ["Spouse", "Child (age 4)"],
            "dental_premium": 42, "vision_premium": 12,
            "retirement_contribution": "8%", "retirement_match": "4%",
        },
        "parental_eligible": True,
        "remote_eligible": True,
    },
}

_COMPANY_HOLIDAYS = [
    {"name": "Memorial Day", "date": "May 26"},
    {"name": "Independence Day", "date": "Jul 4"},
    {"name": "Labor Day", "date": "Sep 1"},
    {"name": "Thanksgiving", "date": "Nov 27-28"},
    {"name": "Year-End", "date": "Dec 24-25, Dec 31-Jan 1"},
]

_FIXED_TIME_OFF_HOLIDAYS = {
    (1, 1): "New Year's Day",
    (7, 4): "Independence Day",
    (12, 24): "December 24",
    (12, 25): "December 25",
    (12, 31): "December 31",
}

_POLICIES = {
    "time_off": {
        "min_notice_5plus_days": "2 weeks",
        "holiday_period": "Dec 15 - Jan 5 requires manager pre-approval",
        "rollover_max": 5,
    },
    "parental_leave": {
        "paternity_weeks": 8, "maternity_weeks": 16,
        "min_tenure_years": 1, "stipend": 2000,
        "backup_childcare_months": 6,
    },
    "remote_work": {
        "standard_days_per_week": 3,
        "new_parent_bonus_days": 2,
        "new_parent_bonus_months": 6,
        "core_hours": "10 AM - 3 PM local",
        "equipment_stipend": 1000,
        "internet_reimbursement": 50,
    },
    "health_insurance": {
        "enrollment_window_days": 30,
        "open_enrollment": "Starts in 45 days",
        "dependent_premium_increase": 125,
        "well_baby_covered": True,
        "pediatric_copay": 20,
        "dependent_life_insurance": 10000,
        "eligible_dependents": [
            "Spouse or domestic partner",
            "Children under age 26",
            "Parents only when they are legal tax dependents and receive more than 50% support",
        ],
        "parent_alternatives": "Medicare (if 65+), Healthcare.gov, or COBRA if recently employed",
        "policy_reference": "Employee Handbook Section 4.2",
    },
}

# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _resolve_employee(query):
    if not query:
        return "jordan"
    q = query.lower().strip()
    for key in _EMPLOYEES:
        if key in q or q in _EMPLOYEES[key]["name"].lower():
            return key
    return "jordan"


def _benefits_value(emp):
    pol = _POLICIES
    values = {}
    if emp["parental_eligible"]:
        weeks = pol["parental_leave"]["paternity_weeks"]
        # Rough salary estimate from title
        weekly_salary = 2500
        values["parental_leave"] = weeks * weekly_salary
        values["family_stipend"] = pol["parental_leave"]["stipend"]
        values["childcare_benefit"] = 3000
    values["equipment_stipend"] = pol["remote_work"]["equipment_stipend"]
    total = sum(values.values())
    return values, total


def _submit_time_off(
    emp_key, start_date, end_date, return_date, days, pto_days,
    coverage_notes, submit,
):
    emp = _EMPLOYEES[emp_key]
    remaining = emp["leave_balance"]["vacation"] - pto_days
    sufficient = remaining >= 0
    parsed_start, _ = _parse_time_off_date(start_date, allow_yearless=True)
    date_key = parsed_start.strftime("%m%d") if parsed_start else "DEMO"
    request_id = f"PTO-{emp['id'].split('-')[-1]}-{date_key}"
    request = {
        "employee": emp["name"], "dates": f"{start_date} to {end_date}",
        "start_date": start_date, "end_date": end_date, "return_date": return_date,
        "days": days, "pto_days": pto_days,
        "status": "No PTO Required" if pto_days == 0 else
                  ("Pending Manager Approval" if submit and sufficient else
                   ("Ready to Submit" if sufficient else "Needs Balance Review")),
        "request_id": request_id,
        "manager": emp["manager"], "balance_after": remaining,
        "sufficient": sufficient, "coverage_notes": coverage_notes,
    }
    return request


def _parse_time_off_date(value, allow_yearless=False):
    if not value:
        return None, None
    formats = [
        ("%Y-%m-%d", True),
        ("%B %d, %Y", True),
        ("%b %d, %Y", True),
    ]
    if allow_yearless:
        formats.extend([
            ("%B %d", False),
            ("%b %d", False),
        ])
    for date_format, includes_year in formats:
        try:
            parse_value = value if includes_year else f"{value} 2025"
            parse_format = date_format if includes_year else f"{date_format} %Y"
            parsed = datetime.strptime(parse_value, parse_format)
            return parsed, date_format
        except ValueError:
            continue
    return None, None


def _format_time_off_date(value, date_format):
    if date_format == "%Y-%m-%d":
        return value.strftime("%Y-%m-%d")
    if "%Y" in date_format:
        return value.strftime("%B %d, %Y").replace(" 0", " ")
    return value.strftime("%B %d").replace(" 0", " ")


def _time_off_holidays(year):
    holidays = {
        date(year, month, day): name
        for (month, day), name in _FIXED_TIME_OFF_HOLIDAYS.items()
    }

    may_end = date(year, 5, 31)
    memorial_day = may_end - timedelta(days=may_end.weekday())
    holidays[memorial_day] = "Memorial Day"

    september_start = date(year, 9, 1)
    labor_day = september_start + timedelta(
        days=(7 - september_start.weekday()) % 7
    )
    holidays[labor_day] = "Labor Day"

    november_start = date(year, 11, 1)
    thanksgiving = november_start + timedelta(
        days=(3 - november_start.weekday()) % 7 + 21
    )
    holidays[thanksgiving] = "Thanksgiving"
    holidays[thanksgiving + timedelta(days=1)] = "Thanksgiving holiday"
    return holidays


def _holidays_for_range(start, end):
    holidays = {}
    for year in range(start.year, end.year + 1):
        holidays.update(_time_off_holidays(year))
    return holidays


def _derive_time_off_schedule(
    start_date, end_date, return_date=None, return_format=None,
):
    start, _ = _parse_time_off_date(start_date)
    end, end_format = _parse_time_off_date(end_date)
    if not start or not end:
        return None, None, None, None, (
            "Invalid time-off dates: include an explicit year using YYYY-MM-DD or Month D, YYYY."
        )
    if start > end:
        return None, None, None, None, (
            "Invalid time-off range: end date must be on or after start date."
        )
    if (end - start).days > 366:
        return None, None, None, None, (
            "Invalid time-off range: requests cannot span more than 366 calendar days."
        )

    schedule_end = end + timedelta(days=14)
    holidays = _holidays_for_range(start, schedule_end)
    requested_weekdays = sum(
        1
        for offset in range((end - start).days + 1)
        if (start + timedelta(days=offset)).weekday() < 5
    )
    working_days = sum(
        1
        for offset in range((end - start).days + 1)
        if (
            (current := start + timedelta(days=offset)).weekday() < 5
            and current.date() not in holidays
        )
    )
    if not requested_weekdays:
        return None, None, None, None, (
            "Invalid time-off range: no weekdays occur in the requested dates."
        )

    parsed_return = end + timedelta(days=1)
    while parsed_return.weekday() >= 5 or parsed_return.date() in holidays:
        parsed_return += timedelta(days=1)
    derived_return = _format_time_off_date(
        parsed_return, return_format or end_format
    )

    if return_date:
        supplied_return, _ = _parse_time_off_date(return_date)
        if not supplied_return:
            return None, None, None, None, (
                "Invalid return date: include an explicit year using YYYY-MM-DD or Month D, YYYY."
            )
        if supplied_return != parsed_return:
            return None, None, None, None, (
                f"Invalid return date: the next working day is {derived_return}."
            )

    holiday_names = []
    cursor = start
    while cursor <= parsed_return:
        name = holidays.get(cursor.date())
        if name and cursor.weekday() < 5 and name not in holiday_names:
            holiday_names.append(name)
        cursor += timedelta(days=1)
    holiday_note = None
    if holiday_names:
        holiday_note = (
            f"{', '.join(holiday_names)} "
            f"{'is' if len(holiday_names) == 1 else 'are'} a company holiday "
            f"and {'is' if len(holiday_names) == 1 else 'are'} not counted."
        )
    return derived_return, holiday_note, requested_weekdays, working_days, None


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class AskHRAgent(BasicAgent):
    """
    Employee self-service HR assistant.

    Operations:
        leave_balance     - check vacation, sick, personal day balances
        submit_time_off   - request time off for given dates
        parental_leave    - parental leave eligibility and benefits
        health_insurance  - health plan details and dependent enrollment
        remote_work       - remote work policy and new-parent flexibility
        benefits_summary  - comprehensive benefits package overview
    """

    def __init__(self):
        self.name = "AskHRAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "leave_balance", "submit_time_off",
                            "parental_leave", "health_insurance",
                            "remote_work", "benefits_summary",
                        ],
                        "description": "The HR inquiry to handle",
                    },
                    "employee_name": {
                        "type": "string",
                        "description": "Employee name (e.g. 'Jordan Chen')",
                    },
                    "start_date": {
                        "type": "string",
                        "description": "Requested time-off start date with explicit year (YYYY-MM-DD or Month D, YYYY)",
                    },
                    "end_date": {
                        "type": "string",
                        "description": "Requested time-off end date with explicit year (YYYY-MM-DD or Month D, YYYY)",
                    },
                    "return_date": {
                        "type": "string",
                        "description": "Optional expected return date with explicit year",
                    },
                    "request_date": {
                        "type": "string",
                        "description": "Optional request submission date with explicit year for notice-policy evaluation",
                    },
                    "days": {
                        "type": "number",
                        "description": "Chargeable working days; when supplied, must exactly match the computed working days",
                    },
                    "coverage_notes": {
                        "type": "string",
                        "description": "Optional project coverage notes for the manager",
                    },
                    "submit": {
                        "type": "boolean",
                        "description": "Submit immediately (default) or only prepare the request",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "leave_balance")
        key = _resolve_employee(kwargs.get("employee_name", ""))
        dispatch = {
            "parental_leave": self._parental_leave,
            "health_insurance": self._health_insurance,
            "remote_work": self._remote_work,
            "benefits_summary": self._benefits_summary,
        }
        if op == "leave_balance":
            return self._leave_balance(key, kwargs.get("employee_name", ""))
        if op == "submit_time_off":
            return self._submit_time_off(key, kwargs)
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(key)

    # ── leave_balance ─────────────────────────────────────────
    def _leave_balance(self, key, query=""):
        # Prefer a live tenant employee when the name is not one of the
        # embedded demo employees; fall back to the embedded layer.
        q = (query or "").lower().strip()
        embedded_match = any(
            k in q or q in _EMPLOYEES[k]["name"].lower() for k in _EMPLOYEES
        ) if q else True
        if q and not embedded_match:
            for live_key, live_emp in _hris_workers().items():
                if live_key in q or q in live_key:
                    return self._hris_leave_balance(live_emp)
            for live_key, live_emp in _live_directory().items():
                if live_key in q or q in live_key:
                    return self._live_leave_balance(live_emp)
        emp = _EMPLOYEES[key]
        lb = emp["leave_balance"]
        pol = _POLICIES["time_off"]
        holidays = "\n".join(f"- {h['name']}: {h['date']}" for h in _COMPANY_HOLIDAYS)
        return (
            f"**Leave Balance: {emp['name']}**\n\n"
            f"| Leave Type | Available |\n|---|---|\n"
            f"| Vacation | {lb['vacation']} days |\n"
            f"| Sick Leave | {lb['sick']} days |\n"
            f"| Personal Days | {lb['personal']} days |\n"
            f"| Accrual Rate | {lb['accrual_rate']} days/month |\n\n"
            f"**Upcoming Company Holidays:**\n{holidays}\n\n"
            f"**Time Off Guidelines:**\n"
            f"- 5+ days: Requires {pol['min_notice_5plus_days']} notice\n"
            f"- {pol['holiday_period']}\n"
            f"- Rollover policy: Max {pol['rollover_max']} days carry to next year\n\n"
            f"Source: [Workday + HR Portal]\nAgents: AskHRAgent"
        )

    # ── HRIS leave_balance (real system of record) ────────────
    def _hris_leave_balance(self, emp):
        seam = "n/a — enrichment seam"
        pol = _POLICIES["time_off"]
        tors = _fetch_hris("time_off_requests")
        mine = [t for t in tors if t.get("worker_id") == emp["id"]]
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
                    f"{emp['name']}, {_tor_dates(t)}) overlaps {other_num} "
                    f"({o.get('status')}, {o.get('worker_name')}, "
                    f"{_tor_dates(o)}) on the {t.get('department_name')} team "
                    f"— approver {t.get('approver_name')} should resolve "
                    f"before approving.\n"
                )
        conflict_block = (
            f"**Team Scheduling Conflicts Detected:**\n{conflict_lines}\n"
            if conflict_lines else
            "**Team Scheduling Conflicts:** none detected for this worker.\n\n"
        )
        return (
            f"**Leave Overview: {emp['name']}** ({emp['id']}, live HRIS)\n\n"
            f"| Detail | Value |\n|---|---|\n"
            f"| Title | {emp['title']} ({emp['level']}) |\n"
            f"| Department | {emp['department']} |\n"
            f"| Manager | {emp['manager'] or seam} |\n"
            f"| Hire Date | {emp['hire_date']} |\n"
            f"| Email | {emp['email']} |\n"
            f"| Vacation | {seam} (wire your absence module) |\n"
            f"| Sick Leave | {seam} |\n\n"
            f"**Time-Off Requests (live HRIS):**\n\n"
            f"| Request | Type | Dates | Days | Status | Team Conflict |\n"
            f"|---|---|---|---|---|---|\n"
            f"{rows}\n"
            f"{conflict_block}"
            f"**Time Off Guidelines:**\n"
            f"- 5+ days: Requires {pol['min_notice_5plus_days']} notice\n"
            f"- {pol['holiday_period']}\n"
            f"- Rollover policy: Max {pol['rollover_max']} days carry to next year\n\n"
            f"Source: [Live Static HRIS — workers + time_off_requests]\n"
            f"Agents: AskHRAgent"
        )

    # ── live leave_balance (tenant directory record) ──────────
    def _live_leave_balance(self, emp):
        seam = "n/a — enrichment seam"
        pol = _POLICIES["time_off"]
        holidays = "\n".join(f"- {h['name']}: {h['date']}" for h in _COMPANY_HOLIDAYS)
        return (
            f"**Leave Balance: {emp['name']}** (live tenant directory)\n\n"
            f"| Detail | Value |\n|---|---|\n"
            f"| Title | {emp['title']} |\n"
            f"| Email | {emp['email']} |\n"
            f"| Department | {emp['department'] or seam} |\n"
            f"| Manager | {emp['manager'] or seam} |\n"
            f"| Vacation | {seam} (wire Workday absences) |\n"
            f"| Sick Leave | {seam} |\n"
            f"| Personal Days | {seam} |\n\n"
            f"**Upcoming Company Holidays:**\n{holidays}\n\n"
            f"**Time Off Guidelines:**\n"
            f"- 5+ days: Requires {pol['min_notice_5plus_days']} notice\n"
            f"- {pol['holiday_period']}\n"
            f"- Rollover policy: Max {pol['rollover_max']} days carry to next year\n\n"
            f"Source: [Live Static Dynamics 365 tenant — systemusers]\nAgents: AskHRAgent"
        )

    # ── submit_time_off ───────────────────────────────────────
    def _submit_time_off(self, key, params):
        emp = _EMPLOYEES[key]
        evidence_request = any(
            name in params
            for name in (
                "start_date", "end_date", "return_date", "request_date", "days",
                "coverage_notes", "submit",
            )
        )
        if not evidence_request:
            today = datetime.now()
            start = (today + timedelta(days=30)).strftime("%b %d")
            end = (today + timedelta(days=34)).strftime("%b %d")
            req = _submit_time_off(key, start, end, "", 5, 5, "", True)
            return (
                f"**Time Off Request Submitted**\n\n"
                f"| Detail | Information |\n|---|---|\n"
                f"| Employee | {emp['name']} |\n"
                f"| Dates | {req['dates']} (5 days) |\n"
                f"| Status | {req['status']} |\n"
                f"| Manager | {req['manager']} |\n"
                f"| Balance After | {req['balance_after']} days remaining |\n\n"
                f"Your manager will be notified automatically.\n\n"
                f"Source: [Workday]\nAgents: AskHRAgent"
            )

        has_start = bool(params.get("start_date"))
        has_end = bool(params.get("end_date"))
        if has_start != has_end:
            return "Invalid time-off range: provide both start_date and end_date."
        if has_start:
            start = params["start_date"]
            end = params["end_date"]
            schedule_start = start
            schedule_end = end
            return_format = None
        else:
            start = "December 18"
            end = "December 24"
            schedule_start = "December 18, 2023"
            schedule_end = "December 24, 2023"
            return_format = "%B %d"
        (
            return_date, holiday_note, requested_weekdays, working_days,
            schedule_error,
        ) = _derive_time_off_schedule(
            schedule_start, schedule_end, params.get("return_date"),
            return_format=return_format,
        )
        if schedule_error:
            return schedule_error
        try:
            days = float(
                params["days"] if params.get("days") is not None
                else working_days
            )
        except (TypeError, ValueError):
            return "Invalid days: provide a numeric number of working days."
        if days < 0:
            return "Invalid days: provide a non-negative number of working days."
        if days != working_days:
            return (
                f"Invalid days: {days:g} does not match the computed "
                f"{working_days} chargeable working days."
            )
        days = int(days) if days.is_integer() else days
        pto_days = days

        request_date = params.get("request_date")
        if request_date:
            parsed_request, _ = _parse_time_off_date(request_date)
            parsed_start, _ = _parse_time_off_date(schedule_start)
            if not parsed_request:
                return (
                    "Invalid request date: include an explicit year using "
                    "YYYY-MM-DD or Month D, YYYY."
                )
            if parsed_request > parsed_start:
                return "Invalid request date: request_date cannot be after start_date."
            notice_days = (parsed_start - parsed_request).days
            if days >= 5:
                notice_status = (
                    f"Meets the two-week requirement ({notice_days} days notice)"
                    if notice_days >= 14
                    else (
                        f"Does not meet the two-week requirement "
                        f"({notice_days} days notice)"
                    )
                )
            else:
                notice_status = (
                    f"Two-week notice is not required for fewer than 5 working "
                    f"days ({notice_days} days notice)"
                )
        else:
            notice_status = (
                "Not evaluated; compliance not established—provide request_date "
                "to check the two-week requirement"
            )
        parsed_range_start, _ = _parse_time_off_date(schedule_start)
        parsed_range_end, _ = _parse_time_off_date(schedule_end)
        live_overlaps = None
        if parsed_range_start and parsed_range_end:
            live_overlaps = _live_team_conflicts(
                parsed_range_start.strftime("%Y-%m-%d"),
                parsed_range_end.strftime("%Y-%m-%d"),
            )
        if live_overlaps is None:
            conflict_status = "None detected in the offline demo calendar"
        elif live_overlaps:
            ex = live_overlaps[0]
            conflict_status = (
                f"{len(live_overlaps)} overlapping request(s) in the live "
                f"HRIS calendar — e.g. {ex.get('request_number')} "
                f"({ex.get('status')}, {ex.get('worker_name')}, "
                f"{ex.get('department_name')}, {_tor_dates(ex)})"
            )
        else:
            conflict_status = "None overlap in the live HRIS time-off calendar"
        coverage_notes = params.get("coverage_notes") or "Optional - add project coverage notes for your manager"
        submit = params.get("submit", True)
        req = _submit_time_off(
            key, start, end, return_date, days, pto_days, coverage_notes, submit
        )
        action = "Submitted" if submit and req["sufficient"] else "Prepared"
        notification = (
            f"{req['manager']} will receive an immediate email and Teams notification; "
            f"approval is expected within 48 hours."
            if submit and req["sufficient"]
            else (
                f"{req['manager']} will be notified when the request is submitted; "
                f"approval is expected within 48 hours."
            )
        )
        return_row = (
            f"| Return Date | {req['return_date']} |\n"
            if req["return_date"] else ""
        )
        holiday_line = (
            f"**Holiday Note:** {holiday_note}\n"
            if holiday_note else ""
        )
        return (
            f"**Time Off Request {action}**\n\n"
            f"| Detail | Information |\n|---|---|\n"
            f"| Employee | {emp['name']} |\n"
            f"| Request ID | {req['request_id']} |\n"
            f"| Dates | {req['dates']} ({days} days) |\n"
            f"{return_row}"
            f"| Status | {req['status']} |\n"
            f"| Manager | {req['manager']} |\n"
            f"| PTO Charged | {req['pto_days']} days |\n"
            f"| Balance After | {req['balance_after']} days remaining |\n\n"
            f"**Policy Check:**\n"
            f"- {'Sufficient balance' if req['sufficient'] else 'Insufficient balance'}: "
            f"{emp['leave_balance']['vacation']} days available\n"
            f"- Advance notice: {notice_status}\n"
            f"- Team conflicts: {conflict_status}\n"
            f"- Blackout dates: None detected\n\n"
            f"Your manager will be notified automatically.\n\n"
            f"**Workflow:** {notification}\n"
            f"{holiday_line}"
            f"**Coverage Notes:** {req['coverage_notes']}\n\n"
            f"**Helpful Reminders:**\n"
            f"- Open enrollment: {_POLICIES['health_insurance']['open_enrollment']}\n"
            f"- PTO carryover: Maximum {_POLICIES['time_off']['rollover_max']} days; review before December 31\n\n"
            f"Source: [Workday]\n"
            f"Evidence sources: [HR Policy Portal + Outlook + Microsoft Teams]\n"
            f"Agents: AskHRAgent"
        )

    # ── parental_leave ────────────────────────────────────────
    def _parental_leave(self, key):
        emp = _EMPLOYEES[key]
        pol = _POLICIES["parental_leave"]
        eligible = emp["parental_eligible"]
        status = "Qualified" if eligible else "Not yet eligible (requires 1+ year tenure)"
        return (
            f"**Parental Leave Benefits: {emp['name']}**\n\n"
            f"| Benefit | Details |\n|---|---|\n"
            f"| Paternity Leave | {pol['paternity_weeks']} weeks fully paid |\n"
            f"| Maternity Leave | {pol['maternity_weeks']} weeks fully paid |\n"
            f"| Your Eligibility | {status} |\n"
            f"| Family Care Stipend | ${pol['stipend']:,} one-time |\n"
            f"| Backup Childcare | {pol['backup_childcare_months']} months included |\n\n"
            f"**Additional Support:**\n"
            f"- Flexible return-to-work schedule available\n"
            f"- Parent Employee Resource Group\n"
            f"- Lactation room access\n\n"
            f"**Next Step:** Submit parental leave form 30 days before due date.\n\n"
            f"Source: [Benefits Portal]\nAgents: AskHRAgent"
        )

    # ── health_insurance ──────────────────────────────────────
    def _health_insurance(self, key):
        emp = _EMPLOYEES[key]
        hp = emp["health_plan"]
        pol = _POLICIES["health_insurance"]
        deps = ", ".join(hp["dependents"]) if hp["dependents"] else "None"
        eligible = "\n".join(f"- {item}" for item in pol["eligible_dependents"])
        return (
            f"**Health Insurance: {emp['name']}**\n\n"
            f"| Coverage | Detail |\n|---|---|\n"
            f"| Plan | {hp['plan']} |\n"
            f"| Monthly Premium | ${hp['monthly_premium']:,} (your contribution) |\n"
            f"| Deductible (Individual) | ${hp['deductible_individual']:,} |\n"
            f"| Out-of-Pocket Max | ${hp['oop_max_individual']:,} |\n"
            f"| Current Dependents | {deps} |\n\n"
            f"**Eligible Dependents:**\n{eligible}\n"
            f"- Alternatives for parents: {pol['parent_alternatives']}\n"
            f"- Policy reference: {pol['policy_reference']}\n\n"
            f"**Adding a Dependent:**\n"
            f"- Enrollment window: {pol['enrollment_window_days']} days from qualifying event\n"
            f"- Premium increase: +${pol['dependent_premium_increase']}/month\n"
            f"- Coverage effective: Date of qualifying event\n\n"
            f"**New Baby Benefits (100% Covered):**\n"
            f"- Well-baby care visits\n"
            f"- All immunizations\n"
            f"- Pediatric visits: ${pol['pediatric_copay']} copay\n"
            f"- Dependent life insurance: ${pol['dependent_life_insurance']:,} automatic\n\n"
            f"Source: [Benefits Portal + Insurance Carrier]\nAgents: AskHRAgent"
        )

    # ── remote_work ───────────────────────────────────────────
    def _remote_work(self, key):
        emp = _EMPLOYEES[key]
        pol = _POLICIES["remote_work"]
        eligible = emp["remote_eligible"]
        total_days = pol["standard_days_per_week"]
        parent_note = ""
        if emp["parental_eligible"]:
            total_days += pol["new_parent_bonus_days"]
            parent_note = (
                f"\n**New Parent Options:**\n"
                f"- Additional {pol['new_parent_bonus_days']} remote days/week for {pol['new_parent_bonus_months']} months\n"
                f"- Gradual return: Part-time for 4 weeks\n"
                f"- Emergency childcare: 10 days/year included\n"
            )
        return (
            f"**Remote Work Policy: {emp['name']}**\n\n"
            f"| Benefit | Your Eligibility |\n|---|---|\n"
            f"| Standard Allowance | {pol['standard_days_per_week']} days/week remote |\n"
            f"| Your Status | {'Eligible' if eligible else 'Not eligible'} |\n"
            f"| Core Hours | {pol['core_hours']} |\n\n"
            f"**Home Office Support:**\n"
            f"- Equipment stipend: ${pol['equipment_stipend']:,} one-time\n"
            f"- Internet reimbursement: ${pol['internet_reimbursement']}/month\n"
            f"- Ergonomic assessment: Virtual consultation\n"
            f"- Same-day IT support available\n"
            f"{parent_note}\n"
            f"Source: [HR Policy Portal + Benefits]\nAgents: AskHRAgent"
        )

    # ── benefits_summary ──────────────────────────────────────
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

    def _benefits_summary(self, key):
        emp = _EMPLOYEES[key]
        lb = emp["leave_balance"]
        hp = emp["health_plan"]
        values, total = _benefits_value(emp)
        pol = _POLICIES

        items = []
        items.append(f"- Time Off: {lb['vacation']} vacation days + {lb['sick']} sick days")
        if emp["parental_eligible"]:
            items.append(f"- Parental Leave: {pol['parental_leave']['paternity_weeks']} weeks paid + ${pol['parental_leave']['stipend']:,} stipend")
        items.append(f"- Health Coverage: {hp['plan']} (${hp['monthly_premium']}/mo)")
        items.append(f"- Dental: ${hp['dental_premium']}/mo; Vision: ${hp['vision_premium']}/mo")
        items.append(
            f"- 401(k): {hp['retirement_contribution']} contribution "
            f"({hp['retirement_match']} employer match)"
        )
        items.append(f"- Remote Work: {pol['remote_work']['standard_days_per_week']} days/week")
        items.append(f"- Equipment Stipend: ${pol['remote_work']['equipment_stipend']:,}")

        value_lines = "\n".join(f"- {k.replace('_', ' ').title()}: ${v:,}" for k, v in values.items())
        live_section = self._live_benefits_section()
        source = (
            "All HR Systems + Live Static HRIS" if live_section
            else "All HR Systems"
        )

        return (
            f"**Benefits Summary: {emp['name']}**\n"
            f"**{emp['title']}, {emp['department']}** ({emp['tenure_years']} years)\n"
            f"Start date: {emp['start_date']} | Location: {emp['location']}\n\n"
            f"**Your Benefits Package:**\n"
            + "\n".join(items) + "\n\n"
            f"**Financial Value:**\n{value_lines}\n"
            f"**Total estimated value: ${total:,}**\n\n"
            f"**Next Steps:**\n"
            f"1. Review parental leave form (submit 30 days before due date)\n"
            f"2. Benefits enrollment changes within 30 days of qualifying event\n"
            f"3. Discuss remote schedule with {emp['manager']}\n\n"
            f"**Open enrollment reminder:** {_POLICIES['health_insurance']['open_enrollment']}.\n\n"
            + live_section +
            f"Source: [{source}]\nAgents: AskHRAgent"
        )


if __name__ == "__main__":
    agent = AskHRAgent()
    print("=" * 60)
    print("EMBEDDED DEMO EMPLOYEE (works offline)")
    print(agent.perform(operation="leave_balance", employee_name="Jordan Chen"))
    print()
    print("=" * 60)
    print("LIVE HRIS WORKER (fetched over HTTP; falls back to CRM, then offline)")
    print(agent.perform(operation="leave_balance", employee_name="Morgan Ellis"))
    print()
    print("=" * 60)
    print("LIVE HRIS TEAM-CONFLICT CATCH (TOR-1006 pending vs TOR-1005 approved)")
    print(agent.perform(operation="leave_balance", employee_name="Jamie Ortiz"))
    print()
    print("=" * 60)
    print("LIVE HRIS CONFLICT CHECK ON A NEW REQUEST (overlaps the TOR-1005 window)")
    print(agent.perform(
        operation="submit_time_off", employee_name="Jordan Chen",
        start_date="2026-01-26", end_date="2026-01-28",
    ))
    print()
    for op in ["submit_time_off", "parental_leave",
               "health_insurance", "remote_work", "benefits_summary"]:
        print("=" * 60)
        print(agent.perform(operation=op, employee_name="Jordan Chen"))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
