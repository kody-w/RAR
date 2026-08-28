---
name: "rar-aibast-agents-library-client-health-score"
description: "Flags at-risk accounts from escalations and pipeline on a live simulated Dynamics 365 tenant, with an offline demo metric fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/client_health_score", "rar_sha256": "66dd54140f9f2a67673c6ef566ed049e42a285ebb042a6507ead5e63d01c72db", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["client-health", "NPS", "retention", "professional-services", "churn"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/client_health_score`. The original RAPP
agent is preserved byte-for-byte in `client_health_score_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "client_id": {
      "description": "Client identifier from the client portfolio, such as CL-301; selects that client's evidence record.",
      "type": "string"
    },
    "operation": {
      "description": "Operation to run; defaults to health_dashboard when omitted.",
      "enum": [
        "health_dashboard",
        "engagement_analysis",
        "satisfaction_trend",
        "at_risk_clients",
        "retention_roadmap",
        "stakeholder_outreach"
      ],
      "type": "string"
    },
    "record_id": {
      "description": "Evidence record identifier for retention_roadmap or stakeholder_outreach, such as CHS-401 or CHS-OUT-401.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `client_health_score_agent.py` and embedded as the fenced Python below (sha256 66dd54140f9f2a67…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `client_health_score_agent.py` first:

```bash
python3 client_health_score_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 client_health_score_agent.py   # or on stdin
python3 client_health_score_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/617abPbRpblX2FoPpRdlETsizt6ZgBiIUDsAAGC7Q4Z+74QK0F3/fdJvvcsu8qejvkwLyQFCWTevOu55yry/fopmKe8Gz799ImRWMZ2Pn3+FCdjNBT9VHQteCzUQTbugunLUIzVLoiibm6ncZcOXbMDC4M6eC0EK9p41xd9UhdtsuvaXbCriyXZjUUzgyVJvOO2NmiKaNyhBL6bkjZop8+7tZhysHXXpenbxjhpul2TTEMR7dKgrsMgqr4CnZJH0PR1Mn766T/+8/OnAnz+9NOvn6I6GMGjT8e6SNrplAT1lNtRNyRMBr6DbXXQZuB9vwEbW/C9T4a0GxrwKE7S3ce3H8akTj/v/v73ag2GbPxx9+V/7sZp+Onndvfx04GVb2bu/n33vuhrlkw//Pzp+4ufP33e/fwpf9PgWxyMedgFQ/zzpx9/FxIXYx9MUQ5k/Pr709fPX238affS6uu3f33z+V+3Jm0WZEkD7P0WtEG9jcX4++6/ePknASMwYEyD6GXGt2lI2j+c/ud3f9oeTN9emfEteovBH87+lxd/2jgkIAneBA9dEDdB//vWP736s9JTUCV5V8fJ8K2bgWZBlP9B7b94+wcR//j9Yw7Stk4GEJPfwvMW2e9x/UP8ivT76mLcaV2b/PTPWgGt56HdpT9/+vvf+WHohp/+/vfdpa3abm3/kEK//Pr98z9++bpzg7qIf9r9+rfPu799Lbui/eG7JlWyjT/8+OM/fv70+0Efh3xo8sP3pP30D1AWLUjb+S1Yr6r4H/9jpxbR0I1dOu1AWczTbgC1WzTJz+3PrZMDK8CfKU+A0CUZxiKsk491/dCVyZsgUJm7X/53UITBOH0JXmU1fqmLcAiG7fAe2d9SdHwVHjDIAQK7ocgKkHA7izGMn9u3fa/D+iEZk2EBaBBuU/IFVN+X14ddAdzyF9K+vW382m+/vMELWPXS1jpKuyjox7lOvr4s8fKk/dA7AlCSPJJoBjLrDoDTLi0AanwGFo5dDeBoelk9VkVdg4APwMRu2N5kA8/89BL2yy+/AFPzn9t3zEB371g4HsCC7+rsvnwBlgDEyvLp5zaJ8m73t1//8bfdf+3+u11vwl9nGAC1PvwONJRtXduBGM6vMgUhAUFMgvjN77/+48OfQEwL8g5EqUiL5H0zwMsqiX9zrn1iviA4sQsT4FTg0Kbvhqlos10xfd1J6e67vuDQ1ysA2Lu8GyeAuD0o66SNNiA1AOZ892TbTbt3ANg+7+YxeTv1FxD6NxWbbxFY/stOPRq7qetq8M9LzbdFYHPXFsD930P//hwIGf427tjfRHzdaa/M2/XBEPT5EHyc8QKcV1y6YffbdiA82LXJ+nP7wv43RHuroHf3gEXJq2O8h/TLK+a7qGsaENjxt7Pf1rw1IqcDuZwMP7fjR4oHwysUUQdU2XbZXMRBGyX/9pFSY97NdfzmP6DpS9JHFOKPqLzl4HsH2r23oN1bD9q9NaHdzzMCwRjQHtjbvzrhbuvmtyObBLTAl9uaGRjznssq8Buw/VUpXZqMI1AvqL+8aqaIQNzfa2T3CmDa1UU3Ape+gvw7zn80zxfcaoa9eysjkP8fBb1rQKIB34N4TkVdPN8R6eUW8OhVBr939B2olFcUgFr2PICQJH/BAl5bfnPsuPsO27v3jrED9rbjm10n3ds5J8neObxqKIzD7zzdOtsvXIO/7nTgZ5DvL+eG3QOk7K6f63p8ZxCvyAwgjq/wvFfMyXGMdwICdnxAY1Z3IeAL21tSg9jYr/yI/op07H5gXuHfKQHgG3qaAsd+yLC3V1KOv4Vs3Fog/yUlDqbg867tdtGQxC8Tgxr4a+2G6oMIBe225smQ/PhbS8inqR9/OhyqLt6+rF8zQHPm8GvRHcY3vb7EH3p9AXodgr44vI44LPRX5PAhQWrfwep72ry8824BKKHfI/CWuwAvgndUeM+QDxnf8+Qz8On46kEtqM3xFcnxj6Eei6x9M+kNZT9Wfsjo+peUGaRl8b7vO8n7cFPyNfu6OwVDCMrVeD0/gvYz1y/w+fohwxm2n76zre/d79//r4QJAcDQgXKfXi7+Xzv+VZjAGSDRX5xw3L1Y4atwXgYnTZjEMYj4G3Wsgw2ENkzqbv04+4ejIvGaY+8OO96VOF478t+OjMGwkiI5Em//+JsdL2HvcNO+gVIE8CgHJn9Q0zdb0K87FVCLV4aCKh5eFfG2T5FcfscxDrOzeUZ9P/9FRn4LxLsO3048ozinb/ZRt/hvr+XfLpbyMgTkz07nQAp8GfOgB8YASO4BFwDJ+jrnQ8pb8n/P6G7IPr8g8q1/JI9XlMDGt3R87dkZNvPj2wIA+HXwPcm/pQngFt+irq7f4e+HHz9Y+M4OQK8EMYqSgw4SgCmGj3T6uhOKpI7HP9QbQJXvNfuGt22SxO/pWBdvFQhw91sLAg74zTP59irlDyr4w28u/xAFcOrzBzC9Z+A/YdOrOQ2vvPv5U3sIviddC0AufwO8MQma7wzpxW/qN4RdQS94d8Q4A8axvTepl3jgmDdM0g3eYhxJ195g6F9TETTzv2DP4Olf8GWw/b92/8J3wZM/0djX7r8irmD/O4376Q888Ychuc/AiPjHzx8Y+K2IP39EBHx8jTcAu0AX+/RTC+Dy8yeQGMl/Nw292ixoD4DqvYYn0BLAWa+qfh+lfhMLvvzzBPjR24o35AONb/iOvX/qR5+Bs8GEA6J1VL6gEPxvL0IO0mx84xYfywF8JctLWvQbuL8mvGnrX8oDBgvq/MVmv3vizxrp3530Tjr+DRR/GgDMGV8P/hTJ9UUQu6aYQFq+DZPtDEbA//gT+ry9+lPIwdM/hxw8/Jd4gyd/ivdr61/E+9N//oW530P8Z3P5f/bWP0Xirb7/Nc3Aw78cgX6Pzsn+gkHwa+Hro35xXl//Igxvir2n4fvo/fG+C1904qX3qzm9z9S/fgLJFbwa2Ud6fYwQYDkYF76MLzp1gL9CL08FwzstBu/+34eLj40AIgHTBTsJIo5xDMaglE6RgCAJEo2IJMUJIokhjE4wJEAoPAlDCHwicIgEfRJPCDSG4IhE4vAVHgAQEQAmQBaLlzJhGuJIFMIpRFIJTWIJDkNAGg0TIZ7GCU0RdIjSePL71qoA2fBu4btFL599n3Nenvgw9NdPIYGBlSdslJj3n+OBvtABapRar6QHe1rbsyVGhRVU+aGEgifiDqJbigdar2bHVXtLdUzB89f+Mp+4U49M92WU6f1p5vbYMieYaEuScUkD9QIvQzNINd9kEKTTIkNoYHVg+aiK3tg9TvjmUxtMqiWNveKQxAM9HJSndtv0SHmsK+6hnaXuT3UrL6u6OL7BDIC/EHCcBHg8lzjjLhjam6csQfB+UtX5RC/e85HVeZ5jaZvDJ21UENbylRktwV+8QFKMHHEORcNj3oc4HnNCweimqeeHCJsSsSUm0lc4QjHj+XlQK515oqsv5sSN7JzHykkxdbUaFuOky0QF1kJeHio4RG/D1YKeSjQrKHfMTiVDO9nRf0KqfyLnQFgQdg479qm35SOiR9oQqo0PuJFanENTMulAYPtlWgtSRJ4FUVSn2hFGDJsP/F59jI3wrPWVfZJtpknribJVfZ/sD5wQa+UJSgrbucJLWUIMszwjfSI0wskVbdGPFX/weTm0p6l8QOW1HVl2pBEmdSdSqAMS7vyr4VTIdcSWXpBvl4zNZiytKImTBPsRMxJmy+Kt0/B2UKml4nvEJ0Z+NdqWuh5ZS40P1Yo9iSVePd+zsjmbSf3ZQ6jn+CktjGTLX9B5RidWsuxok60gk8/6PjyiI2/FM5mCYoiZhONzr72ZUdfNx/VIkwk7zthe6SDc926MYlrgLEYOnlameKdamB51nVfZ3jy7iyTQBC1TlZQ/7PV09LajeWRLS5ggj+4kUruvtyE7XEP0ikCptRgyHWOjWj5XqJBXE4H566EKD+OYXdEexw7DKvgtFI6Bo9tHRCvYQQ2fBxOM9mgQoxZCluI1J4v5QGGiqVf1wJxWWrN4Y8gegzNfeHltW/qwbqYlGbrwLJ9twzc5vj7QxfQfof7saPG2GXmznbgrRugWEZ1WRO0OeH04zA6EG9bmsb58WK2Kr4/EVa7O1HhKxWOCtvY5okyc1IfxqTzLTVqzu4NvRnshjbTuV4kkuycWckvf+iASRzKPklKkqOvJNB4wrUm3kwBHHAOPYUvgemQOjDI/C5EvE04MG+YesmjUHkecXyIrY3MlozAXNRYEZZSDn67Y9HyUVHkNmFS1aMS/pVzaQ8GeXX25ubU+1XMBcvPbWVv50Q1aB2JUTDqLfadzGLMK0x5nJAUNXXorKXw/KtXz6J5xZvSsQg8vcVmMAk5JeKuNVemEN99XLO7G1leGk2PfXMU7BDOSej+LIszNR8Q531ncZwKGofqhIvuZWQTauZaCdVtVBJfvDIPSo05E0AnZxwVVnSr0oNbD+dnyIutzGoMIeMLdD2SH61IkXLYEjwunKzqN36xM9I+UEfIMxTSN2fI3KZCE5bYH34O7wVVTKOedHhnoU22jq8i1vJLXeFmtQqQrnRL3z4AjUdNQ9bnYLMbyn0l8sCTuwEpZE8tT7jzuNrOwIG/VYWyuRhURWSEpWIfH1L5EV9TInzg36wBGS+fIucLgXAXExyDoxEbP/Tj5zAOXjTSLpjt1S2TS1FAqscnEMjIU73NJvmjdSkpBeJ/lkC5Dy+rotPOomNDEuPCkwJKkRaWNQi4n0oNvVv6EyCsLlojrdRgrr+jYOFCfEDJtTye9HrcAPiHtECZQ3haGp5/CBa8Qjj2e2Yp38LkID618GnqpOrsNMh9TSXX7M6k9PX1r+cKCGLway3x4euYxik3eIOjifFlP+PrURnuG4qHSe9s3M0f2K/EiF8sq46f5dHTUxrhUR6V/9P0p4Nx8qVq8SwbHp57qWX7gRqG4xqHZG4+n8IQMhpfxJEBkvGlkvBLXLDGy1ndL6jL3LsZMg7A0s9YDbLlwhNCtB+4eI2oszd3Mp3yU72fOYS45O9dlknZ7wX9kULWukRjvKet5FTeIGS9pHB15yOgOK4z7VZwrPOgL4RPKF7Q8HMj2eohSTKae4t6qDIkrJEE15jrvVFihGKcqPGSfwU8xbRrWmwnrcN0rpcxgKnNsMR1rhozATiYqb1GhbnHXjJwj4aZRWlxJi9p+tQNWucROuDHMdXHu3GiEZceVTbaWJeiVCQlJgqzDbs+18+OOWWvTcDXAVTPj6wlp+6dVZdH1hk6ZfjOeWvbwWS/jqnBUvP2RySpFxrbrKLoVjh0XGecBmsO3YXCL/UBRNIJaRUYtRo2wKmbtbWavMVlRktd5TseFa3rudG4UYVyeNVnAzF2kbmcmzSoWpk9nVjO1JqHESo5j3eAsMEavWDNdoyz11rVioznP7laBkVmJqVbSdyN5kdMsDLKeOcfXlDdpoWOSLHWj5UAJq7RpHtRS3YU84+6SPZA0w+nNh4ZZ3nj3ek+L8HyOBVqUyt4P/Lh24isHFZrcb8ORSY8tb6Iw2qZ+cCFVcxGD+mDtV6uuuAHeywvpVUIECwm1WYlyfTaqnBBJ9rCZQTQQplyFi5x0h0CmGcbxeFZFAlyMJ2oc98N0Gun9xbQbFchtJD/zcN0uB3zC8DtbPNmuBwCQRgnTZ3f/XpGYwAuat5U+mnFUmeZnlYcV894+L9pqYHk5gVAXEYcw8EXQl+35sKJcpJm0UeytzBRicstCi0aDC7m4rqRuX5D4CK+oyczSqLJ73zMl3zWbgL/faFcS0Sa434lLyJhrv+J3FfeCKsPcCaSONGmswXZBo2t3z7dohlIFUA7QKbhMWyu5Ww6cYCSxlfEVeyr8eY6qRlvMgsnOUaaoJDdg5UMUZ5uvePKMDnny1GmLVEWUo7aYYg1rPJXm+cxQaFrNM7cxmWpe/IjfnwtGVFv+gZQLdzCCruKW7cplT/nUzltRsD1SS8e8HbN4bu1jJEntpl44ax84BVKQzcyoOH/jcoWiRTFItooIrQFwwFy9ywXN3kWIhTvFpfZhNG0RZMoonDRyd+wnQYStw+OcFrE3DoJlBsaBV6MtV7P4wDUFGGCN0o8OpstejStkHpFLU3M3Dua1UWvPo2Q/M6VQn8nFEILzFEZWsFV8ubYYwl1PBlHNkJgjRb4f49tFCLFcDDGrlOAiEaU68pG7DbJq4bEj2ymFlwDCUPgmbxMlc3YpnXMK5qSdeSMp2CtDZvwdmR1ViyU9lA4m4u3R2vEFCuLOlzxgekOeRnUNSYB+nUPJS8YkYHZj7f1zZfp1W6bab4xxUu+nB0zR1eXS9SOPZLLVBA5j6xe2lvnUjqT21s8X/yZP9/vlHm4OBR2tQCqR8gYAYr0plzN7kMxxVJ3js7i0FWAb5pQXSH1SspS2PETB8+iedo5oU6dGeei0FARMsUxVUxUz5fbMwGAE9RDzmM+kNLa2E9/48OXCQAMFHx2KLYaxbQw93PxmJAd1LogzlmdPjs2u1AOzB4iwXMOA04wLMP1JrunpgclZzFHYjIjtoaZ4905d2ZB9MnBN48gZwrZbUgk+rjfkPGkl219cilXg+1Oi6HRkNZTph2jCDdM1HXfIRnY4Cpewj2G6HrALzGjP9Lb3MQ2b1gPs3LVzzByQWotQbcg18g5L2lFMMD0FBKSo/HtiQmiZrq1/5wzi5q1hECeZu8Cx9URs6AHIETvdJRmdW/J59bMYn8cTQhseMboWThL92vGX0GtdqXe3pKwIbX9iH5IA82YHa3rJUn0hXg4IAFgFRHyPjWd/cFD4cSwhuudLHj+hBFU9JnwvOGIz6qUb6/nY8RqpPtCE8GMpX0kb1PhhsoduPO2xOiPp6irA6vIgRatGNqrKxpry8FY8tbkuc1ogB/DV6mpNLzC4gHwBd12luCbpcFZOJH0zMZa1bzIfKeer4Jt+w9F9bPr3fcQvkHCgnrrDxcf+KB3kA4aL8zZ30SmxCmWcFo+2Cyk61b6FWcEIXUIN1nomp9EWYk4VxnI9xZI9peC2SsKpsybWeijqkiFJ/GpiPdEwQTnAYYOu6yZIe/qEdsUwwVw19lQ4Y5fA0jUndV29pOjrJRD3mTVH+H6u6Mtd5xYsm9nH9aJrT5JvuqgWtDLglmzCGSeKXA5Cg7ugGWRUypCeL/J4TtD78+qscdz3dZKvDnbvfY03QmTpVJE82Pt8DadNrJ/B0EwBb3SGJG7E1Q363lfhvuFLFjRijS7EUnoedK/vyWd9P8eudEo32CM8b6kykxtnOVJvHIoZ5oaanI4AEp6x5wm+nSdXJks3DEjuTENoMjySE91ChHqDKv5o6n1fhvt7oYiYOY2sZMO9c+GCW24hYOTnCwQysaSbpul+6ifFFZBNnG9nrU7MxGQIf1ZTybBcfrtvaOa2TdXYRkPW/EMLxhZWn0t58q+q4d9ZcbxBkuikJ3NqhLW/oilv8dGhmiD9nBQYSp09vxc02U7N1VYJCanuch0ZeynUF505ErnDqYahcVs3kPXq6Vj8IPjGgV2HnZizsc0rmC8ymBcvE4wKq21BiHsSHvGDyaRnwx78XFQvZHG4OXiiRhWfCueNY81nh9nY0Q2VdQtC1iz22622icxTPebGU/7ymKgVNGE5Y0xyHZi1W0oN8oQM9tucJaL1tBW3abNF7iiqc3cW2201qjjMeLt+JvK2v/h6fBweebw6RBIkxJ2bkPjBQTAgxHQ4mXIlEXEWjx3reVIjDOqUcAb04qZ3ix3wAi6cvi1U5ZgpiOee0PPIz2krP4PxMpe4Gu59HqPBrFJwvRun23F8UJJTA5UIHnKZqjoEgxdtdrfqlBnVSBJG3PGcXpbbvbpAUtETp/XaNaIXT5e6wrdHX2vQFvrFJdXsy9autbAecXopOdo4Vw57KxshpIMDDFPigARcbTVXW4lTBtfvbvnw+CK0JDNrOs263sB8Jg3WytqHEJ+qXAdeerQWe1ftCmsML7tDxHQVjqaECoTcBKM06RuXUNAdTH6h5xxltoKIIaLZkXR8MgEwjLp+r8PVk2I3zNykc3zSVhs/SLd63gto6VQSgunmfn+9U9J92PSwFvuqj0qERFCTame07DXKfR7vqvy0N1u6efCsI8fW4JK53q4uz22hlCXjksbtxbPHfXle2nmhNzD9ejItKkNdrd7Uxl6tSHGt8Qwxzfc0y+1w5oIz2uABdiznkMxT6XqqoAFur14cY45Sw0fUGNR2P0LYnLn3w0l89I/BpfekyEOPpwxadZmdJdO7QUfZ4RSc31OAf7q6K7jrkN5HH3l4gMXOQYjLTXSiB3szLjQAH0h6hM9GmfBUDp2jdTflRgdI6O+FEXv4oi9zj/txNE9NhD43Db2Man+Ec3jKVATCkIPmZuQa5n5ctKguKJRlNidIVmz5rlZon7E6ADr+Aq8nI/VP+KnPVptLQcafI/zEKNjM2ahIOYSdFSl53I+XqVchkVr3bi1biq3M4xbX0lkJ41Clb+1eW0hHJLkFsPJYwdSn9YS01LuZqy5UUgrzmaaOeX8aRWI+l7Tpn0xpujbMQHJsOTw6u+Mi5bRmksFYFx/1w7pXb2pgPxCvvnp2fIP7O97X1aEQfL5J9w37gFNmCbyDDm2tcuviib8HZIK2DQkNAX3r8dsY16U7TKS/ofBMUvadFTBUKNinxoBgdqwvYMbTJwvpjEF93AdlybFT3txGLmUBqO6flceYk3++MWhDHSNZKqhOXNFGIvAwW05w0j/80U/aNOJuUnahmCsedivTtSGnexoytxbT2ivMYE/UxNXHesnvSDKw56ynsxNq9bV4NSkGDVmvJmeMyIN+rCWIp+8ngaUfKiyrVwKCz6prTcrkpRL38LrN0c1mxVYpZmbCpGCIE6By8yvVc8/z3bzY1tG+FmSdUVIMk0jTC+TiczSz2ULRWrAgzaovdeKlbC/2Ya2a4tp4460426sH9OOTsbZB0j8yzjnNOjHPZ2zZ0ASP7u24ZB161fjcSyr4pNPHzVGEPq7FMw+Z13PMNznVOuUKCpxJn5sdG4PonST7vB7OMXGhH5mrPTab7B09p/ocrihiLGyWP2dJsS+MRoNFuFbk+HK/p1g4QzF0cFwjKNd1dAqepHUvL1CulkT/cR81BrbPC3MG7uwTDjEHDzsiGBs4/gxG1rNa9G3WkLhwS+/HbfTa+9WuOKeP4GPGRAdJR8IcDOMN0o8oKYtiyi8WSi8Poo5Q/NoJRxW7Ia6nNwdpYGJDY93bHiat5xPkBx33y9GtDzyK+hlWw1DC8qnKjZe7rGBQhycZxTmtdYs7oRseSzPLJuHYD63iK68Rp+u2H8xaj5RqK3SIMcWDj/cnRJpb727E6IZn3fG2nHXXKrj8clGJEmtmWITGh3mDG9l+HOX7mTiBibDoiuR85CwmobLuafpT4tO8xZHpViSxn56u6CUal6OBJVIs+Fqg7IkQO1IrZlnpdhMX66w22Yj3JZtvkbTGfaQ5FBGUW3N9FP0Bvq4X70xvh4An6x4XTCdxS1FyoDgy6ZQzaaPK+avZwNl5m6FaMCJjJXqfMymXlWVc5nMx5fRrcePMOBLu0iJ0jk3F8M3nHrcuJGHHAxNgkw/FuvdTi+35WoliSVNcDWEfTCU/TplBaJv1eJyniIXTxWXKjtmimBVddjBVawzGm5/w9RnMGiV/f1gz4T3s1HPHGZvaiM9xPittjGAJUmPWYGYQh3WdAqZhz27udaJXN2sxEq+w8ZmsoXx5DNV6VMcYRm4aR2RiR1AbGQV46rfi2bNp2NlUWhMaW98yHKqDoCoy3kO8KarSxO51Kg8QEwTflE+6E97iFHj78qyFlMVrCIQZuR6xrt0rMcbcPCRgzHlkiRwkyMUSjvF4vWpjpeZ1e4RyRNMC56r0SpnO7LLvRaVZaaiWogh6/e+XFN1mfUlQBuc0MXNXlF3by4Tj5ytFZR5FodI+KQRjuRWH69gPwnVD5QG+NZNDqY+8qaRJhnpW0AsD54l0HcWnyF2PrmpAOlGDcQiROdnx9uWweE9nge+HfZRYh1oinco/HfI20+qgdqa9L8oMyxtmnz9uholsUowqePm4145RxDqxjSehmoMBlmQeN4aucOqjTguKYgbKcBkXH1nud1tUHAot92sYor1vKciyFyIDh5VjbWE92ThZC3uQ5rZkcl2e2erm2wTI5jCxclOu5WE7tzO1QLa2wbiAzDFWnwsHOHN/JfDeVVDuhBpaMoTclNLHmdoSLVhKqBltxNkessfEMaD/3Il+yDbP8M6+8Y4HsnicXAZPkUr0z/0UrjSFHnQSoSf11MkWotvoY+88iTKJD55JEMp4WBpknSjl6mgcM4LCru4blLLZPAZZfT22Pl2C0ZW2rQ01blZVS1JtqhfFaGeMLiW+yew8rlBRg65afrc1IjTKq0SawUU/gN4gpzfUzKNDQyXCIY3ziQiGwT6XLdpDxRD74tMq6UtiWX7czisYmdNwcIPy6tK0R1B8ctqHdnwpnmqq9iN7Z1eOLrqkhDNzcQ68DaB6j+gHrLgoXo/mWotk5QFr4kvKm6lR8PRTpo6P/RwdcYM4gAxv5MBALl2LLtSk3/DLeh2bjRTJAcVc3tqrhFIlvIkYOKTRTQ0w4TgeDVWBG/5cHNzuGtLCM8WRRZLcPRMc7vVIhVQCqvJcF5kDmcLAiATEq6MQsxp3mKE2muECYZ3jvrbpJ+0O2zMF2VNNaJUwj1G1nLiyBYFisJz0BYuNTnDcLQjB3emb5TB+Rx0vJyLqS9mYEi9qMVdoFRy3uZK67+F1sQfQOOjwrJ1AgQlUYZ2p9DxWnXsf+Qhf3EvURVJZxNj9UarPJ4eKXXflLsQdeaDxzbrbpTfAmkvY43a5Zbc5uuT4tR1rmXajMbVN1I8P57nT9zYPD/AVBvMwdNcyCxwiCfYKePk1Ck5LAgbaPr6eZcHfYNPwAvxs5xRtXPb0jXVVq1QzPSBIMg4w78Fdgsy1XFa5ojHq6XLYHqRqAilQOSVR8HXjEl19cWHmlmXcWrAPC2C5dPfO8MW63Usym4pssq5r5Tl51jwkFOeQ2aCRdsCeoUb1j44sAtRz2vsx0UVDUKNcfVDqSWhlMJlcQ49FLlYUOGcdJGVSWiKOy6yVW3ZMybSFeMPs3xto6Tg7xW73ZApqQiBTfusfTX1oOAa19f2J4CtO5F3QKjHDQKVOmRnZS+h9ABtiL03lY9zTwslhQigJqErXsUgPhaHjKMLBaAxu9SIqanJDCJev4COnWG3juXfPSLr6LrAOQu9PNenhRtPVRegIQWkFW6xt6aHvM6e5LtdlvCurSAmczrkScQ41NfNcbE6I5yY7iovoVdE/Sc7Ttux5Xu+nq39aIRGWxavxMBupc5+Xjh6OR6nyXEc8bgn0eOwtPKkxDow3nLzH/U44I9fy5g3eY/9cDqFPdoH14M/XC+9NgYatkUI2p25iuLoL2ScJn0rFbYcLPDHuBHnWM4JqEsykrSNg0EWS5Wl4pDP/6KeoaSxnr3tPSbZoZxb4pAjzeTyPPly0G3PCA44njZsgxygXmfadR5FGavVtaqmWMHAbuxdLYZ5PRZ/l0m3fL+Th+Qz3xHxcrukGsyRdcJe9jqAqvAegsoXRcnm4veXGruomWwzdfZrqh2cyCH13my6Abl/s1iJKZYI2r4FZs/e14fGIDu1eYL2rLtBRkNJVGBSORIzE5AW67XPDFmXdQa9IULfXEKJraxH6Y1wd3bvrwQEkriwuB+d9fJQulAK6w7kVD1Sj3vXzovfm/UqdoyQvhvHy3GZlfFhV6wJARJQ71YE6A/2pcc6QWQISP+R3Cd9PxJHsBrZUO6LPRTdullSbpvJcP6O7EG37pidnaC4xAr6Xhzx/BKV/hfG+wc0pq0ahmgARvg/7J8wf5vDZb6hlGMjDlqrsXm2z/mwtkQwcPOMjJcJZb0qKw8BaSB3sb9Vdc0eLwo6pSJ/csPLxSxJO28mVjwtOFlOVbUXHHIrOtp5nTr0IN+/Al/tabJtJdDbb5ofL+eix0a3iLwGtal13DGrh0GUchpeiMqr59ebovJcqUivM6kRYtjxfkTka91cyPeXBI6yzooAH6+rdheCe5qYXFHeOXoPKCbthRAD09Pio9J5uBufIpfo9exsmO6CnR3u5hMTszrZDHZsmHkYJjxfNF1jhwseC7T3nOuU5W2yUx+nYqy0lLryUibp2iU/7lDEf5fNaNWDUZ2rTYs/13hNvykTasx7j7Dbn0JpuGn45men10ac4Px/y5exbVN2bWbXoUYnRtnBKF7Zc2iMlW8seZfcP/gTsPTFZgCg91lDk8ajs41gQ03EdoqCwnClbIVJYrv7zYIwmObUiE/nqYA6pA7nXpEq0y4OdMJttTykVrhaOkYW9UQRVKQ3u31hn68dI4Ri5LfNFWmHbbwQ+vdy456VmYiG7LlVg495Kaj5P7c/RWS4iAtuMtDXG+C5co1mLy3lfoTLNJVtzijXRiwQkCCfs8TxevVNZz+e6Ig9X1yVECj5bkBT7kOI2irsdVv2pTTR5AQnHMJ08Q9QFXyKjeTxGGOEuasOq1oQpMNxf6WLJxjQ8hE6SD+FtpojGS28IZc4KgYsGvEVtva0k5dBbYLBJSlM1R17VHh6wAZ8SJ5CUZuEg6NT5e+MAQJ89RBSPM3Ade5Bjl2Z5cNsDIIGAnW7N8TFecV2yGqX0Mfg+7dkpncjlvFTS7dwvFmWFcKoZBLxQ3EIUVwmjK4Zh/v3T50+vi5sflwb/u9++eF12+v925+r9elS3vG4yR8nrGt7r+vJPb2f99N9q8Z+fPw1RAXR4v0M21nP228Wrv7pB9uVd2Jd3YV9+u0E2bu+/vNC1U/KYfrs6OQXZ63fLPv3THrBaM+w/Xuz79Kb7ny/mg+dRPg/tS8e3X6V5u/UGf0WApv/4P+CjFZxkNwAA -->
