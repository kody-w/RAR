---
name: "rar-rapp-start-brainstem"
description: "Start the person's Brainstem on this computer. Use when they say 'start my Brainstem', 'install a Brainstem' or 'is my Brainstem up'. It reports one already running, starts an installed one, or installs one after the person says yes. Pass yes=true only after the person has agreed to the install."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/start_brainstem_agent", "rar_sha256": "6949e75bf48aa12b8a04a81281db35e95b1f54f016bae4c2bf866b70d49df942", "source_kind": "rar-agent", "source_commit": "fcb927883bdbe52c37698e09e2153daf4ddf045a", "version": "1.0.1", "author": "RAPP", "tags": ["brainstem", "install", "start", "onboarding"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/start_brainstem_agent`. The original RAPP
agent is preserved byte-for-byte in `start_brainstem_agent.py` and in the RCI capsule.

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

start_brainstem_agent — starts the person's Brainstem for them, so they never type the install line.

What it does, in order, and stops at the first that fits:
  1. A Brainstem already answers on this computer  -> says so. Changes nothing.
  2. Something else is using the Brainstem's port  -> says so and stops. It never stops another program.
  3. A Brainstem is installed but not running      -> starts it and waits until it answers.
  4. Nothing is installed                          -> asks for a yes, then downloads the whole installer to a
     file (never piped half-read into a shell), runs it, and waits until the Brainstem answers.

Ask it "status" at any time. It only talks to this computer and to the installer's public page.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "start (default) or status",
      "enum": [
        "start",
        "status"
      ],
      "type": "string"
    },
    "wait": {
      "description": "seconds to wait for it to answer (default 240)",
      "type": "integer"
    },
    "yes": {
      "description": "true only when the person agreed to install",
      "type": "boolean"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `start_brainstem_agent.py` and embedded as the fenced Python below (sha256 6949e75bf48aa12b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `start_brainstem_agent.py` first:

```bash
python3 start_brainstem_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 start_brainstem_agent.py   # or on stdin
python3 start_brainstem_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/start_brainstem_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/start_brainstem_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/start_brainstem_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""start_brainstem_agent — starts the person's Brainstem for them, so they never type the install line.

What it does, in order, and stops at the first that fits:
  1. A Brainstem already answers on this computer  -> says so. Changes nothing.
  2. Something else is using the Brainstem's port  -> says so and stops. It never stops another program.
  3. A Brainstem is installed but not running      -> starts it and waits until it answers.
  4. Nothing is installed                          -> asks for a yes, then downloads the whole installer to a
     file (never piped half-read into a shell), runs it, and waits until the Brainstem answers.

Ask it "status" at any time. It only talks to this computer and to the installer's public page.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/start_brainstem_agent",
    "version": "1.0.1",
    "display_name": "Start Brainstem",
    "description": "Starts the person's Brainstem for them: says if one is already up, starts an installed one, or (after a yes) installs and starts one. Never stops another program.",
    "author": "RAPP",
    "tags": ["brainstem", "install", "start", "onboarding"],
    "category": "devtools",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import hashlib
import json
import os
import re
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    try:
        from basic_agent import BasicAgent
    except ImportError:
        from openrappter.agents.basic_agent import BasicAgent

PORT = 7071
URL = f"http://localhost:{PORT}"
HOME = Path.home() / ".brainstem"
INSTALLER = "https://kody-w.github.io/rapp-installer/install." + ("ps1" if os.name == "nt" else "sh")
LOG = Path(tempfile.gettempdir()) / "start-brainstem.log"


def health():
    """The Brainstem's own health answer, or None."""
    try:
        with urllib.request.urlopen(f"{URL}/health", timeout=2) as r:
            got = json.loads(r.read().decode("utf-8", "replace"))
        return got if isinstance(got, dict) and "agents" in got else None
    except Exception:
        return None


def port_busy():
    s = socket.socket()
    s.settimeout(1)
    try:
        return s.connect_ex(("127.0.0.1", PORT)) == 0
    finally:
        s.close()


def installed():
    """(python, folder) of a whole installed Brainstem, or None. A half-finished install does not count."""
    src = HOME / "src" / "rapp_brainstem"
    for py in (HOME / "venv" / "bin" / "python", HOME / "venv" / "Scripts" / "python.exe"):
        if py.exists() and (src / "brainstem.py").exists():
            try:
                whole = subprocess.run([str(py), "-c", "import flask, requests"], capture_output=True, timeout=30)
            except Exception:
                return None
            return (py, src) if whole.returncode == 0 else None
    return None


def detached(cmd, cwd=None):
    """Run it on its own, so it keeps going after this agent has answered."""
    out = open(LOG, "ab")
    kw = {"stdin": subprocess.DEVNULL, "stdout": out, "stderr": out, "cwd": str(cwd) if cwd else None}
    if os.name == "nt":
        kw["creationflags"] = 0x08000000 | 0x00000200  # no window, own group
    else:
        kw["start_new_session"] = True
    return subprocess.Popen([str(c) for c in cmd], **kw)


def wait_up(seconds, proc=None):
    """The health answer, or None. Stops early when the thing we started has ended without one."""
    end = time.time() + seconds
    while time.time() < end:
        h = health()
        if h:
            return h
        if proc is not None and proc.poll() is not None:
            return health()
        time.sleep(2)
    return None


def log_tail(n=6):
    """The last few plain lines of the log, colour codes removed."""
    if not LOG.exists():
        return ""
    text = re.sub(r"\x1b\[[0-9;]*m", "", LOG.read_bytes()[-2000:].decode("utf-8", "replace"))
    return " | ".join([l.strip() for l in text.splitlines() if l.strip()][-n:])


def stopped(proc, what):
    return {"status": "failed", "say": f"{what} stopped before a Brainstem answered. Nothing else was changed. "
            f"Its last lines: {log_tail()}", "log": str(LOG)}


def fetch_installer():
    """Download the whole installer to a file first. Returns (path, sha256)."""
    with urllib.request.urlopen(INSTALLER, timeout=60) as r:
        body = r.read()
    if len(body) < 2000 or (os.name != "nt" and not body.startswith(b"#!")):
        raise ValueError("the installer did not download whole")
    path = Path(tempfile.mkdtemp(prefix="brainstem-install-")) / INSTALLER.rsplit("/", 1)[1]
    path.write_bytes(body)
    return path, hashlib.sha256(body).hexdigest()


def up(h, how):
    say = f"Your Brainstem is up ({how}). Open {URL}"
    if h.get("status") == "unauthenticated":
        say += f" . It still needs you to sign in once: {URL}/login"
    return {"status": "up", "say": say, "url": URL, "version": h.get("version"), "agents": len(h.get("agents") or [])}


def start(yes=False, wait=240):
    h = health()
    if h:
        return up(h, "it was already running; nothing changed")
    if port_busy():
        return {"status": "blocked", "say": f"Another program is using port {PORT} and it is not a Brainstem. "
                "I will not stop it. Close that program, then ask me again."}
    have = installed()
    if have:
        py, src = have
        proc = detached([py, "brainstem.py"], cwd=src)
        h = wait_up(wait, proc)
        if h:
            return up(h, "started the one already installed")
        if proc.poll() is not None:
            return stopped(proc, "The Brainstem")
        return {"status": "starting", "say": f"I started it but it has not answered yet. Ask me for status. Log: {LOG}"}
    if not yes:
        return {"status": "ask", "say": "No Brainstem is installed on this computer. I can install and start one: "
                f"I download the installer from {INSTALLER}, run it, and it puts everything in {HOME}. "
                "It can take a few minutes. Say yes and I will do it."}
    try:
        path, sha = fetch_installer()
    except Exception as e:
        return {"status": "failed", "say": f"I could not download the installer: {e}"}
    if os.name == "nt":
        cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", path]
    else:
        cmd = ["bash", path]
    proc = detached(cmd)
    h = wait_up(wait, proc)
    if h:
        out = up(h, "installed and started")
        out["installer_sha256"] = sha
        return out
    if proc.poll() is not None:
        out = stopped(proc, "The installer")
        out["installer_sha256"] = sha
        return out
    return {"status": "installing", "installer_sha256": sha,
            "say": f"The install is still running. Ask me for status in a minute. Log: {LOG}"}


def status():
    h = health()
    if h:
        return up(h, "running")
    if port_busy():
        return {"status": "blocked", "say": f"Port {PORT} is in use by something that is not a Brainstem."}
    return {"status": "installed-not-running" if installed() else "not-installed",
            "say": "No Brainstem is answering right now.", "log_tail": log_tail()}


class StartBrainstemAgent(BasicAgent):
    def __init__(self):
        self.name = "StartBrainstem"
        self.metadata = {
            "name": self.name,
            "description": "Start the person's Brainstem on this computer. Use when they say 'start my Brainstem', "
                           "'install a Brainstem' or 'is my Brainstem up'. It reports one already running, starts "
                           "an installed one, or installs one after the person says yes. Pass yes=true only after "
                           "the person has agreed to the install.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["start", "status"], "description": "start (default) or status"},
                    "yes": {"type": "boolean", "description": "true only when the person agreed to install"},
                    "wait": {"type": "integer", "description": "seconds to wait for it to answer (default 240)"},
                },
                "required": [],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs):
        if kwargs.get("action") == "status":
            return json.dumps(status())
        return json.dumps(start(bool(kwargs.get("yes")), int(kwargs.get("wait") or 240)))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
