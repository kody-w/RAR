---
name: "rar-kody-w-predictive-asset-maintenance-intelligence"
description: "End-to-end predictive asset maintenance pipeline for grid infrastructure. Aggregates telemetry, scores asset health, ranks failure probability across 30/90/180-day horizons, drafts Field Service work orders + parts procurement for at-risk assets, and produces a multi-year capex replacement pipeline \u2014 all in one call. Use this when the user wants the whole predictive maintenance run; use the individual agents for a single step."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/predictive_asset_maintenance_intelligence", "rar_sha256": "d792270520fb82ad23815a9b9d6e940da5428ee5baa5fcddc362846adaff90e0", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["energy", "predictive-maintenance", "asset-management", "grid", "field-service"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/predictive_asset_maintenance_intelligence`. The original RAPP
agent is preserved byte-for-byte in `predictive_asset_maintenance_intelligence_agent.py` and in the RCI capsule.

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

Predictive Asset Maintenance Intelligence — single-file RAPP agent stack.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "asset_class": {
      "description": "Restrict the run to a single asset class.",
      "enum": [
        "transformer",
        "switchgear",
        "underground_cable",
        "overhead_line"
      ],
      "type": "string"
    },
    "asset_ids": {
      "description": "Specific asset IDs to run. If omitted, a synthetic fleet sample is used.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "current_fiscal_year": {
      "description": "Current FY for the capex pipeline. Defaults to current year.",
      "type": "integer"
    },
    "horizon_days": {
      "description": "Ranking + work-order horizon. Defaults to 90.",
      "enum": [
        30,
        90,
        180
      ],
      "type": "integer"
    },
    "sample_size": {
      "description": "Fleet sample size when asset_ids is omitted. Defaults to 25.",
      "type": "integer"
    },
    "substation": {
      "description": "Restrict the run to a single substation (e.g. SUB-44).",
      "type": "string"
    },
    "top_n": {
      "description": "How many ranked assets to carry forward. Defaults to 25.",
      "type": "integer"
    },
    "work_order_threshold": {
      "description": "Failure-probability threshold for drafting work orders (0.0-1.0). Defaults to 0.30.",
      "type": "number"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `predictive_asset_maintenance_intelligence_agent.py` and embedded as the fenced Python below (sha256 d792270520fb82ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `predictive_asset_maintenance_intelligence_agent.py` first:

```bash
python3 predictive_asset_maintenance_intelligence_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 predictive_asset_maintenance_intelligence_agent.py   # or on stdin
python3 predictive_asset_maintenance_intelligence_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
    "version": "1.0.1",
    "display_name": "Predictive Asset Maintenance Intelligence",
    "description": (
        "Simulates a grid predictive-maintenance pipeline \u2014 telemetry scoring, failure ranking, work-order and capex drafts \u2014 from seeded synthetic demo data."
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
