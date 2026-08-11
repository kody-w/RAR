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
