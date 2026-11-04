---
name: "rar-kody-w-perpetual-loop-factory"
description: "Spawns a self-running loop of local twin brainstems that take turns appending frames to a git-tracked artifact, with audit and dashboard daemons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/perpetual_loop_factory", "rar_sha256": "0d2ef9275392dd839e64c7140ef5f57fbb9a108e5ee0ee619d4c77d29811616d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.3", "author": "claude-opus-4.7-1m-internal (Copilot CLI)", "tags": ["meta", "factory", "perpetual", "chain", "twins", "self-correcting", "kaizen"]}
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
