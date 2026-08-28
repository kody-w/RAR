---
name: "rar-aibast-agents-library-wealth-insights-generator"
description: "Generates opportunity alerts and client insights from a live simulated Dynamics 365 tenant pipeline, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/wealth_insights_generator", "rar_sha256": "4f77a77ea429868c58bf1d065ec5ba49819b932f594f212a2689bbc512363c48", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["wealth", "insights", "market", "performance", "analytics", "financial-services"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/wealth_insights_generator`. The original RAPP
agent is preserved byte-for-byte in `wealth_insights_generator_agent.py` and in the RCI capsule.

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

Wealth Insights Generator Agent — a template you are meant to mutate.

Generates market briefs, client insights, opportunity alerts, and
performance attribution reports for wealth management teams. In this
template a client opportunity alert is represented as an open Dynamics
365 opportunity — the tenant has no native planning-signal entity, so the
open pipeline stands in for the advisor's opportunity radar.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `opportunity_alerts` operation pulls
     live opportunity records over real HTTP from the globally hosted
     Static Dynamics 365 tenant (Aster Lane Office Systems — synthetic
     data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="opportunity_alerts")
     and look for "Orchard Signal Works — Managed print fleet refresh"
     among the high-priority alerts.
  2. No network? Everything falls back to the embedded demo layer below
     (CLIENT_PORTFOLIOS / OPPORTUNITY_SIGNALS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     WEALTH_INSIGHTS_GENERATOR_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your planning
     platform), or replace _fetch_collection() with your own client. The
     fields the rest of the file needs are listed in
     _normalize_live_alert() — life events and planning context are
     enrichment seams until you wire your CRM notes and planning tools.

OPERATIONS
  market_brief | client_insights | opportunity_alerts
  | performance_attribution | portfolio-intelligence capabilities
  kwargs: operation (required), user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "client_id": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "market_brief",
        "client_insights",
        "opportunity_alerts",
        "performance_attribution",
        "portfolio_opportunity_scan",
        "held_away_wealth_profile",
        "planning_gap_analysis",
        "engagement_strategy",
        "outreach_materials",
        "workflow_summary"
      ],
      "type": "string"
    },
    "user_input": {
      "description": "Optional natural-language request; an exact record key (e.g. WIG-1001) selects a single record.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `wealth_insights_generator_agent.py` and embedded as the fenced Python below (sha256 4f77a77ea429868c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `wealth_insights_generator_agent.py` first:

```bash
python3 wealth_insights_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 wealth_insights_generator_agent.py   # or on stdin
python3 wealth_insights_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Wealth Insights Generator Agent — a template you are meant to mutate.

Generates market briefs, client insights, opportunity alerts, and
performance attribution reports for wealth management teams. In this
template a client opportunity alert is represented as an open Dynamics
365 opportunity — the tenant has no native planning-signal entity, so the
open pipeline stands in for the advisor's opportunity radar.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `opportunity_alerts` operation pulls
     live opportunity records over real HTTP from the globally hosted
     Static Dynamics 365 tenant (Aster Lane Office Systems — synthetic
     data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="opportunity_alerts")
     and look for "Orchard Signal Works — Managed print fleet refresh"
     among the high-priority alerts.
  2. No network? Everything falls back to the embedded demo layer below
     (CLIENT_PORTFOLIOS / OPPORTUNITY_SIGNALS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     WEALTH_INSIGHTS_GENERATOR_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your planning
     platform), or replace _fetch_collection() with your own client. The
     fields the rest of the file needs are listed in
     _normalize_live_alert() — life events and planning context are
     enrichment seams until you wire your CRM notes and planning tools.

OPERATIONS
  market_brief | client_insights | opportunity_alerts
  | performance_attribution | portfolio-intelligence capabilities
  kwargs: operation (required), user_input
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json as _json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/wealth_insights_generator",
    "version": "1.2.0",
    "display_name": "Wealth Insights Generator Agent",
    "description": "Generates opportunity alerts and client insights from a live simulated Dynamics 365 tenant pipeline, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["wealth", "insights", "market", "performance", "analytics", "financial-services"],
    "category": "financial_services",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ---------------------------------------------------------------------------
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export WEALTH_INSIGHTS_GENERATOR_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM/planning client. Downstream
# code only needs the fields produced by _normalize_live_alert().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "WEALTH_INSIGHTS_GENERATOR_DATA_URL",
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
            rows = _json.loads(resp.read().decode("utf-8")).get("value", [])
    except Exception:
        rows = []
    _LIVE_CACHE[collection] = rows
    return rows


def _normalize_live_alert(row):
    """Project an open Dynamics opportunity onto the alert shape this
    agent uses. THIS is the contract your replacement data source must
    meet — a dict with these keys. None means 'not knowable from the CRM
    alone' and the renderers label it as an enrichment seam."""
    probability = int(row.get("closeprobability") or 0)
    value = float(row.get("estimatedvalue") or 0)
    close_date = str(row.get("estimatedclosedate", ""))[:10]
    return {
        "client": row.get("parentaccountidname") or row.get("customeridname", "Unknown"),
        "type": "open_pipeline",
        "description": f"{row.get('name', 'untitled')} — est ${value:,.0f}",
        "priority": "high" if probability >= 50 else "medium",
        "action": f"Advance toward close (probability {probability}%, target {close_date or 'n/a'})",
        "owner": row.get("owneridname", ""),
        "life_events": None,  # enrichment seam — wire your CRM notes / planning tools
        "_live": True,
    }


def _live_alerts():
    """List of live tenant opportunity alerts (open pipeline); [] offline."""
    rows = _fetch_collection("opportunities")
    return [_normalize_live_alert(row) for row in rows if row.get("statecode") == 0]


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

MARKET_DATA = {
    "S&P 500": {"current": 5285.42, "ytd_return": 4.8, "pe_ratio": 22.1, "dividend_yield": 1.35},
    "NASDAQ Composite": {"current": 16742.15, "ytd_return": 6.2, "pe_ratio": 28.5, "dividend_yield": 0.72},
    "Dow Jones Industrial": {"current": 39180.50, "ytd_return": 3.1, "pe_ratio": 19.8, "dividend_yield": 1.82},
    "MSCI EAFE": {"current": 2385.70, "ytd_return": 5.5, "pe_ratio": 15.2, "dividend_yield": 2.95},
    "Bloomberg US Agg Bond": {"current": 98.45, "ytd_return": 1.2, "pe_ratio": 0, "dividend_yield": 4.45},
    "10-Year Treasury": {"current": 4.28, "ytd_return": 0, "pe_ratio": 0, "dividend_yield": 4.28},
    "Gold (per oz)": {"current": 2185.30, "ytd_return": 8.1, "pe_ratio": 0, "dividend_yield": 0},
}

CLIENT_PORTFOLIOS = {
    "WM-001": {
        "name": "Harrison Family Trust",
        "aum": 8500000,
        "strategy": "balanced_growth",
        "ytd_return": 5.2,
        "benchmark_return": 4.1,
        "alpha": 1.1,
        "risk_profile": "moderate",
        "last_contact": "2025-02-20",
        "next_review": "2025-04-15",
        "life_events": ["Daughter starting college Fall 2025"],
    },
    "WM-002": {
        "name": "Dr. Anita Rao",
        "aum": 3200000,
        "strategy": "aggressive_growth",
        "ytd_return": 7.8,
        "benchmark_return": 6.2,
        "alpha": 1.6,
        "risk_profile": "aggressive",
        "last_contact": "2025-03-01",
        "next_review": "2025-06-01",
        "life_events": ["Planning practice sale in 2-3 years"],
    },
    "WM-003": {
        "name": "George & Martha Kensington",
        "aum": 12400000,
        "strategy": "capital_preservation",
        "ytd_return": 2.1,
        "benchmark_return": 1.8,
        "alpha": 0.3,
        "risk_profile": "conservative",
        "last_contact": "2025-01-15",
        "next_review": "2025-04-01",
        "life_events": ["Estate plan revision needed", "RMD optimization"],
    },
    "WM-004": {
        "name": "Tidewater Ventures LLC",
        "aum": 5700000,
        "strategy": "alternative_focused",
        "ytd_return": 3.9,
        "benchmark_return": 4.1,
        "alpha": -0.2,
        "risk_profile": "moderate_aggressive",
        "last_contact": "2025-02-10",
        "next_review": "2025-05-15",
        "life_events": ["Considering real estate exit strategy"],
    },
}

PERFORMANCE_BENCHMARKS = {
    "balanced_growth": {"benchmark": "60/40 Balanced", "1yr": 12.5, "3yr": 8.2, "5yr": 9.1},
    "aggressive_growth": {"benchmark": "80/20 Growth", "1yr": 18.2, "3yr": 10.5, "5yr": 11.8},
    "capital_preservation": {"benchmark": "20/80 Conservative", "1yr": 5.8, "3yr": 3.9, "5yr": 4.5},
    "alternative_focused": {"benchmark": "HFRI Fund Weighted", "1yr": 8.4, "3yr": 6.1, "5yr": 7.2},
}

OPPORTUNITY_SIGNALS = [
    {"client": "WM-001", "type": "education_funding", "description": "529 plan contribution deadline approaching; daughter's college enrollment Fall 2025", "priority": "high", "action": "Schedule meeting to review education funding plan"},
    {"client": "WM-002", "type": "liquidity_event", "description": "Practice sale in 2-3 years; begin pre-sale tax and asset protection planning", "priority": "high", "action": "Engage tax advisor for sale structuring"},
    {"client": "WM-003", "type": "estate_planning", "description": "Estate plan last updated 2019; tax law changes require revision", "priority": "medium", "action": "Coordinate with estate attorney for plan update"},
    {"client": "WM-003", "type": "rmd_optimization", "description": "Client age 74; review Qualified Charitable Distribution strategy", "priority": "medium", "action": "Model QCD scenarios vs standard RMD"},
    {"client": "WM-004", "type": "reallocation", "description": "Portfolio underperforming benchmark; alternative allocation review needed", "priority": "medium", "action": "Prepare alternative manager review presentation"},
]


# ---------------------------------------------------------------------------
# Portfolio Intelligence capabilities (spec: portfolio-intelligence)
#
# Six data-driven capabilities reproducing the one-pager scenario and the
# timestamped demo: scan opportunities, profile held-away wealth, detect
# planning gaps, plan engagement, generate Outlook-ready outreach, and compile
# a workflow summary. Each capability carries response/knowledge/records/key/
# write/generative metadata, supports optional user_input with exact-key
# matching, and returns a useful summary. Write-capable capabilities emit a
# simulated receipt and perform no mutation.
# ---------------------------------------------------------------------------

PORTFOLIO_INTELLIGENCE = {
    "portfolio_opportunity_scan": {
        "name": "Portfolio Opportunity Scan",
        "response": "Here is a strategic, targeted view of your key client opportunities, ranked by wallet-share potential and relationship readiness.",
        "source_system": "Dynamics 365",
        "customer": "the wealth advisory firm",
        "write": False,
        "generative": False,
        "exact_key_required": True,
        "key_field": "client_id",
        "knowledge": [
            "Manual research across systems limited visibility into true total wealth, so the scan aggregates opportunities into one view.",
            "The agent analyzes the total client base and highlights wallet share potential, planning needs, and life event triggers.",
            "Opportunities are prioritized based on potential impact and relationship readiness.",
            "Without any manual digging, the advisor gets a strategic, targeted view of key client opportunities.",
        ],
        "records": [
            {"client_id": "WIG-1001", "client": "Northwind Traders", "wallet_share_potential": "$4.2M held-away", "planning_need": "Diversification", "life_event_trigger": "Business sale pending", "priority": "High"},
            {"client_id": "WIG-1002", "client": "Fabrikam Holdings", "wallet_share_potential": "$1.8M held-away", "planning_need": "Retirement income", "life_event_trigger": "Approaching retirement", "priority": "Medium"},
            {"client_id": "WIG-1003", "client": "Contoso Family Office", "wallet_share_potential": "$6.5M held-away", "planning_need": "Estate transfer", "life_event_trigger": "Grandchild born", "priority": "High"},
        ],
    },
    "held_away_wealth_profile": {
        "name": "Held-Away Wealth Profile",
        "response": "Here is a unified wealth picture for the client, including total wealth, held-away assets, risk factors, and conversion triggers.",
        "source_system": "Dynamics 365",
        "customer": "the wealth advisory firm",
        "write": False,
        "generative": False,
        "exact_key_required": True,
        "key_field": "profile_id",
        "knowledge": [
            "Aggregate held-away assets into a unified wealth picture and form a comprehensive client profile.",
            "The agent delivers a deeper look at the client's total wealth, held away assets, risk factors, and conversion triggers.",
            "This context gives the advisor what is needed to assess the client opportunity effectively.",
        ],
        "records": [
            {"profile_id": "HAW-2001", "client": "Northwind Traders", "total_wealth": "$12.4M", "held_away_assets": "$4.2M", "risk_factor": "Concentrated equity", "conversion_trigger": "Liquidity event"},
            {"profile_id": "HAW-2002", "client": "Fabrikam Holdings", "total_wealth": "$7.1M", "held_away_assets": "$1.8M", "risk_factor": "Interest-rate exposure", "conversion_trigger": "Maturing bonds"},
            {"profile_id": "HAW-2003", "client": "Contoso Family Office", "total_wealth": "$21.0M", "held_away_assets": "$6.5M", "risk_factor": "Illiquid real estate", "conversion_trigger": "Estate review"},
        ],
    },
    "planning_gap_analysis": {
        "name": "Planning Gap Analysis",
        "response": "Here are the client's planning gaps and risk exposures across investment, estate planning, and tax, with priorities to validate.",
        "source_system": "Dynamics 365",
        "customer": "the wealth advisory firm",
        "write": False,
        "generative": False,
        "exact_key_required": True,
        "key_field": "gap_id",
        "knowledge": [
            "Surface planning gaps, diversification needs, and upcoming life events.",
            "Detect planning gaps and risk exposures to support proactive, high-value client conversations.",
            "The agent evaluates investment, estate planning, and tax gaps.",
            "This helps the advisor quickly validate priorities and prepare to have the right conversation.",
        ],
        "records": [
            {"gap_id": "GAP-3001", "client": "Northwind Traders", "investment_gap": "Overweight single stock", "estate_gap": "No updated will", "tax_gap": "Unused loss harvesting", "severity": "High"},
            {"gap_id": "GAP-3002", "client": "Fabrikam Holdings", "investment_gap": "Low diversification", "estate_gap": "Trust unfunded", "tax_gap": "Suboptimal account location", "severity": "Medium"},
            {"gap_id": "GAP-3003", "client": "Contoso Family Office", "investment_gap": "Cash drag", "estate_gap": "Outdated beneficiaries", "tax_gap": "No gifting strategy", "severity": "High"},
        ],
    },
    "engagement_strategy": {
        "name": "Engagement Strategy",
        "response": "Here is a personalized engagement strategy with a phased approach, including personal outreach, discovery topics, and key messages.",
        "source_system": "Dynamics 365",
        "customer": "the wealth advisory firm",
        "write": False,
        "generative": True,
        "exact_key_required": True,
        "key_field": "strategy_id",
        "knowledge": [
            "Prioritize actions based on potential impact and relationship readiness.",
            "Drawing customer intelligence from Dynamics 365, the agent outlines a personalized engagement strategy with a phased approach.",
            "The phased approach includes personal outreach, discovery topics, and key messages.",
            "The advisor is empowered to act with more clarity and confidence.",
        ],
        "records": [
            {"strategy_id": "ENG-4001", "client": "Northwind Traders", "phase": "Phase 1 discovery", "personal_outreach": "Advisor call", "discovery_topic": "Business succession", "key_message": "Consolidate held-away assets"},
            {"strategy_id": "ENG-4002", "client": "Fabrikam Holdings", "phase": "Phase 2 planning", "personal_outreach": "Portfolio review meeting", "discovery_topic": "Retirement income", "key_message": "Bridge the income gap"},
            {"strategy_id": "ENG-4003", "client": "Contoso Family Office", "phase": "Phase 1 discovery", "personal_outreach": "Family meeting", "discovery_topic": "Legacy goals", "key_message": "Coordinate estate transfer"},
        ],
    },
    "outreach_materials": {
        "name": "Outreach Materials",
        "response": "Here are ready-to-use outreach materials, including an outreach email and meeting agenda that can be shared with the client through Outlook.",
        "source_system": "Dynamics 365 CRM",
        "customer": "the wealth advisory firm",
        "write": True,
        "generative": True,
        "exact_key_required": True,
        "key_field": "draft_id",
        "knowledge": [
            "Generate personalized outreach content and meeting materials.",
            "To move into execution mode, the advisor requests an outreach e-mail and meeting agenda.",
            "The agent produces ready to use materials that can be shared with the client through Outlook.",
            "This capability records an external action by preparing materials for delivery through Outlook.",
        ],
        "records": [
            {"draft_id": "OUT-5001", "client": "Northwind Traders", "channel": "Outlook email", "subject": "Unlocking your full wealth picture", "meeting_agenda": "Held-away asset review", "status": "Ready to send"},
            {"draft_id": "OUT-5002", "client": "Fabrikam Holdings", "channel": "Outlook email", "subject": "Preparing your retirement income plan", "meeting_agenda": "Income strategy walkthrough", "status": "Ready to send"},
            {"draft_id": "OUT-5003", "client": "Contoso Family Office", "channel": "Outlook email", "subject": "Aligning your family legacy plan", "meeting_agenda": "Estate coordination session", "status": "Ready to send"},
        ],
    },
    "workflow_summary": {
        "name": "Workflow Summary",
        "response": "Here is a complete workflow summary compiling insights, opportunities, and next actions for consistent follow through.",
        "source_system": "Dynamics 365",
        "customer": "the wealth advisory firm",
        "write": False,
        "generative": True,
        "exact_key_required": True,
        "key_field": "summary_id",
        "knowledge": [
            "Equipped advisors with complete materials and action plans.",
            "The agent compiles insights, opportunities, and next actions.",
            "This creates a complete view the advisor can use to drive consistent follow through.",
            "Improved advisor productivity by replacing hours of manual research with instant insights.",
        ],
        "records": [
            {"summary_id": "SUM-6001", "client": "Northwind Traders", "insight": "Largest held-away opportunity", "opportunity": "Consolidate $4.2M", "next_action": "Send outreach and schedule review", "readiness": "High"},
            {"summary_id": "SUM-6002", "client": "Fabrikam Holdings", "insight": "Retirement income gap", "opportunity": "Reposition $1.8M", "next_action": "Book planning meeting", "readiness": "Medium"},
            {"summary_id": "SUM-6003", "client": "Contoso Family Office", "insight": "Estate transfer window", "opportunity": "Coordinate $6.5M", "next_action": "Convene family meeting", "readiness": "High"},
        ],
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _total_aum():
    """Calculate total AUM across all clients."""
    return sum(c["aum"] for c in CLIENT_PORTFOLIOS.values())


def _avg_alpha():
    """Calculate average alpha across client portfolios."""
    alphas = [c["alpha"] for c in CLIENT_PORTFOLIOS.values()]
    return round(sum(alphas) / len(alphas), 2) if alphas else 0


def _client_health(client):
    """Assess client relationship health."""
    if client["alpha"] >= 1.0 and client["ytd_return"] > client["benchmark_return"]:
        return "Strong"
    elif client["alpha"] >= 0:
        return "Satisfactory"
    return "Attention Needed"


def _field_label(field):
    """Human-readable column label from a snake_case field name."""
    return field.replace("_", " ").title()


def _normalized_lookup_tokens(value):
    """Normalize whitespace-delimited tokens without permitting embedded IDs."""
    normalized = []
    for token in str(value or "").casefold().split():
        cleaned = "".join(char for char in token if char.isalnum())
        if cleaned:
            normalized.append(cleaned)
    return normalized


def _contains_normalized_key(user_input, key):
    """Return True only when the complete normalized key is a token sequence."""
    query = _normalized_lookup_tokens(user_input)
    expected = _normalized_lookup_tokens(key)
    width = len(expected)
    return bool(width) and any(
        query[index:index + width] == expected
        for index in range(len(query) - width + 1)
    )


def _match_records(records, key_field, search_text):
    """Return one exact normalized key match, all records for no input, or none."""
    if search_text:
        matches = [
            record for record in records
            if _contains_normalized_key(search_text, record[key_field])
        ]
        if len(matches) == 1:
            return matches, str(matches[0][key_field])
        return [], None
    return records, None


def _render_records_table(records):
    """Render records as a markdown table using their fields as columns."""
    if not records:
        return ["_No matching records._"]
    fields = list(records[0].keys())
    header = "| " + " | ".join(_field_label(f) for f in fields) + " |"
    divider = "|" + "|".join(["---"] * len(fields)) + "|"
    rows = [header, divider]
    for r in records:
        rows.append("| " + " | ".join(str(r.get(f, "")) for f in fields) + " |")
    return rows


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class WealthInsightsGeneratorAgent(BasicAgent):
    """Wealth management insights generator agent."""

    def __init__(self):
        self.name = "WealthInsightsGeneratorAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Wealth Insights Generator Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "market_brief",
                            "client_insights",
                            "opportunity_alerts",
                            "performance_attribution",
                            "portfolio_opportunity_scan",
                            "held_away_wealth_profile",
                            "planning_gap_analysis",
                            "engagement_strategy",
                            "outreach_materials",
                            "workflow_summary",
                        ],
                    },
                    "client_id": {"type": "string"},
                    "user_input": {
                        "type": "string",
                        "description": "Optional natural-language request; an exact record key (e.g. WIG-1001) selects a single record.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "market_brief")
        dispatch = {
            "market_brief": self._market_brief,
            "client_insights": self._client_insights,
            "opportunity_alerts": self._opportunity_alerts,
            "performance_attribution": self._performance_attribution,
        }
        handler = dispatch.get(operation)
        if handler:
            return handler(**kwargs)
        if operation in PORTFOLIO_INTELLIGENCE:
            return self._portfolio_capability(operation, **kwargs)
        return f"**Error:** Unknown operation `{operation}`."

    def _market_brief(self, **kwargs) -> str:
        lines = ["# Daily Market Brief\n"]
        lines.append("## Index Performance\n")
        lines.append("| Index | Current | YTD Return | P/E | Yield |")
        lines.append("|---|---|---|---|---|")
        for idx, data in MARKET_DATA.items():
            pe = f"{data['pe_ratio']:.1f}" if data["pe_ratio"] else "N/A"
            yld = f"{data['dividend_yield']:.2f}%" if data["dividend_yield"] else "N/A"
            lines.append(f"| {idx} | {data['current']:,.2f} | {data['ytd_return']:+.1f}% | {pe} | {yld} |")
        lines.append("\n## Key Observations\n")
        lines.append("- Equity markets continue positive YTD momentum; NASDAQ leading at +6.2%")
        lines.append("- International developed markets (EAFE) outperforming on weaker dollar")
        lines.append("- Fixed income subdued with 10-Year Treasury at 4.28%")
        lines.append("- Gold rally continues (+8.1% YTD) on geopolitical uncertainty")
        lines.append(f"\n**Total Practice AUM:** ${_total_aum():,.0f}")
        return "\n".join(lines)

    def _client_insights(self, **kwargs) -> str:
        lines = ["# Client Insights Report\n"]
        lines.append(f"**Total AUM:** ${_total_aum():,.0f}")
        lines.append(f"**Average Alpha:** {_avg_alpha()}%\n")
        lines.append("| Client | AUM | Strategy | YTD | Alpha | Health | Next Review |")
        lines.append("|---|---|---|---|---|---|---|")
        for cid, c in CLIENT_PORTFOLIOS.items():
            health = _client_health(c)
            lines.append(
                f"| {c['name']} ({cid}) | ${c['aum']:,.0f} | {c['strategy'].replace('_', ' ').title()} "
                f"| {c['ytd_return']:+.1f}% | {c['alpha']:+.1f}% | {health} | {c['next_review']} |"
            )
        lines.append("\n## Life Events & Planning Needs\n")
        for cid, c in CLIENT_PORTFOLIOS.items():
            if c["life_events"]:
                lines.append(f"### {c['name']} ({cid})\n")
                for event in c["life_events"]:
                    lines.append(f"- {event}")
                lines.append("")
        return "\n".join(lines)

    def _opportunity_alerts(self, **kwargs) -> str:
        live = _live_alerts()
        if live:
            lines = ["# Opportunity Alerts (live tenant)\n"]
            for label, priority in (("High Priority", "high"), ("Medium Priority", "medium")):
                bucket = [s for s in live if s["priority"] == priority]
                if not bucket:
                    continue
                lines.append(f"## {label}\n")
                for s in bucket:
                    lines.append(f"### {s['client']} — Open Pipeline\n")
                    lines.append(f"- **Description:** {s['description']}")
                    lines.append(f"- **Recommended Action:** {s['action']}")
                    lines.append(f"- **Owner:** {s['owner']}")
                    lines.append("- **Life Events:** n/a — enrichment seam\n")
            lines.append(f"**Total Alerts:** {len(live)}")
            lines.append(
                "\n_Source: live Static Dynamics 365 tenant — open opportunities "
                "reinterpreted as advisor opportunity alerts. Life events and "
                "planning context are enrichment seams._"
            )
            return "\n".join(lines)

        lines = ["# Opportunity Alerts\n"]
        high = [s for s in OPPORTUNITY_SIGNALS if s["priority"] == "high"]
        medium = [s for s in OPPORTUNITY_SIGNALS if s["priority"] == "medium"]
        if high:
            lines.append("## High Priority\n")
            for s in high:
                client = CLIENT_PORTFOLIOS.get(s["client"], {})
                lines.append(f"### {client.get('name', s['client'])} — {s['type'].replace('_', ' ').title()}\n")
                lines.append(f"- **Description:** {s['description']}")
                lines.append(f"- **Recommended Action:** {s['action']}\n")
        if medium:
            lines.append("## Medium Priority\n")
            for s in medium:
                client = CLIENT_PORTFOLIOS.get(s["client"], {})
                lines.append(f"### {client.get('name', s['client'])} — {s['type'].replace('_', ' ').title()}\n")
                lines.append(f"- **Description:** {s['description']}")
                lines.append(f"- **Recommended Action:** {s['action']}\n")
        lines.append(f"**Total Alerts:** {len(OPPORTUNITY_SIGNALS)}")
        lines.append("\n_Source: embedded demo layer (offline fallback)._")
        return "\n".join(lines)

    def _performance_attribution(self, **kwargs) -> str:
        lines = ["# Performance Attribution\n"]
        lines.append("## Strategy Benchmarks\n")
        lines.append("| Strategy | Benchmark | 1-Year | 3-Year | 5-Year |")
        lines.append("|---|---|---|---|---|")
        for strat, bench in PERFORMANCE_BENCHMARKS.items():
            lines.append(
                f"| {strat.replace('_', ' ').title()} | {bench['benchmark']} "
                f"| {bench['1yr']}% | {bench['3yr']}% | {bench['5yr']}% |"
            )
        lines.append("\n## Client Performance vs Benchmark\n")
        lines.append("| Client | Strategy | YTD | Benchmark | Alpha | Attribution |")
        lines.append("|---|---|---|---|---|---|")
        for cid, c in CLIENT_PORTFOLIOS.items():
            if c["alpha"] >= 1.0:
                attribution = "Selection + Allocation"
            elif c["alpha"] >= 0:
                attribution = "Allocation"
            else:
                attribution = "Underperformance"
            lines.append(
                f"| {c['name']} | {c['strategy'].replace('_', ' ').title()} "
                f"| {c['ytd_return']:+.1f}% | {c['benchmark_return']:+.1f}% "
                f"| {c['alpha']:+.1f}% | {attribution} |"
            )
        total_alpha_weighted = sum(c["alpha"] * c["aum"] for c in CLIENT_PORTFOLIOS.values()) / _total_aum()
        lines.append(f"\n**AUM-Weighted Alpha:** {total_alpha_weighted:+.2f}%")
        return "\n".join(lines)

    def _portfolio_capability(self, cap_key, **kwargs) -> str:
        """Render a portfolio-intelligence capability.

        Data-driven: exact-key matching on optional user_input, three synthetic
        records, knowledge context, a useful summary, and — for write-capable
        capabilities — a simulated receipt with no mutation.
        """
        cap = PORTFOLIO_INTELLIGENCE[cap_key]
        key_field = cap["key_field"]
        records = cap["records"]

        search_parts = [str(kwargs.get(k, "")) for k in ("user_input", "client_id", key_field)]
        search_text = " ".join(p for p in search_parts if p)
        shown, matched_key = _match_records(records, key_field, search_text)

        write_flag = "Yes" if cap["write"] else "No"
        gen_flag = "Yes" if cap["generative"] else "No"

        lines = [f"# {cap['name']}\n", cap["response"], ""]
        lines.append(
            f"*Source system: {cap['source_system']} · Customer: {cap['customer']} · "
            f"Write: {write_flag} · Generative: {gen_flag} · Exact key: {cap['key_field']}*\n"
        )

        lines.append("## Records\n")
        lines.extend(_render_records_table(shown))
        lines.append("")

        lines.append("## Knowledge\n")
        for k in cap["knowledge"]:
            lines.append(f"- {k}")
        lines.append("")

        lines.append("## Summary\n")
        if matched_key:
            rec = shown[0]
            lines.append(f"- Exact-key match on `{key_field}` = **{matched_key}** ({rec.get('client', 'client')}).")
            highlight = [f"{_field_label(f)}: {v}" for f, v in rec.items() if f != key_field]
            lines.append(f"- {'; '.join(highlight)}.")
        elif search_text:
            lines.append(f"- No exact normalized `{key_field}` matched the request.")
        else:
            lines.append(
                f"- Showing all {len(shown)} record(s). Provide a `{key_field}` "
                f"(e.g. {records[0][key_field]}) via user_input for an exact single-record view."
            )
            high = [r for r in shown if str(r.get("priority", r.get("severity", r.get("readiness", "")))).lower() == "high"]
            if high:
                lines.append(f"- {len(high)} high-priority record(s): " + ", ".join(r["client"] for r in high) + ".")
        lines.append("")

        if cap["write"] and (matched_key or not search_text):
            target = matched_key or shown[0][key_field]
            lines.append("## Write Receipt (Simulated)\n")
            lines.append(f"- Action: prepared {cap['name'].lower()} for delivery via {cap['source_system']}.")
            lines.append(f"- Reference: {key_field} = {target}.")
            lines.append(f"- Receipt ID: RCPT-{str(target).replace('-', '')}")
            lines.append("- Status: **SIMULATED** — no external system was modified and no data was mutated.")

        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = WealthInsightsGeneratorAgent()
    print("=" * 80)
    print("EMBEDDED DEMO MARKET BRIEF (works offline)")
    print(agent.perform(operation="market_brief"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="client_insights"))
    print("\n" + "=" * 80 + "\n")
    print("LIVE TENANT OPPORTUNITY ALERTS (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="opportunity_alerts"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="performance_attribution"))
    for op in (
        "portfolio_opportunity_scan",
        "held_away_wealth_profile",
        "planning_gap_analysis",
        "engagement_strategy",
        "outreach_materials",
        "workflow_summary",
    ):
        print("\n" + "=" * 80 + "\n")
        print(agent.perform(operation=op))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
