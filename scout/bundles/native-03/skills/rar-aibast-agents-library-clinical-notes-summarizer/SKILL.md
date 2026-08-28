---
name: "rar-aibast-agents-library-clinical-notes-summarizer"
description: "Summarizes encounters and medication reviews, joining live simulated FHIR appointment-patient headers with the Dynamics 365 CRM; offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/clinical_notes_summarizer", "rar_sha256": "eb04379ac6704d21092ddb012c16a0221cafa61fe075172418f4dc12326fbe8d", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.3.0", "author": "AIBAST", "tags": ["clinical-notes", "ehr", "encounters", "medications", "referrals", "healthcare"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/clinical_notes_summarizer`. The original RAPP
agent is preserved byte-for-byte in `clinical_notes_summarizer_agent.py` and in the RCI capsule.

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

Clinical Notes Summarizer Agent — a template you are meant to mutate.

Summarizes patient encounters, performs medication reviews, generates
problem lists, produces referral summaries, and runs the demonstrated
pre-op clearance workflow (deterministic, keyed by patient ID ``78392``)
for healthcare providers and care coordinators.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works from anywhere):
       CRM  — the Static Dynamics 365 tenant (Aster Lane Office Systems):
              https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
              A Dynamics case (incident) is reinterpreted as a clinical
              encounter event — e.g. Riverbend Medical Group's case
              "Patient intake forms failing to sync to records system".
       FHIR — the Static FHIR R4 server (Riverbend Medical Group):
              https://kody-w.github.io/static-fhir/fhir/
              Each fulfilled Appointment is joined to its Patient
              resource and summarized as an encounter header with real
              MRN, DOB, gender, visit, and practitioner.
     Try: perform(operation="summarize_encounter")
     — one output renders the embedded demo encounters, the CRM-side
     encounter events, AND the live FHIR Appointment+Patient encounter
     headers (the narrative bodies stay declared simulated).
  2. No network? Everything falls back to the embedded demo layer below
     (PATIENT_ENCOUNTERS / MEDICATIONS / REFERRALS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CLINICAL_NOTES_SUMMARIZER_DATA_URL (CRM side) to any OData-shaped
     endpoint and CLINICAL_NOTES_SUMMARIZER_FHIR_URL (clinical side) to
     any FHIR R4 searchset-bundle host — or replace _fetch_collection()
     / _fetch_fhir_bundle() with calls into an Epic/Cerner FHIR API.
     Fields the rest of the file needs are listed in
     _normalize_live_encounter() — vitals, diagnoses, and labs render as
     "n/a — enrichment seam" until you wire a clinical system.

OPERATIONS
  summarize_encounter | medication_review | problem_list | referral_summary
  | preop_clearance | cardiopulmonary_assessment
  | surgical_medication_reconciliation | anesthesia_risk_plan
  | issue_clearance_note
  kwargs: operation (required), encounter_id, patient_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "encounter_id": {
      "description": "Optional encounter ID to filter results.",
      "type": "string"
    },
    "operation": {
      "description": "The clinical notes operation to perform.",
      "enum": [
        "summarize_encounter",
        "medication_review",
        "problem_list",
        "referral_summary",
        "preop_clearance",
        "cardiopulmonary_assessment",
        "surgical_medication_reconciliation",
        "anesthesia_risk_plan",
        "issue_clearance_note"
      ],
      "type": "string"
    },
    "patient_id": {
      "description": "Optional exact patient ID; 78392 selects the demonstrated pre-op case.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `clinical_notes_summarizer_agent.py` and embedded as the fenced Python below (sha256 eb04379ac6704d21…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `clinical_notes_summarizer_agent.py` first:

```bash
python3 clinical_notes_summarizer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 clinical_notes_summarizer_agent.py   # or on stdin
python3 clinical_notes_summarizer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Clinical Notes Summarizer Agent — a template you are meant to mutate.

Summarizes patient encounters, performs medication reviews, generates
problem lists, produces referral summaries, and runs the demonstrated
pre-op clearance workflow (deterministic, keyed by patient ID ``78392``)
for healthcare providers and care coordinators.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works from anywhere):
       CRM  — the Static Dynamics 365 tenant (Aster Lane Office Systems):
              https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
              A Dynamics case (incident) is reinterpreted as a clinical
              encounter event — e.g. Riverbend Medical Group's case
              "Patient intake forms failing to sync to records system".
       FHIR — the Static FHIR R4 server (Riverbend Medical Group):
              https://kody-w.github.io/static-fhir/fhir/
              Each fulfilled Appointment is joined to its Patient
              resource and summarized as an encounter header with real
              MRN, DOB, gender, visit, and practitioner.
     Try: perform(operation="summarize_encounter")
     — one output renders the embedded demo encounters, the CRM-side
     encounter events, AND the live FHIR Appointment+Patient encounter
     headers (the narrative bodies stay declared simulated).
  2. No network? Everything falls back to the embedded demo layer below
     (PATIENT_ENCOUNTERS / MEDICATIONS / REFERRALS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CLINICAL_NOTES_SUMMARIZER_DATA_URL (CRM side) to any OData-shaped
     endpoint and CLINICAL_NOTES_SUMMARIZER_FHIR_URL (clinical side) to
     any FHIR R4 searchset-bundle host — or replace _fetch_collection()
     / _fetch_fhir_bundle() with calls into an Epic/Cerner FHIR API.
     Fields the rest of the file needs are listed in
     _normalize_live_encounter() — vitals, diagnoses, and labs render as
     "n/a — enrichment seam" until you wire a clinical system.

OPERATIONS
  summarize_encounter | medication_review | problem_list | referral_summary
  | preop_clearance | cardiopulmonary_assessment
  | surgical_medication_reconciliation | anesthesia_risk_plan
  | issue_clearance_note
  kwargs: operation (required), encounter_id, patient_id
"""

import sys
import os
import json
import urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/clinical_notes_summarizer",
    "version": "1.3.0",
    "display_name": "Clinical Notes Summarizer Agent",
    "description": "Summarizes encounters and medication reviews, joining live simulated FHIR appointment-patient headers with the Dynamics 365 CRM; offline fallback.",
    "author": "AIBAST",
    "tags": ["clinical-notes", "ehr", "encounters", "medications", "referrals", "healthcare"],
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
#     export CLINICAL_NOTES_SUMMARIZER_DATA_URL=https://your-org/api/data/v9.2
#   FHIR (R4 searchset bundles, Riverbend Medical Group):
#     export CLINICAL_NOTES_SUMMARIZER_FHIR_URL=https://your-fhir-host/fhir
# or replace _fetch_collection() / _fetch_fhir_bundle() with your
# EHR/FHIR client. Downstream code only needs the fields produced by
# _normalize_live_encounter() and _live_fhir_encounter_headers().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "CLINICAL_NOTES_SUMMARIZER_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
FHIR_SOURCE_URL = os.environ.get(
    "CLINICAL_NOTES_SUMMARIZER_FHIR_URL",
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


def _normalize_live_encounter(row):
    """Project a Dynamics case onto the encounter-summary shape this agent
    renders. THIS is the contract your replacement data source must meet —
    a dict with these keys. None / empty list means 'not available from the
    CRM-side record alone' and the renderer labels it as an enrichment seam
    (wire your EHR, lab system, or vitals feed there)."""
    return {
        "encounter_id": row.get("ticketnumber", "?"),
        "patient": row.get("primarycontactidname") or "Unknown",
        "age": None,          # enrichment seam — wire your EHR demographics
        "date": str(row.get("createdon", ""))[:10],
        "type": row.get(
            "casetypecode@OData.Community.Display.V1.FormattedValue", "Case"
        ),
        "provider": row.get("owneridname", "Unassigned"),
        "chief_complaint": row.get("title", "untitled"),
        "diagnoses": [],      # enrichment seam — wire your EHR problem list
        "abnormal_labs": [],  # enrichment seam — wire your lab system
        "bp": None,           # enrichment seam
        "bmi": None,          # enrichment seam
        "_live": True,
    }


def _live_encounters():
    """Riverbend Medical Group cases from the live tenant, reinterpreted as
    clinical encounter events; [] when offline."""
    rows = _fetch_collection("incidents")
    return [
        _normalize_live_encounter(r) for r in rows
        if r.get("customeridname") == "Riverbend Medical Group"
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


def _live_fhir_encounter_headers():
    """Each fulfilled FHIR Appointment joined to its Patient resource,
    summarized as an encounter header: real MRN, DOB, gender, visit
    description, date, and practitioner from the live clinical record.
    Narrative bodies, diagnoses, and vitals remain enrichment seams —
    the demo narratives in this file stay declared simulated. [] when
    the FHIR feed is unreachable."""
    appts = _fetch_fhir_bundle("Appointment")
    if not appts:
        return []
    patients = {p.get("id"): p for p in _fetch_fhir_bundle("Patient")}
    headers = []
    for a in appts:
        if a.get("status") != "fulfilled":
            continue
        patient_name, practitioner, pat_res = "Unknown", "Unassigned", None
        for p in a.get("participant", []):
            ref = p.get("actor", {}).get("reference", "")
            if ref.startswith("Patient/"):
                patient_name = p.get("actor", {}).get("display", "Unknown")
                pat_res = patients.get(ref.split("/", 1)[1])
            elif ref.startswith("Practitioner/"):
                practitioner = p.get("actor", {}).get("display", "Unassigned")
        headers.append({
            "patient": patient_name,
            "mrn": (pat_res.get("identifier") or [{}])[0].get("value")
            if pat_res else None,
            "dob": pat_res.get("birthDate") if pat_res else None,
            "gender": (pat_res.get("gender") or "").title() or None
            if pat_res else None,
            "visit": a.get("description", "untitled visit"),
            "date": str(a.get("start", ""))[:10],
            "practitioner": practitioner,
        })
    return headers


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

PATIENT_ENCOUNTERS = {
    "ENC-2001": {
        "patient_id": "PT-10045",
        "patient_name": "Margaret Sullivan",
        "age": 68,
        "gender": "Female",
        "encounter_date": "2026-03-12",
        "encounter_type": "Office Visit",
        "provider": "Dr. Anita Patel",
        "chief_complaint": "Follow-up for diabetes management and new onset left knee pain",
        "clinical_notes": (
            "Patient presents for routine diabetes follow-up. Reports increased thirst and "
            "urination over past 2 weeks. Also complains of left knee pain, worse with stairs, "
            "onset 3 weeks ago. No trauma. HbA1c drawn today. Blood pressure elevated at 148/92. "
            "Weight 187 lbs, up 4 lbs from last visit. Bilateral pedal edema noted. "
            "Left knee with mild effusion, no instability. ROM slightly decreased."
        ),
        "vital_signs": {
            "bp_systolic": 148, "bp_diastolic": 92, "heart_rate": 78,
            "temperature_f": 98.4, "respiratory_rate": 16, "weight_lbs": 187,
            "bmi": 31.2, "spo2_pct": 97,
        },
        "diagnoses": [
            {"code": "E11.65", "description": "Type 2 diabetes with hyperglycemia", "status": "active"},
            {"code": "I10", "description": "Essential hypertension", "status": "active"},
            {"code": "M17.12", "description": "Primary osteoarthritis, left knee", "status": "new"},
            {"code": "E66.01", "description": "Morbid obesity due to excess calories", "status": "active"},
        ],
        "lab_results": [
            {"test": "HbA1c", "value": "8.2%", "reference": "<7.0%", "flag": "high"},
            {"test": "Fasting Glucose", "value": "182 mg/dL", "reference": "70-100 mg/dL", "flag": "high"},
            {"test": "eGFR", "value": "62 mL/min", "reference": ">60 mL/min", "flag": "borderline"},
            {"test": "Creatinine", "value": "1.1 mg/dL", "reference": "0.6-1.2 mg/dL", "flag": "normal"},
        ],
    },
    "ENC-2002": {
        "patient_id": "PT-10078",
        "patient_name": "Robert Kim",
        "age": 52,
        "gender": "Male",
        "encounter_date": "2026-03-14",
        "encounter_type": "Urgent Care",
        "provider": "Dr. James Wright",
        "chief_complaint": "Chest tightness and shortness of breath for 2 days",
        "clinical_notes": (
            "52-year-old male with history of GERD and anxiety presents with 2 days of intermittent "
            "chest tightness, worse with exertion. Denies radiation to arm or jaw. Reports occasional "
            "SOB climbing stairs. No syncope, diaphoresis, or palpitations. Family history of MI in "
            "father at age 58. Current smoker, 1 PPD x 20 years. EKG shows normal sinus rhythm, "
            "no ST changes. Troponin negative x2. CXR clear."
        ),
        "vital_signs": {
            "bp_systolic": 138, "bp_diastolic": 86, "heart_rate": 92,
            "temperature_f": 98.6, "respiratory_rate": 18, "weight_lbs": 215,
            "bmi": 29.8, "spo2_pct": 96,
        },
        "diagnoses": [
            {"code": "R07.9", "description": "Chest pain, unspecified", "status": "new"},
            {"code": "K21.0", "description": "GERD with esophagitis", "status": "active"},
            {"code": "F41.1", "description": "Generalized anxiety disorder", "status": "active"},
            {"code": "F17.210", "description": "Nicotine dependence, cigarettes", "status": "active"},
        ],
        "lab_results": [
            {"test": "Troponin I", "value": "<0.01 ng/mL", "reference": "<0.04 ng/mL", "flag": "normal"},
            {"test": "BNP", "value": "45 pg/mL", "reference": "<100 pg/mL", "flag": "normal"},
            {"test": "Total Cholesterol", "value": "248 mg/dL", "reference": "<200 mg/dL", "flag": "high"},
            {"test": "LDL", "value": "168 mg/dL", "reference": "<100 mg/dL", "flag": "high"},
        ],
    },
}

MEDICATIONS = {
    "PT-10045": [
        {"name": "Metformin", "dose": "1000mg", "frequency": "BID", "route": "oral", "indication": "Type 2 Diabetes", "status": "active", "start_date": "2022-05-10"},
        {"name": "Lisinopril", "dose": "20mg", "frequency": "daily", "route": "oral", "indication": "Hypertension", "status": "active", "start_date": "2021-03-15"},
        {"name": "Atorvastatin", "dose": "40mg", "frequency": "daily", "route": "oral", "indication": "Hyperlipidemia", "status": "active", "start_date": "2023-01-20"},
        {"name": "Aspirin", "dose": "81mg", "frequency": "daily", "route": "oral", "indication": "Cardiovascular prevention", "status": "active", "start_date": "2023-01-20"},
        {"name": "Meloxicam", "dose": "15mg", "frequency": "daily", "route": "oral", "indication": "Osteoarthritis", "status": "new", "start_date": "2026-03-12"},
    ],
    "PT-10078": [
        {"name": "Omeprazole", "dose": "20mg", "frequency": "daily", "route": "oral", "indication": "GERD", "status": "active", "start_date": "2024-08-05"},
        {"name": "Sertraline", "dose": "100mg", "frequency": "daily", "route": "oral", "indication": "Anxiety", "status": "active", "start_date": "2023-11-12"},
        {"name": "Atorvastatin", "dose": "80mg", "frequency": "daily", "route": "oral", "indication": "Hyperlipidemia", "status": "new", "start_date": "2026-03-14"},
        {"name": "Aspirin", "dose": "81mg", "frequency": "daily", "route": "oral", "indication": "Cardiovascular prevention", "status": "new", "start_date": "2026-03-14"},
    ],
}

REFERRALS = {
    "REF-3001": {
        "patient_id": "PT-10045",
        "patient_name": "Margaret Sullivan",
        "from_provider": "Dr. Anita Patel",
        "to_specialty": "Orthopedics",
        "to_provider": "Dr. Michael Torres",
        "reason": "Left knee osteoarthritis evaluation - possible injection or surgical consult",
        "urgency": "routine",
        "encounter_id": "ENC-2001",
    },
    "REF-3002": {
        "patient_id": "PT-10078",
        "patient_name": "Robert Kim",
        "from_provider": "Dr. James Wright",
        "to_specialty": "Cardiology",
        "to_provider": "Dr. Sarah Lin",
        "reason": "Stress test and cardiac risk stratification - chest pain with cardiac risk factors",
        "urgency": "urgent",
        "encounter_id": "ENC-2002",
    },
    "REF-3003": {
        "patient_id": "PT-10078",
        "patient_name": "Robert Kim",
        "from_provider": "Dr. James Wright",
        "to_specialty": "Pulmonology",
        "to_provider": "Dr. David Huang",
        "reason": "Smoking cessation program and pulmonary function evaluation",
        "urgency": "routine",
        "encounter_id": "ENC-2002",
    },
}

PREOP_CLEARANCE = {
    "patient_id": "78392",
    "patient": "John Martinez",
    "age": 67,
    "sex": "male",
    "procedure_date": "November 2",
    "encounters_reviewed": 14,
    "cardiac": [
        "Cardiac status: stable",
        "Emergency evaluation 2 months ago: myocardial infarction ruled out",
        "ECG yesterday: normal sinus rhythm, 82 bpm",
        "Cardiac risk: low (Goldman below 1%)",
    ],
    "respiratory": [
        "COPD Stage 2; FEV1 68% predicted",
        "Exacerbation 6 weeks ago: resolved",
        "O2 saturation: 94% on room air",
        "Respiratory risk: moderate",
    ],
    "labs": "Creatinine 1.1, eGFR 67, potassium 4.2 — acceptable",
    "medications": [
        "Metoprolol 50 mg BID",
        "Lisinopril 10 mg daily — hold 24 hours before procedure",
        "Metformin 1000 mg BID",
        "Tamsulosin 0.4 mg — floppy iris risk alert",
        "Aspirin 81 mg",
        "Six additional medications reconciled with no surgical concerns",
    ],
    "plan": [
        "Monitored anesthesia care (MAC)",
        "Extended PACU monitoring for 2-3 hours with continuous pulse oximetry",
        "Notify anesthesia team of floppy iris syndrome risk",
        "Use an afternoon slot for optimal respiratory status",
    ],
    "asa_class": "III",
    "clearance_status": "APPROVED with documented precautions",
    "reconsider_if": [
        "COPD exacerbation within 2 weeks",
        "Acute or new cardiac symptoms",
        "O2 saturation below 90% on room air",
        "Uncontrolled blood pressure above 180/100",
        "Active URI or bronchitis; delay 2-4 weeks",
        "Medication changes that require stability reassessment",
    ],
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _summarize_encounter(encounter_id=None):
    encounters = PATIENT_ENCOUNTERS if not encounter_id else {encounter_id: PATIENT_ENCOUNTERS[encounter_id]}
    summaries = []
    for eid, enc in encounters.items():
        abnormal_labs = [l for l in enc["lab_results"] if l["flag"] != "normal"]
        summaries.append({
            "encounter_id": eid, "patient": enc["patient_name"], "age": enc["age"],
            "date": enc["encounter_date"], "type": enc["encounter_type"],
            "provider": enc["provider"], "chief_complaint": enc["chief_complaint"],
            "diagnoses": enc["diagnoses"], "abnormal_labs": abnormal_labs,
            "bp": f"{enc['vital_signs']['bp_systolic']}/{enc['vital_signs']['bp_diastolic']}",
            "bmi": enc["vital_signs"]["bmi"],
        })
    # Prefer live tenant encounters when reachable; embedded demo stays too.
    live = [] if encounter_id else _live_encounters()
    fhir = [] if encounter_id else _live_fhir_encounter_headers()
    return {"summaries": summaries, "live": live, "fhir": fhir}


def _medication_review(patient_id=None):
    if patient_id:
        meds = {patient_id: MEDICATIONS.get(patient_id, [])}
    else:
        meds = MEDICATIONS
    reviews = []
    for pid, med_list in meds.items():
        active = [m for m in med_list if m["status"] == "active"]
        new = [m for m in med_list if m["status"] == "new"]
        reviews.append({
            "patient_id": pid, "total_medications": len(med_list),
            "active": active, "new": new,
            "polypharmacy_flag": len(med_list) >= 5,
        })
    return {"reviews": reviews}


def _problem_list():
    problems = {}
    for eid, enc in PATIENT_ENCOUNTERS.items():
        pid = enc["patient_id"]
        if pid not in problems:
            problems[pid] = {"patient": enc["patient_name"], "active": [], "new": []}
        for dx in enc["diagnoses"]:
            entry = {"code": dx["code"], "description": dx["description"]}
            if dx["status"] == "new":
                problems[pid]["new"].append(entry)
            else:
                problems[pid]["active"].append(entry)
    return {"patients": problems}


def _referral_summary():
    refs = []
    for rid, ref in REFERRALS.items():
        refs.append({
            "id": rid, "patient": ref["patient_name"],
            "from": ref["from_provider"], "to_specialty": ref["to_specialty"],
            "to_provider": ref["to_provider"], "reason": ref["reason"],
            "urgency": ref["urgency"],
        })
    return {"referrals": refs, "total": len(refs)}


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

class ClinicalNotesSummarizerAgent(BasicAgent):
    """Clinical notes summarization and medication review agent."""

    def __init__(self):
        self.name = "ClinicalNotesSummarizerAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "summarize_encounter",
                            "medication_review",
                            "problem_list",
                            "referral_summary",
                            "preop_clearance",
                            "cardiopulmonary_assessment",
                            "surgical_medication_reconciliation",
                            "anesthesia_risk_plan",
                            "issue_clearance_note",
                        ],
                        "description": "The clinical notes operation to perform.",
                    },
                    "encounter_id": {
                        "type": "string",
                        "description": "Optional encounter ID to filter results.",
                    },
                    "patient_id": {
                        "type": "string",
                        "description": "Optional exact patient ID; 78392 selects the demonstrated pre-op case.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "summarize_encounter")
        if op == "summarize_encounter":
            return self._summarize_encounter()
        elif op == "medication_review":
            return self._medication_review()
        elif op == "problem_list":
            return self._problem_list()
        elif op == "referral_summary":
            return self._referral_summary()
        elif op == "preop_clearance":
            return self._preop_clearance(kwargs.get("patient_id"))
        elif op == "cardiopulmonary_assessment":
            return self._cardiopulmonary_assessment(kwargs.get("patient_id"))
        elif op == "surgical_medication_reconciliation":
            return self._surgical_medication_reconciliation(kwargs.get("patient_id"))
        elif op == "anesthesia_risk_plan":
            return self._anesthesia_risk_plan(kwargs.get("patient_id"))
        elif op == "issue_clearance_note":
            return self._issue_clearance_note(kwargs.get("patient_id"))
        return f"**Error:** Unknown operation `{op}`."

    @staticmethod
    def _preop_case(patient_id):
        if patient_id and patient_id != PREOP_CLEARANCE["patient_id"]:
            return None
        return PREOP_CLEARANCE

    @staticmethod
    def _missing_preop(patient_id):
        return f"**Error:** No demonstrated pre-op case for patient `{patient_id}`. Available patient ID: 78392."

    def _summarize_encounter(self) -> str:
        data = _summarize_encounter()
        lines = ["# Encounter Summaries", ""]
        for s in data["summaries"]:
            lines.append(f"## {s['patient']} (Age {s['age']}) - {s['date']}")
            lines.append(f"**Type:** {s['type']} | **Provider:** {s['provider']}")
            lines.append(f"**Chief Complaint:** {s['chief_complaint']}")
            lines.append(f"**BP:** {s['bp']} | **BMI:** {s['bmi']}")
            lines.append("")
            lines.append("**Diagnoses:**")
            for dx in s["diagnoses"]:
                status_tag = " [NEW]" if dx["status"] == "new" else ""
                lines.append(f"- {dx['code']}: {dx['description']}{status_tag}")
            if s["abnormal_labs"]:
                lines.append("")
                lines.append("**Abnormal Labs:**")
                lines.append("")
                lines.append("| Test | Value | Reference | Flag |")
                lines.append("|------|-------|-----------|------|")
                for lab in s["abnormal_labs"]:
                    lines.append(f"| {lab['test']} | {lab['value']} | {lab['reference']} | {lab['flag'].upper()} |")
            lines.append("")
        if data["live"]:
            lines.append("---")
            lines.append("# Live Tenant Encounters (Dynamics cases — Riverbend Medical Group)")
            lines.append("")
            for s in data["live"]:
                age = "n/a — enrichment seam" if s["age"] is None else s["age"]
                bp = s["bp"] or "n/a — enrichment seam"
                bmi = "n/a — enrichment seam" if s["bmi"] is None else s["bmi"]
                lines.append(f"## {s['patient']} ({s['encounter_id']}) - {s['date']}")
                lines.append(f"**Type:** {s['type']} | **Provider:** {s['provider']}")
                lines.append(f"**Chief Complaint:** {s['chief_complaint']}")
                lines.append(f"**Age:** {age} | **BP:** {bp} | **BMI:** {bmi}")
                lines.append("**Diagnoses:** n/a — enrichment seam (wire your EHR problem list)")
                lines.append("")
        else:
            lines.append("_Live tenant unreachable — showing embedded demo encounters only._")
        if data["fhir"]:
            seam = "n/a — enrichment seam"
            lines.append("---")
            lines.append(
                f"# Live FHIR Encounter Headers ({len(data['fhir'])} fulfilled "
                "Appointment + Patient joins — Riverbend Medical Group)"
            )
            lines.append("")
            lines.append(
                "Each header joins a fulfilled FHIR Appointment to its Patient "
                "resource — MRN, DOB, gender, visit, date, and practitioner are "
                "live clinical data. The narrative bodies remain the embedded "
                "demo layer above and stay declared simulated."
            )
            lines.append("")
            for h in data["fhir"]:
                lines.append(f"## {h['patient']} ({h['mrn'] or seam}) - {h['date']}")
                lines.append(f"**Visit:** {h['visit']} | **Provider:** {h['practitioner']}")
                lines.append(f"**DOB:** {h['dob'] or seam} | **Gender:** {h['gender'] or seam}")
                lines.append(
                    "**Narrative, diagnoses, vitals, labs:** n/a — enrichment seam "
                    "(wire Encounter/Condition/Observation resources)"
                )
                lines.append("")
        else:
            lines.append("_Live FHIR server unreachable — encounter headers unavailable offline._")
        return "\n".join(lines)

    def _medication_review(self) -> str:
        data = _medication_review()
        lines = ["# Medication Review", ""]
        for r in data["reviews"]:
            poly = " [POLYPHARMACY FLAG]" if r["polypharmacy_flag"] else ""
            lines.append(f"## Patient {r['patient_id']}{poly}")
            lines.append(f"**Total Medications:** {r['total_medications']}")
            lines.append("")
            lines.append("| Medication | Dose | Frequency | Route | Indication | Status |")
            lines.append("|-----------|------|-----------|-------|-----------|--------|")
            for m in r["active"] + r["new"]:
                lines.append(
                    f"| {m['name']} | {m['dose']} | {m['frequency']} "
                    f"| {m['route']} | {m['indication']} | {m['status'].upper()} |"
                )
            lines.append("")
        return "\n".join(lines)

    def _problem_list(self) -> str:
        data = _problem_list()
        lines = ["# Problem Lists", ""]
        for pid, pl in data["patients"].items():
            lines.append(f"## {pl['patient']} ({pid})")
            if pl["active"]:
                lines.append("\n**Active Problems:**")
                for p in pl["active"]:
                    lines.append(f"- [{p['code']}] {p['description']}")
            if pl["new"]:
                lines.append("\n**New Problems:**")
                for p in pl["new"]:
                    lines.append(f"- [{p['code']}] {p['description']}")
            lines.append("")
        return "\n".join(lines)

    def _referral_summary(self) -> str:
        data = _referral_summary()
        lines = [
            "# Referral Summary",
            "",
            f"**Total Referrals:** {data['total']}",
            "",
            "| Patient | From | To Specialty | To Provider | Urgency | Reason |",
            "|---------|------|-------------|-------------|---------|--------|",
        ]
        for r in data["referrals"]:
            lines.append(
                f"| {r['patient']} | {r['from']} | {r['to_specialty']} "
                f"| {r['to_provider']} | {r['urgency'].upper()} | {r['reason']} |"
            )
        return "\n".join(lines)

    def _preop_clearance(self, patient_id=None) -> str:
        data = self._preop_case(patient_id)
        if not data:
            return self._missing_preop(patient_id)
        return "\n".join([
            "# Pre-Op Clearance Summary",
            "",
            f"**Patient:** {data['patient']} ({data['patient_id']}), {data['age']}-year-old {data['sex']}",
            f"**Procedure date:** {data['procedure_date']}",
            f"**Evidence reviewed:** {data['encounters_reviewed']} encounters over 12 months, recent labs, ECG, medications, and problem list",
            f"**Labs:** {data['labs']}",
            f"**ASA class:** {data['asa_class']}",
            f"**Clearance:** {data['clearance_status']}",
            "",
            "_Read-only deterministic summary from the demonstrated EHR scenario._",
        ])

    def _cardiopulmonary_assessment(self, patient_id=None) -> str:
        data = self._preop_case(patient_id)
        if not data:
            return self._missing_preop(patient_id)
        lines = ["# Cardiopulmonary Assessment", "", f"**Patient ID:** {data['patient_id']}", "", "## Cardiac"]
        lines.extend(f"- {item}" for item in data["cardiac"])
        lines.append("\n## Respiratory")
        lines.extend(f"- {item}" for item in data["respiratory"])
        lines.append(f"\n**Labs:** {data['labs']}")
        return "\n".join(lines)

    def _surgical_medication_reconciliation(self, patient_id=None) -> str:
        data = self._preop_case(patient_id)
        if not data:
            return self._missing_preop(patient_id)
        lines = [
            "# Surgical Medication Reconciliation",
            "",
            f"**Patient ID:** {data['patient_id']} | **Active medications:** 12",
            "",
        ]
        lines.extend(f"- {item}" for item in data["medications"])
        lines.append("\n_Read-only medication result; no medication order was changed._")
        return "\n".join(lines)

    def _anesthesia_risk_plan(self, patient_id=None) -> str:
        data = self._preop_case(patient_id)
        if not data:
            return self._missing_preop(patient_id)
        lines = [
            "# Anesthesia and Risk Plan",
            "",
            f"**Patient ID:** {data['patient_id']} | **ASA class:** {data['asa_class']}",
            f"**Clearance:** {data['clearance_status']}",
            "",
            "## Recommended plan",
        ]
        lines.extend(f"- {item}" for item in data["plan"])
        lines.append("\n## Reconsider clearance if")
        lines.extend(f"- {item}" for item in data["reconsider_if"])
        return "\n".join(lines)

    def _issue_clearance_note(self, patient_id=None) -> str:
        data = self._preop_case(patient_id)
        if not data:
            return self._missing_preop(patient_id)
        return "\n".join([
            "# Simulated Clearance Note Issue",
            "",
            f"**Patient ID:** {data['patient_id']} | **ASA class:** {data['asa_class']}",
            f"**Decision:** {data['clearance_status']}",
            "**Destination:** Epic EHR pre-op evaluation, ophthalmology, anesthesia, and scheduling teams",
            f"**Simulated receipt:** SIM-CLEARANCE-{data['patient_id']}",
            "",
            "**Status:** SIMULATED — no EHR record, signature, message, or schedule was created or changed.",
        ])


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    agent = ClinicalNotesSummarizerAgent()
    print("=" * 60)
    print("EMBEDDED DEMO + LIVE CRM ENCOUNTERS + LIVE FHIR HEADERS")
    print("(sibling-live demo: fulfilled FHIR Appointments join their")
    print("Patient resources as encounter headers; canned narratives")
    print("stay simulated; both feeds fetched over HTTP, offline-safe)")
    print("=" * 60)
    print(agent.perform(operation="summarize_encounter"))
    for op in [
        "medication_review", "problem_list", "referral_summary",
        "preop_clearance", "cardiopulmonary_assessment",
        "surgical_medication_reconciliation", "anesthesia_risk_plan", "issue_clearance_note",
    ]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
