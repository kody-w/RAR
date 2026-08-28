---
name: "rar-aibast-agents-library-email-drafting"
description: "Drafts outreach, follow-up, and proposal emails personalized with live contacts from a simulated Dynamics 365 tenant, with offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/email_drafting", "rar_sha256": "6cb8018cf57e5ca33f015292300508a7448bff5686d3cf03c0451d38498ef674", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["email", "drafting", "outreach", "follow-up", "proposal", "templates"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/email_drafting`. The original RAPP
agent is preserved byte-for-byte in `email_drafting_agent.py` and in the RCI capsule.

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

Email Drafting Agent — a template you are meant to mutate.

Drafts outreach, follow-up, and proposal emails with tone control and
personalization, pulling the recipient's real name, title, and company
from CRM so every draft starts grounded in an actual contact record.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM contacts and accounts over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="draft_outreach", contact_name="Marcus Webb")
     — drafts to the tenant's real seeded contact (Member Services
     Manager at Bluegrass Credit Union).
  2. No network? Everything falls back to the embedded demo layer below
     (_SAMPLE_CONTEXT / _EMAIL_TEMPLATES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     EMAIL_DRAFTING_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from Salesforce/HubSpot), or replace
     _fetch_collection() with calls into your own API. The fields the
     rest of the file needs are listed in _normalize_live_contact() —
     everything else keeps working untouched. Bracketed fields in the
     drafts (pain point, observation, ROI) are enrichment seams — wire
     your notes, intent data, or news feed there.

OPERATIONS
  draft_outreach | draft_follow_up | draft_proposal | template_library
  kwargs: operation (required), template_key, contact_name (any live
  tenant contact or the embedded demo contact)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "The email drafting operation to perform",
      "enum": [
        "draft_outreach",
        "draft_follow_up",
        "draft_proposal",
        "template_library"
      ],
      "type": "string"
    },
    "template_key": {
      "description": "Template key (e.g. 'cold_outreach')",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `email_drafting_agent.py` and embedded as the fenced Python below (sha256 6cb8018cf57e5ca3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `email_drafting_agent.py` first:

```bash
python3 email_drafting_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 email_drafting_agent.py   # or on stdin
python3 email_drafting_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Email Drafting Agent — a template you are meant to mutate.

Drafts outreach, follow-up, and proposal emails with tone control and
personalization, pulling the recipient's real name, title, and company
from CRM so every draft starts grounded in an actual contact record.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live CRM contacts and accounts over real HTTP
     from the globally hosted Static Dynamics 365 tenant (Aster Lane
     Office Systems — synthetic data, no credentials, works from anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="draft_outreach", contact_name="Marcus Webb")
     — drafts to the tenant's real seeded contact (Member Services
     Manager at Bluegrass Credit Union).
  2. No network? Everything falls back to the embedded demo layer below
     (_SAMPLE_CONTEXT / _EMAIL_TEMPLATES) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     EMAIL_DRAFTING_DATA_URL to any OData-shaped endpoint (your real
     Dynamics org, or JSON exported from Salesforce/HubSpot), or replace
     _fetch_collection() with calls into your own API. The fields the
     rest of the file needs are listed in _normalize_live_contact() —
     everything else keeps working untouched. Bracketed fields in the
     drafts (pain point, observation, ROI) are enrichment seams — wire
     your notes, intent data, or news feed there.

OPERATIONS
  draft_outreach | draft_follow_up | draft_proposal | template_library
  kwargs: operation (required), template_key, contact_name (any live
  tenant contact or the embedded demo contact)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
import json
import urllib.request

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/email_drafting",
    "version": "1.1.0",
    "display_name": "Email Drafting",
    "description": "Drafts outreach, follow-up, and proposal emails personalized with live contacts from a simulated Dynamics 365 tenant, with offline fallback.",
    "author": "AIBAST",
    "tags": ["email", "drafting", "outreach", "follow-up", "proposal", "templates"],
    "category": "general",
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
#   export EMAIL_DRAFTING_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your CRM client. Downstream code
# only needs the fields produced by _normalize_live_contact().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "EMAIL_DRAFTING_DATA_URL",
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


def _normalize_live_contact(row, accounts_by_name):
    """Project a Dynamics contact record onto the context dict the email
    templates use. THIS is the contract your replacement data source must
    meet — the personalization keys below. Bracketed values mean 'the CRM
    alone cannot know this' and mark enrichment seams (wire your notes,
    intent, or news data there)."""
    company = row.get("parentcustomeridname", "their company")
    account = accounts_by_name.get(company, {})
    return {
        "first_name": row.get("firstname", "there"),
        "last_name": row.get("lastname", ""),
        "title": row.get("jobtitle", ""),
        "company_name": company,
        "industry": account.get("industrycode", "their industry"),
        "email": row.get("emailaddress1", ""),
        # Enrichment seams — no CRM field carries these; wire your own data:
        "pain_point": "[pain_point — enrichment seam: wire your notes/intent data]",
        "observation": "[observation — enrichment seam: wire your news feed]",
        "topic": "[topic — enrichment seam]",
        "original_subject": "[original_subject — enrichment seam]",
        "value_prop_one_liner": "[value_prop — enrichment seam]",
        "product_name": _SAMPLE_CONTEXT["product_name"],
        "reference_customer": _SAMPLE_CONTEXT["reference_customer"],
        "result": _SAMPLE_CONTEXT["result"],
        "sender_name": _SAMPLE_CONTEXT["sender_name"],
        "sender_title": _SAMPLE_CONTEXT["sender_title"],
        "meeting_date": _SAMPLE_CONTEXT["meeting_date"],
        "meeting_topic": _SAMPLE_CONTEXT["meeting_topic"],
        "pricing": _SAMPLE_CONTEXT["pricing"],
        "roi_projection": _SAMPLE_CONTEXT["roi_projection"],
        "time_slot_1": _SAMPLE_CONTEXT["time_slot_1"],
        "time_slot_2": _SAMPLE_CONTEXT["time_slot_2"],
        "_live": True,
    }


def _live_contact_roster():
    """fullname-keyed dict of live tenant contacts; {} when offline."""
    contacts = _fetch_collection("contacts")
    if not contacts:
        return {}
    accounts_by_name = {
        a.get("name", ""): a for a in _fetch_collection("accounts")
    }
    return {
        c["fullname"].lower(): _normalize_live_contact(c, accounts_by_name)
        for c in contacts
        if c.get("fullname")
    }


def _resolve_context(query):
    """Embedded demo contact first, then the live tenant roster."""
    q = (query or "").lower().strip()
    if not q or q in "jennifer walsh" or "techvantage" in q:
        return dict(_SAMPLE_CONTEXT), False
    roster = _live_contact_roster()
    for name, ctx in roster.items():
        if q in name or q in ctx["company_name"].lower():
            return ctx, True
    return dict(_SAMPLE_CONTEXT), False


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_EMAIL_TEMPLATES = {
    "cold_outreach": {
        "name": "Cold Outreach", "category": "Prospecting",
        "subject_variants": [
            "{company_name} + {our_product} - Quick Question",
            "Idea for {company_name}'s {pain_point}",
            "{first_name}, saw your post on {topic}",
        ],
        "body": "Hi {first_name},\n\nI noticed {company_name} has been {observation}. Many {industry} leaders we work with have faced similar challenges around {pain_point}.\n\nWe helped {reference_customer} achieve {result} using our {product_name}.\n\nWould you be open to a 15-minute call next week to explore if we could deliver similar results for your team?\n\nBest regards,\n{sender_name}\n{sender_title}",
        "tone": "Professional, consultative",
        "avg_open_rate": 0.32, "avg_reply_rate": 0.08,
    },
    "follow_up_no_reply": {
        "name": "Follow-Up (No Reply)", "category": "Follow-Up",
        "subject_variants": [
            "Re: {original_subject}",
            "Quick follow-up, {first_name}",
            "Still relevant, {first_name}?",
        ],
        "body": "Hi {first_name},\n\nI wanted to follow up on my previous email about {topic}. I understand you're busy, so I'll keep this brief.\n\n{value_prop_one_liner}\n\nI have a few times available this week if you'd like to connect:\n- {time_slot_1}\n- {time_slot_2}\n\nIf the timing isn't right, no worries - just let me know and I'll circle back later.\n\nBest,\n{sender_name}",
        "tone": "Friendly, low-pressure",
        "avg_open_rate": 0.28, "avg_reply_rate": 0.12,
    },
    "proposal_intro": {
        "name": "Proposal Introduction", "category": "Proposal",
        "subject_variants": [
            "Proposal: {project_name} for {company_name}",
            "{company_name} Partnership Proposal",
        ],
        "body": "Dear {first_name},\n\nThank you for the productive conversation on {meeting_date}. As discussed, I'm pleased to share our proposal for {project_name}.\n\n**Executive Summary:**\n{executive_summary}\n\n**Investment:** {pricing}\n**Timeline:** {timeline}\n**Expected ROI:** {roi_projection}\n\nThe attached document contains the full proposal with technical specifications, implementation plan, and customer references.\n\nI'd welcome the opportunity to walk through this with your team. Would {proposed_meeting_date} work for a review session?\n\nBest regards,\n{sender_name}\n{sender_title}",
        "tone": "Formal, value-focused",
        "avg_open_rate": 0.65, "avg_reply_rate": 0.45,
    },
    "meeting_follow_up": {
        "name": "Post-Meeting Follow-Up", "category": "Follow-Up",
        "subject_variants": [
            "Great meeting, {first_name} - Next steps",
            "Summary: {meeting_topic} discussion",
        ],
        "body": "Hi {first_name},\n\nThank you for your time today discussing {meeting_topic}. Here's a quick recap:\n\n**Key Discussion Points:**\n{discussion_points}\n\n**Action Items:**\n{action_items}\n\n**Next Steps:**\n{next_steps}\n\nPlease let me know if I missed anything or if you have questions.\n\nBest,\n{sender_name}",
        "tone": "Professional, action-oriented",
        "avg_open_rate": 0.72, "avg_reply_rate": 0.38,
    },
}

_PERSONALIZATION_FIELDS = {
    "recipient": ["first_name", "last_name", "title", "company_name", "industry"],
    "context": ["pain_point", "observation", "topic", "meeting_date", "meeting_topic"],
    "value": ["product_name", "reference_customer", "result", "roi_projection", "pricing"],
    "sender": ["sender_name", "sender_title", "sender_email", "sender_phone"],
    "scheduling": ["time_slot_1", "time_slot_2", "proposed_meeting_date"],
}

_TONE_SETTINGS = {
    "professional": {"formality": "High", "warmth": "Medium", "urgency": "Low", "use_case": "Enterprise outreach, formal proposals"},
    "consultative": {"formality": "Medium", "warmth": "High", "urgency": "Low", "use_case": "Discovery calls, advisory communications"},
    "friendly": {"formality": "Low", "warmth": "High", "urgency": "Low", "use_case": "Follow-ups, relationship maintenance"},
    "urgent": {"formality": "Medium", "warmth": "Low", "urgency": "High", "use_case": "Time-sensitive offers, renewal deadlines"},
    "executive": {"formality": "High", "warmth": "Low", "urgency": "Medium", "use_case": "C-suite communications, board summaries"},
}

_SAMPLE_CONTEXT = {
    "first_name": "Jennifer", "last_name": "Walsh", "title": "VP of Operations",
    "company_name": "TechVantage Solutions", "industry": "Technology",
    "pain_point": "operational efficiency", "observation": "expanding rapidly into new markets",
    "topic": "digital transformation", "product_name": "Enterprise Platform",
    "reference_customer": "Meridian Corp", "result": "35% improvement in operational throughput",
    "sender_name": "Alex Rivera", "sender_title": "Account Executive",
    "meeting_date": "November 12", "meeting_topic": "platform evaluation",
    "pricing": "$185,000/year", "roi_projection": "3.2x within 18 months",
    "time_slot_1": "Tuesday 2:00 PM", "time_slot_2": "Thursday 10:00 AM",
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _render_template(template_key, context):
    template = _EMAIL_TEMPLATES.get(template_key, {})
    body = template.get("body", "")
    for key, value in context.items():
        body = body.replace(f"{{{key}}}", str(value))
    subject = template["subject_variants"][0] if template.get("subject_variants") else "No Subject"
    for key, value in context.items():
        subject = subject.replace(f"{{{key}}}", str(value))
    return subject, body


def _count_personalization_tokens(template_body):
    count = 0
    i = 0
    while i < len(template_body):
        if template_body[i] == '{':
            j = template_body.find('}', i)
            if j != -1:
                count += 1
                i = j + 1
            else:
                i += 1
        else:
            i += 1
    return count


def _recipient_line(context, is_live):
    name = f"{context['first_name']} {context.get('last_name', '')}".strip()
    if is_live and context.get("email"):
        return f"{name} <{context['email']}>"
    return f"{name} <{context['first_name'].lower()}.{context.get('last_name', 'x').lower()}@techvantage.com>"


def _source_line(is_live):
    if is_live:
        return "Contact source: LIVE Dynamics 365 tenant (Aster Lane Office Systems)"
    return "Contact source: embedded demo layer (simulated)"


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class EmailDraftingAgent(BasicAgent):
    """
    Email drafting assistant.

    Operations:
        draft_outreach   - compose initial outreach emails
        draft_follow_up  - compose follow-up emails
        draft_proposal   - compose proposal introduction emails
        template_library - browse and inspect email templates
    """

    def __init__(self):
        self.name = "EmailDraftingAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "draft_outreach", "draft_follow_up",
                            "draft_proposal", "template_library",
                        ],
                        "description": "The email drafting operation to perform",
                    },
                    "template_key": {
                        "type": "string",
                        "description": "Template key (e.g. 'cold_outreach')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "template_library")
        dispatch = {
            "draft_outreach": self._draft_outreach,
            "draft_follow_up": self._draft_follow_up,
            "draft_proposal": self._draft_proposal,
            "template_library": self._template_library,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(kwargs)

    # ── draft_outreach ─────────────────────────────────────────
    def _draft_outreach(self, params):
        context, is_live = _resolve_context(params.get("contact_name", ""))
        subject, body = _render_template("cold_outreach", context)
        t = _EMAIL_TEMPLATES["cold_outreach"]
        return (
            f"**Draft: Cold Outreach Email**\n\n"
            f"**To:** {_recipient_line(context, is_live)}\n"
            f"**Subject:** {subject}\n"
            f"**Tone:** {t['tone']}\n\n"
            f"---\n\n{body}\n\n---\n\n"
            f"**Performance Benchmarks:**\n"
            f"- Avg Open Rate: {t['avg_open_rate']:.0%}\n"
            f"- Avg Reply Rate: {t['avg_reply_rate']:.0%}\n\n"
            f"**Subject Line Variants:**\n"
            + "\n".join(f"- {s}" for s in t["subject_variants"]) + "\n\n"
            f"{_source_line(is_live)}\n"
            f"Source: [Email Template Engine]\nAgents: EmailDraftingAgent"
        )

    # ── draft_follow_up ────────────────────────────────────────
    def _draft_follow_up(self, params):
        context, is_live = _resolve_context(params.get("contact_name", ""))
        subject, body = _render_template("follow_up_no_reply", context)
        t = _EMAIL_TEMPLATES["follow_up_no_reply"]
        return (
            f"**Draft: Follow-Up Email**\n\n"
            f"**To:** {_recipient_line(context, is_live)}\n"
            f"**Subject:** {subject}\n"
            f"**Tone:** {t['tone']}\n\n"
            f"---\n\n{body}\n\n---\n\n"
            f"**Performance Benchmarks:**\n"
            f"- Avg Open Rate: {t['avg_open_rate']:.0%}\n"
            f"- Avg Reply Rate: {t['avg_reply_rate']:.0%}\n\n"
            f"**Best Practices:**\n"
            f"- Send 3-5 business days after initial email\n"
            f"- Keep under 100 words\n"
            f"- Include specific time slots\n"
            f"- Provide easy opt-out\n\n"
            f"{_source_line(is_live)}\n"
            f"Source: [Email Template Engine]\nAgents: EmailDraftingAgent"
        )

    # ── draft_proposal ─────────────────────────────────────────
    def _draft_proposal(self, params):
        context, is_live = _resolve_context(params.get("contact_name", ""))
        subject, body = _render_template("proposal_intro", context)
        t = _EMAIL_TEMPLATES["proposal_intro"]
        return (
            f"**Draft: Proposal Introduction Email**\n\n"
            f"**To:** {_recipient_line(context, is_live)}\n"
            f"**Subject:** {subject}\n"
            f"**Tone:** {t['tone']}\n\n"
            f"---\n\n{body}\n\n---\n\n"
            f"**Performance Benchmarks:**\n"
            f"- Avg Open Rate: {t['avg_open_rate']:.0%}\n"
            f"- Avg Reply Rate: {t['avg_reply_rate']:.0%}\n\n"
            f"**Attachments Suggested:**\n"
            f"- Full proposal PDF\n"
            f"- ROI calculator spreadsheet\n"
            f"- Customer reference one-pager\n\n"
            f"{_source_line(is_live)}\n"
            f"Source: [Email Template Engine]\nAgents: EmailDraftingAgent"
        )

    # ── template_library ───────────────────────────────────────
    def _template_library(self, params):
        template_rows = ""
        for key, t in _EMAIL_TEMPLATES.items():
            tokens = _count_personalization_tokens(t["body"])
            template_rows += f"| {key} | {t['name']} | {t['category']} | {t['avg_open_rate']:.0%} | {t['avg_reply_rate']:.0%} | {tokens} |\n"
        tone_rows = ""
        for tone, settings in _TONE_SETTINGS.items():
            tone_rows += f"| {tone.title()} | {settings['formality']} | {settings['warmth']} | {settings['urgency']} | {settings['use_case'][:40]} |\n"
        field_categories = "\n".join(f"- **{cat.title()}:** {', '.join(fields)}" for cat, fields in _PERSONALIZATION_FIELDS.items())
        return (
            f"**Email Template Library** (simulated benchmark data)\n\n"
            f"| Key | Name | Category | Open Rate | Reply Rate | Tokens |\n|---|---|---|---|---|---|\n"
            f"{template_rows}\n"
            f"**Tone Settings:**\n\n"
            f"| Tone | Formality | Warmth | Urgency | Use Case |\n|---|---|---|---|---|\n"
            f"{tone_rows}\n"
            f"**Personalization Fields:**\n{field_categories}\n\n"
            f"Source: [Email Template Engine]\nAgents: EmailDraftingAgent"
        )


if __name__ == "__main__":
    agent = EmailDraftingAgent()
    print("=" * 60)
    print("EMBEDDED DEMO CONTACT (works offline)")
    print(agent.perform(operation="draft_outreach"))
    print()
    print("=" * 60)
    print("LIVE TENANT CONTACT (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="draft_outreach", contact_name="Marcus Webb"))
    print()
    print("=" * 60)
    print(agent.perform(operation="template_library"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
