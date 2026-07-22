"""
Support Ticket Resolution Agent — a template you are meant to mutate.

Provides intelligent ticket triage, knowledge base resolution search,
escalation routing, and SLA compliance dashboards for support operations.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live support tickets over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="ticket_triage")
     — with network up, the triage queue is the tenant's live open cases
     (e.g. CAS-260125 "Patient intake forms failing to sync to records
     system" for Riverbend Medical Group). A Dynamics case maps directly
     onto a support ticket; case priority maps to P1/P2/P3.
  2. No network? Everything falls back to the embedded demo layer below
     (SUPPORT_TICKETS / KB_ARTICLES) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SUPPORT_TICKET_RESOLUTION_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from Zendesk/Freshdesk),
     or replace _fetch_collection() with your own ticketing API. The
     fields the rest of the file needs are listed in
     _normalize_live_ticket() — customer ARR and KB matches stay
     "n/a — enrichment seam" until you wire your billing system and
     knowledge base.

OPERATIONS
  ticket_triage | resolution_search | escalation_routing | sla_dashboard
  kwargs: operation (required), category
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
    "name": "@aibast-agents-library/support_ticket_resolution",
    "version": "1.1.0",
    "display_name": "Support Ticket Resolution Agent",
    "description": "Triages tickets and tracks SLAs from a live simulated Dynamics 365 tenant's support cases, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["support", "tickets", "triage", "sla", "knowledge-base", "escalation"],
    "category": "software_digital_products",
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
#   export SUPPORT_TICKET_RESOLUTION_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your ticketing client. Downstream
# code only needs the fields produced by _normalize_live_ticket().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "SUPPORT_TICKET_RESOLUTION_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
_LIVE_CACHE = {}

# Dynamics case priority -> support severity used by this agent.
_PRIORITY_TO_SEVERITY = {"High": "P1", "Normal": "P2", "Low": "P3"}


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


def _normalize_live_ticket(row):
    """Project a Dynamics case (incident) record onto the shape this agent
    uses — a Dynamics case maps directly onto a support ticket. THIS is
    the contract your replacement data source must meet — a dict with
    these keys. None means 'not available from the ticketing system
    alone' and the renderers label it as an enrichment seam."""
    priority = row.get(
        "prioritycode@OData.Community.Display.V1.FormattedValue", "Normal"
    )
    return {
        "id": row.get("ticketnumber", row.get("incidentid", "")),
        "customer": row.get("customeridname", "Unknown"),
        "subject": row.get("title", "untitled"),
        "severity": _PRIORITY_TO_SEVERITY.get(priority, "P2"),
        "category": row.get(
            "casetypecode@OData.Community.Display.V1.FormattedValue", "General"
        ),
        "status": row.get(
            "statecode@OData.Community.Display.V1.FormattedValue", "Active"
        ),
        "assigned_to": row.get("owneridname", "Unassigned"),
        "sla_deadline": str(row.get("resolveby") or "")[:10] or None,
        "age_days": _age_days(row.get("createdon")),
        "open": row.get("statecode") == 0,
        "arr": None,         # enrichment seam — wire your billing system
        "kb_matches": None,  # enrichment seam — wire your knowledge base
        "_live": True,
    }


def _age_days(iso_date):
    try:
        then = datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
        return max(0, (datetime.now(timezone.utc) - then).days)
    except (ValueError, TypeError):
        return 0


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback) — Synthetic domain data
# ---------------------------------------------------------------------------

SUPPORT_TICKETS = {
    "TKT-8001": {
        "customer": "Meridian Healthcare Systems",
        "subject": "Dashboard loading timeout on large datasets",
        "severity": "P2",
        "category": "performance",
        "status": "open",
        "created": "2026-03-15T09:22:00",
        "sla_deadline": "2026-03-16T09:22:00",
        "assigned_to": "Tier 2 - Backend",
        "arr": 186000,
        "description": "Dashboard takes 45+ seconds to load when filtering by date ranges exceeding 90 days.",
    },
    "TKT-8002": {
        "customer": "ClearView Analytics",
        "subject": "SSO login failure after IdP certificate rotation",
        "severity": "P1",
        "category": "authentication",
        "status": "in_progress",
        "created": "2026-03-16T06:15:00",
        "sla_deadline": "2026-03-16T10:15:00",
        "assigned_to": "Tier 3 - Security",
        "arr": 72000,
        "description": "All users unable to authenticate via Okta SSO after certificate rotation. Entire org locked out.",
    },
    "TKT-8003": {
        "customer": "Skyline Hospitality Group",
        "subject": "API rate limit exceeded during bulk import",
        "severity": "P3",
        "category": "api",
        "status": "open",
        "created": "2026-03-14T14:30:00",
        "sla_deadline": "2026-03-17T14:30:00",
        "assigned_to": "Tier 1 - General",
        "arr": 360000,
        "description": "Bulk import process hitting 429 errors. Need temporary rate limit increase or batch guidance.",
    },
    "TKT-8004": {
        "customer": "BrightPath Education",
        "subject": "Report export generates corrupted CSV files",
        "severity": "P2",
        "category": "data_export",
        "status": "waiting_customer",
        "created": "2026-03-13T11:00:00",
        "sla_deadline": "2026-03-14T11:00:00",
        "assigned_to": "Tier 2 - Data",
        "arr": 96000,
        "description": "CSV exports for enrollment reports contain malformed UTF-8 characters. Affects downstream systems.",
    },
    "TKT-8005": {
        "customer": "Granite Construction Co",
        "subject": "Cannot add new users to workspace",
        "severity": "P2",
        "category": "user_management",
        "status": "open",
        "created": "2026-03-16T08:45:00",
        "sla_deadline": "2026-03-17T08:45:00",
        "assigned_to": "Tier 1 - General",
        "arr": 54000,
        "description": "Admin portal returns 500 error when attempting to invite new users. Seat count shows 12/20.",
    },
}

KB_ARTICLES = {
    "KB-101": {"title": "Optimizing Dashboard Performance for Large Datasets", "category": "performance", "views": 1842, "helpfulness": 87},
    "KB-102": {"title": "SSO Certificate Rotation Guide", "category": "authentication", "views": 956, "helpfulness": 92},
    "KB-103": {"title": "API Rate Limits and Bulk Import Best Practices", "category": "api", "views": 2103, "helpfulness": 78},
    "KB-104": {"title": "Troubleshooting CSV Export Encoding Issues", "category": "data_export", "views": 634, "helpfulness": 81},
    "KB-105": {"title": "User Management and Invitation Troubleshooting", "category": "user_management", "views": 1247, "helpfulness": 74},
    "KB-106": {"title": "SAML 2.0 Configuration Reference", "category": "authentication", "views": 712, "helpfulness": 89},
}

SLA_THRESHOLDS = {
    "P1": {"first_response_hrs": 1, "resolution_hrs": 4},
    "P2": {"first_response_hrs": 4, "resolution_hrs": 24},
    "P3": {"first_response_hrs": 8, "resolution_hrs": 72},
    "P4": {"first_response_hrs": 24, "resolution_hrs": 168},
}

RESOLUTION_HISTORY = {
    "performance": {"avg_resolution_hrs": 18.4, "first_contact_resolution_pct": 32},
    "authentication": {"avg_resolution_hrs": 3.2, "first_contact_resolution_pct": 45},
    "api": {"avg_resolution_hrs": 12.6, "first_contact_resolution_pct": 58},
    "data_export": {"avg_resolution_hrs": 22.1, "first_contact_resolution_pct": 28},
    "user_management": {"avg_resolution_hrs": 6.8, "first_contact_resolution_pct": 65},
}

ESCALATION_MATRIX = {
    "Tier 1 - General": {"escalates_to": "Tier 2 - Specialist", "manager": "Rachel Torres"},
    "Tier 2 - Backend": {"escalates_to": "Tier 3 - Engineering", "manager": "David Kim"},
    "Tier 2 - Data": {"escalates_to": "Tier 3 - Engineering", "manager": "David Kim"},
    "Tier 3 - Security": {"escalates_to": "VP Engineering", "manager": "Samira Patel"},
    "Tier 3 - Engineering": {"escalates_to": "VP Engineering", "manager": "Samira Patel"},
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _ticket_triage():
    triaged = []
    for tid, t in SUPPORT_TICKETS.items():
        kb_matches = [a for aid, a in KB_ARTICLES.items() if a["category"] == t["category"]]
        hist = RESOLUTION_HISTORY.get(t["category"], {})
        triaged.append({
            "id": tid, "subject": t["subject"], "severity": t["severity"],
            "category": t["category"], "customer": t["customer"],
            "arr": t["arr"], "status": t["status"],
            "kb_matches": len(kb_matches),
            "avg_resolution_hrs": hist.get("avg_resolution_hrs", 0),
            "fcr_pct": hist.get("first_contact_resolution_pct", 0),
        })
    severity_order = {"P1": 0, "P2": 1, "P3": 2, "P4": 3}
    triaged.sort(key=lambda x: (severity_order.get(x["severity"], 9), -x["arr"]))
    return {"tickets": triaged, "total": len(triaged)}


def _resolution_search(category=None):
    if category:
        matches = {aid: a for aid, a in KB_ARTICLES.items() if a["category"] == category}
    else:
        matches = KB_ARTICLES
    results = []
    for aid, a in matches.items():
        results.append({"id": aid, "title": a["title"], "category": a["category"],
                        "views": a["views"], "helpfulness": a["helpfulness"]})
    results.sort(key=lambda x: x["helpfulness"], reverse=True)
    return {"results": results, "total": len(results)}


def _escalation_routing():
    routes = []
    for tid, t in SUPPORT_TICKETS.items():
        esc = ESCALATION_MATRIX.get(t["assigned_to"], {})
        routes.append({
            "ticket_id": tid, "subject": t["subject"], "severity": t["severity"],
            "current_team": t["assigned_to"], "escalates_to": esc.get("escalates_to", "N/A"),
            "manager": esc.get("manager", "N/A"), "customer": t["customer"],
        })
    return {"routes": routes}


def _sla_dashboard():
    metrics = {"total": len(SUPPORT_TICKETS), "breached": 0, "at_risk": 0, "on_track": 0}
    details = []
    for tid, t in SUPPORT_TICKETS.items():
        sla = SLA_THRESHOLDS.get(t["severity"], {})
        # Simplified: mark P1 open/in_progress as at_risk, breached SLA for TKT-8004
        if tid == "TKT-8004":
            status = "breached"
            metrics["breached"] += 1
        elif t["severity"] == "P1":
            status = "at_risk"
            metrics["at_risk"] += 1
        else:
            status = "on_track"
            metrics["on_track"] += 1
        details.append({
            "ticket_id": tid, "severity": t["severity"], "customer": t["customer"],
            "sla_status": status, "resolution_target_hrs": sla.get("resolution_hrs", 0),
        })
    return {"metrics": metrics, "details": details}


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

class SupportTicketResolutionAgent(BasicAgent):
    """Support ticket triage, resolution, and SLA management agent."""

    def __init__(self):
        self.name = "SupportTicketResolutionAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "ticket_triage",
                            "resolution_search",
                            "escalation_routing",
                            "sla_dashboard",
                        ],
                        "description": "The support operation to perform.",
                    },
                    "category": {
                        "type": "string",
                        "description": "Optional category filter for resolution search.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "ticket_triage")
        if op == "ticket_triage":
            return self._ticket_triage()
        elif op == "resolution_search":
            return self._resolution_search(kwargs.get("category"))
        elif op == "escalation_routing":
            return self._escalation_routing()
        elif op == "sla_dashboard":
            return self._sla_dashboard()
        return f"**Error:** Unknown operation `{op}`."

    def _live_ticket_triage(self, tickets):
        """Triage queue built from live tenant cases (preferred online)."""
        open_tickets = [t for t in tickets if t["open"]]
        sev_order = {"P1": 0, "P2": 1, "P3": 2, "P4": 3}
        open_tickets.sort(key=lambda t: (sev_order.get(t["severity"], 9), t["id"]))
        lines = [
            "# Ticket Triage Queue — Live Tenant Cases",
            "",
            f"Live records from {DATA_SOURCE_URL} (Aster Lane Office Systems).",
            "A Dynamics case maps directly onto a support ticket; case priority",
            "maps to P1/P2/P3.",
            "",
            f"**Open Tickets:** {len(open_tickets)} of {len(tickets)} total",
            "",
            "| Priority | Ticket | Customer | Subject | Category | Age | SLA Target | ARR |",
            "|----------|--------|----------|---------|----------|-----|------------|-----|",
        ]
        for t in open_tickets:
            arr = "n/a — enrichment seam" if t["arr"] is None else f"${t['arr']:,}"
            lines.append(
                f"| {t['severity']} | {t['id']} | {t['customer']} | {t['subject']} "
                f"| {t['category']} | {t['age_days']}d | {t['sla_deadline'] or 'n/a'} "
                f"| {arr} |"
            )
        p1 = sum(1 for t in open_tickets if t["severity"] == "P1")
        lines.append("")
        lines.append(f"**P1 tickets needing immediate attention:** {p1}")
        lines.append(
            "Customer ARR and KB matches need your billing system and knowledge "
            "base — wire them at the LIVE DATA SEAM."
        )
        return "\n".join(lines)

    def _ticket_triage(self) -> str:
        live = [
            t for t in (
                _normalize_live_ticket(row)
                for row in _fetch_collection("incidents")
            )
            if t["id"]
        ]
        if live:
            return self._live_ticket_triage(live)
        data = _ticket_triage()
        lines = [
            "# Ticket Triage Queue",
            "",
            f"**Open Tickets:** {data['total']}",
            "",
            "| Priority | Ticket | Customer | Category | ARR | KB Matches | Avg Resolution |",
            "|----------|--------|----------|----------|-----|-----------|----------------|",
        ]
        for t in data["tickets"]:
            lines.append(
                f"| {t['severity']} | {t['id']} | {t['customer']} | {t['category']} "
                f"| ${t['arr']:,} | {t['kb_matches']} | {t['avg_resolution_hrs']}h |"
            )
        return "\n".join(lines)

    def _resolution_search(self, category=None) -> str:
        data = _resolution_search(category)
        filter_label = f" (filtered: {category})" if category else ""
        lines = [
            f"# Knowledge Base Search{filter_label}",
            "",
            f"**Results:** {data['total']}",
            "",
            "| Article | Category | Views | Helpfulness |",
            "|---------|----------|-------|------------|",
        ]
        for r in data["results"]:
            lines.append(
                f"| {r['title']} | {r['category']} | {r['views']:,} | {r['helpfulness']}% |"
            )
        return "\n".join(lines)

    def _escalation_routing(self) -> str:
        data = _escalation_routing()
        lines = [
            "# Escalation Routing Map",
            "",
            "| Ticket | Severity | Customer | Current Team | Escalates To | Manager |",
            "|--------|----------|----------|-------------|-------------|---------|",
        ]
        for r in data["routes"]:
            lines.append(
                f"| {r['ticket_id']} | {r['severity']} | {r['customer']} "
                f"| {r['current_team']} | {r['escalates_to']} | {r['manager']} |"
            )
        return "\n".join(lines)

    def _sla_dashboard(self) -> str:
        data = _sla_dashboard()
        m = data["metrics"]
        lines = [
            "# SLA Compliance Dashboard",
            "",
            f"**Total Tickets:** {m['total']}",
            f"- On Track: {m['on_track']}",
            f"- At Risk: {m['at_risk']}",
            f"- Breached: {m['breached']}",
            "",
            "| Ticket | Severity | Customer | SLA Status | Resolution Target |",
            "|--------|----------|----------|-----------|-------------------|",
        ]
        for d in data["details"]:
            lines.append(
                f"| {d['ticket_id']} | {d['severity']} | {d['customer']} "
                f"| {d['sla_status'].upper()} | {d['resolution_target_hrs']}h |"
            )
        return "\n".join(lines)


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    agent = SupportTicketResolutionAgent()
    print("=" * 60)
    print("LIVE TENANT TRIAGE QUEUE (fetched over HTTP; falls back to the")
    print("embedded demo tickets offline)")
    print(agent.perform(operation="ticket_triage"))
    print("\n" + "=" * 60)
    print("EMBEDDED DEMO TICKETS (works offline)")
    print(agent.perform(operation="sla_dashboard"))
    for op in ["resolution_search", "escalation_routing"]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
