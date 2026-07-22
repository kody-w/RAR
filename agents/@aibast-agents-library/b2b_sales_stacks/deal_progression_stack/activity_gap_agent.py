"""
Activity Gap Agent — a template you are meant to mutate.

Flags missing sales activities per deal stage, builds completion roadmaps,
and analyzes gap impact so no critical playbook step is skipped during the
deal lifecycle.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="identify_gaps") — the gap report checks live
     open deals such as "Cedar Hollow Printing — Managed print fleet
     refresh" against the stage playbook.
  2. No network? Everything falls back to the embedded demo layer below
     (_DEAL_ACTIVITIES / _STAGE_REQUIREMENTS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     ACTIVITY_GAP_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with calls into your own API. The dict shape the
     rest of the file needs is documented in _normalize_live_deal().
     Activity completion evidence (which playbook steps are actually done)
     is an enrichment seam — wire your activity tracker there.

OPERATIONS
  identify_gaps | stage_requirements | completion_roadmap
  | gap_impact_analysis
  kwargs: operation (required)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request

# ===================================================================
# RAPP AGENT MANIFEST
# ===================================================================
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/activity_gap",
    "version": "1.1.0",
    "display_name": "Activity Gap Analyzer",
    "description": "Flags missing sales activities per stage using live opportunities from a simulated Dynamics 365 tenant, with an embedded offline demo fallback.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "activity-gap", "deal-progression", "pipeline"],
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
#   export ACTIVITY_GAP_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_deal().
# ===================================================================

DATA_SOURCE_URL = os.environ.get(
    "ACTIVITY_GAP_DATA_URL",
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


def _normalize_live_deal(row):
    """Project a Dynamics opportunity onto the shape this agent uses.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not knowable from the CRM alone' and the
    renderers label it an enrichment seam (wire your activity tracker to
    map real CRM activities onto playbook IDs)."""
    return {
        "deal_id": str(row.get("opportunityid", ""))[:8],
        "name": row.get("name", "Unknown"),
        "account": row.get("parentaccountidname", "Unknown"),
        "value": int(float(row.get("estimatedvalue") or 0)),
        "stage": _LIVE_STAGE_MAP.get(row.get("stepname"), "Qualification"),
        "owner": row.get("owneridname", ""),
        "completed": None,   # enrichment seam — wire your activity tracker
        "skipped": None,     # enrichment seam
        "_live": True,
    }


def _live_open_deals():
    """Live open opportunities normalized for this agent; [] when offline."""
    return [_normalize_live_deal(o) for o in _fetch_collection("opportunities")
            if o.get("statecode") == 0]


# ===================================================================
# EMBEDDED DEMO LAYER (offline fallback)
# ===================================================================

_STAGE_REQUIREMENTS = {
    "Qualification": {
        "activities": [
            {"id": "Q1", "name": "Initial discovery call", "weight": 3, "description": "30-min intro call with prospect"},
            {"id": "Q2", "name": "BANT qualification", "weight": 3, "description": "Budget, Authority, Need, Timeline assessed"},
            {"id": "Q3", "name": "Pain point documentation", "weight": 2, "description": "Documented business pain points"},
            {"id": "Q4", "name": "Stakeholder identification", "weight": 2, "description": "Key decision makers mapped"},
            {"id": "Q5", "name": "ICP fit assessment", "weight": 1, "description": "Ideal customer profile scoring"},
        ],
        "min_completion": 80,
    },
    "Discovery": {
        "activities": [
            {"id": "D1", "name": "Technical deep-dive", "weight": 3, "description": "Technical requirements session with IT"},
            {"id": "D2", "name": "Business case outline", "weight": 3, "description": "Initial ROI and value framework"},
            {"id": "D3", "name": "Champion identified", "weight": 3, "description": "Internal champion confirmed and engaged"},
            {"id": "D4", "name": "Competitive landscape", "weight": 2, "description": "Competitors evaluated and positioned"},
            {"id": "D5", "name": "Multi-thread contacts", "weight": 2, "description": "3+ contacts engaged across departments"},
            {"id": "D6", "name": "Demo or POC delivered", "weight": 2, "description": "Product demonstration completed"},
        ],
        "min_completion": 75,
    },
    "Proposal": {
        "activities": [
            {"id": "P1", "name": "Formal proposal sent", "weight": 3, "description": "Customized proposal delivered to prospect"},
            {"id": "P2", "name": "Pricing presented", "weight": 3, "description": "Pricing discussed with decision maker"},
            {"id": "P3", "name": "Executive sponsor meeting", "weight": 3, "description": "Meeting with VP+ level stakeholder"},
            {"id": "P4", "name": "Reference calls provided", "weight": 2, "description": "Customer references shared"},
            {"id": "P5", "name": "Security/compliance review", "weight": 2, "description": "IT security questionnaire completed"},
            {"id": "P6", "name": "Implementation plan shared", "weight": 1, "description": "Deployment timeline presented"},
        ],
        "min_completion": 70,
    },
    "Negotiation": {
        "activities": [
            {"id": "N1", "name": "Terms negotiation call", "weight": 3, "description": "Contract terms discussed with procurement"},
            {"id": "N2", "name": "Legal redline review", "weight": 3, "description": "Legal review of contract terms"},
            {"id": "N3", "name": "Final pricing approved", "weight": 3, "description": "Discount/pricing approved internally"},
            {"id": "N4", "name": "Champion reconfirmed", "weight": 2, "description": "Champion commitment validated"},
            {"id": "N5", "name": "Go-live date agreed", "weight": 2, "description": "Implementation start date confirmed"},
        ],
        "min_completion": 80,
    },
    "Contract": {
        "activities": [
            {"id": "C1", "name": "Final contract sent", "weight": 3, "description": "Executed contract sent for signature"},
            {"id": "C2", "name": "Signature obtained", "weight": 3, "description": "Contract signed by authorized signer"},
            {"id": "C3", "name": "PO received", "weight": 2, "description": "Purchase order issued"},
            {"id": "C4", "name": "Onboarding handoff", "weight": 2, "description": "Customer success team introduced"},
        ],
        "min_completion": 90,
    },
}

_DEAL_ACTIVITIES = {
    "TechCorp Industries": {
        "deal_id": "OPP-001", "value": 890000, "stage": "Proposal", "owner": "Mike Chen",
        "completed": ["Q1", "Q2", "Q3", "Q4", "Q5", "D1", "D2", "D4", "D5", "D6", "P1", "P2"],
        "skipped": ["D3", "P3", "P4", "P5", "P6"],
    },
    "Global Manufacturing": {
        "deal_id": "OPP-002", "value": 720000, "stage": "Negotiation", "owner": "Lisa Torres",
        "completed": ["Q1", "Q2", "Q3", "Q4", "Q5", "D1", "D2", "D3", "D4", "D5", "D6", "P1", "P2", "P3", "P4", "P5", "P6", "N1"],
        "skipped": ["N2", "N3", "N4", "N5"],
    },
    "Apex Financial": {
        "deal_id": "OPP-003", "value": 580000, "stage": "Discovery", "owner": "James Park",
        "completed": ["Q1", "Q2", "Q3", "Q5", "D1"],
        "skipped": ["Q4", "D2", "D3", "D4", "D5", "D6"],
    },
    "Metro Healthcare": {
        "deal_id": "OPP-004", "value": 440000, "stage": "Proposal", "owner": "Mike Chen",
        "completed": ["Q1", "Q2", "Q3", "Q4", "Q5", "D1", "D2", "D3", "D4", "D5", "D6", "P1", "P2", "P3", "P5"],
        "skipped": ["P4", "P6"],
    },
    "Pinnacle Logistics": {
        "deal_id": "OPP-005", "value": 360000, "stage": "Qualification", "owner": "James Park",
        "completed": ["Q1", "Q2"],
        "skipped": ["Q3", "Q4", "Q5"],
    },
    "Pacific Telecom": {
        "deal_id": "OPP-013", "value": 780000, "stage": "Negotiation", "owner": "Lisa Torres",
        "completed": ["Q1", "Q2", "Q3", "Q4", "Q5", "D1", "D2", "D3", "D4", "D5", "D6", "P1", "P2", "P3", "P4", "P5", "P6", "N1", "N2", "N4"],
        "skipped": ["N3", "N5"],
    },
}

_GAP_DEFINITIONS = {
    "champion_missing": {"severity": "critical", "impact": "40% lower win rate without active champion", "stage_block": True},
    "executive_access": {"severity": "critical", "impact": "Deals without exec sponsor close 35% less often", "stage_block": True},
    "pricing_not_discussed": {"severity": "high", "impact": "Late pricing surprises cause 25% of deal losses", "stage_block": False},
    "no_references": {"severity": "medium", "impact": "Reference calls increase win rate by 18%", "stage_block": False},
    "security_incomplete": {"severity": "medium", "impact": "IT security delays add avg 12 days to cycle", "stage_block": False},
    "single_thread": {"severity": "high", "impact": "Single-threaded deals have 50% higher churn risk", "stage_block": True},
    "no_business_case": {"severity": "high", "impact": "Deals without ROI justification stall 2x more", "stage_block": True},
    "legal_not_started": {"severity": "high", "impact": "Legal review adds 8-15 days; late start compounds", "stage_block": False},
}


# ===================================================================
# HELPERS
# ===================================================================

def _get_stage_activities(stage):
    """Return required activities for a given stage and all prior stages."""
    stage_order = ["Qualification", "Discovery", "Proposal", "Negotiation", "Contract"]
    idx = stage_order.index(stage) if stage in stage_order else 0
    all_activities = []
    for s in stage_order[:idx + 1]:
        reqs = _STAGE_REQUIREMENTS.get(s, {})
        for act in reqs.get("activities", []):
            all_activities.append({**act, "stage": s})
    return all_activities


def _compute_gaps(deal_name):
    """Compute gaps for a specific deal."""
    deal = _DEAL_ACTIVITIES.get(deal_name)
    if not deal:
        return []
    required = _get_stage_activities(deal["stage"])
    completed = set(deal["completed"])
    gaps = []
    for act in required:
        if act["id"] not in completed:
            gaps.append({
                "activity_id": act["id"],
                "activity_name": act["name"],
                "description": act["description"],
                "weight": act["weight"],
                "stage": act["stage"],
                "is_critical": act["weight"] >= 3,
            })
    return gaps


def _completion_pct(deal_name):
    """Calculate completion percentage for a deal."""
    deal = _DEAL_ACTIVITIES.get(deal_name)
    if not deal:
        return 0.0
    required = _get_stage_activities(deal["stage"])
    if not required:
        return 100.0
    total_weight = sum(a["weight"] for a in required)
    completed_ids = set(deal["completed"])
    completed_weight = sum(a["weight"] for a in required if a["id"] in completed_ids)
    return round(completed_weight / total_weight * 100, 1)


def _gap_priority(gaps):
    """Sort gaps by priority (critical first, then by weight)."""
    return sorted(gaps, key=lambda g: (-int(g["is_critical"]), -g["weight"]))


# ===================================================================
# AGENT CLASS
# ===================================================================

class ActivityGapAgent(BasicAgent):
    """
    Identifies missing sales activities and generates completion roadmaps.

    Operations:
        identify_gaps        - find missing activities per deal
        stage_requirements   - show required activities for each stage
        completion_roadmap   - prioritized plan to close gaps
        gap_impact_analysis  - analyze business impact of open gaps
    """

    def __init__(self):
        self.name = "ActivityGapAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["identify_gaps", "stage_requirements", "completion_roadmap", "gap_impact_analysis"],
                        "description": "The analysis to perform",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "identify_gaps")
        dispatch = {
            "identify_gaps": self._identify_gaps,
            "stage_requirements": self._stage_requirements,
            "completion_roadmap": self._completion_roadmap,
            "gap_impact_analysis": self._gap_impact_analysis,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"**Error:** Unknown operation '{op}'. Valid: {', '.join(dispatch.keys())}"
        return handler()

    # -- identify_gaps (flagship: prefers LIVE tenant, falls back) ------
    def _identify_gaps(self) -> str:
        live = _live_open_deals()
        if live:
            return self._identify_gaps_live(live)
        sections = []
        total_gaps = 0
        critical_gaps = 0

        for deal_name, deal in _DEAL_ACTIVITIES.items():
            gaps = _compute_gaps(deal_name)
            pct = _completion_pct(deal_name)
            total_gaps += len(gaps)
            crit = [g for g in gaps if g["is_critical"]]
            critical_gaps += len(crit)
            prioritized = _gap_priority(gaps)

            gap_rows = ""
            for g in prioritized[:5]:
                severity = "CRITICAL" if g["is_critical"] else "Standard"
                gap_rows += f"| {g['activity_id']} | {g['activity_name']} | {g['stage']} | {severity} |\n"

            status_icon = "RED" if pct < 60 else ("YELLOW" if pct < 80 else "GREEN")
            sections.append(
                f"**{deal_name} ({deal['stage']}) -- ${deal['value']:,}**\n"
                f"Completion: {pct}% [{status_icon}] | Owner: {deal['owner']}\n\n"
                f"| ID | Missing Activity | Stage | Severity |\n"
                f"|----|-----------------|-------|----------|\n"
                f"{gap_rows}"
            )

        return (
            f"**Activity Gap Analysis -- {len(_DEAL_ACTIVITIES)} Deals**\n\n"
            f"Total gaps identified: **{total_gaps}** | Critical: **{critical_gaps}**\n\n"
            + "\n---\n\n".join(sections)
            + f"\n\nSource: [CRM Activity Logs + Sales Playbook]\n"
            f"Agents: ActivityTrackingAgent, StageComplianceAgent"
        )

    def _identify_gaps_live(self, deals) -> str:
        sections = []
        for d in sorted(deals, key=lambda x: -x["value"]):
            required = _get_stage_activities(d["stage"])
            rows = ""
            for act in required[-5:]:
                rows += (f"| {act['id']} | {act['name']} | {act['stage']} | "
                         f"n/a — enrichment seam |\n")
            sections.append(
                f"**{d['name']} ({d['stage']}) -- ${d['value']:,}**\n"
                f"Owner: {d['owner']} | Completion: n/a — enrichment seam "
                f"(wire your activity tracker)\n\n"
                f"| ID | Required Activity | Stage | Evidence |\n"
                f"|----|------------------|-------|----------|\n"
                f"{rows}"
            )
        return (
            f"**Activity Gap Analysis -- {len(deals)} LIVE Open Deals** "
            f"(Static Dynamics 365 tenant)\n\n"
            f"Playbook requirements come from this template's stage rules; "
            f"completion evidence stays n/a until you wire a real activity "
            f"tracker at the LIVE DATA SEAM.\n\n"
            + "\n---\n\n".join(sections)
            + "\nSource: [Live Dynamics 365 opportunities + Sales Playbook]\n"
            "Agents: ActivityTrackingAgent, StageComplianceAgent"
        )

    # -- stage_requirements --------------------------------------------
    def _stage_requirements(self) -> str:
        sections = []
        for stage in ["Qualification", "Discovery", "Proposal", "Negotiation", "Contract"]:
            reqs = _STAGE_REQUIREMENTS[stage]
            rows = ""
            for act in reqs["activities"]:
                priority = "High" if act["weight"] >= 3 else ("Medium" if act["weight"] >= 2 else "Low")
                rows += f"| {act['id']} | {act['name']} | {priority} | {act['description']} |\n"
            sections.append(
                f"**{stage}** (Min completion: {reqs['min_completion']}%)\n\n"
                f"| ID | Activity | Priority | Description |\n"
                f"|----|----------|----------|-------------|\n"
                f"{rows}"
            )

        total_activities = sum(len(r["activities"]) for r in _STAGE_REQUIREMENTS.values())
        return (
            f"**Stage Activity Requirements**\n\n"
            f"Total activities across all stages: **{total_activities}**\n\n"
            + "\n---\n\n".join(sections)
            + f"\n\nSource: [Sales Playbook + Best Practice Library]\n"
            f"Agents: PlaybookAgent"
        )

    # -- completion_roadmap --------------------------------------------
    def _completion_roadmap(self) -> str:
        roadmap_items = []
        for deal_name, deal in sorted(_DEAL_ACTIVITIES.items(), key=lambda x: -x[1]["value"]):
            gaps = _gap_priority(_compute_gaps(deal_name))
            pct = _completion_pct(deal_name)
            if not gaps:
                continue

            tasks = []
            day = 1
            for g in gaps:
                if g["is_critical"]:
                    tasks.append(f"- Day {day}: **{g['activity_name']}** -- {g['description']} [CRITICAL]")
                    day += 2
                else:
                    tasks.append(f"- Day {day}: {g['activity_name']} -- {g['description']}")
                    day += 1

            est_days = day - 1
            target_pct = min(pct + len(gaps) * 8, 100)
            roadmap_items.append(
                f"**{deal_name} -- ${deal['value']:,}**\n"
                f"Current: {pct}% | Target: {target_pct}% | Est. {est_days} days\n\n"
                + "\n".join(tasks)
            )

        total_deals = len(roadmap_items)
        return (
            f"**Completion Roadmap -- {total_deals} Deals with Gaps**\n\n"
            f"Prioritized by deal value and gap severity.\n\n"
            + "\n\n---\n\n".join(roadmap_items)
            + f"\n\nSource: [Sales Playbook + Activity Tracker]\n"
            f"Agents: RoadmapPlannerAgent"
        )

    # -- gap_impact_analysis -------------------------------------------
    def _gap_impact_analysis(self) -> str:
        impact_data = {}
        for deal_name in _DEAL_ACTIVITIES:
            gaps = _compute_gaps(deal_name)
            for g in gaps:
                key = g["activity_name"]
                if key not in impact_data:
                    impact_data[key] = {"count": 0, "total_value": 0, "critical": g["is_critical"]}
                impact_data[key]["count"] += 1
                impact_data[key]["total_value"] += _DEAL_ACTIVITIES[deal_name]["value"]

        sorted_impacts = sorted(impact_data.items(), key=lambda x: -x[1]["total_value"])

        rows = ""
        for name, data in sorted_impacts:
            severity = "CRITICAL" if data["critical"] else "Standard"
            rows += f"| {name} | {data['count']} | ${data['total_value']:,} | {severity} |\n"

        # Overall metrics
        total_value_at_risk = sum(d["value"] for d in _DEAL_ACTIVITIES.values())
        deals_below_threshold = sum(
            1 for dn in _DEAL_ACTIVITIES if _completion_pct(dn) < _STAGE_REQUIREMENTS.get(
                _DEAL_ACTIVITIES[dn]["stage"], {}
            ).get("min_completion", 70)
        )

        cat_lines = ""
        for cat, info in _GAP_DEFINITIONS.items():
            cat_lines += f"- **{cat.replace('_', ' ').title()}** ({info['severity']}): {info['impact']}\n"

        return (
            f"**Gap Impact Analysis**\n\n"
            f"**Portfolio Overview:**\n"
            f"- Total pipeline analyzed: ${total_value_at_risk:,}\n"
            f"- Deals below completion threshold: {deals_below_threshold}\n\n"
            f"**Most Common Gaps by Pipeline Exposure:**\n\n"
            f"| Gap | Deals Affected | Value Exposed | Severity |\n"
            f"|----|---------------|---------------|----------|\n"
            f"{rows}\n"
            f"**Risk Categories:**\n{cat_lines}\n"
            f"**Recommendation:** Focus on critical gaps in top-value deals first. "
            f"Closing champion and executive access gaps yields highest ROI.\n\n"
            f"Source: [Win/Loss Analysis + Activity Correlation]\n"
            f"Agents: ImpactAnalysisAgent, WinPatternAgent"
        )


if __name__ == "__main__":
    agent = ActivityGapAgent()
    print("=" * 70)
    print("LIVE TENANT DEALS (fetched over HTTP; embedded demo offline)")
    print(agent.perform(operation="identify_gaps"))
    print()
    print("=" * 70)
    print("EMBEDDED DEMO (works offline)")
    print(agent.perform(operation="stage_requirements"))
    print()
    print("=" * 70)
    print(agent.perform(operation="gap_impact_analysis"))
