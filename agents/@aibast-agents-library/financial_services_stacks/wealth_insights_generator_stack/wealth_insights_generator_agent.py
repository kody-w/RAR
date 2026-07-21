"""
Wealth Insights Generator Agent — Financial Services Stack

Generates market briefs, client insights, opportunity alerts, and
performance attribution reports for wealth management teams.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/wealth_insights_generator",
    "version": "1.1.1",
    "display_name": "Wealth Insights Generator Agent",
    "description": "Generates market briefs, client insights, opportunity alerts, and performance attribution for wealth teams from built-in demo data.",
    "author": "AIBAST",
    "tags": ["wealth", "insights", "market", "performance", "analytics", "financial-services"],
    "category": "financial_services",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# ---------------------------------------------------------------------------
# Synthetic domain data
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
    print(agent.perform(operation="market_brief"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="client_insights"))
    print("\n" + "=" * 80 + "\n")
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
