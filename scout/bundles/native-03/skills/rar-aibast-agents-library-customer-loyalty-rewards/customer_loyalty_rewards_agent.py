"""
Customer Loyalty & Rewards Agent — a template you are meant to mutate.

Manages loyalty program dashboards, points summaries, reward
recommendations, tier analysis, and churn-risk win-back campaigns for
customer retention.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live customer records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Live contacts become loyalty members and their account's sales
     orders become spend, so tiers are computed from real order totals.
     Try: perform(operation="points_summary", member_id="Theo Dalton")
  2. No network? Everything falls back to the embedded demo layer below
     (LOYALTY_MEMBERS / TIER_STRUCTURE / REDEMPTION_CATALOG) — the agent
     never crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CUSTOMER_LOYALTY_REWARDS_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your commerce platform), or
     replace _fetch_collection() with calls into your own API. Fields the
     rest of the file needs are listed in _normalize_live_member() —
     everything else keeps working untouched. Fields marked "enrichment
     seam" in the output (points balances, engagement scores) are where
     you wire your actual loyalty platform.

OPERATIONS
  loyalty_dashboard | points_summary | reward_recommendations
  | tier_analysis | churn_risk_analysis | at_risk_profiles
  | win_back_offers | campaign_launch | program_optimization
  | program_summary
  kwargs: operation (required), member_id, user_input
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/customer_loyalty_rewards",
    "version": "1.2.0",
    "display_name": "Customer Loyalty & Rewards Agent",
    "description": "Builds loyalty dashboards, tier analysis, and win-back offers from a live simulated Dynamics 365 tenant, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["loyalty", "rewards", "points", "retention", "tier", "b2c"],
    "category": "b2c_sales",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

# ---------------------------------------------------------------------------
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export CUSTOMER_LOYALTY_REWARDS_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your loyalty platform client.
# Downstream code only needs the fields produced by
# _normalize_live_member().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "CUSTOMER_LOYALTY_REWARDS_DATA_URL",
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


def _normalize_live_member(contact, orders):
    """Project a Dynamics contact record onto the loyalty member shape
    this agent uses. THIS is the contract your replacement data source
    must meet — a dict with these keys. None means 'not available from
    CRM alone' and the renderers label it as an enrichment seam. In this
    template a CRM contact is reinterpreted as a loyalty member and the
    sales orders of their parent account are their spend."""
    account = contact.get("parentcustomeridname", "")
    spend = sum(
        float(o.get("totalamount") or 0)
        for o in orders
        if o.get("customeridname") == account
    )
    if spend >= 6000:
        tier = "platinum"
    elif spend >= 3000:
        tier = "gold"
    elif spend >= 1000:
        tier = "silver"
    else:
        tier = "bronze"
    return {
        "name": contact.get("fullname", "Unknown"),
        "tier": tier,                     # computed from real order totals
        "points_balance": None,           # enrichment seam — wire your loyalty platform
        "points_earned_ytd": None,        # enrichment seam
        "points_redeemed_ytd": None,      # enrichment seam
        "member_since": str(contact.get("createdon", ""))[:10],
        "total_spend_ytd": int(spend),    # real zero when the account has no orders
        "engagement_score": None,         # enrichment seam — wire your engagement analytics
        "birthday_month": None,           # enrichment seam
        "preferred_rewards": [],          # enrichment seam — wire preference data
        "_live": True,
        "_account": account,
        "_email": contact.get("emailaddress1", ""),
    }


def _live_members():
    """name-keyed dict of live tenant loyalty members; {} when offline."""
    contacts = _fetch_collection("contacts")
    if not contacts:
        return {}
    orders = _fetch_collection("salesorders")
    return {
        c["fullname"].lower(): _normalize_live_member(c, orders)
        for c in contacts
        if c.get("fullname")
    }


def _pts(value):
    """None = the CRM alone can't know this (enrichment seam); 0 is real."""
    return "n/a — enrichment seam" if value is None else f"{value:,}"


def _pts_dollars(value):
    return "n/a — enrichment seam" if value is None else f"${_points_value(value):,.2f}"


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
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
        live = _live_members()
        if live:
            members = sorted(live.values(), key=lambda m: -m["total_spend_ytd"])
            total_spend = sum(m["total_spend_ytd"] for m in members)
            shown = members[:10]
            lines = ["# Loyalty Program Dashboard (live tenant data)\n"]
            lines.append(f"**Total Members:** {len(members)} (from live CRM contacts)")
            lines.append("**Total Points Outstanding:** n/a — enrichment seam (wire your loyalty platform)")
            lines.append(f"**Total Member Spend YTD:** ${total_spend:,.0f} (from live sales orders)\n")
            lines.append(f"Top {len(shown)} members by spend:\n")
            lines.append("| Member | Tier | Points | Spend YTD | Engagement | Since |")
            lines.append("|---|---|---|---|---|---|")
            for m in shown:
                lines.append(
                    f"| {m['name']} ({m['_account']}) | {m['tier'].title()} | {_pts(m['points_balance'])} "
                    f"| ${m['total_spend_ytd']:,.0f} | {_pts(m['engagement_score'])} | {m['member_since']} |"
                )
            lines.append("\n## Tier Distribution (computed from live order totals)\n")
            tier_counts = {}
            for m in members:
                tier_counts[m["tier"]] = tier_counts.get(m["tier"], 0) + 1
            for tier in ["platinum", "gold", "silver", "bronze"]:
                lines.append(f"- {tier.title()}: {tier_counts.get(tier, 0)}")
            lines.append("\n_Source: live Static Dynamics 365 tenant (contacts + salesorders)._")
            return "\n".join(lines)

        total_members = len(LOYALTY_MEMBERS)
        total_points = sum(m["points_balance"] for m in LOYALTY_MEMBERS.values())
        total_spend = sum(m["total_spend_ytd"] for m in LOYALTY_MEMBERS.values())
        lines = ["# Loyalty Program Dashboard (embedded demo data — offline)\n"]
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

        if member_id:
            m = _live_members().get(str(member_id).lower().strip())
            if m:
                lines = [f"# Points Summary: {m['name']} (live tenant record)\n"]
                lines.append(f"- **Account:** {m['_account']}")
                lines.append(f"- **Tier:** {m['tier'].title()} (computed from live order totals)")
                lines.append(f"- **Points Balance:** {_pts(m['points_balance'])}")
                lines.append(f"- **Earned YTD:** {_pts(m['points_earned_ytd'])}")
                lines.append(f"- **Redeemed YTD:** {_pts(m['points_redeemed_ytd'])}")
                lines.append(f"- **Spend YTD:** ${m['total_spend_ytd']:,.0f} (real zero means no orders on record)")
                lines.append(f"- **Member Since:** {m['member_since']}")
                lines.append(f"- **Multiplier:** {TIER_STRUCTURE[m['tier']]['points_multiplier']}x\n")
                lines.append("## Earning Opportunities\n")
                for act in ENGAGEMENT_ACTIVITIES:
                    lines.append(f"- **{act['activity']}:** {act['points']}")
                lines.append("\n_Source: live Static Dynamics 365 tenant (contacts + salesorders)._")
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
    print("=" * 60)
    print("EMBEDDED DEMO MEMBER (works offline)")
    print(agent.perform(operation="points_summary", member_id="LM-10001"))
    print()
    print("=" * 60)
    print("LIVE TENANT MEMBER (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="points_summary", member_id="Theo Dalton"))
    print()
    print("=" * 60)
    print(agent.perform(operation="loyalty_dashboard"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="tier_analysis"))
