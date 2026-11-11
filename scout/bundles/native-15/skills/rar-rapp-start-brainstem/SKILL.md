---
name: "rar-rapp-start-brainstem"
description: "Start the person's Brainstem on this computer. Use when they say 'start my Brainstem', 'install a Brainstem' or 'is my Brainstem up'. It reports one already running, starts an installed one, or installs one after the person says yes. Pass yes=true only after the person has agreed to the install."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/start_brainstem_agent", "rar_sha256": "d79d1b29cebde0efd3d59750fe7291cd5bb2e8b84a5b752eec86a045fc345dc5", "source_kind": "rar-agent", "source_commit": "a12ea00788f1f38a27375c04d8be93b7e62584be", "version": "1.0.2", "author": "RAPP", "tags": ["brainstem", "install", "start", "onboarding"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `start_brainstem_agent.py` and embedded as the fenced Python below (sha256 d79d1b29cebde0ef…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `start_brainstem_agent.py` first:

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
    "version": "1.0.2",
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
    # Windows PowerShell reads a saved script without an encoding mark as the local code page and then
    # cannot parse it (9 errors, seen 2026-11-10). The mark is added to the saved copy only; the
    # fingerprint reported is of the bytes as downloaded.
    mark = b"\xef\xbb\xbf" if os.name == "nt" and not body.startswith(b"\xef\xbb\xbf") else b""
    path.write_bytes(mark + body)
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/615V7Oj2JbmX1GcfqiqVmYKb2qiJgbhQYAEQgh1dtzCG+GEEaam/vtsdE5WZsW9t59GcSIObNZe5luWzR9v3tCndfv265vJHI9vn97CqAvarOmzugKLVu+1/aZPo00TtV1d/dRt9q2XVV0flZu6Ak+ybhPUZTP0UftlY3fRZkyjdT2aN503b37qXhzK+fu+nz5tflqvvKLYeD8sb+oWPOj+RrsZmp++bOR+00ZN3fYdkBltvKKNvHDetENVZVXyafOS0W28avPBNwpXwk8rx4+Vj50xUPMHc1YVu80cdV82R697Xf3Wt0MEiIv5n6lTDwhJ2giw7+vXgw/uXwBw0eSVTRF1b7/+139/esvA9duvf7wFBeD7Dci/zGKSqOrBnsKrEvCwmYEPKnAP5MR1W4KlMIo3H3c/d1ERf9r853/eR69Nul9+/VptPn5ZvHlf/JJE/c9f37xg9dvXt182v/22+foGdOuH7uvbDzvWXxv1Q1ttcmDSl3Aom+7nd8Kff/nlO+G/JGr7n/26Ln7+m1AAGpD4yycARv/3J6OX9asywA0IBv3yyy9vfwJkAALt8FJ0BeY//mOjZUFbd3Xcb6ygHvrVr31WRl+rr9V5jS/wt2LdRk/ghswvog+6pq3z6MVoU8eb3/9P6zXN7qXlP/xvSP/DW6H+/cvmDDjUbZZklVds1lj/Wr0erdybNuqi9gnc6s999BmA/nm9AAZtfv+X/L408+8g3MKVYlXNZOVN4DXdUERfVrWdNQfelQxAVEZTFIAE2RR1AITHGYiST8Ccri6e0XsKdfcMZEOYtcCeup1fvAEMv67Mfv/9d9/r0q/Ve5igm/cE7XaA4C91Np8/AyviIkvS/msVBWm9+emPP3/a/N/N/7TrxXyV8Yr+d5CBhopl6Bvgx6EEZN0ryEHCvUD+488PLNfkA9kBXJLFWfS+uciqexR+A9aSmM8ITmz8CAAKwCzXDAb5usl6kNLx5i99/0pub5PWXb8JoyaqwqgKZsDVA+b8hWRV9yBl+6yL50+boYteUn//7pwAkP++0dgjyM+6WJMUqPkiApvrKgPw/+X293XApP2xqH3Z6GuYbRoPRFPaeh8yYu/dLyCSv20HzL1NFY1fqzXXoxUqb43Fd3gAEUAm+HDp59Xna50sgWO7b7JfNF4Pwu5ce0B4+7XqPuLZa1dXBDVQZd4kQxZ6VRD9r4+Q6tJ6KMIXfh/16cML4YdXXjH4LwN383VAIBj7VjH/TWEH/loflaCy1u+lvHqB0s9N9GPZWx3+LeA9gAlwXb2GNrCvbsOo/fSK466vG+Db9zYSZ23Xv9wKLvvuVZngLxvmB+nfyrtXdSPQ7Z/azGbz+X+/F+6u/rJhU1BDQfyB0EhBcH1ZGSJfNlZdRq+FTVQAH4LtQ7ferTp8bzkg9UHg/cjwu8avtvNu94cFq4g1NNo6ab3yJQn9u+pZ90MH8oGr1oD9aFPvZXWV9I49QGuVtdZIoByoeMX70svoF3MMBOO7VX9n/G9/gLnX3buX/7y1mX1a7a2AV8aqqL3w3eFjWhd/uXD1KjD6o+6/wvTnd6ObrAGyUq+IP6/++BbxXRoVBSj2wKrVhk//ZMTfEP7Bnq8V091XE7/3pTUovApkOaj2L7hfbReoBWx4Ndgfvb7K+XvXfWVuM/gFyLMGhPfahcF1BLLo7ddqKIpPb5VXRv/UfddGC9IbBAjQbG3SwKMgC/oset29N9H16u+z0Psk8zPozN5Q9K+u9m7I2vyrAXTt/3qnAfcfD8AgsObMa3ML/Lj2vxWrf8EcJPtaGoCFK8HLheDfCvkLwb/kvjrp2198gVeiJGpXxvO7+n/n+32a+TaXfRtmvg8yH3B+Z7r2+Mir3v4EXNvoMYAaFr6PNR8Etb823lVoU3j9+8jyxxsA1Au93vuA9KM3A/LWaz93a+nawV8gIAbcv5cj8Ox/6NoflF3qgTayzkQkHcI+QgeRH0ZQFIdoiNMkDsURidBwEOK+j0SUT2Ee7pM4EkUBRXgQhscBiuFhgK9+qYc2iP6xVuLVC28ejEQeBJEUFcMxSnkIiZJ4AGEh5Uc06pMRgeAU5kfft96zKvww6V3JFaS/BohX/Lxb9sebT2CAUsI6mXn/sbvtxUOvB39KnS0O6x126jjtVNGKZFtNObYKRGRieHUcHpsl+8oxLl9kp4TnjYUV+JupjFtToeYzzfWVMA5MXVoVeYHwe5J0Qhkfq373rHT7TMX987lVpCd3x49TQOTetvDrGDKKS1Y6Nwvjulkj1MtyvNjC4W4jqLM356g6FUjlWL5V8fFRJKEhqLC+l8/RdtEJ+U5c66x6WI0121VC230w16aYsjh/sS3FOpo3E+33RNxLBgudAtzRPedBtap7tbrCPN+5Tp3c7mFVmubL1m46aNOsmaaeer4q4XRwZR38edWFrSrp/FZtbw9VmkkjaVjMEfvwnFBGdFQJW2oJIhIrcwxb0bkQh5vCqg1/FZu5br2pVmKSD2+OMl+UsDpKJJtYQ0ZYN1/TL48+huX7fEjm+jGPxSSIzq1lyO7i5Q6WRlOmn7xexjnKQVKFPMfazTWLwArYQXGg8/N2gQLjEWUwefSxy77SXV41lev21C1B5Y+khozhTpmxY6Rf8TqztzgWpoibKnKMw/yhlvbEQ40uuxBV/NNpPmlXZLePZvzZy/n1brr+w7Si+4wLrc/QknPwJkLC8pJOfO+q0XNfHkTmgBPUE61rTqmubWIz8HlnzHCP25HIu2Bsijt1fDiOqztntZtc/T7PyhV6GJdnvcwN3NihRWZuayjU/aQcJ8UfzlxX3UYxno5xo+8ZFFL2dlFyLGXjiLLdmhR7nGOXuUpz0u6m3a4eqYXuWiOWyJaklPihuDPkkoEcG7tbMPLnxcvlS9YiRRIN1H1qGovKn45gOw6ey0F+xZLGA+XlBucWLO3rOScUIWtUQ3iUPe03jZOp9DjYGILJcz5UR8vJW0U170U+Yrblc8F4CpMbtz9RmVbEWDjrTDmkW0kOcas7u/qteSbNnpukFHRP+ZkGsz3Nqgdd0GGHx0JzHaDtEzMvyznstk4M1/sQuVxatalPY08fRStAA4t/3E+d18GAD2FBVEvVrqMhwlG3ECifec4GCi4aZfpK/4hTQ70goXoiay2GeJe11Rm3OOu+f7L+aT76lazmtn9VjjOR2Q9PNp/jdg9VMXlINWue4bw9FKlkpm4Z3GGhKZ0zWx6t0newmy/KGYpQaG0K6JnuElBhIapLLqq1tKGl3Ja7dVQT1hgXSCRaBPZG6DZMy61pC/zuWZMqSqac5pi3RIF82t4t7EpthUWfZvo5X5ixzbOsCyxsukdafTyeRRzM8L51omPrfOoFLRVvtmMEkJjELCbZtHVxbqaG0MrVZM1zgg9lYU7FzffubY7Jx60vdr1WYOOZFRSXJPJD4PSHmWHD2GG8CQ12TnuA5r3K0m050x3ydK1bR+55UBTLo/dgz6BNlrpuGESZFZrkNwf/obMdNZhKRHECZG89VX4kVkkK6K3Y6vIMX0zdPkH3iIZsx3oo8bRIjtP4g0sU/ljjt4CYoISsb/IOnksLuiwliWWcOodJc5h4vOIfnBOKDcUonjPCmVegNSwSrk/HDLS/E55K707rP+oAX/BL18LWPuKpEA6eshq4TpgBdTFrzHKlokeaOyD0HiRwnQk983AJp/CFfeF1Gah0Db7kYX62Ludjkce8zUwSi5a+h1h0TcimaD7lsnjYTrNbktvFvhSelFhcMee0kXqnnRlkJ9lVWMZ1/HSP8qhR7Wg8g6j7wsnEoUNvZBpEz+A0Z6g+PHURJcntBD01WSh5DzOX48RII+uFvQsbVxihjuc7Ge3uIkSOOzbjacpesOujNI6SOwi3A5ql93q0Jw1+cjaS9OKN2O46Z8HaS8sVoQlVnnWRlr3vG915ggdXsHq+EfgscaHbPh72dxPL4HAIJfmM+Wx8y7Rqu8Xa4L49eMcY7jvfDtWxmaxtOxY01u+lvqrPUZDP8/NxvHYGv0d4DrpAZSTsODMfRgo/7dKLpUkCRyn8dLez2Ns5M1VUuKbxe1V3o7uUqIJpwfDVMFlufzkIdwrOCXFfHhQZhkdDEjXKT3nrkczW5CMFGS8COQvQIQ+VYLssVqbIhndA2kuvK7arb7Gbk21jzYjY1IZuB3+Qxit6c9LmsTADVSxilOHPWKdI44nZQQyNR0015tMjdaacr68Sq8vxjebzBPWmk8Y/DxXz3B8vV1IxQ8SF+2SvKq6cyccA5SzRNqrIYNSlxV3dvjpncwmC7mJfWa4wEn1/Pglmpw0n/eJNJr3j1O6oNZrF1olFUPqzIefMgDo7W+LKDxgoRZV+Gs1Cox1PoJKbA7l3oSkYRORnUPSwiVG2mLw7GMegFVl6DmobMmDD1KrMRojxGvL7nH/CFpHU2d46TMqiV9KkTMU+O/GlqIJgkx41ND7qK4+nEM9cuiW6tNeuMo75iLAj8AsyBBRCYzP3OEuNwu4n7Wikka1E09mDMYClf0ZMI1EgK54wkKkImrlL1Gc3OO3ta3ZPFQiE7SLy93MjtpnzUJfEk+2IY8z0WHqsVogRl/NzQNkMf2dRiRtPZMYJXsS7CQx3rF2ng6WT8oNDp3h3nbdwHIP+M5V3Sm3T5wTTi/qoVNRVpihV8HGKDkxIxviAi3B5gxiUr6ioejaTm6oNE9fCLc/ZfAzRdNqGXRJTp2cIGQEIFVnpTyyCqowbIGYIUjgs7xlnuiHEhe0Bv3pDx8bsDbQxXzWehU4MC1zIvuSfDn5hnRWMFwKJPz7bOuo7kRkPAkW2kBDJtTVok+s1mIkZ9n4i5O1WZZlbqakDlx08AUvATCv2qcpsGbcWNYPnd6zhSjbCU14kH0JN88ojyok36jBri2KYbrbb7cYnzWNVnV8in9SvKLm7QiiEPCeCZ8T5CrGNoPa1OY28x2ldNpN7m6SLrdc+W62hHgkqkRPFc8fa6Aw6NMtnhZPH4rQkicwy/azinFBzzMNJbcGd5BatVU4wK1gNkt3d8oumyq/BtO8yJROC7ag4jafrhX5OEE8czX2JwXGUL6GUTdTzMFJVhdITbfL57Thasv2AKMjJFTcNzyVLprTR0oQfhhnkPs14u9/H6IHUTnCTOc9ckMgMlNJZUO/FeTlWMGIs8ZOoVOtM0N5pvt5zuD0qNKK5pmr2xbBYNILo5sBs92pWnApui2Ung2LE55W78il/YE0iIdAOlsVz8ygqZGdBnb4Fo6y9pZIT3z0vGq8Lrtst1KWHiOdoIv154NRpf5K1NlsMuFAlb1dxQw53z/21T5RtxzBIb9Gocj9MaR4NvKbtt+behmlpqnBKWlI3OsGUcZe8Bo+r9PDce4zKWuklq2GzcdNnDCbhe+qcjtdAhO2dYghNZAo3+Q5pZ7OQjlJ+IMcqxlSdlsfZyqSCJIyuSBbQn+nTcTRC0Vb6gGLlyb7RyDOh58OAn4fESzP1SgRIZ23dvm9wjJOdkNNU9RxyKPdgl3rLzYT8UI5I5U9blUrES2Dz/f7OZrUDYb1DWxXHKcGZ13F1Lqb7UwCvVA8PFytKyGwumieUseecOUjWIdUlI0LGnG2GjGl3wSwoApOLVqZmUkpFR5wKQGQbXG2cIqLXykUpTql06dNRM1F+P/Omzg6EiiQOs1y8WX10UDM/zISJU30fOsghUmDYFzXpsr3T0S07XbIEXrbRQXcxKcL7sQGvLwh3GY+5PfZt7VnbQBgKp2+xMem27vzgNFHWUMHf12cBcrFj6vTYnTg9EDJi+nta6IfW7WkZA++1u63lCAvEGK21lWJ3AHPq8eGV/T64t6k8PPzH7Ow4NtO7liKaaWSZe6HkslEWMdyWogflgyDedQXxcOHAXo1pn0JgiD0XUhZd7Va+PILkylAFEzyobkgH/tkOEjNoXouhxHVCDx6XclqvXrVCRy/HNsyZa9XhN+dgEuPziQsPurJ52h1vPDUbx6WEmHa+Xt3oBsegeRjkPs6Ke99BMQKfqXqAib6V7ABERWHXx1lUTTuEINaoq3G5neBlKnwRVYPlpmvi9Ryxu4zEbkveiVUg+pZD8PiF3qdpnFmPLD6zB7dFXLfoDgPDQ6fWZkY6mbhrqLgLQYfuuTQxaEBPWIlZh8AjXVfOuxE/X2mVcs/wfLMZJIndPSM+TEmCfPEY7B0tfbTBpREYzN0LFTw4oM1YeL0t9pSuLf6IE6ywzGXgeGpU8XRxowiLKUN7CAjdu7Ah0kh7bKi7zlHsE55ytjYLYiywFSGBgadC42vK35edHRpclXfRU4iFE45CaIztmESMo9YuOqdv7vVcRdR8pJsY0mz2uidLM4z6GU5RtC/gVoQPTNZxLsuIOhlccg4+XdAtgoJ2GRBR5tl7Ll1sxEuQUCZO6r5VxJJxnqHsCUTrX8F7ENrWTCQgAhx0ZNif6kI8Zu2w3eZ9odQycsJOopZIUWPT7Rl3G5VnmEd0vd7vTWVTiqegygPkqpokNKWjB3GqrpPRgxeHy3RCtGeZK1bW0Fvf883lsUMK8dmz1bk28Awh6IcrykuEkxM3LVfYn/qmCiF8mFpMtW7xcK8uqGjqbdpPg9Xvznucfkiaf3j6WH95ds/tJcthweVzN0BZDVOuhzy5QSSxLScz7eYyvJdNDk9JPlbdQIz8ogfP7gTtlp2SV/5lB1WIsaUK43oczl7cgrJfh8RZNpz+iLeGQbWsezsf9gZuOFcHNIa00nXwAmw2QUKDN9lry0DarcEe9OFSJljUE2JfHNJR7jgLvjCnSF4IK7lvk0rlB756hjuYAEOZtZjLtMcxiMZBPuWICT0gHYy2DEE5I7JNytP1ZvJDJUvBjB/C4qxB4eNGxeS5gyIjt8hqrupqBpX/XnHuUW0s0/GbPuKk7VbBr1BUtY0NoYOC6fj5oHvVXtapOc8vMKM/7kenR3pkQiO9JXPUDqgQO+sBQgOzSuXImk91d8mybTmUj2K4QXAwgbkVig4OZrdZ3YQjHY8wcjZlXmhdHnNiUJ1uk7xbBKbMOudIFS5JTr0qWHVVCwouYaqZzlPv7n0T5wjRug2zv0SULMYGqkJtEp6AQoz5hLYt93hoFJKgNrEVt3Q85AI1XO3r3m6LTG/zgTyRnj9E13h4OjZhkyepORG9+UjrLt0pVt2RQYdPPZ4Kl6geuINP1DUlTaMBW7buTD5l06ct2ni9TDohtOw8fCHJ+n7Zy4ZbnydcldoaVzpsrCLmoPlVWXsNDJpgp5/3nF6C9+w8vmhdXwqwNC9lR8x3tDmr/u6oHM8MVcmal5vnB40HeX4K9jtzOEj1vPh9erdUNtmJdMeh3Z21EoZhfvvt7dPbelz+ccL87z4TrgeH/9/OL9+PGusnEFoF0XrevJ7M//qS9eu/1eC/P721QQbkvx++dsWQfBxgrkevn1/7Pvs/HI538/vHtLrqo6n/dpTee8n6bfvtR8rvJ8ffDr7ryq+9NlzPuoHc1wfb1xEwkP0Fefvz/wEzbswbcCAAAA== -->
