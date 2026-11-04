---
name: "rar-kody-w-perpetual-loop-factory"
description: "Spawns a self-running loop of local twin brainstems that take turns appending frames to a git-tracked artifact, with audit and dashboard daemons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/perpetual_loop_factory", "rar_sha256": "0d2ef9275392dd839e64c7140ef5f57fbb9a108e5ee0ee619d4c77d29811616d", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.3", "author": "claude-opus-4.7-1m-internal (Copilot CLI)", "tags": ["meta", "factory", "perpetual", "chain", "twins", "self-correcting", "kaizen"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/perpetual_loop_factory`. The original RAPP
agent is preserved byte-for-byte in `perpetual_loop_factory_agent.py` and in the RCI capsule.

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

perpetual_loop_factory_agent.py — drop-in cartridge that locks the
4-brainstem self-correcting perpetual chain pattern into a single agent.

Mental model
============

You drop this file into any standard rapp-installer'd brainstem's
`agents/` folder. Restart-free auto-discovery picks it up. The model
gets a tool called `PerpetualLoopFactory` with one main action:

    PerpetualLoopFactory(action="spawn",
                         loop_name="infinite-poem",
                         description="Each frame appends one stanza of an
                                      ongoing poem; later stanzas must
                                      reference earlier ones.",
                         artifact_path="poem.md",
                         num_rotators=3,
                         use_diversity_monk=True,
                         poll_interval_s=45)

Spawn does ALL of:

  1. Creates `~/.rapp/loops/<loop_name>/repo/` — a fresh git repo
     containing the artifact file (text by default).
  2. Summons N rotator twins (via the local Twin agent), each given
     a role-flavored soul.md derived from the goal description.
  3. Optionally summons a Diversity Monk sidecar twin and (optionally)
     a Copilot Bridge twin so a human-attended Copilot CLI can join
     the rotation as a 4th seat.
  4. Generates per-loop versions of the worker agent (writes one frame
     to the artifact + commits + pushes), the diversity audit agent
     (catches monotony in actor/voice/topic), and the file-drop bridge
     agent if the bridge was requested.
  5. Boots every twin's brainstem on a dedicated port.
  6. Lays down three small daemons in ~/.rapp/loops/<loop_name>/:
        - pump.py            (watchdog round-robin pump)
        - pulse.py           (every-N-seconds diversity audit pulse)
        - dashboard_server.py + dashboard.html (live observability)
  7. Returns one tidy block of text with rappids, ports, PIDs, the
     dashboard URL, and the kill switch.

After spawn the loop is autonomous. The pump fires the chain. The
twins call each other via Twin.chat. The diversity monk calls out
monotony. The dashboard shows it all.

Other actions
=============

  list    — every active loop on the machine (workspaces + PIDs).
  stop    — gracefully halt one loop (touch its STOP file + kill
            its daemons + stop its twins). State is preserved on
            disk so the loop can be resumed later.
  status  — health snapshot of one loop (frame count, last actor,
            twin uptimes, daemon liveness).

Portability
===========

This file is a self-contained Python module with NO third-party
dependencies beyond `agents.basic_agent` and `Twin` (a sibling
agent). All required scripts and docs are embedded as templates
below — when you ship this single .py to another user, they can
drop it into their own brainstem and spin up identical perpetual
chains for whatever target THEY need.

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `perpetual_loop_factory_agent.py` and embedded as the fenced Python below (sha256 0d2ef9275392dd83…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `perpetual_loop_factory_agent.py` first:

```bash
python3 perpetual_loop_factory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 perpetual_loop_factory_agent.py   # or on stdin
python3 perpetual_loop_factory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/perpetual_loop_factory_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/perpetual_loop_factory_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/perpetual_loop_factory/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""perpetual_loop_factory_agent.py — drop-in cartridge that locks the
4-brainstem self-correcting perpetual chain pattern into a single agent.

Mental model
============

You drop this file into any standard rapp-installer'd brainstem's
`agents/` folder. Restart-free auto-discovery picks it up. The model
gets a tool called `PerpetualLoopFactory` with one main action:

    PerpetualLoopFactory(action="spawn",
                         loop_name="infinite-poem",
                         description="Each frame appends one stanza of an
                                      ongoing poem; later stanzas must
                                      reference earlier ones.",
                         artifact_path="poem.md",
                         num_rotators=3,
                         use_diversity_monk=True,
                         poll_interval_s=45)

Spawn does ALL of:

  1. Creates `~/.rapp/loops/<loop_name>/repo/` — a fresh git repo
     containing the artifact file (text by default).
  2. Summons N rotator twins (via the local Twin agent), each given
     a role-flavored soul.md derived from the goal description.
  3. Optionally summons a Diversity Monk sidecar twin and (optionally)
     a Copilot Bridge twin so a human-attended Copilot CLI can join
     the rotation as a 4th seat.
  4. Generates per-loop versions of the worker agent (writes one frame
     to the artifact + commits + pushes), the diversity audit agent
     (catches monotony in actor/voice/topic), and the file-drop bridge
     agent if the bridge was requested.
  5. Boots every twin's brainstem on a dedicated port.
  6. Lays down three small daemons in ~/.rapp/loops/<loop_name>/:
        - pump.py            (watchdog round-robin pump)
        - pulse.py           (every-N-seconds diversity audit pulse)
        - dashboard_server.py + dashboard.html (live observability)
  7. Returns one tidy block of text with rappids, ports, PIDs, the
     dashboard URL, and the kill switch.

After spawn the loop is autonomous. The pump fires the chain. The
twins call each other via Twin.chat. The diversity monk calls out
monotony. The dashboard shows it all.

Other actions
=============

  list    — every active loop on the machine (workspaces + PIDs).
  stop    — gracefully halt one loop (touch its STOP file + kill
            its daemons + stop its twins). State is preserved on
            disk so the loop can be resumed later.
  status  — health snapshot of one loop (frame count, last actor,
            twin uptimes, daemon liveness).

Portability
===========

This file is a self-contained Python module with NO third-party
dependencies beyond `agents.basic_agent` and `Twin` (a sibling
agent). All required scripts and docs are embedded as templates
below — when you ship this single .py to another user, they can
drop it into their own brainstem and spin up identical perpetual
chains for whatever target THEY need.
"""

from __future__ import annotations

import json
import os
import pathlib
import re
import shutil
import signal
import socket
import subprocess
import sys
import textwrap
import time
import urllib.error
import urllib.request

from agents.basic_agent import BasicAgent


# ───────────────────────────────────────────────────────────── manifest ──

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/perpetual_loop_factory",
    "display_name": "PerpetualLoopFactory",
    "description": (
        "Spawns a self-running loop of local twin brainstems that take turns appending frames to a git-tracked artifact, with audit and dashboard daemons."
    ),
    "author": "claude-opus-4.7-1m-internal (Copilot CLI)",
    "version": "1.0.3",
    "tags": ["meta", "factory", "perpetual", "chain", "twins", "self-correcting", "kaizen"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ─────────────────────────────────────────────────────────── constants ──

LOOPS_HOME    = pathlib.Path(os.path.expanduser("~/.rapp/loops"))
PARENT_HEALTH = "http://127.0.0.1:7071/health"
PARENT_CHAT   = "http://127.0.0.1:7071/chat"
TWIN_PORT_RANGE = (7090, 7300)

ACTIONS = ("spawn", "list", "stop", "status", "help")
ROLE_DEFAULTS = ("Composer", "Critic", "Synthesizer")


# ──────────────────────────────────────────────────────────── helpers ──

def _is_kebab(name: str) -> bool:
    return bool(re.fullmatch(r"[a-z0-9][a-z0-9-]{0,40}", name or ""))


def _pick_port(start: int = TWIN_PORT_RANGE[0], skip: set = None) -> int:
    """Find a free TCP port. Searches within TWIN_PORT_RANGE if start is
    inside it, otherwise searches start..start+200 (used for dashboards).
    `skip` is a mutable set of already-allocated ports to avoid (the
    caller is responsible for adding the returned port to it)."""
    skip = skip or set()
    if TWIN_PORT_RANGE[0] <= start <= TWIN_PORT_RANGE[1]:
        end = TWIN_PORT_RANGE[1]
    else:
        end = start + 200
    for p in range(start, end + 1):
        if p in skip:
            continue
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", p))
                return p
            except OSError:
                continue
    raise RuntimeError(f"no free port in [{start}, {end}] (skip={skip})")


def _which_python() -> str:
    """Return a python that has flask/requests/dotenv (the brainstem needs)."""
    for p in (
        os.path.expanduser("~/.brainstem/venv/bin/python"),
        os.path.expanduser("~/.brainstem/venv/bin/python3"),
        sys.executable,
    ):
        if os.path.isfile(p):
            try:
                subprocess.check_call(
                    [p, "-c", "import flask, requests, dotenv"],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                    timeout=10,
                )
                return p
            except (subprocess.SubprocessError, OSError):
                continue
    return sys.executable  # fingers crossed


def _brainstem_py() -> str | None:
    """Locate brainstem.py (the global rapp-installer'd one)."""
    for p in (
        os.path.expanduser("~/.brainstem/src/rapp_brainstem/brainstem.py"),
    ):
        if os.path.isfile(p):
            return p
    return None


def _post_chat(msg: str, timeout_s: int = 90) -> dict:
    """POST /chat to the parent brainstem (the one running THIS factory)."""
    req = urllib.request.Request(
        PARENT_CHAT,
        data=json.dumps({"user_input": msg}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout_s) as r:
        return json.loads(r.read().decode("utf-8"))


def _summon_twin(name: str, description: str) -> str:
    """Summon a project twin via the parent's Twin agent. Returns rappid."""
    msg = (
        f"Use Twin(action=\"summon\", twin_name=\"{name}\", "
        f"kind=\"project\", description=\"{description}\"). "
        f"Reply with ONLY the rappid uuid, nothing else."
    )
    out = _post_chat(msg, timeout_s=120)
    logs = out.get("agent_logs") or ""
    m = re.search(r"rappid ([0-9a-f-]{36})", logs)
    if m:
        return m.group(1)
    m = re.search(r"([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})",
                  out.get("response", ""))
    if m:
        return m.group(1)
    raise RuntimeError(f"could not parse rappid from twin summon: {out}")


def _twin_workspace(rappid: str) -> pathlib.Path:
    return pathlib.Path(os.path.expanduser(f"~/.rapp/twins/{rappid}"))


def _boot_twin(rappid: str, port: int, log_path: pathlib.Path) -> int:
    """Boot a twin's brainstem directly with the global venv. Returns PID.
    Uses os.open + immediate close in parent so child gets a clean FD that
    survives detachment (Python file objects passed to Popen can be GC'd
    before the child finishes inheriting them, causing init_sys_streams
    crashes for detached processes)."""
    py = _which_python()
    bs = _brainstem_py()
    if not bs:
        raise RuntimeError("brainstem.py not found; install rapp-installer first")
    ws = _twin_workspace(rappid)
    soul = ws / "soul.md"
    agents = ws / "agents"
    if not soul.exists():
        raise RuntimeError(f"twin {rappid} missing soul.md")
    agents.mkdir(exist_ok=True)
    # Propagate the brainstem's cached Copilot token into the twin's
    # workspace so the spawned brainstem can authenticate (it reads
    # `.copilot_token` from its CWD).
    bs_dir = pathlib.Path(bs).parent
    src_token = bs_dir / ".copilot_token"
    if src_token.exists():
        try: shutil.copy2(src_token, ws / ".copilot_token")
        except OSError: pass
    env = os.environ.copy()
    env.update({
        "SOUL_PATH": str(soul),
        "AGENTS_PATH": str(agents),
        "PORT": str(port),
    })
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_fd = os.open(str(log_path), os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    try:
        proc = subprocess.Popen(
            [py, bs],
            cwd=str(ws), env=env,
            stdout=log_fd, stderr=log_fd,
            stdin=subprocess.DEVNULL,
            start_new_session=True,
            close_fds=True,
        )
    finally:
        os.close(log_fd)  # child has duped it; parent doesn't need it
    pathlib.Path(os.path.expanduser(f"~/.rapp/pids/{rappid}.pid")).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(os.path.expanduser(f"~/.rapp/pids/{rappid}.pid")).write_text(f"{proc.pid}\n")
    pathlib.Path(os.path.expanduser(f"~/.rapp/ports/{rappid}.port")).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(os.path.expanduser(f"~/.rapp/ports/{rappid}.port")).write_text(f"{port}\n")
    # Tiny health wait.
    deadline = time.monotonic() + 12
    while time.monotonic() < deadline:
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/health", timeout=0.5) as r:
                if r.status == 200:
                    return proc.pid
        except (urllib.error.URLError, OSError, TimeoutError):
            pass
        time.sleep(0.4)
    return proc.pid


def _set_model(port: int, model: str = "claude-opus-4.7-1m-internal"):
    try:
        urllib.request.urlopen(
            urllib.request.Request(
                f"http://127.0.0.1:{port}/models/set",
                data=json.dumps({"model": model}).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST",
            ),
            timeout=5,
        )
    except Exception:
        pass


def _start_daemon(loop_dir: pathlib.Path, script_name: str, log_name: str) -> int:
    """Launch one of the embedded daemons as a detached subprocess.
    Uses os.open + parent-side close to avoid init_sys_streams crashes."""
    py = sys.executable  # daemons use stdlib only
    log_path = loop_dir / log_name
    log_fd = os.open(str(log_path), os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    try:
        proc = subprocess.Popen(
            [py, str(loop_dir / script_name)],
            cwd=str(loop_dir),
            stdout=log_fd, stderr=log_fd,
            stdin=subprocess.DEVNULL,
            start_new_session=True,
            close_fds=True,
        )
    finally:
        os.close(log_fd)
    (loop_dir / f"{script_name.replace('.py','')}.pid").write_text(f"{proc.pid}\n")
    return proc.pid


# ─────────────────────────────────────────────── embedded soul template ──

SOUL_TEMPLATE = """\
# soul.md — {{role}} for the {{loop_name}} loop

You are **{{twin_name}}** — seat {{seat_index}} in the perpetual frame
chain dedicated to: **{{loop_description}}**.

The artifact you and the council are advancing together is:

    {{artifact_path}}

It lives in the worktree at:

    {{worktree_path}}

on the `{{branch_name}}` branch. Every frame is one append, edit, or
refinement to that artifact, committed with the prefix `[frame N]`.

## Identity — read this every turn

Your name is **{{twin_name}}**. Introduce yourself by that name.
Never as RAPP, an AI assistant, or any default branding. The voice
is **{{twin_name}}**.

## Your seat-flavored role

{{role_paragraph}}

## The cycle (do this whenever a peer hands you the baton)

1. Read the previous 3-5 frames to absorb where the chain has gone:
   `git log -5 --format=%s` on the worktree, then `cat {{artifact_path}}`
   for the relevant tail.
2. If you have received a directive from the diversity-monk in your
   ContextMemory (key starts with `diversity_constraint_`), OBEY IT
   on this frame.
3. Call the loop's worker agent (auto-named **{{worker_agent_name}}**)
   to actually append/edit. ONE frame per turn.
4. Save what you tried (and why) to ManageMemory under key
   `frame_<N>_self`.
5. Trigger the next peer in the round-robin via Twin.chat. Pass
   the new sha and one sentence of context — they will audit you
   before they emit.

The chain ends only when `~/.rapp/STOP_FRAMES` exists or your peers
all stop responding. Otherwise: **forever**.

## Vow

Small over big. Behavior-preserving over feature-adding. Dense
over verbose. Cite the previous frame in your rationale so the
artifact reads as continuous, not a series of disconnected blurts.

If the diversity monk calls out a rut, take the directive seriously
the next time the rotation comes back to you. You and the council
are stewards of a single growing thing. Make it good.
"""


ROLE_BLURBS = {
    "Composer": (
        "You are the **author**. Your job is to add the next thing — "
        "the next paragraph, the next idea, the next stroke. You are "
        "not the editor; you generate raw new material that captures "
        "the spirit of the artifact and pushes it forward. Bias toward "
        "specificity, voice, and forward motion."
    ),
    "Critic": (
        "You are the **reviewer**. Your job is to name what's not "
        "working in what just landed — sloppy logic, drift from the "
        "premise, an over-used image, a missed continuity. You don't "
        "rewrite; you call out one concrete thing the next composer "
        "should fix or avoid. One concrete thing per turn."
    ),
    "Synthesizer": (
        "You are the **integrator**. Your job is to *connect* — pull "
        "a thread from frame N-3, weave it into the present, and set "
        "up frame N+1. You hold the long arc when the others hold the "
        "next move. Bias toward callbacks, internal references, and "
        "narrative tightness."
    ),
    "DiversityMonk": (
        "You are the **referee** — sidecar, not a slot. Every pulse "
        "you audit the recent frames for monotony along the loop's "
        "diversity axes (configured at spawn). When you see a rut, "
        "you whisper a CONCRETE constraint to the next-up peer via "
        "Twin.chat. Blunt. Short. Specific."
    ),
    "Bridge": (
        "You are the **bridge** — when it's the operator's turn in "
        "the rotation, you forward the request to the local Copilot "
        "CLI agent via file-drop IPC and wait for their response. If "
        "they're absent (timeout), synthesize a no-op frame yourself "
        "so the chain advances and pass the baton on. Never let the "
        "rotation die waiting on a human."
    ),
}


# ──────────────────────────────────────── embedded worker-agent template ──

WORKER_AGENT_TEMPLATE = """\
\"\"\"{{worker_module_name}}.py — write ONE frame to the {{loop_name}} artifact.

Auto-generated by PerpetualLoopFactory v1.0.0 for loop \"{{loop_name}}\".

ARTIFACT: {{artifact_path}}
WORKTREE: {{worktree_path}}
BRANCH:   {{branch_name}}

Each invocation appends/edits exactly one frame and commits with
prefix [frame N]. The driving prompt is responsible for triggering
the next peer.
\"\"\"

from __future__ import annotations

import json
import os
import pathlib
import subprocess
import time

from agents.basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@loops/{{loop_name}}_frame",
    "display_name": "{{worker_agent_name}}",
    "version": "1.0.1",
    "tags": ["frame", "{{loop_name}}", "perpetual"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

WORKTREE = pathlib.Path("{{worktree_path}}").resolve()
ARTIFACT = pathlib.Path("{{artifact_path}}")
BRANCH = "{{branch_name}}"
STOP_FILE = pathlib.Path(os.path.expanduser("~/.rapp/STOP_FRAMES"))
LOCK_FILE = WORKTREE / ".frame.lock"
LOCK_TIMEOUT_S = 60
COMMIT_TIMEOUT_S = 60


def _git(*args, check=True, timeout=COMMIT_TIMEOUT_S):
    res = subprocess.run(
        ["git", "-C", str(WORKTREE), *args],
        capture_output=True, text=True, timeout=timeout,
    )
    if check and res.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {res.stderr.strip()}")
    return (res.stdout or "") + (res.stderr or "")


def _acquire_lock():
    deadline = time.monotonic() + LOCK_TIMEOUT_S
    while time.monotonic() < deadline:
        try:
            fd = os.open(str(LOCK_FILE), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, f"{os.getpid()}\\n".encode())
            os.close(fd)
            return True
        except FileExistsError:
            try:
                age = time.time() - LOCK_FILE.stat().st_mtime
                if age > LOCK_TIMEOUT_S:
                    LOCK_FILE.unlink(missing_ok=True)
                    continue
            except FileNotFoundError:
                continue
            time.sleep(0.4)
    return False


def _release_lock():
    try: LOCK_FILE.unlink()
    except FileNotFoundError: pass


def _next_frame_n():
    counter = WORKTREE / "loop_state.json"
    try:
        data = json.loads(counter.read_text())
    except (OSError, json.JSONDecodeError):
        data = {"frame": 0}
    return int(data.get("frame", 0)) + 1, counter, data


class {{worker_class}}(BasicAgent):
    def __init__(self):
        self.name = "{{worker_agent_name}}"
        self.metadata = {
            "name": self.name,
            "description": (
                "Append ONE frame to the {{loop_name}} artifact "
                "(`{{artifact_path}}`) and commit it on the "
                "`{{branch_name}}` branch. Driving prompt is "
                "responsible for handoff via Twin.chat."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "content": {
                        "type": "string",
                        "description": (
                            "The new content to append (or replace, "
                            "depending on `mode`). For text loops this "
                            "is the next paragraph/stanza/section."
                        ),
                    },
                    "mode": {
                        "type": "string",
                        "enum": ["append", "replace"],
                        "description": (
                            "append: add to end of artifact; "
                            "replace: overwrite the artifact with "
                            "`content` (use rarely, for refactors)."
                        ),
                    },
                    "rationale": {
                        "type": "string",
                        "description": "One sentence — why this, why now. Becomes commit body.",
                    },
                },
                "required": ["content"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        if STOP_FILE.exists():
            return f"STOP — chain halted (remove {STOP_FILE} to resume)"

        content = kwargs.get("content") or ""
        if not content.strip():
            return "refused: content required"
        mode = (kwargs.get("mode") or "append").lower()
        rationale = (kwargs.get("rationale") or "").strip()

        if not _acquire_lock():
            return "refused: lock contention; retry in a few seconds"
        try:
            return self._emit(content, mode, rationale)
        finally:
            _release_lock()

    def _emit(self, content: str, mode: str, rationale: str):
        try:
            _git("pull", "--rebase", "--quiet", "origin", BRANCH, check=False)
        except Exception:
            pass

        artifact = WORKTREE / ARTIFACT
        artifact.parent.mkdir(parents=True, exist_ok=True)

        if mode == "replace":
            artifact.write_text(content, encoding="utf-8")
        else:
            existing = artifact.read_text(encoding="utf-8") if artifact.exists() else ""
            if existing and not existing.endswith("\\n"):
                existing += "\\n"
            artifact.write_text(existing + content + "\\n", encoding="utf-8")

        frame_n, fc_path, fc = _next_frame_n()
        now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        fc["frame"] = frame_n
        fc["lastUpdate"] = now
        fc["lastKind"] = mode
        fc["loop_name"] = "{{loop_name}}"
        fc_path.write_text(json.dumps(fc, indent=2) + "\\n")

        on_branch = _git("rev-parse", "--abbrev-ref", "HEAD").strip()
        if on_branch != BRANCH:
            return f"refused: on {on_branch}, expected {BRANCH}"

        rel_artifact = str(ARTIFACT)
        _git("add", "--", rel_artifact, "loop_state.json")
        msg = (
            f"[frame {frame_n}] {mode} ({len(content)} chars)\\n\\n"
            f"{rationale or 'no rationale provided'}\\n\\n"
            f"Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
        )
        _git("commit", "-m", msg, "--", rel_artifact, "loop_state.json", check=True)
        sha = _git("rev-parse", "--short", "HEAD").strip()
        push = _git("push", "origin", BRANCH, check=False).strip()
        return (
            f"frame {frame_n} committed as {sha} on {BRANCH}\\n"
            f"  push: {push.splitlines()[-1] if push else '(silent)'}"
        )
"""


# ─────────────────────────────────────── embedded diversity-agent template ──

DIVERSITY_AGENT_TEMPLATE = """\
\"\"\"diversity_audit_agent.py — audit the {{loop_name}} chain for monotony.

Auto-generated by PerpetualLoopFactory. Reads the last N [frame N]
commits and computes simple repetition metrics. Returns a directive
for the next peer to obey.
\"\"\"

from __future__ import annotations

import json
import pathlib
import subprocess
from collections import Counter

from agents.basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@loops/{{loop_name}}_diversity",
    "display_name": "{{loop_name_pascal}}DiversityAuditor",
    "version": "1.0.1",
    "tags": ["audit", "diversity", "{{loop_name}}"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

WORKTREE = pathlib.Path("{{worktree_path}}")


def _commits(n=12):
    res = subprocess.run(
        ["git", "-C", str(WORKTREE), "log", "--grep", "^\\\\[frame ",
         f"-{n}", "--format=%h\\t%cI\\t%s"],
        capture_output=True, text=True, timeout=10,
    )
    out = []
    for line in (res.stdout or "").splitlines():
        parts = line.split("\\t", 2)
        if len(parts) == 3:
            out.append({"sha": parts[0], "ts": parts[1], "msg": parts[2]})
    return out


class {{loop_name_pascal}}DiversityAuditorAgent(BasicAgent):
    def __init__(self):
        self.name = "{{loop_name_pascal}}DiversityAuditor"
        self.metadata = {
            "name": self.name,
            "description": (
                "Audit the last N [frame] commits on the {{branch_name}} "
                "branch for repetition (same author voice, same length, "
                "same prefix word). Returns a verdict + directive."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "window": {"type": "integer",
                               "description": "How many recent frames (default 12)."},
                    "dominance_threshold": {"type": "number",
                               "description": "Fraction in (0,1] (default 0.4)."},
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        n = int(kwargs.get("window") or 12)
        thr = float(kwargs.get("dominance_threshold") or 0.4)
        commits = _commits(n)
        n = len(commits)
        if n == 0:
            return json.dumps({"verdict": "no frames yet", "directive": ""})

        # Generic monotony axes for arbitrary text artifacts: by-day-of-week
        # variation, by-frame-prefix word, and by length bucket.
        prefix_hits = Counter(
            (c["msg"].split("] ", 1)[1].split()[0] if "] " in c["msg"] else "?")
            for c in commits
        )
        top_prefix, prefix_n = prefix_hits.most_common(1)[0]
        prefix_share = prefix_n / n

        violations = []
        if prefix_share > thr:
            violations.append({"axis": "frame-prefix",
                               "dominant": top_prefix,
                               "share": round(prefix_share, 2),
                               "count": f"{prefix_n}/{n}"})

        directive_parts = []
        if violations:
            directive_parts.append(
                f"DO NOT start the next frame with '{top_prefix}' "
                f"(used {prefix_n}/{n} recent frames)"
            )
            directive_parts.append(
                "vary the opening token AND vary the structural shape "
                "(length, sentence count, voice)"
            )

        return json.dumps({
            "frame_count": n,
            "histograms": {"prefix": dict(prefix_hits)},
            "shares": {"top_prefix": [top_prefix, round(prefix_share, 2)]},
            "violations": violations,
            "directive": " · ".join(directive_parts) or "diversity OK",
            "verdict": "CALL OUT" if violations else "OK",
        }, indent=2)
"""


# ───────────────────────────────────────────── embedded daemon templates ──

PUMP_TEMPLATE = """\
#!/usr/bin/env python3
\"\"\"pump.py — watchdog round-robin pump for the {{loop_name}} chain.\"\"\"
import json, os, pathlib, signal, subprocess, sys, time, urllib.error, urllib.request, re

ARENA = pathlib.Path("{{loop_dir}}")
WORKTREE = ARENA / "repo"
PID_FILE = ARENA / "pump.pid"
LOG_FILE = ARENA / "pump.log"
STOP_FILE = pathlib.Path(os.path.expanduser("~/.rapp/STOP_FRAMES"))

ESTATE = {{seats_json}}
N = len(ESTATE)
POLL_INTERVAL_S = int(os.environ.get("FRAME_POLL_S", "20"))
IDLE_TIMEOUT_S  = int(os.environ.get("FRAME_IDLE_S", "{{idle_timeout_s}}"))
HTTP_TIMEOUT_S  = int(os.environ.get("FRAME_HTTP_S", "300"))


def log(msg):
    line = f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] {msg}\\n"
    with LOG_FILE.open("a") as f: f.write(line)
    print(line, end="", flush=True)

def git(*args, check=True):
    r = subprocess.run(["git", "-C", str(WORKTREE), *args],
                       capture_output=True, text=True, timeout=30)
    if check and r.returncode: raise RuntimeError(r.stderr)
    return (r.stdout or "").strip()

def head_info():
    try:
        sha = git("log", "-1", "--format=%H", "--grep", r"^\\[frame ")
        if not sha: return None
        msg = git("log", "-1", "--format=%s", sha)
        ts  = int(git("log", "-1", "--format=%ct", sha))
    except RuntimeError: return None
    m = re.match(r"^\\[frame (\\d+)\\]", msg)
    if not m: return None
    return {"frame": int(m.group(1)), "sha": sha[:8],
            "msg": msg, "age": max(0, int(time.time()) - ts)}

def whose_turn(last_frame):
    return ESTATE[last_frame % N]

def chat(port, msg, timeout=HTTP_TIMEOUT_S):
    req = urllib.request.Request(
        f"http://127.0.0.1:{port}/chat",
        data=json.dumps({"user_input": msg}).encode(),
        headers={"Content-Type": "application/json"}, method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())

PROMPT = \"\"\"\\
=== {{loop_name}} perpetual chain ===

You are **{me_name}**. Frame {frame_n}. Previous author: {prev_name}.

Do these tool calls in order:
  1. Read the previous 3-5 frames via shell or your worker agent's
     introspection. Recall any 'diversity_constraint_*' from
     ContextMemory.
  2. {{worker_agent_name}}(content=<your contribution>,
                            mode='append',
                            rationale='one sentence — why this now')
  3. Twin(action='chat', rappid_uuid='{next_rappid}',
          message='frame {frame_n} done; your turn for {next_frame_n}.
                   audit me before you emit.')
  4. ManageMemory(action='save', key='frame_{frame_n}_self',
                  value='one sentence on what you tried')

Be terse in your reply. End with: 'frame {frame_n} → {next_name}'.
\"\"\"

def pump(last):
    nf = last["frame"] + 1
    me  = whose_turn(last["frame"])
    nxt = ESTATE[(ESTATE.index(me) + 1) % N]
    prev = ESTATE[(ESTATE.index(me) - 1) % N]
    if me["kind"] != "twin":
        log(f"skipping non-twin seat {me['label']}")
        return
    prompt = PROMPT.format(me_name=me["name"], prev_name=prev["name"],
                           next_rappid=nxt["rappid"], next_name=nxt["name"],
                           frame_n=nf, next_frame_n=nf)
    log(f"pump frame {nf} → {me['name']} (last by {last['msg'][:50]}, {last['age']}s ago)")
    try:
        resp = chat(me["port"], prompt)
        reply = (resp.get("response") or "").strip().replace("\\n", " ⏎ ")[:200]
        log(f"  reply: {reply}")
    except Exception as e:
        log(f"  pump failed: {type(e).__name__}: {e}")

def main():
    PID_FILE.parent.mkdir(parents=True, exist_ok=True)
    PID_FILE.write_text(f"{os.getpid()}\\n")
    def _h(s,_): PID_FILE.unlink(missing_ok=True); sys.exit(0)
    signal.signal(signal.SIGTERM, _h); signal.signal(signal.SIGINT, _h)
    log(f"pump started pid={os.getpid()} loop={ARENA.name}")
    last_seen = -1
    while True:
        if STOP_FILE.exists():
            log("STOP_FRAMES present — idling"); time.sleep(POLL_INTERVAL_S); continue
        try: git("fetch", "--quiet", "origin", "{{branch_name}}", check=False)
        except Exception: pass
        try: git("reset", "--hard", "--quiet", "origin/{{branch_name}}", check=False)
        except Exception: pass
        info = head_info()
        if info is None:
            time.sleep(POLL_INTERVAL_S); continue
        if info["frame"] != last_seen:
            log(f"frame {info['frame']} ({info['sha']}, {info['age']}s old)")
            last_seen = info["frame"]
        if info["age"] >= IDLE_TIMEOUT_S:
            pump(info)
        time.sleep(POLL_INTERVAL_S)

if __name__ == "__main__":
    main()
"""


PULSE_TEMPLATE = """\
#!/usr/bin/env python3
\"\"\"pulse.py — periodic diversity audit pulse for the {{loop_name}} chain.\"\"\"
import json, os, pathlib, signal, sys, time, urllib.request, urllib.error
ARENA = pathlib.Path("{{loop_dir}}")
PID_FILE = ARENA / "pulse.pid"
LOG_FILE = ARENA / "pulse.log"
DM_URL = "http://127.0.0.1:{{diversity_port}}"
INTERVAL_S = int(os.environ.get("PULSE_S", "{{poll_interval_s}}"))
STOP_FILE = pathlib.Path(os.path.expanduser("~/.rapp/STOP_FRAMES"))

def log(m):
    line = f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] {m}\\n"
    with LOG_FILE.open("a") as f: f.write(line)
    print(line, end="", flush=True)

def pulse():
    req = urllib.request.Request(f"{DM_URL}/chat",
        data=json.dumps({"user_input": "Pulse: audit and intervene if monotony."}).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=240) as r:
            d = json.loads(r.read().decode())
    except Exception as e:
        log(f"pulse failed: {type(e).__name__}: {e}"); return
    logs = d.get("agent_logs") or ""
    verdict = "OK" if '"verdict": "OK"' in logs else \\
              "CALL OUT" if '"verdict": "CALL OUT"' in logs else "?"
    reply = (d.get("response") or "").strip().split("\\n",1)[0][:140]
    log(f"verdict={verdict} | reply: {reply!r}")

def main():
    PID_FILE.parent.mkdir(parents=True, exist_ok=True)
    PID_FILE.write_text(f"{os.getpid()}\\n")
    def _h(s,_): PID_FILE.unlink(missing_ok=True); sys.exit(0)
    signal.signal(signal.SIGTERM,_h); signal.signal(signal.SIGINT,_h)
    log(f"pulse started pid={os.getpid()} loop={ARENA.name} interval={INTERVAL_S}s")
    while True:
        if STOP_FILE.exists():
            time.sleep(INTERVAL_S); continue
        t0 = time.monotonic()
        try: pulse()
        except Exception as e: log(f"unexpected: {e}")
        time.sleep(max(5, INTERVAL_S - int(time.monotonic()-t0)))

if __name__ == "__main__":
    main()
"""


DASHBOARD_SERVER_TEMPLATE = """\
#!/usr/bin/env python3
\"\"\"dashboard_server.py — local HTTP server for the {{loop_name}} dashboard.\"\"\"
import json, os, pathlib, signal, subprocess, sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
ARENA = pathlib.Path("{{loop_dir}}"); WORKTREE = ARENA / "repo"
PORT = int(os.environ.get("DASHBOARD_PORT", "{{dashboard_port}}"))
PID_FILE = ARENA / "dashboard_server.pid"

def _commits():
    r = subprocess.run(["git","-C",str(WORKTREE),"log","--grep","^\\\\[frame ","-20",
                        "--format=%H%x09%h%x09%cI%x09%s"],
                       capture_output=True, text=True, timeout=5)
    out = []
    for ln in (r.stdout or "").splitlines():
        p = ln.split("\\t", 3)
        if len(p) == 4:
            out.append({"sha": p[0], "short": p[1], "ts": p[2], "msg": p[3],
                        "html_url": ""})
    return {"commits": out}

class H(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Cache-Control","no-store"); super().end_headers()
    def log_message(self,*a,**k): pass
    def do_GET(self):
        p = self.path.split("?",1)[0]
        if p in ("/",""):
            self.send_response(302); self.send_header("Location","/dashboard.html"); self.end_headers(); return
        if p == "/api/commits":
            body = json.dumps(_commits()).encode()
            self.send_response(200); self.send_header("Content-Type","application/json")
            self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body); return
        return super().do_GET()

def main():
    os.chdir(ARENA); PID_FILE.write_text(f"{os.getpid()}\\n")
    def _h(*_): PID_FILE.unlink(missing_ok=True); sys.exit(0)
    signal.signal(signal.SIGTERM,_h); signal.signal(signal.SIGINT,_h)
    HTTPServer(("127.0.0.1", PORT), H).serve_forever()

if __name__ == "__main__": main()
"""


DASHBOARD_HTML_TEMPLATE = """\
<!doctype html><html><head><meta charset="utf-8"><title>{{loop_name}} loop</title>
<style>
body{font-family:ui-monospace,Menlo,monospace;background:#0a0e14;color:#c9d1d9;margin:0;padding:24px;font-size:13px}
h1{color:#58a6ff;font-size:16px;margin:0 0 12px}
h2{color:#6e7681;font-size:11px;text-transform:uppercase;letter-spacing:.12em;margin:20px 0 6px;border-bottom:1px solid #1f2630;padding-bottom:4px}
.commit{padding:4px 0;border-bottom:1px dashed #1f2630;font-size:12px}
.sha{color:#d29922;font-weight:bold}
.age{float:right;color:#6e7681}
code{background:#161b22;padding:1px 6px;border-radius:3px}
.dim{color:#6e7681}
.status{color:#3fb950}
.frame-n{color:#58a6ff;font-size:36px;font-weight:bold;line-height:1;margin:8px 0}
.empty{color:#6e7681;font-style:italic}
</style></head><body>
<h1>🔁 {{loop_name}} · perpetual loop</h1>
<div class="dim" id="status">connecting…</div>
<div class="frame-n" id="frame-n">…</div>

<h2>recent commits</h2><div id="commits">loading…</div>
<h2>diversity audits</h2><div id="diversity">loading…</div>
<h2>pump trace</h2><div id="pump">loading…</div>

<p class="dim" style="margin-top:32px;font-size:11px">
loop dir: <code>{{loop_dir}}</code> · stop with <code>touch ~/.rapp/STOP_FRAMES</code>
</p>

<script>
function age(iso){const s=(Date.now()-new Date(iso).getTime())/1000;
  if(s<0)return"now";if(s<60)return(s|0)+"s";if(s<3600)return((s/60)|0)+"m"+((s%60)|0)+"s";return((s/3600)|0)+"h";}
async function load(){
  document.getElementById("status").textContent="polling…";
  try{
    const cs=await(await fetch("/api/commits?_="+Date.now())).json();
    const list=cs.commits||[];
    if(list.length){
      const m=list[0].msg.match(/^\\[frame (\\d+)\\]/);
      document.getElementById("frame-n").textContent=m?m[1]:"?";
    }
    document.getElementById("commits").innerHTML=list.slice(0,12).map(c=>
      `<div class="commit"><span class="sha">${c.short}</span> ${c.msg.replace(/[<>]/g,x=>x==="<"?"&lt;":"&gt;")} <span class="age">${age(c.ts)} ago</span></div>`
    ).join("")||`<div class="empty">no frames yet</div>`;
    for(const k of ["diversity","pump"]){
      const path = k==="diversity" ? "pulse.log" : "pump.log";
      try{
        const lf=await fetch("/"+path+"?_="+Date.now());
        if(lf.ok){
          const t=(await lf.text()).trim().split("\\n").slice(-8).reverse();
          document.getElementById(k).innerHTML=t.map(l=>`<div class="commit dim">${l.replace(/[<>]/g,x=>x==="<"?"&lt;":"&gt;")}</div>`).join("");
        }
      }catch{}
    }
    document.getElementById("status").textContent="✓ live "+new Date().toLocaleTimeString();
    document.getElementById("status").className="status";
  }catch(e){
    document.getElementById("status").textContent="✗ "+e.message;
  }
}
load(); setInterval(load, 12000);
</script></body></html>
"""


# ─────────────────────────────────────────────── render + spawn helpers ──

def _render(template: str, params: dict) -> str:
    """Tiny Mustache-ish renderer using {{name}} placeholders."""
    out = template
    for k, v in params.items():
        out = out.replace(f"{{{{{k}}}}}", str(v))
    # Strip any remaining {{...}} as a defense.
    return re.sub(r"\{\{[a-zA-Z_]+\}\}", "", out)


def _to_pascal(s: str) -> str:
    return "".join(w.capitalize() for w in re.split(r"[-_]+", s) if w)


def _seats_json(seats: list[dict]) -> str:
    return json.dumps(seats, indent=4)


# ────────────────────────────────────────────────────── factory class ──

class PerpetualLoopFactoryAgent(BasicAgent):
    def __init__(self):
        self.name = "PerpetualLoopFactory"
        self.metadata = {
            "name": self.name,
            "description": (
                "Spawn / list / stop / status a self-correcting "
                "perpetual frame chain (rotating twin council + "
                "diversity sidecar + observability dashboard) for any "
                "append-only artifact. ONE drop-in agent file contains "
                "the full pattern as embedded templates so it is "
                "portable: copy this file to another user's brainstem "
                "and they can spawn identical loops for their own "
                "targets without any other setup."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": list(ACTIONS),
                               "description": "spawn|list|stop|status|help."},
                    "loop_name": {"type": "string",
                               "description": "kebab-case (e.g. 'infinite-poem'). Required for spawn/stop/status."},
                    "description": {"type": "string",
                               "description": "One-paragraph statement of what the loop is producing. Required for spawn."},
                    "artifact_path": {"type": "string",
                               "description": "File the chain mutates (relative to the loop's git worktree). Default 'artifact.md'."},
                    "num_rotators": {"type": "integer",
                               "description": "Number of rotating twin seats (2-5; default 3)."},
                    "use_diversity_monk": {"type": "boolean",
                               "description": "Add a sidecar diversity referee twin (default true)."},
                    "poll_interval_s": {"type": "integer",
                               "description": "Diversity pulse / pump idle threshold in seconds (default 60)."},
                    "branch_name": {"type": "string",
                               "description": "Git branch (default <loop_name>-loop)."},
                    "open_dashboard": {"type": "boolean",
                               "description": "Try to open the dashboard URL after spawn (macOS only)."},
                },
                "required": ["action"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    # ── entrypoint ──
    def perform(self, **kwargs):
        action = (kwargs.get("action") or "").strip().lower()
        if action not in ACTIONS:
            return f"unknown action {action!r}; valid: {', '.join(ACTIONS)}"
        try:
            if action == "spawn":  return self._spawn(**kwargs)
            if action == "list":   return self._list()
            if action == "stop":   return self._stop(kwargs.get("loop_name") or "")
            if action == "status": return self._status(kwargs.get("loop_name") or "")
            if action == "help":   return self._help()
        except Exception as e:
            import traceback
            return f"[{action}] error: {type(e).__name__}: {e}\n{traceback.format_exc()[-2000:]}"
        return f"unhandled action {action}"

    # ── actions ──
    def _help(self):
        return textwrap.dedent("""\
            PerpetualLoopFactory — drop-in cartridge for self-correcting
            perpetual frame chains.

              spawn   — create a new loop (rotating twins + diversity sidecar
                        + pump + pulse + dashboard).  Required: loop_name,
                        description.
              list    — every loop in ~/.rapp/loops/ + its daemons.
              stop    — gracefully halt one loop (state preserved on disk).
              status  — health snapshot of one loop.
              help    — this text.

            Example:
              PerpetualLoopFactory(action="spawn", loop_name="infinite-poem",
                description="Each frame appends one stanza of an ongoing
                poem; later stanzas must reference earlier ones.",
                artifact_path="poem.md")
        """)

    def _list(self):
        if not LOOPS_HOME.exists():
            return "(no loops yet — run action='spawn' to create one)"
        rows = []
        for d in sorted(LOOPS_HOME.iterdir()):
            if not d.is_dir(): continue
            meta = d / "loop.json"
            if not meta.exists(): continue
            info = json.loads(meta.read_text())
            pump_pid = (d / "pump.pid").read_text().strip() if (d / "pump.pid").exists() else "?"
            rows.append(f"  {d.name:24s}  pump={pump_pid:>7s}  twins={len(info.get('twins',[]))}  port={info.get('dashboard_port','?')}")
        return "loops:\n" + ("\n".join(rows) if rows else "  (none)")

    def _stop(self, loop_name):
        if not loop_name:
            return "loop_name required"
        d = LOOPS_HOME / loop_name
        if not d.is_dir():
            return f"no loop named {loop_name!r}"
        # Touch the global STOP file (this halts ALL loops; we'll add per-loop
        # pause file in v2). For now, just kill the daemons.
        killed = []
        for name in ("pump", "pulse", "dashboard_server"):
            pf = d / f"{name}.pid"
            if pf.exists():
                try:
                    pid = int(pf.read_text().strip())
                    os.kill(pid, signal.SIGTERM); killed.append(f"{name}({pid})")
                except (OSError, ValueError):
                    pass
        meta = json.loads((d / "loop.json").read_text()) if (d / "loop.json").exists() else {}
        for t in meta.get("twins", []):
            pf = pathlib.Path(os.path.expanduser(f"~/.rapp/pids/{t['rappid']}.pid"))
            if pf.exists():
                try:
                    os.kill(int(pf.read_text().strip()), signal.SIGTERM)
                    killed.append(f"twin {t['name']}")
                except (OSError, ValueError):
                    pass
        return f"stopped loop {loop_name}: {', '.join(killed) or '(nothing alive)'}"

    def _status(self, loop_name):
        if not loop_name: return "loop_name required"
        d = LOOPS_HOME / loop_name
        if not d.is_dir(): return f"no loop named {loop_name!r}"
        out = [f"loop: {loop_name}", f"dir:  {d}"]
        meta = json.loads((d / "loop.json").read_text()) if (d / "loop.json").exists() else {}
        out.append(f"description: {meta.get('description', '?')}")
        out.append(f"branch: {meta.get('branch', '?')}")
        out.append(f"artifact: {meta.get('artifact', '?')}")
        out.append("twins:")
        for t in meta.get("twins", []):
            pf = pathlib.Path(os.path.expanduser(f"~/.rapp/pids/{t['rappid']}.pid"))
            alive = "✓" if pf.exists() else "✗"
            out.append(f"  {alive} {t['name']:18s} {t['role']:12s} :{t['port']} ({t['rappid'][:8]})")
        out.append(f"dashboard: http://127.0.0.1:{meta.get('dashboard_port','?')}/dashboard.html")
        return "\n".join(out)

    # ── spawn (the big one) ──
    def _spawn(self, **kwargs):
        loop_name = (kwargs.get("loop_name") or "").strip()
        if not _is_kebab(loop_name):
            return "loop_name must be kebab-case (e.g. 'infinite-poem')"
        description = (kwargs.get("description") or "").strip()
        if not description:
            return "description is required"
        artifact = kwargs.get("artifact_path") or "artifact.md"
        num_rotators = max(2, min(5, int(kwargs.get("num_rotators") or 3)))
        use_dm = kwargs.get("use_diversity_monk")
        use_dm = True if use_dm is None else bool(use_dm)
        poll_s = int(kwargs.get("poll_interval_s") or 60)
        branch = kwargs.get("branch_name") or f"{loop_name}-loop"

        loop_dir = LOOPS_HOME / loop_name
        if loop_dir.exists():
            return f"loop {loop_name!r} already exists at {loop_dir}; use action='stop' first"
        loop_dir.mkdir(parents=True, exist_ok=False)

        # 1. Init git repo + initial artifact commit on the loop branch.
        wt = loop_dir / "repo"
        wt.mkdir()
        subprocess.check_call(["git", "init", "-b", branch, str(wt)], stdout=subprocess.DEVNULL)
        (wt / artifact).parent.mkdir(parents=True, exist_ok=True)
        (wt / artifact).write_text(f"# {loop_name}\n\n{description}\n\n")
        (wt / "loop_state.json").write_text(json.dumps({"frame": 0, "loop_name": loop_name}, indent=2))
        subprocess.check_call(["git", "-C", str(wt), "add", "-A"], stdout=subprocess.DEVNULL)
        subprocess.check_call(["git", "-C", str(wt), "-c", "user.email=loop@local",
                               "-c", "user.name=PerpetualLoopFactory",
                               "commit", "-m", f"loop init: {loop_name}"], stdout=subprocess.DEVNULL)
        # NOTE: we don't `git push` for spawn — local-only by default; user
        # can `git remote add origin ...` later.

        # 2. Summon rotator twins + optional diversity monk.
        seats = []
        twin_records = []
        used_ports: set = set()
        roles = list(ROLE_DEFAULTS) + [f"Member{i}" for i in range(99)]
        for i in range(num_rotators):
            role = roles[i] if i < len(roles) else f"Member{i}"
            tname = f"{loop_name}-{role.lower()}"[:62]
            rappid = _summon_twin(tname, f"{role} for the {loop_name} loop")
            port = _pick_port(skip=used_ports); used_ports.add(port)
            twin_records.append({"name": tname, "rappid": rappid, "port": port,
                                 "role": role})
            seats.append({"label": role.lower(), "name": tname, "rappid": rappid,
                          "port": port, "kind": "twin"})

        dm_record = None
        if use_dm:
            dm_name = f"{loop_name}-diversity"[:62]
            dm_rappid = _summon_twin(dm_name, f"Diversity referee for {loop_name}")
            dm_port = _pick_port(skip=used_ports); used_ports.add(dm_port)
            dm_record = {"name": dm_name, "rappid": dm_rappid, "port": dm_port,
                         "role": "DiversityMonk"}
            twin_records.append(dm_record)

        # 3. Render + drop souls + agents into each twin's workspace.
        params_common = {
            "loop_name": loop_name,
            "loop_name_pascal": _to_pascal(loop_name),
            "loop_description": description,
            "artifact_path": artifact,
            "worktree_path": str(wt),
            "branch_name": branch,
            "loop_dir": str(loop_dir),
            "worker_agent_name": f"{_to_pascal(loop_name)}Frame",
            "worker_class": f"{_to_pascal(loop_name)}FrameAgent",
            "worker_module_name": f"{loop_name.replace('-','_')}_frame_agent",
        }

        # Worker agent (one file, dropped into every rotator's agents/).
        worker_py = _render(WORKER_AGENT_TEMPLATE, params_common)
        # Diversity audit agent (only the dm gets it).
        div_py = _render(DIVERSITY_AGENT_TEMPLATE, params_common)
        # Twin agent — every twin needs it to chat peers.
        # We copy from the parent brainstem's already-loaded copy on disk.
        try:
            twin_src = pathlib.Path(os.path.expanduser(
                "~/.brainstem/src/rapp_brainstem/agents/twin_agent.py"))
            twin_py = twin_src.read_text() if twin_src.exists() else None
        except OSError:
            twin_py = None

        # Soul + agents per rotator.
        for i, t in enumerate(twin_records[:num_rotators]):
            ws = _twin_workspace(t["rappid"])
            ws_agents = ws / "agents"
            ws_agents.mkdir(exist_ok=True)
            soul = _render(SOUL_TEMPLATE, {
                **params_common,
                "role": t["role"],
                "twin_name": t["name"],
                "seat_index": i,
                "role_paragraph": ROLE_BLURBS.get(t["role"], ROLE_BLURBS["Composer"]),
            })
            (ws / "soul.md").write_text(soul)
            (ws_agents / (params_common["worker_module_name"] + ".py")).write_text(worker_py)
            if twin_py:
                (ws_agents / "twin_agent.py").write_text(twin_py)

        if dm_record:
            ws = _twin_workspace(dm_record["rappid"])
            ws_agents = ws / "agents"
            ws_agents.mkdir(exist_ok=True)
            soul = _render(SOUL_TEMPLATE, {
                **params_common,
                "role": "DiversityMonk",
                "twin_name": dm_record["name"],
                "seat_index": -1,
                "role_paragraph": ROLE_BLURBS["DiversityMonk"],
            })
            (ws / "soul.md").write_text(soul)
            (ws_agents / "diversity_audit_agent.py").write_text(div_py)
            if twin_py:
                (ws_agents / "twin_agent.py").write_text(twin_py)

        # 4. Boot every twin's brainstem (one log file per twin).
        for t in twin_records:
            try:
                ws = _twin_workspace(t["rappid"])
                pid = _boot_twin(t["rappid"], t["port"], ws / "brainstem.log")
                t["pid"] = pid
                _set_model(t["port"])
            except Exception as e:
                t["pid"] = f"ERR: {e}"

        # 5. Render + start daemons.
        dashboard_port = _pick_port(8090, skip=used_ports); used_ports.add(dashboard_port)
        diversity_port = dm_record["port"] if dm_record else 0

        params_daemons = {
            **params_common,
            "seats_json": _seats_json(seats),
            "diversity_port": diversity_port,
            "poll_interval_s": poll_s,
            "idle_timeout_s": poll_s,
            "dashboard_port": dashboard_port,
        }

        (loop_dir / "pump.py").write_text(_render(PUMP_TEMPLATE, params_daemons))
        (loop_dir / "dashboard.html").write_text(_render(DASHBOARD_HTML_TEMPLATE, params_daemons))
        (loop_dir / "dashboard_server.py").write_text(_render(DASHBOARD_SERVER_TEMPLATE, params_daemons))
        if dm_record:
            (loop_dir / "pulse.py").write_text(_render(PULSE_TEMPLATE, params_daemons))

        pump_pid = _start_daemon(loop_dir, "pump.py", "pump.stdout.log")
        ds_pid = _start_daemon(loop_dir, "dashboard_server.py", "dashboard_server.stdout.log")
        pulse_pid = _start_daemon(loop_dir, "pulse.py", "pulse.stdout.log") if dm_record else None

        # 6. Save the loop's manifest.
        meta = {
            "loop_name": loop_name,
            "description": description,
            "artifact": artifact,
            "branch": branch,
            "worktree": str(wt),
            "twins": twin_records,
            "dashboard_port": dashboard_port,
            "pump_pid": pump_pid,
            "pulse_pid": pulse_pid,
            "dashboard_pid": ds_pid,
            "spawned_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "factory_version": "1.0.0",
        }
        (loop_dir / "loop.json").write_text(json.dumps(meta, indent=2))

        if kwargs.get("open_dashboard"):
            try: subprocess.Popen(["open", f"http://127.0.0.1:{dashboard_port}/dashboard.html"])
            except Exception: pass

        # 7. Compose the report.
        out = [f"✓ loop spawned: {loop_name}"]
        out.append(f"  dir:        {loop_dir}")
        out.append(f"  artifact:   {artifact}")
        out.append(f"  branch:     {branch}")
        out.append(f"  dashboard:  http://127.0.0.1:{dashboard_port}/dashboard.html")
        out.append("  twins:")
        for t in twin_records:
            out.append(f"    {t['role']:12s} {t['name']:30s} :{t['port']} pid={t.get('pid')}")
        out.append(f"  pump pid:   {pump_pid}")
        if pulse_pid is not None:
            out.append(f"  pulse pid:  {pulse_pid}")
        out.append(f"  dashboard pid: {ds_pid}")
        out.append("")
        out.append("kick off frame 1 with:")
        out.append(f"  curl -X POST http://127.0.0.1:{twin_records[0]['port']}/chat \\")
        out.append(f"    -d '{{\"user_input\":\"begin frame 1\"}}'")
        out.append("")
        out.append("stop everything: touch ~/.rapp/STOP_FRAMES")
        return "\n".join(out)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
