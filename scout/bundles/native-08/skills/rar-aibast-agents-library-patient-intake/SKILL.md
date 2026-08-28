---
name: "rar-aibast-agents-library-patient-intake"
description: "Runs patient intake \u2014 forms, insurance checks, scheduling \u2014 joining a live simulated FHIR patient roster with the Dynamics 365 CRM; offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/patient_intake", "rar_sha256": "f98ba4ec1b98d8a74b3053dcc3acb0e18f7c9daa1f2fc729bf716c23ec14c370", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.3.0", "author": "AIBAST", "tags": ["intake", "insurance", "scheduling", "patient", "registration", "healthcare"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/patient_intake`. The original RAPP
agent is preserved byte-for-byte in `patient_intake_agent.py` and in the RCI capsule.

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

Patient Intake Agent — a template you are meant to mutate.

Manages patient intake workflows including form generation, insurance
verification, appointment scheduling, pre-visit summary preparation, and
the demonstrated Sarah Martinez registration/booking/packet/no-show flows
(simulated receipts, never live writes) for front desk and clinical staff.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works from anywhere):
       CRM  — the Static Dynamics 365 tenant (Aster Lane Office Systems):
              https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
              Dynamics contacts of the healthcare account Riverbend
              Medical Group are reinterpreted as the CRM-side patient
              roster — e.g. contact Priya Natarajan.
       FHIR — the Static FHIR R4 server (Riverbend Medical Group):
              https://kody-w.github.io/static-fhir/fhir/
              20 live Patient resources form the clinical intake roster,
              with real MRNs, DOBs, and demographics.
     Try: perform(operation="intake_form")
     — one output renders the CRM contact roster and the FHIR Patient
     intake roster side by side, joined on the shared Riverbend Medical
     Group organization.
  2. No network? Everything falls back to the embedded demo layer below
     (PATIENTS / INSURANCE_PLANS / PROVIDER_SCHEDULES) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PATIENT_INTAKE_DATA_URL (CRM side) to any OData-shaped endpoint and
     PATIENT_INTAKE_FHIR_URL (clinical side) to any FHIR R4
     searchset-bundle host — or replace _fetch_collection() /
     _fetch_fhir_bundle() with an Epic/Cerner registration API client.
     Fields the rest of the file needs are listed in
     _normalize_live_patient() and _normalize_fhir_patient() — insurance
     and coverage fields render as "n/a — enrichment seam" until you wire
     an eligibility clearinghouse.

OPERATIONS
  intake_form | insurance_verification | appointment_scheduling
  | pre_visit_summary | register_patient | book_appointment
  | send_digital_intake_packet | activate_reminder_workflow
  kwargs: operation (required), patient_id, patient_key

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The intake operation to perform.",
      "enum": [
        "intake_form",
        "insurance_verification",
        "appointment_scheduling",
        "pre_visit_summary",
        "register_patient",
        "book_appointment",
        "send_digital_intake_packet",
        "activate_reminder_workflow"
      ],
      "type": "string"
    },
    "patient_id": {
      "description": "Optional patient ID to filter results.",
      "type": "string"
    },
    "patient_key": {
      "description": "Optional exact demo patient key; use Sarah Martinez.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `patient_intake_agent.py` and embedded as the fenced Python below (sha256 f98ba4ec1b98d8a7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `patient_intake_agent.py` first:

```bash
python3 patient_intake_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 patient_intake_agent.py   # or on stdin
python3 patient_intake_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Patient Intake Agent \u2014 a template you are meant to mutate.

Manages patient intake workflows including form generation, insurance
verification, appointment scheduling, pre-visit summary preparation, and
the demonstrated Sarah Martinez registration/booking/packet/no-show flows
(simulated receipts, never live writes) for front desk and clinical staff.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works from anywhere):
       CRM  \u2014 the Static Dynamics 365 tenant (Aster Lane Office Systems):
              https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
              Dynamics contacts of the healthcare account Riverbend
              Medical Group are reinterpreted as the CRM-side patient
              roster \u2014 e.g. contact Priya Natarajan.
       FHIR \u2014 the Static FHIR R4 server (Riverbend Medical Group):
              https://kody-w.github.io/static-fhir/fhir/
              20 live Patient resources form the clinical intake roster,
              with real MRNs, DOBs, and demographics.
     Try: perform(operation="intake_form")
     \u2014 one output renders the CRM contact roster and the FHIR Patient
     intake roster side by side, joined on the shared Riverbend Medical
     Group organization.
  2. No network? Everything falls back to the embedded demo layer below
     (PATIENTS / INSURANCE_PLANS / PROVIDER_SCHEDULES) \u2014 the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PATIENT_INTAKE_DATA_URL (CRM side) to any OData-shaped endpoint and
     PATIENT_INTAKE_FHIR_URL (clinical side) to any FHIR R4
     searchset-bundle host \u2014 or replace _fetch_collection() /
     _fetch_fhir_bundle() with an Epic/Cerner registration API client.
     Fields the rest of the file needs are listed in
     _normalize_live_patient() and _normalize_fhir_patient() \u2014 insurance
     and coverage fields render as "n/a \u2014 enrichment seam" until you wire
     an eligibility clearinghouse.

OPERATIONS
  intake_form | insurance_verification | appointment_scheduling
  | pre_visit_summary | register_patient | book_appointment
  | send_digital_intake_packet | activate_reminder_workflow
  kwargs: operation (required), patient_id, patient_key
"""

import sys
import os
import json
import urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/patient_intake",
    "version": "1.3.0",
    "display_name": "Patient Intake Agent",
    "description": "Runs patient intake \u2014 forms, insurance checks, scheduling \u2014 joining a live simulated FHIR patient roster with the Dynamics 365 CRM; offline fallback.",
    "author": "AIBAST",
    "tags": ["intake", "insurance", "scheduling", "patient", "registration", "healthcare"],
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
#     export PATIENT_INTAKE_DATA_URL=https://your-org/api/data/v9.2
#   FHIR (R4 searchset bundles, Riverbend Medical Group):
#     export PATIENT_INTAKE_FHIR_URL=https://your-fhir-host/fhir
# or replace _fetch_collection() / _fetch_fhir_bundle() with your
# EHR/PM client. Downstream code only needs the fields produced by
# _normalize_live_patient() and _normalize_fhir_patient().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "PATIENT_INTAKE_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
FHIR_SOURCE_URL = os.environ.get(
    "PATIENT_INTAKE_FHIR_URL",
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


def _normalize_live_patient(row):
    """Project a Dynamics contact onto the intake-form shape this agent
    renders. THIS is the contract your replacement data source must meet —
    a dict with these keys. None means 'not available from the CRM record
    alone' and the renderer labels it as an enrichment seam (wire your
    eligibility clearinghouse or payer portal there)."""
    city = row.get("address1_city") or "?"
    state = row.get("address1_stateorprovince") or "?"
    return {
        "patient_id": row.get("contactid", "")[:8] or "live",
        "name": row.get("fullname", "Unknown"),
        "dob": None,                # enrichment seam — wire your EHR demographics
        "gender": None,             # enrichment seam
        "phone": row.get("telephone1") or "n/a",
        "email": row.get("emailaddress1") or "n/a",
        "address": f"{city}, {state}",
        "emergency_contact": None,  # enrichment seam
        "insurance_payer": None,    # enrichment seam — wire eligibility 270/271
        "member_id": None,          # enrichment seam
        "_live": True,
    }


def _live_patients():
    """Riverbend Medical Group contacts from the live tenant, reinterpreted
    as the patient roster; [] when offline."""
    rows = _fetch_collection("contacts")
    return [
        _normalize_live_patient(r) for r in rows
        if r.get("parentcustomeridname") == "Riverbend Medical Group"
    ]


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


def _normalize_fhir_patient(res):
    """Project a FHIR R4 Patient resource onto the intake-roster row this
    agent renders. Real MRN, DOB, gender, and contact details come from
    the clinical record; insurance stays an enrichment seam (wire your
    eligibility clearinghouse or the Coverage resources)."""
    name = (res.get("name") or [{}])[0]
    full = " ".join(list(name.get("given", [])) + [name.get("family", "")]).strip() or "Unknown"
    telecom = res.get("telecom") or []
    addr = (res.get("address") or [{}])[0]
    return {
        "mrn": (res.get("identifier") or [{}])[0].get("value", res.get("id", "")[:8]),
        "name": full,
        "dob": res.get("birthDate") or None,
        "gender": (res.get("gender") or "").title() or None,
        "phone": next((t.get("value") for t in telecom if t.get("system") == "phone"), "n/a"),
        "email": next((t.get("value") for t in telecom if t.get("system") == "email"), "n/a"),
        "address": f"{addr.get('city', '?')}, {addr.get('state', '?')}",
        "organization": res.get("managingOrganization", {}).get("display", "n/a"),
        "active": res.get("active", True),
    }


def _live_fhir_intake_roster():
    """The live FHIR Patient resources as the clinical intake roster;
    [] when the FHIR feed is unreachable."""
    return [_normalize_fhir_patient(r) for r in _fetch_fhir_bundle("Patient")]


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

PATIENTS = {
    "PT-20001": {
        "name": "Jennifer Walsh",
        "dob": "1978-04-22",
        "gender": "Female",
        "phone": "555-0142",
        "email": "j.walsh@email.com",
        "address": "142 Oak Street, Springfield, IL 62701",
        "emergency_contact": {"name": "Michael Walsh", "relation": "Spouse", "phone": "555-0143"},
        "primary_language": "English",
        "race": "White",
        "ethnicity": "Non-Hispanic",
    },
    "PT-20002": {
        "name": "David Nguyen",
        "dob": "1992-11-08",
        "gender": "Male",
        "phone": "555-0255",
        "email": "d.nguyen@email.com",
        "address": "88 Maple Avenue, Springfield, IL 62702",
        "emergency_contact": {"name": "Linh Nguyen", "relation": "Mother", "phone": "555-0256"},
        "primary_language": "English",
        "race": "Asian",
        "ethnicity": "Non-Hispanic",
    },
    "PT-20003": {
        "name": "Maria Gonzalez",
        "dob": "1965-07-15",
        "gender": "Female",
        "phone": "555-0388",
        "email": "m.gonzalez@email.com",
        "address": "305 Elm Drive, Springfield, IL 62703",
        "emergency_contact": {"name": "Carlos Gonzalez", "relation": "Son", "phone": "555-0389"},
        "primary_language": "Spanish",
        "race": "White",
        "ethnicity": "Hispanic",
    },
}

INSURANCE_PLANS = {
    "PT-20001": {
        "primary": {
            "payer": "Blue Cross Blue Shield of Illinois",
            "plan": "PPO Gold",
            "member_id": "BCBS-884721",
            "group_number": "GRP-44210",
            "effective_date": "2025-01-01",
            "copay_office": 25,
            "copay_specialist": 50,
            "deductible": 1500,
            "deductible_met": 875,
            "coinsurance_pct": 20,
            "verification_status": "verified",
            "last_verified": "2026-03-10",
        },
        "secondary": None,
    },
    "PT-20002": {
        "primary": {
            "payer": "Aetna",
            "plan": "HMO Select",
            "member_id": "AET-552190",
            "group_number": "GRP-88104",
            "effective_date": "2025-07-01",
            "copay_office": 20,
            "copay_specialist": 40,
            "deductible": 2000,
            "deductible_met": 320,
            "coinsurance_pct": 25,
            "verification_status": "verified",
            "last_verified": "2026-03-12",
        },
        "secondary": None,
    },
    "PT-20003": {
        "primary": {
            "payer": "Medicare Part B",
            "plan": "Original Medicare",
            "member_id": "1EG4-TE5-MK72",
            "group_number": "N/A",
            "effective_date": "2025-07-15",
            "copay_office": 0,
            "copay_specialist": 0,
            "deductible": 257,
            "deductible_met": 257,
            "coinsurance_pct": 20,
            "verification_status": "verified",
            "last_verified": "2026-03-14",
        },
        "secondary": {
            "payer": "AARP Medigap Plan F",
            "plan": "Supplemental",
            "member_id": "AARP-MG-88421",
            "group_number": "N/A",
            "effective_date": "2025-07-15",
            "verification_status": "pending",
            "last_verified": None,
        },
    },
}

PROVIDER_SCHEDULES = {
    "Dr. Anita Patel": {
        "specialty": "Internal Medicine",
        "location": "Main Clinic - Suite 200",
        "available_slots": [
            {"date": "2026-03-18", "time": "09:00", "duration_min": 30, "type": "follow_up"},
            {"date": "2026-03-18", "time": "10:30", "duration_min": 60, "type": "new_patient"},
            {"date": "2026-03-19", "time": "14:00", "duration_min": 30, "type": "follow_up"},
            {"date": "2026-03-20", "time": "08:30", "duration_min": 60, "type": "new_patient"},
        ],
    },
    "Dr. James Wright": {
        "specialty": "Family Medicine",
        "location": "Main Clinic - Suite 105",
        "available_slots": [
            {"date": "2026-03-18", "time": "11:00", "duration_min": 30, "type": "follow_up"},
            {"date": "2026-03-19", "time": "09:30", "duration_min": 60, "type": "new_patient"},
            {"date": "2026-03-19", "time": "15:00", "duration_min": 30, "type": "follow_up"},
        ],
    },
    "Dr. Sarah Lin": {
        "specialty": "Cardiology",
        "location": "Cardiology Center - Suite 400",
        "available_slots": [
            {"date": "2026-03-20", "time": "10:00", "duration_min": 45, "type": "consultation"},
            {"date": "2026-03-21", "time": "13:00", "duration_min": 45, "type": "consultation"},
        ],
    },
}

INTAKE_QUESTIONNAIRES = {
    "new_patient": {
        "sections": ["Demographics", "Medical History", "Surgical History", "Family History",
                     "Social History", "Medications", "Allergies", "Review of Systems"],
        "estimated_time_min": 15,
    },
    "follow_up": {
        "sections": ["Medication Changes", "New Symptoms", "Vital Signs Update"],
        "estimated_time_min": 5,
    },
    "annual_wellness": {
        "sections": ["Demographics Update", "Health Risk Assessment", "PHQ-9 Depression Screen",
                     "Fall Risk Assessment", "Advance Directives", "Preventive Services Review"],
        "estimated_time_min": 20,
    },
}

DEMO_INTAKE = {
    "patient_key": "Sarah Martinez",
    "patient": "Sarah Martinez",
    "patient_type": "New Patient",
    "chief_complaint": "Chronic migraines",
    "provider": "Dr. James Anderson, MD",
    "specialty": "Neurology",
    "insurance": "Blue Cross Blue Shield",
    "policy_number": "XXX-XX-7392",
    "group_number": "84721",
    "insurance_status": "Active — verified in real time",
    "copay": "$35 specialist visit",
    "deductible": "$450 met of $1,500",
    "prior_authorization": "Not required for initial consultation",
    "network": "In network — Tier 1",
    "appointment": {
        "date": "Tuesday, January 30, 2024",
        "time": "2:30 PM",
        "duration": "60 minutes",
        "location": "Neurology Clinic — Suite 405",
        "visit_type": "New Patient Consultation",
    },
    "packet": [
        "Demographics and emergency contacts",
        "Insurance verification and card images",
        "Current medications, allergies, prior surgeries, and medical history",
        "HIT-6 migraine questionnaire",
        "HIPAA authorization with digital signature",
        "Financial policy and copay acknowledgment",
    ],
    "portal_phone": "(555) 234-8921",
    "reminders": [
        "72-hour: SMS and email (Saturday 2:30 PM)",
        "24-hour: SMS and optional voice call (Monday 2:30 PM)",
        "2-hour: final SMS (Tuesday 12:30 PM)",
        "Forms completion alert if incomplete by Monday",
        "SMS rescheduling using RESCHEDULE",
        "Waitlist auto-fill when cancellation notice exceeds 24 hours",
    ],
    "historical_no_show_rate": "8% for new patients using this protocol",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _intake_form(patient_id=None):
    forms = []
    pats = {patient_id: PATIENTS[patient_id]} if patient_id and patient_id in PATIENTS else PATIENTS
    for pid, pat in pats.items():
        ins = INSURANCE_PLANS.get(pid, {})
        forms.append({
            "patient_id": pid, "name": pat["name"], "dob": pat["dob"],
            "gender": pat["gender"], "phone": pat["phone"],
            "address": pat["address"],
            "emergency_contact": pat["emergency_contact"],
            "insurance_payer": ins.get("primary", {}).get("payer", "Unknown"),
            "member_id": ins.get("primary", {}).get("member_id", "Unknown"),
        })
    # Prefer live tenant patients when reachable; embedded demo stays too.
    live = [] if patient_id else _live_patients()
    fhir = [] if patient_id else _live_fhir_intake_roster()
    return {"forms": forms, "live": live, "fhir": fhir}


def _insurance_verification():
    results = []
    for pid, ins in INSURANCE_PLANS.items():
        pname = PATIENTS.get(pid, {}).get("name", "Unknown")
        primary = ins.get("primary", {})
        secondary = ins.get("secondary")
        ded_remaining = primary.get("deductible", 0) - primary.get("deductible_met", 0)
        results.append({
            "patient_id": pid, "name": pname,
            "payer": primary.get("payer", "N/A"),
            "plan": primary.get("plan", "N/A"),
            "member_id": primary.get("member_id", "N/A"),
            "status": primary.get("verification_status", "unknown"),
            "copay": primary.get("copay_office", 0),
            "deductible_remaining": max(0, ded_remaining),
            "has_secondary": secondary is not None,
            "secondary_status": secondary.get("verification_status", "N/A") if secondary else "N/A",
        })
    return {"verifications": results}


def _appointment_scheduling():
    schedule = []
    for provider, info in PROVIDER_SCHEDULES.items():
        for slot in info["available_slots"]:
            schedule.append({
                "provider": provider, "specialty": info["specialty"],
                "location": info["location"],
                "date": slot["date"], "time": slot["time"],
                "duration_min": slot["duration_min"],
                "type": slot["type"],
            })
    schedule.sort(key=lambda x: (x["date"], x["time"]))
    return {"available_slots": schedule, "total_slots": len(schedule)}


def _pre_visit_summary():
    summaries = []
    for pid, pat in PATIENTS.items():
        ins = INSURANCE_PLANS.get(pid, {}).get("primary", {})
        copay = ins.get("copay_office", 0)
        ded_remaining = max(0, ins.get("deductible", 0) - ins.get("deductible_met", 0))
        summaries.append({
            "patient_id": pid, "name": pat["name"], "dob": pat["dob"],
            "phone": pat["phone"], "language": pat["primary_language"],
            "payer": ins.get("payer", "N/A"),
            "copay": copay, "deductible_remaining": ded_remaining,
            "verification_status": ins.get("verification_status", "unknown"),
        })
    return {"summaries": summaries}


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

class PatientIntakeAgent(BasicAgent):
    """Patient intake workflow and insurance verification agent."""

    def __init__(self):
        self.name = "PatientIntakeAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "intake_form",
                            "insurance_verification",
                            "appointment_scheduling",
                            "pre_visit_summary",
                            "register_patient",
                            "book_appointment",
                            "send_digital_intake_packet",
                            "activate_reminder_workflow",
                        ],
                        "description": "The intake operation to perform.",
                    },
                    "patient_id": {
                        "type": "string",
                        "description": "Optional patient ID to filter results.",
                    },
                    "patient_key": {
                        "type": "string",
                        "description": "Optional exact demo patient key; use Sarah Martinez.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "intake_form")
        if op == "intake_form":
            return self._intake_form()
        elif op == "insurance_verification":
            return self._insurance_verification()
        elif op == "appointment_scheduling":
            return self._appointment_scheduling()
        elif op == "pre_visit_summary":
            return self._pre_visit_summary()
        elif op == "register_patient":
            return self._register_patient(kwargs.get("patient_key"))
        elif op == "book_appointment":
            return self._book_appointment(kwargs.get("patient_key"))
        elif op == "send_digital_intake_packet":
            return self._send_digital_intake_packet(kwargs.get("patient_key"))
        elif op == "activate_reminder_workflow":
            return self._activate_reminder_workflow(kwargs.get("patient_key"))
        return f"**Error:** Unknown operation `{op}`."

    @staticmethod
    def _demo_intake(patient_key):
        if patient_key and patient_key.lower() != DEMO_INTAKE["patient_key"].lower():
            return None
        return DEMO_INTAKE

    @staticmethod
    def _missing_demo(patient_key):
        return f"**Error:** No demonstrated intake for patient `{patient_key}`. Available key: Sarah Martinez."

    def _intake_form(self) -> str:
        data = _intake_form()
        lines = ["# Patient Intake Forms", ""]
        for f in data["forms"]:
            ec = f["emergency_contact"]
            lines.append(f"## {f['name']} ({f['patient_id']})")
            lines.append(f"- DOB: {f['dob']} | Gender: {f['gender']}")
            lines.append(f"- Phone: {f['phone']}")
            lines.append(f"- Address: {f['address']}")
            lines.append(f"- Emergency Contact: {ec['name']} ({ec['relation']}) - {ec['phone']}")
            lines.append(f"- Insurance: {f['insurance_payer']} (ID: {f['member_id']})")
            lines.append("")
        if data["live"]:
            lines.append("---")
            lines.append("# Live Tenant Patient Roster (Dynamics contacts — Riverbend Medical Group)")
            lines.append("")
            seam = "n/a — enrichment seam"
            for f in data["live"]:
                lines.append(f"## {f['name']} ({f['patient_id']})")
                lines.append(f"- DOB: {f['dob'] or seam} | Gender: {f['gender'] or seam}")
                lines.append(f"- Phone: {f['phone']} | Email: {f['email']}")
                lines.append(f"- Address: {f['address']}")
                lines.append(f"- Emergency Contact: {seam}")
                lines.append(f"- Insurance: {f['insurance_payer'] or seam} (ID: {f['member_id'] or seam})")
                lines.append("")
        else:
            lines.append("_Live tenant unreachable — showing embedded demo patients only._")
        if data["fhir"]:
            seam = "n/a — enrichment seam"
            lines += [
                "",
                "---",
                f"# Live FHIR Intake Roster ({len(data['fhir'])} Patient resources — "
                "Riverbend Medical Group)",
                "",
                "Clinical-side roster from the live FHIR R4 server. The managing "
                "organization is the same Riverbend Medical Group account whose CRM "
                "contacts appear above — one provider group, two live systems. DOB "
                "and gender, enrichment seams on the CRM side, are real here.",
                "",
                "| MRN | Patient | DOB | Gender | Phone | City | Insurance |",
                "|-----|---------|-----|--------|-------|------|-----------|",
            ]
            for p in data["fhir"]:
                lines.append(
                    f"| {p['mrn']} | {p['name']} | {p['dob'] or seam} "
                    f"| {p['gender'] or seam} | {p['phone']} | {p['address']} "
                    f"| {seam} |"
                )
            orgs = {p["organization"] for p in data["fhir"]}
            lines += [
                "",
                f"_Join: managing organization {', '.join(sorted(orgs))} — matches "
                "the CRM account of the contact roster above. Insurance renders as "
                "an enrichment seam until you wire eligibility 270/271 or the FHIR "
                "Coverage resources._",
            ]
        else:
            lines += ["", "_Live FHIR server unreachable — clinical intake roster unavailable offline._"]
        return "\n".join(lines)

    def _insurance_verification(self) -> str:
        data = _insurance_verification()
        lines = [
            "# Insurance Verification",
            "",
            "| Patient | Payer | Plan | Member ID | Status | Copay | Ded. Remaining | Secondary |",
            "|---------|-------|------|-----------|--------|-------|---------------|-----------|",
        ]
        for v in data["verifications"]:
            sec = f"Yes ({v['secondary_status']})" if v["has_secondary"] else "No"
            lines.append(
                f"| {v['name']} | {v['payer']} | {v['plan']} | {v['member_id']} "
                f"| {v['status'].upper()} | ${v['copay']} | ${v['deductible_remaining']:,} | {sec} |"
            )
        return "\n".join(lines)

    def _appointment_scheduling(self) -> str:
        data = _appointment_scheduling()
        lines = [
            "# Available Appointments",
            "",
            f"**Total Available Slots:** {data['total_slots']}",
            "",
            "| Date | Time | Provider | Specialty | Location | Duration | Type |",
            "|------|------|----------|-----------|----------|----------|------|",
        ]
        for s in data["available_slots"]:
            lines.append(
                f"| {s['date']} | {s['time']} | {s['provider']} | {s['specialty']} "
                f"| {s['location']} | {s['duration_min']}min | {s['type']} |"
            )
        return "\n".join(lines)

    def _pre_visit_summary(self) -> str:
        data = _pre_visit_summary()
        lines = ["# Pre-Visit Summaries", ""]
        for s in data["summaries"]:
            lines.append(f"## {s['name']} ({s['patient_id']})")
            lines.append(f"- DOB: {s['dob']} | Language: {s['language']}")
            lines.append(f"- Insurance: {s['payer']} ({s['verification_status'].upper()})")
            lines.append(f"- Copay: ${s['copay']} | Deductible Remaining: ${s['deductible_remaining']:,}")
            lines.append("")
        return "\n".join(lines)

    def _register_patient(self, patient_key=None) -> str:
        data = self._demo_intake(patient_key)
        if not data:
            return self._missing_demo(patient_key)
        return "\n".join([
            "# Simulated Patient Registration",
            "",
            f"**Patient:** {data['patient']} | **Type:** {data['patient_type']}",
            f"**Requested provider:** {data['provider']}, {data['specialty']}",
            f"**Chief complaint:** {data['chief_complaint']}",
            f"**Insurance:** {data['insurance']}",
            f"**Simulated receipt:** SIM-REG-SARAH-MARTINEZ",
            "",
            "**Status:** SIMULATED — no Epic registration or patient record was created or changed.",
        ])

    def _book_appointment(self, patient_key=None) -> str:
        data = self._demo_intake(patient_key)
        if not data:
            return self._missing_demo(patient_key)
        appt = data["appointment"]
        return "\n".join([
            "# Simulated Appointment Booking",
            "",
            f"**Patient:** {data['patient']} | **Provider:** {data['provider']}",
            f"**When:** {appt['date']} at {appt['time']} ({appt['duration']})",
            f"**Location:** {appt['location']} | **Type:** {appt['visit_type']}",
            f"**Coverage:** {data['insurance_status']}; {data['copay']}; {data['prior_authorization']}",
            "**Simulated receipt:** SIM-APPT-SARAH-MARTINEZ-2024-01-30-1430",
            "",
            "**Status:** SIMULATED — no provider calendar, EHR appointment, SMS, or email was changed.",
        ])

    def _send_digital_intake_packet(self, patient_key=None) -> str:
        data = self._demo_intake(patient_key)
        if not data:
            return self._missing_demo(patient_key)
        lines = [
            "# Simulated Digital Intake Packet",
            "",
            f"**Patient:** {data['patient']} | **Portal phone:** {data['portal_phone']}",
            "",
            "## Included forms",
        ]
        lines.extend(f"- {item}" for item in data["packet"])
        lines += [
            "",
            "**Simulated receipt:** SIM-PACKET-SARAH-MARTINEZ",
            "**Status:** SIMULATED — no SharePoint file, portal packet, SMS, or signature request was created.",
        ]
        return "\n".join(lines)

    def _activate_reminder_workflow(self, patient_key=None) -> str:
        data = self._demo_intake(patient_key)
        if not data:
            return self._missing_demo(patient_key)
        lines = [
            "# Simulated No-Show Prevention Workflow",
            "",
            f"**Patient:** {data['patient']} | **Historical no-show rate:** {data['historical_no_show_rate']}",
            "",
        ]
        lines.extend(f"- {item}" for item in data["reminders"])
        lines += [
            "",
            "**Simulated receipt:** SIM-REMINDER-SARAH-MARTINEZ",
            "**Status:** SIMULATED — no Power Automate flow, reminder, reschedule, or waitlist action was created.",
        ]
        return "\n".join(lines)


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    agent = PatientIntakeAgent()
    print("=" * 60)
    print("EMBEDDED DEMO + LIVE CRM ROSTER + LIVE FHIR INTAKE ROSTER")
    print("(sibling-live demo: 20 FHIR Patient resources join the CRM")
    print("contact roster on the Riverbend Medical Group organization;")
    print("both feeds fetched over HTTP and fall back offline)")
    print("=" * 60)
    print(agent.perform(operation="intake_form"))
    for op in [
        "insurance_verification", "appointment_scheduling", "pre_visit_summary",
        "register_patient", "book_appointment", "send_digital_intake_packet",
        "activate_reminder_workflow",
    ]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
