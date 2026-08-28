---
name: "rar-aibast-agents-library-production-line-optimization"
description: "Analyzes OEE, bottlenecks, live simulated Dynamics 365 downtime cases, and spindle vibration telemetry, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/production_line_optimization", "rar_sha256": "f740a969d2c10b4d2f43e86729ec97b49aff04521d30a57e2b90db79b77124ea", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.3.0", "author": "AIBAST", "tags": ["production", "OEE", "bottleneck", "throughput", "manufacturing"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/production_line_optimization`. The original RAPP
agent is preserved byte-for-byte in `production_line_optimization_agent.py` and in the RCI capsule.

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

Production Line Optimization Agent — a template you are meant to mutate.

Analyzes manufacturing line performance metrics including OEE, station
cycle times, and defect rates. Identifies bottlenecks, recommends
throughput improvements, and generates shift-level production plans
to maximize output while maintaining quality targets.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted systems (synthetic data, no credentials, works
     from anywhere):
       CRM  https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
            — Granite Peak Manufacturing cases become downtime events
       TEL  https://kody-w.github.io/static-telemetry/api/v1/
            — sensors, alerts, and 672-point reading series
     The two join on the shared story: the live vibration_spike alert
     on Granite Peak's CNC spindle S-300 carries the real CRM case
     number CAS-260132 ("Line three unplanned downtime from spindle
     vibration"), and its full spindle-vibration reading series backs
     the alert with real stats.
     Try: perform(operation="line_efficiency")
     (renders the CRM downtime cases PLUS the spindle vibration series
     stats and alert window joined on CAS-260132)
  2. No network? Everything falls back to the embedded demo layer below
     (PRODUCTION_LINES / STATIONS / SHIFT_SCHEDULES) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PRODUCTION_LINE_OPTIMIZATION_DATA_URL (CRM) and/or
     PRODUCTION_LINE_OPTIMIZATION_TEL_URL (telemetry) to your own
     endpoints, or replace _fetch_collection() / _fetch_telemetry()
     with an OPC-UA / MES client. Fields the rest of the file needs are
     listed in _normalize_live_downtime_event() — affected line and
     lost hours render as "n/a — enrichment seam" until you wire your
     MES. OEE and cycle-time analytics stay simulated until then.

OPERATIONS
  line_efficiency | bottleneck_analysis | throughput_optimization
  | shift_planning | capacity_model | implementation_plan | roi_analysis
  | monitoring_plan
  kwargs: operation (required), line_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "line_id": {
      "description": "Production line identifier used to select optimization, ROI, and monitoring records.",
      "type": "string"
    },
    "operation": {
      "description": "Operation to perform. Defaults to line_efficiency when omitted.",
      "enum": [
        "line_efficiency",
        "bottleneck_analysis",
        "throughput_optimization",
        "shift_planning",
        "capacity_model",
        "implementation_plan",
        "roi_analysis",
        "monitoring_plan"
      ],
      "type": "string"
    }
  },
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `production_line_optimization_agent.py` and embedded as the fenced Python below (sha256 f740a969d2c10b4d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `production_line_optimization_agent.py` first:

```bash
python3 production_line_optimization_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 production_line_optimization_agent.py   # or on stdin
python3 production_line_optimization_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Production Line Optimization Agent — a template you are meant to mutate.

Analyzes manufacturing line performance metrics including OEE, station
cycle times, and defect rates. Identifies bottlenecks, recommends
throughput improvements, and generates shift-level production plans
to maximize output while maintaining quality targets.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted systems (synthetic data, no credentials, works
     from anywhere):
       CRM  https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
            — Granite Peak Manufacturing cases become downtime events
       TEL  https://kody-w.github.io/static-telemetry/api/v1/
            — sensors, alerts, and 672-point reading series
     The two join on the shared story: the live vibration_spike alert
     on Granite Peak's CNC spindle S-300 carries the real CRM case
     number CAS-260132 ("Line three unplanned downtime from spindle
     vibration"), and its full spindle-vibration reading series backs
     the alert with real stats.
     Try: perform(operation="line_efficiency")
     (renders the CRM downtime cases PLUS the spindle vibration series
     stats and alert window joined on CAS-260132)
  2. No network? Everything falls back to the embedded demo layer below
     (PRODUCTION_LINES / STATIONS / SHIFT_SCHEDULES) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PRODUCTION_LINE_OPTIMIZATION_DATA_URL (CRM) and/or
     PRODUCTION_LINE_OPTIMIZATION_TEL_URL (telemetry) to your own
     endpoints, or replace _fetch_collection() / _fetch_telemetry()
     with an OPC-UA / MES client. Fields the rest of the file needs are
     listed in _normalize_live_downtime_event() — affected line and
     lost hours render as "n/a — enrichment seam" until you wire your
     MES. OEE and cycle-time analytics stay simulated until then.

OPERATIONS
  line_efficiency | bottleneck_analysis | throughput_optimization
  | shift_planning | capacity_model | implementation_plan | roi_analysis
  | monitoring_plan
  kwargs: operation (required), line_id
"""

import sys
import os
import json
import urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/production_line_optimization",
    "version": "1.3.0",
    "display_name": "Production Line Optimization Agent",
    "description": "Analyzes OEE, bottlenecks, live simulated Dynamics 365 downtime cases, and spindle vibration telemetry, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["production", "OEE", "bottleneck", "throughput", "manufacturing"],
    "category": "manufacturing",
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
#   export PRODUCTION_LINE_OPTIMIZATION_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your MES/historian client.
# Downstream code only needs the fields from
# _normalize_live_downtime_event().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "PRODUCTION_LINE_OPTIMIZATION_DATA_URL",
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


# Sibling live source: the static-telemetry API. The vibration_spike
# alert on Granite Peak's CNC spindle S-300 joins the CRM downtime case
# CAS-260132, and its 672-point reading series backs the alert with
# real stats. Override with PRODUCTION_LINE_OPTIMIZATION_TEL_URL.
TELEMETRY_SOURCE_URL = os.environ.get(
    "PRODUCTION_LINE_OPTIMIZATION_TEL_URL",
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


def _granite_peak_vibration():
    """The live vibration_spike alert (-> CRM case CAS-260132) plus
    stats over its full spindle-vibration reading series. Fetches ONE
    672-point series, lazily; None when offline."""
    alert = next(
        (a for a in _fetch_telemetry("alerts")
         if a.get("alert_type") == "vibration_spike"),
        None,
    )
    if not alert:
        return None
    points = _fetch_telemetry(
        f"readings/{alert.get('sensor_id')}", key="points"
    )
    values = [
        p.get("v") for p in points if isinstance(p.get("v"), (int, float))
    ]
    stats = None
    if values:
        threshold = alert.get("threshold")
        stats = {
            "n": len(values),
            "min": min(values),
            "max": max(values),
            "latest": values[-1],
            "over_threshold": sum(
                1 for v in values
                if isinstance(threshold, (int, float)) and v > threshold
            ),
        }
    return {"alert": alert, "stats": stats}


def _normalize_live_downtime_event(row):
    """Project a Dynamics case onto the downtime-event shape this agent
    renders. THIS is the contract your replacement data source must meet —
    a dict with these keys. None means 'not knowable from the case record
    alone' and the renderer labels it as an enrichment seam (wire your MES
    for the affected line and lost production hours)."""
    return {
        "id": row.get("ticketnumber", "?"),
        "plant": row.get("customeridname", "Unknown"),
        "event": row.get("title", "untitled"),
        "reported": str(row.get("createdon", ""))[:10],
        "priority": row.get(
            "prioritycode@OData.Community.Display.V1.FormattedValue", "n/a"
        ),
        "resolved": row.get("statecode") == 1,
        "line": None,        # enrichment seam — wire your MES line mapping
        "lost_hours": None,  # enrichment seam — wire your historian
        "_live": True,
    }


def _live_downtime_events():
    """Granite Peak Manufacturing cases from the live tenant, reinterpreted
    as production downtime/quality events; [] when offline."""
    rows = _fetch_collection("incidents")
    return [
        _normalize_live_downtime_event(r) for r in rows
        if r.get("customeridname") == "Granite Peak Manufacturing"
    ]


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

PRODUCTION_LINES = {
    "LINE-A": {
        "name": "Electronics Assembly Line A",
        "product": "Industrial Control Module ICM-400",
        "design_capacity_per_hour": 180,
        "actual_output_per_hour": 142,
        "availability_pct": 87.0,
        "performance_pct": 82.0,
        "quality_pct": 99.4,
    },
    "LINE-B": {
        "name": "Metal Fabrication Line B",
        "product": "Structural Bracket SB-220",
        "design_capacity_per_hour": 300,
        "actual_output_per_hour": 261,
        "availability_pct": 92.0,
        "performance_pct": 94.5,
        "quality_pct": 98.7,
    },
    "LINE-C": {
        "name": "Polymer Molding Line C",
        "product": "Enclosure Housing EH-150",
        "design_capacity_per_hour": 240,
        "actual_output_per_hour": 168,
        "availability_pct": 78.0,
        "performance_pct": 89.7,
        "quality_pct": 97.2,
    },
}

STATIONS = {
    "LINE-A": [
        {"id": "A1", "name": "SMT Placement", "cycle_time_s": 18.5, "takt_time_s": 20.0, "defect_rate_pct": 0.12},
        {"id": "A2", "name": "Reflow Soldering", "cycle_time_s": 22.1, "takt_time_s": 20.0, "defect_rate_pct": 0.08},
        {"id": "A3", "name": "AOI Inspection", "cycle_time_s": 15.0, "takt_time_s": 20.0, "defect_rate_pct": 0.01},
        {"id": "A4", "name": "Through-Hole Insert", "cycle_time_s": 19.8, "takt_time_s": 20.0, "defect_rate_pct": 0.15},
        {"id": "A5", "name": "Functional Test", "cycle_time_s": 25.3, "takt_time_s": 20.0, "defect_rate_pct": 0.04},
        {"id": "A6", "name": "Conformal Coating", "cycle_time_s": 16.2, "takt_time_s": 20.0, "defect_rate_pct": 0.02},
        {"id": "A7", "name": "Final Assembly", "cycle_time_s": 19.0, "takt_time_s": 20.0, "defect_rate_pct": 0.18},
    ],
    "LINE-B": [
        {"id": "B1", "name": "Laser Cutting", "cycle_time_s": 10.8, "takt_time_s": 12.0, "defect_rate_pct": 0.05},
        {"id": "B2", "name": "CNC Bending", "cycle_time_s": 11.4, "takt_time_s": 12.0, "defect_rate_pct": 0.22},
        {"id": "B3", "name": "Robotic Welding", "cycle_time_s": 14.2, "takt_time_s": 12.0, "defect_rate_pct": 0.30},
        {"id": "B4", "name": "Grinding/Deburr", "cycle_time_s": 9.5, "takt_time_s": 12.0, "defect_rate_pct": 0.06},
        {"id": "B5", "name": "Powder Coating", "cycle_time_s": 11.0, "takt_time_s": 12.0, "defect_rate_pct": 0.10},
        {"id": "B6", "name": "QC Measurement", "cycle_time_s": 8.2, "takt_time_s": 12.0, "defect_rate_pct": 0.00},
    ],
    "LINE-C": [
        {"id": "C1", "name": "Material Drying", "cycle_time_s": 12.0, "takt_time_s": 15.0, "defect_rate_pct": 0.02},
        {"id": "C2", "name": "Injection Molding", "cycle_time_s": 18.4, "takt_time_s": 15.0, "defect_rate_pct": 0.45},
        {"id": "C3", "name": "Trim/Deflash", "cycle_time_s": 10.5, "takt_time_s": 15.0, "defect_rate_pct": 0.08},
        {"id": "C4", "name": "Ultrasonic Weld", "cycle_time_s": 13.8, "takt_time_s": 15.0, "defect_rate_pct": 0.12},
        {"id": "C5", "name": "Dimensional Check", "cycle_time_s": 9.0, "takt_time_s": 15.0, "defect_rate_pct": 0.00},
        {"id": "C6", "name": "Packaging", "cycle_time_s": 7.5, "takt_time_s": 15.0, "defect_rate_pct": 0.05},
    ],
}

SHIFT_SCHEDULES = {
    "Day": {"start": "06:00", "end": "14:00", "hours": 8, "operators": 24, "premium": 1.0},
    "Swing": {"start": "14:00", "end": "22:00", "hours": 8, "operators": 22, "premium": 1.0},
    "Night": {"start": "22:00", "end": "06:00", "hours": 8, "operators": 18, "premium": 1.15},
}

DEFECT_CATEGORIES = {
    "LINE-A": {"solder_bridge": 38, "component_shift": 22, "missing_part": 15, "cosmetic": 14, "functional": 11},
    "LINE-B": {"weld_porosity": 42, "dimensional_oor": 28, "surface_scratch": 18, "bend_angle": 12},
    "LINE-C": {"short_shot": 35, "flash": 25, "sink_mark": 20, "weld_line": 12, "warpage": 8},
}

OPTIMIZATION_SCENARIOS = {
    "LINE-A": {
        "change": "Reprogram functional test sequence and add one parallel test station",
        "investment": 92000, "projected_uph": 171, "annual_margin_gain": 286000,
        "quick_win": "Balance work between A2 and A4", "process_tuning": "Reduce A5 cycle to 19.0s",
    },
    "LINE-B": {
        "change": "Reprogram robotic weld path and pre-stage fixtures",
        "investment": 48000, "projected_uph": 286, "annual_margin_gain": 174000,
        "quick_win": "Pre-stage B3 fixtures", "process_tuning": "Reduce B3 cycle to 11.6s",
    },
    "LINE-C": {
        "change": "Tune molding recipe and add cavity-pressure monitoring",
        "investment": 68000, "projected_uph": 215, "annual_margin_gain": 231000,
        "quick_win": "Standardize resin drying", "process_tuning": "Reduce C2 cycle to 14.4s",
    },
}

EVIDENCE_MARKER = (
    "[Evidence: product-line-optimization one-pager and demo transcript; "
    "capacity modeling, phased implementation, ROI, and real-time monitoring]"
)


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _oee(line_id):
    """Calculate OEE for a production line."""
    pl = PRODUCTION_LINES[line_id]
    return round(pl["availability_pct"] * pl["performance_pct"] * pl["quality_pct"] / 10000, 1)


def _bottleneck_station(line_id):
    """Return the station with the longest cycle time (bottleneck)."""
    stations = STATIONS[line_id]
    return max(stations, key=lambda s: s["cycle_time_s"])


def _throughput_gap(line_id):
    """Units per hour lost vs. design capacity."""
    pl = PRODUCTION_LINES[line_id]
    return pl["design_capacity_per_hour"] - pl["actual_output_per_hour"]


def _daily_output(line_id):
    """Estimate daily output across all shifts."""
    pl = PRODUCTION_LINES[line_id]
    total_hours = sum(s["hours"] for s in SHIFT_SCHEDULES.values())
    return pl["actual_output_per_hour"] * total_hours


def _quality_cost_estimate(line_id):
    """Rough annual cost of quality defects for a line (scrap + rework)."""
    pl = PRODUCTION_LINES[line_id]
    defect_rate = (100 - pl["quality_pct"]) / 100
    annual_units = _daily_output(line_id) * 250
    scrap_cost_per_unit = 12.50  # average
    return round(annual_units * defect_rate * scrap_cost_per_unit, 2)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class ProductionLineOptimizationAgent(BasicAgent):
    """Analyzes production lines for OEE, bottlenecks, and shift planning."""

    def __init__(self):
        self.name = "ProductionLineOptimizationAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "operations": [
                "line_efficiency",
                "bottleneck_analysis",
                "throughput_optimization",
                "shift_planning",
                "capacity_model",
                "implementation_plan",
                "roi_analysis",
                "monitoring_plan",
            ],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "description": "Operation to perform. Defaults to line_efficiency when omitted.",
                        "enum": [
                            "line_efficiency",
                            "bottleneck_analysis",
                            "throughput_optimization",
                            "shift_planning",
                            "capacity_model",
                            "implementation_plan",
                            "roi_analysis",
                            "monitoring_plan",
                        ],
                    },
                    "line_id": {
                        "type": "string",
                        "description": "Production line identifier used to select optimization, ROI, and monitoring records.",
                    },
                },
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "line_efficiency")
        dispatch = {
            "line_efficiency": self._line_efficiency,
            "bottleneck_analysis": self._bottleneck_analysis,
            "throughput_optimization": self._throughput_optimization,
            "shift_planning": self._shift_planning,
            "capacity_model": self._capacity_model,
            "implementation_plan": self._implementation_plan,
            "roi_analysis": self._roi_analysis,
            "monitoring_plan": self._monitoring_plan,
        }
        handler = dispatch.get(operation)
        if handler is None:
            return f"**Error:** Unknown operation `{operation}`. Valid: {', '.join(dispatch.keys())}"
        return handler(**kwargs)

    # ------------------------------------------------------------------
    def _line_efficiency(self, **kwargs) -> str:
        lines = ["## Production Line Efficiency Report\n"]
        lines.append("| Line | Product | OEE | Availability | Performance | Quality | Actual/Design (uph) |")
        lines.append("|------|---------|-----|-------------|-------------|---------|---------------------|")
        for lid, pl in PRODUCTION_LINES.items():
            oee = _oee(lid)
            flag = " **BELOW TARGET**" if oee < 75 else ""
            lines.append(
                f"| {pl['name']} | {pl['product'][:24]} | {oee}%{flag} | "
                f"{pl['availability_pct']}% | {pl['performance_pct']}% | {pl['quality_pct']}% | "
                f"{pl['actual_output_per_hour']}/{pl['design_capacity_per_hour']} |"
            )

        lines.append("\n### Daily Output Summary\n")
        lines.append("| Line | Output/Day | Gap vs Design | Annual Quality Cost |")
        lines.append("|------|-----------|---------------|---------------------|")
        for lid, pl in PRODUCTION_LINES.items():
            daily = _daily_output(lid)
            gap = _throughput_gap(lid) * 24
            qcost = _quality_cost_estimate(lid)
            lines.append(f"| {pl['name']} | {daily:,} | {gap:,} units lost | ${qcost:,.2f} |")
        live = _live_downtime_events()
        if live:
            seam = "n/a — enrichment seam"
            lines.append("\n### Live Tenant Downtime Signals (Dynamics cases — Granite Peak Manufacturing)\n")
            lines.append("| Case | Event | Reported | Priority | Status | Line | Lost Hours |")
            lines.append("|------|-------|----------|----------|--------|------|------------|")
            for e in live:
                status = "Resolved" if e["resolved"] else "Open"
                lines.append(
                    f"| {e['id']} | {e['event']} | {e['reported']} | {e['priority']} | "
                    f"{status} | {e['line'] or seam} | "
                    f"{seam if e['lost_hours'] is None else e['lost_hours']} |"
                )
            lines.append("\n(OEE and cycle-time metrics above remain simulated until an MES is wired.)")
            vib = _granite_peak_vibration()
            if vib:
                alert, stats = vib["alert"], vib["stats"]
                unit = alert.get("unit", "")
                lines.append(
                    "\n#### Spindle Vibration Telemetry — joined to "
                    f"{alert.get('crm_case', 'CAS-260132')}\n"
                )
                lines.append(
                    f"- **Alert:** {alert.get('alert_code', '?')} "
                    f"{alert.get('alert_type', '?')} "
                    f"({str(alert.get('severity', '?')).upper()}) — "
                    f"{alert.get('asset_name', '?')}, peak "
                    f"{alert.get('peak_value')} {unit} vs threshold "
                    f"{alert.get('threshold')} {unit}"
                )
                lines.append(
                    f"- **Alert window:** {alert.get('window_start', '?')} -> "
                    f"{alert.get('window_end', '?')}"
                )
                if stats:
                    lines.append(
                        f"- **Series ({alert.get('sensor_code', '?')}, "
                        f"{stats['n']} points @ 15 min):** min {stats['min']} "
                        f"{unit}, max {stats['max']} {unit}, latest "
                        f"{stats['latest']} {unit}; "
                        f"{stats['over_threshold']} readings above threshold"
                    )
                lines.append(
                    f"- **CRM case:** {alert.get('crm_case', '?')} — the "
                    "downtime case in the table above (joined by ticket number)"
                )
                lines.append(
                    "\n_Source: live static-telemetry alert + reading series "
                    "for Granite Peak Manufacturing's CNC spindle S-300, "
                    "joined to the Static Dynamics 365 case by its real "
                    "ticket number._"
                )
        else:
            lines.append("\n_Live tenant unreachable — showing embedded demo lines only._")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _bottleneck_analysis(self, **kwargs) -> str:
        lines = ["## Bottleneck Analysis\n"]
        for lid in PRODUCTION_LINES:
            pl = PRODUCTION_LINES[lid]
            bn = _bottleneck_station(lid)
            lines.append(f"### {pl['name']}\n")
            lines.append(f"**Bottleneck station:** {bn['name']} ({bn['id']})")
            lines.append(f"- Cycle time: {bn['cycle_time_s']}s (takt: {bn['takt_time_s']}s)")
            over = round(bn['cycle_time_s'] - bn['takt_time_s'], 1)
            lines.append(f"- Over takt by: {over}s ({round(over/bn['takt_time_s']*100,1)}%)")
            lines.append(f"- Defect rate: {bn['defect_rate_pct']}%\n")

            lines.append("| Station | Cycle (s) | Takt (s) | Delta | Defect % |")
            lines.append("|---------|-----------|----------|-------|----------|")
            for st in STATIONS[lid]:
                delta = round(st["cycle_time_s"] - st["takt_time_s"], 1)
                flag = " **BN**" if st["id"] == bn["id"] else ""
                lines.append(
                    f"| {st['name']}{flag} | {st['cycle_time_s']} | {st['takt_time_s']} | "
                    f"{delta:+.1f} | {st['defect_rate_pct']}% |"
                )
            lines.append("")

            lines.append(f"**Top defect categories ({lid}):**")
            for defect, count in DEFECT_CATEGORIES.get(lid, {}).items():
                lines.append(f"- {defect}: {count}%")
            lines.append("")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _throughput_optimization(self, **kwargs) -> str:
        lines = ["## Throughput Optimization Recommendations\n"]
        for lid in PRODUCTION_LINES:
            pl = PRODUCTION_LINES[lid]
            bn = _bottleneck_station(lid)
            gap = _throughput_gap(lid)
            lines.append(f"### {pl['name']} (gap: {gap} uph)\n")
            over = bn["cycle_time_s"] - bn["takt_time_s"]

            # Generate specific recommendations based on bottleneck
            lines.append(f"**Option 1 -- Reduce {bn['name']} cycle time**")
            target = round(bn["takt_time_s"] * 0.95, 1)
            lines.append(f"- Current: {bn['cycle_time_s']}s -> Target: {target}s")
            lines.append(f"- Method: Process re-engineering, tooling upgrade")
            gain1 = round(gap * 0.6)
            lines.append(f"- Expected gain: +{gain1} uph\n")

            lines.append(f"**Option 2 -- Parallel station at bottleneck**")
            lines.append(f"- Add second {bn['name']} unit")
            lines.append(f"- Effective cycle time: {round(bn['cycle_time_s']/2, 1)}s")
            gain2 = round(gap * 0.85)
            lines.append(f"- Expected gain: +{gain2} uph")
            lines.append(f"- Investment estimate: $45,000 - $120,000\n")

            lines.append(f"**Option 3 -- Quality improvement**")
            high_defect = max(STATIONS[lid], key=lambda s: s["defect_rate_pct"])
            lines.append(f"- Target station: {high_defect['name']} ({high_defect['defect_rate_pct']}% defect)")
            lines.append(f"- Reduce rework loop time and scrap")
            gain3 = round(gap * 0.2)
            lines.append(f"- Expected gain: +{gain3} uph\n")

            new_oee = round(_oee(lid) * 1.12, 1)
            lines.append(f"**Combined projected OEE:** {new_oee}% (from {_oee(lid)}%)")
            lines.append("")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _shift_planning(self, **kwargs) -> str:
        lines = ["## Shift Production Plan\n"]
        lines.append("### Shift Schedule\n")
        lines.append("| Shift | Hours | Operators | Premium | Start | End |")
        lines.append("|-------|-------|-----------|---------|-------|-----|")
        for sname, s in SHIFT_SCHEDULES.items():
            lines.append(
                f"| {sname} | {s['hours']} | {s['operators']} | {s['premium']}x | {s['start']} | {s['end']} |"
            )

        lines.append("\n### Planned Output by Line and Shift\n")
        lines.append("| Line | Day Shift | Swing Shift | Night Shift | Daily Total |")
        lines.append("|------|-----------|-------------|-------------|-------------|")
        for lid, pl in PRODUCTION_LINES.items():
            uph = pl["actual_output_per_hour"]
            day_out = uph * SHIFT_SCHEDULES["Day"]["hours"]
            swing_out = uph * SHIFT_SCHEDULES["Swing"]["hours"]
            # Night shift typically runs at 90% efficiency
            night_out = round(uph * SHIFT_SCHEDULES["Night"]["hours"] * 0.9)
            total = day_out + swing_out + night_out
            lines.append(
                f"| {pl['name'][:28]} | {day_out:,} | {swing_out:,} | {night_out:,} | {total:,} |"
            )

        lines.append("\n### Operator Allocation\n")
        total_ops = sum(s["operators"] for s in SHIFT_SCHEDULES.values())
        lines.append(f"- Total operators across shifts: **{total_ops}**")
        lines.append(f"- Lines running: **{len(PRODUCTION_LINES)}**")
        lines.append(f"- Avg operators per line per shift: **{round(total_ops / len(PRODUCTION_LINES) / len(SHIFT_SCHEDULES), 1)}**")

        lines.append("\n### Weekly Capacity Summary\n")
        lines.append("| Line | Weekly Output (5 days) | Weekly Output (6 days) | Weekly Output (7 days) |")
        lines.append("|------|----------------------|----------------------|----------------------|")
        for lid, pl in PRODUCTION_LINES.items():
            d = _daily_output(lid)
            lines.append(f"| {pl['name'][:28]} | {d*5:,} | {d*6:,} | {d*7:,} |")
        return "\n".join(lines)

    def _selected_scenarios(self, **kwargs):
        line_id = str(kwargs.get("line_id", "")).strip().upper()
        if not line_id:
            return list(OPTIMIZATION_SCENARIOS.items()), ""
        scenario = OPTIMIZATION_SCENARIOS.get(line_id)
        if scenario is None:
            return [], f"**Error:** Unknown line `{line_id}`. Valid: {', '.join(OPTIMIZATION_SCENARIOS)}"
        return [(line_id, scenario)], ""

    def _capacity_model(self, **kwargs) -> str:
        scenarios, error = self._selected_scenarios(**kwargs)
        if error:
            return error
        lines = ["## Production Capacity Model", EVIDENCE_MARKER, "",
                 "| Line | Current UPH | Design UPH | Modeled UPH | Gap Closed | Change |",
                 "|------|-------------|------------|-------------|------------|--------|"]
        for line_id, scenario in scenarios:
            line = PRODUCTION_LINES[line_id]
            current = line["actual_output_per_hour"]
            design = line["design_capacity_per_hour"]
            gap = design - current
            closed = round((scenario["projected_uph"] - current) / gap * 100, 1) if gap else 100.0
            lines.append(
                f"| {line_id} | {current} | {design} | {scenario['projected_uph']} | "
                f"{closed}% | {scenario['change']} |"
            )
        return "\n".join(lines)

    def _implementation_plan(self, **kwargs) -> str:
        scenarios, error = self._selected_scenarios(**kwargs)
        if error:
            return error
        lines = ["## Phased Optimization Implementation Plan", EVIDENCE_MARKER, ""]
        for line_id, scenario in scenarios:
            lines.extend([
                f"### {line_id} — {PRODUCTION_LINES[line_id]['name']}",
                f"1. **Quick win (days 1-7):** {scenario['quick_win']}",
                f"2. **Scheduling and tuning (days 8-21):** {scenario['process_tuning']}",
                f"3. **Investment (days 22-60):** {scenario['change']}",
                "4. **Risk mitigation:** Run parallel quality checks until three consecutive lots pass.",
                "",
            ])
        return "\n".join(lines)

    def _roi_analysis(self, **kwargs) -> str:
        scenarios, error = self._selected_scenarios(**kwargs)
        if error:
            return error
        lines = ["## Optimization ROI Analysis", EVIDENCE_MARKER, "",
                 "| Line | Investment | Annual Margin Gain | Payback | 3-Year Net Benefit |",
                 "|------|------------|--------------------|---------|--------------------|"]
        for line_id, scenario in scenarios:
            investment = scenario["investment"]
            gain = scenario["annual_margin_gain"]
            payback = round(investment / gain * 12, 1)
            net = gain * 3 - investment
            lines.append(
                f"| {line_id} | ${investment:,.0f} | ${gain:,.0f} | "
                f"{payback} months | ${net:,.0f} |"
            )
        return "\n".join(lines)

    def _monitoring_plan(self, **kwargs) -> str:
        line_id = str(kwargs.get("line_id", "LINE-A")).strip().upper()
        if line_id not in PRODUCTION_LINES:
            return f"**Error:** Unknown line `{line_id}`. Valid: {', '.join(PRODUCTION_LINES)}"
        return "\n".join([
            "## Real-Time Optimization Monitoring Plan",
            EVIDENCE_MARKER,
            f"**Line lookup:** {line_id} — {PRODUCTION_LINES[line_id]['name']}",
            "",
            "| Metric | Current | Target | Alert |",
            "|--------|---------|--------|-------|",
            f"| OEE | {_oee(line_id)}% | 85% | Below 80% for 30 minutes |",
            f"| Throughput | {PRODUCTION_LINES[line_id]['actual_output_per_hour']} uph | "
            f"{OPTIMIZATION_SCENARIOS[line_id]['projected_uph']} uph | Below target for 2 hours |",
            f"| Bottleneck cycle | {_bottleneck_station(line_id)['cycle_time_s']}s | "
            f"{_bottleneck_station(line_id)['takt_time_s']}s | Above takt for 10 cycles |",
            f"| Quality | {PRODUCTION_LINES[line_id]['quality_pct']}% | 99.5% | Below 99% |",
            "",
            f"- **SIMULATED WRITE RECEIPT:** `MON-SIM-{line_id}` for Power BI/Teams alert subscription",
            "- Simulation only; no dashboard, alert, or external system was changed.",
        ])


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = ProductionLineOptimizationAgent()
    print("=" * 72)
    print("EMBEDDED DEMO LINES + LIVE TENANT DOWNTIME SIGNALS")
    print("(live sections fetched over HTTP; falls back offline —")
    print(" CRM downtime cases + spindle vibration telemetry joined on CAS-260132)")
    print("=" * 72)
    print(agent.perform(operation="line_efficiency"))
    print()
    for op in agent.metadata["operations"][1:]:
        print("=" * 72)
        print(agent.perform(operation=op))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/6286bKrVrYu+CqKfX+kM/E2Ej2uOFUFAgSi74Tg+oSTvgfRCVDefPeaWrtxk3lPnaioHfa2NJlzzNF+Y3wrFv7Hp3CZi3789PMnRmIZ2/n046ckneKxfMxl372Xu7DZX+l00Hn+x0PUz3OTdmlcTz8emvKZHqayXZpwTpMDt3dhW8bTASXwQ9Kv3Vy26SEOpxTsDbvkMD3KLmnSw7OMxvAt/jCnTdqm87j/eFjLuQC7Dn2WNWWXHpK07Q9Z2DRRGNc/AbXSLWwfTTp9+vl//uePn0rw+dPP//gUN+EElj4ZY58s8VuoAk7rQPu2fH1cwuRpN4PzTdjlYONjB/Z24PsjHbN+bMFSkmaHr99+mNIm+/Hwt7/Vazjm018Pn//PwzSPP//SHb7+6cHOL8r/x+HLpp/ydP7hl0/fH/zy6cfDL5/eRvyaZlkZl2kX7798+utvMpJyeoRzXAAR//ht9f3n35z7+fDW6adf//Tgxz8f/C00v4bvmE3l9Nvhf/PwXwTMxdgvefFY5l/73/nvNyH/mw3/Imgqymz+9QEc3pVd/tv5P67/y7E4fIRxOe+/tn2SNr8d++P6vxx7ZwJIom7+UOZD/G9n/83DfxEw9uW/8djvV//lSNt35dyPwIo/3fenB787+M/fPhbhuwxGEP1vifCRQt8T6HeZUmbfd5fTQeu79Oc/6jKm8zJ2h+yXT3/7Gz+O/fjz3/52cLu6A/X3u1z9+z++f/7n33863MKmTH4+/OMvPx7+8lPVl90P3zWp03364a9//ecvn3676OslXzX54Xt1fPonKMQO1MeXynvX4f/4Hwe1jMd+6rP5YMf9Mh/G5QMJful+6ZwCWAH+mYsUCH2m41RGABC+7HuMfZV+CAIgcPj7/x2WUTjNn8N3/U6fmzdojDv8+F7oXyri95kILHOAZOD/vAShO1iMYfzSfQh43/oY0ykdnwCqon1OP4N6//z+cCiBf/4rsb9+SPjpsf/9A8bA9rf+1lkC4PaYlib96W2bV6TdV0tigGPplsYLEN70MdAkK5s3CgIF+gaA5vz2w1SXTQNSYARG9+P+IRv46ue3sL///e/A+OKX7gtcoYcvkDzBYMN3dQ6fPwOTAFzmxfwLqO2iP/zlH//8y+F/Hf6rUx/C33cYADm/RgJoeLV17QCiuryrBQQJhDUNk49I/OOfXx0LxHQgE0HcyqxMvxwG3qrT5JuXbZH5jODEIUqBd4Fn20c/zqAaDuX800HKDt/1BZe+H02H8FD00wzg/pF2yRvYgNQQmPPdk10/HyYQhykDXWKZ0o9b/w6S4UPF9tcYbP/7QT0bh7nvG/DXW82PTeAwKEfg/u858GUdCBn/Mh3YbyJ+OmjvXDw8wjF8FGP49Y4s/BKXfjx8Ow6Eh4cuXX/p/ggsX9wDNgHPxF9D+vkd80Pcty0I7PTt7o89H+3S6UF2p+Mv3fQ16cPxHYq4B6rsh3wpk7CL0//ja0pNRb80yYf/gKZvSV+jkHyNykcO/tYFD+82ePh9Hzx8NMLDLwtyPGHADGD44924D3u/fNzdpiF4DkxsF2DVl6T+3v2BEcvbIcsb2w4fHfpry3xreXg38XfrL7u4WZL3lo9xYfrinl9AWGPgjDcMfJ0FQM8FZh/erphAZoDIz19y6g8TxtsdLfByMv3S/dZ93mk1Ajd9ZOoXcd/cCqrq3WQ+NyCgzeG3oj680fgtBFgXbm+fAJhY5rewtXjHqQW5MIN/36oPC4DHGSQiKId0nj4cIerewREl++DwqqEwDn/wdEu23xh5+umgAzmgUt5hifoNJPvhsTTN9GVCehsxggx4B/ZLrYmOYxyysW8Pjqd/hdm86SMw7ewf5QCiOu3v1JwOP0w7MD2d33kVzuGPh64/xGP64bCwAeav/VhPX4V8yAy7fS3SMf3rb63ibKmg7czzY/oZhus+2T+vP+Vg4Fqin8oe/ohS/Dn5Or99BvMbHD5K+H0f/KR/QuA/9b8vKXQZQ9Ds0oORhvVB/UN+fAx9AARA9NLfRkEQExCw77IcXvl/V+r7hPih0fP071WZ0m7qx3cugP70LScIEvn8AL3tjTXhR06Cugcp9lXCu2LntT+829+h/1KdUwEKAfj+Xfc/f4W35+8G1l/BCFunX275Kgac/L0jAK6ctfP3Udf+jB6PwB3j+A0vPxLgHY+3j77K6JY2ArlxZuzPCHE8ocgBzJMfBQySPgWA1X0MTUCz7778iPTXW75K+a4lmDW/eKAE+JqBRPy28fNvk/cfXXJ4D9nfHPPW8sPCLzP5h8LvaLwL4Yvn3s75NjB/nyv+47+YeX8Y3+A+fvHA2/g/0oODobj2lwD8C0X4Q8w+1Pgw7ZuCHZD0EULgHLD7Nxd+XI0AaO8BYM/vIvm/DvwbWkHvBXa/mcUXs9+I9746BTFIkreP38yjCXcQkSht+vWbDYalc+7ZkXTtV0XSePsAH2yHeX//+ChKgvOrfRZ5zlV4+6/fUvPDmx/I272bzFdhMegyBTD8K9v58Cz6E6gikF0APQAkA2eF88dpRbrxB45xmIPNM+oXnd7z5rcM/JNev+qGI6lS8KHZr+9zv7qWcvgBuP2vb9fB/fjfOQiq88u57xX417en3podQPC+igBh/SgxUHL9G9xAnoJu8GuWglHy17hvmi+97Ye/Ag99Xf0u74dv2fGN+unG+bPLgJ0qcG7clO955SCUaZN8K53pO8x+NNcuTcEjULJfBTXlB3SCev61e3emBsD8r+8K/vVbvv36gUE/fI9OmL3bEDjz0dGAd75Jes8kxUcUvqTuIZzA3N/B4beTaQcaXvFuQSAUYfvLp8N7zG0+uukKBoAPT32VBuz56d0QPzL3oxV+/kj+D34xv/smSOz9d1T6iyhgZ/fRfHSDt74k2lvgn6oMjHv/ht2B1f8dnwMi/tfhj1wMLPyRZYGFf0OdwOofyNKHpD9zIbD4hR78/Dv+AQBgWIBXkr/++EX/MnlT8jIGwJ1++rkDIPXjJ9B+0v8WlX8PaiCFAKC8fwQAujy4Zy7Tj2/fpIOPf/xBxu9mo49gl99mjvE9ECbv5AYc7j2U/IHcHixd+oKmvxn6raW/fywx74+30oAEgQdvQvTd6H9VQf/uD3DZVwD96cClWbg0ANfA4p9ju75JRd+WM8iKjx+CgFbx6ef/+WekBU/+TQ68tfv3OQCe/DEBwMIfE+DTj/+OWIPV3ycA+Pqn6H/6z3/xyD+/r/TRm9+9ffQePL/88OUfn0Agw/ek8TWUXykg2A7o3ufpPfzCp5+O75vD8QuJAc/+P5DDrxJAiwcEBYjISOwY0gSdIPHpGGEJkmFoSoGhgU5jmowwGmDDEcORU4IeQ5xMkYg+JhFJRyR5QrA0fPsQlHic/vqeUcu3VscTjRHgEYrgKEJHeJISdISFGUHTJEFn+Ak/pQhyQn47WoMG9tXUL6a93fWdp75d8tXif3yKCAzsFLFJYr78OcO0S4eoEelXJYPt2XzJZqlb0rz7FNY9jWVXpJYKT1m41y8tTU6xnV+nqmxt5nRFMhEMJUMWs/ACLxxUL/PCiPs5Le0AmVGXbPIyd8PqaFPHpRQ5lfMXBqWO4jHUSVJwNsiY/MLHXSh7atXpgaLS03/CGAnTjdY/sUSPQt5LDfjxChgvcaLJUPZL5qSmY7x8RJvblKxQuJOCZ4h228QRGo6JJfriPUzdCBU22ZRThE7gKq7muvR4RYxJbYT5NFe+a1dRvmbFjnc54xsh9UKs9sVv6OpPJns5uydEzeW6U3gOW1+ULMr4hoEwckpuohSBJ1iPSnmbOxDcxa+Wv+vtRJ1hHGaoemZz57Ex050rK1kndgjCd8S/it45FKczUyZtVlthDGWq5DsnVeTZKazmlDVo8SlCGUJgjhEpEtfiuMBImtGQ1MvoMwcdJvSFkMYFRRfo1ZXEAtOc74f4ODE9h/lboOkyB7VObbXUKdFWU0bvxtnYSoFTGA2TnvPUwzRcuhELEy59hyCGqVaQjyeWjEZjlK/iMaA29SpCnKp59o2iGXbCmVewS+R0eWqUlq9YHT8QP/WNrGPu5yLnj5mfiu+E0VyOCs7ba3YDH1f7tndF7zSj8FJucMul+izURsUkGTZ5wSnPjPuICFq4PEcEXZC70Z2PcZQ+oWfShW7H9SKsqAXFIeLl7NsImU2Rqtrra+avsXHD9ledwTnm9S+PKfyr6XXo65RUNczffXKi+UpCuVTxJCc+w0fmRINsTGX2eU9naNrFxLXO/JpeDOas8yNKThxp5RQN5ZuvXhjlLuMr81p1WnrRmCEz3Xyp0FfJ5ON4P7d3Q9xs5nzuLNWFWG3nxk40I+3JCqsbQhDq5YxoSoDFcla9qKUk8vz5QkGiybwSbaDTdnkek22Z/Afr5r36qsDYSJWDODC3Gue8W48Vvmr6l8bdkj2WEavyncobt/20bxeGS4kCY4tLvUS86DEyK+8YOylrfrldhb2rhA7lWUpjGSTKsFRfVTHFNBFDhlDAriaP49I51GMM6ySuqqin5Tg4m9Tlk1Wjk1kwgmYvYsvYbKjtjKzxWF+sOuqI0aJitCgzGxw0R3NWkz4v1BTZy4su0G7I5StLDYZVF6Hx9ILwBZ/1fMeIFyydb1t6tzaYeFqGMhHzETdeUU/P042AqwR+YFTqiPDsjbC+pfDrMWvLyJexzbltlU7cIzeZI6dvK1MZyIbotRBcX8hqPZgbdqbNMyH0RW3RDkrrdqdU80LTy3RCkOzsrXrOEjbAFd+z0jsc6K8apsru/JqCDiH01r31on+zo6hh9+eR2XkX9a7ssMsCf6Yu9u7nqzDYqiSsUFgS+Xlmd4AdYn7sTjOL3l1Cnm+SANpYp0aljDNFKdNzJeBpAg0xonEr1+YAKa6jFHAUgbLHh2w2leg8Lkm6bdxAMzrjxqf9Qp+l65h6xfOucZnQD8PjVqlSdXN4by4r+nI0mXh3a8Y7m95RJkC+K2R+u4TiyzgjkT7yhsNm/Mt8mOKJDHsmt3pcKZ4ie46Lsz2P5yu/HqPJrgItGzbdRbyplyL7vFJnVenSGtTdLJm9ck09VlFKgrxhcqMVlWJbV9JpariEzoKTFwZPzx1kNxFXnNMivrzsS52fXhA3q+gkWfkaQoOxMjnUk81xv+Xyww80zOtyHeYBqlZDfiJfbgDsQguEXplW5bZ8SveqMiiIRWXV1CmTmvB+Xc+GvxoXihf89W4/KpSkiCg23auXAZAf9Vx11vhcRkeWjJFA5GljM5mEb8xgbdH9zDS0dT8GOsOF8kbDs+kXsIyHAny5BreYE1X+WMEDvEe8XHnzMWedYTWRpD/f2tvOvgoJlkWt8hGFmeKLF6ueUHs6YhmzVlz062sdvGOsnvU1IFUiSeihzZHqOmPV7VkhLL2wjK1YkryTgzYy+dlNS/5e2wOUMrkwSJT9ZOTbIyrT3DpikouWxxPLKc9owK4rJOaOrlw1xy9s3VB0Laujk6IbNz/NJdWQLjFUBMhjKAmfuDy3VFpOAWlOQym4Zhqdq4YUa5TKDYbQvRGFlgceaNCFMpzQvpSX81pjGE7x4WlMPJZcPcp/aR5WP8+iSrC+qmOEG9l8ZHOwURabTsjnTjdjKxVM7SpDovDMFj7So1ZZXyeWSs8yykBMVlfh0c133lYo1hnpHIYXGoY7FGbhqiNZFb+vMMJxpi2fg5WTnBsvY9wSHqOR4O6qBUfxK7aN5g6oFWI1eNbMfkEuhiAZAsYc+8hjnOVUJzfL8q/w1TpVNA9bAZmLocxxCkYW6YbEi9VQMAWnm9PgDsMV+abRHQP713C7etwtQNfYhZWnf5RFmJTwoWKMjFoYRu+5ADruoW97ZErksWdaPkB90BBVlboGvlNI/poH014EpqC5z/OVOdZuIZmcrubK5mi5NXMLZhwFwbcQftr9SCZs7FUtIWw49MLrDSng0KI3p903SesusZjei882YqNhza93r8ObawFDmS9JgokqrGkNtAqCy2ls39Pk5Xgi8BM1asLlwoV5gc77sPoIrSoclzqxCcNHk0yNqkqUZWbvR2njxOmKQP7AyU/t7PJdzyuZke187tPzhkPnob+ysnjbqg2K6aPRIgKz23eIVx/oKz9zmzMBWDoGeaVc0lgsVnpE7JBKMbtln5utQKTTjYnL6Sund8hz1bWpIpgUSLhVMvlUxK0RnmNDIB1rhErpEsKdF0/RKpFidG6KI6jCE6MnHm+reEiO83pWF/5pZ8kAS02t9nGRMe59543ueqoJKErlS16qm77m+fGZG5i53mLHTgDWCUK4Vn4bqRbH827yGIvqFQqvjF0hwdNSbKaPOItpSGYbJhZAYsaGm/JEWDvMellms/Mm32uWCn1l0U68YiUvSzG8LC8rRkc62DR5dWnEG3SmSMBX4jYK8NeCSIz0DLoB2a/HIB4RKz53F4trkK3dX9HLf0IhQvbnSnPa5nZkpDXWQx6w85OHmIt/yfQyTbL5/kT3OXnw5u3kLtAtF4fAVtm6QW5ptZ3mPMleu+q5XmVhuK1PNjT74uoPaeAlUnhkMQo5Cfo0d7nr5TZ3dvO7P4TWkDTEwNP4XCK8GLGtLCuxY3m5dWv8Orvq0jrPbX+0XOt5nlCIHKvcikGUpZ7UrMk9imsrbUQP+zIuEFNX84Uv3hh76VzO8S91XT3Og2NMUw/gCAqyR3zOHe9EV5kjyrazt0ngACsew55XAEur6gomH8aPHoprZkFMZeXsFi+XO3miIA+hPYkaDDqwfksfcLloIxHnZks2r9WXyq42WeTqVcE5Inmrdubjq7v7sk2cDasvI5y+z8DNRpH1nJZZr8V110HlVj6DTq+yqgft2WlaJVT3ydT4BNTschNPoydkIYveniYGuNtNtMjzqxIUftDDC+fwdrePci6uMF/mNx1MxecX76hV51uXrYrN1T7Jgnek+OrOktIu702lES563B5XyT5KqwvGBWQXFYG6RDY9Xdz6vL6u0swzKIuYs5WlKmva1uh5zD090bkPceVwnnJ0iFzIOfu8pNr+Hqzbi33omRjzZCBdL4ZYCfrxtsipemVbbPBDOuRvzNiGCX8xBkx8YhHdkNBLh+YXdH/Kac96/ZXKBgIdX9fZZdO5uFLcKcc6JLxxMD7yFfqsA+zsDoLQjNi2shu+2042vaimUCfGHkS4LqL9Sl2WnEXpwjsSrqVvWwRtLblhr1XSbUKSldyAtdf6mh5gVsZamqQ6bFwe8YMiwIRolY/jQNyGq2h6D0fUc2x9uD7TV4xYB4N2nCOt74VyOLa6W0x6nr403YudCeILRbdU3ClijOEWhqsKIjLP99ITRgmVxQDtnnTOndZgH2KLvwubXlon9m7hJml6/A0M3I3thSuEXRDFR1RAgDlc3e3HFrMKWqtXbCVlJ8NNI8d6KdQfZiXJxelWZEPgKQJtrbUy51xoS7qqkmLfvc7YTsJcO8fMrl7c6IHXat68KCFy2vLMBkdINwsp2lTtNAzkubRs4rhFTJ9ZeNdOXLgaUMbTN8G0TZ8bTduw4lXiAOkFtGGrKX+JL+xTdJDWmnq58QYmeTJiWZa+aLmm2tOCrJLU4HVQaazhemNg24pViaouRe3HjJaZCUTjRR9J8MUaC/PxfDzGSq0F5zi/Bix8nvPBuDdC85qizaHOBSOHab6CEWRWmevrcjexvOCZPqz5kjvmZHu8gikiXMyTw3bLw06Fyd7N1IotiXttbHrn8q1eJRyMNWGA33IEe/g4cC6X9Vg6zPF1H09OXG2LrqHOqgpe4FEdXHqn8PHY+R2MqVvsk0rY+AxxVM+KljhFwyGVEvezB6MOxJyqIwloTpZgcBBn2ZQ/wEAPNenk9/JJ7v0ocyOOnC1dOCsYNGJzgl22+vG4bPeeXCR5DXxFuK8kZzRHjCPkWsyiXcqPqnlHdEO4mJcqv1+Tk3u9k0q1cA3Brs7r0dHB6SLRp+cGes9pNEp/U3wPP+eMzLVZadx4IROSErHkK/uYZ03WyEUUA54Go6hvACpJz1AQuueHwXS3/np7gMZrYcudpKFQb5RbWDYPMW2HhDLLFg5VmlFbpKZ1tt+uNh1e82peL5lPMrgknAMSqdJhAeY2uU5Scnl7kK/YrdOZDs1BQXUoWHS/Q173OOS7+/GqjEfUjU1zYa4NvlFSc+4Knk2itSR4NMVE+ISXKkKK0FNDb/fHkX4ElX9H6CJzcBqF1CIgxmOZ9xRFTtvdYV8WkklbIqgsjzrHa4pAxxZxvKshEAF6QoZsLTJeELsieqwBW7Ozf60QeOkXqxhW0Zdw1GQjflWPcXmqztF4c2LFIvbGIveyN55QzBKTsMWdlrtWi5xeuk/0rwhJQm15HJP5ju8rv0OgaVST7MDO3ZRh6FFoaJCThCOSWHke4VkQ7+6t65WBRfEnGeICdntla9SNuQjFqWMZrslC6GXrZRIfo5A6IdYr6+/dwzyqKL/JZWPebg8BnGTxnXyNbJh0w70NF+54sj2Lh7PZCpEhqB7XAcpK6nps2EvrwizFzGFgIR7QuPCWuR468rQ8fGpfe8dCAH1xHqaKMFY0USGjWAheva57ortGxr1yCG/JwDeWUAuwNeQiLkHyiysSjNifLXoi8F7D+Ut+yULacrGpX4g4UneNa2CMCx78hOleWwyUV2md+6rUyuzgeeK0pUfrwY0zksAvyDE5b3GdKfvjqMo4xV4MGat6Q6yXFk00I7u7kKtvTWs8Bag+JvbxEY1couj6ZCzExe5rRHxkC6vmkXEZi5MOUIhc6IBP4rCvIbFzEMxFziKxni1xqS9oEj7K5IWQCFWvNHdhKPdaCE7vtN5s8bJxOjWOeAS62CdAJpExI+ZsR4OBR10Eu0RIGqlBij3XGNlyKVWVRJe8vlKjlPHA3Mlc5Lq4bsliobOvXdx+OspXCJpxTvCvgIOlgbOpjUu9LIJ7lTfOMP22d9KwRDi0HLhsIWNnkCaaLcOCJQ2AQET8osQuW4VeSzaaSpYHQp+QJ7oU2DLy8Al6mdVVibT8+boQm3mPrY7lstf4Mm7sVVi8anAatXPOdcHJbIjq97YPHMfgc3Plso3kR7McXoseb2LNnMdrnUHyRcLADEsIIvgeGGfXnS3GciVk78CwcVE1uLD4E8qo9hbpsIeHtl+O00XCXxjjKU+JUKJSzs0EtnleJiv01jg6mVenlUl5QdqDWeOBbZN/8R0r8wXdMbp8BHEjNzq5y1vAUFTHnO1j3l6cGFAsng7M8nzpPd7DytrE582pl1WqEQln1pFTHsR4bXhic188NW5kyqm3YxShoxtW5m1jpJsLTYv/6meXpOXH/KK05Eyt3qYpZ/Vol2RDVHWCHPVJJQlMSC91itiIy7TSXWGrjcC0rSKtsJCFLW2jLbfumnFmKpU3gniSuyyIJJBbiaFwtheh+ClghhrFeGWFGaZmfNEYKA5w181L/RcpzrjHDy6AQdr1uDZwrcdzngPz6iipvldk4qxnJGdJ6xpq6pFW7CMRRE7/evG2zKU4Y1HEhFli8fTpM08lOyvaeBVd6XJvthMWGG6p0u6+o8Du6oTxiFaxZ3V6Mgws+oThJ3ve2GF6k6ZWXwK1PMeFTxOpg0E4/kCWZA5h6Dgez1ggi7SWJen6WvwbwaHa606EOdH5l2veaGJrnmo7Ht0AYRED9BXIOb5u57BAdP9lD7lAXh6Tlgti9nCUUUa2AZucOpYZwsxL+VUWFHZiLfiZ6SOYc6IZ0wcwthnl7KO5S8AuPlIFhe7OGXSBRLI93QXEXdcs1fL6l5vkQTdn3YqJd36xNK1OGrI/DiqcEhfWw/1gUu+QzUnpA9fzYF9J36dKwG44Qx/4AlCdSfOC/baLhVS3Qn5dHlRB1pDNDv2JsMPy5tqt2lzLZZdiL76liagLLsXebvMW6mN4pEQpWHj2TECv18xqhjS72rOcDfupY1ddZGlUEvScLQU9g2i2ltr+hmMJvCZ9XrtzdX+lk5OfZL/B0PPzaI36UGXCiX8Wz3N2vXTDtR2Ooyz6xsYFixEYoA1gzihZIKkgqVLho0oozD08L1lfzLk30NGOW0irc/Z8k2eceTgah+erFsjhmCpXKSDFmKtxLsmKspILd2sRMH5ISWwWd+1klkUpkOdnj1Iv3zsyquPhJ/E+1MYlc5udaeLF3alGvTGlrfsSoFibVomBP0nxDs/2M+TRa7nXeUYyWeJzEIZQrCMbU9ppQnR/OMSLK6OLa6KJy46jcRMHwbKkqgZJA0XhST3vj6ub5Zvw2Aw8TAvZfZRmzJfxFtDO5EtzOXR0IxOAzF3dyKy2UpeYoKl1Vzvvcimg27ETJFV/XhdS81VPvfp5iNzI/DRP+2UvM7UUkbQSpzsfcHPLFHe/2bp7c98lyyzspri2Z0u/XbUbMd7K+nhknZQISvemK0OL+FJ89+ep8ImlCIPaouPpHutVilOAA9an/aY683Zei+uKlC4VXlqu5Z2ihXMuMZMTtl6HVXpc+nIvgLJ4EAaG6ovl9CBu5TlTfQF0fL4q1WOjrjf3di4Z+HW7ZSUiVgMmt9Di5TU5Xy5QNBw3/6HSq6tC0l1dWLwap7S+U+cVOPh56Xcql7sKPTu0f1TD8QVJwg69hkePD9NKAxSKjZV55fXId3J01IcI4eOWutkNfvG14fooSPqqGKezTBtmbA03R0PYIU8qXKU5y9Gfx7WHLiOgLxYbK9hz8hHteLf86/0GY2ag901i+73EIbeidwGvMCy2CrybsGgm10QUZycCgoPeQCFqc19SF/WJ6abSWkrvz3iqXZ7v0wDi6kKTTk5H6lrcXfFwcOBgG3ta14Wb+IrmmMT2eGjJRwHXPGCC01ASOP56LJ1W+g0oBjAXxdEiWy3vDYRlRqckv8oR9bihVIGqwzZFXcCZEqxrVRxwCq2o3vX5IoXuRENa0hiYQegmq1NDxKP9EztaufGCWuZJXZQ6RuJGeHg+5d/qjFlQ9S7e4mGnblrI39FKGvvTfTyVUDTakadg4z5E5OVVeEhItEYMmiU2borSU/LOrecsI17EniCPZ0XQliap8DSiSsZMp34krZMihmmTNZPb3g057PTKjlrY2hyM69AsuaDBftSOmF5066rcVZXm2xdGPaYaYFO51v1pP+aQdUx8MO1eTt5u1e0z6x+xKqOia8Q3xZwfd5Ec6Zd75CBLI+E8IWdqwS7otb1c26X1a9DlYv9sULxOSuggGRmqrCt08wi4pZcxp0MdkrbKUHYor7c1hC5s4ZxeamIzejVeLj3SXa9QA8j1PmWNhJTolrBjeSLuhXnqk6bN3d6WYYNHye2+Ui9eYEuc92UG7Y7kjLGCvyiDWrieMXpqdMlULrqST3P3A34rbqSy3nA0WFkSu/RbFJArXVobf5M9ko3xDT/TKnkCLXM74/SVNpBk7VHxGopyJ68q4ZixPRRJc65eL2bKColM+wdvRMazayspx8fgMsL1IG7GcQgMxT2OGbJbD/PVTBvh3aECEPLseiNiLBUoVyqgkR/ddJKyuRh223Zqo6F30DLQtcewTscrGPZfAHFAvymX4FTv4a00y/WYTs2VrGATsvMjZGUF9aieHnURCY/FoVNktDEEs/E2lLLntHsYiKu8MLiFgR4it3VwWpvscazNhJYMsyJVAuotNhrXU95Ry4S+6nK/3NcW/BcaFmfFpU4misCoWIVx1it9MpstvevcljwlXZpIaTYsS6Pqc5KZN7iv/WnAm/VGNwSKHkehs+5GUiqPdd9ILNF4994Kt0V0eLosBFHjWEWHLC8+zgR5fJliPQ6UEu5XT1nlZ4lMT4Jr3IlBkCVIUdFxTxSPu5mGealaEv4wKex1lzl4BdONWm0yHTpzGMNbckvgqEL49ObdS5dvCdhO3NNNyxFu8N29OuKF23KgjMZdQ+BAHUgZEW+rpD3c1rylYfeY3Owi4KaEQQ+6OF5vppOPQtOFo3HhAysMTQInnE0q09tdhfoNLcsdsM1Lh6m6ad1vS1nkcVS8HnsTE2fWEZGqzWHJ1alevun7GHi5JaNOz1IU5dnayWhOx5Wa7ZyWdh/W9XLszyi5LuWA7w8/R852wZ5665RDD8RKjZtQ3RPBpQcvmAR/bwMT4WK+MgW3s+EG8tVTMkrtKI33XDnpGsapiLeWRjNAlwIBTQueXkmjPy0Vje2mvD7qDtC7bGhsBF9pYjg3yoASZuysz3k/NaAjZy1i73PTV8LpcqrT3FYdjacvnTycw7TUuAtXNraSH+P2PKK1c7/fol3F+us+d+PWm9pK1Ar9eM+rz+l4h6+Zym6IHeeJmqwzewGkq3ROTLuUy2O/hIwnmmXoRWzd54FZdF4/9QVOsqsrVxF+bJObkMu5PrVDdurribpWZNum3nOWNdo4YTaDaXeK4OX80koTE56go1oKwWgi99EqB9VnLrPCXDus0FaALIHq3WVP9G196kiJ0XULmmxmy6aU5hxbx2FBqahL31ydGtNNl4GowEjc3oNrrPHvObG8nMfOx+cz89BUgWG4Pnb3uDnTjh44mJJDCbGoBu4IE28BxrNKpj1sfnkW0k263PejmesYc6l6wTf8xqL02WPSR8vv9sm7n/Dn3YE2qtamTgazt2VWQmUO5Ssus1tdT+nreskF3bAD2hJGKrv4Cy5oGdJSJ+I5P+ORY8hH0nohyma+Om2yTV9Fy0lEplpzdPbwolGpIL/fuQKqeWSRCdzVAvwlM4VzTFAlT0QAqCUFEb7mh5dXyQxBTnPNaK3b6zVMSTA3yFGwNVtU1lML6diE+dlpPpFKaqaCPkDGSUMv8RThmCmy6fOUz4QetDeB2sY0ghRLKrI9mjreRV49EXoDt1oPK71ecxFjU5vLFQLSAJ0kr3gp1aMORqmNN8ha0zvVwB4eoQpDzWa70krkHoM8E/rgpl4fFzVy78UgHvOptbxiF+aQEamLcOEQM4C2OynpsBk0+RnHXiy7DvummqOmuren2sbC+hTZAOGnMlo53Hh0bPNqIMcSTEtAFSLR6iYgtboN8eqZ4HHUxxh1VvJ7kzQSpkgQZ7rads2fmKMoMRVWpUMRK69aL6EWQHjxZF3mQRg29kHUDpmMLy9Fcx9p4KppY2VrDU6oueAlow9pW3C6wypfJEWSQSvMuugyd3X8BZDr+S4VSmO3y7EAqa94eeG7va9JaRUzqAiPqawsvqDMgZYvRL0qNNKCAWFvXjoZhItCCGx8ecxr76IaTPOFjJSSo1AccaUIOTj3azbpNJK0k2Y/SHKcmwFTs9sNkaLbUU60wVmmHTIzSImdcnv4DPbwHafi23K3nrqgOomCl5FvoMEVuWnDrlhd27WTSqAlcpNhx+7PdVRJd5ZSB8B6U9vaYc4en7eTTybhXTECpIw2DFZ5m0VPZW2UGIcFQzuhnloeOQS1YH1gk+C6TtWaNrhGKxh/zs/NCacsi7tDSg0/jCl+RbTPIS9U1vmVtq/U7jHe/QzB53E5UsZI6P5yR0v7ivfQ8FLNZLgM7VLFBTOEmyJccxkhVoFVXjB7JMeqvRkNaEXrvSzWIMoIkPRzhCXl3Wf6O/18aHFrMXdIHcbFBhxNP7M43PCbgFfsnKuiOKt0oEDWxFMP6wRyMDPZS6PdqubJuoY3e2f3JsSwhMiIfn1i1Y5WROfcUaNenlx02ggyn31GABCPBhj9CL3Ki9aB5x4L3nWgxfRmBEk1ra/49XEdYo+2/KayYdytR6qiKwvvXg92ua9kKz7RYTWelxAP67p1bpIYuuY6C54kMwN/VXmW0z2VYPvVpavLm715r5lqzDuO3eI7aiJNLL4qmzdEWS9wMcMIsU6OsmoMVMPX431SohFa5LbxV7fUNjgDc7nqlrLSpItKs1F4vjYcf7qZWCGXjGG+XHjDzlTAEhJDBLarRcx56KKhtLIA97x8AQ0TgjGkMI9eO5QZs0kY73GsyTS3+VEgslFTMKSGuBFbQj7dcS/TSeyM6sTjHGKnI681t3CsZKWShu0+7wocyfdxcxQ6sjx3ell8n2Xovd0NGRALLxDt5oHQ+62unBCVJhg0S3sOFVEqVs3u0EbapzieKF1UKFOecOIShFxMca+9c6BBHXMhS6E2KCudeALOEQEMuVClCyGn0lewCVJvhiUs2FBDnOoMoSSWTpLfkqu2iQKfuWvYRFXXL44Qwtwym616vSCwUXcMNG2C4cohqwZj4THzNjwIk9bUWzlE92h0r2BmnCgfw3pivFbXqNyXFOeRdud1eubsQjs+X+JFo+NzsJ9O7eKwdvc4tpXzsDmOHVYHjzM5uyqep5RnjOdPx4JaX/teLYvYKKPTu4+4ZqSZlG/LXg7PLn9uo/YKe1eWhtt8NB6xVxANbB5b1oQGZJip6izfieYay+FwraaWTqrgJVgP1l9s96bFxngXxd1JpEzxn77CBQJv57tQEfmZ8yl1e45QgcuYwFX77QLmRsMtMr3gxcUxw3VKqiPSTY5rqY/mCKhP4k0JTbu38Ryi0Im+JbVLJ3boprjCdqNfp3UH6X0tORmGr5UHn4ZVLzyuCuKUOxGJTYGCuVrjJm6zxmMVdCP2y0au1q0Ws9y5j+SeA9J2X+NYoN6TCvOQySDZ3GPgbTfOfOYpefeoI3W6bKfM6vrItJNz515T+eRlIWSxW/V6EJgaMVlx57pCDCaivquRiN7SV4TWXQ5oJzfyJRKdIT7dKS5bixG7U8slxnp7qci7mgz5nKnNSAXz6XHWkvXJPOUiCnoMAaBXSDAzq177SDDU6VRyoBh/93MozRrYr+DbmKr0ssCUMudX9HWWKR1D1M6b9N6wYSR8es/nUZbq1zTGglCu+JnYQR3zPKzOmhMHV4Bhgc67qd9pqewxSnbVeOFcUdgTN+Z54rfrk4BWQ6Poq8foYRtUCovbraDRJzt7lKeW8gUh0Jj2IRDnXu8QvI3rGz2srnp7AWb8VGIrIGmmt9NnoDiw6zWmPWMNf0+o5qIHl33LrQYyhyerN1XPTdXJS65FQjdTJG0KZOMoVQXo2SmSDgU0AKu4DLnNIFdNjENfZWXouusYxOQwJ6ZqFOV018ujqY9VLg9Wh62Dch9llAvO1SxCypNEzyIV19ARvT90GbngubTwcQZrd3afT6axUzV7bhIbUIb4qYChwcra9JY31QozZp5HGHWizGDW7aebjqYDuXIZqPtDXc7EcTpe8Sk8sQm3y66EZYOM8hHgrxe+XRG2YsnmoT9GPmoVwb0/UXx54HcUhjvP6s2hciNl2JO6gzmx9eHodXJbeCcIokvJa2DBAqalrxJWiadMdXx9dBbDzFL1rDtjRKBX4qIu6goQxe5nNF7Fu8dv3Qkb/RxWjsYLiSsdX9WMm/zTzdn1UyDmbBykhvjEFF7UEedsU73bJDDFW4nXSeIO0z56cwrMMq3hnK34i9daTD6qPovNJlLcKFcPi+PynAqOSHNf5p4O2ZsXjxKOI7VvqPpqEh7GPVjHcxFxxqcK6QqKQSwujtNMXgvYQAC9k2gZkiLhuime2WcNL02buQrmFQZUHOQNxQ7b0zCdue3TApqMau4fEHkyqHyKhGmpTSQGHPLmkugw+TCpcw5HmJIs9z70etAcFWlJpuaNXYIQmLj2JKa2pUM0K+DTmMJX4QExDPMfn3789H7F5usrGf+tt6M/Xir4/+uX67/8Hnz/BBp0cfp+5eH9xtrPH3f9/N9T5z9//DTGJVDmy+sDU7Pk337V/t+9PPD5N6mf31I///mFif3L68Z9N6fb/O2dlTnM3/9Hit95CGzVef4Pb2T84UWM90sTv39Z8q3nx5vwHy89nH5Cgbb//H8AXYGa8ZhDAAA= -->
