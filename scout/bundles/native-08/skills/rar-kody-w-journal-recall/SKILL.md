---
name: "rar-kody-w-journal-recall"
description: "Look up earlier conversations with this Brainstem from the owner's own journal: 'what did I ask about X', 'what did we say last Tuesday', 'find the answer about Y' (action recall, with query and optional since/until dates). Also 'stop logging' / 'pause the journal' (pause_logging), 'start logging again' (resume_logging), and 'are you keeping the log?' (status)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/journal_recall_agent", "rar_sha256": "f97b91e25360b4feb4cd29957e5615339d25394198093d859eaa5e8e45977fac", "source_kind": "rar-agent", "source_commit": "777f5ce19728ba74c8d1225b6d777f3d391df5b2", "author": "kody-w", "tags": ["journal", "memory", "history", "search", "recall"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `journal_recall_agent.py` and embedded as the fenced Python below (sha256 f97b91e25360b4fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `journal_recall_agent.py` first:

```bash
python3 journal_recall_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 journal_recall_agent.py   # or on stdin
python3 journal_recall_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
