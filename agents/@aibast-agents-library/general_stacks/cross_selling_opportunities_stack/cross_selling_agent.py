"""
Cross-Selling Agent

Identifies cross-selling opportunities by analyzing customer product ownership,
product affinity rules, and revenue impact projections.

Where a real deployment would connect to CRM and product databases, this agent
uses a synthetic data layer so it runs anywhere without credentials.

Version 1.1.0 adds evidence-backed buying-signal analysis, tailored outreach,
growth planning, and simulated account assignment while preserving all legacy
operations and identities.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/cross_selling",
    "version": "1.1.1",
    "display_name": "Cross-Selling Opportunities",
    "description": "Reports cross-sell opportunities, product affinity, and revenue projections from built-in demo account data.",
    "author": "AIBAST",
    "tags": ["cross-sell", "upsell", "revenue", "product-affinity", "recommendations"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# SYNTHETIC DATA LAYER
# ═══════════════════════════════════════════════════════════════

_PRODUCT_CATALOG = {
    "PLAT-100": {"name": "Core Platform", "category": "Platform", "annual_price": 24000, "margin_pct": 72},
    "PLAT-200": {"name": "Enterprise Platform", "category": "Platform", "annual_price": 60000, "margin_pct": 75},
    "ANLYT-100": {"name": "Analytics Standard", "category": "Analytics", "annual_price": 12000, "margin_pct": 82},
    "ANLYT-200": {"name": "Analytics Pro", "category": "Analytics", "annual_price": 28000, "margin_pct": 85},
    "INTGR-100": {"name": "Integration Hub", "category": "Integration", "annual_price": 18000, "margin_pct": 78},
    "SECUR-100": {"name": "Security Suite", "category": "Security", "annual_price": 15000, "margin_pct": 80},
    "SUPRT-100": {"name": "Premium Support", "category": "Support", "annual_price": 8000, "margin_pct": 90},
    "TRAIN-100": {"name": "Training Package", "category": "Services", "annual_price": 5000, "margin_pct": 65},
}

_CUSTOMER_OWNERSHIP = {
    "CUST-001": {
        "name": "Meridian Corp", "segment": "Enterprise", "arr": 84000,
        "products": ["PLAT-200", "ANLYT-100", "SUPRT-100"],
        "tenure_months": 24, "health_score": 92, "contact": "Sandra Lee",
    },
    "CUST-002": {
        "name": "Atlas Digital", "segment": "Mid-Market", "arr": 42000,
        "products": ["PLAT-100", "INTGR-100"],
        "tenure_months": 18, "health_score": 78, "contact": "Marco Torres",
    },
    "CUST-003": {
        "name": "Pinnacle Health", "segment": "Enterprise", "arr": 60000,
        "products": ["PLAT-200"],
        "tenure_months": 6, "health_score": 85, "contact": "Dr. Amy Patel",
    },
    "CUST-004": {
        "name": "Greenleaf Retail", "segment": "Mid-Market", "arr": 24000,
        "products": ["PLAT-100"],
        "tenure_months": 12, "health_score": 65, "contact": "Kevin O'Neill",
    },
    "CUST-005": {
        "name": "Beacon Financial", "segment": "Enterprise", "arr": 113000,
        "products": ["PLAT-200", "ANLYT-200", "INTGR-100", "SECUR-100"],
        "tenure_months": 36, "health_score": 96, "contact": "Rachel Kim",
    },
}

_AFFINITY_RULES = [
    {"if_owns": "PLAT-100", "recommend": "ANLYT-100", "affinity_score": 0.85, "success_rate": 0.42, "avg_time_to_close_days": 35},
    {"if_owns": "PLAT-100", "recommend": "INTGR-100", "affinity_score": 0.72, "success_rate": 0.38, "avg_time_to_close_days": 45},
    {"if_owns": "PLAT-200", "recommend": "ANLYT-200", "affinity_score": 0.91, "success_rate": 0.55, "avg_time_to_close_days": 28},
    {"if_owns": "PLAT-200", "recommend": "SECUR-100", "affinity_score": 0.78, "success_rate": 0.48, "avg_time_to_close_days": 30},
    {"if_owns": "ANLYT-100", "recommend": "ANLYT-200", "affinity_score": 0.88, "success_rate": 0.62, "avg_time_to_close_days": 21},
    {"if_owns": "INTGR-100", "recommend": "SECUR-100", "affinity_score": 0.67, "success_rate": 0.35, "avg_time_to_close_days": 40},
    {"if_owns": "PLAT-200", "recommend": "SUPRT-100", "affinity_score": 0.82, "success_rate": 0.65, "avg_time_to_close_days": 14},
    {"if_owns": "PLAT-100", "recommend": "SUPRT-100", "affinity_score": 0.70, "success_rate": 0.50, "avg_time_to_close_days": 21},
]

_CROSS_SELL_SUCCESS_RATES = {
    "Enterprise": {"avg_success_rate": 0.52, "avg_deal_cycle_days": 28, "avg_expansion_pct": 35},
    "Mid-Market": {"avg_success_rate": 0.38, "avg_deal_cycle_days": 42, "avg_expansion_pct": 25},
    "SMB": {"avg_success_rate": 0.28, "avg_deal_cycle_days": 55, "avg_expansion_pct": 18},
}

_BUYING_SIGNALS = {
    "CUST-001": ["Analytics exports increased 38% in 30 days", "Requested predictive dashboard capability", "Budget window opens in Q4"],
    "CUST-002": ["Integration API usage reached 87% of plan", "Requested security review materials", "Renewal is due in 45 days"],
    "CUST-003": ["Added 240 active users this quarter", "Requested analytics benchmark data", "Capital committee meets in 21 days"],
    "CUST-004": ["Store count increased from 18 to 24", "Support contacts rose 22%", "Annual planning starts next month"],
    "CUST-005": ["Security adoption reached 94%", "Requested enablement for new administrators", "Training budget remains available"],
}

_REP_ASSIGNMENTS = {
    "Enterprise": ("Maya Patel", "enterprise expansion and analytics"),
    "Mid-Market": ("Jordan Kim", "mid-market adoption and integrations"),
    "SMB": ("Alex Rivera", "digital expansion"),
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _resolve_customer(query):
    if not query:
        return "CUST-001"
    q = query.upper().strip()
    return q if q in _CUSTOMER_OWNERSHIP else None


def _find_opportunities(customer_id):
    cust = _CUSTOMER_OWNERSHIP[customer_id]
    owned = set(cust["products"])
    opportunities = []
    for rule in _AFFINITY_RULES:
        if rule["if_owns"] in owned and rule["recommend"] not in owned:
            product = _PRODUCT_CATALOG[rule["recommend"]]
            opportunities.append({
                "product_id": rule["recommend"],
                "product_name": product["name"],
                "annual_price": product["annual_price"],
                "affinity_score": rule["affinity_score"],
                "success_rate": rule["success_rate"],
                "est_close_days": rule["avg_time_to_close_days"],
                "margin_pct": product["margin_pct"],
            })
    return sorted(opportunities, key=lambda x: x["affinity_score"], reverse=True)


def _calculate_revenue_impact(opportunities):
    total_arr = sum(o["annual_price"] for o in opportunities)
    weighted_arr = sum(o["annual_price"] * o["success_rate"] for o in opportunities)
    total_margin = sum(o["annual_price"] * o["margin_pct"] / 100 for o in opportunities)
    return total_arr, weighted_arr, total_margin


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class CrossSellingAgent(BasicAgent):
    """
    Cross-selling opportunity identification agent.

    Operations:
        opportunity_scan      - scan a customer for cross-sell opportunities
        product_affinity      - display product affinity rules and scores
        recommendation_engine - generate prioritized recommendations
        revenue_impact        - project revenue impact of cross-sell pipeline
        buying_signals        - surface real-time product and timing signals
        outreach_plan         - create tailored talking points and sequence
        growth_plan           - stage opportunities by conversion timeline
        account_assignments   - simulate rep assignment and Teams alignment
    """

    def __init__(self):
        self.name = "CrossSellingAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "opportunity_scan", "product_affinity",
                            "recommendation_engine", "revenue_impact",
                            "buying_signals", "outreach_plan",
                            "growth_plan", "account_assignments",
                        ],
                        "description": "The cross-selling operation to perform",
                    },
                    "customer_id": {
                        "type": "string",
                        "description": "Customer ID (e.g. 'CUST-001')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "opportunity_scan")
        cust_id = _resolve_customer(kwargs.get("customer_id", ""))
        dispatch = {
            "opportunity_scan": self._opportunity_scan,
            "product_affinity": self._product_affinity,
            "recommendation_engine": self._recommendation_engine,
            "revenue_impact": self._revenue_impact,
            "buying_signals": self._buying_signals,
            "outreach_plan": self._outreach_plan,
            "growth_plan": self._growth_plan,
            "account_assignments": self._account_assignments,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        if cust_id is None:
            return (
                f"**Error:** Unknown customer_id `{kwargs.get('customer_id')}`. "
                f"Available customer IDs: {', '.join(sorted(_CUSTOMER_OWNERSHIP))}."
            )
        return handler(cust_id)

    # ── opportunity_scan ───────────────────────────────────────
    def _opportunity_scan(self, cust_id):
        cust = _CUSTOMER_OWNERSHIP[cust_id]
        opps = _find_opportunities(cust_id)
        owned_names = [_PRODUCT_CATALOG[p]["name"] for p in cust["products"]]
        owned_list = "\n".join(f"- {n}" for n in owned_names)
        opp_rows = ""
        for o in opps:
            opp_rows += f"| {o['product_name']} | ${o['annual_price']:,}/yr | {o['affinity_score']:.0%} | {o['success_rate']:.0%} | {o['est_close_days']}d |\n"
        if not opp_rows:
            opp_rows = "| No opportunities identified | - | - | - | - |\n"
        return (
            f"**Cross-Sell Opportunity Scan: {cust['name']}**\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Segment | {cust['segment']} |\n"
            f"| Current ARR | ${cust['arr']:,} |\n"
            f"| Health Score | {cust['health_score']}/100 |\n"
            f"| Tenure | {cust['tenure_months']} months |\n"
            f"| Contact | {cust['contact']} |\n\n"
            f"**Current Products:**\n{owned_list}\n\n"
            f"**Opportunities Found ({len(opps)}):**\n\n"
            f"| Product | Price | Affinity | Success Rate | Est. Close |\n|---|---|---|---|---|\n"
            f"{opp_rows}\n\n"
            f"Source: [CRM + Product Database + Affinity Engine]\nAgents: CrossSellingAgent"
        )

    # ── product_affinity ───────────────────────────────────────
    def _product_affinity(self, cust_id):
        rule_rows = ""
        for r in _AFFINITY_RULES:
            source = _PRODUCT_CATALOG[r["if_owns"]]["name"]
            target = _PRODUCT_CATALOG[r["recommend"]]["name"]
            rule_rows += f"| {source} | {target} | {r['affinity_score']:.0%} | {r['success_rate']:.0%} | {r['avg_time_to_close_days']}d |\n"
        seg_rows = ""
        for seg, data in _CROSS_SELL_SUCCESS_RATES.items():
            seg_rows += f"| {seg} | {data['avg_success_rate']:.0%} | {data['avg_deal_cycle_days']}d | {data['avg_expansion_pct']}% |\n"
        return (
            f"**Product Affinity Matrix**\n\n"
            f"| If Customer Owns | Recommend | Affinity | Success Rate | Avg Close |\n|---|---|---|---|---|\n"
            f"{rule_rows}\n"
            f"**Segment Benchmarks:**\n\n"
            f"| Segment | Avg Success | Avg Cycle | Avg Expansion |\n|---|---|---|---|\n"
            f"{seg_rows}\n\n"
            f"Source: [Affinity Engine + Historical Data]\nAgents: CrossSellingAgent"
        )

    # ── recommendation_engine ──────────────────────────────────
    def _recommendation_engine(self, cust_id):
        cust = _CUSTOMER_OWNERSHIP[cust_id]
        opps = _find_opportunities(cust_id)
        if not opps:
            return f"**Recommendations: {cust['name']}**\n\nNo cross-sell opportunities identified. Customer owns most recommended products.\n\nSource: [Recommendation Engine]\nAgents: CrossSellingAgent"
        recs = ""
        for i, o in enumerate(opps, 1):
            weighted_value = o["annual_price"] * o["success_rate"]
            recs += (
                f"**{i}. {o['product_name']}** (${o['annual_price']:,}/yr)\n"
                f"   - Affinity Score: {o['affinity_score']:.0%}\n"
                f"   - Projected Win Rate: {o['success_rate']:.0%}\n"
                f"   - Weighted Value: ${weighted_value:,.0f}/yr\n"
                f"   - Est. Close: {o['est_close_days']} days\n\n"
            )
        total_arr, weighted_arr, _ = _calculate_revenue_impact(opps)
        return (
            f"**Prioritized Recommendations: {cust['name']}**\n\n"
            f"Health Score: {cust['health_score']}/100 | Segment: {cust['segment']}\n\n"
            f"{recs}"
            f"**Summary:**\n"
            f"- Total potential ARR: ${total_arr:,}\n"
            f"- Weighted pipeline: ${weighted_arr:,.0f}\n"
            f"- Recommendations: {len(opps)}\n\n"
            f"Source: [Recommendation Engine + CRM]\nAgents: CrossSellingAgent"
        )

    # ── revenue_impact ─────────────────────────────────────────
    def _revenue_impact(self, cust_id):
        all_opps = []
        portfolio_rows = ""
        for cid, cust in _CUSTOMER_OWNERSHIP.items():
            opps = _find_opportunities(cid)
            total_arr, weighted_arr, margin = _calculate_revenue_impact(opps)
            all_opps.extend(opps)
            portfolio_rows += f"| {cust['name']} | {cust['segment']} | ${cust['arr']:,} | {len(opps)} | ${total_arr:,} | ${weighted_arr:,.0f} |\n"
        grand_total_arr = sum(o["annual_price"] for o in all_opps)
        grand_weighted = sum(o["annual_price"] * o["success_rate"] for o in all_opps)
        grand_margin = sum(o["annual_price"] * o["margin_pct"] / 100 for o in all_opps)
        return (
            f"**Cross-Sell Revenue Impact Analysis**\n\n"
            f"| Customer | Segment | Current ARR | Opps | Potential ARR | Weighted |\n|---|---|---|---|---|---|\n"
            f"{portfolio_rows}\n"
            f"**Portfolio Totals:**\n\n"
            f"| Metric | Value |\n|---|---|\n"
            f"| Total Opportunities | {len(all_opps)} |\n"
            f"| Total Potential ARR | ${grand_total_arr:,} |\n"
            f"| Weighted Pipeline | ${grand_weighted:,.0f} |\n"
            f"| Projected Margin | ${grand_margin:,.0f} |\n\n"
            f"Source: [Revenue Analytics + CRM + Product Database]\nAgents: CrossSellingAgent"
        )

    def _buying_signals(self, cust_id):
        cust = _CUSTOMER_OWNERSHIP[cust_id]
        opps = _find_opportunities(cust_id)
        signals = "\n".join(f"- {signal}" for signal in _BUYING_SIGNALS[cust_id])
        top = opps[0] if opps else None
        return (
            f"**Buying Signals: {cust['name']}**\n\n{signals}\n\n"
            f"**Priority:** {'High' if cust['health_score'] >= 80 else 'Monitor'}\n"
            f"**Recommended Product:** {top['product_name'] if top else 'No uncovered product'}\n"
            f"**Confidence:** {top['affinity_score']:.0%}\n" if top else
            f"**Buying Signals: {cust['name']}**\n\n{signals}\n\nNo uncovered product.\n"
        ) + "\nSource: [Dynamics 365 CRM + Product Usage + Feature Requests]\nAgents: CrossSellingAgent"

    def _outreach_plan(self, cust_id):
        cust = _CUSTOMER_OWNERSHIP[cust_id]
        opps = _find_opportunities(cust_id)
        top = opps[0] if opps else None
        if not top:
            return f"**Outreach Plan: {cust['name']}**\n\nNo uncovered product to promote."
        return (
            f"**Tailored Outreach Plan: {cust['name']}**\n\n"
            f"**Contact:** {cust['contact']} | **Offer:** {top['product_name']}\n"
            f"**Talking points:**\n"
            f"- Your current adoption and peer benchmark indicate a {top['affinity_score']:.0%} product fit.\n"
            f"- The estimated annual investment is ${top['annual_price']:,}.\n"
            f"- {_BUYING_SIGNALS[cust_id][0]}.\n\n"
            f"**Sequence:** Day 0 personalized email; Day 3 value workshop; "
            f"Day 10 business-case review; Day {top['est_close_days']} decision target.\n\n"
            f"Source: [Dynamics 365 CRM + Microsoft Teams]\nAgents: CrossSellingAgent"
        )

    def _growth_plan(self, cust_id):
        rows = []
        for cid, cust in _CUSTOMER_OWNERSHIP.items():
            opps = _find_opportunities(cid)
            if not opps:
                continue
            top = opps[0]
            stage = "Quick Win" if top["est_close_days"] <= 21 else "Strategic"
            rows.append(
                f"| {cust['name']} | {top['product_name']} | {stage} | "
                f"{top['est_close_days']} days | ${top['annual_price']:,} |"
            )
        return (
            "**Expansion Growth Plan**\n\n"
            "| Account | Opportunity | Stage | Target | ARR |\n|---|---|---|---|---|\n"
            + "\n".join(rows)
            + "\n\nSource: [Dynamics 365 CRM + Conversion Model]\nAgents: CrossSellingAgent"
        )

    def _account_assignments(self, cust_id):
        rows = []
        for cid, cust in _CUSTOMER_OWNERSHIP.items():
            rep, expertise = _REP_ASSIGNMENTS[cust["segment"]]
            top = _find_opportunities(cid)
            rows.append(
                f"| {cust['name']} | {rep} | {expertise} | "
                f"{top[0]['product_name'] if top else 'Portfolio review'} | Prepared |"
            )
        return (
            "**Simulated Account Assignments**\n\n"
            "| Account | Rep | Expertise | Focus | Status |\n|---|---|---|---|---|\n"
            + "\n".join(rows)
            + "\n\nEmail templates, notifications, and a Teams alignment post are prepared "
              "but were not sent; no CRM assignments were changed.\n\n"
              "Source: [Dynamics 365 CRM + Microsoft Teams]\nAgents: CrossSellingAgent"
        )


if __name__ == "__main__":
    agent = CrossSellingAgent()
    for op in [
        "opportunity_scan", "product_affinity", "recommendation_engine",
        "revenue_impact", "buying_signals", "outreach_plan", "growth_plan",
        "account_assignments",
    ]:
        print("=" * 60)
        print(agent.perform(operation=op, customer_id="CUST-001"))
        print()
