---
name: "rar-aibast-agents-library-license-renewal-expansion"
description: "Manages renewal pipelines and churn risk from a live simulated Dynamics 365 tenant's cases and quotes, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/license_renewal_expansion", "rar_sha256": "398c857f909ae664d8aac2632735ab54f932f7a4a42efd9e91055e0c8d8fc213", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["license", "renewal", "expansion", "churn", "revenue", "saas"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/license_renewal_expansion`. The original RAPP
agent is preserved byte-for-byte in `license_renewal_expansion_agent.py` and in the RCI capsule.

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

License Renewal and Expansion Agent — a template you are meant to mutate.

Manages SaaS license renewal pipelines, identifies expansion opportunities,
assesses churn risk, and projects revenue impact across the customer
portfolio.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live renewal signals over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="renewal_pipeline")
     — with network up, the pipeline surfaces the tenant's live renewal
     cases such as CAS-260134 "License renewal quote requested before
     expiration" (Summit Trail Software) alongside the live open quote
     book. In this template a renewal signal is a Dynamics case and a
     renewal proposal is a Dynamics quote.
  2. No network? Everything falls back to the embedded demo layer below
     (LICENSE_AGREEMENTS / EXPANSION_PRICING) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     LICENSE_RENEWAL_EXPANSION_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your CPQ/billing
     system), or replace _fetch_collection() with your own subscription
     API. The fields the rest of the file needs are listed in
     _normalize_live_renewal_signal() — ARR, seats, and health scores
     stay "n/a — enrichment seam" until you wire your billing/CS data.

OPERATIONS
  renewal_pipeline | expansion_opportunities | churn_risk |
  revenue_impact | account_health_analysis | competitive_strategy |
  renewal_proposal | activate_renewal_package
  kwargs: operation (required), license_id

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "license_id": {
      "description": "Optional license ID to filter results.",
      "type": "string"
    },
    "operation": {
      "description": "The license management operation to perform.",
      "enum": [
        "renewal_pipeline",
        "expansion_opportunities",
        "churn_risk",
        "revenue_impact",
        "account_health_analysis",
        "competitive_strategy",
        "renewal_proposal",
        "activate_renewal_package"
      ],
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `license_renewal_expansion_agent.py` and embedded as the fenced Python below (sha256 398c857f909ae664…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `license_renewal_expansion_agent.py` first:

```bash
python3 license_renewal_expansion_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 license_renewal_expansion_agent.py   # or on stdin
python3 license_renewal_expansion_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
License Renewal and Expansion Agent — a template you are meant to mutate.

Manages SaaS license renewal pipelines, identifies expansion opportunities,
assesses churn risk, and projects revenue impact across the customer
portfolio.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live renewal signals over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="renewal_pipeline")
     — with network up, the pipeline surfaces the tenant's live renewal
     cases such as CAS-260134 "License renewal quote requested before
     expiration" (Summit Trail Software) alongside the live open quote
     book. In this template a renewal signal is a Dynamics case and a
     renewal proposal is a Dynamics quote.
  2. No network? Everything falls back to the embedded demo layer below
     (LICENSE_AGREEMENTS / EXPANSION_PRICING) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     LICENSE_RENEWAL_EXPANSION_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON exported from your CPQ/billing
     system), or replace _fetch_collection() with your own subscription
     API. The fields the rest of the file needs are listed in
     _normalize_live_renewal_signal() — ARR, seats, and health scores
     stay "n/a — enrichment seam" until you wire your billing/CS data.

OPERATIONS
  renewal_pipeline | expansion_opportunities | churn_risk |
  revenue_impact | account_health_analysis | competitive_strategy |
  renewal_proposal | activate_renewal_package
  kwargs: operation (required), license_id
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timezone


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/license_renewal_expansion",
    "version": "1.2.0",
    "display_name": "License Renewal & Expansion Agent",
    "description": "Manages renewal pipelines and churn risk from a live simulated Dynamics 365 tenant's cases and quotes, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["license", "renewal", "expansion", "churn", "revenue", "saas"],
    "category": "software_digital_products",
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
#   export LICENSE_RENEWAL_EXPANSION_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CPQ/billing client.
# Downstream code only needs the fields from
# _normalize_live_renewal_signal().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "LICENSE_RENEWAL_EXPANSION_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
_LIVE_CACHE = {}

# Case-title keywords that mark a tenant case as a renewal signal.
_RENEWAL_KEYWORDS = ("renewal", "license", "subscription", "expansion")


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


def _normalize_live_renewal_signal(row):
    """Project a Dynamics case (incident) record onto the shape this agent
    uses — in this template a renewal signal IS a Dynamics case (a
    renewal proposal is a Dynamics quote). THIS is the contract your
    replacement data source must meet — a dict with these keys. None
    means 'not available from CRM alone' and the renderers label it as
    an enrichment seam."""
    return {
        "signal_id": row.get("ticketnumber", row.get("incidentid", "")),
        "customer": row.get("customeridname", "Unknown"),
        "subject": row.get("title", "untitled"),
        "priority": row.get(
            "prioritycode@OData.Community.Display.V1.FormattedValue", "Normal"
        ),
        "status": row.get(
            "statecode@OData.Community.Display.V1.FormattedValue", "Active"
        ),
        "csm": row.get("owneridname", "Unassigned"),
        "age_days": _age_days(row.get("createdon")),
        "open": row.get("statecode") == 0,
        "arr": None,           # enrichment seam — wire your billing system
        "seats": None,         # enrichment seam
        "health_score": None,  # enrichment seam — wire your CS platform
        "_live": True,
    }


def _age_days(iso_date):
    try:
        then = datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
        return max(0, (datetime.now(timezone.utc) - then).days)
    except (ValueError, TypeError):
        return 0


def _live_renewal_signals():
    """Live tenant cases whose titles look renewal-shaped; [] offline."""
    signals = []
    for row in _fetch_collection("incidents"):
        title = str(row.get("title", "")).lower()
        if any(kw in title for kw in _RENEWAL_KEYWORDS):
            signal = _normalize_live_renewal_signal(row)
            if signal["signal_id"]:
                signals.append(signal)
    return signals


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback) — Synthetic domain data
# ---------------------------------------------------------------------------

LICENSE_AGREEMENTS = {
    "LIC-3001": {
        "customer": "Pinnacle Insurance Corp",
        "plan": "Enterprise",
        "arr": 288000,
        "seats": 150,
        "seats_used": 142,
        "renewal_date": "2026-04-30",
        "contract_start": "2025-04-30",
        "usage_trend": "increasing",
        "nps_score": 72,
        "support_tickets_90d": 4,
        "expansion_signals": ["API usage +45% QoQ", "Requested SSO for 3 subsidiaries"],
        "churn_signals": [],
        "csm": "Dana Reeves",
        "health_score": 88,
    },
    "LIC-3002": {
        "customer": "ClearView Analytics",
        "plan": "Professional",
        "arr": 72000,
        "seats": 30,
        "seats_used": 18,
        "renewal_date": "2026-05-15",
        "contract_start": "2025-05-15",
        "usage_trend": "declining",
        "nps_score": 34,
        "support_tickets_90d": 18,
        "expansion_signals": [],
        "churn_signals": ["Usage down 32%", "Executive sponsor departed", "Competitor eval detected"],
        "csm": "James Okafor",
        "health_score": 29,
    },
    "LIC-3003": {
        "customer": "Redwood Supply Chain",
        "plan": "Enterprise",
        "arr": 192000,
        "seats": 80,
        "seats_used": 79,
        "renewal_date": "2026-06-01",
        "contract_start": "2025-06-01",
        "usage_trend": "stable",
        "nps_score": 65,
        "support_tickets_90d": 7,
        "expansion_signals": ["Inquired about analytics add-on"],
        "churn_signals": ["Budget freeze mentioned in QBR"],
        "csm": "Dana Reeves",
        "health_score": 62,
    },
    "LIC-3004": {
        "customer": "Skyline Hospitality Group",
        "plan": "Enterprise",
        "arr": 360000,
        "seats": 250,
        "seats_used": 248,
        "renewal_date": "2026-04-15",
        "contract_start": "2025-04-15",
        "usage_trend": "increasing",
        "nps_score": 85,
        "support_tickets_90d": 2,
        "expansion_signals": ["Opening 12 new locations", "Requested bulk seat pricing", "Custom integration POC"],
        "churn_signals": [],
        "csm": "James Okafor",
        "health_score": 94,
    },
    "LIC-3005": {
        "customer": "Granite Construction Co",
        "plan": "Professional",
        "arr": 54000,
        "seats": 20,
        "seats_used": 12,
        "renewal_date": "2026-07-01",
        "contract_start": "2025-07-01",
        "usage_trend": "declining",
        "nps_score": 41,
        "support_tickets_90d": 11,
        "expansion_signals": [],
        "churn_signals": ["Primary admin inactive 45 days", "Missed last 2 QBRs"],
        "csm": "Dana Reeves",
        "health_score": 35,
    },
}

EXPANSION_PRICING = {
    "additional_seats": {"unit_price": 120, "min_qty": 10},
    "analytics_addon": {"price": 24000, "description": "Advanced analytics module"},
    "api_premium": {"price": 18000, "description": "Premium API tier with higher rate limits"},
    "sso_subsidiary": {"price": 12000, "description": "SSO extension per subsidiary"},
    "custom_integration": {"price": 36000, "description": "Custom integration package"},
}

RENEWAL_STRATEGIES = {
    "LIC-3001": {
        "competitor": "AtlasCloud",
        "competitor_discount": "18%",
        "switching_cost": 132000,
        "differentiators": ["45% QoQ API growth", "proven SSO integrations", "zero migration downtime"],
        "package": "Enterprise multi-year plus three subsidiary SSO extensions",
        "term": "36 months",
        "annual_value": 324000,
        "concession": "8% year-one expansion discount",
        "roi": "2.5x versus migration and retraining costs",
        "negotiation_levers": ["phased SSO rollout", "price protection", "executive success review"],
        "approvals": ["Sales VP", "Finance", "Legal"],
    },
    "LIC-3002": {
        "competitor": "NovaMetrics",
        "competitor_discount": "22%",
        "switching_cost": 58000,
        "differentiators": ["existing analytics workflows", "retained historical data", "named CSM recovery plan"],
        "package": "Professional renewal with adoption recovery services",
        "term": "12 months",
        "annual_value": 72000,
        "concession": "services credit after 80% adoption",
        "roi": "1.8x versus replacement and migration costs",
        "negotiation_levers": ["90-day adoption milestone", "executive sponsor reset", "quarterly value review"],
        "approvals": ["Sales Director", "Customer Success VP"],
    },
    "LIC-3003": {
        "competitor": "ChainSight",
        "competitor_discount": "12%",
        "switching_cost": 87000,
        "differentiators": ["79 of 80 active seats", "embedded supply-chain workflows", "analytics add-on readiness"],
        "package": "Enterprise renewal with advanced analytics",
        "term": "24 months",
        "annual_value": 216000,
        "concession": "analytics implementation included",
        "roi": "2.2x from avoided migration and faster analytics",
        "negotiation_levers": ["two-year price lock", "analytics pilot", "usage-based expansion review"],
        "approvals": ["Sales VP", "Finance"],
    },
    "LIC-3004": {
        "competitor": "GuestOps",
        "competitor_discount": "15%",
        "switching_cost": 164000,
        "differentiators": ["99% seat utilization", "12-location expansion", "custom integration proof of concept"],
        "package": "Enterprise expansion for 12 new locations with custom integration",
        "term": "36 months",
        "annual_value": 402000,
        "concession": "bulk-seat price protection",
        "roi": "2.9x from rollout speed and avoided re-platforming",
        "negotiation_levers": ["location ramp schedule", "integration milestone", "multi-year price protection"],
        "approvals": ["Sales VP", "Finance", "Solutions Engineering"],
    },
    "LIC-3005": {
        "competitor": "BuildFlow",
        "competitor_discount": "20%",
        "switching_cost": 41000,
        "differentiators": ["existing project history", "configured workflows", "re-engagement playbook"],
        "package": "Professional renewal with guided reactivation",
        "term": "12 months",
        "annual_value": 54000,
        "concession": "60-day adoption services credit",
        "roi": "1.6x versus replacement and retraining costs",
        "negotiation_levers": ["admin reactivation", "usage milestone", "monthly CSM review"],
        "approvals": ["Sales Director", "Customer Success VP"],
    },
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _exact_license(license_id):
    if not license_id:
        return None, "Provide an exact license_id: " + ", ".join(sorted(LICENSE_AGREEMENTS))
    if license_id not in LICENSE_AGREEMENTS:
        return None, f"Unknown license_id `{license_id}`; exact ID required."
    return LICENSE_AGREEMENTS[license_id], None

def _renewal_pipeline():
    pipeline = []
    for lid, lic in LICENSE_AGREEMENTS.items():
        risk = "low" if lic["health_score"] >= 70 else ("medium" if lic["health_score"] >= 50 else "high")
        pipeline.append({
            "id": lid, "customer": lic["customer"], "arr": lic["arr"],
            "renewal_date": lic["renewal_date"], "health_score": lic["health_score"],
            "risk": risk, "csm": lic["csm"],
        })
    pipeline.sort(key=lambda x: x["renewal_date"])
    total_arr = sum(p["arr"] for p in pipeline)
    at_risk_arr = sum(p["arr"] for p in pipeline if p["risk"] == "high")
    return {"pipeline": pipeline, "total_arr": total_arr, "at_risk_arr": at_risk_arr}


def _expansion_opportunities():
    opps = []
    for lid, lic in LICENSE_AGREEMENTS.items():
        if not lic["expansion_signals"]:
            continue
        potential = 0
        items = []
        seat_util = round(lic["seats_used"] / lic["seats"] * 100, 1)
        if seat_util > 90:
            seat_rev = EXPANSION_PRICING["additional_seats"]["unit_price"] * 50
            potential += seat_rev
            items.append({"type": "additional_seats", "value": seat_rev})
        for signal in lic["expansion_signals"]:
            if "analytics" in signal.lower():
                potential += EXPANSION_PRICING["analytics_addon"]["price"]
                items.append({"type": "analytics_addon", "value": EXPANSION_PRICING["analytics_addon"]["price"]})
            if "sso" in signal.lower():
                val = EXPANSION_PRICING["sso_subsidiary"]["price"] * 3
                potential += val
                items.append({"type": "sso_subsidiary", "value": val})
            if "integration" in signal.lower():
                potential += EXPANSION_PRICING["custom_integration"]["price"]
                items.append({"type": "custom_integration", "value": EXPANSION_PRICING["custom_integration"]["price"]})
        opps.append({
            "id": lid, "customer": lic["customer"], "current_arr": lic["arr"],
            "expansion_potential": potential, "items": items, "signals": lic["expansion_signals"],
        })
    opps.sort(key=lambda x: x["expansion_potential"], reverse=True)
    return {"opportunities": opps, "total_potential": sum(o["expansion_potential"] for o in opps)}


def _churn_risk():
    risks = []
    for lid, lic in LICENSE_AGREEMENTS.items():
        if not lic["churn_signals"]:
            continue
        seat_util = round(lic["seats_used"] / lic["seats"] * 100, 1)
        risks.append({
            "id": lid, "customer": lic["customer"], "arr": lic["arr"],
            "health_score": lic["health_score"], "nps": lic["nps_score"],
            "seat_utilization": seat_util, "usage_trend": lic["usage_trend"],
            "signals": lic["churn_signals"], "tickets_90d": lic["support_tickets_90d"],
        })
    risks.sort(key=lambda x: x["health_score"])
    return {"at_risk": risks, "total_arr_at_risk": sum(r["arr"] for r in risks)}


def _revenue_impact():
    renewal = _renewal_pipeline()
    expansion = _expansion_opportunities()
    churn = _churn_risk()
    base_renewal = renewal["total_arr"]
    expansion_val = expansion["total_potential"]
    churn_val = churn["total_arr_at_risk"]
    best_case = base_renewal + expansion_val
    worst_case = base_renewal - churn_val
    expected = base_renewal + round(expansion_val * 0.4) - round(churn_val * 0.3)
    return {
        "base_renewal_arr": base_renewal, "expansion_potential": expansion_val,
        "churn_risk_arr": churn_val, "best_case": best_case,
        "worst_case": worst_case, "expected": expected,
    }


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

class LicenseRenewalExpansionAgent(BasicAgent):
    """License renewal pipeline and expansion opportunity agent."""

    def __init__(self):
        self.name = "LicenseRenewalExpansionAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "renewal_pipeline",
                            "expansion_opportunities",
                            "churn_risk",
                            "revenue_impact",
                            "account_health_analysis",
                            "competitive_strategy",
                            "renewal_proposal",
                            "activate_renewal_package",
                        ],
                        "description": "The license management operation to perform.",
                    },
                    "license_id": {
                        "type": "string",
                        "description": "Optional license ID to filter results.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "renewal_pipeline")
        if op == "renewal_pipeline":
            return self._renewal_pipeline(kwargs.get("license_id"))
        elif op == "expansion_opportunities":
            return self._expansion_opportunities()
        elif op == "churn_risk":
            return self._churn_risk()
        elif op == "revenue_impact":
            return self._revenue_impact()
        elif op == "account_health_analysis":
            return self._account_health_analysis(kwargs.get("license_id"))
        elif op == "competitive_strategy":
            return self._competitive_strategy(kwargs.get("license_id"))
        elif op == "renewal_proposal":
            return self._renewal_proposal(kwargs.get("license_id"))
        elif op == "activate_renewal_package":
            return self._activate_renewal_package(kwargs.get("license_id"))
        return f"**Error:** Unknown operation `{op}`."

    def _live_renewal_pipeline(self, signals):
        """Pipeline built from live tenant cases + quotes (preferred online)."""
        quotes = _fetch_collection("quotes")
        open_quotes = [q for q in quotes if q.get("statecode") in (0, 1)]
        quote_book = sum(float(q.get("totalamount") or 0) for q in open_quotes)
        lines = [
            "# Renewal Pipeline — Live Tenant Signals",
            "",
            f"Live records from {DATA_SOURCE_URL} (Aster Lane Office Systems).",
            "In this template a renewal signal is a Dynamics case and a renewal",
            "proposal is a Dynamics quote. Pass `license_id` (e.g. LIC-3001)",
            "for the embedded demo pipeline.",
            "",
            "## Renewal Signals (live cases)",
            "",
            "| Case | Customer | Subject | Priority | Status | CSM | Age | ARR | Health |",
            "|------|----------|---------|----------|--------|-----|-----|-----|--------|",
        ]
        for s in sorted(signals, key=lambda x: x["signal_id"]):
            arr = "n/a — enrichment seam" if s["arr"] is None else f"${s['arr']:,}"
            health = "n/a — enrichment seam" if s["health_score"] is None else str(s["health_score"])
            lines.append(
                f"| {s['signal_id']} | {s['customer']} | {s['subject']} "
                f"| {s['priority']} | {s['status']} | {s['csm']} "
                f"| {s['age_days']}d | {arr} | {health} |"
            )
        lines.append("")
        lines.append("## Open Quote Book (live quotes)")
        lines.append("")
        lines.append("| Quote | Customer | Amount | Status |")
        lines.append("|-------|----------|--------|--------|")
        for q in sorted(open_quotes, key=lambda x: x.get("quotenumber", "")):
            status = q.get(
                "statecode@OData.Community.Display.V1.FormattedValue", "Active"
            )
            lines.append(
                f"| {q.get('quotenumber', '?')} | {q.get('customeridname', '?')} "
                f"| ${float(q.get('totalamount') or 0):,.2f} | {status} |"
            )
        lines.append("")
        lines.append(
            f"**Open quote book value:** ${quote_book:,.2f} across "
            f"{len(open_quotes)} quotes"
        )
        lines.append(
            "ARR, seats, and health scores need your billing/CS systems — "
            "wire them at the LIVE DATA SEAM."
        )
        return "\n".join(lines)

    def _renewal_pipeline(self, license_id=None) -> str:
        if not license_id:
            signals = _live_renewal_signals()
            if signals:
                return self._live_renewal_pipeline(signals)
        data = _renewal_pipeline()
        lines = [
            "# Renewal Pipeline",
            "",
            f"**Total Renewal ARR:** ${data['total_arr']:,}",
            f"**At-Risk ARR:** ${data['at_risk_arr']:,}",
            "",
            "| Customer | ARR | Renewal Date | Health | Risk | CSM |",
            "|----------|-----|-------------|--------|------|-----|",
        ]
        for p in data["pipeline"]:
            lines.append(
                f"| {p['customer']} | ${p['arr']:,} | {p['renewal_date']} "
                f"| {p['health_score']} | {p['risk'].upper()} | {p['csm']} |"
            )
        return "\n".join(lines)

    def _expansion_opportunities(self) -> str:
        data = _expansion_opportunities()
        lines = [
            "# Expansion Opportunities",
            "",
            f"**Total Expansion Potential:** ${data['total_potential']:,}",
            "",
        ]
        for opp in data["opportunities"]:
            lines.append(f"## {opp['customer']} (Current ARR: ${opp['current_arr']:,})")
            lines.append(f"**Expansion Potential:** ${opp['expansion_potential']:,}")
            lines.append("")
            lines.append("**Signals:**")
            for s in opp["signals"]:
                lines.append(f"- {s}")
            lines.append("")
            lines.append("| Expansion Item | Value |")
            lines.append("|---------------|-------|")
            for item in opp["items"]:
                lines.append(f"| {item['type'].replace('_', ' ').title()} | ${item['value']:,} |")
            lines.append("")
        return "\n".join(lines)

    def _churn_risk(self) -> str:
        data = _churn_risk()
        lines = [
            "# Churn Risk Assessment",
            "",
            f"**Total ARR at Risk:** ${data['total_arr_at_risk']:,}",
            "",
        ]
        for r in data["at_risk"]:
            lines.append(f"## {r['customer']} (ARR: ${r['arr']:,})")
            lines.append(f"- Health Score: {r['health_score']}")
            lines.append(f"- NPS: {r['nps']}")
            lines.append(f"- Seat Utilization: {r['seat_utilization']}%")
            lines.append(f"- Usage Trend: {r['usage_trend']}")
            lines.append(f"- Support Tickets (90d): {r['tickets_90d']}")
            lines.append("")
            lines.append("**Churn Signals:**")
            for s in r["signals"]:
                lines.append(f"- {s}")
            lines.append("")
        return "\n".join(lines)

    def _revenue_impact(self) -> str:
        data = _revenue_impact()
        lines = [
            "# Revenue Impact Projection",
            "",
            f"**Base Renewal ARR:** ${data['base_renewal_arr']:,}",
            f"**Expansion Potential:** ${data['expansion_potential']:,}",
            f"**Churn Risk ARR:** ${data['churn_risk_arr']:,}",
            "",
            "## Scenarios",
            "",
            "| Scenario | Projected ARR |",
            "|----------|--------------|",
            f"| Best Case (full expansion, no churn) | ${data['best_case']:,} |",
            f"| Expected (40% expansion, 30% churn) | ${data['expected']:,} |",
            f"| Worst Case (no expansion, full churn) | ${data['worst_case']:,} |",
            "",
            "## Recommendations",
            "- Prioritize executive engagement for high-churn-risk accounts.",
            "- Fast-track expansion proposals for Skyline Hospitality and Pinnacle Insurance.",
            "- Assign dedicated CSM resources to ClearView Analytics and Granite Construction.",
        ]
        return "\n".join(lines)

    def _account_health_analysis(self, license_id) -> str:
        lic, error = _exact_license(license_id)
        if error:
            return f"**Error:** {error}"
        strategy = RENEWAL_STRATEGIES[license_id]
        utilization = round(lic["seats_used"] / lic["seats"] * 100, 1)
        lines = [
            f"# Account Health Analysis — {lic['customer']}",
            "",
            f"**License ID:** {license_id}",
            f"**Health Score:** {lic['health_score']}/100",
            f"**Feature Adoption:** {utilization}% seat utilization",
            f"**Usage Trend:** {lic['usage_trend']}",
            f"**Support Tickets (90d):** {lic['support_tickets_90d']}",
            f"**Renewal ARR:** ${lic['arr']:,}",
            "",
            "## Expansion Signals",
        ]
        if lic["expansion_signals"]:
            lines.extend(f"- {signal}" for signal in lic["expansion_signals"])
        else:
            lines.append("- None")
        lines.extend(["", "## Competitive Context", f"- Competitor: {strategy['competitor']}"])
        lines.extend(f"- {item}" for item in strategy["differentiators"])
        return "\n".join(lines)

    def _competitive_strategy(self, license_id) -> str:
        lic, error = _exact_license(license_id)
        if error:
            return f"**Error:** {error}"
        strategy = RENEWAL_STRATEGIES[license_id]
        lines = [
            f"# Competitive Counter-Strategy — {lic['customer']}",
            "",
            f"**License ID:** {license_id}",
            f"**Competing Offer:** {strategy['competitor']} at a {strategy['competitor_discount']} discount",
            f"**True Switching Cost:** ${strategy['switching_cost']:,}",
            f"**Value Defense:** {strategy['roi']}",
            "",
            "## Differentiated Value",
        ]
        lines.extend(f"- {item}" for item in strategy["differentiators"])
        lines.extend(["", "## Counter-Strategy", f"- Lead with quantified switching cost of ${strategy['switching_cost']:,}."])
        lines.extend(f"- {lever}" for lever in strategy["negotiation_levers"])
        return "\n".join(lines)

    def _renewal_proposal(self, license_id) -> str:
        lic, error = _exact_license(license_id)
        if error:
            return f"**Error:** {error}"
        strategy = RENEWAL_STRATEGIES[license_id]
        return "\n".join([
            f"# Renewal and Expansion Proposal — {lic['customer']}",
            "",
            f"**License ID:** {license_id}",
            f"**Structured Offer:** {strategy['package']}",
            f"**Term:** {strategy['term']}",
            f"**Annual Contract Value:** ${strategy['annual_value']:,}",
            f"**Pre-Approved Concession:** {strategy['concession']}",
            f"**ROI Positioning:** {strategy['roi']}",
            f"**Dynamics Proposal Receipt:** sim-d365-proposal-{license_id.lower()}",
        ])

    def _activate_renewal_package(self, license_id) -> str:
        lic, error = _exact_license(license_id)
        if error:
            return f"**Error:** {error}"
        strategy = RENEWAL_STRATEGIES[license_id]
        lines = [
            f"# Customer-Ready Renewal Package — {lic['customer']}",
            "",
            f"**License ID:** {license_id}",
            f"**Presentation:** renewal-expansion-{license_id.lower()}.pptx",
            f"**Narrative:** Protect current value, quantify ${strategy['switching_cost']:,} in switching cost, and expand through {strategy['package'].lower()}.",
            "",
            "## Meeting Talking Points",
            f"- Account health is {lic['health_score']}/100 with {lic['seats_used']} of {lic['seats']} seats active.",
            f"- The offer delivers {strategy['roi']}.",
            f"- Counter {strategy['competitor']}'s {strategy['competitor_discount']} discount with differentiated value and price protection.",
            "",
            "## Negotiation Levers",
        ]
        lines.extend(f"- {lever}" for lever in strategy["negotiation_levers"])
        lines.extend(["", "## Pre-Staged Approvals"])
        lines.extend(f"- {approval}: ready for review" for approval in strategy["approvals"])
        lines.extend([
            "",
            f"**Approval Receipt:** sim-approval-{license_id.lower()}",
            f"**Microsoft Teams Package Receipt:** sim-teams-renewal-{license_id.lower()}",
            "**External Writes:** simulated; no live Dynamics 365, approval, or Teams mutation performed.",
        ])
        return "\n".join(lines)


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    agent = LicenseRenewalExpansionAgent()
    print("=" * 60)
    print("EMBEDDED DEMO PIPELINE (works offline)")
    print(agent.perform(operation="renewal_pipeline", license_id="LIC-3001"))
    print("\n" + "=" * 60)
    print("LIVE TENANT RENEWAL SIGNALS (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="renewal_pipeline"))
    for op in ["expansion_opportunities", "churn_risk", "revenue_impact"]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/62757Lr2JUm+CqM2z9KKmYmvMuJmhl4gIQjDEGgsyMFDxDeA1Tr3Rs859xMqUoq1VTMiRs3CHLvtZf91rcYm3/+FsxT3g7ffv5Gywxt2d9++BYnYzQU3VS0zfG2GjRBloynIWmSNahOXdElVdEc7wRNfIryeWhOQzGWp3Ro61NwqoolOY1FPVfBlMQnbm+CuojGE4Jjpylpgmb6l/EUBeOXgH5up2T84bQWU368cWrT9C39FCd1e0qDqgqDqPzp0CrZgrqrkvHbz//zf/3wrThef/v5z9+iKhiPt74pRZQ0Y2J+KslvXdCMh/50ljTTsbkKmuxY1e2Hrc3x3CVD2g718VacpKevpz+MSZX+cPrXfy3XYMjGP55+/L9P4zT8/Etz+vpru9O/nT4//SlLpj/88q099gZvT/3y7YfTL9++nPTrdyf98u2Pv+8u0g8B//Z31/3VKe+/IZnejn1r9NOv/371H/5GherT9F+L+Djtr447lv5+YPLdI7+2XdcO09wUU5GM//m5/2DTH/7RIR/J8Os7Gf5zub+v+4eihmRJmvkwqu6CaPpn7vnrtf9QZBBF7dxMv+ZJUE35r0daV/tY/BMX/INN/40IRG3dJdPhwCX59ciqoziy/Z+46e/s+G8c/Fv2DG3XjkH1X8y1r9X/jQOPIBTLoe3vso4SPjDkn3n67+/6rynwJSr95du//is/DO3w87/+68lpyqZdD0z5XqSnP/257f7yp59++fbtLweGNIdX5+j9wRtC/sf/OKlFNLRjm04n6wj7dBqO0Bd18kvzS2PnxXg6/k15cnon3DAWYZV8rTuc9Uw+BB34dfrT/xsUYTBOPwZv9Bl/rIpwCIYd+K77dwN/K68//XSyD7HtUGTFkWAnkzaMX5qP3e8juyEZk2E5wDTcp+THA6p+fL84FYc9/1Dmrx/bf+r2P33A7LH2rbnJygf2duNcJT+9rXLzpPmyITrAN9mSaD4kV210qJEW1RuZj9Pb6sD06e2BsSyq6hQXw2FuO+wfsg8v/fwW9qc//ekwO/+l+YRZ5PTZRkbgWPCbOqcffzzsOTA+y6dfmiTK29O//Pkv/3L636f/bNeH8PcZxgH3XzE4NLxYunY6smOu344+vQOaBPFHDP78ly+vHmKaZDgdESvSA7w+Nh8gWibxdxdbEv0jjOGnMDlce7i1fmNd0WSnYvrpJKen3/Q9Dn1/dDSuU96O09GjuqSJkybaD6nBYc5vnmza6TQeKTem+w+neUw+Tv3TkQYfKtYHAgbTn04qa5ymtq2O/95qfiw6NrdNcbj/twT4fP8QMhyNk/ku4qeT9s7CUxcMQZcPwdcZafAZl3Y4fd9+CA9OR3b80rybZvJ21UcxfLrnWHR4JvoK6Y/vmJ8O4KmPwI7fz/5Y89HN7fbI62T45Ui5z3QPhncoovZQZT9lcxEHTZT8X18pNebtXMUf/js0fUv6ikL8FZWPHPxq3aev3v2RUr818NNHBz/9MsMghB52HJZ3b2Jx2tv54/A6ORjF24H1fJj1mdXfKYsVBNbpq0L+I3/54VQcsZs+s+K3ujn9Tav74YjCeFCVN1v5ner88KHjV9GPp6/+c/rsP6fgjSGfeRbN49TWb3+9ZaZtVbQfCkq6e7Il2TrZvGootM2fXN28Wm84g3466YfrjhR+Cwjb7cjCUzdX1fjJrL6bMRbZARXj6e35z2KQbNv4JGHHzi9kzKo2PDjU/pGvh9utd+ijv0fKTn+g35E9KcFBvvQ0Pbz2JcPa3/k2fo/BuDeH/LeUOJiCH05Ne4qG5MOThz4HkWuHcvwig82+5smQ/PE77ufT1I0/A0DZxvuP60/Zwfnm8KeiBcYPvX6Mv/T68dALCLoCeB8BLNRPMPAlwR72n3/ja7/h+r/9Z8zrS+8Pgtkk01u/09z98OHf76tP4zwcpfMFD7/R1L/2+Je0T+Y6ztHBVscTS1s/wjgIIejR95R/l2kf1PZ46ufkw/mf+PIl50i44jtzPP3Bmuv6iLN9VHd1so4GdPS85I+noGqbbDzS9Au1Dm0Om5tPyV+CwrYtD5hqPvH5t/oI/l2mvBtJ8Hvg32Z8ZHHwJea38vjq+/9u/ceJP73XwgfytN8d+f+c+HflH0cfcPlm6+Ppzdff9fjWOKnDJI4P0z/YfBXsR4KFSdWuX4f+QZFZXrP4X2nR5HmV12zrBJz4h0FrlqxrvxqmzMqa+MfvMXzL/IS15gP8ogP38oPFfkr7Gh0+tER+OqlBmbyL50CK4bBl+tityHf+xNE2fbJ4Wv1U5ueDgUxfMr4rZPIa79LKr7/r8t70q2Mqb9uOxD7p3JGbP4550B32HW2gaw+o/W7X+8zPqvzNg+2Q/fCG5Y+edUT/AIRj40edfKxmjRsQHs318OSXlPGj8P74sevoPNWRn6df02SK8oMaVtUnAv/hj5+Z/SHjTXbGOfxtfPsSRBvyJ9gfUFfF3/vn+BvKfIB+kyTHR29IrYqPdC2+b/+1OYotqIpX8us7BX/jGp+J9YffokOb5g+HK4Np/ATIT8589PMj67/H6Cj0/SiVBgi+70qao/3k76703lsf1fAmXdUHwK9HU/q07MszAGt9wM4HiuoGb9L2EZsP4Pz3AHAwin8wvxyf/D6BnP735+a/HiGOBf+A97+3/h1W/l3I31LnDzH/gAofyz957c9/xU7/8MaKw+T4iPnvRPc9vn4+fPu5ORrBD9+OjEr++cz7ZgZ1cmD6+B6U30olw9v899NfST+e/nbg1z9eHOp/75wy9875I0mmj1ZzkMdpfE/k09691TiccETmTah/s+Q/CrU/8OtTXv3Rnj8i/rvtxwlfsP4x7DfzMZz/z/+A6h/fA/zdoB6f/B7U4+FvI3q88Q8i+t73dyL6IeFvw/kh4++H89v/+g/e+MtbwGc034b87prfl7bhmz+8HfeG7M/vI/787QhZ8E7xr6B9zRXH8mOG+HF88yoA+gl86xcMn/z4+Oz/68Txtf1Ar4P4HvsRioxIjEgpkAoSHEdjMggiGEdgAsGCEENTCoFTIkADFE7SmEooCMSwBIzImEwjGEIOeeNRplHyHlqPTnaIDNMQg6MQSkGCTCgCTTAIxJOYgvAQS+OEInEqRCgs+X1rWTTxl52fdr2d+Nvw8/bHl7l//hbi6LFSQkeZ/vxjgUN14qE8tU4BAPPWXhrdlfjaXWCPtOsSEavZJwNCiou1mW04tXpB2PUgkJ8OH3hAEcUOtS4wmpACVc7TTLM2eona1wjNdwt/iHxWgmKLnM1M3xVxmbYLtD4QBj7+O3vSolI5CJ+5AkkTXjTmJY04qgCAYgFgHi6AfCSm0vTRMfObUIa9V0hy8hVmdx2VqiZMYIqIR+ShsHl4O/vdzkrsokTNwzCosGrVOGJGnXDywCNFa/ZeqLoWDYhkczJp91F+LufX7oLRudjA7Q4r42WW1hjALoxMny8EobrpHIqYIde+sZa0LEzQrrWVIKgbOsverUOlhmm5aCa0FE5cAt1FQlJWwDhXKXdkvL/FgBSg2zTdcx+R+KyooCVDz+ozLkjq+WL4V2F0MBOJFCluqEi9dj4HuBJJHpXuz+J62wi6sFGC9JShRgyX4MIbb0eeo2dPe8rNdUmbobTXh58QGd+llhm3KzndGr84Y3tsBzGtrFUxy1yjggIorGN6Y1V+Q4lRWFROy0oMvFG3IBQlWVltPnuEj9crIjsa4XbLg/ciKFBDe4UL7Ya3VH/Gc8xMRyJvmbMx19BJcogOHG2GsRktn6GGA0S9LVbGPtDkSr8eJcpFF19GaQNkkTXBgmKDiqXXXIcwpZTZCuFsb+wiZGS4CZfYUWu0YXqbyKOLUwuUtZuXwLo8rXFBx3IaV4cgaCCE9zPhvmbixQ2XKHYlXX6uRwZ6PFEvussOOF2QmNNHSux526D6ij5VgTIm4hraOC2gs1qNCsAsDEeXrWN5K79R7D1h5xvOzitKUL0oXCF5GyWNXBO2agL0ZbcSCvn+jX/ycoaUGTtC3UKjIJLgKwgyNqlSI63scCZLlPgKoNLSFyIqYzaHix1OH4gkZFCGp0y0vwSS0SBqVaTZuj1947mSUhdx3LwQoMdpqGEXZym8qBqwwGT6aknjOcYNREbShqdLjVhrwZM1accY+UxLinYnaJMtVQCLeZbOOgTC0kI8e13OWFn2TNmkbBAD6gf9XPpHansRpVGKRuMeehH5VhAx8bLq6QynT0EdRxVAMXS0G8ZaVW4k6Kc/FtBEcLnxXJ6q8TiUDxJWdhbZWrNHbt+Ws/cg/aZDiqI1+NuLtFixoxKDsLHhMdBpi/BtluFuZ3UYx7kliooghWlKGdurYtCUw3Ka1lolWvOqyHHEhipWkOtk8uBLAgCUJ6fUUt2qEWkSF5Dl95aKng5lP2/lqA7QJUgs4NX1E/aUUPtKTa/0bBZ+2G+VtVysG45dgPO1YCwLlHfhjuyIKl1oi4eZbbLlbF+n+uyPcJwwZ5zHZp8orqAI1aP5BHM+Cs4kr83+rrdjWKM+A7L9UxwBgzFT0hIyHfLuOA4H8ZFF5MvKh6SU5KRFLnWDZ0ufWJsz1kfNVQY9MrnC8WmGIKswXqtmFEauaad1rBVWtRxkX53DO2chPwj2CGemI1eZhEovup8IkFVD8sZY1M0OcHrP1BIfVfvKtFDskyDrEZGY0BK+0wru7ZyLClMTlgkimUmQV+KTxfe8WdY4uZ7z5ZXPLPeSyjMATxELPFPeq5CWDMcrfe/j5yWl+rsljn6ja7qhBMKMlYp6V+WUFiVMjCHrST1urNJH1MaKE4TcJdy+XRnzZrCvsBBb5cwN7R1IV4pchgDWcsIItXN869OtNh6ejIjKxQqQVPRDhlyvRHpkspePYePi93I+b0CTwxs1ChCr+bRhMrnJ6tA2Bo3S+84TvS1HGThCSkem679mAScy9qrwXgDk2HA2UvKJSWDHN06bUpOsmSRbyYZwMW5mxffRWdDRaRP9dZeJda4UgaGvFg8GRYFr8/neTNYSKLiZPEIwfPrR4xbmcu4CQK6lSNE1YAo/Pba5Y14hEFf2lmeAWJpPoedHEeNKlI9zmJSDq0vbgnxUh06vt6qexkRnVT8qjrLK2Lk2DdLKnEARRNmySVr2a1wclebGXcyueBnQAY2iUzLVKD2zO48x/W0BJUymtAwCzdZKsx4GPAMgkAU4o8BqnHVHE+wp4Aw/dSV/laq89QNrcJdWSExk6zfogPnrQOk2lqAjzZTyFaiIHO/lnPG9FKFpkGzaVbuos8jR4A0ZBnMGioPqqY6mSiQjM2x0SYLrgw6MayroHL1y6zmjIRWObg6HaKoug5chgxBNbx06FF0lMPNYW4QIvZA6mNMrIzhGntWggeRRdiPLivF2a4YP1lPHWfIi0Xu1PW8ZYBgLdvQAmqtog7hhcpePYjonormCXWM4Q0c+CPIFnTPtaJu41j5pgMjPpBhw18TRWuNm1/Dq7JyCGNIBVckkPDOShMbIYKZXElrwkTwdUbyqnqMgUkplncbFTGnzvjQ4C+r0qvLvcclDibEGtybszHMF3JaiN2Ird5hDFkU+9byQCKScUE3hxNiDW/ec5YFQ8ia4Mp3QyuCREq4Yz08wXM2SzQSOUw5wyrqKF4YRl2yPruc5v2hgIdkXziFJ+hn7TDvGMYfequcIMUhM+R1zZDnoXAs6wYZ5mLRErkvnVufNZKyMOeIYi4HKObSsKWAJ10OJrnl6qUPlhpTeKIFLO4BkoIhkR2rDpwYUmCm4Y68mu4UJ0pbsslWSv1w6StaS25pfSS/oxYP+4vF5mng/u3CaDcgoI4vceq2LKocXlYFN2ghp3g5pD8ki4TZw1qx3M0SRSiXn/UbAu04kT9fCDdbgX7ix6hJtvJguQ1Hr3DlldHtg7U2E3ZfqFgM6ANU+TwFT7d3QqJ1gskwbKlOePw02VGkWPWfY2q4DurMX2QJd5wLR21wAclZjUyG1pCJj9YCDQdMrzHqzrj0hj5kQyOET71Pa5Z+0IUjUtVjNcRUG1Vt72cde/R1TnrcCyliUfloKrXCPihKRS+7x9esIAw1TO0NRz3srAUrLFUDikLYOkVVa7vxjlzyZozuLAflm6134wUArKimbw16lYOaTEneRi8xnDs25eeVaA63iJIpJabblcZZFFfd6sKs13ZyR6XBnDM9NVK6VZCAHa23Z/EUC5+YGuCB3IbLF59IxK2i5fcCwGjHbObblGMNpL39/g/JEd/BCQzdFQrMGv7x6AWFfnQTu9gyE0v1sXgNtvRiYGdXX2OnG8OpaoS5ftuLmVp5RBABB8unooYC081Zc+JUssJek6ixoPT8Uh77xvg54LG8iwwuFQMthmtVgWnfc9P7Cqa2vXFwecXFCnFkb4DUnqEOzsYE9NKK9HapsPk/u7DsZ/AToK0kPFpihfXs1kxvVj6FUX853GvZAZ2LKoGXFS5y/dIdviBturc+mqFk1C3zrsTUEDSttBg1O5GaSaT4CG6418cxtXQgSVumAgwHQXTrP8Atp4ydPvo72XqegiQKMSOd62QUSB4NoZPv9aB+4DGUpqHb90VlXiFXVLFSOIN63c8iEYwDFxliadgEGfQeSa8HZpKTyyaqfJXMvzFYKb/Q9oapoORthebvWSR17hC4VkcjUquZx5k6v3WwHl2cu3jPl6GxSqQdC5/D1c10Sncll3GkSZocX+BmB9nuwQYdli8kRDl2E7QfwvgiD6OBr/9wh381dPvZR2tf0mblmTLfsV0pzQHcQchObBiBJV2YiDUJD9byNVEtnZsCA+QYIUVWBJtpcVgL2TWyu2TDPsFLLeeNJdY7pFtMFKnxMRJ4PZK7gCWRkCZy05+MxnweUyo45jyqdCH5iHhKpWSPM9Zwyo9XLairn7Gpb2QuDHj61EGcKnvvEBR/TEFxfa5yddQZrLkNMTWh3L48+F0vwGZsXeEPiVaCilz3p6MasXmAGQ/wImUiBeNoUm2pkeJlJqpmmn054fugmrgoPeKsVa26uY2g/vWXHC4iBn6bf+ZW6ibUDnOdUevJ+jZyReXFpgLHPeSKAZb2+ONSsLuANr/I7Ik1Hd2vkl8reLwVE0/h1yl44+YTDW4afOfCBNeZeNxDwODflvfUe00Ey0Zh7xkuh7BvlSYA+qdJkbll6ZBGaE6108XbWxVDzAZ9ddRQMjQFmKDygBZm6ML8hO/G4jLSMni29tJTp6Q+Jy3JKUIUKA+oW790WbFX1eh8BkD27x9jpAEXBXfWjQzxWhtQbakYlT1g4yD2LG/Zi+SaT7Mw9X3FeTVG2aaHMRyJY1UrrNeXnR9T6OuVGUSTG+U7TTBZYCT3BCb1cCaXsvXmCGDcd74gi9lQCNbQEhDjCimkF6xFOQ1OUDPBVqZDDDkPs788yOiMHJsXNg79mu4uO3rjBDZcSZTT4GP+asokVAzTdEIRXEDAe7CXnCDyCBSquAnS+w1cLGO+LwZIixnQzFst64Nk3z2hCUMuAp6/VRuOHSSSHwRBGIUws6FWrVcgPReIhNA6MvqhkCL2hdhUVYDJQkVK49lYxpa8X4hZfDoBDXwNM1LnErZcpBmU0c/vsfuPdwig0eLzhxmsip2flO+5MIgVSVQrU202pAO0tbB2dwePJu/Sknp3TsFKQmC2DbioaaBiPWrMfUn92g5YKakIk7jBmTQqhdhjOEyOpCsHlegzgFQMvaRlKieFYtDIYSiI4tIdNZeFN8zHO2E2P7vHi3UxZQ4eKdkukiFrtmRSXA2eFxwyq11sqb9rLLTwZKjY6WXYGzIXwEUFx8WgjerODTZrB+Jh6vDZlLxWQzk4KQLbg4Pu2ehU3sDGLsaDxqs3FUDMWocqRacajdkXDiMRJ7TpsRvwpHPRjprk0zavavQr1FlnYNEOZhLh9TgdJucnnQxcnc/R+Giktzjpn1zi7MTLWo9zMjNsccaghqu4gKkWRoRQAUaE6srUctlrSarZNxBOS3TKhaAuWEfvzfjSrcAvuEwKgD9/K6O4AoJgexGGl/VB/HROLJDbOhlmLqdBls8+N2AUlM8pSr4WYDmGitr0abBs8QuGpAXipIv26k2S6WJjK1Cb62NTKwxFPMbziGKLoHHtqi5nZFcxgz+ie1/5DKeiFlsUmSG4NyaxChvWP6fyS5Axc55XqJgy6hcFVvNzlm+wtpHDbbNpIGHG7T+wdMiTGwrtBJRITDQjcY3a9BtTEuUSS1pc9U1iGrDsvmGQ7Tu2l23lIWAvDiAR2BEERpWIFL3ypwRhNT/yzflxv4o5f2G0yeOk84jJDy6XWHpNQ3oW2Lk69xxhNJSkLwLKt0rVgagOZ5sqcafWCkueTQacmUYvqHFyrbDsjE5bs6AQBxjPdn9f9Wvp4t4yG3+OZY9xqQjNBZj048DTRI62mdkJETzHGCi7WnjnJwRU+CG6B8d0gMir4WuvrIz5Kk+YvBt9J2qrluXPMZdWq1p2v5gDt29Uxc8f9bdx9GxGGZAAONiaWOTsj+jJe7liPpbOtVPz08KPlgdiBNz3sWt0i9HqTzf0hFmzvs8oz24g28jK8vaF5EuB9OyaZqZ9Xy1cMEfXUC7clIb3g+j3rS3WAFFKjbwTfw4XuTl6cUncjmM/HMH730+kgSSsXeLj5UFrLEZgSwtDMr0r4lUW9qyuZp8Oqy4sa1mRQiHNKIpnEhGHSRMSJUhuWIN4RbUlkCN6h6DVsXhsRnd+9zrjaA0RpPFjzcm8oPbQG9sq7VHbM3TnI+Lxw9VFtSP1biccETLsXjdwXD+rjyXkhZ5fL4UlQqQo2+InJq4aEHiA2+cnTrID5AMlnQKULxm4cXfQYgM3BPu9TjLjoDVDuz/k+c5ecZtYYVXD0STWE8Mi2i/WqUUPZqto20bJIA+pAb3CBrrR/kCQr26nB5ieMHB65DbvCLexeB6WtUS0xp8XRbQ4Mr7Ot5rH7NLBsHQA1f4S1VNaUjLXQpnV7YVChOgE2t3plg2UPkju3llQYcdtZ9GslsMWb4leamdDkDTGxEw1CwZNP5VQcXGg4jYTIHTKbgkNRU0n9fs5eKRiifL0nRBEW8SN/vVJEI4QgFB6BO4pZTz2xJXATjJyjMkJ84C4/AUKxduksknv1hJONrwJFVa27Llx0C+M3yveNM8UD3k0aJOP2BDctTRhcnqwUNdWt6LVrb1ZPceDsDtkHGpcbKIG13TmTR/2nMTrTwiCbbAl7d5/gJhGKOgcr9jYaiPIlc0HjORtIoqBx3Ybx4QiXSovJmmbPCbgBqQLCQHTdEvXZlTOqY9X+TC7ZHW4Axxndkn/imLd41MOfnclKYO8BPeS436KpgSRxMxUtDwvmWTxEww2KQRDgeZzqO59O9pNAenXG8sIDhdtNqa9dACJ3bVKcTXH1au5L3wsx/uy349QLuABy0St+miLZIA64lEjSoqlJldaAbPUz7qqmENWH0bc+e8F6nq6Va5C10Nhr+93MUEpE8bj2axDf5VrTCaJN0nCEB8nfVgNWvbNBMLLg0t4RSZkiH0+3vi4dGAx6ZJeQozXJcy7GtWypSJEyxYGKXHVSbFJaupAH/aZBpWTze3PWhNemG7O6d7rBiWctdBrGjGKTjTaSFARAnPGmn9nu4iQhjHPiA1/azaZKE6BveJL5cizo3l3Vo5Z3iPOZtp4xv3RSj4lc8TCfljXvOrzHl4aUXC50pXOwT/Zy4dizqREHZbpfzjShMs5qsgKR3B+q2+Lz63qM40P6eEWMcgHiWFnFZHAXurCCIuBdRY8bbK3YFdJaMnjlBh6aK5xavvoAhOrGWB0tSnkKOVkA9mf26d5rs3bAIH2Inrtf1dZZmbuWgBFzhPm1DUt/p8ksb7zK8jEb2zy1aufcH3VmnM8jtrkU0DreExSiXvUYmQUusbqjmLiMnleJyaNRYPVS6s4wP0zHo4J2UIhbeDCLg4rBkYdQ1ug0rZn1vgH63i5G+mt/Ljt01GgJgoyCXamsqUscC602lCja2G/IgX77uFO19pQChMty1Hs+VStgTbboRJkHLZnVcgr2C1O72Infd6ShPTTm5Q/BiLeAcA9pSUMvwMAESIZqrNtK+IPIiFq2nBdU1WaG3eQhfbkyye/S5mb+o4RM5FXW4zp3rFnutwOpA6dyognTn8tLMsYeAu9YTF7AJAo7/WzHoGStt/oG4x2/B0CoBup1vVbDXKXN3k+d3aECblFrHRStwSzBnpXCogoOYo+x1eCoysC4I7nrqDjEDgRtdmQ/aGmuZ1Tnu8Nn8BL5XF1ZCkIuBQlBsCsOJC/f7kO8dDXTVdcn3d8OUlRfEIuZJzgexPY+YCoYRQ+dhK99U9qjpphYr7mVG+pPAfH4Zxxh9M2gL48b66RmgyL61a2zW9oJciEMww21+t6EXhV5IB1nkA1RdSrHj+g9w6di1J9uKF3qijeX7uZeX7HSkFyGXbHOjJdQvGFg3waXmi7lo6XeEiCJ1xtyGQMhE4H4IPqcaOR+mPuwhb6kqTpwzJaitouaG6XTeuR4D79BuFeRHl27gpIseo28dxFUywZd4Krw/DqUtLe5481JirOYj9NdYI1hvCn98KDaUsUKea13dqJoC2Kv4ktI7op9QOJ2vUxdgAwQe49jyAKDbajvjzYOwCHMitYM0vLcMvimyAhLWc97Q0zr5XJu94dSB8swX23C7E3yNeeRjt99EB3VtmTSZbp2oiF2gCLe/dE9C8VSR9w53BEaOV5sfCATcQjLw+iZo5lcfJiJyaM/3o8hCcGW670lWHM8N3d14SN0b/S2KW4VYlmEcwW3vq0oQXrd7Qq/TwspwUrovuRgD2ljQS8vCI1EltevnIQ5HaRZOTONUa9E/e2YqCHi4kG7uRF3/Zbzk55da0cNexiNelmA9ztzbweq3HRXvz9Q+gaWY3Zv1nW5ZFHelVdH3F+12s1sex9Xczb9uAGHybEs8GnzDeGvmA9K4hBdtP5M7vl1ejydoXcpqMoD+t4ENTSCsjhnKKh1S+Q4/QODYXVNgX7ykHapTU0pElPe775Z6ZKDqkJEWPd4w7kbJgfT/ZXxVAfjSnuDsEJMyZxD2ExPoxG51BZA2sSjr0xkL2dyVOEHCzwkCz23nOmAqSp2FodKpIR2En8WqIxUKucRemqC6X35QiB6Gfsrjzv7VrzgjJi8BtEbK8TvtMgXVU12/f0xouEYYheiYS697DXd/FSRq1NCECP0z7pRjJi6joC/m4aBl8HBUiWoLBabYpzgFe7YaBPAVuDugz+v94Vmr2dg9ua0bZdjSJ+pZVB5QtvgOnixYfJgZFKXocdYwhaNMINIWXAxWuMabNdUaEacIC7EkaYRny4PAy9uSMW7NhpfcZ2bNU6fzwrnpQt6B1bckNJiXVAKg8lS72w6DFT3hVdytDdlCXQHebgDZ1miAa+twWvDXYdoups7Il4FTfY34Mk+vIsb3rQ74p+lOQOxZJWvqbPwNTEJ2uCS6RY7+CKUqRRayWBsEOsUVjKymBFxKisVZwezGo9T9t7QciahOnacFZ0NXo+NpNS0kn3Sti7nIdNtfL0WUjeeTVE7ywpNsJ5yS3Ju07jrmhKogj6A7mHnMuAPzyZuz3Hv3p3lxnKrQIdEkaB8Kuu9vfY8WD/ccRfOzkDvt0luJreUzeaBuJ3XMCMwcxK4wtpw2+iHW7V99Cg8RNBpE9XWpI6srcM3EYyQszWm0NECYLnVro0WaHqwI7DRpxC28MLcTdRy5Tuex2oEIYJLj8WRoQ7W+Ioprg95stq3S7d0zymq/NE7q+Nsn62hxZ17MLTD40W8cTv3AnzS7CtCKUUUU1F6KZYof7jBxKn4LFbC+rQgZxauqyhEadUKBawMOU9nL2dYAH1z0CAip34EAPNe3456A83g7mN+UMZEzyRKGyeW2D3HKJ2vJIBUDOULkanOKMm4+sW4Pp0X3i+me08I3L1h9yHRwfEhXtILdoz67oOQfe9xBZvEjbvB66kzJBF0MQXRAqtka+1N7eh5wJe7DdxEBvE73oJmkml1/X67G5l+CbCjMSnUXVcrhwcl2yomKMon9wpnfeJjM1BOxnR1vPAquIG4b8yFtSh9va76FfD4Hsc13bimY/7A+5fYV1XfP8Zr6zXTFWPCxhqEMT3f4z2Seh+l6mNOUiEZT6kX4NY3X8xLAOb1OVTJTFMvsyuHTFeK90kFw5mGOUViZYibHUEbM1Xus/DSPR+5/2yTi0fnTQ8HCsoPsHM1HQhlofuAR7XGMbd1tXosR6vnwYRCgauBy0XrMpsg6RYExDo/c8BNSi5Q9ESh7a5DOYalbOcLAdr6kGpfPA7iScVk2JAeyQkr2G5PHQiHNdDUcnwENaQv8w64B9DF0xdB1fvLtX54hTZM1bZalDZU4QW3pPnpLIBdJePr/e2Xtfd98qDFUZq7PRbCJjrboM3eQdEaJsGDV2wrr0dbdF73WEbjKfTPYn/xDFa86E4cMToHpntDnB/X1y2Vnw3TYPq+miWCvDaaZnDnFl+Q0t+KxOH4Njdtgr7KwyXIBORg7JKbaBBU59eb4zA3Gs/1I4P0nopI1KY0An8VTzHc92gUBlvBFtWCyhflR+xr2SAPoZVe0LdUYXRcC++710jGnVyW9cjl5OmK08SZgnUNg12/WkikpftD5UkTZgX4LIUF1y/OK66Ui2PytOyRz3SQnAqG7/7lmGyWSFLgvWyg7ik2XTo/ySl9REynOY1yxYaBz6wJ98YbQ7R8S0hh6kosjIoL47G4duUDpKc86MrcmMtNzWRzPYbogBF4fXztVaHEYna2W5BKfaGGY/FhAhumeeeOPaAkEzEzG7p45u1uOgDiDlu1oPAqRxVGoqKoo8Wgz2QlDu7Z7O8w2q9uASd6fGfT9YzcQBmcYZQ/9Hpc0KW0Y5uddkhRyrmI2MfjsZjX8O5TR/sLnmQnnUe3usHHHCDq4kZY14BEBfgqbrGFx4xaj0izWzqsUuJ95x5nQ0hIR5Wp4MKB6hVwqumBVOdcUfV5UuajrSFaAkgo57P2SpaDhF33p3l0JaAu8kziyC7wt42B7FdWzivrqx2ejk+b8RcuwYcMSh3kOMWhGnO/yQ6Irw2rm2pCCI/ZvhvnLnGYLuSuZhbiC6p2Ph7UZzkB1WcJa/cevd7jjhyDSa+bo4jdonhA2BOvUX4krcausnE7p244XtfJbjmOWRGbE6Y7z+jkZOiL488V9FgTL/Atlon3wOAD67kPGUita1XRLxAXFLqP16aRwIEvivCyYByOX/rqLsctVBh8Gkn1gAKbTLVPbg0RTinH0b8TNM9UGnyOlxJgR/hKlPiFbtRbQ6850NEKv/mmcMEdnPNR4nJXOlRdZQAVrol7e7UqInVs690i0VuvW5VOEma2WUA2tOAWdQXhlyBqECksy3g1RgsCKnXL2QfSVuyc2P05f9QJdtW0zeWc+/mocotsLnAsNH7MQFIUpY+LpxwT2TVOGwPykQFIK6C4Z8Zu1aV6vlRRD/Yu2Wn47hg+0Ry5FhCLJKZcs9tZIBFQQ100zLaIOehItr8YGYXNIND0Gm/YI34RNstKKykXujW+AVmLq7fQUvm+zkTikjjWbnVMr0qx7pYNGhHBaySUJQxrNPSZVALPe3vD92Z4CPe7ACBnra6Vgcoe7QC6uG/ZDRAAOYDoZOmk8S4rGmUiXpFo97kN4rP9wl1amQRju4ooCGbP/kFB/Fo5R8PHs2kI5Eec9B4kTmJOpFbRpCR8Y+W7iM0W6kDbQxVQIEgsQjsHjwk5G4fD8E4X2PBhj7I3peSVdrZKYUWtTBWn3LNraOOenKib0fMH2cIze6xXV5SjVmxZNRK1HaKdS+iODXG9V3fiOjeFWOxyg4k2RUvVqwRW7HVehct1uQH2DapFjt5ddsaqC1la/Ezt061b0SfKwBLlq8P1KAQaaOsCj7i5vXTy3UjI0VPO/Rr6F/EV4EIKRT2yPdkleT5GvYcHNNyQ0UXzmr+qewL7lmHqXL3zCjUFCr7SNXR1Vqn0NgAMsilqBPaJ0TCRevtVvzaD2lBdf7lZTwSxHFETFrDvCVERLfF8tnahMNwl7a8bkEcpH3H3YEV1YKP8QuigOEpfmwuFyq6tArGjANpLo3Wb6J0Lpma8IfDYTVg1IDawvNBUYvaU6zIuLYcx6faEADV5WWTyhQ+A2g1d4T2Xe73XEU/vcoEU3S03KaeoUMMG5rrSWmZMjBc8SeTu03D/jJyrm5tXQGhigkRSHYDYF+Neo2V8dEl/VIupUr2ptGYYW3wlK1dvxaIUQpZB3HH8qHchbeoa5BoOmbWssPAG32/3Y9R5AfQxaqsxjiU3mv72w7f3Vfuv69v//Kd776ux/7/d0P28TNsu79+2RMnn5eog/vnjrJ//C7r8rx++DVFxaPJ5+3is5uz7Zd2/d/f4xy+RP36J/PGv7x5//rLh16htpmSbvl9rn4Ls/evu3267/3YF+69vfX+/5/37Fe+3vCAY3wp+/Czz47I09BN8qPmX/wM/CSP93z4AAA== -->
