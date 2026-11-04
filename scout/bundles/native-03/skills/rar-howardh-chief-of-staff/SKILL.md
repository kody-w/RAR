---
name: "rar-howardh-chief-of-staff"
description: "Chief of Staff \u2014 your personal AI executive partner powered by LIVE Microsoft 365 data. Use this agent (NOT Obsidian) when the user wants: a morning/daily brief from their actual email and calendar, meeting prep using real email history, open action items or commitments from their inbox, drafting a real email reply, industry/market signal pulse, 'what should I work on now?', or a catch-up digest of missed emails. This agent queries LIVE M365 data via WorkIQ \u2014 it sees your real emails, meetings, and Teams messages. Obsidian is for local wiki notes. ChiefOfStaff is for live work data from Microsoft 365."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/chief_of_staff_agent", "rar_sha256": "fedbb91cc50aca1912b9b29727b385cf6a4e06507e808d67ccb690a8eb4df9bc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Howard Hoy", "tags": ["productivity", "chief-of-staff", "m365", "workiq", "executive", "triage", "meeting-prep"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `chief_of_staff_agent.py` and embedded as the fenced Python below (sha256 fedbb91cc50aca19…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `chief_of_staff_agent.py` first:

```bash
python3 chief_of_staff_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 chief_of_staff_agent.py   # or on stdin
python3 chief_of_staff_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@howardh/chief_of_staff_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/chief_of_staff_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@howardh/chief_of_staff_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
