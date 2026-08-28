---
name: "rar-aibast-agents-library-regulatory-compliance-fed"
description: "Tracks remediation from live tasks on a simulated Dynamics 365 tenant, with FISMA/FedRAMP gap analysis that works offline."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/regulatory_compliance_fed", "rar_sha256": "1a29a0ce065f24eb47b60af788a80a027314aa876ab5ea528685c2be865d10e8", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["compliance", "FISMA", "FedRAMP", "NIST", "audit", "federal", "regulatory"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/regulatory_compliance_fed`. The original RAPP
agent is preserved byte-for-byte in `regulatory_compliance_fed_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "enum": [
        "compliance_dashboard",
        "gap_analysis",
        "remediation_plan",
        "audit_readiness"
      ],
      "type": "string"
    },
    "regulation": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `regulatory_compliance_fed_agent.py` and embedded as the fenced Python below (sha256 1a29a0ce065f24eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `regulatory_compliance_fed_agent.py` first:

```bash
python3 regulatory_compliance_fed_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 regulatory_compliance_fed_agent.py   # or on stdin
python3 regulatory_compliance_fed_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
