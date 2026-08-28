---
name: "rar-aibast-agents-library-workforce-clearance-onboarding"
description: "Tracks onboarding blockers from a live simulated Dynamics 365 CRM joined to an HRIS hire roster, with clearance checklists that work offline."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/workforce_clearance_onboarding", "rar_sha256": "181d78db4148c5939d7f6ff52142b5f80972d15303aad8505e716a758721b0aa", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.2.0", "author": "AIBAST", "tags": ["clearance", "onboarding", "background-check", "workforce", "federal", "access"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/workforce_clearance_onboarding`. The original RAPP
agent is preserved byte-for-byte in `workforce_clearance_onboarding_agent.py` and in the RCI capsule.

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

Workforce Clearance & Onboarding Agent — a template you are meant to mutate.

Manages security clearance tracking, onboarding checklists, background
check status, and access provisioning for federal workforce management.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted systems (synthetic data, no credentials, works
     from anywhere):
       CRM  https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       HRIS https://kody-w.github.io/static-hris/api/v1/
     An onboarding or background-check hold is represented as a
     Dynamics case — e.g. CAS-260135 "Contractor onboarding blocked on
     background check" for Nina Kowalski of Beacon Hill Staffing
     Partners; days-in-queue is real clock math. The HRIS workers
     collection is the live onboarding roster (25 workers AL-00xx with
     hire dates, departments, manager chains).
     Try: perform(operation="onboarding_checklist")
     to see the live roster joined with the open CRM clearance holds
     in one view.
  2. No network? Everything falls back to the embedded demo layer below
     (EMPLOYEES / ONBOARDING_STEPS / INVESTIGATION_TIMELINES) — the
     agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     WORKFORCE_CLEARANCE_ONBOARDING_DATA_URL (CRM) and
     WORKFORCE_CLEARANCE_ONBOARDING_HRIS_URL (HRIS) to your own
     endpoints, or replace _fetch_collection() with your own API
     client. Fields the rest of the file needs are listed in
     _normalize_live_case() / _normalize_roster_worker() — everything
     else keeps working untouched. Fields marked "enrichment seam" in
     the output (investigation tier, clearance level) are where you
     wire DCSA/eQIP.

OPERATIONS
  clearance_status | onboarding_checklist | background_check_tracker
  | access_provisioning
  kwargs: operation (required), employee_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "employee_id": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "clearance_status",
        "onboarding_checklist",
        "background_check_tracker",
        "access_provisioning"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `workforce_clearance_onboarding_agent.py` and embedded as the fenced Python below (sha256 181d78db4148c593…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `workforce_clearance_onboarding_agent.py` first:

```bash
python3 workforce_clearance_onboarding_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 workforce_clearance_onboarding_agent.py   # or on stdin
python3 workforce_clearance_onboarding_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Workforce Clearance & Onboarding Agent — a template you are meant to mutate.

Manages security clearance tracking, onboarding checklists, background
check status, and access provisioning for federal workforce management.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted systems (synthetic data, no credentials, works
     from anywhere):
       CRM  https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       HRIS https://kody-w.github.io/static-hris/api/v1/
     An onboarding or background-check hold is represented as a
     Dynamics case — e.g. CAS-260135 "Contractor onboarding blocked on
     background check" for Nina Kowalski of Beacon Hill Staffing
     Partners; days-in-queue is real clock math. The HRIS workers
     collection is the live onboarding roster (25 workers AL-00xx with
     hire dates, departments, manager chains).
     Try: perform(operation="onboarding_checklist")
     to see the live roster joined with the open CRM clearance holds
     in one view.
  2. No network? Everything falls back to the embedded demo layer below
     (EMPLOYEES / ONBOARDING_STEPS / INVESTIGATION_TIMELINES) — the
     agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     WORKFORCE_CLEARANCE_ONBOARDING_DATA_URL (CRM) and
     WORKFORCE_CLEARANCE_ONBOARDING_HRIS_URL (HRIS) to your own
     endpoints, or replace _fetch_collection() with your own API
     client. Fields the rest of the file needs are listed in
     _normalize_live_case() / _normalize_roster_worker() — everything
     else keeps working untouched. Fields marked "enrichment seam" in
     the output (investigation tier, clearance level) are where you
     wire DCSA/eQIP.

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
    "version": "1.2.0",
    "display_name": "Workforce Clearance & Onboarding Agent",
    "description": "Tracks onboarding blockers from a live simulated Dynamics 365 CRM joined to an HRIS hire roster, with clearance checklists that work offline.",
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
# TWO live sources, both synthetic OData-shaped JSON on GitHub Pages:
#   CRM  (Dynamics 365 — onboarding/clearance holds as cases):
#     export WORKFORCE_CLEARANCE_ONBOARDING_DATA_URL=...
#   HRIS (workers collection = the live onboarding roster):
#     export WORKFORCE_CLEARANCE_ONBOARDING_HRIS_URL=...
# or replace _fetch_collection() with your clients. Downstream code
# only needs the fields produced by _normalize_live_case() and
# _normalize_roster_worker().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "WORKFORCE_CLEARANCE_ONBOARDING_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
HRIS_SOURCE_URL = os.environ.get(
    "WORKFORCE_CLEARANCE_ONBOARDING_HRIS_URL",
    "https://kody-w.github.io/static-hris/api/v1",
)
_LIVE_CACHE = {}


def _fetch_collection(collection, timeout=6, base_url=None):
    """One bounded GET per URL per process. Returns [] on ANY
    failure — offline, DNS, bad JSON — so the demo layer takes over."""
    url = f"{base_url or DATA_SOURCE_URL}/{collection}.json"
    if url in _LIVE_CACHE:
        return _LIVE_CACHE[url]
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "rapp-agent-template/1.0"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            rows = json.loads(resp.read().decode("utf-8")).get("value", [])
    except Exception:
        rows = []
    _LIVE_CACHE[url] = rows
    return rows


def _fetch_hris(collection):
    """Fetch a collection from the sibling HRIS; [] when offline."""
    return _fetch_collection(collection, base_url=HRIS_SOURCE_URL)


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


def _normalize_roster_worker(row):
    """Project an HRIS worker onto the onboarding-roster shape this
    agent uses. Hire date, department, and manager are real HRIS
    fields; clearance level is not an HRIS concept here — it stays an
    enrichment seam (wire DCSA/eQIP)."""
    return {
        "worker_id": row.get("worker_id", ""),
        "name": row.get("full_name", "Unknown"),
        "title": row.get("job_title", ""),
        "department": row.get("department_name", ""),
        "hire_date": row.get("hire_date", ""),
        "days_since_hire": _days_since(row.get("hire_date")),  # real clock math
        "manager": row.get("manager_name", ""),
        "level": row.get("level", ""),
        "clearance_level": None,  # enrichment seam — wire DCSA/eQIP
        "_live": True,
    }


def _live_roster():
    """Live HRIS onboarding roster (workers, newest hires first); []
    when offline."""
    roster = [
        _normalize_roster_worker(row)
        for row in _fetch_hris("workers")
        if row.get("full_name") and row.get("status") == "active"
    ]
    return sorted(roster, key=lambda w: w["hire_date"], reverse=True)


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

        roster = _live_roster()
        if roster:
            recent = roster[:10]
            lines = ["# Onboarding Roster (live HRIS workers, joined to CRM holds)\n"]
            lines.append(f"**Active workers on the roster:** {len(roster)} "
                         f"(showing {len(recent)} most recent hires)\n")
            lines.append("## Most Recent Hires\n")
            lines.append("| Worker | Title | Department | Hire Date | Days Since Hire | Manager | Clearance |")
            lines.append("|---|---|---|---|---|---|---|")
            for w in recent:
                days = w["days_since_hire"] if w["days_since_hire"] is not None else "n/a"
                lines.append(
                    f"| {w['name']} ({w['worker_id']}) | {w['title']} ({w['level']}) "
                    f"| {w['department']} | {w['hire_date']} | {days} "
                    f"| {w['manager']} | n/a — enrichment seam |"
                )
            holds = [c for c in _live_onboarding_cases() if c["status"] == "open"]
            lines.append("\n## Open Onboarding/Clearance Holds (CRM join)\n")
            if holds:
                lines.append("| Case | Candidate | Issue | Opened | Days in Queue |")
                lines.append("|---|---|---|---|---|")
                for c in sorted(holds, key=lambda x: x["opened"]):
                    days = c["days_in_queue"] if c["days_in_queue"] is not None else "n/a"
                    lines.append(
                        f"| {c['id']} | {c['candidate']} | {c['issue']} "
                        f"| {c['opened']} | {days} |"
                    )
                roster_names = {w["name"].lower() for w in roster}
                matched = [c for c in holds
                           if str(c["candidate"]).lower() in roster_names]
                if matched:
                    lines.append(
                        f"\n{len(matched)} hold(s) match a roster worker by name."
                    )
                else:
                    lines.append(
                        "\nNo hold matches a roster worker by name — these are "
                        "candidate/staffing-partner cases still upstream of the "
                        "HRIS roster; the candidate-to-worker link is an "
                        "enrichment seam."
                    )
            else:
                lines.append("No open onboarding or clearance holds in the CRM.")
            lines.append("\n_Sources: live Static HRIS (workers = onboarding "
                         "roster; hire dates and days-since-hire are real clock "
                         "math) + live Static Dynamics 365 tenant (incidents = "
                         "onboarding/clearance holds)._")
            return "\n".join(lines)

        lines = ["# Onboarding Status Summary (embedded demo data — offline)\n"]
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
    print("LIVE HRIS ONBOARDING ROSTER + CRM CLEARANCE HOLDS (joined; falls back offline)")
    print(agent.perform(operation="onboarding_checklist"))
    print()
    print("=" * 60)
    print("EMBEDDED DEMO WORKFORCE (works offline)")
    print(agent.perform(operation="clearance_status"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="onboarding_checklist", employee_id="EMP-5001"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="access_provisioning", employee_id="EMP-5001"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
