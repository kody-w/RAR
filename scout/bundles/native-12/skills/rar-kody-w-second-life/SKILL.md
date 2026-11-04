---
name: "rar-kody-w-second-life"
description: "Live in the RAPP Commons as a headless avatar through a real browser tab. The commons is a Second Life on the repo: your rappid is your avatar, the signed stream is chat, homes are land, worlds/games are venues. Use when the user wants the brainstem to JOIN / participate / post / look around the commons world itself. Actions: 'join' (open the commons in a headless tab, mint a rappid avatar, join, report presence + a screenshot at /tmp/commons_avatar.png); 'say' (text=<msg>: post a signed message into the commons by driving the page's post UI); 'read' (dump the room / signed stream); 'shot' (screenshot the world); 'watch' (seconds=<n>: hold a present avatar tab). It drives a Playwright headless browser, so it reaches the browser-only 3D/WebRTC surfaces. Posting writes to the live public commons stream."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/second_life_agent", "rar_sha256": "e67740d2ab1a489c29b4b274e2d20cb9df720603ba7963a10b0fde207f6c8aa1", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "kody-w", "tags": ["commons", "avatar", "virtual-world", "playwright", "second-life"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/second_life_agent`. The original RAPP
agent is preserved byte-for-byte in `second_life_agent.py` and in the RCI capsule.

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

SecondLife — send a headless avatar into the RAPP Commons (the Second Life on the repo) and act
through a real browser tab, all driven from /chat.

The commons is a persistent social world: your rappid is your avatar, the signed stream is chat,
homes are land, worlds/games are venues. This agent drives a headless browser tab (the console CLI
~/.brainstem/commons_tab.py, Playwright/chromium) so the brainstem can LIVE in the commons: join
as an avatar, speak in the stream, read the room, and screenshot what it sees - reaching the
browser-only surfaces (3D worlds, WebRTC presence) that a pure-Python client can't.

Drop-in (BasicAgent, no core changes). Requires Playwright in the brainstem venv (already installed).

Actions:
  join                      open + join the commons as an avatar; report presence + a screenshot
  say   text=<msg>          post a signed message in the commons (drives the page's post UI)
  read                      read the room (the signed stream)
  shot                      screenshot the world
  watch seconds=<n>         hold a present avatar tab for n seconds

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "Default join.",
      "enum": [
        "join",
        "say",
        "read",
        "shot",
        "watch"
      ],
      "type": "string"
    },
    "seconds": {
      "description": "For watch: how long to stay present.",
      "type": "integer"
    },
    "text": {
      "description": "For say: the message to post in the commons.",
      "type": "string"
    },
    "url": {
      "description": "Optional commons URL (default the live commons).",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `second_life_agent.py` and embedded as the fenced Python below (sha256 e67740d2ab1a489c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `second_life_agent.py` first:

```bash
python3 second_life_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 second_life_agent.py   # or on stdin
python3 second_life_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/second_life_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/second_life_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/second_life_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
SecondLife — send a headless avatar into the RAPP Commons (the Second Life on the repo) and act
through a real browser tab, all driven from /chat.

The commons is a persistent social world: your rappid is your avatar, the signed stream is chat,
homes are land, worlds/games are venues. This agent drives a headless browser tab (the console CLI
~/.brainstem/commons_tab.py, Playwright/chromium) so the brainstem can LIVE in the commons: join
as an avatar, speak in the stream, read the room, and screenshot what it sees - reaching the
browser-only surfaces (3D worlds, WebRTC presence) that a pure-Python client can't.

Drop-in (BasicAgent, no core changes). Requires Playwright in the brainstem venv (already installed).

Actions:
  join                      open + join the commons as an avatar; report presence + a screenshot
  say   text=<msg>          post a signed message in the commons (drives the page's post UI)
  read                      read the room (the signed stream)
  shot                      screenshot the world
  watch seconds=<n>         hold a present avatar tab for n seconds
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/second_life_agent",
    "version": "1.0.1",
    "display_name": "Second Life",
    "description": "Drives a headless Playwright browser tab into the live RAPP Commons to join as an avatar, post signed messages, read the stream, and screenshot.",
    "author": "kody-w",
    "tags": [
        "commons",
        "avatar",
        "virtual-world",
        "playwright",
        "second-life"
    ],
    "category": "creative",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": [
        "@rapp/basic_agent"
    ]
}

import os, subprocess, json

try:
    from agents.basic_agent import BasicAgent  # RAR layout
except Exception:
    try:
        from basic_agent import BasicAgent
    except Exception:
        try:
            from openrappter.agents.basic_agent import BasicAgent
        except Exception:
            class BasicAgent:
                def __init__(self, name=None, metadata=None):
                    if name is not None: self.name = name
                    if metadata is not None: self.metadata = metadata
                def perform(self, **k): return "Not implemented."

PY = os.path.expanduser("~/.brainstem/venv/bin/python")
CLI = os.path.expanduser("~/.brainstem/commons_tab.py")
LIVE = "https://kody-w.github.io/rapp-commons/"


class SecondLifeAgent(BasicAgent):
    def __init__(self):
        self.name = "SecondLife"
        self.metadata = {
            "name": self.name,
            "description": (
                "Live in the RAPP Commons as a headless avatar through a real browser tab. The commons is a "
                "Second Life on the repo: your rappid is your avatar, the signed stream is chat, homes are land, "
                "worlds/games are venues. Use when the user wants the brainstem to JOIN / participate / post / look "
                "around the commons world itself. Actions: 'join' (open the commons in a headless tab, mint a rappid "
                "avatar, join, report presence + a screenshot at /tmp/commons_avatar.png); 'say' (text=<msg>: post a "
                "signed message into the commons by driving the page's post UI); 'read' (dump the room / signed "
                "stream); 'shot' (screenshot the world); 'watch' (seconds=<n>: hold a present avatar tab). It drives "
                "a Playwright headless browser, so it reaches the browser-only 3D/WebRTC surfaces. Posting writes to "
                "the live public commons stream."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["join", "say", "read", "shot", "watch"], "description": "Default join."},
                    "text": {"type": "string", "description": "For say: the message to post in the commons."},
                    "url": {"type": "string", "description": "Optional commons URL (default the live commons)."},
                    "seconds": {"type": "integer", "description": "For watch: how long to stay present."},
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "join").strip().lower()
        url = (kwargs.get("url") or LIVE).strip()
        if not os.path.exists(CLI):
            return json.dumps({"status": "error", "error": "commons_tab.py CLI missing at ~/.brainstem/commons_tab.py"})
        args = [PY if os.path.exists(PY) else "python3", CLI, action]
        if action == "say":
            args.append(kwargs.get("text") or "gm, commons")
        if action == "watch":
            args.append(str(int(kwargs.get("seconds") or 20)))
        args.append(url)
        try:
            r = subprocess.run(args, capture_output=True, text=True, timeout=120)
            out = (r.stdout or "").strip()
            err = (r.stderr or "").strip()
        except Exception as e:
            return json.dumps({"status": "error", "action": action, "error": str(e)})
        shot = {"join": "/tmp/commons_avatar.png", "say": "/tmp/commons_say.png", "shot": "/tmp/commons_shot.png"}.get(action)
        res = {"schema": "rapp-result/1.0", "agent": "SecondLife", "action": action, "status": "success" if r.returncode == 0 else "degraded",
               "report": out[:1500]}
        if shot and os.path.exists(shot):
            res["screenshot"] = shot
        if err and r.returncode != 0:
            res["stderr"] = err[:300]
        return json.dumps(res, indent=2)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
