---
name: "rar-aibast-agents-library-sales-chat"
description: "Answers chat questions from a live product catalog on a simulated Dynamics 365 tenant, with promotions and an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/sales_chat", "rar_sha256": "db0e860853560f566ee7107dad1928d1e5c14256fd8f3074ccd0957d7b6be10c", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["sales", "chat", "product", "promotion", "order", "b2c"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/sales_chat`. The original RAPP
agent is preserved byte-for-byte in `sales_chat_agent.py` and in the RCI capsule.

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

Sales Chat Agent — a template you are meant to mutate.

Handles product inquiries, availability checks, promotion lookups,
and order assistance for retail sales chat interactions.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls a live product catalog over real HTTP from
     the globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     The tenant's 12 sellable products (AsterPrint printers, ScanDock
     scanners, service plans) answer chat inquiries with live prices.
     Try: perform(operation="product_inquiry", product_id="AST-PRN-620")
  2. No network? Everything falls back to the embedded demo layer below
     (PRODUCT_CATALOG / STOCK_LEVELS / ACTIVE_PROMOTIONS) — the agent
     never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SALES_CHAT_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from your commerce catalog), or
     replace _fetch_collection() with your own API client. Fields the
     rest of the file needs are listed in _normalize_live_product() —
     everything else keeps working untouched. Fields marked "enrichment
     seam" in the output (stock, ratings, warranty) are where you wire
     your inventory and reviews systems.

OPERATIONS
  product_inquiry | availability_check | promotion_lookup
  | order_assistance
  kwargs: operation (required), product_id, category

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "category": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "product_inquiry",
        "availability_check",
        "promotion_lookup",
        "order_assistance"
      ],
      "type": "string"
    },
    "product_id": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sales_chat_agent.py` and embedded as the fenced Python below (sha256 db0e860853560f56…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sales_chat_agent.py` first:

```bash
python3 sales_chat_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sales_chat_agent.py   # or on stdin
python3 sales_chat_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Sales Chat Agent — a template you are meant to mutate.

Handles product inquiries, availability checks, promotion lookups,
and order assistance for retail sales chat interactions.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls a live product catalog over real HTTP from
     the globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     The tenant's 12 sellable products (AsterPrint printers, ScanDock
     scanners, service plans) answer chat inquiries with live prices.
     Try: perform(operation="product_inquiry", product_id="AST-PRN-620")
  2. No network? Everything falls back to the embedded demo layer below
     (PRODUCT_CATALOG / STOCK_LEVELS / ACTIVE_PROMOTIONS) — the agent
     never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SALES_CHAT_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from your commerce catalog), or
     replace _fetch_collection() with your own API client. Fields the
     rest of the file needs are listed in _normalize_live_product() —
     everything else keeps working untouched. Fields marked "enrichment
     seam" in the output (stock, ratings, warranty) are where you wire
     your inventory and reviews systems.

OPERATIONS
  product_inquiry | availability_check | promotion_lookup
  | order_assistance
  kwargs: operation (required), product_id, category
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/sales_chat",
    "version": "1.1.0",
    "display_name": "Sales Chat Agent",
    "description": "Answers chat questions from a live product catalog on a simulated Dynamics 365 tenant, with promotions and an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["sales", "chat", "product", "promotion", "order", "b2c"],
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
#   export SALES_CHAT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your commerce catalog client.
# Downstream code only needs the fields produced by
# _normalize_live_product().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "SALES_CHAT_DATA_URL",
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
    seam (wire your inventory, reviews, and warranty systems)."""
    return {
        "name": row.get("name", "Unknown"),
        "price": float(row.get("price") or 0),
        "description": row.get("description", ""),
        "rating": None,          # enrichment seam — wire your reviews platform
        "reviews_count": None,   # enrichment seam
        "warranty": None,        # enrichment seam — wire your warranty system
        "stock": None,           # enrichment seam — wire your inventory system
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
    """None = the catalog alone can't know this (enrichment seam); 0 is
    real."""
    return "n/a — enrichment seam" if value is None else f"{value}"


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

PRODUCT_CATALOG = {
    "PROD-101": {
        "name": "Ultra-Slim Laptop 14-inch",
        "category": "electronics",
        "subcategory": "laptops",
        "price": 999.99,
        "description": "14-inch FHD display, 16GB RAM, 512GB SSD, Intel Core i7, all-day battery",
        "features": ["Backlit keyboard", "Fingerprint reader", "USB-C charging", "Wi-Fi 6E"],
        "rating": 4.6,
        "reviews_count": 842,
        "warranty": "1 year manufacturer",
    },
    "PROD-102": {
        "name": "Wireless Noise-Canceling Headphones",
        "category": "electronics",
        "subcategory": "audio",
        "price": 279.99,
        "description": "Premium over-ear headphones with adaptive ANC, 30-hour battery, multipoint connection",
        "features": ["Adaptive noise canceling", "Hi-Res Audio certified", "Foldable design", "Carrying case included"],
        "rating": 4.8,
        "reviews_count": 1205,
        "warranty": "2 year manufacturer",
    },
    "PROD-103": {
        "name": "Smart Fitness Watch Series 5",
        "category": "electronics",
        "subcategory": "wearables",
        "price": 349.99,
        "description": "Advanced fitness tracking, GPS, heart rate, SpO2, sleep analysis, 5ATM water resistance",
        "features": ["Always-on display", "7-day battery", "100+ workout modes", "Mobile payments"],
        "rating": 4.5,
        "reviews_count": 678,
        "warranty": "1 year manufacturer",
    },
    "PROD-104": {
        "name": "Ergonomic Office Chair",
        "category": "furniture",
        "subcategory": "chairs",
        "price": 599.99,
        "description": "Fully adjustable ergonomic mesh chair with lumbar support, headrest, and armrests",
        "features": ["12-position recline", "Adjustable lumbar", "Breathable mesh", "Weight capacity 300 lbs"],
        "rating": 4.7,
        "reviews_count": 456,
        "warranty": "5 year manufacturer",
    },
    "PROD-105": {
        "name": "Robot Vacuum & Mop Combo",
        "category": "home",
        "subcategory": "cleaning",
        "price": 449.99,
        "description": "LiDAR navigation, auto-empty station, simultaneous vacuum and mop",
        "features": ["LiDAR mapping", "Auto-empty base", "App control", "2-in-1 vacuum/mop"],
        "rating": 4.4,
        "reviews_count": 892,
        "warranty": "2 year manufacturer",
    },
}

STOCK_LEVELS = {
    "PROD-101": {"online": 145, "store_downtown": 8, "store_mall": 12, "store_suburban": 5, "warehouse": 320},
    "PROD-102": {"online": 230, "store_downtown": 15, "store_mall": 20, "store_suburban": 10, "warehouse": 480},
    "PROD-103": {"online": 78, "store_downtown": 4, "store_mall": 6, "store_suburban": 2, "warehouse": 150},
    "PROD-104": {"online": 42, "store_downtown": 2, "store_mall": 3, "store_suburban": 1, "warehouse": 85},
    "PROD-105": {"online": 95, "store_downtown": 5, "store_mall": 7, "store_suburban": 3, "warehouse": 200},
}

ACTIVE_PROMOTIONS = {
    "PROMO-SP25": {
        "name": "Spring Tech Sale",
        "discount_type": "percentage",
        "discount_value": 15,
        "valid_from": "2025-03-01",
        "valid_to": "2025-03-31",
        "applicable_categories": ["electronics"],
        "min_purchase": 200,
        "promo_code": "SPRING15",
        "stackable": False,
    },
    "PROMO-BUNDLE": {
        "name": "Smart Home Bundle",
        "discount_type": "fixed",
        "discount_value": 75,
        "valid_from": "2025-03-10",
        "valid_to": "2025-04-10",
        "applicable_categories": ["electronics", "home"],
        "min_purchase": 500,
        "promo_code": "SMARTHOME75",
        "stackable": False,
    },
    "PROMO-SHIP": {
        "name": "Free Shipping Weekend",
        "discount_type": "free_shipping",
        "discount_value": 0,
        "valid_from": "2025-03-14",
        "valid_to": "2025-03-16",
        "applicable_categories": ["all"],
        "min_purchase": 50,
        "promo_code": "FREESHIP",
        "stackable": True,
    },
    "PROMO-CHAIR": {
        "name": "Home Office Upgrade",
        "discount_type": "percentage",
        "discount_value": 20,
        "valid_from": "2025-03-05",
        "valid_to": "2025-03-25",
        "applicable_categories": ["furniture"],
        "min_purchase": 0,
        "promo_code": "OFFICE20",
        "stackable": True,
    },
}

ORDER_PROCESSING = {
    "standard_shipping": {"days": "5-7 business days", "cost": 8.95},
    "express_shipping": {"days": "2-3 business days", "cost": 14.95},
    "next_day": {"days": "Next business day", "cost": 24.95},
    "store_pickup": {"days": "Same day (if in stock)", "cost": 0},
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _apply_best_promo(product):
    """Find and apply the best promotion for a product."""
    best_savings = 0
    best_promo = None
    for pid, promo in ACTIVE_PROMOTIONS.items():
        cats = promo["applicable_categories"]
        if "all" not in cats and product["category"] not in cats:
            continue
        if product["price"] < promo["min_purchase"]:
            continue
        if promo["discount_type"] == "percentage":
            savings = product["price"] * promo["discount_value"] / 100
        elif promo["discount_type"] == "fixed":
            savings = promo["discount_value"]
        else:
            savings = 0
        if savings > best_savings:
            best_savings = savings
            best_promo = promo
    return best_promo, round(best_savings, 2)


def _total_stock(product_id):
    """Calculate total stock across all locations."""
    stock = STOCK_LEVELS.get(product_id, {})
    return sum(stock.values())


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class SalesChatAgent(BasicAgent):
    """Retail sales chat assistant agent."""

    def __init__(self):
        self.name = "SalesChatAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Sales Chat Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "product_inquiry",
                            "availability_check",
                            "promotion_lookup",
                            "order_assistance",
                        ],
                    },
                    "product_id": {"type": "string"},
                    "category": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "product_inquiry")
        dispatch = {
            "product_inquiry": self._product_inquiry,
            "availability_check": self._availability_check,
            "promotion_lookup": self._promotion_lookup,
            "order_assistance": self._order_assistance,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        return handler(**kwargs)

    def _product_inquiry(self, **kwargs) -> str:
        product_id = kwargs.get("product_id")
        live = _live_catalog() if (not product_id or product_id not in PRODUCT_CATALOG) else {}
        if product_id and product_id in live:
            p = live[product_id]
            lines = [f"# {p['name']} ({product_id}) — live tenant record\n"]
            lines.append(f"**Price:** ${p['price']:,.2f} (live list price)")
            lines.append(f"**Status:** {'Active' if p['active'] else 'Retired'}")
            lines.append(f"**Rating:** {_na(p['rating'])}")
            lines.append(f"**Warranty:** {_na(p['warranty'])}\n")
            lines.append(f"**Description:** {p['description'] or 'n/a'}\n")
            lines.append(f"**Availability:** {_na(p['stock'])} (wire your inventory system)")
            lines.append("\n_Source: live Static Dynamics 365 tenant (products)._")
            return "\n".join(lines)
        if not product_id and live:
            lines = ["# Product Catalog (live tenant data)\n"]
            lines.append("| Product ID | Name | Price | Rating | Stock |")
            lines.append("|---|---|---|---|---|")
            for pid, p in sorted(live.items()):
                lines.append(
                    f"| {pid} | {p['name']} | ${p['price']:,.2f} "
                    f"| {_na(p['rating'])} | {_na(p['stock'])} |"
                )
            lines.append("\n_Source: live Static Dynamics 365 tenant (products). "
                         "Rating and stock are enrichment seams._")
            return "\n".join(lines)
        if product_id and product_id in PRODUCT_CATALOG:
            p = PRODUCT_CATALOG[product_id]
            promo, savings = _apply_best_promo(p)
            lines = [f"# {p['name']}\n"]
            lines.append(f"**Price:** ${p['price']:,.2f}")
            if promo:
                sale_price = p["price"] - savings
                lines.append(f"**Sale Price:** ${sale_price:,.2f} (save ${savings:,.2f} with code {promo['promo_code']})")
            lines.append(f"**Category:** {p['category'].title()} > {p['subcategory'].title()}")
            lines.append(f"**Rating:** {p['rating']}/5 ({p['reviews_count']:,} reviews)")
            lines.append(f"**Warranty:** {p['warranty']}\n")
            lines.append(f"**Description:** {p['description']}\n")
            lines.append("## Key Features\n")
            for feat in p["features"]:
                lines.append(f"- {feat}")
            total = _total_stock(product_id)
            lines.append(f"\n**Availability:** {'In Stock' if total > 0 else 'Out of Stock'} ({total} units)")
            return "\n".join(lines)

        lines = ["# Product Catalog (embedded demo data — offline)\n"]
        lines.append("| Product ID | Name | Category | Price | Rating | In Stock |")
        lines.append("|---|---|---|---|---|---|")
        for pid, p in PRODUCT_CATALOG.items():
            total = _total_stock(pid)
            lines.append(
                f"| {pid} | {p['name']} | {p['category'].title()} "
                f"| ${p['price']:,.2f} | {p['rating']} | {total} |"
            )
        return "\n".join(lines)

    def _availability_check(self, **kwargs) -> str:
        product_id = kwargs.get("product_id")
        if product_id and product_id in STOCK_LEVELS:
            stock = STOCK_LEVELS[product_id]
            product = PRODUCT_CATALOG.get(product_id, {})
            lines = [f"# Availability: {product.get('name', product_id)}\n"]
            lines.append("| Location | Stock | Status |")
            lines.append("|---|---|---|")
            for location, qty in stock.items():
                status = "In Stock" if qty > 5 else "Low Stock" if qty > 0 else "Out of Stock"
                lines.append(f"| {location.replace('_', ' ').title()} | {qty} | {status} |")
            total = sum(stock.values())
            lines.append(f"\n**Total Available:** {total} units")
            return "\n".join(lines)

        lines = ["# Stock Availability Overview\n"]
        lines.append("| Product | Online | Downtown | Mall | Suburban | Warehouse | Total |")
        lines.append("|---|---|---|---|---|---|---|")
        for pid, stock in STOCK_LEVELS.items():
            product = PRODUCT_CATALOG.get(pid, {})
            total = sum(stock.values())
            lines.append(
                f"| {product.get('name', pid)} | {stock.get('online', 0)} "
                f"| {stock.get('store_downtown', 0)} | {stock.get('store_mall', 0)} "
                f"| {stock.get('store_suburban', 0)} | {stock.get('warehouse', 0)} | {total} |"
            )
        return "\n".join(lines)

    def _promotion_lookup(self, **kwargs) -> str:
        lines = ["# Active Promotions\n"]
        lines.append("| Promo | Name | Discount | Code | Valid Through | Min Purchase |")
        lines.append("|---|---|---|---|---|---|")
        for pid, promo in ACTIVE_PROMOTIONS.items():
            if promo["discount_type"] == "percentage":
                disc = f"{promo['discount_value']}% off"
            elif promo["discount_type"] == "fixed":
                disc = f"${promo['discount_value']} off"
            else:
                disc = "Free shipping"
            min_p = f"${promo['min_purchase']}" if promo["min_purchase"] > 0 else "None"
            lines.append(
                f"| {pid} | {promo['name']} | {disc} | {promo['promo_code']} "
                f"| {promo['valid_to']} | {min_p} |"
            )
        lines.append("\n## Product-Specific Savings\n")
        for pid, product in PRODUCT_CATALOG.items():
            promo, savings = _apply_best_promo(product)
            if promo:
                sale_price = product["price"] - savings
                lines.append(
                    f"- **{product['name']}:** ${product['price']:,.2f} -> "
                    f"${sale_price:,.2f} (save ${savings:,.2f} with {promo['promo_code']})"
                )
        lines.append("\n*Note: Non-stackable promotions cannot be combined with other offers.*")
        return "\n".join(lines)

    def _order_assistance(self, **kwargs) -> str:
        lines = ["# Order Assistance\n"]
        lines.append("## Shipping Options\n")
        lines.append("| Method | Delivery Time | Cost |")
        lines.append("|---|---|---|")
        for method, info in ORDER_PROCESSING.items():
            cost = f"${info['cost']:,.2f}" if info["cost"] > 0 else "Free"
            lines.append(f"| {method.replace('_', ' ').title()} | {info['days']} | {cost} |")
        lines.append("\n## Order Support Topics\n")
        topics = {
            "Order Tracking": "Provide order number for real-time tracking updates",
            "Order Modification": "Changes can be made within 1 hour of placement",
            "Cancellation": "Full refund if cancelled before shipment",
            "Price Match": "We match verified competitor prices within 14 days of purchase",
            "Gift Wrapping": "Available for $5.99 per item at checkout",
            "International Shipping": "Available to 40+ countries; duties calculated at checkout",
        }
        for topic, detail in topics.items():
            lines.append(f"- **{topic}:** {detail}")
        lines.append("\n## Payment Methods Accepted\n")
        payments = ["Visa", "Mastercard", "Amex", "Discover", "PayPal", "Apple Pay", "Google Pay", "Affirm (Buy Now, Pay Later)"]
        for p in payments:
            lines.append(f"- {p}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = SalesChatAgent()
    print("=" * 60)
    print("EMBEDDED DEMO PRODUCT (works offline)")
    print(agent.perform(operation="product_inquiry", product_id="PROD-101"))
    print()
    print("=" * 60)
    print("LIVE TENANT PRODUCT (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="product_inquiry", product_id="AST-PRN-620"))
    print()
    print("=" * 60)
    print(agent.perform(operation="availability_check", product_id="PROD-103"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="promotion_lookup"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="order_assistance"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
