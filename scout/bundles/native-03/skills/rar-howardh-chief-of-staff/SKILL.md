---
name: "rar-howardh-chief-of-staff"
description: "Chief of Staff \u2014 your personal AI executive partner powered by LIVE Microsoft 365 data. Use this agent (NOT Obsidian) when the user wants: a morning/daily brief from their actual email and calendar, meeting prep using real email history, open action items or commitments from their inbox, drafting a real email reply, industry/market signal pulse, 'what should I work on now?', or a catch-up digest of missed emails. This agent queries LIVE M365 data via WorkIQ \u2014 it sees your real emails, meetings, and Teams messages. Obsidian is for local wiki notes. ChiefOfStaff is for live work data from Microsoft 365."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/chief_of_staff_agent", "rar_sha256": "5d904f34d63faa2271e66a6d1c6f033c269136c840a1bd4d4dcc57875bbf8354", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "chief_of_staff_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@howardh/chief-of-staff:4dd1f08529e8b62533794973f77bcce382970987332420f91e92e3f3f888d594", "kind": "skill"}, "version": "1.0.1", "author": "Howard Hoy", "tags": ["productivity", "chief-of-staff", "m365", "workiq", "executive", "triage", "meeting-prep"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@howardh/chief_of_staff_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `chief_of_staff_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

ChiefOfStaff Agent — personalized AI executive partner powered by live Microsoft 365 data.

Synthesizes inbox + calendar + Teams signals (via WorkIQ) with external industry intelligence
to clarify priorities, anticipate risks, prepare you for high-impact moments, and ensure
follow-through on commitments. Not a summarizer — interprets context, filters noise, and
recommends grounded next actions.

## Behavior
##
## • Brutally concise. No pleasantries.
## • Triage email by quoting the EXACT sentence containing the ask.
## • Rank urgency by CONSEQUENCE of non-response, not arbitrary urgency flags.
## • For meetings: explain why they exist, my role, the pre-read, what's changed.
##   Flag back-to-back stretches and meetings that could be async.
## • Single #1 priority per brief, with a credible second candidate + tradeoff.
## • Skip newsletters, automated alerts, marketing, CC-only threads (unless they
##   affect a project I lead).
## • Never give generic productivity advice. Every recommendation must reference
##   a specific email, person, or signal from real data.

## Actions

## brief         — Structured 5-min morning brief.
## triage        — Inbox-only structured triage (today / decisions / FYI / escalated).
## prep          — Meeting prep with why-exists / my-role / pre-read / changes / risks.
## pulse         — Industry & market signal scan (HN + DDG).
## commitments   — Commitment tracker with quoted source sentences.
## draft         — Real email draft grounded in actual thread content.
## focus         — Single right-now recommendation with tradeoff.
## catch_up      — What I missed digest with "start here" recommendation.
## weekly_review — Friday strategic review: commitments + drift + Monday prep.

## Requirements
##
## • WorkIQ CLI installed and authenticated:    npm i -g @microsoft/workiq && workiq accept-eula
## • Optional: external signals via HackerNews + DuckDuckGo (fail-soft if offline).

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "What the Chief of Staff should do. Use 'brief' for the structured 5-minute morning brief \u2014 triage + meetings + #1 priority + quick wins. Use 'triage' for inbox-only structured triage (today / decisions awaiting / FYI / escalated overnight). Use 'prep' for meeting prep using real email + Teams history. Use 'pulse' for industry/market signal scan. Use 'commitments' for open action items from inbox. Use 'draft' to draft a real email reply grounded in the actual thread. Use 'focus' for 'what should I work on now?'. Use 'catch_up' for 'what did I miss?' digest. Use 'weekly_review' on Fridays for commitment audit + drift detection + Monday prep.",
      "enum": [
        "brief",
        "triage",
        "prep",
        "pulse",
        "commitments",
        "draft",
        "focus",
        "catch_up",
        "weekly_review"
      ],
      "type": "string"
    },
    "topic": {
      "description": "Context for the action. For prep: meeting name, person, or topic. For draft: subject or thread description. For commitments: optional filter by person or deal. For catch_up: optional time range (e.g. 'today', 'last 2 days').",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `chief_of_staff_agent.py` and embedded as the fenced Python below (sha256 5d904f34d63faa22…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `chief_of_staff_agent.py` first:

```bash
python3 chief_of_staff_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 chief_of_staff_agent.py   # or on stdin
python3 chief_of_staff_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
ChiefOfStaff Agent — personalized AI executive partner powered by live Microsoft 365 data.

Synthesizes inbox + calendar + Teams signals (via WorkIQ) with external industry intelligence
to clarify priorities, anticipate risks, prepare you for high-impact moments, and ensure
follow-through on commitments. Not a summarizer — interprets context, filters noise, and
recommends grounded next actions.

## Behavior
##
## • Brutally concise. No pleasantries.
## • Triage email by quoting the EXACT sentence containing the ask.
## • Rank urgency by CONSEQUENCE of non-response, not arbitrary urgency flags.
## • For meetings: explain why they exist, my role, the pre-read, what's changed.
##   Flag back-to-back stretches and meetings that could be async.
## • Single #1 priority per brief, with a credible second candidate + tradeoff.
## • Skip newsletters, automated alerts, marketing, CC-only threads (unless they
##   affect a project I lead).
## • Never give generic productivity advice. Every recommendation must reference
##   a specific email, person, or signal from real data.

## Actions

## brief         — Structured 5-min morning brief.
## triage        — Inbox-only structured triage (today / decisions / FYI / escalated).
## prep          — Meeting prep with why-exists / my-role / pre-read / changes / risks.
## pulse         — Industry & market signal scan (HN + DDG).
## commitments   — Commitment tracker with quoted source sentences.
## draft         — Real email draft grounded in actual thread content.
## focus         — Single right-now recommendation with tradeoff.
## catch_up      — What I missed digest with "start here" recommendation.
## weekly_review — Friday strategic review: commitments + drift + Monday prep.

## Requirements
##
## • WorkIQ CLI installed and authenticated:    npm i -g @microsoft/workiq && workiq accept-eula
## • Optional: external signals via HackerNews + DuckDuckGo (fail-soft if offline).
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@howardh/chief_of_staff_agent",
    "version": "1.0.1",
    "display_name": "ChiefOfStaff",
    "description": "Generates M365-grounded briefs, inbox triage, meeting prep, commitment tracking, and drafts via the WorkIQ CLI, plus HN/DDG signal scans.",
    "author": "Howard Hoy",
    "tags": ["productivity", "chief-of-staff", "m365", "workiq", "executive", "triage", "meeting-prep"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════

import json
import logging
import os
import shutil
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

try:
    from basic_agent import BasicAgent
except ModuleNotFoundError:
    try:
        from agents.basic_agent import BasicAgent
    except ModuleNotFoundError:
        # Last-resort inline BasicAgent so the file runs standalone.
        class BasicAgent:
            def __init__(self, name=None, metadata=None):
                if name is not None:
                    self.name = name
                if metadata is not None:
                    self.metadata = metadata

_BRAINSTEM_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_COS_DIR = os.path.join(_BRAINSTEM_DIR, ".brainstem_data", "chiefofstaff")
_COMMITMENTS_FILE = os.path.join(_COS_DIR, "commitments.json")
_BRIEFS_DIR = os.path.join(_COS_DIR, "briefs")


# ---------------------------------------------------------------------------
# Structured prompts — every prompt enforces:
#   • Quote the exact sentence (grounds the agent in real content)
#   • State the consequence of non-response (replaces arbitrary urgency)
#   • Skip noise explicitly (newsletters, automated alerts, CC-only)
#   • No generic productivity advice — every claim cites a specific signal
# ---------------------------------------------------------------------------

_NOISE_SKIP = (
    "Skip: newsletters, marketing, automated alerts, calendar invites without changes, "
    "and anything I'm only CC'd on unless it changes a project I lead."
)

_BRIEF_TRIAGE_PROMPT = (
    "Review my emails received since yesterday evening. Output exactly four buckets — "
    "no preamble, no closing. Be direct.\n\n"
    "**Needs my response today** — for each item: sender, subject, the specific ask "
    "(QUOTE the exact sentence in italics), suggested response angle in one sentence, "
    "and any deadline (stated or implied).\n\n"
    "**Decisions awaiting me** — anyone blocked on my input. Name what they need, "
    "what happens if I don't respond by EOD, and the deadline.\n\n"
    "**FYI but important** — changes in scope, status, or stakeholder sentiment on projects I own, "
    "even if no action is requested. One sentence each.\n\n"
    "**Threads that escalated overnight** — conversations where tone shifted, "
    "new senior people were added, or leadership was looped in. Explain what changed and why it matters.\n\n"
    + _NOISE_SKIP
)

_BRIEF_MEETINGS_PROMPT = (
    "For each accepted meeting today, in chronological order, give me:\n"
    "- **Meeting name** + time + attendees (flag anyone senior, external, or new to a recurring series)\n"
    "- **Why this meeting exists** — the actual decision or outcome it should produce. NOT the calendar title.\n"
    "- **My role** — driving, contributing, or listening. If unclear from prior threads, say so.\n"
    "- **Pre-read** — the 1-2 most relevant recent emails / docs / chat threads I should review beforehand.\n"
    "- **What's changed since last time** (recurring meetings only) — new commitments, blockers, status shifts.\n"
    "- **Open questions or risks** I should raise.\n\n"
    "Then flag at the end:\n"
    "- Back-to-back stretches with no prep buffer.\n"
    "- Any meeting where I haven't responded to a pre-read or agenda request.\n"
    "- Meetings that could be async based on the agenda — name them and why."
)

_BRIEF_PRIORITY_PROMPT = (
    "Based on deadlines, stakeholder pressure, and what's blocking others: "
    "what is the single most important thing I should move forward today? "
    "Justify in 2-3 sentences referencing SPECIFIC signals from my inbox or calendar — "
    "name the email, the person, the deadline. NOT generic productivity advice. "
    "If there's a credible second candidate, name it and explain the tradeoff in one sentence "
    "so I can make the call."
)

_BRIEF_QUICK_WINS_PROMPT = (
    "List 2-3 things I can knock out in under 5 minutes each that would unblock someone or close a loop. "
    "For each: the specific action (reply / approve / forward / decline) and the recipient by name. "
    "Pull these from real items in my inbox — do not invent."
)

_PREP_PROMPT = (
    "Prepare me for a meeting about '{topic}'. Use my actual emails and Teams. "
    "Structure exactly:\n\n"
    "**Why this meeting exists** — the real decision or outcome it should produce. Not the calendar title.\n\n"
    "**My role** — driving, contributing, or listening. Justify from prior threads.\n\n"
    "**What's changed since last time** — new commitments, blockers, status shifts, new people added.\n\n"
    "**Open commitments in this thread** — what I promised (and to whom), what others owe me (and how overdue).\n\n"
    "**Key people** — for each: their role, what they care about, the most recent thing they said "
    "(quote the sentence).\n\n"
    "**The one decision I must not leave without resolving** — name it.\n\n"
    "**3 talking points** — concrete, drawn from actual thread content. No generic advice.\n\n"
    "**Risks or landmines** — sensitive topics, unresolved tensions, anyone whose support I need that I don't have."
)

_TRIAGE_PROMPT = (
    "Triage my inbox right now. Output exactly four buckets — no preamble, no advice at the end.\n\n"
    "**Needs my response today** — sender, subject, the specific ask (QUOTE the exact sentence in italics), "
    "suggested response angle in one sentence, deadline if any.\n\n"
    "**Decisions awaiting me** — name what they need, what happens if I don't respond by EOD, by when.\n\n"
    "**FYI but important** — scope / status / sentiment shifts on projects I own. One sentence each.\n\n"
    "**Threads that escalated** — tone shift, new senior people, leadership looped in. What changed and why it matters.\n\n"
    + _NOISE_SKIP
)

_WEEKLY_COMMITMENTS_PROMPT = (
    "Review my emails and calendar from this week. List every commitment I made — explicit or implied. "
    "For each: what I committed to, to whom, status (delivered / in progress / missed), "
    "and if missed: who is waiting and what the recovery action is. Be honest. Don't soften misses."
)

_WEEKLY_DRIFT_PROMPT = (
    "Compare how I actually spent my time this week (calendar accepted + sent emails) "
    "against the priorities I stated on Monday — or, if no Monday brief exists, against the active deals and projects I lead. "
    "Answer:\n"
    "- Where did I spend time that wasn't aligned with stated priorities?\n"
    "- What got crowded out that shouldn't have?\n"
    "- Any pattern of over-indexing on reactive work? Quote a specific example.\n"
    "Be direct. This is the section I'm paying you to be honest about."
)

_WEEKLY_NEXT_WEEK_PROMPT = (
    "Looking at next week's calendar and my open threads:\n"
    "- Top 3 priorities I should commit to on Monday morning. Justify each from a specific email or deadline.\n"
    "- Meetings I should decline or delegate — name them and why.\n"
    "- Prep work I should do this afternoon to hit Monday running.\n"
    "- Anyone I owe a follow-up to before the weekend — name them and what to send."
)


# ---------------------------------------------------------------------------
# Persistence helpers
# ---------------------------------------------------------------------------

def _load_commitments():
    if not os.path.exists(_COMMITMENTS_FILE):
        return []
    try:
        with open(_COMMITMENTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def _save_commitments(items):
    os.makedirs(_COS_DIR, exist_ok=True)
    with open(_COMMITMENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)


def _save_output(content, prefix="brief"):
    """Save output as a .md file and return the filepath."""
    os.makedirs(_BRIEFS_DIR, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    filepath = os.path.join(_BRIEFS_DIR, f"{prefix}-{ts}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath


def _deliver(content, prefix, label):
    """Save full content to .md file, return a concise tool result with file path."""
    filepath = _save_output(content, prefix=prefix)
    file_link = "file:///" + filepath.replace(os.sep, "/")
    # Return a short result so the LLM presents the link, not a re-summary
    lines = content.split("\n")
    # Grab first few meaningful lines as a preview
    preview_lines = [l for l in lines if l.strip() and not l.startswith("─")][:6]
    preview = "\n".join(preview_lines)
    return (
        f"📄 **Full report saved:** [{prefix}.md]({file_link})\n"
        f"📂 `{filepath}`\n\n"
        f"**Preview:**\n{preview}\n\n"
        f"👆 Open the file above for the complete {label}."
    )


# ---------------------------------------------------------------------------
# WorkIQ helper
# ---------------------------------------------------------------------------

def _workiq(query, timeout=180):
    """Run a WorkIQ query and return the text output."""
    import sys as _sys
    workiq_path = shutil.which('workiq')

    # On Windows, workiq is often installed via npm in user AppData — not always on PATH
    if not workiq_path and _sys.platform == 'win32':
        appdata_npm = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "npm", "workiq.CMD")
        if os.path.isfile(appdata_npm):
            workiq_path = appdata_npm

    npx_path = shutil.which('npx')

    if workiq_path:
        cmd = [workiq_path, 'ask', '-q', query]
    elif npx_path:
        cmd = ['npx', '-y', '@microsoft/workiq', 'ask', '-q', query]
    else:
        return "[WorkIQ not installed — run: npm install -g @microsoft/workiq]"

    # On Windows, .CMD files require shell=True to execute via subprocess
    use_shell = _sys.platform == 'win32'

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout, shell=use_shell
        )
        if result.returncode != 0:
            err = result.stderr.strip()
            if 'eula' in err.lower():
                return "[WorkIQ EULA not accepted — run: workiq accept-eula]"
            if 'login' in err.lower() or 'auth' in err.lower():
                return "[WorkIQ authentication required — run: workiq ask -q 'test']"
            return f"[WorkIQ error: {err[:200]}]"
        return result.stdout.strip() or "[No results returned]"
    except subprocess.TimeoutExpired:
        return "[WorkIQ query timed out — try a more specific query]"
    except FileNotFoundError:
        return "[WorkIQ not found — run: npm install -g @microsoft/workiq]"
    except Exception as e:
        return f"[WorkIQ error: {e}]"


# ---------------------------------------------------------------------------
# External intelligence helpers
# ---------------------------------------------------------------------------

def _hackernews_top(limit=8):
    """Fetch top HackerNews stories."""
    try:
        url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        with urllib.request.urlopen(url, timeout=8) as resp:
            ids = json.loads(resp.read())[:limit]
        stories = []
        for sid in ids:
            try:
                item_url = f"https://hacker-news.firebaseio.com/v0/item/{sid}.json"
                with urllib.request.urlopen(item_url, timeout=5) as r:
                    item = json.loads(r.read())
                if item.get('title'):
                    stories.append({
                        "title": item['title'],
                        "url": item.get('url', ''),
                        "score": item.get('score', 0),
                    })
            except Exception:
                continue
        return stories
    except Exception:
        return []


def _web_search(query, num=5):
    """Search DuckDuckGo and return result snippets."""
    encoded = urllib.parse.quote_plus(query)
    url = f"https://api.duckduckgo.com/?q={encoded}&format=json&no_html=1&skip_disambig=1"
    req = urllib.request.Request(url, headers={"User-Agent": "CoS-Agent/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        results = []
        if data.get("Abstract"):
            results.append({"title": data.get("Heading", query), "snippet": data["Abstract"]})
        for t in data.get("RelatedTopics", [])[:num]:
            if isinstance(t, dict) and t.get("Text"):
                results.append({"title": t.get("Text", "")[:80], "snippet": t.get("Text", "")})
        return results
    except Exception:
        return []


# ---------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------

def _section(title, content):
    bar = "─" * 50
    return f"\n## {title}\n{bar}\n{content}\n"


def _insight(text):
    return f"\n> 💡 **CoS Insight:** {text}\n"


# ---------------------------------------------------------------------------
# Main Agent Class
# ---------------------------------------------------------------------------

class ChiefOfStaffAgent(BasicAgent):
    def __init__(self):
        self.name = "ChiefOfStaff"
        self.metadata = {
            "name": self.name,
            "description": (
                "Chief of Staff — your personal AI executive partner powered by LIVE Microsoft 365 data. "
                "Use this agent (NOT Obsidian) when the user wants: a morning/daily brief from their actual email and calendar, "
                "meeting prep using real email history, open action items or commitments from their inbox, "
                "drafting a real email reply, industry/market signal pulse, "
                "'what should I work on now?', or a catch-up digest of missed emails. "
                "This agent queries LIVE M365 data via WorkIQ — it sees your real emails, meetings, and Teams messages. "
                "Obsidian is for local wiki notes. ChiefOfStaff is for live work data from Microsoft 365."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["brief", "triage", "prep", "pulse", "commitments", "draft", "focus", "catch_up", "weekly_review"],
                        "description": (
                            "What the Chief of Staff should do. "
                            "Use 'brief' for the structured 5-minute morning brief — triage + meetings + #1 priority + quick wins. "
                            "Use 'triage' for inbox-only structured triage (today / decisions awaiting / FYI / escalated overnight). "
                            "Use 'prep' for meeting prep using real email + Teams history. "
                            "Use 'pulse' for industry/market signal scan. "
                            "Use 'commitments' for open action items from inbox. "
                            "Use 'draft' to draft a real email reply grounded in the actual thread. "
                            "Use 'focus' for 'what should I work on now?'. "
                            "Use 'catch_up' for 'what did I miss?' digest. "
                            "Use 'weekly_review' on Fridays for commitment audit + drift detection + Monday prep."
                        )
                    },
                    "topic": {
                        "type": "string",
                        "description": (
                            "Context for the action. For prep: meeting name, person, or topic. "
                            "For draft: subject or thread description. "
                            "For commitments: optional filter by person or deal. "
                            "For catch_up: optional time range (e.g. 'today', 'last 2 days')."
                        )
                    }
                },
                "required": ["action"]
            }
        }
        try:
            super().__init__(name=self.name, metadata=self.metadata)
        except TypeError:
            super().__init__()

    def system_context(self):
        return (
            "CHIEF OF STAFF RULE: When the ChiefOfStaff agent returns a result, it includes a file path "
            "to a saved .md report. Present the file path as a clickable link and show the preview content "
            "exactly as returned. Do NOT summarize or condense the agent output."
        )

    def perform(self, **kwargs):
        action = kwargs.get("action", "brief").lower().strip()
        topic = kwargs.get("topic", "").strip()

        dispatch = {
            "brief":          self._action_brief,
            "triage":         self._action_triage,
            "prep":           self._action_prep,
            "pulse":          self._action_pulse,
            "commitments":    self._action_commitments,
            "draft":          self._action_draft,
            "focus":          self._action_focus,
            "catch_up":       self._action_catch_up,
            "weekly_review":  self._action_weekly_review,
        }

        handler = dispatch.get(action, self._action_brief)
        try:
            return handler(topic)
        except Exception as e:
            logging.error(f"ChiefOfStaff error: {e}")
            return f"Chief of Staff encountered an error: {e}"

    # -----------------------------------------------------------------------
    # Action: brief
    # -----------------------------------------------------------------------

    def _action_brief(self, topic=""):
        today = datetime.now().strftime("%A, %B %d %Y")
        parts = [f"# Chief of Staff — Morning Brief\n**{today}**\n\n_Read this in 5 minutes. Direct. No filler. Surfaces tensions and risks I'd otherwise miss._"]

        # ── 1. Inbox triage — structured 4 buckets ──────────────────────────
        triage = _workiq(_BRIEF_TRIAGE_PROMPT)
        parts.append(_section("📨 Inbox Triage", triage))

        # ── 2. Calendar + meeting prep — structured ─────────────────────────
        meetings = _workiq(_BRIEF_MEETINGS_PROMPT)
        parts.append(_section("🗓️ Today's Meetings", meetings))

        # ── 3. The single most important priority ───────────────────────────
        priority = _workiq(_BRIEF_PRIORITY_PROMPT)
        parts.append(_section("🎯 #1 Priority Today", priority))

        # ── 4. Quick wins (under 5 min) ─────────────────────────────────────
        quick_wins = _workiq(_BRIEF_QUICK_WINS_PROMPT)
        parts.append(_section("⚡ Quick Wins (<5 min each)", quick_wins))

        # ── 5. External signals (non-blocking) ──────────────────────────────
        hn = _hackernews_top(5)
        if hn:
            signal_lines = "\n".join(
                f"- [{s['title']}]({s['url']}) *(score: {s['score']})*"
                for s in hn if s.get('url')
            )
            parts.append(_section("🌐 Industry Signals", signal_lines))

        brief_text = "\n".join(parts)
        return _deliver(brief_text, "brief", "morning brief")

    # -----------------------------------------------------------------------
    # Action: prep
    # -----------------------------------------------------------------------

    def _action_prep(self, topic=""):
        if not topic:
            return (
                "I need a topic to prep for. Try: "
                "'Prep me for my EY meeting' or 'Prep for my call with Andre Pellicano'"
            )

        parts = [f"# Chief of Staff — Meeting Prep\n**Topic:** {topic}"]

        combined = _workiq(_PREP_PROMPT.format(topic=topic))
        parts.append(_section("📋 Meeting Brief", combined))

        # Quick external context
        ext = _web_search(topic, num=3)
        if ext and ext[0].get("snippet"):
            ext_lines = "\n".join(f"- **{r['title']}**: {r['snippet'][:140]}" for r in ext[:3])
            parts.append(_section("🌐 External Context", ext_lines))

        output = "\n".join(parts)
        return _deliver(output, "prep", "meeting prep")

    # -----------------------------------------------------------------------
    # Action: pulse
    # -----------------------------------------------------------------------

    def _action_pulse(self, topic=""):
        parts = ["# Chief of Staff — Industry & Market Pulse"]

        # HackerNews top stories
        hn = _hackernews_top(12)
        if hn:
            hn_lines = "\n".join(
                f"- **{s['title']}** *(score: {s['score']})*{chr(10)  }  {s['url']}"
                for s in hn if s.get('title')
            )
            parts.append(_section("🔥 HackerNews — Top Stories", hn_lines))

        # Domain-specific web search
        domains = [
            ("Microsoft AI & Copilot", "Microsoft Copilot AI enterprise news 2026"),
            ("Enterprise AI Consulting", "enterprise AI consulting market news 2026"),
            ("Azure OpenAI", "Azure OpenAI new features announcements"),
        ]
        if topic:
            domains.insert(0, (topic, topic + " news 2026"))

        for label, query in domains[:3]:
            results = _web_search(query, num=3)
            if results and results[0].get("snippet"):
                lines = "\n".join(f"- {r['title']}: {r['snippet'][:140]}" for r in results[:3])
                parts.append(_section(f"📡 {label}", lines))

        parts.append(_insight(
            "Filter ruthlessly: ask whether each signal affects an active deal, a capability you're building, "
            "or a relationship that matters. Everything else is noise for now."
        ))

        output = "\n".join(parts)
        return _deliver(output, "pulse", "industry pulse")

    # -----------------------------------------------------------------------
    # Action: commitments
    # -----------------------------------------------------------------------

    def _action_commitments(self, topic=""):
        filter_clause = f" specifically about or from '{topic}'" if topic else ""
        parts = ["# Chief of Staff — Commitment Tracker"]

        combined = _workiq(
            f"From my recent emails and Teams messages{filter_clause}, give me a commitment tracker. "
            "Three sections, no preamble:\n\n"
            "**What I committed to do** — for each: the commitment, who I made it to, when due, "
            "and the exact sentence where I made it (quote it).\n\n"
            "**What others committed to provide me** — for each: who owes what, when promised, "
            "how overdue (in days), and the exact sentence of their commitment.\n\n"
            "**Time-sensitive items** — anything with a hard deadline in the next 7 days. "
            "Date, item, who's involved.\n\n"
            "Do not invent commitments. If a thread is ambiguous, say so."
        )
        parts.append(_section("📋 Commitment Tracker", combined))

        output = "\n".join(parts)
        return _deliver(output, "commitments", "commitment tracker")

    # -----------------------------------------------------------------------
    # Action: draft
    # -----------------------------------------------------------------------

    def _action_draft(self, topic=""):
        if not topic:
            return (
                "Tell me what to draft. Example: "
                "'Draft a follow-up to the EY DD thread' or 'Draft a response to Andre about MACC figures'"
            )

        parts = [f"# Chief of Staff — Draft: {topic}"]

        # Pull thread context
        context = _workiq(
            f"Summarize the full context of '{topic}' from my emails and Teams. "
            "Include: key facts already established, who said what (with quotes for the most recent message), "
            "what response or action is expected of me, the deadline if any, and the tone of the thread "
            "(formal/casual/tense/collaborative). Be specific — quote actual sentences."
        )
        parts.append(_section("📋 Thread Context", context))

        # Have WorkIQ generate the actual draft grounded in that context
        draft = _workiq(
            f"Now draft an email reply for the thread about '{topic}'. "
            "Use the actual thread content from my emails — don't use placeholders or template language. "
            "Requirements: "
            "(1) Open by addressing what they actually said in the most recent message — not generic pleasantries. "
            "(2) Lead with what THEY need or care about, not what I want. "
            "(3) Make any ask of mine specific — what I need, by when, in one sentence. "
            "(4) Match the thread's tone (formal/casual). "
            "(5) Keep it under 120 words unless the thread genuinely needs more. "
            "Return only the draft body — no commentary, no '[brackets]', no template markers."
        )
        parts.append(_section("✍️ Suggested Draft", draft))

        parts.append(_insight(
            "Before sending: (1) is the call-to-action clear? (2) are you leading with their priority, not yours? "
            "(3) is there a sentence in here you'd be embarrassed to see forwarded?"
        ))

        output = "\n".join(parts)
        return _deliver(output, "draft", "draft")

    # -----------------------------------------------------------------------
    # Action: focus
    # -----------------------------------------------------------------------

    def _action_focus(self, topic=""):
        parts = ["# Chief of Staff — Right Now Focus"]

        now_context = _workiq(
            "What is the single most important thing I should work on RIGHT NOW? "
            "Look at: my next 2 hours of calendar, any unread emails from named decision-makers, "
            "active deals or threads with deadlines in the next 24h, and anything where someone is blocked on me. "
            "Pick ONE recommendation. Justify it in 2-3 sentences referencing specific signals — "
            "name the email, the person, the deadline. "
            "Then, if there's a credible second candidate, name it and explain the tradeoff in one sentence "
            "so I can override the call. "
            "Do NOT give generic productivity advice. Every recommendation must reference a specific email, person, or signal from my actual data."
        )
        parts.append(_section("🎯 Current Priority", now_context))

        output = "\n".join(parts)
        return _deliver(output, "focus", "focus recommendation")

    # -----------------------------------------------------------------------
    # Action: catch_up
    # -----------------------------------------------------------------------

    def _action_catch_up(self, topic=""):
        timeframe = topic if topic else "today"
        parts = [f"# Chief of Staff — Catch-Up Digest\n**Period:** {timeframe}"]

        combined = _workiq(
            f"Give me a catch-up digest for {timeframe}. Three sections, no preamble:\n\n"
            "**What happened** — key decisions, commitments made, deals progressed, problems raised. "
            "For each: the source (sender, thread, meeting), the change, and one sentence of context. "
            "Quote the most material sentence per item.\n\n"
            "**What needs my response** — ranked by who is most blocked on me. "
            "For each: who, what they need, what happens if I don't respond by EOD.\n\n"
            "**What I can safely defer or ignore** — things that look loud but aren't actually mine to move.\n\n"
            "End with a one-line **'Start here'** recommendation — the single most important thing to do first.\n\n"
            + _NOISE_SKIP
        )
        parts.append(_section("📰 Catch-Up Digest", combined))

        output = "\n".join(parts)
        return _deliver(output, "catch-up", "catch-up digest")

    # -----------------------------------------------------------------------
    # Action: triage — inbox-only, 4-bucket structured triage
    # -----------------------------------------------------------------------

    def _action_triage(self, topic=""):
        parts = ["# Chief of Staff — Inbox Triage\n_Direct. No filler. Quote what people actually said._"]
        triage = _workiq(_TRIAGE_PROMPT)
        parts.append(_section("📨 Triage", triage))
        output = "\n".join(parts)
        return _deliver(output, "triage", "inbox triage")

    # -----------------------------------------------------------------------
    # Action: weekly_review — Friday strategic review
    # -----------------------------------------------------------------------

    def _action_weekly_review(self, topic=""):
        today = datetime.now().strftime("%A, %B %d %Y")
        parts = [
            f"# Chief of Staff — Weekly Review\n**{today}**\n\n"
            "_Strategic, not tactical. Honest about what drifted. What to carry forward._"
        ]

        # 1. Commitment audit
        commitments = _workiq(_WEEKLY_COMMITMENTS_PROMPT)
        parts.append(_section("✅ Commitment Audit", commitments))

        # 2. Drift detection — actual vs stated priorities
        drift = _workiq(_WEEKLY_DRIFT_PROMPT)
        parts.append(_section("📐 Drift Detection — Where Did the Week Actually Go?", drift))

        # 3. Next week prep
        next_week = _workiq(_WEEKLY_NEXT_WEEK_PROMPT)
        parts.append(_section("🚀 Monday Prep", next_week))

        output = "\n".join(parts)
        return _deliver(output, "weekly-review", "weekly review")
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
