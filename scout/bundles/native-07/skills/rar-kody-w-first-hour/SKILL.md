---
name: "rar-kody-w-first-hour"
description: "Walks someone through their first hour with their Brainstem, one step at a time. Call it when they ask to learn, get started, take the tour, or want the next step. Give the step back in your own short words and end by offering the next step."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/first_hour_agent", "rar_sha256": "c9db0320a031fc0801f3fca2d73bf8a1a3d44987e1da95d3758f933a83c46585", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "@kody-w", "tags": ["first-hour", "learn", "getting-started"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `first_hour_agent.py` and embedded as the fenced Python below (sha256 c9db0320a031fc08…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `first_hour_agent.py` first:

```bash
python3 first_hour_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 first_hour_agent.py   # or on stdin
python3 first_hour_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/first_hour_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/first_hour_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/first_hour_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
