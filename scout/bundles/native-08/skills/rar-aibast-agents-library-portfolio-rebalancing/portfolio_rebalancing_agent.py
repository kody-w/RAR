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
