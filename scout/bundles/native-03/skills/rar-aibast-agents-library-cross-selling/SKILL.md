---
name: "rar-aibast-agents-library-cross-selling"
description: "Builds expansion growth plans from a live simulated Dynamics 365 tenant's open pipeline, with affinity demos and an offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/cross_selling", "rar_sha256": "12d3bbf7a218d40f4e2238e57f5441f78a23b11e3e3dfe72de8d5374cf236197", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["cross-sell", "upsell", "revenue", "product-affinity", "recommendations"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/cross_selling`. The original RAPP
agent is preserved byte-for-byte in `cross_selling_agent.py` and in the RCI capsule.

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

Cross-Selling Agent — a template you are meant to mutate.

Identifies cross-selling opportunities by analyzing customer product
ownership, product affinity rules, and revenue impact projections. In
this template the expansion pipeline is fed by live Dynamics 365
opportunities — open deals become the growth plan, staged Quick Win or
Strategic by their real close probability.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `growth_plan` operation pulls live
     opportunity records over real HTTP from the globally hosted Static
     Dynamics 365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="growth_plan")
     and look for "Orchard Signal Works — Managed print fleet refresh"
     staged as a Quick Win at 60% probability.
  2. No network? Everything falls back to the embedded demo layer below
     (_PRODUCT_CATALOG / _CUSTOMER_OWNERSHIP / _AFFINITY_RULES) — the
     agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CROSS_SELLING_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from your CRM), or replace
     _fetch_collection() with your own client. The fields the rest of
     the file needs are listed in _normalize_live_expansion() — product
     affinity stays an enrichment seam until you wire your usage data.

OPERATIONS
  opportunity_scan | product_affinity | recommendation_engine
  | revenue_impact | buying_signals | outreach_plan | growth_plan
  | account_assignments
  kwargs: operation (required), customer_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "customer_id": {
      "description": "Customer ID (e.g. 'CUST-001')",
      "type": "string"
    },
    "operation": {
      "description": "The cross-selling operation to perform",
      "enum": [
        "opportunity_scan",
        "product_affinity",
        "recommendation_engine",
        "revenue_impact",
        "buying_signals",
        "outreach_plan",
        "growth_plan",
        "account_assignments"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `cross_selling_agent.py` and embedded as the fenced Python below (sha256 12d3bbf7a218d40f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `cross_selling_agent.py` first:

```bash
python3 cross_selling_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 cross_selling_agent.py   # or on stdin
python3 cross_selling_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cross-Selling Agent — a template you are meant to mutate.

Identifies cross-selling opportunities by analyzing customer product
ownership, product affinity rules, and revenue impact projections. In
this template the expansion pipeline is fed by live Dynamics 365
opportunities — open deals become the growth plan, staged Quick Win or
Strategic by their real close probability.

HOW THIS TEMPLATE WORKS
  1. Out of the box the flagship `growth_plan` operation pulls live
     opportunity records over real HTTP from the globally hosted Static
     Dynamics 365 tenant (Aster Lane Office Systems — synthetic data, no
     credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="growth_plan")
     and look for "Orchard Signal Works — Managed print fleet refresh"
     staged as a Quick Win at 60% probability.
  2. No network? Everything falls back to the embedded demo layer below
     (_PRODUCT_CATALOG / _CUSTOMER_OWNERSHIP / _AFFINITY_RULES) — the
     agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CROSS_SELLING_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from your CRM), or replace
     _fetch_collection() with your own client. The fields the rest of
     the file needs are listed in _normalize_live_expansion() — product
     affinity stays an enrichment seam until you wire your usage data.

OPERATIONS
  opportunity_scan | product_affinity | recommendation_engine
  | revenue_impact | buying_signals | outreach_plan | growth_plan
  | account_assignments
  kwargs: operation (required), customer_id
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json as _json
import urllib.request

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/cross_selling",
    "version": "1.2.0",
    "display_name": "Cross-Selling Opportunities",
    "description": "Builds expansion growth plans from a live simulated Dynamics 365 tenant's open pipeline, with affinity demos and an offline fallback.",
    "author": "AIBAST",
    "tags": ["cross-sell", "upsell", "revenue", "product-affinity", "recommendations"],
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
#   export CROSS_SELLING_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_expansion().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "CROSS_SELLING_DATA_URL",
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


def _normalize_live_expansion(row):
    """Project an open Dynamics opportunity onto the expansion shape this
    agent uses. THIS is the contract your replacement data source must
    meet — a dict with these keys. None means 'not knowable from the CRM
    alone' and the renderers label it as an enrichment seam."""
    probability = int(row.get("closeprobability") or 0)
    return {
        "account": row.get("parentaccountidname") or row.get("customeridname", "Unknown"),
        "opportunity": row.get("name", "untitled"),
        "arr": float(row.get("estimatedvalue") or 0),
        "probability": probability,
        "stage": "Quick Win" if probability >= 50 else "Strategic",
        "target_date": str(row.get("estimatedclosedate", ""))[:10],
        "affinity": None,  # enrichment seam — wire your product usage data
        "_live": True,
    }


def _live_expansions():
    """List of live tenant expansion opportunities (open); [] offline."""
    rows = _fetch_collection("opportunities")
    return [_normalize_live_expansion(row) for row in rows if row.get("statecode") == 0]


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_PRODUCT_CATALOG = {
    "PLAT-100": {"name": "Core Platform", "category": "Platform", "annual_price": 24000, "margin_pct": 72},
    "PLAT-200": {"name": "Enterprise Platform", "category": "Platform", "annual_price": 60000, "margin_pct": 75},
    "ANLYT-100": {"name": "Analytics Standard", "category": "Analytics", "annual_price": 12000, "margin_pct": 82},
    "ANLYT-200": {"name": "Analytics Pro", "category": "Analytics", "annual_price": 28000, "margin_pct": 85},
    "INTGR-100": {"name": "Integration Hub", "category": "Integration", "annual_price": 18000, "margin_pct": 78},
    "SECUR-100": {"name": "Security Suite", "category": "Security", "annual_price": 15000, "margin_pct": 80},
    "SUPRT-100": {"name": "Premium Support", "category": "Support", "annual_price": 8000, "margin_pct": 90},
    "TRAIN-100": {"name": "Training Package", "category": "Services", "annual_price": 5000, "margin_pct": 65},
}

_CUSTOMER_OWNERSHIP = {
    "CUST-001": {
        "name": "Meridian Corp", "segment": "Enterprise", "arr": 84000,
        "products": ["PLAT-200", "ANLYT-100", "SUPRT-100"],
        "tenure_months": 24, "health_score": 92, "contact": "Sandra Lee",
    },
    "CUST-002": {
        "name": "Atlas Digital", "segment": "Mid-Market", "arr": 42000,
        "products": ["PLAT-100", "INTGR-100"],
        "tenure_months": 18, "health_score": 78, "contact": "Marco Torres",
    },
    "CUST-003": {
        "name": "Pinnacle Health", "segment": "Enterprise", "arr": 60000,
        "products": ["PLAT-200"],
        "tenure_months": 6, "health_score": 85, "contact": "Dr. Amy Patel",
    },
    "CUST-004": {
        "name": "Greenleaf Retail", "segment": "Mid-Market", "arr": 24000,
        "products": ["PLAT-100"],
        "tenure_months": 12, "health_score": 65, "contact": "Kevin O'Neill",
    },
    "CUST-005": {
        "name": "Beacon Financial", "segment": "Enterprise", "arr": 113000,
        "products": ["PLAT-200", "ANLYT-200", "INTGR-100", "SECUR-100"],
        "tenure_months": 36, "health_score": 96, "contact": "Rachel Kim",
    },
}

_AFFINITY_RULES = [
    {"if_owns": "PLAT-100", "recommend": "ANLYT-100", "affinity_score": 0.85, "success_rate": 0.42, "avg_time_to_close_days": 35},
    {"if_owns": "PLAT-100", "recommend": "INTGR-100", "affinity_score": 0.72, "success_rate": 0.38, "avg_time_to_close_days": 45},
    {"if_owns": "PLAT-200", "recommend": "ANLYT-200", "affinity_score": 0.91, "success_rate": 0.55, "avg_time_to_close_days": 28},
    {"if_owns": "PLAT-200", "recommend": "SECUR-100", "affinity_score": 0.78, "success_rate": 0.48, "avg_time_to_close_days": 30},
    {"if_owns": "ANLYT-100", "recommend": "ANLYT-200", "affinity_score": 0.88, "success_rate": 0.62, "avg_time_to_close_days": 21},
    {"if_owns": "INTGR-100", "recommend": "SECUR-100", "affinity_score": 0.67, "success_rate": 0.35, "avg_time_to_close_days": 40},
    {"if_owns": "PLAT-200", "recommend": "SUPRT-100", "affinity_score": 0.82, "success_rate": 0.65, "avg_time_to_close_days": 14},
    {"if_owns": "PLAT-100", "recommend": "SUPRT-100", "affinity_score": 0.70, "success_rate": 0.50, "avg_time_to_close_days": 21},
]

_CROSS_SELL_SUCCESS_RATES = {
    "Enterprise": {"avg_success_rate": 0.52, "avg_deal_cycle_days": 28, "avg_expansion_pct": 35},
    "Mid-Market": {"avg_success_rate": 0.38, "avg_deal_cycle_days": 42, "avg_expansion_pct": 25},
    "SMB": {"avg_success_rate": 0.28, "avg_deal_cycle_days": 55, "avg_expansion_pct": 18},
}

_BUYING_SIGNALS = {
    "CUST-001": ["Analytics exports increased 38% in 30 days", "Requested predictive dashboard capability", "Budget window opens in Q4"],
    "CUST-002": ["Integration API usage reached 87% of plan", "Requested security review materials", "Renewal is due in 45 days"],
    "CUST-003": ["Added 240 active users this quarter", "Requested analytics benchmark data", "Capital committee meets in 21 days"],
    "CUST-004": ["Store count increased from 18 to 24", "Support contacts rose 22%", "Annual planning starts next month"],
    "CUST-005": ["Security adoption reached 94%", "Requested enablement for new administrators", "Training budget remains available"],
}

_REP_ASSIGNMENTS = {
    "Enterprise": ("Maya Patel", "enterprise expansion and analytics"),
    "Mid-Market": ("Jordan Kim", "mid-market adoption and integrations"),
    "SMB": ("Alex Rivera", "digital expansion"),
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _resolve_customer(query):
    if not query:
        return "CUST-001"
    q = query.upper().strip()
    return q if q in _CUSTOMER_OWNERSHIP else None


def _find_opportunities(customer_id):
    cust = _CUSTOMER_OWNERSHIP[customer_id]
    owned = set(cust["products"])
    opportunities = []
    for rule in _AFFINITY_RULES:
        if rule["if_owns"] in owned and rule["recommend"] not in owned:
            product = _PRODUCT_CATALOG[rule["recommend"]]
            opportunities.append({
                "product_id": rule["recommend"],
                "product_name": product["name"],
                "annual_price": product["annual_price"],
                "affinity_score": rule["affinity_score"],
                "success_rate": rule["success_rate"],
                "est_close_days": rule["avg_time_to_close_days"],
                "margin_pct": product["margin_pct"],
            })
    return sorted(opportunities, key=lambda x: x["affinity_score"], reverse=True)


def _calculate_revenue_impact(opportunities):
    total_arr = sum(o["annual_price"] for o in opportunities)
    weighted_arr = sum(o["annual_price"] * o["success_rate"] for o in opportunities)
    total_margin = sum(o["annual_price"] * o["margin_pct"] / 100 for o in opportunities)
    return total_arr, weighted_arr, total_margin


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class CrossSellingAgent(BasicAgent):
    """
    Cross-selling opportunity identification agent.

    Operations:
        opportunity_scan      - scan a customer for cross-sell opportunities
        product_affinity      - display product affinity rules and scores
        recommendation_engine - generate prioritized recommendations
        revenue_impact        - project revenue impact of cross-sell pipeline
        buying_signals        - surface real-time product and timing signals
        outreach_plan         - create tailored talking points and sequence
        growth_plan           - stage opportunities by conversion timeline
        account_assignments   - simulate rep assignment and Teams alignment
    """

    def __init__(self):
        self.name = "CrossSellingAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "opportunity_scan", "product_affinity",
                            "recommendation_engine", "revenue_impact",
                            "buying_signals", "outreach_plan",
                            "growth_plan", "account_assignments",
                        ],
                        "description": "The cross-selling operation to perform",
                    },
                    "customer_id": {
                        "type": "string",
                        "description": "Customer ID (e.g. 'CUST-001')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "opportunity_scan")
        cust_id = _resolve_customer(kwargs.get("customer_id", ""))
        dispatch = {
            "opportunity_scan": self._opportunity_scan,
            "product_affinity": self._product_affinity,
            "recommendation_engine": self._recommendation_engine,
            "revenue_impact": self._revenue_impact,
            "buying_signals": self._buying_signals,
            "outreach_plan": self._outreach_plan,
            "growth_plan": self._growth_plan,
            "account_assignments": self._account_assignments,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        if cust_id is None:
            return (
                f"**Error:** Unknown customer_id `{kwargs.get('customer_id')}`. "
                f"Available customer IDs: {', '.join(sorted(_CUSTOMER_OWNERSHIP))}."
            )
        return handler(cust_id)

    # ── opportunity_scan ───────────────────────────────────────
    def _opportunity_scan(self, cust_id):
        cust = _CUSTOMER_OWNERSHIP[cust_id]
        opps = _find_opportunities(cust_id)
        owned_names = [_PRODUCT_CATALOG[p]["name"] for p in cust["products"]]
        owned_list = "\n".join(f"- {n}" for n in owned_names)
        opp_rows = ""
        for o in opps:
            opp_rows += f"| {o['product_name']} | ${o['annual_price']:,}/yr | {o['affinity_score']:.0%} | {o['success_rate']:.0%} | {o['est_close_days']}d |\n"
        if not opp_rows:
            opp_rows = "| No opportunities identified | - | - | - | - |\n"
        return (
            f"**Cross-Sell Opportunity Scan: {cust['name']}**\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Segment | {cust['segment']} |\n"
            f"| Current ARR | ${cust['arr']:,} |\n"
            f"| Health Score | {cust['health_score']}/100 |\n"
            f"| Tenure | {cust['tenure_months']} months |\n"
            f"| Contact | {cust['contact']} |\n\n"
            f"**Current Products:**\n{owned_list}\n\n"
            f"**Opportunities Found ({len(opps)}):**\n\n"
            f"| Product | Price | Affinity | Success Rate | Est. Close |\n|---|---|---|---|---|\n"
            f"{opp_rows}\n\n"
            f"Source: [CRM + Product Database + Affinity Engine]\nAgents: CrossSellingAgent"
        )

    # ── product_affinity ───────────────────────────────────────
    def _product_affinity(self, cust_id):
        rule_rows = ""
        for r in _AFFINITY_RULES:
            source = _PRODUCT_CATALOG[r["if_owns"]]["name"]
            target = _PRODUCT_CATALOG[r["recommend"]]["name"]
            rule_rows += f"| {source} | {target} | {r['affinity_score']:.0%} | {r['success_rate']:.0%} | {r['avg_time_to_close_days']}d |\n"
        seg_rows = ""
        for seg, data in _CROSS_SELL_SUCCESS_RATES.items():
            seg_rows += f"| {seg} | {data['avg_success_rate']:.0%} | {data['avg_deal_cycle_days']}d | {data['avg_expansion_pct']}% |\n"
        return (
            f"**Product Affinity Matrix**\n\n"
            f"| If Customer Owns | Recommend | Affinity | Success Rate | Avg Close |\n|---|---|---|---|---|\n"
            f"{rule_rows}\n"
            f"**Segment Benchmarks:**\n\n"
            f"| Segment | Avg Success | Avg Cycle | Avg Expansion |\n|---|---|---|---|\n"
            f"{seg_rows}\n\n"
            f"Source: [Affinity Engine + Historical Data]\nAgents: CrossSellingAgent"
        )

    # ── recommendation_engine ──────────────────────────────────
    def _recommendation_engine(self, cust_id):
        cust = _CUSTOMER_OWNERSHIP[cust_id]
        opps = _find_opportunities(cust_id)
        if not opps:
            return f"**Recommendations: {cust['name']}**\n\nNo cross-sell opportunities identified. Customer owns most recommended products.\n\nSource: [Recommendation Engine]\nAgents: CrossSellingAgent"
        recs = ""
        for i, o in enumerate(opps, 1):
            weighted_value = o["annual_price"] * o["success_rate"]
            recs += (
                f"**{i}. {o['product_name']}** (${o['annual_price']:,}/yr)\n"
                f"   - Affinity Score: {o['affinity_score']:.0%}\n"
                f"   - Projected Win Rate: {o['success_rate']:.0%}\n"
                f"   - Weighted Value: ${weighted_value:,.0f}/yr\n"
                f"   - Est. Close: {o['est_close_days']} days\n\n"
            )
        total_arr, weighted_arr, _ = _calculate_revenue_impact(opps)
        return (
            f"**Prioritized Recommendations: {cust['name']}**\n\n"
            f"Health Score: {cust['health_score']}/100 | Segment: {cust['segment']}\n\n"
            f"{recs}"
            f"**Summary:**\n"
            f"- Total potential ARR: ${total_arr:,}\n"
            f"- Weighted pipeline: ${weighted_arr:,.0f}\n"
            f"- Recommendations: {len(opps)}\n\n"
            f"Source: [Recommendation Engine + CRM]\nAgents: CrossSellingAgent"
        )

    # ── revenue_impact ─────────────────────────────────────────
    def _revenue_impact(self, cust_id):
        all_opps = []
        portfolio_rows = ""
        for cid, cust in _CUSTOMER_OWNERSHIP.items():
            opps = _find_opportunities(cid)
            total_arr, weighted_arr, margin = _calculate_revenue_impact(opps)
            all_opps.extend(opps)
            portfolio_rows += f"| {cust['name']} | {cust['segment']} | ${cust['arr']:,} | {len(opps)} | ${total_arr:,} | ${weighted_arr:,.0f} |\n"
        grand_total_arr = sum(o["annual_price"] for o in all_opps)
        grand_weighted = sum(o["annual_price"] * o["success_rate"] for o in all_opps)
        grand_margin = sum(o["annual_price"] * o["margin_pct"] / 100 for o in all_opps)
        return (
            f"**Cross-Sell Revenue Impact Analysis**\n\n"
            f"| Customer | Segment | Current ARR | Opps | Potential ARR | Weighted |\n|---|---|---|---|---|---|\n"
            f"{portfolio_rows}\n"
            f"**Portfolio Totals:**\n\n"
            f"| Metric | Value |\n|---|---|\n"
            f"| Total Opportunities | {len(all_opps)} |\n"
            f"| Total Potential ARR | ${grand_total_arr:,} |\n"
            f"| Weighted Pipeline | ${grand_weighted:,.0f} |\n"
            f"| Projected Margin | ${grand_margin:,.0f} |\n\n"
            f"Source: [Revenue Analytics + CRM + Product Database]\nAgents: CrossSellingAgent"
        )

    def _buying_signals(self, cust_id):
        cust = _CUSTOMER_OWNERSHIP[cust_id]
        opps = _find_opportunities(cust_id)
        signals = "\n".join(f"- {signal}" for signal in _BUYING_SIGNALS[cust_id])
        top = opps[0] if opps else None
        return (
            f"**Buying Signals: {cust['name']}**\n\n{signals}\n\n"
            f"**Priority:** {'High' if cust['health_score'] >= 80 else 'Monitor'}\n"
            f"**Recommended Product:** {top['product_name'] if top else 'No uncovered product'}\n"
            f"**Confidence:** {top['affinity_score']:.0%}\n" if top else
            f"**Buying Signals: {cust['name']}**\n\n{signals}\n\nNo uncovered product.\n"
        ) + "\nSource: [Dynamics 365 CRM + Product Usage + Feature Requests]\nAgents: CrossSellingAgent"

    def _outreach_plan(self, cust_id):
        cust = _CUSTOMER_OWNERSHIP[cust_id]
        opps = _find_opportunities(cust_id)
        top = opps[0] if opps else None
        if not top:
            return f"**Outreach Plan: {cust['name']}**\n\nNo uncovered product to promote."
        return (
            f"**Tailored Outreach Plan: {cust['name']}**\n\n"
            f"**Contact:** {cust['contact']} | **Offer:** {top['product_name']}\n"
            f"**Talking points:**\n"
            f"- Your current adoption and peer benchmark indicate a {top['affinity_score']:.0%} product fit.\n"
            f"- The estimated annual investment is ${top['annual_price']:,}.\n"
            f"- {_BUYING_SIGNALS[cust_id][0]}.\n\n"
            f"**Sequence:** Day 0 personalized email; Day 3 value workshop; "
            f"Day 10 business-case review; Day {top['est_close_days']} decision target.\n\n"
            f"Source: [Dynamics 365 CRM + Microsoft Teams]\nAgents: CrossSellingAgent"
        )

    def _growth_plan(self, cust_id):
        live = _live_expansions()
        if live:
            rows = []
            for e in sorted(live, key=lambda x: -x["probability"]):
                rows.append(
                    f"| {e['account']} | {e['opportunity']} | {e['stage']} "
                    f"({e['probability']}%) | {e['target_date'] or 'n/a'} | ${e['arr']:,.0f} |"
                )
            weighted = sum(e["arr"] * e["probability"] / 100 for e in live)
            return (
                "**Expansion Growth Plan (live tenant)**\n\n"
                "| Account | Opportunity | Stage | Target | ARR |\n|---|---|---|---|---|\n"
                + "\n".join(rows)
                + f"\n\n**Open opportunities:** {len(live)} | "
                  f"**Weighted pipeline:** ${weighted:,.0f}\n"
                  "Product affinity is an enrichment seam — wire your usage data.\n\n"
                  "_Source: live Static Dynamics 365 tenant — open opportunities "
                  "staged by real close probability._\n"
                  "Agents: CrossSellingAgent"
            )

        rows = []
        for cid, cust in _CUSTOMER_OWNERSHIP.items():
            opps = _find_opportunities(cid)
            if not opps:
                continue
            top = opps[0]
            stage = "Quick Win" if top["est_close_days"] <= 21 else "Strategic"
            rows.append(
                f"| {cust['name']} | {top['product_name']} | {stage} | "
                f"{top['est_close_days']} days | ${top['annual_price']:,} |"
            )
        return (
            "**Expansion Growth Plan**\n\n"
            "| Account | Opportunity | Stage | Target | ARR |\n|---|---|---|---|---|\n"
            + "\n".join(rows)
            + "\n\n_Source: embedded demo layer (offline fallback)._\nAgents: CrossSellingAgent"
        )

    def _account_assignments(self, cust_id):
        rows = []
        for cid, cust in _CUSTOMER_OWNERSHIP.items():
            rep, expertise = _REP_ASSIGNMENTS[cust["segment"]]
            top = _find_opportunities(cid)
            rows.append(
                f"| {cust['name']} | {rep} | {expertise} | "
                f"{top[0]['product_name'] if top else 'Portfolio review'} | Prepared |"
            )
        return (
            "**Simulated Account Assignments**\n\n"
            "| Account | Rep | Expertise | Focus | Status |\n|---|---|---|---|---|\n"
            + "\n".join(rows)
            + "\n\nEmail templates, notifications, and a Teams alignment post are prepared "
              "but were not sent; no CRM assignments were changed.\n\n"
              "Source: [Dynamics 365 CRM + Microsoft Teams]\nAgents: CrossSellingAgent"
        )


if __name__ == "__main__":
    agent = CrossSellingAgent()
    print("=" * 60)
    print("EMBEDDED DEMO SCAN (works offline)")
    print(agent.perform(operation="opportunity_scan", customer_id="CUST-001"))
    print()
    print("=" * 60)
    print("LIVE TENANT GROWTH PLAN (opportunities fetched over HTTP; falls back offline)")
    print(agent.perform(operation="growth_plan", customer_id="CUST-001"))
    print()
    for op in [
        "product_affinity", "recommendation_engine",
        "revenue_impact", "buying_signals", "outreach_plan",
        "account_assignments",
    ]:
        print("=" * 60)
        print(agent.perform(operation=op, customer_id="CUST-001"))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
