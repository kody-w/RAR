---
name: "rar-aibast-agents-library-returns-exchange"
description: "Checks return eligibility against live orders from a simulated Dynamics 365 tenant, with exchange and refund flows that work offline."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/returns_exchange", "rar_sha256": "89065ae5961458e590f5aeb78b797ad3f71bd85632b4e5d9d4f7f951b9c3d444", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["returns", "exchange", "refund", "retail", "customer-service", "b2c"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/returns_exchange`. The original RAPP
agent is preserved byte-for-byte in `returns_exchange_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "item_sku": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "return_initiation",
        "eligibility_check",
        "exchange_options",
        "refund_status"
      ],
      "type": "string"
    },
    "order_id": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `returns_exchange_agent.py` and embedded as the fenced Python below (sha256 89065ae5961458e5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `returns_exchange_agent.py` first:

```bash
python3 returns_exchange_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 returns_exchange_agent.py   # or on stdin
python3 returns_exchange_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
