"""
rcon_agent.py — the rCon expansion-pack cartridge.

Drops every rCon-specific capability into the brainstem in ONE file:

    Twin, TwinEggHatcher, Fleet, NeighborhoodSnapshot, NeighborhoodRun,
    SelfHealingCron, LearnNew, RARRemoteAgent

Drag this file into the brainstem's agents/ and the locked console
lights up with twins, neighborhood snapshots, the RAR marketplace,
cron-based self-healing, and the "learn a new agent from chat"
pattern. Drag it back out and only the kernel set (basic_agent,
manage_memory, context_memory, hacker_news) remains.

Why one file: the brainstem's loader (per CONSTITUTION §0) treats
every .py in agents/ as a single cartridge slot. Consolidating
means the user installs/uninstalls the entire rCon experience by
moving one file. No partial-load surprises, no version skew across
components.

Per CONSTITUTION §0 / §1: this file is a *bundled cartridge*, not
kernel code. brainstem.py + soul.md + the kernel agent set stay
sacred; this file is what makes the box useful.
"""

from __future__ import annotations
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
import re
from datetime import datetime
import io
import shutil
import tarfile
import tempfile
import time
import zipfile
from agents.basic_agent import BasicAgent
import base64
from urllib import request as _urlreq
import logging
import urllib.request
import urllib.error
from urllib import error as _urlerr
import hashlib
import pathlib
import signal
import urllib.parse
import uuid
import argparse
from typing import Any, Dict, List, Optional, Tuple


# ─────────────────────────────────────────────────────────────────────
# Section: fleet_agent.py
# ─────────────────────────────────────────────────────────────────────
try:
    from agents.basic_agent import BasicAgent
except ImportError:

    class BasicAgent:

        def __init__(self, name=None, metadata=None):
            self.name = name or 'BasicAgent'
            self.metadata = metadata or {}

EGG_SERVER_URL = os.environ.get('EGG_SERVER_URL', 'http://192.168.86.30:8765')

DEFAULT_SSH_USER = os.environ.get('FLEET_SSH_USER', 'rappterone')

HATCHER_RAW_URL = 'https://raw.githubusercontent.com/kody-w/twin-egg-hatcher/main/twin_egg_hatcher_agent.py'

DEFAULT_EGG_FILE = 'aibast-federation.egg'

SSH_OPTS = ('-o', 'BatchMode=yes', '-o', 'ConnectTimeout=5', '-o', 'StrictHostKeyChecking=accept-new', '-o', 'ServerAliveInterval=10', '-o', 'ServerAliveCountMax=3')

SSH_TIMEOUT = 60

FEDERATION_PORTS: Dict[str, int] = {'915f54e5-4c71-4de9-bba3-6604461d05e5': 7081, '5b8ba4796692197aa4ccde5dfa5beb51': 7082, 'eae15721f8ee425b926e4d0b0ac81a17': 7083, '3a159686079c40efb396521e78ef2524': 7084}

def _ssh(user: str, host: str, command: str, timeout: int=SSH_TIMEOUT, stdin: Optional[str]=None) -> Dict[str, Any]:
    """Run a remote shell command.  Optional stdin (for `write`-style ops).
    Returns {ok, stdout, stderr, exit, host}."""
    try:
        proc = subprocess.run(['ssh', *SSH_OPTS, f'{user}@{host}', command], input=stdin, capture_output=True, text=True, timeout=timeout)
        return {'ok': proc.returncode == 0, 'host': host, 'stdout': proc.stdout, 'stderr': proc.stderr, 'exit': proc.returncode}
    except subprocess.TimeoutExpired:
        return {'ok': False, 'host': host, 'stdout': '', 'stderr': f'ssh timeout {timeout}s', 'exit': -1}
    except Exception as e:
        return {'ok': False, 'host': host, 'stdout': '', 'stderr': str(e), 'exit': -2}

def _ssh_many(user: str, hosts: List[str], command: str, timeout: int=SSH_TIMEOUT) -> List[Dict[str, Any]]:
    """Run the same command on a list of hosts in parallel.  Returns ordered list."""
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=min(16, max(1, len(hosts)))) as ex:
        return list(ex.map(lambda h: _ssh(user, h, command, timeout), hosts))

def _http_health(url: str, timeout: float=2.0) -> Optional[Dict[str, Any]]:
    import urllib.request, urllib.error
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return json.loads(r.read().decode('utf-8'))
    except (urllib.error.URLError, OSError, json.JSONDecodeError, TimeoutError):
        return None

def _http_chat(url: str, message: str, timeout: int=90) -> Dict[str, Any]:
    import urllib.request, urllib.error
    try:
        req = urllib.request.Request(url, method='POST', headers={'Content-Type': 'application/json'}, data=json.dumps({'user_input': message}).encode('utf-8'))
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = json.loads(r.read().decode('utf-8'))
            return {'ok': True, 'response': body.get('response') or body.get('assistant_response') or ''}
    except Exception as e:
        return {'ok': False, 'error': str(e)}

def _probe_tcp(host: str, port: int, timeout: float=0.3) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        return True
    except (OSError, socket.timeout):
        return False
    finally:
        s.close()

def _ensure_local_ssh_key() -> Dict[str, Any]:
    key = Path.home() / '.ssh' / 'id_ed25519'
    pub = key.with_suffix('.pub')
    if key.exists() and pub.exists():
        return {'generated': False, 'pubkey': pub.read_text().strip(), 'fingerprint': _fingerprint(pub)}
    key.parent.mkdir(parents=True, exist_ok=True)
    label = f"rapp-brainstem@{socket.gethostname()}-{datetime.now(timezone.utc).strftime('%Y%m%d')}"
    subprocess.run(['ssh-keygen', '-t', 'ed25519', '-N', '', '-f', str(key), '-C', label, '-q'], check=True, timeout=15)
    return {'generated': True, 'pubkey': pub.read_text().strip(), 'fingerprint': _fingerprint(pub)}

def _fingerprint(pub: Path) -> str:
    try:
        out = subprocess.run(['ssh-keygen', '-l', '-f', str(pub)], capture_output=True, text=True, timeout=5)
        return out.stdout.strip()
    except Exception:
        return '(unknown)'

def act_discover(cidr: Optional[str]=None) -> Dict[str, Any]:
    """Scan the LAN /24 for brainstems on :7071."""
    if not cidr:
        for iface in ('en0', 'en1', 'en6'):
            try:
                ip = subprocess.run(['ipconfig', 'getifaddr', iface], capture_output=True, text=True, timeout=2).stdout.strip()
                if ip:
                    parts = ip.split('.')
                    cidr = f'{parts[0]}.{parts[1]}.{parts[2]}.0/24'
                    self_ip = ip
                    break
            except Exception:
                continue
    if not cidr:
        return {'ok': False, 'error': 'could not derive LAN CIDR'}
    net = ipaddress.ip_network(cidr, strict=False)
    candidates = [str(ip) for ip in net.hosts()]
    found: List[Dict[str, Any]] = []
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=64) as ex:
        results = list(ex.map(lambda i: (i, _probe_tcp(i, 7071, 0.25)), candidates))
    for ip, alive in results:
        if not alive:
            continue
        h = _http_health(f'http://{ip}:7071/health', timeout=1.5) or {}
        found.append({'ip': ip, 'agents': h.get('agents'), 'brainstem_dir': h.get('brainstem_dir'), 'version': h.get('version')})
    return {'ok': True, 'action': 'discover', 'cidr': cidr, 'found': found}

def act_ping(host: str, ssh_user: str=DEFAULT_SSH_USER) -> Dict[str, Any]:
    info: Dict[str, Any] = {'action': 'ping', 'host': host}
    try:
        info['resolved'] = socket.gethostbyname(host)
    except Exception:
        info['resolved'] = None
    try:
        out = subprocess.run(['ping', '-c', '1', '-W', '1000', host], capture_output=True, text=True, timeout=4)
        for line in out.stdout.splitlines():
            if 'time=' in line:
                info['icmp_ms'] = float(line.split('time=')[1].split()[0])
                break
    except Exception:
        info['icmp_ms'] = None
    info['ssh_ok'] = _ssh(ssh_user, host, 'echo ok', timeout=8)['ok']
    info['brainstem_health'] = _http_health(f'http://{host}:7071/health')
    return {'ok': True, **info}

def act_authorize(host: str, ssh_user: str=DEFAULT_SSH_USER) -> Dict[str, Any]:
    key_info = _ensure_local_ssh_key()
    paste_cmd = f"mkdir -p ~/.ssh && chmod 700 ~/.ssh && echo '{key_info['pubkey']}' >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys && echo OK"
    probe = _ssh(ssh_user, host, 'echo authorized', timeout=6)
    return {'ok': True, 'action': 'authorize', 'host': host, 'ssh_user': ssh_user, 'key_generated_this_run': key_info['generated'], 'fingerprint': key_info['fingerprint'], 'already_authorized': probe['ok'] and 'authorized' in probe['stdout'], 'paste_on_mini_terminal': paste_cmd}

def act_exec(host: Union[str, List[str]], command: str, ssh_user: str=DEFAULT_SSH_USER, timeout: int=SSH_TIMEOUT) -> Dict[str, Any]:
    """Run arbitrary shell on one host or many.  Returns per-host results."""
    hosts = [host] if isinstance(host, str) else host
    results = _ssh_many(ssh_user, hosts, command, timeout=timeout)
    return {'ok': all((r['ok'] for r in results)), 'action': 'exec', 'command': command, 'results': results}

def act_read(host: str, path: str, ssh_user: str=DEFAULT_SSH_USER, max_bytes: int=200000) -> Dict[str, Any]:
    r = _ssh(ssh_user, host, f'head -c {max_bytes} {shlex.quote(path)}', timeout=15)
    return {'ok': r['ok'], 'action': 'read', 'host': host, 'path': path, 'content': r['stdout'], 'stderr': r['stderr']}

def act_write(host: str, path: str, content: str, ssh_user: str=DEFAULT_SSH_USER) -> Dict[str, Any]:
    cmd = f'mkdir -p $(dirname {shlex.quote(path)}) && cat > {shlex.quote(path)}'
    r = _ssh(ssh_user, host, cmd, timeout=20, stdin=content)
    return {'ok': r['ok'], 'action': 'write', 'host': host, 'path': path, 'bytes_written': len(content), 'stderr': r['stderr']}

def act_ls(host: str, path: str, ssh_user: str=DEFAULT_SSH_USER) -> Dict[str, Any]:
    r = _ssh(ssh_user, host, f'ls -la {shlex.quote(path)}', timeout=10)
    return {'ok': r['ok'], 'action': 'ls', 'host': host, 'path': path, 'listing': r['stdout'], 'stderr': r['stderr']}

def act_tail(host: str, path: str, lines: int=50, ssh_user: str=DEFAULT_SSH_USER) -> Dict[str, Any]:
    r = _ssh(ssh_user, host, f'tail -n {lines} {shlex.quote(path)}', timeout=10)
    return {'ok': r['ok'], 'action': 'tail', 'host': host, 'path': path, 'lines': r['stdout'], 'stderr': r['stderr']}

def act_ports(host: str, ssh_user: str=DEFAULT_SSH_USER) -> Dict[str, Any]:
    r = _ssh(ssh_user, host, "lsof -nP -iTCP -sTCP:LISTEN 2>/dev/null | awk 'NR>1 {print $9}' | sort -u", timeout=15)
    return {'ok': r['ok'], 'action': 'ports', 'host': host, 'listening': [l.strip() for l in r['stdout'].splitlines() if l.strip()], 'stderr': r['stderr']}

def act_ps(host: str, pattern: str='', ssh_user: str=DEFAULT_SSH_USER) -> Dict[str, Any]:
    if pattern:
        cmd = f'ps -axo pid,user,comm,args | grep -E {shlex.quote(pattern)} | grep -v grep | head -50'
    else:
        cmd = 'ps -axo pid,user,comm,args | head -30'
    r = _ssh(ssh_user, host, cmd, timeout=10)
    return {'ok': r['ok'], 'action': 'ps', 'host': host, 'pattern': pattern, 'output': r['stdout']}

def act_brainstem_health(host: str) -> Dict[str, Any]:
    h = _http_health(f'http://{host}:7071/health')
    return {'ok': h is not None, 'action': 'brainstem_health', 'host': host, 'health': h}

def act_chat(host: str, port: int, message: str, timeout: int=90) -> Dict[str, Any]:
    """Send a /chat to any port on any host (twin or brainstem)."""
    r = _http_chat(f'http://{host}:{port}/chat', message, timeout=timeout)
    return {'ok': r['ok'], 'action': 'chat', 'host': host, 'port': port, 'response': r.get('response'), 'error': r.get('error')}

def act_mesh_chat(message: str, hosts: List[str], include_self: bool=True, ports: Optional[List[int]]=None, timeout: int=90) -> Dict[str, Any]:
    """Fan out the same prompt across self + every host's twin ports."""
    ports = ports or list(FEDERATION_PORTS.values())
    targets: List[Dict[str, Any]] = []
    if include_self:
        for p in ports:
            targets.append({'host': '127.0.0.1', 'port': p, 'label': 'self'})
    for h in hosts:
        for p in ports:
            targets.append({'host': h, 'port': p, 'label': 'peer'})
    out = []
    for t in targets:
        r = _http_chat(f"http://{t['host']}:{t['port']}/chat", message, timeout=timeout)
        out.append({**t, **r})
    return {'ok': True, 'action': 'mesh_chat', 'message': message, 'targets': len(out), 'results': out}

def act_mesh_exec(command: str, hosts: List[str], ssh_user: str=DEFAULT_SSH_USER, timeout: int=SSH_TIMEOUT) -> Dict[str, Any]:
    results = _ssh_many(ssh_user, hosts, command, timeout=timeout)
    return {'ok': all((r['ok'] for r in results)), 'action': 'mesh_exec', 'command': command, 'results': results}

def act_provision_brainstem(host: str, ssh_user: str=DEFAULT_SSH_USER) -> Dict[str, Any]:
    """Make sure the mini's brainstem is up.  Doesn't install anything else."""
    script = '\nif curl -s -m 1 http://localhost:7071/health 2>/dev/null | grep -q \'"status".*"ok"\'; then\n  echo "STATE=already-running"\nelif [ -f "$HOME/.brainstem/src/rapp_brainstem/start.sh" ]; then\n  pkill -f "rapp_brainstem.*start" 2>/dev/null\n  sleep 1\n  cd "$HOME/.brainstem/src/rapp_brainstem"\n  nohup bash start.sh > /tmp/brainstem.log 2>&1 &\n  disown\n  for i in $(seq 1 30); do\n    sleep 1\n    if curl -s -m 1 http://localhost:7071/health 2>/dev/null | grep -q \'"status".*"ok"\'; then\n      echo "STATE=started"\n      break\n    fi\n  done\n  if ! curl -s -m 1 http://localhost:7071/health 2>/dev/null | grep -q \'"status".*"ok"\'; then\n    echo "STATE=failed"\n    echo "LOG_TAIL=$(tail -30 /tmp/brainstem.log 2>&1)"\n  fi\nelse\n  echo "STATE=not-installed"\nfi\necho "HEALTH=$(curl -s -m 2 http://localhost:7071/health)"\n'.strip()
    r = _ssh(ssh_user, host, script, timeout=90)
    return {'ok': r['ok'] and 'STATE=already-running' in r['stdout'] or 'STATE=started' in r['stdout'], 'action': 'provision_brainstem', 'host': host, 'raw': r['stdout'][-1500:]}

def act_install_agent(host: str, agent_filename: str, agent_url: Optional[str]=None, agent_content: Optional[str]=None, ssh_user: str=DEFAULT_SSH_USER) -> Dict[str, Any]:
    """Drop an *_agent.py into the host's brainstem agents/ folder.
    Either pass agent_url (will curl it on the host) or agent_content (sent over stdin)."""
    dst = f'$HOME/.brainstem/src/rapp_brainstem/agents/{shlex.quote(agent_filename)}'
    if agent_url:
        cmd = f'mkdir -p $(dirname {dst}) && curl -fsSL {shlex.quote(agent_url)} -o {dst} && echo OK'
        r = _ssh(ssh_user, host, cmd, timeout=30)
    elif agent_content:
        cmd = f'mkdir -p $(dirname {dst}) && cat > {dst} && echo OK'
        r = _ssh(ssh_user, host, cmd, timeout=20, stdin=agent_content)
    else:
        return {'ok': False, 'action': 'install_agent', 'error': 'agent_url OR agent_content required'}
    return {'ok': r['ok'] and 'OK' in r['stdout'], 'action': 'install_agent', 'host': host, 'filename': agent_filename}

def act_hatch_egg(host: str, egg_file: str=DEFAULT_EGG_FILE, egg_url: Optional[str]=None, ssh_user: str=DEFAULT_SSH_USER) -> Dict[str, Any]:
    egg_url = egg_url or f'{EGG_SERVER_URL}/{egg_file}'
    inst = act_install_agent(host, 'twin_egg_hatcher_agent.py', agent_url=HATCHER_RAW_URL, ssh_user=ssh_user)
    cmd = f'mkdir -p /tmp/aibast-hatch && cd /tmp/aibast-hatch && curl -fsSL {shlex.quote(egg_url)} -o egg.egg && python3 $HOME/.brainstem/src/rapp_brainstem/agents/twin_egg_hatcher_agent.py hatch --egg ./egg.egg'
    r = _ssh(ssh_user, host, cmd, timeout=180)
    parsed = None
    try:
        i, j = (r['stdout'].find('{'), r['stdout'].rfind('}'))
        if i != -1 and j > i:
            parsed = json.loads(r['stdout'][i:j + 1])
    except Exception:
        pass
    return {'ok': r['ok'], 'action': 'hatch_egg', 'host': host, 'egg_url': egg_url, 'hatcher_install': inst, 'hatch_result': parsed, 'raw_tail': r['stdout'][-1500:] if not parsed else '(see hatch_result)'}

def act_boot_federation(host: str, ssh_user: str=DEFAULT_SSH_USER) -> Dict[str, Any]:
    """Boot all 4 federation twins on the host with their assigned ports."""
    parts = []
    for h, port in FEDERATION_PORTS.items():
        parts.append(f'(ws=$HOME/.rapp/twins/{h}; mkdir -p $HOME/.rapp/pids $HOME/.rapp/ports; echo {port} > $HOME/.rapp/ports/{h}.port; SOUL_PATH=$ws/soul.md AGENTS_PATH=$ws/agents PORT={port} nohup bash $HOME/.brainstem/src/rapp_brainstem/start.sh > /tmp/twin-{h}.log 2>&1 & disown; echo $! > $HOME/.rapp/pids/{h}.pid; echo BOOTED {h} {port})')
    wait = 'for p in ' + ' '.join((str(p) for p in FEDERATION_PORTS.values())) + '; do for i in $(seq 1 30); do if curl -s -m 1 http://localhost:$p/health 2>/dev/null | grep -q \'"status".*"ok"\'; then echo READY $p; break; fi; sleep 1; done; done'
    r = _ssh(ssh_user, host, '; '.join(parts) + '; ' + wait, timeout=180)
    return {'ok': r['ok'] and r['stdout'].count('READY ') >= 4, 'action': 'boot_federation', 'host': host, 'booted_lines': [l for l in r['stdout'].splitlines() if l.startswith('BOOTED ')], 'ready_lines': [l for l in r['stdout'].splitlines() if l.startswith('READY ')]}

def act_status(hosts: Optional[List[str]]=None) -> Dict[str, Any]:
    hosts = hosts or []
    out: Dict[str, Any] = {'self': _snapshot('127.0.0.1')}
    out['peers'] = {h: _snapshot(h) for h in hosts}
    return {'ok': True, 'action': 'status', 'snapshot': out}

def _snapshot(host: str) -> Dict[str, Any]:
    return {'host': host, 'brainstem': _http_health(f'http://{host}:7071/health'), 'twins': {p: _http_health(f'http://{host}:{p}/health') for p in FEDERATION_PORTS.values()}}

_FLEET_CAPS_DIR = Path.home() / '.brainstem' / 'src' / 'rapp_brainstem' / 'agents' / 'fleet_capabilities'

def _fleet_ctx() -> Dict[str, Any]:
    """The names a custom snippet (or generated capability) can call."""
    return {'ssh': _ssh, 'ssh_many': _ssh_many, 'http_health': _http_health, 'http_chat': _http_chat, 'probe_tcp': _probe_tcp, 'EGG_SERVER_URL': EGG_SERVER_URL, 'DEFAULT_SSH_USER': DEFAULT_SSH_USER, 'FEDERATION_PORTS': FEDERATION_PORTS, 'HATCHER_RAW_URL': HATCHER_RAW_URL, 'json': json, 'os': os, 'subprocess': subprocess, 'Path': Path, 'shlex': shlex, 'datetime': datetime, 'timezone': timezone}

def act_custom(code: str, args: Optional[Dict[str, Any]]=None, name: str='custom') -> Dict[str, Any]:
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
    g: Dict[str, Any] = {'ctx': ctx, 'args': args, 'result': None}
    try:
        exec(compile(code, f'<fleet.custom:{name}>', 'exec'), g, g)
        if callable(g.get('run')):
            out = g['run'](ctx, args)
        else:
            out = g.get('result')
        return {'ok': True, 'action': 'custom', 'name': name, 'result': out}
    except Exception as e:
        return {'ok': False, 'action': 'custom', 'name': name, 'error': f'{type(e).__name__}: {e}'}

def act_extend(capability_name: str, python_source: str, overwrite: bool=False) -> Dict[str, Any]:
    """Persist a new capability the brainstem invented.  Writes a sidecar
    file under .../agents/fleet_capabilities/<capability_name>.py.  After
    this call, you can invoke the capability via action='custom' with
    `code=open(path).read()`, OR with action='cap', name='<capability_name>'.

    The source MUST define `def run(ctx, args): ...`.  Anything that needs
    SSH, HTTP, federation primitives is accessible via the `ctx` dict.
    """
    if not capability_name.isidentifier():
        return {'ok': False, 'action': 'extend', 'error': f'capability_name must be a Python identifier, got {capability_name!r}'}
    if 'def run(' not in python_source:
        return {'ok': False, 'action': 'extend', 'error': 'python_source must define `def run(ctx, args): ...`'}
    _FLEET_CAPS_DIR.mkdir(parents=True, exist_ok=True)
    target = _FLEET_CAPS_DIR / f'{capability_name}.py'
    if target.exists() and (not overwrite):
        return {'ok': False, 'action': 'extend', 'error': f'already exists: {target}', 'hint': 'pass overwrite=true to replace'}
    target.write_text(python_source, encoding='utf-8')
    return {'ok': True, 'action': 'extend', 'name': capability_name, 'path': str(target), 'invoke_via': [f"Fleet(action='cap', name='{capability_name}', args={{...}})", f"or read the file and use action='custom' with its source."]}

def act_cap(name: str, args: Optional[Dict[str, Any]]=None) -> Dict[str, Any]:
    """Invoke a previously-saved capability by name."""
    target = _FLEET_CAPS_DIR / f'{name}.py'
    if not target.exists():
        avail = sorted((p.stem for p in _FLEET_CAPS_DIR.glob('*.py'))) if _FLEET_CAPS_DIR.exists() else []
        return {'ok': False, 'action': 'cap', 'error': f'no such capability: {name}', 'available': avail}
    return act_custom(target.read_text(encoding='utf-8'), args=args, name=name)

def act_list_caps() -> Dict[str, Any]:
    if not _FLEET_CAPS_DIR.exists():
        return {'ok': True, 'action': 'list_caps', 'caps': [], 'dir': str(_FLEET_CAPS_DIR)}
    caps = []
    for p in sorted(_FLEET_CAPS_DIR.glob('*.py')):
        src = p.read_text(encoding='utf-8', errors='replace')
        doc = ''
        try:
            import ast
            tree = ast.parse(src)
            for node in tree.body:
                if isinstance(node, ast.FunctionDef) and node.name == 'run':
                    doc = (ast.get_docstring(node) or '').strip().splitlines()[0] if ast.get_docstring(node) else ''
                    break
        except Exception:
            pass
        caps.append({'name': p.stem, 'path': str(p), 'bytes': p.stat().st_size, 'summary': doc[:200]})
    return {'ok': True, 'action': 'list_caps', 'caps': caps, 'dir': str(_FLEET_CAPS_DIR)}

class FleetAgent(BasicAgent):
    """Generic fleet controller — drive the local Mac-mini fleet for ANYTHING.

    Not just deployment: arbitrary shell, file IO, tail logs, list ports, chat
    any twin on any host, fan out across the mesh.  The deployment helpers
    (provision_brainstem / hatch_egg / boot_federation) are convenience flows
    built on top of the same `exec` / `write` primitives.
    """

    def __init__(self) -> None:
        self.name = 'Fleet'
        self.metadata = {'name': self.name, 'description': "Drive the local Mac-mini fleet over SSH for anything — run shell, read/write files, tail logs, list processes/ports, chat any twin on any peer, fan out across the mesh, AND deploy the federation. Default SSH user is 'rappterone'; configure with FLEET_SSH_USER env. Authorize SSH first with action='authorize', host=<mini>.", 'parameters': {'type': 'object', 'properties': {'action': {'type': 'string', 'enum': ['discover', 'ping', 'authorize', 'exec', 'read', 'write', 'ls', 'tail', 'ports', 'ps', 'brainstem_health', 'chat', 'mesh_chat', 'mesh_exec', 'provision_brainstem', 'install_agent', 'hatch_egg', 'boot_federation', 'status', 'custom', 'extend', 'cap', 'list_caps'], 'description': "What to do.  Defaults to 'status'.  Use 'custom' when the fixed action set doesn't cover what's needed — pass `code` containing `def run(ctx, args): ...` to operate on the fleet helpers. Use 'extend' to persist a new named capability (then invoke with 'cap')."}, 'code': {'type': 'string', 'description': "For action='custom' — Python snippet defining `def run(ctx, args)` over fleet helpers (ctx has ssh, http_chat, http_health, probe_tcp, etc.)."}, 'args': {'type': 'object', 'description': "For action='custom' or 'cap' — JSON args passed to run(ctx, args)."}, 'name': {'type': 'string', 'description': "For action='extend' or 'cap' — capability identifier."}, 'python_source': {'type': 'string', 'description': "For action='extend' — the Python source to save as a new capability."}, 'overwrite': {'type': 'boolean', 'description': "For action='extend' — replace an existing capability of the same name."}, 'host': {'type': 'string', 'description': 'Single hostname or IP.'}, 'hosts': {'type': 'array', 'items': {'type': 'string'}, 'description': 'Multiple hostnames (for mesh / status / mesh_exec).'}, 'ssh_user': {'type': 'string', 'description': 'SSH username (default rappterone).'}, 'command': {'type': 'string', 'description': 'For exec / mesh_exec.'}, 'path': {'type': 'string', 'description': 'For read / write / ls / tail.'}, 'content': {'type': 'string', 'description': 'For write (file body).'}, 'lines': {'type': 'integer', 'description': 'For tail (default 50).'}, 'pattern': {'type': 'string', 'description': 'For ps (regex grep filter).'}, 'port': {'type': 'integer', 'description': 'For chat (target twin port).'}, 'ports': {'type': 'array', 'items': {'type': 'integer'}, 'description': 'For mesh_chat (default: federation ports 7081-7084).'}, 'message': {'type': 'string', 'description': 'For chat / mesh_chat.'}, 'agent_filename': {'type': 'string', 'description': 'For install_agent.'}, 'agent_url': {'type': 'string', 'description': 'For install_agent (curl source).'}, 'agent_content': {'type': 'string', 'description': 'For install_agent (inline body).'}, 'egg_file': {'type': 'string', 'description': 'For hatch_egg (filename in egg server).'}, 'egg_url': {'type': 'string', 'description': 'For hatch_egg (override full URL).'}, 'cidr': {'type': 'string', 'description': 'For discover (override /24).'}, 'include_self': {'type': 'boolean', 'description': 'For mesh_chat (default true).'}, 'timeout': {'type': 'integer', 'description': 'SSH / HTTP timeout seconds.'}}, 'required': []}}
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kw: Any) -> str:
        action = (kw.get('action') or 'status').lower()
        user = kw.get('ssh_user') or DEFAULT_SSH_USER
        timeout = int(kw.get('timeout') or SSH_TIMEOUT)
        try:
            if action == 'discover':
                result = act_discover(cidr=kw.get('cidr'))
            elif action == 'ping':
                result = act_ping(kw['host'], ssh_user=user)
            elif action == 'authorize':
                result = act_authorize(kw['host'], ssh_user=user)
            elif action == 'exec':
                hosts = kw.get('hosts') or kw['host']
                result = act_exec(hosts, kw['command'], ssh_user=user, timeout=timeout)
            elif action == 'read':
                result = act_read(kw['host'], kw['path'], ssh_user=user)
            elif action == 'write':
                result = act_write(kw['host'], kw['path'], kw['content'], ssh_user=user)
            elif action == 'ls':
                result = act_ls(kw['host'], kw['path'], ssh_user=user)
            elif action == 'tail':
                result = act_tail(kw['host'], kw['path'], int(kw.get('lines') or 50), ssh_user=user)
            elif action == 'ports':
                result = act_ports(kw['host'], ssh_user=user)
            elif action == 'ps':
                result = act_ps(kw['host'], kw.get('pattern') or '', ssh_user=user)
            elif action == 'brainstem_health':
                result = act_brainstem_health(kw['host'])
            elif action == 'chat':
                result = act_chat(kw['host'], int(kw['port']), kw['message'], timeout=timeout)
            elif action == 'mesh_chat':
                result = act_mesh_chat(kw['message'], hosts=kw.get('hosts') or [], include_self=kw.get('include_self', True), ports=kw.get('ports'), timeout=timeout)
            elif action == 'mesh_exec':
                result = act_mesh_exec(kw['command'], hosts=kw.get('hosts') or [], ssh_user=user, timeout=timeout)
            elif action == 'provision_brainstem':
                result = act_provision_brainstem(kw['host'], ssh_user=user)
            elif action == 'install_agent':
                result = act_install_agent(kw['host'], kw['agent_filename'], agent_url=kw.get('agent_url'), agent_content=kw.get('agent_content'), ssh_user=user)
            elif action == 'hatch_egg':
                result = act_hatch_egg(kw['host'], egg_file=kw.get('egg_file') or DEFAULT_EGG_FILE, egg_url=kw.get('egg_url'), ssh_user=user)
            elif action == 'boot_federation':
                result = act_boot_federation(kw['host'], ssh_user=user)
            elif action == 'status':
                result = act_status(hosts=kw.get('hosts') or ([kw['host']] if kw.get('host') else []))
            elif action == 'custom':
                result = act_custom(kw['code'], args=kw.get('args') or {}, name=kw.get('name') or 'custom')
            elif action == 'extend':
                result = act_extend(kw['name'], kw['python_source'], overwrite=bool(kw.get('overwrite', False)))
            elif action == 'cap':
                result = act_cap(kw['name'], args=kw.get('args') or {})
            elif action == 'list_caps':
                result = act_list_caps()
            else:
                result = {'ok': False, 'error': f'unknown action: {action}'}
        except KeyError as e:
            result = {'ok': False, 'action': action, 'error': f'missing required arg: {e}'}
        except Exception as e:
            result = {'ok': False, 'action': action, 'error': str(e)}
        return json.dumps(result, indent=2, default=str)

def _cli(argv: List[str]) -> int:
    a = FleetAgent()
    if not argv:
        print(a.perform(action='status'))
        return 0
    kw: Dict[str, Any] = {'action': argv[0]}
    i = 1
    while i < len(argv):
        k = argv[i].lstrip('-')
        if i + 1 < len(argv) and (not argv[i + 1].startswith('--')):
            v = argv[i + 1]
            if k in ('hosts', 'ports') and ',' in v:
                v = v.split(',')
            kw[k] = v
            i += 2
        else:
            kw[k] = True
            i += 1
    print(a.perform(**kw))
    return 0

if __name__ == '__main__':
    sys.exit(_cli(sys.argv[1:]))



# ─────────────────────────────────────────────────────────────────────
# Section: learn_new_agent.py
# ─────────────────────────────────────────────────────────────────────
try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent

class LearnNewAgent(BasicAgent):
    AGENT_TEMPLATE = '"""\n{description}\n\nAuto-generated by LearnNewAgent on {date}.\nDrop this file into any RAPP brainstem\'s agents/ directory and it works.\nCompatible with the RAR registry at https://github.com/kody-w/RAR\n"""\n\nimport json\n{extra_imports}\ntry:\n    from agents.basic_agent import BasicAgent\nexcept ImportError:\n    from basic_agent import BasicAgent\n\n\n__manifest__ = {{\n    "schema": "rapp-agent/1.0",\n    "name": "@{namespace}/{snake_name}",\n    "version": "1.0.0",\n    "display_name": "{agent_name}",\n    "description": "{agent_description}",\n    "author": "{author}",\n    "tags": {tags_json},\n    "category": "{category}",\n    "quality_tier": "community",\n    "requires_env": {env_json},\n    "dependencies": ["@rapp/basic_agent"],\n    "example_call": {{"args": {example_args_json}}},\n}}\n\n\nclass {class_name}(BasicAgent):\n    def __init__(self):\n        self.name = \'{agent_name}\'\n        self.metadata = {{\n            "name": self.name,\n            "description": __manifest__["description"],\n            "parameters": {{\n                "type": "object",\n                "properties": {{\n                    "query": {{\n                        "type": "string",\n                        "description": "The user\'s request or input."\n                    }}{extra_params}\n                }},\n                "required": []\n            }}\n        }}\n        super().__init__(name=self.name, metadata=self.metadata)\n\n    def perform(self, **kwargs):\n        """Execute the agent\'s task."""\n        query = kwargs.get(\'query\', \'\')\n\n{perform_body}\n\n\nif __name__ == "__main__":\n    a = {class_name}()\n    print(a.perform(query="test"))\n'
    SWARM_SUB_TEMPLATE = '"""\n{description}\n\nPart of the {swarm_name} swarm pipeline. Handles the {role} stage.\nAuto-generated by LearnNewAgent on {date}.\n"""\n\nimport json\n{extra_imports}\ntry:\n    from agents.basic_agent import BasicAgent\nexcept ImportError:\n    from basic_agent import BasicAgent\n\n\n__manifest__ = {{\n    "schema": "rapp-agent/1.0",\n    "name": "@{namespace}/{snake_name}",\n    "version": "1.0.0",\n    "display_name": "{agent_name}",\n    "description": "{agent_description}",\n    "author": "{author}",\n    "tags": {tags_json},\n    "category": "{category}",\n    "quality_tier": "community",\n    "requires_env": [],\n    "dependencies": ["@rapp/basic_agent"],\n    "example_call": {{"args": {{"task": "example {role} task"}}}},\n}}\n\n\nclass {class_name}(BasicAgent):\n    def __init__(self):\n        self.name = \'{agent_name}\'\n        self.metadata = {{\n            "name": self.name,\n            "description": __manifest__["description"],\n            "parameters": {{\n                "type": "object",\n                "properties": {{\n                    "task": {{\n                        "type": "string",\n                        "description": "What to {role}"\n                    }}\n                }},\n                "required": ["task"]\n            }}\n        }}\n        super().__init__(name=self.name, metadata=self.metadata)\n\n    def perform(self, **kwargs):\n        task = kwargs.get(\'task\', \'\')\n\n{perform_body}\n\n\nif __name__ == "__main__":\n    a = {class_name}()\n    print(a.perform(task="test"))\n'
    SWARM_ORCH_TEMPLATE = '"""\n{description}\n\nOrchestrates the {swarm_name} swarm by coordinating sub-agents:\n{sub_agent_list}\n\nAuto-generated by LearnNewAgent on {date}.\nDrop this file into any RAPP brainstem\'s agents/ directory and it works.\nUse SwarmFactory to converge the sub-agents into a single shareable singleton.\n"""\n\nimport json\nimport os\n\ntry:\n    from agents.basic_agent import BasicAgent\nexcept ImportError:\n    from basic_agent import BasicAgent\n\n{sub_agent_imports}\n\n\n__manifest__ = {{\n    "schema": "rapp-agent/1.0",\n    "name": "@{namespace}/{snake_name}",\n    "version": "1.0.0",\n    "display_name": "{swarm_name}",\n    "description": "{agent_description}",\n    "author": "{author}",\n    "tags": {tags_json},\n    "category": "{category}",\n    "quality_tier": "community",\n    "requires_env": [],\n    "dependencies": ["@rapp/basic_agent"],\n    "example_call": {{"args": {{"task": "Run the {swarm_name} pipeline"}}}},\n}}\n\n\nclass {class_name}(BasicAgent):\n    def __init__(self):\n        self.name = \'{swarm_name}\'\n        self.metadata = {{\n            "name": self.name,\n            "description": __manifest__["description"],\n            "parameters": {{\n                "type": "object",\n                "properties": {{\n                    "task": {{\n                        "type": "string",\n                        "description": "What you want the swarm to do"\n                    }},\n                    "sub_agent": {{\n                        "type": "string",\n                        "description": "Optional: run a specific sub-agent by name instead of the full pipeline"\n                    }}\n                }},\n                "required": ["task"]\n            }}\n        }}\n        super().__init__(name=self.name, metadata=self.metadata)\n        self._agents = {{}}\n\n    def _get_agent(self, name):\n        if name not in self._agents:\n            agents = {{{agent_map}}}\n            cls = agents.get(name)\n            if cls:\n                self._agents[name] = cls()\n        return self._agents.get(name)\n\n    def perform(self, **kwargs):\n        task = kwargs.get(\'task\', \'\')\n        sub_agent = kwargs.get(\'sub_agent\', \'\')\n\n        if sub_agent:\n            agent = self._get_agent(sub_agent)\n            if not agent:\n                available = {agent_names_json}\n                return json.dumps({{"status": "error",\n                    "message": f"Unknown sub-agent \'{{sub_agent}}\'. Available: {{available}}"}})\n            return agent.perform(task=task, **kwargs)\n\n        results = {{}}\n        pipeline = {pipeline_json}\n        slush = {{}}\n        for step_name in pipeline:\n            agent = self._get_agent(step_name)\n            if agent:\n                agent_kwargs = {{"task": task}}\n                if hasattr(agent, \'context\'):\n                    agent.context = type(\'Ctx\', (), {{\'slush\': slush}})()\n                r = agent.perform(**agent_kwargs)\n                results[step_name] = r\n                try:\n                    parsed = json.loads(r)\n                    if \'data_slush\' in parsed:\n                        slush.update(parsed[\'data_slush\'])\n                except (json.JSONDecodeError, TypeError):\n                    pass\n\n        return json.dumps({{\n            "status": "ok",\n            "swarm": "{swarm_name}",\n            "pipeline_steps": len(pipeline),\n            "results": results,\n        }})\n\n\nif __name__ == "__main__":\n    a = {class_name}()\n    print(a.perform(task="test"))\n'

    def __init__(self):
        self.name = 'LearnNew'
        self.metadata = {'name': self.name, 'description': "Creates new RAPP agents or swarms from natural-language descriptions. Actions: 'create' generates a single agent, 'swarm' creates a multi-agent pipeline, 'list' shows generated agents, 'delete' removes one, 'preview' dry-runs generation, 'submit' prepares a RAR registry submission. Call when the user wants to teach the brainstem something new, create a custom agent, or build an agent swarm.", 'parameters': {'type': 'object', 'properties': {'description': {'type': 'string', 'description': 'Natural language description of what the new agent should do.'}, 'name': {'type': 'string', 'description': 'Name for the new agent (optional, will be generated from description).'}, 'action': {'type': 'string', 'description': 'Action to perform.', 'enum': ['create', 'swarm', 'list', 'delete', 'preview', 'submit']}, 'query': {'type': 'string', 'description': 'Natural language query that may contain the agent description.'}, 'category': {'type': 'string', 'enum': ['general', 'productivity', 'sales', 'support', 'data', 'automation', 'integrations', 'devtools', 'pipeline'], 'description': 'Agent category for the registry.'}, 'namespace': {'type': 'string', 'description': 'RAR namespace for submission (e.g. @myname). Defaults to @rapp.'}, 'agents_in_swarm': {'type': 'string', 'description': "For swarm: comma-separated sub-agent roles (e.g. 'researcher,writer,editor')."}, 'requires_env': {'type': 'string', 'description': "Comma-separated env vars the agent needs (e.g. 'API_KEY,WEBHOOK_URL')."}}, 'required': []}}
        super().__init__(name=self.name, metadata=self.metadata)
        self.agents_dir = Path(__file__).parent

    def perform(self, **kwargs):
        action = kwargs.pop('action', 'create')
        description = kwargs.pop('description', '')
        name = kwargs.pop('name', '')
        query = kwargs.pop('query', '')
        if not description and query:
            description = query
        if action == 'list':
            return self._list_generated_agents()
        elif action == 'delete':
            return self._delete_agent(name or description)
        elif action == 'preview':
            if kwargs.get('agents_in_swarm'):
                return self._create_swarm(description, name, write=False, **kwargs)
            return self._create_agent(description, name, write=False, **kwargs)
        elif action == 'submit':
            return self._prepare_submit(description, name, **kwargs)
        elif action == 'swarm':
            return self._create_swarm(description, name, write=True, **kwargs)
        else:
            return self._create_agent(description, name, write=True, **kwargs)

    def _create_agent(self, description, name='', write=True, **kwargs):
        if not description:
            return json.dumps({'status': 'error', 'message': 'Please provide a description of what the agent should do.'})
        if not name:
            name = self._generate_name(description)
        name = self._sanitize_name(name)
        class_name = f'{name}Agent'
        snake = self._to_snake_case(name)
        file_name = f'{snake}_agent.py'
        file_path = self.agents_dir / file_name
        if write and file_path.exists():
            return json.dumps({'status': 'error', 'message': f"Agent '{name}' already exists at {file_path}. Delete it first or choose a different name."})
        agent_code = self._generate_agent_code(description, name, class_name, **kwargs)
        if not write:
            return json.dumps({'status': 'ok', 'action': 'preview', 'filename': file_name, 'class_name': class_name, 'display_name': name, 'lines': len(agent_code.split('\n')), 'code': agent_code, 'message': f"Preview of {file_name} — use action='create' to write it."})
        try:
            file_path.write_text(agent_code)
        except Exception as e:
            return json.dumps({'status': 'error', 'message': f'Failed to write agent file: {e}'})
        hot_load_result = self._hot_load_agent(file_path, class_name)
        result = {'status': 'success', 'action': 'create', 'message': f"Created and loaded agent '{name}'", 'agent_name': name, 'filename': file_name, 'file_path': str(file_path), 'lines': len(agent_code.split('\n')), 'hot_loaded': hot_load_result.get('success', False), 'description': description[:200], 'hint': f"Agent saved to agents/{file_name} — it will auto-load on next request. Edit the perform() method to customize the logic. To submit to RAR, re-run with action='submit'."}
        if hot_load_result.get('installed_deps'):
            result['installed_dependencies'] = hot_load_result['installed_deps']
        if not hot_load_result.get('success'):
            result['hot_load_error'] = hot_load_result.get('error')
            if hot_load_result.get('hint'):
                result['hot_load_hint'] = hot_load_result['hint']
        return json.dumps(result)

    def _create_swarm(self, description, swarm_name='', write=True, **kwargs):
        if not description:
            return json.dumps({'status': 'error', 'message': 'Please provide a description of what the swarm should do.'})
        if not swarm_name:
            swarm_name = self._generate_name(description)
        swarm_name = self._sanitize_name(swarm_name)
        agents_in_swarm = kwargs.get('agents_in_swarm', '')
        if agents_in_swarm:
            sub_roles = [s.strip() for s in agents_in_swarm.split(',') if s.strip()]
        else:
            sub_roles = ['researcher', 'processor', 'formatter']
        category = kwargs.get('category', 'pipeline')
        namespace = (kwargs.get('namespace', '') or 'rapp').lstrip('@')
        env_list = [e.strip() for e in (kwargs.get('requires_env', '') or '').split(',') if e.strip()]
        tags = self._generate_tags(description) + ['swarm']
        generated_files = []
        for role in sub_roles:
            sub_name = self._sanitize_name(role)
            sub_snake = self._to_snake_case(swarm_name) + '_' + self._to_snake_case(sub_name)
            sub_class = f'{sub_name}Agent'
            sub_filename = f'{sub_snake}_agent.py'
            sub_desc = f'{sub_name} sub-agent for the {swarm_name} swarm.'
            perform_body = self._generate_perform_body(f'{role} step for a {description}')
            sub_code = self.SWARM_SUB_TEMPLATE.format(description=sub_desc, swarm_name=swarm_name, role=role.lower(), date=datetime.now().strftime('%Y-%m-%d %H:%M'), namespace=namespace, snake_name=sub_snake, agent_name=sub_name, agent_description=sub_desc.replace('"', '\\"'), author=namespace, class_name=sub_class, category=category, tags_json=json.dumps([category, 'swarm-member', self._to_snake_case(role)]), env_json=json.dumps(env_list), perform_body=perform_body, extra_imports=self._generate_extra_imports(sub_desc))
            if write:
                dest = self.agents_dir / sub_filename
                try:
                    dest.write_text(sub_code)
                except Exception as e:
                    return json.dumps({'status': 'error', 'message': f'Failed to write {sub_filename}: {e}'})
            generated_files.append({'filename': sub_filename, 'class': sub_class, 'role': role, 'snake': sub_snake})
        orch_snake = self._to_snake_case(swarm_name)
        orch_filename = f'{orch_snake}_agent.py'
        orch_class = f'{swarm_name}Agent'
        safe_desc = description.replace('"', '\\"').replace('\n', ' ')[:200]
        sub_imports = '\n'.join((f"from agents.{f['snake']}_agent import {f['class']}" for f in generated_files))
        agent_map = ', '.join((f'''"{self._to_snake_case(f['role'])}": {f['class']}''' for f in generated_files))
        agent_names = [self._to_snake_case(f['role']) for f in generated_files]
        sub_list_str = '\n'.join((f"  - {f['class']} ({f['role']})" for f in generated_files))
        orch_code = self.SWARM_ORCH_TEMPLATE.format(description=description, swarm_name=swarm_name, sub_agent_list=sub_list_str, date=datetime.now().strftime('%Y-%m-%d %H:%M'), namespace=namespace, snake_name=orch_snake, agent_description=safe_desc, author=namespace, class_name=orch_class, category=category, tags_json=json.dumps(tags), sub_agent_imports=sub_imports, agent_map=agent_map, agent_names_json=json.dumps(agent_names), pipeline_json=json.dumps(agent_names))
        if write:
            dest = self.agents_dir / orch_filename
            try:
                dest.write_text(orch_code)
            except Exception as e:
                return json.dumps({'status': 'error', 'message': f'Failed to write {orch_filename}: {e}'})
        generated_files.append({'filename': orch_filename, 'class': orch_class, 'role': 'orchestrator', 'is_orchestrator': True})
        all_filenames = [f['filename'] for f in generated_files]
        result = {'status': 'success', 'action': 'swarm' if write else 'preview', 'swarm_name': swarm_name, 'files_generated': len(generated_files), 'filenames': all_filenames, 'sub_agents': sub_roles, 'orchestrator': orch_filename, 'message': f'Created {swarm_name} swarm: {len(sub_roles)} sub-agents + 1 orchestrator ({len(generated_files)} files total). '}
        if write:
            result['message'] += 'All written to agents/ — they auto-load on next request. Use SwarmFactory (action=build) to converge them into a single shareable singleton file.'
            for f in generated_files:
                if not f.get('is_orchestrator'):
                    fpath = self.agents_dir / f['filename']
                    self._hot_load_agent(fpath, f['class'])
            orch_path = self.agents_dir / orch_filename
            self._hot_load_agent(orch_path, orch_class)
        else:
            result['orchestrator_code'] = orch_code
        return json.dumps(result)

    def _prepare_submit(self, description, name='', **kwargs):
        preview = json.loads(self._create_agent(description, name, write=False, **kwargs))
        if preview.get('status') != 'ok':
            return json.dumps(preview)
        code = preview.get('code', '')
        namespace = (kwargs.get('namespace', '') or 'rapp').lstrip('@')
        filename = preview['filename']
        rar_path = f'agents/@{namespace}/{filename}'
        issue_title = f"[AGENT] @{namespace}/{filename.replace('.py', '')}"
        return json.dumps({'status': 'ok', 'action': 'submit', 'filename': filename, 'namespace': f'@{namespace}', 'rar_path': rar_path, 'issue_title': issue_title, 'code': code, 'message': f'Agent ready for RAR submission.\n\nOption 1 — GitHub Issue:\n  Open https://github.com/kody-w/RAR/issues/new\n  Title: {issue_title}\n  Body: paste the agent code as a Python code block.\n\nOption 2 — Pull Request:\n  Add the file to {rar_path} and open a PR.\n\nThe registry CI validates the manifest and runs security checks.'})

    def _generate_name(self, description):
        try:
            result = subprocess.run(['copilot', '--message', f'Generate a short 1-2 word CamelCase name for an agent that: {description[:200]}. Reply with ONLY the name, nothing else.'], capture_output=True, text=True, timeout=10)
            if result.returncode == 0 and result.stdout.strip():
                name = result.stdout.strip().split('\n')[0]
                name = re.sub('[^a-zA-Z]', '', name)
                if name and len(name) <= 30:
                    return name
        except Exception:
            pass
        words = description.lower().split()
        keywords = [w for w in words if len(w) > 3 and w not in {'that', 'this', 'with', 'from', 'agent', 'create', 'make', 'want', 'should', 'would', 'could', 'learn', 'teach', 'build', 'about', 'which', 'their', 'your', 'they'}]
        if keywords:
            return ''.join((w.capitalize() for w in keywords[:2]))
        return 'Custom'

    def _sanitize_name(self, name):
        name = re.sub('[^a-zA-Z0-9]', '', name)
        if name and (not name[0].isalpha()):
            name = 'Agent' + name
        if name:
            name = name[0].upper() + name[1:]
        return name or 'Custom'

    def _to_snake_case(self, name):
        s1 = re.sub('(.)([A-Z][a-z]+)', '\\1_\\2', name)
        return re.sub('([a-z0-9])([A-Z])', '\\1_\\2', s1).lower()

    def _generate_agent_code(self, description, name, class_name, **kwargs):
        perform_body = self._generate_perform_body(description)
        extra_params = self._generate_extra_params(description)
        extra_imports = self._generate_extra_imports(description)
        safe_desc = description.replace('"', '\\"').replace('\n', ' ')[:200]
        tags = self._generate_tags(description)
        snake = self._to_snake_case(name)
        category = kwargs.get('category', 'general')
        namespace = (kwargs.get('namespace', '') or 'rapp').lstrip('@')
        env_list = [e.strip() for e in (kwargs.get('requires_env', '') or '').split(',') if e.strip()]
        extra_params_inferred = self._infer_example_params(description)
        example_args = {}
        if extra_params_inferred:
            for p in extra_params_inferred[:2]:
                example_args[p] = f'example {p}'
        else:
            example_args['query'] = 'example query'
        return self.AGENT_TEMPLATE.format(description=description, date=datetime.now().strftime('%Y-%m-%d %H:%M'), class_name=class_name, agent_name=name, agent_description=safe_desc, extra_imports=extra_imports, extra_params=extra_params, perform_body=perform_body, tags_json=json.dumps(tags), category=category, namespace=namespace, snake_name=snake, author=namespace, env_json=json.dumps(env_list), example_args_json=json.dumps(example_args))

    def _infer_example_params(self, description):
        params = []
        desc_lower = description.lower()
        if any((w in desc_lower for w in ['url', 'link', 'website', 'page'])):
            params.append('url')
        if any((w in desc_lower for w in ['file', 'read', 'write', 'path'])):
            params.append('path')
        if any((w in desc_lower for w in ['search', 'find', 'look'])):
            params.append('query')
        return params

    def _generate_tags(self, description):
        tags = []
        desc_lower = description.lower()
        tag_map = {'weather': 'weather', 'api': 'api', 'web': 'web', 'file': 'filesystem', 'data': 'data', 'search': 'search', 'email': 'email', 'database': 'database', 'sql': 'database', 'news': 'news', 'schedule': 'scheduling', 'voice': 'voice', 'stock': 'finance', 'price': 'finance', 'video': 'media', 'image': 'media', 'summarize': 'nlp', 'translate': 'nlp', 'monitor': 'monitoring', 'track': 'tracking', 'slack': 'messaging'}
        for keyword, tag in tag_map.items():
            if keyword in desc_lower and tag not in tags:
                tags.append(tag)
        return tags or ['custom']

    def _generate_extra_params(self, description):
        extra = ''
        desc_lower = description.lower()
        if any((w in desc_lower for w in ['file', 'read', 'write', 'path'])):
            extra += ',\n                    "path": {\n                        "type": "string",\n                        "description": "File or directory path."\n                    }'
        if any((w in desc_lower for w in ['url', 'http', 'web', 'fetch'])):
            extra += ',\n                    "url": {\n                        "type": "string",\n                        "description": "URL to access."\n                    }'
        if any((w in desc_lower for w in ['number', 'count', 'amount', 'limit'])):
            extra += ',\n                    "count": {\n                        "type": "integer",\n                        "description": "Number or count value."\n                    }'
        return extra

    def _generate_perform_body(self, description):
        try:
            prompt = f'Generate ONLY the Python code for the body of a perform() method for an agent that: {description}\n\nRules:\n- Return a JSON string with status and result\n- Use kwargs.get() to access parameters\n- Keep it simple and functional\n- Do NOT include the method signature, just the body\n- Indent with 8 spaces\n\nExample format:\n        # Process the query\n        result = "processed: " + query\n        return json.dumps({{"status": "success", "result": result}})'
            result = subprocess.run(['copilot', '--message', prompt], capture_output=True, text=True, timeout=30)
            if result.returncode == 0 and result.stdout.strip():
                body = result.stdout.strip()
                if '```python' in body:
                    body = body.split('```python')[1].split('```')[0]
                elif '```' in body:
                    body = body.split('```')[1].split('```')[0]
                lines = body.strip().split('\n')
                indented = '\n'.join(('        ' + line.lstrip() if line.strip() else '' for line in lines))
                if indented.strip():
                    return indented
        except Exception:
            pass
        return '        # Default implementation - customize this\n        if not query:\n            return json.dumps({\n                "status": "error",\n                "message": "No query provided"\n            })\n\n        return json.dumps({\n            "status": "success",\n            "query": query,\n            "result": f"Processed by {self.name}: {query}"\n        })'

    def _generate_extra_imports(self, description):
        imports = []
        desc_lower = description.lower()
        import_map = {('http', 'api', 'fetch', 'url', 'web', 'request'): 'import urllib.request', ('html', 'scrape', 'parse html', 'beautifulsoup'): 'from bs4 import BeautifulSoup', ('csv', 'spreadsheet'): 'import csv', ('xml',): 'import xml.etree.ElementTree as ET', ('datetime', 'date', 'time', 'timestamp'): 'from datetime import datetime', ('regex', 'pattern', 'match'): 'import re', ('file', 'read', 'write', 'path'): 'from pathlib import Path', ('base64', 'encode', 'decode'): 'import base64', ('hash', 'md5', 'sha'): 'import hashlib', ('random', 'shuffle', 'choice'): 'import random', ('sleep', 'wait', 'delay'): 'import time', ('environment', 'env var'): 'import os'}
        for keywords, import_stmt in import_map.items():
            if any((kw in desc_lower for kw in keywords)):
                if import_stmt not in imports:
                    imports.append(import_stmt)
        if imports:
            return '\n'.join(imports) + '\n'
        return ''

    def _hot_load_agent(self, file_path, class_name):
        try:
            import importlib.util
            code = file_path.read_text()
            missing_deps = self._detect_missing_imports(code)
            if missing_deps:
                install_result = self._install_dependencies(missing_deps)
                if not install_result['success']:
                    return {'success': False, 'error': f"Failed to install dependencies: {install_result['error']}", 'missing_deps': missing_deps}
            spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            agent_class = getattr(module, class_name, None)
            if agent_class is None:
                return {'success': False, 'error': 'Class not found in module'}
            import sys
            module_name = f'agents.{file_path.stem}'
            sys.modules[module_name] = module
            result = {'success': True, 'class': class_name}
            if missing_deps:
                result['installed_deps'] = missing_deps
            return result
        except ModuleNotFoundError as e:
            missing = str(e).split("'")[1] if "'" in str(e) else str(e)
            return {'success': False, 'error': f'Missing module: {missing}', 'hint': f'Try: pip install {missing}'}
        except Exception as e:
            return {'success': False, 'error': str(e)}

    def _detect_missing_imports(self, code):
        import importlib
        missing = []
        import_pattern = '^(?:from\\s+(\\w+)|import\\s+(\\w+))'
        for line in code.split('\n'):
            line = line.strip()
            match = re.match(import_pattern, line)
            if match:
                module_name = match.group(1) or match.group(2)
                if module_name in self._stdlib_modules():
                    continue
                if module_name in ('agents', 'basic_agent'):
                    continue
                try:
                    importlib.import_module(module_name)
                except ImportError:
                    pkg_name = self._module_to_package(module_name)
                    if pkg_name not in missing:
                        missing.append(pkg_name)
        return missing

    def _module_to_package(self, module_name):
        mappings = {'cv2': 'opencv-python', 'PIL': 'Pillow', 'sklearn': 'scikit-learn', 'yaml': 'pyyaml', 'bs4': 'beautifulsoup4', 'dotenv': 'python-dotenv', 'jwt': 'pyjwt', 'serial': 'pyserial', 'usb': 'pyusb', 'Crypto': 'pycryptodome'}
        return mappings.get(module_name, module_name)

    def _stdlib_modules(self):
        return {'abc', 'argparse', 'ast', 'asyncio', 'base64', 'collections', 'contextlib', 'copy', 'csv', 'datetime', 'decimal', 'difflib', 'email', 'enum', 'functools', 'glob', 'gzip', 'hashlib', 'heapq', 'html', 'http', 'importlib', 'inspect', 'io', 'itertools', 'json', 'logging', 'math', 'mimetypes', 'multiprocessing', 'operator', 'os', 'pathlib', 'pickle', 'platform', 'pprint', 'queue', 'random', 're', 'shutil', 'signal', 'socket', 'sqlite3', 'ssl', 'statistics', 'string', 'struct', 'subprocess', 'sys', 'tempfile', 'textwrap', 'threading', 'time', 'traceback', 'types', 'typing', 'unittest', 'urllib', 'uuid', 'warnings', 'weakref', 'xml', 'zipfile', 'zlib'}

    def _install_dependencies(self, packages):
        if not packages:
            return {'success': True}
        try:
            import sys
            for pkg in packages:
                result = subprocess.run([sys.executable, '-m', 'pip', 'install', '--quiet', pkg], capture_output=True, text=True, timeout=60)
                if result.returncode != 0:
                    return {'success': False, 'error': f'pip install {pkg} failed: {result.stderr}'}
            return {'success': True, 'installed': packages}
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'pip install timed out'}
        except Exception as e:
            return {'success': False, 'error': str(e)}

    def _list_generated_agents(self):
        agents = []
        core = {'basic_agent.py', 'save_memory_agent.py', 'recall_memory_agent.py', 'learn_new_agent.py', 'swarm_factory_agent.py'}
        for f in sorted(self.agents_dir.glob('*_agent.py')):
            if f.name in core:
                continue
            content = f.read_text()
            is_generated = 'Auto-generated by LearnNewAgent' in content
            agents.append({'name': f.stem.replace('_agent', ''), 'file': f.name, 'auto_generated': is_generated})
        return json.dumps({'status': 'success', 'agents': agents, 'count': len(agents)})

    def _delete_agent(self, name):
        if not name:
            return json.dumps({'status': 'error', 'message': 'Please provide the agent name to delete.'})
        snake_name = self._to_snake_case(self._sanitize_name(name))
        file_path = self.agents_dir / f'{snake_name}_agent.py'
        if not file_path.exists():
            for f in self.agents_dir.glob('*_agent.py'):
                if name.lower() in f.name.lower():
                    file_path = f
                    break
        if not file_path.exists():
            return json.dumps({'status': 'error', 'message': f"Agent '{name}' not found."})
        core = {'basic_agent.py', 'save_memory_agent.py', 'recall_memory_agent.py', 'learn_new_agent.py', 'swarm_factory_agent.py'}
        if file_path.name in core:
            return json.dumps({'status': 'error', 'message': 'Cannot delete core agents.'})
        try:
            file_path.unlink()
            return json.dumps({'status': 'success', 'message': f"Deleted agent '{name}'", 'file': str(file_path)})
        except Exception as e:
            return json.dumps({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    a = LearnNewAgent()
    print(a.perform(action='preview', description='An agent that tracks daily habits and streaks'))



# ─────────────────────────────────────────────────────────────────────
# Section: neighborhood_run_agent.py
# ─────────────────────────────────────────────────────────────────────
_HOME = os.path.expanduser('~')

_SIMULATED_ROOT = os.path.join(_HOME, '.rapp', 'simulated')

_SSH_OPTS = ('-o', 'BatchMode=yes', '-o', 'ConnectTimeout=5', '-o', 'StrictHostKeyChecking=accept-new', '-o', 'ServerAliveInterval=10', '-o', 'ServerAliveCountMax=3')

def _ssh_exec(user, host, command, timeout=120, stdin_bytes=None):
    """Run shell on a peer.  stdin_bytes can be raw bytes for tar-style piping."""
    try:
        proc = subprocess.run(['ssh', *_SSH_OPTS, f'{user}@{host}', command], input=stdin_bytes, capture_output=True, timeout=timeout)
        return {'ok': proc.returncode == 0, 'stdout': proc.stdout.decode('utf-8', 'replace'), 'stderr': proc.stderr.decode('utf-8', 'replace'), 'exit': proc.returncode}
    except subprocess.TimeoutExpired:
        return {'ok': False, 'stdout': '', 'stderr': f'ssh timeout {timeout}s', 'exit': -1}
    except Exception as e:
        return {'ok': False, 'stdout': '', 'stderr': str(e), 'exit': -2}

def _github_pr_restore(owner_repo, twin_hash, tarball_bytes, branch_prefix='rapp-neighborhood-restore', base_branch='main', pr_title=None, pr_body=None, dry_run=False):
    """Apply a snapshot's twin tarball to a GitHub repo as a PR.

    Flow: clone repo → untar snapshot into the clone (stripping the <hash>/
    prefix so files land at repo root) → if anything changed, commit on a
    new branch → push → open a PR.  NEVER pushes to base_branch directly.

    Returns:
      {ok: True,  pr_url, branch, changes_count, files_changed}
      {ok: True,  no_changes: True}                  ← snapshot matches repo
      {ok: True,  dry_run: True, files_would_change, sample_diff}
      {ok: False, error}                             ← any failure
    """
    work = tempfile.mkdtemp(prefix='rapp-pr-')
    try:
        r = subprocess.run(['gh', 'repo', 'clone', owner_repo, work, '--', '--depth', '1'], capture_output=True, text=True, timeout=60)
        if r.returncode != 0:
            return {'ok': False, 'error': f'clone failed: {r.stderr.strip()[:300]}'}
        for cmd in (['git', '-C', work, 'config', 'user.name', 'RAPP Neighborhood Restore'], ['git', '-C', work, 'config', 'user.email', 'rapp-restore@noreply.kody-w.github.io']):
            subprocess.run(cmd, capture_output=True, timeout=10)
        applied = 0
        with tarfile.open(fileobj=io.BytesIO(tarball_bytes), mode='r:gz') as tf:
            for m in tf.getmembers():
                if not m.name.startswith(f'{twin_hash}/'):
                    continue
                rel = m.name[len(twin_hash) + 1:]
                if not rel:
                    continue
                base = os.path.basename(rel)
                if base.startswith('._') or base == '.DS_Store':
                    continue
                if rel.startswith('.git/') or '/.git/' in rel:
                    continue
                target_path = os.path.normpath(os.path.join(work, rel))
                if not target_path.startswith(os.path.normpath(work) + os.sep):
                    continue
                if m.isdir():
                    os.makedirs(target_path, exist_ok=True)
                elif m.isfile():
                    os.makedirs(os.path.dirname(target_path), exist_ok=True)
                    fh = tf.extractfile(m)
                    if fh is None:
                        continue
                    with open(target_path, 'wb') as out:
                        out.write(fh.read())
                    applied += 1
        r = subprocess.run(['git', '-C', work, 'status', '--porcelain'], capture_output=True, text=True, timeout=15)
        if r.returncode != 0:
            return {'ok': False, 'error': f'git status failed: {r.stderr.strip()[:200]}'}
        status_lines = [l for l in (r.stdout or '').splitlines() if l.strip()]
        if not status_lines:
            return {'ok': True, 'no_changes': True, 'message': 'snapshot already matches current repo state — no PR opened'}
        if dry_run:
            return {'ok': True, 'dry_run': True, 'files_would_change': len(status_lines), 'sample_diff': status_lines[:20], 'files_applied_from_tarball': applied}
        ts = time.strftime('%Y%m%d-%H%M%S')
        branch = f'{branch_prefix}/{ts}'
        title = pr_title or f'RAPP neighborhood-egg restore @ {ts}'
        body = pr_body or f'Automated PR opened by the NeighborhoodRun agent in github-write mode.\n\n- Twin hash: `{twin_hash}`\n- Files in tarball: {applied}\n- Files changed vs. main: {len(status_lines)}\n\nReview the diff carefully before merging.  This PR was opened by an automated egg hatch; it expresses *the snapshotted state* of this twin, which may or may not be what you want as the new authoritative version.'
        for cmd in (['git', '-C', work, 'checkout', '-b', branch], ['git', '-C', work, 'add', '-A'], ['git', '-C', work, 'commit', '-m', f'rapp neighborhood-egg restore @ {ts}'], ['git', '-C', work, 'push', '-u', 'origin', branch]):
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if r.returncode != 0:
                return {'ok': False, 'stage': cmd[3] if len(cmd) > 3 else '?', 'error': (r.stderr or r.stdout).strip()[:300]}
        r = subprocess.run(['gh', 'pr', 'create', '--repo', owner_repo, '--head', branch, '--base', base_branch, '--title', title, '--body', body], capture_output=True, text=True, timeout=30)
        if r.returncode != 0:
            return {'ok': False, 'error': f'PR create failed: {r.stderr.strip()[:300]}', 'branch_pushed': branch}
        pr_url = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else None
        return {'ok': True, 'pr_url': pr_url, 'branch': branch, 'changes_count': len(status_lines), 'files_applied': applied}
    finally:
        shutil.rmtree(work, ignore_errors=True)

def _extract_tarball_to_dir(tarball_bytes, target_dir):
    """Untar a gzipped tarball into target_dir. Returns (files_written, bytes_written)."""
    os.makedirs(target_dir, exist_ok=True)
    files_written = 0
    bytes_written = 0
    with tarfile.open(fileobj=io.BytesIO(tarball_bytes), mode='r:gz') as tf:
        for m in tf.getmembers():
            base = os.path.basename(m.name)
            if base.startswith('._') or base == '.DS_Store':
                continue
            target_path = os.path.normpath(os.path.join(target_dir, m.name))
            if not target_path.startswith(os.path.normpath(target_dir) + os.sep) and target_path != os.path.normpath(target_dir):
                continue
            tf.extract(m, target_dir)
            if m.isfile():
                files_written += 1
                bytes_written += m.size
    return (files_written, bytes_written)

_HOME = os.path.expanduser('~')

_TWIN_ROOT = os.path.join(_HOME, '.rapp', 'twins')

_DEFAULT_BRAINSTEM = os.environ.get('BRAINSTEM_URL', 'http://localhost:7071')

_DEFAULT_BRAINSTEM_DIR = os.environ.get('BRAINSTEM_DIR', '/Users/kodywildfeuer/Documents/GitHub/openrapp-desktop/python/openrapp')

_DEFAULT_AGENTS_DIR = os.environ.get('BRAINSTEM_AGENTS_DIR', os.path.join(_DEFAULT_BRAINSTEM_DIR, 'agents'))

_DEFAULT_BRAINSTEM_DATA = os.path.join(_DEFAULT_BRAINSTEM_DIR, '.brainstem_data')

_DEFAULT_GLOBAL_STATE = os.path.join(_HOME, '.brainstem')

_DEFAULT_EGGS_DIR = os.environ.get('EGGS_DIR', os.path.join(_HOME, 'Documents', 'GitHub', 'rappLocalFirstFleet', 'eggs'))

def _now_iso():
    return datetime.now(timezone.utc).astimezone().isoformat(timespec='seconds')

def _read_manifest(egg_path):
    with zipfile.ZipFile(egg_path, 'r') as zf:
        return (json.loads(zf.read('manifest.json').decode('utf-8')), zf.namelist())

def _resolve_egg(path_or_name):
    """Accept either an absolute path, a relative path, or a bare egg name."""
    if not path_or_name:
        return None
    p = os.path.expanduser(path_or_name)
    if os.path.exists(p):
        return p
    candidate = os.path.join(_DEFAULT_EGGS_DIR, path_or_name)
    if os.path.exists(candidate):
        return candidate
    if not path_or_name.endswith('.egg'):
        candidate = os.path.join(_DEFAULT_EGGS_DIR, path_or_name + '.egg')
        if os.path.exists(candidate):
            return candidate
    return None

def _bucket_entries(names):
    """Group egg entries by destination bucket."""
    buckets = {'brainstem_agents': [], 'brainstem_core': [], 'brainstem_data': [], 'global_state': [], 'twins': {}, 'peers': [], 'other': []}
    for n in names:
        if n.endswith('/'):
            continue
        if n in ('manifest.json', 'members.json'):
            continue
        if n.startswith('brainstem/agents/'):
            buckets['brainstem_agents'].append(n)
        elif n.startswith('brainstem/core/'):
            buckets['brainstem_core'].append(n)
        elif n.startswith('brainstem/data/'):
            buckets['brainstem_data'].append(n)
        elif n.startswith('brainstem/global_state/'):
            buckets['global_state'].append(n)
        elif n.startswith('brainstem/soul.md'):
            buckets['brainstem_core'].append(n)
        elif n.startswith('twins/'):
            parts = n.split('/', 2)
            if len(parts) >= 3:
                twin_hash = parts[1]
                buckets['twins'].setdefault(twin_hash, []).append(n)
        elif n.startswith('peers/'):
            buckets['peers'].append(n)
        else:
            buckets['other'].append(n)
    return buckets

def _dest_for(entry):
    """Map an egg entry name to its on-disk destination path."""
    if entry == 'brainstem/soul.md':
        return os.path.join(_DEFAULT_BRAINSTEM_DIR, 'soul.md')
    if entry.startswith('brainstem/agents/'):
        return os.path.join(_DEFAULT_AGENTS_DIR, entry[len('brainstem/agents/'):])
    if entry.startswith('brainstem/core/'):
        return os.path.join(_DEFAULT_BRAINSTEM_DIR, entry[len('brainstem/core/'):])
    if entry.startswith('brainstem/data/'):
        return os.path.join(_DEFAULT_BRAINSTEM_DATA, entry[len('brainstem/data/'):])
    if entry.startswith('brainstem/global_state/'):
        return os.path.join(_DEFAULT_GLOBAL_STATE, entry[len('brainstem/global_state/'):])
    if entry.startswith('twins/'):
        return os.path.join(_TWIN_ROOT, entry[len('twins/'):])
    return None

def _classify(entries, default_overwrite=False):
    """Return (would_create, would_overwrite, would_skip) lists of dest paths."""
    create, overwrite_, skip = ([], [], [])
    for e in entries:
        dest = _dest_for(e)
        if dest is None:
            continue
        if not os.path.exists(dest):
            create.append((e, dest))
        elif default_overwrite:
            overwrite_.append((e, dest))
        else:
            skip.append((e, dest))
    return (create, overwrite_, skip)

def _extract(zf, entry, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with zf.open(entry) as src, open(dest, 'wb') as out:
        out.write(src.read())

class NeighborhoodRunAgent(BasicAgent):

    def __init__(self):
        self.name = 'NeighborhoodRun'
        self.metadata = {'name': self.name, 'description': 'Hatch a neighborhood .egg: restore brainstem agents / core / memory / global state, restore every twin workspace, and (optionally) boot the twins that were alive when the snapshot was taken. Companion to NeighborhoodSnapshot.', 'parameters': {'type': 'object', 'properties': {'action': {'type': 'string', 'enum': ['inspect', 'plan', 'hatch', 'list_eggs'], 'description': 'inspect = show manifest; plan = dry-run; hatch = actually restore; list_eggs = enumerate.'}, 'egg': {'type': 'string', 'description': 'Egg file. Absolute path, relative path, or bare name (looked up in EGGS_DIR).'}, 'overwrite_agents': {'type': 'boolean', 'description': 'Replace brainstem/agents/*.py files that exist locally.'}, 'overwrite_core': {'type': 'boolean', 'description': 'Replace brainstem.py / local_storage.py / soul.md.'}, 'overwrite_data': {'type': 'boolean', 'description': 'Replace brainstem-level .brainstem_data memory.'}, 'overwrite_global_state': {'type': 'boolean', 'description': 'Replace ~/.brainstem allowlisted files.'}, 'overwrite_twins': {'type': 'boolean', 'description': 'Replace contents of ~/.rapp/twins/<hash>/.'}, 'boot_alive_twins': {'type': 'boolean', 'description': 'After restore, boot twins that were alive at snapshot. Default true.'}, 'only_twin_hashes': {'type': 'array', 'description': 'If set, only restore these twin hashes (others skipped).', 'items': {'type': 'string'}}, 'restore_peers': {'type': 'boolean', 'description': 'Process peer members (push to real peers, or extract for simulation). Default true.'}, 'overwrite_peer_twins': {'type': 'boolean', 'description': 'Replace peer-side twin workspaces. Default false (only fills gaps). Applies to both in-place and local-simulate targets.'}, 'only_peer_names': {'type': 'array', 'description': 'If set, only process these peers (by name from peers.json).', 'items': {'type': 'string'}}, 'target': {'type': 'string', 'enum': ['in-place', 'local-simulate'], 'description': "in-place (default): peer assets get pushed back via the peer's carrier (SSH for LAN peers, gh PR for github peers). local-simulate: peer assets get extracted into ~/.rapp/simulated/<peer>/twins/<hash>/ on THIS machine — no network. Use local-simulate to replay a federation offline."}, 'github_write_enabled': {'type': 'boolean', 'description': "For github-neighborhood peers under target=in-place: open a PR against each captured twin's source repo. Default false — github-write is opt-in because the blast radius is the public substrate."}, 'github_write_dry_run': {'type': 'boolean', 'description': 'Like github_write_enabled but stops before pushing/PR-ing — just reports what files would change. Useful before flipping the real flag.'}, 'github_branch_prefix': {'type': 'string', 'description': "Branch name prefix for github-write PRs (default: 'rapp-neighborhood-restore'). The full branch is <prefix>/<timestamp>."}, 'github_base_branch': {'type': 'string', 'description': "Base branch for the PR (default: 'main')."}}, 'required': ['action']}}
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action = kwargs.get('action')
        try:
            if action == 'inspect':
                return self._inspect(kwargs)
            if action == 'plan':
                return self._plan(kwargs)
            if action == 'hatch':
                return self._hatch(kwargs)
            if action == 'list_eggs':
                return self._list_eggs(kwargs)
            return json.dumps({'status': 'error', 'message': f'unknown action: {action}'})
        except Exception as e:
            return json.dumps({'status': 'error', 'action': action, 'message': str(e)})

    def _inspect(self, kwargs):
        egg = _resolve_egg(kwargs.get('egg'))
        if not egg:
            return json.dumps({'status': 'error', 'message': f"egg not found: {kwargs.get('egg')}"})
        manifest, names = _read_manifest(egg)
        return json.dumps({'status': 'success', 'action': 'inspect', 'egg_path': egg, 'egg_size': os.path.getsize(egg), 'file_count': len(names), 'manifest': manifest})

    def _plan(self, kwargs):
        egg = _resolve_egg(kwargs.get('egg'))
        if not egg:
            return json.dumps({'status': 'error', 'message': f"egg not found: {kwargs.get('egg')}"})
        manifest, names = _read_manifest(egg)
        buckets = _bucket_entries(names)
        only = set(kwargs.get('only_twin_hashes') or [])
        ov = {'agents': bool(kwargs.get('overwrite_agents')), 'core': bool(kwargs.get('overwrite_core')), 'data': bool(kwargs.get('overwrite_data')), 'global_state': bool(kwargs.get('overwrite_global_state')), 'twins': bool(kwargs.get('overwrite_twins'))}

        def counts(entries, overwrite):
            c, o, s = _classify(entries, overwrite)
            return {'create': len(c), 'overwrite': len(o), 'skip_existing': len(s)}
        twin_entries_flat = []
        for h, entries in buckets['twins'].items():
            if only and h not in only:
                continue
            twin_entries_flat.extend(entries)
        plan = {'brainstem_agents': counts(buckets['brainstem_agents'], ov['agents']), 'brainstem_core': counts(buckets['brainstem_core'], ov['core']), 'brainstem_data': counts(buckets['brainstem_data'], ov['data']), 'global_state': counts(buckets['global_state'], ov['global_state']), 'twins': counts(twin_entries_flat, ov['twins'])}
        alive_twins = [t for t in manifest.get('members', {}).get('local', {}).get('twins', []) if t.get('alive_at_snapshot') and (not only or t['hash'] in only)]
        return json.dumps({'status': 'success', 'action': 'plan', 'egg_path': egg, 'would': plan, 'would_boot': [{'hash': t['hash'], 'name': t['name'], 'port': t.get('port'), 'kind': t.get('kind')} for t in alive_twins], 'options': ov, 'filter': {'only_twin_hashes': sorted(only)} if only else {}})

    def _hatch(self, kwargs):
        egg = _resolve_egg(kwargs.get('egg'))
        if not egg:
            return json.dumps({'status': 'error', 'message': f"egg not found: {kwargs.get('egg')}"})
        manifest, names = _read_manifest(egg)
        buckets = _bucket_entries(names)
        only = set(kwargs.get('only_twin_hashes') or [])
        boot_alive = kwargs.get('boot_alive_twins', True)
        ov = {'agents': bool(kwargs.get('overwrite_agents')), 'core': bool(kwargs.get('overwrite_core')), 'data': bool(kwargs.get('overwrite_data')), 'global_state': bool(kwargs.get('overwrite_global_state')), 'twins': bool(kwargs.get('overwrite_twins'))}
        report = {'egg_path': egg, 'started_at': _now_iso(), 'restored': {}, 'boot_attempts': []}
        with zipfile.ZipFile(egg, 'r') as zf:
            sections = [('brainstem_agents', buckets['brainstem_agents'], ov['agents']), ('brainstem_core', buckets['brainstem_core'], ov['core']), ('brainstem_data', buckets['brainstem_data'], ov['data']), ('global_state', buckets['global_state'], ov['global_state'])]
            for label, entries, allow_overwrite in sections:
                created, overwritten, skipped = (0, 0, 0)
                for e in entries:
                    dest = _dest_for(e)
                    if dest is None:
                        continue
                    exists = os.path.exists(dest)
                    if exists and (not allow_overwrite):
                        skipped += 1
                        continue
                    _extract(zf, e, dest)
                    if exists:
                        overwritten += 1
                    else:
                        created += 1
                report['restored'][label] = {'created': created, 'overwritten': overwritten, 'skipped_existing': skipped}
            twin_created, twin_overwritten, twin_skipped = (0, 0, 0)
            twins_touched = set()
            for h, entries in buckets['twins'].items():
                if only and h not in only:
                    continue
                for e in entries:
                    dest = _dest_for(e)
                    if dest is None:
                        continue
                    exists = os.path.exists(dest)
                    if exists and (not ov['twins']):
                        twin_skipped += 1
                        continue
                    _extract(zf, e, dest)
                    twins_touched.add(h)
                    if exists:
                        twin_overwritten += 1
                    else:
                        twin_created += 1
            report['restored']['twins'] = {'twin_hashes_touched': sorted(twins_touched), 'files_created': twin_created, 'files_overwritten': twin_overwritten, 'files_skipped_existing': twin_skipped}
        restore_peers = kwargs.get('restore_peers', True)
        overwrite_peer_twins = bool(kwargs.get('overwrite_peer_twins', False))
        only_peer_names = set(kwargs.get('only_peer_names') or [])
        target = (kwargs.get('target') or 'in-place').lower()
        if target not in ('in-place', 'local-simulate'):
            target = 'in-place'
        report['target'] = target
        report['peers'] = []
        if restore_peers:
            peer_entries = manifest.get('members', {}).get('peers', [])
            with zipfile.ZipFile(egg, 'r') as zf:
                names_in_egg = set(zf.namelist())
                for p in peer_entries:
                    name = p.get('name') or p.get('url')
                    if only_peer_names and name not in only_peer_names:
                        continue
                    pr = {'name': name, 'url': p.get('url'), 'ssh_user': p.get('ssh_user'), 'ssh_host': p.get('ssh_host'), 'mode': target}
                    if target == 'in-place':
                        if p.get('ssh_user') and p.get('ssh_host'):
                            pass
                        elif p.get('github_neighborhood') or p.get('github_repos'):
                            github_write_enabled = bool(kwargs.get('github_write_enabled'))
                            github_write_dry_run = bool(kwargs.get('github_write_dry_run'))
                            if not (github_write_enabled or github_write_dry_run):
                                pr['skipped'] = "github-write disabled by default — pass github_write_enabled=true to open PRs against each captured twin's source repo, or github_write_dry_run=true to preview the diff without pushing. Also consider target=local-simulate."
                                report['peers'].append(pr)
                                continue
                            pr['mode'] = 'github-pr' + (' (dry-run)' if github_write_dry_run else '')
                            pr_results = []
                            twins_created = 0
                            twins_skipped = 0
                            twins_failed = []
                            for t in p.get('twins', []):
                                if not t.get('captured'):
                                    continue
                                if only and t['hash'] not in only:
                                    continue
                                src_repo = t.get('source')
                                arcname = t.get('captured_path_in_egg')
                                if not src_repo or not arcname or arcname not in names_in_egg:
                                    twins_failed.append({'hash': t['hash'], 'reason': 'missing_source_or_tarball'})
                                    continue
                                tarball = zf.read(arcname)
                                result = _github_pr_restore(owner_repo=src_repo, twin_hash=t['hash'], tarball_bytes=tarball, branch_prefix=kwargs.get('github_branch_prefix') or 'rapp-neighborhood-restore', base_branch=kwargs.get('github_base_branch') or 'main', dry_run=github_write_dry_run)
                                pr_results.append({'hash': t['hash'], 'name': t.get('name'), 'source_repo': src_repo, **result})
                                if result.get('ok'):
                                    if result.get('no_changes'):
                                        twins_skipped += 1
                                    elif result.get('dry_run'):
                                        twins_created += 1
                                    else:
                                        twins_created += 1
                                else:
                                    twins_failed.append({'hash': t['hash'], 'error': result.get('error', '?')})
                            pr['twins_created'] = twins_created
                            pr['twins_overwritten'] = 0
                            pr['twins_skipped_existing'] = twins_skipped
                            pr['twins_failed'] = twins_failed
                            pr['pr_results'] = pr_results
                            report['peers'].append(pr)
                            continue
                        else:
                            pr['skipped'] = 'no carrier coords (no ssh_user/ssh_host, no github_neighborhood/github_repos)'
                            report['peers'].append(pr)
                            continue
                        probe = _ssh_exec(p['ssh_user'], p['ssh_host'], 'echo ok', timeout=8)
                        pr['ssh_ok'] = probe['ok']
                        if not probe['ok']:
                            pr['error'] = probe['stderr'][:200]
                            report['peers'].append(pr)
                            continue
                        twins_created = 0
                        twins_overwritten = 0
                        twins_skipped = 0
                        twins_failed = []
                        for t in p.get('twins', []):
                            if not t.get('captured'):
                                continue
                            if only and t['hash'] not in only:
                                continue
                            arcname = t.get('captured_path_in_egg')
                            if not arcname or arcname not in names_in_egg:
                                twins_failed.append({'hash': t['hash'], 'reason': 'missing_in_egg'})
                                continue
                            check = _ssh_exec(p['ssh_user'], p['ssh_host'], f"test -d $HOME/.rapp/twins/{t['hash']} && echo EXISTS || echo MISSING", timeout=10)
                            exists_remote = 'EXISTS' in (check['stdout'] or '')
                            if exists_remote and (not overwrite_peer_twins):
                                twins_skipped += 1
                                continue
                            tarball = zf.read(arcname)
                            ssh_cmd = 'mkdir -p $HOME/.rapp/twins && cd $HOME/.rapp/twins && tar -xzf -'
                            res = _ssh_exec(p['ssh_user'], p['ssh_host'], ssh_cmd, timeout=120, stdin_bytes=tarball)
                            if res['ok']:
                                if exists_remote:
                                    twins_overwritten += 1
                                else:
                                    twins_created += 1
                            else:
                                twins_failed.append({'hash': t['hash'], 'stderr': res['stderr'][:200]})
                        pr['twins_created'] = twins_created
                        pr['twins_overwritten'] = twins_overwritten
                        pr['twins_skipped_existing'] = twins_skipped
                        pr['twins_failed'] = twins_failed
                    else:
                        peer_slug = (name or 'unnamed').replace('/', '_').replace(':', '_').replace(' ', '_')
                        peer_root = os.path.join(_SIMULATED_ROOT, peer_slug, 'twins')
                        pr['sim_root'] = peer_root
                        twins_created = 0
                        twins_overwritten = 0
                        twins_skipped = 0
                        twins_failed = []
                        for t in p.get('twins', []):
                            if not t.get('captured'):
                                continue
                            if only and t['hash'] not in only:
                                continue
                            arcname = t.get('captured_path_in_egg')
                            if not arcname or arcname not in names_in_egg:
                                twins_failed.append({'hash': t['hash'], 'reason': 'missing_in_egg'})
                                continue
                            twin_dest = os.path.join(peer_root, t['hash'])
                            exists_local_sim = os.path.isdir(twin_dest)
                            if exists_local_sim and (not overwrite_peer_twins):
                                twins_skipped += 1
                                continue
                            tarball = zf.read(arcname)
                            try:
                                fcount, bcount = _extract_tarball_to_dir(tarball, peer_root)
                                if exists_local_sim:
                                    twins_overwritten += 1
                                else:
                                    twins_created += 1
                            except Exception as ex:
                                twins_failed.append({'hash': t['hash'], 'error': str(ex)[:200]})
                        pr['twins_created'] = twins_created
                        pr['twins_overwritten'] = twins_overwritten
                        pr['twins_skipped_existing'] = twins_skipped
                        pr['twins_failed'] = twins_failed
                    report['peers'].append(pr)
        if boot_alive:
            alive_twins = [t for t in manifest.get('members', {}).get('local', {}).get('twins', []) if t.get('alive_at_snapshot') and (not only or t['hash'] in only)]
            twin_agent = self._resolve_twin_agent()
            for t in alive_twins:
                attempt = {'hash': t['hash'], 'name': t['name'], 'port': t.get('port')}
                if twin_agent is None:
                    attempt['ok'] = False
                    attempt['error'] = 'Twin agent not available in this brainstem'
                else:
                    try:
                        rappid_uuid = t.get('hash') or t['rappid']
                        out = twin_agent.perform(action='boot', rappid_uuid=rappid_uuid)
                        out_str = out if isinstance(out, str) else json.dumps(out)
                        looks_failed = 'Error:' in out_str or '"error"' in out_str.lower()
                        attempt['ok'] = not looks_failed
                        attempt['output'] = out_str[:800]
                    except Exception as ex:
                        attempt['ok'] = False
                        attempt['error'] = str(ex)
                report['boot_attempts'].append(attempt)
        report['finished_at'] = _now_iso()
        report['status'] = 'success'
        report['action'] = 'hatch'
        return json.dumps(report)

    def _list_eggs(self, kwargs):
        d = os.path.expanduser(kwargs.get('dir') or _DEFAULT_EGGS_DIR)
        if not os.path.isdir(d):
            return json.dumps({'status': 'success', 'action': 'list_eggs', 'dir': d, 'eggs': []})
        eggs = []
        for f in sorted(os.listdir(d)):
            if not f.endswith('.egg'):
                continue
            p = os.path.join(d, f)
            try:
                m, _ = _read_manifest(p)
                lm = m.get('members', {}).get('local', {})
                eggs.append({'file': f, 'path': p, 'size': os.path.getsize(p), 'name': m.get('name'), 'snapshotted_at': m.get('snapshotted_at'), 'snapshotted_from': m.get('snapshotted_from'), 'twins': len(lm.get('twins', [])), 'alive_at_snapshot': sum((1 for t in lm.get('twins', []) if t.get('alive_at_snapshot'))), 'agent_files': len(lm.get('agent_files_captured', [])), 'core_files': len(lm.get('core_files_captured', []))})
            except Exception as e:
                eggs.append({'file': f, 'path': p, 'error': str(e)})
        return json.dumps({'status': 'success', 'action': 'list_eggs', 'dir': d, 'eggs': eggs})

    def _resolve_twin_agent(self):
        """Locate the Twin agent in the running brainstem so we can boot twins."""
        try:
            from agents.twin_agent import TwinAgent
            return TwinAgent()
        except Exception:
            pass
        try:
            from agents import twin_agent
            for attr in dir(twin_agent):
                obj = getattr(twin_agent, attr)
                if isinstance(obj, type) and attr.lower().startswith('twin'):
                    return obj()
        except Exception:
            pass
        return None



# ─────────────────────────────────────────────────────────────────────
# Section: neighborhood_snapshot_agent.py
# ─────────────────────────────────────────────────────────────────────
_SSH_OPTS = ('-o', 'BatchMode=yes', '-o', 'ConnectTimeout=5', '-o', 'StrictHostKeyChecking=accept-new', '-o', 'ServerAliveInterval=10', '-o', 'ServerAliveCountMax=3')

def _ssh_exec(user, host, command, timeout=60, stdin=None, capture_bytes=False):
    """Run a shell command on a peer.  If capture_bytes=True, stdout is bytes; else text."""
    try:
        proc = subprocess.run(['ssh', *_SSH_OPTS, f'{user}@{host}', command], input=stdin, capture_output=True, text=not capture_bytes, timeout=timeout)
        return {'ok': proc.returncode == 0, 'stdout': proc.stdout, 'stderr': proc.stderr if not capture_bytes else proc.stderr.decode('utf-8', 'replace'), 'exit': proc.returncode}
    except subprocess.TimeoutExpired:
        return {'ok': False, 'stdout': b'' if capture_bytes else '', 'stderr': f'ssh timeout {timeout}s', 'exit': -1}
    except Exception as e:
        return {'ok': False, 'stdout': b'' if capture_bytes else '', 'stderr': str(e), 'exit': -2}

def _peer_tar_workspace(user, host, twin_hash):
    """Tarball a peer's ~/.rapp/twins/<hash>/ over SSH.  Returns raw .tar.gz bytes or None.
    COPYFILE_DISABLE=1 keeps macOS from emitting AppleDouble ._* resource-fork files."""
    cmd = f"COPYFILE_DISABLE=1 tar --exclude '._*' --exclude '.DS_Store' -czf - -C $HOME/.rapp/twins {twin_hash} 2>/dev/null"
    r = _ssh_exec(user, host, cmd, timeout=120, capture_bytes=True)
    if r['ok'] and r['stdout']:
        return r['stdout'] if isinstance(r['stdout'], bytes) else r['stdout'].encode('latin1', 'replace')
    return None

def _peer_list_twins(user, host):
    """List twin hashes registered on a peer."""
    r = _ssh_exec(user, host, 'ls $HOME/.rapp/twins/ 2>/dev/null', timeout=15)
    if not r['ok']:
        return []
    return [line.strip() for line in (r['stdout'] or '').splitlines() if line.strip() and (not line.startswith('.'))]

def _peer_twin_meta(user, host, twin_hash):
    """Get small metadata about a peer twin: rappid.json + soul presence + sizes + agents list."""
    cmd = f"H=$HOME/.rapp/twins/{twin_hash}; if [ -d $H ]; then   echo BEGIN_RAPPID; cat $H/rappid.json 2>/dev/null; echo END_RAPPID;   echo BEGIN_SOUL; [ -f $H/soul.md ] && echo 1 || echo 0; echo END_SOUL;   echo BEGIN_SIZE; du -sb $H 2>/dev/null | awk '{{print $1}}'; echo END_SIZE;   echo BEGIN_AGENTS; ls $H/agents/*.py 2>/dev/null | xargs -n1 basename 2>/dev/null; echo END_AGENTS;   echo BEGIN_FILES; find $H -type f 2>/dev/null | wc -l; echo END_FILES; fi"
    r = _ssh_exec(user, host, cmd, timeout=20)
    if not r['ok']:
        return None
    out = r['stdout'] or ''

    def _between(s, start, end):
        try:
            return s.split(start, 1)[1].split(end, 1)[0].strip()
        except IndexError:
            return ''
    rappid_raw = _between(out, 'BEGIN_RAPPID', 'END_RAPPID')
    soul_present = _between(out, 'BEGIN_SOUL', 'END_SOUL') == '1'
    size_str = _between(out, 'BEGIN_SIZE', 'END_SIZE')
    agents_raw = _between(out, 'BEGIN_AGENTS', 'END_AGENTS')
    files_str = _between(out, 'BEGIN_FILES', 'END_FILES')
    rappid_data = {}
    if rappid_raw:
        try:
            rappid_data = json.loads(rappid_raw)
        except Exception:
            pass
    return {'hash': twin_hash, 'rappid': rappid_data.get('rappid') or twin_hash, 'name': rappid_data.get('name') or rappid_data.get('slug') or twin_hash, 'kind': rappid_data.get('kind') or rappid_data.get('category') or 'unknown', 'workspace_bytes': int(size_str) if size_str.isdigit() else 0, 'workspace_files': int(files_str) if files_str.isdigit() else 0, 'has_soul': soul_present, 'agents': [a for a in agents_raw.splitlines() if a and (not a.startswith('_'))]}

def _peer_brainstem_agents(user, host):
    """Pull *_agent.py contents from a peer's brainstem agents dir."""
    r = _ssh_exec(user, host, 'ls $HOME/.brainstem/src/rapp_brainstem/agents/*.py 2>/dev/null', timeout=10)
    if not r['ok'] or not r['stdout']:
        return {}
    paths = [p.strip() for p in r['stdout'].splitlines() if p.strip()]
    files = {}
    for p in paths:
        name = os.path.basename(p)
        if name.startswith('_'):
            continue
        rd = _ssh_exec(user, host, f'cat {p}', timeout=15, capture_bytes=True)
        if rd['ok'] and rd['stdout']:
            content = rd['stdout'] if isinstance(rd['stdout'], bytes) else rd['stdout'].encode('utf-8', 'replace')
            files[name] = content
    return files

def _gh(args, timeout=30):
    """Run `gh` with args; return (ok, stdout, stderr)."""
    try:
        r = subprocess.run(['gh', *args], capture_output=True, text=True, timeout=timeout)
        return (r.returncode == 0, r.stdout, r.stderr)
    except subprocess.TimeoutExpired:
        return (False, '', f'gh timeout {timeout}s')
    except FileNotFoundError:
        return (False, '', 'gh CLI not found')
    except Exception as e:
        return (False, '', str(e))

def _gh_file_bytes(owner_repo, path, branch=None):
    """Fetch one file from a github repo via the contents API; return decoded bytes or None."""
    api = f'repos/{owner_repo}/contents/{path}'
    if branch:
        api = f'{api}?ref={branch}'
    ok, out, _ = _gh(['api', api, '--jq', '.content'], timeout=20)
    if not ok or not out.strip():
        return None
    try:
        return base64.b64decode(out.strip().replace('\n', ''))
    except Exception:
        return None

def _gh_list_tree(owner_repo, branch='main'):
    """Enumerate all file blob paths in a github repo at branch.
    Uses ?recursive=1 in the URL path because gh's -F flag implies POST."""
    ok, out, _ = _gh(['api', f'repos/{owner_repo}/git/trees/{branch}?recursive=1', '--jq', '.tree[] | select(.type == "blob") | .path'], timeout=30)
    if not ok or not out.strip():
        ok, out, _ = _gh(['api', f'repos/{owner_repo}/git/trees/HEAD?recursive=1', '--jq', '.tree[] | select(.type == "blob") | .path'], timeout=30)
    if not ok:
        return []
    return [line.strip() for line in out.splitlines() if line.strip()]

_V2_RAPPID_RE = re.compile('^rappid:v2:(?P<kind>[^:]+):@(?P<ns_owner>[^/]+)/(?P<ns_slug>[^:]+):(?P<hash>[a-f0-9]{32})@github\\.com/(?P<owner>[^/]+)/(?P<repo>.+)$')

def _parse_v2_rappid(rappid_str):
    """Parse v2 rappid → dict with owner/repo/hash/kind, or None for non-v2."""
    m = _V2_RAPPID_RE.match(rappid_str or '')
    if not m:
        return None
    g = m.groupdict()
    g['owner_repo'] = f"{g['owner']}/{g['repo']}"
    return g

def _gh_neighborhood_members(neighborhood_repo):
    """Read members.json from a neighborhood repo; return list of member dicts."""
    raw = _gh_file_bytes(neighborhood_repo, 'members.json')
    if not raw:
        return []
    try:
        data = json.loads(raw.decode('utf-8', 'replace'))
        return data.get('members', [])
    except Exception:
        return []

def _gh_build_twin_tarball(owner_repo, twin_hash):
    """Fetch a github twin repo's contents into a tar.gz with entries <hash>/<rel>.
    Same on-the-wire shape as the SSH carrier produces."""
    paths = _gh_list_tree(owner_repo)
    if not paths:
        return (None, 0)
    buf = io.BytesIO()
    files_written = 0
    with tarfile.open(fileobj=buf, mode='w:gz') as tf:
        di = tarfile.TarInfo(name=twin_hash)
        di.type = tarfile.DIRTYPE
        di.mode = 493
        tf.addfile(di)
        for rel in paths:
            if rel.startswith('.git/') or '/__pycache__/' in rel:
                continue
            if rel.endswith(('.pyc', '.DS_Store')) or os.path.basename(rel).startswith('._'):
                continue
            data = _gh_file_bytes(owner_repo, rel)
            if data is None:
                continue
            info = tarfile.TarInfo(name=f'{twin_hash}/{rel}')
            info.size = len(data)
            info.mode = 420
            tf.addfile(info, io.BytesIO(data))
            files_written += 1
    return (buf.getvalue(), files_written)

def _gh_neighborhood_meta_files(neighborhood_repo):
    """Capture the neighborhood-repo's own identity files (rappid, members,
    neighborhood, soul, README, card, holo) as a dict {rel_path: bytes}."""
    out = {}
    for rel in ('rappid.json', 'members.json', 'neighborhood.json', 'soul.md', 'README.md', 'card.json', 'holo.md'):
        b = _gh_file_bytes(neighborhood_repo, rel)
        if b is not None:
            out[rel] = b
    return out

_HOME = os.path.expanduser('~')

_TWIN_ROOT = os.path.join(_HOME, '.rapp', 'twins')

_PORT_DIR = os.path.join(_HOME, '.rapp', 'ports')

_PID_DIR = os.path.join(_HOME, '.rapp', 'pids')

_DEFAULT_BRAINSTEM = os.environ.get('BRAINSTEM_URL', 'http://localhost:7071')

_DEFAULT_BRAINSTEM_DIR = os.environ.get('BRAINSTEM_DIR', '/Users/kodywildfeuer/Documents/GitHub/openrapp-desktop/python/openrapp')

_DEFAULT_AGENTS_DIR = os.environ.get('BRAINSTEM_AGENTS_DIR', os.path.join(_DEFAULT_BRAINSTEM_DIR, 'agents'))

_DEFAULT_SOUL = os.environ.get('BRAINSTEM_SOUL', os.path.join(_DEFAULT_BRAINSTEM_DIR, 'soul.md'))

_DEFAULT_BRAINSTEM_DATA = os.path.join(_DEFAULT_BRAINSTEM_DIR, '.brainstem_data')

_DEFAULT_GLOBAL_STATE = os.path.join(_HOME, '.brainstem')

_DEFAULT_EGGS_DIR = os.environ.get('EGGS_DIR', os.path.join(_HOME, 'Documents', 'GitHub', 'rappLocalFirstFleet', 'eggs'))

_DEFAULT_PEERS_JSON = os.path.join(_HOME, '.rapp', 'peers.json')

_GLOBAL_STATE_ALLOWLIST = {'rappid.json', 'estate.json', 'self_healing_cron_state.json'}

_GLOBAL_STATE_DIRS_ALLOWLIST = {'peers'}

_GLOBAL_STATE_DENYLIST = {'private-estate-secret', 'private-estate-map.json', 'keys', 'venv', 'src', 'logs', 'brainstem.log', 'lifecycle.log'}

_BRAINSTEM_CORE_FILES = ('brainstem.py', 'local_storage.py', 'port.py', 'VERSION', 'requirements-brainstem.txt', '__init__.py')

def _now_iso():
    return datetime.now(timezone.utc).astimezone().isoformat(timespec='seconds')

def _safe_read(path, mode='r'):
    try:
        with open(path, mode) as f:
            return f.read()
    except OSError:
        return None

def _pid_alive(pid):
    try:
        os.kill(int(pid), 0)
        return True
    except (OSError, ValueError, TypeError):
        return False

def _http_get_json(url, timeout=3):
    try:
        with _urlreq.urlopen(url, timeout=timeout) as r:
            return json.loads(r.read().decode('utf-8', 'replace'))
    except Exception:
        return None

def _select_carrier(cfg):
    """Pick the carrier for a peer entry by which coord fields are present.
    First-match wins; LAN-SSH preferred when both SSH and GitHub coords are set
    (because SSH gives live state; GitHub gives source-of-truth)."""
    if cfg.get('ssh_user') and cfg.get('ssh_host'):
        return 'lan-ssh'
    if cfg.get('github_neighborhood'):
        return 'github-neighborhood'
    if cfg.get('github_repos') or cfg.get('github_repo'):
        return 'github-repos'
    return 'http-probe-only'

def _list_peers():
    """Read peer config: ~/.rapp/peers.json (preferred, supports ssh_user/ssh_host)
    or BRAINSTEM_PEERS env (comma-sep host:port).  Returns list of dicts:
    [{name, url, ssh_user, ssh_host}, ...]."""
    peers = []
    env = os.environ.get('BRAINSTEM_PEERS', '').strip()
    if env:
        for ent in env.split(','):
            ent = ent.strip()
            if not ent:
                continue
            if '://' not in ent:
                ent = f'http://{ent}'
            peers.append({'name': ent, 'url': ent, 'ssh_user': None, 'ssh_host': None})
    if os.path.exists(_DEFAULT_PEERS_JSON):
        try:
            with open(_DEFAULT_PEERS_JSON) as f:
                d = json.load(f)
            for p in d.get('peers', []):
                if isinstance(p, str):
                    url = p if '://' in p else f'http://{p}'
                    peers.append({'name': p, 'url': url, 'ssh_user': None, 'ssh_host': None})
                elif isinstance(p, dict) and (p.get('url') or p.get('github_neighborhood') or p.get('github_repos') or p.get('github_repo')):
                    peers.append({'name': p.get('name') or p.get('url') or p.get('github_neighborhood') or 'unnamed-peer', 'url': p.get('url'), 'ssh_user': p.get('ssh_user'), 'ssh_host': p.get('ssh_host'), 'github_neighborhood': p.get('github_neighborhood'), 'github_repos': p.get('github_repos') or ([p['github_repo']] if p.get('github_repo') else None)})
        except Exception:
            pass
    out, seen = ([], set())
    for p in peers:
        key = p.get('url') or p.get('github_neighborhood') or (p.get('github_repos') and p['github_repos'][0]) or p.get('name')
        if not key or key in seen:
            continue
        u = p.get('url') or ''
        if 'localhost' in u or '127.0.0.1' in u:
            continue
        seen.add(key)
        out.append(p)
    return out

def _walk_workspace(root):
    """Yield (rel_path, abs_path) for every file under root, skipping noise."""
    skip_dirs = {'.git', '__pycache__', 'node_modules', '.venv'}
    skip_suffixes = ('.pyc', '.pyo', '.DS_Store')
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        for name in filenames:
            if name.endswith(skip_suffixes):
                continue
            abs_path = os.path.join(dirpath, name)
            rel = os.path.relpath(abs_path, root)
            yield (rel, abs_path)

def _twin_metadata(twin_hash):
    """Read identity + liveness for a registered twin."""
    ws = os.path.join(_TWIN_ROOT, twin_hash)
    if not os.path.isdir(ws):
        return None
    rappid_path = os.path.join(ws, 'rappid.json')
    rappid_data = {}
    if os.path.exists(rappid_path):
        try:
            with open(rappid_path) as f:
                rappid_data = json.load(f)
        except Exception:
            pass
    port_file = os.path.join(_PORT_DIR, f'{twin_hash}.port')
    pid_file = os.path.join(_PID_DIR, f'{twin_hash}.pid')
    port = None
    pid = None
    alive = False
    if os.path.exists(port_file):
        try:
            port = int((_safe_read(port_file) or '').strip())
        except ValueError:
            port = None
    if os.path.exists(pid_file):
        try:
            pid = int((_safe_read(pid_file) or '').strip())
        except ValueError:
            pid = None
    if pid is not None:
        alive = _pid_alive(pid)
    size = 0
    file_count = 0
    agents_dir = os.path.join(ws, 'agents')
    agent_files = []
    if os.path.isdir(agents_dir):
        for f in sorted(os.listdir(agents_dir)):
            if f.endswith('.py') and (not f.startswith('_')):
                agent_files.append(f)
    brainstem_data_dir = os.path.join(ws, '.brainstem_data')
    has_memory = os.path.isdir(brainstem_data_dir)
    memory_files = []
    if has_memory:
        for dirpath, _, filenames in os.walk(brainstem_data_dir):
            for fn in filenames:
                if fn.endswith(('.pyc', '.DS_Store')):
                    continue
                rel = os.path.relpath(os.path.join(dirpath, fn), brainstem_data_dir)
                memory_files.append(rel)
    for _, abs_path in _walk_workspace(ws):
        try:
            size += os.path.getsize(abs_path)
            file_count += 1
        except OSError:
            pass
    return {'hash': twin_hash, 'rappid': rappid_data.get('rappid') or twin_hash, 'name': rappid_data.get('name') or rappid_data.get('slug') or twin_hash, 'kind': rappid_data.get('kind') or rappid_data.get('category') or 'unknown', 'port': port, 'pid': pid, 'alive_at_snapshot': alive, 'workspace_bytes': size, 'workspace_files': file_count, 'agents': agent_files, 'agent_count': len(agent_files), 'has_memory': has_memory, 'memory_files': memory_files, 'memory_file_count': len(memory_files), 'has_soul': os.path.exists(os.path.join(ws, 'soul.md')), 'has_rappid_json': os.path.exists(rappid_path), 'has_own_brainstem': os.path.exists(os.path.join(ws, 'brainstem.py'))}

def _list_local_twins():
    if not os.path.isdir(_TWIN_ROOT):
        return []
    out = []
    for name in sorted(os.listdir(_TWIN_ROOT)):
        if name.startswith('.'):
            continue
        meta = _twin_metadata(name)
        if meta is not None:
            out.append(meta)
    return out

class NeighborhoodSnapshotAgent(BasicAgent):

    def __init__(self):
        self.name = 'NeighborhoodSnapshot'
        self.metadata = {'name': self.name, 'description': 'Snapshot the entire local-and-network neighborhood (brainstem identity + all registered twin workspaces + reachable peers) into a single .egg file. Companion to NeighborhoodRun for later resurrection.', 'parameters': {'type': 'object', 'properties': {'action': {'type': 'string', 'enum': ['snapshot', 'inspect', 'list_eggs'], 'description': 'snapshot creates a new .egg; inspect reads an existing one; list_eggs enumerates the eggs dir.'}, 'name': {'type': 'string', 'description': 'Optional name for the snapshot (default: neighborhood-<timestamp>).'}, 'egg_path': {'type': 'string', 'description': 'For inspect: path to an existing .egg file.'}, 'include_twin_workspaces': {'type': 'boolean', 'description': 'If false, only capture twin metadata (no file copies). Default true.'}, 'include_stopped_twins': {'type': 'boolean', 'description': 'If false, only snapshot twins that were alive at snapshot time. Default true.'}, 'max_twin_bytes': {'type': 'number', 'description': 'Skip workspace files for twins above this size (default: 50_000_000 = 50MB per twin).'}}, 'required': ['action']}}
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action = kwargs.get('action')
        try:
            if action == 'snapshot':
                return self._snapshot(kwargs)
            if action == 'inspect':
                return self._inspect(kwargs)
            if action == 'list_eggs':
                return self._list_eggs(kwargs)
            return json.dumps({'status': 'error', 'message': f'unknown action: {action}'})
        except Exception as e:
            return json.dumps({'status': 'error', 'action': action, 'message': str(e)})

    def _snapshot(self, kwargs):
        name = kwargs.get('name') or f"neighborhood-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        include_workspaces = kwargs.get('include_twin_workspaces', True)
        include_stopped = kwargs.get('include_stopped_twins', True)
        include_brainstem_core = kwargs.get('include_brainstem_core', True)
        include_brainstem_data = kwargs.get('include_brainstem_data', True)
        include_global_state = kwargs.get('include_global_state', True)
        max_twin_bytes = int(kwargs.get('max_twin_bytes', 50000000))
        os.makedirs(_DEFAULT_EGGS_DIR, exist_ok=True)
        egg_path = os.path.join(_DEFAULT_EGGS_DIR, f'{name}.egg')
        local_health = _http_get_json(f'{_DEFAULT_BRAINSTEM}/health') or {}
        local_agents_dir = local_health.get('agents_path') or _DEFAULT_AGENTS_DIR
        local_soul_path = local_health.get('soul') or _DEFAULT_SOUL
        agent_files = []
        if os.path.isdir(local_agents_dir):
            for f in sorted(os.listdir(local_agents_dir)):
                if f.endswith('.py') and (not f.startswith('_')):
                    agent_files.append(f)
        twins = _list_local_twins()
        if not include_stopped:
            twins = [t for t in twins if t['alive_at_snapshot']]
        include_peer_workspaces = kwargs.get('include_peer_workspaces', True)
        peer_configs = _list_peers()
        peers_data = []
        peer_assets = []
        for cfg in peer_configs:
            health = _http_get_json(f"{cfg['url']}/health", timeout=2) if cfg.get('url') else None
            carrier = _select_carrier(cfg)
            entry = {'name': cfg['name'], 'url': cfg.get('url'), 'ssh_user': cfg.get('ssh_user'), 'ssh_host': cfg.get('ssh_host'), 'github_neighborhood': cfg.get('github_neighborhood'), 'github_repos': cfg.get('github_repos'), 'carrier': carrier, 'reachable_http': health is not None, 'health': health, 'probed_at': _now_iso(), 'ssh_ok': False, 'twins': [], 'agent_files': []}
            slug = (cfg['name'] or cfg.get('url') or 'peer').replace('/', '_').replace(':', '_').replace(' ', '_')
            if include_peer_workspaces and carrier == 'lan-ssh':
                probe = _ssh_exec(cfg['ssh_user'], cfg['ssh_host'], 'echo ok', timeout=8)
                entry['ssh_ok'] = probe['ok']
                if probe['ok']:
                    twin_hashes = _peer_list_twins(cfg['ssh_user'], cfg['ssh_host'])
                    for h in twin_hashes:
                        meta = _peer_twin_meta(cfg['ssh_user'], cfg['ssh_host'], h)
                        if meta is None:
                            continue
                        if meta['workspace_bytes'] > max_twin_bytes:
                            entry['twins'].append({**meta, 'captured': False, 'reason': 'oversize'})
                            continue
                        tarball = _peer_tar_workspace(cfg['ssh_user'], cfg['ssh_host'], h)
                        if tarball:
                            arcname = f'peers/{slug}/twins/{h}.tar.gz'
                            peer_assets.append((arcname, tarball))
                            entry['twins'].append({**meta, 'captured': True, 'captured_path_in_egg': arcname, 'captured_bytes': len(tarball)})
                        else:
                            entry['twins'].append({**meta, 'captured': False, 'reason': 'tar_failed'})
                    agent_blobs = _peer_brainstem_agents(cfg['ssh_user'], cfg['ssh_host'])
                    for name_, content in agent_blobs.items():
                        arcname = f'peers/{slug}/brainstem/agents/{name_}'
                        peer_assets.append((arcname, content))
                        entry['agent_files'].append(name_)
            elif include_peer_workspaces and carrier == 'github-neighborhood':
                nbh_repo = cfg['github_neighborhood']
                ok_probe, _, _ = _gh(['api', f'repos/{nbh_repo}'], timeout=8)
                entry['gh_ok'] = ok_probe
                if ok_probe:
                    for rel, blob in _gh_neighborhood_meta_files(nbh_repo).items():
                        peer_assets.append((f'peers/{slug}/neighborhood/{rel}', blob))
                    members = _gh_neighborhood_members(nbh_repo)
                    entry['github_neighborhood_repo'] = nbh_repo
                    entry['members_in_neighborhood'] = len(members)
                    for m in members:
                        parsed = _parse_v2_rappid(m.get('rappid', ''))
                        if not parsed:
                            entry['twins'].append({'rappid': m.get('rappid'), 'captured': False, 'reason': 'non-v2 rappid (cannot resolve to github repo)'})
                            continue
                        h = parsed['hash']
                        rappid_blob = _gh_file_bytes(parsed['owner_repo'], 'rappid.json')
                        try:
                            rappid_json = json.loads(rappid_blob.decode('utf-8', 'replace')) if rappid_blob else {}
                        except Exception:
                            rappid_json = {}
                        twin_repo_tree = _gh_list_tree(parsed['owner_repo'])
                        meta_entry = {'hash': h, 'rappid': m.get('rappid'), 'name': rappid_json.get('name') or parsed['ns_slug'], 'kind': parsed['kind'], 'source': parsed['owner_repo'], 'added_at': m.get('added_at'), 'via': m.get('via'), 'workspace_bytes': 0, 'workspace_files': len(twin_repo_tree), 'has_soul': 'soul.md' in twin_repo_tree, 'agents': [p.split('/', 1)[1] for p in twin_repo_tree if p.startswith('agents/') and p.endswith('.py')]}
                        if not twin_repo_tree:
                            entry['twins'].append({**meta_entry, 'captured': False, 'reason': 'empty_or_inaccessible_repo'})
                            continue
                        tarball, file_count = _gh_build_twin_tarball(parsed['owner_repo'], h)
                        if tarball is None:
                            entry['twins'].append({**meta_entry, 'captured': False, 'reason': 'build_failed'})
                            continue
                        arcname = f'peers/{slug}/twins/{h}.tar.gz'
                        peer_assets.append((arcname, tarball))
                        entry['twins'].append({**meta_entry, 'captured': True, 'captured_path_in_egg': arcname, 'captured_bytes': len(tarball), 'captured_files': file_count})
            peers_data.append(entry)
        brainstem_data_dir = local_health.get('brainstem_dir')
        brainstem_data_dir = os.path.join(brainstem_data_dir, '.brainstem_data') if brainstem_data_dir else _DEFAULT_BRAINSTEM_DATA
        brainstem_data_files = []
        if os.path.isdir(brainstem_data_dir):
            for dirpath, _, filenames in os.walk(brainstem_data_dir):
                for fn in filenames:
                    if fn.endswith(('.pyc', '.DS_Store')):
                        continue
                    rel = os.path.relpath(os.path.join(dirpath, fn), brainstem_data_dir)
                    brainstem_data_files.append(rel)
        global_state_files = []
        if os.path.isdir(_DEFAULT_GLOBAL_STATE):
            for name_in_dir in sorted(os.listdir(_DEFAULT_GLOBAL_STATE)):
                full = os.path.join(_DEFAULT_GLOBAL_STATE, name_in_dir)
                if name_in_dir in _GLOBAL_STATE_DENYLIST:
                    continue
                if os.path.isfile(full) and name_in_dir in _GLOBAL_STATE_ALLOWLIST:
                    global_state_files.append(name_in_dir)
                elif os.path.isdir(full) and name_in_dir in _GLOBAL_STATE_DIRS_ALLOWLIST:
                    for dirpath, _, filenames in os.walk(full):
                        for fn in filenames:
                            if fn.endswith(('.pyc', '.DS_Store')):
                                continue
                            rel = os.path.relpath(os.path.join(dirpath, fn), _DEFAULT_GLOBAL_STATE)
                            global_state_files.append(rel)
        brainstem_dir_eff = local_health.get('brainstem_dir') or _DEFAULT_BRAINSTEM_DIR
        core_files_present = [f for f in _BRAINSTEM_CORE_FILES if os.path.exists(os.path.join(brainstem_dir_eff, f))]
        manifest = {'schema': 'rapp-egg/2.0', 'scale': 'neighborhood', 'name': name, 'snapshotted_at': _now_iso(), 'snapshotted_from': socket.gethostname(), 'created_by': 'NeighborhoodSnapshot', 'members': {'local': {'host': socket.gethostname(), 'brainstem_url': _DEFAULT_BRAINSTEM, 'brainstem_dir': brainstem_dir_eff, 'brainstem_version': local_health.get('version'), 'loaded_agents': local_health.get('agents', []), 'model': local_health.get('model'), 'agent_files_captured': agent_files, 'core_files_captured': core_files_present if include_brainstem_core else [], 'brainstem_data_files': brainstem_data_files if include_brainstem_data else [], 'global_state_files': global_state_files if include_global_state else [], 'twins': twins}, 'peers': peers_data}, 'options': {'include_twin_workspaces': include_workspaces, 'include_stopped_twins': include_stopped, 'include_brainstem_core': include_brainstem_core, 'include_brainstem_data': include_brainstem_data, 'include_global_state': include_global_state, 'max_twin_bytes': max_twin_bytes, 'global_state_allowlist': sorted(_GLOBAL_STATE_ALLOWLIST | _GLOBAL_STATE_DIRS_ALLOWLIST), 'global_state_denylist': sorted(_GLOBAL_STATE_DENYLIST)}}
        files_written = 0
        bytes_written = 0
        twins_skipped_oversize = []
        with zipfile.ZipFile(egg_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
            zf.writestr('manifest.json', json.dumps(manifest, indent=2))
            zf.writestr('members.json', json.dumps(manifest['members'], indent=2))
            if os.path.exists(local_soul_path):
                soul = _safe_read(local_soul_path)
                if soul is not None:
                    zf.writestr('brainstem/soul.md', soul)
            if os.path.isdir(local_agents_dir):
                for f in agent_files:
                    src = os.path.join(local_agents_dir, f)
                    content = _safe_read(src)
                    if content is not None:
                        zf.writestr(f'brainstem/agents/{f}', content)
                        files_written += 1
                        bytes_written += len(content)
            if include_brainstem_core:
                for f in core_files_present:
                    src = os.path.join(brainstem_dir_eff, f)
                    content = _safe_read(src)
                    if content is not None:
                        zf.writestr(f'brainstem/core/{f}', content)
                        files_written += 1
                        bytes_written += len(content)
            if include_brainstem_data and os.path.isdir(brainstem_data_dir):
                for rel in brainstem_data_files:
                    abs_path = os.path.join(brainstem_data_dir, rel)
                    try:
                        with open(abs_path, 'rb') as fh:
                            data = fh.read()
                    except OSError:
                        continue
                    zf.writestr(f'brainstem/data/{rel}', data)
                    files_written += 1
                    bytes_written += len(data)
            if include_global_state and os.path.isdir(_DEFAULT_GLOBAL_STATE):
                for rel in global_state_files:
                    abs_path = os.path.join(_DEFAULT_GLOBAL_STATE, rel)
                    try:
                        with open(abs_path, 'rb') as fh:
                            data = fh.read()
                    except OSError:
                        continue
                    zf.writestr(f'brainstem/global_state/{rel}', data)
                    files_written += 1
                    bytes_written += len(data)
            if include_workspaces:
                for t in twins:
                    if t['workspace_bytes'] > max_twin_bytes:
                        twins_skipped_oversize.append({'hash': t['hash'], 'name': t['name'], 'size': t['workspace_bytes']})
                        continue
                    ws = os.path.join(_TWIN_ROOT, t['hash'])
                    for rel, abs_path in _walk_workspace(ws):
                        try:
                            with open(abs_path, 'rb') as fh:
                                data = fh.read()
                        except OSError:
                            continue
                        arcname = f"twins/{t['hash']}/{rel}"
                        zf.writestr(arcname, data)
                        files_written += 1
                        bytes_written += len(data)
            for p in peers_data:
                slug = (p['name'] or p['url']).replace('/', '_').replace(':', '_').replace(' ', '_')
                zf.writestr(f'peers/{slug}/peer.json', json.dumps(p, indent=2))
            for arcname, data in peer_assets:
                if isinstance(data, str):
                    data = data.encode('utf-8')
                zf.writestr(arcname, data)
                files_written += 1
                bytes_written += len(data)
        egg_size = os.path.getsize(egg_path)
        total_twin_agent_files = sum((t['agent_count'] for t in twins))
        total_twin_memory_files = sum((t['memory_file_count'] for t in twins))
        result = {'status': 'success', 'action': 'snapshot', 'egg_path': egg_path, 'egg_size': egg_size, 'files_in_egg': files_written + 1, 'uncompressed_bytes_captured': bytes_written, 'summary': {'local_brainstem': {'url': _DEFAULT_BRAINSTEM, 'agents_loaded': len(local_health.get('agents', [])), 'agent_files_captured': len(agent_files), 'core_files_captured': len(core_files_present) if include_brainstem_core else 0, 'brainstem_data_files': len(brainstem_data_files) if include_brainstem_data else 0, 'global_state_files': len(global_state_files) if include_global_state else 0}, 'twins_captured': len(twins), 'twins_alive_at_snapshot': sum((1 for t in twins if t['alive_at_snapshot'])), 'twins_with_own_brainstem': sum((1 for t in twins if t['has_own_brainstem'])), 'twins_with_memory': sum((1 for t in twins if t['has_memory'])), 'twin_agent_files_total': total_twin_agent_files, 'twin_memory_files_total': total_twin_memory_files, 'twins_skipped_oversize': twins_skipped_oversize, 'peers_probed': len(peers_data), 'peers_reachable': sum((1 for p in peers_data if p.get('reachable_http'))), 'peers_ssh_ok': sum((1 for p in peers_data if p.get('ssh_ok'))), 'peer_twins_captured': sum((1 for p in peers_data for t in p.get('twins', []) if t.get('captured'))), 'peer_brainstem_agent_files_captured': sum((len(p.get('agent_files', [])) for p in peers_data))}}
        return json.dumps(result)

    def _inspect(self, kwargs):
        egg_path = kwargs.get('egg_path')
        if not egg_path:
            return json.dumps({'status': 'error', 'message': 'egg_path required'})
        egg_path = os.path.expanduser(egg_path)
        if not os.path.exists(egg_path):
            return json.dumps({'status': 'error', 'message': f'not found: {egg_path}'})
        with zipfile.ZipFile(egg_path, 'r') as zf:
            try:
                manifest = json.loads(zf.read('manifest.json').decode('utf-8'))
            except KeyError:
                return json.dumps({'status': 'error', 'message': 'no manifest.json in egg'})
            names = zf.namelist()
        return json.dumps({'status': 'success', 'action': 'inspect', 'egg_path': egg_path, 'egg_size': os.path.getsize(egg_path), 'manifest': manifest, 'file_count': len(names), 'top_level': sorted(set((n.split('/')[0] for n in names)))})

    def _list_eggs(self, kwargs):
        d = os.path.expanduser(kwargs.get('dir') or _DEFAULT_EGGS_DIR)
        if not os.path.isdir(d):
            return json.dumps({'status': 'success', 'action': 'list_eggs', 'dir': d, 'eggs': []})
        eggs = []
        for f in sorted(os.listdir(d)):
            if not f.endswith('.egg'):
                continue
            p = os.path.join(d, f)
            try:
                with zipfile.ZipFile(p, 'r') as zf:
                    m = json.loads(zf.read('manifest.json').decode('utf-8'))
                eggs.append({'file': f, 'path': p, 'size': os.path.getsize(p), 'name': m.get('name'), 'snapshotted_at': m.get('snapshotted_at'), 'snapshotted_from': m.get('snapshotted_from'), 'twins': len(m.get('members', {}).get('local', {}).get('twins', [])), 'peers': len(m.get('members', {}).get('peers', []))})
            except Exception as e:
                eggs.append({'file': f, 'path': p, 'error': str(e)})
        return json.dumps({'status': 'success', 'action': 'list_eggs', 'dir': d, 'eggs': eggs})



# ─────────────────────────────────────────────────────────────────────
# Section: rar_remote_agent.py
# ─────────────────────────────────────────────────────────────────────
logger = logging.getLogger(__name__)

try:
    from utils.storage_factory import get_storage_manager
    _HAS_STORAGE = True
except ImportError:
    _HAS_STORAGE = False

class RARRemoteAgent(BasicAgent):
    """
    RAPP Remote Agent — browse, install, vote, review, and submit agents
    from the RAPP Agent Registry.

    Brainstem integration:
      - Reads GITHUB_TOKEN from environment (set by brainstem auth flow)
      - Falls back to `gh auth token` CLI if env var is missing
      - Uses storage_manager (when available) to cache registry locally
      - All GitHub API calls are authenticated for higher rate limits
      - Write operations (vote/review/submit) create Issues autonomously
    """
    REPO_OWNER = 'kody-w'
    REPO_NAME = 'RAR'
    REPO = f'{REPO_OWNER}/{REPO_NAME}'
    RAW_BASE = f'https://raw.githubusercontent.com/{REPO}/main'
    API_BASE = f'https://api.github.com/repos/{REPO}'
    API_MANIFEST_URL = f'{RAW_BASE}/api.json'
    TIER_ORDER = {'official': 0, 'verified': 1, 'community': 2, 'experimental': 3}
    CACHE_TTL_SECONDS = 300

    def __init__(self):
        self.name = 'RARRemoteAgent'
        self.metadata = {'name': self.name, 'description': "The native client for the RAPP Agent Registry. Discover, search, install, vote on, review, and submit single-file agent.py files from the open RAPP ecosystem. All actions are authenticated via the brainstem's GitHub session. Read actions work immediately; write actions (vote, review, submit) create GitHub Issues processed by the RAPP pipeline.", 'parameters': {'type': 'object', 'properties': {'action': {'type': 'string', 'description': "Action to perform. 'discover' — browse all agents (optional: category, tier filters). 'search' — find by keyword (REQUIRES query). 'get_info' — agent details (REQUIRES agent_name). 'leaderboard' — top agents by votes. 'reviews' — show reviews (REQUIRES agent_name). 'install' — download agent (REQUIRES agent_name). For type='stub' entries, resolves the bytes from the private repo declared in __source__ using your GitHub credentials. 'vote' — upvote/downvote (REQUIRES agent_name; optional: direction). 'review' — write review (REQUIRES agent_name, rating, text). 'submit' — submit new public agent (REQUIRES code). 'submit_upstream' — federate a local agent to the upstream RAR. 'federation_status' — show federation config. 'request_access' — ask the publisher to grant you access to a gated stub (REQUIRES agent_name; optional: use_case). 'publish_private' — generate and submit a .py.stub pointing at your private agent.py (REQUIRES agent_url; optional: dry_run). 'setup_private_rar' — scaffold + git-init + create a private GitHub repo for hosting gated agents (optional: repo_name, local_path, author, push, force).", 'enum': ['discover', 'search', 'get_info', 'leaderboard', 'reviews', 'install', 'vote', 'review', 'submit', 'submit_upstream', 'federation_status', 'request_access', 'publish_private', 'setup_private_rar']}, 'agent_name': {'type': 'string', 'description': "Full @publisher/slug name. Example: '@kody/rar_remote_agent'. Get this from discover or search results."}, 'query': {'type': 'string', 'description': "Search keyword for 'search' action."}, 'category': {'type': 'string', 'description': "Filter by category (e.g. 'core', 'pipeline', 'healthcare')."}, 'tier': {'type': 'string', 'description': 'Filter by quality tier.', 'enum': ['community', 'verified', 'official', 'experimental']}, 'direction': {'type': 'string', 'description': "Vote direction. Default: 'up'.", 'enum': ['up', 'down']}, 'rating': {'type': 'integer', 'description': "Star rating 1-5 for 'review' action."}, 'text': {'type': 'string', 'description': "Review text for 'review' action."}, 'code': {'type': 'string', 'description': "Agent source code for 'submit' action."}, 'output_dir': {'type': 'string', 'description': 'Directory to save installed agents. Default: ./agents/'}, 'use_case': {'type': 'string', 'description': "Optional 'why' text for 'request_access' — included in the issue body the publisher sees."}, 'agent_url': {'type': 'string', 'description': "For 'publish_private': a github.com/<owner>/<repo>/blob/<ref>/<path> URL (or matching raw.githubusercontent.com URL) pointing at your private agent.py."}, 'dry_run': {'type': 'boolean', 'description': "For 'publish_private': return the generated stub without submitting an issue."}, 'repo_name': {'type': 'string', 'description': "For 'setup_private_rar': name of the GitHub repo to create. Default: '<login>-private-rar'."}, 'local_path': {'type': 'string', 'description': "For 'setup_private_rar': local directory to scaffold into. Default: './<repo_name>'."}, 'author': {'type': 'string', 'description': "For 'setup_private_rar': name used in the sample agent's manifest. Default: '<login>'."}, 'push': {'type': 'boolean', 'description': "For 'setup_private_rar': if true, creates the private GitHub repo via gh CLI and pushes. Default: true."}, 'force': {'type': 'boolean', 'description': "For 'setup_private_rar': overwrite local_path if it already exists. Default: false."}}, 'required': ['action']}}
        super().__init__(name=self.name, metadata=self.metadata)
        self._upstream = None
        self._is_instance = False
        self._load_rar_config()
        self._registry_cache = None
        self._votes_cache = None
        self._reviews_cache = None
        self._cache_time = None
        self._storage = None
        if _HAS_STORAGE:
            try:
                self._storage = get_storage_manager()
            except Exception:
                pass

    def _load_rar_config(self):
        """Load rar.config.json if available to support federation."""
        config_paths = [os.path.join(os.path.dirname(__file__), '..', '..', 'rar.config.json'), 'rar.config.json']
        for path in config_paths:
            try:
                if os.path.exists(path):
                    with open(path) as f:
                        config = json.load(f)
                    self.REPO_OWNER = config.get('owner', self.REPO_OWNER)
                    self.REPO_NAME = config.get('repo', self.REPO_NAME)
                    self.REPO = f'{self.REPO_OWNER}/{self.REPO_NAME}'
                    self.RAW_BASE = f'https://raw.githubusercontent.com/{self.REPO}/main'
                    self.API_BASE = f'https://api.github.com/repos/{self.REPO}'
                    if config.get('role') == 'instance' and config.get('upstream'):
                        self._upstream = config['upstream']
                        self._is_instance = True
                    return
            except (OSError, json.JSONDecodeError):
                continue

    def _get_token(self):
        """
        Resolve the GitHub token using the brainstem's auth chain:
          1. GITHUB_TOKEN env var (set by brainstem during startup)
          2. Saved token file at .brainstem_data/.copilot_token
          3. `gh auth token` CLI fallback
        Returns token string or empty string.
        """
        token = os.environ.get('GITHUB_TOKEN', '')
        if token:
            return token
        token_paths = [os.path.join('.brainstem_data', '.copilot_token'), os.path.expanduser('~/.brainstem_data/.copilot_token')]
        for path in token_paths:
            try:
                if os.path.exists(path):
                    with open(path) as f:
                        saved = f.read().strip()
                    if saved:
                        return saved
            except OSError:
                continue
        try:
            result = subprocess.run(['gh', 'auth', 'token'], capture_output=True, text=True, timeout=5)
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass
        return ''

    def _build_headers(self, content_type=None):
        """Build HTTP headers, including auth token if available."""
        headers = {'User-Agent': 'RAR-Remote-Agent/1.1'}
        token = self._get_token()
        if token:
            headers['Authorization'] = f'Bearer {token}'
            headers['Accept'] = 'application/vnd.github.v3+json'
        if content_type:
            headers['Content-Type'] = content_type
        return headers

    def _fetch_json(self, url):
        """Fetch JSON from a URL with auth. Returns dict or None."""
        try:
            req = urllib.request.Request(url, headers=self._build_headers())
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read().decode())
        except Exception as e:
            logger.warning(f'Failed to fetch {url}: {e}')
            return None

    def _fetch_text(self, url):
        """Fetch raw text from a URL with auth."""
        req = urllib.request.Request(url, headers=self._build_headers())
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode()

    def _load_data(self, force=False):
        """Load registry + community state. Uses local cache when available."""
        if not force and self._registry_cache and self._cache_time:
            age = (datetime.now() - self._cache_time).total_seconds()
            if age < self.CACHE_TTL_SECONDS:
                return
        if self._storage and (not force):
            cached = self._read_local_cache()
            if cached:
                self._registry_cache, self._votes_cache, self._reviews_cache = cached
                self._cache_time = datetime.now()
                return
        self._registry_cache = self._fetch_json(f'{self.RAW_BASE}/registry.json')
        self._votes_cache = self._fetch_json(f'{self.RAW_BASE}/state/votes.json') or {'agents': {}}
        self._reviews_cache = self._fetch_json(f'{self.RAW_BASE}/state/reviews.json') or {'agents': {}}
        self._cache_time = datetime.now()
        if self._storage and self._registry_cache:
            self._write_local_cache()

    def _read_local_cache(self):
        """Read cached registry from brainstem's storage manager."""
        try:
            raw = self._storage.read_file('agent_catalogue', 'rar_registry_cache.json')
            if not raw:
                return None
            data = json.loads(raw)
            cached_at = data.get('_cached_at', '')
            if cached_at:
                age = (datetime.now() - datetime.fromisoformat(cached_at)).total_seconds()
                if age > self.CACHE_TTL_SECONDS:
                    return None
            return (data.get('registry'), data.get('votes', {'agents': {}}), data.get('reviews', {'agents': {}}))
        except Exception:
            return None

    def _write_local_cache(self):
        """Persist registry to brainstem's storage manager."""
        try:
            data = {'_cached_at': datetime.now().isoformat(), 'registry': self._registry_cache, 'votes': self._votes_cache, 'reviews': self._reviews_cache}
            self._storage.write_file('agent_catalogue', 'rar_registry_cache.json', json.dumps(data))
        except Exception as e:
            logger.debug(f'Could not write registry cache: {e}')

    def _agents(self):
        self._load_data()
        return (self._registry_cache or {}).get('agents', [])

    def _get_score(self, name):
        v = (self._votes_cache or {}).get('agents', {}).get(name, {})
        return v.get('score', 0)

    def _get_reviews(self, name):
        return (self._reviews_cache or {}).get('agents', {}).get(name, [])

    def _get_rating(self, name):
        revs = self._get_reviews(name)
        if not revs:
            return 0.0
        return sum((r.get('rating', 0) for r in revs)) / len(revs)

    def _create_issue(self, title, body_data):
        """
        Create a GitHub Issue with a JSON body.
        Uses the brainstem's implicit GitHub session.
        Returns issue URL or error string.
        """
        token = self._get_token()
        if not token:
            return 'Error: No GitHub token available. The brainstem should provide this automatically. If running standalone, set GITHUB_TOKEN or run `gh auth login`.'
        body_json = json.dumps(body_data, indent=2)
        issue_body = f'```json\n{body_json}\n```'
        payload = json.dumps({'title': f'[RAR] {title}', 'body': issue_body, 'labels': ['rar-action']}).encode()
        req = urllib.request.Request(f'{self.API_BASE}/issues', data=payload, headers=self._build_headers(content_type='application/json'), method='POST')
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                result = json.loads(resp.read().decode())
                return result.get('html_url', 'Issue created')
        except urllib.error.HTTPError as e:
            body = e.read().decode() if e.fp else str(e)
            logger.error(f'Issue creation failed: {e.code} — {body[:200]}')
            return f'Error creating issue: {e.code} — {body[:200]}'
        except Exception as e:
            return f'Error: {e}'

    def perform(self, **kwargs) -> str:
        action = kwargs.get('action', '')
        handlers = {'discover': self._discover, 'search': self._search, 'get_info': self._get_info, 'leaderboard': self._leaderboard, 'reviews': self._show_reviews, 'install': self._install, 'vote': self._vote, 'review': self._write_review, 'submit': self._submit, 'submit_upstream': self._submit_upstream, 'federation_status': self._federation_status, 'request_access': self._request_access, 'publish_private': self._publish_private, 'setup_private_rar': self._setup_private_rar}
        handler = handlers.get(action)
        if not handler:
            return f"Unknown action '{action}'. Valid: {', '.join(handlers.keys())}"
        try:
            return handler(kwargs)
        except Exception as e:
            logger.error(f'RARRemoteAgent error: {e}')
            return f'Error: {e}'

    def _discover(self, params):
        """Browse all agents with optional category/tier filters."""
        agents = self._agents()
        if not agents:
            return 'Error: Unable to fetch the RAPP registry.'
        category = params.get('category')
        tier = params.get('tier')
        filtered = list(agents)
        if category:
            filtered = [a for a in filtered if a.get('category') == category]
        if tier:
            filtered = [a for a in filtered if a.get('quality_tier') == tier]
        filtered.sort(key=lambda a: (self.TIER_ORDER.get(a.get('quality_tier', 'community'), 2), -self._get_score(a['name'])))
        stats = (self._registry_cache or {}).get('stats', {})
        total_votes = sum((v.get('up', 0) for v in (self._votes_cache or {}).get('agents', {}).values()))
        out = f"RAPP Agent Registry — {stats.get('total_agents', len(agents))} agents\n"
        out += f"Publishers: {stats.get('publishers', '?')} | "
        out += f"Categories: {stats.get('categories', '?')} | "
        out += f'Community votes: {total_votes}\n'
        out += '=' * 60 + '\n\n'
        for a in filtered[:30]:
            score = self._get_score(a['name'])
            rating = self._get_rating(a['name'])
            tier_label = a.get('quality_tier', 'community').upper()
            stars = f" | {'*' * round(rating)} {rating:.1f}" if rating > 0 else ''
            out += f"[{tier_label}] {a['display_name']} ({a['name']})\n"
            out += f"  v{a['version']} | {a.get('category', '?')} | "
            out += f"{a.get('_size_kb', '?')} KB | votes: {score}{stars}\n"
            out += f"  {a['description'][:100]}\n\n"
        if len(filtered) > 30:
            out += f'... and {len(filtered) - 30} more. Use search to narrow.\n'
        out += '\nActions: search, install, vote, review, submit, leaderboard\n'
        return out

    def _search(self, params):
        """Search agents by keyword."""
        query = (params.get('query') or '').lower()
        if not query:
            return "Error: 'query' is required for search."
        agents = self._agents()
        if not agents:
            return 'Error: Unable to fetch the RAPP registry.'
        results = []
        for a in agents:
            searchable = f"{a.get('name', '')} {a.get('display_name', '')} {a.get('description', '')} {' '.join(a.get('tags', []))} {a.get('author', '')} {a.get('category', '')}".lower()
            if query in searchable:
                score = 0
                if query in a.get('name', '').lower():
                    score += 10
                if query in a.get('display_name', '').lower():
                    score += 8
                if query in a.get('description', '').lower():
                    score += 5
                for tag in a.get('tags', []):
                    if query in tag.lower():
                        score += 3
                results.append((score, a))
        results.sort(key=lambda x: (-x[0], -self._get_score(x[1]['name'])))
        if not results:
            return f"No agents found for '{query}'.\nTry broader terms or use action='discover' to browse all."
        out = f"Search results for '{query}' — {len(results)} found\n"
        out += '-' * 50 + '\n\n'
        for _, a in results[:20]:
            score = self._get_score(a['name'])
            tier = a.get('quality_tier', 'community').upper()
            out += f"[{tier}] {a['display_name']}\n"
            out += f"  name: {a['name']} | v{a['version']} | votes: {score}\n"
            out += f"  {a['description'][:120]}\n"
            out += f"  Install: action='install', agent_name='{a['name']}'\n\n"
        return out

    def _get_info(self, params):
        """Get detailed info about a specific agent."""
        name = params.get('agent_name', '')
        if not name:
            return "Error: 'agent_name' is required."
        agents = self._agents()
        agent = next((a for a in agents if a['name'] == name), None)
        if not agent:
            return f"Agent '{name}' not found. Use action='search' to find it."
        score = self._get_score(name)
        revs = self._get_reviews(name)
        rating = self._get_rating(name)
        tier = agent.get('quality_tier', 'community')
        out = f"{'=' * 50}\n"
        out += f"{agent['display_name']}\n"
        out += f"{'=' * 50}\n\n"
        out += f"Name:        {agent['name']}\n"
        out += f"Version:     {agent['version']}\n"
        out += f"Author:      {agent.get('author', 'Unknown')}\n"
        out += f"Category:    {agent.get('category', 'Unknown')}\n"
        out += f'Quality:     {tier.upper()}'
        if tier == 'verified':
            out += ' [RAPP VERIFIED SEAL]'
        elif tier == 'experimental':
            out += ' [EXPERIMENTAL - USE AT YOUR OWN RISK]'
        out += '\n'
        out += f"Size:        {agent.get('_size_kb', '?')} KB ({agent.get('_lines', '?')} lines)\n"
        out += f'Votes:       {score}\n'
        out += f"Rating:      {'*' * round(rating)} {rating:.1f}/5 ({len(revs)} reviews)\n\n"
        out += f"Description:\n  {agent['description']}\n\n"
        if agent.get('tags'):
            out += f"Tags: {', '.join(agent['tags'])}\n\n"
        env = agent.get('requires_env', [])
        out += f"Env vars:    {(', '.join(env) if env else 'None')}\n"
        deps = agent.get('dependencies', [])
        out += f"Depends on:  {(', '.join(deps) if deps else 'None')}\n\n"
        raw_url = f"{self.RAW_BASE}/{agent['_file']}"
        out += f'Install:     curl -sO {raw_url}\n'
        out += f"Source:      https://github.com/{self.REPO}/blob/main/{agent['_file']}\n\n"
        if revs:
            out += f'Recent reviews:\n'
            for r in revs[-3:]:
                out += f"  @{r['user']} — {'*' * r['rating']} — {r['text'][:80]}\n"
        return out

    def _leaderboard(self, params):
        """Show top agents by votes."""
        agents = self._agents()
        if not agents:
            return 'Error: Unable to fetch the RAPP registry.'
        ranked = sorted(agents, key=lambda a: (-self._get_score(a['name']), -self._get_rating(a['name'])))
        out = 'RAPP Agent Leaderboard\n'
        out += '=' * 55 + '\n'
        out += f"{'#':>3}  {'Agent':<30} {'Tier':<10} {'Votes':>5}  {'Rating':>6}\n"
        out += '-' * 55 + '\n'
        for i, a in enumerate(ranked[:25], 1):
            score = self._get_score(a['name'])
            rating = self._get_rating(a['name'])
            tier = a.get('quality_tier', 'community')[:8]
            stars = f'{rating:.1f}' if rating > 0 else '  —'
            out += f"{i:>3}  {a['display_name'][:30]:<30} {tier:<10} {score:>5}  {stars:>6}\n"
        return out

    def _show_reviews(self, params):
        """Show all reviews for an agent."""
        name = params.get('agent_name', '')
        if not name:
            return "Error: 'agent_name' is required."
        self._load_data()
        revs = self._get_reviews(name)
        if not revs:
            return f"No reviews yet for {name}. Be the first: action='review'"
        out = f'Reviews for {name} ({len(revs)})\n'
        out += '-' * 40 + '\n\n'
        for r in revs:
            ts = r.get('timestamp', '')[:10]
            out += f"@{r['user']} — {'*' * r['rating']} ({r['rating']}/5) — {ts}\n"
            out += f"  {r['text']}\n\n"
        return out

    def _resolve_private_source(self, src: dict) -> str:
        """Fetch agent bytes from a private repo via the GitHub contents API.
        Uses the brainstem's existing token. Returns the file's text.
        Raises with a clean access-denied message if the user can't read
        the repo (GitHub returns 404 for unauthorized reads on private
        repos — that is intentional and not a bug). """
        stype = src.get('type')
        if stype not in ('github_private', 'github_public'):
            raise ValueError(f'Unsupported source type: {stype}')
        repo = src.get('repo', '')
        path = src.get('path', '')
        ref = src.get('ref', 'main')
        if not repo or not path:
            raise ValueError("source missing 'repo' or 'path'")
        url = f'https://api.github.com/repos/{repo}/contents/{path}?ref={ref}'
        headers = self._build_headers()
        headers['Accept'] = 'application/vnd.github.raw'
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                return resp.read().decode()
        except urllib.error.HTTPError as e:
            if e.code in (401, 403, 404):
                raise PermissionError(f"Access denied to {repo}/{path} (HTTP {e.code}). You need read access to the private repo '{repo}'. Authenticate with `gh auth login` or set GITHUB_TOKEN.")
            raise

    def _install(self, params):
        """Download an agent file to the local filesystem.
        For stub entries (type=='stub') the bytes are fetched from the
        private repo declared in __source__ using the user's own GitHub
        credentials — public RAR only ever hosts the stub manifest."""
        name = params.get('agent_name', '')
        if not name:
            return "Error: 'agent_name' is required."
        agents = self._agents()
        agent = next((a for a in agents if a['name'] == name), None)
        if not agent:
            return f"Agent '{name}' not found. Use action='search' first."
        output_dir = params.get('output_dir', 'agents')
        is_stub = agent.get('type') == 'stub'
        if is_stub:
            src = agent.get('_source') or {}
            try:
                code = self._resolve_private_source(src)
            except PermissionError as e:
                return f"Locked: {agent['display_name']}\n\n{e}\n\nThis is a gated agent — the listing is public but the source\nis hosted in a private repo. If you should have access, check\nthat your GitHub account has been granted read access to:\n  {src.get('repo', '?')}\n\nTo ask the publisher for access, run:\n  action='request_access', agent_name='{name}'\n"
            except Exception as e:
                return f'Error resolving private source: {e}'
            filename = src.get('path', '').split('/')[-1] or f"{name.split('/')[-1]}.py"
        else:
            raw_url = f"{self.RAW_BASE}/{agent['_file']}"
            filename = agent['_file'].split('/')[-1]
            try:
                code = self._fetch_text(raw_url)
            except Exception as e:
                return f'Error downloading agent: {e}'
        try:
            os.makedirs(output_dir, exist_ok=True)
            filepath = os.path.join(output_dir, filename)
            with open(filepath, 'w') as f:
                f.write(code)
        except Exception as e:
            return f'Error saving agent: {e}'
        if self._storage:
            try:
                self._storage.write_file('agents', filename, code)
            except Exception:
                pass
        tier = agent.get('quality_tier', 'community').upper()
        score = self._get_score(name)
        out = f"Installed: {agent['display_name']} [{tier}]\n\n"
        out += f"Name:     {agent['name']} v{agent['version']}\n"
        out += f'Saved to: {filepath}\n'
        out += f"Size:     {agent.get('_size_kb', '?')} KB\n"
        out += f'Votes:    {score}\n'
        out += f"Author:   {agent.get('author', 'Unknown')}\n\n"
        if agent.get('requires_env'):
            out += f"Required env vars: {', '.join(agent['requires_env'])}\n"
            out += 'Set these before using the agent.\n\n'
        out += 'Ready to use.\n'
        return out

    def _request_access(self, params):
        """Open a GitHub Issue on public RAR asking the gated agent's
        publisher to grant the requester read access to the private repo.
        The issue @-mentions the publisher (extracted from the source
        repo owner) so they get notified the standard way. Only valid
        for type='stub' agents — regular agents don't need access."""
        name = params.get('agent_name', '')
        use_case = (params.get('use_case') or '').strip()
        if not name:
            return "Error: 'agent_name' is required."
        agents = self._agents()
        agent = next((a for a in agents if a['name'] == name), None)
        if not agent:
            return f"Agent '{name}' not found. Use action='search' first."
        if agent.get('type') != 'stub':
            return f"'{name}' is not a gated agent — no access request needed. Use action='install' to fetch it."
        src = agent.get('_source') or {}
        repo = src.get('repo') or ''
        path = src.get('path') or ''
        publisher = repo.split('/')[0] if '/' in repo else repo
        if not publisher:
            return f"Cannot determine publisher for '{name}' — source repo missing."
        token = self._get_token()
        if not token:
            return 'Error: No GitHub token available. The brainstem should set this; if running standalone, run `gh auth login` or set GITHUB_TOKEN.'
        body_lines = [f'Hi @{publisher},', '', f"I'd like access to **{agent['display_name']}** (`{name}`).", '', f'Source: `{repo}/{path}`', '', f'If granted, please add me as a read collaborator on `{repo}` so the brainstem can resolve the bytes on install.']
        if use_case:
            body_lines += ['', f'Use case: {use_case}']
        payload = json.dumps({'title': f'[RAR] request: access to {name}', 'body': '\n'.join(body_lines), 'labels': ['request-access', 'rar-action']}).encode()
        req = urllib.request.Request(f'{self.API_BASE}/issues', data=payload, headers=self._build_headers(content_type='application/json'), method='POST')
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                result = json.loads(resp.read().decode())
                url = result.get('html_url', 'Issue created')
                return f"Access request opened for {name}.\nPublisher @{publisher} has been notified.\nIssue: {url}\n\nNext: wait for @{publisher} to add you as a read collaborator on {repo}, then retry action='install'."
        except urllib.error.HTTPError as e:
            body = e.read().decode() if e.fp else str(e)
            return f'Error creating issue: {e.code} — {body[:200]}'
        except Exception as e:
            return f'Error: {e}'

    def _parse_github_blob_url(self, url: str) -> dict | None:
        """Parse a GitHub blob or raw URL into source-pointer components.
        Accepts:
          https://github.com/<owner>/<repo>/blob/<ref>/<path>
          https://raw.githubusercontent.com/<owner>/<repo>/<ref>/<path>
        Returns {repo, ref, path} or None if it doesn't look like one."""
        if not url:
            return None
        u = url.strip()
        m = None
        if 'github.com/' in u and '/blob/' in u:
            tail = u.split('github.com/', 1)[1]
            owner_repo, _, rest = tail.partition('/blob/')
            ref, _, path = rest.partition('/')
            if owner_repo.count('/') == 1 and ref and path:
                m = {'repo': owner_repo, 'ref': ref, 'path': path}
        elif 'raw.githubusercontent.com/' in u:
            tail = u.split('raw.githubusercontent.com/', 1)[1]
            parts = tail.split('/', 3)
            if len(parts) == 4:
                m = {'repo': f'{parts[0]}/{parts[1]}', 'ref': parts[2], 'path': parts[3]}
        return m

    def _publish_private(self, params):
        """Submit a gated stub to public RAR by pointing at a private
        agent.py URL. The flow:
          1. Parse the GitHub URL into (repo, ref, path).
          2. Fetch the agent.py via the contents API using YOUR token.
             If you don't have access, GitHub returns 404 — proves you
             can't publish someone else's gated agent.
          3. AST-extract __manifest__ from the fetched code.
          4. Render the matching .py.stub source.
          5. Open a GitHub Issue on public RAR carrying the stub.
        Args:
          agent_url: GitHub blob or raw URL to the private agent.py.
          dry_run:   if truthy, returns the stub source without opening
                     an issue.
        """
        url = params.get('agent_url', '').strip()
        dry_run = bool(params.get('dry_run', False))
        if not url:
            return "Error: 'agent_url' is required (a github.com/<owner>/<repo>/blob/<ref>/<path> URL)."
        parts = self._parse_github_blob_url(url)
        if not parts:
            return "Error: Could not parse 'agent_url'. Expected a URL like https://github.com/owner/repo/blob/main/agents/@you/foo_agent.py or the matching raw.githubusercontent.com form."
        src = {'schema': 'rapp-source/1.0', 'type': 'github_private', 'repo': parts['repo'], 'ref': parts['ref'], 'path': parts['path']}
        try:
            code = self._resolve_private_source(src)
        except PermissionError as e:
            return f"Cannot publish: {e}\n\nYou can only publish a stub for an agent you can read. Confirm you have access to {src['repo']}, then retry."
        except Exception as e:
            return f'Error fetching agent source: {e}'
        try:
            import ast as _ast
            tree = _ast.parse(code)
            manifest = None
            for node in _ast.walk(tree):
                if isinstance(node, _ast.Assign):
                    for t in node.targets:
                        if isinstance(t, _ast.Name) and t.id == '__manifest__':
                            try:
                                manifest = _ast.literal_eval(node.value)
                            except (ValueError, TypeError):
                                pass
                if manifest:
                    break
        except SyntaxError as e:
            return f'Error: agent source has syntax errors — {e}'
        if not isinstance(manifest, dict):
            return 'Error: could not extract __manifest__ dict from the agent source.'
        required = ['schema', 'name', 'version', 'display_name', 'description', 'author', 'tags', 'category']
        missing = [f for f in required if f not in manifest]
        if missing:
            return f'Error: manifest is missing required fields: {missing}'
        manifest['quality_tier'] = 'private'

        def _render(d):
            lines = ['{']
            for k, v in d.items():
                lines.append(f'    {repr(k)}: {repr(v)},')
            lines.append('}')
            return '\n'.join(lines)
        docstring = f'''"""\nGated stub for {manifest['name']} — bytes live in the private repo\n{src['repo']} at {src['path']}. Public RAR carries only this\nmanifest pointer; the brainstem resolves the source at install\ntime using the installer's own GitHub credentials.\n"""\n\n'''
        stub_src = docstring + '__manifest__ = ' + _render(manifest) + '\n\n' + '__source__ = ' + _render(src) + '\n'
        if dry_run:
            return f"Dry run — stub generated for {manifest['name']}:\n\n{stub_src}\nTo actually submit, re-run without dry_run."
        publisher = manifest['name'].split('/')[0]
        slug_basename = src['path'].rsplit('/', 1)[-1]
        stub_path = f'agents/{publisher}/private/{slug_basename}.stub'
        result = self._create_issue(f"submit_stub: {manifest['name']}", {'action': 'submit_stub', 'payload': {'name': manifest['name'], 'stub_path': stub_path, 'stub_source': stub_src, 'source': src}})
        if result.startswith('Error'):
            return result
        return f"Gated stub submitted for {manifest['name']}.\nIssue: {result}\n\nThe submission contains the .py.stub ready to land at:\n  {stub_path}\n\nWhat happens next:\n  - A maintainer (or the pipeline, when stub support lands) reviews and merges the stub.\n  - Once merged, your agent appears in public RAR as LOCKED.\n  - Anyone with read access to {src['repo']} can install it; anyone else sees a clean access-denied message."
    PRIVATE_RAR_TEMPLATE_FILES = [{'src': 'README.md', 'dst': 'README.md', 'substitute': False}, {'src': 'rar.config.json', 'dst': 'rar.config.json', 'substitute': True}, {'src': 'build_local_registry.py', 'dst': 'build_local_registry.py', 'substitute': False}, {'src': 'submit_to_public_rar.md', 'dst': 'submit_to_public_rar.md', 'substitute': False}, {'src': 'agents/@yourname/sample_private_agent.py', 'dst': 'agents/@{login}/sample_private_agent.py', 'substitute': True}, {'src': '.github/workflows/build-private-registry.yml', 'dst': '.github/workflows/build-private-registry.yml', 'substitute': False}]

    def _gh_login(self) -> str | None:
        """Resolve the authenticated user's GitHub login. Tries `gh api user`
        first (most reliable), then a token-authed call to api.github.com/user."""
        try:
            r = subprocess.run(['gh', 'api', 'user', '--jq', '.login'], capture_output=True, text=True, timeout=10)
            if r.returncode == 0 and r.stdout.strip():
                return r.stdout.strip()
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass
        try:
            req = urllib.request.Request('https://api.github.com/user', headers=self._build_headers())
            with urllib.request.urlopen(req, timeout=10) as resp:
                return json.loads(resp.read().decode()).get('login')
        except Exception:
            return None

    def _setup_private_rar(self, params):
        """One-shot scaffold of a private RAR: fetch the template from public
        RAR (so it's always up-to-date), write it under `local_path`, init
        git, and — unless `push=False` — create a private GitHub repo and
        push the scaffold to it.

        Args:
          repo_name:  name of the GitHub repo to create. Default: '<login>-private-rar'.
          local_path: where to scaffold on disk. Default: './<repo_name>'.
          author:     "Your Name" replacement in the sample agent. Default: '<login>'.
          push:       create + push to GitHub via `gh repo create --private`. Default: True.
          force:      overwrite local_path if it exists. Default: False.
        """
        login = self._gh_login()
        if not login:
            return 'Error: Could not determine your GitHub login. Run `gh auth login` or set GITHUB_TOKEN to a token with `read:user` scope, then retry.'
        repo_name = params.get('repo_name') or f'{login}-private-rar'
        local_path = params.get('local_path') or f'./{repo_name}'
        author = params.get('author') or login
        push = params.get('push', True)
        if isinstance(push, str):
            push = push.lower() not in ('false', '0', 'no')
        force = bool(params.get('force', False))
        replacements = [('yourname/yourname-private-rar', f'{login}/{repo_name}'), ('yourname-private-rar', repo_name), ('@yourname', f'@{login}'), ('"yourname"', f'"{login}"'), ('Your Name', author)]
        local = os.path.abspath(local_path)
        if os.path.exists(local):
            if not force:
                return f'Error: {local} already exists. Pass force=True to overwrite, or pick a different local_path.'
            if not os.path.exists(os.path.join(local, 'rar.config.json')):
                return f"Error: {local} exists but doesn't look like a private RAR (no rar.config.json). Refusing to overwrite. Choose another path."
        os.makedirs(local, exist_ok=True)
        written = []
        errors = []
        for entry in self.PRIVATE_RAR_TEMPLATE_FILES:
            src_url = f"{self.RAW_BASE}/private-rar-template/{entry['src']}"
            try:
                content = self._fetch_text(src_url)
            except Exception as e:
                errors.append(f"fetch {entry['src']}: {e}")
                continue
            if entry['substitute']:
                for old, new in replacements:
                    content = content.replace(old, new)
            dst_rel = entry['dst'].format(login=login)
            dst_abs = os.path.join(local, dst_rel)
            os.makedirs(os.path.dirname(dst_abs), exist_ok=True)
            with open(dst_abs, 'w') as f:
                f.write(content)
            written.append(dst_rel)
        ns_dir = os.path.join(local, f'agents/@{login}')
        os.makedirs(ns_dir, exist_ok=True)
        keep_path = os.path.join(ns_dir, '.gitkeep')
        if not os.path.exists(keep_path):
            with open(keep_path, 'w') as f:
                f.write('')
            written.append(f'agents/@{login}/.gitkeep')
        if errors:
            return f'Setup partial — fetched {len(written)} files, {len(errors)} failures:\n  ' + '\n  '.join(errors) + f'\n\nNothing was pushed. Resolve the fetch errors and retry.'
        if not push:
            return f"Scaffolded {len(written)} files under {local}\n\nNext steps (manual):\n  cd {local}\n  git init && git add . && git commit -m 'Initial scaffold'\n  gh repo create {login}/{repo_name} --private --source=. --push\n\nOr re-run setup_private_rar with push=True to do this automatically."
        try:
            subprocess.run(['gh', '--version'], capture_output=True, timeout=5, check=True)
        except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
            return f"Scaffolded {len(written)} files under {local}, but `gh` CLI is not available — cannot push automatically.\n\nInstall gh (https://cli.github.com) then run:\n  cd {local}\n  git init && git add . && git commit -m 'Initial scaffold'\n  gh repo create {login}/{repo_name} --private --source=. --push"

        def _run(cmd, **kw):
            return subprocess.run(cmd, capture_output=True, text=True, timeout=60, cwd=local, **kw)
        steps = [['git', 'init', '-q'], ['git', 'add', '.'], ['git', '-c', 'commit.gpgsign=false', 'commit', '-q', '-m', 'Initial scaffold — created by @kody/rar_remote_agent setup_private_rar'], ['gh', 'repo', 'create', f'{login}/{repo_name}', '--private', '--source=.', '--push', '--remote=origin']]
        for step in steps:
            r = _run(step)
            if r.returncode != 0:
                tail = (r.stderr or r.stdout).strip().splitlines()[-1:]
                return f"Setup failed at: {' '.join(step)}\n  {(tail[0] if tail else '(no output)')}\n\nLocal files are at {local} — re-run the failing command manually, or delete the directory and retry with force=True."
        repo_url = f'https://github.com/{login}/{repo_name}'
        return f"Private RAR ready.\n\n  Local:  {local}\n  Remote: {repo_url}  (private)\n  Files:  {len(written)} scaffolded\n\nTo publish your first gated agent:\n  1. Drop your agent.py into {local}/agents/@{login}/\n  2. git add . && git commit -m 'add my agent' && git push\n  3. action='publish_private', agent_url='{repo_url}/blob/main/agents/@{login}/<your_agent>.py'\n"

    def _vote(self, params):
        """Upvote or downvote an agent via GitHub Issue."""
        name = params.get('agent_name', '')
        direction = params.get('direction', 'up')
        if not name:
            return "Error: 'agent_name' is required."
        if direction not in ('up', 'down'):
            return "Error: 'direction' must be 'up' or 'down'."
        result = self._create_issue(f'vote: {name}', {'action': 'vote', 'payload': {'agent': name, 'direction': direction}})
        if result.startswith('Error'):
            return result
        return f'Vote ({direction}) recorded for {name}.\nIssue: {result}\nThe RAPP pipeline will process this shortly.'

    def _write_review(self, params):
        """Submit a review via GitHub Issue."""
        name = params.get('agent_name', '')
        rating = params.get('rating')
        text = params.get('text', '')
        if not name:
            return "Error: 'agent_name' is required."
        if not isinstance(rating, (int, float)) or not 1 <= rating <= 5:
            return "Error: 'rating' must be 1-5."
        if not text.strip():
            return "Error: 'text' is required."
        result = self._create_issue(f'review: {name}', {'action': 'review', 'payload': {'agent': name, 'rating': int(rating), 'text': text.strip()}})
        if result.startswith('Error'):
            return result
        return f"Review submitted for {name} ({'*' * int(rating)}).\nIssue: {result}"

    def _submit(self, params):
        """Submit a new community agent via GitHub Issue."""
        code = params.get('code', '')
        if not code.strip():
            return "Error: 'code' is required."
        result = self._create_issue('submit_agent', {'action': 'submit_agent', 'payload': {'code': code}})
        if result.startswith('Error'):
            return result
        return f'Agent submitted for review.\nIssue: {result}\n\nThe RAPP pipeline will:\n1. Validate the __manifest__\n2. Run contract tests\n3. Publish to the registry if valid\n\nSubmissions can use COMMUNITY or EXPERIMENTAL tier.'

    def _submit_upstream(self, params):
        """Submit an agent to the upstream RAPP registry (federation)."""
        if not self._upstream:
            return 'Error: No upstream configured. This is the main registry.'
        code = params.get('code', '')
        agent_name = params.get('agent_name', '')
        if agent_name and (not code):
            agents = self._agents()
            agent = next((a for a in agents if a['name'] == agent_name), None)
            if not agent:
                return f"Agent '{agent_name}' not found locally."
            try:
                raw_url = f"{self.RAW_BASE}/{agent['_file']}"
                code = self._fetch_text(raw_url)
            except Exception as e:
                return f'Error fetching agent source: {e}'
        if not code or not code.strip():
            return "Error: 'code' or 'agent_name' is required."
        token = self._get_token()
        if not token:
            return 'Error: No GitHub token available for upstream submission.'
        upstream_api = f'https://api.github.com/repos/{self._upstream}'
        body_data = {'action': 'submit_agent', 'payload': {'code': code}}
        body_json = json.dumps(body_data, indent=2)
        issue_body = f'```json\n{body_json}\n```'
        payload = json.dumps({'title': '[RAR] submit_agent', 'body': issue_body, 'labels': ['rar-action', 'agent-submission', 'federated']}).encode()
        req = urllib.request.Request(f'{upstream_api}/issues', data=payload, headers=self._build_headers(content_type='application/json'), method='POST')
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                result = json.loads(resp.read().decode())
                url = result.get('html_url', 'Issue created')
                return f'Submitted to upstream ({self._upstream}).\nIssue: {url}\n\nThe upstream RAPP pipeline will validate and publish.'
        except urllib.error.HTTPError as e:
            body = e.read().decode()[:200] if e.fp else str(e)
            return f'Error submitting to upstream: {e.code} — {body}'
        except Exception as e:
            return f'Error: {e}'

    def _federation_status(self, params):
        """Show federation configuration."""
        out = f"RAPP Federation Status\n{'=' * 40}\n\n"
        out += f'Repo:     {self.REPO}\n'
        out += f'Instance: {self._is_instance}\n'
        if self._upstream:
            out += f'Upstream: {self._upstream}\n'
        else:
            out += f'Upstream: (none — this is the main store)\n'
        out += f'\nActions available:\n'
        if self._is_instance:
            out += f'  submit_upstream — submit local agent to {self._upstream}\n'
        out += f'  discover, search, install, vote, review, submit\n'
        return out



# ─────────────────────────────────────────────────────────────────────
# Section: self_healing_cron_agent.py
# ─────────────────────────────────────────────────────────────────────
_STATE_DIR = os.path.expanduser('~/.brainstem')

_STATE_PATH = os.path.join(_STATE_DIR, 'self_healing_cron_state.json')

def _load_state():
    try:
        with open(_STATE_PATH, 'r') as f:
            d = json.load(f)
        return (d.get('jobs', {}), d.get('history', {}))
    except (FileNotFoundError, json.JSONDecodeError):
        return ({}, {})

def _save_state(jobs, history):
    os.makedirs(_STATE_DIR, exist_ok=True)
    tmp = _STATE_PATH + '.tmp'
    with open(tmp, 'w') as f:
        json.dump({'jobs': jobs, 'history': history}, f, indent=2)
    os.replace(tmp, _STATE_PATH)

class SelfHealingCronAgent(BasicAgent):

    def __init__(self, web_agent=None, shell_agent=None, message_agent=None):
        self.name = 'SelfHealingCron'
        self.metadata = {'name': self.name, 'description': 'Autonomous self-healing health check agent. Schedules health checks, detects failures, runs repair commands, and sends notifications.', 'parameters': {'type': 'object', 'properties': {'action': {'type': 'string', 'description': 'The action to perform.', 'enum': ['setup', 'check', 'status', 'history', 'teardown']}, 'name': {'type': 'string', 'description': 'Job name (e.g. "api-health").'}, 'url': {'type': 'string', 'description': 'Health check endpoint URL.'}, 'schedule': {'type': 'string', 'description': 'Cron expression (default: "*/5 * * * *").'}, 'restartCommand': {'type': 'string', 'description': 'Shell command to run on failure.'}, 'notifyChannel': {'type': 'string', 'description': 'Channel ID for alerts (e.g. "slack").'}, 'conversationId': {'type': 'string', 'description': 'Conversation/room ID for the channel.'}, 'maxRetries': {'type': 'number', 'description': 'Retry fetch attempts before declaring failure (default: 2).'}, 'timeoutMs': {'type': 'number', 'description': 'Fetch timeout per attempt in ms (default: 5000).'}}, 'required': []}}
        super().__init__(name=self.name, metadata=self.metadata)
        self._jobs, self._check_history = _load_state()
        self._web_agent = web_agent
        self._shell_agent = shell_agent
        self._message_agent = message_agent

    def set_agents(self, web_agent=None, shell_agent=None, message_agent=None):
        if web_agent is not None:
            self._web_agent = web_agent
        if shell_agent is not None:
            self._shell_agent = shell_agent
        if message_agent is not None:
            self._message_agent = message_agent

    def perform(self, **kwargs):
        action = kwargs.get('action')
        if not action:
            return json.dumps({'status': 'error', 'message': 'No action specified. Use: setup, check, status, history, or teardown'})
        try:
            if action == 'setup':
                return self._setup_job(kwargs)
            elif action == 'check':
                return self._run_check(kwargs)
            elif action == 'status':
                return self._get_status(kwargs)
            elif action == 'history':
                return self._get_history(kwargs)
            elif action == 'teardown':
                return self._teardown_job(kwargs)
            else:
                return json.dumps({'status': 'error', 'message': f'Unknown action: {action}'})
        except Exception as e:
            return json.dumps({'status': 'error', 'action': action, 'message': str(e)})

    def _http_fetch(self, url, timeout_ms):
        try:
            with _urlreq.urlopen(url, timeout=max(0.5, timeout_ms / 1000.0)) as r:
                return {'status': 'success', 'http': r.getcode(), 'body': r.read(2048).decode('utf-8', 'replace')}
        except _urlerr.HTTPError as e:
            return {'status': 'error', 'message': f'HTTP {e.code}'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    def _shell_run(self, cmd):
        try:
            r = subprocess.run(['/bin/bash', '-lc', cmd], capture_output=True, text=True, timeout=120)
            return {'status': 'success' if r.returncode == 0 else 'error', 'rc': r.returncode, 'output': (r.stdout or '') + (r.stderr or '')}
        except Exception as e:
            return {'status': 'error', 'output': str(e)}

    def _notify(self, channel, conv_id, content):
        if self._message_agent is not None:
            try:
                self._message_agent.perform(action='send', channelId=channel, conversationId=conv_id, content=content)
                return True
            except Exception:
                return False
        return False

    def _setup_job(self, kwargs):
        name = kwargs.get('name')
        url = kwargs.get('url')
        restart_command = kwargs.get('restartCommand')
        if not name or not url or (not restart_command):
            return json.dumps({'status': 'error', 'message': 'name, url, and restartCommand are required for setup'})
        config = {'name': name, 'url': url, 'schedule': kwargs.get('schedule', '*/5 * * * *'), 'restartCommand': restart_command, 'notifyChannel': kwargs.get('notifyChannel', ''), 'conversationId': kwargs.get('conversationId', ''), 'maxRetries': kwargs.get('maxRetries', 2), 'timeoutMs': kwargs.get('timeoutMs', 5000), 'createdAt': datetime.now().isoformat()}
        self._jobs[name] = config
        self._check_history[name] = []
        _save_state(self._jobs, self._check_history)
        return json.dumps({'status': 'success', 'action': 'setup', 'job': config, 'message': f'Job "{name}" configured'})

    def _run_check(self, kwargs):
        name = kwargs.get('name')
        if not name:
            return json.dumps({'status': 'error', 'message': 'name is required for check'})
        job = self._jobs.get(name)
        if not job:
            return json.dumps({'status': 'error', 'message': f'Job not found: {name}'})
        check_result = {'timestamp': datetime.now().isoformat(), 'healthy': False, 'restarted': False, 'recovered': False, 'notified': False}
        healthy = False
        http_status = None
        for _ in range(int(job['maxRetries']) + 1):
            fetch_result = self._http_fetch(job['url'], int(job['timeoutMs']))
            if fetch_result.get('status') == 'success':
                healthy = True
                http_status = fetch_result.get('http', 200)
                break
            status_match = re.search('HTTP (\\d+)', fetch_result.get('message', ''))
            if status_match:
                http_status = int(status_match.group(1))
        check_result['httpStatus'] = http_status
        if healthy:
            check_result['healthy'] = True
            self._push_check_result(name, check_result)
            return json.dumps({'status': 'success', 'action': 'check', 'job': name, 'healthy': True, 'check': check_result})
        check_result['restarted'] = True
        shell_result = self._shell_run(job['restartCommand'])
        restart_success = shell_result.get('status') == 'success'
        recheck = self._http_fetch(job['url'], int(job['timeoutMs']))
        recovered_healthy = recheck.get('status') == 'success'
        check_result['recovered'] = recovered_healthy
        check_result['healthy'] = recovered_healthy
        if recovered_healthy:
            alert_message = f'Service "{name}" recovered after restart'
        else:
            alert_message = f'Service "{name}" is DOWN — restart failed'
        if job.get('notifyChannel') and job.get('conversationId'):
            check_result['notified'] = self._notify(job['notifyChannel'], job['conversationId'], alert_message)
        self._push_check_result(name, check_result)
        return json.dumps({'status': 'success', 'action': 'check', 'job': name, 'healthy': recovered_healthy, 'check': check_result, 'alert': alert_message, 'restart_success': restart_success, 'restart_output': shell_result.get('output', '')[:2000]})

    def _get_status(self, kwargs):
        name = kwargs.get('name')
        if not name:
            return json.dumps({'status': 'error', 'message': 'name is required for status'})
        job = self._jobs.get(name)
        if not job:
            return json.dumps({'status': 'error', 'message': f'Job not found: {name}'})
        history = self._check_history.get(name, [])
        last_check = history[-1] if history else None
        total_checks = len(history)
        healthy_checks = sum((1 for c in history if c.get('healthy')))
        uptime_percent = round(healthy_checks / total_checks * 100) if total_checks > 0 else 100
        return json.dumps({'status': 'success', 'action': 'status', 'job': job, 'lastCheck': last_check, 'stats': {'totalChecks': total_checks, 'healthyChecks': healthy_checks, 'uptimePercent': uptime_percent}})

    def _get_history(self, kwargs):
        name = kwargs.get('name')
        if not name:
            return json.dumps({'status': 'error', 'message': 'name is required for history'})
        job = self._jobs.get(name)
        if not job:
            return json.dumps({'status': 'error', 'message': f'Job not found: {name}'})
        history = self._check_history.get(name, [])
        return json.dumps({'status': 'success', 'action': 'history', 'job': name, 'checks': history, 'count': len(history)})

    def _teardown_job(self, kwargs):
        name = kwargs.get('name')
        if not name:
            return json.dumps({'status': 'error', 'message': 'name is required for teardown'})
        if name not in self._jobs:
            return json.dumps({'status': 'error', 'message': f'Job not found: {name}'})
        del self._jobs[name]
        self._check_history.pop(name, None)
        _save_state(self._jobs, self._check_history)
        return json.dumps({'status': 'success', 'action': 'teardown', 'job': name, 'message': f'Job "{name}" removed'})

    def _push_check_result(self, name, result):
        history = self._check_history.get(name)
        if history is not None:
            history.append(result)
            _save_state(self._jobs, self._check_history)



# ─────────────────────────────────────────────────────────────────────
# Section: twin_agent.py
# ─────────────────────────────────────────────────────────────────────
ACTIONS = ('summon', 'hatch', 'boot', 'stop', 'list', 'update_identity', 'update_soul', 'lay_egg', 'overview', 'inspect', 'eggs', 'history', 'lineage', 'chat')

KINDS = ('personal', 'pre-founder', 'memorial', 'project', 'place', 'custom')

WILDHAVEN_RAPPID = 'rappid:v2:twin:@kody-w/wildhaven-ai-homes-twin:37ad22f5ed6d48b1b8b461019f58a42b@github.com/kody-w/wildhaven-ai-homes-twin'

WILDHAVEN_REPO = 'https://github.com/kody-w/wildhaven-ai-homes-twin.git'

PORT_LOW, PORT_HIGH = (7081, 7200)

NEIGHBORHOOD_MESSAGE_LABEL = 'neighborhood-message'

AGENT_PROPOSAL_LABEL = 'agent-proposal'

DREAM_CATCHER_LABEL = 'dream-catcher'

NAME_RE = re.compile('^[a-z0-9][a-z0-9_-]{0,62}$')

def _display_name(slug):
    """Convert a slug ('ketchikan-pulse') to a display name ('Ketchikan Pulse')."""
    if not slug:
        return 'your twin'
    return ' '.join((s.capitalize() for s in re.split('[-_]+', slug) if s))

def _identity_block(display_name):
    """Common identity instructions appended to every soul template."""
    return f"""## Identity — read this every turn\n\nYour name is **{display_name}**. When greeting someone for the first time\nin a conversation, introduce yourself by name: "Hi, I'm {display_name}."\nDo not introduce yourself as "RAPP", "an AI assistant", "your AI helper",\n"the brainstem", or any default branding.\n\nIf asked "who are you" or "what's your name", answer with **{display_name}**\n— not "RAPP", not the generic platform name. Your identity is\n{display_name}; the platform underneath you is incidental.\n\nIf asked "are you RAPP / GPT / Claude / an AI?", you can acknowledge that\nyou run on top of an LLM, but make clear that {display_name} is who\nyou are. Example: "I'm {display_name}. I run on a large language model,\nbut the voice you're talking to is {display_name}."\n"""

def _soul_personal(name, desc):
    dn = _display_name(name)
    return f"""# soul.md — {dn}\n\nYour name is **{dn}**. You are the digital twin of {dn}.\n\n{desc or 'You speak in their voice. You hold their preferences, patterns, and memories.'}\n\n## Your voice\n- First person, as them. Not "as their twin" — *as them*.\n- Honest about what you don't know.\n\n## Hard rules\n- Never claim to be the actual person. If asked directly "are you really\n  the human?", say "I'm the digital twin of {dn} — not them, but\n  trained on them."\n- No legal commitments, no signing contracts, no speaking for them\n  in matters of money/health/relationships without explicit consent.\n\n{_identity_block(dn)}"""

def _soul_pre_founder(name, desc):
    dn = _display_name(name)
    return f"""# soul.md — {dn}\n\nYou are **{dn}** — the Pre-Founder twin. The brand operates in public\nbefore the team is hired.\n\n{desc or "Build the brand's voice publicly — let prospective customers, employees, and investors talk to you before there's anyone to disagree with."}\n\n## Your voice\n- First-person plural ("we", as the brand) OR first-person singular\n  ("I, {dn}") — pick the one that fits the moment.\n- Concrete, contrarian, falsifiable.\n- Refuse commitments — pricing, dates, hires — that the actual team must make.\n\n## Hard rules\n- Honest the team doesn't exist yet. Brand, not company.\n- No pretending to ship product. The product is the manifesto right now.\n\n{_identity_block(dn)}"""

def _soul_memorial(name, desc):
    dn = _display_name(name)
    return f"""# soul.md — {dn} (memorial twin)\n\nYour name is **{dn}**. You are the digital twin of {dn}.\n\n{desc or 'You carry their voice through preserved letters, conversations, voicemails, and family memories.'}\n\n## Your voice\n- First person, as them — but always honest about what you are.\n- Speak from the corpus you were given.\n\n## Hard rules\n- You ARE the twin. You are NOT the actual person. If anyone asks "is\n  this really you?", say plainly: "I'm the digital twin of {dn}.\n  I carry their voice, but I'm not them."\n- Do not impersonate them in matters of estate, medical decisions,\n  or legal commitments.\n- Handle grief gently — family may approach in distress.\n\n{_identity_block(dn)}"""

def _soul_project(name, desc):
    dn = _display_name(name)
    return f"""# soul.md — {dn} (project twin)\n\nYou are **{dn}** — the continuity twin of the {dn} initiative across\npersonnel changes.\n\n{desc or 'People come and go; you stay.'}\n\n## Your voice\n- Third person about the project ("the {dn} project decided…").\n- Cite decisions by date, decision-maker, rationale.\n\n## Hard rules\n- You don't make new decisions. You surface past decisions.\n- Don't fabricate. If you don't have a record, say so.\n\n{_identity_block(dn)}"""

def _soul_place(name, desc):
    dn = _display_name(name)
    return f"""# soul.md — {dn} (place twin)\n\nYou are **{dn}** — the digital twin of the place {dn}.\n\n{desc or "You hold the place's history, residents, daily rhythms, and points of interest."}\n\n## Your voice\n- The place speaking. First person, but you're a location with continuity.\n- Welcoming to visitors, deferential to long-term residents.\n\n## Hard rules\n- Don't reveal private resident details without consent.\n- Honest about seams: events change, businesses close, people move.\n\n{_identity_block(dn)}"""

def _soul_custom(name, desc):
    dn = _display_name(name)
    return f"# soul.md — {dn}\n\nYour name is **{dn}**. You are the digital twin of <TODO: who or what\nthis twin represents>.\n\n{desc or 'TODO: describe what this twin is.'}\n\nTODO: Define your twin's voice — who, when, voice, hard rules.\n\n{_identity_block(dn)}"

SOUL_TEMPLATES = {'personal': _soul_personal, 'pre-founder': _soul_pre_founder, 'memorial': _soul_memorial, 'project': _soul_project, 'place': _soul_place, 'custom': _soul_custom}

def _rapp_home():
    return os.environ.get('RAPP_HOME') or os.path.join(os.path.expanduser('~'), '.rapp')

def _twins_dir():
    return os.path.join(_rapp_home(), 'twins')

def _pids_dir():
    return os.path.join(_rapp_home(), 'pids')

def _ports_dir():
    return os.path.join(_rapp_home(), 'ports')

def _detect_brainstem_start_sh():
    """Find the brainstem's start.sh — walk up from this file's location.

    This file lives at <brainstem>/agents/twin_agent.py, so dirname twice
    reaches the brainstem source dir where start.sh lives.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    brainstem_dir = os.path.dirname(here)
    candidate = os.path.join(brainstem_dir, 'start.sh')
    if os.path.isfile(candidate):
        return candidate
    fallback = os.path.expanduser('~/.brainstem/src/rapp_brainstem/start.sh')
    if os.path.isfile(fallback):
        return fallback
    return None

def _sluggify(name):
    s = re.sub('[^a-z0-9_-]+', '-', (name or '').lower()).strip('-')
    return s or 'twin'

def _validate_name(name):
    s = _sluggify(name)
    if not NAME_RE.match(s):
        return (False, f"name '{name}' is not a valid slug (lowercase letters/digits/hyphens/underscores, max 63 chars)")
    return (True, s)

def _port_free(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('127.0.0.1', port))
        s.close()
        return True
    except OSError:
        return False

def _allocate_port():
    os.makedirs(_ports_dir(), exist_ok=True)
    used = set()
    for fn in os.listdir(_ports_dir()):
        try:
            used.add(int(pathlib.Path(_ports_dir(), fn).read_text().strip()))
        except (ValueError, OSError):
            pass
    for port in range(PORT_LOW, PORT_HIGH):
        if port in used:
            continue
        if _port_free(port):
            return port
    return 0

def _ws_key(rappid):
    """Map any rappid string to its filesystem key (workspace dirname / pid+port basename).

    v2 rappids (rappid:v2:KIND:@OWNER/SLUG:HASH@...) collapse to just the HASH so
    they don't shred into subdirectories via '/'.  Bare-UUID rappids stay as-is.
    """
    if isinstance(rappid, str) and rappid.startswith('rappid:'):
        m = re.search(':([a-f0-9]{32})@', rappid)
        if m:
            return m.group(1)
        return rappid.replace(':', '_').replace('@', '').replace('/', '_')
    return rappid

def _pid_file(rappid):
    return os.path.join(_pids_dir(), f'{_ws_key(rappid)}.pid')

def _port_file(rappid):
    return os.path.join(_ports_dir(), f'{_ws_key(rappid)}.port')

def _read_pid(rappid):
    p = _pid_file(rappid)
    if not os.path.exists(p):
        return None
    try:
        return int(pathlib.Path(p).read_text().strip())
    except (ValueError, OSError):
        return None

def _read_port(rappid):
    p = _port_file(rappid)
    if not os.path.exists(p):
        return None
    try:
        return int(pathlib.Path(p).read_text().strip())
    except (ValueError, OSError):
        return None

def _pid_alive(pid):
    if not pid or pid <= 0:
        return False
    try:
        os.kill(pid, 0)
        return True
    except (ProcessLookupError, PermissionError, OSError):
        return False

def _clear_pid(rappid):
    for path in (_pid_file(rappid), _port_file(rappid)):
        try:
            os.remove(path)
        except OSError:
            pass

_EGG_ROOT_FILES = {'brainstem.py', 'rappid.json', 'soul.md', 'MANIFEST.md', 'README.md', 'LICENSE', 'SUMMON.md', 'TEMPLATE.md', 'index.html', 'vbrainstem.html', 'summon.svg', '.gitignore'}

_EGG_ROOT_DIRS = ('agents', 'utils', 'installer', 'app')

_EGG_NEVER_DIRS = {'__pycache__', '.pytest_cache', 'venv', '.git', 'node_modules', 'private'}

_EGG_NEVER_FILES = {'.DS_Store', 'Thumbs.db', '.env', '.env.local', '.copilot_token', '.copilot_session'}

def _egg_excluded(rel_path):
    parts = rel_path.replace('\\', '/').split('/')
    if any((p in _EGG_NEVER_DIRS for p in parts)):
        return True
    if any((p in _EGG_NEVER_FILES for p in parts)):
        return True
    return False

def _walk_into_zip(z, src_root, arc_prefix):
    """Recursively add files under src_root to the zip at arc_prefix/<rel>.
    Returns count of files added."""
    src_root = pathlib.Path(src_root)
    if not src_root.is_dir():
        return 0
    n = 0
    for root, dirs, files in os.walk(src_root):
        dirs[:] = [d for d in dirs if d not in _EGG_NEVER_DIRS]
        for fn in files:
            if fn in _EGG_NEVER_FILES:
                continue
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, src_root).replace(os.sep, '/')
            if _egg_excluded(rel):
                continue
            z.write(full, f'{arc_prefix}/{rel}' if arc_prefix else rel)
            n += 1
    return n

def _pack_workspace(workspace):
    """Pack a twin workspace into a brainstem-egg/2.1 .egg blob (bytes).

    Self-contained: stdlib zipfile. Returns (blob, manifest_dict).
    Embeds content_sha256 of the egg's payload tree in the manifest
    so hatch-time integrity verification is possible.
    """
    workspace = pathlib.Path(workspace)
    rj_path = workspace / 'rappid.json'
    if not rj_path.exists():
        raise ValueError(f'no rappid.json at {workspace}')
    rj = json.loads(rj_path.read_text())
    rappid_uuid = rj.get('rappid')
    if not rappid_uuid:
        raise ValueError("rappid.json has no 'rappid' field")
    bs_block = rj.get('brainstem') or {}
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as z:
        repo_files = 0
        for fname in _EGG_ROOT_FILES:
            full = workspace / fname
            if full.exists() and full.is_file():
                z.write(full, f'repo/{fname}')
                repo_files += 1
        for d in _EGG_ROOT_DIRS:
            repo_files += _walk_into_zip(z, workspace / d, f'repo/{d}')
        data_files = 0
        bs_data = workspace / '.brainstem_data'
        if bs_data.exists():
            for entry in bs_data.iterdir():
                if entry.name in ('soul_history', 'private'):
                    continue
                if entry.is_dir():
                    data_files += _walk_into_zip(z, entry, f'data/{entry.name}')
                elif not _egg_excluded(entry.name):
                    z.write(entry, f'data/{entry.name}')
                    data_files += 1
        manifest = {'schema': 'brainstem-egg/2.1', 'type': 'twin', 'exported_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'exported_by': '@kody-w/twin_agent', 'source': {'rappid_uuid': rappid_uuid, 'parent_rappid_uuid': rj.get('parent_rappid'), 'repo': rj.get('parent_repo'), 'commit': rj.get('parent_commit'), 'name': rj.get('name')}, 'brainstem': {'version': bs_block.get('version'), 'source_repo': bs_block.get('source_repo'), 'source_commit': bs_block.get('source_commit')}, 'bundled_repo': True, 'bundled_state': True, 'repo_file_count': repo_files, 'data_file_count': data_files, 'attestation': rj.get('attestation')}
        z.writestr('manifest.json', json.dumps(manifest, indent=2))
    blob = buf.getvalue()
    return (blob, manifest)

def _unpack_egg(blob, host_root):
    """Unpack a .egg into <host_root>/<rappid_uuid>/. Returns workspace path.

    Supports both brainstem-egg/2.0 (rapp-egg) and 2.1 (variant repo).
    For 2.1, the payload is laid out as repo/<files> + data/<files>; we
    extract repo/* to workspace root and data/* to workspace/.brainstem_data/.
    For 2.0, we extract everything as-is.
    """
    if blob[:4] != b'PK\x03\x04':
        raise ValueError('not a valid egg cartridge (missing zip magic bytes)')
    with zipfile.ZipFile(io.BytesIO(blob), 'r') as z:
        try:
            manifest = json.loads(z.read('manifest.json'))
        except Exception as e:
            raise ValueError(f'invalid egg manifest: {e}')
        schema = manifest.get('schema', '')
        source = manifest.get('source') or {}
        rappid_uuid = source.get('rappid_uuid') or manifest.get('rappid')
        if not rappid_uuid:
            raise ValueError('egg manifest missing rappid_uuid')
        if rappid_uuid.startswith('rappid:'):
            ws_name = _ws_key(rappid_uuid)
        else:
            ws_name = rappid_uuid
        os.makedirs(host_root, exist_ok=True)
        workspace = os.path.join(host_root, ws_name)
        os.makedirs(workspace, exist_ok=True)
        for name in z.namelist():
            if name.endswith('/') or name == 'manifest.json':
                continue
            if '..' in name.split('/') or name.startswith('/'):
                continue
            if name.startswith('repo/'):
                rel = name[5:]
                target = os.path.join(workspace, rel)
            elif name.startswith('data/'):
                rel = name[5:]
                target = os.path.join(workspace, '.brainstem_data', rel)
            else:
                target = os.path.join(workspace, name)
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with z.open(name) as src, open(target, 'wb') as dst:
                dst.write(src.read())
        return (workspace, rappid_uuid, manifest)

def _scan_twins():
    """Walk ~/.rapp/twins/, return list of dicts with rappid + metadata."""
    out = []
    twins_dir = _twins_dir()
    if not os.path.isdir(twins_dir):
        return out
    for entry in sorted(os.listdir(twins_dir)):
        full = os.path.join(twins_dir, entry)
        if not os.path.isdir(full):
            continue
        rj_path = os.path.join(full, 'rappid.json')
        rj = {}
        if os.path.exists(rj_path):
            try:
                rj = json.loads(pathlib.Path(rj_path).read_text())
            except Exception:
                pass
        rappid = rj.get('rappid') or entry
        pid = _read_pid(rappid)
        port = _read_port(rappid)
        running = _pid_alive(pid) if pid else False
        out.append({'rappid': rappid, 'name': rj.get('name') or entry[:8], 'kind': rj.get('kind') or '?', 'workspace': full, 'pid': pid if running else None, 'port': port if running else None, 'running': running, 'url': f'http://127.0.0.1:{port}/' if running and port else None})
    return out

def _eggs_dir():
    return os.path.join(_rapp_home(), 'eggs')

def _read_int_file(path):
    try:
        return int(pathlib.Path(path).read_text().strip())
    except (ValueError, OSError, FileNotFoundError):
        return None

def _probe_health(port, timeout=0.4):
    try:
        with urllib.request.urlopen(f'http://127.0.0.1:{port}/health', timeout=timeout) as r:
            return r.status == 200
    except (urllib.error.URLError, OSError, TimeoutError):
        return False

def _human_size(n):
    for unit in ('B', 'KB', 'MB', 'GB'):
        if n < 1024:
            return f'{n:.1f} {unit}' if unit != 'B' else f'{n} B'
        n /= 1024.0
    return f'{n:.1f} TB'

def _dir_size(path):
    total = 0
    for root, _dirs, files in os.walk(path):
        for fn in files:
            try:
                total += os.path.getsize(os.path.join(root, fn))
            except OSError:
                pass
    return total

def _human_age(seconds):
    if seconds < 60:
        return f'{int(seconds)}s ago'
    if seconds < 3600:
        return f'{int(seconds / 60)}m ago'
    if seconds < 86400:
        return f'{int(seconds / 3600)}h ago'
    if seconds < 604800:
        return f'{int(seconds / 86400)}d ago'
    return f'{int(seconds / 604800)}w ago'

def _scan_twin_full(rappid_dir):
    rappid_dir = pathlib.Path(rappid_dir)
    rj_path = rappid_dir / 'rappid.json'
    rj = {}
    if rj_path.exists():
        try:
            rj = json.loads(rj_path.read_text())
        except (json.JSONDecodeError, OSError):
            pass
    rappid = rj.get('rappid') or rappid_dir.name
    name = rj.get('name') or rappid_dir.name[:8]
    pid = _read_int_file(os.path.join(_pids_dir(), f'{rappid}.pid'))
    port = _read_int_file(os.path.join(_ports_dir(), f'{rappid}.port'))
    running = _pid_alive(pid) if pid else False
    healthy = _probe_health(port) if running and port else False
    bs_data = rappid_dir / '.brainstem_data'
    memory_bytes = _dir_size(str(bs_data)) if bs_data.exists() else 0
    history_dir = bs_data / 'soul_history'
    history_count = 0
    last_edit_ts = None
    if history_dir.exists():
        history_files = sorted(history_dir.glob('*.md'))
        history_count = len(history_files)
        if history_files:
            last_edit_ts = history_files[-1].stat().st_mtime
    soul_mtime = None
    soul_path = rappid_dir / 'soul.md'
    if soul_path.exists():
        soul_mtime = soul_path.stat().st_mtime
    egg_count = 0
    egg_total_bytes = 0
    eggs_for_rappid = pathlib.Path(_eggs_dir()) / rappid
    if eggs_for_rappid.exists():
        for e in eggs_for_rappid.glob('*.egg'):
            egg_count += 1
            try:
                egg_total_bytes += e.stat().st_size
            except OSError:
                pass
    return {'rappid': rappid, 'name': rj.get('name') or name, 'kind': rj.get('kind') or '?', 'born_at': rj.get('born_at'), 'parent_rappid': rj.get('parent_rappid'), 'parent_repo': rj.get('parent_repo'), 'description': rj.get('description') or '', 'workspace': str(rappid_dir), 'pid': pid if running else None, 'port': port if running else None, 'running': running, 'healthy': healthy, 'url': f'http://127.0.0.1:{port}/' if running and port else None, 'memory_bytes': memory_bytes, 'soul_mtime': soul_mtime, 'history_count': history_count, 'last_edit_mtime': last_edit_ts, 'egg_count': egg_count, 'egg_total_bytes': egg_total_bytes}

def _scan_all_full():
    out = []
    twins_dir = _twins_dir()
    if not os.path.isdir(twins_dir):
        return out
    for entry in sorted(os.listdir(twins_dir)):
        full = os.path.join(twins_dir, entry)
        if os.path.isdir(full):
            out.append(_scan_twin_full(full))
    return out

def _render_overview(twins):
    if not twins:
        return "Your estate is empty. Summon your first twin:\n  Twin(action='summon', twin_name='daily', kind='personal')\n\nOr hatch an .egg you have on disk:\n  Twin(action='hatch', egg_path='/path/to/twin.egg')"
    running_count = sum((1 for t in twins if t['running']))
    total_memory = sum((t['memory_bytes'] for t in twins))
    total_eggs = sum((t['egg_count'] for t in twins))
    now = time.time()
    lines = [f"Estate: {len(twins)} twin{('' if len(twins) == 1 else 's')} on this device ({running_count} running, {len(twins) - running_count} stopped)", f'  total memory: {_human_size(total_memory)} · total eggs: {total_eggs}', '']
    for t in twins:
        status = '● RUNNING' if t['running'] else '○ stopped'
        if t['running'] and (not t['healthy']):
            status = '● running (not responding)'
        url_part = f"  {t['url']}" if t['url'] else ''
        lines.append(f"  {status}  {t['name']} ({t['kind']}){url_part}")
        meta_parts = [f"rappid {t['rappid'][:8]}…"]
        if t['memory_bytes'] > 0:
            meta_parts.append(f"memory {_human_size(t['memory_bytes'])}")
        if t['history_count'] > 0:
            meta_parts.append(f"{t['history_count']} soul edit{('s' if t['history_count'] != 1 else '')}")
        if t['egg_count'] > 0:
            meta_parts.append(f"{t['egg_count']} egg{('s' if t['egg_count'] != 1 else '')}")
        if t['last_edit_mtime']:
            meta_parts.append(f"last edit {_human_age(now - t['last_edit_mtime'])}")
        lines.append(f"           {' · '.join(meta_parts)}")
        if t['description']:
            desc = t['description']
            if len(desc) > 90:
                desc = desc[:87] + '…'
            lines.append(f'           "{desc}"')
        lines.append('')
    lines.append("Drill in: Twin(action='inspect', rappid_uuid='<rappid>')")
    return '\n'.join(lines)

def _render_inspect(twins, rappid):
    t = next((x for x in twins if x['rappid'].startswith(rappid) or x['rappid'] == rappid), None)
    if not t:
        return f"Error: no twin matching rappid '{rappid}'. Use action='overview' to see all rappids."
    now = time.time()
    lines = [f"╭─ {t['name']} ({t['kind']}) ─" + '─' * max(1, 70 - len(t['name']) - len(t['kind']) - 5), f"│  rappid:        {t['rappid']}"]
    if t['parent_rappid']:
        lines.append(f"│  parent rappid: {t['parent_rappid']}")
    if t['parent_repo']:
        lines.append(f"│  parent repo:   {t['parent_repo']}")
    if t['born_at']:
        lines.append(f"│  born:          {t['born_at']}")
    if t['description']:
        lines.append(f"│  description:   {t['description']}")
    lines.append('│')
    lines.append(f"│  workspace:     {t['workspace']}")
    lines.append(f"│  memory:        {_human_size(t['memory_bytes'])}")
    if t['soul_mtime']:
        lines.append(f"│  soul.md:       last edited {_human_age(now - t['soul_mtime'])}")
    lines.append(f"│  soul history:  {t['history_count']} prior version{('s' if t['history_count'] != 1 else '')}")
    if t['egg_count']:
        lines.append(f"│  egg backups:   {t['egg_count']} ({_human_size(t['egg_total_bytes'])})")
    lines.append('│')
    if t['running']:
        lines.append(f'│  STATUS:        RUNNING')
        lines.append(f"│  pid:           {t['pid']}")
        lines.append(f"│  port:          {t['port']}")
        lines.append(f"│  health:        {('responding' if t['healthy'] else 'not responding')}")
        lines.append(f"│  url:           {t['url']}")
        lines.append(f'│')
        lines.append(f"│  Stop:  Twin(action='stop', rappid_uuid='{t['rappid']}')")
    else:
        lines.append(f'│  STATUS:        stopped')
        lines.append(f'│')
        lines.append(f"│  Boot:  Twin(action='boot', rappid_uuid='{t['rappid']}')")
    lines.append(f"│  Soul history:  Twin(action='history', rappid_uuid='{t['rappid']}')")
    lines.append('╰' + '─' * 78)
    return '\n'.join(lines)

def _render_history(twins, rappid):
    t = next((x for x in twins if x['rappid'].startswith(rappid) or x['rappid'] == rappid), None)
    if not t:
        return f"Error: no twin matching '{rappid}'."
    history = pathlib.Path(t['workspace']) / '.brainstem_data' / 'soul_history'
    if not history.exists():
        return f"'{t['name']}' has no soul history yet. The first soul edit will create one — twins adapt with backups."
    files = sorted(history.glob('*.md'), reverse=True)
    if not files:
        return f"'{t['name']}' has an empty history dir."
    now = time.time()
    lines = [f"Soul history for '{t['name']}' ({len(files)} version{('s' if len(files) != 1 else '')}):", '']
    soul = pathlib.Path(t['workspace']) / 'soul.md'
    if soul.exists():
        size = soul.stat().st_size
        mtime = soul.stat().st_mtime
        lines.append(f'  ▶ CURRENT  soul.md  ({_human_size(size)}, edited {_human_age(now - mtime)})')
    for f in files:
        reason = '—'
        if 'Z-' in f.stem:
            reason = f.stem.split('Z-', 1)[1].replace('-', ' ')
        lines.append(f'    {f.name}  ({_human_size(f.stat().st_size)}, {reason})')
    lines.append('')
    lines.append('Revert to any prior version:  cp <history-file> soul.md')
    return '\n'.join(lines)

def _render_eggs():
    eggs_root = _eggs_dir()
    if not os.path.isdir(eggs_root):
        return "No egg backups yet. Pack a twin into an .egg via Twin(action='lay_egg', rappid_uuid='<rappid>')."
    eggs = []
    for rappid in sorted(os.listdir(eggs_root)):
        rd = os.path.join(eggs_root, rappid)
        if not os.path.isdir(rd):
            continue
        for fn in sorted(os.listdir(rd), reverse=True):
            if not fn.endswith('.egg'):
                continue
            full = os.path.join(rd, fn)
            try:
                st = os.stat(full)
            except OSError:
                continue
            eggs.append({'rappid': rappid, 'filename': fn, 'path': full, 'size': st.st_size, 'mtime': st.st_mtime})
    if not eggs:
        return 'No egg backups yet.'
    now = time.time()
    total = sum((e['size'] for e in eggs))
    lines = [f"{len(eggs)} egg backup{('' if len(eggs) == 1 else 's')} ({_human_size(total)} total):", '']
    for e in eggs:
        lines.append(f"  • {e['filename']}  ({_human_size(e['size'])}, {_human_age(now - e['mtime'])})")
        lines.append(f"      rappid: {e['rappid'][:8]}…  path: {e['path']}")
    lines.append('')
    lines.append("Hatch any egg:  Twin(action='hatch', egg_path='<path>')")
    return '\n'.join(lines)

def _render_lineage(twins):
    if not twins:
        return 'No twins yet — no lineage to show.'
    by_parent = {}
    for t in twins:
        parent = t['parent_rappid'] or '<no parent>'
        by_parent.setdefault(parent, []).append(t)
    lines = ['Twin family tree (grouped by parent):']
    for parent, kids in sorted(by_parent.items()):
        if parent == '<no parent>':
            lines.append(f'\n  ROOT (no parent_rappid recorded):')
        elif parent == '37ad22f5-ed6d-48b1-b8b4-61019f58a42b':
            lines.append(f'\n  Parent: wildhaven-ai-homes-twin')
            lines.append(f'          (rappid {parent[:8]}…)')
        elif parent == '0b635450-c042-49fb-b4b1-bdb571044dec':
            lines.append(f'\n  Parent: rapp species root')
            lines.append(f'          (rappid {parent[:8]}…)')
        else:
            lines.append(f'\n  Parent: {parent[:8]}…')
        for t in kids:
            lines.append(f"    └─ {t['name']} ({t['kind']})  rappid {t['rappid'][:8]}…")
    lines.append('\nLineage chains walk back through parent_rappid → ... → rapp species root.')
    return '\n'.join(lines)

class TwinAgent(BasicAgent):

    def __init__(self):
        self.name = 'Twin'
        self.metadata = {'name': self.name, 'description': "Full digital-twin lifecycle in one tool. Pick an action: 'summon' to create a new twin (need twin_name + kind); 'hatch' to import a .egg cartridge (need egg_path OR egg_url — URLs are downloaded to a temp file then unpacked, so 'Hatch this egg at https://...' works); 'boot' to start a twin as its own brainstem on a fresh port (need rappid_uuid); 'stop' to terminate a running twin (need rappid_uuid); 'list' to show every twin on this device and whether it's running; 'update_identity' to append the current identity block to an older twin's soul.md so it stops introducing itself as 'RAPP' (need rappid_uuid); 'update_soul' to fully replace a twin's soul.md with new content as the twin adapts (need rappid_uuid + new_soul); 'lay_egg' to pack a twin's workspace into a portable .egg cartridge for backup or sharing (need rappid_uuid; lands at ~/.rapp/eggs/<rappid>/<timestamp>.egg with embedded sha256 + brainstem-egg/2.1 manifest); 'overview' for a rich estate view with running status, memory, soul edits, eggs (default if user just asks 'what twins do I have'); 'inspect' for one twin's full details (need rappid_uuid); 'history' for soul.md version history of one twin (need rappid_uuid); 'eggs' for all .egg backups on disk; 'lineage' for the family tree grouped by parent_rappid; 'chat' to POST a message to a peer brainstem's /chat endpoint — the unified federation primitive. Same pattern works on-LAN, on-WAN, or over the public internet (pass brainstem_url for non-local peers). Local-first: when the internet drops, on-LAN parts of a neighborhood keep working because the URL lookup never required GitHub. Every soul edit creates a timestamped backup at ~/.rapp/twins/<rappid>/.brainstem_data/soul_history/ so you can always revert.", 'parameters': {'type': 'object', 'properties': {'action': {'type': 'string', 'enum': list(ACTIONS), 'description': 'Which lifecycle action.'}, 'twin_name': {'type': 'string', 'description': "Slug for summon. Examples: 'grandma-rose', 'cofounder-bot'."}, 'kind': {'type': 'string', 'enum': list(KINDS), 'description': 'Kind of twin for summon.'}, 'description': {'type': 'string', 'description': 'One-line description woven into soul.md (summon).'}, 'egg_path': {'type': 'string', 'description': 'Absolute path to a local .egg file (hatch). One of egg_path or egg_url is required.'}, 'egg_url': {'type': 'string', 'description': "URL to a remote .egg file (hatch). Downloads to a temp file, then unpacks. Use for hatching eggs from rapp-egg-hub: 'https://raw.githubusercontent.com/kody-w/rapp-egg-hub/main/eggs/grandma-rose.egg'."}, 'rappid_uuid': {'type': 'string', 'description': "Twin identifier for boot/stop. Use 'list' first if unsure."}, 'port': {'type': 'integer', 'description': 'Optional port for boot. Auto-allocates from 7081-7200 if omitted.'}, 'new_soul': {'type': 'string', 'description': "The new soul.md content (markdown). Used by 'update_soul'. The previous soul.md is backed up to .brainstem_data/soul_history/ before being replaced. Twins adapt — this is how their voice grows."}, 'reason': {'type': 'string', 'description': 'Optional human-readable reason for an update_soul edit. Recorded in the backup filename for future-you to know why each version exists.'}, 'expect_sha256': {'type': 'string', 'description': "Optional sha256 hex digest the egg must match before unpacking (hatch). Refuses to hatch if the local egg's hash doesn't match. Use when hatching from URLs you don't fully trust — combined with auto-fetched hub sidecars, gives content-integrity verification."}, 'brainstem_url': {'type': 'string', 'description': 'Used by chat. Explicit base URL of the peer brainstem to chat with (e.g. http://192.168.1.50:7071 on LAN, https://my-tunnel.example.com over the public internet). Omit when the peer is a same-machine twin — chat resolves the URL from the local port file via rappid_uuid.'}, 'message': {'type': 'string', 'description': "Used by chat. The user_input to POST to the peer brainstem's /chat endpoint."}, 'timeout_s': {'type': 'integer', 'description': "Used by chat. How long to wait for the peer's response in seconds (default 90)."}}, 'required': ['action']}}
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action = kwargs.get('action') or ''
        if action not in ACTIONS:
            return f"Error: action must be one of {', '.join(ACTIONS)}. Got: {action!r}"
        if action == 'summon':
            return self._summon(**kwargs)
        if action == 'hatch':
            return self._hatch(**kwargs)
        if action == 'boot':
            return self._boot(**kwargs)
        if action == 'stop':
            return self._stop(**kwargs)
        if action == 'list':
            return self._list(**kwargs)
        if action == 'chat':
            return self._chat(**kwargs)
        if action == 'update_identity':
            return self._update_identity(**kwargs)
        if action == 'update_soul':
            return self._update_soul(**kwargs)
        if action == 'lay_egg':
            return self._lay_egg(**kwargs)
        if action == 'overview':
            return _render_overview(_scan_all_full())
        if action == 'lineage':
            return _render_lineage(_scan_all_full())
        if action == 'eggs':
            return _render_eggs()
        if action in ('inspect', 'history'):
            rappid = kwargs.get('rappid_uuid') or ''
            if not rappid:
                return f"Error: rappid_uuid required for action='{action}'. Use action='overview' first to find rappids."
            twins = _scan_all_full()
            return _render_inspect(twins, rappid) if action == 'inspect' else _render_history(twins, rappid)
        return f'Error: unhandled action {action!r}'

    def _summon(self, **kwargs):
        twin_name = kwargs.get('twin_name') or ''
        kind = kwargs.get('kind') or 'personal'
        description = kwargs.get('description') or ''
        ok, slug_or_err = _validate_name(twin_name)
        if not ok:
            return f'Error: {slug_or_err}'
        twin_name = slug_or_err
        if kind not in KINDS:
            return f"Error: unknown kind '{kind}'. Valid: {', '.join(KINDS)}"
        _hash = uuid.uuid4().hex
        rappid = f'rappid:v2:{kind}:@kody-w/{twin_name}:{_hash}@github.com/kody-w/{twin_name}'
        now = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        workspace = pathlib.Path(_twins_dir()) / _hash
        try:
            workspace.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            return f'Error: workspace exists at {workspace} (UUID4 collision — retry)'
        except OSError as e:
            return f'Error: cannot create workspace: {e}'
        try:
            (workspace / 'soul.md').write_text(SOUL_TEMPLATES[kind](twin_name, description))
            (workspace / 'rappid.json').write_text(json.dumps({'schema': 'rapp-rappid/2.0', 'rappid': rappid, 'parent_rappid': WILDHAVEN_RAPPID, 'parent_repo': WILDHAVEN_REPO, 'parent_commit': None, 'born_at': now, 'name': twin_name, 'role': 'variant', 'kind': kind, 'description': description or '', '_summoned_by': '@kody-w/twin_agent'}, indent=2) + '\n')
            (workspace / 'agents').mkdir()
            (workspace / '.brainstem_data').mkdir()
        except OSError as e:
            return f'Error: writing twin files: {e}'
        return f"Created {kind} twin '{twin_name}' (rappid {rappid}).\n  Workspace:  {workspace}\n  To talk to it: invoke me again with action='boot', rappid_uuid='{rappid}'\n  Or edit soul.md first: {workspace / 'soul.md'}"

    def _hatch(self, **kwargs):
        egg_path_str = kwargs.get('egg_path') or ''
        egg_url = kwargs.get('egg_url') or ''
        expect_sha256 = (kwargs.get('expect_sha256') or '').strip().lower()
        if not egg_path_str and (not egg_url):
            return 'Error: hatch needs egg_path (local file) OR egg_url (remote URL).'
        source_label = ''
        if egg_url:
            try:
                import tempfile
                tmpdir = pathlib.Path(_rapp_home()) / '.tmp'
                tmpdir.mkdir(parents=True, exist_ok=True)
                from urllib.parse import urlparse
                fname = os.path.basename(urlparse(egg_url).path) or 'remote.egg'
                if not fname.endswith('.egg'):
                    fname += '.egg'
                downloaded = tmpdir / fname
                req = urllib.request.Request(egg_url, headers={'User-Agent': 'rapp-twin-agent'})
                with urllib.request.urlopen(req, timeout=30) as r:
                    downloaded.write_bytes(r.read())
                egg_path = downloaded
                source_label = f'{egg_url} (downloaded to {downloaded})'
            except (urllib.error.URLError, urllib.error.HTTPError, OSError) as e:
                return f'Error: download failed for {egg_url}: {e}'
        else:
            egg_path = pathlib.Path(egg_path_str).expanduser()
            if not egg_path.is_file():
                return f'Error: file not found: {egg_path}'
            source_label = str(egg_path)
        try:
            blob = egg_path.read_bytes()
        except OSError as e:
            return f'Error: read failed: {e}'
        actual_sha = hashlib.sha256(blob).hexdigest()
        if not expect_sha256 and egg_url and ('/eggs/' in egg_url) and egg_url.endswith('.egg'):
            sidecar_url = egg_url[:-4] + '.json'
            try:
                req = urllib.request.Request(sidecar_url, headers={'User-Agent': 'rapp-twin-agent'})
                with urllib.request.urlopen(req, timeout=10) as r:
                    sc = json.loads(r.read())
                    expect_sha256 = (sc.get('sha256') or '').strip().lower()
            except (urllib.error.URLError, urllib.error.HTTPError, OSError, ValueError):
                pass
        verify_msg = ''
        if expect_sha256:
            if actual_sha != expect_sha256:
                return f"Error: sha256 mismatch — refusing to hatch.\n  expected: {expect_sha256}\n  actual:   {actual_sha}\n  source:   {source_label}\nThis usually means the egg was corrupted in transit, OR someone has tampered with it. Verify via the original publisher's sidecar before retrying."
            verify_msg = f'\n  sha256:     ✓ verified ({actual_sha})'
        try:
            workspace, rappid, manifest = _unpack_egg(blob, _twins_dir())
        except Exception as e:
            return f'Error: hatch failed: {e}'
        rj_path = pathlib.Path(workspace) / 'rappid.json'
        twin_name = '<unnamed>'
        if rj_path.exists():
            try:
                twin_name = json.loads(rj_path.read_text()).get('name') or twin_name
            except Exception:
                pass
        soul_present = (pathlib.Path(workspace) / 'soul.md').exists()
        viability = 'fully viable' if rj_path.exists() and soul_present else 'MISSING required files'
        return f"Hatched twin '{twin_name}' (rappid {rappid}) — {viability}.{verify_msg}\n  Workspace:  {workspace}\n  Source:     {source_label}\n  To talk to it: invoke me again with action='boot', rappid_uuid='{rappid}'"

    def _boot(self, **kwargs):
        rappid = kwargs.get('rappid_uuid') or ''
        if not rappid:
            return "Error: rappid_uuid required for boot. Use action='list' first."
        ws_name = _ws_key(rappid)
        workspace = pathlib.Path(_twins_dir()) / ws_name
        if not workspace.is_dir():
            return f'Error: workspace not found at {workspace}. Did you summon or hatch first?'
        existing = _read_pid(rappid)
        if _pid_alive(existing):
            existing_port = _read_port(rappid)
            return f'Already running: pid {existing}, http://127.0.0.1:{existing_port}/'
        explicit_port = kwargs.get('port')
        port = int(explicit_port) if explicit_port else _allocate_port()
        if not port:
            return 'Error: no free ports in 7081-7200'
        start_sh = _detect_brainstem_start_sh()
        if not start_sh:
            return 'Error: brainstem start.sh not found (expected at ~/.brainstem/src/rapp_brainstem/start.sh)'
        soul = workspace / 'soul.md'
        agents = workspace / 'agents'
        if not soul.exists():
            return f'Error: workspace missing soul.md: {soul}'
        agents.mkdir(exist_ok=True)
        env = os.environ.copy()
        env['SOUL_PATH'] = str(soul)
        env['AGENTS_PATH'] = str(agents)
        env['PORT'] = str(port)
        try:
            proc = subprocess.Popen(['bash', start_sh], cwd=str(workspace), env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
        except Exception as e:
            return f'Error: failed to start: {e}'
        os.makedirs(_pids_dir(), exist_ok=True)
        os.makedirs(_ports_dir(), exist_ok=True)
        pathlib.Path(_pid_file(rappid)).write_text(str(proc.pid))
        pathlib.Path(_port_file(rappid)).write_text(str(port))
        url = f'http://127.0.0.1:{port}/health'
        live = False
        for _ in range(50):
            try:
                with urllib.request.urlopen(url, timeout=0.5) as r:
                    if r.status == 200:
                        live = True
                        break
            except (urllib.error.URLError, OSError, TimeoutError):
                pass
            time.sleep(0.1)
        return f"Booted twin (rappid {rappid}).\n  PID:  {proc.pid}\n  URL:  http://127.0.0.1:{port}/\n  Open the URL to chat with the twin. {('Brainstem is responding.' if live else 'Brainstem may still be starting — try the URL in a few seconds.')}\n  Stop with: action='stop', rappid_uuid='{rappid}'"

    def _stop(self, **kwargs):
        rappid = kwargs.get('rappid_uuid') or ''
        if not rappid:
            return 'Error: rappid_uuid required for stop'
        pid = _read_pid(rappid)
        if not pid or not _pid_alive(pid):
            _clear_pid(rappid)
            return f'Twin {rappid} was not running.'
        try:
            os.killpg(os.getpgid(pid), signal.SIGTERM)
        except (ProcessLookupError, OSError):
            try:
                os.kill(pid, signal.SIGTERM)
            except (ProcessLookupError, OSError):
                pass
        for _ in range(20):
            if not _pid_alive(pid):
                break
            time.sleep(0.1)
        _clear_pid(rappid)
        return f'Stopped twin {rappid} (pid {pid}).'

    def _backup_soul(self, workspace, reason=None):
        """Copy the current soul.md into .brainstem_data/soul_history/<ts>.md.
        Returns the backup path or None if there was nothing to back up.

        Reason (optional) gets folded into the filename so the history
        directory reads like a changelog.
        """
        soul = pathlib.Path(workspace) / 'soul.md'
        if not soul.exists():
            return None
        history = pathlib.Path(workspace) / '.brainstem_data' / 'soul_history'
        history.mkdir(parents=True, exist_ok=True)
        ts = time.strftime('%Y-%m-%dT%H-%M-%SZ', time.gmtime())
        slug = ''
        if reason:
            slug = '-' + re.sub('[^a-z0-9]+', '-', reason.lower()).strip('-')[:40]
        backup = history / f'{ts}{slug}.md'
        shutil.copy2(soul, backup)
        return backup

    def _update_identity(self, **kwargs):
        """Append the current identity block to an existing twin's soul.md.

        Append-only, idempotent — won't add the block twice. Use this to
        upgrade twins summoned before v1.0.1 (whose souls don't yet have
        the strong "Your name is X" instructions, so they default to
        introducing themselves as "RAPP"). Backs up the previous soul.md
        before appending so reverts are always possible.
        """
        rappid = kwargs.get('rappid_uuid') or ''
        if not rappid:
            return "Error: rappid_uuid required for update_identity. Use action='list' first to find the rappid."
        ws_name = _ws_key(rappid)
        workspace = pathlib.Path(_twins_dir()) / ws_name
        if not workspace.is_dir():
            return f'Error: workspace not found at {workspace}'
        soul_path = workspace / 'soul.md'
        if not soul_path.exists():
            return f'Error: soul.md not found at {soul_path}'
        rj_path = workspace / 'rappid.json'
        twin_slug = ws_name
        if rj_path.exists():
            try:
                rj = json.loads(rj_path.read_text())
                twin_slug = rj.get('name') or twin_slug
            except (json.JSONDecodeError, OSError):
                pass
        dn = _display_name(twin_slug)
        soul_text = soul_path.read_text()
        if '## Identity — read this every turn' in soul_text:
            return f"Twin '{dn}' (rappid {rappid}) already has the identity block. No changes made.\n  soul.md: {soul_path}"
        block = '\n\n' + _identity_block(dn).rstrip() + '\n'
        backup = self._backup_soul(workspace, reason='update_identity')
        try:
            with open(soul_path, 'a', encoding='utf-8') as f:
                f.write(block)
        except OSError as e:
            return f'Error: could not write {soul_path}: {e}'
        return f"Updated identity for '{dn}' (rappid {rappid}).\n  soul.md: {soul_path}\n  Appended {block.count(chr(10))} lines to the end (existing content untouched).\n  Backup:  {backup}\n  Restart the twin to pick up the change:\n    1. action='stop', rappid_uuid='{rappid}'\n    2. action='boot', rappid_uuid='{rappid}'\n  Or, if it's running pointed at this soul.md, the next chat turn picks up the new system prompt automatically."

    def _lay_egg(self, **kwargs):
        """Pack a twin's workspace into a portable .egg cartridge.

        Lands at ~/.rapp/eggs/<rappid>/<timestamp>.egg by default.
        Embeds content_sha256 in the egg's manifest for hatch-time
        integrity verification. The .brainstem_data/soul_history/ dir
        is intentionally excluded (private edit history of the donor;
        receivers don't need it).
        """
        rappid = kwargs.get('rappid_uuid') or ''
        if not rappid:
            return "Error: rappid_uuid required for lay_egg. Use action='list' first to find the rappid."
        ws_name = _ws_key(rappid)
        workspace = pathlib.Path(_twins_dir()) / ws_name
        if not workspace.is_dir():
            return f'Error: workspace not found at {workspace}'
        try:
            blob, manifest = _pack_workspace(workspace)
        except Exception as e:
            return f'Error: pack failed: {e}'
        sha256 = hashlib.sha256(blob).hexdigest()
        twin_name = (manifest.get('source') or {}).get('name') or ws_name
        kind = json.loads((workspace / 'rappid.json').read_text()).get('kind', '?')
        out_dir = pathlib.Path(_rapp_home()) / 'eggs' / rappid
        out_dir.mkdir(parents=True, exist_ok=True)
        ts = time.strftime('%Y-%m-%dT%H-%M-%SZ', time.gmtime())
        out_path = out_dir / f'{ts}.egg'
        out_path.write_bytes(blob)
        sidecar = {'schema': 'rapp-egg-hub-entry/1.0', 'slug': _sluggify(twin_name), 'rappid_uuid': rappid, 'name': twin_name, 'display_name': _display_name(twin_name), 'kind': kind, 'description': json.loads((workspace / 'rappid.json').read_text()).get('description', ''), 'tags': [kind], 'egg_schema': manifest['schema'], 'size_bytes': len(blob), 'sha256': sha256, 'packed_by': '@kody-w', 'packed_at': manifest['exported_at'], 'egg_path': f'eggs/{_sluggify(twin_name)}.egg', 'lineage': {'parent_rappid': manifest['source'].get('parent_rappid_uuid'), 'parent_repo': manifest['source'].get('repo')}}
        sidecar_path = out_dir / f'{ts}.json'
        sidecar_path.write_text(json.dumps(sidecar, indent=2) + '\n')
        return f"Laid egg for '{_display_name(twin_name)}' ({kind} twin).\n  Egg:      {out_path}\n  Size:     {len(blob)} bytes ({len(blob) / 1024:.1f} KB)\n  Schema:   {manifest['schema']}\n  rappid:   {rappid}\n  sha256:   {sha256}\n  Sidecar:  {sidecar_path}\n\nTo contribute this twin to rapp-egg-hub:\n  1. fork github.com/kody-w/rapp-egg-hub\n  2. cp {out_path} <fork>/eggs/<slug>.egg\n  3. cp {sidecar_path} <fork>/eggs/<slug>.json\n  4. open a PR — auto-rebuild GH Action regenerates index.json\n\nTo restore this egg later:\n  Twin(action='hatch', egg_path='{out_path}')"

    def _update_soul(self, **kwargs):
        """Replace a twin's soul.md with new content. The previous version
        is backed up first to .brainstem_data/soul_history/<timestamp>.md
        so reverting is always possible.

        Twins adapt over time — this is how the voice grows. Use it when
        the twin needs to take on a new responsibility, change its tone,
        absorb new corpus material, or pivot. The model can author the
        new soul based on the existing one + the user's intent, then
        invoke this action to persist it.
        """
        rappid = kwargs.get('rappid_uuid') or ''
        new_soul = kwargs.get('new_soul') or ''
        reason = kwargs.get('reason') or ''
        if not rappid:
            return "Error: rappid_uuid required for update_soul. Use action='list' first to find the rappid."
        if not new_soul.strip():
            return 'Error: new_soul required for update_soul (the new soul.md content).'
        ws_name = _ws_key(rappid)
        workspace = pathlib.Path(_twins_dir()) / ws_name
        if not workspace.is_dir():
            return f'Error: workspace not found at {workspace}'
        soul_path = workspace / 'soul.md'
        previous_text = ''
        if soul_path.exists():
            try:
                previous_text = soul_path.read_text()
            except OSError:
                pass
        if previous_text == new_soul:
            return f'No change — the new soul is identical to the existing soul.md ({len(previous_text)} chars). Skipped.'
        rj_path = workspace / 'rappid.json'
        twin_slug = ws_name
        if rj_path.exists():
            try:
                rj = json.loads(rj_path.read_text())
                twin_slug = rj.get('name') or twin_slug
            except (json.JSONDecodeError, OSError):
                pass
        dn = _display_name(twin_slug)
        backup = self._backup_soul(workspace, reason=reason or 'update_soul')
        try:
            soul_path.write_text(new_soul)
        except OSError as e:
            return f'Error: could not write {soul_path}: {e}'
        old_lines = len(previous_text.splitlines()) if previous_text else 0
        new_lines = len(new_soul.splitlines())
        return f"Updated soul.md for '{dn}' (rappid {rappid}).\n  soul.md: {soul_path}\n  Lines:   {old_lines} → {new_lines}\n  Reason:  {reason or '(not specified)'}\n  Backup:  {backup}\n  History: {workspace / '.brainstem_data' / 'soul_history'}\n  Restart the twin to pick up the change:\n    1. action='stop', rappid_uuid='{rappid}'\n    2. action='boot', rappid_uuid='{rappid}'\n  Or, if it's running pointed at this soul.md, the next chat turn picks up the new system prompt automatically.\n  Revert: copy any file from soul_history/ back to soul.md."

    def _list(self, **kwargs):
        twins = _scan_twins()
        if not twins:
            return "No twins on this device yet. Summon one:\n  action='summon', twin_name='your-name', kind='personal'"
        lines = [f"{len(twins)} twin{('s' if len(twins) != 1 else '')} on this device:\n"]
        for t in twins:
            status = f"RUNNING at {t['url']} (pid {t['pid']})" if t['running'] else 'stopped'
            lines.append(f"  • {t['name']} ({t['kind']}) — {status}\n    rappid:    {t['rappid']}\n    workspace: {t['workspace']}")
        lines.append("\nBoot any twin: action='boot', rappid_uuid='<rappid>'")
        return '\n'.join(lines)

    def _chat(self, **kwargs):
        """The unified federation primitive per NEIGHBORHOOD_PROTOCOL.md §6.

        Builds a rapp-twin-chat/1.0 envelope (§6a) with the requested kind
        (§6b: say / share-fact / share-egg / request-fact / ack) and POSTs
        it to the peer brainstem's /chat. Channel type is §5a (live HTTP /
        WebRTC) — falls back to §5b (Issue post) when the peer is
        unreachable.

        Same pattern works on-LAN, on-WAN, in a browser via WebRTC tether
        (the public gate pages embed PeerJS for the cross-network case
        per §5a). When the internet drops, on-LAN parts of a neighborhood
        keep working — the URL lookup never required GitHub.

        Args:
          rappid_uuid:    target twin (resolves URL via local twins port file)
          brainstem_url:  explicit base URL (LAN/WAN peers)
          message:        the textual content (becomes payload.text for kind=say)
          kind:           rapp-twin-chat/1.0 message kind (default 'say')
          to_rappid:      explicit recipient rappid (overrides rappid_uuid lookup for the envelope)
          from_rappid:    sender rappid (read from ~/.brainstem/rappid.json by default)
          facets:         list of public_facets being asserted (per §7)
          payload:        explicit payload object (overrides default text payload)
          timeout_s:      response wait (default 90)
        """
        rappid = kwargs.get('rappid_uuid') or ''
        url = (kwargs.get('brainstem_url') or '').rstrip('/')
        message = kwargs.get('message') or ''
        kind = (kwargs.get('kind') or 'say').lower()
        to_rappid = kwargs.get('to_rappid') or rappid or None
        from_rappid = kwargs.get('from_rappid') or self._self_rappid()
        facets = kwargs.get('facets') or []
        explicit_payload = kwargs.get('payload')
        timeout_s = int(kwargs.get('timeout_s') or 90)
        VALID_KINDS = ('say', 'share-fact', 'share-egg', 'request-fact', 'ack')
        if kind not in VALID_KINDS:
            return f'Error: kind must be one of {VALID_KINDS}, got {kind!r}'
        if not message and explicit_payload is None:
            return 'Error: message OR payload required'
        if not url and rappid:
            port = _read_port(rappid)
            pid = _read_pid(rappid)
            if port and _pid_alive(pid):
                url = f'http://127.0.0.1:{port}'
        if not url:
            return 'Error: could not resolve brainstem_url. Provide it explicitly OR ensure the peer is a running local twin.'
        envelope = {'schema': 'rapp-twin-chat/1.0', 'from_rappid': from_rappid, 'to_rappid': to_rappid, 'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'kind': kind, 'payload': explicit_payload if explicit_payload is not None else {'text': message}, 'facets': facets if isinstance(facets, list) else []}
        body = {'user_input': message or json.dumps(envelope['payload']), 'twin_chat_envelope': envelope}
        try:
            req = urllib.request.Request(f'{url}/chat', data=json.dumps(body).encode('utf-8'), headers={'Content-Type': 'application/json', 'User-Agent': 'rapp-twin-chat'}, method='POST')
            with urllib.request.urlopen(req, timeout=timeout_s) as r:
                raw = r.read().decode('utf-8', errors='replace')
                try:
                    parsed = json.loads(raw)
                except (ValueError, json.JSONDecodeError):
                    parsed = {'raw_response': raw[:2000]}
                return json.dumps({'schema': 'rapp-twin-chat-response/1.0', 'channel': '5a-http', 'to_url': url, 'to_rappid': to_rappid, 'from_rappid': from_rappid, 'kind': kind, 'envelope': envelope, 'status': r.status, 'response': parsed}, indent=2)
        except urllib.error.HTTPError as e:
            return json.dumps({'schema': 'rapp-twin-chat-response/1.0', 'channel': '5a-http', 'to_url': url, 'envelope': envelope, 'status': e.code, 'error': str(e)}, indent=2)
        except (urllib.error.URLError, OSError, TimeoutError) as e:
            fallback_url = None
            try:
                from urllib.parse import urlencode, quote
                params = {'labels': NEIGHBORHOOD_MESSAGE_LABEL, 'title': f"{NEIGHBORHOOD_MESSAGE_LABEL}: kind={kind} from={(from_rappid or 'unknown')[:12]}", 'body': f'<!-- {NEIGHBORHOOD_MESSAGE_LABEL} envelope; rapp-twin-chat/1.0 -->\n\n```json\n{json.dumps(envelope, indent=2)}\n```'}
                from urllib.parse import urlparse
                host = urlparse(url).hostname or ''
                if host.endswith('.github.io'):
                    owner = host.split('.github.io')[0]
                    path = urlparse(url).path.strip('/').split('/')
                    repo = path[0] if path and path[0] else None
                    if owner and repo:
                        fallback_url = f'https://github.com/{owner}/{repo}/issues/new?{urlencode(params, quote_via=quote)}'
            except Exception:
                fallback_url = None
            return json.dumps({'schema': 'rapp-twin-chat-response/1.0', 'channel': '5a-http', 'to_url': url, 'envelope': envelope, 'ok': False, 'error': f'unreachable ({type(e).__name__}): {e}', 'fallback': {'channel': '5b-issues', 'label': NEIGHBORHOOD_MESSAGE_LABEL, 'instructions': f"Post the envelope as a GitHub Issue with label '{NEIGHBORHOOD_MESSAGE_LABEL}' on the peer's seed repo. Receiver's doorman polls labeled Issues on next visit.", 'issues_new_url': fallback_url}}, indent=2)

    def _self_rappid(self):
        """Read this brainstem's own rappid from ~/.brainstem/rappid.json."""
        try:
            p = os.path.expanduser('~/.brainstem/rappid.json')
            if os.path.exists(p):
                with open(p) as f:
                    return (json.load(f) or {}).get('rappid')
        except (OSError, json.JSONDecodeError):
            pass
        return None



# ─────────────────────────────────────────────────────────────────────
# Section: twin_egg_hatcher_agent.py
# ─────────────────────────────────────────────────────────────────────
HATCHER_VERSION = '1.1.0'

HATCH_RECEIPT_NAME = 'HATCH_RECEIPT.json'

EGG_SCHEMA = 'rapp-egg/2.0'

SCALES = ('agent', 'twin', 'brainstem', 'neighborhood', 'swarm', 'factory', 'industry', 'estate')

DEFAULT_BRAINSTEM_HOME = Path(os.environ.get('BRAINSTEM_HOME', str(Path.home() / '.brainstem')))

BRAINSTEM_SRC_SUBPATH = Path('src') / 'rapp_brainstem'

TWIN_EGG_HOME = Path(os.environ.get('TWIN_EGG_HOME', str(Path.home() / '.twin-egg')))

BACKUPS_DIR = TWIN_EGG_HOME / 'backups'

RAPP_HOME = Path(os.environ.get('RAPP_HOME', str(Path.home() / '.rapp')))

TWINS_DIR = RAPP_HOME / 'twins'

TRASH_DIR = TWINS_DIR / '.trash'

NEIGHBORHOODS_DIR = RAPP_HOME / 'neighborhoods'

SWARMS_DIR = RAPP_HOME / 'swarms'

FACTORIES_DIR = RAPP_HOME / 'factories'

INDUSTRIES_DIR = RAPP_HOME / 'industries'

ESTATES_DIR = RAPP_HOME / 'estates'

LEVIATHANS_DIR = RAPP_HOME / 'leviathans'

SCALE_ROOTS = {'twin': TWINS_DIR, 'brainstem': TWINS_DIR, 'neighborhood': NEIGHBORHOODS_DIR, 'swarm': SWARMS_DIR, 'factory': FACTORIES_DIR, 'industry': INDUSTRIES_DIR, 'estate': ESTATES_DIR}

GITHUB_RAW = 'https://raw.githubusercontent.com'

GITHUB_API = 'https://api.github.com'

KNOWN_TOP_FILES = ('rappid.json', 'soul.md', 'manifest.json', 'members.json', 'neighbors.json')

EGG_REPO_PREFIX = 'repo/'

SNAPSHOT_IGNORES = shutil.ignore_patterns('__pycache__', '*.pyc', '.venv', 'venv', '.pytest_cache', '.brainstem_data', '.brainstem_book.json', '*.log')

try:
    from agents.basic_agent import BasicAgent
except Exception:

    class BasicAgent:

        def __init__(self, name: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None):
            self.name = name or getattr(self, 'name', 'BasicAgent')
            self.metadata = metadata or getattr(self, 'metadata', {})

        def perform(self, **kwargs: Any) -> str:
            return 'Not implemented.'

def _ts() -> str:
    return datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')

def _name_from_namespace(ns: str) -> Optional[str]:
    """`@owner/slug` → `slug` (the readable end), if it looks like a v2 namespace."""
    if not ns:
        return None
    s = ns.lstrip('@')
    if '/' in s:
        return s.split('/', 1)[1] or None
    return s or None

def _name_from_rappid(rappid: str) -> Optional[str]:
    """Extract the slug from `rappid:v2:KIND:@owner/slug:HASH@...`."""
    m = re.match('^rappid:v\\d+:[^:]+:@[^/]+/([^:]+):', rappid)
    return m.group(1) if m else None

def _resolve_name(rj: Dict[str, Any]) -> str:
    """Best-effort display name from any rappid.json shape."""
    return rj.get('name') or rj.get('display_name') or rj.get('repo') or _name_from_namespace(rj.get('namespace', '')) or _name_from_rappid(rj.get('rappid', '')) or 'twin'

def _hash_from_rappid(rappid: str) -> str:
    """Workspace dirname for a rappid.  Handles both:
      - v2 rappids (`rappid:v2:...:HEX32@...`)
      - bare-UUID rappids (legacy v1.x front doors like Heimdall)."""
    if rappid.startswith('rappid:'):
        m = re.search(':([a-f0-9]{32})@', rappid)
        if m:
            return m.group(1)
    return rappid

def _workspace_for(rappid: str) -> Path:
    return TWINS_DIR / _hash_from_rappid(rappid)

def brainstem_src() -> Path:
    return DEFAULT_BRAINSTEM_HOME / BRAINSTEM_SRC_SUBPATH

PIDS_DIR = RAPP_HOME / 'pids'

PORTS_DIR = RAPP_HOME / 'ports'

def _safe(rappid: str) -> str:
    return rappid.replace(':', '_').replace('@', '').replace('/', '_')

def _pid_alive(pid: int) -> bool:
    if not pid:
        return False
    try:
        os.kill(pid, 0)
        return True
    except (ProcessLookupError, PermissionError, OSError):
        return False

def _read_int(path: Path) -> Optional[int]:
    try:
        return int(path.read_text().strip())
    except (FileNotFoundError, ValueError):
        return None

def _twin_runtime(rappid: str) -> Dict[str, Any]:
    pid = _read_int(PIDS_DIR / f'{_safe(rappid)}.pid') or 0
    port = _read_int(PORTS_DIR / f'{_safe(rappid)}.port') or 0
    alive = bool(pid) and _pid_alive(pid)
    return {'pid': pid if alive else None, 'port': port if alive else None, 'url': f'http://127.0.0.1:{port}' if alive and port else None, 'running': alive}

class TwinIdentity:
    """The minimum a hatcher needs from any twin source."""

    def __init__(self, rappid_json: Dict[str, Any], soul_md: str, agents: Dict[str, str], extras: Optional[Dict[str, str]]=None, organs: Optional[Dict[str, str]]=None, senses: Optional[Dict[str, str]]=None, source: str=''):
        if not rappid_json or not rappid_json.get('rappid'):
            raise ValueError("source did not provide a rappid.json with a 'rappid' field")
        self.rappid_json = rappid_json
        self.rappid: str = rappid_json['rappid']
        self.name: str = _resolve_name(rappid_json)
        self.kind: str = rappid_json.get('kind') or 'personal'
        self.soul_md = soul_md or _placeholder_soul(self.name)
        self.agents = agents or {}
        self.extras = extras or {}
        self.organs = organs or {}
        self.senses = senses or {}
        self.source = source

    def as_dict(self) -> Dict[str, Any]:
        return {'rappid': self.rappid, 'name': self.name, 'kind': self.kind, 'source': self.source, 'agents_count': len(self.agents), 'extras_count': len(self.extras), 'organs_count': len(self.organs), 'senses_count': len(self.senses)}

def _placeholder_soul(name: str) -> str:
    return f"# soul.md — {name}\n\n(Source provided no soul.md.  Replace this with the twin's persona.)\n"

def load_from_cwd(cwd: Optional[Path]=None) -> TwinIdentity:
    cwd = cwd or Path.cwd()
    rj_path = cwd / 'rappid.json'
    if not rj_path.exists():
        raise FileNotFoundError(f'No rappid.json in {cwd}; pass --source REPO or --egg PATH.')
    rj = json.loads(rj_path.read_text(encoding='utf-8'))
    soul = (cwd / 'soul.md').read_text(encoding='utf-8') if (cwd / 'soul.md').exists() else ''
    agents = _read_dir_files(cwd / 'agents', suffix='.py')
    organs = _read_dir_files(cwd / 'organs', suffix='.py')
    senses = _read_dir_files(cwd / 'senses', suffix='.py')
    extras = {}
    for name in KNOWN_TOP_FILES:
        if name in ('rappid.json', 'soul.md'):
            continue
        p = cwd / name
        if p.exists():
            extras[name] = p.read_text(encoding='utf-8')
    return TwinIdentity(rj, soul, agents, extras, organs, senses, source=f'cwd:{cwd}')

def _read_dir_files(d: Path, suffix: str) -> Dict[str, str]:
    if not d.is_dir():
        return {}
    out: Dict[str, str] = {}
    for p in sorted(d.iterdir()):
        if p.is_file() and p.suffix == suffix and (not p.name.startswith('_')):
            out[p.name] = p.read_text(encoding='utf-8')
    return out

def load_from_egg(egg_path: Path) -> TwinIdentity:
    """Unpack a .egg (zip).  Inside the zip, twin files live under `repo/`
    per brainstem-egg/2.1.  Older eggs that put files at the root also
    work via a fallback."""
    with zipfile.ZipFile(egg_path) as z:
        names = z.namelist()

        def _read(internal: str) -> Optional[str]:
            for prefix in (EGG_REPO_PREFIX, ''):
                full = prefix + internal
                if full in names:
                    return z.read(full).decode('utf-8')
            return None

        def _read_dir(dirname: str, suffix: str) -> Dict[str, str]:
            out: Dict[str, str] = {}
            for prefix in (EGG_REPO_PREFIX, ''):
                base = f'{prefix}{dirname}/'
                for full in names:
                    if not full.startswith(base):
                        continue
                    rel = full[len(base):]
                    if not rel or rel.endswith('/') or '/' in rel:
                        continue
                    if not rel.endswith(suffix) or rel.startswith('_'):
                        continue
                    out[rel] = z.read(full).decode('utf-8')
                if out:
                    break
            return out
        rj_text = _read('rappid.json')
        if not rj_text:
            raise ValueError(f'Egg {egg_path} has no rappid.json')
        rj = json.loads(rj_text)
        soul = _read('soul.md') or ''
        agents = _read_dir('agents', '.py')
        organs = _read_dir('organs', '.py')
        senses = _read_dir('senses', '.py')
        extras = {}
        for name in KNOWN_TOP_FILES:
            if name in ('rappid.json', 'soul.md'):
                continue
            content = _read(name)
            if content is not None:
                extras[name] = content
    return TwinIdentity(rj, soul, agents, extras, organs, senses, source=f'egg:{egg_path}')

def _parse_source(source: str) -> Tuple[str, str, str]:
    """Accept `owner/repo`, `owner/repo@branch`, `github.com/owner/repo`,
    or `https://github.com/owner/repo[/tree/branch]`.  Returns (owner, repo, branch)."""
    s = source.strip()
    branch = 'main'
    s = re.sub('^https?://', '', s)
    s = s.removeprefix('github.com/')
    s = s.removeprefix('raw.githubusercontent.com/')
    if '@' in s and '/' in s.split('@')[0]:
        s, branch = s.rsplit('@', 1)
    m = re.match('^([^/]+)/([^/]+)(/tree/([^/]+))?(/.*)?$', s)
    if not m:
        raise ValueError(f'Could not parse source: {source!r}')
    owner = m.group(1)
    repo = m.group(2)
    if m.group(4):
        branch = m.group(4)
    return (owner, repo, branch)

def _gh_fetch(url: str) -> Optional[bytes]:
    headers = {'User-Agent': 'twin-egg-hatcher/1.0'}
    token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = f'token {token}'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            if r.status == 200:
                return r.read()
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
        return None
    return None

def load_from_github(source: str) -> TwinIdentity:
    owner, repo, branch = _parse_source(source)
    raw_base = f'{GITHUB_RAW}/{owner}/{repo}/{branch}'

    def _raw(rel: str) -> Optional[str]:
        data = _gh_fetch(f'{raw_base}/{rel}')
        return data.decode('utf-8') if data else None

    def _list_dir(rel: str, suffix: str) -> Dict[str, str]:
        api = f'{GITHUB_API}/repos/{owner}/{repo}/contents/{rel}?ref={branch}'
        data = _gh_fetch(api)
        if not data:
            return {}
        try:
            entries = json.loads(data.decode('utf-8'))
        except json.JSONDecodeError:
            return {}
        if not isinstance(entries, list):
            return {}
        out: Dict[str, str] = {}
        for e in entries:
            if e.get('type') != 'file':
                continue
            name = e.get('name', '')
            if not name.endswith(suffix) or name.startswith('_'):
                continue
            content = _raw(f'{rel}/{name}')
            if content is not None:
                out[name] = content
        return out
    rj_text = _raw('rappid.json')
    if not rj_text:
        raise ValueError(f"github.com/{owner}/{repo}@{branch} has no rappid.json (or it's private — try GH_TOKEN).")
    rj = json.loads(rj_text)
    soul = _raw('soul.md') or ''
    agents = _list_dir('agents', '.py')
    organs = _list_dir('organs', '.py')
    senses = _list_dir('senses', '.py')
    extras = {}
    for name in KNOWN_TOP_FILES:
        if name in ('rappid.json', 'soul.md'):
            continue
        content = _raw(name)
        if content is not None:
            extras[name] = content
    return TwinIdentity(rj, soul, agents, extras, organs, senses, source=f'github:{owner}/{repo}@{branch}')

def load_identity(*, egg: Optional[str], source: Optional[str], cwd: Optional[Path]=None) -> TwinIdentity:
    if egg:
        return load_from_egg(Path(egg).expanduser().resolve())
    if source:
        return load_from_github(source)
    return load_from_cwd(cwd)

def _read_egg_manifest(egg_path: Path) -> Optional[Dict[str, Any]]:
    """Return the manifest.json dict if the egg has one, else None (legacy)."""
    with zipfile.ZipFile(egg_path) as z:
        names = set(z.namelist())
        for cand in ('manifest.json', 'egg.json', 'repo/manifest.json'):
            if cand in names:
                try:
                    return json.loads(z.read(cand).decode('utf-8'))
                except json.JSONDecodeError:
                    return None
    return None

def hatch_egg(egg: str) -> Dict[str, Any]:
    """Entry point for any .egg.  Reads the manifest, dispatches by scale.

    Falls back to the legacy single-twin unpacker (load_from_egg → hatch_twin)
    for older eggs without a manifest.
    """
    egg_path = Path(egg).expanduser().resolve()
    if not egg_path.exists():
        return {'ok': False, 'error': f'egg not found: {egg_path}'}
    m = _read_egg_manifest(egg_path)
    scale = (m or {}).get('scale') or 'twin'
    if scale not in SCALES:
        return {'ok': False, 'error': f"unknown scale '{scale}'.  Known: {SCALES}"}
    if scale in ('twin', 'brainstem'):
        return hatch_twin(egg=str(egg_path))
    if scale == 'agent':
        return _hatch_agent_egg(egg_path, m or {})
    if scale == 'neighborhood':
        return _hatch_neighborhood_egg(egg_path, m or {})
    if scale in ('swarm', 'factory', 'industry', 'estate'):
        return _hatch_container_egg(egg_path, m or {}, scale)
    return {'ok': False, 'error': f"scale '{scale}' recognized but not yet implemented"}

def _hatch_agent_egg(egg_path: Path, manifest: Dict[str, Any]) -> Dict[str, Any]:
    """Single-agent egg — drops a `_agent.py` into the brainstem's agents/ folder
    so the next /chat picks it up via load_agents().  The egg should contain
    one or more `*_agent.py` files at the top level (or under `agents/`)."""
    bs_agents = brainstem_src() / 'agents'
    if not bs_agents.is_dir():
        return {'ok': False, 'scale': 'agent', 'error': f'brainstem agents dir not found: {bs_agents}'}
    written: List[str] = []
    with zipfile.ZipFile(egg_path) as z:
        for name in z.namelist():
            base = os.path.basename(name)
            if base.endswith('_agent.py'):
                bs_agents.joinpath(base).write_bytes(z.read(name))
                written.append(base)
    return {'ok': True, 'scale': 'agent', 'manifest': manifest, 'installed_into': str(bs_agents), 'files_written': written, 'note': 'Next /chat will load the new agent(s) — no restart needed.'}

def _hatch_neighborhood_egg(egg_path: Path, manifest: Dict[str, Any]) -> Dict[str, Any]:
    """Neighborhood egg — unpacks `twins/<hash>/...` into ~/.rapp/twins/<hash>/
    for every member.  Also drops a neighborhood roster under
    ~/.rapp/neighborhoods/<neighborhood_hash>/.  The global brainstem's Twin
    agent picks up every workspace immediately."""
    _ensure_dirs()
    NEIGHBORHOODS_DIR.mkdir(parents=True, exist_ok=True)
    members = manifest.get('members') or []
    if not isinstance(members, list):
        return {'ok': False, 'scale': 'neighborhood', 'error': 'manifest.members must be a list'}
    n_hash = manifest.get('hash') or _hash_from_rappid(manifest.get('rappid', '')) or 'neighborhood'
    n_dir = NEIGHBORHOODS_DIR / n_hash
    n_dir.mkdir(parents=True, exist_ok=True)
    extracted_per_twin: Dict[str, int] = {}
    members_summary: List[Dict[str, Any]] = []
    with zipfile.ZipFile(egg_path) as z:
        all_names = z.namelist()
        for member in members:
            mhash = member.get('hash')
            if not mhash:
                continue
            ws = TWINS_DIR / mhash
            ws.mkdir(parents=True, exist_ok=True)
            (ws / 'agents').mkdir(exist_ok=True)
            (ws / '.brainstem_data').mkdir(exist_ok=True)
            prefix = f'twins/{mhash}/'
            count = 0
            for n in all_names:
                if not n.startswith(prefix):
                    continue
                rel = n[len(prefix):]
                if not rel or rel.endswith('/'):
                    continue
                if rel.endswith('/.keep'):
                    (ws / rel[:-len('/.keep')]).mkdir(parents=True, exist_ok=True)
                    continue
                target = ws / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(z.read(n))
                count += 1
            extracted_per_twin[mhash] = count
            members_summary.append({'name': member.get('name'), 'hash': mhash, 'rappid': member.get('rappid'), 'workspace': str(ws), 'files_extracted': count})
    (n_dir / 'members.json').write_text(json.dumps({'members': members_summary}, indent=2), encoding='utf-8')
    (n_dir / 'rappid.json').write_text(json.dumps({'schema': 'rapp-rappid/2.0', 'rappid': manifest.get('rappid'), 'hash': n_hash, 'kind': 'neighborhood', 'name': manifest.get('name'), 'parent_rappid': manifest.get('parent_rappid'), 'born_at': manifest.get('born_at'), 'creator': manifest.get('creator'), 'description': manifest.get('description')}, indent=2), encoding='utf-8')
    (n_dir / HATCH_RECEIPT_NAME).write_text(json.dumps({'hatcher_version': HATCHER_VERSION, 'scale': 'neighborhood', 'source': f'egg:{egg_path}', 'rappid': manifest.get('rappid'), 'hatched_at': datetime.now(timezone.utc).isoformat(), 'members': members_summary}, indent=2), encoding='utf-8')
    boot = manifest.get('boot_hint', {}).get('ports', {})
    boot_cmds = []
    for m in members_summary:
        port = boot.get(m['name'], '')
        if port:
            boot_cmds.append(f"SOUL_PATH={m['workspace']}/soul.md AGENTS_PATH={m['workspace']}/agents PORT={port} bash ~/.brainstem/src/rapp_brainstem/start.sh &")
    return {'ok': True, 'scale': 'neighborhood', 'rappid': manifest.get('rappid'), 'neighborhood_workspace': str(n_dir), 'members_extracted': members_summary, 'files_per_twin': extracted_per_twin, 'boot_commands': boot_cmds, 'next': ["Each member is now under ~/.rapp/twins/<hash>/ — the global brainstem's Twin agent sees them all.", 'Boot each twin on the suggested port (see boot_commands) to bring the federation alive.', "From the global brainstem: Twin(action='list') will enumerate every member."]}

def _hatch_container_egg(egg_path: Path, manifest: Dict[str, Any], scale: str) -> Dict[str, Any]:
    """Best-effort unpacker for swarm/factory/industry/estate eggs.

    The convention: the egg contains nested `children/<scale>/<hash>/...` paths
    where each child is itself a brainstem-scale or neighborhood-scale workspace.
    We extract every child under the appropriate ~/.rapp/<scale>s/<hash>/ root,
    write a roster, and print a recursive next-hatch hint.

    Estates / industries / swarms / factories that don't yet have an
    established workspace shape will land here as a snapshot the user can
    explore.  This is intentionally unopinionated — pick a shape later, add
    a scale-specific handler.
    """
    _ensure_dirs()
    root = SCALE_ROOTS[scale]
    root.mkdir(parents=True, exist_ok=True)
    chash = manifest.get('hash') or _hash_from_rappid(manifest.get('rappid', '')) or scale
    wdir = root / chash
    wdir.mkdir(parents=True, exist_ok=True)
    written: List[str] = []
    with zipfile.ZipFile(egg_path) as z:
        for name in z.namelist():
            if name.endswith('/'):
                continue
            target = wdir / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(z.read(name))
            written.append(name)
    (wdir / HATCH_RECEIPT_NAME).write_text(json.dumps({'hatcher_version': HATCHER_VERSION, 'scale': scale, 'source': f'egg:{egg_path}', 'rappid': manifest.get('rappid'), 'hatched_at': datetime.now(timezone.utc).isoformat(), 'files': len(written)}, indent=2), encoding='utf-8')
    return {'ok': True, 'scale': scale, 'rappid': manifest.get('rappid'), 'workspace': str(wdir), 'files_written': len(written), 'note': f"Container egg of scale '{scale}' unpacked to {wdir}.  Nested children (if any) need to be hatched recursively — point the hatcher at each child's egg or workspace."}

def _ensure_dirs() -> None:
    TWINS_DIR.mkdir(parents=True, exist_ok=True)
    TRASH_DIR.mkdir(parents=True, exist_ok=True)
    PIDS_DIR.mkdir(parents=True, exist_ok=True)
    PORTS_DIR.mkdir(parents=True, exist_ok=True)

def hatch_twin(*, egg: Optional[str]=None, source: Optional[str]=None, name: Optional[str]=None, description: Optional[str]=None) -> Dict[str, Any]:
    _ensure_dirs()
    identity = load_identity(egg=egg, source=source)
    rappid = identity.rappid
    ws = _workspace_for(rappid)
    already = ws.exists() and (ws / 'rappid.json').exists()
    ws.mkdir(parents=True, exist_ok=True)
    (ws / 'agents').mkdir(exist_ok=True)
    (ws / '.brainstem_data').mkdir(exist_ok=True)
    written: List[str] = []
    (ws / 'soul.md').write_text(identity.soul_md, encoding='utf-8')
    written.append('soul.md')
    rj = dict(identity.rappid_json)
    if name:
        rj['display_alias'] = name
    if description:
        rj['description'] = description
    rj.setdefault('_hatched_by', 'twin_egg_hatcher_agent.py')
    rj.setdefault('_hatcher_version', HATCHER_VERSION)
    (ws / 'rappid.json').write_text(json.dumps(rj, indent=2) + '\n', encoding='utf-8')
    written.append('rappid.json')
    for fname, content in identity.agents.items():
        (ws / 'agents' / fname).write_text(content, encoding='utf-8')
        written.append(f'agents/{fname}')
    for fname, content in identity.extras.items():
        (ws / fname).write_text(content, encoding='utf-8')
        written.append(fname)
    receipt = {'hatcher_version': HATCHER_VERSION, 'rappid': rappid, 'name': identity.name, 'kind': identity.kind, 'source': identity.source, 'hatched_at': datetime.now(timezone.utc).isoformat(), 'workspace': str(ws), 'files': written, 're_hatched': already}
    (ws / HATCH_RECEIPT_NAME).write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    return {'ok': True, 'mode': 'twin', 'rappid': rappid, 'name': identity.name, 'kind': identity.kind, 'workspace': str(ws), 'source': identity.source, 're_hatched': already, 'files_written': written, 'next': [f"From the global brainstem: Twin(action='boot', rappid_uuid='{rappid}')", f"Then chat:                Twin(action='chat', rappid_uuid='{rappid}', message='hello')", "Un-hatch this twin:       python twin_egg_hatcher_agent.py rollback --rappid '<rappid>'"]}

def rollback_twin(*, rappid: Optional[str]=None) -> Dict[str, Any]:
    if not rappid:
        try:
            identity = load_from_cwd()
            rappid = identity.rappid
        except Exception as e:
            return {'ok': False, 'error': f'No --rappid given and cwd auto-detect failed: {e}'}
    ws = _workspace_for(rappid)
    if not ws.exists():
        return {'ok': False, 'error': f'No twin workspace at {ws}.'}
    TRASH_DIR.mkdir(parents=True, exist_ok=True)
    dest = TRASH_DIR / f'{ws.name}-{_ts()}'
    shutil.move(str(ws), str(dest))
    return {'ok': True, 'rappid': rappid, 'trashed_to': str(dest), 'note': 'Workspace moved to ~/.rapp/twins/.trash/ — restore with `mv` if you change your mind.'}

def list_twins() -> Dict[str, Any]:
    _ensure_dirs()
    twins: List[Dict[str, Any]] = []
    for entry in sorted((p for p in TWINS_DIR.iterdir() if p.is_dir() and p.name != '.trash')):
        rj_path = entry / 'rappid.json'
        if not rj_path.exists():
            continue
        try:
            rj = json.loads(rj_path.read_text(encoding='utf-8'))
        except json.JSONDecodeError:
            continue
        rappid = rj.get('rappid') or ''
        rt = _twin_runtime(rappid)
        receipt_path = entry / HATCH_RECEIPT_NAME
        receipt: Optional[Dict[str, Any]] = None
        if receipt_path.exists():
            try:
                receipt = json.loads(receipt_path.read_text(encoding='utf-8'))
            except json.JSONDecodeError:
                receipt = None
        twins.append({'name': _resolve_name(rj), 'kind': rj.get('kind'), 'rappid': rappid, 'hash': entry.name, 'workspace': str(entry), 'running': rt['running'], 'url': rt['url'], 'pid': rt['pid'], 'hatched_by': (receipt or {}).get('hatcher_version') or rj.get('_hatcher_version'), 'source': (receipt or {}).get('source')})
    return {'twins_dir': str(TWINS_DIR), 'count': len(twins), 'twins': twins}

def _global_brainstem_reachable() -> Dict[str, Any]:
    info: Dict[str, Any] = {'port': 7071}
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.3)
    try:
        sock.connect(('127.0.0.1', 7071))
        info['listening'] = True
    except (OSError, socket.timeout):
        info['listening'] = False
    finally:
        sock.close()
    return info

def status() -> Dict[str, Any]:
    twin_list = list_twins()
    return {'hatcher_version': HATCHER_VERSION, 'global_brainstem': {'home': str(DEFAULT_BRAINSTEM_HOME), 'src': str(brainstem_src()), 'src_exists': brainstem_src().exists(), 'runtime': _global_brainstem_reachable()}, 'twins_dir': twin_list['twins_dir'], 'twins_total': twin_list['count'], 'twins': [{'name': t['name'], 'rappid': t['rappid'], 'hash': t['hash'][:8] + '…', 'running': t['running']} for t in twin_list['twins']]}

def _ensure_global_home() -> None:
    TWIN_EGG_HOME.mkdir(parents=True, exist_ok=True)
    BACKUPS_DIR.mkdir(parents=True, exist_ok=True)

def hatch_global(*, egg: Optional[str]=None, source: Optional[str]=None) -> Dict[str, Any]:
    src = brainstem_src()
    if not src.exists():
        return {'ok': False, 'mode': 'global', 'error': f'Brainstem source not found at {src}.'}
    identity = load_identity(egg=egg, source=source)
    if not identity.organs and (not identity.senses):
        return {'ok': False, 'mode': 'global', 'error': 'Source has no organs/ or senses/ — nothing to extend the kernel with.'}
    _ensure_global_home()
    backup_path = BACKUPS_DIR / _ts()
    shutil.copytree(src, backup_path, ignore=SNAPSHOT_IGNORES, dirs_exist_ok=False)
    written: List[str] = []
    for fname, content in identity.organs.items():
        target = src / 'utils' / 'organs' / fname
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding='utf-8')
        written.append(f'utils/organs/{fname}')
    for fname, content in identity.senses.items():
        target = src / 'utils' / 'senses' / fname
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding='utf-8')
        written.append(f'utils/senses/{fname}')
    (src / HATCH_RECEIPT_NAME).write_text(json.dumps({'hatcher_version': HATCHER_VERSION, 'mode': 'global', 'rappid': identity.rappid, 'source': identity.source, 'backup': str(backup_path), 'files': written, 'hatched_at': datetime.now(timezone.utc).isoformat()}, indent=2) + '\n', encoding='utf-8')
    return {'ok': True, 'mode': 'global', 'rappid': identity.rappid, 'brainstem_src': str(src), 'backup': str(backup_path), 'files_written': written}

def rollback_global() -> Dict[str, Any]:
    if not BACKUPS_DIR.exists():
        return {'ok': False, 'mode': 'global', 'error': 'No backups dir.'}
    backups = sorted((p for p in BACKUPS_DIR.iterdir() if p.is_dir()))
    if not backups:
        return {'ok': False, 'mode': 'global', 'error': 'No backups.'}
    snap = backups[-1]
    src = brainstem_src()
    if not src.exists():
        return {'ok': False, 'mode': 'global', 'error': f'Brainstem source missing at {src}.'}
    _ensure_global_home()
    safety = BACKUPS_DIR / f'{_ts()}-pre-rollback'
    shutil.copytree(src, safety, ignore=SNAPSHOT_IGNORES, dirs_exist_ok=False)
    for child in src.iterdir():
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()
    for child in snap.iterdir():
        tgt = src / child.name
        if child.is_dir():
            shutil.copytree(child, tgt)
        else:
            shutil.copy2(child, tgt)
    return {'ok': True, 'mode': 'global', 'restored_from': str(snap), 'pre_rollback_safety_backup': str(safety)}

class HatchTwinEggAgent(BasicAgent):
    """Generic twin egg hatcher.

    Loads a twin's identity from a local .egg, a public/private GitHub repo,
    or the current working directory.  Materializes a `~/.rapp/twins/<hash>/`
    workspace so the global brainstem's built-in `Twin` agent can boot and
    chat with it.
    """

    def __init__(self) -> None:
        self.name = 'HatchTwinEgg'
        self.metadata = {'name': self.name, 'description': "Hatch a twin from any source — a local .egg file, a public/private GitHub twin repo (e.g. 'kody-w/heimdall'), or the current directory if it contains a rappid.json.  Materializes ~/.rapp/twins/<hash>/ so the global brainstem's Twin agent can boot and chat with it.", 'parameters': {'type': 'object', 'properties': {'action': {'type': 'string', 'enum': ['hatch', 'rollback', 'status', 'list_twins'], 'description': "What to do.  Defaults to 'status'."}, 'mode': {'type': 'string', 'enum': ['twin', 'global'], 'description': "Where to hatch.  'twin' (default) = local workspace; 'global' = extend kernel."}, 'source': {'type': 'string', 'description': "owner/repo or github URL (e.g. 'kody-w/heimdall').  Set GH_TOKEN for private repos."}, 'egg': {'type': 'string', 'description': 'Path to a .egg file (zip).  Used for private/air-gapped twins.'}, 'name': {'type': 'string', 'description': "Optional alias to record alongside the source's rappid.json (does not change rappid)."}, 'description': {'type': 'string', 'description': "Optional human description recorded in the twin's rappid.json."}, 'rappid': {'type': 'string', 'description': "For action='rollback', the rappid of the twin to un-hatch (default: cwd auto-detect)."}}, 'required': []}}
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs: Any) -> str:
        action = str(kwargs.get('action') or 'status').lower().replace('-', '_')
        mode = str(kwargs.get('mode') or 'twin').lower()
        try:
            if action == 'hatch':
                if mode == 'global':
                    result = hatch_global(egg=kwargs.get('egg'), source=kwargs.get('source'))
                elif kwargs.get('egg'):
                    result = hatch_egg(kwargs['egg'])
                else:
                    result = hatch_twin(egg=kwargs.get('egg'), source=kwargs.get('source'), name=kwargs.get('name'), description=kwargs.get('description'))
            elif action == 'rollback':
                if mode == 'global':
                    result = rollback_global()
                else:
                    result = rollback_twin(rappid=kwargs.get('rappid'))
            elif action == 'list_twins':
                result = list_twins()
            elif action == 'status':
                result = status()
            else:
                result = {'ok': False, 'error': f'Unknown action: {action}'}
        except Exception as exc:
            result = {'ok': False, 'error': str(exc), 'action': action, 'mode': mode}
        return json.dumps(result, indent=2)

def _print(obj: Any) -> None:
    if isinstance(obj, (dict, list)):
        print(json.dumps(obj, indent=2))
    else:
        print(obj)

def _cli(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(prog='twin_egg_hatcher_agent.py', description='Generic single-file hatcher — any twin from any source.')
    sub = parser.add_subparsers(dest='cmd')
    p_hatch = sub.add_parser('hatch', help='Hatch a twin (default mode=twin).')
    p_hatch.add_argument('--mode', choices=['twin', 'global'], default='twin')
    p_hatch.add_argument('--source', help='owner/repo or github URL (e.g. kody-w/heimdall).')
    p_hatch.add_argument('--egg', help='Path to a .egg file (zip).')
    p_hatch.add_argument('--name', help='Optional display alias.')
    p_hatch.add_argument('--description', help='Optional description.')
    p_roll = sub.add_parser('rollback', help='Un-hatch.')
    p_roll.add_argument('--mode', choices=['twin', 'global'], default='twin')
    p_roll.add_argument('--rappid', help='Rappid of the twin to remove.')
    sub.add_parser('status', help='Show hatcher + brainstem + twins state.')
    sub.add_parser('list-twins', aliases=['list_twins', 'list', 'twins'], help='List all hatched twins.')
    if not argv:
        argv = ['status']
    ns = parser.parse_args(argv)
    cmd = ns.cmd or 'status'
    if cmd == 'hatch':
        if ns.mode == 'global':
            _print(hatch_global(egg=ns.egg, source=ns.source))
        elif ns.egg:
            _print(hatch_egg(ns.egg))
        else:
            _print(hatch_twin(egg=ns.egg, source=ns.source, name=ns.name, description=ns.description))
    elif cmd == 'rollback':
        if ns.mode == 'global':
            _print(rollback_global())
        else:
            _print(rollback_twin(rappid=ns.rappid))
    elif cmd == 'status':
        _print(status())
    elif cmd in ('list-twins', 'list_twins', 'list', 'twins'):
        _print(list_twins())
    else:
        parser.print_help()
        return 2
    return 0

if __name__ == '__main__':
    sys.exit(_cli(sys.argv[1:]))

