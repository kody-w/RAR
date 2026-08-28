---
name: "rar-aibast-agents-library-sales-simulation"
description: "Builds sales role-play scenarios from live opportunities in a simulated Dynamics 365 tenant, with personas, scoring, and offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/sales_simulation", "rar_sha256": "73e63fad33cd0c6c6f10ed623e4b00cc753f68266548c5ca6d2744bd98401f04", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["sales", "simulation", "training", "objections", "personas", "scoring"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/sales_simulation`. The original RAPP
agent is preserved byte-for-byte in `sales_simulation_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The simulation operation to perform",
      "enum": [
        "scenario_setup",
        "run_simulation",
        "objection_practice",
        "performance_score"
      ],
      "type": "string"
    },
    "scenario_id": {
      "description": "Scenario ID (e.g. 'SCN-001')",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sales_simulation_agent.py` and embedded as the fenced Python below (sha256 73e63fad33cd0c6c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sales_simulation_agent.py` first:

```bash
python3 sales_simulation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sales_simulation_agent.py   # or on stdin
python3 sales_simulation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
