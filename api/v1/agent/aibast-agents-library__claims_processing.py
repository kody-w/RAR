"""
Claims Processing Agent — Financial Services Stack

Supports the insurance claims lifecycle with intake, adjudication review,
fraud flagging, and settlement recommendations.

Version 1.1.0 adds five backward-compatible capability operations derived from
the Claims Processing external agent spec (rapp-external-agent-spec/1.0):

  - claim_triage           Classify and route the incoming claims queue into tiers.
  - fraud_detection        Summarize fraud patterns and recommend SIU referrals.
  - auto_adjudication      Auto-adjudicate eligible simple claims with justifications.
  - complex_claim_prep     Pre-prepare complex claim files for adjusters.
  - performance_metrics    Compare processing metrics to baseline and recap to leadership.

Each new operation carries fully embedded, deterministic spec data (grounding
knowledge, synthetic records, triggers, responses). They accept an optional
``user_input`` for exact-keyed record matching, always return a useful summary,
and — for capabilities marked as write actions — emit a simulated write receipt
with no live mutation of any external system. The four legacy operations are
retained exactly and remain the default behavior.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/claims_processing",
    "version": "1.1.0",
    "display_name": "Claims Processing Agent",
    "description": "Insurance claims processing with intake, adjudication review, fraud detection, and settlement recommendations.",
    "author": "AIBAST",
    "tags": ["claims", "insurance", "adjudication", "fraud", "settlement", "financial-services"],
    "category": "financial_services",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# ---------------------------------------------------------------------------
# Synthetic domain data
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
        summary = _claims_summary()
        lines = ["# Claims Intake Dashboard\n"]
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
    print(agent.perform(operation="claim_intake"))
    print("\n" + "=" * 80 + "\n")
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
