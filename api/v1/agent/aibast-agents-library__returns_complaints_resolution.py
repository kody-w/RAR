"""
Returns & Complaints Resolution Agent — Retail & CPG Stack

Handles return processing, complaint classification, resolution
recommendation, and trend analysis for retail customer service operations.

Version 1.1.0 adds deterministic, exact-keyed service recovery, quality/fraud,
simulated resolution, follow-up, and executive reporting workflows.
"""

import sys
import os

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"),
)
from basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/returns_complaints_resolution",
    "version": "1.1.0",
    "display_name": "Returns & Complaints Resolution Agent",
    "description": (
        "Automates return processing, classifies customer complaints, "
        "recommends optimal resolutions, and identifies complaint trends "
        "for retail and CPG customer service teams."
    ),
    "author": "AIBAST",
    "tags": [
        "returns",
        "complaints",
        "customer-service",
        "resolution",
        "retail",
    ],
    "category": "retail_cpg",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# ---------------------------------------------------------------------------
# Synthetic Data — Return Requests
# ---------------------------------------------------------------------------

RETURN_REQUESTS = {
    "RET-4001": {
        "order_id": "ORD-88712",
        "customer_id": "CUST-2041",
        "customer_name": "Sarah Mitchell",
        "product": "Classic Denim Jacket",
        "sku": "SKU-1001",
        "purchase_price": 89.99,
        "purchase_date": "2026-02-14",
        "request_date": "2026-03-02",
        "reason": "wrong_size",
        "condition": "unworn_tags_attached",
        "channel": "online",
        "status": "pending_review",
        "notes": "Ordered size M, needs size L. Willing to exchange.",
    },
    "RET-4002": {
        "order_id": "ORD-89234",
        "customer_id": "CUST-3178",
        "customer_name": "James Kowalski",
        "product": "Smart Fitness Tracker",
        "sku": "SKU-1004",
        "purchase_price": 129.99,
        "purchase_date": "2026-01-20",
        "request_date": "2026-03-10",
        "reason": "defective",
        "condition": "non_functional",
        "channel": "in_store",
        "status": "approved",
        "notes": "Heart rate sensor stopped working after 3 weeks. Under warranty.",
    },
    "RET-4003": {
        "order_id": "ORD-87455",
        "customer_id": "CUST-1590",
        "customer_name": "Maria Chen",
        "product": "Premium Running Shoes",
        "sku": "SKU-1005",
        "purchase_price": 149.99,
        "purchase_date": "2026-02-28",
        "request_date": "2026-03-08",
        "reason": "not_as_described",
        "condition": "lightly_used",
        "channel": "online",
        "status": "pending_review",
        "notes": "Color shown online was navy but received was dark grey.",
    },
    "RET-4004": {
        "order_id": "ORD-90100",
        "customer_id": "CUST-4422",
        "customer_name": "David Okafor",
        "product": "Wireless Earbuds Pro",
        "sku": "SKU-1002",
        "purchase_price": 59.99,
        "purchase_date": "2026-03-01",
        "request_date": "2026-03-12",
        "reason": "changed_mind",
        "condition": "opened_unused",
        "channel": "online",
        "status": "pending_review",
        "notes": "Found a better deal elsewhere. Wants full refund.",
    },
    "RET-4005": {
        "order_id": "ORD-86321",
        "customer_id": "CUST-0887",
        "customer_name": "Linda Park",
        "product": "Leather Crossbody Bag",
        "sku": "SKU-1007",
        "purchase_price": 79.99,
        "purchase_date": "2025-12-18",
        "request_date": "2026-03-14",
        "reason": "defective",
        "condition": "damaged",
        "channel": "in_store",
        "status": "escalated",
        "notes": "Strap broke after normal use. Outside 60-day window but claims manufacturing defect.",
    },
    "RET-4006": {
        "order_id": "ORD-91005",
        "customer_id": "CUST-5610",
        "customer_name": "Robert Fernandez",
        "product": "UV Protection Sunglasses",
        "sku": "SKU-1008",
        "purchase_price": 44.99,
        "purchase_date": "2026-03-05",
        "request_date": "2026-03-15",
        "reason": "wrong_item",
        "condition": "unopened",
        "channel": "online",
        "status": "approved",
        "notes": "Received aviator style instead of ordered wayfarer style.",
    },
}

COMPLAINT_CATEGORIES = {
    "product_quality": {
        "label": "Product Quality",
        "severity_weight": 0.85,
        "avg_resolution_hours": 36,
        "escalation_rate": 0.15,
        "keywords": ["defective", "broken", "poor quality", "fell apart", "not durable"],
        "monthly_volume": 142,
    },
    "order_fulfillment": {
        "label": "Order Fulfillment",
        "severity_weight": 0.70,
        "avg_resolution_hours": 24,
        "escalation_rate": 0.08,
        "keywords": ["wrong item", "missing", "late delivery", "not received", "damaged in shipping"],
        "monthly_volume": 98,
    },
    "pricing_billing": {
        "label": "Pricing & Billing",
        "severity_weight": 0.65,
        "avg_resolution_hours": 18,
        "escalation_rate": 0.05,
        "keywords": ["overcharged", "wrong price", "coupon not applied", "double charged"],
        "monthly_volume": 67,
    },
    "service_experience": {
        "label": "Service Experience",
        "severity_weight": 0.60,
        "avg_resolution_hours": 48,
        "escalation_rate": 0.22,
        "keywords": ["rude staff", "long wait", "unhelpful", "no response", "poor communication"],
        "monthly_volume": 53,
    },
}

RESOLUTION_PLAYBOOKS = {
    "full_refund": {
        "label": "Full Refund",
        "applicable_reasons": ["defective", "wrong_item", "not_as_described"],
        "applicable_conditions": ["non_functional", "unopened", "damaged"],
        "max_days_since_purchase": 90,
        "cost_impact": "high",
        "csat_impact": "high",
        "steps": [
            "Verify purchase and return eligibility",
            "Approve full refund to original payment method",
            "Generate prepaid return shipping label",
            "Send confirmation email with refund timeline",
            "Process refund within 3-5 business days",
        ],
    },
    "exchange": {
        "label": "Product Exchange",
        "applicable_reasons": ["wrong_size", "wrong_item", "not_as_described"],
        "applicable_conditions": ["unworn_tags_attached", "unopened", "opened_unused"],
        "max_days_since_purchase": 60,
        "cost_impact": "medium",
        "csat_impact": "very_high",
        "steps": [
            "Confirm desired replacement item and availability",
            "Generate prepaid return label for original item",
            "Ship replacement item with expedited shipping",
            "Send tracking information for both shipments",
            "Follow up after delivery to confirm satisfaction",
        ],
    },
    "store_credit": {
        "label": "Store Credit",
        "applicable_reasons": ["changed_mind", "wrong_size"],
        "applicable_conditions": ["opened_unused", "lightly_used", "unworn_tags_attached"],
        "max_days_since_purchase": 45,
        "cost_impact": "low",
        "csat_impact": "moderate",
        "steps": [
            "Verify item condition meets return standards",
            "Issue store credit for full purchase amount plus 10% bonus",
            "Credit applied to customer loyalty account",
            "Send email with credit balance and expiration date",
        ],
    },
    "warranty_replacement": {
        "label": "Warranty Replacement",
        "applicable_reasons": ["defective"],
        "applicable_conditions": ["non_functional", "damaged"],
        "max_days_since_purchase": 365,
        "cost_impact": "medium",
        "csat_impact": "high",
        "steps": [
            "Verify product is within warranty period",
            "Collect defect documentation and photos",
            "Submit warranty claim to manufacturer",
            "Ship replacement from warranty stock",
            "Allow customer to keep defective unit or provide return label",
        ],
    },
    "partial_refund": {
        "label": "Partial Refund",
        "applicable_reasons": ["not_as_described", "changed_mind"],
        "applicable_conditions": ["lightly_used"],
        "max_days_since_purchase": 30,
        "cost_impact": "medium",
        "csat_impact": "moderate",
        "steps": [
            "Assess item condition and determine refund percentage",
            "Apply restocking fee if applicable (15% for opened items)",
            "Process partial refund to original payment method",
            "Notify customer of refund amount and timeline",
        ],
    },
}

TREND_DATA = {
    "months": ["2025-10", "2025-11", "2025-12", "2026-01", "2026-02", "2026-03"],
    "total_returns": [312, 345, 498, 387, 328, 360],
    "return_rate_pct": [4.1, 4.5, 6.2, 5.0, 4.3, 4.7],
    "top_return_reasons": {
        "wrong_size": [98, 112, 160, 125, 105, 115],
        "defective": [72, 68, 95, 82, 71, 78],
        "changed_mind": [65, 78, 130, 88, 70, 80],
        "not_as_described": [45, 52, 68, 55, 48, 52],
        "wrong_item": [32, 35, 45, 37, 34, 35],
    },
    "avg_resolution_hours": [28.5, 30.2, 38.7, 32.1, 27.8, 29.4],
    "csat_score": [4.1, 4.0, 3.6, 3.9, 4.2, 4.1],
    "refund_total_usd": [18720.00, 21450.00, 34200.00, 24800.00, 19650.00, 22100.00],
}

EVIDENCE_CAPABILITIES = {
    "escalation_snapshot": {
        "title": "Escalated Complaint Snapshot",
        "source_system": "Dynamics 365 Customer Service and Outlook",
        "write": False,
        "key_field": "case_id",
        "summary": (
            "Combines customer value, purchase history, support interactions, "
            "sentiment, and churn risk into an immediate-action snapshot."
        ),
        "record": {
            "case_id": "CASE-DAVID-CHEN",
            "customer": "David Chen; Diamond VIP; 47 purchases; $18,400 lifetime value",
            "issue": "ProBook Elite 15 display flickers and will not boot on day 3",
            "warranty": "Active 2-year standard warranty",
            "history": "45-minute hold with three transfers, followed by failed troubleshooting",
            "sentiment": "High frustration after two failed support calls",
            "churn_risk": "87%; immediate recovery action recommended",
        },
    },
    "recovery_options": {
        "title": "Customer-Value Recovery Options",
        "source_system": "Dynamics 365 Customer Service",
        "write": False,
        "key_field": "option_set_id",
        "summary": (
            "Compares resolution tiers by fulfillment speed, recovery cost, "
            "retention probability, and customer lifetime value."
        ),
        "record": {
            "option_set_id": "OPTIONS-DAVID-CHEN",
            "tier_1": "Elite Plus upgrade; same-day courier; $200 credit; 90-day extension; $540 cost",
            "tier_2": "Same-model replacement; 2-day shipping; $100 credit; $180 cost; 65% retention",
            "tier_3": "Same-model replacement; standard 5-day shipping; $0 incremental cost; 35% retention",
            "recommendation": "Tier 1 protects $18,400 lifetime value for $540, a 34:1 retention ROI",
        },
    },
    "resolution_execution": {
        "title": "Resolution Execution and Talking Points",
        "source_system": "Dynamics 365 Customer Service, Outlook, and Teams",
        "write": True,
        "key_field": "resolution_id",
        "summary": (
            "Prepares approved fulfillment, credit, return, and empathetic "
            "communication actions while keeping every external write simulated."
        ),
        "record": {
            "resolution_id": "RESOLUTION-DAVID-TIER1",
            "fulfillment": "Elite Plus upgrade prepared for same-day courier delivery at 4:30 PM",
            "credit": "$200 store credit and 90-day return extension prepared",
            "return": "Return label prepared for the defective laptop",
            "talking_points": "Apologize, acknowledge Diamond status, explain upgrade and speed, confirm credit, provide direct ownership",
            "execution_note": "Simulation only; no shipment, credit, label, or customer message is created",
        },
    },
    "follow_up_plan": {
        "title": "Service Recovery Follow-Up Plan",
        "source_system": "Dynamics 365 Customer Service and Outlook",
        "write": True,
        "key_field": "follow_up_id",
        "summary": (
            "Prepares structured post-resolution touchpoints and monitoring "
            "without scheduling messages or changing a customer record."
        ),
        "record": {
            "follow_up_id": "FOLLOWUP-DAVID-30D",
            "today": "Delivery confirmation at 18:00 and manager email at 19:00",
            "day_3": "Customer success call and NPS survey",
            "day_7": "Elite Plus tips and 25% accessory offer",
            "day_30": "Relationship health check and VIP appreciation invitation",
            "monitoring": "90-day ticket priority, churn-risk tracking, and purchase-behavior analysis",
            "execution_note": "Simulation only; no communication, task, or CRM update is scheduled",
        },
    },
    "quality_fraud_analysis": {
        "title": "SKU Quality and Return Fraud Analysis",
        "source_system": "Dynamics 365 Commerce and Customer Service",
        "write": False,
        "key_field": "analysis_id",
        "summary": (
            "Surfaces deterministic SKU-level defect and suspicious-return "
            "patterns for quality and loss-prevention review."
        ),
        "record": {
            "analysis_id": "ANALYSIS-PROBOOK-Q2",
            "quality_signal": "Display-failure returns reached 4.8%, above the 1.5% category baseline",
            "affected_batch": "ProBook Elite 15 batch PB15-0426; 23 related cases",
            "fraud_signal": "Three accounts share delivery addresses across seven high-value return requests",
            "recommended_actions": "Open supplier quality review; hold affected batch; route linked accounts to loss prevention",
            "decision_boundary": "Signals require human review; no return is denied automatically",
        },
    },
    "recovery_report": {
        "title": "Service Recovery Executive Report",
        "source_system": "Microsoft Teams",
        "write": True,
        "key_field": "report_id",
        "summary": (
            "Produces case and program economics with a simulated leadership "
            "distribution receipt."
        ),
        "record": {
            "report_id": "REPORT-RECOVERY-Q2",
            "case_result": "Resolved in 4 hours; $18,400 lifetime value protected for $540; 34:1 retention ROI",
            "program_metrics": "4.2-hour resolution; 94% retention; +47 NPS recovery; 76% six-month repeat purchase",
            "program_economics": "$127,000 quarterly investment; $4.8M protected revenue; $4.67M net value",
            "executive_summary": "Customer crisis converted into a loyalty recovery with structured 30-day follow-up",
            "distribution": "Prepared for leadership review in Microsoft Teams",
        },
    },
}

_EVIDENCE_KEY_PUNCTUATION = "-_.,:;()?!/#@+$%^&*=[]{}<>~`'\""


def _normalize_evidence_tokens(text):
    tokens = []
    for raw in str(text).split():
        cleaned = "".join(
            character.lower()
            for character in raw
            if character not in _EVIDENCE_KEY_PUNCTUATION
        )
        if cleaned:
            tokens.append(cleaned)
    return tokens


def _record_for_evidence_request(capability, key, user_input):
    record = capability["record"]
    key_field = capability["key_field"]
    if key:
        if str(record[key_field]).lower() == str(key).strip().lower():
            return "match", record
        return "not_found", None
    query_tokens = _normalize_evidence_tokens(user_input)
    key_tokens = _normalize_evidence_tokens(record[key_field])
    width = len(key_tokens)
    if width and any(
        query_tokens[index:index + width] == key_tokens
        for index in range(len(query_tokens) - width + 1)
    ):
        return "match", record
    return "summary", None


def _format_evidence_record(record):
    return "\n".join(
        f"- **{field.replace('_', ' ').title()}:** {value}"
        for field, value in record.items()
    )


# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------

def _days_since_purchase(ret):
    """Calculate days between purchase and return request (simplified)."""
    purchase_parts = ret["purchase_date"].split("-")
    request_parts = ret["request_date"].split("-")
    p_days = int(purchase_parts[0]) * 365 + int(purchase_parts[1]) * 30 + int(purchase_parts[2])
    r_days = int(request_parts[0]) * 365 + int(request_parts[1]) * 30 + int(request_parts[2])
    return r_days - p_days


def _classify_complaint(text):
    """Classify complaint text into a category based on keyword matching."""
    text_lower = text.lower()
    best_cat = "service_experience"
    best_score = 0
    for cat_id, cat in COMPLAINT_CATEGORIES.items():
        score = sum(1 for kw in cat["keywords"] if kw in text_lower)
        if score > best_score:
            best_score = score
            best_cat = cat_id
    return best_cat


def _recommend_resolution(ret):
    """Pick best resolution playbook for a return request."""
    reason = ret["reason"]
    condition = ret["condition"]
    days = _days_since_purchase(ret)
    best_match = None
    for pb_id, pb in RESOLUTION_PLAYBOOKS.items():
        if reason in pb["applicable_reasons"] and condition in pb["applicable_conditions"]:
            if days <= pb["max_days_since_purchase"]:
                if best_match is None or pb["csat_impact"] in ("very_high", "high"):
                    best_match = pb_id
    return best_match or "store_credit"


def _return_rate_trend():
    """Calculate return-rate trend direction."""
    rates = TREND_DATA["return_rate_pct"]
    recent_avg = sum(rates[-3:]) / 3
    earlier_avg = sum(rates[:3]) / 3
    if recent_avg < earlier_avg - 0.3:
        return "improving"
    elif recent_avg > earlier_avg + 0.3:
        return "worsening"
    return "stable"


# ---------------------------------------------------------------------------
# Agent Class
# ---------------------------------------------------------------------------

class ReturnsComplaintsResolutionAgent(BasicAgent):
    """Agent for automated returns processing and complaint resolution."""

    def __init__(self):
        self.name = "returns-complaints-resolution-agent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "return_processing",
                            "complaint_classification",
                            "resolution_recommendation",
                            "trend_analysis",
                            "escalation_snapshot",
                            "recovery_options",
                            "resolution_execution",
                            "follow_up_plan",
                            "quality_fraud_analysis",
                            "recovery_report",
                        ],
                    },
                    "return_id": {"type": "string"},
                    "complaint_text": {"type": "string"},
                    "key": {"type": "string"},
                    "user_input": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _return_processing(self, **kwargs):
        return_id = kwargs.get("return_id")
        if return_id and return_id in RETURN_REQUESTS:
            returns = {return_id: RETURN_REQUESTS[return_id]}
        else:
            returns = RETURN_REQUESTS
        lines = ["# Return Processing Queue", ""]
        lines.append("| Return ID | Customer | Product | Reason | Condition | Days | Status |")
        lines.append("|-----------|----------|---------|--------|-----------|------|--------|")
        for rid, ret in returns.items():
            days = _days_since_purchase(ret)
            lines.append(
                f"| {rid} | {ret['customer_name']} | {ret['product']} "
                f"| {ret['reason'].replace('_', ' ')} | {ret['condition'].replace('_', ' ')} "
                f"| {days} | {ret['status'].replace('_', ' ')} |"
            )
        lines.append("")
        for rid, ret in returns.items():
            lines.append(f"### {rid} — {ret['product']}")
            lines.append("")
            lines.append(f"- **Order:** {ret['order_id']}")
            lines.append(f"- **Customer:** {ret['customer_name']} (`{ret['customer_id']}`)")
            lines.append(f"- **Purchase Date:** {ret['purchase_date']} | **Request Date:** {ret['request_date']}")
            lines.append(f"- **Channel:** {ret['channel']}")
            lines.append(f"- **Price:** ${ret['purchase_price']:.2f}")
            lines.append(f"- **Notes:** {ret['notes']}")
            lines.append("")
        pending = sum(1 for r in RETURN_REQUESTS.values() if r["status"] == "pending_review")
        total_value = sum(r["purchase_price"] for r in returns.values())
        lines.append(f"**Pending Reviews:** {pending} | **Queue Value:** ${total_value:,.2f}")
        return "\n".join(lines)

    def _complaint_classification(self, **kwargs):
        complaint_text = kwargs.get("complaint_text", "")
        lines = ["# Complaint Classification", ""]
        if complaint_text:
            cat_id = _classify_complaint(complaint_text)
            cat = COMPLAINT_CATEGORIES[cat_id]
            lines.append(f"**Input:** \"{complaint_text}\"")
            lines.append(f"**Classified As:** {cat['label']} (`{cat_id}`)")
            lines.append(f"**Severity Weight:** {cat['severity_weight']}")
            lines.append(f"**Avg Resolution Time:** {cat['avg_resolution_hours']}h")
            lines.append(f"**Escalation Rate:** {cat['escalation_rate']*100:.0f}%")
            lines.append("")
        lines.append("## Complaint Category Reference")
        lines.append("")
        lines.append("| Category | Monthly Volume | Severity | Avg Resolution | Escalation Rate |")
        lines.append("|----------|---------------|----------|----------------|-----------------|")
        total_volume = 0
        for cat_id, cat in COMPLAINT_CATEGORIES.items():
            total_volume += cat["monthly_volume"]
            lines.append(
                f"| {cat['label']} | {cat['monthly_volume']} "
                f"| {cat['severity_weight']:.2f} | {cat['avg_resolution_hours']}h "
                f"| {cat['escalation_rate']*100:.0f}% |"
            )
        lines.append("")
        lines.append(f"**Total Monthly Complaints:** {total_volume}")
        return "\n".join(lines)

    def _resolution_recommendation(self, **kwargs):
        return_id = kwargs.get("return_id")
        if return_id and return_id in RETURN_REQUESTS:
            returns = {return_id: RETURN_REQUESTS[return_id]}
        else:
            returns = {k: v for k, v in RETURN_REQUESTS.items() if v["status"] == "pending_review"}
        lines = ["# Resolution Recommendations", ""]
        for rid, ret in returns.items():
            rec_id = _recommend_resolution(ret)
            playbook = RESOLUTION_PLAYBOOKS[rec_id]
            lines.append(f"## {rid} — {ret['customer_name']}")
            lines.append("")
            lines.append(f"- **Product:** {ret['product']} (${ret['purchase_price']:.2f})")
            lines.append(f"- **Reason:** {ret['reason'].replace('_', ' ')}")
            lines.append(f"- **Recommended Resolution:** {playbook['label']}")
            lines.append(f"- **Cost Impact:** {playbook['cost_impact']} | **CSAT Impact:** {playbook['csat_impact']}")
            lines.append("")
            lines.append("**Resolution Steps:**")
            for i, step in enumerate(playbook["steps"], 1):
                lines.append(f"  {i}. {step}")
            lines.append("")
        lines.append("## Available Resolution Playbooks")
        lines.append("")
        for pb_id, pb in RESOLUTION_PLAYBOOKS.items():
            lines.append(f"- **{pb['label']}** (`{pb_id}`): Window {pb['max_days_since_purchase']}d, "
                         f"Cost: {pb['cost_impact']}, CSAT: {pb['csat_impact']}")
        return "\n".join(lines)

    def _trend_analysis(self, **kwargs):
        trend_dir = _return_rate_trend()
        lines = [
            "# Returns & Complaints Trend Analysis",
            "",
            f"**Overall Trend:** {trend_dir.upper()}",
            "",
            "## Monthly Returns Overview",
            "",
            "| Month | Total Returns | Return Rate | Avg Resolution | CSAT | Refund Total |",
            "|-------|--------------|-------------|----------------|------|--------------|",
        ]
        for i, month in enumerate(TREND_DATA["months"]):
            lines.append(
                f"| {month} | {TREND_DATA['total_returns'][i]} "
                f"| {TREND_DATA['return_rate_pct'][i]}% "
                f"| {TREND_DATA['avg_resolution_hours'][i]}h "
                f"| {TREND_DATA['csat_score'][i]}/5.0 "
                f"| ${TREND_DATA['refund_total_usd'][i]:,.2f} |"
            )
        lines.append("")
        lines.append("## Return Reasons Breakdown (Last 6 Months)")
        lines.append("")
        for reason, volumes in TREND_DATA["top_return_reasons"].items():
            total = sum(volumes)
            avg = round(total / len(volumes), 1)
            lines.append(f"- **{reason.replace('_', ' ').title()}:** {total} total, {avg} avg/month")
        lines.append("")
        total_refunded = sum(TREND_DATA["refund_total_usd"])
        lines.append(f"**Total Refunded (6 months):** ${total_refunded:,.2f}")
        lines.append("")
        lines.append("## Key Insights")
        lines.append("")
        lines.append("- Holiday season (Dec) drove a 44% spike in returns, primarily changed-mind returns")
        lines.append("- Wrong-size returns consistently highest — consider enhanced size guide implementation")
        lines.append("- Resolution time improved 8% over the period despite volume increases")
        lines.append("- CSAT recovered to 4.1 after post-holiday dip to 3.6")
        return "\n".join(lines)

    def _evidence_capability(self, capability_name, **kwargs):
        capability = EVIDENCE_CAPABILITIES[capability_name]
        lookup_status, record = _record_for_evidence_request(
            capability,
            kwargs.get("key", ""),
            kwargs.get("user_input", ""),
        )
        lines = [
            f"# {capability['title']}",
            "",
            capability["summary"],
            "",
            f"## {capability['source_system']} (synthetic demo data)",
            "",
        ]
        if lookup_status == "not_found":
            lines.append(
                f"No record matched the requested {capability['key_field']}. "
                "Not substituting another record."
            )
        else:
            selected = record or capability["record"]
            label = "Exact keyed record" if lookup_status == "match" else "Worked example"
            lines.extend([f"**{label}:**", _format_evidence_record(selected)])

        if capability["write"] and lookup_status == "match":
            receipt_key = record[capability["key_field"]]
            lines.extend([
                "",
                "## Simulated Write Receipt",
                "",
                "- **Action Status:** simulated",
                f"- **Receipt:** SIM-{capability_name.upper()}-{receipt_key}",
                f"- **Target System:** {capability['source_system']}",
                "- **External Changes:** none; no live fulfillment, credit, communication, or record update occurred",
            ])
        elif capability["write"]:
            lines.extend([
                "",
                "_Write-capable workflow; provide an exact key to generate a "
                "simulated receipt. No external system is modified._",
            ])
        else:
            lines.extend(["", "_Read-only; no external system is modified._"])
        return "\n".join(lines)

    def perform(self, **kwargs):
        operation = kwargs.get("operation", "return_processing")
        dispatch = {
            "return_processing": self._return_processing,
            "complaint_classification": self._complaint_classification,
            "resolution_recommendation": self._resolution_recommendation,
            "trend_analysis": self._trend_analysis,
            "escalation_snapshot": self._evidence_capability,
            "recovery_options": self._evidence_capability,
            "resolution_execution": self._evidence_capability,
            "follow_up_plan": self._evidence_capability,
            "quality_fraud_analysis": self._evidence_capability,
            "recovery_report": self._evidence_capability,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"Unknown operation `{operation}`. Valid: {', '.join(dispatch.keys())}"
        if operation in EVIDENCE_CAPABILITIES:
            return handler(operation, **kwargs)
        return handler(**kwargs)


# ---------------------------------------------------------------------------
# Main — exercise all operations
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = ReturnsComplaintsResolutionAgent()
    print("=" * 80)
    print(agent.perform(operation="return_processing"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="complaint_classification", complaint_text="The product fell apart after one week, poor quality stitching"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="resolution_recommendation", return_id="RET-4001"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="trend_analysis"))
    print("=" * 80)
