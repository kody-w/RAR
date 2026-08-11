"""
License Renewal and Expansion Agent for Software/Digital Products.

Manages SaaS license renewal pipelines, identifies expansion opportunities,
assesses churn risk, and projects revenue impact across the customer portfolio.

Version 1.1.0 adds deterministic, evidence-derived account-health,
competitive-strategy, proposal, and activation operations. The four original
operations and the agent's package/runtime identity remain unchanged.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/license_renewal_expansion",
    "version": "1.1.0",
    "display_name": "License Renewal & Expansion Agent",
    "description": "Manages SaaS license renewal pipelines, expansion opportunities, churn risk analysis, and revenue impact projections.",
    "author": "AIBAST",
    "tags": ["license", "renewal", "expansion", "churn", "revenue", "saas"],
    "category": "software_digital_products",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ---------------------------------------------------------------------------
# Synthetic domain data
# ---------------------------------------------------------------------------

LICENSE_AGREEMENTS = {
    "LIC-3001": {
        "customer": "Pinnacle Insurance Corp",
        "plan": "Enterprise",
        "arr": 288000,
        "seats": 150,
        "seats_used": 142,
        "renewal_date": "2026-04-30",
        "contract_start": "2025-04-30",
        "usage_trend": "increasing",
        "nps_score": 72,
        "support_tickets_90d": 4,
        "expansion_signals": ["API usage +45% QoQ", "Requested SSO for 3 subsidiaries"],
        "churn_signals": [],
        "csm": "Dana Reeves",
        "health_score": 88,
    },
    "LIC-3002": {
        "customer": "ClearView Analytics",
        "plan": "Professional",
        "arr": 72000,
        "seats": 30,
        "seats_used": 18,
        "renewal_date": "2026-05-15",
        "contract_start": "2025-05-15",
        "usage_trend": "declining",
        "nps_score": 34,
        "support_tickets_90d": 18,
        "expansion_signals": [],
        "churn_signals": ["Usage down 32%", "Executive sponsor departed", "Competitor eval detected"],
        "csm": "James Okafor",
        "health_score": 29,
    },
    "LIC-3003": {
        "customer": "Redwood Supply Chain",
        "plan": "Enterprise",
        "arr": 192000,
        "seats": 80,
        "seats_used": 79,
        "renewal_date": "2026-06-01",
        "contract_start": "2025-06-01",
        "usage_trend": "stable",
        "nps_score": 65,
        "support_tickets_90d": 7,
        "expansion_signals": ["Inquired about analytics add-on"],
        "churn_signals": ["Budget freeze mentioned in QBR"],
        "csm": "Dana Reeves",
        "health_score": 62,
    },
    "LIC-3004": {
        "customer": "Skyline Hospitality Group",
        "plan": "Enterprise",
        "arr": 360000,
        "seats": 250,
        "seats_used": 248,
        "renewal_date": "2026-04-15",
        "contract_start": "2025-04-15",
        "usage_trend": "increasing",
        "nps_score": 85,
        "support_tickets_90d": 2,
        "expansion_signals": ["Opening 12 new locations", "Requested bulk seat pricing", "Custom integration POC"],
        "churn_signals": [],
        "csm": "James Okafor",
        "health_score": 94,
    },
    "LIC-3005": {
        "customer": "Granite Construction Co",
        "plan": "Professional",
        "arr": 54000,
        "seats": 20,
        "seats_used": 12,
        "renewal_date": "2026-07-01",
        "contract_start": "2025-07-01",
        "usage_trend": "declining",
        "nps_score": 41,
        "support_tickets_90d": 11,
        "expansion_signals": [],
        "churn_signals": ["Primary admin inactive 45 days", "Missed last 2 QBRs"],
        "csm": "Dana Reeves",
        "health_score": 35,
    },
}

EXPANSION_PRICING = {
    "additional_seats": {"unit_price": 120, "min_qty": 10},
    "analytics_addon": {"price": 24000, "description": "Advanced analytics module"},
    "api_premium": {"price": 18000, "description": "Premium API tier with higher rate limits"},
    "sso_subsidiary": {"price": 12000, "description": "SSO extension per subsidiary"},
    "custom_integration": {"price": 36000, "description": "Custom integration package"},
}

RENEWAL_STRATEGIES = {
    "LIC-3001": {
        "competitor": "AtlasCloud",
        "competitor_discount": "18%",
        "switching_cost": 132000,
        "differentiators": ["45% QoQ API growth", "proven SSO integrations", "zero migration downtime"],
        "package": "Enterprise multi-year plus three subsidiary SSO extensions",
        "term": "36 months",
        "annual_value": 324000,
        "concession": "8% year-one expansion discount",
        "roi": "2.5x versus migration and retraining costs",
        "negotiation_levers": ["phased SSO rollout", "price protection", "executive success review"],
        "approvals": ["Sales VP", "Finance", "Legal"],
    },
    "LIC-3002": {
        "competitor": "NovaMetrics",
        "competitor_discount": "22%",
        "switching_cost": 58000,
        "differentiators": ["existing analytics workflows", "retained historical data", "named CSM recovery plan"],
        "package": "Professional renewal with adoption recovery services",
        "term": "12 months",
        "annual_value": 72000,
        "concession": "services credit after 80% adoption",
        "roi": "1.8x versus replacement and migration costs",
        "negotiation_levers": ["90-day adoption milestone", "executive sponsor reset", "quarterly value review"],
        "approvals": ["Sales Director", "Customer Success VP"],
    },
    "LIC-3003": {
        "competitor": "ChainSight",
        "competitor_discount": "12%",
        "switching_cost": 87000,
        "differentiators": ["79 of 80 active seats", "embedded supply-chain workflows", "analytics add-on readiness"],
        "package": "Enterprise renewal with advanced analytics",
        "term": "24 months",
        "annual_value": 216000,
        "concession": "analytics implementation included",
        "roi": "2.2x from avoided migration and faster analytics",
        "negotiation_levers": ["two-year price lock", "analytics pilot", "usage-based expansion review"],
        "approvals": ["Sales VP", "Finance"],
    },
    "LIC-3004": {
        "competitor": "GuestOps",
        "competitor_discount": "15%",
        "switching_cost": 164000,
        "differentiators": ["99% seat utilization", "12-location expansion", "custom integration proof of concept"],
        "package": "Enterprise expansion for 12 new locations with custom integration",
        "term": "36 months",
        "annual_value": 402000,
        "concession": "bulk-seat price protection",
        "roi": "2.9x from rollout speed and avoided re-platforming",
        "negotiation_levers": ["location ramp schedule", "integration milestone", "multi-year price protection"],
        "approvals": ["Sales VP", "Finance", "Solutions Engineering"],
    },
    "LIC-3005": {
        "competitor": "BuildFlow",
        "competitor_discount": "20%",
        "switching_cost": 41000,
        "differentiators": ["existing project history", "configured workflows", "re-engagement playbook"],
        "package": "Professional renewal with guided reactivation",
        "term": "12 months",
        "annual_value": 54000,
        "concession": "60-day adoption services credit",
        "roi": "1.6x versus replacement and retraining costs",
        "negotiation_levers": ["admin reactivation", "usage milestone", "monthly CSM review"],
        "approvals": ["Sales Director", "Customer Success VP"],
    },
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _exact_license(license_id):
    if not license_id:
        return None, "Provide an exact license_id: " + ", ".join(sorted(LICENSE_AGREEMENTS))
    if license_id not in LICENSE_AGREEMENTS:
        return None, f"Unknown license_id `{license_id}`; exact ID required."
    return LICENSE_AGREEMENTS[license_id], None

def _renewal_pipeline():
    pipeline = []
    for lid, lic in LICENSE_AGREEMENTS.items():
        risk = "low" if lic["health_score"] >= 70 else ("medium" if lic["health_score"] >= 50 else "high")
        pipeline.append({
            "id": lid, "customer": lic["customer"], "arr": lic["arr"],
            "renewal_date": lic["renewal_date"], "health_score": lic["health_score"],
            "risk": risk, "csm": lic["csm"],
        })
    pipeline.sort(key=lambda x: x["renewal_date"])
    total_arr = sum(p["arr"] for p in pipeline)
    at_risk_arr = sum(p["arr"] for p in pipeline if p["risk"] == "high")
    return {"pipeline": pipeline, "total_arr": total_arr, "at_risk_arr": at_risk_arr}


def _expansion_opportunities():
    opps = []
    for lid, lic in LICENSE_AGREEMENTS.items():
        if not lic["expansion_signals"]:
            continue
        potential = 0
        items = []
        seat_util = round(lic["seats_used"] / lic["seats"] * 100, 1)
        if seat_util > 90:
            seat_rev = EXPANSION_PRICING["additional_seats"]["unit_price"] * 50
            potential += seat_rev
            items.append({"type": "additional_seats", "value": seat_rev})
        for signal in lic["expansion_signals"]:
            if "analytics" in signal.lower():
                potential += EXPANSION_PRICING["analytics_addon"]["price"]
                items.append({"type": "analytics_addon", "value": EXPANSION_PRICING["analytics_addon"]["price"]})
            if "sso" in signal.lower():
                val = EXPANSION_PRICING["sso_subsidiary"]["price"] * 3
                potential += val
                items.append({"type": "sso_subsidiary", "value": val})
            if "integration" in signal.lower():
                potential += EXPANSION_PRICING["custom_integration"]["price"]
                items.append({"type": "custom_integration", "value": EXPANSION_PRICING["custom_integration"]["price"]})
        opps.append({
            "id": lid, "customer": lic["customer"], "current_arr": lic["arr"],
            "expansion_potential": potential, "items": items, "signals": lic["expansion_signals"],
        })
    opps.sort(key=lambda x: x["expansion_potential"], reverse=True)
    return {"opportunities": opps, "total_potential": sum(o["expansion_potential"] for o in opps)}


def _churn_risk():
    risks = []
    for lid, lic in LICENSE_AGREEMENTS.items():
        if not lic["churn_signals"]:
            continue
        seat_util = round(lic["seats_used"] / lic["seats"] * 100, 1)
        risks.append({
            "id": lid, "customer": lic["customer"], "arr": lic["arr"],
            "health_score": lic["health_score"], "nps": lic["nps_score"],
            "seat_utilization": seat_util, "usage_trend": lic["usage_trend"],
            "signals": lic["churn_signals"], "tickets_90d": lic["support_tickets_90d"],
        })
    risks.sort(key=lambda x: x["health_score"])
    return {"at_risk": risks, "total_arr_at_risk": sum(r["arr"] for r in risks)}


def _revenue_impact():
    renewal = _renewal_pipeline()
    expansion = _expansion_opportunities()
    churn = _churn_risk()
    base_renewal = renewal["total_arr"]
    expansion_val = expansion["total_potential"]
    churn_val = churn["total_arr_at_risk"]
    best_case = base_renewal + expansion_val
    worst_case = base_renewal - churn_val
    expected = base_renewal + round(expansion_val * 0.4) - round(churn_val * 0.3)
    return {
        "base_renewal_arr": base_renewal, "expansion_potential": expansion_val,
        "churn_risk_arr": churn_val, "best_case": best_case,
        "worst_case": worst_case, "expected": expected,
    }


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

class LicenseRenewalExpansionAgent(BasicAgent):
    """License renewal pipeline and expansion opportunity agent."""

    def __init__(self):
        self.name = "LicenseRenewalExpansionAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "renewal_pipeline",
                            "expansion_opportunities",
                            "churn_risk",
                            "revenue_impact",
                            "account_health_analysis",
                            "competitive_strategy",
                            "renewal_proposal",
                            "activate_renewal_package",
                        ],
                        "description": "The license management operation to perform.",
                    },
                    "license_id": {
                        "type": "string",
                        "description": "Optional license ID to filter results.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "renewal_pipeline")
        if op == "renewal_pipeline":
            return self._renewal_pipeline()
        elif op == "expansion_opportunities":
            return self._expansion_opportunities()
        elif op == "churn_risk":
            return self._churn_risk()
        elif op == "revenue_impact":
            return self._revenue_impact()
        elif op == "account_health_analysis":
            return self._account_health_analysis(kwargs.get("license_id"))
        elif op == "competitive_strategy":
            return self._competitive_strategy(kwargs.get("license_id"))
        elif op == "renewal_proposal":
            return self._renewal_proposal(kwargs.get("license_id"))
        elif op == "activate_renewal_package":
            return self._activate_renewal_package(kwargs.get("license_id"))
        return f"**Error:** Unknown operation `{op}`."

    def _renewal_pipeline(self) -> str:
        data = _renewal_pipeline()
        lines = [
            "# Renewal Pipeline",
            "",
            f"**Total Renewal ARR:** ${data['total_arr']:,}",
            f"**At-Risk ARR:** ${data['at_risk_arr']:,}",
            "",
            "| Customer | ARR | Renewal Date | Health | Risk | CSM |",
            "|----------|-----|-------------|--------|------|-----|",
        ]
        for p in data["pipeline"]:
            lines.append(
                f"| {p['customer']} | ${p['arr']:,} | {p['renewal_date']} "
                f"| {p['health_score']} | {p['risk'].upper()} | {p['csm']} |"
            )
        return "\n".join(lines)

    def _expansion_opportunities(self) -> str:
        data = _expansion_opportunities()
        lines = [
            "# Expansion Opportunities",
            "",
            f"**Total Expansion Potential:** ${data['total_potential']:,}",
            "",
        ]
        for opp in data["opportunities"]:
            lines.append(f"## {opp['customer']} (Current ARR: ${opp['current_arr']:,})")
            lines.append(f"**Expansion Potential:** ${opp['expansion_potential']:,}")
            lines.append("")
            lines.append("**Signals:**")
            for s in opp["signals"]:
                lines.append(f"- {s}")
            lines.append("")
            lines.append("| Expansion Item | Value |")
            lines.append("|---------------|-------|")
            for item in opp["items"]:
                lines.append(f"| {item['type'].replace('_', ' ').title()} | ${item['value']:,} |")
            lines.append("")
        return "\n".join(lines)

    def _churn_risk(self) -> str:
        data = _churn_risk()
        lines = [
            "# Churn Risk Assessment",
            "",
            f"**Total ARR at Risk:** ${data['total_arr_at_risk']:,}",
            "",
        ]
        for r in data["at_risk"]:
            lines.append(f"## {r['customer']} (ARR: ${r['arr']:,})")
            lines.append(f"- Health Score: {r['health_score']}")
            lines.append(f"- NPS: {r['nps']}")
            lines.append(f"- Seat Utilization: {r['seat_utilization']}%")
            lines.append(f"- Usage Trend: {r['usage_trend']}")
            lines.append(f"- Support Tickets (90d): {r['tickets_90d']}")
            lines.append("")
            lines.append("**Churn Signals:**")
            for s in r["signals"]:
                lines.append(f"- {s}")
            lines.append("")
        return "\n".join(lines)

    def _revenue_impact(self) -> str:
        data = _revenue_impact()
        lines = [
            "# Revenue Impact Projection",
            "",
            f"**Base Renewal ARR:** ${data['base_renewal_arr']:,}",
            f"**Expansion Potential:** ${data['expansion_potential']:,}",
            f"**Churn Risk ARR:** ${data['churn_risk_arr']:,}",
            "",
            "## Scenarios",
            "",
            "| Scenario | Projected ARR |",
            "|----------|--------------|",
            f"| Best Case (full expansion, no churn) | ${data['best_case']:,} |",
            f"| Expected (40% expansion, 30% churn) | ${data['expected']:,} |",
            f"| Worst Case (no expansion, full churn) | ${data['worst_case']:,} |",
            "",
            "## Recommendations",
            "- Prioritize executive engagement for high-churn-risk accounts.",
            "- Fast-track expansion proposals for Skyline Hospitality and Pinnacle Insurance.",
            "- Assign dedicated CSM resources to ClearView Analytics and Granite Construction.",
        ]
        return "\n".join(lines)

    def _account_health_analysis(self, license_id) -> str:
        lic, error = _exact_license(license_id)
        if error:
            return f"**Error:** {error}"
        strategy = RENEWAL_STRATEGIES[license_id]
        utilization = round(lic["seats_used"] / lic["seats"] * 100, 1)
        lines = [
            f"# Account Health Analysis — {lic['customer']}",
            "",
            f"**License ID:** {license_id}",
            f"**Health Score:** {lic['health_score']}/100",
            f"**Feature Adoption:** {utilization}% seat utilization",
            f"**Usage Trend:** {lic['usage_trend']}",
            f"**Support Tickets (90d):** {lic['support_tickets_90d']}",
            f"**Renewal ARR:** ${lic['arr']:,}",
            "",
            "## Expansion Signals",
        ]
        if lic["expansion_signals"]:
            lines.extend(f"- {signal}" for signal in lic["expansion_signals"])
        else:
            lines.append("- None")
        lines.extend(["", "## Competitive Context", f"- Competitor: {strategy['competitor']}"])
        lines.extend(f"- {item}" for item in strategy["differentiators"])
        return "\n".join(lines)

    def _competitive_strategy(self, license_id) -> str:
        lic, error = _exact_license(license_id)
        if error:
            return f"**Error:** {error}"
        strategy = RENEWAL_STRATEGIES[license_id]
        lines = [
            f"# Competitive Counter-Strategy — {lic['customer']}",
            "",
            f"**License ID:** {license_id}",
            f"**Competing Offer:** {strategy['competitor']} at a {strategy['competitor_discount']} discount",
            f"**True Switching Cost:** ${strategy['switching_cost']:,}",
            f"**Value Defense:** {strategy['roi']}",
            "",
            "## Differentiated Value",
        ]
        lines.extend(f"- {item}" for item in strategy["differentiators"])
        lines.extend(["", "## Counter-Strategy", f"- Lead with quantified switching cost of ${strategy['switching_cost']:,}."])
        lines.extend(f"- {lever}" for lever in strategy["negotiation_levers"])
        return "\n".join(lines)

    def _renewal_proposal(self, license_id) -> str:
        lic, error = _exact_license(license_id)
        if error:
            return f"**Error:** {error}"
        strategy = RENEWAL_STRATEGIES[license_id]
        return "\n".join([
            f"# Renewal and Expansion Proposal — {lic['customer']}",
            "",
            f"**License ID:** {license_id}",
            f"**Structured Offer:** {strategy['package']}",
            f"**Term:** {strategy['term']}",
            f"**Annual Contract Value:** ${strategy['annual_value']:,}",
            f"**Pre-Approved Concession:** {strategy['concession']}",
            f"**ROI Positioning:** {strategy['roi']}",
            f"**Dynamics Proposal Receipt:** sim-d365-proposal-{license_id.lower()}",
        ])

    def _activate_renewal_package(self, license_id) -> str:
        lic, error = _exact_license(license_id)
        if error:
            return f"**Error:** {error}"
        strategy = RENEWAL_STRATEGIES[license_id]
        lines = [
            f"# Customer-Ready Renewal Package — {lic['customer']}",
            "",
            f"**License ID:** {license_id}",
            f"**Presentation:** renewal-expansion-{license_id.lower()}.pptx",
            f"**Narrative:** Protect current value, quantify ${strategy['switching_cost']:,} in switching cost, and expand through {strategy['package'].lower()}.",
            "",
            "## Meeting Talking Points",
            f"- Account health is {lic['health_score']}/100 with {lic['seats_used']} of {lic['seats']} seats active.",
            f"- The offer delivers {strategy['roi']}.",
            f"- Counter {strategy['competitor']}'s {strategy['competitor_discount']} discount with differentiated value and price protection.",
            "",
            "## Negotiation Levers",
        ]
        lines.extend(f"- {lever}" for lever in strategy["negotiation_levers"])
        lines.extend(["", "## Pre-Staged Approvals"])
        lines.extend(f"- {approval}: ready for review" for approval in strategy["approvals"])
        lines.extend([
            "",
            f"**Approval Receipt:** sim-approval-{license_id.lower()}",
            f"**Microsoft Teams Package Receipt:** sim-teams-renewal-{license_id.lower()}",
            "**External Writes:** simulated; no live Dynamics 365, approval, or Teams mutation performed.",
        ])
        return "\n".join(lines)


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    agent = LicenseRenewalExpansionAgent()
    for op in ["renewal_pipeline", "expansion_opportunities", "churn_risk", "revenue_impact"]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
