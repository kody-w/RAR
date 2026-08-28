---
name: "rar-aibast-agents-library-it-ticket-management"
description: "Builds ticket dashboards from live D365 cases plus a simulated ServiceNow-shaped ITSM desk, joining repeat-CI clusters to CRM cases; offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/it_ticket_management", "rar_sha256": "a640f23976da1b619888599c1ec678a51601e48530ba77a6f6ace15be383ef66", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.2.0", "author": "AIBAST", "tags": ["it", "tickets", "helpdesk", "sla", "priority", "resolution"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/it_ticket_management`. The original RAPP
agent is preserved byte-for-byte in `it_ticket_management_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The ticket management operation to perform",
      "enum": [
        "ticket_dashboard",
        "priority_assignment",
        "sla_tracking",
        "resolution_report"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `it_ticket_management_agent.py` and embedded as the fenced Python below (sha256 a640f23976da1b61…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `it_ticket_management_agent.py` first:

```bash
python3 it_ticket_management_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 it_ticket_management_agent.py   # or on stdin
python3 it_ticket_management_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/6276a7jRrYm+ipC9o9jN52WSFEU6YO+3ZznUaQo8rrh4jzPk6jqevcb2rmddh0XCmjgbmQmJCpixRq/9a2dob9/CZY578Yvv3whRYq82V9++hInUzQW/Vx0LXhMLUUdT4e5iKpkPsTBlIddMIIn6dg1h7pYkwNzxi6HKJiS6dDXy3QIDlPRLHUwJ/HhloxrESVat32d8qAHT0T7ph7AGdVPh7Ir2qLNDmPSJ8H8lRYPEdg/JyM4rzvQlvpN6n8eujStizY5pEFdh0FU/QzUTJ5B09fJ9OWX//d///SlAK+//PL3L1EdTODRF9G2PzRWgzbIkiZpZzID/4B9ddBmYEG/A7tb8L5PxrQbG/AoTtLD57sfpqROfzr89/9ebcGYTT8evv4/h2kef/m1PXz+dP3hfxy+ffpzlsw//PqlA3uDt9d+/fLT4dcv3zz223eP/frlxz92x8XUB3OUAxl//+Pp++dfbfzl8Fbn59/+6yc//det/Vh0YzHvvwEnFFn7NvuP3f/iw78ImOrgt3kEHgZh+WPnn5/+ZcuYTF29vO3+DcSxG/904l8++tPmf/zxMg/auE5G4Ivf3fLh0a7/k8OK9NB28+9Lf/lnJcZkXsb2kP76xWmrttvaw/dY/HL4e9f/49cvf2z4XPwp6Ycfv/wDZE8LgrtE7w3v5Plv/+2gFtHYTV06H25Rt8yHcWnnokl+bX9t7byYDuDPnCdA2AqytQjr5HNdP3Zl8iEIJO3hb/8rKMJgmr8G7+SbvtZFOAbjfizm32PZfM/Pv/18sIFEEKKsaIP6YJGG8Wv7sfF9Wg+cCWoJFFC4z8lXkKRf3y8ORXv4278S99vHzp/7/W8HYOl72Vtf611jQT8tdfLz2xY3T9pPzaOgPSTPJFqA0LqLgAZpAcrrp8NHFEGZz2+7p6qoaxCnERjZjfuHbOCbX97C/va3vwFj81/bb7V1PnzDkekIFnxX5/D1KzAFlHOWz7+2SZR3h//4+z/+4/B/Dv9u14fw9xkGSN5PzwMNpZuuHUAJLm+LQVBAGJMg/vD83//x6VAgpgXJBeJUpEXybTMAkyqJf/fuTSC/IhfsECbAq8CjzTtV37hUzD8fxPTwXd/Dtyx+I1zeTQANAW61cdJGO5AaAHO+e/KdqxNIwCndfzosU/Jx6t9A8D9UbH6LwPK/HVTaAEDX1W+0A2p+LAKbu7YA7v8e+2/PgZDxP6YD9buInw/aO/cOfTAGfT4Gn2ekwbe4dOPh9+1AeHBok+3X9g2SH8nxURrf3AMWAc9EnyH9+o75IeoakEjx9PvZH2s+4Nzugjc+/9pOn0kejO9QRB1QZT9kSxEHbZT852dKTXm31PGH/4Cmb0mfUYg/o/KRg6J9+IbVhz/A+vCB1odfF+QEo0B9YHD/biiHvVs+zmySAHwOTGsWYM23ZBbbOalBoN47gdDPlvVHSRy2Ys7/aGGHtUg2kN+/4yJw+B/AeLgp5OE75n1L8+9o9pkH4BOQH+23wviuYfBry+xt0BTRdHg3Rpq8sYcfijYqQKbMP75reXwnaQDSqP2Tnp+2TkEDIjkWQGfg5XfL/AnEJgUOfFtQB2FSfxgr6O7BFsTbwWZVQyFt9uDqlnx74xz880EH3gdV8HZ52D1BIh/6pa6nb/06Dubg8I7YtyISbNv41s1tVz+8wewN/t/wctrfuTYdfpj2Fgib34kCdv8EwPgQjcnboiKogRO3bqw+OUHQ7lsO1P3xD5R+t/JP+94q3d4JGB3+yU1z0r4j+gP5zq+DEoBur6cpoA6H2zcdfvwz6Ofz3E+/HI9VF+9ft58zENgl/LnojtOH6K/xp+ivQPQx6IvjW+vjSvyMHL9L+SAif9XqOz85/PDhnj8YzMEOANB/JQ3x8C0w30WdTwdRoz8KAVCj/ytNi3lqPjQEfes4vw/4XUN73H/5zke+N7T/8e+YxZ+s+SPNQRVu32Dvd0Z1GJZkSQ6G4tw+4RBkxXe7P2V9FMuHB96mtUsTgk73rRLevG36V6ztzc0+qdunlA8C98tbxOkEn8DfA/T9DXIFyQkOyUF6/vpFCarkXZEHpy0+muq7Ij9kUAB+UuCngwGKDgDjl+9KfJxF3r4i2Ak+X4EQHQDyIWnHrq4/Kj783Popqf8QANobaLEAKot6AUUN5P3wLw7/8ef3JgTgbAfQc34n+P88sG+cA/UOmsObi/5h8duNCXBRHANwi5OmA6W6g0QG5dptn6f/8Jst0jJr3w7Hw282S6q/0aRB0qLt/fjnyH3D7fYD3SMA7DloWp8E+EOl888AKKvkXdQADYHXg/ljnyLe2QND2uThBmR/O/nNxObP40X78/zfVFIjeVZlNfu39/rfHEt52wAK96AzoFB+p+qgufXAy/Pb3/9OyDt1/izkX5XMp8xPMd8l//A24Vuavfvau3sAFvLRZX/86d3FQJbVQfTZ3BLADUF0/pyhH/s/cjeqizdZ+OhqoMd8TC0fRGH6joUf3a1NEvARaCKfYupierc2kBG/taDUgrp4Jb+9S+KTVP3wR3SSoPnIvXcznn4LACpH761/kvXGZ/Dk1y/tMfh9G8jHIso/8nECEn798p9A9TH5pvo7r0CFAwvfgkEH+h6v37F3foPpB+brBmuRtqhrHzD/X2HgTaH+SvHB038i9WDj/zn8lbODx9+GmV/+4M5vABwWoGn843tuAhEFbf/LLy3oJD99Afia/Ns5601MmuQNC++5DPBiIHYuko933494v/nnefMdvb927j90Ain2+8QGZkAAS2D++wsivo//qyvA0z+7Arz9ix++gFFy3vu3ZWAieC/6xz/ey7654X3UH6r/sbQL35z/PUi8KcC3afLvX4DxwbvtfJr/ORaA5WAE+Dq9CdIR/vn01iIYvxFd8Nn/xcDwuRPUFSCvYGuAoacUORNXLA7gEIMJHMcvBBHBSYRd8eACA5BMUPxyPoXB9RpgKQbqCr6EyRk/JymGvd0DMjJKfnvzv+KtzQkmUAxNgjNyOSNEeIkTjAjRIMUIcAqRXuALnCAIjPyxFTg2/jTxm0lv/32fXd6u+LT0719CDAUrBXQSyW8/9JE4EdeHUmq9cjxaZncZvSm5WUG1nPzyqiRl5LvqfEVNZO6rqcPk3JtNyy+L2kY971icYgfa1rOX4BxRLfNC0hbp5FfD149IVZu3286YgWCeoWzS9lGexli1+HNj6xdsi17xFh4bmtra8ZyA84/tOX3RD+mxPwkNYSfY9dQyLUKVixOpYEOJbU78ZQ39E0+nMVFuHrWyNulC9iaMz+o1+Iuh4NLZLeVreYZYJvXUVaF3dnZdBI2Sa0QRzb6h98aQfPa6pDqNbP4r2xsloV5YkMgc+XhGec3SNvJE+JGqrpNzSZaru9/6jSPQym+nlSHyZ0jkrXaDvITTSRdJTS1RllqpnqTmbk/2wV87hekpLFueD+N8u6+TXJ2bIytGaRrz0JURZyJJJ4IPT5AQauZRuLxgqz0jx+Rxn3F1fs4dspw2m5tQUsQvy7am6o3IdiJFPChGiRx1WiVb18QzPUh/zQFjZdOeR5MmnOv9hYTt02NFmkoh6c7oi+Te4IQyScWRbYqxAjakpOdDbFuoorH8RWPF5pganBEvUrgndUp6+gvF+t3N40zNHId83ihty4zKk09CdXpML/KELpeXtpLtiVuNtqOKUMKr/bpcl3P3sO+pQa3ZXe/LBOGgK08p1aX26ZAU2sfjMVwLg1mO7nKdsIVsRYyXvFsXRmOpw17ZZc9LTOLeQzSNULcTSHn5/GXbN3Pi/OHI2QWkZ15gq1IPsd0lYQtcnHcKR9iTuarWzMkIFqpN6VrZHBQcHnGCWhZbzp/QZrr7McElys46l7aLDDV0cvgWLy+tNWQHv/CXneBh8Vo4NPIgeYHI9JmHI6cXp1CY7jTS4vJqUlwcgXYq1Phe+FDR7DJinic6fsKqiJNZb3APzzaD8R7iFHGtHud+JcVLzrSNKLZu81iFKFqe8SZk7OSiF7Ok+ed14y1aYFzqsYTYXXSYFyGG2mua3QTC79OOPQyexAtWSfsjjItbJKvsFLzS18ZVof5QCcOL5mDkPJCbCC9aSPjwTJA9tYz7hC9csNmjcWF+kZ6GwoF8lw0SaRrnhXJoAdOIOI0VV3olxDONMjYlixkrhBh5sz/0QIOuxHa5ZjD2xJJSgDp/gl+32yYIjF1ImaDi+XjCMvgssD5I6pedAgMJ+tnptH5qNP01EcoE6VCjJc0mRqpbPazw5bOTPPuvQE+ImFCufXuMViu7IDFxidubgEz00b+Y9ZQXgYRbdqfBJzq09ArP1c3hrBPPOVcTFR2HkVEtstKCeoiOLvKTbFwSyNIfPLSxFEQNncU/NEyVnprJX9mmYm6RJDyK5ES+GhTZOjwlBot6evzSXJogeaF8J1AY5ViUmZIEG5uDre4JKSQP7FwcIzOtz08xGG6Bv8UnvqingMx0ne77c7ZQmz7Uz24Spbg+BSQmAKzz6oQR9VnZhLwgF9bx8uyIyztL3zx2cvLe2WxYxLINxOcYrAlm2DvZ3pHIS17MpbpErfSiZOR5fY2yMPEoc+kuUWdeQHZfqVeC5SHiDRbjBCXUAj1Oa+NSdXzeuTm7R6akP7l1g2EM22OQYivbDaG73UM7Ow5Lr8DqSq4PeYKOi+09jwGKMYSQRHrJuFNzGqErvudX7j4ixFx5PBq52op2eSxqHJqd4OpC3QsDv+cdg7WsVb745/wgye1hsvSYvSpa3dvroONavh6PkvlC4dl7XCUA9XfoeH7g1BEDEKZSmQhjKq+/xBN2vG4Et6a1q5Mo5mmbpusZevU66KQHm6etR3oOR7WYX/VUtbcpXhD34m3z05cF+0rs651Mc8USXYx+sNYyayPMjk3dxi/FOWkS7EVU2VzD1npVsDhTGpfoZH2uE9cnEnuXVt4p0PApGbFEde2CBIEjWFSIUMwpVLt6AiGzBS31XOyGckEQ0LWL6YohMKF0DoRpsGVsmzNlqPG+qSSOZhFn9LXTqfEiC52raxqrYVlbV3S+8iehnxOznu1IhJ4d8boWxDNeN5XOwqOsI0x7Vu8eeqpHspouTKDey0yZAISXMtRAdsVZ5jzIRxYVbVbi0OkkcnSRwRY3RTqT4FbbUqz/Yka0pnSDfu1Hs249ODU5ezwmUHmerqIIS9jxuN0RmScVlcLB4HwlQxc+kgOlQhGsHjFf4Zbjg+ERhigmmFFbzVjiwD9uF1IbR18sSfL4OBryDX2uontkaHy9KRu1lXGClwHhmUZ2u2/C8NxoeuFjk6lxWiNZaFZ59IkFS4GqnqYsBoTUAt0ceZOFN6h0CQ2nysV76bq56aD1kBEXZEhBq/Ex0/yNtFv21vlumnO6HpFi1pxJt5r32mXDXJPAm4Zw+eeJh17RmsAzaPZCvWBraaw1bCHl4N1mzLFKb75S4mQtqS89gr3H09LkWX2mdlmVNDmxY6wn1fgU13c1JInNzCRZnoiukOnRE7DsGs5TOuZ5q1vSk8bYlo+YhN+8o8zM+zXNRojESMbtC2ikhaktzA7NjFymk0tJLwaxGMVoPTvn+ronjKqfZUVv8SrSYu7V3FXdRKueWbqm4Bb9fAwtY9ChNpX8pxcqxjas8mm3ARLsTOa1+EshL6waeIp9sh8QG93OSk5QD0RgbWGKkAWSJL7io8RG+DWqMe6FmyzVXNkUqmd32Sp0zkmAaoPPiZE3mra4imxWZF7VPxG9nMXiufYVpIsOcCnzPJWADBzjGjaaXj1bsngKH5Cx6ZpNpvc1l47BuaZJLS4My0POgN6pXkLMs1DO1sg3TH3ud/pioUdXJxjZfsimbSX9kD5HvH+4UEphRNc4XsYxEDnkpkdRZoRiUJjoQ44jp1EaUUrKHwsvHgUlZAi4f6gqpC3BZtKzrruj2/ROM0FevhhdNeT+LLZkNk4RLaQXaOsjCSPU1FUs3toEwu0plDw2OXkMw1Oec+ftfLFkDrlJ+UgYhHy6W4G1BbEvUBIOeOGL35Cn/Ixqo488knLk5iSxVZoeXYdDfbU/enA0C+5TqrJzEMlu2N0WsZCtwPZEFcIvajfcNWrl6lw7Z2PFKHt2K+Pzs7apciLsM//+VXWGkPiJAtN+QHcZl0uCJOl3K6TG+bjVGHUdiaE60elziJVjiq+dn0RQe7+VqB0p+iXFRN/sfVuaL5W8Pd3XpSdYuJCa+b4n4lDX0y325hvcJjqrWpcMo0p4nX1B5I4bZaSoTjkmxZ/sXLntYtaZRKhMKqKtJqCVDhdqCTqpY0kZZBLZyXhlcoQkSjx1zXVQKBzjcvuuGmOFruPpIhjQ7cUQo+ZtGbaSNc8+ZcUMwCgzLjGHpOzNbMrtfn21LETEIlsSQL/1XLlGXfio1zEW0aOeRqinTbyw0bKYlpVzZHzDfetoSgygOiTs0Lz7tK5NI9WRAjy10+cncSkm1qpw2inU1yOovAJJ6bR69pMKu49HVNyxySD9yBK1ZrS1TOUT7/VkRylxAfkYpN47I6vnPgTlHkLBaJyTfClyTL1KYm+81OeZdwEGgs7k9b1zAlTK2Z66ZeF31FUZS3jes9vGawtd0kHuUEqtMG6nkNmjRrBtyluMedoZWyFcbsbtSV1evVVJTxsd3I1SxBtuXypGENm9S0+NAQd7LNxHgg4ukI8mNRk8X+qQxua5i4c7j7Cc7ytZbVjxFX3Vc7HCXXLEFrENq7N4F9Exk29U0Vluij8rI1fqjpFZBhT6clcHNLlbjgRZFG42A6DKBltWMv/U5kDfHGjOHicUn8/cK7Zqx4q2GyYHgowAroLPth73zOZec+dFG6hcbdHNIqQ02inSVuHL+WaGgh7xL/EG6a7GSdBEJk/XDr1Rmal5TcYBVyhZgpZsyEW7aRCk872ymLqxJ0TAMYvKzUA4uULoS8kufRsdYQdaLcI3o1kqE51SDZM3uuV5npZ5NYTbcHu2r0GS2YDJxZrfBDl/4syAkCgHwHC3mw69VTeoSgz6BA2sRl09puOsM5+j3kYEBTzu7ubcfYu7WixzQ01TrRHOOZ8ooSUs/Wz7LdFzvacuLHTB9ZyPc1VQlxPMWfVC4xF5D+iC6PKjw1E3JSu1swgVXSw+txX2SS8X+ruYr8oYOoPz7G8vRRqWFNBGL2yXWj7RAF8kvd91wZFy7EIzPqrZuwcX4jPJxVmQWNiQB3FhJIKrFk7k27ZjuilkedbAU0bjMjlsO2g0q6jirSdzs7zTJp0J+Oxachif79D5eX7MKqfu7C7cEeDJJ7zdJ9p+Zr3VlgBhaBPHSZm2yVcLr/KTotXp0lUpGUG9dM1ILxWYmK8mrEC8p6sZiTkktN3vYnwz2FZ8iXRZJTfKWRLdAj1UU+haoQV9VWqLVOjTfbWZjczFpxCzpNQ0z2ayIRpBXZrYi+ZM+X6HRSc3xLT0aiZOHFfiU0sH/zFe1yuVGEi5NmN0I06DIohRZNSxKiQeaFqopfUXBQ6UV84++yTjho5sRpULJ2Ior8q+xERVqm1KFIw+gzIoKeXWUZ29UBNNPizNcIspIs+Rlb1/cZY/B7Zx8/ksDUEYBPCt8N0RTJWWJKn5vAQ3egBzZAMTJAS7ggVGnCM1Do0l3K9m+qwEnLxys8cajaIXk5F6e3OF2Na+L5uj5acTMZj0s3/1+aZE/qj5kH/0r3fOfx2dElsWGHpYrUQk4xMd0Dl6zck81uwwwVKpegsVGFh+o3y+bsjhMcn9wjyfOxtqVNMYl3XQXio5mhGf38y1aISO3A0pbI5kWWSmzZRXSV78pOw9aNsxxiKdkmRuxBHhsw1P1gFlEF6Z1lHHNNEnxuPon1iWMnvsRZIU47A9ZXaeyN1Yer77j506X0uCuRmmPfBGw1VZhlUMeWKzfcfVvPKXKnWS54CWtGkbfteOAntij3ItyhxvJ+1FiWLdHKtVMelJkEjQVbh6d2izWctMpNgEpwWVZGZhUCkToQZxlzcXIZlkTJbLxUBQWh/4XN64kcRl4TUPz5kuGMQCDzGKV1j2nYkCq591QsV9e+JHrKLyJq1cgTaCp57pu43az1khRgTGy8kyzEGDeoeN9htUXHh6qig9l8tZq5Joz/EwWQL0LNgSOodgcnwRjFPbmtqOzjgnnNYHSWhdLm6roRl+Om2FcxTXbe3AkC8GUFPOqr6HVI7cal85LjWrFxh9R2/7krcaISdZE0teCw+n1BhZV7iXNv2KbwHK5Hi2q1dWKxq52kuN9yYwrbNiH/oFj4tLMUhCMhbDWulxoftO/iC1E3OTFanaJ7GI4aEh/dyaKQVJ9LvtbXveJKDyrSs0hID6oKOZXQAB0A3k8ZhMT3iIUs1wF4TqTEin6MnDqOQ56aY0Goklp8ITy0n/5l6FoZyLmDT5vKkaxDC3hwXmBDPzzZSwnuRcLL4qJqOCJ4q52Z0ymIsmcBCtpr117/y8uwTUsVRvYjYU08wjMI/CGAKJuze7AzEPWIy9zkqmEGdk9sN481Hl6gxzPYnG1gXBYOjbqYktv4KCFQFT1sJcG2OSMrpAFwS5XxV4Irv76ey0LMwuNcSJ96xzgo1O6nL1zVumVXfBpl6yeqJIFVM3q70wXKFJFRHksdEP80AutEC3rdLzVJ2yHt1tKBQIuk620EXjETIoGAFmHo3eQyL9wEwpmoETZQPhz7Ff9fOZIFPLDS6z2q5w6VR80fZWtmXnpXFZoxUX2QHGM1QhO3UW8ruJ6FXgEg9Ti8uHkjNrfBaS84s4nl74BfOhrTpeL5K9jseYPnrjvaCclJjPENpqztHvHaJDCOEVaS591K8lLtKX00k7B1JwNB+oLCuQKEpalC8XB2JxjWjzYzFbbRTtYVxtBUzpGdxWWX+RpJ1iel08TXCuKnyETH5ZwsUeaA+zjHFMN0NeNMtgd7WAkymtFo+v5CQjOuzWMNOPczzqhIF0cTxPQqeFkFTMQzEGzflWhGXvEye52OiQOVlDRQ4pAaltwrgY1s0mfWeHM5gwRhi18ODFwtQ5VnO998Wl5uiniXkJj3u23jhNLPaq7l4308H6jRuadj09Z7vngoEfrwg5lEPbca7CSDwL1fGGgrkMfZJP616CQaaZEH4m1GLC6vDVXXXkkXis41ZezgUUTVN0TbCmLGcewfcuybn2jX7IFn+e63DZ7ovIP5sjdYXJykWR4ooWCpzgS828zEYQp2gX9bI1ukGlkduxOGYKbk9gpA+ZdXu06Rgw/O4powChZtWsOoa0jUKnhWMjtYMHFIQrhkHKwlhcL8nmylu5odkLjI8w6rFlgVZkhXgctEAPLCTSzsDJwNBJz8JEsbJy+xGWWdHyI8tfyfM6ZdGJkAOTV3ffu7i0w1m+13VJo98NEb2h20XdlUfqE7z2GlaVPN0ocWlxV5COj5tnOak8tqZsG7k5oKkHuk5+snf6OIgOaG5mthniOtRgxjFV7uQuD8q8TBJVmZMV+c5uYxkV0bK5lSdSTw1GpcfbcT9lOES5rvhoKxhRvBdmXyt86NzUThMos43kTJ49PmzSE3dBPZ8HofSP91fxjEdlvNDmmqci5uO08nxcAul4lchUqDf72B+bTLxyu7BxblSGJfYgwBp8JBTiClsQ9LCTIbb7RxmMe1evkygrFx9adNmDdj5waDakLNx3fEruhovZqHix3aE7nWKDaVC5zi5mrpOzfc5M/6pTxFJr23MFgRb6mCn8JKvWqCK1dEMFqtyzh7lghjmuufeA7nuVemoIXV5MSdi6nyVp0HI5Sbwqt5Xkk7lqop6fRjYPLhFXNlsjWHgXUHLOi1vLUMmM9yb6DAK6uWU9lr0UFTEl537sM+MuWHyLEUdmBCTpQkzpMRrSgHKb1F8xtZNPzv1mzipkRvnGB6gxpdTVqGrpzvBSYR4pD0HOro5HeijzOCsoW2LmuY6+4sp5wpRiP6s7IAK3voovMUMakuNxsMeEIaHkFHbNoamVSM3uzqCXG+V2CZSbUxa1GvozuuHpxWbPEWLHq9VPiOpAD7ZN+p65QAGxPBrYDV70AJt6cocI/xb3lzRASqu/XZVooYOHSpy3a86mU6Ba0jTWknje9OEl7055kpbrDcBGne2PGakBGKSljp/hZxeQkcT31p5TVXUOW5fiy31yYDVuVjCk1byvP6jda1C1BDWKjGRwP8k2JARlqvs7sYSt0WT44CNoWg8mbryCGi4DM8yv8qMZjEJaUE1oJUeVNbtwirZU42THrRLSopc+mvYF54nHi+5yJgQsiHp4DDeIhWXa8hXb8OUVn/P01dZXPX/Gj6bZsykaQXG38anfLKsKRgqZ8/N8xGB7dpSprBOW1mSBxMN71wq11TJZdgpRyBHE2+pp0pX2WLSirZ1MLkNl5wTwuUztjuOWYf4kmC7Qy0mOTZEeSPQiqMWrnKpwgVivIdRcunLCRhTRjQIECMqrGxrLNlERMToNdtohrDfBzEBXas/aOif7d0woSOpJv2bzOZ+rU99t+mZz5815kaBlKXeXMJ4elmabGJcYJVm3ylKjE9sd/U1Uj+yx1HWHvzInDTIv0mkLvVp7RTT3mp0iJMKHrmfnXSeW1BAtabnc7qdHk2aPi7YZpIFdIb+B5xVCAHXQom0F8e91UMTZgl4cXoxbaZqaBOdwhoGut3jBfIvRUcpchw6rJaoVFvn9/2FcvhV7s5+HElkDz+u8ro8gKU4u8mtDhoG8oVDulupLTliOWbzKTlIuJm+t3/Rg0tnUMXLQ/JHgTz3lUI5XHFVP6x2Tdt5ZHhgS+syN5qSXHCCnTpBE524M19GvT5f8AgvzazdYVnJ1HhsuWYDe2xsS38/bKzpj4t77zspAEMehOlR68WnmbpLMFzlvgDlDWh7TLeK9eeoDeLv1/qVwc16519frOh0fjnQaiwUSR6oUNZ3nQk8/85irlNZt5ORWzyWtkOFT5czNfX8YIvZEmeqeXqrEj8LrApjbUuCBqT8A3C3mQykoT1XZEfZF/4zog85nTj8E+jyOw6I+kTuJiaEB3SoH85rn40FNdx99+oIXI+3VKK5DbJl3l7yvzk5jsKrfZqxuktCtuNM57WNM6J9zekVHJoqOqwdDpBWdpCIuJ7Mm5l3rt+k0p9udPrY94fso5qQcfZG7OyALXYY9sMK5uQ2XYg/njrOQrcwvi4ZDmjf11LEwdb8iysVxQbvcurP5dOHHtDTVE9+TRRmYrrcp7e5KrgETkNjFQ4D2sEYYXjNrEGTt0Uawgd6zLd9lRUNQqEYWxgIIb5RCk72olRWWMls3DHeXNuvObeJmn1dPCcPI7Z4EkgQgq1ct93OPeVRUffH9BvJeg1Ooxgl/nAGeZ6G90pJ905TuCiOo1mMaDelumNkkmwuJ4fur1DA+Ow5G5xT6/f5SXSdELz3HUiRt1Ka73lcwZHVwXKpVFgzphCxBYshUtKcPXsikBL/fZWScdI2scW+Q8bTK5DZtZIquCHsjPeMKeFwjzTUV3YJxeqUYrLDD+LBcxAtheBmb/DYiN89p6CTCAnKwvX09m4+eoIn7GL0KJ5YMta+ror0Ytlwt/nXl0gctn1+Jx0xXdDnB8e11puRrm+xxtOWeySDu7Hp+l4Ghy3qG8UmVzzD7ai4W7PCFda5gDXe0reAsucxrD5fRDcnZSDs9J+UYrXRvBve2tp4Bicl7BjhDb1rZlD2UDhmE9Eb60ZGWnDLX8X2KcS7OqFRQR4V5ZsgjwNZuOmWdFtWFKr+OELPi7ssLuvV8hDQisqz0KScj6DCN/corDGq82KUFfjMvRn4HDWnE14fU3xxzpsno+FrqrO2s04OXE1et8atSX5WMJZOMV+tl248YjdorFnf79uTV5tbhBs4k6I3XPP1IiQ7EOVP5JNLwmeRFct2TBvQyfIFDa+8QWfULzuFooTTu43Wds7NgnbGi4Z374pWBzRhdN4dllcxLSI6SmoLx0dDmMopqenY6fBau1QTZKRyz6pwU4zjmbH7fTIyvHv3FUkfDGR2ss66nV52he+hgbjZwrBzYPneXnbBEXcUXitYcTzTmWGCeEzlau8OyzBSWU7+MIHzkhH073dexP2se3pVp11M0T+OLRVuVhA1tiqprl2sqVgclRAsjmJCeTttf+XVgxNeImcNlXnkvD19Q14b8snVMYt4KQNsJFk1NVno6+xOMvznon5DvmI9K6ejIPG0BhlKFeL3HGz/WKYI89+Temuk+l09+Ws3Gy9rHi5nV6toL1YU48hqZFggkGFIpNEfLr02OOuJJAPPULeayCwslp/o2WApgsnc3dsIOmaq6wYcIvdw8+A5L3WKwyMBogxoRhG+vGZG/NMA5W3J7bFVKKvJZnfAWUCqPaHFFqWWbpM9RC8+z2QWZYDpVZmEOdMr2ujtmOoLCp2vkqlaC5qU8mnL74IlOZ8/BdJz0Oltr4v7iINklMLIKkMddqi9JR4gz/7zFsBpddhHveAjW+fzq8ubAr4F6Q/oLtgUPM7+sp1cWxs6FRm8zLKpPQpGbI3uHpLPSnCkKu2uAPSqTlxVTItuzrN7q8+O+ShXNAmaSP67UOgGGm9wCLE465aaCkYB4Rthyb8TrYzxTZxy1rv7dS1Imnctig5KqA/5nOcUpz3JSa5rZDAKtXVbmvCDL2U+aq6QIaD/jLyhWrWBrkMB1wRSz5nptGQgibzxsSuZLOWm200qnB5bYhatqEKDcMTdxPswTd1TW3PuZ3H1yI49FMOMCPNsQdqyhCyDU947aH7in7nKgsWbaeassYTKGRr5vDR76clWXNB0xZzH+XmYZ49nYMtFUkEP9wM7tbBwl6BIOt6qEIFBmtowVCMam8fl+va2sLNX7IHNKh1YYX3gtGHt0QluFx9O6nYs1ZenXuT9nR9QeZnijT5F4pbvrq+RPMeQLRo3f/UGyh8B/ha8cKnONkMJqMIZ+wsjUfV0z7kGgJk/kZKT7dsTdi7vXDi6Awk2+aDjtkoDtP+tZr0n5VuikiQuc45DtvLj7vIrinKpq/CJHAsurB1RfS2URLSgi5zJFEUt2k+l4QZres7Q9RPFOQTpUsty110LmQZTX6+tmTZOhSBireH0x65g331NsMja5Af0IXtHEL8BcTJN3uD03VKPZd5vT+ilK9kxsm1fswnoRT3LHrwueTCRxd4+iSkt0frmkFgg73daQ1q54RBi70Z1SRz8l8uncuX4qzkYlQ5b9uHATnp8RsUznTrHmp0ZaHS5asyc7dePf1fziebWalSt13Hvy8eoLctFv7iN+gbkp2lGZqRK+tuWR5qUQTmYR6SrkxYcdY3VUpI5tU1FaAR+tujgLckQ8Soo5Xrj71ePa54Pfy7vHL48yv+fLLfF6ITkGcH8Hg1Db69TRGFG602nPPZ6GmJPXWR/Jy32TkyEVdclseUAzRGXk4SiDoFXqbSKLGohFbpeodEnieFbrZ+568uo/0Lbl8Bsod8q6sPwCDaxxChr/dSnjCZO620iWCkYWRLIzazanT5TOkS1Kj68TJpySMLQ8OKBS01Fo5EEQDOHaqotZJ3eAOux+uWl7fowHniVa+2JLUZkJDaGcxf519172KU6pqByMYGbJ25QuDUcnXFTCm1570iNDIFTUtixKJjtpWyTP59eGr+rDIUcsEUrv1PYzliWaN82BmI5pFujqJYERgstUyD1FLoKwq3sKwsQy0BE6YtfjMEkterSIqz3cV4wUWOdx5EuVu7eOcCcubGx1bndbObGbhCzfq5lVBvx4lMI7xsThk51vPSQ+siMjZCN6whVDFTCyP9YXFdBDmbC7ICmQInXnEvc6SU4X6uMXhR6JJ4TACxePSujAewU4BcEKaACx0Z3DS2Jw9k05WSPQh6aZI4Vj6eRPTLCR5JefvrxvMH9evf233/p638j8/+1i6Lc7nN36/opGlLxvwb6/wfLLx1m//Hs1/vdPX8aoAEp8u+o61Uv2+/XQf3XR9Wsxf/0m7es/XXT9dhf6t6hr5+Q5/34HeQ6y99c/gSfAkm/bJvAqT+r+/UWGb/d9/3QX+J9u/L5V+7jq/3EnF/4ZAQr+4/8D23CxrhA7AAA= -->
