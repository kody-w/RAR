---
name: "rar-aibast-agents-library-contract-risk-review"
description: "Scans agreements for risk and drafts renegotiation briefs from a live simulated Dynamics 365 tenant, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/contract_risk_review", "rar_sha256": "763346bca63b7e157ecfd00418cc0733d96f8235a03d931ebf79c1f374f8fb2f", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["contract", "risk", "legal", "compliance", "professional-services"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/contract_risk_review`. The original RAPP
agent is preserved byte-for-byte in `contract_risk_review_agent.py` and in the RCI capsule.

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

Contract Risk Review Agent — a template you are meant to mutate.

Scans professional-services contracts for risky clauses, checks compliance
with internal policies, and generates renegotiation briefs highlighting
liability exposure, IP concerns, and unfavorable terms.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template a Dynamics quote is reinterpreted as an active
     commercial agreement under review — e.g. quote "QUO-260108,
     Proposal for Harbor Pine Consulting".
     Try: perform(operation="risk_scan")
  2. No network? Everything falls back to the embedded demo layer below
     (CONTRACTS / CLAUSES / COMPLIANCE_REQUIREMENTS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CONTRACT_RISK_REVIEW_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your CLM), or replace
     _fetch_collection() with an Ironclad/Icertis client. Fields the
     rest of the file needs are listed in _normalize_live_contract() —
     clause-level risk renders as "n/a — enrichment seam" until you wire
     a CLM with clause extraction.

OPERATIONS
  risk_scan | clause_analysis | compliance_check | renegotiation_brief
  | implementation_package
  kwargs: operation (required), record_id, contract_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "contract_id": {
      "description": "Contract identifier, such as CTR-5001; selects all implementation-package records for that contract.",
      "type": "string"
    },
    "operation": {
      "description": "Operation to run; defaults to risk_scan when omitted.",
      "enum": [
        "risk_scan",
        "clause_analysis",
        "compliance_check",
        "renegotiation_brief",
        "implementation_package"
      ],
      "type": "string"
    },
    "record_id": {
      "description": "Evidence amendment record identifier for implementation_package, such as CRR-501.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `contract_risk_review_agent.py` and embedded as the fenced Python below (sha256 763346bca63b7e15…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `contract_risk_review_agent.py` first:

```bash
python3 contract_risk_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 contract_risk_review_agent.py   # or on stdin
python3 contract_risk_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Contract Risk Review Agent — a template you are meant to mutate.

Scans professional-services contracts for risky clauses, checks compliance
with internal policies, and generates renegotiation briefs highlighting
liability exposure, IP concerns, and unfavorable terms.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template a Dynamics quote is reinterpreted as an active
     commercial agreement under review — e.g. quote "QUO-260108,
     Proposal for Harbor Pine Consulting".
     Try: perform(operation="risk_scan")
  2. No network? Everything falls back to the embedded demo layer below
     (CONTRACTS / CLAUSES / COMPLIANCE_REQUIREMENTS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CONTRACT_RISK_REVIEW_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your CLM), or replace
     _fetch_collection() with an Ironclad/Icertis client. Fields the
     rest of the file needs are listed in _normalize_live_contract() —
     clause-level risk renders as "n/a — enrichment seam" until you wire
     a CLM with clause extraction.

OPERATIONS
  risk_scan | clause_analysis | compliance_check | renegotiation_brief
  | implementation_package
  kwargs: operation (required), record_id, contract_id
"""

import sys
import os
import json
import urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/contract_risk_review",
    "version": "1.2.0",
    "display_name": "Contract Risk Review Agent",
    "description": "Scans agreements for risk and drafts renegotiation briefs from a live simulated Dynamics 365 tenant, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["contract", "risk", "legal", "compliance", "professional-services"],
    "category": "professional_services",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export CONTRACT_RISK_REVIEW_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CLM client. Downstream
# code only needs the fields from _normalize_live_contract().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "CONTRACT_RISK_REVIEW_DATA_URL",
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


def _normalize_live_contract(row):
    """Project a Dynamics quote onto the contract-register row this agent
    renders. THIS is the contract your replacement data source must meet —
    a dict with these keys. None means 'not knowable from the commercial
    record alone' and the renderer labels it as an enrichment seam (wire a
    CLM with clause extraction for risk scoring)."""
    return {
        "id": row.get("quotenumber", "?"),
        "client": row.get("customeridname", "Unknown"),
        "title": row.get("name", "n/a"),
        "value": float(row.get("totalamount") or 0),
        "status": row.get(
            "statecode@OData.Community.Display.V1.FormattedValue", "Unknown"
        ),
        "expires": str(row.get("effectiveto") or "")[:10] or "n/a",
        "risk_score": None,   # enrichment seam — wire your CLM clause analysis
        "high_issues": None,  # enrichment seam
        "_live": True,
    }


def _live_contract_register():
    """Tenant quotes reinterpreted as the active commercial-agreement
    register; [] when offline."""
    rows = _fetch_collection("quotes")
    return sorted(
        (_normalize_live_contract(r) for r in rows),
        key=lambda c: c["value"], reverse=True,
    )


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

CONTRACTS = {
    "CTR-5001": {
        "client": "NovaTech Systems",
        "type": "Master Services Agreement",
        "value": 25000000,
        "term_months": 36,
        "governing_law": "Delaware",
        "renewal_date": "2028-06-30",
        "risk_score": 6.5,
        "pages": 47,
        "status": "under_review",
    },
    "CTR-5002": {
        "client": "Meridian Healthcare",
        "type": "Statement of Work",
        "value": 4200000,
        "term_months": 18,
        "governing_law": "New York",
        "renewal_date": "2027-09-15",
        "risk_score": 3.8,
        "pages": 22,
        "status": "active",
    },
    "CTR-5003": {
        "client": "Atlas Financial Group",
        "type": "Master Services Agreement",
        "value": 12000000,
        "term_months": 24,
        "governing_law": "California",
        "renewal_date": "2027-12-01",
        "risk_score": 5.2,
        "pages": 38,
        "status": "active",
    },
    "CTR-5004": {
        "client": "Orion Defense Systems",
        "type": "IDIQ Task Order",
        "value": 8500000,
        "term_months": 60,
        "governing_law": "Federal (FAR)",
        "renewal_date": "2030-03-31",
        "risk_score": 4.1,
        "pages": 64,
        "status": "active",
    },
}

CLAUSES = {
    "CTR-5001": [
        {"section": "7.1", "title": "Liability Cap", "risk": "HIGH",
         "issue": "Cap limited to fees paid in preceding 12 months ($2-8M range); no carve-outs for IP or data breach",
         "recommendation": "Increase to annual contract value ($8.3M minimum) with carve-outs"},
        {"section": "8.2", "title": "IP Ownership", "risk": "HIGH",
         "issue": "All work product assigned to client including improvements and derivatives; no pre-existing IP protection",
         "recommendation": "Carve out pre-existing IP; add license-back for client-specific derivatives"},
        {"section": "9.4", "title": "Payment Terms", "risk": "MEDIUM",
         "issue": "Net 60 days vs company standard Net 30; creates $1.4M cash-flow delay",
         "recommendation": "Negotiate to Net 30 or Net 45 with early-pay discount"},
        {"section": "12.1", "title": "Termination", "risk": "HIGH",
         "issue": "Client may terminate immediately for any breach with no cure period",
         "recommendation": "Add 30-day cure period for non-material breaches"},
        {"section": "14.3", "title": "SLA Penalties", "risk": "MEDIUM",
         "issue": "Penalties uncapped; could exceed monthly fees in extreme scenarios",
         "recommendation": "Cap penalties at 10% of monthly fees"},
        {"section": "15.2", "title": "Change Orders", "risk": "MEDIUM",
         "issue": "Verbal change approvals accepted; creates scope-creep exposure",
         "recommendation": "Require written change orders signed by authorized representatives"},
    ],
    "CTR-5003": [
        {"section": "5.1", "title": "Indemnification", "risk": "HIGH",
         "issue": "One-sided indemnification; we indemnify client but no reciprocal obligation",
         "recommendation": "Add mutual indemnification clause"},
        {"section": "6.3", "title": "Data Handling", "risk": "MEDIUM",
         "issue": "No data destruction timeline after engagement ends; liability lingers",
         "recommendation": "Add 90-day data destruction clause with certification"},
        {"section": "11.2", "title": "Non-Compete", "risk": "MEDIUM",
         "issue": "12-month non-compete for similar engagements in financial services sector",
         "recommendation": "Narrow scope to specific sub-sector or reduce to 6 months"},
    ],
}

COMPLIANCE_REQUIREMENTS = {
    "liability_cap_minimum": 5000000,
    "payment_terms_max_days": 45,
    "ip_preexisting_protection": True,
    "mutual_indemnification": True,
    "cure_period_days": 30,
    "data_destruction_clause": True,
    "change_order_written": True,
    "sla_penalty_cap_pct": 15,
}

RENEWAL_CALENDAR = [
    {"contract_id": "CTR-5002", "renewal_date": "2027-09-15", "days_out": 547, "action": "Begin renewal discussions Q1 2027"},
    {"contract_id": "CTR-5003", "renewal_date": "2027-12-01", "days_out": 624, "action": "Address risk clauses before renewal"},
    {"contract_id": "CTR-5001", "renewal_date": "2028-06-30", "days_out": 835, "action": "Renegotiate critical terms at Year-2 review"},
    {"contract_id": "CTR-5004", "renewal_date": "2030-03-31", "days_out": 1474, "action": "Option-year review in 2028"},
]

EVIDENCE_CAPABILITIES = {
    "implementation_package": {
        "title": "Prioritized Amendment and Redline Package",
        "write": True,
        "records": [
            {
                "record_id": "CRR-501",
                "contract_id": "CTR-5001",
                "priority": "P0",
                "benchmark": "liability cap of at least annual contract value",
                "quantified_impact": "$6.3M additional uncovered exposure at the low end",
                "amendment": "raise cap to $8.3M and add IP/data-breach carve-outs",
                "redline": "Section 7.1 replacement language prepared",
            },
            {
                "record_id": "CRR-502",
                "contract_id": "CTR-5001",
                "priority": "P0",
                "benchmark": "supplier retains pre-existing intellectual property",
                "quantified_impact": "all reusable improvements currently assigned to client",
                "amendment": "carve out pre-existing IP and add a derivative license-back",
                "redline": "Section 8.2 replacement language prepared",
            },
            {
                "record_id": "CRR-503",
                "contract_id": "CTR-5001",
                "priority": "P1",
                "benchmark": "Net 30 to Net 45 payment terms",
                "quantified_impact": "$1.4M cash-flow delay under Net 60",
                "amendment": "replace Net 60 with Net 30, fallback Net 45",
                "redline": "Section 9.4 replacement language prepared",
            },
        ],
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _high_risk_count(contract_id):
    """Count HIGH-risk clauses for a contract."""
    return sum(1 for c in CLAUSES.get(contract_id, []) if c["risk"] == "HIGH")


def _compliance_gaps(contract_id):
    """Check contract clauses against compliance requirements."""
    gaps = []
    clauses = CLAUSES.get(contract_id, [])
    clause_titles = {c["title"].lower() for c in clauses}
    ctr = CONTRACTS[contract_id]

    # Check specific known issues
    for cl in clauses:
        if cl["risk"] in ("HIGH", "MEDIUM"):
            gaps.append({"clause": cl["title"], "section": cl["section"], "severity": cl["risk"],
                         "requirement": cl["recommendation"]})
    return gaps


def _total_exposure():
    """Sum the value of contracts with risk score above 5."""
    return sum(c["value"] for c in CONTRACTS.values() if c["risk_score"] >= 5.0)


def _evidence_matches(user_input, records):
    """Match explicit evidence IDs without falling through to another contract."""
    tokens = {
        "".join(ch for ch in token.upper() if ch.isalnum())
        for token in str(user_input).split()
    }
    return [
        record for record in records
        if "".join(ch for ch in record["record_id"].upper() if ch.isalnum()) in tokens
    ]


def _evidence_selector(capability, kwargs):
    """Resolve explicit evidence or contract identifiers to evidence record IDs."""
    if kwargs.get("record_id"):
        return kwargs["record_id"]
    if kwargs.get("contract_id"):
        record_ids = [
            record["record_id"]
            for record in EVIDENCE_CAPABILITIES[capability]["records"]
            if record["contract_id"] == kwargs["contract_id"]
        ]
        return " ".join(record_ids) or kwargs["contract_id"]
    return kwargs.get("user_input", "")


def _render_evidence_operation(capability, user_input=""):
    spec = EVIDENCE_CAPABILITIES[capability]
    records = spec["records"]
    matches = _evidence_matches(user_input, records) if user_input else records
    lines = [f"## {spec['title']}\n"]
    if user_input and not matches:
        lines.append("No exact `record_id` match was found; no substitute contract was used.")
    else:
        lines.append("Benchmark-grounded, deterministic amendments:")
        for record in matches:
            lines.append("- " + "; ".join(f"{key}: {value}" for key, value in record.items()))
    target = matches[0]["record_id"] if matches else "NO-MATCH"
    lines.extend([
        "\n### Simulated Write Receipt",
        f"- receipt_id: SIM-{capability.upper()}-{target}",
        "- status: simulated",
        "- target_systems: Microsoft Word and Microsoft Teams",
        "- artifacts: redlined agreement and prioritized implementation plan",
        "- No document was edited or shared; this is a preview-only write.",
    ])
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class ContractRiskReviewAgent(BasicAgent):
    """Scans contracts for risk and generates compliance reports."""

    def __init__(self):
        self.name = "ContractRiskReviewAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "operations": [
                "risk_scan",
                "clause_analysis",
                "compliance_check",
                "renegotiation_brief",
                "implementation_package",
            ],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "description": "Operation to run; defaults to risk_scan when omitted.",
                        "enum": [
                            "risk_scan",
                            "clause_analysis",
                            "compliance_check",
                            "renegotiation_brief",
                            "implementation_package",
                        ],
                    },
                    "record_id": {
                        "type": "string",
                        "description": "Evidence amendment record identifier for implementation_package, such as CRR-501.",
                    },
                    "contract_id": {
                        "type": "string",
                        "description": "Contract identifier, such as CTR-5001; selects all implementation-package records for that contract.",
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "risk_scan")
        dispatch = {
            "risk_scan": self._risk_scan,
            "clause_analysis": self._clause_analysis,
            "compliance_check": self._compliance_check,
            "renegotiation_brief": self._renegotiation_brief,
            "implementation_package": self._implementation_package,
        }
        handler = dispatch.get(operation)
        if handler is None:
            return f"**Error:** Unknown operation `{operation}`. Valid: {', '.join(dispatch.keys())}"
        return handler(**kwargs)

    # ------------------------------------------------------------------
    def _risk_scan(self, **kwargs) -> str:
        lines = ["## Contract Risk Scan\n"]
        exposure = _total_exposure()
        total_val = sum(c["value"] for c in CONTRACTS.values())
        lines.append(f"**Active contracts:** {len(CONTRACTS)}")
        lines.append(f"**Total contract value:** ${total_val:,.0f}")
        lines.append(f"**Value at elevated risk (score >= 5.0):** ${exposure:,.0f}\n")

        lines.append("| Contract | Client | Type | Value | Term | Risk Score | HIGH Issues |")
        lines.append("|----------|--------|------|-------|------|------------|-------------|")
        ranked = sorted(CONTRACTS.items(), key=lambda x: x[1]["risk_score"], reverse=True)
        for cid, c in ranked:
            hrc = _high_risk_count(cid)
            lines.append(
                f"| {cid} | {c['client']} | {c['type']} | ${c['value']:,.0f} | "
                f"{c['term_months']}mo | {c['risk_score']}/10 | {hrc} |"
            )

        lines.append("\n### Upcoming Renewals\n")
        lines.append("| Contract | Client | Renewal Date | Days Out | Action |")
        lines.append("|----------|--------|-------------|----------|--------|")
        for r in RENEWAL_CALENDAR:
            client = CONTRACTS[r["contract_id"]]["client"]
            lines.append(f"| {r['contract_id']} | {client} | {r['renewal_date']} | {r['days_out']} | {r['action']} |")
        live = _live_contract_register()
        if live:
            seam = "n/a — enrichment seam"
            lines.append("\n### Live Tenant Agreement Register (Dynamics quotes reinterpreted as contracts)\n")
            lines.append("| Ref | Client | Title | Value | Status | Expires | Risk Score | HIGH Issues |")
            lines.append("|-----|--------|-------|-------|--------|---------|------------|-------------|")
            for c in live:
                lines.append(
                    f"| {c['id']} | {c['client']} | {c['title'][:32]} | ${c['value']:,.2f} | "
                    f"{c['status']} | {c['expires']} | {c['risk_score'] or seam} | "
                    f"{seam if c['high_issues'] is None else c['high_issues']} |"
                )
            lines.append("\n(Risk columns await a CLM with clause extraction — see the LIVE DATA SEAM.)")
        else:
            lines.append("\n_Live tenant unreachable — showing embedded demo contracts only._")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _clause_analysis(self, **kwargs) -> str:
        lines = ["## Clause-Level Risk Analysis\n"]
        for cid in CLAUSES:
            c = CONTRACTS[cid]
            lines.append(f"### {cid} -- {c['client']} (${c['value']:,.0f})\n")
            lines.append("| Section | Clause | Risk | Issue | Recommendation |")
            lines.append("|---------|--------|------|-------|----------------|")
            for cl in CLAUSES[cid]:
                lines.append(
                    f"| {cl['section']} | {cl['title']} | **{cl['risk']}** | "
                    f"{cl['issue'][:60]}... | {cl['recommendation'][:50]}... |"
                )
            high = sum(1 for cl in CLAUSES[cid] if cl["risk"] == "HIGH")
            med = sum(1 for cl in CLAUSES[cid] if cl["risk"] == "MEDIUM")
            lines.append(f"\n**Summary:** {high} HIGH, {med} MEDIUM risk clauses\n")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _compliance_check(self, **kwargs) -> str:
        lines = ["## Compliance Check Results\n"]
        lines.append("### Internal Policy Requirements\n")
        lines.append("| Requirement | Policy Standard |")
        lines.append("|-------------|----------------|")
        for key, val in COMPLIANCE_REQUIREMENTS.items():
            label = key.replace("_", " ").title()
            lines.append(f"| {label} | {val} |")

        lines.append("\n### Contract Compliance Status\n")
        for cid, c in CONTRACTS.items():
            gaps = _compliance_gaps(cid)
            status = "PASS" if not gaps else f"FAIL ({len(gaps)} gaps)"
            lines.append(f"#### {cid} -- {c['client']} -- **{status}**\n")
            if gaps:
                lines.append("| Clause | Section | Severity | Required Action |")
                lines.append("|--------|---------|----------|-----------------|")
                for g in gaps:
                    lines.append(f"| {g['clause']} | {g['section']} | {g['severity']} | {g['requirement']} |")
                lines.append("")
            else:
                lines.append("All compliance requirements met.\n")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _renegotiation_brief(self, **kwargs) -> str:
        lines = ["## Renegotiation Brief\n"]
        # Focus on highest-risk contracts
        high_risk = [(cid, c) for cid, c in CONTRACTS.items() if c["risk_score"] >= 5.0]
        high_risk.sort(key=lambda x: x[1]["risk_score"], reverse=True)

        for cid, c in high_risk:
            clauses = CLAUSES.get(cid, [])
            lines.append(f"### {cid} -- {c['client']}")
            lines.append(f"- **Value:** ${c['value']:,.0f} over {c['term_months']} months")
            lines.append(f"- **Risk score:** {c['risk_score']}/10")
            lines.append(f"- **Governing law:** {c['governing_law']}")
            lines.append(f"- **Renewal:** {c['renewal_date']}\n")

            non_negotiable = [cl for cl in clauses if cl["risk"] == "HIGH"]
            negotiable = [cl for cl in clauses if cl["risk"] == "MEDIUM"]

            if non_negotiable:
                lines.append("**Non-Negotiable Amendments (must resolve):**")
                for i, cl in enumerate(non_negotiable, 1):
                    lines.append(f"{i}. **{cl['title']}** (Section {cl['section']}): {cl['recommendation']}")
            if negotiable:
                lines.append("\n**Preferred Amendments:**")
                for i, cl in enumerate(negotiable, 1):
                    lines.append(f"{i}. **{cl['title']}** (Section {cl['section']}): {cl['recommendation']}")

            lines.append("\n**Negotiation strategy:**")
            lines.append(f"- Lead with non-negotiable items; concede on lower-priority terms if needed")
            lines.append(f"- Fallback: accept current value on MEDIUM items if all HIGH items resolved")
            lines.append(f"- Escalation path: General Counsel review if impasse on liability cap")
            lines.append("")

        total_risk_val = sum(c["value"] for _, c in high_risk)
        lines.append(f"**Total contract value requiring renegotiation:** ${total_risk_val:,.0f}")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _implementation_package(self, **kwargs) -> str:
        return _render_evidence_operation(
            "implementation_package",
            _evidence_selector("implementation_package", kwargs),
        )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = ContractRiskReviewAgent()
    print("=" * 72)
    print("EMBEDDED DEMO CONTRACTS + LIVE TENANT AGREEMENT REGISTER")
    print("(live section fetched over HTTP; falls back offline)")
    print("=" * 72)
    print(agent.perform(operation="risk_scan"))
    print()
    for op in agent.metadata["operations"][1:]:
        print("=" * 72)
        print(agent.perform(operation=op))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
