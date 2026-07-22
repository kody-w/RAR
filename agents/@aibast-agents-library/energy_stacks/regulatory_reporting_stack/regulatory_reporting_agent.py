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
