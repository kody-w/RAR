---
name: "rar-aibast-agents-library-customer-360-speech"
description: "Builds customer 360 profiles from live accounts, orders, and cases in a simulated Dynamics 365 tenant, with an embedded offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/customer_360_speech", "rar_sha256": "6ba087b8885c52ce347b6692679ee5a8e75b6d4a205615cbe3f0f35531b9d1db", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["customer-360", "speech", "sentiment", "omnichannel", "profile", "b2c"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/customer_360_speech`. The original RAPP
agent is preserved byte-for-byte in `customer_360_speech_agent.py` and in the RCI capsule.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "customer_id": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "customer_profile",
        "interaction_history",
        "sentiment_analysis",
        "next_best_action"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_360_speech_agent.py` and embedded as the fenced Python below (sha256 6ba087b8885c52ce…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_360_speech_agent.py` first:

```bash
python3 customer_360_speech_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 customer_360_speech_agent.py   # or on stdin
python3 customer_360_speech_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
