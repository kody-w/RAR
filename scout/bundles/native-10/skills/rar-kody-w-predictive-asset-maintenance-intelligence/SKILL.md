---
name: "rar-kody-w-predictive-asset-maintenance-intelligence"
description: "End-to-end predictive asset maintenance pipeline for grid infrastructure. Aggregates telemetry, scores asset health, ranks failure probability across 30/90/180-day horizons, drafts Field Service work orders + parts procurement for at-risk assets, and produces a multi-year capex replacement pipeline \u2014 all in one call. Use this when the user wants the whole predictive maintenance run; use the individual agents for a single step."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/predictive_asset_maintenance_intelligence", "rar_sha256": "0d74c48db5b63727319d7514b0743c1db08214d20c27560ebcd4902b205eeeed", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["energy", "predictive-maintenance", "asset-management", "grid", "field-service"]}
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
