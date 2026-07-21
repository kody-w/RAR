"""
Identify Discounts Agent

Scans for applicable discounts, checks eligibility criteria, calculates
savings, and manages approval workflows for discount programs.

Where a real deployment would connect to pricing engines and CRM, this
agent uses a synthetic data layer so it runs anywhere without credentials.

Version 1.1.0 adds evidence-backed procurement discount prioritization,
purchase-order drafting, bulk strategy, execution planning, and simulated
Teams tracking. Existing sales-discount operations remain unchanged.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/identify_discounts",
    "version": "1.1.1",
    "display_name": "Identify Discounts",
    "description": "Scans built-in demo pricing data for discounts, checks eligibility, calculates savings, and drafts purchase orders.",
    "author": "AIBAST",
    "tags": ["discounts", "pricing", "savings", "eligibility", "approval"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# SYNTHETIC DATA LAYER
# ═══════════════════════════════════════════════════════════════

_DISCOUNT_PROGRAMS = {
    "VOL-001": {"name": "Volume Discount", "type": "Volume", "description": "Tiered pricing based on license count", "max_discount_pct": 25, "stackable": False, "requires_approval": False, "auto_apply": True},
    "MULTI-001": {"name": "Multi-Year Commitment", "type": "Term", "description": "Discount for 2-3 year contract commitments", "max_discount_pct": 20, "stackable": True, "requires_approval": False, "auto_apply": True},
    "EDU-001": {"name": "Education Pricing", "type": "Segment", "description": "Special pricing for accredited educational institutions", "max_discount_pct": 40, "stackable": False, "requires_approval": True, "auto_apply": False},
    "NPO-001": {"name": "Non-Profit Discount", "type": "Segment", "description": "Reduced pricing for registered non-profit organizations", "max_discount_pct": 35, "stackable": False, "requires_approval": True, "auto_apply": False},
    "COMP-001": {"name": "Competitive Switch", "type": "Strategic", "description": "Discount for customers switching from competitor platforms", "max_discount_pct": 30, "stackable": True, "requires_approval": True, "auto_apply": False},
    "LOYAL-001": {"name": "Loyalty Renewal", "type": "Retention", "description": "Discount for customers renewing after 3+ years", "max_discount_pct": 15, "stackable": True, "requires_approval": False, "auto_apply": True},
    "BUNDLE-001": {"name": "Product Bundle", "type": "Bundle", "description": "Discount when purchasing 3+ products together", "max_discount_pct": 18, "stackable": True, "requires_approval": False, "auto_apply": True},
}

_ELIGIBILITY_CRITERIA = {
    "VOL-001": {"min_licenses": 50, "tiers": [
        {"min": 50, "max": 99, "discount_pct": 10},
        {"min": 100, "max": 249, "discount_pct": 15},
        {"min": 250, "max": 499, "discount_pct": 20},
        {"min": 500, "max": 99999, "discount_pct": 25},
    ]},
    "MULTI-001": {"min_term_years": 2, "tiers": [
        {"term_years": 2, "discount_pct": 10},
        {"term_years": 3, "discount_pct": 20},
    ]},
    "EDU-001": {"required_docs": ["Accreditation certificate", "Tax-exempt status letter"], "institution_types": ["University", "College", "K-12 School District"]},
    "NPO-001": {"required_docs": ["501(c)(3) determination letter", "Organization charter"], "org_types": ["Registered Non-Profit", "NGO", "Foundation"]},
    "COMP-001": {"competitors": ["Competitor A", "Competitor B", "Competitor C"], "proof_required": "Active subscription screenshot or invoice"},
    "LOYAL-001": {"min_tenure_years": 3, "min_health_score": 70, "no_outstanding_balance": True},
    "BUNDLE-001": {"min_products": 3, "eligible_products": ["Core Platform", "Enterprise Platform", "Analytics Standard", "Analytics Pro", "Integration Hub", "Security Suite"]},
}

_VOLUME_TIERS = [
    {"label": "Tier 1", "min_licenses": 50, "max_licenses": 99, "discount_pct": 10, "price_per_license": 90},
    {"label": "Tier 2", "min_licenses": 100, "max_licenses": 249, "discount_pct": 15, "price_per_license": 85},
    {"label": "Tier 3", "min_licenses": 250, "max_licenses": 499, "discount_pct": 20, "price_per_license": 80},
    {"label": "Tier 4", "min_licenses": 500, "max_licenses": 99999, "discount_pct": 25, "price_per_license": 75},
]

_APPROVAL_RULES = {
    "up_to_15_pct": {"approver": "Sales Manager", "sla_hours": 4, "auto_approve_if": "Deal size > $50K and health score > 80"},
    "15_to_25_pct": {"approver": "VP Sales", "sla_hours": 8, "auto_approve_if": None},
    "25_to_35_pct": {"approver": "CRO", "sla_hours": 24, "auto_approve_if": None},
    "above_35_pct": {"approver": "CEO", "sla_hours": 48, "auto_approve_if": None},
}

_SAMPLE_DEAL = {
    "customer": "Atlas Digital", "licenses": 175, "list_price_per_license": 100,
    "products": ["Enterprise Platform", "Analytics Pro", "Integration Hub", "Security Suite"],
    "term_years": 3, "is_competitive_switch": True, "competitor": "Competitor B",
    "tenure_years": 0, "health_score": 0, "is_edu": False, "is_npo": False,
}

_PLANNED_PURCHASES = [
    {"category": "Medical supplies", "vendor": "MedSource", "amount": 180000, "discount_pct": 12, "expires": "2025-12-15", "timing": "Buy by 2025-12-10"},
    {"category": "Imaging devices", "vendor": "Diagnostic Systems", "amount": 420000, "discount_pct": 8, "expires": "2025-11-30", "timing": "Act this week"},
    {"category": "Software licenses", "vendor": "CloudWorks", "amount": 96000, "discount_pct": 15, "expires": "2025-12-31", "timing": "Consolidate before renewal"},
]


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _check_eligibility(deal, program_id):
    criteria = _ELIGIBILITY_CRITERIA.get(program_id, {})
    program = _DISCOUNT_PROGRAMS[program_id]
    if program_id == "VOL-001":
        if deal["licenses"] >= criteria.get("min_licenses", 0):
            for tier in criteria["tiers"]:
                if tier["min"] <= deal["licenses"] <= tier["max"]:
                    return True, tier["discount_pct"]
        return False, 0
    elif program_id == "MULTI-001":
        if deal["term_years"] >= criteria.get("min_term_years", 99):
            for tier in criteria["tiers"]:
                if deal["term_years"] >= tier["term_years"]:
                    best = tier["discount_pct"]
            return True, best
        return False, 0
    elif program_id == "BUNDLE-001":
        eligible_count = sum(1 for p in deal["products"] if p in criteria.get("eligible_products", []))
        if eligible_count >= criteria.get("min_products", 99):
            return True, program["max_discount_pct"]
        return False, 0
    elif program_id == "COMP-001":
        if deal.get("is_competitive_switch"):
            return True, program["max_discount_pct"]
        return False, 0
    elif program_id == "LOYAL-001":
        if deal.get("tenure_years", 0) >= criteria.get("min_tenure_years", 99):
            return True, program["max_discount_pct"]
        return False, 0
    return False, 0


def _calculate_savings(deal, applicable_discounts):
    list_total = deal["licenses"] * deal["list_price_per_license"] * deal["term_years"] * 12
    best_discount = max((d[1] for d in applicable_discounts), default=0)
    savings = list_total * best_discount / 100
    final_price = list_total - savings
    return list_total, savings, final_price, best_discount


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class IdentifyDiscountsAgent(BasicAgent):
    """
    Discount identification and management agent.

    Operations:
        discount_scan      - scan available discounts for a deal
        eligibility_check  - check eligibility for specific programs
        savings_calculation - calculate total savings
        approval_workflow  - determine approval requirements
        purchase_savings   - prioritize vendor savings for planned purchases
        expiring_discounts - explain time-sensitive savings impact
        draft_purchase_order - prepare a discounted bundled PO
        bulk_order_strategy - model consolidated volume-tier savings
        execution_timeline - produce actionable procurement next steps
        setup_tracking     - simulate Teams tracking and reminders
    """

    def __init__(self):
        self.name = "IdentifyDiscountsAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "discount_scan", "eligibility_check",
                            "savings_calculation", "approval_workflow",
                            "purchase_savings", "expiring_discounts",
                            "draft_purchase_order", "bulk_order_strategy",
                            "execution_timeline", "setup_tracking",
                        ],
                        "description": "The discount operation to perform",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "discount_scan")
        dispatch = {
            "discount_scan": self._discount_scan,
            "eligibility_check": self._eligibility_check,
            "savings_calculation": self._savings_calculation,
            "approval_workflow": self._approval_workflow,
            "purchase_savings": self._purchase_savings,
            "expiring_discounts": self._expiring_discounts,
            "draft_purchase_order": self._draft_purchase_order,
            "bulk_order_strategy": self._bulk_order_strategy,
            "execution_timeline": self._execution_timeline,
            "setup_tracking": self._setup_tracking,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler()

    # ── discount_scan ──────────────────────────────────────────
    def _discount_scan(self):
        deal = _SAMPLE_DEAL
        rows = ""
        for pid, prog in _DISCOUNT_PROGRAMS.items():
            eligible, pct = _check_eligibility(deal, pid)
            status = f"Eligible ({pct}%)" if eligible else "Not Eligible"
            rows += f"| {pid} | {prog['name']} | {prog['type']} | {prog['max_discount_pct']}% | {status} | {'Yes' if prog['requires_approval'] else 'Auto'} |\n"
        return (
            f"**Discount Scan: {deal['customer']}**\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Licenses | {deal['licenses']} |\n"
            f"| Products | {len(deal['products'])} |\n"
            f"| Term | {deal['term_years']} years |\n"
            f"| Competitive Switch | {'Yes' if deal['is_competitive_switch'] else 'No'} |\n\n"
            f"**Available Programs:**\n\n"
            f"| ID | Program | Type | Max Discount | Status | Approval |\n|---|---|---|---|---|---|\n"
            f"{rows}\n\n"
            f"Source: [Pricing Engine + Discount Rules]\nAgents: IdentifyDiscountsAgent"
        )

    # ── eligibility_check ──────────────────────────────────────
    def _eligibility_check(self):
        deal = _SAMPLE_DEAL
        eligible_list = []
        for pid in _DISCOUNT_PROGRAMS:
            eligible, pct = _check_eligibility(deal, pid)
            if eligible:
                eligible_list.append((pid, pct))
        detail_rows = ""
        for pid, pct in eligible_list:
            prog = _DISCOUNT_PROGRAMS[pid]
            detail_rows += f"| {prog['name']} | {pct}% | {'Yes' if prog['stackable'] else 'No'} | {prog['description'][:50]} |\n"
        vol_rows = ""
        for tier in _VOLUME_TIERS:
            marker = " <-- Current" if tier["min_licenses"] <= deal["licenses"] <= tier["max_licenses"] else ""
            vol_rows += f"| {tier['label']} | {tier['min_licenses']}-{tier['max_licenses']} | {tier['discount_pct']}% | ${tier['price_per_license']}/license |{marker}\n"
        return (
            f"**Eligibility Check: {deal['customer']}**\n\n"
            f"**Eligible Programs ({len(eligible_list)}):**\n\n"
            f"| Program | Discount | Stackable | Description |\n|---|---|---|---|\n"
            f"{detail_rows}\n"
            f"**Volume Tier Placement:**\n\n"
            f"| Tier | Licenses | Discount | Price |\n|---|---|---|---|\n"
            f"{vol_rows}\n\n"
            f"Source: [Eligibility Engine]\nAgents: IdentifyDiscountsAgent"
        )

    # ── savings_calculation ────────────────────────────────────
    def _savings_calculation(self):
        deal = _SAMPLE_DEAL
        applicable = []
        for pid in _DISCOUNT_PROGRAMS:
            eligible, pct = _check_eligibility(deal, pid)
            if eligible:
                applicable.append((pid, pct))
        list_total, savings, final_price, best_pct = _calculate_savings(deal, applicable)
        return (
            f"**Savings Calculation: {deal['customer']}**\n\n"
            f"| Metric | Value |\n|---|---|\n"
            f"| List Price | ${deal['list_price_per_license']}/license/month |\n"
            f"| Licenses | {deal['licenses']} |\n"
            f"| Term | {deal['term_years']} years |\n"
            f"| List Total | ${list_total:,} |\n"
            f"| Best Discount | {best_pct}% |\n"
            f"| Total Savings | ${savings:,.0f} |\n"
            f"| **Final Price** | **${final_price:,.0f}** |\n\n"
            f"**Applicable Discounts:**\n"
            + "\n".join(f"- {_DISCOUNT_PROGRAMS[pid]['name']}: {pct}%" for pid, pct in applicable) + "\n\n"
            f"**Note:** Non-stackable discounts use highest single discount. Stackable discounts may be combined with approval.\n\n"
            f"Source: [Pricing Engine + Deal Calculator]\nAgents: IdentifyDiscountsAgent"
        )

    # ── approval_workflow ──────────────────────────────────────
    def _approval_workflow(self):
        deal = _SAMPLE_DEAL
        applicable = []
        for pid in _DISCOUNT_PROGRAMS:
            eligible, pct = _check_eligibility(deal, pid)
            if eligible:
                applicable.append((pid, pct))
        _, _, _, best_pct = _calculate_savings(deal, applicable)
        if best_pct <= 15:
            tier_key = "up_to_15_pct"
        elif best_pct <= 25:
            tier_key = "15_to_25_pct"
        elif best_pct <= 35:
            tier_key = "25_to_35_pct"
        else:
            tier_key = "above_35_pct"
        approval = _APPROVAL_RULES[tier_key]
        approval_rows = ""
        for key, rule in _APPROVAL_RULES.items():
            marker = " <-- Required" if key == tier_key else ""
            approval_rows += f"| {key.replace('_', ' ').title()} | {rule['approver']} | {rule['sla_hours']}h | {rule.get('auto_approve_if', 'Manual review')}{marker} |\n"
        needs_approval = any(_DISCOUNT_PROGRAMS[pid]["requires_approval"] for pid, _ in applicable)
        return (
            f"**Approval Workflow: {deal['customer']}**\n\n"
            f"**Discount Level:** {best_pct}% | **Required Approver:** {approval['approver']}\n\n"
            f"**Approval Matrix:**\n\n"
            f"| Discount Range | Approver | SLA | Auto-Approve Criteria |\n|---|---|---|---|\n"
            f"{approval_rows}\n"
            f"**Programs Requiring Manual Approval:** {'Yes' if needs_approval else 'None'}\n"
            f"**Estimated Approval Time:** {approval['sla_hours']} hours\n\n"
            f"Source: [Approval Engine + Deal Desk]\nAgents: IdentifyDiscountsAgent"
        )

    def _purchase_savings(self):
        ranked = sorted(
            _PLANNED_PURCHASES,
            key=lambda item: item["amount"] * item["discount_pct"] / 100,
            reverse=True,
        )
        total_savings = sum(
            item["amount"] * item["discount_pct"] / 100 for item in ranked
        )
        rows = "\n".join(
            f"| {item['category']} | {item['vendor']} | ${item['amount']:,} | "
            f"{item['discount_pct']}% | ${item['amount'] * item['discount_pct'] / 100:,.0f} | "
            f"{item['expires']} |"
            for item in ranked
        )
        return (
            "**Prioritized Purchase Savings**\n\n"
            "| Category | Vendor | Planned Spend | Discount | Savings | Expires |\n"
            "|---|---|---|---|---|---|\n" + rows
            + f"\n\n**Quarterly savings snapshot:** ${total_savings:,.0f} across "
              f"{len(ranked)} purchasing areas."
            + "\n\nSource: [Dynamics 365 Vendor Data + Contract Terms]\n"
              "Agents: IdentifyDiscountsAgent"
        )

    def _expiring_discounts(self):
        rows = "\n".join(
            f"| {item['vendor']} | {item['category']} | {item['expires']} | "
            f"${item['amount'] * item['discount_pct'] / 100:,.0f} | {item['timing']} |"
            for item in sorted(_PLANNED_PURCHASES, key=lambda item: item["expires"])
        )
        return (
            "**Expiring Discount Decisions**\n\n"
            "| Vendor | Category | Expires | Savings at Risk | Recommendation |\n"
            "|---|---|---|---|---|\n" + rows
            + "\n\nSource: [Dynamics 365 + Vendor Promotions]\nAgents: IdentifyDiscountsAgent"
        )

    def _draft_purchase_order(self):
        items = _PLANNED_PURCHASES[:2]
        subtotal = sum(item["amount"] for item in items)
        savings = sum(item["amount"] * item["discount_pct"] / 100 for item in items)
        return (
            "**Discounted Purchase Order Draft**\n\n"
            f"- **Items bundled:** {', '.join(item['category'] for item in items)}\n"
            f"- **Subtotal:** ${subtotal:,}\n"
            f"- **Applied savings:** ${savings:,.0f}\n"
            f"- **Draft total:** ${subtotal - savings:,.0f}\n"
            "- **Status:** Prepared for procurement review\n\n"
            "Draft only; no purchase order was created in Dynamics 365.\n\n"
            "Source: [Dynamics 365 Procurement]\nAgents: IdentifyDiscountsAgent"
        )

    def _bulk_order_strategy(self):
        licenses = next(item for item in _PLANNED_PURCHASES if item["category"] == "Software licenses")
        consolidated_amount = 144000
        tier_discount = 20
        return (
            "**Bulk Order Strategy**\n\n"
            f"- Consolidate facility software renewals from ${licenses['amount']:,} "
            f"to ${consolidated_amount:,} of managed spend.\n"
            f"- Unlock the {tier_discount}% volume tier.\n"
            f"- Projected consolidated savings: ${consolidated_amount * tier_discount / 100:,.0f}.\n"
            "- Preserve the current renewal window and validate unused licenses before ordering.\n\n"
            "Source: [Dynamics 365 + License Inventory]\nAgents: IdentifyDiscountsAgent"
        )

    def _execution_timeline(self):
        return (
            "**Savings Execution Timeline**\n\n"
            "| Date | Action | Owner | Dependency |\n|---|---|---|---|\n"
            "| 2025-11-21 | Confirm imaging-device quantities | Category Buyer | Clinical approval |\n"
            "| 2025-11-24 | Submit discounted PO draft | Procurement Manager | Vendor quote |\n"
            "| 2025-12-05 | Consolidate supply demand | Facility Leads | Forecast sign-off |\n"
            "| 2025-12-10 | Secure medical-supply promotion | Finance Director | Budget approval |\n"
            "| 2025-12-20 | Finalize license true-up | IT Procurement | Usage audit |\n\n"
            "Source: [Procurement Plan]\nAgents: IdentifyDiscountsAgent"
        )

    def _setup_tracking(self):
        return (
            "**Simulated Savings Tracking Setup**\n\n"
            "- Teams channel card: Prepared\n"
            "- Approval reminders: Prepared for 48 and 24 hours before each deadline\n"
            "- Stakeholders: Procurement Manager, Finance Director, Category Buyer\n"
            "- Tracked opportunities: 3\n\n"
            "Dry-run receipt: no Teams message, reminder, or Dynamics record was created.\n\n"
            "Source: [Microsoft Teams + Dynamics 365]\nAgents: IdentifyDiscountsAgent"
        )


if __name__ == "__main__":
    agent = IdentifyDiscountsAgent()
    for op in [
        "discount_scan", "eligibility_check", "savings_calculation",
        "approval_workflow", "purchase_savings", "expiring_discounts",
        "draft_purchase_order", "bulk_order_strategy", "execution_timeline",
        "setup_tracking",
    ]:
        print("=" * 60)
        print(agent.perform(operation=op))
        print()
