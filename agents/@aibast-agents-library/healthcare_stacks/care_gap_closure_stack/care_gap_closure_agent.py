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
  1. Out of the box it pulls live cases, contacts, and tasks over real
     HTTP from the globally hosted Static Dynamics 365 tenant (Aster
     Lane Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="gap_analysis")
     — alongside the HEDIS measure table it surfaces Riverbend Medical
     Group's real seeded queue, e.g. CAS-260124 "Prior authorization
     request pending beyond SLA" (High priority).
  2. No network? Everything falls back to the embedded demo layer below
     (HEDIS_MEASURES / PATIENT_SEGMENTS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CARE_GAP_CLOSURE_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from your population-health
     platform), or replace _fetch_collection() with your registry
     client. The fields the rest of the file needs are listed in
     _normalize_live_work_item() — patient identifiers and measure
     attribution are enrichment seams; wire your EHR/registry there
     (and mind PHI: this template ships only synthetic data).

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
    "version": "1.2.0",
    "display_name": "Care Gap Closure Agent",
    "description": "Analyzes HEDIS care gaps and surfaces the live care-coordination queue from a simulated Dynamics 365 tenant, with offline demo fallback.",
    "author": "AIBAST",
    "tags": ["hedis", "care-gaps", "quality-measures", "outreach", "population-health", "healthcare"],
    "category": "healthcare",
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
#   export CARE_GAP_CLOSURE_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your registry/EHR client.
# Downstream code only needs the fields produced by
# _normalize_live_work_item().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "CARE_GAP_CLOSURE_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
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
    print("EMBEDDED DEMO MEASURES + LIVE TENANT QUEUE")
    print("(HEDIS table works offline; the Riverbend queue is fetched")
    print("over HTTP and falls back gracefully)")
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
