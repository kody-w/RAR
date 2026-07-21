"""
Product Feedback Synthesizer Agent for Software/Digital Products.

Aggregates and synthesizes customer feedback, feature requests, sentiment
analysis, and roadmap impact assessments for product management teams.

Version 1.1.0 adds deterministic, evidence-derived pain-point analysis,
retention and competitive risk alerts, and simulated Jira/Teams activation.
The four original operations and the agent's package/runtime identity remain
unchanged.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/product_feedback_synthesizer",
    "version": "1.1.1",
    "display_name": "Product Feedback Synthesizer Agent",
    "description": "Synthesizes customer feedback, sentiment, and roadmap impact reports for product teams from built-in demo data; Jira/Teams writes are simulated.",
    "author": "AIBAST",
    "tags": ["feedback", "product", "feature-requests", "sentiment", "roadmap", "nps"],
    "category": "software_digital_products",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ---------------------------------------------------------------------------
# Synthetic domain data
# ---------------------------------------------------------------------------

FEEDBACK_ENTRIES = {
    "FB-5001": {
        "customer": "Meridian Healthcare Systems",
        "channel": "support_ticket",
        "date": "2026-02-14",
        "category": "usability",
        "sentiment": "negative",
        "score": 2,
        "text": "The dashboard takes too many clicks to get to key metrics. We need a customizable home view.",
        "arr_impact": 186000,
    },
    "FB-5002": {
        "customer": "Apex Financial Group",
        "channel": "nps_survey",
        "date": "2026-02-20",
        "category": "feature_gap",
        "sentiment": "neutral",
        "score": 6,
        "text": "Product is solid but missing real-time alerting capabilities that competitors offer.",
        "arr_impact": 240000,
    },
    "FB-5003": {
        "customer": "Skyline Hospitality Group",
        "channel": "qbr",
        "date": "2026-03-01",
        "category": "praise",
        "sentiment": "positive",
        "score": 9,
        "text": "Integration with our POS system has been seamless. Would love to see mobile app improvements.",
        "arr_impact": 360000,
    },
    "FB-5004": {
        "customer": "Vanguard Logistics",
        "channel": "support_ticket",
        "date": "2026-01-28",
        "category": "bug_report",
        "sentiment": "negative",
        "score": 1,
        "text": "Data export fails consistently for reports over 10K rows. This is blocking our migration.",
        "arr_impact": 84000,
    },
    "FB-5005": {
        "customer": "BrightPath Education",
        "channel": "in_app",
        "date": "2026-03-05",
        "category": "feature_gap",
        "sentiment": "neutral",
        "score": 5,
        "text": "Need role-based access controls for student data. Currently everyone sees everything.",
        "arr_impact": 96000,
    },
    "FB-5006": {
        "customer": "Orion Manufacturing",
        "channel": "sales_call",
        "date": "2026-03-10",
        "category": "feature_gap",
        "sentiment": "positive",
        "score": 8,
        "text": "Great product overall. If you add workflow automation we would double our seat count.",
        "arr_impact": 312000,
    },
}

FEATURE_REQUESTS = {
    "FR-001": {
        "title": "Customizable Dashboard Home View",
        "votes": 87,
        "arr_weight": 612000,
        "status": "under_review",
        "effort": "medium",
        "category": "usability",
        "linked_feedback": ["FB-5001"],
    },
    "FR-002": {
        "title": "Real-Time Alerting Engine",
        "votes": 134,
        "arr_weight": 780000,
        "status": "planned_q3",
        "effort": "high",
        "category": "feature_gap",
        "linked_feedback": ["FB-5002"],
    },
    "FR-003": {
        "title": "Mobile App Enhancements",
        "votes": 62,
        "arr_weight": 420000,
        "status": "in_progress",
        "effort": "medium",
        "category": "usability",
        "linked_feedback": ["FB-5003"],
    },
    "FR-004": {
        "title": "Large Dataset Export Fix",
        "votes": 41,
        "arr_weight": 264000,
        "status": "in_progress",
        "effort": "low",
        "category": "bug_fix",
        "linked_feedback": ["FB-5004"],
    },
    "FR-005": {
        "title": "Role-Based Access Controls (RBAC)",
        "votes": 156,
        "arr_weight": 960000,
        "status": "planned_q2",
        "effort": "high",
        "category": "security",
        "linked_feedback": ["FB-5005"],
    },
    "FR-006": {
        "title": "Workflow Automation Builder",
        "votes": 203,
        "arr_weight": 1140000,
        "status": "planned_q3",
        "effort": "high",
        "category": "feature_gap",
        "linked_feedback": ["FB-5006"],
    },
}

NPS_SCORES = {
    "2025-Q4": {"promoters": 142, "passives": 88, "detractors": 45, "score": 35},
    "2026-Q1": {"promoters": 158, "passives": 91, "detractors": 51, "score": 36},
}

EVIDENCE_ACTIONS = {
    "FR-001": {
        "pain_point": "Too many clicks to reach key metrics",
        "theme": "Customizable experience",
        "frequency": 87,
        "severity": 4,
        "retention_impact": "medium",
        "competitive_gap": "Competitors offer configurable home views",
        "jira_project": "PRODUCT",
        "teams_channel": "Product Feedback Triage",
    },
    "FR-002": {
        "pain_point": "Missing real-time alerting",
        "theme": "Proactive monitoring",
        "frequency": 134,
        "severity": 5,
        "retention_impact": "high",
        "competitive_gap": "Alerting is available in competing products",
        "jira_project": "PLATFORM",
        "teams_channel": "Product and Engineering",
    },
    "FR-003": {
        "pain_point": "Mobile workflows lag the web experience",
        "theme": "Mobile productivity",
        "frequency": 62,
        "severity": 3,
        "retention_impact": "medium",
        "competitive_gap": "Mobile parity is becoming a buying criterion",
        "jira_project": "MOBILE",
        "teams_channel": "Mobile Experience",
    },
    "FR-004": {
        "pain_point": "Exports fail above 10,000 rows",
        "theme": "Reliability at scale",
        "frequency": 41,
        "severity": 5,
        "retention_impact": "high",
        "competitive_gap": "Reliable large exports are required for migrations",
        "jira_project": "DATA",
        "teams_channel": "Data Reliability",
    },
    "FR-005": {
        "pain_point": "Student data lacks role-based access controls",
        "theme": "Enterprise security",
        "frequency": 156,
        "severity": 5,
        "retention_impact": "critical",
        "competitive_gap": "Enterprise competitors include granular RBAC",
        "jira_project": "SECURITY",
        "teams_channel": "Security and Product",
    },
    "FR-006": {
        "pain_point": "Teams cannot automate repeatable workflows",
        "theme": "Workflow automation",
        "frequency": 203,
        "severity": 4,
        "retention_impact": "high",
        "competitive_gap": "Competitor automation is blocking expansion",
        "jira_project": "AUTOMATION",
        "teams_channel": "Automation Roadmap",
    },
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _exact_feature(feature_id):
    if not feature_id:
        return None, "Provide an exact feature_id: " + ", ".join(sorted(FEATURE_REQUESTS))
    if feature_id not in FEATURE_REQUESTS:
        return None, f"Unknown feature_id `{feature_id}`; exact ID required."
    return FEATURE_REQUESTS[feature_id], None

def _feedback_summary():
    by_sentiment = {"positive": 0, "neutral": 0, "negative": 0}
    by_category = {}
    by_channel = {}
    total_arr = 0
    for fb in FEEDBACK_ENTRIES.values():
        by_sentiment[fb["sentiment"]] += 1
        by_category[fb["category"]] = by_category.get(fb["category"], 0) + 1
        by_channel[fb["channel"]] = by_channel.get(fb["channel"], 0) + 1
        total_arr += fb["arr_impact"]
    avg_score = round(sum(fb["score"] for fb in FEEDBACK_ENTRIES.values()) / len(FEEDBACK_ENTRIES), 1)
    return {
        "total_entries": len(FEEDBACK_ENTRIES),
        "by_sentiment": by_sentiment,
        "by_category": by_category,
        "by_channel": by_channel,
        "avg_score": avg_score,
        "total_arr_represented": total_arr,
    }


def _feature_request_ranking():
    ranked = sorted(FEATURE_REQUESTS.values(), key=lambda x: x["arr_weight"], reverse=True)
    return {"requests": ranked, "total_requests": len(ranked)}


def _sentiment_analysis():
    results = []
    for fid, fb in FEEDBACK_ENTRIES.items():
        results.append({
            "id": fid, "customer": fb["customer"], "sentiment": fb["sentiment"],
            "score": fb["score"], "category": fb["category"], "channel": fb["channel"],
            "excerpt": fb["text"][:80],
        })
    pos = sum(1 for r in results if r["sentiment"] == "positive")
    neg = sum(1 for r in results if r["sentiment"] == "negative")
    return {"entries": results, "positive_pct": round(pos / len(results) * 100, 1),
            "negative_pct": round(neg / len(results) * 100, 1), "nps_trend": NPS_SCORES}


def _roadmap_impact():
    impacts = []
    for frid, fr in FEATURE_REQUESTS.items():
        impacts.append({
            "id": frid, "title": fr["title"], "votes": fr["votes"],
            "arr_weight": fr["arr_weight"], "effort": fr["effort"],
            "status": fr["status"], "category": fr["category"],
            "priority_score": round(fr["arr_weight"] / 1000 / (3 if fr["effort"] == "high" else 2 if fr["effort"] == "medium" else 1), 1),
        })
    impacts.sort(key=lambda x: x["priority_score"], reverse=True)
    return {"items": impacts}


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

class ProductFeedbackSynthesizerAgent(BasicAgent):
    """Product feedback synthesis and roadmap impact agent."""

    def __init__(self):
        self.name = "ProductFeedbackSynthesizerAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "feedback_summary",
                            "feature_requests",
                            "sentiment_analysis",
                            "roadmap_impact",
                            "pain_point_analysis",
                            "risk_alerts",
                            "activate_roadmap_action",
                        ],
                        "description": "The feedback operation to perform.",
                    },
                    "feature_id": {
                        "type": "string",
                        "description": "Exact feature request ID for roadmap activation.",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "feedback_summary")
        if op == "feedback_summary":
            return self._feedback_summary()
        elif op == "feature_requests":
            return self._feature_requests()
        elif op == "sentiment_analysis":
            return self._sentiment_analysis()
        elif op == "roadmap_impact":
            return self._roadmap_impact()
        elif op == "pain_point_analysis":
            return self._pain_point_analysis()
        elif op == "risk_alerts":
            return self._risk_alerts()
        elif op == "activate_roadmap_action":
            return self._activate_roadmap_action(kwargs.get("feature_id"))
        return f"**Error:** Unknown operation `{op}`."

    def _feedback_summary(self) -> str:
        data = _feedback_summary()
        lines = [
            "# Product Feedback Summary",
            "",
            f"**Total Feedback Entries:** {data['total_entries']}",
            f"**Avg Satisfaction Score:** {data['avg_score']}/10",
            f"**ARR Represented:** ${data['total_arr_represented']:,}",
            "",
            "## Sentiment Breakdown",
            "",
            "| Sentiment | Count |",
            "|-----------|-------|",
        ]
        for s, c in data["by_sentiment"].items():
            lines.append(f"| {s.title()} | {c} |")
        lines.append("")
        lines.append("## By Category")
        lines.append("")
        lines.append("| Category | Count |")
        lines.append("|----------|-------|")
        for cat, c in data["by_category"].items():
            lines.append(f"| {cat.replace('_', ' ').title()} | {c} |")
        lines.append("")
        lines.append("## By Channel")
        lines.append("")
        lines.append("| Channel | Count |")
        lines.append("|---------|-------|")
        for ch, c in data["by_channel"].items():
            lines.append(f"| {ch.replace('_', ' ').title()} | {c} |")
        return "\n".join(lines)

    def _feature_requests(self) -> str:
        data = _feature_request_ranking()
        lines = [
            "# Feature Requests (Ranked by ARR Weight)",
            "",
            f"**Total Requests:** {data['total_requests']}",
            "",
            "| Rank | Feature | Votes | ARR Weight | Effort | Status |",
            "|------|---------|-------|-----------|--------|--------|",
        ]
        for i, fr in enumerate(data["requests"], 1):
            lines.append(
                f"| {i} | {fr['title']} | {fr['votes']} | ${fr['arr_weight']:,} "
                f"| {fr['effort'].upper()} | {fr['status']} |"
            )
        return "\n".join(lines)

    def _sentiment_analysis(self) -> str:
        data = _sentiment_analysis()
        lines = [
            "# Sentiment Analysis",
            "",
            f"**Positive:** {data['positive_pct']}% | **Negative:** {data['negative_pct']}%",
            "",
            "## NPS Trend",
            "",
            "| Quarter | Promoters | Passives | Detractors | NPS |",
            "|---------|-----------|----------|------------|-----|",
        ]
        for q, nps in data["nps_trend"].items():
            lines.append(f"| {q} | {nps['promoters']} | {nps['passives']} | {nps['detractors']} | {nps['score']} |")
        lines.append("")
        lines.append("## Recent Feedback")
        lines.append("")
        lines.append("| Customer | Sentiment | Score | Category | Excerpt |")
        lines.append("|----------|-----------|-------|----------|---------|")
        for e in data["entries"]:
            lines.append(
                f"| {e['customer']} | {e['sentiment'].upper()} | {e['score']} "
                f"| {e['category']} | {e['excerpt']}... |"
            )
        return "\n".join(lines)

    def _roadmap_impact(self) -> str:
        data = _roadmap_impact()
        lines = [
            "# Roadmap Impact Assessment",
            "",
            "| Rank | Feature | Priority Score | ARR Weight | Effort | Status |",
            "|------|---------|---------------|-----------|--------|--------|",
        ]
        for i, item in enumerate(data["items"], 1):
            lines.append(
                f"| {i} | {item['title']} | {item['priority_score']} "
                f"| ${item['arr_weight']:,} | {item['effort'].upper()} | {item['status']} |"
            )
        lines.append("")
        lines.append("## Recommendations")
        lines.append("- RBAC and Workflow Automation are highest priority by ARR-weighted scoring.")
        lines.append("- Large Dataset Export fix is quick win with low effort and active churn risk.")
        lines.append("- Real-Time Alerting should be accelerated given competitive pressure.")
        return "\n".join(lines)

    def _pain_point_analysis(self) -> str:
        ranked = sorted(
            EVIDENCE_ACTIONS.items(),
            key=lambda item: (item[1]["frequency"] * item[1]["severity"], item[0]),
            reverse=True,
        )
        lines = [
            "# Pain Point and Feature Theme Analysis",
            "",
            "| Rank | Feature ID | Pain Point | Theme | Frequency | Severity | Retention Impact |",
            "|------|------------|------------|-------|-----------|----------|------------------|",
        ]
        for rank, (feature_id, action) in enumerate(ranked, 1):
            lines.append(
                f"| {rank} | {feature_id} | {action['pain_point']} | {action['theme']} "
                f"| {action['frequency']} | {action['severity']}/5 | {action['retention_impact'].upper()} |"
            )
        lines.extend([
            "",
            "Ranking is deterministic: feedback frequency multiplied by severity, with feature ID as the tie-breaker.",
        ])
        return "\n".join(lines)

    def _risk_alerts(self) -> str:
        ranked = sorted(
            EVIDENCE_ACTIONS.items(),
            key=lambda item: (FEATURE_REQUESTS[item[0]]["arr_weight"], item[0]),
            reverse=True,
        )
        lines = [
            "# Churn Risk and Competitive Gap Alerts",
            "",
            "| Feature ID | Retention Risk | ARR Represented | Competitive Gap |",
            "|------------|----------------|-----------------|-----------------|",
        ]
        for feature_id, action in ranked:
            request = FEATURE_REQUESTS[feature_id]
            lines.append(
                f"| {feature_id} | {action['retention_impact'].upper()} "
                f"| ${request['arr_weight']:,} | {action['competitive_gap']} |"
            )
        lines.extend([
            "",
            "**Recommended Intervention:** Escalate critical/high retention risks before the next roadmap review.",
        ])
        return "\n".join(lines)

    def _activate_roadmap_action(self, feature_id) -> str:
        request, error = _exact_feature(feature_id)
        if error:
            return f"**Error:** {error}"
        action = EVIDENCE_ACTIONS[feature_id]
        priority_score = round(
            request["arr_weight"] / 1000
            / (3 if request["effort"] == "high" else 2 if request["effort"] == "medium" else 1),
            1,
        )
        return "\n".join([
            f"# Roadmap Action Activated — {request['title']}",
            "",
            f"**Feature ID:** {feature_id}",
            f"**Theme:** {action['theme']}",
            f"**Pain Point:** {action['pain_point']}",
            f"**Evidence:** {action['frequency']} signals at severity {action['severity']}/5",
            f"**Business Impact:** ${request['arr_weight']:,} ARR represented",
            f"**Engineering Effort:** {request['effort'].upper()}",
            f"**Priority Score:** {priority_score}",
            f"**Retention Risk:** {action['retention_impact'].upper()}",
            f"**Competitive Gap:** {action['competitive_gap']}",
            "",
            f"**Jira Ticket:** {action['jira_project']}-{feature_id}",
            f"**Jira Receipt:** sim-jira-{feature_id.lower()}",
            f"**Microsoft Teams Channel:** {action['teams_channel']}",
            f"**Teams Receipt:** sim-teams-product-{feature_id.lower()}",
            "**External Writes:** simulated; no live Jira or Microsoft Teams mutation performed.",
        ])


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    agent = ProductFeedbackSynthesizerAgent()
    for op in ["feedback_summary", "feature_requests", "sentiment_analysis", "roadmap_impact"]:
        print(f"\n{'='*60}")
        print(f"Operation: {op}")
        print("=" * 60)
        print(agent.perform(operation=op))
