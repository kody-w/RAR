---
name: "rar-aibast-agents-library-account-intelligence"
description: "Generates account briefings, stakeholder maps, and deal risk reports from a live simulated Dynamics 365 tenant, with an offline demo fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/account_intelligence", "rar_sha256": "db3bf0e8b9dc53a4c16c879a11501783a03b923fa7142132f5d0ad0037d1f376", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.2.0", "author": "AIBAST", "tags": ["b2b", "sales", "account-intelligence", "stakeholder-mapping", "competitive-intel"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/account_intelligence`. The original RAPP
agent is preserved byte-for-byte in `account_intelligence_agent.py` and in the RCI capsule.

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

Account Intelligence Agent — a template you are meant to mutate.

Surfaces account overviews, stakeholder maps, competitive positioning, and
deal risk assessment for enterprise accounts, producing executive-ready
briefings.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="account_overview",
                  account_name="Granite Peak Manufacturing")
  2. No network? Everything falls back to the embedded demo layer below
     (_ACCOUNTS / _STAKEHOLDERS / _COMPETITORS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     ACCOUNT_INTELLIGENCE_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with calls into your own API. Fields the rest of
     the file needs are listed in _normalize_live_account() — everything
     else keeps working untouched. Fields marked "enrichment seam" in the
     output (revenue, employees, spend) are where you wire ZoomInfo, D&B,
     or your finance system.

OPERATIONS
  account_overview | stakeholder_map | competitive_intel | value_messaging
  | risk_assessment | executive_briefing | share_briefing
  kwargs: operation (required), account_name, account_id (share_briefing)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "account_id": {
      "description": "Exact CRM account ID for share_briefing (e.g. 'acc-001')",
      "type": "string"
    },
    "account_name": {
      "description": "Account name to analyze (e.g. 'Acme Corporation')",
      "type": "string"
    },
    "operation": {
      "description": "The analysis to perform",
      "enum": [
        "account_overview",
        "stakeholder_map",
        "competitive_intel",
        "value_messaging",
        "risk_assessment",
        "executive_briefing",
        "share_briefing"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `account_intelligence_agent.py` and embedded as the fenced Python below (sha256 db3bf0e8b9dc53a4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `account_intelligence_agent.py` first:

```bash
python3 account_intelligence_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 account_intelligence_agent.py   # or on stdin
python3 account_intelligence_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
Account Intelligence Agent — a template you are meant to mutate.

Surfaces account overviews, stakeholder maps, competitive positioning, and
deal risk assessment for enterprise accounts, producing executive-ready
briefings.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM records over real HTTP from the
     globally hosted Static Dynamics 365 tenant (Aster Lane Office
     Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="account_overview",
                  account_name="Granite Peak Manufacturing")
  2. No network? Everything falls back to the embedded demo layer below
     (_ACCOUNTS / _STAKEHOLDERS / _COMPETITORS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     ACCOUNT_INTELLIGENCE_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON you export from Salesforce/HubSpot), or replace
     _fetch_collection() with calls into your own API. Fields the rest of
     the file needs are listed in _normalize_live_account() — everything
     else keeps working untouched. Fields marked "enrichment seam" in the
     output (revenue, employees, spend) are where you wire ZoomInfo, D&B,
     or your finance system.

OPERATIONS
  account_overview | stakeholder_map | competitive_intel | value_messaging
  | risk_assessment | executive_briefing | share_briefing
  kwargs: operation (required), account_name, account_id (share_briefing)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request
from datetime import datetime, timedelta, timezone

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/account_intelligence",
    "version": "1.2.0",
    "display_name": "Account Intelligence",
    "description": "Generates account briefings, stakeholder maps, and deal risk reports from a live simulated Dynamics 365 tenant, with an offline demo fallback.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "account-intelligence", "stakeholder-mapping", "competitive-intel"],
    "category": "b2b_sales",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# LIVE DATA SEAM — swap this for your real system
#
# Default: the globally hosted Static Dynamics 365 tenant (synthetic
# Aster Lane Office Systems data served as OData-shaped JSON from
# GitHub Pages). To hook your own world, either:
#   export ACCOUNT_INTELLIGENCE_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_account().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "ACCOUNT_INTELLIGENCE_DATA_URL",
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


def _normalize_live_account(row, opportunities, incidents):
    """Project a Dynamics account record onto the shape this agent uses.
    THIS is the contract your replacement data source must meet — a dict
    with these keys. None means 'not available from CRM alone' and the
    renderers label it as an enrichment seam."""
    name = row.get("name", "Unknown")
    open_opp_value = sum(
        float(o.get("estimatedvalue") or 0)
        for o in opportunities
        if o.get("parentaccountidname") == name and o.get("statecode") == 0
    )
    open_cases = [
        i for i in incidents
        if i.get("customeridname") == name and i.get("statecode") == 0
    ]
    resolved_cases = [
        i for i in incidents
        if i.get("customeridname") == name and i.get("statecode") == 1
    ]
    news = [
        {"headline": f"Open case: {c.get('title', 'untitled')}",
         "age_days": _age_days(c.get("createdon"))}
        for c in open_cases[:4]
    ] + [
        {"headline": f"Resolved: {c.get('title', 'untitled')}",
         "age_days": _age_days(c.get("createdon"))}
        for c in resolved_cases[:2]
    ]
    return {
        "id": row.get("accountnumber", row.get("accountid", "")),
        "name": name,
        "industry": row.get("industrycode", "Unknown"),
        "hq": f"{row.get('address1_city', '?')}, {row.get('address1_stateorprovince', '?')}",
        "revenue": None,           # enrichment seam — wire D&B / your ERP
        "employees": None,         # enrichment seam
        "current_spend": None,     # enrichment seam — wire your billing system
        "opportunity_value": int(open_opp_value),
        "products_owned": [],
        "contract_renewal": "n/a (wire your contract system)",
        "recent_news": news or [{"headline": "No open cases on record", "age_days": 0}],
        "_live": True,
        "_owner": row.get("owneridname", ""),
        "_open_cases": len(open_cases),
    }


def _age_days(iso_date):
    try:
        then = datetime.fromisoformat(str(iso_date).replace("Z", "+00:00"))
        return max(0, (datetime.now(timezone.utc) - then).days)
    except (ValueError, TypeError):
        return 0


def _live_roster():
    """name-keyed dict of live tenant accounts; {} when offline."""
    rows = _fetch_collection("accounts")
    if not rows:
        return {}
    opportunities = _fetch_collection("opportunities")
    incidents = _fetch_collection("incidents")
    return {
        row["name"].lower(): _normalize_live_account(row, opportunities, incidents)
        for row in rows
        if row.get("name")
    }


def _money(value):
    """None = the CRM alone can't know this (enrichment seam); 0 is real."""
    return "n/a — enrichment seam" if value is None else f"${value:,}"


def _num(value):
    return "n/a — enrichment seam" if value is None else f"{value:,}"


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# Stands in for CRM, LinkedIn, ZoomInfo, D&B when there is no network.
# ═══════════════════════════════════════════════════════════════

_ACCOUNTS = {
    "acme": {
        "id": "acc-001", "name": "Acme Corporation", "industry": "Manufacturing",
        "revenue": 2_800_000_000, "employees": 12_400, "hq": "Chicago, IL",
        "current_spend": 1_200_000, "opportunity_value": 2_400_000,
        "products_owned": ["Platform Core", "Analytics Module"],
        "contract_renewal": "8 months",
        "recent_news": [
            {"headline": "CEO mentioned digital transformation in Q3 earnings call", "age_days": 12},
            {"headline": "New CTO Sarah Chen hired from AWS", "age_days": 42},
            {"headline": "Competitor RFP issued for operations platform", "age_days": 30},
        ],
    },
    "contoso": {
        "id": "acc-002", "name": "Contoso Ltd", "industry": "Technology",
        "revenue": 980_000_000, "employees": 4_200, "hq": "Redmond, WA",
        "current_spend": 680_000, "opportunity_value": 1_100_000,
        "products_owned": ["Platform Core"],
        "contract_renewal": "3 months",
        "recent_news": [
            {"headline": "Series D funding of $120M announced", "age_days": 18},
            {"headline": "Expanding EMEA operations with new London office", "age_days": 45},
        ],
    },
    "fabrikam": {
        "id": "acc-003", "name": "Fabrikam Industries", "industry": "Manufacturing",
        "revenue": 1_500_000_000, "employees": 8_700, "hq": "Detroit, MI",
        "current_spend": 450_000, "opportunity_value": 890_000,
        "products_owned": ["Analytics Module"],
        "contract_renewal": "14 months",
        "recent_news": [
            {"headline": "Q2 revenue up 18% YoY", "age_days": 25},
            {"headline": "New VP of IT appointed", "age_days": 60},
        ],
    },
    "northwind": {
        "id": "acc-004", "name": "Northwind Traders", "industry": "Retail",
        "revenue": 620_000_000, "employees": 3_100, "hq": "Portland, OR",
        "current_spend": 220_000, "opportunity_value": 540_000,
        "products_owned": [],
        "contract_renewal": None,
        "recent_news": [
            {"headline": "Launched e-commerce platform", "age_days": 15},
        ],
    },
}

_STAKEHOLDERS = {
    "acme": [
        {"name": "Sarah Chen",  "role": "CTO",           "influence": "Decision Maker", "sentiment": "Unknown",  "meetings": 0,  "notes": "New hire from AWS, 6 weeks ago. Controls tech budget."},
        {"name": "James Miller", "role": "VP Operations", "influence": "Champion",       "sentiment": "Positive", "meetings": 14, "notes": "Promoted to VP last quarter. Advocated for 3 vendor decisions."},
        {"name": "Lisa Park",    "role": "CFO",           "influence": "Economic Buyer", "sentiment": "Neutral",  "meetings": 2,  "notes": "Requested business case and ROI validation."},
        {"name": "David Wong",   "role": "IT Director",   "influence": "Influencer",     "sentiment": "Positive", "meetings": 8,  "notes": "Technical evaluator. Likes our API-first approach."},
        {"name": "Rachel Torres","role": "Procurement",    "influence": "Gatekeeper",     "sentiment": "Neutral",  "meetings": 1,  "notes": "Standard procurement process, 4-6 week cycle."},
        {"name": "Kevin Park",   "role": "VP Engineering", "influence": "Influencer",     "sentiment": "Positive", "meetings": 5,  "notes": "Attended 2 product demos."},
        {"name": "Maria Lopez",  "role": "Director of Strategy", "influence": "Influencer", "sentiment": "Unknown", "meetings": 0, "notes": "No contact yet."},
        {"name": "Tom Bradley",  "role": "CEO",           "influence": "Executive Sponsor", "sentiment": "Unknown", "meetings": 0, "notes": "Mentioned digital transformation in earnings call."},
    ],
    "contoso": [
        {"name": "Alex Kim",    "role": "CTO",        "influence": "Decision Maker", "sentiment": "Positive", "meetings": 10, "notes": "Strong advocate."},
        {"name": "Pat Johnson",  "role": "CFO",        "influence": "Economic Buyer", "sentiment": "Neutral",  "meetings": 3,  "notes": "Budget cautious."},
        {"name": "Sam Rivera",   "role": "VP Product", "influence": "Champion",       "sentiment": "Positive", "meetings": 7,  "notes": "Wants expansion."},
    ],
    "fabrikam": [
        {"name": "Chris Anderson","role": "VP IT",       "influence": "Decision Maker", "sentiment": "Neutral",  "meetings": 4, "notes": "New to role."},
        {"name": "Dana White",    "role": "COO",         "influence": "Champion",       "sentiment": "Positive", "meetings": 6, "notes": "Drives operational efficiency."},
    ],
    "northwind": [
        {"name": "Jordan Lee",  "role": "CTO",    "influence": "Decision Maker", "sentiment": "Unknown", "meetings": 1, "notes": "Initial discovery call."},
        {"name": "Casey Brown",  "role": "CEO",    "influence": "Executive Sponsor", "sentiment": "Unknown", "meetings": 0, "notes": "No contact yet."},
    ],
}

_COMPETITORS = {
    "acme": [
        {"name": "CompetitorA", "relationship": "Medium", "product_fit": 78, "pricing": "-15% below market", "impl_weeks": 14, "activity": "On-site demo last week, aggressive discount offered"},
        {"name": "CompetitorB", "relationship": "Weak",   "product_fit": 82, "pricing": "+10% above market", "impl_weeks": 10, "activity": "Early conversations only, no formal proposal"},
    ],
    "contoso": [
        {"name": "CompetitorA", "relationship": "Strong", "product_fit": 85, "pricing": "Market rate",      "impl_weeks": 12, "activity": "Incumbent on analytics module"},
    ],
    "fabrikam": [
        {"name": "CompetitorC", "relationship": "Weak",   "product_fit": 70, "pricing": "-20% below market", "impl_weeks": 18, "activity": "Low-cost proposal submitted"},
    ],
    "northwind": [],
}

_OUR_PROFILE = {
    "relationship": "Strong", "product_fit": 94, "pricing": "Market rate",
    "impl_weeks": 8,
    "advantages": [
        "Existing integration with customer ERP (3-week head start)",
        "Champion relationship established",
        "Superior customer references in target industry",
    ],
}

_ACCOUNT_KEYS_BY_ID = {account["id"]: key for key, account in _ACCOUNTS.items()}


# ═══════════════════════════════════════════════════════════════
# HELPERS — real computation, synthetic inputs
# ═══════════════════════════════════════════════════════════════

def _resolve_account(query):
    """Fuzzy-match an account name to our synthetic data."""
    if not query:
        return "acme"
    q = query.lower().strip()
    for key in _ACCOUNTS:
        if key in q or q in _ACCOUNTS[key]["name"].lower():
            return key
    # Not an embedded demo account — try the live tenant roster.
    live = _live_roster()
    for key in live:
        if key in q or q in key:
            return key
    return "acme"


def _get_account(key):
    """Unified lookup: embedded demo accounts first, then live tenant."""
    if key in _ACCOUNTS:
        return _ACCOUNTS[key]
    return _live_roster().get(key) or _ACCOUNTS["acme"]


def _health_score(key):
    """Compute account health from engagement signals."""
    stks = _STAKEHOLDERS.get(key, [])
    acct = _get_account(key)

    total_meetings = sum(s["meetings"] for s in stks)
    positive_ratio = sum(1 for s in stks if s["sentiment"] == "Positive") / max(len(stks), 1)
    product_depth = len(acct["products_owned"]) / 3

    engagement = min(100, int(total_meetings * 3.5))
    adoption = int(product_depth * 100)
    sentiment = int(positive_ratio * 100)
    renewal_risk = max(5, 50 - total_meetings * 2 - int(positive_ratio * 30))

    overall = int(engagement * 0.3 + adoption * 0.2 + sentiment * 0.3 + (100 - renewal_risk) * 0.2)
    return {
        "overall": overall,
        "engagement": engagement,
        "adoption": adoption,
        "sentiment_score": sentiment,
        "renewal_risk_pct": renewal_risk,
        "touchpoints_30d": total_meetings,
        "csat": round(3.0 + positive_ratio * 2, 1),
    }


def _deal_risks(key):
    """Compute deal risks from stakeholder and competitive data."""
    stks = _STAKEHOLDERS.get(key, [])
    comps = _COMPETITORS.get(key, [])
    risks = []

    for s in stks:
        if s["influence"] == "Decision Maker" and s["meetings"] == 0:
            risks.append({"risk": f"No relationship with {s['role']} ({s['name']})",
                          "severity": "High", "mitigation": "Champion intro this week", "owner": "You"})
    for c in comps:
        if "-" in c["pricing"]:
            risks.append({"risk": f"{c['name']} pricing pressure ({c['pricing']})",
                          "severity": "High", "mitigation": "TCO analysis showing lower total cost", "owner": "You"})
    for s in stks:
        if s["influence"] == "Economic Buyer" and s["sentiment"] != "Positive":
            risks.append({"risk": f"{s['role']} needs ROI validation",
                          "severity": "Medium", "mitigation": "Send customized ROI calculator", "owner": "Finance"})

    champion_count = sum(1 for s in stks if s["influence"] == "Champion" and s["sentiment"] == "Positive")
    blocker_count = len([r for r in risks if r["severity"] == "High"])
    win_prob = min(95, max(20, 50 + champion_count * 15 - blocker_count * 10 + len(stks) * 2))
    return risks, win_prob


def _value_messaging(key):
    """Generate stakeholder-specific talking points."""
    stks = _STAKEHOLDERS.get(key, [])
    acct = _get_account(key)
    messaging = {}
    for s in stks:
        if s["influence"] not in ("Decision Maker", "Economic Buyer", "Champion"):
            continue
        role = s["role"]
        if any(t in role for t in ("CTO", "IT", "Engineering")):
            messaging[s["name"]] = {"role": role, "focus": "Tech Vision", "points": [
                "Platform aligns with digital transformation roadmap",
                "API-first architecture integrates with existing systems",
                f"3 {acct['industry']} CTO references available for peer conversation",
            ]}
        elif any(t in role for t in ("CFO", "Finance")):
            savings = int(acct["opportunity_value"] * 1.75)
            messaging[s["name"]] = {"role": role, "focus": "ROI", "points": [
                f"${savings:,} projected savings over 3 years",
                f"{_OUR_PROFILE['impl_weeks']}-week implementation vs competitor's longer timeline",
                "Risk-free pilot: 90-day proof of value before full commitment",
            ]}
        elif s["influence"] == "Champion":
            messaging[s["name"]] = {"role": role, "focus": "Internal Positioning", "points": [
                "Positions your team as transformation leaders",
                "Executive visibility on project success metrics",
                "Co-innovation partnership opportunity",
            ]}
    return messaging


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class AccountIntelligenceAgent(BasicAgent):
    """
    Produces 360-degree account intelligence briefings.

    Operations:
        account_overview  - firmographics, health score, recent news
        stakeholder_map   - org chart, buying committee, relationship gaps
        competitive_intel - landscape analysis and positioning
        value_messaging   - stakeholder-specific talking points
        risk_assessment   - deal risks with mitigation actions
        executive_briefing - full compiled briefing
        share_briefing    - post a briefing to Teams with simulated receipts
    """

    def __init__(self):
        self.name = "AccountIntelligenceAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "account_overview", "stakeholder_map",
                            "competitive_intel", "value_messaging",
                            "risk_assessment", "executive_briefing",
                            "share_briefing",
                        ],
                        "description": "The analysis to perform",
                    },
                    "account_name": {
                        "type": "string",
                        "description": "Account name to analyze (e.g. 'Acme Corporation')",
                    },
                    "account_id": {
                        "type": "string",
                        "description": "Exact CRM account ID for share_briefing (e.g. 'acc-001')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "account_overview")
        if op == "share_briefing":
            return self._share_briefing(kwargs.get("account_id"))
        key = _resolve_account(kwargs.get("account_name", ""))
        dispatch = {
            "account_overview": self._account_overview,
            "stakeholder_map": self._stakeholder_map,
            "competitive_intel": self._competitive_intel,
            "value_messaging": self._value_messaging,
            "risk_assessment": self._risk_assessment,
            "executive_briefing": self._executive_briefing,
        }
        handler = dispatch.get(op)
        if not handler:
            return json.dumps({"status": "error", "message": f"Unknown operation: {op}"})
        return handler(key)

    def _share_briefing(self, account_id):
        key = _ACCOUNT_KEYS_BY_ID.get(account_id)
        if key is None:
            valid_ids = ", ".join(sorted(_ACCOUNT_KEYS_BY_ID))
            return json.dumps({
                "status": "error",
                "message": f"Unknown account_id: {account_id!r}",
                "valid_account_ids": valid_ids,
            })

        account = _get_account(key)
        health = _health_score(key)
        risks, win_probability = _deal_risks(key)
        receipt = {
            "status": "simulated",
            "account_id": account_id,
            "account": account["name"],
            "artifact": f"account-briefing-{account_id}.docx",
            "teams_message_id": f"sim-teams-account-{account_id}",
            "crm_activity_id": f"sim-d365-activity-{account_id}",
            "health_score": health["overall"],
            "win_probability": win_probability,
            "risk_count": len(risks),
            "next_action": risks[0]["mitigation"] if risks else "Maintain current engagement cadence",
        }
        return "**Account Briefing Share Receipt**\n\n```json\n" + json.dumps(receipt, indent=2) + "\n```"

    # ── account_overview ──────────────────────────────────────
    def _account_overview(self, key):
        acct = _get_account(key)
        h = _health_score(key)
        news = "\n".join(f"- {n['headline']} ({n['age_days']} days ago)" for n in acct["recent_news"])
        return (
            f"**Account Overview: {acct['name']}**\n\n"
            f"| Attribute | Details |\n|---|---|\n"
            f"| Industry | {acct['industry']} |\n"
            f"| Revenue | {_money(acct['revenue'])} |\n"
            f"| Employees | {_num(acct['employees'])} |\n"
            f"| HQ | {acct['hq']} |\n"
            f"| Current spend | {_money(acct['current_spend'])} |\n"
            f"| Opportunity | {_money(acct['opportunity_value'])} open pipeline |\n\n"
            f"**Account Health Score: {h['overall']}/100**\n"
            f"- Engagement: {h['engagement']}% ({h['touchpoints_30d']} touchpoints last 30 days)\n"
            f"- Product adoption: {h['adoption']}% feature utilization\n"
            f"- Support sentiment: {h['csat']}/5 CSAT\n"
            f"- Renewal risk: {h['renewal_risk_pct']}%\n\n"
            f"**Recent Activity:**\n{news}\n\n"
            f"Source: [CRM + News Intelligence + LinkedIn]\n"
            f"Agents: AccountProfileAgent, AccountHealthScoreAgent"
        )

    # ── stakeholder_map ───────────────────────────────────────
    def _stakeholder_map(self, key):
        stks = _STAKEHOLDERS.get(key, [])
        if not stks:
            return "No stakeholders mapped for this account yet."

        table = "| Name | Role | Influence | Sentiment | Engagement |\n|---|---|---|---|---|\n"
        for s in stks:
            eng = f"{s['meetings']} meetings" if s["meetings"] > 0 else "Schedule intro"
            table += f"| {s['name']} | {s['role']} | {s['influence']} | {s['sentiment']} | {eng} |\n"

        gaps = [s for s in stks if s["meetings"] == 0 and s["influence"] in ("Decision Maker", "Economic Buyer", "Executive Sponsor")]
        gap_lines = ""
        if gaps:
            gap_lines = "\n**Relationship Gaps:**\n"
            for g in gaps:
                gap_lines += f"- {g['name']} ({g['role']}): {g['notes']}\n"

        champions = [s for s in stks if s["influence"] == "Champion" and s["sentiment"] == "Positive"]
        champ_lines = ""
        if champions:
            c = champions[0]
            champ_lines = f"\n**Champion Intelligence:**\n{c['name']} — {c['notes']}\n"

        return (
            f"**Stakeholder Map ({len(stks)} contacts):**\n\n"
            f"{table}{gap_lines}{champ_lines}\n"
            "Source: [LinkedIn Sales Navigator + CRM Contacts + Meeting History]\n"
            "Agents: StakeholderMappingAgent"
        )

    # ── competitive_intel ─────────────────────────────────────
    def _competitive_intel(self, key):
        comps = _COMPETITORS.get(key, [])
        if not comps:
            return "No active competitors identified for this account."

        header = "| Factor | You |" + "".join(f" {c['name']} |" for c in comps) + "\n"
        sep = "|---|---|" + "".join("---|" for _ in comps) + "\n"
        rows_data = [
            ("Relationship depth", _OUR_PROFILE["relationship"], [c["relationship"] for c in comps]),
            ("Product fit", f"{_OUR_PROFILE['product_fit']}%", [f"{c['product_fit']}%" for c in comps]),
            ("Pricing", _OUR_PROFILE["pricing"], [c["pricing"] for c in comps]),
            ("Implementation", f"{_OUR_PROFILE['impl_weeks']} weeks", [f"{c['impl_weeks']} weeks" for c in comps]),
        ]
        rows = ""
        for label, ours, theirs in rows_data:
            rows += f"| {label} | {ours} |" + "".join(f" {t} |" for t in theirs) + "\n"

        activity = "\n**Competitor Activity:**\n" + "".join(f"- {c['name']}: {c['activity']}\n" for c in comps)
        advantages = "\n**Your Advantages:**\n" + "".join(f"{i}. {a}\n" for i, a in enumerate(_OUR_PROFILE["advantages"], 1))

        price_threats = [c for c in comps if "-" in c["pricing"]]
        risk = f"\n**Risk Alert:** {price_threats[0]['name']}'s discount may appeal to economic buyer.\n" if price_threats else ""

        return f"**Competitive Intelligence:**\n\n{header}{sep}{rows}{activity}{advantages}{risk}\nSource: [Competitive Intel + Win/Loss Database]\nAgents: CompetitiveIntelligenceAgent"

    # ── value_messaging ───────────────────────────────────────
    def _value_messaging(self, key):
        messaging = _value_messaging(key)
        if not messaging:
            return "No decision-maker or champion contacts mapped yet."

        output = "**Meeting Talking Points:**\n\n"
        for name, data in messaging.items():
            output += f"**For {name} ({data['role']} — {data['focus']}):**\n"
            for pt in data["points"]:
                output += f'- "{pt}"\n'
            output += "\n"

        output += (
            "**Objection Handling:**\n"
            '- Price concern: "Total cost of ownership is 23% lower when factoring implementation and support"\n'
            '- Risk concern: "Deployed at 47 similar companies with 94% success rate"\n\n'
            "Source: [Value Engineering + Reference Database]\nAgents: ValueMessagingAgent"
        )
        return output

    # ── risk_assessment ───────────────────────────────────────
    def _risk_assessment(self, key):
        acct = _get_account(key)
        risks, win_prob = _deal_risks(key)
        if not risks:
            return f"No significant risks identified for {acct['name']}. Win probability: {win_prob}%."

        table = "| Risk | Severity | Mitigation | Owner |\n|---|---|---|---|\n"
        for r in risks:
            table += f"| {r['risk']} | {r['severity']} | {r['mitigation']} | {r['owner']} |\n"

        high = [r for r in risks if r["severity"] == "High"]
        actions = ""
        if high:
            actions = "\n**Immediate Actions:**\n" + "".join(f"{i}. {r['mitigation']} — {r['owner']}\n" for i, r in enumerate(high, 1))

        return (
            f"**Deal Risk Assessment: {acct['name']}**\n\n{table}\n"
            f"**Win Probability:** {win_prob}%\n"
            f"**Opportunity Value:** {_money(acct['opportunity_value'])}\n"
            f"{actions}\nSource: [Deal Analytics + Risk Models]\nAgents: DealRiskAssessmentAgent"
        )

    # ── executive_briefing ────────────────────────────────────
    def _executive_briefing(self, key):
        acct = _get_account(key)
        h = _health_score(key)
        risks, win_prob = _deal_risks(key)
        stks = _STAKEHOLDERS.get(key, [])
        comps = _COMPETITORS.get(key, [])
        gaps = sum(1 for s in stks if s["meetings"] == 0)

        checklist = "".join(f"- {r['mitigation']}\n" for r in risks if r["severity"] == "High")
        return (
            f"**Account Intelligence Briefing: {acct['name']}**\n\n"
            f"**Opportunity Summary:**\n"
            f"- Deal value: {_money(acct['opportunity_value'])} (current spend {_money(acct['current_spend'])})\n"
            f"- Win probability: {win_prob}%\n"
            f"- Account health: {h['overall']}/100\n\n"
            f"| Analysis | Key Finding |\n|---|---|\n"
            f"| Account health | {h['engagement']}% engagement, {h['adoption']}% adoption, {h['renewal_risk_pct']}% churn risk |\n"
            f"| Stakeholders | {len(stks)} mapped, {gaps} need intro, {sum(1 for s in stks if s['influence']=='Champion')} champions |\n"
            f"| Competition | {len(comps)} active, you lead on fit/speed |\n"
            f"| Risks | {len(risks)} identified, {sum(1 for r in risks if r['severity']=='High')} critical |\n\n"
            f"**Pre-Meeting Checklist:**\n{checklist}\n"
            "Source: [All Intelligence Systems]\nAgents: BriefingDocumentAgent (orchestrating all agents)"
        )


if __name__ == "__main__":
    agent = AccountIntelligenceAgent()
    print("=" * 60)
    print("EMBEDDED DEMO ACCOUNT (works offline)")
    print(agent.perform(operation="account_overview", account_name="Acme Corporation"))
    print()
    print("=" * 60)
    print("LIVE TENANT ACCOUNT (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="account_overview", account_name="Granite Peak Manufacturing"))
    print()
    print("=" * 60)
    print(agent.perform(operation="executive_briefing", account_name="Acme Corporation"))
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
