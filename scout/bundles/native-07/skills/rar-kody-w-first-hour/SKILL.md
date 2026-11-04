---
name: "rar-kody-w-first-hour"
description: "Walks someone through their first hour with their Brainstem, one step at a time. Call it when they ask to learn, get started, take the tour, or want the next step. Give the step back in your own short words and end by offering the next step."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/first_hour_agent", "rar_sha256": "c9db0320a031fc0801f3fca2d73bf8a1a3d44987e1da95d3758f933a83c46585", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "@kody-w", "tags": ["first-hour", "learn", "getting-started"]}
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
