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
