---
name: "rar-aibast-agents-library-cart-abandonment-recovery"
description: "Analyzes stalled checkouts from live orders in a simulated Dynamics 365 tenant, with recovery tooling and an embedded offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/cart_abandonment_recovery", "rar_sha256": "f74e09c3d9a4fbe53fca3697ab5d147b766ded273023ef10507f94b1278e0dc2", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["cart-abandonment", "recovery", "ecommerce", "conversion", "email", "b2c"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/cart_abandonment_recovery`. The original RAPP
agent is preserved byte-for-byte in `cart_abandonment_recovery_agent.py` and in the RCI capsule.

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

Cart Abandonment Recovery Agent — a template you are meant to mutate.

Analyzes cart abandonment patterns, manages recovery campaigns, optimizes
incentives, and tracks conversion metrics for e-commerce teams.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live sales orders over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere). In
     this template an UNFULFILLED or CANCELED Dynamics sales order is
     reinterpreted as an abandoned/stalled checkout:
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="abandonment_analysis") — live stalled
     checkouts include order ORD-260102 for Marigold Field Services
     ($2,880, still Submitted).
  2. No network? Everything falls back to the embedded demo layer below
     (ABANDONED_CARTS / RECOVERY_CAMPAIGNS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CART_ABANDONMENT_RECOVERY_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON you export from Shopify/your
     commerce stack), or replace _fetch_collection() with your own
     client. The dict shape the rest of the file needs is documented in
     _normalize_live_cart(). Exit page, device, and segment are
     enrichment seams — wire your web analytics there; campaign and
     incentive ops stay simulated until you do.

OPERATIONS
  abandonment_analysis | recovery_campaign | incentive_optimization
  | conversion_tracking | cart_opportunity_scan | segment_recovery_strategy
  | campaign_launch | recovery_forecast | recovery_optimization
  kwargs: operation (required), cart_id, user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "cart_id": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "abandonment_analysis",
        "recovery_campaign",
        "incentive_optimization",
        "conversion_tracking",
        "cart_opportunity_scan",
        "segment_recovery_strategy",
        "campaign_launch",
        "recovery_forecast",
        "recovery_optimization"
      ],
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `cart_abandonment_recovery_agent.py` and embedded as the fenced Python below (sha256 f74e09c3d9a4fbe5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `cart_abandonment_recovery_agent.py` first:

```bash
python3 cart_abandonment_recovery_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 cart_abandonment_recovery_agent.py   # or on stdin
python3 cart_abandonment_recovery_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cart Abandonment Recovery Agent — a template you are meant to mutate.

Analyzes cart abandonment patterns, manages recovery campaigns, optimizes
incentives, and tracks conversion metrics for e-commerce teams.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live sales orders over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere). In
     this template an UNFULFILLED or CANCELED Dynamics sales order is
     reinterpreted as an abandoned/stalled checkout:
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="abandonment_analysis") — live stalled
     checkouts include order ORD-260102 for Marigold Field Services
     ($2,880, still Submitted).
  2. No network? Everything falls back to the embedded demo layer below
     (ABANDONED_CARTS / RECOVERY_CAMPAIGNS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CART_ABANDONMENT_RECOVERY_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON you export from Shopify/your
     commerce stack), or replace _fetch_collection() with your own
     client. The dict shape the rest of the file needs is documented in
     _normalize_live_cart(). Exit page, device, and segment are
     enrichment seams — wire your web analytics there; campaign and
     incentive ops stay simulated until you do.

OPERATIONS
  abandonment_analysis | recovery_campaign | incentive_optimization
  | conversion_tracking | cart_opportunity_scan | segment_recovery_strategy
  | campaign_launch | recovery_forecast | recovery_optimization
  kwargs: operation (required), cart_id, user_input
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/cart_abandonment_recovery",
    "version": "1.2.0",
    "display_name": "Cart Abandonment Recovery Agent",
    "description": "Analyzes stalled checkouts from live orders in a simulated Dynamics 365 tenant, with recovery tooling and an embedded offline demo fallback.",
    "author": "AIBAST",
    "tags": ["cart-abandonment", "recovery", "ecommerce", "conversion", "email", "b2c"],
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
# GitHub Pages). In this template an unfulfilled/canceled sales order is
# reinterpreted as an abandoned checkout. To hook your own world, either:
#   export CART_ABANDONMENT_RECOVERY_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your commerce client. Downstream
# code only needs the fields produced by _normalize_live_cart().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "CART_ABANDONMENT_RECOVERY_DATA_URL",
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


def _normalize_live_cart(row):
    """Project a Dynamics sales order onto the cart shape this agent uses.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not knowable from the CRM alone' and the
    renderers label it an enrichment seam (exit page, device, and segment
    come from your web analytics)."""
    status = row.get("statecode@OData.Community.Display.V1.FormattedValue", "")
    return {
        "cart_id": row.get("ordernumber", "ORD-?"),
        "customer": row.get("customeridname", "Unknown"),
        "cart_value": float(row.get("totalamount") or 0),
        "status": status,
        "abandoned_at": str(row.get("createdon") or "")[:10],
        "segment": None,    # enrichment seam — wire your CDP
        "page_exit": None,  # enrichment seam — wire web analytics
        "device": None,     # enrichment seam
        "_live": True,
    }


def _live_stalled_checkouts():
    """Live unfulfilled/canceled sales orders as stalled checkouts;
    [] when offline."""
    return [_normalize_live_cart(o) for o in _fetch_collection("salesorders")
            if not o.get("datefulfilled")]


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

ABANDONED_CARTS = {
    "CART-20001": {
        "customer": "Emily Rodriguez",
        "email": "e.rodriguez@example.com",
        "segment": "loyal_shopper",
        "items": [
            {"name": "Wireless Noise-Canceling Headphones", "sku": "ELEC-4421", "price": 249.99, "qty": 1},
            {"name": "Premium Headphone Case", "sku": "ACC-1102", "price": 34.99, "qty": 1},
        ],
        "cart_value": 284.98,
        "abandoned_at": "2025-03-04T14:22:00",
        "page_exit": "shipping_options",
        "device": "mobile",
        "prior_purchases": 8,
        "recovery_status": "email_1_sent",
    },
    "CART-20002": {
        "customer": "Michael Tang",
        "email": "m.tang@example.com",
        "segment": "new_visitor",
        "items": [
            {"name": "Smart Home Hub Pro", "sku": "SMRT-3305", "price": 179.99, "qty": 1},
            {"name": "Smart Bulb 4-Pack", "sku": "SMRT-1140", "price": 59.99, "qty": 2},
        ],
        "cart_value": 299.97,
        "abandoned_at": "2025-03-05T09:15:00",
        "page_exit": "account_creation",
        "device": "desktop",
        "prior_purchases": 0,
        "recovery_status": "not_contacted",
    },
    "CART-20003": {
        "customer": "Sarah Kim",
        "email": "s.kim@example.com",
        "segment": "high_value",
        "items": [
            {"name": "4K OLED Smart TV 65-inch", "sku": "TV-7720", "price": 1299.99, "qty": 1},
            {"name": "Soundbar System", "sku": "AUD-5501", "price": 449.99, "qty": 1},
            {"name": "HDMI Cable 6ft", "sku": "ACC-0042", "price": 14.99, "qty": 2},
        ],
        "cart_value": 1779.96,
        "abandoned_at": "2025-03-05T18:45:00",
        "page_exit": "payment",
        "device": "desktop",
        "prior_purchases": 12,
        "recovery_status": "not_contacted",
    },
    "CART-20004": {
        "customer": "Guest User",
        "email": None,
        "segment": "guest",
        "items": [
            {"name": "Running Shoes Pro X", "sku": "SHOE-2201", "price": 129.99, "qty": 1},
        ],
        "cart_value": 129.99,
        "abandoned_at": "2025-03-06T11:30:00",
        "page_exit": "cart_page",
        "device": "mobile",
        "prior_purchases": 0,
        "recovery_status": "unrecoverable",
    },
}

RECOVERY_CAMPAIGNS = {
    "email_1": {"name": "Reminder Email", "delay_hours": 1, "subject": "You left something behind!", "incentive": None, "avg_open_rate": 45.2, "avg_conversion": 8.5},
    "email_2": {"name": "Urgency Email", "delay_hours": 24, "subject": "Your cart is waiting — items selling fast", "incentive": None, "avg_open_rate": 38.1, "avg_conversion": 5.2},
    "email_3": {"name": "Incentive Email", "delay_hours": 72, "subject": "Here's 10% off to complete your order", "incentive": "10% discount", "avg_open_rate": 42.8, "avg_conversion": 12.1},
    "sms_1": {"name": "SMS Reminder", "delay_hours": 2, "subject": "Complete your order at [Store]", "incentive": None, "avg_open_rate": 98.0, "avg_conversion": 4.8},
    "retargeting_ad": {"name": "Retargeting Display Ad", "delay_hours": 6, "subject": "Dynamic product ad on social/display", "incentive": None, "avg_open_rate": 0, "avg_conversion": 2.1},
}

INCENTIVE_OPTIONS = {
    "percent_off_10": {"description": "10% off cart total", "cost_margin_impact": 10.0, "conversion_lift": 35.0},
    "percent_off_15": {"description": "15% off cart total", "cost_margin_impact": 15.0, "conversion_lift": 48.0},
    "free_shipping": {"description": "Free standard shipping", "cost_margin_impact": 5.5, "conversion_lift": 28.0},
    "dollar_off_20": {"description": "$20 off orders over $150", "cost_margin_impact": 8.0, "conversion_lift": 22.0},
    "gift_with_purchase": {"description": "Free accessory with order", "cost_margin_impact": 6.0, "conversion_lift": 18.0},
}

CONVERSION_METRICS = {
    "overall_abandonment_rate": 71.4,
    "recovery_rate": 12.8,
    "avg_recovered_value": 187.50,
    "total_abandoned_30d": 4250,
    "total_recovered_30d": 544,
    "total_recovered_revenue_30d": 102000,
}

EVIDENCE_ACTIONS = {
    "cart_opportunity_scan": {
        "title": "Today's Cart Opportunity Scan",
        "write": False,
        "records": [
            {"record_id": "CART-SCAN-VIP", "segment": "VIP", "carts": 34, "value": "$18K", "recovery_likelihood": "45%"},
            {"record_id": "CART-SCAN-REPEAT", "segment": "Repeat buyers", "carts": 89, "value": "$24K", "recovery_likelihood": "38%"},
            {"record_id": "CART-SCAN-NEW", "segment": "New visitors", "carts": 412, "value": "$53K", "recovery_likelihood": "22%"},
        ],
        "context": "847 carts worth $127K; top opportunities Sarah M. $892, James K. $647, Emily R. $534; drivers: shipping 42%, comparison shopping 28%, payment friction 18%.",
    },
    "segment_recovery_strategy": {
        "title": "Personalized Segment Recovery Strategies",
        "write": False,
        "records": [
            {"record_id": "STRAT-VIP", "segment": "VIP", "offer": "personal note and express shipping", "sequence": "email, SMS at 1h, shipping offer at 4h, call at 24h for carts over $500"},
            {"record_id": "STRAT-REPEAT", "segment": "Repeat buyers", "offer": "points reminder and free shipping", "sequence": "email, push at 2h, shipping hint at 12h"},
            {"record_id": "STRAT-NEW", "segment": "New visitors", "offer": "welcome 10% off", "sequence": "email, retargeting, social proof at 24h"},
        ],
        "context": "Strategies reflect customer value, intent, urgency, and margin-protecting guardrails.",
    },
    "campaign_launch": {
        "title": "Multi-Touch Campaign Launch",
        "write": True,
        "records": [
            {"record_id": "CAMP-HIGH-VALUE", "campaign": "High-value win-back", "members": 8400, "status": "sent", "channels": "Outlook email and SMS"},
            {"record_id": "CAMP-POINT-EXPIRY", "campaign": "Point expiry alert", "members": 12000, "status": "sent", "channels": "Outlook email and push"},
            {"record_id": "CAMP-LAPSED", "campaign": "Lapsed browser", "members": 13600, "status": "active", "channels": "email and retargeting"},
        ],
        "context": "Preview-only orchestration for Outlook with real-time Microsoft Teams updates.",
    },
    "recovery_forecast": {
        "title": "48-Hour Recovery Forecast",
        "write": False,
        "records": [
            {"record_id": "FCST-VIP", "segment": "VIP", "recovery": "45%", "revenue": "$8,280"},
            {"record_id": "FCST-REPEAT", "segment": "Repeat buyers", "recovery": "38%", "revenue": "$9,196"},
            {"record_id": "FCST-NEW", "segment": "New visitors", "recovery": "22%", "revenue": "$11,616"},
            {"record_id": "FCST-TOTAL", "segment": "Total", "recovery": "27%", "revenue": "$37,940"},
        ],
        "context": "Industry benchmark 18%; target 27%; monthly impact rises from $172K to $228K (+$56K).",
    },
    "recovery_optimization": {
        "title": "Recovery Rate Optimization",
        "write": False,
        "records": [
            {"record_id": "OPT-EXIT-INTENT", "opportunity": "Exit-intent 10% popup", "impact": "+$18K/month", "detail": "8-12% conversion; same-day implementation"},
            {"record_id": "OPT-SMS", "opportunity": "SMS all segments", "impact": "+$12K/month", "detail": "channel expansion"},
            {"record_id": "OPT-DYNAMIC-PRICE", "opportunity": "Dynamic pricing", "impact": "+$8K/month", "detail": "protect margin with targeted offers"},
            {"record_id": "OPT-SHIPPING", "opportunity": "Lower free-shipping threshold $75 to $65", "impact": "+$6K/month", "detail": "addresses 42% shipping-reveal abandonment"},
        ],
        "context": "Combined opportunities target recovery improvement from 27% to 35%.",
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
            return "No exact `record_id` match was found; no substitute cart or segment was used."
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
            f"- receipt_id: SIM-CART-CAMPAIGN-{receipt_key}",
            "- status: simulated",
            "- target_systems: Outlook and Microsoft Teams",
            "- No external system changed; campaign sends and updates are preview-only.",
        ])
    else:
        lines.append("\n_Read-only analysis; no external system changed._")
    return "\n".join(lines)

def _abandonment_by_exit():
    """Break down abandonment by exit page."""
    by_page = {}
    for cart in ABANDONED_CARTS.values():
        page = cart["page_exit"]
        by_page[page] = by_page.get(page, 0) + 1
    return by_page


def _recommended_incentive(cart):
    """Recommend optimal incentive based on cart value and customer segment."""
    if cart["segment"] == "high_value" and cart["cart_value"] > 500:
        return "percent_off_10"
    elif cart["segment"] == "loyal_shopper":
        return "free_shipping"
    elif cart["segment"] == "new_visitor":
        return "percent_off_15"
    return "dollar_off_20"


def _total_abandoned_value():
    """Sum of all abandoned cart values."""
    return sum(c["cart_value"] for c in ABANDONED_CARTS.values())


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class CartAbandonmentRecoveryAgent(BasicAgent):
    """Cart abandonment recovery agent for e-commerce."""

    def __init__(self):
        self.name = "CartAbandonmentRecoveryAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Cart Abandonment Recovery Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "abandonment_analysis",
                            "recovery_campaign",
                            "incentive_optimization",
                            "conversion_tracking",
                            "cart_opportunity_scan",
                            "segment_recovery_strategy",
                            "campaign_launch",
                            "recovery_forecast",
                            "recovery_optimization",
                        ],
                    },
                    "cart_id": {"type": "string"},
                    "user_input": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "abandonment_analysis")
        dispatch = {
            "abandonment_analysis": self._abandonment_analysis,
            "recovery_campaign": self._recovery_campaign,
            "incentive_optimization": self._incentive_optimization,
            "conversion_tracking": self._conversion_tracking,
            "cart_opportunity_scan": self._evidence_action,
            "segment_recovery_strategy": self._evidence_action,
            "campaign_launch": self._evidence_action,
            "recovery_forecast": self._evidence_action,
            "recovery_optimization": self._evidence_action,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        if operation in EVIDENCE_ACTIONS:
            return handler(operation, **kwargs)
        return handler(**kwargs)

    def _evidence_action(self, action, **kwargs) -> str:
        return _evidence_action(action, **kwargs)

    def _abandonment_analysis(self, **kwargs) -> str:
        live = _live_stalled_checkouts()
        if live:
            total_value = sum(c["cart_value"] for c in live)
            lines = ["# Cart Abandonment Analysis — LIVE stalled checkouts "
                     "(Static Dynamics 365 tenant)\n"]
            lines.append("In this template an unfulfilled or canceled Dynamics "
                         "sales order is treated as an abandoned checkout.\n")
            lines.append(f"**Stalled Checkouts:** {len(live)}")
            lines.append(f"**Total Value at Risk:** ${total_value:,.2f}\n")
            lines.append("## Stalled Checkout Detail\n")
            lines.append("| Order | Customer | Value | Order Status | Created | Exit Page | Device |")
            lines.append("|---|---|---|---|---|---|---|")
            for c in sorted(live, key=lambda x: -x["cart_value"]):
                lines.append(
                    f"| {c['cart_id']} | {c['customer']} | ${c['cart_value']:,.2f} "
                    f"| {c['status']} | {c['abandoned_at']} "
                    f"| n/a — enrichment seam | n/a |"
                )
            lines.append("\nExit page, device, and segment stay n/a until you "
                         "wire your web analytics at the LIVE DATA SEAM.")
            return "\n".join(lines)
        total_value = _total_abandoned_value()
        by_exit = _abandonment_by_exit()
        lines = ["# Cart Abandonment Analysis\n"]
        lines.append(f"**Abandoned Carts:** {len(ABANDONED_CARTS)}")
        lines.append(f"**Total Abandoned Value:** ${total_value:,.2f}")
        lines.append(f"**Abandonment Rate:** {CONVERSION_METRICS['overall_abandonment_rate']}%\n")
        lines.append("## Abandoned Carts Detail\n")
        lines.append("| Cart ID | Customer | Segment | Value | Exit Page | Device | Status |")
        lines.append("|---|---|---|---|---|---|---|")
        for cid, c in ABANDONED_CARTS.items():
            lines.append(
                f"| {cid} | {c['customer']} | {c['segment'].replace('_', ' ').title()} "
                f"| ${c['cart_value']:,.2f} | {c['page_exit'].replace('_', ' ').title()} "
                f"| {c['device'].title()} | {c['recovery_status'].replace('_', ' ').title()} |"
            )
        lines.append("\n## Exit Page Breakdown\n")
        for page, count in by_exit.items():
            lines.append(f"- {page.replace('_', ' ').title()}: {count}")
        return "\n".join(lines)

    def _recovery_campaign(self, **kwargs) -> str:
        lines = ["# Recovery Campaign Dashboard\n"]
        lines.append("## Campaign Sequence\n")
        lines.append("| Campaign | Delay | Subject | Incentive | Open Rate | Conversion |")
        lines.append("|---|---|---|---|---|---|")
        for cid, camp in RECOVERY_CAMPAIGNS.items():
            incentive = camp["incentive"] or "None"
            lines.append(
                f"| {camp['name']} | {camp['delay_hours']}h | {camp['subject']} "
                f"| {incentive} | {camp['avg_open_rate']}% | {camp['avg_conversion']}% |"
            )
        lines.append("\n## Carts Pending Recovery\n")
        pending = {k: v for k, v in ABANDONED_CARTS.items() if v["recovery_status"] != "unrecoverable" and v["email"] is not None}
        for cid, cart in pending.items():
            lines.append(f"- **{cid}** ({cart['customer']}): ${cart['cart_value']:,.2f} — Status: {cart['recovery_status'].replace('_', ' ').title()}")
        unrecoverable = sum(1 for c in ABANDONED_CARTS.values() if c["recovery_status"] == "unrecoverable")
        lines.append(f"\n**Unrecoverable (no email):** {unrecoverable}")
        return "\n".join(lines)

    def _incentive_optimization(self, **kwargs) -> str:
        lines = ["# Incentive Optimization\n"]
        lines.append("## Available Incentives\n")
        lines.append("| Incentive | Description | Margin Impact | Conversion Lift |")
        lines.append("|---|---|---|---|")
        for iid, inc in INCENTIVE_OPTIONS.items():
            lines.append(f"| {iid.replace('_', ' ').title()} | {inc['description']} | {inc['cost_margin_impact']}% | +{inc['conversion_lift']}% |")
        lines.append("\n## Recommended Incentives by Cart\n")
        for cid, cart in ABANDONED_CARTS.items():
            if cart["recovery_status"] == "unrecoverable":
                continue
            rec = _recommended_incentive(cart)
            inc = INCENTIVE_OPTIONS[rec]
            lines.append(f"### {cid}: {cart['customer']} (${cart['cart_value']:,.2f})\n")
            lines.append(f"- **Segment:** {cart['segment'].replace('_', ' ').title()}")
            lines.append(f"- **Recommended:** {inc['description']}")
            lines.append(f"- **Expected Lift:** +{inc['conversion_lift']}%")
            est_recovery = cart["cart_value"] * (1 - inc["cost_margin_impact"] / 100)
            lines.append(f"- **Net Recovery Value:** ${est_recovery:,.2f}\n")
        return "\n".join(lines)

    def _conversion_tracking(self, **kwargs) -> str:
        m = CONVERSION_METRICS
        lines = ["# Conversion Tracking (30-Day)\n"]
        lines.append(f"- **Abandonment Rate:** {m['overall_abandonment_rate']}%")
        lines.append(f"- **Recovery Rate:** {m['recovery_rate']}%")
        lines.append(f"- **Avg Recovered Order Value:** ${m['avg_recovered_value']:,.2f}")
        lines.append(f"- **Total Abandoned Carts:** {m['total_abandoned_30d']:,}")
        lines.append(f"- **Total Recovered:** {m['total_recovered_30d']:,}")
        lines.append(f"- **Recovered Revenue:** ${m['total_recovered_revenue_30d']:,.0f}\n")
        lines.append("## Campaign Performance\n")
        lines.append("| Campaign | Open Rate | Conversion | Est. Recovered |")
        lines.append("|---|---|---|---|")
        for cid, camp in RECOVERY_CAMPAIGNS.items():
            est = round(m["total_abandoned_30d"] * camp["avg_conversion"] / 100 * m["avg_recovered_value"], 0)
            lines.append(f"| {camp['name']} | {camp['avg_open_rate']}% | {camp['avg_conversion']}% | ${est:,.0f} |")
        potential = _total_abandoned_value()
        lines.append(f"\n**Current Active Cart Value at Risk:** ${potential:,.2f}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = CartAbandonmentRecoveryAgent()
    print("=" * 80)
    print("LIVE TENANT STALLED CHECKOUTS (fetched over HTTP; embedded demo offline)")
    print(agent.perform(operation="abandonment_analysis"))
    print("\n" + "=" * 80 + "\n")
    print("EMBEDDED DEMO (works offline, simulated)")
    print(agent.perform(operation="recovery_campaign"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="conversion_tracking"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
