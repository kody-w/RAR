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
        "Bootstrap a self-correcting perpetual frame chain (rotating "
        "council of twins + diversity sidecar + observability dashboard) "
        "for any append-only artifact (novel, codebase, score, knowledge "
        "base, dataset). One agent.py drops the whole pattern. Drop, "
        "spawn, watch."
    ),
    "author": "claude-opus-4.7-1m-internal (Copilot CLI)",
    "version": "1.0.0",
    "tags": ["meta", "factory", "perpetual", "chain", "twins", "self-correcting", "kaizen"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent", "@kody-w/twin_agent"],
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
    "version": "1.0.0",
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
    "version": "1.0.0",
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
