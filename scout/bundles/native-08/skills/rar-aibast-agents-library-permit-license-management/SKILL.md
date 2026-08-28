---
name: "rar-aibast-agents-library-permit-license-management"
description: "Tracks permit applications from a live simulated Dynamics 365 tenant plus renewal calendars and gap analysis, with an offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/permit_license_management", "rar_sha256": "4ea739f90368c84d3160f2b39f3cc2bd773c63f48d134df07288fa7004a586f8", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["permits", "licenses", "compliance", "regulatory", "energy", "renewals"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/permit_license_management`. The original RAPP
agent is preserved byte-for-byte in `permit_license_management_agent.py` and in the RCI capsule.

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

Permit and License Management Agent — a template you are meant to mutate.

Tracks permits and licenses across energy facilities, manages renewal
calendars, identifies compliance gaps, and monitors application status
for regulatory requirements.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live application records over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template a permit or license request is represented as a
     Dynamics case — e.g. CAS-260130 "Building permit application
     awaiting plan review" (City of Alder Creek) and CAS-260134
     "License renewal quote requested before expiration" (Summit Trail
     Software).
     Try: perform(operation="application_status")
  2. No network? Everything falls back to the embedded demo layer below
     (PERMITS / APPLICATIONS / REGULATORY_REQUIREMENTS) — the agent
     never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PERMIT_LICENSE_MANAGEMENT_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your permitting
     system), or replace _fetch_collection() with your own API client.
     Fields the rest of the file needs are listed in
     _normalize_live_application() — everything else keeps working
     untouched. Fields marked "enrichment seam" in the output (issuing
     authority, public comments) are where you wire your regulator
     portals.

OPERATIONS
  permit_inventory | renewal_calendar | compliance_gaps
  | application_status | at_risk_permits | initiate_renewal_workflow
  kwargs: operation (required), facility, permit_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "facility": {
      "description": "Optional facility name to filter results.",
      "type": "string"
    },
    "operation": {
      "description": "The permit management operation to perform.",
      "enum": [
        "permit_inventory",
        "renewal_calendar",
        "compliance_gaps",
        "application_status",
        "at_risk_permits",
        "initiate_renewal_workflow"
      ],
      "type": "string"
    },
    "permit_id": {
      "description": "Exact permit ID required by initiate_renewal_workflow.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `permit_license_management_agent.py` and embedded as the fenced Python below (sha256 4ea739f90368c84d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `permit_license_management_agent.py` first:

```bash
python3 permit_license_management_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 permit_license_management_agent.py   # or on stdin
python3 permit_license_management_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Permit and License Management Agent — a template you are meant to mutate.

Tracks permits and licenses across energy facilities, manages renewal
calendars, identifies compliance gaps, and monitors application status
for regulatory requirements.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live application records over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template a permit or license request is represented as a
     Dynamics case — e.g. CAS-260130 "Building permit application
     awaiting plan review" (City of Alder Creek) and CAS-260134
     "License renewal quote requested before expiration" (Summit Trail
     Software).
     Try: perform(operation="application_status")
  2. No network? Everything falls back to the embedded demo layer below
     (PERMITS / APPLICATIONS / REGULATORY_REQUIREMENTS) — the agent
     never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PERMIT_LICENSE_MANAGEMENT_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your permitting
     system), or replace _fetch_collection() with your own API client.
     Fields the rest of the file needs are listed in
     _normalize_live_application() — everything else keeps working
     untouched. Fields marked "enrichment seam" in the output (issuing
     authority, public comments) are where you wire your regulator
     portals.

OPERATIONS
  permit_inventory | renewal_calendar | compliance_gaps
  | application_status | at_risk_permits | initiate_renewal_workflow
  kwargs: operation (required), facility, permit_id
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/permit_license_management",
    "version": "1.2.0",
    "display_name": "Permit & License Management Agent",
    "description": "Tracks permit applications from a live simulated Dynamics 365 tenant plus renewal calendars and gap analysis, with an offline fallback.",
    "author": "AIBAST",
    "tags": ["permits", "licenses", "compliance", "regulatory", "energy", "renewals"],
    "category": "energy",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ---------------------------------------------------------------------------
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export PERMIT_LICENSE_MANAGEMENT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your permitting-system client.
# Downstream code only needs the fields produced by
# _normalize_live_application().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "PERMIT_LICENSE_MANAGEMENT_DATA_URL",
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


_PERMIT_KEYWORDS = ("permit", "license", "licence", "renewal")


def _normalize_live_application(row):
    """Project a Dynamics case onto the application shape this agent
    uses. THIS is the contract your replacement data source must meet —
    a dict with these keys. None means 'not available from CRM alone'
    and the renderers label it as an enrichment seam. In this template a
    permit or license request is represented as a Dynamics case."""
    resolveby = row.get("resolveby")
    return {
        "id": row.get("ticketnumber", ""),
        "name": row.get("title", "untitled"),
        "facility": row.get("customeridname", "Unknown"),
        "authority": None,        # enrichment seam — wire your regulator portal
        "submitted": str(row.get("createdon", ""))[:10],
        "status": "under_review" if row.get("statecode") == 0 else "decided",
        "expected_decision": str(resolveby)[:10] if resolveby else None,
        "comments": None,         # enrichment seam — wire public-comment tracking
        "_live": True,
    }


def _live_applications():
    """Live tenant cases that read as permit/license requests; []
    when offline."""
    return [
        _normalize_live_application(i)
        for i in _fetch_collection("incidents")
        if any(k in str(i.get("title", "")).lower() for k in _PERMIT_KEYWORDS)
    ]


def _na(value):
    """None = the CRM alone can't know this (enrichment seam); 0 is
    real."""
    return "n/a — enrichment seam" if value is None else f"{value}"


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

PERMITS = {
    "PRM-6001": {
        "name": "Title V Air Operating Permit",
        "facility": "Riverside Generating Station",
        "issuing_authority": "CA Air Resources Board",
        "permit_number": "AOP-CA-2024-1847",
        "issued_date": "2024-06-15",
        "expiration_date": "2029-06-15",
        "status": "active",
        "type": "air_quality",
        "renewal_lead_days": 365,
        "conditions": 24,
        "last_inspection": "2025-09-22",
    },
    "PRM-6002": {
        "name": "NPDES Stormwater Discharge Permit",
        "facility": "Riverside Generating Station",
        "issuing_authority": "CA State Water Board",
        "permit_number": "NPDES-CA-0052841",
        "issued_date": "2023-03-01",
        "expiration_date": "2026-03-01",
        "status": "expired",
        "type": "water_discharge",
        "renewal_lead_days": 180,
        "conditions": 18,
        "last_inspection": "2025-07-14",
    },
    "PRM-6003": {
        "name": "RCRA Hazardous Waste Generator",
        "facility": "Bayshore Refinery",
        "issuing_authority": "EPA Region 6",
        "permit_number": "TXD-0489-2215",
        "issued_date": "2022-01-10",
        "expiration_date": "2027-01-10",
        "status": "active",
        "type": "waste_management",
        "renewal_lead_days": 270,
        "conditions": 32,
        "last_inspection": "2025-11-05",
    },
    "PRM-6004": {
        "name": "Pipeline Operating License",
        "facility": "Northeast Corridor Pipeline",
        "issuing_authority": "PHMSA",
        "permit_number": "PHMSA-NE-7742",
        "issued_date": "2021-08-20",
        "expiration_date": "2026-08-20",
        "status": "active",
        "type": "pipeline_operation",
        "renewal_lead_days": 365,
        "conditions": 28,
        "last_inspection": "2025-10-30",
    },
    "PRM-6005": {
        "name": "Coal Combustion Residuals Permit",
        "facility": "Ridgeline Coal Station",
        "issuing_authority": "CO Dept of Public Health",
        "permit_number": "CCR-CO-2023-0091",
        "issued_date": "2023-04-01",
        "expiration_date": "2026-04-01",
        "status": "active",
        "type": "waste_management",
        "renewal_lead_days": 180,
        "conditions": 21,
        "last_inspection": "2025-08-18",
    },
    "PRM-6006": {
        "name": "Spill Prevention Control Plan",
        "facility": "Bayshore Refinery",
        "issuing_authority": "EPA Region 6",
        "permit_number": "SPCC-TX-2024-3340",
        "issued_date": "2024-02-15",
        "expiration_date": "2029-02-15",
        "status": "active",
        "type": "spill_prevention",
        "renewal_lead_days": 365,
        "conditions": 15,
        "last_inspection": "2025-06-02",
    },
}

APPLICATIONS = {
    "APP-7001": {
        "permit_name": "NPDES Stormwater Discharge Permit Renewal",
        "facility": "Riverside Generating Station",
        "submitted_date": "2025-09-01",
        "authority": "CA State Water Board",
        "status": "under_review",
        "expected_decision": "2026-04-15",
        "comments_received": 3,
    },
    "APP-7002": {
        "permit_name": "New Source Review - Gas Turbine Expansion",
        "facility": "Riverside Generating Station",
        "submitted_date": "2026-01-20",
        "authority": "CA Air Resources Board",
        "status": "public_comment",
        "expected_decision": "2026-06-30",
        "comments_received": 12,
    },
    "APP-7003": {
        "permit_name": "Pipeline Integrity Management Plan Update",
        "facility": "Northeast Corridor Pipeline",
        "submitted_date": "2026-02-10",
        "authority": "PHMSA",
        "status": "submitted",
        "expected_decision": "2026-05-15",
        "comments_received": 0,
    },
}

REGULATORY_REQUIREMENTS = {
    "air_quality": ["Continuous emissions monitoring", "Annual stack testing", "Quarterly compliance reports"],
    "water_discharge": ["Monthly effluent sampling", "Annual DMR submission", "Stormwater pollution prevention plan"],
    "waste_management": ["Biennial hazardous waste report", "Manifest tracking", "Land disposal restrictions compliance"],
    "pipeline_operation": ["Integrity management program", "Operator qualification records", "Emergency response plan"],
    "spill_prevention": ["Annual SPCC plan review", "Integrity testing of containers", "Discharge prevention briefings"],
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _permit_inventory():
    inventory = []
    for pid, p in PERMITS.items():
        inventory.append({
            "id": pid, "name": p["name"], "facility": p["facility"],
            "authority": p["issuing_authority"], "permit_number": p["permit_number"],
            "status": p["status"], "type": p["type"],
            "expiration": p["expiration_date"], "conditions": p["conditions"],
        })
    active = sum(1 for p in PERMITS.values() if p["status"] == "active")
    expired = sum(1 for p in PERMITS.values() if p["status"] == "expired")
    return {"permits": inventory, "total": len(inventory), "active": active, "expired": expired}


def _renewal_calendar():
    calendar = []
    for pid, p in PERMITS.items():
        calendar.append({
            "id": pid, "name": p["name"], "facility": p["facility"],
            "expiration": p["expiration_date"], "status": p["status"],
            "renewal_lead_days": p["renewal_lead_days"],
        })
    calendar.sort(key=lambda x: x["expiration"])
    return {"calendar": calendar}


def _compliance_gaps():
    gaps = []
    for pid, p in PERMITS.items():
        if p["status"] == "expired":
            gaps.append({
                "id": pid, "name": p["name"], "facility": p["facility"],
                "gap_type": "expired_permit", "severity": "critical",
                "detail": f"Permit {p['permit_number']} expired on {p['expiration_date']}",
            })
        reqs = REGULATORY_REQUIREMENTS.get(p["type"], [])
        if p["type"] == "water_discharge" and p["status"] == "expired":
            for req in reqs:
                gaps.append({
                    "id": pid, "name": p["name"], "facility": p["facility"],
                    "gap_type": "requirement_at_risk", "severity": "high",
                    "detail": f"Requirement '{req}' at risk due to expired permit",
                })
    return {"gaps": gaps, "total": len(gaps), "critical": sum(1 for g in gaps if g["severity"] == "critical")}


def _application_status():
    statuses = []
    for aid, a in APPLICATIONS.items():
        statuses.append({
            "id": aid, "name": a["permit_name"], "facility": a["facility"],
            "authority": a["authority"], "submitted": a["submitted_date"],
            "status": a["status"], "expected_decision": a["expected_decision"],
            "comments": a["comments_received"],
        })
    return {"applications": statuses, "total": len(statuses)}


def _at_risk_permits():
    risk = {
        "PRM-6002": ("critical", "Expired; renewal remains under review"),
        "PRM-6005": ("critical", "Expires within 30 days"),
        "PRM-6004": ("at_risk", "Renewal lead window is open"),
    }
    return [
        {
            "permit_id": permit_id,
            "permit": PERMITS[permit_id]["name"],
            "facility": PERMITS[permit_id]["facility"],
            "expiration": PERMITS[permit_id]["expiration_date"],
            "risk": severity,
            "reason": reason,
        }
        for permit_id, (severity, reason) in risk.items()
    ]


def _renewal_workflow(permit_id):
    permit = PERMITS.get(permit_id)
    if not permit:
        return None
    return {
        "permit_id": permit_id,
        "permit": permit["name"],
        "facility": permit["facility"],
        "workflow_id": f"RNW-{permit_id[4:]}-2026",
        "system": "Dynamics 365",
        "stakeholders": ["Compliance Manager", "Facility Manager"],
        "channels": ["Microsoft Teams", "Outlook"],
    }


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

class PermitLicenseManagementAgent(BasicAgent):
    """Permit and license tracking and compliance management agent."""

    def __init__(self):
        self.name = "PermitLicenseManagementAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "permit_inventory",
                            "renewal_calendar",
                            "compliance_gaps",
                            "application_status",
                            "at_risk_permits",
                            "initiate_renewal_workflow",
                        ],
                        "description": "The permit management operation to perform.",
                    },
                    "facility": {
                        "type": "string",
                        "description": "Optional facility name to filter results.",
                    },
                    "permit_id": {
                        "type": "string",
                        "description": "Exact permit ID required by initiate_renewal_workflow.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "permit_inventory")
        if op == "permit_inventory":
            return self._permit_inventory()
        elif op == "renewal_calendar":
            return self._renewal_calendar()
        elif op == "compliance_gaps":
            return self._compliance_gaps()
        elif op == "application_status":
            return self._application_status()
        elif op == "at_risk_permits":
            return self._at_risk_permits()
        elif op == "initiate_renewal_workflow":
            return self._initiate_renewal_workflow(kwargs.get("permit_id"))
        return f"**Error:** Unknown operation `{op}`."

    def _permit_inventory(self) -> str:
        data = _permit_inventory()
        lines = [
            "# Permit & License Inventory",
            "",
            f"**Total Permits:** {data['total']} | **Active:** {data['active']} | **Expired:** {data['expired']}",
            "",
            "| ID | Permit | Facility | Authority | Status | Expiration | Conditions |",
            "|----|--------|----------|-----------|--------|-----------|-----------|",
        ]
        for p in data["permits"]:
            lines.append(
                f"| {p['id']} | {p['name']} | {p['facility']} "
                f"| {p['authority']} | {p['status'].upper()} | {p['expiration']} | {p['conditions']} |"
            )
        return "\n".join(lines)

    def _renewal_calendar(self) -> str:
        data = _renewal_calendar()
        lines = [
            "# Permit Renewal Calendar",
            "",
            "| Permit | Facility | Expiration | Status | Lead Time |",
            "|--------|----------|-----------|--------|-----------|",
        ]
        for c in data["calendar"]:
            lines.append(
                f"| {c['name']} | {c['facility']} | {c['expiration']} "
                f"| {c['status'].upper()} | {c['renewal_lead_days']} days |"
            )
        return "\n".join(lines)

    def _compliance_gaps(self) -> str:
        data = _compliance_gaps()
        if data["total"] == 0:
            return "# Compliance Gaps\n\nNo compliance gaps identified."
        lines = [
            "# Compliance Gap Analysis",
            "",
            f"**Total Gaps:** {data['total']} | **Critical:** {data['critical']}",
            "",
            "| Permit | Facility | Gap Type | Severity | Detail |",
            "|--------|----------|----------|----------|--------|",
        ]
        for g in data["gaps"]:
            lines.append(
                f"| {g['name']} | {g['facility']} | {g['gap_type']} "
                f"| {g['severity'].upper()} | {g['detail']} |"
            )
        return "\n".join(lines)

    def _application_status(self) -> str:
        live = _live_applications()
        if live:
            lines = [
                "# Permit Application Status (live tenant data)",
                "",
                f"**Applications on record:** {len(live)} "
                f"({sum(1 for a in live if a['status'] == 'under_review')} under review)",
                "",
                "| ID | Application | Applicant | Authority | Submitted | Status | Decision Date | Comments |",
                "|----|-------------|-----------|-----------|-----------|--------|--------------|----------|",
            ]
            for a in sorted(live, key=lambda x: x["submitted"]):
                lines.append(
                    f"| {a['id']} | {a['name']} | {a['facility']} "
                    f"| {_na(a['authority'])} | {a['submitted']} | {a['status']} "
                    f"| {a['expected_decision'] or 'n/a'} | {_na(a['comments'])} |"
                )
            lines.append("")
            lines.append("_Source: live Static Dynamics 365 tenant (incidents). A permit or "
                         "license request is represented as a Dynamics case; issuing "
                         "authority and public comments are enrichment seams._")
            return "\n".join(lines)

        data = _application_status()
        lines = [
            "# Permit Application Status (embedded demo data — offline)",
            "",
            f"**Active Applications:** {data['total']}",
            "",
            "| ID | Application | Facility | Authority | Submitted | Status | Decision Date | Comments |",
            "|----|-------------|----------|-----------|-----------|--------|--------------|----------|",
        ]
        for a in data["applications"]:
            lines.append(
                f"| {a['id']} | {a['name']} | {a['facility']} "
                f"| {a['authority']} | {a['submitted']} | {a['status']} "
                f"| {a['expected_decision']} | {a['comments']} |"
            )
        return "\n".join(lines)

    def _at_risk_permits(self) -> str:
        lines = [
            "# Unified At-Risk and Critical Permit View",
            "",
            "| Permit ID | Permit | Facility | Expiration | Risk | Reason |",
            "|-----------|--------|----------|------------|------|--------|",
        ]
        for row in _at_risk_permits():
            lines.append(
                f"| {row['permit_id']} | {row['permit']} | {row['facility']} "
                f"| {row['expiration']} | {row['risk'].upper()} | {row['reason']} |"
            )
        lines.extend([
            "",
            "**Evidence:** Energy Operations demo 01:27-01:49 — automated "
            "tracking and a unified view of at-risk and critical permits.",
        ])
        return "\n".join(lines)

    def _initiate_renewal_workflow(self, permit_id) -> str:
        if not permit_id:
            return (
                "# Initiate Renewal Workflow\n\nProvide an exact `permit_id`. "
                f"Available IDs: {', '.join(sorted(PERMITS))}."
            )
        receipt = _renewal_workflow(permit_id)
        if not receipt:
            return f"**Error:** Unknown permit_id `{permit_id}`."
        return "\n".join([
            "# Permit Renewal Workflow",
            "",
            f"- **Permit:** {receipt['permit']} (`{receipt['permit_id']}`)",
            f"- **Facility:** {receipt['facility']}",
            f"- **Workflow ID:** {receipt['workflow_id']}",
            f"- **Stakeholders:** {', '.join(receipt['stakeholders'])}",
            "",
            "## Simulated Write Receipt",
            "",
            f"- **Workflow:** Simulated creation in {receipt['system']}.",
            f"- **Notifications:** Simulated delivery through {', '.join(receipt['channels'])}.",
            "- **Mode:** dry-run; no live workflow, permit, message, or email was mutated.",
            "- **Evidence:** Energy Operations demo 01:49-01:56.",
        ])


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    agent = PermitLicenseManagementAgent()
    print("=" * 60)
    print("LIVE TENANT APPLICATIONS (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="application_status"))
    print()
    print("=" * 60)
    print("EMBEDDED DEMO PERMITS (works offline)")
    for op in ["permit_inventory", "renewal_calendar", "compliance_gaps"]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
