"""
Financial Services Regulatory Compliance Agent — Financial Services Stack

Manages compliance dashboards, regulation tracking, remediation planning,
and examination preparation for financial institution compliance teams.

Version 1.1.0 adds six real-time trade compliance capabilities modeled on the
Regulatory Compliance Monitoring spec (MiFID II surveillance, reporting issue
triage, batch remediation, execution-quality analysis with venue ranking,
certification tracking, and a shareable compliance summary). Each capability
embeds its curated response, knowledge notes, exactly three synthetic records,
an exact-key lookup, no-input summaries, and — for write-capable operations —
simulated write receipts that never mutate the in-memory data.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/fs_regulatory_compliance",
    "version": "1.1.0",
    "display_name": "FS Regulatory Compliance Agent",
    "description": "Financial services regulatory compliance with SOX, Dodd-Frank, BSA tracking, remediation planning, and examiner preparation.",
    "author": "AIBAST",
    "tags": ["compliance", "SOX", "Dodd-Frank", "BSA", "AML", "regulatory", "financial-services", "MiFID-II", "trade-surveillance", "best-execution", "venue-ranking"],
    "category": "financial_services",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# ---------------------------------------------------------------------------
# Synthetic domain data
# ---------------------------------------------------------------------------

REGULATIONS = {
    "SOX": {
        "full_name": "Sarbanes-Oxley Act",
        "sections": {"302": "CEO/CFO Certification", "404": "Internal Controls Assessment", "409": "Real-Time Disclosure"},
        "regulator": "SEC",
        "compliance_score": 92.0,
        "last_assessment": "2025-01-31",
        "next_assessment": "2025-07-31",
    },
    "Dodd-Frank": {
        "full_name": "Dodd-Frank Wall Street Reform Act",
        "sections": {"Volcker": "Proprietary Trading Restrictions", "Title VII": "Derivatives Regulation", "Title X": "Consumer Protection"},
        "regulator": "Fed / OCC / CFPB",
        "compliance_score": 87.5,
        "last_assessment": "2024-12-15",
        "next_assessment": "2025-06-15",
    },
    "BSA-AML": {
        "full_name": "Bank Secrecy Act / Anti-Money Laundering",
        "sections": {"CDD": "Customer Due Diligence", "SAR": "Suspicious Activity Reporting", "CTR": "Currency Transaction Reporting"},
        "regulator": "FinCEN / OCC",
        "compliance_score": 84.0,
        "last_assessment": "2025-02-28",
        "next_assessment": "2025-08-31",
    },
    "GLBA": {
        "full_name": "Gramm-Leach-Bliley Act",
        "sections": {"Privacy": "Financial Privacy Rule", "Safeguards": "Safeguards Rule", "Pretexting": "Pretexting Protection"},
        "regulator": "FTC / Fed",
        "compliance_score": 95.0,
        "last_assessment": "2025-01-15",
        "next_assessment": "2026-01-15",
    },
    "FCRA": {
        "full_name": "Fair Credit Reporting Act",
        "sections": {"Accuracy": "Information Accuracy", "Disputes": "Consumer Dispute Resolution", "Furnishing": "Data Furnisher Requirements"},
        "regulator": "CFPB",
        "compliance_score": 89.0,
        "last_assessment": "2024-11-30",
        "next_assessment": "2025-05-31",
    },
}

EXAMINATION_FINDINGS = [
    {"id": "EF-2024-01", "regulation": "BSA-AML", "finding": "SAR filing timeliness below 90% threshold", "severity": "moderate", "status": "remediation_in_progress", "due": "2025-06-30", "owner": "BSA Officer"},
    {"id": "EF-2024-02", "regulation": "BSA-AML", "finding": "CDD refresh cycle exceeding 24-month requirement for high-risk customers", "severity": "significant", "status": "open", "due": "2025-04-30", "owner": "BSA Officer"},
    {"id": "EF-2024-03", "regulation": "SOX", "finding": "Access control review documentation incomplete for 2 IT systems", "severity": "moderate", "status": "remediation_in_progress", "due": "2025-05-31", "owner": "IT Audit Manager"},
    {"id": "EF-2024-04", "regulation": "Dodd-Frank", "finding": "Consumer complaint response time exceeded 15-day requirement in 8% of cases", "severity": "low", "status": "closed", "due": "2025-03-31", "owner": "Consumer Compliance"},
    {"id": "EF-2024-05", "regulation": "FCRA", "finding": "Dispute resolution letters missing required disclosures in 3 cases", "severity": "low", "status": "closed", "due": "2025-02-28", "owner": "Operations Manager"},
]

REMEDIATION_PLANS = [
    {"finding": "EF-2024-01", "action": "Implement automated SAR filing workflow with deadline alerts", "milestone": "2025-05-15", "pct": 60, "owner": "BSA Officer"},
    {"finding": "EF-2024-02", "action": "Accelerate CDD refresh for 142 high-risk customers", "milestone": "2025-04-15", "pct": 35, "owner": "BSA Officer"},
    {"finding": "EF-2024-03", "action": "Complete access review documentation for Oracle EBS and Salesforce", "milestone": "2025-04-30", "pct": 70, "owner": "IT Audit Manager"},
]

UPCOMING_EXAMINATIONS = [
    {"examiner": "OCC", "type": "Safety & Soundness", "scheduled": "2025-05-12", "duration_weeks": 3, "lead_examiner": "Regional Examiner — District 4"},
    {"examiner": "FinCEN", "type": "BSA/AML Targeted Review", "scheduled": "2025-07-01", "duration_weeks": 2, "lead_examiner": "FinCEN Enforcement Division"},
    {"examiner": "CFPB", "type": "Consumer Compliance", "scheduled": "2025-09-15", "duration_weeks": 2, "lead_examiner": "CFPB Supervision — Region III"},
]


# ---------------------------------------------------------------------------
# Real-time trade compliance capabilities (Regulatory Compliance Monitoring spec)
#
# Each entry embeds the curated response, knowledge notes, exactly three
# synthetic records, the exact-lookup key field, and write/generative metadata.
# ---------------------------------------------------------------------------

SPEC_OPERATIONS = {
    "trade_surveillance": {
        "name": "Trade Surveillance Review",
        "description": "Analyzes executed trades in real time, highlights overall compliance performance, and surfaces the items that need immediate attention.",
        "source_system": "Microsoft Dataverse",
        "write": False,
        "generative": False,
        "exact_key_required": True,
        "key_field": "trade_id",
        "triggers": [
            "Review our trading activity for compliance",
            "Scan all executed trades for reporting accuracy",
            "Which trades need immediate attention?",
        ],
        "knowledge": [
            "The agent analyzes all 12,000 trades and surfaces the 24 items that need immediate attention (demo 00:00:57-00:01:06).",
            "Trades are scanned against MiFID II rules automatically to detect errors and issues before they become violations (one-pager, Slide 1).",
            "The manager gets a targeted view of only the most relevant insights instead of scanning dashboards (demo 00:01:07-00:01:14).",
        ],
        "response": "Here is the compliance surveillance view for the requested trades.",
        "records": [
            {"trade_id": "TRD-10432", "instrument": "EU Govt Bond", "desk": "Rates Desk", "compliance_status": "Reportable breach", "flagged_items": 3},
            {"trade_id": "TRD-10588", "instrument": "Equity Swap", "desk": "Equities Desk", "compliance_status": "Pass", "flagged_items": 0},
            {"trade_id": "TRD-10743", "instrument": "FX Forward", "desk": "FX Desk", "compliance_status": "Needs review", "flagged_items": 1},
        ],
    },
    "reporting_issue": {
        "name": "Reporting Issue Triage",
        "description": "Categorizes each reporting issue, identifies which fields can be auto-corrected, and flags the trades needing manual review with impact and effort.",
        "source_system": "Microsoft Dataverse",
        "write": False,
        "generative": False,
        "exact_key_required": True,
        "key_field": "issue_id",
        "triggers": [
            "Show reporting issues and suggested fixes",
            "Which fields can be auto-corrected?",
            "Which trades need manual review?",
        ],
        "knowledge": [
            "The agent categorizes each issue, identifies which fields can be auto-corrected, and flags the few trades needing manual review (demo 00:01:20-00:01:30).",
            "The manager receives clarity on both impact and effort required to move forward (demo 00:01:30-00:01:32).",
            "Reporting errors, venue mismatches, and other issues previously required time-consuming investigation (one-pager, Slide 1).",
        ],
        "response": "Here is the triaged reporting issue with its category, suggested fix, and effort.",
        "records": [
            {"issue_id": "RPT-2207", "field_name": "Execution venue", "category": "Auto-correctable", "remediation": "Auto-correct venue code", "effort": "Low"},
            {"issue_id": "RPT-2311", "field_name": "Trade timestamp", "category": "Auto-correctable", "remediation": "Normalize timestamp", "effort": "Low"},
            {"issue_id": "RPT-2450", "field_name": "Counterparty LEI", "category": "Manual review", "remediation": "Confirm LEI with desk", "effort": "High"},
        ],
    },
    "batch_remediation": {
        "name": "Batch Remediation",
        "description": "Amends eligible trades, submits updates to the regulatory portal, and outlines missing documentation for the impacted strategy in one automated sequence.",
        "source_system": "Microsoft Dataverse",
        "write": True,
        "generative": False,
        "exact_key_required": True,
        "key_field": "batch_id",
        "triggers": [
            "Execute the batch fix and show documentation gaps",
            "Amend eligible trades and submit updates",
            "Automate corrections and submissions to the regulatory portal",
        ],
        "knowledge": [
            "The agent amends eligible trades, submits updates, and outlines missing documentation for the impacted strategy within the same streamlined workflow (demo 00:01:42-00:01:52).",
            "Corrections and submissions to the regulatory portal are automated (one-pager, Slide 1).",
            "Strategy documentation was inconsistent, risking non-compliance, so documentation gaps are flagged (one-pager, Slide 1).",
        ],
        "response": "The batch fix has been executed; here are the amended trades, submission status, and documentation gaps.",
        "records": [
            {"batch_id": "FIX-0091", "strategy": "Momentum Alpha", "trades_amended": 18, "submission_status": "Submitted", "doc_gap": "Missing algo sign-off"},
            {"batch_id": "FIX-0092", "strategy": "Mean Reversion", "trades_amended": 4, "submission_status": "Queued", "doc_gap": "None"},
            {"batch_id": "FIX-0093", "strategy": "Cross-Venue Arb", "trades_amended": 2, "submission_status": "Submitted", "doc_gap": "Outdated risk memo"},
        ],
    },
    "execution_analysis": {
        "name": "Execution Quality Analysis",
        "description": "Delivers execution quality insights and venue performance rankings, and auto-generates a report ready for client distribution.",
        "source_system": "Microsoft Dataverse",
        "write": False,
        "generative": True,
        "exact_key_required": True,
        "key_field": "analysis_id",
        "triggers": [
            "Run an execution analysis",
            "Show venue performance rankings",
            "Generate an execution quality report",
        ],
        "knowledge": [
            "The agent delivers execution quality insights, venue performance rankings, and an auto-generated report ready for client distribution (demo 00:02:01-00:02:11).",
            "The report helps leadership easily validate performance (demo 00:02:11-00:02:12).",
            "Trades are scanned for best-execution performance (one-pager, Slide 1).",
        ],
        "response": "Here is the execution quality analysis with venue ranking and an auto-generated report for client distribution.",
        "records": [
            {"analysis_id": "EXA-5501", "venue": "Xetra", "execution_score": 96, "ranking": "Top venue", "report_status": "Report generated"},
            {"analysis_id": "EXA-5502", "venue": "Euronext", "execution_score": 88, "ranking": "Second", "report_status": "Report generated"},
            {"analysis_id": "EXA-5503", "venue": "Turquoise", "execution_score": 72, "ranking": "Underperformer", "report_status": "Report generated"},
        ],
    },
    "certification_tracking": {
        "name": "Certification and Training Tracking",
        "description": "Surfaces upcoming certification expirations, schedules required sessions, and enrolls traders to maintain audit readiness.",
        "source_system": "Microsoft Dataverse",
        "write": True,
        "generative": False,
        "exact_key_required": True,
        "key_field": "cert_id",
        "triggers": [
            "Check trader certifications and training gaps",
            "Which certifications are expiring soon?",
            "Enroll traders in required training",
        ],
        "knowledge": [
            "The agent surfaces upcoming expirations, schedules required sessions, and provides a training dashboard for team visibility (demo 00:02:17-00:02:25).",
            "Certification expirations are identified and traders are enrolled (one-pager, Slide 1).",
            "Certification readiness is maintained across the desk with automated scheduling and alerts (one-pager, Slide 1).",
        ],
        "response": "Here are the trader certification statuses, upcoming expirations, and scheduled training actions.",
        "records": [
            {"cert_id": "CERT-3120", "trader": "Priya Nolan", "certification": "MiFID II Best Execution", "expires_on": "2026-09-30", "action": "Enroll in refresher"},
            {"cert_id": "CERT-3121", "trader": "Marco Field", "certification": "Market Abuse Regulation", "expires_on": "2026-11-15", "action": "Schedule session"},
            {"cert_id": "CERT-3122", "trader": "Dana Ruiz", "certification": "Algo Trading Governance", "expires_on": "2027-01-20", "action": "Up to date"},
        ],
    },
    "compliance_summary": {
        "name": "Compliance Summary",
        "description": "Creates a clean, shareable summary capturing fixes completed, risks resolved, and next steps for collaboration through Microsoft Teams.",
        "source_system": "Microsoft Dataverse",
        "write": False,
        "generative": True,
        "exact_key_required": True,
        "key_field": "summary_id",
        "triggers": [
            "Create a shareable compliance summary",
            "Close out the compliance workflow",
            "Summarize fixes completed and risks resolved",
        ],
        "knowledge": [
            "The agent creates a clean, shareable summary capturing fixes completed, risks resolved, and next steps (demo 00:02:27-00:02:35).",
            "Collaboration is supported through Microsoft Teams (demo 00:00:37-00:00:38; featured tools).",
            "The manager is already seeing progress and has a clear path to resolution (demo 00:01:52-00:01:56).",
        ],
        "response": "Here is the shareable compliance summary with fixes completed, risks resolved, and next steps.",
        "records": [
            {"summary_id": "SUM-7788", "period": "Q3 review", "fixes_completed": 22, "risks_resolved": 19, "next_step": "Distribute to leadership"},
            {"summary_id": "SUM-7789", "period": "Ad hoc audit", "fixes_completed": 5, "risks_resolved": 5, "next_step": "Archive record"},
            {"summary_id": "SUM-7790", "period": "Monthly close", "fixes_completed": 12, "risks_resolved": 10, "next_step": "Escalate documentation gap"},
        ],
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _overall_compliance():
    """Weighted overall compliance score."""
    weights = {"SOX": 0.25, "Dodd-Frank": 0.20, "BSA-AML": 0.25, "GLBA": 0.15, "FCRA": 0.15}
    score = sum(REGULATIONS[r]["compliance_score"] * w for r, w in weights.items())
    return round(score, 1)


def _open_findings_count():
    """Count open findings."""
    return sum(1 for f in EXAMINATION_FINDINGS if f["status"] not in ("closed",))


def _humanize(field):
    """Turn a snake_case field name into a Title Case label."""
    return field.replace("_", " ").title()


def _render_record(record):
    """Render a single record as a bullet list of its fields."""
    return "\n".join(f"- **{_humanize(k)}:** {v}" for k, v in record.items())


def _normalized_lookup_tokens(value):
    """Normalize whitespace-delimited tokens without permitting embedded IDs."""
    normalized = []
    for token in str(value or "").casefold().split():
        cleaned = "".join(char for char in token if char.isalnum())
        if cleaned:
            normalized.append(cleaned)
    return normalized


def _contains_normalized_key(user_input, key):
    """Return True only when the complete normalized key is a token sequence."""
    query = _normalized_lookup_tokens(user_input)
    expected = _normalized_lookup_tokens(key)
    width = len(expected)
    return bool(width) and any(
        query[index:index + width] == expected
        for index in range(len(query) - width + 1)
    )


def _match_records(spec, user_input):
    """Return the uniquely matched record for a complete normalized key."""
    key_field = spec["key_field"]
    matches = [
        record for record in spec["records"]
        if _contains_normalized_key(user_input, record[key_field])
    ]
    return matches if len(matches) == 1 else []


def _spec_metadata_block(spec):
    """Render the source/behavior metadata for a capability."""
    return "\n".join([
        "## Capability Metadata\n",
        f"- **Source System:** {spec['source_system']}",
        f"- **Key Field:** `{spec['key_field']}`",
        f"- **Exact Key Required:** {spec['exact_key_required']}",
        f"- **Write:** {spec['write']}",
        f"- **Generative:** {spec['generative']}",
    ])


def _run_spec_operation(op_key, spec, **kwargs):
    """
    Data-driven handler for the six real-time compliance capabilities.

    Behavior:
      * No `user_input`  -> no-input summary listing all three records.
      * With `user_input`-> exact-key lookup (exact_key_required); only records
        whose key string is present in the input are returned.
      * Write-capable ops append a *simulated* write receipt and never mutate
        the embedded records.
    """
    user_input = kwargs.get("user_input")
    lines = [f"# {spec['name']}\n"]
    lines.append(f"_{spec['description']}_\n")
    lines.append(f"> {spec['response']}\n")

    if user_input:
        matches = _match_records(spec, user_input)
        if matches:
            lines.append(f"## Exact Lookup ({len(matches)} match)\n")
            for record in matches:
                lines.append(_render_record(record))
                lines.append("")
        else:
            lines.append("## Exact Lookup\n")
            lines.append(
                f"No record matched an exact normalized `{spec['key_field']}` "
                "in your request.\n"
            )
    else:
        matches = spec["records"]
        lines.append(f"## Summary — {len(matches)} records\n")
        headers = list(matches[0].keys())
        lines.append("| " + " | ".join(_humanize(h) for h in headers) + " |")
        lines.append("|" + "|".join(["---"] * len(headers)) + "|")
        for record in matches:
            lines.append("| " + " | ".join(str(record[h]) for h in headers) + " |")
        lines.append("")

    if spec["write"] and (not user_input or matches):
        lines.append("## Simulated Write Receipt\n")
        affected = matches if user_input else spec["records"]
        keys = ", ".join(str(r[spec["key_field"]]) for r in affected) or "none"
        lines.append(
            f"- **Action:** Simulated write to {spec['source_system']} for {keys}."
        )
        lines.append(
            "- **Result:** Receipt generated for demo purposes only — "
            "no records were mutated (read-only simulation)."
        )
        lines.append("")

    lines.append(_spec_metadata_block(spec))
    lines.append("\n## Knowledge\n")
    for note in spec["knowledge"]:
        lines.append(f"- {note}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class FSRegulatoryComplianceAgent(BasicAgent):
    """Financial services regulatory compliance agent."""

    def __init__(self):
        self.name = "FSRegulatoryComplianceAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "FS Regulatory Compliance Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "compliance_dashboard",
                            "regulation_tracker",
                            "remediation_plan",
                            "examiner_prep",
                            "trade_surveillance",
                            "reporting_issue",
                            "batch_remediation",
                            "execution_analysis",
                            "certification_tracking",
                            "compliance_summary",
                        ],
                    },
                    "regulation": {"type": "string"},
                    "user_input": {
                        "type": "string",
                        "description": "Optional. Exact key (e.g. TRD-10432, EXA-5503) for the real-time compliance capabilities; omit for a full summary.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "compliance_dashboard")
        dispatch = {
            "compliance_dashboard": self._compliance_dashboard,
            "regulation_tracker": self._regulation_tracker,
            "remediation_plan": self._remediation_plan,
            "examiner_prep": self._examiner_prep,
        }
        handler = dispatch.get(operation)
        if handler:
            return handler(**kwargs)
        spec = SPEC_OPERATIONS.get(operation)
        if spec:
            return _run_spec_operation(operation, spec, **kwargs)
        return f"**Error:** Unknown operation `{operation}`."

    def _compliance_dashboard(self, **kwargs) -> str:
        overall = _overall_compliance()
        open_count = _open_findings_count()
        lines = ["# FS Regulatory Compliance Dashboard\n"]
        lines.append(f"**Overall Compliance Score:** {overall}%")
        lines.append(f"**Open Findings:** {open_count}\n")
        lines.append("## Regulation Scores\n")
        lines.append("| Regulation | Full Name | Regulator | Score | Last Assessed | Next Due |")
        lines.append("|---|---|---|---|---|---|")
        for reg_id, reg in REGULATIONS.items():
            lines.append(
                f"| {reg_id} | {reg['full_name']} | {reg['regulator']} "
                f"| {reg['compliance_score']}% | {reg['last_assessment']} | {reg['next_assessment']} |"
            )
        lines.append("\n## Findings Summary\n")
        by_status = {}
        for f in EXAMINATION_FINDINGS:
            by_status[f["status"]] = by_status.get(f["status"], 0) + 1
        for status, count in by_status.items():
            lines.append(f"- {status.replace('_', ' ').title()}: {count}")
        return "\n".join(lines)

    def _regulation_tracker(self, **kwargs) -> str:
        regulation = kwargs.get("regulation")
        regs = REGULATIONS
        if regulation and regulation in REGULATIONS:
            regs = {regulation: REGULATIONS[regulation]}
        lines = ["# Regulation Tracker\n"]
        for reg_id, reg in regs.items():
            lines.append(f"## {reg_id} — {reg['full_name']}\n")
            lines.append(f"- **Regulator:** {reg['regulator']}")
            lines.append(f"- **Compliance Score:** {reg['compliance_score']}%")
            lines.append(f"- **Last Assessment:** {reg['last_assessment']}")
            lines.append(f"- **Next Assessment:** {reg['next_assessment']}\n")
            lines.append("### Key Sections\n")
            for sec_id, sec_name in reg["sections"].items():
                lines.append(f"- **{sec_id}:** {sec_name}")
            findings = [f for f in EXAMINATION_FINDINGS if f["regulation"] == reg_id]
            if findings:
                lines.append(f"\n### Findings ({len(findings)})\n")
                for f in findings:
                    lines.append(f"- **{f['id']}** [{f['severity'].upper()}]: {f['finding']} — {f['status'].replace('_', ' ').title()}")
            lines.append("")
        return "\n".join(lines)

    def _remediation_plan(self, **kwargs) -> str:
        lines = ["# Remediation Plan Status\n"]
        lines.append("| Finding | Action | Owner | Milestone | Progress |")
        lines.append("|---|---|---|---|---|")
        for r in REMEDIATION_PLANS:
            lines.append(
                f"| {r['finding']} | {r['action']} | {r['owner']} "
                f"| {r['milestone']} | {r['pct']}% |"
            )
        avg_progress = sum(r["pct"] for r in REMEDIATION_PLANS) / len(REMEDIATION_PLANS) if REMEDIATION_PLANS else 0
        lines.append(f"\n**Average Progress:** {avg_progress:.0f}%")
        lines.append("\n## Open Findings Requiring Remediation\n")
        open_findings = [f for f in EXAMINATION_FINDINGS if f["status"] != "closed"]
        for f in open_findings:
            lines.append(f"- **{f['id']}** ({f['regulation']}) — {f['finding']} [Due: {f['due']}]")
        return "\n".join(lines)

    def _examiner_prep(self, **kwargs) -> str:
        lines = ["# Examination Preparation\n"]
        lines.append("## Upcoming Examinations\n")
        lines.append("| Examiner | Type | Scheduled | Duration | Lead |")
        lines.append("|---|---|---|---|---|")
        for exam in UPCOMING_EXAMINATIONS:
            lines.append(
                f"| {exam['examiner']} | {exam['type']} | {exam['scheduled']} "
                f"| {exam['duration_weeks']} weeks | {exam['lead_examiner']} |"
            )
        lines.append("\n## Pre-Examination Checklist\n")
        checklist = [
            "Board and committee minutes prepared and indexed",
            "Policies and procedures current with regulatory changes",
            "Internal audit reports available for last 3 years",
            "Compliance testing results documented",
            "Prior MRA/MRIA status updates prepared",
            "Capital adequacy and stress test results available",
            "BSA/AML independent testing report current",
            "Consumer complaint log updated",
            "IT risk assessment and SOC reports available",
            "Organizational chart and key personnel list current",
        ]
        for item in checklist:
            lines.append(f"- [ ] {item}")
        lines.append("\n## Prior Finding Status for Examiners\n")
        lines.append("| Finding | Regulation | Severity | Status | Due |")
        lines.append("|---|---|---|---|---|")
        for f in EXAMINATION_FINDINGS:
            lines.append(
                f"| {f['id']} | {f['regulation']} | {f['severity'].title()} "
                f"| {f['status'].replace('_', ' ').title()} | {f['due']} |"
            )
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = FSRegulatoryComplianceAgent()
    print(agent.perform(operation="compliance_dashboard"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="regulation_tracker", regulation="BSA-AML"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="remediation_plan"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="examiner_prep"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="trade_surveillance"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="execution_analysis", user_input="Run execution analysis EXA-5503"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="batch_remediation", user_input="Execute batch fix FIX-0091 and show documentation gaps"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="certification_tracking"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="compliance_summary", user_input="Create the shareable compliance summary SUM-7788"))
