---
name: "rar-aibast-agents-library-supply-chain-disruption-alert"
description: "Flags disruptions from simulated Dynamics 365 cases plus ERP late deliveries and blocked invoices in one feed, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/supply_chain_disruption_alert", "rar_sha256": "ed9a780b446808d9b6ac20d38a8e67344a9ee30cd4067fa095feb5884def7484", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.3.0", "author": "AIBAST", "tags": ["supply-chain", "disruption", "risk-management", "logistics", "retail"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/supply_chain_disruption_alert`. The original RAPP
agent is preserved byte-for-byte in `supply_chain_disruption_alert_agent.py` and in the RCI capsule.

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

Supply Chain Disruption Alert Agent — a template you are meant to mutate.

Monitors supply chain routes for disruptions, assesses risk levels,
generates mitigation plans, and identifies alternative suppliers.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live disruption signals over real HTTP from
     TWO globally hosted simulated systems (synthetic data, no
     credentials, works from anywhere):
       CRM — Static Dynamics 365 tenant (Aster Lane Office Systems):
         https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       ERP — Static ERP (purchase orders, goods receipts, invoices):
         https://kody-w.github.io/static-erp/api/v1/
     Try: perform(operation="disruption_dashboard")
     — one output joins BOTH worlds: the tenant's live supply-chain
     cases such as CAS-260133 "Cold chain temperature excursion in
     produce section" (Harbor Lights Grocery) AND real inbound-supply
     exceptions computed from ERP documents — GR-88005 posted 9 days
     after PO-47005's expected delivery (Quarry Bend Foundry) and the
     payment-blocked invoice SINV-92003 on PO-47003. In this template a
     disruption signal is a Dynamics case or an ERP document exception.
  2. No network? Everything falls back to the embedded demo layer below
     (SUPPLY_ROUTES / DISRUPTION_EVENTS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SUPPLY_CHAIN_DISRUPTION_ALERT_DATA_URL (CRM side) and/or
     SUPPLY_CHAIN_DISRUPTION_ALERT_ERP_URL (ERP side) to any endpoint
     with the same shapes, or replace _fetch_collection() with your own
     logistics API. The fields the rest of the file needs are listed in
     _normalize_live_disruption() — revenue impact and affected routes
     stay "n/a — enrichment seam" until you wire your planning system.

OPERATIONS
  disruption_dashboard | risk_assessment | mitigation_plan |
  supplier_alternatives | disruption_impact | response_scenarios |
  response_execution | recovery_tracking | incident_report
  kwargs: operation (required), route_id, disruption_id, category, key,
  user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "category": {
      "type": "string"
    },
    "disruption_id": {
      "type": "string"
    },
    "key": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "disruption_dashboard",
        "risk_assessment",
        "mitigation_plan",
        "supplier_alternatives",
        "disruption_impact",
        "response_scenarios",
        "response_execution",
        "recovery_tracking",
        "incident_report"
      ],
      "type": "string"
    },
    "route_id": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `supply_chain_disruption_alert_agent.py` and embedded as the fenced Python below (sha256 ed9a780b446808d9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `supply_chain_disruption_alert_agent.py` first:

```bash
python3 supply_chain_disruption_alert_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 supply_chain_disruption_alert_agent.py   # or on stdin
python3 supply_chain_disruption_alert_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Supply Chain Disruption Alert Agent — a template you are meant to mutate.

Monitors supply chain routes for disruptions, assesses risk levels,
generates mitigation plans, and identifies alternative suppliers.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live disruption signals over real HTTP from
     TWO globally hosted simulated systems (synthetic data, no
     credentials, works from anywhere):
       CRM — Static Dynamics 365 tenant (Aster Lane Office Systems):
         https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       ERP — Static ERP (purchase orders, goods receipts, invoices):
         https://kody-w.github.io/static-erp/api/v1/
     Try: perform(operation="disruption_dashboard")
     — one output joins BOTH worlds: the tenant's live supply-chain
     cases such as CAS-260133 "Cold chain temperature excursion in
     produce section" (Harbor Lights Grocery) AND real inbound-supply
     exceptions computed from ERP documents — GR-88005 posted 9 days
     after PO-47005's expected delivery (Quarry Bend Foundry) and the
     payment-blocked invoice SINV-92003 on PO-47003. In this template a
     disruption signal is a Dynamics case or an ERP document exception.
  2. No network? Everything falls back to the embedded demo layer below
     (SUPPLY_ROUTES / DISRUPTION_EVENTS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SUPPLY_CHAIN_DISRUPTION_ALERT_DATA_URL (CRM side) and/or
     SUPPLY_CHAIN_DISRUPTION_ALERT_ERP_URL (ERP side) to any endpoint
     with the same shapes, or replace _fetch_collection() with your own
     logistics API. The fields the rest of the file needs are listed in
     _normalize_live_disruption() — revenue impact and affected routes
     stay "n/a — enrichment seam" until you wire your planning system.

OPERATIONS
  disruption_dashboard | risk_assessment | mitigation_plan |
  supplier_alternatives | disruption_impact | response_scenarios |
  response_execution | recovery_tracking | incident_report
  kwargs: operation (required), route_id, disruption_id, category, key,
  user_input
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
from datetime import datetime, timezone

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/supply_chain_disruption_alert",
    "version": "1.3.0",
    "display_name": "Supply Chain Disruption Alert Agent",
    "description": (
        "Flags disruptions from simulated Dynamics 365 cases plus ERP late deliveries and blocked invoices in one feed, with an offline demo fallback."
    ),
    "author": "AIBAST",
    "tags": [
        "supply-chain",
        "disruption",
        "risk-management",
        "logistics",
        "retail",
    ],
    "category": "retail_cpg",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# ═══════════════════════════════════════════════════════════════
# LIVE DATA SEAM — swap this for your real systems
#
# Defaults: TWO globally hosted simulated systems (synthetic data
# served as JSON from GitHub Pages). To hook your own world, either:
#   export SUPPLY_CHAIN_DISRUPTION_ALERT_DATA_URL=https://your-org/api/data/v9.2
#   export SUPPLY_CHAIN_DISRUPTION_ALERT_ERP_URL=https://your-erp/api/v1
# or replace _fetch_collection() with your TMS/visibility client.
# Downstream code only needs the fields from _normalize_live_disruption()
# and _erp_inbound_exceptions().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "SUPPLY_CHAIN_DISRUPTION_ALERT_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
ERP_SOURCE_URL = os.environ.get(
    "SUPPLY_CHAIN_DISRUPTION_ALERT_ERP_URL",
    "https://kody-w.github.io/static-erp/api/v1",
)
_LIVE_CACHE = {}

# Case-title keywords that mark a tenant case as a supply-chain signal.
_DISRUPTION_KEYWORDS = (
    "shipment", "freight", "cold chain", "backorder", "delivery",
    "delayed", "downtime", "tracking",
)


def _fetch_collection(collection, timeout=6, base_url=None):
    """One bounded GET per collection per source per process. Returns []
    on ANY failure — offline, DNS, bad JSON — so the demo layer takes
    over. Cache is keyed by full URL so CRM and ERP never collide."""
    url = f"{base_url or DATA_SOURCE_URL}/{collection}.json"
    if url in _LIVE_CACHE:
        return _LIVE_CACHE[url]
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "rapp-agent-template/1.0"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            rows = json.loads(resp.read().decode("utf-8")).get("value", [])
    except Exception:
        rows = []
    _LIVE_CACHE[url] = rows
    return rows


def _erp(collection):
    """Rows from the live simulated ERP (purchase_orders, goods_receipts,
    supplier_invoices, suppliers, materials); [] offline."""
    return _fetch_collection(collection, base_url=ERP_SOURCE_URL)


def _erp_inbound_exceptions():
    """REAL inbound-supply exceptions joined from live ERP documents:
    goods receipts posted after the PO's expected delivery date, and
    payment-blocked supplier invoices (with the received-vs-invoiced
    quantity break behind them). [] when the ERP is unreachable."""
    pos = _erp("purchase_orders")
    if not pos:
        return []
    grs = _erp("goods_receipts")
    invs = _erp("supplier_invoices")
    by_po = {p.get("po_number"): p for p in pos}
    events = []
    for g in grs:
        po = by_po.get(g.get("po_number"))
        if not po:
            continue
        expected = str(po.get("expected_delivery_date", ""))[:10]
        posted = str(g.get("posting_date", ""))[:10]
        if expected and posted > expected:
            try:
                days = (
                    datetime.fromisoformat(posted) - datetime.fromisoformat(expected)
                ).days
            except ValueError:
                days = 0
            events.append({
                "type": "LATE DELIVERY",
                "document": g.get("receipt_number", "?"),
                "po_number": g.get("po_number", "?"),
                "supplier": g.get("supplier_name", "?"),
                "detail": (
                    f"posted {posted}, {days} days after expected {expected}"
                ),
            })
    for i in invs:
        if not i.get("payment_block"):
            continue
        po = by_po.get(i.get("po_number"))
        received = {}
        for g in grs:
            if g.get("po_number") != i.get("po_number"):
                continue
            for l in g.get("lines", []):
                m = l.get("material_number", "?")
                received[m] = received.get(m, 0) + int(float(l.get("quantity_received") or 0))
        breaks = []
        for l in i.get("lines", []):
            m = l.get("material_number", "?")
            qty_inv = int(float(l.get("quantity_invoiced") or 0))
            if received and received.get(m, 0) != qty_inv:
                breaks.append(f"{m} received {received.get(m, 0)} vs invoiced {qty_inv}")
        events.append({
            "type": "BLOCKED INVOICE",
            "document": i.get("invoice_number", "?"),
            "po_number": i.get("po_number", "?"),
            "supplier": i.get("supplier_name", "?"),
            "detail": (
                f"${float(i.get('total_amount') or 0):,.2f} payment-blocked"
                + (f"; {'; '.join(breaks)}" if breaks else "")
            ),
        })
    return events


def _normalize_live_disruption(row):
    """Project a Dynamics case (incident) record onto the shape this agent
    uses — in this template a supply-chain disruption signal IS a Dynamics
    case. THIS is the contract your replacement data source must meet — a
    dict with these keys. None means 'not available from the service desk
    alone' and the renderers label it as an enrichment seam."""
    return {
        "event_id": row.get("ticketnumber", row.get("incidentid", "")),
        "title": row.get("title", "untitled"),
        "customer": row.get("customeridname", "Unknown"),
        "severity": row.get(
            "prioritycode@OData.Community.Display.V1.FormattedValue", "Normal"
        ),
        "status": row.get(
            "statecode@OData.Community.Display.V1.FormattedValue", "Active"
        ),
        "open": row.get("statecode") == 0,
        "age_days": _age_days(row.get("createdon")),
        "revenue_impact": None,   # enrichment seam — wire your planning system
        "affected_routes": None,  # enrichment seam — wire your TMS
        "_live": True,
    }


def _age_days(iso_date):
    try:
        then = datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
        return max(0, (datetime.now(timezone.utc) - then).days)
    except (ValueError, TypeError):
        return 0


def _live_disruption_signals():
    """Live tenant cases whose titles look supply-chain-shaped; [] offline."""
    signals = []
    for row in _fetch_collection("incidents"):
        title = str(row.get("title", "")).lower()
        if any(kw in title for kw in _DISRUPTION_KEYWORDS):
            signal = _normalize_live_disruption(row)
            if signal["event_id"]:
                signals.append(signal)
    return signals


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback) — Supply Chain Network
# ---------------------------------------------------------------------------

SUPPLY_ROUTES = {
    "RT-APAC-01": {
        "name": "Asia-Pacific Primary",
        "origin": "Shenzhen, China",
        "destination": "Los Angeles, CA",
        "transport_mode": "ocean_freight",
        "transit_days": 18,
        "carriers": ["COSCO Shipping", "Evergreen Marine"],
        "annual_volume_teu": 4800,
        "annual_value_usd": 28500000.00,
        "categories": ["Electronics", "Accessories"],
        "current_status": "disrupted",
        "reliability_score": 0.82,
    },
    "RT-EURO-01": {
        "name": "European Apparel Route",
        "origin": "Porto, Portugal",
        "destination": "Newark, NJ",
        "transport_mode": "ocean_freight",
        "transit_days": 12,
        "carriers": ["Maersk Line", "MSC"],
        "annual_volume_teu": 2200,
        "annual_value_usd": 15800000.00,
        "categories": ["Apparel"],
        "current_status": "at_risk",
        "reliability_score": 0.91,
    },
    "RT-DOMESTIC-01": {
        "name": "West Coast to Midwest",
        "origin": "Los Angeles, CA",
        "destination": "Chicago, IL",
        "transport_mode": "intermodal_rail",
        "transit_days": 4,
        "carriers": ["Union Pacific", "BNSF Railway"],
        "annual_volume_teu": 6500,
        "annual_value_usd": 42000000.00,
        "categories": ["Electronics", "Accessories", "Apparel", "Footwear"],
        "current_status": "normal",
        "reliability_score": 0.95,
    },
    "RT-LATAM-01": {
        "name": "Central America Footwear",
        "origin": "Leon, Mexico",
        "destination": "Dallas, TX",
        "transport_mode": "trucking",
        "transit_days": 3,
        "carriers": ["J.B. Hunt", "Werner Enterprises"],
        "annual_volume_teu": 1800,
        "annual_value_usd": 12400000.00,
        "categories": ["Footwear"],
        "current_status": "normal",
        "reliability_score": 0.93,
    },
    "RT-SEASIA-01": {
        "name": "Southeast Asia Textiles",
        "origin": "Ho Chi Minh City, Vietnam",
        "destination": "Savannah, GA",
        "transport_mode": "ocean_freight",
        "transit_days": 22,
        "carriers": ["Yang Ming", "ONE Line"],
        "annual_volume_teu": 3100,
        "annual_value_usd": 19200000.00,
        "categories": ["Apparel", "Home"],
        "current_status": "disrupted",
        "reliability_score": 0.78,
    },
}

DISRUPTION_EVENTS = {
    "DISR-001": {
        "title": "Port Congestion — Los Angeles/Long Beach",
        "type": "port_congestion",
        "severity": "high",
        "affected_routes": ["RT-APAC-01"],
        "start_date": "2026-03-05",
        "estimated_resolution": "2026-03-28",
        "delay_days": 8,
        "affected_skus": ["SKU-1002", "SKU-1004", "SKU-1006", "SKU-1008"],
        "estimated_revenue_impact": 2150000.00,
        "description": (
            "Severe vessel queue at LA/LB ports due to labor slowdown and "
            "equipment shortages. Average vessel wait time is 6 days."
        ),
        "status": "active",
    },
    "DISR-002": {
        "title": "Typhoon Disruption — South China Sea",
        "type": "weather_event",
        "severity": "critical",
        "affected_routes": ["RT-APAC-01", "RT-SEASIA-01"],
        "start_date": "2026-03-10",
        "estimated_resolution": "2026-03-20",
        "delay_days": 12,
        "affected_skus": ["SKU-1002", "SKU-1003", "SKU-1004", "SKU-1006", "SKU-1008", "SKU-1010"],
        "estimated_revenue_impact": 3800000.00,
        "description": (
            "Typhoon Mirinae forcing rerouting of vessels through northern "
            "Pacific corridor. Multiple sailings cancelled or delayed."
        ),
        "status": "active",
    },
    "DISR-003": {
        "title": "EU Customs Regulation Change",
        "type": "regulatory",
        "severity": "medium",
        "affected_routes": ["RT-EURO-01"],
        "start_date": "2026-03-01",
        "estimated_resolution": "2026-04-15",
        "delay_days": 5,
        "affected_skus": ["SKU-1001", "SKU-1003"],
        "estimated_revenue_impact": 720000.00,
        "description": (
            "New EU sustainability documentation requirements adding processing "
            "time at origin. Additional compliance certificates needed for textiles."
        ),
        "status": "active",
    },
}

RISK_SCORES = {
    "RT-APAC-01": {
        "overall_risk": 0.78,
        "geopolitical": 0.65,
        "weather": 0.82,
        "infrastructure": 0.70,
        "labor": 0.75,
        "regulatory": 0.40,
        "financial": 0.35,
    },
    "RT-EURO-01": {
        "overall_risk": 0.45,
        "geopolitical": 0.30,
        "weather": 0.20,
        "infrastructure": 0.25,
        "labor": 0.35,
        "regulatory": 0.72,
        "financial": 0.28,
    },
    "RT-DOMESTIC-01": {
        "overall_risk": 0.22,
        "geopolitical": 0.05,
        "weather": 0.30,
        "infrastructure": 0.20,
        "labor": 0.25,
        "regulatory": 0.10,
        "financial": 0.15,
    },
    "RT-LATAM-01": {
        "overall_risk": 0.35,
        "geopolitical": 0.25,
        "weather": 0.15,
        "infrastructure": 0.40,
        "labor": 0.30,
        "regulatory": 0.45,
        "financial": 0.32,
    },
    "RT-SEASIA-01": {
        "overall_risk": 0.72,
        "geopolitical": 0.50,
        "weather": 0.85,
        "infrastructure": 0.55,
        "labor": 0.40,
        "regulatory": 0.48,
        "financial": 0.30,
    },
}

MITIGATION_PLAYBOOKS = {
    "port_congestion": {
        "label": "Port Congestion Mitigation",
        "immediate_actions": [
            "Divert eligible shipments to alternate ports (Oakland, Seattle-Tacoma)",
            "Activate premium drayage contracts for priority container retrieval",
            "Convert ocean shipments under 2 TEU to air freight for critical SKUs",
        ],
        "short_term_actions": [
            "Increase safety stock at distribution centers by 20%",
            "Negotiate priority berthing with carrier partners",
            "Activate cross-dock bypass for pre-cleared containers",
        ],
        "long_term_actions": [
            "Diversify port-of-entry strategy across West and East Coast",
            "Invest in inland port relationships for rail-direct receiving",
            "Develop dual-source contracts for top-volume categories",
        ],
        "estimated_mitigation_cost": 340000.00,
        "risk_reduction_pct": 45,
    },
    "weather_event": {
        "label": "Weather Event Mitigation",
        "immediate_actions": [
            "Activate emergency inventory reserves at regional warehouses",
            "Reroute in-transit vessels through safe corridors",
            "Expedite air freight for high-priority SKUs with less than 7 days supply",
        ],
        "short_term_actions": [
            "Shift demand to in-stock alternative products via merchandising",
            "Enable backorder with guaranteed delivery dates for affected items",
            "Communicate proactively with B2B customers on revised timelines",
        ],
        "long_term_actions": [
            "Integrate real-time weather monitoring into planning systems",
            "Build seasonal safety stock buffers for typhoon/hurricane seasons",
            "Qualify backup suppliers in geographically diverse regions",
        ],
        "estimated_mitigation_cost": 520000.00,
        "risk_reduction_pct": 55,
    },
    "regulatory": {
        "label": "Regulatory Change Mitigation",
        "immediate_actions": [
            "Engage customs broker to prepare updated documentation templates",
            "Pre-certify next 3 shipments with new compliance requirements",
            "Brief all origin-side partners on updated export procedures",
        ],
        "short_term_actions": [
            "Conduct compliance audit of all active POs on affected routes",
            "Update vendor manual with new regulatory requirements",
            "Schedule training session for procurement team",
        ],
        "long_term_actions": [
            "Subscribe to regulatory change monitoring service",
            "Build compliance buffer time into standard lead times",
            "Develop relationships with in-country compliance consultants",
        ],
        "estimated_mitigation_cost": 85000.00,
        "risk_reduction_pct": 70,
    },
}

ALTERNATIVE_SUPPLIERS = {
    "Electronics": [
        {
            "name": "TechSource Taiwan",
            "location": "Taipei, Taiwan",
            "lead_time_days": 21,
            "quality_rating": 4.5,
            "capacity_units_monthly": 15000,
            "price_premium_pct": 8.0,
            "certifications": ["ISO 9001", "ISO 14001"],
            "min_order_qty": 500,
        },
        {
            "name": "KoreanTech Partners",
            "location": "Incheon, South Korea",
            "lead_time_days": 19,
            "quality_rating": 4.7,
            "capacity_units_monthly": 10000,
            "price_premium_pct": 12.0,
            "certifications": ["ISO 9001", "IATF 16949"],
            "min_order_qty": 300,
        },
    ],
    "Apparel": [
        {
            "name": "TurkTex Industries",
            "location": "Istanbul, Turkey",
            "lead_time_days": 16,
            "quality_rating": 4.3,
            "capacity_units_monthly": 25000,
            "price_premium_pct": 5.0,
            "certifications": ["GOTS", "OEKO-TEX"],
            "min_order_qty": 1000,
        },
        {
            "name": "BanglaStitch Ltd",
            "location": "Dhaka, Bangladesh",
            "lead_time_days": 25,
            "quality_rating": 4.0,
            "capacity_units_monthly": 40000,
            "price_premium_pct": -3.0,
            "certifications": ["WRAP", "BSCI"],
            "min_order_qty": 2000,
        },
    ],
    "Footwear": [
        {
            "name": "IndoSole Manufacturing",
            "location": "Tangerang, Indonesia",
            "lead_time_days": 28,
            "quality_rating": 4.2,
            "capacity_units_monthly": 18000,
            "price_premium_pct": 2.0,
            "certifications": ["ISO 9001", "SA8000"],
            "min_order_qty": 800,
        },
    ],
    "Accessories": [
        {
            "name": "IndiaGlobal Accessories",
            "location": "Mumbai, India",
            "lead_time_days": 24,
            "quality_rating": 4.1,
            "capacity_units_monthly": 30000,
            "price_premium_pct": -5.0,
            "certifications": ["ISO 9001"],
            "min_order_qty": 1500,
        },
        {
            "name": "MediterraneanCraft Co",
            "location": "Florence, Italy",
            "lead_time_days": 14,
            "quality_rating": 4.8,
            "capacity_units_monthly": 5000,
            "price_premium_pct": 25.0,
            "certifications": ["ISO 9001", "Made in Italy"],
            "min_order_qty": 200,
        },
    ],
    "Home": [
        {
            "name": "ThaiHome Products",
            "location": "Bangkok, Thailand",
            "lead_time_days": 20,
            "quality_rating": 4.3,
            "capacity_units_monthly": 12000,
            "price_premium_pct": 4.0,
            "certifications": ["ISO 9001", "FSC"],
            "min_order_qty": 600,
        },
    ],
}

EVIDENCE_CAPABILITIES = {
    "disruption_impact": {
        "title": "Disruption Root Cause and Impact",
        "source_system": "Dynamics 365 Supply Chain Management",
        "write": False,
        "key_field": "incident_id",
        "summary": (
            "Connects a detected disruption to root cause, severity, affected "
            "stores, SKUs, revenue, and customer impact."
        ),
        "record": {
            "incident_id": "INC-PORTLAND-DC",
            "root_cause": "Portland distribution-center conveyor failure causing a 3-day backlog",
            "scope": "12 Northwest stores; 143 products; Seattle Flagship at 47% stockout",
            "category_impact": "Electronics 42 SKUs; apparel 38; home goods 31; sporting 32",
            "revenue_exposure": "$84,300 per week and escalating",
            "customer_impact": "37 complaints, 280% above baseline, with social mentions rising",
            "severity": "Critical; immediate management decision required",
        },
    },
    "response_scenarios": {
        "title": "Emergency Response Scenarios",
        "source_system": "Dynamics 365 Supply Chain Management",
        "write": False,
        "key_field": "scenario_id",
        "summary": (
            "Compares response timelines, fulfillment coverage, cost, revenue "
            "recovery, and ROI before making a recommendation."
        ),
        "record": {
            "scenario_id": "SCENARIO-DENVER-TRANSFER",
            "option_a": "Denver DC transfer; 36 hours; 80 priority SKUs; $15,600 cost; $47,000 recovery; 3:1 ROI",
            "option_b": "Wait for Portland; 2 days; 40% restored; $0 response cost; $127,000 additional loss",
            "expansion": "Add five high-impact stores for $8,900, bringing total response investment to $24,500",
            "recommendation": "Execute Denver transfer and five-store expansion to protect $78,000 revenue",
        },
    },
    "response_execution": {
        "title": "Emergency Response Execution",
        "source_system": "Dynamics 365 Supply Chain Management and Microsoft Teams",
        "write": True,
        "key_field": "execution_id",
        "summary": (
            "Prepares transfer, receiving, restocking, and notification actions "
            "without triggering connected operations systems."
        ),
        "record": {
            "execution_id": "EXEC-DENVER-NORTHWEST",
            "seattle": "80 priority electronics SKUs; simulated departure 18:00; simulated arrival Friday 10:00",
            "additional_stores": "Portland South, Tacoma Mall, Bellevue Square, Olympia Center, Spokane Valley; 60 SKUs each",
            "coordination": "Store notifications, receiving staff, tablet restocking plans, and customer SMS prepared",
            "economics": "$24,500 response investment; $78,000 projected recovery",
            "execution_note": "Simulation only; no freight, workflow, staffing, or notification action occurs",
        },
    },
    "recovery_tracking": {
        "title": "Shipment Tracking and Recovery Plan",
        "source_system": "Dynamics 365 Supply Chain Management",
        "write": False,
        "key_field": "tracking_id",
        "summary": (
            "Provides deterministic shipment status, recovery milestones, "
            "backlog clearance, and prevention recommendations."
        ),
        "record": {
            "tracking_id": "TRACK-DENVER-PORTLAND",
            "shipment": "Denver truck departed 18:04; Seattle ETA Friday 09:47; on schedule",
            "repair": "Conveyor repair Thursday 20:00; backlog processing Friday 06:00; normal operations Friday noon",
            "backlog": "340 pending orders; Seattle and affected stores first; full clearance Saturday end of day",
            "prevention": "$145,000 backup conveyor; 48-hour installation; $340,000 three-year avoided-loss value",
        },
    },
    "incident_report": {
        "title": "Incident Report and Leadership Distribution",
        "source_system": "Microsoft Teams",
        "write": True,
        "key_field": "report_id",
        "summary": (
            "Builds a financial and operational incident report with a "
            "simulated leadership distribution receipt."
        ),
        "record": {
            "report_id": "REPORT-PORTLAND-DC",
            "financial_impact": "$84,300 at risk; $24,500 response cost; $78,000 recovered; $53,500 net value protected",
            "performance": "47 minutes detection-to-action; 36-hour alternate DC activation; 95% inventory in 3 days",
            "lessons": "Backup conveyor, multi-DC sourcing rules, and monitoring tuned to reduce response by 18 minutes",
            "prevention_value": "$340,000 avoided losses over three years versus $145,000 investment",
            "distribution": "Prepared for executive team review in Microsoft Teams",
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

def _total_revenue_at_risk():
    return sum(d["estimated_revenue_impact"] for d in DISRUPTION_EVENTS.values() if d["status"] == "active")


def _affected_route_count():
    affected = set()
    for d in DISRUPTION_EVENTS.values():
        if d["status"] == "active":
            affected.update(d["affected_routes"])
    return len(affected)


def _risk_level_label(score):
    if score >= 0.70:
        return "HIGH"
    if score >= 0.40:
        return "MEDIUM"
    return "LOW"


def _total_mitigation_cost():
    seen_types = set()
    total = 0.0
    for d in DISRUPTION_EVENTS.values():
        if d["status"] == "active" and d["type"] not in seen_types:
            pb = MITIGATION_PLAYBOOKS.get(d["type"], {})
            total += pb.get("estimated_mitigation_cost", 0)
            seen_types.add(d["type"])
    return total


def _best_alternative(category):
    alts = ALTERNATIVE_SUPPLIERS.get(category, [])
    if not alts:
        return None
    return min(alts, key=lambda a: a["lead_time_days"])


# ---------------------------------------------------------------------------
# Agent Class
# ---------------------------------------------------------------------------

class SupplyChainDisruptionAlertAgent(BasicAgent):
    """Agent for supply chain disruption monitoring and mitigation."""

    def __init__(self):
        self.name = "supply-chain-disruption-alert-agent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "disruption_dashboard",
                            "risk_assessment",
                            "mitigation_plan",
                            "supplier_alternatives",
                            "disruption_impact",
                            "response_scenarios",
                            "response_execution",
                            "recovery_tracking",
                            "incident_report",
                        ],
                    },
                    "route_id": {"type": "string"},
                    "disruption_id": {"type": "string"},
                    "category": {"type": "string"},
                    "key": {"type": "string"},
                    "user_input": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def _live_disruption_dashboard(self, signals):
        """Disruption feed built from live tenant cases (preferred online)."""
        open_signals = [s for s in signals if s["open"]]
        lines = [
            "# Supply Chain Disruption Dashboard — Live Tenant Signals",
            "",
            f"Live records from {DATA_SOURCE_URL} (Aster Lane Office Systems).",
            "In this template a disruption signal is a Dynamics case. Pass",
            "`route_id` or `disruption_id` for the embedded demo network view.",
            "",
            "| Case | Event | Customer | Severity | Status | Age | Revenue Impact |",
            "|------|-------|----------|----------|--------|-----|----------------|",
        ]
        for s in sorted(signals, key=lambda x: x["event_id"]):
            impact = (
                "n/a — enrichment seam"
                if s["revenue_impact"] is None
                else f"${s['revenue_impact']:,.2f}"
            )
            lines.append(
                f"| {s['event_id']} | {s['title']} | {s['customer']} "
                f"| {s['severity']} | {s['status']} | {s['age_days']}d | {impact} |"
            )
        high = sum(1 for s in open_signals if s["severity"] == "High")
        lines.append("")
        lines.append(
            f"**Active signals:** {len(open_signals)} open of {len(signals)} matched "
            f"| **High severity:** {high}"
        )
        exceptions = _erp_inbound_exceptions()
        if exceptions:
            lines.append("")
            lines.append("## Inbound Supply Exceptions — Live ERP (POs vs receipts vs invoices)")
            lines.append("")
            lines.append("| Type | Document | PO | Supplier | Detail |")
            lines.append("|------|----------|----|----------|--------|")
            for e in exceptions:
                lines.append(
                    f"| **{e['type']}** | {e['document']} | {e['po_number']} "
                    f"| {e['supplier']} | {e['detail']} |"
                )
            lines.append("")
            lines.append(
                f"**ERP exceptions:** {len(exceptions)} computed from real document "
                "joins in the live simulated ERP — one feed with the CRM cases above."
            )
        else:
            lines.append("")
            lines.append("_Simulated ERP unreachable — inbound document exceptions unavailable._")
        lines.append(
            "Affected routes and revenue impact need your TMS/planning system — "
            "wire it at the LIVE DATA SEAM."
        )
        return "\n".join(lines)

    def _disruption_dashboard(self, **kwargs):
        if not kwargs.get("route_id") and not kwargs.get("disruption_id"):
            signals = _live_disruption_signals()
            if signals:
                return self._live_disruption_dashboard(signals)
        rev_at_risk = _total_revenue_at_risk()
        routes_affected = _affected_route_count()
        lines = [
            "# Supply Chain Disruption Dashboard",
            "",
            f"**Active Disruptions:** {len([d for d in DISRUPTION_EVENTS.values() if d['status'] == 'active'])}",
            f"**Routes Affected:** {routes_affected} of {len(SUPPLY_ROUTES)}",
            f"**Total Revenue at Risk:** ${rev_at_risk:,.2f}",
            "",
            "## Active Disruption Events",
            "",
            "| ID | Title | Type | Severity | Delay | Revenue Impact | Resolution ETA |",
            "|----|-------|------|----------|-------|----------------|----------------|",
        ]
        for did, d in DISRUPTION_EVENTS.items():
            if d["status"] == "active":
                lines.append(
                    f"| {did} | {d['title']} | {d['type'].replace('_', ' ')} "
                    f"| {d['severity'].upper()} | +{d['delay_days']}d "
                    f"| ${d['estimated_revenue_impact']:,.2f} | {d['estimated_resolution']} |"
                )
        lines.append("")
        lines.append("## Route Status Overview")
        lines.append("")
        lines.append("| Route | Origin | Destination | Mode | Status | Reliability |")
        lines.append("|-------|--------|-------------|------|--------|-------------|")
        for rid, route in SUPPLY_ROUTES.items():
            status_display = route["current_status"].upper().replace("_", " ")
            lines.append(
                f"| {route['name']} | {route['origin']} | {route['destination']} "
                f"| {route['transport_mode'].replace('_', ' ')} "
                f"| {status_display} | {route['reliability_score']*100:.0f}% |"
            )
        lines.append("")
        for did, d in DISRUPTION_EVENTS.items():
            if d["status"] == "active":
                lines.append(f"### {did}: {d['title']}")
                lines.append("")
                lines.append(f"{d['description']}")
                lines.append("")
                lines.append(f"**Affected SKUs:** {', '.join(d['affected_skus'])}")
                lines.append(f"**Affected Routes:** {', '.join(d['affected_routes'])}")
                lines.append("")
        return "\n".join(lines)

    def _risk_assessment(self, **kwargs):
        route_id = kwargs.get("route_id")
        if route_id and route_id in RISK_SCORES:
            routes = {route_id: RISK_SCORES[route_id]}
        else:
            routes = RISK_SCORES
        lines = [
            "# Supply Chain Risk Assessment",
            "",
            "## Risk Score Matrix",
            "",
            "| Route | Overall | Geopolitical | Weather | Infrastructure | Labor | Regulatory | Financial |",
            "|-------|---------|--------------|---------|----------------|-------|------------|-----------|",
        ]
        for rid, scores in routes.items():
            route_name = SUPPLY_ROUTES.get(rid, {}).get("name", rid)
            level = _risk_level_label(scores["overall_risk"])
            lines.append(
                f"| {route_name} | **{scores['overall_risk']:.2f}** ({level}) "
                f"| {scores['geopolitical']:.2f} | {scores['weather']:.2f} "
                f"| {scores['infrastructure']:.2f} | {scores['labor']:.2f} "
                f"| {scores['regulatory']:.2f} | {scores['financial']:.2f} |"
            )
        lines.append("")
        lines.append("## Risk Level Distribution")
        lines.append("")
        high = sum(1 for s in RISK_SCORES.values() if s["overall_risk"] >= 0.70)
        med = sum(1 for s in RISK_SCORES.values() if 0.40 <= s["overall_risk"] < 0.70)
        low = sum(1 for s in RISK_SCORES.values() if s["overall_risk"] < 0.40)
        lines.append(f"- **HIGH risk routes:** {high}")
        lines.append(f"- **MEDIUM risk routes:** {med}")
        lines.append(f"- **LOW risk routes:** {low}")
        lines.append("")
        lines.append("## Highest Risk Factors")
        lines.append("")
        all_factors = {}
        for scores in RISK_SCORES.values():
            for factor in ["geopolitical", "weather", "infrastructure", "labor", "regulatory", "financial"]:
                all_factors.setdefault(factor, []).append(scores[factor])
        for factor, values in sorted(all_factors.items(), key=lambda x: -max(x[1])):
            avg_score = sum(values) / len(values)
            peak = max(values)
            lines.append(f"- **{factor.title()}:** avg {avg_score:.2f}, peak {peak:.2f}")
        return "\n".join(lines)

    def _mitigation_plan(self, **kwargs):
        disruption_id = kwargs.get("disruption_id")
        if disruption_id and disruption_id in DISRUPTION_EVENTS:
            events = {disruption_id: DISRUPTION_EVENTS[disruption_id]}
        else:
            events = {k: v for k, v in DISRUPTION_EVENTS.items() if v["status"] == "active"}
        total_cost = _total_mitigation_cost()
        lines = [
            "# Disruption Mitigation Plan",
            "",
            f"**Estimated Total Mitigation Investment:** ${total_cost:,.2f}",
            "",
        ]
        for did, event in events.items():
            playbook = MITIGATION_PLAYBOOKS.get(event["type"], {})
            if not playbook:
                continue
            lines.append(f"## {did}: {event['title']}")
            lines.append(f"**Playbook:** {playbook['label']}")
            lines.append(f"**Expected Risk Reduction:** {playbook['risk_reduction_pct']}%")
            lines.append(f"**Mitigation Cost:** ${playbook['estimated_mitigation_cost']:,.2f}")
            lines.append("")
            lines.append("### Immediate Actions (0-48 hours)")
            for action in playbook["immediate_actions"]:
                lines.append(f"1. {action}")
            lines.append("")
            lines.append("### Short-Term Actions (1-2 weeks)")
            for action in playbook["short_term_actions"]:
                lines.append(f"1. {action}")
            lines.append("")
            lines.append("### Long-Term Actions (1-3 months)")
            for action in playbook["long_term_actions"]:
                lines.append(f"1. {action}")
            lines.append("")
        return "\n".join(lines)

    def _supplier_alternatives(self, **kwargs):
        category = kwargs.get("category")
        if category and category in ALTERNATIVE_SUPPLIERS:
            cats = {category: ALTERNATIVE_SUPPLIERS[category]}
        else:
            cats = ALTERNATIVE_SUPPLIERS
        lines = ["# Alternative Supplier Directory", ""]
        for cat_name, suppliers in cats.items():
            best = _best_alternative(cat_name)
            lines.append(f"## {cat_name}")
            if best:
                lines.append(f"**Recommended (fastest lead time):** {best['name']} — {best['lead_time_days']}d")
            lines.append("")
            lines.append("| Supplier | Location | Lead Time | Quality | Capacity/Mo | Price Premium | MOQ |")
            lines.append("|----------|----------|-----------|---------|-------------|---------------|-----|")
            for sup in suppliers:
                premium_str = f"+{sup['price_premium_pct']:.1f}%" if sup["price_premium_pct"] >= 0 else f"{sup['price_premium_pct']:.1f}%"
                lines.append(
                    f"| {sup['name']} | {sup['location']} | {sup['lead_time_days']}d "
                    f"| {sup['quality_rating']}/5.0 | {sup['capacity_units_monthly']:,} "
                    f"| {premium_str} | {sup['min_order_qty']:,} |"
                )
            lines.append("")
            lines.append("**Certifications:**")
            for sup in suppliers:
                lines.append(f"- {sup['name']}: {', '.join(sup['certifications'])}")
            lines.append("")
        total_suppliers = sum(len(s) for s in ALTERNATIVE_SUPPLIERS.values())
        lines.append(f"**Total Qualified Alternatives:** {total_suppliers} suppliers across {len(ALTERNATIVE_SUPPLIERS)} categories")
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
                "- **External Changes:** none; no live freight, workflow, message, or report distribution occurred",
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
        operation = kwargs.get("operation", "disruption_dashboard")
        dispatch = {
            "disruption_dashboard": self._disruption_dashboard,
            "risk_assessment": self._risk_assessment,
            "mitigation_plan": self._mitigation_plan,
            "supplier_alternatives": self._supplier_alternatives,
            "disruption_impact": self._evidence_capability,
            "response_scenarios": self._evidence_capability,
            "response_execution": self._evidence_capability,
            "recovery_tracking": self._evidence_capability,
            "incident_report": self._evidence_capability,
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
    agent = SupplyChainDisruptionAlertAgent()
    print("=" * 80)
    print("EMBEDDED DEMO NETWORK (works offline)")
    print(agent.perform(operation="disruption_dashboard", disruption_id="DISR-002"))
    print("\n" + "=" * 80)
    print("LIVE TENANT DISRUPTION SIGNALS + LIVE ERP INBOUND EXCEPTIONS")
    print("(cold-chain case, late delivery, blocked invoice; falls back offline)")
    print(agent.perform(operation="disruption_dashboard"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="risk_assessment", route_id="RT-APAC-01"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="mitigation_plan", disruption_id="DISR-002"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="supplier_alternatives", category="Electronics"))
    print("=" * 80)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
