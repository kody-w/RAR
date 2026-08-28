---
name: "rar-aibast-agents-library-slg-grants-management"
description: "Tracks grant compliance and budgets from a live simulated Dynamics 365 tenant's grant cases, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/slg_grants_management", "rar_sha256": "7f901350c900aa62b69b47e6e015847a8909265b1a0c1a68183c0757bddd1130", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["grants", "budget", "reporting", "local-government", "state-government"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/slg_grants_management`. The original RAPP
agent is preserved byte-for-byte in `grants_management_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "grant_id": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "grants_portfolio",
        "application_status",
        "reporting_calendar",
        "budget_tracking"
      ],
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `grants_management_agent.py` and embedded as the fenced Python below (sha256 7f901350c900aa62…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `grants_management_agent.py` first:

```bash
python3 grants_management_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 grants_management_agent.py   # or on stdin
python3 grants_management_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
