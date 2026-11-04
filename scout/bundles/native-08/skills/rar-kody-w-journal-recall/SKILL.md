---
name: "rar-kody-w-journal-recall"
description: "Look up earlier conversations with this Brainstem from the owner's own journal: 'what did I ask about X', 'what did we say last Tuesday', 'find the answer about Y' (action recall, with query and optional since/until dates). Also 'stop logging' / 'pause the journal' (pause_logging), 'start logging again' (resume_logging), and 'are you keeping the log?' (status)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/journal_recall_agent", "rar_sha256": "f6358978b97b93606c74b987803dfc099f42e3ff143825040616102d5f8201bf", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "kody-w", "tags": ["journal", "memory", "history", "search", "recall"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/journal_recall_agent`. The original RAPP
agent is preserved byte-for-byte in `journal_recall_agent.py` and in the RCI capsule.

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

Journal Recall — ask your Brainstem what you two said before, from the record you own.

"What did I ask about the Peru trip?", "what did we say last Tuesday?", "stop logging for a while", "are you
keeping the log?" The answers come from the Brainstem Journal on this device (the sidecar on :7074, fed by the
journal_tap grail layer). Nothing leaves the device; the agent only reads the journal's search door.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "enum": [
        "recall",
        "pause_logging",
        "resume_logging",
        "status"
      ],
      "type": "string"
    },
    "n": {
      "description": "for recall: how many matches (default 10)",
      "type": "integer"
    },
    "query": {
      "description": "for recall: the words to look for (topic, name, phrase)",
      "type": "string"
    },
    "since": {
      "description": "for recall: ISO date or datetime, e.g. 2026-11-01",
      "type": "string"
    },
    "until": {
      "description": "for recall: ISO date or datetime",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `journal_recall_agent.py` and embedded as the fenced Python below (sha256 f6358978b97b9360…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `journal_recall_agent.py` first:

```bash
python3 journal_recall_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 journal_recall_agent.py   # or on stdin
python3 journal_recall_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
