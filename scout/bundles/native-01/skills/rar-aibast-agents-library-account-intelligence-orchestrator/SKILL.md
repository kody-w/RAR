---
name: "rar-aibast-agents-library-account-intelligence-orchestrator"
description: "Simulates a multi-agent pipeline for account intelligence briefings, with stage sequencing and status reports over built-in demo data."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/account_intelligence_orchestrator_agent", "rar_sha256": "d1ea6994c730d10e73f1687afe32c41b0ca8f233d19fc692ea572fda18bc2d1b", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "AIBAST", "tags": ["b2b", "sales", "orchestration", "pipeline", "account-intelligence"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/account_intelligence_orchestrator_agent`. The original RAPP
agent is preserved byte-for-byte in `account_intelligence_orchestrator_agent.py` and in the RCI capsule.

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

Account Intelligence Orchestrator

Coordinates multi-agent pipelines for enterprise account intelligence.
Manages stage sequencing, agent dispatch, timing estimates, and pipeline
status reporting across the account intelligence stack.

Where a real deployment would invoke sub-agents via an orchestration bus,
this agent uses a synthetic data layer so it runs anywhere without
credentials.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The orchestration operation to perform",
      "enum": [
        "orchestrate_briefing",
        "run_pipeline",
        "check_status",
        "generate_report"
      ],
      "type": "string"
    },
    "pipeline": {
      "description": "Pipeline key (full_briefing, quick_snapshot, competitive_deep_dive)",
      "type": "string"
    },
    "run_id": {
      "description": "Orchestration run ID for status checks",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `account_intelligence_orchestrator_agent.py` and embedded as the fenced Python below (sha256 d1ea6994c730d10e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `account_intelligence_orchestrator_agent.py` first:

```bash
python3 account_intelligence_orchestrator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 account_intelligence_orchestrator_agent.py   # or on stdin
python3 account_intelligence_orchestrator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Account Intelligence Orchestrator

Coordinates multi-agent pipelines for enterprise account intelligence.
Manages stage sequencing, agent dispatch, timing estimates, and pipeline
status reporting across the account intelligence stack.

Where a real deployment would invoke sub-agents via an orchestration bus,
this agent uses a synthetic data layer so it runs anywhere without
credentials.
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
    "name": "@aibast-agents-library/account_intelligence_orchestrator_agent",
    "version": "1.0.1",
    "display_name": "Account Intelligence Orchestrator",
    "description": "Simulates a multi-agent pipeline for account intelligence briefings, with stage sequencing and status reports over built-in demo data.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "orchestration", "pipeline", "account-intelligence"],
    "category": "b2b_sales",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# SYNTHETIC DATA LAYER
# ═══════════════════════════════════════════════════════════════

_PIPELINES = {
    "full_briefing": {
        "id": "pipe-001",
        "name": "Full Account Briefing",
        "stages": [
            {
                "stage": 1, "name": "Data Collection",
                "agents": ["AccountProfileAgent", "AccountHealthScoreAgent"],
                "avg_duration_sec": 4.2, "parallel": True,
            },
            {
                "stage": 2, "name": "Stakeholder Analysis",
                "agents": ["StakeholderMappingAgent", "EngagementTrackerAgent"],
                "avg_duration_sec": 6.8, "parallel": True,
            },
            {
                "stage": 3, "name": "Market Intelligence",
                "agents": ["CompetitiveIntelligenceAgent", "NewsMonitorAgent"],
                "avg_duration_sec": 5.1, "parallel": True,
            },
            {
                "stage": 4, "name": "Risk & Messaging",
                "agents": ["DealRiskAssessmentAgent", "ValueMessagingAgent"],
                "avg_duration_sec": 3.9, "parallel": True,
            },
            {
                "stage": 5, "name": "Briefing Assembly",
                "agents": ["BriefingDocumentAgent"],
                "avg_duration_sec": 2.3, "parallel": False,
            },
        ],
    },
    "quick_snapshot": {
        "id": "pipe-002",
        "name": "Quick Account Snapshot",
        "stages": [
            {
                "stage": 1, "name": "Core Data",
                "agents": ["AccountProfileAgent"],
                "avg_duration_sec": 3.1, "parallel": False,
            },
            {
                "stage": 2, "name": "Health Check",
                "agents": ["AccountHealthScoreAgent"],
                "avg_duration_sec": 2.4, "parallel": False,
            },
        ],
    },
    "competitive_deep_dive": {
        "id": "pipe-003",
        "name": "Competitive Deep Dive",
        "stages": [
            {
                "stage": 1, "name": "Competitor Scan",
                "agents": ["CompetitiveIntelligenceAgent", "NewsMonitorAgent"],
                "avg_duration_sec": 5.5, "parallel": True,
            },
            {
                "stage": 2, "name": "Win/Loss Analysis",
                "agents": ["WinLossAnalyzerAgent"],
                "avg_duration_sec": 4.7, "parallel": False,
            },
            {
                "stage": 3, "name": "Battlecard Generation",
                "agents": ["BattlecardGeneratorAgent"],
                "avg_duration_sec": 3.2, "parallel": False,
            },
        ],
    },
}

_ORCHESTRATION_RUNS = {
    "run-2001": {
        "pipeline": "full_briefing", "account": "Acme Corporation",
        "requested_by": "Michael Torres", "status": "completed",
        "started_at": "2025-03-14T09:12:00Z", "completed_at": "2025-03-14T09:12:22Z",
        "stages_completed": 5, "stages_total": 5,
        "agents_invoked": 9, "agents_succeeded": 9, "agents_failed": 0,
        "total_duration_sec": 22.3, "output_tokens": 4820,
    },
    "run-2002": {
        "pipeline": "quick_snapshot", "account": "Contoso Ltd",
        "requested_by": "Sarah Kim", "status": "completed",
        "started_at": "2025-03-14T10:05:00Z", "completed_at": "2025-03-14T10:05:06Z",
        "stages_completed": 2, "stages_total": 2,
        "agents_invoked": 2, "agents_succeeded": 2, "agents_failed": 0,
        "total_duration_sec": 5.5, "output_tokens": 1240,
    },
    "run-2003": {
        "pipeline": "full_briefing", "account": "Fabrikam Industries",
        "requested_by": "Michael Torres", "status": "running",
        "started_at": "2025-03-14T14:30:00Z", "completed_at": None,
        "stages_completed": 3, "stages_total": 5,
        "agents_invoked": 6, "agents_succeeded": 5, "agents_failed": 1,
        "total_duration_sec": 16.1, "output_tokens": 3100,
    },
    "run-2004": {
        "pipeline": "competitive_deep_dive", "account": "Northwind Traders",
        "requested_by": "Casey Brown", "status": "queued",
        "started_at": None, "completed_at": None,
        "stages_completed": 0, "stages_total": 3,
        "agents_invoked": 0, "agents_succeeded": 0, "agents_failed": 0,
        "total_duration_sec": 0, "output_tokens": 0,
    },
}

_AGENT_HEALTH = {
    "AccountProfileAgent": {"status": "healthy", "avg_latency_ms": 1120, "success_rate": 99.2, "last_invocation": "2025-03-14T14:30:02Z"},
    "AccountHealthScoreAgent": {"status": "healthy", "avg_latency_ms": 890, "success_rate": 98.7, "last_invocation": "2025-03-14T14:30:02Z"},
    "StakeholderMappingAgent": {"status": "healthy", "avg_latency_ms": 2340, "success_rate": 97.5, "last_invocation": "2025-03-14T14:30:09Z"},
    "EngagementTrackerAgent": {"status": "healthy", "avg_latency_ms": 1560, "success_rate": 99.1, "last_invocation": "2025-03-14T14:30:09Z"},
    "CompetitiveIntelligenceAgent": {"status": "degraded", "avg_latency_ms": 3450, "success_rate": 94.3, "last_invocation": "2025-03-14T14:30:15Z"},
    "NewsMonitorAgent": {"status": "healthy", "avg_latency_ms": 1890, "success_rate": 98.0, "last_invocation": "2025-03-14T14:30:15Z"},
    "DealRiskAssessmentAgent": {"status": "healthy", "avg_latency_ms": 1340, "success_rate": 99.4, "last_invocation": "2025-03-14T14:30:19Z"},
    "ValueMessagingAgent": {"status": "healthy", "avg_latency_ms": 1120, "success_rate": 99.6, "last_invocation": "2025-03-14T14:30:19Z"},
    "BriefingDocumentAgent": {"status": "healthy", "avg_latency_ms": 2100, "success_rate": 99.8, "last_invocation": "2025-03-14T09:12:22Z"},
    "WinLossAnalyzerAgent": {"status": "healthy", "avg_latency_ms": 2780, "success_rate": 97.9, "last_invocation": "2025-03-13T16:45:00Z"},
    "BattlecardGeneratorAgent": {"status": "healthy", "avg_latency_ms": 1950, "success_rate": 98.5, "last_invocation": "2025-03-13T16:49:00Z"},
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _estimate_duration(pipeline_key):
    """Compute estimated pipeline duration from stage timings."""
    pipe = _PIPELINES.get(pipeline_key)
    if not pipe:
        return 0.0
    return sum(s["avg_duration_sec"] for s in pipe["stages"])


def _total_agents_in_pipeline(pipeline_key):
    """Count unique agents across all stages."""
    pipe = _PIPELINES.get(pipeline_key)
    if not pipe:
        return 0
    agents = set()
    for stage in pipe["stages"]:
        agents.update(stage["agents"])
    return len(agents)


def _pipeline_health(pipeline_key):
    """Assess overall pipeline health from agent health data."""
    pipe = _PIPELINES.get(pipeline_key)
    if not pipe:
        return "unknown"
    agents = set()
    for stage in pipe["stages"]:
        agents.update(stage["agents"])
    statuses = [_AGENT_HEALTH.get(a, {}).get("status", "unknown") for a in agents]
    if all(s == "healthy" for s in statuses):
        return "healthy"
    if any(s == "down" for s in statuses):
        return "degraded"
    return "warning"


def _avg_success_rate(pipeline_key):
    """Average success rate across pipeline agents."""
    pipe = _PIPELINES.get(pipeline_key)
    if not pipe:
        return 0.0
    agents = set()
    for stage in pipe["stages"]:
        agents.update(stage["agents"])
    rates = [_AGENT_HEALTH.get(a, {}).get("success_rate", 0) for a in agents]
    return round(sum(rates) / max(len(rates), 1), 1)


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class AccountIntelligenceOrchestrator(BasicAgent):
    """
    Coordinates multi-agent pipelines for account intelligence.

    Operations:
        orchestrate_briefing - plan and describe a pipeline execution
        run_pipeline         - simulate running a pipeline with status
        check_status         - check status of orchestration runs
        generate_report      - full orchestration health and metrics report
    """

    def __init__(self):
        self.name = "AccountIntelligenceOrchestrator"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "orchestrate_briefing", "run_pipeline",
                            "check_status", "generate_report",
                        ],
                        "description": "The orchestration operation to perform",
                    },
                    "pipeline": {
                        "type": "string",
                        "description": "Pipeline key (full_briefing, quick_snapshot, competitive_deep_dive)",
                    },
                    "run_id": {
                        "type": "string",
                        "description": "Orchestration run ID for status checks",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "orchestrate_briefing")
        dispatch = {
            "orchestrate_briefing": self._orchestrate_briefing,
            "run_pipeline": self._run_pipeline,
            "check_status": self._check_status,
            "generate_report": self._generate_report,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"**Error:** Unknown operation `{op}`."
        return handler(**kwargs)

    # ── orchestrate_briefing ──────────────────────────────────
    def _orchestrate_briefing(self, **kwargs):
        pipeline_key = kwargs.get("pipeline", "full_briefing")
        pipe = _PIPELINES.get(pipeline_key)
        if not pipe:
            return f"**Error:** Pipeline `{pipeline_key}` not found. Available: {', '.join(_PIPELINES.keys())}"

        est = _estimate_duration(pipeline_key)
        agent_count = _total_agents_in_pipeline(pipeline_key)
        health = _pipeline_health(pipeline_key)

        stage_rows = ""
        for s in pipe["stages"]:
            mode = "Parallel" if s["parallel"] else "Sequential"
            agents = ", ".join(s["agents"])
            stage_rows += f"| {s['stage']} | {s['name']} | {agents} | {mode} | {s['avg_duration_sec']}s |\n"

        return (
            f"**Pipeline Execution Plan: {pipe['name']}**\n\n"
            f"| Property | Value |\n|---|---|\n"
            f"| Pipeline ID | {pipe['id']} |\n"
            f"| Total Stages | {len(pipe['stages'])} |\n"
            f"| Total Agents | {agent_count} |\n"
            f"| Est. Duration | {est:.1f}s |\n"
            f"| Pipeline Health | {health.title()} |\n"
            f"| Avg Success Rate | {_avg_success_rate(pipeline_key)}% |\n\n"
            f"**Stage Sequence:**\n\n"
            f"| Stage | Name | Agents | Mode | Avg Time |\n|---|---|---|---|---|\n"
            f"{stage_rows}\n"
            f"**Agent Readiness:**\n"
            + "".join(
                f"- {a}: {_AGENT_HEALTH[a]['status'].title()} "
                f"({_AGENT_HEALTH[a]['avg_latency_ms']}ms avg latency)\n"
                for s in pipe["stages"] for a in s["agents"] if a in _AGENT_HEALTH
            )
            + f"\nSource: [Orchestration Engine + Agent Registry]\n"
            f"Agents: AccountIntelligenceOrchestrator"
        )

    # ── run_pipeline ──────────────────────────────────────────
    def _run_pipeline(self, **kwargs):
        pipeline_key = kwargs.get("pipeline", "full_briefing")
        pipe = _PIPELINES.get(pipeline_key)
        if not pipe:
            return f"**Error:** Pipeline `{pipeline_key}` not found."

        est = _estimate_duration(pipeline_key)
        agent_count = _total_agents_in_pipeline(pipeline_key)

        stage_status = ""
        for i, s in enumerate(pipe["stages"]):
            if i < 3:
                icon = "DONE"
                dur = f"{s['avg_duration_sec']}s"
            elif i == 3:
                icon = "RUNNING"
                dur = "in progress"
            else:
                icon = "PENDING"
                dur = "waiting"
            stage_status += f"| {s['stage']} | {s['name']} | {icon} | {dur} |\n"

        completed_agents = sum(len(s["agents"]) for s in pipe["stages"][:3])
        running_agents = len(pipe["stages"][3]["agents"]) if len(pipe["stages"]) > 3 else 0

        return (
            f"**Pipeline Execution: {pipe['name']}**\n\n"
            f"| Property | Value |\n|---|---|\n"
            f"| Run ID | run-2005 |\n"
            f"| Status | Running |\n"
            f"| Progress | Stage 4 of {len(pipe['stages'])} |\n"
            f"| Agents Completed | {completed_agents}/{agent_count} |\n"
            f"| Agents Running | {running_agents} |\n"
            f"| Elapsed Time | {sum(s['avg_duration_sec'] for s in pipe['stages'][:3]):.1f}s |\n"
            f"| Est. Remaining | {sum(s['avg_duration_sec'] for s in pipe['stages'][3:]):.1f}s |\n\n"
            f"**Stage Progress:**\n\n"
            f"| Stage | Name | Status | Duration |\n|---|---|---|---|\n"
            f"{stage_status}\n"
            f"**Live Agent Output:**\n"
            f"- AccountProfileAgent: Returned firmographics for target account\n"
            f"- StakeholderMappingAgent: Mapped 8 stakeholders across buying committee\n"
            f"- CompetitiveIntelligenceAgent: Identified 2 active competitors\n"
            f"- DealRiskAssessmentAgent: Processing risk factors...\n\n"
            f"Source: [Orchestration Engine]\n"
            f"Agents: AccountIntelligenceOrchestrator"
        )

    # ── check_status ──────────────────────────────────────────
    def _check_status(self, **kwargs):
        run_id = kwargs.get("run_id", "run-2001")
        run = _ORCHESTRATION_RUNS.get(run_id)
        if not run:
            return f"**Error:** Run `{run_id}` not found. Available: {', '.join(_ORCHESTRATION_RUNS.keys())}"

        pipe = _PIPELINES.get(run["pipeline"], {})
        pipe_name = pipe.get("name", run["pipeline"]) if pipe else run["pipeline"]

        started = run["started_at"] or "Not started"
        completed = run["completed_at"] or "In progress"
        failed_note = ""
        if run["agents_failed"] > 0:
            failed_note = f"\n**Warning:** {run['agents_failed']} agent(s) failed during execution. Check agent health dashboard."

        return (
            f"**Orchestration Run Status: {run_id}**\n\n"
            f"| Property | Value |\n|---|---|\n"
            f"| Pipeline | {pipe_name} |\n"
            f"| Account | {run['account']} |\n"
            f"| Requested By | {run['requested_by']} |\n"
            f"| Status | {run['status'].title()} |\n"
            f"| Stages | {run['stages_completed']}/{run['stages_total']} |\n"
            f"| Agents Invoked | {run['agents_invoked']} |\n"
            f"| Agents Succeeded | {run['agents_succeeded']} |\n"
            f"| Agents Failed | {run['agents_failed']} |\n"
            f"| Duration | {run['total_duration_sec']}s |\n"
            f"| Output Tokens | {run['output_tokens']:,} |\n"
            f"| Started | {started} |\n"
            f"| Completed | {completed} |\n"
            f"{failed_note}\n"
            f"Source: [Orchestration Engine + Run History]\n"
            f"Agents: AccountIntelligenceOrchestrator"
        )

    # ── generate_report ───────────────────────────────────────
    def _generate_report(self, **kwargs):
        total_runs = len(_ORCHESTRATION_RUNS)
        completed_runs = sum(1 for r in _ORCHESTRATION_RUNS.values() if r["status"] == "completed")
        running_runs = sum(1 for r in _ORCHESTRATION_RUNS.values() if r["status"] == "running")
        queued_runs = sum(1 for r in _ORCHESTRATION_RUNS.values() if r["status"] == "queued")
        total_agents_invoked = sum(r["agents_invoked"] for r in _ORCHESTRATION_RUNS.values())
        total_failures = sum(r["agents_failed"] for r in _ORCHESTRATION_RUNS.values())
        avg_duration = sum(r["total_duration_sec"] for r in _ORCHESTRATION_RUNS.values() if r["status"] == "completed") / max(completed_runs, 1)

        pipeline_rows = ""
        for key, pipe in _PIPELINES.items():
            est = _estimate_duration(key)
            health = _pipeline_health(key)
            cnt = _total_agents_in_pipeline(key)
            pipeline_rows += f"| {pipe['name']} | {len(pipe['stages'])} stages | {cnt} agents | {est:.1f}s est. | {health.title()} |\n"

        agent_rows = ""
        for agent_name, health in sorted(_AGENT_HEALTH.items()):
            agent_rows += (
                f"| {agent_name} | {health['status'].title()} | "
                f"{health['avg_latency_ms']}ms | {health['success_rate']}% |\n"
            )

        run_rows = ""
        for run_id, run in _ORCHESTRATION_RUNS.items():
            run_rows += (
                f"| {run_id} | {run['account']} | {run['pipeline']} | "
                f"{run['status'].title()} | {run['total_duration_sec']}s |\n"
            )

        return (
            f"**Orchestration Health Report**\n\n"
            f"**Summary:**\n"
            f"| Metric | Value |\n|---|---|\n"
            f"| Total Runs | {total_runs} |\n"
            f"| Completed | {completed_runs} |\n"
            f"| Running | {running_runs} |\n"
            f"| Queued | {queued_runs} |\n"
            f"| Total Agents Invoked | {total_agents_invoked} |\n"
            f"| Agent Failures | {total_failures} |\n"
            f"| Avg Completion Time | {avg_duration:.1f}s |\n\n"
            f"**Available Pipelines:**\n\n"
            f"| Pipeline | Stages | Agents | Est. Duration | Health |\n|---|---|---|---|---|\n"
            f"{pipeline_rows}\n"
            f"**Agent Health Dashboard:**\n\n"
            f"| Agent | Status | Avg Latency | Success Rate |\n|---|---|---|---|\n"
            f"{agent_rows}\n"
            f"**Recent Runs:**\n\n"
            f"| Run ID | Account | Pipeline | Status | Duration |\n|---|---|---|---|---|\n"
            f"{run_rows}\n"
            f"Source: [Orchestration Engine + Agent Registry + Run History]\n"
            f"Agents: AccountIntelligenceOrchestrator"
        )


if __name__ == "__main__":
    agent = AccountIntelligenceOrchestrator()
    for op in ["orchestrate_briefing", "run_pipeline", "check_status", "generate_report"]:
        print("=" * 60)
        print(agent.perform(operation=op))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
