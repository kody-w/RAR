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
    "version": "1.0.0",
    "display_name": "ChiefOfStaff",
    "description": "Personal AI executive partner — live M365-grounded brief, triage, meeting prep, commitments, drafts, weekly review.",
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