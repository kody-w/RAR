"""
Asset Maintenance Forecast Agent — a template you are meant to mutate.

Provides predictive maintenance forecasting, asset health monitoring,
budget projections, and work order planning for energy infrastructure
including turbines, transformers, and pipelines.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live asset and work order records over real
     HTTP from the globally hosted Static Dynamics 365 tenant (Aster
     Lane Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template a Field Service customer asset stands in for a
     piece of energy infrastructure: its registration date drives real
     age math and its work orders are its maintenance history.
     Try: perform(operation="asset_health")
     (surfaces live assets like "Cedar Hollow Printing Sensor Kit K4 13"
     with their open work orders)
  2. No network? Everything falls back to the embedded demo layer below
     (ASSETS / BUDGET_RATES / IOT_SIGNALS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     ASSET_MAINTENANCE_FORECAST_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your EAM/CMMS), or
     replace _fetch_collection() with your own API client. Fields the
     rest of the file needs are listed in _normalize_live_asset() —
     everything else keeps working untouched. Fields marked "enrichment
     seam" in the output (condition scores, operating hours, failure
     rates) are where you wire your IoT historian and EAM.

OPERATIONS
  maintenance_forecast | asset_health | budget_projection
  | work_order_plan | iot_failure_analysis | schedule_maintenance
  kwargs: operation (required), asset_id (schedule_maintenance)
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
    "name": "@aibast-agents-library/asset_maintenance_forecast",
    "version": "1.2.0",
    "display_name": "Asset Maintenance Forecast Agent",
    "description": "Monitors asset health and maintenance from live work orders on a simulated Dynamics 365 tenant, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["maintenance", "asset-health", "energy", "predictive", "work-orders", "budget"],
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
#   export ASSET_MAINTENANCE_FORECAST_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your EAM/CMMS client. Downstream
# code only needs the fields produced by _normalize_live_asset().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "ASSET_MAINTENANCE_FORECAST_DATA_URL",
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


def _asset_age_years(iso_date):
    try:
        then = datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
        if then.tzinfo is None:
            then = then.replace(tzinfo=timezone.utc)
        return round((datetime.now(timezone.utc) - then).days / 365.25, 1)
    except (ValueError, TypeError):
        return None


def _normalize_live_asset(row, workorders):
    """Project a Dynamics customer asset onto the asset shape this agent
    uses. THIS is the contract your replacement data source must meet —
    a dict with these keys. None means 'not available from Field Service
    records alone' and the renderers label it as an enrichment seam. In
    this template a Field Service customer asset is reinterpreted as a
    monitored piece of infrastructure; its work orders are its
    maintenance history."""
    name = row.get("msdyn_name", "Unknown")
    account = row.get("msdyn_accountname", "")
    related = [
        w for w in workorders
        if w.get("msdyn_serviceaccountname") == account
    ]
    open_wos = [w for w in related if w.get("statecode") == 0]
    return {
        "name": name,
        "type": row.get("msdyn_productname", "asset"),
        "location": account,
        "serial": row.get("msdyn_serialnumber", ""),
        "age_years": _asset_age_years(row.get("msdyn_registrationdate")),
        "condition_score": None,       # enrichment seam — wire your IoT historian
        "operating_hours": None,       # enrichment seam
        "failure_rate_annual_pct": None,  # enrichment seam — wire your reliability model
        "open_work_orders": len(open_wos),   # real count
        "total_work_orders": len(related),   # real count
        "_live": True,
    }


def _live_assets():
    """List of live tenant assets with their work order counts; []
    when offline."""
    rows = _fetch_collection("msdyn_customerassets")
    if not rows:
        return []
    workorders = _fetch_collection("msdyn_workorders")
    return [_normalize_live_asset(row, workorders) for row in rows]


def _na(value):
    """None = Field Service records alone can't know this (enrichment
    seam); 0 is real."""
    return "n/a — enrichment seam" if value is None else f"{value}"


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

ASSETS = {
    "AST-T001": {
        "name": "Wind Turbine Alpha-7",
        "type": "wind_turbine",
        "location": "Sweetwater Wind Farm, TX",
        "installed_year": 2016,
        "age_years": 10,
        "capacity_mw": 3.2,
        "condition_score": 68,
        "last_major_service": "2025-06-15",
        "operating_hours": 72480,
        "failure_rate_annual_pct": 4.2,
        "maintenance_history": [
            {"date": "2025-06-15", "type": "major", "cost": 48000, "description": "Gearbox bearing replacement"},
            {"date": "2025-11-20", "type": "minor", "cost": 8200, "description": "Blade pitch calibration"},
            {"date": "2026-01-10", "type": "inspection", "cost": 3500, "description": "Annual structural inspection"},
        ],
        "predicted_next_failure": "2026-08-15",
        "replacement_cost": 2400000,
    },
    "AST-X002": {
        "name": "Substation Transformer B-12",
        "type": "transformer",
        "location": "Ridgeline Substation, CO",
        "installed_year": 2008,
        "age_years": 18,
        "capacity_mw": 120.0,
        "condition_score": 42,
        "last_major_service": "2024-09-22",
        "operating_hours": 148920,
        "failure_rate_annual_pct": 8.7,
        "maintenance_history": [
            {"date": "2024-09-22", "type": "major", "cost": 125000, "description": "Oil filtration and bushing replacement"},
            {"date": "2025-04-11", "type": "minor", "cost": 18500, "description": "Cooling fan motor replacement"},
            {"date": "2025-12-05", "type": "inspection", "cost": 6200, "description": "DGA oil analysis - elevated acetylene"},
        ],
        "predicted_next_failure": "2026-05-01",
        "replacement_cost": 4800000,
    },
    "AST-P003": {
        "name": "Gas Pipeline Segment NE-14",
        "type": "pipeline",
        "location": "Northeast Corridor, PA",
        "installed_year": 2012,
        "age_years": 14,
        "capacity_mw": 0,
        "condition_score": 75,
        "last_major_service": "2025-08-30",
        "operating_hours": 0,
        "failure_rate_annual_pct": 1.8,
        "maintenance_history": [
            {"date": "2025-08-30", "type": "major", "cost": 210000, "description": "Corrosion remediation and recoating"},
            {"date": "2025-11-15", "type": "inspection", "cost": 15000, "description": "Inline inspection pig run"},
            {"date": "2026-02-20", "type": "minor", "cost": 9800, "description": "Valve actuator servicing"},
        ],
        "predicted_next_failure": "2027-03-01",
        "replacement_cost": 12000000,
    },
    "AST-T004": {
        "name": "Gas Turbine GT-3A",
        "type": "gas_turbine",
        "location": "Riverside Generating Station, CA",
        "installed_year": 2019,
        "age_years": 7,
        "capacity_mw": 85.0,
        "condition_score": 88,
        "last_major_service": "2025-10-12",
        "operating_hours": 38200,
        "failure_rate_annual_pct": 1.2,
        "maintenance_history": [
            {"date": "2025-10-12", "type": "major", "cost": 340000, "description": "Hot gas path inspection"},
            {"date": "2026-01-28", "type": "minor", "cost": 22000, "description": "Fuel nozzle cleaning"},
        ],
        "predicted_next_failure": "2027-10-01",
        "replacement_cost": 18000000,
    },
}

BUDGET_RATES = {
    "major": {"wind_turbine": 52000, "transformer": 135000, "pipeline": 225000, "gas_turbine": 360000},
    "minor": {"wind_turbine": 9000, "transformer": 20000, "pipeline": 12000, "gas_turbine": 25000},
    "inspection": {"wind_turbine": 4000, "transformer": 7000, "pipeline": 16000, "gas_turbine": 15000},
}

IOT_SIGNALS = {
    "AST-T001": {
        "signal": "gearbox vibration",
        "reading": 8.4,
        "unit": "mm/s",
        "threshold": 7.1,
        "risk": "high",
        "targeted_action": "Inspect gearbox bearings and confirm lubrication quality.",
    },
    "AST-X002": {
        "signal": "dissolved acetylene",
        "reading": 42,
        "unit": "ppm",
        "threshold": 35,
        "risk": "critical",
        "targeted_action": "Perform an expedited DGA review and internal transformer inspection.",
    },
    "AST-T004": {
        "signal": "exhaust temperature spread",
        "reading": 18,
        "unit": "C",
        "threshold": 22,
        "risk": "watch",
        "targeted_action": "Trend combustor performance at the next operating interval.",
    },
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _maintenance_forecast():
    forecasts = []
    for aid, a in ASSETS.items():
        forecasts.append({
            "id": aid, "name": a["name"], "type": a["type"],
            "condition_score": a["condition_score"],
            "failure_rate_pct": a["failure_rate_annual_pct"],
            "predicted_failure": a["predicted_next_failure"],
            "last_service": a["last_major_service"],
            "location": a["location"],
        })
    forecasts.sort(key=lambda x: x["predicted_failure"])
    return {"forecasts": forecasts}


def _asset_health():
    health = []
    for aid, a in ASSETS.items():
        status = "critical" if a["condition_score"] < 50 else ("warning" if a["condition_score"] < 70 else "good")
        health.append({
            "id": aid, "name": a["name"], "type": a["type"],
            "condition_score": a["condition_score"], "status": status,
            "age_years": a["age_years"], "operating_hours": a["operating_hours"],
            "replacement_cost": a["replacement_cost"],
        })
    health.sort(key=lambda x: x["condition_score"])
    return {"assets": health, "avg_condition": round(sum(a["condition_score"] for a in ASSETS.values()) / len(ASSETS), 1)}


def _budget_projection():
    total = 0
    projections = []
    for aid, a in ASSETS.items():
        atype = a["type"]
        annual = BUDGET_RATES["major"][atype] + BUDGET_RATES["minor"][atype] * 2 + BUDGET_RATES["inspection"][atype]
        if a["condition_score"] < 50:
            annual = round(annual * 1.5)
        total += annual
        projections.append({
            "id": aid, "name": a["name"], "type": atype,
            "annual_budget": annual, "replacement_cost": a["replacement_cost"],
            "condition_score": a["condition_score"],
        })
    projections.sort(key=lambda x: x["annual_budget"], reverse=True)
    return {"projections": projections, "total_annual": total}


def _work_order_plan():
    orders = []
    priority = 1
    for aid, a in sorted(ASSETS.items(), key=lambda x: x[1]["condition_score"]):
        atype = a["type"]
        if a["condition_score"] < 50:
            orders.append({
                "priority": priority, "asset_id": aid, "asset_name": a["name"],
                "work_type": "major", "description": f"Urgent major service - condition score {a['condition_score']}",
                "estimated_cost": BUDGET_RATES["major"][atype],
                "target_date": "2026-Q2",
            })
            priority += 1
        if a["condition_score"] < 70:
            orders.append({
                "priority": priority, "asset_id": aid, "asset_name": a["name"],
                "work_type": "inspection", "description": f"Detailed condition assessment required",
                "estimated_cost": BUDGET_RATES["inspection"][atype],
                "target_date": "2026-Q2",
            })
            priority += 1
        orders.append({
            "priority": priority, "asset_id": aid, "asset_name": a["name"],
            "work_type": "minor", "description": "Scheduled preventive maintenance",
            "estimated_cost": BUDGET_RATES["minor"][atype],
            "target_date": "2026-Q3",
        })
        priority += 1
    return {"work_orders": orders, "total_cost": sum(o["estimated_cost"] for o in orders)}


def _iot_failure_analysis():
    results = []
    for asset_id, signal in IOT_SIGNALS.items():
        asset = ASSETS[asset_id]
        results.append({
            "asset_id": asset_id,
            "asset": asset["name"],
            "signal": signal["signal"],
            "reading": f"{signal['reading']} {signal['unit']}",
            "threshold": f"{signal['threshold']} {signal['unit']}",
            "risk": signal["risk"],
            "predicted_failure": asset["predicted_next_failure"],
            "targeted_action": signal["targeted_action"],
        })
    return results


def _schedule_maintenance(asset_id):
    asset = ASSETS.get(asset_id)
    if not asset:
        return None
    work_type = "major" if asset["condition_score"] < 50 else "inspection"
    return {
        "asset_id": asset_id,
        "asset": asset["name"],
        "work_type": work_type,
        "scheduled_window": "2026-04-06T08:00:00Z",
        "estimated_cost": BUDGET_RATES[work_type][asset["type"]],
        "system": "Dynamics 365 ERP",
        "status": "simulated",
    }


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

class AssetMaintenanceForecastAgent(BasicAgent):
    """Predictive maintenance and asset health agent for energy infrastructure."""

    def __init__(self):
        self.name = "AssetMaintenanceForecastAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "maintenance_forecast",
                            "asset_health",
                            "budget_projection",
                            "work_order_plan",
                            "iot_failure_analysis",
                            "schedule_maintenance",
                        ],
                        "description": "The maintenance operation to perform.",
                    },
                    "asset_id": {
                        "type": "string",
                        "description": "Asset ID; required by schedule_maintenance.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "maintenance_forecast")
        if op == "maintenance_forecast":
            return self._maintenance_forecast()
        elif op == "asset_health":
            return self._asset_health()
        elif op == "budget_projection":
            return self._budget_projection()
        elif op == "work_order_plan":
            return self._work_order_plan()
        elif op == "iot_failure_analysis":
            return self._iot_failure_analysis()
        elif op == "schedule_maintenance":
            return self._schedule_maintenance(kwargs.get("asset_id"))
        return f"**Error:** Unknown operation `{op}`."

    def _maintenance_forecast(self) -> str:
        data = _maintenance_forecast()
        lines = [
            "# Maintenance Forecast",
            "",
            "| Asset | Type | Condition | Failure Rate | Predicted Failure | Last Service |",
            "|-------|------|-----------|-------------|-------------------|--------------|",
        ]
        for f in data["forecasts"]:
            lines.append(
                f"| {f['name']} | {f['type']} | {f['condition_score']} "
                f"| {f['failure_rate_pct']}% | {f['predicted_failure']} | {f['last_service']} |"
            )
        lines.append("")
        lines.append("## Action Items")
        lines.append("- Substation Transformer B-12 requires immediate attention (predicted failure Q2 2026).")
        lines.append("- Wind Turbine Alpha-7 approaching maintenance window (predicted failure Q3 2026).")
        return "\n".join(lines)

    def _asset_health(self) -> str:
        live = _live_assets()
        if live:
            live.sort(key=lambda a: (-a["open_work_orders"], -(a["age_years"] or 0)))
            lines = [
                "# Asset Health Dashboard (live tenant data)",
                "",
                f"**Assets monitored:** {len(live)} (live Field Service customer assets)",
                "**Average Condition Score:** n/a — enrichment seam (wire your IoT historian)",
                "",
                "| Asset | Product | Account | Age | Open WOs | Total WOs | Condition |",
                "|-------|---------|---------|-----|----------|-----------|-----------|",
            ]
            for a in live:
                age = f"{a['age_years']}yr" if a["age_years"] is not None else "n/a"
                lines.append(
                    f"| {a['name']} | {a['type']} | {a['location']} | {age} "
                    f"| {a['open_work_orders']} | {a['total_work_orders']} "
                    f"| {_na(a['condition_score'])} |"
                )
            lines.append("")
            lines.append("_Source: live Static Dynamics 365 tenant (msdyn_customerassets + "
                         "msdyn_workorders). A customer asset stands in for a piece of "
                         "infrastructure; work order counts are real, condition scoring is "
                         "an enrichment seam._")
            return "\n".join(lines)

        data = _asset_health()
        lines = [
            "# Asset Health Dashboard (embedded demo data — offline)",
            "",
            f"**Average Condition Score:** {data['avg_condition']}",
            "",
            "| Asset | Type | Condition | Status | Age | Operating Hours | Replacement Cost |",
            "|-------|------|-----------|--------|-----|----------------|-----------------|",
        ]
        for a in data["assets"]:
            hrs = f"{a['operating_hours']:,}" if a["operating_hours"] else "N/A"
            lines.append(
                f"| {a['name']} | {a['type']} | {a['condition_score']} "
                f"| {a['status'].upper()} | {a['age_years']}yr | {hrs} | ${a['replacement_cost']:,} |"
            )
        return "\n".join(lines)

    def _budget_projection(self) -> str:
        data = _budget_projection()
        lines = [
            "# Maintenance Budget Projection",
            "",
            f"**Total Annual Budget:** ${data['total_annual']:,}",
            "",
            "| Asset | Type | Condition | Annual Budget | Replacement Cost |",
            "|-------|------|-----------|--------------|-----------------|",
        ]
        for p in data["projections"]:
            lines.append(
                f"| {p['name']} | {p['type']} | {p['condition_score']} "
                f"| ${p['annual_budget']:,} | ${p['replacement_cost']:,} |"
            )
        return "\n".join(lines)

    def _work_order_plan(self) -> str:
        data = _work_order_plan()
        lines = [
            "# Work Order Plan",
            "",
            f"**Total Planned Cost:** ${data['total_cost']:,}",
            "",
            "| Priority | Asset | Work Type | Description | Est. Cost | Target |",
            "|----------|-------|-----------|-------------|----------|--------|",
        ]
        for wo in data["work_orders"]:
            lines.append(
                f"| {wo['priority']} | {wo['asset_name']} | {wo['work_type'].upper()} "
                f"| {wo['description']} | ${wo['estimated_cost']:,} | {wo['target_date']} |"
            )
        return "\n".join(lines)

    def _iot_failure_analysis(self) -> str:
        rows = _iot_failure_analysis()
        lines = [
            "# Real-Time IoT Failure Analysis",
            "",
            "| Asset ID | Asset | Signal | Reading | Threshold | Risk | Predicted Failure | Targeted Action |",
            "|----------|-------|--------|---------|-----------|------|-------------------|-----------------|",
        ]
        for row in rows:
            lines.append(
                f"| {row['asset_id']} | {row['asset']} | {row['signal']} | {row['reading']} "
                f"| {row['threshold']} | {row['risk'].upper()} | "
                f"{row['predicted_failure']} | {row['targeted_action']} |"
            )
        lines.extend([
            "",
            "**Evidence:** Energy Operations demo 00:52-01:15 — real-time IoT "
            "monitoring, AI-driven failure prediction, and targeted actions.",
        ])
        return "\n".join(lines)

    def _schedule_maintenance(self, asset_id) -> str:
        if not asset_id:
            return (
                "# Schedule Maintenance\n\nProvide an exact `asset_id`. "
                f"Available IDs: {', '.join(sorted(ASSETS))}."
            )
        receipt = _schedule_maintenance(asset_id)
        if not receipt:
            return f"**Error:** Unknown asset_id `{asset_id}`."
        return "\n".join([
            "# Maintenance Scheduling",
            "",
            f"- **Asset:** {receipt['asset']} (`{receipt['asset_id']}`)",
            f"- **Work Type:** {receipt['work_type']}",
            f"- **Scheduled Window:** {receipt['scheduled_window']}",
            f"- **Estimated Cost:** ${receipt['estimated_cost']:,}",
            "",
            "## Simulated Write Receipt",
            "",
            f"- **Action:** Schedule maintenance in {receipt['system']}.",
            "- **Mode:** dry-run; no live ERP record was created or mutated.",
            "- **Evidence:** Energy Operations demo 01:15-01:20.",
        ])


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    agent = AssetMaintenanceForecastAgent()
    print("=" * 60)
    print("LIVE TENANT ASSETS (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="asset_health"))
    print()
    print("=" * 60)
    print("EMBEDDED DEMO FLEET (works offline)")
    print(agent.perform(operation="maintenance_forecast"))
    for op in ["budget_projection", "work_order_plan"]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
