---
name: "rar-kody-w-predictive-asset-maintenance-intelligence"
description: "End-to-end predictive asset maintenance pipeline for grid infrastructure. Aggregates telemetry, scores asset health, ranks failure probability across 30/90/180-day horizons, drafts Field Service work orders + parts procurement for at-risk assets, and produces a multi-year capex replacement pipeline \u2014 all in one call. Use this when the user wants the whole predictive maintenance run; use the individual agents for a single step."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/predictive_asset_maintenance_intelligence", "rar_sha256": "0d74c48db5b63727319d7514b0743c1db08214d20c27560ebcd4902b205eeeed", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["energy", "predictive-maintenance", "asset-management", "grid", "field-service"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `predictive_asset_maintenance_intelligence_agent.py` and embedded as the fenced Python below (sha256 0d74c48db5b63727…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `predictive_asset_maintenance_intelligence_agent.py` first:

```bash
python3 predictive_asset_maintenance_intelligence_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 predictive_asset_maintenance_intelligence_agent.py   # or on stdin
python3 predictive_asset_maintenance_intelligence_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/predictive_asset_maintenance_intelligence_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/predictive_asset_maintenance_intelligence_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/predictive_asset_maintenance_intelligence/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
