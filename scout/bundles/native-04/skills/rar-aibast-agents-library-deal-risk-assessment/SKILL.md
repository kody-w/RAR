---
name: "rar-aibast-agents-library-deal-risk-assessment"
description: "Assesses deal risk from live opportunities in a simulated Dynamics 365 tenant, with matrices, plans, and an embedded offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/deal_risk_assessment", "rar_sha256": "82f7a32137a201c8376188a67c6fe060f9b269fdb48e6af2c08cc203ac365e33", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["b2b", "sales", "risk-assessment", "deal-progression", "pipeline"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/deal_risk_assessment`. The original RAPP
agent is preserved byte-for-byte in `deal_risk_assessment_agent.py` and in the RCI capsule.

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

Deal Risk Assessment Agent — a template you are meant to mutate.

Scores multi-factor deal risk, builds portfolio risk matrices, generates
mitigation plans, and tracks risk trends so sales leadership can manage
risk before it becomes slippage.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="assess_risks") — the assessment covers live
     open deals such as "Blue Heron Stationery — Preventive maintenance
     program", scored from CRM-visible signals (close probability +
     schedule slip).
  2. No network? Everything falls back to the embedded demo layer below
     (_RISK_FACTORS / _MITIGATION_PLAYBOOKS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     DEAL_RISK_ASSESSMENT_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON you export from Salesforce/HubSpot), or
     replace _fetch_collection() with your own client. The dict shape the
     rest of the file needs is documented in _normalize_live_deal().
     Champion, budget, competitive, and decision risk are enrichment
     seams — wire Gong / your risk signals there.

OPERATIONS
  assess_risks | risk_matrix | mitigation_plan | risk_trend
  kwargs: operation (required)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The analysis to perform",
      "enum": [
        "assess_risks",
        "risk_matrix",
        "mitigation_plan",
        "risk_trend"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `deal_risk_assessment_agent.py` and embedded as the fenced Python below (sha256 82f7a32137a201c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `deal_risk_assessment_agent.py` first:

```bash
python3 deal_risk_assessment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 deal_risk_assessment_agent.py   # or on stdin
python3 deal_risk_assessment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Deal Risk Assessment Agent — a template you are meant to mutate.

Scores multi-factor deal risk, builds portfolio risk matrices, generates
mitigation plans, and tracks risk trends so sales leadership can manage
risk before it becomes slippage.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="assess_risks") — the assessment covers live
     open deals such as "Blue Heron Stationery — Preventive maintenance
     program", scored from CRM-visible signals (close probability +
     schedule slip).
  2. No network? Everything falls back to the embedded demo layer below
     (_RISK_FACTORS / _MITIGATION_PLAYBOOKS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     DEAL_RISK_ASSESSMENT_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON you export from Salesforce/HubSpot), or
     replace _fetch_collection() with your own client. The dict shape the
     rest of the file needs is documented in _normalize_live_deal().
     Champion, budget, competitive, and decision risk are enrichment
     seams — wire Gong / your risk signals there.

OPERATIONS
  assess_risks | risk_matrix | mitigation_plan | risk_trend
  kwargs: operation (required)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timezone

# ===================================================================
# RAPP AGENT MANIFEST
# ===================================================================
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/deal_risk_assessment",
    "version": "1.1.0",
    "display_name": "Deal Risk Assessment",
    "description": "Assesses deal risk from live opportunities in a simulated Dynamics 365 tenant, with matrices, plans, and an embedded offline demo fallback.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "risk-assessment", "deal-progression", "pipeline"],
    "category": "b2b_sales",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ===================================================================
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export DEAL_RISK_ASSESSMENT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_deal().
# ===================================================================

DATA_SOURCE_URL = os.environ.get(
    "DEAL_RISK_ASSESSMENT_DATA_URL",
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


_LIVE_STAGE_MAP = {"Qualify": "Qualification", "Develop": "Discovery",
                   "Propose": "Proposal", "Close": "Negotiation"}


def _days_overdue(iso_date):
    """Days past an ISO date (0 if in the future or unparseable)."""
    try:
        then = datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
        return max(0, (datetime.now(timezone.utc) - then).days)
    except (ValueError, TypeError):
        return 0


def _normalize_live_deal(row):
    """Project a Dynamics opportunity onto the shape this agent uses.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not knowable from the CRM alone' and the
    renderers label it an enrichment seam (wire Gong / your risk-signal
    systems for champion, budget, competitive, and decision risk)."""
    overdue = _days_overdue(row.get("estimatedclosedate"))
    prob = int(row.get("closeprobability") or 0)
    # CRM-visible composite: inverse close probability plus schedule slip.
    crm_risk = max(5, min(95, (100 - prob) + min(20, overdue // 14 * 5)))
    return {
        "deal_id": str(row.get("opportunityid", ""))[:8],
        "name": row.get("name", "Unknown"),
        "account": row.get("parentaccountidname", "Unknown"),
        "value": int(float(row.get("estimatedvalue") or 0)),
        "stage": _LIVE_STAGE_MAP.get(row.get("stepname"), "Qualification"),
        "owner": row.get("owneridname", ""),
        "crm_probability": prob,
        "days_past_est_close": overdue,
        "crm_risk": crm_risk,
        "factors": None,  # enrichment seam — wire your risk-signal systems
        "_live": True,
    }


def _live_open_deals():
    """Live open opportunities normalized for this agent; [] when offline."""
    return [_normalize_live_deal(o) for o in _fetch_collection("opportunities")
            if o.get("statecode") == 0]


# ===================================================================
# EMBEDDED DEMO LAYER (offline fallback)
# ===================================================================

_RISK_FACTORS = {
    "TechCorp Industries": {
        "deal_id": "OPP-001", "value": 890000, "stage": "Proposal", "owner": "Mike Chen",
        "factors": {
            "champion_risk": {"score": 85, "detail": "Champion silent for 18 days, new VP joined org"},
            "budget_risk": {"score": 40, "detail": "Budget approved in Q3 planning, still allocated"},
            "timeline_risk": {"score": 65, "detail": "34 days in Proposal, 2.1x benchmark"},
            "competitive_risk": {"score": 70, "detail": "Nextera Platform in active evaluation"},
            "technical_risk": {"score": 30, "detail": "POC completed successfully, positive feedback"},
            "decision_risk": {"score": 75, "detail": "Executive change, new decision maker not engaged"},
        },
    },
    "Global Manufacturing": {
        "deal_id": "OPP-002", "value": 720000, "stage": "Negotiation", "owner": "Lisa Torres",
        "factors": {
            "champion_risk": {"score": 25, "detail": "Champion active and frustrated with legal delays"},
            "budget_risk": {"score": 35, "detail": "Budget confirmed, procurement process slow"},
            "timeline_risk": {"score": 70, "detail": "28 days in Negotiation, 2.3x benchmark"},
            "competitive_risk": {"score": 45, "detail": "Vendara offering 25% discount, we lead on features"},
            "technical_risk": {"score": 15, "detail": "Technical validation complete, no concerns"},
            "decision_risk": {"score": 50, "detail": "Legal review creating bottleneck, not relationship issue"},
        },
    },
    "Apex Financial": {
        "deal_id": "OPP-003", "value": 580000, "stage": "Discovery", "owner": "James Park",
        "factors": {
            "champion_risk": {"score": 90, "detail": "CTO disengaged, no response in 12 days"},
            "budget_risk": {"score": 60, "detail": "Budget not yet allocated, fiscal year change pending"},
            "timeline_risk": {"score": 55, "detail": "25 days in Discovery, 1.4x benchmark"},
            "competitive_risk": {"score": 80, "detail": "Three competitors in evaluation, RFP coming"},
            "technical_risk": {"score": 45, "detail": "Security compliance concerns in financial services"},
            "decision_risk": {"score": 70, "detail": "No executive sponsor, buying committee not mapped"},
        },
    },
    "Metro Healthcare": {
        "deal_id": "OPP-004", "value": 440000, "stage": "Proposal", "owner": "Mike Chen",
        "factors": {
            "champion_risk": {"score": 20, "detail": "VP Digital actively championing internally"},
            "budget_risk": {"score": 65, "detail": "Budget on hold pending board approval next month"},
            "timeline_risk": {"score": 50, "detail": "22 days in Proposal, 1.4x benchmark"},
            "competitive_risk": {"score": 30, "detail": "Nextera struggling with HIPAA requirements"},
            "technical_risk": {"score": 35, "detail": "HIPAA compliance validated, minor integration work"},
            "decision_risk": {"score": 40, "detail": "Decision maker identified and engaged"},
        },
    },
    "Pacific Telecom": {
        "deal_id": "OPP-013", "value": 780000, "stage": "Negotiation", "owner": "Lisa Torres",
        "factors": {
            "champion_risk": {"score": 10, "detail": "SVP Ops strong advocate, weekly check-ins"},
            "budget_risk": {"score": 20, "detail": "Budget approved, PO in procurement queue"},
            "timeline_risk": {"score": 35, "detail": "14 days in Negotiation, 1.2x benchmark"},
            "competitive_risk": {"score": 15, "detail": "CloudFirst eliminated in technical evaluation"},
            "technical_risk": {"score": 10, "detail": "Full technical sign-off obtained"},
            "decision_risk": {"score": 25, "detail": "Procurement process standard, no blockers"},
        },
    },
    "Pinnacle Logistics": {
        "deal_id": "OPP-005", "value": 360000, "stage": "Qualification", "owner": "James Park",
        "factors": {
            "champion_risk": {"score": 80, "detail": "IT Director silent, no internal advocate found"},
            "budget_risk": {"score": 70, "detail": "No budget discussion, unclear funding source"},
            "timeline_risk": {"score": 60, "detail": "20 days in Qualification, 1.4x benchmark"},
            "competitive_risk": {"score": 40, "detail": "No known competitors, but early stage"},
            "technical_risk": {"score": 50, "detail": "Requirements not fully scoped"},
            "decision_risk": {"score": 85, "detail": "No champion, no exec sponsor, single contact only"},
        },
    },
}

_RISK_HISTORY = {
    "TechCorp Industries": [52, 55, 60, 64, 68, 72],
    "Global Manufacturing": [30, 32, 35, 38, 42, 44],
    "Apex Financial": [40, 48, 55, 60, 65, 70],
    "Metro Healthcare": [35, 33, 36, 38, 40, 42],
    "Pacific Telecom": [28, 25, 22, 20, 18, 16],
    "Pinnacle Logistics": [50, 55, 58, 62, 65, 68],
}

_MITIGATION_PLAYBOOKS = {
    "champion_risk": {
        "high": [
            "Immediately identify 3 alternative champion candidates in org chart",
            "Multi-thread outreach via LinkedIn, email, and mutual connections",
            "Offer executive briefing or value workshop to create new relationships",
            "Escalate to your VP for peer-level executive outreach",
        ],
        "medium": [
            "Schedule regular weekly touchpoints with current champion",
            "Identify backup champion as insurance",
            "Share exclusive industry insights to maintain engagement",
        ],
    },
    "budget_risk": {
        "high": [
            "Build CFO-ready business case with 3-year TCO and ROI",
            "Offer phased implementation to reduce upfront commitment",
            "Provide flexible payment terms or subscription model",
            "Connect champion with finance team for internal advocacy",
        ],
        "medium": [
            "Confirm budget cycle timing and approval process",
            "Share peer company ROI case studies",
            "Offer bridge pricing or pilot to maintain momentum",
        ],
    },
    "competitive_risk": {
        "high": [
            "Prepare head-to-head comparison with proof points",
            "Arrange customer reference calls in same vertical",
            "Offer differentiated proof-of-value engagement",
            "Accelerate timeline to reduce evaluation window",
        ],
        "medium": [
            "Monitor competitive activity through champion",
            "Reinforce key differentiators in all communications",
            "Share competitive battle card with internal stakeholders",
        ],
    },
    "decision_risk": {
        "high": [
            "Map complete buying committee and decision process",
            "Secure executive sponsor meeting within 5 business days",
            "Provide decision framework to champion for internal use",
            "Identify and address individual stakeholder concerns",
        ],
        "medium": [
            "Validate decision criteria and timeline with champion",
            "Ensure all decision makers have received value messaging",
            "Schedule group demo or workshop for buying committee",
        ],
    },
    "timeline_risk": {
        "high": [
            "Reset mutual action plan with new target dates",
            "Identify and address specific bottleneck causing delays",
            "Offer implementation accelerators or quick-start packages",
            "Escalate internally for resource prioritization",
        ],
        "medium": [
            "Review and update mutual action plan timeline",
            "Schedule weekly progress checkpoints",
            "Pre-stage next-step resources to remove friction",
        ],
    },
    "technical_risk": {
        "high": [
            "Schedule technical deep-dive with solutions architect",
            "Provide security and compliance documentation proactively",
            "Offer extended POC or pilot to address concerns",
            "Connect prospect technical team with engineering leadership",
        ],
        "medium": [
            "Share technical documentation and architecture overview",
            "Address open technical questions in writing",
            "Offer technical office hours for prospect IT team",
        ],
    },
}


# ===================================================================
# HELPERS
# ===================================================================

def _composite_risk(deal_name):
    """Calculate weighted composite risk score."""
    factors = _RISK_FACTORS.get(deal_name, {}).get("factors", {})
    weights = {
        "champion_risk": 0.25, "budget_risk": 0.15, "timeline_risk": 0.15,
        "competitive_risk": 0.20, "technical_risk": 0.10, "decision_risk": 0.15,
    }
    total = sum(factors.get(f, {}).get("score", 0) * w for f, w in weights.items())
    return round(total)


def _severity_label(score):
    """Classify risk severity."""
    if score >= 70:
        return "CRITICAL"
    if score >= 50:
        return "HIGH"
    if score >= 30:
        return "MODERATE"
    return "LOW"


# ===================================================================
# AGENT CLASS
# ===================================================================

class DealRiskAssessmentAgent(BasicAgent):
    """
    Assesses and manages deal risk across the pipeline.

    Operations:
        assess_risks     - multi-factor risk assessment per deal
        risk_matrix      - portfolio-level risk matrix
        mitigation_plan  - actionable mitigation steps per deal
        risk_trend       - risk score trends over time
    """

    def __init__(self):
        self.name = "DealRiskAssessmentAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["assess_risks", "risk_matrix", "mitigation_plan", "risk_trend"],
                        "description": "The analysis to perform",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "assess_risks")
        dispatch = {
            "assess_risks": self._assess_risks,
            "risk_matrix": self._risk_matrix,
            "mitigation_plan": self._mitigation_plan,
            "risk_trend": self._risk_trend,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"**Error:** Unknown operation '{op}'. Valid: {', '.join(dispatch.keys())}"
        return handler()

    # -- assess_risks (flagship: prefers LIVE tenant, falls back) -------
    def _assess_risks(self) -> str:
        live = _live_open_deals()
        if live:
            sections = []
            for d in sorted(live, key=lambda x: -x["crm_risk"]):
                severity = _severity_label(d["crm_risk"])
                schedule_detail = (f"{d['days_past_est_close']} days past estimated close"
                                   if d["days_past_est_close"] else "On schedule")
                if d["days_past_est_close"]:
                    timeline_score = min(95, 60 + min(35, d["days_past_est_close"] // 7 * 5))
                else:
                    timeline_score = 20
                factor_rows = (
                    f"| Timeline Risk | {timeline_score}/100 | {_severity_label(timeline_score)} | {schedule_detail} |\n"
                    f"| Close Probability | {100 - d['crm_probability']}/100 | {_severity_label(100 - d['crm_probability'])} | CRM close probability {d['crm_probability']}% |\n"
                    f"| Champion Risk | n/a | n/a | n/a — enrichment seam (wire contact intel) |\n"
                    f"| Budget Risk | n/a | n/a | n/a — enrichment seam |\n"
                    f"| Competitive Risk | n/a | n/a | n/a — enrichment seam (wire Crayon/Klue) |\n"
                    f"| Decision Risk | n/a | n/a | n/a — enrichment seam |\n"
                )
                sections.append(
                    f"**{d['name']} -- ${d['value']:,} ({d['stage']})**\n"
                    f"CRM-Visible Risk: **{d['crm_risk']}/100 [{severity}]** | Owner: {d['owner']}\n\n"
                    f"| Factor | Score | Level | Detail |\n"
                    f"|--------|-------|-------|--------|\n"
                    f"{factor_rows}"
                )
            total_value = sum(d["value"] for d in live)
            critical_value = sum(d["value"] for d in live if d["crm_risk"] >= 70)
            return (
                f"**Deal Risk Assessment -- {len(live)} LIVE Open Deals** "
                f"(Static Dynamics 365 tenant)\n\n"
                f"Live pipeline: ${total_value:,} | Critical risk exposure: ${critical_value:,}\n\n"
                + "\n---\n\n".join(sections)
                + f"\n\nComposite uses only CRM-visible signals; the remaining "
                f"factors stay n/a until you wire real risk signals at the "
                f"LIVE DATA SEAM.\n\n"
                f"Source: [Live Dynamics 365 opportunities]\n"
                f"Agents: RiskScoringEngine"
            )
        sections = []
        for deal_name in sorted(_RISK_FACTORS.keys(), key=lambda d: -_composite_risk(d)):
            deal = _RISK_FACTORS[deal_name]
            composite = _composite_risk(deal_name)
            severity = _severity_label(composite)

            factor_rows = ""
            for fname, fdata in sorted(deal["factors"].items(), key=lambda x: -x[1]["score"]):
                label = fname.replace("_", " ").title()
                fsev = _severity_label(fdata["score"])
                factor_rows += f"| {label} | {fdata['score']}/100 | {fsev} | {fdata['detail']} |\n"

            sections.append(
                f"**{deal_name} -- ${deal['value']:,} ({deal['stage']})**\n"
                f"Composite Risk: **{composite}/100 [{severity}]** | Owner: {deal['owner']}\n\n"
                f"| Factor | Score | Level | Detail |\n"
                f"|--------|-------|-------|--------|\n"
                f"{factor_rows}"
            )

        total_value = sum(d["value"] for d in _RISK_FACTORS.values())
        critical_value = sum(d["value"] for dn, d in _RISK_FACTORS.items() if _composite_risk(dn) >= 70)

        return (
            f"**Deal Risk Assessment -- {len(_RISK_FACTORS)} Deals**\n\n"
            f"Total pipeline: ${total_value:,} | Critical risk exposure: ${critical_value:,}\n\n"
            + "\n---\n\n".join(sections)
            + f"\n\nSource: [CRM + Activity Analytics + Gong Signals]\n"
            f"Agents: RiskScoringEngine, DealAnalyticsAgent"
        )

    # -- risk_matrix ---------------------------------------------------
    def _risk_matrix(self) -> str:
        deals_by_quadrant = {"high_value_high_risk": [], "high_value_low_risk": [],
                             "low_value_high_risk": [], "low_value_low_risk": []}
        value_threshold = 500000
        risk_threshold = 50

        for deal_name, deal in _RISK_FACTORS.items():
            composite = _composite_risk(deal_name)
            high_val = deal["value"] >= value_threshold
            high_risk = composite >= risk_threshold

            if high_val and high_risk:
                deals_by_quadrant["high_value_high_risk"].append((deal_name, deal, composite))
            elif high_val:
                deals_by_quadrant["high_value_low_risk"].append((deal_name, deal, composite))
            elif high_risk:
                deals_by_quadrant["low_value_high_risk"].append((deal_name, deal, composite))
            else:
                deals_by_quadrant["low_value_low_risk"].append((deal_name, deal, composite))

        def format_quadrant(items):
            if not items:
                return "  None\n"
            return "".join(f"  - {n}: ${d['value']:,} (risk: {r}/100)\n" for n, d, r in items)

        return (
            f"**Risk Matrix -- Pipeline Portfolio View**\n\n"
            f"Value threshold: ${value_threshold:,} | Risk threshold: {risk_threshold}/100\n\n"
            f"**Quadrant 1: High Value + High Risk (IMMEDIATE ACTION)**\n"
            f"{format_quadrant(deals_by_quadrant['high_value_high_risk'])}\n"
            f"**Quadrant 2: High Value + Low Risk (PROTECT & ACCELERATE)**\n"
            f"{format_quadrant(deals_by_quadrant['high_value_low_risk'])}\n"
            f"**Quadrant 3: Low Value + High Risk (EVALUATE ROI OF EFFORT)**\n"
            f"{format_quadrant(deals_by_quadrant['low_value_high_risk'])}\n"
            f"**Quadrant 4: Low Value + Low Risk (MONITOR)**\n"
            f"{format_quadrant(deals_by_quadrant['low_value_low_risk'])}\n"
            f"**Recommendation:** Focus 70% of leadership attention on Quadrant 1 deals. "
            f"Quadrant 2 deals need acceleration, not intervention.\n\n"
            f"Source: [Risk Scoring + Pipeline Data]\n"
            f"Agents: PortfolioRiskAgent"
        )

    # -- mitigation_plan -----------------------------------------------
    def _mitigation_plan(self) -> str:
        sections = []
        for deal_name in sorted(_RISK_FACTORS.keys(), key=lambda d: -_composite_risk(d)):
            deal = _RISK_FACTORS[deal_name]
            composite = _composite_risk(deal_name)
            if composite < 40:
                continue

            top_risks = sorted(deal["factors"].items(), key=lambda x: -x[1]["score"])[:3]
            risk_plans = []
            for fname, fdata in top_risks:
                level = "high" if fdata["score"] >= 60 else "medium"
                playbook = _MITIGATION_PLAYBOOKS.get(fname, {}).get(level, [])
                if playbook:
                    steps = "\n".join(f"    {i}. {s}" for i, s in enumerate(playbook, 1))
                    label = fname.replace("_", " ").title()
                    risk_plans.append(f"  **{label}** (Score: {fdata['score']}):\n{steps}")

            sections.append(
                f"**{deal_name} -- ${deal['value']:,} (Risk: {composite}/100)**\n"
                f"Owner: {deal['owner']} | Stage: {deal['stage']}\n\n"
                + "\n\n".join(risk_plans)
            )

        return (
            f"**Mitigation Plans -- High-Risk Deals**\n\n"
            f"Plans generated for deals with composite risk >= 40.\n\n"
            + "\n\n---\n\n".join(sections)
            + f"\n\n**Execution Timeline:** All critical mitigations should begin within 48 hours. "
            f"Review progress in weekly pipeline meeting.\n\n"
            f"Source: [Risk Playbook + Best Practices]\n"
            f"Agents: MitigationPlannerAgent"
        )

    # -- risk_trend ----------------------------------------------------
    def _risk_trend(self) -> str:
        sections = []
        for deal_name in sorted(_RISK_FACTORS.keys(), key=lambda d: -_RISK_FACTORS[d]["value"]):
            history = _RISK_HISTORY.get(deal_name, [])
            if not history:
                continue
            current = history[-1]
            start = history[0]
            delta = current - start
            direction = "WORSENING" if delta > 5 else ("IMPROVING" if delta < -5 else "STABLE")

            trend_line = " -> ".join(f"{s}" for s in history)

            sections.append(
                f"**{deal_name} -- ${_RISK_FACTORS[deal_name]['value']:,}**\n"
                f"Direction: {direction} | Current: {current}/100 | 6-week change: {delta:+d}\n"
                f"Trend: {trend_line}\n"
            )

        worsening = sum(1 for h in _RISK_HISTORY.values() if h and h[-1] - h[0] > 5)
        improving = sum(1 for h in _RISK_HISTORY.values() if h and h[-1] - h[0] < -5)

        return (
            f"**Risk Trend Analysis -- 6-Week View**\n\n"
            f"Worsening: {worsening} | Improving: {improving} | "
            f"Stable: {len(_RISK_HISTORY) - worsening - improving}\n\n"
            + "\n---\n\n".join(sections)
            + f"\n\n**Alert:** Deals with worsening risk trends require immediate pipeline review.\n\n"
            f"Source: [Historical Risk Scores]\n"
            f"Agents: RiskTrendEngine"
        )


if __name__ == "__main__":
    agent = DealRiskAssessmentAgent()
    print("=" * 70)
    print("LIVE TENANT RISK ASSESSMENT (fetched over HTTP; embedded demo offline)")
    print(agent.perform(operation="assess_risks"))
    print()
    print("=" * 70)
    print("EMBEDDED DEMO (works offline, simulated)")
    print(agent.perform(operation="risk_matrix"))
    print()
    print("=" * 70)
    print(agent.perform(operation="risk_trend"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/6276a7jRrYm+ipC9o+yi05zEEdfnL6XlEiRFGdK4tBu2BzFeaY4VNe7d2jvTNtVfXCAC7SQuXOLilixxm99Cxn6x5dgnrJ2+PLLF1biWPv25acvcTJGQ95Nedu8H49j8v5ziJOgOgz5WB7Soa0PVf5KDm3XtcM0N/mUgxV5cwgOY17PVTAl8eG8NUGdR+PhSBKHKWmCZvrpsORTdqiDacijZPzp0FVBA/4Jmhj8PSR1mMQx2NqmaZU3CTizbg9pUFVhEJU/A92SNai7Khm//PI//udPX3Lw+5df/vElqoIRPPpyBipaQMNPneukmdgn+AH2gWOeYEG3AWMb8L5LhrQdavAoTtLDt3c/jEmV/nT4+9/LJRie44+Hr//9ME7DL782h2+vtjv8x+Hz05+fyfTDr19asDd4u+rXLz8dfv0SfJz829tN469ffvxzZ5yPXTBFGdj/jz+fvl//vumXw1uNn3/769Of/n3L++lvH25c/9zxl4f/x4YahOj5oehvb5//uenfPvjPT5qGpIn/7aCPZ39Z/s8/f81APKtkALZ+N/vDW233F4fk6aFpp+9Lf/nXY4dkmofmkP765e9/54ehHX75+98P96Zs2qU5/OHyw9/+0Xb//NvPh0dQ5fEvh3/87afD334u2rz54Y9zy2Qbf/jxx3/++uXPE75J/3b0Dz9++SdIpQZEeo7eYt+Z9N/+20HNo6Ed23Q62FE7T4dhbqa8Tn5tfm1uWQ6yfTxMWQKEvZJhzMMq+bauG9oi+RAE0vjw+/8X5GEwTl+DdyaOX6s8HIJhg9/V9OnH4I9k/f3nww1IbIf8mTeg2CzWMH5tPja+T+uGZEyGFyiPcJuSryBjv75/eZfd7/+ZuN8+dv7cbb9/1BdY9tbXOkmHKOjGuUp+ftviZEnzTfPoXYJrEs1AaNVGQIM0r95VCg5uK1Du09vuscyrCgR2AEa2w/YhG/jml7ew33//HRib/dp8Ftrx8IkkIwwW/KHO4etXYAoo8Gc2/dokUdaCQP7zb4f/dfivdn0If59hAAu/eR5oKNu6dgD1OL8tfkPQOCVB/OH5f/zzm0OBmAZkI4hTnr5x6r0ZwEuZxN+9a4vsV4wgD2ECvAo8Wr9hLW+eh3z6+SClhz/0BYe+PxoB0GXtOAGA6kAVJE20AakBMOcPT76TewRpOqbbT4d5TD5O/R0E/0PF+rcILP/9oJ6Mw9S2FfjxVvNjEdjcNjlw/x+x/3wOhAx/Gw/cdxE/H7R37h26YAi6bAi+nZEGn3Fph8P37UB4cGiS5dfmjZjJ21UfBfTpHrAIeCb6FtKv75gforauQWDH72d/rPlA9VsLsjkZfm3Gb0keDO9QRC1QZTs85zwOmij5f76l1Ji1cxV/+A9o+pb0LQrxt6h85OAbtw9v4D78idyHD+g+/DpjCIoD9YHB3buvHLZ2/jizTkBDefutnoE1n8kMDgW5Cp5UU/710xF/9q2fDuGcV8CmdwTTtsrbz3b2Zzf6buX4a/MnLP61R00D6EPj57YP/APl0IIwgyo5VCDvABJkefdRSMB9wP2/Nh9rv+fVBH4DrgWrxyrvOrDgQ21Rdw43UbIPN141FPbGHxzdutpvxEJ/PujAjyCf384L2/UtpJuravzswCdL/bcu/A7EZ22It5vx2azB3m/w96zaEPTT7SN9QRTsdyZE/1mvPvzAvgN9UALQiPU0BS76JsPe3uk3fo/NuDVA/ltKHEzBTwDWD9GQgKKY8qACjlvaAfjsQ4+g2ZYsGZIfv+N9Nk3d+AsMl228fV1+fgJ2MIc/5y08fuj1Nf6m11egFxx0Ofw+An4xP2PwNwm3Yfvljwb+R2v4j/+jFX/X9u3GPzHy8JG3n778JhDIaD6SBgRpBg07AIZ+4ao5OYjJANLB/qydd7Z/E2m8ewCwFoSjBrX54b4/nAXawXMI6jc9GN/ZGX96AsTt6yv/7Btj/mzex/0QVS0oYrAjDMK8yqftAH2TMkZZEs/vtSBvfvz5/RQD9d+Cqp7e/v1/D/y7/gBAA9B6E6bx8KZM7/J4G/wHsfogVFWwgbiGSdUu38T/8Jsl2dffBPZ00y37AB9+U6WbdGFvkq79BjLS43T9av+rDz/Ks/lAoAiAT/aumk8HfpK3DyWPPx/UoPzIfFC3wNHB9LFbkR784cze2IPNs+qnLm92MX2TceZZ5VMn1rZ521Z57fbbe/1vd0t5WwUy6aCfQTJ8HbOgA5aBYuxA5wdp+z7om5iPMvgjt9vh+dMbFj96xhtGkvVdOJ8Bsd9FDJIoSmBxDu2unX58L/5DEECBKDn8liaAVfwWtVX1CX8//PhJad+HHt7sJKryd8P6QNY4j94QCPT7SwUCgPqjnj+wtkmS+INOxG300caSj2b9WwMyGhCbPfntnZ2/vVPyh8/Qg9cpA0QYnP8GtRiQq5/ekN2BKnyn4SdYxUkEEgxk7AcEvSEzAWgUZe8jvqdVEvxZxwvA/8OlBQkEf5rzse97ck7vuv1AK93grY/M+ACov5YZaOF/4aDg3b+Ry++ff9JJsPmTSv/yF0r3w5D0M1Ak/vHN2gHmgD7z5ZcGAN5PX0AYk/+S5b87YZ0A0BrfUwGoIyD2jYnvd38c8X7zryPOO1QArattfHO69juavMeNZgYzwv/4FywBj/9iJHj3b0Z+//zDyC9gSpm27q024JegOL/8E5DN7za+Rf+p159L2/DNIN+09N3yPgeVf3wBlgVv+Ptm2zeSCZYDQvl1fLdbGP0ZeR8fDJ+0CXz2/4N+ftsJ8hVQIbCVxlIqOGLokQpAfkT0kSJRmg5IKiLTBCGRlAkxkknjEKcTMkixCKGjCEOOQQTAOjkegbwRpFGU/PZmE/lbmzANCSwK0RSh6ISh8IRAETKJGZQMiTROGJpkwiNDJH9uLXPgxE8TP016++8PJvx2xTdL//ElJHGwUsRHif18nWAGjcmjFM6+Cw1kzMY3f7jnQdfviD7S/aWqszB3zF4a49u4to+euWtlhhznvWLKCDxQ7sZ4h/AbpaS6eSbX3KuwOwEN124s4yPLuueZgFh2zNeBRG7BaygQfIRygY62Yo42m7de9guGqSMMFxQnSHOkHBGydCRAwE9qR0zKZdvMO73fOJqmHHRiZWltiplgcMprJvnCl64khaxDKMernVC0n/P3UJYNmyk5SJl9lG9yo6hG7qk+r2Vyec1yTN1vw7Lw3HNfziMV8Xcbi6jGMR5XKSvZR7ZdMcNbu5yZHki47sIorQvOasqpATkUHsen3OUOzclQFEnUZUzoSQCHXF3ag0/WRURI0ZtM+LUXQ5GCIqLFysXj0JxXdD1xmnV+Wtt9u9Ywq5iPvHy1MPcSxq7IYcMK8+camFz3nBc8wFSLvw3wjQ1cL5MFlewU7Jz5UC9qVPhS6PtYcEaX58JCFE3uc40X0ZC8RuLwQLjVPGUTo7E5X8eYpD6A/cImSEXGj3CjxmrhPj32ZnGRTgmh9MwFHildwpBHEc7J06Y/8z5+cvRM1d5ajuSL3WW55N34GBekSA0ygxIVudkbQ7pFBpLjFgwTadeoGkRxkpxHZBmpSdwHSl8G9ip02HqXL6Y+07xNSn5/vpfOfcfxRSZD8UFcSpuct6hZ11MZXVO2dRM2VKVclkiVMh9oNcJVcj0XPEdblSQN1XObpEk6TtL1mWIEZTqq0uqRZVk6eDhPd0t19byfPE2iHuOLqQn66sivy8Sx5ygyPKSMw3kJdzixOzfvPPWm35S200znrJ0nfNZoS0RUa5NuC+RDeQGVr5Io3Zvq8nJJ4uw9sU8aSxLpeplz4hLPd1pQSIZj0VfHwck1OWl04nb0FS5i6lggCbddxZCHjBWJjR7S9jZOue3MuASkrwUdPzL2Qk+JJNVdo+a6T7BKFhryakQnO1YpUsp2aDd2rTftWrnfqGbCoL583Zq+aLICS6C4FyrE2hALEJHmuE8WAC0tS/cnTR3pqAgaAlJTRUVb3eGBteUZi4ttF9CnnV0QKxntUJPI09JtCe3Q3u3xwm/wWulGIV1LGZLiyvS53C4kORaVZpdCxFfGa2l7iCaqOS7RD1zKtEZr/NORiPQyPFqCGD9vFRmcdPqEp88k0iRL2naL8Vee1tft4hmgtC0Mby/607dMvsLHo8bJuamvwok28eUUASabGJDtOaKgnrXsmcxGk1xCQ1jzmJHvVHUvFfc8paZmSxRh5lF/PzdPGR4bPHPt55lUWL8IWMKOu+Cu0/RLBJrUGobyV7yARCFjzVtQZwsSMuUtP2t3wixoazpeFN2BJfk1O21UYi1CoWXaznCj73OwVpiVB4/WMhRXkLWlRkeHMTZHwxJy5ac2v52TZYb1pSRq0YYk3zeReAbU4yUf78qavYYs4fhBoZSJ4RnjtTaZWnOkUZOnFk0qD0vhiwtgSFMSrGbRmdKyfW37lbndEiRXMRXz8xSHz4u46hIDH8OiR9iOc1iPx9hCrJGSXY7ofIJftDiproPOMI+EKcyqXUVB8onRiLOhWgQFGd0MEwsjo88CEa1Fnp6PRF91TjnuZ8+5BicidB1BiGvF8sd1Cg0XCx8BWaDWU6MgLA3YDTHRXHuxd8cSt/WYe1gQRgGx3x6x/bqwIjkc3avHIS8rK50W18hzC0uXcfC2dBPa+tKuA0tf7phbllRNJ1vg3UzM4ciE9bDNOWmoM3ZOBDFPT8k4Ymq26jEY5KO0zfp2mknvEned+hyLZto7jCEWX8YbprhdkO01+C/oUst6zL06dsRwd7w7w2QgWL2qdHd1cyySQ5sbnHnyWDFYi0vpK5dnu6xr/0xe1RB0mn9xjM7gorY8V5lXl0EgX9R1v+KdU8X+kl8Mz7RinN2bmUxzk8FOjXzmj4UHNXjkDvydEoYIM8dWrjMtuGzTiBesGo6pQzHnYVWJMRHL+NHcjDHZt3hxWKFZo0ISs3XRe+3cCtP5yfvmyMej6xUam+h0pZ7SnO1yud5ZRQo8MwU4y3kbRlEBz/CFFk8Cd7nOCGJKycWEZFZ5ZJjaJbx+4hFLn4Silte6jz2+XRnFZDLkscoeLz/Pj6olbnI5L6lFXkK9KvrdvU5d2kKEBueCSYsGiicM0yAiIc4cwpCRgpOjiGir74Wj88Ch+RXbJdeGLSbzdCq+EtVI4yvIVH1uNPupwVCriaQnl8lrcmiF3SNpEyqDZaQHBY8FXWnCsXVgdhRNVRREV23LwpM8+hnbuUaJzdpIqxHSAh+EPi8MNeHh0C3nTYwb4Fpd7w8iXeJKwaW+u165c9X5z8Q3cly3SEJ93amioJSbbeDDPLy0CNWQ1zNa0wBe2qjy0IJAFSas7Sk5HZ3Ucy/n/XXUk008V1V4u4u7iuoZql0YxtbKUT1eZmezsTHARgwlN2U8jgg9st3dx/MXAUG2SVxvtxcxlqR2knKM6JRKwAVM7zR11kWmm49XFntecopnDdyzTmXW3esS9sKZa9T3gF+Y7Ml+vXqnRMW0EUspExi4fQgCfGpbge6EK8MZa2fOJHJq04Kq6tDHzae+vHI6RoQxgDHtYUD87ikkeW7GrOMt3eNf52VbqvSRF63jCPE+iNCYn7JIuvd5B9WAiemihy40vLyeT6Q2JDC140whJTxqHisTeZ3HtATG25GnuN7zcnwme0e6Z7bptJbirrdnofkseZejG3V31nak2CxR2Gvjj6Em2z4PLZyizYSbHc2N650nwuPBXbwRwrkLnFswwqT8eGl7TCXUXFaTx3snAvZceke8i7oUr8sYDCRpy8hqTWKWlCsmX4kLSkuDcmy3XHXqK+Jec2O37hm2u14/6aN02XRlO0MUxHL6iSBKWSW0+9SeueOxtlmeq3Riymv6ZD3U6BJyd2aITS+V4kwu7lZZiNx9iPCkAfW3C4bt21i9KdmtDi/3E3fLJffMKJC+SfaiP554I+Qbp66X6JnT+YOwjh6kPaF6QE3SUmO5upTPa37GGzYsbV4oIAu0QF7lNii/WzM+Ce5zaTgwmRxl+3hKLrdbBQgmIfjrnagg02zLXZOio0xC1nL083OkEoJ6KURasV/n+/Ha3rBHp+PJI0YhAelEhN3PF/VVPjBWMiKvQL2NXUa4iCaCvT98mej3Dj+uuTOlk3XyOA+BcTEuwmPkhnzH1rNUGQzZtHz/irBYpDjsGqaXvn8kGZRKkIdamKkmyWkvm2vUO4+ahV6SGbEm4x5vqTub3krfRScLoYLwaC66x0/NnKYwSrgacOHdFrdWYSA8rMMkHysMdIQbefLLtT/1tyBgAZuj2bxGlTo3lYrinqE6Jax/v3A+2j8ER356OgMa7pxxxquyPVIOyltN3q7+icV8DumEIh+XaHBwlLJ7NjdWPLjhzrEf7vKxWeSrOXnD1icXp3sGXXsJxWsbChDbr5Z/DczA3R33Yt0c9ygUj5VogtI7n3pSlLLKGZlqjjAUzWD5RLVF41CbjfgnzdMS1BnUUa0W8+VPj2ZB+93GUXv39S6PEZkNKP5ai+q6xScLGyimeGoqnDIjrCd1uuh3WMTz/TjCjM3wixnYski80o3kZwLOt1nEyyau1svpyAcJd1ruUf+6jo/EmZYoFpNjjBTH4nFiZs+Y4awjPPkWPXuVE4rmWEdt6p/NfnYFaFUwJdC3swWnDrHgXSIkkWVHC0vX48nLslcRyzBeJTPE8LbZK3fzFUPKLQu4O2+6DRLe2vNLwrf8BBrxFXfWoVJu0Y0+XwpaCCoyJbCFr9mFnWslyE47HGf7azPNmjn6VrbxeF73i84oOdzg8qm5PVVPUUI+rdNXTmUcfsZCjBEbIWEFj/KuMJ5uZkFdFTwbQpfnOKKOpIhgdHlDqtIyqdB6dAutn4JzCgsuzmEuLuBaoVUY1F1Y6pZhV9/2OvZ1cjxxukigUz44uRjwtRjEs6aOXUs2kHUb+2U5Fdzj1Nk+4tNF9Wz42TpuF/ba5YtlifD9Re7H5sSaxDEw+SKpebMgT8brJTANnMFID61pfCQlvhHrVbn7mXBxiPoKPZ4pgqo929kmpckn2SKaxdEBi28u18dQmsvlzPinJ5Gg95JLVUcWaAxoLz+FG044Cx7PqqSdEiiRTPbBTShcLhXLejRgfnGqmLpIOA/62U6duQRPf3tYF6igjcfu1xymVEN+AwqKZhrzWGZtgA5ZuXLcvJNxu7dcZghx9fIwvpexVRXZkn2hja3qIJEpHQTQehn3J8dSpx23nNhS69PDzuMzeXQ4M0dk4kJgqKTgFPdK5qodEtOlTaqggsXQJtjicD1/KQtZog/xOWQ+zwdwrdz8ORL41AgznTd858bOHL+C+t6zvOxXqq3U2E2Ml+GWiPuMAySTxGXebNYrYtrmycV+CNlVZ+Sr/TiRIPlkBHezh18RTMVUS8dmo+1ievv2TffaxtHfbakbsaeUX5MsKg2T79KXMmcAGwZnQzgBl3wTzUThSu9HscYUv1oNFsHV5ggS2lLGneJVwVRdafawtRXlWy4eb2FblqAmJiIqnbNkRSyxvyYeAZ28PI13cRTHLcKWJPRVT+RCATfOiwu1D8pPVvaaNqs8kafHqQ+lK7xf5af5tKYbEnFE5KTKM0en5/kaciE51AJ65RAKgFmaqfx55qZcfIYyda5Od4WXoP0+A74vLfyFsRdrr+9kY/TYSUkCEcGn5AYVGq/Iy75LZyHWuyfn4i46npFsM5Uinyz52h0zp4LTtcn5s+DckG5G+ARFUdXQ+vmkLU0CCn8qDWvgMrlBOltrDMYtGwKGz7UL0SrlP1xjub3Oq7eWvgHS3Ke2tQ8oZaD3i8TmTIE9+yR8Gpg23jnFZTdJw+cZuUKdIrxca8+hJV+pDL5DiEA0MDn7r/nqiMaUkQO1t9lzHmeIYzE0Tv3TygjphV0f/UsyBlDxsuOZGHzCrWPPCXdOff/v2pZPGnVPYlIuAiIeh/5Is8gThoubv88cAAJIuEbZQzVUf98d/Uz1YzFyJDTsCmk/DBg6lpTwlCG91Z/FFj3G61OpJ+vFNAMP47OERDKs0v10eYSPUtubqkgSx2b153midFlwSHdz5GY1qEd2Y8IxxOS7BdWUB7tCeSWWWbk9YYIj2LOOy+RdsWhu1NxBe1TLg1wqWuQU4sEoPiVQ/h3hyCD2Kf5MJEZJlYjKGGOf32ki1XoC2EpyhMpDDUuKLDKnR3w8uTc0GGDhltcW+bpn8IB2UnJljtlCucRFMO6cgdSjSIoXaccTEYWmHHSYHAHD9lIWOBwZM+O2R0pqMxE6p8GOnMyoqCdn4IZXaOXnm2T0/unUIMYRjhMXY2xOiHmnG+wrZTGvAKqZtNf65tIOHqwgYZkvSmPu1N4V15OrJwJStGyQdzitOdhaQRLLmp4ylhXan8/p0/cLAhcq2dtq5gSo/TChaFG5cx7s+dXwq3N4bPwaZ5x1JZ5O2rnj9dHJuwqCzXZ1cwpsvT5l5im+4qeGY1nX4F4hzlXIKtG9QDsn0IJGwp+v7GaYBC/bcZ33YnOaTGi9H+98g+DHZTnfqprOfMvCyDjeoqvpZ6UgqfeJG+VMr2CBms5jebe2+jWYTtz6tqrca1ecvOsWGV1+zy8TpwXkUO4I2l1F+hEOUuBINyWREGlOZqwucXzraTBWpetgSje88cqmZy83kOl2dduDTMOtiAok99qNUl4kl57UAUTp44TeAgU/JmftxZ/kliG4i7mI1mSpNky3KmaRUIYvKhgsb/nUwUSe5fhchSlh8GkF+vzdF7Q4558uD2dxbpLotR+XmU6OuMiudHJ3j3MXYPyM4fMZ0f1Hnxc5s917gj9jONLDJ13w1brXU5Q85/aZtSlHUCeeiVXJ0OmuGiNy2dwoxPX7ZPNmTdio9oBqNxd1jEU5PbnIjXa2nJkd+Ct5vNhzR0QSppuKHNknWWwCowoSMDtWRlaKmeKoOoa6gtwIK1NU3iQhpReiaI2UFKe9ABqxEf+8jKMmI4p8c+/cyy5ygk2jjDX3TkXLgc+2XWUem5+R5wsjHdW2lXwtKBbRrY/sMWooLtyX3FATDCl00K+vl3hdWhiw59z16NO0+RBlebZ+usQ0UwJD+B2yeuF2Gth6v4bl+ZbNFTJV/tHl2xd+lgssV1/Kg23clk3a4LVWerJn/eXaMrBX6fdzkOsxqaK40QdXcRn0zYyTbVMHccyKsyjPCqXQhNMlXWi7rxLvQR8oH4yKuEL1XGroiaPO3O1ZNSGB4auaJg3sw7FPmFF6e2VY7GWc0UuHCFgDKrOTEO1S9F19R4i+CYijqMnrcSBQXYhHXfWkmmBUcenDN1HNmxvjC2oL3Zm9ytVQe22hRCC9zlzte3Y6x3mCDJBzmbWrv52cNenN5wJGseWIB9MVfbnjCCmRQXtQtV8v8uRA2YyWHVbc8bHybTA3SQs27w1+HZOr8NCJpHldLgZ3Hm4qdrFI7NrHzwXDnnpZek/WJWmaKjW6jCT1Ik69R+xDAtkyY3pPP3f7Lue4J8MFEJ3quUULExP17QINt0esssYDV1HTO2Hxe8QOWv/B9lYSIwYx7SWLj1Zc42009i5vt0fdZAb2iWK9i8AXYRs5BNPVMkKO+xrg95wKlLqU/BbHGcFw8vGqN1zJb0IzOLRZ48iGX7FbvPOlkrrtcCpRLJaxoUbyGQ2saQ8kS+tXt125K/ysLpJOqKd2ygn8Blqiepn7cuqNjcdElXEoT+IAmXuMWe51Z2F19WN1ubjxNoERCpLyXd4CYQk2OxeNAS+sinhc2e6R+IxZ3V8GpD4NHZYupyAqAGuf0ONujC/egENdgWd3SYiHFp0F5dHCwlk7PneOe9CJJShRglEwK7PlM0pS1969GWeUMshnbN8yJ4avYjDWcsxlSezrXIi/CO6Bk4HP8fC9ehzv5d2wELfryyCZV1Rv5HuRTYhOLPqAdWMaYsdrv5yDEPTOlybciLt4PZamTvPiI5ACRHZ5/nyEE0R/ZesduZKo6Zdy6IVeN0XglWnxcZeEfrEwI+jYgLCuaM7J0dkin4Hdm17Rp1YdxbMcLIvPKpxhTPrJL9o2L7A1GFqqPkOabkEX4dg9bjd9wGnRRxIGVJpDQX2QHjPGwETU90TNPhrcFiPHa5f2NbTtTw92YsayNHttE30/vk5U7lVnkrMQs410Ur81EZWBgY1Pu6iVFwXao72PntDpNkb3Xae8MxUI/UNF1orGnXjdAHOx1mI0bPx2A05MDWjrTcgXjOuQN6Mr5YJE7oF59nPnFBdqYXAuLM+Va7yCSzhOQkSjLa7yS6098F2RIZvHQs+96B5OW/Szi3ltVNMU43TxOEo3NSysfGfs4DLWCoHZEsMS/YJ2ingdkmgbw6ZmyDyotBCt10atHmtNp+uDNgv/kTRxHNxTqRxZG7M0sdoIfhwFmUnPNQW9nGYRpEA6Z/caDfvjXS6mbVZ8Obidr88r6c2VrFzsbHfPhDewzBRYQT6srrMJ7XIPXhImgYGCJh9msdN+sq0KGRr6FfJx2uhxohOJfnO37SVHD9t/FBe3ETUlnwPNz9PCSK5ySyxUpl/KdpVTzdVnLUgQ0kWV8AINOCloSIrfqJiqXGlrCT5PxZsrrHWQL5eQ8MTUyT1cx9pydyC3uD9TbYeMfFn6s/Cs+jpLksejc0kHJR8y5RaB4LWFyRvkcIafe89P/LVxRfOEufdMGiN2Z5GJvWQOGuhDnu/qcMEmuGzNJqYAEl7JUemOHGBqiZJZ93hh2ZlIYt5WmBuHYat5fSWi7JJL3/jqmXmZjEHGgZIqgEmA3ox0SbjeCWQh2iqPmV1tlJe6UzorMb4xzJtUdilorJJnJBn1qE68y4MZfiNyOU4lyjj2N/GR5KdNxVPTUSQNu+xkJD4ltjgSVDorIY5k7qSgMQGlD3SkxjyKQq2VQXFz+hEVHbRbSHOtO/fEsgEPvZKX21n3NYTwV8dRgbvmfj8SFRJL4dnpu3WDb0Z9R+M1zbFSRF44fOcx2ZnQKXuRMfYS9+Nq+amuj7mqDMcUNU03oNGS6ggkpj2VnBX21AQhtZ7FY4ymwTVisoFnCs0Zstt1T1c1K6M0w+kazl/Pnfa8WHdnbq2SofJHRAwqNdN8iuGrbLAgf3+gZlgSiMKaGbo/jeh+qx6sSngaYaCumznkYLWMWVzTBDFfR6Zcc4/ojvyD0vIKhhraTDFLpAzBTkvnRVWEIGAt7S2rVkJkKT4YZtgM6Tj6XDHBzMMgtuu2kx36atxE46ZLP9x1IVxyBx3XLCFmyS6CCGWLOzPAVozgw2so5ikj+CdF7M3zqdXTKySJ+CwTLURamjbJ5HxXT1pTGFEiPl6JIWaXLmy1/QK6cDlHa+rer+dMofkaBPJ2fhGvZw8TS0Lv8eTJDblMGiREDpFiITZB0x4jrxxuMzwVcxUg6eNZBcLdPItYvZX1HMHaKe7dqGAUQbwgcBdMzissu7spjCNNQQMlsWUIY1PuLkuIvFjKJxE2HvtnclcCwN28rEYjrh/OzHwkt4ZAzPhcXFc3S9UHzQaRRZf3QDuv9wwJZMLGGRspTjkyZHDZhRx0unNu2o/RBTCR3R8uPD4GYp3K4rk79R4losz+pJFEf9hG4OixvVFtVU+m4V8K2SyRBms2qJYC1PJt4QV5vdCg6C3HILuLylgLsjjKfFcpiEKjbfM+NO2VGuaj3l7ExFfuBT8qJkRssFL4U1jDWJuHBJITWsg9oL5h5dutduUJVyjsQchLcR/OWdCc7YGYrtM4K9KxgtK6KPySoYKEVKaKVQBdhmjG0YKruVfWGF95E8IjcbfP/bZXMYZsbuHOxESh1Z300bAOyew8lVZbG1BJdyOYeVVEp+TydSEn1aBFMuhCGaF3EYOe4+u25qu7G0ZcT/cQTSMdOomIXAgxPXR4PJ6hVzw4ia9eHOhsYCpgUuMjXzzjOPC5emH9x2bXAaSiEuQrGZGNsEsG4wtFH/7Q0vde1eHbTXj4oVGhVRcz48xfncZlNTW5aY/R2kmuC7XBsVoD68/8cDbroauP/nXga7TNbihM0zNslTV2G+9BaG43Ab66fX2+CqJuS70XaWcj5+HHOSyT5qEFxIPM94tlBkN58sYsvQkZ1lDQbaUsYTlNp+RJpBycKmoCd4MXIh7CxNdIoGyvnySKAOMRMSvdnCcA/6hleGltxD5e94Q9SrBwl72O9O421JE5VZfrBRHvLAx634tMUeflouPV07FbYZNHbDDOImAS0Q1b22eVXeetAGMN1JBcKmTINWem/tg/9Ww27i/ELwWnmO5K2x/b3l3HASx4DvLD6AnJeBrnmj4W88Y1wgtrnjIJEcVzhoPZJhk1vdA+SSHSVbq1NultzhnDuHkAs8atPG494xD1DXktt+j+0BwnCeYHodr50Vco/HqhLn209eODWWUvYL1UoEsX63KnvZZgnjxVTgbsnh/CjpfXkHUvlmul1OZrR8YPztQRt+pHYRqnFyiPRSxQoY0r2pFRghfTfaJC2s/CwhUsmL0ikgY9ZMYLcw2BjR0ey+5o84riSiQkFAXdca/7SUyu3Uz3nCbYmTA1Wgb5jtzgPpagtFt5mgmLbQWv1KZDWEIzackQtY9D2qUTXYvQintLHuG+SVHpctXzPeIpxIWPYcMS0DzIaFTsLaFSCk/PFvMicF3tClU41upa5Epf8q+WaPymhsjmiVO40tzsCwQ/qHkkkUhJ1sa27k12v8SnZSGQugr2Pj8VXXNujrJSIVhFxBkZqPp1ityjPUjNreW285JZLYr50mm68UOXD7hGlXS9Kgs1T5TbJ9SWDs7rvlyQdYKJdM04Gkf3borhXDXiR/IwLg/8ZesPR3Z1DNGmi8XQjlQx6JnuB+/kKuixcSg4A5lojXLhctozni1qOBWWHxZdKltuz/RUbMS86J6yE0nB9kVpW7AbOjuxq1SX+ZzoZ/o2lNf1eeShAjEfvrBYmiAugXSNgKtj1WSk0nqY8WiT9YqXKknMQ5e1Ssi7I5ZsVFqKY3dXLVzazcGa6LY22RJMjPs81OajntD02UwJKhkPWI/KM2r2rSxJjjydepUW78pqbF46ZvdKCNXM80G3HmMNFCb0YpybTmPX+wnySUWWR7cDOYx7rKPcMRQ6UbUtbTKWXieHeDKREe9duzDHmqNeAfaaceG+B1R4sS9JZc4hoszu1b0AGmXnY9FbJcksnH0TKcISvHrwy8zFnBAdH2vTlV1dpEczSypDPeOu1XRpPgCOD0eCG3SitnajeqYJyywEU2cKPAT94tLBCVVoT4MU0D4eHwG5PxUtzy5+cpYxaAeTu9Gv3uBtY19MN4rkyJBix85LyUVLLNJNH8d8DNnHnWsGOH0FhHeTIaUzt+c0d2Y4amIsVXALxqsFTP0iQsOvOlLacIDtcLX9XsganzpLMHFPX0gKACV1aM2iINR/kYNfy1xBVI5qKjc1Fut66WpA8q9QjskRsZn3KrmTnZvlKq+Q+3GvRbk7SWTlMlFd5g/oaNsDitr9qHkXnypfx9YlWd7h+d1VVADeo6TzutLeSsrqH+20FoV63FBpykzfyAnRvmy1ai74uVd39oKEgukW1wbBxPTc2S0MmV4VJ1PUcnd58U8vkNWWlIUiAUM+5xnxxZHAOBfVT/dphZ6XDJecXfU+ghYnIjsydM0maKkobskbRfDcMaZm6SFLGxdEhOS1IknhE5ohrTXWrQr7xNTFrr8hTljBnlJlNqEKl/S6VgA626FTrNGVK02rnUAcGPuyPE57xyX62vm2M/cFGlyQaQirZ3Ulj5OEj6OPThTUNa/THScbeEytRW7bUAppzzmHuFgG1Lk9yjZUjUtK7nRkcQyMnUGiK6Xu3hM4HPvVJo3boNEQJpzhh+NRgjJQvALJ77uP1/A4iNWY9fmVfp4XeGHrvBjc/PJkWfY//uPLT1/et6K/3fX9L7/X9L4l+n/tsurnvdL29Xl5/30zd0iC+JePs375r9X4nz99GaIcKPF5/Xas5uf3K6v/2eXbr29pX9/Svv7L5dtx+/xiUAsQZp2+X3qeguf7245fQix8r3nfUv92w/hfd38I/fiyAXiWf37JMe+S9038t4IfX1L7uC2M/vxW85//G6LOXTH6OQAA -->
