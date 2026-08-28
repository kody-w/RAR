---
name: "rar-aibast-agents-library-account-messaging"
description: "Drafts personalized outreach, follow-up emails, and campaign sequences for enterprise accounts using built-in demo data."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/account_messaging", "rar_sha256": "e20cab25e71fc4a8c1051be9eb7c04e7b21d9553f2cf3eee10ec251c5e1b0a86", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "AIBAST", "tags": ["b2b", "sales", "messaging", "outreach", "email-sequences"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/account_messaging`. The original RAPP
agent is preserved byte-for-byte in `messaging_agent.py` and in the RCI capsule.

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

Account Messaging Agent

Generates personalized outreach sequences, follow-up emails, proposal
introductions, and multi-touch campaign sequences for enterprise B2B
accounts. Optimizes messaging based on stakeholder role, engagement
history, and response analytics.

Where a real deployment would call email platforms and CRM APIs, this
agent uses a synthetic data layer so it runs anywhere without credentials.

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
      "description": "The messaging operation to perform",
      "enum": [
        "generate_outreach",
        "create_follow_up",
        "draft_proposal_intro",
        "campaign_sequence"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `messaging_agent.py` and embedded as the fenced Python below (sha256 e20cab25e71fc4a8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `messaging_agent.py` first:

```bash
python3 messaging_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 messaging_agent.py   # or on stdin
python3 messaging_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Account Messaging Agent

Generates personalized outreach sequences, follow-up emails, proposal
introductions, and multi-touch campaign sequences for enterprise B2B
accounts. Optimizes messaging based on stakeholder role, engagement
history, and response analytics.

Where a real deployment would call email platforms and CRM APIs, this
agent uses a synthetic data layer so it runs anywhere without credentials.
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
    "name": "@aibast-agents-library/account_messaging",
    "version": "1.0.1",
    "display_name": "Account Messaging",
    "description": "Drafts personalized outreach, follow-up emails, and campaign sequences for enterprise accounts using built-in demo data.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "messaging", "outreach", "email-sequences"],
    "category": "b2b_sales",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# SYNTHETIC DATA LAYER
# ═══════════════════════════════════════════════════════════════

_ACCOUNTS = {
    "acme": {
        "id": "acc-001", "name": "Acme Corporation", "industry": "Manufacturing",
        "revenue": 2_800_000_000, "employees": 12_400, "hq": "Chicago, IL",
        "current_spend": 1_200_000, "opportunity_value": 2_400_000,
        "pain_points": ["legacy ERP integration", "manual reporting", "supply chain visibility"],
    },
    "contoso": {
        "id": "acc-002", "name": "Contoso Ltd", "industry": "Technology",
        "revenue": 980_000_000, "employees": 4_200, "hq": "Redmond, WA",
        "current_spend": 680_000, "opportunity_value": 1_100_000,
        "pain_points": ["scaling data infrastructure", "EMEA compliance", "vendor consolidation"],
    },
    "fabrikam": {
        "id": "acc-003", "name": "Fabrikam Industries", "industry": "Manufacturing",
        "revenue": 1_500_000_000, "employees": 8_700, "hq": "Detroit, MI",
        "current_spend": 450_000, "opportunity_value": 890_000,
        "pain_points": ["production downtime analytics", "quality control automation", "workforce scheduling"],
    },
    "northwind": {
        "id": "acc-004", "name": "Northwind Traders", "industry": "Retail",
        "revenue": 620_000_000, "employees": 3_100, "hq": "Portland, OR",
        "current_spend": 220_000, "opportunity_value": 540_000,
        "pain_points": ["omnichannel inventory", "customer data platform", "last-mile logistics"],
    },
}

_STAKEHOLDERS = {
    "acme": [
        {"name": "Sarah Chen", "role": "CTO", "influence": "Decision Maker", "email_pref": "concise_technical", "last_email_days_ago": None, "open_rate": 0.0, "reply_rate": 0.0},
        {"name": "James Miller", "role": "VP Operations", "influence": "Champion", "email_pref": "roi_focused", "last_email_days_ago": 3, "open_rate": 0.82, "reply_rate": 0.45},
        {"name": "Lisa Park", "role": "CFO", "influence": "Economic Buyer", "email_pref": "executive_summary", "last_email_days_ago": 14, "open_rate": 0.65, "reply_rate": 0.20},
        {"name": "David Wong", "role": "IT Director", "influence": "Influencer", "email_pref": "concise_technical", "last_email_days_ago": 7, "open_rate": 0.78, "reply_rate": 0.35},
    ],
    "contoso": [
        {"name": "Alex Kim", "role": "CTO", "influence": "Decision Maker", "email_pref": "concise_technical", "last_email_days_ago": 5, "open_rate": 0.88, "reply_rate": 0.52},
        {"name": "Pat Johnson", "role": "CFO", "influence": "Economic Buyer", "email_pref": "executive_summary", "last_email_days_ago": 21, "open_rate": 0.55, "reply_rate": 0.15},
    ],
    "fabrikam": [
        {"name": "Chris Anderson", "role": "VP IT", "influence": "Decision Maker", "email_pref": "roi_focused", "last_email_days_ago": 10, "open_rate": 0.72, "reply_rate": 0.28},
        {"name": "Dana White", "role": "COO", "influence": "Champion", "email_pref": "roi_focused", "last_email_days_ago": 4, "open_rate": 0.85, "reply_rate": 0.40},
    ],
    "northwind": [
        {"name": "Jordan Lee", "role": "CTO", "influence": "Decision Maker", "email_pref": "concise_technical", "last_email_days_ago": 30, "open_rate": 0.50, "reply_rate": 0.10},
    ],
}

_EMAIL_TEMPLATES = {
    "concise_technical": {
        "subject_pattern": "Quick technical overview: {topic}",
        "tone": "Direct, data-driven, minimal fluff",
        "max_words": 150,
        "cta_style": "15-min technical walkthrough",
    },
    "roi_focused": {
        "subject_pattern": "{value_prop} for {company}",
        "tone": "Business outcome oriented, metrics-heavy",
        "max_words": 200,
        "cta_style": "ROI calculator review",
    },
    "executive_summary": {
        "subject_pattern": "Strategic alignment: {company} + {our_company}",
        "tone": "High-level, strategic, peer-to-peer",
        "max_words": 120,
        "cta_style": "Executive briefing (20 min)",
    },
}

_MESSAGING_HISTORY = {
    "acme": {
        "total_emails_sent": 34, "total_opens": 24, "total_replies": 11,
        "avg_open_rate": 0.71, "avg_reply_rate": 0.32,
        "best_subject": "3 manufacturing CTO references for your ERP modernization",
        "best_day": "Tuesday", "best_time": "9:15 AM CT",
        "sequences_active": 2, "sequences_completed": 3,
    },
    "contoso": {
        "total_emails_sent": 18, "total_opens": 14, "total_replies": 7,
        "avg_open_rate": 0.78, "avg_reply_rate": 0.39,
        "best_subject": "Scaling data infrastructure post Series D",
        "best_day": "Wednesday", "best_time": "10:30 AM PT",
        "sequences_active": 1, "sequences_completed": 2,
    },
    "fabrikam": {
        "total_emails_sent": 12, "total_opens": 8, "total_replies": 3,
        "avg_open_rate": 0.67, "avg_reply_rate": 0.25,
        "best_subject": "Production downtime reduction case study",
        "best_day": "Monday", "best_time": "8:00 AM ET",
        "sequences_active": 1, "sequences_completed": 1,
    },
    "northwind": {
        "total_emails_sent": 5, "total_opens": 2, "total_replies": 0,
        "avg_open_rate": 0.40, "avg_reply_rate": 0.0,
        "best_subject": "Omnichannel inventory for retail",
        "best_day": "Thursday", "best_time": "11:00 AM PT",
        "sequences_active": 0, "sequences_completed": 1,
    },
}

_RESPONSE_BENCHMARKS = {
    "cold_outreach": {"open_rate": 0.22, "reply_rate": 0.03},
    "warm_intro": {"open_rate": 0.55, "reply_rate": 0.18},
    "existing_relationship": {"open_rate": 0.72, "reply_rate": 0.35},
    "champion_referral": {"open_rate": 0.81, "reply_rate": 0.48},
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


def _engagement_tier(stakeholder):
    """Classify stakeholder engagement level."""
    if stakeholder["last_email_days_ago"] is None:
        return "no_contact"
    if stakeholder["reply_rate"] >= 0.40:
        return "highly_engaged"
    if stakeholder["open_rate"] >= 0.60:
        return "moderately_engaged"
    return "low_engagement"


def _recommended_approach(stakeholder):
    """Determine messaging approach based on engagement."""
    tier = _engagement_tier(stakeholder)
    if tier == "no_contact":
        return "champion_referral"
    if tier == "highly_engaged":
        return "existing_relationship"
    if tier == "moderately_engaged":
        return "warm_intro"
    return "cold_outreach"


def _generate_subject(template_key, account, topic="platform capabilities"):
    tmpl = _EMAIL_TEMPLATES.get(template_key, _EMAIL_TEMPLATES["concise_technical"])
    return tmpl["subject_pattern"].format(
        topic=topic,
        value_prop=f"${account['opportunity_value']:,} efficiency opportunity",
        company=account["name"],
        our_company="TechVenture Solutions",
    )


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class MessagingAgent(BasicAgent):
    """
    Generates personalized B2B sales messaging.

    Operations:
        generate_outreach    - initial outreach emails per stakeholder
        create_follow_up     - follow-up drafts based on engagement
        draft_proposal_intro - proposal introduction email
        campaign_sequence    - multi-touch campaign plan
    """

    def __init__(self):
        self.name = "MessagingAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "generate_outreach", "create_follow_up",
                            "draft_proposal_intro", "campaign_sequence",
                        ],
                        "description": "The messaging operation to perform",
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
        op = kwargs.get("operation", "generate_outreach")
        key = _resolve_account(kwargs.get("account_name", ""))
        dispatch = {
            "generate_outreach": self._generate_outreach,
            "create_follow_up": self._create_follow_up,
            "draft_proposal_intro": self._draft_proposal_intro,
            "campaign_sequence": self._campaign_sequence,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"**Error:** Unknown operation `{op}`."
        return handler(key)

    # ── generate_outreach ─────────────────────────────────────
    def _generate_outreach(self, key):
        acct = _ACCOUNTS[key]
        stks = _STAKEHOLDERS.get(key, [])
        history = _MESSAGING_HISTORY.get(key, {})

        output = (
            f"**Outreach Drafts: {acct['name']}**\n\n"
            f"Account context: {acct['industry']}, ${acct['revenue']:,} revenue, "
            f"pain points: {', '.join(acct['pain_points'])}\n"
            f"Historical performance: {history.get('avg_open_rate', 0):.0%} open rate, "
            f"{history.get('avg_reply_rate', 0):.0%} reply rate\n"
            f"Best send window: {history.get('best_day', 'Tuesday')} at {history.get('best_time', '9:00 AM')}\n\n"
        )

        for s in stks:
            tier = _engagement_tier(s)
            approach = _recommended_approach(s)
            bench = _RESPONSE_BENCHMARKS[approach]
            tmpl = _EMAIL_TEMPLATES.get(s["email_pref"], _EMAIL_TEMPLATES["concise_technical"])
            subject = _generate_subject(s["email_pref"], acct, acct["pain_points"][0])

            output += (
                f"---\n**To: {s['name']} ({s['role']}) — {s['influence']}**\n"
                f"Engagement tier: {tier.replace('_', ' ').title()} | Approach: {approach.replace('_', ' ').title()}\n"
                f"Expected: {bench['open_rate']:.0%} open / {bench['reply_rate']:.0%} reply\n\n"
                f"**Subject:** {subject}\n"
                f"**Tone:** {tmpl['tone']} (max {tmpl['max_words']} words)\n"
                f"**CTA:** {tmpl['cta_style']}\n\n"
            )

        output += (
            f"Source: [Email Analytics + CRM Engagement History]\n"
            f"Agents: MessagingAgent"
        )
        return output

    # ── create_follow_up ──────────────────────────────────────
    def _create_follow_up(self, key):
        acct = _ACCOUNTS[key]
        stks = _STAKEHOLDERS.get(key, [])
        history = _MESSAGING_HISTORY.get(key, {})

        needs_follow_up = [s for s in stks if s["last_email_days_ago"] is not None and s["last_email_days_ago"] >= 7]
        if not needs_follow_up:
            needs_follow_up = [s for s in stks if s["last_email_days_ago"] is not None]

        output = (
            f"**Follow-Up Drafts: {acct['name']}**\n\n"
            f"Contacts needing follow-up: {len(needs_follow_up)}\n\n"
        )

        for s in needs_follow_up:
            days = s["last_email_days_ago"]
            urgency = "High" if days >= 14 else "Medium" if days >= 7 else "Low"
            opened = "Yes (engaged)" if s["open_rate"] >= 0.60 else "No (re-engage)"

            if s["reply_rate"] >= 0.30:
                follow_up_type = "Value-add: share relevant case study or insight"
            elif s["open_rate"] >= 0.60:
                follow_up_type = "Nudge: brief check-in referencing last conversation"
            else:
                follow_up_type = "Re-engage: new angle via different channel or champion intro"

            output += (
                f"---\n**{s['name']} ({s['role']})**\n"
                f"| Detail | Value |\n|---|---|\n"
                f"| Last Contact | {days} days ago |\n"
                f"| Urgency | {urgency} |\n"
                f"| Opens Previous | {opened} |\n"
                f"| Reply Rate | {s['reply_rate']:.0%} |\n"
                f"| Strategy | {follow_up_type} |\n\n"
            )

        output += (
            f"**Best practices for {acct['name']}:**\n"
            f"- Top-performing subject line: \"{history.get('best_subject', 'N/A')}\"\n"
            f"- Optimal send: {history.get('best_day', 'Tuesday')} at {history.get('best_time', '9:00 AM')}\n\n"
            f"Source: [Email Analytics + Engagement Tracking]\n"
            f"Agents: MessagingAgent"
        )
        return output

    # ── draft_proposal_intro ──────────────────────────────────
    def _draft_proposal_intro(self, key):
        acct = _ACCOUNTS[key]
        stks = _STAKEHOLDERS.get(key, [])

        decision_makers = [s for s in stks if s["influence"] in ("Decision Maker", "Economic Buyer")]
        champions = [s for s in stks if s["influence"] == "Champion"]

        pain_list = "\n".join(f"  {i}. {p.title()}" for i, p in enumerate(acct["pain_points"], 1))
        dm_list = "\n".join(f"  - {s['name']} ({s['role']})" for s in decision_makers) or "  - No decision makers mapped"
        champ_list = "\n".join(f"  - {s['name']} ({s['role']})" for s in champions) or "  - No champions identified"

        savings = int(acct["opportunity_value"] * 1.65)
        impl_weeks = 8 if acct["industry"] == "Manufacturing" else 6

        return (
            f"**Proposal Introduction: {acct['name']}**\n\n"
            f"**Context:**\n"
            f"- Industry: {acct['industry']} | Revenue: ${acct['revenue']:,}\n"
            f"- Current spend: ${acct['current_spend']:,}/yr | Opportunity: ${acct['opportunity_value']:,}\n\n"
            f"**Key Pain Points Addressed:**\n{pain_list}\n\n"
            f"**Proposal Highlights:**\n"
            f"- Projected 3-year savings: ${savings:,}\n"
            f"- Implementation timeline: {impl_weeks} weeks\n"
            f"- Risk-free 90-day pilot included\n"
            f"- Dedicated customer success manager\n\n"
            f"**Distribution:**\n"
            f"Decision Makers:\n{dm_list}\n"
            f"Champions (internal advocates):\n{champ_list}\n\n"
            f"**Recommended Subject:** \"Proposal: Addressing {acct['pain_points'][0]} at {acct['name']}\"\n\n"
            f"**Email Structure:**\n"
            f"1. Reference recent conversation or trigger event\n"
            f"2. Summarize 3 key pain points and proposed solutions\n"
            f"3. Highlight ROI: ${savings:,} over 3 years\n"
            f"4. Attach executive summary (2 pages) + full proposal\n"
            f"5. CTA: 30-minute proposal walkthrough\n\n"
            f"Source: [Proposal Engine + Value Engineering]\n"
            f"Agents: MessagingAgent"
        )

    # ── campaign_sequence ─────────────────────────────────────
    def _campaign_sequence(self, key):
        acct = _ACCOUNTS[key]
        stks = _STAKEHOLDERS.get(key, [])
        history = _MESSAGING_HISTORY.get(key, {})

        total_touches = 7
        sequence = [
            {"day": 1, "channel": "Email", "action": "Personalized intro referencing trigger event", "stakeholders": "All decision makers"},
            {"day": 3, "channel": "LinkedIn", "action": "Connect request with custom note", "stakeholders": "CTO, VP-level"},
            {"day": 5, "channel": "Email", "action": "Value-add: industry case study", "stakeholders": "Technical evaluators"},
            {"day": 8, "channel": "Phone", "action": "Champion check-in call", "stakeholders": "Champion only"},
            {"day": 10, "channel": "Email", "action": "ROI calculator + executive summary", "stakeholders": "Economic buyer"},
            {"day": 14, "channel": "Email", "action": "Peer reference offer", "stakeholders": "Decision maker"},
            {"day": 18, "channel": "Email", "action": "Meeting request with clear agenda", "stakeholders": "Full buying committee"},
        ]

        seq_rows = ""
        for s in sequence:
            seq_rows += f"| Day {s['day']} | {s['channel']} | {s['action']} | {s['stakeholders']} |\n"

        ab_variants = (
            "**A/B Testing Plan:**\n"
            "| Element | Variant A | Variant B |\n|---|---|---|\n"
            f"| Subject Line | Pain-point led | ROI-led |\n"
            f"| CTA | 15-min call | Calendar link |\n"
            f"| Send Time | {history.get('best_day', 'Tuesday')} AM | Thursday PM |\n"
            f"| Tone | Consultative | Direct |\n"
        )

        return (
            f"**Campaign Sequence: {acct['name']}**\n\n"
            f"**Account Profile:**\n"
            f"- {acct['industry']} | {acct['employees']:,} employees | ${acct['opportunity_value']:,} opportunity\n"
            f"- Active sequences: {history.get('sequences_active', 0)} | "
            f"Completed: {history.get('sequences_completed', 0)}\n\n"
            f"**{total_touches}-Touch Sequence:**\n\n"
            f"| Day | Channel | Action | Target |\n|---|---|---|---|\n"
            f"{seq_rows}\n"
            f"{ab_variants}\n"
            f"**Success Metrics:**\n"
            f"- Target open rate: 65%+ (current: {history.get('avg_open_rate', 0):.0%})\n"
            f"- Target reply rate: 30%+ (current: {history.get('avg_reply_rate', 0):.0%})\n"
            f"- Target meeting booked: by Day 18\n\n"
            f"Source: [Campaign Engine + Email Analytics + CRM]\n"
            f"Agents: MessagingAgent"
        )


if __name__ == "__main__":
    agent = MessagingAgent()
    for op in ["generate_outreach", "create_follow_up", "draft_proposal_intro", "campaign_sequence"]:
        print("=" * 60)
        print(agent.perform(operation=op, account_name="Acme Corporation"))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
