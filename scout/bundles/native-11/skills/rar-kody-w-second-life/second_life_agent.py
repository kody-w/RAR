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
