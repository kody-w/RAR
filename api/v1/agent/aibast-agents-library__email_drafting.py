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
