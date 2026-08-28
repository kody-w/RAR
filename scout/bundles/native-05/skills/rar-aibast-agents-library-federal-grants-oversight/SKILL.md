---
name: "rar-aibast-agents-library-federal-grants-oversight"
description: "Monitors grant compliance events from a live simulated Dynamics 365 tenant, with dashboards and audit prep that work offline."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/federal_grants_oversight", "rar_sha256": "3e7d38620ad3562d8228c9c5e6b12fe343466117a3984cfb18d991f90dbfa347", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["grants", "oversight", "compliance", "audit", "federal", "reporting"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/federal_grants_oversight`. The original RAPP
agent is preserved byte-for-byte in `federal_grants_oversight_agent.py` and in the RCI capsule.

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

Federal Grants Oversight Agent — a template you are meant to mutate.

Monitors federal grant programs with dashboards, compliance tracking,
reporting status updates, and audit preparation support for grant
program managers and oversight officers.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live oversight events over real HTTP from
     the globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template a grant compliance finding is represented as a
     Dynamics case at a government account — e.g. CAS-260136 "Grant
     drawdown report rejected for missing form" at Federal Plaza
     Services Agency.
     Try: perform(operation="compliance_monitoring")
  2. No network? Everything falls back to the embedded demo layer below
     (FEDERAL_GRANTS / COMPLIANCE_REQUIREMENTS / AUDIT_FINDINGS) — the
     agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     FEDERAL_GRANTS_OVERSIGHT_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your grants
     management system), or replace _fetch_collection() with your own
     API client. Fields the rest of the file needs are listed in
     _normalize_live_finding() — everything else keeps working
     untouched. Fields marked "enrichment seam" in the output (CFDA
     numbers, questioned costs) are where you wire your payment
     management system.

OPERATIONS
  grants_dashboard | compliance_monitoring | reporting_status
  | audit_preparation
  kwargs: operation (required), grant_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "grant_id": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "grants_dashboard",
        "compliance_monitoring",
        "reporting_status",
        "audit_preparation"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `federal_grants_oversight_agent.py` and embedded as the fenced Python below (sha256 3e7d38620ad3562d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `federal_grants_oversight_agent.py` first:

```bash
python3 federal_grants_oversight_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 federal_grants_oversight_agent.py   # or on stdin
python3 federal_grants_oversight_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Federal Grants Oversight Agent — a template you are meant to mutate.

Monitors federal grant programs with dashboards, compliance tracking,
reporting status updates, and audit preparation support for grant
program managers and oversight officers.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live oversight events over real HTTP from
     the globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template a grant compliance finding is represented as a
     Dynamics case at a government account — e.g. CAS-260136 "Grant
     drawdown report rejected for missing form" at Federal Plaza
     Services Agency.
     Try: perform(operation="compliance_monitoring")
  2. No network? Everything falls back to the embedded demo layer below
     (FEDERAL_GRANTS / COMPLIANCE_REQUIREMENTS / AUDIT_FINDINGS) — the
     agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     FEDERAL_GRANTS_OVERSIGHT_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your grants
     management system), or replace _fetch_collection() with your own
     API client. Fields the rest of the file needs are listed in
     _normalize_live_finding() — everything else keeps working
     untouched. Fields marked "enrichment seam" in the output (CFDA
     numbers, questioned costs) are where you wire your payment
     management system.

OPERATIONS
  grants_dashboard | compliance_monitoring | reporting_status
  | audit_preparation
  kwargs: operation (required), grant_id
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/federal_grants_oversight",
    "version": "1.1.0",
    "display_name": "Federal Grants Oversight Agent",
    "description": "Monitors grant compliance events from a live simulated Dynamics 365 tenant, with dashboards and audit prep that work offline.",
    "author": "AIBAST",
    "tags": ["grants", "oversight", "compliance", "audit", "federal", "reporting"],
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
#   export FEDERAL_GRANTS_OVERSIGHT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your grants-management client.
# Downstream code only needs the fields produced by
# _normalize_live_finding().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "FEDERAL_GRANTS_OVERSIGHT_DATA_URL",
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


def _normalize_live_finding(row):
    """Project a Dynamics case onto the oversight-finding shape this
    agent uses. THIS is the contract your replacement data source must
    meet — a dict with these keys. None means 'not available from CRM
    alone' and the renderers label it as an enrichment seam. In this
    template a grant compliance finding is represented as a Dynamics
    case at a government account."""
    return {
        "id": row.get("ticketnumber", ""),
        "recipient": row.get("customeridname", "Unknown"),
        "finding": row.get("title", "untitled"),
        "severity": {1: "high", 2: "moderate", 3: "low"}.get(row.get("prioritycode"), "moderate"),
        "status": "open" if row.get("statecode") == 0 else "resolved",
        "opened": str(row.get("createdon", ""))[:10],
        "cfda": None,             # enrichment seam — wire your grants system
        "questioned_cost": None,  # enrichment seam — wire payment management
        "_live": True,
    }


def _live_findings():
    """Live oversight findings: cases at government accounts; []
    when offline."""
    accounts = _fetch_collection("accounts")
    if not accounts:
        return []
    gov_names = {
        a["name"] for a in accounts
        if "government" in str(a.get("industrycode", "")).lower() and a.get("name")
    }
    return [
        _normalize_live_finding(i)
        for i in _fetch_collection("incidents")
        if i.get("customeridname") in gov_names
    ]


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

FEDERAL_GRANTS = {
    "GRT-2025-4401": {
        "program": "Homeland Security Grant Program (HSGP)",
        "cfda": "97.067",
        "recipient": "State of Virginia — Dept. of Emergency Management",
        "award_amount": 8750000,
        "federal_share": 0.75,
        "period_start": "2024-10-01",
        "period_end": "2027-09-30",
        "status": "active",
        "funds_drawn": 3125000,
        "milestones": {
            "equipment_procurement": {"due": "2025-06-30", "status": "in_progress", "pct": 62},
            "training_exercises": {"due": "2025-12-31", "status": "on_track", "pct": 35},
            "final_report": {"due": "2027-09-30", "status": "pending", "pct": 0},
        },
    },
    "GRT-2025-4402": {
        "program": "Community Development Block Grant (CDBG)",
        "cfda": "14.218",
        "recipient": "City of Richmond — Housing Authority",
        "award_amount": 3200000,
        "federal_share": 1.0,
        "period_start": "2025-01-01",
        "period_end": "2026-12-31",
        "status": "active",
        "funds_drawn": 480000,
        "milestones": {
            "needs_assessment": {"due": "2025-03-31", "status": "complete", "pct": 100},
            "construction_phase_1": {"due": "2025-09-30", "status": "in_progress", "pct": 28},
            "construction_phase_2": {"due": "2026-06-30", "status": "pending", "pct": 0},
            "close_out": {"due": "2026-12-31", "status": "pending", "pct": 0},
        },
    },
    "GRT-2025-4403": {
        "program": "COPS Hiring Program (CHP)",
        "cfda": "16.710",
        "recipient": "Metro Police Department — District 5",
        "award_amount": 1875000,
        "federal_share": 0.75,
        "period_start": "2024-07-01",
        "period_end": "2027-06-30",
        "status": "active",
        "funds_drawn": 937500,
        "milestones": {
            "hiring_cohort_1": {"due": "2025-01-15", "status": "complete", "pct": 100},
            "hiring_cohort_2": {"due": "2025-07-15", "status": "in_progress", "pct": 45},
            "retention_review": {"due": "2026-07-15", "status": "pending", "pct": 0},
            "final_report": {"due": "2027-06-30", "status": "pending", "pct": 0},
        },
    },
    "GRT-2025-4404": {
        "program": "Title III — Strengthening Institutions",
        "cfda": "84.031",
        "recipient": "Westfield Community College",
        "award_amount": 2100000,
        "federal_share": 1.0,
        "period_start": "2024-10-01",
        "period_end": "2029-09-30",
        "status": "active",
        "funds_drawn": 420000,
        "milestones": {
            "curriculum_redesign": {"due": "2025-08-31", "status": "in_progress", "pct": 55},
            "technology_upgrade": {"due": "2026-03-31", "status": "pending", "pct": 0},
            "faculty_development": {"due": "2027-09-30", "status": "pending", "pct": 0},
            "sustainability_plan": {"due": "2029-06-30", "status": "pending", "pct": 0},
        },
    },
}

COMPLIANCE_REQUIREMENTS = {
    "2 CFR 200": {
        "title": "Uniform Administrative Requirements",
        "sections": {
            "200.302": {"name": "Financial Management", "frequency": "continuous"},
            "200.303": {"name": "Internal Controls", "frequency": "continuous"},
            "200.328": {"name": "Financial Reporting", "frequency": "quarterly"},
            "200.329": {"name": "Performance Reporting", "frequency": "semi-annual"},
            "200.344": {"name": "Closeout", "frequency": "end_of_grant"},
        },
    },
    "Single Audit": {
        "title": "Single Audit Act (A-133)",
        "sections": {
            "threshold": {"name": "Expenditure Threshold ($750K)", "frequency": "annual"},
            "findings": {"name": "Prior Year Findings Follow-up", "frequency": "annual"},
            "schedule": {"name": "Schedule of Expenditures (SEFA)", "frequency": "annual"},
        },
    },
}

AUDIT_FINDINGS = [
    {"id": "AF-2024-01", "grant": "GRT-2025-4401", "severity": "low", "finding": "Late submission of SF-425 Q2 report by 8 days", "status": "resolved", "corrective_action": "Automated reminders implemented"},
    {"id": "AF-2024-02", "grant": "GRT-2025-4402", "severity": "moderate", "finding": "Cost allocation methodology not documented for shared personnel", "status": "in_progress", "corrective_action": "Cost allocation plan under review"},
    {"id": "AF-2024-03", "grant": "GRT-2025-4403", "severity": "low", "finding": "Equipment inventory tags missing on 3 of 47 items", "status": "resolved", "corrective_action": "Physical inventory completed and reconciled"},
    {"id": "AF-2023-07", "grant": "GRT-2025-4404", "severity": "high", "finding": "Supplanting concern — state funding reduced concurrent with federal award", "status": "in_progress", "corrective_action": "MOE documentation being compiled by finance office"},
]

REPORTING_SCHEDULE = {
    "SF-425": {"name": "Federal Financial Report", "frequency": "quarterly", "next_due": "2025-04-30"},
    "SF-PPR": {"name": "Performance Progress Report", "frequency": "semi-annual", "next_due": "2025-06-30"},
    "A-133": {"name": "Single Audit Report", "frequency": "annual", "next_due": "2025-03-31"},
    "FFATA": {"name": "FFATA Sub-award Report", "frequency": "monthly", "next_due": "2025-04-15"},
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _portfolio_summary():
    """Compute aggregate portfolio metrics."""
    total_awarded = sum(g["award_amount"] for g in FEDERAL_GRANTS.values())
    total_drawn = sum(g["funds_drawn"] for g in FEDERAL_GRANTS.values())
    draw_rate = round((total_drawn / total_awarded) * 100, 1) if total_awarded else 0
    return {"total_awarded": total_awarded, "total_drawn": total_drawn, "draw_rate": draw_rate, "grant_count": len(FEDERAL_GRANTS)}


def _compliance_score(grant_id):
    """Compute compliance score for a grant based on findings."""
    findings = [f for f in AUDIT_FINDINGS if f["grant"] == grant_id]
    if not findings:
        return 100.0
    deductions = {"low": 5, "moderate": 15, "high": 30}
    total_deduction = sum(deductions.get(f["severity"], 0) for f in findings if f["status"] != "resolved")
    return max(0, 100 - total_deduction)


def _milestone_health(grant):
    """Assess milestone health across a grant."""
    milestones = grant["milestones"]
    total = len(milestones)
    complete = sum(1 for m in milestones.values() if m["status"] == "complete")
    at_risk = sum(1 for m in milestones.values() if m["status"] == "in_progress" and m["pct"] < 40)
    return {"total": total, "complete": complete, "at_risk": at_risk}


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class FederalGrantsOversightAgent(BasicAgent):
    """Federal grants oversight agent for program monitoring and compliance."""

    def __init__(self):
        self.name = "FederalGrantsOversightAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Federal Grants Oversight Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "grants_dashboard",
                            "compliance_monitoring",
                            "reporting_status",
                            "audit_preparation",
                        ],
                    },
                    "grant_id": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "grants_dashboard")
        dispatch = {
            "grants_dashboard": self._grants_dashboard,
            "compliance_monitoring": self._compliance_monitoring,
            "reporting_status": self._reporting_status,
            "audit_preparation": self._audit_preparation,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        return handler(**kwargs)

    def _grants_dashboard(self, **kwargs) -> str:
        summary = _portfolio_summary()
        lines = ["# Federal Grants Dashboard\n"]
        lines.append(f"**Total Awards:** {summary['grant_count']}")
        lines.append(f"**Total Awarded:** ${summary['total_awarded']:,.0f}")
        lines.append(f"**Total Drawn:** ${summary['total_drawn']:,.0f}")
        lines.append(f"**Draw Rate:** {summary['draw_rate']}%\n")
        lines.append("## Grant Portfolio\n")
        lines.append("| Grant ID | Program | Recipient | Award | Drawn | Status |")
        lines.append("|---|---|---|---|---|---|")
        for gid, g in FEDERAL_GRANTS.items():
            lines.append(
                f"| {gid} | {g['program']} | {g['recipient']} "
                f"| ${g['award_amount']:,.0f} | ${g['funds_drawn']:,.0f} | {g['status'].title()} |"
            )
        lines.append("\n## Milestone Summary\n")
        for gid, g in FEDERAL_GRANTS.items():
            health = _milestone_health(g)
            lines.append(f"- **{gid}:** {health['complete']}/{health['total']} complete, {health['at_risk']} at risk")
        return "\n".join(lines)

    def _compliance_monitoring(self, **kwargs) -> str:
        live = _live_findings()
        if live:
            open_findings = [f for f in live if f["status"] == "open"]
            lines = ["# Compliance Monitoring Report (live tenant data)\n"]
            lines.append(f"**Oversight events at government accounts:** {len(live)} "
                         f"({len(open_findings)} open)\n")
            lines.append("## Live Findings\n")
            lines.append("| Case | Recipient | Finding | Severity | Status | Opened | Questioned Cost |")
            lines.append("|---|---|---|---|---|---|---|")
            for f in sorted(live, key=lambda x: (x["status"] != "open", x["opened"])):
                lines.append(
                    f"| {f['id']} | {f['recipient']} | {f['finding']} | {f['severity'].upper()} "
                    f"| {f['status'].title()} | {f['opened']} | n/a — enrichment seam |"
                )
            lines.append("\n## Regulatory Framework\n")
            for reg_id, reg in COMPLIANCE_REQUIREMENTS.items():
                lines.append(f"### {reg_id} — {reg['title']}\n")
                for sec_id, sec in reg["sections"].items():
                    lines.append(f"- **{sec_id}:** {sec['name']} ({sec['frequency']})")
                lines.append("")
            lines.append("_Source: live Static Dynamics 365 tenant (accounts + incidents). "
                         "A grant compliance finding is represented as a Dynamics case at a "
                         "government account; CFDA and questioned costs are enrichment seams._")
            return "\n".join(lines)

        lines = ["# Compliance Monitoring Report (embedded demo data — offline)\n"]
        lines.append("## Grant Compliance Scores\n")
        lines.append("| Grant ID | Program | Compliance Score |")
        lines.append("|---|---|---|")
        for gid, g in FEDERAL_GRANTS.items():
            score = _compliance_score(gid)
            lines.append(f"| {gid} | {g['program']} | {score}% |")
        lines.append("\n## Regulatory Framework\n")
        for reg_id, reg in COMPLIANCE_REQUIREMENTS.items():
            lines.append(f"### {reg_id} — {reg['title']}\n")
            for sec_id, sec in reg["sections"].items():
                lines.append(f"- **{sec_id}:** {sec['name']} ({sec['frequency']})")
            lines.append("")
        lines.append("## Active Findings\n")
        active = [f for f in AUDIT_FINDINGS if f["status"] != "resolved"]
        if active:
            lines.append("| Finding ID | Grant | Severity | Finding | Status |")
            lines.append("|---|---|---|---|---|")
            for f in active:
                lines.append(f"| {f['id']} | {f['grant']} | {f['severity'].upper()} | {f['finding']} | {f['status']} |")
        else:
            lines.append("No active findings.")
        return "\n".join(lines)

    def _reporting_status(self, **kwargs) -> str:
        lines = ["# Grant Reporting Status\n"]
        lines.append("## Upcoming Reports\n")
        lines.append("| Report | Name | Frequency | Next Due |")
        lines.append("|---|---|---|---|")
        for rid, r in REPORTING_SCHEDULE.items():
            lines.append(f"| {rid} | {r['name']} | {r['frequency'].title()} | {r['next_due']} |")
        lines.append("\n## Grant-Level Milestones\n")
        for gid, g in FEDERAL_GRANTS.items():
            lines.append(f"### {gid} — {g['program']}\n")
            lines.append("| Milestone | Due Date | Status | Progress |")
            lines.append("|---|---|---|---|")
            for mname, mdata in g["milestones"].items():
                display = mname.replace("_", " ").title()
                lines.append(f"| {display} | {mdata['due']} | {mdata['status'].replace('_', ' ').title()} | {mdata['pct']}% |")
            lines.append("")
        return "\n".join(lines)

    def _audit_preparation(self, **kwargs) -> str:
        lines = ["# Audit Preparation Report\n"]
        lines.append("## Prior Findings Status\n")
        lines.append("| Finding ID | Grant | Severity | Finding | Status | Corrective Action |")
        lines.append("|---|---|---|---|---|---|")
        for f in AUDIT_FINDINGS:
            lines.append(
                f"| {f['id']} | {f['grant']} | {f['severity'].upper()} "
                f"| {f['finding']} | {f['status'].replace('_', ' ').title()} | {f['corrective_action']} |"
            )
        resolved = sum(1 for f in AUDIT_FINDINGS if f["status"] == "resolved")
        total = len(AUDIT_FINDINGS)
        lines.append(f"\n**Findings Resolved:** {resolved}/{total}")
        lines.append("\n## Audit Readiness Checklist\n")
        checklist = [
            "Schedule of Expenditures of Federal Awards (SEFA) prepared",
            "Cost allocation plans current and documented",
            "Subrecipient monitoring documentation complete",
            "Equipment inventory reconciled",
            "Time-and-effort certifications on file",
            "Procurement documentation meets federal standards",
            "Financial reconciliation between GL and drawdowns",
            "Prior year corrective action plans implemented",
        ]
        for item in checklist:
            lines.append(f"- [ ] {item}")
        lines.append("\n## Single Audit Threshold Analysis\n")
        total_expended = sum(g["funds_drawn"] for g in FEDERAL_GRANTS.values())
        threshold = 750000
        lines.append(f"- **Total Federal Expenditures:** ${total_expended:,.0f}")
        lines.append(f"- **Single Audit Threshold:** ${threshold:,.0f}")
        above = "Yes" if total_expended >= threshold else "No"
        lines.append(f"- **Audit Required:** {above}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = FederalGrantsOversightAgent()
    print("=" * 60)
    print("LIVE TENANT OVERSIGHT EVENTS (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="compliance_monitoring"))
    print()
    print("=" * 60)
    print("EMBEDDED DEMO PORTFOLIO (works offline)")
    print(agent.perform(operation="grants_dashboard"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="reporting_status"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="audit_preparation"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
