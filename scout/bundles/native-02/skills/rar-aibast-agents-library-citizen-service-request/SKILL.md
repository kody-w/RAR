---
name: "rar-aibast-agents-library-citizen-service-request"
description: "Handles 311-style intake and routing from a live simulated Dynamics 365 tenant's service cases, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/citizen_service_request", "rar_sha256": "33b6a25019280cb2c687286897a5bcef088ecef796331b206a1a4827a973246c", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["311", "citizen-services", "municipal", "routing", "SLA", "local-government"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/citizen_service_request`. The original RAPP
agent is preserved byte-for-byte in `citizen_service_request_agent.py` and in the RCI capsule.

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

Citizen Service Request Agent — a template you are meant to mutate.

Handles citizen service request intake, department routing, status
updates, and resolution summaries for municipal 311-style systems.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live service cases over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="request_intake")
     — with network up, the intake dashboard is built from the tenant's
     38 live cases (e.g. CAS-260130 "Building permit application
     awaiting plan review" for City of Alder Creek). In this template a
     citizen service request is represented as a Dynamics case
     (incident).
  2. No network? Everything falls back to the embedded demo layer below
     (SERVICE_REQUESTS / DEPARTMENT_ROUTING) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CITIZEN_SERVICE_REQUEST_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your 311/CRM system), or
     replace _fetch_collection() with your own service API. The fields
     the rest of the file needs are listed in _normalize_live_request() —
     ward and department stay "n/a — enrichment seam" until you wire
     your municipal routing system.

OPERATIONS
  request_intake | routing_assignment | status_update | resolution_summary
  kwargs: operation (required), request_id, category

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "category": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "request_intake",
        "routing_assignment",
        "status_update",
        "resolution_summary"
      ],
      "type": "string"
    },
    "request_id": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `citizen_service_request_agent.py` and embedded as the fenced Python below (sha256 33b6a25019280cb2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `citizen_service_request_agent.py` first:

```bash
python3 citizen_service_request_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 citizen_service_request_agent.py   # or on stdin
python3 citizen_service_request_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Citizen Service Request Agent — a template you are meant to mutate.

Handles citizen service request intake, department routing, status
updates, and resolution summaries for municipal 311-style systems.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live service cases over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="request_intake")
     — with network up, the intake dashboard is built from the tenant's
     38 live cases (e.g. CAS-260130 "Building permit application
     awaiting plan review" for City of Alder Creek). In this template a
     citizen service request is represented as a Dynamics case
     (incident).
  2. No network? Everything falls back to the embedded demo layer below
     (SERVICE_REQUESTS / DEPARTMENT_ROUTING) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CITIZEN_SERVICE_REQUEST_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your 311/CRM system), or
     replace _fetch_collection() with your own service API. The fields
     the rest of the file needs are listed in _normalize_live_request() —
     ward and department stay "n/a — enrichment seam" until you wire
     your municipal routing system.

OPERATIONS
  request_intake | routing_assignment | status_update | resolution_summary
  kwargs: operation (required), request_id, category
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
    "name": "@aibast-agents-library/citizen_service_request",
    "version": "1.1.0",
    "display_name": "Citizen Service Request Agent",
    "description": "Handles 311-style intake and routing from a live simulated Dynamics 365 tenant's service cases, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["311", "citizen-services", "municipal", "routing", "SLA", "local-government"],
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
#   export CITIZEN_SERVICE_REQUEST_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your 311/CRM client. Downstream
# code only needs the fields produced by _normalize_live_request().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "CITIZEN_SERVICE_REQUEST_DATA_URL",
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
            rows = json.loads(resp.read().decode("utf-8")).get("value", [])
    except Exception:
        rows = []
    _LIVE_CACHE[collection] = rows
    return rows


def _normalize_live_request(row):
    """Project a Dynamics case (incident) record onto the shape this agent
    uses — in this template a citizen service request IS a Dynamics case.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not available from the case system
    alone' and the renderers label it as an enrichment seam."""
    return {
        "request_id": row.get("ticketnumber", row.get("incidentid", "")),
        "category": row.get(
            "casetypecode@OData.Community.Display.V1.FormattedValue", "General"
        ),
        "description": row.get("title", "untitled"),
        "submitter": row.get("customeridname", "Unknown"),
        "channel": row.get(
            "caseorigincode@OData.Community.Display.V1.FormattedValue", "Unknown"
        ),
        "priority": row.get(
            "prioritycode@OData.Community.Display.V1.FormattedValue", "Normal"
        ),
        "status": row.get(
            "statecode@OData.Community.Display.V1.FormattedValue", "Active"
        ),
        "assigned_to": row.get("owneridname") or None,
        "sla_target": str(row.get("resolveby") or "")[:10] or None,
        "age_days": _age_days(row.get("createdon")),
        "open": row.get("statecode") == 0,
        "ward": None,        # enrichment seam — wire your GIS/routing system
        "department": None,  # enrichment seam
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

SERVICE_REQUESTS = {
    "SR-2025-10001": {
        "category": "pothole_repair",
        "description": "Large pothole on Main St between 3rd and 4th Ave, approximately 18 inches wide",
        "location": "142 Main Street",
        "ward": 3,
        "submitted": "2025-02-28",
        "submitter": "Maria Gonzalez",
        "channel": "web_portal",
        "priority": "high",
        "status": "assigned",
        "department": "Public Works — Streets Division",
        "assigned_to": "Crew 7-B",
        "sla_target": "2025-03-07",
    },
    "SR-2025-10002": {
        "category": "streetlight_outage",
        "description": "Streetlight at intersection of Pine and Oak has been out for 2 weeks",
        "location": "Pine St & Oak Ave",
        "ward": 5,
        "submitted": "2025-03-01",
        "submitter": "David Kim",
        "channel": "phone_311",
        "priority": "medium",
        "status": "in_progress",
        "department": "Public Works — Electrical",
        "assigned_to": "Tech Unit 3",
        "sla_target": "2025-03-15",
    },
    "SR-2025-10003": {
        "category": "trash_collection_missed",
        "description": "Missed residential trash pickup on scheduled collection day (Tuesday)",
        "location": "2847 Elm Drive",
        "ward": 2,
        "submitted": "2025-03-04",
        "submitter": "Linda Park",
        "channel": "mobile_app",
        "priority": "medium",
        "status": "resolved",
        "department": "Sanitation Services",
        "assigned_to": "Route 12-A",
        "sla_target": "2025-03-06",
        "resolved_date": "2025-03-05",
        "resolution": "Special pickup completed. Route schedule updated to prevent recurrence.",
    },
    "SR-2025-10004": {
        "category": "graffiti_removal",
        "description": "Graffiti on retaining wall along Riverside Park walking path",
        "location": "Riverside Park — east entrance",
        "ward": 4,
        "submitted": "2025-03-05",
        "submitter": "Anonymous",
        "channel": "web_portal",
        "priority": "low",
        "status": "pending",
        "department": "Parks & Recreation",
        "assigned_to": None,
        "sla_target": "2025-03-19",
    },
    "SR-2025-10005": {
        "category": "water_main_break",
        "description": "Water bubbling up from street surface near fire hydrant, flooding sidewalk",
        "location": "600 block of Washington Blvd",
        "ward": 1,
        "submitted": "2025-03-06",
        "submitter": "James Walker",
        "channel": "phone_311",
        "priority": "critical",
        "status": "in_progress",
        "department": "Water & Sewer — Emergency",
        "assigned_to": "Emergency Crew Alpha",
        "sla_target": "2025-03-07",
    },
}

DEPARTMENT_ROUTING = {
    "pothole_repair": {"department": "Public Works — Streets Division", "sla_days": 7, "priority_default": "high"},
    "streetlight_outage": {"department": "Public Works — Electrical", "sla_days": 14, "priority_default": "medium"},
    "trash_collection_missed": {"department": "Sanitation Services", "sla_days": 2, "priority_default": "medium"},
    "graffiti_removal": {"department": "Parks & Recreation", "sla_days": 14, "priority_default": "low"},
    "water_main_break": {"department": "Water & Sewer — Emergency", "sla_days": 1, "priority_default": "critical"},
    "sidewalk_damage": {"department": "Public Works — Streets Division", "sla_days": 21, "priority_default": "low"},
    "noise_complaint": {"department": "Code Enforcement", "sla_days": 3, "priority_default": "medium"},
    "abandoned_vehicle": {"department": "Police — Non-Emergency", "sla_days": 7, "priority_default": "low"},
    "tree_hazard": {"department": "Public Works — Urban Forestry", "sla_days": 5, "priority_default": "high"},
    "illegal_dumping": {"department": "Sanitation Services", "sla_days": 7, "priority_default": "medium"},
}

SLA_TARGETS = {
    "critical": {"response_hours": 4, "resolution_days": 1},
    "high": {"response_hours": 24, "resolution_days": 7},
    "medium": {"response_hours": 48, "resolution_days": 14},
    "low": {"response_hours": 72, "resolution_days": 21},
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _sla_compliance():
    """Calculate SLA compliance metrics."""
    total = len(SERVICE_REQUESTS)
    resolved = [sr for sr in SERVICE_REQUESTS.values() if sr["status"] == "resolved"]
    on_time = sum(1 for sr in resolved if sr.get("resolved_date", "9999") <= sr["sla_target"])
    resolution_rate = round((len(resolved) / total) * 100, 1) if total else 0
    sla_rate = round((on_time / len(resolved)) * 100, 1) if resolved else 0
    return {"total": total, "resolved": len(resolved), "resolution_rate": resolution_rate, "sla_compliance": sla_rate}


def _category_breakdown():
    """Count requests by category."""
    breakdown = {}
    for sr in SERVICE_REQUESTS.values():
        cat = sr["category"]
        breakdown[cat] = breakdown.get(cat, 0) + 1
    return breakdown


def _ward_breakdown():
    """Count requests by ward."""
    breakdown = {}
    for sr in SERVICE_REQUESTS.values():
        ward = sr["ward"]
        breakdown[ward] = breakdown.get(ward, 0) + 1
    return breakdown


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class CitizenServiceRequestAgent(BasicAgent):
    """Citizen service request management agent for municipalities."""

    def __init__(self):
        self.name = "CitizenServiceRequestAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Citizen Service Request Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "request_intake",
                            "routing_assignment",
                            "status_update",
                            "resolution_summary",
                        ],
                    },
                    "request_id": {"type": "string"},
                    "category": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "request_intake")
        dispatch = {
            "request_intake": self._request_intake,
            "routing_assignment": self._routing_assignment,
            "status_update": self._status_update,
            "resolution_summary": self._resolution_summary,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        return handler(**kwargs)

    def _live_request_intake(self, requests):
        """Intake dashboard built from live tenant cases (preferred online)."""
        open_reqs = [r for r in requests if r["open"]]
        lines = [
            "# Service Request Intake Dashboard — Live Tenant Cases\n",
            f"Live records from {DATA_SOURCE_URL} (Aster Lane Office Systems).",
            "In this template a citizen service request is a Dynamics case.",
            "Pass `request_id` (e.g. SR-2025-10001) for the embedded demo view.\n",
            f"**Total Requests:** {len(requests)}",
            f"**Open:** {len(open_reqs)} | **Closed:** {len(requests) - len(open_reqs)}\n",
            "## Open Requests\n",
            "| Case | Category | Description | Submitter | Priority | Channel | Age | Department |",
            "|---|---|---|---|---|---|---|---|",
        ]
        for r in sorted(open_reqs, key=lambda x: x["request_id"]):
            dept = r["department"] if r["department"] is not None else "n/a — enrichment seam"
            lines.append(
                f"| {r['request_id']} | {r['category']} | {r['description']} "
                f"| {r['submitter']} | {r['priority']} | {r['channel']} "
                f"| {r['age_days']}d | {dept} |"
            )
        lines.append("\n## Requests by Category\n")
        by_cat = {}
        for r in requests:
            by_cat[r["category"]] = by_cat.get(r["category"], 0) + 1
        for cat, count in sorted(by_cat.items()):
            lines.append(f"- {cat}: {count}")
        lines.append(
            "\nWard and department routing need your GIS/municipal system — "
            "wire it at the LIVE DATA SEAM."
        )
        return "\n".join(lines)

    def _request_intake(self, **kwargs) -> str:
        if not kwargs.get("request_id") and not kwargs.get("category"):
            live = [
                r for r in (
                    _normalize_live_request(row)
                    for row in _fetch_collection("incidents")
                )
                if r["request_id"]
            ]
            if live:
                return self._live_request_intake(live)
        lines = ["# Service Request Intake Dashboard\n"]
        metrics = _sla_compliance()
        lines.append(f"**Total Requests:** {metrics['total']}")
        lines.append(f"**Resolved:** {metrics['resolved']} ({metrics['resolution_rate']}%)")
        lines.append(f"**SLA Compliance:** {metrics['sla_compliance']}%\n")
        lines.append("## Active Requests\n")
        lines.append("| SR ID | Category | Location | Priority | Status | Department |")
        lines.append("|---|---|---|---|---|---|")
        for srid, sr in SERVICE_REQUESTS.items():
            cat = sr["category"].replace("_", " ").title()
            lines.append(
                f"| {srid} | {cat} | {sr['location']} "
                f"| {sr['priority'].title()} | {sr['status'].replace('_', ' ').title()} | {sr['department']} |"
            )
        lines.append("\n## Requests by Category\n")
        for cat, count in _category_breakdown().items():
            lines.append(f"- {cat.replace('_', ' ').title()}: {count}")
        lines.append("\n## Requests by Ward\n")
        for ward, count in sorted(_ward_breakdown().items()):
            lines.append(f"- Ward {ward}: {count}")
        return "\n".join(lines)

    def _routing_assignment(self, **kwargs) -> str:
        lines = ["# Service Request Routing Guide\n"]
        lines.append("## Category Routing Table\n")
        lines.append("| Category | Department | SLA (days) | Default Priority |")
        lines.append("|---|---|---|---|")
        for cat, routing in DEPARTMENT_ROUTING.items():
            lines.append(
                f"| {cat.replace('_', ' ').title()} | {routing['department']} "
                f"| {routing['sla_days']} | {routing['priority_default'].title()} |"
            )
        lines.append("\n## SLA Response Standards\n")
        lines.append("| Priority | Response Time | Resolution Target |")
        lines.append("|---|---|---|")
        for priority, sla in SLA_TARGETS.items():
            lines.append(f"| {priority.title()} | {sla['response_hours']} hours | {sla['resolution_days']} days |")
        lines.append("\n## Pending Assignment\n")
        unassigned = {k: v for k, v in SERVICE_REQUESTS.items() if v["assigned_to"] is None}
        if unassigned:
            for srid, sr in unassigned.items():
                routing = DEPARTMENT_ROUTING.get(sr["category"], {})
                lines.append(f"- **{srid}:** {sr['category'].replace('_', ' ').title()} -> {routing.get('department', 'TBD')}")
        else:
            lines.append("All requests currently assigned.")
        return "\n".join(lines)

    def _status_update(self, **kwargs) -> str:
        request_id = kwargs.get("request_id")
        if request_id and request_id in SERVICE_REQUESTS:
            sr = SERVICE_REQUESTS[request_id]
            lines = [f"# Status Update: {request_id}\n"]
            lines.append(f"- **Category:** {sr['category'].replace('_', ' ').title()}")
            lines.append(f"- **Description:** {sr['description']}")
            lines.append(f"- **Location:** {sr['location']} (Ward {sr['ward']})")
            lines.append(f"- **Submitted:** {sr['submitted']} via {sr['channel'].replace('_', ' ').title()}")
            lines.append(f"- **Priority:** {sr['priority'].title()}")
            lines.append(f"- **Status:** {sr['status'].replace('_', ' ').title()}")
            lines.append(f"- **Department:** {sr['department']}")
            lines.append(f"- **Assigned To:** {sr['assigned_to'] or 'Unassigned'}")
            lines.append(f"- **SLA Target:** {sr['sla_target']}")
            if sr.get("resolved_date"):
                lines.append(f"- **Resolved:** {sr['resolved_date']}")
            if sr.get("resolution"):
                lines.append(f"- **Resolution:** {sr['resolution']}")
            return "\n".join(lines)

        lines = ["# Request Status Summary\n"]
        lines.append("| SR ID | Category | Status | Assigned To | SLA Target |")
        lines.append("|---|---|---|---|---|")
        for srid, sr in SERVICE_REQUESTS.items():
            lines.append(
                f"| {srid} | {sr['category'].replace('_', ' ').title()} "
                f"| {sr['status'].replace('_', ' ').title()} | {sr['assigned_to'] or 'Unassigned'} | {sr['sla_target']} |"
            )
        return "\n".join(lines)

    def _resolution_summary(self, **kwargs) -> str:
        lines = ["# Resolution Summary Report\n"]
        metrics = _sla_compliance()
        lines.append(f"**Resolution Rate:** {metrics['resolution_rate']}%")
        lines.append(f"**SLA Compliance:** {metrics['sla_compliance']}%\n")
        resolved = {k: v for k, v in SERVICE_REQUESTS.items() if v["status"] == "resolved"}
        if resolved:
            lines.append("## Resolved Requests\n")
            for srid, sr in resolved.items():
                lines.append(f"### {srid}: {sr['category'].replace('_', ' ').title()}\n")
                lines.append(f"- **Location:** {sr['location']}")
                lines.append(f"- **Submitted:** {sr['submitted']}")
                lines.append(f"- **Resolved:** {sr.get('resolved_date', 'N/A')}")
                lines.append(f"- **SLA Target:** {sr['sla_target']}")
                met = "Yes" if sr.get("resolved_date", "9999") <= sr["sla_target"] else "No"
                lines.append(f"- **SLA Met:** {met}")
                lines.append(f"- **Resolution:** {sr.get('resolution', 'N/A')}\n")
        open_requests = {k: v for k, v in SERVICE_REQUESTS.items() if v["status"] != "resolved"}
        if open_requests:
            lines.append("## Open Requests\n")
            lines.append("| SR ID | Category | Priority | Status | SLA Target |")
            lines.append("|---|---|---|---|---|")
            for srid, sr in open_requests.items():
                lines.append(
                    f"| {srid} | {sr['category'].replace('_', ' ').title()} "
                    f"| {sr['priority'].title()} | {sr['status'].replace('_', ' ').title()} | {sr['sla_target']} |"
                )
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = CitizenServiceRequestAgent()
    print("LIVE TENANT INTAKE QUEUE (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="request_intake"))
    print("\n" + "=" * 80 + "\n")
    print("EMBEDDED DEMO REQUEST (works offline)")
    print(agent.perform(operation="request_intake", category="pothole_repair"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="routing_assignment"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="status_update", request_id="SR-2025-10001"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="resolution_summary"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
