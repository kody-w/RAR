---
name: "rar-rapp-start-brainstem"
description: "Start the person's Brainstem on this computer. Use when they say 'start my Brainstem', 'install a Brainstem' or 'is my Brainstem up'. It reports one already running, starts an installed one, or installs one after the person says yes. Pass yes=true only after the person has agreed to the install."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/start_brainstem_agent", "rar_sha256": "f07dc57512a2a1b5d8b72aa69f3536b4512cdfb3f59d08d5e2be0076d3484fa9", "source_kind": "rar-agent", "source_commit": "06760087109e14174031ee39b3dcb4bca4d70f93", "author": "RAPP", "tags": ["brainstem", "install", "start", "onboarding"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `start_brainstem_agent.py` and embedded as the fenced Python below (sha256 f07dc57512a2a1b5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `start_brainstem_agent.py` first:

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
    "version": "1.0.0",
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
    if h.get("copilot") != "✓":
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
