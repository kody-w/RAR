"""Summon Agent — scan a RAR card's QR code on your phone and it lands in this Brainstem.

Starts (or stops) the summon sidecar beside this Brainstem. The sidecar is fetched from
RAR's stacks/summon/ and its sha256 is checked against the RAR registry before it runs.
It listens only on this Mac and its Tailscale address, and installs cards through the
Brainstem's own /agents/import, which checks every file's sha256 again. Nothing in the
Brainstem kernel changes.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/summon_agent",
    "version": "1.1.0",
    "display_name": "Summon",
    "description": "Starts a sidecar so scanning a RAR card's QR code on your phone installs that card into this Brainstem over Tailscale.",
    "author": "kody-w",
    "tags": ["summon", "qr", "install", "tailscale", "stack"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import hashlib
import json
import os
import signal
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

from agents.basic_agent import BasicAgent

RAR_BASE = os.getenv("RAR_BASE", "https://raw.githubusercontent.com/kody-w/RAR/main")


def _brain_port():
    return os.getenv("PORT", "7071")


def _home():
    d = Path.home() / ".brainstem" / f"summon-{_brain_port()}"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _port_owner(port):
    out = subprocess.run(["lsof", "-tnP", f"-iTCP:{port}", "-sTCP:LISTEN"],
                         capture_output=True, text=True).stdout.split()
    return int(out[0]) if out else None


class SummonAgent(BasicAgent):
    def __init__(self):
        self.name = "Summon"
        self.metadata = {
            "name": self.name,
            "description": ("Set up or check scan-to-summon: lets the owner scan a RAR card's QR code "
                            "with their phone to install it into this Brainstem. Use action 'start' to "
                            "turn it on and get the pairing page, 'status' to check it, 'stop' to turn it off. "
                            "'distros' lists summoned distros; 'dismiss' (name) stops one and moves it, memory "
                            "included, to the attic; 'restore' (name) brings the newest dismissed copy back."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["start", "status", "stop", "distros", "dismiss", "restore"],
                               "description": "what to do"},
                    "name": {"type": "string", "description": "distro name, for dismiss or restore"},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        action = kwargs.get("action", "status")
        port = int(os.getenv("SUMMON_PORT", "7390"))
        pidf = _home() / "summond.pid"
        pid = int(pidf.read_text()) if pidf.exists() else None
        running = pid is not None and _port_owner(port) == pid

        if action in ("distros", "dismiss", "restore"):
            if not running:
                return "Summon is off, so there are no summoned distros to manage. Ask me to start it."
            name = (kwargs.get("name") or "").strip().lower()
            if action == "distros":
                req = urllib.request.Request(f"http://127.0.0.1:{port}/distros")
            else:
                if not name:
                    return f"Which distro should I {action}?"
                req = urllib.request.Request(f"http://127.0.0.1:{port}/{action}/{urllib.parse.quote(name)}",
                                             data=b"", method="POST")
            out = json.loads(urllib.request.urlopen(req, timeout=180).read())
            if action == "distros":
                on = [f"{d['name']} ({'running' if d['running'] else 'stopped'})" for d in out["summoned"]]
                return (f"Summoned: {', '.join(on) or 'none'}. "
                        f"In the attic: {', '.join(out['dismissed']) or 'none'}.")
            if not out.get("ok"):
                return f"Couldn't {action} {name}: {out.get('error')}"
            if action == "dismiss":
                return f"{name} is stopped and moved to the attic with its memory. Say 'restore {name}' to bring it back."
            return (f"{name} is back with its memory. On this Mac open {out.get('local_url')}; "
                    "on your phone, scan its card again.")
        if action == "status":
            return (f"Summon is on. Pair your phone at http://127.0.0.1:{port}/pair" if running
                    else "Summon is off. Ask me to start it.")
        if action == "stop":
            if running:
                os.kill(pid, signal.SIGTERM)
                pidf.unlink(missing_ok=True)
                return "Summon is off."
            return "Summon was already off."
        if running:
            return f"Summon is already on. Pair your phone at http://127.0.0.1:{port}/pair"
        owner = _port_owner(port)
        if owner:
            return f"Port {port} is already used by another program (pid {owner}), so Summon can't start."

        # Fetch the sidecar from RAR and check it against the registry before it ever runs.
        reg = json.loads(urllib.request.urlopen(f"{RAR_BASE}/registry.json", timeout=30).read())
        pack = next((p for p in reg.get("stack_packs", []) if p["name"] == "summon"), None)
        if not pack or not pack.get("_verified"):
            return "RAR does not list a verified summon stack, so nothing was started."
        want = pack["files"]["summond.py"]["sha256"]
        body = urllib.request.urlopen(f"{RAR_BASE}/{pack['path']}/summond.py", timeout=30).read()
        if hashlib.sha256(body).hexdigest() != want:
            return "The summon sidecar from RAR did not match its fingerprint, so nothing was started."
        script = _home() / "summond.py"
        script.write_bytes(body)

        proc = subprocess.Popen(
            [sys.executable, str(script), f"http://127.0.0.1:{_brain_port()}", str(port), RAR_BASE],
            env={**os.environ, "SUMMON_HOME": str(_home())},
            stdout=open(_home() / "summond.log", "w"), stderr=subprocess.STDOUT,
            start_new_session=True)
        for _ in range(50):
            if proc.poll() is not None:
                return f"Summon failed to start (see {_home() / 'summond.log'})."
            if _port_owner(port) == proc.pid:
                pidf.write_text(str(proc.pid))
                return (f"Summon is on. Open http://127.0.0.1:{port}/pair on this Mac and scan the code "
                        "with your phone (it must be on your Tailscale network). After that, scanning any "
                        "RAR card installs it here.")
            time.sleep(0.2)
        proc.kill()
        return "Summon did not come up in time, so it was stopped."
