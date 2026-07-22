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
