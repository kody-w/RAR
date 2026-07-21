"""
Prior Authorization Agent for Healthcare.

Manages prior authorization requests, checks clinical criteria against
payer rules, tracks authorization status, and prepares appeal documentation
for denied or pending authorizations.

Version 1.1.0 extends the agent with six outcomes demonstrated in the source
prior authorization demo while preserving every legacy operation:

- ``authorization_verification`` — Authorization Intake and Verification
- ``payer_requirement``          — Payer Requirement Analysis
- ``authorization_submission``   — Authorization Submission and Notification (simulated write)
- ``approval_prediction``        — Approval Probability and Appeal Strategy (generative)
- ``authorization_tracking``     — Authorization Tracking and Teams Notification (simulated write)
- ``denial_appeal_status``       — Denial and Active Appeal Insight

Each new capability is a keyed lookup over embedded evidence records. Pass an
exact record key via ``key`` (or embed it in ``user_input``) to retrieve one
record; omit it for a no-input evidence summary. Write-capable operations emit
an explicit *simulated* write receipt and never mutate an external system — all
data lives in-file and every response is fully deterministic.
"""

import sys
import os
import re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/prior_authorization",
    "version": "1.1.1",
    "display_name": "Prior Authorization Agent",
    "description": "Tracks prior-authorization requests, clinical criteria checks, and appeals against built-in demo payer rules.",
    "author": "AIBAST",
    "tags": ["prior-auth", "authorization", "payer", "clinical-criteria", "appeals", "healthcare"],
    "category": "healthcare",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ---------------------------------------------------------------------------
# Synthetic domain data
# ---------------------------------------------------------------------------

AUTH_REQUESTS = {
    "AUTH-4001": {
        "patient": "Margaret Sullivan",
        "patient_id": "PT-10045",
        "procedure": "Left Knee MRI without Contrast",
        "cpt_code": "73721",
        "diagnosis": "M17.12 - Primary osteoarthritis, left knee",
        "requesting_provider": "Dr. Anita Patel",
        "payer": "Blue Cross Blue Shield of Illinois",
        "plan": "PPO Gold",
        "submitted_date": "2026-03-13",
        "status": "approved",
        "decision_date": "2026-03-14",
        "auth_number": "BCBS-AUTH-884210",
        "valid_through": "2026-06-14",
        "notes": "Auto-approved based on clinical criteria match.",
    },
    "AUTH-4002": {
        "patient": "Robert Kim",
        "patient_id": "PT-10078",
        "procedure": "Cardiac Stress Test (Nuclear)",
        "cpt_code": "78452",
        "diagnosis": "R07.9 - Chest pain, unspecified",
        "requesting_provider": "Dr. James Wright",
        "payer": "Aetna",
        "plan": "HMO Select",
        "submitted_date": "2026-03-15",
        "status": "pending_review",
        "decision_date": None,
        "auth_number": None,
        "valid_through": None,
        "notes": "Requires peer-to-peer review. Additional documentation requested.",
    },
    "AUTH-4003": {
        "patient": "Maria Gonzalez",
        "patient_id": "PT-20003",
        "procedure": "Total Hip Arthroplasty",
        "cpt_code": "27130",
        "diagnosis": "M16.11 - Primary osteoarthritis, right hip",
        "requesting_provider": "Dr. Michael Torres",
        "payer": "Medicare Part B",
        "plan": "Original Medicare",
        "submitted_date": "2026-03-10",
        "status": "approved",
        "decision_date": "2026-03-11",
        "auth_number": "MCR-AUTH-THA-99201",
        "valid_through": "2026-09-11",
        "notes": "Medicare LCD criteria met. Pre-op clearance required.",
    },
    "AUTH-4004": {
        "patient": "David Nguyen",
        "patient_id": "PT-20002",
        "procedure": "Lumbar Spine MRI with Contrast",
        "cpt_code": "72149",
        "diagnosis": "M54.5 - Low back pain",
        "requesting_provider": "Dr. James Wright",
        "payer": "Aetna",
        "plan": "HMO Select",
        "submitted_date": "2026-03-08",
        "status": "denied",
        "decision_date": "2026-03-12",
        "auth_number": None,
        "valid_through": None,
        "notes": "Denied: Conservative therapy requirement not met. Minimum 6 weeks PT required.",
    },
}

CLINICAL_CRITERIA = {
    "73721": {
        "procedure": "Knee MRI",
        "payer_rules": {
            "BCBS": {"requires": ["Physical exam documented", "X-ray completed", "Conservative therapy >= 4 weeks"], "auto_approve": True},
            "Aetna": {"requires": ["Physical exam documented", "X-ray completed", "Conservative therapy >= 6 weeks", "Specialist referral"], "auto_approve": False},
            "Medicare": {"requires": ["Physical exam documented", "Imaging appropriate per LCD"], "auto_approve": True},
        },
        "avg_turnaround_days": 1.5,
        "approval_rate_pct": 92,
    },
    "78452": {
        "procedure": "Nuclear Cardiac Stress Test",
        "payer_rules": {
            "BCBS": {"requires": ["Cardiac risk factors documented", "EKG performed", "Symptoms documented"], "auto_approve": False},
            "Aetna": {"requires": ["Cardiac risk factors documented", "EKG performed", "Peer-to-peer if age < 55"], "auto_approve": False},
            "Medicare": {"requires": ["Symptoms documented", "EKG performed"], "auto_approve": True},
        },
        "avg_turnaround_days": 3.2,
        "approval_rate_pct": 78,
    },
    "27130": {
        "procedure": "Total Hip Arthroplasty",
        "payer_rules": {
            "BCBS": {"requires": ["Failed conservative therapy >= 3 months", "Imaging confirming severe OA", "Functional impairment documented"], "auto_approve": False},
            "Aetna": {"requires": ["Failed conservative therapy >= 3 months", "Imaging", "Functional assessment", "BMI < 40"], "auto_approve": False},
            "Medicare": {"requires": ["LCD criteria met", "Pre-op clearance", "Imaging"], "auto_approve": True},
        },
        "avg_turnaround_days": 5.0,
        "approval_rate_pct": 85,
    },
    "72149": {
        "procedure": "Lumbar MRI with Contrast",
        "payer_rules": {
            "BCBS": {"requires": ["Conservative therapy >= 4 weeks", "Red flags absent", "Physical exam documented"], "auto_approve": True},
            "Aetna": {"requires": ["Conservative therapy >= 6 weeks", "Physical therapy documented", "Red flags absent"], "auto_approve": False},
            "Medicare": {"requires": ["Symptoms documented", "Exam documented"], "auto_approve": True},
        },
        "avg_turnaround_days": 2.0,
        "approval_rate_pct": 74,
    },
}

PAYER_APPROVAL_RATES = {
    "Blue Cross Blue Shield of Illinois": {"overall_pct": 88, "avg_days": 1.8, "appeal_success_pct": 62},
    "Aetna": {"overall_pct": 72, "avg_days": 4.1, "appeal_success_pct": 48},
    "Medicare Part B": {"overall_pct": 94, "avg_days": 1.2, "appeal_success_pct": 71},
}


# ---------------------------------------------------------------------------
# v1.1.0 — Data-driven capabilities (source demo)
#
# Each capability is a self-contained record: the demonstrated response,
# knowledge statements, and evidence records keyed by an exact identifier,
# and the write/generative provenance flags. Everything is embedded in-file;
# nothing calls an external system. Write-capable operations return a clearly
# labelled *simulated* receipt only.
# ---------------------------------------------------------------------------

CAPABILITIES = {
    "authorization_verification": {
        "display_name": "Authorization Intake and Verification",
        "class_ref": "AuthorizationVerificationAgent",
        "summary": "Verifies patient demographics, coverage, and clinical documentation into a single decision-ready view.",
        "response": "I've verified patient demographics, insurance coverage, and clinical documentation into one decision-ready view. Ready to submit.",
        "source_system": "EHR and insurance verification",
        "customer": "multispecialty orthopedic practice",
        "write": False,
        "generative": False,
        "exact_key_required": True,
        "key_field": "request_id",
        "key_label": "Request ID",
        "knowledge": [
            "Connects to EHR systems and insurance verification to confirm patient demographics, coverage, and clinical documentation before submission.",
            "Presents verified patient, coverage, and documentation status together in a single decision-ready view.",
            "The coordinator provides key context while the agent assembles the verified authorization intake.",
        ],
        "records": [
            {
                "request_id": "MR-489327",
                "patient": "Robert Chen, DOB 05/22/1965",
                "payer": "PPO #XY4829103",
                "procedure": "72148 - Lumbar MRI without contrast",
                "diagnosis": "M54.5 - Chronic low back pain",
                "provider": "Dr. Thompson, NPI 1234567890",
                "coverage_status": "Verified",
                "documentation_status": "Complete - failed 6 weeks conservative therapy",
            },
        ],
    },
    "payer_requirement": {
        "display_name": "Payer Requirement Analysis",
        "class_ref": "PayerRequirementAgent",
        "summary": "Checks payer-specific requirements against the patient's documentation and confirms whether all criteria are met.",
        "response": "Payer requirement analysis complete. I checked the payer criteria against the patient's documentation and confirmed the matches.",
        "source_system": "Payer portal and clinical documentation",
        "customer": "multispecialty orthopedic practice",
        "write": False,
        "generative": False,
        "exact_key_required": True,
        "key_field": "cpt_code",
        "key_label": "CPT Code",
        "knowledge": [
            "Pulls payer-specific requirements and matches them with EHR data through automated criteria screening.",
            "Automatically checks payer requirements against the patient's documentation and confirms when all criteria are met.",
            "Flags missing elements when payer criteria are only partially satisfied.",
        ],
        "records": [
            {
                "cpt_code": "72148",
                "payer": "PPO #XY4829103",
                "procedure": "Lumbar MRI without contrast",
                "requirement_met": "Yes",
                "evidence_source": "Last 3 office visits; PT for 6 weeks; NSAIDs; symptoms for 8 weeks without improvement",
                "estimated_review": "24-48 hours",
            },
        ],
    },
    "authorization_submission": {
        "display_name": "Authorization Submission and Notification",
        "class_ref": "AuthorizationSubmissionAgent",
        "summary": "Submits the request to the payer, returns submission details, and notifies the patient and care team.",
        "response": "Authorization request submitted. Here are the submission details, and I've sent notifications to the patient and the care team.",
        "source_system": "Electronic payer portal",
        "customer": "multispecialty orthopedic practice",
        "write": True,
        "generative": False,
        "exact_key_required": True,
        "key_field": "submission_id",
        "key_label": "Submission ID",
        "knowledge": [
            "Submits requests directly to payer portals and sends real-time updates once submitted.",
            "Provides submission details in moments, including submission time and expected decision timeline.",
            "Intelligently sends notifications to the patient and the care team after submission.",
        ],
        "records": [
            {
                "submission_id": "PA-2024-892741",
                "patient": "Robert Chen",
                "payer_reference": "Case #4729183",
                "submitted_at": "Today at 3:47 PM",
                "expected_decision": "2 business days",
                "screening": "Automated criteria screening",
                "notifications_sent": "Patient SMS with tracking link and care team update",
            },
        ],
    },
    "approval_prediction": {
        "display_name": "Approval Probability and Appeal Strategy",
        "class_ref": "ApprovalPredictionAgent",
        "summary": "Calculates an approval probability from documentation and outlines an appeal strategy if the request is denied.",
        "response": "I analyzed the documentation to calculate an approval probability and prepared an appeal strategy in case the request is denied.",
        "source_system": "Clinical documentation and historical authorization outcomes",
        "customer": "multispecialty orthopedic practice",
        "write": False,
        "generative": True,
        "exact_key_required": True,
        "key_field": "authorization",
        "key_label": "Authorization",
        "knowledge": [
            "Analyzes documentation and calculates an approval probability based on comprehensive evidence meeting payer criteria.",
            "Predicts approval likelihood and prepares automated appeal packages to protect revenue and reduce delays.",
            "In the same motion, outlines an appeal strategy should the request be denied.",
        ],
        "records": [
            {
                "authorization": "PA-2024-892741",
                "procedure": "Lumbar MRI",
                "approval_probability": "87%",
                "historical_approval_rate": "94% for similar cases",
                "appeal_strategy": "Peer-to-peer review with radiologist; add functional impact documentation and imaging-guideline citation",
            },
        ],
    },
    "authorization_tracking": {
        "display_name": "Authorization Tracking and Teams Notification",
        "class_ref": "AuthorizationTrackingAgent",
        "summary": "Configures multi-party notifications and scheduled status checks, then shares the dashboard via Microsoft Teams.",
        "response": "Automated tracking configured with multi-party notifications and scheduled status checks, and I've shared the monitoring dashboard through Microsoft Teams.",
        "source_system": "Payer portal, secure messaging, and Microsoft Teams",
        "customer": "multispecialty orthopedic practice",
        "write": True,
        "generative": False,
        "exact_key_required": True,
        "key_field": "authorization",
        "key_label": "Authorization",
        "knowledge": [
            "Sets up multi-party notifications and scheduled status checks for an authorization.",
            "Shares the monitoring dashboard through Microsoft Teams to drive alignment with the broader clinical team.",
            "Configures auto-escalation rules that trigger if no decision is reached within the set window.",
        ],
        "records": [
            {
                "authorization": "PA-2024-892741",
                "status_check_interval": "Every 4 hours",
                "expected_decision": "2 business days",
                "escalation_rule": "Auto-trigger if no decision in 48 hours; alert within 2 hours of decision",
                "notifications_sent": "Patient SMS on approval; radiology scheduling alert; Dr. Thompson secure message",
                "appeal_readiness": "Appeal workflow ready if denied",
            },
        ],
    },
    "denial_appeal_status": {
        "display_name": "Denial and Active Appeal Insight",
        "class_ref": "DenialAppealStatusAgent",
        "summary": "Explains the demonstrated Medicare sleep-study denial and its active appeal status; the legacy auth_request operation already supplies the portfolio view.",
        "response": "Here is the Medicare denial analysis and the active appeal status, including actions already taken and the expected decision timeline.",
        "source_system": "Medicare portal and appeal tracking",
        "customer": "multispecialty orthopedic practice",
        "write": False,
        "generative": False,
        "exact_key_required": True,
        "key_field": "case_key",
        "key_label": "Case Key",
        "knowledge": [
            "Captures denial details and outlines how the appeal is already underway when a request is denied.",
            "Gives the coordinator clarity and confidence on next steps for pending and denied cases.",
            "The existing auth_request operation remains the portfolio view, avoiding a duplicate operation.",
        ],
        "records": [
            {
                "case_key": "Johnson Sleep Study",
                "patient": "Johnson",
                "procedure": "Sleep Study",
                "status": "Denied - active appeal in peer-to-peer review",
                "appeal_actions": "Peer-to-peer review tomorrow at 2 PM; additional symptom questionnaire completed",
                "appeal_probability": "78%",
                "expected_decision": "Within 5 business days",
            },
        ],
    },
}

# Human-friendly labels for record fields when rendered.
_FIELD_LABELS = {
    "request_id": "Request ID", "cpt_code": "CPT Code", "submission_id": "Submission ID",
    "case_key": "Case Key",
    "patient": "Patient", "payer": "Payer", "procedure": "Procedure",
    "diagnosis": "Diagnosis", "provider": "Provider", "payer_reference": "Payer Reference",
    "coverage_status": "Coverage Status", "documentation_status": "Documentation Status",
    "requirement_met": "Requirement Met", "evidence_source": "Evidence Source",
    "estimated_review": "Estimated Review", "screening": "Screening",
    "submitted_at": "Submitted At", "expected_decision": "Expected Decision",
    "notifications_sent": "Notifications Sent", "approval_probability": "Approval Probability",
    "historical_approval_rate": "Historical Approval Rate",
    "appeal_probability": "Appeal Probability", "appeal_strategy": "Appeal Strategy",
    "authorization": "Authorization", "status_check_interval": "Status Check Interval",
    "escalation_rule": "Escalation Rule", "appeal_readiness": "Appeal Readiness",
    "status": "Status", "appeal_actions": "Appeal Actions",
}


def _field_label(field: str) -> str:
    return _FIELD_LABELS.get(field, field.replace("_", " ").title())


def _normalize_lookup_token(value: str) -> str:
    normalized = " ".join(str(value or "").strip().lower().split())
    return re.sub(r"^[^a-z0-9]+|[^a-z0-9]+$", "", normalized)


def _resolve_record(cap: dict, user_input: str, key: str):
    """Exact keyed lookup. Returns (mode, record) where mode is match/notfound/summary."""
    key_field = cap["key_field"]
    raw_key = str(key or "").strip()
    if raw_key:
        explicit_key = _normalize_lookup_token(raw_key)
        for rec in cap["records"]:
            record_key = _normalize_lookup_token(rec[key_field])
            if record_key == explicit_key:
                return ("match", rec)
        return ("notfound", None)

    normalized_input = " ".join(str(user_input or "").strip().lower().split())
    if normalized_input:
        for rec in cap["records"]:
            record_key = _normalize_lookup_token(rec[key_field])
            boundary_pattern = rf"(?<![a-z0-9_-]){re.escape(record_key)}(?![a-z0-9_-])"
            if re.search(boundary_pattern, normalized_input):
                return ("match", rec)
        return ("notfound", None)
    return ("summary", None)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _auth_request_status():
    requests = []
    for aid, auth in AUTH_REQUESTS.items():
        requests.append({
            "id": aid, "patient": auth["patient"], "procedure": auth["procedure"],
            "cpt": auth["cpt_code"], "payer": auth["payer"], "status": auth["status"],
            "submitted": auth["submitted_date"], "decision": auth["decision_date"] or "Pending",
            "auth_number": auth["auth_number"] or "N/A",
        })
    status_counts = {}
    for r in requests:
        status_counts[r["status"]] = status_counts.get(r["status"], 0) + 1
    return {"requests": requests, "status_counts": status_counts}


def _clinical_criteria_check():
    checks = []
    for aid, auth in AUTH_REQUESTS.items():
        cpt = auth["cpt_code"]
        criteria = CLINICAL_CRITERIA.get(cpt, {})
        payer_key = None
        for key in ["BCBS", "Aetna", "Medicare"]:
            if key.lower() in auth["payer"].lower():
                payer_key = key
                break
        rules = criteria.get("payer_rules", {}).get(payer_key, {})
        checks.append({
            "auth_id": aid, "patient": auth["patient"],
            "procedure": auth["procedure"], "cpt": cpt,
            "payer": auth["payer"],
            "requirements": rules.get("requires", []),
            "auto_approve": rules.get("auto_approve", False),
            "approval_rate": criteria.get("approval_rate_pct", 0),
            "avg_turnaround": criteria.get("avg_turnaround_days", 0),
        })
    return {"checks": checks}


def _status_tracking():
    tracking = []
    for aid, auth in AUTH_REQUESTS.items():
        payer_stats = PAYER_APPROVAL_RATES.get(auth["payer"], {})
        tracking.append({
            "id": aid, "patient": auth["patient"], "procedure": auth["procedure"],
            "status": auth["status"], "payer": auth["payer"],
            "submitted": auth["submitted_date"],
            "decision": auth["decision_date"] or "Awaiting",
            "valid_through": auth["valid_through"] or "N/A",
            "payer_avg_days": payer_stats.get("avg_days", 0),
            "notes": auth["notes"],
        })
    return {"tracking": tracking}


def _appeal_preparation():
    denied = [auth for auth in AUTH_REQUESTS.values() if auth["status"] == "denied"]
    appeals = []
    for auth in denied:
        payer_stats = PAYER_APPROVAL_RATES.get(auth["payer"], {})
        criteria = CLINICAL_CRITERIA.get(auth["cpt_code"], {})
        payer_key = None
        for key in ["BCBS", "Aetna", "Medicare"]:
            if key.lower() in auth["payer"].lower():
                payer_key = key
                break
        rules = criteria.get("payer_rules", {}).get(payer_key, {})
        appeals.append({
            "patient": auth["patient"], "procedure": auth["procedure"],
            "payer": auth["payer"], "denial_reason": auth["notes"],
            "criteria_not_met": rules.get("requires", []),
            "appeal_success_rate": payer_stats.get("appeal_success_pct", 0),
            "recommended_actions": [
                "Document conservative therapy completed to date",
                "Obtain physical therapy records",
                "Schedule peer-to-peer review with medical director",
                "Submit supplemental clinical documentation",
            ],
        })
    return {"appeals": appeals, "total_denied": len(denied)}


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

class PriorAuthorizationAgent(BasicAgent):
    """Prior authorization management and clinical criteria checking agent."""

    def __init__(self):
        self.name = "PriorAuthorizationAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "auth_request",
                            "clinical_criteria_check",
                            "status_tracking",
                            "appeal_preparation",
                            "authorization_verification",
                            "payer_requirement",
                            "authorization_submission",
                            "approval_prediction",
                            "authorization_tracking",
                            "denial_appeal_status",
                        ],
                        "description": "The prior authorization operation to perform.",
                    },
                    "auth_id": {
                        "type": "string",
                        "description": "Optional authorization ID to filter results.",
                    },
                    "key": {
                        "type": "string",
                        "description": "Optional exact evidence key (MR-489327, 72148, PA-2024-892741, or Johnson Sleep Study).",
                    },
                    "user_input": {
                        "type": "string",
                        "description": "Optional natural-language request; an exact record key embedded here is matched automatically.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "auth_request")
        if op == "auth_request":
            return self._auth_request()
        elif op == "clinical_criteria_check":
            return self._clinical_criteria_check()
        elif op == "status_tracking":
            return self._status_tracking()
        elif op == "appeal_preparation":
            return self._appeal_preparation()
        elif op in CAPABILITIES:
            return self._run_capability(
                op,
                user_input=kwargs.get("user_input", ""),
                key=kwargs.get("key", ""),
            )
        return f"**Error:** Unknown operation `{op}`."

    def _auth_request(self) -> str:
        data = _auth_request_status()
        lines = [
            "# Prior Authorization Requests",
            "",
            "**Status Summary:** " + " | ".join(f"{s}: {c}" for s, c in data["status_counts"].items()),
            "",
            "| ID | Patient | Procedure | CPT | Payer | Status | Submitted | Decision | Auth # |",
            "|----|---------|-----------|-----|-------|--------|-----------|----------|--------|",
        ]
        for r in data["requests"]:
            lines.append(
                f"| {r['id']} | {r['patient']} | {r['procedure']} | {r['cpt']} "
                f"| {r['payer']} | {r['status'].upper()} | {r['submitted']} "
                f"| {r['decision']} | {r['auth_number']} |"
            )
        return "\n".join(lines)

    def _clinical_criteria_check(self) -> str:
        data = _clinical_criteria_check()
        lines = ["# Clinical Criteria Check", ""]
        for c in data["checks"]:
            auto = "Yes" if c["auto_approve"] else "No"
            lines.append(f"## {c['auth_id']}: {c['procedure']} ({c['patient']})")
            lines.append(f"**Payer:** {c['payer']} | **Auto-Approve:** {auto}")
            lines.append(f"**Historical Approval Rate:** {c['approval_rate']}% | **Avg Turnaround:** {c['avg_turnaround']} days")
            lines.append("")
            lines.append("**Requirements:**")
            for req in c["requirements"]:
                lines.append(f"- {req}")
            lines.append("")
        return "\n".join(lines)

    def _status_tracking(self) -> str:
        data = _status_tracking()
        lines = ["# Authorization Status Tracking", ""]
        for t in data["tracking"]:
            lines.append(f"## {t['id']}: {t['procedure']}")
            lines.append(f"- Patient: {t['patient']}")
            lines.append(f"- Payer: {t['payer']} (avg decision: {t['payer_avg_days']} days)")
            lines.append(f"- Status: {t['status'].upper()}")
            lines.append(f"- Submitted: {t['submitted']} | Decision: {t['decision']} | Valid Through: {t['valid_through']}")
            lines.append(f"- Notes: {t['notes']}")
            lines.append("")
        return "\n".join(lines)

    def _appeal_preparation(self) -> str:
        data = _appeal_preparation()
        if data["total_denied"] == 0:
            return "# Appeal Preparation\n\nNo denied authorizations requiring appeals."
        lines = [
            "# Appeal Preparation",
            "",
            f"**Total Denied Authorizations:** {data['total_denied']}",
            "",
        ]
        for a in data["appeals"]:
            lines.append(f"## {a['procedure']} - {a['patient']}")
            lines.append(f"**Payer:** {a['payer']}")
            lines.append(f"**Denial Reason:** {a['denial_reason']}")
            lines.append(f"**Appeal Success Rate:** {a['appeal_success_rate']}%")
            lines.append("")
            lines.append("**Criteria Not Met:**")
            for c in a["criteria_not_met"]:
                lines.append(f"- {c}")
            lines.append("")
            lines.append("**Recommended Actions:**")
            for action in a["recommended_actions"]:
                lines.append(f"1. {action}")
            lines.append("")
        return "\n".join(lines)


    # -----------------------------------------------------------------
    # v1.1.0 — data-driven capability renderer (exact keyed lookup)
    # -----------------------------------------------------------------
    def _run_capability(self, op: str, user_input: str = "", key: str = "") -> str:
        cap = CAPABILITIES[op]
        mode, record = _resolve_record(cap, user_input, key)
        if mode == "notfound":
            attempted = str(key or "").strip() or str(user_input or "").strip()
            return self._capability_notfound(cap, attempted)
        if mode == "match":
            return self._capability_detail(cap, record)
        return self._capability_summary(cap)

    def _provenance_lines(self, cap: dict) -> list:
        return [
            "",
            "**Provenance**",
            f"- Source system: {cap['source_system']} (evidence-derived data embedded in-agent)",
            f"- Customer: {cap['customer']}",
            f"- Write: {'yes (simulated only)' if cap['write'] else 'no (read-only)'} "
            f"| Generative: {'yes' if cap['generative'] else 'no'} "
            f"| Exact key required: {'yes' if cap['exact_key_required'] else 'no'}",
        ]

    def _knowledge_lines(self, cap: dict) -> list:
        lines = ["", "**Knowledge**"]
        for k in cap["knowledge"]:
            lines.append(f"- {k}")
        return lines

    def _capability_detail(self, cap: dict, record: dict) -> str:
        key_field = cap["key_field"]
        key_val = record[key_field]
        lines = [
            f"# {cap['display_name']}",
            "",
            f"> {cap['response']}",
            "",
            f"## {cap['key_label']}: {key_val}",
        ]
        for field, value in record.items():
            lines.append(f"- **{_field_label(field)}:** {value}")
        if cap["generative"]:
            lines.append("")
            lines.append("_Deterministic generative outcome captured from the demonstrated documentation analysis._")
        lines += self._knowledge_lines(cap)
        if cap["write"]:
            receipt = f"SIM-RCPT-{key_val}"
            lines += [
                "",
                "**Simulated Write Receipt**",
                f"- Receipt ID: {receipt}",
                f"- Action: recorded against `{key_val}` in the in-agent store",
                "- Status: SIMULATED — no external system was contacted or mutated.",
                "- All evidence-derived data is embedded; this call has no side effects.",
            ]
        else:
            lines += [
                "",
                "_Read-only operation: no data was written and no external system was mutated._",
            ]
        lines += self._provenance_lines(cap)
        return "\n".join(lines)

    def _capability_summary(self, cap: dict) -> str:
        key_field = cap["key_field"]
        fields = list(cap["records"][0].keys())
        headers = [_field_label(f) for f in fields]
        lines = [
            f"# {cap['display_name']}",
            "",
            f"> {cap['response']}",
            "",
            cap["summary"],
            "",
            f"**Portfolio ({len(cap['records'])} records)** — provide an exact "
            f"{cap['key_label']} via `key` or in `user_input` for full detail.",
            "",
            "| " + " | ".join(headers) + " |",
            "|" + "|".join(["---"] * len(headers)) + "|",
        ]
        for rec in cap["records"]:
            lines.append("| " + " | ".join(str(rec[f]) for f in fields) + " |")
        keys = ", ".join(rec[key_field] for rec in cap["records"])
        lines += ["", f"**Available {cap['key_label']}s:** {keys}"]
        lines += self._knowledge_lines(cap)
        if cap["write"]:
            lines += [
                "",
                "_This capability can record a simulated write when a specific key is supplied; "
                "no external system is ever mutated._",
            ]
        lines += self._provenance_lines(cap)
        return "\n".join(lines)

    def _capability_notfound(self, cap: dict, key: str) -> str:
        keys = ", ".join(rec[cap["key_field"]] for rec in cap["records"])
        return (
            f"# {cap['display_name']}\n\n"
            f"**Error:** No record found for {cap['key_label']} `{key}`.\n\n"
            f"This capability requires an exact key match. "
            f"Available {cap['key_label']}s: {keys}."
        )


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    agent = PriorAuthorizationAgent()
    legacy_ops = ["auth_request", "clinical_criteria_check", "status_tracking", "appeal_preparation"]
    for op in legacy_ops:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
    for op in CAPABILITIES:
        print(f"\n{'='*60}")
        print(f"Operation: {op} (no-input summary)")
        print("=" * 60)
        print(agent.perform(operation=op))
        sample_key = CAPABILITIES[op]["records"][0][CAPABILITIES[op]["key_field"]]
        print(f"\n{'-'*60}")
        print(f"Operation: {op} (keyed: {sample_key})")
        print("-" * 60)
        print(agent.perform(operation=op, key=sample_key))
