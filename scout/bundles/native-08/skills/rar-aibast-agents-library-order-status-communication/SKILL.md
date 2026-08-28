---
name: "rar-aibast-agents-library-order-status-communication"
description: "Tracks orders and drafts delay and status communications from a live simulated Dynamics 365 tenant, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/order_status_communication", "rar_sha256": "d42aa6d42446646d0f1307cc0b3b813e6b10f59f211da17d529fceee878135b3", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["orders", "communication", "shipment", "customer-service", "manufacturing"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/order_status_communication`. The original RAPP
agent is preserved byte-for-byte in `order_status_communication_agent.py` and in the RCI capsule.

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

Order Status Communication Agent — a template you are meant to mutate.

Tracks manufacturing orders through production and shipment stages,
generates customer-facing status updates, identifies delays proactively,
and drafts notification messages with recovery timelines.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     The tenant's sales orders map onto this agent's order book directly
     — e.g. order "ORD-260100" for Cedar Hollow Printing (Fulfilled).
     Try: perform(operation="order_lookup")
  2. No network? Everything falls back to the embedded demo layer below
     (ORDERS / SHIPMENTS / DELAY_REASONS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     ORDER_STATUS_COMMUNICATION_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your ERP/OMS), or
     replace _fetch_collection() with a SAP/NetSuite order API client.
     Fields the rest of the file needs are listed in
     _normalize_live_order() — production percent-complete and carrier
     tracking render as "n/a — enrichment seam" until you wire your MES
     and carrier APIs.

OPERATIONS
  order_lookup | shipment_tracking | delay_notification | customer_update
  | recovery_plan | engagement_execution | quality_validation
  | performance_review
  kwargs: operation (required), order_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "Operation to perform. Defaults to order_lookup when omitted.",
      "enum": [
        "order_lookup",
        "shipment_tracking",
        "delay_notification",
        "customer_update",
        "recovery_plan",
        "engagement_execution",
        "quality_validation",
        "performance_review"
      ],
      "type": "string"
    },
    "order_id": {
      "description": "Order identifier used to select recovery, engagement, quality, and performance records.",
      "type": "string"
    }
  },
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `order_status_communication_agent.py` and embedded as the fenced Python below (sha256 d42aa6d42446646d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `order_status_communication_agent.py` first:

```bash
python3 order_status_communication_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 order_status_communication_agent.py   # or on stdin
python3 order_status_communication_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Order Status Communication Agent — a template you are meant to mutate.

Tracks manufacturing orders through production and shipment stages,
generates customer-facing status updates, identifies delays proactively,
and drafts notification messages with recovery timelines.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     The tenant's sales orders map onto this agent's order book directly
     — e.g. order "ORD-260100" for Cedar Hollow Printing (Fulfilled).
     Try: perform(operation="order_lookup")
  2. No network? Everything falls back to the embedded demo layer below
     (ORDERS / SHIPMENTS / DELAY_REASONS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     ORDER_STATUS_COMMUNICATION_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your ERP/OMS), or
     replace _fetch_collection() with a SAP/NetSuite order API client.
     Fields the rest of the file needs are listed in
     _normalize_live_order() — production percent-complete and carrier
     tracking render as "n/a — enrichment seam" until you wire your MES
     and carrier APIs.

OPERATIONS
  order_lookup | shipment_tracking | delay_notification | customer_update
  | recovery_plan | engagement_execution | quality_validation
  | performance_review
  kwargs: operation (required), order_id
"""

import sys
import os
import json
import urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/order_status_communication",
    "version": "1.2.0",
    "display_name": "Order Status Communication Agent",
    "description": "Tracks orders and drafts delay and status communications from a live simulated Dynamics 365 tenant, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["orders", "communication", "shipment", "customer-service", "manufacturing"],
    "category": "manufacturing",
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
#   export ORDER_STATUS_COMMUNICATION_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your ERP/OMS client. Downstream
# code only needs the fields produced by _normalize_live_order().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "ORDER_STATUS_COMMUNICATION_DATA_URL",
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
    """Project a Dynamics sales order onto the order-book row this agent
    renders. THIS is the contract your replacement data source must meet —
    a dict with these keys. None means 'not knowable from the CRM order
    alone' and the renderer labels it as an enrichment seam (wire your MES
    for percent-complete and your carrier API for tracking)."""
    return {
        "id": row.get("ordernumber", "?"),
        "customer": row.get("customeridname", "Unknown"),
        "product": row.get("name", "n/a"),
        "value": float(row.get("totalamount") or 0),
        "status": row.get(
            "statecode@OData.Community.Display.V1.FormattedValue", "Unknown"
        ),
        "promised_date": str(row.get("requestdeliveryby") or "")[:10] or "n/a",
        "fulfilled_date": str(row.get("datefulfilled") or "")[:10] or None,
        "pct_complete": None,  # enrichment seam — wire your MES
        "_live": True,
    }


def _live_order_book():
    """Sales orders from the live tenant; [] when offline."""
    return [_normalize_live_order(r) for r in _fetch_collection("salesorders")]


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

ORDERS = {
    "ORD-7810": {
        "customer": "Ford Motor Company",
        "contact_name": "James Mitchell",
        "contact_email": "j.mitchell@ford.example.com",
        "product": "6R140 Transmission Housing",
        "quantity": 2500,
        "unit_price": 168.00,
        "order_date": "2026-02-01",
        "promised_date": "2026-03-20",
        "status": "in_production",
        "pct_complete": 74,
    },
    "ORD-7811": {
        "customer": "Caterpillar Inc.",
        "contact_name": "Rita Vasquez",
        "contact_email": "r.vasquez@cat.example.com",
        "product": "D11 Track Frame Weldment",
        "quantity": 40,
        "unit_price": 12450.00,
        "order_date": "2026-01-15",
        "promised_date": "2026-04-10",
        "status": "in_production",
        "pct_complete": 45,
    },
    "ORD-7812": {
        "customer": "Tesla Inc.",
        "contact_name": "Derek Chung",
        "contact_email": "d.chung@tesla.example.com",
        "product": "Model Y Rocker Panel Stamping",
        "quantity": 8000,
        "unit_price": 42.50,
        "order_date": "2026-02-10",
        "promised_date": "2026-03-15",
        "status": "shipped",
        "pct_complete": 100,
    },
    "ORD-7813": {
        "customer": "John Deere",
        "contact_name": "Angela Torres",
        "contact_email": "a.torres@deere.example.com",
        "product": "Hydraulic Cylinder Barrel",
        "quantity": 600,
        "unit_price": 385.00,
        "order_date": "2026-02-18",
        "promised_date": "2026-03-28",
        "status": "delayed",
        "pct_complete": 30,
    },
}

SHIPMENTS = {
    "ORD-7812": {
        "carrier": "XPO Logistics",
        "tracking_number": "XPO-884291047",
        "ship_date": "2026-03-12",
        "est_delivery": "2026-03-15",
        "origin": "Detroit, MI",
        "destination": "Fremont, CA",
        "weight_kg": 4200,
        "status": "in_transit",
    },
}

DELAY_REASONS = {
    "ORD-7813": {
        "reason": "Raw material shortage -- alloy steel bar stock delayed from supplier",
        "original_date": "2026-03-28",
        "revised_date": "2026-04-08",
        "days_delayed": 11,
        "recovery_actions": [
            "Alternate supplier qualified; first shipment arriving 2026-03-19",
            "Weekend overtime shifts approved for CNC cell",
            "Partial shipment of 200 units by 2026-03-28",
        ],
        "cost_impact": 14200.00,
    },
}

CUSTOMER_CONTACTS = {
    "Ford Motor Company": {
        "account_manager": "Sarah Lin",
        "escalation_contact": "Tom Bradley, Plant Manager",
        "preferred_channel": "email",
        "sla_response_hours": 4,
    },
    "Caterpillar Inc.": {
        "account_manager": "Robert Kim",
        "escalation_contact": "VP Supply Chain",
        "preferred_channel": "EDI",
        "sla_response_hours": 8,
    },
    "Tesla Inc.": {
        "account_manager": "Sarah Lin",
        "escalation_contact": "Logistics Director",
        "preferred_channel": "portal",
        "sla_response_hours": 2,
    },
    "John Deere": {
        "account_manager": "Robert Kim",
        "escalation_contact": "Procurement Director",
        "preferred_channel": "email",
        "sla_response_hours": 4,
    },
}

RECOVERY_PLANS = {
    "ORD-7813": {
        "root_cause": "Alloy steel bar stock shipment missed supplier departure cutoff",
        "containment": "Release 200-unit partial shipment from completed stock",
        "corrective_action": "Dual-source remaining bar stock and add weekend CNC shifts",
        "revised_milestones": ["200 units: 2026-03-28", "400 units: 2026-04-04", "complete: 2026-04-08"],
        "owner": "Robert Kim", "next_review": "2026-03-20 09:00",
    },
}

QUALITY_VALIDATIONS = {
    "ORD-7813": {
        "incoming_material": "Mill certificate MTR-7813 verified; chemistry within ASTM A519",
        "production_quality": "First-piece dimensional inspection passed 18/18 characteristics",
        "final_validation": "Pressure test required on each recovery lot before release",
        "quality_status": "conditional release approved",
    },
    "ORD-7812": {
        "incoming_material": "Coil certificate COIL-MY-442 verified",
        "production_quality": "Stamping capability Cpk 1.48",
        "final_validation": "Final dimensional audit passed",
        "quality_status": "released",
    },
}

PERFORMANCE_RECORDS = {
    "ORD-7813": {
        "on_time_before_pct": 82, "on_time_recovery_pct": 96,
        "quality_ppm_before": 920, "quality_ppm_recovery": 310,
        "customer_inquiries_before": 14, "customer_inquiries_after": 3,
        "lesson": "Trigger dual-source review when material ETA slips more than 48 hours",
    },
}

EVIDENCE_MARKER = (
    "[Evidence: order-status-communication one-pager and demo transcript; "
    "recovery planning, multichannel execution, QA validation, and performance review]"
)

DELIVERY_DATE_CONTRACT_CASES = (
    {"order_id": "ORD-7813", "expected": "2026-04-08", "obsolete": "2026-03-28"},
    {"order_id": "ORD-7810", "expected": "2026-03-20", "obsolete": None},
)


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _order_value(order_id):
    """Total dollar value of an order."""
    o = ORDERS[order_id]
    return round(o["quantity"] * o["unit_price"], 2)


def _is_at_risk(order_id):
    """Determine if an order is delayed or at risk of missing its date."""
    return ORDERS[order_id]["status"] == "delayed" or order_id in DELAY_REASONS


def _published_delivery_date(order_id):
    """Return a revised delivery date when one exists, otherwise the promise date."""
    delay = DELAY_REASONS.get(order_id, {})
    return delay.get("revised_date", ORDERS[order_id]["promised_date"])


def _days_until_promise(order_id):
    """Rough days remaining until promised delivery (fixed calculation)."""
    # Using a fixed reference of 2026-03-17 for deterministic output
    promise = ORDERS[order_id]["promised_date"]
    year, month, day = map(int, promise.split("-"))
    ref_year, ref_month, ref_day = 2026, 3, 17
    return (year - ref_year) * 365 + (month - ref_month) * 30 + (day - ref_day)


def _build_customer_update(order_id):
    """Draft a markdown customer notification."""
    o = ORDERS[order_id]
    lines = []
    lines.append(f"**Subject:** Order {order_id} Status Update -- {o['product']}")
    lines.append(f"\nDear {o['contact_name']},\n")

    if order_id in DELAY_REASONS:
        d = DELAY_REASONS[order_id]
        lines.append(f"We are writing to inform you of a revised delivery date for your order.")
        lines.append(f"\n- **Original date:** {d['original_date']}")
        lines.append(f"- **Revised date:** {d['revised_date']}")
        lines.append(f"- **Reason:** {d['reason']}")
        lines.append("\n**Recovery actions underway:**")
        for action in d["recovery_actions"]:
            lines.append(f"- {action}")
    elif o["status"] == "shipped":
        sh = SHIPMENTS.get(order_id, {})
        lines.append(f"Your order has shipped and is on its way.")
        lines.append(f"\n- **Carrier:** {sh.get('carrier', 'TBD')}")
        lines.append(f"- **Tracking:** {sh.get('tracking_number', 'TBD')}")
        lines.append(f"- **Est. delivery:** {sh.get('est_delivery', 'TBD')}")
    else:
        lines.append(f"Your order is progressing on schedule.")
        lines.append(f"\n- **Completion:** {o['pct_complete']}%")
        lines.append(f"- **Promised delivery:** {o['promised_date']}")

    lines.append("\nPlease do not hesitate to reach out with any questions.")
    lines.append(f"\nBest regards,")
    am = CUSTOMER_CONTACTS.get(o["customer"], {}).get("account_manager", "Account Team")
    lines.append(f"{am}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class OrderStatusCommunicationAgent(BasicAgent):
    """Tracks orders and generates proactive customer communications."""

    def __init__(self):
        self.name = "OrderStatusCommunicationAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "operations": [
                "order_lookup",
                "shipment_tracking",
                "delay_notification",
                "customer_update",
                "recovery_plan",
                "engagement_execution",
                "quality_validation",
                "performance_review",
            ],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "description": "Operation to perform. Defaults to order_lookup when omitted.",
                        "enum": [
                            "order_lookup",
                            "shipment_tracking",
                            "delay_notification",
                            "customer_update",
                            "recovery_plan",
                            "engagement_execution",
                            "quality_validation",
                            "performance_review",
                        ],
                    },
                    "order_id": {
                        "type": "string",
                        "description": "Order identifier used to select recovery, engagement, quality, and performance records.",
                    },
                },
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "order_lookup")
        dispatch = {
            "order_lookup": self._order_lookup,
            "shipment_tracking": self._shipment_tracking,
            "delay_notification": self._delay_notification,
            "customer_update": self._customer_update,
            "recovery_plan": self._recovery_plan,
            "engagement_execution": self._engagement_execution,
            "quality_validation": self._quality_validation,
            "performance_review": self._performance_review,
        }
        handler = dispatch.get(operation)
        if handler is None:
            return f"**Error:** Unknown operation `{operation}`. Valid: {', '.join(dispatch.keys())}"
        return handler(**kwargs)

    # ------------------------------------------------------------------
    def _order_lookup(self, **kwargs) -> str:
        lines = ["## Order Status Dashboard\n"]
        lines.append("| Order | Customer | Product | Qty | Value | Status | Complete | Promise Date | Days Left |")
        lines.append("|-------|----------|---------|-----|-------|--------|----------|--------------|-----------|")
        for oid, o in ORDERS.items():
            val = _order_value(oid)
            dl = _days_until_promise(oid)
            risk_flag = " **DELAYED**" if _is_at_risk(oid) else ""
            lines.append(
                f"| {oid} | {o['customer']} | {o['product'][:28]} | {o['quantity']:,} | "
                f"${val:,.2f} | {o['status']}{risk_flag} | {o['pct_complete']}% | {o['promised_date']} | {dl} |"
            )
        total_val = sum(_order_value(oid) for oid in ORDERS)
        at_risk_val = sum(_order_value(oid) for oid in ORDERS if _is_at_risk(oid))
        lines.append(f"\n**Total order book value:** ${total_val:,.2f}")
        lines.append(f"**At-risk order value:** ${at_risk_val:,.2f}")
        live = _live_order_book()
        if live:
            seam = "n/a — enrichment seam"
            lines.append("\n### Live Tenant Order Book (Dynamics sales orders)\n")
            lines.append("| Order | Customer | Description | Value | Status | Promise Date | Fulfilled | Complete |")
            lines.append("|-------|----------|-------------|-------|--------|--------------|-----------|----------|")
            for o in live:
                pct = seam if o["pct_complete"] is None else f"{o['pct_complete']}%"
                lines.append(
                    f"| {o['id']} | {o['customer']} | {o['product'][:30]} | ${o['value']:,.2f} | "
                    f"{o['status']} | {o['promised_date']} | {o['fulfilled_date'] or 'not yet'} | {pct} |"
                )
            live_total = sum(o["value"] for o in live)
            lines.append(f"\n**Live tenant order book value:** ${live_total:,.2f}")
        else:
            lines.append("\n_Live tenant unreachable — showing embedded demo orders only._")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _shipment_tracking(self, **kwargs) -> str:
        lines = ["## Shipment Tracking\n"]
        if not SHIPMENTS:
            lines.append("No active shipments at this time.")
            return "\n".join(lines)

        lines.append("| Order | Carrier | Tracking | Ship Date | Est Delivery | Route | Weight | Status |")
        lines.append("|-------|---------|----------|-----------|-------------|-------|--------|--------|")
        for oid, sh in SHIPMENTS.items():
            route = f"{sh['origin']} -> {sh['destination']}"
            lines.append(
                f"| {oid} | {sh['carrier']} | {sh['tracking_number']} | {sh['ship_date']} | "
                f"{sh['est_delivery']} | {route} | {sh['weight_kg']:,} kg | {sh['status']} |"
            )

        lines.append("\n### Shipped Orders Detail\n")
        for oid in SHIPMENTS:
            o = ORDERS.get(oid, {})
            lines.append(f"- **{oid}** ({o.get('customer', 'N/A')}): {o.get('product', 'N/A')} -- "
                         f"{o.get('quantity', 0):,} units, ${_order_value(oid):,.2f}")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _delay_notification(self, **kwargs) -> str:
        lines = ["## Delay Notifications\n"]
        if not DELAY_REASONS:
            lines.append("No delays currently reported.")
            return "\n".join(lines)

        for oid, d in DELAY_REASONS.items():
            o = ORDERS[oid]
            cc = CUSTOMER_CONTACTS.get(o["customer"], {})
            lines.append(f"### {oid} -- {o['customer']}")
            lines.append(f"- **Product:** {o['product']}")
            lines.append(f"- **Quantity:** {o['quantity']:,} units (${_order_value(oid):,.2f})")
            lines.append(f"- **Delay:** {d['days_delayed']} days ({d['original_date']} -> {d['revised_date']})")
            lines.append(f"- **Reason:** {d['reason']}")
            lines.append(f"- **Cost impact:** ${d['cost_impact']:,.2f}")
            lines.append(f"- **Account manager:** {cc.get('account_manager', 'N/A')}")
            lines.append(f"- **SLA response window:** {cc.get('sla_response_hours', 'N/A')} hours")
            lines.append(f"- **Preferred channel:** {cc.get('preferred_channel', 'email')}")
            lines.append("\n**Recovery actions:**")
            for action in d["recovery_actions"]:
                lines.append(f"- {action}")
            lines.append("")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _customer_update(self, **kwargs) -> str:
        lines = ["## Customer Update Drafts\n"]
        lines.append("The following update messages have been prepared for all active orders:\n")
        for oid in ORDERS:
            lines.append(f"---\n### {oid} -- {ORDERS[oid]['customer']}\n")
            lines.append(_build_customer_update(oid))
            lines.append("")
        return "\n".join(lines)

    def _order_record(self, records, default_order_id, **kwargs):
        order_id = str(kwargs.get("order_id", default_order_id)).strip().upper()
        record = records.get(order_id)
        if record is None:
            return order_id, None, (
                f"**Error:** No record for order `{order_id}`. Valid: {', '.join(records)}"
            )
        return order_id, record, ""

    def _recovery_plan(self, **kwargs) -> str:
        order_id, plan, error = self._order_record(RECOVERY_PLANS, "ORD-7813", **kwargs)
        if error:
            return error
        order = ORDERS[order_id]
        lines = [
            "## Order Recovery Plan", EVIDENCE_MARKER,
            f"**Order lookup:** {order_id} — {order['customer']} / {order['product']}",
            f"- Root cause: {plan['root_cause']}",
            f"- Containment: {plan['containment']}",
            f"- Corrective action: {plan['corrective_action']}",
            f"- Owner: {plan['owner']}",
            f"- Next review: {plan['next_review']}",
            "- Revised delivery timeline:",
        ]
        lines.extend(f"  - {milestone}" for milestone in plan["revised_milestones"])
        return "\n".join(lines)

    def _engagement_execution(self, **kwargs) -> str:
        order_id = str(kwargs.get("order_id", "ORD-7813")).strip().upper()
        if order_id not in ORDERS:
            return f"**Error:** Unknown order `{order_id}`. Valid: {', '.join(ORDERS)}"
        order = ORDERS[order_id]
        contact = CUSTOMER_CONTACTS[order["customer"]]
        plan = RECOVERY_PLANS.get(order_id)
        delivery_date = _published_delivery_date(order_id)
        follow_up = plan["next_review"] if plan else order["promised_date"] + " 09:00"
        return "\n".join([
            "## Multichannel Engagement Execution",
            EVIDENCE_MARKER,
            f"**Order lookup:** {order_id} — {order['customer']}",
            f"- Preferred channel: {contact['preferred_channel']}",
            f"- Email draft: prepared for {order['contact_email']} with delivery date {delivery_date}",
            f"- EDI status: prepared with {order['status']} / {order['pct_complete']}% complete / delivery date {delivery_date}",
            f"- Portal update: prepared with delivery date {delivery_date}",
            f"- Follow-up scheduled: {follow_up}",
            f"- CRM note: recovery and customer-notification summary prepared with delivery date {delivery_date}",
            f"- **SIMULATED WRITE RECEIPT:** `ENG-SIM-{order_id}`",
            "- Simulation only; no email, EDI message, portal update, meeting, or CRM note was sent.",
        ])

    def _quality_validation(self, **kwargs) -> str:
        order_id, quality, error = self._order_record(
            QUALITY_VALIDATIONS, "ORD-7813", **kwargs
        )
        if error:
            return error
        return "\n".join([
            "## Order Quality Assurance Validation",
            EVIDENCE_MARKER,
            f"**Order lookup:** {order_id} — {ORDERS[order_id]['product']}",
            f"- Incoming material: {quality['incoming_material']}",
            f"- Production quality: {quality['production_quality']}",
            f"- Final validation: {quality['final_validation']}",
            f"- Release status: **{quality['quality_status']}**",
        ])

    def _performance_review(self, **kwargs) -> str:
        order_id, perf, error = self._order_record(
            PERFORMANCE_RECORDS, "ORD-7813", **kwargs
        )
        if error:
            return error
        return "\n".join([
            "## Recovery Performance Review",
            EVIDENCE_MARKER,
            f"**Order lookup:** {order_id} — {ORDERS[order_id]['customer']}",
            "",
            "| Measure | Before | Recovery Projection |",
            "|---------|--------|---------------------|",
            f"| On-time delivery | {perf['on_time_before_pct']}% | {perf['on_time_recovery_pct']}% |",
            f"| Quality PPM | {perf['quality_ppm_before']} | {perf['quality_ppm_recovery']} |",
            f"| Customer inquiries | {perf['customer_inquiries_before']} | {perf['customer_inquiries_after']} |",
            "",
            f"**Lesson learned:** {perf['lesson']}",
        ])


def _validate_delivery_date_contracts(agent):
    """Exercise delayed and non-delayed dates across customer and engagement views."""
    for case in DELIVERY_DATE_CONTRACT_CASES:
        order_id = case["order_id"]
        expected = case["expected"]
        assert _published_delivery_date(order_id) == expected
        assert expected in _build_customer_update(order_id)
        engagement = agent.perform(operation="engagement_execution", order_id=order_id)
        assert expected in engagement
        obsolete = case["obsolete"]
        if obsolete:
            assert obsolete not in engagement


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = OrderStatusCommunicationAgent()
    _validate_delivery_date_contracts(agent)
    print("=" * 72)
    print("EMBEDDED DEMO ORDERS + LIVE TENANT ORDER BOOK")
    print("(live section fetched over HTTP; falls back offline)")
    print("=" * 72)
    print(agent.perform(operation="order_lookup"))
    print()
    for op in agent.metadata["operations"][1:]:
        print("=" * 72)
        print(agent.perform(operation=op))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
