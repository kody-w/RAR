---
name: "rar-aibast-agents-library-identify-discounts"
description: "Scans live quotes from a simulated Dynamics 365 tenant for discounts and expiring savings, with eligibility checks and offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/identify_discounts", "rar_sha256": "291a85fc41aab99c74b58fff0d3f4bc90a669e9c82ef14cefaae2a961b91c0d2", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["discounts", "pricing", "savings", "eligibility", "approval"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/identify_discounts`. The original RAPP
agent is preserved byte-for-byte in `identify_discounts_agent.py` and in the RCI capsule.

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

Identify Discounts Agent — a template you are meant to mutate.

Scans for applicable discounts, checks eligibility criteria, calculates
savings, and manages approval workflows for discount programs.

The live tenant has no native "vendor promotion" entity, so in this
template an open Dynamics QUOTE is read from the buying side — a priced
proposal on the table whose negotiated discount expires with the quote
window. Say the same in your own mutation if you reinterpret an entity.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live quotes over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="purchase_savings")
     — ranks the tenant's real seeded quotes (e.g. "Proposal for
     Harbor Pine Consulting", $100 negotiated discount) by savings.
  2. No network? Everything falls back to the embedded demo layer below
     (_PLANNED_PURCHASES / _DISCOUNT_PROGRAMS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     IDENTIFY_DISCOUNTS_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your ERP), or replace
     _fetch_collection() with your procurement client. The fields the
     rest of the file needs are listed in _normalize_live_quote() —
     everything else keeps working untouched.

OPERATIONS
  discount_scan | eligibility_check | savings_calculation
  | approval_workflow | purchase_savings | expiring_discounts
  | draft_purchase_order | bulk_order_strategy | execution_timeline
  | setup_tracking
  kwargs: operation (required)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The discount operation to perform",
      "enum": [
        "discount_scan",
        "eligibility_check",
        "savings_calculation",
        "approval_workflow",
        "purchase_savings",
        "expiring_discounts",
        "draft_purchase_order",
        "bulk_order_strategy",
        "execution_timeline",
        "setup_tracking"
      ],
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `identify_discounts_agent.py` and embedded as the fenced Python below (sha256 291a85fc41aab99c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `identify_discounts_agent.py` first:

```bash
python3 identify_discounts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 identify_discounts_agent.py   # or on stdin
python3 identify_discounts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify Discounts Agent — a template you are meant to mutate.

Scans for applicable discounts, checks eligibility criteria, calculates
savings, and manages approval workflows for discount programs.

The live tenant has no native "vendor promotion" entity, so in this
template an open Dynamics QUOTE is read from the buying side — a priced
proposal on the table whose negotiated discount expires with the quote
window. Say the same in your own mutation if you reinterpret an entity.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live quotes over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="purchase_savings")
     — ranks the tenant's real seeded quotes (e.g. "Proposal for
     Harbor Pine Consulting", $100 negotiated discount) by savings.
  2. No network? Everything falls back to the embedded demo layer below
     (_PLANNED_PURCHASES / _DISCOUNT_PROGRAMS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     IDENTIFY_DISCOUNTS_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your ERP), or replace
     _fetch_collection() with your procurement client. The fields the
     rest of the file needs are listed in _normalize_live_quote() —
     everything else keeps working untouched.

OPERATIONS
  discount_scan | eligibility_check | savings_calculation
  | approval_workflow | purchase_savings | expiring_discounts
  | draft_purchase_order | bulk_order_strategy | execution_timeline
  | setup_tracking
  kwargs: operation (required)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/identify_discounts",
    "version": "1.2.0",
    "display_name": "Identify Discounts",
    "description": "Scans live quotes from a simulated Dynamics 365 tenant for discounts and expiring savings, with eligibility checks and offline fallback.",
    "author": "AIBAST",
    "tags": ["discounts", "pricing", "savings", "eligibility", "approval"],
    "category": "general",
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
#   export IDENTIFY_DISCOUNTS_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your ERP/procurement client.
# Downstream code only needs the fields produced by
# _normalize_live_quote().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "IDENTIFY_DISCOUNTS_DATA_URL",
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


def _normalize_live_quote(row):
    """Project a Dynamics quote record onto the planned-purchase shape
    this agent uses. THIS is the contract your replacement data source
    must meet — a dict with these keys. 0 savings is a real zero (no
    negotiated discount on that quote); None means 'not available'."""
    amount = float(row.get("totalamount") or 0)
    savings = float(row.get("discountamount") or 0)
    gross = amount + savings
    expires = str(row.get("effectiveto", ""))[:10] or None
    return {
        "category": row.get("name", "Unnamed proposal"),
        "vendor": "Aster Lane Office Systems",
        "amount": amount,
        "savings": savings,
        "discount_pct": round(savings / gross * 100, 1) if gross else 0.0,
        "expires": expires,
        "timing": f"Convert before {expires}" if expires else "n/a — enrichment seam (wire your contract dates)",
        "status": row.get("statuscode@OData.Community.Display.V1.FormattedValue", "Open"),
        "_live": True,
    }


def _live_planned_purchases():
    """Live tenant quotes as planned purchases; [] when offline."""
    rows = _fetch_collection("quotes")
    return [_normalize_live_quote(r) for r in rows if r.get("name")]


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
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
            f"**Discount Scan: {deal['customer']}** (embedded demo deal — simulated)\n\n"
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
            f"**Eligibility Check: {deal['customer']}** (embedded demo deal — simulated)\n\n"
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
            f"**Savings Calculation: {deal['customer']}** (embedded demo deal — simulated)\n\n"
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
            f"**Approval Workflow: {deal['customer']}** (embedded demo deal — simulated)\n\n"
            f"**Discount Level:** {best_pct}% | **Required Approver:** {approval['approver']}\n\n"
            f"**Approval Matrix:**\n\n"
            f"| Discount Range | Approver | SLA | Auto-Approve Criteria |\n|---|---|---|---|\n"
            f"{approval_rows}\n"
            f"**Programs Requiring Manual Approval:** {'Yes' if needs_approval else 'None'}\n"
            f"**Estimated Approval Time:** {approval['sla_hours']} hours\n\n"
            f"Source: [Approval Engine + Deal Desk]\nAgents: IdentifyDiscountsAgent"
        )

    def _purchase_savings(self):
        live = _live_planned_purchases()
        if live:
            ranked = sorted(live, key=lambda item: item["savings"], reverse=True)
            total_savings = sum(item["savings"] for item in ranked)
            rows = "\n".join(
                f"| {item['category'][:42]} | {item['vendor']} | ${item['amount']:,.0f} | "
                f"{item['discount_pct']}% | ${item['savings']:,.0f} | {item['expires'] or 'n/a'} |"
                for item in ranked
            )
            return (
                "**Prioritized Purchase Savings** (LIVE quotes from the Aster Lane "
                "Dynamics 365 tenant, read from the buying side)\n\n"
                "| Proposal | Vendor | Quoted Spend | Discount | Savings | Quote Expires |\n"
                "|---|---|---|---|---|---|\n" + rows
                + f"\n\n**Savings snapshot:** ${total_savings:,.0f} of negotiated "
                  f"discount across {len(ranked)} open proposals. 0% rows are real "
                  "zeros — no discount negotiated yet.\n\n"
                  "Source: [Live Dynamics 365 Tenant — quotes]\n"
                  "Agents: IdentifyDiscountsAgent"
            )
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
            "**Prioritized Purchase Savings** (embedded demo data — live tenant unreachable)\n\n"
            "| Category | Vendor | Planned Spend | Discount | Savings | Expires |\n"
            "|---|---|---|---|---|---|\n" + rows
            + f"\n\n**Quarterly savings snapshot:** ${total_savings:,.0f} across "
              f"{len(ranked)} purchasing areas."
            + "\n\nSource: [Embedded Demo Layer]\n"
              "Agents: IdentifyDiscountsAgent"
        )

    def _expiring_discounts(self):
        live = _live_planned_purchases()
        discounted = [q for q in live if q["savings"] > 0]
        if discounted:
            rows = "\n".join(
                f"| {item['vendor']} | {item['category'][:42]} | {item['expires'] or 'n/a'} | "
                f"${item['savings']:,.0f} | {item['timing']} |"
                for item in sorted(discounted, key=lambda item: item["expires"] or "9999")
            )
            return (
                "**Expiring Discount Decisions** (LIVE quotes from the Aster Lane "
                "Dynamics 365 tenant)\n\n"
                "| Vendor | Proposal | Quote Expires | Savings at Risk | Recommendation |\n"
                "|---|---|---|---|---|\n" + rows
                + "\n\nSource: [Live Dynamics 365 Tenant — quotes]\nAgents: IdentifyDiscountsAgent"
            )
        rows = "\n".join(
            f"| {item['vendor']} | {item['category']} | {item['expires']} | "
            f"${item['amount'] * item['discount_pct'] / 100:,.0f} | {item['timing']} |"
            for item in sorted(_PLANNED_PURCHASES, key=lambda item: item["expires"])
        )
        return (
            "**Expiring Discount Decisions** (embedded demo data — live tenant unreachable)\n\n"
            "| Vendor | Category | Expires | Savings at Risk | Recommendation |\n"
            "|---|---|---|---|---|\n" + rows
            + "\n\nSource: [Embedded Demo Layer]\nAgents: IdentifyDiscountsAgent"
        )

    def _draft_purchase_order(self):
        items = _PLANNED_PURCHASES[:2]
        subtotal = sum(item["amount"] for item in items)
        savings = sum(item["amount"] * item["discount_pct"] / 100 for item in items)
        return (
            "**Discounted Purchase Order Draft** (embedded demo data — simulated)\n\n"
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
            "**Bulk Order Strategy** (embedded demo data — simulated)\n\n"
            f"- Consolidate facility software renewals from ${licenses['amount']:,} "
            f"to ${consolidated_amount:,} of managed spend.\n"
            f"- Unlock the {tier_discount}% volume tier.\n"
            f"- Projected consolidated savings: ${consolidated_amount * tier_discount / 100:,.0f}.\n"
            "- Preserve the current renewal window and validate unused licenses before ordering.\n\n"
            "Source: [Dynamics 365 + License Inventory]\nAgents: IdentifyDiscountsAgent"
        )

    def _execution_timeline(self):
        return (
            "**Savings Execution Timeline** (embedded demo data — simulated)\n\n"
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
    print("=" * 60)
    print("EMBEDDED DEMO DEAL (works offline)")
    print(agent.perform(operation="discount_scan"))
    print()
    print("=" * 60)
    print("LIVE TENANT QUOTES (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="purchase_savings"))
    print()
    print("=" * 60)
    print(agent.perform(operation="expiring_discounts"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
