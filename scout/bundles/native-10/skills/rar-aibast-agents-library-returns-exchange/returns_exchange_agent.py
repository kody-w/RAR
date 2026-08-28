"""
Returns & Exchange Agent — a template you are meant to mutate.

Manages return initiations, eligibility checks, exchange options,
and refund status tracking for retail operations.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live order records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Live sales orders drive real eligibility math — e.g. ORD-260100
     for Cedar Hollow Printing was fulfilled 2026-01-12, so the 30-day
     window verdict is computed from the actual fulfillment date.
     Try: perform(operation="eligibility_check", order_id="ORD-260100")
  2. No network? Everything falls back to the embedded demo layer below
     (ORDERS / RETURN_POLICIES / EXCHANGE_INVENTORY) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     RETURNS_EXCHANGE_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from your OMS), or replace
     _fetch_collection() with your own API client. Fields the rest of
     the file needs are listed in _normalize_live_order() — everything
     else keeps working untouched. Fields marked "enrichment seam" in
     the output (line items, payment method) are where you wire your
     order-line and payments systems.

OPERATIONS
  return_initiation | eligibility_check | exchange_options | refund_status
  kwargs: operation (required), order_id, item_sku
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timezone

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/returns_exchange",
    "version": "1.1.0",
    "display_name": "Returns & Exchange Agent",
    "description": "Checks return eligibility against live orders from a simulated Dynamics 365 tenant, with exchange and refund flows that work offline.",
    "author": "AIBAST",
    "tags": ["returns", "exchange", "refund", "retail", "customer-service", "b2c"],
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
#   export RETURNS_EXCHANGE_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your OMS client. Downstream code
# only needs the fields produced by _normalize_live_order().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "RETURNS_EXCHANGE_DATA_URL",
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


def _normalize_live_order(row):
    """Project a Dynamics sales order onto the order shape this agent
    uses. THIS is the contract your replacement data source must meet —
    a dict with these keys. None means 'not available from the order
    header alone' and the renderers label it as an enrichment seam."""
    delivered = row.get("datefulfilled")
    return {
        "customer": row.get("customeridname", "Unknown"),
        "order_date": str(row.get("createdon", ""))[:10],
        "items": None,             # enrichment seam — wire your order-line system
        "order_total": float(row.get("totalamount") or 0),
        "shipping_paid": float(row.get("freightamount") or 0),
        "payment_method": None,    # enrichment seam — wire your payments system
        "delivered": str(delivered)[:10] if delivered else None,
        "_live": True,
    }


def _live_orders():
    """ordernumber-keyed dict of live tenant orders; {} when offline."""
    rows = _fetch_collection("salesorders")
    return {
        row["ordernumber"]: _normalize_live_order(row)
        for row in rows
        if row.get("ordernumber")
    }


def _days_since(iso_date):
    try:
        then = datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
        if then.tzinfo is None:
            then = then.replace(tzinfo=timezone.utc)
        return max(0, (datetime.now(timezone.utc) - then).days)
    except (ValueError, TypeError):
        return None


def _live_eligibility(order):
    """Real 30-day-window math against the order's actual fulfillment
    date. Returns (verdict, details)."""
    if not order["delivered"]:
        return False, "Not yet fulfilled — return window has not started"
    days = _days_since(order["delivered"])
    window = RETURN_POLICIES["standard"]["window_days"]
    if days is None:
        return False, "Fulfillment date unreadable"
    if days > window:
        return False, f"Return window expired ({days} days since delivery vs {window}-day policy)"
    return True, f"Eligible — {days} days since delivery, within the {window}-day window"


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

ORDERS = {
    "ORD-55001": {
        "customer": "Amanda Collins",
        "order_date": "2025-02-15",
        "items": [
            {"sku": "DRS-4420", "name": "Midi Wrap Dress — Emerald", "size": "M", "price": 128.00, "qty": 1},
            {"sku": "SHL-2201", "name": "Cashmere Scarf — Charcoal", "price": 89.00, "qty": 1},
        ],
        "order_total": 217.00,
        "shipping_paid": 0.00,
        "payment_method": "credit_card",
        "delivered": "2025-02-20",
    },
    "ORD-55002": {
        "customer": "James Lee",
        "order_date": "2025-01-28",
        "items": [
            {"sku": "SNK-7710", "name": "Premium Leather Sneakers — White", "size": "10", "price": 185.00, "qty": 1},
        ],
        "order_total": 185.00,
        "shipping_paid": 8.95,
        "payment_method": "paypal",
        "delivered": "2025-02-02",
    },
    "ORD-55003": {
        "customer": "Sophie Martin",
        "order_date": "2025-02-25",
        "items": [
            {"sku": "JKT-3315", "name": "Quilted Puffer Jacket — Black", "size": "S", "price": 245.00, "qty": 1},
            {"sku": "BT-1190", "name": "Ankle Rain Boots", "size": "7", "price": 95.00, "qty": 1},
            {"sku": "UM-0050", "name": "Compact Umbrella — Navy", "price": 32.00, "qty": 1},
        ],
        "order_total": 372.00,
        "shipping_paid": 0.00,
        "payment_method": "credit_card",
        "delivered": "2025-03-01",
    },
    "ORD-55004": {
        "customer": "Derek Patel",
        "order_date": "2024-12-10",
        "items": [
            {"sku": "ELEC-8820", "name": "Wireless Earbuds Pro", "price": 159.00, "qty": 1},
        ],
        "order_total": 159.00,
        "shipping_paid": 5.95,
        "payment_method": "credit_card",
        "delivered": "2024-12-15",
    },
}

RETURN_POLICIES = {
    "standard": {"window_days": 30, "condition": "unworn_with_tags", "refund_method": "original_payment", "restocking_fee_pct": 0, "categories": ["apparel", "accessories"]},
    "footwear": {"window_days": 30, "condition": "unworn_original_box", "refund_method": "original_payment", "restocking_fee_pct": 0, "categories": ["footwear"]},
    "electronics": {"window_days": 15, "condition": "unopened_or_defective", "refund_method": "original_payment", "restocking_fee_pct": 15, "categories": ["electronics"]},
    "final_sale": {"window_days": 0, "condition": "no_returns", "refund_method": "none", "restocking_fee_pct": 0, "categories": ["clearance", "intimates"]},
}

EXCHANGE_INVENTORY = {
    "DRS-4420": {"available_sizes": {"XS": 2, "S": 5, "M": 0, "L": 8, "XL": 3}, "available_colors": ["emerald", "navy", "burgundy"]},
    "SNK-7710": {"available_sizes": {"8": 4, "9": 6, "10": 2, "11": 5, "12": 3}, "available_colors": ["white", "black"]},
    "JKT-3315": {"available_sizes": {"XS": 1, "S": 0, "M": 4, "L": 3, "XL": 2}, "available_colors": ["black", "olive"]},
}

REFUND_PROCESSING = {
    "credit_card": {"processing_days": 5, "description": "Refund to original credit card"},
    "paypal": {"processing_days": 3, "description": "Refund to PayPal account"},
    "store_credit": {"processing_days": 1, "description": "Instant store credit issued"},
    "gift_card": {"processing_days": 1, "description": "Refund to gift card balance"},
}

ACTIVE_RETURNS = {
    "RET-8001": {"order": "ORD-55001", "items": ["DRS-4420"], "reason": "wrong_size", "type": "exchange", "status": "awaiting_return", "rma_issued": "2025-03-02", "label_sent": True},
    "RET-8002": {"order": "ORD-55002", "items": ["SNK-7710"], "reason": "defective", "type": "refund", "status": "received_inspecting", "rma_issued": "2025-03-04", "label_sent": True},
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _check_eligibility(order, item_sku):
    """Check return eligibility for an item."""
    delivered = order["delivered"]
    delivered_parts = [int(x) for x in delivered.split("-")]
    delivered_day = delivered_parts[0] * 365 + delivered_parts[1] * 30 + delivered_parts[2]
    today_day = 2025 * 365 + 3 * 30 + 10
    days_since = today_day - delivered_day
    item = next((i for i in order["items"] if i["sku"] == item_sku), None)
    if not item:
        return False, "Item not found in order"
    sku_prefix = item_sku.split("-")[0]
    category_map = {"DRS": "standard", "SHL": "standard", "SNK": "footwear", "JKT": "standard", "BT": "footwear", "UM": "standard", "ELEC": "electronics"}
    policy_key = category_map.get(sku_prefix, "standard")
    policy = RETURN_POLICIES.get(policy_key, RETURN_POLICIES["standard"])
    if policy["window_days"] == 0:
        return False, "Item is final sale — no returns"
    if days_since > policy["window_days"]:
        return False, f"Return window expired ({days_since} days vs {policy['window_days']}-day policy)"
    return True, f"Eligible under {policy_key} policy ({policy['window_days']}-day window)"


def _refund_amount(order, item_sku):
    """Calculate refund amount for an item."""
    item = next((i for i in order["items"] if i["sku"] == item_sku), None)
    if not item:
        return 0
    sku_prefix = item_sku.split("-")[0]
    category_map = {"DRS": "standard", "SHL": "standard", "SNK": "footwear", "JKT": "standard", "BT": "footwear", "UM": "standard", "ELEC": "electronics"}
    policy_key = category_map.get(sku_prefix, "standard")
    policy = RETURN_POLICIES.get(policy_key, RETURN_POLICIES["standard"])
    fee = item["price"] * policy["restocking_fee_pct"] / 100
    return round(item["price"] - fee, 2)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class ReturnsExchangeAgent(BasicAgent):
    """Returns and exchange management agent."""

    def __init__(self):
        self.name = "ReturnsExchangeAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Returns & Exchange Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "return_initiation",
                            "eligibility_check",
                            "exchange_options",
                            "refund_status",
                        ],
                    },
                    "order_id": {"type": "string"},
                    "item_sku": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "return_initiation")
        dispatch = {
            "return_initiation": self._return_initiation,
            "eligibility_check": self._eligibility_check,
            "exchange_options": self._exchange_options,
            "refund_status": self._refund_status,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        return handler(**kwargs)

    def _return_initiation(self, **kwargs) -> str:
        lines = ["# Return Initiation\n"]
        lines.append("## Active Returns\n")
        lines.append("| Return ID | Order | Items | Reason | Type | Status |")
        lines.append("|---|---|---|---|---|---|")
        for rid, ret in ACTIVE_RETURNS.items():
            lines.append(
                f"| {rid} | {ret['order']} | {', '.join(ret['items'])} "
                f"| {ret['reason'].replace('_', ' ').title()} | {ret['type'].title()} "
                f"| {ret['status'].replace('_', ' ').title()} |"
            )
        lines.append("\n## Return Process\n")
        steps = [
            "Customer initiates return request (online or in-store)",
            "System checks eligibility against return policy",
            "RMA number generated and prepaid label sent",
            "Customer ships item back within 7 days",
            "Warehouse receives and inspects item",
            "Refund or exchange processed",
        ]
        for i, step in enumerate(steps, 1):
            lines.append(f"{i}. {step}")
        lines.append("\n## Return Policies\n")
        lines.append("| Policy | Window | Condition | Restocking Fee |")
        lines.append("|---|---|---|---|")
        for pid, pol in RETURN_POLICIES.items():
            window = f"{pol['window_days']} days" if pol["window_days"] > 0 else "No returns"
            lines.append(
                f"| {pid.replace('_', ' ').title()} | {window} "
                f"| {pol['condition'].replace('_', ' ').title()} | {pol['restocking_fee_pct']}% |"
            )
        return "\n".join(lines)

    def _eligibility_check(self, **kwargs) -> str:
        order_id = kwargs.get("order_id")
        item_sku = kwargs.get("item_sku")
        lines = ["# Return Eligibility Check\n"]
        live = _live_orders() if (not order_id or order_id not in ORDERS) else {}
        if order_id and order_id in live:
            order = live[order_id]
            eligible, details = _live_eligibility(order)
            lines.append(f"**Order:** {order_id} (live tenant record)")
            lines.append(f"**Customer:** {order['customer']}")
            lines.append(f"**Order Date:** {order['order_date']}")
            lines.append(f"**Delivered:** {order['delivered'] or 'not yet fulfilled'}")
            lines.append(f"**Order Total:** ${order['order_total']:,.2f}")
            lines.append(f"**Shipping Paid:** ${order['shipping_paid']:,.2f}")
            lines.append("**Payment Method:** n/a — enrichment seam (wire your payments system)\n")
            lines.append("## Order Eligibility\n")
            lines.append(f"- **Eligible:** {'Yes' if eligible else 'No'}")
            lines.append(f"- **Details:** {details}")
            lines.append("- **Line Items:** n/a — enrichment seam (wire your order-line system "
                         "for per-item verdicts)")
            lines.append("\n_Source: live Static Dynamics 365 tenant (salesorders)._")
            return "\n".join(lines)
        if not order_id and live:
            lines.append("## All Orders — Eligibility Summary (live tenant data)\n")
            lines.append("| Order | Customer | Delivered | Total | Eligible |")
            lines.append("|---|---|---|---|---|")
            for oid, order in sorted(live.items()):
                eligible, details = _live_eligibility(order)
                lines.append(
                    f"| {oid} | {order['customer']} | {order['delivered'] or 'not fulfilled'} "
                    f"| ${order['order_total']:,.2f} | {'Yes' if eligible else 'No — ' + details.split(' — ')[0].lower()} |"
                )
            lines.append("\n_Source: live Static Dynamics 365 tenant (salesorders)._")
            return "\n".join(lines)
        if order_id and order_id in ORDERS:
            order = ORDERS[order_id]
            lines.append(f"**Order:** {order_id}")
            lines.append(f"**Customer:** {order['customer']}")
            lines.append(f"**Order Date:** {order['order_date']}")
            lines.append(f"**Delivered:** {order['delivered']}\n")
            lines.append("## Item Eligibility\n")
            lines.append("| SKU | Item | Price | Eligible | Details |")
            lines.append("|---|---|---|---|---|")
            for item in order["items"]:
                eligible, details = _check_eligibility(order, item["sku"])
                status = "Yes" if eligible else "No"
                lines.append(f"| {item['sku']} | {item['name']} | ${item['price']:,.2f} | {status} | {details} |")
        else:
            lines.append("## All Orders — Eligibility Summary\n")
            lines.append("| Order | Customer | Delivered | Items | Eligible |")
            lines.append("|---|---|---|---|---|")
            for oid, order in ORDERS.items():
                eligible_count = sum(1 for i in order["items"] if _check_eligibility(order, i["sku"])[0])
                lines.append(
                    f"| {oid} | {order['customer']} | {order['delivered']} "
                    f"| {len(order['items'])} | {eligible_count}/{len(order['items'])} |"
                )
        return "\n".join(lines)

    def _exchange_options(self, **kwargs) -> str:
        item_sku = kwargs.get("item_sku")
        lines = ["# Exchange Options\n"]
        if item_sku and item_sku in EXCHANGE_INVENTORY:
            inv = EXCHANGE_INVENTORY[item_sku]
            product = None
            for order in ORDERS.values():
                for item in order["items"]:
                    if item["sku"] == item_sku:
                        product = item
                        break
            name = product["name"] if product else item_sku
            lines.append(f"## {name} ({item_sku})\n")
            lines.append("### Available Sizes\n")
            lines.append("| Size | Stock | Status |")
            lines.append("|---|---|---|")
            for size, qty in inv["available_sizes"].items():
                status = "Available" if qty > 0 else "Out of Stock"
                lines.append(f"| {size} | {qty} | {status} |")
            lines.append(f"\n### Available Colors\n")
            for color in inv["available_colors"]:
                lines.append(f"- {color.replace('_', ' ').title()}")
        else:
            lines.append("## Exchange Inventory Summary\n")
            lines.append("| SKU | Sizes Available | Colors |")
            lines.append("|---|---|---|")
            for sku, inv in EXCHANGE_INVENTORY.items():
                available = [s for s, q in inv["available_sizes"].items() if q > 0]
                lines.append(
                    f"| {sku} | {', '.join(available)} "
                    f"| {', '.join(c.replace('_', ' ').title() for c in inv['available_colors'])} |"
                )
        return "\n".join(lines)

    def _refund_status(self, **kwargs) -> str:
        lines = ["# Refund Status\n"]
        lines.append("## Active Returns & Refunds\n")
        for rid, ret in ACTIVE_RETURNS.items():
            order = ORDERS.get(ret["order"], {})
            lines.append(f"### {rid}\n")
            lines.append(f"- **Order:** {ret['order']}")
            lines.append(f"- **Customer:** {order.get('customer', 'Unknown')}")
            lines.append(f"- **Items:** {', '.join(ret['items'])}")
            lines.append(f"- **Reason:** {ret['reason'].replace('_', ' ').title()}")
            lines.append(f"- **Type:** {ret['type'].title()}")
            lines.append(f"- **Status:** {ret['status'].replace('_', ' ').title()}")
            lines.append(f"- **RMA Issued:** {ret['rma_issued']}")
            if ret["type"] == "refund":
                payment = order.get("payment_method", "credit_card")
                processing = REFUND_PROCESSING.get(payment, {})
                for item_sku in ret["items"]:
                    amount = _refund_amount(order, item_sku)
                    lines.append(f"- **Refund Amount:** ${amount:,.2f}")
                lines.append(f"- **Refund Method:** {processing.get('description', 'N/A')}")
                lines.append(f"- **Processing Time:** {processing.get('processing_days', 'N/A')} business days")
            lines.append("")
        lines.append("## Refund Processing Times\n")
        lines.append("| Method | Processing Time | Description |")
        lines.append("|---|---|---|")
        for method, info in REFUND_PROCESSING.items():
            lines.append(f"| {method.replace('_', ' ').title()} | {info['processing_days']} days | {info['description']} |")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = ReturnsExchangeAgent()
    print("=" * 60)
    print("EMBEDDED DEMO ORDER (works offline)")
    print(agent.perform(operation="eligibility_check", order_id="ORD-55001"))
    print()
    print("=" * 60)
    print("LIVE TENANT ORDER (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="eligibility_check", order_id="ORD-260100"))
    print()
    print("=" * 60)
    print(agent.perform(operation="return_initiation"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="refund_status"))
