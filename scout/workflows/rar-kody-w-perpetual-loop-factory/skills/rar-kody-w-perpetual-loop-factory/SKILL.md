---
name: "rar-kody-w-perpetual-loop-factory"
description: "Spawns a self-running loop of local twin brainstems that take turns appending frames to a git-tracked artifact, with audit and dashboard daemons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/perpetual_loop_factory", "rar_sha256": "1e53fe183fd90dfda9e8c438e9d8b3fb82f98254763757ed87a9c28869477f53", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "perpetual_loop_factory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/perpetual-loop-factory:4b225f1abb9a64b97583f7287b5075d9acf7e64fc4916abdf0725cc5788b3ee3", "kind": "skill"}, "version": "1.0.3", "author": "claude-opus-4.7-1m-internal (Copilot CLI)", "tags": ["meta", "factory", "perpetual", "chain", "twins", "self-correcting", "kaizen"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/perpetual_loop_factory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `perpetual_loop_factory_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `perpetual_loop_factory_agent.py` and embedded as the fenced Python below (sha256 1e53fe183fd90dfd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `perpetual_loop_factory_agent.py` first:

```bash
python3 perpetual_loop_factory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 perpetual_loop_factory_agent.py   # or on stdin
python3 perpetual_loop_factory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
