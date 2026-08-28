---
name: "rar-aibast-agents-library-emission-tracking"
description: "Tracks GHG compliance events from a simulated Dynamics 365 tenant with telemetry load-proxy aggregates, plus an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/emission_tracking", "rar_sha256": "a10361576bd03c8e6e27fe7c2cd6c92325dc2c594ecbef167adcad2fa34a2392", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.3.0", "author": "AIBAST", "tags": ["emissions", "carbon", "compliance", "ghg", "sustainability", "energy"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/emission_tracking`. The original RAPP
agent is preserved byte-for-byte in `emission_tracking_agent.py` and in the RCI capsule.

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

Emission Tracking Agent — a template you are meant to mutate.

Monitors greenhouse gas emissions across facilities, tracks regulatory
compliance, develops reduction plans, and analyzes carbon offset opportunities.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted systems (synthetic data, no credentials, works
     from anywhere):
       CRM  https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
            — cases at Energy-industry accounts become compliance events
       TEL  https://kody-w.github.io/static-telemetry/api/v1/
            — sensors, alerts, and 672-point reading series
     The two join on the shared world: the live load_fault alert on
     Prairie Wind Energy Cooperative's feeder breaker F-7 carries the
     real CRM case number CAS-260128 ("Substation feeder fault flagged
     in telemetry export"), and load/power reading series become
     load-proxy aggregates. Converting those aggregates to tonnes CO2e
     needs an emission factor telemetry cannot know — that stays an
     enrichment seam.
     Try: perform(operation="compliance_status")
     (renders the CRM compliance cases PLUS the telemetry load overlay
     joined on CAS-260128)
  2. No network? Everything falls back to the embedded demo layer below
     (FACILITIES / CARBON_OFFSETS / REGULATIONS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     EMISSION_TRACKING_DATA_URL (CRM) and/or EMISSION_TRACKING_TEL_URL
     (telemetry) to your own endpoints (your real Dynamics org, your
     CEMS/metering platform), or replace _fetch_collection() /
     _fetch_telemetry() with your own API client. Fields the rest of
     the file needs are listed in _normalize_live_event() — everything
     else keeps working untouched. Fields marked "enrichment seam" in
     the output (tonnes CO2e, emission factors) are where you wire your
     emissions metering / CEMS platform.

OPERATIONS
  emissions_dashboard | compliance_status | reduction_plan
  | carbon_offset_analysis | strategic_implementation_plan
  kwargs: operation (required), facility_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "facility_id": {
      "description": "Optional facility ID to filter results.",
      "type": "string"
    },
    "operation": {
      "description": "The emission tracking operation to perform.",
      "enum": [
        "emissions_dashboard",
        "compliance_status",
        "reduction_plan",
        "carbon_offset_analysis",
        "strategic_implementation_plan"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `emission_tracking_agent.py` and embedded as the fenced Python below (sha256 a10361576bd03c8e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `emission_tracking_agent.py` first:

```bash
python3 emission_tracking_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 emission_tracking_agent.py   # or on stdin
python3 emission_tracking_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Emission Tracking Agent — a template you are meant to mutate.

Monitors greenhouse gas emissions across facilities, tracks regulatory
compliance, develops reduction plans, and analyzes carbon offset opportunities.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted systems (synthetic data, no credentials, works
     from anywhere):
       CRM  https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
            — cases at Energy-industry accounts become compliance events
       TEL  https://kody-w.github.io/static-telemetry/api/v1/
            — sensors, alerts, and 672-point reading series
     The two join on the shared world: the live load_fault alert on
     Prairie Wind Energy Cooperative's feeder breaker F-7 carries the
     real CRM case number CAS-260128 ("Substation feeder fault flagged
     in telemetry export"), and load/power reading series become
     load-proxy aggregates. Converting those aggregates to tonnes CO2e
     needs an emission factor telemetry cannot know — that stays an
     enrichment seam.
     Try: perform(operation="compliance_status")
     (renders the CRM compliance cases PLUS the telemetry load overlay
     joined on CAS-260128)
  2. No network? Everything falls back to the embedded demo layer below
     (FACILITIES / CARBON_OFFSETS / REGULATIONS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     EMISSION_TRACKING_DATA_URL (CRM) and/or EMISSION_TRACKING_TEL_URL
     (telemetry) to your own endpoints (your real Dynamics org, your
     CEMS/metering platform), or replace _fetch_collection() /
     _fetch_telemetry() with your own API client. Fields the rest of
     the file needs are listed in _normalize_live_event() — everything
     else keeps working untouched. Fields marked "enrichment seam" in
     the output (tonnes CO2e, emission factors) are where you wire your
     emissions metering / CEMS platform.

OPERATIONS
  emissions_dashboard | compliance_status | reduction_plan
  | carbon_offset_analysis | strategic_implementation_plan
  kwargs: operation (required), facility_id
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/emission_tracking",
    "version": "1.3.0",
    "display_name": "Emission Tracking Agent",
    "description": "Tracks GHG compliance events from a simulated Dynamics 365 tenant with telemetry load-proxy aggregates, plus an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["emissions", "carbon", "compliance", "ghg", "sustainability", "energy"],
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
#   export EMISSION_TRACKING_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your EHS/CEMS client. Downstream
# code only needs the fields produced by _normalize_live_event().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "EMISSION_TRACKING_DATA_URL",
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


# Sibling live source: the static-telemetry API. Load/power reading
# series become load-proxy aggregates, and the load_fault alert joins
# the CRM compliance case CAS-260128 (Prairie Wind Energy Cooperative).
# Override with EMISSION_TRACKING_TEL_URL.
TELEMETRY_SOURCE_URL = os.environ.get(
    "EMISSION_TRACKING_TEL_URL",
    "https://kody-w.github.io/static-telemetry/api/v1",
)


def _fetch_telemetry(path, key="value", timeout=6):
    """Bounded GET against the telemetry API, cached in _LIVE_CACHE by
    full URL. Returns [] on ANY failure — offline-safe. Reading series
    are large (672 points each) — fetch them lazily, at most a couple
    per run."""
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


def _reading_aggregates(sensor_id):
    """avg/max/latest over one live reading series; None offline."""
    points = _fetch_telemetry(f"readings/{sensor_id}", key="points")
    values = [p.get("v") for p in points if isinstance(p.get("v"), (int, float))]
    if not values:
        return None
    return {
        "n": len(values),
        "avg": round(sum(values) / len(values), 2),
        "max": max(values),
        "latest": values[-1],
    }


def _load_proxy_rows(limit=2):
    """Load-proxy aggregates from live load/power sensors. The feeder
    load sensor (Prairie Wind Energy Cooperative — the account behind
    compliance case CAS-260128) is picked first. Converting a load
    proxy to tonnes CO2e requires an emission factor telemetry cannot
    know — the renderer labels it as an enrichment seam. Fetches at
    most `limit` reading series per run."""
    sensors = _fetch_telemetry("sensors")
    if not sensors:
        return []
    picks = [s for s in sensors if "load" in str(s.get("sensor_type", ""))]
    picks += [
        s for s in sensors
        if "power" in str(s.get("sensor_type", "")) and s not in picks
    ]
    rows = []
    for s in picks[:limit]:
        agg = _reading_aggregates(s.get("sensor_id"))
        if not agg:
            continue
        rows.append({
            "sensor": s.get("sensor_code", "?"),
            "type": s.get("sensor_type", "?"),
            "unit": s.get("unit", ""),
            "account": s.get("account_name", "?"),
            "asset": s.get("asset_name", "?"),
            "agg": agg,
        })
    return rows


def _load_fault_alert():
    """The live load_fault alert (joins CRM case CAS-260128); None
    when offline."""
    for a in _fetch_telemetry("alerts"):
        if a.get("alert_type") == "load_fault":
            return a
    return None


def _normalize_live_event(row):
    """Project a Dynamics case onto the compliance-event shape this
    agent uses. THIS is the contract your replacement data source must
    meet — a dict with these keys. None means 'not available from CRM
    alone' and the renderers label it as an enrichment seam. In this
    template a case at an Energy-industry account is reinterpreted as an
    environmental/telemetry compliance event."""
    return {
        "facility": row.get("customeridname", "Unknown"),
        "case": row.get("ticketnumber", ""),
        "event": row.get("title", "untitled"),
        "priority": {1: "High", 2: "Normal", 3: "Low"}.get(row.get("prioritycode"), "Normal"),
        "status": "Open" if row.get("statecode") == 0 else "Resolved",
        "opened": str(row.get("createdon", ""))[:10],
        "co2_impact_tonnes": None,  # enrichment seam — wire your CEMS / metering
        "_live": True,
    }


def _live_compliance_events():
    """Compliance events at live Energy-industry accounts; [] offline."""
    accounts = _fetch_collection("accounts")
    if not accounts:
        return []
    energy_names = {
        a["name"] for a in accounts
        if "energy" in str(a.get("industrycode", "")).lower() and a.get("name")
    }
    return [
        _normalize_live_event(i)
        for i in _fetch_collection("incidents")
        if i.get("customeridname") in energy_names
    ]


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

FACILITIES = {
    "FAC-E01": {
        "name": "Riverside Generating Station",
        "location": "Sacramento, CA",
        "type": "natural_gas_plant",
        "capacity_mw": 340,
        "emissions": {
            "scope_1": {"co2_tonnes": 482000, "ch4_tonnes": 1240, "n2o_tonnes": 85},
            "scope_2": {"co2_tonnes": 12400, "ch4_tonnes": 0, "n2o_tonnes": 0},
            "scope_3": {"co2_tonnes": 38500, "ch4_tonnes": 280, "n2o_tonnes": 15},
        },
        "regulatory_threshold_co2": 500000,
        "reduction_target_pct": 15,
        "baseline_year": 2022,
        "baseline_co2": 545000,
    },
    "FAC-E02": {
        "name": "Sweetwater Wind Farm",
        "location": "Nolan County, TX",
        "type": "wind_farm",
        "capacity_mw": 180,
        "emissions": {
            "scope_1": {"co2_tonnes": 0, "ch4_tonnes": 0, "n2o_tonnes": 0},
            "scope_2": {"co2_tonnes": 3200, "ch4_tonnes": 0, "n2o_tonnes": 0},
            "scope_3": {"co2_tonnes": 8400, "ch4_tonnes": 12, "n2o_tonnes": 2},
        },
        "regulatory_threshold_co2": 25000,
        "reduction_target_pct": 5,
        "baseline_year": 2022,
        "baseline_co2": 14200,
    },
    "FAC-E03": {
        "name": "Ridgeline Coal Station",
        "location": "Moffat County, CO",
        "type": "coal_plant",
        "capacity_mw": 520,
        "emissions": {
            "scope_1": {"co2_tonnes": 1420000, "ch4_tonnes": 3800, "n2o_tonnes": 420},
            "scope_2": {"co2_tonnes": 18200, "ch4_tonnes": 0, "n2o_tonnes": 0},
            "scope_3": {"co2_tonnes": 95000, "ch4_tonnes": 1200, "n2o_tonnes": 85},
        },
        "regulatory_threshold_co2": 1500000,
        "reduction_target_pct": 30,
        "baseline_year": 2022,
        "baseline_co2": 1780000,
    },
    "FAC-E04": {
        "name": "Bayshore Refinery",
        "location": "Beaumont, TX",
        "type": "refinery",
        "capacity_mw": 0,
        "emissions": {
            "scope_1": {"co2_tonnes": 890000, "ch4_tonnes": 5600, "n2o_tonnes": 210},
            "scope_2": {"co2_tonnes": 42000, "ch4_tonnes": 0, "n2o_tonnes": 0},
            "scope_3": {"co2_tonnes": 2100000, "ch4_tonnes": 8400, "n2o_tonnes": 320},
        },
        "regulatory_threshold_co2": 1000000,
        "reduction_target_pct": 20,
        "baseline_year": 2022,
        "baseline_co2": 1050000,
    },
}

CARBON_OFFSETS = {
    "OFF-001": {"project": "Appalachian Reforestation", "type": "forestry", "credits_available": 45000, "price_per_tonne": 18.50, "vintage": 2025, "verified_by": "Verra VCS"},
    "OFF-002": {"project": "Texas Wind REC Bundle", "type": "renewable_energy", "credits_available": 120000, "price_per_tonne": 12.75, "vintage": 2026, "verified_by": "Green-e"},
    "OFF-003": {"project": "Montana Methane Capture", "type": "methane_capture", "credits_available": 28000, "price_per_tonne": 24.00, "vintage": 2025, "verified_by": "ACR"},
    "OFF-004": {"project": "Iowa Agricultural Soil Carbon", "type": "soil_carbon", "credits_available": 35000, "price_per_tonne": 22.00, "vintage": 2026, "verified_by": "Gold Standard"},
}

REGULATIONS = {
    "EPA_GHGRP": {"name": "EPA GHG Reporting Program", "threshold_co2": 25000, "deadline": "2026-03-31"},
    "CA_CAPANDTRADE": {"name": "California Cap-and-Trade", "threshold_co2": 25000, "deadline": "2026-04-01"},
    "EPA_NSPS": {"name": "EPA New Source Performance Standards", "threshold_co2": 0, "deadline": "2026-06-30"},
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _emissions_dashboard():
    dashboard = []
    for fid, f in FACILITIES.items():
        s1 = f["emissions"]["scope_1"]["co2_tonnes"]
        s2 = f["emissions"]["scope_2"]["co2_tonnes"]
        s3 = f["emissions"]["scope_3"]["co2_tonnes"]
        total = s1 + s2 + s3
        dashboard.append({
            "id": fid, "name": f["name"], "type": f["type"],
            "scope_1": s1, "scope_2": s2, "scope_3": s3, "total": total,
            "threshold": f["regulatory_threshold_co2"],
            "pct_of_threshold": round(s1 / f["regulatory_threshold_co2"] * 100, 1) if f["regulatory_threshold_co2"] else 0,
        })
    total_all = sum(d["total"] for d in dashboard)
    return {"facilities": dashboard, "total_emissions": total_all}


def _compliance_status():
    statuses = []
    for fid, f in FACILITIES.items():
        s1 = f["emissions"]["scope_1"]["co2_tonnes"]
        threshold = f["regulatory_threshold_co2"]
        compliant = s1 <= threshold
        gap = s1 - threshold if not compliant else 0
        current_reduction = round((1 - s1 / f["baseline_co2"]) * 100, 1) if f["baseline_co2"] else 0
        statuses.append({
            "id": fid, "name": f["name"],
            "scope_1_co2": s1, "threshold": threshold,
            "compliant": compliant, "gap_tonnes": gap,
            "target_reduction_pct": f["reduction_target_pct"],
            "actual_reduction_pct": current_reduction,
            "on_track": current_reduction >= f["reduction_target_pct"],
        })
    return {"statuses": statuses}


def _reduction_plan():
    plans = []
    for fid, f in FACILITIES.items():
        s1 = f["emissions"]["scope_1"]["co2_tonnes"]
        target = round(f["baseline_co2"] * (1 - f["reduction_target_pct"] / 100))
        remaining = max(0, s1 - target)
        actions = []
        if f["type"] == "coal_plant":
            actions = [
                {"action": "Fuel switching to natural gas", "reduction_tonnes": 400000, "cost_mm": 85.0},
                {"action": "Carbon capture retrofit", "reduction_tonnes": 300000, "cost_mm": 120.0},
                {"action": "Efficiency upgrades", "reduction_tonnes": 50000, "cost_mm": 12.0},
            ]
        elif f["type"] == "natural_gas_plant":
            actions = [
                {"action": "Heat recovery optimization", "reduction_tonnes": 25000, "cost_mm": 4.5},
                {"action": "Turbine efficiency upgrade", "reduction_tonnes": 18000, "cost_mm": 8.0},
                {"action": "Methane leak detection and repair", "reduction_tonnes": 8000, "cost_mm": 1.2},
            ]
        elif f["type"] == "refinery":
            actions = [
                {"action": "Process electrification", "reduction_tonnes": 120000, "cost_mm": 45.0},
                {"action": "Flare gas recovery", "reduction_tonnes": 35000, "cost_mm": 6.0},
                {"action": "Hydrogen integration", "reduction_tonnes": 80000, "cost_mm": 55.0},
            ]
        plans.append({
            "id": fid, "name": f["name"], "current_co2": s1,
            "target_co2": target, "remaining_reduction": remaining,
            "actions": actions,
        })
    return {"plans": plans}


def _carbon_offset_analysis():
    total_gap = 0
    for f in FACILITIES.values():
        s1 = f["emissions"]["scope_1"]["co2_tonnes"]
        target = round(f["baseline_co2"] * (1 - f["reduction_target_pct"] / 100))
        total_gap += max(0, s1 - target)
    offsets = []
    for oid, o in CARBON_OFFSETS.items():
        total_cost = round(o["credits_available"] * o["price_per_tonne"])
        offsets.append({
            "id": oid, "project": o["project"], "type": o["type"],
            "credits": o["credits_available"], "price": o["price_per_tonne"],
            "total_cost": total_cost, "verified_by": o["verified_by"],
        })
    total_credits = sum(o["credits"] for o in offsets)
    total_cost = sum(o["total_cost"] for o in offsets)
    return {"offsets": offsets, "total_credits": total_credits,
            "total_cost": total_cost, "emission_gap": total_gap}


def _strategic_implementation_plan():
    plan = _reduction_plan()["plans"]
    phases = []
    phase_number = 1
    for facility in plan:
        for action in facility["actions"][:1]:
            phases.append({
                "phase": phase_number,
                "facility": facility["name"],
                "action": action["action"],
                "window": f"2026-Q{phase_number}",
                "owner": ["Operations", "Sustainability", "Engineering"][phase_number - 1],
                "reduction_tonnes": action["reduction_tonnes"],
                "cost_mm": action["cost_mm"],
                "success_metric": f"Verify {action['reduction_tonnes']:,} tonnes annual CO2e reduction",
            })
            phase_number += 1
    return phases


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

class EmissionTrackingAgent(BasicAgent):
    """GHG emission monitoring and compliance tracking agent."""

    def __init__(self):
        self.name = "EmissionTrackingAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "emissions_dashboard",
                            "compliance_status",
                            "reduction_plan",
                            "carbon_offset_analysis",
                            "strategic_implementation_plan",
                        ],
                        "description": "The emission tracking operation to perform.",
                    },
                    "facility_id": {
                        "type": "string",
                        "description": "Optional facility ID to filter results.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "emissions_dashboard")
        if op == "emissions_dashboard":
            return self._emissions_dashboard()
        elif op == "compliance_status":
            return self._compliance_status()
        elif op == "reduction_plan":
            return self._reduction_plan()
        elif op == "carbon_offset_analysis":
            return self._carbon_offset_analysis()
        elif op == "strategic_implementation_plan":
            return self._strategic_implementation_plan()
        return f"**Error:** Unknown operation `{op}`."

    def _emissions_dashboard(self) -> str:
        data = _emissions_dashboard()
        lines = [
            "# Emissions Dashboard",
            "",
            f"**Total Portfolio Emissions:** {data['total_emissions']:,} tonnes CO2e",
            "",
            "| Facility | Type | Scope 1 | Scope 2 | Scope 3 | Total | % of Threshold |",
            "|----------|------|---------|---------|---------|-------|---------------|",
        ]
        for f in data["facilities"]:
            lines.append(
                f"| {f['name']} | {f['type']} | {f['scope_1']:,} | {f['scope_2']:,} "
                f"| {f['scope_3']:,} | {f['total']:,} | {f['pct_of_threshold']}% |"
            )
        return "\n".join(lines)

    def _compliance_status(self) -> str:
        events = _live_compliance_events()
        if events:
            open_events = [e for e in events if e["status"] == "Open"]
            lines = [
                "# Compliance Status (live tenant data)",
                "",
                f"**Energy-sector compliance events on record:** {len(events)} "
                f"({len(open_events)} open)",
                "**Metered CO2e impact:** n/a — enrichment seam (wire your CEMS / metering)",
                "",
                "| Case | Facility | Event | Priority | Status | Opened | CO2e Impact |",
                "|------|----------|-------|----------|--------|--------|-------------|",
            ]
            for e in sorted(events, key=lambda x: (x["status"] != "Open", x["opened"])):
                lines.append(
                    f"| {e['case']} | {e['facility']} | {e['event']} | {e['priority']} "
                    f"| {e['status']} | {e['opened']} | n/a — enrichment seam |"
                )
            lines.append("")
            lines.append("_Source: live Static Dynamics 365 tenant (accounts + incidents). "
                         "A case at an Energy-industry account is reinterpreted as an "
                         "environmental/telemetry compliance event._")
            alert = _load_fault_alert()
            proxies = _load_proxy_rows()
            if alert or proxies:
                lines.extend(["", "## Live Telemetry Load Overlay", ""])
            if alert:
                unit = alert.get("unit", "")
                lines.extend([
                    f"- **{alert.get('alert_code', '?')} {alert.get('alert_type', '?')}** "
                    f"({str(alert.get('severity', '?')).upper()}): "
                    f"{alert.get('asset_name', '?')} at {alert.get('account_name', '?')} — "
                    f"peak {alert.get('peak_value')} {unit} vs threshold "
                    f"{alert.get('threshold')} {unit}",
                    f"- **Joined CRM case:** {alert.get('crm_case', 'n/a')} "
                    "(the compliance event in the table above)",
                    f"- **Alert window:** {alert.get('window_start', '?')} -> "
                    f"{alert.get('window_end', '?')}",
                    "",
                ])
            if proxies:
                lines.extend([
                    "| Sensor | Signal | Account | Avg | Max | Latest | Samples | CO2e Impact |",
                    "|--------|--------|---------|-----|-----|--------|---------|-------------|",
                ])
                for p in proxies:
                    a, u = p["agg"], p["unit"]
                    lines.append(
                        f"| {p['sensor']} | {p['type']} | {p['account']} "
                        f"| {a['avg']} {u} | {a['max']} {u} | {a['latest']} {u} "
                        f"| {a['n']} @ 15 min | n/a — enrichment seam (emission factor) |"
                    )
                lines.append("")
                lines.append(
                    "_Source: live static-telemetry sensors, alerts, and reading "
                    "series. Load-proxy aggregates are real; converting them to "
                    "tonnes CO2e needs an emission factor from your CEMS/metering "
                    "platform — that column is an enrichment seam._"
                )
            return "\n".join(lines)

        data = _compliance_status()
        lines = [
            "# Compliance Status (embedded demo data — offline)",
            "",
            "| Facility | Scope 1 CO2 | Threshold | Compliant | Gap | Target Reduction | Actual |",
            "|----------|-------------|-----------|-----------|-----|-----------------|--------|",
        ]
        for s in data["statuses"]:
            comp = "YES" if s["compliant"] else "NO"
            track = "On Track" if s["on_track"] else "Behind"
            lines.append(
                f"| {s['name']} | {s['scope_1_co2']:,} | {s['threshold']:,} "
                f"| {comp} | {s['gap_tonnes']:,} | {s['target_reduction_pct']}% | {s['actual_reduction_pct']}% ({track}) |"
            )
        return "\n".join(lines)

    def _reduction_plan(self) -> str:
        data = _reduction_plan()
        lines = ["# Emission Reduction Plans", ""]
        for p in data["plans"]:
            if not p["actions"]:
                continue
            lines.append(f"## {p['name']}")
            lines.append(f"Current: {p['current_co2']:,} tonnes | Target: {p['target_co2']:,} tonnes | Gap: {p['remaining_reduction']:,} tonnes")
            lines.append("")
            lines.append("| Action | Reduction (tonnes) | Cost ($M) |")
            lines.append("|--------|-------------------|----------|")
            for a in p["actions"]:
                lines.append(f"| {a['action']} | {a['reduction_tonnes']:,} | ${a['cost_mm']}M |")
            lines.append("")
        return "\n".join(lines)

    def _carbon_offset_analysis(self) -> str:
        data = _carbon_offset_analysis()
        lines = [
            "# Carbon Offset Analysis",
            "",
            f"**Emission Gap to Cover:** {data['emission_gap']:,} tonnes",
            f"**Total Credits Available:** {data['total_credits']:,} tonnes",
            f"**Total Offset Cost:** ${data['total_cost']:,}",
            "",
            "| Project | Type | Credits | Price/t | Total Cost | Verified By |",
            "|---------|------|---------|---------|-----------|-------------|",
        ]
        for o in data["offsets"]:
            lines.append(
                f"| {o['project']} | {o['type']} | {o['credits']:,} "
                f"| ${o['price']:.2f} | ${o['total_cost']:,} | {o['verified_by']} |"
            )
        return "\n".join(lines)

    def _strategic_implementation_plan(self) -> str:
        phases = _strategic_implementation_plan()
        total_cost = sum(row["cost_mm"] for row in phases)
        total_reduction = sum(row["reduction_tonnes"] for row in phases)
        lines = [
            "# Strategic Emissions Implementation Plan",
            "",
            f"**Planned Investment:** ${total_cost:.1f}M",
            f"**Expected Annual Reduction:** {total_reduction:,} tonnes CO2e",
            "",
            "| Phase | Window | Facility | Action | Owner | Reduction | Cost | Success Metric |",
            "|-------|--------|----------|--------|-------|-----------|------|----------------|",
        ]
        for row in phases:
            lines.append(
                f"| {row['phase']} | {row['window']} | {row['facility']} | {row['action']} "
                f"| {row['owner']} | {row['reduction_tonnes']:,} t | ${row['cost_mm']}M "
                f"| {row['success_metric']} |"
            )
        lines.extend([
            "",
            "**Evidence:** Energy Operations demo 02:47-03:02 — opportunity cost "
            "analysis followed by a strategic implementation plan.",
        ])
        return "\n".join(lines)


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    agent = EmissionTrackingAgent()
    print("=" * 60)
    print("LIVE TENANT COMPLIANCE EVENTS + TELEMETRY LOAD OVERLAY")
    print("(CRM cases joined to the load_fault alert on CAS-260128; falls back offline)")
    print(agent.perform(operation="compliance_status"))
    print()
    print("=" * 60)
    print("EMBEDDED DEMO PORTFOLIO (works offline)")
    print(agent.perform(operation="emissions_dashboard"))
    for op in ["reduction_plan", "carbon_offset_analysis"]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/6272bLrxrUl+iuMXQ/HNiShJ0BVnHsvWqIlQDQEwKsTMvqG6IgedPnfK7n22ltyWXbVQ61QSCSQOXO2Y46pSP7tSzhPRTd8+fkLI7OM7Xz54UuSjvFQ9lPZteCxM4TxYzycpfMh7pq+LsM2Tg/pkrbTeMiGrjmEh7Fs5jqc0uTA723YlPF4wI/kYUrbsJ0OazkV4HOdNuk07Ie6C5Mf+6Hb9kOY50Oag43jD4e+nsdD2B66LKvLNj0kadMdsrCuI3D+T0CtdAvB8en45ef//79++FKCz19+/tuXuA5H8OiL0JTjCDT+ULdscyYHCoJdddjm4HW/Aytb8L1Ph6wbGvAoSbPD57c/jWmd/XD4y18eazjk458PP/4/h3Eafv6lPXz+df3hPw9f3/6Up9OffvnSgb3h20e/fPnh8MuX9PP88dckHIuoC4fkly9//k1AmX3I+M9/tfR3Z73/hnSah/bw1uunX/9gw59+Jzqtfyf8txj9Ok7hNI//XvQ/Lf+Xgoc0meO3vb/2wKf/Xuo/rv3XuoZDBNaAiI/p9GvYhvU+lv87hf9wz788AkQRpFdexr++EwZkYDuF/4dG/Nutvz/wc1f2y5e//EUYhm74+S9/Objto+1WkM7f0uTw1791/d//+tMvX778HaRvC8R/9dE7e//bfzvoZTx0Y5dNBzvu5ukwzO1UNukv7S+tU5TjAfwzFSk4bEmHsYzq9HMdqKQq/RAESufw1/8vLKNwnH4M3/k//liX0RAOO/wthX6dPuvjrz8dHCCuG8q8BE48WIxp/tJ+7Hof1Q/pmA4LqOhon9IfQZH8+P5wKIEd/yTr149tP/X7X0EBJ+81b00tTj7EYT/OdfrT2wqvSNtPnWNQ5+mWxjOQWHcxOD4r6zcIgFO7eknBfqDD+Cjr+pCUAzCvA8Dxlg288vNb2F//+ldgZvFL+7Ww8cNXyBphsOC7OocfAc6kAE7yYvqlTeOiO/zH3/7+H4f/cfh3uz6Ev88wAbJ8+hxoqNjG5QDqf24+kO8dwDRMPnz+t79/ehOIadPhACJUZmX6dTMAs0eafHOtLTE/YuTxEKXApcCdTd8NE3DhoZx+OsjZ4bu+4ND3KwCJh6IbJwCHfdomaRvvQGoIzPnuybabDiNIsTHbfzjMY/px6l9B2D9UbH6NwfK/HnTOPExdV4N/vdX8WAQ2d20J3P898F+fAyHDf4wH9puInw6Xd9Yd+nAI+2IIP8/Iwq9x6YbDt+1AeHho0/WX9h9r5qt7wCLgmfgzpD++Y/7uKQ0I7Pjt7I81H63E6UAep8Mv7fiZ3uHwDkXcAVX2Qz6XyRu2/vtnSo1FN9fJh/+Apm9Jn1FIPqPykYPfusThW5s4fPSJwy8zhqAE0B1Y27872WHv5o8Dm/TdwoBdzQxM+ZrJOvAasHw8gO6VtuBg4JA8HA/fcfoQvmt5fHuorMupfKf29LWPgn73bpXAb7+0v4HvDyC+S1p3/XvBJ3Ye3jgDNr7T/gPnXiCjvsLf4Sv8AXB558jcfhzxoZpkeAdHku2DI+imxjjCwTMs1X6DFfrTwQCOAgn79k7UbSDnDv1c1yPI0eWrawcQiLd/v6a85Djm1xbveMYn3uV1F4GmvH9kJXDuuL8zZDz8adxbIHd6hzecwh8ObXeIgS3Au2VYAzPWbniMn0K+0oZ2X4t0SP/8Gwhzln44FNPUjz/D8KNL9h/Xn3LAHubop7KD3w2qjH9MPinGj4BiwGFfwu/z4OX0Ewb/I5p/BjUG+QoiMh0EkAX5/mPZJvP4JiJhDDLnXcsRsLxJ/5nefBfnCNr/Xq/vDOdDqQX9Y23GtB1B6oCw1iko76/hPVLYj30Hyuft9+SdlqACQUg/JbxrZ1q7QwWWHLqvdTIWIDuTt1fr5OdPoFnSD3L1axbO9fT1ALD8U4gJqhnIPHjA/k9XHLjusz0tKaj3LAXhGg4R0OEB/iv+SL3TbfgEsk8xH4nxjtPbrYd2biKwlGPsH7EjgmL0ATAje47Gr2X/TeRXhbIa8L03FH4lRO3vOGG6vRMZEKav/nhbAffd+jURf+eQz1B9ivhDJvkTsKoFKfyBqgDlgZa/vXwX8tQBOBgPnIF9k9MCLT+457cC/oS23yn4ibPvnv4tkm8YBiwx3N9bPyWlLcC34g17QOGw+elbAIf95+9c8zsj+M8/ZGvfiMWfhjfeD1+byIfDf0vPryltaq798fYfufVHAdfh/innnTQgUYBRv0Xp4wwMwHoHbJ/elfn/HoQ3rIK+C7z2Zt3A1QCvPvwFTkhBmJMEiPlg5UD4O08AXq3flBUZTtZkRxbsAwwOsljj8qshirbgvB9YwtkFYCQbF/vPv7kv/Wwb7bu5fAqKQXcpgG2fU8CHA/GfDjrIyDdcAVQePmr5vVuTb8KBZxzmYAuM/lWfn4Hfp09Zgi7bNjjzV8diOFW+nH99L/7VtbTDn4BD//xONRhE+Z/XgXp/L/tm3Hf//vntj7cOhze1A/H5KFoAfh/PPkrj+wDUDfkPH2s/pXCCbsNACshj4OJ3k3lnA0j47r0TfAdx/TVLp7gApLyuv/a8P/358A1GPt991wW8+hisvqvDmIBv1eWbxBzEMq2Tb+RlfIP+p5SPvv3uu585P7xx4wPIQT3+2gKNwrp8pb++weTXDxT80/eIpd8z5Fu216C4HmkKutY7h952ATzt5rhIk+86NOEA+M977PnH2vjlCzjyd1qBJt6D9vSn35XnD/9rQYLJ7K3xR9v46NBr+fXDNyf/1oG/exr+8Px3h390ScMUrK/p+N73B+MVoIj/VJrg2f8yA4G9/+PwxwMJePHvRw+w9+s4+fPvRgRQ888ZmJSAtPjkDvuvZfIeY8sYNI70y88taNg/fAE5lv6bofdN1D4cML5HZICQ/RsP049vv5cLvv7jsG98fHjz8c9VB5l/5zxImekDjAGbn8b3ND7t/VsDYCQ49z3RfLfin6U6HwjyGclvQ8PvzAYHfILjx5wPmgqY8f9oTAZv/yks4Nk/huW96A9jAl7825h8+a9/Muvvb+FfQ/JW6Tcbf1vaRe/x6+2Bbyn2dgDwfvjmJZ/+/5zQwHIwjf04vhkrjP6EvHUPh6+TB3j3fzq7fW4DFACMEmBfiCL4ESWpY5QgeEynxxSjspSKsTg5xicMx8gEfCZPRBqDuQM9UmEShwmWhTgRYvgJezsG1BBw6ZuNl29VEPREHIk0BHtx7BSRSXo8RUSYHU8n6njKSJREUwxDf7cVKJZ82vfVnrfzvo+Rbz98mvm3L9GRACslYpSZr38cTCOnENUj+65lkHVDzchgSeUsKPIu3QMqqd0zhl19QY5x3fFZwdnPN0s9RXgyzGKd89ZlN2fxRCzQdR83MoHvyqPCs0o6S52F3rxbHULqcdqkc9qacFZizMhfuoGAVN1/icWidKoApycYXuFKY6VXEdPOeouKxyLKo9bmNC8rmL/fV9P0XiMpnqVCOeu3UcwfFi5nmqcx94qsr/nZPG+oEGzYS91IalHuR/m8v9jVk70yedirnFlhE8frI095OixXOyqvWVUw08msZ10Yr/rIzJWUry1NwtTzsp1fegDPhOgSbRyUQSqWghsp+pOxGJU2cxK+H3Xz/pDxo4hm7XI7Z7CzE/A0rQUlGuWKechZUh/twlKjYr6EJQjmltIz48Su56oaL50wmOvVtdYVx7HAsY/BBOYbzbReq8Ew5qnJ2krKfFikRp0QLN0bIN43zyGasi6D6ddoXGszlXVRthbelLlGWpKC607FiT97OpOXPBqap122T7ZJPrSzc1yXM9VfHoIFT5SP6MpxaQJsaZQs02Yy8KnxxiQYHLfqyplLdo59E37FQurjBWVchnTdQNwd5FLAVGF0JMkbTsmloyT3z6mpidWL78okq7dzkGmy3N4ldyO1ujxyzO4xItm5qglBXugK81mbrxxR6Ce+JwpAX+TAY3wPsRKrm6LXK8sSstSQXMUYtDAfq1gIoxzup7X0VOmhYwlUsIF520pPowjhpiCFkuGK4GBVAiusiXN1BnWNwNNIXamznK6cBV9X5/aycgU7EwIr5bDNYrkTi4PIC1TO8RXMU352oUiOEphR1FT9qsz8XXaKYCTx7Eo/r3gkRdnEL8kVvb+KcaTk3MufV1aN1ABqaVywZJUNrYLTM0FpkrC3kSFnzcAjwsvDIEY3bJEHc37dfMEpFLSEz9cq4Y3rGo1ngZl5n+XHelVMLu3avekslhHjNj8SnLBy55W1WeF2dV2WFTlq3HhCXgML4mnlDJzwkKROvg8DlxWcyu3skr1QsdpkzfSwAfjUtRhYMVasSF38auSY3pI27XORp7fRMLryJDDmtQwfY9iTazdn2RPW42JxceuKqNeH2dNKLOSPla1W8WUnsWDNJYqdY1UXNhsyKR06iY/6hJRP1U23Zb1MlnDlIEbzEkdmVVbf+K1hrIFgkszudAn3jdeDMrc5OQXJyBMhmVUzkTDZguc4JePbivswLO9lNNJSPapkV5Qze2Jqpudk5c6+NoglGjYcNJbYrXAZpyQ/08Wxk5MzKhBdf3rRJ+g4mA7+rKRiwdMidh7cuUxsoTqVlFkIwv1lndLTg4ISPyLxMcQpAnbJ5yokR7rwU4rrNj/IkanQX3F/nQISuTJbADElLbibfBHOC+IYdn4z6rTOg5c1uLdcJo83Wj+tjDxy21WckfNQwWvS5QlhER5CYupdei3Vw8zEo3MPca85ydbx7nDshYDyoFYegLm1kbFRAI68FIqVbNfuiiVvaqsrLHvSzdupO3Xk9UJyHDvUL4bmJOhELuvDE4m7ajzpGhW6oBXPJiULclZcmaEQdl5flcvZpqQTppRFD7+OnMEkrWITOpurzlDodcPMYX0XpkrmUDRWUEcRFG7KMudR2MoUPtZLlqUy3kV6YArnG4wOu99Rt/yEM8OGibDSrT15v175onHOu1b096P5HDV1HLRw0tgqw0YODfgb0+kYPKY5KxPyDkrLr2Ti1NCW8NI7yIYDunbOAZepDJ0r/uD4QUzzKMYwZWdSdgJVqp5A3DylvJLFo3Y1x3pygvUhPTm6xp3Lpi9MRbhkT2VbVlLkMMiMSkbFdk5u47iZlPti0Ge7PAzsRFCSzrp9mz/ZCS5ln+MuyHSqRs58pkVLLm3mr9WDRSF8pLRqbpksFc9kXIMmo6DdrKzB3PhmW/IPy9/38KKzaX+6YedFPhEdusC0fLpyZ4tP5SaXCaIRoFPSHMuM1xIez90WM32nGeHCybagr+77dFtVcgWD4ksg6CJSmMG1+b6iXhCtvTpmfyTF6CSSs2IB7uawwR7zijERFqmNkXiSgSqEq9prelWoR+QhlmsXoN5Jk+nUDzSi3NQJPw0BLhlty91hkTads37fL+HekXVI6Mc2x2cSLoatoiWDEGGZIvielvUFNoZAPlptcIY3U3KPsNvg9GhkwnNWDIGPuazDk/5cVueqRiyTY8uJCI/cy2pWK9cvu0SLmM2ZweLH5tUPFHLxTHOAr5fOuE2sNMWVTzAeMwuiEou2ZFMJekeX7pL2MncSjVohJ/wuDzXed8801XK+v6az3PqXAB1F5JhLMK/c+Eoi+rkSTIbBuXwUepzP2BxdGPgGSTmylLrMr/hjhDQDDkSQh8OQBSpzddcO6k9lsvDbtR2Vp1w9Gd49Uc65mIhBRL3iIgsx6aM1I8nsZLjnJw8VkJCqt23KXYJVb5zUGQT74ss4V2UzP1M29chfFh9wJMMjKvLCovpW52KfNdYFC02KXwPYV3B0ZwPSylcVjNBCMJ2D8unWxmCHMbkIS4XIzLXFJQtgj4N3rQQ/O0mRWgVTwuvcIkKj8NFOMfcCBMQSLE/u2VySQv3B4ZSEwoVK1Da1XLU7S2pnbc2PJ3HsXox7oeKugIMZ3sVc2Elyh9leVXTVxJ1ATf11jQJG9ySFo2yWsuJltWO9eKjTxD4e1xierom07GrS522Zq8iVh5fESYah7p/sMDgRvF66mnfXwVvImQyVXo0MFzuyPhym7pQvWmQFYe6jCz7LCs0SEk+TJiGPl6dL7pey7avQvKtFiswkGiO+/dDfZEcKWKxqkOPNWaCxo1WmEJH47qvaqgdhL/fBdGFvG5/MiG5cWe+ey6IahiOyNy/XWFHdXl65idfHKogwojZmzfG4jTkZD9+5PMuOsCAZqeOrT3a5gWIDoI3pyVGuEGxY5EXRPVcfK9pzq6xZ0Q2xxWVcWA5hgk3HxHvNv6RHBzGoRKVls+l8Lfe5yl6QqCsmO4r1XBor/nV1NY+t1Qsf5sECWf4JgePRV680kLAkD5f2H3okq3KOiAIvDbk0Q6DyYkFVmrYYntccYqgxU6jmKtzCkXEsQXkR7axyaR8qAVSRfFBcb/b9ATLoTqsDO8n+he2uCbES2g1vX9ndfupCxWE8X3QlmI4kZQDdoxnY7k7HL44izsfLunsEul6l+jYjvPzCmODMK1chcbV70DHl9SZ0YnjGRN8heceVXvjRyzoBr+jNN0wEzh5MtqdZdzbOSOSHel5DedhzZ3q9htjjKVJbelE9quztZ6XAbClYe23SRHbH+w3Gniaj3AVyd5irUV/68YSYFKtlR9Xm7kUlpnEiPu/dkXtw9Amzz1l7dju9htTHhXcfyTEJBXes9bbGVbZVvTMjRq+gvx5voodO5zOPpsxpk04MHFrpcrrRZfyouahiqlfuNDhr9t2Z14PRlDiWQusLX0Q2l2ziM7896dYYPYEbIurW+lRuIIVDreNqpz3f0PXzNDcFXhPbJBX1FQ99wKfd7HKC7mAC3S41BNGO6WudPjw0xUddvbXEp0vfM3K1oIxC9flyrMiLEbc64Mx5ihVKrD4nQFO9ysZoPQ32viYEt7m3wqsuZLFRlF67KJWcsBjm2Pu1u1WElWJmyR+jhX4txUZWMFEorjaYMl5KuFsco07hGlhxZbgZIf8++E3wRO6Olj+lVH1tN//ZxeJU23Y1XMvgzha3YN07PWY4hrBf6lmyb7bWW2vHuJPHrf1VshFJmO44o6/6rbOefikiQZ9dCL2By/PjqKoywctna8WiROH19BKNpDxoaT8BFvjwyzpsxpfJp6ykD+IgE8bgGOpsbWeGbTXXP9+xmQ2ubPrk0bopB0aWzXt+Y1vi9YKpi/2qniQv6jmOYtf+MqZXs0GNBLEhn9drB6u1k8s1vtAV9Cv3kjyl/SShi7HTsmdk+hCAqeb5BE/qRK/rQXXDO2qT0k2ulpeWrAPjrgzUry1Gi4jEFiULx6ZccItcTbgaJ+ao1iQ2GKlO2dl6NF5HLy/FLW7lLb9v1Vbntt0MXB8IL5ezkxPqunCB0SnCO4BadfXIDvqz0E43yJmri3qt2d3i+7Fm7vE2lPdrMUv+83Vk76Vk4w5WaLLYK8kj7PSS5e/Z9ugWLhRxZ89Sz8jOV0ksjPZxm462tbW42xiYnfI749HtknHShSl309JTKRnGxr6wR70P1bjDUpNZbOPenrz9qDAW0SRqG7DjVbFWeZyC3BuZ6+4fdSztHdhZ6yyjT/aRaoQuPQfdhHvYjd6RALKvccgwYAoSlK1bs3y7mvoVM7RCNnpsWK3LzVZwwtTsY8GEWBIqzpF9/z9NUOtWZolEYId7asxcli1sczpxBEem/iZdQI3ROAmdKxr0Q97jk9q/Wko/3dhtprE54MCwfI1ySi3mxqQIZ6x0zarb0XgNnnyFaRbRHEA6R80hSJk4Zi6DI/q+O6/2yBIRQRyp2xxFjeDTsMPMRwIBZBNwYZjF+IRcyrMHctaIm1Pxglas51kFznlDFZ/qwhvCo2knXc/18emFTj7c7yCTkfp2O5902DXtm4vcGxR+EopiPETfNDpjbm/WPSFbUjHjuKkQiMfjYoQ97Mm8vLESRW/3LlN9dzmUNW0yHypugy8JgoX3k6dbz3wIp0FubEkVQ87H6kF4DToyCYitbQXlyWw+1WP9qo89fwmsUkAM0rFo2LdQGFImGLaRjO4NaIv5ZKKo3ocvYdu/rgatodoJiyYnXF4+dcm4EfNOuMskQRxEoaO1WAjUkqeCUpix7fG8O1HoeM5ApSVJpD50qKoq9TbljI7NuDsTylWOb+RAUMRLnNryZljzmUUMrVnh1cLmIxxNy/HlAcy/lM/Izq6AilxyzMk4Ex9W7Ejh8f3yWBb/mFyM08uFOKovoPm1EurNYgcrYuUh4V6MxlyWmjZDjTYDkyeGdQYYVrJIBBDetsNZwY1ryvQahSgQI3H8k2EfSqBlt4YkFLLJ7eQlGpwW3cic0vlFLedNjs2EnefTOKVH7JxKaF7UbKBG1LNezBvNCnThpga0B+4rwisk2tV2B72XFeT9wU8DC9qWcqol05WvOofvuabEtdbSZrIjRbykzIOn/BRWFzpeSrKinZ2m5vjlwEmunigynqJ+MY5eTJNQ7YbhS83hmHHwC9SUHArg5ByjNLnqe1+0vMxgx/DMUzNcS33fAUaE8adZTILUw7C5XI+wZvs0rV48j8r8MH5M87HZhxKOIp8mr/gGYSpIkCOueuk4+TlnEdkpKbmWK2+Wiy/WjTau9Nag6VyEqg3XDwwaUD0xK0kviGMqXuK2Idt0I4++FxTZGptrUtQh19X19XxsMQmNkqZbbDdKfFo6U66pN6vQtseZ0FHCNbkcuwepqFuiKNcOFyflaovxkqet9HoMm9hNfbjZdX825X0wV1G5a0SdCJtTIWWxFVKudd1TLDmnt002YuGqYQLF4y5wXTBEeOOqynGQLU6hbpz1VnC9GPavO2rOITedZmmCLIi5bhrZVkeYUFJq1JVKwZzLgxJkSK6P82DF/UY1hXgjFGSC/dPVovoL4j1wTD8lN/MB+LTZ4Su7jjn/Kkkh7uBa3BOauZM1OzdkZngGgia1IcXmE+XnpTmi01F8UdD1WEDUYGp9S9iXdrEe+pg5CoNFPGLqbIjiUkeeDSIShzpLXVnbst2qkigH45tzPeeuRp3djbhIwqNEx7rlavh0PB2pZTSpI7SE/LF5zc+nhd0cdJU1F8DbLA/c2a+giyLal1UbcjgXiuvKymJ0ObXka8HMLpmUl4P3/hIvDuL7y6TQdyq/cleW81bDIPYHzsxVo87yOk4bPCWRkVRd9JqLLeWvizMXtjnyqosNT7uIVnfCpnDzblXdwXg/tNnt6ZyOpfRgIYkfxyQzkPCRCHeFDX3jHl7r+g7ABLDmywVMV1CM7OeN9JjbbTypVXzN8AhCjtM0RgGE50gFejHWtFHjtVHrtXAMsI30kkfFF7Ou66F0lFZaNTNv4V0Eo+V6WYLgqO4qdw/D4aUc627djePcoK6X7QRCsZck2SZMCTD8kQQlF8WIAdNixzf2qw56y7/IK3NGVqwdJjSJ7DuGXcijbaw3bwYJf7puI6VCauiTWOciJo0LpENY2atZHI9ylbP/LK+dx5vIy1gvptM+MbZlsMqx7/5lueijESwiVqhi8XpSq0NHkL6vWH2/nJ7n+fjwkId9Qqyd0uisf7F6s9XZriWXcOVuIvKidvSmMDZdjaanNBvJGnWku8KFaUp9l6bLtMTMGcsy8urY7IJwof24SUdPsCVy1l6+B7L1cZp4yfd4XBOPNcVVCQndNai/uYQzhMnt+RJYCpko1a1tjGczM+Y230wSHkW8m4n10GUqWlgpA6wxd98j05vm9WRR07cBfd5foUkf05C9n3VioCd9sKYtMPxb7s6sFCIjJrTmzKZlL4mmxcDcU2Rez1qLKlafw2fc3c8n9ILhtYeWHNV6Cfp6vaQMgYxMHtN1mGtabOkjd6uMDnMKQJStTJDlqAvQwdL7c8A9X6yBm01MLKxnVppW7dfEUe9xcLZZVXmpr+Ro61moBQQrLfj5avYBlO5yMJyKXXdNfzh3Nrv7Kwexzj4aIYnVmcOxMGYptMDvhUycCEYOxZK2o5SC7mcVEZIUvfdPgLgFOsr61p0TtFgencuJ18020nXUg+gZ0pUswmuFraVQAxoJj+PjVqzasQuAzm5/8k+t4q5qQC8ewQxe9NAfjFhUAnU+HouFecwarMwkTGImGeQvtYMcFcVFSPbFLNLBcJvdWFVO89C/lvdCPFIMrAG9Y40DkNxGWX8G1YoJelDW4mOHaicVRlE1npkiiShYe+828qb2T6yjrrDBFMuVOkWT6qB13+3S6WI01CReqgelv8ZKm+DjubATCR6mwQbdsaXOjRwCUmtqptI/lUvt6bm2tfpKzrbDnEt+h/cw0CJRnMWd7z2ZskeHCdiaT7yIvXgbH6hq0pSsYCRbwjExWTVYkug4XyGpaMrRynQQLU5WvBe0KG4W8czLaus0yxb1CXkQNzfjjukzegQpKpqCKx7vNufVLnSHjnATdbjJpGmQ+OxcePjMIVm03zU0QsHM4N7VUV2yObUDomsnX7qu8L1H3VD0a5D8ARNw1UslThcokRNtjDp0mt+8ckKbl/yIJxK93reE0uLiEbWhzE30tCGtpOX5pGFWnfQvAYDZGD1ssYGe8c7A18x5BU8NIZUaZrZOvGAXNG/kHZFTl+LXpTllFcMPriWqLpfwehMNonF2uscd6XUwFAxDe+qeuIvAqjcmGp10rxsyVrB2tmQbEGDLp4QaxWnMnNuJQqXKUiKX5pSIaK/i3QvnyZXCvMaflvy6Wstk6D1hXcZxhOXMbV50AZGxE2FGlnNpWz3hAVFz9GYjcNMXN7GRVvQSJy/Idu1n/Ti3NP10ErMNAZWWNtfenTUN86tfSUs5V96aoGZUjcrEQS5rXR79FlfK1Lk3EuqZq05CqgkLV33rR2gDUDMJtIs3vi0mWySdFVa04iwex9318f58UxvR08/Me+T1SItFjrfmkcCw2mDXMwNjoVTnc2Q3jItKropOj2SNHMoYw06pR2vp0fKKJOPcn2QYpC+GOgPlY/cH3mIv130pcNY/T57KCeugEOkapJ3XYlqHgiYsLGRAx8fRhNBbBUkQwc1XQ7if8Ror88I0HagQcH9D8hSOpJn2kW7KzVVgrCaoldNL0SI8EE3FL4+rp57qiXFUCheeu7tpsC+e2ZPlwKEM54S2nKHXTYUbpeD7Ac4fGnu7nISjWmkorM7D6iJuSBpnW4Uinor9hkIe/XAdErra9ei4D4yViiFDBY8OXdULlzLhzjdmJO6SPtYJi5WiLQZqVqHdsDU1g0B3ingk6ZNOJ8/sKuaYLp769PvOJjc4u3a+RkHYu0anbnu88j7u85dbdL60qlAwSxyk3wPy/oxv3tQqeHp5WIMNzrmdd0DMFocT8+JCX3trTlo9Eq0m4xSs4GOdeEF7gpa8GTHOk5OIi572teSbt8stozC5XNPmDr+BuIpf51XS2Xh+5uY5gaKoOL7aB36Z+chhrmt9G6krc6fkPWtPJyMMtRTuDKO5ylx7jJEZGJNgW9xQKDP1ePzkbFYJX/BzfySGcrNRMBXhventEnTFXxgPCC6z6WDuGAyKvkG8PFDD9cTtqBcq/F7V4e0OwPaUZhgGKOk42WK3DP7VbKyJCznuydc5tOEEMpP3mDSPQ7PsyOyeG4xfHUltkWzP4QVVq9X3US3HtnMTJB7dvdz8uPvV6iVjOUHT1XcLc1cl9xEALu1q0FA/0b1SiiDpWDytQw2QJFc0QErLne6mMcNsa4vN5u66M/m4hvgOCgVz1wAzdalSt0dBnfSibRKsD8iik/gh2rrLUVsFn+XUO2GV10iZjjahpklTPbqZC8+Z6BEjMd50/VyzOipqsksFEHDyxTAnZDs/M42NqAsNophFvdXD0KziwIbO8VTaq1hOa1CEtkIDjJlbn+3T6dqU9QT3CPciNzRXPU+NT0o07EvXtW035seT/3y1krf4tnQsdUBjpWGpi8rpSHqj93spPYegfdom3mdZyz61ZJ941CbnqNVG/CXdvZgZ0YZVzdejTEowNxP9fVvK2MHJObbk5NiXOiz012DIDKO0s0W/GEjKVetrTi/l3ayiIqaHG8bWXnq8lim/4dy9sjF4U14MRtw0thHQ19RvTjpUu1oaCRiHpvFEQ1RnnNWBrtPnlOaIOgTLchcs/GXjlQiZVxJwlXCayEDjCjB2PtLblVerhjIKtgKgJQAqQJV9GBjc7XqD8vuUX3KLJi4KxsRIcswWTmrUQTnLkSOar6hj3e1837mMeC502b3I3TYijalCg7TxTulz+xkMSdp7c+wtgdxvVwPq8yabOb56wPsMsyx6SUtkv5zrtVVNjtpVp4tcT5H5C3W+NJaVBUKRxGC01J+jh4rqVDg8XUgMrz9NNubEy7rIG4T01vXm8y+TSGMBXuPTC3IRJdTjTesafFSSewWX5L5MJ3+Bjntz9FxBj1yzSUr7eXyclXHk/O6huxcp9KAoZW7hXYqQOYz4MN3i67zGrmXfU907x3RI9RZy6yeVWbtSyoh1Je6mDXUXHopoFw5Z2DgK2RDcg469wLR8ZLHVsNQOmwc/Jrf2CZofEcod3szmtCvNCyG8Rb3fIEksYEwVOZWuFjMuwXTmwiN97hHZpEwIgMviVPNZNc5hoJZm6Gt2Bz/cUZoClG9w6jUxagM/7i1USEmc5gu5Skfedtv5gl6WSQoJvTHoKasDu69gRbkq2XTxZWXOrkYP1802Xyk1j+WgUMFwsj2CS6KAMY/D43o5Yr1FdnbEE4M4gUHbniENjTHBIdr6tbDHlo6evawtlwxSymp50CSZQQ+GPG2vxBvv2JPBrzN7aoDb1ulUPDsNz57DM0KcLKFt8oTGDoFfLbYVcnuzr22uDJBCpudNjO3Fvr7yQrLN6QymomP6cEW+YdMC9WwhX0LihPhWdhzoNr+z2jmkzAL1G5HAAu/yWMr9DGZUKMguWJIPja2pKlbJ8G4VlOZsmXdrYOtZeNADVQKyrI+EV7Kops4laTSv7jGWVVNKdSg6XAT49c2YHp1299XLVWDrklTLczT3NH0rpLg5iubTxedu2NubLUIchWpgUuPud+6Y3B93XmPhB6kaIQ3DvbhPYoD5hchiOBi0Ero9NTgkKpOCmEO5og7wx5DfwhRDwRSxjQ4x3Zrrdg/4GZQEVN4iArrdg/RyUyWDpS90vtz6WxMF2tzKsXi/dUst1JGJJFJ9kWNsfD6eWP4MmuKyn2ONujD5YDmr3jUIlsPV8bK75HDhGv5i3akyrhUBi+GRPLnHK0nNaN9S1F21n/Br0YxQRVa03ikHyjY9kStSJp9g1BBW4qXxvhcoe47r0ybrCHMPp6h3VIct8ixQu9rvLf1Cz+ktWNCToz245nyuBvxOcsLNdU3QXZToGtByjgiMZCaUB4h8BW131UsC5tn7Tadg4gTdt7p/GE20LtvWhAFT5Tz/2oxRG90Od47WETdOhlc6/IX2cka6JlCqyd127xjBeKTC60Qs8/D01dTLVD8yyT68kFadBzftzFToQFsv1S5oOmUetFdixT2L2jRBG8Q3RDAhelj8emZDuMoTPLo1XbeLxfSVMypU4+oOqvF37MVW5S05tYn6eOa2zvW5hzgoIhl1PU91NqLzXeeSlV9Mjz2mwo5dcbTVbfTywMXrjC8ItExNCkMdfveLh/nQLKU6sxa5xbnPQzPdOYKemasitKvTHpOTG4j16Rp6XDL7PGUFR4ob/btUBxLhQUpGosxa6CNfKRy6+ZQfac4xSG6bNaKJi8svjEg6IgF0/hR6aYpk2dOCcQ2fXfluRuVx2ccEb+07jGVQn1ZyNhuNDcfjcmEp8nrJ5j5r4QSKHXkNqyd6NmYYfsrQCY12lOBG7USdAhOuxc2UsJ6tn0mBZbRzpoZkQ6fWlGrkMjyyhQXsjEHDallfaBOXLtr5LoKCqfZxmbn+ZtSRa9fPxpcRiN1IEqvwJFu8NkKCGxR6Vy7vxNX1dquP+YYLXG01KZgxn2fdsIOIYZgvP3x5347+vF77r3/o9r72+H/t9uXXi5Ld8v61bJy+75m+f/Tw88dZP/8bHf7rhy9DXAINvt4kHes5/3YB84/ukf74TdSPv7tH+vXnO7/GYKBMt+nb9eIpzMd/uIL7/U7tP9zABV/y4kPKPE5h2YbRx53hjzu879+XvDX8+LXix81X9Ccc6Pn3/wn+PyPVcjwAAA== -->
