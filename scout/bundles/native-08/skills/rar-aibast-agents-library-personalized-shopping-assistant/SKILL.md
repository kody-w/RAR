---
name: "rar-aibast-agents-library-personalized-shopping-assistant"
description: "Recommends products and checks a live catalog from a simulated Dynamics 365 tenant, with an offline demo fallback for every operation."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/personalized_shopping_assistant", "rar_sha256": "6f02e955c5212f2deb68cab2674901f367a6eaa77ca0e85834df0da46189d83c", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["shopping", "personalization", "recommendations", "style", "inventory", "b2c"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/personalized_shopping_assistant`. The original RAPP
agent is preserved byte-for-byte in `personalized_shopping_assistant_agent.py` and in the RCI capsule.

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

Personalized Shopping Assistant Agent — a template you are meant to mutate.

Delivers product recommendations, style profiles, inventory checks,
and outfit building for personalized retail experiences.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls a live product catalog over real HTTP from
     the globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     The tenant's 12 sellable products (printers, scanners, service
     plans) become the live catalog.
     Try: perform(operation="inventory_check", sku="AST-PRN-620")
  2. No network? Everything falls back to the embedded demo layer below
     (PRODUCT_CATALOG / CUSTOMER_PREFERENCES / OUTFIT_TEMPLATES) — the
     agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PERSONALIZED_SHOPPING_ASSISTANT_DATA_URL to any OData-shaped
     endpoint (your real Dynamics org, or JSON exported from Shopify /
     your PIM), or replace _fetch_collection() with your own API client.
     Fields the rest of the file needs are listed in
     _normalize_live_product() — everything else keeps working
     untouched. Fields marked "enrichment seam" in the output (stock by
     size, ratings, style tags) are where you wire your inventory and
     reviews systems.

OPERATIONS
  product_recommendations | style_profile | inventory_check
  | outfit_builder | occasion_analysis | occasion_outfit_options
  | network_availability | loyalty_pricing | clienteling_follow_up
  kwargs: operation (required), customer_id, sku, user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "product_recommendations",
        "style_profile",
        "inventory_check",
        "outfit_builder",
        "occasion_analysis",
        "occasion_outfit_options",
        "network_availability",
        "loyalty_pricing",
        "clienteling_follow_up"
      ],
      "type": "string"
    },
    "sku": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `personalized_shopping_assistant_agent.py` and embedded as the fenced Python below (sha256 6f02e955c5212f2d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `personalized_shopping_assistant_agent.py` first:

```bash
python3 personalized_shopping_assistant_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 personalized_shopping_assistant_agent.py   # or on stdin
python3 personalized_shopping_assistant_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Personalized Shopping Assistant Agent — a template you are meant to mutate.

Delivers product recommendations, style profiles, inventory checks,
and outfit building for personalized retail experiences.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls a live product catalog over real HTTP from
     the globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     The tenant's 12 sellable products (printers, scanners, service
     plans) become the live catalog.
     Try: perform(operation="inventory_check", sku="AST-PRN-620")
  2. No network? Everything falls back to the embedded demo layer below
     (PRODUCT_CATALOG / CUSTOMER_PREFERENCES / OUTFIT_TEMPLATES) — the
     agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PERSONALIZED_SHOPPING_ASSISTANT_DATA_URL to any OData-shaped
     endpoint (your real Dynamics org, or JSON exported from Shopify /
     your PIM), or replace _fetch_collection() with your own API client.
     Fields the rest of the file needs are listed in
     _normalize_live_product() — everything else keeps working
     untouched. Fields marked "enrichment seam" in the output (stock by
     size, ratings, style tags) are where you wire your inventory and
     reviews systems.

OPERATIONS
  product_recommendations | style_profile | inventory_check
  | outfit_builder | occasion_analysis | occasion_outfit_options
  | network_availability | loyalty_pricing | clienteling_follow_up
  kwargs: operation (required), customer_id, sku, user_input
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/personalized_shopping_assistant",
    "version": "1.2.0",
    "display_name": "Personalized Shopping Assistant Agent",
    "description": "Recommends products and checks a live catalog from a simulated Dynamics 365 tenant, with an offline demo fallback for every operation.",
    "author": "AIBAST",
    "tags": ["shopping", "personalization", "recommendations", "style", "inventory", "b2c"],
    "category": "b2c_sales",
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
#   export PERSONALIZED_SHOPPING_ASSISTANT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your commerce/PIM client.
# Downstream code only needs the fields produced by
# _normalize_live_product().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "PERSONALIZED_SHOPPING_ASSISTANT_DATA_URL",
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


def _normalize_live_product(row):
    """Project a Dynamics product record onto the catalog shape this
    agent uses. THIS is the contract your replacement data source must
    meet — a dict with these keys. None means 'not available from the
    product entity alone' and the renderers label it as an enrichment
    seam (wire your inventory, reviews, and merchandising systems)."""
    return {
        "name": row.get("name", "Unknown"),
        "category": (row.get("description") or "product").split(".")[0][:40],
        "price": float(row.get("price") or 0),
        "brand": None,        # enrichment seam — wire your PIM
        "rating": None,       # enrichment seam — wire your reviews platform
        "stock": None,        # enrichment seam — wire your inventory system
        "active": row.get("statecode") == 0,
        "_live": True,
    }


def _live_catalog():
    """productnumber-keyed dict of live tenant products; {} offline."""
    rows = _fetch_collection("products")
    return {
        row["productnumber"]: _normalize_live_product(row)
        for row in rows
        if row.get("productnumber")
    }


def _na(value):
    """None = the product entity alone can't know this (enrichment seam);
    0 is real."""
    return "n/a — enrichment seam" if value is None else f"{value}"


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

PRODUCT_CATALOG = {
    "SKU-1001": {"name": "Classic Oxford Shirt — White", "category": "tops", "subcategory": "shirts", "price": 68.00, "brand": "Heritage Co.", "sizes": ["S", "M", "L", "XL"], "colors": ["white", "blue", "pink"], "style_tags": ["classic", "business", "smart_casual"], "rating": 4.7, "stock": {"S": 12, "M": 25, "L": 18, "XL": 8}},
    "SKU-1002": {"name": "Slim Fit Chinos — Navy", "category": "bottoms", "subcategory": "pants", "price": 79.00, "brand": "Heritage Co.", "sizes": ["30", "32", "34", "36"], "colors": ["navy", "khaki", "olive"], "style_tags": ["classic", "smart_casual", "weekend"], "rating": 4.5, "stock": {"30": 6, "32": 15, "34": 20, "36": 10}},
    "SKU-1003": {"name": "Merino Wool Crew Sweater", "category": "tops", "subcategory": "sweaters", "price": 125.00, "brand": "Alpine Knits", "sizes": ["S", "M", "L", "XL"], "colors": ["charcoal", "burgundy", "forest"], "style_tags": ["classic", "smart_casual", "layering"], "rating": 4.8, "stock": {"S": 4, "M": 10, "L": 8, "XL": 3}},
    "SKU-1004": {"name": "Leather Chelsea Boots", "category": "footwear", "subcategory": "boots", "price": 195.00, "brand": "Cobblestone", "sizes": ["8", "9", "10", "11", "12"], "colors": ["brown", "black"], "style_tags": ["classic", "smart_casual", "evening"], "rating": 4.6, "stock": {"8": 5, "9": 8, "10": 12, "11": 7, "12": 3}},
    "SKU-1005": {"name": "Quilted Vest", "category": "outerwear", "subcategory": "vests", "price": 110.00, "brand": "Northfield", "sizes": ["S", "M", "L", "XL"], "colors": ["navy", "olive", "black"], "style_tags": ["casual", "outdoor", "layering"], "rating": 4.4, "stock": {"S": 2, "M": 7, "L": 5, "XL": 9}},
    "SKU-1006": {"name": "Silk Pocket Square", "category": "accessories", "subcategory": "pocket_squares", "price": 35.00, "brand": "Heritage Co.", "sizes": ["OS"], "colors": ["navy_paisley", "burgundy_dot", "green_stripe"], "style_tags": ["classic", "business", "evening"], "rating": 4.9, "stock": {"OS": 30}},
    "SKU-1007": {"name": "Performance Running Shoe", "category": "footwear", "subcategory": "athletic", "price": 145.00, "brand": "Stride Labs", "sizes": ["8", "9", "10", "11", "12"], "colors": ["white_grey", "black_red"], "style_tags": ["athletic", "casual", "performance"], "rating": 4.7, "stock": {"8": 10, "9": 15, "10": 20, "11": 12, "12": 6}},
    "SKU-1008": {"name": "Linen Blazer — Unstructured", "category": "outerwear", "subcategory": "blazers", "price": 225.00, "brand": "Riviera Style", "sizes": ["S", "M", "L", "XL"], "colors": ["tan", "light_blue"], "style_tags": ["smart_casual", "evening", "summer"], "rating": 4.3, "stock": {"S": 3, "M": 6, "L": 4, "XL": 2}},
}

CUSTOMER_PREFERENCES = {
    "SHOP-001": {
        "name": "Daniel Reeves",
        "size_top": "L",
        "size_bottom": "34",
        "size_shoe": "10",
        "style_preference": ["classic", "smart_casual"],
        "brand_affinity": ["Heritage Co.", "Alpine Knits"],
        "color_preference": ["navy", "charcoal", "white"],
        "budget_range": {"min": 50, "max": 250},
        "purchase_history": ["SKU-1001", "SKU-1002", "SKU-1006"],
    },
    "SHOP-002": {
        "name": "Olivia Chen",
        "size_top": "S",
        "size_bottom": "30",
        "size_shoe": "8",
        "style_preference": ["casual", "outdoor", "athletic"],
        "brand_affinity": ["Northfield", "Stride Labs"],
        "color_preference": ["olive", "black", "white_grey"],
        "budget_range": {"min": 30, "max": 175},
        "purchase_history": ["SKU-1005", "SKU-1007"],
    },
}

OUTFIT_TEMPLATES = {
    "business_casual": {"name": "Business Casual", "pieces": ["tops:shirts", "bottoms:pants", "footwear:boots", "accessories:pocket_squares"]},
    "weekend_smart": {"name": "Weekend Smart", "pieces": ["tops:sweaters", "bottoms:pants", "footwear:boots"]},
    "active_weekend": {"name": "Active Weekend", "pieces": ["outerwear:vests", "footwear:athletic"]},
    "evening_out": {"name": "Evening Out", "pieces": ["outerwear:blazers", "tops:shirts", "bottoms:pants", "footwear:boots"]},
}

EVIDENCE_ACTIONS = {
    "occasion_analysis": {
        "title": "Occasion-Specific Style Analysis",
        "write": False,
        "records": [
            {"record_id": "CLIENT-JENNIFER", "customer": "Jennifer Hayes", "archetype": "Modern Classic", "palette": "neutrals, navy, burgundy", "fit": "tailored, not tight", "price_range": "$150-$400 per piece", "brands": "Theory, Vince, Equipment"},
            {"record_id": "OCCASION-BUSINESS-DINNER", "occasion": "business dinner with clients", "dress_code": "business elegant", "impression": "polished and confident", "comfort": "seated dining and standing cocktails", "recommendation": "structured, not stuffy"},
        ],
        "context": "Sizes: tops 6/Small with relaxed fit, bottoms 28/6 high-rise, dresses 6 midi, shoes 8 comfortable heels. Notes: structured pieces, no prints, investment over trends.",
    },
    "occasion_outfit_options": {
        "title": "Complete Occasion Outfit Options",
        "write": False,
        "records": [
            {"record_id": "LOOK-POWER-SUITING", "look": "Power Suiting", "pieces": "Theory wool crepe blazer, Vince navy shell, Equipment high-rise pant, block heel, leather tote", "total": "$1,595", "recommendation": "best match for established style"},
            {"record_id": "LOOK-ELEGANT", "look": "Elegant Simplicity", "pieces": "Theory midi sheath, Theory blazer, kitten heel, gold bar necklace", "total": "$1,110", "recommendation": "one-piece alternative"},
            {"record_id": "LOOK-MODERN-EDGE", "look": "Modern Edge", "pieces": "Vince tailored jumpsuit and evening leather accessories", "total": "$920", "recommendation": "strong alternative with warehouse lead time"},
        ],
        "context": "High-match pieces include a 96% wool crepe blazer, 94% silk shell, 92% tailored pant, and 91% midi sheath. Avoid prints, fitted dresses, and trend-led pieces.",
    },
    "network_availability": {
        "title": "Store and Warehouse Availability",
        "write": False,
        "records": [
            {"record_id": "STOCK-OUTFIT-1", "look": "Power Suiting", "status": "4 of 5 items in store", "low_stock": "Equipment pant size 28, two left", "substitution": "Stuart Weitzman size 8 block heel, $315, prior fit history"},
            {"record_id": "STOCK-OUTFIT-2", "look": "Elegant Simplicity", "status": "dress, kitten heel, and necklace in stock", "low_stock": "none", "substitution": "not required"},
            {"record_id": "STOCK-OUTFIT-3", "look": "Modern Edge", "status": "jumpsuit only size 4 locally", "low_stock": "requested size unavailable", "substitution": "warehouse in two days or downtown location"},
        ],
        "context": "Outfit 1 is fully available today with the evidence-grounded shoe swap.",
    },
    "loyalty_pricing": {
        "title": "Loyalty-Optimized Pricing",
        "write": False,
        "records": [
            {"record_id": "PRICE-POWER-SUITING", "original_total": "$1,595", "platinum_discount": "-$159", "bundle_bonus": "-$72", "points_applied": "-$42", "final_price": "$1,322", "savings": "$273 (17%)"},
            {"record_id": "BENEFIT-ALTERATIONS", "benefit": "Free alterations", "value": "$35", "eligibility": "Platinum client"},
        ],
        "context": "The package applies the active 10% Platinum discount, 5% three-piece bundle bonus, point redemption, and free alterations.",
    },
    "clienteling_follow_up": {
        "title": "Saved Looks and Follow-Up Triggers",
        "write": True,
        "records": [
            {"record_id": "SAVE-BUSINESS-DINNER", "profile_action": "save Outfit 1 as Business Dinner Look", "wishlist": "Outfits 2 and 3", "profile_update": "confirm sizes and add Stuart Weitzman brand note"},
            {"record_id": "FOLLOWUP-JENNIFER", "triggers": "new Theory arrivals, low-stock pants, wishlist sale", "channel": "Outlook", "continuity": "available to any associate through Dynamics 365"},
        ],
        "context": "Session result: five preferences matched, three complete looks, Power Suiting recommended, 4 of 5 items in store, and $273 saved.",
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _evidence_action(action, **kwargs):
    """Render a demo-grounded action with exact record-key lookup."""
    spec = EVIDENCE_ACTIONS[action]
    user_input = str(kwargs.get("user_input", ""))
    normalized = {
        "".join(ch for ch in token.upper() if ch.isalnum())
        for token in user_input.split()
    }
    records = spec["records"]
    if user_input:
        records = [
            record for record in records
            if "".join(ch for ch in record["record_id"].upper() if ch.isalnum()) in normalized
        ]
        if not records:
            return "No exact `record_id` match was found; no substitute customer, look, or item was used."
    lines = [
        f"## {spec['title']}",
        f"\n{spec['context']}",
        "\nDeterministic evidence-backed records:",
    ]
    for record in records:
        lines.append("- " + "; ".join(f"{key}: {value}" for key, value in record.items()))
    if spec["write"]:
        receipt_key = records[0]["record_id"] if len(records) == 1 else "BATCH"
        lines.extend([
            "\n### Simulated Write Receipt",
            f"- receipt_id: SIM-CLIENTELING-{receipt_key}",
            "- status: simulated",
            "- target_systems: Dynamics 365 and Outlook",
            "- No external system changed; profile updates, saved looks, wishlists, and notifications are preview-only.",
        ])
    else:
        lines.append("\n_Read-only analysis; no external system changed._")
    return "\n".join(lines)

def _match_score(product, preferences):
    """Calculate match score between product and customer preferences."""
    score = 0
    style_overlap = set(product["style_tags"]) & set(preferences["style_preference"])
    score += len(style_overlap) * 20
    if product["brand"] in preferences["brand_affinity"]:
        score += 25
    color_overlap = set(product["colors"]) & set(preferences["color_preference"])
    score += len(color_overlap) * 10
    if preferences["budget_range"]["min"] <= product["price"] <= preferences["budget_range"]["max"]:
        score += 15
    return min(100, score)


def _check_stock(product, size):
    """Check stock availability for a product and size."""
    return product["stock"].get(size, 0)


def _get_recommendations(customer_id, limit=5):
    """Get top product recommendations for a customer."""
    prefs = CUSTOMER_PREFERENCES.get(customer_id, {})
    if not prefs:
        return []
    scored = []
    for sku, product in PRODUCT_CATALOG.items():
        if sku in prefs.get("purchase_history", []):
            continue
        score = _match_score(product, prefs)
        scored.append((sku, product, score))
    scored.sort(key=lambda x: x[2], reverse=True)
    return scored[:limit]


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class PersonalizedShoppingAssistantAgent(BasicAgent):
    """Personalized shopping assistant agent."""

    def __init__(self):
        self.name = "PersonalizedShoppingAssistantAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Personalized Shopping Assistant Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "product_recommendations",
                            "style_profile",
                            "inventory_check",
                            "outfit_builder",
                            "occasion_analysis",
                            "occasion_outfit_options",
                            "network_availability",
                            "loyalty_pricing",
                            "clienteling_follow_up",
                        ],
                    },
                    "customer_id": {"type": "string"},
                    "sku": {"type": "string"},
                    "user_input": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "product_recommendations")
        dispatch = {
            "product_recommendations": self._product_recommendations,
            "style_profile": self._style_profile,
            "inventory_check": self._inventory_check,
            "outfit_builder": self._outfit_builder,
            "occasion_analysis": self._evidence_action,
            "occasion_outfit_options": self._evidence_action,
            "network_availability": self._evidence_action,
            "loyalty_pricing": self._evidence_action,
            "clienteling_follow_up": self._evidence_action,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        if operation in EVIDENCE_ACTIONS:
            return handler(operation, **kwargs)
        return handler(**kwargs)

    def _evidence_action(self, action, **kwargs) -> str:
        return _evidence_action(action, **kwargs)

    def _product_recommendations(self, **kwargs) -> str:
        customer_id = kwargs.get("customer_id", "SHOP-001")
        prefs = CUSTOMER_PREFERENCES.get(customer_id, {})
        recs = _get_recommendations(customer_id)
        lines = [f"# Product Recommendations: {prefs.get('name', 'Customer')}\n"]
        lines.append(f"**Style:** {', '.join(prefs.get('style_preference', []))}")
        lines.append(f"**Budget:** ${prefs.get('budget_range', {}).get('min', 0)} - ${prefs.get('budget_range', {}).get('max', 0)}\n")
        if recs:
            lines.append("| Rank | Product | Brand | Price | Match Score | Rating |")
            lines.append("|---|---|---|---|---|---|")
            for i, (sku, product, score) in enumerate(recs, 1):
                lines.append(
                    f"| {i} | {product['name']} ({sku}) | {product['brand']} "
                    f"| ${product['price']:,.2f} | {score}% | {product['rating']} |"
                )
        else:
            lines.append("No recommendations available.")
        return "\n".join(lines)

    def _style_profile(self, **kwargs) -> str:
        customer_id = kwargs.get("customer_id", "SHOP-001")
        prefs = CUSTOMER_PREFERENCES.get(customer_id, {})
        lines = [f"# Style Profile: {prefs.get('name', 'Unknown')}\n"]
        lines.append(f"## Sizing\n")
        lines.append(f"- Top: {prefs.get('size_top', 'N/A')}")
        lines.append(f"- Bottom: {prefs.get('size_bottom', 'N/A')}")
        lines.append(f"- Shoe: {prefs.get('size_shoe', 'N/A')}\n")
        lines.append("## Style Preferences\n")
        for style in prefs.get("style_preference", []):
            lines.append(f"- {style.replace('_', ' ').title()}")
        lines.append("\n## Brand Affinity\n")
        for brand in prefs.get("brand_affinity", []):
            lines.append(f"- {brand}")
        lines.append("\n## Color Preference\n")
        for color in prefs.get("color_preference", []):
            lines.append(f"- {color.replace('_', ' ').title()}")
        lines.append(f"\n## Budget Range\n")
        br = prefs.get("budget_range", {})
        lines.append(f"${br.get('min', 0)} - ${br.get('max', 0)}")
        lines.append("\n## Purchase History\n")
        for sku in prefs.get("purchase_history", []):
            product = PRODUCT_CATALOG.get(sku, {})
            lines.append(f"- {product.get('name', sku)} — ${product.get('price', 0):,.2f}")
        return "\n".join(lines)

    def _inventory_check(self, **kwargs) -> str:
        sku = kwargs.get("sku")
        live = _live_catalog() if (not sku or sku not in PRODUCT_CATALOG) else {}
        if sku and sku in live:
            p = live[sku]
            lines = [f"# Inventory Check: {p['name']} ({sku}) — live tenant record\n"]
            lines.append(f"- **Price:** ${p['price']:,.2f} (live list price)")
            lines.append(f"- **Brand:** {_na(p['brand'])}")
            lines.append(f"- **Rating:** {_na(p['rating'])}")
            lines.append(f"- **Status:** {'Active' if p['active'] else 'Retired'}")
            lines.append(f"- **Stock:** {_na(p['stock'])} (wire your inventory system)")
            lines.append("\n_Source: live Static Dynamics 365 tenant (products)._")
            return "\n".join(lines)
        if not sku and live:
            lines = ["# Inventory Overview (live tenant catalog)\n"]
            lines.append("| SKU | Product | Price | Stock | Status |")
            lines.append("|---|---|---|---|---|")
            for pn, p in sorted(live.items()):
                status = "Active" if p["active"] else "Retired"
                lines.append(f"| {pn} | {p['name']} | ${p['price']:,.2f} | {_na(p['stock'])} | {status} |")
            lines.append("\n_Source: live Static Dynamics 365 tenant (products). "
                         "Stock is an enrichment seam — wire your inventory system._")
            return "\n".join(lines)
        if sku and sku in PRODUCT_CATALOG:
            product = PRODUCT_CATALOG[sku]
            lines = [f"# Inventory Check: {product['name']} ({sku})\n"]
            lines.append(f"- **Price:** ${product['price']:,.2f}")
            lines.append(f"- **Brand:** {product['brand']}")
            lines.append(f"- **Rating:** {product['rating']}\n")
            lines.append("## Stock by Size\n")
            lines.append("| Size | Stock | Status |")
            lines.append("|---|---|---|")
            for size, qty in product["stock"].items():
                status = "In Stock" if qty > 5 else "Low Stock" if qty > 0 else "Out of Stock"
                lines.append(f"| {size} | {qty} | {status} |")
            total = sum(product["stock"].values())
            lines.append(f"\n**Total Units:** {total}")
            return "\n".join(lines)

        lines = ["# Inventory Overview (embedded demo data — offline)\n"]
        lines.append("| SKU | Product | Price | Total Stock | Status |")
        lines.append("|---|---|---|---|---|")
        for sku, p in PRODUCT_CATALOG.items():
            total = sum(p["stock"].values())
            status = "In Stock" if total > 10 else "Low Stock" if total > 0 else "Out of Stock"
            lines.append(f"| {sku} | {p['name']} | ${p['price']:,.2f} | {total} | {status} |")
        return "\n".join(lines)

    def _outfit_builder(self, **kwargs) -> str:
        customer_id = kwargs.get("customer_id", "SHOP-001")
        prefs = CUSTOMER_PREFERENCES.get(customer_id, {})
        lines = [f"# Outfit Builder: {prefs.get('name', 'Customer')}\n"]
        for template_id, template in OUTFIT_TEMPLATES.items():
            lines.append(f"## {template['name']}\n")
            total_price = 0
            for piece_spec in template["pieces"]:
                cat, subcat = piece_spec.split(":")
                matches = [(sku, p) for sku, p in PRODUCT_CATALOG.items() if p["category"] == cat and p["subcategory"] == subcat]
                if matches:
                    best = max(matches, key=lambda x: _match_score(x[1], prefs) if prefs else x[1]["rating"])
                    sku, product = best
                    total_price += product["price"]
                    lines.append(f"- **{cat.replace('_', ' ').title()}:** {product['name']} — ${product['price']:,.2f}")
                else:
                    lines.append(f"- **{cat.replace('_', ' ').title()}:** No matching item found")
            lines.append(f"\n**Outfit Total:** ${total_price:,.2f}\n")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = PersonalizedShoppingAssistantAgent()
    print("=" * 60)
    print("EMBEDDED DEMO PRODUCT (works offline)")
    print(agent.perform(operation="inventory_check", sku="SKU-1003"))
    print()
    print("=" * 60)
    print("LIVE TENANT PRODUCT (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="inventory_check", sku="AST-PRN-620"))
    print()
    print("=" * 60)
    print(agent.perform(operation="product_recommendations", customer_id="SHOP-001"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="outfit_builder", customer_id="SHOP-001"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
