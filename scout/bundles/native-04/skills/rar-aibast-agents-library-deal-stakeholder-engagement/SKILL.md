---
name: "rar-aibast-agents-library-deal-stakeholder-engagement"
description: "Maps buying committees for live deals from a simulated Dynamics 365 tenant using real CRM contacts, with an embedded offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/deal_stakeholder_engagement", "rar_sha256": "9c279e91ec1743d61866206591ba726b313f28ecd623674cc95314c31db9fb9c", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["b2b", "sales", "stakeholder-engagement", "deal-progression", "relationships"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/deal_stakeholder_engagement`. The original RAPP
agent is preserved byte-for-byte in `stakeholder_engagement_agent.py` and in the RCI capsule.

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

Stakeholder Engagement Agent — a template you are meant to mutate.

Scores stakeholder engagement, maps buying committees, generates targeted
engagement plans, and analyzes sentiment so no deal stays single-threaded.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities and contacts over real
     HTTP from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="engagement_score") — live open deals such as
     "Cedar Hollow Printing — Managed print fleet refresh" are mapped to
     their real CRM contacts (e.g. Theo Dalton, Print Services Lead).
  2. No network? Everything falls back to the embedded demo layer below
     (_STAKEHOLDERS / _SENTIMENT_SIGNALS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     DEAL_STAKEHOLDER_ENGAGEMENT_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON you export from Salesforce/HubSpot),
     or replace _fetch_collection() with your own client. The dict shape
     the rest of the file needs is documented in
     _normalize_live_stakeholders(). Email/meeting counts and sentiment
     are enrichment seams — wire Gong / email analytics there.

OPERATIONS
  engagement_score | relationship_map | engagement_plan | sentiment_analysis
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
        "engagement_score",
        "relationship_map",
        "engagement_plan",
        "sentiment_analysis"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `stakeholder_engagement_agent.py` and embedded as the fenced Python below (sha256 9c279e91ec1743d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `stakeholder_engagement_agent.py` first:

```bash
python3 stakeholder_engagement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 stakeholder_engagement_agent.py   # or on stdin
python3 stakeholder_engagement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Stakeholder Engagement Agent — a template you are meant to mutate.

Scores stakeholder engagement, maps buying committees, generates targeted
engagement plans, and analyzes sentiment so no deal stays single-threaded.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM opportunities and contacts over real
     HTTP from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="engagement_score") — live open deals such as
     "Cedar Hollow Printing — Managed print fleet refresh" are mapped to
     their real CRM contacts (e.g. Theo Dalton, Print Services Lead).
  2. No network? Everything falls back to the embedded demo layer below
     (_STAKEHOLDERS / _SENTIMENT_SIGNALS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     DEAL_STAKEHOLDER_ENGAGEMENT_DATA_URL to any OData-shaped endpoint
     (your real Dynamics org, or JSON you export from Salesforce/HubSpot),
     or replace _fetch_collection() with your own client. The dict shape
     the rest of the file needs is documented in
     _normalize_live_stakeholders(). Email/meeting counts and sentiment
     are enrichment seams — wire Gong / email analytics there.

OPERATIONS
  engagement_score | relationship_map | engagement_plan | sentiment_analysis
  kwargs: operation (required)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request

# ===================================================================
# RAPP AGENT MANIFEST
# ===================================================================
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/deal_stakeholder_engagement",
    "version": "1.1.0",
    "display_name": "Stakeholder Engagement",
    "description": "Maps buying committees for live deals from a simulated Dynamics 365 tenant using real CRM contacts, with an embedded offline demo fallback.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "stakeholder-engagement", "deal-progression", "relationships"],
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
#   export DEAL_STAKEHOLDER_ENGAGEMENT_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the shape produced by _normalize_live_stakeholders().
# ===================================================================

DATA_SOURCE_URL = os.environ.get(
    "DEAL_STAKEHOLDER_ENGAGEMENT_DATA_URL",
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


def _normalize_live_stakeholders(opp, contacts):
    """Project a Dynamics opportunity + its account's contacts onto the
    shape this agent uses. THIS is the contract your replacement data
    source must meet — a deal dict with a "contacts" list. None means
    'not knowable from the CRM alone' and the renderers label it an
    enrichment seam (wire Gong / email analytics for engagement counts
    and sentiment)."""
    account = opp.get("parentaccountidname", "Unknown")
    deal_contacts = [
        {
            "name": c.get("fullname", "Unknown"),
            "title": c.get("jobtitle", "Unknown"),
            "role": None,           # enrichment seam — classify your committee
            "emails": None,         # enrichment seam — wire email analytics
            "meetings": None,       # enrichment seam
            "last_touch_days": None,  # enrichment seam
            "sentiment": None,      # enrichment seam — wire Gong
            "influence": None,      # enrichment seam
            "support_level": None,  # enrichment seam
            "email": c.get("emailaddress1", ""),
        }
        for c in contacts
        if c.get("parentcustomeridname") == account
    ]
    return {
        "deal_id": str(opp.get("opportunityid", ""))[:8],
        "name": opp.get("name", "Unknown"),
        "account": account,
        "value": int(float(opp.get("estimatedvalue") or 0)),
        "stage": _LIVE_STAGE_MAP.get(opp.get("stepname"), "Qualification"),
        "owner": opp.get("owneridname", ""),
        "contacts": deal_contacts,
        "_live": True,
    }


def _live_deals_with_contacts():
    """Live open opportunities joined to their account contacts; [] offline."""
    opps = [o for o in _fetch_collection("opportunities") if o.get("statecode") == 0]
    if not opps:
        return []
    contacts = _fetch_collection("contacts")
    return [_normalize_live_stakeholders(o, contacts) for o in opps]


# ===================================================================
# EMBEDDED DEMO LAYER (offline fallback)
# ===================================================================

_STAKEHOLDERS = {
    "TechCorp Industries": {
        "deal_id": "OPP-001", "value": 890000, "stage": "Proposal", "owner": "Mike Chen",
        "contacts": [
            {"name": "Mark Reynolds", "title": "VP of IT", "role": "Economic Buyer",
             "emails": 8, "meetings": 2, "last_touch_days": 18, "sentiment": "neutral",
             "influence": "high", "support_level": "unknown"},
            {"name": "Jennifer Walsh", "title": "Director of Engineering", "role": "Technical Evaluator",
             "emails": 12, "meetings": 3, "last_touch_days": 22, "sentiment": "positive",
             "influence": "medium", "support_level": "supporter"},
            {"name": "Robert Kim", "title": "CIO", "role": "Executive Sponsor",
             "emails": 2, "meetings": 0, "last_touch_days": 45, "sentiment": "unknown",
             "influence": "very_high", "support_level": "unknown"},
            {"name": "Amanda Chen", "title": "Procurement Manager", "role": "Procurement",
             "emails": 4, "meetings": 1, "last_touch_days": 12, "sentiment": "neutral",
             "influence": "medium", "support_level": "neutral"},
            {"name": "David Park", "title": "IT Manager", "role": "End User",
             "emails": 6, "meetings": 2, "last_touch_days": 8, "sentiment": "positive",
             "influence": "low", "support_level": "champion"},
        ],
    },
    "Global Manufacturing": {
        "deal_id": "OPP-002", "value": 720000, "stage": "Negotiation", "owner": "Lisa Torres",
        "contacts": [
            {"name": "Rachel Green", "title": "Dir. Operations", "role": "Champion",
             "emails": 18, "meetings": 5, "last_touch_days": 5, "sentiment": "frustrated",
             "influence": "high", "support_level": "champion"},
            {"name": "Tom Bennett", "title": "CFO", "role": "Economic Buyer",
             "emails": 4, "meetings": 1, "last_touch_days": 14, "sentiment": "cautious",
             "influence": "very_high", "support_level": "neutral"},
            {"name": "Lisa Park", "title": "Legal Counsel", "role": "Legal",
             "emails": 10, "meetings": 2, "last_touch_days": 3, "sentiment": "neutral",
             "influence": "medium", "support_level": "blocker"},
            {"name": "James Miller", "title": "VP Manufacturing", "role": "Executive Sponsor",
             "emails": 3, "meetings": 1, "last_touch_days": 20, "sentiment": "positive",
             "influence": "very_high", "support_level": "supporter"},
        ],
    },
    "Apex Financial": {
        "deal_id": "OPP-003", "value": 580000, "stage": "Discovery", "owner": "James Park",
        "contacts": [
            {"name": "David Liu", "title": "CTO", "role": "Technical Buyer",
             "emails": 5, "meetings": 1, "last_touch_days": 12, "sentiment": "cautious",
             "influence": "very_high", "support_level": "neutral"},
            {"name": "Sarah Kim", "title": "VP Compliance", "role": "Compliance",
             "emails": 2, "meetings": 0, "last_touch_days": 30, "sentiment": "unknown",
             "influence": "high", "support_level": "unknown"},
            {"name": "Mike Torres", "title": "IT Director", "role": "Technical Evaluator",
             "emails": 3, "meetings": 1, "last_touch_days": 15, "sentiment": "neutral",
             "influence": "medium", "support_level": "neutral"},
        ],
    },
    "Metro Healthcare": {
        "deal_id": "OPP-004", "value": 440000, "stage": "Proposal", "owner": "Mike Chen",
        "contacts": [
            {"name": "Sandra Patel", "title": "VP Digital", "role": "Champion",
             "emails": 14, "meetings": 4, "last_touch_days": 9, "sentiment": "positive",
             "influence": "high", "support_level": "champion"},
            {"name": "Dr. Karen Lee", "title": "CMO", "role": "Executive Sponsor",
             "emails": 3, "meetings": 1, "last_touch_days": 14, "sentiment": "positive",
             "influence": "very_high", "support_level": "supporter"},
            {"name": "Brian Walsh", "title": "IT Security Manager", "role": "Technical Evaluator",
             "emails": 8, "meetings": 2, "last_touch_days": 7, "sentiment": "positive",
             "influence": "medium", "support_level": "supporter"},
            {"name": "Nancy Drew", "title": "Finance Director", "role": "Budget Holder",
             "emails": 2, "meetings": 0, "last_touch_days": 28, "sentiment": "unknown",
             "influence": "high", "support_level": "unknown"},
        ],
    },
    "Pacific Telecom": {
        "deal_id": "OPP-013", "value": 780000, "stage": "Negotiation", "owner": "Lisa Torres",
        "contacts": [
            {"name": "Diana Cruz", "title": "SVP Operations", "role": "Executive Sponsor",
             "emails": 16, "meetings": 5, "last_touch_days": 3, "sentiment": "very_positive",
             "influence": "very_high", "support_level": "champion"},
            {"name": "Alex Huang", "title": "VP Engineering", "role": "Technical Buyer",
             "emails": 12, "meetings": 4, "last_touch_days": 5, "sentiment": "positive",
             "influence": "high", "support_level": "supporter"},
            {"name": "Maria Santos", "title": "Procurement Director", "role": "Procurement",
             "emails": 8, "meetings": 2, "last_touch_days": 2, "sentiment": "neutral",
             "influence": "medium", "support_level": "neutral"},
            {"name": "Kevin O'Brien", "title": "CTO", "role": "Economic Buyer",
             "emails": 6, "meetings": 2, "last_touch_days": 7, "sentiment": "positive",
             "influence": "very_high", "support_level": "supporter"},
            {"name": "Priya Sharma", "title": "Data Analytics Lead", "role": "End User",
             "emails": 10, "meetings": 3, "last_touch_days": 4, "sentiment": "very_positive",
             "influence": "low", "support_level": "champion"},
        ],
    },
}

_SENTIMENT_SIGNALS = {
    "very_positive": {"score": 90, "label": "Strong advocate", "risk": "low"},
    "positive": {"score": 70, "label": "Favorable", "risk": "low"},
    "neutral": {"score": 50, "label": "Undecided", "risk": "medium"},
    "cautious": {"score": 35, "label": "Hesitant", "risk": "medium"},
    "frustrated": {"score": 30, "label": "Frustrated but engaged", "risk": "high"},
    "negative": {"score": 15, "label": "Opposed", "risk": "critical"},
    "unknown": {"score": 40, "label": "No signal", "risk": "medium"},
}


# ===================================================================
# HELPERS
# ===================================================================

def _engagement_score(contact):
    """Calculate engagement score for a single contact."""
    email_score = min(contact["emails"] * 5, 30)
    meeting_score = min(contact["meetings"] * 15, 30)
    recency_score = max(0, 25 - contact["last_touch_days"]) * 1.5
    sentiment_data = _SENTIMENT_SIGNALS.get(contact["sentiment"], {"score": 40})
    sentiment_score = sentiment_data["score"] * 0.2
    return round(min(100, email_score + meeting_score + recency_score + sentiment_score))


def _deal_engagement_score(deal_name):
    """Calculate aggregate engagement score for a deal."""
    deal = _STAKEHOLDERS.get(deal_name, {})
    contacts = deal.get("contacts", [])
    if not contacts:
        return 0
    influence_weights = {"very_high": 3, "high": 2, "medium": 1.5, "low": 1}
    weighted_sum = 0
    weight_total = 0
    for c in contacts:
        w = influence_weights.get(c["influence"], 1)
        weighted_sum += _engagement_score(c) * w
        weight_total += w
    return round(weighted_sum / max(weight_total, 1))


def _relationship_gaps(deal_name):
    """Identify gaps in relationship coverage."""
    deal = _STAKEHOLDERS.get(deal_name, {})
    contacts = deal.get("contacts", [])
    gaps = []
    has_champion = any(c["support_level"] == "champion" for c in contacts)
    has_exec = any(c["role"] in ("Executive Sponsor", "Economic Buyer") and c["last_touch_days"] <= 14 for c in contacts)
    has_technical = any(c["role"] == "Technical Evaluator" and c["sentiment"] in ("positive", "very_positive") for c in contacts)

    if not has_champion:
        gaps.append("No active champion identified")
    if not has_exec:
        gaps.append("Executive sponsor not recently engaged")
    if not has_technical:
        gaps.append("Technical evaluator not positively engaged")
    for c in contacts:
        if c["last_touch_days"] >= 21 and c["influence"] in ("high", "very_high"):
            gaps.append(f"{c['name']} ({c['title']}) -- no contact in {c['last_touch_days']} days")
    if len(contacts) < 3:
        gaps.append(f"Only {len(contacts)} contacts -- recommend 4+ for multi-threading")
    return gaps


# ===================================================================
# AGENT CLASS
# ===================================================================

class StakeholderEngagementAgent(BasicAgent):
    """
    Tracks and optimizes stakeholder engagement for pipeline deals.

    Operations:
        engagement_score   - per-deal and per-contact engagement scoring
        relationship_map   - buying committee mapping with gaps
        engagement_plan    - targeted outreach plan per deal
        sentiment_analysis - sentiment signals and risk assessment
    """

    def __init__(self):
        self.name = "StakeholderEngagementAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["engagement_score", "relationship_map", "engagement_plan", "sentiment_analysis"],
                        "description": "The analysis to perform",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "engagement_score")
        dispatch = {
            "engagement_score": self._engagement_score,
            "relationship_map": self._relationship_map,
            "engagement_plan": self._engagement_plan,
            "sentiment_analysis": self._sentiment_analysis,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"**Error:** Unknown operation '{op}'. Valid: {', '.join(dispatch.keys())}"
        return handler()

    # -- engagement_score (flagship: prefers LIVE tenant, falls back) ---
    def _engagement_score(self) -> str:
        live = _live_deals_with_contacts()
        if live:
            sections = []
            for deal in sorted(live, key=lambda d: -d["value"]):
                contact_rows = ""
                for c in deal["contacts"]:
                    contact_rows += (f"| {c['name']} | {c['title']} | {c['email']} | "
                                     f"n/a — enrichment seam | n/a | n/a |\n")
                if not contact_rows:
                    contact_rows = "| (no CRM contacts on this account yet) | | | | | |\n"
                thread_note = ("multi-threaded" if len(deal["contacts"]) >= 3
                               else f"only {len(deal['contacts'])} contact(s) — single-thread risk")
                sections.append(
                    f"**{deal['name']} -- ${deal['value']:,} ({deal['stage']})**\n"
                    f"CRM contacts mapped: {len(deal['contacts'])} ({thread_note}) | "
                    f"Owner: {deal['owner']}\n\n"
                    f"| Contact | Title | Email | Score | Last Touch | Influence |\n"
                    f"|---------|-------|-------|-------|-----------|----------|\n"
                    f"{contact_rows}"
                )
            return (
                f"**Stakeholder Engagement — {len(live)} LIVE Open Deals** "
                f"(Static Dynamics 365 tenant)\n\n"
                f"Contacts come from the live CRM; engagement scores, touch "
                f"recency, and influence stay n/a until you wire Gong / email "
                f"analytics at the LIVE DATA SEAM.\n\n"
                + "\n---\n\n".join(sections)
                + f"\n\nSource: [Live Dynamics 365 opportunities + contacts]\n"
                f"Agents: EngagementScoringEngine"
            )
        sections = []
        for deal_name in sorted(_STAKEHOLDERS.keys(), key=lambda d: -_STAKEHOLDERS[d]["value"]):
            deal = _STAKEHOLDERS[deal_name]
            deal_score = _deal_engagement_score(deal_name)
            grade = "A" if deal_score >= 75 else ("B" if deal_score >= 55 else ("C" if deal_score >= 40 else "D"))

            contact_rows = ""
            for c in sorted(deal["contacts"], key=lambda x: -_engagement_score(x)):
                score = _engagement_score(c)
                contact_rows += (f"| {c['name']} | {c['title']} | {c['role']} | "
                                 f"{score}/100 | {c['last_touch_days']}d ago | {c['influence']} |\n")

            sections.append(
                f"**{deal_name} -- ${deal['value']:,} ({deal['stage']})**\n"
                f"Deal Engagement: **{deal_score}/100 [{grade}]** | "
                f"Contacts: {len(deal['contacts'])} | Owner: {deal['owner']}\n\n"
                f"| Contact | Title | Role | Score | Last Touch | Influence |\n"
                f"|---------|-------|------|-------|-----------|----------|\n"
                f"{contact_rows}"
            )

        return (
            f"**Stakeholder Engagement Scores**\n\n"
            + "\n---\n\n".join(sections)
            + f"\n\nSource: [CRM + Email Analytics + Calendar]\n"
            f"Agents: EngagementScoringEngine"
        )

    # -- relationship_map ----------------------------------------------
    def _relationship_map(self) -> str:
        sections = []
        for deal_name in sorted(_STAKEHOLDERS.keys(), key=lambda d: -_STAKEHOLDERS[d]["value"]):
            deal = _STAKEHOLDERS[deal_name]
            gaps = _relationship_gaps(deal_name)

            map_rows = ""
            for c in deal["contacts"]:
                support_icon = {"champion": "CHAMPION", "supporter": "Supporter",
                                "neutral": "Neutral", "blocker": "BLOCKER",
                                "unknown": "Unknown"}.get(c["support_level"], "Unknown")
                map_rows += (f"| {c['name']} | {c['title']} | {c['role']} | "
                             f"{c['influence']} | {support_icon} |\n")

            gap_lines = "\n".join(f"  - {g}" for g in gaps) if gaps else "  - No critical gaps identified"

            sections.append(
                f"**{deal_name} -- ${deal['value']:,}**\n"
                f"Buying Committee ({len(deal['contacts'])} mapped):\n\n"
                f"| Contact | Title | Role | Influence | Support |\n"
                f"|---------|-------|------|----------|--------|\n"
                f"{map_rows}\n"
                f"**Relationship Gaps:**\n{gap_lines}\n"
            )

        return (
            f"**Relationship Map -- Buying Committee Analysis**\n\n"
            + "\n---\n\n".join(sections)
            + f"\n\nSource: [CRM Contacts + LinkedIn + Meeting History]\n"
            f"Agents: RelationshipMappingAgent"
        )

    # -- engagement_plan -----------------------------------------------
    def _engagement_plan(self) -> str:
        sections = []
        for deal_name in sorted(_STAKEHOLDERS.keys(), key=lambda d: -_STAKEHOLDERS[d]["value"]):
            deal = _STAKEHOLDERS[deal_name]
            contacts = deal["contacts"]

            actions = []
            for c in sorted(contacts, key=lambda x: _engagement_score(x)):
                score = _engagement_score(c)
                if score < 40:
                    actions.append(f"- **{c['name']} ({c['title']}):** Re-engagement outreach -- "
                                   f"personalized email + meeting request (Score: {score}/100)")
                elif c["last_touch_days"] >= 14:
                    actions.append(f"- **{c['name']} ({c['title']}):** Schedule touchpoint -- "
                                   f"{c['last_touch_days']} days since last contact")
                elif c["support_level"] == "unknown":
                    actions.append(f"- **{c['name']} ({c['title']}):** Sentiment discovery -- "
                                   f"informal 1:1 to assess support level")

            if not actions:
                actions.append("- All stakeholders adequately engaged -- maintain cadence")

            sections.append(
                f"**{deal_name} -- ${deal['value']:,}**\n"
                f"Owner: {deal['owner']} | Stage: {deal['stage']}\n\n"
                + "\n".join(actions)
            )

        return (
            f"**Engagement Plans -- Targeted Outreach**\n\n"
            + "\n\n---\n\n".join(sections)
            + f"\n\n**General Best Practices:**\n"
            f"- Touch all high-influence contacts at least every 10 days\n"
            f"- Multi-thread to 4+ contacts before Proposal stage\n"
            f"- Confirm champion support monthly with direct conversation\n"
            f"- Engage executive sponsor before any pricing discussion\n\n"
            f"Source: [Engagement Data + Best Practice Playbook]\n"
            f"Agents: EngagementPlannerAgent"
        )

    # -- sentiment_analysis --------------------------------------------
    def _sentiment_analysis(self) -> str:
        sections = []
        for deal_name in sorted(_STAKEHOLDERS.keys(), key=lambda d: -_STAKEHOLDERS[d]["value"]):
            deal = _STAKEHOLDERS[deal_name]

            rows = ""
            risk_contacts = 0
            for c in deal["contacts"]:
                sig = _SENTIMENT_SIGNALS.get(c["sentiment"], {"score": 40, "label": "Unknown", "risk": "medium"})
                rows += (f"| {c['name']} | {c['title']} | {c['sentiment']} | "
                         f"{sig['score']}/100 | {sig['label']} | {sig['risk']} |\n")
                if sig["risk"] in ("high", "critical"):
                    risk_contacts += 1

            avg_sentiment = round(sum(
                _SENTIMENT_SIGNALS.get(c["sentiment"], {"score": 40})["score"]
                for c in deal["contacts"]
            ) / max(len(deal["contacts"]), 1))

            overall_risk = "HIGH" if risk_contacts >= 2 else ("MEDIUM" if risk_contacts >= 1 else "LOW")

            sections.append(
                f"**{deal_name} -- ${deal['value']:,}**\n"
                f"Avg Sentiment: {avg_sentiment}/100 | Risk Contacts: {risk_contacts} | Overall: {overall_risk}\n\n"
                f"| Contact | Title | Sentiment | Score | Label | Risk |\n"
                f"|---------|-------|-----------|-------|-------|------|\n"
                f"{rows}"
            )

        return (
            f"**Sentiment Analysis -- Stakeholder Signals**\n\n"
            + "\n---\n\n".join(sections)
            + f"\n\n**Signal Interpretation:**\n"
            f"- Very Positive (90): Strong internal advocate\n"
            f"- Positive (70): Favorable, continue engagement\n"
            f"- Neutral (50): Needs value reinforcement\n"
            f"- Cautious (35): Address concerns proactively\n"
            f"- Frustrated (30): Engaged but at risk -- resolve issues quickly\n"
            f"- Unknown (40): Requires direct interaction to assess\n\n"
            f"Source: [Gong Call Analysis + Email Sentiment + Meeting Notes]\n"
            f"Agents: SentimentAnalysisEngine"
        )


if __name__ == "__main__":
    agent = StakeholderEngagementAgent()
    print("=" * 70)
    print("LIVE TENANT BUYING COMMITTEES (fetched over HTTP; embedded demo offline)")
    print(agent.perform(operation="engagement_score"))
    print()
    print("=" * 70)
    print("EMBEDDED DEMO (works offline, simulated)")
    print(agent.perform(operation="relationship_map"))
    print()
    print("=" * 70)
    print(agent.perform(operation="sentiment_analysis"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
