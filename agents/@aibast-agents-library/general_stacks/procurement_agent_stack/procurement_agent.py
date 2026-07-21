"""
Procurement Agent

Manages purchase requests, vendor comparisons, approval routing, and
spend analysis for organizational procurement workflows.

Where a real deployment would connect to ERP and procurement platforms,
this agent uses a synthetic data layer so it runs anywhere without credentials.

Version 1.1.0 adds evidence-backed optimal-vendor selection, discounted PO
creation previews, Teams reminder preparation, and RFQ orchestration. Existing
operations and package identity are preserved.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/procurement_agent",
    "version": "1.1.1",
    "display_name": "Procurement Agent",
    "description": "Manages purchase requests, vendor comparisons, approval routing, and spend analysis over built-in demo procurement data.",
    "author": "AIBAST",
    "tags": ["procurement", "purchasing", "vendor", "approval", "spend-analysis"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# SYNTHETIC DATA LAYER
# ═══════════════════════════════════════════════════════════════

_PURCHASE_REQUESTS = {
    "PR-5001": {"id": "PR-5001", "title": "Cloud Infrastructure Upgrade", "requester": "Sarah Chen", "department": "IT", "category": "Technology", "amount": 125000, "priority": "High", "status": "Pending Approval", "vendor_preferred": "AWS", "justification": "Current infrastructure at 92% capacity, scaling needed for Q1 growth", "budget_code": "IT-INFRA-2025"},
    "PR-5002": {"id": "PR-5002", "title": "Office Furniture - New Floor Build-Out", "requester": "Tom Rivera", "department": "Facilities", "category": "Office Supplies", "amount": 48500, "priority": "Medium", "status": "Vendor Selection", "vendor_preferred": "Steelcase", "justification": "5th floor build-out for 30 new employees starting Q2", "budget_code": "FAC-CAPEX-2025"},
    "PR-5003": {"id": "PR-5003", "title": "Annual Software License Renewal - Salesforce", "requester": "Mike Torres", "department": "Sales", "category": "Software", "amount": 215000, "priority": "High", "status": "Approved", "vendor_preferred": "Salesforce", "justification": "Annual enterprise license renewal, 200 seats", "budget_code": "SALES-SW-2025"},
    "PR-5004": {"id": "PR-5004", "title": "Employee Training Program - Leadership Development", "requester": "Lisa Park", "department": "HR", "category": "Professional Services", "amount": 35000, "priority": "Low", "status": "Draft", "vendor_preferred": "FranklinCovey", "justification": "Q2 leadership development program for 25 managers", "budget_code": "HR-TRAIN-2025"},
}

_VENDOR_CATALOG = {
    "VND-001": {"name": "AWS", "category": "Cloud Infrastructure", "contract_status": "Active", "tier": "Strategic", "rating": 4.7, "annual_spend": 890000, "payment_terms": "Net 30", "contact": "Enterprise Account Manager"},
    "VND-002": {"name": "Salesforce", "category": "CRM Software", "contract_status": "Active", "tier": "Strategic", "rating": 4.5, "annual_spend": 430000, "payment_terms": "Annual Prepay", "contact": "Customer Success Manager"},
    "VND-003": {"name": "Steelcase", "category": "Office Furniture", "contract_status": "Active", "tier": "Preferred", "rating": 4.3, "annual_spend": 125000, "payment_terms": "Net 45", "contact": "Account Representative"},
    "VND-004": {"name": "Herman Miller", "category": "Office Furniture", "contract_status": "Active", "tier": "Approved", "rating": 4.6, "annual_spend": 85000, "payment_terms": "Net 30", "contact": "Regional Sales"},
    "VND-005": {"name": "Azure", "category": "Cloud Infrastructure", "contract_status": "Active", "tier": "Strategic", "rating": 4.6, "annual_spend": 650000, "payment_terms": "Net 30", "contact": "Technical Account Manager"},
    "VND-006": {"name": "FranklinCovey", "category": "Training Services", "contract_status": "Active", "tier": "Approved", "rating": 4.2, "annual_spend": 45000, "payment_terms": "Net 30", "contact": "Program Director"},
}

_APPROVAL_THRESHOLDS = [
    {"max_amount": 5000, "approver": "Direct Manager", "sla_hours": 4},
    {"max_amount": 25000, "approver": "Department Head", "sla_hours": 8},
    {"max_amount": 100000, "approver": "VP Finance", "sla_hours": 24},
    {"max_amount": 500000, "approver": "CFO", "sla_hours": 48},
    {"max_amount": 999999999, "approver": "CEO + Board", "sla_hours": 120},
]

_SPEND_CATEGORIES = {
    "Technology": {"budget": 2500000, "spent_ytd": 1875000, "committed": 340000, "available": 285000, "trend": "+12% YoY"},
    "Software": {"budget": 800000, "spent_ytd": 645000, "committed": 215000, "available": -60000, "trend": "+18% YoY"},
    "Office Supplies": {"budget": 350000, "spent_ytd": 210000, "committed": 48500, "available": 91500, "trend": "-5% YoY"},
    "Professional Services": {"budget": 500000, "spent_ytd": 325000, "committed": 35000, "available": 140000, "trend": "+8% YoY"},
    "Travel": {"budget": 200000, "spent_ytd": 142000, "committed": 18000, "available": 40000, "trend": "-15% YoY"},
}

_OFFICE_FURNITURE_QUOTES = {
    "VND-003": {"unit_price": 1425, "volume_discount_pct": 12, "delivery_days": 4, "contract_compliant": True},
    "VND-004": {"unit_price": 1510, "volume_discount_pct": 15, "delivery_days": 7, "contract_compliant": True},
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _get_approval_level(amount):
    for threshold in _APPROVAL_THRESHOLDS:
        if amount <= threshold["max_amount"]:
            return threshold
    return _APPROVAL_THRESHOLDS[-1]


def _find_competing_vendors(category):
    return [v for v in _VENDOR_CATALOG.values() if category.lower() in v["category"].lower()]


def _total_spend_summary():
    total_budget = sum(c["budget"] for c in _SPEND_CATEGORIES.values())
    total_spent = sum(c["spent_ytd"] for c in _SPEND_CATEGORIES.values())
    total_committed = sum(c["committed"] for c in _SPEND_CATEGORIES.values())
    return total_budget, total_spent, total_committed


def _rank_office_furniture_vendors(quantity=30):
    ranked = []
    for vendor_id, quote in _OFFICE_FURNITURE_QUOTES.items():
        vendor = _VENDOR_CATALOG[vendor_id]
        gross = quote["unit_price"] * quantity
        net = gross * (1 - quote["volume_discount_pct"] / 100)
        score = vendor["rating"] * 20 - quote["delivery_days"] - net / 10000
        ranked.append({
            "score": score,
            "vendor_id": vendor_id,
            "vendor": vendor,
            "quote": quote,
            "gross": gross,
            "net": net,
        })
    return sorted(ranked, key=lambda item: (-item["score"], item["vendor_id"]))


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class ProcurementAgent(BasicAgent):
    """
    Procurement management agent.

    Operations:
        purchase_request   - create and view purchase requests
        vendor_comparison  - compare vendors for a category
        approval_routing   - determine approval path for a request
        spend_analysis     - analyze spend by category and budget
        optimal_vendor     - apply contract terms and rank approved vendors
        create_purchase_order - preview a discounted PO and approval route
        approval_reminders - prepare Teams reminders for approvers
        create_rfq         - simulate RFQ distribution and response tracking
        duplicate_license_check - flag overlapping software entitlements
    """

    def __init__(self):
        self.name = "ProcurementAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "purchase_request", "vendor_comparison",
                            "approval_routing", "spend_analysis",
                            "optimal_vendor", "create_purchase_order",
                            "approval_reminders", "create_rfq",
                            "duplicate_license_check",
                        ],
                        "description": "The procurement operation to perform",
                    },
                    "request_id": {
                        "type": "string",
                        "description": "Purchase request ID (e.g. 'PR-5001')",
                    },
                    "vendor_id": {
                        "type": "string",
                        "description": "Optional approved office-furniture vendor ID for create_purchase_order",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "purchase_request")
        dispatch = {
            "purchase_request": self._purchase_request,
            "vendor_comparison": self._vendor_comparison,
            "approval_routing": self._approval_routing,
            "spend_analysis": self._spend_analysis,
            "optimal_vendor": self._optimal_vendor,
            "create_purchase_order": self._create_purchase_order,
            "approval_reminders": self._approval_reminders,
            "create_rfq": self._create_rfq,
            "duplicate_license_check": self._duplicate_license_check,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(kwargs)

    # ── purchase_request ───────────────────────────────────────
    def _purchase_request(self, params):
        req_id = params.get("request_id") or "PR-5001"
        if req_id not in _PURCHASE_REQUESTS:
            return (
                f"**Error:** Unknown request_id `{req_id}`. "
                f"Available request IDs: {', '.join(sorted(_PURCHASE_REQUESTS))}."
            )
        pr = _PURCHASE_REQUESTS[req_id]
        approval = _get_approval_level(pr["amount"])
        return (
            f"**Purchase Request: {pr['id']}**\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Title | {pr['title']} |\n"
            f"| Requester | {pr['requester']} ({pr['department']}) |\n"
            f"| Category | {pr['category']} |\n"
            f"| Amount | ${pr['amount']:,} |\n"
            f"| Priority | {pr['priority']} |\n"
            f"| Status | {pr['status']} |\n"
            f"| Preferred Vendor | {pr['vendor_preferred']} |\n"
            f"| Budget Code | {pr['budget_code']} |\n"
            f"| Required Approver | {approval['approver']} |\n\n"
            f"**Justification:** {pr['justification']}\n\n"
            f"Source: [Procurement System]\nAgents: ProcurementAgent"
        )

    # ── vendor_comparison ──────────────────────────────────────
    def _vendor_comparison(self, params):
        rows = ""
        for vid, v in _VENDOR_CATALOG.items():
            rows += f"| {vid} | {v['name']} | {v['category']} | {v['tier']} | {v['rating']}/5 | ${v['annual_spend']:,} | {v['payment_terms']} |\n"
        return (
            f"**Vendor Comparison**\n\n"
            f"| ID | Vendor | Category | Tier | Rating | Annual Spend | Terms |\n|---|---|---|---|---|---|---|\n"
            f"{rows}\n"
            f"**Vendor Tiers:**\n"
            f"- Strategic: Long-term partners, best pricing, dedicated support\n"
            f"- Preferred: Competitive pricing, standard support, pre-approved\n"
            f"- Approved: Vetted and available, standard terms\n\n"
            f"Source: [Vendor Management System]\nAgents: ProcurementAgent"
        )

    # ── approval_routing ───────────────────────────────────────
    def _approval_routing(self, params):
        req_id = params.get("request_id") or "PR-5001"
        if req_id not in _PURCHASE_REQUESTS:
            return (
                f"**Error:** Unknown request_id `{req_id}`. "
                f"Available request IDs: {', '.join(sorted(_PURCHASE_REQUESTS))}."
            )
        pr = _PURCHASE_REQUESTS[req_id]
        approval = _get_approval_level(pr["amount"])
        threshold_rows = ""
        for t in _APPROVAL_THRESHOLDS:
            limit = f"${t['max_amount']:,}" if t["max_amount"] < 999999999 else "Unlimited"
            marker = " <-- This request" if t == approval else ""
            threshold_rows += f"| Up to {limit} | {t['approver']} | {t['sla_hours']}h |{marker}\n"
        return (
            f"**Approval Routing: {pr['id']}**\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Request | {pr['title']} |\n"
            f"| Amount | ${pr['amount']:,} |\n"
            f"| Required Approver | {approval['approver']} |\n"
            f"| Approval SLA | {approval['sla_hours']} hours |\n"
            f"| Current Status | {pr['status']} |\n\n"
            f"**Approval Thresholds:**\n\n"
            f"| Amount Limit | Approver | SLA |\n|---|---|---|\n"
            f"{threshold_rows}\n\n"
            f"Source: [Approval Workflow Engine]\nAgents: ProcurementAgent"
        )

    # ── spend_analysis ─────────────────────────────────────────
    def _spend_analysis(self, params):
        total_budget, total_spent, total_committed = _total_spend_summary()
        total_available = total_budget - total_spent - total_committed
        cat_rows = ""
        for cat, data in _SPEND_CATEGORIES.items():
            utilization = (data["spent_ytd"] + data["committed"]) / data["budget"] * 100
            status = "Over Budget" if data["available"] < 0 else ("At Risk" if utilization > 85 else "On Track")
            cat_rows += f"| {cat} | ${data['budget']:,} | ${data['spent_ytd']:,} | ${data['committed']:,} | ${data['available']:,} | {status} | {data['trend']} |\n"
        return (
            f"**Spend Analysis**\n\n"
            f"| Metric | Value |\n|---|---|\n"
            f"| Total Budget | ${total_budget:,} |\n"
            f"| Spent YTD | ${total_spent:,} ({total_spent/total_budget*100:.0f}%) |\n"
            f"| Committed | ${total_committed:,} |\n"
            f"| Available | ${total_available:,} |\n\n"
            f"**By Category:**\n\n"
            f"| Category | Budget | Spent YTD | Committed | Available | Status | Trend |\n|---|---|---|---|---|---|---|\n"
            f"{cat_rows}\n"
            f"**Alerts:**\n"
            f"- Software category over budget by $60,000 - requires reallocation\n"
            f"- Technology committed spend approaching budget limit\n\n"
            f"Source: [ERP + Finance System]\nAgents: ProcurementAgent"
        )

    def _optimal_vendor(self, params):
        quantity = 30
        ranked = _rank_office_furniture_vendors(quantity)
        rows = "\n".join(
            f"| {item['vendor_id']} | {item['vendor']['name']} | {item['vendor']['rating']}/5 | "
            f"{item['quote']['volume_discount_pct']}% | {item['quote']['delivery_days']} days | "
            f"${item['net']:,.0f} | {'Yes' if item['quote']['contract_compliant'] else 'No'} |"
            for item in ranked
        )
        winner = ranked[0]
        return (
            "**Optimal Approved Vendor**\n\n"
            "| Vendor ID | Vendor | Rating | Volume Discount | Delivery | Net Cost | Contract Compliant |\n"
            "|---|---|---|---|---|---|---|\n" + rows
            + f"\n\n**Recommendation:** {winner['vendor']['name']} ({winner['vendor_id']}) for best combined "
              "contract value, delivery timing, and performance.\n\n"
              "Source: [Dynamics 365 Vendor Master + Contract Terms]\nAgents: ProcurementAgent"
        )

    def _create_purchase_order(self, params):
        request_id = params.get("request_id") or "PR-5002"
        if request_id not in _PURCHASE_REQUESTS:
            return (
                f"**Error:** Unknown request_id `{request_id}`. "
                f"Available request IDs: {', '.join(sorted(_PURCHASE_REQUESTS))}."
            )
        pr = _PURCHASE_REQUESTS[request_id]
        if pr["category"] != "Office Supplies":
            return (
                f"**Error:** Request `{request_id}` has category `{pr['category']}` and is "
                "incompatible with the approved office-furniture quote set. "
                "Use request_id `PR-5002`."
            )
        ranked = _rank_office_furniture_vendors(30)
        vendor_id = params.get("vendor_id") or ranked[0]["vendor_id"]
        if vendor_id not in _OFFICE_FURNITURE_QUOTES:
            return (
                f"**Error:** Unknown or ineligible office-furniture vendor_id `{vendor_id}`. "
                f"Available vendor IDs: {', '.join(sorted(_OFFICE_FURNITURE_QUOTES))}."
            )
        vendor = _VENDOR_CATALOG[vendor_id]
        quote = _OFFICE_FURNITURE_QUOTES[vendor_id]
        gross = quote["unit_price"] * 30
        discount = gross * quote["volume_discount_pct"] / 100
        total = gross - discount
        approval = _get_approval_level(total)
        return (
            f"**Purchase Order Preview for {pr['id']}**\n\n"
            f"- Vendor: {vendor['name']} ({vendor_id})\n"
            "- Bundle: 30 ergonomic workstation packages\n"
            f"- Gross: ${gross:,}\n"
            f"- Volume discount: {quote['volume_discount_pct']}% (${discount:,.0f})\n"
            f"- PO total: ${total:,.0f}\n"
            f"- Budget check: Within {pr['budget_code']}\n"
            f"- Approval route: {approval['approver']} ({approval['sla_hours']}h SLA)\n\n"
            "Dry-run receipt: no Dynamics 365 PO or approval was created.\n\n"
            "Source: [Dynamics 365 Procurement + Microsoft Teams]\nAgents: ProcurementAgent"
        )

    def _approval_reminders(self, params):
        request_id = params.get("request_id") or "PR-5002"
        if request_id not in _PURCHASE_REQUESTS:
            return (
                f"**Error:** Unknown request_id `{request_id}`. "
                f"Available request IDs: {', '.join(sorted(_PURCHASE_REQUESTS))}."
            )
        pr = _PURCHASE_REQUESTS[request_id]
        approval = _get_approval_level(pr["amount"])
        return (
            f"**Approval Reminder Preview: {pr['id']}**\n\n"
            f"- Approver: {approval['approver']}\n"
            f"- Teams reminders: 8 hours and 2 hours before the {approval['sla_hours']}h SLA\n"
            f"- Escalation: Finance Operations at SLA breach\n"
            f"- Status: Prepared, not sent\n\n"
            "Source: [Microsoft Teams + Dynamics 365]\nAgents: ProcurementAgent"
        )

    def _create_rfq(self, params):
        rows = "\n".join(
            f"| {vendor_id} | {vendor['name']} | Prepared | 2025-11-24 | "
            f"Price, delivery, warranty, sustainability |"
            for vendor_id, vendor in _VENDOR_CATALOG.items()
            if vendor["category"] == "Office Furniture"
        )
        return (
            "**Office Furniture RFQ Preview**\n\n"
            "| Vendor ID | Vendor | Distribution | Due | Evaluation Criteria |\n"
            "|---|---|---|---|---|\n" + rows
            + "\n\nResponse tracker and weighted evaluation matrix are prepared. "
              "No RFQ was distributed and no vendor record was changed.\n\n"
              "Source: [Dynamics 365 Procurement + Microsoft Teams]\nAgents: ProcurementAgent"
        )

    def _duplicate_license_check(self, params):
        return (
            "**Duplicate Software License Check**\n\n"
            "| Product | Purchased | Assigned | Overlap | Annual Avoidable Spend | Action |\n"
            "|---|---|---|---|---|---|\n"
            "| CRM Enterprise | 200 | 176 | 24 | $25,800 | Remove inactive seats before renewal |\n"
            "| Diagram Pro | 80 | 61 | 9 shared-suite overlaps | $4,860 | Consolidate to suite entitlement |\n\n"
            "**Total flagged:** $30,660 annual avoidable spend.\n"
            "Analysis only; no license, contract, or purchase record was changed.\n\n"
            "Source: [Dynamics 365 Procurement + License Inventory]\nAgents: ProcurementAgent"
        )


if __name__ == "__main__":
    agent = ProcurementAgent()
    for op in [
        "purchase_request", "vendor_comparison", "approval_routing",
        "spend_analysis", "optimal_vendor", "create_purchase_order",
        "approval_reminders", "create_rfq", "duplicate_license_check",
    ]:
        print("=" * 60)
        print(agent.perform(operation=op, request_id="PR-5001"))
        print()
