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
