---
name: "rar-aibast-agents-library-claims-processing"
description: "Processes claims and disputes from a live simulated Dynamics 365 tenant, with triage, fraud flags, and an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/claims_processing", "rar_sha256": "862839f3377e4d487950a3b8f6bb7cb3b7d4accb29c978d45e9bee6161332a58", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["claims", "insurance", "adjudication", "fraud", "settlement", "financial-services"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/claims_processing`. The original RAPP
agent is preserved byte-for-byte in `claims_processing_agent.py` and in the RCI capsule.

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

Claims Processing Agent — a template you are meant to mutate.

Supports the insurance claims lifecycle with intake, adjudication review,
fraud flagging, and settlement recommendations, plus five capability
operations (claim_triage, fraud_detection, auto_adjudication,
complex_claim_prep, performance_metrics) derived from the Claims
Processing external agent spec (rapp-external-agent-spec/1.0).

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live claim records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template a claim or dispute IS a Dynamics case at a
     financial-services account — e.g. CAS-260126 "Disputed card
     transaction under investigation" at Bluegrass Credit Union, and
     CAS-260127, member Marcus Webb's loan application review.
     Try: perform(operation="claim_intake")
  2. No network? Everything falls back to the embedded demo layer below
     (CLAIMS / POLICY_DETAILS / FRAUD_INDICATORS / SPEC_CAPABILITIES) —
     the agent never crashes offline, and capability operations that
     stay canned keep saying "simulated".
  3. Make it yours at the LIVE DATA SEAM below: set
     CLAIMS_PROCESSING_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from your claims platform), or
     replace _fetch_collection() with your own API client. Fields the
     rest of the file needs are listed in _normalize_live_claim() —
     everything else keeps working untouched. Fields marked "enrichment
     seam" in the output (policy numbers, claimed amounts, fraud
     scores) are where you wire your policy admin and fraud-scoring
     systems.

OPERATIONS
  claim_intake | adjudication_review | fraud_flag
  | settlement_recommendation | claim_triage | fraud_detection
  | auto_adjudication | complex_claim_prep | performance_metrics
  kwargs: operation (required), claim_id, user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "claim_id": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "claim_intake",
        "adjudication_review",
        "fraud_flag",
        "settlement_recommendation",
        "claim_triage",
        "fraud_detection",
        "auto_adjudication",
        "complex_claim_prep",
        "performance_metrics"
      ],
      "type": "string"
    },
    "user_input": {
      "description": "Optional natural-language request; enables exact-keyed record matching for the v1.1.0 capability operations.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `claims_processing_agent.py` and embedded as the fenced Python below (sha256 862839f3377e4d48…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `claims_processing_agent.py` first:

```bash
python3 claims_processing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 claims_processing_agent.py   # or on stdin
python3 claims_processing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Claims Processing Agent — a template you are meant to mutate.

Supports the insurance claims lifecycle with intake, adjudication review,
fraud flagging, and settlement recommendations, plus five capability
operations (claim_triage, fraud_detection, auto_adjudication,
complex_claim_prep, performance_metrics) derived from the Claims
Processing external agent spec (rapp-external-agent-spec/1.0).

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live claim records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template a claim or dispute IS a Dynamics case at a
     financial-services account — e.g. CAS-260126 "Disputed card
     transaction under investigation" at Bluegrass Credit Union, and
     CAS-260127, member Marcus Webb's loan application review.
     Try: perform(operation="claim_intake")
  2. No network? Everything falls back to the embedded demo layer below
     (CLAIMS / POLICY_DETAILS / FRAUD_INDICATORS / SPEC_CAPABILITIES) —
     the agent never crashes offline, and capability operations that
     stay canned keep saying "simulated".
  3. Make it yours at the LIVE DATA SEAM below: set
     CLAIMS_PROCESSING_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from your claims platform), or
     replace _fetch_collection() with your own API client. Fields the
     rest of the file needs are listed in _normalize_live_claim() —
     everything else keeps working untouched. Fields marked "enrichment
     seam" in the output (policy numbers, claimed amounts, fraud
     scores) are where you wire your policy admin and fraud-scoring
     systems.

OPERATIONS
  claim_intake | adjudication_review | fraud_flag
  | settlement_recommendation | claim_triage | fraud_detection
  | auto_adjudication | complex_claim_prep | performance_metrics
  kwargs: operation (required), claim_id, user_input
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/claims_processing",
    "version": "1.2.0",
    "display_name": "Claims Processing Agent",
    "description": "Processes claims and disputes from a live simulated Dynamics 365 tenant, with triage, fraud flags, and an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["claims", "insurance", "adjudication", "fraud", "settlement", "financial-services"],
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
#   export CLAIMS_PROCESSING_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your claims-platform client.
# Downstream code only needs the fields produced by
# _normalize_live_claim().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "CLAIMS_PROCESSING_DATA_URL",
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
            rows = json.loads(resp.read().decode("utf-8")).get("value", [])
    except Exception:
        rows = []
    _LIVE_CACHE[collection] = rows
    return rows


def _normalize_live_claim(row):
    """Project a Dynamics case onto the claim shape this agent uses.
    THIS is the contract your replacement data source must meet — a
    dict with these keys. None means 'not available from CRM alone' and
    the renderers label it as an enrichment seam. In this template a
    claim or dispute IS a Dynamics case at a financial-services
    account."""
    return {
        "id": row.get("ticketnumber", ""),
        "claimant": row.get("customeridname", "Unknown"),
        "policy_number": None,    # enrichment seam — wire your policy admin system
        "loss_type": row.get("title", "untitled"),
        "claimed_amount": None,   # enrichment seam — wire your claims platform
        "adjuster": row.get("owneridname", ""),
        "status": "open" if row.get("statecode") == 0 else "resolved",
        "priority": {1: "High", 2: "Normal", 3: "Low"}.get(row.get("prioritycode"), "Normal"),
        "date_filed": str(row.get("createdon", ""))[:10],
        "fraud_score": None,      # enrichment seam — wire your fraud-scoring model
        "_live": True,
    }


def _live_claims():
    """Live claims: cases at financial-services accounts or their
    member contacts; [] when offline."""
    accounts = _fetch_collection("accounts")
    if not accounts:
        return []
    fin_names = {
        a["name"] for a in accounts
        if "financial" in str(a.get("industrycode", "")).lower() and a.get("name")
    }
    member_names = {
        c["fullname"] for c in _fetch_collection("contacts")
        if c.get("parentcustomeridname") in fin_names and c.get("fullname")
    }
    return [
        _normalize_live_claim(i)
        for i in _fetch_collection("incidents")
        if i.get("customeridname") in fin_names or i.get("customeridname") in member_names
    ]


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

CLAIMS = {
    "CLM-2025-7001": {
        "claimant": "Margaret Sullivan",
        "policy_number": "HO-445892",
        "policy_type": "homeowners",
        "date_of_loss": "2025-01-15",
        "date_filed": "2025-01-18",
        "loss_type": "water_damage",
        "description": "Burst pipe in upstairs bathroom caused water damage to ceiling, walls, and flooring in two rooms",
        "claimed_amount": 28500,
        "adjuster": "Brian Keller",
        "status": "under_review",
        "fraud_score": 12,
        "supporting_docs": ["photos", "plumber_invoice", "repair_estimate"],
    },
    "CLM-2025-7002": {
        "claimant": "David Park",
        "policy_number": "AU-331205",
        "policy_type": "auto",
        "date_of_loss": "2025-02-08",
        "date_filed": "2025-02-09",
        "loss_type": "collision",
        "description": "Rear-end collision at intersection of 5th Ave and Main St, other driver cited",
        "claimed_amount": 14200,
        "adjuster": "Sandra Ortiz",
        "status": "approved",
        "fraud_score": 5,
        "supporting_docs": ["police_report", "photos", "body_shop_estimate", "medical_records"],
    },
    "CLM-2025-7003": {
        "claimant": "Apex Commercial Properties",
        "policy_number": "CP-778341",
        "policy_type": "commercial_property",
        "date_of_loss": "2025-02-22",
        "date_filed": "2025-02-24",
        "loss_type": "fire_damage",
        "description": "Electrical fire in warehouse section B, significant inventory and structural damage",
        "claimed_amount": 485000,
        "adjuster": "Brian Keller",
        "status": "investigation",
        "fraud_score": 68,
        "supporting_docs": ["fire_report", "photos", "inventory_list", "financial_statements"],
    },
    "CLM-2025-7004": {
        "claimant": "Jennifer Liu",
        "policy_number": "HO-557210",
        "policy_type": "homeowners",
        "date_of_loss": "2025-03-01",
        "date_filed": "2025-03-02",
        "loss_type": "theft",
        "description": "Home burglary — electronics, jewelry, and collectibles stolen",
        "claimed_amount": 42000,
        "adjuster": "Sandra Ortiz",
        "status": "pending_documentation",
        "fraud_score": 45,
        "supporting_docs": ["police_report", "photos"],
    },
}

POLICY_DETAILS = {
    "HO-445892": {"coverage_limit": 350000, "deductible": 1500, "premium_annual": 2400, "effective": "2024-07-01", "expiry": "2025-07-01"},
    "AU-331205": {"coverage_limit": 100000, "deductible": 500, "premium_annual": 1800, "effective": "2024-11-01", "expiry": "2025-11-01"},
    "CP-778341": {"coverage_limit": 2000000, "deductible": 10000, "premium_annual": 18500, "effective": "2024-09-01", "expiry": "2025-09-01"},
    "HO-557210": {"coverage_limit": 400000, "deductible": 2000, "premium_annual": 2800, "effective": "2025-01-01", "expiry": "2026-01-01"},
}

FRAUD_INDICATORS = {
    "financial_stress": {"weight": 15, "description": "Claimant shows signs of recent financial distress"},
    "claim_timing": {"weight": 12, "description": "Claim filed shortly after policy inception or increase in coverage"},
    "excessive_amount": {"weight": 20, "description": "Claimed amount significantly exceeds typical loss for category"},
    "inconsistent_narrative": {"weight": 18, "description": "Inconsistencies between claimant statement and evidence"},
    "prior_claims_history": {"weight": 10, "description": "Multiple prior claims on same or similar policies"},
    "delayed_reporting": {"weight": 8, "description": "Significant delay between loss event and claim filing"},
    "witness_issues": {"weight": 12, "description": "Lack of independent witnesses or corroborating evidence"},
    "documentation_gaps": {"weight": 15, "description": "Missing or incomplete supporting documentation"},
}

ADJUSTER_NOTES = {
    "CLM-2025-7001": ["Initial inspection completed 01/20 — damage consistent with pipe burst", "Plumber confirms corrosion in copper fitting", "Estimate from licensed contractor received"],
    "CLM-2025-7002": ["Police report confirms other party at fault", "Body shop estimate within market range", "Medical records show minor soft tissue injury"],
    "CLM-2025-7003": ["Fire marshal report pending", "Financial statements show declining revenue for 3 quarters", "Inventory list lacks purchase receipts for high-value items", "SIU referral initiated"],
    "CLM-2025-7004": ["Police report filed but no suspects identified", "Itemized list of stolen items requested", "Receipts or appraisals needed for jewelry and collectibles"],
}


# ---------------------------------------------------------------------------
# Embedded spec capabilities (rapp-external-agent-spec/1.0)
#
# Deterministic, self-contained data for the five capability operations added
# in v1.1.0. Nothing here performs network calls or mutates external systems.
# ---------------------------------------------------------------------------

SPEC_CAPABILITIES = {
    "claim_triage": {
        "title": "Claim Intake Triage",
        "description": "Analyzes the incoming claims queue and instantly classifies and routes each claim into automated or human workflows, grouping them into tiers and flagging regulatory deadlines and VIP policy holders.",
        "response": "Here is the triage of today's incoming claims queue, grouped into tiers with regulatory deadlines and VIP policy holders flagged for your attention.",
        "source_system": "Dynamics 365 CRM",
        "customer": "an insurance company",
        "write": False,
        "generative": False,
        "exact_key_required": True,
        "key_field": "claim_id",
        "triggers": [
            "process today's incoming queue",
            "triage claims instantly",
            "classify and route claims",
            "group claims into tiers",
            "flag regulatory deadlines and VIP policy holders",
        ],
        "knowledge": [
            "Incoming claims are analyzed automatically and grouped into tiers such as fast-track, auto-adjudicate, and complex.",
            "Regulatory deadlines and VIP policy holders are flagged without manual reviews so the manager sees where attention is needed most.",
            "Standardized triage accelerates routing and reduces adjuster workloads.",
            "Claims are routed instantly to automated or human workflows based on complexity and risk.",
        ],
        "synthetic_data": [
            {"claim_id": "CLM48213", "claimant": "Contoso Freight", "tier": "Fast-track", "deadline_flag": "Regulatory 5-day", "vip": False},
            {"claim_id": "CLM50117", "claimant": "Aria Holt", "tier": "Complex", "deadline_flag": "Standard", "vip": True},
            {"claim_id": "CLM50942", "claimant": "Fabrikam Logistics", "tier": "Auto-adjudicate", "deadline_flag": "None", "vip": False},
        ],
    },
    "fraud_detection": {
        "title": "Fraud Detection and SIU Referral",
        "description": "Summarizes suspicious patterns, highlights the small set of claims with strong fraud indicators, generates SIU evidence packages, and recommends which claims to send to the Special Investigations Unit.",
        "response": "Here are the fraud detection results: suspicious patterns are summarized, high risk claims are highlighted, and SIU referrals with evidence packages are recommended so serious risks are not missed.",
        "source_system": "Dynamics 365 CRM",
        "customer": "an insurance company",
        "write": True,
        "generative": True,
        "exact_key_required": True,
        "key_field": "case_id",
        "triggers": [
            "fraud detection results and high risk claims",
            "highlight claims with strong fraud indicators",
            "recommend which claims to send to SIU",
            "generate SIU evidence packages",
            "summarize suspicious patterns",
        ],
        "knowledge": [
            "The agent summarizes suspicious patterns and highlights a small set of claims with strong fraud indicators.",
            "It recommends which claims to send to the Special Investigations Unit and generates SIU evidence packages.",
            "Earlier fraud detection and SIU referrals reduce fraud exposure and protect claim payouts.",
            "Flagging suspected fraud early gives the manager confidence that serious risks won't be missed.",
        ],
        "synthetic_data": [
            {"case_id": "FRD77341", "claimant": "Northwind Auto", "fraud_score": 0.91, "indicator": "Duplicate invoice", "siu_referral": True},
            {"case_id": "FRD77420", "claimant": "Marcus Vale", "fraud_score": 0.44, "indicator": "None material", "siu_referral": False},
            {"case_id": "FRD78002", "claimant": "Tailspin Movers", "fraud_score": 0.87, "indicator": "Staged loss pattern", "siu_referral": True},
        ],
    },
    "auto_adjudication": {
        "title": "Simple Claim Auto-Adjudication",
        "description": "Auto-adjudicates eligible simple claims in minutes by issuing approvals and denials within guidelines, providing justifications, and showing overall efficiency gains.",
        "response": "Here are the auto-adjudication results: eligible simple claims were approved or denied within guidelines in minutes, each with a justification, alongside the overall efficiency gains.",
        "source_system": "Dynamics 365 CRM",
        "customer": "an insurance company",
        "write": True,
        "generative": True,
        "exact_key_required": True,
        "key_field": "adjudication_id",
        "triggers": [
            "auto adjudicate eligible claims",
            "issue approvals and denials within guidelines",
            "adjudicate simple claims in minutes",
            "provide justifications for decisions",
            "show efficiency gains",
        ],
        "knowledge": [
            "The agent auto-adjudicates eligible claims in minutes, issuing approvals and denials within guidelines.",
            "Every decision includes a justification and shows overall efficiency gains.",
            "Auto-adjudicating simple claims shortens cycle times and improves consistency.",
            "What once took hours or days for adjusters is now a quick controlled sequence.",
        ],
        "synthetic_data": [
            {"adjudication_id": "ADJ61208", "claimant": "Contoso Freight", "decision": "Approved", "amount": 1450, "justification": "Within policy limits"},
            {"adjudication_id": "ADJ61334", "claimant": "Priya Raman", "decision": "Denied", "amount": 0, "justification": "Coverage lapsed"},
            {"adjudication_id": "ADJ61590", "claimant": "Wingtip Rentals", "decision": "Approved", "amount": 880, "justification": "Documentation complete"},
        ],
    },
    "complex_claim_prep": {
        "title": "Complex Claim File Preparation",
        "description": "Pre-prepares complex claim files by assembling coverage summaries, key facts, missing information, and recommended actions so adjusters open each file with a clear decision-ready view instead of starting from scratch.",
        "response": "Here are the pre-prepared complex claim files: each includes a coverage summary, key facts, missing information, and recommended actions so adjusters open a clear decision-ready view.",
        "source_system": "Dynamics 365 CRM",
        "customer": "an insurance company",
        "write": False,
        "generative": True,
        "exact_key_required": True,
        "key_field": "file_id",
        "triggers": [
            "prepare complex claims with analysis for adjusters",
            "assemble coverage summaries and key facts",
            "highlight missing information and recommended actions",
            "give adjusters ready-to-review summaries",
            "pre-prepare complex claim files",
        ],
        "knowledge": [
            "The agent assembles coverage summaries, key facts, missing information, and recommended actions for complex claims.",
            "Adjusters open each file with a clear decision-ready view instead of starting from scratch.",
            "Pre-analyzing complex claims and highlighting missing documents accelerates adjudication with ready-for-review claim files.",
            "Pre-preparing complex claim files gives adjusters ready-to-review summaries.",
        ],
        "synthetic_data": [
            {"file_id": "PREP33915", "claimant": "Fabrikam Logistics", "coverage_summary": "Commercial auto, collision", "missing_info": "Police report", "recommended_action": "Request report then approve"},
            {"file_id": "PREP34028", "claimant": "Lena Ortiz", "coverage_summary": "Homeowner, water damage", "missing_info": "Repair estimate", "recommended_action": "Assign field adjuster"},
            {"file_id": "PREP34771", "claimant": "Adatum Property", "coverage_summary": "Property, fire loss", "missing_info": "None", "recommended_action": "Ready for decision"},
        ],
    },
    "performance_metrics": {
        "title": "Processing Metrics and Recap",
        "description": "Compares today's processing results to baseline, suggests targeted changes to further shorten cycle time, and shares a concise recap of claims processed, fraud prevented, and complex files prepared with leadership through Microsoft Teams.",
        "response": "Here are today's processing metrics compared to baseline, with targeted improvement suggestions and a concise recap of claims processed, fraud prevented, and complex files prepared, ready to share with leadership through Microsoft Teams.",
        "source_system": "Dynamics 365 CRM",
        "customer": "an insurance company",
        "write": True,
        "generative": True,
        "exact_key_required": True,
        "key_field": "report_id",
        "triggers": [
            "request processing metrics and improvement opportunities",
            "compare today's results to baseline",
            "suggest targeted changes to shorten cycle time",
            "provide a concise recap for leadership",
            "share recap through Microsoft Teams",
        ],
        "knowledge": [
            "The agent compares today's results to baseline and suggests targeted changes to further shorten cycle time.",
            "It provides a concise recap of claims processed, fraud prevented, and complex files prepared.",
            "The recap is ready to share with leadership through Microsoft Teams.",
            "Insights are surfaced in Microsoft Teams so the manager can see where attention is needed.",
        ],
        "synthetic_data": [
            {"report_id": "RPT20614", "metric": "Avg cycle time (hrs)", "today_value": 6, "baseline_value": 19, "improvement": "68% faster"},
            {"report_id": "RPT20615", "metric": "Claims auto-adjudicated", "today_value": 142, "baseline_value": 40, "improvement": "3.5x volume"},
            {"report_id": "RPT20616", "metric": "Fraud referrals to SIU", "today_value": 7, "baseline_value": 2, "improvement": "Earlier detection"},
        ],
    },
}

_KEY_PUNCTUATION = "-_.,:;()?!/#@+$%^&*=[]{}<>~`'\""


def _normalize_tokens(text):
    """Lowercase, strip punctuation, and split into comparable tokens."""
    tokens = []
    for raw in str(text).split():
        cleaned = "".join(ch for ch in raw.lower() if ch not in _KEY_PUNCTUATION)
        if cleaned:
            tokens.append(cleaned)
    return tokens


def _exact_key_matches(user_input, records, key_field):
    """Return records whose key_field appears as a contiguous token run in user_input."""
    query_tokens = _normalize_tokens(user_input)
    if not query_tokens:
        return []
    matches = []
    for record in records:
        key_tokens = _normalize_tokens(record.get(key_field, ""))
        width = len(key_tokens)
        if not width:
            continue
        if any(query_tokens[i:i + width] == key_tokens for i in range(len(query_tokens) - width + 1)):
            matches.append(record)
    return matches


def _format_record(record):
    """Render a synthetic record as a readable single-line summary."""
    return ", ".join(f"{key}: {value}" for key, value in record.items())


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _settlement_amount(claim):
    """Calculate recommended settlement amount."""
    policy = POLICY_DETAILS.get(claim["policy_number"], {})
    deductible = policy.get("deductible", 0)
    coverage = policy.get("coverage_limit", 0)
    claimed = claim["claimed_amount"]
    if claim["fraud_score"] >= 60:
        return 0
    net = min(claimed, coverage) - deductible
    if claim["fraud_score"] >= 30:
        net = round(net * 0.75, 2)
    return max(0, round(net, 2))


def _claims_summary():
    """Compute aggregate claims metrics."""
    total_claimed = sum(c["claimed_amount"] for c in CLAIMS.values())
    avg_fraud = sum(c["fraud_score"] for c in CLAIMS.values()) / len(CLAIMS)
    by_status = {}
    for c in CLAIMS.values():
        by_status[c["status"]] = by_status.get(c["status"], 0) + 1
    return {"total_claimed": total_claimed, "avg_fraud_score": round(avg_fraud, 1), "by_status": by_status, "count": len(CLAIMS)}


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class ClaimsProcessingAgent(BasicAgent):
    """Insurance claims processing agent."""

    def __init__(self):
        self.name = "ClaimsProcessingAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Claims Processing Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "claim_intake",
                            "adjudication_review",
                            "fraud_flag",
                            "settlement_recommendation",
                            "claim_triage",
                            "fraud_detection",
                            "auto_adjudication",
                            "complex_claim_prep",
                            "performance_metrics",
                        ],
                    },
                    "claim_id": {"type": "string"},
                    "user_input": {
                        "type": "string",
                        "description": "Optional natural-language request; enables exact-keyed record matching for the v1.1.0 capability operations.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "claim_intake")
        dispatch = {
            "claim_intake": self._claim_intake,
            "adjudication_review": self._adjudication_review,
            "fraud_flag": self._fraud_flag,
            "settlement_recommendation": self._settlement_recommendation,
            "claim_triage": self._claim_triage_capability,
            "fraud_detection": self._fraud_detection_capability,
            "auto_adjudication": self._auto_adjudication_capability,
            "complex_claim_prep": self._complex_claim_prep_capability,
            "performance_metrics": self._performance_metrics_capability,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        return handler(**kwargs)

    def _claim_intake(self, **kwargs) -> str:
        live = _live_claims()
        if live:
            open_claims = [c for c in live if c["status"] == "open"]
            lines = ["# Claims Intake Dashboard (live tenant data)\n"]
            lines.append(f"**Total Claims/Disputes:** {len(live)} ({len(open_claims)} open)")
            lines.append("**Total Claimed:** n/a — enrichment seam (wire your claims platform)")
            lines.append("**Avg Fraud Score:** n/a — enrichment seam (wire your fraud model)\n")
            lines.append("| Claim | Claimant | Matter | Priority | Filed | Status | Amount | Fraud |")
            lines.append("|---|---|---|---|---|---|---|---|")
            for c in sorted(live, key=lambda x: (x["status"] != "open", x["date_filed"])):
                lines.append(
                    f"| {c['id']} | {c['claimant']} | {c['loss_type']} | {c['priority']} "
                    f"| {c['date_filed']} | {c['status'].title()} "
                    f"| n/a — enrichment seam | n/a — enrichment seam |"
                )
            lines.append("\n_Source: live Static Dynamics 365 tenant (accounts + contacts + "
                         "incidents). A claim or dispute IS a Dynamics case at a "
                         "financial-services account or one of its member contacts; claimed "
                         "amounts and fraud scores are enrichment seams._")
            return "\n".join(lines)

        summary = _claims_summary()
        lines = ["# Claims Intake Dashboard (embedded demo data — offline)\n"]
        lines.append(f"**Total Claims:** {summary['count']}")
        lines.append(f"**Total Claimed:** ${summary['total_claimed']:,.0f}")
        lines.append(f"**Avg Fraud Score:** {summary['avg_fraud_score']}\n")
        lines.append("| Claim ID | Claimant | Policy Type | Loss | Amount | Status | Fraud |")
        lines.append("|---|---|---|---|---|---|---|")
        for cid, c in CLAIMS.items():
            lines.append(
                f"| {cid} | {c['claimant']} | {c['policy_type'].replace('_', ' ').title()} "
                f"| {c['loss_type'].replace('_', ' ').title()} | ${c['claimed_amount']:,.0f} "
                f"| {c['status'].replace('_', ' ').title()} | {c['fraud_score']} |"
            )
        lines.append("\n## Status Distribution\n")
        for status, count in summary["by_status"].items():
            lines.append(f"- {status.replace('_', ' ').title()}: {count}")
        return "\n".join(lines)

    def _adjudication_review(self, **kwargs) -> str:
        claim_id = kwargs.get("claim_id", "CLM-2025-7001")
        claim = CLAIMS.get(claim_id, list(CLAIMS.values())[0])
        policy = POLICY_DETAILS.get(claim["policy_number"], {})
        notes = ADJUSTER_NOTES.get(claim_id, [])
        lines = [f"# Adjudication Review: {claim_id}\n"]
        lines.append(f"- **Claimant:** {claim['claimant']}")
        lines.append(f"- **Policy:** {claim['policy_number']} ({claim['policy_type'].replace('_', ' ').title()})")
        lines.append(f"- **Date of Loss:** {claim['date_of_loss']}")
        lines.append(f"- **Loss Type:** {claim['loss_type'].replace('_', ' ').title()}")
        lines.append(f"- **Description:** {claim['description']}")
        lines.append(f"- **Claimed Amount:** ${claim['claimed_amount']:,.0f}")
        lines.append(f"- **Adjuster:** {claim['adjuster']}")
        lines.append(f"- **Fraud Score:** {claim['fraud_score']}/100\n")
        lines.append("## Policy Details\n")
        lines.append(f"- Coverage Limit: ${policy.get('coverage_limit', 0):,.0f}")
        lines.append(f"- Deductible: ${policy.get('deductible', 0):,.0f}")
        lines.append(f"- Effective: {policy.get('effective', 'N/A')} to {policy.get('expiry', 'N/A')}\n")
        lines.append("## Supporting Documents\n")
        for doc in claim["supporting_docs"]:
            lines.append(f"- [x] {doc.replace('_', ' ').title()}")
        if notes:
            lines.append("\n## Adjuster Notes\n")
            for note in notes:
                lines.append(f"- {note}")
        return "\n".join(lines)

    def _fraud_flag(self, **kwargs) -> str:
        lines = ["# Fraud Detection Report\n"]
        lines.append("## Fraud Indicator Reference\n")
        lines.append("| Indicator | Weight | Description |")
        lines.append("|---|---|---|")
        for ind_id, ind in FRAUD_INDICATORS.items():
            lines.append(f"| {ind_id.replace('_', ' ').title()} | {ind['weight']} | {ind['description']} |")
        flagged = {k: v for k, v in CLAIMS.items() if v["fraud_score"] >= 30}
        lines.append(f"\n## Flagged Claims (score >= 30)\n")
        if flagged:
            lines.append("| Claim ID | Claimant | Amount | Fraud Score | Status |")
            lines.append("|---|---|---|---|---|")
            for cid, c in flagged.items():
                lines.append(
                    f"| {cid} | {c['claimant']} | ${c['claimed_amount']:,.0f} "
                    f"| {c['fraud_score']} | {c['status'].replace('_', ' ').title()} |"
                )
        else:
            lines.append("No claims currently flagged.")
        high_risk = {k: v for k, v in CLAIMS.items() if v["fraud_score"] >= 60}
        if high_risk:
            lines.append("\n## SIU Referrals (score >= 60)\n")
            for cid, c in high_risk.items():
                lines.append(f"- **{cid}:** {c['claimant']} — ${c['claimed_amount']:,.0f} (score: {c['fraud_score']})")
        return "\n".join(lines)

    def _settlement_recommendation(self, **kwargs) -> str:
        lines = ["# Settlement Recommendations\n"]
        lines.append("| Claim ID | Claimant | Claimed | Deductible | Fraud Score | Recommended |")
        lines.append("|---|---|---|---|---|---|")
        for cid, c in CLAIMS.items():
            policy = POLICY_DETAILS.get(c["policy_number"], {})
            settlement = _settlement_amount(c)
            lines.append(
                f"| {cid} | {c['claimant']} | ${c['claimed_amount']:,.0f} "
                f"| ${policy.get('deductible', 0):,.0f} | {c['fraud_score']} | ${settlement:,.0f} |"
            )
        total_claimed = sum(c["claimed_amount"] for c in CLAIMS.values())
        total_recommended = sum(_settlement_amount(c) for c in CLAIMS.values())
        lines.append(f"\n**Total Claimed:** ${total_claimed:,.0f}")
        lines.append(f"**Total Recommended Settlement:** ${total_recommended:,.0f}")
        savings = total_claimed - total_recommended
        lines.append(f"**Savings from Adjustments:** ${savings:,.0f}")
        return "\n".join(lines)

    # -----------------------------------------------------------------------
    # v1.1.0 spec capability operations (backward-compatible)
    # -----------------------------------------------------------------------

    def _spec_capability(self, cap_key, **kwargs) -> str:
        """Generic, deterministic renderer for an embedded spec capability.

        Provides grounding, exact-keyed record matching against optional
        ``user_input``, a useful summary, and — for write capabilities — a
        simulated write receipt with no live mutation of any external system.
        """
        cap = SPEC_CAPABILITIES[cap_key]
        records = cap["synthetic_data"]
        key_field = cap["key_field"]
        lookup_values = []
        for field in dict.fromkeys(("user_input", key_field, "claim_id")):
            value = str(kwargs.get(field) or "").strip()
            if value:
                lookup_values.append(value)

        candidate_sets = [
            _exact_key_matches(value, records, key_field)
            for value in lookup_values
        ]
        exact_lookup = bool(candidate_sets) and all(
            len(candidates) == 1 for candidates in candidate_sets
        )
        if exact_lookup:
            matched_keys = {
                str(candidates[0][key_field]) for candidates in candidate_sets
            }
            exact_lookup = len(matched_keys) == 1
        matches = candidate_sets[0] if exact_lookup else []

        lines = [f"# {cap['title']}\n"]
        lines.append(cap["response"] + "\n")

        lines.append("## Grounded in domain knowledge\n")
        for fact in cap["knowledge"]:
            lines.append(f"- {fact}")
        lines.append(f"\n## Records — {cap['source_system']} (synthetic demo data)\n")
        lines.append(f"\n## Records — {cap['source_system']} (synthetic demo data)\n")
        receipt_target = "BATCH"
        if lookup_values and matches:
            receipt_target = str(matches[0].get(key_field, "BATCH"))
            lines.append(f"Exact match on `{key_field}`:")
            for record in matches:
                lines.append(f"- {_format_record(record)}")
        elif lookup_values:
            lines.append(
                f"No exact normalized `{key_field}` matched every supplied "
                "identifier, or the request was ambiguous. No action was simulated."
            )
        else:
            lines.append("Worked example (synthetic demo data — no customer data needed):")
            for record in records:
                lines.append(f"- {_format_record(record)}")

        if cap["write"] and (not lookup_values or matches):
            lines.append("\n## Simulated Write Receipt\n")
            lines.append("- Action Status: simulated")
            lines.append(f"- Receipt: SIM-{cap_key.upper()}-{receipt_target}")
            lines.append(f"- Target System: {cap['source_system']}")
            lines.append("- No external system changed (no live mutation).")
        elif cap["write"]:
            lines.append("\n_No write action was simulated for the rejected lookup._")
        else:
            lines.append("\n_Read-only capability — no external system is modified._")

        user_input = str(kwargs.get("user_input") or "").strip()
        if user_input and matches:
            lines.append(f"\n_(Responding to: {user_input[:160]})_")
        return "\n".join(lines)

    def _claim_triage_capability(self, **kwargs) -> str:
        return self._spec_capability("claim_triage", **kwargs)

    def _fraud_detection_capability(self, **kwargs) -> str:
        return self._spec_capability("fraud_detection", **kwargs)

    def _auto_adjudication_capability(self, **kwargs) -> str:
        return self._spec_capability("auto_adjudication", **kwargs)

    def _complex_claim_prep_capability(self, **kwargs) -> str:
        return self._spec_capability("complex_claim_prep", **kwargs)

    def _performance_metrics_capability(self, **kwargs) -> str:
        return self._spec_capability("performance_metrics", **kwargs)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = ClaimsProcessingAgent()
    print("=" * 60)
    print("LIVE TENANT CLAIMS (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="claim_intake"))
    print()
    print("=" * 60)
    print("EMBEDDED DEMO CLAIM (works offline)")
    print(agent.perform(operation="adjudication_review", claim_id="CLM-2025-7003"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="fraud_flag"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="settlement_recommendation"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(
        operation="claim_triage",
        user_input="Process today's queue and show the triage tier for claim CLM48213.",
    ))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(
        operation="fraud_detection",
        user_input="Show fraud detection results for high risk case FRD77341.",
    ))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(
        operation="auto_adjudication",
        user_input="Auto adjudicate the eligible claim ADJ61208 within guidelines.",
    ))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(
        operation="complex_claim_prep",
        user_input="Prepare the complex claim file PREP33915 with analysis for adjusters.",
    ))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="performance_metrics"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
