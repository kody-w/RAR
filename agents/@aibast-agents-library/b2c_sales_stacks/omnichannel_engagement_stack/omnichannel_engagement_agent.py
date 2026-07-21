"""
Omnichannel Engagement Agent — B2C Sales Stack

Analyzes channel performance, maps customer journeys, optimizes
engagement strategies, and provides campaign attribution insights.

Version 1.1.0 adds five demo-grounded customer-journey operations with
deterministic records, exact record-key lookup, and a simulated handoff receipt.
No external system is changed, and all legacy operations remain unchanged.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/omnichannel_engagement",
    "version": "1.1.1",
    "display_name": "Omnichannel Engagement Agent",
    "description": "Analyzes channel performance, customer journeys, and campaign attribution from built-in demo engagement data.",
    "author": "AIBAST",
    "tags": ["omnichannel", "engagement", "journey", "attribution", "campaign", "b2c"],
    "category": "b2c_sales",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# ---------------------------------------------------------------------------
# Synthetic domain data
# ---------------------------------------------------------------------------

CHANNELS = {
    "email": {"sessions_30d": 145000, "conversions_30d": 4350, "revenue_30d": 870000, "cost_30d": 12500, "avg_order_value": 200.0, "bounce_rate": 18.5},
    "sms": {"sessions_30d": 62000, "conversions_30d": 1860, "revenue_30d": 325500, "cost_30d": 8200, "avg_order_value": 175.0, "bounce_rate": 5.2},
    "social_media": {"sessions_30d": 230000, "conversions_30d": 2760, "revenue_30d": 552000, "cost_30d": 45000, "avg_order_value": 200.0, "bounce_rate": 42.0},
    "web_organic": {"sessions_30d": 480000, "conversions_30d": 9600, "revenue_30d": 1920000, "cost_30d": 18000, "avg_order_value": 200.0, "bounce_rate": 35.0},
    "web_paid": {"sessions_30d": 185000, "conversions_30d": 5550, "revenue_30d": 1110000, "cost_30d": 95000, "avg_order_value": 200.0, "bounce_rate": 28.0},
    "mobile_app": {"sessions_30d": 310000, "conversions_30d": 12400, "revenue_30d": 2480000, "cost_30d": 22000, "avg_order_value": 200.0, "bounce_rate": 12.0},
    "in_store": {"sessions_30d": 95000, "conversions_30d": 28500, "revenue_30d": 5700000, "cost_30d": 180000, "avg_order_value": 200.0, "bounce_rate": 0},
}

CUSTOMER_JOURNEYS = {
    "journey_discovery": {
        "name": "Discovery to Purchase",
        "touchpoints": ["social_media_ad", "website_browse", "email_signup", "email_promo", "website_purchase"],
        "avg_days": 14,
        "conversion_rate": 3.2,
        "avg_touchpoints": 5,
    },
    "journey_repeat": {
        "name": "Repeat Purchase",
        "touchpoints": ["email_promo", "mobile_app_browse", "mobile_app_purchase"],
        "avg_days": 3,
        "conversion_rate": 18.5,
        "avg_touchpoints": 3,
    },
    "journey_winback": {
        "name": "Win-Back",
        "touchpoints": ["email_winback", "sms_offer", "website_browse", "website_purchase"],
        "avg_days": 21,
        "conversion_rate": 8.4,
        "avg_touchpoints": 4,
    },
    "journey_impulse": {
        "name": "Impulse Purchase",
        "touchpoints": ["social_media_ad", "website_purchase"],
        "avg_days": 0,
        "conversion_rate": 1.8,
        "avg_touchpoints": 2,
    },
}

CAMPAIGN_RESULTS = {
    "CAMP-301": {"name": "Spring Collection Launch", "channel": "email", "sent": 250000, "opens": 62500, "clicks": 18750, "conversions": 2250, "revenue": 450000, "cost": 5000},
    "CAMP-302": {"name": "Flash Sale — 48 Hours", "channel": "sms", "sent": 120000, "opens": 115200, "clicks": 24000, "conversions": 3600, "revenue": 540000, "cost": 6000},
    "CAMP-303": {"name": "Influencer Partnership", "channel": "social_media", "sent": 0, "opens": 0, "clicks": 85000, "conversions": 1700, "revenue": 340000, "cost": 35000},
    "CAMP-304": {"name": "Google Shopping Ads", "channel": "web_paid", "sent": 0, "opens": 0, "clicks": 45000, "conversions": 2700, "revenue": 540000, "cost": 42000},
    "CAMP-305": {"name": "App Push — Loyalty Members", "channel": "mobile_app", "sent": 85000, "opens": 42500, "clicks": 17000, "conversions": 5100, "revenue": 765000, "cost": 2000},
}

EVIDENCE_ACTIONS = {
    "unified_customer_journey": {
        "title": "Unified Customer Journey",
        "write": False,
        "records": [
            {"record_id": "JOURNEY-SARAH", "customer": "Sarah Mitchell", "history": "8 channels over 3 days", "cart": "$289", "status": "currently holding", "mood": "likely frustrated"},
            {"record_id": "TOUCH-MOBILE", "day": "3 days ago", "channel": "mobile app", "action": "checkout started", "issue": "payment declined"},
            {"record_id": "TOUCH-CHAT", "day": "2 days ago", "channel": "chat", "action": "sizing question", "issue": "disconnected"},
            {"record_id": "TOUCH-EMAIL", "day": "yesterday", "channel": "email", "action": "cart reminder", "issue": "no action"},
            {"record_id": "TOUCH-PHONE", "day": "today", "channel": "phone", "action": "support call", "issue": "currently holding"},
        ],
        "context": "Channel preferences over 30 days: mobile app 12 interactions, website 8, chat 3 with frustration.",
    },
    "friction_resolution": {
        "title": "Journey Friction Resolution",
        "write": False,
        "records": [
            {"record_id": "ISSUE-SIZING", "issue": "Alpine Parka sizing guidance", "status": "unanswered", "impact": "blocking purchase", "resolution": "runs one size small"},
            {"record_id": "ISSUE-COLOR", "issue": "navy availability", "status": "unanswered", "impact": "blocking purchase", "resolution": "navy in stock, S-XL"},
            {"record_id": "ISSUE-PAYMENT", "issue": "card declined", "status": "needs resolution", "impact": "checkout stalled", "resolution": "offer payment alternatives"},
        ],
        "context": "The disconnected chat left two questions unresolved after 18 minutes; the prepared opening apologizes and continues without asking Sarah to repeat context.",
    },
    "channel_recommendation": {
        "title": "Channel and Timing Recommendation",
        "write": False,
        "records": [
            {"record_id": "CHANNEL-PHONE", "channel": "Phone", "engagement": "resolve now", "use": "current payment issue"},
            {"record_id": "CHANNEL-SMS", "channel": "SMS", "engagement": "76% response", "use": "confirmation and order status"},
            {"record_id": "CHANNEL-PUSH", "channel": "Mobile push", "engagement": "82% open", "use": "promotions at 10 AM"},
            {"record_id": "CHANNEL-EMAIL", "channel": "Email", "engagement": "34% open", "use": "avoid for urgency"},
        ],
        "context": "Sarah responds to urgency, values fit guidance, and peaks from 7-9 PM; avoid chat in the short term.",
    },
    "proactive_engagement_plan": {
        "title": "Proactive Engagement and Recovery Plan",
        "write": False,
        "records": [
            {"record_id": "PLAN-AFTER-PURCHASE", "timing": "order through day 7", "actions": "SMS size guide, delivery-day mobile styling tips, in-app review request"},
            {"record_id": "PLAN-UPCOMING", "timing": "3 days through 8 weeks", "actions": "accessory bundle, birthday bonus, spring preview"},
            {"record_id": "PLAN-WIN-BACK", "timing": "hour 1 through day 5", "actions": "SMS reminder, low-stock push, 10% code, personal stylist call"},
        ],
        "context": "Avoid email campaigns, chat offers, and generic messages because they conflict with observed channel history.",
    },
    "handoff_package": {
        "title": "Seamless Service Handoff Package",
        "write": True,
        "records": [
            {"record_id": "HANDOFF-SARAH", "customer": "Sarah Mitchell", "tier": "Gold", "ltv": "$2,400", "purchase": "Alpine Parka", "blockers": "sizing resolved; payment in progress", "mood": "previously frustrated, now engaged"},
            {"record_id": "HANDOFF-CONTEXT", "payments": "card decline and alternatives", "styling": "size preferences and past purchases", "pickup": "location and inventory", "loyalty": "points and tier benefits"},
        ],
        "context": "The transfer script says complete history is shared so the customer need not repeat anything; preview includes CRM note, cart link, and conversation summary.",
    },
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _evidence_action(action, **kwargs):
    """Render a demo-grounded action with exact record-key lookup."""
    spec = EVIDENCE_ACTIONS[action]
    user_input = str(kwargs.get("user_input", ""))
    normalized = {
        "".join(ch for ch in token.upper() if ch.isalnum())
        for token in user_input.split()
    }
    records = spec["records"]
    if user_input:
        records = [
            record for record in records
            if "".join(ch for ch in record["record_id"].upper() if ch.isalnum()) in normalized
        ]
        if not records:
            return "No exact `record_id` match was found; no substitute customer or touchpoint was used."
    lines = [
        f"## {spec['title']}",
        f"\n{spec['context']}",
        "\nDeterministic evidence-backed records:",
    ]
    for record in records:
        lines.append("- " + "; ".join(f"{key}: {value}" for key, value in record.items()))
    if spec["write"]:
        receipt_key = records[0]["record_id"] if len(records) == 1 else "BATCH"
        lines.extend([
            "\n### Simulated Write Receipt",
            f"- receipt_id: SIM-HANDOFF-{receipt_key}",
            "- status: simulated",
            "- target_systems: Dynamics 365 and Microsoft Teams",
            "- No external system changed; CRM notes, routing, and transfer context are preview-only.",
        ])
    else:
        lines.append("\n_Read-only analysis; no external system changed._")
    return "\n".join(lines)

def _channel_conversion_rate(channel):
    """Calculate conversion rate for a channel."""
    if channel["sessions_30d"] == 0:
        return 0
    return round((channel["conversions_30d"] / channel["sessions_30d"]) * 100, 2)


def _channel_roas(channel):
    """Calculate return on ad spend."""
    if channel["cost_30d"] == 0:
        return 0
    return round(channel["revenue_30d"] / channel["cost_30d"], 2)


def _campaign_roi(campaign):
    """Calculate campaign ROI."""
    if campaign["cost"] == 0:
        return 0
    return round(((campaign["revenue"] - campaign["cost"]) / campaign["cost"]) * 100, 1)


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class OmnichannelEngagementAgent(BasicAgent):
    """Omnichannel engagement analytics agent."""

    def __init__(self):
        self.name = "OmnichannelEngagementAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Omnichannel Engagement Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "channel_performance",
                            "journey_analysis",
                            "engagement_optimization",
                            "campaign_attribution",
                            "unified_customer_journey",
                            "friction_resolution",
                            "channel_recommendation",
                            "proactive_engagement_plan",
                            "handoff_package",
                        ],
                    },
                    "channel": {"type": "string"},
                    "campaign_id": {"type": "string"},
                    "user_input": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "channel_performance")
        dispatch = {
            "channel_performance": self._channel_performance,
            "journey_analysis": self._journey_analysis,
            "engagement_optimization": self._engagement_optimization,
            "campaign_attribution": self._campaign_attribution,
            "unified_customer_journey": self._evidence_action,
            "friction_resolution": self._evidence_action,
            "channel_recommendation": self._evidence_action,
            "proactive_engagement_plan": self._evidence_action,
            "handoff_package": self._evidence_action,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        if operation in EVIDENCE_ACTIONS:
            return handler(operation, **kwargs)
        return handler(**kwargs)

    def _evidence_action(self, action, **kwargs) -> str:
        return _evidence_action(action, **kwargs)

    def _channel_performance(self, **kwargs) -> str:
        total_revenue = sum(c["revenue_30d"] for c in CHANNELS.values())
        total_conversions = sum(c["conversions_30d"] for c in CHANNELS.values())
        lines = ["# Channel Performance (30-Day)\n"]
        lines.append(f"**Total Revenue:** ${total_revenue:,.0f}")
        lines.append(f"**Total Conversions:** {total_conversions:,}\n")
        lines.append("| Channel | Sessions | Conversions | CVR | Revenue | Cost | ROAS |")
        lines.append("|---|---|---|---|---|---|---|")
        for ch_name, ch in CHANNELS.items():
            cvr = _channel_conversion_rate(ch)
            roas = _channel_roas(ch)
            lines.append(
                f"| {ch_name.replace('_', ' ').title()} | {ch['sessions_30d']:,} | {ch['conversions_30d']:,} "
                f"| {cvr}% | ${ch['revenue_30d']:,.0f} | ${ch['cost_30d']:,.0f} | {roas}x |"
            )
        lines.append("\n## Revenue Share by Channel\n")
        for ch_name, ch in CHANNELS.items():
            share = round((ch["revenue_30d"] / total_revenue) * 100, 1) if total_revenue else 0
            lines.append(f"- {ch_name.replace('_', ' ').title()}: {share}%")
        return "\n".join(lines)

    def _journey_analysis(self, **kwargs) -> str:
        lines = ["# Customer Journey Analysis\n"]
        for jid, j in CUSTOMER_JOURNEYS.items():
            lines.append(f"## {j['name']}\n")
            lines.append(f"- **Avg Duration:** {j['avg_days']} days")
            lines.append(f"- **Avg Touchpoints:** {j['avg_touchpoints']}")
            lines.append(f"- **Conversion Rate:** {j['conversion_rate']}%\n")
            lines.append("**Touchpoint Sequence:**\n")
            for i, tp in enumerate(j["touchpoints"], 1):
                arrow = " -> " if i < len(j["touchpoints"]) else ""
                lines.append(f"{i}. {tp.replace('_', ' ').title()}{arrow}")
            lines.append("")
        lines.append("## Journey Optimization Opportunities\n")
        lines.append("- **Discovery:** Shorten path by enabling social commerce checkout")
        lines.append("- **Repeat:** Leverage push notifications for faster re-engagement")
        lines.append("- **Win-Back:** Test earlier SMS touchpoint (day 7 vs day 14)")
        lines.append("- **Impulse:** Optimize social ad creative for direct conversion")
        return "\n".join(lines)

    def _engagement_optimization(self, **kwargs) -> str:
        lines = ["# Engagement Optimization Report\n"]
        lines.append("## Channel Efficiency Ranking\n")
        ranked = []
        for ch_name, ch in CHANNELS.items():
            roas = _channel_roas(ch)
            cvr = _channel_conversion_rate(ch)
            ranked.append((ch_name, roas, cvr, ch))
        ranked.sort(key=lambda x: x[1], reverse=True)
        lines.append("| Rank | Channel | ROAS | CVR | Bounce Rate | Recommendation |")
        lines.append("|---|---|---|---|---|---|")
        for i, (name, roas, cvr, ch) in enumerate(ranked, 1):
            if roas > 50:
                rec = "Scale investment"
            elif roas > 10:
                rec = "Optimize spend"
            else:
                rec = "Review ROI"
            lines.append(
                f"| {i} | {name.replace('_', ' ').title()} | {roas}x | {cvr}% "
                f"| {ch['bounce_rate']}% | {rec} |"
            )
        total_cost = sum(c["cost_30d"] for c in CHANNELS.values())
        total_rev = sum(c["revenue_30d"] for c in CHANNELS.values())
        lines.append(f"\n**Total Marketing Spend:** ${total_cost:,.0f}")
        lines.append(f"**Total Revenue:** ${total_rev:,.0f}")
        lines.append(f"**Blended ROAS:** {round(total_rev / total_cost, 1)}x")
        lines.append("\n## Optimization Actions\n")
        lines.append("1. Shift 10% of social media budget to mobile app push campaigns")
        lines.append("2. Implement progressive profiling on email signups")
        lines.append("3. Launch A/B test on checkout flow for web paid traffic")
        lines.append("4. Increase SMS frequency for high-value customer segment")
        return "\n".join(lines)

    def _campaign_attribution(self, **kwargs) -> str:
        lines = ["# Campaign Attribution Report\n"]
        lines.append("| Campaign | Channel | Conversions | Revenue | Cost | ROI |")
        lines.append("|---|---|---|---|---|---|")
        total_rev = 0
        total_cost = 0
        for cid, c in CAMPAIGN_RESULTS.items():
            roi = _campaign_roi(c)
            total_rev += c["revenue"]
            total_cost += c["cost"]
            lines.append(
                f"| {c['name']} ({cid}) | {c['channel'].replace('_', ' ').title()} "
                f"| {c['conversions']:,} | ${c['revenue']:,.0f} | ${c['cost']:,.0f} | {roi}% |"
            )
        lines.append(f"\n**Total Campaign Revenue:** ${total_rev:,.0f}")
        lines.append(f"**Total Campaign Cost:** ${total_cost:,.0f}")
        overall_roi = round(((total_rev - total_cost) / total_cost) * 100, 1) if total_cost else 0
        lines.append(f"**Overall Campaign ROI:** {overall_roi}%")
        lines.append("\n## Campaign Detail\n")
        for cid, c in CAMPAIGN_RESULTS.items():
            lines.append(f"### {c['name']} ({cid})\n")
            if c["sent"] > 0:
                open_rate = round((c["opens"] / c["sent"]) * 100, 1)
                ctr = round((c["clicks"] / c["sent"]) * 100, 1)
                lines.append(f"- Sent: {c['sent']:,} | Opens: {c['opens']:,} ({open_rate}%) | Clicks: {c['clicks']:,} ({ctr}%)")
            else:
                lines.append(f"- Clicks: {c['clicks']:,}")
            conv_rate = round((c["conversions"] / c["clicks"]) * 100, 1) if c["clicks"] else 0
            lines.append(f"- Conversions: {c['conversions']:,} ({conv_rate}% click-to-conversion)")
            lines.append(f"- Revenue: ${c['revenue']:,.0f} | Cost: ${c['cost']:,.0f}\n")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = OmnichannelEngagementAgent()
    print(agent.perform(operation="channel_performance"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="journey_analysis"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="engagement_optimization"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="campaign_attribution"))
