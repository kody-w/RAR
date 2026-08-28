---
name: "rar-aibast-agents-library-customer-loyalty-rewards"
description: "Builds loyalty dashboards, tier analysis, and win-back offers from a live simulated Dynamics 365 tenant, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/customer_loyalty_rewards", "rar_sha256": "ec9d6c53dd139186d4835c37dd678deba5380bf3172619876eb2c9d5446bb1cd", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["loyalty", "rewards", "points", "retention", "tier", "b2c"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/customer_loyalty_rewards`. The original RAPP
agent is preserved byte-for-byte in `customer_loyalty_rewards_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "member_id": {
      "type": "string"
    },
    "operation": {
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
        "program_summary"
      ],
      "type": "string"
    },
    "user_input": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_loyalty_rewards_agent.py` and embedded as the fenced Python below (sha256 ec9d6c53dd139186…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_loyalty_rewards_agent.py` first:

```bash
python3 customer_loyalty_rewards_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 customer_loyalty_rewards_agent.py   # or on stdin
python3 customer_loyalty_rewards_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
