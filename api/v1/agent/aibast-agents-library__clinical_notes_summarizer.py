"""
Clinical Notes Summarizer Agent for Healthcare.

Summarizes patient encounters, performs medication reviews, generates
problem lists, and produces referral summaries from clinical documentation
for healthcare providers and care coordinators.

Version 1.1.0 preserves those operations and adds the demonstrated pre-op
clearance workflow. Added results use the patient facts visible in the source
demo, are deterministic and keyed by patient ID ``78392``, and simulate the
final EHR and care-team update without performing a live write.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/clinical_notes_summarizer",
    "version": "1.1.0",
    "display_name": "Clinical Notes Summarizer Agent",
    "description": "Summarizes patient encounters, performs medication reviews, generates problem lists, and produces referral summaries.",
    "author": "AIBAST",
    "tags": ["clinical-notes", "ehr", "encounters", "medications", "referrals", "healthcare"],
    "category": "healthcare",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ---------------------------------------------------------------------------
# Synthetic domain data
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
    return {"summaries": summaries}


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
    for op in [
        "summarize_encounter", "medication_review", "problem_list", "referral_summary",
        "preop_clearance", "cardiopulmonary_assessment",
        "surgical_medication_reconciliation", "anesthesia_risk_plan", "issue_clearance_note",
    ]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
