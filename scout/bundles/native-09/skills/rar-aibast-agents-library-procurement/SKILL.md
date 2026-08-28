---
name: "rar-aibast-agents-library-procurement"
description: "Routes purchase requests over a simulated Dynamics 365 tenant and ERP, flagging three-way-match breaks and blocked invoices, with offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/procurement_agent", "rar_sha256": "ec4e120ce732fa89bfc0a35f445944aa0b9fc8749b867d715eb143dab917a2aa", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.3.0", "author": "AIBAST", "tags": ["procurement", "purchasing", "vendor", "approval", "spend-analysis"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/procurement_agent`. The original RAPP
agent is preserved byte-for-byte in `procurement_agent.py` and in the RCI capsule.

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

Procurement Agent — a template you are meant to mutate.

Manages purchase requests, vendor comparisons, approval routing, and
spend analysis for organizational procurement workflows.

The live tenant has no native "purchase requisition" entity, so in this
template a Dynamics SALES ORDER is read from the buying side — an order
your organization has placed with the supplier Aster Lane Office
Systems. Say the same in your own mutation if you reinterpret an entity.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works from anywhere):
       CRM — Static Dynamics 365 tenant (Aster Lane Office Systems):
         https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       ERP — Static ERP (suppliers, purchase orders, goods receipts,
       supplier invoices):
         https://kody-w.github.io/static-erp/api/v1/
     Try: perform(operation="purchase_request", request_id="PO-47003")
     — a real ERP purchase order (Orchard Signal Works print heads)
     joined to its goods receipt GR-88003 and invoice SINV-92003: the
     three-way match BREAKS (36 received vs 40 invoiced) and the
     payment-blocked invoice is flagged automatically.
  2. No network? Everything falls back to the embedded demo layer below
     (_PURCHASE_REQUESTS / _VENDOR_CATALOG) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PROCUREMENT_AGENT_DATA_URL (CRM side) and/or
     PROCUREMENT_AGENT_ERP_URL (ERP side) to any endpoint with the same
     shapes, or replace _fetch_collection() with your procurement
     client. The fields the rest of the file needs are listed in
     _normalize_live_request() / _normalize_erp_po() — requester,
     department, and budget code are labeled "n/a — enrichment seam";
     wire your HR and finance systems there.

OPERATIONS
  purchase_request | vendor_comparison | approval_routing
  | spend_analysis | optimal_vendor | create_purchase_order
  | approval_reminders | create_rfq | duplicate_license_check
  kwargs: operation (required), request_id (embedded 'PR-5001' or live
  'ORD-260100'), vendor_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The procurement operation to perform",
      "enum": [
        "purchase_request",
        "vendor_comparison",
        "approval_routing",
        "spend_analysis",
        "optimal_vendor",
        "create_purchase_order",
        "approval_reminders",
        "create_rfq",
        "duplicate_license_check"
      ],
      "type": "string"
    },
    "request_id": {
      "description": "Purchase request ID (e.g. 'PR-5001')",
      "type": "string"
    },
    "vendor_id": {
      "description": "Optional approved office-furniture vendor ID for create_purchase_order",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `procurement_agent.py` and embedded as the fenced Python below (sha256 ec4e120ce732fa89…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `procurement_agent.py` first:

```bash
python3 procurement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 procurement_agent.py   # or on stdin
python3 procurement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Procurement Agent — a template you are meant to mutate.

Manages purchase requests, vendor comparisons, approval routing, and
spend analysis for organizational procurement workflows.

The live tenant has no native "purchase requisition" entity, so in this
template a Dynamics SALES ORDER is read from the buying side — an order
your organization has placed with the supplier Aster Lane Office
Systems. Say the same in your own mutation if you reinterpret an entity.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works from anywhere):
       CRM — Static Dynamics 365 tenant (Aster Lane Office Systems):
         https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       ERP — Static ERP (suppliers, purchase orders, goods receipts,
       supplier invoices):
         https://kody-w.github.io/static-erp/api/v1/
     Try: perform(operation="purchase_request", request_id="PO-47003")
     — a real ERP purchase order (Orchard Signal Works print heads)
     joined to its goods receipt GR-88003 and invoice SINV-92003: the
     three-way match BREAKS (36 received vs 40 invoiced) and the
     payment-blocked invoice is flagged automatically.
  2. No network? Everything falls back to the embedded demo layer below
     (_PURCHASE_REQUESTS / _VENDOR_CATALOG) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     PROCUREMENT_AGENT_DATA_URL (CRM side) and/or
     PROCUREMENT_AGENT_ERP_URL (ERP side) to any endpoint with the same
     shapes, or replace _fetch_collection() with your procurement
     client. The fields the rest of the file needs are listed in
     _normalize_live_request() / _normalize_erp_po() — requester,
     department, and budget code are labeled "n/a — enrichment seam";
     wire your HR and finance systems there.

OPERATIONS
  purchase_request | vendor_comparison | approval_routing
  | spend_analysis | optimal_vendor | create_purchase_order
  | approval_reminders | create_rfq | duplicate_license_check
  kwargs: operation (required), request_id (embedded 'PR-5001' or live
  'ORD-260100'), vendor_id
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
    "name": "@aibast-agents-library/procurement_agent",
    "version": "1.3.0",
    "display_name": "Procurement Agent",
    "description": "Routes purchase requests over a simulated Dynamics 365 tenant and ERP, flagging three-way-match breaks and blocked invoices, with offline fallback.",
    "author": "AIBAST",
    "tags": ["procurement", "purchasing", "vendor", "approval", "spend-analysis"],
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
#   export PROCUREMENT_AGENT_DATA_URL=https://your-org/api/data/v9.2
#   export PROCUREMENT_AGENT_ERP_URL=https://your-erp/api/v1
# or replace _fetch_collection() with your procurement client.
# Downstream code only needs the fields produced by
# _normalize_live_request() and _normalize_erp_po().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "PROCUREMENT_AGENT_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
ERP_SOURCE_URL = os.environ.get(
    "PROCUREMENT_AGENT_ERP_URL",
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


def _normalize_live_request(row):
    """Project a Dynamics sales order (read from the buying side) onto
    the purchase-request shape this agent uses. THIS is the contract
    your replacement data source must meet — a dict with these keys.
    None means 'not available from the order alone' and renderers label
    it as an enrichment seam."""
    return {
        "id": row.get("ordernumber", row.get("salesorderid", "")),
        "title": row.get("name", "Unnamed order"),
        "requester": None,       # enrichment seam — wire your HR/identity system
        "department": None,      # enrichment seam
        "category": "Office Systems",
        "amount": float(row.get("totalamount") or 0),
        "priority": None,        # enrichment seam — wire your intake workflow
        "status": row.get("statuscode@OData.Community.Display.V1.FormattedValue", "Open"),
        "vendor_preferred": "Aster Lane Office Systems",
        "justification": row.get("description", ""),
        "budget_code": None,     # enrichment seam — wire your finance system
        "discount": float(row.get("discountamount") or 0),
        "_live": True,
    }


def _live_requests():
    """ordernumber-keyed dict of live tenant orders; {} when offline."""
    rows = _fetch_collection("salesorders")
    return {
        r["id"]: r
        for r in (_normalize_live_request(row) for row in rows)
        if r["id"]
    }


def _normalize_erp_po(row):
    """Project a live ERP purchase order onto the purchase-request shape
    this agent uses. buyer_name is a REAL field here — only department,
    priority, and budget code stay enrichment seams."""
    lines = row.get("lines", [])
    title = "; ".join(
        str(l.get("material_description", l.get("material_number", "?")))
        for l in lines
    ) or "Unnamed purchase order"
    return {
        "id": row.get("po_number", ""),
        "title": title,
        "requester": row.get("buyer_name"),
        "department": None,      # enrichment seam
        "category": "Direct Materials",
        "amount": float(row.get("total_amount") or 0),
        "priority": None,        # enrichment seam
        "status": row.get("status", "open"),
        "vendor_preferred": row.get("supplier_name", "Unknown"),
        "justification": f"ERP purchase order for plant {row.get('plant', '?')}, "
                         f"expected delivery {str(row.get('expected_delivery_date', ''))[:10] or 'n/a'}",
        "budget_code": None,     # enrichment seam
        "discount": 0.0,
        "_live": True,
        "_erp": True,
    }


def _erp_purchase_orders():
    """po_number-keyed dict of live ERP purchase orders; {} offline."""
    return {
        r["id"]: r
        for r in (_normalize_erp_po(row) for row in _erp("purchase_orders"))
        if r["id"]
    }


def _erp_three_way_block(po_number):
    """Render the three-way match for one ERP PO — PO lines vs goods
    receipts vs supplier invoices, joined on po_number/material_number.
    Returns '' when the ERP is unreachable or the PO has no documents."""
    grs = [g for g in _erp("goods_receipts") if g.get("po_number") == po_number]
    invs = [i for i in _erp("supplier_invoices") if i.get("po_number") == po_number]
    po = next(
        (p for p in _erp("purchase_orders") if p.get("po_number") == po_number),
        None,
    )
    if po is None:
        return ""
    ordered, received, invoiced = {}, {}, {}
    for l in po.get("lines", []):
        m = l.get("material_number", "?")
        ordered[m] = ordered.get(m, 0) + int(float(l.get("quantity") or 0))
    for g in grs:
        for l in g.get("lines", []):
            m = l.get("material_number", "?")
            received[m] = received.get(m, 0) + int(float(l.get("quantity_received") or 0))
    for i in invs:
        for l in i.get("lines", []):
            m = l.get("material_number", "?")
            invoiced[m] = invoiced.get(m, 0) + int(float(l.get("quantity_invoiced") or 0))
    rows, flags = "", []
    for m in ordered:
        o, r, v = ordered[m], received.get(m, 0), invoiced.get(m, 0)
        result = "MATCH" if o == r == v else "**BREAK**"
        rows += f"| {m} | {o} | {r} | {v} | {result} |\n"
        if o != r or o != v:
            flags.append(
                f"- **Match break** on {m}: ordered {o}, received {r}, invoiced {v}."
            )
    for i in invs:
        if i.get("payment_block"):
            flags.append(
                f"- **Invoice {i.get('invoice_number')} is PAYMENT BLOCKED** "
                f"(status `{i.get('status')}`, ${float(i.get('total_amount') or 0):,.2f}, "
                f"due {str(i.get('due_date', ''))[:10]}). Resolve the quantity "
                "discrepancy before releasing payment."
            )
    docs = ", ".join(
        [g.get("receipt_number", "?") for g in grs]
        + [i.get("invoice_number", "?") for i in invs]
    ) or "none posted yet"
    return (
        "**Three-Way Match (LIVE ERP):** documents {docs}\n\n"
        "| Material | Ordered | Received | Invoiced | Result |\n|---|---|---|---|---|\n"
        "{rows}\n"
        "{flags}\n"
    ).format(
        docs=docs,
        rows=rows.rstrip("\n"),
        flags="\n".join(flags) if flags else "All lines match — clear to pay.",
    )


def _na(value):
    """None = the order alone can't know this (enrichment seam)."""
    return "n/a — enrichment seam" if value is None else value


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_PURCHASE_REQUESTS = {
    "PR-5001": {"id": "PR-5001", "title": "Cloud Infrastructure Upgrade", "requester": "Sarah Chen", "department": "IT", "category": "Technology", "amount": 125000, "priority": "High", "status": "Pending Approval", "vendor_preferred": "AWS", "justification": "Current infrastructure at 92% capacity, scaling needed for Q1 growth", "budget_code": "IT-INFRA-2025"},
    "PR-5002": {"id": "PR-5002", "title": "Office Furniture - New Floor Build-Out", "requester": "Tom Rivera", "department": "Facilities", "category": "Office Supplies", "amount": 48500, "priority": "Medium", "status": "Vendor Selection", "vendor_preferred": "Steelcase", "justification": "5th floor build-out for 30 new employees starting Q2", "budget_code": "FAC-CAPEX-2025"},
    "PR-5003": {"id": "PR-5003", "title": "Annual Software License Renewal - Salesforce", "requester": "Mike Torres", "department": "Sales", "category": "Software", "amount": 215000, "priority": "High", "status": "Approved", "vendor_preferred": "Salesforce", "justification": "Annual enterprise license renewal, 200 seats", "budget_code": "SALES-SW-2025"},
    "PR-5004": {"id": "PR-5004", "title": "Employee Training Program - Leadership Development", "requester": "Lisa Park", "department": "HR", "category": "Professional Services", "amount": 35000, "priority": "Low", "status": "Draft", "vendor_preferred": "FranklinCovey", "justification": "Q2 leadership development program for 25 managers", "budget_code": "HR-TRAIN-2025"},
}

_VENDOR_CATALOG = {
    "VND-001": {"name": "AWS", "category": "Cloud Infrastructure", "contract_status": "Active", "tier": "Strategic", "rating": 4.7, "annual_spend": 890000, "payment_terms": "Net 30", "contact": "Enterprise Account Manager"},
    "VND-002": {"name": "Salesforce", "category": "CRM Software", "contract_status": "Active", "tier": "Strategic", "rating": 4.5, "annual_spend": 430000, "payment_terms": "Annual Prepay", "contact": "Customer Success Manager"},
    "VND-003": {"name": "Steelcase", "category": "Office Furniture", "contract_status": "Active", "tier": "Preferred", "rating": 4.3, "annual_spend": 125000, "payment_terms": "Net 45", "contact": "Account Representative"},
    "VND-004": {"name": "Herman Miller", "category": "Office Furniture", "contract_status": "Active", "tier": "Approved", "rating": 4.6, "annual_spend": 85000, "payment_terms": "Net 30", "contact": "Regional Sales"},
    "VND-005": {"name": "Azure", "category": "Cloud Infrastructure", "contract_status": "Active", "tier": "Strategic", "rating": 4.6, "annual_spend": 650000, "payment_terms": "Net 30", "contact": "Technical Account Manager"},
    "VND-006": {"name": "FranklinCovey", "category": "Training Services", "contract_status": "Active", "tier": "Approved", "rating": 4.2, "annual_spend": 45000, "payment_terms": "Net 30", "contact": "Program Director"},
}

_APPROVAL_THRESHOLDS = [
    {"max_amount": 5000, "approver": "Direct Manager", "sla_hours": 4},
    {"max_amount": 25000, "approver": "Department Head", "sla_hours": 8},
    {"max_amount": 100000, "approver": "VP Finance", "sla_hours": 24},
    {"max_amount": 500000, "approver": "CFO", "sla_hours": 48},
    {"max_amount": 999999999, "approver": "CEO + Board", "sla_hours": 120},
]

_SPEND_CATEGORIES = {
    "Technology": {"budget": 2500000, "spent_ytd": 1875000, "committed": 340000, "available": 285000, "trend": "+12% YoY"},
    "Software": {"budget": 800000, "spent_ytd": 645000, "committed": 215000, "available": -60000, "trend": "+18% YoY"},
    "Office Supplies": {"budget": 350000, "spent_ytd": 210000, "committed": 48500, "available": 91500, "trend": "-5% YoY"},
    "Professional Services": {"budget": 500000, "spent_ytd": 325000, "committed": 35000, "available": 140000, "trend": "+8% YoY"},
    "Travel": {"budget": 200000, "spent_ytd": 142000, "committed": 18000, "available": 40000, "trend": "-15% YoY"},
}

_OFFICE_FURNITURE_QUOTES = {
    "VND-003": {"unit_price": 1425, "volume_discount_pct": 12, "delivery_days": 4, "contract_compliant": True},
    "VND-004": {"unit_price": 1510, "volume_discount_pct": 15, "delivery_days": 7, "contract_compliant": True},
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _get_approval_level(amount):
    for threshold in _APPROVAL_THRESHOLDS:
        if amount <= threshold["max_amount"]:
            return threshold
    return _APPROVAL_THRESHOLDS[-1]


def _resolve_request(request_id):
    """Embedded demo requests first, then live tenant orders, then live
    ERP purchase orders. Returns (request, is_live) or (None, False)."""
    if request_id in _PURCHASE_REQUESTS:
        return _PURCHASE_REQUESTS[request_id], False
    live = _live_requests()
    if request_id in live:
        return live[request_id], True
    erp = _erp_purchase_orders()
    if request_id in erp:
        return erp[request_id], True
    return None, False


def _known_request_ids():
    ids = sorted(_PURCHASE_REQUESTS)
    live = sorted(_live_requests()) + sorted(_erp_purchase_orders())
    return ", ".join(ids + live) if live else ", ".join(ids)


def _find_competing_vendors(category):
    return [v for v in _VENDOR_CATALOG.values() if category.lower() in v["category"].lower()]


def _total_spend_summary():
    total_budget = sum(c["budget"] for c in _SPEND_CATEGORIES.values())
    total_spent = sum(c["spent_ytd"] for c in _SPEND_CATEGORIES.values())
    total_committed = sum(c["committed"] for c in _SPEND_CATEGORIES.values())
    return total_budget, total_spent, total_committed


def _rank_office_furniture_vendors(quantity=30):
    ranked = []
    for vendor_id, quote in _OFFICE_FURNITURE_QUOTES.items():
        vendor = _VENDOR_CATALOG[vendor_id]
        gross = quote["unit_price"] * quantity
        net = gross * (1 - quote["volume_discount_pct"] / 100)
        score = vendor["rating"] * 20 - quote["delivery_days"] - net / 10000
        ranked.append({
            "score": score,
            "vendor_id": vendor_id,
            "vendor": vendor,
            "quote": quote,
            "gross": gross,
            "net": net,
        })
    return sorted(ranked, key=lambda item: (-item["score"], item["vendor_id"]))


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class ProcurementAgent(BasicAgent):
    """
    Procurement management agent.

    Operations:
        purchase_request   - create and view purchase requests
        vendor_comparison  - compare vendors for a category
        approval_routing   - determine approval path for a request
        spend_analysis     - analyze spend by category and budget
        optimal_vendor     - apply contract terms and rank approved vendors
        create_purchase_order - preview a discounted PO and approval route
        approval_reminders - prepare Teams reminders for approvers
        create_rfq         - simulate RFQ distribution and response tracking
        duplicate_license_check - flag overlapping software entitlements
    """

    def __init__(self):
        self.name = "ProcurementAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "purchase_request", "vendor_comparison",
                            "approval_routing", "spend_analysis",
                            "optimal_vendor", "create_purchase_order",
                            "approval_reminders", "create_rfq",
                            "duplicate_license_check",
                        ],
                        "description": "The procurement operation to perform",
                    },
                    "request_id": {
                        "type": "string",
                        "description": "Purchase request ID (e.g. 'PR-5001')",
                    },
                    "vendor_id": {
                        "type": "string",
                        "description": "Optional approved office-furniture vendor ID for create_purchase_order",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "purchase_request")
        dispatch = {
            "purchase_request": self._purchase_request,
            "vendor_comparison": self._vendor_comparison,
            "approval_routing": self._approval_routing,
            "spend_analysis": self._spend_analysis,
            "optimal_vendor": self._optimal_vendor,
            "create_purchase_order": self._create_purchase_order,
            "approval_reminders": self._approval_reminders,
            "create_rfq": self._create_rfq,
            "duplicate_license_check": self._duplicate_license_check,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(kwargs)

    # ── purchase_request ───────────────────────────────────────
    def _purchase_request(self, params):
        req_id = params.get("request_id") or "PR-5001"
        pr, is_live = _resolve_request(req_id)
        if pr is None:
            return (
                f"**Error:** Unknown request_id `{req_id}`. "
                f"Available request IDs: {_known_request_ids()}."
            )
        approval = _get_approval_level(pr["amount"])
        if pr.get("_erp"):
            source = "Record source: LIVE purchase order from the simulated ERP"
        elif is_live:
            source = "Record source: LIVE order from the Aster Lane Dynamics 365 tenant (read as a purchase request)"
        else:
            source = "Record source: embedded demo layer (simulated)"
        match_block = ""
        if pr.get("_erp"):
            rendered = _erp_three_way_block(pr["id"])
            if rendered:
                match_block = rendered + "\n"
        return (
            f"**Purchase Request: {pr['id']}**\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Title | {pr['title']} |\n"
            f"| Requester | {_na(pr['requester'])} ({_na(pr['department'])}) |\n"
            f"| Category | {pr['category']} |\n"
            f"| Amount | ${pr['amount']:,.0f} |\n"
            f"| Priority | {_na(pr['priority'])} |\n"
            f"| Status | {pr['status']} |\n"
            f"| Preferred Vendor | {pr['vendor_preferred']} |\n"
            f"| Budget Code | {_na(pr['budget_code'])} |\n"
            f"| Required Approver | {approval['approver']} |\n\n"
            f"**Justification:** {pr['justification']}\n\n"
            f"{match_block}"
            f"{source}\n"
            f"Source: [Procurement System]\nAgents: ProcurementAgent"
        )

    # ── vendor_comparison ──────────────────────────────────────
    def _vendor_comparison(self, params):
        rows = ""
        for vid, v in _VENDOR_CATALOG.items():
            rows += f"| {vid} | {v['name']} | {v['category']} | {v['tier']} | {v['rating']}/5 | ${v['annual_spend']:,} | {v['payment_terms']} |\n"
        return (
            f"**Vendor Comparison** (embedded demo data — simulated)\n\n"
            f"| ID | Vendor | Category | Tier | Rating | Annual Spend | Terms |\n|---|---|---|---|---|---|---|\n"
            f"{rows}\n"
            f"**Vendor Tiers:**\n"
            f"- Strategic: Long-term partners, best pricing, dedicated support\n"
            f"- Preferred: Competitive pricing, standard support, pre-approved\n"
            f"- Approved: Vetted and available, standard terms\n\n"
            f"Source: [Vendor Management System]\nAgents: ProcurementAgent"
        )

    # ── approval_routing ───────────────────────────────────────
    def _approval_routing(self, params):
        req_id = params.get("request_id") or "PR-5001"
        pr, is_live = _resolve_request(req_id)
        if pr is None:
            return (
                f"**Error:** Unknown request_id `{req_id}`. "
                f"Available request IDs: {_known_request_ids()}."
            )
        approval = _get_approval_level(pr["amount"])
        threshold_rows = ""
        for t in _APPROVAL_THRESHOLDS:
            limit = f"${t['max_amount']:,}" if t["max_amount"] < 999999999 else "Unlimited"
            marker = " <-- This request" if t == approval else ""
            threshold_rows += f"| Up to {limit} | {t['approver']} | {t['sla_hours']}h |{marker}\n"
        source = (
            "Record source: LIVE order from the Aster Lane Dynamics 365 tenant"
            if is_live else
            "Record source: embedded demo layer (simulated)"
        )
        return (
            f"**Approval Routing: {pr['id']}**\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Request | {pr['title']} |\n"
            f"| Amount | ${pr['amount']:,.0f} |\n"
            f"| Required Approver | {approval['approver']} |\n"
            f"| Approval SLA | {approval['sla_hours']} hours |\n"
            f"| Current Status | {pr['status']} |\n\n"
            f"**Approval Thresholds:**\n\n"
            f"| Amount Limit | Approver | SLA |\n|---|---|---|\n"
            f"{threshold_rows}\n"
            f"{source}\n"
            f"Source: [Approval Workflow Engine]\nAgents: ProcurementAgent"
        )

    # ── spend_analysis ─────────────────────────────────────────
    def _spend_analysis(self, params):
        total_budget, total_spent, total_committed = _total_spend_summary()
        total_available = total_budget - total_spent - total_committed
        cat_rows = ""
        for cat, data in _SPEND_CATEGORIES.items():
            utilization = (data["spent_ytd"] + data["committed"]) / data["budget"] * 100
            status = "Over Budget" if data["available"] < 0 else ("At Risk" if utilization > 85 else "On Track")
            cat_rows += f"| {cat} | ${data['budget']:,} | ${data['spent_ytd']:,} | ${data['committed']:,} | ${data['available']:,} | {status} | {data['trend']} |\n"
        live = _live_requests()
        live_total = sum(r["amount"] for r in live.values())
        live_line = (
            f"**Live tenant order book:** {len(live)} orders totaling ${live_total:,.0f} "
            "with supplier Aster Lane Office Systems (LIVE Dynamics 365 tenant).\n\n"
            if live else
            "**Live tenant order book:** live tenant unreachable — embedded demo data only.\n\n"
        )
        return (
            f"**Spend Analysis** (budget book is embedded demo data — simulated)\n\n"
            f"| Metric | Value |\n|---|---|\n"
            f"| Total Budget | ${total_budget:,} |\n"
            f"| Spent YTD | ${total_spent:,} ({total_spent/total_budget*100:.0f}%) |\n"
            f"| Committed | ${total_committed:,} |\n"
            f"| Available | ${total_available:,} |\n\n"
            f"**By Category:**\n\n"
            f"| Category | Budget | Spent YTD | Committed | Available | Status | Trend |\n|---|---|---|---|---|---|---|\n"
            f"{cat_rows}\n"
            f"{live_line}"
            f"**Alerts:**\n"
            f"- Software category over budget by $60,000 - requires reallocation\n"
            f"- Technology committed spend approaching budget limit\n\n"
            f"Source: [ERP + Finance System + Live Dynamics 365 Tenant]\nAgents: ProcurementAgent"
        )

    def _optimal_vendor(self, params):
        quantity = 30
        ranked = _rank_office_furniture_vendors(quantity)
        rows = "\n".join(
            f"| {item['vendor_id']} | {item['vendor']['name']} | {item['vendor']['rating']}/5 | "
            f"{item['quote']['volume_discount_pct']}% | {item['quote']['delivery_days']} days | "
            f"${item['net']:,.0f} | {'Yes' if item['quote']['contract_compliant'] else 'No'} |"
            for item in ranked
        )
        winner = ranked[0]
        return (
            "**Optimal Approved Vendor** (embedded demo data — simulated)\n\n"
            "| Vendor ID | Vendor | Rating | Volume Discount | Delivery | Net Cost | Contract Compliant |\n"
            "|---|---|---|---|---|---|---|\n" + rows
            + f"\n\n**Recommendation:** {winner['vendor']['name']} ({winner['vendor_id']}) for best combined "
              "contract value, delivery timing, and performance.\n\n"
              "Source: [Dynamics 365 Vendor Master + Contract Terms]\nAgents: ProcurementAgent"
        )

    def _create_purchase_order(self, params):
        request_id = params.get("request_id") or "PR-5002"
        if request_id not in _PURCHASE_REQUESTS:
            return (
                f"**Error:** Unknown request_id `{request_id}`. "
                f"Available request IDs: {', '.join(sorted(_PURCHASE_REQUESTS))}."
            )
        pr = _PURCHASE_REQUESTS[request_id]
        if pr["category"] != "Office Supplies":
            return (
                f"**Error:** Request `{request_id}` has category `{pr['category']}` and is "
                "incompatible with the approved office-furniture quote set. "
                "Use request_id `PR-5002`."
            )
        ranked = _rank_office_furniture_vendors(30)
        vendor_id = params.get("vendor_id") or ranked[0]["vendor_id"]
        if vendor_id not in _OFFICE_FURNITURE_QUOTES:
            return (
                f"**Error:** Unknown or ineligible office-furniture vendor_id `{vendor_id}`. "
                f"Available vendor IDs: {', '.join(sorted(_OFFICE_FURNITURE_QUOTES))}."
            )
        vendor = _VENDOR_CATALOG[vendor_id]
        quote = _OFFICE_FURNITURE_QUOTES[vendor_id]
        gross = quote["unit_price"] * 30
        discount = gross * quote["volume_discount_pct"] / 100
        total = gross - discount
        approval = _get_approval_level(total)
        return (
            f"**Purchase Order Preview for {pr['id']}** (embedded demo data — simulated)\n\n"
            f"- Vendor: {vendor['name']} ({vendor_id})\n"
            "- Bundle: 30 ergonomic workstation packages\n"
            f"- Gross: ${gross:,}\n"
            f"- Volume discount: {quote['volume_discount_pct']}% (${discount:,.0f})\n"
            f"- PO total: ${total:,.0f}\n"
            f"- Budget check: Within {pr['budget_code']}\n"
            f"- Approval route: {approval['approver']} ({approval['sla_hours']}h SLA)\n\n"
            "Dry-run receipt: no Dynamics 365 PO or approval was created.\n\n"
            "Source: [Dynamics 365 Procurement + Microsoft Teams]\nAgents: ProcurementAgent"
        )

    def _approval_reminders(self, params):
        request_id = params.get("request_id") or "PR-5002"
        pr, is_live = _resolve_request(request_id)
        if pr is None:
            return (
                f"**Error:** Unknown request_id `{request_id}`. "
                f"Available request IDs: {_known_request_ids()}."
            )
        approval = _get_approval_level(pr["amount"])
        return (
            f"**Approval Reminder Preview: {pr['id']}**\n\n"
            f"- Approver: {approval['approver']}\n"
            f"- Teams reminders: 8 hours and 2 hours before the {approval['sla_hours']}h SLA\n"
            f"- Escalation: Finance Operations at SLA breach\n"
            f"- Status: Prepared, not sent\n\n"
            "Source: [Microsoft Teams + Dynamics 365]\nAgents: ProcurementAgent"
        )

    def _create_rfq(self, params):
        rows = "\n".join(
            f"| {vendor_id} | {vendor['name']} | Prepared | 2025-11-24 | "
            f"Price, delivery, warranty, sustainability |"
            for vendor_id, vendor in _VENDOR_CATALOG.items()
            if vendor["category"] == "Office Furniture"
        )
        return (
            "**Office Furniture RFQ Preview** (embedded demo data — simulated)\n\n"
            "| Vendor ID | Vendor | Distribution | Due | Evaluation Criteria |\n"
            "|---|---|---|---|---|\n" + rows
            + "\n\nResponse tracker and weighted evaluation matrix are prepared. "
              "No RFQ was distributed and no vendor record was changed.\n\n"
              "Source: [Dynamics 365 Procurement + Microsoft Teams]\nAgents: ProcurementAgent"
        )

    def _duplicate_license_check(self, params):
        return (
            "**Duplicate Software License Check** (embedded demo data — simulated)\n\n"
            "| Product | Purchased | Assigned | Overlap | Annual Avoidable Spend | Action |\n"
            "|---|---|---|---|---|---|\n"
            "| CRM Enterprise | 200 | 176 | 24 | $25,800 | Remove inactive seats before renewal |\n"
            "| Diagram Pro | 80 | 61 | 9 shared-suite overlaps | $4,860 | Consolidate to suite entitlement |\n\n"
            "**Total flagged:** $30,660 annual avoidable spend.\n"
            "Analysis only; no license, contract, or purchase record was changed.\n\n"
            "Source: [Dynamics 365 Procurement + License Inventory]\nAgents: ProcurementAgent"
        )


if __name__ == "__main__":
    agent = ProcurementAgent()
    print("=" * 60)
    print("EMBEDDED DEMO REQUEST (works offline)")
    print(agent.perform(operation="purchase_request", request_id="PR-5001"))
    print()
    print("=" * 60)
    print("LIVE TENANT ORDER (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="purchase_request", request_id="ORD-260100"))
    print()
    print("=" * 60)
    print("LIVE ERP PO + THREE-WAY MATCH (blocked invoice SINV-92003)")
    print(agent.perform(operation="purchase_request", request_id="PO-47003"))
    print()
    print("=" * 60)
    print(agent.perform(operation="spend_analysis"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
