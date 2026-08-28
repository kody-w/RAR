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
