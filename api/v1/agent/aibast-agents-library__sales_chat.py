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
