"""
Voice to CRM Email Drafting Agent — a template you are meant to mutate.

Generates meeting recaps, extracts action items, drafts follow-up
emails, and manages distribution lists from captured conversations.

The live tenant has no native "meeting transcript" entity, so in this
template a Dynamics CASE's email thread is read as the conversation: the
thread's messages become the recap topics, the correspondents become the
attendees, and the tasks regarding the case become the action items.
Say the same in your own mutation if you reinterpret an entity.

HOW THIS TEMPLATE WORKS
  1. Out of the box it pulls live cases, emails, and tasks over real
     HTTP from the globally hosted Static Dynamics 365 tenant (Aster
     Lane Office Systems — synthetic data, no credentials, works from
     anywhere):
     https://kody-w.github.io/static-dynamics-365/api/data/v9.2/
     Try: perform(operation="meeting_recap", meeting_id="CAS-260119")
     — recaps the tenant's real seeded email thread on "Freight
     tracking status clarification".
  2. No network? Everything falls back to the embedded demo layer below
     (_MEETING_TRANSCRIPTS / _ACTION_ITEMS) — the agent never crashes
     offline.
  3. Make it yours at the LIVE DATA SEAM below: set
     VOICE_TO_CRM_EMAIL_DATA_URL to any OData-shaped endpoint (your
     real Dynamics org, or Graph-exported JSON), or replace
     _fetch_collection() with your calendar/mail client. The fields the
     rest of the file needs are listed in _normalize_live_thread() —
     decisions and sentiment are labeled "n/a — enrichment seam"; wire
     your meeting-intelligence platform there.

OPERATIONS
  meeting_recap | action_items | follow_up_draft | distribution_list
  kwargs: operation (required), meeting_id (embedded 'MTG-001' or a
  live case number like 'CAS-260119')
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
    "name": "@aibast-agents-library/voice_to_crm_email",
    "version": "1.1.0",
    "display_name": "Voice to CRM Email",
    "description": "Drafts recaps, action items, and follow-ups from live case email threads in a simulated Dynamics 365 tenant, with offline fallback.",
    "author": "AIBAST",
    "tags": ["voice", "email", "meeting-recap", "action-items", "follow-up"],
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
#   export VOICE_TO_CRM_EMAIL_DATA_URL=https://your-org/api/data/v9.2
# or replace _fetch_collection() with your mail/calendar client.
# Downstream code only needs the fields produced by
# _normalize_live_thread().
# ═══════════════════════════════════════════════════════════════

DATA_SOURCE_URL = os.environ.get(
    "VOICE_TO_CRM_EMAIL_DATA_URL",
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


def _normalize_live_thread(case, case_emails, case_tasks):
    """Project a Dynamics case + its email thread + its tasks onto the
    meeting shape this agent uses. THIS is the contract your replacement
    data source must meet — a dict with these keys. None means 'not
    available from the thread alone' and renderers label it as an
    enrichment seam."""
    attendees, seen = [], set()
    for e in case_emails:
        for name, email in ((e.get("fromname"), e.get("fromaddress")),
                            (e.get("recipientidname"), None)):
            if name and name not in seen:
                seen.add(name)
                attendees.append({
                    "name": name,
                    "role": None,   # enrichment seam — wire your directory
                    "company": case.get("customeridname", ""),
                    "email": email or "n/a",
                })
    _PRIORITY = {0: "Low", 1: "Normal", 2: "High"}
    action_items = [
        {
            "id": t.get("activityid", "")[:8] or "task",
            "action": t.get("subject", "Untitled task"),
            "owner": t.get("owneridname", "unassigned"),
            "due_date": str(t.get("scheduledend", ""))[:10] or "n/a",
            "status": "Open" if t.get("statecode") == 0 else "Closed",
            "priority": _PRIORITY.get(t.get("prioritycode"), "Normal"),
        }
        for t in case_tasks
    ]
    return {
        "id": case.get("ticketnumber", ""),
        "title": case.get("title", "Untitled case"),
        "date": str(case.get("createdon", ""))[:10],
        "duration_min": None,   # enrichment seam — threads have no duration
        "attendees": attendees,
        "key_topics": sorted({e.get("subject", "") for e in case_emails if e.get("subject")}),
        "decisions": [],        # enrichment seam — wire your meeting-intelligence
        "sentiment": None,      # enrichment seam
        "action_items": action_items,
        "_live": True,
    }


def _live_thread(query):
    """Live thread for a case number or title fragment; None offline
    or when no emails regard that case."""
    q = (query or "").lower().strip()
    if not q:
        return None
    incidents = _fetch_collection("incidents")
    if not incidents:
        return None
    case = None
    for row in incidents:
        if q in str(row.get("ticketnumber", "")).lower() or q in str(row.get("title", "")).lower():
            case = row
            break
    if case is None:
        return None
    title = case.get("title", "")
    case_emails = [e for e in _fetch_collection("emails") if e.get("regardingobjectidname") == title]
    case_tasks = [t for t in _fetch_collection("tasks") if t.get("regardingobjectidname") == title]
    if not case_emails and not case_tasks:
        return None
    return _normalize_live_thread(case, case_emails, case_tasks)


# ═══════════════════════════════════════════════════════════════
# EMBEDDED DEMO LAYER (offline fallback)
# ═══════════════════════════════════════════════════════════════

_MEETING_TRANSCRIPTS = {
    "MTG-001": {
        "id": "MTG-001", "title": "TechVantage Solutions - Quarterly Business Review",
        "date": "2025-11-12", "duration_min": 55,
        "attendees": [
            {"name": "Jennifer Walsh", "role": "VP Operations", "company": "TechVantage Solutions", "email": "jennifer.walsh@techvantage.com"},
            {"name": "Sam Patel", "role": "IT Director", "company": "TechVantage Solutions", "email": "sam.patel@techvantage.com"},
            {"name": "Alex Rivera", "role": "Account Executive", "company": "Our Company", "email": "alex.rivera@ourcompany.com"},
            {"name": "Sarah Chen", "role": "Account Manager", "company": "Our Company", "email": "sarah.chen@ourcompany.com"},
        ],
        "key_topics": ["Q3 usage review", "APAC expansion plans", "Analytics upgrade discussion", "Contract renewal timeline"],
        "decisions": ["Proceed with Analytics Pro evaluation", "Schedule technical deep-dive with IT team", "Begin renewal discussions in January"],
        "sentiment": "Positive",
    },
}

_ACTION_ITEMS = {
    "MTG-001": [
        {"id": "AI-001", "action": "Send Analytics Pro product brief and pricing", "owner": "Alex Rivera", "due_date": "2025-11-15", "status": "Open", "priority": "High"},
        {"id": "AI-002", "action": "Schedule technical deep-dive session with IT team", "owner": "Sarah Chen", "due_date": "2025-11-19", "status": "Open", "priority": "High"},
        {"id": "AI-003", "action": "Provide APAC deployment case studies", "owner": "Alex Rivera", "due_date": "2025-11-22", "status": "Open", "priority": "Medium"},
        {"id": "AI-004", "action": "Share Q3 usage analytics dashboard", "owner": "Sarah Chen", "due_date": "2025-11-14", "status": "Open", "priority": "High"},
        {"id": "AI-005", "action": "Prepare renewal proposal framework", "owner": "Alex Rivera", "due_date": "2025-12-15", "status": "Open", "priority": "Medium"},
        {"id": "AI-006", "action": "Evaluate SSO integration requirements for APAC", "owner": "Sam Patel", "due_date": "2025-12-01", "status": "Open", "priority": "Medium"},
    ],
}

_EMAIL_TEMPLATES = {
    "meeting_recap": {
        "subject": "Meeting Recap: {meeting_title} - {date}",
        "body": "Hi {attendee_names},\n\nThank you for a productive meeting today. Here's a summary of our discussion:\n\n**Key Topics:**\n{topics}\n\n**Decisions Made:**\n{decisions}\n\n**Action Items:**\n{action_items}\n\nPlease review and let me know if I missed anything. Looking forward to our next steps.\n\nBest regards,\n{sender_name}",
    },
    "follow_up": {
        "subject": "Follow-up: {action_item} - {meeting_title}",
        "body": "Hi {recipient_name},\n\nFollowing up on our meeting on {date} regarding {meeting_title}.\n\nAs discussed, I wanted to share the following:\n\n{content}\n\nPlease let me know if you have any questions or need additional information.\n\nBest,\n{sender_name}",
    },
}

_DISTRIBUTION_LISTS = {
    "MTG-001": {
        "all_attendees": ["jennifer.walsh@techvantage.com", "sam.patel@techvantage.com", "alex.rivera@ourcompany.com", "sarah.chen@ourcompany.com"],
        "external_only": ["jennifer.walsh@techvantage.com", "sam.patel@techvantage.com"],
        "internal_only": ["alex.rivera@ourcompany.com", "sarah.chen@ourcompany.com"],
        "action_item_owners": ["alex.rivera@ourcompany.com", "sarah.chen@ourcompany.com", "sam.patel@techvantage.com"],
    },
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _resolve_meeting(query):
    """Embedded demo meetings first, then live case threads.
    Returns (meeting_dict, action_items, is_live)."""
    q = (query or "").upper().strip()
    if not q or "MTG-" in q:
        key = "MTG-001"
        for k in _MEETING_TRANSCRIPTS:
            if k in q:
                key = k
        return _MEETING_TRANSCRIPTS[key], _ACTION_ITEMS.get(key, []), False
    thread = _live_thread(query)
    if thread:
        return thread, thread["action_items"], True
    return _MEETING_TRANSCRIPTS["MTG-001"], _ACTION_ITEMS.get("MTG-001", []), False


def _format_action_items(items):
    lines = []
    for item in items:
        lines.append(f"- [{item['priority']}] {item['action']} (Owner: {item['owner']}, Due: {item['due_date']})")
    return "\n".join(lines) or "- None on record"


def _render_recap_email(mtg, items):
    topics = "\n".join(f"- {t}" for t in mtg["key_topics"]) or "- n/a"
    decisions = "\n".join(f"- {d}" for d in mtg["decisions"]) or "- n/a — enrichment seam (wire your meeting-intelligence platform)"
    action_items = _format_action_items(items)
    attendee_names = ", ".join(a["name"] for a in mtg["attendees"]) or "team"
    template = _EMAIL_TEMPLATES["meeting_recap"]
    subject = template["subject"].replace("{meeting_title}", mtg["title"]).replace("{date}", mtg["date"])
    body = template["body"].replace("{attendee_names}", attendee_names).replace("{topics}", topics).replace("{decisions}", decisions).replace("{action_items}", action_items).replace("{sender_name}", "Alex Rivera")
    return subject, body


def _source_line(is_live):
    if is_live:
        return "Thread source: LIVE case email thread from the Aster Lane Dynamics 365 tenant"
    return "Thread source: embedded demo layer (simulated)"


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class VoiceToCRMEmailAgent(BasicAgent):
    """
    Voice-to-CRM email agent for meeting follow-ups.

    Operations:
        meeting_recap      - generate meeting recap from voice transcript
        action_items       - extract and organize action items
        follow_up_draft    - draft follow-up emails for action items
        distribution_list  - manage email distribution lists
    """

    def __init__(self):
        self.name = "VoiceToCRMEmailAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "meeting_recap", "action_items",
                            "follow_up_draft", "distribution_list",
                        ],
                        "description": "The email operation to perform",
                    },
                    "meeting_id": {
                        "type": "string",
                        "description": "Meeting ID (e.g. 'MTG-001')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "meeting_recap")
        mtg, items, is_live = _resolve_meeting(kwargs.get("meeting_id", ""))
        dispatch = {
            "meeting_recap": self._meeting_recap,
            "action_items": self._action_items,
            "follow_up_draft": self._follow_up_draft,
            "distribution_list": self._distribution_list,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        return handler(mtg, items, is_live)

    def _meeting_recap(self, mtg, items, is_live):
        subject, body = _render_recap_email(mtg, items)
        attendee_rows = ""
        for a in mtg["attendees"]:
            role = a["role"] or "n/a — enrichment seam"
            attendee_rows += f"| {a['name']} | {role} | {a['company']} | {a['email']} |\n"
        duration = f"{mtg['duration_min']} minutes" if mtg["duration_min"] else "n/a — enrichment seam"
        sentiment = mtg["sentiment"] or "n/a — enrichment seam"
        return (
            f"**Meeting Recap: {mtg['title']}**\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Date | {mtg['date']} |\n"
            f"| Duration | {duration} |\n"
            f"| Sentiment | {sentiment} |\n\n"
            f"**Attendees:**\n\n"
            f"| Name | Role | Company | Email |\n|---|---|---|---|\n"
            f"{attendee_rows}\n"
            f"**Draft Email:**\n\n"
            f"**Subject:** {subject}\n\n"
            f"---\n{body}\n---\n\n"
            f"{_source_line(is_live)}\n"
            f"Source: [Conversation Thread + AI Summary]\nAgents: VoiceToCRMEmailAgent"
        )

    def _action_items(self, mtg, items, is_live):
        rows = ""
        for item in items:
            rows += f"| {item['id']} | {item['action'][:40]} | {item['owner']} | {item['due_date']} | {item['priority']} | {item['status']} |\n"
        if not rows:
            rows = "| - | No tasks on record for this thread | - | - | - | - |\n"
        by_owner = {}
        for item in items:
            by_owner.setdefault(item["owner"], []).append(item)
        owner_summary = "\n".join(f"- {owner}: {len(owner_items)} items" for owner, owner_items in by_owner.items()) or "- None"
        return (
            f"**Action Items: {mtg['id']}**\n\n"
            f"| ID | Action | Owner | Due Date | Priority | Status |\n|---|---|---|---|---|---|\n"
            f"{rows}\n"
            f"**By Owner:**\n{owner_summary}\n\n"
            f"**Total Items:** {len(items)} | **High Priority:** {sum(1 for i in items if i['priority'] == 'High')}\n\n"
            f"{_source_line(is_live)}\n"
            f"Source: [Thread Tasks + NLP Extraction]\nAgents: VoiceToCRMEmailAgent"
        )

    def _follow_up_draft(self, mtg, items, is_live):
        high_priority = [i for i in items if i["priority"] == "High"] or items
        drafts = ""
        for item in high_priority[:2]:
            drafts += (
                f"**To:** {item['owner']}\n"
                f"**Subject:** Follow-up: {item['action'][:50]} - {mtg['title']}\n"
                f"**Due:** {item['due_date']}\n\n"
                f"Hi {item['owner'].split()[0]},\n\n"
                f"Following up on the {mtg['date']} conversation. As discussed, the next step is:\n\n"
                f"- {item['action']}\n\n"
                f"Please let me know if you need any additional information.\n\n"
                f"Best, Alex\n\n---\n\n"
            )
        if not drafts:
            drafts = "No open action items to follow up on for this thread.\n\n"
        return (
            f"**Follow-Up Drafts: {mtg['title']}**\n\n"
            f"Generated {min(2, len(high_priority))} follow-up email draft(s).\n\n"
            f"{drafts}"
            f"{_source_line(is_live)}\n"
            f"Source: [Email Template Engine]\nAgents: VoiceToCRMEmailAgent"
        )

    def _distribution_list(self, mtg, items, is_live):
        if is_live:
            addresses = sorted({a["email"] for a in mtg["attendees"] if a["email"] and a["email"] != "n/a"})
            owners = sorted({i["owner"] for i in items})
            return (
                f"**Distribution Lists: {mtg['id']}** (built from the LIVE case thread)\n\n"
                f"| List | Recipients | Members |\n|---|---|---|\n"
                f"| Thread Correspondents | {len(addresses)} | {', '.join(addresses) or 'n/a'} |\n"
                f"| Action Item Owners | {len(owners)} | {', '.join(owners) or 'n/a'} |\n\n"
                f"Owner email addresses are an enrichment seam — wire your "
                f"directory to resolve system users to mailboxes.\n\n"
                f"{_source_line(is_live)}\n"
                f"Source: [Thread Metadata + Contact Directory]\nAgents: VoiceToCRMEmailAgent"
            )
        lists = _DISTRIBUTION_LISTS.get(mtg["id"], {})
        list_rows = ""
        for list_name, emails in lists.items():
            list_rows += f"| {list_name.replace('_', ' ').title()} | {len(emails)} | {', '.join(emails[:2])}{'...' if len(emails) > 2 else ''} |\n"
        return (
            f"**Distribution Lists: {mtg['id']}** (embedded demo data — simulated)\n\n"
            f"| List | Recipients | Members |\n|---|---|---|\n"
            f"{list_rows}\n"
            f"**Recommended for Recap:** All Attendees ({len(lists.get('all_attendees', []))} recipients)\n"
            f"**Recommended for Action Items:** Action Item Owners ({len(lists.get('action_item_owners', []))} recipients)\n\n"
            f"Source: [Meeting Metadata + Contact Directory]\nAgents: VoiceToCRMEmailAgent"
        )


if __name__ == "__main__":
    agent = VoiceToCRMEmailAgent()
    print("=" * 60)
    print("EMBEDDED DEMO MEETING (works offline)")
    print(agent.perform(operation="meeting_recap", meeting_id="MTG-001"))
    print()
    print("=" * 60)
    print("LIVE TENANT CASE THREAD (fetched over HTTP; falls back offline)")
    print(agent.perform(operation="meeting_recap", meeting_id="CAS-260119"))
    print()
    print("=" * 60)
    print(agent.perform(operation="action_items", meeting_id="CAS-260131"))
