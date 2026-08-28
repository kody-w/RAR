---
name: "rar-aibast-agents-library-supplier-risk-monitoring"
description: "Computes supplier risk from simulated ERP blocked invoices and late receipts, joined to Dynamics 365 cases, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/supplier_risk_monitoring", "rar_sha256": "93ad57d2e6b7a0d36375c39acbb1314bb7f52ebd3b2bacc6136b75fc2e85d392", "source_kind": "rar-agent", "source_commit": "019464ea325329b5de69b4af699769f5151e2212", "version": "1.3.0", "author": "AIBAST", "tags": ["supplier", "risk", "procurement", "supply-chain", "manufacturing"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/supplier_risk_monitoring`. The original RAPP
agent is preserved byte-for-byte in `supplier_risk_monitoring_agent.py` and in the RCI capsule.

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

Supplier Risk Monitoring Agent — a template you are meant to mutate.

Monitors supplier health across quality, delivery, financial stability,
and geopolitical dimensions. Produces risk scorecards, disruption alerts,
and alternative-sourcing recommendations to protect supply continuity.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works from anywhere):
       CRM — Static Dynamics 365 tenant (Aster Lane Office Systems):
         https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       ERP — Static ERP (suppliers, purchase orders, goods receipts,
       supplier invoices):
         https://kody-w.github.io/static-erp/api/v1/
     An open high-priority Dynamics case is a supply-disruption event,
     and REAL risk signals are computed per live ERP supplier — blocked
     invoices, late goods receipts — joined to CRM cases by account
     name.
     Try: perform(operation="risk_dashboard")
     — Orchard Signal Works flags blocked invoice SINV-92003
     (PO-47003), Quarry Bend Foundry flags GR-88005 posted 9 days late
     (PO-47005), and Granite Peak Manufacturing joins to its CRM
     downtime case CAS-260132.
  2. No network? Everything falls back to the embedded demo layer below
     (SUPPLIERS / RECENT_INCIDENTS / BACKUP_SUPPLIERS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SUPPLIER_RISK_MONITORING_DATA_URL (CRM side) and/or
     SUPPLIER_RISK_MONITORING_ERP_URL (ERP side) to any endpoint with
     the same shapes, or replace _fetch_collection() with a Coupa/SAP
     Ariba client. Fields the rest of the file needs are listed in
     _normalize_live_disruption() — spend exposure and risk scores render
     as "n/a — enrichment seam" until you wire spend analytics.

OPERATIONS
  risk_dashboard | supplier_scorecard | disruption_alerts
  | alternative_sourcing | risk_driver_analysis | mitigation_plan
  | financial_exposure | execution_timeline | monitoring_plan
  kwargs: operation (required), supplier_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "Operation to perform. Defaults to risk_dashboard when omitted.",
      "enum": [
        "risk_dashboard",
        "supplier_scorecard",
        "disruption_alerts",
        "alternative_sourcing",
        "risk_driver_analysis",
        "mitigation_plan",
        "financial_exposure",
        "execution_timeline",
        "monitoring_plan"
      ],
      "type": "string"
    },
    "supplier_id": {
      "description": "Supplier identifier used to select risk, mitigation, exposure, timeline, and monitoring records.",
      "type": "string"
    }
  },
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `supplier_risk_monitoring_agent.py` and embedded as the fenced Python below (sha256 93ad57d2e6b7a0d3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `supplier_risk_monitoring_agent.py` first:

```bash
python3 supplier_risk_monitoring_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 supplier_risk_monitoring_agent.py   # or on stdin
python3 supplier_risk_monitoring_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Supplier Risk Monitoring Agent — a template you are meant to mutate.

Monitors supplier health across quality, delivery, financial stability,
and geopolitical dimensions. Produces risk scorecards, disruption alerts,
and alternative-sourcing recommendations to protect supply continuity.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from TWO
     globally hosted simulated systems (synthetic data, no credentials,
     works from anywhere):
       CRM — Static Dynamics 365 tenant (Aster Lane Office Systems):
         https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
       ERP — Static ERP (suppliers, purchase orders, goods receipts,
       supplier invoices):
         https://kody-w.github.io/static-erp/api/v1/
     An open high-priority Dynamics case is a supply-disruption event,
     and REAL risk signals are computed per live ERP supplier — blocked
     invoices, late goods receipts — joined to CRM cases by account
     name.
     Try: perform(operation="risk_dashboard")
     — Orchard Signal Works flags blocked invoice SINV-92003
     (PO-47003), Quarry Bend Foundry flags GR-88005 posted 9 days late
     (PO-47005), and Granite Peak Manufacturing joins to its CRM
     downtime case CAS-260132.
  2. No network? Everything falls back to the embedded demo layer below
     (SUPPLIERS / RECENT_INCIDENTS / BACKUP_SUPPLIERS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     SUPPLIER_RISK_MONITORING_DATA_URL (CRM side) and/or
     SUPPLIER_RISK_MONITORING_ERP_URL (ERP side) to any endpoint with
     the same shapes, or replace _fetch_collection() with a Coupa/SAP
     Ariba client. Fields the rest of the file needs are listed in
     _normalize_live_disruption() — spend exposure and risk scores render
     as "n/a — enrichment seam" until you wire spend analytics.

OPERATIONS
  risk_dashboard | supplier_scorecard | disruption_alerts
  | alternative_sourcing | risk_driver_analysis | mitigation_plan
  | financial_exposure | execution_timeline | monitoring_plan
  kwargs: operation (required), supplier_id
"""

import sys
import os
import json
import datetime
import urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/supplier_risk_monitoring",
    "version": "1.3.0",
    "display_name": "Supplier Risk Monitoring Agent",
    "description": "Computes supplier risk from simulated ERP blocked invoices and late receipts, joined to Dynamics 365 cases, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["supplier", "risk", "procurement", "supply-chain", "manufacturing"],
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
#   export SUPPLIER_RISK_MONITORING_DATA_URL=https://your-org/api/data/v9.2
#   export SUPPLIER_RISK_MONITORING_ERP_URL=https://your-erp/api/v1
# or replace _fetch_collection() with your SRM client. Downstream
# code only needs the fields from _normalize_live_disruption() and
# _erp_supplier_risk().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "SUPPLIER_RISK_MONITORING_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
ERP_SOURCE_URL = os.environ.get(
    "SUPPLIER_RISK_MONITORING_ERP_URL",
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


def _days_between(earlier_iso, later_iso):
    """Whole days between two ISO date(-time) strings; 0 on parse issues."""
    try:
        a = datetime.date.fromisoformat(str(earlier_iso)[:10])
        b = datetime.date.fromisoformat(str(later_iso)[:10])
        return (b - a).days
    except (ValueError, TypeError):
        return 0


def _erp_supplier_risk():
    """REAL risk signals per live ERP supplier: payment-blocked invoices,
    goods receipts posted after the PO's expected delivery date, and open
    PO exposure — joined to CRM cases by account name (e.g. Granite Peak
    Manufacturing -> CAS-260132). [] when the ERP is unreachable."""
    suppliers = _erp("suppliers")
    if not suppliers:
        return []
    pos = _erp("purchase_orders")
    grs = _erp("goods_receipts")
    invs = _erp("supplier_invoices")
    incidents = _fetch_collection("incidents")
    expected = {
        p.get("po_number"): str(p.get("expected_delivery_date", ""))[:10]
        for p in pos
    }
    out = []
    for s in suppliers:
        name = s.get("name", "?")
        open_exposure = sum(
            float(p.get("total_amount") or 0)
            for p in pos
            if p.get("supplier_name") == name and p.get("status") == "open"
        )
        blocked = [
            i for i in invs
            if i.get("supplier_name") == name and i.get("payment_block")
        ]
        late = []
        for g in grs:
            if g.get("supplier_name") != name:
                continue
            exp = expected.get(g.get("po_number"), "")
            post = str(g.get("posting_date", ""))[:10]
            if exp and post > exp:
                late.append((g, _days_between(exp, post)))
        case = next(
            (c for c in incidents if c.get("customeridname") == name), None
        )
        flags = [
            f"invoice {i.get('invoice_number')} payment-blocked on "
            f"{i.get('po_number')} (${float(i.get('total_amount') or 0):,.2f})"
            for i in blocked
        ] + [
            f"{g.get('receipt_number')} posted {days} days after "
            f"{g.get('po_number')} expected delivery"
            for g, days in late
        ]
        if case:
            flags.append(
                f"CRM case {case.get('ticketnumber')} "
                f"\"{case.get('title')}\" "
                f"({case.get('statecode@OData.Community.Display.V1.FormattedValue', 'Active')})"
            )
        out.append({
            "name": name,
            "category": s.get("category", "?"),
            "terms": s.get("payment_terms", "?"),
            "open_exposure": open_exposure,
            "blocked_count": len(blocked),
            "late_count": len(late),
            "crm_case": case.get("ticketnumber") if case else None,
            "signal": "ELEVATED" if (blocked or late or case) else "OK",
            "flags": flags,
        })
    return out


_LIVE_SEVERITY = {"High": "HIGH", "Normal": "MEDIUM", "Low": "LOW"}


def _normalize_live_disruption(row):
    """Project an open Dynamics case onto the disruption-event shape this
    agent renders. THIS is the contract your replacement data source must
    meet — a dict with these keys. None means 'not knowable from the case
    alone' and the renderer labels it as an enrichment seam (wire spend
    analytics for exposure)."""
    prio = row.get(
        "prioritycode@OData.Community.Display.V1.FormattedValue", "Normal"
    )
    return {
        "supplier": row.get("customeridname", "Unknown"),
        "date": str(row.get("createdon", ""))[:10],
        "severity": _LIVE_SEVERITY.get(prio, "MEDIUM"),
        "description": row.get("title", "untitled"),
        "spend_exposed": None,  # enrichment seam — wire your spend cube
        "_live": True,
    }


def _live_disruptions():
    """Open high-priority cases from the live tenant, reinterpreted as
    supply-disruption events; [] when offline."""
    rows = _fetch_collection("incidents")
    events = [
        _normalize_live_disruption(r) for r in rows
        if r.get("statecode") == 0
        and r.get("prioritycode@OData.Community.Display.V1.FormattedValue") == "High"
    ]
    return sorted(events, key=lambda e: e["date"], reverse=True)


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

SUPPLIERS = {
    "SUP-101": {
        "name": "TechnoCore Semiconductor (Taiwan)",
        "category": "Microcontrollers",
        "region": "Asia-Pacific",
        "country": "Taiwan",
        "annual_spend": 4800000,
        "quality_score": 82,
        "delivery_score": 74,
        "financial_score": 68,
        "geopolitical_score": 42,
        "overall_risk": 8.2,
        "tier": 1,
    },
    "SUP-102": {
        "name": "Shenzhen Electronics Co.",
        "category": "Passive Components",
        "region": "Asia-Pacific",
        "country": "China",
        "annual_spend": 3200000,
        "quality_score": 71,
        "delivery_score": 78,
        "financial_score": 55,
        "geopolitical_score": 58,
        "overall_risk": 6.5,
        "tier": 1,
    },
    "SUP-103": {
        "name": "Malaysia Semicon Pte Ltd",
        "category": "Power ICs",
        "region": "Asia-Pacific",
        "country": "Malaysia",
        "annual_spend": 2100000,
        "quality_score": 91,
        "delivery_score": 88,
        "financial_score": 84,
        "geopolitical_score": 82,
        "overall_risk": 3.8,
        "tier": 1,
    },
    "SUP-104": {
        "name": "Midwest Casting & Forge",
        "category": "Aluminum Castings",
        "region": "North America",
        "country": "USA",
        "annual_spend": 5600000,
        "quality_score": 88,
        "delivery_score": 65,
        "financial_score": 72,
        "geopolitical_score": 95,
        "overall_risk": 4.9,
        "tier": 1,
    },
    "SUP-105": {
        "name": "Rheinmetall Precision GmbH",
        "category": "CNC Machined Parts",
        "region": "Europe",
        "country": "Germany",
        "annual_spend": 3800000,
        "quality_score": 95,
        "delivery_score": 91,
        "financial_score": 89,
        "geopolitical_score": 88,
        "overall_risk": 2.4,
        "tier": 2,
    },
}

RECENT_INCIDENTS = [
    {"supplier_id": "SUP-101", "date": "2026-02-28", "severity": "HIGH",
     "description": "Cross-strait military exercises caused 5-day port closure; delayed 3 shipments"},
    {"supplier_id": "SUP-102", "date": "2026-03-05", "severity": "MEDIUM",
     "description": "Quality excursion: capacitor lot C-4410 failed incoming inspection (2.3% defect rate vs 0.5% spec)"},
    {"supplier_id": "SUP-104", "date": "2026-03-10", "severity": "HIGH",
     "description": "Equipment failure at foundry; force majeure declared, 7-day production halt"},
    {"supplier_id": "SUP-102", "date": "2026-03-12", "severity": "LOW",
     "description": "New export control regulations announced; compliance review underway"},
]

BACKUP_SUPPLIERS = {
    "SUP-101": [
        {"name": "Samsung Foundry (Korea)", "lead_time_weeks": 12, "qual_status": "In Progress", "est_cost_premium_pct": 8},
        {"name": "GlobalFoundries (USA)", "lead_time_weeks": 16, "qual_status": "Not Started", "est_cost_premium_pct": 15},
    ],
    "SUP-102": [
        {"name": "Murata Electronics (Japan)", "lead_time_weeks": 6, "qual_status": "Qualified", "est_cost_premium_pct": 5},
        {"name": "Vishay Intertechnology (USA)", "lead_time_weeks": 4, "qual_status": "Qualified", "est_cost_premium_pct": 12},
    ],
    "SUP-104": [
        {"name": "Alcoa Precision Castings (USA)", "lead_time_weeks": 8, "qual_status": "In Progress", "est_cost_premium_pct": 6},
    ],
}

SUPPLY_RISK_PLANS = {
    "SUP-101": {
        "financial_trend": "credit outlook negative; days payable outstanding +11",
        "operational_capacity_pct": 72, "logistics_reliability_pct": 68,
        "safety_stock_days": 35, "dual_source": "Samsung Foundry (Korea)",
        "mitigation_investment": 384000, "modeled_disruption_loss": 2150000,
        "owner": "Electronics Category Manager", "next_review": "2026-03-19",
    },
    "SUP-102": {
        "financial_trend": "stable; margin pressure from export controls",
        "operational_capacity_pct": 81, "logistics_reliability_pct": 76,
        "safety_stock_days": 21, "dual_source": "Murata Electronics (Japan)",
        "mitigation_investment": 160000, "modeled_disruption_loss": 980000,
        "owner": "Components Sourcing Lead", "next_review": "2026-03-22",
    },
    "SUP-104": {
        "financial_trend": "stable; repair cash requirement elevated",
        "operational_capacity_pct": 54, "logistics_reliability_pct": 71,
        "safety_stock_days": 28, "dual_source": "Alcoa Precision Castings (USA)",
        "mitigation_investment": 336000, "modeled_disruption_loss": 1740000,
        "owner": "Metals Category Manager", "next_review": "2026-03-18",
    },
}

EVIDENCE_MARKER = (
    "[Evidence: supply-risk-monitoring one-pager and demo transcript; "
    "risk-driver intelligence, mitigation, financial exposure, execution, and continuous alerts]"
)


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _composite_score(supplier):
    """Weighted composite health score (0-100, higher = healthier)."""
    return round(
        supplier["quality_score"] * 0.30
        + supplier["delivery_score"] * 0.25
        + supplier["financial_score"] * 0.25
        + supplier["geopolitical_score"] * 0.20,
        1,
    )


def _risk_tier_label(overall_risk):
    """Convert numeric risk to a label."""
    if overall_risk >= 7.0:
        return "CRITICAL"
    elif overall_risk >= 5.0:
        return "HIGH"
    elif overall_risk >= 3.0:
        return "MODERATE"
    return "LOW"


def _total_spend():
    """Total annual spend across all suppliers."""
    return sum(s["annual_spend"] for s in SUPPLIERS.values())


def _spend_at_risk(threshold=5.0):
    """Annual spend with suppliers above the given risk threshold."""
    return sum(s["annual_spend"] for s in SUPPLIERS.values() if s["overall_risk"] >= threshold)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class SupplierRiskMonitoringAgent(BasicAgent):
    """Monitors supplier risk and generates mitigation plans."""

    def __init__(self):
        self.name = "SupplierRiskMonitoringAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "operations": [
                "risk_dashboard",
                "supplier_scorecard",
                "disruption_alerts",
                "alternative_sourcing",
                "risk_driver_analysis",
                "mitigation_plan",
                "financial_exposure",
                "execution_timeline",
                "monitoring_plan",
            ],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "description": "Operation to perform. Defaults to risk_dashboard when omitted.",
                        "enum": [
                            "risk_dashboard",
                            "supplier_scorecard",
                            "disruption_alerts",
                            "alternative_sourcing",
                            "risk_driver_analysis",
                            "mitigation_plan",
                            "financial_exposure",
                            "execution_timeline",
                            "monitoring_plan",
                        ],
                    },
                    "supplier_id": {
                        "type": "string",
                        "description": "Supplier identifier used to select risk, mitigation, exposure, timeline, and monitoring records.",
                    },
                },
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "risk_dashboard")
        dispatch = {
            "risk_dashboard": self._risk_dashboard,
            "supplier_scorecard": self._supplier_scorecard,
            "disruption_alerts": self._disruption_alerts,
            "alternative_sourcing": self._alternative_sourcing,
            "risk_driver_analysis": self._risk_driver_analysis,
            "mitigation_plan": self._mitigation_plan,
            "financial_exposure": self._financial_exposure,
            "execution_timeline": self._execution_timeline,
            "monitoring_plan": self._monitoring_plan,
        }
        handler = dispatch.get(operation)
        if handler is None:
            return f"**Error:** Unknown operation `{operation}`. Valid: {', '.join(dispatch.keys())}"
        return handler(**kwargs)

    # ------------------------------------------------------------------
    def _risk_dashboard(self, **kwargs) -> str:
        lines = ["## Supplier Risk Dashboard\n"]
        total = _total_spend()
        at_risk = _spend_at_risk(5.0)
        lines.append(f"**Total annual supplier spend:** ${total:,.0f}")
        lines.append(f"**Spend at elevated risk (score >= 5.0):** ${at_risk:,.0f} ({round(at_risk/total*100,1)}%)\n")

        lines.append("| Supplier | Category | Country | Spend | Risk Score | Risk Tier | Composite Health |")
        lines.append("|----------|----------|---------|-------|------------|-----------|------------------|")
        ranked = sorted(SUPPLIERS.values(), key=lambda s: s["overall_risk"], reverse=True)
        for s in ranked:
            tier = _risk_tier_label(s["overall_risk"])
            health = _composite_score(s)
            lines.append(
                f"| {s['name'][:32]} | {s['category']} | {s['country']} | "
                f"${s['annual_spend']:,.0f} | {s['overall_risk']} | **{tier}** | {health}/100 |"
            )

        lines.append(f"\n**Active incidents:** {len(RECENT_INCIDENTS)}")
        high_incidents = sum(1 for i in RECENT_INCIDENTS if i["severity"] == "HIGH")
        lines.append(f"**HIGH severity incidents:** {high_incidents}")

        erp_risk = _erp_supplier_risk()
        if erp_risk:
            lines.append("\n### Live ERP Supplier Risk Signals (REAL joins: invoices, receipts, CRM cases)\n")
            lines.append("| Supplier | Category | Terms | Open PO Exposure | Blocked Invoices | Late Receipts | CRM Case | Signal |")
            lines.append("|----------|----------|-------|------------------|------------------|---------------|----------|--------|")
            for r in sorted(erp_risk, key=lambda x: (x["signal"] == "OK", x["name"])):
                lines.append(
                    f"| {r['name']} | {r['category']} | {r['terms']} | "
                    f"${r['open_exposure']:,.2f} | {r['blocked_count']} | {r['late_count']} | "
                    f"{r['crm_case'] or '—'} | **{r['signal']}** |"
                )
            flagged = [r for r in erp_risk if r["flags"]]
            if flagged:
                lines.append("\n**ERP/CRM risk evidence:**")
                for r in flagged:
                    for f in r["flags"]:
                        lines.append(f"- {r['name']}: {f}")
            lines.append(
                "\nAnnual spend and financial scores per ERP supplier: "
                "n/a — enrichment seam (wire your spend cube)."
            )
        else:
            lines.append("\n_Simulated ERP unreachable — live supplier risk signals unavailable._")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _supplier_scorecard(self, **kwargs) -> str:
        lines = ["## Supplier Scorecards\n"]
        for sid, s in SUPPLIERS.items():
            health = _composite_score(s)
            tier = _risk_tier_label(s["overall_risk"])
            lines.append(f"### {s['name']} ({sid})")
            lines.append(f"- **Category:** {s['category']}")
            lines.append(f"- **Region:** {s['region']} ({s['country']})")
            lines.append(f"- **Annual spend:** ${s['annual_spend']:,.0f}")
            lines.append(f"- **Tier:** {s['tier']}")
            lines.append(f"- **Overall risk:** {s['overall_risk']}/10 ({tier})")
            lines.append(f"- **Composite health:** {health}/100\n")
            lines.append("| Dimension | Score | Status |")
            lines.append("|-----------|-------|--------|")
            for dim in ["quality_score", "delivery_score", "financial_score", "geopolitical_score"]:
                val = s[dim]
                status = "Good" if val >= 80 else "Watch" if val >= 60 else "At Risk"
                label = dim.replace("_score", "").replace("_", " ").title()
                lines.append(f"| {label} | {val}/100 | {status} |")

            # Show incidents for this supplier
            incidents = [i for i in RECENT_INCIDENTS if i["supplier_id"] == sid]
            if incidents:
                lines.append(f"\n**Recent incidents ({len(incidents)}):**")
                for inc in incidents:
                    lines.append(f"- [{inc['severity']}] {inc['date']}: {inc['description']}")
            lines.append("")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _disruption_alerts(self, **kwargs) -> str:
        lines = ["## Active Disruption Alerts\n"]
        if not RECENT_INCIDENTS:
            lines.append("No active disruption alerts.")
            return "\n".join(lines)

        sorted_incidents = sorted(RECENT_INCIDENTS, key=lambda i: {"HIGH": 0, "MEDIUM": 1, "LOW": 2}.get(i["severity"], 3))
        lines.append("| Severity | Date | Supplier | Description |")
        lines.append("|----------|------|----------|-------------|")
        for inc in sorted_incidents:
            sname = SUPPLIERS.get(inc["supplier_id"], {}).get("name", inc["supplier_id"])
            lines.append(f"| **{inc['severity']}** | {inc['date']} | {sname[:28]} | {inc['description']} |")

        lines.append("\n### Impact Assessment\n")
        for inc in sorted_incidents:
            if inc["severity"] != "HIGH":
                continue
            s = SUPPLIERS.get(inc["supplier_id"], {})
            lines.append(f"**{s.get('name', inc['supplier_id'])}**")
            lines.append(f"- Annual spend exposed: ${s.get('annual_spend', 0):,.0f}")
            lines.append(f"- Category: {s.get('category', 'N/A')}")
            has_backup = inc["supplier_id"] in BACKUP_SUPPLIERS
            lines.append(f"- Backup suppliers available: {'Yes' if has_backup else 'No'}")
            lines.append("")
        live = _live_disruptions()
        if live:
            seam = "n/a — enrichment seam"
            lines.append("### Live Tenant Disruption Events (open high-priority Dynamics cases)\n")
            lines.append("| Severity | Date | Supplier/Account | Description | Spend Exposed |")
            lines.append("|----------|------|------------------|-------------|---------------|")
            for e in live:
                exposed = seam if e["spend_exposed"] is None else f"${e['spend_exposed']:,.0f}"
                lines.append(
                    f"| **{e['severity']}** | {e['date']} | {e['supplier'][:28]} | "
                    f"{e['description']} | {exposed} |"
                )
        else:
            lines.append("_Live tenant unreachable — showing embedded demo incidents only._")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _alternative_sourcing(self, **kwargs) -> str:
        lines = ["## Alternative Sourcing Plan\n"]
        if not BACKUP_SUPPLIERS:
            lines.append("No alternative suppliers have been identified.")
            return "\n".join(lines)

        for sid, backups in BACKUP_SUPPLIERS.items():
            s = SUPPLIERS.get(sid, {})
            lines.append(f"### Alternatives for {s.get('name', sid)} ({s.get('category', 'N/A')})")
            lines.append(f"- **Current spend:** ${s.get('annual_spend', 0):,.0f}")
            lines.append(f"- **Current risk:** {s.get('overall_risk', 'N/A')}/10\n")
            lines.append("| Alternative Supplier | Lead Time | Qual Status | Cost Premium |")
            lines.append("|---------------------|-----------|-------------|--------------|")
            for b in backups:
                lines.append(
                    f"| {b['name']} | {b['lead_time_weeks']} weeks | {b['qual_status']} | +{b['est_cost_premium_pct']}% |"
                )

            # Recommendation
            qualified = [b for b in backups if b["qual_status"] == "Qualified"]
            if qualified:
                best = min(qualified, key=lambda b: b["est_cost_premium_pct"])
                lines.append(f"\n**Recommendation:** Activate {best['name']} immediately "
                             f"(qualified, +{best['est_cost_premium_pct']}% premium, {best['lead_time_weeks']}-week lead)")
            else:
                fastest = min(backups, key=lambda b: b["lead_time_weeks"])
                lines.append(f"\n**Recommendation:** Accelerate qualification of {fastest['name']} "
                             f"({fastest['lead_time_weeks']}-week lead, currently {fastest['qual_status']})")
            lines.append("")

        total_premium = 0
        for sid, backups in BACKUP_SUPPLIERS.items():
            s = SUPPLIERS.get(sid, {})
            best_prem = min(b["est_cost_premium_pct"] for b in backups)
            total_premium += s.get("annual_spend", 0) * best_prem / 100
        lines.append(f"**Estimated annual cost of full diversification:** ${total_premium:,.0f}")
        lines.append(f"**Risk reduction value:** ${_spend_at_risk(5.0):,.0f} of spend de-risked")
        return "\n".join(lines)

    def _risk_plan(self, **kwargs):
        supplier_id = str(kwargs.get("supplier_id", "SUP-101")).strip().upper()
        plan = SUPPLY_RISK_PLANS.get(supplier_id)
        if plan is None:
            valid = ", ".join(SUPPLY_RISK_PLANS)
            return supplier_id, None, f"**Error:** Unknown supplier `{supplier_id}`. Valid: {valid}"
        return supplier_id, plan, ""

    def _risk_driver_analysis(self, **kwargs) -> str:
        supplier_id, plan, error = self._risk_plan(**kwargs)
        if error:
            return error
        supplier = SUPPLIERS[supplier_id]
        return "\n".join([
            "## Supply Risk Driver Analysis",
            EVIDENCE_MARKER,
            f"**Supplier lookup:** {supplier_id} — {supplier['name']}",
            f"- Region/category: {supplier['region']} / {supplier['category']}",
            f"- Financial trend: {plan['financial_trend']}",
            f"- Operational capacity: {plan['operational_capacity_pct']}%",
            f"- Logistics reliability: {plan['logistics_reliability_pct']}%",
            f"- Quality score: {supplier['quality_score']}/100",
            f"- Overall risk: {supplier['overall_risk']}/10 ({_risk_tier_label(supplier['overall_risk'])})",
        ])

    def _mitigation_plan(self, **kwargs) -> str:
        supplier_id, plan, error = self._risk_plan(**kwargs)
        if error:
            return error
        return "\n".join([
            "## Targeted Supply Risk Mitigation",
            EVIDENCE_MARKER,
            f"**Supplier lookup:** {supplier_id} — {SUPPLIERS[supplier_id]['name']}",
            "1. **Immediate:** Escalate active incidents and verify open shipment ETAs.",
            f"2. **Containment:** Raise safety stock to {plan['safety_stock_days']} days.",
            f"3. **Diversification:** Qualify/activate {plan['dual_source']}.",
            "4. **Validation:** Run first-article, logistics-lane, and commercial reviews.",
            f"5. **Owner/review:** {plan['owner']} / {plan['next_review']}.",
        ])

    def _financial_exposure(self, **kwargs) -> str:
        supplier_id, plan, error = self._risk_plan(**kwargs)
        if error:
            return error
        investment = plan["mitigation_investment"]
        loss = plan["modeled_disruption_loss"]
        avoided = round(loss * 0.72)
        roi = round((avoided - investment) / investment * 100, 1)
        return "\n".join([
            "## Supply Risk Financial Exposure",
            EVIDENCE_MARKER,
            f"**Supplier lookup:** {supplier_id} — {SUPPLIERS[supplier_id]['category']}",
            f"- Annual spend exposed: ${SUPPLIERS[supplier_id]['annual_spend']:,.0f}",
            f"- Modeled disruption loss: ${loss:,.0f}",
            f"- Mitigation investment: ${investment:,.0f}",
            f"- Modeled loss avoided: ${avoided:,.0f}",
            f"- First-year mitigation ROI: {roi}%",
        ])

    def _execution_timeline(self, **kwargs) -> str:
        supplier_id, plan, error = self._risk_plan(**kwargs)
        if error:
            return error
        return "\n".join([
            "## Supply Risk Execution Timeline",
            EVIDENCE_MARKER,
            f"**Supplier lookup:** {supplier_id} — {SUPPLIERS[supplier_id]['name']}",
            "",
            "| Phase | Window | Action |",
            "|-------|--------|--------|",
            "| Immediate | 0-48 hours | Confirm shipments, incident owner, and safety-stock gap |",
            f"| Validate | Days 3-14 | Qualify {plan['dual_source']} and test logistics lane |",
            f"| Optimize | Days 15-45 | Hold {plan['safety_stock_days']} days stock and rebalance awards |",
            "",
            f"- **SIMULATED WRITE RECEIPT:** `RISK-SIM-{supplier_id}` for Teams stakeholder update",
            "- Simulation only; no sourcing award, purchase order, or Teams message was created.",
        ])

    def _monitoring_plan(self, **kwargs) -> str:
        supplier_id, plan, error = self._risk_plan(**kwargs)
        if error:
            return error
        return "\n".join([
            "## Continuous Supply Risk Monitoring",
            EVIDENCE_MARKER,
            f"**Supplier lookup:** {supplier_id} — {SUPPLIERS[supplier_id]['name']}",
            "",
            "| Signal | Cadence | Alert Threshold |",
            "|--------|---------|-----------------|",
            "| Financial health | Daily | Credit score falls 5 points |",
            f"| Operational capacity | Hourly | Below {plan['operational_capacity_pct']}% baseline by 10 points |",
            f"| Logistics reliability | Per shipment | Below {plan['logistics_reliability_pct']}% |",
            "| Quality | Per lot | Defect rate above 0.5% |",
            "| Geopolitical | Daily | Severity HIGH |",
            "",
            f"Next human review: **{plan['next_review']}**, owned by **{plan['owner']}**.",
        ])


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = SupplierRiskMonitoringAgent()
    print("=" * 72)
    print("EMBEDDED DEMO INCIDENTS + LIVE TENANT DISRUPTION EVENTS")
    print("(live section fetched over HTTP; falls back offline)")
    print("=" * 72)
    print(agent.perform(operation="disruption_alerts"))
    print()
    print("=" * 72)
    print("LIVE ERP SUPPLIER RISK SIGNALS + CRM CASE JOIN")
    print("(blocked invoices, late receipts; falls back offline)")
    print("=" * 72)
    print(agent.perform(operation="risk_dashboard"))
    print()
    for op in [o for o in agent.metadata["operations"] if o not in ("disruption_alerts", "risk_dashboard")]:
        print("=" * 72)
        print(agent.perform(operation=op))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/628V7PjSLIm+FdoOQ+3ulFZIDRRa3d3oQUBCggCxNRYNbTWmj393yd4UpTq2WtjtsfygQTCPTxcfP45zSL/+cmfp6wdPv38iVFYxrQ+/fgpisdwyLspbxvwmGvrbp7i8TDOXVfl8XAY8rE8JENbH8a8nit/iqODYNwOQdWGJficN0ubh0DCb6LD+/VhiMMYKBx/PBRt3oAlU3vg98av83A8YCRxCP0xBm/XfMqA1KFNkgqsO0Rx3R4Sv6oCPyx/AqbFm193VTx++vm//48fP+Xg86ef//kprPwRPPpkfrXQAAbqbZNP7ZA3KZPGzQRkK79JwaJuB+dtwPcuHpJ2qMGjKE4OX7/9MMZV8uPh738vV39Ix78dPv/fh3Eafv6lOXz9a8FK/+2bw38eviz6KY2nH3759P3FL59+PPzy6e2lXyN/zILWH6JfPv3tNxVRPnb+FGZAwz9/e/r++6vYz4e3RT/9+sfnP/5Z7Ftwfh3DFnj7D6J/ffcXcWDRMH9E/Fe/iodp/E36L6/+IuxXUzw04OhL/OvYzkMInP6b/L97++O/P/UA1gy/+o1f7WM+/vnsf3z7FxV1PuXph/9/7UCof5P+04u/CCZ54zdh7le/xlvXjvMQ/yb713d/EY+3OJw/tE95Hb/T9jfxv777q9nf8/TPZv/xxe8E//XbxwyUGAgKSKRvOfWRjN9T8XdJlyffV+fj4dI28c9/tGWIp3loDskvn/7+d2EY2uHnv//9YDdl067N77L+H//8/vlf//jp8PCrPPr58M//+PHwHz+9q/uH75aU8T7+8Le//euXT79t9HWTr5b88L3OPv0LlHMDKm0O35rf1fzf/ttBz8OhHdtkOphhO0+HYW7ejvyl+aWxMnAK8G/K3vACMmPMgyr+uq4b2iL+UASg5PCP/9fPA3+cPvtvJBg/V3kw+MMOf6+Lj/z6zd/gVBbQCj6nIPzVwWBut1+aD+H3jt0Qj/GwABQL9in+DFDj8/sDgL3DP/53Kn/9kP6p2//xAYpg6dtug1MA8nXjXMU/vc/kZHHz9QQhQMEv2RMfAKwCK5K8ekMk2LytlhjIA1PGMq8qEHpQ1WCf/UM38NHPb2X/+Mc/wKGzX5ovgIcdvoD6CIMF3805fP4MjgPANs2mX5o4zNrDf/zzX/9x+J+H/y+pD+XvPW4Ad79GAFiomtfLAURzrt9uPrzDGfvRRwT++a+vTgVqGpCBIF55ksdfhEFdgLbxzcOmzHxGCfIQxMCzwKt11w4TcOEhn346KMnhu71g0/cr0GYOWTtOoFl0cRPFTbgDrT44zndPNu10GEHGjsn+42Ee449d/wGS4MPE+tcQLP/HQeduoC+11bs5ATM/FgFhEEPg/u/x//IcKBn+Yzyw31T8dLi8c/DQ+YPfZYP/dY/E/xKXdjh8EwfK/UMTr7807+4Vv131UUtf3AMWAc+EX0P6+R3zQ9jWNQjs+G3vjzUfTddqQVbHwy/N+DXZ/eGj17bAlP2QznkEwCv+v76m1Ji1cxV9+A9Y+tb0NQrR16h85OC3Hnp4N9HDb1308NFGD7/M6BHBwRHAobuP3r6388e+deyD9+B49QxO9CWhv4r/jjtkIFHePf5d1+OhnwF6TCAoEQDHt9E/Hr4jLmi7fpB/vAbOB4mdxm3Xgu/vcAAHAc+Nb6T46XAb2mh+840PYvK9yYFi+a13Hb73rreq3/Wkz9960ofjaqA1+ojH+D4KwJEJuPaL+TuIBICfZgYmfZxOvjoHS1bMgyXoN42xhINzNc7mG+yQnw5X4HKQ+m8/B+0GsvfQzVU1Ht4H/dgLWHh4R+pL8ciWdftCqizn+hUv06oNAPnZP/IbhOk3ujXu76wbDz+MewN2mN4p40/+j4emPYRDDKpgAi783iTXdijHL9r9Zl+zeIj/9hv6c4b+La7mOxnDP3KzKW7ekf2BeefaQfMBL7smCSB4B/OLFX/7fSPJpqkbf4bhso32z+tPKWB0c/BT3sLjh+rP0VfVn4Fq2O9y+G03vNA/ofB3LW8y+UeD3k9++JZEILAdiFn2rjLgxY8HadsCd37nmd9VfU+8b6T0/8jYeOg+bFyQb8YxH60QNDCAQAA6c1Ab0/6bv9489t0j/K8p8/l3GQgAopm+WfbOQkNgtK85m6eg0YwfdRR+4dvRm5F+SZb34b+f46tfvnLtr9q+He7HL3T7j874JvIb9X4H/INxgw4GShGgQzN91QTO8S7dj8/WsP/8nRd/b/r/+b+ntl83ur5jM0QH8+NUB+dL8lV+Ov55RDiYyuXxmUaPR+yrih9u1884Bb7/7cfDffYHgGMsKMmDCGyMwJcvaiTj8+l0PBKH7kth0CD79/Hj8H/SQwA9b19Lgw+gKD7cYh+gmt/Mb2ieP4Dt7ZePas+Br4BrvmqIAO15k40vMeUY8zNKHhEM/fAOCgC/BTA+vSvr/zkIb+wCHRloe08r4JxgXnmrfFd/XAdxFAErP6aZyt9BFIO4atdvppr27aYpgmEeYJATnHCxflUunMKDD+9HLMOd7duv31f97Zuf38q/tJXm3Xy+qgtB98lAaL/OUB/mYj+BM5fxG4QAXAM89qcPaU15CAeesZiDKTD6F6ve/PNbNnzb81dDMc+/6teLYl0N5SL9+pb51Ta0ww/vXBrzKP7b281wO/xXkiCZvwh+ZPWH4LslNvsBhLkDoZg+psCvat5GjiAlQfPyu3d+t2+4BI0H5M6vSQxY5q9hW1Vf2t8Pf/s6QB64du582GRu36p2AATwEIICAvzlIOZxFX3jLeN3lP5otk0cR1/qsMo/Uitvvur4tQFlANrVK/71XZW/m4t++B6R8c1ADt9GhS907HtPelck4CffPOSDwvzUwP432bgBjT978wEQAL/+5dPhTXarj/66AjrwVfnH/AOwafxoQdebYDCWcr18dJ0/1iUgcX+d/MDDv856QPR/Hv7dnAYe/7vZCzz+87T1oeKv0xJ4+NcZ6C3+p6kHiH8ZBH7+3aTxwxD3Mzh5BGr4+0ny6D3KA+wApOfTzw1oqT9+eoPWfzn+v6lZHYMzju+fDEBnB/tMefzx7fue7y9//Pnj+t2cNx/4AoY/Hfg48edq+oCNP3l9fZP4FvgHZM/HTxbNXH/6+b//CTTBi78G5/3by5+DA579u8iAx/8uMuDxnyIDnvw1LB+/pPw5LG/ZP4bl0//48dO0d2/fgsnsveu/fmc2iMRfvPWdPeYfFCR5fwRc+aPrgLH2zaXeZv/4u/z58Xu9/Hj4PiV/lM5v1nzjS29//smgf31/0gbvme9t4puYfvlp55+fQMj9N8X4GvSvYyFYDkbAz+ObGMPIT8e3O/3hy4AD3v0fDoxfpQFGgcEFiNOYHxFUhMZkQPnHCCMxiggx2g+DAMEQPAiohEDjIMICFDSKkEQwsJBIQjQ+ERFGo+/keMc5/vXNSPO3RUeExkk89jGUwFA6IKKYpAPcT0iapkg6IRACiVEU+Z1omTfR12N+OdbbVd9n17c7vp72n58CEgcrZXxUmC9/HEzbdODegsukJbA5rdTN2Uih39VoVlv8tViD/NjEGG58uzxiAn3OH6yQzepDaM7FSKGvGyoQJ51OYBbagyvFMDnTcXeqAgfUCcRXWll8DtKyclR51QkpfpGB5a7xaI4wPFrXdWRv65jejH4l8FLm4MW5Ja/zTXVXssZS1cOn9TXsCqC/GC7Z5jiXpzROHsUd83TU35iiqLH87unkKclcWU86hBJetFddasaCt0AepaY1aPwewZiab9dFJW7DKz49dVa6qbt4urjLSs3sDXqwlBKxruS4tpU/aazRlfKOUm1oUNhiKIzfJtnr4q3l8UmTgnEsgRMF6cb0J1bwx+0qnMj5preijrM+w/P0Il8VxBM5/9SsRSmSa8K2ZfJihKy+1FSOQ+MJIsuX1U/jabG8PhFvFRHCER8/z5vjGckrUx486NMEiTtJ7UEr6q57bjTX8v7kKDFVTri96GqFNSFeSccgq2QbclNGgPjYz3hkYdrrdX0VGbMF1PHVmFKBT7guHL3+gQshw9wZXDrLUyW25ijDAjswpzuPeufwSnGkqI9PeWHxmtIVCEc3bpGKnrr6XBOMYssQTWrE4hWWqVskwvM6M8Ls9aXaHt0RYUZ83tIrbBFN8JQYdrw9r0JVh86FghAdd0Rr7nMdlkKaelhwWKTV7plM9lj5fSqS17TJBRVNLpL0KDOdybkwttU/VZtlrmVxeXaB4IarX7ZrXOjM3WdylLgdFztQm1p/QTh/lwOPlNV2q7IImS2ft3lxJPBVDyBf3D3DopS7pt2ja1vcG1xvcwbvJG2VKEjMPLZVQjqavL4pS5m274xmsAqv8XGAk8OVkdyc7zb8mpalKZ1MuoC39MmVXvWoVTlFBb8gNFJIGP6VutUWbTxbL3dXcV5QCJzJMHPOhxdNtgajxa88r6u98zzjRphAWUpkKIvgJ6q1U7PFB2fWGZFK78cnh/jGMLYot+ZWfBb99mzST+ia0Pf44SZoVD4we3ZFwqErmH9owRV+BcfWGRhMkfkxPrITI56ESovc6nnlGw+hL9l1hNcBjzfZyqTjCq2MZCYjeip5LZQD9RaxD7dgknhBSmtuz70t5RRzIVKO4VaOOzG75IWDxBgnBO0SIu8oLzCIwe6h9eQx4s2WNegl9m2lKtuadeRZV+gBPqmMr44ntL7xq8/gLXu7H9mVsRcHJ26rNWte0tBE7A7mXPev4FHALe0RHTbtSWPsPAuvR2+pj3d40aipOxNJm+MMfRwU9iQy5f1mFw7TPXeXwRudJ5X+TD28YlBx6swm96UX06UNyEbdaJ/SCs8PVLTHyvok1Wutz8iDvCDDkfJvmHXTRuJ2zSJXhaJlpvMKgqm+Up176KjwKqIl1TyfQ1wqMreQQjyZN5K5+ewo+a+ZZ+3iKdu5nyrKcxtZSGMJSoesQpDttGbFtILIuwoj27TRV7VnkfSOaNpiC5DVnonXBeyHnipZ8SALvdG2KKW9dV6WhGD1O3O3w5NVuMtRpdeWExJOlAJINy5JzjIRc0tjnoESKIoqbZ7FCTUdJcKz/qXeVt199QKldz2q7dlxtbmpyMKXShdoDwpUGU5wM2vkFgEUT/fy1UH3PHi9mCfOkLjcagJfbRKrajkRPE7YdQ9tQkrpgJoyvk9nsn+gfLYN3jCww/F2Yy/SEiHnlTZVxqinEJTwDGbnLrUprlQIDdU6BlYYkDYxWp8wnBEWHmouffbieOoZw7b64OgbjRBHM5tH0VRHURMSAuMbJkw7qDzCuiQxKyVlBRRlD4lDyo3mL5fbcjKylif5LmbwYWmhYn9aCxKJR413JJqDr8vVDA23lJnMQFPpWpb0nS6Xfj9xN/s6VxiFxIVMa5hJ7maQDExLXKe4L2EkuVrxjlNp4L0I3IVgdBYEVH2x08ngKGMbPWl6jeLNuguD1kXRWMygVsOZh2v7RHc6l+zeoJ+jCJofbhg+jTHcmCGBRxtgPG4dTW5e2bXQkG7sMLN4RIb9oJHMjgTtnuYI2eMSt60cyUEkt2x9tlPTFl8ggr0UTz8snt5Rp/BjmZ7zTDYUG8JfdXGswl0wK3HqV0v1i7vp9xpj0zbbXXvRsGc/W/u1YwOC1Nc123yCPPnBkyKbksvSa+wW49lGNs5gAzjNFpdF/PhYmp4CxhiHF+D1SltHVMEvm5rLBJNkkcBtlBrsTGBGdyfDlfs9bumXcp24i8eHMhYRoTLjmG8IRuYy95DE11u57GwTsM2YCS3M2BG0JjCWwDABwevtpJ98hb720WW90TzfKgmD726oqFUDzl8kd8pLb0tSloxz5PhFfiWOxDD6kIpZz3gLMUCQGo7XLbhhJUZRotbK8vioygZAeqbiAhczoOiOJwBmPitgjc1wnI7wsAI9+gJ00dBcDYfzrwYV2xDn+cf29WwpT+GKc/I0u+4iIUfYN9Db0+k2JjdjpjWgK8O415T1uVFvKc70rF0zzH5U9PSYzi1rIoiqqUFCzmjy4B+DSo8u1ZO6E1tX2RciJlyOLX9ui6YzhdOZqljOpd0NN5m7gYHGm2EnVjpNqlVGYmi0F8x2dso4oUW0H4/eOT+zzfZc5Rv5JOqsvFPNHkuaXnVnLH3wiZvGbD6E7PkCCw6D82cc4q5B8GijHLQvdum0YJ3Lwq+P8R3L4M2WtzSL4MS+Mq3kvmAhXPkEF2DjYp8jta4uzRYbkyyveaaix+Imu/zdhhn/iYsqz4H2FJTp05XOVxzQPjYXuPGiPLzGvD2erCi2O80rpUVfJeVqOUd7YXuZuSmicoei+GUM4kW/XAp6weL+fHskxmJIEWzeMDplyyOyiYMh6hiGIHx4lGSWU7AWkpZUsSYJcZbtApl8y4hz7Q6rl1GSKCRYsSx3p3Iynk5nc3wQ99nA4HM7U0unIgpdx3J2XgMA54+e6ljYjSz9yU4Nf5/ds7ZrT4NQGqgtacbbuGhkDOnEmHXA2C76aORyH9gdpKLPgaIA5K6UrxhBKzSfNfB0qgbGge/iLh3v5pGzE+9ZngOKZ7NSxKCcIOSjJTzl5IKIoVLJ9+aU1eJJ8wbvSuTWVew6OWqQsych9GCTUu+a7nLxi6S4+FxitNKZNZxgUK3bg8smJD73nHO+YzHCYvqUvYLUzV25sKUVOQohTeJwISgKmG8A/1ufrP6aOpfgebcf0usw6hRD4NZNHKb2kl9hPUdzSE0txMS4I0rXjFHpl2S704+O2/XiMlpupXAx5/VU4xRTcy3mgMeyKwCWDvDVNq/kflx5Ir0QdbDbUMmfqhLsfW5ffK/VSdEStYFsKPcc1Ma21FvAc0MIoyWzG0E7Vf4OD27anF5oQa/L6enjTzwJY7neJP8WMObG1JuR58RDUWXvavO4epwdsWgslwK1x2agu8V969coJHAZxZDBrqIXmPXWGb+QlO5qmiOsD/qKn5hbKV3j7HIR4kZP9cHsz+518TdMGbmXUQu5Qz6dNe2IgutEwZOw3CxLSzprT7bvrwxaHMO+rOtiaWlqoO+7imdXaOoMp+znPG1t7hFnR8fLLkR2izfWmZmj3XrqaVi6I2J3aGjaW8aIlXnZw3upuXHr1azv3fgNEjdvbJxUzOutCMQLdxeX/L45asrlalbzJ8qp9nuU3GfGMiMLRXh9vYtNXtjli9/UClny6VXMEqhmZKciw8voO+w4oaqcbbidr6/VPnNqcd79lB9fxcmm2Jd45Or9UeZ2mvFHU4mFQhiK3DFfJ/pRABBW2/ll3u/Wmb6xd69b54woYK61k1of88w4PXj4KOiBFTeYrW62Lk0ixTr62cqVp4LvixCcPO3Be/ZZy6H1GbUnq+ETb29epr9td7ENshvTwOogi0xlsHbIM7Nq+g/r6vTybXypSISgF/GKeev4Igh8a2yotcRkyhnPPjK5SqduBMt5konX17KKOFnzFtnfnVBZ/GLE1j26WBA9IM+TgBHuQ92OGKaTDromJS7l1z60M5iqEgLXIENaCqvyqtvZ8i/hcD8lrhk2t5NJIo3A6hlGaW0CL49CtfymsbRd5IJG9tzUpiv0KaChyjEL1ZwbFV+zwRIZ1qbQLDiVkpalY2heC0tiKvF8K2epaM/cIlKLDJfNE+SsZqB8KcIusQ8MpWbCTWuIFzflTnE2W/9UBnDYCHr4WBBTwqCHAotbtSB3EiNvbhndGXqXrUALtJu3nRBP4s4vkFd+Y0Z9vUSOQD2MXKZHlqbCvlPOV+wICtavb/6ruVz8SxW0ZrFOlKMPsR8V5xt9cfSac2/Mo72uIluN0P5UBX6QA1y5zK18RClTztpy0hI9AoxZbHb+qlsQezqDuU06acra13U0FfjxSiIFC8+2vUh6JnQSfRdXl5GVOSnY/c7kt/SO02IMx5hxuW0vR9Bi/hwQ7fQij0OJkzcSUCqaItqXkJ9iqqSssaT5appmzhrpYNuT8ZXITx+bJf6Izzcr6zCNhuz0nokxAWb9JNXkKqJOk2Xe+lCod7bAA4PK7ni3PUDuhqWhajIYinBMue31HSWSgHWy57NhJuQWRMPdNZwwmuU5a5ewO4s9d7k+QuLe6rCG42yp4ClzFFBMelRtv7P1Gc0jKux27nR/0XcWMZV5ZHumPmK7zynpRgg8gdTDGmuZH6XyjJPeiU4coU7mNMXJ2RQRVc6fVoLcbpL9wE0u7iCRPM/XhDg1dPjcAzRTK3zP1cdrcV6J2Qa6xO0czRMsl5p1wndVhptJ38yswYDG+Lx0TXuE9OtW448ISS/dZEbE1l3jh+rvryHhmKjI7g3fPho3Ybf3cIOm08Q4J/9e4B60+9hDT7tJHAQ3PqcDDy++eQNpeuJzAT9W+zney0zSa6VAh0GRIUnL9ecVPbrSfSudbaXBeEqkpZPKYMIqofsNgmTbP8YmF4KkOqkGYBOBxEfdddhUogKjtb69jllrHxtVRNNTSXJm1BigJGMF2JGQ7hhc1sGujcDJKS0pCT6/tA6rvc7+VZePgOc6cKpHRAqL/UqmoGwUaII4YW6PSyOrzkKvUDqFVDwp5M05JeMsP9DVJoMb5c+OUEbauXypSTjw1JxZ8GKtLxp/nJsJUdiCf4iugSkRlp1k/CEo/AWu23PCP3l+USnu2D2pBsMArG9pQr6K/nWlZcWvco/rlSeOoIIBqys11ZQ8P0wSXngYhdh7Mw13ptwKMYlLYWXx2PIYMMey2IjzUJFaA9JOl9aXxftEm3whLA+UiKitmuj5vMXLK13dbulcp9Zuhn6ipoTDJ7HmUiK6PODzk8r9BzNV4Sr32325s4MM2mE3c0f7xaXXI1dGWWQ0kUYdcaN02I08pysCEI2wdgPV0y0dOIoOXDCkVYHpZjzyNMEsD8uxjPHE04LLBwLjtYDtxxpWS3lPHaW75bH71JbIa/UqU6CFuWgJph2JxHAUEk/jAEWL2VwenXZ68q7Kw4FTJhtg1gBmUyg2b2daNS2MxeKnhN1KO+GvcBuzT0BbPcNYrNmzZHobEBdXiVACsywEZjLijCETBy3JRKR9T1H0s0eF66MCKxPi3A/QOABU6WGselygYWnaHElirXdxhK3ofM8lqaFYLdc8+nV5pAEZ09FpVBLMgDadPMFdjro7RPtqffXDY3G6SW55WydDVuNRzCsXbBe143wN1KCteIY6w46+jGf4cV6o2VXdElb5nEi0rrpCNoVtCzWmsnmadL5CRBEliwURCSeK+wd0v5QpmoEWHpXS+bQD4HxVXFN4cnv37eOm0b0iEqUnApoVPsmVmLVoXF7aKrbrFVpGi8uRGEdJJTvG2ryxHRTonXSnVDCSrUOcbJh/ZErUXR8PsdBDDxb2+cxu2cvMNI6RW8nPVLpgKsE5xo8lwHy+Q8vjJHI3Ys/9heNjzr95woKQM4mlt9N9PbWKAllBfUVsmqJFinotQ9eI7iSMfrHcWncYEKpOHXmIyZMolyZFSguS8nxMu68ckhIe2pQFb/UtzgFYTDLnb3QeqCLNnaoWBOclEfa03uIIO48Rf62TlFSoVVX5fbcFjolPkEzt9XCBVP515sN4n3gYW21+J0+brxA6JhnF8zXpeYHoMrckXrtI5SnbHzYXOJV85P0bGzZ6LMcpq+FzE4fJSaELsac13YTOVHJhQlZNL82xxQt5Yq/C7Lxo4YbLa8TbzRGiAE2ZEWN9eieWPGmx3eVXiS6F3Ox5oloxWing49VlSwm/n5U2fdzpBJRxil3v0JJzbHNaU0wtV3mADVdQAPdzFDFWhSefoA/nenSF2eRlHGL542mty5eCepDQnux+njcaTTgkzkWD7p73zmq6jCCygjAvLu56q5fsezpf0P6qly5uk2bvdifsFQWSeckRVeVWl6qP+p1x5BNqcuhjZGVElkh03obX6yUOJsueT+wR5RhuRilnPB4zp+bOJffgGiErXVRVUkkj9Bi/0+Zlvb5UIbsjEn0ZN4MSwExhlRQP53d8Pmr83G5tdgf4hAp9h5w53RNXeGYeplXazjZTrNx1nc+wGZSaN7ixao3I3fr2cuDn2vHQiSs9td0s19xD/uU4J+Bha+PP9nBRuYp+4ISF5znXPSUOe9Yjq1raNmS2QYL+3NVoHW8P53baWJvoz4hXeuGC9CDzPC8pH4/+maA5omcNGG3bYSWd4Vle5aoKCCdP0iGfHIUmMbfmOorOb6YCATf6aIa/au9xvmTOfYEfCvYiOi0JMKRHxCBCfPlquc/uiMbt+U5pxHPaSKTCFk2c7zqW3Jo9BLj26ovhDrcZSyJznVz6jfYfJG94chBH8ejQcEMuZwnlaZkd4rQMUl+31SbztfvLOFY9LjHS2iO4ZkPZWYEIJdNwySEuVh5AnC45hbFBIwpIklcYfTLmmH2NOTx5OSoY5qw0WE4uhL5GaHV3RwlSirhNJ8o7oujCiure6/DT1GpOvYyvs1lpKSzNehxMnf0wQENCAp8xS24Zpelp85itEaJ0aew+zR7TC9dt6RJ5p3MtUU/Ae6UZa3j6Vec+56sCCnfQM5pGU3P20JYYNRrBfEiLOiDrbdNyxRklI0U19VpfrfBcCMz9MskgEbYsIbgti54nPAJMgWAgj3vyNOlx9HClyrA5hy05W6+xMk6IdWRarYSgo0v7+vPp1gnmK5C3JTKYJK0x801ZzkQGk0irkLbw8bqvfqSz+t67QmT3qPJs9kDzxFIQUD73X8t9mUT10peLSzrCFhRlV44ZX+YnQzJV1dHXGrqsepEKZp2Pdf6EIpWrQ9I8uW3RiOjtaoxslj7Wio2TxMgMV3x1TztpL2VxjPAhuiu9ZkrCmYTOy8Cv2vkhlPpjtNo0S/2pv2sxfD8T0uzlIZlf+IrpgaqCDhT+OuesGt5Zset1cYOOM+o8AY+ThpqHNLsPSTIUXUAMUjh0/DP/eF3V12VnzFmsi0Ge9os9ulqPYhNWnlZOCDc2aJ9u3FDnwRgXQlyqfepVZ056tAX9h3AIkXoOPYYPvncf8rwbShK6np0ZZEHay+O+tHqJ7pVKE4K5FWkf0kW45TmC7ttzP/UBJ5+BtfgJWdcXezYuoiG3Z3op58BRrip9IbnVe65SRwn71DHDGXcfYfIAdEiW0aCXT6567le96/dJanM+M4dyB/2NgC8EHVUnaLdPMOeeYOEVJwWZ3Ai4aU4yfEbvmRW0XdK9PGwZJ5RPp643iuSyR7lRTHCq8Ompr14P9QmyHkYQkmg7dt1bZL1fcH18vgxu98PYAcwUzOQPg3xgUteDLpHK0mCt6t27Bqae98ulGtqEuUAuGvnO+fZA9KAMwJi5hvi5iln4HNac4ZP8w+zKaX6UjAGfN1UL4Vc1vyw26hBqQHH0dX4gBP4I4FNPbsRLqTey66gSqryzDgGvytpp9Eg0CBqfgnVah89z3PuxR138cdZmCEAb4XbOzuN9DUMPIwgKplPGwEnEl4xIgtHcSyl4ZlM+eZbl8vpkFC76PLbQPt1DzqdxUtom267kJzpru7UOKSnCS3mCbzAResYpJbOZCUeptCqxbfozWztYivEnEn2ywhNMv4QdKuglWYPA4f1wEZy2EQ1f1hUoDgIiixSMHNPbKiQ176e2UlvSvD/zOHpyJidJW2q87OdO50VfGK6qrVGYl0eOUeZtAzNJYEhz0IJ50HBWqdZ8AVsCpnQX08oTQwzn9Jwbwovxzg9KiGWto8cjlgUzP1nhhtKRoojhEO3rq73WKH6LDXdgzvuy3tgnxPlrzIpN8P6p6QjG2OOCqhGqAsore6p6lBfQeOUN3jXouPBYM+t2rC0CbxtjFg7NevSvD2R7IidPLS7US7OWveFE6fa025QSwhRBHVSV5TvmULtC8+2IMuQuIZ2tCcUMfIGdErtGx9ulhhYpWLC6fFYy2bCQ/TqBHBxjkXPO8CYGdSwjRIuU+iozjcox4/BACuwCsTopqLVqFvTCJCOj1ra1eeELtikOUSNNixKBD5eWJqpH8zpNkY13K0ROQ5XDGVuKl8dmlfw0b9LV8xt8iHPVYLCz6CnegDd9CUmGMfEscXFCvb/2D4PLh97i0KUufEd7bXfSmO7ROe6POuXEEuIBapqfip289lmGaXm5A5/URZ5J6vM2HVcs4vmHvBCmNw8V6ywdigTxrlpHAXOsLdWp7XnDzohb0Ueel1HxTONXMrtW2cV4DpHtG/eqgHsmq8V2PFoPt8rCVhwLSyHW55CATi4lPVe9+KUZRR4dHTyMUG7upQfe7efobAh1eV/2snzdzlKfoc4+XO8eWpUVv1t32pe4p2ef/AtHLpKAJIKqP4pqxGrGWGcfhhf5ZvnlEz/bKZ+yLOxxMj57Z8/284XDTJPgz4LzVN3TSGbdFL68YFxAw+2kjUkG3xDWsn/sYeQgo6cOzPNpVjjidAqdy+JACUdVX9oK7wlk5lzHobi49Vnu0VD9lrtSEt7zbE5OQsEPI3XRTs7uk4BvgloaI3TS8pFfl95C3H5EKb9/KcfcybpEPKuBRDg9IqdxrMXxjRRJlCStM85IKPCa7zQKdjK0lx2lLpR303TT5Py4VI/1kiD8laoLKhYn/exfbs288clZupW1+LgIvI8ceVd4sXSkoo/G7BjJseFdsvxmbMhXFdtXPyfzYuOuwdAdrZXlH5d7xs30dpk8fh0iQFfN43JRdaq8d5wfP7rjS84euFUw26nP4/uU6KTPrmZwv01TIMnkTJkXITXhGLKccrdeiR67l9ATjjKcAUxultHRicpXg5fjNdVavnQme1DmKsYJg/JYbMT5ck9uZw+X8Cff9xpPZ6wvxy+lH+qbxPhBgJDt5YQKMoc2LbM+AdnKIad6PDrnISsohm8dmIgkXkWMDjzAkCqVdN0Wmue6K5wV+TUT1GNZaJ4gshdLu2rry2xz49QYWfVQg2myj7drNCQUFgTX7VoOIX/sTq+Vbmm3COlJt1ppPkcRV+aqq5FHCJ5bagm1Uh96lCPRq1Vv14CUm57xdiWKM46U9mf8vJOVrmt5D6DcNW/xq4ElcXZQWiWavLb0yF+1lWgBn1Hl03A+a8I8jgvfKIkukJe1Auivi4/QzHHTgaUTtWX6HBvPYn+5mITkr7wRoxTC2rRk9dRIGpJBnAQU/2UfQ027RAiCQo6vcvcLFwBK+FSi8+Z1XkM9hZPGTLbFMdKEhuozpwVNoPMpoplwNeapd7DXFU/ceJYKeQ+qyJfh2zzKSkkz4tU2xSXjLvEFamXcyVl/ypWBa6ZbV1xHzMEkQWskUu38asZUgpXJPWoZSLn5jFzkrmFtNllTedMxV0yCFHHt7glyYU5BXSTz84iNhOU8CXhQz9NTjIsnO8WWV4UJxgnEHiBiVXAV3w+d6xFLhYb07bJmGRUaoSZAEW4d41ge0hUNXiti5Sch5PQbK1c0dLvSz9MJy8wAh+rVO9vY63S7qNDUcYV+zclusSJUDl56nhWygSdqECKx3tRUGun3C/EM6uBZceh0Jq/UnIw19HoIyHSB7MpkK0QNIsLBz3wzHAE4BTfCAfjRo6Z7pDB/NlvNp2ElWK9sjGwLtJI20dHtSigsd0u3NJRTSws6DQzyEKWk+mtnakzWHpg8GVbh9S87tifMwrJYWBU9jeGCXFAzckSURu5uNkccxQIuzO/I5JxY5Ph0Bro5Wav7NOz48oKN4cKYUS+vxOmp5NvuDxX9JC6pNw4eJsnNa8Ifj50MZBK/1LOVDQRH2EB7c8FrlFmEI5isZ/3Ih2hvm2upiRqjx5Upz57iZueS72/KdL4aE2DEW9nyD0U+pudUtPfmKmjPSfQ6p9iLxer0AA2jRYJhxofphrRY3Vq4nhRmI8AUHdWqjtjGm/9yqwIltWOz7ka06Ek8ak6AV30drUZyvAc4mteZ0EDw6j/kjdde0FRltBdqjzM0uya5uws59IphDW5NOWcNon1yXg3oxZBkX7jS7qfjbg160g0D0+2S6+9t28bpMRwG1iR1j3722WCxDlHNyjJdeOyqdTHPQj7vbrj+KEfdwGrExqV5otW7MLuGjC/9Jr84hGL5dU+83aYCjFEYk75erk2JZve7Vs0OHdtHEtZV1d97JN41TYnW/YpXgFCbJFk3ELnnhtcgWeizYiTQgVytyKuOo/zMOdlUu42218TIuPLTd0zsqXfBdX9M9Y2u/bVJuug5OR7ImEjzqkJrLn4xUvuJ9pyXdG9wXPT4VmxbWzOp0OexF7neOQQXvD0L1SLxFLHxHpJ7cR27IhlGNO+nXbgttXgSHOZyZV32pIsWbJ4j5Hnu7mKZdJ0w7E/2aT4I15f8tPZE24lCf67xRwnTNaiiM2+xmjXBIufrXVQwmpg+Al9mnVa4Rtxw1YNCzDhOj2EF0Kb6fg17qXnim10VYSM6z76zQZXTp8ANN1sNlbQhHiVv894DDMcOR5+v1TKYxpMhnulmGHR3zsap10lpbKk9dDuRPjPY7Ir6HBxRdqC9V31Bu4Ylwch3320oR3sAiiIZ9EnaexAhYZfu3Bin0fawWyZHlcYsIg/V1uNik46dPtSRmKZlkaJS800CzgN1vr3ca3bT+eWIXi7nTBdSLdURYvZOo5y/spi8inykBqyimPsgC2bh3PnhwdomYHB3nXHQSd9WzjIQ9C5F0iOzx5Y4b1f5bk2y/ZJ0gClwhj40iJdZNcasmXYYrKs0jZAsCFmLh3A0K+bEA/8aljdSJpSsKF4pIx7OwkZWj9QDI3U6CfUZxSlaQAoEry18uEKYqD2H9H7Z4z4GM3FP3/TO0W+N2z+KFOU3/Ra4T0VIHzSRtCscPB/igO9ntxACV1ZfQ/Z0MiOAiVpelPlVLGrpyEuVo8eFdu+y35+fYitW+CsjOWW73u9D77PoqzXgLLhvooIyhm4CiiM+efURCO2Rw3PLFM9PZr5jYEAXkUydd8w/XlQVDCa3zlVMC992NN37qnqVNk7B/tHgq+3IAwJnl71a4mTXaOymS/upsy/BZYmWu4xwuJqpZm8tTjiQo7QSFnkOL2bfyVvIX1lfCWYJ3/rmCmZCuucH1/BZ103hl6QMlN9xWLA+TmDSZD3lDqMWtztxQko9Lt3JGDaToRXs84mlizM0GLNVVWBok72HTCQIRFBlHEr0ft6YRWtx5qFLmHT2LGF5noqGXPaQ8m5qawKOM3Xt+dzxkI4+WwhGWfcJ5v3Zk29bLkQwl6FeKDdTXc/e/b548yMlOv+acrhNl9RTupG2XYTPdWLQI4xgj1uF3Jjt/Tsydh+thyE5PmRdwrlIgy48qup2NYznhpKYTc9mLU+AeXd6OcwvkXpi9l5wR721eVfhQitB4W692YAlUBDMV66VegPv1Mf5Zap+fGLJZ6whxU4VDKUJcMjkAscXKRHjEEy4i36ryCgSu+NTpnfUFq8QC0ace3vsLykrji4ux8QldItFOEW7z61yjTfDKUbY83GrqUiszRfrLbqXUDYC94S4vhLK0RJE6LIs3efbU8JElDg9dHeRKETpar/OIAtRARhA3Xh7aZRySuAhVKdykLwyjNXwmvvSjWPnub0uTaVXxH2txdmdE+mYeV6XQ/l6S61zsRribqp1lmwt5eIO1ULXYRD1LryRZVESmczG+BVWbrOtKDT0bIsZvR6n9Xp5XhwvOzFR4TqaV2BnSD9eF54ptbO6SBmjjFiTywYVkFoxbcFdjTwkuUMkRoTQ1Z/nhtVZ+ziAMZmA+OO4iCcydQFwUKni5Mad2pGH6YuWRrPV4BnBYjmPKrAXuL9waHh/gZ7eb95pud0Z9Z7BAuzcr27hpiwNQqZaxmVFEqrYtdRzsXC8NgTCs9TmEfdF82APeYHKpoplOxHXCGma16JfrxbdudQObxHmsc8YrF5VU8ga6zSr/Dzcg2RLmQgHJIOukvoFw9oZMqMOQfqLfOxTGx4IdNFl95LUc2Ox14LL/G5ic1+ln1DsLvFNdzwbR5SRRvKEOuLXENYvt6iwl+cyuVTVO8GQJLeXwYz+sYVhV0lyDsMdRrSR0/Ag6NP9glkRr57g+ygadtRBi/567u5zqkGK1Xj4ulwaGyApFFbp09KeAsMw//mfH7c9qvjrhZj/8jb6+7bA/2+XFr7cL2iX93XRMP648hL70c8fe/38X5vyP378NIQ5MOTLdYyxmtNv1xf+3WWMz980fn5r/PyHyxhfbsf++r6uG2/Tt1tCE2BKb6u+CX69QvPpw+pwHj7uYn+7l7N/DjM/f9+eqX9/WfBt5cf/NfBxhQT5CQO2/ut/AVd1HMRERQAA -->
