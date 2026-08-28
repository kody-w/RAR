---
name: "rar-aibast-agents-library-prior-authorization"
description: "Tracks prior-auth requests and appeals, joining a live simulated FHIR server (denied preauth claim) with the Dynamics 365 CRM case; offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/prior_authorization", "rar_sha256": "dea92230903fbd44557fa79a63bd008addf48c63d672390890f0bfb8b99e1779", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.3.0", "author": "AIBAST", "tags": ["prior-auth", "authorization", "payer", "clinical-criteria", "appeals", "healthcare"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/prior_authorization`. The original RAPP
agent is preserved byte-for-byte in `prior_authorization_agent.py` and in the RCI capsule.

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

Prior Authorization Agent — a template you are meant to mutate.

Manages prior authorization requests, checks clinical criteria against
payer rules, tracks authorization status, prepares appeal documentation,
and replays six demonstrated capability outcomes (keyed evidence lookups
with simulated write receipts — never live writes).

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works from anywhere):
       CRM  — the Static Dynamics 365 tenant (Aster Lane Office Systems):
              https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
              A Dynamics case for the healthcare account Riverbend
              Medical Group is reinterpreted as an authorization
              work-queue item — e.g. CAS-260124 "Prior authorization
              request pending beyond SLA".
       FHIR — the Static FHIR R4 server (Riverbend Medical Group):
              https://kody-w.github.io/static-fhir/fhir/
              The denied preauthorization Claim RMG-CLM-260108 (the
              $1,875 Cardiac MRI) and the cancelled Appointment it
              references.
     Try: perform(operation="auth_request")
     — one briefing joins the denied FHIR preauth Claim, the cancelled
     FHIR Appointment it deferred, and the CRM case CAS-260124 that
     tracks the same SLA breach: three systems in one output.
  2. No network? Everything falls back to the embedded demo layer below
     (AUTH_REQUESTS / CLINICAL_CRITERIA / CAPABILITIES) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PRIOR_AUTHORIZATION_DATA_URL (CRM side) to any OData-shaped endpoint
     and PRIOR_AUTHORIZATION_FHIR_URL (clinical side) to any FHIR R4
     searchset-bundle host — or replace _fetch_collection() /
     _fetch_fhir_bundle() with an X12 278 or payer-API client. Fields the
     rest of the file needs are listed in _normalize_live_auth() — CPT
     code and auth number render as "n/a — enrichment seam" until you
     wire a payer system.

OPERATIONS
  auth_request | clinical_criteria_check | status_tracking
  | appeal_preparation | authorization_verification | payer_requirement
  | authorization_submission | approval_prediction | authorization_tracking
  | denial_appeal_status
  kwargs: operation (required), auth_id, key, user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "auth_id": {
      "description": "Optional authorization ID to filter results.",
      "type": "string"
    },
    "key": {
      "description": "Optional exact evidence key (MR-489327, 72148, PA-2024-892741, or Johnson Sleep Study).",
      "type": "string"
    },
    "operation": {
      "description": "The prior authorization operation to perform.",
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
        "denial_appeal_status"
      ],
      "type": "string"
    },
    "user_input": {
      "description": "Optional natural-language request; an exact record key embedded here is matched automatically.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prior_authorization_agent.py` and embedded as the fenced Python below (sha256 dea92230903fbd44…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prior_authorization_agent.py` first:

```bash
python3 prior_authorization_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prior_authorization_agent.py   # or on stdin
python3 prior_authorization_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prior Authorization Agent — a template you are meant to mutate.

Manages prior authorization requests, checks clinical criteria against
payer rules, tracks authorization status, prepares appeal documentation,
and replays six demonstrated capability outcomes (keyed evidence lookups
with simulated write receipts — never live writes).

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works from anywhere):
       CRM  — the Static Dynamics 365 tenant (Aster Lane Office Systems):
              https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
              A Dynamics case for the healthcare account Riverbend
              Medical Group is reinterpreted as an authorization
              work-queue item — e.g. CAS-260124 "Prior authorization
              request pending beyond SLA".
       FHIR — the Static FHIR R4 server (Riverbend Medical Group):
              https://kody-w.github.io/static-fhir/fhir/
              The denied preauthorization Claim RMG-CLM-260108 (the
              $1,875 Cardiac MRI) and the cancelled Appointment it
              references.
     Try: perform(operation="auth_request")
     — one briefing joins the denied FHIR preauth Claim, the cancelled
     FHIR Appointment it deferred, and the CRM case CAS-260124 that
     tracks the same SLA breach: three systems in one output.
  2. No network? Everything falls back to the embedded demo layer below
     (AUTH_REQUESTS / CLINICAL_CRITERIA / CAPABILITIES) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PRIOR_AUTHORIZATION_DATA_URL (CRM side) to any OData-shaped endpoint
     and PRIOR_AUTHORIZATION_FHIR_URL (clinical side) to any FHIR R4
     searchset-bundle host — or replace _fetch_collection() /
     _fetch_fhir_bundle() with an X12 278 or payer-API client. Fields the
     rest of the file needs are listed in _normalize_live_auth() — CPT
     code and auth number render as "n/a — enrichment seam" until you
     wire a payer system.

OPERATIONS
  auth_request | clinical_criteria_check | status_tracking
  | appeal_preparation | authorization_verification | payer_requirement
  | authorization_submission | approval_prediction | authorization_tracking
  | denial_appeal_status
  kwargs: operation (required), auth_id, key, user_input
"""

import sys
import os
import re
import json
import urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/prior_authorization",
    "version": "1.3.0",
    "display_name": "Prior Authorization Agent",
    "description": "Tracks prior-auth requests and appeals, joining a live simulated FHIR server (denied preauth claim) with the Dynamics 365 CRM case; offline fallback.",
    "author": "AIBAST",
    "tags": ["prior-auth", "authorization", "payer", "clinical-criteria", "appeals", "healthcare"],
    "category": "healthcare",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# LIVE DATA SEAM — swap this for your real systems
#
# Two live sources, both synthetic and hosted on GitHub Pages:
#   CRM  (OData-shaped Dynamics 365, Aster Lane Office Systems):
#     export PRIOR_AUTHORIZATION_DATA_URL=https://your-org/api/data/v9.2
#   FHIR (R4 searchset bundles, Riverbend Medical Group):
#     export PRIOR_AUTHORIZATION_FHIR_URL=https://your-fhir-host/fhir
# or replace _fetch_collection() / _fetch_fhir_bundle() with your
# payer-portal client. Downstream code only needs the fields from
# _normalize_live_auth() and _live_preauth_story().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "PRIOR_AUTHORIZATION_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
FHIR_SOURCE_URL = os.environ.get(
    "PRIOR_AUTHORIZATION_FHIR_URL",
    "https://kody-w.github.io/static-fhir/fhir",
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


def _fetch_fhir_bundle(resource, timeout=6):
    """Sibling helper for the FHIR side: one bounded GET per resource
    type per process (cached by full URL). Returns the list of entry
    resources from the R4 searchset Bundle; [] on ANY failure."""
    url = f"{FHIR_SOURCE_URL}/{resource}.json"
    if url in _LIVE_CACHE:
        return _LIVE_CACHE[url]
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "rapp-agent-template/1.0"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            bundle = json.loads(resp.read().decode("utf-8"))
        rows = [e.get("resource", {}) for e in bundle.get("entry", [])]
    except Exception:
        rows = []
    _LIVE_CACHE[url] = rows
    return rows


_LIVE_STATE = {0: "pending_review", 1: "approved", 2: "cancelled"}


def _normalize_live_auth(row):
    """Project a Dynamics case onto the auth-request row this agent renders.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not available from the CRM-side record
    alone' and the renderer labels it as an enrichment seam (wire your
    payer portal or X12 278 clearinghouse there)."""
    return {
        "id": row.get("ticketnumber", "?"),
        "patient": row.get("primarycontactidname") or "Unknown",
        "procedure": row.get("title", "untitled request"),
        "cpt": None,          # enrichment seam — wire your coding system
        "payer": row.get("customeridname", "Unknown"),
        "status": _LIVE_STATE.get(row.get("statecode"), "pending_review"),
        "submitted": str(row.get("createdon", ""))[:10],
        "decision": str(row.get("resolvedon") or "")[:10] or "Pending",
        "auth_number": None,  # enrichment seam — assigned by the payer
        "_live": True,
    }


def _live_auth_queue():
    """Riverbend Medical Group cases from the live tenant, reinterpreted as
    the authorization work queue; [] when offline."""
    rows = _fetch_collection("incidents")
    return [
        _normalize_live_auth(r) for r in rows
        if r.get("customeridname") == "Riverbend Medical Group"
    ]


def _live_preauth_story():
    """The cross-system denial story joined on the shared Riverbend
    Medical Group world: the FHIR preauthorization Claim (denied,
    cancelled), the cancelled FHIR Appointment the claim references,
    and the CRM case tracking the same prior-auth SLA breach.
    None when the FHIR feed is unreachable."""
    claims = _fetch_fhir_bundle("Claim")
    claim = next((c for c in claims if c.get("use") == "preauthorization"), None)
    if not claim:
        return None
    seam = "n/a — enrichment seam"
    item = (claim.get("item") or [{}])[0]
    coding = (item.get("productOrService", {}).get("coding") or [{}])[0]
    outcome = next(
        (e.get("valueCode") for e in claim.get("extension", [])
         if str(e.get("url", "")).endswith("adjudication-outcome")),
        seam,
    )
    note = next(
        (s.get("valueString") for s in claim.get("supportingInfo", [])
         if s.get("valueString")),
        seam,
    )
    appt_ref = next(
        (s.get("valueReference", {}).get("reference", "")
         for s in claim.get("supportingInfo", [])
         if s.get("valueReference", {}).get("reference", "").startswith("Appointment/")),
        "",
    )
    appointment = None
    if appt_ref:
        appt_id = appt_ref.split("/", 1)[1]
        raw = next(
            (a for a in _fetch_fhir_bundle("Appointment") if a.get("id") == appt_id),
            None,
        )
        if raw:
            appointment = {
                "id": raw.get("id", "?"),
                "description": raw.get("description", "untitled"),
                "status": raw.get("status", "?"),
                "start": str(raw.get("start", ""))[:16].replace("T", " "),
                "participants": "; ".join(
                    p.get("actor", {}).get("display", "?")
                    for p in raw.get("participant", [])
                ) or "none listed",
            }
    crm_case = next(
        (c for c in _live_auth_queue()
         if "prior authorization" in c["procedure"].lower()),
        None,
    )
    return {
        "claim": {
            "claim_number": (claim.get("identifier") or [{}])[0].get(
                "value", claim.get("id", "?")
            ),
            "use": claim.get("use", "?"),
            "patient": claim.get("patient", {}).get("display", "Unknown"),
            "service": coding.get("display", "unspecified service"),
            "serviced": item.get("servicedDate", "n/a"),
            "total": float(claim.get("total", {}).get("value") or 0.0),
            "currency": claim.get("total", {}).get("currency", "USD"),
            "status": claim.get("status", "?"),
            "outcome": outcome,
            "insurer": claim.get("insurer", {}).get("display", "Unknown"),
            "note": note,
        },
        "appointment": appointment,
        "crm_case": crm_case,
    }


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
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
        live = _live_auth_queue()
        if live:
            seam = "n/a — enrichment seam"
            lines += [
                "",
                "## Live Tenant Authorization Queue (Dynamics cases — Riverbend Medical Group)",
                "",
                "| ID | Patient | Request | CPT | Account | Status | Submitted | Decision | Auth # |",
                "|----|---------|---------|-----|---------|--------|-----------|----------|--------|",
            ]
            for r in live:
                lines.append(
                    f"| {r['id']} | {r['patient']} | {r['procedure']} | {r['cpt'] or seam} "
                    f"| {r['payer']} | {r['status'].upper()} | {r['submitted']} "
                    f"| {r['decision']} | {r['auth_number'] or seam} |"
                )
        else:
            lines += ["", "_Live tenant unreachable — showing embedded demo requests only._"]
        story = _live_preauth_story()
        if story:
            claim = story["claim"]
            lines += [
                "",
                "## Live Denial Briefing — FHIR Claim + FHIR Appointment + CRM Case",
                "",
                "One prior-auth denial, three live systems, joined on the shared "
                "Riverbend Medical Group world:",
                "",
                f"**FHIR Claim {claim['claim_number']}** (use: {claim['use']})",
                f"- Patient: {claim['patient']}",
                f"- Service: {claim['service']} (serviced {claim['serviced']})",
                f"- Total: ${claim['total']:,.2f} {claim['currency']}",
                f"- Status: {claim['status']} | Adjudication outcome: {claim['outcome']}",
                f"- Insurer: {claim['insurer']}",
                f"- Denial note: {claim['note']}",
            ]
            appt = story.get("appointment")
            if appt:
                lines += [
                    "",
                    f"**FHIR Appointment {appt['id'][:8]}** (referenced by the claim)",
                    f"- Description: {appt['description']}",
                    f"- Status: {appt['status']} | Was scheduled: {appt['start']} UTC",
                    f"- Participants: {appt['participants']}",
                ]
            else:
                lines += ["", "**FHIR Appointment:** linked appointment unresolvable — n/a"]
            case = story.get("crm_case")
            if case:
                lines += [
                    "",
                    f"**CRM Case {case['id']}** (Dynamics 365 — account: {case['payer']})",
                    f"- Title: {case['procedure']}",
                    f"- Status: {case['status'].upper()} | Opened: {case['submitted']} "
                    f"| Contact: {case['patient']}",
                ]
            else:
                lines += ["", "**CRM Case:** no matching prior-auth case reachable — n/a"]
            lines += [
                "",
                "_Join: the cancelled preauthorization Claim references the deferred "
                "Cardiac MRI Appointment; the CRM case tracks the same prior-auth "
                "SLA breach for the same provider group._",
            ]
        else:
            lines += ["", "_Live FHIR server unreachable — denial briefing unavailable offline._"]
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
    print("=" * 60)
    print("EMBEDDED DEMO + LIVE CRM AUTH QUEUE + LIVE FHIR DENIAL STORY")
    print("(sibling-live demo: the FHIR preauth Claim, its cancelled")
    print("Appointment, and CRM case CAS-260124 join in one briefing;")
    print("both feeds fetched over HTTP and fall back offline)")
    print("=" * 60)
    print(agent.perform(operation="auth_request"))
    legacy_ops = ["clinical_criteria_check", "status_tracking", "appeal_preparation"]
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/5S4h47kyLIl+CuJmgGm72N3UwRFsAdvdykjGNQySE4P+lIGtdZ33r8vI6taXYXdRKGQSbqbm5sdO3aMf/sSzFPWDl9++kIJNGVaX77/EidjNOTdlLfN+dgagqgcP7ohb4cf3os/hqSfk3EaP4Im/gi6Lgmq8fuPos2bvHl9BB9VviQfY17PVTAl8Qd/F4yPMRmWZPj4Lk6a/HzWDcmnqagK8vovH2t+/j5lyQe7N0GdR+PHBcc+GEP+iIIx+Z8fbZpWeZN8pEFVhac7P55eJltQd1Uyfvnpf/3v77/k5+9ffvrbl9PgeD76or3dpT6vlh/B+yrUK2mmc18VNK9zQbef75rz7y4Z0naoz0dxkn58++u7ManS7z/+4z/KNRhe418+fvi/PsZp+Onn5uPbT9t9/OfH17c/vpLpu5+/tOfez5N+/vL9x8+fcf3lW6h+/vKX33fm6efm//yHNX+w/v4Zkmkemo+3Jz/+8seV3/3BWFL9wVx0BimPguqXM31TMuTBL1GWROW/t/wvNv3LQ8YpmObxl+kNizPf/9743y3+l0a/ouiXExZd8GsQ/204/mH9PzOdNx8MpVG0IAmWwJn/zuAwN79EQReEeZVP+3d/Xvk139//48P5hPUvedPN03/+CQq/P/+KhTP//2R3mex/3nY++Ffr/3C7b36nP3/5j//ghqEdfvqP//iwm7Jp1+bjNxB+/PVvbfdff/3x5y9f/ussj+ZE7xy9X7yr47/9tw85j4Z2bNPpw4zaefo4AzDldfJz83NjZfn4cf57F+SQnGU75mGVfFvXDW2RfBo6q/Ljr/9PkIfBOP0QvKtr/KHKwyEYdvCTLX4J/lh/f/3xwzoNnn+/8iaoPgxK035uPve9DztT+ckR8Ue4T8kPZxH+8P7lncO//hNrv3xu/LHb//rJQueqt7cGI5yM0Y1zlfz4vskzS5pvfkdB85FsSTSfNqv2xPtHmp/s8f15w7GtTsKa3rcey7yqPuJ8OK/YDvun7TMyP72N/fWvfz2vmv3cfKWOy8dXlhzBN3Z+defjhx/Om5xs9cqmn5skytqP//G3//ofH//n49/t+jT+PkM72etb3E8PH6aqfJz4mOt3cD/eSUyC+DPuf/uvb/E8zTQnsZ5ZytM8+br5rOgyiX8NrnmnfkAw/CNMzqCeAa27dpjeTJ1PP34I6cdv/p6Hvl+dvP6RteP0ESdd0pyEHe2n1eC8zm+RbNrpYzzzMKb79+8i+Dz1r2fqP12sTwYJpr9+yIz2MbVtdf73dvNz0bm5/aSb31L/9fm7Yv7H+EH/auLHD+WNvI93eXfZEHw7Iw2+5qUdPn7dfhoPPppk/bl594DkHapPhHwNz7nojEz0LaU/vHP+EbV1fSZ2/PXszzWfrcpqTywnw8/N+A3iwfBORdSeruwfrzmPgyY6+9HXQIxZO1efvSw9PX1b+paF+FtWPjH42Yk+/tSKPj570cfPMwLB6On9ed/u3Ss/9nb+PLJOgvP9ebN6Pi/zFcty8I7Yt0b88adi+K0jf//xyd3jx6+k/vErqZ/h+ozsid5gP70d5k/wT1+b+5+tfSXt7z++sut55Fe2/YjbaP4tvCc/fRZHcnq+n4WTbyde6vbNM5+h/J1MP85YnSE/7Xx3Etz5KlnyN6reddiWczf+3Hz2/98Vw/p2+h335F0pv8ap+QTEp7j4XDD+5TMud/X5Yd0F88PiZE2iLO7jqRqi+eZL+McP9czTWS/v5ITtdkL+o5uravxq5p3Z4cTBO71fK+5uWdpHOrT1h/VUv1Huq2rDU3fsn0Vxeve7n+P+hup5r3FvzhOmN86CKfj+o2nPwCfnJaf8rY2+GVrb4Yz1p/Wg2dcsGZK//N6T3mrn16u+3TXfcY7+rIimpHkD4zvqjdIPKTglkZqm+RlK86srf/np79tMNk3d+BMIlm28/7D++DojPYc/5i04ftr/If5m/4fTPhh0Ofi+AbiQPyLg35uifnfmLcs+Tjr59DQ7Izdl0Ru4QXRWxumhcYZ3CE/2+HsbchJ/4vI2tHP35v0hOUs4GU6svSMavEXln+H49xbeUfzhhPt8Utl55V9Dlvz4+vHs9uYPCA7BCHo2Ue0fC+XvbX2rm483z70ZMUz29gS1KVE/f/nxt8WfAvYfM/P52EB/k7a/3fnPl/z/n5I0ywfw87+/3/lmtD8r6N+rlnlL6Q9Dvv3ASPJnFKDrx3env39v5L/D31+JU10HQ5wH0YdsCH/57HPf6DlKquq0T3XdKein+pNkp38M3El57xoefw2TNew//aaef1Mh//mvdPC3cLYngsMhT9J39N8TxNcG9u2OnxH+dVT4vN/3f/bym7HPdX92+DRxenjW4Pe/3e3XceKPKPna1z6NfKPC98oxqJM3CE7XkiDKfjofDknyW7mfbePt90lrp8D7vD9ytqv2JKjpDc7/+4N7t4tTT5x3ek8s48d7ZnnT+dt4UodJHJ+3e9PlR/XJxmFStes3P76jbOv+i8HpNmda5gf4wUiCIjCU9AtjCBZnCNT72R9k7V/+iM2vXfGTKr/Zi87mmZ3k+22G+vT38uOHHJTvAnq3nOEsuulztyQ43AdLWdSHyVHyV7d+OgH+a4w0Q1CNX94OqobgU5agKr+8l/9iG9LHd+8Ajye1/+V91ZPhPlT25JIfxizo3qzfxJ8J+mbqnZV/Zu6dy6/mfuthf7L5req+WRmTYIiy08EfwrmJz97+KVx+BdfwtT2d9PhLmkxR9kvUnqiJvo4LH79W17d374L75auV775NpCcVuTDygRDXt63PxvkDpQnv7vrWbR98nlTxJ2S+mRreZPKt3XxKjSZJzgVvZqzyz+ZxYueX5iyRoMqP5Jd3F/rUtd/9lkRGs35NXBsnX0fsN/yb+cTN+0KnIhvePPnzlwYMfmO/5hQ52Sf2z5DUP3/5eMv56p3dX5tP/qbnr5f4huTP9qlqnPEZ+c+O+cdiPTXrv5gNzzd/PwWee//Pxz9OZe+Hf5LtXxVS9OvLT3c+Dzzde7v/zdCf9oxzWOfj+M1cd04gy9dTTpb9p4f82as3mZzrvzn31fH3m6+j109/GJm+++ZI/Jfvv0YiP+nj1Czf/2HQe39BOBvuqRC//NScUuL7L2dLTP7tF4d3MOqzvQ3j+wvF6f554JQnn399O+b9658/u6ifv5zo/zPLC+y7EE5sTZ9gOCedaXx/DZn27u3Eqb7Oe78nvtPtf2M02U4h/bsQOxd/fCcbP6BX8oIQ338QCIxev//QzsEBQtAfriRCoPD37yJ4tFkznn6YVZJ0Zyec4/0v//T836L6j168u9g/U7G/J+K84rdW8vml58T+l5/+1586yfn4X4DzfPN34Dyf/CMy3w//JTI/k/Z3yPyHDb/D8usBfw/Lf9jwB3/+GSa//O9/EsY/AO9fZ7M5tw9B9cP709Z8doBfdc3//Pgcet+p/ip1PxP9WwN6C9C3BKuDk/+ST55p67cCeavdf5LU051fC+Sdjt8z/Lvjbfj+OPB2/D3QfP2u9rcvJ/iDt6z8Bv9v3w/O5UMw/DC+ZykQ/hE6Dzz//joTn+/+v39Z+Lbx7DPnmPv5HS8gEeQCkdAlDWMUxTAiDQgywC9hDEHXII5T9BrhlxgnkAsJXUkohcI0vIYkmcAEQb4RdHbFKPnlPSnmb2cgmERxNAkuCHZByBCLE5wM0SDFSZLAyRSDMThBEBj5feuZ6PjbDb/e6B2+3z5yfJb+14v+7UuIo+fKOzoK1NcfBgRgMjidVx/hKwavIqsopDCUJWBwTeQbG7nnSD8Lswr7Yd8PM+lm9sQZ/sAzZd1beU+L6XiQmQYcwJqWVbJdKUajst2rBx/oIzxGuidjrJHeRMqOznc59fHRAXhhUYUOvo0pMNRgZ4hsf3G7XATBIwXhBBUWp75eaUULbzI/iopm3Q/3nvtGLSKmymMBsgwX6hI/96sRrVL17Omc2K6SBNVWlmXKEt8JQ1gZDTTuYU7fRp/Ex+QqkmQIr7sV18MkSVu4CQvzio2eQJT2Vo0MxVxeWEFAWEuJC3aRNV1ACugp3EReHbbOC4uaj9Z77+eyBYpymEiCQHsjjUhcOF+ky0YdZJzXuVH0gv8Sa5LEwnVflldBwCsmlKcCRxdsbJ6NT6pU9Bg5h3XVq+4JwvWaYmitsEBGrvzKLqt2H0gFL6g03EmAa9VLd4E2/EFcjqJnh6Xo0EUiwM7Tkx3eRjvjFfrewbR8gew06xARYASR83R2FGm0EUqxlV0iQK6312P3N4VW2WZHKWo5FqXN5gtDe3ld2wLf+q+xNO/j8UqwR8VQagmWuXyJjSlnGQZPwxcKSynrC7eVqCWvy7LXjNx2Yu74ywIrw9VEl2J3FcoV+gfZKLWh8vWNGNf0kUh+DsQUv99NPYBY/RrmBwWRkXXzAZYm0sjLX7sLKtDFSmIpQdwyLfxUmUlvslQi72bnrq41HaJoBTABdbncG/BF5MuiZc5zAh9r0pU4t0fZCReBHTn52h38C7+bN2fuFWOi2KtU8wG6jctdjanmPhXtKC1o/dr4C8qMAHK/Mg71LHJLmuhnwCsp+2JVN1PaBLjTt6Y96nxe4ng0NwwGIhDkiYkAXi6NGx4hvPz7VUgCqs3AJM+m5abfMXK84lY5wmAaTvjTAaSk8DHvRD+ddV0QgBCI7/QOMr463FXQTF05ogsK4jBZK1f68NN7Gc0aJrsPDISPFVDxRLsckK1EFEIDspagF7a6gvxozFrqRuWRkxq+ij4fkgNGSQ2t3yjiejRcsPJyYcjh8wY8SqaBWNOADlWoEMRbjKz1+EBCKZLBo4xmhXiPOwifrjZWCLQeIlJaA/QIrgL7sMwryJqBs1QkyJfKjZinkHNGjeIYj/JleGLSjN048lbrBtvBmBk/GC9SuEtao77Aeh1K1EOYecmG1d2FLCXqFllO2mmFD+yXTXpJfrkLBlhVkJfULm7oYKCKuSSV9M7kGRd6lxm83zzwBVWCkAt0RaCra9yfioGD65qw85XQCDhDMBCiI+LE4kgqly461XFy3zB1zpKmCddnkLqJq+Bx0aJEGg519oihTCgpo3mK98ASvcIKWIEWkmvWjWSAThtZ7DsD5PJtKPuOIJuugOENyirIkMBQfSYcUrJyVGN4hUduBSkckUg7eSdhuo9cAg29ZClYzK9bNFxrQRwGQIBe82jxjJ2LfvGAsb3g1+M2MZDGTGbOZvkiQJLBjCUtgrXwOofXW7tXL5jY/EzVKOHaSDBtHt3rtinYhuLPE+ucQz1ytVydLjaZwBwwZspeK33p+J0y78dEwOSYgjvH3Qy63pCkT9rHk9+fwCO8rMvNYIywXFZrsNBaqykzyfCrgZYuIOrKi89vQsowNzAHk1KzxVIusaxfkAu/CErU35oRUm2rQ3WxpdlrdZdlUND2KJLjqjTCG1hnokLhh3yXOYa3wVV+2uZo3L1o9kxU4Fm3MHCYMDVRM+WjMlLFu6085VOcurMqpfRglMm6p8sXi5RY91qyNmBiizaVVEwtF6y9F7YJifz20mzufrt5F+fBF9GhQWU5aeW1KIj1HG9x85qsEffwqQiqgnaFl3sGYtfgYjpTK5hGz7XTtkS3AxUUiOLnQjC814TGAKPtV8yjjGl2Nay6RejL7LVdIx1g787jH/odFJYt3jjtdZGsenmSzKG4qRXoI1efsJti6KarVCOqRo+PqVdA/JEs/SXBtNdCuBknV50qrmxf4gOWFKC4jEuUDLBkCc9wOrj7ipw1Yu8hSBlPDw6f8MKi0aqAevVSjF0UwNuDkZ2H93CaYZKf1mu1YNya1cs8uV4ycXqyrUMKYku76nKrlLl/9YDjtm/ILnnps+3PUUHD0XLKsAG0x9dRIByh09na7V3wHNTL6wGp+rWKqJsk0h3GBFtuPera5Vsg4oItrXgkmXfWT3xvN9hKEJHYjFcqeT1F3dRr8xKaea3CUG+X1XbvY8yctYcsPPoYOpIYLCnSIi8h/cAS1WiCWeix3JDVUzsAbZxvfZwb9aJeUB/wrcSJ9uNGweERijyR47I/AKmXMlsy4ci9T1A9rZX8MPRMcyjtwcuNzhzXVz/FODBxAjVd5gRcHyAa2GOt6jfksbKbhRja0YDgCC4kCLJg0ZA0KSKzpTa63L2YWsRON0zQozr6uZK6ibMJmptPa01aA4BKhJPaFiExbu2ckYI1JG4ILL4IrySp4wlnCAXo+kqCLmKAZg521lm5FImBSJhjDrjJ1z5Au4oo4fDhlowhb6eEmZ5ildJ9xgH91HuuNzPQPCJMn2H18Vp8pWWqu4MnqCsaLUW9XBtG2xsw8Jb7ILlY7fqXyDe0kd/QINjz51O1lDLqmIzqYVafBQvQx5cAsSwdstYhXY4lDrcbTTIkMLPHXC48nHGtuAlUaiD3AS6nQaKqJ+QHplCBs6WLHJCFxu7HWVtmow3tkAnZLIvd4eyaxCgRx46AtsdIH6J4ZwiOXPV092kgBCF96Q70rkQCD7BSjgZKB8Ib8mJ2c5cW3TroXufsSnLvQ/durhjQBp0tNZf4+thlC36tjhci1n3ssC5/KJfUoHqiKq6dC27F7JgPGioJCy89hT8K8c0LC3PNzz50y1m/A/w5oDb07IfztcPdJ7A5hA4h4JXFxhyJ+d4Fb6ASvdbm6KMojC9LekLgQqR6/BCkroKzY3UG5WhwTNv1VqmU2xjsFjacwotnMYsY3OmEtF0Inv4CV92ToXSQqpIAnucvt85KL/dQRoHX/LJJXuInGhNw6zZ4dK6i3u0Ojq1ldqo3QVCxciq6CjB1s2KdD3g4cKCUA4phw842ArGXHZK9qwx6fTPfJLw90YwcwjNvsJC8NaJ+ZfSJp7okDcl6ZZS2L12BqXuGQkJDpdspLo1ju63UWJfjYyMeGcL2a6jKoQk8veEhvF7ccBdIAUG54kD1uUzWeOHNtK3syjjatQyeR1OxF1DAvfXC810PeZaTBS1LRbnAMtxKV4BZqRRPaALFt1rlQhYOBdYe1fcr8ew84DqGtsvQVgFU4WHiOiCmhNrd9AzUxKtUKpJlHatmu/LKzTrrwtF1AShVRQWJvnjOoxopPDooAIjXlCUI9+G/vAuULexxgaAEdrld4fKlPNJ1p3wItHKcTl/GQpWEltX8mVe28TuxioJ5EMldRD0VuO6nps98DPC9lxWv/nmIDZ92SYwUX2Znlt0plCk1la98Gt+tSybZq0tR1kHFNrSStLVLJZU3rWd42kirckC+TNeVKL8+mzfmUgHEeGioS0CjFsUNv0nre354vfTCoDfosO3IEGCGvRmwYOTq6T7BQBmT2eSNSilIkluImq6BgebkPPvZHIipwnIomOUohQT6rhc2eR8XzHwJagGD8dz7IxWnYvr0G1e/X0WsRh9hDsuSDNTaLiezUIDn9MGinExSGxVQ1A1V9DGKZQo3JnqXe1H3gDi0TtLrA5R4oZiHyCuG2o9X41ry1UI6tE3I6pAlsjBN/JzVuLMpEMqqVgVIj/4198S7ylDpy2vs+1Wh4VG3j9HTomzLVltEd7RLmIhik+NUUoLgU/LVP0WoLz+cBAEvyPwS5FF1rYFwWMThrgKHX+eVuDxcgCi4HCt7XTMv7tMmB8A1cTOR0qzf5vJGd2TxEDZZpryNWjQao65EUxP5fWJJfad7cg2FQmJ1mJcybBlZXbxt6ij2+rozgn+j2qdCo934nnGAjhpuHsu3PP8ktW1NlhsR8Fw2ttUKHx2xQ66b746HWeKz6cSHkbtllcV3Gnn0dfV6iMAURAem39s6sqac5+IHVOt9dUp+PYHahyzPsuC6HYLKC7BPwn2kPS1gIms8bLNH1JtuZ2QcmmCGh+1JHixMDWvFTA1I61RH0OZg1jdIvlG3NhQAarP2h1d1fZE23LrTq5B52WSr2KAkqc1S7XoKlbvWMXO6y/h2Q4cMtJ41zPXHwTi+p0MnwZG6k4lbdLYzu2U2BpwLUbL5WAdRAc5kBPFFKs5wRNYKuXVVtGCVlZVkj7kTHDVrHZTCCIjUJ5ED9muS7ZvZPO7o1W4XryDc5aAdMuAfvN+760MgMnO4xXcUPg6WZ6815Re+qPsAJJcSt+Kk6CqxrA+ivJY3luY68Eo5dzNpk+esqiBWyX6YEYHP0XxX6i+4yZrr5j2KhitXiyIV4LYol1NWPNiT9GQ7nZgXrK5QZWcN9ehot33xiP3KcW/gws5ebvxs4Ns1pjeW2YHbTCpZPdPPdrJmvb0pAOk1wIjOHuhYd8CGrKc89F4mXDAcbYGscQfXnAOaRYux5Sp/IXviyAp+MRf5fkUy86Jl5UAa63QS9sCeVOmXNcsfQ2RmYbPcOjqW7pRu4wAeh8kldMG1m2BkkMzLxXoB0YRf5ccTvF0utnsl+EzqngwkBSKRI6lDYWJ+Sm2mly1NMetdWIaqMMPgilJ3dDLtu9ZiAnidvQnnz9EAvkrZ4ceMfTzKxHytd1zzOk7EQpPbpBkRzQNtumDUlTZUbQILDEt86JXuLbzqnZ171Y9zhoEUU1+dWvENCoqYDZBP4agre87XC8st6K04WHUH5jrcbchByLVem7RNsCmp5TsSI01gB6I6Va9uNKrq0F7N+nzQjj2ajD3YT5XiXsY0wjMgMjL+2i5rnU/3zrP0tvKPUR9iJwv7oWM26OkdMg81M/sskS6idMtXeNXCZ+5Rq7bAsMbePuXgpV9vixm+UDytG02WUFhBnboBYngmEisvDG/LT680k7oJYetZ0Ckt0jbNU0funHNaby9G98Sby+U+gtY5J3vb/EqWfI1t0WHv7NoAh7KcM+ztLuJh1NnQ9rQXoRR263psgPoIWOKUoHRAgptCAmaZ7A91niMXPYuPBPCqV52LAMyapu7PxttzEiW2KFVe8SXV0GZnS387FALlhePqgLZNQWMNX57krOyGgmn67Qgv8cXTGkfH8QjwFXvhSfxeey1nZSxOaZG9GRVjwKEaX80bupD3ASNUF2iWaiek+eL5FnqynUrCOEIu/jmx6WjE0Guxo0xrIQoYG9otlyg9BtmW8YRzoqT8rSvMnRUDLoUfN/xhzXkzzC86XkOkI0SJIFY6y7Q7zlAPYJDBLYSaQkCS9WXyXEBX8WuKkEWaSZPgYph/4W0o+2ew3OCR+xfyAkLOQcLVQWCVxefeKtQ8TxOogIlsoF3S5C6BnYI0MLteNXKJkSPwXjZ4bBzjrc9pU2X0tUQZY2BrPpyQVepXC1u3x4smbl5xdMfqbeYNQEzTsh9ElZjozeZMSstedyzQL+PC7lNn4e7t5SAKl1zpbal6YvPsi9i55URka6qR5iQSl/vFP8ceOz72SuM0l90WxqbGEJqm9FQjNmg2SIjHnRjx5xRnQDtS9FKUa0ubGNkL6fCmxJzkyQ7TKbX9efGtWxrkg3iqczvaa4sfregKCLVNS4C4vVxUDjeEi44HBkgD98AvQy42HT5xdUUVCsmjATmjGoKXfYjEG6/zNqTYj5s4gVgU82xiSNSaR8RNpFkLHGfSJ8YBU3IJnoiEKaobzYg12GzsXLR3kCRgqrgJulQ2nW/xpT94FFLfe9uvlLtHr2CLAvgwZb2JANuLCW8AT7HnTFVbmOIWYRBi+BQCxIRyQoI92d6r9ONqncNomQ1nA6WTJVMCGTOu3Mbmjo1XpYMasM1N+IPZx/IyQXNV4Wg1H0hP2q0lCGEOopGkB5UZJwOUIuQLTh1MS6+tZke9eh3nWS6dzWjA95SmYpnqVNv1Th3t1F3u1cw0MduGzkor5zvZAletLQl3bQvXl/KYMywMp3wfnf2Euc+aSpJC07Ny3zI4oXpn41SUI5DCsxJ72/Kfnu3c4gddiuKQ7R6tTU7nP/Qe7saZI6X8UsaXrrbXMPKwFDn1QyZEnVJer6pZQEWDQhiHogwJD0VVSVknmiZbgFqEjRjaYUPMGCVKKHNdTKdmjbGZcVgeNXIbTefxZur8QzKENFPT7pCQquM8jn2hZPNimcXNdY1e5GJ2g1R6xW22LNtQ+CxmAptyvzxHciLR2Iq0m3w0FKAXDRRM16d7OyqHV83p8eByvYGryKwE2QeuGXa9r4f3kE6kNQTYWD23UiC+k+W1ePrPGYLdQRDH5WUqTV1PnlYscKaBYoeC6Wr1Yrow1KvXdHPQnss0mKpbtTbUh7Jil+dMlgMvqVeNEL4mZANzvHKCRIZpEroapVS/iGsi+0Ts5rLeae7dWsEwkSLGUkz3ehNzor6k3b3FzXuLDexeQiYqQj6N75ECJI3O6/cZJU/x0LBZ/UJ9svcCFrqlFrwQAZ4NV61RHZ4zyhZO7cbycde47s4eCJdn0DOhnAXWKsFKdp+tXX12vKakHWAjNj/hvuYGfGbz/jnbtKn1kmBSU8777UlYvZ5lSVrMTZkPKOkiV0PFLlZKPxYgHV7PyXvZPEvqoBfEGtjzxo6xIpIO1RArYG16fmC1ZfHgElAxKwW6QszPK6sixeToHKHyFnUdMJ9L9uF17CoAO69TGcc9eADbCtfpdJZX6CCBnfjyBN7lmB5rGuLJhZNHeWfX4nDV3A1j8mKcBDoXj+opiAlr+pqZ5gX70tQQKTrWyc7+1eoX/0HdKFn0ZDkLbQmxRUGGao3qdPeSP+nLFfM0QYEmMdN6wXQWH3w9GXsumVjJUIz0JDw4Rx1oNV+3UttTuajq3u9WgY4ukAxRQJgoUqPoFKtjZFIAhS4IkPAqUttfsQBnkMrttFrQmP0FIQ+kq7an2d5NlL4lzt46QwgzfjbFTh5wMx8WGzQp7bXyu81OrUKupgJDoTuyBqzFSWp0chKocBw0SFAr8Mi6rTN5GETNmFqnXNE1asV4pqFbFefwIxNx2i4x0o5Rr0NRPPaL53SjzWJhsDOzgkJV0s2kFPml+oZySCdrtJWKpNetzAM11V5PHE0b+gXVlajQCA3fHWwsXnwt+/dZNMHWexJsF+bs/cL6zcpJy4xAYyBG2ksnbXyn9YKgnlwFto8EmtA1A2UVp4OSv1PCI28VQsj1q8GbY+kdhwqITfUI2ZIzKqdh5fjJZ/kJtRhCBMWM2LJ+uTfLpZX8ZjjxphYj7jWOIZeKc0MQ+mVVt0tfKPLd3x6VaaDPwV+30GyWI7gW0/bSpEum+VTUPcPs6h+WY2NlTU+aUCAChVnUw7s0XSslNHANfNuKTo1YvTh90rWLZebdnbOH3DBF3X5mjxmtAdFHkmOVp36TN3pqmPyU4r61XFaTTgIK3vx7meizxPOPR2vQDF1Ic72eff/sKQtoijZU7ep1uHMAOTK8Kk24cEkiAgBHIsHJRGPARYwUf36kB3YjQe0oopRwGsNLpdAJoEC/btMtDIehgBWzDwZ8YaNr+rLX+5aLVG7d4tyT3ZY+0aSU4LrJM3HpGw+5kMhVO/j9qrgz4pC8xSnjyoSVmBZ2aShBoeF3edJZkSK9MBaycBEvonKFSpN+dEbmsDm/8ANGnvcFYlFYG4di96uVYIsKFYW9JflmTlwUAZCjDXI9XbCbP1GL7TieL7aDHYPWQ06KBx17WW56cZnLzBiwdjTzzGiWldXfF1KVlWHY1YsjD4yjzk4gK1diD1+L4xUhb69nqVrQ8gzgPan9PgltGWQv3T2Dg4EUrhuB0KeAuvSKR2hB54yYqHoKUYaqJh/kizUymO9WuGzojg9Zq3gVW+/7ikHcK7Qc2hdyLNHtEeVPsWP0Rb6KLuSzXjycdaoDj/DqKA/snKyJl7EblKp3ysO7a3vZ5TCteurKPWK5CB73azg2mYf0NA11oAcG95sI0cwduMQLt+/dMzkqJsGj20aJGZqVTZ/IB0ohBarca6Vedy9gAv5U/tswXTHN40EOcH2UnE7RKjjFgsvgA/ClUz6vvmY/kIdVXxMUuggUXsXyaBaPrRTJvi04fdultPJxqmw219cBSGoEStxNQNF7KzGMG+HNmMnlbYvcYpUzV0xn1XWJkJLFu5zPHiVU+BZnkjtDdxhK9Ji1N6FgetxjqSWXe6IbzHV556AlBZjJ4/K4myVmlA12yza1ufjPlwPqQ7Qh2rGxm0hKGaOZiXmHz+yBKrz39orftmKABKMIsEPWfcg49aDVjdhzP2oO2sxuF3jLWg2R9o+L7Mu6livaTYXzFWcmeZcYlHyC+25ShgDeKVvSxtxWApMW79bOGV7Vhd2NoA9dPIi5zEY9vZcLcz9KvrP47JS9JtejZ1YkWyXgVOSiCYsMw302c3iVvLlZ4ZSQXsRFWbyHCFigzE1tN5nFtj1UtsIpgS1HRw+Dc6YPrubxQKq3Z05DoKLbNn4sOkMp6oBKVYO8hFnwejT3S+GdCXzKnRtc9xHvxlcoqfDUKtxRFlpYneJDBTRJba1JoOxwvzz8qIQjiE8JnoPo3peOURA07ywImuPZLhpDWvMiKfRDV6hWGk9GxiEHKCyYotxqd4BV+vAuFO7yHpTZNCGMQJtWxmqo4g1AnzXwosLGkr0+V8RQvoBiC8/JYcra2bnE88zqZsDbhevMnrs+Qvs5oNJL21Et4NlzuAG0IuYlBHRc3pTA3PRBaxHAJzvblf3qgzZW/WDqiZjNJhOCeyW1XMxfGRdLCO6yabTVxhtEb7h238UdkR3o6doPwJQeNLVcyVyDO16AFbwsZRaSTcg4OCq2O+NpP429TibKJyBqdAeeo66tgFASvQZCae42UR6mMO/nyJAYwip56mYEr4v7qrO0vyPjI8ZkADbCOXcVyy0bB6OJu4teW7I6LA24OQPhKUUFR1wKhPlTA2X29ripcxXIe+La3c0YMUJwkbvRQAZOeMdVbKvRIwln3RB5G91UNpDyUab91Sf3q6uzD9sgiJ0hT1VHbtTDZBKvwDSYFhmLC15MJy4jxdsc/exfFhQ9r+5OlWXnD21hYkf8Iv3IySwPvdHSVjN+CgTHYN7Su/+sxgwqgUrBZL+4Kk5kKbvc7mbQaavTX1Z69/zg/UErqJUzrSAngbIB3Ndlcxtq5GIz47k95l3ZM1xRRJVzwqICY51FltEfnHHTmpeGqqCQpcU4QWlMqQxYu0TQpo/X5lzyiyAMxM2GTlKCDWLS1OHC0jf91QF9MRDkheMMX9/PnCY2aYbh2HalBEOLbgZMT14oZxEQhobIHFwS59ofrAjSci+PqxPeac/dW5slOGEj73GKws+Ssy9Bit+dW/Oitksf1QX4pHc7K3NgX0Lt0V5MF7T8Quw6BrVFWGBGlmSHMlYvB3TdTFssrpw7653lSyIAh1XZC7nTFYkK8LOXZCZkLbTds24yBVxfeh6JUGcSapUFmBvZAYZi7BSWDN4g5h0zO6XeuMyNXh6UET47weUImpfHynBmPDumHT1QZeKGLWZBpucr3zflRs8T6SHcm8OfHnNLLXck9rykoP1ohxTvWSxJkN8UfFLhIYCf5mH307zS6qO7Uuw9tBnbmh9UQQaLwauQmfkSlxa9djORTe4fFXNr6XqIzrzuZc1F6nWFJeiSw609+fxtJ/O4ZLL2JLPLxEC0kTPIQOJPnUkXAN5ZPl4yolir3txcy3taEkVezOVpkoqEIUaXcaGEHtVFBD3WaU6qBWhYzsR+rlQIo8iU29uxEtA4vsFZpXGrsqmS8oyeXTADEBvhvBeVszRdHLIg8FgUs3wxihAPsSPw0ZEXAIPFtYfsSR61jhe/g1PviBnpaY63DMwDL2NGDxiHtBUu85I/pce9nsnKsvWRhCNt1l91USJkpO4RPA6GFJZo3jb04zXkwx3g64JIY4547DHX6Iylbk/Gwh/cmfXcM89iDMkdfuwXMpXWYluGi096DwtLexeTpqgksWkm3eiIRrZ+eM/7bXUkBxOlXCt1qW/0TvZe48Vy5lBHQC1BziHu0NQawH3IE6vu0npMcEGUyUUSvzCtHJIEeiqdST3DCsGx2uAeEsu8uyGiODYLnvWQFzI61ABlylpV2PbhNexC/jn5yIKj1egE9nhqtnvbk1pfxZXYbd69h/sFfsLcM6o5bDsejft4VJu7OSA+TmHizE/16UTk65zX4gQc1RsK8oQ+GQ+LwM+4yixWVcrmiIvETXPZE1J2qWrQqPAp4SOqza9Lr/bo0GbZMq55Rjc33/Cp4cYXgUP6Xufd1GufrZB/LJg8oQ48LBaNM1xxXWufT3HFnp4qGx8PFXPvdDxn7hPHHaCr/MBGqtsGOYbYnOqRVlRydvs2z5KndnHx27XfecE9LDBbEOS4ta8qwl8MdXHaUShEZrBlP7g9+e4p9bE7PJ62h/t46hk9nTtBccvsagWG+ik2d9t04pFfZdKnHQwe1vUBunjf97l5VDYRiXVkJAyc53yxgFFqp+GiuZfklNrIFfAvIPAyB1URVkOJ8P2YEL1z+QmTz8lVvBsLV1ORmBJ0+hpiEYGk3DYjpN3Sy+OphDZCgU1Y8iIgza+nINw1SMsz7SwYVBofj4FYTEZJq02zHhl8Nhwa8uMMdaWyjWdSf57quGGI647h4xDsLSeFEvOaaY+iw80mKwJvqxJE9vWU4l7KIZTJlOyjGVzJiZNhVWc2waEMsEU8Z1V6XIt855D16ZzzH4hNDKcWVkwGF+Z5uEaR91HVy6A7e1f+6XEjzXVlE086coAQkGj4gjKiDtM+oomq46eNlcMaCA4LfI4c6x7CoKOtDNr2ie8F1Ut5SsACxtWI0ZbbRa6TPhdMN3qexa/gpXr4IWZfBiXdIPsKLeJz38eq8EnTGth7zN4qoJdFSS14CiZv1YuGkwCSYMbj54EWZslc2+4+hxzft/fosUluuub2Cr7qxIvWAjcXADi6ar3W8PPJdKn7zJP1tIoRTnYzhxVQZ9xLXnua8yA23oLO3iodnChVEHaC7mZvA9Eh76xnI7U1MYcHURwzhqhQeksYh/dp98U+x4eDFc7FJst11gt/rF7kMEtjj5OPhB6XORUH2YTzaccBzp2eq0lUlENVSgOx7U2m264btpqcGNiIONFsTS4QF+zFvPRgxXhcvQ+SK77crL+/HL6BCFK85xbR3hHwOrJ3l9dQ29deQTQsmeBCyjkxU+qYPDnx+lpx0eQUwKXr1ezdzODPaecOSul6f833Zbx6ZSI5Blmp/b6xVQeLB9dFQVQgGaiIzp3ZF5VsqUuY9ItF5Pg+IXTpesEIoeS9xnqkj7lnbmmb7KSdcc/FEm0q3ioMjcmGeGAjpWhHJ5njK+MuTA5EtzK474K4sjlne48kskKzuMQFRGZwpFIxl9aLsysXqhMnmYhhUI657ZyjsW6Y1/Zxh0UrM8NN9M+8RV2Rt+RI11MYUOnUSI50pDrvQwQMkVLFPQGGytjxATxFfS2e0Yq2SD06pZ89nkbFG0UmpI0bn5C8+UuNl6SSjq50yXTlnCg6iL4aF856Vvtm3peqND14aJxhMMqniJmhNJnDMx/iCAtOYT8/nwXU0MHhSJAdYvfj7J2OzKPH9TnBsf+6iCeJo73s5oeuBrvey9BTZWBWVqbhpo0UyZvOpvujm81zq1eQgwSHRYvqETISnPK2JIiiH7ivicoCssWkU21xbS6dU6AoJSHWgoQYm0cHdUkIIuc47peG0M5HBJ5D2hhNL1vKKza9mqJ7aM4+sMBRxsWwr2dRJ2SqhktaqL3BilYRCC/WrRrQTtG5wJv9geYqEYdmKAIFoO8zYwqaM45jeOoXIa9i7ADygMBKgK6otuGKG32DEMGiRA5qMjYUYu3sMXcdGxKBTUpmQEfUJmC6ePYyq4/OyHpEBVV5lobVEAtBlfGFOT4dMFjEcN+bk10paKMEZZH4sEfZHt2PhrdFNXSBNfAC32AADMebpeKkVzTEvdMjW876/oqlzi22R+0uO+aUgwGeDHUZhf2UPRMk7GY1mHY3VXM+ZBADfBrgYZP5NYLuh2lHutGCduTI4ytVFLMeT8rhYSnGLi1PJe6iYxdx3ovdjB/4Y2utgGggG5/yXVv2DQ0uAJOXzVW7ej3R81MJ30tUR9Ey7e4HjDAPoUSj/GhmY9kb0z1B/4D6AnNcK7tG4WtEKaU1Yzx2qCdBlhpBAJAKSu04g+Qzuelivd0OnVWILUYFvOW5fhnhto3ya+BDrCtjjYjREBAd3TOIyauz6LR7mdI03DZLfPLyUl3dsB6aCenp2ntsMQ5fSoWMH0b36M/kPW4VBPT+VhkXZNaIbCoSbJ4rIoS6uZvKovXQ5amHsq1CpaEtcAmpiHpt4Z1KsTw5cpqB2vFxW93rsnO003uRYzNTkQY2i9HugxkZ3uS8bqUfzoi0ojkdFlXlaxYhuMIs1OZNa/2wXXHCeE5GpMej3lDshmFU4EK97WweQcmwp5kD2is5PMb2HhEJPN+5eEsuU7hrEpKNFgg4MrSAAOYbHc73N31yotfzWZNVcoVwPogm92kfoIMLYztfB8ymkiQi/BBcQmiKryGxcAnbAE8hBFhQ6ydl8ppDDMu7ZyV4DBal3qrLYjPjcBE24jY6p4ZYbml0BN2i6fUzTjMPv+oWsBWrlwrxQ8DIyn+lQBvLlTZPJaO9LA1er5x/lXSc2UC4DkH/qvAAc5CJccS+FiWHDB4KWh6Mz2Vgd1C6H2jzE+KBbKMKbRfDE/stkLrTVQKrMUaia9KzjXhvLzWp4B3NvZ5uHCQVsHSxvkQGbQmnDAoQ0tUdap2pM1JrTLMd+gBxCr+0sHPpPOa6PlJkuMEQhYWKEF+jKmwQ/0kI5dklWYULIMXZVZ3ARVxogilUyrXJ7Lsdx2Sp+9FVnMTrvmZWFUMhZ1WkCuBLB17UAx1hFlfAmvJGLe9n9NS5YP1K9ZVTRVHUkg1I7jRIcyfmGiHbLHf3kxkVA1lvbjcfq6adCSay2brYsnABFSPzdZQi3sDTYjk3bA7Uo7+GT8oAni7TtZHpkeOiGFWiWb1ZYXSsQW3BZNZ1ArmlSOnjymstvFwBaaBDtL0wLsYqq5Pjs1pfhOhsl5PLSA8wFxPCK8FEYWopO1xxgKBRqqVK8f1rDoi3XOQrzz2GB9a5wo0oxDx5yTyr1erdhGcwo499rtbHKGa1pZyk3AfifaG8Fd/5RSulfuirsNSEZdunE1YSE6bcHfbcPIOABUEvT3DWAQDasDrmxE3ILDZcS2yXrNhbCSq2MyzYq5SnFKDTFznqTrOz0jeToI/PNSY9Kd2ehKsmSwaNDgG89LjxKveca6hucnPlsZOn/JXahbGoEM84dT0kuL8fIo3HW5zG5ZA+bySXY2qu+Tmy9jUa188DMbIgrNM5FMDZrhBVxkbOV1Tgxq8L9ZgPIqesJYJD3B6M65SMweMlZXd18ype31pJSmksOC6xKL222OGlcNiEg8b0SxE3pZADeNBRd7CA7KRiTUd+BUu+wLIjcGR73iTM1fh6PzhffBKOnTe2U+nrSlrW4AXFbgU5m2BOR1DjKravq//QlEqLtgvsT6nMiUia8YbI1xxaZgX7qnU0xWUQZnsEGq7746HxZsouV4ZWUvUSPcLIi5f4pS6aeLuRe23jR+VEBih5Rl2Cw1Bu06keJCLhusLnQ6zU6Z4EOJOeOcdhRl+qHCuG7lQOlgZMm+wBd/L14T6LQ8D4Wrlkw4zLSg81J0utYIHYUiEqgWz24iyjPXgByVMX3XWZmuCre2Wz5w0i7sspG5QbT3RoQEiFEkcD2tGvxtivj9w3jecwb3ZTz4FvbRHKW8REyxB64EqnVdKrV5RlR6zllI2KmDrRIUz0hSdqXKB2FoysbVkQcoLMh6/dN4ZNbdEmyJTujx5rhWDlzpN6FtyfNHmewjS8WiNOLxho6TwEc1wjPgAuCoqwfVnKXD8rp6AEIS25P7sqhJElCjO9vOPMfUlCb0iSbZGzLX5CroGcdypxZ5vVJQboy9x29j0I7DBQXz0uzgejmM143y1N6YObA9+0AMLrSiJ95Ik9sNpoS5fSeiiKk8KN8KtdGPYFimMRekGbNM1ScEDdc1/wEh9hil0InbwY162GWll9zOINfj2cbJHPwU6+Abe54m57Ny4sLsmlJkH12YX7poUaqGvUQ1vvey8Fkg73wvEcrhAaoBLIgpfR7VN9MjeoGZugWW5PwW72iIzuKZplgz6gLa01DH8pUVgVseymh2lSWVdoloyOt276Bsu4bzPn+JPEkoJ7Za2Rvb7ZK4k+fXnqcStW5Vn0q0ccenvDelT7wodIx8yu3CI7DzGJ8W3RAQohNHeaJOgIPapnK0BaPxApFT6NpstjjYTVcmueeF2EiSNEef/cJH00kJEcm3Gqb3EPpk/mBbdXvQ+M7KZEY8HNM2IUfYQqGy7VvI2XsHF1bgd6+ACwXC2sVx7pHbtLDTZRQSxJbASah8iW9P0U2bdlIhySu3JrWD+t1h5lx0qAAFUebRWpTXRPMAmfFV4NZYdXnLGphDzU6seZfGAoWnuqhcEpQcemLtpNnYz9cq9esDQVOn24uncT0VNA9ZdBOJnAM2MLQWy3ee2PVnVxvFON6Z6hHowS2lVy5uzCNC9PCR+b+yhhzK66mxXVftPKseeEo3BX7o/nCr0Sn1zuogeLGMauc7XHjnQOyE/MGu2Id9UWz+2RdWLo9VCanehu2QQDesuvyaSpz5bRxXzfYK1DPBZ7PbklJo/SWeqV8jxpmU4tsFsry/tPNtKpJ9VxzXFxHCh6vujnkMEZJYXPcAiBmR6k7VrHiLKeY14V6d7DmbIUS+4oKwftCec5fxkKkfKoPU/WqVUpYcAUesbpmSe52KPqYjoPdhgFuQprI6tCgG0DykCQaTZ8eQ0ke9q0C/DQ5m4u+vAc7/L/t5U763nTiMIA/F9yS1I87OSOxTabDWY3UlUBBmP2nQGp/7046ddEVZWr3nEz4kiM5vBKcx5+1EufzaQizVMXtjEzcHhNIxWDbUQVu7ZCOdoY4Wzn5/EskYbyhPyspVtwfoV5KuPdkmVjWCzG5Vgc2iK955hf2PwUkbL5nvZoo5ZwVQw4R671Wf1mQR1kBZ1M6VZZl940lOR2vABUuqaMGtCwDaYor4QM6dJ6i+cc74RAi4GfJRM2omNotdKBaybHfM2yt/o5KY0wGZXzSJKIqwN3L98rS4uPmoQ5TXydp7RxK4PUAeq9GZDSw7pgWqqNueydneVYIuTLUmMmi13Jx7mQYZmZ6CV4jYNIz0M4xv3rIfNiaQ0q0S9jnvtPki9J6yJ5MOpduZHnRcl0BqVSYHqSIN71rjw0aMAVaGT11yzPX3DVslZTKTd2mU6omrxKK1ULn2DFLNziLC+6xWtpiwvldb3Mb+apK4MMMWa2Y6PinJo8tkKUvRrW0lii5pX5A5TVSX4+t20mr047sRbJJjPAZ89wwdLNdyU/RDLxRsFK2qdZhyzETnaxW3ROIj3O+00pru/r3eQhQLM1RmVn43sDSz06ZpiSGDmQwk73BnuPy61fqw9qXg8HBYYpGYw93JaLAvvBwaXbyTb0PGk3xQ19IPIgu5xO1/ML4rJaIINAW68Dtd6hvFRZHuss7cgXYL1clT+uZZzXAB1EmPrZkdt7PsLGBk28kl68n3uRA2e6Xk+Ox42Hps1uhhjeu3mq6Eh/Pv1QUwVZIx7xni+y4Cg57YCfa7KHe6aphh5TLEo5rgEpDJYFiGNU3LZuzk9Buy8iFP0W5I15veJFSNBZyR4JMpb5UmvYDcHXTiw7R3jMw1CI636Eh8j4zPhwjwUWJoOGTHQfMUS48qYOal728zBxZ00kXI7CqvUgnbyEShRQxTGC6odYt4TFn2C40X0d0U2tYKJWS/beboRzreAIpjqjbUNdRWnqhiZSX7eqThQ17id1bRumBGCMjhiUZUlK7hewf3DHImxMrdCjs0c3nhmjfsE6Ri3w8HxY4Ex0J5B6+z+5VPvkhjL+hM8Er1jP7JjIboH1ONM7V3KNBIY5JzzVUsR8NjlhhcpI6HyOCfrhZL8qqizA9Hh46SMyTuS19fbWhmUNgJjhp5ne+WJ4oZBg8oIuUDYndBTqUZvBhZg2hIsy8qJst1p+OayRk+Q0v2/FmTlgXvJG5Hw/saKAzhrwIXolzUc9KW4914zy6GTP3DPn/Vj2rUESwr6hGnmSPMQhyRoety0a+6ab7aS8Iy1+zSPEbjpx2btfM0+mXS0o6yoaZcLyhhg2Kq60K3X9PN447tPnT2+u5G/J4lfc3nvA/X+bs/8+Et/Mb9UqTt6mQJ+Ej6/f3vX1l1X8/vlTH7/2Gr67AUM5PT+G7f9LDfjyQy/9WQ34zqD8ETf1mMDxw/MYw+cbFf30Y82/JYcPHuInhOLLB0LxDzYx7E8/ZKx3xd8kxW/uAfgN3+v+8y8W0GRBfVUAAA== -->
