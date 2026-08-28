---
name: "rar-aibast-agents-library-energy-regulatory-reporting"
description: "Tracks filing deadlines from live work items on a simulated Dynamics 365 tenant, with validation and audit prep that work offline."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/energy_regulatory_reporting", "rar_sha256": "45c64ca391d9bddeb695a36cb4a7c013ed744a91a2d50f7e637a81e3cbb93866", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["regulatory", "reporting", "epa", "ferc", "audit", "compliance", "energy"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/energy_regulatory_reporting`. The original RAPP
agent is preserved byte-for-byte in `regulatory_reporting_agent.py` and in the RCI capsule.

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

Energy Regulatory Reporting Agent — a template you are meant to mutate.

Manages regulatory report status tracking, data validation, submission
workflows, and audit readiness assessments for EPA, FERC, and state
regulatory filings.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live work items over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template a Dynamics task is reinterpreted as a regulatory
     reporting work item: its scheduled end is the filing deadline and
     overdue status is computed against the clock — e.g. the open task
     "Review service notes — CAS-260131" tied to a records-request
     backlog that exceeds a statutory deadline.
     Try: perform(operation="submission_tracker")
  2. No network? Everything falls back to the embedded demo layer below
     (REGULATORY_REPORTS / DATA_VALIDATION_RULES / AUDIT_FINDINGS) — the
     agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     ENERGY_REGULATORY_REPORTING_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your compliance
     tracker), or replace _fetch_collection() with your own API client.
     Fields the rest of the file needs are listed in
     _normalize_live_work_item() — everything else keeps working
     untouched. Fields marked "enrichment seam" in the output (authority,
     quality scores) are where you wire your filing systems.

OPERATIONS
  report_status | data_validation | submission_tracker | audit_readiness
  | emissions_summary | generate_regulatory_report | prepare_epa_submission
  kwargs: operation (required), report_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The regulatory reporting operation to perform.",
      "enum": [
        "report_status",
        "data_validation",
        "submission_tracker",
        "audit_readiness",
        "emissions_summary",
        "generate_regulatory_report",
        "prepare_epa_submission"
      ],
      "type": "string"
    },
    "report_id": {
      "description": "Optional report ID to filter results.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `regulatory_reporting_agent.py` and embedded as the fenced Python below (sha256 45c64ca391d9bdde…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `regulatory_reporting_agent.py` first:

```bash
python3 regulatory_reporting_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 regulatory_reporting_agent.py   # or on stdin
python3 regulatory_reporting_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Energy Regulatory Reporting Agent — a template you are meant to mutate.

Manages regulatory report status tracking, data validation, submission
workflows, and audit readiness assessments for EPA, FERC, and state
regulatory filings.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live work items over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template a Dynamics task is reinterpreted as a regulatory
     reporting work item: its scheduled end is the filing deadline and
     overdue status is computed against the clock — e.g. the open task
     "Review service notes — CAS-260131" tied to a records-request
     backlog that exceeds a statutory deadline.
     Try: perform(operation="submission_tracker")
  2. No network? Everything falls back to the embedded demo layer below
     (REGULATORY_REPORTS / DATA_VALIDATION_RULES / AUDIT_FINDINGS) — the
     agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     ENERGY_REGULATORY_REPORTING_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your compliance
     tracker), or replace _fetch_collection() with your own API client.
     Fields the rest of the file needs are listed in
     _normalize_live_work_item() — everything else keeps working
     untouched. Fields marked "enrichment seam" in the output (authority,
     quality scores) are where you wire your filing systems.

OPERATIONS
  report_status | data_validation | submission_tracker | audit_readiness
  | emissions_summary | generate_regulatory_report | prepare_epa_submission
  kwargs: operation (required), report_id
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timezone


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/energy_regulatory_reporting",
    "version": "1.2.0",
    "display_name": "Energy Regulatory Reporting Agent",
    "description": "Tracks filing deadlines from live work items on a simulated Dynamics 365 tenant, with validation and audit prep that work offline.",
    "author": "AIBAST",
    "tags": ["regulatory", "reporting", "epa", "ferc", "audit", "compliance", "energy"],
    "category": "energy",
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
#   export ENERGY_REGULATORY_REPORTING_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your compliance-tracker client.
# Downstream code only needs the fields produced by
# _normalize_live_work_item().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "ENERGY_REGULATORY_REPORTING_DATA_URL",
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


def _normalize_live_work_item(row):
    """Project a Dynamics task onto the reporting work-item shape this
    agent uses. THIS is the contract your replacement data source must
    meet — a dict with these keys. None means 'not available from CRM
    alone' and the renderers label it as an enrichment seam. In this
    template a Dynamics task is reinterpreted as a regulatory reporting
    work item and its scheduled end is the filing deadline."""
    state = row.get("statecode")
    deadline = str(row.get("scheduledend", ""))[:10]
    overdue = False
    if state == 0 and deadline:
        try:
            due = datetime.fromisoformat(deadline).replace(tzinfo=timezone.utc)
            overdue = due < datetime.now(timezone.utc)
        except ValueError:
            pass
    return {
        "name": row.get("subject", "untitled"),
        "regarding": row.get("regardingobjectidname", ""),
        "authority": None,   # enrichment seam — wire your filing systems
        "deadline": deadline or "n/a",
        "status": {0: "overdue" if overdue else "open",
                   1: "completed", 2: "canceled"}.get(state, "unknown"),
        "owner": row.get("owneridname", ""),
        "_live": True,
    }


def _live_work_items():
    """Live tenant reporting work items, open first; [] when offline."""
    items = [_normalize_live_work_item(t) for t in _fetch_collection("tasks")]
    items.sort(key=lambda x: (x["status"] in ("completed", "canceled"), x["deadline"]))
    return items


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

REGULATORY_REPORTS = {
    "RPT-9001": {
        "name": "EPA GHG Reporting Program (Subpart C)",
        "authority": "EPA",
        "facility": "Riverside Generating Station",
        "reporting_period": "CY 2025",
        "deadline": "2026-03-31",
        "status": "in_progress",
        "data_quality_score": 87,
        "completeness_pct": 78,
        "assignee": "Environmental Compliance Team",
        "last_updated": "2026-03-10",
    },
    "RPT-9002": {
        "name": "FERC Form 1 Annual Report",
        "authority": "FERC",
        "facility": "Corporate (All Facilities)",
        "reporting_period": "CY 2025",
        "deadline": "2026-04-18",
        "status": "in_progress",
        "data_quality_score": 92,
        "completeness_pct": 65,
        "assignee": "Regulatory Affairs",
        "last_updated": "2026-03-12",
    },
    "RPT-9003": {
        "name": "TCEQ Annual Emissions Inventory",
        "authority": "State - Texas",
        "facility": "Bayshore Refinery",
        "reporting_period": "CY 2025",
        "deadline": "2026-03-31",
        "status": "submitted",
        "data_quality_score": 95,
        "completeness_pct": 100,
        "assignee": "Environmental Compliance Team",
        "last_updated": "2026-03-05",
    },
    "RPT-9004": {
        "name": "Colorado Air Quality Control Division Report",
        "authority": "State - Colorado",
        "facility": "Ridgeline Coal Station",
        "reporting_period": "CY 2025",
        "deadline": "2026-04-30",
        "status": "not_started",
        "data_quality_score": 0,
        "completeness_pct": 0,
        "assignee": "Environmental Compliance Team",
        "last_updated": None,
    },
    "RPT-9005": {
        "name": "EPA Toxics Release Inventory (TRI)",
        "authority": "EPA",
        "facility": "Bayshore Refinery",
        "reporting_period": "CY 2025",
        "deadline": "2026-07-01",
        "status": "in_progress",
        "data_quality_score": 74,
        "completeness_pct": 42,
        "assignee": "Health & Safety Team",
        "last_updated": "2026-02-28",
    },
    "RPT-9006": {
        "name": "PHMSA Annual Pipeline Safety Report",
        "authority": "PHMSA",
        "facility": "Northeast Corridor Pipeline",
        "reporting_period": "CY 2025",
        "deadline": "2026-03-15",
        "status": "overdue",
        "data_quality_score": 81,
        "completeness_pct": 90,
        "assignee": "Pipeline Operations",
        "last_updated": "2026-03-14",
    },
}

DATA_VALIDATION_RULES = {
    "emissions_data": {
        "rules": ["Non-negative values", "Year-over-year variance < 25%", "Mass balance check", "Unit conversion validation"],
        "source_systems": ["CEMS", "Fuel metering", "Production logs"],
    },
    "financial_data": {
        "rules": ["Reconciliation to GL", "Rate base validation", "Depreciation schedule check", "Intercompany elimination"],
        "source_systems": ["SAP", "PowerPlan", "Hyperion"],
    },
    "safety_data": {
        "rules": ["Incident classification verification", "Mileage data reconciliation", "Leak survey completeness"],
        "source_systems": ["PIMS", "GIS", "Inspection database"],
    },
}

AUDIT_FINDINGS = {
    "AUD-001": {"report": "RPT-9001", "finding": "Missing CEMS calibration records for Q3", "severity": "medium", "status": "open", "due_date": "2026-03-25"},
    "AUD-002": {"report": "RPT-9002", "finding": "Depreciation schedule mismatch with PowerPlan", "severity": "high", "status": "remediated", "due_date": "2026-03-15"},
    "AUD-003": {"report": "RPT-9005", "finding": "Threshold calculation methodology not documented", "severity": "low", "status": "open", "due_date": "2026-05-01"},
    "AUD-004": {"report": "RPT-9006", "finding": "Pipeline mileage discrepancy between GIS and PIMS", "severity": "high", "status": "open", "due_date": "2026-03-20"},
}

EMISSIONS_SUMMARY = [
    {
        "facility": "Riverside Generating Station",
        "report_id": "RPT-9001",
        "scope_1_co2e": 482000,
        "year_over_year_pct": -6.2,
        "quality_score": 87,
    },
    {
        "facility": "Bayshore Refinery",
        "report_id": "RPT-9005",
        "scope_1_co2e": 890000,
        "year_over_year_pct": -4.8,
        "quality_score": 74,
    },
    {
        "facility": "Ridgeline Coal Station",
        "report_id": "RPT-9004",
        "scope_1_co2e": 1420000,
        "year_over_year_pct": -8.1,
        "quality_score": 0,
    },
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _report_status():
    reports = []
    for rid, r in REGULATORY_REPORTS.items():
        reports.append({
            "id": rid, "name": r["name"], "authority": r["authority"],
            "facility": r["facility"], "deadline": r["deadline"],
            "status": r["status"], "completeness_pct": r["completeness_pct"],
            "data_quality": r["data_quality_score"], "assignee": r["assignee"],
        })
    reports.sort(key=lambda x: x["deadline"])
    overdue = sum(1 for r in reports if r["status"] == "overdue")
    submitted = sum(1 for r in reports if r["status"] == "submitted")
    return {"reports": reports, "total": len(reports), "overdue": overdue, "submitted": submitted}


def _data_validation():
    validations = []
    for rid, r in REGULATORY_REPORTS.items():
        if r["status"] in ("not_started",):
            continue
        issues = []
        if r["data_quality_score"] < 80:
            issues.append(f"Data quality score below threshold ({r['data_quality_score']}/100)")
        if r["completeness_pct"] < 100 and r["status"] != "submitted":
            issues.append(f"Data collection incomplete ({r['completeness_pct']}%)")
        validations.append({
            "report_id": rid, "name": r["name"],
            "quality_score": r["data_quality_score"],
            "completeness": r["completeness_pct"],
            "issues": issues, "passed": len(issues) == 0,
        })
    return {"validations": validations, "pass_rate": round(sum(1 for v in validations if v["passed"]) / len(validations) * 100, 1) if validations else 0}


def _submission_tracker():
    tracker = []
    for rid, r in REGULATORY_REPORTS.items():
        tracker.append({
            "id": rid, "name": r["name"], "authority": r["authority"],
            "deadline": r["deadline"], "status": r["status"],
            "last_updated": r["last_updated"] or "N/A",
        })
    tracker.sort(key=lambda x: x["deadline"])
    return {"submissions": tracker}


def _audit_readiness():
    findings_by_report = {}
    for aid, af in AUDIT_FINDINGS.items():
        rid = af["report"]
        if rid not in findings_by_report:
            findings_by_report[rid] = []
        findings_by_report[rid].append({
            "id": aid, "finding": af["finding"],
            "severity": af["severity"], "status": af["status"],
            "due_date": af["due_date"],
        })
    open_findings = sum(1 for af in AUDIT_FINDINGS.values() if af["status"] == "open")
    high_sev = sum(1 for af in AUDIT_FINDINGS.values() if af["severity"] == "high" and af["status"] == "open")
    return {"findings_by_report": findings_by_report, "total_findings": len(AUDIT_FINDINGS),
            "open_findings": open_findings, "high_severity_open": high_sev}


def _report_risks(report_id):
    report = REGULATORY_REPORTS[report_id]
    risks = []
    if report["completeness_pct"] < 100:
        risks.append(f"Data is {report['completeness_pct']}% complete")
    if report["data_quality_score"] < 80:
        risks.append(f"Quality score {report['data_quality_score']}/100 is below threshold")
    for finding in AUDIT_FINDINGS.values():
        if finding["report"] == report_id and finding["status"] == "open":
            risks.append(finding["finding"])
    return risks


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

class RegulatoryReportingAgent(BasicAgent):
    """Regulatory reporting status and audit readiness agent."""

    def __init__(self):
        self.name = "RegulatoryReportingAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "report_status",
                            "data_validation",
                            "submission_tracker",
                            "audit_readiness",
                            "emissions_summary",
                            "generate_regulatory_report",
                            "prepare_epa_submission",
                        ],
                        "description": "The regulatory reporting operation to perform.",
                    },
                    "report_id": {
                        "type": "string",
                        "description": "Optional report ID to filter results.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "report_status")
        if op == "report_status":
            return self._report_status()
        elif op == "data_validation":
            return self._data_validation()
        elif op == "submission_tracker":
            return self._submission_tracker()
        elif op == "audit_readiness":
            return self._audit_readiness()
        elif op == "emissions_summary":
            return self._emissions_summary()
        elif op == "generate_regulatory_report":
            return self._generate_regulatory_report(kwargs.get("report_id"))
        elif op == "prepare_epa_submission":
            return self._prepare_epa_submission(kwargs.get("report_id"))
        return f"**Error:** Unknown operation `{op}`."

    def _report_status(self) -> str:
        data = _report_status()
        lines = [
            "# Regulatory Report Status",
            "",
            f"**Total Reports:** {data['total']} | **Submitted:** {data['submitted']} | **Overdue:** {data['overdue']}",
            "",
            "| Report | Authority | Facility | Deadline | Status | Complete | Quality |",
            "|--------|-----------|----------|----------|--------|---------|---------|",
        ]
        for r in data["reports"]:
            lines.append(
                f"| {r['name']} | {r['authority']} | {r['facility']} "
                f"| {r['deadline']} | {r['status'].upper()} | {r['completeness_pct']}% | {r['data_quality']}/100 |"
            )
        return "\n".join(lines)

    def _data_validation(self) -> str:
        data = _data_validation()
        lines = [
            "# Data Validation Results",
            "",
            f"**Validation Pass Rate:** {data['pass_rate']}%",
            "",
            "| Report | Quality Score | Completeness | Issues | Passed |",
            "|--------|-------------|-------------|--------|--------|",
        ]
        for v in data["validations"]:
            passed = "YES" if v["passed"] else "NO"
            issue_str = "; ".join(v["issues"]) if v["issues"] else "None"
            lines.append(
                f"| {v['name']} | {v['quality_score']}/100 | {v['completeness']}% | {issue_str} | {passed} |"
            )
        return "\n".join(lines)

    def _submission_tracker(self) -> str:
        live = _live_work_items()
        if live:
            open_items = [i for i in live if i["status"] in ("open", "overdue")]
            overdue = [i for i in live if i["status"] == "overdue"]
            lines = [
                "# Submission Tracker (live tenant data)",
                "",
                f"**Reporting work items:** {len(live)} | "
                f"**Open:** {len(open_items)} | **Overdue:** {len(overdue)}",
                "",
                "| Work Item | Regarding | Authority | Deadline | Status | Owner |",
                "|-----------|-----------|-----------|----------|--------|-------|",
            ]
            for s in live[:15]:
                lines.append(
                    f"| {s['name']} | {s['regarding']} | n/a — enrichment seam "
                    f"| {s['deadline']} | {s['status'].upper()} | {s['owner']} |"
                )
            if len(live) > 15:
                lines.append(f"| ... and {len(live) - 15} more | | | | | |")
            lines.append("")
            lines.append("_Source: live Static Dynamics 365 tenant (tasks). A task is "
                         "reinterpreted as a reporting work item; overdue status is real "
                         "clock math against its scheduled end._")
            return "\n".join(lines)

        data = _submission_tracker()
        lines = [
            "# Submission Tracker (embedded demo data — offline)",
            "",
            "| Report | Authority | Deadline | Status | Last Updated |",
            "|--------|-----------|----------|--------|-------------|",
        ]
        for s in data["submissions"]:
            lines.append(
                f"| {s['name']} | {s['authority']} | {s['deadline']} "
                f"| {s['status'].upper()} | {s['last_updated']} |"
            )
        return "\n".join(lines)

    def _audit_readiness(self) -> str:
        data = _audit_readiness()
        lines = [
            "# Audit Readiness Assessment",
            "",
            f"**Total Findings:** {data['total_findings']} | "
            f"**Open:** {data['open_findings']} | "
            f"**High Severity Open:** {data['high_severity_open']}",
            "",
        ]
        for rid, findings in data["findings_by_report"].items():
            rpt_name = REGULATORY_REPORTS.get(rid, {}).get("name", rid)
            lines.append(f"## {rpt_name}")
            lines.append("")
            lines.append("| Finding | Severity | Status | Due Date |")
            lines.append("|---------|----------|--------|----------|")
            for f in findings:
                lines.append(f"| {f['finding']} | {f['severity'].upper()} | {f['status'].upper()} | {f['due_date']} |")
            lines.append("")
        return "\n".join(lines)

    def _emissions_summary(self) -> str:
        total = sum(row["scope_1_co2e"] for row in EMISSIONS_SUMMARY)
        lines = [
            "# Consolidated Emissions Summary",
            "",
            f"**Portfolio Scope 1 CO2e:** {total:,} tonnes",
            "",
            "| Facility | Report | Scope 1 CO2e | YoY Change | Quality |",
            "|----------|--------|--------------|------------|---------|",
        ]
        for row in EMISSIONS_SUMMARY:
            lines.append(
                f"| {row['facility']} | {row['report_id']} | {row['scope_1_co2e']:,} "
                f"| {row['year_over_year_pct']}% | {row['quality_score']}/100 |"
            )
        lines.extend([
            "",
            "**Evidence:** Energy Operations demo 02:02-02:20 — emissions data "
            "consolidation and a rich summary for reporting progress.",
        ])
        return "\n".join(lines)

    def _generate_regulatory_report(self, report_id) -> str:
        if not report_id:
            return (
                "# Generate Regulatory Report\n\nProvide an exact `report_id`. "
                f"Available IDs: {', '.join(sorted(REGULATORY_REPORTS))}."
            )
        report = REGULATORY_REPORTS.get(report_id)
        if not report:
            return f"**Error:** Unknown report_id `{report_id}`."
        risks = _report_risks(report_id)
        lines = [
            f"# Generated Regulatory Report — {report_id}",
            "",
            f"- **Filing:** {report['name']}",
            f"- **Authority:** {report['authority']}",
            f"- **Reporting Period:** {report['reporting_period']}",
            f"- **Completeness:** {report['completeness_pct']}%",
            f"- **Data Quality:** {report['data_quality_score']}/100",
            "",
            "## Compliance Checks",
            "",
        ]
        lines.extend(f"- RISK: {risk}" for risk in risks)
        if not risks:
            lines.append("- PASS: No pre-filing risks identified.")
        lines.extend([
            "",
            "**Evidence:** Energy Operations demo 02:02-02:30 — automated report "
            "generation and compliance checks before filing.",
        ])
        return "\n".join(lines)

    def _prepare_epa_submission(self, report_id) -> str:
        if not report_id:
            return "# Prepare EPA Submission\n\nProvide an exact EPA `report_id`: RPT-9001 or RPT-9005."
        report = REGULATORY_REPORTS.get(report_id)
        if not report:
            return f"**Error:** Unknown report_id `{report_id}`."
        if report["authority"] != "EPA":
            return f"**Error:** Report `{report_id}` is not an EPA filing."
        risks = _report_risks(report_id)
        disposition = "HOLD — resolve risks before filing" if risks else "READY"
        lines = [
            f"# EPA Submission Preparation — {report_id}",
            "",
            f"- **Filing:** {report['name']}",
            f"- **Disposition:** {disposition}",
            f"- **Risk Count:** {len(risks)}",
        ]
        lines.extend(f"- **Risk:** {risk}" for risk in risks)
        lines.extend([
            "",
            "## Simulated Write Receipt",
            "",
            "- **Action:** Prepare submission package for the EPA portal.",
            "- **Mode:** dry-run; no filing was transmitted and no live record was mutated.",
            "- **Evidence:** Energy Operations demo 02:20-02:30.",
        ])
        return "\n".join(lines)


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    agent = RegulatoryReportingAgent()
    print("=" * 60)
    print("LIVE TENANT WORK ITEMS (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="submission_tracker"))
    print()
    print("=" * 60)
    print("EMBEDDED DEMO FILINGS (works offline)")
    for op in ["report_status", "data_validation", "audit_readiness"]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
