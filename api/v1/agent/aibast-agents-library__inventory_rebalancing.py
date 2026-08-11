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
