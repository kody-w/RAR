"""
Supplier Risk Monitoring Agent

Monitors supplier health across quality, delivery, financial stability,
and geopolitical dimensions. Produces risk scorecards, disruption alerts,
and alternative-sourcing recommendations to protect supply continuity.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/supplier_risk_monitoring",
    "version": "1.1.0",
    "display_name": "Supplier Risk Monitoring Agent",
    "description": "Monitors supplier risk across quality, delivery, financial, and geopolitical dimensions with scorecards, disruption alerts, and alternative-sourcing plans.",
    "author": "AIBAST",
    "tags": ["supplier", "risk", "procurement", "supply-chain", "manufacturing"],
    "category": "manufacturing",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ---------------------------------------------------------------------------
# Synthetic domain data
# ---------------------------------------------------------------------------

SUPPLIERS = {
    "SUP-101": {
        "name": "TechnoCore Semiconductor (Taiwan)",
        "category": "Microcontrollers",
        "region": "Asia-Pacific",
        "country": "Taiwan",
        "annual_spend": 4800000,
        "quality_score": 82,
        "delivery_score": 74,
        "financial_score": 68,
        "geopolitical_score": 42,
        "overall_risk": 8.2,
        "tier": 1,
    },
    "SUP-102": {
        "name": "Shenzhen Electronics Co.",
        "category": "Passive Components",
        "region": "Asia-Pacific",
        "country": "China",
        "annual_spend": 3200000,
        "quality_score": 71,
        "delivery_score": 78,
        "financial_score": 55,
        "geopolitical_score": 58,
        "overall_risk": 6.5,
        "tier": 1,
    },
    "SUP-103": {
        "name": "Malaysia Semicon Pte Ltd",
        "category": "Power ICs",
        "region": "Asia-Pacific",
        "country": "Malaysia",
        "annual_spend": 2100000,
        "quality_score": 91,
        "delivery_score": 88,
        "financial_score": 84,
        "geopolitical_score": 82,
        "overall_risk": 3.8,
        "tier": 1,
    },
    "SUP-104": {
        "name": "Midwest Casting & Forge",
        "category": "Aluminum Castings",
        "region": "North America",
        "country": "USA",
        "annual_spend": 5600000,
        "quality_score": 88,
        "delivery_score": 65,
        "financial_score": 72,
        "geopolitical_score": 95,
        "overall_risk": 4.9,
        "tier": 1,
    },
    "SUP-105": {
        "name": "Rheinmetall Precision GmbH",
        "category": "CNC Machined Parts",
        "region": "Europe",
        "country": "Germany",
        "annual_spend": 3800000,
        "quality_score": 95,
        "delivery_score": 91,
        "financial_score": 89,
        "geopolitical_score": 88,
        "overall_risk": 2.4,
        "tier": 2,
    },
}

RECENT_INCIDENTS = [
    {"supplier_id": "SUP-101", "date": "2026-02-28", "severity": "HIGH",
     "description": "Cross-strait military exercises caused 5-day port closure; delayed 3 shipments"},
    {"supplier_id": "SUP-102", "date": "2026-03-05", "severity": "MEDIUM",
     "description": "Quality excursion: capacitor lot C-4410 failed incoming inspection (2.3% defect rate vs 0.5% spec)"},
    {"supplier_id": "SUP-104", "date": "2026-03-10", "severity": "HIGH",
     "description": "Equipment failure at foundry; force majeure declared, 7-day production halt"},
    {"supplier_id": "SUP-102", "date": "2026-03-12", "severity": "LOW",
     "description": "New export control regulations announced; compliance review underway"},
]

BACKUP_SUPPLIERS = {
    "SUP-101": [
        {"name": "Samsung Foundry (Korea)", "lead_time_weeks": 12, "qual_status": "In Progress", "est_cost_premium_pct": 8},
        {"name": "GlobalFoundries (USA)", "lead_time_weeks": 16, "qual_status": "Not Started", "est_cost_premium_pct": 15},
    ],
    "SUP-102": [
        {"name": "Murata Electronics (Japan)", "lead_time_weeks": 6, "qual_status": "Qualified", "est_cost_premium_pct": 5},
        {"name": "Vishay Intertechnology (USA)", "lead_time_weeks": 4, "qual_status": "Qualified", "est_cost_premium_pct": 12},
    ],
    "SUP-104": [
        {"name": "Alcoa Precision Castings (USA)", "lead_time_weeks": 8, "qual_status": "In Progress", "est_cost_premium_pct": 6},
    ],
}

SUPPLY_RISK_PLANS = {
    "SUP-101": {
        "financial_trend": "credit outlook negative; days payable outstanding +11",
        "operational_capacity_pct": 72, "logistics_reliability_pct": 68,
        "safety_stock_days": 35, "dual_source": "Samsung Foundry (Korea)",
        "mitigation_investment": 384000, "modeled_disruption_loss": 2150000,
        "owner": "Electronics Category Manager", "next_review": "2026-03-19",
    },
    "SUP-102": {
        "financial_trend": "stable; margin pressure from export controls",
        "operational_capacity_pct": 81, "logistics_reliability_pct": 76,
        "safety_stock_days": 21, "dual_source": "Murata Electronics (Japan)",
        "mitigation_investment": 160000, "modeled_disruption_loss": 980000,
        "owner": "Components Sourcing Lead", "next_review": "2026-03-22",
    },
    "SUP-104": {
        "financial_trend": "stable; repair cash requirement elevated",
        "operational_capacity_pct": 54, "logistics_reliability_pct": 71,
        "safety_stock_days": 28, "dual_source": "Alcoa Precision Castings (USA)",
        "mitigation_investment": 336000, "modeled_disruption_loss": 1740000,
        "owner": "Metals Category Manager", "next_review": "2026-03-18",
    },
}

EVIDENCE_MARKER = (
    "[Evidence: supply-risk-monitoring one-pager and demo transcript; "
    "risk-driver intelligence, mitigation, financial exposure, execution, and continuous alerts]"
)


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _composite_score(supplier):
    """Weighted composite health score (0-100, higher = healthier)."""
    return round(
        supplier["quality_score"] * 0.30
        + supplier["delivery_score"] * 0.25
        + supplier["financial_score"] * 0.25
        + supplier["geopolitical_score"] * 0.20,
        1,
    )


def _risk_tier_label(overall_risk):
    """Convert numeric risk to a label."""
    if overall_risk >= 7.0:
        return "CRITICAL"
    elif overall_risk >= 5.0:
        return "HIGH"
    elif overall_risk >= 3.0:
        return "MODERATE"
    return "LOW"


def _total_spend():
    """Total annual spend across all suppliers."""
    return sum(s["annual_spend"] for s in SUPPLIERS.values())


def _spend_at_risk(threshold=5.0):
    """Annual spend with suppliers above the given risk threshold."""
    return sum(s["annual_spend"] for s in SUPPLIERS.values() if s["overall_risk"] >= threshold)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class SupplierRiskMonitoringAgent(BasicAgent):
    """Monitors supplier risk and generates mitigation plans."""

    def __init__(self):
        self.name = "SupplierRiskMonitoringAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "operations": [
                "risk_dashboard",
                "supplier_scorecard",
                "disruption_alerts",
                "alternative_sourcing",
                "risk_driver_analysis",
                "mitigation_plan",
                "financial_exposure",
                "execution_timeline",
                "monitoring_plan",
            ],
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "risk_dashboard")
        dispatch = {
            "risk_dashboard": self._risk_dashboard,
            "supplier_scorecard": self._supplier_scorecard,
            "disruption_alerts": self._disruption_alerts,
            "alternative_sourcing": self._alternative_sourcing,
            "risk_driver_analysis": self._risk_driver_analysis,
            "mitigation_plan": self._mitigation_plan,
            "financial_exposure": self._financial_exposure,
            "execution_timeline": self._execution_timeline,
            "monitoring_plan": self._monitoring_plan,
        }
        handler = dispatch.get(operation)
        if handler is None:
            return f"**Error:** Unknown operation `{operation}`. Valid: {', '.join(dispatch.keys())}"
        return handler(**kwargs)

    # ------------------------------------------------------------------
    def _risk_dashboard(self, **kwargs) -> str:
        lines = ["## Supplier Risk Dashboard\n"]
        total = _total_spend()
        at_risk = _spend_at_risk(5.0)
        lines.append(f"**Total annual supplier spend:** ${total:,.0f}")
        lines.append(f"**Spend at elevated risk (score >= 5.0):** ${at_risk:,.0f} ({round(at_risk/total*100,1)}%)\n")

        lines.append("| Supplier | Category | Country | Spend | Risk Score | Risk Tier | Composite Health |")
        lines.append("|----------|----------|---------|-------|------------|-----------|------------------|")
        ranked = sorted(SUPPLIERS.values(), key=lambda s: s["overall_risk"], reverse=True)
        for s in ranked:
            tier = _risk_tier_label(s["overall_risk"])
            health = _composite_score(s)
            lines.append(
                f"| {s['name'][:32]} | {s['category']} | {s['country']} | "
                f"${s['annual_spend']:,.0f} | {s['overall_risk']} | **{tier}** | {health}/100 |"
            )

        lines.append(f"\n**Active incidents:** {len(RECENT_INCIDENTS)}")
        high_incidents = sum(1 for i in RECENT_INCIDENTS if i["severity"] == "HIGH")
        lines.append(f"**HIGH severity incidents:** {high_incidents}")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _supplier_scorecard(self, **kwargs) -> str:
        lines = ["## Supplier Scorecards\n"]
        for sid, s in SUPPLIERS.items():
            health = _composite_score(s)
            tier = _risk_tier_label(s["overall_risk"])
            lines.append(f"### {s['name']} ({sid})")
            lines.append(f"- **Category:** {s['category']}")
            lines.append(f"- **Region:** {s['region']} ({s['country']})")
            lines.append(f"- **Annual spend:** ${s['annual_spend']:,.0f}")
            lines.append(f"- **Tier:** {s['tier']}")
            lines.append(f"- **Overall risk:** {s['overall_risk']}/10 ({tier})")
            lines.append(f"- **Composite health:** {health}/100\n")
            lines.append("| Dimension | Score | Status |")
            lines.append("|-----------|-------|--------|")
            for dim in ["quality_score", "delivery_score", "financial_score", "geopolitical_score"]:
                val = s[dim]
                status = "Good" if val >= 80 else "Watch" if val >= 60 else "At Risk"
                label = dim.replace("_score", "").replace("_", " ").title()
                lines.append(f"| {label} | {val}/100 | {status} |")

            # Show incidents for this supplier
            incidents = [i for i in RECENT_INCIDENTS if i["supplier_id"] == sid]
            if incidents:
                lines.append(f"\n**Recent incidents ({len(incidents)}):**")
                for inc in incidents:
                    lines.append(f"- [{inc['severity']}] {inc['date']}: {inc['description']}")
            lines.append("")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _disruption_alerts(self, **kwargs) -> str:
        lines = ["## Active Disruption Alerts\n"]
        if not RECENT_INCIDENTS:
            lines.append("No active disruption alerts.")
            return "\n".join(lines)

        sorted_incidents = sorted(RECENT_INCIDENTS, key=lambda i: {"HIGH": 0, "MEDIUM": 1, "LOW": 2}.get(i["severity"], 3))
        lines.append("| Severity | Date | Supplier | Description |")
        lines.append("|----------|------|----------|-------------|")
        for inc in sorted_incidents:
            sname = SUPPLIERS.get(inc["supplier_id"], {}).get("name", inc["supplier_id"])
            lines.append(f"| **{inc['severity']}** | {inc['date']} | {sname[:28]} | {inc['description']} |")

        lines.append("\n### Impact Assessment\n")
        for inc in sorted_incidents:
            if inc["severity"] != "HIGH":
                continue
            s = SUPPLIERS.get(inc["supplier_id"], {})
            lines.append(f"**{s.get('name', inc['supplier_id'])}**")
            lines.append(f"- Annual spend exposed: ${s.get('annual_spend', 0):,.0f}")
            lines.append(f"- Category: {s.get('category', 'N/A')}")
            has_backup = inc["supplier_id"] in BACKUP_SUPPLIERS
            lines.append(f"- Backup suppliers available: {'Yes' if has_backup else 'No'}")
            lines.append("")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _alternative_sourcing(self, **kwargs) -> str:
        lines = ["## Alternative Sourcing Plan\n"]
        if not BACKUP_SUPPLIERS:
            lines.append("No alternative suppliers have been identified.")
            return "\n".join(lines)

        for sid, backups in BACKUP_SUPPLIERS.items():
            s = SUPPLIERS.get(sid, {})
            lines.append(f"### Alternatives for {s.get('name', sid)} ({s.get('category', 'N/A')})")
            lines.append(f"- **Current spend:** ${s.get('annual_spend', 0):,.0f}")
            lines.append(f"- **Current risk:** {s.get('overall_risk', 'N/A')}/10\n")
            lines.append("| Alternative Supplier | Lead Time | Qual Status | Cost Premium |")
            lines.append("|---------------------|-----------|-------------|--------------|")
            for b in backups:
                lines.append(
                    f"| {b['name']} | {b['lead_time_weeks']} weeks | {b['qual_status']} | +{b['est_cost_premium_pct']}% |"
                )

            # Recommendation
            qualified = [b for b in backups if b["qual_status"] == "Qualified"]
            if qualified:
                best = min(qualified, key=lambda b: b["est_cost_premium_pct"])
                lines.append(f"\n**Recommendation:** Activate {best['name']} immediately "
                             f"(qualified, +{best['est_cost_premium_pct']}% premium, {best['lead_time_weeks']}-week lead)")
            else:
                fastest = min(backups, key=lambda b: b["lead_time_weeks"])
                lines.append(f"\n**Recommendation:** Accelerate qualification of {fastest['name']} "
                             f"({fastest['lead_time_weeks']}-week lead, currently {fastest['qual_status']})")
            lines.append("")

        total_premium = 0
        for sid, backups in BACKUP_SUPPLIERS.items():
            s = SUPPLIERS.get(sid, {})
            best_prem = min(b["est_cost_premium_pct"] for b in backups)
            total_premium += s.get("annual_spend", 0) * best_prem / 100
        lines.append(f"**Estimated annual cost of full diversification:** ${total_premium:,.0f}")
        lines.append(f"**Risk reduction value:** ${_spend_at_risk(5.0):,.0f} of spend de-risked")
        return "\n".join(lines)

    def _risk_plan(self, **kwargs):
        supplier_id = str(kwargs.get("supplier_id", "SUP-101")).strip().upper()
        plan = SUPPLY_RISK_PLANS.get(supplier_id)
        if plan is None:
            valid = ", ".join(SUPPLY_RISK_PLANS)
            return supplier_id, None, f"**Error:** Unknown supplier `{supplier_id}`. Valid: {valid}"
        return supplier_id, plan, ""

    def _risk_driver_analysis(self, **kwargs) -> str:
        supplier_id, plan, error = self._risk_plan(**kwargs)
        if error:
            return error
        supplier = SUPPLIERS[supplier_id]
        return "\n".join([
            "## Supply Risk Driver Analysis",
            EVIDENCE_MARKER,
            f"**Supplier lookup:** {supplier_id} — {supplier['name']}",
            f"- Region/category: {supplier['region']} / {supplier['category']}",
            f"- Financial trend: {plan['financial_trend']}",
            f"- Operational capacity: {plan['operational_capacity_pct']}%",
            f"- Logistics reliability: {plan['logistics_reliability_pct']}%",
            f"- Quality score: {supplier['quality_score']}/100",
            f"- Overall risk: {supplier['overall_risk']}/10 ({_risk_tier_label(supplier['overall_risk'])})",
        ])

    def _mitigation_plan(self, **kwargs) -> str:
        supplier_id, plan, error = self._risk_plan(**kwargs)
        if error:
            return error
        return "\n".join([
            "## Targeted Supply Risk Mitigation",
            EVIDENCE_MARKER,
            f"**Supplier lookup:** {supplier_id} — {SUPPLIERS[supplier_id]['name']}",
            "1. **Immediate:** Escalate active incidents and verify open shipment ETAs.",
            f"2. **Containment:** Raise safety stock to {plan['safety_stock_days']} days.",
            f"3. **Diversification:** Qualify/activate {plan['dual_source']}.",
            "4. **Validation:** Run first-article, logistics-lane, and commercial reviews.",
            f"5. **Owner/review:** {plan['owner']} / {plan['next_review']}.",
        ])

    def _financial_exposure(self, **kwargs) -> str:
        supplier_id, plan, error = self._risk_plan(**kwargs)
        if error:
            return error
        investment = plan["mitigation_investment"]
        loss = plan["modeled_disruption_loss"]
        avoided = round(loss * 0.72)
        roi = round((avoided - investment) / investment * 100, 1)
        return "\n".join([
            "## Supply Risk Financial Exposure",
            EVIDENCE_MARKER,
            f"**Supplier lookup:** {supplier_id} — {SUPPLIERS[supplier_id]['category']}",
            f"- Annual spend exposed: ${SUPPLIERS[supplier_id]['annual_spend']:,.0f}",
            f"- Modeled disruption loss: ${loss:,.0f}",
            f"- Mitigation investment: ${investment:,.0f}",
            f"- Modeled loss avoided: ${avoided:,.0f}",
            f"- First-year mitigation ROI: {roi}%",
        ])

    def _execution_timeline(self, **kwargs) -> str:
        supplier_id, plan, error = self._risk_plan(**kwargs)
        if error:
            return error
        return "\n".join([
            "## Supply Risk Execution Timeline",
            EVIDENCE_MARKER,
            f"**Supplier lookup:** {supplier_id} — {SUPPLIERS[supplier_id]['name']}",
            "",
            "| Phase | Window | Action |",
            "|-------|--------|--------|",
            "| Immediate | 0-48 hours | Confirm shipments, incident owner, and safety-stock gap |",
            f"| Validate | Days 3-14 | Qualify {plan['dual_source']} and test logistics lane |",
            f"| Optimize | Days 15-45 | Hold {plan['safety_stock_days']} days stock and rebalance awards |",
            "",
            f"- **SIMULATED WRITE RECEIPT:** `RISK-SIM-{supplier_id}` for Teams stakeholder update",
            "- Simulation only; no sourcing award, purchase order, or Teams message was created.",
        ])

    def _monitoring_plan(self, **kwargs) -> str:
        supplier_id, plan, error = self._risk_plan(**kwargs)
        if error:
            return error
        return "\n".join([
            "## Continuous Supply Risk Monitoring",
            EVIDENCE_MARKER,
            f"**Supplier lookup:** {supplier_id} — {SUPPLIERS[supplier_id]['name']}",
            "",
            "| Signal | Cadence | Alert Threshold |",
            "|--------|---------|-----------------|",
            "| Financial health | Daily | Credit score falls 5 points |",
            f"| Operational capacity | Hourly | Below {plan['operational_capacity_pct']}% baseline by 10 points |",
            f"| Logistics reliability | Per shipment | Below {plan['logistics_reliability_pct']}% |",
            "| Quality | Per lot | Defect rate above 0.5% |",
            "| Geopolitical | Daily | Severity HIGH |",
            "",
            f"Next human review: **{plan['next_review']}**, owned by **{plan['owner']}**.",
        ])


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = SupplierRiskMonitoringAgent()
    for op in agent.metadata["operations"]:
        print("=" * 72)
        print(agent.perform(operation=op))
        print()
