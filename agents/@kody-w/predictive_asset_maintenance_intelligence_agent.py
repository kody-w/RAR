"""Predictive Asset Maintenance Intelligence — single-file RAPP agent stack.

Energy Utilities. One portable file that bundles an entire predictive
maintenance pipeline for critical grid infrastructure. Drop this one file into
any RAPP brainstem `agents/` directory and the LLM gains eight specialist
agents PLUS a top-level orchestrator that runs the whole pipeline end to end.

The eight specialists (the LLM can compose them; no orchestrator required):

  1. AssetSensorAggregatorAgent    — normalize IoT/SCADA telemetry per asset
  2. AssetHealthScorerAgent        — anomaly + health score, condition band, RUL
  3. FailureProbabilityRankerAgent — rank fleet by p(fail) over 30/90/180 days
  4. MaintenanceWorkOrderAgent     — draft D365 Field Service work orders
  5. PartsPlannerAgent             — consolidate parts, flag long-lead, PR triggers
  6. FieldExecutionCaptureAgent    — capture Power Apps mobile closeout
  7. AssetRegisterWritebackAgent   — stage AMS + ERP fixed-asset register updates
  8. LifecycleCapexPlannerAgent    — multi-year capex replacement pipeline

Plus:

  *. PredictiveAssetMaintenanceIntelligenceAgent — runs 1->2->3 then fans out to
     work-order/parts drafting and the capex pipeline in a single call.

    sensors -> [1 aggregator] -> [2 scorer] -> [3 ranker] -+-> [4 WO] -> [5 parts]
                                                           |     |
                                                           |     +-> [6 capture] -> [7 register]
                                                           +-> [8 capex planner]

No PII. Synthetic, domain-shaped outputs. Deterministic where it matters
(per-asset telemetry is seeded so demos and code reviews are reproducible).
Every perform() returns a JSON string per the RAR single-file contract.
"""

import os
import json
import math
import random
import hashlib
from datetime import datetime, timedelta

# ═══════════════════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by the RAR registry builder.
# ═══════════════════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/predictive_asset_maintenance_intelligence",
    "version": "1.0.0",
    "display_name": "Predictive Asset Maintenance Intelligence",
    "description": (
        "End-to-end predictive maintenance for grid infrastructure: aggregates "
        "telemetry, scores asset health, ranks failure probability over "
        "30/90/180 days, drafts Field Service work orders and parts procurement, "
        "and builds a multi-year capex replacement pipeline — eight specialist "
        "agents plus an orchestrator in one file."
    ),
    "author": "Kody Wildfeuer",
    "tags": [
        "energy",
        "predictive-maintenance",
        "asset-management",
        "grid",
        "field-service",
    ],
    "category": "energy",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════════════════


# ── Portable BasicAgent import ───────────────────────────────────────────────
# Works inside a RAPP brainstem (agents.basic_agent / basic_agent shims) and
# standalone (inline fallback) so this file is shareable with zero setup.
try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    try:
        from basic_agent import BasicAgent
    except ModuleNotFoundError:
        class BasicAgent:
            """Minimal inline fallback base. The brainstem's real BasicAgent
            supersedes this when present; discovery ignores classes named
            'BasicAgent', so this is never registered as an agent itself."""

            def __init__(self, name=None, metadata=None):
                if name is not None:
                    self.name = name
                elif not hasattr(self, "name"):
                    self.name = "BasicAgent"
                if metadata is not None:
                    self.metadata = metadata
                elif not hasattr(self, "metadata"):
                    self.metadata = {
                        "name": self.name,
                        "description": "Base agent -- override this.",
                        "parameters": {"type": "object", "properties": {}, "required": []},
                    }

            def perform(self, **kwargs):
                return "Not implemented."

            def system_context(self):
                return None

            def to_tool(self):
                return {
                    "type": "function",
                    "function": {
                        "name": self.name,
                        "description": self.metadata.get("description", ""),
                        "parameters": self.metadata.get(
                            "parameters", {"type": "object", "properties": {}}
                        ),
                    },
                }


def _ok(agent, message, data):
    return {"status": "success", "agent": agent, "message": message, "data": data}


# ═════════════════════════════════════════════════════════════════════════════
# 1. Asset Sensor Aggregator
#    Pulls and normalizes IoT/SCADA telemetry across grid assets (transformers,
#    switchgear, cables, overhead lines). Produces a time-aligned health snapshot
#    per asset so downstream agents can score, rank and act.
# ═════════════════════════════════════════════════════════════════════════════

ASSET_CLASSES = ["transformer", "switchgear", "underground_cable", "overhead_line"]


def _stable_seed(*parts) -> int:
    h = hashlib.sha256("|".join(str(p) for p in parts).encode()).hexdigest()
    return int(h[:8], 16)


def _synth_asset(asset_id, asset_class=None):
    rng = random.Random(_stable_seed(asset_id))
    asset_class = asset_class or rng.choice(ASSET_CLASSES)
    age_years = rng.randint(3, 42)

    base = {
        "transformer": {"temp_c": rng.uniform(55, 95), "load_pct": rng.uniform(40, 110),
                        "oil_dga_ppm": rng.uniform(20, 800), "partial_discharge_pc": rng.uniform(5, 1200)},
        "switchgear": {"temp_c": rng.uniform(25, 70), "load_pct": rng.uniform(30, 95),
                       "operations_count": rng.randint(50, 4000), "sf6_ppm": rng.uniform(0.1, 8.0)},
        "underground_cable": {"temp_c": rng.uniform(20, 65), "load_pct": rng.uniform(35, 105),
                              "moisture_index": rng.uniform(0.05, 0.85), "partial_discharge_pc": rng.uniform(3, 950)},
        "overhead_line": {"temp_c": rng.uniform(15, 55), "load_pct": rng.uniform(25, 90),
                          "sag_cm": rng.uniform(10, 220), "vegetation_clearance_m": rng.uniform(0.4, 6.5)},
    }[asset_class]

    return {
        "asset_id": asset_id,
        "asset_class": asset_class,
        "age_years": age_years,
        "substation": f"SUB-{rng.randint(1, 99):02d}",
        "voltage_kv": rng.choice([11, 22, 33, 66, 132, 230, 345]),
        "telemetry": base,
        "last_sample_utc": (datetime.utcnow() - timedelta(minutes=rng.randint(0, 14))).isoformat() + "Z",
        "sensor_health": "ok" if rng.random() > 0.06 else "intermittent",
    }


class AssetSensorAggregatorAgent(BasicAgent):
    def __init__(self):
        self.name = "AssetSensorAggregatorAgent"
        self.metadata = {
            "name": self.name,
            "description": (
                "Aggregates and normalizes IoT/SCADA telemetry across grid assets "
                "(transformers, switchgear, cables, overhead lines). Returns a "
                "time-aligned health snapshot per asset."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "asset_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional list of asset IDs to aggregate. If omitted, returns a synthetic fleet sample.",
                    },
                    "asset_class": {
                        "type": "string",
                        "enum": ASSET_CLASSES,
                        "description": "Filter to a single asset class.",
                    },
                    "substation": {
                        "type": "string",
                        "description": "Filter to a single substation (e.g. SUB-44).",
                    },
                    "sample_size": {
                        "type": "integer",
                        "description": "When asset_ids is omitted, number of synthetic assets to return.",
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _run(self, **kwargs):
        asset_ids = kwargs.get("asset_ids") or []
        asset_class = kwargs.get("asset_class")
        substation = kwargs.get("substation")
        sample_size = int(kwargs.get("sample_size") or 25)

        if not asset_ids:
            asset_ids = [f"AST-{i:05d}" for i in range(1, sample_size + 1)]

        snapshots = [_synth_asset(aid, asset_class) for aid in asset_ids]
        if substation:
            snapshots = [s for s in snapshots if s["substation"] == substation]

        return _ok(self.name, f"Aggregated telemetry for {len(snapshots)} asset(s).", {
            "as_of_utc": datetime.utcnow().isoformat() + "Z",
            "sources": ["Azure IoT Hub", "SCADA Historian", "Asset Management System"],
            "asset_count": len(snapshots),
            "snapshots": snapshots,
        })

    def perform(self, **kwargs):
        return json.dumps(self._run(**kwargs))


# ═════════════════════════════════════════════════════════════════════════════
# 2. Asset Health Scorer
#    Anomaly score, health score, condition band, Remaining Useful Life (RUL).
#    Heuristics are domain-shaped — not real ML, but realistic-shaped.
# ═════════════════════════════════════════════════════════════════════════════

def _norm(x, lo, hi):
    if hi <= lo:
        return 0.0
    return max(0.0, min(1.0, (x - lo) / (hi - lo)))


def _score_snapshot(snap):
    klass = snap.get("asset_class")
    t = snap.get("telemetry") or {}
    age = snap.get("age_years", 10)
    age_factor = _norm(age, 0, 50)  # older = worse

    if klass == "transformer":
        stress = max(
            _norm(t.get("temp_c", 60), 50, 110),
            _norm(t.get("load_pct", 50), 60, 130),
            _norm(t.get("oil_dga_ppm", 100), 50, 1000),
            _norm(t.get("partial_discharge_pc", 50), 100, 1500),
        )
    elif klass == "switchgear":
        stress = max(
            _norm(t.get("temp_c", 30), 30, 80),
            _norm(t.get("load_pct", 50), 60, 110),
            _norm(t.get("operations_count", 500), 1000, 5000),
            _norm(t.get("sf6_ppm", 1), 1, 10),
        )
    elif klass == "underground_cable":
        stress = max(
            _norm(t.get("temp_c", 30), 30, 70),
            _norm(t.get("load_pct", 50), 60, 120),
            _norm(t.get("moisture_index", 0.2), 0.2, 1.0),
            _norm(t.get("partial_discharge_pc", 50), 80, 1200),
        )
    else:  # overhead_line
        stress = max(
            _norm(t.get("temp_c", 25), 20, 60),
            _norm(t.get("load_pct", 50), 50, 100),
            _norm(t.get("sag_cm", 60), 80, 250),
            1.0 - _norm(t.get("vegetation_clearance_m", 3.0), 0.5, 5.0),
        )

    anomaly = round(min(1.0, 0.65 * stress + 0.35 * age_factor), 3)
    health = int(round(100 * (1 - anomaly)))

    # Plausible RUL curve: a healthy asset gets years; a stressed one collapses fast.
    rul_days = max(7, int(round(3650 * math.exp(-2.6 * anomaly))))

    if anomaly < 0.30:
        band = "Healthy"
    elif anomaly < 0.55:
        band = "Watch"
    elif anomaly < 0.78:
        band = "Degraded"
    else:
        band = "Critical"

    return {
        "asset_id": snap.get("asset_id"),
        "asset_class": klass,
        "substation": snap.get("substation"),
        "age_years": snap.get("age_years"),
        "anomaly_score": anomaly,
        "health_score": health,
        "rul_days": rul_days,
        "condition_band": band,
        "key_drivers": _drivers(klass, t),
    }


def _drivers(klass, t):
    drivers = []
    if klass == "transformer":
        if t.get("oil_dga_ppm", 0) > 400:
            drivers.append("Elevated DGA")
        if t.get("temp_c", 0) > 85:
            drivers.append("High oil temp")
        if t.get("load_pct", 0) > 95:
            drivers.append("Sustained overload")
        if t.get("partial_discharge_pc", 0) > 600:
            drivers.append("Partial discharge activity")
    elif klass == "switchgear":
        if t.get("sf6_ppm", 0) > 4:
            drivers.append("SF6 leak signal")
        if t.get("operations_count", 0) > 2500:
            drivers.append("High operations count")
        if t.get("temp_c", 0) > 55:
            drivers.append("Hotspot trend")
    elif klass == "underground_cable":
        if t.get("moisture_index", 0) > 0.5:
            drivers.append("Moisture ingress")
        if t.get("partial_discharge_pc", 0) > 500:
            drivers.append("Insulation degradation")
        if t.get("load_pct", 0) > 90:
            drivers.append("Thermal cycling")
    else:
        if t.get("sag_cm", 0) > 180:
            drivers.append("Excessive sag")
        if t.get("vegetation_clearance_m", 5) < 1.5:
            drivers.append("Vegetation encroachment")
        if t.get("temp_c", 0) > 50:
            drivers.append("Conductor heating")
    return drivers or ["Normal operating envelope"]


class AssetHealthScorerAgent(BasicAgent):
    def __init__(self):
        self.name = "AssetHealthScorerAgent"
        self.metadata = {
            "name": self.name,
            "description": (
                "Computes anomaly score, health score, condition band and "
                "Remaining Useful Life (RUL) for each asset from normalized "
                "telemetry snapshots."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "snapshots": {
                        "type": "array",
                        "description": "Array of asset snapshots from AssetSensorAggregatorAgent.",
                    },
                },
                "required": ["snapshots"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _run(self, **kwargs):
        snapshots = kwargs.get("snapshots")
        if not snapshots or not isinstance(snapshots, list):
            return {
                "status": "needs_input",
                "agent": self.name,
                "message": "Provide `snapshots` (list) from AssetSensorAggregatorAgent. No data will be fabricated.",
            }
        scored = [_score_snapshot(s) for s in snapshots]
        band_counts = {b: 0 for b in ("Healthy", "Watch", "Degraded", "Critical")}
        for s in scored:
            band_counts[s["condition_band"]] += 1
        return _ok(self.name, f"Scored {len(scored)} asset(s).", {
            "as_of_utc": datetime.utcnow().isoformat() + "Z",
            "model": "rule-based-v1 (heuristic, domain-shaped)",
            "summary": band_counts,
            "scored": scored,
        })

    def perform(self, **kwargs):
        return json.dumps(self._run(**kwargs))


# ═════════════════════════════════════════════════════════════════════════════
# 3. Failure Probability Ranker
#    Failure probability across 30/90/180-day horizons, ranked. Deterministic
#    for a given input snapshot. p(180) >= p(90) >= p(30) always.
# ═════════════════════════════════════════════════════════════════════════════

def _prob(anomaly, horizon_days):
    # Exponential survival model. Hazard rate grows quadratically with anomaly,
    # so a healthy asset stays low even on a 180-day horizon, while a critical
    # one spikes fast — and p(180) >= p(90) >= p(30) always.
    hazard_per_day = 0.0008 + (max(0.0, min(1.0, anomaly)) ** 2) * 0.015
    p = 1.0 - math.exp(-hazard_per_day * horizon_days)
    return round(p, 4)


class FailureProbabilityRankerAgent(BasicAgent):
    def __init__(self):
        self.name = "FailureProbabilityRankerAgent"
        self.metadata = {
            "name": self.name,
            "description": (
                "Ranks assets by failure probability across 30 / 90 / 180-day "
                "horizons using the anomaly scores produced by AssetHealthScorerAgent."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "scored": {
                        "type": "array",
                        "description": "Array of scored assets from AssetHealthScorerAgent.data.scored.",
                    },
                    "horizon_days": {
                        "type": "integer",
                        "enum": [30, 90, 180],
                        "description": "Horizon to sort by. Defaults to 90.",
                    },
                    "top_n": {
                        "type": "integer",
                        "description": "Return only the top N highest-risk assets. Defaults to 25.",
                    },
                    "min_probability": {
                        "type": "number",
                        "description": "Filter to assets at or above this probability for the chosen horizon (0.0-1.0).",
                    },
                },
                "required": ["scored"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _run(self, **kwargs):
        scored = kwargs.get("scored")
        if not scored or not isinstance(scored, list):
            return {
                "status": "needs_input",
                "agent": self.name,
                "message": "Provide `scored` (list) from AssetHealthScorerAgent. No data will be fabricated.",
            }
        horizon = int(kwargs.get("horizon_days") or 90)
        if horizon not in (30, 90, 180):
            horizon = 90
        top_n = int(kwargs.get("top_n") or 25)
        min_prob = float(kwargs.get("min_probability") or 0.0)

        ranked = []
        for s in scored:
            anomaly = float(s.get("anomaly_score", 0.0))
            ranked.append({
                "asset_id": s.get("asset_id"),
                "asset_class": s.get("asset_class"),
                "substation": s.get("substation"),
                "age_years": s.get("age_years"),
                "anomaly_score": anomaly,
                "health_score": s.get("health_score"),
                "rul_days": s.get("rul_days"),
                "condition_band": s.get("condition_band"),
                "p_fail_30d": _prob(anomaly, 30),
                "p_fail_90d": _prob(anomaly, 90),
                "p_fail_180d": _prob(anomaly, 180),
                "key_drivers": s.get("key_drivers", []),
            })

        ranked.sort(key=lambda r: r[f"p_fail_{horizon}d"], reverse=True)
        if min_prob > 0:
            ranked = [r for r in ranked if r[f"p_fail_{horizon}d"] >= min_prob]
        ranked = ranked[:top_n]

        return _ok(self.name, f"Ranked {len(ranked)} asset(s) by {horizon}-day failure probability.", {
            "as_of_utc": datetime.utcnow().isoformat() + "Z",
            "horizon_days": horizon,
            "top_n": top_n,
            "min_probability": min_prob,
            "ranked": ranked,
        })

    def perform(self, **kwargs):
        return json.dumps(self._run(**kwargs))


# ═════════════════════════════════════════════════════════════════════════════
# 4. Maintenance Work Order
#    Generates Field Service work order drafts (pending_review) for assets that
#    cross a configured probability threshold. Shaped for D365 Field Service.
# ═════════════════════════════════════════════════════════════════════════════

CLASS_TASKS = {
    "transformer": [
        ("Oil DGA Sample + Analyze", "specialist_oil_sampling_crew", 4, "P2"),
        ("Bushing IR + Capacitance Test", "transformer_test_crew", 3, "P2"),
        ("Cooler Bank Inspection", "substation_crew", 2, "P3"),
    ],
    "switchgear": [
        ("SF6 Leak Investigation", "switchgear_specialist", 3, "P1"),
        ("Contact Resistance Test", "substation_crew", 3, "P2"),
        ("Thermography Scan", "thermography_team", 1, "P3"),
    ],
    "underground_cable": [
        ("Partial Discharge Field Survey", "cable_pd_crew", 5, "P2"),
        ("Joint Inspection (selective)", "cable_splice_crew", 4, "P2"),
        ("Sheath Bonding Verification", "cable_test_crew", 3, "P3"),
    ],
    "overhead_line": [
        ("Aerial Patrol + LiDAR Resag Check", "aerial_patrol_team", 4, "P2"),
        ("Vegetation Management Dispatch", "vegetation_crew", 6, "P2"),
        ("Conductor Hotspot Inspection", "line_crew", 3, "P3"),
    ],
}


def _wo_id(asset_id, horizon):
    h = hashlib.sha256(f"{asset_id}|{horizon}|wo".encode()).hexdigest()
    return "WO-" + h[:10].upper()


def _due_by(priority):
    days = {"P1": 3, "P2": 14, "P3": 30}.get(priority, 21)
    return (datetime.utcnow() + timedelta(days=days)).date().isoformat()


class MaintenanceWorkOrderAgent(BasicAgent):
    def __init__(self):
        self.name = "MaintenanceWorkOrderAgent"
        self.metadata = {
            "name": self.name,
            "description": (
                "Generates Field Service work order drafts for assets crossing a "
                "configured failure-probability threshold. Outputs are pending_review "
                "and shaped for D365 Field Service / ServiceNow-style ingestion."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "ranked": {
                        "type": "array",
                        "description": "Ranked asset rows from FailureProbabilityRankerAgent.data.ranked.",
                    },
                    "horizon_days": {
                        "type": "integer",
                        "enum": [30, 90, 180],
                        "description": "Horizon to evaluate against. Defaults to 90.",
                    },
                    "threshold": {
                        "type": "number",
                        "description": "Minimum failure probability for the chosen horizon (0.0-1.0). Defaults to 0.30.",
                    },
                    "max_orders": {
                        "type": "integer",
                        "description": "Cap on number of WOs generated. Defaults to 50.",
                    },
                },
                "required": ["ranked"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _run(self, **kwargs):
        ranked = kwargs.get("ranked")
        if not ranked or not isinstance(ranked, list):
            return {
                "status": "needs_input",
                "agent": self.name,
                "message": "Provide `ranked` (list) from FailureProbabilityRankerAgent. No data will be fabricated.",
            }
        horizon = int(kwargs.get("horizon_days") or 90)
        if horizon not in (30, 90, 180):
            horizon = 90
        threshold = float(kwargs.get("threshold") or 0.30)
        max_orders = int(kwargs.get("max_orders") or 50)

        prob_key = f"p_fail_{horizon}d"
        eligible = [r for r in ranked if float(r.get(prob_key, 0)) >= threshold]
        eligible.sort(key=lambda r: r[prob_key], reverse=True)
        eligible = eligible[:max_orders]

        orders = []
        for r in eligible:
            klass = r.get("asset_class") or "transformer"
            tasks = CLASS_TASKS.get(klass, CLASS_TASKS["transformer"])
            priority = "P1" if r[prob_key] >= 0.75 else "P2" if r[prob_key] >= 0.50 else "P3"
            task_name, crew, est_hours, _ = tasks[0]
            orders.append({
                "work_order_id": _wo_id(r["asset_id"], horizon),
                "status": "pending_review",
                "asset_id": r["asset_id"],
                "asset_class": klass,
                "substation": r.get("substation"),
                "priority": priority,
                "horizon_days": horizon,
                "failure_probability": r[prob_key],
                "condition_band": r.get("condition_band"),
                "task": task_name,
                "assigned_crew_type": crew,
                "estimated_hours": est_hours,
                "due_by": _due_by(priority),
                "rationale": "; ".join(r.get("key_drivers", []) or ["Threshold exceeded"]),
                "target_system": "D365 Field Service",
            })

        return _ok(self.name, f"Drafted {len(orders)} work order(s) above {threshold:.0%} on {horizon}-day horizon.", {
            "as_of_utc": datetime.utcnow().isoformat() + "Z",
            "threshold": threshold,
            "horizon_days": horizon,
            "orders": orders,
        })

    def perform(self, **kwargs):
        return json.dumps(self._run(**kwargs))


# ═════════════════════════════════════════════════════════════════════════════
# 5. Parts Planner
#    Consolidates parts/materials demand from pending work orders, flags
#    long-lead items, emits SAP MM / D365 Supply Chain procurement triggers.
# ═════════════════════════════════════════════════════════════════════════════

# task -> list of (material, qty_per_wo, lead_time_days, unit_cost_usd)
TASK_BOM = {
    "Oil DGA Sample + Analyze": [
        ("Oil sample kit", 1, 7, 85),
        ("DGA lab analysis", 1, 5, 220),
    ],
    "Bushing IR + Capacitance Test": [
        ("Replacement HV bushing (preorder)", 1, 90, 18500),
        ("Insulation oil top-up (drum)", 1, 14, 920),
    ],
    "Cooler Bank Inspection": [
        ("Cooler fan assembly", 1, 21, 1450),
        ("Radiator gasket set", 2, 14, 180),
    ],
    "SF6 Leak Investigation": [
        ("SF6 leak detector cartridge", 1, 7, 320),
        ("SF6 gas cylinder (50kg)", 1, 28, 4800),
    ],
    "Contact Resistance Test": [
        ("Micro-ohmmeter consumables", 1, 7, 95),
    ],
    "Thermography Scan": [
        ("IR camera battery pack", 1, 7, 280),
    ],
    "Partial Discharge Field Survey": [
        ("PD coupler kit", 1, 14, 1750),
    ],
    "Joint Inspection (selective)": [
        ("Cable joint kit (selective)", 1, 60, 4200),
        ("Heat-shrink sleeve set", 2, 14, 110),
    ],
    "Sheath Bonding Verification": [
        ("Sheath voltage limiter", 1, 21, 540),
    ],
    "Aerial Patrol + LiDAR Resag Check": [
        ("Drone battery (LiPo)", 2, 7, 240),
    ],
    "Vegetation Management Dispatch": [
        ("Chipper fuel + PPE pack", 1, 3, 320),
    ],
    "Conductor Hotspot Inspection": [
        ("Compression sleeve repair set", 2, 21, 410),
    ],
}

LONG_LEAD_DAYS = 30


class PartsPlannerAgent(BasicAgent):
    def __init__(self):
        self.name = "PartsPlannerAgent"
        self.metadata = {
            "name": self.name,
            "description": (
                "Aggregates parts / materials demand from pending work orders, "
                "flags long-lead items, and emits procurement triggers shaped "
                "for SAP MM / D365 Supply Chain ingestion."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "orders": {
                        "type": "array",
                        "description": "Work orders from MaintenanceWorkOrderAgent.data.orders.",
                    },
                    "long_lead_threshold_days": {
                        "type": "integer",
                        "description": "Flag any item with lead time >= this many days. Defaults to 30.",
                    },
                },
                "required": ["orders"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _run(self, **kwargs):
        orders = kwargs.get("orders")
        if not orders or not isinstance(orders, list):
            return {
                "status": "needs_input",
                "agent": self.name,
                "message": "Provide `orders` (list) from MaintenanceWorkOrderAgent. No data will be fabricated.",
            }
        long_lead = int(kwargs.get("long_lead_threshold_days") or LONG_LEAD_DAYS)

        demand = {}
        per_order_lines = []
        for o in orders:
            task = o.get("task")
            qty_mult = 1
            bom = TASK_BOM.get(task, [])
            for material, qty, lead, cost in bom:
                entry = demand.setdefault(material, {
                    "material": material,
                    "total_qty": 0,
                    "lead_time_days": lead,
                    "unit_cost_usd": cost,
                    "linked_work_orders": [],
                    "long_lead": lead >= long_lead,
                })
                entry["total_qty"] += qty * qty_mult
                entry["linked_work_orders"].append(o.get("work_order_id"))
                per_order_lines.append({
                    "work_order_id": o.get("work_order_id"),
                    "asset_id": o.get("asset_id"),
                    "material": material,
                    "qty": qty * qty_mult,
                    "lead_time_days": lead,
                    "unit_cost_usd": cost,
                    "extended_cost_usd": qty * qty_mult * cost,
                })

        consolidated = []
        triggers = []
        for entry in demand.values():
            entry["extended_cost_usd"] = entry["total_qty"] * entry["unit_cost_usd"]
            consolidated.append(entry)
            if entry["long_lead"]:
                triggers.append({
                    "procurement_trigger_id": f"PR-{abs(hash(entry['material'])) % 10_000_000:07d}",
                    "material": entry["material"],
                    "qty": entry["total_qty"],
                    "lead_time_days": entry["lead_time_days"],
                    "needed_by": (datetime.utcnow() + timedelta(days=entry["lead_time_days"])).date().isoformat(),
                    "target_system": "SAP MM / D365 Supply Chain",
                    "linked_work_orders": entry["linked_work_orders"],
                })

        total_cost = round(sum(e["extended_cost_usd"] for e in consolidated), 2)

        return _ok(self.name, f"Planned parts for {len(orders)} WO(s). {len(triggers)} long-lead trigger(s) emitted.", {
            "as_of_utc": datetime.utcnow().isoformat() + "Z",
            "long_lead_threshold_days": long_lead,
            "total_estimated_cost_usd": total_cost,
            "consolidated_demand": consolidated,
            "procurement_triggers": triggers,
            "per_order_lines": per_order_lines,
        })

    def perform(self, **kwargs):
        return json.dumps(self._run(**kwargs))


# ═════════════════════════════════════════════════════════════════════════════
# 6. Field Execution Capture
#    Captures and structures field-execution outcomes from a Power Apps mobile
#    form. Produces the closeout JSON that updates the WO and feeds write-back.
# ═════════════════════════════════════════════════════════════════════════════

VALID_COMPLETION = {"completed", "partial", "deferred", "escalated"}
VALID_QUALITY = {"pass", "pass_with_observations", "fail"}


class FieldExecutionCaptureAgent(BasicAgent):
    def __init__(self):
        self.name = "FieldExecutionCaptureAgent"
        self.metadata = {
            "name": self.name,
            "description": (
                "Captures and structures field-execution outcomes from the "
                "Power Apps mobile form. Produces the closeout JSON that "
                "updates the WO and feeds the asset register."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "work_order_id": {"type": "string", "description": "WO identifier from MaintenanceWorkOrderAgent."},
                    "asset_id": {"type": "string", "description": "Asset under maintenance."},
                    "crew_id": {"type": "string", "description": "Crew identifier."},
                    "started_utc": {"type": "string", "description": "ISO timestamp."},
                    "completed_utc": {"type": "string", "description": "ISO timestamp."},
                    "completion_status": {
                        "type": "string",
                        "enum": sorted(VALID_COMPLETION),
                        "description": "Disposition.",
                    },
                    "actual_hours": {"type": "number", "description": "Hours on tools."},
                    "findings": {"type": "array", "items": {"type": "string"}, "description": "Free-text findings."},
                    "photos_count": {"type": "integer", "description": "Photos captured."},
                    "quality_check": {"type": "string", "enum": sorted(VALID_QUALITY)},
                    "parts_consumed": {
                        "type": "array",
                        "description": "List of {material, qty} consumed in the field.",
                    },
                    "next_action": {"type": "string", "description": "Recommended next action."},
                },
                "required": ["work_order_id", "asset_id", "completion_status"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _run(self, **kwargs):
        wo = kwargs.get("work_order_id")
        asset = kwargs.get("asset_id")
        completion = kwargs.get("completion_status")

        missing = [k for k, v in {
            "work_order_id": wo,
            "asset_id": asset,
            "completion_status": completion,
        }.items() if not v]
        if missing:
            return {
                "status": "needs_input",
                "agent": self.name,
                "message": f"Missing required field(s): {', '.join(missing)}.",
            }
        if completion not in VALID_COMPLETION:
            return {
                "status": "error",
                "agent": self.name,
                "message": f"completion_status must be one of {sorted(VALID_COMPLETION)}.",
            }

        quality = kwargs.get("quality_check")
        if quality and quality not in VALID_QUALITY:
            return {
                "status": "error",
                "agent": self.name,
                "message": f"quality_check must be one of {sorted(VALID_QUALITY)}.",
            }

        capture = {
            "capture_id": f"FC-{abs(hash(wo)) % 10_000_000:07d}",
            "work_order_id": wo,
            "asset_id": asset,
            "crew_id": kwargs.get("crew_id"),
            "started_utc": kwargs.get("started_utc"),
            "completed_utc": kwargs.get("completed_utc") or datetime.utcnow().isoformat() + "Z",
            "completion_status": completion,
            "actual_hours": kwargs.get("actual_hours"),
            "findings": kwargs.get("findings") or [],
            "photos_count": int(kwargs.get("photos_count") or 0),
            "quality_check": quality or "pass",
            "parts_consumed": kwargs.get("parts_consumed") or [],
            "next_action": kwargs.get("next_action"),
            "source_system": "Power Apps Mobile",
            "ready_for_writeback": completion in {"completed", "partial"},
        }

        return _ok(self.name, f"Captured execution for {wo}.", capture)

    def perform(self, **kwargs):
        return json.dumps(self._run(**kwargs))


# ═════════════════════════════════════════════════════════════════════════════
# 7. Asset Register Write-back
#    Stages updates to the Asset Management System and ERP fixed-asset register
#    based on completed maintenance work and the post-work condition band.
# ═════════════════════════════════════════════════════════════════════════════

class AssetRegisterWritebackAgent(BasicAgent):
    def __init__(self):
        self.name = "AssetRegisterWritebackAgent"
        self.metadata = {
            "name": self.name,
            "description": (
                "Stages updates to the Asset Management System and ERP fixed-asset "
                "register based on completed maintenance work and the post-work "
                "condition band."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "capture": {
                        "type": "object",
                        "description": "Capture envelope from FieldExecutionCaptureAgent.data.",
                    },
                    "new_condition_band": {
                        "type": "string",
                        "enum": ["Healthy", "Watch", "Degraded", "Critical"],
                        "description": "Operator's post-work condition assessment.",
                    },
                    "useful_life_delta_years": {
                        "type": "number",
                        "description": "Adjustment to useful life in years (positive = extended).",
                    },
                    "book_value_adjustment_usd": {
                        "type": "number",
                        "description": "Optional adjustment to book value in USD.",
                    },
                },
                "required": ["capture"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _run(self, **kwargs):
        capture = kwargs.get("capture")
        if not capture or not isinstance(capture, dict):
            return {
                "status": "needs_input",
                "agent": self.name,
                "message": "Provide `capture` (dict) from FieldExecutionCaptureAgent. No data will be fabricated.",
            }
        if not capture.get("ready_for_writeback", False):
            return {
                "status": "blocked",
                "agent": self.name,
                "message": "Capture is not ready for writeback (completion_status not completed/partial).",
                "data": {"capture_id": capture.get("capture_id")},
            }

        asset_id = capture.get("asset_id")
        wo = capture.get("work_order_id")
        new_band = kwargs.get("new_condition_band") or "Watch"
        life_delta = float(kwargs.get("useful_life_delta_years") or 0.0)
        book_adj = float(kwargs.get("book_value_adjustment_usd") or 0.0)

        ams_envelope = {
            "target_system": "Asset Management System (AMS)",
            "asset_id": asset_id,
            "patch": {
                "condition_band": new_band,
                "last_maintenance_date_utc": capture.get("completed_utc") or datetime.utcnow().isoformat() + "Z",
                "last_work_order_id": wo,
                "useful_life_delta_years": life_delta,
                "field_findings": capture.get("findings") or [],
                "quality_check": capture.get("quality_check"),
            },
        }

        erp_envelope = {
            "target_system": "ERP Fixed-Asset Register",
            "asset_id": asset_id,
            "patch": {
                "last_maintenance_journal_ref": wo,
                "last_maintenance_date_utc": capture.get("completed_utc") or datetime.utcnow().isoformat() + "Z",
                "book_value_adjustment_usd": book_adj,
                "useful_life_delta_years": life_delta,
                "requires_finance_review": abs(book_adj) > 0 or abs(life_delta) >= 1,
            },
        }

        return _ok(self.name, f"Staged write-back for asset {asset_id}.", {
            "as_of_utc": datetime.utcnow().isoformat() + "Z",
            "asset_id": asset_id,
            "envelopes": [ams_envelope, erp_envelope],
            "dispatch_state": "ready_for_integration_runtime",
        })

    def perform(self, **kwargs):
        return json.dumps(self._run(**kwargs))


# ═════════════════════════════════════════════════════════════════════════════
# 8. Lifecycle Capex Planner
#    Multi-year capital replacement pipeline: candidates, fiscal year placement,
#    indicative cost, avoided-failure value, benefit/cost ratio.
# ═════════════════════════════════════════════════════════════════════════════

# Indicative replacement cost (USD) and avoided-failure value per asset class
CLASS_ECONOMICS = {
    "transformer": {"replace_cost_usd": 950_000, "avoided_failure_usd": 4_800_000},
    "switchgear": {"replace_cost_usd": 320_000, "avoided_failure_usd": 1_500_000},
    "underground_cable": {"replace_cost_usd": 1_100_000, "avoided_failure_usd": 3_200_000},
    "overhead_line": {"replace_cost_usd": 480_000, "avoided_failure_usd": 1_800_000},
}


def _fiscal_year_offset(p180, age_years):
    """Return number of years out before the asset is slated for replacement."""
    if p180 >= 0.65 or age_years >= 40:
        return 0
    if p180 >= 0.45 or age_years >= 32:
        return 1
    if p180 >= 0.30 or age_years >= 25:
        return 2
    return 3


class LifecycleCapexPlannerAgent(BasicAgent):
    def __init__(self):
        self.name = "LifecycleCapexPlannerAgent"
        self.metadata = {
            "name": self.name,
            "description": (
                "Produces a multi-year capital replacement pipeline from the "
                "scored / ranked fleet: candidates, fiscal year placement, "
                "indicative cost, and avoided-failure value."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "ranked": {
                        "type": "array",
                        "description": "Ranked rows from FailureProbabilityRankerAgent.data.ranked (must include 180-day prob).",
                    },
                    "current_fiscal_year": {
                        "type": "integer",
                        "description": "Current FY (e.g. 2026). Defaults to current calendar year.",
                    },
                    "horizon_years": {
                        "type": "integer",
                        "description": "How many FYs forward to plan. Defaults to 4.",
                    },
                },
                "required": ["ranked"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _run(self, **kwargs):
        ranked = kwargs.get("ranked")
        if not ranked or not isinstance(ranked, list):
            return {
                "status": "needs_input",
                "agent": self.name,
                "message": "Provide `ranked` (list) from FailureProbabilityRankerAgent. No data will be fabricated.",
            }
        cfy = int(kwargs.get("current_fiscal_year") or datetime.utcnow().year)
        horizon = int(kwargs.get("horizon_years") or 4)

        pipeline = []
        for r in ranked:
            klass = r.get("asset_class") or "transformer"
            economics = CLASS_ECONOMICS.get(klass, CLASS_ECONOMICS["transformer"])
            age_years = int(r.get("age_years", 0))  # tolerated if absent
            p180 = float(r.get("p_fail_180d", 0.0))
            fy_offset = _fiscal_year_offset(p180, age_years)
            if fy_offset >= horizon:
                continue  # outside the planning window
            pipeline.append({
                "asset_id": r["asset_id"],
                "asset_class": klass,
                "substation": r.get("substation"),
                "anomaly_score": r.get("anomaly_score"),
                "p_fail_180d": p180,
                "condition_band": r.get("condition_band"),
                "planned_fiscal_year": cfy + fy_offset,
                "indicative_replace_cost_usd": economics["replace_cost_usd"],
                "avoided_failure_value_usd": economics["avoided_failure_usd"],
                "benefit_cost_ratio": round(
                    economics["avoided_failure_usd"] * p180 / max(1, economics["replace_cost_usd"]), 2
                ),
                "justification_drivers": r.get("key_drivers", []),
            })

        pipeline.sort(key=lambda x: (x["planned_fiscal_year"], -x["benefit_cost_ratio"]))

        by_fy = {}
        for row in pipeline:
            fy = row["planned_fiscal_year"]
            agg = by_fy.setdefault(fy, {
                "fiscal_year": fy,
                "candidates": 0,
                "total_replace_cost_usd": 0,
                "total_avoided_failure_value_usd": 0,
                "by_class": {},
            })
            agg["candidates"] += 1
            agg["total_replace_cost_usd"] += row["indicative_replace_cost_usd"]
            agg["total_avoided_failure_value_usd"] += row["avoided_failure_value_usd"]
            agg["by_class"][row["asset_class"]] = agg["by_class"].get(row["asset_class"], 0) + 1
        by_fy_sorted = [by_fy[k] for k in sorted(by_fy.keys())]

        return _ok(self.name, f"Planned {len(pipeline)} candidate(s) across {len(by_fy_sorted)} fiscal year(s).", {
            "as_of_utc": datetime.utcnow().isoformat() + "Z",
            "current_fiscal_year": cfy,
            "horizon_years": horizon,
            "annual_summary": by_fy_sorted,
            "pipeline": pipeline,
        })

    def perform(self, **kwargs):
        return json.dumps(self._run(**kwargs))


# ═════════════════════════════════════════════════════════════════════════════
# *. Orchestrator — Predictive Asset Maintenance Intelligence
#    The "Primary processing engine": runs aggregate -> score -> rank, then fans
#    out to work-order/parts drafting and the capex pipeline in a single call.
# ═════════════════════════════════════════════════════════════════════════════

class PredictiveAssetMaintenanceIntelligenceAgent(BasicAgent):
    def __init__(self):
        self.name = "PredictiveAssetMaintenanceIntelligenceAgent"
        self.metadata = {
            "name": self.name,
            "description": (
                "End-to-end predictive asset maintenance pipeline for grid "
                "infrastructure. Aggregates telemetry, scores asset health, ranks "
                "failure probability across 30/90/180-day horizons, drafts Field "
                "Service work orders + parts procurement for at-risk assets, and "
                "produces a multi-year capex replacement pipeline — all in one call. "
                "Use this when the user wants the whole predictive maintenance run; "
                "use the individual agents for a single step."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "asset_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Specific asset IDs to run. If omitted, a synthetic fleet sample is used.",
                    },
                    "asset_class": {
                        "type": "string",
                        "enum": ASSET_CLASSES,
                        "description": "Restrict the run to a single asset class.",
                    },
                    "substation": {
                        "type": "string",
                        "description": "Restrict the run to a single substation (e.g. SUB-44).",
                    },
                    "sample_size": {
                        "type": "integer",
                        "description": "Fleet sample size when asset_ids is omitted. Defaults to 25.",
                    },
                    "horizon_days": {
                        "type": "integer",
                        "enum": [30, 90, 180],
                        "description": "Ranking + work-order horizon. Defaults to 90.",
                    },
                    "top_n": {
                        "type": "integer",
                        "description": "How many ranked assets to carry forward. Defaults to 25.",
                    },
                    "work_order_threshold": {
                        "type": "number",
                        "description": "Failure-probability threshold for drafting work orders (0.0-1.0). Defaults to 0.30.",
                    },
                    "current_fiscal_year": {
                        "type": "integer",
                        "description": "Current FY for the capex pipeline. Defaults to current year.",
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _run(self, **kwargs):
        horizon = int(kwargs.get("horizon_days") or 90)
        if horizon not in (30, 90, 180):
            horizon = 90
        top_n = int(kwargs.get("top_n") or 25)
        threshold = float(kwargs.get("work_order_threshold") or 0.30)

        # 1 — aggregate telemetry
        agg = AssetSensorAggregatorAgent()._run(
            asset_ids=kwargs.get("asset_ids"),
            asset_class=kwargs.get("asset_class"),
            substation=kwargs.get("substation"),
            sample_size=kwargs.get("sample_size"),
        )
        snapshots = agg.get("data", {}).get("snapshots", [])
        if not snapshots:
            return {
                "status": "needs_input",
                "agent": self.name,
                "message": "No assets matched the requested filters; nothing to analyze.",
                "data": {"aggregation": agg},
            }

        # 2 — score health
        scored_res = AssetHealthScorerAgent()._run(snapshots=snapshots)
        scored = scored_res.get("data", {}).get("scored", [])

        # 3 — rank failure probability
        ranked_res = FailureProbabilityRankerAgent()._run(scored=scored, horizon_days=horizon, top_n=top_n)
        ranked = ranked_res.get("data", {}).get("ranked", [])

        # 4 — draft work orders for at-risk assets
        wo_res = MaintenanceWorkOrderAgent()._run(ranked=ranked, horizon_days=horizon, threshold=threshold)
        orders = wo_res.get("data", {}).get("orders", [])

        # 5 — plan parts for those work orders
        parts_res = PartsPlannerAgent()._run(orders=orders)

        # 8 — capex replacement pipeline off the same ranked fleet
        capex_res = LifecycleCapexPlannerAgent()._run(
            ranked=ranked, current_fiscal_year=kwargs.get("current_fiscal_year")
        )

        band_summary = scored_res.get("data", {}).get("summary", {})
        return _ok(
            self.name,
            (
                f"Ran predictive maintenance over {len(snapshots)} asset(s): "
                f"{band_summary.get('Critical', 0)} critical, "
                f"{band_summary.get('Degraded', 0)} degraded; "
                f"{len(orders)} work order(s) drafted; "
                f"{len(capex_res.get('data', {}).get('pipeline', []))} capex candidate(s)."
            ),
            {
                "as_of_utc": datetime.utcnow().isoformat() + "Z",
                "horizon_days": horizon,
                "work_order_threshold": threshold,
                "fleet_summary": band_summary,
                "ranked": ranked,
                "work_orders": orders,
                "parts_plan": parts_res.get("data", {}),
                "capex_pipeline": capex_res.get("data", {}),
                "stage_status": {
                    "aggregate": agg.get("status"),
                    "score": scored_res.get("status"),
                    "rank": ranked_res.get("status"),
                    "work_orders": wo_res.get("status"),
                    "parts": parts_res.get("status"),
                    "capex": capex_res.get("status"),
                },
            },
        )

    def perform(self, **kwargs):
        return json.dumps(self._run(**kwargs))


# ── Self-test / demo ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    out = PredictiveAssetMaintenanceIntelligenceAgent().perform(sample_size=12, horizon_days=90)
    print(out[:4000])
