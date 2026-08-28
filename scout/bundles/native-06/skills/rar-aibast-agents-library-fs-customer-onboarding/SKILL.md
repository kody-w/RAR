---
name: "rar-aibast-agents-library-fs-customer-onboarding"
description: "Tracks bank customer onboarding and KYC from a live simulated Dynamics 365 tenant (leads as applications), with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/fs_customer_onboarding", "rar_sha256": "5fdb19d2d6fb379d1f58ec7b4c62a0e496de92b9214d3721eb480553cc08a5ab", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["KYC", "onboarding", "account-setup", "compliance", "financial-services", "identity-verification", "sanctions-screening", "account-provisioning"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/fs_customer_onboarding`. The original RAPP
agent is preserved byte-for-byte in `customer_onboarding_fs_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Financial Services Customer Onboarding Agent — a template you are meant to mutate.

Manages KYC verification, account setup, document checklists, and
onboarding status tracking for financial institution customer onboarding.
In this template a new-customer onboarding application is represented as a
Dynamics 365 lead — the tenant has no native "application" entity, so leads
stand in for the intake pipeline.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `onboarding_status` operation pulls live
     lead records over real HTTP from the globally hosted Static Dynamics
     365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="onboarding_status")
     and look for the Silas Dunn / Bluegrass Credit Union application.
  2. No network? Everything falls back to the embedded demo layer below
     (CUSTOMER_APPLICATIONS / VERIFICATION_STATUS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     FS_CUSTOMER_ONBOARDING_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your loan/deposit origination
     system), or replace _fetch_collection() with calls into your own API.
     The fields the rest of the file needs are listed in
     _normalize_live_application() — everything else keeps working
     untouched. Fields rendered "n/a — enrichment seam" (account requested,
     KYC risk rating) are where you wire your core banking / KYC vendor.

OPERATIONS
  kyc_verification | account_setup | document_checklist | onboarding_status
  | identity_verification | compliance_screening | document_collection
  | account_provisioning | onboarding_timeline
  kwargs: operation (required), application_id, user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "application_id": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "kyc_verification",
        "account_setup",
        "document_checklist",
        "onboarding_status",
        "identity_verification",
        "compliance_screening",
        "document_collection",
        "account_provisioning",
        "onboarding_timeline"
      ],
      "type": "string"
    },
    "user_input": {
      "description": "Natural-language request containing an exact record key (e.g. IDV-3001, SCR-4102, DOC-5202, ACCT-6302, MIL-7402) for capability operations.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_onboarding_fs_agent.py` and embedded as the fenced Python below (sha256 5fdb19d2d6fb379d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_onboarding_fs_agent.py` first:

```bash
python3 customer_onboarding_fs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 customer_onboarding_fs_agent.py   # or on stdin
python3 customer_onboarding_fs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Financial Services Customer Onboarding Agent — a template you are meant to mutate.

Manages KYC verification, account setup, document checklists, and
onboarding status tracking for financial institution customer onboarding.
In this template a new-customer onboarding application is represented as a
Dynamics 365 lead — the tenant has no native "application" entity, so leads
stand in for the intake pipeline.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `onboarding_status` operation pulls live
     lead records over real HTTP from the globally hosted Static Dynamics
     365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="onboarding_status")
     and look for the Silas Dunn / Bluegrass Credit Union application.
  2. No network? Everything falls back to the embedded demo layer below
     (CUSTOMER_APPLICATIONS / VERIFICATION_STATUS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     FS_CUSTOMER_ONBOARDING_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your loan/deposit origination
     system), or replace _fetch_collection() with calls into your own API.
     The fields the rest of the file needs are listed in
     _normalize_live_application() — everything else keeps working
     untouched. Fields rendered "n/a — enrichment seam" (account requested,
     KYC risk rating) are where you wire your core banking / KYC vendor.

OPERATIONS
  kyc_verification | account_setup | document_checklist | onboarding_status
  | identity_verification | compliance_screening | document_collection
  | account_provisioning | onboarding_timeline
  kwargs: operation (required), application_id, user_input
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json as _json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/fs_customer_onboarding",
    "version": "1.2.0",
    "display_name": "FS Customer Onboarding Agent",
    "description": "Tracks bank customer onboarding and KYC from a live simulated Dynamics 365 tenant (leads as applications), with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["KYC", "onboarding", "account-setup", "compliance", "financial-services", "identity-verification", "sanctions-screening", "account-provisioning"],
    "category": "financial_services",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ---------------------------------------------------------------------------
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export FS_CUSTOMER_ONBOARDING_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your origination-system client.
# Downstream code only needs the fields produced by
# _normalize_live_application().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "FS_CUSTOMER_ONBOARDING_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
_LIVE_CACHE = {}


def _fetch_collection(collection, timeout=6):
    """One bounded GET per collection per process. Returns [] on ANY
    failure — offline, DNS, bad JSON — so the demo layer takes over."""
    if collection in _LIVE_CACHE:
        return _LIVE_CACHE[collection]
    try:
        req = urllib.request.Request(
            f"{DATA_SOURCE_URL}/{collection}.json",
            headers={"User-Agent": "rapp-agent-template/1.0"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            rows = _json.loads(resp.read().decode("utf-8")).get("value", [])
    except Exception:
        rows = []
    _LIVE_CACHE[collection] = rows
    return rows


def _normalize_live_application(row):
    """Project a Dynamics lead onto the application shape this agent uses.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not knowable from the CRM alone' and the
    renderers label it as an enrichment seam."""
    state = row.get("statecode")
    status = {0: "application_received", 1: "approved", 2: "withdrawn"}.get(state, "application_received")
    company = row.get("companyname")
    return {
        "applicant": row.get("fullname") or company or "Unknown",
        "application_type": "business" if company else "individual",
        "account_requested": None,   # enrichment seam — wire your core banking system
        "submitted": str(row.get("createdon", ""))[:10],
        "status": status,
        "risk_rating": None,         # enrichment seam — wire your KYC/AML vendor
        "relationship_manager": row.get("owneridname", ""),
        "estimated_assets": float(row.get("estimatedamount") or 0),
        "_company": company or "",
        "_live": True,
    }


def _live_applications():
    """Lead-keyed dict of live tenant onboarding applications; {} offline."""
    rows = _fetch_collection("leads")
    if not rows:
        return {}
    return {
        f"LEAD-{str(row.get('leadid', ''))[:8]}": _normalize_live_application(row)
        for row in rows
        if row.get("leadid")
    }


def _seam(value, formatter=str):
    """None = the CRM alone can't know this (enrichment seam)."""
    return "n/a — enrichment seam" if value is None else formatter(value)


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
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


def _onboarding_pipeline(applications):
    """Summarize onboarding pipeline metrics."""
    by_status = {}
    for app in applications.values():
        by_status[app["status"]] = by_status.get(app["status"], 0) + 1
    total_assets = sum(app["estimated_assets"] for app in applications.values())
    return {"count": len(applications), "by_status": by_status, "total_assets": total_assets}


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
        live = _live_applications()
        applications = live or CUSTOMER_APPLICATIONS
        pipeline = _onboarding_pipeline(applications)
        lines = ["# Customer Onboarding Pipeline\n"]
        lines.append(f"**Applications:** {pipeline['count']}")
        lines.append(f"**Total Estimated Assets:** ${pipeline['total_assets']:,.0f}\n")
        lines.append("## Pipeline Status\n")
        for status, count in pipeline["by_status"].items():
            lines.append(f"- {status.replace('_', ' ').title()}: {count}")
        lines.append("\n## Application Details\n")
        lines.append("| App ID | Applicant | Account | Risk | Est. Assets | Status | RM |")
        lines.append("|---|---|---|---|---|---|---|")
        for aid, app in applications.items():
            applicant = app["applicant"]
            if app.get("_company"):
                applicant = f"{applicant} ({app['_company']})"
            lines.append(
                f"| {aid} | {applicant} "
                f"| {_seam(app['account_requested'], lambda v: v.replace('_', ' ').title())} "
                f"| {_seam(app['risk_rating'], lambda v: v.title())} | ${app['estimated_assets']:,.0f} "
                f"| {app['status'].replace('_', ' ').title()} | {app['relationship_manager']} |"
            )
        if live:
            lines.append(
                "\n_Source: live Static Dynamics 365 tenant — Dynamics leads "
                "reinterpreted as onboarding applications. Account/risk columns "
                "are enrichment seams (wire your core banking / KYC vendor)._"
            )
        else:
            lines.append("\n_Source: embedded demo layer (offline fallback)._")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = FSCustomerOnboardingAgent()
    print("=" * 80)
    print("EMBEDDED DEMO APPLICATION (works offline)")
    print(agent.perform(operation="kyc_verification", application_id="APP-6003"))
    print("\n" + "=" * 80 + "\n")
    print("LIVE TENANT PIPELINE (leads fetched over HTTP; falls back offline)")
    print(agent.perform(operation="onboarding_status"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="document_checklist", application_id="APP-6002"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="identity_verification", user_input="Run identity verification for IDV-3001"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="onboarding_timeline"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
