---
name: "rar-aibast-agents-library-personalized-marketing"
description: "Segments live audiences and designs campaigns from a live simulated Dynamics 365 tenant's contacts and orders, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/personalized_marketing", "rar_sha256": "6092f9183c36ec5135ef15dcb022012a8d9a0f86f87ea2595629ab1eac566e1f", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["marketing", "personalization", "segmentation", "campaigns", "retail"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/personalized_marketing`. The original RAPP
agent is preserved byte-for-byte in `personalized_marketing_agent.py` and in the RCI capsule.

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

Personalized Marketing Agent — a template you are meant to mutate.

Drives customer segmentation, campaign design, content personalization,
and performance analysis for targeted retail marketing programs.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live contacts and sales orders over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="customer_segmentation")
     — with network up, segments are derived from the tenant's 40 live
     contacts (e.g. Marcus Webb at Bluegrass Credit Union) and real
     sales-order spend per account.
  2. No network? Everything falls back to the embedded demo layer below
     (CUSTOMER_SEGMENTS / CAMPAIGN_TEMPLATES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PERSONALIZED_MARKETING_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your CDP/ESP), or replace
     _fetch_collection() with your own audience API. The fields the rest
     of the file needs are listed in _normalize_live_customer() — LTV and
     engagement stay "n/a — enrichment seam" until you wire your loyalty
     or analytics system.

OPERATIONS
  customer_segmentation | campaign_design | content_personalization |
  performance_analysis | holiday_campaign_plan | creative_ab_test |
  campaign_scheduling | revenue_scenarios
  kwargs: operation (required), segment_id, campaign_id, key, user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "campaign_id": {
      "type": "string"
    },
    "key": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "customer_segmentation",
        "campaign_design",
        "content_personalization",
        "performance_analysis",
        "holiday_campaign_plan",
        "creative_ab_test",
        "campaign_scheduling",
        "revenue_scenarios"
      ],
      "type": "string"
    },
    "segment_id": {
      "type": "string"
    },
    "user_input": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `personalized_marketing_agent.py` and embedded as the fenced Python below (sha256 6092f9183c36ec51…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `personalized_marketing_agent.py` first:

```bash
python3 personalized_marketing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 personalized_marketing_agent.py   # or on stdin
python3 personalized_marketing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Personalized Marketing Agent — a template you are meant to mutate.

Drives customer segmentation, campaign design, content personalization,
and performance analysis for targeted retail marketing programs.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live contacts and sales orders over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="customer_segmentation")
     — with network up, segments are derived from the tenant's 40 live
     contacts (e.g. Marcus Webb at Bluegrass Credit Union) and real
     sales-order spend per account.
  2. No network? Everything falls back to the embedded demo layer below
     (CUSTOMER_SEGMENTS / CAMPAIGN_TEMPLATES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PERSONALIZED_MARKETING_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your CDP/ESP), or replace
     _fetch_collection() with your own audience API. The fields the rest
     of the file needs are listed in _normalize_live_customer() — LTV and
     engagement stay "n/a — enrichment seam" until you wire your loyalty
     or analytics system.

OPERATIONS
  customer_segmentation | campaign_design | content_personalization |
  performance_analysis | holiday_campaign_plan | creative_ab_test |
  campaign_scheduling | revenue_scenarios
  kwargs: operation (required), segment_id, campaign_id, key, user_input
"""

import sys
import os

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"),
)
from basic_agent import BasicAgent
import json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/personalized_marketing",
    "version": "1.2.0",
    "display_name": "Personalized Marketing Agent",
    "description": (
        "Segments live audiences and designs campaigns from a live simulated Dynamics 365 tenant's contacts and orders, with an offline demo fallback."
    ),
    "author": "AIBAST",
    "tags": [
        "marketing",
        "personalization",
        "segmentation",
        "campaigns",
        "retail",
    ],
    "category": "retail_cpg",
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
#   export PERSONALIZED_MARKETING_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CDP/CRM client. Downstream
# code only needs the fields produced by _normalize_live_customer().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "PERSONALIZED_MARKETING_DATA_URL",
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


def _normalize_live_customer(row, spend_by_account):
    """Project a Dynamics contact record onto the shape this agent uses.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not available from CRM alone' and the
    renderers label it as an enrichment seam."""
    account = row.get("parentcustomeridname", "")
    return {
        "name": row.get("fullname", "Unknown"),
        "account": account or "(individual)",
        "title": row.get("jobtitle", ""),
        "city": row.get("address1_city", ""),
        "email_on_file": bool(row.get("emailaddress1")),
        "spend": spend_by_account.get(account, 0.0),
        "lifetime_value": None,     # enrichment seam — wire loyalty/analytics
        "engagement_score": None,   # enrichment seam
        "_live": True,
    }


def _live_spend_by_account():
    """Total live sales-order value per account name; {} when offline."""
    spend = {}
    for order in _fetch_collection("salesorders"):
        name = order.get("customeridname")
        if name:
            spend[name] = spend.get(name, 0.0) + float(order.get("totalamount") or 0)
    return spend


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback) — Customer Segments
# ---------------------------------------------------------------------------

CUSTOMER_SEGMENTS = {
    "SEG-LOYAL": {
        "name": "Loyal Advocates",
        "size": 42850,
        "avg_age": 38,
        "gender_split": {"female": 0.56, "male": 0.42, "other": 0.02},
        "avg_annual_spend": 1875.00,
        "avg_orders_per_year": 18.3,
        "avg_basket_size": 102.46,
        "preferred_channels": ["in_store", "mobile_app"],
        "top_categories": ["Apparel", "Footwear", "Accessories"],
        "churn_risk": 0.04,
        "lifetime_value": 11250.00,
        "engagement_score": 92,
    },
    "SEG-ATRISK": {
        "name": "At-Risk Churners",
        "size": 18420,
        "avg_age": 44,
        "gender_split": {"female": 0.48, "male": 0.50, "other": 0.02},
        "avg_annual_spend": 620.00,
        "avg_orders_per_year": 5.1,
        "avg_basket_size": 121.57,
        "preferred_channels": ["email", "desktop_web"],
        "top_categories": ["Electronics", "Home"],
        "churn_risk": 0.38,
        "lifetime_value": 3720.00,
        "engagement_score": 31,
    },
    "SEG-NEW": {
        "name": "New Explorers",
        "size": 27600,
        "avg_age": 26,
        "gender_split": {"female": 0.51, "male": 0.45, "other": 0.04},
        "avg_annual_spend": 340.00,
        "avg_orders_per_year": 3.8,
        "avg_basket_size": 89.47,
        "preferred_channels": ["social_media", "mobile_app"],
        "top_categories": ["Apparel", "Beauty", "Accessories"],
        "churn_risk": 0.22,
        "lifetime_value": 2040.00,
        "engagement_score": 58,
    },
    "SEG-HIGHVAL": {
        "name": "High-Value VIPs",
        "size": 8750,
        "avg_age": 47,
        "gender_split": {"female": 0.60, "male": 0.38, "other": 0.02},
        "avg_annual_spend": 4200.00,
        "avg_orders_per_year": 24.6,
        "avg_basket_size": 170.73,
        "preferred_channels": ["in_store", "mobile_app", "email"],
        "top_categories": ["Premium Apparel", "Footwear", "Jewelry"],
        "churn_risk": 0.06,
        "lifetime_value": 33600.00,
        "engagement_score": 97,
    },
    "SEG-DORMANT": {
        "name": "Dormant Lapsed",
        "size": 34200,
        "avg_age": 41,
        "gender_split": {"female": 0.47, "male": 0.51, "other": 0.02},
        "avg_annual_spend": 85.00,
        "avg_orders_per_year": 0.8,
        "avg_basket_size": 106.25,
        "preferred_channels": ["email"],
        "top_categories": ["Home", "Electronics"],
        "churn_risk": 0.72,
        "lifetime_value": 510.00,
        "engagement_score": 9,
    },
}

CAMPAIGN_TEMPLATES = {
    "CAMP-WINBACK": {
        "name": "Win-Back Journey",
        "type": "automated_email",
        "target_segment": "SEG-DORMANT",
        "stages": 4,
        "duration_days": 28,
        "discount_offer": "20% off next purchase",
        "subject_lines": [
            "We miss you — here is 20% off",
            "Your favorites are waiting",
            "Last chance: exclusive offer inside",
            "Final reminder: your 20% expires tomorrow",
        ],
        "historical_open_rate": 0.18,
        "historical_click_rate": 0.04,
        "historical_conversion_rate": 0.012,
    },
    "CAMP-LOYALTY": {
        "name": "Loyalty Tier Upgrade",
        "type": "multi_channel",
        "target_segment": "SEG-LOYAL",
        "stages": 3,
        "duration_days": 14,
        "discount_offer": "Early access + double points",
        "subject_lines": [
            "You are almost Gold status!",
            "Earn double points this weekend",
            "Congratulations on your tier upgrade",
        ],
        "historical_open_rate": 0.42,
        "historical_click_rate": 0.15,
        "historical_conversion_rate": 0.08,
    },
    "CAMP-NEWWELCOME": {
        "name": "New Customer Welcome",
        "type": "automated_email",
        "target_segment": "SEG-NEW",
        "stages": 5,
        "duration_days": 30,
        "discount_offer": "15% off first order over $50",
        "subject_lines": [
            "Welcome! Here is 15% off your first order",
            "Discover our best sellers",
            "Complete your look — curated picks",
            "Your style profile is ready",
            "Join our rewards program today",
        ],
        "historical_open_rate": 0.35,
        "historical_click_rate": 0.11,
        "historical_conversion_rate": 0.055,
    },
    "CAMP-VIP": {
        "name": "VIP Exclusive Preview",
        "type": "multi_channel",
        "target_segment": "SEG-HIGHVAL",
        "stages": 2,
        "duration_days": 7,
        "discount_offer": "Private sale — 30% off new collection",
        "subject_lines": [
            "VIP Only: private sale starts now",
            "Your exclusive early access ends tonight",
        ],
        "historical_open_rate": 0.58,
        "historical_click_rate": 0.24,
        "historical_conversion_rate": 0.14,
    },
}

AB_TEST_RESULTS = {
    "ABT-001": {
        "campaign": "CAMP-WINBACK",
        "variant_a": {"subject": "We miss you — here is 20% off", "open_rate": 0.18, "click_rate": 0.04, "conversions": 82},
        "variant_b": {"subject": "Come back for something special", "open_rate": 0.21, "click_rate": 0.05, "conversions": 107},
        "winner": "B",
        "confidence": 0.94,
        "sample_size": 8500,
    },
    "ABT-002": {
        "campaign": "CAMP-LOYALTY",
        "variant_a": {"subject": "You are almost Gold status!", "open_rate": 0.42, "click_rate": 0.15, "conversions": 341},
        "variant_b": {"subject": "Unlock Gold rewards today", "open_rate": 0.39, "click_rate": 0.13, "conversions": 298},
        "winner": "A",
        "confidence": 0.91,
        "sample_size": 6200,
    },
    "ABT-003": {
        "campaign": "CAMP-VIP",
        "variant_a": {"subject": "VIP Only: private sale starts now", "open_rate": 0.58, "click_rate": 0.24, "conversions": 215},
        "variant_b": {"subject": "Your private collection awaits", "open_rate": 0.61, "click_rate": 0.27, "conversions": 248},
        "winner": "B",
        "confidence": 0.88,
        "sample_size": 3400,
    },
}

CONTENT_BLOCKS = {
    "hero_banner": {
        "SEG-LOYAL": {"headline": "Thank You for Being a Loyal Customer", "cta": "Shop Your Rewards"},
        "SEG-ATRISK": {"headline": "We Have Something Special for You", "cta": "Rediscover Your Favorites"},
        "SEG-NEW": {"headline": "Welcome to the Family", "cta": "Start Shopping"},
        "SEG-HIGHVAL": {"headline": "Exclusive Access Just for You", "cta": "View Private Collection"},
        "SEG-DORMANT": {"headline": "It Has Been a While — Come Back", "cta": "See What Is New"},
    },
    "product_recs": {
        "SEG-LOYAL": ["Classic Denim Jacket", "Premium Running Shoes", "Leather Crossbody Bag"],
        "SEG-ATRISK": ["Wireless Earbuds Pro", "Smart Fitness Tracker"],
        "SEG-NEW": ["Organic Cotton T-Shirt", "Stainless Water Bottle", "UV Protection Sunglasses"],
        "SEG-HIGHVAL": ["Limited Edition Blazer", "Designer Handbag", "Artisan Watch"],
        "SEG-DORMANT": ["Best Sellers Bundle", "Gift Card"],
    },
}

VIP_REVENUE_AUDIENCE = 12400

VIP_REVENUE_SCENARIO_INPUTS = {
    "conservative": {
        "open_rate": 0.68,
        "click_rate": 0.24,
        "conversion_rate": 0.124,
        "average_order_value": 340,
    },
    "expected": {
        "open_rate": 0.72,
        "click_rate": 0.28,
        "conversion_rate": 0.142,
        "average_order_value": 380,
    },
    "optimistic": {
        "open_rate": 0.78,
        "click_rate": 0.32,
        "conversion_rate": 0.168,
        "average_order_value": 420,
    },
}


def _calculate_scenario_revenue(audience, conversion_rate, average_order_value):
    return round(audience * conversion_rate * average_order_value, 2)


def _format_revenue_scenario(scenario):
    revenue = _calculate_scenario_revenue(
        VIP_REVENUE_AUDIENCE,
        scenario["conversion_rate"],
        scenario["average_order_value"],
    )
    return (
        f"{scenario['open_rate']:.0%} open; "
        f"{scenario['click_rate']:.0%} click; "
        f"{scenario['conversion_rate']:.1%} conversion; "
        f"${scenario['average_order_value']:,.0f} average order; "
        f"${revenue:,.2f} revenue"
    )


def _validate_revenue_formula_contract():
    expected_revenue = {
        "conservative": 522784,
        "expected": 669104,
        "optimistic": 874944,
    }
    for name, scenario in VIP_REVENUE_SCENARIO_INPUTS.items():
        actual = _calculate_scenario_revenue(
            VIP_REVENUE_AUDIENCE,
            scenario["conversion_rate"],
            scenario["average_order_value"],
        )
        assert actual == expected_revenue[name]

    baseline = expected_revenue["expected"]
    assert _calculate_scenario_revenue(
        VIP_REVENUE_AUDIENCE * 2, 0.142, 380
    ) == baseline * 2
    assert _calculate_scenario_revenue(
        VIP_REVENUE_AUDIENCE, 0.152, 380
    ) == baseline + 47120
    assert _calculate_scenario_revenue(
        VIP_REVENUE_AUDIENCE, 0.142, 400
    ) == baseline + 35216


EVIDENCE_CAPABILITIES = {
    "holiday_campaign_plan": {
        "title": "High-Value Holiday Campaign Plan",
        "source_system": "Dynamics 365 Customer Insights",
        "write": False,
        "key_field": "campaign_id",
        "summary": (
            "Connects behavior-and-value segmentation to a complete multi-wave "
            "holiday campaign strategy with segment-level performance."
        ),
        "record": {
            "campaign_id": "HOLIDAY-VIP-2026",
            "customer_base": "240,000 active customers across five value segments",
            "priority_segment": "VIP Shoppers; 12,400 customers; $340 average order; 12.4% predicted conversion",
            "waves": "VIP launch day; Frequent Buyers day 2; Seasonal Shoppers day 5; New Subscribers day 7",
            "offers": "VIP 30% early access; favorites sale; holiday gifts with free shipping; 40% welcome offer",
            "projection": "$8.12M revenue from a $47,000 campaign investment",
            "strategy": "Launch VIP first, then expand sequentially using segment behavior",
        },
    },
    "creative_ab_test": {
        "title": "Personalized Creative and A/B Test",
        "source_system": "Dynamics 365 Customer Insights - Journeys",
        "write": False,
        "key_field": "test_id",
        "summary": (
            "Generates segment-personalized content and a deterministic "
            "A/B test design with winner-selection criteria."
        ),
        "record": {
            "test_id": "AB-VIP-EARLY-ACCESS",
            "campaign": "Early Access VIP - 30% Off Everything",
            "variant_a": "Product focus; purchase-history hero; subject 'Sarah, Your Favorites Are 30% Off'; CTA Shop My Picks",
            "variant_b": "Urgency focus; countdown hero; 24-hour VIP access subject; CTA Activate My VIP Access",
            "variant_c": "Rewards focus; 3X points subject; CTA Claim VIP Rewards",
            "split": "33% / 33% / 34% for 12 hours",
            "selection_rule": "Automatically select winner by open rate plus revenue",
        },
    },
    "campaign_scheduling": {
        "title": "Campaign Scheduling Workflow",
        "source_system": "Dynamics 365 Customer Insights - Journeys",
        "write": True,
        "key_field": "schedule_id",
        "summary": (
            "Prepares audience scheduling, multistep nurture automation, "
            "tracking, and optimization without activating a live campaign."
        ),
        "record": {
            "schedule_id": "SCHED-VIP-0800",
            "launch": "08:00 PST for 12,400 VIP customers",
            "test": "Three variants with 33/33/34 split; winner selection after 12 hours",
            "workflow": "Hour 0 initial send; hour 24 browse abandonment; hour 48 cart abandonment; hour 72 final call",
            "tracking": "Open, click, conversion, and revenue dashboard with milestone alerts",
            "approval": "Prepared for marketing director review and approval",
            "execution_note": "Simulation only; no campaign, message, or customer journey is activated",
        },
    },
    "revenue_scenarios": {
        "title": "Campaign Revenue Scenarios and Executive Brief",
        "source_system": "Dynamics 365 Customer Insights",
        "write": False,
        "key_field": "model_id",
        "summary": (
            "Models conservative, expected, and optimistic campaign outcomes "
            "and produces a stakeholder-ready strategy recap."
        ),
        "record": {
            "model_id": "ROI-VIP-HOLIDAY",
            "audience": f"{VIP_REVENUE_AUDIENCE:,} VIP customers",
            "formula": "audience * conversion rate * average order value",
            "conservative": _format_revenue_scenario(
                VIP_REVENUE_SCENARIO_INPUTS["conservative"]
            ),
            "expected": _format_revenue_scenario(
                VIP_REVENUE_SCENARIO_INPUTS["expected"]
            ),
            "optimistic": _format_revenue_scenario(
                VIP_REVENUE_SCENARIO_INPUTS["optimistic"]
            ),
            "economics": "$47,000 investment; 30:1 to 45:1 VIP-wave ROI; $8.12M all-wave projection",
            "executive_brief": "Five segments, four waves over seven days, three creative variants, and a 72-hour nurture workflow",
        },
    },
}

_EVIDENCE_KEY_PUNCTUATION = "-_.,:;()?!/#@+$%^&*=[]{}<>~`'\""


def _normalize_evidence_tokens(text):
    tokens = []
    for raw in str(text).split():
        cleaned = "".join(
            character.lower()
            for character in raw
            if character not in _EVIDENCE_KEY_PUNCTUATION
        )
        if cleaned:
            tokens.append(cleaned)
    return tokens


def _record_for_evidence_request(capability, key, user_input):
    record = capability["record"]
    key_field = capability["key_field"]
    if key:
        if str(record[key_field]).lower() == str(key).strip().lower():
            return "match", record
        return "not_found", None
    query_tokens = _normalize_evidence_tokens(user_input)
    key_tokens = _normalize_evidence_tokens(record[key_field])
    width = len(key_tokens)
    if width and any(
        query_tokens[index:index + width] == key_tokens
        for index in range(len(query_tokens) - width + 1)
    ):
        return "match", record
    return "summary", None


def _format_evidence_record(record):
    return "\n".join(
        f"- **{field.replace('_', ' ').title()}:** {value}"
        for field, value in record.items()
    )


# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------

def _total_addressable_customers():
    return sum(seg["size"] for seg in CUSTOMER_SEGMENTS.values())


def _weighted_avg_ltv():
    total_size = _total_addressable_customers()
    weighted = sum(seg["size"] * seg["lifetime_value"] for seg in CUSTOMER_SEGMENTS.values())
    return round(weighted / total_size, 2) if total_size > 0 else 0


def _segment_revenue_contribution(seg_id):
    seg = CUSTOMER_SEGMENTS.get(seg_id, {})
    return round(seg.get("size", 0) * seg.get("avg_annual_spend", 0), 2)


def _campaign_projected_revenue(camp_id):
    camp = CAMPAIGN_TEMPLATES.get(camp_id, {})
    seg = CUSTOMER_SEGMENTS.get(camp.get("target_segment", ""), {})
    audience = seg.get("size", 0)
    conv_rate = camp.get("historical_conversion_rate", 0)
    basket = seg.get("avg_basket_size", 0)
    return round(audience * conv_rate * basket, 2)


# ---------------------------------------------------------------------------
# Agent Class
# ---------------------------------------------------------------------------

class PersonalizedMarketingAgent(BasicAgent):
    """Agent for personalized retail marketing orchestration."""

    def __init__(self):
        self.name = "personalized-marketing-agent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "customer_segmentation",
                            "campaign_design",
                            "content_personalization",
                            "performance_analysis",
                            "holiday_campaign_plan",
                            "creative_ab_test",
                            "campaign_scheduling",
                            "revenue_scenarios",
                        ],
                    },
                    "segment_id": {"type": "string"},
                    "campaign_id": {"type": "string"},
                    "key": {"type": "string"},
                    "user_input": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _live_customer_segmentation(self, customers):
        """Segmentation derived from live tenant records (preferred online)."""
        buyers = [c for c in customers if c["spend"] > 0]
        prospects = [c for c in customers if c["spend"] == 0]
        buyer_account_spend = {c["account"]: c["spend"] for c in buyers}
        accounts = {}
        for c in customers:
            accounts.setdefault(c["account"], []).append(c)
        lines = [
            "# Customer Segmentation — Live Tenant Audience",
            "",
            f"Live records from {DATA_SOURCE_URL} (Aster Lane Office Systems).",
            "Pass `segment_id` (e.g. SEG-LOYAL) for the embedded demo segment view.",
            "",
            f"**Contacts on file:** {len(customers)} across {len(accounts)} accounts",
            "",
            "| Segment (derived from live sales orders) | Contacts | Order Spend | LTV | Engagement |",
            "|------------------------------------------|----------|-------------|-----|------------|",
            f"| Active Buyers (account has orders) | {len(buyers)} "
            f"| ${sum(buyer_account_spend.values()):,.2f} "
            f"| n/a — enrichment seam | n/a — enrichment seam |",
            f"| Prospects (no orders yet) | {len(prospects)} | $0.00 "
            f"| n/a — enrichment seam | n/a — enrichment seam |",
            "",
            "## Top Buyer Accounts",
            "",
            "| Account | Order Spend | Sample Contact |",
            "|---------|-------------|----------------|",
        ]
        spend_ranked = sorted(
            buyer_account_spend.items(), key=lambda kv: kv[1], reverse=True
        )
        for account, spend in spend_ranked[:5]:
            sample = next(c for c in buyers if c["account"] == account)
            title = f" ({sample['title']})" if sample["title"] else ""
            lines.append(f"| {account} | ${spend:,.2f} | {sample['name']}{title} |")
        lines.append("")
        lines.append(
            "LTV, churn risk, and engagement need your loyalty/analytics system — "
            "wire it at the LIVE DATA SEAM."
        )
        return "\n".join(lines)

    def _customer_segmentation(self, **kwargs):
        if not kwargs.get("segment_id"):
            contacts = _fetch_collection("contacts")
            if contacts:
                spend = _live_spend_by_account()
                customers = [_normalize_live_customer(c, spend) for c in contacts]
                return self._live_customer_segmentation(customers)
        lines = [
            "# Customer Segmentation Overview",
            "",
            f"**Total Addressable Customers:** {_total_addressable_customers():,}",
            f"**Weighted Average LTV:** ${_weighted_avg_ltv():,.2f}",
            "",
            "| Segment | Size | Avg Spend | Orders/Yr | LTV | Churn Risk | Engagement |",
            "|---------|------|-----------|-----------|-----|------------|------------|",
        ]
        for seg_id, seg in CUSTOMER_SEGMENTS.items():
            lines.append(
                f"| {seg['name']} | {seg['size']:,} | ${seg['avg_annual_spend']:,.2f} "
                f"| {seg['avg_orders_per_year']} | ${seg['lifetime_value']:,.2f} "
                f"| {seg['churn_risk']*100:.0f}% | {seg['engagement_score']}/100 |"
            )
        lines.append("")
        lines.append("## Revenue Contribution by Segment")
        lines.append("")
        for seg_id, seg in CUSTOMER_SEGMENTS.items():
            rev = _segment_revenue_contribution(seg_id)
            lines.append(f"- **{seg['name']}:** ${rev:,.2f}")
        return "\n".join(lines)

    def _campaign_design(self, **kwargs):
        campaign_id = kwargs.get("campaign_id")
        if campaign_id and campaign_id in CAMPAIGN_TEMPLATES:
            camps = {campaign_id: CAMPAIGN_TEMPLATES[campaign_id]}
        else:
            camps = CAMPAIGN_TEMPLATES
        lines = ["# Campaign Design Portfolio", ""]
        for cid, camp in camps.items():
            seg = CUSTOMER_SEGMENTS.get(camp["target_segment"], {})
            proj_rev = _campaign_projected_revenue(cid)
            lines.append(f"## {camp['name']} (`{cid}`)")
            lines.append("")
            lines.append(f"- **Type:** {camp['type']}")
            lines.append(f"- **Target Segment:** {seg.get('name', 'Unknown')} ({camp['target_segment']})")
            lines.append(f"- **Audience Size:** {seg.get('size', 0):,}")
            lines.append(f"- **Duration:** {camp['duration_days']} days, {camp['stages']} stages")
            lines.append(f"- **Offer:** {camp['discount_offer']}")
            lines.append(f"- **Projected Revenue:** ${proj_rev:,.2f}")
            lines.append("")
            lines.append("**Email Sequence:**")
            for i, subj in enumerate(camp["subject_lines"], 1):
                lines.append(f"  {i}. {subj}")
            lines.append("")
            lines.append(f"**Historical Benchmarks:** Open {camp['historical_open_rate']*100:.0f}% | "
                         f"Click {camp['historical_click_rate']*100:.0f}% | "
                         f"Convert {camp['historical_conversion_rate']*100:.1f}%")
            lines.append("")
        return "\n".join(lines)

    def _content_personalization(self, **kwargs):
        segment_id = kwargs.get("segment_id")
        if segment_id and segment_id in CUSTOMER_SEGMENTS:
            segs = {segment_id: CUSTOMER_SEGMENTS[segment_id]}
        else:
            segs = CUSTOMER_SEGMENTS
        lines = ["# Content Personalization Matrix", ""]
        for seg_id, seg in segs.items():
            hero = CONTENT_BLOCKS["hero_banner"].get(seg_id, {})
            recs = CONTENT_BLOCKS["product_recs"].get(seg_id, [])
            lines.append(f"## {seg['name']} (`{seg_id}`)")
            lines.append("")
            lines.append("**Hero Banner:**")
            lines.append(f"- Headline: \"{hero.get('headline', '')}\"")
            lines.append(f"- CTA: \"{hero.get('cta', '')}\"")
            lines.append("")
            lines.append("**Product Recommendations:**")
            for prod in recs:
                lines.append(f"- {prod}")
            lines.append("")
            lines.append(f"**Preferred Channels:** {', '.join(seg['preferred_channels'])}")
            lines.append(f"**Top Categories:** {', '.join(seg['top_categories'])}")
            lines.append("")
        return "\n".join(lines)

    def _performance_analysis(self, **kwargs):
        lines = [
            "# Marketing Performance Analysis",
            "",
            "## A/B Test Results",
            "",
            "| Test | Campaign | Winner | Confidence | Sample | Lift |",
            "|------|----------|--------|------------|--------|------|",
        ]
        for test_id, test in AB_TEST_RESULTS.items():
            camp_name = CAMPAIGN_TEMPLATES.get(test["campaign"], {}).get("name", test["campaign"])
            a_conv = test["variant_a"]["conversions"]
            b_conv = test["variant_b"]["conversions"]
            lift = round(((max(a_conv, b_conv) - min(a_conv, b_conv)) / min(a_conv, b_conv)) * 100, 1)
            lines.append(
                f"| {test_id} | {camp_name} | Variant {test['winner']} "
                f"| {test['confidence']*100:.0f}% | {test['sample_size']:,} | +{lift}% |"
            )
        lines.append("")
        lines.append("## Campaign ROI Summary")
        lines.append("")
        lines.append("| Campaign | Audience | Proj. Revenue | Conv. Rate | Est. ROAS |")
        lines.append("|----------|----------|---------------|------------|-----------|")
        for cid, camp in CAMPAIGN_TEMPLATES.items():
            seg = CUSTOMER_SEGMENTS.get(camp["target_segment"], {})
            rev = _campaign_projected_revenue(cid)
            cost_estimate = seg.get("size", 0) * 0.35  # $0.35 per contact
            roas = round(rev / cost_estimate, 2) if cost_estimate > 0 else 0
            lines.append(
                f"| {camp['name']} | {seg.get('size', 0):,} | ${rev:,.2f} "
                f"| {camp['historical_conversion_rate']*100:.1f}% | {roas}x |"
            )
        lines.append("")
        total_rev = sum(_campaign_projected_revenue(c) for c in CAMPAIGN_TEMPLATES)
        lines.append(f"**Total Projected Campaign Revenue:** ${total_rev:,.2f}")
        return "\n".join(lines)

    def _evidence_capability(self, capability_name, **kwargs):
        capability = EVIDENCE_CAPABILITIES[capability_name]
        lookup_status, record = _record_for_evidence_request(
            capability,
            kwargs.get("key", ""),
            kwargs.get("user_input", ""),
        )
        lines = [
            f"# {capability['title']}",
            "",
            capability["summary"],
            "",
            f"## {capability['source_system']} (synthetic demo data)",
            "",
        ]
        if lookup_status == "not_found":
            lines.append(
                f"No record matched the requested {capability['key_field']}. "
                "Not substituting another record."
            )
        else:
            selected = record or capability["record"]
            label = "Exact keyed record" if lookup_status == "match" else "Worked example"
            lines.extend([f"**{label}:**", _format_evidence_record(selected)])

        if capability["write"] and lookup_status == "match":
            receipt_key = record[capability["key_field"]]
            lines.extend([
                "",
                "## Simulated Write Receipt",
                "",
                "- **Action Status:** simulated",
                f"- **Receipt:** SIM-{capability_name.upper()}-{receipt_key}",
                f"- **Target System:** {capability['source_system']}",
                "- **External Changes:** none; no live campaign or message was created",
            ])
        elif capability["write"]:
            lines.extend([
                "",
                "_Write-capable workflow; provide an exact key to generate a "
                "simulated receipt. No external system is modified._",
            ])
        else:
            lines.extend(["", "_Read-only; no external system is modified._"])
        return "\n".join(lines)

    def perform(self, **kwargs):
        operation = kwargs.get("operation", "customer_segmentation")
        dispatch = {
            "customer_segmentation": self._customer_segmentation,
            "campaign_design": self._campaign_design,
            "content_personalization": self._content_personalization,
            "performance_analysis": self._performance_analysis,
            "holiday_campaign_plan": self._evidence_capability,
            "creative_ab_test": self._evidence_capability,
            "campaign_scheduling": self._evidence_capability,
            "revenue_scenarios": self._evidence_capability,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"Unknown operation `{operation}`. Valid: {', '.join(dispatch.keys())}"
        if operation in EVIDENCE_CAPABILITIES:
            return handler(operation, **kwargs)
        return handler(**kwargs)


# ---------------------------------------------------------------------------
# Main — exercise all operations
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    _validate_revenue_formula_contract()
    agent = PersonalizedMarketingAgent()
    print("=" * 80)
    print("EMBEDDED DEMO SEGMENTS (works offline)")
    print(agent.perform(operation="customer_segmentation", segment_id="SEG-LOYAL"))
    print("\n" + "=" * 80)
    print("LIVE TENANT AUDIENCE (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="customer_segmentation"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="campaign_design", campaign_id="CAMP-VIP"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="content_personalization", segment_id="SEG-LOYAL"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="performance_analysis"))
    print("=" * 80)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
