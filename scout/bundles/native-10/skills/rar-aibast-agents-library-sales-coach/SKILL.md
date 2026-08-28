---
name: "rar-aibast-agents-library-sales-coach"
description: "Coaches reps with live pipeline stats from a simulated Dynamics 365 tenant plus call reviews and skill plans, with offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/sales_coach", "rar_sha256": "ccbfc298d6e53e7aef78b65e06bf84f2c5abe33fddc9ad5d705fcfa671695585", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["sales", "coaching", "training", "performance", "call-review"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/sales_coach`. The original RAPP
agent is preserved byte-for-byte in `sales_coach_agent.py` and in the RCI capsule.

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

Sales Coach Agent — a template you are meant to mutate.

AI-powered sales coaching with call reviews, skill assessments,
personalized coaching plans, and performance dashboards. Rep pipeline
numbers (open value, won/lost, win rate) are computed from real CRM
opportunities; call scores and skill rubrics come from your coaching
platform.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="skill_assessment", rep_name="Sam Patel")
     — Sam Patel is a real seeded opportunity owner in the tenant; the
     agent computes his live pipeline and win rate from his deals.
  2. No network? Everything falls back to the embedded demo layer below
     (_SKILL_ASSESSMENTS / _CALL_TRANSCRIPTS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SALES_COACH_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from Salesforce), or replace
     _fetch_collection() with your CRM client. The fields the rest of
     the file needs are listed in _normalize_live_rep() — call scores
     for live reps are labeled "n/a — enrichment seam"; wire your call
     recording / conversation intelligence platform there.

OPERATIONS
  call_review | skill_assessment | coaching_plan | performance_dashboard
  kwargs: operation (required), rep_name (embedded 'Alex Rivera' or a
  live tenant opportunity owner like 'Sam Patel'), call_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "call_id": {
      "description": "Call ID to review (e.g. 'CALL-901')",
      "type": "string"
    },
    "operation": {
      "description": "The coaching operation to perform",
      "enum": [
        "call_review",
        "skill_assessment",
        "coaching_plan",
        "performance_dashboard"
      ],
      "type": "string"
    },
    "rep_name": {
      "description": "Sales rep name (e.g. 'Alex Rivera')",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sales_coach_agent.py` and embedded as the fenced Python below (sha256 ccbfc298d6e53e7a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sales_coach_agent.py` first:

```bash
python3 sales_coach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sales_coach_agent.py   # or on stdin
python3 sales_coach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Sales Coach Agent — a template you are meant to mutate.

AI-powered sales coaching with call reviews, skill assessments,
personalized coaching plans, and performance dashboards. Rep pipeline
numbers (open value, won/lost, win rate) are computed from real CRM
opportunities; call scores and skill rubrics come from your coaching
platform.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="skill_assessment", rep_name="Sam Patel")
     — Sam Patel is a real seeded opportunity owner in the tenant; the
     agent computes his live pipeline and win rate from his deals.
  2. No network? Everything falls back to the embedded demo layer below
     (_SKILL_ASSESSMENTS / _CALL_TRANSCRIPTS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SALES_COACH_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from Salesforce), or replace
     _fetch_collection() with your CRM client. The fields the rest of
     the file needs are listed in _normalize_live_rep() — call scores
     for live reps are labeled "n/a — enrichment seam"; wire your call
     recording / conversation intelligence platform there.

OPERATIONS
  call_review | skill_assessment | coaching_plan | performance_dashboard
  kwargs: operation (required), rep_name (embedded 'Alex Rivera' or a
  live tenant opportunity owner like 'Sam Patel'), call_id
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/sales_coach",
    "version": "1.1.0",
    "display_name": "Sales Coach",
    "description": "Coaches reps with live pipeline stats from a simulated Dynamics 365 tenant plus call reviews and skill plans, with offline fallback.",
    "author": "AIBAST",
    "tags": ["sales", "coaching", "training", "performance", "call-review"],
    "category": "general",
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
#   export SALES_COACH_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_rep().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "SALES_COACH_DATA_URL",
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


def _normalize_live_rep(owner_name, opportunities):
    """Project a rep's Dynamics opportunities onto the pipeline shape
    this agent uses. THIS is the contract your replacement data source
    must meet — a dict with these keys. Pipeline numbers are computed
    from real records; None means 'not knowable from CRM alone' and
    renderers label it as an enrichment seam (call scores live in your
    conversation-intelligence platform)."""
    mine = [o for o in opportunities if o.get("owneridname") == owner_name]
    open_opps = [o for o in mine if o.get("statecode") == 0]
    won = sum(1 for o in mine if o.get("statecode") == 1)
    lost = sum(1 for o in mine if o.get("statecode") == 2)
    closed = won + lost
    return {
        "name": owner_name,
        "open_count": len(open_opps),
        "open_value": sum(float(o.get("estimatedvalue") or 0) for o in open_opps),
        "won": won,
        "lost": lost,
        "win_rate": round(won / closed * 100) if closed else None,
        "overall": None,            # enrichment seam — wire your coaching platform
        "quota_attainment": None,   # enrichment seam — wire your quota system
        "scores": None,             # enrichment seam — wire call recordings
        "_live": True,
    }


def _live_rep_roster():
    """name-keyed dict of live tenant opportunity owners; {} offline."""
    opportunities = _fetch_collection("opportunities")
    owners = sorted({o.get("owneridname") for o in opportunities if o.get("owneridname")})
    return {name: _normalize_live_rep(name, opportunities) for name in owners}


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_CALL_TRANSCRIPTS = {
    "CALL-901": {
        "id": "CALL-901", "rep": "Alex Rivera", "prospect": "Jennifer Walsh (TechVantage)",
        "date": "2025-11-12", "duration_min": 32, "type": "Discovery",
        "outcome": "Meeting Scheduled", "deal_value": 185000,
        "scores": {"opening": 85, "discovery_questions": 72, "active_listening": 90, "value_articulation": 68, "next_steps": 95, "objection_handling": 60},
        "highlights": ["Strong rapport building in first 3 minutes", "Identified 3 key pain points", "Secured next meeting with VP"],
        "improvements": ["Ask more open-ended discovery questions", "Missed opportunity to quantify business impact", "Did not address competitor mention"],
        "talk_ratio": {"rep": 58, "prospect": 42},
    },
    "CALL-902": {
        "id": "CALL-902", "rep": "Sarah Kim", "prospect": "David Park (Greenridge Partners)",
        "date": "2025-11-11", "duration_min": 45, "type": "Proposal Review",
        "outcome": "Verbal Agreement", "deal_value": 72000,
        "scores": {"opening": 92, "discovery_questions": 88, "active_listening": 85, "value_articulation": 91, "next_steps": 88, "objection_handling": 82},
        "highlights": ["Excellent value quantification with ROI numbers", "Handled pricing objection confidently", "Clear mutual action plan"],
        "improvements": ["Could have involved more stakeholders", "Missed upsell opportunity for Analytics Pro"],
        "talk_ratio": {"rep": 45, "prospect": 55},
    },
    "CALL-903": {
        "id": "CALL-903", "rep": "Tom Rivera", "prospect": "Maria Santos (BlueHorizon Health)",
        "date": "2025-11-10", "duration_min": 28, "type": "Renewal Discussion",
        "outcome": "Expansion Identified", "deal_value": 240000,
        "scores": {"opening": 78, "discovery_questions": 65, "active_listening": 82, "value_articulation": 75, "next_steps": 70, "objection_handling": 55},
        "highlights": ["Customer mentioned expansion plans", "Good understanding of healthcare compliance needs"],
        "improvements": ["Rushed through opening - no personal connection", "Failed to probe deeper on expansion timeline", "Weak close - no specific next meeting date", "Did not handle budget concern effectively"],
        "talk_ratio": {"rep": 65, "prospect": 35},
    },
}

_SCORING_RUBRICS = {
    "opening": {"weight": 0.10, "criteria": ["Warm greeting and rapport", "Agenda setting", "Time confirmation", "Reference to previous interactions"]},
    "discovery_questions": {"weight": 0.25, "criteria": ["Open-ended questions", "Pain point identification", "Budget qualification", "Timeline discovery", "Decision process mapping"]},
    "active_listening": {"weight": 0.15, "criteria": ["Paraphrasing", "Acknowledgment phrases", "Follow-up on responses", "Note-taking signals"]},
    "value_articulation": {"weight": 0.20, "criteria": ["ROI quantification", "Customer-specific benefits", "Competitive differentiation", "Social proof/references"]},
    "next_steps": {"weight": 0.15, "criteria": ["Clear action items", "Mutual commitment", "Timeline specified", "Calendar invite sent"]},
    "objection_handling": {"weight": 0.15, "criteria": ["Acknowledge concern", "Clarifying questions", "Reframe with value", "Proof points", "Trial close after handling"]},
}

_SKILL_ASSESSMENTS = {
    "Alex Rivera": {"overall": 78, "tenure_months": 18, "quota_attainment": 0.92, "scores": {"opening": 85, "discovery": 72, "listening": 90, "value": 68, "closing": 82, "objections": 60}, "trend": "Improving", "rank": 3},
    "Sarah Kim": {"overall": 88, "tenure_months": 36, "quota_attainment": 1.15, "scores": {"opening": 92, "discovery": 88, "listening": 85, "value": 91, "closing": 88, "objections": 82}, "trend": "Consistent", "rank": 1},
    "Tom Rivera": {"overall": 71, "tenure_months": 12, "quota_attainment": 0.78, "scores": {"opening": 78, "discovery": 65, "listening": 82, "value": 75, "closing": 70, "objections": 55}, "trend": "Needs Improvement", "rank": 5},
}

_COACHING_RECOMMENDATIONS = {
    "objection_handling": [
        {"activity": "Role-play: Price Objection Scenarios", "duration": "30 min", "frequency": "2x/week", "resource": "Objection Handling Playbook Ch. 4"},
        {"activity": "Review 5 recorded calls where objections were handled well", "duration": "45 min", "frequency": "1x/week", "resource": "Call Library - Top Performers"},
        {"activity": "Practice the Feel-Felt-Found framework", "duration": "15 min", "frequency": "Daily", "resource": "Sales Methodology Guide"},
    ],
    "discovery_questions": [
        {"activity": "SPIN Selling question practice", "duration": "20 min", "frequency": "Daily", "resource": "SPIN Selling Workbook"},
        {"activity": "Shadow top performer discovery calls", "duration": "60 min", "frequency": "2x/week", "resource": "Peer Coaching Program"},
        {"activity": "Complete BANT qualification checklist review", "duration": "15 min", "frequency": "After each call", "resource": "Qualification Framework"},
    ],
    "value_articulation": [
        {"activity": "Customer ROI case study review", "duration": "30 min", "frequency": "3x/week", "resource": "Customer Success Stories Library"},
        {"activity": "Practice value proposition delivery", "duration": "15 min", "frequency": "Daily", "resource": "Value Prop Toolkit"},
        {"activity": "Create custom ROI calculations for top 5 prospects", "duration": "45 min", "frequency": "1x/week", "resource": "ROI Calculator Tool"},
    ],
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _resolve_rep(query):
    """Embedded demo reps first, then live tenant opportunity owners.
    Returns (rep_name, is_live)."""
    if not query:
        return "Alex Rivera", False
    q = query.lower().strip()
    for name in _SKILL_ASSESSMENTS:
        if q in name.lower():
            return name, False
    for name in _live_rep_roster():
        if q in name.lower():
            return name, True
    return "Alex Rivera", False


def _weighted_call_score(scores):
    total = 0
    for skill, rubric in _SCORING_RUBRICS.items():
        total += scores.get(skill, 0) * rubric["weight"]
    return round(total)


def _identify_weakest_skills(rep_name, top_n=2):
    assessment = _SKILL_ASSESSMENTS.get(rep_name, {})
    scores = assessment.get("scores", {})
    sorted_skills = sorted(scores.items(), key=lambda x: x[1])
    return sorted_skills[:top_n]


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class SalesCoachAgent(BasicAgent):
    """
    Sales coaching assistant.

    Operations:
        call_review           - review and score a sales call
        skill_assessment      - assess a rep's skill profile
        coaching_plan         - generate a personalized coaching plan
        performance_dashboard - team performance overview
    """

    def __init__(self):
        self.name = "SalesCoachAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "call_review", "skill_assessment",
                            "coaching_plan", "performance_dashboard",
                        ],
                        "description": "The coaching operation to perform",
                    },
                    "rep_name": {
                        "type": "string",
                        "description": "Sales rep name (e.g. 'Alex Rivera')",
                    },
                    "call_id": {
                        "type": "string",
                        "description": "Call ID to review (e.g. 'CALL-901')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "performance_dashboard")
        dispatch = {
            "call_review": self._call_review,
            "skill_assessment": self._skill_assessment,
            "coaching_plan": self._coaching_plan,
            "performance_dashboard": self._performance_dashboard,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(kwargs)

    # ── call_review ────────────────────────────────────────────
    def _call_review(self, params):
        call_id = params.get("call_id", "CALL-901")
        call = _CALL_TRANSCRIPTS.get(call_id, list(_CALL_TRANSCRIPTS.values())[0])
        weighted = _weighted_call_score(call["scores"])
        score_rows = "\n".join(f"| {skill.replace('_', ' ').title()} | {score}/100 | {_SCORING_RUBRICS[skill]['weight']:.0%} |" for skill, score in call["scores"].items())
        highlights = "\n".join(f"- {h}" for h in call["highlights"])
        improvements = "\n".join(f"- {i}" for i in call["improvements"])
        return (
            f"**Call Review: {call['id']}** (embedded demo call — simulated)\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Rep | {call['rep']} |\n"
            f"| Prospect | {call['prospect']} |\n"
            f"| Date | {call['date']} |\n"
            f"| Duration | {call['duration_min']} min |\n"
            f"| Type | {call['type']} |\n"
            f"| Outcome | {call['outcome']} |\n"
            f"| **Overall Score** | **{weighted}/100** |\n\n"
            f"**Skill Scores:**\n\n"
            f"| Skill | Score | Weight |\n|---|---|---|\n"
            f"{score_rows}\n\n"
            f"**Talk Ratio:** Rep {call['talk_ratio']['rep']}% / Prospect {call['talk_ratio']['prospect']}%\n\n"
            f"**Highlights:**\n{highlights}\n\n"
            f"**Areas for Improvement:**\n{improvements}\n\n"
            f"Source: [Call Recording + AI Analysis]\nAgents: SalesCoachAgent"
        )

    # ── skill_assessment ───────────────────────────────────────
    def _skill_assessment(self, params):
        rep_name, is_live = _resolve_rep(params.get("rep_name", ""))
        if is_live:
            rep = _live_rep_roster()[rep_name]
            win_rate = f"{rep['win_rate']}%" if rep["win_rate"] is not None else "n/a (no closed deals yet)"
            return (
                f"**Skill Assessment: {rep_name}** (LIVE rep from the Aster Lane Dynamics 365 tenant)\n\n"
                f"| Metric | Value |\n|---|---|\n"
                f"| Open Pipeline | {rep['open_count']} deals, ${rep['open_value']:,.0f} |\n"
                f"| Won / Lost | {rep['won']} / {rep['lost']} |\n"
                f"| Win Rate | {win_rate} |\n"
                f"| Overall Skill Score | n/a — enrichment seam |\n"
                f"| Quota Attainment | n/a — enrichment seam |\n\n"
                f"Pipeline numbers above are computed from this rep's real "
                f"opportunity records in the live tenant. Skill scores are an "
                f"enrichment seam — wire your call-recording / conversation-"
                f"intelligence platform to populate them.\n\n"
                f"Source: [Live Dynamics 365 Tenant — opportunities]\nAgents: SalesCoachAgent"
            )
        assessment = _SKILL_ASSESSMENTS[rep_name]
        score_rows = "\n".join(f"| {skill.title()} | {score}/100 |" for skill, score in assessment["scores"].items())
        weakest = _identify_weakest_skills(rep_name)
        weak_list = "\n".join(f"- {skill.title()}: {score}/100" for skill, score in weakest)
        return (
            f"**Skill Assessment: {rep_name}** (embedded demo rep — simulated)\n\n"
            f"| Metric | Value |\n|---|---|\n"
            f"| Overall Score | {assessment['overall']}/100 |\n"
            f"| Tenure | {assessment['tenure_months']} months |\n"
            f"| Quota Attainment | {assessment['quota_attainment']:.0%} |\n"
            f"| Trend | {assessment['trend']} |\n"
            f"| Team Rank | #{assessment['rank']} |\n\n"
            f"**Skill Breakdown:**\n\n| Skill | Score |\n|---|---|\n{score_rows}\n\n"
            f"**Focus Areas (weakest skills):**\n{weak_list}\n\n"
            f"Source: [Coaching Platform + CRM]\nAgents: SalesCoachAgent"
        )

    # ── coaching_plan ──────────────────────────────────────────
    def _coaching_plan(self, params):
        rep_name, is_live = _resolve_rep(params.get("rep_name", ""))
        if is_live:
            rep = _live_rep_roster()[rep_name]
            return (
                f"**Coaching Plan: {rep_name}** (LIVE rep from the Aster Lane Dynamics 365 tenant)\n\n"
                f"Live pipeline: {rep['open_count']} open deals (${rep['open_value']:,.0f}), "
                f"{rep['won']} won, {rep['lost']} lost.\n\n"
                f"Skill scores for this rep are n/a — enrichment seam. A coaching "
                f"plan needs call-level scoring; wire your conversation-"
                f"intelligence platform at the LIVE DATA SEAM, then this operation "
                f"will target the rep's weakest skills automatically (see the "
                f"embedded demo reps for the full plan shape).\n\n"
                f"Source: [Live Dynamics 365 Tenant + Coaching Platform seam]\nAgents: SalesCoachAgent"
            )
        weakest = _identify_weakest_skills(rep_name)
        plan = ""
        for skill, score in weakest:
            recs = _COACHING_RECOMMENDATIONS.get(skill, _COACHING_RECOMMENDATIONS.get("objection_handling", []))
            plan += f"**{skill.replace('_', ' ').title()}** (Current: {score}/100)\n\n"
            for rec in recs:
                plan += f"- {rec['activity']} ({rec['duration']}, {rec['frequency']})\n  Resource: {rec['resource']}\n"
            plan += "\n"
        return (
            f"**Coaching Plan: {rep_name}** (embedded demo rep — simulated)\n\n"
            f"**Assessment:** {_SKILL_ASSESSMENTS[rep_name]['overall']}/100 overall\n"
            f"**Goal:** Improve weakest skills by 15+ points in 30 days\n\n"
            f"{plan}"
            f"**Timeline:** 4-week program with weekly check-ins\n"
            f"**Success Metrics:** Skill score improvement, call conversion rate, quota attainment\n\n"
            f"Source: [Coaching Platform]\nAgents: SalesCoachAgent"
        )

    # ── performance_dashboard ──────────────────────────────────
    def _performance_dashboard(self, params):
        rows = ""
        for name, a in sorted(_SKILL_ASSESSMENTS.items(), key=lambda x: x[1]["overall"], reverse=True):
            rows += f"| {name} | {a['overall']}/100 | {a['quota_attainment']:.0%} | {a['trend']} | #{a['rank']} |\n"
        team_avg = sum(a["overall"] for a in _SKILL_ASSESSMENTS.values()) / len(_SKILL_ASSESSMENTS)
        team_quota = sum(a["quota_attainment"] for a in _SKILL_ASSESSMENTS.values()) / len(_SKILL_ASSESSMENTS)
        live = _live_rep_roster()
        if live:
            live_rows = ""
            for name, rep in live.items():
                win_rate = f"{rep['win_rate']}%" if rep["win_rate"] is not None else "n/a"
                live_rows += f"| {name} | {rep['open_count']} | ${rep['open_value']:,.0f} | {rep['won']} | {rep['lost']} | {win_rate} |\n"
            live_section = (
                f"**Live Pipeline by Rep (LIVE Dynamics 365 tenant — computed from real opportunity records):**\n\n"
                f"| Rep | Open Deals | Open Value | Won | Lost | Win Rate |\n|---|---|---|---|---|---|\n"
                f"{live_rows}\n"
            )
        else:
            live_section = "**Live Pipeline by Rep:** live tenant unreachable — embedded demo data only.\n\n"
        return (
            f"**Sales Performance Dashboard**\n\n"
            f"**Team Summary (embedded demo coaching data — simulated):**\n"
            f"- Team Size: {len(_SKILL_ASSESSMENTS)}\n"
            f"- Avg Score: {team_avg:.0f}/100\n"
            f"- Avg Quota Attainment: {team_quota:.0%}\n"
            f"- Calls Reviewed: {len(_CALL_TRANSCRIPTS)}\n\n"
            f"**Individual Performance (simulated):**\n\n"
            f"| Rep | Score | Quota | Trend | Rank |\n|---|---|---|---|---|\n"
            f"{rows}\n"
            f"{live_section}"
            f"Source: [Coaching Platform + Live Dynamics 365 Tenant]\nAgents: SalesCoachAgent"
        )


if __name__ == "__main__":
    agent = SalesCoachAgent()
    print("=" * 60)
    print("EMBEDDED DEMO REP (works offline)")
    print(agent.perform(operation="skill_assessment", rep_name="Alex Rivera"))
    print()
    print("=" * 60)
    print("LIVE TENANT REP (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="skill_assessment", rep_name="Sam Patel"))
    print()
    print("=" * 60)
    print(agent.perform(operation="performance_dashboard"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
