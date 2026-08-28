---
name: "rar-aibast-agents-library-proposal-generation"
description: "Analyzes RFPs and live quotes from a simulated Dynamics 365 tenant into proposal packages with pricing, plus an embedded offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/proposal_generation", "rar_sha256": "a1b7b71d3bb6e0a54079d527ac2bfa059d3ef8913475c24f107a5fd92362d5c7", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["b2b", "sales", "proposal", "rfp", "pricing", "competitive-positioning"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/proposal_generation`. The original RAPP
agent is preserved byte-for-byte in `proposal_generation_agent.py` and in the RCI capsule.

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

Proposal Generation Agent — a template you are meant to mutate.

Analyzes RFPs, generates executive summaries, builds solution pricing,
selects references, assembles proposal packages, and computes win
probability.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM quotes and opportunities over real
     HTTP from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works from anywhere).
     In this template a Dynamics QUOTE is treated as the RFP/proposal
     snapshot for its account:
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="analyze_rfp",
                  rfp_name="Juniper Ridge Furnishings")
  2. No network? Everything falls back to the embedded demo layer below
     (_RFPS / _PRODUCT_CATALOG / _REFERENCES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PROPOSAL_GENERATION_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with your own client. The dict shape the rest of
     the file needs is documented in _normalize_live_rfp(). Requirement
     extraction, cost/margin models, and competitor shortlists are
     enrichment seams — wire your RFP parser, pricing engine, and
     competitive intel there.

OPERATIONS
  analyze_rfp | executive_summary | solution_pricing
  | references_positioning | compile_proposal | delivery_summary
  | deliver_proposal
  kwargs: operation (required), rfp_name, rfp_id (deliver_proposal)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The proposal operation to perform",
      "enum": [
        "analyze_rfp",
        "executive_summary",
        "solution_pricing",
        "references_positioning",
        "compile_proposal",
        "delivery_summary",
        "deliver_proposal"
      ],
      "type": "string"
    },
    "rfp_id": {
      "description": "Exact RFP ID for deliver_proposal (e.g. 'RFP-2024-0147')",
      "type": "string"
    },
    "rfp_name": {
      "description": "RFP or account name (e.g. 'Meridian Healthcare')",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `proposal_generation_agent.py` and embedded as the fenced Python below (sha256 a1b7b71d3bb6e0a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `proposal_generation_agent.py` first:

```bash
python3 proposal_generation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 proposal_generation_agent.py   # or on stdin
python3 proposal_generation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
Proposal Generation Agent — a template you are meant to mutate.

Analyzes RFPs, generates executive summaries, builds solution pricing,
selects references, assembles proposal packages, and computes win
probability.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM quotes and opportunities over real
     HTTP from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works from anywhere).
     In this template a Dynamics QUOTE is treated as the RFP/proposal
     snapshot for its account:
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="analyze_rfp",
                  rfp_name="Juniper Ridge Furnishings")
  2. No network? Everything falls back to the embedded demo layer below
     (_RFPS / _PRODUCT_CATALOG / _REFERENCES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PROPOSAL_GENERATION_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with your own client. The dict shape the rest of
     the file needs is documented in _normalize_live_rfp(). Requirement
     extraction, cost/margin models, and competitor shortlists are
     enrichment seams — wire your RFP parser, pricing engine, and
     competitive intel there.

OPERATIONS
  analyze_rfp | executive_summary | solution_pricing
  | references_positioning | compile_proposal | delivery_summary
  | deliver_proposal
  kwargs: operation (required), rfp_name, rfp_id (deliver_proposal)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timedelta, timezone

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/proposal_generation",
    "version": "1.2.0",
    "display_name": "Proposal Generation",
    "description": "Analyzes RFPs and live quotes from a simulated Dynamics 365 tenant into proposal packages with pricing, plus an embedded offline demo fallback.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "proposal", "rfp", "pricing", "competitive-positioning"],
    "category": "b2b_sales",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). In this template a Dynamics QUOTE stands in for an
# RFP/proposal snapshot. To hook your own world, either:
#   export PROPOSAL_GENERATION_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_rfp().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "PROPOSAL_GENERATION_DATA_URL",
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


def _normalize_live_rfp(quote, opp):
    """Project a Dynamics quote (+ its opportunity) onto the RFP shape this
    agent uses. THIS is the contract your replacement data source must
    meet. In this template a quote is reinterpreted as the RFP/proposal
    snapshot; requirement extraction is an enrichment seam (wire your RFP
    parser), and competitor shortlists come from your competitive intel."""
    account = quote.get("customeridname", "Unknown")
    opp = opp or {}
    project = (opp.get("name") or quote.get("name") or account)
    if "—" in project:
        project = project.split("—", 1)[1].strip()
    quote_total = float(quote.get("totalamount") or 0)
    quote_list = float(quote.get("totallineitemamount") or 0) or quote_total
    deal_value = int(float(opp.get("estimatedvalue") or 0) or quote_total)
    try:
        close = datetime.fromisoformat(str(opp.get("estimatedclosedate", "")).replace("Z", "+00:00"))
        timeline_days = max(0, (close - datetime.now(timezone.utc)).days)
    except (ValueError, TypeError):
        timeline_days = 0
    return {
        "id": quote.get("quotenumber", "QUO-?"),
        "account": account,
        "industry": "Unknown",  # enrichment seam — wire firmographics
        "deal_value": deal_value,
        "budget_ceiling": int(quote_total) or deal_value,
        "project": project,
        "decision_timeline_days": timeline_days,
        "key_stakeholder": opp.get("parentcontactidname") or "n/a — enrichment seam",
        "competitors_shortlisted": [],  # enrichment seam — wire Crayon/Klue
        "requirements": [
            {"id": "R1", "text": project, "category": "Business", "weight": 1.0},
        ],
        "existing_assets": ["n/a — enrichment seam (wire your content library)"],
        "quote_total": quote_total,
        "quote_list": quote_list,
        "quote_status": quote.get("statecode@OData.Community.Display.V1.FormattedValue", ""),
        "_live": True,
    }


def _live_rfp_roster():
    """Account-name-keyed dict of live quotes-as-RFPs; {} when offline."""
    quotes = _fetch_collection("quotes")
    if not quotes:
        return {}
    opps_by_name = {o.get("name"): o for o in _fetch_collection("opportunities")}
    roster = {}
    for q in quotes:
        account = q.get("customeridname")
        if not account:
            continue
        opp = opps_by_name.get(q.get("opportunityidname"))
        roster.setdefault(account.lower(), _normalize_live_rfp(q, opp))
    return roster


def _pct(value):
    """None = not knowable without your cost model (enrichment seam)."""
    return "n/a — enrichment seam" if value is None else f"{value}%"


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# Stands in for CRM, Product Catalog, Reference DB, Competitive Intel
# ═══════════════════════════════════════════════════════════════

_RFPS = {
    "meridian": {
        "id": "RFP-2024-0147", "account": "Meridian Healthcare", "industry": "Healthcare",
        "deal_value": 1_200_000, "budget_ceiling": 1_250_000,
        "project": "Digital Transformation Platform",
        "decision_timeline_days": 14, "key_stakeholder": "CIO Amanda Foster",
        "competitors_shortlisted": ["CompetitorA", "CompetitorB"],
        "requirements": [
            {"id": "R1", "text": "EHR integration capabilities", "category": "Technical", "weight": 0.25},
            {"id": "R2", "text": "HIPAA compliance certification", "category": "Compliance", "weight": 0.20},
            {"id": "R3", "text": "24/7 support SLA with <15-min response", "category": "Support", "weight": 0.15},
            {"id": "R4", "text": "Implementation under 16 weeks", "category": "Delivery", "weight": 0.20},
            {"id": "R5", "text": "Comprehensive staff training program", "category": "Training", "weight": 0.10},
            {"id": "R6", "text": "Data migration from legacy systems", "category": "Technical", "weight": 0.10},
        ],
        "existing_assets": [
            "Healthcare case study (Memorial Health System)",
            "HIPAA compliance documentation",
            "Implementation methodology deck",
            "Training curriculum template",
        ],
    },
    "contoso": {
        "id": "RFP-2024-0152", "account": "Contoso Technologies", "industry": "Technology",
        "deal_value": 800_000, "budget_ceiling": 850_000,
        "project": "Cloud Migration & Modernization",
        "decision_timeline_days": 21, "key_stakeholder": "VP Engineering Alex Kim",
        "competitors_shortlisted": ["CompetitorA"],
        "requirements": [
            {"id": "R1", "text": "Multi-cloud orchestration (AWS + Azure)", "category": "Technical", "weight": 0.30},
            {"id": "R2", "text": "Zero-downtime migration methodology", "category": "Delivery", "weight": 0.25},
            {"id": "R3", "text": "SOC 2 Type II compliance", "category": "Compliance", "weight": 0.15},
            {"id": "R4", "text": "24/7 managed services post-migration", "category": "Support", "weight": 0.20},
            {"id": "R5", "text": "Knowledge transfer and runbooks", "category": "Training", "weight": 0.10},
        ],
        "existing_assets": [
            "Cloud migration playbook",
            "SOC 2 Type II audit report",
            "Multi-cloud architecture reference",
        ],
    },
    "pinnacle": {
        "id": "RFP-2024-0159", "account": "Pinnacle Financial Group", "industry": "Financial Services",
        "deal_value": 1_500_000, "budget_ceiling": 1_600_000,
        "project": "Core Banking Platform Upgrade",
        "decision_timeline_days": 30, "key_stakeholder": "CTO Marcus Webb",
        "competitors_shortlisted": ["CompetitorA", "CompetitorB", "CompetitorC"],
        "requirements": [
            {"id": "R1", "text": "Real-time transaction processing (<50ms)", "category": "Technical", "weight": 0.25},
            {"id": "R2", "text": "PCI-DSS Level 1 and SOX compliance", "category": "Compliance", "weight": 0.25},
            {"id": "R3", "text": "99.999% uptime SLA", "category": "Support", "weight": 0.20},
            {"id": "R4", "text": "Phased rollout across 120 branches", "category": "Delivery", "weight": 0.20},
            {"id": "R5", "text": "End-user and admin training certification", "category": "Training", "weight": 0.10},
        ],
        "existing_assets": [
            "Financial services case study (Atlantic Credit Union)",
            "PCI-DSS compliance package",
            "Branch rollout methodology",
        ],
    },
}

_RFP_KEYS_BY_ID = {rfp["id"]: key for key, rfp in _RFPS.items()}

_PRODUCT_CATALOG = {
    "platform_core": {"name": "Platform Core License", "list_price": 420_000, "category": "Software", "margin_floor": 0.38},
    "integration_suite": {"name": "Integration Suite", "list_price": 180_000, "category": "Software", "margin_floor": 0.40},
    "analytics_module": {"name": "Analytics & Reporting", "list_price": 80_000, "category": "Software", "margin_floor": 0.45},
    "implementation": {"name": "Implementation Services", "list_price": 380_000, "category": "Services", "margin_floor": 0.35},
    "training": {"name": "Training Program", "list_price": 120_000, "category": "Services", "margin_floor": 0.50},
    "support_3yr": {"name": "3-Year Premium Support", "list_price": 180_000, "category": "Support", "margin_floor": 0.55},
}

_SOLUTION_CONFIGS = {
    "Healthcare": ["platform_core", "integration_suite", "analytics_module", "implementation", "training", "support_3yr"],
    "Technology": ["platform_core", "integration_suite", "implementation", "training", "support_3yr"],
    "Financial Services": ["platform_core", "integration_suite", "analytics_module", "implementation", "training", "support_3yr"],
}

_DISCOUNT_RULES = {
    "Software": {"base": 0.08, "volume_threshold": 600_000, "volume_bonus": 0.03, "max": 0.15},
    "Services": {"base": 0.10, "volume_threshold": 400_000, "volume_bonus": 0.04, "max": 0.18},
    "Support": {"base": 0.25, "volume_threshold": 150_000, "volume_bonus": 0.05, "max": 0.35},
}

_REFERENCES = [
    {"customer": "Memorial Health System", "industry": "Healthcare", "size": "8 facilities",
     "results": "34% efficiency gain, $2.4M annual savings", "impl_weeks": 11, "contact_ready": True},
    {"customer": "Pacific Medical Group", "industry": "Healthcare", "size": "15 facilities",
     "results": "$2.4M savings/year, 99.9% uptime", "impl_weeks": 14, "contact_ready": True},
    {"customer": "Summit Healthcare Network", "industry": "Healthcare", "size": "6 facilities",
     "results": "12-week go-live, 28% cost reduction", "impl_weeks": 12, "contact_ready": True},
    {"customer": "Atlas Cloud Services", "industry": "Technology", "size": "800 employees",
     "results": "Zero-downtime migration, 40% infra cost reduction", "impl_weeks": 10, "contact_ready": True},
    {"customer": "Nexus Software Corp", "industry": "Technology", "size": "2,400 employees",
     "results": "3x deployment velocity, 99.95% uptime", "impl_weeks": 8, "contact_ready": False},
    {"customer": "Atlantic Credit Union", "industry": "Financial Services", "size": "120 branches",
     "results": "Sub-30ms latency, zero audit findings", "impl_weeks": 16, "contact_ready": True},
    {"customer": "Sentinel Insurance", "industry": "Financial Services", "size": "$4B AUM",
     "results": "PCI-DSS compliant in 90 days, 22% ops savings", "impl_weeks": 14, "contact_ready": True},
    {"customer": "Vanguard Logistics", "industry": "Manufacturing", "size": "3,200 employees",
     "results": "18% throughput improvement", "impl_weeks": 12, "contact_ready": False},
]

_COMPETITOR_CAPABILITIES = {
    "CompetitorA": {
        "impl_weeks": 20, "hipaa_certified": True, "ehr_integration": "Third-party",
        "support_sla_min": 240, "pricing_position": "Market rate",
        "strengths": ["Large install base", "Brand recognition"],
        "weaknesses": ["Slow implementation", "Middleware dependency"],
    },
    "CompetitorB": {
        "impl_weeks": 16, "hipaa_certified": False, "ehr_integration": "Native",
        "support_sla_min": 60, "pricing_position": "+5% above market",
        "strengths": ["Native integrations", "Modern UI"],
        "weaknesses": ["HIPAA pending", "Limited references"],
    },
    "CompetitorC": {
        "impl_weeks": 24, "hipaa_certified": True, "ehr_integration": "Third-party",
        "support_sla_min": 120, "pricing_position": "-10% below market",
        "strengths": ["Low price", "Long track record"],
        "weaknesses": ["Legacy architecture", "High customization cost"],
    },
}

_OUR_CAPABILITIES = {
    "impl_weeks": 12, "hipaa_certified": True, "ehr_integration": "Native",
    "support_sla_min": 15, "pricing_position": "Market rate",
    "certifications": ["SOC 2 Type II", "HIPAA", "ISO 27001", "PCI-DSS Level 1"],
    "differentiators": [
        "Pre-built healthcare accelerators cut implementation by 40%",
        "Native EHR integration eliminates middleware costs",
        "15-minute support SLA is fastest in industry",
        "API-first architecture for seamless ecosystem integration",
    ],
}

_IMPL_PHASES = [
    {"phase": 1, "name": "Foundation", "duration_weeks": 4,
     "activities": ["Infrastructure assessment", "Connector deployment", "Security configuration", "Core team training"]},
    {"phase": 2, "name": "Rollout", "duration_weeks": 6,
     "activities": ["Phased facility deployment", "Workflow integration", "Staff certification", "Go-live support"]},
    {"phase": 3, "name": "Optimization", "duration_weeks": 2,
     "activities": ["Performance tuning", "Advanced training", "Success metrics validation", "Handoff to support"]},
]


# ═══════════════════════════════════════════════════════════════
# HELPERS -- real computation, synthetic inputs
# ═══════════════════════════════════════════════════════════════

def _resolve_rfp(query):
    """Fuzzy-match an RFP or account name — embedded demo RFPs first,
    then the live tenant quote roster."""
    if not query:
        return "meridian"
    q = query.lower().strip()
    for key in _RFPS:
        if key in q or q in _RFPS[key]["account"].lower():
            return key
    live = _live_rfp_roster()
    for key in live:
        if key in q or q in key:
            return key
    return "meridian"


def _get_rfp(key):
    """Unified lookup: embedded demo RFPs first, then live tenant quotes."""
    if key in _RFPS:
        return _RFPS[key]
    return _live_rfp_roster().get(key) or _RFPS["meridian"]


def _match_capabilities(rfp):
    """Score how well our capabilities match each RFP requirement. Returns list of dicts + overall %."""
    cap_map = {
        "EHR integration": {"score": 95, "evidence": "Native Epic & Cerner connectors, certified"},
        "HIPAA compliance": {"score": 100, "evidence": "SOC 2 Type II + HIPAA certified"},
        "24/7 support": {"score": 98, "evidence": "24/7/365 with 15-min response SLA"},
        "15-min response": {"score": 98, "evidence": "Industry-leading 15-min SLA"},
        "Implementation under": {"score": 90, "evidence": f"{_OUR_CAPABILITIES['impl_weeks']}-week methodology with accelerators"},
        "staff training": {"score": 92, "evidence": "Role-based curriculum with certification"},
        "Data migration": {"score": 88, "evidence": "Automated migration toolkit, 50+ connectors"},
        "Multi-cloud": {"score": 91, "evidence": "AWS + Azure + GCP orchestration layer"},
        "Zero-downtime": {"score": 93, "evidence": "Blue-green deployment with automated rollback"},
        "SOC 2": {"score": 100, "evidence": "SOC 2 Type II audit current"},
        "managed services": {"score": 90, "evidence": "Dedicated SRE team, 99.99% uptime track record"},
        "Knowledge transfer": {"score": 85, "evidence": "Structured runbook and shadowing program"},
        "Real-time transaction": {"score": 87, "evidence": "Sub-30ms processing demonstrated at Atlantic CU"},
        "PCI-DSS": {"score": 100, "evidence": "PCI-DSS Level 1 certified"},
        "99.999%": {"score": 88, "evidence": "99.99% historical, architecture supports five-nines"},
        "Phased rollout": {"score": 92, "evidence": "Proven branch-by-branch methodology"},
        "certification": {"score": 90, "evidence": "LMS-integrated certification tracks"},
    }
    matches = []
    for req in rfp["requirements"]:
        best_score = 75  # default baseline
        best_evidence = "Addressed through standard platform capabilities"
        for kw, cap in cap_map.items():
            if kw.lower() in req["text"].lower():
                if cap["score"] > best_score:
                    best_score = cap["score"]
                    best_evidence = cap["evidence"]
        matches.append({
            "req_id": req["id"], "requirement": req["text"],
            "category": req["category"], "weight": req["weight"],
            "fit_score": best_score, "evidence": best_evidence,
        })
    weighted_total = sum(m["fit_score"] * m["weight"] for m in matches)
    weight_sum = sum(m["weight"] for m in matches)
    overall = round(weighted_total / weight_sum, 1) if weight_sum else 0
    return matches, overall


def _compute_pricing(rfp):
    """Build solution pricing with discounts, savings, and margin analysis.
    For LIVE quotes the real quote totals are used; margin is None because
    the CRM alone has no cost model (enrichment seam)."""
    if rfp.get("_live"):
        total_list = int(rfp["quote_list"])
        total_proposed = int(rfp["quote_total"])
        discount_pct = (round((1 - total_proposed / total_list) * 100, 1)
                        if total_list else 0.0)
        return {
            "line_items": [],
            "total_list": total_list,
            "total_proposed": total_proposed,
            "total_savings": max(0, total_list - total_proposed),
            "overall_discount_pct": max(0.0, discount_pct),
            "overall_margin_pct": None,  # enrichment seam — wire your cost model
            "budget_ceiling": rfp["budget_ceiling"],
            "within_budget": total_proposed <= rfp["budget_ceiling"],
            "budget_headroom": rfp["budget_ceiling"] - total_proposed,
        }
    industry = rfp["industry"]
    components = _SOLUTION_CONFIGS.get(industry, _SOLUTION_CONFIGS["Technology"])
    budget = rfp["budget_ceiling"]

    line_items = []
    total_list = 0
    total_proposed = 0
    total_cost = 0

    for comp_key in components:
        prod = _PRODUCT_CATALOG[comp_key]
        cat = prod["category"]
        rules = _DISCOUNT_RULES[cat]
        discount = rules["base"]
        if prod["list_price"] >= rules["volume_threshold"]:
            discount += rules["volume_bonus"]
        discount = min(discount, rules["max"])

        list_price = prod["list_price"]
        proposed = int(list_price * (1 - discount))
        cost = int(list_price * (1 - prod["margin_floor"]))
        margin_pct = round((proposed - cost) / proposed * 100, 1) if proposed else 0

        line_items.append({
            "component": prod["name"], "category": cat,
            "list_price": list_price, "discount_pct": round(discount * 100, 1),
            "proposed_price": proposed, "savings": list_price - proposed,
            "cost": cost, "margin_pct": margin_pct,
        })
        total_list += list_price
        total_proposed += proposed
        total_cost += cost

    # Adjust if proposed exceeds budget
    if total_proposed > budget:
        scale = budget / total_proposed
        for item in line_items:
            item["proposed_price"] = int(item["proposed_price"] * scale)
            item["savings"] = item["list_price"] - item["proposed_price"]
            item["margin_pct"] = round((item["proposed_price"] - item["cost"]) / max(item["proposed_price"], 1) * 100, 1)
        total_proposed = sum(i["proposed_price"] for i in line_items)

    overall_discount = round((1 - total_proposed / total_list) * 100, 1) if total_list else 0
    overall_margin = round((total_proposed - total_cost) / max(total_proposed, 1) * 100, 1)
    within_budget = total_proposed <= budget

    return {
        "line_items": line_items,
        "total_list": total_list, "total_proposed": total_proposed,
        "total_savings": total_list - total_proposed,
        "overall_discount_pct": overall_discount,
        "overall_margin_pct": overall_margin,
        "budget_ceiling": budget, "within_budget": within_budget,
        "budget_headroom": budget - total_proposed,
    }


def _score_references(industry):
    """Select and score references by industry relevance."""
    scored = []
    for ref in _REFERENCES:
        relevance = 100 if ref["industry"] == industry else 30
        if ref["contact_ready"]:
            relevance += 10
        scored.append({**ref, "relevance_score": min(relevance, 100)})
    scored.sort(key=lambda r: r["relevance_score"], reverse=True)
    return scored[:4]


def _build_differentiator_matrix(competitor_keys):
    """Build comparison matrix of us vs named competitors."""
    rows = []
    factors = [
        ("Implementation", lambda c: f"{c['impl_weeks']} weeks", f"{_OUR_CAPABILITIES['impl_weeks']} weeks"),
        ("HIPAA certified", lambda c: "Yes" if c["hipaa_certified"] else "Pending", "Yes"),
        ("EHR integration", lambda c: c["ehr_integration"], _OUR_CAPABILITIES["ehr_integration"]),
        ("Support SLA", lambda c: f"{c['support_sla_min']} min", f"{_OUR_CAPABILITIES['support_sla_min']} min"),
        ("Pricing", lambda c: c["pricing_position"], _OUR_CAPABILITIES["pricing_position"]),
    ]
    for label, comp_fn, ours in factors:
        row = {"factor": label, "us": ours}
        for ck in competitor_keys:
            comp = _COMPETITOR_CAPABILITIES.get(ck)
            row[ck] = comp_fn(comp) if comp else "N/A"
        rows.append(row)
    return rows


def _compute_win_probability(rfp, capability_score, pricing):
    """Compute win probability from fit, pricing, references, and competition factors."""
    # Capability fit factor (0-30 points)
    fit_pts = min(30, capability_score * 0.3)

    # Pricing factor (0-25 points)
    pricing_pts = 20 if pricing["within_budget"] else 10
    if pricing["budget_headroom"] > 30_000:
        pricing_pts += 5

    # Reference strength (0-20 points)
    industry_refs = [r for r in _REFERENCES if r["industry"] == rfp["industry"]]
    ref_pts = min(20, len(industry_refs) * 7)

    # Competition factor (0-25 points) -- fewer competitors = better odds
    num_competitors = len(rfp["competitors_shortlisted"])
    comp_pts = max(5, 25 - num_competitors * 7)
    # Bonus if we beat all on implementation speed
    all_slower = all(
        _COMPETITOR_CAPABILITIES.get(c, {}).get("impl_weeks", 99) > _OUR_CAPABILITIES["impl_weeks"]
        for c in rfp["competitors_shortlisted"]
    )
    if all_slower:
        comp_pts += 5

    raw = fit_pts + pricing_pts + ref_pts + comp_pts
    win_pct = min(95, max(15, int(raw)))
    return win_pct, {
        "capability_fit": round(fit_pts, 1), "pricing_strength": pricing_pts,
        "reference_strength": ref_pts, "competitive_position": min(comp_pts, 25),
    }


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class ProposalGenerationAgent(BasicAgent):
    """
    Generates complete sales proposals from RFP analysis through delivery.

    Operations:
        analyze_rfp          - Extract and score requirements from RFP
        executive_summary    - Personalized exec summary with capability match
        solution_pricing     - Phased implementation plan + optimized pricing
        references_positioning - Best references + competitive differentiator matrix
        compile_proposal     - Assemble full proposal package with page counts
        delivery_summary     - Final summary with computed win probability
        deliver_proposal     - simulate branded document delivery with receipts
    """

    def __init__(self):
        self.name = "ProposalGenerationAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "analyze_rfp", "executive_summary",
                            "solution_pricing", "references_positioning",
                            "compile_proposal", "delivery_summary",
                            "deliver_proposal",
                        ],
                        "description": "The proposal operation to perform",
                    },
                    "rfp_name": {
                        "type": "string",
                        "description": "RFP or account name (e.g. 'Meridian Healthcare')",
                    },
                    "rfp_id": {
                        "type": "string",
                        "description": "Exact RFP ID for deliver_proposal (e.g. 'RFP-2024-0147')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "analyze_rfp")
        if op == "deliver_proposal":
            return self._deliver_proposal(kwargs.get("rfp_id"))
        key = _resolve_rfp(kwargs.get("rfp_name", ""))
        dispatch = {
            "analyze_rfp": self._analyze_rfp,
            "executive_summary": self._executive_summary,
            "solution_pricing": self._solution_pricing,
            "references_positioning": self._references_positioning,
            "compile_proposal": self._compile_proposal,
            "delivery_summary": self._delivery_summary,
        }
        handler = dispatch.get(op)
        if not handler:
            return json.dumps({"status": "error", "message": f"Unknown operation: {op}"})
        return handler(key)

    def _deliver_proposal(self, rfp_id):
        key = _RFP_KEYS_BY_ID.get(rfp_id)
        if key is None:
            return json.dumps({
                "status": "error",
                "message": f"Unknown rfp_id: {rfp_id!r}",
                "valid_rfp_ids": ", ".join(sorted(_RFP_KEYS_BY_ID)),
            })
        rfp = _get_rfp(key)
        matches, overall = _match_capabilities(rfp)
        pricing = _compute_pricing(rfp)
        win_probability, _ = _compute_win_probability(rfp, overall, pricing)
        receipt = {
            "status": "simulated",
            "rfp_id": rfp_id,
            "account": rfp["account"],
            "proposal_document": f"{rfp_id.lower()}-proposal.docx",
            "presentation_deck": f"{rfp_id.lower()}-executive-deck.pptx",
            "requirement_coverage_pct": overall,
            "proposed_price": pricing["total_proposed"],
            "gross_margin_pct": pricing["overall_margin_pct"],
            "win_probability_pct": win_probability,
            "document_receipt_id": f"sim-m365-doc-{rfp_id.lower()}",
            "teams_message_id": f"sim-teams-proposal-{rfp_id.lower()}",
        }
        return "**Proposal Delivery Receipt**\n\n```json\n" + json.dumps(receipt, indent=2) + "\n```"

    # ── analyze_rfp ────────────────────────────────────────────
    def _analyze_rfp(self, key):
        rfp = _get_rfp(key)
        matches, overall = _match_capabilities(rfp)

        req_table = "| ID | Requirement | Category | Weight | Fit Score | Evidence |\n|---|---|---|---|---|---|\n"
        for m in matches:
            req_table += (
                f"| {m['req_id']} | {m['requirement']} | {m['category']} "
                f"| {int(m['weight']*100)}% | {m['fit_score']}% | {m['evidence']} |\n"
            )

        assets = "\n".join(f"- {a}" for a in rfp["existing_assets"])

        live_note = ("\n_LIVE tenant record (Static Dynamics 365): a Dynamics quote is "
                     "treated as the RFP snapshot; requirement extraction is an "
                     "enrichment seam — wire your RFP parser at the LIVE DATA SEAM._\n"
                     if rfp.get("_live") else "")
        return (
            f"**RFP Analysis: {rfp['account']} -- {rfp['project']}**\n"
            f"{live_note}\n"
            f"| Detail | Information |\n|---|---|\n"
            f"| RFP ID | {rfp['id']} |\n"
            f"| Account | {rfp['account']} |\n"
            f"| Deal value | ${rfp['deal_value']:,} |\n"
            f"| Budget ceiling | ${rfp['budget_ceiling']:,} |\n"
            f"| Decision timeline | {rfp['decision_timeline_days']} days |\n"
            f"| Key stakeholder | {rfp['key_stakeholder']} |\n"
            f"| Competitors shortlisted | {', '.join(rfp['competitors_shortlisted'])} |\n\n"
            f"**Requirements Analysis (Overall Fit: {overall}%):**\n\n{req_table}\n"
            f"**Existing Assets Found:**\n{assets}\n\n"
            f"Source: [CRM + RFP Document + Content Library]\n"
            f"Agents: RFPAnalysisAgent, ContentLibraryAgent"
        )

    # ── executive_summary ──────────────────────────────────────
    def _executive_summary(self, key):
        rfp = _get_rfp(key)
        matches, overall = _match_capabilities(rfp)
        pricing = _compute_pricing(rfp)

        needs_table = "| Your Need | Our Solution | Fit |\n|---|---|---|\n"
        for m in matches[:4]:
            needs_table += f"| {m['requirement'][:40]} | {m['evidence'][:50]} | {m['fit_score']}% |\n"

        refs = _score_references(rfp["industry"])
        top_ref = refs[0] if refs else None
        ref_line = f"\n**Proven {rfp['industry']} Success:**\n{top_ref['customer']} achieved {top_ref['results']}.\n" if top_ref else ""

        budget_status = "within budget" if pricing["within_budget"] else "requires negotiation"
        headroom = pricing["budget_headroom"]

        return (
            f"**Executive Summary: Transforming {rfp['account']}'s Future**\n\n"
            f"{rfp['account']} has an opportunity to {rfp['project'].lower()} with a solution "
            f"that matches {overall}% of stated requirements.\n\n"
            f"**Why Us:**\n\n{needs_table}\n"
            f"**Capability Match:** {overall}% overall fit score\n"
            f"**Pricing:** ${pricing['total_proposed']:,} total ({budget_status}, "
            f"${abs(headroom):,} {'under' if headroom >= 0 else 'over'} ceiling)\n"
            f"**Margin:** {_pct(pricing['overall_margin_pct'])} gross margin\n"
            f"{ref_line}\n"
            f"**Personalization Applied:**\n"
            f"- Tailored to {rfp['key_stakeholder']}'s priorities\n"
            f"- {rfp['industry']}-specific references and compliance language\n"
            f"- Matched exact RFP terminology and requirement IDs\n\n"
            f"Source: [Content Library + Stakeholder Intel]\n"
            f"Agents: ExecutiveSummaryAgent"
        )

    # ── solution_pricing ───────────────────────────────────────
    def _solution_pricing(self, key):
        rfp = _get_rfp(key)
        pricing = _compute_pricing(rfp)

        if rfp.get("_live"):
            return (
                f"**Solution & Pricing: {rfp['account']}** — LIVE quote snapshot "
                f"(Static Dynamics 365 tenant)\n\n"
                f"| Metric | Value |\n|---|---|\n"
                f"| Quote | {rfp['id']} ({rfp['quote_status']}) |\n"
                f"| Line-item total | ${pricing['total_list']:,} |\n"
                f"| Quoted total | ${pricing['total_proposed']:,} |\n"
                f"| Discount | {pricing['overall_discount_pct']}% |\n"
                f"| Gross margin | {_pct(pricing['overall_margin_pct'])} |\n\n"
                f"Component-level pricing and the implementation plan are "
                f"enrichment seams — wire your CPQ / pricing engine at the "
                f"LIVE DATA SEAM. The embedded demo RFPs show the full "
                f"phased pricing renderer.\n\n"
                f"Source: [Live Dynamics 365 quotes]\n"
                f"Agents: PricingOptimizationAgent"
            )

        # Implementation phases
        phase_lines = ""
        for p in _IMPL_PHASES:
            week_start = sum(pp["duration_weeks"] for pp in _IMPL_PHASES[:p["phase"]-1]) + 1
            week_end = week_start + p["duration_weeks"] - 1
            activities = ", ".join(p["activities"])
            phase_lines += f"\n**Phase {p['phase']}: {p['name']} (Weeks {week_start}-{week_end})**\n- {activities}\n"

        # Pricing table
        price_table = "| Component | List Price | Discount | Proposed | Savings | Margin |\n|---|---|---|---|---|---|\n"
        for item in pricing["line_items"]:
            price_table += (
                f"| {item['component']} | ${item['list_price']:,} | {item['discount_pct']}% "
                f"| ${item['proposed_price']:,} | ${item['savings']:,} | {item['margin_pct']}% |\n"
            )
        price_table += (
            f"| **Total** | **${pricing['total_list']:,}** | **{pricing['overall_discount_pct']}%** "
            f"| **${pricing['total_proposed']:,}** | **${pricing['total_savings']:,}** "
            f"| **{pricing['overall_margin_pct']}%** |\n"
        )

        budget_flag = "WITHIN" if pricing["within_budget"] else "EXCEEDS"

        return (
            f"**Solution & Pricing: {rfp['account']}**\n\n"
            f"**Implementation Approach ({_OUR_CAPABILITIES['impl_weeks']} weeks):**\n"
            f"{phase_lines}\n"
            f"**Pricing Structure:**\n\n{price_table}\n"
            f"**Budget Analysis:**\n"
            f"- Budget ceiling: ${pricing['budget_ceiling']:,}\n"
            f"- Proposed total: ${pricing['total_proposed']:,}\n"
            f"- Status: **{budget_flag}** (headroom: ${pricing['budget_headroom']:,})\n"
            f"- Overall discount: {pricing['overall_discount_pct']}%\n"
            f"- Gross margin: {pricing['overall_margin_pct']}% (floor: 35%)\n\n"
            f"Source: [Pricing Engine + Competitive Data]\n"
            f"Agents: SolutionArchitectAgent, PricingOptimizationAgent"
        )

    # ── references_positioning ─────────────────────────────────
    def _references_positioning(self, key):
        rfp = _get_rfp(key)
        refs = _score_references(rfp["industry"])
        comp_keys = rfp["competitors_shortlisted"]
        matrix = _build_differentiator_matrix(comp_keys)

        # References table
        ref_table = "| Customer | Size | Results | Relevance | Contact Ready |\n|---|---|---|---|---|\n"
        for r in refs:
            ready = "Yes" if r["contact_ready"] else "On request"
            ref_table += f"| {r['customer']} | {r['size']} | {r['results']} | {r['relevance_score']}% | {ready} |\n"

        # Differentiator matrix
        comp_headers = " | ".join(comp_keys)
        matrix_header = f"| Factor | Us | {comp_headers} |\n|---|---|" + "---|" * len(comp_keys) + "\n"
        matrix_rows = ""
        for row in matrix:
            comp_vals = " | ".join(str(row.get(ck, "N/A")) for ck in comp_keys)
            matrix_rows += f"| {row['factor']} | {row['us']} | {comp_vals} |\n"

        # Objection pre-handlers from differentiators
        objections = "\n".join(f"- \"{d}\"" for d in _OUR_CAPABILITIES["differentiators"][:3])

        # Win theme
        our_impl = _OUR_CAPABILITIES["impl_weeks"]
        fastest = all(
            _COMPETITOR_CAPABILITIES.get(c, {}).get("impl_weeks", 99) > our_impl
            for c in comp_keys
        )
        theme = "Speed + Compliance + Support" if fastest else "Compliance + Integration + Support"

        return (
            f"**References & Competitive Positioning: {rfp['account']}**\n\n"
            f"**Customer References ({rfp['industry']}-weighted):**\n\n{ref_table}\n"
            f"**Win Theme: {theme}**\n\n"
            f"**Competitive Differentiator Matrix:**\n\n{matrix_header}{matrix_rows}\n"
            f"**Objection Pre-Handlers:**\n{objections}\n\n"
            f"Source: [Reference Database + Competitive Intel]\n"
            f"Agents: CompetitiveDifferentiationAgent, ContentLibraryAgent"
        )

    # ── compile_proposal ───────────────────────────────────────
    def _compile_proposal(self, key):
        rfp = _get_rfp(key)
        pricing = _compute_pricing(rfp)
        matches, overall = _match_capabilities(rfp)
        refs = _score_references(rfp["industry"])

        num_reqs = len(rfp["requirements"])
        num_refs = len(refs)
        num_comps = len(rfp["competitors_shortlisted"])
        # Estimate page count from content sections
        page_count = 12 + num_reqs * 2 + num_refs * 2 + num_comps * 3 + 4

        sections = [
            ("Executive Summary (personalized)", 3),
            (f"Company Overview + {rfp['industry']} Expertise", 4),
            ("Solution Architecture + Roadmap", 6),
            (f"Implementation Methodology ({_OUR_CAPABILITIES['impl_weeks']}-week plan)", 5),
            ("Pricing + Investment Summary", 4),
            (f"Customer References + Case Studies ({num_refs})", num_refs * 2),
            ("Team Bios (Industry specialists)", 3),
            ("Terms + Conditions", 3),
        ]

        section_list = "\n".join(f"{i}. {name} ({pages} pages)" for i, (name, pages) in enumerate(sections, 1))

        certs_found = [c for c in _OUR_CAPABILITIES["certifications"]
                       if any(c.lower() in req["text"].lower() for req in rfp["requirements"])]
        cert_attachments = "\n".join(f"- {c} documentation (attached)" for c in certs_found) if certs_found else "- Standard compliance package"

        return (
            f"**Proposal Package: {rfp['account']} -- {rfp['project']}**\n\n"
            f"**Main Document ({page_count} pages):**\n{section_list}\n\n"
            f"**Supporting Materials:**\n{cert_attachments}\n"
            f"- {refs[0]['customer']} case study (2 pages)\n"
            f"- Implementation timeline visual (1 page)\n\n"
            f"**Delivery Package:**\n"
            f"- PDF proposal (branded template)\n"
            f"- Executive presentation (12 slides)\n"
            f"- Pricing spreadsheet (detailed breakdown)\n"
            f"- Reference contact sheet ({num_refs} contacts)\n\n"
            f"**Pre-Delivery Checklist:**\n"
            f"- Legal review: Approved\n"
            f"- Pricing approval: margin {_pct(pricing['overall_margin_pct'])} (floor: 35%)\n"
            f"- Branding: Compliant\n"
            f"- Requirement coverage: {overall}% fit verified\n"
            f"- Spell check: Complete\n\n"
            f"Source: [Document Assembly + Compliance Check]\n"
            f"Agents: ProposalAssemblyAgent"
        )

    # ── delivery_summary ───────────────────────────────────────
    def _delivery_summary(self, key):
        rfp = _get_rfp(key)
        matches, overall = _match_capabilities(rfp)
        pricing = _compute_pricing(rfp)
        refs = _score_references(rfp["industry"])
        win_pct, factors = _compute_win_probability(rfp, overall, pricing)

        factor_table = "| Factor | Score | Max |\n|---|---|---|\n"
        factor_table += f"| Capability fit | {factors['capability_fit']} | 30 |\n"
        factor_table += f"| Pricing strength | {factors['pricing_strength']} | 25 |\n"
        factor_table += f"| Reference strength | {factors['reference_strength']} | 20 |\n"
        factor_table += f"| Competitive position | {factors['competitive_position']} | 25 |\n"
        factor_table += f"| **Total** | **{win_pct}** | **100** |\n"

        return (
            f"**Delivery Summary: {rfp['account']} -- {rfp['project']}**\n\n"
            f"| Element | Status |\n|---|---|\n"
            f"| Capability match | {overall}% fit to {len(rfp['requirements'])} requirements |\n"
            f"| Executive summary | Personalized to {rfp['key_stakeholder']} |\n"
            f"| Solution | {_OUR_CAPABILITIES['impl_weeks']}-week implementation plan |\n"
            f"| Pricing | ${pricing['total_proposed']:,} ({pricing['overall_discount_pct']}% discount, {_pct(pricing['overall_margin_pct'])} margin) |\n"
            f"| References | {len(refs)} {rfp['industry']}-specific, contact-ready |\n"
            f"| Compliance | {', '.join(_OUR_CAPABILITIES['certifications'][:3])} included |\n\n"
            f"**Win Probability: {win_pct}%**\n\n{factor_table}\n"
            f"**Session Accomplishments:**\n"
            f"- RFP requirements mapped to capabilities ({overall}% fit)\n"
            f"- Executive summary personalized to {rfp['key_stakeholder']}\n"
            f"- Competitive positioning vs {len(rfp['competitors_shortlisted'])} shortlisted vendors\n"
            f"- Pricing optimized (${pricing['total_savings']:,} discount, {pricing['overall_margin_pct']}% margin protected)\n"
            f"- Full proposal package assembled\n\n"
            f"**Delivery Recommendation:**\n"
            f"- Submit within {rfp['decision_timeline_days']} day window\n"
            f"- Request confirmation meeting within 48 hours\n"
            f"- Offer reference calls proactively\n"
            f"- CC executive sponsor for alignment\n\n"
            f"Source: [All Proposal Systems]\n"
            f"Agents: ProposalAssemblyAgent (orchestrating all agents)"
        )


if __name__ == "__main__":
    agent = ProposalGenerationAgent()
    print("=" * 70)
    print("EMBEDDED DEMO RFP (works offline)")
    print(agent.perform(operation="analyze_rfp", rfp_name="Meridian Healthcare"))
    print()
    print("=" * 70)
    print("LIVE TENANT QUOTE-AS-RFP (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="analyze_rfp", rfp_name="Juniper Ridge Furnishings"))
    print()
    print("=" * 70)
    print(agent.perform(operation="solution_pricing", rfp_name="Juniper Ridge Furnishings"))
    print()
    print("=" * 70)
    print(agent.perform(operation="delivery_summary", rfp_name="Meridian Healthcare"))
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
