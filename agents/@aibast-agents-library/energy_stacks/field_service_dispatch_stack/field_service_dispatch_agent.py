"""
Field Service Dispatch Agent — a template you are meant to mutate.

Manages field service operations including dispatch dashboards, route
optimization, technician assignment based on skills, and emergency response
coordination for energy infrastructure maintenance.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live work orders and crew rosters over real
     HTTP from the globally hosted Static Dynamics 365 tenant (Aster
     Lane Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     The tenant's 15 Field Service work orders drive the dashboard —
     e.g. WO-260100, a High-priority printer fault for Cedar Hollow
     Printing that is still Unscheduled.
     Try: perform(operation="dispatch_dashboard")
  2. No network? Everything falls back to the embedded demo layer below
     (TECHNICIANS / SERVICE_REQUESTS / OUTAGES) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     FIELD_SERVICE_DISPATCH_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your FSM system), or
     replace _fetch_collection() with your own API client. Fields the
     rest of the file needs are listed in _normalize_live_workorder() —
     everything else keeps working untouched. Fields marked "enrichment
     seam" in the output (estimated hours, certifications) are where you
     wire your scheduling and HR systems.

OPERATIONS
  dispatch_dashboard | route_optimization | technician_assignment
  | emergency_response | optimized_schedule | outage_orchestration
  | crew_status_updates | post_incident_review | follow_on_work_orders
  kwargs: operation (required), zone, outage_id
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/field_service_dispatch",
    "version": "1.2.0",
    "display_name": "Field Service Dispatch Agent",
    "description": "Dispatches from live work orders on a simulated Dynamics 365 tenant, with routing, crews, outage response, and an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["field-service", "dispatch", "routing", "technicians", "emergency", "energy"],
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
#   export FIELD_SERVICE_DISPATCH_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your FSM client. Downstream code
# only needs the fields produced by _normalize_live_workorder().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "FIELD_SERVICE_DISPATCH_DATA_URL",
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


_WO_STATUS = {
    690970000: "unscheduled",
    690970001: "scheduled",
    690970002: "in_progress",
    690970003: "completed",
    690970004: "posted",
    690970005: "closed",
}


def _normalize_live_workorder(row):
    """Project a Dynamics Field Service work order onto the request
    shape this agent uses. THIS is the contract your replacement data
    source must meet — a dict with these keys. None means 'not available
    from the work order alone' and the renderers label it as an
    enrichment seam."""
    return {
        "id": row.get("msdyn_name", ""),
        "title": f"{row.get('msdyn_primaryincidenttypename', 'Service')} — "
                 f"{row.get('msdyn_serviceaccountname', 'Unknown account')}",
        "priority": str(row.get("msdyn_priorityname", "Normal")).lower(),
        "type": row.get("msdyn_workordertypename", "service"),
        "zone": row.get("msdyn_stateorprovince", "?"),
        "location": f"{row.get('msdyn_city', '?')}, {row.get('msdyn_stateorprovince', '?')}",
        "status": _WO_STATUS.get(row.get("msdyn_systemstatus"), "unknown"),
        "estimated_hours": None,  # enrichment seam — wire your scheduling engine
        "_live": True,
    }


def _live_workorders():
    """Live tenant work orders as request dicts; [] when offline."""
    return [_normalize_live_workorder(w) for w in _fetch_collection("msdyn_workorders")]


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

TECHNICIANS = {
    "TECH-201": {
        "name": "Carlos Rivera",
        "certifications": ["electrical_high_voltage", "transformer_maintenance", "confined_space"],
        "zone": "West",
        "status": "available",
        "current_location": "Sacramento, CA",
        "jobs_today": 1,
        "max_jobs": 4,
        "efficiency_rating": 94,
        "years_experience": 12,
    },
    "TECH-202": {
        "name": "Amy Blackwell",
        "certifications": ["wind_turbine", "electrical_high_voltage", "crane_operation"],
        "zone": "Central",
        "status": "on_job",
        "current_location": "Sweetwater, TX",
        "jobs_today": 2,
        "max_jobs": 4,
        "efficiency_rating": 91,
        "years_experience": 8,
    },
    "TECH-203": {
        "name": "Raj Patel",
        "certifications": ["gas_turbine", "combustion_systems", "electrical_high_voltage"],
        "zone": "West",
        "status": "available",
        "current_location": "Bakersfield, CA",
        "jobs_today": 0,
        "max_jobs": 4,
        "efficiency_rating": 97,
        "years_experience": 15,
    },
    "TECH-204": {
        "name": "Sarah Johansson",
        "certifications": ["pipeline_inspection", "welding_api1104", "hazmat"],
        "zone": "Northeast",
        "status": "available",
        "current_location": "Scranton, PA",
        "jobs_today": 1,
        "max_jobs": 4,
        "efficiency_rating": 88,
        "years_experience": 6,
    },
    "TECH-205": {
        "name": "Marcus Thompson",
        "certifications": ["electrical_high_voltage", "transformer_maintenance", "scada_systems"],
        "zone": "Central",
        "status": "on_break",
        "current_location": "Denver, CO",
        "jobs_today": 2,
        "max_jobs": 4,
        "efficiency_rating": 92,
        "years_experience": 10,
    },
}

SERVICE_REQUESTS = {
    "SR-4001": {
        "title": "Transformer oil leak - Ridgeline Substation",
        "priority": "high",
        "type": "corrective",
        "required_certs": ["transformer_maintenance", "electrical_high_voltage"],
        "zone": "Central",
        "location": "Moffat County, CO",
        "equipment": "Substation Transformer B-12",
        "estimated_hours": 6,
        "status": "unassigned",
    },
    "SR-4002": {
        "title": "Quarterly turbine blade inspection - Sweetwater",
        "priority": "medium",
        "type": "preventive",
        "required_certs": ["wind_turbine"],
        "zone": "Central",
        "location": "Nolan County, TX",
        "equipment": "Wind Turbine Alpha-7",
        "estimated_hours": 4,
        "status": "assigned",
    },
    "SR-4003": {
        "title": "Gas turbine fuel nozzle replacement",
        "priority": "high",
        "type": "corrective",
        "required_certs": ["gas_turbine", "combustion_systems"],
        "zone": "West",
        "location": "Sacramento, CA",
        "equipment": "Gas Turbine GT-3A",
        "estimated_hours": 8,
        "status": "unassigned",
    },
    "SR-4004": {
        "title": "Pipeline cathodic protection survey",
        "priority": "medium",
        "type": "preventive",
        "required_certs": ["pipeline_inspection"],
        "zone": "Northeast",
        "location": "Lackawanna County, PA",
        "equipment": "Gas Pipeline Segment NE-14",
        "estimated_hours": 5,
        "status": "unassigned",
    },
    "SR-4005": {
        "title": "Emergency: SCADA communication failure",
        "priority": "critical",
        "type": "emergency",
        "required_certs": ["scada_systems", "electrical_high_voltage"],
        "zone": "Central",
        "location": "Denver, CO",
        "equipment": "Ridgeline Substation SCADA",
        "estimated_hours": 3,
        "status": "unassigned",
    },
}

GEOGRAPHIC_ZONES = {
    "West": {"states": ["CA", "NV", "OR", "WA"], "technicians": 2, "open_requests": 1},
    "Central": {"states": ["TX", "CO", "OK", "KS", "NM"], "technicians": 2, "open_requests": 3},
    "Northeast": {"states": ["PA", "NY", "NJ", "CT", "MA"], "technicians": 1, "open_requests": 1},
}

OUTAGES = {
    "OUT-901": {
        "site": "Ridgeline Regional Hospital feeder",
        "zone": "Central",
        "priority": "critical",
        "customers_impacted": 18400,
        "required_certs": ["scada_systems", "electrical_high_voltage"],
        "crew_id": "TECH-205",
        "distance_miles": 8,
        "eta_minutes": 22,
        "restoration_estimate": "2026-03-20T16:30:00Z",
        "active_order": "SR-4002",
        "customer_channel": "SMS and email",
    },
    "OUT-902": {
        "site": "Riverside water treatment feeder",
        "zone": "West",
        "priority": "critical",
        "customers_impacted": 7200,
        "required_certs": ["electrical_high_voltage"],
        "crew_id": "TECH-201",
        "distance_miles": 12,
        "eta_minutes": 28,
        "restoration_estimate": "2026-03-20T17:10:00Z",
        "active_order": "SR-4001",
        "customer_channel": "SMS and utility portal",
    },
    "OUT-903": {
        "site": "Sweetwater north collector",
        "zone": "Central",
        "priority": "high",
        "customers_impacted": 3100,
        "required_certs": ["wind_turbine"],
        "crew_id": "TECH-202",
        "distance_miles": 15,
        "eta_minutes": 34,
        "restoration_estimate": "2026-03-20T18:00:00Z",
        "active_order": "SR-4004",
        "customer_channel": "email and utility portal",
    },
}

INCIDENT_RESULTS = {
    "OUT-901": {
        "actual_response_minutes": 19,
        "sla_minutes": 30,
        "restoration_minutes": 96,
        "avoided_outage_cost": 245000,
        "response_cost": 32000,
        "first_time_fix": True,
        "preventive_action": "Replace aging SCADA radio and add redundant telemetry.",
        "resilience_action": "Prioritize critical-facility feeder telemetry in the resilience plan.",
    },
    "OUT-902": {
        "actual_response_minutes": 26,
        "sla_minutes": 30,
        "restoration_minutes": 118,
        "avoided_outage_cost": 171000,
        "response_cost": 28000,
        "first_time_fix": True,
        "preventive_action": "Inspect feeder relays and stage a replacement breaker.",
        "resilience_action": "Pre-stage switching plans for essential public-service sites.",
    },
    "OUT-903": {
        "actual_response_minutes": 33,
        "sla_minutes": 45,
        "restoration_minutes": 142,
        "avoided_outage_cost": 92000,
        "response_cost": 21000,
        "first_time_fix": False,
        "preventive_action": "Add quarterly collector-cable thermal imaging.",
        "resilience_action": "Increase wind-farm cable spares at the Central depot.",
    },
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _dispatch_dashboard():
    priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    requests = []
    for sid, sr in SERVICE_REQUESTS.items():
        requests.append({
            "id": sid, "title": sr["title"], "priority": sr["priority"],
            "type": sr["type"], "zone": sr["zone"], "location": sr["location"],
            "status": sr["status"], "estimated_hours": sr["estimated_hours"],
        })
    requests.sort(key=lambda x: priority_order.get(x["priority"], 9))
    available = sum(1 for t in TECHNICIANS.values() if t["status"] == "available")
    unassigned = sum(1 for sr in SERVICE_REQUESTS.values() if sr["status"] == "unassigned")
    return {"requests": requests, "available_techs": available, "unassigned_requests": unassigned,
            "total_requests": len(requests)}


def _route_optimization():
    routes = []
    for zone_name, zone in GEOGRAPHIC_ZONES.items():
        zone_techs = [t for t in TECHNICIANS.values() if t["zone"] == zone_name]
        zone_reqs = [sr for sr in SERVICE_REQUESTS.values() if sr["zone"] == zone_name]
        total_hrs = sum(sr["estimated_hours"] for sr in zone_reqs)
        tech_capacity = sum(t["max_jobs"] - t["jobs_today"] for t in zone_techs)
        routes.append({
            "zone": zone_name, "states": zone["states"],
            "technicians": len(zone_techs), "open_requests": len(zone_reqs),
            "total_hours": total_hrs, "remaining_capacity": tech_capacity,
            "utilization_pct": round((1 - tech_capacity / (len(zone_techs) * 4)) * 100, 1) if zone_techs else 0,
        })
    return {"routes": routes}


def _technician_assignment():
    assignments = []
    for sid, sr in SERVICE_REQUESTS.items():
        if sr["status"] != "unassigned":
            continue
        candidates = []
        for tid, t in TECHNICIANS.items():
            has_certs = all(c in t["certifications"] for c in sr["required_certs"])
            in_zone = t["zone"] == sr["zone"]
            available = t["status"] in ("available", "on_break")
            has_capacity = t["jobs_today"] < t["max_jobs"]
            if has_certs and has_capacity:
                candidates.append({
                    "tech_id": tid, "name": t["name"],
                    "in_zone": in_zone, "status": t["status"],
                    "efficiency": t["efficiency_rating"],
                    "score": t["efficiency_rating"] + (10 if in_zone else 0) + (5 if available else 0),
                })
        candidates.sort(key=lambda x: x["score"], reverse=True)
        assignments.append({
            "request_id": sid, "title": sr["title"], "priority": sr["priority"],
            "required_certs": sr["required_certs"],
            "best_candidate": candidates[0] if candidates else None,
            "total_candidates": len(candidates),
        })
    return {"assignments": assignments}


def _emergency_response():
    emergencies = [sr for sr in SERVICE_REQUESTS.values() if sr["type"] == "emergency" or sr["priority"] == "critical"]
    response_plan = []
    for em in emergencies:
        eligible = []
        for tid, t in TECHNICIANS.items():
            if all(c in t["certifications"] for c in em["required_certs"]):
                eligible.append({"id": tid, "name": t["name"], "status": t["status"], "location": t["current_location"]})
        response_plan.append({
            "title": em["title"], "priority": em["priority"],
            "location": em["location"], "equipment": em["equipment"],
            "estimated_hours": em["estimated_hours"],
            "eligible_responders": eligible,
        })
    return {"emergencies": response_plan, "total": len(response_plan)}


def _optimized_schedule():
    plan = [
        ("SR-4005", "TECH-205", "08:00", 18, 3),
        ("SR-4001", "TECH-201", "09:00", 24, 6),
        ("SR-4003", "TECH-203", "09:30", 16, 8),
        ("SR-4004", "TECH-204", "10:00", 21, 5),
        ("SR-4002", "TECH-202", "13:00", 12, 4),
    ]
    return [
        {
            "request_id": request_id,
            "technician": TECHNICIANS[tech_id]["name"],
            "start": start,
            "travel_minutes": travel,
            "job_hours": hours,
            "skill_match": "qualified",
        }
        for request_id, tech_id, start, travel, hours in plan
    ]


def _outage_orchestration(outage_id):
    outage = OUTAGES.get(outage_id)
    if not outage:
        return None
    technician = TECHNICIANS[outage["crew_id"]]
    return {
        **outage,
        "outage_id": outage_id,
        "crew": technician["name"],
        "crew_status": technician["status"],
    }


def _crew_status_updates():
    statuses = [
        ("OUT-901", "Crew on site; SCADA radio isolated", 65),
        ("OUT-902", "Crew en route; switching plan approved", 20),
        ("OUT-903", "Collector cable fault located", 48),
    ]
    return [
        {
            "outage_id": outage_id,
            "site": OUTAGES[outage_id]["site"],
            "crew": TECHNICIANS[OUTAGES[outage_id]["crew_id"]]["name"],
            "status": status,
            "progress_pct": progress,
            "customers_impacted": OUTAGES[outage_id]["customers_impacted"],
            "restoration_estimate": OUTAGES[outage_id]["restoration_estimate"],
        }
        for outage_id, status, progress in statuses
    ]


def _post_incident_review(outage_id):
    outage = OUTAGES.get(outage_id)
    result = INCIDENT_RESULTS.get(outage_id)
    if not outage or not result:
        return None
    return {
        **result,
        "outage_id": outage_id,
        "site": outage["site"],
        "customers_impacted": outage["customers_impacted"],
        "roi_pct": round(
            (result["avoided_outage_cost"] - result["response_cost"])
            / result["response_cost"] * 100,
            1,
        ),
    }


def _follow_on_work_order(outage_id):
    review = _post_incident_review(outage_id)
    if not review:
        return None
    return {
        "work_order_id": f"WO-{outage_id[4:]}-F1",
        "outage_id": outage_id,
        "site": review["site"],
        "action": review["preventive_action"],
        "target_date": "2026-04-15",
        "monthly_gain": (
            f"{review['actual_response_minutes']} minute response; "
            f"${review['avoided_outage_cost'] - review['response_cost']:,} net avoided cost"
        ),
    }


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

class FieldServiceDispatchAgent(BasicAgent):
    """Field service dispatch and technician management agent."""

    def __init__(self):
        self.name = "FieldServiceDispatchAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "dispatch_dashboard",
                            "route_optimization",
                            "technician_assignment",
                            "emergency_response",
                            "optimized_schedule",
                            "outage_orchestration",
                            "crew_status_updates",
                            "post_incident_review",
                            "follow_on_work_orders",
                        ],
                        "description": "The dispatch operation to perform.",
                    },
                    "zone": {
                        "type": "string",
                        "description": "Optional geographic zone filter.",
                    },
                    "outage_id": {
                        "type": "string",
                        "description": "Exact outage ID for orchestration and incident operations.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "dispatch_dashboard")
        if op == "dispatch_dashboard":
            return self._dispatch_dashboard()
        elif op == "route_optimization":
            return self._route_optimization()
        elif op == "technician_assignment":
            return self._technician_assignment()
        elif op == "emergency_response":
            return self._emergency_response()
        elif op == "optimized_schedule":
            return self._optimized_schedule()
        elif op == "outage_orchestration":
            return self._outage_orchestration(kwargs.get("outage_id"))
        elif op == "crew_status_updates":
            return self._crew_status_updates()
        elif op == "post_incident_review":
            return self._post_incident_review(kwargs.get("outage_id"))
        elif op == "follow_on_work_orders":
            return self._follow_on_work_orders(kwargs.get("outage_id"))
        return f"**Error:** Unknown operation `{op}`."

    def _dispatch_dashboard(self) -> str:
        live = _live_workorders()
        if live:
            resources = _fetch_collection("bookableresources")
            bookings = _fetch_collection("bookableresourcebookings")
            priority_order = {"critical": 0, "high": 1, "normal": 2, "medium": 2, "low": 3}
            live.sort(key=lambda r: (priority_order.get(r["priority"], 9), r["id"]))
            unassigned = sum(1 for r in live if r["status"] == "unscheduled")
            lines = [
                "# Field Service Dispatch Dashboard (live tenant data)",
                "",
                f"**Total Work Orders:** {len(live)} | "
                f"**Unscheduled:** {unassigned} | "
                f"**Bookable Crews:** {len(resources)} "
                f"({len(bookings)} bookings on record)",
                "",
                "| Priority | Work Order | Request | Type | Location | Hours | Status |",
                "|----------|------------|---------|------|----------|-------|--------|",
            ]
            for r in live:
                lines.append(
                    f"| {r['priority'].upper()} | {r['id']} | {r['title']} | {r['type']} "
                    f"| {r['location']} | n/a — enrichment seam | {r['status']} |"
                )
            lines.append("")
            lines.append("_Source: live Static Dynamics 365 tenant (msdyn_workorders + "
                         "bookableresources). Estimated hours are an enrichment seam — "
                         "wire your scheduling engine._")
            return "\n".join(lines)

        data = _dispatch_dashboard()
        lines = [
            "# Field Service Dispatch Dashboard (embedded demo data — offline)",
            "",
            f"**Total Requests:** {data['total_requests']} | "
            f"**Unassigned:** {data['unassigned_requests']} | "
            f"**Available Techs:** {data['available_techs']}",
            "",
            "| Priority | Request | Type | Zone | Location | Hours | Status |",
            "|----------|---------|------|------|----------|-------|--------|",
        ]
        for r in data["requests"]:
            lines.append(
                f"| {r['priority'].upper()} | {r['title']} | {r['type']} "
                f"| {r['zone']} | {r['location']} | {r['estimated_hours']}h | {r['status']} |"
            )
        return "\n".join(lines)

    def _route_optimization(self) -> str:
        data = _route_optimization()
        lines = [
            "# Route Optimization by Zone",
            "",
            "| Zone | States | Technicians | Open Requests | Total Hours | Capacity | Utilization |",
            "|------|--------|------------|---------------|-------------|----------|-------------|",
        ]
        for r in data["routes"]:
            lines.append(
                f"| {r['zone']} | {', '.join(r['states'])} | {r['technicians']} "
                f"| {r['open_requests']} | {r['total_hours']}h | {r['remaining_capacity']} slots | {r['utilization_pct']}% |"
            )
        return "\n".join(lines)

    def _technician_assignment(self) -> str:
        data = _technician_assignment()
        lines = ["# Technician Assignment Recommendations", ""]
        for a in data["assignments"]:
            lines.append(f"## {a['request_id']}: {a['title']}")
            lines.append(f"Priority: {a['priority'].upper()} | Required Certs: {', '.join(a['required_certs'])}")
            lines.append(f"Candidates: {a['total_candidates']}")
            if a["best_candidate"]:
                bc = a["best_candidate"]
                lines.append(f"**Recommended:** {bc['name']} (score: {bc['score']}, efficiency: {bc['efficiency']}%, in-zone: {bc['in_zone']})")
            else:
                lines.append("**No eligible technicians available.**")
            lines.append("")
        return "\n".join(lines)

    def _emergency_response(self) -> str:
        data = _emergency_response()
        if data["total"] == 0:
            return "# Emergency Response\n\nNo active emergencies."
        lines = [
            "# Emergency Response Plan",
            "",
            f"**Active Emergencies:** {data['total']}",
            "",
        ]
        for em in data["emergencies"]:
            lines.append(f"## {em['title']}")
            lines.append(f"- Priority: {em['priority'].upper()}")
            lines.append(f"- Location: {em['location']}")
            lines.append(f"- Equipment: {em['equipment']}")
            lines.append(f"- Estimated Hours: {em['estimated_hours']}")
            lines.append("")
            lines.append("**Eligible Responders:**")
            lines.append("")
            lines.append("| Technician | Status | Current Location |")
            lines.append("|-----------|--------|-----------------|")
            for r in em["eligible_responders"]:
                lines.append(f"| {r['name']} | {r['status']} | {r['location']} |")
            lines.append("")
        return "\n".join(lines)

    def _optimized_schedule(self) -> str:
        rows = _optimized_schedule()
        lines = [
            "# Optimized Daily Schedule",
            "",
            f"**Total Travel:** {sum(row['travel_minutes'] for row in rows)} minutes",
            f"**Crew Capacity Used:** {sum(row['job_hours'] for row in rows)} hours",
            "",
            "| Start | Request | Technician | Travel | Job | Skill Match |",
            "|-------|---------|------------|--------|-----|-------------|",
        ]
        for row in rows:
            lines.append(
                f"| {row['start']} | {row['request_id']} | {row['technician']} "
                f"| {row['travel_minutes']} min | {row['job_hours']}h | {row['skill_match']} |"
            )
        lines.extend([
            "",
            "**Evidence:** Field Service Dispatch demo 00:47-01:07 — intelligently "
            "assigned jobs, reduced travel, and maximized crew capacity.",
        ])
        return "\n".join(lines)

    def _outage_orchestration(self, outage_id) -> str:
        if not outage_id:
            return (
                "# Outage Orchestration\n\nProvide an exact `outage_id`. "
                f"Available IDs: {', '.join(sorted(OUTAGES))}."
            )
        row = _outage_orchestration(outage_id)
        if not row:
            return f"**Error:** Unknown outage_id `{outage_id}`."
        return "\n".join([
            f"# Outage Orchestration — {outage_id}",
            "",
            f"- **Critical Site:** {row['site']}",
            f"- **Customers Impacted:** {row['customers_impacted']:,}",
            f"- **Nearest Qualified Crew:** {row['crew']} ({row['distance_miles']} miles)",
            f"- **Dispatch ETA:** {row['eta_minutes']} minutes",
            f"- **Restoration Estimate:** {row['restoration_estimate']}",
            "",
            "## Simulated Write Receipt",
            "",
            f"- **Dispatch:** Simulated assignment of {row['crew']} in Dynamics 365 Field Service.",
            f"- **Reprioritization:** Simulated pause and reroute of {row['active_order']}.",
            f"- **Customer Update:** Simulated notification through {row['customer_channel']}.",
            "- **Mode:** dry-run; no work order, crew schedule, or customer record was mutated.",
            "- **Evidence:** Field Service Dispatch demo 01:08-01:30.",
        ])

    def _crew_status_updates(self) -> str:
        lines = [
            "# Real-Time Crew and Customer Impact Status",
            "",
            "| Outage | Site | Crew | Status | Progress | Customers | Restoration Estimate |",
            "|--------|------|------|--------|----------|-----------|----------------------|",
        ]
        for row in _crew_status_updates():
            lines.append(
                f"| {row['outage_id']} | {row['site']} | {row['crew']} | {row['status']} "
                f"| {row['progress_pct']}% | {row['customers_impacted']:,} "
                f"| {row['restoration_estimate']} |"
            )
        lines.extend([
            "",
            "**Evidence:** Field Service Dispatch demo 01:31-01:46 — live crew "
            "updates, customer impact analysis, and timeline estimates.",
        ])
        return "\n".join(lines)

    def _post_incident_review(self, outage_id) -> str:
        if not outage_id:
            return (
                "# Post-Incident Review\n\nProvide an exact `outage_id`. "
                f"Available IDs: {', '.join(sorted(INCIDENT_RESULTS))}."
            )
        row = _post_incident_review(outage_id)
        if not row:
            return f"**Error:** Unknown outage_id `{outage_id}`."
        first_fix = "YES" if row["first_time_fix"] else "NO"
        return "\n".join([
            f"# Post-Incident Review — {outage_id}",
            "",
            f"- **Site:** {row['site']}",
            f"- **Response:** {row['actual_response_minutes']} min vs {row['sla_minutes']} min SLA",
            f"- **Restoration:** {row['restoration_minutes']} minutes",
            f"- **First-Time Fix:** {first_fix}",
            f"- **Avoided Outage Cost:** ${row['avoided_outage_cost']:,}",
            f"- **Response Cost:** ${row['response_cost']:,}",
            f"- **ROI:** {row['roi_pct']}%",
            f"- **Preventive Action:** {row['preventive_action']}",
            f"- **Resilience Plan:** {row['resilience_action']}",
            "",
            "**Evidence:** Field Service Dispatch demo 01:47-02:03 — performance "
            "metrics, impact, ROI, preventive actions, and resilience planning.",
        ])

    def _follow_on_work_orders(self, outage_id) -> str:
        if not outage_id:
            return (
                "# Follow-On Work Orders\n\nProvide an exact `outage_id`. "
                f"Available IDs: {', '.join(sorted(INCIDENT_RESULTS))}."
            )
        row = _follow_on_work_order(outage_id)
        if not row:
            return f"**Error:** Unknown outage_id `{outage_id}`."
        return "\n".join([
            f"# Follow-On Work Order — {row['work_order_id']}",
            "",
            f"- **Site:** {row['site']}",
            f"- **Preventive Action:** {row['action']}",
            f"- **Target Date:** {row['target_date']}",
            f"- **Monthly Operational Gain:** {row['monthly_gain']}",
            "",
            "## Simulated Write Receipt",
            "",
            "- **Action:** Create the follow-on work order in Dynamics 365 Field Service.",
            "- **Leadership Summary:** Simulated monthly operational-gains publication.",
            "- **Mode:** dry-run; no live work order or leadership record was mutated.",
            "- **Evidence:** Field Service Dispatch demo 02:03-02:16.",
        ])


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    agent = FieldServiceDispatchAgent()
    print("=" * 60)
    print("LIVE TENANT WORK ORDERS (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="dispatch_dashboard"))
    print()
    print("=" * 60)
    print("EMBEDDED DEMO CREWS (works offline)")
    for op in ["route_optimization", "technician_assignment", "emergency_response"]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
