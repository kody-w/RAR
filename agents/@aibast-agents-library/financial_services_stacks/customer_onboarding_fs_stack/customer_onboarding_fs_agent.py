"""
Financial Services Customer Onboarding Agent — Financial Services Stack

Manages KYC verification, account setup, document checklists, and
onboarding status tracking for financial institution customer onboarding.

Version 1.1.0 adds evidence-derived, data-driven onboarding capabilities
(identity verification, compliance screening, document collection, account
provisioning, and the onboarding timeline) as backward-compatible operations
routed through a deterministic keyed-lookup helper. All prior operations and
their behavior are preserved unchanged.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/fs_customer_onboarding",
    "version": "1.1.1",
    "display_name": "FS Customer Onboarding Agent",
    "description": "Guides bank customer onboarding with KYC checks, document checklists, and status tracking using built-in demo data.",
    "author": "AIBAST",
    "tags": ["KYC", "onboarding", "account-setup", "compliance", "financial-services", "identity-verification", "sanctions-screening", "account-provisioning"],
    "category": "financial_services",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# ---------------------------------------------------------------------------
# Synthetic domain data
# ---------------------------------------------------------------------------

CUSTOMER_APPLICATIONS = {
    "APP-6001": {
        "applicant": "Sarah Chen",
        "application_type": "individual",
        "account_requested": "premium_checking",
        "submitted": "2025-02-20",
        "status": "kyc_in_progress",
        "risk_rating": "low",
        "relationship_manager": "Michael Torres",
        "estimated_assets": 250000,
    },
    "APP-6002": {
        "applicant": "Blackwood Capital Partners LLC",
        "application_type": "business",
        "account_requested": "commercial_checking",
        "submitted": "2025-02-25",
        "status": "document_review",
        "risk_rating": "medium",
        "relationship_manager": "Jessica Nguyen",
        "estimated_assets": 2400000,
    },
    "APP-6003": {
        "applicant": "Ahmed Al-Rashid",
        "application_type": "individual",
        "account_requested": "wealth_management",
        "submitted": "2025-03-01",
        "status": "enhanced_due_diligence",
        "risk_rating": "high",
        "relationship_manager": "Jessica Nguyen",
        "estimated_assets": 5800000,
    },
    "APP-6004": {
        "applicant": "Maria Fontaine",
        "application_type": "individual",
        "account_requested": "basic_savings",
        "submitted": "2025-03-05",
        "status": "approved",
        "risk_rating": "low",
        "relationship_manager": "Michael Torres",
        "estimated_assets": 15000,
    },
}

KYC_DOCUMENTS = {
    "individual": [
        {"document": "Government-issued photo ID", "required": True},
        {"document": "Social Security Number verification", "required": True},
        {"document": "Proof of address (utility bill or bank statement)", "required": True},
        {"document": "W-9 Tax Form", "required": True},
        {"document": "Source of funds documentation", "required": False},
    ],
    "business": [
        {"document": "Articles of Incorporation / Formation", "required": True},
        {"document": "EIN verification letter", "required": True},
        {"document": "Certificate of Good Standing", "required": True},
        {"document": "Operating Agreement / Bylaws", "required": True},
        {"document": "Beneficial ownership declaration (FinCEN BOI)", "required": True},
        {"document": "Government ID for all authorized signers", "required": True},
        {"document": "Business license", "required": False},
        {"document": "Financial statements (last 2 years)", "required": False},
    ],
}

VERIFICATION_STATUS = {
    "APP-6001": {
        "id_verification": "complete",
        "ssn_verification": "complete",
        "address_verification": "pending",
        "ofac_screening": "clear",
        "pep_screening": "clear",
        "adverse_media": "clear",
    },
    "APP-6002": {
        "id_verification": "complete",
        "ein_verification": "complete",
        "beneficial_ownership": "in_progress",
        "ofac_screening": "clear",
        "pep_screening": "clear",
        "adverse_media": "clear",
    },
    "APP-6003": {
        "id_verification": "complete",
        "ssn_verification": "complete",
        "address_verification": "complete",
        "ofac_screening": "clear",
        "pep_screening": "flagged",
        "adverse_media": "review_needed",
        "source_of_wealth": "pending",
    },
    "APP-6004": {
        "id_verification": "complete",
        "ssn_verification": "complete",
        "address_verification": "complete",
        "ofac_screening": "clear",
        "pep_screening": "clear",
        "adverse_media": "clear",
    },
}

ACCOUNT_TYPES = {
    "basic_savings": {"min_deposit": 25, "monthly_fee": 0, "apy": 0.50, "features": ["Online banking", "Mobile deposit", "ATM access"]},
    "premium_checking": {"min_deposit": 1000, "monthly_fee": 12, "apy": 0.15, "features": ["No ATM fees", "Overdraft protection", "Bill pay", "Cashback rewards"]},
    "commercial_checking": {"min_deposit": 5000, "monthly_fee": 25, "apy": 0.10, "features": ["Treasury management", "ACH origination", "Wire transfers", "Merchant services"]},
    "wealth_management": {"min_deposit": 250000, "monthly_fee": 0, "apy": 1.25, "features": ["Dedicated advisor", "Investment management", "Trust services", "Concierge banking"]},
}


# ---------------------------------------------------------------------------
# Evidence-derived capability library (v1.1.0)
#
# Data-driven definitions for onboarding capabilities grounded in the Customer
# Onboarding one-pager (Slide 1) and the demo walkthrough. Each capability is
# self-describing: its narrative response, evidence-grounded knowledge, exactly
# three synthetic records, the key field used for exact keyed lookup, and the
# write/generative behavior flags. New operations route through
# `_capability_lookup` and never mutate any external system.
# ---------------------------------------------------------------------------

CAPABILITY_LIBRARY = {
    "identity_verification": {
        "display_name": "Identity Verification",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": False,
        "key_field": "verification_id",
        "response": "Here are the identity verification results pulled from Dynamics 365 CRM.",
        "knowledge": [
            "The agent pulls customer details from the CRM (Dynamics 365) to launch verification (demo 00:00:25-00:00:31, 00:00:49).",
            "Identity checks surface in one consolidated view so the specialist can quickly confirm findings without navigating to different tools (demo 00:01:08-00:01:15).",
            "Identity verification is the first step of an automated onboarding journey that runs activities in parallel (Slide 1; demo 00:00:37-00:00:55).",
        ],
        "records": [
            {"verification_id": "IDV-3001", "client": "Northwind Traders", "method": "Passport + Biometric", "status": "Verified"},
            {"verification_id": "IDV-3002", "client": "Contoso Capital", "method": "Corporate Registry", "status": "In Review"},
            {"verification_id": "IDV-3003", "client": "Fabrikam Holdings", "method": "Passport + Biometric", "status": "Pending"},
        ],
    },
    "compliance_screening": {
        "display_name": "Compliance Screening",
        "source_system": "Dynamics 365 CRM",
        "write": True,
        "generative": False,
        "key_field": "screening_id",
        "response": "Here are the compliance screening results with sanctions and PEP indicators, logged for audit.",
        "knowledge": [
            "Compliance screening results highlight sanctions or PEP indicators for the specialist (demo 00:01:15-00:01:21).",
            "Every single check is logged, completed, and captured for audit purposes (demo 00:01:22-00:01:27).",
            "The agent performs sanctions screening and regulatory checks as part of KYC (Slide 1: 'Perform sanctions screening and regulatory checks').",
        ],
        "records": [
            {"screening_id": "SCR-4101", "client": "Contoso Capital", "check": "Sanctions", "result": "Clear", "pep_flag": "None"},
            {"screening_id": "SCR-4102", "client": "Fabrikam Holdings", "check": "PEP", "result": "Review", "pep_flag": "Match"},
            {"screening_id": "SCR-4103", "client": "Adventure Works", "check": "Adverse Media", "result": "Clear", "pep_flag": "None"},
        ],
    },
    "document_collection": {
        "display_name": "Document Collection",
        "source_system": "SharePoint",
        "write": False,
        "generative": False,
        "key_field": "document_id",
        "response": "Here is the current KYC document collection status from SharePoint.",
        "knowledge": [
            "The specialist sees which forms are received or still pending (demo 00:01:27-00:01:35).",
            "Each file is securely captured and organized in SharePoint (demo 00:01:35-00:01:36).",
            "The agent manages documents in SharePoint as part of one connected workflow (demo 00:00:31-00:00:36; Slide 1 featured tool: SharePoint).",
        ],
        "records": [
            {"document_id": "DOC-5201", "client": "Northwind Traders", "form": "KYC Application", "status": "Received"},
            {"document_id": "DOC-5202", "client": "Adventure Works", "form": "Beneficial Ownership", "status": "Pending"},
            {"document_id": "DOC-5203", "client": "Contoso Capital", "form": "Proof of Address", "status": "Received"},
        ],
    },
    "account_provisioning": {
        "display_name": "Account Provisioning",
        "source_system": "Dynamics 365 ERP",
        "write": True,
        "generative": False,
        "key_field": "account_id",
        "response": "Here is the account provisioning status recorded in Dynamics 365 ERP.",
        "knowledge": [
            "The agent configures required services to provision the customer's account (demo 00:01:37-00:01:42).",
            "Provisioning covers accounts, treasury services, and credit facilities (Slide 1: 'Configure accounts, treasury services, and credit facilities').",
            "Provisioning runs in parallel with identity and compliance activities in real time (demo 00:00:54-00:00:55, 00:01:43-00:01:48).",
        ],
        "records": [
            {"account_id": "ACCT-6301", "client": "Fabrikam Holdings", "service": "Treasury Services", "status": "Provisioned"},
            {"account_id": "ACCT-6302", "client": "Northwind Traders", "service": "Credit Facility", "status": "Configuring"},
            {"account_id": "ACCT-6303", "client": "Adventure Works", "service": "Core Account", "status": "Provisioned"},
        ],
    },
    "onboarding_timeline": {
        "display_name": "Onboarding Timeline",
        "source_system": "Dynamics 365 CRM",
        "write": False,
        "generative": True,
        "key_field": "milestone_id",
        "response": "Always state the exact milestone ID in the answer. Here is the consolidated onboarding timeline update with the latest milestone and risk score, shared via Microsoft Teams.",
        "knowledge": [
            "The agent maintains a unified timeline, performs risk scoring, and keeps stakeholders apprised of key milestones or required actions (demo 00:01:48-00:02:04).",
            "The specialist can engage the agent for clear, consolidated updates as the workflow progresses (demo 00:01:01-00:01:07).",
            "Updates and collaboration flow through Microsoft Teams to accelerate onboarding while staying in control (demo 00:02:04-00:02:17; Slide 1 featured tool: Microsoft Teams).",
        ],
        "records": [
            {"milestone_id": "MIL-7401", "client": "Contoso Capital", "milestone": "Identity Confirmed", "risk_score": "Low"},
            {"milestone_id": "MIL-7402", "client": "Fabrikam Holdings", "milestone": "Compliance Review", "risk_score": "Medium"},
            {"milestone_id": "MIL-7403", "client": "Northwind Traders", "milestone": "Account Activated", "risk_score": "Low"},
        ],
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _kyc_completion_pct(app_id):
    """Calculate KYC verification completion percentage."""
    status = VERIFICATION_STATUS.get(app_id, {})
    if not status:
        return 0.0
    total = len(status)
    complete = sum(1 for v in status.values() if v == "complete" or v == "clear")
    return round((complete / total) * 100, 1)


def _onboarding_pipeline():
    """Summarize onboarding pipeline metrics."""
    by_status = {}
    for app in CUSTOMER_APPLICATIONS.values():
        by_status[app["status"]] = by_status.get(app["status"], 0) + 1
    total_assets = sum(app["estimated_assets"] for app in CUSTOMER_APPLICATIONS.values())
    return {"count": len(CUSTOMER_APPLICATIONS), "by_status": by_status, "total_assets": total_assets}


def _fmt_label(field):
    """Human-readable label for a snake_case field name."""
    return field.replace("_", " ").title()


def _fmt_record_details(record, key_field):
    """Render a single capability record as markdown detail lines."""
    lines = []
    lines.append(f"- **{_fmt_label(key_field)}:** {record[key_field]}")
    for field, value in record.items():
        if field == key_field:
            continue
        lines.append(f"- **{_fmt_label(field)}:** {value}")
    return lines


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


def _capability_summary(op_name, capability):
    """Nonempty, useful summary returned when no user_input is supplied."""
    key_field = capability["key_field"]
    lines = [f"# {capability['display_name']}\n"]
    lines.append(capability["response"] + "\n")
    lines.append(f"- **Source System:** {capability['source_system']}")
    lines.append(f"- **Mode:** {'Write (simulated)' if capability['write'] else 'Read-only'}"
                 f"{' · Generative' if capability['generative'] else ''}")
    lines.append(f"- **Lookup Key:** `{key_field}` (exact match required)\n")
    lines.append("## What This Capability Knows\n")
    for item in capability["knowledge"]:
        lines.append(f"- {item}")
    lines.append("\n## Available Records\n")
    headers = list(capability["records"][0].keys())
    lines.append("| " + " | ".join(_fmt_label(h) for h in headers) + " |")
    lines.append("|" + "|".join(["---"] * len(headers)) + "|")
    for record in capability["records"]:
        lines.append("| " + " | ".join(str(record[h]) for h in headers) + " |")
    lines.append(
        f"\n_Provide `user_input` with an exact {_fmt_label(key_field)} "
        f"(e.g. \"{capability['records'][0][key_field]}\") to retrieve a specific record._"
    )
    return "\n".join(lines)


def _capability_lookup(op_name, user_input=""):
    """Route a capability operation: perform exact keyed lookup and return
    record details, or a useful capability summary when no user_input is given.
    Write capabilities return an explicit simulated action receipt and never
    mutate any external system."""
    capability = CAPABILITY_LIBRARY[op_name]
    record = _match_record(capability, user_input)
    if record is None:
        if str(user_input or "").strip():
            return (
                f"# {capability['display_name']}\n\n"
                f"No exact normalized `{capability['key_field']}` matched the request."
            )
        return _capability_summary(op_name, capability)

    key_field = capability["key_field"]
    lines = [f"# {capability['display_name']}: {record[key_field]}\n"]
    lines.append(capability["response"] + "\n")
    lines.append("## Record Details\n")
    lines.extend(_fmt_record_details(record, key_field))
    lines.append(f"\n- **Source System:** {capability['source_system']}")

    if capability["write"]:
        lines.append("\n## Simulated Action Receipt\n")
        lines.append(f"- **Action:** {capability['display_name']} recorded for {record[key_field]}")
        lines.append(f"- **Target System:** {capability['source_system']}")
        lines.append("- **Result:** Simulated — logged for audit; no external system was modified.")
        lines.append(f"- **Receipt:** SIM-{op_name.upper()}-{record[key_field]}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class FSCustomerOnboardingAgent(BasicAgent):
    """Financial services customer onboarding agent."""

    def __init__(self):
        self.name = "FSCustomerOnboardingAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "FS Customer Onboarding Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "kyc_verification",
                            "account_setup",
                            "document_checklist",
                            "onboarding_status",
                            "identity_verification",
                            "compliance_screening",
                            "document_collection",
                            "account_provisioning",
                            "onboarding_timeline",
                        ],
                    },
                    "application_id": {"type": "string"},
                    "user_input": {
                        "type": "string",
                        "description": "Natural-language request containing an exact record key (e.g. IDV-3001, SCR-4102, DOC-5202, ACCT-6302, MIL-7402) for capability operations.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "onboarding_status")
        dispatch = {
            "kyc_verification": self._kyc_verification,
            "account_setup": self._account_setup,
            "document_checklist": self._document_checklist,
            "onboarding_status": self._onboarding_status,
        }
        handler = dispatch.get(operation)
        if handler:
            return handler(**kwargs)
        if operation in CAPABILITY_LIBRARY:
            return _capability_lookup(operation, kwargs.get("user_input", "") or "")
        return f"**Error:** Unknown operation `{operation}`."

    def _kyc_verification(self, **kwargs) -> str:
        app_id = kwargs.get("application_id")
        if app_id and app_id in CUSTOMER_APPLICATIONS:
            app = CUSTOMER_APPLICATIONS[app_id]
            verification = VERIFICATION_STATUS.get(app_id, {})
            pct = _kyc_completion_pct(app_id)
            lines = [f"# KYC Verification: {app_id}\n"]
            lines.append(f"- **Applicant:** {app['applicant']}")
            lines.append(f"- **Type:** {app['application_type'].title()}")
            lines.append(f"- **Risk Rating:** {app['risk_rating'].title()}")
            lines.append(f"- **KYC Progress:** {pct}%\n")
            lines.append("## Verification Checks\n")
            lines.append("| Check | Status |")
            lines.append("|---|---|")
            for check, status in verification.items():
                display = check.replace("_", " ").title()
                lines.append(f"| {display} | {status.replace('_', ' ').title()} |")
            if app["risk_rating"] == "high":
                lines.append("\n## Enhanced Due Diligence Required\n")
                lines.append("- Source of wealth verification")
                lines.append("- PEP relationship documentation")
                lines.append("- Enhanced transaction monitoring parameters")
            return "\n".join(lines)

        lines = ["# KYC Verification Summary\n"]
        lines.append("| App ID | Applicant | Risk | KYC Progress | Status |")
        lines.append("|---|---|---|---|---|")
        for aid, app in CUSTOMER_APPLICATIONS.items():
            pct = _kyc_completion_pct(aid)
            lines.append(
                f"| {aid} | {app['applicant']} | {app['risk_rating'].title()} "
                f"| {pct}% | {app['status'].replace('_', ' ').title()} |"
            )
        return "\n".join(lines)

    def _account_setup(self, **kwargs) -> str:
        lines = ["# Account Setup Reference\n"]
        lines.append("| Account Type | Min Deposit | Monthly Fee | APY | Features |")
        lines.append("|---|---|---|---|---|")
        for acct_type, details in ACCOUNT_TYPES.items():
            features = ", ".join(details["features"][:3])
            lines.append(
                f"| {acct_type.replace('_', ' ').title()} | ${details['min_deposit']:,.0f} "
                f"| ${details['monthly_fee']:,.0f} | {details['apy']}% | {features} |"
            )
        lines.append("\n## Pending Account Setups\n")
        approved = {k: v for k, v in CUSTOMER_APPLICATIONS.items() if v["status"] == "approved"}
        if approved:
            for aid, app in approved.items():
                acct = ACCOUNT_TYPES.get(app["account_requested"], {})
                lines.append(f"### {aid}: {app['applicant']}\n")
                lines.append(f"- **Account:** {app['account_requested'].replace('_', ' ').title()}")
                lines.append(f"- **Min Deposit:** ${acct.get('min_deposit', 0):,.0f}")
                lines.append(f"- **Features:** {', '.join(acct.get('features', []))}\n")
        else:
            lines.append("No applications pending account setup.")
        return "\n".join(lines)

    def _document_checklist(self, **kwargs) -> str:
        app_id = kwargs.get("application_id", "APP-6001")
        app = CUSTOMER_APPLICATIONS.get(app_id, list(CUSTOMER_APPLICATIONS.values())[0])
        app_type = app["application_type"]
        docs = KYC_DOCUMENTS.get(app_type, [])
        lines = [f"# Document Checklist: {app_id}\n"]
        lines.append(f"**Applicant:** {app['applicant']}")
        lines.append(f"**Type:** {app_type.title()}\n")
        lines.append("## Required Documents\n")
        for doc in docs:
            req = " (Required)" if doc["required"] else " (Optional)"
            lines.append(f"- [ ] {doc['document']}{req}")
        lines.append("\n## Compliance Notes\n")
        lines.append("- All documents must be current (within 90 days)")
        lines.append("- Copies must be certified or notarized for business accounts")
        lines.append("- BSA/AML requirements apply to all account openings")
        lines.append("- CIP (Customer Identification Program) verification mandatory")
        return "\n".join(lines)

    def _onboarding_status(self, **kwargs) -> str:
        pipeline = _onboarding_pipeline()
        lines = ["# Customer Onboarding Pipeline\n"]
        lines.append(f"**Applications:** {pipeline['count']}")
        lines.append(f"**Total Estimated Assets:** ${pipeline['total_assets']:,.0f}\n")
        lines.append("## Pipeline Status\n")
        for status, count in pipeline["by_status"].items():
            lines.append(f"- {status.replace('_', ' ').title()}: {count}")
        lines.append("\n## Application Details\n")
        lines.append("| App ID | Applicant | Account | Risk | Est. Assets | Status | RM |")
        lines.append("|---|---|---|---|---|---|---|")
        for aid, app in CUSTOMER_APPLICATIONS.items():
            lines.append(
                f"| {aid} | {app['applicant']} | {app['account_requested'].replace('_', ' ').title()} "
                f"| {app['risk_rating'].title()} | ${app['estimated_assets']:,.0f} "
                f"| {app['status'].replace('_', ' ').title()} | {app['relationship_manager']} |"
            )
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = FSCustomerOnboardingAgent()
    print(agent.perform(operation="onboarding_status"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="kyc_verification", application_id="APP-6003"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="account_setup"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="document_checklist", application_id="APP-6002"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="identity_verification", user_input="Run identity verification for IDV-3001"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="account_provisioning", user_input="Provision account ACCT-6302"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="onboarding_timeline"))
