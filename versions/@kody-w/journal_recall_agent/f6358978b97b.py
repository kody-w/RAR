# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/journal_recall_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/journal_recall_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/journal_recall_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""Journal Recall — ask your Brainstem what you two said before, from the record you own.

"What did I ask about the Peru trip?", "what did we say last Tuesday?", "stop logging for a while", "are you
keeping the log?" The answers come from the Brainstem Journal on this device (the sidecar on :7074, fed by the
journal_tap grail layer). Nothing leaves the device; the agent only reads the journal's search door.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/journal_recall_agent",
    "version": "1.0.0",
    "display_name": "Journal Recall",
    "description": "Finds earlier conversations in the owner's Brainstem Journal (what did I ask about X, what did we say last Tuesday) and pauses or resumes the journal's recording from chat.",
    "author": "kody-w",
    "tags": ["journal", "memory", "history", "search", "recall"],
    "category": "memory",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import json
import os
import urllib.parse
import urllib.request

from agents.basic_agent import BasicAgent

JOURNAL = os.environ.get("JOURNAL_URL", "http://127.0.0.1:7074").rstrip("/")
STORE = os.path.expanduser(os.environ.get("JOURNAL_STORE", "~/.brainstem/journal"))
PAUSED = os.path.join(STORE, "paused")
DOWN = ("The journal is not running on this device, so there is no record to search. "
        "It starts with: python3 journal.py (brainstem-journal) or `journal install-login`.")


class JournalRecallAgent(BasicAgent):
    def __init__(self):
        self.name = "JournalRecall"
        self.metadata = {
            "name": self.name,
            "description": (
                "Look up earlier conversations with this Brainstem from the owner's own journal: 'what did I ask "
                "about X', 'what did we say last Tuesday', 'find the answer about Y' (action recall, with query and "
                "optional since/until dates). Also 'stop logging' / 'pause the journal' (pause_logging), 'start "
                "logging again' (resume_logging), and 'are you keeping the log?' (status)."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["recall", "pause_logging", "resume_logging", "status"]},
                    "query": {"type": "string", "description": "for recall: the words to look for (topic, name, phrase)"},
                    "since": {"type": "string", "description": "for recall: ISO date or datetime, e.g. 2026-11-01"},
                    "until": {"type": "string", "description": "for recall: ISO date or datetime"},
                    "n": {"type": "integer", "description": "for recall: how many matches (default 10)"},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    def _get(self, path):
        with urllib.request.urlopen(JOURNAL + path, timeout=10) as r:
            return json.loads(r.read().decode("utf-8"))

    def perform(self, action="recall", query=None, since=None, until=None, n=None, **_):
        if action == "pause_logging":
            os.makedirs(STORE, exist_ok=True)
            open(PAUSED, "a").close()
            return "Paused: new turns are not being recorded in the journal until you say to start again."
        if action == "resume_logging":
            try:
                os.remove(PAUSED)
            except FileNotFoundError:
                pass
            return "Recording again: every turn goes to the journal on this device."
        if action == "status":
            paused = os.path.exists(PAUSED)
            try:
                st = self._get("/journal/stats")
            except Exception:
                return DOWN + (" Recording is also paused." if paused else "")
            return (f"The journal holds {st.get('frames', 0)} recorded turns at {st.get('store')}. "
                    + ("Recording is PAUSED." if paused else "Recording is on."))
        # recall
        if not query or not str(query).strip():
            return "Tell me what to look for, e.g. 'what did I ask about the Peru trip'."
        q = {"q": query, "n": int(n or 10)}
        if since:
            q["since"] = since
        if until:
            q["until"] = until
        try:
            res = self._get("/journal/search?" + urllib.parse.urlencode(q))
        except Exception:
            return DOWN
        hits = res.get("hits") or []
        if not hits:
            return f"Nothing in the journal matches '{query}'" + (f" since {since}" if since else "") + "."
        lines = [f"From the journal ({res.get('total', len(hits))} matching turn(s); answer only from these):"]
        for h in hits:
            at = (h.get("at") or "")[:16].replace("T", " ")
            req = " ".join((h.get("request") or "").split())[:160]
            ans = " ".join((h.get("response") or "").split())[:240]
            mark = f" [{h['reaction']}]" if h.get("reaction") else ""
            lines.append(f"- {at}  you: {req}  |  it: {ans}{mark}")
        return "\n".join(lines)
