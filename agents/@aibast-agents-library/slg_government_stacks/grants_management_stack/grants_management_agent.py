"""
SLG Grants Management Agent — a template you are meant to mutate.

Manages state and local government grant portfolios including
application tracking, reporting calendars, and budget monitoring.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live grant-compliance cases over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="grants_portfolio")
     — with network up, the portfolio view surfaces the tenant's live
     grant cases such as CAS-260136 "Grant drawdown report rejected for
     missing form" (Federal Plaza Services Agency) plus the open tasks
     tracking them. In this template a grant compliance item is
     represented as a Dynamics case (incident) and its work items as
     Dynamics tasks.
  2. No network? Everything falls back to the embedded demo layer below
     (GRANTS_PORTFOLIO / REPORTING_REQUIREMENTS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SLG_GRANTS_MANAGEMENT_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from eCivis/AmpliFund), or
     replace _fetch_collection() with your grants-system API. The fields
     the rest of the file needs are listed in _normalize_live_grant_case()
     — award amounts and burn rates stay "n/a — enrichment seam" until
     you wire your ERP/grants ledger.

OPERATIONS
  grants_portfolio | application_status | reporting_calendar |
  budget_tracking
  kwargs: operation (required), grant_id
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timezone

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/slg_grants_management",
    "version": "1.1.0",
    "display_name": "SLG Grants Management Agent",
    "description": "Tracks grant compliance and budgets from a live simulated Dynamics 365 tenant's grant cases, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["grants", "budget", "reporting", "local-government", "state-government"],
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
#   export SLG_GRANTS_MANAGEMENT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your grants-system client.
# Downstream code only needs the fields from _normalize_live_grant_case().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "SLG_GRANTS_MANAGEMENT_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
_LIVE_CACHE = {}

# Case-title keywords that mark a tenant case as a grant-office item.
_GRANT_KEYWORDS = ("grant", "drawdown", "nofo", "subaward")


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


def _normalize_live_grant_case(row, tasks):
    """Project a Dynamics case (incident) record onto the shape this agent
    uses — in this template a grant compliance item IS a Dynamics case,
    and its work items are Dynamics tasks. THIS is the contract your
    replacement data source must meet — a dict with these keys. None
    means 'not available from the case system alone' and the renderers
    label it as an enrichment seam."""
    title = row.get("title", "untitled")
    open_tasks = [
        t for t in tasks
        if t.get("regardingobjectidname") == title and t.get("statecode") == 0
    ]
    return {
        "case_id": row.get("ticketnumber", row.get("incidentid", "")),
        "title": title,
        "grantee": row.get("customeridname", "Unknown"),
        "status": row.get(
            "statecode@OData.Community.Display.V1.FormattedValue", "Active"
        ),
        "priority": row.get(
            "prioritycode@OData.Community.Display.V1.FormattedValue", "Normal"
        ),
        "owner": row.get("owneridname", "Unassigned"),
        "due_date": str(row.get("resolveby") or "")[:10] or None,
        "age_days": _age_days(row.get("createdon")),
        "open": row.get("statecode") == 0,
        "open_tasks": len(open_tasks),
        "award_amount": None,  # enrichment seam — wire your ERP/grants ledger
        "burn_rate": None,     # enrichment seam
        "_live": True,
    }


def _age_days(iso_date):
    try:
        then = datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
        return max(0, (datetime.now(timezone.utc) - then).days)
    except (ValueError, TypeError):
        return 0


def _live_grant_queue():
    """Live tenant cases whose titles look grant-shaped; [] offline."""
    rows = [
        row for row in _fetch_collection("incidents")
        if any(kw in str(row.get("title", "")).lower() for kw in _GRANT_KEYWORDS)
    ]
    if not rows:
        return []
    tasks = _fetch_collection("tasks")
    queue = [_normalize_live_grant_case(row, tasks) for row in rows]
    return [g for g in queue if g["case_id"]]


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback) — Synthetic domain data
# ---------------------------------------------------------------------------

GRANTS_PORTFOLIO = {
    "LG-2025-001": {
        "title": "Community Policing Initiative Grant",
        "grantor": "State Dept. of Justice",
        "amount": 475000,
        "match_required": 0.25,
        "local_match": 118750,
        "start_date": "2024-07-01",
        "end_date": "2026-06-30",
        "status": "active",
        "department": "Police Department",
        "spent": 198000,
        "encumbered": 52000,
    },
    "LG-2025-002": {
        "title": "Clean Water Infrastructure Improvement",
        "grantor": "EPA — State Revolving Fund",
        "amount": 2800000,
        "match_required": 0.20,
        "local_match": 560000,
        "start_date": "2025-01-01",
        "end_date": "2027-12-31",
        "status": "active",
        "department": "Public Works",
        "spent": 140000,
        "encumbered": 825000,
    },
    "LG-2025-003": {
        "title": "Youth Employment Summer Program",
        "grantor": "State Dept. of Labor",
        "amount": 165000,
        "match_required": 0.10,
        "local_match": 16500,
        "start_date": "2025-04-01",
        "end_date": "2025-09-30",
        "status": "pending_award",
        "department": "Parks & Recreation",
        "spent": 0,
        "encumbered": 0,
    },
    "LG-2025-004": {
        "title": "Broadband Expansion — Underserved Areas",
        "grantor": "NTIA — BEAD Program",
        "amount": 1250000,
        "match_required": 0.25,
        "local_match": 312500,
        "start_date": "2025-03-01",
        "end_date": "2028-02-28",
        "status": "application_submitted",
        "department": "IT Department",
        "spent": 0,
        "encumbered": 0,
    },
    "LG-2025-005": {
        "title": "Historic Downtown Revitalization",
        "grantor": "State Historic Preservation Office",
        "amount": 380000,
        "match_required": 0.50,
        "local_match": 190000,
        "start_date": "2024-10-01",
        "end_date": "2026-09-30",
        "status": "active",
        "department": "Community Development",
        "spent": 142500,
        "encumbered": 67000,
    },
}

APPLICATION_WORKFLOWS = {
    "pre_application": ["Identify funding opportunity", "Review NOFO requirements", "Assess eligibility", "Obtain internal authorization"],
    "application": ["Prepare project narrative", "Develop budget justification", "Gather required certifications", "Complete SF-424 forms", "Submit via grants.gov or state portal"],
    "post_submission": ["Confirm receipt", "Respond to clarification requests", "Await award notification"],
    "award_setup": ["Execute grant agreement", "Set up grant fund codes in ERP", "Establish reporting calendar", "Notify department leads"],
    "implementation": ["Procure goods/services per grant terms", "Track expenditures against budget", "Submit progress reports", "Monitor compliance"],
    "closeout": ["Complete final expenditure report", "Submit final performance report", "Return unused funds", "Archive documentation"],
}

REPORTING_REQUIREMENTS = {
    "LG-2025-001": [
        {"report": "Quarterly Financial Report", "due": "2025-04-15", "status": "upcoming"},
        {"report": "Semi-Annual Performance Report", "due": "2025-07-31", "status": "upcoming"},
        {"report": "Annual Single Audit (if applicable)", "due": "2025-12-31", "status": "upcoming"},
    ],
    "LG-2025-002": [
        {"report": "Monthly Draw Request", "due": "2025-04-10", "status": "upcoming"},
        {"report": "Quarterly Progress Report", "due": "2025-04-30", "status": "upcoming"},
        {"report": "Davis-Bacon Certified Payroll", "due": "2025-04-07", "status": "upcoming"},
    ],
    "LG-2025-005": [
        {"report": "Quarterly Expenditure Report", "due": "2025-04-15", "status": "upcoming"},
        {"report": "Photo Documentation Update", "due": "2025-06-30", "status": "upcoming"},
        {"report": "Historic Preservation Compliance Review", "due": "2025-09-30", "status": "upcoming"},
    ],
}

BUDGET_CATEGORIES = {
    "personnel": "Salaries, wages, and fringe benefits",
    "contractual": "Professional services and subcontracts",
    "equipment": "Capital equipment over $5,000",
    "supplies": "Office and operational supplies",
    "travel": "Staff travel and training",
    "indirect": "Indirect cost allocation",
    "other": "Miscellaneous direct costs",
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _portfolio_totals():
    """Aggregate portfolio financial totals."""
    total_awards = sum(g["amount"] for g in GRANTS_PORTFOLIO.values())
    total_match = sum(g["local_match"] for g in GRANTS_PORTFOLIO.values())
    total_spent = sum(g["spent"] for g in GRANTS_PORTFOLIO.values())
    total_encumbered = sum(g["encumbered"] for g in GRANTS_PORTFOLIO.values())
    available = total_awards - total_spent - total_encumbered
    return {
        "total_awards": total_awards,
        "total_match": total_match,
        "total_spent": total_spent,
        "total_encumbered": total_encumbered,
        "available": available,
    }


def _burn_rate(grant):
    """Calculate spending rate as percentage of award."""
    if grant["amount"] == 0:
        return 0.0
    return round(((grant["spent"] + grant["encumbered"]) / grant["amount"]) * 100, 1)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class SLGGrantsManagementAgent(BasicAgent):
    """State and local government grants management agent."""

    def __init__(self):
        self.name = "SLGGrantsManagementAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "SLG Grants Management Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "grants_portfolio",
                            "application_status",
                            "reporting_calendar",
                            "budget_tracking",
                        ],
                    },
                    "grant_id": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "grants_portfolio")
        dispatch = {
            "grants_portfolio": self._grants_portfolio,
            "application_status": self._application_status,
            "reporting_calendar": self._reporting_calendar,
            "budget_tracking": self._budget_tracking,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        return handler(**kwargs)

    def _live_grants_portfolio(self, queue):
        """Grant compliance queue from live tenant cases (preferred online)."""
        lines = [
            "# Grants Compliance Queue — Live Tenant Cases\n",
            f"Live records from {DATA_SOURCE_URL} (Aster Lane Office Systems).",
            "In this template a grant compliance item is a Dynamics case.",
            "Pass `grant_id` (e.g. LG-2025-001) for the embedded demo portfolio.\n",
            f"**Matched grant cases:** {len(queue)} "
            f"({sum(1 for g in queue if g['open'])} open)\n",
            "| Case | Item | Grantee | Priority | Status | Due | Open Tasks | Award | Burn Rate |",
            "|---|---|---|---|---|---|---|---|---|",
        ]
        for g in sorted(queue, key=lambda x: x["case_id"]):
            award = "n/a — enrichment seam" if g["award_amount"] is None else f"${g['award_amount']:,.0f}"
            burn = "n/a — enrichment seam" if g["burn_rate"] is None else f"{g['burn_rate']}%"
            lines.append(
                f"| {g['case_id']} | {g['title']} | {g['grantee']} "
                f"| {g['priority']} | {g['status']} | {g['due_date'] or 'n/a'} "
                f"| {g['open_tasks']} | {award} | {burn} |"
            )
        lines.append("")
        lines.append(
            "Award amounts, match, and burn rates need your ERP/grants ledger — "
            "wire it at the LIVE DATA SEAM."
        )
        return "\n".join(lines)

    def _grants_portfolio(self, **kwargs) -> str:
        if not kwargs.get("grant_id"):
            queue = _live_grant_queue()
            if queue:
                return self._live_grants_portfolio(queue)
        totals = _portfolio_totals()
        lines = ["# Grants Portfolio Overview\n"]
        lines.append(f"**Total Awards:** ${totals['total_awards']:,.0f}")
        lines.append(f"**Local Match Committed:** ${totals['total_match']:,.0f}")
        lines.append(f"**Spent:** ${totals['total_spent']:,.0f}")
        lines.append(f"**Encumbered:** ${totals['total_encumbered']:,.0f}")
        lines.append(f"**Available:** ${totals['available']:,.0f}\n")
        lines.append("| Grant ID | Title | Grantor | Amount | Status | Dept |")
        lines.append("|---|---|---|---|---|---|")
        for gid, g in GRANTS_PORTFOLIO.items():
            lines.append(
                f"| {gid} | {g['title']} | {g['grantor']} "
                f"| ${g['amount']:,.0f} | {g['status'].replace('_', ' ').title()} | {g['department']} |"
            )
        return "\n".join(lines)

    def _application_status(self, **kwargs) -> str:
        lines = ["# Grant Application Status\n"]
        pending = {k: v for k, v in GRANTS_PORTFOLIO.items() if v["status"] in ("pending_award", "application_submitted")}
        if pending:
            lines.append("## Pending Applications\n")
            for gid, g in pending.items():
                lines.append(f"### {gid}: {g['title']}\n")
                lines.append(f"- **Grantor:** {g['grantor']}")
                lines.append(f"- **Amount Requested:** ${g['amount']:,.0f}")
                lines.append(f"- **Match Required:** {g['match_required'] * 100:.0f}% (${g['local_match']:,.0f})")
                lines.append(f"- **Status:** {g['status'].replace('_', ' ').title()}")
                lines.append(f"- **Department:** {g['department']}\n")
        lines.append("## Application Workflow Reference\n")
        for phase, steps in APPLICATION_WORKFLOWS.items():
            lines.append(f"### {phase.replace('_', ' ').title()}\n")
            for i, step in enumerate(steps, 1):
                lines.append(f"{i}. {step}")
            lines.append("")
        return "\n".join(lines)

    def _reporting_calendar(self, **kwargs) -> str:
        lines = ["# Grant Reporting Calendar\n"]
        for gid, reports in REPORTING_REQUIREMENTS.items():
            grant = GRANTS_PORTFOLIO.get(gid, {})
            lines.append(f"## {gid}: {grant.get('title', 'Unknown')}\n")
            lines.append("| Report | Due Date | Status |")
            lines.append("|---|---|---|")
            for r in reports:
                lines.append(f"| {r['report']} | {r['due']} | {r['status'].title()} |")
            lines.append("")
        all_reports = []
        for gid, reports in REPORTING_REQUIREMENTS.items():
            for r in reports:
                all_reports.append({"grant": gid, "report": r["report"], "due": r["due"]})
        all_reports.sort(key=lambda x: x["due"])
        lines.append("## Upcoming Reports (All Grants)\n")
        lines.append("| Due Date | Grant | Report |")
        lines.append("|---|---|---|")
        for r in all_reports[:10]:
            lines.append(f"| {r['due']} | {r['grant']} | {r['report']} |")
        return "\n".join(lines)

    def _budget_tracking(self, **kwargs) -> str:
        grant_id = kwargs.get("grant_id")
        lines = ["# Grant Budget Tracking\n"]
        grants = {}
        if grant_id and grant_id in GRANTS_PORTFOLIO:
            grants = {grant_id: GRANTS_PORTFOLIO[grant_id]}
        else:
            grants = {k: v for k, v in GRANTS_PORTFOLIO.items() if v["status"] == "active"}
        for gid, g in grants.items():
            rate = _burn_rate(g)
            available = g["amount"] - g["spent"] - g["encumbered"]
            lines.append(f"## {gid}: {g['title']}\n")
            lines.append(f"- **Award Amount:** ${g['amount']:,.0f}")
            lines.append(f"- **Local Match:** ${g['local_match']:,.0f} ({g['match_required'] * 100:.0f}%)")
            lines.append(f"- **Spent:** ${g['spent']:,.0f}")
            lines.append(f"- **Encumbered:** ${g['encumbered']:,.0f}")
            lines.append(f"- **Available:** ${available:,.0f}")
            lines.append(f"- **Burn Rate:** {rate}%")
            lines.append(f"- **Period:** {g['start_date']} to {g['end_date']}\n")
        lines.append("## Budget Category Reference\n")
        for cat, desc in BUDGET_CATEGORIES.items():
            lines.append(f"- **{cat.title()}:** {desc}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = SLGGrantsManagementAgent()
    print("LIVE TENANT GRANT CASES (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="grants_portfolio"))
    print("\n" + "=" * 80 + "\n")
    print("EMBEDDED DEMO PORTFOLIO (works offline)")
    print(agent.perform(operation="grants_portfolio", grant_id="LG-2025-001"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="application_status"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="reporting_calendar"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="budget_tracking"))
