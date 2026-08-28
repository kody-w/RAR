---
name: "rar-aibast-agents-library-deal-progression"
description: "Analyzes pipeline health and stalled deals from live opportunities in a simulated Dynamics 365 tenant, with an embedded offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/deal_progression", "rar_sha256": "71f69b7bf3a581b9a0549b696ac3730ffdddbf50fef3761bced7d0806f35b9a4", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["b2b", "sales", "deal-progression", "pipeline", "forecasting"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/deal_progression`. The original RAPP
agent is preserved byte-for-byte in `deal_progression_agent.py` and in the RCI capsule.

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

Deal Progression Agent — a template you are meant to mutate.

Tracks deal progression across the pipeline, flags stalled opportunities,
generates blocker-specific action plans, and produces executive-ready
pipeline health reports.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="pipeline_health") — the health report covers
     live open deals such as "Willow Brook Legal — Office sensor
     deployment", classified by CRM close probability and schedule slip.
  2. No network? Everything falls back to the embedded demo layer below
     (_PIPELINE / _BLOCKER_PLAYBOOK) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     DEAL_PROGRESSION_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with your own client. The dict shape the rest of
     the file needs is documented in _normalize_live_deal(). Blocker and
     champion intelligence is an enrichment seam — wire call/email
     analytics there; blocker-driven ops stay simulated until you do.

OPERATIONS
  pipeline_health | stalled_deals | action_plans | acceleration
  | assign_tasks | executive_summary | activate_action_plan
  kwargs: operation (required), opportunity_id (activate_action_plan)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The analysis to perform",
      "enum": [
        "pipeline_health",
        "stalled_deals",
        "action_plans",
        "acceleration",
        "assign_tasks",
        "executive_summary",
        "activate_action_plan"
      ],
      "type": "string"
    },
    "opportunity_id": {
      "description": "Exact opportunity ID for activate_action_plan (e.g. 'OPP-002')",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `deal_progression_agent.py` and embedded as the fenced Python below (sha256 71f69b7bf3a581b9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `deal_progression_agent.py` first:

```bash
python3 deal_progression_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 deal_progression_agent.py   # or on stdin
python3 deal_progression_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
Deal Progression Agent — a template you are meant to mutate.

Tracks deal progression across the pipeline, flags stalled opportunities,
generates blocker-specific action plans, and produces executive-ready
pipeline health reports.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="pipeline_health") — the health report covers
     live open deals such as "Willow Brook Legal — Office sensor
     deployment", classified by CRM close probability and schedule slip.
  2. No network? Everything falls back to the embedded demo layer below
     (_PIPELINE / _BLOCKER_PLAYBOOK) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     DEAL_PROGRESSION_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with your own client. The dict shape the rest of
     the file needs is documented in _normalize_live_deal(). Blocker and
     champion intelligence is an enrichment seam — wire call/email
     analytics there; blocker-driven ops stay simulated until you do.

OPERATIONS
  pipeline_health | stalled_deals | action_plans | acceleration
  | assign_tasks | executive_summary | activate_action_plan
  kwargs: operation (required), opportunity_id (activate_action_plan)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timedelta, timezone

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/deal_progression",
    "version": "1.2.0",
    "display_name": "Deal Progression",
    "description": "Analyzes pipeline health and stalled deals from live opportunities in a simulated Dynamics 365 tenant, with an embedded offline demo fallback.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "deal-progression", "pipeline", "forecasting"],
    "category": "b2b_sales",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export DEAL_PROGRESSION_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_deal().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "DEAL_PROGRESSION_DATA_URL",
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


_LIVE_STAGE_MAP = {"Qualify": "Qualification", "Develop": "Discovery",
                   "Propose": "Proposal", "Close": "Negotiation"}


def _days_overdue(iso_date):
    """Days past an ISO date (0 if in the future or unparseable)."""
    try:
        then = datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
        return max(0, (datetime.now(timezone.utc) - then).days)
    except (ValueError, TypeError):
        return 0


def _normalize_live_deal(row):
    """Project a Dynamics opportunity onto the shape this agent uses.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not knowable from the CRM alone' and the
    renderers label it an enrichment seam (wire call/email analytics for
    blocker and champion intelligence)."""
    return {
        "id": str(row.get("opportunityid", ""))[:8],
        "name": row.get("name", "Unknown"),
        "account": row.get("parentaccountidname", "Unknown"),
        "value": int(float(row.get("estimatedvalue") or 0)),
        "stage": _LIVE_STAGE_MAP.get(row.get("stepname"), "Qualification"),
        "owner": row.get("owneridname", ""),
        "probability": int(row.get("closeprobability") or 0),
        "days_past_est_close": _days_overdue(row.get("estimatedclosedate")),
        "champion_name": None,    # enrichment seam — wire your contact intel
        "champion_status": None,  # enrichment seam
        "blocker": None,          # enrichment seam — wire call analytics
        "_live": True,
    }


def _live_open_deals():
    """Live open opportunities normalized for this agent; [] when offline."""
    return [_normalize_live_deal(o) for o in _fetch_collection("opportunities")
            if o.get("statecode") == 0]


def _classify_live_deals(deals):
    """Classify live deals from CRM-visible signals: past the estimated
    close date = stalled; low close probability = at risk."""
    on_track, at_risk, stalled = [], [], []
    for d in deals:
        if d["days_past_est_close"] > 0:
            stalled.append(d)
        elif d["probability"] < 50:
            at_risk.append(d)
        else:
            on_track.append(d)
    return on_track, at_risk, stalled


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# Stands in for Salesforce, Gong, Clari, etc.
# ═══════════════════════════════════════════════════════════════

# Stage benchmarks — average days a healthy deal spends in each stage
_STAGE_BENCHMARKS = {
    "Qualification":  14,
    "Discovery":      18,
    "Proposal":       16,
    "Negotiation":    12,
    "Contract":       10,
}

# Sales team with capacity data
_REPS = [
    {"name": "Mike Chen",    "title": "Sr. Account Executive",  "active_deals": 11, "capacity": 14, "specialty": "executive alignment"},
    {"name": "Lisa Torres",  "title": "Account Executive",      "active_deals": 9,  "capacity": 12, "specialty": "contract negotiation"},
    {"name": "James Park",   "title": "Sr. Account Executive",  "active_deals": 12, "capacity": 14, "specialty": "technical sales"},
    {"name": "Sarah Kim",    "title": "Account Executive",      "active_deals": 8,  "capacity": 12, "specialty": "executive alignment"},
    {"name": "Ryan Davis",   "title": "Account Executive",      "active_deals": 7,  "capacity": 12, "specialty": "mid-market"},
]

# Full pipeline — 47 opportunities
_PIPELINE = [
    # ── Stalled deals (12) ──────────────────────────────────────
    {"id": "OPP-001", "name": "TechCorp Industries",     "account": "TechCorp Industries",     "value": 890_000, "stage": "Proposal",     "days_in_stage": 34, "owner": "Mike Chen",    "last_contact_days": 18, "champion_name": "VP IT - Mark Reynolds",        "champion_status": "Silent",           "blocker": "executive_change"},
    {"id": "OPP-002", "name": "Global Manufacturing",    "account": "Global Manufacturing",    "value": 720_000, "stage": "Negotiation",  "days_in_stage": 28, "owner": "Lisa Torres",  "last_contact_days": 5,  "champion_name": "Dir. Ops - Rachel Green",      "champion_status": "Active frustrated", "blocker": "legal_review"},
    {"id": "OPP-003", "name": "Apex Financial",          "account": "Apex Financial Group",    "value": 580_000, "stage": "Discovery",    "days_in_stage": 25, "owner": "James Park",   "last_contact_days": 12, "champion_name": "CTO - David Liu",              "champion_status": "Disengaged",       "blocker": "competitor_eval"},
    {"id": "OPP-004", "name": "Metro Healthcare",        "account": "Metro Health Systems",    "value": 440_000, "stage": "Proposal",     "days_in_stage": 22, "owner": "Mike Chen",    "last_contact_days": 9,  "champion_name": "VP Digital - Sandra Patel",    "champion_status": "Active",           "blocker": "budget_hold"},
    {"id": "OPP-005", "name": "Pinnacle Logistics",      "account": "Pinnacle Logistics Inc.", "value": 360_000, "stage": "Qualification","days_in_stage": 20, "owner": "James Park",   "last_contact_days": 14, "champion_name": "IT Dir - Tom Bradley",         "champion_status": "Silent",           "blocker": "no_champion"},
    {"id": "OPP-006", "name": "Summit Retail Group",     "account": "Summit Retail Group",     "value": 310_000, "stage": "Discovery",    "days_in_stage": 24, "owner": "Sarah Kim",    "last_contact_days": 11, "champion_name": "COO - Angela Morris",          "champion_status": "Lukewarm",         "blocker": "competitor_eval"},
    {"id": "OPP-007", "name": "Vanguard Energy",         "account": "Vanguard Energy Corp",    "value": 270_000, "stage": "Proposal",     "days_in_stage": 21, "owner": "Ryan Davis",   "last_contact_days": 16, "champion_name": "VP Eng - Carlos Reyes",        "champion_status": "Silent",           "blocker": "executive_change"},
    {"id": "OPP-008", "name": "Cascade Media",           "account": "Cascade Media Holdings",  "value": 220_000, "stage": "Negotiation",  "days_in_stage": 18, "owner": "Lisa Torres",  "last_contact_days": 7,  "champion_name": "Dir. Tech - Nina Chow",        "champion_status": "Active",           "blocker": "legal_review"},
    {"id": "OPP-009", "name": "Atlas Construction",      "account": "Atlas Construction Co.",  "value": 180_000, "stage": "Qualification","days_in_stage": 19, "owner": "James Park",   "last_contact_days": 20, "champion_name": "None identified",              "champion_status": "None",             "blocker": "no_champion"},
    {"id": "OPP-010", "name": "Horizon Pharma",          "account": "Horizon Pharmaceuticals", "value": 150_000, "stage": "Discovery",    "days_in_stage": 22, "owner": "Sarah Kim",    "last_contact_days": 13, "champion_name": "VP R&D - Greg Foster",         "champion_status": "Disengaged",       "blocker": "budget_hold"},
    {"id": "OPP-011", "name": "Sterling Insurance",      "account": "Sterling Insurance Co.",  "value": 130_000, "stage": "Proposal",     "days_in_stage": 20, "owner": "Mike Chen",    "last_contact_days": 15, "champion_name": "CIO - Barbara Wells",          "champion_status": "Lukewarm",         "blocker": "competitor_eval"},
    {"id": "OPP-012", "name": "Redwood Education",       "account": "Redwood Education Group", "value": 110_000, "stage": "Qualification","days_in_stage": 18, "owner": "Ryan Davis",   "last_contact_days": 10, "champion_name": "Dir. IT - Paul Simmons",       "champion_status": "Active",           "blocker": "budget_hold"},

    # ── At-risk deals (7) ───────────────────────────────────────
    {"id": "OPP-013", "name": "Pacific Telecom",         "account": "Pacific Telecom Inc.",    "value": 780_000, "stage": "Negotiation",  "days_in_stage": 14, "owner": "Lisa Torres",  "last_contact_days": 3,  "champion_name": "SVP Ops - Diana Cruz",         "champion_status": "Active",           "blocker": "procurement_process"},
    {"id": "OPP-014", "name": "Northstar Aerospace",     "account": "Northstar Aerospace",     "value": 650_000, "stage": "Proposal",     "days_in_stage": 17, "owner": "Mike Chen",    "last_contact_days": 4,  "champion_name": "VP IT - Kyle Jensen",          "champion_status": "Active",           "blocker": "technical_validation"},
    {"id": "OPP-015", "name": "Beacon Financial",        "account": "Beacon Financial Corp",   "value": 520_000, "stage": "Discovery",    "days_in_stage": 19, "owner": "James Park",   "last_contact_days": 6,  "champion_name": "CTO - Amy Nakamura",           "champion_status": "Active",           "blocker": "stakeholder_alignment"},
    {"id": "OPP-016", "name": "Crestline Hotels",        "account": "Crestline Hospitality",   "value": 480_000, "stage": "Qualification","days_in_stage": 15, "owner": "Sarah Kim",    "last_contact_days": 5,  "champion_name": "Dir. Digital - Frank Russo",   "champion_status": "Active",           "blocker": "timeline_uncertainty"},
    {"id": "OPP-017", "name": "Ironbridge Steel",        "account": "Ironbridge Steel Corp",   "value": 410_000, "stage": "Proposal",     "days_in_stage": 17, "owner": "Ryan Davis",   "last_contact_days": 4,  "champion_name": "VP Mfg - Helen Park",          "champion_status": "Active",           "blocker": "stakeholder_alignment"},
    {"id": "OPP-018", "name": "Emerald Biotech",         "account": "Emerald Biotech Ltd.",    "value": 370_000, "stage": "Negotiation",  "days_in_stage": 13, "owner": "Lisa Torres",  "last_contact_days": 2,  "champion_name": "CIO - Roger Tran",             "champion_status": "Active",           "blocker": "procurement_process"},
    {"id": "OPP-019", "name": "Sapphire Analytics",      "account": "Sapphire Analytics Inc.", "value": 290_000, "stage": "Discovery",    "days_in_stage": 19, "owner": "James Park",   "last_contact_days": 7,  "champion_name": "VP Data - Megan Lowe",         "champion_status": "Active",           "blocker": "technical_validation"},

    # ── On-track deals (24) ─────────────────────────────────────
    {"id": "OPP-020", "name": "DataFlow Corp",           "account": "DataFlow Corp",           "value": 340_000, "stage": "Contract",     "days_in_stage": 3,  "owner": "Lisa Torres",  "last_contact_days": 1,  "champion_name": "VP Eng - Steve Hall",          "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-021", "name": "Summit Industries",       "account": "Summit Industries Inc.",  "value": 280_000, "stage": "Contract",     "days_in_stage": 5,  "owner": "Mike Chen",    "last_contact_days": 1,  "champion_name": "CTO - Laura Adams",            "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-022", "name": "Tech Dynamics",           "account": "Tech Dynamics LLC",       "value": 190_000, "stage": "Contract",     "days_in_stage": 2,  "owner": "Sarah Kim",    "last_contact_days": 0,  "champion_name": "IT Dir - Ben Wright",          "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-023", "name": "Orion Software",          "account": "Orion Software Inc.",     "value": 420_000, "stage": "Negotiation",  "days_in_stage": 5,  "owner": "James Park",   "last_contact_days": 1,  "champion_name": "VP Prod - Jill Carter",        "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-024", "name": "Vertex Solutions",        "account": "Vertex Solutions Corp",   "value": 380_000, "stage": "Proposal",     "days_in_stage": 8,  "owner": "Ryan Davis",   "last_contact_days": 2,  "champion_name": "CIO - Dan Mitchell",           "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-025", "name": "Phoenix Consulting",      "account": "Phoenix Consulting Grp",  "value": 310_000, "stage": "Discovery",    "days_in_stage": 10, "owner": "Mike Chen",    "last_contact_days": 3,  "champion_name": "CEO - Tina Brooks",            "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-026", "name": "Cirrus Cloud Services",   "account": "Cirrus Cloud Services",   "value": 540_000, "stage": "Proposal",     "days_in_stage": 7,  "owner": "Lisa Torres",  "last_contact_days": 2,  "champion_name": "VP Infra - Raj Patel",         "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-027", "name": "Quantum Analytics",       "account": "Quantum Analytics LLC",   "value": 290_000, "stage": "Discovery",    "days_in_stage": 9,  "owner": "Sarah Kim",    "last_contact_days": 4,  "champion_name": "CTO - Eric Saunders",          "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-028", "name": "Bluewave Telecom",        "account": "Bluewave Telecom Inc.",   "value": 460_000, "stage": "Negotiation",  "days_in_stage": 6,  "owner": "James Park",   "last_contact_days": 1,  "champion_name": "SVP Tech - Maria Gonzalez",    "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-029", "name": "Granite Capital",         "account": "Granite Capital Mgmt",    "value": 350_000, "stage": "Qualification","days_in_stage": 7,  "owner": "Mike Chen",    "last_contact_days": 3,  "champion_name": "Dir. IT - Jake Morton",        "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-030", "name": "Silverline Media",        "account": "Silverline Media Group",  "value": 230_000, "stage": "Proposal",     "days_in_stage": 6,  "owner": "Ryan Davis",   "last_contact_days": 2,  "champion_name": "VP Tech - Olivia Hart",        "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-031", "name": "Trident Manufacturing",   "account": "Trident Mfg Corp",        "value": 510_000, "stage": "Negotiation",  "days_in_stage": 4,  "owner": "Lisa Torres",  "last_contact_days": 1,  "champion_name": "COO - William Chen",           "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-032", "name": "Falcon Logistics",        "account": "Falcon Logistics Inc.",   "value": 270_000, "stage": "Discovery",    "days_in_stage": 11, "owner": "Sarah Kim",    "last_contact_days": 3,  "champion_name": "VP Ops - Christine Lee",       "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-033", "name": "Prism Technologies",      "account": "Prism Technologies LLC",  "value": 390_000, "stage": "Proposal",     "days_in_stage": 9,  "owner": "James Park",   "last_contact_days": 2,  "champion_name": "CTO - Derek Nash",             "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-034", "name": "Keystone Health",         "account": "Keystone Health Corp",    "value": 320_000, "stage": "Qualification","days_in_stage": 8,  "owner": "Mike Chen",    "last_contact_days": 4,  "champion_name": "VP Digital - Susan Park",      "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-035", "name": "Neptune Shipping",        "account": "Neptune Shipping Co.",    "value": 180_000, "stage": "Discovery",    "days_in_stage": 6,  "owner": "Ryan Davis",   "last_contact_days": 2,  "champion_name": "CIO - Alan Foster",            "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-036", "name": "Ember Software",          "account": "Ember Software Inc.",     "value": 450_000, "stage": "Proposal",     "days_in_stage": 5,  "owner": "Lisa Torres",  "last_contact_days": 1,  "champion_name": "VP Eng - Kevin Zhao",          "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-037", "name": "Ridgeline Capital",       "account": "Ridgeline Capital Grp",   "value": 260_000, "stage": "Negotiation",  "days_in_stage": 3,  "owner": "Sarah Kim",    "last_contact_days": 1,  "champion_name": "Dir. Tech - Nancy White",      "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-038", "name": "Aurora Aerospace",        "account": "Aurora Aerospace Ltd.",   "value": 530_000, "stage": "Discovery",    "days_in_stage": 8,  "owner": "James Park",   "last_contact_days": 3,  "champion_name": "SVP Eng - Robert Kim",         "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-039", "name": "Cobalt Chemicals",        "account": "Cobalt Chemical Corp",    "value": 200_000, "stage": "Qualification","days_in_stage": 5,  "owner": "Mike Chen",    "last_contact_days": 2,  "champion_name": "VP IT - Dorothy Mills",        "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-040", "name": "Zenith Insurance",        "account": "Zenith Insurance Group",  "value": 340_000, "stage": "Proposal",     "days_in_stage": 4,  "owner": "Ryan Davis",   "last_contact_days": 1,  "champion_name": "CTO - Philip Grant",           "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-041", "name": "Legacy Healthcare",       "account": "Legacy Health Systems",   "value": 280_000, "stage": "Negotiation",  "days_in_stage": 7,  "owner": "Lisa Torres",  "last_contact_days": 2,  "champion_name": "Dir. Digital - Kelly Young",   "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-042", "name": "Pinnacle Software",       "account": "Pinnacle Software Inc.",  "value": 410_000, "stage": "Discovery",    "days_in_stage": 7,  "owner": "Sarah Kim",    "last_contact_days": 3,  "champion_name": "VP Prod - Brian Hughes",       "champion_status": "Active",           "blocker": "none"},
    {"id": "OPP-043", "name": "Titan Energy",            "account": "Titan Energy Corp",       "value": 370_000, "stage": "Proposal",     "days_in_stage": 10, "owner": "James Park",   "last_contact_days": 2,  "champion_name": "CIO - Martha Clark",           "champion_status": "Active",           "blocker": "none"},

    # ── Closed Won (3) — for velocity reference ────────────────
    {"id": "OPP-044", "name": "Axiom Partners",          "account": "Axiom Partners LLC",      "value": 520_000, "stage": "Closed Won",   "days_in_stage": 0,  "owner": "Mike Chen",    "last_contact_days": 0,  "champion_name": "CEO - Janet Rivera",           "champion_status": "Won",              "blocker": "none"},
    {"id": "OPP-045", "name": "Delta Dynamics",          "account": "Delta Dynamics Corp",     "value": 310_000, "stage": "Closed Won",   "days_in_stage": 0,  "owner": "Lisa Torres",  "last_contact_days": 0,  "champion_name": "VP Ops - Scott Morgan",        "champion_status": "Won",              "blocker": "none"},
    {"id": "OPP-046", "name": "Vector Analytics",        "account": "Vector Analytics Inc.",   "value": 190_000, "stage": "Closed Won",   "days_in_stage": 0,  "owner": "Sarah Kim",    "last_contact_days": 0,  "champion_name": "CTO - Lisa Brown",             "champion_status": "Won",              "blocker": "none"},

    # ── Closed Lost (1) — for context ──────────────────────────
    {"id": "OPP-047", "name": "Omega Systems",           "account": "Omega Systems Inc.",      "value": 430_000, "stage": "Closed Lost",  "days_in_stage": 0,  "owner": "James Park",   "last_contact_days": 0,  "champion_name": "VP IT - Chris Taylor",         "champion_status": "Lost",             "blocker": "competitor_won"},
]

_DEALS_BY_ID = {deal["id"]: deal for deal in _PIPELINE}

# Blocker-to-action mapping for action plan generation
_BLOCKER_PLAYBOOK = {
    "executive_change": {
        "diagnosis": "Champion disengaged, economic buyer changed",
        "week1": [
            "Day 1: Research new executive background (LinkedIn, news)",
            "Day 2: Call existing champion — acknowledge gap, request intro",
            "Day 3: Send executive-tailored ROI analysis",
            "Day 5: Executive sponsor outreach (your VP to their exec)",
        ],
        "week2": [
            "Schedule executive meeting with business case",
            "Re-present proposal with finance lens",
            "Establish new champion relationship",
        ],
        "resource": "exec alignment specialist",
    },
    "legal_review": {
        "diagnosis": "Process bottleneck, not relationship issue",
        "week1": [
            "Today: Call champion — acknowledge legal delay",
            "Tomorrow: Send pre-approved contract template (removes 80% of redlines)",
            "Day 3: Offer 30-day out clause to reduce perceived risk",
            "Day 5: Legal-to-legal call to resolve remaining items",
        ],
        "week2": [
            "Follow up on outstanding redline items",
            "Escalate any remaining blockers to VP Legal",
        ],
        "resource": "legal team fast-track review",
    },
    "competitor_eval": {
        "diagnosis": "Active competitive evaluation in progress",
        "week1": [
            "Day 1: Request competitive landscape details from champion",
            "Day 2: Prepare head-to-head comparison deck",
            "Day 3: Schedule technical deep-dive vs competitor capabilities",
            "Day 5: Deliver customer reference calls in same vertical",
        ],
        "week2": [
            "Provide proof-of-value pilot offer",
            "Executive peer reference call",
            "Submit best-and-final with differentiated terms",
        ],
        "resource": "competitive intelligence team",
    },
    "budget_hold": {
        "diagnosis": "Budget approval stalled or deprioritized",
        "week1": [
            "Day 1: Confirm budget timeline with champion",
            "Day 2: Build CFO-ready business case with 3-year TCO",
            "Day 3: Offer phased implementation to reduce upfront cost",
            "Day 5: Provide flexible payment terms proposal",
        ],
        "week2": [
            "Schedule CFO meeting with ROI walkthrough",
            "Share peer company case study with hard ROI numbers",
        ],
        "resource": "value engineering team",
    },
    "no_champion": {
        "diagnosis": "No internal champion identified or engaged",
        "week1": [
            "Day 1: Map org chart and identify 3 potential champions",
            "Day 2: Multi-thread outreach via LinkedIn and email",
            "Day 3: Offer executive briefing or lunch-and-learn",
            "Day 5: Ask existing contacts for warm introductions",
        ],
        "week2": [
            "Host on-site workshop to build relationships",
            "Provide industry insights to create value before selling",
            "Identify and cultivate power sponsor",
        ],
        "resource": "senior AE for relationship building",
    },
}


# ═══════════════════════════════════════════════════════════════
# HELPERS — real computation, synthetic inputs
# ═══════════════════════════════════════════════════════════════

_ACTIVE_STAGES = {"Qualification", "Discovery", "Proposal", "Negotiation", "Contract"}


def _active_pipeline():
    """Return only open, active-stage deals."""
    return [d for d in _PIPELINE if d["stage"] in _ACTIVE_STAGES]


def _classify_deals():
    """Classify every active deal as on_track, at_risk, or stalled."""
    on_track, at_risk, stalled = [], [], []
    for d in _active_pipeline():
        benchmark = _STAGE_BENCHMARKS.get(d["stage"], 14)
        ratio = d["days_in_stage"] / benchmark
        if ratio >= 1.25:
            stalled.append(d)
        elif ratio >= 1.0 or d["last_contact_days"] >= 10:
            at_risk.append(d)
        else:
            on_track.append(d)
    return on_track, at_risk, stalled


def _total_value(deals):
    """Sum opportunity values."""
    return sum(d["value"] for d in deals)


def _avg_days_stalled(deals):
    """Average days in stage beyond benchmark for a list of deals."""
    if not deals:
        return 0
    excess = []
    for d in deals:
        benchmark = _STAGE_BENCHMARKS.get(d["stage"], 14)
        excess.append(d["days_in_stage"] - benchmark)
    return round(sum(excess) / len(excess))


def _blocker_summary(stalled):
    """Group stalled deals by blocker type and count."""
    counts = {}
    for d in stalled:
        b = d["blocker"]
        label = {
            "executive_change": "Missing executive sponsor",
            "legal_review": "Legal / contract review",
            "competitor_eval": "Competitor evaluation ongoing",
            "budget_hold": "Budget approval pending",
            "no_champion": "No internal champion",
        }.get(b, b)
        counts[label] = counts.get(label, 0) + 1
    return counts


def _deals_by_owner(deals):
    """Group deals by rep name."""
    grouped = {}
    for d in deals:
        grouped.setdefault(d["owner"], []).append(d)
    return grouped


def _quick_wins():
    """Deals in Contract stage with recent contact — near close."""
    return [d for d in _active_pipeline()
            if d["stage"] == "Contract" and d["last_contact_days"] <= 3]


def _acceleration_opportunities():
    """Identify deals that can be pulled forward by intervention type."""
    active = _active_pipeline()
    exec_align = [d for d in active if d["stage"] in ("Proposal", "Negotiation")
                  and d["blocker"] in ("executive_change", "no_champion", "stakeholder_alignment", "none")
                  and d["days_in_stage"] >= 5]
    contract_fast = [d for d in active if d["blocker"] in ("legal_review", "procurement_process")
                     or d["stage"] == "Contract"]
    pov_offer = [d for d in active if d["blocker"] in ("competitor_eval", "technical_validation", "timeline_uncertainty")
                 or (d["stage"] == "Discovery" and d["days_in_stage"] >= 8)]
    return exec_align, contract_fast, pov_offer


def _rep_capacity():
    """Calculate rep capacity and stalled deal load."""
    _, _, stalled = _classify_deals()
    owner_stalled = _deals_by_owner(stalled)
    result = []
    for rep in _REPS:
        rep_stalled = owner_stalled.get(rep["name"], [])
        result.append({
            "name": rep["name"],
            "title": rep["title"],
            "active_deals": rep["active_deals"],
            "capacity": rep["capacity"],
            "available_slots": rep["capacity"] - rep["active_deals"],
            "stalled_count": len(rep_stalled),
            "stalled_value": _total_value(rep_stalled),
            "specialty": rep["specialty"],
        })
    return result


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class DealProgressionAgent(BasicAgent):
    """
    Tracks deal progression and accelerates pipeline velocity.

    Operations:
        pipeline_health    - full pipeline health with on-track / at-risk / stalled breakdown
        stalled_deals      - deep-dive into stalled deals with blocker analysis
        action_plans       - week-by-week action plans per stalled deal
        acceleration       - deals that can be pulled forward with targeted actions
        assign_tasks       - assign tasks to reps based on capacity
        executive_summary  - session summary with all findings and actions
        activate_action_plan - update one exact deal and notify its owner
    """

    def __init__(self):
        self.name = "DealProgressionAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "pipeline_health", "stalled_deals",
                            "action_plans", "acceleration",
                            "assign_tasks", "executive_summary",
                            "activate_action_plan",
                        ],
                        "description": "The analysis to perform",
                    },
                    "opportunity_id": {
                        "type": "string",
                        "description": "Exact opportunity ID for activate_action_plan (e.g. 'OPP-002')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "pipeline_health")
        if op == "activate_action_plan":
            return self._activate_action_plan(kwargs.get("opportunity_id"))
        dispatch = {
            "pipeline_health": self._pipeline_health,
            "stalled_deals": self._stalled_deals,
            "action_plans": self._action_plans,
            "acceleration": self._acceleration,
            "assign_tasks": self._assign_tasks,
            "executive_summary": self._executive_summary,
        }
        handler = dispatch.get(op)
        if not handler:
            return json.dumps({"status": "error", "message": f"Unknown operation: {op}"})
        return handler()

    def _activate_action_plan(self, opportunity_id):
        deal = _DEALS_BY_ID.get(opportunity_id)
        if deal is None:
            return json.dumps({
                "status": "error",
                "message": f"Unknown opportunity_id: {opportunity_id!r}",
                "valid_opportunity_ids": ", ".join(sorted(_DEALS_BY_ID)),
            })
        playbook = _BLOCKER_PLAYBOOK.get(deal["blocker"])
        if playbook is None:
            tasks = ["Confirm next milestone with the buyer", "Update forecast and follow-up date"]
            diagnosis = "No active blocker; maintain momentum"
        else:
            tasks = playbook["week1"] + playbook["week2"]
            diagnosis = playbook["diagnosis"]
        receipt = {
            "status": "simulated",
            "opportunity_id": opportunity_id,
            "account": deal["account"],
            "owner": deal["owner"],
            "diagnosis": diagnosis,
            "tasks_created": len(tasks),
            "first_task": tasks[0],
            "deadline": "10 days",
            "crm_update_id": f"sim-d365-plan-{opportunity_id.lower()}",
            "teams_message_id": f"sim-teams-owner-{opportunity_id.lower()}",
        }
        return "**Deal Action Plan Activation Receipt**\n\n```json\n" + json.dumps(receipt, indent=2) + "\n```"

    # ── pipeline_health (flagship: prefers LIVE tenant, falls back) ──
    def _pipeline_health(self):
        live = _live_open_deals()
        if live:
            on_track, at_risk, stalled = _classify_live_deals(live)
            total_value = _total_value(live)
            top_stalled = sorted(stalled, key=lambda x: -x["value"])[:4]
            return (
                f"**Pipeline Health Summary — {len(live)} LIVE Open Deals** "
                f"(Static Dynamics 365 tenant)\n\n"
                f"Analyzed **${total_value:,}** live pipeline.\n\n"
                f"| Status | Deals | Value | Signal |\n"
                f"|--------|-------|-------|--------|\n"
                f"| On Track | {len(on_track)} | ${_total_value(on_track):,} | prob >= 50%, on schedule |\n"
                f"| At Risk | {len(at_risk)} | ${_total_value(at_risk):,} | close probability < 50% |\n"
                f"| Stalled | {len(stalled)} | ${_total_value(stalled):,} | past estimated close date |\n\n"
                f"**Critical Stalled Deals (top {len(top_stalled)} by value):**\n\n"
                + "".join(
                    f"{i}. **{d['name']}** — ${d['value']:,} — "
                    f"{d['days_past_est_close']} days past estimated close "
                    f"({d['stage']}, prob {d['probability']}%, owner {d['owner']})\n"
                    for i, d in enumerate(top_stalled, 1)
                )
                + f"\n**Root Cause Analysis:** n/a — enrichment seam "
                f"(wire call/email analytics at the LIVE DATA SEAM)\n\n"
                f"Source: [Live Dynamics 365 opportunities]\n"
                f"Agents: PipelineAnalyticsAgent, StalledDealDetectionAgent"
            )
        on_track, at_risk, stalled = _classify_deals()
        active = _active_pipeline()
        total_value = _total_value(active)
        blockers = _blocker_summary(stalled)

        at_risk_avg = _avg_days_stalled(at_risk) if at_risk else 0
        stalled_avg = round(sum(d["days_in_stage"] for d in stalled) / max(len(stalled), 1))

        blocker_lines = "\n".join(f"- {count} deals: {label}" for label, count in
                                   sorted(blockers.items(), key=lambda x: -x[1]))

        return (
            f"**Pipeline Health Summary**\n\n"
            f"Analyzed **${total_value / 1_000_000:.1f}M** pipeline across **{len(active)}** active opportunities.\n\n"
            f"| Status | Deals | Value | Avg Days in Stage |\n"
            f"|--------|-------|-------|-------------------|\n"
            f"| On Track | {len(on_track)} | ${_total_value(on_track) / 1_000_000:.1f}M | within benchmark |\n"
            f"| At Risk | {len(at_risk)} | ${_total_value(at_risk) / 1_000_000:.1f}M | +{at_risk_avg} days over |\n"
            f"| Stalled | {len(stalled)} | ${_total_value(stalled) / 1_000_000:.1f}M | avg {stalled_avg} days |\n\n"
            f"**Critical Stalled Deals (top 4 by value):**\n\n"
            + "".join(
                f"{i}. **{d['name']}** — ${d['value']:,} — {d['days_in_stage']} days in {d['stage']}\n"
                for i, d in enumerate(sorted(stalled, key=lambda x: -x["value"])[:4], 1)
            )
            + f"\n**Root Cause Analysis:**\n{blocker_lines}\n\n"
            f"Source: [Salesforce + Activity Analytics]\n"
            f"Agents: PipelineAnalyticsAgent, StalledDealDetectionAgent"
        )

    # ── stalled_deals ─────────────────────────────────────────
    def _stalled_deals(self):
        _, _, stalled = _classify_deals()
        stalled_sorted = sorted(stalled, key=lambda x: -x["value"])

        sections = []
        for d in stalled_sorted:
            benchmark = _STAGE_BENCHMARKS.get(d["stage"], 14)
            multiplier = round(d["days_in_stage"] / benchmark, 1)
            playbook = _BLOCKER_PLAYBOOK.get(d["blocker"], {})
            diagnosis = playbook.get("diagnosis", d["blocker"].replace("_", " ").title())

            sections.append(
                f"**{d['name']} — ${d['value']:,}**\n\n"
                f"| Factor | Status |\n|--------|--------|\n"
                f"| Stage | {d['stage']} |\n"
                f"| Days stalled | {d['days_in_stage']} ({multiplier}x benchmark of {benchmark} days) |\n"
                f"| Last contact | {d['last_contact_days']} days ago |\n"
                f"| Champion | {d['champion_name']} ({d['champion_status']}) |\n"
                f"| Blocker | {d['blocker'].replace('_', ' ').title()} |\n\n"
                f"**Diagnosis:** {diagnosis}\n"
            )

        avg_velocity = 45  # benchmark close cycle
        return (
            f"**Stalled Deal Deep-Dive ({len(stalled)} deals, ${_total_value(stalled) / 1_000_000:.1f}M at risk)**\n\n"
            + "\n---\n\n".join(sections)
            + f"\n**Velocity Comparison:** Average deal closes in {avg_velocity} days — "
            f"stalled deals average {round(sum(d['days_in_stage'] for d in stalled) / len(stalled))} days in current stage alone.\n\n"
            f"Source: [CRM + Email Analytics + Meeting Logs]\n"
            f"Agents: DealDiagnosticsAgent, StalledDealDetectionAgent"
        )

    # ── action_plans ──────────────────────────────────────────
    def _action_plans(self):
        _, _, stalled = _classify_deals()
        stalled_sorted = sorted(stalled, key=lambda x: -x["value"])

        plans = []
        for d in stalled_sorted:
            playbook = _BLOCKER_PLAYBOOK.get(d["blocker"])
            if not playbook:
                continue

            week1 = "\n".join(f"- {task}" for task in playbook["week1"])
            week2 = "\n".join(f"- {task}" for task in playbook["week2"])

            plans.append(
                f"**{d['name']} — ${d['value']:,} ({d['stage']})**\n\n"
                f"**Week 1:**\n{week1}\n\n"
                f"**Week 2:**\n{week2}\n\n"
                f"**Assigned Resource:** {playbook['resource'].title()}\n"
                f"**Owner:** {d['owner']}\n"
                f"**Expected Outcome:** Deal back on track within 10 days\n"
            )

        total_tasks = sum(
            len(_BLOCKER_PLAYBOOK.get(d["blocker"], {}).get("week1", []))
            + len(_BLOCKER_PLAYBOOK.get(d["blocker"], {}).get("week2", []))
            for d in stalled_sorted if d["blocker"] in _BLOCKER_PLAYBOOK
        )

        return (
            f"**Action Plans — {len(plans)} Stalled Deals**\n\n"
            f"Total tasks generated: **{total_tasks}**\n\n"
            + "\n---\n\n".join(plans)
            + f"\nSource: [Sales Playbook + Win Patterns]\n"
            f"Agents: NextBestActionAgent"
        )

    # ── acceleration ──────────────────────────────────────────
    def _acceleration(self):
        exec_align, contract_fast, pov_offer = _acceleration_opportunities()
        quick = _quick_wins()

        rows = (
            f"| Executive alignment | {len(exec_align)} | "
            f"${_total_value(exec_align) / 1_000_000:.1f}M | 12 days avg |\n"
            f"| Contract fast-track | {len(contract_fast)} | "
            f"${_total_value(contract_fast) / 1_000_000:.1f}M | 8 days avg |\n"
            f"| Proof-of-value offer | {len(pov_offer)} | "
            f"${_total_value(pov_offer) / 1_000_000:.1f}M | 15 days avg |\n"
        )

        quick_lines = "".join(
            f"- **{d['name']}:** ${d['value']:,} — "
            f"{'verbal commit, awaiting signature' if d['days_in_stage'] <= 3 else 'final approval pending'}\n"
            for d in sorted(quick, key=lambda x: -x["value"])
        )

        quick_total = _total_value(quick)
        combined_value = _total_value(exec_align) + _total_value(contract_fast) + _total_value(pov_offer)

        # Rep-level stalled summary
        _, _, stalled = _classify_deals()
        rep_stalled = _deals_by_owner(stalled)
        rep_rows = ""
        for rep in _REPS:
            rep_deals = rep_stalled.get(rep["name"], [])
            if rep_deals:
                top_blocker = max(
                    set(d["blocker"] for d in rep_deals),
                    key=lambda b: sum(1 for d in rep_deals if d["blocker"] == b),
                )
                action = {
                    "executive_change": "Executive introductions",
                    "legal_review": "Contract negotiations",
                    "competitor_eval": "Competitive positioning",
                    "budget_hold": "ROI business cases",
                    "no_champion": "Re-engagement campaign",
                }.get(top_blocker, "Deal acceleration")
                rep_rows += f"| {rep['name']} | {len(rep_deals)} | {action} |\n"

        return (
            f"**Pipeline Acceleration Strategy**\n\n"
            f"Identified **${combined_value / 1_000_000:.1f}M** that can be pulled forward "
            f"with targeted interventions.\n\n"
            f"**Acceleration Opportunities:**\n\n"
            f"| Action | Deals Impacted | Value | Days Saved |\n"
            f"|--------|----------------|-------|------------|\n"
            f"{rows}\n"
            f"**Quick Wins (Close This Week):**\n{quick_lines}\n"
            f"Quick-win total: **${quick_total / 1_000_000:.1f}M**\n\n"
            f"**Rep-Level Actions:**\n\n"
            f"| Rep | Stalled Deals | Priority Action |\n"
            f"|-----|---------------|----------------|\n"
            f"{rep_rows}\n"
            f"**Forecast Impact:** Accelerating these deals adds "
            f"**$2.4M** to Q4 commit.\n\n"
            f"Source: [Pipeline Analytics + Historical Patterns]\n"
            f"Agents: PipelineAccelerationAgent"
        )

    # ── assign_tasks ──────────────────────────────────────────
    def _assign_tasks(self):
        _, _, stalled = _classify_deals()
        rep_stalled = _deals_by_owner(stalled)
        caps = _rep_capacity()

        # Calculate tasks per rep based on their stalled deals and playbook
        assignments = []
        total_tasks = 0
        for rc in caps:
            rep_deals = rep_stalled.get(rc["name"], [])
            task_count = 0
            for d in rep_deals:
                pb = _BLOCKER_PLAYBOOK.get(d["blocker"], {})
                task_count += len(pb.get("week1", [])) + len(pb.get("week2", []))
            # Support reps get tasks from cross-assignment
            if task_count == 0 and rc["specialty"] == "executive alignment" and rc["available_slots"] > 2:
                task_count = 3  # exec support tasks
            total_tasks += task_count
            if task_count > 0:
                deadline = "This week" if rc["stalled_count"] <= 2 else f"Next {min(rc['stalled_count'] * 2, 7)} days"
                role_note = f"{rc['stalled_count']} stalled" if rc["stalled_count"] > 0 else "Exec support"
                assignments.append({
                    "name": rc["name"],
                    "tasks": task_count,
                    "deadline": deadline,
                    "deals": role_note,
                })

        table = "".join(
            f"| {a['name']} | {a['tasks']} tasks | {a['deadline']} | {a['deals']} |\n"
            for a in assignments
        )

        return (
            f"**Task Assignments Completed**\n\n"
            f"**{total_tasks}** tasks assigned across **{len(assignments)}** reps.\n\n"
            f"| Rep | Tasks | Deadline | Deals |\n"
            f"|-----|-------|----------|-------|\n"
            f"{table}\n"
            f"**Automated Monitoring:**\n"
            f"- Daily Slack alerts for overdue tasks\n"
            f"- Deal stage change notifications\n"
            f"- Weekly pipeline velocity report\n"
            f"- Stall warning at 7 days (vs current 21)\n\n"
            f"**Accountability Cadence:**\n"
            f"- Daily: Automated task reminders\n"
            f"- Wednesday: Pipeline review meeting (30 min)\n"
            f"- Friday: Deal progression scorecard\n\n"
            f"**Success Metrics:**\n"
            f"- Target: Reduce avg stall time from 21 to 10 days\n"
            f"- Goal: Move ${_total_value(stalled) / 1_000_000:.1f}M stalled back to active\n"
            f"- Forecast: Add $2.4M to Q4 commit\n\n"
            f"Source: [Salesforce + Task Management]\n"
            f"Agents: TaskAssignmentAgent"
        )

    # ── executive_summary ─────────────────────────────────────
    def _executive_summary(self):
        on_track, at_risk, stalled = _classify_deals()
        active = _active_pipeline()
        total_val = _total_value(active)
        stalled_val = _total_value(stalled)
        quick = _quick_wins()
        quick_val = _total_value(quick)
        blockers = _blocker_summary(stalled)

        # Count total tasks
        total_tasks = 0
        for d in stalled:
            pb = _BLOCKER_PLAYBOOK.get(d["blocker"], {})
            total_tasks += len(pb.get("week1", [])) + len(pb.get("week2", []))

        blocker_labels = ", ".join(
            label.lower() for label, _ in sorted(blockers.items(), key=lambda x: -x[1])[:3]
        )

        top_stalled = sorted(stalled, key=lambda x: -x["value"])[:2]
        immediate_lines = ""
        if quick:
            immediate_lines += f"- ${quick_val / 1_000:,.0f}K in quick wins closing this week\n"
        for d in top_stalled:
            immediate_lines += f"- {d['name']} (${d['value']:,}) action plan activated\n"
        immediate_lines += f"- All {len(stalled)} stalled deals have intervention plans\n"

        on_track_pct = round(len(on_track) / max(len(active), 1) * 100)
        target_pct = min(on_track_pct + 18, 95)

        return (
            f"**Pipeline Acceleration Program — Executive Summary**\n\n"
            f"| Analysis | Result |\n"
            f"|----------|--------|\n"
            f"| Pipeline analyzed | ${total_val / 1_000_000:.1f}M across {len(active)} deals |\n"
            f"| Stalled identified | {len(stalled)} deals, ${stalled_val / 1_000_000:.1f}M at risk |\n"
            f"| Root causes | {blocker_labels} |\n"
            f"| Actions created | {total_tasks} specific tasks assigned |\n"
            f"| Acceleration target | ${(_total_value(stalled) + _total_value(at_risk)) / 1_000_000:.1f}M can be pulled forward |\n\n"
            f"**Immediate Impact:**\n{immediate_lines}\n"
            f"**Process Improvements:**\n"
            f"- Early warning at 7 days (was 21)\n"
            f"- Daily automated task tracking\n"
            f"- Weekly velocity reviews scheduled\n"
            f"- Rep accountability scorecard active\n\n"
            f"**Expected Outcomes:**\n"
            f"- Reduce stall time: 21 days to 10 days\n"
            f"- Q4 forecast improvement: +$2.4M commit\n"
            f"- Pipeline health: {target_pct}% on-track (from {on_track_pct}%)\n\n"
            f"Source: [All Pipeline Systems]\n"
            f"Agents: PipelineReportAgent (orchestrating all agents)"
        )


if __name__ == "__main__":
    agent = DealProgressionAgent()
    print("=" * 70)
    print("LIVE TENANT PIPELINE (fetched over HTTP; embedded demo offline)")
    print(agent.perform(operation="pipeline_health"))
    print()
    print("=" * 70)
    print("EMBEDDED DEMO (works offline, simulated)")
    print(agent.perform(operation="stalled_deals"))
    print()
    print("=" * 70)
    print(agent.perform(operation="executive_summary"))
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
