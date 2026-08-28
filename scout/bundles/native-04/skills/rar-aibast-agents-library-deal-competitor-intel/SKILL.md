---
name: "rar-aibast-agents-library-deal-competitor-intel"
description: "Maps competitive exposure across live deals from a simulated Dynamics 365 tenant, with threat scores and an embedded offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/deal_competitor_intel", "rar_sha256": "fe7b22defb0093ff68c066828af6b63ee4c35dcb0f028193b11218583953dfa7", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["b2b", "sales", "competitive-intelligence", "deal-progression", "strategy"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/deal_competitor_intel`. The original RAPP
agent is preserved byte-for-byte in `competitor_intelligence_agent.py` and in the RCI capsule.

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

Deal Competitor Intelligence Agent — a template you are meant to mutate.

Produces competitor snapshots, per-deal threat assessments,
counter-positioning strategies, and win/loss patterns so sales teams can
address competitive pressure with data-driven counter-strategies.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="competitor_snapshot") — the deal-exposure
     table lists live open deals such as "Copper Kite Design — Secure
     print rollout".
  2. No network? Everything falls back to the embedded demo layer below
     (_DEAL_COMPETITORS / _COMPETITORS) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     DEAL_COMPETITOR_INTEL_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON you export from Salesforce/HubSpot), or
     replace _fetch_collection() with your own client. The dict shape the
     rest of the file needs is documented in _normalize_live_deal().
     Which competitors sit in each evaluation is an enrichment seam —
     wire Crayon/Klue or your CRM competitor field there. The competitor
     landscape and win/loss ops stay simulated until you do.

OPERATIONS
  competitor_snapshot | threat_assessment | counter_strategy
  | win_loss_patterns
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
        "competitor_snapshot",
        "threat_assessment",
        "counter_strategy",
        "win_loss_patterns"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `competitor_intelligence_agent.py` and embedded as the fenced Python below (sha256 fe7b22defb0093ff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `competitor_intelligence_agent.py` first:

```bash
python3 competitor_intelligence_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 competitor_intelligence_agent.py   # or on stdin
python3 competitor_intelligence_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Deal Competitor Intelligence Agent — a template you are meant to mutate.

Produces competitor snapshots, per-deal threat assessments,
counter-positioning strategies, and win/loss patterns so sales teams can
address competitive pressure with data-driven counter-strategies.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="competitor_snapshot") — the deal-exposure
     table lists live open deals such as "Copper Kite Design — Secure
     print rollout".
  2. No network? Everything falls back to the embedded demo layer below
     (_DEAL_COMPETITORS / _COMPETITORS) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     DEAL_COMPETITOR_INTEL_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON you export from Salesforce/HubSpot), or
     replace _fetch_collection() with your own client. The dict shape the
     rest of the file needs is documented in _normalize_live_deal().
     Which competitors sit in each evaluation is an enrichment seam —
     wire Crayon/Klue or your CRM competitor field there. The competitor
     landscape and win/loss ops stay simulated until you do.

OPERATIONS
  competitor_snapshot | threat_assessment | counter_strategy
  | win_loss_patterns
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
    "name": "@aibast-agents-library/deal_competitor_intel",
    "version": "1.1.0",
    "display_name": "Deal Competitor Intelligence",
    "description": "Maps competitive exposure across live deals from a simulated Dynamics 365 tenant, with threat scores and an embedded offline demo fallback.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "competitive-intelligence", "deal-progression", "strategy"],
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
#   export DEAL_COMPETITOR_INTEL_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_deal().
# ===================================================================

DATA_SOURCE_URL = os.environ.get(
    "DEAL_COMPETITOR_INTEL_DATA_URL",
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
    renderers label it an enrichment seam (wire Crayon/Klue or your CRM
    competitor field)."""
    return {
        "deal_id": str(row.get("opportunityid", ""))[:8],
        "name": row.get("name", "Unknown"),
        "account": row.get("parentaccountidname", "Unknown"),
        "value": int(float(row.get("estimatedvalue") or 0)),
        "stage": _LIVE_STAGE_MAP.get(row.get("stepname"), "Qualification"),
        "competitors_in_eval": None,  # enrichment seam — wire Crayon/Klue
        "incumbent": None,            # enrichment seam
        "eval_status": row.get("description") or "n/a — enrichment seam",
        "_live": True,
    }


def _live_open_deals():
    """Live open opportunities normalized for this agent; [] when offline."""
    return [_normalize_live_deal(o) for o in _fetch_collection("opportunities")
            if o.get("statecode") == 0]


# ===================================================================
# EMBEDDED DEMO LAYER (offline fallback)
# ===================================================================

_COMPETITORS = {
    "Vendara Solutions": {
        "type": "Direct", "market_share": 22.4, "funding": "$180M Series D",
        "strengths": ["Lower price point", "Fast implementation", "Strong SMB presence"],
        "weaknesses": ["Limited enterprise features", "No AI/ML capability", "Weak integrations"],
        "pricing_model": "Per-user, $45/mo", "avg_deal_discount": 18,
        "recent_moves": "Launched AI add-on Q4 2025; acquired DataSync for integrations",
    },
    "Nextera Platform": {
        "type": "Direct", "market_share": 18.7, "funding": "$320M Series E",
        "strengths": ["Strong enterprise features", "Gartner leader quadrant", "Large partner ecosystem"],
        "weaknesses": ["High total cost", "Complex implementation", "18-month avg deployment"],
        "pricing_model": "Platform license, $120K/yr base", "avg_deal_discount": 12,
        "recent_moves": "Price increase 15% in Jan 2026; lost 3 Fortune 500 accounts",
    },
    "CloudFirst Systems": {
        "type": "Indirect", "market_share": 11.2, "funding": "$85M Series C",
        "strengths": ["Cloud-native architecture", "Developer-friendly API", "Modern UI"],
        "weaknesses": ["Young company (4 years)", "Limited customer success team", "No on-prem option"],
        "pricing_model": "Usage-based, ~$60K/yr avg", "avg_deal_discount": 22,
        "recent_moves": "Expanded to EMEA; hired ex-Salesforce CRO",
    },
    "Legacy Corp ERP": {
        "type": "Incumbent", "market_share": 31.5, "funding": "Public (NYSE: LCE)",
        "strengths": ["Installed base loyalty", "Full ERP suite", "Global support"],
        "weaknesses": ["Outdated UX", "Slow innovation", "Lock-in contracts"],
        "pricing_model": "Enterprise agreement, $200K+/yr", "avg_deal_discount": 8,
        "recent_moves": "Announced cloud migration path; partnership with Accenture",
    },
}

_DEAL_COMPETITORS = {
    "TechCorp Industries": {
        "deal_id": "OPP-001", "value": 890000, "stage": "Proposal",
        "competitors_in_eval": ["Nextera Platform", "CloudFirst Systems"],
        "incumbent": "Legacy Corp ERP",
        "prospect_priorities": ["AI capabilities", "Integration speed", "Total cost of ownership"],
        "eval_status": "Shortlisted to 2 vendors, final decision in 3 weeks",
    },
    "Global Manufacturing": {
        "deal_id": "OPP-002", "value": 720000, "stage": "Negotiation",
        "competitors_in_eval": ["Vendara Solutions"],
        "incumbent": None,
        "prospect_priorities": ["Price", "Manufacturing-specific features", "Implementation speed"],
        "eval_status": "Verbal preference for us, Vendara offering 25% discount",
    },
    "Apex Financial": {
        "deal_id": "OPP-003", "value": 580000, "stage": "Discovery",
        "competitors_in_eval": ["Nextera Platform", "Vendara Solutions", "CloudFirst Systems"],
        "incumbent": "Legacy Corp ERP",
        "prospect_priorities": ["Security compliance", "Financial services expertise", "Scalability"],
        "eval_status": "Early evaluation, RFP expected in 2 weeks",
    },
    "Metro Healthcare": {
        "deal_id": "OPP-004", "value": 440000, "stage": "Proposal",
        "competitors_in_eval": ["Nextera Platform"],
        "incumbent": None,
        "prospect_priorities": ["HIPAA compliance", "Interoperability", "Patient data security"],
        "eval_status": "Strong position, Nextera struggling with compliance requirements",
    },
    "Pacific Telecom": {
        "deal_id": "OPP-013", "value": 780000, "stage": "Negotiation",
        "competitors_in_eval": ["CloudFirst Systems"],
        "incumbent": "Legacy Corp ERP",
        "prospect_priorities": ["API-first architecture", "Real-time analytics", "Scalability"],
        "eval_status": "Procurement stage, CloudFirst eliminated in technical eval",
    },
}

_WIN_LOSS_DATA = {
    "Vendara Solutions": {"wins_against": 14, "losses_to": 8, "win_rate": 63.6, "avg_cycle_delta": -5,
                          "common_win_factor": "Enterprise feature depth and AI", "common_loss_factor": "Price sensitivity in SMB deals"},
    "Nextera Platform": {"wins_against": 9, "losses_to": 11, "win_rate": 45.0, "avg_cycle_delta": 8,
                         "common_win_factor": "Implementation speed and modern UX", "common_loss_factor": "Brand recognition and analyst positioning"},
    "CloudFirst Systems": {"wins_against": 12, "losses_to": 5, "win_rate": 70.6, "avg_cycle_delta": -3,
                           "common_win_factor": "Enterprise maturity and support", "common_loss_factor": "Developer mindshare in cloud-native shops"},
    "Legacy Corp ERP": {"wins_against": 18, "losses_to": 6, "win_rate": 75.0, "avg_cycle_delta": 12,
                        "common_win_factor": "Modern platform vs legacy stack", "common_loss_factor": "Switching cost fear and executive relationships"},
}


# ===================================================================
# HELPERS
# ===================================================================

def _threat_score(competitor_name, deal_priorities):
    """Calculate threat score 0-100 for a competitor in context of deal priorities."""
    comp = _COMPETITORS.get(competitor_name, {})
    base = 50
    strength_match = sum(1 for s in comp.get("strengths", [])
                         for p in deal_priorities if any(w in s.lower() for w in p.lower().split()))
    weakness_match = sum(1 for w in comp.get("weaknesses", [])
                         for p in deal_priorities if any(word in w.lower() for word in p.lower().split()))
    wl = _WIN_LOSS_DATA.get(competitor_name, {})
    win_rate_against = wl.get("win_rate", 50)
    score = base + (strength_match * 10) - (weakness_match * 8) + (50 - win_rate_against) * 0.3
    return max(10, min(95, round(score)))


def _counter_strategy(competitor_name, deal_priorities):
    """Generate counter-positioning strategy."""
    comp = _COMPETITORS.get(competitor_name, {})
    weaknesses = comp.get("weaknesses", [])
    strategies = []
    for w in weaknesses:
        strategies.append(f"Highlight our advantage: {w} is a known gap for {competitor_name}")
    for p in deal_priorities:
        strategies.append(f"Demonstrate proof point for '{p}' with customer reference")
    return strategies[:5]


# ===================================================================
# AGENT CLASS
# ===================================================================

class CompetitorIntelligenceAgent(BasicAgent):
    """
    Provides competitive intelligence for active deals.

    Operations:
        competitor_snapshot  - overview of all competitors and market positioning
        threat_assessment    - per-deal threat scoring and competitive analysis
        counter_strategy     - counter-positioning recommendations per deal
        win_loss_patterns    - historical win/loss analysis by competitor
    """

    def __init__(self):
        self.name = "CompetitorIntelligenceAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["competitor_snapshot", "threat_assessment", "counter_strategy", "win_loss_patterns"],
                        "description": "The analysis to perform",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "competitor_snapshot")
        dispatch = {
            "competitor_snapshot": self._competitor_snapshot,
            "threat_assessment": self._threat_assessment,
            "counter_strategy": self._counter_strategy,
            "win_loss_patterns": self._win_loss_patterns,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"**Error:** Unknown operation '{op}'. Valid: {', '.join(dispatch.keys())}"
        return handler()

    # -- competitor_snapshot (flagship: deal exposure prefers LIVE) -----
    def _competitor_snapshot(self) -> str:
        rows = ""
        for name, comp in _COMPETITORS.items():
            strengths_str = comp["strengths"][0]
            weakness_str = comp["weaknesses"][0]
            rows += (f"| {name} | {comp['type']} | {comp['market_share']}% | "
                     f"{comp['pricing_model']} | {strengths_str} | {weakness_str} |\n")

        live = _live_open_deals()
        if live:
            deal_exposure = ""
            for deal in sorted(live, key=lambda d: -d["value"]):
                comps = "n/a — enrichment seam"
                inc = "n/a — enrichment seam"
                deal_exposure += f"| {deal['name']} | ${deal['value']:,} | {comps} | {inc} |\n"
            total_pipeline = sum(d["value"] for d in live)
            exposure_title = (
                f"**Deal-Level Competitive Exposure — {len(live)} LIVE open deals, "
                f"${total_pipeline:,} pipeline (Static Dynamics 365 tenant):**\n"
                f"Competitor attribution stays n/a until you wire Crayon/Klue "
                f"or your CRM competitor field at the LIVE DATA SEAM.\n"
            )
            source_line = "Source: [Competitive Intel DB (simulated) + Live Dynamics 365 opportunities]\n"
        else:
            deal_exposure = ""
            for deal_name, deal in sorted(_DEAL_COMPETITORS.items(), key=lambda x: -x[1]["value"]):
                comps = ", ".join(deal["competitors_in_eval"])
                inc = deal["incumbent"] or "None"
                deal_exposure += f"| {deal_name} | ${deal['value']:,} | {comps} | {inc} |\n"
            total_pipeline = sum(d["value"] for d in _DEAL_COMPETITORS.values())
            exposure_title = f"**Deal-Level Competitive Exposure (${total_pipeline:,} demo pipeline):**\n"
            source_line = "Source: [Competitive Intel DB + CRM Notes (simulated)]\n"

        return (
            f"**Competitive Landscape Snapshot** (landscape data simulated)\n\n"
            f"**Active Competitors ({len(_COMPETITORS)}):**\n\n"
            f"| Competitor | Type | Market Share | Pricing | Top Strength | Top Weakness |\n"
            f"|-----------|------|-------------|---------|-------------|-------------|\n"
            f"{rows}\n"
            f"{exposure_title}\n"
            f"| Deal | Value | Competitors in Eval | Incumbent |\n"
            f"|------|-------|--------------------|-----------|\n"
            f"{deal_exposure}\n"
            f"{source_line}"
            f"Agents: MarketIntelAgent, CRMDataAgent"
        )

    # -- threat_assessment ---------------------------------------------
    def _threat_assessment(self) -> str:
        sections = []
        for deal_name, deal in sorted(_DEAL_COMPETITORS.items(), key=lambda x: -x[1]["value"]):
            threat_rows = ""
            max_threat = 0
            for comp_name in deal["competitors_in_eval"]:
                score = _threat_score(comp_name, deal["prospect_priorities"])
                max_threat = max(max_threat, score)
                level = "CRITICAL" if score >= 70 else ("HIGH" if score >= 50 else "MODERATE")
                comp = _COMPETITORS.get(comp_name, {})
                recent = comp.get("recent_moves", "No recent activity")
                threat_rows += f"| {comp_name} | {score}/100 | {level} | {recent} |\n"

            if deal["incumbent"]:
                inc_score = _threat_score(deal["incumbent"], deal["prospect_priorities"])
                max_threat = max(max_threat, inc_score)
                level = "CRITICAL" if inc_score >= 70 else ("HIGH" if inc_score >= 50 else "MODERATE")
                threat_rows += f"| {deal['incumbent']} (Incumbent) | {inc_score}/100 | {level} | Switching cost advantage |\n"

            overall = "CRITICAL" if max_threat >= 70 else ("HIGH" if max_threat >= 50 else "MODERATE")
            sections.append(
                f"**{deal_name} -- ${deal['value']:,} ({deal['stage']})**\n"
                f"Overall Threat Level: **{overall}** | Status: {deal['eval_status']}\n\n"
                f"| Competitor | Threat Score | Level | Recent Activity |\n"
                f"|-----------|-------------|-------|----------------|\n"
                f"{threat_rows}"
            )

        return (
            f"**Threat Assessment -- {len(_DEAL_COMPETITORS)} Active Deals**\n\n"
            + "\n---\n\n".join(sections)
            + f"\n\nSource: [Competitive Intel + Deal Notes + Market Data]\n"
            f"Agents: ThreatScoringAgent, CompetitorTrackingAgent"
        )

    # -- counter_strategy ----------------------------------------------
    def _counter_strategy(self) -> str:
        sections = []
        for deal_name, deal in sorted(_DEAL_COMPETITORS.items(), key=lambda x: -x[1]["value"]):
            all_comps = deal["competitors_in_eval"][:]
            if deal["incumbent"]:
                all_comps.append(deal["incumbent"])

            comp_strategies = []
            for comp_name in all_comps:
                strategies = _counter_strategy(comp_name, deal["prospect_priorities"])
                strategy_lines = "\n".join(f"  - {s}" for s in strategies)
                comp_strategies.append(f"- **vs {comp_name}:**\n{strategy_lines}")

            priorities_str = ", ".join(deal["prospect_priorities"])
            sections.append(
                f"**{deal_name} -- ${deal['value']:,}**\n"
                f"Prospect priorities: {priorities_str}\n\n"
                + "\n".join(comp_strategies)
            )

        return (
            f"**Counter-Positioning Strategies**\n\n"
            f"Tailored strategies based on prospect priorities and competitor weaknesses.\n\n"
            + "\n\n---\n\n".join(sections)
            + f"\n\nSource: [Competitive Playbook + Win/Loss Library]\n"
            f"Agents: StrategyAdvisorAgent"
        )

    # -- win_loss_patterns ---------------------------------------------
    def _win_loss_patterns(self) -> str:
        rows = ""
        for comp_name, wl in sorted(_WIN_LOSS_DATA.items(), key=lambda x: -x[1]["win_rate"]):
            total = wl["wins_against"] + wl["losses_to"]
            delta_str = f"+{wl['avg_cycle_delta']}" if wl["avg_cycle_delta"] > 0 else str(wl["avg_cycle_delta"])
            rows += (f"| {comp_name} | {wl['wins_against']}-{wl['losses_to']} "
                     f"| {wl['win_rate']}% | {delta_str} days "
                     f"| {wl['common_win_factor']} | {wl['common_loss_factor']} |\n")

        total_wins = sum(wl["wins_against"] for wl in _WIN_LOSS_DATA.values())
        total_losses = sum(wl["losses_to"] for wl in _WIN_LOSS_DATA.values())
        overall_rate = round(total_wins / (total_wins + total_losses) * 100, 1)

        best = max(_WIN_LOSS_DATA.items(), key=lambda x: x[1]["win_rate"])
        worst = min(_WIN_LOSS_DATA.items(), key=lambda x: x[1]["win_rate"])

        return (
            f"**Win/Loss Pattern Analysis**\n\n"
            f"Overall competitive win rate: **{overall_rate}%** ({total_wins}W-{total_losses}L)\n\n"
            f"| Competitor | Record | Win Rate | Cycle Delta | Key Win Factor | Key Loss Factor |\n"
            f"|-----------|--------|---------|------------|---------------|----------------|\n"
            f"{rows}\n"
            f"**Key Insights:**\n"
            f"- Strongest position vs **{best[0]}** ({best[1]['win_rate']}% win rate): {best[1]['common_win_factor']}\n"
            f"- Most challenged by **{worst[0]}** ({worst[1]['win_rate']}% win rate): {worst[1]['common_loss_factor']}\n"
            f"- Deals against incumbents take avg 12 days longer but yield higher ACV\n"
            f"- Multi-competitor evaluations (3+) reduce win rate by 15%\n\n"
            f"**Recommendation:** Prioritize early competitive disqualification in Discovery stage. "
            f"Reference calls and POC differentiation are highest-impact tactics.\n\n"
            f"Source: [Win/Loss Database + CRM Outcomes]\n"
            f"Agents: WinLossAnalyticsAgent"
        )


if __name__ == "__main__":
    agent = CompetitorIntelligenceAgent()
    print("=" * 70)
    print("LIVE TENANT DEAL EXPOSURE (fetched over HTTP; embedded demo offline)")
    print(agent.perform(operation="competitor_snapshot"))
    print()
    print("=" * 70)
    print("EMBEDDED DEMO (works offline, simulated)")
    print(agent.perform(operation="threat_assessment"))
    print()
    print("=" * 70)
    print(agent.perform(operation="win_loss_patterns"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
