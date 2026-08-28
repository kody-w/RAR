---
name: "rar-aibast-agents-library-pipeline-velocity"
description: "Measures pipeline velocity from live opportunities in a simulated Dynamics 365 tenant, with bottlenecks and an embedded offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/pipeline_velocity", "rar_sha256": "1dfc4e8edab7dcefee1b54e7160e5ba1854e3bc99f9c500e3827a559c2594b68", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["b2b", "sales", "pipeline-velocity", "deal-progression", "analytics"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/pipeline_velocity`. The original RAPP
agent is preserved byte-for-byte in `pipeline_velocity_agent.py` and in the RCI capsule.

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

Pipeline Velocity Agent — a template you are meant to mutate.

Measures pipeline velocity across stages, detects bottlenecks, benchmarks
against history, and drafts acceleration plans to improve time-to-close.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="velocity_dashboard") — velocity, stage
     distribution, and cycle length are computed from live records such
     as the closed-won "Foxglove Learning — Secure print rollout".
  2. No network? Everything falls back to the embedded demo layer below
     (_STAGE_TIMESTAMPS / _QUARTERLY_VELOCITY) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PIPELINE_VELOCITY_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with your own client. The dict shape the rest of
     the file needs is documented in _normalize_live_deal(). Per-stage
     timestamp history is an enrichment seam — wire your CRM stage audit
     log there; quarterly trend stays simulated until you do.

OPERATIONS
  velocity_dashboard | stage_analysis | bottleneck_detection
  | acceleration_plan
  kwargs: operation (required)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The analysis to perform",
      "enum": [
        "velocity_dashboard",
        "stage_analysis",
        "bottleneck_detection",
        "acceleration_plan"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pipeline_velocity_agent.py` and embedded as the fenced Python below (sha256 1dfc4e8edab7dcef…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pipeline_velocity_agent.py` first:

```bash
python3 pipeline_velocity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pipeline_velocity_agent.py   # or on stdin
python3 pipeline_velocity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pipeline Velocity Agent — a template you are meant to mutate.

Measures pipeline velocity across stages, detects bottlenecks, benchmarks
against history, and drafts acceleration plans to improve time-to-close.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="velocity_dashboard") — velocity, stage
     distribution, and cycle length are computed from live records such
     as the closed-won "Foxglove Learning — Secure print rollout".
  2. No network? Everything falls back to the embedded demo layer below
     (_STAGE_TIMESTAMPS / _QUARTERLY_VELOCITY) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PIPELINE_VELOCITY_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with your own client. The dict shape the rest of
     the file needs is documented in _normalize_live_deal(). Per-stage
     timestamp history is an enrichment seam — wire your CRM stage audit
     log there; quarterly trend stays simulated until you do.

OPERATIONS
  velocity_dashboard | stage_analysis | bottleneck_detection
  | acceleration_plan
  kwargs: operation (required)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timezone

# ===================================================================
# RAPP AGENT MANIFEST
# ===================================================================
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/pipeline_velocity",
    "version": "1.1.0",
    "display_name": "Pipeline Velocity",
    "description": "Measures pipeline velocity from live opportunities in a simulated Dynamics 365 tenant, with bottlenecks and an embedded offline demo fallback.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "pipeline-velocity", "deal-progression", "analytics"],
    "category": "b2b_sales",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ===================================================================
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export PIPELINE_VELOCITY_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_deal().
# ===================================================================

DATA_SOURCE_URL = os.environ.get(
    "PIPELINE_VELOCITY_DATA_URL",
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


_LIVE_STAGE_MAP = {"Qualify": "Qualification", "Develop": "Discovery",
                   "Propose": "Proposal", "Close": "Negotiation"}


def _parse_dt(iso_date):
    try:
        return datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
    except (ValueError, TypeError):
        return None


def _normalize_live_deal(row):
    """Project a Dynamics opportunity onto the shape this agent uses.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not knowable from the CRM alone' and the
    renderers label it an enrichment seam (per-stage timestamps need your
    CRM stage audit log)."""
    created = _parse_dt(row.get("createdon"))
    closed = _parse_dt(row.get("actualclosedate"))
    end = closed or datetime.now(timezone.utc)
    age = max(0, (end - created).days) if created else 0
    state = row.get("statecode")
    if state == 1:
        stage = "Closed Won"
    elif state == 2:
        stage = "Closed Lost"
    else:
        stage = _LIVE_STAGE_MAP.get(row.get("stepname"), "Qualification")
    return {
        "deal_id": str(row.get("opportunityid", ""))[:8],
        "name": row.get("name", "Unknown"),
        "value": int(float(row.get("estimatedvalue") or 0)),
        "owner": row.get("owneridname", ""),
        "current_stage": stage,
        "total_age": age,
        "probability": (int(row.get("closeprobability") or 0)) / 100,
        "stages": None,  # enrichment seam — wire your stage audit log
        "_open": state == 0,
        "_live": True,
    }


def _live_deals():
    """All live opportunities normalized for this agent; [] when offline."""
    return [_normalize_live_deal(o) for o in _fetch_collection("opportunities")]


# ===================================================================
# EMBEDDED DEMO LAYER (offline fallback)
# ===================================================================

_STAGE_TIMESTAMPS = {
    "TechCorp Industries": {
        "deal_id": "OPP-001", "value": 890000, "owner": "Mike Chen",
        "stages": {"Qualification": 12, "Discovery": 16, "Proposal": 34},
        "current_stage": "Proposal", "total_age": 62, "probability": 0.35,
    },
    "Global Manufacturing": {
        "deal_id": "OPP-002", "value": 720000, "owner": "Lisa Torres",
        "stages": {"Qualification": 10, "Discovery": 15, "Proposal": 14, "Negotiation": 28},
        "current_stage": "Negotiation", "total_age": 67, "probability": 0.55,
    },
    "Apex Financial": {
        "deal_id": "OPP-003", "value": 580000, "owner": "James Park",
        "stages": {"Qualification": 11, "Discovery": 25},
        "current_stage": "Discovery", "total_age": 36, "probability": 0.20,
    },
    "Metro Healthcare": {
        "deal_id": "OPP-004", "value": 440000, "owner": "Mike Chen",
        "stages": {"Qualification": 9, "Discovery": 14, "Proposal": 22},
        "current_stage": "Proposal", "total_age": 45, "probability": 0.45,
    },
    "Pacific Telecom": {
        "deal_id": "OPP-013", "value": 780000, "owner": "Lisa Torres",
        "stages": {"Qualification": 8, "Discovery": 12, "Proposal": 11, "Negotiation": 14},
        "current_stage": "Negotiation", "total_age": 45, "probability": 0.75,
    },
    "Pinnacle Logistics": {
        "deal_id": "OPP-005", "value": 360000, "owner": "James Park",
        "stages": {"Qualification": 20},
        "current_stage": "Qualification", "total_age": 20, "probability": 0.10,
    },
    "Northstar Aerospace": {
        "deal_id": "OPP-014", "value": 650000, "owner": "Mike Chen",
        "stages": {"Qualification": 10, "Discovery": 13, "Proposal": 17},
        "current_stage": "Proposal", "total_age": 40, "probability": 0.50,
    },
    "DataFlow Corp": {
        "deal_id": "OPP-020", "value": 340000, "owner": "Lisa Torres",
        "stages": {"Qualification": 7, "Discovery": 10, "Proposal": 9, "Negotiation": 8, "Contract": 3},
        "current_stage": "Contract", "total_age": 37, "probability": 0.90,
    },
}

_CONVERSION_RATES = {
    "Qualification_to_Discovery": {"rate": 0.72, "avg_days": 12, "benchmark_days": 14},
    "Discovery_to_Proposal": {"rate": 0.58, "avg_days": 16, "benchmark_days": 18},
    "Proposal_to_Negotiation": {"rate": 0.65, "avg_days": 15, "benchmark_days": 16},
    "Negotiation_to_Contract": {"rate": 0.78, "avg_days": 11, "benchmark_days": 12},
    "Contract_to_Closed_Won": {"rate": 0.88, "avg_days": 7, "benchmark_days": 10},
}

_STAGE_BENCHMARKS = {
    "Qualification": {"target_days": 14, "median_days": 11, "p75_days": 16, "p90_days": 22},
    "Discovery": {"target_days": 18, "median_days": 14, "p75_days": 20, "p90_days": 28},
    "Proposal": {"target_days": 16, "median_days": 12, "p75_days": 18, "p90_days": 26},
    "Negotiation": {"target_days": 12, "median_days": 9, "p75_days": 14, "p90_days": 20},
    "Contract": {"target_days": 10, "median_days": 6, "p75_days": 10, "p90_days": 15},
}

_QUARTERLY_VELOCITY = {
    "Q1_2025": {"avg_cycle": 58, "pipeline_value": 8200000, "deals_closed": 14, "velocity_index": 1980000},
    "Q2_2025": {"avg_cycle": 54, "pipeline_value": 9100000, "deals_closed": 16, "velocity_index": 2700000},
    "Q3_2025": {"avg_cycle": 51, "pipeline_value": 10400000, "deals_closed": 18, "velocity_index": 3670000},
    "Q4_2025": {"avg_cycle": 48, "pipeline_value": 11200000, "deals_closed": 21, "velocity_index": 4900000},
}


# ===================================================================
# HELPERS
# ===================================================================

def _pipeline_velocity_formula(num_deals, avg_value, win_rate, avg_cycle):
    """Standard pipeline velocity = (# deals x avg value x win rate) / avg cycle days."""
    if avg_cycle == 0:
        return 0
    return round(num_deals * avg_value * win_rate / avg_cycle)


def _current_bottlenecks():
    """Identify stages where deals are exceeding benchmarks."""
    bottlenecks = {}
    for deal_name, deal in _STAGE_TIMESTAMPS.items():
        stage = deal["current_stage"]
        days = deal["stages"].get(stage, 0)
        benchmark = _STAGE_BENCHMARKS.get(stage, {})
        target = benchmark.get("target_days", 14)
        if days > target:
            if stage not in bottlenecks:
                bottlenecks[stage] = {"deals": [], "total_value": 0, "avg_excess": 0}
            excess = days - target
            bottlenecks[stage]["deals"].append({"name": deal_name, "value": deal["value"], "days": days, "excess": excess})
            bottlenecks[stage]["total_value"] += deal["value"]

    for stage, data in bottlenecks.items():
        data["avg_excess"] = round(sum(d["excess"] for d in data["deals"]) / len(data["deals"]))
    return bottlenecks


# ===================================================================
# AGENT CLASS
# ===================================================================

class PipelineVelocityAgent(BasicAgent):
    """
    Measures and optimizes pipeline velocity.

    Operations:
        velocity_dashboard   - overall velocity metrics and KPIs
        stage_analysis       - per-stage conversion and timing analysis
        bottleneck_detection - identify stages causing slowdowns
        acceleration_plan    - recommendations to improve velocity
    """

    def __init__(self):
        self.name = "PipelineVelocityAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["velocity_dashboard", "stage_analysis", "bottleneck_detection", "acceleration_plan"],
                        "description": "The analysis to perform",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "velocity_dashboard")
        dispatch = {
            "velocity_dashboard": self._velocity_dashboard,
            "stage_analysis": self._stage_analysis,
            "bottleneck_detection": self._bottleneck_detection,
            "acceleration_plan": self._acceleration_plan,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"**Error:** Unknown operation '{op}'. Valid: {', '.join(dispatch.keys())}"
        return handler()

    # -- velocity_dashboard (flagship: prefers LIVE tenant, falls back) -
    def _velocity_dashboard(self) -> str:
        live = _live_deals()
        if live:
            open_deals = [d for d in live if d["_open"]]
            won_deals = [d for d in live if d["current_stage"] == "Closed Won"]
            num_deals = len(open_deals)
            total_value = sum(d["value"] for d in open_deals)
            avg_value = round(total_value / max(num_deals, 1))
            won_cycles = [d["total_age"] for d in won_deals if d["total_age"]]
            avg_cycle = round(sum(won_cycles) / max(len(won_cycles), 1)) if won_cycles else \
                round(sum(d["total_age"] for d in open_deals) / max(num_deals, 1))
            avg_prob = round(sum(d["probability"] for d in open_deals) / max(num_deals, 1), 2)
            velocity = _pipeline_velocity_formula(num_deals, avg_value, avg_prob, avg_cycle)

            stage_counts = {}
            for d in open_deals:
                s = d["current_stage"]
                stage_counts.setdefault(s, {"count": 0, "value": 0})
                stage_counts[s]["count"] += 1
                stage_counts[s]["value"] += d["value"]
            stage_rows = ""
            for stage in ["Qualification", "Discovery", "Proposal", "Negotiation", "Contract"]:
                sc = stage_counts.get(stage, {"count": 0, "value": 0})
                stage_rows += f"| {stage} | {sc['count']} | ${sc['value']:,} |\n"

            return (
                f"**Pipeline Velocity Dashboard — LIVE** (Static Dynamics 365 tenant)\n\n"
                f"| Metric | Value |\n"
                f"|--------|-------|\n"
                f"| Active Deals | {num_deals} |\n"
                f"| Total Pipeline | ${total_value:,} |\n"
                f"| Avg Deal Value | ${avg_value:,} |\n"
                f"| Avg Win Prob (CRM) | {avg_prob:.0%} |\n"
                f"| Avg Cycle Length | {avg_cycle} days (from {len(won_cycles)} closed-won deals) |\n"
                f"| **Pipeline Velocity** | **${velocity:,}/day** |\n\n"
                f"**Stage Distribution (open deals):**\n\n"
                f"| Stage | Deals | Value |\n"
                f"|-------|-------|-------|\n"
                f"{stage_rows}\n"
                f"**Quarterly Velocity Trend:** n/a — enrichment seam "
                f"(wire your historical analytics; the offline demo shows a simulated trend)\n\n"
                f"Source: [Live Dynamics 365 opportunities]\n"
                f"Agents: VelocityEngine, PipelineTracker"
            )
        deals = _STAGE_TIMESTAMPS
        num_deals = len(deals)
        total_value = sum(d["value"] for d in deals.values())
        avg_value = round(total_value / max(num_deals, 1))
        avg_cycle = round(sum(d["total_age"] for d in deals.values()) / max(num_deals, 1))
        avg_prob = round(sum(d["probability"] for d in deals.values()) / max(num_deals, 1), 2)
        velocity = _pipeline_velocity_formula(num_deals, avg_value, avg_prob, avg_cycle)

        # Stage distribution
        stage_counts = {}
        for d in deals.values():
            s = d["current_stage"]
            if s not in stage_counts:
                stage_counts[s] = {"count": 0, "value": 0}
            stage_counts[s]["count"] += 1
            stage_counts[s]["value"] += d["value"]

        stage_rows = ""
        for stage in ["Qualification", "Discovery", "Proposal", "Negotiation", "Contract"]:
            sc = stage_counts.get(stage, {"count": 0, "value": 0})
            stage_rows += f"| {stage} | {sc['count']} | ${sc['value']:,} |\n"

        # Quarterly trend
        q_rows = ""
        for q, data in _QUARTERLY_VELOCITY.items():
            q_rows += f"| {q.replace('_', ' ')} | ${data['velocity_index']:,}/day | {data['avg_cycle']}d | {data['deals_closed']} |\n"

        return (
            f"**Pipeline Velocity Dashboard**\n\n"
            f"| Metric | Value |\n"
            f"|--------|-------|\n"
            f"| Active Deals | {num_deals} |\n"
            f"| Total Pipeline | ${total_value:,} |\n"
            f"| Avg Deal Value | ${avg_value:,} |\n"
            f"| Avg Win Rate | {avg_prob:.0%} |\n"
            f"| Avg Cycle Length | {avg_cycle} days |\n"
            f"| **Pipeline Velocity** | **${velocity:,}/day** |\n\n"
            f"**Stage Distribution:**\n\n"
            f"| Stage | Deals | Value |\n"
            f"|-------|-------|-------|\n"
            f"{stage_rows}\n"
            f"**Quarterly Velocity Trend:**\n\n"
            f"| Quarter | Velocity | Avg Cycle | Deals Closed |\n"
            f"|---------|----------|-----------|-------------|\n"
            f"{q_rows}\n"
            f"Source: [CRM Pipeline Data + Historical Analytics]\n"
            f"Agents: VelocityEngine, PipelineTracker"
        )

    # -- stage_analysis ------------------------------------------------
    def _stage_analysis(self) -> str:
        rows = ""
        for transition, data in _CONVERSION_RATES.items():
            stages = transition.replace("_to_", " -> ").replace("_", " ")
            delta = data["avg_days"] - data["benchmark_days"]
            delta_str = f"{delta:+d}d" if delta != 0 else "on target"
            rows += (f"| {stages} | {data['rate']:.0%} | {data['avg_days']}d | "
                     f"{data['benchmark_days']}d | {delta_str} |\n")

        # Per-deal current stage timing
        deal_rows = ""
        for deal_name in sorted(_STAGE_TIMESTAMPS.keys(), key=lambda d: -_STAGE_TIMESTAMPS[d]["value"]):
            deal = _STAGE_TIMESTAMPS[deal_name]
            stage = deal["current_stage"]
            days = deal["stages"].get(stage, 0)
            benchmark = _STAGE_BENCHMARKS.get(stage, {}).get("target_days", 14)
            ratio = round(days / max(benchmark, 1), 1)
            status = "ON TRACK" if ratio <= 1.0 else ("SLOW" if ratio <= 1.5 else "STALLED")
            deal_rows += f"| {deal_name} | ${deal['value']:,} | {stage} | {days}d | {benchmark}d | {ratio}x | {status} |\n"

        return (
            f"**Stage-by-Stage Analysis**\n\n"
            f"**Conversion Rates:**\n\n"
            f"| Transition | Rate | Avg Days | Benchmark | Delta |\n"
            f"|-----------|------|---------|-----------|-------|\n"
            f"{rows}\n"
            f"**Current Deal Timing:**\n\n"
            f"| Deal | Value | Stage | Days | Benchmark | Ratio | Status |\n"
            f"|------|-------|-------|------|-----------|-------|--------|\n"
            f"{deal_rows}\n"
            f"Source: [Stage Transition Data + Benchmarks]\n"
            f"Agents: StageAnalysisEngine"
        )

    # -- bottleneck_detection ------------------------------------------
    def _bottleneck_detection(self) -> str:
        bottlenecks = _current_bottlenecks()

        if not bottlenecks:
            return "**Bottleneck Detection**\n\nNo bottlenecks detected. All deals within benchmark timelines."

        sections = []
        for stage in ["Qualification", "Discovery", "Proposal", "Negotiation", "Contract"]:
            bn = bottlenecks.get(stage)
            if not bn:
                continue
            deal_lines = ""
            for d in sorted(bn["deals"], key=lambda x: -x["value"]):
                deal_lines += f"  - {d['name']}: ${d['value']:,} -- {d['days']}d (+{d['excess']}d over)\n"

            benchmark = _STAGE_BENCHMARKS[stage]
            sections.append(
                f"**{stage} Stage Bottleneck**\n"
                f"Deals affected: {len(bn['deals'])} | Value at risk: ${bn['total_value']:,}\n"
                f"Avg excess: {bn['avg_excess']} days | Benchmark: {benchmark['target_days']}d\n"
                f"P75: {benchmark['p75_days']}d | P90: {benchmark['p90_days']}d\n\n"
                f"Affected deals:\n{deal_lines}"
            )

        total_bottleneck_value = sum(bn["total_value"] for bn in bottlenecks.values())
        return (
            f"**Bottleneck Detection Report**\n\n"
            f"Bottlenecks found in **{len(bottlenecks)}** stages | "
            f"Total value impacted: **${total_bottleneck_value:,}**\n\n"
            + "\n---\n\n".join(sections)
            + f"\n\n**Root Cause Patterns:**\n"
            f"- Proposal stage: Executive access and competitive evaluation delays\n"
            f"- Negotiation stage: Legal review and procurement process bottlenecks\n"
            f"- Qualification stage: Insufficient early engagement and champion gaps\n\n"
            f"Source: [Pipeline Analytics + Stage Duration Data]\n"
            f"Agents: BottleneckDetectionEngine"
        )

    # -- acceleration_plan ---------------------------------------------
    def _acceleration_plan(self) -> str:
        bottlenecks = _current_bottlenecks()

        stage_actions = {
            "Qualification": [
                "Implement automated BANT qualification scoring",
                "Add discovery call within 48h of lead assignment",
                "Set 14-day SLA with escalation for stalled qualification",
            ],
            "Discovery": [
                "Mandate multi-threading by day 10 of Discovery",
                "Require champion identification before stage exit",
                "Offer POC or demo within first week of Discovery",
            ],
            "Proposal": [
                "Pre-stage executive sponsor meeting before proposal delivery",
                "Include competitive differentiation in every proposal",
                "Set 16-day proposal stage SLA with weekly reviews",
            ],
            "Negotiation": [
                "Send pre-approved contract templates day 1 of Negotiation",
                "Schedule legal-to-legal call within 3 business days",
                "Offer flexible payment terms to reduce procurement friction",
            ],
            "Contract": [
                "Assign deal desk support for all contracts over $200K",
                "Implement e-signature with 48-hour reminder cadence",
                "Pre-schedule onboarding kickoff to create urgency",
            ],
        }

        sections = []
        for stage in ["Qualification", "Discovery", "Proposal", "Negotiation", "Contract"]:
            bn = bottlenecks.get(stage)
            actions = stage_actions.get(stage, [])
            impact = f"${bn['total_value']:,} at risk, {bn['avg_excess']}d avg excess" if bn else "Preventive measures"
            action_lines = "\n".join(f"  {i}. {a}" for i, a in enumerate(actions, 1))
            sections.append(
                f"**{stage}** -- {impact}\n{action_lines}"
            )

        # Overall targets
        current_avg = round(sum(d["total_age"] for d in _STAGE_TIMESTAMPS.values()) / max(len(_STAGE_TIMESTAMPS), 1))
        target_avg = round(current_avg * 0.78)

        return (
            f"**Pipeline Acceleration Plan**\n\n"
            f"Current avg cycle: **{current_avg} days** | Target: **{target_avg} days** (-22%)\n\n"
            + "\n\n".join(sections)
            + f"\n\n**Implementation Timeline:**\n"
            f"- Week 1: Deploy SLA tracking and automated alerts\n"
            f"- Week 2: Train team on stage exit criteria and acceleration tactics\n"
            f"- Week 3: Launch weekly velocity reviews in pipeline meetings\n"
            f"- Week 4: First velocity improvement measurement\n\n"
            f"**Expected Outcomes:**\n"
            f"- Reduce avg cycle from {current_avg} to {target_avg} days\n"
            f"- Increase pipeline velocity by 28%\n"
            f"- Eliminate 60% of stage bottlenecks within 30 days\n\n"
            f"Source: [Best Practices + Velocity Benchmarks]\n"
            f"Agents: AccelerationPlannerAgent"
        )


if __name__ == "__main__":
    agent = PipelineVelocityAgent()
    print("=" * 70)
    print("LIVE TENANT DASHBOARD (fetched over HTTP; embedded demo offline)")
    print(agent.perform(operation="velocity_dashboard"))
    print()
    print("=" * 70)
    print("EMBEDDED DEMO (works offline, simulated)")
    print(agent.perform(operation="stage_analysis"))
    print()
    print("=" * 70)
    print(agent.perform(operation="bottleneck_detection"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/627abOjWNIm+Fdk0R8qs5QRAgRC5Ng7M4DYxL5JQGdbFvu+iB2q67/30Y0bmfV2Vb82H+aaRZgE5/jx5fHH3a+d+/cv/jRmbf/l1y+kQJGm9eWXL1E8hH3ejXnbgMdy7A9THw+HLu/iKm/iwxxXbZiP2yHp2/pQ5XN8aLuu7cepycccrMybg38Y8nqq/DGODret8es8HA7nC3YY48Zvxl8OSz5mh6Adxypu4rAcDn4TgX+HuA7iKAK72iT5OC2K6/aQ+FUV+GH5DagXr37dVfHw5df//j9++ZKDz19+/fuXsPIH8OiL9qnl41NJMo2bEeyq/CYFr7sNWNuA713cJ21fg0dRnBw+v/00xFXyy+Gvfy0Xv0+Hnw9f/+/DMPa//tYcPn/a7vAfh+9vv6Xx+NNvX1qw13/76rcvvxx++/LDOb9H/pAFrd9Hv335+c/9UT50/hhmQMrf/3z6/vn3W389vFX69vu/vvvlf98+jH4a/+43frUN+fDn1v/8/F+2/RmD36N4jMPvpvzY/O/e/osIPwzj6tMLv3fA03/u/5dX/7T5H39+zED0wTLglR8O+vBu2/2T6/Lk0LTjj6W//mcl+nic+uaQ/Pblr39l+r7tf/3rXw92Uzbt0hz+CNHhL39vu3/85dvh4Vd59Ovh73/55fCXb0WbNz/9cW4Zb8NPP//8j9++/HnCp/TPo3/6+cs/APAagIzpwyFv3P23/3aQ87BvhzYZD2bYTuOhn5oxr+Pfmt8aK8tBWgyHMYuBsDnuhzyo4s91Xd8W3z0LQH/42//r54E/jF/9N3KHr1Ue9H6/nX6k3x9Q+Nu3gwXEtX2e5iC4B4PUtN+aj13vozqQs3E/g0wKtjH+CuD99f3hnZx/+xdZv39s+9Ztf/vIQ7DmralBC4fQ74apir+9rXhmcfOpc/hO1TUOJyARiADHJznIyV+AdUNbAUYY3xYPZV5VIKQ9MK/ttw/ZwCu/voX97W9/A2ZmvzXfU/J8+E46wwks+EOdw9evwA5ABGk2/gZQmLUghP/4y+F/Hv6rXR/C32dogBM+fQ40vJuqcgCZO9Vvxx7eAYz96MPnf//HpzeBmAbgEEQoT95U9t4MPFXG0Q/Xmjz5FcEuhyAGLgXurN/MlzfpIR+/HYTk8Ie+4ND3K8Bsh6wdRkBkXdxEcRNuQKoPzPnDk29YDwCgQ7L9cpiG+OPUv4Gwf6hY/x6C5X87yLR2GNu2Av+91fxYBDa3TQ7c/0fgvz8HQvq/DAfqh4hvB+WNukPn936X9f7nGYn/PS5tf/ixHQj3D028/Na8mTV+u+ojdb67BywCngk/Q/r1HfND2NY1COzw4+yPNR/Eb7UAx3H/WzN8wtvv36EIW6DKdkinPPKbMP6/PiE1ZO1URR/+A5q+JX1GIfqMygcGf/D74QfBHz4Y/vDbhEAwCnQH1nbvunPY2unjwDoGBefttHoCpnxH8n9R1Px3EgPovlkT4Pk76w3/XKp+AbFvwqz2+3J4+/3DxweA97cvf/kAedT7yTvy/8R+hzf7DW89gGP79p0igBy+ju3XsGqH72rx6vNg8YJ5sBhZk0iLOTxVQzTfRAR/O6jASQCsb88E7Qrwduimqhq+V2DakP+3Kvz28nfg85alfS/WYO8nq6VVG4Ciun1gE7jYfIc5/He1+vAT+Y7iQfKBm9QkycMfMsztja3hh++HrQHy31Iif/R/AWx9CPsYIH7M/Qp4bWmBw77r4TfbksV9/PMPGs/GsRt+PZ3KNtq+Lt9S0B1Mwbe8PQ0fen2NPvX6CvQ6+V1+eh9xmolvyOlTgtVvv/5Rx/9g/P/4P1TkHzr/ePnL94B/ygLFYOzzYPqodh8BDbcQQB0AIAVtyxtVAPXd9Hbcn03QG9k9yINhCrNPQf53BvmIcPR1ASj47QvbrsD5YL0U+33zZo5PXUxAp0By14MsPPRtVYGs+O3Lt7coBCRwC9JyfPvw/zkw7wQCDAv2vjsjgE7QG72h9T7sjw7qo3Oq/A3ELgBmLp86/fS7aZEc87slyAz4JGvm4XT4XbdJw2IMyf39wUgqLVjuHz56C/1OD80HiYSAP7J4+BT32ad9qHn+dpD9Mn5DE2RfDxJg/NgtCQ/mcCMt8mAypPxdm3eHMH7K0ASNkQSF+ePs39+Lf7cN6W0UAMtBvYF4fx0yvwOGARrt2reTfnqf8oHxT0F/wLft01/etPbB+W8miNd3bnyPlumDUgVwEsYnfgrMrh1//lgMCLvy/0D370kM+oHfQxCI7/T108/fu9aPQ999RVjl74LzwYxRHr4pDOj3WXCGd7J+ivrg2jdXNnEcfTQCURt+lKH4o9j+3gDQgpZkj39/Iwm0Wn7108/fDlrcf/1nXL4ZA3yvux9s8xb1rsQNIOXsLQ841a9/BG4BLP1d2zc7fAg6+FOU/3B71aZv1XpAwa/J70GSAz4Ye+De9+Jt+Kce/t3KVB+OjNoPqlI1xiAtQVU+2OlfcwyU6P/ceIIH/7bVBLv/5+FfO0jw+Hub/es/tW8/9fFrAkZFP787ekBEoLJ8+bUBLPjLFxD4+L/o/9+VrwaH9sN7WgAEDIS+afL97Y8D3l/+8/TzDu0fFgAs/hgbwBjSTGB6+O//hl7Ay/9sOnjw70wHj//F7i9gpBm37m3Jm4LAzPIP0Gv+MPt93p/K/rm0Dd4N5LsrfZe+73PN378Ac/03TX4a/NljguWgn/w6vGvuCf4GAS3A9++9E3j3/7X7/NwGEA+aIbAPjpIQja9x5Ad4FIISHsMBhsY4fIFiLPDhK/hyDkKCSIgQg6D4fEVwH8OIEMEINLhc304DSA3j39/9RP5WJUgCDAkDOIHwa0zgaIzB0CWOCPgSYEkUE9cLEZwJLP5za5k30ad93+15O++PRvjth08z//4luKBgJY8OAvn9hz4R9tWHtcK8S8nJnF/wbaL2qOCiVFFi9EJErtLUGRyT2MWrOVnItu0xGJ5nl+OWYmGNNjhzCiX87sUe8bh1VGIU0lFCIRqWHo/aeyb1sOW9NGR94wwGIR1vg3K88EUXT0icc9TW4M3pdAkQf6/oa3GGUOyJhr0HuicpKBWeUHXpEXazekW4PAmtyl0tOC8FHrZLbmluncrc/YpYMBkJz43YWEY27JSSGNiCrV68N0Uq3T0kuQ8QTs0BjYm2FCzlLVbgmqipjdjdppQT5MyhOyLjRCiSpN1RaZmh25aq2ll8xuUcm6Gqomh4R2friPMhEjsEtJlBUZ60AnpaclIc8aNWb8sjP21X7CnqcyOx8LKoZhybtfToL4msXG8mGTr3bZPbglIfKOfEJflcBMLbOSSZPULex/J66xKXRW7UGYWSvd4TB1fYWrRCz0tIViay7DiTTtOpS4XPeEpq5NHwwkUf3cYbSDRRsUbTSpOc4BN1rI3brTzbZEtxtH+JkHqxsxCRpqVZ0TE9yVM6UdYisCpcJJJTyE9IpryOq21LCpG+Vc6O0/TNXHTu/OjViX0uAA08U5kZTPrhpM40FLrxXCBHLDUX2l3VIcvP6fV2VCoZXcr+FI6KN1owhD4HglYdf2Q3sdUCi6fItpXCNcKH1UFYQ2t7CklkrJjrs0EJk8lsSM7utHDJ1WGNrpJL2ZWn6gO1Qlib1hl9DtHIknrYPacaLgTPldhUcjuigrlMk66Z60VyyRXn2/jIvwjrRXYUVWEIJ6lkJ0/QCaHyOvSgaVDmcAWFCQnRcctIdcHCHe9fZDlMjpBoo2Lv9k3OceaaQh0WW5B9Ki6x1Xrkqt2PsRMIo5KcKji6MZ6z7ic5gceEX5HwZmH6iWTJ6FXqC8sjDpu71KpRYrZoZRjpupFERH1PwtEgGQ53u9taaW3MnyDEa+Nic7OoKMOGbK+ZeU5fwn1JGvcIAIfz8ah3Y3c+xg0nwwLlDpJyq5VOHXqyaIWUDzI9D7AWpcl6S0WlUoR1RmZSO57mCjEBeAKCPxqJFSINrpGcEWrF80g4g5z2Fls8VdXMM2biu0ZMVHdqSQLiKTf2A8lxebLMoCEhp5RvoJRmIyXlL45M3Lkny2OC1Ok8ZJfajT2TCkZbKR8npIm1geqnFZEa+uwqMtkpGjI7p03UexUmH1v9gib1GK0rRtEjmSzhWnZPVNRxknYZZ0wDh5qYGp39oJ/meyoZLH+m9Xx/XNAGiRFeQbPHzhMpD3vIjW5lpMO5hfWGafE9wnN75c5MT5Tzj4NBKYteRLx7nLNMKQZMheKLPboZwbSKgoc3BF7K9CjXS8EqmSRwDqRV1j6vCshGCiEGXMWxe1buvVjP3EmWxY1ng5s+yvGiyQKElUMaWIzpKkfpGiBxndOw/1yRes+QE1ufj2R+sx43IpZ0y0RP9Vlj5u2keuccZrZGMkjqRUwwIZ1EczOeL+LRlsou47Kxd6Wg3Kl+vlI2xqKOq61Cau2X2R1PZ69CSlL0VJJkrNVhXqxuwRMEWSf5uqDCmRPx4EQ4VxJ73qFkwMjNvjY4Z0DxrBei1p7TAomk6UzWi/KAtibwlmv5gINcAqVhbAM5n6D2ktHNOPdRM9rP85nhruqcBCSB1m7LmXqEssq8xuWAIZfSlBRbkxiUHloqOsLQjc+yuhY1+CEz49E5RyUdqTjz7ChNZOLraYgIrEg73M+qzlZlFZFJghMYeiKLh/183jtReLBGOylE/+pLyXAupigzwcmAgtnAbJOg0IeIqshDMWbZvgmWwp7QVrrNnrbSdo2cyJVnbhHFW4Jy7oRzKlNa/xzuUCq0wUAzKNfSkdkVuUCkDE/YPk1H0CKVY6kf/eYhVOVWalp+r2GsV5go1Wn+QrqotZ5hUh3TjdB1PeYIQl3S8ZjFoqLuA31ZfISCliu0oLSkB22kyg/i1pfhea46SN5272rhU+ZSLW3r2TUinqRN9i56Sgt9UZPGoULsTulbqtFWhUonNw5d0xWJBjVJvckD1ciWa48H3rjenjvC3MoNG5zuNPlEfm8tk7Rit0AH0lSDtpnZ9XJ72cU+MAlNCvp8yjMa42WSWyw+hdCYRm/oNY1VXCStrrnsrxPRnuu5ZGwHw4m4YZaupDJ+gU60qDsZxJ+zV6QIngb3rGSe1IdxL6lW8d02JdQbFPK4/Ojoirs4+zai9Q6Jz4WgzslluvEONXoQy0nTTBa6raFQw0n+1pMzQanopVUeUTTw1kPfu2W04Z2UgybBKF0FbReihTnbppaNBLyHxXp5z81rWVAGv7YGAFRGb7lvpvmOPl2n2sMzLduFsHmOriY7n7nOBd+aLrJx2dYbujjpSWpH6BjlJ+YEnaO8zlc+ba2TVMClzB5xUUwqS21PWRBGA2vhN8KdUQmJwnTEMNgwzhV8LV/aM4mfSS5hEkIK2saktEXam++pp5GgWT0KOBLeJ9nKHF0shc6LNNyKOqEaSVEa0/SC8tKz9f2zGT9DjUw383GcCty/oog69T7KqPM5QitJWE96xHDnxYbEK5Mjs3tbkMUJVVfUepBTQo/ORwuyarFPbImbIUzVLRD30k5F/qSqVuua0jWa0uqW9uI0UPjxGUcrwjAXHcbc8wtKXGNB5cnpjhQC5tNiY7uHUIzqcruUlnm9d2uqmz7UbuTFaFWxkrLO8IVj13gQslhZNQezudye4+lqUfPxBGc9FK8Nwz2w6SQECR8aOxdYnmccxfVh9HNFC1v6jB+6rj69opXv2vU2kcdM7/z75Ublt6B9hbv6EJ+A2I58KU7svbpQej6d7hbFXFbJt8Sc4AyWKyV4kWfSBkJXauj50hHh2aVxExIFOaQkNSgaZrN1qXfcMqBlwT67QcYnyA3wxahTpDKekDYqOcokXpZOWSSUOsL9tAdhEckS0m+3zS/Dzh1qvRIMgqIoutSLC/2yM4lbIR4mFdCmoBkzUElrnDfhmisNkxsGHJ6pl08xwvCEmFlL3Nvo2dGSsS83pViFdYjz41IWda76R2TtzojiQ6Gl8q5dXG5kaebIVq73Hk/VIiZ0Q9ND55gnS2vE7RX2pPqReF53gmWstBqldo6TuJ1R1k+DbCaywib2HHCpB5tOjjk2D9PWcDNXzJCE891WUHFklv36ulF2n2LEY9WDyCBvYa3HcypAHMn1rYfDWGPYck3ipXhq4+dMum1VcDnEet5K82gbhDjVUC2aYhlmHs2Tr2i0HyPwLqNkoUru7VZd0aB6Lcoq7HnLufaxWeljTs/oeX5FGZ2aUnAqZ/S+NsSw3zaqPioG/7B4bw2HhaNLBFmTF9GkLNvTA00q1kOp1bkZmpnGXzbpvfJ1BRVDZFZj43HKuDZX+2W2HLKO9XqXcaUXiONsti9Ic/QOHvAB0a9uHS1jLN6crDNFc6kvr96sXHdOM8qYK1VoxD1G4aA/Zk3DHFUrOmrUksipum5Rg/MFtJ5yWnk8L10hwnAfik44SsH+YpuGakLjxjHWIJ4pe1IxYXnQrzByvON5auBjXtzMkkfOc5D2GHSfHSc/u3cvu9TL62UNrX+rdcJNRgaabxuBIKg787jkICihXZhZvWCzOLTjct1784LjcRkJjX7iEpGKivvZX+qXfC/wMwhHs1FbgAWLx17bI7EKgUx3lOwML9LpGEo9lxwhJcHRyuqN9HBAfEzAru9KIo7TYiM3UTzezjjkyiGsMULmh+517MpNxuLSZE/UZXJ0GfXO+MUGfSutLS5uAawaQobZ1Wl+dOTloj7uWsx2vCSddda8hOrmapA2jGUzEHPg0PMpQEdjxi7RUdbSHIlOMUiX67Tf7hju314SeadQ2ZG6az3fjwFmRbiznZAYckxqeXY4UGXuT0T3uCebR54N10P1560AJ6yxKlcjv8Pj7TbUtxWbk/lRFqdWs6tEtKFNNEBhyouBRS2CVXaPnG5sIFuFLJTp1BA10mjb3M87HPpHTx1jFgmI3QvvCeXA6uK8wkczGPvx6h6LuXl5OCSPCp4ETn6aAmHiCE1lZ5MQVboRUma/M2jZcBfBYzk4q/CRqAuBWQK+W6K5D46qtF3UFYoLzi9AjyIwCaOQSHNPbe3Rbt6tLs3LCyeuT19U3d70AqjrI2K6YJXuUnS96PoNA3EhY2O6hynRB4tJl5J8JRhy6keLlDqLdkDvBA0crTL+gDCmczUhZ6nspyMQD900ylfR4dCDIZZ2OcMmjcvlnVX4aDoBJZPJgkJHiwxF0NHbpqO+buklmEUlZ0Dl8DhyQWPsRYuHBPGY8Ds9zDfSIWPEIZFzQy614KXMuD/1x3lc1rPNUGi/0Ge/ePU6SYitcn0K3NURtFgM4ZYdq5Ce4IF8IhSTQInqn6v9fC+8U2Pp3HHXUzptHzRLkl6+2pb2cK2efVkI5niKvLovRiib+XV+UdvxtOKPcbsKr4uzuLCLwE6RPBFnT57B+HDTPSbObD771+D1QM8PHDk7t8BzlKjoz1aMLYHfU8Q0eZx4cq4JqwfEa1CRc97fZzBnwkmzXm9jcHlenpxbIND0rksPR62e13NKPMy7Go1ZuuSP6ca5O8U+t0fMjPF21qBt1GWHOAZSjZ3xXqtFxsqQAoa8xVUaUk51QcQ0lB8NHJUuLofqF5ltY5+DwrGX+n0D/VN0axC4PsrqLpSkfN8qXVwlcTJa/HUNzJViH8xwdoZclGydM+5k24OeCGNxnQDqvIZCN7DaHfHorMOpDB4JZJqOTOC8SsqtcmjE4VCKZ8Rs56HmnBd010MRDgRjhIW1zh1FvpSPbHB7eFAgqSiY8WwERE40Fbrf2nu6hETEHVe6tv2l8N36tfAW7WUEqFkKfnQEz41T6x7Ki6dy7BJUhUsVAgGSa/LHLGr1wYgH9yVUFH7uODA/2a/Fiq8rBT+vBopmeYbc3UnrdP9U5koUqde7con927Mhoa7y+IoTppUmGJvtjieSOPqhxaRXvpt6ViFfJ484zRhpdP6uWiX07I5Nz1ZoeOcem1+spKu9quf2LIJIhEDDsVRcKooaRuovGaJmrDrVbOMqlHTJckN/iGTCt9dx9nI3Oi++YWt2/Bq3WzRv/tOGVS932gQ+I+ljCFzPuJjHY/Kw7dSxWMq7tBzI8C3vhIbKxbvrJeMRqyonEaB1hBJebZrrRS6DTdyuebHCCO/tbWlRvRQa8U6S93s6wSZvVM1reLWvFMwavcgW/SoNDUTHWCyAcu7prx41c+72QBvhTudyqyyjyTqc350M8p511/4eqd0VYY5nzeIHSZNerR9UlG11/iNYxmGASo9o4QECGyHqtk/okSWz465O5Ys4IheIPm7uQj/JQdnpZ46cpaMq3q+Sh+fzA+ebPCxDi8V8R0yUMeIfgfRQwlbLhppYbPxMiVW3haJhu6xibMrrGfvXp9ys1t3EbO5h2mku8s1Eb5n71J7dnbI5Mwv0c14cHYf1CTvwWAnjnrJ4oSpC3kIjEGlsgJ8PdCjooTvei7ucR9HRGjO/NunervnrufaD+iKEQ2hfkqsz9va2LEtaPvjVBrOrCLhlU8SXJO/a5MZcNmy5FDP2WUxu1vUV0zwV1Y7mSPOGQy9Pv8OB9nIv7OnpeDZGiM5rrPyUr2/GVDh3exKqJ2fT0LBgd3KkF/u51JrSh7CC9GUS1Og2OY/2IRCTJlgGCvnOSfewcZnFkWBrUDyWB3kUn0dNeUyzIQ7+HI55XYGc6RW1G+aTMj1PyZ0cZq4XWqzRwrsYvxTWftTso07Xtbr3smw+Cq187cY8jsek1lSMoo87LnPRCStr6az14zLwNKVz6hht8Zm6HMdwxecFcS5sS7lFclZ3Nb3O9CkBfpAERp54m/FRioYrRVTzOwqzTnwdysdtLclqzk/BXAQb6G1fj1z0GR2mCM/fHQ7wXE+xV5nqogqnDdNjjOb5vI20wW3kqZBijh1IGHqJt3THxPsuP65VmPoN/4qTUncfmylBvomZc7UhHIRsgnwuh7O218PDn+DwUWc0oBWVDFZLQDXLeBpVJw93GrGfRFT5sF1EmRhPL5odycHV2B55vtxV9ZcO0zNeeOgiSKxMEG3pdIy8Wu/Yijna01Ds8lD2IXNj6lA1X+3QS2cp3R8nV+L26hLGyCXtSlXsb3exUPiTvRwZoyIvxH5ZKbyFTe12P0avdKFGR9XmmSCltPdW7bnfXvv19oL5SsReVRhReEUeJf7ZB0VvP315p8bd6i/oPUgW70RVLntlTkOmCeRyF1+7brzYGLpcyysBSw/QRtwYVxi0zRAoCbdiTQkA+8oQY3WO0KIeVd33nhfRYg+hqhSSqe7hRAoKHDTgGJK5dfr+ffWZeUzNPigzjneNSiEGXVztu0jUj5tMF0/Sa+2h8fUrJ2rdi39dTOOVIbU7dVkz84SzXmxQyfIRIUH1vJ43bwqqi2FnV7eTbX+yaoEs7ZpIhfzYnEx5LjNV62HZodBNcV7DcoKcJMH4/HRlXidoacgXEigi6aYPk/WN+tEJZZHHlJtwntYUCwnbDjagJ5BednBSdMqDScDjtXnpkEzc0/pmkQ9ZCd2IgiMnEhVMze6NHJ5ZihjvIkV7OfRc8WZau2xa1sJ8TWQRdGm30t1M71xrY1HcwpQfy8F6Kx6kXUUXliJRvtGblbnMJIVIzY7CqK32FyuuzRDnrieevT1tTDmn9FG4Oyz1yC9N7ctao6eUb75gpG2hOd+VmONkqEmB2aNDrVYoSBKW2RpoPjzhpFzqUyIW2e5GQxVEOQ8kIzWYeofsCHHOyMGa7BIVZ14okcbb4JhA05J1EbsKDVdnLElJES49sQgKGGzLx9sdiWlvep0UWEpfnEMxYsItBuHqN8gIOY1LshDl8Od14zXzqkZbi4EhnrKp7XSb5gp3/X3jHF6Edl6UT+xd8cSNvIiN2qXDYywkxZ0aT6Itzau1KY5edYHbkK8U3G3hWjPU6AvvEseVYItYeSgr5LjBiricPDnYA+HxNlFBIWy2BwWbe8Q+RnrgjhRooveB7Wo4HeLXC8n5uwOEkKV3hhddiCOaE7L6GZKGALrqZQ+lSkOW3euzfjw+kL1o1oeoHjFpDjl+ur3u4XI+GesR3y8XNoc0Jl5PCBISg2sUui2kSo6M16xcBxVXdiqsCqzK1hReZVWjw3vG8RRnKuP2cl4r34gZ1qTdeKScy5JLFZmr18ilkZmzyeVkUnx+RDfXuSkepuIXwoxIZVWdRIqgs/CIQoQvd584gkZXenoqYkb2IPcKOoJW+k4+WY/B2NBP0RdcPqMzthPn7ITt0bFOELRtlpBaTDJ5ZAIiVMmDFKpgqhYxjBh7D5tAvGdxASb8O08+oQRNhH4b2KGuIr47Ec68ocLFftC39MhnxyfLBMokdLxyHytWkMKtfches7EGWWTQbgoNapEoDg+3JD+ppJBFhOn11kxLKFJKfofc7lNAEQ0nFn3TKf7NkoyR9MHEe4nclFrW+BI23Bm6+/PLskoLzyEwKnXyC8CwZ8lj6Vd3SM55pRefHFJnSZM0i1wwzp3sbUp+tg3oSwgYu4NqM9ntbNsYZgrcLueJ+eRmtUloA360QsZzT9i57LE1X+kZTtmX7OJYO2mvYQq54UkMSu9zl7IWqPMcUaqbCDVdCrgl3+JWv9M4wGMzXS2f8lBvtVtbMiJUzKRb/jL6C6fnLdU1pXadw4Hy0ttDMVpEHl/b6AKre7IXj5YZv7QnzZrHQHmJazzyoWLtnqTQlbw3TaSfVDC/q/Zqc4Kuiqvhavhoc1x1WzZIhdpbsyMGn4xgzkva68lwIW22qedYdv3ZPl2Eqk4rLfTDHANNg1XJL27DGDDkL9Vt8js/MBRqLJCkRAHQbGG8MqC+r7NTSaVYI2Yjab75RHRSKchNPt5v+7ONEU6j6JZWzoF4EeU1O7t3mFu7iUIDoaGv29C8mOse4sfH5aVXKWfH0RyjDpgP7m4qrtQTzLmiMi/7kcwYdOYBfAs3bvSB3msxF0RPwsMb80DYzOq3sOvz/qmO4YscyEn1L/vDmfzIfVg1J2kpSpOQojbeSLhFJzJbRh+5vlEkT61phbt6iH1f5Hs8dhlRtssrwLEG9hayroOL0DtohfowveA1W1juWYLEhU0ThG7FJNwnFrsx+mIzxrJgllGCSexpFfHxMvg3hjZX1LTjIxtd+RUWNYdnmUenp3okKGA6ZuD9fqUTeZ3du+kmJwvldZ597cRzsIqrdLlSsh+f6XpXT3lPGhC3LeP4urKts9aw3PPVQmJXAcTqNNxDg+jztb0Yr7F/9HBaD1YVUy8wj7umLckKFWhHLpWvjVHOvl1vqNM7cHasWjDVwNeR2cTxeR1YLbWtMxFW/pQUnW9IlyivXA/qO4TgMFhFhOTq3brMcmtXce6Ro7jPonOx591uk6RHzqk055qJFVFo3iNMSUnlsQRFKcZ6yT8WYr4tce4MZUyKy6oW5n4ajoIWZvjR2AehZ6PJpSq99y2cUrXQwSVtty8XXZrpib30gePLhDejiaudnVPO25k/hBvjBaDl6EZ5ubThWhdXfprLOQV9BrOq+xVvySEPxUi81qdptRsRL/JTor8MYeQ51AP4HYjiXPGtyKqmQZOEfPPii8m/4LTpTaWMZdqIeT1WySFKJmttUnjRRF/ClfFRad3GCISQPQVIwO+CYNzqooJKJkwlOdspc7OUYbuf4Mlv/VJcQhwC7cb0rIMmwPPgIlrXlAqLqyM/XDJcg9CJmEfzpPir4T3iIe8WZEAWonMVUc9v/tXKglJrW/HcMRZSV7qlyaZJZ1hRdFGEPfdd0/yQveR0aNNdmoUFVF7WReU3jHJ77urAlUk+TeGeF8F+J8zjzZlOjdnwOpZaoAWlaDeNTUNSAYlFXs6OVdVnGUMq81V1ESd9ch1rrgq5tqVxra6EtweDhvFsmUklm4loDlIvvDdOcT1hd8Zj3atHOApsrLCFaaq6Za/WdKhLlT3XoB/zrnh0rowMrZ7Ya0Y+xJ0ntfDUzt6xk0b8JUjRqyThDaEgVFC8tdXOCGdrBJhCGs3xC8ULBpd0zwYxm30vRk8uKdeIdISky2uSzNRFu5cgFWKoj3JXwqCH0FTPRoRiSeOb+9g8sDTg0N3dVl+sHiJ0RCxyl3UbZpSpgvx43JUh4rDM0bCVah5kovslyze4Qy9aQnHsVCqSicsr00QSRWWv0/E8LTI1HmF/kHIWShikRoWVjrabT9bijEbO836i5YrGhDD3mNsDAJJn4aWoJI5ikcqkEZVUCMmV71BXdXXb3u2rYqTu7bhN3jIJ92q02BsYW6aup8VkZGOj22qtm1KpmyoAXprRL47TL09IQ9yrTT/T5dqSDPKouxb0YLO+YHNLMHSTI+bASle8s1FIQqtphxozQ7ehZBAFMW+sRaWvlNxvmlvOgqGT+UQ1c/JwbP+I50vOeMR4CqNjtazc02P629pZKH41RHy51QSjtUT3asj7XZmimGDp5lXxL8alimVujBONtkLE2w5FUeaxomxVwCD66oJpJZvaS7/clPD0XAWfkSI1QiDiddaVOSF4aX6JHS4XOBtq6xJpzfEcNS3akfDFQ3Op84rLrYf5pXOC6/TqMK/ScyWc8uO1HvfhSG/+0Z/kerpfIgeKOvGCxDlzyVyZbdCHKEU3sVxC8thcqaG1uQ1fE5Ik/+PLL1/e9w8/78j9n6//v69S/f92o+v75at2ft8iDuP33bU+9qNfP8769b/Q4X/88qUP87cGH7fThmpKf1zq+nd3077+EPX1n+6mDdv3m/NtM8br+OOO4Oin7z8b+hIgwXvN+xro+2rgv9n/voH5FSif9vEwfN7Ve9/mG/NweCv48SccH5fp4G9vNf/xvwBQkkT7STUAAA== -->
