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
