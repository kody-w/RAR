---
name: "rar-aibast-agents-library-activity-gap"
description: "Flags missing sales activities per stage using live opportunities from a simulated Dynamics 365 tenant, with an embedded offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/activity_gap", "rar_sha256": "99bc2d4e0e44d0930ac4218d16dc91503d2cc56928551dc8a13efc9f7347258a", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["b2b", "sales", "activity-gap", "deal-progression", "pipeline"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/activity_gap`. The original RAPP
agent is preserved byte-for-byte in `activity_gap_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The analysis to perform",
      "enum": [
        "identify_gaps",
        "stage_requirements",
        "completion_roadmap",
        "gap_impact_analysis"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `activity_gap_agent.py` and embedded as the fenced Python below (sha256 99bc2d4e0e44d093…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `activity_gap_agent.py` first:

```bash
python3 activity_gap_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 activity_gap_agent.py   # or on stdin
python3 activity_gap_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
