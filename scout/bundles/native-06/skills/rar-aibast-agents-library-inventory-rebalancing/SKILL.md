---
name: "rar-aibast-agents-library-inventory-rebalancing"
description: "Analyzes stock vs demand and joins simulated ERP materials and goods receipts to the Dynamics 365 catalog, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/inventory_rebalancing", "rar_sha256": "7c44c44d6539d4a22d69eb6ace52608bed017348cd144ec56638b41c102ffd37", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.3.0", "author": "AIBAST", "tags": ["inventory", "warehouse", "supply-chain", "rebalancing", "manufacturing"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/inventory_rebalancing`. The original RAPP
agent is preserved byte-for-byte in `inventory_rebalancing_agent.py` and in the RCI capsule.

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

Inventory Rebalancing Agent — a template you are meant to mutate.

Analyzes warehouse inventory levels across multiple facilities, identifies
imbalances relative to demand forecasts, and generates transfer plans with
cost-optimized rebalancing recommendations. Supports SKU-level snapshot
reporting, inter-warehouse transfer planning, and holding-cost analysis.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works from anywhere):
       CRM — Static Dynamics 365 tenant (Aster Lane Office Systems):
         https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       ERP — Static ERP (materials, purchase orders, goods receipts):
         https://kody-w.github.io/static-erp/api/v1/
     The tenant's product catalog is the finished-goods SKU master; the
     ERP's 20 materials are the component master, joined to goods
     receipts as REAL inbound supply and back to the CRM catalog by
     product name (e.g. material CMP-PRH-0420 "Print head assembly,
     AsterPrint M420" feeds CRM product AST-PRN-420).
     Try: perform(operation="inventory_snapshot")
     — the ERP section flags the real short receipt: 36 of 40 print
     heads received on PO-47003.
  2. No network? Everything falls back to the embedded demo layer below
     (WAREHOUSES / SKU_INVENTORY / DEMAND_FORECASTS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     INVENTORY_REBALANCING_DATA_URL (CRM side) and/or
     INVENTORY_REBALANCING_ERP_URL (ERP side) to any endpoint with the
     same shapes, or replace _fetch_collection() with a SAP/NetSuite
     client. Fields the rest of the file needs are listed in
     _normalize_live_sku() — per-warehouse bin levels render as "n/a —
     enrichment seam" until you wire your WMS.

OPERATIONS
  inventory_snapshot | rebalance_recommendation | transfer_plan
  | cost_analysis | portfolio_analysis | recovery_plan | policy_update
  | continuous_optimization
  kwargs: operation (required), sku

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "Operation to perform. Defaults to inventory_snapshot when omitted.",
      "enum": [
        "inventory_snapshot",
        "rebalance_recommendation",
        "transfer_plan",
        "cost_analysis",
        "portfolio_analysis",
        "recovery_plan",
        "policy_update",
        "continuous_optimization"
      ],
      "type": "string"
    },
    "sku": {
      "description": "SKU identifier used to select inventory recovery, policy, and optimization records.",
      "type": "string"
    }
  },
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `inventory_rebalancing_agent.py` and embedded as the fenced Python below (sha256 7c44c44d6539d4a2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `inventory_rebalancing_agent.py` first:

```bash
python3 inventory_rebalancing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 inventory_rebalancing_agent.py   # or on stdin
python3 inventory_rebalancing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Inventory Rebalancing Agent — a template you are meant to mutate.

Analyzes warehouse inventory levels across multiple facilities, identifies
imbalances relative to demand forecasts, and generates transfer plans with
cost-optimized rebalancing recommendations. Supports SKU-level snapshot
reporting, inter-warehouse transfer planning, and holding-cost analysis.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works from anywhere):
       CRM — Static Dynamics 365 tenant (Aster Lane Office Systems):
         https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       ERP — Static ERP (materials, purchase orders, goods receipts):
         https://kody-w.github.io/static-erp/api/v1/
     The tenant's product catalog is the finished-goods SKU master; the
     ERP's 20 materials are the component master, joined to goods
     receipts as REAL inbound supply and back to the CRM catalog by
     product name (e.g. material CMP-PRH-0420 "Print head assembly,
     AsterPrint M420" feeds CRM product AST-PRN-420).
     Try: perform(operation="inventory_snapshot")
     — the ERP section flags the real short receipt: 36 of 40 print
     heads received on PO-47003.
  2. No network? Everything falls back to the embedded demo layer below
     (WAREHOUSES / SKU_INVENTORY / DEMAND_FORECASTS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     INVENTORY_REBALANCING_DATA_URL (CRM side) and/or
     INVENTORY_REBALANCING_ERP_URL (ERP side) to any endpoint with the
     same shapes, or replace _fetch_collection() with a SAP/NetSuite
     client. Fields the rest of the file needs are listed in
     _normalize_live_sku() — per-warehouse bin levels render as "n/a —
     enrichment seam" until you wire your WMS.

OPERATIONS
  inventory_snapshot | rebalance_recommendation | transfer_plan
  | cost_analysis | portfolio_analysis | recovery_plan | policy_update
  | continuous_optimization
  kwargs: operation (required), sku
"""

import sys
import os
import json
import urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/inventory_rebalancing",
    "version": "1.3.0",
    "display_name": "Inventory Rebalancing Agent",
    "description": "Analyzes stock vs demand and joins simulated ERP materials and goods receipts to the Dynamics 365 catalog, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["inventory", "warehouse", "supply-chain", "rebalancing", "manufacturing"],
    "category": "manufacturing",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# LIVE DATA SEAM — swap this for your real systems
#
# Defaults: TWO globally hosted simulated systems (synthetic data
# served as JSON from GitHub Pages). To hook your own world, either:
#   export INVENTORY_REBALANCING_DATA_URL=https://your-org/api/data/v9.2
#   export INVENTORY_REBALANCING_ERP_URL=https://your-erp/api/v1
# or replace _fetch_collection() with your WMS/ERP client. Downstream
# code only needs the fields produced by _normalize_live_sku() and
# _erp_material_master().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "INVENTORY_REBALANCING_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
ERP_SOURCE_URL = os.environ.get(
    "INVENTORY_REBALANCING_ERP_URL",
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


def _normalize_live_sku(row, assets):
    """Project a Dynamics product onto the SKU shape this agent renders.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not knowable from the catalog record
    alone' and the renderer labels it as an enrichment seam (wire your
    WMS bin levels and demand planner there)."""
    name = row.get("name", "Unknown")
    deployed = sum(1 for a in assets if a.get("msdyn_productname") == name)
    return {
        "sku": row.get("productnumber", "?"),
        "description": name,
        "unit_cost": float(row.get("currentcost") or 0),
        "list_price": float(row.get("price") or 0),
        "deployed_assets": deployed,       # real count from customer assets
        "warehouse_levels": None,          # enrichment seam — wire your WMS
        "reorder_point": None,             # enrichment seam — wire demand planning
        "_live": True,
    }


def _live_catalog():
    """Tenant products reinterpreted as the SKU master, with deployed
    units counted from installed customer assets; [] when offline."""
    rows = _fetch_collection("products")
    assets = _fetch_collection("msdyn_customerassets") if rows else []
    return [_normalize_live_sku(r, assets) for r in rows]


def _erp_material_master():
    """Live ERP materials joined to goods receipts (REAL inbound supply)
    and to the CRM product catalog by product name — the ERP component
    that feeds each finished-goods SKU. [] when the ERP is unreachable."""
    materials = _erp("materials")
    if not materials:
        return []
    inbound = {}
    for g in _erp("goods_receipts"):
        for l in g.get("lines", []):
            m = l.get("material_number", "?")
            inbound[m] = inbound.get(m, 0) + int(float(l.get("quantity_received") or 0))
    products = _fetch_collection("products")
    rows = []
    for m in materials:
        num = m.get("material_number", "?")
        desc = m.get("description", "")
        crm = next(
            (p for p in products if p.get("name") and p["name"] in desc), None
        )
        rows.append({
            "material": num,
            "description": desc,
            "group": m.get("material_group", "?"),
            "std_price": float(m.get("standard_price") or 0),
            "lead_time_days": m.get("lead_time_days"),
            "supplier": m.get("preferred_supplier_name", "?"),
            "inbound_received": inbound.get(num, 0),
            "crm_product": f"{crm.get('productnumber')} ({crm.get('name')})" if crm else None,
        })
    return rows


def _erp_short_receipts():
    """POs whose goods receipts came up short: for each ERP purchase
    order already receipted, compare ordered vs received per material.
    Returns [] when the ERP is unreachable or everything matched."""
    pos = _erp("purchase_orders")
    grs = _erp("goods_receipts")
    shorts = []
    for p in pos:
        po_no = p.get("po_number")
        p_grs = [g for g in grs if g.get("po_number") == po_no]
        if not p_grs:
            continue
        received = {}
        for g in p_grs:
            for l in g.get("lines", []):
                m = l.get("material_number", "?")
                received[m] = received.get(m, 0) + int(float(l.get("quantity_received") or 0))
        for l in p.get("lines", []):
            m = l.get("material_number", "?")
            ordered = int(float(l.get("quantity") or 0))
            got = received.get(m, 0)
            if got < ordered:
                shorts.append({
                    "material": m,
                    "description": l.get("material_description", ""),
                    "po_number": po_no,
                    "supplier": p.get("supplier_name", "?"),
                    "ordered": ordered,
                    "received": got,
                })
    return shorts


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

WAREHOUSES = {
    "WH-ATL": {
        "name": "Atlanta Distribution Center",
        "region": "Southeast",
        "capacity_pallets": 12000,
        "used_pallets": 10450,
        "annual_holding_cost_per_pallet": 142.0,
    },
    "WH-ORD": {
        "name": "Chicago Regional Hub",
        "region": "Midwest",
        "capacity_pallets": 18000,
        "used_pallets": 9200,
        "annual_holding_cost_per_pallet": 158.0,
    },
    "WH-DFW": {
        "name": "Dallas Fulfillment Center",
        "region": "South Central",
        "capacity_pallets": 15000,
        "used_pallets": 14100,
        "annual_holding_cost_per_pallet": 135.0,
    },
    "WH-SEA": {
        "name": "Seattle West Coast Depot",
        "region": "Pacific Northwest",
        "capacity_pallets": 10000,
        "used_pallets": 4300,
        "annual_holding_cost_per_pallet": 172.0,
    },
}

SKU_INVENTORY = {
    "SKU-4401": {"description": "Brushless DC Motor 48V", "unit_cost": 87.50, "weight_kg": 3.2,
                  "levels": {"WH-ATL": 3200, "WH-ORD": 1800, "WH-DFW": 4100, "WH-SEA": 600}},
    "SKU-4402": {"description": "Planetary Gearbox PG-20", "unit_cost": 214.00, "weight_kg": 5.8,
                  "levels": {"WH-ATL": 750, "WH-ORD": 2400, "WH-DFW": 300, "WH-SEA": 1100}},
    "SKU-4403": {"description": "Linear Actuator LA-150", "unit_cost": 162.30, "weight_kg": 4.1,
                  "levels": {"WH-ATL": 1900, "WH-ORD": 500, "WH-DFW": 2600, "WH-SEA": 200}},
    "SKU-4404": {"description": "Servo Controller SC-800", "unit_cost": 345.00, "weight_kg": 1.4,
                  "levels": {"WH-ATL": 400, "WH-ORD": 1200, "WH-DFW": 950, "WH-SEA": 1800}},
    "SKU-4405": {"description": "Encoder Module EM-512", "unit_cost": 58.75, "weight_kg": 0.6,
                  "levels": {"WH-ATL": 5000, "WH-ORD": 3100, "WH-DFW": 4800, "WH-SEA": 900}},
    "SKU-4406": {"description": "Harmonic Drive HD-25", "unit_cost": 489.00, "weight_kg": 7.3,
                  "levels": {"WH-ATL": 180, "WH-ORD": 620, "WH-DFW": 90, "WH-SEA": 340}},
}

DEMAND_FORECASTS = {
    "SKU-4401": {"WH-ATL": 2800, "WH-ORD": 2600, "WH-DFW": 3000, "WH-SEA": 1500},
    "SKU-4402": {"WH-ATL": 1100, "WH-ORD": 900, "WH-DFW": 1200, "WH-SEA": 800},
    "SKU-4403": {"WH-ATL": 800, "WH-ORD": 1400, "WH-DFW": 1100, "WH-SEA": 900},
    "SKU-4404": {"WH-ATL": 700, "WH-ORD": 600, "WH-DFW": 800, "WH-SEA": 500},
    "SKU-4405": {"WH-ATL": 3500, "WH-ORD": 4200, "WH-DFW": 3800, "WH-SEA": 2300},
    "SKU-4406": {"WH-ATL": 300, "WH-ORD": 250, "WH-DFW": 400, "WH-SEA": 280},
}

REORDER_POINTS = {
    "SKU-4401": 1200, "SKU-4402": 500, "SKU-4403": 600,
    "SKU-4404": 350, "SKU-4405": 2000, "SKU-4406": 150,
}

TRANSFER_COSTS_PER_KG = {
    ("WH-ATL", "WH-ORD"): 0.28, ("WH-ATL", "WH-DFW"): 0.22,
    ("WH-ATL", "WH-SEA"): 0.41, ("WH-ORD", "WH-ATL"): 0.28,
    ("WH-ORD", "WH-DFW"): 0.25, ("WH-ORD", "WH-SEA"): 0.34,
    ("WH-DFW", "WH-ATL"): 0.22, ("WH-DFW", "WH-ORD"): 0.25,
    ("WH-DFW", "WH-SEA"): 0.38, ("WH-SEA", "WH-ATL"): 0.41,
    ("WH-SEA", "WH-ORD"): 0.34, ("WH-SEA", "WH-DFW"): 0.38,
}

INVENTORY_RECOVERY_RECORDS = {
    "SKU-4401": {
        "velocity": "fast", "days_on_hand": 41, "obsolete_risk": "low",
        "working_capital": 848750.00, "action": "retain and rebalance",
        "safety_stock": 1250, "dynamic_reorder_point": 1320,
    },
    "SKU-4404": {
        "velocity": "slow", "days_on_hand": 173, "obsolete_risk": "medium",
        "working_capital": 1500750.00, "action": "vendor return then targeted markdown",
        "safety_stock": 320, "dynamic_reorder_point": 410,
    },
    "SKU-4406": {
        "velocity": "obsolete", "days_on_hand": 286, "obsolete_risk": "high",
        "working_capital": 601470.00, "action": "flash sale and supplier return",
        "safety_stock": 140, "dynamic_reorder_point": 165,
    },
}

EVIDENCE_MARKER = (
    "[Evidence: inventory-rebalancing one-pager and demo transcript; "
    "portfolio classification, recovery planning, dynamic policies, and continuous checks]"
)


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _utilization_pct(wh_id):
    """Return warehouse utilization as a percentage."""
    wh = WAREHOUSES[wh_id]
    return round(wh["used_pallets"] / wh["capacity_pallets"] * 100, 1)


def _stock_vs_demand(sku, wh_id):
    """Return surplus (+) or deficit (-) for a SKU at a warehouse."""
    on_hand = SKU_INVENTORY[sku]["levels"].get(wh_id, 0)
    forecast = DEMAND_FORECASTS[sku].get(wh_id, 0)
    return on_hand - forecast


def _total_inventory_value(wh_id):
    """Sum the dollar value of all SKUs at a warehouse."""
    total = 0.0
    for sku, info in SKU_INVENTORY.items():
        qty = info["levels"].get(wh_id, 0)
        total += qty * info["unit_cost"]
    return round(total, 2)


def _build_imbalances():
    """Return list of (sku, wh_from, wh_to, qty, cost) transfer suggestions."""
    transfers = []
    for sku, info in SKU_INVENTORY.items():
        surpluses = []
        deficits = []
        for wh_id in WAREHOUSES:
            delta = _stock_vs_demand(sku, wh_id)
            if delta > 200:
                surpluses.append((wh_id, delta))
            elif delta < -200:
                deficits.append((wh_id, abs(delta)))
        surpluses.sort(key=lambda x: x[1], reverse=True)
        deficits.sort(key=lambda x: x[1], reverse=True)
        for src, s_qty in surpluses:
            for dst, d_qty in deficits:
                move_qty = min(s_qty, d_qty)
                if move_qty <= 0:
                    continue
                cost_per_unit = TRANSFER_COSTS_PER_KG.get(
                    (src, dst), 0.30) * info["weight_kg"]
                cost = round(move_qty * cost_per_unit, 2)
                transfers.append((sku, src, dst, move_qty, cost))
                s_qty -= move_qty
                d_qty -= move_qty
    return transfers


def _annual_holding_cost(wh_id):
    """Estimate total annual holding cost for a warehouse."""
    wh = WAREHOUSES[wh_id]
    return round(wh["used_pallets"] * wh["annual_holding_cost_per_pallet"], 2)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class InventoryRebalancingAgent(BasicAgent):
    """Optimizes multi-warehouse inventory distribution against demand forecasts."""

    def __init__(self):
        self.name = "InventoryRebalancingAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "operations": [
                "inventory_snapshot",
                "rebalance_recommendation",
                "transfer_plan",
                "cost_analysis",
                "portfolio_analysis",
                "recovery_plan",
                "policy_update",
                "continuous_optimization",
            ],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "description": "Operation to perform. Defaults to inventory_snapshot when omitted.",
                        "enum": [
                            "inventory_snapshot",
                            "rebalance_recommendation",
                            "transfer_plan",
                            "cost_analysis",
                            "portfolio_analysis",
                            "recovery_plan",
                            "policy_update",
                            "continuous_optimization",
                        ],
                    },
                    "sku": {
                        "type": "string",
                        "description": "SKU identifier used to select inventory recovery, policy, and optimization records.",
                    },
                },
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    # ------------------------------------------------------------------
    # Dispatcher
    # ------------------------------------------------------------------
    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "inventory_snapshot")
        dispatch = {
            "inventory_snapshot": self._inventory_snapshot,
            "rebalance_recommendation": self._rebalance_recommendation,
            "transfer_plan": self._transfer_plan,
            "cost_analysis": self._cost_analysis,
            "portfolio_analysis": self._portfolio_analysis,
            "recovery_plan": self._recovery_plan,
            "policy_update": self._policy_update,
            "continuous_optimization": self._continuous_optimization,
        }
        handler = dispatch.get(operation)
        if handler is None:
            return f"**Error:** Unknown operation `{operation}`. Valid operations: {', '.join(dispatch.keys())}"
        return handler(**kwargs)

    # ------------------------------------------------------------------
    # Operations
    # ------------------------------------------------------------------
    def _inventory_snapshot(self, **kwargs) -> str:
        lines = ["## Inventory Snapshot\n"]
        lines.append("| Warehouse | Region | Utilization | Pallets Used/Cap | Inventory Value |")
        lines.append("|-----------|--------|-------------|------------------|-----------------|")
        for wh_id, wh in WAREHOUSES.items():
            util = _utilization_pct(wh_id)
            val = _total_inventory_value(wh_id)
            flag = " :red_circle:" if util > 90 else ""
            lines.append(
                f"| {wh['name']} | {wh['region']} | {util}%{flag} | "
                f"{wh['used_pallets']:,}/{wh['capacity_pallets']:,} | ${val:,.2f} |"
            )

        lines.append("\n### SKU Levels by Warehouse\n")
        lines.append("| SKU | Description | ATL | ORD | DFW | SEA | Reorder Pt |")
        lines.append("|-----|-------------|-----|-----|-----|-----|------------|")
        for sku, info in SKU_INVENTORY.items():
            lvls = info["levels"]
            rp = REORDER_POINTS[sku]
            row_cells = [f"{lvls.get(wh, 0):,}" for wh in WAREHOUSES]
            flags = []
            for wh in WAREHOUSES:
                if lvls.get(wh, 0) < rp:
                    flags.append(wh)
            note = f" (below reorder at {', '.join(flags)})" if flags else ""
            lines.append(
                f"| {sku} | {info['description']} | {' | '.join(row_cells)} | {rp:,}{note} |"
            )
        live = _live_catalog()
        if live:
            seam = "n/a — enrichment seam"
            lines.append("\n### Live Tenant SKU Master (Dynamics products + installed assets)\n")
            lines.append("| SKU | Description | Unit Cost | List Price | Deployed Assets | Warehouse Levels | Reorder Pt |")
            lines.append("|-----|-------------|-----------|------------|-----------------|------------------|------------|")
            for s in live:
                lines.append(
                    f"| {s['sku']} | {s['description']} | ${s['unit_cost']:,.2f} | "
                    f"${s['list_price']:,.2f} | {s['deployed_assets']} | "
                    f"{s['warehouse_levels'] or seam} | {s['reorder_point'] or seam} |"
                )
        else:
            lines.append("\n_Live tenant unreachable — showing embedded demo inventory only._")
        erp_rows = _erp_material_master()
        if erp_rows:
            lines.append("\n### Live ERP Material Master + Inbound Supply (goods receipts, joined to the CRM catalog)\n")
            lines.append("| Material | Description | Group | Std Price | Lead Time | Preferred Supplier | Inbound Received | Feeds CRM Product |")
            lines.append("|----------|-------------|-------|-----------|-----------|--------------------|------------------|-------------------|")
            for r in erp_rows:
                lines.append(
                    f"| {r['material']} | {r['description']} | {r['group']} | "
                    f"${r['std_price']:,.2f} | {r['lead_time_days']}d | {r['supplier']} | "
                    f"{r['inbound_received']:,} | {r['crm_product'] or '—'} |"
                )
            for s in _erp_short_receipts():
                lines.append(
                    f"\n**Short receipt flagged:** {s['material']} ({s['description']}) — "
                    f"{s['received']} received vs {s['ordered']} ordered on {s['po_number']} "
                    f"({s['supplier']}). Check the goods receipt before counting this "
                    "as available supply."
                )
            lines.append(
                f"\n**ERP component view:** {len(erp_rows)} live materials; per-warehouse "
                "bin levels remain n/a — enrichment seam (wire your WMS)."
            )
        else:
            lines.append("\n_Simulated ERP unreachable — component material master unavailable._")
        return "\n".join(lines)

    def _rebalance_recommendation(self, **kwargs) -> str:
        lines = ["## Rebalance Recommendations\n"]
        lines.append("Analysis of stock-vs-demand across all facilities:\n")
        lines.append("| SKU | Warehouse | On-Hand | Forecast | Delta | Status |")
        lines.append("|-----|-----------|---------|----------|-------|--------|")
        critical_count = 0
        for sku in SKU_INVENTORY:
            for wh_id in WAREHOUSES:
                delta = _stock_vs_demand(sku, wh_id)
                on_hand = SKU_INVENTORY[sku]["levels"].get(wh_id, 0)
                forecast = DEMAND_FORECASTS[sku].get(wh_id, 0)
                if delta < -200:
                    status = "DEFICIT"
                    critical_count += 1
                elif delta > 500:
                    status = "SURPLUS"
                else:
                    status = "Balanced"
                if status != "Balanced":
                    lines.append(
                        f"| {sku} | {WAREHOUSES[wh_id]['name'][:20]} | "
                        f"{on_hand:,} | {forecast:,} | {delta:+,} | **{status}** |"
                    )
        lines.append(f"\n**Critical imbalances detected:** {critical_count}")
        lines.append("**Recommendation:** Execute transfer plan to redistribute surplus stock to deficit locations.")
        return "\n".join(lines)

    def _transfer_plan(self, **kwargs) -> str:
        transfers = _build_imbalances()
        lines = ["## Transfer Plan\n"]
        if not transfers:
            lines.append("No transfers required; inventory is balanced within tolerance.")
            return "\n".join(lines)

        lines.append("| SKU | From | To | Qty | Unit Wt (kg) | Transfer Cost |")
        lines.append("|-----|------|----|-----|--------------|---------------|")
        total_cost = 0.0
        total_units = 0
        for sku, src, dst, qty, cost in transfers:
            wt = SKU_INVENTORY[sku]["weight_kg"]
            lines.append(
                f"| {sku} | {src} | {dst} | {qty:,} | {wt} | ${cost:,.2f} |"
            )
            total_cost += cost
            total_units += qty

        lines.append(f"\n**Total units to transfer:** {total_units:,}")
        lines.append(f"**Total transfer cost:** ${total_cost:,.2f}")
        lines.append(f"**Estimated transit time:** 2-5 business days (ground freight)")
        lines.append(
            "\n### Expected Post-Transfer Utilization\n"
        )
        lines.append("| Warehouse | Current Util | Projected Util |")
        lines.append("|-----------|-------------|----------------|")
        for wh_id, wh in WAREHOUSES.items():
            cur = _utilization_pct(wh_id)
            # Rough projection: assume net transfer effect
            net = sum(q for s, _, d, q, _ in transfers if d == wh_id) - sum(
                q for s, _, d, q, _ in transfers if s == wh_id
            )
            # This is a simplified model
            proj_pallets = wh["used_pallets"] + int(net * 0.02)  # rough pallet factor
            proj = round(proj_pallets / wh["capacity_pallets"] * 100, 1)
            lines.append(f"| {wh['name']} | {cur}% | {proj}% |")
        return "\n".join(lines)

    def _cost_analysis(self, **kwargs) -> str:
        lines = ["## Inventory Holding & Transfer Cost Analysis\n"]

        lines.append("### Annual Holding Costs\n")
        lines.append("| Warehouse | Pallets | Cost/Pallet/Yr | Annual Holding Cost |")
        lines.append("|-----------|---------|----------------|---------------------|")
        total_holding = 0.0
        for wh_id, wh in WAREHOUSES.items():
            hc = _annual_holding_cost(wh_id)
            total_holding += hc
            lines.append(
                f"| {wh['name']} | {wh['used_pallets']:,} | "
                f"${wh['annual_holding_cost_per_pallet']:.2f} | ${hc:,.2f} |"
            )
        lines.append(f"\n**Total annual holding cost:** ${total_holding:,.2f}")

        lines.append("\n### Inventory Value at Risk (Below Reorder Point)\n")
        lines.append("| SKU | Warehouse | On-Hand | Reorder Pt | Shortfall | Value at Risk |")
        lines.append("|-----|-----------|---------|------------|-----------|---------------|")
        total_risk = 0.0
        for sku, info in SKU_INVENTORY.items():
            rp = REORDER_POINTS[sku]
            for wh_id in WAREHOUSES:
                qty = info["levels"].get(wh_id, 0)
                if qty < rp:
                    shortfall = rp - qty
                    val = round(shortfall * info["unit_cost"], 2)
                    total_risk += val
                    lines.append(
                        f"| {sku} | {wh_id} | {qty:,} | {rp:,} | {shortfall:,} | ${val:,.2f} |"
                    )
        lines.append(f"\n**Total value at risk from stockouts:** ${total_risk:,.2f}")

        transfers = _build_imbalances()
        transfer_cost = sum(c for _, _, _, _, c in transfers)
        lines.append(f"\n### Transfer vs. Holding Trade-off")
        lines.append(f"- One-time transfer cost: **${transfer_cost:,.2f}**")
        lines.append(f"- Avoided expedited-shipping premium (est.): **${transfer_cost * 3.2:,.2f}**")
        lines.append(f"- Net annual benefit from rebalancing: **${total_risk * 0.6 - transfer_cost:,.2f}**")
        return "\n".join(lines)

    def _selected_recovery_records(self, **kwargs):
        sku = str(kwargs.get("sku", "")).strip().upper()
        if not sku:
            return list(INVENTORY_RECOVERY_RECORDS.items()), ""
        record = INVENTORY_RECOVERY_RECORDS.get(sku)
        if record is None:
            valid = ", ".join(INVENTORY_RECOVERY_RECORDS)
            return [], f"**Error:** Unknown SKU `{sku}`. Valid: {valid}"
        return [(sku, record)], ""

    def _portfolio_analysis(self, **kwargs) -> str:
        records, error = self._selected_recovery_records(**kwargs)
        if error:
            return error
        lines = ["## Inventory Portfolio Classification", EVIDENCE_MARKER, "",
                 "| SKU | Item | Velocity | Days on Hand | Obsolescence Risk | Working Capital |",
                 "|-----|------|----------|--------------|-------------------|-----------------|"]
        for sku, rec in records:
            item = SKU_INVENTORY[sku]
            lines.append(
                f"| {sku} | {item['description']} | {rec['velocity']} | "
                f"{rec['days_on_hand']} | {rec['obsolete_risk']} | "
                f"${rec['working_capital']:,.2f} |"
            )
        tied_up = sum(rec["working_capital"] for _, rec in records)
        lines.append(f"\n**Working capital represented:** ${tied_up:,.2f}")
        return "\n".join(lines)

    def _recovery_plan(self, **kwargs) -> str:
        records, error = self._selected_recovery_records(**kwargs)
        if error:
            return error
        lines = ["## Phased Inventory Recovery Plan", EVIDENCE_MARKER, "",
                 "| Phase | SKU | Deterministic Action | Success Measure |",
                 "|-------|-----|----------------------|-----------------|"]
        for sku, rec in records:
            lines.extend([
                f"| 1 - Contain | {sku} | Freeze nonessential replenishment | No new excess receipts |",
                f"| 2 - Recover | {sku} | {rec['action']} | Reduce days on hand below 90 |",
                f"| 3 - Sustain | {sku} | Adopt safety stock {rec['safety_stock']} and reorder point "
                f"{rec['dynamic_reorder_point']} | Weekly policy compliance |",
            ])
        lines.append("\n**Implementation timeline:** contain in 7 days, recover in 30 days, sustain from day 31.")
        return "\n".join(lines)

    def _policy_update(self, **kwargs) -> str:
        sku = str(kwargs.get("sku", "SKU-4406")).strip().upper()
        record = INVENTORY_RECOVERY_RECORDS.get(sku)
        if record is None:
            return f"**Error:** Unknown SKU `{sku}`. Valid: {', '.join(INVENTORY_RECOVERY_RECORDS)}"
        return "\n".join([
            "## Dynamic Inventory Policy Update",
            EVIDENCE_MARKER,
            f"**SKU lookup:** {sku} — {SKU_INVENTORY[sku]['description']}",
            f"- Safety stock: {record['safety_stock']} units",
            f"- Dynamic reorder point: {record['dynamic_reorder_point']} units",
            f"- Recommended disposition: {record['action']}",
            f"- **SIMULATED WRITE:** `INV-POLICY-{sku}` queued for Dynamics 365",
            "- Simulation only; no inventory, purchase order, or external system was mutated.",
        ])

    def _continuous_optimization(self, **kwargs) -> str:
        return "\n".join([
            "## Continuous Inventory Optimization",
            EVIDENCE_MARKER,
            "",
            "| Check | Cadence | Alert Threshold | Owner |",
            "|-------|---------|-----------------|-------|",
            "| Slow-moving inventory | Daily | >120 days on hand | Inventory Manager |",
            "| Warehouse utilization | Hourly | >90% | Distribution Lead |",
            "| Dynamic safety stock | Weekly | Forecast variance >15% | Supply Planning |",
            "| Obsolescence exposure | Monthly | Risk=high | Procurement Manager |",
            "",
            "**Success metrics:** working capital released, storage cost avoided, "
            "warehouse utilization, and stockout rate.",
        ])


# ---------------------------------------------------------------------------
# Main — exercise all operations
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = InventoryRebalancingAgent()
    print("=" * 72)
    print("EMBEDDED DEMO WAREHOUSES + LIVE TENANT SKU MASTER")
    print("+ LIVE ERP MATERIALS AND INBOUND SUPPLY (goods receipts, CRM join)")
    print("(live sections fetched over HTTP; fall back offline)")
    print("=" * 72)
    print(agent.perform(operation="inventory_snapshot"))
    print()
    for op in agent.metadata["operations"][1:]:
        print("=" * 72)
        print(agent.perform(operation=op))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
