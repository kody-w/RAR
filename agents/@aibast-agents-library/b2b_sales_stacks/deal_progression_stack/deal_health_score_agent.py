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
