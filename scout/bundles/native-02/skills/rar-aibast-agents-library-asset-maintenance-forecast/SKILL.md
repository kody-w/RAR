---
name: "rar-aibast-agents-library-asset-maintenance-forecast"
description: "Monitors asset health from live CRM work orders joined to simulated telemetry sensor stats and alerts, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/asset_maintenance_forecast", "rar_sha256": "3b19a5b8d75932797bd11152c321ce6d83789f0092ed326df11e145a415120ac", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.3.0", "author": "AIBAST", "tags": ["maintenance", "asset-health", "energy", "predictive", "work-orders", "budget"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/asset_maintenance_forecast`. The original RAPP
agent is preserved byte-for-byte in `asset_maintenance_forecast_agent.py` and in the RCI capsule.

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

Asset Maintenance Forecast Agent — a template you are meant to mutate.

Provides predictive maintenance forecasting, asset health monitoring,
budget projections, and work order planning for energy infrastructure
including turbines, transformers, and pipelines.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted systems (synthetic data, no credentials, works
     from anywhere):
       CRM  https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
            — customer assets and work orders (maintenance history)
       TEL  https://kody-w.github.io/static-telemetry/api/v1/
            — sensors, alerts, and 672-point reading series
     Telemetry sensors carry REAL msdyn_customerassetid values, so
     sensor health joins straight onto CRM assets and their work
     orders; the three active alerts carry real CRM case numbers.
     Try: perform(operation="iot_failure_analysis")
     (joins the live vibration_spike alert to CRM case CAS-260132 —
     Granite Peak Manufacturing's spindle downtime case)
  2. No network? Everything falls back to the embedded demo layer below
     (ASSETS / BUDGET_RATES / IOT_SIGNALS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     ASSET_MAINTENANCE_FORECAST_DATA_URL (CRM) and/or
     ASSET_MAINTENANCE_FORECAST_TEL_URL (telemetry) to your own
     endpoints (your real Dynamics org, your IoT historian), or replace
     _fetch_collection() / _fetch_telemetry() with your own API client.
     Fields the rest of the file needs are listed in
     _normalize_live_asset() — everything else keeps working untouched.
     Fields marked "enrichment seam" in the output (condition scores,
     operating hours, failure rates) are where you wire your
     reliability model.

OPERATIONS
  maintenance_forecast | asset_health | budget_projection
  | work_order_plan | iot_failure_analysis | schedule_maintenance
  kwargs: operation (required), asset_id (schedule_maintenance)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "asset_id": {
      "description": "Asset ID; required by schedule_maintenance.",
      "type": "string"
    },
    "operation": {
      "description": "The maintenance operation to perform.",
      "enum": [
        "maintenance_forecast",
        "asset_health",
        "budget_projection",
        "work_order_plan",
        "iot_failure_analysis",
        "schedule_maintenance"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `asset_maintenance_forecast_agent.py` and embedded as the fenced Python below (sha256 3b19a5b8d7593279…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `asset_maintenance_forecast_agent.py` first:

```bash
python3 asset_maintenance_forecast_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 asset_maintenance_forecast_agent.py   # or on stdin
python3 asset_maintenance_forecast_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Asset Maintenance Forecast Agent — a template you are meant to mutate.

Provides predictive maintenance forecasting, asset health monitoring,
budget projections, and work order planning for energy infrastructure
including turbines, transformers, and pipelines.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted systems (synthetic data, no credentials, works
     from anywhere):
       CRM  https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
            — customer assets and work orders (maintenance history)
       TEL  https://kody-w.github.io/static-telemetry/api/v1/
            — sensors, alerts, and 672-point reading series
     Telemetry sensors carry REAL msdyn_customerassetid values, so
     sensor health joins straight onto CRM assets and their work
     orders; the three active alerts carry real CRM case numbers.
     Try: perform(operation="iot_failure_analysis")
     (joins the live vibration_spike alert to CRM case CAS-260132 —
     Granite Peak Manufacturing's spindle downtime case)
  2. No network? Everything falls back to the embedded demo layer below
     (ASSETS / BUDGET_RATES / IOT_SIGNALS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     ASSET_MAINTENANCE_FORECAST_DATA_URL (CRM) and/or
     ASSET_MAINTENANCE_FORECAST_TEL_URL (telemetry) to your own
     endpoints (your real Dynamics org, your IoT historian), or replace
     _fetch_collection() / _fetch_telemetry() with your own API client.
     Fields the rest of the file needs are listed in
     _normalize_live_asset() — everything else keeps working untouched.
     Fields marked "enrichment seam" in the output (condition scores,
     operating hours, failure rates) are where you wire your
     reliability model.

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
    "version": "1.3.0",
    "display_name": "Asset Maintenance Forecast Agent",
    "description": "Monitors asset health from live CRM work orders joined to simulated telemetry sensor stats and alerts, with an offline demo fallback.",
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


# Sibling live source: the static-telemetry API (sensors, alerts, and
# per-sensor reading series). Sensors carry REAL msdyn_customerassetid
# values and alerts carry real CRM case numbers, so both join onto the
# CRM tenant above. Override with ASSET_MAINTENANCE_FORECAST_TEL_URL.
TELEMETRY_SOURCE_URL = os.environ.get(
    "ASSET_MAINTENANCE_FORECAST_TEL_URL",
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


def _reading_stats(sensor_id):
    """min/max/latest over one live reading series; None offline."""
    points = _fetch_telemetry(f"readings/{sensor_id}", key="points")
    values = [p.get("v") for p in points if isinstance(p.get("v"), (int, float))]
    if not values:
        return None
    return {
        "n": len(values),
        "min": min(values),
        "max": max(values),
        "latest": values[-1],
    }


def _sensor_health_rows(limit=2):
    """Join live telemetry sensors onto CRM customer assets (via the
    REAL msdyn_customerassetid each sensor carries) and each asset's
    work orders. Fetches at most `limit` reading series per run."""
    sensors = _fetch_telemetry("sensors")
    if not sensors:
        return []
    assets = {
        a.get("msdyn_customerassetid"): a
        for a in _fetch_collection("msdyn_customerassets")
    }
    workorders = _fetch_collection("msdyn_workorders")
    rows = []
    for s in sensors:
        crm_asset = assets.get(s.get("asset_id"))
        if not crm_asset:
            continue
        stats = _reading_stats(s.get("sensor_id"))
        if not stats:
            continue
        account = crm_asset.get("msdyn_accountname", "")
        related = [
            w for w in workorders
            if w.get("msdyn_serviceaccountname") == account
        ]
        rows.append({
            "sensor": s.get("sensor_code", "?"),
            "type": s.get("sensor_type", "?"),
            "unit": s.get("unit", ""),
            "asset": crm_asset.get("msdyn_name", "?"),
            "stats": stats,
            "open_wos": sum(1 for w in related if w.get("statecode") == 0),
            "total_wos": len(related),
        })
        if len(rows) >= limit:
            break
    return rows


def _active_alert_cases():
    """The live telemetry alerts joined to their real CRM cases by
    ticket number (e.g. vibration_spike -> CAS-260132); [] offline."""
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
            "severity": a.get("severity", "?"),
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
            sensor_rows = _sensor_health_rows()
            if sensor_rows:
                lines.extend([
                    "",
                    "## Live Sensor Health (telemetry joined to CRM assets)",
                    "",
                    "| Sensor | Signal | CRM Asset | Latest | Min | Max | Open WOs | Total WOs |",
                    "|--------|--------|-----------|--------|-----|-----|----------|-----------|",
                ])
                for s in sensor_rows:
                    st, u = s["stats"], s["unit"]
                    lines.append(
                        f"| {s['sensor']} | {s['type']} | {s['asset']} "
                        f"| {st['latest']} {u} | {st['min']} {u} | {st['max']} {u} "
                        f"| {s['open_wos']} | {s['total_wos']} |"
                    )
                lines.append("")
                lines.append(
                    "_Source: live static-telemetry sensors + reading series "
                    f"({sensor_rows[0]['stats']['n']} points @ 15 min each), joined to CRM "
                    "customer assets via the REAL msdyn_customerassetid each sensor "
                    "carries. Work order counts come from the CRM side of the join._"
                )
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
        live = _active_alert_cases()
        if live:
            lines = [
                "# Real-Time IoT Failure Analysis (live telemetry + CRM)",
                "",
                f"**Active alerts:** {len(live)}",
                "",
                "| Alert | Type | Asset | Account | Reading | Threshold | Severity | CRM Case | Case Status |",
                "|-------|------|-------|---------|---------|-----------|----------|----------|-------------|",
            ]
            for a in live:
                lines.append(
                    f"| {a['alert']} | {a['type']} | {a['asset']} | {a['account']} "
                    f"| {a['reading']} | {a['threshold']} | {a['severity'].upper()} "
                    f"| {a['case']} | {a['case_status']} |"
                )
            lines.append("")
            lines.append("**Linked CRM cases:**")
            for a in live:
                lines.append(f"- {a['case']}: {a['case_title']} ({a['case_status']})")
            lines.append("")
            lines.append(
                "_Source: live static-telemetry alerts joined to Static Dynamics "
                "365 cases by ticket number (vibration_spike -> CAS-260132, "
                "temperature_excursion -> CAS-260138, load_fault -> CAS-260128)._"
            )
            return "\n".join(lines)

        rows = _iot_failure_analysis()
        lines = [
            "# Real-Time IoT Failure Analysis (embedded demo data — offline)",
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
    print("LIVE TENANT ASSETS + SENSOR HEALTH (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="asset_health"))
    print()
    print("=" * 60)
    print("LIVE TELEMETRY ALERTS JOINED TO CRM CASES (falls back offline)")
    print(agent.perform(operation="iot_failure_analysis"))
    print()
    print("=" * 60)
    print("EMBEDDED DEMO FLEET (works offline)")
    print(agent.perform(operation="maintenance_forecast"))
    for op in ["budget_projection", "work_order_plan"]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
