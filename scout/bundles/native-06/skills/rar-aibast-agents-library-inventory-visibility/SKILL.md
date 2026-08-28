---
name: "rar-aibast-agents-library-inventory-visibility"
description: "Reports stock dashboards joining a simulated Dynamics 365 catalog with ERP materials and goods receipts as inbound supply, with offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/inventory_visibility", "rar_sha256": "1fab16e92d49c19489ed2992df56294a8c1133aa9eefc87bc1f2a93dc08ce3e5", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.3.0", "author": "AIBAST", "tags": ["inventory", "stock-management", "replenishment", "omni-channel", "retail"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/inventory_visibility`. The original RAPP
agent is preserved byte-for-byte in `inventory_visibility_agent.py` and in the RCI capsule.

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

Inventory Visibility Agent — a template you are meant to mutate.

Provides omni-channel inventory visibility across stores, warehouses, and
channels: stock dashboards, stock-out alerts, replenishment plans, and
channel allocation for retail operations.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works anywhere):
       CRM — Static Dynamics 365 tenant (Aster Lane Office Systems):
         https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       ERP — Static ERP (materials, purchase orders, goods receipts):
         https://kody-w.github.io/static-erp/api/v1/
     Try: perform(operation="inventory_dashboard")
     — the dashboard is built from the tenant's live products (e.g.
     "Mobile Cart M8", AST-CRT-008) plus live sales-order demand, and
     joins the ERP's 20 materials with goods receipts as REAL inbound
     supply per CRM product (material CMP-PRH-0420 "Print head assembly,
     AsterPrint M420" feeds AST-PRN-420 — and only 36 of 40 units
     arrived on PO-47003, which the dashboard flags).
  2. No network? Everything falls back to the embedded demo layer below
     (STORES / SKUS / INVENTORY) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     INVENTORY_VISIBILITY_DATA_URL (CRM side) and/or
     INVENTORY_VISIBILITY_ERP_URL (ERP side) to any endpoint with the
     same shapes, or replace _fetch_collection() with your own inventory
     API. The fields the rest of the file needs are listed in
     _normalize_live_product() — everything else keeps working
     untouched. Per-location on-hand and days-of-supply are labeled
     "n/a — enrichment seam" until you wire your WMS.

OPERATIONS
  inventory_dashboard | stock_alerts | replenishment_plan |
  channel_allocation | network_inventory_status | reallocation_scenarios |
  reallocation_execution | investment_proposal
  kwargs: operation (required), sku_id, location_id, key, user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "key": {
      "type": "string"
    },
    "location_id": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "inventory_dashboard",
        "stock_alerts",
        "replenishment_plan",
        "channel_allocation",
        "network_inventory_status",
        "reallocation_scenarios",
        "reallocation_execution",
        "investment_proposal"
      ],
      "type": "string"
    },
    "sku_id": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `inventory_visibility_agent.py` and embedded as the fenced Python below (sha256 1fab16e92d49c194…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `inventory_visibility_agent.py` first:

```bash
python3 inventory_visibility_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 inventory_visibility_agent.py   # or on stdin
python3 inventory_visibility_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Inventory Visibility Agent — a template you are meant to mutate.

Provides omni-channel inventory visibility across stores, warehouses, and
channels: stock dashboards, stock-out alerts, replenishment plans, and
channel allocation for retail operations.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works anywhere):
       CRM — Static Dynamics 365 tenant (Aster Lane Office Systems):
         https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       ERP — Static ERP (materials, purchase orders, goods receipts):
         https://kody-w.github.io/static-erp/api/v1/
     Try: perform(operation="inventory_dashboard")
     — the dashboard is built from the tenant's live products (e.g.
     "Mobile Cart M8", AST-CRT-008) plus live sales-order demand, and
     joins the ERP's 20 materials with goods receipts as REAL inbound
     supply per CRM product (material CMP-PRH-0420 "Print head assembly,
     AsterPrint M420" feeds AST-PRN-420 — and only 36 of 40 units
     arrived on PO-47003, which the dashboard flags).
  2. No network? Everything falls back to the embedded demo layer below
     (STORES / SKUS / INVENTORY) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     INVENTORY_VISIBILITY_DATA_URL (CRM side) and/or
     INVENTORY_VISIBILITY_ERP_URL (ERP side) to any endpoint with the
     same shapes, or replace _fetch_collection() with your own inventory
     API. The fields the rest of the file needs are listed in
     _normalize_live_product() — everything else keeps working
     untouched. Per-location on-hand and days-of-supply are labeled
     "n/a — enrichment seam" until you wire your WMS.

OPERATIONS
  inventory_dashboard | stock_alerts | replenishment_plan |
  channel_allocation | network_inventory_status | reallocation_scenarios |
  reallocation_execution | investment_proposal
  kwargs: operation (required), sku_id, location_id, key, user_input
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
    "name": "@aibast-agents-library/inventory_visibility",
    "version": "1.3.0",
    "display_name": "Inventory Visibility Agent",
    "description": (
        "Reports stock dashboards joining a simulated Dynamics 365 catalog with ERP materials and goods receipts as inbound supply, with offline fallback."
    ),
    "author": "AIBAST",
    "tags": [
        "inventory",
        "stock-management",
        "replenishment",
        "omni-channel",
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
#   export INVENTORY_VISIBILITY_DATA_URL=https://your-org/api/data/v9.2
#   export INVENTORY_VISIBILITY_ERP_URL=https://your-erp/api/v1
# or replace _fetch_collection() with your ERP/WMS client. Downstream
# code only needs the fields produced by _normalize_live_product()
# and _erp_inbound_by_product().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "INVENTORY_VISIBILITY_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
ERP_SOURCE_URL = os.environ.get(
    "INVENTORY_VISIBILITY_ERP_URL",
    "https://kody-w.github.io/static-erp/api/v1",
)
_LIVE_CACHE = {}


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
    """Rows from the live simulated ERP (materials, purchase_orders,
    goods_receipts, suppliers, supplier_invoices); [] offline."""
    return _fetch_collection(collection, base_url=ERP_SOURCE_URL)


def _erp_inbound_by_product(products):
    """Join live ERP materials + goods receipts to the CRM catalog:
    each ERP material whose description names a CRM product becomes
    REAL inbound component supply for that product. Also flags short
    receipts (received < ordered on receipted POs). Returns (rows,
    short_flags); ([], []) when the ERP is unreachable."""
    materials = _erp("materials")
    if not materials:
        return [], []
    received = {}
    for g in _erp("goods_receipts"):
        for l in g.get("lines", []):
            m = l.get("material_number", "?")
            received[m] = received.get(m, 0) + int(float(l.get("quantity_received") or 0))
    rows = []
    for m in materials:
        desc = m.get("description", "")
        crm = next(
            (p for p in products if p.get("name") and p["name"] in desc), None
        )
        rows.append({
            "material": m.get("material_number", "?"),
            "description": desc,
            "group": m.get("material_group", "?"),
            "lead_time_days": m.get("lead_time_days"),
            "supplier": m.get("preferred_supplier_name", "?"),
            "inbound_received": received.get(m.get("material_number"), 0),
            "feeds_sku": (crm.get("productnumber") or crm.get("sku_id")) if crm else None,
        })
    shorts = []
    grs = _erp("goods_receipts")
    for p in _erp("purchase_orders"):
        po_no = p.get("po_number")
        p_grs = [g for g in grs if g.get("po_number") == po_no]
        if not p_grs:
            continue
        got = {}
        for g in p_grs:
            for l in g.get("lines", []):
                m = l.get("material_number", "?")
                got[m] = got.get(m, 0) + int(float(l.get("quantity_received") or 0))
        for l in p.get("lines", []):
            m = l.get("material_number", "?")
            ordered = int(float(l.get("quantity") or 0))
            if got.get(m, 0) < ordered:
                shorts.append(
                    f"{m} ({l.get('material_description', '')}): "
                    f"{got.get(m, 0)} of {ordered} received on {po_no} "
                    f"({p.get('supplier_name', '?')})"
                )
    return rows, shorts


def _normalize_live_product(row):
    """Project a Dynamics product record onto the shape this agent uses.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not available from the catalog alone'
    and the renderers label it as an enrichment seam."""
    def _f(value):
        try:
            return float(value)
        except (TypeError, ValueError):
            return None
    return {
        "sku_id": row.get("productnumber") or row.get("productid", ""),
        "name": row.get("name", "Unknown"),
        "category": row.get(
            "producttypecode@OData.Community.Display.V1.FormattedValue", "General"
        ),
        "unit_cost": _f(row.get("currentcost")),
        "retail_price": _f(row.get("price")),
        "on_hand": None,          # enrichment seam — wire your WMS
        "description": row.get("description", ""),
        "active": row.get("statecode") == 0,
        "_live": True,
    }


def _na(value, fmt="{}"):
    """None = the source system alone can't know this (enrichment seam)."""
    return "n/a — enrichment seam" if value is None else fmt.format(value)


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback) — Stores & Warehouses
# ---------------------------------------------------------------------------

STORES = {
    "STR-001": {
        "name": "Downtown Flagship",
        "city": "Chicago",
        "state": "IL",
        "type": "flagship",
        "capacity_sqft": 42000,
    },
    "STR-002": {
        "name": "Northshore Mall",
        "city": "Evanston",
        "state": "IL",
        "type": "mall",
        "capacity_sqft": 18500,
    },
    "STR-003": {
        "name": "Oakbrook Center",
        "city": "Oak Brook",
        "state": "IL",
        "type": "outlet",
        "capacity_sqft": 12000,
    },
    "STR-004": {
        "name": "Michigan Ave Express",
        "city": "Chicago",
        "state": "IL",
        "type": "express",
        "capacity_sqft": 6500,
    },
}

WAREHOUSES = {
    "WH-CENTRAL": {
        "name": "Central Distribution Center",
        "city": "Romeoville",
        "state": "IL",
        "capacity_pallets": 22000,
    },
    "WH-EAST": {
        "name": "East Regional Warehouse",
        "city": "Indianapolis",
        "state": "IN",
        "capacity_pallets": 14000,
    },
}

SKUS = {
    "SKU-1001": {"name": "Classic Denim Jacket", "category": "Apparel", "unit_cost": 34.50, "retail_price": 89.99},
    "SKU-1002": {"name": "Wireless Earbuds Pro", "category": "Electronics", "unit_cost": 18.75, "retail_price": 59.99},
    "SKU-1003": {"name": "Organic Cotton T-Shirt", "category": "Apparel", "unit_cost": 8.20, "retail_price": 29.99},
    "SKU-1004": {"name": "Smart Fitness Tracker", "category": "Electronics", "unit_cost": 42.00, "retail_price": 129.99},
    "SKU-1005": {"name": "Premium Running Shoes", "category": "Footwear", "unit_cost": 55.00, "retail_price": 149.99},
    "SKU-1006": {"name": "Stainless Water Bottle", "category": "Accessories", "unit_cost": 6.80, "retail_price": 24.99},
    "SKU-1007": {"name": "Leather Crossbody Bag", "category": "Accessories", "unit_cost": 27.50, "retail_price": 79.99},
    "SKU-1008": {"name": "UV Protection Sunglasses", "category": "Accessories", "unit_cost": 12.30, "retail_price": 44.99},
}

# Current on-hand quantities per location per SKU
INVENTORY = {
    "STR-001": {"SKU-1001": 74, "SKU-1002": 132, "SKU-1003": 210, "SKU-1004": 45, "SKU-1005": 38, "SKU-1006": 195, "SKU-1007": 61, "SKU-1008": 88},
    "STR-002": {"SKU-1001": 35, "SKU-1002": 67, "SKU-1003": 98, "SKU-1004": 22, "SKU-1005": 14, "SKU-1006": 110, "SKU-1007": 29, "SKU-1008": 53},
    "STR-003": {"SKU-1001": 18, "SKU-1002": 41, "SKU-1003": 65, "SKU-1004": 9, "SKU-1005": 7, "SKU-1006": 72, "SKU-1007": 15, "SKU-1008": 30},
    "STR-004": {"SKU-1001": 12, "SKU-1002": 28, "SKU-1003": 44, "SKU-1004": 6, "SKU-1005": 5, "SKU-1006": 55, "SKU-1007": 8, "SKU-1008": 19},
    "WH-CENTRAL": {"SKU-1001": 1450, "SKU-1002": 2300, "SKU-1003": 3800, "SKU-1004": 780, "SKU-1005": 620, "SKU-1006": 4100, "SKU-1007": 950, "SKU-1008": 1700},
    "WH-EAST": {"SKU-1001": 820, "SKU-1002": 1100, "SKU-1003": 2200, "SKU-1004": 410, "SKU-1005": 350, "SKU-1006": 2600, "SKU-1007": 530, "SKU-1008": 900},
}

SAFETY_STOCK = {
    "STR-001": {"SKU-1001": 30, "SKU-1002": 50, "SKU-1003": 80, "SKU-1004": 20, "SKU-1005": 15, "SKU-1006": 70, "SKU-1007": 25, "SKU-1008": 35},
    "STR-002": {"SKU-1001": 15, "SKU-1002": 30, "SKU-1003": 45, "SKU-1004": 10, "SKU-1005": 8, "SKU-1006": 40, "SKU-1007": 12, "SKU-1008": 20},
    "STR-003": {"SKU-1001": 10, "SKU-1002": 20, "SKU-1003": 30, "SKU-1004": 5, "SKU-1005": 5, "SKU-1006": 25, "SKU-1007": 8, "SKU-1008": 12},
    "STR-004": {"SKU-1001": 8, "SKU-1002": 15, "SKU-1003": 20, "SKU-1004": 4, "SKU-1005": 3, "SKU-1006": 20, "SKU-1007": 5, "SKU-1008": 10},
}

LEAD_TIMES_DAYS = {
    "WH-CENTRAL": {"STR-001": 1, "STR-002": 1, "STR-003": 2, "STR-004": 1},
    "WH-EAST": {"STR-001": 2, "STR-002": 2, "STR-003": 3, "STR-004": 2},
}

CHANNEL_DEMAND = {
    "in_store": {"weight": 0.45, "daily_units_avg": 320},
    "online_ship": {"weight": 0.30, "daily_units_avg": 215},
    "bopis": {"weight": 0.15, "daily_units_avg": 108},
    "marketplace": {"weight": 0.10, "daily_units_avg": 72},
}

DAILY_SELL_THROUGH = {
    "SKU-1001": 6.2, "SKU-1002": 9.8, "SKU-1003": 14.5, "SKU-1004": 3.1,
    "SKU-1005": 2.7, "SKU-1006": 12.0, "SKU-1007": 4.4, "SKU-1008": 7.3,
}

EVIDENCE_CAPABILITIES = {
    "network_inventory_status": {
        "title": "Cross-Location Inventory Status",
        "source_system": "Dynamics 365 Commerce",
        "write": False,
        "key_field": "status_id",
        "summary": (
            "Returns SKU-level inventory across stores, warehouses, in-transit, "
            "and ecommerce reserves while highlighting allocation imbalances."
        ),
        "record": {
            "status_id": "STATUS-WINTER-JACKETS-NW",
            "product": "Alpine Pro Winter Jacket",
            "scope": "51 locations",
            "inventory": "Stores 1,847; warehouses 940; in-transit 285; ecommerce reserve 128",
            "imbalance": "Portland Flagship 0 units; Portland Mall 3 units at 8/day; Seattle excess 247 units at 4/day",
            "opportunity": "Transfer 120 Seattle units to Portland to recover $18,400 in sales",
            "inputs_considered": "Real-time inventory, POS demand, and demand forecast",
        },
    },
    "reallocation_scenarios": {
        "title": "Demand-Aware Reallocation Scenarios",
        "source_system": "Dynamics 365 Supply Chain Management",
        "write": False,
        "key_field": "plan_id",
        "summary": (
            "Compares urgent and planned transfers using demand forecasts, "
            "distance, transit time, cost, and revenue recovery."
        ),
        "record": {
            "plan_id": "PLAN-SEATTLE-PORTLAND",
            "phase_1": "Move 40 units Seattle Flagship to Portland Flagship by overnight van; 12 hours; $340; $6,800 recovery",
            "phase_2": "Move 80 units from three Seattle suburban stores by regular truck; 24-48 hours; $180; $11,600 recovery",
            "total": "120 units; $520 transportation; $18,400 recovered revenue; 35:1 ROI",
            "source_impact": "Seattle retains 127 units, an 8-week supply at current demand",
            "recommendation": "Execute emergency phase first, then planned replenishment",
        },
    },
    "reallocation_execution": {
        "title": "Reallocation Execution and Health",
        "source_system": "Dynamics 365 Supply Chain Management and Microsoft Teams",
        "write": True,
        "key_field": "execution_id",
        "summary": (
            "Prepares transfer execution, stakeholder notifications, status "
            "tracking, and a system-wide inventory health view."
        ),
        "record": {
            "execution_id": "EXEC-SEATTLE-PORTLAND",
            "transfer_status": "Phase 1 van scheduled and pickup confirmed; Phase 2 truck routed",
            "notifications": "Store teams notified; Portland ecommerce availability prepared",
            "health": "Balance score 72/100; 43 days supply; $2.8M overstock; 147 stockouts/month",
            "additional_opportunities": "8 SKU reallocations; 680 units; 15 routes; $84,200 recovery for $3,400",
            "execution_note": "Simulation only; no quantities, routes, or notifications are changed",
        },
    },
    "investment_proposal": {
        "title": "Inventory Automation Investment Proposal",
        "source_system": "Microsoft Teams",
        "write": True,
        "key_field": "proposal_id",
        "summary": (
            "Builds an automation proposal with RFID, auto-replenishment, "
            "predictive allocation, and deterministic financial projections."
        ),
        "record": {
            "proposal_id": "PROPOSAL-NW-AUTOMATION",
            "rfid": "$85,000; accuracy 87% to 99.8%; $127,000 annual labor savings; 8-month payback",
            "auto_replenishment": "$45,000; stockouts down 62%; $142,000 annual savings; 3.8-month payback",
            "predictive_allocation": "$32,000; $71,000 annual revenue protection; 5.4-month payback",
            "three_year_projection": "$162,000 investment; $1,020,000 benefits; $858,000 net value; 530% ROI",
            "distribution": "Prepared for CFO and operations review in Microsoft Teams",
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

def _total_network_inventory(sku_id):
    """Sum on-hand across all locations for a given SKU."""
    return sum(loc.get(sku_id, 0) for loc in INVENTORY.values())


def _days_of_supply(sku_id, location_id):
    """Estimate days-of-supply at a location."""
    on_hand = INVENTORY.get(location_id, {}).get(sku_id, 0)
    daily = DAILY_SELL_THROUGH.get(sku_id, 1.0)
    return round(on_hand / daily, 1) if daily > 0 else 999.0


def _stock_status(sku_id, location_id):
    """Return stock status label for a SKU at a location."""
    on_hand = INVENTORY.get(location_id, {}).get(sku_id, 0)
    safety = SAFETY_STOCK.get(location_id, {}).get(sku_id, 0)
    if on_hand == 0:
        return "OUT_OF_STOCK"
    if on_hand <= safety:
        return "CRITICAL"
    if on_hand <= safety * 1.5:
        return "LOW"
    return "HEALTHY"


def _replenishment_qty(sku_id, location_id, target_days=14):
    """Calculate replenishment quantity targeting N days of supply."""
    on_hand = INVENTORY.get(location_id, {}).get(sku_id, 0)
    daily = DAILY_SELL_THROUGH.get(sku_id, 1.0)
    target_qty = int(daily * target_days)
    needed = max(0, target_qty - on_hand)
    return needed


def _channel_allocation_units(sku_id, total_available):
    """Allocate available inventory across channels by demand weight."""
    allocations = {}
    for channel, info in CHANNEL_DEMAND.items():
        allocations[channel] = int(total_available * info["weight"])
    remainder = total_available - sum(allocations.values())
    allocations["in_store"] += remainder
    return allocations


# ---------------------------------------------------------------------------
# Agent Class
# ---------------------------------------------------------------------------

class InventoryVisibilityAgent(BasicAgent):
    """Agent providing omni-channel inventory visibility and planning."""

    def __init__(self):
        self.name = "inventory-visibility-agent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "inventory_dashboard",
                            "stock_alerts",
                            "replenishment_plan",
                            "channel_allocation",
                            "network_inventory_status",
                            "reallocation_scenarios",
                            "reallocation_execution",
                            "investment_proposal",
                        ],
                    },
                    "sku_id": {"type": "string"},
                    "location_id": {"type": "string"},
                    "key": {"type": "string"},
                    "user_input": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    # ---- operations -------------------------------------------------------

    def _live_inventory_dashboard(self, products):
        """Dashboard built from live tenant records (preferred when online)."""
        orders = _fetch_collection("salesorders")
        open_orders = [o for o in orders if o.get("statecode") in (0, 1)]
        open_demand = sum(float(o.get("totalamount") or 0) for o in open_orders)
        lines = [
            "# Inventory Dashboard — Live Tenant Catalog",
            "",
            f"Live records from {DATA_SOURCE_URL} (Aster Lane Office Systems).",
            "Pass `location_id` (e.g. STR-001) for the embedded demo store view.",
            "",
            "| SKU | Product | Category | Unit Cost | Retail | On-Hand | Active |",
            "|-----|---------|----------|-----------|--------|---------|--------|",
        ]
        for p in sorted(products, key=lambda x: x["sku_id"]):
            lines.append(
                f"| {p['sku_id']} | {p['name']} | {p['category']} "
                f"| {_na(p['unit_cost'], '${:,.2f}')} | {_na(p['retail_price'], '${:,.2f}')} "
                f"| {_na(p['on_hand'])} | {'yes' if p['active'] else 'no'} |"
            )
        lines.append("")
        lines.append(f"**Catalog size:** {len(products)} live products")
        lines.append(
            f"**Demand signal (live sales orders):** {len(open_orders)} open orders, "
            f"${open_demand:,.2f} open order value"
        )
        lines.append(
            "**Per-location on-hand / days-of-supply:** n/a — enrichment seam "
            "(wire your WMS at the LIVE DATA SEAM)"
        )
        erp_rows, shorts = _erp_inbound_by_product(products)
        if erp_rows:
            lines.append("")
            lines.append("## Inbound Supply — Live ERP Materials + Goods Receipts")
            lines.append("")
            lines.append("| Material | Description | Group | Lead Time | Supplier | Inbound Received | Feeds SKU |")
            lines.append("|----------|-------------|-------|-----------|----------|------------------|-----------|")
            for r in erp_rows:
                lines.append(
                    f"| {r['material']} | {r['description']} | {r['group']} "
                    f"| {r['lead_time_days']}d | {r['supplier']} "
                    f"| {r['inbound_received']:,} | {r['feeds_sku'] or '—'} |"
                )
            lines.append("")
            lines.append(
                f"**ERP inbound view:** {len(erp_rows)} live materials joined to the "
                "CRM catalog by product name; quantities are REAL goods-receipt sums."
            )
            for s in shorts:
                lines.append(f"**Short receipt flagged:** {s}")
        else:
            lines.append("")
            lines.append("_Simulated ERP unreachable — inbound supply view unavailable._")
        return "\n".join(lines)

    def _inventory_dashboard(self, **kwargs):
        location_id = kwargs.get("location_id")
        if not location_id:
            live = [
                p for p in (
                    _normalize_live_product(r) for r in _fetch_collection("products")
                )
                if p["sku_id"]
            ]
            if live:
                return self._live_inventory_dashboard(live)
        locations = [location_id] if location_id and location_id in INVENTORY else list(STORES.keys())
        lines = ["# Inventory Dashboard", ""]
        for loc_id in locations:
            loc_info = STORES.get(loc_id, WAREHOUSES.get(loc_id, {}))
            lines.append(f"## {loc_info.get('name', loc_id)} (`{loc_id}`)")
            lines.append("")
            lines.append("| SKU | Product | On-Hand | Safety Stock | Status | Days of Supply |")
            lines.append("|-----|---------|---------|--------------|--------|----------------|")
            for sku_id in sorted(SKUS.keys()):
                sku = SKUS[sku_id]
                on_hand = INVENTORY[loc_id].get(sku_id, 0)
                safety = SAFETY_STOCK.get(loc_id, {}).get(sku_id, "N/A")
                status = _stock_status(sku_id, loc_id)
                dos = _days_of_supply(sku_id, loc_id)
                lines.append(f"| {sku_id} | {sku['name']} | {on_hand} | {safety} | {status} | {dos} |")
            lines.append("")
        total_units = sum(sum(v.values()) for v in INVENTORY.values())
        lines.append(f"**Total Network Inventory:** {total_units:,} units across {len(INVENTORY)} locations")
        return "\n".join(lines)

    def _stock_alerts(self, **kwargs):
        lines = ["# Stock Alerts", "", "## Critical & Out-of-Stock Items", ""]
        lines.append("| Location | SKU | Product | On-Hand | Safety Stock | Status | Action Required |")
        lines.append("|----------|-----|---------|---------|--------------|--------|-----------------|")
        alert_count = 0
        for loc_id in sorted(STORES.keys()):
            for sku_id in sorted(SKUS.keys()):
                status = _stock_status(sku_id, loc_id)
                if status in ("CRITICAL", "OUT_OF_STOCK"):
                    sku = SKUS[sku_id]
                    on_hand = INVENTORY[loc_id].get(sku_id, 0)
                    safety = SAFETY_STOCK[loc_id].get(sku_id, 0)
                    action = "Emergency replenish" if status == "OUT_OF_STOCK" else "Expedite transfer"
                    loc_name = STORES[loc_id]["name"]
                    lines.append(
                        f"| {loc_name} | {sku_id} | {sku['name']} | {on_hand} | {safety} | {status} | {action} |"
                    )
                    alert_count += 1
        lines.append("")
        lines.append(f"**Total Alerts:** {alert_count}")
        lines.append("")
        lines.append("## Low-Stock Warnings")
        lines.append("")
        low_count = 0
        for loc_id in sorted(STORES.keys()):
            for sku_id in sorted(SKUS.keys()):
                status = _stock_status(sku_id, loc_id)
                if status == "LOW":
                    dos = _days_of_supply(sku_id, loc_id)
                    lines.append(f"- **{STORES[loc_id]['name']}** / {SKUS[sku_id]['name']}: {dos} days remaining")
                    low_count += 1
        lines.append(f"\n**Low-Stock Warnings:** {low_count}")
        return "\n".join(lines)

    def _replenishment_plan(self, **kwargs):
        target_days = 14
        lines = [
            "# Replenishment Plan",
            "",
            f"**Target:** {target_days}-day supply at each store",
            "",
        ]
        total_cost = 0.0
        for loc_id in sorted(STORES.keys()):
            store = STORES[loc_id]
            lines.append(f"## {store['name']} (`{loc_id}`)")
            lines.append("")
            lines.append("| SKU | Product | Current | Target | Replenish Qty | Source | Lead Time | Est. Cost |")
            lines.append("|-----|---------|---------|--------|---------------|--------|-----------|-----------|")
            for sku_id in sorted(SKUS.keys()):
                qty = _replenishment_qty(sku_id, loc_id, target_days)
                if qty > 0:
                    sku = SKUS[sku_id]
                    on_hand = INVENTORY[loc_id][sku_id]
                    target_qty = on_hand + qty
                    wh_central = INVENTORY["WH-CENTRAL"].get(sku_id, 0)
                    source = "WH-CENTRAL" if wh_central >= qty else "WH-EAST"
                    lt = LEAD_TIMES_DAYS.get(source, {}).get(loc_id, 3)
                    cost = round(qty * sku["unit_cost"], 2)
                    total_cost += cost
                    lines.append(
                        f"| {sku_id} | {sku['name']} | {on_hand} | {target_qty} | {qty} | {source} | {lt}d | ${cost:,.2f} |"
                    )
            lines.append("")
        lines.append(f"**Estimated Total Replenishment Cost:** ${total_cost:,.2f}")
        return "\n".join(lines)

    def _channel_allocation(self, **kwargs):
        sku_id = kwargs.get("sku_id", "SKU-1001")
        sku = SKUS.get(sku_id, SKUS["SKU-1001"])
        total = _total_network_inventory(sku_id)
        allocations = _channel_allocation_units(sku_id, total)
        lines = [
            "# Channel Allocation",
            "",
            f"**SKU:** {sku_id} — {sku['name']}",
            f"**Total Network Inventory:** {total:,} units",
            "",
            "| Channel | Weight | Allocated Units | Daily Demand Avg | Days Coverage |",
            "|---------|--------|-----------------|------------------|---------------|",
        ]
        for channel, units in allocations.items():
            info = CHANNEL_DEMAND[channel]
            daily = info["daily_units_avg"]
            coverage = round(units / daily, 1) if daily > 0 else 0
            lines.append(
                f"| {channel.replace('_', ' ').title()} | {info['weight']*100:.0f}% | {units:,} | {daily} | {coverage} |"
            )
        lines.append("")
        lines.append("## Allocation Recommendations")
        lines.append("")
        lines.append("- **In-Store Priority:** Flagship and mall locations receive 60% of in-store allocation")
        lines.append("- **Online Buffer:** Maintain 3-day safety stock for e-commerce fulfillment")
        lines.append("- **BOPIS Reserve:** Hold 10% buffer for same-day pickup surges")
        lines.append("- **Marketplace Cap:** Limit marketplace allocation to prevent channel conflict")
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
                "- **External Changes:** none; no live mutation or notification occurred",
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

    # ---- dispatch ----------------------------------------------------------

    def perform(self, **kwargs):
        operation = kwargs.get("operation", "inventory_dashboard")
        dispatch = {
            "inventory_dashboard": self._inventory_dashboard,
            "stock_alerts": self._stock_alerts,
            "replenishment_plan": self._replenishment_plan,
            "channel_allocation": self._channel_allocation,
            "network_inventory_status": self._evidence_capability,
            "reallocation_scenarios": self._evidence_capability,
            "reallocation_execution": self._evidence_capability,
            "investment_proposal": self._evidence_capability,
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
    agent = InventoryVisibilityAgent()
    print("=" * 80)
    print("EMBEDDED DEMO STORE (works offline)")
    print(agent.perform(operation="inventory_dashboard", location_id="STR-001"))
    print("\n" + "=" * 80)
    print("LIVE TENANT CATALOG + LIVE ERP INBOUND SUPPLY (goods-receipt join;")
    print("fetched over HTTP; falls back offline)")
    print(agent.perform(operation="inventory_dashboard"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="stock_alerts"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="replenishment_plan"))
    print("\n" + "=" * 80)
    print(agent.perform(operation="channel_allocation", sku_id="SKU-1003"))
    print("=" * 80)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
