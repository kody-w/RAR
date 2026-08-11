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
