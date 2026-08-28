---
name: "rar-kody-w-second-life"
description: "Live in the RAPP Commons as a headless avatar through a real browser tab. The commons is a Second Life on the repo: your rappid is your avatar, the signed stream is chat, homes are land, worlds/games are venues. Use when the user wants the brainstem to JOIN / participate / post / look around the commons world itself. Actions: 'join' (open the commons in a headless tab, mint a rappid avatar, join, report presence + a screenshot at /tmp/commons_avatar.png); 'say' (text=<msg>: post a signed message into the commons by driving the page's post UI); 'read' (dump the room / signed stream); 'shot' (screenshot the world); 'watch' (seconds=<n>: hold a present avatar tab). It drives a Playwright headless browser, so it reaches the browser-only 3D/WebRTC surfaces. Posting writes to the live public commons stream."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/second_life_agent", "rar_sha256": "bee60124864e6783bd6de6d039904dd3890a602008b56367bfdc83a754978ba3", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "kody-w", "tags": ["commons", "avatar", "virtual-world", "playwright", "second-life"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `second_life_agent.py` and embedded as the fenced Python below (sha256 bee60124864e6783…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `second_life_agent.py` first:

```bash
python3 second_life_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 second_life_agent.py   # or on stdin
python3 second_life_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
