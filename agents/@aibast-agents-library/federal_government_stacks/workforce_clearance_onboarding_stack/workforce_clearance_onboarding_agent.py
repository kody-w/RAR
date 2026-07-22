"""
Workforce Clearance & Onboarding Agent — a template you are meant to mutate.

Manages security clearance tracking, onboarding checklists, background
check status, and access provisioning for federal workforce management.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live onboarding blockers over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template an onboarding or background-check hold is
     represented as a Dynamics case — e.g. CAS-260135 "Contractor
     onboarding blocked on background check" for Nina Kowalski of
     Beacon Hill Staffing Partners; days-in-queue is real clock math.
     Try: perform(operation="background_check_tracker")
  2. No network? Everything falls back to the embedded demo layer below
     (EMPLOYEES / ONBOARDING_STEPS / INVESTIGATION_TIMELINES) — the
     agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     WORKFORCE_CLEARANCE_ONBOARDING_DATA_URL to any OData-shaped
     endpoint (your real Dynamics org, or JSON exported from your HR
     system), or replace _fetch_collection() with your own API client.
     Fields the rest of the file needs are listed in
     _normalize_live_case() — everything else keeps working untouched.
     Fields marked "enrichment seam" in the output (investigation tier,
     clearance level) are where you wire DCSA/eQIP and your HRIS.

OPERATIONS
  clearance_status | onboarding_checklist | background_check_tracker
  | access_provisioning
  kwargs: operation (required), employee_id
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timezone

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/workforce_clearance_onboarding",
    "version": "1.1.0",
    "display_name": "Workforce Clearance & Onboarding Agent",
    "description": "Tracks onboarding blockers from a live simulated Dynamics 365 tenant, with clearance and access checklists that work offline.",
    "author": "AIBAST",
    "tags": ["clearance", "onboarding", "background-check", "workforce", "federal", "access"],
    "category": "federal_government",
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
#   export WORKFORCE_CLEARANCE_ONBOARDING_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your HRIS client. Downstream code
# only needs the fields produced by _normalize_live_case().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "WORKFORCE_CLEARANCE_ONBOARDING_DATA_URL",
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
            rows = json.loads(resp.read().decode("utf-8")).get("value", [])
    except Exception:
        rows = []
    _LIVE_CACHE[collection] = rows
    return rows


_ONBOARDING_KEYWORDS = ("onboarding", "background check", "clearance", "badge")


def _days_since(iso_date):
    try:
        then = datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
        if then.tzinfo is None:
            then = then.replace(tzinfo=timezone.utc)
        return max(0, (datetime.now(timezone.utc) - then).days)
    except (ValueError, TypeError):
        return None


def _normalize_live_case(row):
    """Project a Dynamics case onto the onboarding-blocker shape this
    agent uses. THIS is the contract your replacement data source must
    meet — a dict with these keys. None means 'not available from CRM
    alone' and the renderers label it as an enrichment seam. In this
    template an onboarding or background-check hold is represented as a
    Dynamics case."""
    return {
        "id": row.get("ticketnumber", ""),
        "candidate": row.get("customeridname", "Unknown"),
        "issue": row.get("title", "untitled"),
        "opened": str(row.get("createdon", ""))[:10],
        "days_in_queue": _days_since(row.get("createdon")),  # real clock math
        "status": "open" if row.get("statecode") == 0 else "resolved",
        "investigation_tier": None,  # enrichment seam — wire DCSA/eQIP
        "clearance_level": None,     # enrichment seam — wire your HRIS
        "_live": True,
    }


def _live_onboarding_cases():
    """Live tenant cases that read as onboarding/clearance holds; []
    when offline."""
    return [
        _normalize_live_case(i)
        for i in _fetch_collection("incidents")
        if any(k in str(i.get("title", "")).lower() for k in _ONBOARDING_KEYWORDS)
    ]


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

EMPLOYEES = {
    "EMP-5001": {
        "name": "Sarah Mitchell",
        "position": "Cybersecurity Analyst (GS-13)",
        "office": "Office of the CISO",
        "hire_date": "2025-03-01",
        "clearance_level": "Top Secret/SCI",
        "clearance_status": "pending_adjudication",
        "investigation_type": "T5",
        "investigation_opened": "2024-11-15",
        "interim_clearance": True,
        "eod_date": "2025-03-15",
    },
    "EMP-5002": {
        "name": "James Thornton",
        "position": "Program Analyst (GS-12)",
        "office": "Office of Acquisition Management",
        "hire_date": "2025-02-01",
        "clearance_level": "Secret",
        "clearance_status": "active",
        "investigation_type": "T3",
        "investigation_opened": "2024-09-01",
        "interim_clearance": False,
        "eod_date": "2025-02-10",
    },
    "EMP-5003": {
        "name": "Priya Desai",
        "position": "Data Scientist (GS-14)",
        "office": "Office of Data Analytics",
        "hire_date": "2025-04-01",
        "clearance_level": "Top Secret",
        "clearance_status": "investigation_in_progress",
        "investigation_type": "T5",
        "investigation_opened": "2025-01-10",
        "interim_clearance": False,
        "eod_date": None,
    },
    "EMP-5004": {
        "name": "Robert Chen",
        "position": "IT Specialist (GS-11)",
        "office": "Office of Information Technology",
        "hire_date": "2025-01-15",
        "clearance_level": "Public Trust (MBI)",
        "clearance_status": "active",
        "investigation_type": "T2",
        "investigation_opened": "2024-10-01",
        "interim_clearance": False,
        "eod_date": "2025-01-20",
    },
}

ONBOARDING_STEPS = {
    "pre_arrival": [
        {"step": "Tentative offer accepted", "required": True, "days_before_eod": 30},
        {"step": "SF-86 submitted to DCSA", "required": True, "days_before_eod": 28},
        {"step": "Drug test completed", "required": True, "days_before_eod": 21},
        {"step": "Official offer letter issued", "required": True, "days_before_eod": 14},
        {"step": "PIV card pre-enrollment", "required": True, "days_before_eod": 7},
    ],
    "day_one": [
        {"step": "Oath of office administered", "required": True},
        {"step": "PIV card issued and activated", "required": True},
        {"step": "Building access badge provisioned", "required": True},
        {"step": "IT equipment issued (laptop, phone)", "required": True},
        {"step": "Orientation briefing attended", "required": True},
    ],
    "first_week": [
        {"step": "Network account activated", "required": True},
        {"step": "Email and collaboration tools provisioned", "required": True},
        {"step": "Mandatory cyber awareness training", "required": True},
        {"step": "Records management training", "required": True},
        {"step": "Meet with supervisor — IDP discussion", "required": True},
    ],
    "first_30_days": [
        {"step": "Complete all required TMS training modules", "required": True},
        {"step": "Ethics briefing and financial disclosure (if applicable)", "required": False},
        {"step": "Telework agreement signed", "required": False},
        {"step": "Benefits enrollment confirmed", "required": True},
        {"step": "Performance plan established", "required": True},
    ],
}

INVESTIGATION_TIMELINES = {
    "T1": {"name": "Tier 1 (Low Risk)", "avg_days": 30, "target_days": 40},
    "T2": {"name": "Tier 2 (Moderate Risk / Public Trust)", "avg_days": 60, "target_days": 80},
    "T3": {"name": "Tier 3 (Secret)", "avg_days": 90, "target_days": 120},
    "T4": {"name": "Tier 4 (High Risk Public Trust)", "avg_days": 120, "target_days": 150},
    "T5": {"name": "Tier 5 (Top Secret / SCI)", "avg_days": 180, "target_days": 240},
}

ACCESS_REQUIREMENTS = {
    "Top Secret/SCI": {
        "network_access": ["JWICS", "SIPRNet", "NIPRNet"],
        "physical_access": ["SCIF", "Classified Workspace", "General Building"],
        "systems": ["XKEYSCORE-SIM", "SIGINT-Portal", "IC-Cloud"],
        "additional": ["SCI indoctrination briefing", "Polygraph (if CI)"],
    },
    "Top Secret": {
        "network_access": ["SIPRNet", "NIPRNet"],
        "physical_access": ["Classified Workspace", "General Building"],
        "systems": ["SIPR-Email", "Classified-SharePoint"],
        "additional": ["TS indoctrination briefing"],
    },
    "Secret": {
        "network_access": ["SIPRNet", "NIPRNet"],
        "physical_access": ["General Building"],
        "systems": ["SIPR-Email"],
        "additional": [],
    },
    "Public Trust (MBI)": {
        "network_access": ["NIPRNet"],
        "physical_access": ["General Building"],
        "systems": ["Agency-Email", "Agency-VPN", "SharePoint"],
        "additional": [],
    },
}

ONBOARDING_STATUS = {
    "EMP-5001": {"pre_arrival": "complete", "day_one": "complete", "first_week": "in_progress", "first_30_days": "pending"},
    "EMP-5002": {"pre_arrival": "complete", "day_one": "complete", "first_week": "complete", "first_30_days": "complete"},
    "EMP-5003": {"pre_arrival": "in_progress", "day_one": "pending", "first_week": "pending", "first_30_days": "pending"},
    "EMP-5004": {"pre_arrival": "complete", "day_one": "complete", "first_week": "complete", "first_30_days": "in_progress"},
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _clearance_days_elapsed(emp):
    """Calculate approximate days since investigation opened."""
    parts = emp["investigation_opened"].split("-")
    opened_ordinal = int(parts[0]) * 365 + int(parts[1]) * 30 + int(parts[2])
    current_ordinal = 2025 * 365 + 3 * 30 + 15
    return max(0, current_ordinal - opened_ordinal)


def _onboarding_pct(emp_id):
    """Calculate onboarding completion percentage."""
    status = ONBOARDING_STATUS.get(emp_id, {})
    phases = ["pre_arrival", "day_one", "first_week", "first_30_days"]
    complete = sum(1 for p in phases if status.get(p) == "complete")
    return round((complete / len(phases)) * 100, 0)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class WorkforceClearanceOnboardingAgent(BasicAgent):
    """Federal workforce clearance and onboarding management agent."""

    def __init__(self):
        self.name = "WorkforceClearanceOnboardingAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Workforce Clearance & Onboarding Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "clearance_status",
                            "onboarding_checklist",
                            "background_check_tracker",
                            "access_provisioning",
                        ],
                    },
                    "employee_id": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "clearance_status")
        dispatch = {
            "clearance_status": self._clearance_status,
            "onboarding_checklist": self._onboarding_checklist,
            "background_check_tracker": self._background_check_tracker,
            "access_provisioning": self._access_provisioning,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        return handler(**kwargs)

    def _clearance_status(self, **kwargs) -> str:
        lines = ["# Security Clearance Status\n"]
        lines.append("| Employee | Position | Clearance | Status | Investigation | Interim |")
        lines.append("|---|---|---|---|---|---|")
        for eid, emp in EMPLOYEES.items():
            interim = "Yes" if emp["interim_clearance"] else "No"
            status = emp["clearance_status"].replace("_", " ").title()
            lines.append(
                f"| {emp['name']} ({eid}) | {emp['position']} | {emp['clearance_level']} "
                f"| {status} | {emp['investigation_type']} | {interim} |"
            )
        pending = sum(1 for e in EMPLOYEES.values() if e["clearance_status"] != "active")
        lines.append(f"\n**Pending Clearances:** {pending}/{len(EMPLOYEES)}")
        active = sum(1 for e in EMPLOYEES.values() if e["clearance_status"] == "active")
        lines.append(f"**Active Clearances:** {active}/{len(EMPLOYEES)}")
        return "\n".join(lines)

    def _onboarding_checklist(self, **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        if employee_id and employee_id in EMPLOYEES:
            emp = EMPLOYEES[employee_id]
            status = ONBOARDING_STATUS.get(employee_id, {})
            pct = _onboarding_pct(employee_id)
            lines = [f"# Onboarding Checklist: {emp['name']}\n"]
            lines.append(f"- **Position:** {emp['position']}")
            lines.append(f"- **Office:** {emp['office']}")
            lines.append(f"- **EOD Date:** {emp['eod_date'] or 'TBD'}")
            lines.append(f"- **Completion:** {pct}%\n")
            for phase, steps in ONBOARDING_STEPS.items():
                phase_status = status.get(phase, "pending")
                lines.append(f"## {phase.replace('_', ' ').title()} — {phase_status.replace('_', ' ').title()}\n")
                for s in steps:
                    check = "x" if phase_status == "complete" else " "
                    req = " (required)" if s["required"] else ""
                    lines.append(f"- [{check}] {s['step']}{req}")
                lines.append("")
            return "\n".join(lines)

        lines = ["# Onboarding Status Summary\n"]
        lines.append("| Employee | Position | EOD | Completion |")
        lines.append("|---|---|---|---|")
        for eid, emp in EMPLOYEES.items():
            pct = _onboarding_pct(eid)
            lines.append(f"| {emp['name']} ({eid}) | {emp['position']} | {emp['eod_date'] or 'TBD'} | {pct}% |")
        return "\n".join(lines)

    def _background_check_tracker(self, **kwargs) -> str:
        live = _live_onboarding_cases()
        if live:
            open_holds = [c for c in live if c["status"] == "open"]
            lines = ["# Background Check Tracker (live tenant data)\n"]
            lines.append(f"**Onboarding/clearance holds on record:** {len(live)} "
                         f"({len(open_holds)} open)\n")
            lines.append("## Live Holds\n")
            lines.append("| Case | Candidate | Issue | Opened | Days in Queue | Tier | Status |")
            lines.append("|---|---|---|---|---|---|---|")
            for c in sorted(live, key=lambda x: (x["status"] != "open", x["opened"])):
                days = c["days_in_queue"] if c["days_in_queue"] is not None else "n/a"
                lines.append(
                    f"| {c['id']} | {c['candidate']} | {c['issue']} | {c['opened']} "
                    f"| {days} | n/a — enrichment seam | {c['status'].title()} |"
                )
            lines.append("\n## Investigation Timeline Reference\n")
            lines.append("| Tier | Name | Avg Days | Target Days |")
            lines.append("|---|---|---|---|")
            for tid, t in INVESTIGATION_TIMELINES.items():
                lines.append(f"| {tid} | {t['name']} | {t['avg_days']} | {t['target_days']} |")
            lines.append("\n_Source: live Static Dynamics 365 tenant (incidents). An "
                         "onboarding or background-check hold is represented as a Dynamics "
                         "case; days-in-queue is real clock math, investigation tier is an "
                         "enrichment seam._")
            return "\n".join(lines)

        lines = ["# Background Check Tracker (embedded demo data — offline)\n"]
        lines.append("## Investigation Timeline Reference\n")
        lines.append("| Tier | Name | Avg Days | Target Days |")
        lines.append("|---|---|---|---|")
        for tid, t in INVESTIGATION_TIMELINES.items():
            lines.append(f"| {tid} | {t['name']} | {t['avg_days']} | {t['target_days']} |")
        lines.append("\n## Active Investigations\n")
        lines.append("| Employee | Type | Opened | Days Elapsed | Target | Status |")
        lines.append("|---|---|---|---|---|---|")
        for eid, emp in EMPLOYEES.items():
            days = _clearance_days_elapsed(emp)
            inv = INVESTIGATION_TIMELINES.get(emp["investigation_type"], {})
            target = inv.get("target_days", 0)
            overdue = " (OVERDUE)" if days > target and emp["clearance_status"] != "active" else ""
            lines.append(
                f"| {emp['name']} | {emp['investigation_type']} | {emp['investigation_opened']} "
                f"| {days} | {target} | {emp['clearance_status'].replace('_', ' ').title()}{overdue} |"
            )
        return "\n".join(lines)

    def _access_provisioning(self, **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        if employee_id and employee_id in EMPLOYEES:
            emp = EMPLOYEES[employee_id]
            access = ACCESS_REQUIREMENTS.get(emp["clearance_level"], {})
            lines = [f"# Access Provisioning: {emp['name']}\n"]
            lines.append(f"- **Clearance Level:** {emp['clearance_level']}")
            lines.append(f"- **Status:** {emp['clearance_status'].replace('_', ' ').title()}\n")
            lines.append("## Network Access\n")
            for net in access.get("network_access", []):
                lines.append(f"- [ ] {net}")
            lines.append("\n## Physical Access\n")
            for phys in access.get("physical_access", []):
                lines.append(f"- [ ] {phys}")
            lines.append("\n## System Access\n")
            for sys_name in access.get("systems", []):
                lines.append(f"- [ ] {sys_name}")
            if access.get("additional"):
                lines.append("\n## Additional Requirements\n")
                for add in access["additional"]:
                    lines.append(f"- [ ] {add}")
            return "\n".join(lines)

        lines = ["# Access Provisioning Summary\n"]
        lines.append("| Clearance Level | Networks | Physical | Systems |")
        lines.append("|---|---|---|---|")
        for level, access in ACCESS_REQUIREMENTS.items():
            lines.append(
                f"| {level} | {', '.join(access['network_access'])} "
                f"| {', '.join(access['physical_access'])} | {', '.join(access['systems'])} |"
            )
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = WorkforceClearanceOnboardingAgent()
    print("=" * 60)
    print("LIVE TENANT ONBOARDING HOLDS (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="background_check_tracker"))
    print()
    print("=" * 60)
    print("EMBEDDED DEMO WORKFORCE (works offline)")
    print(agent.perform(operation="clearance_status"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="onboarding_checklist", employee_id="EMP-5001"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="access_provisioning", employee_id="EMP-5001"))
