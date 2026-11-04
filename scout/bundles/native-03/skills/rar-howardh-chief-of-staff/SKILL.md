---
name: "rar-howardh-chief-of-staff"
description: "Chief of Staff \u2014 your personal AI executive partner powered by LIVE Microsoft 365 data. Use this agent (NOT Obsidian) when the user wants: a morning/daily brief from their actual email and calendar, meeting prep using real email history, open action items or commitments from their inbox, drafting a real email reply, industry/market signal pulse, 'what should I work on now?', or a catch-up digest of missed emails. This agent queries LIVE M365 data via WorkIQ \u2014 it sees your real emails, meetings, and Teams messages. Obsidian is for local wiki notes. ChiefOfStaff is for live work data from Microsoft 365."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/chief_of_staff_agent", "rar_sha256": "fedbb91cc50aca1912b9b29727b385cf6a4e06507e808d67ccb690a8eb4df9bc", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Howard Hoy", "tags": ["productivity", "chief-of-staff", "m365", "workiq", "executive", "triage", "meeting-prep"]}
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
