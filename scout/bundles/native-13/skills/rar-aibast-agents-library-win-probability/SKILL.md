---
name: "rar-aibast-agents-library-win-probability"
description: "Scores win probability for live deals from a simulated Dynamics 365 tenant, with factor analysis and an embedded offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/win_probability", "rar_sha256": "299d43eb11991491ca4a26ab8e3f3634225348db9b84f4320543274353c90252", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["b2b", "sales", "win-probability", "deal-progression", "forecasting"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/win_probability`. The original RAPP
agent is preserved byte-for-byte in `win_probability_agent.py` and in the RCI capsule.

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

Win Probability Agent — a template you are meant to mutate.

Calculates deal win probabilities with weighted factor analysis, trend
tracking, and deal-to-deal comparisons to improve close rates.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="calculate_probability") — the scorecard uses
     the real CRM close probability of live open deals such as "Orchard
     Signal Works — Managed print fleet refresh" (60%).
  2. No network? Everything falls back to the embedded demo layer below
     (_DEAL_ATTRIBUTES / _PROBABILITY_HISTORY) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     WIN_PROBABILITY_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with your own client. The dict shape the rest of
     the file needs is documented in _normalize_live_deal(). The 8-factor
     model inputs (champion strength, momentum, coverage...) are
     enrichment seams — wire Gong / your analytics there; factor ops stay
     simulated until you do.

OPERATIONS
  calculate_probability | factor_analysis | probability_trend
  | deal_comparison
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
        "calculate_probability",
        "factor_analysis",
        "probability_trend",
        "deal_comparison"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `win_probability_agent.py` and embedded as the fenced Python below (sha256 299d43eb11991491…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `win_probability_agent.py` first:

```bash
python3 win_probability_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 win_probability_agent.py   # or on stdin
python3 win_probability_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Win Probability Agent — a template you are meant to mutate.

Calculates deal win probabilities with weighted factor analysis, trend
tracking, and deal-to-deal comparisons to improve close rates.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="calculate_probability") — the scorecard uses
     the real CRM close probability of live open deals such as "Orchard
     Signal Works — Managed print fleet refresh" (60%).
  2. No network? Everything falls back to the embedded demo layer below
     (_DEAL_ATTRIBUTES / _PROBABILITY_HISTORY) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     WIN_PROBABILITY_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with your own client. The dict shape the rest of
     the file needs is documented in _normalize_live_deal(). The 8-factor
     model inputs (champion strength, momentum, coverage...) are
     enrichment seams — wire Gong / your analytics there; factor ops stay
     simulated until you do.

OPERATIONS
  calculate_probability | factor_analysis | probability_trend
  | deal_comparison
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
    "name": "@aibast-agents-library/win_probability",
    "version": "1.1.0",
    "display_name": "Win Probability",
    "description": "Scores win probability for live deals from a simulated Dynamics 365 tenant, with factor analysis and an embedded offline demo fallback.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "win-probability", "deal-progression", "forecasting"],
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
#   export WIN_PROBABILITY_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_deal().
# ===================================================================

DATA_SOURCE_URL = os.environ.get(
    "WIN_PROBABILITY_DATA_URL",
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
    renderers label it an enrichment seam (the 8-factor model needs
    signals from Gong / your engagement analytics)."""
    return {
        "deal_id": str(row.get("opportunityid", ""))[:8],
        "name": row.get("name", "Unknown"),
        "value": int(float(row.get("estimatedvalue") or 0)),
        "stage": _LIVE_STAGE_MAP.get(row.get("stepname"), "Qualification"),
        "owner": row.get("owneridname", ""),
        "crm_probability": int(row.get("closeprobability") or 0),
        "factors": None,  # enrichment seam — wire your signal systems
        "_live": True,
    }


def _live_open_deals():
    """Live open opportunities normalized for this agent; [] when offline."""
    return [_normalize_live_deal(o) for o in _fetch_collection("opportunities")
            if o.get("statecode") == 0]


# ===================================================================
# EMBEDDED DEMO LAYER (offline fallback)
# ===================================================================

_DEAL_ATTRIBUTES = {
    "TechCorp Industries": {
        "deal_id": "OPP-001", "value": 890000, "stage": "Proposal", "owner": "Mike Chen",
        "factors": {
            "stage_progression": {"value": 0.55, "weight": 0.20, "detail": "3 of 5 stages completed"},
            "champion_strength": {"value": 0.20, "weight": 0.18, "detail": "Champion silent 18 days"},
            "stakeholder_coverage": {"value": 0.40, "weight": 0.12, "detail": "2 of 5 stakeholders engaged"},
            "activity_momentum": {"value": 0.25, "weight": 0.12, "detail": "Activity declined 75% in last 14 days"},
            "competitive_position": {"value": 0.40, "weight": 0.10, "detail": "2 competitors in evaluation"},
            "deal_velocity": {"value": 0.30, "weight": 0.10, "detail": "2.1x benchmark in current stage"},
            "budget_confidence": {"value": 0.65, "weight": 0.08, "detail": "Budget approved in Q3 planning"},
            "executive_access": {"value": 0.15, "weight": 0.10, "detail": "No exec meeting in 45 days"},
        },
    },
    "Global Manufacturing": {
        "deal_id": "OPP-002", "value": 720000, "stage": "Negotiation", "owner": "Lisa Torres",
        "factors": {
            "stage_progression": {"value": 0.80, "weight": 0.20, "detail": "4 of 5 stages completed"},
            "champion_strength": {"value": 0.70, "weight": 0.18, "detail": "Champion active but frustrated"},
            "stakeholder_coverage": {"value": 0.60, "weight": 0.12, "detail": "3 of 4 stakeholders engaged"},
            "activity_momentum": {"value": 0.55, "weight": 0.12, "detail": "Consistent engagement, slight decline"},
            "competitive_position": {"value": 0.70, "weight": 0.10, "detail": "Leading, competitor offering discount"},
            "deal_velocity": {"value": 0.35, "weight": 0.10, "detail": "2.3x benchmark in Negotiation"},
            "budget_confidence": {"value": 0.75, "weight": 0.08, "detail": "Budget confirmed, procurement slow"},
            "executive_access": {"value": 0.45, "weight": 0.10, "detail": "Exec engaged but 20 days since contact"},
        },
    },
    "Apex Financial": {
        "deal_id": "OPP-003", "value": 580000, "stage": "Discovery", "owner": "James Park",
        "factors": {
            "stage_progression": {"value": 0.30, "weight": 0.20, "detail": "2 of 5 stages completed"},
            "champion_strength": {"value": 0.15, "weight": 0.18, "detail": "CTO disengaged, no response"},
            "stakeholder_coverage": {"value": 0.20, "weight": 0.12, "detail": "1 of 6 stakeholders engaged"},
            "activity_momentum": {"value": 0.15, "weight": 0.12, "detail": "Activity declined 80% in last 14 days"},
            "competitive_position": {"value": 0.25, "weight": 0.10, "detail": "3 competitors, RFP coming"},
            "deal_velocity": {"value": 0.45, "weight": 0.10, "detail": "1.4x benchmark in Discovery"},
            "budget_confidence": {"value": 0.30, "weight": 0.08, "detail": "Budget not yet allocated"},
            "executive_access": {"value": 0.10, "weight": 0.10, "detail": "No executive contact established"},
        },
    },
    "Metro Healthcare": {
        "deal_id": "OPP-004", "value": 440000, "stage": "Proposal", "owner": "Mike Chen",
        "factors": {
            "stage_progression": {"value": 0.55, "weight": 0.20, "detail": "3 of 5 stages completed"},
            "champion_strength": {"value": 0.85, "weight": 0.18, "detail": "VP Digital actively championing"},
            "stakeholder_coverage": {"value": 0.65, "weight": 0.12, "detail": "3 of 4 stakeholders engaged"},
            "activity_momentum": {"value": 0.60, "weight": 0.12, "detail": "Steady engagement maintained"},
            "competitive_position": {"value": 0.80, "weight": 0.10, "detail": "Competitor struggling with compliance"},
            "deal_velocity": {"value": 0.50, "weight": 0.10, "detail": "1.4x benchmark, moderate delay"},
            "budget_confidence": {"value": 0.40, "weight": 0.08, "detail": "Budget on hold, board approval needed"},
            "executive_access": {"value": 0.70, "weight": 0.10, "detail": "CMO engaged as executive sponsor"},
        },
    },
    "Pacific Telecom": {
        "deal_id": "OPP-013", "value": 780000, "stage": "Negotiation", "owner": "Lisa Torres",
        "factors": {
            "stage_progression": {"value": 0.80, "weight": 0.20, "detail": "4 of 5 stages completed"},
            "champion_strength": {"value": 0.95, "weight": 0.18, "detail": "SVP Ops strong advocate, weekly calls"},
            "stakeholder_coverage": {"value": 0.85, "weight": 0.12, "detail": "4 of 5 stakeholders engaged"},
            "activity_momentum": {"value": 0.90, "weight": 0.12, "detail": "High and increasing activity"},
            "competitive_position": {"value": 0.90, "weight": 0.10, "detail": "Competitor eliminated in eval"},
            "deal_velocity": {"value": 0.75, "weight": 0.10, "detail": "1.2x benchmark, near target"},
            "budget_confidence": {"value": 0.90, "weight": 0.08, "detail": "Budget approved, PO in queue"},
            "executive_access": {"value": 0.85, "weight": 0.10, "detail": "CTO and SVP both engaged"},
        },
    },
    "Pinnacle Logistics": {
        "deal_id": "OPP-005", "value": 360000, "stage": "Qualification", "owner": "James Park",
        "factors": {
            "stage_progression": {"value": 0.15, "weight": 0.20, "detail": "1 of 5 stages, early"},
            "champion_strength": {"value": 0.10, "weight": 0.18, "detail": "No champion identified"},
            "stakeholder_coverage": {"value": 0.15, "weight": 0.12, "detail": "1 contact, single-threaded"},
            "activity_momentum": {"value": 0.20, "weight": 0.12, "detail": "Minimal activity, declining"},
            "competitive_position": {"value": 0.50, "weight": 0.10, "detail": "No known competitors yet"},
            "deal_velocity": {"value": 0.40, "weight": 0.10, "detail": "1.4x benchmark in Qualification"},
            "budget_confidence": {"value": 0.20, "weight": 0.08, "detail": "No budget discussion held"},
            "executive_access": {"value": 0.05, "weight": 0.10, "detail": "No executive contact at all"},
        },
    },
}

_HISTORICAL_WIN_FACTORS = {
    "champion_strength": {"avg_won": 0.82, "avg_lost": 0.28, "discriminative_power": 0.92},
    "executive_access": {"avg_won": 0.76, "avg_lost": 0.22, "discriminative_power": 0.88},
    "stakeholder_coverage": {"avg_won": 0.74, "avg_lost": 0.31, "discriminative_power": 0.82},
    "activity_momentum": {"avg_won": 0.78, "avg_lost": 0.35, "discriminative_power": 0.78},
    "stage_progression": {"avg_won": 0.85, "avg_lost": 0.42, "discriminative_power": 0.75},
    "competitive_position": {"avg_won": 0.72, "avg_lost": 0.38, "discriminative_power": 0.70},
    "deal_velocity": {"avg_won": 0.70, "avg_lost": 0.40, "discriminative_power": 0.65},
    "budget_confidence": {"avg_won": 0.80, "avg_lost": 0.45, "discriminative_power": 0.62},
}

_SCORING_WEIGHTS = {
    "stage_progression": 0.20,
    "champion_strength": 0.18,
    "stakeholder_coverage": 0.12,
    "activity_momentum": 0.12,
    "competitive_position": 0.10,
    "deal_velocity": 0.10,
    "budget_confidence": 0.08,
    "executive_access": 0.10,
}

_PROBABILITY_HISTORY = {
    "TechCorp Industries": [0.52, 0.48, 0.42, 0.38, 0.35, 0.32],
    "Global Manufacturing": [0.40, 0.45, 0.50, 0.52, 0.55, 0.56],
    "Apex Financial": [0.35, 0.30, 0.25, 0.22, 0.20, 0.18],
    "Metro Healthcare": [0.38, 0.42, 0.45, 0.48, 0.50, 0.52],
    "Pacific Telecom": [0.50, 0.58, 0.65, 0.72, 0.78, 0.82],
    "Pinnacle Logistics": [0.20, 0.18, 0.15, 0.14, 0.12, 0.11],
}


# ===================================================================
# HELPERS
# ===================================================================

def _calculate_win_prob(deal_name):
    """Calculate weighted win probability."""
    deal = _DEAL_ATTRIBUTES.get(deal_name, {})
    factors = deal.get("factors", {})
    probability = 0
    for fname, fdata in factors.items():
        probability += fdata["value"] * fdata["weight"]
    return round(probability * 100, 1)


def _top_factors(deal_name, top_n=3):
    """Return top contributing factors (positive) for a deal."""
    deal = _DEAL_ATTRIBUTES.get(deal_name, {})
    factors = deal.get("factors", {})
    contributions = []
    for fname, fdata in factors.items():
        contribution = fdata["value"] * fdata["weight"]
        contributions.append({"name": fname, "value": fdata["value"], "weight": fdata["weight"],
                              "contribution": contribution, "detail": fdata["detail"]})
    return sorted(contributions, key=lambda x: -x["contribution"])[:top_n]


def _bottom_factors(deal_name, top_n=3):
    """Return weakest factors dragging down probability."""
    deal = _DEAL_ATTRIBUTES.get(deal_name, {})
    factors = deal.get("factors", {})
    weaknesses = []
    for fname, fdata in factors.items():
        gap = (1.0 - fdata["value"]) * fdata["weight"]
        weaknesses.append({"name": fname, "value": fdata["value"], "weight": fdata["weight"],
                           "gap": gap, "detail": fdata["detail"]})
    return sorted(weaknesses, key=lambda x: -x["gap"])[:top_n]


def _prob_trend(deal_name):
    """Analyze probability trend."""
    history = _PROBABILITY_HISTORY.get(deal_name, [])
    if len(history) < 2:
        return "stable", 0
    delta = history[-1] - history[-2]
    overall = history[-1] - history[0]
    if overall > 0.05:
        return "improving", round(overall * 100, 1)
    if overall < -0.05:
        return "declining", round(overall * 100, 1)
    return "stable", round(overall * 100, 1)


# ===================================================================
# AGENT CLASS
# ===================================================================

class WinProbabilityAgent(BasicAgent):
    """
    Calculates and analyzes win probabilities for pipeline deals.

    Operations:
        calculate_probability - compute win probability per deal
        factor_analysis       - weighted factor contributions
        probability_trend     - 6-period probability trend
        deal_comparison       - side-by-side deal comparison
    """

    def __init__(self):
        self.name = "WinProbabilityAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["calculate_probability", "factor_analysis", "probability_trend", "deal_comparison"],
                        "description": "The analysis to perform",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "calculate_probability")
        dispatch = {
            "calculate_probability": self._calculate_probability,
            "factor_analysis": self._factor_analysis,
            "probability_trend": self._probability_trend,
            "deal_comparison": self._deal_comparison,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"**Error:** Unknown operation '{op}'. Valid: {', '.join(dispatch.keys())}"
        return handler()

    # -- calculate_probability (flagship: prefers LIVE, falls back) -----
    def _calculate_probability(self) -> str:
        live = _live_open_deals()
        if live:
            rows = ""
            probs = []
            total_value = 0
            weighted_value = 0.0
            for d in sorted(live, key=lambda x: -x["value"]):
                prob = d["crm_probability"]
                probs.append(prob)
                total_value += d["value"]
                weighted_value += d["value"] * prob / 100
                rows += (f"| {d['name']} | ${d['value']:,} | {d['stage']} | "
                         f"**{prob}%** | n/a — enrichment seam | n/a |\n")
            avg_prob = round(sum(probs) / max(len(probs), 1), 1)
            return (
                f"**Win Probability Scorecard — {len(live)} LIVE Open Deals** "
                f"(Static Dynamics 365 tenant)\n\n"
                f"Portfolio avg: **{avg_prob}%** | Total pipeline: ${total_value:,} | "
                f"Weighted value: ${weighted_value:,.0f}\n\n"
                f"| Deal | Value | Stage | Win Prob (CRM) | Top Factor | Biggest Gap |\n"
                f"|------|-------|-------|---------------|-----------|------------|\n"
                f"{rows}\n"
                f"**Scoring:** probabilities come straight from the live CRM. The "
                f"8-factor model activates when you wire engagement signals at the "
                f"LIVE DATA SEAM.\n\n"
                f"Source: [Live Dynamics 365 opportunities]\n"
                f"Agents: ProbabilityScoringEngine"
            )
        rows = ""
        probs = []
        total_value = 0
        weighted_value = 0

        for deal_name in sorted(_DEAL_ATTRIBUTES.keys(), key=lambda d: -_DEAL_ATTRIBUTES[d]["value"]):
            deal = _DEAL_ATTRIBUTES[deal_name]
            prob = _calculate_win_prob(deal_name)
            probs.append(prob)
            total_value += deal["value"]
            weighted_value += deal["value"] * prob / 100
            direction, _ = _prob_trend(deal_name)
            trend_str = {"improving": "UP", "declining": "DOWN", "stable": "FLAT"}.get(direction, "FLAT")

            top = _top_factors(deal_name, 1)
            bottom = _bottom_factors(deal_name, 1)
            top_str = top[0]["name"].replace("_", " ").title() if top else "-"
            bottom_str = bottom[0]["name"].replace("_", " ").title() if bottom else "-"

            rows += (f"| {deal_name} | ${deal['value']:,} | {deal['stage']} | "
                     f"**{prob}%** | {trend_str} | {top_str} | {bottom_str} |\n")

        avg_prob = round(sum(probs) / max(len(probs), 1), 1)

        return (
            f"**Win Probability Scorecard**\n\n"
            f"Portfolio avg: **{avg_prob}%** | Total pipeline: ${total_value:,} | "
            f"Weighted value: ${weighted_value:,.0f}\n\n"
            f"| Deal | Value | Stage | Win Prob | Trend | Top Factor | Biggest Gap |\n"
            f"|------|-------|-------|---------|-------|-----------|------------|\n"
            f"{rows}\n"
            f"**Scoring Model:** 8 factors weighted by predictive power from historical win/loss data.\n\n"
            f"Source: [CRM + Activity Data + Win/Loss Database]\n"
            f"Agents: ProbabilityScoringEngine"
        )

    # -- factor_analysis -----------------------------------------------
    def _factor_analysis(self) -> str:
        sections = []
        for deal_name in sorted(_DEAL_ATTRIBUTES.keys(), key=lambda d: -_DEAL_ATTRIBUTES[d]["value"]):
            deal = _DEAL_ATTRIBUTES[deal_name]
            prob = _calculate_win_prob(deal_name)

            factor_rows = ""
            for fname, fdata in sorted(deal["factors"].items(), key=lambda x: -x[1]["value"] * x[1]["weight"]):
                contribution = round(fdata["value"] * fdata["weight"] * 100, 1)
                max_possible = round(fdata["weight"] * 100, 1)
                label = fname.replace("_", " ").title()
                factor_rows += (f"| {label} | {fdata['value']:.0%} | {fdata['weight']:.0%} | "
                                f"{contribution}% | {max_possible}% | {fdata['detail']} |\n")

            sections.append(
                f"**{deal_name} -- ${deal['value']:,} (Win Prob: {prob}%)**\n\n"
                f"| Factor | Score | Weight | Contribution | Max Possible | Detail |\n"
                f"|--------|-------|--------|-------------|-------------|--------|\n"
                f"{factor_rows}"
            )

        hist_rows = ""
        for fname in sorted(_HISTORICAL_WIN_FACTORS.keys(),
                            key=lambda f: -_HISTORICAL_WIN_FACTORS[f]["discriminative_power"]):
            hf = _HISTORICAL_WIN_FACTORS[fname]
            label = fname.replace("_", " ").title()
            hist_rows += (f"| {label} | {hf['avg_won']:.0%} | {hf['avg_lost']:.0%} | "
                          f"{hf['discriminative_power']:.0%} |\n")

        return (
            f"**Factor Analysis -- Win Probability Drivers**\n\n"
            + "\n---\n\n".join(sections)
            + f"\n\n**Historical Factor Importance:**\n\n"
            f"| Factor | Avg (Won) | Avg (Lost) | Discriminative Power |\n"
            f"|--------|----------|----------|--------------------|\n"
            f"{hist_rows}\n"
            f"Source: [Win/Loss Analysis + Factor Model]\n"
            f"Agents: FactorAnalysisEngine"
        )

    # -- probability_trend ---------------------------------------------
    def _probability_trend(self) -> str:
        sections = []
        for deal_name in sorted(_DEAL_ATTRIBUTES.keys(), key=lambda d: -_DEAL_ATTRIBUTES[d]["value"]):
            history = _PROBABILITY_HISTORY.get(deal_name, [])
            if not history:
                continue
            direction, delta = _prob_trend(deal_name)
            status = {"improving": "IMPROVING", "declining": "DECLINING", "stable": "STABLE"}.get(direction, "STABLE")

            period_labels = ["W-5", "W-4", "W-3", "W-2", "W-1", "Current"]
            trend_line = " | ".join(f"{period_labels[i]}: {h:.0%}" for i, h in enumerate(history))
            peak = max(history)
            trough = min(history)

            sections.append(
                f"**{deal_name} -- ${_DEAL_ATTRIBUTES[deal_name]['value']:,}**\n"
                f"Status: {status} | Current: {history[-1]:.0%} | 6-week delta: {delta:+.1f}%\n"
                f"Trend: {trend_line}\n"
                f"Range: {trough:.0%} - {peak:.0%}\n"
            )

        improving = sum(1 for d in _PROBABILITY_HISTORY if _prob_trend(d)[0] == "improving")
        declining = sum(1 for d in _PROBABILITY_HISTORY if _prob_trend(d)[0] == "declining")

        return (
            f"**Win Probability Trends -- 6-Week Analysis**\n\n"
            f"Improving: {improving} | Declining: {declining} | "
            f"Stable: {len(_PROBABILITY_HISTORY) - improving - declining}\n\n"
            + "\n---\n\n".join(sections)
            + f"\n\n**Insight:** Deals with 3+ consecutive weeks of decline require immediate "
            f"intervention to reverse trajectory.\n\n"
            f"Source: [Historical Probability Scores]\n"
            f"Agents: TrendAnalysisEngine"
        )

    # -- deal_comparison -----------------------------------------------
    def _deal_comparison(self) -> str:
        deals_sorted = sorted(_DEAL_ATTRIBUTES.keys(), key=lambda d: -_calculate_win_prob(d))

        factor_names = list(_SCORING_WEIGHTS.keys())
        header = "| Factor | " + " | ".join(d.split()[0] for d in deals_sorted) + " |\n"
        separator = "|--------|" + "|".join("------" for _ in deals_sorted) + "|\n"

        rows = ""
        for fname in factor_names:
            label = fname.replace("_", " ").title()
            values = []
            for deal_name in deals_sorted:
                val = _DEAL_ATTRIBUTES[deal_name]["factors"].get(fname, {}).get("value", 0)
                values.append(f"{val:.0%}")
            rows += f"| {label} | " + " | ".join(values) + " |\n"

        prob_values = [f"**{_calculate_win_prob(d)}%**" for d in deals_sorted]
        rows += f"| **Win Probability** | " + " | ".join(prob_values) + " |\n"

        best = deals_sorted[0]
        worst = deals_sorted[-1]
        best_prob = _calculate_win_prob(best)
        worst_prob = _calculate_win_prob(worst)

        return (
            f"**Deal Comparison Matrix**\n\n"
            f"Best: **{best}** ({best_prob}%) | Needs attention: **{worst}** ({worst_prob}%)\n\n"
            f"{header}{separator}{rows}\n"
            f"**Comparison Insights:**\n"
            f"- {best} leads on champion strength and stakeholder coverage\n"
            f"- {worst} critically low on champion, executive access, and momentum\n"
            f"- Deals above 50% win probability share strong champion + executive access\n"
            f"- Activity momentum is the leading indicator of probability direction\n\n"
            f"**Pattern:** Deals that win have avg champion score of 82% vs 28% for losses. "
            f"Champion strength is the single strongest predictor.\n\n"
            f"Source: [Comparative Analytics + Win/Loss Patterns]\n"
            f"Agents: ComparisonEngine"
        )


if __name__ == "__main__":
    agent = WinProbabilityAgent()
    print("=" * 70)
    print("LIVE TENANT SCORECARD (fetched over HTTP; embedded demo offline)")
    print(agent.perform(operation="calculate_probability"))
    print()
    print("=" * 70)
    print("EMBEDDED DEMO (works offline, simulated)")
    print(agent.perform(operation="factor_analysis"))
    print()
    print("=" * 70)
    print(agent.perform(operation="deal_comparison"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
