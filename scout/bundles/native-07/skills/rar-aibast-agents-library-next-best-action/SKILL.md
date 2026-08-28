---
name: "rar-aibast-agents-library-next-best-action"
description: "Recommends next actions for live deals from a simulated Dynamics 365 tenant, matched by CRM stage, with an embedded offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/next_best_action", "rar_sha256": "b1bca4d4801b40f637da7729f310367c179085a5d1638de4101e77988835ab60", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["b2b", "sales", "next-best-action", "deal-progression", "recommendations"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/next_best_action`. The original RAPP
agent is preserved byte-for-byte in `next_best_action_agent.py` and in the RCI capsule.

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

Next Best Action Agent — a template you are meant to mutate.

Recommends prioritized next actions per deal from stage, risk, and
engagement context, with sequenced plans, impact forecasts, and rep
assignments to maximize pipeline velocity.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="recommend_actions") — recommendations are
     generated for live open deals such as "Orchard Signal Works —
     Managed print fleet refresh", matched to the action library by
     their real CRM stage.
  2. No network? Everything falls back to the embedded demo layer below
     (_DEAL_CONTEXT / _ACTION_TEMPLATES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     NEXT_BEST_ACTION_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with your own client. The dict shape the rest of
     the file needs is documented in _normalize_live_deal(). Blocker and
     health context is an enrichment seam — wire Gong / your health
     scoring there for blocker-targeted recommendations.

OPERATIONS
  recommend_actions | action_sequence | impact_forecast | rep_assignments
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
        "recommend_actions",
        "action_sequence",
        "impact_forecast",
        "rep_assignments"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `next_best_action_agent.py` and embedded as the fenced Python below (sha256 b1bca4d4801b40f6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `next_best_action_agent.py` first:

```bash
python3 next_best_action_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 next_best_action_agent.py   # or on stdin
python3 next_best_action_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Next Best Action Agent — a template you are meant to mutate.

Recommends prioritized next actions per deal from stage, risk, and
engagement context, with sequenced plans, impact forecasts, and rep
assignments to maximize pipeline velocity.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="recommend_actions") — recommendations are
     generated for live open deals such as "Orchard Signal Works —
     Managed print fleet refresh", matched to the action library by
     their real CRM stage.
  2. No network? Everything falls back to the embedded demo layer below
     (_DEAL_CONTEXT / _ACTION_TEMPLATES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     NEXT_BEST_ACTION_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with your own client. The dict shape the rest of
     the file needs is documented in _normalize_live_deal(). Blocker and
     health context is an enrichment seam — wire Gong / your health
     scoring there for blocker-targeted recommendations.

OPERATIONS
  recommend_actions | action_sequence | impact_forecast | rep_assignments
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
    "name": "@aibast-agents-library/next_best_action",
    "version": "1.1.0",
    "display_name": "Next Best Action",
    "description": "Recommends next actions for live deals from a simulated Dynamics 365 tenant, matched by CRM stage, with an embedded offline demo fallback.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "next-best-action", "deal-progression", "recommendations"],
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
#   export NEXT_BEST_ACTION_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_deal().
# ===================================================================

DATA_SOURCE_URL = os.environ.get(
    "NEXT_BEST_ACTION_DATA_URL",
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
    renderers label it an enrichment seam (wire Gong / your health scoring
    for blocker-targeted recommendations)."""
    return {
        "deal_id": str(row.get("opportunityid", ""))[:8],
        "name": row.get("name", "Unknown"),
        "account": row.get("parentaccountidname", "Unknown"),
        "value": int(float(row.get("estimatedvalue") or 0)),
        "stage": _LIVE_STAGE_MAP.get(row.get("stepname"), "Qualification"),
        "owner": row.get("owneridname", ""),
        "probability": int(row.get("closeprobability") or 0),
        "blocker": None,       # enrichment seam — wire call analytics
        "risk_score": None,    # enrichment seam — wire your risk scoring
        "health_score": None,  # enrichment seam
        "_live": True,
    }


def _live_open_deals():
    """Live open opportunities normalized for this agent; [] when offline."""
    return [_normalize_live_deal(o) for o in _fetch_collection("opportunities")
            if o.get("statecode") == 0]


def _recommend_for_live_deal(deal):
    """Rank action templates for a live deal by its real CRM stage.
    Blocker matching is skipped (enrichment seam)."""
    recommendations = []
    for action_id, template in _ACTION_TEMPLATES.items():
        if deal["stage"] not in template["applicable_stages"]:
            continue
        outcome = _HISTORICAL_OUTCOMES.get(action_id, {})
        priority_score = (
            template["impact_score"] * 0.4 +
            outcome.get("success_rate", 0.5) * 100 * 0.3 +
            (100 - outcome.get("avg_days_to_impact", 5) * 10) * 0.3
        )
        recommendations.append({
            "action_id": action_id,
            "name": template["name"],
            "description": template["description"],
            "effort_hours": template["effort_hours"],
            "priority_score": round(priority_score, 1),
            "success_rate": outcome.get("success_rate", 0.5),
            "days_to_impact": outcome.get("avg_days_to_impact", 5),
        })
    return sorted(recommendations, key=lambda r: -r["priority_score"])


# ===================================================================
# EMBEDDED DEMO LAYER (offline fallback)
# ===================================================================

_ACTION_TEMPLATES = {
    "executive_outreach": {
        "name": "Executive Sponsor Outreach",
        "effort_hours": 2.0, "impact_score": 85,
        "description": "VP-to-VP outreach to establish executive alignment",
        "applicable_stages": ["Proposal", "Negotiation"],
        "applicable_blockers": ["executive_change", "no_champion", "stakeholder_alignment"],
    },
    "champion_reengagement": {
        "name": "Champion Re-engagement",
        "effort_hours": 1.5, "impact_score": 78,
        "description": "Personalized outreach to silent or disengaged champion",
        "applicable_stages": ["Discovery", "Proposal", "Negotiation"],
        "applicable_blockers": ["executive_change", "competitor_eval"],
    },
    "roi_business_case": {
        "name": "ROI Business Case Delivery",
        "effort_hours": 4.0, "impact_score": 82,
        "description": "CFO-ready business case with 3-year TCO analysis",
        "applicable_stages": ["Proposal", "Negotiation"],
        "applicable_blockers": ["budget_hold"],
    },
    "competitive_differentiation": {
        "name": "Competitive Differentiation Session",
        "effort_hours": 3.0, "impact_score": 75,
        "description": "Head-to-head comparison with proof points and references",
        "applicable_stages": ["Discovery", "Proposal"],
        "applicable_blockers": ["competitor_eval", "technical_validation"],
    },
    "legal_fast_track": {
        "name": "Legal Fast-Track Package",
        "effort_hours": 1.0, "impact_score": 70,
        "description": "Pre-approved contract template with flexible terms",
        "applicable_stages": ["Negotiation", "Contract"],
        "applicable_blockers": ["legal_review", "procurement_process"],
    },
    "reference_call": {
        "name": "Customer Reference Call",
        "effort_hours": 1.5, "impact_score": 72,
        "description": "Arrange reference call with similar customer in same vertical",
        "applicable_stages": ["Discovery", "Proposal"],
        "applicable_blockers": ["competitor_eval", "technical_validation", "timeline_uncertainty"],
    },
    "technical_deep_dive": {
        "name": "Technical Deep-Dive Workshop",
        "effort_hours": 3.0, "impact_score": 68,
        "description": "Hands-on technical session with prospect engineering team",
        "applicable_stages": ["Discovery", "Proposal"],
        "applicable_blockers": ["technical_validation"],
    },
    "multi_thread_outreach": {
        "name": "Multi-Thread Outreach Campaign",
        "effort_hours": 2.5, "impact_score": 65,
        "description": "Engage 3+ contacts across departments simultaneously",
        "applicable_stages": ["Qualification", "Discovery"],
        "applicable_blockers": ["no_champion", "stakeholder_alignment"],
    },
    "contract_negotiation": {
        "name": "Contract Terms Negotiation",
        "effort_hours": 2.0, "impact_score": 80,
        "description": "Address outstanding contract terms with procurement/legal",
        "applicable_stages": ["Negotiation", "Contract"],
        "applicable_blockers": ["legal_review", "procurement_process"],
    },
    "value_workshop": {
        "name": "Value Realization Workshop",
        "effort_hours": 3.5, "impact_score": 74,
        "description": "On-site workshop demonstrating business value and implementation plan",
        "applicable_stages": ["Proposal", "Negotiation"],
        "applicable_blockers": ["budget_hold", "timeline_uncertainty"],
    },
}

_DEAL_CONTEXT = {
    "TechCorp Industries": {
        "deal_id": "OPP-001", "value": 890000, "stage": "Proposal", "owner": "Mike Chen",
        "blocker": "executive_change", "days_in_stage": 34, "last_contact_days": 18,
        "champion_status": "Silent", "risk_score": 72, "health_score": 42,
    },
    "Global Manufacturing": {
        "deal_id": "OPP-002", "value": 720000, "stage": "Negotiation", "owner": "Lisa Torres",
        "blocker": "legal_review", "days_in_stage": 28, "last_contact_days": 5,
        "champion_status": "Active frustrated", "risk_score": 44, "health_score": 63,
    },
    "Apex Financial": {
        "deal_id": "OPP-003", "value": 580000, "stage": "Discovery", "owner": "James Park",
        "blocker": "competitor_eval", "days_in_stage": 25, "last_contact_days": 12,
        "champion_status": "Disengaged", "risk_score": 70, "health_score": 32,
    },
    "Metro Healthcare": {
        "deal_id": "OPP-004", "value": 440000, "stage": "Proposal", "owner": "Mike Chen",
        "blocker": "budget_hold", "days_in_stage": 22, "last_contact_days": 9,
        "champion_status": "Active", "risk_score": 42, "health_score": 67,
    },
    "Pacific Telecom": {
        "deal_id": "OPP-013", "value": 780000, "stage": "Negotiation", "owner": "Lisa Torres",
        "blocker": "procurement_process", "days_in_stage": 14, "last_contact_days": 3,
        "champion_status": "Active", "risk_score": 16, "health_score": 85,
    },
    "Pinnacle Logistics": {
        "deal_id": "OPP-005", "value": 360000, "stage": "Qualification", "owner": "James Park",
        "blocker": "no_champion", "days_in_stage": 20, "last_contact_days": 14,
        "champion_status": "Silent", "risk_score": 68, "health_score": 28,
    },
}

_REP_PROFILES = {
    "Mike Chen": {"title": "Sr. Account Executive", "specialty": "executive alignment",
                  "active_deals": 11, "capacity": 14, "avg_close_rate": 0.34,
                  "strengths": ["C-level relationships", "Complex deal navigation"]},
    "Lisa Torres": {"title": "Account Executive", "specialty": "contract negotiation",
                    "active_deals": 9, "capacity": 12, "avg_close_rate": 0.38,
                    "strengths": ["Procurement expertise", "Legal coordination"]},
    "James Park": {"title": "Sr. Account Executive", "specialty": "technical sales",
                   "active_deals": 12, "capacity": 14, "avg_close_rate": 0.31,
                   "strengths": ["Technical depth", "Solution architecture"]},
    "Sarah Kim": {"title": "Account Executive", "specialty": "executive alignment",
                  "active_deals": 8, "capacity": 12, "avg_close_rate": 0.36,
                  "strengths": ["Relationship building", "Stakeholder management"]},
    "Ryan Davis": {"title": "Account Executive", "specialty": "mid-market",
                   "active_deals": 7, "capacity": 12, "avg_close_rate": 0.42,
                   "strengths": ["Fast deal cycles", "SMB/mid-market focus"]},
}

_HISTORICAL_OUTCOMES = {
    "executive_outreach": {"success_rate": 0.72, "avg_days_to_impact": 5, "stage_advance_rate": 0.45},
    "champion_reengagement": {"success_rate": 0.65, "avg_days_to_impact": 3, "stage_advance_rate": 0.35},
    "roi_business_case": {"success_rate": 0.68, "avg_days_to_impact": 7, "stage_advance_rate": 0.40},
    "competitive_differentiation": {"success_rate": 0.62, "avg_days_to_impact": 5, "stage_advance_rate": 0.30},
    "legal_fast_track": {"success_rate": 0.80, "avg_days_to_impact": 4, "stage_advance_rate": 0.55},
    "reference_call": {"success_rate": 0.70, "avg_days_to_impact": 3, "stage_advance_rate": 0.28},
    "technical_deep_dive": {"success_rate": 0.66, "avg_days_to_impact": 5, "stage_advance_rate": 0.32},
    "multi_thread_outreach": {"success_rate": 0.55, "avg_days_to_impact": 7, "stage_advance_rate": 0.20},
    "contract_negotiation": {"success_rate": 0.78, "avg_days_to_impact": 5, "stage_advance_rate": 0.50},
    "value_workshop": {"success_rate": 0.64, "avg_days_to_impact": 8, "stage_advance_rate": 0.38},
}


# ===================================================================
# HELPERS
# ===================================================================

def _recommend_for_deal(deal_name):
    """Generate ranked action recommendations for a deal."""
    ctx = _DEAL_CONTEXT.get(deal_name, {})
    stage = ctx.get("stage", "")
    blocker = ctx.get("blocker", "")
    recommendations = []
    for action_id, template in _ACTION_TEMPLATES.items():
        if stage in template["applicable_stages"] and blocker in template["applicable_blockers"]:
            outcome = _HISTORICAL_OUTCOMES.get(action_id, {})
            priority_score = (
                template["impact_score"] * 0.4 +
                outcome.get("success_rate", 0.5) * 100 * 0.3 +
                (100 - outcome.get("avg_days_to_impact", 5) * 10) * 0.3
            )
            recommendations.append({
                "action_id": action_id,
                "name": template["name"],
                "description": template["description"],
                "effort_hours": template["effort_hours"],
                "priority_score": round(priority_score, 1),
                "success_rate": outcome.get("success_rate", 0.5),
                "days_to_impact": outcome.get("avg_days_to_impact", 5),
            })
    return sorted(recommendations, key=lambda r: -r["priority_score"])


def _expected_impact(deal_name, action_id):
    """Forecast expected impact of an action on a deal."""
    ctx = _DEAL_CONTEXT.get(deal_name, {})
    outcome = _HISTORICAL_OUTCOMES.get(action_id, {})
    value = ctx.get("value", 0)
    success_rate = outcome.get("success_rate", 0.5)
    stage_advance = outcome.get("stage_advance_rate", 0.3)
    expected_value_impact = round(value * success_rate * stage_advance)
    return expected_value_impact


# ===================================================================
# AGENT CLASS
# ===================================================================

class NextBestActionAgent(BasicAgent):
    """
    Recommends prioritized next-best actions for pipeline deals.

    Operations:
        recommend_actions  - prioritized action recommendations per deal
        action_sequence    - sequenced multi-step action plans
        impact_forecast    - expected impact of recommended actions
        rep_assignments    - optimal rep assignment for actions
    """

    def __init__(self):
        self.name = "NextBestActionAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["recommend_actions", "action_sequence", "impact_forecast", "rep_assignments"],
                        "description": "The analysis to perform",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "recommend_actions")
        dispatch = {
            "recommend_actions": self._recommend_actions,
            "action_sequence": self._action_sequence,
            "impact_forecast": self._impact_forecast,
            "rep_assignments": self._rep_assignments,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"**Error:** Unknown operation '{op}'. Valid: {', '.join(dispatch.keys())}"
        return handler()

    # -- recommend_actions (flagship: prefers LIVE tenant, falls back) --
    def _recommend_actions(self) -> str:
        live = _live_open_deals()
        if live:
            sections = []
            total_actions = 0
            for d in sorted(live, key=lambda x: -x["value"]):
                recs = _recommend_for_live_deal(d)
                total_actions += len(recs)
                rows = ""
                for i, r in enumerate(recs[:4], 1):
                    rows += (f"| {i} | {r['name']} | {r['priority_score']} | "
                             f"{r['effort_hours']}h | {r['success_rate']:.0%} | {r['days_to_impact']}d |\n")
                sections.append(
                    f"**{d['name']} -- ${d['value']:,} ({d['stage']})**\n"
                    f"CRM close probability: {d['probability']}% | Owner: {d['owner']} | "
                    f"Risk/Health: n/a — enrichment seam\n\n"
                    f"| # | Action | Priority | Effort | Success Rate | Time to Impact |\n"
                    f"|---|--------|----------|--------|-------------|---------------|\n"
                    f"{rows}"
                )
            return (
                f"**Next Best Action Recommendations -- {len(live)} LIVE Open Deals** "
                f"(Static Dynamics 365 tenant)\n\n"
                f"Total actions recommended: **{total_actions}** — matched by real CRM stage; "
                f"blocker targeting stays off until you wire call analytics at the LIVE DATA SEAM.\n\n"
                + "\n---\n\n".join(sections)
                + f"\n\nSource: [Live Dynamics 365 opportunities + Action Library]\n"
                f"Agents: ActionRecommendationEngine"
            )
        sections = []
        total_actions = 0
        for deal_name in sorted(_DEAL_CONTEXT.keys(), key=lambda d: -_DEAL_CONTEXT[d]["value"]):
            ctx = _DEAL_CONTEXT[deal_name]
            recs = _recommend_for_deal(deal_name)
            total_actions += len(recs)

            rows = ""
            for i, r in enumerate(recs[:4], 1):
                rows += (f"| {i} | {r['name']} | {r['priority_score']} | "
                         f"{r['effort_hours']}h | {r['success_rate']:.0%} | {r['days_to_impact']}d |\n")

            urgency = "IMMEDIATE" if ctx["risk_score"] >= 60 else ("THIS WEEK" if ctx["risk_score"] >= 40 else "STANDARD")
            sections.append(
                f"**{deal_name} -- ${ctx['value']:,} ({ctx['stage']})**\n"
                f"Risk: {ctx['risk_score']}/100 | Health: {ctx['health_score']}/100 | Urgency: {urgency}\n\n"
                f"| # | Action | Priority | Effort | Success Rate | Time to Impact |\n"
                f"|---|--------|----------|--------|-------------|---------------|\n"
                f"{rows}"
            )

        return (
            f"**Next Best Action Recommendations -- {len(_DEAL_CONTEXT)} Deals**\n\n"
            f"Total actions recommended: **{total_actions}**\n\n"
            + "\n---\n\n".join(sections)
            + f"\n\nSource: [Deal Context + Historical Outcomes + Action Library]\n"
            f"Agents: ActionRecommendationEngine"
        )

    # -- action_sequence -----------------------------------------------
    def _action_sequence(self) -> str:
        sections = []
        for deal_name in sorted(_DEAL_CONTEXT.keys(), key=lambda d: -_DEAL_CONTEXT[d]["value"]):
            ctx = _DEAL_CONTEXT[deal_name]
            recs = _recommend_for_deal(deal_name)
            if not recs:
                continue

            day = 1
            sequence = []
            for r in recs[:4]:
                end_day = day + r["days_to_impact"] - 1
                sequence.append(f"- **Days {day}-{end_day}:** {r['name']} -- {r['description']}")
                day = end_day + 1

            total_days = day - 1
            sections.append(
                f"**{deal_name} -- ${ctx['value']:,}**\n"
                f"Total sequence: {total_days} days | Owner: {ctx['owner']}\n\n"
                + "\n".join(sequence)
                + f"\n- **Day {total_days + 1}:** Review progress and reassess\n"
            )

        return (
            f"**Action Sequences -- Multi-Step Plans**\n\n"
            f"Sequenced for optimal execution and minimal rep context-switching.\n\n"
            + "\n\n---\n\n".join(sections)
            + f"\n\nSource: [Action Sequencing Model + Rep Calendars]\n"
            f"Agents: SequencePlannerAgent"
        )

    # -- impact_forecast -----------------------------------------------
    def _impact_forecast(self) -> str:
        rows = ""
        total_expected = 0
        total_pipeline = 0

        for deal_name in sorted(_DEAL_CONTEXT.keys(), key=lambda d: -_DEAL_CONTEXT[d]["value"]):
            ctx = _DEAL_CONTEXT[deal_name]
            recs = _recommend_for_deal(deal_name)
            total_pipeline += ctx["value"]

            if recs:
                top_action = recs[0]
                impact = _expected_impact(deal_name, top_action["action_id"])
                total_expected += impact
                outcome = _HISTORICAL_OUTCOMES.get(top_action["action_id"], {})
                advance_pct = round(outcome.get("stage_advance_rate", 0.3) * 100)
                rows += (f"| {deal_name} | ${ctx['value']:,} | {top_action['name']} | "
                         f"${impact:,} | {advance_pct}% | {top_action['days_to_impact']}d |\n")

        roi_pct = round(total_expected / max(total_pipeline, 1) * 100, 1)

        return (
            f"**Impact Forecast -- Expected Outcomes**\n\n"
            f"Total pipeline: ${total_pipeline:,} | Expected value impact: ${total_expected:,}\n"
            f"Action ROI: {roi_pct}% of pipeline value influenced\n\n"
            f"| Deal | Value | Top Action | Expected Impact | Stage Advance | Timeline |\n"
            f"|------|-------|-----------|----------------|--------------|----------|\n"
            f"{rows}\n"
            f"**Assumptions:**\n"
            f"- Impact based on historical success rates for similar actions\n"
            f"- Stage advance probability assumes timely execution\n"
            f"- Expected value = Deal value x Success rate x Stage advance rate\n\n"
            f"Source: [Historical Outcomes + Predictive Model]\n"
            f"Agents: ForecastEngine"
        )

    # -- rep_assignments -----------------------------------------------
    def _rep_assignments(self) -> str:
        assignments = []
        for deal_name in sorted(_DEAL_CONTEXT.keys(), key=lambda d: -_DEAL_CONTEXT[d]["value"]):
            ctx = _DEAL_CONTEXT[deal_name]
            recs = _recommend_for_deal(deal_name)
            if not recs:
                continue

            top_action = recs[0]
            owner = ctx["owner"]
            owner_profile = _REP_PROFILES.get(owner, {})
            available = owner_profile.get("capacity", 12) - owner_profile.get("active_deals", 10)

            # Check if a specialist would be better
            best_rep = owner
            best_reason = "Current owner, maintains continuity"
            for rep_name, profile in _REP_PROFILES.items():
                rep_available = profile["capacity"] - profile["active_deals"]
                if rep_available > available and any(
                    s.lower() in top_action["description"].lower() for s in profile["strengths"]
                ):
                    best_rep = rep_name
                    best_reason = f"Specialist in {profile['specialty']}, {rep_available} slots available"
                    break

            assignments.append(
                f"| {deal_name} | ${ctx['value']:,} | {top_action['name']} | "
                f"{best_rep} | {best_reason} |\n"
            )

        rows = "".join(assignments)

        # Rep workload summary
        workload_rows = ""
        for rep_name, profile in _REP_PROFILES.items():
            assigned = sum(1 for d in _DEAL_CONTEXT.values() if d["owner"] == rep_name)
            available = profile["capacity"] - profile["active_deals"]
            workload_rows += f"| {rep_name} | {profile['title']} | {assigned} | {available} | {profile['specialty']} |\n"

        return (
            f"**Optimized Rep Assignments**\n\n"
            f"| Deal | Value | Action | Assigned To | Rationale |\n"
            f"|------|-------|--------|------------|----------|\n"
            f"{rows}\n"
            f"**Team Workload:**\n\n"
            f"| Rep | Title | Active Deals | Available Slots | Specialty |\n"
            f"|-----|-------|-------------|----------------|----------|\n"
            f"{workload_rows}\n"
            f"**Optimization Notes:**\n"
            f"- Assignments balance workload with deal-specific expertise\n"
            f"- Cross-assignments recommended when specialist skills needed\n"
            f"- Review assignments weekly in pipeline meeting\n\n"
            f"Source: [Rep Profiles + Workload Data + Skill Matrix]\n"
            f"Agents: AssignmentOptimizer"
        )


if __name__ == "__main__":
    agent = NextBestActionAgent()
    print("=" * 70)
    print("LIVE TENANT RECOMMENDATIONS (fetched over HTTP; embedded demo offline)")
    print(agent.perform(operation="recommend_actions"))
    print()
    print("=" * 70)
    print("EMBEDDED DEMO (works offline, simulated)")
    print(agent.perform(operation="action_sequence"))
    print()
    print("=" * 70)
    print(agent.perform(operation="rep_assignments"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
