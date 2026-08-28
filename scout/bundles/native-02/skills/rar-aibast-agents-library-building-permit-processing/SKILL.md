---
name: "rar-aibast-agents-library-building-permit-processing"
description: "Tracks permit status and fees from a live simulated Dynamics 365 tenant's permit cases, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/building_permit_processing", "rar_sha256": "804d55baff28a32c074f862436217a599966f8ab3579cc2493d1fc6655a743c9", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["permits", "building", "zoning", "inspection", "local-government", "fees", "code-compliance", "workflow-routing"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/building_permit_processing`. The original RAPP
agent is preserved byte-for-byte in `building_permit_processing_agent.py` and in the RCI capsule.

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

Building Permit Processing Agent — a template you are meant to mutate.

Manages building permit workflows including status tracking, review
checklists, inspector assignments, and fee calculations for local
government permitting offices.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live permit-office cases over real HTTP from
     the globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="permit_status")
     — with network up, the queue surfaces the tenant's live permit cases
     such as CAS-260130 "Building permit application awaiting plan
     review" (City of Alder Creek). In this template a permit application
     is represented as a Dynamics case (incident).
  2. No network? Everything falls back to the embedded demo layer below
     (PERMIT_APPLICATIONS / ZONING_REQUIREMENTS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     BUILDING_PERMIT_PROCESSING_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from Accela/Tyler), or
     replace _fetch_collection() with your permitting API. The fields the
     rest of the file needs are listed in _normalize_live_permit() —
     valuation, parcel, and zoning stay "n/a — enrichment seam" until you
     wire your land-management system.

OPERATIONS
  permit_status | review_checklist | inspector_assignment |
  fee_calculation | application_intake | code_compliance_review |
  review_routing | approval_workflow | permit_issuance
  kwargs: operation (required), permit_id, key, user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "key": {
      "description": "Exact record key advertised by the selected evidence operation.",
      "type": "string"
    },
    "operation": {
      "enum": [
        "permit_status",
        "review_checklist",
        "inspector_assignment",
        "fee_calculation",
        "application_intake",
        "code_compliance_review",
        "review_routing",
        "approval_workflow",
        "permit_issuance"
      ],
      "type": "string"
    },
    "permit_id": {
      "type": "string"
    },
    "user_input": {
      "description": "Natural-language request containing an exact advertised record key.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `building_permit_processing_agent.py` and embedded as the fenced Python below (sha256 804d55baff28a32c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `building_permit_processing_agent.py` first:

```bash
python3 building_permit_processing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 building_permit_processing_agent.py   # or on stdin
python3 building_permit_processing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Building Permit Processing Agent — a template you are meant to mutate.

Manages building permit workflows including status tracking, review
checklists, inspector assignments, and fee calculations for local
government permitting offices.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live permit-office cases over real HTTP from
     the globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="permit_status")
     — with network up, the queue surfaces the tenant's live permit cases
     such as CAS-260130 "Building permit application awaiting plan
     review" (City of Alder Creek). In this template a permit application
     is represented as a Dynamics case (incident).
  2. No network? Everything falls back to the embedded demo layer below
     (PERMIT_APPLICATIONS / ZONING_REQUIREMENTS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     BUILDING_PERMIT_PROCESSING_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from Accela/Tyler), or
     replace _fetch_collection() with your permitting API. The fields the
     rest of the file needs are listed in _normalize_live_permit() —
     valuation, parcel, and zoning stay "n/a — enrichment seam" until you
     wire your land-management system.

OPERATIONS
  permit_status | review_checklist | inspector_assignment |
  fee_calculation | application_intake | code_compliance_review |
  review_routing | approval_workflow | permit_issuance
  kwargs: operation (required), permit_id, key, user_input
"""

import sys
import os
import re

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timezone

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/building_permit_processing",
    "version": "1.2.0",
    "display_name": "Building Permit Processing Agent",
    "description": "Tracks permit status and fees from a live simulated Dynamics 365 tenant's permit cases, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["permits", "building", "zoning", "inspection", "local-government", "fees", "code-compliance", "workflow-routing"],
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
#   export BUILDING_PERMIT_PROCESSING_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your permitting-system client.
# Downstream code only needs the fields from _normalize_live_permit().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "BUILDING_PERMIT_PROCESSING_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
_LIVE_CACHE = {}

# Case-title keywords that mark a tenant case as a permit-office item.
_PERMIT_KEYWORDS = ("permit", "plan review", "inspection", "zoning", "variance")


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


def _normalize_live_permit(row):
    """Project a Dynamics case (incident) record onto the shape this agent
    uses — in this template a permit application IS a Dynamics case.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not available from the case system
    alone' and the renderers label it as an enrichment seam."""
    return {
        "permit_id": row.get("ticketnumber", row.get("incidentid", "")),
        "applicant": row.get("customeridname", "Unknown"),
        "description": row.get("title", "untitled"),
        "status": row.get(
            "statecode@OData.Community.Display.V1.FormattedValue", "Active"
        ),
        "priority": row.get(
            "prioritycode@OData.Community.Display.V1.FormattedValue", "Normal"
        ),
        "reviewer": row.get("owneridname", "Unassigned"),
        "age_days": _age_days(row.get("createdon")),
        "open": row.get("statecode") == 0,
        "valuation": None,        # enrichment seam — wire your land-mgmt system
        "parcel_id": None,        # enrichment seam
        "zoning_district": None,  # enrichment seam
        "_live": True,
    }


def _age_days(iso_date):
    try:
        then = datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
        return max(0, (datetime.now(timezone.utc) - then).days)
    except (ValueError, TypeError):
        return 0


def _live_permit_queue():
    """Live tenant cases whose titles look permit-shaped; [] offline."""
    queue = []
    for row in _fetch_collection("incidents"):
        title = str(row.get("title", "")).lower()
        if any(kw in title for kw in _PERMIT_KEYWORDS):
            permit = _normalize_live_permit(row)
            if permit["permit_id"]:
                queue.append(permit)
    return queue


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback) — Synthetic domain data
# ---------------------------------------------------------------------------

PERMIT_APPLICATIONS = {
    "BP-2025-0101": {
        "applicant": "Greenfield Development LLC",
        "property_address": "4520 Oak Ridge Blvd",
        "parcel_id": "045-221-009",
        "permit_type": "new_construction",
        "description": "3-story mixed-use building — 12 residential units, ground floor retail",
        "submitted": "2025-01-15",
        "valuation": 4200000,
        "zoning_district": "MU-2 (Mixed Use)",
        "status": "plan_review",
        "assigned_reviewer": "Karen Whitfield",
        "review_cycle": 2,
    },
    "BP-2025-0102": {
        "applicant": "Johnson Family Trust",
        "property_address": "812 Maple Street",
        "parcel_id": "023-114-003",
        "permit_type": "residential_addition",
        "description": "650 sq ft second-story addition to single-family residence",
        "submitted": "2025-02-03",
        "valuation": 185000,
        "zoning_district": "R-1 (Single Family Residential)",
        "status": "approved",
        "assigned_reviewer": "Tom Delgado",
        "review_cycle": 1,
    },
    "BP-2025-0103": {
        "applicant": "Sunrise Solar Inc.",
        "property_address": "1100 Industrial Pkwy",
        "parcel_id": "067-340-015",
        "permit_type": "commercial_alteration",
        "description": "Rooftop solar installation — 240 panel array on warehouse",
        "submitted": "2025-02-20",
        "valuation": 320000,
        "zoning_district": "I-1 (Light Industrial)",
        "status": "inspection_scheduled",
        "assigned_reviewer": "Karen Whitfield",
        "review_cycle": 1,
    },
    "BP-2025-0104": {
        "applicant": "Metro School District",
        "property_address": "2200 Education Way",
        "parcel_id": "034-502-001",
        "permit_type": "institutional",
        "description": "New gymnasium and cafeteria wing — 18,000 sq ft",
        "submitted": "2025-01-28",
        "valuation": 6800000,
        "zoning_district": "PF (Public Facilities)",
        "status": "corrections_required",
        "assigned_reviewer": "Tom Delgado",
        "review_cycle": 3,
    },
}

ZONING_REQUIREMENTS = {
    "R-1 (Single Family Residential)": {
        "max_height": "35 ft / 2.5 stories",
        "setbacks": {"front": 25, "side": 5, "rear": 20},
        "lot_coverage": 40,
        "parking": "2 spaces per unit",
    },
    "MU-2 (Mixed Use)": {
        "max_height": "55 ft / 4 stories",
        "setbacks": {"front": 0, "side": 0, "rear": 10},
        "lot_coverage": 80,
        "parking": "1 space per unit + 1 per 500 sq ft commercial",
    },
    "I-1 (Light Industrial)": {
        "max_height": "45 ft / 3 stories",
        "setbacks": {"front": 20, "side": 10, "rear": 15},
        "lot_coverage": 60,
        "parking": "1 per 1,000 sq ft",
    },
    "PF (Public Facilities)": {
        "max_height": "50 ft / 3 stories",
        "setbacks": {"front": 30, "side": 15, "rear": 20},
        "lot_coverage": 50,
        "parking": "Per use determination",
    },
}

INSPECTION_SCHEDULE = {
    "BP-2025-0103": [
        {"type": "Electrical Rough-In", "inspector": "Dave Martinez", "date": "2025-03-20", "status": "scheduled"},
        {"type": "Structural Mounting", "inspector": "Lisa Park", "date": "2025-03-22", "status": "scheduled"},
        {"type": "Final Electrical", "inspector": "Dave Martinez", "date": "2025-04-05", "status": "pending"},
    ],
}

FEE_TABLES = {
    "plan_review": {"base": 250, "per_thousand_valuation": 4.50},
    "building_permit": {"base": 150, "per_thousand_valuation": 8.75},
    "electrical": {"base": 75, "per_thousand_valuation": 1.25},
    "plumbing": {"base": 75, "per_thousand_valuation": 1.25},
    "mechanical": {"base": 75, "per_thousand_valuation": 1.00},
    "fire_review": {"base": 200, "per_thousand_valuation": 2.00},
    "technology_surcharge": {"base": 25, "per_thousand_valuation": 0.50},
}

INSPECTORS = {
    "Dave Martinez": {"specialty": "Electrical", "available_slots": 3, "zone": "East"},
    "Lisa Park": {"specialty": "Structural", "available_slots": 2, "zone": "East"},
    "Carlos Reyes": {"specialty": "Plumbing/Mechanical", "available_slots": 4, "zone": "West"},
    "Ann Kowalski": {"specialty": "Fire/Life Safety", "available_slots": 2, "zone": "All"},
}

EVIDENCE_CAPABILITIES = {
    "application_intake": {
        "display_name": "Application Intake and Completeness",
        "source_system": "Dynamics 365 Customer Service and SharePoint",
        "key_field": "permit_id",
        "write": False,
        "knowledge": [
            "Classifies permit applications and validates required documents at intake.",
            "Highlights missing or duplicate items before plan review begins.",
            "Presents essential applicant, contractor, project, and fee details in one view.",
        ],
        "records": [
            {
                "permit_id": "BP-2024-3847",
                "classification": "Residential Addition",
                "applicant": "Johnson Residence",
                "documents_complete": "4 of 5",
                "missing_items": "HOA approval letter",
                "intake_decision": "Hold for missing document",
            },
            {
                "permit_id": "BP-2025-0102",
                "classification": "Residential Addition",
                "applicant": "Johnson Family Trust",
                "documents_complete": "5 of 5",
                "missing_items": "None",
                "intake_decision": "Ready for plan review",
            },
            {
                "permit_id": "BP-2025-0103",
                "classification": "Commercial Alteration",
                "applicant": "Sunrise Solar Inc.",
                "documents_complete": "6 of 6",
                "missing_items": "None",
                "intake_decision": "Ready for plan review",
            },
        ],
    },
    "code_compliance_review": {
        "display_name": "Automated Code Compliance Review",
        "source_system": "Building, electrical, plumbing, and zoning code library",
        "key_field": "review_id",
        "write": False,
        "knowledge": [
            "Checks plans across building, electrical, plumbing, and zoning requirements.",
            "Separates passing requirements from clarifications and required corrections.",
            "Estimates resubmission impact so staff can prioritize the next action.",
        ],
        "records": [
            {
                "review_id": "REV-BP-2024-3847",
                "permit_id": "BP-2024-3847",
                "requirements_checked": 247,
                "passed": 245,
                "clarifications": "Egress window manufacturer cut sheet",
                "corrections": "Add second bathroom GFCI per NEC 210.8",
                "estimated_resubmission": "1-2 days",
            },
            {
                "review_id": "REV-BP-2025-0102",
                "permit_id": "BP-2025-0102",
                "requirements_checked": 193,
                "passed": 193,
                "clarifications": "None",
                "corrections": "None",
                "estimated_resubmission": "Ready to advance",
            },
            {
                "review_id": "REV-BP-2025-0103",
                "permit_id": "BP-2025-0103",
                "requirements_checked": 214,
                "passed": 213,
                "clarifications": "Roof loading calculation",
                "corrections": "None",
                "estimated_resubmission": "1 day",
            },
        ],
    },
    "review_routing": {
        "display_name": "Intelligent Plan Review Routing",
        "source_system": "Dynamics 365 Customer Service and Microsoft Teams",
        "key_field": "routing_id",
        "write": True,
        "knowledge": [
            "Recommends reviewers based on specialization, workload, and availability.",
            "Generates a review packet containing the application, compliance checklist, property history, and zoning verification.",
            "Schedules parallel specialty reviews and drafts an applicant status notification.",
        ],
        "records": [
            {
                "routing_id": "ROUTE-BP-2024-3847",
                "permit_id": "BP-2024-3847",
                "primary_reviewer": "Mike Chen",
                "specialization": "Residential additions",
                "workload": "8 permits (moderate)",
                "parallel_reviews": "Electrical: Sarah Martinez; Plumbing: David Park",
                "packet_status": "Generated",
                "applicant_update": "Under review; 2 minor items need clarification",
            },
            {
                "routing_id": "ROUTE-BP-2025-0102",
                "permit_id": "BP-2025-0102",
                "primary_reviewer": "Tom Delgado",
                "specialization": "Residential additions",
                "workload": "5 permits (light)",
                "parallel_reviews": "Structural: Lisa Park",
                "packet_status": "Generated",
                "applicant_update": "Plan review assigned",
            },
            {
                "routing_id": "ROUTE-BP-2025-0103",
                "permit_id": "BP-2025-0103",
                "primary_reviewer": "Karen Whitfield",
                "specialization": "Commercial solar",
                "workload": "7 permits (moderate)",
                "parallel_reviews": "Electrical: Dave Martinez",
                "packet_status": "Generated",
                "applicant_update": "Specialty review scheduled",
            },
        ],
    },
    "approval_workflow": {
        "display_name": "Approval Workflow Tracking",
        "source_system": "Dynamics 365 Customer Service",
        "key_field": "workflow_id",
        "write": False,
        "knowledge": [
            "Maintains a unified timeline from intake through issuance.",
            "Surfaces reviewer feedback, applicant revisions, and correction status.",
            "Provides transparent real-time status and the next scheduled action.",
        ],
        "records": [
            {
                "workflow_id": "FLOW-BP-2024-3847",
                "permit_id": "BP-2024-3847",
                "current_stage": "Final review",
                "completed": "Intake; completeness; compliance scan; routing; corrections",
                "reviewer_feedback": "Provide egress specs and second GFCI",
                "revision_status": "Both corrections validated",
                "next_step": "Final review at 9:00 AM",
            },
            {
                "workflow_id": "FLOW-BP-2025-0102",
                "permit_id": "BP-2025-0102",
                "current_stage": "Approved",
                "completed": "Intake; review; approval",
                "reviewer_feedback": "No open comments",
                "revision_status": "Not required",
                "next_step": "Permit issuance",
            },
            {
                "workflow_id": "FLOW-BP-2025-0104",
                "permit_id": "BP-2025-0104",
                "current_stage": "Corrections required",
                "completed": "Intake; compliance scan; third review cycle",
                "reviewer_feedback": "Update seismic and life-safety sheets",
                "revision_status": "Pending applicant",
                "next_step": "Validate revised plans",
            },
        ],
    },
    "permit_issuance": {
        "display_name": "Permit Package, Inspection, and Notification",
        "source_system": "Dynamics 365 Customer Service, Microsoft Teams, and SharePoint",
        "key_field": "issuance_id",
        "write": True,
        "knowledge": [
            "Assembles the digital permit card, approved plans, safety checklist, and posting requirements.",
            "Schedules required inspections and makes assignments available to inspectors.",
            "Drafts a citizen notification with portal and mobile inspection instructions.",
        ],
        "records": [
            {
                "issuance_id": "ISSUE-BP-2024-3847",
                "permit_id": "BP-2024-3847",
                "package": "Digital card; stamped plans; safety checklist; posting requirements",
                "inspections": "Foundation; framing; rough electrical/plumbing; final",
                "notification": "Approved; digital documents available in portal",
                "status": "Ready for construction",
            },
            {
                "issuance_id": "ISSUE-BP-2025-0102",
                "permit_id": "BP-2025-0102",
                "package": "Digital card; stamped plans; posting requirements",
                "inspections": "Foundation; framing; final",
                "notification": "Approved; schedule inspections 24 hours in advance",
                "status": "Ready for construction",
            },
            {
                "issuance_id": "ISSUE-BP-2025-0103",
                "permit_id": "BP-2025-0103",
                "package": "Digital card; stamped solar plans; electrical checklist",
                "inspections": "Structural mounting; rough electrical; final electrical",
                "notification": "Inspection schedule available in portal",
                "status": "Inspection scheduled",
            },
        ],
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _calculate_fees(valuation):
    """Calculate permit fees based on project valuation."""
    fees = {}
    total = 0
    for fee_name, schedule in FEE_TABLES.items():
        amount = schedule["base"] + (valuation / 1000) * schedule["per_thousand_valuation"]
        amount = round(amount, 2)
        fees[fee_name] = amount
        total += amount
    return fees, round(total, 2)


def _review_checklist(permit_type):
    """Return review checklist items based on permit type."""
    common = [
        "Verify application completeness",
        "Confirm property ownership / authorization",
        "Zoning compliance verification",
        "Setback and height compliance",
        "Parking requirement verification",
    ]
    type_specific = {
        "new_construction": [
            "Structural engineering review",
            "Fire and life safety review",
            "Accessibility (ADA) compliance",
            "Stormwater management plan",
            "Utility connection approvals",
            "Environmental review (CEQA/NEPA if applicable)",
        ],
        "residential_addition": [
            "Structural adequacy of existing foundation",
            "Egress requirements met",
            "Energy code compliance (Title 24)",
        ],
        "commercial_alteration": [
            "Electrical load calculation review",
            "Fire alarm system impact assessment",
            "Structural load verification",
        ],
        "institutional": [
            "Structural engineering review",
            "Fire and life safety review",
            "ADA accessibility compliance",
            "School facility standards (DSA if applicable)",
            "Seismic compliance verification",
            "Hazardous materials assessment",
        ],
    }
    return common + type_specific.get(permit_type, [])


def _evidence_capability(operation_name, **kwargs):
    """Return an offline capability summary or an exact synthetic record."""
    capability = EVIDENCE_CAPABILITIES[operation_name]
    key_field = capability["key_field"]
    selector = str(kwargs.get(key_field) or kwargs.get("key") or "").strip()
    user_input = str(kwargs.get("user_input", "")).strip()
    input_tokens = {
        token.casefold()
        for token in re.findall(r"[A-Za-z0-9]+(?:[-_][A-Za-z0-9]+)*", user_input)
    }

    record = None
    for candidate in capability["records"]:
        candidate_key = str(candidate[key_field])
        normalized_key = candidate_key.casefold()
        if selector and normalized_key == selector.casefold():
            record = candidate
            break
        if not selector and user_input and normalized_key in input_tokens:
            record = candidate
            break

    if selector or user_input:
        if record is None:
            available = ", ".join(str(item[key_field]) for item in capability["records"])
            return f"**Error:** No {key_field.replace('_', ' ')} matched. Available keys: {available}."
        lines = [f"# {capability['display_name']}: {record[key_field]}\n"]
        for field, value in record.items():
            lines.append(f"- **{field.replace('_', ' ').title()}:** {value}")
        lines.append(f"- **Source System:** {capability['source_system']}")
        if capability["write"]:
            lines.extend([
                "\n## Simulated Write Receipt\n",
                f"- **Receipt:** SIM-{operation_name.upper()}-{record[key_field]}",
                f"- **Action:** {capability['display_name']}",
                "- **Result:** Simulated only; no external system was modified.",
            ])
        return "\n".join(lines)

    lines = [f"# {capability['display_name']}\n"]
    lines.append(f"**Mode:** {'Simulated write' if capability['write'] else 'Read-only'}")
    lines.append(f"**Source System:** {capability['source_system']}\n")
    lines.append("## Capability\n")
    lines.extend(f"- {item}" for item in capability["knowledge"])
    lines.append("\n## Available Records\n")
    for item in capability["records"]:
        lines.append(f"- `{item[key_field]}`")
    lines.append(f"\nProvide `{key_field}` or `key` for an exact offline lookup.")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class BuildingPermitProcessingAgent(BasicAgent):
    """Building permit processing agent for local government."""

    def __init__(self):
        self.name = "BuildingPermitProcessingAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Building Permit Processing Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "permit_status",
                            "review_checklist",
                            "inspector_assignment",
                            "fee_calculation",
                            "application_intake",
                            "code_compliance_review",
                            "review_routing",
                            "approval_workflow",
                            "permit_issuance",
                        ],
                    },
                    "permit_id": {"type": "string"},
                    "key": {
                        "type": "string",
                        "description": "Exact record key advertised by the selected evidence operation.",
                    },
                    "user_input": {
                        "type": "string",
                        "description": "Natural-language request containing an exact advertised record key.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "permit_status")
        dispatch = {
            "permit_status": self._permit_status,
            "review_checklist": self._review_checklist,
            "inspector_assignment": self._inspector_assignment,
            "fee_calculation": self._fee_calculation,
        }
        if operation in EVIDENCE_CAPABILITIES:
            return _evidence_capability(operation, **kwargs)
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        return handler(**kwargs)

    def _permit_status(self, **kwargs) -> str:
        permit_id = kwargs.get("permit_id")
        if permit_id and permit_id in PERMIT_APPLICATIONS:
            p = PERMIT_APPLICATIONS[permit_id]
            zoning = ZONING_REQUIREMENTS.get(p["zoning_district"], {})
            lines = [f"# Permit Status: {permit_id}\n"]
            lines.append(f"- **Applicant:** {p['applicant']}")
            lines.append(f"- **Address:** {p['property_address']}")
            lines.append(f"- **Parcel:** {p['parcel_id']}")
            lines.append(f"- **Type:** {p['permit_type'].replace('_', ' ').title()}")
            lines.append(f"- **Description:** {p['description']}")
            lines.append(f"- **Submitted:** {p['submitted']}")
            lines.append(f"- **Valuation:** ${p['valuation']:,.0f}")
            lines.append(f"- **Zoning:** {p['zoning_district']}")
            lines.append(f"- **Status:** {p['status'].replace('_', ' ').title()}")
            lines.append(f"- **Reviewer:** {p['assigned_reviewer']}")
            lines.append(f"- **Review Cycle:** {p['review_cycle']}")
            if zoning:
                lines.append(f"\n## Zoning Requirements — {p['zoning_district']}\n")
                lines.append(f"- Max Height: {zoning['max_height']}")
                lines.append(f"- Lot Coverage: {zoning['lot_coverage']}%")
                lines.append(f"- Parking: {zoning['parking']}")
                sb = zoning["setbacks"]
                lines.append(f"- Setbacks: Front {sb['front']}ft, Side {sb['side']}ft, Rear {sb['rear']}ft")
            return "\n".join(lines)

        live_queue = _live_permit_queue()
        if live_queue and not permit_id:
            lines = [
                "# Permit Applications Queue — Live Tenant Cases\n",
                f"Live records from {DATA_SOURCE_URL} (Aster Lane Office Systems).",
                "In this template a permit application is a Dynamics case. Pass",
                "`permit_id` (e.g. BP-2025-0101) for the embedded demo view.\n",
                "| Case | Applicant | Description | Priority | Status | Reviewer | Age | Valuation |",
                "|---|---|---|---|---|---|---|---|",
            ]
            for p in sorted(live_queue, key=lambda x: x["permit_id"]):
                valuation = (
                    "n/a — enrichment seam"
                    if p["valuation"] is None
                    else f"${p['valuation']:,.0f}"
                )
                lines.append(
                    f"| {p['permit_id']} | {p['applicant']} | {p['description']} "
                    f"| {p['priority']} | {p['status']} | {p['reviewer']} "
                    f"| {p['age_days']}d | {valuation} |"
                )
            open_count = sum(1 for p in live_queue if p["open"])
            lines.append(f"\n**Open permit cases:** {open_count} of {len(live_queue)} matched")
            lines.append(
                "Valuation, parcel, and zoning need your land-management system — "
                "wire it at the LIVE DATA SEAM."
            )
            return "\n".join(lines)

        lines = ["# Permit Applications Dashboard\n"]
        lines.append("| Permit ID | Applicant | Type | Valuation | Status | Reviewer |")
        lines.append("|---|---|---|---|---|---|")
        for pid, p in PERMIT_APPLICATIONS.items():
            lines.append(
                f"| {pid} | {p['applicant']} | {p['permit_type'].replace('_', ' ').title()} "
                f"| ${p['valuation']:,.0f} | {p['status'].replace('_', ' ').title()} | {p['assigned_reviewer']} |"
            )
        total_val = sum(p["valuation"] for p in PERMIT_APPLICATIONS.values())
        lines.append(f"\n**Total Applications:** {len(PERMIT_APPLICATIONS)}")
        lines.append(f"**Total Valuation:** ${total_val:,.0f}")
        return "\n".join(lines)

    def _review_checklist(self, **kwargs) -> str:
        permit_id = kwargs.get("permit_id", "BP-2025-0101")
        p = PERMIT_APPLICATIONS.get(permit_id, list(PERMIT_APPLICATIONS.values())[0])
        checklist = _review_checklist(p["permit_type"])
        lines = [f"# Review Checklist: {permit_id}\n"]
        lines.append(f"**Project:** {p['description']}")
        lines.append(f"**Type:** {p['permit_type'].replace('_', ' ').title()}")
        lines.append(f"**Reviewer:** {p['assigned_reviewer']}\n")
        for i, item in enumerate(checklist, 1):
            lines.append(f"- [ ] {i}. {item}")
        lines.append(f"\n**Total Items:** {len(checklist)}")
        return "\n".join(lines)

    def _inspector_assignment(self, **kwargs) -> str:
        lines = ["# Inspector Assignment\n"]
        lines.append("## Available Inspectors\n")
        lines.append("| Inspector | Specialty | Available Slots | Zone |")
        lines.append("|---|---|---|---|")
        for name, info in INSPECTORS.items():
            lines.append(f"| {name} | {info['specialty']} | {info['available_slots']} | {info['zone']} |")
        lines.append("\n## Scheduled Inspections\n")
        for pid, inspections in INSPECTION_SCHEDULE.items():
            p = PERMIT_APPLICATIONS.get(pid, {})
            lines.append(f"### {pid} — {p.get('property_address', 'Unknown')}\n")
            lines.append("| Type | Inspector | Date | Status |")
            lines.append("|---|---|---|---|")
            for insp in inspections:
                lines.append(f"| {insp['type']} | {insp['inspector']} | {insp['date']} | {insp['status'].title()} |")
            lines.append("")
        return "\n".join(lines)

    def _fee_calculation(self, **kwargs) -> str:
        permit_id = kwargs.get("permit_id")
        lines = ["# Permit Fee Calculation\n"]
        permits_to_calc = {}
        if permit_id and permit_id in PERMIT_APPLICATIONS:
            permits_to_calc = {permit_id: PERMIT_APPLICATIONS[permit_id]}
        else:
            permits_to_calc = PERMIT_APPLICATIONS
        for pid, p in permits_to_calc.items():
            fees, total = _calculate_fees(p["valuation"])
            lines.append(f"## {pid}: {p['applicant']}\n")
            lines.append(f"**Project Valuation:** ${p['valuation']:,.0f}\n")
            lines.append("| Fee Category | Amount |")
            lines.append("|---|---|")
            for fee_name, amount in fees.items():
                display = fee_name.replace("_", " ").title()
                lines.append(f"| {display} | ${amount:,.2f} |")
            lines.append(f"| **Total** | **${total:,.2f}** |")
            lines.append("")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = BuildingPermitProcessingAgent()
    print("LIVE TENANT PERMIT QUEUE (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="permit_status"))
    print("\n" + "=" * 80 + "\n")
    print("EMBEDDED DEMO PERMIT (works offline)")
    print(agent.perform(operation="permit_status", permit_id="BP-2025-0101"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="review_checklist", permit_id="BP-2025-0104"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="inspector_assignment"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="fee_calculation", permit_id="BP-2025-0101"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
