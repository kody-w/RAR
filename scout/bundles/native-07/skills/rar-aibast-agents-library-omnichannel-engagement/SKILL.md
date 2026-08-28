---
name: "rar-aibast-agents-library-omnichannel-engagement"
description: "Analyzes channel mix, journeys, and campaign attribution from a live simulated Dynamics 365 tenant, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/omnichannel_engagement", "rar_sha256": "8e9c11585b63da13bd5ed59343bed3e9ee9a1d32c5b34d89e4daa7087f3b3d12", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["omnichannel", "engagement", "journey", "attribution", "campaign", "b2c"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/omnichannel_engagement`. The original RAPP
agent is preserved byte-for-byte in `omnichannel_engagement_agent.py` and in the RCI capsule.

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

Omnichannel Engagement Agent — a template you are meant to mutate.

Analyzes channel performance, maps customer journeys, optimizes
engagement strategies, and provides campaign attribution insights.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live engagement records over real HTTP from
     the globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Cases (Phone / Email / Web origin) and email activities become the
     live channel mix — e.g. the Web-origin case "Disputed card
     transaction under investigation" for Bluegrass Credit Union.
     Try: perform(operation="channel_performance")
  2. No network? Everything falls back to the embedded demo layer below
     (CHANNELS / CUSTOMER_JOURNEYS / CAMPAIGN_RESULTS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     OMNICHANNEL_ENGAGEMENT_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your CDP/martech stack),
     or replace _fetch_collection() with your own API client. Fields the
     rest of the file needs are listed in _normalize_live_channels() —
     everything else keeps working untouched. Fields marked "enrichment
     seam" in the output (revenue, cost, conversions) are where you wire
     your commerce and ad platforms.

OPERATIONS
  channel_performance | journey_analysis | engagement_optimization
  | campaign_attribution | unified_customer_journey | friction_resolution
  | channel_recommendation | proactive_engagement_plan | handoff_package
  kwargs: operation (required), channel, campaign_id, user_input

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "campaign_id": {
      "type": "string"
    },
    "channel": {
      "type": "string"
    },
    "operation": {
      "enum": [
        "channel_performance",
        "journey_analysis",
        "engagement_optimization",
        "campaign_attribution",
        "unified_customer_journey",
        "friction_resolution",
        "channel_recommendation",
        "proactive_engagement_plan",
        "handoff_package"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `omnichannel_engagement_agent.py` and embedded as the fenced Python below (sha256 8e9c11585b63da13…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `omnichannel_engagement_agent.py` first:

```bash
python3 omnichannel_engagement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 omnichannel_engagement_agent.py   # or on stdin
python3 omnichannel_engagement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Omnichannel Engagement Agent — a template you are meant to mutate.

Analyzes channel performance, maps customer journeys, optimizes
engagement strategies, and provides campaign attribution insights.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live engagement records over real HTTP from
     the globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Cases (Phone / Email / Web origin) and email activities become the
     live channel mix — e.g. the Web-origin case "Disputed card
     transaction under investigation" for Bluegrass Credit Union.
     Try: perform(operation="channel_performance")
  2. No network? Everything falls back to the embedded demo layer below
     (CHANNELS / CUSTOMER_JOURNEYS / CAMPAIGN_RESULTS) — the agent never
     crashes offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     OMNICHANNEL_ENGAGEMENT_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or JSON exported from your CDP/martech stack),
     or replace _fetch_collection() with your own API client. Fields the
     rest of the file needs are listed in _normalize_live_channels() —
     everything else keeps working untouched. Fields marked "enrichment
     seam" in the output (revenue, cost, conversions) are where you wire
     your commerce and ad platforms.

OPERATIONS
  channel_performance | journey_analysis | engagement_optimization
  | campaign_attribution | unified_customer_journey | friction_resolution
  | channel_recommendation | proactive_engagement_plan | handoff_package
  kwargs: operation (required), channel, campaign_id, user_input
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))
from basic_agent import BasicAgent
import json
import urllib.request

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/omnichannel_engagement",
    "version": "1.2.0",
    "display_name": "Omnichannel Engagement Agent",
    "description": "Analyzes channel mix, journeys, and campaign attribution from a live simulated Dynamics 365 tenant, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["omnichannel", "engagement", "journey", "attribution", "campaign", "b2c"],
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
#   export OMNICHANNEL_ENGAGEMENT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CDP / martech client.
# Downstream code only needs the shape produced by
# _normalize_live_channels().
# ---------------------------------------------------------------------------

DATA_SOURCE_URL = os.environ.get(
    "OMNICHANNEL_ENGAGEMENT_DATA_URL",
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


_CASE_ORIGIN_LABELS = {1: "phone", 2: "email", 3: "web"}


def _normalize_live_channels(incidents, emails):
    """Project live tenant activity onto the channel shape this agent
    uses. THIS is the contract your replacement data source must meet —
    a dict of channel-name -> metrics dicts with these keys. None means
    'not available from CRM alone' and the renderers label it as an
    enrichment seam. In this template a case's origin (Phone/Email/Web)
    is reinterpreted as its engagement channel and email activities are
    email-channel touchpoints; interactions stand in for sessions."""
    channels = {}
    for inc in incidents:
        label = _CASE_ORIGIN_LABELS.get(inc.get("caseorigincode"), "other")
        ch = channels.setdefault(label, {
            "interactions_30d": 0,   # real count of live records
            "open_items": 0,          # real count (statecode == 0)
            "resolved_items": 0,      # real count (statecode == 1)
            "conversions_30d": None,  # enrichment seam — wire your commerce platform
            "revenue_30d": None,      # enrichment seam
            "cost_30d": None,         # enrichment seam — wire your ad platforms
        })
        ch["interactions_30d"] += 1
        if inc.get("statecode") == 0:
            ch["open_items"] += 1
        elif inc.get("statecode") == 1:
            ch["resolved_items"] += 1
    if emails:
        ch = channels.setdefault("email", {
            "interactions_30d": 0, "open_items": 0, "resolved_items": 0,
            "conversions_30d": None, "revenue_30d": None, "cost_30d": None,
        })
        ch["interactions_30d"] += len(emails)
    return channels


def _na(value, fmt="{:,}"):
    """None = the CRM alone can't know this (enrichment seam); 0 is real."""
    return "n/a — enrichment seam" if value is None else fmt.format(value)


# ---------------------------------------------------------------------------
# EMBEDDED DEMO LAYER (offline fallback)
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
        incidents = _fetch_collection("incidents")
        if incidents:
            emails = _fetch_collection("emails")
            live = _normalize_live_channels(incidents, emails)
            total = sum(c["interactions_30d"] for c in live.values())
            lines = ["# Channel Performance (live tenant data)\n"]
            lines.append(f"**Total Interactions:** {total:,} (live cases + email activities)")
            lines.append("**Total Revenue:** n/a — enrichment seam (wire your commerce platform)\n")
            lines.append("| Channel | Interactions | Open | Resolved | Revenue | Cost |")
            lines.append("|---|---|---|---|---|---|")
            for name, ch in sorted(live.items(), key=lambda kv: -kv[1]["interactions_30d"]):
                lines.append(
                    f"| {name.replace('_', ' ').title()} | {ch['interactions_30d']:,} "
                    f"| {ch['open_items']:,} | {ch['resolved_items']:,} "
                    f"| {_na(ch['revenue_30d'])} | {_na(ch['cost_30d'])} |"
                )
            lines.append("\n## Interaction Share by Channel\n")
            for name, ch in sorted(live.items(), key=lambda kv: -kv[1]["interactions_30d"]):
                share = round((ch["interactions_30d"] / total) * 100, 1) if total else 0
                lines.append(f"- {name.replace('_', ' ').title()}: {share}%")
            lines.append("\n_Source: live Static Dynamics 365 tenant (incidents + emails). "
                         "Case origin is reinterpreted as engagement channel._")
            return "\n".join(lines)

        total_revenue = sum(c["revenue_30d"] for c in CHANNELS.values())
        total_conversions = sum(c["conversions_30d"] for c in CHANNELS.values())
        lines = ["# Channel Performance (30-Day, embedded demo data — offline)\n"]
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
    print("=" * 60)
    print("LIVE TENANT CHANNEL MIX (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="channel_performance"))
    print()
    print("=" * 60)
    print("EMBEDDED DEMO ANALYTICS (works offline)")
    print(agent.perform(operation="campaign_attribution"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="journey_analysis"))
    print("\n" + "=" * 60 + "\n")
    print(agent.perform(operation="engagement_optimization"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
