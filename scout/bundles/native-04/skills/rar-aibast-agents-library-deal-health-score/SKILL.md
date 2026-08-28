---
name: "rar-aibast-agents-library-deal-health-score"
description: "Scores deal health from live opportunities in a simulated Dynamics 365 tenant, with trends, alerts, and an embedded offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/deal_health_score", "rar_sha256": "d2e789bbc862d009e54289c5d563dd6c7a554fdfafcc8b6857dce4a5b09b86d0", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["b2b", "sales", "deal-health", "scoring", "pipeline"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/deal_health_score`. The original RAPP
agent is preserved byte-for-byte in `deal_health_score_agent.py` and in the RCI capsule.

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

Deal Health Score Agent — a template you are meant to mutate.

Calculates 0-100 deal health scores from engagement, stakeholder,
velocity, and sentiment signals, with trend analysis, benchmarks, and
proactive alerts to keep deals on track.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="calculate_health") — the scorecard covers
     live open deals such as "Marigold Field Services — Mobile
     workstation expansion", scored from CRM-visible signals
     (close probability + schedule slip).
  2. No network? Everything falls back to the embedded demo layer below
     (_DEAL_METRICS / _TREND_HISTORY) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     DEAL_HEALTH_SCORE_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with your own client. The dict shape the rest of
     the file needs is documented in _normalize_live_deal(). Engagement
     and sentiment signals (emails, meetings, tone) are enrichment
     seams — wire Gong / email analytics there.

OPERATIONS
  calculate_health | trend_analysis | benchmark_comparison | health_alerts
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
        "calculate_health",
        "trend_analysis",
        "benchmark_comparison",
        "health_alerts"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `deal_health_score_agent.py` and embedded as the fenced Python below (sha256 d2e789bbc862d009…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `deal_health_score_agent.py` first:

```bash
python3 deal_health_score_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 deal_health_score_agent.py   # or on stdin
python3 deal_health_score_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Deal Health Score Agent — a template you are meant to mutate.

Calculates 0-100 deal health scores from engagement, stakeholder,
velocity, and sentiment signals, with trend analysis, benchmarks, and
proactive alerts to keep deals on track.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="calculate_health") — the scorecard covers
     live open deals such as "Marigold Field Services — Mobile
     workstation expansion", scored from CRM-visible signals
     (close probability + schedule slip).
  2. No network? Everything falls back to the embedded demo layer below
     (_DEAL_METRICS / _TREND_HISTORY) — the agent never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     DEAL_HEALTH_SCORE_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with your own client. The dict shape the rest of
     the file needs is documented in _normalize_live_deal(). Engagement
     and sentiment signals (emails, meetings, tone) are enrichment
     seams — wire Gong / email analytics there.

OPERATIONS
  calculate_health | trend_analysis | benchmark_comparison | health_alerts
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
    "name": "@aibast-agents-library/deal_health_score",
    "version": "1.1.0",
    "display_name": "Deal Health Score",
    "description": "Scores deal health from live opportunities in a simulated Dynamics 365 tenant, with trends, alerts, and an embedded offline demo fallback.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "deal-health", "scoring", "pipeline"],
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
#   export DEAL_HEALTH_SCORE_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_deal().
# ===================================================================

DATA_SOURCE_URL = os.environ.get(
    "DEAL_HEALTH_SCORE_DATA_URL",
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
    renderers label it an enrichment seam (wire Gong / email analytics
    for engagement and sentiment)."""
    overdue = _days_overdue(row.get("estimatedclosedate"))
    crm_prob = int(row.get("closeprobability") or 0)
    # CRM-signal health: close probability, penalized when the deal has
    # slipped past its own estimated close date. Real math on real fields.
    crm_health = max(5, min(95, crm_prob - min(30, overdue // 7 * 5)))
    return {
        "deal_id": str(row.get("opportunityid", ""))[:8],
        "name": row.get("name", "Unknown"),
        "account": row.get("parentaccountidname", "Unknown"),
        "value": int(float(row.get("estimatedvalue") or 0)),
        "stage": _LIVE_STAGE_MAP.get(row.get("stepname"), "Qualification"),
        "owner": row.get("owneridname", ""),
        "crm_probability": crm_prob,
        "days_past_est_close": overdue,
        "crm_health": crm_health,
        "engagement": None,   # enrichment seam — wire email/meeting analytics
        "sentiment": None,    # enrichment seam — wire Gong
        "_live": True,
    }


def _live_open_deals():
    """Live open opportunities normalized for this agent; [] when offline."""
    return [_normalize_live_deal(o) for o in _fetch_collection("opportunities")
            if o.get("statecode") == 0]


# ===================================================================
# EMBEDDED DEMO LAYER (offline fallback)
# ===================================================================

_DEAL_METRICS = {
    "TechCorp Industries": {
        "deal_id": "OPP-001", "value": 890000, "stage": "Proposal", "owner": "Mike Chen",
        "engagement": {"emails_sent": 24, "emails_opened": 18, "meetings_held": 6, "calls_logged": 8, "days_since_last_touch": 18},
        "stakeholders": {"total": 5, "engaged": 2, "champion_active": False, "exec_sponsor": False},
        "velocity": {"days_in_stage": 34, "benchmark_days": 16, "stage_entries": 4, "regression_count": 1},
        "sentiment": {"last_meeting_tone": "neutral", "email_responsiveness": 0.42, "objections_raised": 3, "positive_signals": 1},
    },
    "Global Manufacturing": {
        "deal_id": "OPP-002", "value": 720000, "stage": "Negotiation", "owner": "Lisa Torres",
        "engagement": {"emails_sent": 31, "emails_opened": 28, "meetings_held": 9, "calls_logged": 12, "days_since_last_touch": 5},
        "stakeholders": {"total": 4, "engaged": 3, "champion_active": True, "exec_sponsor": False},
        "velocity": {"days_in_stage": 28, "benchmark_days": 12, "stage_entries": 5, "regression_count": 0},
        "sentiment": {"last_meeting_tone": "positive", "email_responsiveness": 0.78, "objections_raised": 2, "positive_signals": 4},
    },
    "Apex Financial": {
        "deal_id": "OPP-003", "value": 580000, "stage": "Discovery", "owner": "James Park",
        "engagement": {"emails_sent": 12, "emails_opened": 6, "meetings_held": 2, "calls_logged": 3, "days_since_last_touch": 12},
        "stakeholders": {"total": 6, "engaged": 1, "champion_active": False, "exec_sponsor": False},
        "velocity": {"days_in_stage": 25, "benchmark_days": 18, "stage_entries": 2, "regression_count": 0},
        "sentiment": {"last_meeting_tone": "cautious", "email_responsiveness": 0.35, "objections_raised": 4, "positive_signals": 0},
    },
    "Metro Healthcare": {
        "deal_id": "OPP-004", "value": 440000, "stage": "Proposal", "owner": "Mike Chen",
        "engagement": {"emails_sent": 18, "emails_opened": 15, "meetings_held": 5, "calls_logged": 7, "days_since_last_touch": 9},
        "stakeholders": {"total": 4, "engaged": 3, "champion_active": True, "exec_sponsor": True},
        "velocity": {"days_in_stage": 22, "benchmark_days": 16, "stage_entries": 4, "regression_count": 0},
        "sentiment": {"last_meeting_tone": "positive", "email_responsiveness": 0.72, "objections_raised": 1, "positive_signals": 3},
    },
    "Pacific Telecom": {
        "deal_id": "OPP-013", "value": 780000, "stage": "Negotiation", "owner": "Lisa Torres",
        "engagement": {"emails_sent": 35, "emails_opened": 32, "meetings_held": 11, "calls_logged": 14, "days_since_last_touch": 3},
        "stakeholders": {"total": 5, "engaged": 4, "champion_active": True, "exec_sponsor": True},
        "velocity": {"days_in_stage": 14, "benchmark_days": 12, "stage_entries": 5, "regression_count": 0},
        "sentiment": {"last_meeting_tone": "very_positive", "email_responsiveness": 0.91, "objections_raised": 0, "positive_signals": 6},
    },
    "Pinnacle Logistics": {
        "deal_id": "OPP-005", "value": 360000, "stage": "Qualification", "owner": "James Park",
        "engagement": {"emails_sent": 8, "emails_opened": 3, "meetings_held": 1, "calls_logged": 2, "days_since_last_touch": 14},
        "stakeholders": {"total": 3, "engaged": 1, "champion_active": False, "exec_sponsor": False},
        "velocity": {"days_in_stage": 20, "benchmark_days": 14, "stage_entries": 1, "regression_count": 0},
        "sentiment": {"last_meeting_tone": "neutral", "email_responsiveness": 0.25, "objections_raised": 2, "positive_signals": 0},
    },
}

_BENCHMARKS = {
    "top_quartile": {"health_score": 82, "engagement_rate": 0.85, "stakeholder_coverage": 0.80, "velocity_ratio": 0.90},
    "median": {"health_score": 62, "engagement_rate": 0.60, "stakeholder_coverage": 0.55, "velocity_ratio": 1.10},
    "bottom_quartile": {"health_score": 38, "engagement_rate": 0.35, "stakeholder_coverage": 0.30, "velocity_ratio": 1.60},
}

_TREND_HISTORY = {
    "TechCorp Industries": [72, 68, 61, 55, 48, 42],
    "Global Manufacturing": [45, 52, 58, 62, 65, 63],
    "Apex Financial": [55, 50, 44, 38, 35, 32],
    "Metro Healthcare": [58, 62, 65, 68, 70, 67],
    "Pacific Telecom": [60, 65, 72, 78, 82, 85],
    "Pinnacle Logistics": [40, 38, 35, 33, 30, 28],
}


# ===================================================================
# HELPERS
# ===================================================================

def _calculate_health(deal_name):
    """Calculate composite health score (0-100)."""
    m = _DEAL_METRICS.get(deal_name)
    if not m:
        return 0

    eng = m["engagement"]
    email_rate = eng["emails_opened"] / max(eng["emails_sent"], 1)
    touch_score = max(0, 25 - eng["days_since_last_touch"]) * 4
    meeting_score = min(eng["meetings_held"] * 8, 30)
    engagement_score = round(email_rate * 30 + touch_score * 0.3 + meeting_score * 0.4)

    st = m["stakeholders"]
    coverage = st["engaged"] / max(st["total"], 1)
    champion_bonus = 15 if st["champion_active"] else 0
    exec_bonus = 10 if st["exec_sponsor"] else 0
    stakeholder_score = round(coverage * 40 + champion_bonus + exec_bonus)

    v = m["velocity"]
    ratio = v["days_in_stage"] / max(v["benchmark_days"], 1)
    velocity_score = max(0, round(100 - (ratio - 1) * 50)) if ratio > 1 else 100
    regression_penalty = v["regression_count"] * 15
    velocity_score = max(0, velocity_score - regression_penalty)

    s = m["sentiment"]
    tone_map = {"very_positive": 25, "positive": 20, "neutral": 10, "cautious": 5, "negative": 0}
    tone_score = tone_map.get(s["last_meeting_tone"], 10)
    response_score = round(s["email_responsiveness"] * 25)
    signal_score = max(0, (s["positive_signals"] - s["objections_raised"]) * 8)
    sentiment_score = tone_score + response_score + signal_score

    composite = round(
        engagement_score * 0.25 +
        stakeholder_score * 0.30 +
        velocity_score * 0.25 +
        sentiment_score * 0.20
    )
    return max(0, min(100, composite))


def _health_grade(score):
    """Convert numeric score to letter grade."""
    if score >= 80:
        return "A"
    if score >= 65:
        return "B"
    if score >= 50:
        return "C"
    if score >= 35:
        return "D"
    return "F"


def _trend_direction(history):
    """Determine trend from score history."""
    if len(history) < 2:
        return "stable", 0
    recent = history[-2:]
    delta = recent[-1] - recent[0]
    if delta > 3:
        return "improving", delta
    if delta < -3:
        return "declining", delta
    return "stable", delta


# ===================================================================
# AGENT CLASS
# ===================================================================

class DealHealthScoreAgent(BasicAgent):
    """
    Calculates deal health scores and surfaces trends and alerts.

    Operations:
        calculate_health      - compute health scores for all deals
        trend_analysis         - 6-period trend with direction indicators
        benchmark_comparison   - compare deals against quartile benchmarks
        health_alerts          - proactive alerts for declining or critical deals
    """

    def __init__(self):
        self.name = "DealHealthScoreAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["calculate_health", "trend_analysis", "benchmark_comparison", "health_alerts"],
                        "description": "The analysis to perform",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "calculate_health")
        dispatch = {
            "calculate_health": self._calculate_health,
            "trend_analysis": self._trend_analysis,
            "benchmark_comparison": self._benchmark_comparison,
            "health_alerts": self._health_alerts,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"**Error:** Unknown operation '{op}'. Valid: {', '.join(dispatch.keys())}"
        return handler()

    # -- calculate_health (flagship: prefers LIVE tenant, falls back) ---
    def _calculate_health(self) -> str:
        live = _live_open_deals()
        if live:
            rows = ""
            scores = []
            for d in sorted(live, key=lambda x: -x["value"]):
                scores.append(d["crm_health"])
                grade = _health_grade(d["crm_health"])
                schedule = (f"{d['days_past_est_close']}d past est. close"
                            if d["days_past_est_close"] else "on schedule")
                rows += (f"| {d['name']} | ${d['value']:,} | {d['stage']} | "
                         f"{d['crm_health']}/100 | {grade} | {schedule} | "
                         f"n/a — enrichment seam |\n")
            avg_score = round(sum(scores) / max(len(scores), 1))
            critical = sum(1 for s in scores if s < 40)
            healthy = sum(1 for s in scores if s >= 65)
            return (
                f"**Deal Health Scorecard — {len(live)} LIVE Open Deals** "
                f"(Static Dynamics 365 tenant)\n\n"
                f"Portfolio avg: **{avg_score}/100** | Healthy: {healthy} | Critical: {critical}\n\n"
                f"| Deal | Value | Stage | CRM Health | Grade | Schedule | Engagement/Sentiment |\n"
                f"|------|-------|-------|-----------|-------|----------|---------------------|\n"
                f"{rows}\n"
                f"**Scoring:** CRM-visible signals only (close probability + schedule slip). "
                f"Engagement and sentiment stay n/a until you wire Gong / email analytics "
                f"at the LIVE DATA SEAM.\n\n"
                f"Source: [Live Dynamics 365 opportunities]\n"
                f"Agents: HealthScoringEngine"
            )
        rows = ""
        scores = []
        for deal_name in sorted(_DEAL_METRICS.keys(), key=lambda d: -_DEAL_METRICS[d]["value"]):
            m = _DEAL_METRICS[deal_name]
            score = _calculate_health(deal_name)
            scores.append(score)
            grade = _health_grade(score)
            trend, delta = _trend_direction(_TREND_HISTORY.get(deal_name, []))
            trend_str = f"+{delta}" if delta > 0 else str(delta)
            rows += f"| {deal_name} | ${m['value']:,} | {m['stage']} | {score}/100 | {grade} | {trend} ({trend_str}) |\n"

        avg_score = round(sum(scores) / max(len(scores), 1))
        critical = sum(1 for s in scores if s < 40)
        healthy = sum(1 for s in scores if s >= 65)

        return (
            f"**Deal Health Scorecard**\n\n"
            f"Portfolio avg: **{avg_score}/100** | Healthy: {healthy} | Critical: {critical}\n\n"
            f"| Deal | Value | Stage | Health | Grade | Trend |\n"
            f"|------|-------|-------|--------|-------|-------|\n"
            f"{rows}\n"
            f"**Scoring Factors:** Engagement (25%), Stakeholder Coverage (30%), "
            f"Velocity (25%), Sentiment (20%)\n\n"
            f"Source: [CRM + Email Analytics + Meeting Logs + Gong]\n"
            f"Agents: HealthScoringEngine, EngagementTracker"
        )

    # -- trend_analysis ------------------------------------------------
    def _trend_analysis(self) -> str:
        sections = []
        for deal_name in sorted(_DEAL_METRICS.keys(), key=lambda d: -_DEAL_METRICS[d]["value"]):
            history = _TREND_HISTORY.get(deal_name, [])
            if not history:
                continue
            current = history[-1]
            direction, delta = _trend_direction(history)
            period_labels = ["W-5", "W-4", "W-3", "W-2", "W-1", "Current"]
            score_line = " | ".join(f"{period_labels[i]}: {s}" for i, s in enumerate(history))
            peak = max(history)
            trough = min(history)
            volatility = peak - trough

            status = "IMPROVING" if direction == "improving" else ("DECLINING" if direction == "declining" else "STABLE")
            sections.append(
                f"**{deal_name} -- ${_DEAL_METRICS[deal_name]['value']:,}**\n"
                f"Status: {status} | Current: {current}/100 | 6-week delta: {history[-1] - history[0]:+d}\n"
                f"Trend: {score_line}\n"
                f"Range: {trough}-{peak} (volatility: {volatility})\n"
            )

        improving = sum(1 for d in _TREND_HISTORY.values() if d and d[-1] > d[0])
        declining = sum(1 for d in _TREND_HISTORY.values() if d and d[-1] < d[0])

        return (
            f"**Health Score Trends -- 6-Week Analysis**\n\n"
            f"Improving: {improving} | Declining: {declining} | Stable: {len(_TREND_HISTORY) - improving - declining}\n\n"
            + "\n---\n\n".join(sections)
            + f"\n\nSource: [Historical Health Scores + Activity Logs]\n"
            f"Agents: TrendAnalysisEngine"
        )

    # -- benchmark_comparison ------------------------------------------
    def _benchmark_comparison(self) -> str:
        rows = ""
        for deal_name in sorted(_DEAL_METRICS.keys(), key=lambda d: -_DEAL_METRICS[d]["value"]):
            m = _DEAL_METRICS[deal_name]
            score = _calculate_health(deal_name)
            eng = m["engagement"]
            st = m["stakeholders"]
            v = m["velocity"]

            email_rate = round(eng["emails_opened"] / max(eng["emails_sent"], 1), 2)
            coverage = round(st["engaged"] / max(st["total"], 1), 2)
            vel_ratio = round(v["days_in_stage"] / max(v["benchmark_days"], 1), 2)

            if score >= _BENCHMARKS["top_quartile"]["health_score"]:
                quartile = "Top 25%"
            elif score >= _BENCHMARKS["median"]["health_score"]:
                quartile = "Above Median"
            elif score >= _BENCHMARKS["bottom_quartile"]["health_score"]:
                quartile = "Below Median"
            else:
                quartile = "Bottom 25%"

            rows += f"| {deal_name} | {score} | {quartile} | {email_rate} | {coverage} | {vel_ratio}x |\n"

        return (
            f"**Benchmark Comparison**\n\n"
            f"**Quartile Thresholds:**\n"
            f"- Top 25%: Health >= {_BENCHMARKS['top_quartile']['health_score']}, "
            f"Engagement >= {_BENCHMARKS['top_quartile']['engagement_rate']}\n"
            f"- Median: Health >= {_BENCHMARKS['median']['health_score']}, "
            f"Engagement >= {_BENCHMARKS['median']['engagement_rate']}\n"
            f"- Bottom 25%: Health < {_BENCHMARKS['bottom_quartile']['health_score']}\n\n"
            f"| Deal | Score | Quartile | Email Rate | Stakeholder Coverage | Velocity Ratio |\n"
            f"|------|-------|----------|-----------|---------------------|---------------|\n"
            f"{rows}\n"
            f"**Note:** Velocity ratio >1.0 means deal is slower than benchmark.\n\n"
            f"Source: [Pipeline Benchmarks + Peer Comparison Data]\n"
            f"Agents: BenchmarkEngine"
        )

    # -- health_alerts -------------------------------------------------
    def _health_alerts(self) -> str:
        alerts = []
        for deal_name in _DEAL_METRICS:
            m = _DEAL_METRICS[deal_name]
            score = _calculate_health(deal_name)
            history = _TREND_HISTORY.get(deal_name, [])
            direction, delta = _trend_direction(history)

            deal_alerts = []
            if score < 35:
                deal_alerts.append({"level": "CRITICAL", "msg": f"Health score critically low at {score}/100"})
            if direction == "declining" and delta <= -5:
                deal_alerts.append({"level": "WARNING", "msg": f"Rapid decline: {delta} points in last period"})
            if m["engagement"]["days_since_last_touch"] >= 14:
                deal_alerts.append({"level": "CRITICAL", "msg": f"No contact in {m['engagement']['days_since_last_touch']} days"})
            if not m["stakeholders"]["champion_active"]:
                deal_alerts.append({"level": "WARNING", "msg": "No active champion identified"})
            if m["velocity"]["days_in_stage"] > m["velocity"]["benchmark_days"] * 1.5:
                deal_alerts.append({"level": "WARNING", "msg": f"Stage velocity {m['velocity']['days_in_stage']}d vs {m['velocity']['benchmark_days']}d benchmark"})
            if m["sentiment"]["objections_raised"] >= 3:
                deal_alerts.append({"level": "INFO", "msg": f"{m['sentiment']['objections_raised']} unresolved objections logged"})

            for a in deal_alerts:
                alerts.append({"deal": deal_name, "value": m["value"], **a})

        alerts.sort(key=lambda a: (0 if a["level"] == "CRITICAL" else (1 if a["level"] == "WARNING" else 2), -a["value"]))

        rows = ""
        for a in alerts:
            rows += f"| {a['level']} | {a['deal']} | ${a['value']:,} | {a['msg']} |\n"

        critical_count = sum(1 for a in alerts if a["level"] == "CRITICAL")
        warning_count = sum(1 for a in alerts if a["level"] == "WARNING")

        return (
            f"**Health Alerts Dashboard**\n\n"
            f"Critical: **{critical_count}** | Warnings: **{warning_count}** | Total: {len(alerts)}\n\n"
            f"| Level | Deal | Value | Alert |\n"
            f"|-------|------|-------|-------|\n"
            f"{rows}\n"
            f"**Recommended Actions:**\n"
            f"- Critical alerts require same-day response from deal owner\n"
            f"- Warning alerts should be addressed within 48 hours\n"
            f"- Schedule pipeline review for all deals scoring below 40\n\n"
            f"Source: [Real-time Health Monitoring]\n"
            f"Agents: AlertEngine, NotificationAgent"
        )


if __name__ == "__main__":
    agent = DealHealthScoreAgent()
    print("=" * 70)
    print("LIVE TENANT SCORECARD (fetched over HTTP; embedded demo offline)")
    print(agent.perform(operation="calculate_health"))
    print()
    print("=" * 70)
    print("EMBEDDED DEMO (works offline, simulated)")
    print(agent.perform(operation="trend_analysis"))
    print()
    print("=" * 70)
    print(agent.perform(operation="health_alerts"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
