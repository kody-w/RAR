---
name: "rar-howardh-chief-of-staff"
description: "Chief of Staff \u2014 your personal AI executive partner powered by LIVE Microsoft 365 data. Use this agent (NOT Obsidian) when the user wants: a morning/daily brief from their actual email and calendar, meeting prep using real email history, open action items or commitments from their inbox, drafting a real email reply, industry/market signal pulse, 'what should I work on now?', or a catch-up digest of missed emails. This agent queries LIVE M365 data via WorkIQ \u2014 it sees your real emails, meetings, and Teams messages. Obsidian is for local wiki notes. ChiefOfStaff is for live work data from Microsoft 365."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/chief_of_staff_agent", "rar_sha256": "5d904f34d63faa2271e66a6d1c6f033c269136c840a1bd4d4dcc57875bbf8354", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Howard Hoy", "tags": ["productivity", "chief-of-staff", "m365", "workiq", "executive", "triage", "meeting-prep"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@howardh/chief_of_staff_agent`. The original RAPP
agent is preserved byte-for-byte in `chief_of_staff_agent.py` and in the RCI capsule.

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
