---
name: "rar-aibast-agents-library-deal-tracking"
description: "Reports pipeline snapshots, deal movement, stage velocity, and forecast accuracy from built-in demo CRM data."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/deal_tracking", "rar_sha256": "3d5f5bb65818acd562853d85c7e8e57a392689a99b1e8360d4f08ba56c4d0a73", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "AIBAST", "tags": ["b2b", "sales", "deal-tracking", "pipeline", "forecasting"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/deal_tracking`. The original RAPP
agent is preserved byte-for-byte in `deal_tracking_agent.py` and in the RCI capsule.

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

Deal Tracking Agent

Tracks pipeline snapshots, deal stage movement, stage velocity metrics,
and forecast accuracy for enterprise B2B sales. Provides real-time
visibility into deal health and progression patterns.

Where a real deployment would call CRM and forecasting APIs, this agent
uses a synthetic data layer so it runs anywhere without credentials.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The tracking operation to perform",
      "enum": [
        "pipeline_snapshot",
        "deal_movement",
        "stage_velocity",
        "forecast_accuracy"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `deal_tracking_agent.py` and embedded as the fenced Python below (sha256 3d5f5bb65818acd5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `deal_tracking_agent.py` first:

```bash
python3 deal_tracking_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 deal_tracking_agent.py   # or on stdin
python3 deal_tracking_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Deal Tracking Agent

Tracks pipeline snapshots, deal stage movement, stage velocity metrics,
and forecast accuracy for enterprise B2B sales. Provides real-time
visibility into deal health and progression patterns.

Where a real deployment would call CRM and forecasting APIs, this agent
uses a synthetic data layer so it runs anywhere without credentials.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
from datetime import datetime, timedelta

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/deal_tracking",
    "version": "1.0.1",
    "display_name": "Deal Tracking",
    "description": "Reports pipeline snapshots, deal movement, stage velocity, and forecast accuracy from built-in demo CRM data.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "deal-tracking", "pipeline", "forecasting"],
    "category": "b2b_sales",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# SYNTHETIC DATA LAYER
# ═══════════════════════════════════════════════════════════════

_DEALS = {
    "deal-001": {
        "name": "Acme Corporation - Platform Expansion",
        "account": "Acme Corporation", "owner": "Michael Torres",
        "amount": 2_400_000, "stage": "Proposal",
        "win_probability": 68, "close_date": "2025-04-05",
        "created": "2024-11-15", "days_open": 120,
        "stage_history": [
            {"stage": "Qualification", "entered": "2024-11-15", "exited": "2024-12-10", "days": 25},
            {"stage": "Discovery", "entered": "2024-12-10", "exited": "2025-01-15", "days": 36},
            {"stage": "Solution Design", "entered": "2025-01-15", "exited": "2025-02-08", "days": 24},
            {"stage": "Proposal", "entered": "2025-02-08", "exited": None, "days": 34},
        ],
        "next_steps": "Executive meeting scheduled, pending CTO intro",
        "risk_flags": ["Competitor pricing pressure", "No CTO relationship"],
    },
    "deal-002": {
        "name": "Contoso Ltd - Renewal + Expansion",
        "account": "Contoso Ltd", "owner": "Michael Torres",
        "amount": 1_100_000, "stage": "Negotiation",
        "win_probability": 82, "close_date": "2025-03-31",
        "created": "2024-10-01", "days_open": 165,
        "stage_history": [
            {"stage": "Qualification", "entered": "2024-10-01", "exited": "2024-10-20", "days": 19},
            {"stage": "Discovery", "entered": "2024-10-20", "exited": "2024-11-28", "days": 39},
            {"stage": "Solution Design", "entered": "2024-11-28", "exited": "2025-01-10", "days": 43},
            {"stage": "Proposal", "entered": "2025-01-10", "exited": "2025-03-02", "days": 51},
            {"stage": "Negotiation", "entered": "2025-03-02", "exited": None, "days": 12},
        ],
        "next_steps": "Legal review of contract terms, pricing finalization",
        "risk_flags": ["CFO budget cautious"],
    },
    "deal-003": {
        "name": "Fabrikam Industries - Analytics Suite",
        "account": "Fabrikam Industries", "owner": "Michael Torres",
        "amount": 890_000, "stage": "Discovery",
        "win_probability": 45, "close_date": "2025-06-30",
        "created": "2025-01-20", "days_open": 53,
        "stage_history": [
            {"stage": "Qualification", "entered": "2025-01-20", "exited": "2025-02-05", "days": 16},
            {"stage": "Discovery", "entered": "2025-02-05", "exited": None, "days": 37},
        ],
        "next_steps": "Workshop with VP IT, stakeholder mapping",
        "risk_flags": ["New VP IT decision maker", "Low-cost competitor"],
    },
    "deal-004": {
        "name": "Northwind Traders - E-commerce Platform",
        "account": "Northwind Traders", "owner": "Michael Torres",
        "amount": 540_000, "stage": "Qualification",
        "win_probability": 25, "close_date": "2025-07-31",
        "created": "2025-03-05", "days_open": 9,
        "stage_history": [
            {"stage": "Qualification", "entered": "2025-03-05", "exited": None, "days": 9},
        ],
        "next_steps": "Schedule discovery call, research account",
        "risk_flags": ["No existing relationship", "Greenfield account"],
    },
    "deal-005": {
        "name": "Acme Corporation - Support Tier Upgrade",
        "account": "Acme Corporation", "owner": "Sarah Kim",
        "amount": 180_000, "stage": "Closed Won",
        "win_probability": 100, "close_date": "2025-02-28",
        "created": "2025-01-05", "days_open": 54,
        "stage_history": [
            {"stage": "Qualification", "entered": "2025-01-05", "exited": "2025-01-12", "days": 7},
            {"stage": "Proposal", "entered": "2025-01-12", "exited": "2025-02-15", "days": 34},
            {"stage": "Negotiation", "entered": "2025-02-15", "exited": "2025-02-28", "days": 13},
            {"stage": "Closed Won", "entered": "2025-02-28", "exited": None, "days": 0},
        ],
        "next_steps": "Implementation kickoff",
        "risk_flags": [],
    },
}

_STAGE_BENCHMARKS = {
    "Qualification": {"avg_days": 18, "conversion_rate": 0.72, "target_days": 14},
    "Discovery": {"avg_days": 32, "conversion_rate": 0.65, "target_days": 28},
    "Solution Design": {"avg_days": 28, "conversion_rate": 0.78, "target_days": 21},
    "Proposal": {"avg_days": 25, "conversion_rate": 0.70, "target_days": 21},
    "Negotiation": {"avg_days": 18, "conversion_rate": 0.85, "target_days": 14},
}

_FORECAST_HISTORY = {
    "2025-Q1": {
        "forecast_date": "2025-01-15", "target": 2_500_000,
        "committed": 1_800_000, "best_case": 2_900_000, "pipeline": 4_200_000,
        "actual_to_date": 2_100_000, "accuracy_committed": 0.86, "accuracy_best_case": 0.72,
    },
    "2025-Q2": {
        "forecast_date": "2025-03-10", "target": 3_000_000,
        "committed": 1_100_000, "best_case": 3_500_000, "pipeline": 5_830_000,
        "actual_to_date": 0, "accuracy_committed": None, "accuracy_best_case": None,
    },
}

_PIPELINE_SNAPSHOTS = {
    "2025-03-01": {"total": 5_110_000, "qualification": 540_000, "discovery": 890_000, "solution_design": 0, "proposal": 2_580_000, "negotiation": 1_100_000},
    "2025-03-07": {"total": 5_110_000, "qualification": 540_000, "discovery": 890_000, "solution_design": 0, "proposal": 2_580_000, "negotiation": 1_100_000},
    "2025-03-14": {"total": 4_930_000, "qualification": 540_000, "discovery": 890_000, "solution_design": 0, "proposal": 2_400_000, "negotiation": 1_100_000},
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _weighted_pipeline(deals):
    """Calculate probability-weighted pipeline value."""
    return sum(d["amount"] * d["win_probability"] / 100 for d in deals if d["stage"] not in ("Closed Won", "Closed Lost"))


def _stage_velocity(deal):
    """Get current stage days vs benchmark."""
    current = deal["stage_history"][-1] if deal["stage_history"] else None
    if not current or current["stage"] not in _STAGE_BENCHMARKS:
        return None, None, None
    bench = _STAGE_BENCHMARKS[current["stage"]]
    days = current["days"]
    status = "On track" if days <= bench["target_days"] else "Slow" if days <= bench["avg_days"] * 1.5 else "Stalled"
    return days, bench["avg_days"], status


def _pipeline_change(snap1_key, snap2_key):
    """Calculate pipeline change between two snapshots."""
    s1 = _PIPELINE_SNAPSHOTS.get(snap1_key, {})
    s2 = _PIPELINE_SNAPSHOTS.get(snap2_key, {})
    if not s1 or not s2:
        return 0
    return s2.get("total", 0) - s1.get("total", 0)


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class DealTrackingAgent(BasicAgent):
    """
    Tracks deal pipeline and progression metrics.

    Operations:
        pipeline_snapshot  - current pipeline state
        deal_movement      - deal stage transitions and trends
        stage_velocity     - stage duration vs benchmarks
        forecast_accuracy  - forecast vs actual comparison
    """

    def __init__(self):
        self.name = "DealTrackingAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "pipeline_snapshot", "deal_movement",
                            "stage_velocity", "forecast_accuracy",
                        ],
                        "description": "The tracking operation to perform",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "pipeline_snapshot")
        dispatch = {
            "pipeline_snapshot": self._pipeline_snapshot,
            "deal_movement": self._deal_movement,
            "stage_velocity": self._stage_velocity,
            "forecast_accuracy": self._forecast_accuracy,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"**Error:** Unknown operation `{op}`."
        return handler()

    # ── pipeline_snapshot ─────────────────────────────────────
    def _pipeline_snapshot(self):
        active_deals = [d for d in _DEALS.values() if d["stage"] not in ("Closed Won", "Closed Lost")]
        total_value = sum(d["amount"] for d in active_deals)
        weighted = _weighted_pipeline(active_deals)
        deal_count = len(active_deals)

        deal_rows = ""
        for d in sorted(active_deals, key=lambda x: x["amount"], reverse=True):
            deal_rows += (
                f"| {d['name'][:40]} | {d['stage']} | ${d['amount']:,} | "
                f"{d['win_probability']}% | {d['close_date']} | {d['owner']} |\n"
            )

        # Stage summary
        stage_totals = {}
        for d in active_deals:
            s = d["stage"]
            if s not in stage_totals:
                stage_totals[s] = {"count": 0, "value": 0}
            stage_totals[s]["count"] += 1
            stage_totals[s]["value"] += d["amount"]

        stage_rows = ""
        for stage in ["Qualification", "Discovery", "Solution Design", "Proposal", "Negotiation"]:
            data = stage_totals.get(stage, {"count": 0, "value": 0})
            if data["count"] > 0:
                stage_rows += f"| {stage} | {data['count']} | ${data['value']:,} |\n"

        change = _pipeline_change("2025-03-01", "2025-03-14")
        change_str = f"+${change:,}" if change >= 0 else f"-${abs(change):,}"

        return (
            f"**Pipeline Snapshot**\n\n"
            f"| Metric | Value |\n|---|---|\n"
            f"| Total Pipeline | ${total_value:,} |\n"
            f"| Weighted Pipeline | ${int(weighted):,} |\n"
            f"| Active Deals | {deal_count} |\n"
            f"| 14-Day Change | {change_str} |\n\n"
            f"**Deals:**\n\n"
            f"| Deal | Stage | Amount | Probability | Close Date | Owner |\n|---|---|---|---|---|---|\n"
            f"{deal_rows}\n"
            f"**By Stage:**\n\n"
            f"| Stage | Deals | Value |\n|---|---|---|\n"
            f"{stage_rows}\n"
            f"Source: [CRM Pipeline + Deal Intelligence]\n"
            f"Agents: DealTrackingAgent"
        )

    # ── deal_movement ─────────────────────────────────────────
    def _deal_movement(self):
        output = f"**Deal Movement Analysis**\n\n"

        for deal_id, d in _DEALS.items():
            if d["stage"] in ("Closed Won", "Closed Lost"):
                continue

            history_rows = ""
            for h in d["stage_history"]:
                status = "Current" if h["exited"] is None else f"Completed ({h['days']}d)"
                bench = _STAGE_BENCHMARKS.get(h["stage"], {})
                vs_bench = ""
                if bench and h["exited"] is not None:
                    vs_bench = f" ({'on target' if h['days'] <= bench['target_days'] else 'over target'})"
                history_rows += f"| {h['stage']} | {h['entered']} | {h.get('exited', 'Current')} | {h['days']}d{vs_bench} | {status} |\n"

            risks = ", ".join(d["risk_flags"]) if d["risk_flags"] else "None"

            output += (
                f"---\n**{d['name']}** (${d['amount']:,})\n\n"
                f"| Stage | Entered | Exited | Duration | Status |\n|---|---|---|---|---|\n"
                f"{history_rows}\n"
                f"- Days open: {d['days_open']} | Win probability: {d['win_probability']}%\n"
                f"- Next steps: {d['next_steps']}\n"
                f"- Risk flags: {risks}\n\n"
            )

        output += (
            f"Source: [CRM Stage History + Deal Analytics]\n"
            f"Agents: DealTrackingAgent"
        )
        return output

    # ── stage_velocity ────────────────────────────────────────
    def _stage_velocity(self):
        bench_rows = ""
        for stage, bench in _STAGE_BENCHMARKS.items():
            bench_rows += (
                f"| {stage} | {bench['avg_days']}d | {bench['target_days']}d | "
                f"{bench['conversion_rate']:.0%} |\n"
            )

        deal_velocity_rows = ""
        for d in _DEALS.values():
            if d["stage"] in ("Closed Won", "Closed Lost"):
                continue
            days, avg, status = _stage_velocity(d)
            if days is not None:
                deal_velocity_rows += (
                    f"| {d['name'][:35]} | {d['stage']} | {days}d | "
                    f"{avg}d | {status} |\n"
                )

        # Deals at risk of stalling
        at_risk = []
        for d in _DEALS.values():
            days, avg, status = _stage_velocity(d)
            if status == "Slow" or status == "Stalled":
                at_risk.append(f"- {d['name']}: {days}d in {d['stage']} ({status})")

        at_risk_section = ""
        if at_risk:
            at_risk_section = "\n**Deals at Risk of Stalling:**\n" + "\n".join(at_risk) + "\n"

        return (
            f"**Stage Velocity Report**\n\n"
            f"**Benchmarks:**\n\n"
            f"| Stage | Avg Days | Target | Conversion |\n|---|---|---|---|\n"
            f"{bench_rows}\n"
            f"**Current Deal Velocity:**\n\n"
            f"| Deal | Stage | Days | Benchmark | Status |\n|---|---|---|---|---|\n"
            f"{deal_velocity_rows}"
            f"{at_risk_section}\n"
            f"**Recommendations:**\n"
            f"- Review deals exceeding target days in stage\n"
            f"- Schedule next-step meetings for slow-moving deals\n"
            f"- Verify buying committee engagement on stalled deals\n\n"
            f"Source: [CRM + Stage Analytics + Historical Benchmarks]\n"
            f"Agents: DealTrackingAgent"
        )

    # ── forecast_accuracy ─────────────────────────────────────
    def _forecast_accuracy(self):
        output = f"**Forecast Accuracy Report**\n\n"

        for quarter, f in _FORECAST_HISTORY.items():
            acc_committed = f"{f['accuracy_committed']:.0%}" if f["accuracy_committed"] is not None else "Pending"
            acc_best = f"{f['accuracy_best_case']:.0%}" if f["accuracy_best_case"] is not None else "Pending"

            output += (
                f"**{quarter}:**\n\n"
                f"| Metric | Value |\n|---|---|\n"
                f"| Forecast Date | {f['forecast_date']} |\n"
                f"| Target | ${f['target']:,} |\n"
                f"| Committed | ${f['committed']:,} |\n"
                f"| Best Case | ${f['best_case']:,} |\n"
                f"| Pipeline | ${f['pipeline']:,} |\n"
                f"| Actual to Date | ${f['actual_to_date']:,} |\n"
                f"| Committed Accuracy | {acc_committed} |\n"
                f"| Best Case Accuracy | {acc_best} |\n\n"
            )

        # Active deals forecast contribution
        active = [d for d in _DEALS.values() if d["stage"] not in ("Closed Won", "Closed Lost")]
        weighted = _weighted_pipeline(active)

        commit_deals = [d for d in active if d["win_probability"] >= 75]
        upside_deals = [d for d in active if 40 <= d["win_probability"] < 75]

        commit_value = sum(d["amount"] for d in commit_deals)
        upside_value = sum(d["amount"] for d in upside_deals)

        output += (
            f"**Current Quarter Forecast Build:**\n\n"
            f"| Category | Deals | Value | Weighted |\n|---|---|---|---|\n"
            f"| Commit (75%+) | {len(commit_deals)} | ${commit_value:,} | ${int(sum(d['amount'] * d['win_probability'] / 100 for d in commit_deals)):,} |\n"
            f"| Upside (40-74%) | {len(upside_deals)} | ${upside_value:,} | ${int(sum(d['amount'] * d['win_probability'] / 100 for d in upside_deals)):,} |\n"
            f"| Total Active | {len(active)} | ${sum(d['amount'] for d in active):,} | ${int(weighted):,} |\n\n"
            f"Source: [CRM Forecast + Deal History + Revenue Analytics]\n"
            f"Agents: DealTrackingAgent"
        )
        return output


if __name__ == "__main__":
    agent = DealTrackingAgent()
    for op in ["pipeline_snapshot", "deal_movement", "stage_velocity", "forecast_accuracy"]:
        print("=" * 60)
        print(agent.perform(operation=op))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
