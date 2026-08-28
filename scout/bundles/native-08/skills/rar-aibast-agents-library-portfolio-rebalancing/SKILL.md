---
name: "rar-aibast-agents-library-portfolio-rebalancing"
description: "Analyzes portfolio drift and trades from a live simulated Dynamics 365 tenant (product lines as positions), with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/portfolio_rebalancing", "rar_sha256": "0f1d4d1d56d9c6249854b927421a486038d693daa784e6d4e7fbaccf6c19f83f", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["portfolio", "rebalancing", "allocation", "tax", "trading", "financial-services", "retirement-projection", "risk-analysis"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/portfolio_rebalancing`. The original RAPP
agent is preserved byte-for-byte in `portfolio_rebalancing_agent.py` and in the RCI capsule.

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

Portfolio Rebalancing Agent — a template you are meant to mutate.

Analyzes portfolio drift, generates rebalancing recommendations, assesses
tax impact, and creates execution plans. In this template a portfolio is
represented as a Dynamics 365 opportunity and its product lines are the
positions — the tenant has no native holdings entity, so line-item values
give real allocations while target weights stay an enrichment seam.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `portfolio_analysis` operation pulls live
     opportunity product lines over real HTTP from the globally hosted
     Static Dynamics 365 tenant (Aster Lane Office Systems — synthetic
     data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="portfolio_analysis")
     and look for the "Foxglove Learning — Secure print rollout" book
     with its Sensor Kit K4 position.
  2. No network? Everything falls back to the embedded demo layer below
     (PORTFOLIOS / TAX_RATES) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PORTFOLIO_REBALANCING_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your custodian), or replace
     _fetch_collection() with your own client. The fields the rest of the
     file needs are listed in _normalize_live_portfolio() — target
     weights and cost basis render "n/a — enrichment seam" until you wire
     your model-portfolio and tax-lot systems.

OPERATIONS
  portfolio_analysis | rebalance_recommendation | tax_impact
  | execution_plan | retirement_projection | risk_analysis
  | client_deliverables
  kwargs: operation (required), portfolio_id, user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "enum": [
        "portfolio_analysis",
        "rebalance_recommendation",
        "tax_impact",
        "execution_plan",
        "retirement_projection",
        "risk_analysis",
        "client_deliverables"
      ],
      "type": "string"
    },
    "portfolio_id": {
      "type": "string"
    },
    "user_input": {
      "description": "Optional exact evidence-record key, such as PROJ-7101, RISK-8201, or DLV-9301.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `portfolio_rebalancing_agent.py` and embedded as the fenced Python below (sha256 0f1d4d1d56d9c624…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `portfolio_rebalancing_agent.py` first:

```bash
python3 portfolio_rebalancing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 portfolio_rebalancing_agent.py   # or on stdin
python3 portfolio_rebalancing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Portfolio Rebalancing Agent — a template you are meant to mutate.

Analyzes portfolio drift, generates rebalancing recommendations, assesses
tax impact, and creates execution plans. In this template a portfolio is
represented as a Dynamics 365 opportunity and its product lines are the
positions — the tenant has no native holdings entity, so line-item values
give real allocations while target weights stay an enrichment seam.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `portfolio_analysis` operation pulls live
     opportunity product lines over real HTTP from the globally hosted
     Static Dynamics 365 tenant (Aster Lane Office Systems — synthetic
     data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="portfolio_analysis")
     and look for the "Foxglove Learning — Secure print rollout" book
     with its Sensor Kit K4 position.
  2. No network? Everything falls back to the embedded demo layer below
     (PORTFOLIOS / TAX_RATES) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PORTFOLIO_REBALANCING_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your custodian), or replace
     _fetch_collection() with your own client. The fields the rest of the
     file needs are listed in _normalize_live_portfolio() — target
     weights and cost basis render "n/a — enrichment seam" until you wire
     your model-portfolio and tax-lot systems.

OPERATIONS
  portfolio_analysis | rebalance_recommendation | tax_impact
  | execution_plan | retirement_projection | risk_analysis
  | client_deliverables
  kwargs: operation (required), portfolio_id, user_input
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json as _json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/portfolio_rebalancing",
    "version": "1.2.0",
    "display_name": "Portfolio Rebalancing Agent",
    "description": "Analyzes portfolio drift and trades from a live simulated Dynamics 365 tenant (product lines as positions), with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["portfolio", "rebalancing", "allocation", "tax", "trading", "financial-services", "retirement-projection", "risk-analysis"],
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
#   export PORTFOLIO_REBALANCING_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your custodian client. Downstream
# code only needs the fields produced by _normalize_live_portfolio().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "PORTFOLIO_REBALANCING_DATA_URL",
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


def _normalize_live_portfolio(opp_name, lines):
    """Project one opportunity's product lines onto the portfolio shape
    this agent uses. THIS is the contract your replacement data source
    must meet — a dict with these keys. None means 'not knowable from the
    CRM alone' and the renderers label it as an enrichment seam."""
    total = sum(float(l.get("extendedamount") or 0) for l in lines)
    holdings = {}
    for l in lines:
        name = l.get("productidname", "Unknown position")
        value = float(l.get("extendedamount") or 0)
        holdings[name] = {
            "value": value,
            "quantity": float(l.get("quantity") or 0),
            "current_pct": round(value / total * 100, 1) if total else 0.0,
            "target_pct": None,   # enrichment seam — wire your model portfolios
            "cost_basis": None,   # enrichment seam — wire your tax-lot system
        }
    return {
        "name": opp_name,
        "manager": lines[0].get("owneridname", "") if lines else "",
        "total_value": total,
        "holdings": holdings,
        "_live": True,
    }


def _live_portfolios():
    """opportunity-keyed dict of live tenant portfolios; {} when offline."""
    rows = _fetch_collection("opportunityproducts")
    if not rows:
        return {}
    grouped = {}
    for row in rows:
        grouped.setdefault(row.get("opportunityidname", "Unknown"), []).append(row)
    return {
        f"PORT-{str(lines[0].get('opportunityid', ''))[:8]}": _normalize_live_portfolio(opp_name, lines)
        for opp_name, lines in grouped.items()
    }


def _seam(value, formatter=str):
    """None = the CRM alone can't know this (enrichment seam)."""
    return "n/a — enrichment seam" if value is None else formatter(value)


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

PORTFOLIOS = {
    "PORT-5001": {
        "name": "Growth Allocation Fund",
        "manager": "Victoria Reeves, CFA",
        "strategy": "growth",
        "total_value": 12450000,
        "benchmark": "60/40 Growth Blend",
        "rebalance_frequency": "quarterly",
        "drift_threshold": 3.0,
        "holdings": {
            "US Large Cap": {"ticker": "VTI", "value": 4357500, "current_pct": 35.0, "target_pct": 30.0, "cost_basis": 3800000},
            "US Small Cap": {"ticker": "VB", "value": 872500, "current_pct": 7.0, "target_pct": 10.0, "cost_basis": 750000},
            "Intl Developed": {"ticker": "VEA", "value": 1493750, "current_pct": 12.0, "target_pct": 15.0, "cost_basis": 1600000},
            "Emerging Markets": {"ticker": "VWO", "value": 622500, "current_pct": 5.0, "target_pct": 5.0, "cost_basis": 680000},
            "US Aggregate Bond": {"ticker": "BND", "value": 3112500, "current_pct": 25.0, "target_pct": 25.0, "cost_basis": 3200000},
            "TIPS": {"ticker": "VTIP", "value": 622500, "current_pct": 5.0, "target_pct": 5.0, "cost_basis": 600000},
            "REITs": {"ticker": "VNQ", "value": 622500, "current_pct": 5.0, "target_pct": 5.0, "cost_basis": 550000},
            "Cash": {"ticker": "VMFXX", "value": 746250, "current_pct": 6.0, "target_pct": 5.0, "cost_basis": 746250},
        },
    },
    "PORT-5002": {
        "name": "Conservative Income Portfolio",
        "manager": "Daniel Kim, CFP",
        "strategy": "income",
        "total_value": 8200000,
        "benchmark": "30/70 Income Blend",
        "rebalance_frequency": "semi-annual",
        "drift_threshold": 2.0,
        "holdings": {
            "US Large Cap Dividend": {"ticker": "VYM", "value": 1312000, "current_pct": 16.0, "target_pct": 15.0, "cost_basis": 1100000},
            "Intl Dividend": {"ticker": "VYMI", "value": 656000, "current_pct": 8.0, "target_pct": 10.0, "cost_basis": 700000},
            "US Investment Grade": {"ticker": "VCIT", "value": 2132000, "current_pct": 26.0, "target_pct": 25.0, "cost_basis": 2250000},
            "US Treasury": {"ticker": "VGIT", "value": 1640000, "current_pct": 20.0, "target_pct": 20.0, "cost_basis": 1700000},
            "Municipal Bonds": {"ticker": "VTEB", "value": 1148000, "current_pct": 14.0, "target_pct": 15.0, "cost_basis": 1200000},
            "High Yield": {"ticker": "VWEHX", "value": 492000, "current_pct": 6.0, "target_pct": 5.0, "cost_basis": 460000},
            "Preferred Stock": {"ticker": "PFF", "value": 410000, "current_pct": 5.0, "target_pct": 5.0, "cost_basis": 420000},
            "Cash": {"ticker": "VMFXX", "value": 410000, "current_pct": 5.0, "target_pct": 5.0, "cost_basis": 410000},
        },
    },
}

TAX_RATES = {
    "short_term_capital_gains": 0.37,
    "long_term_capital_gains": 0.20,
    "qualified_dividends": 0.20,
    "ordinary_income": 0.37,
    "net_investment_income_tax": 0.038,
}

EVIDENCE_CAPABILITIES = {
    "retirement_projection": {
        "name": "Retirement Projection Modeling",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": False,
        "key_field": "projection_id",
        "knowledge": [
            "The agent models retirement projections by running simulations to estimate future values and income coverage (demo 00:01:30-00:01:37).",
            "The manager uses the projections to validate the strategy and finalize decisions (demo 00:01:37-00:01:42).",
            "The one-pager identifies retirement projection modeling and success calculations as a core agent capability.",
        ],
        "records": [
            {"projection_id": "PROJ-7101", "portfolio_id": "PORT-5001", "horizon_years": 20, "projected_value": "$25.8M", "income_coverage": "118%", "success_probability": "91%"},
            {"projection_id": "PROJ-7102", "portfolio_id": "PORT-5002", "horizon_years": 15, "projected_value": "$12.7M", "income_coverage": "104%", "success_probability": "86%"},
            {"projection_id": "PROJ-7103", "portfolio_id": "PORT-5001", "horizon_years": 25, "projected_value": "$31.4M", "income_coverage": "126%", "success_probability": "94%"},
        ],
    },
    "risk_analysis": {
        "name": "Portfolio Risk Analysis",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": False,
        "key_field": "risk_id",
        "knowledge": [
            "The agent surfaces key factors showing potential risk reduction before the manager completes the review (demo 00:01:43-00:01:55).",
            "Portfolio drift and risk are analyzed together to keep allocations aligned to investment goals (one-pager, Slide 1).",
            "Market signals and client-specific factors ground the risk view (demo 00:00:50-00:00:58).",
        ],
        "records": [
            {"risk_id": "RISK-8201", "portfolio_id": "PORT-5001", "factor": "US large-cap concentration", "current_exposure": "35%", "proposed_exposure": "30%", "risk_effect": "Concentration reduced"},
            {"risk_id": "RISK-8202", "portfolio_id": "PORT-5002", "factor": "Interest-rate duration", "current_exposure": "46%", "proposed_exposure": "44%", "risk_effect": "Duration reduced"},
            {"risk_id": "RISK-8203", "portfolio_id": "PORT-5001", "factor": "International underweight", "current_exposure": "12%", "proposed_exposure": "15%", "risk_effect": "Diversification improved"},
        ],
    },
    "client_deliverables": {
        "name": "Client-Ready Deliverables and Audit Logging",
        "source_system": "Microsoft 365 and Dynamics 365 CRM",
        "write": True,
        "generative": True,
        "key_field": "deliverable_id",
        "knowledge": [
            "The agent drafts client-ready materials in Word and Excel and surfaces updates in Microsoft Teams (demo 00:01:56-00:02:03).",
            "Approved actions are logged back to Dynamics for complete audit-ready records (demo 00:02:03-00:02:08).",
            "The one-pager calls for presentations and implementation plans that clearly demonstrate advisor value.",
        ],
        "records": [
            {"deliverable_id": "DLV-9301", "portfolio_id": "PORT-5001", "word_brief": "Ready", "excel_model": "Ready", "teams_update": "Prepared", "dynamics_log": "Pending approval"},
            {"deliverable_id": "DLV-9302", "portfolio_id": "PORT-5002", "word_brief": "Ready", "excel_model": "Ready", "teams_update": "Prepared", "dynamics_log": "Pending approval"},
            {"deliverable_id": "DLV-9303", "portfolio_id": "PORT-5001", "word_brief": "Draft", "excel_model": "Ready", "teams_update": "Not prepared", "dynamics_log": "Awaiting review"},
        ],
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _calculate_drift(portfolio):
    """Calculate drift for each holding and identify rebalance needs."""
    trades = []
    for asset, data in portfolio["holdings"].items():
        drift = round(data["current_pct"] - data["target_pct"], 2)
        if abs(drift) >= portfolio["drift_threshold"]:
            target_value = portfolio["total_value"] * data["target_pct"] / 100
            trade_value = round(target_value - data["value"], 2)
            trades.append({
                "asset": asset,
                "ticker": data["ticker"],
                "current_pct": data["current_pct"],
                "target_pct": data["target_pct"],
                "drift": drift,
                "action": "sell" if drift > 0 else "buy",
                "trade_value": abs(trade_value),
            })
    return trades


def _estimate_tax(holding, sell_amount):
    """Estimate tax liability on a sale."""
    cost_basis = holding["cost_basis"]
    current_value = holding["value"]
    if current_value == 0:
        return 0
    gain_pct = (current_value - cost_basis) / current_value
    gain = sell_amount * gain_pct
    if gain <= 0:
        return 0
    tax_rate = TAX_RATES["long_term_capital_gains"] + TAX_RATES["net_investment_income_tax"]
    return round(gain * tax_rate, 2)


def _max_drift(portfolio):
    """Find maximum absolute drift in portfolio."""
    drifts = [abs(d["current_pct"] - d["target_pct"]) for d in portfolio["holdings"].values()]
    return max(drifts) if drifts else 0


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


def _evidence_capability(operation, user_input=""):
    """Render a deterministic evidence-derived capability."""
    capability = EVIDENCE_CAPABILITIES[operation]
    records = capability["records"]
    key_field = capability["key_field"]
    lookup_supplied = bool(str(user_input or "").strip())
    matches = [
        record for record in records
        if _contains_normalized_key(user_input, record[key_field])
    ]
    match = matches[0] if len(matches) == 1 else None

    lines = [f"# {capability['name']}\n"]
    lines.append(f"**Source System:** {capability['source_system']}")
    lines.append(f"**Lookup Key:** `{key_field}`\n")
    if match:
        lines.append(f"## Record {match[key_field]}\n")
        for field, value in match.items():
            lines.append(f"- **{field.replace('_', ' ').title()}:** {value}")
    elif lookup_supplied:
        lines.append(
            f"No exact normalized `{key_field}` matched the request."
        )
    else:
        headers = list(records[0])
        lines.append(f"## Summary — {len(records)} records\n")
        lines.append("| " + " | ".join(field.replace("_", " ").title() for field in headers) + " |")
        lines.append("|" + "|".join("---" for _ in headers) + "|")
        for record in records:
            lines.append("| " + " | ".join(str(record[field]) for field in headers) + " |")

    if capability["write"] and match:
        lines.append("\n## Simulated Write Receipt\n")
        lines.append(f"- **Receipt ID:** SIM-{match[key_field]}")
        lines.append(f"- **Target:** {capability['source_system']}")
        lines.append("- **Status:** Simulated only — no external system or record was modified.")

    lines.append("\n## Knowledge\n")
    for fact in capability["knowledge"]:
        lines.append(f"- {fact}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class PortfolioRebalancingAgent(BasicAgent):
    """Portfolio rebalancing agent."""

    def __init__(self):
        self.name = "PortfolioRebalancingAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Portfolio Rebalancing Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "portfolio_analysis",
                            "rebalance_recommendation",
                            "tax_impact",
                            "execution_plan",
                            "retirement_projection",
                            "risk_analysis",
                            "client_deliverables",
                        ],
                    },
                    "portfolio_id": {"type": "string"},
                    "user_input": {
                        "type": "string",
                        "description": "Optional exact evidence-record key, such as PROJ-7101, RISK-8201, or DLV-9301.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "portfolio_analysis")
        dispatch = {
            "portfolio_analysis": self._portfolio_analysis,
            "rebalance_recommendation": self._rebalance_recommendation,
            "tax_impact": self._tax_impact,
            "execution_plan": self._execution_plan,
        }
        handler = dispatch.get(operation)
        if handler:
            return handler(**kwargs)
        if operation in EVIDENCE_CAPABILITIES:
            return _evidence_capability(operation, kwargs.get("user_input", ""))
        return f"**Error:** Unknown operation `{operation}`."

    def _portfolio_analysis(self, **kwargs) -> str:
        live = _live_portfolios()
        if live:
            lines = ["# Portfolio Analysis (live tenant)\n"]
            for pid, port in live.items():
                lines.append(f"## {pid}: {port['name']}\n")
                lines.append(f"- **Manager:** {port['manager']}")
                lines.append(f"- **Total Value:** ${port['total_value']:,.0f}")
                lines.append("- **Rebalance Needed:** unknown — target weights are an enrichment seam\n")
                lines.append("| Position | Qty | Value | Current % | Target % | Drift |")
                lines.append("|---|---|---|---|---|---|")
                for asset, data in port["holdings"].items():
                    lines.append(
                        f"| {asset} | {data['quantity']:g} | ${data['value']:,.0f} "
                        f"| {data['current_pct']}% | {_seam(data['target_pct'])} "
                        f"| {_seam(data['target_pct'], lambda _: '—')} |"
                    )
                lines.append("")
            lines.append(
                "_Source: live Static Dynamics 365 tenant — opportunity product "
                "lines reinterpreted as portfolio positions. Target weights and "
                "cost basis are enrichment seams (wire your model-portfolio and "
                "tax-lot systems)._"
            )
            return "\n".join(lines)

        lines = ["# Portfolio Analysis\n"]
        for pid, port in PORTFOLIOS.items():
            max_d = _max_drift(port)
            needs_rebalance = "Yes" if max_d >= port["drift_threshold"] else "No"
            lines.append(f"## {pid}: {port['name']}\n")
            lines.append(f"- **Manager:** {port['manager']}")
            lines.append(f"- **Strategy:** {port['strategy'].title()}")
            lines.append(f"- **Total Value:** ${port['total_value']:,.0f}")
            lines.append(f"- **Benchmark:** {port['benchmark']}")
            lines.append(f"- **Max Drift:** {max_d:.1f}%")
            lines.append(f"- **Drift Threshold:** {port['drift_threshold']}%")
            lines.append(f"- **Rebalance Needed:** {needs_rebalance}\n")
            lines.append("| Asset | Ticker | Value | Current % | Target % | Drift |")
            lines.append("|---|---|---|---|---|---|")
            for asset, data in port["holdings"].items():
                drift = round(data["current_pct"] - data["target_pct"], 1)
                sign = "+" if drift > 0 else ""
                lines.append(
                    f"| {asset} | {data['ticker']} | ${data['value']:,.0f} "
                    f"| {data['current_pct']}% | {data['target_pct']}% | {sign}{drift}% |"
                )
            lines.append("")
        lines.append("_Source: embedded demo layer (offline fallback)._")
        return "\n".join(lines)

    def _rebalance_recommendation(self, **kwargs) -> str:
        portfolio_id = kwargs.get("portfolio_id", "PORT-5001")
        port = PORTFOLIOS.get(portfolio_id, list(PORTFOLIOS.values())[0])
        trades = _calculate_drift(port)
        lines = [f"# Rebalance Recommendation: {port['name']}\n"]
        lines.append(f"**Portfolio Value:** ${port['total_value']:,.0f}")
        lines.append(f"**Drift Threshold:** {port['drift_threshold']}%\n")
        if not trades:
            lines.append("No rebalancing trades required — all holdings within drift threshold.")
            return "\n".join(lines)
        lines.append("## Recommended Trades\n")
        lines.append("| Asset | Ticker | Action | Current % | Target % | Drift | Trade Amount |")
        lines.append("|---|---|---|---|---|---|---|")
        total_sell = 0
        total_buy = 0
        for t in trades:
            sign = "+" if t["drift"] > 0 else ""
            lines.append(
                f"| {t['asset']} | {t['ticker']} | {t['action'].upper()} "
                f"| {t['current_pct']}% | {t['target_pct']}% | {sign}{t['drift']}% | ${t['trade_value']:,.0f} |"
            )
            if t["action"] == "sell":
                total_sell += t["trade_value"]
            else:
                total_buy += t["trade_value"]
        lines.append(f"\n**Total Sells:** ${total_sell:,.0f}")
        lines.append(f"**Total Buys:** ${total_buy:,.0f}")
        return "\n".join(lines)

    def _tax_impact(self, **kwargs) -> str:
        portfolio_id = kwargs.get("portfolio_id", "PORT-5001")
        port = PORTFOLIOS.get(portfolio_id, list(PORTFOLIOS.values())[0])
        trades = _calculate_drift(port)
        sell_trades = [t for t in trades if t["action"] == "sell"]
        lines = [f"# Tax Impact Analysis: {port['name']}\n"]
        lines.append("## Tax Rate Reference\n")
        for rate_name, rate in TAX_RATES.items():
            lines.append(f"- {rate_name.replace('_', ' ').title()}: {rate * 100:.1f}%")
        lines.append("\n## Estimated Tax on Sell Trades\n")
        if not sell_trades:
            lines.append("No sell trades required.")
            return "\n".join(lines)
        lines.append("| Asset | Ticker | Sell Amount | Cost Basis | Unrealized Gain | Est. Tax |")
        lines.append("|---|---|---|---|---|---|")
        total_tax = 0
        for t in sell_trades:
            holding = port["holdings"][t["asset"]]
            gain_pct = (holding["value"] - holding["cost_basis"]) / holding["value"] if holding["value"] else 0
            unrealized = round(t["trade_value"] * gain_pct, 2)
            tax = _estimate_tax(holding, t["trade_value"])
            total_tax += tax
            lines.append(
                f"| {t['asset']} | {t['ticker']} | ${t['trade_value']:,.0f} "
                f"| ${holding['cost_basis']:,.0f} | ${unrealized:,.0f} | ${tax:,.0f} |"
            )
        lines.append(f"\n**Total Estimated Tax Liability:** ${total_tax:,.0f}")
        lines.append("\n## Tax-Efficient Alternatives\n")
        lines.append("- Direct new contributions to underweight asset classes")
        lines.append("- Use tax-loss positions to offset gains")
        lines.append("- Rebalance within tax-advantaged accounts first")
        lines.append("- Consider charitable donation of appreciated shares")
        return "\n".join(lines)

    def _execution_plan(self, **kwargs) -> str:
        portfolio_id = kwargs.get("portfolio_id", "PORT-5001")
        port = PORTFOLIOS.get(portfolio_id, list(PORTFOLIOS.values())[0])
        trades = _calculate_drift(port)
        lines = [f"# Execution Plan: {port['name']}\n"]
        lines.append(f"**Rebalance Frequency:** {port['rebalance_frequency'].title()}")
        lines.append(f"**Total Trades:** {len(trades)}\n")
        if not trades:
            lines.append("No trades required at this time.")
            return "\n".join(lines)
        sell_trades = [t for t in trades if t["action"] == "sell"]
        buy_trades = [t for t in trades if t["action"] == "buy"]
        lines.append("## Step 1: Execute Sells\n")
        if sell_trades:
            for i, t in enumerate(sell_trades, 1):
                lines.append(f"{i}. SELL ${t['trade_value']:,.0f} of {t['ticker']} ({t['asset']})")
        else:
            lines.append("No sells required.")
        lines.append("\n## Step 2: Settle Cash (T+1)\n")
        lines.append("- Allow sell proceeds to settle before purchasing\n")
        lines.append("## Step 3: Execute Buys\n")
        if buy_trades:
            for i, t in enumerate(buy_trades, 1):
                lines.append(f"{i}. BUY ${t['trade_value']:,.0f} of {t['ticker']} ({t['asset']})")
        else:
            lines.append("No buys required.")
        lines.append("\n## Step 4: Verification\n")
        lines.append("- Confirm post-trade allocations match targets")
        lines.append("- Update portfolio records")
        lines.append("- Generate client notification")
        lines.append("- Document compliance review")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = PortfolioRebalancingAgent()
    print("=" * 80)
    print("LIVE TENANT PORTFOLIOS (product lines fetched over HTTP; falls back offline)")
    print(agent.perform(operation="portfolio_analysis"))
    print("\n" + "=" * 80 + "\n")
    print("EMBEDDED DEMO REBALANCE (works offline)")
    print(agent.perform(operation="rebalance_recommendation", portfolio_id="PORT-5001"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="tax_impact", portfolio_id="PORT-5001"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="execution_plan", portfolio_id="PORT-5001"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
