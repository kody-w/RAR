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
