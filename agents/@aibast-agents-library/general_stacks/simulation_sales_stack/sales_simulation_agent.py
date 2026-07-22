"""
Sales Simulation Agent — a template you are meant to mutate.

Simulates sales scenarios with buyer personas, objection practice, and
performance scoring for training and preparation. Scenarios can be
built from REAL open opportunities so reps rehearse the deals they are
actually working.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live opportunities and accounts over real
     HTTP from the globally hosted Static Dynamics 365 tenant (Aster
     Lane Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="scenario_setup",
                  scenario_id="Copper Kite Design")
     — builds a role-play scenario from the tenant's real seeded
     "Copper Kite Design — Secure print rollout" opportunity ($5,700,
     50% close probability).
  2. No network? Everything falls back to the embedded demo layer below
     (_SCENARIOS / _BUYER_PERSONAS) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SALES_SIMULATION_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from Salesforce), or replace
     _fetch_collection() with your CRM client. The fields the rest of
     the file needs are listed in _normalize_live_scenario() —
     difficulty is derived from close probability by a stated rule, and
     the buyer's actual personality is an enrichment seam (wire your
     meeting notes).

OPERATIONS
  scenario_setup | run_simulation | objection_practice
  | performance_score
  kwargs: operation (required), scenario_id (embedded 'SCN-001' or a
  live opportunity/account name like 'Copper Kite Design')
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
    "name": "@aibast-agents-library/sales_simulation",
    "version": "1.1.0",
    "display_name": "Sales Simulation",
    "description": "Builds sales role-play scenarios from live opportunities in a simulated Dynamics 365 tenant, with personas, scoring, and offline fallback.",
    "author": "AIBAST",
    "tags": ["sales", "simulation", "training", "objections", "personas", "scoring"],
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
#   export SALES_SIMULATION_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_scenario().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "SALES_SIMULATION_DATA_URL",
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


def _normalize_live_scenario(opp, accounts_by_name):
    """Project a Dynamics opportunity onto the scenario shape this agent
    uses. THIS is the contract your replacement data source must meet —
    a dict with these keys. Difficulty is DERIVED from close probability
    (<=35% Advanced, 36-60% Intermediate, >60% Beginner) — a training
    rule, not CRM data. The buyer's real personality is an enrichment
    seam; wire your meeting notes there."""
    prob = int(opp.get("closeprobability") or 0)
    account_name = opp.get("customeridname", "Unknown account")
    account = accounts_by_name.get(account_name, {})
    if prob <= 35:
        difficulty = "Advanced"
    elif prob <= 60:
        difficulty = "Intermediate"
    else:
        difficulty = "Beginner"
    return {
        "id": opp.get("name", account_name),
        "name": opp.get("name", "Live opportunity"),
        "difficulty": difficulty,
        "industry": account.get("industrycode", "Unknown"),
        "deal_size": float(opp.get("estimatedvalue") or 0),
        "stage": f"Open — {prob}% close probability",
        "context": (
            f"Real open deal with {account_name} "
            f"(owner: {opp.get('owneridname', 'unassigned')}; est. close "
            f"{str(opp.get('estimatedclosedate', ''))[:10]}). "
            f"{opp.get('description', '')}"
        ),
        "objectives": [
            "Confirm the pains behind this opportunity with open questions",
            "Validate budget against the recorded estimated value",
            "Map the decision process and any missing stakeholders",
            "Advance the close probability with a concrete next step",
        ],
        "time_limit_min": 30,
        "_live": True,
    }


def _live_scenarios():
    """Scenario-shaped dicts for live OPEN opportunities; [] offline."""
    opportunities = _fetch_collection("opportunities")
    if not opportunities:
        return []
    accounts_by_name = {a.get("name", ""): a for a in _fetch_collection("accounts")}
    return [
        _normalize_live_scenario(o, accounts_by_name)
        for o in opportunities
        if o.get("statecode") == 0
    ]


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_SCENARIOS = {
    "SCN-001": {
        "id": "SCN-001", "name": "Enterprise Discovery Call", "difficulty": "Intermediate",
        "industry": "Financial Services", "deal_size": 250000, "stage": "Discovery",
        "context": "First meeting with VP of Operations at a mid-size bank. They reached out after seeing a case study about a competitor.",
        "objectives": ["Identify top 3 pain points", "Qualify budget and timeline", "Map decision-making process", "Secure follow-up with technical team"],
        "time_limit_min": 30,
    },
    "SCN-002": {
        "id": "SCN-002", "name": "Competitive Displacement", "difficulty": "Advanced",
        "industry": "Healthcare", "deal_size": 180000, "stage": "Proposal",
        "context": "The prospect is using Competitor B and their contract ends in 60 days. They are evaluating alternatives due to poor support.",
        "objectives": ["Position against Competitor B", "Address migration concerns", "Present ROI over 3 years", "Get verbal commitment to move forward"],
        "time_limit_min": 45,
    },
    "SCN-003": {
        "id": "SCN-003", "name": "Renewal with Expansion", "difficulty": "Beginner",
        "industry": "Technology", "deal_size": 95000, "stage": "Negotiation",
        "context": "Existing customer for 2 years. Happy with the product but budget is tight. They need 50 additional licenses.",
        "objectives": ["Secure renewal commitment", "Present expansion pricing", "Handle budget objection", "Agree on implementation timeline"],
        "time_limit_min": 25,
    },
}

_BUYER_PERSONAS = {
    "analytical_cfo": {
        "name": "The Analytical CFO", "role": "Chief Financial Officer",
        "personality": "Data-driven, skeptical, asks for ROI proof",
        "priorities": ["Cost reduction", "Compliance", "Risk mitigation"],
        "communication_style": "Formal, numbers-focused, wants written proposals",
        "common_objections": ["Show me the ROI data", "What's the total cost of ownership?", "How does this compare to building in-house?"],
        "decision_factors": {"price": 0.35, "roi": 0.30, "risk": 0.20, "references": 0.15},
    },
    "visionary_cto": {
        "name": "The Visionary CTO", "role": "Chief Technology Officer",
        "personality": "Innovation-focused, technical depth, future-looking",
        "priorities": ["Scalability", "Integration capabilities", "Technical architecture"],
        "communication_style": "Technical, whiteboard sessions, wants demos",
        "common_objections": ["Can it handle our scale?", "What about vendor lock-in?", "How does the API compare?"],
        "decision_factors": {"technology": 0.35, "scalability": 0.25, "integration": 0.25, "support": 0.15},
    },
    "pragmatic_vp_ops": {
        "name": "The Pragmatic VP Ops", "role": "VP of Operations",
        "personality": "Results-oriented, implementation-focused, timeline-driven",
        "priorities": ["Time to value", "Ease of deployment", "Team adoption"],
        "communication_style": "Direct, agenda-driven, wants implementation plans",
        "common_objections": ["What's the implementation timeline?", "How much training does my team need?", "What if adoption is low?"],
        "decision_factors": {"implementation": 0.30, "adoption": 0.25, "support": 0.25, "price": 0.20},
    },
}

_OBJECTION_LIBRARY = {
    "price": {
        "objection": "Your solution is too expensive compared to alternatives.",
        "category": "Price", "frequency": "Very Common",
        "recommended_response": "I understand budget is important. Let me walk through the total value - our customers typically see 3.2x ROI within 18 months. When you factor in the cost of the problem you're solving ($X/month in lost productivity), the investment pays for itself in Q2.",
        "framework": "Acknowledge > Quantify Value > Reframe as Investment",
        "success_rate": 0.65,
    },
    "competitor": {
        "objection": "We're already evaluating [Competitor] and they seem to have similar features.",
        "category": "Competition", "frequency": "Common",
        "recommended_response": "It's smart to evaluate options. Many of our current customers evaluated [Competitor] as well. What they found is that our platform offers significantly better [specific differentiator]. Would it be helpful if I connected you with a customer who made that exact switch?",
        "framework": "Validate > Differentiate > Offer Proof",
        "success_rate": 0.55,
    },
    "timing": {
        "objection": "This isn't a priority for us right now.",
        "category": "Timing", "frequency": "Common",
        "recommended_response": "I completely understand. Can I ask what would need to change for this to become a priority? The reason I ask is that our customers who waited reported the problem costing them approximately $X per quarter.",
        "framework": "Acknowledge > Probe Trigger > Quantify Cost of Inaction",
        "success_rate": 0.42,
    },
    "authority": {
        "objection": "I'd need to get buy-in from several other stakeholders.",
        "category": "Authority", "frequency": "Very Common",
        "recommended_response": "That makes sense for a decision of this magnitude. Who else would be involved? I'd be happy to prepare tailored materials for each stakeholder's perspective - whether that's the technical team, finance, or executive sponsor.",
        "framework": "Validate > Map Stakeholders > Offer Support",
        "success_rate": 0.72,
    },
}

_SCORING_CRITERIA = {
    "opening": {"weight": 0.10, "max_points": 10, "criteria": "Professional opening, agenda, time check"},
    "discovery": {"weight": 0.25, "max_points": 25, "criteria": "Open questions, pain identification, qualification"},
    "value_prop": {"weight": 0.20, "max_points": 20, "criteria": "Customer-specific benefits, ROI, differentiation"},
    "objection_handling": {"weight": 0.20, "max_points": 20, "criteria": "Framework usage, empathy, evidence-based"},
    "closing": {"weight": 0.15, "max_points": 15, "criteria": "Clear next steps, mutual commitment, urgency"},
    "professionalism": {"weight": 0.10, "max_points": 10, "criteria": "Tone, active listening, adaptability"},
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _resolve_scenario(query):
    """Embedded demo scenarios first, then scenarios built from live
    open opportunities. Returns (scenario, is_live)."""
    q = (query or "").strip()
    if not q:
        return _SCENARIOS["SCN-001"], False
    qu = q.upper()
    for key in _SCENARIOS:
        if key in qu:
            return _SCENARIOS[key], False
    ql = q.lower()
    for scn in _live_scenarios():
        if ql in scn["name"].lower():
            return scn, True
    return _SCENARIOS["SCN-001"], False


def _compute_simulation_score(performance):
    total = 0
    for skill, criteria in _SCORING_CRITERIA.items():
        score = performance.get(skill, criteria["max_points"] * 0.7)
        total += score * criteria["weight"] / criteria["max_points"] * 100
    return round(total)


_SAMPLE_PERFORMANCE = {"opening": 8, "discovery": 18, "value_prop": 14, "objection_handling": 16, "closing": 11, "professionalism": 9}


def _scenario_source_line(is_live):
    if is_live:
        return "Scenario source: LIVE opportunity from the Aster Lane Dynamics 365 tenant"
    return "Scenario source: embedded demo layer (simulated)"


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class SalesSimulationAgent(BasicAgent):
    """
    Sales simulation and training agent.

    Operations:
        scenario_setup      - set up a simulation scenario
        run_simulation      - run and score a simulated sales call
        objection_practice  - practice handling specific objections
        performance_score   - detailed scoring of simulation performance
    """

    def __init__(self):
        self.name = "SalesSimulationAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "scenario_setup", "run_simulation",
                            "objection_practice", "performance_score",
                        ],
                        "description": "The simulation operation to perform",
                    },
                    "scenario_id": {
                        "type": "string",
                        "description": "Scenario ID (e.g. 'SCN-001')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "scenario_setup")
        scenario, is_live = _resolve_scenario(kwargs.get("scenario_id", ""))
        dispatch = {
            "scenario_setup": self._scenario_setup,
            "run_simulation": self._run_simulation,
            "objection_practice": self._objection_practice,
            "performance_score": self._performance_score,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(scenario, is_live)

    # ── scenario_setup ─────────────────────────────────────────
    def _scenario_setup(self, scn, is_live):
        objectives = "\n".join(f"{i+1}. {o}" for i, o in enumerate(scn["objectives"]))
        persona_rows = ""
        for pid, p in _BUYER_PERSONAS.items():
            persona_rows += f"| {p['name']} | {p['role']} | {p['personality'][:40]} | {', '.join(p['priorities'][:2])} |\n"
        return (
            f"**Simulation Setup: {scn['name']}**\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Scenario | {scn['id']} |\n"
            f"| Difficulty | {scn['difficulty']}{' (derived from close probability)' if is_live else ''} |\n"
            f"| Industry | {scn['industry']} |\n"
            f"| Deal Size | ${scn['deal_size']:,.0f} |\n"
            f"| Stage | {scn['stage']} |\n"
            f"| Time Limit | {scn['time_limit_min']} minutes |\n\n"
            f"**Context:** {scn['context']}\n\n"
            f"**Objectives:**\n{objectives}\n\n"
            f"**Available Buyer Personas** (training archetypes — the real "
            f"buyer's personality is an enrichment seam):\n\n"
            f"| Persona | Role | Personality | Priorities |\n|---|---|---|---|\n"
            f"{persona_rows}\n"
            f"{_scenario_source_line(is_live)}\n"
            f"Source: [Sales Training Platform + Live Dynamics 365 Tenant]\nAgents: SalesSimulationAgent"
        )

    # ── run_simulation ─────────────────────────────────────────
    def _run_simulation(self, scn, is_live):
        score = _compute_simulation_score(_SAMPLE_PERFORMANCE)
        perf_rows = ""
        for skill, criteria in _SCORING_CRITERIA.items():
            pts = _SAMPLE_PERFORMANCE.get(skill, 0)
            perf_rows += f"| {skill.replace('_', ' ').title()} | {pts}/{criteria['max_points']} | {criteria['weight']:.0%} | {criteria['criteria'][:40]} |\n"
        grade = "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else ("D" if score >= 60 else "F")))
        return (
            f"**Simulation Results: {scn['name']}** (simulated sample run)\n\n"
            f"**Overall Score: {score}/100 (Grade: {grade})**\n\n"
            f"| Skill | Points | Weight | Criteria |\n|---|---|---|---|\n"
            f"{perf_rows}\n"
            f"**Outcome:** {'Deal Advanced' if score >= 70 else 'Deal Stalled'}\n\n"
            f"**Feedback:**\n"
            f"- Strong opening and professionalism throughout\n"
            f"- Discovery was thorough but missed budget qualification\n"
            f"- Objection handling was effective on price, needs work on timing\n"
            f"- Clear next steps established\n\n"
            f"{_scenario_source_line(is_live)}\n"
            f"Source: [Simulation Engine]\nAgents: SalesSimulationAgent"
        )

    # ── objection_practice ─────────────────────────────────────
    def _objection_practice(self, scn, is_live):
        obj_rows = ""
        for key, obj in _OBJECTION_LIBRARY.items():
            obj_rows += f"| {key.title()} | {obj['category']} | {obj['frequency']} | {obj['success_rate']:.0%} |\n"
        detail_sections = ""
        for key, obj in _OBJECTION_LIBRARY.items():
            detail_sections += (
                f"**{obj['category']} Objection:**\n"
                f"- Buyer says: \"{obj['objection']}\"\n"
                f"- Framework: {obj['framework']}\n"
                f"- Recommended: {obj['recommended_response'][:120]}...\n\n"
            )
        return (
            f"**Objection Practice Library** (embedded demo library — simulated)\n\n"
            f"| Objection | Category | Frequency | Success Rate |\n|---|---|---|---|\n"
            f"{obj_rows}\n"
            f"{detail_sections}"
            f"Source: [Sales Training Platform]\nAgents: SalesSimulationAgent"
        )

    # ── performance_score ──────────────────────────────────────
    def _performance_score(self, scn, is_live):
        score = _compute_simulation_score(_SAMPLE_PERFORMANCE)
        criteria_rows = ""
        for skill, c in _SCORING_CRITERIA.items():
            pts = _SAMPLE_PERFORMANCE.get(skill, 0)
            pct = pts / c["max_points"] * 100
            criteria_rows += f"| {skill.replace('_', ' ').title()} | {pts}/{c['max_points']} | {pct:.0f}% | {c['criteria']} |\n"
        return (
            f"**Performance Score Detail** (simulated sample run)\n\n"
            f"**Overall: {score}/100**\n\n"
            f"| Skill | Score | Percentage | Criteria |\n|---|---|---|---|\n"
            f"{criteria_rows}\n"
            f"**Improvement Plan:**\n"
            f"- Focus on value proposition delivery (scored 70%)\n"
            f"- Practice objection handling frameworks daily\n"
            f"- Review top performer call recordings for closing techniques\n\n"
            f"**Next Simulation:** Recommended to retry at higher difficulty\n\n"
            f"Source: [Simulation Engine + Scoring Algorithm]\nAgents: SalesSimulationAgent"
        )


if __name__ == "__main__":
    agent = SalesSimulationAgent()
    print("=" * 60)
    print("EMBEDDED DEMO SCENARIO (works offline)")
    print(agent.perform(operation="scenario_setup", scenario_id="SCN-001"))
    print()
    print("=" * 60)
    print("LIVE TENANT SCENARIO (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="scenario_setup", scenario_id="Copper Kite Design"))
    print()
    print("=" * 60)
    print(agent.perform(operation="run_simulation", scenario_id="SCN-001"))
