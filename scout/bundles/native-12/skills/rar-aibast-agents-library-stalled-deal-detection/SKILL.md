---
name: "rar-aibast-agents-library-stalled-deal-detection"
description: "Detects stalled deals from live opportunities in a simulated Dynamics 365 tenant using real CRM dates, with an embedded offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/stalled_deal_detection", "rar_sha256": "f1252b80c13fec14bd4043a2c4365aaf46b9ebc1e2a428ecd5c82582ef8e634a", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["b2b", "sales", "stalled-deals", "deal-progression", "pipeline"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/stalled_deal_detection`. The original RAPP
agent is preserved byte-for-byte in `stalled_deal_detection_agent.py` and in the RCI capsule.

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

Stalled Deal Detection Agent — a template you are meant to mutate.

Detects stalled deals against thresholds, classifies root causes,
generates day-by-day intervention plans, and surfaces leading indicators
for stall prevention.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="detect_stalls") — live open deals such as
     "Juniper Ridge Furnishings — Document capture modernization" are
     flagged from real CRM dates (days past estimated close, days since
     the record was last touched).
  2. No network? Everything falls back to the embedded demo layer below
     (_DEAL_TIMELINES / _INTERVENTION_PLAYBOOKS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     STALLED_DEAL_DETECTION_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON you export from Salesforce/HubSpot), or
     replace _fetch_collection() with your own client. The dict shape the
     rest of the file needs is documented in _normalize_live_deal().
     Blocker and champion status are enrichment seams — wire call/email
     analytics there; blocker-driven ops stay simulated until you do.

OPERATIONS
  detect_stalls | root_cause_analysis | intervention_plan | stall_prevention
  kwargs: operation (required)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The analysis to perform",
      "enum": [
        "detect_stalls",
        "root_cause_analysis",
        "intervention_plan",
        "stall_prevention"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `stalled_deal_detection_agent.py` and embedded as the fenced Python below (sha256 f1252b80c13fec14…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `stalled_deal_detection_agent.py` first:

```bash
python3 stalled_deal_detection_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 stalled_deal_detection_agent.py   # or on stdin
python3 stalled_deal_detection_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Stalled Deal Detection Agent — a template you are meant to mutate.

Detects stalled deals against thresholds, classifies root causes,
generates day-by-day intervention plans, and surfaces leading indicators
for stall prevention.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="detect_stalls") — live open deals such as
     "Juniper Ridge Furnishings — Document capture modernization" are
     flagged from real CRM dates (days past estimated close, days since
     the record was last touched).
  2. No network? Everything falls back to the embedded demo layer below
     (_DEAL_TIMELINES / _INTERVENTION_PLAYBOOKS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     STALLED_DEAL_DETECTION_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON you export from Salesforce/HubSpot), or
     replace _fetch_collection() with your own client. The dict shape the
     rest of the file needs is documented in _normalize_live_deal().
     Blocker and champion status are enrichment seams — wire call/email
     analytics there; blocker-driven ops stay simulated until you do.

OPERATIONS
  detect_stalls | root_cause_analysis | intervention_plan | stall_prevention
  kwargs: operation (required)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timezone

# ===================================================================
# RAPP AGENT MANIFEST
# ===================================================================
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/stalled_deal_detection",
    "version": "1.1.0",
    "display_name": "Stalled Deal Detection",
    "description": "Detects stalled deals from live opportunities in a simulated Dynamics 365 tenant using real CRM dates, with an embedded offline demo fallback.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "stalled-deals", "deal-progression", "pipeline"],
    "category": "b2b_sales",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ===================================================================
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export STALLED_DEAL_DETECTION_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_deal().
# ===================================================================

DATA_SOURCE_URL = os.environ.get(
    "STALLED_DEAL_DETECTION_DATA_URL",
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


def _days_since(iso_date):
    """Days since an ISO date (0 if in the future or unparseable)."""
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
    blocker and champion signals)."""
    return {
        "deal_id": str(row.get("opportunityid", ""))[:8],
        "name": row.get("name", "Unknown"),
        "account": row.get("parentaccountidname", "Unknown"),
        "value": int(float(row.get("estimatedvalue") or 0)),
        "stage": _LIVE_STAGE_MAP.get(row.get("stepname"), "Qualification"),
        "owner": row.get("owneridname", ""),
        "days_past_est_close": _days_since(row.get("estimatedclosedate")),
        "days_since_update": _days_since(row.get("modifiedon")),
        "champion": None,          # enrichment seam — wire contact intel
        "champion_status": None,   # enrichment seam
        "blocker": None,           # enrichment seam — wire call analytics
        "next_step": None,         # enrichment seam
        "_live": True,
    }


def _live_open_deals():
    """Live open opportunities normalized for this agent; [] when offline."""
    return [_normalize_live_deal(o) for o in _fetch_collection("opportunities")
            if o.get("statecode") == 0]


def _classify_live_stall(deal):
    """Classify a live deal from CRM-visible dates only."""
    if deal["days_past_est_close"] > 30 or deal["days_since_update"] > 60:
        return "CRITICAL"
    if deal["days_past_est_close"] > 0:
        return "STALLED"
    if deal["days_since_update"] > 21:
        return "WARNING"
    return "ON TRACK"


# ===================================================================
# EMBEDDED DEMO LAYER (offline fallback)
# ===================================================================

_STAGE_THRESHOLDS = {
    "Qualification": {"warning": 12, "stalled": 18, "critical": 25},
    "Discovery": {"warning": 15, "stalled": 22, "critical": 30},
    "Proposal": {"warning": 14, "stalled": 20, "critical": 28},
    "Negotiation": {"warning": 10, "stalled": 16, "critical": 24},
    "Contract": {"warning": 8, "stalled": 14, "critical": 20},
}

_DEAL_TIMELINES = {
    "TechCorp Industries": {
        "deal_id": "OPP-001", "value": 890000, "stage": "Proposal", "owner": "Mike Chen",
        "days_in_stage": 34, "last_contact_days": 18, "last_meeting_days": 22,
        "champion": "VP IT - Mark Reynolds", "champion_status": "Silent",
        "activities_last_14d": 2, "activities_prior_14d": 8,
        "blocker": "executive_change", "next_step": "None scheduled",
        "stage_history": [
            {"stage": "Qualification", "days": 12, "outcome": "advanced"},
            {"stage": "Discovery", "days": 16, "outcome": "advanced"},
            {"stage": "Proposal", "days": 34, "outcome": "stalled"},
        ],
    },
    "Global Manufacturing": {
        "deal_id": "OPP-002", "value": 720000, "stage": "Negotiation", "owner": "Lisa Torres",
        "days_in_stage": 28, "last_contact_days": 5, "last_meeting_days": 8,
        "champion": "Dir. Ops - Rachel Green", "champion_status": "Active frustrated",
        "activities_last_14d": 6, "activities_prior_14d": 9,
        "blocker": "legal_review", "next_step": "Legal redline review scheduled",
        "stage_history": [
            {"stage": "Qualification", "days": 10, "outcome": "advanced"},
            {"stage": "Discovery", "days": 15, "outcome": "advanced"},
            {"stage": "Proposal", "days": 14, "outcome": "advanced"},
            {"stage": "Negotiation", "days": 28, "outcome": "stalled"},
        ],
    },
    "Apex Financial": {
        "deal_id": "OPP-003", "value": 580000, "stage": "Discovery", "owner": "James Park",
        "days_in_stage": 25, "last_contact_days": 12, "last_meeting_days": 18,
        "champion": "CTO - David Liu", "champion_status": "Disengaged",
        "activities_last_14d": 1, "activities_prior_14d": 5,
        "blocker": "competitor_eval", "next_step": "None scheduled",
        "stage_history": [
            {"stage": "Qualification", "days": 11, "outcome": "advanced"},
            {"stage": "Discovery", "days": 25, "outcome": "stalled"},
        ],
    },
    "Metro Healthcare": {
        "deal_id": "OPP-004", "value": 440000, "stage": "Proposal", "owner": "Mike Chen",
        "days_in_stage": 22, "last_contact_days": 9, "last_meeting_days": 12,
        "champion": "VP Digital - Sandra Patel", "champion_status": "Active",
        "activities_last_14d": 4, "activities_prior_14d": 6,
        "blocker": "budget_hold", "next_step": "Board meeting next month",
        "stage_history": [
            {"stage": "Qualification", "days": 9, "outcome": "advanced"},
            {"stage": "Discovery", "days": 14, "outcome": "advanced"},
            {"stage": "Proposal", "days": 22, "outcome": "stalled"},
        ],
    },
    "Pinnacle Logistics": {
        "deal_id": "OPP-005", "value": 360000, "stage": "Qualification", "owner": "James Park",
        "days_in_stage": 20, "last_contact_days": 14, "last_meeting_days": 18,
        "champion": "IT Dir - Tom Bradley", "champion_status": "Silent",
        "activities_last_14d": 1, "activities_prior_14d": 3,
        "blocker": "no_champion", "next_step": "None scheduled",
        "stage_history": [
            {"stage": "Qualification", "days": 20, "outcome": "stalled"},
        ],
    },
    "Summit Retail Group": {
        "deal_id": "OPP-006", "value": 310000, "stage": "Discovery", "owner": "Sarah Kim",
        "days_in_stage": 24, "last_contact_days": 11, "last_meeting_days": 15,
        "champion": "COO - Angela Morris", "champion_status": "Lukewarm",
        "activities_last_14d": 2, "activities_prior_14d": 5,
        "blocker": "competitor_eval", "next_step": "Competitive comparison pending",
        "stage_history": [
            {"stage": "Qualification", "days": 8, "outcome": "advanced"},
            {"stage": "Discovery", "days": 24, "outcome": "stalled"},
        ],
    },
    "Vanguard Energy": {
        "deal_id": "OPP-007", "value": 270000, "stage": "Proposal", "owner": "Ryan Davis",
        "days_in_stage": 21, "last_contact_days": 16, "last_meeting_days": 20,
        "champion": "VP Eng - Carlos Reyes", "champion_status": "Silent",
        "activities_last_14d": 1, "activities_prior_14d": 4,
        "blocker": "executive_change", "next_step": "None scheduled",
        "stage_history": [
            {"stage": "Qualification", "days": 10, "outcome": "advanced"},
            {"stage": "Discovery", "days": 12, "outcome": "advanced"},
            {"stage": "Proposal", "days": 21, "outcome": "stalled"},
        ],
    },
}

_ROOT_CAUSE_TAXONOMY = {
    "executive_change": {"category": "Organizational", "severity": "critical",
                         "description": "Executive leadership change disrupted buying process",
                         "recovery_probability": 0.45, "avg_recovery_days": 18},
    "legal_review": {"category": "Process", "severity": "high",
                     "description": "Legal and contract review creating bottleneck",
                     "recovery_probability": 0.75, "avg_recovery_days": 10},
    "competitor_eval": {"category": "Competitive", "severity": "high",
                        "description": "Active competitive evaluation extended decision timeline",
                        "recovery_probability": 0.55, "avg_recovery_days": 14},
    "budget_hold": {"category": "Financial", "severity": "high",
                    "description": "Budget approval stalled or deprioritized",
                    "recovery_probability": 0.60, "avg_recovery_days": 20},
    "no_champion": {"category": "Relationship", "severity": "critical",
                    "description": "No internal champion to drive deal forward",
                    "recovery_probability": 0.35, "avg_recovery_days": 22},
}

_INTERVENTION_PLAYBOOKS = {
    "executive_change": {
        "day_1": "Research new executive via LinkedIn, company announcements",
        "day_2": "Contact existing champion for intel on new leadership priorities",
        "day_3": "Prepare executive-tailored value proposition",
        "day_5": "VP-to-VP outreach to new executive",
        "day_7": "Send industry insight piece to build credibility",
        "day_10": "Schedule executive briefing meeting",
        "day_14": "Present revised business case to new stakeholders",
    },
    "legal_review": {
        "day_1": "Send pre-approved contract template to reduce redlines",
        "day_2": "Schedule legal-to-legal call",
        "day_3": "Offer 30-day out clause to reduce perceived risk",
        "day_5": "Follow up on outstanding redline items",
        "day_7": "Escalate remaining items to VP Legal",
        "day_10": "Present final contract for signature",
    },
    "competitor_eval": {
        "day_1": "Request competitive landscape details from champion",
        "day_2": "Prepare head-to-head comparison deck",
        "day_3": "Schedule technical deep-dive vs competitor",
        "day_5": "Deliver customer reference calls in same vertical",
        "day_7": "Offer differentiated proof-of-value pilot",
        "day_10": "Submit best-and-final with differentiated terms",
    },
    "budget_hold": {
        "day_1": "Confirm budget timeline with champion",
        "day_2": "Build CFO-ready business case with 3-year TCO",
        "day_3": "Offer phased implementation to reduce upfront cost",
        "day_5": "Provide flexible payment terms proposal",
        "day_7": "Schedule CFO meeting with ROI walkthrough",
        "day_10": "Share peer company case study with hard ROI",
    },
    "no_champion": {
        "day_1": "Map org chart and identify 3 potential champions",
        "day_2": "Multi-thread outreach via LinkedIn and email",
        "day_3": "Offer executive briefing or lunch-and-learn",
        "day_5": "Ask existing contacts for warm introductions",
        "day_7": "Host on-site workshop to build relationships",
        "day_10": "Provide industry insights to create value",
        "day_14": "Evaluate deal viability if no champion emerges",
    },
}


# ===================================================================
# HELPERS
# ===================================================================

def _classify_stall(deal):
    """Classify deal stall severity based on thresholds."""
    stage = deal["stage"]
    days = deal["days_in_stage"]
    thresholds = _STAGE_THRESHOLDS.get(stage, {"warning": 14, "stalled": 20, "critical": 28})

    if days >= thresholds["critical"]:
        return "CRITICAL"
    if days >= thresholds["stalled"]:
        return "STALLED"
    if days >= thresholds["warning"]:
        return "WARNING"
    return "ON TRACK"


def _activity_trend(deal):
    """Calculate activity trend direction."""
    recent = deal["activities_last_14d"]
    prior = deal["activities_prior_14d"]
    if prior == 0:
        return "no_baseline"
    change = (recent - prior) / prior
    if change <= -0.5:
        return "sharp_decline"
    if change < 0:
        return "declining"
    if change > 0.5:
        return "increasing"
    return "stable"


def _stall_probability(deal):
    """Calculate probability of deal stalling further."""
    base = 50
    if deal["last_contact_days"] >= 14:
        base += 20
    if deal["champion_status"] in ("Silent", "Disengaged"):
        base += 15
    trend = _activity_trend(deal)
    if trend in ("sharp_decline", "declining"):
        base += 10
    if deal["next_step"] == "None scheduled":
        base += 10
    return min(95, base)


# ===================================================================
# AGENT CLASS
# ===================================================================

class StalledDealDetectionAgent(BasicAgent):
    """
    Detects and manages stalled deals in the pipeline.

    Operations:
        detect_stalls      - identify all stalled and at-risk deals
        root_cause_analysis - classify root causes of stalls
        intervention_plan  - day-by-day intervention plans per deal
        stall_prevention   - leading indicators and prevention recommendations
    """

    def __init__(self):
        self.name = "StalledDealDetectionAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["detect_stalls", "root_cause_analysis", "intervention_plan", "stall_prevention"],
                        "description": "The analysis to perform",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "detect_stalls")
        dispatch = {
            "detect_stalls": self._detect_stalls,
            "root_cause_analysis": self._root_cause_analysis,
            "intervention_plan": self._intervention_plan,
            "stall_prevention": self._stall_prevention,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"**Error:** Unknown operation '{op}'. Valid: {', '.join(dispatch.keys())}"
        return handler()

    # -- detect_stalls (flagship: prefers LIVE tenant, falls back) ------
    def _detect_stalls(self) -> str:
        live = _live_open_deals()
        if live:
            rows = ""
            stalled_value = 0
            warning_value = 0
            stalled_ct = 0
            warning_ct = 0
            for d in sorted(live, key=lambda x: -x["value"]):
                status = _classify_live_stall(d)
                if status in ("CRITICAL", "STALLED"):
                    stalled_ct += 1
                    stalled_value += d["value"]
                elif status == "WARNING":
                    warning_ct += 1
                    warning_value += d["value"]
                rows += (f"| {d['name']} | ${d['value']:,} | {d['stage']} | "
                         f"{d['days_past_est_close']}d | {d['days_since_update']}d | "
                         f"{status} | n/a — enrichment seam |\n")
            return (
                f"**Stalled Deal Detection Report — {len(live)} LIVE Open Deals** "
                f"(Static Dynamics 365 tenant)\n\n"
                f"Stalled/Critical: **{stalled_ct}** (${stalled_value:,}) | "
                f"Warning: **{warning_ct}** (${warning_value:,})\n\n"
                f"| Deal | Value | Stage | Past Est. Close | Since Last Update | Status | Champion |\n"
                f"|------|-------|-------|----------------|-------------------|--------|----------|\n"
                f"{rows}\n"
                f"**Detection Signals (CRM dates only):** past estimated close date = stalled; "
                f">30d past or >60d untouched = critical; >21d untouched = warning. "
                f"Champion/blocker signals stay n/a until you wire call analytics "
                f"at the LIVE DATA SEAM.\n\n"
                f"Source: [Live Dynamics 365 opportunities]\n"
                f"Agents: StallDetectionEngine"
            )
        stalled = []
        warning = []
        for deal_name, deal in _DEAL_TIMELINES.items():
            status = _classify_stall(deal)
            if status in ("CRITICAL", "STALLED"):
                stalled.append((deal_name, deal, status))
            elif status == "WARNING":
                warning.append((deal_name, deal, status))

        rows = ""
        for name, deal, status in sorted(stalled + warning, key=lambda x: -(x[1]["value"])):
            rows += (f"| {name} | ${deal['value']:,} | {deal['stage']} | {deal['days_in_stage']}d | "
                     f"{status} | {deal['last_contact_days']}d | {deal['champion_status']} |\n")

        stalled_value = sum(d["value"] for _, d, s in stalled)
        warning_value = sum(d["value"] for _, d, s in warning)

        return (
            f"**Stalled Deal Detection Report**\n\n"
            f"Stalled: **{len(stalled)}** deals (${stalled_value:,}) | "
            f"Warning: **{len(warning)}** deals (${warning_value:,})\n\n"
            f"| Deal | Value | Stage | Days in Stage | Status | Last Contact | Champion |\n"
            f"|------|-------|-------|--------------|--------|-------------|----------|\n"
            f"{rows}\n"
            f"**Detection Thresholds:**\n"
            + "\n".join(f"- {stage}: Warning={t['warning']}d, Stalled={t['stalled']}d, Critical={t['critical']}d"
                        for stage, t in _STAGE_THRESHOLDS.items())
            + f"\n\nSource: [CRM Pipeline Data + Activity Logs]\n"
            f"Agents: StallDetectionEngine"
        )

    # -- root_cause_analysis -------------------------------------------
    def _root_cause_analysis(self) -> str:
        cause_groups = {}
        for deal_name, deal in _DEAL_TIMELINES.items():
            status = _classify_stall(deal)
            if status not in ("CRITICAL", "STALLED"):
                continue
            blocker = deal["blocker"]
            if blocker not in cause_groups:
                cause_groups[blocker] = []
            cause_groups[blocker].append((deal_name, deal))

        sections = []
        for cause, deals in sorted(cause_groups.items(), key=lambda x: -sum(d["value"] for _, d in x[1])):
            taxonomy = _ROOT_CAUSE_TAXONOMY.get(cause, {})
            total_value = sum(d["value"] for _, d in deals)
            deal_list = "\n".join(
                f"  - {n}: ${d['value']:,} ({d['stage']}, {d['days_in_stage']}d stalled)"
                for n, d in sorted(deals, key=lambda x: -x[1]["value"])
            )
            sections.append(
                f"**{cause.replace('_', ' ').title()}** [{taxonomy.get('category', 'Unknown')}]\n"
                f"Severity: {taxonomy.get('severity', 'unknown').upper()} | "
                f"Deals: {len(deals)} | Value: ${total_value:,}\n"
                f"Recovery probability: {taxonomy.get('recovery_probability', 0.5):.0%} | "
                f"Avg recovery: {taxonomy.get('avg_recovery_days', 14)} days\n\n"
                f"Description: {taxonomy.get('description', cause)}\n\n"
                f"Affected deals:\n{deal_list}"
            )

        return (
            f"**Root Cause Analysis -- Stalled Deals**\n\n"
            f"Identified **{len(cause_groups)}** distinct root cause categories.\n\n"
            + "\n\n---\n\n".join(sections)
            + f"\n\n**Pattern Insight:** Organizational and relationship causes have lowest "
            f"recovery rates and require executive-level intervention.\n\n"
            f"Source: [Deal History + Stall Pattern Database]\n"
            f"Agents: RootCauseEngine"
        )

    # -- intervention_plan ---------------------------------------------
    def _intervention_plan(self) -> str:
        sections = []
        for deal_name in sorted(_DEAL_TIMELINES.keys(), key=lambda d: -_DEAL_TIMELINES[d]["value"]):
            deal = _DEAL_TIMELINES[deal_name]
            status = _classify_stall(deal)
            if status not in ("CRITICAL", "STALLED"):
                continue

            playbook = _INTERVENTION_PLAYBOOKS.get(deal["blocker"], {})
            if not playbook:
                continue

            steps = "\n".join(f"  - **{day.replace('_', ' ').title()}:** {action}"
                              for day, action in sorted(playbook.items(), key=lambda x: int(x[0].split("_")[1])))

            taxonomy = _ROOT_CAUSE_TAXONOMY.get(deal["blocker"], {})
            recovery_prob = taxonomy.get("recovery_probability", 0.5)
            recovery_days = taxonomy.get("avg_recovery_days", 14)

            sections.append(
                f"**{deal_name} -- ${deal['value']:,} ({deal['stage']})**\n"
                f"Status: {status} | Owner: {deal['owner']} | Root Cause: {deal['blocker'].replace('_', ' ').title()}\n"
                f"Recovery probability: {recovery_prob:.0%} | Expected timeline: {recovery_days} days\n\n"
                f"**Intervention Steps:**\n{steps}\n"
            )

        return (
            f"**Intervention Plans -- Stalled Deals**\n\n"
            + "\n---\n\n".join(sections)
            + f"\n\n**Execution Notes:**\n"
            f"- Assign each plan to deal owner with daily check-in\n"
            f"- Escalate to sales leadership if no progress by Day 7\n"
            f"- Evaluate deal viability if no improvement by Day 14\n\n"
            f"Source: [Intervention Playbook + Best Practices]\n"
            f"Agents: InterventionPlannerAgent"
        )

    # -- stall_prevention ----------------------------------------------
    def _stall_prevention(self) -> str:
        at_risk = []
        for deal_name, deal in _DEAL_TIMELINES.items():
            prob = _stall_probability(deal)
            trend = _activity_trend(deal)
            at_risk.append((deal_name, deal, prob, trend))

        at_risk.sort(key=lambda x: -x[2])

        rows = ""
        for name, deal, prob, trend in at_risk:
            trend_label = {"sharp_decline": "SHARP DECLINE", "declining": "Declining",
                           "stable": "Stable", "increasing": "Increasing",
                           "no_baseline": "No baseline"}.get(trend, trend)
            rows += (f"| {name} | ${deal['value']:,} | {deal['stage']} | "
                     f"{prob}% | {trend_label} | {deal['next_step']} |\n")

        no_next_step = sum(1 for _, d, _, _ in at_risk if d["next_step"] == "None scheduled")
        silent_champions = sum(1 for _, d, _, _ in at_risk if d["champion_status"] in ("Silent", "Disengaged"))
        declining_activity = sum(1 for _, _, _, t in at_risk if t in ("sharp_decline", "declining"))

        return (
            f"**Stall Prevention Dashboard**\n\n"
            f"**Leading Indicators:**\n"
            f"- Deals with no next step: **{no_next_step}**\n"
            f"- Silent/disengaged champions: **{silent_champions}**\n"
            f"- Declining activity trend: **{declining_activity}**\n\n"
            f"**Stall Probability by Deal:**\n\n"
            f"| Deal | Value | Stage | Stall Prob | Activity Trend | Next Step |\n"
            f"|------|-------|-------|-----------|---------------|----------|\n"
            f"{rows}\n"
            f"**Prevention Recommendations:**\n"
            f"1. Mandate next-step scheduling before any deal review\n"
            f"2. Alert at 7 days without activity (current: 21 days)\n"
            f"3. Require champion check-in every 10 days\n"
            f"4. Auto-flag deals with declining activity for manager review\n"
            f"5. Weekly stall-risk scoring in pipeline meetings\n\n"
            f"Source: [Predictive Analytics + Activity Patterns]\n"
            f"Agents: StallPreventionEngine"
        )


if __name__ == "__main__":
    agent = StalledDealDetectionAgent()
    print("=" * 70)
    print("LIVE TENANT STALL DETECTION (fetched over HTTP; embedded demo offline)")
    print(agent.perform(operation="detect_stalls"))
    print()
    print("=" * 70)
    print("EMBEDDED DEMO (works offline, simulated)")
    print(agent.perform(operation="root_cause_analysis"))
    print()
    print("=" * 70)
    print(agent.perform(operation="intervention_plan"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
