"""Fleet — drive the local Mac-mini fleet from the brainstem for ANYTHING.

This is a generic adapter, not just a deployer.  The brainstem can:

  General-purpose
  ---------------
  discover         scan the LAN for brainstems / Macs
  ping             ssh+http reachability check for one host
  authorize        emit the SSH-key paste command + check if already in
  exec             run arbitrary shell on a host (or set of hosts)
  read             fetch a file's contents from a host
  write            write a file's contents onto a host
  ls               directory listing on a host
  tail             last N lines of a file on a host
  ports            list listening TCP ports on a host
  ps               list processes matching a pattern on a host

  Federation / brainstem-aware
  ----------------------------
  brainstem_health    /health on a host's :7071
  chat                POST /chat to any port on any host (twin or brainstem)
  mesh_chat           fan out the same prompt across self + every host's twins
  mesh_exec           fan out the same shell command across hosts
  provision_brainstem ensure brainstem is running on a host
  install_agent       drop an agent .py file into a host's brainstem agents/
  hatch_egg           push a local .egg via HTTP server, hatch on a host
  boot_federation     boot all 4 federation twins on their assigned ports
  status              fleet snapshot (self + every host)

The agent uses SSH (key-auth) to reach minis.  Generate a key via
action='authorize' on first run; that returns the one-line paste the
mini operator runs on their terminal to install your pubkey.

Environment overrides
---------------------
    EGG_SERVER_URL    default http://192.168.86.30:8765
    FLEET_SSH_USER    default rappterone
"""

from __future__ import annotations


# ═══════════════════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — extracted by kody-w/RAR's build_registry.py via AST.
# ═══════════════════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/fleet",
    "version": "1.0.0",
    "display_name": "Fleet",
    "description": (
        "Drive a Mac-mini fleet from the brainstem for anything — discover, "
        "authorize SSH, run arbitrary shell, read/write files, tail logs, "
        "chat any twin on any peer, fan out across the mesh, AND deploy the "
        "federation egg.  Includes escape hatches (custom/extend/cap) so the "
        "brainstem can invent new capabilities when the fixed action set "
        "doesn't cover what the user needs."
    ),
    "author": "Kody Wildfeuer",
    "tags": ["fleet", "ssh", "mesh", "deployment", "federation", "remote", "rapp",
             "self-extending"],
    "category": "devtools",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent", "@kody-w/twin_egg_hatcher"],
}


import ipaddress
import json
import os
import shlex
import socket
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # pragma: no cover
    class BasicAgent:  # type: ignore[no-redef]
        def __init__(self, name=None, metadata=None):
            self.name = name or "BasicAgent"
            self.metadata = metadata or {}


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

EGG_SERVER_URL = os.environ.get("EGG_SERVER_URL", "http://192.168.86.30:8765")
DEFAULT_SSH_USER = os.environ.get("FLEET_SSH_USER", "rappterone")
HATCHER_RAW_URL = (
    "https://raw.githubusercontent.com/kody-w/twin-egg-hatcher/main/"
    "twin_egg_hatcher_agent.py"
)
DEFAULT_EGG_FILE = "aibast-federation.egg"
SSH_OPTS = (
    "-o", "BatchMode=yes",
    "-o", "ConnectTimeout=5",
    "-o", "StrictHostKeyChecking=accept-new",
    "-o", "ServerAliveInterval=10",
    "-o", "ServerAliveCountMax=3",
)
SSH_TIMEOUT = 60

# Federation twins → ports (hash → port).  Used for boot_federation and chat.
FEDERATION_PORTS: Dict[str, int] = {
    "915f54e5-4c71-4de9-bba3-6604461d05e5": 7081,  # heimdall
    "5b8ba4796692197aa4ccde5dfa5beb51":     7082,  # @kody-w
    "eae15721f8ee425b926e4d0b0ac81a17":     7083,  # bots-in-blazers
    "3a159686079c40efb396521e78ef2524":     7084,  # aibast
}


# ---------------------------------------------------------------------------
# Low-level helpers
# ---------------------------------------------------------------------------

def _ssh(user: str, host: str, command: str, timeout: int = SSH_TIMEOUT,
         stdin: Optional[str] = None) -> Dict[str, Any]:
    """Run a remote shell command.  Optional stdin (for `write`-style ops).
    Returns {ok, stdout, stderr, exit, host}."""
    try:
        proc = subprocess.run(
            ["ssh", *SSH_OPTS, f"{user}@{host}", command],
            input=stdin,
            capture_output=True, text=True, timeout=timeout,
        )
        return {
            "ok": proc.returncode == 0,
            "host": host,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
            "exit": proc.returncode,
        }
    except subprocess.TimeoutExpired:
        return {"ok": False, "host": host, "stdout": "", "stderr": f"ssh timeout {timeout}s", "exit": -1}
    except Exception as e:
        return {"ok": False, "host": host, "stdout": "", "stderr": str(e), "exit": -2}


def _ssh_many(user: str, hosts: List[str], command: str,
              timeout: int = SSH_TIMEOUT) -> List[Dict[str, Any]]:
    """Run the same command on a list of hosts in parallel.  Returns ordered list."""
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=min(16, max(1, len(hosts)))) as ex:
        return list(ex.map(lambda h: _ssh(user, h, command, timeout), hosts))


def _http_health(url: str, timeout: float = 2.0) -> Optional[Dict[str, Any]]:
    import urllib.request, urllib.error
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except (urllib.error.URLError, OSError, json.JSONDecodeError, TimeoutError):
        return None


def _http_chat(url: str, message: str, timeout: int = 90) -> Dict[str, Any]:
    import urllib.request, urllib.error
    try:
        req = urllib.request.Request(
            url, method="POST",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"user_input": message}).encode("utf-8"),
        )
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = json.loads(r.read().decode("utf-8"))
            return {"ok": True, "response": body.get("response") or body.get("assistant_response") or ""}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def _probe_tcp(host: str, port: int, timeout: float = 0.3) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        return True
    except (OSError, socket.timeout):
        return False
    finally:
        s.close()


# ---------------------------------------------------------------------------
# SSH key bootstrap
# ---------------------------------------------------------------------------

def _ensure_local_ssh_key() -> Dict[str, Any]:
    key = Path.home() / ".ssh" / "id_ed25519"
    pub = key.with_suffix(".pub")
    if key.exists() and pub.exists():
        return {"generated": False, "pubkey": pub.read_text().strip(),
                "fingerprint": _fingerprint(pub)}
    key.parent.mkdir(parents=True, exist_ok=True)
    label = f"rapp-brainstem@{socket.gethostname()}-{datetime.now(timezone.utc).strftime('%Y%m%d')}"
    subprocess.run(
        ["ssh-keygen", "-t", "ed25519", "-N", "", "-f", str(key), "-C", label, "-q"],
        check=True, timeout=15,
    )
    return {"generated": True, "pubkey": pub.read_text().strip(),
            "fingerprint": _fingerprint(pub)}


def _fingerprint(pub: Path) -> str:
    try:
        out = subprocess.run(
            ["ssh-keygen", "-l", "-f", str(pub)],
            capture_output=True, text=True, timeout=5,
        )
        return out.stdout.strip()
    except Exception:
        return "(unknown)"


# ---------------------------------------------------------------------------
# General actions
# ---------------------------------------------------------------------------

def act_discover(cidr: Optional[str] = None) -> Dict[str, Any]:
    """Scan the LAN /24 for brainstems on :7071."""
    if not cidr:
        for iface in ("en0", "en1", "en6"):
            try:
                ip = subprocess.run(
                    ["ipconfig", "getifaddr", iface],
                    capture_output=True, text=True, timeout=2,
                ).stdout.strip()
                if ip:
                    parts = ip.split(".")
                    cidr = f"{parts[0]}.{parts[1]}.{parts[2]}.0/24"
                    self_ip = ip
                    break
            except Exception:
                continue
    if not cidr:
        return {"ok": False, "error": "could not derive LAN CIDR"}
    net = ipaddress.ip_network(cidr, strict=False)
    candidates = [str(ip) for ip in net.hosts()]
    found: List[Dict[str, Any]] = []
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=64) as ex:
        results = list(ex.map(lambda i: (i, _probe_tcp(i, 7071, 0.25)), candidates))
    for ip, alive in results:
        if not alive:
            continue
        h = _http_health(f"http://{ip}:7071/health", timeout=1.5) or {}
        found.append({"ip": ip, "agents": h.get("agents"),
                      "brainstem_dir": h.get("brainstem_dir"),
                      "version": h.get("version")})
    return {"ok": True, "action": "discover", "cidr": cidr, "found": found}


def act_ping(host: str, ssh_user: str = DEFAULT_SSH_USER) -> Dict[str, Any]:
    info: Dict[str, Any] = {"action": "ping", "host": host}
    try:
        info["resolved"] = socket.gethostbyname(host)
    except Exception:
        info["resolved"] = None
    try:
        out = subprocess.run(["ping", "-c", "1", "-W", "1000", host],
                             capture_output=True, text=True, timeout=4)
        for line in out.stdout.splitlines():
            if "time=" in line:
                info["icmp_ms"] = float(line.split("time=")[1].split()[0])
                break
    except Exception:
        info["icmp_ms"] = None
    info["ssh_ok"] = _ssh(ssh_user, host, "echo ok", timeout=8)["ok"]
    info["brainstem_health"] = _http_health(f"http://{host}:7071/health")
    return {"ok": True, **info}


def act_authorize(host: str, ssh_user: str = DEFAULT_SSH_USER) -> Dict[str, Any]:
    key_info = _ensure_local_ssh_key()
    paste_cmd = (
        f"mkdir -p ~/.ssh && chmod 700 ~/.ssh && "
        f"echo '{key_info['pubkey']}' >> ~/.ssh/authorized_keys && "
        f"chmod 600 ~/.ssh/authorized_keys && echo OK"
    )
    probe = _ssh(ssh_user, host, "echo authorized", timeout=6)
    return {
        "ok": True, "action": "authorize", "host": host,
        "ssh_user": ssh_user,
        "key_generated_this_run": key_info["generated"],
        "fingerprint": key_info["fingerprint"],
        "already_authorized": probe["ok"] and "authorized" in probe["stdout"],
        "paste_on_mini_terminal": paste_cmd,
    }


def act_exec(host: Union[str, List[str]], command: str,
             ssh_user: str = DEFAULT_SSH_USER, timeout: int = SSH_TIMEOUT) -> Dict[str, Any]:
    """Run arbitrary shell on one host or many.  Returns per-host results."""
    hosts = [host] if isinstance(host, str) else host
    results = _ssh_many(ssh_user, hosts, command, timeout=timeout)
    return {"ok": all(r["ok"] for r in results), "action": "exec",
            "command": command, "results": results}


def act_read(host: str, path: str, ssh_user: str = DEFAULT_SSH_USER,
             max_bytes: int = 200000) -> Dict[str, Any]:
    r = _ssh(ssh_user, host, f"head -c {max_bytes} {shlex.quote(path)}", timeout=15)
    return {"ok": r["ok"], "action": "read", "host": host, "path": path,
            "content": r["stdout"], "stderr": r["stderr"]}


def act_write(host: str, path: str, content: str,
              ssh_user: str = DEFAULT_SSH_USER) -> Dict[str, Any]:
    cmd = f"mkdir -p $(dirname {shlex.quote(path)}) && cat > {shlex.quote(path)}"
    r = _ssh(ssh_user, host, cmd, timeout=20, stdin=content)
    return {"ok": r["ok"], "action": "write", "host": host, "path": path,
            "bytes_written": len(content), "stderr": r["stderr"]}


def act_ls(host: str, path: str, ssh_user: str = DEFAULT_SSH_USER) -> Dict[str, Any]:
    r = _ssh(ssh_user, host, f"ls -la {shlex.quote(path)}", timeout=10)
    return {"ok": r["ok"], "action": "ls", "host": host, "path": path,
            "listing": r["stdout"], "stderr": r["stderr"]}


def act_tail(host: str, path: str, lines: int = 50,
             ssh_user: str = DEFAULT_SSH_USER) -> Dict[str, Any]:
    r = _ssh(ssh_user, host, f"tail -n {lines} {shlex.quote(path)}", timeout=10)
    return {"ok": r["ok"], "action": "tail", "host": host, "path": path,
            "lines": r["stdout"], "stderr": r["stderr"]}


def act_ports(host: str, ssh_user: str = DEFAULT_SSH_USER) -> Dict[str, Any]:
    r = _ssh(ssh_user, host, "lsof -nP -iTCP -sTCP:LISTEN 2>/dev/null | awk 'NR>1 {print $9}' | sort -u",
             timeout=15)
    return {"ok": r["ok"], "action": "ports", "host": host,
            "listening": [l.strip() for l in r["stdout"].splitlines() if l.strip()],
            "stderr": r["stderr"]}


def act_ps(host: str, pattern: str = "", ssh_user: str = DEFAULT_SSH_USER) -> Dict[str, Any]:
    if pattern:
        cmd = f"ps -axo pid,user,comm,args | grep -E {shlex.quote(pattern)} | grep -v grep | head -50"
    else:
        cmd = "ps -axo pid,user,comm,args | head -30"
    r = _ssh(ssh_user, host, cmd, timeout=10)
    return {"ok": r["ok"], "action": "ps", "host": host, "pattern": pattern,
            "output": r["stdout"]}


# ---------------------------------------------------------------------------
# Brainstem-aware actions
# ---------------------------------------------------------------------------

def act_brainstem_health(host: str) -> Dict[str, Any]:
    h = _http_health(f"http://{host}:7071/health")
    return {"ok": h is not None, "action": "brainstem_health", "host": host, "health": h}


def act_chat(host: str, port: int, message: str, timeout: int = 90) -> Dict[str, Any]:
    """Send a /chat to any port on any host (twin or brainstem)."""
    r = _http_chat(f"http://{host}:{port}/chat", message, timeout=timeout)
    return {"ok": r["ok"], "action": "chat", "host": host, "port": port,
            "response": r.get("response"), "error": r.get("error")}


def act_mesh_chat(message: str, hosts: List[str],
                  include_self: bool = True,
                  ports: Optional[List[int]] = None,
                  timeout: int = 90) -> Dict[str, Any]:
    """Fan out the same prompt across self + every host's twin ports."""
    ports = ports or list(FEDERATION_PORTS.values())
    targets: List[Dict[str, Any]] = []
    if include_self:
        for p in ports:
            targets.append({"host": "127.0.0.1", "port": p, "label": "self"})
    for h in hosts:
        for p in ports:
            targets.append({"host": h, "port": p, "label": "peer"})
    out = []
    for t in targets:
        r = _http_chat(f"http://{t['host']}:{t['port']}/chat", message, timeout=timeout)
        out.append({**t, **r})
    return {"ok": True, "action": "mesh_chat", "message": message, "targets": len(out),
            "results": out}


def act_mesh_exec(command: str, hosts: List[str],
                  ssh_user: str = DEFAULT_SSH_USER, timeout: int = SSH_TIMEOUT) -> Dict[str, Any]:
    results = _ssh_many(ssh_user, hosts, command, timeout=timeout)
    return {"ok": all(r["ok"] for r in results), "action": "mesh_exec",
            "command": command, "results": results}


def act_provision_brainstem(host: str, ssh_user: str = DEFAULT_SSH_USER) -> Dict[str, Any]:
    """Make sure the mini's brainstem is up.  Doesn't install anything else."""
    # No `set -e` — partial info on failure is useful.
    script = r'''
if curl -s -m 1 http://localhost:7071/health 2>/dev/null | grep -q '"status".*"ok"'; then
  echo "STATE=already-running"
elif [ -f "$HOME/.brainstem/src/rapp_brainstem/start.sh" ]; then
  pkill -f "rapp_brainstem.*start" 2>/dev/null
  sleep 1
  cd "$HOME/.brainstem/src/rapp_brainstem"
  nohup bash start.sh > /tmp/brainstem.log 2>&1 &
  disown
  for i in $(seq 1 30); do
    sleep 1
    if curl -s -m 1 http://localhost:7071/health 2>/dev/null | grep -q '"status".*"ok"'; then
      echo "STATE=started"
      break
    fi
  done
  if ! curl -s -m 1 http://localhost:7071/health 2>/dev/null | grep -q '"status".*"ok"'; then
    echo "STATE=failed"
    echo "LOG_TAIL=$(tail -30 /tmp/brainstem.log 2>&1)"
  fi
else
  echo "STATE=not-installed"
fi
echo "HEALTH=$(curl -s -m 2 http://localhost:7071/health)"
'''.strip()
    r = _ssh(ssh_user, host, script, timeout=90)
    return {"ok": r["ok"] and "STATE=already-running" in r["stdout"] or "STATE=started" in r["stdout"],
            "action": "provision_brainstem", "host": host, "raw": r["stdout"][-1500:]}


def act_install_agent(host: str, agent_filename: str, agent_url: Optional[str] = None,
                      agent_content: Optional[str] = None,
                      ssh_user: str = DEFAULT_SSH_USER) -> Dict[str, Any]:
    """Drop an *_agent.py into the host's brainstem agents/ folder.
    Either pass agent_url (will curl it on the host) or agent_content (sent over stdin)."""
    dst = f"$HOME/.brainstem/src/rapp_brainstem/agents/{shlex.quote(agent_filename)}"
    if agent_url:
        cmd = f"mkdir -p $(dirname {dst}) && curl -fsSL {shlex.quote(agent_url)} -o {dst} && echo OK"
        r = _ssh(ssh_user, host, cmd, timeout=30)
    elif agent_content:
        cmd = f"mkdir -p $(dirname {dst}) && cat > {dst} && echo OK"
        r = _ssh(ssh_user, host, cmd, timeout=20, stdin=agent_content)
    else:
        return {"ok": False, "action": "install_agent", "error": "agent_url OR agent_content required"}
    return {"ok": r["ok"] and "OK" in r["stdout"], "action": "install_agent",
            "host": host, "filename": agent_filename}


def act_hatch_egg(host: str, egg_file: str = DEFAULT_EGG_FILE,
                  egg_url: Optional[str] = None,
                  ssh_user: str = DEFAULT_SSH_USER) -> Dict[str, Any]:
    egg_url = egg_url or f"{EGG_SERVER_URL}/{egg_file}"
    # Make sure hatcher is installed first
    inst = act_install_agent(host, "twin_egg_hatcher_agent.py", agent_url=HATCHER_RAW_URL,
                             ssh_user=ssh_user)
    cmd = (
        "mkdir -p /tmp/aibast-hatch && cd /tmp/aibast-hatch && "
        f"curl -fsSL {shlex.quote(egg_url)} -o egg.egg && "
        "python3 $HOME/.brainstem/src/rapp_brainstem/agents/twin_egg_hatcher_agent.py "
        "hatch --egg ./egg.egg"
    )
    r = _ssh(ssh_user, host, cmd, timeout=180)
    parsed = None
    try:
        i, j = r["stdout"].find("{"), r["stdout"].rfind("}")
        if i != -1 and j > i:
            parsed = json.loads(r["stdout"][i:j + 1])
    except Exception:
        pass
    return {"ok": r["ok"], "action": "hatch_egg", "host": host, "egg_url": egg_url,
            "hatcher_install": inst, "hatch_result": parsed,
            "raw_tail": r["stdout"][-1500:] if not parsed else "(see hatch_result)"}


def act_boot_federation(host: str, ssh_user: str = DEFAULT_SSH_USER) -> Dict[str, Any]:
    """Boot all 4 federation twins on the host with their assigned ports."""
    parts = []
    for h, port in FEDERATION_PORTS.items():
        parts.append(
            f'(ws=$HOME/.rapp/twins/{h}; '
            f'mkdir -p $HOME/.rapp/pids $HOME/.rapp/ports; '
            f'echo {port} > $HOME/.rapp/ports/{h}.port; '
            f'SOUL_PATH=$ws/soul.md AGENTS_PATH=$ws/agents PORT={port} '
            f'nohup bash $HOME/.brainstem/src/rapp_brainstem/start.sh '
            f'> /tmp/twin-{h}.log 2>&1 & disown; '
            f'echo $! > $HOME/.rapp/pids/{h}.pid; '
            f'echo BOOTED {h} {port})'
        )
    wait = ("for p in " + " ".join(str(p) for p in FEDERATION_PORTS.values()) + "; do "
            "for i in $(seq 1 30); do "
            'if curl -s -m 1 http://localhost:$p/health 2>/dev/null | grep -q \'"status".*"ok"\'; '
            "then echo READY $p; break; fi; sleep 1; done; done")
    r = _ssh(ssh_user, host, "; ".join(parts) + "; " + wait, timeout=180)
    return {
        "ok": r["ok"] and r["stdout"].count("READY ") >= 4,
        "action": "boot_federation", "host": host,
        "booted_lines": [l for l in r["stdout"].splitlines() if l.startswith("BOOTED ")],
        "ready_lines": [l for l in r["stdout"].splitlines() if l.startswith("READY ")],
    }


def act_status(hosts: Optional[List[str]] = None) -> Dict[str, Any]:
    hosts = hosts or []
    out: Dict[str, Any] = {"self": _snapshot("127.0.0.1")}
    out["peers"] = {h: _snapshot(h) for h in hosts}
    return {"ok": True, "action": "status", "snapshot": out}


def _snapshot(host: str) -> Dict[str, Any]:
    return {
        "host": host,
        "brainstem": _http_health(f"http://{host}:7071/health"),
        "twins": {p: _http_health(f"http://{host}:{p}/health")
                  for p in FEDERATION_PORTS.values()},
    }


# ---------------------------------------------------------------------------
# Escape hatches — let the brainstem invent new capabilities when the
# fixed action set doesn't cover what the user asked for.
# ---------------------------------------------------------------------------
#
# The brainstem is single-user, single-machine, and trusted (agents drop
# Python into ~/.brainstem/agents/ already).  These actions deliberately
# expose Python execution against the fleet helpers so the LLM can compose
# new behavior on the fly.

_FLEET_CAPS_DIR = Path.home() / ".brainstem" / "src" / "rapp_brainstem" / "agents" / "fleet_capabilities"


def _fleet_ctx() -> Dict[str, Any]:
    """The names a custom snippet (or generated capability) can call."""
    return {
        # SSH
        "ssh":        _ssh,
        "ssh_many":   _ssh_many,
        # HTTP
        "http_health":  _http_health,
        "http_chat":    _http_chat,
        "probe_tcp":    _probe_tcp,
        # constants
        "EGG_SERVER_URL":   EGG_SERVER_URL,
        "DEFAULT_SSH_USER": DEFAULT_SSH_USER,
        "FEDERATION_PORTS": FEDERATION_PORTS,
        "HATCHER_RAW_URL":  HATCHER_RAW_URL,
        # stdlib re-exports for convenience
        "json": json, "os": os, "subprocess": subprocess,
        "Path": Path, "shlex": shlex, "datetime": datetime, "timezone": timezone,
    }


def act_custom(code: str, args: Optional[Dict[str, Any]] = None,
               name: str = "custom") -> Dict[str, Any]:
    """Execute a Python snippet against the fleet helpers.  The snippet must
    define a function `run(ctx, args)` (or set a `result` variable).  Returns
    whatever `run` returns (must be JSON-serializable) or the value of
    `result`.

    Example snippet:
        def run(ctx, args):
            r = ctx['ssh']('rappterone', args['host'], 'sw_vers')
            return {'sw_vers': r['stdout']}

    Trust model: this is local, single-user, same as drop-in agents.  Use
    when the fixed action list doesn't cover what the brainstem needs.
    """
    ctx = _fleet_ctx()
    args = args or {}
    g: Dict[str, Any] = {"ctx": ctx, "args": args, "result": None}
    try:
        exec(compile(code, f"<fleet.custom:{name}>", "exec"), g, g)
        if callable(g.get("run")):
            out = g["run"](ctx, args)
        else:
            out = g.get("result")
        return {"ok": True, "action": "custom", "name": name, "result": out}
    except Exception as e:
        return {"ok": False, "action": "custom", "name": name,
                "error": f"{type(e).__name__}: {e}"}


def act_extend(capability_name: str, python_source: str,
               overwrite: bool = False) -> Dict[str, Any]:
    """Persist a new capability the brainstem invented.  Writes a sidecar
    file under .../agents/fleet_capabilities/<capability_name>.py.  After
    this call, you can invoke the capability via action='custom' with
    `code=open(path).read()`, OR with action='cap', name='<capability_name>'.

    The source MUST define `def run(ctx, args): ...`.  Anything that needs
    SSH, HTTP, federation primitives is accessible via the `ctx` dict.
    """
    if not capability_name.isidentifier():
        return {"ok": False, "action": "extend",
                "error": f"capability_name must be a Python identifier, got {capability_name!r}"}
    if "def run(" not in python_source:
        return {"ok": False, "action": "extend",
                "error": "python_source must define `def run(ctx, args): ...`"}
    _FLEET_CAPS_DIR.mkdir(parents=True, exist_ok=True)
    target = _FLEET_CAPS_DIR / f"{capability_name}.py"
    if target.exists() and not overwrite:
        return {"ok": False, "action": "extend", "error": f"already exists: {target}",
                "hint": "pass overwrite=true to replace"}
    target.write_text(python_source, encoding="utf-8")
    return {
        "ok": True, "action": "extend", "name": capability_name,
        "path": str(target),
        "invoke_via": [
            f"Fleet(action='cap', name='{capability_name}', args={{...}})",
            f"or read the file and use action='custom' with its source.",
        ],
    }


def act_cap(name: str, args: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Invoke a previously-saved capability by name."""
    target = _FLEET_CAPS_DIR / f"{name}.py"
    if not target.exists():
        avail = sorted(p.stem for p in _FLEET_CAPS_DIR.glob("*.py")) if _FLEET_CAPS_DIR.exists() else []
        return {"ok": False, "action": "cap", "error": f"no such capability: {name}",
                "available": avail}
    return act_custom(target.read_text(encoding="utf-8"), args=args, name=name)


def act_list_caps() -> Dict[str, Any]:
    if not _FLEET_CAPS_DIR.exists():
        return {"ok": True, "action": "list_caps", "caps": [], "dir": str(_FLEET_CAPS_DIR)}
    caps = []
    for p in sorted(_FLEET_CAPS_DIR.glob("*.py")):
        src = p.read_text(encoding="utf-8", errors="replace")
        # Grab the docstring of `run` if present
        doc = ""
        try:
            import ast
            tree = ast.parse(src)
            for node in tree.body:
                if isinstance(node, ast.FunctionDef) and node.name == "run":
                    doc = (ast.get_docstring(node) or "").strip().splitlines()[0] if ast.get_docstring(node) else ""
                    break
        except Exception:
            pass
        caps.append({"name": p.stem, "path": str(p), "bytes": p.stat().st_size, "summary": doc[:200]})
    return {"ok": True, "action": "list_caps", "caps": caps, "dir": str(_FLEET_CAPS_DIR)}


# ---------------------------------------------------------------------------
# Dispatcher / agent
# ---------------------------------------------------------------------------

class FleetAgent(BasicAgent):
    """Generic fleet controller — drive the local Mac-mini fleet for ANYTHING.

    Not just deployment: arbitrary shell, file IO, tail logs, list ports, chat
    any twin on any host, fan out across the mesh.  The deployment helpers
    (provision_brainstem / hatch_egg / boot_federation) are convenience flows
    built on top of the same `exec` / `write` primitives.
    """

    def __init__(self) -> None:
        self.name = "Fleet"
        self.metadata = {
            "name": self.name,
            "description": (
                "Drive the local Mac-mini fleet over SSH for anything — run shell, "
                "read/write files, tail logs, list processes/ports, chat any twin "
                "on any peer, fan out across the mesh, AND deploy the federation. "
                "Default SSH user is 'rappterone'; configure with FLEET_SSH_USER env. "
                "Authorize SSH first with action='authorize', host=<mini>."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": [
                            "discover", "ping", "authorize",
                            "exec", "read", "write", "ls", "tail", "ports", "ps",
                            "brainstem_health", "chat", "mesh_chat", "mesh_exec",
                            "provision_brainstem", "install_agent",
                            "hatch_egg", "boot_federation", "status",
                            "custom", "extend", "cap", "list_caps",
                        ],
                        "description": (
                            "What to do.  Defaults to 'status'.  "
                            "Use 'custom' when the fixed action set doesn't cover what's needed — "
                            "pass `code` containing `def run(ctx, args): ...` to operate on the fleet helpers. "
                            "Use 'extend' to persist a new named capability (then invoke with 'cap')."
                        ),
                    },
                    "code":   {"type": "string", "description": "For action='custom' — Python snippet defining `def run(ctx, args)` over fleet helpers (ctx has ssh, http_chat, http_health, probe_tcp, etc.)."},
                    "args":   {"type": "object", "description": "For action='custom' or 'cap' — JSON args passed to run(ctx, args)."},
                    "name":   {"type": "string", "description": "For action='extend' or 'cap' — capability identifier."},
                    "python_source": {"type": "string", "description": "For action='extend' — the Python source to save as a new capability."},
                    "overwrite": {"type": "boolean", "description": "For action='extend' — replace an existing capability of the same name."},
                    "host":     {"type": "string",  "description": "Single hostname or IP."},
                    "hosts":    {"type": "array",   "items": {"type": "string"},
                                 "description": "Multiple hostnames (for mesh / status / mesh_exec)."},
                    "ssh_user": {"type": "string",  "description": "SSH username (default rappterone)."},
                    "command":  {"type": "string",  "description": "For exec / mesh_exec."},
                    "path":     {"type": "string",  "description": "For read / write / ls / tail."},
                    "content":  {"type": "string",  "description": "For write (file body)."},
                    "lines":    {"type": "integer", "description": "For tail (default 50)."},
                    "pattern":  {"type": "string",  "description": "For ps (regex grep filter)."},
                    "port":     {"type": "integer", "description": "For chat (target twin port)."},
                    "ports":    {"type": "array",   "items": {"type": "integer"},
                                 "description": "For mesh_chat (default: federation ports 7081-7084)."},
                    "message":  {"type": "string",  "description": "For chat / mesh_chat."},
                    "agent_filename": {"type": "string", "description": "For install_agent."},
                    "agent_url":      {"type": "string", "description": "For install_agent (curl source)."},
                    "agent_content":  {"type": "string", "description": "For install_agent (inline body)."},
                    "egg_file": {"type": "string", "description": "For hatch_egg (filename in egg server)."},
                    "egg_url":  {"type": "string", "description": "For hatch_egg (override full URL)."},
                    "cidr":     {"type": "string", "description": "For discover (override /24)."},
                    "include_self": {"type": "boolean", "description": "For mesh_chat (default true)."},
                    "timeout":  {"type": "integer", "description": "SSH / HTTP timeout seconds."},
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kw: Any) -> str:
        action = (kw.get("action") or "status").lower()
        user = kw.get("ssh_user") or DEFAULT_SSH_USER
        timeout = int(kw.get("timeout") or SSH_TIMEOUT)
        try:
            if action == "discover":
                result = act_discover(cidr=kw.get("cidr"))
            elif action == "ping":
                result = act_ping(kw["host"], ssh_user=user)
            elif action == "authorize":
                result = act_authorize(kw["host"], ssh_user=user)
            elif action == "exec":
                hosts = kw.get("hosts") or kw["host"]
                result = act_exec(hosts, kw["command"], ssh_user=user, timeout=timeout)
            elif action == "read":
                result = act_read(kw["host"], kw["path"], ssh_user=user)
            elif action == "write":
                result = act_write(kw["host"], kw["path"], kw["content"], ssh_user=user)
            elif action == "ls":
                result = act_ls(kw["host"], kw["path"], ssh_user=user)
            elif action == "tail":
                result = act_tail(kw["host"], kw["path"], int(kw.get("lines") or 50), ssh_user=user)
            elif action == "ports":
                result = act_ports(kw["host"], ssh_user=user)
            elif action == "ps":
                result = act_ps(kw["host"], kw.get("pattern") or "", ssh_user=user)
            elif action == "brainstem_health":
                result = act_brainstem_health(kw["host"])
            elif action == "chat":
                result = act_chat(kw["host"], int(kw["port"]), kw["message"],
                                  timeout=timeout)
            elif action == "mesh_chat":
                result = act_mesh_chat(kw["message"], hosts=kw.get("hosts") or [],
                                       include_self=kw.get("include_self", True),
                                       ports=kw.get("ports"), timeout=timeout)
            elif action == "mesh_exec":
                result = act_mesh_exec(kw["command"], hosts=kw.get("hosts") or [],
                                       ssh_user=user, timeout=timeout)
            elif action == "provision_brainstem":
                result = act_provision_brainstem(kw["host"], ssh_user=user)
            elif action == "install_agent":
                result = act_install_agent(kw["host"], kw["agent_filename"],
                                           agent_url=kw.get("agent_url"),
                                           agent_content=kw.get("agent_content"),
                                           ssh_user=user)
            elif action == "hatch_egg":
                result = act_hatch_egg(kw["host"],
                                       egg_file=kw.get("egg_file") or DEFAULT_EGG_FILE,
                                       egg_url=kw.get("egg_url"),
                                       ssh_user=user)
            elif action == "boot_federation":
                result = act_boot_federation(kw["host"], ssh_user=user)
            elif action == "status":
                result = act_status(hosts=kw.get("hosts") or
                                          ([kw["host"]] if kw.get("host") else []))
            elif action == "custom":
                result = act_custom(kw["code"], args=kw.get("args") or {},
                                    name=kw.get("name") or "custom")
            elif action == "extend":
                result = act_extend(kw["name"], kw["python_source"],
                                    overwrite=bool(kw.get("overwrite", False)))
            elif action == "cap":
                result = act_cap(kw["name"], args=kw.get("args") or {})
            elif action == "list_caps":
                result = act_list_caps()
            else:
                result = {"ok": False, "error": f"unknown action: {action}"}
        except KeyError as e:
            result = {"ok": False, "action": action, "error": f"missing required arg: {e}"}
        except Exception as e:
            result = {"ok": False, "action": action, "error": str(e)}
        return json.dumps(result, indent=2, default=str)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _cli(argv: List[str]) -> int:
    a = FleetAgent()
    if not argv:
        print(a.perform(action="status"))
        return 0
    kw: Dict[str, Any] = {"action": argv[0]}
    i = 1
    while i < len(argv):
        k = argv[i].lstrip("-")
        if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
            v = argv[i + 1]
            if k in ("hosts", "ports") and "," in v:
                v = v.split(",")
            kw[k] = v
            i += 2
        else:
            kw[k] = True
            i += 1
    print(a.perform(**kw))
    return 0


if __name__ == "__main__":
    sys.exit(_cli(sys.argv[1:]))
