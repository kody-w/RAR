"""
IT Ticket Management Agent — a template you are meant to mutate.

Intelligent IT ticket management with dashboard views, priority
assignment, SLA tracking, and resolution reporting. In this template a
Dynamics 365 CASE (incident) is read as an IT ticket — same triage
shape, different label.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live data over real HTTP from TWO sibling
     systems (synthetic data, no credentials, works from anywhere):
       CRM — the Static Dynamics 365 tenant (Aster Lane Office Systems):
         https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       ITSM — the Static ITSM desk (real ServiceNow Table-API shape,
       30 INC records):
         https://kody-w.github.io/static-itsm/api/now/table/
     Try: perform(operation="ticket_dashboard")
     — the dashboard shows the CRM case queue PLUS the live ITSM desk
     with real INC numbers, and joins repeat-CI clusters back to CRM
     cases: INC0010001 + INC0010027 both hit "Lakeview University
     Benefits Portal" and join to CAS-260137 "Open enrollment benefits
     portal login failures" (Lakeview University).
  2. No network? Everything falls back to the embedded demo layer below
     (_TICKETS / _TEAM_CAPACITY) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     IT_TICKET_MANAGEMENT_DATA_URL to any OData-shaped endpoint and
     IT_TICKET_MANAGEMENT_ITSM_URL to any ServiceNow Table-API-shaped
     endpoint (your real instance exports), or replace the fetchers
     with your ITSM client. The fields the rest of the file needs are
     listed in _normalize_live_ticket() — team and users_affected are
     labeled "n/a — enrichment seam"; wire your workforce and asset
     systems there.

OPERATIONS
  ticket_dashboard | priority_assignment | sla_tracking
  | resolution_report
  kwargs: operation (required)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timezone

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/it_ticket_management",
    "version": "1.2.0",
    "display_name": "IT Ticket Management",
    "description": "Builds ticket dashboards from live D365 cases plus a simulated ServiceNow-shaped ITSM desk, joining repeat-CI clusters to CRM cases; offline fallback.",
    "author": "AIBAST",
    "tags": ["it", "tickets", "helpdesk", "sla", "priority", "resolution"],
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
#   export IT_TICKET_MANAGEMENT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your ITSM client. Downstream code
# only needs the fields produced by _normalize_live_ticket().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "IT_TICKET_MANAGEMENT_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
# Sibling system: the Static ITSM desk — real ServiceNow Table API
# shape ({"result": [...]}, INC numbers, reference fields as
# {display_value, link, value} dicts). Point at your own instance:
#   export IT_TICKET_MANAGEMENT_ITSM_URL=https://your-instance/api/now/table
ITSM_SOURCE_URL = os.environ.get(
    "IT_TICKET_MANAGEMENT_ITSM_URL",
    "https://kody-w.github.io/static-itsm/api/now/table",
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
            rows = json.loads(resp.read().decode("utf-8")).get("value", [])
    except Exception:
        rows = []
    _LIVE_CACHE[collection] = rows
    return rows


def _fetch_itsm_table(table, timeout=6):
    """Sibling fetcher for the ServiceNow-shaped ITSM desk. Same rules
    as _fetch_collection — lazy, one bounded GET, [] on ANY failure —
    but parses the Table API envelope {"result": [...]} and caches in
    _LIVE_CACHE keyed by full URL."""
    url = f"{ITSM_SOURCE_URL}/{table}.json"
    if url in _LIVE_CACHE:
        return _LIVE_CACHE[url]
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "rapp-agent-template/1.0"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            rows = json.loads(resp.read().decode("utf-8")).get("result", [])
    except Exception:
        rows = []
    _LIVE_CACHE[url] = rows
    return rows


# ServiceNow incident coded values -> labels (Table API returns codes).
_SN_STATE = {"1": "New", "2": "In Progress", "3": "On Hold",
             "6": "Resolved", "7": "Closed", "8": "Canceled"}
_SN_PRIORITY = {"1": "P1-Critical", "2": "P2-High",
                "3": "P3-Medium", "4": "P4-Low"}


def _sn_display(ref):
    """ServiceNow reference fields arrive as {display_value, link, value}
    dicts (or "" when empty) — extract the display value."""
    return ref.get("display_value", "") if isinstance(ref, dict) else ""


def _itsm_desk_section(limit=10):
    """Markdown section for the live ITSM desk: active incidents with
    real INC numbers/state/priority, plus repeat-CI clusters joined to
    the CRM case queue by company. One line when the desk is offline."""
    rows = _fetch_itsm_table("incident")
    if not rows:
        return ("**ITSM Desk:** unreachable — live ServiceNow-shaped "
                "desk section skipped (simulated fallback above is "
                "unaffected)\n")
    active = [r for r in rows if r.get("active") == "true"]
    active.sort(key=lambda r: (str(r.get("priority", "9")), str(r.get("number", ""))))
    inc_rows = ""
    for r in active[:limit]:
        inc_rows += (
            f"| {r.get('number', '')} "
            f"| {_SN_PRIORITY.get(str(r.get('priority', '')), r.get('priority', ''))} "
            f"| {_SN_STATE.get(str(r.get('state', '')), r.get('state', ''))} "
            f"| {r.get('company', '')} "
            f"| {_sn_display(r.get('cmdb_ci')) or 'n/a'} "
            f"| {_sn_display(r.get('assigned_to')) or 'unassigned'} |\n"
        )
    more = f"(showing {min(limit, len(active))} of {len(active)} active)\n" if len(active) > limit else ""
    # Repeat-CI clusters: >1 active incident on the same configuration
    # item, joined back to the CRM case queue on the shared company.
    by_ci = {}
    for r in active:
        ci = _sn_display(r.get("cmdb_ci"))
        if ci:
            by_ci.setdefault(ci, []).append(r)
    crm_cases = _fetch_collection("incidents")
    cluster_lines = ""
    for ci, hits in sorted(by_ci.items(), key=lambda kv: -len(kv[1])):
        if len(hits) < 2:
            continue
        nums = ", ".join(sorted(h.get("number", "") for h in hits))
        company = hits[0].get("company", "")
        related = [c for c in crm_cases if c.get("customeridname") == company]
        if related:
            c = related[0]
            join = (f" <-> CRM {c.get('ticketnumber', '')} "
                    f"\"{str(c.get('title', ''))[:45]}\"")
        else:
            join = " <-> CRM case: none found for this company"
        cluster_lines += f"- {ci} ({company}): {nums}{join}\n"
    if not cluster_lines:
        cluster_lines = "- No repeat-CI clusters among active incidents\n"
    return (
        f"**ITSM Desk (LIVE ServiceNow-shaped incident table — "
        f"{len(active)} active of {len(rows)}):**\n\n"
        f"| Number | Priority | State | Company | Configuration Item | Assigned To |\n"
        f"|---|---|---|---|---|---|\n"
        f"{inc_rows}{more}\n"
        f"**Repeat-CI Clusters (joined to the CRM case queue by company):**\n"
        f"{cluster_lines}"
    )


# Dynamics case priority has no P1 tier, so the mapping is deliberately
# conservative: High -> P2, Normal -> P3, Low -> P4.
_PRIORITY_TO_SEVERITY = {"High": "P2-High", "Normal": "P3-Medium", "Low": "P4-Low"}


def _normalize_live_ticket(row):
    """Project a Dynamics case record onto the ticket shape this agent
    uses. THIS is the contract your replacement data source must meet —
    a dict with these keys. None means 'not available from the case
    alone' and renderers label it as an enrichment seam."""
    priority = row.get("prioritycode@OData.Community.Display.V1.FormattedValue", "Normal")
    severity = _PRIORITY_TO_SEVERITY.get(priority, "P3-Medium")
    return {
        "id": row.get("ticketnumber", row.get("incidentid", "")),
        "subject": row.get("title", "Untitled case"),
        "category": row.get("casetypecode@OData.Community.Display.V1.FormattedValue", "Case"),
        "severity": severity,
        "status": row.get("statuscode@OData.Community.Display.V1.FormattedValue", "Open"),
        "assignee": row.get("owneridname", "unassigned"),
        "team": None,              # enrichment seam — wire your workforce system
        "created": row.get("createdon", ""),
        "sla_target_hours": _SLA_TARGETS[severity]["resolution_hours"],
        "elapsed_hours": _hours_since(row.get("createdon")),
        "users_affected": None,    # enrichment seam — wire your asset/impact data
        "customer": row.get("customeridname", ""),
        "_live": True,
    }


def _hours_since(iso_date):
    try:
        then = datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
        return max(0.0, round((datetime.now(timezone.utc) - then).total_seconds() / 3600, 1))
    except (ValueError, TypeError):
        return 0.0


def _open_tickets():
    """Live open tenant cases as tickets, else the embedded demo queue.
    Returns (tickets_by_id, is_live)."""
    rows = _fetch_collection("incidents")
    live = {
        t["id"]: t
        for t in (_normalize_live_ticket(r) for r in rows if r.get("statecode") == 0)
        if t["id"]
    }
    if live:
        return live, True
    return _TICKETS, False


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_TICKETS = {
    "TKT-8001": {"id": "TKT-8001", "subject": "Email server degradation - 847 users affected", "category": "Infrastructure", "severity": "P1-Critical", "status": "In Progress", "assignee": "Sarah Chen", "team": "Network Team", "created": "2025-11-14T08:15:00Z", "sla_target_hours": 1, "elapsed_hours": 0.5, "users_affected": 847, "description": "Exchange server memory at 98%, automatic restart needed"},
    "TKT-8002": {"id": "TKT-8002", "subject": "VPN connectivity failure for Finance dept", "category": "Network", "severity": "P1-Critical", "status": "In Progress", "assignee": "Mike Torres", "team": "Network Team", "created": "2025-11-14T08:30:00Z", "sla_target_hours": 1, "elapsed_hours": 0.25, "users_affected": 234, "description": "VPN profile corruption affecting Finance department users"},
    "TKT-8003": {"id": "TKT-8003", "subject": "CRM system timeout errors", "category": "Application", "severity": "P2-High", "status": "Assigned", "assignee": "James Martinez", "team": "Application Support", "created": "2025-11-14T09:00:00Z", "sla_target_hours": 4, "elapsed_hours": 0.1, "users_affected": 156, "description": "Dynamics 365 experiencing intermittent timeout errors"},
    "TKT-8004": {"id": "TKT-8004", "subject": "Password reset - batch of 12 new hires", "category": "Access Management", "severity": "P3-Medium", "status": "Open", "assignee": "Lisa Wong", "team": "Desktop Support", "created": "2025-11-14T09:15:00Z", "sla_target_hours": 8, "elapsed_hours": 0, "users_affected": 12, "description": "New hire onboarding batch needs initial password setup"},
    "TKT-8005": {"id": "TKT-8005", "subject": "Printer not working on 3rd floor", "category": "Hardware", "severity": "P3-Medium", "status": "Open", "assignee": "unassigned", "team": "Desktop Support", "created": "2025-11-14T09:30:00Z", "sla_target_hours": 8, "elapsed_hours": 0, "users_affected": 35, "description": "HP LaserJet on 3rd floor showing offline, paper jam cleared"},
    "TKT-8006": {"id": "TKT-8006", "subject": "Request for dual monitor setup", "category": "Hardware", "severity": "P4-Low", "status": "Open", "assignee": "unassigned", "team": "Desktop Support", "created": "2025-11-13T16:00:00Z", "sla_target_hours": 24, "elapsed_hours": 17, "users_affected": 1, "description": "Employee requesting second monitor for productivity"},
    "TKT-8007": {"id": "TKT-8007", "subject": "Software license request - Adobe Creative Suite", "category": "Software", "severity": "P4-Low", "status": "Pending Approval", "assignee": "Lisa Wong", "team": "Desktop Support", "created": "2025-11-13T14:00:00Z", "sla_target_hours": 24, "elapsed_hours": 19, "users_affected": 1, "description": "Marketing team member needs Adobe CC license"},
    "TKT-8008": {"id": "TKT-8008", "subject": "Conference room AV system not projecting", "category": "Hardware", "severity": "P2-High", "status": "In Progress", "assignee": "Mike Chen", "team": "Desktop Support", "created": "2025-11-14T08:45:00Z", "sla_target_hours": 4, "elapsed_hours": 0.3, "users_affected": 20, "description": "Board room projector showing no signal, executive meeting at 10 AM"},
}

_SLA_TARGETS = {
    "P1-Critical": {"response_hours": 0.25, "resolution_hours": 1, "escalation_after_hours": 0.5, "penalty_per_breach": 500},
    "P2-High": {"response_hours": 0.5, "resolution_hours": 4, "escalation_after_hours": 2, "penalty_per_breach": 200},
    "P3-Medium": {"response_hours": 2, "resolution_hours": 8, "escalation_after_hours": 6, "penalty_per_breach": 50},
    "P4-Low": {"response_hours": 4, "resolution_hours": 24, "escalation_after_hours": 20, "penalty_per_breach": 0},
}

_TEAM_CAPACITY = {
    "Network Team": {"members": 3, "current_tickets": 4, "capacity_pct": 72, "skills": ["Infrastructure", "Network", "Security"]},
    "Application Support": {"members": 4, "current_tickets": 6, "capacity_pct": 65, "skills": ["CRM", "ERP", "Custom Apps"]},
    "Desktop Support": {"members": 5, "current_tickets": 18, "capacity_pct": 88, "skills": ["Hardware", "Software", "Access Management"]},
    "Database Team": {"members": 2, "current_tickets": 2, "capacity_pct": 30, "skills": ["SQL Server", "Azure SQL", "Performance"]},
}

_RESOLUTION_HISTORY = {
    "this_week": {"resolved": 89, "avg_resolution_hours": 4.2, "sla_met_pct": 94.2, "first_call_resolution_pct": 67, "csat": 4.5},
    "last_week": {"resolved": 94, "avg_resolution_hours": 4.5, "sla_met_pct": 91.8, "first_call_resolution_pct": 62, "csat": 4.3},
    "this_month": {"resolved": 312, "avg_resolution_hours": 4.3, "sla_met_pct": 93.1, "first_call_resolution_pct": 65, "csat": 4.4},
    "top_categories": [
        {"category": "Password Resets", "count": 58, "pct": 18.6, "automation_candidate": True},
        {"category": "Software Access", "count": 47, "pct": 15.1, "automation_candidate": True},
        {"category": "VPN Issues", "count": 38, "pct": 12.2, "automation_candidate": False},
        {"category": "Hardware Requests", "count": 35, "pct": 11.2, "automation_candidate": False},
        {"category": "Email Issues", "count": 29, "pct": 9.3, "automation_candidate": False},
    ],
}


# ═══════════════════════════════════════════════════════════════
# HELPERS — real computation, live or embedded inputs
# ═══════════════════════════════════════════════════════════════

def _tickets_by_severity(tickets):
    by_sev = {}
    for t in tickets.values():
        by_sev.setdefault(t["severity"], []).append(t)
    return by_sev


def _sla_at_risk(tickets):
    at_risk = []
    for t in tickets.values():
        if t["status"] not in ("Resolved", "Closed", "Cancelled"):
            sla = _SLA_TARGETS.get(t["severity"], {})
            remaining = sla.get("resolution_hours", 24) - t["elapsed_hours"]
            if remaining < sla.get("resolution_hours", 24) * 0.3:
                at_risk.append({**t, "remaining_hours": remaining})
    return sorted(at_risk, key=lambda x: x["remaining_hours"])


def _team_workload_summary():
    total_tickets = sum(tc["current_tickets"] for tc in _TEAM_CAPACITY.values())
    total_members = sum(tc["members"] for tc in _TEAM_CAPACITY.values())
    return total_tickets, total_members


def _queue_source_line(is_live):
    if is_live:
        return "Queue source: LIVE cases from the Aster Lane Dynamics 365 tenant"
    return "Queue source: embedded demo layer (simulated — live tenant unreachable)"


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class ITTicketManagementAgent(BasicAgent):
    """
    IT ticket management agent.

    Operations:
        ticket_dashboard    - overview of all open tickets and queue status
        priority_assignment - assign priority and route tickets
        sla_tracking        - track SLA compliance and at-risk tickets
        resolution_report   - generate resolution metrics and trends
    """

    def __init__(self):
        self.name = "ITTicketManagementAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "ticket_dashboard", "priority_assignment",
                            "sla_tracking", "resolution_report",
                        ],
                        "description": "The ticket management operation to perform",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "ticket_dashboard")
        dispatch = {
            "ticket_dashboard": self._ticket_dashboard,
            "priority_assignment": self._priority_assignment,
            "sla_tracking": self._sla_tracking,
            "resolution_report": self._resolution_report,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler()

    # ── ticket_dashboard ───────────────────────────────────────
    def _ticket_dashboard(self):
        tickets, is_live = _open_tickets()
        by_sev = _tickets_by_severity(tickets)
        sev_rows = ""
        for sev in ["P1-Critical", "P2-High", "P3-Medium", "P4-Low"]:
            count = len(by_sev.get(sev, []))
            sev_rows += f"| {sev} | {count} | {_SLA_TARGETS[sev]['resolution_hours']}h |\n"
        listed = sorted(tickets.values(), key=lambda x: x["severity"])[:15]
        ticket_rows = ""
        for t in listed:
            ticket_rows += f"| {t['id']} | {t['subject'][:45]} | {t['severity']} | {t['status']} | {t['assignee']} |\n"
        more = f"(showing {len(listed)} of {len(tickets)})\n" if len(tickets) > len(listed) else ""
        total_tickets, total_members = _team_workload_summary()
        return (
            f"**IT Ticket Dashboard**\n\n"
            f"**Summary:** {len(tickets)} open tickets | {total_members} team members (team roster is embedded demo data)\n\n"
            f"**By Severity:**\n\n"
            f"| Severity | Count | SLA Target |\n|---|---|---|\n"
            f"{sev_rows}\n"
            f"**Open Tickets:**\n\n"
            f"| ID | Subject | Severity | Status | Assignee |\n|---|---|---|---|---|\n"
            f"{ticket_rows}{more}\n"
            f"{_itsm_desk_section()}\n"
            f"{_queue_source_line(is_live)}\n"
            f"Source: [Case Queue + ITSM Desk (ServiceNow-shaped)]\nAgents: ITTicketManagementAgent"
        )

    # ── priority_assignment ────────────────────────────────────
    def _priority_assignment(self):
        assignment_rows = ""
        for t in _TICKETS.values():
            sla = _SLA_TARGETS[t["severity"]]
            assignment_rows += f"| {t['id']} | {t['severity']} | {t['team']} | {t['assignee']} | {t['users_affected']} | {sla['resolution_hours']}h |\n"
        team_rows = ""
        for team_name, tc in _TEAM_CAPACITY.items():
            team_rows += f"| {team_name} | {tc['members']} | {tc['current_tickets']} | {tc['capacity_pct']}% | {', '.join(tc['skills'][:2])} |\n"
        return (
            f"**Priority Assignment Matrix** (embedded demo data — simulated)\n\n"
            f"**Ticket Assignments:**\n\n"
            f"| ID | Priority | Team | Assignee | Users Affected | SLA |\n|---|---|---|---|---|---|\n"
            f"{assignment_rows}\n"
            f"**Team Capacity:**\n\n"
            f"| Team | Members | Tickets | Capacity | Skills |\n|---|---|---|---|---|\n"
            f"{team_rows}\n\n"
            f"Source: [Ticketing + Workforce Management]\nAgents: ITTicketManagementAgent"
        )

    # ── sla_tracking ───────────────────────────────────────────
    def _sla_tracking(self):
        tickets, is_live = _open_tickets()
        at_risk = _sla_at_risk(tickets)[:10]
        risk_rows = ""
        for t in at_risk:
            state = f"{t['remaining_hours']:.1f}h" if t["remaining_hours"] >= 0 else f"BREACHED {-t['remaining_hours']:.0f}h ago"
            risk_rows += f"| {t['id']} | {t['severity']} | {state} | {t['assignee']} | {t['subject'][:40]} |\n"
        if not risk_rows:
            risk_rows = "| None | - | - | - | All tickets on track |\n"
        sla_rows = ""
        for sev, targets in _SLA_TARGETS.items():
            sla_rows += f"| {sev} | {targets['response_hours']}h | {targets['resolution_hours']}h | {targets['escalation_after_hours']}h | ${targets['penalty_per_breach']} |\n"
        return (
            f"**SLA Tracking Dashboard**\n\n"
            f"**At-Risk Tickets** (elapsed time computed against SLA targets):\n\n"
            f"| Ticket | Severity | Time Remaining | Assignee | Subject |\n|---|---|---|---|---|\n"
            f"{risk_rows}\n"
            f"**SLA Targets:**\n\n"
            f"| Severity | Response | Resolution | Escalation | Breach Penalty |\n|---|---|---|---|---|\n"
            f"{sla_rows}\n"
            f"**Historical SLA Compliance:** {_RESOLUTION_HISTORY['this_week']['sla_met_pct']}% (embedded demo history — simulated)\n\n"
            f"{_queue_source_line(is_live)}\n"
            f"Source: [Case Queue + SLA Engine]\nAgents: ITTicketManagementAgent"
        )

    # ── resolution_report ──────────────────────────────────────
    def _resolution_report(self):
        tw = _RESOLUTION_HISTORY["this_week"]
        lw = _RESOLUTION_HISTORY["last_week"]
        tm = _RESOLUTION_HISTORY["this_month"]
        trend_rows = (
            f"| This Week | {tw['resolved']} | {tw['avg_resolution_hours']}h | {tw['sla_met_pct']}% | {tw['first_call_resolution_pct']}% | {tw['csat']}/5 |\n"
            f"| Last Week | {lw['resolved']} | {lw['avg_resolution_hours']}h | {lw['sla_met_pct']}% | {lw['first_call_resolution_pct']}% | {lw['csat']}/5 |\n"
            f"| This Month | {tm['resolved']} | {tm['avg_resolution_hours']}h | {tm['sla_met_pct']}% | {tm['first_call_resolution_pct']}% | {tm['csat']}/5 |\n"
        )
        cat_rows = ""
        for cat in _RESOLUTION_HISTORY["top_categories"]:
            auto = "Yes" if cat["automation_candidate"] else "No"
            cat_rows += f"| {cat['category']} | {cat['count']} | {cat['pct']}% | {auto} |\n"
        return (
            f"**Resolution Report** (embedded demo history — simulated)\n\n"
            f"**Performance Trends:**\n\n"
            f"| Period | Resolved | Avg Resolution | SLA Met | FCR | CSAT |\n|---|---|---|---|---|---|\n"
            f"{trend_rows}\n"
            f"**Top Issue Categories (This Month):**\n\n"
            f"| Category | Count | % of Total | Automate? |\n|---|---|---|---|\n"
            f"{cat_rows}\n"
            f"**Recommendations:**\n"
            f"- Automate password resets (18.6% of volume) to save ~22 hours/week\n"
            f"- Implement self-service software access portal (15.1% of volume)\n"
            f"- Investigate recurring VPN issues (12.2% of volume)\n\n"
            f"Source: [Ticketing Analytics + Power BI]\nAgents: ITTicketManagementAgent"
        )


if __name__ == "__main__":
    agent = ITTicketManagementAgent()
    print("=" * 60)
    print("EMBEDDED DEMO QUEUE (works offline)")
    print(agent.perform(operation="priority_assignment"))
    print()
    print("=" * 60)
    print("LIVE CRM QUEUE + LIVE ITSM DESK (both fetched over HTTP;")
    print("the dashboard joins repeat-CI incident clusters — e.g. the")
    print("Lakeview Benefits Portal pair INC0010001 + INC0010027 —")
    print("back to the CRM case queue; falls back offline)")
    print(agent.perform(operation="ticket_dashboard"))
    print()
    print("=" * 60)
    print(agent.perform(operation="sla_tracking"))
