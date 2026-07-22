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
