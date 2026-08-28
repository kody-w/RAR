---
name: "rar-aibast-agents-library-stakeholder-intelligence"
description: "Maps org charts, buying committees, engagement gaps, and relationship strength for accounts using built-in demo data."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/stakeholder_intelligence", "rar_sha256": "cb303ab64beaa9c9d5ed1ba797d18c561a66cdacb6afb4dacbc24dbb0015c897", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "AIBAST", "tags": ["b2b", "sales", "stakeholder-mapping", "org-chart", "buying-committee"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/stakeholder_intelligence`. The original RAPP
agent is preserved byte-for-byte in `stakeholder_intelligence_agent.py` and in the RCI capsule.

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

Stakeholder Intelligence Agent

Maps organizational hierarchies, analyzes buying committees, identifies
engagement gaps, and scores relationship strength for enterprise B2B
accounts. Provides actionable recommendations for stakeholder engagement
and champion development.

Where a real deployment would call LinkedIn Sales Navigator and CRM APIs,
this agent uses a synthetic data layer so it runs anywhere without
credentials.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "account_name": {
      "description": "Account name (e.g. 'Acme Corporation')",
      "type": "string"
    },
    "operation": {
      "description": "The stakeholder analysis to perform",
      "enum": [
        "map_org_chart",
        "analyze_buying_committee",
        "engagement_gaps",
        "relationship_strength"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `stakeholder_intelligence_agent.py` and embedded as the fenced Python below (sha256 cb303ab64beaa9c9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `stakeholder_intelligence_agent.py` first:

```bash
python3 stakeholder_intelligence_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 stakeholder_intelligence_agent.py   # or on stdin
python3 stakeholder_intelligence_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Stakeholder Intelligence Agent

Maps organizational hierarchies, analyzes buying committees, identifies
engagement gaps, and scores relationship strength for enterprise B2B
accounts. Provides actionable recommendations for stakeholder engagement
and champion development.

Where a real deployment would call LinkedIn Sales Navigator and CRM APIs,
this agent uses a synthetic data layer so it runs anywhere without
credentials.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
from datetime import datetime, timedelta

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/stakeholder_intelligence",
    "version": "1.0.1",
    "display_name": "Stakeholder Intelligence",
    "description": "Maps org charts, buying committees, engagement gaps, and relationship strength for accounts using built-in demo data.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "stakeholder-mapping", "org-chart", "buying-committee"],
    "category": "b2b_sales",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# SYNTHETIC DATA LAYER
# ═══════════════════════════════════════════════════════════════

_ACCOUNTS = {
    "acme": {"id": "acc-001", "name": "Acme Corporation", "industry": "Manufacturing", "employees": 12_400},
    "contoso": {"id": "acc-002", "name": "Contoso Ltd", "industry": "Technology", "employees": 4_200},
    "fabrikam": {"id": "acc-003", "name": "Fabrikam Industries", "industry": "Manufacturing", "employees": 8_700},
    "northwind": {"id": "acc-004", "name": "Northwind Traders", "industry": "Retail", "employees": 3_100},
}

_ORG_HIERARCHIES = {
    "acme": [
        {"name": "Tom Bradley", "role": "CEO", "reports_to": None, "department": "Executive", "level": "C-Suite", "tenure_years": 8},
        {"name": "Sarah Chen", "role": "CTO", "reports_to": "Tom Bradley", "department": "Technology", "level": "C-Suite", "tenure_years": 0.1},
        {"name": "Lisa Park", "role": "CFO", "reports_to": "Tom Bradley", "department": "Finance", "level": "C-Suite", "tenure_years": 5},
        {"name": "James Miller", "role": "VP Operations", "reports_to": "Tom Bradley", "department": "Operations", "level": "VP", "tenure_years": 3},
        {"name": "Kevin Park", "role": "VP Engineering", "reports_to": "Sarah Chen", "department": "Engineering", "level": "VP", "tenure_years": 2},
        {"name": "David Wong", "role": "IT Director", "reports_to": "Sarah Chen", "department": "IT", "level": "Director", "tenure_years": 4},
        {"name": "Maria Lopez", "role": "Director of Strategy", "reports_to": "Tom Bradley", "department": "Strategy", "level": "Director", "tenure_years": 1},
        {"name": "Rachel Torres", "role": "Procurement Manager", "reports_to": "Lisa Park", "department": "Procurement", "level": "Manager", "tenure_years": 6},
    ],
    "contoso": [
        {"name": "Alex Kim", "role": "CTO", "reports_to": "CEO", "department": "Technology", "level": "C-Suite", "tenure_years": 4},
        {"name": "Pat Johnson", "role": "CFO", "reports_to": "CEO", "department": "Finance", "level": "C-Suite", "tenure_years": 3},
        {"name": "Sam Rivera", "role": "VP Product", "reports_to": "Alex Kim", "department": "Product", "level": "VP", "tenure_years": 2},
    ],
    "fabrikam": [
        {"name": "Chris Anderson", "role": "VP IT", "reports_to": "CEO", "department": "IT", "level": "VP", "tenure_years": 0.5},
        {"name": "Dana White", "role": "COO", "reports_to": "CEO", "department": "Operations", "level": "C-Suite", "tenure_years": 6},
    ],
    "northwind": [
        {"name": "Jordan Lee", "role": "CTO", "reports_to": "Casey Brown", "department": "Technology", "level": "C-Suite", "tenure_years": 2},
        {"name": "Casey Brown", "role": "CEO", "reports_to": None, "department": "Executive", "level": "C-Suite", "tenure_years": 10},
    ],
}

_BUYING_COMMITTEE = {
    "acme": [
        {"name": "Sarah Chen", "role": "CTO", "committee_role": "Decision Maker", "budget_authority": True, "veto_power": True, "priority": "Technical architecture and scalability"},
        {"name": "Lisa Park", "role": "CFO", "committee_role": "Economic Buyer", "budget_authority": True, "veto_power": True, "priority": "ROI and total cost of ownership"},
        {"name": "James Miller", "role": "VP Operations", "committee_role": "Champion", "budget_authority": False, "veto_power": False, "priority": "Operational efficiency gains"},
        {"name": "David Wong", "role": "IT Director", "committee_role": "Technical Evaluator", "budget_authority": False, "veto_power": False, "priority": "Integration and security"},
        {"name": "Rachel Torres", "role": "Procurement", "committee_role": "Gatekeeper", "budget_authority": False, "veto_power": True, "priority": "Compliance and vendor terms"},
        {"name": "Tom Bradley", "role": "CEO", "committee_role": "Executive Sponsor", "budget_authority": True, "veto_power": True, "priority": "Strategic alignment"},
    ],
    "contoso": [
        {"name": "Alex Kim", "role": "CTO", "committee_role": "Decision Maker", "budget_authority": True, "veto_power": True, "priority": "Platform consolidation"},
        {"name": "Pat Johnson", "role": "CFO", "committee_role": "Economic Buyer", "budget_authority": True, "veto_power": True, "priority": "Budget optimization"},
        {"name": "Sam Rivera", "role": "VP Product", "committee_role": "Champion", "budget_authority": False, "veto_power": False, "priority": "Product expansion"},
    ],
    "fabrikam": [
        {"name": "Chris Anderson", "role": "VP IT", "committee_role": "Decision Maker", "budget_authority": True, "veto_power": True, "priority": "IT modernization"},
        {"name": "Dana White", "role": "COO", "committee_role": "Champion", "budget_authority": False, "veto_power": False, "priority": "Operational efficiency"},
    ],
    "northwind": [
        {"name": "Jordan Lee", "role": "CTO", "committee_role": "Decision Maker", "budget_authority": True, "veto_power": True, "priority": "E-commerce technology"},
        {"name": "Casey Brown", "role": "CEO", "committee_role": "Executive Sponsor", "budget_authority": True, "veto_power": True, "priority": "Growth strategy"},
    ],
}

_ENGAGEMENT_DATA = {
    "acme": {
        "Sarah Chen": {"meetings": 0, "emails_sent": 0, "emails_opened": 0, "last_touch": None, "sentiment": "Unknown", "content_downloaded": []},
        "James Miller": {"meetings": 14, "emails_sent": 22, "emails_opened": 18, "last_touch": "2025-03-12", "sentiment": "Positive", "content_downloaded": ["ROI Calculator", "Case Study: Manufacturing"]},
        "Lisa Park": {"meetings": 2, "emails_sent": 8, "emails_opened": 5, "last_touch": "2025-02-28", "sentiment": "Neutral", "content_downloaded": ["Executive Summary"]},
        "David Wong": {"meetings": 8, "emails_sent": 15, "emails_opened": 12, "last_touch": "2025-03-10", "sentiment": "Positive", "content_downloaded": ["API Docs", "Security Whitepaper", "Integration Guide"]},
        "Rachel Torres": {"meetings": 1, "emails_sent": 3, "emails_opened": 2, "last_touch": "2025-02-15", "sentiment": "Neutral", "content_downloaded": []},
        "Kevin Park": {"meetings": 5, "emails_sent": 10, "emails_opened": 8, "last_touch": "2025-03-08", "sentiment": "Positive", "content_downloaded": ["Technical Architecture"]},
        "Maria Lopez": {"meetings": 0, "emails_sent": 2, "emails_opened": 0, "last_touch": None, "sentiment": "Unknown", "content_downloaded": []},
        "Tom Bradley": {"meetings": 0, "emails_sent": 0, "emails_opened": 0, "last_touch": None, "sentiment": "Unknown", "content_downloaded": []},
    },
    "contoso": {
        "Alex Kim": {"meetings": 10, "emails_sent": 18, "emails_opened": 16, "last_touch": "2025-03-13", "sentiment": "Positive", "content_downloaded": ["Platform Overview", "Roadmap"]},
        "Pat Johnson": {"meetings": 3, "emails_sent": 6, "emails_opened": 3, "last_touch": "2025-02-20", "sentiment": "Neutral", "content_downloaded": []},
        "Sam Rivera": {"meetings": 7, "emails_sent": 12, "emails_opened": 10, "last_touch": "2025-03-11", "sentiment": "Positive", "content_downloaded": ["Product Demo", "Expansion Guide"]},
    },
    "fabrikam": {
        "Chris Anderson": {"meetings": 4, "emails_sent": 8, "emails_opened": 6, "last_touch": "2025-03-04", "sentiment": "Neutral", "content_downloaded": ["Overview Deck"]},
        "Dana White": {"meetings": 6, "emails_sent": 10, "emails_opened": 9, "last_touch": "2025-03-10", "sentiment": "Positive", "content_downloaded": ["Ops Case Study"]},
    },
    "northwind": {
        "Jordan Lee": {"meetings": 1, "emails_sent": 3, "emails_opened": 1, "last_touch": "2025-02-12", "sentiment": "Unknown", "content_downloaded": []},
        "Casey Brown": {"meetings": 0, "emails_sent": 0, "emails_opened": 0, "last_touch": None, "sentiment": "Unknown", "content_downloaded": []},
    },
}

_INFLUENCE_SCORES = {
    "acme": {
        "Sarah Chen": 92, "Tom Bradley": 95, "Lisa Park": 85, "James Miller": 78,
        "David Wong": 62, "Kevin Park": 58, "Rachel Torres": 55, "Maria Lopez": 50,
    },
    "contoso": {"Alex Kim": 90, "Pat Johnson": 82, "Sam Rivera": 70},
    "fabrikam": {"Chris Anderson": 85, "Dana White": 80},
    "northwind": {"Jordan Lee": 88, "Casey Brown": 95},
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _resolve_account(query):
    if not query:
        return "acme"
    q = query.lower().strip()
    for key in _ACCOUNTS:
        if key in q or q in _ACCOUNTS[key]["name"].lower():
            return key
    return "acme"


def _relationship_score(engagement):
    """Compute 0-100 relationship score from engagement data."""
    meetings_score = min(40, engagement["meetings"] * 3)
    email_score = min(20, engagement["emails_opened"])
    recency_score = 0
    if engagement["last_touch"]:
        days_since = 14  # synthetic approximation
        recency_score = max(0, 25 - days_since)
    content_score = min(15, len(engagement["content_downloaded"]) * 5)
    sentiment_bonus = {"Positive": 10, "Neutral": 3, "Unknown": 0}
    total = meetings_score + email_score + recency_score + content_score + sentiment_bonus.get(engagement["sentiment"], 0)
    return min(100, total)


def _engagement_gap_severity(engagement, committee_member):
    """Assess gap severity based on role importance and engagement level."""
    score = _relationship_score(engagement)
    has_veto = committee_member.get("veto_power", False)
    has_budget = committee_member.get("budget_authority", False)

    if score == 0 and (has_veto or has_budget):
        return "Critical"
    if score < 20 and has_veto:
        return "High"
    if score < 30:
        return "Medium"
    return "Low"


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class StakeholderIntelligenceAgent(BasicAgent):
    """
    Provides deep stakeholder intelligence for enterprise accounts.

    Operations:
        map_org_chart           - organizational hierarchy mapping
        analyze_buying_committee - buying committee analysis with roles
        engagement_gaps         - identify and prioritize engagement gaps
        relationship_strength   - score and rank all relationships
    """

    def __init__(self):
        self.name = "StakeholderIntelligenceAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "map_org_chart", "analyze_buying_committee",
                            "engagement_gaps", "relationship_strength",
                        ],
                        "description": "The stakeholder analysis to perform",
                    },
                    "account_name": {
                        "type": "string",
                        "description": "Account name (e.g. 'Acme Corporation')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "map_org_chart")
        key = _resolve_account(kwargs.get("account_name", ""))
        dispatch = {
            "map_org_chart": self._map_org_chart,
            "analyze_buying_committee": self._analyze_buying_committee,
            "engagement_gaps": self._engagement_gaps,
            "relationship_strength": self._relationship_strength,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"**Error:** Unknown operation `{op}`."
        return handler(key)

    # ── map_org_chart ─────────────────────────────────────────
    def _map_org_chart(self, key):
        acct = _ACCOUNTS[key]
        org = _ORG_HIERARCHIES.get(key, [])

        if not org:
            return f"**Org Chart: {acct['name']}**\n\nNo organizational data mapped yet."

        org_rows = ""
        for p in org:
            reports = p["reports_to"] or "Board"
            tenure = f"{p['tenure_years']:.1f}" if p["tenure_years"] < 1 else str(int(p["tenure_years"]))
            org_rows += f"| {p['name']} | {p['role']} | {p['department']} | {p['level']} | {reports} | {tenure}yr |\n"

        c_suite = [p for p in org if p["level"] == "C-Suite"]
        vp_level = [p for p in org if p["level"] == "VP"]
        directors = [p for p in org if p["level"] in ("Director", "Manager")]
        new_hires = [p for p in org if p["tenure_years"] < 1]

        new_hire_note = ""
        if new_hires:
            new_hire_note = "\n**Recent Changes:**\n" + "".join(
                f"- {p['name']} ({p['role']}): New to role ({p['tenure_years']:.1f}yr tenure)\n" for p in new_hires
            )

        return (
            f"**Org Chart: {acct['name']}**\n\n"
            f"| Name | Role | Department | Level | Reports To | Tenure |\n|---|---|---|---|---|---|\n"
            f"{org_rows}\n"
            f"**Structure Summary:**\n"
            f"- C-Suite: {len(c_suite)} executives\n"
            f"- VP Level: {len(vp_level)} leaders\n"
            f"- Director/Manager: {len(directors)} contacts\n"
            f"- Total Mapped: {len(org)} stakeholders\n"
            f"{new_hire_note}\n"
            f"Source: [LinkedIn Sales Navigator + CRM + Org Intelligence]\n"
            f"Agents: StakeholderIntelligenceAgent"
        )

    # ── analyze_buying_committee ──────────────────────────────
    def _analyze_buying_committee(self, key):
        acct = _ACCOUNTS[key]
        committee = _BUYING_COMMITTEE.get(key, [])
        engagement = _ENGAGEMENT_DATA.get(key, {})

        if not committee:
            return f"**Buying Committee: {acct['name']}**\n\nNo buying committee mapped yet."

        rows = ""
        for m in committee:
            eng = engagement.get(m["name"], {})
            meetings = eng.get("meetings", 0)
            sentiment = eng.get("sentiment", "Unknown")
            rows += (
                f"| {m['name']} | {m['role']} | {m['committee_role']} | "
                f"{'Yes' if m['budget_authority'] else 'No'} | "
                f"{'Yes' if m['veto_power'] else 'No'} | "
                f"{meetings} mtgs | {sentiment} |\n"
            )

        veto_holders = [m for m in committee if m["veto_power"]]
        budget_holders = [m for m in committee if m["budget_authority"]]
        champions = [m for m in committee if m["committee_role"] == "Champion"]

        champion_intel = ""
        if champions:
            c = champions[0]
            c_eng = engagement.get(c["name"], {})
            champion_intel = (
                f"\n**Champion Profile: {c['name']}**\n"
                f"- Role: {c['role']} | Priority: {c['priority']}\n"
                f"- Meetings: {c_eng.get('meetings', 0)} | Sentiment: {c_eng.get('sentiment', 'Unknown')}\n"
                f"- Content engaged: {', '.join(c_eng.get('content_downloaded', ['None']))}\n"
            )

        return (
            f"**Buying Committee Analysis: {acct['name']}**\n\n"
            f"| Name | Role | Committee Role | Budget Auth | Veto | Engagement | Sentiment |\n|---|---|---|---|---|---|---|\n"
            f"{rows}\n"
            f"**Committee Composition:**\n"
            f"- Total members: {len(committee)}\n"
            f"- Veto holders: {len(veto_holders)} ({', '.join(v['name'] for v in veto_holders)})\n"
            f"- Budget authority: {len(budget_holders)} ({', '.join(b['name'] for b in budget_holders)})\n"
            f"- Champions: {len(champions)}\n"
            f"{champion_intel}\n"
            f"Source: [LinkedIn + CRM + Meeting History]\n"
            f"Agents: StakeholderIntelligenceAgent"
        )

    # ── engagement_gaps ───────────────────────────────────────
    def _engagement_gaps(self, key):
        acct = _ACCOUNTS[key]
        committee = _BUYING_COMMITTEE.get(key, [])
        engagement = _ENGAGEMENT_DATA.get(key, {})

        gaps = []
        for m in committee:
            eng = engagement.get(m["name"], {"meetings": 0, "emails_sent": 0, "emails_opened": 0, "last_touch": None, "sentiment": "Unknown", "content_downloaded": []})
            score = _relationship_score(eng)
            severity = _engagement_gap_severity(eng, m)
            if score < 50:
                gaps.append({
                    "name": m["name"], "role": m["role"],
                    "committee_role": m["committee_role"],
                    "relationship_score": score, "severity": severity,
                    "veto_power": m["veto_power"],
                    "meetings": eng.get("meetings", 0),
                    "last_touch": eng.get("last_touch"),
                    "priority": m["priority"],
                })

        gaps.sort(key=lambda g: {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}.get(g["severity"], 4))

        if not gaps:
            return f"**Engagement Gaps: {acct['name']}**\n\nNo significant engagement gaps identified. All key stakeholders are adequately engaged."

        gap_rows = ""
        for g in gaps:
            last = g["last_touch"] or "Never"
            gap_rows += (
                f"| {g['name']} | {g['role']} | {g['committee_role']} | "
                f"{g['severity']} | {g['relationship_score']}/100 | {g['meetings']} | {last} |\n"
            )

        actions = "\n**Recommended Actions:**\n"
        for i, g in enumerate(gaps[:5], 1):
            if g["severity"] == "Critical":
                actions += f"{i}. **Urgent:** Get champion intro to {g['name']} ({g['role']}) — controls {g['priority']}\n"
            elif g["severity"] == "High":
                actions += f"{i}. **This week:** Schedule meeting with {g['name']} — {g['priority']}\n"
            else:
                actions += f"{i}. Plan touchpoint with {g['name']} ({g['role']})\n"

        return (
            f"**Engagement Gaps: {acct['name']}**\n\n"
            f"Gaps identified: {len(gaps)} stakeholders below engagement threshold\n\n"
            f"| Name | Role | Committee Role | Severity | Score | Meetings | Last Touch |\n|---|---|---|---|---|---|---|\n"
            f"{gap_rows}"
            f"{actions}\n"
            f"Source: [CRM Engagement + Meeting History + Email Analytics]\n"
            f"Agents: StakeholderIntelligenceAgent"
        )

    # ── relationship_strength ─────────────────────────────────
    def _relationship_strength(self, key):
        acct = _ACCOUNTS[key]
        engagement = _ENGAGEMENT_DATA.get(key, {})
        influence = _INFLUENCE_SCORES.get(key, {})

        scored = []
        for name, eng in engagement.items():
            rel_score = _relationship_score(eng)
            inf_score = influence.get(name, 50)
            weighted = int(rel_score * 0.6 + inf_score * 0.4)
            scored.append({
                "name": name, "relationship_score": rel_score,
                "influence_score": inf_score, "weighted_score": weighted,
                "meetings": eng["meetings"], "sentiment": eng["sentiment"],
                "content": len(eng["content_downloaded"]),
            })

        scored.sort(key=lambda s: s["weighted_score"], reverse=True)

        rows = ""
        for s in scored:
            rows += (
                f"| {s['name']} | {s['relationship_score']}/100 | "
                f"{s['influence_score']}/100 | {s['weighted_score']}/100 | "
                f"{s['meetings']} | {s['sentiment']} | {s['content']} |\n"
            )

        avg_rel = int(sum(s["relationship_score"] for s in scored) / max(len(scored), 1))
        strong = sum(1 for s in scored if s["weighted_score"] >= 60)
        weak = sum(1 for s in scored if s["weighted_score"] < 30)

        top = scored[0] if scored else None
        weakest = scored[-1] if scored else None

        summary = ""
        if top and weakest:
            summary = (
                f"\n**Key Insights:**\n"
                f"- Strongest relationship: {top['name']} (score: {top['weighted_score']})\n"
                f"- Weakest relationship: {weakest['name']} (score: {weakest['weighted_score']})\n"
                f"- Average relationship score: {avg_rel}/100\n"
                f"- Strong relationships (60+): {strong}\n"
                f"- Weak relationships (<30): {weak}\n"
            )

        return (
            f"**Relationship Strength: {acct['name']}**\n\n"
            f"| Name | Relationship | Influence | Weighted | Meetings | Sentiment | Content |\n|---|---|---|---|---|---|---|\n"
            f"{rows}"
            f"{summary}\n"
            f"Source: [CRM + LinkedIn + Meeting History + Content Analytics]\n"
            f"Agents: StakeholderIntelligenceAgent"
        )


if __name__ == "__main__":
    agent = StakeholderIntelligenceAgent()
    for op in ["map_org_chart", "analyze_buying_committee", "engagement_gaps", "relationship_strength"]:
        print("=" * 60)
        print(agent.perform(operation=op, account_name="Acme Corporation"))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
