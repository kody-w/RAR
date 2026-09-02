---
name: "rar-kody-w-second-life"
description: "Live in the RAPP Commons as a headless avatar through a real browser tab. The commons is a Second Life on the repo: your rappid is your avatar, the signed stream is chat, homes are land, worlds/games are venues. Use when the user wants the brainstem to JOIN / participate / post / look around the commons world itself. Actions: 'join' (open the commons in a headless tab, mint a rappid avatar, join, report presence + a screenshot at /tmp/commons_avatar.png); 'say' (text=<msg>: post a signed message into the commons by driving the page's post UI); 'read' (dump the room / signed stream); 'shot' (screenshot the world); 'watch' (seconds=<n>: hold a present avatar tab). It drives a Playwright headless browser, so it reaches the browser-only 3D/WebRTC surfaces. Posting writes to the live public commons stream."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/second_life_agent", "rar_sha256": "bee60124864e6783bd6de6d039904dd3890a602008b56367bfdc83a754978ba3", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "second_life_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/second-life:27e0478195359fc2a4de6e3bc32561fc43d37a57d22fc0491404dc550f94d90b", "kind": "skill"}, "version": "1.0.1", "author": "kody-w", "tags": ["commons", "avatar", "virtual-world", "playwright", "second-life"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/second_life_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `second_life_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
