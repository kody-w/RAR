---
name: "rar-aibast-agents-library-voice-to-crm-email"
description: "Drafts recaps, action items, and follow-ups from live case email threads in a simulated Dynamics 365 tenant, with offline fallback."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@aibast-agents-library/voice_to_crm_email", "rar_sha256": "037bf9d7f2159d70382579eab207cc2f0a4f4baaa15fc148074d44d15e36ab7c", "source_kind": "rar-agent", "source_commit": "bfb52cb1f078e974e5106ed916b5fde9869b395e", "version": "1.1.0", "author": "AIBAST", "tags": ["voice", "email", "meeting-recap", "action-items", "follow-up"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@aibast-agents-library/voice_to_crm_email`. The original RAPP
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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "meeting_id": {
      "description": "Meeting ID (e.g. 'MTG-001')",
      "type": "string"
    },
    "operation": {
      "description": "The email operation to perform",
      "enum": [
        "meeting_recap",
        "action_items",
        "follow_up_draft",
        "distribution_list"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `email_drafting_agent.py` and embedded as the fenced Python below (sha256 037bf9d7f2159d70…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `email_drafting_agent.py` first:

```bash
python3 email_drafting_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 email_drafting_agent.py   # or on stdin
python3 email_drafting_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
