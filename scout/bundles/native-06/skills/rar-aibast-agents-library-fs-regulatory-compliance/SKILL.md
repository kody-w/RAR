---
name: "rar-aibast-agents-library-fs-regulatory-compliance"
description: "Tracks compliance findings and remediation from a live simulated Dynamics 365 tenant (cases and tasks), with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/fs_regulatory_compliance", "rar_sha256": "3db36e36416a456a6669e40e96b14edd3b31b7eb53228aa97ba9f967ff10334b", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["compliance", "SOX", "Dodd-Frank", "BSA", "AML", "regulatory", "financial-services", "MiFID-II", "trade-surveillance", "best-execution", "venue-ranking"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/fs_regulatory_compliance`. The original RAPP
agent is preserved byte-for-byte in `regulatory_compliance_fs_agent.py` and in the RCI capsule.

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

Financial Services Regulatory Compliance Agent — a template you are meant to mutate.

Manages compliance dashboards, regulation tracking, remediation planning,
and examination preparation for financial institution compliance teams.
In this template a compliance finding is represented as a Dynamics 365
case and a remediation action as a Dynamics task — the tenant has no
native regulatory entities, so the case/task queue stands in for the
findings register and remediation tracker.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `remediation_plan` operation pulls live
     task and case records over real HTTP from the globally hosted Static
     Dynamics 365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="remediation_plan")
     and look for "Records request backlog exceeds statutory deadline"
     with its "Review service notes — CAS-260131" remediation task.
  2. No network? Everything falls back to the embedded demo layer below
     (REGULATIONS / EXAMINATION_FINDINGS / REMEDIATION_PLANS) — the agent
     never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     FS_REGULATORY_COMPLIANCE_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your GRC platform), or
     replace _fetch_collection() with your own client. The fields the
     rest of the file needs are listed in _normalize_live_remediation()
     — the regulation column stays "n/a — enrichment seam" until you
     wire your obligations register.

OPERATIONS
  compliance_dashboard | regulation_tracker | remediation_plan
  | examiner_prep | trade_surveillance | reporting_issue
  | batch_remediation | execution_analysis | certification_tracking
  | compliance_summary
  kwargs: operation (required), regulation, user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
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
        "compliance_summary"
      ],
      "type": "string"
    },
    "regulation": {
      "type": "string"
    },
    "user_input": {
      "description": "Optional. Exact key (e.g. TRD-10432, EXA-5503) for the real-time compliance capabilities; omit for a full summary.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `regulatory_compliance_fs_agent.py` and embedded as the fenced Python below (sha256 3db36e36416a456a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `regulatory_compliance_fs_agent.py` first:

```bash
python3 regulatory_compliance_fs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 regulatory_compliance_fs_agent.py   # or on stdin
python3 regulatory_compliance_fs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Financial Services Regulatory Compliance Agent — a template you are meant to mutate.

Manages compliance dashboards, regulation tracking, remediation planning,
and examination preparation for financial institution compliance teams.
In this template a compliance finding is represented as a Dynamics 365
case and a remediation action as a Dynamics task — the tenant has no
native regulatory entities, so the case/task queue stands in for the
findings register and remediation tracker.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `remediation_plan` operation pulls live
     task and case records over real HTTP from the globally hosted Static
     Dynamics 365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="remediation_plan")
     and look for "Records request backlog exceeds statutory deadline"
     with its "Review service notes — CAS-260131" remediation task.
  2. No network? Everything falls back to the embedded demo layer below
     (REGULATIONS / EXAMINATION_FINDINGS / REMEDIATION_PLANS) — the agent
     never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     FS_REGULATORY_COMPLIANCE_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your GRC platform), or
     replace _fetch_collection() with your own client. The fields the
     rest of the file needs are listed in _normalize_live_remediation()
     — the regulation column stays "n/a — enrichment seam" until you
     wire your obligations register.

OPERATIONS
  compliance_dashboard | regulation_tracker | remediation_plan
  | examiner_prep | trade_surveillance | reporting_issue
  | batch_remediation | execution_analysis | certification_tracking
  | compliance_summary
  kwargs: operation (required), regulation, user_input
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json as _json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/fs_regulatory_compliance",
    "version": "1.2.0",
    "display_name": "FS Regulatory Compliance Agent",
    "description": "Tracks compliance findings and remediation from a live simulated Dynamics 365 tenant (cases and tasks), with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["compliance", "SOX", "Dodd-Frank", "BSA", "AML", "regulatory", "financial-services", "MiFID-II", "trade-surveillance", "best-execution", "venue-ranking"],
    "category": "financial_services",
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
#   export FS_REGULATORY_COMPLIANCE_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your GRC-platform client. Downstream
# code only needs the fields produced by _normalize_live_remediation().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "FS_REGULATORY_COMPLIANCE_DATA_URL",
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
            rows = _json.loads(resp.read().decode("utf-8")).get("value", [])
    except Exception:
        rows = []
    _LIVE_CACHE[collection] = rows
    return rows


def _normalize_live_remediation(row):
    """Project a Dynamics task onto the remediation-plan shape this agent
    uses. THIS is the contract your replacement data source must meet —
    a dict with these keys. None means 'not knowable from the CRM alone'
    and the renderers label it as an enrichment seam."""
    return {
        "finding": row.get("regardingobjectidname") or "(unlinked)",
        "action": row.get("subject", "untitled task"),
        "regulation": None,  # enrichment seam — wire your obligations register
        "milestone": str(row.get("scheduledend", ""))[:10],
        "pct": int(row.get("percentcomplete") or 0),
        "owner": row.get("owneridname", ""),
        "_live": True,
    }


def _live_remediations():
    """List of live tenant remediation actions (tasks); [] when offline."""
    rows = _fetch_collection("tasks")
    return [_normalize_live_remediation(row) for row in rows if row.get("activityid")]


def _live_open_findings():
    """List of live tenant open findings (open cases); [] when offline."""
    rows = _fetch_collection("incidents")
    return [
        {
            "id": f"EF-{str(row.get('incidentid', ''))[:8]}",
            "finding": row.get("title", "untitled"),
            "customer": row.get("customeridname", ""),
            "due": str(row.get("resolveby", ""))[:10] or "n/a",
        }
        for row in rows
        if row.get("statecode") == 0
    ]


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
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
        live = _live_remediations()
        if live:
            lines = ["# Remediation Plan Status (live tenant)\n"]
            lines.append("| Finding | Action | Regulation | Owner | Milestone | Progress |")
            lines.append("|---|---|---|---|---|---|")
            for r in live:
                regulation = r["regulation"] if r["regulation"] is not None else "n/a — enrichment seam"
                lines.append(
                    f"| {r['finding']} | {r['action']} | {regulation} | {r['owner']} "
                    f"| {r['milestone']} | {r['pct']}% |"
                )
            avg_progress = sum(r["pct"] for r in live) / len(live)
            lines.append(f"\n**Average Progress:** {avg_progress:.0f}%")
            open_findings = _live_open_findings()
            if open_findings:
                lines.append("\n## Open Findings Requiring Remediation\n")
                for f in open_findings:
                    lines.append(f"- **{f['id']}** ({f['customer']}) — {f['finding']} [Due: {f['due']}]")
            lines.append(
                "\n_Source: live Static Dynamics 365 tenant — cases reinterpreted "
                "as compliance findings and tasks as remediation actions. The "
                "regulation column is an enrichment seam (wire your obligations "
                "register)._"
            )
            return "\n".join(lines)

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
        lines.append("\n_Source: embedded demo layer (offline fallback)._")
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
    print("=" * 80)
    print("EMBEDDED DEMO DASHBOARD (works offline)")
    print(agent.perform(operation="compliance_dashboard"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="regulation_tracker", regulation="BSA-AML"))
    print("\n" + "=" * 80 + "\n")
    print("LIVE TENANT REMEDIATION PLAN (tasks fetched over HTTP; falls back offline)")
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/6286bKjWLYm+CrHvH7czEt4gAQIEWXV3YxiEPMkqCiLZAYxz6C8+e61ddxjupld19qsj7m5SbD32mv81reO+fa/fwmXuejGLz99oUSasuwvP3xJ0ikey34uuxY8tscwrqaPuGv6ugzbOP3IyjYp23z6CNvkY0ybNCnD9+KPbOyaj/CjLtf0YyqbpQ7nNPlgjzZsynj6QC/4x5y2YTt//CUOp/SbgDmcqumvP3xs5VyABx9dltVlm34kadN9ZGFdR+D8H4Fa6R4CFdLpy0//83/98KUEn7/89PcvcR1O4NEX3jLT/H1iNx7Mb7pSedrOYG8dtjlY1B/A1hZ879Mx68YGPErS7OP7t79MaZ398PHv/15t4ZhPf/34+n99TPP408/tx/efDqz8Zur/+Pi26Mc8nf/y85ffXvz85YePn7/87qxfknAqoi4ck5+//PV3QUk59eEcF0DO339/+v75f9v808dbux9/+Vdvf/jPIsZvrgD6/DK/w5eOvwv453f/YvtvMf2lB6774+Y/v/mnre8ggeiNv/Rj2v++70+P/7DpH79/LEAy1OkIPPKrcz59+5tn/+C9Mvt19U9/Pn9M52Vsf335l98i+fuqqU9jcISlc8wvms6ZlC1qqvV/Oum9418f88u4tL+8X//y29bfhfzwufEP2fS7iO/bs5+//Pu/c+PYjT/9+79/OG3Vdlv7hxT7299/+/yPv/3485cv/wBZ34KEXOL3s3fS/7f/9qGU8dhNXTZ/WHG3zB9Ap7ls0p/bn1u7KKcP8GcuUnDmmo5TGdXp93X92D3TT0Gg4j7+9v+EZRRO89fwXTDT17qMxnA84Gz6NV9AWf0h9/7244cNpHZjmZdtWH+YlK7/3H5ufp8Iojyl4wqKPzrm9Csorq/vDx8lsOpfyvsFHPS5+8f++NsnLIClb71NRvyIw35a6vTHt01ekbbfLYgBWKR7Gi9AcN3FQIusBPDwA7B16moAQfPb/qkq6xqk1AiMBWd+w6yl/ekt7G9/+xswuvi5/YYL6Mc33Jvgd2B/Vefj61dgDsCkvJh/btO46D7+7e//+LeP//j4P+36FP4+Qwfw9D0CQEPJ0tQPkA5L83bzxzucaZh8RuDv//juVCAGVMoHiFeZlem3zQARqzT51cOWQH0945ePKAWeBV5t+m6cASJ/lPOPH2L28Zu+4ND3KwC0H0U3zQBT+7RN0jY+gNQQmPObJ9tu/phArk3Z8cPHMqWfp/4NJMGnis0vMVj+tw+F0T/mrqvBX281PxeBzV1bAvf/Fv9vz4GQ8d+mD/pXET9+qO8c/OjDMeyLMfx+RhZ+i0s3fvy6HQgPP9p0+7l9g3z6dtVnFXxzD1gEPBN/D+nXd8zfzakBgZ1+PftzzWfzsTuQ1QD+2ul7sofjOxRxB1Q5PvKlTN7p99+/p9RUdEudfPoPaPqW9D0KyfeofOYgD1K+jUsQTgskeRmDGP3eez5+bz4fn93n4+fljJwwYBJwQv9uiR9Ht3zq0aTvXgjMbRZg4bcEV8K3G//Ub3/D+c/c/hW9Pz7RG0T9hz/14Dcqt++nIBwg1b8B7/dXIBvC7+ACEufdx7/b8Y5QOS+fb/5wMMjNZgJaie23WvrNgPBf0IF33YMD3pXfvj0fvrPuj73/5/bd9D8LMPyTyuH3yPxpw5sW/Oq6dyC+E4cCrGq7n9u3SWv68TuYfIBTy7l81//UfU/MKYU/xQxLugBGMv+aIm/jwYqf29+YDJBTvvPknyjN9xb5GRpB8z5sQbQ+bE7R75TNfXiaKVtvYD/9+KGB/AF1/D456vZvuV2H+VSU/Rv0/tw3//YHnO+Xup4+SdP3FvGp81uRT3+9kxWE/uOdsd9ARLBt/RvX+sz1uosASzo+Kxz43XoXS/xd1L/kXtSnpfcQkCwty0D+fljHu0KnX/09HS2QPL+LLJzDHz4d/ikuHtPk7eewBm7euhHwwm+crz22Ih3Tv/7aKIt57qefYLjqkuPr9mMOuN0S/Vh28PSp3dfku15fgV5w2Jfw+yB4JX88w98l2OPx02/E7Ddn/Y9/RU5+ba1vl9VdV33G9+cv5nfHjSmIPwC/N4+suxyURJym4PlbleUzdRKAwW/O+fOX75I+uWgJcPMtZS3T7WP6VunAFXP6m58Yyvp6viAn9PTzlz9nDYjgj29ZZ4B6HcCy+e2s//uDe6MOKCVQLW9mO33q9AaAdyDTJkqTBETwk/nW4QGCFKV1t31X6i8md3Pu3wjLB/zBPShFVD+//sKLKiuqt/djk1M4Vvz2GCSpav31j1X0CbHf5bWfcBwDJC6ASd9p96fW6I8fSliBxjK/oWoEdTl/7r6LLvfBUjb1YXGU8k25N8P7VSJv/fJdR830f2E0UCUipTLcL+89vzjm/W0qyJUPjQXh/joVYQ/MBR2p78p3Yr4P+y7qM9F/y95uBCgHgvrZPtP93dPAxs/Ue+/5uJnMG/jmd7L89b3yNyngKYjaL1kK+CTgG3X9rQ385a/fYvy5+0274rp8N+7PDgPwvk6mbwjxXcz0W21/9pv2M4HeEF6Xn0UHQOWXFhwe1uUr/eVdy3+kyn/5NUP/EIk/ADlQa2nadz4e74xr4fDXhWkLOl3xboDAy2EDsuzN7uq32r9l6ph+tyICLf9T4O9w9glbv9Pc955/NT8ALvPPU8Hnw/9UamD/f3z8icuD72B9kv4yLYDvAar12RL+4zvxAIn+SzlNS/ptZ/Rm9X90zKe0N4N7nwAaX31MoIv8x0ecgr0Amf6gEBD1TcgfDJgW0PbH4/38G8n+6Q+w+pd33QPvJH/9Y9f8JDfjL2XbL59zIahpQA2+/NQCEP7hC0i39L+cJd89tEmBd6f3/Al4dP/WNv389tvx7y9pu4AJ83/+y4EOyPlnl38+/LPLv8+9v/kbfP9nf3/u+5O/wZN/cvanqP/sbPDwXzv7/eKfPP0FDN7z0b99BOaQ96p//NGOt9H/9PoP/gav//y7Be3zQ1j/+MHtgAV8VOnx8Zf0xxzUocl+PSEYev7hDXRfcRxB//pr3/4Eh6/vKeePNARMCWFU1p8c4L9/dA0Ar/f68CMDof34bsD79wj/ScNPC75lyjtYv0fwd1u76D0qvY35FWTepoAcCN9t63sWfJ+mwHIwOX2d3nwSPv2IvGMTjt/mAvDu/+Oc9X03QErA98F2NInQS4pesNMlxPBLeLlcyBRDUvISnTDQPdAIPUVEGuHo+XwNQ5KIQjIjL0SWnRAUxSIgbwJgASL6pszlW6Moi/BzHJ0yhLimJIGl+Am5pAl5ukR4lqTk9UJGKImnv28F6ZF8N/ObWW8f/jbyvd3x3dq/f4kuGFgpYJNIffthYNIlQ1d5WtE9T1CcH9W+sc5iJfpNyc49dj0Z+TDnfUeFfd8uypYYveybh3Vzh2vHeo70nJ9kkS13skJtdHmpJs1n+hS5MypeHuVVZyPd3koZf8ivocrSRfDJ7e7h8I3UIV9aIBn1UqZ2or3aSf7KZU8jv+vL3SBtsoVhEiYLoZpwXQ+sVx+Y+3j406tFMSVG/FUBvTJT2+D0usPm4kfMfvOEUopUE1c8u1fwUvHjrLAOdc1uiUAS5fZqMkgT+ycN3SDBFpgjVWCIUCmX3a3r9niUG2RfNN/OHBlmaQm2refjsuMOWFNBkXZzttN1V9j1FqN5zTUKfWZpIOxFq/49uG53jG+k62T0xbWNdFjdYsK3LtS4aQZ+FfrnNU76Fh0lIeSm1uJ80ZJ6ukKZkIof8fXqCgX7UORbBhWHUSG2Q3lZ2B0C1GQ3ZTosPjRVX7KQyFt2saOFynuRUuoc1NmjzLitFFqvEciYoowdxwkRVlhZW2JghWxsrlCrwgXBn6vTqZH9pVG1qYN6FLJzfVX7FmfgMFITzDgyMSr3IOYaxqQdgaHqXAaUAebuuUjLXI8vingoZ8DDqBmvmNLGdJp/hWr3atXYnDnxuIp1s3mS/5z1J6Pru/88O8VjkedzGNyyNWBeB1Q5i/Q41TDdtQXjVWdH7K6iuN2G3kViBDmxz4a7GssJow7hLGLjzOUawx9YHDzRdnbuVtSnVaklr2jBpua4BuyVDPSAbLqLkxBMLLgNVxq3nLXaMdtI4OI1W9FXfElvN8q4b9cAo6JOuZCDRJ/cKxioTpxJmLxhmI+EQ5TB3flIyRNcOqqAWkrmQqd+Fm+EzvmD4t0ezOq0eUFsZdFWlCE1mfR8cmt8zTxG4gAFMuLuFmLnC4w8WjtcIFQ+cJi6n0OFG9rDwkp+FR0kU9oTMOzu8KHBMI1Qi77vCLg5jDvkF7pUMQsTkMJdZzxDEk32IgqUg56GNdvlF+ufU5dvofOODnByJZQ79OyuejRhWrRipQitYNIiq5e+39Tn3tWwnS9y0Rf8szA3PNgPFu8Y3lSVfizGAvWgI4Ygbbv0Jn118sRqT/DjdT7tGHExLpdRhcc2XzY257J4fNlwTTMJ2p5mSNgl58l4YHpZ2Iy7T9rq4uT+jCmP0EXOUmcxmDHmNLXsYd2PKgMI8OSsONIbxMpvpOEgMA+Tx7bkp0OWq+AsHRF1h9Di9KS72YzDznemE8NunJafW51G9WJROoZ99pXXq5zkXMwNyl+5mFWqVFG4qbRbRrFDTuFMKdXzpRc2NijdE4h7DB2m1z1vnOigCw0fV8i8VYlX7UadHN31BvdBR3UNlomps+Zjy+od4l+fOrpHInEWKSHxGi5g+JTamB563isuM21sflkO4t7y8rjApIxxOUIJHWYJ50reot13jEvLXWRutFSWbF6GptOXMvDZFRFeTIFUHooqMMOVhI9cK+bJIggHWU9eFyo/8eerQ9OQ+pxKmlVuLK3kPHEVz6r2MPjE02jq0M0bHSGWHWYpzFnCfCVTnZ/j5tkfVierIV07ozo/8FMtyj2rn/bq4mD8qN80HYk3I1DqS6M5hPaiTlDEWOdEnQSKskaHvzNWBlOKP10GyNY3/ybdR4LEui2CXcxkcf9ZTlt6uMGolfCFnHxX7k+PUHw4SYp1kCCJkmKsFC3gAu6+WFLcb03U5dlJUSY2l+CTZIfhOWk1aSc6G+JfV6XQzrK+04sbsK9nfCGPgxn2+ZQjoSyTyai6g79m3IO4kvaVFBBaMn2toixdyNWFDG0RkVq1q2TokhO9SN05zBjXQIlVDaYMbymOAXNg4kJuMepPLQZ6Vy/cOcoUITnjwqq7J3wW8iyj3mG21mhB8sNZN5yuox26ag1GtDKLdKCK6LzEZgfRi5hnvgKfmU+BPr1eOAJt+kkHqc860Cq/grMnuzBkrZDmV011DXpCdFFIO7ErNsPLkmZXH6bvAmFntcs2vcK1OEH057h9RsoLKzBnFv051AuEps01ZAVGguPrS8hZfDNj18OqlqFVmI5abbSbWz/gpjzDwcAgyOIYOqOG8rEPbffYTNYz8t5R0kepHwRhzvxCoYu/yUXWQRxZLez5vu43q8dBQALSx6AHlCf8oXb5tdqSVYx2fdat6jY1lKRZJKFv3OoQ2ElZGFJgVP9kazo5jrnDexCSdUNPZ6K0hztxMU+OrBUmB0FgtIoUC+p0NaXQyaaMZ97dCpbWcVqRqxdbvmQM0btNtsjzeY+euAkXvnLabtZFLyyFj92oqayt3061TbizTglYVQCCsUy+uetaV9CGLO9FmL9ascOas/n0dHdYVGxV+XOoCrHEwfB95D2Kb33k6Wo6NaNYXMSnqK19/nImuF67kwSa+L5vh6+CwpPHM9YzwjE2T52ebIHsd6fByFO99i+hefSIufaqrwdLvu2RUjAkVcFkHnWUrdtFhDGv6tZVR9ChtnXfzAVbc2GYNIJHz6UxpLFws3NVZmbrQj6Cw/Fgdg3Ea5lK1YOm7tH1RVuJsdOJOktXrH5CJwnJHvux29o6VmCcj8kGfvRzrKrOSjdEFsK7uuHqgOH9A/NIbw6Zs7vvR9LCfvpKCt22rXeeD+1eYeSNwZ8FNj4Q/nYD/Vezw6MDHOcWTy1CnBsd5zGcYbgRYrhCK6CbepfWl+vQMgXexNpdEBDAOqwj8tH8WkYS7040p144nJEYJzOHOjwStcfoM8ZePbRG8+k46cRD3cT0yVeenK6mcCpPhZPv8P1BXY3xamzqNJ9VsxzxO10jz1llFUULH5reCU8+F49QNYqn5Nmk0WJaU5qFFZ47o8Bkg8ZP942gZlXpfHOja7G2urZ1HG1KmNeVNpEzu7E7+tK00FVDxtLtx6szA4uJLZpbFz0/I8LE+11lTVJqJOyNmO4diBktX0gWT7Uxhnwe0V7us+vi3ZCoSyPlQkAJjOBvwiQ6pvREkchFrNsGhW3v9NSVJagQ40iDMzcmjoXcf5o0DHd23BfjgCPdiUG4K3Fl7PlRYuIsZmRRSGaLmnCjYhUVxBpbus38UBflbvABbwTQ0eraVkHL/GSeeinQr0QSPdPnKGCyw7KvMq2OF2UrFJcbd2+1ceBPbArp4MmznUhy24rwp2cuqrEc4LJwtyfJZ00xJrnkwglc4yBP0vMh2glZSFbKaxJeUh/XwirUV2Iqt1JHubonsVXqMdMtjAxXzuOj2NuHMFjF2ttz3oWrw0FBjVPXeDxJr6kMcgPqgltdOXckZI2nrWdFDw+mtaCcVxp9P7Cvlg1Xbp6i+zhLj7gv4RDnoFTUfCbuVpcGrTi5cbzPkpxuApS091DXLfnlaTpauwEYvkQrJRe0lS+ZcWyWiE/cg8FzouB9XSs1fzEvdYs7W72q52nTmXyW9bztIE8dU5vhlDi6CpeehetDbrLz2eRfmDhR4pNBTH50Qi3KMOWB2iuMsBN+Cc5bRRK4lK0x7K4rs+SreIguq7rpudJe8Sm+BNPDuCS02biVceGZg7g6z/he2vvyWCkXOohneeI9pUwpkq2UTM6GhdV9nKjRVejxbDpz2ChKbjqfiCdxjovhbhhbpz5VVjUrkc7Y48heTIXsXrROSeWaNKNSSXEki9hiB8MY4itqu5uEb08FHTm1xs/ojYv3cTHIXZm9cmMZ4sK3Uufv2oBqRqi70XKgRMgzcDvjG5E2nWHf2Sf58EkD8ccr1VnCpUxu4qPlD5KMC0gmzVyqSoEyJ/i4n9MUAD8F0drxQMFyJL9VJmHcTMDLaLJOxaDlPe5OE8c0jneTlvhZmNxDTEhlp3i6UlpsCNyLfuW5VyqM01XvIljASQiKKBqG4FTNr2dsJU8deepnCjpv6zUC80IhbHeIriJiwAWYSoQUBx33iTUBlfmLLK83LXk6km95Fy0SBjXwkJTFcNHYpMDxtGtjGDHfxLgnXXjMNM6RtBUw4QRRrt6MkdKugLJn8zNPHv5A+au07Y7NKzh7uYdRHkIojqH3yaDVkoOSLIoflxZ5NCifRhlvtzAGxTpqux28F8QVbZ8KnN2mayhsKlRZEZaP2AXk++mAkQkK+DRQWImMtk7cDATtwsxRSTRn9oLywIjkzCFKRAWRg936HZdGc5+GU3j20wm1K41HVf05oA9Rzx7XhkYFDFDuotU9bIwJoUl3U6eDUuiFlB8vWhhZ8M0ywWidKG1P65XpcptzoVBfjsDBL8YqlSxjcEbv4tI5PEE9bD4s033iry12t0WFoYxHeu4Gld23M12np4TVW4vtjedVyow2lfCmOY2hVdoyN8CuhqKW7jD34pU7Nn2mTTWTZPFlrud1dYRSsKkmqHnKbhcmxSTfEA1tImjOb2kxFNqFPd32O40y2b4tYvn0oEK/1TBmAdeKxUVhMNg4oj0YqcL0eLM9Ix4t5IYQY4MxwfzB0gEXaXYhN7cc5MP55k8qEbdkszbohESTgR1De8eqFYq4dUOlcGe1nK/O2pTyakRA7fOx8GTcIWDMgyrKqbj+iYU6ZTXPMTZlVTkdqkQoq9zK5enx8M8O2+iS9pDCR+7elkDhOdRAq0dhlOMJHi4L76Pm+WK7XIWPYKiSjf3OrwyATkAJOj2I9isizYQlWiR2SmEo1zl1t2AcN7RxOWahwHCAYmvyOkhnOxtnxQ0BCWYwd5ZjohxcpltOTKNSm2nZrKDAVkDDJw/zmvNTr7bOJltyimMZ8rqFcOm5Kx1UuMG2HZOrUBfhUS/yIPbnagDV4OySu1JH9WSD9s54XAPRtstenIG/EUS83bfbrd2TOqCnMx058mox8jX0zs5ii5t2XHz5JtKW4b1mo5GddT4FuHfIlLDMhh7DE49SUbZSbTpJ6mSXA+1QFtPVZ2ozsvWkr0YfJY6gMtH2YEu2jym5tjwqS9ZQUiOKrSFY4CHGzzpspg7nZUpDiRcYM59ot2oezIWIxZW6wkc2+ptP1ErPB9gUU23M7dvgCYBNZ10WgyU6BTFmZyMAmliD7o+jbXfRszbjbvTU+baw4bg8rnw9X0XqkgJTzwpzFzPsphZOLZRznjETvhr0s9/228USUGMQb2WsSJAGcDgLcYyqsp2iH327ytRjWm8PitgEKj1NV2+hUxGh2YXmouDmmGMOekrbynkujYimnaZzsZD+GS6eDoX7IucNeLAKjsbhivJyGVbKO3KcZfRBYXFqEcu2UesYNDbgbQIlkf3lxLRPZi+J2nGIJNyHm5yBqWbL2FwLsDIIXNd57PbTH0WeN9WKqa51WV1mrVp9Cuqz1Uh23lqNVLkefbG1A0/C/qWFe8EgVddPpNY0R8Xd0Mej7ShEwtALETjivtyW9IwRs9/p3NqJmR8p0VXpcKboirOL35wkkS1OQDVn5PWCqviSYA4vn2DmYtAjr+jHQZnLi5jb0H/dL+5sapFe2BNj5VfF70pDlRA/L+6wAQmlKL5a+FlqVZPLVe5iO9Rx0Ri3THUjnIMUF/0RI/KrMo87zt1y0r1F/mEV9g0+XI260Rxnb61DqSeVne/moBjHSloRLN6ekjKH8RFdpGMJbY1BnMfSxFnGyzdIQeyA6c5J84jxtPKPBYWO6yZ4AZ+4AxjuTv6qoemKh2AsFm+D7GkpVuQcIGb9fOpm1YVoUkIf5xOTuV71mmbnUghX3dBRpoCD4oKc58aFE0PB7Bj3qba6xwUBn6ab5ToOwsus7+WkpNTcxAhP3KNkw9QYyn+ySrqfuEmUnVDqDoO6a9jDcA99k2dKGke0uzIXm3e3sDvzTV5fLlsGMXRGmPLmy/XLd6bgRufTAzm7g8lfFfoRXcTSTgMr3/d1S7FrfK4skbcwxmXzcx86ReWc9xFzyk3cwQiwnKjronKwL/d+OUFYy0Kr1TR4EPZEed8ko57CHnNWLRVx3Ir3wMfVm8hoQzmADwvsXtrLRo4lqrn8M4auHWSucQ/tjGRblo+Jl0lPAmMy9avbJmwMoUc5bmyUDqpfvV6VGicpw/DVwe+3sbNs2FNz+nxNTzFzY3KmUgCmEumGhXcBLiNjBeVxiWsWITumGdMVcFyj1QnZHnSMCouVAi33hEm74TvhlAXrdWGQdhuv18G659JrWFsx8l8iHJC56Mq+Ht3h20Yfd6b0soh6hXGosyAQF46YKedqb9S5Wj1PZsqW5axAjDbhTiVXxtxG3HhETsewach2MSfH21Vw0nszEzj1TIPBkCCmOFK4BZMmlb+8fYngHJhO72FtyzdAMUUHJtGHAXnKHo2Ifm5fWcQbWaV7QbC3tZvm1a3ZqGRsYtsbpbN3kl/EmLmhsETlrFQ7+9wU5M5pwW65cTBJV5iv6FehDzfXHPqzRMIPrk3vnLmEHBl2LzmPOFMR4+EMm8jVkcQDlBFkZpgul3eq8fjczo/t1igqlpt5XdBhM1Fk0V2icL+XdZ8jTXpzTvsa9o/xvkyee61bMLo/TR+Qkj6ju5PWw66H3xhKBcP0MiQyAFDZup1CKVCTElg7dE/nOV08PJjFVdW1e2Q415v8fJE824dsy+zsMpMzz4gP+9kbtGTjWUalHH8ZwfCE1kvCkHqTu5293FKWqK+xfM/jGCavxIFJaNTVBnPbLNR5Qal/Sl16v98OhAV85MiOZhhdOV/vRHIXCCoo2KU5B4NPI9s0UFeN8s/62JkGey2t7lUdYRT6FbOUF3xGOm5MzYOp787U7xfilcZexToO3NMM9YpvZxGSvRtfF30gSU356KKOC7JdYGtWGe/n5UGzt/PszAx0zzHOeSCUyz2SvJrrblm9M2lOHMkN7JH0N551ylrms146sWKvabZ0OeOSMZMPJ0sFf9BnTZuEm5HzhwH3+2Y2gSyl/DUNG/kYI/eUJhfzpFnlfp+yLLc0eaNAve1ORZoPjHiK2SqaZ4A9mvWk0pFVlb0UL1tZTDcaetir4Xq+n1cOsST4suWxlqf3YtuFphNhJruZ+NbhbRfSjuXFyS0x5gJrrUC6Xc1TiczN7h+JnulZ/rBWD7q/7iQlMg3LiJmGD1t0v4WpXqUGy7jbRWvg7YWFajnfLrSC9u19FelOp+yy8A0jSyd+3sHkPtK82iOPu2NIWb9RGUkwkCEhFShfAPzjBneioGba5rvo0x3A4IdwOD2cA1XH5XqcoifSFxd7e7hBEmiFIJnkhjei1o02X+ypauB2pGjMDHNGfPb49PQ4o4r9LD1o8gAztHlc4PTqNIOxzVpK3Ot9WJxKz3xcB7meHaqWUQSzKUkLlIv8zJ95VHgdzAvnB66hx6l5BqdpKjJhVtAksGQPvvVzWhl+c6kH9fR4vZ67fCIWRnape6CfpYvUr3h3vwSMIz/YI4hin6/DV58H5lga6Mx31aFpmkKHGkmdtNeT89pFsjFOhmNKwQaPujik4c46olaD4RfUck17FGSUqG19Vx9Zelite6GTru3IDrDiWfWaDQrOLlPCSTEJ9FlErasBX3X6wS6D/hCYuW4tFzFXBNMcUyGsOxLfOdu4U8ZT1i6W45weCq7RiNDymGeecsLZCHNB48UUTv4y5eFa5Bi0YVh+vKBgj3DGggQw6gpFGo/8KknJct8nSJBv/niIxL3eJ7lPDy+lZgKVPYBW9OnhYWfomKWWQZl9kpSXuuPC9fwwKTbH4nI6lKDi7oJi6ad7Lky+KbRUu+yDfX49hS0nMJbM4wTvzexE00gLwzcqNqfIO2kSvuuqql/QwJQ56Cn3g1PYcVnj0co/NDpLOuaZvNRbAebiyD9NTfO0SxfDBQP2q9Kimun63CsvBtVT7eJ5eCUtUjbDlindwtRqc+XvLrHAdTKQ8YmyhuFVOrEc2oWq8Von6WCcNebmXPkd8fSC5KSH8vgAuK66XDs4rHSiYo0N6DVmbHctHHKVnqfK58XbY5IqRX9ymXxxwqINu16RwKx4upxnhpTV4QnBzWicbyTqzUNRF48nPEtPfudThBf00DYK7CFHRK6mi8q87FduLxrjlVhY2rpH3m/KztuaBTjBOAR3wVWPqYj0eWuBW1NNbIO7UV/v/f6Ir0GCmBhrPg4XYwJimq2XorTCWQoPJ/E2IYh97gqmcn583uHHxcmTJ6+ApMEFlI/02ubB1GxMYVgjcVNcl4VRq3B/tIxqW2P8ilhG6BsVpA2gY4HNiKZs0vXzSrGsVmBBwaW+0t9s/86LTc9ZvYzc+6bLpUOiK5bGVS5uYPXGU3Sbl4i9jFtKq9hY7abQ38XLcd6rF9641GlvyRkjU4mVzyqSci7CjFuYvrBgaUuo5BLf8p9xv3LyHDulcHQPbsOC7fmMnvQWChoLIQJsL/jO+hfBcxFyWpTnpMo+gNqIEda+bmkXwciNwPzb63KF8Fr1nVtwphY5b2ySL7S0zU8cKrnbs5qdIlqQWmpajlZeq3TlzKQa1PFhZ1t8gbOsOYeCqlW+JS1QUKqwhdRl/LyOyAVtn4S77MEGp3MBej0BT+d9TRglMHKMl4Ts7nJBWeBTwJ5aPKuvjwsjYtPJdHe+iuOmK5Hhzt/zx7hSs8MjlfnEstDbUNeg54AWhn7RAUwdV8Qwk5W+jkS9tbKGZ5zhnLQ6ZquNeIjVnN1zkmHiPl8zpmnVeF53gshtnFb0Kz1woQk4J+TVDMx2iYxMEaEte8RrJ5gAqnLMtZ4tmouL7onB0JXmLwsiWoyn6WMYtr56IVYq1W+rSxhqPfXcFSfNYV5vkS6VLHo1cAfv5CL304m5yguGr2M3C15D+PdCq/WUfiFj7TDuYoeVPMxBTxgI5dnD6EzbBRrs/kXQG0rPe+V7Q1E8fAn19BsU6Qdz66MH64miZKV5dmsjYZiZeV8n0bebU3DqHrOav/T7lR+qDOYGz+nYg2JaapkeaZtcrXvWOoZ2s/MhtXw4N1HOuJoF3Gs6lDplb57U1DwxM8vziyc/vP6u31zjzCysmcuK9ZJXzDdkonM3AxA+rpNNH71h2MFwrrXUvjIQp+2B5I6qGcWQAW4ulsQQhi49r0lm2+M6TKSQEss0ZUS/dQUZEhqQpj91BcxF0Zr2uWIGj1ER0SWVCucSdxJFRIHVXvzNfEpUzRqb8ipRJiFM/CQSoUZQiiweD05WE/OUNHEbFHXjtuqDjl1Yo3amRNKZMcSLYyCY2UtqtzHrwZVU+fJ0xPC4C6UbDu1JtS340iLMmJHFgKyyNlTTCAKBUd46D+RjMsjiuOnphc0BJTitee0k7jk+TDZRZcx86ITH4p1/ArSFGfAqPLTZt8/oTosXQZeOjrlkDEmO6yaJDK9aO0+WjdF3XpB5suTruQzwtWMfiCpqvVwZrnuEr7mgqbuUBvqmUFnuIMpwGdocB7Sa5d2w9uwwPtdLnPLdfbplMQ3rFxueXpDMefCG3KcQTDnYHe8KAV2LewiXK2vKT9upFIHkestaIolDGmViqEyshjpHovkqughFYs/unpm5NzGwHByBrIPJF/C4WlXDU4Fh4U0OwcC9n7fUOuQqzVqT8pGTLj6PnDrxJ9yw43N7Jnjvcm/nAM8exf7ySVWkDPUpPonaJXqsUxCMZq5dU8gPRiENPsp1E+GQtdQUvjCixfcdJT2rkHIQ5JkPhp5kust4flwIL9x8sg5IiOrPUzrSLy2JMsLutM54EFiN+bEVP2RHYLByanNhrVHGKLQVC3qxYrLlhTTQUTtGTGbljFw8gdpH5qnz18tk+ZPZgpqGL0wc3t0Sut+mzs+SlO5mOzJ7rT78827w+WBd7MkaSI4RwXwjGiCpIdEzHTA0VitaV6fyxnqcxsgxzb483Agl+DW5cDe9AKXRopeJhtKmV6spNylRwmEK34yIfEbCLcMoX03LiC1W49rVJF4x8YtnWiXoLy1/3aaRFvJW4GQDdcpMrszRFfNk1I0Blan4fLJHVURpjVOrJHWsbZVv4VFzd6pkq/MWBjmzbZh1N26+wSipb9b02Why5YSS8ZlbIHkq5Vx9yMZBTDfCvXr8q+h8HMYfAdTIxi0qOk7hmPihiqkvpNkiDwxFm7Y2w7Ll0yOS+HRqtOZqmwVoEwCAmlOF37ychIW5Y89NCGNx6Hae6C/P8Dl23Uuhq6c8mrm0ItMFfQUM/FCXjKJspOh1+RWIkuBdJrK0+SF9Ctps7SGBB5orlROqpOOYks5kBTci6hsla068SJ+9Im1aXyb6OQRtuJ7viybWCzK4D29yinKlutJ00ZuUXq+UMKRmwtxi06yZkZBqMxslmKESS5lNGw1QBfTPBMSVpi0hbF/J0rTl6kLnFEpKcl8x4gFxMMSsExvdsuAihXjSHNR8QBKo7rftOXq2zWZhKkvh+a6Ab4PYNIV1Rqvb6XwG0y/25OoASlb1OjDIzmeGGcZT5FS4+7xTk+sr5wd/L+NbXO9wdLLDo+Jj7qjG/mUBptZfR3VWNz08xkM7BTsriS6aHZccs8d8uNZX57asgHui8tUz1z4lCLeUmH2tSVEKhYd67oyhwOi9eCSg21/LnoNVa6rIfFjbnmnWVLyjtSI7XHtqMry49csrEbvpwSX4aB2+2seeCwawZi1QiALitglXrrJURaScP2Yw32X90ECCQ2jysAVu6vsNSalXLdVsXR7P42KIj8KPj2eSgAZIocVlcUxfIf0hbslLt2Mv0rqSAywmTvWYjY0dX9UeqYrK5AQRrK/xHI2FHM7NuJTPhGzuQ2HW8Bq6QeM1SNjHsIwN1oqXFo1kzy52CyW1GdTcB1K1OiTGHude3m7Dwp6RFoWcFepVIn/0caajA4rqcMKNc89OJXFb24Rc4hXddDOmpjlfU5CL+sPRNFx63M0AzJh3ZDypO41KOy3c2C67U+4r2KVCTUOlroLh2r20kF+FsnCThiTO8+2VIA+AJjxKbk8SGng2PScHZKCqheFotJmCnubnLmp2U+FuV2493eblcr+VsZxCaibIMxRN2ZmQM7QbMmhPHV32cWJ21/C1Yd3D1+7ZniJNtspUL7gATeXhmiZzBU1014YtM0r9SRRc1qD6QsAxgZMqYb0HMh2s6jEHmIzWzpQF/XggwWsXnkO6lQdlrY/h6TX1SHRzRyhjb+LIognyKQTTdLQaBp8RSZn6R09l/O2JT6h0f9Jdd0PXSrJv7JVKbNXd6NRJmxqUoCUENtyQN0ha6htZvq4utPjOE2p7uGdH/OjyU1zjXuUftQHG7CXPzVt31abbEEmgP5xqTNZldBjCADPGLfPYK8ojeniJaHZwX/UtgXE5YaiygAM4RaZxjTZS4y6iCrEJFzDH6QYtJzNDicvotQTXOA56PYp4XKdB2OFXGlWOti1Ooh22lT3c2FZMyGnnWbY1nssvjSmWQYov6NRjkXYHLeX+ZKWdW+RWvxzy1OQcqm+XOmLkqAWtBMEnlyo7W/DMhjUDBD4iNOsiDXHVBONSlE1ZSi8U7Mpmr9PFOtpZ1yJMx3MZxTJuOWx3vz/Lvs+u7lZ327qrF85YL6Tqn3u1J7V29+6LEqW7yepPYb9mg7u2mIEd6MkRFhK6M0c8sKMLN6pze8L06yQTdQen2D02HwTinKo04B5dhxZUYFex31286Un7KzNS+5LJkcs9ng/Ao8/LyMvk5fSCjPvIQ+Nd8YK8DV/Na+gk2VCDZ5CopKL74z24LScb7ofyHgPCn1xa2JAE6knDgcdcy+oW8wPJcyhjLm65eqM0PyCPPVtsLK7+DD/dJbwHT+aRmoMGL88jPV1zBB/UPpvKOHu0JKyFvSuQgfFEQCuMENdvrlhgRpXR+04+eVKyyd3oQAQYoCGj65PQDplOxlKftl5Rb9nPVA/O1bnmxdeDvx3qRt7CkZ8mWVw88TpteqDPPOrUwHMWrBtMUkwS84DqwJEshRxjdB1su+5djIVlynd4gx8Q/TjIDF0XPt1c63aT7AsCiC52UfyAd6ehI2LJ5S29bjGnfKzuAgfOS62IoRVOqrxsyniCcE9bbgR9PF3YCfxhjfoRuPj16vfZcFbmLtCzq/uVqJbRia5OD5koT0+dVvo0uUz77AozumQn+7LmagRwWJfinpZ39HXtlBVSL9r6pFU3XRPKdgUWf+AiLqc+i/O3/lE/JPO+Co4B95dR28biuifuoRfz3bigseMhaWWkcnhBfRouBR56vqYrbA1PpOSx1mjboU7hybvCe+9vA0xrAh4brBMEs0Bz0hMGk31znRK0nfzMVatblO927o4VtPfYfCNg3EM3ZCyvE6U+ShoXz3esGKPujOjQeLzcRUITYu30hDzsh2o5a+AUV9SbZXYXkiSL0XHpzQS3U/u6clzCeJl6TcZaGCEMO13uezvM802Q765p8xHUDUhWOM55FMWZHye+5S/9UJV8H+GXk2MUo+APQ+lohZaEV8ZAWv6A7ZKodReFOVetk6lGu/FxuQsEIprRFgwZw/CZAL3iUWt6y01BO3rAvifU/pxhJxXyn0gACEpMPOWchDrAuJ1mWJ8HKiZL5IYoJ9Z4qbywcG2INSCzp3V2nGY+OaN+Qp4euXDnZnhWeJQw9+BxpZShSNVqv2SR9+rWYSwyQ3m07nzx0H6aG/iammsxXoIlxplmikzPrUhhdlwTI7xycVfjjEMSFlbavU15V1ua672+jmKqkBcH7h7XS4Sotqgl+mV4zqdgfV9PXq15n2Hfv7d5fU9MGragyVTx44CaOKPLgyZtpsuVXoB7KYb1U45gt+JBcdluTZPLonS/CUvBFucVKW7PHm0W5ZU27C0ecAwu8dKs8kBRmjuNJrvfWQUSPMnE6NHCWrOQY0fdTMmm0GbsnvPeVqwjwoTXhrIgQ5LlvsSzmlyU4SHr7G6G41Brm4+I0mPt4B61XkfxiM79ginlmboD4D6VGOoc3hizokoTLwTmZIigUOnJK6/zOZCI2BWviGypydTzkosruFFK+rybVHsoUkC0Lnkmr5flNU5bBhx9gJHo7qDVvb1g96Zjw41IB4RpnVo3Lq8BaU8z25on+pEcqrZHc+ds86DV1Xp1kzhYOJKC8zKl+INK5FcePeXdsAmsJ04HpJTFqpJ3SI3uYJzdVd/jA+iOjiVB+3zDdU7BIjad7bzvIvUTFcljWOstxy5Q8Mwmzp5I1w42nZR0zRIPZFIA8ZXC8TIoNKRwCYoEzqIKSmqhBFKtOGq79dAa98xylJpUMiEE6b43geE6/p2UrTOgqD37ZJYF9SqdPJHe0VL6uqKGyexh5+Cd9EAmjc1Tz4efRcznpkTfWxWDPVDwosvsZca7FR4+mWRuiHrVFYDpiRVl8CVWa1AeHKxfO3qYctRXwz3FwLwKO/vQpturD6cM7V9U6my37sIYPXRi5N3PmKPMu5F4MBWL5mR8FeXVcAnkvnaPfJ9oPCyoY85cpe1YHz0seiRUurhCQXXtQaq9YFO504+zd7rKBnS5EdyierV4ubYixZ9naqTuN5Ho2qEtpFrGk5TlKWvoHwL7/rdEawM/+1NAvsJmDzJm3Nzauq5qu0ulf7wyoS2zVDWDx5m5MSyRIQgtQcOrNCjqyw9f3lcXv99w+y//E4b3bZ//3y4dfbsf1K3v+8dx+r5lNaZh8tPnWT/916r8rx++jHEJFPl2nWqql/zX60f/6jLV12z6+rvQr3+6TDUd3/43g66d033+9drfHObTny/qgaWW9gB/s12SfOXHsK3AF9p6u5FS7r/f3gMnfHr2+036r9/vCb/v1SklL7JfRfHXK3tf/9OVvSgFqv92Iw88AP5Z0q/vs94X0/7X+8E4fbtSdvrxDGz/x/8GPVWsga5HAAA= -->
