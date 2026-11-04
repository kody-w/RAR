---
name: "rar-kody-w-journal-recall"
description: "Look up earlier conversations with this Brainstem from the owner's own journal: 'what did I ask about X', 'what did we say last Tuesday', 'find the answer about Y' (action recall, with query and optional since/until dates). Also 'stop logging' / 'pause the journal' (pause_logging), 'start logging again' (resume_logging), and 'are you keeping the log?' (status)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/journal_recall_agent", "rar_sha256": "f6358978b97b93606c74b987803dfc099f42e3ff143825040616102d5f8201bf", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "kody-w", "tags": ["journal", "memory", "history", "search", "recall"]}
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
