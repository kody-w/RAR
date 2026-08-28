"""
Customer 360 & Speech Agent — a template you are meant to mutate.

Serves unified customer profiles, interaction history, sentiment
analysis, and next-best-action recommendations across all channels.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live accounts, orders, and cases over real
     HTTP from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="customer_profile",
                  customer_id="Blue Heron Stationery")
     — the 360 view is assembled from that account's real CRM record,
     sales orders, and support cases.
  2. No network? Everything falls back to the embedded demo layer below
     (CUSTOMER_PROFILES / INTERACTION_HISTORY) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     CUSTOMER_360_SPEECH_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from your commerce/CDP stack), or
     replace _fetch_collection() with your own client. The dict shape the
     rest of the file needs is documented in _normalize_live_customer().
     Segment, channel preferences, and speech sentiment are enrichment
     seams — wire your CDP / speech analytics there; sentiment and
     next-best-action ops stay simulated until you do.

OPERATIONS
  customer_profile | interaction_history | sentiment_analysis
  | next_best_action
  kwargs: operation (required), customer_id (embedded ID like "C360-001"
  or a live tenant account name)
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/customer_360_speech",
    "version": "1.1.0",
    "display_name": "Customer 360 & Speech Agent",
    "description": "Builds customer 360 profiles from live accounts, orders, and cases in a simulated Dynamics 365 tenant, with an embedded offline demo fallback.",
    "author": "AIBAST",
    "tags": ["customer-360", "speech", "sentiment", "omnichannel", "profile", "b2c"],
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
#   export CUSTOMER_360_SPEECH_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM/CDP client. Downstream
# code only needs the fields produced by _normalize_live_customer().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "CUSTOMER_360_SPEECH_DATA_URL",
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


def _normalize_live_customer(account, orders, incidents):
    """Project a Dynamics account (+ its orders and cases) onto the shape
    this agent uses. THIS is the contract your replacement data source
    must meet — a dict with these keys. None means 'not knowable from the
    CRM alone' and the renderers label it an enrichment seam (segment,
    preferences, and speech sentiment come from your CDP / speech
    analytics)."""
    name = account.get("name", "Unknown")
    acct_orders = [o for o in orders if o.get("customeridname") == name]
    acct_cases = [i for i in incidents if i.get("customeridname") == name]
    order_dates = sorted(str(o.get("createdon") or "")[:10] for o in acct_orders)
    return {
        "name": name,
        "email": account.get("emailaddress1", ""),
        "phone": account.get("telephone1", ""),
        "city": f"{account.get('address1_city', '?')}, {account.get('address1_stateorprovince', '?')}",
        "lifetime_value": sum(float(o.get("totalamount") or 0) for o in acct_orders),
        "total_orders": len(acct_orders),
        "last_order": order_dates[-1] if order_dates else "n/a",
        "open_cases": sum(1 for i in acct_cases if i.get("statecode") == 0),
        "resolved_cases": sum(1 for i in acct_cases if i.get("statecode") == 1),
        "segment": None,      # enrichment seam — wire your CDP
        "preferences": None,  # enrichment seam
        "sentiment": None,    # enrichment seam — wire speech analytics
        "_live": True,
    }


def _live_customer_roster():
    """Name-keyed dict of live tenant customers; {} when offline."""
    accounts = _fetch_collection("accounts")
    if not accounts:
        return {}
    orders = _fetch_collection("salesorders")
    incidents = _fetch_collection("incidents")
    return {
        a["name"].lower(): _normalize_live_customer(a, orders, incidents)
        for a in accounts
        if a.get("name")
    }


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
# ---------------------------------------------------------------------------

CUSTOMER_PROFILES = {
    "C360-001": {
        "name": "Jessica Alvarez",
        "email": "j.alvarez@example.com",
        "phone": "(555) 234-5678",
        "segment": "premium",
        "lifetime_value": 12450,
        "member_since": "2019-06-15",
        "preferred_channel": "mobile_app",
        "preferences": {"categories": ["electronics", "home"], "communication": "email", "language": "en"},
        "purchase_history_summary": {"total_orders": 47, "avg_order_value": 264.89, "last_order": "2025-02-28", "return_rate": 4.2},
    },
    "C360-002": {
        "name": "Brian O'Connell",
        "email": "b.oconnell@example.com",
        "phone": "(555) 876-1234",
        "segment": "standard",
        "lifetime_value": 3280,
        "member_since": "2022-01-10",
        "preferred_channel": "website",
        "preferences": {"categories": ["sports", "outdoor"], "communication": "sms", "language": "en"},
        "purchase_history_summary": {"total_orders": 15, "avg_order_value": 218.67, "last_order": "2025-01-15", "return_rate": 8.0},
    },
    "C360-003": {
        "name": "Mei Lin Zhang",
        "email": "m.zhang@example.com",
        "phone": "(555) 445-9012",
        "segment": "at_risk",
        "lifetime_value": 5890,
        "member_since": "2020-09-22",
        "preferred_channel": "phone",
        "preferences": {"categories": ["fashion", "beauty"], "communication": "email", "language": "en"},
        "purchase_history_summary": {"total_orders": 28, "avg_order_value": 210.36, "last_order": "2024-10-05", "return_rate": 12.5},
    },
}

INTERACTION_HISTORY = {
    "C360-001": [
        {"date": "2025-03-05", "channel": "mobile_app", "type": "purchase", "details": "Order #ORD-88421 — Wireless Speaker", "sentiment": "positive", "agent": None},
        {"date": "2025-02-20", "channel": "chat", "type": "inquiry", "details": "Asked about loyalty points redemption", "sentiment": "positive", "agent": "ChatBot"},
        {"date": "2025-02-10", "channel": "email", "type": "campaign_click", "details": "Clicked spring sale email — viewed 3 products", "sentiment": "neutral", "agent": None},
        {"date": "2025-01-28", "channel": "phone", "type": "support", "details": "Delivery delay on order #ORD-87910", "sentiment": "negative", "agent": "Agent_Kelly"},
    ],
    "C360-002": [
        {"date": "2025-01-15", "channel": "website", "type": "purchase", "details": "Order #ORD-85220 — Hiking Boots", "sentiment": "positive", "agent": None},
        {"date": "2025-01-02", "channel": "email", "type": "campaign_open", "details": "Opened New Year promotion email", "sentiment": "neutral", "agent": None},
    ],
    "C360-003": [
        {"date": "2024-12-15", "channel": "phone", "type": "complaint", "details": "Wrong size shipped on order #ORD-84100 — requested refund", "sentiment": "negative", "agent": "Agent_Marcus"},
        {"date": "2024-10-05", "channel": "website", "type": "purchase", "details": "Order #ORD-82450 — Fall collection items", "sentiment": "neutral", "agent": None},
        {"date": "2024-09-20", "channel": "chat", "type": "support", "details": "Sizing guidance for dresses", "sentiment": "positive", "agent": "ChatBot"},
        {"date": "2024-08-14", "channel": "phone", "type": "complaint", "details": "Late delivery — order arrived 5 days after estimate", "sentiment": "negative", "agent": "Agent_Kelly"},
    ],
}

NEXT_BEST_ACTIONS = {
    "premium_engagement": {"action": "Send personalized VIP preview of new collection", "channel": "email", "timing": "immediate", "expected_conversion": 22.5},
    "win_back": {"action": "Send win-back offer with 20% discount and free shipping", "channel": "email", "timing": "immediate", "expected_conversion": 15.0},
    "loyalty_nurture": {"action": "Remind of loyalty points balance and redemption options", "channel": "mobile_push", "timing": "next_3_days", "expected_conversion": 18.0},
    "service_recovery": {"action": "Proactive outreach from manager with apology and store credit", "channel": "phone", "timing": "immediate", "expected_conversion": 35.0},
    "cross_sell": {"action": "Recommend complementary products based on purchase history", "channel": "email", "timing": "next_7_days", "expected_conversion": 12.0},
    "reactivation_sms": {"action": "Send SMS with limited-time exclusive offer", "channel": "sms", "timing": "next_3_days", "expected_conversion": 10.5},
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _overall_sentiment(customer_id):
    """Calculate overall sentiment score from interactions."""
    interactions = INTERACTION_HISTORY.get(customer_id, [])
    if not interactions:
        return "neutral", 0.0
    scores = {"positive": 1, "neutral": 0, "negative": -1}
    total = sum(scores.get(i["sentiment"], 0) for i in interactions)
    avg = total / len(interactions)
    if avg > 0.3:
        return "positive", round(avg, 2)
    elif avg < -0.3:
        return "negative", round(avg, 2)
    return "neutral", round(avg, 2)


def _recommend_action(profile, sentiment_label):
    """Determine best next action based on segment and sentiment."""
    if sentiment_label == "negative" and profile["segment"] == "at_risk":
        return "service_recovery"
    if profile["segment"] == "premium":
        return "premium_engagement"
    if profile["segment"] == "at_risk":
        return "win_back"
    return "cross_sell"


# ---------------------------------------------------------------------------
# Agent class
# ---------------------------------------------------------------------------

class Customer360SpeechAgent(BasicAgent):
    """Customer 360 and speech analytics agent."""

    def __init__(self):
        self.name = "Customer360SpeechAgent"
        self.metadata = {
            "name": self.name,
            "display_name": "Customer 360 & Speech Agent",
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "customer_profile",
                            "interaction_history",
                            "sentiment_analysis",
                            "next_best_action",
                        ],
                    },
                    "customer_id": {"type": "string"},
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        operation = kwargs.get("operation", "customer_profile")
        dispatch = {
            "customer_profile": self._customer_profile,
            "interaction_history": self._interaction_history,
            "sentiment_analysis": self._sentiment_analysis,
            "next_best_action": self._next_best_action,
        }
        handler = dispatch.get(operation)
        if not handler:
            return f"**Error:** Unknown operation `{operation}`."
        return handler(**kwargs)

    def _customer_profile(self, **kwargs) -> str:
        customer_id = kwargs.get("customer_id")

        # LIVE tenant lookup: a live account name (or fragment) as customer_id
        if customer_id and customer_id not in CUSTOMER_PROFILES:
            roster = _live_customer_roster()
            q = customer_id.lower().strip()
            match = next((c for key, c in roster.items() if q in key or key in q), None)
            if match:
                return "\n".join([
                    f"# Customer Profile: {match['name']} — LIVE (Static Dynamics 365 tenant)\n",
                    f"- **Email:** {match['email']}",
                    f"- **Phone:** {match['phone']}",
                    f"- **Location:** {match['city']}",
                    f"- **Segment:** n/a — enrichment seam (wire your CDP)",
                    f"- **Overall Sentiment:** n/a — enrichment seam (wire speech analytics)\n",
                    "## Purchase Summary (from live sales orders)\n",
                    f"- Total Orders: {match['total_orders']}",
                    f"- Lifetime Value: ${match['lifetime_value']:,.2f}",
                    f"- Last Order: {match['last_order']}\n",
                    "## Service Summary (from live cases)\n",
                    f"- Open Cases: {match['open_cases']}",
                    f"- Resolved Cases: {match['resolved_cases']}",
                ])

        # LIVE overview when no specific embedded customer requested
        if not customer_id:
            roster = _live_customer_roster()
            if roster:
                lines = ["# Customer 360 Overview — LIVE (Static Dynamics 365 tenant)\n"]
                lines.append("| Customer | LTV | Orders | Last Order | Open Cases | Sentiment |")
                lines.append("|---|---|---|---|---|---|")
                for c in sorted(roster.values(), key=lambda x: -x["lifetime_value"]):
                    lines.append(
                        f"| {c['name']} | ${c['lifetime_value']:,.2f} | {c['total_orders']} "
                        f"| {c['last_order']} | {c['open_cases']} | n/a — enrichment seam |"
                    )
                total_ltv = sum(c["lifetime_value"] for c in roster.values())
                lines.append(f"\n**Total Customer LTV (live orders):** ${total_ltv:,.2f}")
                lines.append("\nSegment and sentiment stay n/a until you wire your "
                             "CDP / speech analytics at the LIVE DATA SEAM.")
                return "\n".join(lines)

        if customer_id and customer_id in CUSTOMER_PROFILES:
            p = CUSTOMER_PROFILES[customer_id]
            ph = p["purchase_history_summary"]
            sentiment, score = _overall_sentiment(customer_id)
            lines = [f"# Customer Profile: {p['name']} ({customer_id})\n"]
            lines.append(f"- **Email:** {p['email']}")
            lines.append(f"- **Phone:** {p['phone']}")
            lines.append(f"- **Segment:** {p['segment'].replace('_', ' ').title()}")
            lines.append(f"- **Lifetime Value:** ${p['lifetime_value']:,.0f}")
            lines.append(f"- **Member Since:** {p['member_since']}")
            lines.append(f"- **Preferred Channel:** {p['preferred_channel'].replace('_', ' ').title()}")
            lines.append(f"- **Overall Sentiment:** {sentiment.title()} ({score})\n")
            lines.append("## Purchase Summary\n")
            lines.append(f"- Total Orders: {ph['total_orders']}")
            lines.append(f"- Avg Order Value: ${ph['avg_order_value']:,.2f}")
            lines.append(f"- Last Order: {ph['last_order']}")
            lines.append(f"- Return Rate: {ph['return_rate']}%\n")
            lines.append("## Preferences\n")
            lines.append(f"- Categories: {', '.join(p['preferences']['categories'])}")
            lines.append(f"- Communication: {p['preferences']['communication'].upper()}")
            return "\n".join(lines)

        lines = ["# Customer 360 Overview\n"]
        lines.append("| ID | Name | Segment | LTV | Orders | Last Order | Sentiment |")
        lines.append("|---|---|---|---|---|---|---|")
        for cid, p in CUSTOMER_PROFILES.items():
            sentiment, _ = _overall_sentiment(cid)
            ph = p["purchase_history_summary"]
            lines.append(
                f"| {cid} | {p['name']} | {p['segment'].replace('_', ' ').title()} "
                f"| ${p['lifetime_value']:,.0f} | {ph['total_orders']} | {ph['last_order']} | {sentiment.title()} |"
            )
        total_ltv = sum(p["lifetime_value"] for p in CUSTOMER_PROFILES.values())
        lines.append(f"\n**Total Customer LTV:** ${total_ltv:,.0f}")
        return "\n".join(lines)

    def _interaction_history(self, **kwargs) -> str:
        customer_id = kwargs.get("customer_id", "C360-001")
        profile = CUSTOMER_PROFILES.get(customer_id, list(CUSTOMER_PROFILES.values())[0])
        interactions = INTERACTION_HISTORY.get(customer_id, [])
        lines = [f"# Interaction History: {profile['name']}\n"]
        if interactions:
            lines.append("| Date | Channel | Type | Details | Sentiment | Agent |")
            lines.append("|---|---|---|---|---|---|")
            for i in interactions:
                agent = i["agent"] or "Self-Service"
                lines.append(
                    f"| {i['date']} | {i['channel'].replace('_', ' ').title()} | {i['type'].replace('_', ' ').title()} "
                    f"| {i['details']} | {i['sentiment'].title()} | {agent} |"
                )
        else:
            lines.append("No interaction history available.")
        lines.append(f"\n**Total Interactions:** {len(interactions)}")
        return "\n".join(lines)

    def _sentiment_analysis(self, **kwargs) -> str:
        lines = ["# Sentiment Analysis Report\n"]
        lines.append("| Customer | Segment | Sentiment | Score | Interactions | Negative Count |")
        lines.append("|---|---|---|---|---|---|")
        for cid, p in CUSTOMER_PROFILES.items():
            sentiment, score = _overall_sentiment(cid)
            interactions = INTERACTION_HISTORY.get(cid, [])
            neg_count = sum(1 for i in interactions if i["sentiment"] == "negative")
            lines.append(
                f"| {p['name']} ({cid}) | {p['segment'].replace('_', ' ').title()} "
                f"| {sentiment.title()} | {score} | {len(interactions)} | {neg_count} |"
            )
        lines.append("\n## At-Risk Customers (Negative Sentiment)\n")
        for cid, p in CUSTOMER_PROFILES.items():
            sentiment, score = _overall_sentiment(cid)
            if sentiment == "negative":
                interactions = INTERACTION_HISTORY.get(cid, [])
                neg_interactions = [i for i in interactions if i["sentiment"] == "negative"]
                lines.append(f"### {p['name']} ({cid})\n")
                for i in neg_interactions:
                    lines.append(f"- [{i['date']}] {i['channel']}: {i['details']}")
                lines.append("")
        return "\n".join(lines)

    def _next_best_action(self, **kwargs) -> str:
        lines = ["# Next Best Action Recommendations\n"]
        for cid, p in CUSTOMER_PROFILES.items():
            sentiment, score = _overall_sentiment(cid)
            action_key = _recommend_action(p, sentiment)
            action = NEXT_BEST_ACTIONS[action_key]
            lines.append(f"## {p['name']} ({cid})\n")
            lines.append(f"- **Segment:** {p['segment'].replace('_', ' ').title()}")
            lines.append(f"- **Sentiment:** {sentiment.title()} ({score})")
            lines.append(f"- **Recommended Action:** {action['action']}")
            lines.append(f"- **Channel:** {action['channel'].replace('_', ' ').title()}")
            lines.append(f"- **Timing:** {action['timing'].replace('_', ' ').title()}")
            lines.append(f"- **Expected Conversion:** {action['expected_conversion']}%\n")
        lines.append("## Action Library\n")
        lines.append("| Action | Channel | Timing | Conversion |")
        lines.append("|---|---|---|---|")
        for aid, a in NEXT_BEST_ACTIONS.items():
            lines.append(f"| {a['action']} | {a['channel'].replace('_', ' ').title()} | {a['timing'].replace('_', ' ').title()} | {a['expected_conversion']}% |")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    agent = Customer360SpeechAgent()
    print("=" * 80)
    print("LIVE TENANT OVERVIEW (fetched over HTTP; embedded demo offline)")
    print(agent.perform(operation="customer_profile"))
    print("\n" + "=" * 80 + "\n")
    print("LIVE TENANT CUSTOMER (falls back to demo default offline)")
    print(agent.perform(operation="customer_profile", customer_id="Blue Heron Stationery"))
    print("\n" + "=" * 80 + "\n")
    print("EMBEDDED DEMO CUSTOMER (works offline)")
    print(agent.perform(operation="customer_profile", customer_id="C360-001"))
    print("\n" + "=" * 80 + "\n")
    print(agent.perform(operation="sentiment_analysis"))
