---
name: "rar-kody-w-predictive-asset-maintenance-intelligence"
description: "End-to-end predictive asset maintenance pipeline for grid infrastructure. Aggregates telemetry, scores asset health, ranks failure probability across 30/90/180-day horizons, drafts Field Service work orders + parts procurement for at-risk assets, and produces a multi-year capex replacement pipeline \u2014 all in one call. Use this when the user wants the whole predictive maintenance run; use the individual agents for a single step."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/predictive_asset_maintenance_intelligence", "rar_sha256": "d792270520fb82ad23815a9b9d6e940da5428ee5baa5fcddc362846adaff90e0", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "predictive_asset_maintenance_intelligence_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/predictive-asset-maintenance-intelligence:8c6264eead8494110036a16e6ee3cb558461d878ed263ab472c407b584536ed5", "kind": "skill"}, "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["energy", "predictive-maintenance", "asset-management", "grid", "field-service"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/predictive_asset_maintenance_intelligence`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `predictive_asset_maintenance_intelligence_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
