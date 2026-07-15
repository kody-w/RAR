"""
Ask HR Agent

AI-powered HR assistant for employee self-service: time-off requests,
benefits inquiries, parental leave guidance, and policy lookups.

Where a real deployment would call Workday, Benefits Portal, or HR systems,
this agent uses a synthetic data layer so it runs anywhere without credentials.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
from datetime import date, datetime, timedelta

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/ask_hr",
    "version": "1.1.0",
    "display_name": "Ask HR",
    "description": "AI-powered HR assistant for time-off requests, benefits inquiries, parental leave, and policy lookups.",
    "author": "AIBAST",
    "tags": ["hr", "human-resources", "benefits", "time-off", "employee-self-service"],
    "category": "human_resources",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# SYNTHETIC DATA LAYER
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
            "leave_balance": self._leave_balance,
            "parental_leave": self._parental_leave,
            "health_insurance": self._health_insurance,
            "remote_work": self._remote_work,
            "benefits_summary": self._benefits_summary,
        }
        if op == "submit_time_off":
            return self._submit_time_off(key, kwargs)
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(key)

    # ── leave_balance ─────────────────────────────────────────
    def _leave_balance(self, key):
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
            f"- Team conflicts: None detected in the offline demo calendar\n"
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
            f"Source: [All HR Systems]\nAgents: AskHRAgent"
        )


if __name__ == "__main__":
    agent = AskHRAgent()
    for op in ["leave_balance", "submit_time_off", "parental_leave",
               "health_insurance", "remote_work", "benefits_summary"]:
        print("=" * 60)
        print(agent.perform(operation=op, employee_name="Jordan Chen"))
        print()
