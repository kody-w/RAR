---
name: "rar-aibast-agents-library-care-gap-closure"
description: "Analyzes HEDIS care gaps, joining live simulated FHIR appointment gap signals with the Dynamics 365 care-coordination queue; offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/care_gap_closure", "rar_sha256": "dfb2de8ae5d620dd765bb9baa6ac77de2e8ff235c423fc3e89640996478a55a6", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.3.0", "author": "AIBAST", "tags": ["hedis", "care-gaps", "quality-measures", "outreach", "population-health", "healthcare"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/care_gap_closure`. The original RAPP
agent is preserved byte-for-byte in `care_gap_closure_agent.py` and in the RCI capsule.

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

Care Gap Closure Agent for Healthcare — a template you are meant to mutate.

Analyzes HEDIS quality measure gaps, prioritizes patient outreach,
manages outreach campaigns, and provides HEDIS compliance dashboards
for population health management teams.

The live tenant has no native clinical registry, so in this template an
open Dynamics CASE for the provider group Riverbend Medical Group is
read as a patient-affecting care-coordination work item (e.g. a prior
authorization pending beyond SLA), and the tasks regarding it become
the outreach work queue. Say the same in your own mutation if you
reinterpret an entity.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works from anywhere):
       CRM  — the Static Dynamics 365 tenant (Aster Lane Office Systems):
              https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
              cases, contacts, and tasks — Riverbend Medical Group's real
              seeded queue, e.g. CAS-260124 "Prior authorization request
              pending beyond SLA" (High priority).
       FHIR — the Static FHIR R4 server (Riverbend Medical Group):
              https://kody-w.github.io/static-fhir/fhir/
              Appointment resources read as care-gap signals — cancelled
              visits are open gaps, fulfilled visits are closed ones.
     Try: perform(operation="gap_analysis")
     — alongside the HEDIS table it renders the CRM queue AND the FHIR
     gap signals, and ties the cancelled "Cardiac MRI ... pending prior
     authorization" Appointment to CRM case CAS-260124 in one output.
  2. No network? Everything falls back to the embedded demo layer below
     (HEDIS_MEASURES / PATIENT_SEGMENTS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CARE_GAP_CLOSURE_DATA_URL (CRM side) to any OData-shaped endpoint
     and CARE_GAP_CLOSURE_FHIR_URL (clinical side) to any FHIR R4
     searchset-bundle host — or replace _fetch_collection() /
     _fetch_fhir_bundle() with your registry client. The fields the rest
     of the file needs are listed in _normalize_live_work_item() —
     patient identifiers and measure attribution are enrichment seams;
     wire your EHR/registry there (and mind PHI: this template ships
     only synthetic data).

OPERATIONS
  gap_analysis | patient_prioritization | outreach_campaign
  | hedis_dashboard | barrier_analysis | launch_outreach_campaign
  | campaign_monitoring
  kwargs: operation (required), measure_id (CDC-HBA1C selects the
  demonstrated A1C campaign)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "measure_id": {
      "description": "Optional exact HEDIS measure ID; CDC-HBA1C selects the demonstrated A1C campaign.",
      "type": "string"
    },
    "operation": {
      "description": "The care gap closure operation to perform.",
      "enum": [
        "gap_analysis",
        "patient_prioritization",
        "outreach_campaign",
        "hedis_dashboard",
        "barrier_analysis",
        "launch_outreach_campaign",
        "campaign_monitoring"
      ],
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `care_gap_closure_agent.py` and embedded as the fenced Python below (sha256 dfb2de8ae5d620dd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `care_gap_closure_agent.py` first:

```bash
python3 care_gap_closure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 care_gap_closure_agent.py   # or on stdin
python3 care_gap_closure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Care Gap Closure Agent for Healthcare — a template you are meant to mutate.

Analyzes HEDIS quality measure gaps, prioritizes patient outreach,
manages outreach campaigns, and provides HEDIS compliance dashboards
for population health management teams.

The live tenant has no native clinical registry, so in this template an
open Dynamics CASE for the provider group Riverbend Medical Group is
read as a patient-affecting care-coordination work item (e.g. a prior
authorization pending beyond SLA), and the tasks regarding it become
the outreach work queue. Say the same in your own mutation if you
reinterpret an entity.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works from anywhere):
       CRM  — the Static Dynamics 365 tenant (Aster Lane Office Systems):
              https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
              cases, contacts, and tasks — Riverbend Medical Group's real
              seeded queue, e.g. CAS-260124 "Prior authorization request
              pending beyond SLA" (High priority).
       FHIR — the Static FHIR R4 server (Riverbend Medical Group):
              https://kody-w.github.io/static-fhir/fhir/
              Appointment resources read as care-gap signals — cancelled
              visits are open gaps, fulfilled visits are closed ones.
     Try: perform(operation="gap_analysis")
     — alongside the HEDIS table it renders the CRM queue AND the FHIR
     gap signals, and ties the cancelled "Cardiac MRI ... pending prior
     authorization" Appointment to CRM case CAS-260124 in one output.
  2. No network? Everything falls back to the embedded demo layer below
     (HEDIS_MEASURES / PATIENT_SEGMENTS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CARE_GAP_CLOSURE_DATA_URL (CRM side) to any OData-shaped endpoint
     and CARE_GAP_CLOSURE_FHIR_URL (clinical side) to any FHIR R4
     searchset-bundle host — or replace _fetch_collection() /
     _fetch_fhir_bundle() with your registry client. The fields the rest
     of the file needs are listed in _normalize_live_work_item() —
     patient identifiers and measure attribution are enrichment seams;
     wire your EHR/registry there (and mind PHI: this template ships
     only synthetic data).

OPERATIONS
  gap_analysis | patient_prioritization | outreach_campaign
  | hedis_dashboard | barrier_analysis | launch_outreach_campaign
  | campaign_monitoring
  kwargs: operation (required), measure_id (CDC-HBA1C selects the
  demonstrated A1C campaign)
"""

import sys
import os
import json
import urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/care_gap_closure",
    "version": "1.3.0",
    "display_name": "Care Gap Closure Agent",
    "description": "Analyzes HEDIS care gaps, joining live simulated FHIR appointment gap signals with the Dynamics 365 care-coordination queue; offline fallback.",
    "author": "AIBAST",
    "tags": ["hedis", "care-gaps", "quality-measures", "outreach", "population-health", "healthcare"],
    "category": "healthcare",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ---------------------------------------------------------------------------
# LIVE DATA SEAM — swap this for your real systems
#
# Two live sources, both synthetic and hosted on GitHub Pages:
#   CRM  (OData-shaped Dynamics 365, Aster Lane Office Systems):
#     export CARE_GAP_CLOSURE_DATA_URL=https://your-org/api/data/v9.2
#   FHIR (R4 searchset bundles, Riverbend Medical Group):
#     export CARE_GAP_CLOSURE_FHIR_URL=https://your-fhir-host/fhir
# or replace _fetch_collection() / _fetch_fhir_bundle() with your
# registry/EHR client. Downstream code only needs the fields produced
# by _normalize_live_work_item() and _live_appointment_gap_signals().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "CARE_GAP_CLOSURE_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
FHIR_SOURCE_URL = os.environ.get(
    "CARE_GAP_CLOSURE_FHIR_URL",
    "https://kody-w.github.io/static-fhir/fhir",
)
_LIVE_CACHE = {}

_PROVIDER_GROUP = "Riverbend Medical Group"


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


def _normalize_live_work_item(case, case_tasks):
    """Project a Dynamics case (read as a care-coordination work item)
    onto the shape this agent uses. THIS is the contract your
    replacement data source must meet — a dict with these keys. None
    means 'not available from the case alone'; patient identity and
    HEDIS measure attribution are enrichment seams (wire your EHR /
    registry — never embed real PHI in a template)."""
    return {
        "case_number": case.get("ticketnumber", ""),
        "title": case.get("title", "Untitled case"),
        "priority": case.get("prioritycode@OData.Community.Display.V1.FormattedValue", "Normal"),
        "status": case.get("statuscode@OData.Community.Display.V1.FormattedValue", "Open"),
        "opened": str(case.get("createdon", ""))[:10],
        "owner": case.get("owneridname", "unassigned"),
        "contact": case.get("primarycontactidname"),
        "measure_id": None,  # enrichment seam — wire your HEDIS registry
        "tasks": [
            {
                "subject": t.get("subject", "Untitled task"),
                "owner": t.get("owneridname", "unassigned"),
                "due": str(t.get("scheduledend", ""))[:10],
            }
            for t in case_tasks
        ],
        "_live": True,
    }


def _live_care_queue():
    """Open cases for the provider group, with their tasks; [] offline."""
    incidents = _fetch_collection("incidents")
    open_cases = [
        c for c in incidents
        if c.get("customeridname") == _PROVIDER_GROUP and c.get("statecode") == 0
    ]
    if not open_cases:
        return []
    tasks = _fetch_collection("tasks")
    queue = []
    for case in open_cases:
        case_tasks = [
            t for t in tasks
            if t.get("regardingobjectidname") == case.get("title")
        ]
        queue.append(_normalize_live_work_item(case, case_tasks))
    return queue


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


def _live_appointment_gap_signals():
    """FHIR Appointment resources read as care-gap signals: a cancelled
    visit is an open gap (care deferred or missed), a fulfilled visit is
    a recently closed one. HEDIS measure attribution stays an enrichment
    seam. None when the FHIR feed is unreachable."""
    appts = _fetch_fhir_bundle("Appointment")
    if not appts:
        return None

    def _row(a):
        patient = practitioner = "?"
        for p in a.get("participant", []):
            ref = p.get("actor", {}).get("reference", "")
            if ref.startswith("Patient/"):
                patient = p.get("actor", {}).get("display", "?")
            elif ref.startswith("Practitioner/"):
                practitioner = p.get("actor", {}).get("display", "?")
        return {
            "description": a.get("description", "untitled"),
            "patient": patient,
            "practitioner": practitioner,
            "start": str(a.get("start", ""))[:10],
            "status": a.get("status", "?"),
        }

    counts = {}
    for a in appts:
        status = a.get("status", "unknown")
        counts[status] = counts.get(status, 0) + 1
    return {
        "counts": counts,
        "cancelled": [_row(a) for a in appts if a.get("status") == "cancelled"],
        "fulfilled": [_row(a) for a in appts if a.get("status") == "fulfilled"],
    }


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

HEDIS_MEASURES = {
    "BCS": {
        "name": "Breast Cancer Screening",
        "description": "Women 50-74 with mammogram in past 2 years",
        "eligible_patients": 4280,
        "compliant_patients": 3210,
        "gap_rate_pct": 25.0,
        "revenue_per_closure": 45,
        "national_benchmark_pct": 78.2,
        "star_rating_impact": "4-star threshold at 76%",
    },
    "CDC-HBA1C": {
        "name": "Diabetes HbA1c Testing",
        "description": "Diabetic patients 18-75 with HbA1c test in past year",
        "eligible_patients": 6120,
        "compliant_patients": 5202,
        "gap_rate_pct": 15.0,
        "revenue_per_closure": 62,
        "national_benchmark_pct": 88.5,
        "star_rating_impact": "5-star threshold at 90%",
    },
    "COL": {
        "name": "Colorectal Cancer Screening",
        "description": "Adults 45-75 with appropriate colorectal screening",
        "eligible_patients": 8940,
        "compliant_patients": 5810,
        "gap_rate_pct": 35.0,
        "revenue_per_closure": 38,
        "national_benchmark_pct": 72.1,
        "star_rating_impact": "4-star threshold at 68%",
    },
    "CBP": {
        "name": "Controlling Blood Pressure",
        "description": "Hypertensive patients 18-85 with BP adequately controlled",
        "eligible_patients": 7650,
        "compliant_patients": 5355,
        "gap_rate_pct": 30.0,
        "revenue_per_closure": 55,
        "national_benchmark_pct": 65.8,
        "star_rating_impact": "4-star threshold at 64%",
    },
    "AWC": {
        "name": "Adolescent Well-Care Visits",
        "description": "Adolescents 12-21 with at least one well-care visit",
        "eligible_patients": 3200,
        "compliant_patients": 1920,
        "gap_rate_pct": 40.0,
        "revenue_per_closure": 28,
        "national_benchmark_pct": 58.4,
        "star_rating_impact": "3-star threshold at 54%",
    },
}

PATIENT_SEGMENTS = {
    "multi_gap_high_risk": {
        "count": 1842,
        "description": "Patients with 3+ open gaps and chronic conditions",
        "avg_risk_score": 3.8,
        "preferred_outreach": "phone_call",
        "response_rate_pct": 42,
    },
    "single_gap_engaged": {
        "count": 5610,
        "description": "Patients with 1 open gap and recent visit history",
        "avg_risk_score": 1.4,
        "preferred_outreach": "patient_portal",
        "response_rate_pct": 68,
    },
    "unreachable": {
        "count": 890,
        "description": "Patients with no valid contact info or repeated no-shows",
        "avg_risk_score": 2.9,
        "preferred_outreach": "mail",
        "response_rate_pct": 8,
    },
    "recently_compliant": {
        "count": 3420,
        "description": "Patients who closed gaps in last 90 days",
        "avg_risk_score": 1.1,
        "preferred_outreach": "none",
        "response_rate_pct": 0,
    },
}

OUTREACH_CHANNELS = {
    "phone_call": {"cost_per_contact": 4.50, "avg_response_rate_pct": 38, "avg_conversion_pct": 22},
    "patient_portal": {"cost_per_contact": 0.25, "avg_response_rate_pct": 52, "avg_conversion_pct": 31},
    "sms": {"cost_per_contact": 0.15, "avg_response_rate_pct": 45, "avg_conversion_pct": 18},
    "mail": {"cost_per_contact": 2.80, "avg_response_rate_pct": 12, "avg_conversion_pct": 6},
    "email": {"cost_per_contact": 0.08, "avg_response_rate_pct": 28, "avg_conversion_pct": 14},
}

DEMO_A1C_CAMPAIGN = {
    "measure_id": "CDC-HBA1C",
    "measure": "Diabetes A1C testing",
    "patients": 387,
    "revenue_at_risk": 189450,
    "risk_tiers": [
        "A1C >9.0 (Critical): 156 patients, average gap 8.7 months",
        "A1C 7-9 (Moderate): 137 patients, average gap 7.2 months",
    ],
    "barriers": [
        "Transportation: 34% (132 patients)",
        "No-show history: 28% (108 patients)",
        "Spanish language: 18% (70 patients)",
        "Insurance lapsed: 12% (46 patients)",
    ],
    "deployment": [
        "SMS: 294 patients (76% valid mobile)",
        "Patient portal: 312 messages",
        "Voicemail: 387 queued over 3 days",
        "RN outreach: 94 callbacks scheduled",
        "Mobile clinic: 47 slots reserved for the next 2 weeks",
        "Uber Health: 132 vouchers issued",
    ],
    "projected_close_rate": "68%",
    "projected_revenue_saved": 128700,
    "alerts": [
        "Close rate below 60%",
        "3 failed contact attempts",
        "Critical patient non-response over 48 hours",
        "Campaign budget variance over 15%",
    ],
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _gap_analysis():
    analysis = []
    for mid, m in HEDIS_MEASURES.items():
        gap_count = m["eligible_patients"] - m["compliant_patients"]
        current_rate = round((m["compliant_patients"] / m["eligible_patients"]) * 100, 1)
        revenue_opportunity = gap_count * m["revenue_per_closure"]
        analysis.append({
            "measure_id": mid, "name": m["name"],
            "eligible": m["eligible_patients"], "compliant": m["compliant_patients"],
            "gap_count": gap_count, "compliance_rate": current_rate,
            "gap_rate_pct": m["gap_rate_pct"],
            "benchmark": m["national_benchmark_pct"],
            "revenue_opportunity": revenue_opportunity,
            "star_impact": m["star_rating_impact"],
        })
    analysis.sort(key=lambda x: x["revenue_opportunity"], reverse=True)
    total_rev = sum(a["revenue_opportunity"] for a in analysis)
    return {"measures": analysis, "total_revenue_opportunity": total_rev}


def _patient_prioritization():
    segments = []
    for seg_id, seg in PATIENT_SEGMENTS.items():
        segments.append({
            "segment": seg_id.replace("_", " ").title(),
            "count": seg["count"],
            "description": seg["description"],
            "risk_score": seg["avg_risk_score"],
            "preferred_channel": seg["preferred_outreach"],
            "expected_response_pct": seg["response_rate_pct"],
        })
    segments.sort(key=lambda x: x["risk_score"], reverse=True)
    return {"segments": segments}


def _outreach_campaign():
    campaigns = []
    for mid, m in HEDIS_MEASURES.items():
        gap_count = m["eligible_patients"] - m["compliant_patients"]
        best_channel = max(OUTREACH_CHANNELS.items(), key=lambda x: x[1]["avg_conversion_pct"])
        channel_name, channel = best_channel
        projected_closures = round(gap_count * channel["avg_conversion_pct"] / 100)
        cost = round(gap_count * channel["cost_per_contact"], 2)
        revenue = projected_closures * m["revenue_per_closure"]
        campaigns.append({
            "measure": m["name"], "gap_count": gap_count,
            "channel": channel_name, "projected_closures": projected_closures,
            "cost": cost, "projected_revenue": revenue,
            "roi": round(revenue / cost, 1) if cost > 0 else 0,
        })
    campaigns.sort(key=lambda x: x["roi"], reverse=True)
    return {"campaigns": campaigns}


def _hedis_dashboard():
    dashboard = []
    for mid, m in HEDIS_MEASURES.items():
        current_rate = round((m["compliant_patients"] / m["eligible_patients"]) * 100, 1)
        vs_benchmark = round(current_rate - m["national_benchmark_pct"], 1)
        dashboard.append({
            "measure_id": mid, "name": m["name"],
            "current_rate": current_rate, "benchmark": m["national_benchmark_pct"],
            "vs_benchmark": vs_benchmark,
            "star_impact": m["star_rating_impact"],
            "eligible": m["eligible_patients"],
        })
    return {"measures": dashboard}


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

class CareGapClosureAgent(BasicAgent):
    """HEDIS care gap analysis and outreach management agent."""

    def __init__(self):
        self.name = "CareGapClosureAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "gap_analysis",
                            "patient_prioritization",
                            "outreach_campaign",
                            "hedis_dashboard",
                            "barrier_analysis",
                            "launch_outreach_campaign",
                            "campaign_monitoring",
                        ],
                        "description": "The care gap closure operation to perform.",
                    },
                    "measure_id": {
                        "type": "string",
                        "description": "Optional exact HEDIS measure ID; CDC-HBA1C selects the demonstrated A1C campaign.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "gap_analysis")
        if op == "gap_analysis":
            return self._gap_analysis()
        elif op == "patient_prioritization":
            return self._patient_prioritization()
        elif op == "outreach_campaign":
            return self._outreach_campaign()
        elif op == "hedis_dashboard":
            return self._hedis_dashboard()
        elif op == "barrier_analysis":
            return self._barrier_analysis(kwargs.get("measure_id"))
        elif op == "launch_outreach_campaign":
            return self._launch_outreach_campaign(kwargs.get("measure_id"))
        elif op == "campaign_monitoring":
            return self._campaign_monitoring(kwargs.get("measure_id"))
        return f"**Error:** Unknown operation `{op}`."

    @staticmethod
    def _demo_campaign(measure_id):
        if measure_id and measure_id != DEMO_A1C_CAMPAIGN["measure_id"]:
            return None
        return DEMO_A1C_CAMPAIGN

    def _gap_analysis(self) -> str:
        data = _gap_analysis()
        lines = [
            "# Care Gap Analysis",
            "",
            f"**Total Revenue Opportunity:** ${data['total_revenue_opportunity']:,}",
            "",
            "| Measure | Eligible | Compliant | Gaps | Rate | Benchmark | Revenue Opp | Star Impact |",
            "|---------|----------|-----------|------|------|-----------|------------|-------------|",
        ]
        for m in data["measures"]:
            lines.append(
                f"| {m['name']} | {m['eligible']:,} | {m['compliant']:,} | {m['gap_count']:,} "
                f"| {m['compliance_rate']}% | {m['benchmark']}% | ${m['revenue_opportunity']:,} | {m['star_impact']} |"
            )
        lines.append("")
        lines.append("_Measure table above is the embedded demo layer (simulated)._")
        queue = _live_care_queue()
        if queue:
            lines += [
                "",
                f"## Live care-coordination queue — {_PROVIDER_GROUP}",
                "",
                "LIVE open cases from the Aster Lane Dynamics 365 tenant, read as "
                "care-coordination work items (measure attribution is an "
                "enrichment seam — wire your HEDIS registry):",
                "",
                "| Case | Work Item | Priority | Status | Owner | Open Tasks |",
                "|------|-----------|----------|--------|-------|------------|",
            ]
            for item in queue:
                task_note = "; ".join(
                    f"{t['subject']} (due {t['due']})" for t in item["tasks"]
                ) or "none on record"
                lines.append(
                    f"| {item['case_number']} | {item['title'][:45]} | {item['priority']} "
                    f"| {item['status']} | {item['owner']} | {task_note} |"
                )
        else:
            lines += [
                "",
                "_Live care-coordination queue: live tenant unreachable — "
                "embedded demo layer only._",
            ]
        signals = _live_appointment_gap_signals()
        if signals:
            crm_pa_case = next(
                (item["case_number"] for item in queue
                 if "prior authorization" in item["title"].lower()),
                None,
            )
            counts = " | ".join(
                f"{status}: {n}" for status, n in sorted(signals["counts"].items())
            )
            lines += [
                "",
                "## Live FHIR appointment gap signals — Riverbend Medical Group",
                "",
                "LIVE Appointment resources from the FHIR R4 server, read as gap "
                "signals: cancelled = open gap (care deferred or missed), "
                "fulfilled = recently closed gap. HEDIS measure attribution is an "
                "enrichment seam — wire your registry.",
                "",
                f"**Appointment status mix:** {counts}",
                "",
                f"**Open gap signals (cancelled visits — {len(signals['cancelled'])}):**",
                "",
                "| Patient | Deferred/Missed Visit | Was Scheduled | Practitioner | CRM Tie-in |",
                "|---------|----------------------|---------------|--------------|------------|",
            ]
            for row in signals["cancelled"]:
                if crm_pa_case and "prior authorization" in row["description"].lower():
                    tie = f"tracked as case {crm_pa_case}"
                else:
                    tie = "n/a — enrichment seam"
                lines.append(
                    f"| {row['patient']} | {row['description'][:55]} | {row['start']} "
                    f"| {row['practitioner']} | {tie} |"
                )
            closed = ", ".join(
                f"{r['patient']} ({r['description']}, {r['start']})"
                for r in signals["fulfilled"]
            ) or "none"
            lines += [
                "",
                f"**Recently closed signals (fulfilled visits — "
                f"{len(signals['fulfilled'])}):** {closed}",
            ]
            if crm_pa_case:
                lines += [
                    "",
                    "_Join: the cancelled \"Cardiac MRI ... pending prior "
                    f"authorization\" Appointment and CRM case {crm_pa_case} in the "
                    "queue above are the same blocked care event — clinical signal "
                    "on the FHIR side, coordination work item on the CRM side._",
                ]
        else:
            lines += [
                "",
                "_Live FHIR appointment gap signals: FHIR server unreachable — "
                "embedded demo layer only._",
            ]
        return "\n".join(lines)

    def _patient_prioritization(self) -> str:
        data = _patient_prioritization()
        lines = [
            "# Patient Prioritization",
            "",
            "| Segment | Count | Risk Score | Preferred Channel | Expected Response |",
            "|---------|-------|-----------|-------------------|-------------------|",
        ]
        for s in data["segments"]:
            lines.append(
                f"| {s['segment']} | {s['count']:,} | {s['risk_score']} "
                f"| {s['preferred_channel']} | {s['expected_response_pct']}% |"
            )
        lines.append("")
        lines.append("## Recommendations")
        lines.append("- Prioritize multi-gap high-risk patients with phone outreach for highest impact.")
        lines.append("- Leverage patient portal messaging for single-gap engaged patients (lowest cost).")
        lines.append("- Initiate address verification campaign for unreachable segment.")
        return "\n".join(lines)

    def _outreach_campaign(self) -> str:
        data = _outreach_campaign()
        lines = [
            "# Outreach Campaign Plan",
            "",
            "| Measure | Gaps | Channel | Projected Closures | Cost | Revenue | ROI |",
            "|---------|------|---------|--------------------|------|---------|-----|",
        ]
        for c in data["campaigns"]:
            lines.append(
                f"| {c['measure']} | {c['gap_count']:,} | {c['channel']} "
                f"| {c['projected_closures']:,} | ${c['cost']:,.2f} | ${c['projected_revenue']:,} | {c['roi']}x |"
            )
        return "\n".join(lines)

    def _hedis_dashboard(self) -> str:
        data = _hedis_dashboard()
        lines = [
            "# HEDIS Dashboard",
            "",
            "| Measure | Current Rate | Benchmark | vs Benchmark | Eligible | Star Impact |",
            "|---------|-------------|-----------|-------------|----------|-------------|",
        ]
        for m in data["measures"]:
            direction = "+" if m["vs_benchmark"] >= 0 else ""
            lines.append(
                f"| {m['name']} | {m['current_rate']}% | {m['benchmark']}% "
                f"| {direction}{m['vs_benchmark']}% | {m['eligible']:,} | {m['star_impact']} |"
            )
        return "\n".join(lines)

    def _barrier_analysis(self, measure_id=None) -> str:
        data = self._demo_campaign(measure_id)
        if not data:
            return f"**Error:** No demonstrated campaign for measure `{measure_id}`. Available measure: CDC-HBA1C."
        lines = [
            "# A1C Risk and Barrier Analysis",
            "",
            f"**Measure ID:** {data['measure_id']} | **Patients:** {data['patients']} | "
            f"**Revenue at risk:** ${data['revenue_at_risk']:,}",
            "",
            "## Risk tiers",
        ]
        lines.extend(f"- {item}" for item in data["risk_tiers"])
        lines.append("\n## Engagement barriers")
        lines.extend(f"- {item}" for item in data["barriers"])
        lines.append("\n_Read-only result grounded in the demonstrated Medicare Advantage cohort._")
        return "\n".join(lines)

    def _launch_outreach_campaign(self, measure_id=None) -> str:
        data = self._demo_campaign(measure_id)
        if not data:
            return f"**Error:** No demonstrated campaign for measure `{measure_id}`. Available measure: CDC-HBA1C."
        lines = [
            "# Simulated A1C Outreach Campaign Launch",
            "",
            f"**Measure ID:** {data['measure_id']} | **Scope:** {data['patients']} patients",
            "",
        ]
        lines.extend(f"- {item}" for item in data["deployment"])
        lines += [
            "",
            f"**Simulated receipt:** SIM-CAMPAIGN-{data['measure_id']}",
            "**Status:** SIMULATED — no Dynamics 365, Power Automate, Teams, or patient channel was contacted or changed.",
        ]
        return "\n".join(lines)

    def _campaign_monitoring(self, measure_id=None) -> str:
        data = self._demo_campaign(measure_id)
        if not data:
            return f"**Error:** No demonstrated campaign for measure `{measure_id}`. Available measure: CDC-HBA1C."
        lines = [
            "# A1C Campaign Monitoring",
            "",
            f"**Measure ID:** {data['measure_id']}",
            f"**Projected close rate:** {data['projected_close_rate']}",
            f"**Projected revenue saved:** ${data['projected_revenue_saved']:,}",
            "**Teams cadence:** Daily 8 AM summary",
            "",
            "## Alert triggers",
        ]
        lines.extend(f"- {item}" for item in data["alerts"])
        lines.append("\n_Read-only deterministic snapshot; no external systems were queried._")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    agent = CareGapClosureAgent()
    print("=" * 60)
    print("EMBEDDED DEMO MEASURES + LIVE CRM QUEUE + LIVE FHIR SIGNALS")
    print("(sibling-live demo: FHIR cancelled/fulfilled Appointments are")
    print("gap signals, and the cancelled Cardiac MRI ties to CRM case")
    print("CAS-260124; both feeds fetched over HTTP, offline-safe)")
    print("=" * 60)
    print(agent.perform(operation="gap_analysis"))
    for op in [
        "patient_prioritization", "outreach_campaign", "hedis_dashboard",
        "barrier_analysis", "launch_outreach_campaign", "campaign_monitoring",
    ]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
