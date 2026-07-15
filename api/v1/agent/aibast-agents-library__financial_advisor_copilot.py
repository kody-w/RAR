"""
Financial Advisor Copilot Agent — Financial Services Stack

Assists financial advisors with client reviews, portfolio summaries,
investment recommendations, and compliance checks.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/financial_advisor_copilot",
    "version": "1.1.0",
    "display_name": "Financial Advisor Copilot Agent",
    "description": "Financial advisor support with client reviews, portfolio summaries, recommendation engine, compliance checks, and branch banking & advisory workflows (intake, product education, account opening, planning, advisor handoff).",
    "author": "AIBAST",
    "tags": ["advisor", "portfolio", "investment", "compliance", "financial-services", "branch-banking", "advisory"],
    "category": "financial_services",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# ---------------------------------------------------------------------------
# Synthetic domain data
# ---------------------------------------------------------------------------

CLIENT_PORTFOLIOS = {
    "CLI-3001": {
        "name": "Robert & Susan Whitfield",
        "advisor": "James Morrison, CFP",
        "risk_profile": "moderate",
        "age": 58,
        "retirement_target": 67,
        "total_assets": 1850000,
        "holdings": {
            "US Equities": {"value": 555000, "allocation": 30.0, "target": 35.0},
            "International Equities": {"value": 185000, "allocation": 10.0, "target": 15.0},
            "Fixed Income": {"value": 647500, "allocation": 35.0, "target": 30.0},
            "Real Estate (REITs)": {"value": 185000, "allocation": 10.0, "target": 10.0},
            "Alternatives": {"value": 92500, "allocation": 5.0, "target": 5.0},
            "Cash & Equivalents": {"value": 185000, "allocation": 10.0, "target": 5.0},
        },
        "annual_income": 285000,
        "annual_contributions": 45000,
        "last_review": "2024-12-15",
    },
    "CLI-3002": {
        "name": "Angela Martinez",
        "advisor": "James Morrison, CFP",
        "risk_profile": "aggressive",
        "age": 34,
        "retirement_target": 60,
        "total_assets": 420000,
        "holdings": {
            "US Equities": {"value": 210000, "allocation": 50.0, "target": 45.0},
            "International Equities": {"value": 84000, "allocation": 20.0, "target": 20.0},
            "Fixed Income": {"value": 42000, "allocation": 10.0, "target": 10.0},
            "Emerging Markets": {"value": 50400, "allocation": 12.0, "target": 15.0},
            "Alternatives": {"value": 21000, "allocation": 5.0, "target": 5.0},
            "Cash & Equivalents": {"value": 12600, "allocation": 3.0, "target": 5.0},
        },
        "annual_income": 145000,
        "annual_contributions": 24000,
        "last_review": "2025-01-20",
    },
    "CLI-3003": {
        "name": "William Chen Trust",
        "advisor": "Patricia Lane, CFA",
        "risk_profile": "conservative",
        "age": 72,
        "retirement_target": 0,
        "total_assets": 4200000,
        "holdings": {
            "US Equities": {"value": 630000, "allocation": 15.0, "target": 15.0},
            "International Equities": {"value": 210000, "allocation": 5.0, "target": 5.0},
            "Fixed Income": {"value": 1890000, "allocation": 45.0, "target": 45.0},
            "Municipal Bonds": {"value": 840000, "allocation": 20.0, "target": 20.0},
            "Real Estate (REITs)": {"value": 210000, "allocation": 5.0, "target": 5.0},
            "Cash & Equivalents": {"value": 420000, "allocation": 10.0, "target": 10.0},
        },
        "annual_income": 0,
        "annual_contributions": 0,
        "last_review": "2025-02-10",
    },
}

INVESTMENT_RECOMMENDATIONS = {
    "moderate": [
        {"action": "Rebalance to target allocation", "rationale": "Drift from target exceeds 3% in multiple asset classes"},
        {"action": "Reduce cash overweight", "rationale": "Excess cash drag on returns; deploy to equities"},
        {"action": "Increase international exposure", "rationale": "Underweight vs target; diversification benefit"},
    ],
    "aggressive": [
        {"action": "Increase emerging markets allocation", "rationale": "Below target; favorable long-term growth outlook"},
        {"action": "Consider small-cap tilt", "rationale": "Long time horizon supports higher-volatility allocations"},
        {"action": "Build cash reserve to target 5%", "rationale": "Slightly underweight cash for opportunistic rebalancing"},
    ],
    "conservative": [
        {"action": "Maintain current allocation", "rationale": "Portfolio aligned with targets; no rebalancing needed"},
        {"action": "Review bond duration", "rationale": "Consider shortening duration if rate hikes expected"},
        {"action": "Tax-loss harvesting review", "rationale": "Identify unrealized losses for year-end tax planning"},
    ],
}

COMPLIANCE_RULES = {
    "reg_bi": {"name": "Regulation Best Interest", "description": "Ensure recommendations are in client's best interest", "applies_to": "all"},
    "form_crs": {"name": "Form CRS Delivery", "description": "Relationship summary delivered at account opening and annually", "applies_to": "all"},
    "suitability": {"name": "Suitability Obligation", "description": "Investment recommendations suitable for client profile", "applies_to": "all"},
    "concentration_limit": {"name": "Concentration Limit", "description": "No single position exceeds 10% of portfolio", "applies_to": "all"},
    "senior_investor": {"name": "Senior Investor Protection", "description": "Enhanced protections for clients age 65+", "applies_to": "seniors"},
}


# ---------------------------------------------------------------------------
# Branch banking & advisory capabilities (v1.1.0)
#
# Five backward-compatible operations sourced from the
# branch-banking-advisory spec. Each capability carries its spec response,
# knowledge, exactly three synthetic records, an exact lookup key, and
# write/generative metadata. Operations support an optional `user_input`:
# supplying a record key performs an exact keyed lookup; omitting it returns
# a useful no-input summary of all records. Write capabilities emit a
# simulated receipt only — no live system mutation occurs.
# ---------------------------------------------------------------------------

BRANCH_BANKING_CAPABILITIES = {
    "branch_intake": {
        "name": "Branch Intake and Verification",
        "description": "Automates customer intake, identity verification, and service routing to coordinate branch check-in and balance team workloads.",
        "source_system": "Dynamics 365 CRM",
        "write": True,
        "generative": False,
        "key_field": "intake_id",
        "response": "I can check in the customer, confirm identity verification, and route them to the correct specialist.",
        "knowledge": [
            "The Financial Advisor Agent automates check-in, identity verification, and service routing (demo 00:00:45-00:00:49).",
            "Intake coordination improves service speed and balances team workloads for a mid-sized credit union (one-pager, Opportunity).",
            "Identity verification and routing remove slow, multi-system check-in steps that undermined trust and satisfaction (demo 00:00:16-00:00:26).",
        ],
        "records": [
            {"intake_id": "INT4101", "customer": "Marisol Vega", "branch": "Lakeshore Community Credit Union", "service": "Education savings consultation", "verification": "ID verified", "route_to": "Financial Advisor"},
            {"intake_id": "INT4102", "customer": "Darnell Brooks", "branch": "Lakeshore Community Credit Union", "service": "Loan inquiry", "verification": "Pending document", "route_to": "Loan Officer"},
            {"intake_id": "INT4103", "customer": "Priya Nair", "branch": "Riverbend Federal Credit Union", "service": "Account opening", "verification": "ID verified", "route_to": "Branch Banker"},
        ],
    },
    "advisory_education": {
        "name": "Advisory Product Education",
        "description": "Guides customers and bankers through advisory and product education, explaining plan basics, state benefits, contribution rules, and investment structures in plain language.",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": True,
        "key_field": "topic_id",
        "response": "I can explain the plan in plain language, including state benefits, contribution rules, and investment structures so it maps to your family's goals.",
        "knowledge": [
            "The agent walks a customer through 529 plan basics in plain language, state benefits, contribution rules, and investment structures (demo 00:01:08-00:01:16).",
            "Education helps a customer quickly see what matches her family's goals before meeting an advisor (demo 00:01:16-00:01:19).",
            "The credit union used the agent to guide bankers through account opening and investment services (one-pager, How the Agent helped).",
        ],
        "records": [
            {"topic_id": "EDU529", "topic": "529 plan basics", "summary": "Plain-language overview of 529 education savings plans", "state_benefit": "State tax deduction available", "contribution_rule": "Annual gift-tax exclusion applies", "audience": "Families"},
            {"topic_id": "EDUIRA", "topic": "Roth IRA basics", "summary": "Overview of Roth IRA saving and withdrawals", "state_benefit": "Tax-free qualified withdrawals", "contribution_rule": "Annual contribution limit applies", "audience": "Individuals"},
            {"topic_id": "EDUCUST", "topic": "Custodial account basics", "summary": "Overview of UTMA custodial accounts", "state_benefit": "Gift-tax considerations apply", "contribution_rule": "Irrevocable gift to the minor", "audience": "Parents"},
        ],
    },
    "account_opening": {
        "name": "Account Opening and Application",
        "description": "Opens accounts by preparing the application, autofilling information, and completing identity and eligibility checks to remove slow manual steps for the customer and advisor.",
        "source_system": "Dynamics 365 ERP",
        "write": True,
        "generative": False,
        "key_field": "application_id",
        "response": "I can prepare the application, autofill the information from the customer profile, and complete the identity and eligibility checks before submission.",
        "knowledge": [
            "The customer provides her details and asks the agent to open the 529 account (demo 00:01:29-00:01:34).",
            "The agent prepares the application, autofills information, and completes identity and eligibility checks (demo 00:01:35-00:01:42).",
            "Automating these steps removes slow manual steps for both the customer and the advisor (demo 00:01:42-00:01:46).",
        ],
        "records": [
            {"application_id": "APP529A", "customer": "Marisol Vega", "product": "529 education savings account", "autofill": "Completed from profile", "eligibility": "Passed identity and eligibility checks", "status": "Ready to submit"},
            {"application_id": "APP529B", "customer": "Priya Nair", "product": "529 education savings account", "autofill": "Partially completed", "eligibility": "Awaiting SSN confirmation", "status": "On hold"},
            {"application_id": "APPIRAC", "customer": "Darnell Brooks", "product": "Roth IRA account", "autofill": "Completed from profile", "eligibility": "Passed identity checks", "status": "Ready to submit"},
        ],
    },
    "financial_planning": {
        "name": "Financial Planning and Risk Assessment",
        "description": "Models future college costs, explores contribution scenarios, and provides a risk-aligned investment approach and research to support clarity without replacing professional guidance.",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": True,
        "key_field": "scenario_id",
        "response": "I can model future college costs, explore contribution scenarios, and suggest a risk-aligned approach for clarity, without replacing professional guidance.",
        "knowledge": [
            "When she has a planning question, the agent models future college costs and explores contribution scenarios (demo 00:01:46-00:01:54).",
            "With goals and time horizon captured, the agent provides a risk-aligned investment approach to consider, supporting clarity without replacing professional guidance (demo 00:02:01-00:02:10).",
            "The credit union used the agent to provide real-time risk assessments and financial research (one-pager, How the Agent helped).",
        ],
        "records": [
            {"scenario_id": "PLN18YR", "goal": "Fund a 4-year degree in 18 years", "projected_cost": "$180,000 projected", "monthly_contribution": "$450 monthly suggested", "risk_profile": "Moderate risk-aligned mix"},
            {"scenario_id": "PLN10YR", "goal": "Fund college in 10 years", "projected_cost": "$140,000 projected", "monthly_contribution": "$820 monthly suggested", "risk_profile": "Conservative risk-aligned mix"},
            {"scenario_id": "PLN05YR", "goal": "Fund tuition in 5 years", "projected_cost": "$90,000 projected", "monthly_contribution": "$1,300 monthly suggested", "risk_profile": "Low risk-aligned mix"},
        ],
    },
    "advisor_handoff": {
        "name": "Advisor Handoff and Follow-up Scheduling",
        "description": "Schedules a follow-up meeting with a specialist in Microsoft Teams and transfers case notes, risk data, and conversation history so the advisor has full context.",
        "source_system": "Dynamics 365 CRM",
        "write": True,
        "generative": False,
        "key_field": "handoff_id",
        "response": "I can schedule the follow-up meeting with the specialist in Microsoft Teams and transfer the case notes, risk data, and conversation history to the advisor.",
        "knowledge": [
            "To finish up, the agent schedules a follow-up meeting with an educational planning specialist in Microsoft Teams (demo 00:02:10-00:02:17).",
            "The agent passes along the full context to the advisor and helps the customer leave feeling supported and confident about next steps (demo 00:02:17-00:02:24).",
            "The credit union used the agent to transfer case notes, risk data, and conversation history to advisors (one-pager, How the Agent helped).",
        ],
        "records": [
            {"handoff_id": "HOFF7001", "customer": "Marisol Vega", "specialist": "Education Planning Specialist", "meeting": "Microsoft Teams follow-up scheduled", "context": "Case notes and risk data transferred"},
            {"handoff_id": "HOFF7002", "customer": "Darnell Brooks", "specialist": "Lending Specialist", "meeting": "Microsoft Teams follow-up scheduled", "context": "Loan inquiry context transferred"},
            {"handoff_id": "HOFF7003", "customer": "Priya Nair", "specialist": "Retirement Specialist", "meeting": "Microsoft Teams follow-up pending", "context": "Investment profile transferred"},
        ],
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _field_label(field):
    """Human-readable label for a record field name."""
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


def _match_record(capability, user_input):
    """Return the uniquely matched record for a complete normalized key."""
    if not user_input:
        return None
    key_field = capability["key_field"]
    matches = [
        record for record in capability["records"]
        if _contains_normalized_key(user_input, record[key_field])
    ]
    return matches[0] if len(matches) == 1 else None

def _allocation_drift(holdings):
    """Calculate max allocation drift from target."""
    max_drift = 0
    for asset, data in holdings.items():
        drift = abs(data["allocation"] - data["target"])
        if drift > max_drift:
            max_drift = drift
    return round(max_drift, 1)


def _years_to_retirement(client):
    """Calculate years remaining to retirement."""
    if client["retirement_target"] == 0:
        return 0
    return max(0, client["retirement_target"] - client["age"])


def _compliance_flags(client):
    """Check for compliance issues."""
    flags = []
    for asset, data in client["holdings"].items():
        if data["allocation"] > 50:
            flags.append(f"Concentration risk: {asset} at {data['allocation']}%")
    if client["age"] >= 65:
        flags.append("Senior investor protections apply")
    drift = _allocation_drift(client["holdings"])
    if drift > 5:
        flags.append(f"Allocation drift of {drift}% exceeds threshold")
    return flags


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class FinancialAdvisorCopilotAgent(BasicAgent):
    """Financial advisor copilot agent."""

    def __init__(self):
        self.name = "FinancialAdvisorCopilotAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Financial Advisor Copilot Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "client_review",
                            "portfolio_summary",
                            "recommendation_engine",
                            "compliance_check",
                            "branch_intake",
                            "advisory_education",
                            "account_opening",
                            "financial_planning",
                            "advisor_handoff",
                        ],
                    },
                    "client_id": {"type": "string"},
                    "user_input": {
                        "type": "string",
                        "description": "Optional free-text request. Include a record key (e.g. INT4101, EDU529, APP529A, PLN18YR, HOFF7001) for an exact keyed lookup; omit for a summary of all records.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "client_review")
        dispatch = {
            "client_review": self._client_review,
            "portfolio_summary": self._portfolio_summary,
            "recommendation_engine": self._recommendation_engine,
            "compliance_check": self._compliance_check,
        }
        handler = dispatch.get(operation)
        if handler:
            return handler(**kwargs)
        if operation in BRANCH_BANKING_CAPABILITIES:
            return self._branch_capability(**kwargs)
        return f"**Error:** Unknown operation `{operation}`."

    def _client_review(self, **kwargs) -> str:
        lines = ["# Client Review Summary\n"]
        lines.append("| Client | Advisor | Risk | Assets | Age | Retirement In | Last Review |")
        lines.append("|---|---|---|---|---|---|---|")
        for cid, c in CLIENT_PORTFOLIOS.items():
            yrs = _years_to_retirement(c)
            ret_str = f"{yrs} yrs" if yrs > 0 else "Retired"
            lines.append(
                f"| {c['name']} ({cid}) | {c['advisor']} | {c['risk_profile'].title()} "
                f"| ${c['total_assets']:,.0f} | {c['age']} | {ret_str} | {c['last_review']} |"
            )
        total_aum = sum(c["total_assets"] for c in CLIENT_PORTFOLIOS.values())
        lines.append(f"\n**Total AUM:** ${total_aum:,.0f}")
        lines.append(f"**Clients:** {len(CLIENT_PORTFOLIOS)}")
        return "\n".join(lines)

    def _portfolio_summary(self, **kwargs) -> str:
        client_id = kwargs.get("client_id", "CLI-3001")
        client = CLIENT_PORTFOLIOS.get(client_id, list(CLIENT_PORTFOLIOS.values())[0])
        drift = _allocation_drift(client["holdings"])
        lines = [f"# Portfolio Summary: {client['name']}\n"]
        lines.append(f"- **Risk Profile:** {client['risk_profile'].title()}")
        lines.append(f"- **Total Assets:** ${client['total_assets']:,.0f}")
        lines.append(f"- **Annual Contributions:** ${client['annual_contributions']:,.0f}")
        lines.append(f"- **Max Allocation Drift:** {drift}%\n")
        lines.append("## Holdings\n")
        lines.append("| Asset Class | Value | Current % | Target % | Drift |")
        lines.append("|---|---|---|---|---|")
        for asset, data in client["holdings"].items():
            d = round(data["allocation"] - data["target"], 1)
            sign = "+" if d > 0 else ""
            lines.append(
                f"| {asset} | ${data['value']:,.0f} | {data['allocation']}% "
                f"| {data['target']}% | {sign}{d}% |"
            )
        return "\n".join(lines)

    def _recommendation_engine(self, **kwargs) -> str:
        client_id = kwargs.get("client_id", "CLI-3001")
        client = CLIENT_PORTFOLIOS.get(client_id, list(CLIENT_PORTFOLIOS.values())[0])
        recs = INVESTMENT_RECOMMENDATIONS.get(client["risk_profile"], [])
        lines = [f"# Investment Recommendations: {client['name']}\n"]
        lines.append(f"**Risk Profile:** {client['risk_profile'].title()}")
        lines.append(f"**Years to Retirement:** {_years_to_retirement(client) or 'Retired'}\n")
        lines.append("## Recommendations\n")
        for i, rec in enumerate(recs, 1):
            lines.append(f"### {i}. {rec['action']}\n")
            lines.append(f"**Rationale:** {rec['rationale']}\n")
        lines.append("## Rebalancing Trades\n")
        lines.append("| Asset Class | Current | Target | Action | Est. Amount |")
        lines.append("|---|---|---|---|---|")
        for asset, data in client["holdings"].items():
            diff_pct = data["target"] - data["allocation"]
            if abs(diff_pct) >= 1.0:
                amount = abs(diff_pct / 100 * client["total_assets"])
                action = "Buy" if diff_pct > 0 else "Sell"
                lines.append(f"| {asset} | {data['allocation']}% | {data['target']}% | {action} | ${amount:,.0f} |")
        return "\n".join(lines)

    def _compliance_check(self, **kwargs) -> str:
        lines = ["# Compliance Check Report\n"]
        lines.append("## Regulatory Requirements\n")
        lines.append("| Rule | Description | Applies To |")
        lines.append("|---|---|---|")
        for rule_id, rule in COMPLIANCE_RULES.items():
            lines.append(f"| {rule['name']} | {rule['description']} | {rule['applies_to'].title()} |")
        lines.append("\n## Client Compliance Status\n")
        for cid, c in CLIENT_PORTFOLIOS.items():
            flags = _compliance_flags(c)
            status = "Issues Found" if flags else "Compliant"
            lines.append(f"### {c['name']} ({cid}) — {status}\n")
            if flags:
                for f in flags:
                    lines.append(f"- **Flag:** {f}")
            else:
                lines.append("- No compliance issues detected")
            lines.append("")
        return "\n".join(lines)

    # -- Branch banking & advisory operations (v1.1.0) --------------------

    def _branch_capability(self, **kwargs) -> str:
        operation = kwargs.get("operation")
        capability = BRANCH_BANKING_CAPABILITIES[operation]
        user_input = (kwargs.get("user_input") or "").strip()
        record = _match_record(capability, user_input)
        if record is not None:
            return self._capability_detail(capability, record)
        if user_input:
            return (
                f"# {capability['name']}\n\n"
                f"No exact normalized `{capability['key_field']}` matched the request."
            )
        return self._capability_summary(capability)

    def _metadata_block(self, capability) -> str:
        return (
            f"**Source System:** {capability['source_system']}  |  "
            f"**Write:** {'Yes' if capability['write'] else 'No'}  |  "
            f"**Generative:** {'Yes' if capability['generative'] else 'No'}"
        )

    def _knowledge_block(self, capability) -> list:
        lines = ["## Knowledge\n"]
        for item in capability["knowledge"]:
            lines.append(f"- {item}")
        return lines

    def _write_receipt(self, capability, record) -> str:
        key = record[capability["key_field"]]
        return "\n".join([
            "## Simulated Write Receipt\n",
            f"- **Receipt ID:** SIM-{key}",
            f"- **Target System:** {capability['source_system']}",
            f"- **Reference Key:** {key}",
            "- **Status:** Simulated — no live system mutation performed",
        ])

    def _capability_detail(self, capability, record) -> str:
        key_field = capability["key_field"]
        lines = [f"# {capability['name']}\n"]
        lines.append(capability["response"] + "\n")
        lines.append(f"## Record: {record[key_field]}\n")
        for field, value in record.items():
            lines.append(f"- **{_field_label(field)}:** {value}")
        lines.append("")
        lines.append(self._metadata_block(capability))
        lines.append("")
        lines.extend(self._knowledge_block(capability))
        if capability["write"]:
            lines.append("")
            lines.append(self._write_receipt(capability, record))
        return "\n".join(lines)

    def _capability_summary(self, capability) -> str:
        records = capability["records"]
        key_field = capability["key_field"]
        lines = [f"# {capability['name']}\n"]
        lines.append(capability["response"] + "\n")
        lines.append(f"_No record key supplied — showing all {len(records)} records._\n")
        headers = list(records[0].keys())
        lines.append("| " + " | ".join(_field_label(h) for h in headers) + " |")
        lines.append("|" + "---|" * len(headers))
        for record in records:
            lines.append("| " + " | ".join(str(record[h]) for h in headers) + " |")
        lines.append("")
        lines.append(self._metadata_block(capability))
        lines.append("")
        lines.extend(self._knowledge_block(capability))
        lines.append("")
        if capability["write"]:
            lines.append(
                f"_Provide a {_field_label(key_field)} to generate a simulated write "
                f"receipt (no live mutation)._"
            )
        else:
            lines.append(
                f"_Provide a {_field_label(key_field)} for an exact keyed lookup of a single record._"
            )
        return "\n".join(lines)

if __name__ == "__main__":
    agent = FinancialAdvisorCopilotAgent()
    print(agent.perform(operation="client_review"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="portfolio_summary", client_id="CLI-3001"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="recommendation_engine", client_id="CLI-3002"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="compliance_check"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="branch_intake", user_input="Check in intake INT4101 and route the customer"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="advisory_education", user_input="Explain topic EDU529 for a family"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="account_opening", user_input="Open the account for application APP529A"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="financial_planning", user_input="Model scenario PLN18YR"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="advisor_handoff"))
