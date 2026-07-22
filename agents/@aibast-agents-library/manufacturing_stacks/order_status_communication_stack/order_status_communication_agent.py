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
