"""
Customer Loyalty & Rewards Agent — B2C Sales Stack

Manages loyalty program dashboards, points summaries, reward
recommendations, and tier analysis for customer retention.

Version 1.1.0 adds six demo-grounded loyalty operations with deterministic
records, exact record-key lookup, and simulated campaign/Teams receipts. No
external system is changed, and all legacy operations remain unchanged.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/customer_loyalty_rewards",
    "version": "1.1.1",
    "display_name": "Customer Loyalty & Rewards Agent",
    "description": "Reports loyalty dashboards, points, reward recommendations, and churn-risk offers from built-in demo program data.",
    "author": "AIBAST",
    "tags": ["loyalty", "rewards", "points", "retention", "tier", "b2c"],
    "category": "b2c_sales",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# ---------------------------------------------------------------------------
# Synthetic domain data
# ---------------------------------------------------------------------------

LOYALTY_MEMBERS = {
    "LM-10001": {
        "name": "Katherine Brooks",
        "tier": "platinum",
        "points_balance": 48250,
        "points_earned_ytd": 12400,
        "points_redeemed_ytd": 8000,
        "member_since": "2018-03-15",
        "total_spend_ytd": 6200,
        "engagement_score": 92,
        "birthday_month": 5,
        "preferred_rewards": ["travel", "dining"],
    },
    "LM-10002": {
        "name": "Antonio Vasquez",
        "tier": "gold",
        "points_balance": 22100,
        "points_earned_ytd": 6800,
        "points_redeemed_ytd": 2500,
        "member_since": "2020-08-22",
        "total_spend_ytd": 3400,
        "engagement_score": 75,
        "birthday_month": 11,
        "preferred_rewards": ["merchandise", "gift_cards"],
    },
    "LM-10003": {
        "name": "Rachel Nguyen",
        "tier": "silver",
        "points_balance": 8450,
        "points_earned_ytd": 3200,
        "points_redeemed_ytd": 0,
        "member_since": "2023-01-10",
        "total_spend_ytd": 1600,
        "engagement_score": 58,
        "birthday_month": 3,
        "preferred_rewards": ["discounts"],
    },
    "LM-10004": {
        "name": "Derek Washington",
        "tier": "bronze",
        "points_balance": 2100,
        "points_earned_ytd": 900,
        "points_redeemed_ytd": 0,
        "member_since": "2024-06-05",
        "total_spend_ytd": 450,
        "engagement_score": 32,
        "birthday_month": 8,
        "preferred_rewards": ["discounts", "free_shipping"],
    },
}

TIER_STRUCTURE = {
    "bronze": {"min_spend": 0, "points_multiplier": 1.0, "perks": ["Birthday bonus points", "Member-only sales access"], "next_tier": "silver", "spend_to_next": 1000},
    "silver": {"min_spend": 1000, "points_multiplier": 1.25, "perks": ["Bronze perks", "Free standard shipping", "Early access to new products"], "next_tier": "gold", "spend_to_next": 3000},
    "gold": {"min_spend": 3000, "points_multiplier": 1.5, "perks": ["Silver perks", "Free express shipping", "Exclusive gold events", "Annual gift"], "next_tier": "platinum", "spend_to_next": 6000},
    "platinum": {"min_spend": 6000, "points_multiplier": 2.0, "perks": ["Gold perks", "Personal shopping advisor", "Free returns", "VIP lounge access", "Quarterly bonus"], "next_tier": None, "spend_to_next": 0},
}

REDEMPTION_CATALOG = {
    "travel_voucher_500": {"name": "$500 Travel Voucher", "points_cost": 25000, "category": "travel", "value": 500},
    "dining_card_100": {"name": "$100 Dining Gift Card", "points_cost": 5000, "category": "dining", "value": 100},
    "merch_headphones": {"name": "Premium Wireless Headphones", "points_cost": 15000, "category": "merchandise", "value": 249},
    "gift_card_50": {"name": "$50 Store Gift Card", "points_cost": 2500, "category": "gift_cards", "value": 50},
    "discount_20pct": {"name": "20% Off Next Purchase", "points_cost": 3000, "category": "discounts", "value": 0},
    "free_shipping_3mo": {"name": "Free Shipping for 3 Months", "points_cost": 1500, "category": "free_shipping", "value": 30},
}

ENGAGEMENT_ACTIVITIES = [
    {"activity": "Purchase", "points": "2 per $1 spent", "frequency": "per_transaction"},
    {"activity": "Product Review", "points": "100 bonus", "frequency": "per_review"},
    {"activity": "Referral Signup", "points": "500 bonus", "frequency": "per_referral"},
    {"activity": "Birthday", "points": "Double points for birthday month", "frequency": "annual"},
    {"activity": "Social Share", "points": "50 bonus", "frequency": "per_share"},
    {"activity": "App Download", "points": "250 one-time bonus", "frequency": "once"},
]

EVIDENCE_ACTIONS = {
    "churn_risk_analysis": {
        "title": "Member Churn-Risk Analysis",
        "write": False,
        "records": [
            {"record_id": "SEG-ENGAGED", "segment": "Engaged", "members": "124K", "churn_risk": "5%"},
            {"record_id": "SEG-ACTIVE", "segment": "Active", "members": "198K", "churn_risk": "12%"},
            {"record_id": "SEG-AT-RISK", "segment": "At-risk", "members": "34K", "churn_risk": "68%"},
            {"record_id": "SEG-DORMANT", "segment": "Dormant", "members": "94K", "churn_risk": "89%"},
        ],
        "context": "450K members analyzed; 34K at risk with $2.1M in unredeemed points; $840K expires in 30 days. Signals include 60+ days without purchase, high balances without redemption, sudden disengagement, and browse-without-buy.",
    },
    "at_risk_profiles": {
        "title": "Top At-Risk Member Profiles",
        "write": False,
        "records": [
            {"record_id": "MEM-LINDA-M", "member": "Linda M.", "points": 12400, "last_purchase": "72 days", "risk": "94%", "trigger": "favorite designer-accessories brand on sale; 8K points expire in 21 days"},
            {"record_id": "MEM-KEVIN-R", "member": "Kevin R.", "points": 8900, "last_purchase": "65 days", "risk": "88%", "trigger": "high balance and recent disengagement"},
            {"record_id": "MEM-SARAH-T", "member": "Sarah T.", "points": 7200, "last_purchase": "81 days", "risk": "86%", "trigger": "browse-without-buy pattern"},
        ],
        "context": "The three highlighted members represent $48K in annual value and warrant personalized outreach.",
    },
    "win_back_offers": {
        "title": "Personalized Win-Back Offers",
        "write": False,
        "records": [
            {"record_id": "OFFER-LINDA-M", "audience": "Linda M.", "offer": "favorite bags 40% off, double points, 8K-point expiry reminder"},
            {"record_id": "OFFER-HIGH-VALUE", "audience": "High-value (8,400)", "offer": "VIP early access and 3X points for 14 days"},
            {"record_id": "OFFER-EXPIRY", "audience": "Point expiry (12,000)", "offer": "25% bonus when points are redeemed this week"},
            {"record_id": "OFFER-LAPSED", "audience": "Lapsed browsers (13,600)", "offer": "viewed items, 20% off, and free shipping"},
        ],
        "context": "Offers are tailored from member interests, preferences, activity patterns, and point-expiry context.",
    },
    "campaign_launch": {
        "title": "Loyalty Campaign Launch and Forecast",
        "write": True,
        "records": [
            {"record_id": "LOY-CAMP-HIGH-VALUE", "campaign": "High-value win-back", "members": 8400, "status": "sent"},
            {"record_id": "LOY-CAMP-EXPIRY", "campaign": "Point expiry alert", "members": 12000, "status": "sent"},
            {"record_id": "LOY-CAMP-LAPSED", "campaign": "Lapsed browser", "members": 13600, "status": "active"},
        ],
        "context": "Expected 14-day results: 24% re-engagement, $489,600 revenue, $640K liability reduction, $1.4M LTV protected, and 58:1 ROI on $8,400 cost.",
    },
    "program_optimization": {
        "title": "Loyalty Program Optimization",
        "write": False,
        "records": [
            {"record_id": "LOY-OPT-EXPIRY", "improvement": "Dynamic point expiry", "impact": "+$340K/year", "priority": "high"},
            {"record_id": "LOY-OPT-TIER", "improvement": "Tier advancement alerts", "impact": "+18% engagement", "priority": "high"},
            {"record_id": "LOY-OPT-REWARDS", "improvement": "Personalized rewards", "impact": "+24% redemption", "priority": "high"},
        ],
        "context": "Quick win: alert members within 200 points of Gold; rolling expiry with activity extension targets a 40% dormancy reduction.",
    },
    "program_summary": {
        "title": "Loyalty Optimization Summary",
        "write": True,
        "records": [
            {"record_id": "LOY-SUMMARY-001", "members_analyzed": "450K", "at_risk": "34K ($2.1M points)", "campaigns": "3 segments / 34K members", "expected_revenue": "$489,600", "ltv_protected": "$1.4M", "roi": "58:1"},
        ],
        "context": "Next steps: monitor daily, implement tier alerts this week, and plan a personalized-rewards pilot. The recap is prepared for Microsoft Teams sharing.",
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
            return "No exact `record_id` match was found; no substitute member or segment was used."
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
            f"- receipt_id: SIM-LOYALTY-{receipt_key}",
            "- status: simulated",
            "- target_systems: Dynamics 365, Outlook, and Microsoft Teams",
            "- No external system changed; campaign activation and recap sharing are preview-only.",
        ])
    else:
        lines.append("\n_Read-only analysis; no external system changed._")
    return "\n".join(lines)

def _points_value(points):
    """Convert points to dollar value (1 point = $0.02)."""
    return round(points * 0.02, 2)


def _tier_progress(member):
    """Calculate progress toward next tier."""
    tier_info = TIER_STRUCTURE.get(member["tier"], {})
    if tier_info["next_tier"] is None:
        return 100.0
    spend_needed = tier_info["spend_to_next"]
    if spend_needed == 0:
        return 100.0
    current_spend = member["total_spend_ytd"]
    return min(100.0, round((current_spend / spend_needed) * 100, 1))


def _recommended_rewards(member):
    """Recommend rewards based on preferences and points balance."""
    recs = []
    for rid, reward in REDEMPTION_CATALOG.items():
        if reward["category"] in member["preferred_rewards"] and reward["points_cost"] <= member["points_balance"]:
            recs.append((rid, reward))
    return recs


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class CustomerLoyaltyRewardsAgent(BasicAgent):
    """Customer loyalty and rewards management agent."""

    def __init__(self):
        self.name = "CustomerLoyaltyRewardsAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Customer Loyalty & Rewards Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "loyalty_dashboard",
                            "points_summary",
                            "reward_recommendations",
                            "tier_analysis",
                            "churn_risk_analysis",
                            "at_risk_profiles",
                            "win_back_offers",
                            "campaign_launch",
                            "program_optimization",
                            "program_summary",
                        ],
                    },
                    "member_id": {"type": "string"},
                    "user_input": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "loyalty_dashboard")
        dispatch = {
            "loyalty_dashboard": self._loyalty_dashboard,
            "points_summary": self._points_summary,
            "reward_recommendations": self._reward_recommendations,
            "tier_analysis": self._tier_analysis,
            "churn_risk_analysis": self._evidence_action,
            "at_risk_profiles": self._evidence_action,
            "win_back_offers": self._evidence_action,
            "campaign_launch": self._evidence_action,
            "program_optimization": self._evidence_action,
            "program_summary": self._evidence_action,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        if operation in EVIDENCE_ACTIONS:
            return handler(operation, **kwargs)
        return handler(**kwargs)

    def _evidence_action(self, action, **kwargs) -> str:
        return _evidence_action(action, **kwargs)

    def _loyalty_dashboard(self, **kwargs) -> str:
        total_members = len(LOYALTY_MEMBERS)
        total_points = sum(m["points_balance"] for m in LOYALTY_MEMBERS.values())
        total_spend = sum(m["total_spend_ytd"] for m in LOYALTY_MEMBERS.values())
        lines = ["# Loyalty Program Dashboard\n"]
        lines.append(f"**Total Members:** {total_members}")
        lines.append(f"**Total Points Outstanding:** {total_points:,} (${_points_value(total_points):,.2f})")
        lines.append(f"**Total Member Spend YTD:** ${total_spend:,.0f}\n")
        lines.append("| Member | Tier | Points | Spend YTD | Engagement | Since |")
        lines.append("|---|---|---|---|---|---|")
        for mid, m in LOYALTY_MEMBERS.items():
            lines.append(
                f"| {m['name']} ({mid}) | {m['tier'].title()} | {m['points_balance']:,} "
                f"| ${m['total_spend_ytd']:,.0f} | {m['engagement_score']} | {m['member_since']} |"
            )
        lines.append("\n## Tier Distribution\n")
        tier_counts = {}
        for m in LOYALTY_MEMBERS.values():
            tier_counts[m["tier"]] = tier_counts.get(m["tier"], 0) + 1
        for tier in ["platinum", "gold", "silver", "bronze"]:
            lines.append(f"- {tier.title()}: {tier_counts.get(tier, 0)}")
        return "\n".join(lines)

    def _points_summary(self, **kwargs) -> str:
        member_id = kwargs.get("member_id")
        if member_id and member_id in LOYALTY_MEMBERS:
            m = LOYALTY_MEMBERS[member_id]
            lines = [f"# Points Summary: {m['name']}\n"]
            lines.append(f"- **Tier:** {m['tier'].title()}")
            lines.append(f"- **Points Balance:** {m['points_balance']:,} (${_points_value(m['points_balance']):,.2f})")
            lines.append(f"- **Earned YTD:** {m['points_earned_ytd']:,}")
            lines.append(f"- **Redeemed YTD:** {m['points_redeemed_ytd']:,}")
            lines.append(f"- **Multiplier:** {TIER_STRUCTURE[m['tier']]['points_multiplier']}x\n")
            lines.append("## Earning Opportunities\n")
            for act in ENGAGEMENT_ACTIVITIES:
                lines.append(f"- **{act['activity']}:** {act['points']}")
            return "\n".join(lines)

        lines = ["# Points Summary — All Members\n"]
        lines.append("| Member | Tier | Balance | Earned YTD | Redeemed YTD | Value |")
        lines.append("|---|---|---|---|---|---|")
        for mid, m in LOYALTY_MEMBERS.items():
            lines.append(
                f"| {m['name']} ({mid}) | {m['tier'].title()} | {m['points_balance']:,} "
                f"| {m['points_earned_ytd']:,} | {m['points_redeemed_ytd']:,} | ${_points_value(m['points_balance']):,.2f} |"
            )
        return "\n".join(lines)

    def _reward_recommendations(self, **kwargs) -> str:
        lines = ["# Reward Recommendations\n"]
        for mid, m in LOYALTY_MEMBERS.items():
            recs = _recommended_rewards(m)
            lines.append(f"## {m['name']} ({mid}) — {m['points_balance']:,} points\n")
            if recs:
                lines.append("| Reward | Points Cost | Category | Value |")
                lines.append("|---|---|---|---|")
                for rid, reward in recs:
                    val = f"${reward['value']}" if reward["value"] else "Discount"
                    lines.append(f"| {reward['name']} | {reward['points_cost']:,} | {reward['category'].replace('_', ' ').title()} | {val} |")
            else:
                lines.append("No matching rewards available at current points balance.")
            lines.append("")
        lines.append("## Full Redemption Catalog\n")
        lines.append("| Reward | Points | Category | Value |")
        lines.append("|---|---|---|---|")
        for rid, r in REDEMPTION_CATALOG.items():
            val = f"${r['value']}" if r["value"] else "Discount"
            lines.append(f"| {r['name']} | {r['points_cost']:,} | {r['category'].replace('_', ' ').title()} | {val} |")
        return "\n".join(lines)

    def _tier_analysis(self, **kwargs) -> str:
        lines = ["# Tier Analysis\n"]
        lines.append("## Tier Structure\n")
        lines.append("| Tier | Min Spend | Multiplier | Key Perks |")
        lines.append("|---|---|---|---|")
        for tier, info in TIER_STRUCTURE.items():
            perks = "; ".join(info["perks"][:2])
            lines.append(f"| {tier.title()} | ${info['min_spend']:,.0f} | {info['points_multiplier']}x | {perks} |")
        lines.append("\n## Member Tier Progress\n")
        for mid, m in LOYALTY_MEMBERS.items():
            progress = _tier_progress(m)
            tier_info = TIER_STRUCTURE[m["tier"]]
            lines.append(f"### {m['name']} ({mid}) — {m['tier'].title()}\n")
            lines.append(f"- Spend YTD: ${m['total_spend_ytd']:,.0f}")
            lines.append(f"- Engagement Score: {m['engagement_score']}")
            if tier_info["next_tier"]:
                remaining = max(0, tier_info["spend_to_next"] - m["total_spend_ytd"])
                lines.append(f"- Progress to {tier_info['next_tier'].title()}: {progress}%")
                lines.append(f"- Spend Remaining: ${remaining:,.0f}")
            else:
                lines.append(f"- Status: Top Tier Achieved")
            lines.append("")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = CustomerLoyaltyRewardsAgent()
    print(agent.perform(operation="loyalty_dashboard"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="points_summary", member_id="LM-10001"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="reward_recommendations"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="tier_analysis"))
