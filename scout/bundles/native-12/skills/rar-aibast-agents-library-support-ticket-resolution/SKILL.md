---
name: "rar-aibast-agents-library-support-ticket-resolution"
description: "Triages tickets and tracks SLAs from a live simulated Dynamics 365 tenant's support cases, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/support_ticket_resolution", "rar_sha256": "803150569eae5d2f820e74baf9420c32528a8a3a0aec6252a2361f2a77f896bb", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["support", "tickets", "triage", "sla", "knowledge-base", "escalation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/support_ticket_resolution`. The original RAPP
agent is preserved byte-for-byte in `support_ticket_resolution_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "category": {
      "description": "Optional category filter for resolution search.",
      "type": "string"
    },
    "operation": {
      "description": "The support operation to perform.",
      "enum": [
        "ticket_triage",
        "resolution_search",
        "escalation_routing",
        "sla_dashboard"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `support_ticket_resolution_agent.py` and embedded as the fenced Python below (sha256 803150569eae5d2f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `support_ticket_resolution_agent.py` first:

```bash
python3 support_ticket_resolution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 support_ticket_resolution_agent.py   # or on stdin
python3 support_ticket_resolution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
