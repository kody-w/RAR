---
name: "rar-aibast-agents-library-field-service-dispatch"
description: "Dispatches from live simulated Dynamics 365 work orders with a telemetry alert overlay, routing, crews, and an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/field_service_dispatch", "rar_sha256": "3df888f1d02db30e680e318c4aebdd3e6793e8b395d3832b771f3dc3aa9d65a1", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.3.0", "author": "AIBAST", "tags": ["field-service", "dispatch", "routing", "technicians", "emergency", "energy"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/field_service_dispatch`. The original RAPP
agent is preserved byte-for-byte in `field_service_dispatch_agent.py` and in the RCI capsule.

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

Field Service Dispatch Agent — a template you are meant to mutate.

Manages field service operations including dispatch dashboards, route
optimization, technician assignment based on skills, and emergency response
coordination for energy infrastructure maintenance.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted systems (synthetic data, no credentials, works
     from anywhere):
       CRM  https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
            — 15 Field Service work orders + bookable crews
       TEL  https://kody-w.github.io/static-telemetry/api/v1/
            — sensors, alerts, and 672-point reading series
     The dispatch board overlays the three ACTIVE telemetry alerts,
     each joined to its real CRM case by ticket number: vibration_spike
     -> CAS-260132 (Granite Peak), temperature_excursion -> CAS-260138
     (Harbor Lights), load_fault -> CAS-260128 (Prairie Wind).
     Try: perform(operation="dispatch_dashboard")
     (live work orders PLUS the active-alert overlay with its CRM
     case joins)
  2. No network? Everything falls back to the embedded demo layer below
     (TECHNICIANS / SERVICE_REQUESTS / OUTAGES) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     FIELD_SERVICE_DISPATCH_DATA_URL (CRM) and/or
     FIELD_SERVICE_DISPATCH_TEL_URL (telemetry) to your own endpoints
     (your real Dynamics org, your IoT/monitoring platform), or replace
     _fetch_collection() / _fetch_telemetry() with your own API client.
     Fields the rest of the file needs are listed in
     _normalize_live_workorder() — everything else keeps working
     untouched. Fields marked "enrichment seam" in the output
     (estimated hours, certifications) are where you wire your
     scheduling and HR systems.

OPERATIONS
  dispatch_dashboard | route_optimization | technician_assignment
  | emergency_response | optimized_schedule | outage_orchestration
  | crew_status_updates | post_incident_review | follow_on_work_orders
  kwargs: operation (required), zone, outage_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The dispatch operation to perform.",
      "enum": [
        "dispatch_dashboard",
        "route_optimization",
        "technician_assignment",
        "emergency_response",
        "optimized_schedule",
        "outage_orchestration",
        "crew_status_updates",
        "post_incident_review",
        "follow_on_work_orders"
      ],
      "type": "string"
    },
    "outage_id": {
      "description": "Exact outage ID for orchestration and incident operations.",
      "type": "string"
    },
    "zone": {
      "description": "Optional geographic zone filter.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `field_service_dispatch_agent.py` and embedded as the fenced Python below (sha256 3df888f1d02db30e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `field_service_dispatch_agent.py` first:

```bash
python3 field_service_dispatch_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 field_service_dispatch_agent.py   # or on stdin
python3 field_service_dispatch_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Field Service Dispatch Agent — a template you are meant to mutate.

Manages field service operations including dispatch dashboards, route
optimization, technician assignment based on skills, and emergency response
coordination for energy infrastructure maintenance.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted systems (synthetic data, no credentials, works
     from anywhere):
       CRM  https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
            — 15 Field Service work orders + bookable crews
       TEL  https://kody-w.github.io/static-telemetry/api/v1/
            — sensors, alerts, and 672-point reading series
     The dispatch board overlays the three ACTIVE telemetry alerts,
     each joined to its real CRM case by ticket number: vibration_spike
     -> CAS-260132 (Granite Peak), temperature_excursion -> CAS-260138
     (Harbor Lights), load_fault -> CAS-260128 (Prairie Wind).
     Try: perform(operation="dispatch_dashboard")
     (live work orders PLUS the active-alert overlay with its CRM
     case joins)
  2. No network? Everything falls back to the embedded demo layer below
     (TECHNICIANS / SERVICE_REQUESTS / OUTAGES) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     FIELD_SERVICE_DISPATCH_DATA_URL (CRM) and/or
     FIELD_SERVICE_DISPATCH_TEL_URL (telemetry) to your own endpoints
     (your real Dynamics org, your IoT/monitoring platform), or replace
     _fetch_collection() / _fetch_telemetry() with your own API client.
     Fields the rest of the file needs are listed in
     _normalize_live_workorder() — everything else keeps working
     untouched. Fields marked "enrichment seam" in the output
     (estimated hours, certifications) are where you wire your
     scheduling and HR systems.

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
    "version": "1.3.0",
    "display_name": "Field Service Dispatch Agent",
    "description": "Dispatches from live simulated Dynamics 365 work orders with a telemetry alert overlay, routing, crews, and an offline demo fallback.",
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


# Sibling live source: the static-telemetry API. Its three ACTIVE
# alerts overlay the dispatch board, each joined to its real CRM case
# by ticket number. Override with FIELD_SERVICE_DISPATCH_TEL_URL.
TELEMETRY_SOURCE_URL = os.environ.get(
    "FIELD_SERVICE_DISPATCH_TEL_URL",
    "https://kody-w.github.io/static-telemetry/api/v1",
)


def _fetch_telemetry(path, key="value", timeout=6):
    """Bounded GET against the telemetry API, cached in _LIVE_CACHE by
    full URL. Returns [] on ANY failure — offline-safe. Reading series
    are large (672 points each) — fetch them lazily, at most a couple
    per run (the dispatch overlay needs none)."""
    url = f"{TELEMETRY_SOURCE_URL}/{path}.json"
    if url in _LIVE_CACHE:
        return _LIVE_CACHE[url]
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "rapp-agent-template/1.0"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8")).get(key, [])
    except Exception:
        data = []
    _LIVE_CACHE[url] = data
    return data


def _active_alert_overlay():
    """Live telemetry alerts joined to their real CRM cases by ticket
    number (vibration_spike -> CAS-260132, temperature_excursion ->
    CAS-260138, load_fault -> CAS-260128); [] when offline."""
    alerts = _fetch_telemetry("alerts")
    if not alerts:
        return []
    cases = {
        c.get("ticketnumber"): c for c in _fetch_collection("incidents")
    }
    rows = []
    for a in alerts:
        case = cases.get(a.get("crm_case")) or {}
        unit = a.get("unit", "")
        rows.append({
            "alert": a.get("alert_code", "?"),
            "type": a.get("alert_type", "?"),
            "severity": str(a.get("severity", "?")),
            "asset": a.get("asset_name", "?"),
            "account": a.get("account_name", "?"),
            "reading": f"{a.get('peak_value')} {unit}".strip(),
            "threshold": f"{a.get('threshold')} {unit}".strip(),
            "case": a.get("crm_case") or "n/a",
            "case_title": case.get("title", "n/a — case not found"),
            "case_status": (
                "Open" if case.get("statecode") == 0
                else ("Resolved" if case else "?")
            ),
        })
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
            overlay = _active_alert_overlay()
            if overlay:
                lines.extend([
                    "",
                    "## Active Telemetry Alerts (live overlay)",
                    "",
                    "| Severity | Alert | Type | Asset | Account | Reading vs Threshold | CRM Case | Case Status |",
                    "|----------|-------|------|-------|---------|----------------------|----------|-------------|",
                ])
                for a in overlay:
                    lines.append(
                        f"| {a['severity'].upper()} | {a['alert']} | {a['type']} "
                        f"| {a['asset']} | {a['account']} "
                        f"| {a['reading']} vs {a['threshold']} "
                        f"| {a['case']} | {a['case_status']} |"
                    )
                lines.append("")
                lines.append("**Alert-linked CRM cases:**")
                for a in overlay:
                    lines.append(
                        f"- {a['case']}: {a['case_title']} ({a['case_status']})"
                    )
                lines.append("")
                lines.append(
                    "_Source: live static-telemetry alerts joined to Static "
                    "Dynamics 365 cases by ticket number. Dispatch a crew "
                    "against the alert's CRM case, not the raw signal._"
                )
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
    print("LIVE TENANT WORK ORDERS + TELEMETRY ALERT OVERLAY")
    print("(alerts joined to CRM cases CAS-260132/CAS-260138/CAS-260128; falls back offline)")
    print(agent.perform(operation="dispatch_dashboard"))
    print()
    print("=" * 60)
    print("EMBEDDED DEMO CREWS (works offline)")
    for op in ["route_optimization", "technician_assignment", "emergency_response"]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
