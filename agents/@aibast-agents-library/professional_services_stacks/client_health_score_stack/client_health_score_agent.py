"""
Client Health Score Agent — a template you are meant to mutate.

Monitors professional-services client portfolios using engagement metrics,
NPS scores, project margins, utilization rates, and escalation history.
Surfaces at-risk accounts and generates retention action plans.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     In this template the tenant's accounts are read as the client
     portfolio, its open cases as escalation signals, and its open
     opportunities as pipeline — e.g. Harbor Pine Consulting.
     Try: perform(operation="health_dashboard")
  2. No network? Everything falls back to the embedded demo layer below
     (CLIENTS / EVIDENCE_CAPABILITIES) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CLIENT_HEALTH_SCORE_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your PSA), or replace
     _fetch_collection() with a Salesforce/OpenAir client. Fields the
     rest of the file needs are listed in _normalize_live_client() —
     NPS, margin, and utilization render as "n/a — enrichment seam"
     until you wire your survey tool and PSA.

OPERATIONS
  health_dashboard | engagement_analysis | satisfaction_trend
  | at_risk_clients | retention_roadmap | stakeholder_outreach
  kwargs: operation (required), record_id, client_id
"""

import sys
import os
import json
import urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/client_health_score",
    "version": "1.2.0",
    "display_name": "Client Health Score Agent",
    "description": "Flags at-risk accounts from escalations and pipeline on a live simulated Dynamics 365 tenant, with an offline demo metric fallback.",
    "author": "AIBAST",
    "tags": ["client-health", "NPS", "retention", "professional-services", "churn"],
    "category": "professional_services",
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
#   export CLIENT_HEALTH_SCORE_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM/PSA client. Downstream
# code only needs the fields produced by _normalize_live_client().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "CLIENT_HEALTH_SCORE_DATA_URL",
    "https://kody-w.github.io/static-dynamics-365/api/data/v9.2",
)
_LIVE_CACHE = {}


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


def _normalize_live_client(row, incidents, opportunities):
    """Project a Dynamics account onto the client-health shape this agent
    renders. THIS is the contract your replacement data source must meet —
    a dict with these keys. None means 'not knowable from CRM signals
    alone' and the renderer labels it as an enrichment seam (wire your
    NPS survey tool and PSA for margin/utilization)."""
    name = row.get("name", "Unknown")
    open_cases = sum(
        1 for i in incidents
        if i.get("customeridname") == name and i.get("statecode") == 0
    )
    open_pipeline = sum(
        float(o.get("estimatedvalue") or 0)
        for o in opportunities
        if o.get("parentaccountidname") == name and o.get("statecode") == 0
    )
    return {
        "name": name,
        "open_escalations": open_cases,      # real count from live cases
        "open_pipeline": int(open_pipeline), # real sum from live opportunities
        "owner": row.get("owneridname", ""),
        "nps": None,                # enrichment seam — wire your survey tool
        "project_margin_pct": None, # enrichment seam — wire your PSA
        "utilization_pct": None,    # enrichment seam
        "health_score": None,       # enrichment seam — compute once wired
        "_live": True,
    }


def _live_portfolio():
    """Tenant accounts with escalation and pipeline signals; [] offline."""
    rows = _fetch_collection("accounts")
    if not rows:
        return []
    incidents = _fetch_collection("incidents")
    opportunities = _fetch_collection("opportunities")
    clients = [_normalize_live_client(r, incidents, opportunities) for r in rows]
    return sorted(clients, key=lambda c: c["open_escalations"], reverse=True)


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

CLIENTS = {
    "CL-301": {
        "name": "TechCorp Industries",
        "annual_value": 2400000,
        "nps": -15,
        "project_margin_pct": 18.2,
        "utilization_pct": 64,
        "billing_trend": "declining",
        "escalations_90d": 4,
        "exec_meetings_90d": 0,
        "satisfaction_scores": [8.2, 7.4, 6.1, 5.1],
        "health_score": 42,
        "risk_label": "CRITICAL",
    },
    "CL-302": {
        "name": "Global Finance Corp",
        "annual_value": 1500000,
        "nps": -20,
        "project_margin_pct": 22.5,
        "utilization_pct": 45,
        "billing_trend": "flat",
        "escalations_90d": 2,
        "exec_meetings_90d": 1,
        "satisfaction_scores": [7.8, 7.2, 6.5, 6.0],
        "health_score": 58,
        "risk_label": "AT_RISK",
    },
    "CL-303": {
        "name": "Healthcare Solutions Inc",
        "annual_value": 1200000,
        "nps": 5,
        "project_margin_pct": 26.0,
        "utilization_pct": 72,
        "billing_trend": "flat",
        "escalations_90d": 3,
        "exec_meetings_90d": 1,
        "satisfaction_scores": [8.0, 7.8, 7.0, 6.8],
        "health_score": 61,
        "risk_label": "AT_RISK",
    },
    "CL-304": {
        "name": "Apex Manufacturing",
        "annual_value": 3200000,
        "nps": 45,
        "project_margin_pct": 31.4,
        "utilization_pct": 88,
        "billing_trend": "growing",
        "escalations_90d": 0,
        "exec_meetings_90d": 3,
        "satisfaction_scores": [8.5, 8.8, 9.0, 9.1],
        "health_score": 91,
        "risk_label": "HEALTHY",
    },
    "CL-305": {
        "name": "National Logistics Group",
        "annual_value": 2800000,
        "nps": 38,
        "project_margin_pct": 28.7,
        "utilization_pct": 82,
        "billing_trend": "growing",
        "escalations_90d": 1,
        "exec_meetings_90d": 2,
        "satisfaction_scores": [7.9, 8.2, 8.5, 8.6],
        "health_score": 84,
        "risk_label": "HEALTHY",
    },
    "CL-306": {
        "name": "Silverline Retail",
        "annual_value": 1900000,
        "nps": 22,
        "project_margin_pct": 24.1,
        "utilization_pct": 76,
        "billing_trend": "flat",
        "escalations_90d": 1,
        "exec_meetings_90d": 2,
        "satisfaction_scores": [7.5, 7.6, 7.8, 7.9],
        "health_score": 75,
        "risk_label": "HEALTHY",
    },
    "CL-307": {
        "name": "Pinnacle Energy",
        "annual_value": 3600000,
        "nps": 52,
        "project_margin_pct": 33.0,
        "utilization_pct": 91,
        "billing_trend": "growing",
        "escalations_90d": 0,
        "exec_meetings_90d": 4,
        "satisfaction_scores": [8.8, 9.0, 9.2, 9.3],
        "health_score": 94,
        "risk_label": "HEALTHY",
    },
    "CL-308": {
        "name": "Metro Transit Authority",
        "annual_value": 2100000,
        "nps": 30,
        "project_margin_pct": 27.3,
        "utilization_pct": 79,
        "billing_trend": "growing",
        "escalations_90d": 0,
        "exec_meetings_90d": 2,
        "satisfaction_scores": [7.6, 7.9, 8.1, 8.3],
        "health_score": 81,
        "risk_label": "HEALTHY",
    },
}

EVIDENCE_CAPABILITIES = {
    "retention_roadmap": {
        "title": "30-Day Retention Roadmap",
        "write": False,
        "records": [
            {
                "record_id": "CHS-401",
                "client": "TechCorp Industries",
                "risk_factors": "negative NPS, four escalations, no executive meeting",
                "quick_win": "resolve the two oldest escalations within 72 hours",
                "stakeholder_map": "client COO accountable; delivery VP owner; executive sponsor consulted",
                "stakeholder_touchpoint": "executive sponsor value review on day 7",
                "day_30_outcome": "approved recovery plan and weekly health-score review",
            },
            {
                "record_id": "CHS-402",
                "client": "Global Finance Corp",
                "risk_factors": "negative NPS and 45% utilization",
                "quick_win": "complete a scope-to-value workshop within five days",
                "stakeholder_map": "client CFO accountable; account director owner; adoption lead consulted",
                "stakeholder_touchpoint": "account sponsor checkpoint on day 10",
                "day_30_outcome": "adoption plan with measurable utilization targets",
            },
        ],
    },
    "stakeholder_outreach": {
        "title": "Stakeholder Outreach and Meeting Preparation",
        "write": True,
        "records": [
            {
                "record_id": "CHS-OUT-401",
                "client": "TechCorp Industries",
                "outreach": "executive sponsor email with recovery-plan summary",
                "meeting_material": "health trend, risk drivers, ROI recap, and decision log",
                "schedule": "2026-03-24 10:00",
                "channels": "Outlook and Microsoft Teams",
            },
            {
                "record_id": "CHS-OUT-402",
                "client": "Global Finance Corp",
                "outreach": "account sponsor invitation to scope-to-value workshop",
                "meeting_material": "utilization gap, adoption milestones, and owners",
                "schedule": "2026-03-26 14:00",
                "channels": "Outlook and Microsoft Teams",
            },
        ],
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _portfolio_value():
    """Total annual portfolio value."""
    return sum(c["annual_value"] for c in CLIENTS.values())


def _at_risk_value():
    """Sum of annual value for CRITICAL and AT_RISK clients."""
    return sum(c["annual_value"] for c in CLIENTS.values() if c["risk_label"] in ("CRITICAL", "AT_RISK"))


def _avg_health():
    """Average health score across all clients."""
    scores = [c["health_score"] for c in CLIENTS.values()]
    return round(sum(scores) / len(scores), 1)


def _satisfaction_trend(client):
    """Return trend direction based on last 4 quarterly scores."""
    scores = client["satisfaction_scores"]
    if len(scores) < 2:
        return "insufficient_data"
    if scores[-1] > scores[0] + 0.3:
        return "improving"
    elif scores[-1] < scores[0] - 0.3:
        return "declining"
    return "stable"


def _churn_probability(client):
    """Simplified churn probability from health score."""
    hs = client["health_score"]
    if hs <= 45:
        return 0.78
    elif hs <= 60:
        return 0.45
    elif hs <= 70:
        return 0.20
    elif hs <= 80:
        return 0.10
    return 0.03


def _evidence_matches(user_input, records):
    """Match explicit record IDs without substituting a different client."""
    tokens = {
        "".join(ch for ch in token.upper() if ch.isalnum())
        for token in str(user_input).split()
    }
    return [
        record for record in records
        if "".join(ch for ch in record["record_id"].upper() if ch.isalnum()) in tokens
    ]


def _evidence_selector(capability, kwargs):
    """Resolve explicit evidence or client identifiers to evidence record IDs."""
    if kwargs.get("record_id"):
        return kwargs["record_id"]
    if kwargs.get("client_id"):
        client = CLIENTS.get(kwargs["client_id"])
        if not client:
            return kwargs["client_id"]
        record_ids = [
            record["record_id"]
            for record in EVIDENCE_CAPABILITIES[capability]["records"]
            if record["client"] == client["name"]
        ]
        return " ".join(record_ids) or kwargs["client_id"]
    return kwargs.get("user_input", "")


def _render_evidence_operation(capability, user_input=""):
    """Render deterministic evidence data and simulated write receipts."""
    spec = EVIDENCE_CAPABILITIES[capability]
    records = spec["records"]
    matches = _evidence_matches(user_input, records) if user_input else records
    lines = [f"## {spec['title']}\n"]
    if user_input and not matches:
        lines.append("No exact `record_id` match was found; no substitute client was used.")
    else:
        lines.append("Deterministic evidence-backed records:")
        for record in matches:
            lines.append("- " + "; ".join(f"{key}: {value}" for key, value in record.items()))
    if spec["write"]:
        target = matches[0]["record_id"] if matches else "NO-MATCH"
        lines.extend([
            "\n### Simulated Write Receipt",
            f"- receipt_id: SIM-{capability.upper()}-{target}",
            "- status: simulated",
            "- target_systems: Outlook and Microsoft Teams",
            "- No external system changed; outreach, materials, and meetings are preview-only.",
        ])
    else:
        lines.append("\n_Read-only analysis; no external system changed._")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class ClientHealthScoreAgent(BasicAgent):
    """Monitors client health and identifies at-risk accounts."""

    def __init__(self):
        self.name = "ClientHealthScoreAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "operations": [
                "health_dashboard",
                "engagement_analysis",
                "satisfaction_trend",
                "at_risk_clients",
                "retention_roadmap",
                "stakeholder_outreach",
            ],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "description": "Operation to run; defaults to health_dashboard when omitted.",
                        "enum": [
                            "health_dashboard",
                            "engagement_analysis",
                            "satisfaction_trend",
                            "at_risk_clients",
                            "retention_roadmap",
                            "stakeholder_outreach",
                        ],
                    },
                    "record_id": {
                        "type": "string",
                        "description": "Evidence record identifier for retention_roadmap or stakeholder_outreach, such as CHS-401 or CHS-OUT-401.",
                    },
                    "client_id": {
                        "type": "string",
                        "description": "Client identifier from the client portfolio, such as CL-301; selects that client's evidence record.",
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "health_dashboard")
        dispatch = {
            "health_dashboard": self._health_dashboard,
            "engagement_analysis": self._engagement_analysis,
            "satisfaction_trend": self._satisfaction_trend,
            "at_risk_clients": self._at_risk_clients,
            "retention_roadmap": self._retention_roadmap,
            "stakeholder_outreach": self._stakeholder_outreach,
        }
        handler = dispatch.get(operation)
        if handler is None:
            return f"**Error:** Unknown operation `{operation}`. Valid: {', '.join(dispatch.keys())}"
        return handler(**kwargs)

    # ------------------------------------------------------------------
    def _health_dashboard(self, **kwargs) -> str:
        lines = ["## Client Health Dashboard\n"]
        pv = _portfolio_value()
        arv = _at_risk_value()
        lines.append(f"**Portfolio value:** ${pv:,.0f}")
        lines.append(f"**At-risk value:** ${arv:,.0f} ({round(arv/pv*100,1)}%)")
        lines.append(f"**Avg health score:** {_avg_health()}/100\n")

        lines.append("| Client | Annual Value | Health | NPS | Margin | Util % | Risk |")
        lines.append("|--------|-------------|--------|-----|--------|--------|------|")
        ranked = sorted(CLIENTS.values(), key=lambda c: c["health_score"])
        for c in ranked:
            lines.append(
                f"| {c['name']} | ${c['annual_value']:,.0f} | {c['health_score']}/100 | "
                f"{c['nps']:+d} | {c['project_margin_pct']}% | {c['utilization_pct']}% | **{c['risk_label']}** |"
            )

        critical = sum(1 for c in CLIENTS.values() if c["risk_label"] == "CRITICAL")
        at_risk = sum(1 for c in CLIENTS.values() if c["risk_label"] == "AT_RISK")
        healthy = sum(1 for c in CLIENTS.values() if c["risk_label"] == "HEALTHY")
        lines.append(f"\n**Distribution:** {critical} critical, {at_risk} at-risk, {healthy} healthy")
        live = _live_portfolio()
        if live:
            seam = "n/a — enrichment seam"
            lines.append("\n### Live Tenant Portfolio (Dynamics accounts + cases + pipeline)\n")
            lines.append("| Client | Open Escalations | Open Pipeline | Owner | NPS | Margin | Util % | Health |")
            lines.append("|--------|------------------|---------------|-------|-----|--------|--------|--------|")
            for c in live[:10]:
                lines.append(
                    f"| {c['name'][:30]} | {c['open_escalations']} | ${c['open_pipeline']:,} | "
                    f"{c['owner']} | {seam} | {seam} | {seam} | {seam} |"
                )
            lines.append(f"\n({len(live)} live accounts total; escalation and pipeline "
                         "columns are real CRM signals, the rest await enrichment.)")
        else:
            lines.append("\n_Live tenant unreachable — showing embedded demo portfolio only._")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _engagement_analysis(self, **kwargs) -> str:
        lines = ["## Engagement Analysis\n"]
        lines.append("| Client | Exec Meetings (90d) | Escalations (90d) | Billing Trend | Utilization |")
        lines.append("|--------|--------------------:|------------------:|---------------|-------------|")
        for cid, c in CLIENTS.items():
            flag = " **LOW**" if c["exec_meetings_90d"] == 0 and c["risk_label"] != "HEALTHY" else ""
            lines.append(
                f"| {c['name']} | {c['exec_meetings_90d']}{flag} | {c['escalations_90d']} | "
                f"{c['billing_trend']} | {c['utilization_pct']}% |"
            )

        lines.append("\n### Engagement Red Flags\n")
        for cid, c in CLIENTS.items():
            flags = []
            if c["exec_meetings_90d"] == 0:
                flags.append("No executive contact in 90 days")
            if c["escalations_90d"] >= 3:
                flags.append(f"{c['escalations_90d']} escalations in 90 days")
            if c["utilization_pct"] < 60:
                flags.append(f"Low utilization ({c['utilization_pct']}%) -- may not see value")
            if c["billing_trend"] == "declining":
                flags.append("Declining billing trend")
            if flags:
                lines.append(f"**{c['name']}:**")
                for f in flags:
                    lines.append(f"- {f}")
                lines.append("")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _satisfaction_trend(self, **kwargs) -> str:
        lines = ["## Client Satisfaction Trends\n"]
        lines.append("| Client | Q1 | Q2 | Q3 | Q4 | Trend | NPS |")
        lines.append("|--------|-----|-----|-----|-----|-------|-----|")
        for cid, c in CLIENTS.items():
            scores = c["satisfaction_scores"]
            trend = _satisfaction_trend(c)
            trend_icon = {"improving": "UP", "declining": "DOWN", "stable": "FLAT"}.get(trend, "-")
            cols = " | ".join(f"{s:.1f}" for s in scores)
            lines.append(f"| {c['name']} | {cols} | **{trend_icon}** | {c['nps']:+d} |")

        declining = [c for c in CLIENTS.values() if _satisfaction_trend(c) == "declining"]
        if declining:
            lines.append("\n### Declining Accounts Requiring Attention\n")
            for c in declining:
                drop = round(c["satisfaction_scores"][0] - c["satisfaction_scores"][-1], 1)
                lines.append(f"- **{c['name']}**: dropped {drop} points over 4 quarters (NPS: {c['nps']:+d})")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _at_risk_clients(self, **kwargs) -> str:
        lines = ["## At-Risk Client Report\n"]
        at_risk = {cid: c for cid, c in CLIENTS.items() if c["risk_label"] in ("CRITICAL", "AT_RISK")}
        if not at_risk:
            lines.append("No clients currently at risk.")
            return "\n".join(lines)

        total_risk_val = sum(c["annual_value"] for c in at_risk.values())
        lines.append(f"**Clients at risk:** {len(at_risk)}")
        lines.append(f"**Total value at risk:** ${total_risk_val:,.0f}\n")

        for cid, c in sorted(at_risk.items(), key=lambda x: x[1]["health_score"]):
            churn = _churn_probability(c)
            lines.append(f"### {c['name']} -- Health: {c['health_score']}/100 ({c['risk_label']})")
            lines.append(f"- **Annual value:** ${c['annual_value']:,.0f}")
            lines.append(f"- **Churn probability:** {churn*100:.0f}%")
            lines.append(f"- **NPS:** {c['nps']:+d}")
            lines.append(f"- **Satisfaction trend:** {_satisfaction_trend(c)}")
            lines.append(f"- **Escalations (90d):** {c['escalations_90d']}")
            lines.append(f"- **Exec meetings (90d):** {c['exec_meetings_90d']}")

            lines.append("\n**Recommended retention actions:**")
            if c["exec_meetings_90d"] == 0:
                lines.append("- Schedule executive sponsor meeting within 7 days")
            if c["escalations_90d"] >= 3:
                lines.append("- Deploy SWAT team to resolve open issues")
            if c["utilization_pct"] < 60:
                lines.append("- Review scope alignment; client may not be extracting full value")
            if c["nps"] < 0:
                lines.append("- Conduct root-cause analysis on negative NPS drivers")
            lines.append(f"- Prepare value-delivered summary (ROI documentation)")
            lines.append("")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    def _retention_roadmap(self, **kwargs) -> str:
        return _render_evidence_operation(
            "retention_roadmap", _evidence_selector("retention_roadmap", kwargs)
        )

    # ------------------------------------------------------------------
    def _stakeholder_outreach(self, **kwargs) -> str:
        return _render_evidence_operation(
            "stakeholder_outreach", _evidence_selector("stakeholder_outreach", kwargs)
        )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = ClientHealthScoreAgent()
    print("=" * 72)
    print("EMBEDDED DEMO PORTFOLIO + LIVE TENANT PORTFOLIO")
    print("(live section fetched over HTTP; falls back offline)")
    print("=" * 72)
    print(agent.perform(operation="health_dashboard"))
    print()
    for op in agent.metadata["operations"][1:]:
        print("=" * 72)
        print(agent.perform(operation=op))
        print()
