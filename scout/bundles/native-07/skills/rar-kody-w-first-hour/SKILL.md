---
name: "rar-kody-w-first-hour"
description: "Walks someone through their first hour with their Brainstem, one step at a time. Call it when they ask to learn, get started, take the tour, or want the next step. Give the step back in your own short words and end by offering the next step."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/first_hour_agent", "rar_sha256": "61dd52033a67e19c2c88909a379cfd2a855a1c18f76065ecde2bb330a3681997", "source_kind": "rar-agent", "source_commit": "9c74e2746f3c7ad967bba5618a4b12763742f74c", "author": "@kody-w", "tags": ["first-hour", "learn", "getting-started"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/first_hour_agent`. The original RAPP
agent is preserved byte-for-byte in `first_hour_agent.py` and in the RCI capsule.

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

FirstHour: your first hour with your Brainstem, as one agent.

Drag this file onto your Brainstem window and click OK. Then say: teach me my first hour.
It is one file that does one job, like every agent. Read it: the six steps are below, in plain words.

Your AI, as files you own.
1. Learn it in an hour. It thinks the way you do, so you can see how it works.
2. Run it on any computer. Mac, Windows or Linux. Its memory stays in your own folder.
3. Hand it to anyone. It is just files. One agent is one file.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "step": {
      "description": "Which step, 1 to 6. Use 1 to start.",
      "maximum": 6,
      "minimum": 1,
      "type": "integer"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `first_hour_agent.py` and embedded as the fenced Python below (sha256 61dd52033a67e19c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `first_hour_agent.py` first:

```bash
python3 first_hour_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 first_hour_agent.py   # or on stdin
python3 first_hour_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""FirstHour: your first hour with your Brainstem, as one agent.

Drag this file onto your Brainstem window and click OK. Then say: teach me my first hour.
It is one file that does one job, like every agent. Read it: the six steps are below, in plain words.

Your AI, as files you own.
1. Learn it in an hour. It thinks the way you do, so you can see how it works.
2. Run it on any computer. Mac, Windows or Linux. Its memory stays in your own folder.
3. Hand it to anyone. It is just files. One agent is one file.
"""
try:
    from agents.basic_agent import BasicAgent
except ImportError:  # outside a Brainstem, for example the registry's own tests
    from basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/first_hour_agent",
    "version": "1.0.0",
    "display_name": "FirstHour",
    "description": "Walks you through your first hour with your Brainstem, one step at a time.",
    "author": "@kody-w",
    "tags": ["first-hour", "learn", "getting-started"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

STEPS = [
    ("Get your Brainstem.",
     "You already did: you are talking to it. It runs while its Terminal window is open. "
     "Paste the install line again any time to bring it back, memory and all."),
    ("Talk to it.",
     "Tell me one thing to remember about you, like your favorite coffee. "
     "Tomorrow, ask me what I remember. My memory is a file in your Brainstem's folder."),
    ("See what it can do.",
     "Click the circled plus at the top right (it says Manage installed agents when you point at it). "
     "Each one listed is an agent: one file that does one job. I am one of them: FirstHour."),
    ("Read an agent.",
     "Click Export next to ManageMemory. Your browser saves a small file, usually in Downloads. "
     "Drag it into a chat with any AI and ask: Explain this in plain words. "
     "It is a short program for one job: saving what you ask me to remember."),
    ("Make your own.",
     "In that same chat, ask for a new agent just like it, for a chore you repeat, as a file you can download. "
     "Drag that file onto this window and click OK when it asks. I use it on your next message. "
     "If it says the agent did not load, paste that message into the chat and ask for a fix."),
    ("Hand it on.",
     "Export your new agent and send the file to a friend. They drag it onto their Brainstem and it works "
     "the same way. Or share it in the registry: https://github.com/kody-w/RAR"),
]


class FirstHourAgent(BasicAgent):
    def __init__(self):
        self.name = "FirstHour"
        self.metadata = {
            "name": self.name,
            "description": (
                "Walks someone through their first hour with their Brainstem, one step at a time. "
                "Call it when they ask to learn, get started, take the tour, or want the next step. "
                "Give the step back in your own short words and end by offering the next step."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "step": {"type": "integer", "description": "Which step, 1 to 6. Use 1 to start.",
                             "minimum": 1, "maximum": 6}
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, step=1, **kwargs):
        try:
            step = max(1, min(len(STEPS), int(step)))
        except (TypeError, ValueError):
            step = 1
        title, text = STEPS[step - 1]
        after = (f" When you are ready, say next for step {step + 1} of {len(STEPS)}."
                 if step < len(STEPS) else
                 " That is the hour. Tomorrow I am still here, on your computer, remembering. "
                 "Your AI, as files you own.")
        return f"Step {step} of {len(STEPS)}: {title} {text}{after}"
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
