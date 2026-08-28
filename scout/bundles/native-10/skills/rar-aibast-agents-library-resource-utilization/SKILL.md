---
name: "rar-aibast-agents-library-resource-utilization"
description: "Reports consultant utilization and staffing plans from a live simulated Dynamics 365 tenant booking calendar, with an offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/resource_utilization", "rar_sha256": "1f1b744ebbe7d2503dd0b654951d7ebbd44bd50f4624e60a33be74e3e9c79c6b", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["utilization", "staffing", "capacity", "bench", "professional-services"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/resource_utilization`. The original RAPP
agent is preserved byte-for-byte in `resource_utilization_agent.py` and in the RCI capsule.

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

Resource Utilization Agent — a template you are meant to mutate.

Tracks consultant utilization, billable hours, and capacity across a
professional-services firm. Forecasts demand, identifies bench resources,
and generates staffing recommendations to hit utilization targets.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template the tenant's bookable resources are reinterpreted
     as the consultant bench and their bookings as scheduled billable
     work — e.g. resource "Riley Chen" with booked hours computed from
     the live booking calendar.
     Try: perform(operation="utilization_dashboard")
  2. No network? Everything falls back to the embedded demo layer below
     (CONSULTANTS / PROJECT_PIPELINE / UTILIZATION_TARGETS) — the agent
     never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     RESOURCE_UTILIZATION_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your PSA), or replace
     _fetch_collection() with a Kantata/OpenAir client. Fields the rest
     of the file needs are listed in _normalize_live_consultant() —
     bill rates and skills render as "n/a — enrichment seam" until you
     wire your rate card and skills matrix.

OPERATIONS
  utilization_dashboard | capacity_forecast | bench_analysis
  | staffing_recommendation | skill_gap_options | executive_impact_report
  kwargs: operation (required), record_id, consultant_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "consultant_id": {
      "description": "Consultant identifier, such as CON-405; selects that consultant's skill-gap option.",
      "type": "string"
    },
    "operation": {
      "description": "Operation to run; defaults to utilization_dashboard when omitted.",
      "enum": [
        "utilization_dashboard",
        "capacity_forecast",
        "bench_analysis",
        "staffing_recommendation",
        "skill_gap_options",
        "executive_impact_report"
      ],
      "type": "string"
    },
    "record_id": {
      "description": "Evidence record identifier for skill_gap_options or executive_impact_report, such as RU-601 or RU-EXEC-601.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `resource_utilization_agent.py` and embedded as the fenced Python below (sha256 1f1b744ebbe7d250…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `resource_utilization_agent.py` first:

```bash
python3 resource_utilization_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 resource_utilization_agent.py   # or on stdin
python3 resource_utilization_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Resource Utilization Agent — a template you are meant to mutate.

Tracks consultant utilization, billable hours, and capacity across a
professional-services firm. Forecasts demand, identifies bench resources,
and generates staffing recommendations to hit utilization targets.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template the tenant's bookable resources are reinterpreted
     as the consultant bench and their bookings as scheduled billable
     work — e.g. resource "Riley Chen" with booked hours computed from
     the live booking calendar.
     Try: perform(operation="utilization_dashboard")
  2. No network? Everything falls back to the embedded demo layer below
     (CONSULTANTS / PROJECT_PIPELINE / UTILIZATION_TARGETS) — the agent
     never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     RESOURCE_UTILIZATION_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your PSA), or replace
     _fetch_collection() with a Kantata/OpenAir client. Fields the rest
     of the file needs are listed in _normalize_live_consultant() —
     bill rates and skills render as "n/a — enrichment seam" until you
     wire your rate card and skills matrix.

OPERATIONS
  utilization_dashboard | capacity_forecast | bench_analysis
  | staffing_recommendation | skill_gap_options | executive_impact_report
  kwargs: operation (required), record_id, consultant_id
"""

import sys
import os
import json
import urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/resource_utilization",
    "version": "1.2.0",
    "display_name": "Resource Utilization Agent",
    "description": "Reports consultant utilization and staffing plans from a live simulated Dynamics 365 tenant booking calendar, with an offline fallback.",
    "author": "AIBAST",
    "tags": ["utilization", "staffing", "capacity", "bench", "professional-services"],
    "category": "professional_services",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export RESOURCE_UTILIZATION_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your PSA client. Downstream
# code only needs the fields from _normalize_live_consultant().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "RESOURCE_UTILIZATION_DATA_URL",
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


def _normalize_live_consultant(row, bookings):
    """Project a Dynamics bookable resource + its bookings onto the
    consultant shape this agent renders. THIS is the contract your
    replacement data source must meet — a dict with these keys. None
    means 'not knowable from the scheduling records alone' and the
    renderer labels it as an enrichment seam (wire your rate card and
    skills matrix)."""
    name = row.get("name", "Unknown")
    mine = [b for b in bookings if b.get("resourcename") == name]
    booked_minutes = sum(
        int(b.get("duration") or 0) for b in mine
        if b.get("bookingstatusname") in ("Scheduled", "In Progress", "Completed")
    )
    return {
        "name": name,
        "booked_hours": round(booked_minutes / 60, 1),  # real, from bookings
        "bookings": len(mine),
        "status": "billable" if booked_minutes else "bench",
        "rate_hr": None,   # enrichment seam — wire your rate card
        "skills": None,    # enrichment seam — wire your skills matrix
        "level": None,     # enrichment seam
        "_live": True,
    }


def _live_bench():
    """Tenant bookable resources reinterpreted as the consultant bench,
    with booked hours computed from the live calendar; [] when offline."""
    rows = _fetch_collection("bookableresources")
    bookings = _fetch_collection("bookableresourcebookings") if rows else []
    return [_normalize_live_consultant(r, bookings) for r in rows]


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

CONSULTANTS = {
    "CON-401": {"name": "Elena Vasquez", "level": "Senior", "skills": ["Cloud Architecture", "Azure", "DevOps"],
                 "rate_hr": 275, "utilization_pct": 92, "status": "billable",
                 "current_project": "TechCorp Transformation", "project_end": "2026-06-30"},
    "CON-402": {"name": "Michael Chen", "level": "Senior", "skills": ["Data Engineering", "Databricks", "Python"],
                 "rate_hr": 260, "utilization_pct": 88, "status": "billable",
                 "current_project": "Apex Analytics Platform", "project_end": "2026-05-15"},
    "CON-403": {"name": "Priya Sharma", "level": "Manager", "skills": ["Program Management", "Agile", "Change Mgmt"],
                 "rate_hr": 310, "utilization_pct": 95, "status": "billable",
                 "current_project": "Pinnacle Energy ERP", "project_end": "2026-08-31"},
    "CON-404": {"name": "David Okafor", "level": "Mid", "skills": ["Data Analytics", "Power BI", "SQL"],
                 "rate_hr": 175, "utilization_pct": 0, "status": "bench",
                 "current_project": None, "project_end": None},
    "CON-405": {"name": "Sarah Kim", "level": "Mid", "skills": ["Cloud Architecture", "AWS", "Terraform"],
                 "rate_hr": 185, "utilization_pct": 0, "status": "bench",
                 "current_project": None, "project_end": None},
    "CON-406": {"name": "James Wright", "level": "Junior", "skills": ["Business Analysis", "Requirements", "Jira"],
                 "rate_hr": 125, "utilization_pct": 0, "status": "bench",
                 "current_project": None, "project_end": None},
    "CON-407": {"name": "Lisa Tanaka", "level": "Senior", "skills": ["Cybersecurity", "Identity", "Compliance"],
                 "rate_hr": 290, "utilization_pct": 78, "status": "billable",
                 "current_project": "Atlas Security Audit", "project_end": "2026-04-10"},
    "CON-408": {"name": "Robert Garcia", "level": "Mid", "skills": ["ERP", "D365", "Integration"],
                 "rate_hr": 195, "utilization_pct": 0, "status": "bench",
                 "current_project": None, "project_end": None},
    "CON-409": {"name": "Amanda Foster", "level": "Mid", "skills": ["UX Design", "Research", "Figma"],
                 "rate_hr": 165, "utilization_pct": 85, "status": "billable",
                 "current_project": "Metro Transit Portal", "project_end": "2026-05-01"},
    "CON-410": {"name": "Chen Wei", "level": "Senior", "skills": ["AI/ML", "Python", "Azure ML"],
                 "rate_hr": 295, "utilization_pct": 0, "status": "bench",
                 "current_project": None, "project_end": None},
}

PROJECT_PIPELINE = [
    {"name": "FinanceHub Cloud Migration", "start": "2026-04-01", "months": 6,
     "needs": [("Cloud Architecture", "Senior", 1), ("DevOps", "Mid", 2)], "probability": 0.85},
    {"name": "Healthcare Digital Transformation", "start": "2026-04-15", "months": 12,
     "needs": [("Program Management", "Manager", 1), ("Data Analytics", "Mid", 2), ("Business Analysis", "Junior", 1)], "probability": 0.75},
    {"name": "Retail Analytics Platform", "start": "2026-05-01", "months": 8,
     "needs": [("AI/ML", "Senior", 1), ("Data Engineering", "Mid", 1)], "probability": 0.60},
    {"name": "Government Cyber Assessment", "start": "2026-04-01", "months": 3,
     "needs": [("Cybersecurity", "Senior", 2), ("Compliance", "Mid", 1)], "probability": 0.90},
]

UTILIZATION_TARGETS = {
    "Senior": 85,
    "Manager": 80,
    "Mid": 80,
    "Junior": 75,
    "firm_target": 85,
}

BENCH_COST_PER_MONTH = {
    "Senior": 22000,
    "Manager": 25000,
    "Mid": 14000,
    "Junior": 10000,
}

EVIDENCE_CAPABILITIES = {
    "skill_gap_options": {
        "title": "Near-Ready Skill Gap Options",
        "write": False,
        "records": [
            {
                "record_id": "RU-601",
                "consultant": "Sarah Kim",
                "pipeline_need": "FinanceHub Cloud Migration / Azure architecture",
                "gap": "AWS-to-Azure platform mapping",
                "option": "two-week Azure landing-zone accelerator",
                "delivery_guardrail": "pair with Elena Vasquez for architecture review",
                "upskilling_roi": "$29,600 monthly billable value versus $14,000 bench cost",
            },
            {
                "record_id": "RU-602",
                "consultant": "Robert Garcia",
                "pipeline_need": "FinanceHub Cloud Migration / DevOps",
                "gap": "Terraform delivery evidence",
                "option": "three-week Terraform lab plus internal deployment",
                "delivery_guardrail": "technical gate before client assignment",
                "upskilling_roi": "$31,200 monthly billable value versus $14,000 bench cost",
            },
        ],
    },
    "executive_impact_report": {
        "title": "Executive Utilization Impact Report",
        "write": True,
        "records": [
            {
                "record_id": "RU-EXEC-601",
                "scenario": "deploy direct bench-to-pipeline matches",
                "dashboard": "utilization, bench cost, skills, pipeline, and financial upside",
            },
            {
                "record_id": "RU-EXEC-602",
                "scenario": "deploy matches, close near-ready gaps, and move remaining bench to billable innovation work",
                "dashboard": "utilization, bench cost, skills, pipeline, and financial upside",
            },
        ],
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _firm_utilization():
    """Average utilization across all consultants."""
    rates = [c["utilization_pct"] for c in CONSULTANTS.values()]
    return round(sum(rates) / len(rates), 1)


def _bench_consultants():
    """Return list of bench consultants."""
    return {cid: c for cid, c in CONSULTANTS.items() if c["status"] == "bench"}


def _monthly_bench_cost():
    """Total monthly cost of bench consultants."""
    total = 0
    for c in CONSULTANTS.values():
        if c["status"] == "bench":
            total += BENCH_COST_PER_MONTH.get(c["level"], 14000)
    return total


def _skill_match(consultant, required_skill):
    """Check if a consultant has a matching skill."""
    return any(required_skill.lower() in s.lower() for s in consultant["skills"])


def _find_matches_for_pipeline():
    """Match bench consultants to pipeline project needs."""
    matches = []
    bench = _bench_consultants()
    for proj in PROJECT_PIPELINE:
        for skill, level, count in proj["needs"]:
            candidates = [
                (cid, c) for cid, c in bench.items()
                if c["level"] == level and _skill_match(c, skill)
            ]
            for cid, c in candidates[:count]:
                matches.append({
                    "consultant_id": cid,
                    "consultant_name": c["name"],
                    "project": proj["name"],
                    "skill_matched": skill,
                    "level": level,
                    "probability": proj["probability"],
                    "start": proj["start"],
                })
    return matches


def _deployment_metrics(consultant_ids):
    """Calculate financial and utilization impact from current source records."""
    bench = _bench_consultants()
    selected_ids = list(dict.fromkeys(
        cid for cid in consultant_ids if cid in bench
    ))
    monthly_savings = sum(
        BENCH_COST_PER_MONTH.get(bench[cid]["level"], 14000)
        for cid in selected_ids
    )
    monthly_capacity_revenue = sum(
        bench[cid]["rate_hr"] * 160 for cid in selected_ids
    )
    total = len(CONSULTANTS)
    projected_billable = total - len(bench) + len(selected_ids)
    projected_utilization = (
        round(projected_billable / total * 87, 1) if total else 0
    )
    return {
        "monthly_savings": monthly_savings,
        "monthly_capacity_revenue": monthly_capacity_revenue,
        "current_utilization": _firm_utilization(),
        "projected_utilization": projected_utilization,
    }


def _executive_impact_records():
    """Build executive records from consultants, matches, rates, and cost tables."""
    templates = EVIDENCE_CAPABILITIES["executive_impact_report"]["records"]
    direct_ids = [
        match["consultant_id"] for match in _find_matches_for_pipeline()
    ]
    scenario_ids = [
        direct_ids,
        list(_bench_consultants()),
    ]
    records = []
    for template, consultant_ids in zip(templates, scenario_ids):
        metrics = _deployment_metrics(consultant_ids)
        records.append({
            "record_id": template["record_id"],
            "scenario": template["scenario"],
            "projected_savings": (
                f"${metrics['monthly_savings']:,.0f} "
                "monthly bench-cost reduction"
            ),
            "new_revenue": (
                f"${metrics['monthly_capacity_revenue']:,.0f} "
                "monthly billable capacity/revenue"
            ),
            "utilization_progress": (
                f"{metrics['current_utilization']}% current to "
                f"{metrics['projected_utilization']}% projected"
            ),
            "dashboard": template["dashboard"],
        })
    return records


def _evidence_matches(user_input, records):
    """Match explicit scenario IDs without silently substituting another plan."""
    tokens = {
        "".join(ch for ch in token.upper() if ch.isalnum())
        for token in str(user_input).split()
    }
    return [
        record for record in records
        if "".join(ch for ch in record["record_id"].upper() if ch.isalnum()) in tokens
    ]


def _evidence_selector(capability, kwargs):
    """Resolve explicit evidence or consultant identifiers to evidence record IDs."""
    if kwargs.get("record_id"):
        return kwargs["record_id"]
    if kwargs.get("consultant_id"):
        consultant = CONSULTANTS.get(kwargs["consultant_id"])
        if not consultant:
            return kwargs["consultant_id"]
        records = EVIDENCE_CAPABILITIES[capability]["records"]
        record_ids = [
            record["record_id"]
            for record in records
            if record.get("consultant") == consultant["name"]
        ]
        return " ".join(record_ids) or kwargs["consultant_id"]
    return kwargs.get("user_input", "")


def _render_evidence_operation(capability, user_input=""):
    spec = EVIDENCE_CAPABILITIES[capability]
    records = (
        _executive_impact_records()
        if capability == "executive_impact_report"
        else spec["records"]
    )
    matches = _evidence_matches(user_input, records) if user_input else records
    lines = [f"## {spec['title']}\n"]
    if user_input and not matches:
        lines.append("No exact `record_id` match was found; no substitute scenario was used.")
    else:
        lines.append("Deterministic workforce-planning scenarios:")
        for record in matches:
            lines.append("- " + "; ".join(f"{key}: {value}" for key, value in record.items()))
    if spec["write"]:
        target = matches[0]["record_id"] if matches else "NO-MATCH"
        lines.extend([
            "\n### Simulated Write Receipt",
            f"- receipt_id: SIM-{capability.upper()}-{target}",
            "- status: simulated",
            "- target_system: Microsoft Teams executive dashboard",
            "- No dashboard or message was published; this is a preview-only write.",
        ])
    else:
        lines.append("\n_Read-only analysis; no external system changed._")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class ResourceUtilizationAgent(BasicAgent):
    """Tracks consultant utilization and generates staffing plans."""

    def __init__(self):
        self.name = "ResourceUtilizationAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "operations": [
                "utilization_dashboard",
                "capacity_forecast",
                "bench_analysis",
                "staffing_recommendation",
                "skill_gap_options",
                "executive_impact_report",
            ],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "description": "Operation to run; defaults to utilization_dashboard when omitted.",
                        "enum": [
                            "utilization_dashboard",
                            "capacity_forecast",
                            "bench_analysis",
                            "staffing_recommendation",
                            "skill_gap_options",
                            "executive_impact_report",
                        ],
                    },
                    "record_id": {
                        "type": "string",
                        "description": "Evidence record identifier for skill_gap_options or executive_impact_report, such as RU-601 or RU-EXEC-601.",
                    },
                    "consultant_id": {
                        "type": "string",
                        "description": "Consultant identifier, such as CON-405; selects that consultant's skill-gap option.",
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "utilization_dashboard")
        dispatch = {
            "utilization_dashboard": self._utilization_dashboard,
            "capacity_forecast": self._capacity_forecast,
            "bench_analysis": self._bench_analysis,
            "staffing_recommendation": self._staffing_recommendation,
            "skill_gap_options": self._skill_gap_options,
            "executive_impact_report": self._executive_impact_report,
        }
        handler = dispatch.get(operation)
        if handler is None:
            return f"**Error:** Unknown operation `{operation}`. Valid: {', '.join(dispatch.keys())}"
        return handler(**kwargs)

    # ------------------------------------------------------------------
    def _utilization_dashboard(self, **kwargs) -> str:
        lines = ["## Resource Utilization Dashboard\n"]
        firm_util = _firm_utilization()
        target = UTILIZATION_TARGETS["firm_target"]
        gap = round(target - firm_util, 1)
        bench = _bench_consultants()
        lines.append(f"**Firm utilization:** {firm_util}% (target: {target}%, gap: {gap}pp)")
        lines.append(f"**Total headcount:** {len(CONSULTANTS)}")
        lines.append(f"**Billable:** {len(CONSULTANTS) - len(bench)}")
        lines.append(f"**Bench:** {len(bench)}")
        lines.append(f"**Monthly bench cost:** ${_monthly_bench_cost():,.0f}\n")

        lines.append("| ID | Name | Level | Rate/Hr | Util % | Status | Project | End Date |")
        lines.append("|----|------|-------|---------|--------|--------|---------|----------|")
        for cid, c in CONSULTANTS.items():
            proj = c["current_project"] or "-"
            end = c["project_end"] or "-"
            flag = " **BENCH**" if c["status"] == "bench" else ""
            lines.append(
                f"| {cid} | {c['name']} | {c['level']} | ${c['rate_hr']} | "
                f"{c['utilization_pct']}% | {c['status']}{flag} | {proj[:22]} | {end} |"
            )

        lines.append("\n### Utilization by Level\n")
        lines.append("| Level | Headcount | Avg Util | Target | Status |")
        lines.append("|-------|-----------|----------|--------|--------|")
        for level in ("Senior", "Manager", "Mid", "Junior"):
            members = [c for c in CONSULTANTS.values() if c["level"] == level]
            if not members:
                continue
            avg = round(sum(c["utilization_pct"] for c in members) / len(members), 1)
            tgt = UTILIZATION_TARGETS.get(level, 80)
            status = "On Track" if avg >= tgt else "Below Target"
            lines.append(f"| {level} | {len(members)} | {avg}% | {tgt}% | {status} |")
        live = _live_bench()
        if live:
            seam = "n/a — enrichment seam"
            lines.append("\n### Live Tenant Consultant Bench (Dynamics bookable resources + bookings)\n")
            lines.append("| Consultant | Booked Hours | Bookings | Status | Rate/Hr | Skills |")
            lines.append("|------------|--------------|----------|--------|---------|--------|")
            for c in live:
                lines.append(
                    f"| {c['name']} | {c['booked_hours']} | {c['bookings']} | {c['status']} | "
                    f"{c['rate_hr'] or seam} | {c['skills'] or seam} |"
                )
            lines.append("\n(Booked hours are computed from the live booking calendar; "
                         "rates and skills await enrichment.)")
        else:
            lines.append("\n_Live tenant unreachable — showing embedded demo consultants only._")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _capacity_forecast(self, **kwargs) -> str:
        lines = ["## Capacity Forecast (Next 90 Days)\n"]
        lines.append("### Upcoming Project Endings\n")
        lines.append("| Consultant | Project | End Date | Level | Skills |")
        lines.append("|------------|---------|----------|-------|--------|")
        ending_soon = [(cid, c) for cid, c in CONSULTANTS.items()
                       if c["project_end"] and c["project_end"] <= "2026-06-30"]
        for cid, c in sorted(ending_soon, key=lambda x: x[1]["project_end"]):
            lines.append(
                f"| {c['name']} | {c['current_project']} | {c['project_end']} | "
                f"{c['level']} | {', '.join(c['skills'][:2])} |"
            )

        lines.append("\n### Pipeline Demand\n")
        lines.append("| Project | Start | Duration | Probability | Roles Needed |")
        lines.append("|---------|-------|----------|-------------|--------------|")
        for proj in PROJECT_PIPELINE:
            roles = "; ".join(f"{s} ({l})" for s, l, _ in proj["needs"])
            lines.append(
                f"| {proj['name']} | {proj['start']} | {proj['months']}mo | "
                f"{proj['probability']*100:.0f}% | {roles} |"
            )

        total_roles = sum(count for proj in PROJECT_PIPELINE for _, _, count in proj["needs"])
        lines.append(f"\n**Total roles in pipeline:** {total_roles}")
        lines.append(f"**Bench available:** {len(_bench_consultants())}")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _bench_analysis(self, **kwargs) -> str:
        lines = ["## Bench Analysis\n"]
        bench = _bench_consultants()
        monthly_cost = _monthly_bench_cost()
        lines.append(f"**Bench headcount:** {len(bench)}")
        lines.append(f"**Monthly bench cost:** ${monthly_cost:,.0f}")
        lines.append(f"**Annualized bench cost:** ${monthly_cost * 12:,.0f}\n")

        lines.append("| ID | Name | Level | Rate/Hr | Skills | Monthly Cost | Days on Bench |")
        lines.append("|----|------|-------|---------|--------|-------------|---------------|")
        for cid, c in bench.items():
            mc = BENCH_COST_PER_MONTH.get(c["level"], 14000)
            skills = ", ".join(c["skills"][:2])
            lines.append(
                f"| {cid} | {c['name']} | {c['level']} | ${c['rate_hr']} | {skills} | ${mc:,.0f} | est. 30+ |"
            )

        lines.append("\n### Skill Inventory on Bench\n")
        skill_counts = {}
        for c in bench.values():
            for s in c["skills"]:
                skill_counts[s] = skill_counts.get(s, 0) + 1
        lines.append("| Skill | Available |")
        lines.append("|-------|-----------|")
        for s, count in sorted(skill_counts.items(), key=lambda x: x[1], reverse=True):
            lines.append(f"| {s} | {count} |")

        lines.append(f"\n**Revenue opportunity if deployed:** ${sum(c['rate_hr'] * 160 for c in bench.values()):,.0f}/month")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _staffing_recommendation(self, **kwargs) -> str:
        lines = ["## Staffing Recommendations\n"]
        matches = _find_matches_for_pipeline()

        if matches:
            lines.append("### Bench-to-Pipeline Matches\n")
            lines.append("| Consultant | Project | Skill Match | Level | Probability | Start |")
            lines.append("|------------|---------|-------------|-------|-------------|-------|")
            for m in matches:
                lines.append(
                    f"| {m['consultant_name']} | {m['project']} | {m['skill_matched']} | "
                    f"{m['level']} | {m['probability']*100:.0f}% | {m['start']} |"
                )
            deployed_ids = {m["consultant_id"] for m in matches}
            deployed_cost = sum(
                BENCH_COST_PER_MONTH.get(CONSULTANTS[cid]["level"], 14000) for cid in deployed_ids
            )
            lines.append(f"\n**Bench cost saved if deployed:** ${deployed_cost:,.0f}/month")
        else:
            lines.append("No direct bench-to-pipeline matches found.\n")

        # Unmatched bench
        matched_ids = {m["consultant_id"] for m in matches}
        unmatched = {cid: c for cid, c in _bench_consultants().items() if cid not in matched_ids}
        if unmatched:
            lines.append("\n### Unmatched Bench Resources\n")
            lines.append("| Consultant | Level | Skills | Recommendation |")
            lines.append("|------------|-------|--------|----------------|")
            for cid, c in unmatched.items():
                rec = "Upskill to cloud/AI" if c["level"] in ("Mid", "Junior") else "Internal innovation project"
                lines.append(f"| {c['name']} | {c['level']} | {', '.join(c['skills'][:2])} | {rec} |")

        # Utilization projection
        bench = _bench_consultants()
        current_util = _firm_utilization()
        deployable = len(matches)
        total = len(CONSULTANTS)
        currently_billable = total - len(bench)
        projected_billable = currently_billable + deployable
        projected_util = round(projected_billable / total * 100 * 0.87, 1)  # weighted avg
        lines.append(f"\n### Projected Utilization Impact")
        lines.append(f"- Current firm utilization: **{current_util}%**")
        lines.append(f"- Projected after deployment: **{projected_util}%**")
        lines.append(f"- Target: **{UTILIZATION_TARGETS['firm_target']}%**")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _skill_gap_options(self, **kwargs) -> str:
        return _render_evidence_operation(
            "skill_gap_options", _evidence_selector("skill_gap_options", kwargs)
        )

    # ------------------------------------------------------------------
    def _executive_impact_report(self, **kwargs) -> str:
        return _render_evidence_operation(
            "executive_impact_report",
            _evidence_selector("executive_impact_report", kwargs),
        )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = ResourceUtilizationAgent()
    print("=" * 72)
    print("EMBEDDED DEMO CONSULTANTS + LIVE TENANT BENCH")
    print("(live section fetched over HTTP; falls back offline)")
    print("=" * 72)
    print(agent.perform(operation="utilization_dashboard"))
    print()
    for op in agent.metadata["operations"][1:]:
        print("=" * 72)
        print(agent.perform(operation=op))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
