---
name: "rar-aibast-agents-library-procurement-support"
description: "Tracks requisitions and supplier signals over a simulated Dynamics 365 tenant and ERP (POs, receipts, blocked invoices), with offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/procurement_support", "rar_sha256": "08de4f1c0f746fef3915574fb31e4a3c55a817402532f4cd58b5756dd3faebf8", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.2.0", "author": "AIBAST", "tags": ["procurement", "requisition", "contracts", "supplier", "budget"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/procurement_support`. The original RAPP
agent is preserved byte-for-byte in `procurement_support_agent.py` and in the RCI capsule.

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

Procurement Support Agent — a template you are meant to mutate.

Provides procurement support operations including requisition status
tracking, contract lookups, supplier performance scoring, and budget
checking.

The live tenant has no native "requisition" entity, so in this template
a Dynamics SALES ORDER is read from the buying side — an order your
organization has placed with the supplier Aster Lane Office Systems.
Say the same in your own mutation if you reinterpret an entity.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works from anywhere):
       CRM — Static Dynamics 365 tenant (Aster Lane Office Systems):
         https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       ERP — Static ERP (suppliers, purchase orders, goods receipts,
       supplier invoices):
         https://kody-w.github.io/static-erp/api/v1/
     Try: perform(operation="supplier_performance")
     — the embedded scorecard PLUS real per-supplier signals joined
     from live ERP documents: Orchard Signal Works shows the blocked
     invoice SINV-92003 (PO-47003) and Quarry Bend Foundry the goods
     receipt GR-88005 posted 9 days late against PO-47005.
     Also try: perform(operation="requisition_status",
     requisition_id="PO-47003") to track one live ERP PO.
  2. No network? Everything falls back to the embedded demo layer below
     (_REQUISITIONS / _CONTRACTS) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PROCUREMENT_SUPPORT_DATA_URL (CRM side) and/or
     PROCUREMENT_SUPPORT_ERP_URL (ERP side) to any endpoint with the
     same shapes, or replace _fetch_collection() with your procurement
     client. The fields the rest of the file needs are listed in
     _normalize_live_requisition() — requester and department are
     labeled "n/a — enrichment seam"; wire your HR/identity system
     there.

OPERATIONS
  requisition_status | contract_lookup | supplier_performance
  | budget_check
  kwargs: operation (required), requisition_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The procurement support operation to perform",
      "enum": [
        "requisition_status",
        "contract_lookup",
        "supplier_performance",
        "budget_check"
      ],
      "type": "string"
    },
    "requisition_id": {
      "description": "Requisition ID (e.g. 'REQ-7001')",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `procurement_support_agent.py` and embedded as the fenced Python below (sha256 08de4f1c0f746fef…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `procurement_support_agent.py` first:

```bash
python3 procurement_support_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 procurement_support_agent.py   # or on stdin
python3 procurement_support_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Procurement Support Agent — a template you are meant to mutate.

Provides procurement support operations including requisition status
tracking, contract lookups, supplier performance scoring, and budget
checking.

The live tenant has no native "requisition" entity, so in this template
a Dynamics SALES ORDER is read from the buying side — an order your
organization has placed with the supplier Aster Lane Office Systems.
Say the same in your own mutation if you reinterpret an entity.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works from anywhere):
       CRM — Static Dynamics 365 tenant (Aster Lane Office Systems):
         https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       ERP — Static ERP (suppliers, purchase orders, goods receipts,
       supplier invoices):
         https://kody-w.github.io/static-erp/api/v1/
     Try: perform(operation="supplier_performance")
     — the embedded scorecard PLUS real per-supplier signals joined
     from live ERP documents: Orchard Signal Works shows the blocked
     invoice SINV-92003 (PO-47003) and Quarry Bend Foundry the goods
     receipt GR-88005 posted 9 days late against PO-47005.
     Also try: perform(operation="requisition_status",
     requisition_id="PO-47003") to track one live ERP PO.
  2. No network? Everything falls back to the embedded demo layer below
     (_REQUISITIONS / _CONTRACTS) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PROCUREMENT_SUPPORT_DATA_URL (CRM side) and/or
     PROCUREMENT_SUPPORT_ERP_URL (ERP side) to any endpoint with the
     same shapes, or replace _fetch_collection() with your procurement
     client. The fields the rest of the file needs are listed in
     _normalize_live_requisition() — requester and department are
     labeled "n/a — enrichment seam"; wire your HR/identity system
     there.

OPERATIONS
  requisition_status | contract_lookup | supplier_performance
  | budget_check
  kwargs: operation (required), requisition_id
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/procurement_support",
    "version": "1.2.0",
    "display_name": "Procurement Support",
    "description": "Tracks requisitions and supplier signals over a simulated Dynamics 365 tenant and ERP (POs, receipts, blocked invoices), with offline fallback.",
    "author": "AIBAST",
    "tags": ["procurement", "requisition", "contracts", "supplier", "budget"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# LIVE DATA SEAM — swap this for your real systems
#
# Defaults: TWO globally hosted simulated systems (synthetic data
# served as JSON from GitHub Pages). To hook your own world, either:
#   export PROCUREMENT_SUPPORT_DATA_URL=https://your-org/api/data/v9.2
#   export PROCUREMENT_SUPPORT_ERP_URL=https://your-erp/api/v1
# or replace _fetch_collection() with your procurement client.
# Downstream code only needs the fields produced by
# _normalize_live_requisition() and _normalize_erp_requisition().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "PROCUREMENT_SUPPORT_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
ERP_SOURCE_URL = os.environ.get(
    "PROCUREMENT_SUPPORT_ERP_URL",
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
    """Rows from the live simulated ERP (suppliers, materials,
    purchase_orders, goods_receipts, supplier_invoices); [] offline."""
    return _fetch_collection(collection, base_url=ERP_SOURCE_URL)


def _normalize_live_requisition(row):
    """Project a Dynamics sales order (read from the buying side) onto
    the requisition shape this agent uses. THIS is the contract your
    replacement data source must meet — a dict with these keys. None
    means 'not available from the order alone' (enrichment seam); 0 is
    a real zero."""
    fulfilled = str(row.get("datefulfilled") or "")[:10] or None
    return {
        "id": row.get("ordernumber", row.get("salesorderid", "")),
        "title": row.get("name", "Unnamed order"),
        "requester": None,     # enrichment seam — wire your HR/identity system
        "department": None,    # enrichment seam
        "amount": float(row.get("totalamount") or 0),
        "status": row.get("statuscode@OData.Community.Display.V1.FormattedValue", "Open"),
        "created": str(row.get("createdon", ""))[:10],
        "po_number": row.get("ordernumber"),
        "supplier": "Aster Lane Office Systems",
        "delivery_date": fulfilled,
        "received_pct": 100 if fulfilled else 0,
        "_live": True,
    }


def _live_requisitions():
    """Live tenant orders as requisitions; [] when offline."""
    rows = _fetch_collection("salesorders")
    return [_normalize_live_requisition(r) for r in rows if r.get("ordernumber")]


def _normalize_erp_requisition(row, receipts):
    """Project a live ERP purchase order onto the requisition shape."""
    received = [g for g in receipts if g.get("po_number") == row.get("po_number")]
    title = "; ".join(
        str(l.get("material_description", l.get("material_number", "?")))
        for l in row.get("lines", [])
    ) or "Unnamed purchase order"
    return {
        "id": row.get("po_number", ""),
        "title": title,
        "requester": row.get("buyer_name"),
        "department": None,      # enrichment seam
        "amount": float(row.get("total_amount") or 0),
        "status": row.get("status", "open"),
        "created": str(row.get("order_date", ""))[:10],
        "po_number": row.get("po_number"),
        "supplier": row.get("supplier_name", "Unknown"),
        "delivery_date": str(received[0].get("posting_date", ""))[:10] if received else None,
        "received_pct": 100 if received else 0,
        "_live": True,
        "_erp": True,
    }


def _erp_requisitions():
    """Live ERP purchase orders as requisitions; [] when offline."""
    receipts = _erp("goods_receipts")
    return [
        _normalize_erp_requisition(r, receipts)
        for r in _erp("purchase_orders")
        if r.get("po_number")
    ]


def _erp_supplier_signals():
    """Real per-supplier risk signals joined from live ERP documents:
    purchase orders, goods receipts (late vs expected delivery), and
    supplier invoices (payment blocks). [] when the ERP is unreachable."""
    suppliers = _erp("suppliers")
    if not suppliers:
        return []
    pos = _erp("purchase_orders")
    grs = _erp("goods_receipts")
    invs = _erp("supplier_invoices")
    expected = {
        p.get("po_number"): str(p.get("expected_delivery_date", ""))[:10]
        for p in pos
    }
    signals = []
    for s in suppliers:
        name = s.get("name", "?")
        s_pos = [p for p in pos if p.get("supplier_name") == name]
        s_grs = [g for g in grs if g.get("supplier_name") == name]
        late = [
            g for g in s_grs
            if expected.get(g.get("po_number"))
            and str(g.get("posting_date", ""))[:10] > expected[g.get("po_number")]
        ]
        blocked = [
            i for i in invs
            if i.get("supplier_name") == name and i.get("payment_block")
        ]
        flags = []
        for g in late:
            flags.append(
                f"{g.get('receipt_number')} posted {str(g.get('posting_date',''))[:10]} "
                f"vs {expected.get(g.get('po_number'))} expected on {g.get('po_number')}"
            )
        for i in blocked:
            flags.append(
                f"{i.get('invoice_number')} payment-blocked on {i.get('po_number')} "
                f"(${float(i.get('total_amount') or 0):,.2f})"
            )
        signals.append({
            "name": name,
            "terms": s.get("payment_terms", "?"),
            "category": s.get("category", "?"),
            "po_count": len(s_pos),
            "receipt_count": len(s_grs),
            "late_count": len(late),
            "blocked_count": len(blocked),
            "status": "REVIEW" if (late or blocked) else "OK",
            "flags": flags,
        })
    return signals


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_REQUISITIONS = {
    "REQ-7001": {"id": "REQ-7001", "title": "Q1 Marketing Collateral Print Run", "requester": "Angela Martinez", "department": "Marketing", "amount": 18500, "status": "Approved", "created": "2025-10-28", "po_number": "PO-44201", "supplier": "PrintPro Services", "delivery_date": "2025-12-05", "received_pct": 0},
    "REQ-7002": {"id": "REQ-7002", "title": "Server Room UPS Replacement", "requester": "Frank O'Brien", "department": "IT", "amount": 42000, "status": "In Transit", "created": "2025-10-15", "po_number": "PO-44189", "supplier": "APC by Schneider Electric", "delivery_date": "2025-11-20", "received_pct": 0},
    "REQ-7003": {"id": "REQ-7003", "title": "Annual Compliance Audit Services", "requester": "Carla Dubois", "department": "Finance", "amount": 65000, "status": "Under Review", "created": "2025-11-10", "po_number": None, "supplier": "Deloitte", "delivery_date": None, "received_pct": 0},
    "REQ-7004": {"id": "REQ-7004", "title": "Ergonomic Office Chairs (50 units)", "requester": "Derek Washington", "department": "HR", "amount": 27500, "status": "Delivered", "created": "2025-09-20", "po_number": "PO-44102", "supplier": "Herman Miller", "delivery_date": "2025-10-25", "received_pct": 100},
    "REQ-7005": {"id": "REQ-7005", "title": "Cloud Security Assessment Tool", "requester": "Frank O'Brien", "department": "IT", "amount": 35000, "status": "Pending Approval", "created": "2025-11-12", "po_number": None, "supplier": "CrowdStrike", "delivery_date": None, "received_pct": 0},
}

_CONTRACTS = {
    "CTR-3001": {"id": "CTR-3001", "supplier": "AWS", "title": "Enterprise Cloud Services Agreement", "start": "2024-01-01", "end": "2026-12-31", "total_value": 2670000, "annual_value": 890000, "status": "Active", "auto_renew": True, "notice_period_days": 90, "category": "Technology"},
    "CTR-3002": {"id": "CTR-3002", "supplier": "Salesforce", "title": "CRM Enterprise License Agreement", "start": "2024-04-01", "end": "2025-03-31", "total_value": 430000, "annual_value": 430000, "status": "Renewal Due", "auto_renew": False, "notice_period_days": 60, "category": "Software"},
    "CTR-3003": {"id": "CTR-3003", "supplier": "Deloitte", "title": "Professional Services MSA", "start": "2023-06-01", "end": "2025-05-31", "total_value": 195000, "annual_value": 97500, "status": "Active", "auto_renew": True, "notice_period_days": 30, "category": "Professional Services"},
    "CTR-3004": {"id": "CTR-3004", "supplier": "Herman Miller", "title": "Furniture Supply Agreement", "start": "2024-07-01", "end": "2025-06-30", "total_value": 125000, "annual_value": 125000, "status": "Active", "auto_renew": True, "notice_period_days": 30, "category": "Office Supplies"},
    "CTR-3005": {"id": "CTR-3005", "supplier": "CrowdStrike", "title": "Endpoint Security Subscription", "start": "2025-01-01", "end": "2025-12-31", "total_value": 78000, "annual_value": 78000, "status": "Active", "auto_renew": True, "notice_period_days": 60, "category": "Security"},
}

_SUPPLIER_SCORES = {
    "AWS": {"overall": 94, "quality": 96, "delivery": 92, "responsiveness": 93, "pricing": 88, "innovation": 97, "risk_level": "Low", "total_orders": 47, "on_time_pct": 98.2},
    "Salesforce": {"overall": 87, "quality": 90, "delivery": 88, "responsiveness": 82, "pricing": 78, "innovation": 92, "risk_level": "Low", "total_orders": 12, "on_time_pct": 95.0},
    "Deloitte": {"overall": 91, "quality": 94, "delivery": 89, "responsiveness": 90, "pricing": 82, "innovation": 88, "risk_level": "Low", "total_orders": 8, "on_time_pct": 96.5},
    "Herman Miller": {"overall": 89, "quality": 95, "delivery": 85, "responsiveness": 88, "pricing": 80, "innovation": 85, "risk_level": "Low", "total_orders": 15, "on_time_pct": 92.0},
    "CrowdStrike": {"overall": 92, "quality": 95, "delivery": 94, "responsiveness": 91, "pricing": 83, "innovation": 96, "risk_level": "Low", "total_orders": 6, "on_time_pct": 100.0},
    "PrintPro Services": {"overall": 78, "quality": 80, "delivery": 72, "responsiveness": 75, "pricing": 85, "innovation": 65, "risk_level": "Medium", "total_orders": 22, "on_time_pct": 82.0},
}

_BUDGET_ALLOCATIONS = {
    "IT": {"annual_budget": 1800000, "spent": 1245000, "committed": 77000, "remaining": 478000, "q4_forecast": 320000},
    "Marketing": {"annual_budget": 650000, "spent": 482000, "committed": 18500, "remaining": 149500, "q4_forecast": 125000},
    "Finance": {"annual_budget": 400000, "spent": 275000, "committed": 65000, "remaining": 60000, "q4_forecast": 80000},
    "HR": {"annual_budget": 350000, "spent": 245000, "committed": 27500, "remaining": 77500, "q4_forecast": 55000},
    "Sales": {"annual_budget": 500000, "spent": 380000, "committed": 0, "remaining": 120000, "q4_forecast": 90000},
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _contracts_expiring_soon(days=90):
    expiring = []
    for cid, c in _CONTRACTS.items():
        if c["status"] in ("Active", "Renewal Due"):
            expiring.append(c)
    return expiring


def _budget_health():
    total_budget = sum(d["annual_budget"] for d in _BUDGET_ALLOCATIONS.values())
    total_spent = sum(d["spent"] for d in _BUDGET_ALLOCATIONS.values())
    total_committed = sum(d["committed"] for d in _BUDGET_ALLOCATIONS.values())
    return total_budget, total_spent, total_committed


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class ProcurementSupportAgent(BasicAgent):
    """
    Procurement support agent.

    Operations:
        requisition_status   - track requisition status and delivery
        contract_lookup      - look up contracts and renewal dates
        supplier_performance - view supplier performance scores
        budget_check         - check budget availability by department
    """

    def __init__(self):
        self.name = "ProcurementSupportAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "requisition_status", "contract_lookup",
                            "supplier_performance", "budget_check",
                        ],
                        "description": "The procurement support operation to perform",
                    },
                    "requisition_id": {
                        "type": "string",
                        "description": "Requisition ID (e.g. 'REQ-7001')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "requisition_status")
        dispatch = {
            "requisition_status": self._requisition_status,
            "contract_lookup": self._contract_lookup,
            "supplier_performance": self._supplier_performance,
            "budget_check": self._budget_check,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(kwargs)

    # ── requisition_status ─────────────────────────────────────
    def _requisition_status(self, params):
        query = (params.get("requisition_id") or "").upper().strip()
        live = _live_requisitions()
        erp = _erp_requisitions() if query.startswith("PO-") else []
        if query.startswith("REQ-") and query in _REQUISITIONS:
            reqs, source = [_REQUISITIONS[query]], "embedded demo layer (simulated)"
        elif query and any(r["id"] == query for r in erp):
            reqs = [r for r in erp if r["id"] == query]
            source = "LIVE purchase order from the simulated ERP (real supplier, receipt, and invoice joins)"
        elif query and any(r["id"] == query for r in live):
            reqs = [r for r in live if r["id"] == query]
            source = "LIVE order from the Aster Lane Dynamics 365 tenant (read as a requisition)"
        elif live:
            reqs, source = live, "LIVE orders from the Aster Lane Dynamics 365 tenant (read as requisitions)"
        else:
            reqs, source = list(_REQUISITIONS.values()), "embedded demo layer (simulated — live tenant unreachable)"
        rows = ""
        for req in reqs:
            po = req["po_number"] or "Pending"
            rows += f"| {req['id']} | {req['title'][:35]} | ${req['amount']:,.0f} | {req['status']} | {po} | {req['supplier']} |\n"
        delivered = sum(1 for r in reqs if r["received_pct"] == 100)
        in_flight = len(reqs) - delivered
        return (
            f"**Requisition Status Dashboard**\n\n"
            f"| ID | Title | Amount | Status | PO# | Supplier |\n|---|---|---|---|---|---|\n"
            f"{rows}\n"
            f"**Status Summary:**\n"
            f"- Delivered/received: {delivered}\n"
            f"- In flight: {in_flight}\n"
            f"- Total tracked spend: ${sum(r['amount'] for r in reqs):,.0f}\n\n"
            f"Record source: {source}\n"
            f"Source: [Procurement System + ERP]\nAgents: ProcurementSupportAgent"
        )

    # ── contract_lookup ────────────────────────────────────────
    def _contract_lookup(self, params):
        rows = ""
        for c in _CONTRACTS.values():
            auto = "Yes" if c["auto_renew"] else "No"
            rows += f"| {c['id']} | {c['supplier']} | {c['title'][:30]} | ${c['annual_value']:,} | {c['end']} | {c['status']} | {auto} |\n"
        renewal_count = sum(1 for c in _CONTRACTS.values() if c["status"] == "Renewal Due")
        total_value = sum(c["annual_value"] for c in _CONTRACTS.values())
        return (
            f"**Contract Portfolio** (embedded demo data — simulated)\n\n"
            f"| ID | Supplier | Title | Annual Value | End Date | Status | Auto-Renew |\n|---|---|---|---|---|---|---|\n"
            f"{rows}\n"
            f"**Summary:**\n"
            f"- Active contracts: {len(_CONTRACTS)}\n"
            f"- Total annual value: ${total_value:,}\n"
            f"- Renewals due: {renewal_count}\n\n"
            f"Source: [Contract Management System]\nAgents: ProcurementSupportAgent"
        )

    # ── supplier_performance ───────────────────────────────────
    def _supplier_performance(self, params):
        rows = ""
        for name, s in sorted(_SUPPLIER_SCORES.items(), key=lambda x: x[1]["overall"], reverse=True):
            rows += f"| {name} | {s['overall']} | {s['quality']} | {s['delivery']} | {s['responsiveness']} | {s['pricing']} | {s['risk_level']} | {s['on_time_pct']}% |\n"
        live = _live_requisitions()
        if live:
            fulfilled = sum(1 for r in live if r["received_pct"] == 100)
            live_line = (
                f"\n**Live supplier snapshot (Aster Lane Office Systems, from the LIVE tenant):** "
                f"{len(live)} orders on record, {fulfilled} fulfilled. Quality/responsiveness "
                "scores are an enrichment seam — wire your supplier scorecard system.\n"
            )
        else:
            live_line = "\n**Live supplier snapshot:** live tenant unreachable — embedded demo data only.\n"
        signals = _erp_supplier_signals()
        if signals:
            erp_rows = ""
            erp_flags = []
            for s in signals:
                erp_rows += (
                    f"| {s['name']} | {s['category']} | {s['terms']} | {s['po_count']} | "
                    f"{s['receipt_count']} | {s['late_count']} | {s['blocked_count']} | {s['status']} |\n"
                )
                erp_flags.extend(f"- {s['name']}: {f}" for f in s["flags"])
            erp_block = (
                "\n**Live ERP Supplier Signals** (joined from LIVE ERP POs, goods receipts, and invoices):\n\n"
                "| Supplier | Category | Terms | POs | Receipts | Late Receipts | Blocked Invoices | Signal |\n"
                "|---|---|---|---|---|---|---|---|\n"
                f"{erp_rows}\n"
                + ("**ERP Exceptions:**\n" + "\n".join(erp_flags) + "\n" if erp_flags else "")
            )
        else:
            erp_block = "\n**Live ERP supplier signals:** ERP unreachable — embedded demo data only.\n"
        return (
            f"**Supplier Performance Scorecard** (embedded demo scores — simulated)\n\n"
            f"| Supplier | Overall | Quality | Delivery | Response | Pricing | Risk | On-Time |\n|---|---|---|---|---|---|---|---|\n"
            f"{rows}\n"
            f"**Scoring Methodology:** Weighted composite (Quality 30%, Delivery 25%, Responsiveness 20%, Pricing 15%, Innovation 10%)\n"
            f"{live_line}"
            f"{erp_block}\n"
            f"**Alerts:**\n"
            f"- PrintPro Services: Below 80 overall - consider alternative suppliers\n"
            f"- All strategic suppliers (AWS, Salesforce) maintaining 87+ scores\n\n"
            f"Source: [Supplier Management System + Live Dynamics 365 Tenant + Live ERP]\nAgents: ProcurementSupportAgent"
        )

    # ── budget_check ───────────────────────────────────────────
    def _budget_check(self, params):
        total_budget, total_spent, total_committed = _budget_health()
        total_remaining = total_budget - total_spent - total_committed
        rows = ""
        for dept, b in _BUDGET_ALLOCATIONS.items():
            util = (b["spent"] + b["committed"]) / b["annual_budget"] * 100
            status = "Over" if b["remaining"] < 0 else ("At Risk" if util > 85 else "On Track")
            rows += f"| {dept} | ${b['annual_budget']:,} | ${b['spent']:,} | ${b['committed']:,} | ${b['remaining']:,} | {util:.0f}% | {status} |\n"
        return (
            f"**Budget Check** (embedded demo data — simulated)\n\n"
            f"| Metric | Value |\n|---|---|\n"
            f"| Total Budget | ${total_budget:,} |\n"
            f"| Spent YTD | ${total_spent:,} ({total_spent/total_budget*100:.0f}%) |\n"
            f"| Committed | ${total_committed:,} |\n"
            f"| Remaining | ${total_remaining:,} |\n\n"
            f"**By Department:**\n\n"
            f"| Department | Budget | Spent | Committed | Remaining | Utilization | Status |\n|---|---|---|---|---|---|---|\n"
            f"{rows}\n"
            f"**Alerts:**\n"
            f"- Finance department at risk: Q4 forecast ($80K) exceeds remaining ($60K)\n"
            f"- IT has sufficient budget for planned Q4 purchases\n\n"
            f"Source: [ERP + Finance System]\nAgents: ProcurementSupportAgent"
        )


if __name__ == "__main__":
    agent = ProcurementSupportAgent()
    print("=" * 60)
    print("EMBEDDED DEMO REQUISITION (works offline)")
    print(agent.perform(operation="requisition_status", requisition_id="REQ-7001"))
    print()
    print("=" * 60)
    print("LIVE TENANT REQUISITIONS (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="requisition_status"))
    print()
    print("=" * 60)
    print("LIVE ERP PURCHASE ORDER (blocked-invoice PO; falls back offline)")
    print(agent.perform(operation="requisition_status", requisition_id="PO-47003"))
    print()
    print("=" * 60)
    print("SUPPLIER PERFORMANCE + LIVE ERP SIGNALS (late receipts, blocked invoices)")
    print(agent.perform(operation="supplier_performance"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
