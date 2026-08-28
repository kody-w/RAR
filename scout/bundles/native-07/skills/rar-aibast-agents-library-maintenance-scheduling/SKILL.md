---
name: "rar-aibast-agents-library-maintenance-scheduling"
description: "Builds predictive maintenance schedules and work orders from a live simulated Dynamics 365 tenant, with an offline demo telemetry fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/maintenance_scheduling", "rar_sha256": "d6c819ed44648205ffc79f63a1c65f990f552fb45897638e2a59a259630358d2", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["maintenance", "predictive", "scheduling", "manufacturing", "IoT"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/maintenance_scheduling`. The original RAPP
agent is preserved byte-for-byte in `maintenance_scheduling_agent.py` and in the RCI capsule.

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

Maintenance Scheduling Agent — a template you are meant to mutate.

Manages predictive and preventive maintenance for manufacturing equipment.
Analyzes sensor telemetry, failure probability models, and technician
availability to generate optimized work-order schedules that minimize
unplanned downtime while controlling maintenance spend.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     The tenant's Field Service work orders and customer assets map onto
     this agent's world directly — e.g. work order "WO-260100" (printer
     fault at Cedar Hollow Printing, Break/Fix, unscheduled).
     Try: perform(operation="schedule_overview")
  2. No network? Everything falls back to the embedded demo layer below
     (EQUIPMENT / SENSOR_READINGS / TECHNICIANS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     MAINTENANCE_SCHEDULING_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your CMMS), or replace
     _fetch_collection() with a Maximo/Fiix client. Fields the rest of
     the file needs are listed in _normalize_live_work_order() — runtime
     hours and failure probabilities render as "n/a — enrichment seam"
     until you wire IoT telemetry.

OPERATIONS
  schedule_overview | predictive_alerts | work_order_plan
  | downtime_analysis | maintenance_plan | create_work_order
  | maintenance_calendar | fleet_optimization
  kwargs: operation (required), equipment_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "equipment_id": {
      "description": "Equipment identifier used to select maintenance planning and work-order records.",
      "type": "string"
    },
    "operation": {
      "description": "Operation to perform. Defaults to schedule_overview when omitted.",
      "enum": [
        "schedule_overview",
        "predictive_alerts",
        "work_order_plan",
        "downtime_analysis",
        "maintenance_plan",
        "create_work_order",
        "maintenance_calendar",
        "fleet_optimization"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `maintenance_scheduling_agent.py` and embedded as the fenced Python below (sha256 d6c819ed44648205…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `maintenance_scheduling_agent.py` first:

```bash
python3 maintenance_scheduling_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 maintenance_scheduling_agent.py   # or on stdin
python3 maintenance_scheduling_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintenance Scheduling Agent — a template you are meant to mutate.

Manages predictive and preventive maintenance for manufacturing equipment.
Analyzes sensor telemetry, failure probability models, and technician
availability to generate optimized work-order schedules that minimize
unplanned downtime while controlling maintenance spend.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     The tenant's Field Service work orders and customer assets map onto
     this agent's world directly — e.g. work order "WO-260100" (printer
     fault at Cedar Hollow Printing, Break/Fix, unscheduled).
     Try: perform(operation="schedule_overview")
  2. No network? Everything falls back to the embedded demo layer below
     (EQUIPMENT / SENSOR_READINGS / TECHNICIANS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     MAINTENANCE_SCHEDULING_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your CMMS), or replace
     _fetch_collection() with a Maximo/Fiix client. Fields the rest of
     the file needs are listed in _normalize_live_work_order() — runtime
     hours and failure probabilities render as "n/a — enrichment seam"
     until you wire IoT telemetry.

OPERATIONS
  schedule_overview | predictive_alerts | work_order_plan
  | downtime_analysis | maintenance_plan | create_work_order
  | maintenance_calendar | fleet_optimization
  kwargs: operation (required), equipment_id
"""

import sys
import os
import json
import urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/maintenance_scheduling",
    "version": "1.2.0",
    "display_name": "Maintenance Scheduling Agent",
    "description": "Builds predictive maintenance schedules and work orders from a live simulated Dynamics 365 tenant, with an offline demo telemetry fallback.",
    "author": "AIBAST",
    "tags": ["maintenance", "predictive", "scheduling", "manufacturing", "IoT"],
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
#   export MAINTENANCE_SCHEDULING_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CMMS client. Downstream
# code only needs the fields from _normalize_live_work_order().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "MAINTENANCE_SCHEDULING_DATA_URL",
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


_FMT = "@OData.Community.Display.V1.FormattedValue"


def _normalize_live_work_order(row):
    """Project a Dynamics Field Service work order onto the schedule row
    this agent renders. THIS is the contract your replacement data source
    must meet — a dict with these keys. None means 'not knowable from the
    work-order record alone' and the renderer labels it as an enrichment
    seam (wire IoT telemetry / failure models there)."""
    return {
        "id": row.get("msdyn_name", "?"),
        "asset": row.get("msdyn_customerassetname") or "n/a",
        "account": row.get("msdyn_serviceaccountname", "Unknown"),
        "issue": row.get("msdyn_primaryincidenttypename") or "n/a",
        "type": row.get("msdyn_workordertypename") or "n/a",
        "status": row.get("msdyn_systemstatus" + _FMT, "Unknown"),
        "priority": row.get("msdyn_priorityname") or "n/a",
        "runtime_hours": None,   # enrichment seam — wire IoT telemetry
        "failure_prob": None,    # enrichment seam — wire your failure model
        "_live": True,
    }


def _live_work_orders():
    """Open work orders from the live tenant; [] when offline."""
    rows = _fetch_collection("msdyn_workorders")
    return [
        _normalize_live_work_order(r) for r in rows
        if "Open" in str(r.get("msdyn_systemstatus" + _FMT, ""))
    ]


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

EQUIPMENT = {
    "EQ-CNC-01": {
        "name": "CNC Milling Center #1",
        "type": "CNC Mill",
        "install_date": "2019-03-14",
        "last_service": "2025-11-02",
        "runtime_hours": 18420,
        "mtbf_hours": 4200,
        "status": "running",
    },
    "EQ-CNC-02": {
        "name": "CNC Milling Center #2",
        "type": "CNC Mill",
        "install_date": "2021-07-22",
        "last_service": "2026-01-18",
        "runtime_hours": 9840,
        "mtbf_hours": 4200,
        "status": "running",
    },
    "EQ-PRS-01": {
        "name": "Hydraulic Press 400T",
        "type": "Press",
        "install_date": "2017-11-05",
        "last_service": "2025-09-30",
        "runtime_hours": 26100,
        "mtbf_hours": 5500,
        "status": "warning",
    },
    "EQ-WLD-01": {
        "name": "Robotic Welder Cell A",
        "type": "Welder",
        "install_date": "2022-01-10",
        "last_service": "2026-02-05",
        "runtime_hours": 7200,
        "mtbf_hours": 3800,
        "status": "running",
    },
    "EQ-INJ-01": {
        "name": "Injection Molder 220T",
        "type": "Injection Molder",
        "install_date": "2018-06-18",
        "last_service": "2025-08-12",
        "runtime_hours": 22800,
        "mtbf_hours": 4800,
        "status": "critical",
    },
    "EQ-ASM-01": {
        "name": "Assembly Line Conveyor",
        "type": "Conveyor",
        "install_date": "2020-04-01",
        "last_service": "2026-01-05",
        "runtime_hours": 14600,
        "mtbf_hours": 7000,
        "status": "running",
    },
}

SENSOR_READINGS = {
    "EQ-CNC-01": {"vibration_mm_s": 4.2, "temp_c": 62, "oil_pressure_bar": 48, "spindle_load_pct": 78},
    "EQ-CNC-02": {"vibration_mm_s": 2.1, "temp_c": 55, "oil_pressure_bar": 51, "spindle_load_pct": 64},
    "EQ-PRS-01": {"vibration_mm_s": 7.8, "temp_c": 74, "oil_pressure_bar": 38, "hydraulic_level_pct": 62},
    "EQ-WLD-01": {"vibration_mm_s": 1.9, "temp_c": 48, "arc_stability_pct": 96, "wire_feed_mpm": 8.4},
    "EQ-INJ-01": {"vibration_mm_s": 9.3, "temp_c": 88, "barrel_pressure_bar": 1420, "cycle_time_s": 34.7},
    "EQ-ASM-01": {"vibration_mm_s": 1.4, "temp_c": 38, "belt_tension_n": 620, "motor_current_a": 12.3},
}

FAILURE_PROBABILITIES = {
    "EQ-CNC-01": {"30_day": 0.12, "60_day": 0.28, "90_day": 0.41, "failure_mode": "Spindle bearing wear"},
    "EQ-CNC-02": {"30_day": 0.03, "60_day": 0.08, "90_day": 0.14, "failure_mode": "Normal wear"},
    "EQ-PRS-01": {"30_day": 0.35, "60_day": 0.58, "90_day": 0.74, "failure_mode": "Hydraulic seal degradation"},
    "EQ-WLD-01": {"30_day": 0.05, "60_day": 0.11, "90_day": 0.19, "failure_mode": "Wire feed mechanism"},
    "EQ-INJ-01": {"30_day": 0.62, "60_day": 0.84, "90_day": 0.93, "failure_mode": "Barrel heater band failure"},
    "EQ-ASM-01": {"30_day": 0.02, "60_day": 0.06, "90_day": 0.10, "failure_mode": "Belt splice fatigue"},
}

TECHNICIANS = {
    "TECH-201": {"name": "Marcus Rivera", "certifications": ["CNC Mill", "Press", "General"],
                  "shift": "Day", "available_hours_week": 40, "committed_hours": 24},
    "TECH-202": {"name": "Karen Oduya", "certifications": ["Welder", "Conveyor", "General"],
                  "shift": "Day", "available_hours_week": 40, "committed_hours": 16},
    "TECH-203": {"name": "James Whitfield", "certifications": ["Injection Molder", "Press", "CNC Mill"],
                  "shift": "Night", "available_hours_week": 40, "committed_hours": 30},
    "TECH-204": {"name": "Lin Zhao", "certifications": ["CNC Mill", "Welder", "Injection Molder", "General"],
                  "shift": "Day", "available_hours_week": 40, "committed_hours": 20},
}

MAINTENANCE_HISTORY = [
    {"eq_id": "EQ-INJ-01", "date": "2025-08-12", "type": "Preventive", "hours": 6, "cost": 2400.00,
     "notes": "Replaced heater bands 3 and 4, calibrated barrel sensors"},
    {"eq_id": "EQ-PRS-01", "date": "2025-09-30", "type": "Corrective", "hours": 12, "cost": 8750.00,
     "notes": "Emergency hydraulic seal replacement, fluid flush"},
    {"eq_id": "EQ-CNC-01", "date": "2025-11-02", "type": "Preventive", "hours": 4, "cost": 1200.00,
     "notes": "Spindle bearing inspection, oil change, alignment check"},
    {"eq_id": "EQ-ASM-01", "date": "2026-01-05", "type": "Preventive", "hours": 3, "cost": 650.00,
     "notes": "Belt tension adjustment, roller lubrication"},
    {"eq_id": "EQ-CNC-02", "date": "2026-01-18", "type": "Preventive", "hours": 4, "cost": 1100.00,
     "notes": "Tool holder inspection, coolant system flush"},
    {"eq_id": "EQ-WLD-01", "date": "2026-02-05", "type": "Preventive", "hours": 5, "cost": 1800.00,
     "notes": "Wire feed calibration, torch tip replacement, gas flow test"},
]

DOWNTIME_COST_PER_HOUR = {
    "CNC Mill": 850, "Press": 1200, "Welder": 600,
    "Injection Molder": 1400, "Conveyor": 2200,
}

MAINTENANCE_PLAN_RECORDS = {
    "EQ-INJ-01": {
        "production_order": "ORD-7813", "delivery_priority": "critical",
        "window": "2026-03-21 22:00-2026-03-22 06:00", "capacity_impact_pct": 4.0,
        "parts": ["Heater band HB-220 x2", "Thermocouple TC-K x1"],
        "crew": ["James Whitfield", "Lin Zhao"], "backup_equipment": "EQ-INJ-02",
        "backup_status": "available", "estimated_hours": 8,
    },
    "EQ-PRS-01": {
        "production_order": "ORD-7810", "delivery_priority": "high",
        "window": "2026-03-28 06:00-11:00", "capacity_impact_pct": 6.5,
        "parts": ["Hydraulic seal kit HS-400 x1", "ISO 46 fluid x40L"],
        "crew": ["Marcus Rivera"], "backup_equipment": "EQ-PRS-02",
        "backup_status": "available at 80% capacity", "estimated_hours": 5,
    },
    "EQ-CNC-01": {
        "production_order": "ORD-7811", "delivery_priority": "standard",
        "window": "2026-04-04 14:00-17:00", "capacity_impact_pct": 2.0,
        "parts": ["Spindle bearing kit SB-42 x1"],
        "crew": ["Marcus Rivera"], "backup_equipment": "EQ-CNC-02",
        "backup_status": "available", "estimated_hours": 3,
    },
}

EVIDENCE_MARKER = (
    "[Evidence: maintenance-scheduling one-pager and demo transcript; "
    "production-aware windows, parts/crew staging, work-order execution, and calendar]"
)


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _risk_priority(eq_id):
    """Return a 0-100 risk score combining failure probability and sensor anomalies."""
    fp = FAILURE_PROBABILITIES[eq_id]["30_day"]
    sensor = SENSOR_READINGS[eq_id]
    vib_score = min(sensor.get("vibration_mm_s", 0) / 10.0, 1.0)
    temp_score = min(sensor.get("temp_c", 20) / 100.0, 1.0)
    return round((fp * 60 + vib_score * 25 + temp_score * 15) * 100 / 100, 1)


def _best_technician(eq_type):
    """Find the best-fit available technician for an equipment type."""
    candidates = []
    for tid, tech in TECHNICIANS.items():
        if eq_type in tech["certifications"] or "General" in tech["certifications"]:
            free = tech["available_hours_week"] - tech["committed_hours"]
            if free > 0:
                candidates.append((tid, tech, free))
    candidates.sort(key=lambda x: x[2], reverse=True)
    return candidates[0] if candidates else None


def _estimated_downtime_cost(eq_id, hours):
    """Calculate cost of downtime for given equipment and hours."""
    eq_type = EQUIPMENT[eq_id]["type"]
    return hours * DOWNTIME_COST_PER_HOUR.get(eq_type, 500)


def _work_order_hours(failure_prob_30):
    """Estimate work-order hours from 30-day failure probability."""
    if failure_prob_30 >= 0.50:
        return 8
    elif failure_prob_30 >= 0.25:
        return 5
    elif failure_prob_30 >= 0.10:
        return 3
    return 2


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class MaintenanceSchedulingAgent(BasicAgent):
    """Predictive maintenance scheduling for manufacturing equipment."""

    def __init__(self):
        self.name = "MaintenanceSchedulingAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "operations": [
                "schedule_overview",
                "predictive_alerts",
                "work_order_plan",
                "downtime_analysis",
                "maintenance_plan",
                "create_work_order",
                "maintenance_calendar",
                "fleet_optimization",
            ],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "description": "Operation to perform. Defaults to schedule_overview when omitted.",
                        "enum": [
                            "schedule_overview",
                            "predictive_alerts",
                            "work_order_plan",
                            "downtime_analysis",
                            "maintenance_plan",
                            "create_work_order",
                            "maintenance_calendar",
                            "fleet_optimization",
                        ],
                    },
                    "equipment_id": {
                        "type": "string",
                        "description": "Equipment identifier used to select maintenance planning and work-order records.",
                    },
                },
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "schedule_overview")
        dispatch = {
            "schedule_overview": self._schedule_overview,
            "predictive_alerts": self._predictive_alerts,
            "work_order_plan": self._work_order_plan,
            "downtime_analysis": self._downtime_analysis,
            "maintenance_plan": self._maintenance_plan,
            "create_work_order": self._create_work_order,
            "maintenance_calendar": self._maintenance_calendar,
            "fleet_optimization": self._fleet_optimization,
        }
        handler = dispatch.get(operation)
        if handler is None:
            return f"**Error:** Unknown operation `{operation}`. Valid: {', '.join(dispatch.keys())}"
        return handler(**kwargs)

    # ------------------------------------------------------------------
    def _schedule_overview(self, **kwargs) -> str:
        lines = ["## Maintenance Schedule Overview\n"]
        lines.append("### Equipment Status\n")
        lines.append("| ID | Equipment | Type | Status | Runtime (hrs) | Last Service | Risk Score |")
        lines.append("|----|-----------|------|--------|---------------|--------------|------------|")
        for eq_id, eq in EQUIPMENT.items():
            risk = _risk_priority(eq_id)
            status_label = {"running": "OK", "warning": "WARN", "critical": "CRIT"}.get(eq["status"], eq["status"])
            lines.append(
                f"| {eq_id} | {eq['name']} | {eq['type']} | **{status_label}** | "
                f"{eq['runtime_hours']:,} | {eq['last_service']} | {risk} |"
            )

        lines.append("\n### Technician Availability\n")
        lines.append("| Technician | Shift | Certifications | Avail Hrs/Wk | Committed | Free |")
        lines.append("|------------|-------|----------------|-------------|-----------|------|")
        for tid, tech in TECHNICIANS.items():
            free = tech["available_hours_week"] - tech["committed_hours"]
            certs = ", ".join(tech["certifications"])
            lines.append(
                f"| {tech['name']} | {tech['shift']} | {certs} | "
                f"{tech['available_hours_week']} | {tech['committed_hours']} | {free} |"
            )

        lines.append("\n### Recent Maintenance History\n")
        lines.append("| Date | Equipment | Type | Hours | Cost |")
        lines.append("|------|-----------|------|-------|------|")
        for rec in MAINTENANCE_HISTORY[-5:]:
            eq_name = EQUIPMENT.get(rec["eq_id"], {}).get("name", rec["eq_id"])
            lines.append(
                f"| {rec['date']} | {eq_name} | {rec['type']} | {rec['hours']} | ${rec['cost']:,.2f} |"
            )
        live = _live_work_orders()
        if live:
            seam = "n/a — enrichment seam"
            lines.append("\n### Live Tenant Open Work Orders (Dynamics Field Service)\n")
            lines.append("| WO | Asset | Account | Issue | Type | Status | Priority | Runtime (hrs) |")
            lines.append("|----|-------|---------|-------|------|--------|----------|---------------|")
            for w in live:
                runtime = seam if w["runtime_hours"] is None else f"{w['runtime_hours']:,}"
                lines.append(
                    f"| {w['id']} | {w['asset']} | {w['account']} | {w['issue']} | "
                    f"{w['type']} | {w['status']} | {w['priority']} | {runtime} |"
                )
        else:
            lines.append("\n_Live tenant unreachable — showing embedded demo equipment only._")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _predictive_alerts(self, **kwargs) -> str:
        lines = ["## Predictive Maintenance Alerts\n"]
        alerts = []
        for eq_id in EQUIPMENT:
            fp = FAILURE_PROBABILITIES[eq_id]
            risk = _risk_priority(eq_id)
            if fp["30_day"] >= 0.10:
                severity = "CRITICAL" if fp["30_day"] >= 0.50 else "WARNING" if fp["30_day"] >= 0.25 else "WATCH"
                alerts.append((severity, eq_id, fp, risk))
        alerts.sort(key=lambda x: x[3], reverse=True)

        if not alerts:
            lines.append("No predictive alerts at this time. All equipment within normal parameters.")
            return "\n".join(lines)

        for severity, eq_id, fp, risk in alerts:
            eq = EQUIPMENT[eq_id]
            sensor = SENSOR_READINGS[eq_id]
            lines.append(f"### [{severity}] {eq['name']} ({eq_id})")
            lines.append(f"- **Failure mode:** {fp['failure_mode']}")
            lines.append(f"- **30-day failure probability:** {fp['30_day']*100:.0f}%")
            lines.append(f"- **60-day failure probability:** {fp['60_day']*100:.0f}%")
            lines.append(f"- **90-day failure probability:** {fp['90_day']*100:.0f}%")
            lines.append(f"- **Risk score:** {risk}/100")
            lines.append("- **Current sensor readings:**")
            for k, v in sensor.items():
                lines.append(f"  - {k}: {v}")
            lines.append("")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _work_order_plan(self, **kwargs) -> str:
        lines = ["## Work Order Plan\n"]
        lines.append("Priority-ranked work orders for the next 30 days:\n")
        lines.append("| Priority | Equipment | Work Description | Est Hours | Assigned Tech | Shift |")
        lines.append("|----------|-----------|------------------|-----------|---------------|-------|")

        ranked = sorted(EQUIPMENT.keys(), key=lambda e: _risk_priority(e), reverse=True)
        priority = 0
        total_hours = 0
        for eq_id in ranked:
            fp = FAILURE_PROBABILITIES[eq_id]
            if fp["30_day"] < 0.10:
                continue
            priority += 1
            eq = EQUIPMENT[eq_id]
            tech_match = _best_technician(eq["type"])
            tech_name = tech_match[1]["name"] if tech_match else "UNASSIGNED"
            shift = tech_match[1]["shift"] if tech_match else "-"
            est_hours = _work_order_hours(fp["30_day"])
            total_hours += est_hours
            lines.append(
                f"| P{priority} | {eq['name']} | {fp['failure_mode']} -- preventive service | "
                f"{est_hours} | {tech_name} | {shift} |"
            )

        lines.append(f"\n**Total work orders:** {priority}")
        lines.append(f"**Total estimated labor hours:** {total_hours}")
        lines.append("\n**Scheduling notes:**")
        lines.append("- P1 work orders should be completed within 7 days")
        lines.append("- P2 work orders within 14 days")
        lines.append("- P3+ within 30 days")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _downtime_analysis(self, **kwargs) -> str:
        lines = ["## Downtime & Cost Analysis\n"]
        lines.append("### Unplanned Downtime Risk (Next 90 Days)\n")
        lines.append("| Equipment | 30-Day P(Fail) | Est Downtime (hrs) | Downtime Cost | Prevention Cost | Net Savings |")
        lines.append("|-----------|----------------|--------------------|--------------:|----------------:|------------:|")
        total_dt_cost = 0.0
        total_prev_cost = 0.0
        for eq_id, eq in EQUIPMENT.items():
            fp = FAILURE_PROBABILITIES[eq_id]
            p = fp["30_day"]
            if p < 0.10:
                continue
            dt_hrs = round(p * 24, 1)
            dt_cost = _estimated_downtime_cost(eq_id, dt_hrs)
            prev_cost = round(dt_cost * 0.25, 2)
            savings = round(dt_cost - prev_cost, 2)
            total_dt_cost += dt_cost
            total_prev_cost += prev_cost
            lines.append(
                f"| {eq['name']} | {p*100:.0f}% | {dt_hrs} | "
                f"${dt_cost:,.2f} | ${prev_cost:,.2f} | ${savings:,.2f} |"
            )

        lines.append(f"\n**Total downtime cost exposure:** ${total_dt_cost:,.2f}")
        lines.append(f"**Total preventive maintenance cost:** ${total_prev_cost:,.2f}")
        lines.append(f"**Net savings from preventive action:** ${total_dt_cost - total_prev_cost:,.2f}")

        lines.append("\n### Historical Maintenance Spend\n")
        total_hist = sum(r["cost"] for r in MAINTENANCE_HISTORY)
        prev_count = sum(1 for r in MAINTENANCE_HISTORY if r["type"] == "Preventive")
        corr_count = sum(1 for r in MAINTENANCE_HISTORY if r["type"] == "Corrective")
        lines.append(f"- Total spend (last 12 months): **${total_hist:,.2f}**")
        lines.append(f"- Preventive work orders: **{prev_count}**")
        lines.append(f"- Corrective (unplanned) work orders: **{corr_count}**")
        lines.append(f"- Preventive-to-corrective ratio: **{prev_count}:{corr_count}** (target 5:1)")
        return "\n".join(lines)

    def _maintenance_record(self, **kwargs):
        equipment_id = str(kwargs.get("equipment_id", "EQ-INJ-01")).strip().upper()
        record = MAINTENANCE_PLAN_RECORDS.get(equipment_id)
        if record is None:
            valid = ", ".join(MAINTENANCE_PLAN_RECORDS)
            return equipment_id, None, f"**Error:** Unknown equipment `{equipment_id}`. Valid: {valid}"
        return equipment_id, record, ""

    def _maintenance_plan(self, **kwargs) -> str:
        equipment_id, plan, error = self._maintenance_record(**kwargs)
        if error:
            return error
        eq = EQUIPMENT[equipment_id]
        fp = FAILURE_PROBABILITIES[equipment_id]
        return "\n".join([
            "## Production-Aware Maintenance Plan",
            EVIDENCE_MARKER,
            f"**Equipment lookup:** {equipment_id} — {eq['name']}",
            f"- Related production order: {plan['production_order']} ({plan['delivery_priority']} priority)",
            f"- 30-day failure probability: {fp['30_day'] * 100:.0f}% ({fp['failure_mode']})",
            f"- Lowest-impact window: {plan['window']}",
            f"- Modeled capacity impact: {plan['capacity_impact_pct']}%",
            f"- Parts confirmed: {', '.join(plan['parts'])}",
            f"- Crew confirmed: {', '.join(plan['crew'])}",
            f"- Backup: {plan['backup_equipment']} — {plan['backup_status']}",
            f"- Estimated duration: {plan['estimated_hours']} hours",
        ])

    def _create_work_order(self, **kwargs) -> str:
        equipment_id, plan, error = self._maintenance_record(**kwargs)
        if error:
            return error
        receipt = f"WO-SIM-{equipment_id.replace('EQ-', '')}-202603"
        return "\n".join([
            "## Simulated Work-Order Execution",
            EVIDENCE_MARKER,
            f"**Equipment lookup:** {equipment_id} — {EQUIPMENT[equipment_id]['name']}",
            f"- **SIMULATED WRITE RECEIPT:** `{receipt}`",
            f"- Dynamics 365 work order window: {plan['window']}",
            f"- Teams crew assignment: {', '.join(plan['crew'])}",
            f"- Reserved parts: {', '.join(plan['parts'])}",
            f"- Backup equipment validated: {plan['backup_equipment']} ({plan['backup_status']})",
            "- Simulation only; no work order, inventory, calendar, or Teams message was created.",
        ])

    def _maintenance_calendar(self, **kwargs) -> str:
        lines = ["## 30-Day Maintenance Calendar", EVIDENCE_MARKER, "",
                 "| Equipment | Window | Production Order | Capacity Impact | Crew |",
                 "|-----------|--------|------------------|-----------------|------|"]
        for equipment_id, plan in MAINTENANCE_PLAN_RECORDS.items():
            lines.append(
                f"| {equipment_id} | {plan['window']} | {plan['production_order']} | "
                f"{plan['capacity_impact_pct']}% | {', '.join(plan['crew'])} |"
            )
        lines.append("\nAll windows are deterministic planning records; no external calendars were changed.")
        return "\n".join(lines)

    def _fleet_optimization(self, **kwargs) -> str:
        ranked = sorted(
            EQUIPMENT, key=lambda equipment_id: _risk_priority(equipment_id), reverse=True
        )
        lines = ["## Long-Term Fleet Maintenance Optimization", EVIDENCE_MARKER, "",
                 "| Rank | Equipment | Risk | 90-Day Failure Probability | Action |",
                 "|------|-----------|------|----------------------------|--------|"]
        for rank, equipment_id in enumerate(ranked, 1):
            risk = _risk_priority(equipment_id)
            probability = FAILURE_PROBABILITIES[equipment_id]["90_day"] * 100
            action = "planned overhaul" if probability >= 70 else "condition monitor" if probability >= 30 else "routine PM"
            lines.append(
                f"| {rank} | {equipment_id} | {risk} | {probability:.0f}% | {action} |"
            )
        lines.append("\n**Optimization KPIs:** unplanned downtime, schedule adherence, "
                     "emergency repair spend, and preventive-to-corrective ratio.")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = MaintenanceSchedulingAgent()
    print("=" * 72)
    print("EMBEDDED DEMO FLEET + LIVE TENANT WORK ORDERS")
    print("(live section fetched over HTTP; falls back offline)")
    print("=" * 72)
    print(agent.perform(operation="schedule_overview"))
    print()
    for op in agent.metadata["operations"][1:]:
        print("=" * 72)
        print(agent.perform(operation=op))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
