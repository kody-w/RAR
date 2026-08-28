---
name: "rar-aibast-agents-library-meeting-prep"
description: "Generates pre-meeting briefs, talking points, objection prep, and follow-up templates from built-in demo account data."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/meeting_prep", "rar_sha256": "4a91d34945375407eebd1affec505833c1c541efadd6d98354d8a15f06ca38b9", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "AIBAST", "tags": ["b2b", "sales", "meeting-prep", "briefing", "objection-handling"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/meeting_prep`. The original RAPP
agent is preserved byte-for-byte in `meeting_prep_agent.py` and in the RCI capsule.

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

Meeting Prep Agent

Generates pre-meeting briefings, talking points, objection preparation,
and follow-up templates for enterprise B2B sales meetings. Combines
account intelligence, stakeholder data, and competitive context into
actionable meeting materials.

Where a real deployment would call CRM and calendar APIs, this agent
uses a synthetic data layer so it runs anywhere without credentials.

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
      "description": "The meeting prep operation",
      "enum": [
        "pre_meeting_brief",
        "talking_points",
        "objection_prep",
        "follow_up_template"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `meeting_prep_agent.py` and embedded as the fenced Python below (sha256 4a91d34945375407…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `meeting_prep_agent.py` first:

```bash
python3 meeting_prep_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 meeting_prep_agent.py   # or on stdin
python3 meeting_prep_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Meeting Prep Agent

Generates pre-meeting briefings, talking points, objection preparation,
and follow-up templates for enterprise B2B sales meetings. Combines
account intelligence, stakeholder data, and competitive context into
actionable meeting materials.

Where a real deployment would call CRM and calendar APIs, this agent
uses a synthetic data layer so it runs anywhere without credentials.
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
    "name": "@aibast-agents-library/meeting_prep",
    "version": "1.0.1",
    "display_name": "Meeting Prep",
    "description": "Generates pre-meeting briefs, talking points, objection prep, and follow-up templates from built-in demo account data.",
    "author": "AIBAST",
    "tags": ["b2b", "sales", "meeting-prep", "briefing", "objection-handling"],
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
        "revenue": 2_800_000_000, "employees": 12_400,
        "current_spend": 1_200_000, "opportunity_value": 2_400_000,
        "products_owned": ["Platform Core", "Analytics Module"],
        "pain_points": ["legacy ERP integration", "manual reporting", "supply chain visibility"],
    },
    "contoso": {
        "id": "acc-002", "name": "Contoso Ltd", "industry": "Technology",
        "revenue": 980_000_000, "employees": 4_200,
        "current_spend": 680_000, "opportunity_value": 1_100_000,
        "products_owned": ["Platform Core"],
        "pain_points": ["scaling data infrastructure", "EMEA compliance", "vendor consolidation"],
    },
    "fabrikam": {
        "id": "acc-003", "name": "Fabrikam Industries", "industry": "Manufacturing",
        "revenue": 1_500_000_000, "employees": 8_700,
        "current_spend": 450_000, "opportunity_value": 890_000,
        "products_owned": ["Analytics Module"],
        "pain_points": ["production downtime analytics", "quality control automation", "workforce scheduling"],
    },
    "northwind": {
        "id": "acc-004", "name": "Northwind Traders", "industry": "Retail",
        "revenue": 620_000_000, "employees": 3_100,
        "current_spend": 220_000, "opportunity_value": 540_000,
        "products_owned": [],
        "pain_points": ["omnichannel inventory", "customer data platform", "last-mile logistics"],
    },
}

_UPCOMING_MEETINGS = {
    "acme": [
        {
            "id": "mtg-001", "title": "Executive Strategy Review",
            "date": "2025-03-15", "time": "10:00 AM CT", "duration_min": 60,
            "location": "Zoom (Executive Boardroom)",
            "our_attendees": ["Michael Torres (AE)", "Jennifer Walsh (SE)", "Mark Stevens (VP Sales)"],
            "their_attendees": [
                {"name": "Sarah Chen", "role": "CTO", "sentiment": "Unknown", "meetings_prior": 0},
                {"name": "James Miller", "role": "VP Operations", "sentiment": "Positive", "meetings_prior": 14},
                {"name": "Lisa Park", "role": "CFO", "sentiment": "Neutral", "meetings_prior": 2},
            ],
            "objective": "Present expansion proposal and secure CTO alignment",
            "deal_stage": "Proposal", "deal_value": 2_400_000,
        },
    ],
    "contoso": [
        {
            "id": "mtg-002", "title": "Renewal Discussion + Expansion",
            "date": "2025-03-18", "time": "2:00 PM PT", "duration_min": 45,
            "location": "Microsoft Teams",
            "our_attendees": ["Michael Torres (AE)", "Sarah Kim (CSM)"],
            "their_attendees": [
                {"name": "Alex Kim", "role": "CTO", "sentiment": "Positive", "meetings_prior": 10},
                {"name": "Pat Johnson", "role": "CFO", "sentiment": "Neutral", "meetings_prior": 3},
            ],
            "objective": "Finalize renewal terms and introduce expansion options",
            "deal_stage": "Negotiation", "deal_value": 1_100_000,
        },
    ],
    "fabrikam": [
        {
            "id": "mtg-003", "title": "Discovery Workshop",
            "date": "2025-03-21", "time": "9:00 AM ET", "duration_min": 90,
            "location": "On-site (Detroit office)",
            "our_attendees": ["Michael Torres (AE)", "Jennifer Walsh (SE)"],
            "their_attendees": [
                {"name": "Chris Anderson", "role": "VP IT", "sentiment": "Neutral", "meetings_prior": 4},
                {"name": "Dana White", "role": "COO", "sentiment": "Positive", "meetings_prior": 6},
            ],
            "objective": "Deep-dive into production analytics requirements",
            "deal_stage": "Discovery", "deal_value": 890_000,
        },
    ],
    "northwind": [
        {
            "id": "mtg-004", "title": "Initial Discovery Call",
            "date": "2025-03-22", "time": "11:00 AM PT", "duration_min": 30,
            "location": "Zoom",
            "our_attendees": ["Michael Torres (AE)"],
            "their_attendees": [
                {"name": "Jordan Lee", "role": "CTO", "sentiment": "Unknown", "meetings_prior": 1},
            ],
            "objective": "Understand e-commerce platform needs and qualify opportunity",
            "deal_stage": "Qualification", "deal_value": 540_000,
        },
    ],
}

_MEETING_HISTORY = {
    "acme": [
        {"date": "2025-03-10", "title": "Technical Architecture Review", "attendees": 4, "outcome": "Positive — David Wong endorsed API approach", "action_items": ["Send integration guide", "Schedule SE deep dive"]},
        {"date": "2025-02-28", "title": "CFO Business Case Review", "attendees": 3, "outcome": "Neutral — Lisa requested ROI calculator", "action_items": ["Build customized ROI model", "Send reference customer contacts"]},
        {"date": "2025-02-15", "title": "Procurement Introduction", "attendees": 2, "outcome": "Neutral — standard process initiated", "action_items": ["Submit vendor questionnaire", "Provide security documentation"]},
    ],
    "contoso": [
        {"date": "2025-03-11", "title": "Product Roadmap Preview", "attendees": 3, "outcome": "Positive — Sam excited about new features", "action_items": ["Send beta access details", "Schedule expansion discussion"]},
    ],
    "fabrikam": [
        {"date": "2025-03-04", "title": "Platform Demo", "attendees": 2, "outcome": "Neutral — Chris wants to see manufacturing-specific features", "action_items": ["Prepare manufacturing demo environment", "Share case study"]},
    ],
    "northwind": [
        {"date": "2025-02-12", "title": "Initial Intro Call", "attendees": 2, "outcome": "Positive — Jordan interested in omnichannel capabilities", "action_items": ["Send retail case studies", "Prepare discovery questions"]},
    ],
}

_COMMON_OBJECTIONS = {
    "price": {
        "objection": "Your solution is more expensive than alternatives",
        "response": "When factoring total cost of ownership including implementation, support, and time-to-value, our 3-year TCO is actually 23% lower. Let me walk you through the comparison.",
        "proof_points": ["47 similar deployments at 94% success rate", "8-week implementation vs 14+ weeks for alternatives", "Dedicated CSM included at no extra cost"],
    },
    "risk": {
        "objection": "We're concerned about implementation risk and disruption",
        "response": "We offer a 90-day proof-of-value pilot with full rollback capability. In manufacturing deployments our size, we've achieved 94% on-time delivery.",
        "proof_points": ["Phased rollout approach minimizes disruption", "Dedicated implementation team", "3 reference customers in your industry available"],
    },
    "incumbent": {
        "objection": "We already have a solution that works",
        "response": "I understand the value of continuity. Our customers who switched found that integration capabilities and real-time analytics delivered ROI within the first quarter.",
        "proof_points": ["Average 3.2x productivity improvement", "Native ERP integration vs custom connectors", "Real-time dashboards vs batch reporting"],
    },
    "timing": {
        "objection": "This isn't the right time / we need to wait until next budget cycle",
        "response": "I understand budget timing. Our flexible licensing allows us to start with a pilot this quarter and scale in the next budget cycle. This gives your team a head start.",
        "proof_points": ["Pilot program with deferred billing", "Quarterly payment options", "ROI typically visible within 90 days"],
    },
    "internal": {
        "objection": "We're considering building this internally",
        "response": "Build vs buy is an important consideration. Our analysis shows that internal builds take 3-5x longer and cost 2-4x more when factoring in maintenance and opportunity cost.",
        "proof_points": ["Average internal build takes 18+ months", "Ongoing maintenance costs often exceed license fees", "Our roadmap delivers features faster than internal teams"],
    },
}

_FOLLOW_UP_TEMPLATES = {
    "executive": {
        "subject": "Follow-up: {meeting_title} — Next Steps",
        "sections": ["Thank you and key takeaways", "Agreed action items with owners", "Proposed timeline", "Attached materials"],
        "tone": "Professional, concise, action-oriented",
        "send_within": "2 hours",
    },
    "technical": {
        "subject": "Technical Follow-up: {meeting_title}",
        "sections": ["Technical requirements summary", "Architecture recommendations", "Integration approach", "POC proposal"],
        "tone": "Technical, detailed, solution-focused",
        "send_within": "4 hours",
    },
    "discovery": {
        "subject": "Great conversation — {meeting_title} Summary",
        "sections": ["Pain points discussed", "Proposed approach", "Suggested next steps", "Relevant resources"],
        "tone": "Consultative, educational, helpful",
        "send_within": "Same day",
    },
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


def _attendee_prep_level(attendee):
    """Classify how much prep is needed for each attendee."""
    if attendee["meetings_prior"] == 0:
        return "Full Research"
    if attendee["sentiment"] == "Unknown":
        return "Sentiment Discovery"
    if attendee["sentiment"] == "Neutral":
        return "Value Reinforcement"
    return "Relationship Building"


def _meeting_risk_level(meeting):
    """Assess meeting risk based on attendee composition."""
    unknown_sentiment = sum(1 for a in meeting["their_attendees"] if a["sentiment"] == "Unknown")
    first_meetings = sum(1 for a in meeting["their_attendees"] if a["meetings_prior"] == 0)
    if first_meetings >= 2 or unknown_sentiment >= 2:
        return "High"
    if first_meetings >= 1 or unknown_sentiment >= 1:
        return "Medium"
    return "Low"


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class MeetingPrepAgent(BasicAgent):
    """
    Prepares comprehensive meeting materials for B2B sales.

    Operations:
        pre_meeting_brief  - full meeting briefing document
        talking_points     - stakeholder-specific talking points
        objection_prep     - objection handling preparation
        follow_up_template - post-meeting follow-up draft
    """

    def __init__(self):
        self.name = "MeetingPrepAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "pre_meeting_brief", "talking_points",
                            "objection_prep", "follow_up_template",
                        ],
                        "description": "The meeting prep operation",
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
        op = kwargs.get("operation", "pre_meeting_brief")
        key = _resolve_account(kwargs.get("account_name", ""))
        dispatch = {
            "pre_meeting_brief": self._pre_meeting_brief,
            "talking_points": self._talking_points,
            "objection_prep": self._objection_prep,
            "follow_up_template": self._follow_up_template,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"**Error:** Unknown operation `{op}`."
        return handler(key)

    # ── pre_meeting_brief ─────────────────────────────────────
    def _pre_meeting_brief(self, key):
        acct = _ACCOUNTS[key]
        meetings = _UPCOMING_MEETINGS.get(key, [])
        history = _MEETING_HISTORY.get(key, [])

        if not meetings:
            return f"**Meeting Brief: {acct['name']}**\n\nNo upcoming meetings scheduled."

        mtg = meetings[0]
        risk_level = _meeting_risk_level(mtg)

        attendee_rows = ""
        for a in mtg["their_attendees"]:
            prep = _attendee_prep_level(a)
            attendee_rows += (
                f"| {a['name']} | {a['role']} | {a['sentiment']} | "
                f"{a['meetings_prior']} | {prep} |\n"
            )

        our_team = "\n".join(f"- {a}" for a in mtg["our_attendees"])

        recent_history = ""
        if history:
            recent_history = "\n**Recent Meeting History:**\n"
            for h in history[:3]:
                recent_history += f"- {h['date']}: {h['title']} — {h['outcome']}\n"
                if h["action_items"]:
                    for ai in h["action_items"]:
                        recent_history += f"  - Action: {ai}\n"

        return (
            f"**Pre-Meeting Brief: {mtg['title']}**\n\n"
            f"| Detail | Value |\n|---|---|\n"
            f"| Account | {acct['name']} ({acct['industry']}) |\n"
            f"| Date/Time | {mtg['date']} at {mtg['time']} |\n"
            f"| Duration | {mtg['duration_min']} minutes |\n"
            f"| Location | {mtg['location']} |\n"
            f"| Objective | {mtg['objective']} |\n"
            f"| Deal Stage | {mtg['deal_stage']} |\n"
            f"| Deal Value | ${mtg['deal_value']:,} |\n"
            f"| Meeting Risk | {risk_level} |\n\n"
            f"**Their Attendees:**\n\n"
            f"| Name | Role | Sentiment | Prior Meetings | Prep Level |\n|---|---|---|---|---|\n"
            f"{attendee_rows}\n"
            f"**Our Team:**\n{our_team}\n\n"
            f"**Account Context:**\n"
            f"- Revenue: ${acct['revenue']:,} | Employees: {acct['employees']:,}\n"
            f"- Current spend: ${acct['current_spend']:,}/yr | Opportunity: ${acct['opportunity_value']:,}\n"
            f"- Products owned: {', '.join(acct['products_owned']) or 'None'}\n"
            f"- Pain points: {', '.join(acct['pain_points'])}\n"
            f"{recent_history}\n"
            f"Source: [CRM + Calendar + Meeting Intelligence]\n"
            f"Agents: MeetingPrepAgent"
        )

    # ── talking_points ────────────────────────────────────────
    def _talking_points(self, key):
        acct = _ACCOUNTS[key]
        meetings = _UPCOMING_MEETINGS.get(key, [])

        if not meetings:
            return f"**Talking Points: {acct['name']}**\n\nNo upcoming meetings scheduled."

        mtg = meetings[0]
        output = f"**Talking Points: {mtg['title']}**\n\n"

        for a in mtg["their_attendees"]:
            role = a["role"]
            output += f"---\n**For {a['name']} ({role}):**\n\n"

            if any(t in role for t in ("CTO", "IT", "Engineering", "VP IT")):
                output += (
                    f"**Theme: Technical Vision & Architecture**\n"
                    f"- \"Our API-first architecture integrates natively with your existing {acct['industry'].lower()} systems\"\n"
                    f"- \"We've reduced integration timelines by 60% with our pre-built connectors\"\n"
                    f"- \"Three {acct['industry'].lower()} CTOs are available for a peer conversation\"\n\n"
                )
            elif any(t in role for t in ("CFO", "Finance")):
                savings = int(acct["opportunity_value"] * 1.75)
                output += (
                    f"**Theme: ROI & Business Value**\n"
                    f"- \"${savings:,} projected savings over 3 years based on similar deployments\"\n"
                    f"- \"8-week implementation means faster time-to-value than any alternative\"\n"
                    f"- \"90-day proof-of-value pilot — no commitment until you see results\"\n\n"
                )
            elif any(t in role for t in ("Operations", "COO")):
                output += (
                    f"**Theme: Operational Excellence**\n"
                    f"- \"Real-time dashboards replace manual reporting, saving 15+ hours per week\"\n"
                    f"- \"Predictive analytics identify issues before they impact production\"\n"
                    f"- \"Your team becomes the transformation leaders within {acct['name']}\"\n\n"
                )
            elif any(t in role for t in ("Product", "VP Product")):
                output += (
                    f"**Theme: Product Capability & Roadmap**\n"
                    f"- \"Our platform scales with your growth — supporting 10x current volume\"\n"
                    f"- \"Co-innovation partnership for industry-specific features\"\n"
                    f"- \"Quarterly product council with direct influence on roadmap\"\n\n"
                )
            else:
                output += (
                    f"**Theme: Strategic Partnership**\n"
                    f"- \"We're investing in long-term partnership, not just a transaction\"\n"
                    f"- \"Dedicated executive sponsor and customer success team\"\n"
                    f"- \"Quarterly business reviews to ensure continuous value delivery\"\n\n"
                )

        output += (
            f"**Universal Proof Points:**\n"
            f"- 94% customer retention rate\n"
            f"- 47 deployments in {acct['industry'].lower()} industry\n"
            f"- 8-week average implementation time\n"
            f"- 24/7 dedicated support with named CSM\n\n"
            f"Source: [Sales Playbook + Value Engineering + References]\n"
            f"Agents: MeetingPrepAgent"
        )
        return output

    # ── objection_prep ────────────────────────────────────────
    def _objection_prep(self, key):
        acct = _ACCOUNTS[key]
        meetings = _UPCOMING_MEETINGS.get(key, [])

        # Determine likely objections based on meeting context
        likely = []
        if meetings:
            mtg = meetings[0]
            for a in mtg["their_attendees"]:
                if "CFO" in a["role"] or "Finance" in a["role"]:
                    likely.extend(["price", "timing"])
                if a["sentiment"] == "Unknown":
                    likely.extend(["risk", "incumbent"])
                if a["meetings_prior"] == 0:
                    likely.append("risk")

        likely = list(dict.fromkeys(likely))  # dedupe preserving order
        if not likely:
            likely = list(_COMMON_OBJECTIONS.keys())

        output = f"**Objection Preparation: {acct['name']}**\n\n"
        output += f"Likely objections based on attendee analysis: {len(likely)}\n\n"

        for obj_key in likely:
            obj = _COMMON_OBJECTIONS.get(obj_key)
            if not obj:
                continue

            output += (
                f"---\n**Objection: \"{obj['objection']}\"**\n\n"
                f"**Recommended Response:**\n"
                f"\"{obj['response']}\"\n\n"
                f"**Proof Points:**\n"
                + "".join(f"- {p}\n" for p in obj["proof_points"])
                + "\n"
            )

        output += (
            f"**General Objection Handling Tips:**\n"
            f"1. Acknowledge the concern before responding\n"
            f"2. Ask clarifying questions to understand the root issue\n"
            f"3. Use specific data points and customer references\n"
            f"4. Offer concrete next steps to address the concern\n\n"
            f"Source: [Sales Playbook + Win/Loss Analysis + Customer References]\n"
            f"Agents: MeetingPrepAgent"
        )
        return output

    # ── follow_up_template ────────────────────────────────────
    def _follow_up_template(self, key):
        acct = _ACCOUNTS[key]
        meetings = _UPCOMING_MEETINGS.get(key, [])
        history = _MEETING_HISTORY.get(key, [])

        if not meetings:
            return f"**Follow-Up Template: {acct['name']}**\n\nNo upcoming meetings to prepare follow-up for."

        mtg = meetings[0]

        # Select template based on meeting type
        if mtg["deal_stage"] in ("Qualification", "Discovery"):
            tmpl = _FOLLOW_UP_TEMPLATES["discovery"]
        elif any("CTO" in a["role"] or "Engineering" in a["role"] for a in mtg["their_attendees"]):
            tmpl = _FOLLOW_UP_TEMPLATES["technical"]
        else:
            tmpl = _FOLLOW_UP_TEMPLATES["executive"]

        subject = tmpl["subject"].format(meeting_title=mtg["title"])
        sections = "\n".join(f"  {i}. {s}" for i, s in enumerate(tmpl["sections"], 1))

        # Build action items from recent history
        recent_actions = ""
        if history:
            recent_actions = "\n**Open Action Items from Previous Meetings:**\n"
            for h in history[:2]:
                for ai in h.get("action_items", []):
                    recent_actions += f"- {ai} (from {h['date']})\n"

        attendee_list = ", ".join(f"{a['name']} ({a['role']})" for a in mtg["their_attendees"])

        return (
            f"**Follow-Up Template: {mtg['title']}**\n\n"
            f"| Detail | Value |\n|---|---|\n"
            f"| Subject | {subject} |\n"
            f"| Tone | {tmpl['tone']} |\n"
            f"| Send Within | {tmpl['send_within']} |\n"
            f"| Recipients | {attendee_list} |\n\n"
            f"**Email Structure:**\n{sections}\n\n"
            f"**Draft Opening:**\n"
            f"\"Thank you for your time today discussing {mtg['objective'].lower()}. "
            f"I wanted to summarize our key discussion points and confirm next steps.\"\n\n"
            f"**Key Attachments to Include:**\n"
            f"- Meeting summary (1 page)\n"
            f"- Relevant case study for {acct['industry'].lower()}\n"
            f"- Proposal or technical documentation as discussed\n"
            f"- Calendar invite for next meeting\n"
            f"{recent_actions}\n"
            f"**Draft Closing:**\n"
            f"\"I'll follow up on [action items] by [date]. In the meantime, please don't "
            f"hesitate to reach out with any questions. Looking forward to our next conversation.\"\n\n"
            f"Source: [Meeting Templates + CRM + Action Items]\n"
            f"Agents: MeetingPrepAgent"
        )


if __name__ == "__main__":
    agent = MeetingPrepAgent()
    for op in ["pre_meeting_brief", "talking_points", "objection_prep", "follow_up_template"]:
        print("=" * 60)
        print(agent.perform(operation=op, account_name="Acme Corporation"))
        print()
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
