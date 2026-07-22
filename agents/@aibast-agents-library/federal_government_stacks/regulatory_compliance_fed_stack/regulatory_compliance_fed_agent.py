"""
Regulatory Compliance (Federal) Agent — a template you are meant to mutate.

Provides compliance dashboards, gap analyses, remediation planning,
and audit readiness assessments for federal regulatory frameworks
including FISMA, FedRAMP, and NIST standards.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live remediation records over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template a Dynamics task is reinterpreted as a POA&M-style
     remediation action: its owner, due date, and percent complete are
     real record values — e.g. the open task "Review service notes —
     CAS-260131" tied to a statutory-deadline backlog.
     Try: perform(operation="remediation_plan")
  2. No network? Everything falls back to the embedded demo layer below
     (FEDERAL_REGULATIONS / COMPLIANCE_GAPS / REMEDIATION_ACTIONS) —
     the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     REGULATORY_COMPLIANCE_FED_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your GRC platform),
     or replace _fetch_collection() with your own API client. Fields
     the rest of the file needs are listed in
     _normalize_live_remediation() — everything else keeps working
     untouched. Fields marked "enrichment seam" in the output (control
     IDs, frameworks) are where you wire your GRC system.

OPERATIONS
  compliance_dashboard | gap_analysis | remediation_plan
  | audit_readiness
  kwargs: operation (required), regulation
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/regulatory_compliance_fed",
    "version": "1.1.0",
    "display_name": "Regulatory Compliance (Federal) Agent",
    "description": "Tracks remediation from live tasks on a simulated Dynamics 365 tenant, with FISMA/FedRAMP gap analysis that works offline.",
    "author": "AIBAST",
    "tags": ["compliance", "FISMA", "FedRAMP", "NIST", "audit", "federal", "regulatory"],
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
#   export REGULATORY_COMPLIANCE_FED_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your GRC-platform client.
# Downstream code only needs the fields produced by
# _normalize_live_remediation().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "REGULATORY_COMPLIANCE_FED_DATA_URL",
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


def _normalize_live_remediation(row):
    """Project a Dynamics task onto the remediation-action shape this
    agent uses. THIS is the contract your replacement data source must
    meet — a dict with these keys. None means 'not available from CRM
    alone' and the renderers label it as an enrichment seam. In this
    template a Dynamics task is reinterpreted as a POA&M-style
    remediation action."""
    state = row.get("statecode")
    return {
        "action": row.get("subject", "untitled"),
        "gap": row.get("regardingobjectidname", ""),
        "control": None,   # enrichment seam — wire your GRC platform
        "owner": row.get("owneridname", ""),
        "target": str(row.get("scheduledend", ""))[:10],
        "status": {0: "in_progress", 1: "complete", 2: "canceled"}.get(state, "unknown"),
        "pct": 100 if state == 1 else int(row.get("percentcomplete") or 0),
        "_live": True,
    }


def _live_remediations():
    """Live tenant remediation actions; [] when offline."""
    return [_normalize_live_remediation(t) for t in _fetch_collection("tasks")]


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

FEDERAL_REGULATIONS = {
    "FISMA": {
        "full_name": "Federal Information Security Modernization Act",
        "authority": "44 U.S.C. 3551-3558",
        "oversight_body": "OMB / DHS CISA",
        "control_framework": "NIST SP 800-53 Rev 5",
        "reporting_cadence": "annual",
        "agency_score": 82.5,
        "control_families_assessed": 20,
        "controls_implemented": 847,
        "controls_total": 1007,
    },
    "FedRAMP": {
        "full_name": "Federal Risk and Authorization Management Program",
        "authority": "OMB Circular A-130",
        "oversight_body": "FedRAMP PMO / GSA",
        "control_framework": "NIST SP 800-53 (FedRAMP Baseline)",
        "reporting_cadence": "continuous",
        "agency_score": 78.0,
        "control_families_assessed": 18,
        "controls_implemented": 312,
        "controls_total": 421,
    },
    "PRIVACT": {
        "full_name": "Privacy Act of 1974",
        "authority": "5 U.S.C. 552a",
        "oversight_body": "OMB / Senior Agency Official for Privacy",
        "control_framework": "NIST SP 800-122 / OMB M-17-12",
        "reporting_cadence": "annual",
        "agency_score": 91.0,
        "control_families_assessed": 8,
        "controls_implemented": 124,
        "controls_total": 131,
    },
    "Section508": {
        "full_name": "Section 508 Accessibility",
        "authority": "29 U.S.C. 794d",
        "oversight_body": "GSA / Agency CIO",
        "control_framework": "WCAG 2.1 / Revised 508 Standards",
        "reporting_cadence": "semi-annual",
        "agency_score": 65.0,
        "control_families_assessed": 5,
        "controls_implemented": 38,
        "controls_total": 62,
    },
}

COMPLIANCE_GAPS = [
    {"id": "GAP-001", "regulation": "FISMA", "family": "AC - Access Control", "control": "AC-2(7)", "description": "Privileged account reviews not performed within 90-day window", "severity": "high", "systems_affected": 12, "remediation_effort": "medium"},
    {"id": "GAP-002", "regulation": "FISMA", "family": "SI - System Integrity", "control": "SI-4", "description": "Continuous monitoring not covering all FISMA systems", "severity": "high", "systems_affected": 8, "remediation_effort": "high"},
    {"id": "GAP-003", "regulation": "FedRAMP", "family": "RA - Risk Assessment", "control": "RA-5", "description": "Vulnerability scanning frequency below FedRAMP requirements for 3 CSPs", "severity": "moderate", "systems_affected": 3, "remediation_effort": "low"},
    {"id": "GAP-004", "regulation": "FedRAMP", "family": "CM - Configuration Mgmt", "control": "CM-6", "description": "Configuration baselines not documented for 2 cloud environments", "severity": "moderate", "systems_affected": 2, "remediation_effort": "medium"},
    {"id": "GAP-005", "regulation": "Section508", "family": "Web Content", "control": "1.4.3", "description": "Color contrast ratios below 4.5:1 on 14 public web pages", "severity": "moderate", "systems_affected": 14, "remediation_effort": "low"},
    {"id": "GAP-006", "regulation": "Section508", "family": "Documents", "control": "1.3.1", "description": "PDF documents lacking proper heading structure and alt text", "severity": "low", "systems_affected": 47, "remediation_effort": "medium"},
    {"id": "GAP-007", "regulation": "PRIVACT", "family": "PII Management", "control": "AR-4", "description": "Privacy impact assessment overdue for 1 system of records", "severity": "low", "systems_affected": 1, "remediation_effort": "low"},
]

AUDIT_FINDINGS = {
    "FY24-OIG-01": {"source": "OIG Annual FISMA Audit", "finding": "Weakness in identity and access management", "severity": "significant", "status": "open", "due_date": "2025-06-30"},
    "FY24-OIG-02": {"source": "OIG Annual FISMA Audit", "finding": "Incomplete POA&M remediation tracking", "severity": "moderate", "status": "in_progress", "due_date": "2025-04-30"},
    "FY24-OIG-03": {"source": "OIG Annual FISMA Audit", "finding": "Configuration management documentation gaps", "severity": "moderate", "status": "closed", "due_date": "2025-03-31"},
    "FY24-GAO-01": {"source": "GAO IT Management Review", "finding": "IT spending transparency improvements needed", "severity": "moderate", "status": "open", "due_date": "2025-09-30"},
}

REMEDIATION_ACTIONS = [
    {"gap": "GAP-001", "action": "Implement automated privileged access reviews via PAM tool", "owner": "IAM Team", "start": "2025-03-01", "target": "2025-06-30", "status": "in_progress", "pct": 35},
    {"gap": "GAP-002", "action": "Extend CDM dashboard coverage to remaining 8 systems", "owner": "SOC", "start": "2025-02-15", "target": "2025-08-31", "status": "in_progress", "pct": 20},
    {"gap": "GAP-003", "action": "Update scanning schedules in Tenable for FedRAMP CSPs", "owner": "Vulnerability Mgmt", "start": "2025-03-15", "target": "2025-04-30", "status": "planned", "pct": 0},
    {"gap": "GAP-004", "action": "Document configuration baselines using CIS benchmarks", "owner": "Cloud Ops", "start": "2025-04-01", "target": "2025-06-30", "status": "planned", "pct": 0},
    {"gap": "GAP-005", "action": "Remediate contrast issues across public website", "owner": "Web Team", "start": "2025-03-01", "target": "2025-05-31", "status": "in_progress", "pct": 50},
    {"gap": "GAP-006", "action": "Batch remediate PDF accessibility with automated tooling", "owner": "Content Team", "start": "2025-04-15", "target": "2025-07-31", "status": "planned", "pct": 0},
    {"gap": "GAP-007", "action": "Complete PIA for overdue system of records", "owner": "Privacy Office", "start": "2025-03-01", "target": "2025-04-15", "status": "in_progress", "pct": 70},
]


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _overall_compliance_score():
    """Compute weighted overall compliance score."""
    weights = {"FISMA": 0.40, "FedRAMP": 0.25, "PRIVACT": 0.20, "Section508": 0.15}
    score = sum(FEDERAL_REGULATIONS[reg]["agency_score"] * w for reg, w in weights.items())
    return round(score, 1)


def _gap_summary():
    """Summarize gaps by severity."""
    summary = {"high": 0, "moderate": 0, "low": 0}
    for gap in COMPLIANCE_GAPS:
        summary[gap["severity"]] += 1
    return summary


def _remediation_progress():
    """Calculate overall remediation progress."""
    if not REMEDIATION_ACTIONS:
        return 0.0
    total_pct = sum(a["pct"] for a in REMEDIATION_ACTIONS)
    return round(total_pct / len(REMEDIATION_ACTIONS), 1)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class RegulatoryComplianceFedAgent(BasicAgent):
    """Federal regulatory compliance agent."""

    def __init__(self):
        self.name = "RegulatoryComplianceFedAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Regulatory Compliance (Federal) Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "compliance_dashboard",
                            "gap_analysis",
                            "remediation_plan",
                            "audit_readiness",
                        ],
                    },
                    "regulation": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "compliance_dashboard")
        dispatch = {
            "compliance_dashboard": self._compliance_dashboard,
            "gap_analysis": self._gap_analysis,
            "remediation_plan": self._remediation_plan,
            "audit_readiness": self._audit_readiness,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        return handler(**kwargs)

    def _compliance_dashboard(self, **kwargs) -> str:
        overall = _overall_compliance_score()
        gap_sum = _gap_summary()
        lines = ["# Federal Compliance Dashboard\n"]
        lines.append(f"**Overall Compliance Score:** {overall}%\n")
        lines.append("## Regulatory Framework Scores\n")
        lines.append("| Regulation | Score | Controls Implemented | Total Controls | Coverage |")
        lines.append("|---|---|---|---|---|")
        for reg_id, reg in FEDERAL_REGULATIONS.items():
            coverage = round((reg["controls_implemented"] / reg["controls_total"]) * 100, 1) if reg["controls_total"] else 0
            lines.append(
                f"| {reg_id} ({reg['full_name']}) | {reg['agency_score']}% "
                f"| {reg['controls_implemented']} | {reg['controls_total']} | {coverage}% |"
            )
        lines.append(f"\n## Gap Summary\n")
        lines.append(f"- **High:** {gap_sum['high']}")
        lines.append(f"- **Moderate:** {gap_sum['moderate']}")
        lines.append(f"- **Low:** {gap_sum['low']}")
        lines.append(f"- **Total:** {sum(gap_sum.values())}")
        return "\n".join(lines)

    def _gap_analysis(self, **kwargs) -> str:
        regulation = kwargs.get("regulation")
        gaps = COMPLIANCE_GAPS
        if regulation:
            gaps = [g for g in gaps if g["regulation"] == regulation]
        lines = ["# Compliance Gap Analysis\n"]
        if regulation:
            lines[0] = f"# Compliance Gap Analysis — {regulation}\n"
        lines.append("| Gap ID | Regulation | Family | Control | Severity | Systems | Effort |")
        lines.append("|---|---|---|---|---|---|---|")
        for g in gaps:
            lines.append(
                f"| {g['id']} | {g['regulation']} | {g['family']} | {g['control']} "
                f"| {g['severity'].upper()} | {g['systems_affected']} | {g['remediation_effort'].title()} |"
            )
        lines.append("\n## Gap Details\n")
        for g in gaps:
            lines.append(f"### {g['id']}: {g['control']} ({g['regulation']})\n")
            lines.append(f"- **Description:** {g['description']}")
            lines.append(f"- **Severity:** {g['severity'].upper()}")
            lines.append(f"- **Systems Affected:** {g['systems_affected']}")
            lines.append(f"- **Remediation Effort:** {g['remediation_effort'].title()}\n")
        return "\n".join(lines)

    def _remediation_plan(self, **kwargs) -> str:
        live = _live_remediations()
        if live:
            active = [a for a in live if a["status"] == "in_progress"]
            overall = round(sum(a["pct"] for a in live) / len(live), 1)
            shown = sorted(live, key=lambda a: (a["status"] != "in_progress", a["target"]))[:15]
            lines = ["# Remediation Plan (live tenant data)\n"]
            lines.append(f"**Actions on record:** {len(live)} | **In progress:** {len(active)} "
                         f"| **Overall Progress:** {overall}% (real percent-complete math)\n")
            lines.append("| Action | Gap | Control | Owner | Target | Status | Progress |")
            lines.append("|---|---|---|---|---|---|---|")
            for a in shown:
                lines.append(
                    f"| {a['action']} | {a['gap']} | n/a — enrichment seam | {a['owner']} "
                    f"| {a['target']} | {a['status'].replace('_', ' ').title()} | {a['pct']}% |"
                )
            if len(live) > len(shown):
                lines.append(f"| ... and {len(live) - len(shown)} more | | | | | | |")
            lines.append("\n_Source: live Static Dynamics 365 tenant (tasks). A task is "
                         "reinterpreted as a POA&M-style remediation action; control "
                         "mappings are an enrichment seam — wire your GRC platform._")
            return "\n".join(lines)

        progress = _remediation_progress()
        lines = ["# Remediation Plan (embedded demo data — offline)\n"]
        lines.append(f"**Overall Progress:** {progress}%\n")
        lines.append("| Gap | Action | Owner | Target | Status | Progress |")
        lines.append("|---|---|---|---|---|---|")
        for a in REMEDIATION_ACTIONS:
            lines.append(
                f"| {a['gap']} | {a['action']} | {a['owner']} "
                f"| {a['target']} | {a['status'].replace('_', ' ').title()} | {a['pct']}% |"
            )
        in_progress = [a for a in REMEDIATION_ACTIONS if a["status"] == "in_progress"]
        if in_progress:
            lines.append("\n## Active Remediations\n")
            for a in in_progress:
                lines.append(f"- **{a['gap']}:** {a['action']} — {a['pct']}% complete (target: {a['target']})")
        return "\n".join(lines)

    def _audit_readiness(self, **kwargs) -> str:
        lines = ["# Audit Readiness Assessment\n"]
        lines.append("## OIG / GAO Findings Status\n")
        lines.append("| Finding ID | Source | Finding | Severity | Status | Due Date |")
        lines.append("|---|---|---|---|---|---|")
        for fid, f in AUDIT_FINDINGS.items():
            lines.append(
                f"| {fid} | {f['source']} | {f['finding']} "
                f"| {f['severity'].title()} | {f['status'].replace('_', ' ').title()} | {f['due_date']} |"
            )
        open_findings = sum(1 for f in AUDIT_FINDINGS.values() if f["status"] != "closed")
        lines.append(f"\n**Open Findings:** {open_findings}/{len(AUDIT_FINDINGS)}")
        lines.append("\n## Readiness Checklist\n")
        checklist = [
            "System Security Plans (SSP) current for all FISMA systems",
            "POA&M items updated with milestones and completion dates",
            "Continuous monitoring data feeds operational",
            "Annual security assessments completed",
            "Incident response plan tested within last 12 months",
            "Privacy impact assessments current",
            "Authority to Operate (ATO) documentation available",
            "Supply chain risk management plan documented",
        ]
        for item in checklist:
            lines.append(f"- [ ] {item}")
        overall = _overall_compliance_score()
        lines.append(f"\n**Agency Compliance Posture:** {overall}%")
        readiness = "High" if overall >= 85 else "Moderate" if overall >= 70 else "Low"
        lines.append(f"**Audit Readiness Level:** {readiness}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = RegulatoryComplianceFedAgent()
    print("=" * 60)
    print("LIVE TENANT REMEDIATIONS (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="remediation_plan"))
    print()
    print("=" * 60)
    print("EMBEDDED DEMO FRAMEWORKS (works offline)")
    print(agent.perform(operation="compliance_dashboard"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="gap_analysis", regulation="FISMA"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="audit_readiness"))
