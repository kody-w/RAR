"""
Utility Billing Assistance Agent — SLG Government Stack

Provides utility billing support including account inquiries, usage
analysis, payment plan management, and assistance program eligibility
for municipal utility departments.

Version 1.1.0 adds evidence-derived smart-meter analysis, leak adjustments,
eligibility screening, assistance enrollment, repair scheduling, and customer
resolution capabilities. Existing operations remain unchanged; new write
operations return deterministic simulated receipts and never modify an
external system.
"""

import sys
import os
import re

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/utility_billing_assistance",
    "version": "1.1.1",
    "display_name": "Utility Billing Assistance Agent",
    "description": "Answers utility billing inquiries, analyzes usage, and sets up payment plans and assistance eligibility from built-in demo data.",
    "author": "AIBAST",
    "tags": ["utility", "billing", "water", "payment", "assistance", "municipal", "leak-detection", "smart-meter"],
    "category": "slg_government",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# ---------------------------------------------------------------------------
# Synthetic domain data
# ---------------------------------------------------------------------------

UTILITY_ACCOUNTS = {
    "ACCT-90001": {
        "customer": "Patricia Hernandez",
        "address": "1245 Cedar Lane",
        "account_type": "residential",
        "services": ["water", "sewer", "stormwater"],
        "status": "active",
        "balance_current": 127.45,
        "balance_past_due": 0.00,
        "autopay": True,
        "last_payment": {"date": "2025-02-15", "amount": 118.90},
    },
    "ACCT-90002": {
        "customer": "Green Valley Shopping Center",
        "address": "5600 Commerce Blvd",
        "account_type": "commercial",
        "services": ["water", "sewer", "stormwater", "fire_line"],
        "status": "active",
        "balance_current": 2845.60,
        "balance_past_due": 1420.30,
        "autopay": False,
        "last_payment": {"date": "2025-01-20", "amount": 2650.00},
    },
    "ACCT-90003": {
        "customer": "Robert & Linda Thompson",
        "address": "887 Willow Creek Dr",
        "account_type": "residential",
        "services": ["water", "sewer", "stormwater", "trash"],
        "status": "delinquent",
        "balance_current": 245.80,
        "balance_past_due": 489.20,
        "autopay": False,
        "last_payment": {"date": "2024-11-18", "amount": 135.00},
    },
    "ACCT-90004": {
        "customer": "Sunnyvale Elementary School",
        "address": "300 Education Way",
        "account_type": "institutional",
        "services": ["water", "sewer", "stormwater", "irrigation"],
        "status": "active",
        "balance_current": 1890.25,
        "balance_past_due": 0.00,
        "autopay": True,
        "last_payment": {"date": "2025-02-28", "amount": 1756.00},
    },
}

USAGE_HISTORY = {
    "ACCT-90001": [
        {"period": "2024-09", "water_gallons": 4200, "sewer_gallons": 3780, "amount": 98.50},
        {"period": "2024-10", "water_gallons": 3800, "sewer_gallons": 3420, "amount": 92.10},
        {"period": "2024-11", "water_gallons": 3100, "sewer_gallons": 2790, "amount": 84.30},
        {"period": "2024-12", "water_gallons": 2900, "sewer_gallons": 2610, "amount": 81.20},
        {"period": "2025-01", "water_gallons": 3000, "sewer_gallons": 2700, "amount": 82.90},
        {"period": "2025-02", "water_gallons": 3200, "sewer_gallons": 2880, "amount": 86.45},
    ],
    "ACCT-90003": [
        {"period": "2024-09", "water_gallons": 8500, "sewer_gallons": 7650, "amount": 145.20},
        {"period": "2024-10", "water_gallons": 9200, "sewer_gallons": 8280, "amount": 152.80},
        {"period": "2024-11", "water_gallons": 12400, "sewer_gallons": 11160, "amount": 198.50},
        {"period": "2024-12", "water_gallons": 14800, "sewer_gallons": 13320, "amount": 232.10},
        {"period": "2025-01", "water_gallons": 13200, "sewer_gallons": 11880, "amount": 215.40},
        {"period": "2025-02", "water_gallons": 11500, "sewer_gallons": 10350, "amount": 189.80},
    ],
}

RATE_STRUCTURES = {
    "water_residential": {
        "base_charge": 18.50,
        "tiers": [
            {"range": "0-3,000 gal", "rate_per_1000": 4.25},
            {"range": "3,001-6,000 gal", "rate_per_1000": 6.50},
            {"range": "6,001-10,000 gal", "rate_per_1000": 9.75},
            {"range": "Over 10,000 gal", "rate_per_1000": 14.00},
        ],
    },
    "water_commercial": {
        "base_charge": 45.00,
        "tiers": [
            {"range": "0-10,000 gal", "rate_per_1000": 5.80},
            {"range": "10,001-50,000 gal", "rate_per_1000": 5.25},
            {"range": "Over 50,000 gal", "rate_per_1000": 4.90},
        ],
    },
    "sewer": {"base_charge": 12.75, "rate_per_1000": 5.10},
    "stormwater": {"residential": 8.50, "commercial_per_eru": 8.50},
    "trash": {"residential": 22.00},
}

ASSISTANCE_PROGRAMS = {
    "LIHWAP": {
        "name": "Low-Income Household Water Assistance Program",
        "income_limit_pct_fpl": 150,
        "max_benefit": 1500,
        "eligibility": "Household income at or below 150% FPL",
        "documents_required": ["Proof of income", "Utility bill", "ID", "Household size verification"],
        "status": "accepting_applications",
    },
    "senior_discount": {
        "name": "Senior Citizen Rate Discount",
        "income_limit_pct_fpl": 200,
        "max_benefit": 0,
        "eligibility": "Age 65+ and income at or below 200% FPL",
        "documents_required": ["Proof of age", "Proof of income", "Utility account number"],
        "status": "accepting_applications",
        "discount_pct": 25,
    },
    "arrearage_forgiveness": {
        "name": "COVID-19 Arrearage Forgiveness Program",
        "income_limit_pct_fpl": 200,
        "max_benefit": 3000,
        "eligibility": "Past-due balance accrued during March 2020 - December 2023",
        "documents_required": ["Utility account statement", "Income verification"],
        "status": "limited_funds",
    },
    "payment_plan": {
        "name": "Extended Payment Arrangement",
        "income_limit_pct_fpl": 0,
        "max_benefit": 0,
        "eligibility": "Any customer with past-due balance over $100",
        "documents_required": ["Signed payment agreement"],
        "status": "always_available",
        "max_installments": 12,
    },
}

EVIDENCE_CAPABILITIES = {
    "smart_meter_analysis": {
        "display_name": "Smart Meter Anomaly and Leak Analysis",
        "source_system": "Dynamics 365 CRM and utility meter data",
        "key_field": "analysis_id",
        "write": False,
        "knowledge": [
            "Compares current consumption with the account's historical baseline.",
            "Uses hourly smart-meter readings to locate concentrated usage anomalies.",
            "Identifies leak-consistent patterns and explains the likely cause.",
        ],
        "records": [
            {
                "analysis_id": "METER-RES-782MD",
                "account_id": "RES-782MD",
                "current_usage": "22,000 gallons",
                "baseline_usage": "4,500 gallons",
                "increase": "389%",
                "anomaly_window": "March 10-13; 182 gallons/hour",
                "diagnosis": "Internal leak, likely toilet flapper",
            },
            {
                "analysis_id": "METER-ACCT-90001",
                "account_id": "ACCT-90001",
                "current_usage": "3,200 gallons",
                "baseline_usage": "3,400 gallons",
                "increase": "-6%",
                "anomaly_window": "None",
                "diagnosis": "Stable usage",
            },
            {
                "analysis_id": "METER-ACCT-90003",
                "account_id": "ACCT-90003",
                "current_usage": "11,500 gallons",
                "baseline_usage": "8,500 gallons",
                "increase": "35%",
                "anomaly_window": "Overnight continuous flow",
                "diagnosis": "Possible fixture leak",
            },
        ],
    },
    "leak_adjustment": {
        "display_name": "Municipal Leak Adjustment",
        "source_system": "Municipal billing system",
        "key_field": "adjustment_id",
        "write": True,
        "knowledge": [
            "Applies municipal policy consistently to excess consumption.",
            "Calculates water-only charges, sewer waivers, credits, and the revised bill.",
            "Creates a full audit trail and states repair-proof requirements.",
        ],
        "records": [
            {
                "adjustment_id": "ADJ-RES-782MD",
                "account_id": "RES-782MD",
                "policy": "Municipal Code 18.42 one-time leak adjustment",
                "excess_volume": "17,500 gallons",
                "credit": "$97.80",
                "new_bill": "$86.70",
                "condition": "Proof of repair within 30 days",
            },
            {
                "adjustment_id": "ADJ-ACCT-90003",
                "account_id": "ACCT-90003",
                "policy": "Residential verified-leak adjustment",
                "excess_volume": "3,000 gallons",
                "credit": "$28.35",
                "new_bill": "$217.45",
                "condition": "Licensed repair invoice within 30 days",
            },
            {
                "adjustment_id": "ADJ-ACCT-90002",
                "account_id": "ACCT-90002",
                "policy": "Commercial anomaly review",
                "excess_volume": "Pending verification",
                "credit": "$0.00",
                "new_bill": "$4,265.90",
                "condition": "Meter inspection required",
            },
        ],
    },
    "assistance_eligibility": {
        "display_name": "Assistance Eligibility Screening",
        "source_system": "Dynamics 365 CRM and assistance program rules",
        "key_field": "screening_id",
        "write": False,
        "knowledge": [
            "Screens household income against municipal and emergency assistance rules.",
            "Surfaces available credits, grants, discounts, and payment-plan options.",
            "Explains qualification and total potential financial relief.",
        ],
        "records": [
            {
                "screening_id": "SCREEN-RES-782MD",
                "account_id": "RES-782MD",
                "income": "$32,400 (68% AMI)",
                "eligible_programs": "LIWAP; LIHEAP emergency fund; 6-month payment plan",
                "potential_relief": "$350",
                "decision": "Qualifies",
            },
            {
                "screening_id": "SCREEN-ACCT-90003",
                "account_id": "ACCT-90003",
                "income": "142% FPL",
                "eligible_programs": "LIHWAP; extended payment arrangement",
                "potential_relief": "Up to $1,500",
                "decision": "Qualifies",
            },
            {
                "screening_id": "SCREEN-ACCT-90001",
                "account_id": "ACCT-90001",
                "income": "Not supplied",
                "eligible_programs": "Extended payment arrangement",
                "potential_relief": "Payment flexibility",
                "decision": "Income documentation required for other programs",
            },
        ],
    },
    "assistance_enrollment": {
        "display_name": "Payment Plan and Assistance Enrollment",
        "source_system": "Municipal billing system and customer portal",
        "key_field": "enrollment_id",
        "write": True,
        "knowledge": [
            "Configures a payment plan and initiates program enrollment in one workflow.",
            "Pre-fills application forms and lists the required income and residency documents.",
            "Sends forms with a portal link and a deterministic response deadline.",
        ],
        "records": [
            {
                "enrollment_id": "ENROLL-RES-782MD",
                "account_id": "RES-782MD",
                "payment_plan": "6 months at $14.45; 0% interest",
                "program": "LIWAP",
                "documents": "Pay stubs or tax return; lease or property deed",
                "deadline": "14 days",
                "status": "Application pre-filled",
            },
            {
                "enrollment_id": "ENROLL-ACCT-90003",
                "account_id": "ACCT-90003",
                "payment_plan": "12 months at $40.77",
                "program": "LIHWAP",
                "documents": "Proof of income; utility bill; ID; household size",
                "deadline": "14 days",
                "status": "Application pre-filled",
            },
            {
                "enrollment_id": "ENROLL-ACCT-90002",
                "account_id": "ACCT-90002",
                "payment_plan": "6 months at $236.72",
                "program": "Extended Payment Arrangement",
                "documents": "Signed payment agreement",
                "deadline": "10 days",
                "status": "Agreement generated",
            },
        ],
    },
    "repair_scheduling": {
        "display_name": "Conservation Repair Scheduling",
        "source_system": "Municipal field service schedule",
        "key_field": "repair_id",
        "write": True,
        "knowledge": [
            "Matches eligible residents with city-certified repair providers.",
            "Schedules a repair window and lists included conservation equipment.",
            "States program value and expected water savings.",
        ],
        "records": [
            {
                "repair_id": "REPAIR-RES-782MD",
                "account_id": "RES-782MD",
                "appointment": "Tuesday, April 2, 1:00-3:00 PM",
                "provider": "City Maintenance licensed plumber",
                "services": "Toilet flapper; faucet aerators; leak detection tablets; low-flow showerhead",
                "program_value": "$85",
                "estimated_savings": "6,000 gallons/month",
            },
            {
                "repair_id": "REPAIR-ACCT-90003",
                "account_id": "ACCT-90003",
                "appointment": "Thursday, April 4, 9:00-11:00 AM",
                "provider": "City Conservation Crew",
                "services": "Fixture inspection; leak repair kit",
                "program_value": "$75",
                "estimated_savings": "3,000 gallons/month",
            },
            {
                "repair_id": "REPAIR-ACCT-90001",
                "account_id": "ACCT-90001",
                "appointment": "Friday, April 5, 1:00-3:00 PM",
                "provider": "City Conservation Crew",
                "services": "Efficiency audit; faucet aerators",
                "program_value": "$40",
                "estimated_savings": "500 gallons/month",
            },
        ],
    },
    "resolution_summary": {
        "display_name": "Customer Resolution and Account Update",
        "source_system": "Dynamics 365 CRM and Microsoft Outlook",
        "key_field": "resolution_id",
        "write": True,
        "knowledge": [
            "Packages credits, payment plans, enrollment, and repair actions into one resolution.",
            "Updates the synthetic account audit summary and schedules follow-up.",
            "Creates a transparent customer communication for Outlook and portal delivery.",
        ],
        "records": [
            {
                "resolution_id": "RESOLVE-RES-782MD",
                "account_id": "RES-782MD",
                "actions": "$97.80 credit; payment plan; LIWAP pending; LIHEAP info; repair scheduled",
                "delivery": "Outlook email and postal mail",
                "follow_up": "30 days",
                "total_relief": "$347.80 plus future leak savings",
            },
            {
                "resolution_id": "RESOLVE-ACCT-90003",
                "account_id": "ACCT-90003",
                "actions": "$28.35 credit; payment plan; LIHWAP pending; repair scheduled",
                "delivery": "Outlook email and customer portal",
                "follow_up": "30 days",
                "total_relief": "Up to $1,528.35",
            },
            {
                "resolution_id": "RESOLVE-ACCT-90002",
                "account_id": "ACCT-90002",
                "actions": "Payment agreement generated; meter inspection requested",
                "delivery": "Outlook email",
                "follow_up": "10 days",
                "total_relief": "Pending inspection",
            },
        ],
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _calculate_water_bill(gallons, account_type):
    """Calculate water charges based on tiered rate structure."""
    if account_type == "commercial":
        rate_info = RATE_STRUCTURES["water_commercial"]
    else:
        rate_info = RATE_STRUCTURES["water_residential"]
    total = rate_info["base_charge"]
    remaining = gallons
    for tier in rate_info["tiers"]:
        range_str = tier["range"]
        if range_str.startswith("Over"):
            total += (remaining / 1000) * tier["rate_per_1000"]
            remaining = 0
        else:
            parts = range_str.replace(",", "").replace(" gal", "").split("-")
            low = int(parts[0])
            high = int(parts[1])
            tier_volume = min(remaining, high - low + 1)
            if tier_volume > 0:
                total += (tier_volume / 1000) * tier["rate_per_1000"]
                remaining -= tier_volume
        if remaining <= 0:
            break
    return round(total, 2)


def _usage_trend(account_id):
    """Analyze usage trend for an account."""
    history = USAGE_HISTORY.get(account_id, [])
    if len(history) < 2:
        return "insufficient_data"
    recent = history[-1]["water_gallons"]
    previous_avg = sum(h["water_gallons"] for h in history[:-1]) / (len(history) - 1)
    if recent > previous_avg * 1.20:
        return "significantly_increasing"
    elif recent > previous_avg * 1.05:
        return "slightly_increasing"
    elif recent < previous_avg * 0.80:
        return "significantly_decreasing"
    elif recent < previous_avg * 0.95:
        return "slightly_decreasing"
    return "stable"


def _evidence_capability(operation_name, **kwargs):
    """Return an offline capability summary or an exact synthetic record."""
    capability = EVIDENCE_CAPABILITIES[operation_name]
    key_field = capability["key_field"]
    selector = str(kwargs.get(key_field) or kwargs.get("key") or "").strip()
    user_input = str(kwargs.get("user_input", "")).strip()
    input_tokens = {
        token.casefold()
        for token in re.findall(r"[A-Za-z0-9]+(?:[-_][A-Za-z0-9]+)*", user_input)
    }

    record = None
    for candidate in capability["records"]:
        candidate_key = str(candidate[key_field])
        normalized_key = candidate_key.casefold()
        if selector and normalized_key == selector.casefold():
            record = candidate
            break
        if not selector and user_input and normalized_key in input_tokens:
            record = candidate
            break

    if selector or user_input:
        if record is None:
            available = ", ".join(str(item[key_field]) for item in capability["records"])
            return f"**Error:** No {key_field.replace('_', ' ')} matched. Available keys: {available}."
        lines = [f"# {capability['display_name']}: {record[key_field]}\n"]
        for field, value in record.items():
            lines.append(f"- **{field.replace('_', ' ').title()}:** {value}")
        lines.append(f"- **Source System:** {capability['source_system']}")
        if capability["write"]:
            lines.extend([
                "\n## Simulated Write Receipt\n",
                f"- **Receipt:** SIM-{operation_name.upper()}-{record[key_field]}",
                f"- **Action:** {capability['display_name']}",
                "- **Result:** Simulated only; no external system was modified.",
            ])
        return "\n".join(lines)

    lines = [f"# {capability['display_name']}\n"]
    lines.append(f"**Mode:** {'Simulated write' if capability['write'] else 'Read-only'}")
    lines.append(f"**Source System:** {capability['source_system']}\n")
    lines.append("## Capability\n")
    lines.extend(f"- {item}" for item in capability["knowledge"])
    lines.append("\n## Available Records\n")
    for item in capability["records"]:
        lines.append(f"- `{item[key_field]}`")
    lines.append(f"\nProvide `{key_field}` or `key` for an exact offline lookup.")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class UtilityBillingAssistanceAgent(BasicAgent):
    """Municipal utility billing assistance agent."""

    def __init__(self):
        self.name = "UtilityBillingAssistanceAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Utility Billing Assistance Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "billing_inquiry",
                            "usage_analysis",
                            "payment_plan",
                            "assistance_programs",
                            "smart_meter_analysis",
                            "leak_adjustment",
                            "assistance_eligibility",
                            "assistance_enrollment",
                            "repair_scheduling",
                            "resolution_summary",
                        ],
                    },
                    "account_id": {"type": "string"},
                    "key": {
                        "type": "string",
                        "description": "Exact record key advertised by the selected evidence operation.",
                    },
                    "user_input": {
                        "type": "string",
                        "description": "Natural-language request containing an exact advertised record key.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "billing_inquiry")
        dispatch = {
            "billing_inquiry": self._billing_inquiry,
            "usage_analysis": self._usage_analysis,
            "payment_plan": self._payment_plan,
            "assistance_programs": self._assistance_programs,
        }
        if operation in EVIDENCE_CAPABILITIES:
            return _evidence_capability(operation, **kwargs)
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        return handler(**kwargs)

    def _billing_inquiry(self, **kwargs) -> str:
        account_id = kwargs.get("account_id")
        if account_id and account_id in UTILITY_ACCOUNTS:
            acct = UTILITY_ACCOUNTS[account_id]
            total_due = acct["balance_current"] + acct["balance_past_due"]
            lines = [f"# Billing Inquiry: {account_id}\n"]
            lines.append(f"- **Customer:** {acct['customer']}")
            lines.append(f"- **Address:** {acct['address']}")
            lines.append(f"- **Account Type:** {acct['account_type'].title()}")
            lines.append(f"- **Services:** {', '.join(s.replace('_', ' ').title() for s in acct['services'])}")
            lines.append(f"- **Status:** {acct['status'].title()}")
            lines.append(f"- **Current Charges:** ${acct['balance_current']:,.2f}")
            lines.append(f"- **Past Due:** ${acct['balance_past_due']:,.2f}")
            lines.append(f"- **Total Due:** ${total_due:,.2f}")
            lines.append(f"- **Auto-Pay:** {'Yes' if acct['autopay'] else 'No'}")
            lines.append(f"- **Last Payment:** ${acct['last_payment']['amount']:,.2f} on {acct['last_payment']['date']}")
            return "\n".join(lines)

        lines = ["# Utility Accounts Summary\n"]
        lines.append("| Account | Customer | Type | Current | Past Due | Status |")
        lines.append("|---|---|---|---|---|---|")
        for aid, acct in UTILITY_ACCOUNTS.items():
            lines.append(
                f"| {aid} | {acct['customer']} | {acct['account_type'].title()} "
                f"| ${acct['balance_current']:,.2f} | ${acct['balance_past_due']:,.2f} | {acct['status'].title()} |"
            )
        total_ar = sum(a["balance_current"] + a["balance_past_due"] for a in UTILITY_ACCOUNTS.values())
        lines.append(f"\n**Total Accounts Receivable:** ${total_ar:,.2f}")
        return "\n".join(lines)

    def _usage_analysis(self, **kwargs) -> str:
        account_id = kwargs.get("account_id", "ACCT-90001")
        history = USAGE_HISTORY.get(account_id, [])
        acct = UTILITY_ACCOUNTS.get(account_id, {})
        trend = _usage_trend(account_id)
        lines = [f"# Usage Analysis: {account_id}\n"]
        lines.append(f"**Customer:** {acct.get('customer', 'Unknown')}")
        lines.append(f"**Usage Trend:** {trend.replace('_', ' ').title()}\n")
        if history:
            lines.append("| Period | Water (gal) | Sewer (gal) | Amount |")
            lines.append("|---|---|---|---|")
            for h in history:
                lines.append(f"| {h['period']} | {h['water_gallons']:,} | {h['sewer_gallons']:,} | ${h['amount']:,.2f} |")
            avg_water = sum(h["water_gallons"] for h in history) / len(history)
            avg_bill = sum(h["amount"] for h in history) / len(history)
            lines.append(f"\n**Avg Monthly Water Usage:** {avg_water:,.0f} gallons")
            lines.append(f"**Avg Monthly Bill:** ${avg_bill:,.2f}")
        lines.append("\n## Rate Structure\n")
        for rate_name, rate_info in RATE_STRUCTURES.items():
            lines.append(f"### {rate_name.replace('_', ' ').title()}\n")
            if isinstance(rate_info, dict) and "tiers" in rate_info:
                lines.append(f"Base Charge: ${rate_info['base_charge']:,.2f}\n")
                for tier in rate_info["tiers"]:
                    lines.append(f"- {tier['range']}: ${tier['rate_per_1000']:,.2f}/1,000 gal")
            elif isinstance(rate_info, dict) and "base_charge" in rate_info:
                lines.append(f"Base: ${rate_info['base_charge']:,.2f}, Rate: ${rate_info.get('rate_per_1000', 0):,.2f}/1,000 gal")
            lines.append("")
        return "\n".join(lines)

    def _payment_plan(self, **kwargs) -> str:
        account_id = kwargs.get("account_id", "ACCT-90003")
        acct = UTILITY_ACCOUNTS.get(account_id, list(UTILITY_ACCOUNTS.values())[2])
        past_due = acct["balance_past_due"]
        lines = [f"# Payment Plan Options: {account_id}\n"]
        lines.append(f"**Customer:** {acct['customer']}")
        lines.append(f"**Past Due Balance:** ${past_due:,.2f}\n")
        if past_due > 0:
            lines.append("## Installment Options\n")
            lines.append("| Installments | Monthly Payment | Total |")
            lines.append("|---|---|---|")
            for months in [3, 6, 9, 12]:
                monthly = round(past_due / months, 2)
                lines.append(f"| {months} months | ${monthly:,.2f} | ${past_due:,.2f} |")
            lines.append("\n*Note: Current charges continue to accrue during payment plan.*\n")
        lines.append("## Payment Plan Requirements\n")
        pp = ASSISTANCE_PROGRAMS["payment_plan"]
        lines.append(f"- {pp['eligibility']}")
        lines.append(f"- Maximum installments: {pp['max_installments']}")
        lines.append(f"- Documents required: {', '.join(pp['documents_required'])}")
        return "\n".join(lines)

    def _assistance_programs(self, **kwargs) -> str:
        lines = ["# Utility Assistance Programs\n"]
        for prog_id, prog in ASSISTANCE_PROGRAMS.items():
            lines.append(f"## {prog['name']}\n")
            lines.append(f"- **Eligibility:** {prog['eligibility']}")
            if prog["max_benefit"] > 0:
                lines.append(f"- **Maximum Benefit:** ${prog['max_benefit']:,.0f}")
            if prog.get("discount_pct"):
                lines.append(f"- **Discount:** {prog['discount_pct']}%")
            lines.append(f"- **Status:** {prog['status'].replace('_', ' ').title()}")
            lines.append(f"- **Documents Required:**")
            for doc in prog["documents_required"]:
                lines.append(f"  - {doc}")
            lines.append("")
        lines.append("## Federal Poverty Level Reference (2025)\n")
        fpl_table = {1: 15650, 2: 21150, 3: 26650, 4: 32150, 5: 37650}
        lines.append("| Household Size | 100% FPL | 150% FPL | 200% FPL |")
        lines.append("|---|---|---|---|")
        for size, fpl in fpl_table.items():
            lines.append(f"| {size} | ${fpl:,} | ${int(fpl * 1.5):,} | ${fpl * 2:,} |")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = UtilityBillingAssistanceAgent()
    print(agent.perform(operation="billing_inquiry"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="billing_inquiry", account_id="ACCT-90002"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="usage_analysis", account_id="ACCT-90003"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="payment_plan", account_id="ACCT-90003"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="assistance_programs"))
