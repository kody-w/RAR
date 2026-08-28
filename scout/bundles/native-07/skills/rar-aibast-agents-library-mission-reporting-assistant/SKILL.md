---
name: "rar-aibast-agents-library-mission-reporting-assistant"
description: "Computes mission KPIs from live records on a simulated Dynamics 365 tenant, with briefs and trend analyses that work offline."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/mission_reporting_assistant", "rar_sha256": "9cfa2e32539fd7d1848bf36ec4354cd334a7adadfba826d7582cb5b85ca2b42c", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["mission", "reporting", "KPI", "stakeholder", "federal", "dashboard"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/mission_reporting_assistant`. The original RAPP
agent is preserved byte-for-byte in `mission_reporting_assistant_agent.py` and in the RCI capsule.

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

Mission Reporting Assistant Agent — a template you are meant to mutate.

Generates mission summaries, KPI dashboards, stakeholder briefs, and
trend analyses for federal program and mission managers.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live operational records over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template mission KPIs are computed from real service
     records — case resolution rate, backlog, first-response coverage,
     and task completion — across the tenant's 38 cases and 36 tasks
     (including CAS-260131, a records-request backlog past its
     statutory deadline).
     Try: perform(operation="kpi_dashboard")
  2. No network? Everything falls back to the embedded demo layer below
     (MISSION_OBJECTIVES / KPIS / STAKEHOLDERS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     MISSION_REPORTING_ASSISTANT_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your performance
     system), or replace _fetch_collection() with your own API client.
     The KPI shape the rest of the file needs is listed in
     _normalize_live_kpis() — everything else keeps working untouched.
     Fields marked "enrichment seam" in the output (targets, trends)
     are where you wire your strategic-planning system.

OPERATIONS
  mission_summary | kpi_dashboard | stakeholder_brief | trend_analysis
  kwargs: operation (required), mission_id, stakeholder_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "mission_id": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "mission_summary",
        "kpi_dashboard",
        "stakeholder_brief",
        "trend_analysis"
      ],
      "type": "string"
    },
    "stakeholder_id": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `mission_reporting_assistant_agent.py` and embedded as the fenced Python below (sha256 9cfa2e32539fd7d1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `mission_reporting_assistant_agent.py` first:

```bash
python3 mission_reporting_assistant_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 mission_reporting_assistant_agent.py   # or on stdin
python3 mission_reporting_assistant_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Mission Reporting Assistant Agent — a template you are meant to mutate.

Generates mission summaries, KPI dashboards, stakeholder briefs, and
trend analyses for federal program and mission managers.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live operational records over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template mission KPIs are computed from real service
     records — case resolution rate, backlog, first-response coverage,
     and task completion — across the tenant's 38 cases and 36 tasks
     (including CAS-260131, a records-request backlog past its
     statutory deadline).
     Try: perform(operation="kpi_dashboard")
  2. No network? Everything falls back to the embedded demo layer below
     (MISSION_OBJECTIVES / KPIS / STAKEHOLDERS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     MISSION_REPORTING_ASSISTANT_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your performance
     system), or replace _fetch_collection() with your own API client.
     The KPI shape the rest of the file needs is listed in
     _normalize_live_kpis() — everything else keeps working untouched.
     Fields marked "enrichment seam" in the output (targets, trends)
     are where you wire your strategic-planning system.

OPERATIONS
  mission_summary | kpi_dashboard | stakeholder_brief | trend_analysis
  kwargs: operation (required), mission_id, stakeholder_id
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/mission_reporting_assistant",
    "version": "1.1.0",
    "display_name": "Mission Reporting Assistant Agent",
    "description": "Computes mission KPIs from live records on a simulated Dynamics 365 tenant, with briefs and trend analyses that work offline.",
    "author": "AIBAST",
    "tags": ["mission", "reporting", "KPI", "stakeholder", "federal", "dashboard"],
    "category": "federal_government",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# ---------------------------------------------------------------------------
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export MISSION_REPORTING_ASSISTANT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your performance-system client.
# Downstream code only needs the KPI shape produced by
# _normalize_live_kpis().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "MISSION_REPORTING_ASSISTANT_DATA_URL",
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


def _normalize_live_kpis(incidents, tasks):
    """Compute mission KPIs from live service records. THIS is the
    contract your replacement data source must meet — a list of dicts
    with these keys (name, current, target, unit, trend). Current values
    are real math over live records; None means 'not available from CRM
    alone' (targets and trends live in your strategic-planning system —
    an enrichment seam)."""
    kpis = []
    if incidents:
        resolved = sum(1 for i in incidents if i.get("statecode") == 1)
        open_cases = sum(1 for i in incidents if i.get("statecode") == 0)
        responded = sum(1 for i in incidents if i.get("firstresponsesenton"))
        kpis.append({"name": "Case Resolution Rate",
                     "current": round(resolved / len(incidents) * 100, 1),
                     "target": None, "unit": "%", "trend": None})
        kpis.append({"name": "Open Case Backlog",
                     "current": open_cases,
                     "target": None, "unit": "cases", "trend": None})
        kpis.append({"name": "First Response Coverage",
                     "current": round(responded / len(incidents) * 100, 1),
                     "target": None, "unit": "%", "trend": None})
    if tasks:
        completed = sum(1 for t in tasks if t.get("statecode") == 1)
        kpis.append({"name": "Task Completion Rate",
                     "current": round(completed / len(tasks) * 100, 1),
                     "target": None, "unit": "%", "trend": None})
    return kpis


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

MISSION_OBJECTIVES = {
    "MO-001": {
        "name": "Cybersecurity Posture Improvement",
        "strategic_goal": "SG-2: Secure Federal Networks",
        "lead_office": "Office of the CISO",
        "status": "on_track",
        "priority": "critical",
        "start_date": "2024-10-01",
        "target_date": "2025-09-30",
        "budget_allocated": 14500000,
        "budget_spent": 7250000,
        "description": "Improve agency cybersecurity posture across all FISMA systems to achieve 95% compliance.",
    },
    "MO-002": {
        "name": "Customer Experience Modernization",
        "strategic_goal": "SG-4: Deliver Excellent Service",
        "lead_office": "Office of Customer Experience",
        "status": "at_risk",
        "priority": "high",
        "start_date": "2024-10-01",
        "target_date": "2026-03-31",
        "budget_allocated": 8200000,
        "budget_spent": 4920000,
        "description": "Modernize public-facing digital services to achieve 80% customer satisfaction.",
    },
    "MO-003": {
        "name": "Workforce Transformation Initiative",
        "strategic_goal": "SG-5: Build Future Workforce",
        "lead_office": "Office of Human Capital",
        "status": "on_track",
        "priority": "high",
        "start_date": "2025-01-01",
        "target_date": "2027-09-30",
        "budget_allocated": 5600000,
        "budget_spent": 840000,
        "description": "Recruit, reskill, and retain critical technology talent across the agency.",
    },
}

KPIS = {
    "KPI-101": {"name": "FISMA Compliance Rate", "mission": "MO-001", "target": 95.0, "current": 87.3, "unit": "%", "trend": "improving"},
    "KPI-102": {"name": "Mean Time to Remediate (Critical)", "mission": "MO-001", "target": 15, "current": 22, "unit": "days", "trend": "improving"},
    "KPI-103": {"name": "Phishing Click Rate", "mission": "MO-001", "target": 3.0, "current": 4.8, "unit": "%", "trend": "stable"},
    "KPI-201": {"name": "Customer Satisfaction Score", "mission": "MO-002", "target": 80.0, "current": 68.5, "unit": "%", "trend": "declining"},
    "KPI-202": {"name": "Digital Service Adoption", "mission": "MO-002", "target": 70.0, "current": 52.1, "unit": "%", "trend": "improving"},
    "KPI-203": {"name": "Average Transaction Time", "mission": "MO-002", "target": 5.0, "current": 8.3, "unit": "minutes", "trend": "improving"},
    "KPI-301": {"name": "Critical Position Fill Rate", "mission": "MO-003", "target": 90.0, "current": 72.0, "unit": "%", "trend": "improving"},
    "KPI-302": {"name": "Employee Engagement Score", "mission": "MO-003", "target": 75.0, "current": 69.4, "unit": "%", "trend": "stable"},
    "KPI-303": {"name": "Training Completion Rate", "mission": "MO-003", "target": 85.0, "current": 61.5, "unit": "%", "trend": "improving"},
}

STAKEHOLDERS = {
    "SH-01": {"name": "Deputy Secretary", "role": "Executive Sponsor", "briefing_frequency": "monthly", "interest": "strategic_outcomes"},
    "SH-02": {"name": "CFO", "role": "Budget Oversight", "briefing_frequency": "quarterly", "interest": "financial_performance"},
    "SH-03": {"name": "CIO", "role": "Technology Lead", "briefing_frequency": "bi-weekly", "interest": "it_modernization"},
    "SH-04": {"name": "CHCO", "role": "Workforce Lead", "briefing_frequency": "monthly", "interest": "workforce_metrics"},
    "SH-05": {"name": "OMB Desk Officer", "role": "External Oversight", "briefing_frequency": "quarterly", "interest": "performance_targets"},
    "SH-06": {"name": "Congressional Liaison", "role": "Legislative Affairs", "briefing_frequency": "as_needed", "interest": "appropriations_alignment"},
}

QUARTERLY_TRENDS = {
    "Q1-FY24": {"KPI-101": 78.1, "KPI-201": 72.0, "KPI-301": 65.0},
    "Q2-FY24": {"KPI-101": 80.5, "KPI-201": 71.2, "KPI-301": 67.5},
    "Q3-FY24": {"KPI-101": 83.2, "KPI-201": 70.0, "KPI-301": 69.0},
    "Q4-FY24": {"KPI-101": 85.0, "KPI-201": 69.1, "KPI-301": 70.8},
    "Q1-FY25": {"KPI-101": 87.3, "KPI-201": 68.5, "KPI-301": 72.0},
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _kpi_status(kpi):
    """Determine KPI status relative to target."""
    if kpi["unit"] in ("days", "minutes"):
        pct = (kpi["target"] / kpi["current"]) * 100 if kpi["current"] else 100
    else:
        pct = (kpi["current"] / kpi["target"]) * 100 if kpi["target"] else 0
    if pct >= 95:
        return "On Target"
    elif pct >= 75:
        return "Near Target"
    else:
        return "Below Target"


def _budget_utilization(mission):
    """Compute budget utilization percentage."""
    if mission["budget_allocated"] == 0:
        return 0.0
    return round((mission["budget_spent"] / mission["budget_allocated"]) * 100, 1)


def _trend_direction(values):
    """Determine trend direction from a list of values."""
    if len(values) < 2:
        return "insufficient_data"
    recent = values[-1]
    previous = values[-2]
    if recent > previous * 1.02:
        return "improving"
    elif recent < previous * 0.98:
        return "declining"
    return "stable"


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class MissionReportingAssistantAgent(BasicAgent):
    """Mission reporting assistant for federal program management."""

    def __init__(self):
        self.name = "MissionReportingAssistantAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Mission Reporting Assistant Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "mission_summary",
                            "kpi_dashboard",
                            "stakeholder_brief",
                            "trend_analysis",
                        ],
                    },
                    "mission_id": {"type": "string"},
                    "stakeholder_id": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "mission_summary")
        dispatch = {
            "mission_summary": self._mission_summary,
            "kpi_dashboard": self._kpi_dashboard,
            "stakeholder_brief": self._stakeholder_brief,
            "trend_analysis": self._trend_analysis,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        return handler(**kwargs)

    def _mission_summary(self, **kwargs) -> str:
        lines = ["# Mission Summary Report\n"]
        for mid, m in MISSION_OBJECTIVES.items():
            util = _budget_utilization(m)
            lines.append(f"## {mid}: {m['name']}\n")
            lines.append(f"- **Strategic Goal:** {m['strategic_goal']}")
            lines.append(f"- **Lead Office:** {m['lead_office']}")
            lines.append(f"- **Status:** {m['status'].replace('_', ' ').title()}")
            lines.append(f"- **Priority:** {m['priority'].title()}")
            lines.append(f"- **Period:** {m['start_date']} to {m['target_date']}")
            lines.append(f"- **Budget:** ${m['budget_allocated']:,.0f} allocated / ${m['budget_spent']:,.0f} spent ({util}%)")
            lines.append(f"- **Description:** {m['description']}\n")
            mission_kpis = {k: v for k, v in KPIS.items() if v["mission"] == mid}
            if mission_kpis:
                lines.append("| KPI | Current | Target | Status |")
                lines.append("|---|---|---|---|")
                for kid, kpi in mission_kpis.items():
                    status = _kpi_status(kpi)
                    lines.append(f"| {kpi['name']} | {kpi['current']} {kpi['unit']} | {kpi['target']} {kpi['unit']} | {status} |")
            lines.append("")
        return "\n".join(lines)

    def _kpi_dashboard(self, **kwargs) -> str:
        incidents = _fetch_collection("incidents")
        if incidents:
            tasks = _fetch_collection("tasks")
            live = _normalize_live_kpis(incidents, tasks)
            lines = ["# KPI Dashboard (live tenant data)\n"]
            lines.append(f"Computed from {len(incidents)} live cases and {len(tasks)} live tasks.\n")
            lines.append("| KPI | Current | Target | Unit | Trend | Status |")
            lines.append("|---|---|---|---|---|---|")
            for kpi in live:
                lines.append(
                    f"| {kpi['name']} | {kpi['current']} "
                    f"| n/a — enrichment seam | {kpi['unit']} "
                    f"| n/a — enrichment seam | measured |"
                )
            lines.append("\n_Source: live Static Dynamics 365 tenant (incidents + tasks). "
                         "Current values are real math over live records; targets and "
                         "trends are enrichment seams — wire your strategic-planning "
                         "system._")
            return "\n".join(lines)

        lines = ["# KPI Dashboard (embedded demo data — offline)\n"]
        lines.append("| KPI ID | Name | Mission | Current | Target | Unit | Trend | Status |")
        lines.append("|---|---|---|---|---|---|---|---|")
        for kid, kpi in KPIS.items():
            status = _kpi_status(kpi)
            lines.append(
                f"| {kid} | {kpi['name']} | {kpi['mission']} "
                f"| {kpi['current']} | {kpi['target']} | {kpi['unit']} "
                f"| {kpi['trend'].title()} | {status} |"
            )
        on_target = sum(1 for k in KPIS.values() if _kpi_status(k) == "On Target")
        near = sum(1 for k in KPIS.values() if _kpi_status(k) == "Near Target")
        below = sum(1 for k in KPIS.values() if _kpi_status(k) == "Below Target")
        lines.append(f"\n**Summary:** {on_target} on target, {near} near target, {below} below target")
        return "\n".join(lines)

    def _stakeholder_brief(self, **kwargs) -> str:
        lines = ["# Stakeholder Briefing Guide\n"]
        lines.append("## Stakeholder Registry\n")
        lines.append("| ID | Name | Role | Briefing Frequency | Interest Area |")
        lines.append("|---|---|---|---|---|")
        for sid, s in STAKEHOLDERS.items():
            lines.append(
                f"| {sid} | {s['name']} | {s['role']} "
                f"| {s['briefing_frequency'].replace('_', ' ').title()} | {s['interest'].replace('_', ' ').title()} |"
            )
        lines.append("\n## Executive Brief\n")
        for mid, m in MISSION_OBJECTIVES.items():
            lines.append(f"### {m['name']} — {m['status'].replace('_', ' ').title()}\n")
            mission_kpis = {k: v for k, v in KPIS.items() if v["mission"] == mid}
            highlights = []
            for kid, kpi in mission_kpis.items():
                status = _kpi_status(kpi)
                if status == "Below Target":
                    highlights.append(f"- **Action Needed:** {kpi['name']} at {kpi['current']}{kpi['unit']} vs target {kpi['target']}{kpi['unit']}")
                elif status == "On Target":
                    highlights.append(f"- **On Track:** {kpi['name']} at {kpi['current']}{kpi['unit']}")
            for h in highlights:
                lines.append(h)
            lines.append("")
        return "\n".join(lines)

    def _trend_analysis(self, **kwargs) -> str:
        lines = ["# Trend Analysis\n"]
        tracked_kpis = ["KPI-101", "KPI-201", "KPI-301"]
        for kid in tracked_kpis:
            kpi = KPIS[kid]
            lines.append(f"## {kid}: {kpi['name']}\n")
            lines.append(f"**Target:** {kpi['target']} {kpi['unit']}\n")
            lines.append("| Quarter | Value |")
            lines.append("|---|---|")
            values = []
            for qtr, data in QUARTERLY_TRENDS.items():
                val = data.get(kid)
                if val is not None:
                    values.append(val)
                    lines.append(f"| {qtr} | {val} {kpi['unit']} |")
            direction = _trend_direction(values)
            lines.append(f"\n**Trend:** {direction.title()}")
            if values:
                change = round(values[-1] - values[0], 1)
                lines.append(f"**Net Change:** {'+' if change >= 0 else ''}{change} {kpi['unit']} over {len(values)} quarters\n")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = MissionReportingAssistantAgent()
    print("=" * 60)
    print("LIVE TENANT KPIs (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="kpi_dashboard"))
    print()
    print("=" * 60)
    print("EMBEDDED DEMO MISSIONS (works offline)")
    print(agent.perform(operation="mission_summary"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="stakeholder_brief"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="trend_analysis"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
