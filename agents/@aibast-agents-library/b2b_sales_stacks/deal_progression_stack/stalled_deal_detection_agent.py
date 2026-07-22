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
