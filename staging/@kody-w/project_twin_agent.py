"""ProjectTwin — single-file lifecycle agent for project-anchored twins.

One agent. Every verb the global brainstem needs to manage a project-twin
neighborhood through natural language:

  action=hatch        Create a project twin from the global kernel.
  action=hatch_all    Hatch a twin for every subdir of a parent dir.
  action=list         List all project twins on this device with status.
  action=status       Alias for list.
  action=boot         Spawn ./start.sh for a named twin (idempotent).
  action=chat         POST /chat to a twin (auto-boots if not running).
  action=dispatch     Fan-out natural-language message to many twins (async, returns job_id).
  action=job_status   Read kanban for a dispatched job from ~/.rapp/jobs/<id>/.
  action=await_job    Block until all twins in a dispatched job finish.
  action=stop         Kill the process listening on the twin's port.
  action=remove       Unlink twin's canonical entry (and optionally wipe anchor).

Spec conformance (sibling to twin_egg_hatcher_agent.py):
  - rappid.json schema rapp-rappid/2.0, kind="project", parent_rappid
    from ~/.brainstem/rappid.json. Same shape twin_egg_hatcher writes.
  - manifest.json schema rapp-twin-manifest/1.0 with port_hint.
  - HATCH_RECEIPT.json same fields the canonical hatcher writes.
  - Twin workspace symlinked at ~/.rapp/twins/<rappid-hash>/ so the global
    brainstem's built-in Twin agent (and any other twin-aware tool) picks
    it up automatically. Filesystem is the source of truth per
    TWIN_LIFECYCLE_SPEC §2 — no parallel device-side registry.
  - tracker_export uses the canonical 32-hex rappid hash as project id.
"""
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/project_twin_agent",
    "version": "0.3.2",
    "display_name": "ProjectTwin",
    "description": (
        "Single-file lifecycle agent for project-anchored brainstem twins. "
        "Hatch a twin from the global kernel into any project's directory, "
        "list/boot/chat/dispatch/stop/remove. Embeds the companion "
        "ProjectWorkspace agent (scoped git+file ops per twin) as a string "
        "constant — written into each new twin at hatch time. Pure transport "
        "surface: chat/dispatch carry your natural-language message verbatim "
        "to the twin(s); the twin's own LLM + agents decide what to do. "
        "Spec-compliant with kody-w/RAPP (rappid/2.0, manifest, hatch-receipt). "
        "Full spec: kody-w/RAPP-Network."
    ),
    "author": "kody-w",
    "tags": [
        "brainstem", "twin", "project", "hatch", "neighborhood",
        "dispatch", "network", "lifecycle", "singleton", "rapp-network",
    ],
    "category": "integrations",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import hashlib
import json
import os
import re
import shutil
import signal
import socket
import subprocess
import threading
import time
import urllib.error
import urllib.request
import uuid
from datetime import datetime, timezone
from pathlib import Path

from agents.basic_agent import BasicAgent


RAPP_HOME = Path(os.environ.get("RAPP_HOME", str(Path.home() / ".rapp")))
TWINS_DIR = RAPP_HOME / "twins"
JOBS_DIR = RAPP_HOME / "jobs"
HATCH_RECEIPT_NAME = "HATCH_RECEIPT.json"
HATCHER_VERSION = "project_twin/0.3.0"

# This agent is PURE TRANSPORT — it does not template, gate, or shape the
# messages flowing through it. The MESSAGE field on every chat/dispatch is the
# verbatim natural-language string the global brainstem (or its user) wants the
# twin to receive. The twin's own LLM + its own agents decide what to do with it.
# There is intentionally no "workflow" baked in here; if a user wants a twin to
# scan changes and update docs, they (or the global LLM composing for them) say
# that in plain English. Capability discovery: ask the twin "what can you do?"
# — it replies based on its own agent list. The global never has to know.

KERNEL_FILES = [
    "brainstem.py", "local_storage.py", "requirements.txt",
    "start.sh", "start.ps1", "index.html", "VERSION",
]
AGENT_HELPERS = ["basic_agent.py"]
# Default agents every project twin gets so it can do real work right away.
# Copied from global agents/ if present. Missing ones are silently skipped.
# Optional agents — copied into each new twin IF they exist in the global
# agents/ dir. They're nice-to-have, not required. The twin still works without
# them. (ProjectWorkspace is required and EMBEDDED below, not listed here.)
DEFAULT_PROJECT_AGENTS = [
    "context_memory_agent.py",
    "manage_memory_agent.py",
    "workiq_agent_agent.py",
]
# Env vars to scrub from the child process so the twin's own .env wins.
# Without this the child inherits PORT=7071 from the global and load_dotenv
# (which doesn't override existing vars by default) leaves the wrong port set.
ENV_TO_STRIP_FOR_CHILD = ["PORT", "SOUL_PATH", "AGENTS_PATH", "FLASK_RUN_PORT"]
AUTH_FILES = [".copilot_token", ".copilot_session"]
# GITHUB_MODEL is intentionally NOT inherited into the twin's .env — the model
# follows the global brainstem at boot time (the parent process passes its own
# GITHUB_MODEL via the child env, and load_dotenv won't override that). This
# way a `GITHUB_MODEL=...` change in the global .env auto-propagates to every
# twin on next boot, no per-twin updates required.
ENV_KEYS_TO_INHERIT = ["GITHUB_TOKEN", "VOICE_ZIP_PASSWORD", "TEAMS_CHANNEL_EMAIL"]
DEFAULT_PORT_FLOOR = 7073
BOOT_WAIT_SECONDS = 18
BOOT_POLL_INTERVAL = 0.5

# ---------------------------------------------------------------------------
# EMBEDDED COMPANION AGENT — ProjectWorkspace
#
# This file is the ONE drop-in for the whole project-twin neighborhood.
# Every project twin needs a ProjectWorkspace agent to do scoped git+file ops
# inside its own project root. To avoid requiring a second agent file in
# the global brainstem's agents/ dir, the full source is embedded below as
# a string. _do_hatch writes it into each new twin's agents/ at hatch time.
# ---------------------------------------------------------------------------
_PROJECT_WORKSPACE_AGENT_SRC = r'''
"""ProjectWorkspace — file & git capabilities scoped to the twin's project root.

A project twin lives at <project_root>/.brainstem/src/rapp_brainstem/. This
agent gives the twin's LLM full read access to <project_root> and SAFE write
access — every write is path-traversal-checked (must resolve inside the
project root), refused inside the .brainstem/ subtree, audit-logged, and
requires apply=true (default false means "preview only").

This is the agent the global brainstem's dispatch fans work out to — each
project twin uses its OWN ProjectWorkspace instance against its OWN project
tree, so the global never has to know anything project-specific.

Verbs:
  action=scan_changes  Recent commits + diff stats from git for this project.
  action=find_docs     Locate Markdown/doc files in the project.
  action=list_files    Glob inside the project root.
  action=read_file     Read one text file (size-capped, must be under root).
  action=write_file    Write/replace one file under project root. Required:
                       apply=true. Backs up the prior content as <file>.bak.<ts>.
"""
import json
import os
import re
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

from agents.basic_agent import BasicAgent


MAX_READ_BYTES = 200_000
AUDIT_LOG_NAME = "workspace_audit.log"
DEFAULT_DOC_PATTERNS = ["*.md", "README*", "CHANGELOG*", "CLAUDE.md", "docs", "DOCS"]


def _project_root() -> Path:
    """The user's project — parent of this twin's .brainstem/ subtree."""
    # this file: <project_root>/.brainstem/src/rapp_brainstem/agents/project_workspace_agent.py
    return Path(__file__).resolve().parents[4]


def _brainstem_dir() -> Path:
    """The twin's brainstem dir — never write here from this agent."""
    return Path(__file__).resolve().parents[1]


def _audit(event: dict) -> None:
    p = _brainstem_dir() / AUDIT_LOG_NAME
    event["ts"] = datetime.now(timezone.utc).isoformat()
    try:
        with p.open("a") as f:
            f.write(json.dumps(event) + "\n")
    except OSError:
        pass


def _resolve_under(path: str, root: Path) -> Path:
    if not path:
        return None
    p = (root / path) if not os.path.isabs(path) else Path(path)
    try:
        rp = p.resolve()
        rp.relative_to(root.resolve())
        return rp
    except (ValueError, OSError):
        return None


def _scan_changes(since: str = "14.days.ago", max_files: int = 40) -> dict:
    root = _project_root()
    # Locate the git repo via git itself — handles project_root being a subdir of a monorepo.
    try:
        top = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, timeout=10,
        )
    except (subprocess.SubprocessError, FileNotFoundError) as e:
        return {"error": f"git not available: {e}"}
    if top.returncode != 0:
        return {"error": f"not inside a git repo: {root}", "git_stderr": (top.stderr or "").strip()}
    toplevel = Path(top.stdout.strip())

    # Path relative to toplevel — used to scope log/diff to THIS project subdir.
    try:
        rel = root.resolve().relative_to(toplevel.resolve())
    except ValueError:
        rel = None
    scope_args = ["--", str(rel)] if (rel and str(rel) != ".") else []
    scope_label = str(rel) if (rel and str(rel) != ".") else "(toplevel)"

    try:
        log = subprocess.run(
            ["git", "-C", str(root), "log", "--since", since,
             "--pretty=format:%h%x09%an%x09%ad%x09%s", "--date=short", "-n", "50"] + scope_args,
            capture_output=True, text=True, timeout=20,
        )
        names = subprocess.run(
            ["git", "-C", str(root), "log", "--since", since, "--name-only",
             "--pretty=format:", "-n", "50"] + scope_args,
            capture_output=True, text=True, timeout=20,
        )
        stat = subprocess.run(
            ["git", "-C", str(root), "log", "--since", since, "--stat",
             "--pretty=format:%h %s", "-n", "20"] + scope_args,
            capture_output=True, text=True, timeout=20,
        )
    except (subprocess.SubprocessError, FileNotFoundError) as e:
        return {"error": f"git failed: {e}"}

    changed_files = []
    for line in (names.stdout or "").splitlines():
        line = line.strip()
        if line and line not in changed_files:
            changed_files.append(line)
    return {
        "ok": True,
        "project_root": str(root),
        "git_toplevel": str(toplevel),
        "scoped_to": scope_label,
        "since": since,
        "commit_count": len([c for c in (log.stdout or "").splitlines() if c.strip()]),
        "commits": (log.stdout or "").splitlines()[:50],
        "changed_files": changed_files[:max_files],
        "stat_summary": (stat.stdout or "")[:4000],
    }


def _find_docs(max_results: int = 80) -> dict:
    root = _project_root()
    docs = []
    skip_parts = {"node_modules", "venv", ".venv", "__pycache__", "dist", "build", ".brainstem"}
    for p in sorted(root.rglob("*.md")):
        rel = p.relative_to(root)
        if any(part.startswith(".") for part in rel.parts):
            continue
        if any(part in skip_parts for part in rel.parts):
            continue
        try:
            size = p.stat().st_size
        except OSError:
            continue
        docs.append({"path": str(rel), "size": size})
        if len(docs) >= max_results:
            break
    return {"ok": True, "project_root": str(root), "doc_count": len(docs), "docs": docs}


def _list_files(pattern: str = "**/*", max_results: int = 80) -> dict:
    root = _project_root()
    matches = []
    skip_parts = {"node_modules", "venv", ".venv", "__pycache__", ".git", ".brainstem"}
    for p in sorted(root.glob(pattern)):
        if not p.is_file():
            continue
        rel = p.relative_to(root)
        if any(part.startswith(".") for part in rel.parts):
            continue
        if any(part in skip_parts for part in rel.parts):
            continue
        matches.append(str(rel))
        if len(matches) >= max_results:
            break
    return {"ok": True, "project_root": str(root), "pattern": pattern, "matches": matches}


def _read_file(path: str) -> dict:
    root = _project_root()
    p = _resolve_under(path, root)
    if not p:
        return {"error": f"refused: path not inside project root ({root})"}
    if not p.exists():
        return {"error": f"file not found: {p.relative_to(root)}"}
    if not p.is_file():
        return {"error": f"not a regular file: {p.relative_to(root)}"}
    size = p.stat().st_size
    if size > MAX_READ_BYTES:
        return {"error": f"file too big ({size} bytes; cap is {MAX_READ_BYTES})",
                "path": str(p.relative_to(root)), "size": size}
    try:
        content = p.read_text(errors="replace")
    except OSError as e:
        return {"error": f"read failed: {e}"}
    return {"ok": True, "path": str(p.relative_to(root)), "size": size, "content": content}


def _write_file(path: str, content: str, apply: bool = False) -> dict:
    root = _project_root()
    p = _resolve_under(path, root)
    if not p:
        return {"error": f"refused: path outside project root ({root})"}
    if _resolve_under(str(p), _brainstem_dir()) is not None:
        return {"error": "refused: cannot write inside the .brainstem/ subtree"}
    rel = p.relative_to(root)
    p.parent.mkdir(parents=True, exist_ok=True)

    prev = ""
    if p.exists():
        try:
            prev = p.read_text(errors="replace")
        except OSError:
            prev = ""

    if not apply:
        _audit({"action": "write_preview", "path": str(rel),
                "prev_size": len(prev), "new_size": len(content)})
        return {
            "ok": True, "applied": False, "preview": True,
            "path": str(rel),
            "prev_size": len(prev), "new_size": len(content),
            "delta_bytes": len(content) - len(prev),
            "new_first_500": content[:500],
        }

    backup_path = None
    if p.exists():
        backup_path = p.with_suffix(p.suffix + f".bak.{int(time.time())}")
        try:
            backup_path.write_text(prev)
        except OSError as e:
            return {"error": f"backup failed: {e}"}
    try:
        p.write_text(content)
    except OSError as e:
        return {"error": f"write failed: {e}"}
    _audit({"action": "write_file", "path": str(rel), "size": len(content),
            "backup": str(backup_path.relative_to(root)) if backup_path else None})
    return {
        "ok": True, "applied": True,
        "path": str(rel),
        "size": len(content),
        "backup": str(backup_path.relative_to(root)) if backup_path else None,
    }


class ProjectWorkspaceAgent(BasicAgent):
    def __init__(self):
        self.name = "ProjectWorkspace"
        self.metadata = {
            "name": self.name,
            "description": (
                "File and git capabilities scoped to THIS project twin's project root. "
                "Use this agent when the user wants to scan recent code changes, find docs, "
                "read files, or write/update files inside this project. Writes require "
                "apply=true (default is dry-run preview). Writes inside the .brainstem/ "
                "subtree are refused. Every write is backed up as <file>.bak.<ts>."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["scan_changes", "find_docs", "list_files", "read_file", "write_file"],
                        "description": "Which workspace verb to run.",
                    },
                    "since": {"type": "string", "description": "For action=scan_changes: git-log --since value, e.g. '7.days.ago', '2026-05-01'. Default: '14.days.ago'."},
                    "pattern": {"type": "string", "description": "For action=list_files: glob (default '**/*')."},
                    "path": {"type": "string", "description": "For action=read_file or write_file: path relative to the project root (or absolute, but must resolve inside root)."},
                    "content": {"type": "string", "description": "For action=write_file: the new file contents."},
                    "apply": {"type": "boolean", "description": "For action=write_file: must be true to actually write. False (default) returns a preview only."},
                    "max_results": {"type": "integer", "description": "Cap for find_docs / list_files."},
                    "max_files": {"type": "integer", "description": "Cap for scan_changes changed-file list."},
                },
                "required": ["action"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action = kwargs.get("action") or "scan_changes"
        try:
            if action == "scan_changes":
                return json.dumps(_scan_changes(
                    since=kwargs.get("since", "14.days.ago"),
                    max_files=int(kwargs.get("max_files") or 40),
                ), indent=2)
            if action == "find_docs":
                return json.dumps(_find_docs(int(kwargs.get("max_results") or 80)), indent=2)
            if action == "list_files":
                return json.dumps(_list_files(
                    pattern=kwargs.get("pattern", "**/*"),
                    max_results=int(kwargs.get("max_results") or 80),
                ), indent=2)
            if action == "read_file":
                return json.dumps(_read_file(kwargs.get("path", "")), indent=2)
            if action == "write_file":
                return json.dumps(_write_file(
                    kwargs.get("path", ""),
                    kwargs.get("content", ""),
                    bool(kwargs.get("apply", False)),
                ), indent=2)
            return json.dumps({
                "error": f"unknown action: {action}",
                "valid": ["scan_changes", "find_docs", "list_files", "read_file", "write_file"],
            })
        except Exception as e:
            return json.dumps({"error": f"{type(e).__name__}: {e}", "action": action})
'''



# Consolidated form: `rappid:@<owner>/<slug>:<64hex>` (256-bit, no trailing @suffix).
# Legacy form (still read): `rappid:v2:<kind>:@<owner>/<slug>:<32hex>@github.com/...`.
_HASH_RE = re.compile(r":([a-f0-9]{64})$|:([a-f0-9]{32})@")
_AGENT_NAME_RE = re.compile(r"""self\.name\s*=\s*['"]([^'"]+)['"]""")
_AGENT_DESC_RE = re.compile(r"""['"]description['"]\s*:\s*\(?\s*['"]([^'"]+)['"]""")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _global_brainstem_dir() -> Path:
    return Path(__file__).resolve().parent.parent


def _hash_from_rappid(rappid: str) -> str:
    if rappid and rappid.startswith("rappid:"):
        m = _HASH_RE.search(rappid)
        if m:
            return m.group(1) or m.group(2)
    return rappid or ""


def _mint_v2_rappid(kind: str, owner: str, repo: str) -> str:
    # Canonical RAPP §6.2 keyless mint: rappid:@<owner>/<slug>:<64hex>, tail is
    # Hb("rapp/1:rappid", uuid4) (domain-separated, never a name-hash). owner/repo
    # are canonicalized to the §6.1 grammar so a real login "Kody-W" / repo
    # "My_Repo" yields a valid rappid. `kind` lives in the record, not the string.
    _o = re.sub(r"[^a-z0-9]+", "-", (owner or "anon").lower()).strip("-") or "anon"
    _r = re.sub(r"[^a-z0-9]+", "-", (repo or "x").lower()).strip("-") or "x"
    digest = hashlib.sha256(b"rapp/1:rappid\n" + uuid.uuid4().bytes).hexdigest()
    return f"rappid:@{_o}/{_r}:{digest}"


def _slug(s: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", s.strip().lower()).strip("-")
    return s or "project"


def _port_is_free(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind(("127.0.0.1", port))
        except OSError:
            return False
    return True


def _port_in_use(port: int) -> bool:
    """True if something is listening on the port (twin is running)."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.3)
        return s.connect_ex(("127.0.0.1", port)) == 0


def _ports_taken_by_twins() -> set:
    taken = set()
    if not TWINS_DIR.exists():
        return taken
    for entry in TWINS_DIR.iterdir():
        if entry.name.startswith("."):
            continue
        mpath = entry / "manifest.json"
        if not mpath.exists():
            continue
        try:
            m = json.loads(mpath.read_text())
            p = m.get("port_hint") or m.get("port")
            if isinstance(p, int):
                taken.add(p)
        except (json.JSONDecodeError, OSError):
            pass
    return taken


def _pick_port(floor: int, also_avoid: set) -> int:
    taken = _ports_taken_by_twins() | (also_avoid or set())
    port = floor
    while port < 7200:
        if port not in taken and _port_is_free(port):
            return port
        port += 1
    raise RuntimeError(f"no free port in [{floor}, 7200)")


def _read_env(path: Path) -> dict:
    env = {}
    if not path.exists():
        return env
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        env[k.strip()] = v.strip()
    return env


def _write_env(path: Path, env: dict) -> None:
    # NOTE: GITHUB_MODEL is intentionally not in this list — twins follow the
    # global's GITHUB_MODEL at boot time (parent injects via child env).
    lines = ["# Generated by ProjectTwin — edit values, never the kernel.",
             "# GITHUB_MODEL is not set here; the twin uses the global brainstem's",
             "# current model choice automatically. Override only by adding the",
             "# line manually if you need this twin to pin to a different model.",
             ""]
    for k in ["GITHUB_TOKEN", "SOUL_PATH", "AGENTS_PATH", "PORT", "VOICE_ZIP_PASSWORD", "TEAMS_CHANNEL_EMAIL"]:
        if k in env:
            lines.append(f"{k}={env[k]}")
    path.write_text("\n".join(lines) + "\n")


def _read_global_rappid() -> dict:
    p = Path.home() / ".brainstem" / "rappid.json"
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text())
    except (json.JSONDecodeError, OSError):
        return {}


def _derive_owner_repo(project_root: Path) -> tuple:
    try:
        out = subprocess.run(
            ["git", "-C", str(project_root), "remote", "get-url", "origin"],
            capture_output=True, text=True, timeout=4
        )
        if out.returncode == 0:
            m = re.search(r"github\.com[:/]+([^/]+)/([^/.\s]+)(?:\.git)?", out.stdout.strip())
            if m:
                return m.group(1), m.group(2)
    except (subprocess.SubprocessError, FileNotFoundError):
        pass
    return None, None


def _parse_agent_meta(filepath: Path) -> tuple:
    fallback = filepath.stem.replace("_agent", "").replace("_", " ").title().replace(" ", "")
    try:
        src = filepath.read_text(errors="replace")
    except OSError:
        return fallback, ""
    n = _AGENT_NAME_RE.search(src)
    d = _AGENT_DESC_RE.search(src)
    return n.group(1) if n else fallback, d.group(1) if d else ""


def _link_canonical_twin(twin_hash: str, target_dir: Path, force: bool = True) -> dict:
    TWINS_DIR.mkdir(parents=True, exist_ok=True)
    link = TWINS_DIR / twin_hash
    if link.is_symlink():
        current = os.readlink(link)
        if Path(current).resolve() == target_dir.resolve():
            return {"link": str(link), "target": str(target_dir), "status": "already-linked"}
        if not force:
            return {"link": str(link), "target": str(target_dir), "status": "exists-other", "current": current}
        link.unlink()
        link.symlink_to(target_dir, target_is_directory=True)
        return {"link": str(link), "target": str(target_dir), "status": "relinked"}
    if link.exists():
        return {"link": str(link), "target": str(target_dir), "status": "exists-real-dir", "warning": "canonical path is a real dir; left untouched"}
    link.symlink_to(target_dir, target_is_directory=True)
    return {"link": str(link), "target": str(target_dir), "status": "linked"}


def _list_project_twins() -> list:
    """Scan ~/.rapp/twins/ and return only project-kind twins with full status."""
    out = []
    if not TWINS_DIR.exists():
        return out
    for entry in sorted(TWINS_DIR.iterdir()):
        if entry.name.startswith("."):
            continue
        rj = entry / "rappid.json"
        if not rj.exists():
            continue
        try:
            rd = json.loads(rj.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        if rd.get("kind") != "project":
            continue
        mj = entry / "manifest.json"
        md = {}
        if mj.exists():
            try:
                md = json.loads(mj.read_text())
            except (json.JSONDecodeError, OSError):
                pass
        port = md.get("port_hint") or md.get("port")
        anchor = md.get("anchor_path") or rd.get("_planted_at_path") or str(entry.resolve())
        running = bool(port) and _port_in_use(int(port))
        out.append({
            "hash": entry.name,
            "name": rd.get("name") or entry.name,
            "display_name": rd.get("display_name"),
            "rappid": rd.get("rappid"),
            "port": port,
            "anchor": anchor,
            "running": running,
            "url": f"http://localhost:{port}" if (port and running) else None,
        })
    return out


def _resolve_twin(name_or_hash: str) -> Path:
    """Find a project twin's workspace by hash, hash-prefix, or name."""
    if not name_or_hash:
        return None
    if (TWINS_DIR / name_or_hash).exists():
        return TWINS_DIR / name_or_hash
    twins = _list_project_twins()
    # Exact name
    for t in twins:
        if t["name"] == name_or_hash or t.get("display_name") == name_or_hash:
            return TWINS_DIR / t["hash"]
    # Hash prefix
    for t in twins:
        if t["hash"].startswith(name_or_hash):
            return TWINS_DIR / t["hash"]
    # Loose name (slug match)
    slug = _slug(name_or_hash)
    for t in twins:
        if _slug(t["name"]) == slug or (t.get("display_name") and _slug(t["display_name"]) == slug):
            return TWINS_DIR / t["hash"]
    return None


def _read_port(ws: Path):
    mj = ws / "manifest.json"
    if not mj.exists():
        return None
    try:
        return json.loads(mj.read_text()).get("port_hint")
    except (json.JSONDecodeError, OSError):
        return None


def _pid_on_port(port: int):
    try:
        out = subprocess.run(["lsof", "-tiTCP:" + str(port), "-sTCP:LISTEN", "-n", "-P"],
                             capture_output=True, text=True, timeout=3)
        pid = out.stdout.strip().split("\n")[0]
        return int(pid) if pid else None
    except (subprocess.SubprocessError, ValueError, FileNotFoundError):
        return None


def _boot_twin(name_or_hash: str) -> dict:
    ws = _resolve_twin(name_or_hash)
    if not ws:
        return {"error": f"no project twin matching: {name_or_hash}", "hint": "try action=list"}
    port = _read_port(ws)
    if not port:
        return {"error": f"no port_hint in {ws}/manifest.json"}
    if _port_in_use(port):
        return {"ok": True, "name": name_or_hash, "port": port, "url": f"http://localhost:{port}",
                "already_running": True, "pid": _pid_on_port(port)}
    start_sh = ws / "start.sh"
    if not start_sh.exists():
        return {"error": f"no start.sh in {ws}"}
    try:
        os.chmod(start_sh, 0o755)
    except OSError:
        pass
    log_path = ws / "boot.log"
    log_fh = open(log_path, "a")
    # Scrub env vars that would shadow the twin's own .env (load_dotenv doesn't
    # override existing process env vars by default).
    child_env = {k: v for k, v in os.environ.items() if k not in ENV_TO_STRIP_FOR_CHILD}
    child_env["PORT"] = str(port)
    proc = subprocess.Popen(
        ["bash", str(start_sh)],
        cwd=str(ws.resolve()),
        stdout=log_fh, stderr=subprocess.STDOUT,
        start_new_session=True,
        env=child_env,
    )
    waited = 0.0
    while waited < BOOT_WAIT_SECONDS:
        if _port_in_use(port):
            return {"ok": True, "name": name_or_hash, "port": port, "url": f"http://localhost:{port}",
                    "pid": proc.pid, "started_now": True, "waited_seconds": round(waited, 1),
                    "boot_log": str(log_path)}
        time.sleep(BOOT_POLL_INTERVAL)
        waited += BOOT_POLL_INTERVAL
    return {"error": f"twin did not bind port {port} within {BOOT_WAIT_SECONDS}s",
            "name": name_or_hash, "pid": proc.pid, "boot_log": str(log_path)}


def _remove_twin(name_or_hash: str, wipe_anchor: bool = False) -> dict:
    """Remove a project twin from the device. By default only unlinks the
    canonical symlink at ~/.rapp/twins/<hash>/ and stops the process — the
    project-anchored dir at <project>/.brainstem/src/rapp_brainstem/ is left
    intact (least-surprise). With wipe_anchor=True, also rm -rf the anchor."""
    ws = _resolve_twin(name_or_hash)
    if not ws:
        return {"error": f"no project twin matching: {name_or_hash}"}
    # Resolve anchor BEFORE we touch the symlink so we can rm the real path.
    anchor = None
    try:
        anchor = Path(os.readlink(ws)) if ws.is_symlink() else ws.resolve()
    except OSError:
        anchor = ws.resolve()
    # Stop if running
    port = _read_port(ws)
    stop_result = None
    if port and _port_in_use(int(port)):
        stop_result = _stop_twin(name_or_hash)
    # Unlink the symlink (or rm the dir if it's a real dir at the canonical path)
    canonical_removed = False
    if ws.is_symlink():
        try:
            ws.unlink()
            canonical_removed = True
        except OSError as e:
            return {"error": f"failed to unlink {ws}: {e}"}
    elif ws.exists():
        return {"error": f"canonical path {ws} is a real directory, not a symlink — refusing to recurse-delete without manual review"}
    # Optionally wipe the anchor (project-resident dir)
    anchor_removed = False
    if wipe_anchor and anchor and anchor.exists():
        try:
            shutil.rmtree(anchor)
            anchor_removed = True
        except OSError as e:
            return {"error": f"unlinked canonical but failed to wipe anchor {anchor}: {e}", "canonical_removed": canonical_removed}
    return {
        "ok": True,
        "name": name_or_hash,
        "canonical_link_removed": canonical_removed,
        "anchor_removed": anchor_removed,
        "anchor_preserved_at": str(anchor) if (anchor and not anchor_removed) else None,
        "stopped": stop_result,
    }


def _stop_twin(name_or_hash: str) -> dict:
    ws = _resolve_twin(name_or_hash)
    if not ws:
        return {"error": f"no project twin matching: {name_or_hash}"}
    port = _read_port(ws)
    if not port:
        return {"error": f"no port_hint in {ws}/manifest.json"}
    if not _port_in_use(port):
        return {"ok": True, "name": name_or_hash, "port": port, "note": "already stopped"}
    pid = _pid_on_port(port)
    if not pid:
        return {"ok": True, "port": port, "note": "port in use but pid not resolvable"}
    try:
        os.kill(pid, signal.SIGTERM)
        for _ in range(20):
            time.sleep(0.2)
            if not _port_in_use(port):
                return {"ok": True, "name": name_or_hash, "port": port, "stopped_pid": pid}
        os.kill(pid, signal.SIGKILL)
        return {"ok": True, "name": name_or_hash, "port": port, "stopped_pid": pid, "force_killed": True}
    except ProcessLookupError:
        return {"ok": True, "port": port, "note": "process already gone"}
    except OSError as e:
        return {"error": f"kill failed: {e}"}


def _chat_with_twin(name_or_hash: str, message: str, auto_boot: bool = True, timeout: int = 60) -> dict:
    if not message:
        return {"error": "message is required"}
    ws = _resolve_twin(name_or_hash)
    if not ws:
        return {"error": f"no project twin matching: {name_or_hash}"}
    port = _read_port(ws)
    if not port:
        return {"error": f"no port_hint in {ws}/manifest.json"}
    booted = None
    if not _port_in_use(port):
        if not auto_boot:
            return {"error": f"twin {name_or_hash} not running on port {port}; set auto_boot=true"}
        booted = _boot_twin(name_or_hash)
        if booted.get("error"):
            return {"error": "auto-boot failed", "boot_result": booted}
    req = urllib.request.Request(
        f"http://127.0.0.1:{port}/chat",
        data=json.dumps({"user_input": message}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode("utf-8"))
    except (socket.timeout, TimeoutError) as e:
        return {"error": f"twin chat timed out after {timeout}s: {e}", "port": port}
    except urllib.error.URLError as e:
        return {"error": f"http error: {e}", "port": port}
    except (json.JSONDecodeError, ValueError, OSError) as e:
        return {"error": f"bad response or connection issue: {e}", "port": port}
    except Exception as e:
        return {"error": f"chat failed: {type(e).__name__}: {e}", "port": port}
    reply = data.get("response") or data.get("assistant_response") or ""
    # Strip the |||VOICE||| / |||TWIN||| trailer for the headline reply but
    # also surface the raw response + the twin's own agent_logs so the global
    # brainstem can introspect WHICH of the twin's agents the twin used.
    main = reply.split("|||VOICE|||")[0].strip()
    return {
        "ok": True,
        "name": name_or_hash,
        "port": port,
        "url": f"http://localhost:{port}",
        "reply": main,
        "voice": (reply.split("|||VOICE|||", 1)[1].split("|||TWIN|||", 1)[0].strip()
                  if "|||VOICE|||" in reply else None),
        "raw_response": reply,
        "twin_agent_logs": (data.get("agent_logs") or "")[:8000],
        "auto_booted": bool(booted),
    }


# ---------------------------------------------------------------------------
# Hatch (core creation verb)
# ---------------------------------------------------------------------------

def _do_hatch(**kwargs) -> dict:
    project_path = (kwargs.get("project_path") or "").strip()
    if not project_path:
        return {"error": "project_path is required for hatch"}
    project_root = Path(project_path).expanduser().resolve()
    if not project_root.exists() or not project_root.is_dir():
        return {"error": f"project_path not a directory: {project_root}"}

    global_dir = _global_brainstem_dir()
    target_dir = project_root / ".brainstem" / "src" / "rapp_brainstem"
    target_agents = target_dir / "agents"
    target_agents.mkdir(parents=True, exist_ok=True)

    # Kernel + helpers (verbatim copy)
    copied, missing = [], []
    for fname in KERNEL_FILES:
        src = global_dir / fname
        if src.exists():
            shutil.copy2(src, target_dir / fname)
            copied.append(fname)
        else:
            missing.append(fname)
    for fname in AGENT_HELPERS:
        src = global_dir / "agents" / fname
        if src.exists():
            shutil.copy2(src, target_agents / fname)
            copied.append(f"agents/{fname}")
    # Always write the EMBEDDED ProjectWorkspace agent — no external file required.
    # This is what makes project_twin_agent.py a true one-drop-in deliverable: it
    # carries its companion agent inside itself, ready to materialize on every hatch.
    (target_agents / "project_workspace_agent.py").write_text(_PROJECT_WORKSPACE_AGENT_SRC)
    copied.append("agents/project_workspace_agent.py (embedded)")
    # Opportunistic — copy if the global has them; if not, twins still work fully.
    for fname in DEFAULT_PROJECT_AGENTS:
        src = global_dir / "agents" / fname
        if src.exists():
            shutil.copy2(src, target_agents / fname)
            copied.append(f"agents/{fname}")

    # soul.md (preserve project's)
    preserved = []
    force_soul = bool(kwargs.get("force_soul", False))
    target_soul = target_dir / "soul.md"
    if target_soul.exists() and not force_soul:
        preserved.append("soul.md")
    elif (global_dir / "soul.md").exists():
        shutil.copy2(global_dir / "soul.md", target_soul)
        copied.append("soul.md")

    # Identity (derive coords, mint rappid, idempotent on re-hatch)
    global_rappid_doc = _read_global_rappid()
    parent_rappid = global_rappid_doc.get("rappid")
    operator_github = global_rappid_doc.get("github")

    owner = kwargs.get("owner") or None
    repo = kwargs.get("repo") or None
    owner_source = "param"
    if not owner or not repo:
        git_owner, git_repo = _derive_owner_repo(project_root)
        owner = owner or git_owner or operator_github or "local"
        repo = repo or git_repo or f"{_slug(project_root.name)}-brainstem"
        owner_source = "git-remote" if git_owner else ("operator-github" if operator_github else "fallback-local")

    existing_rappid_path = target_dir / "rappid.json"
    rappid = None
    if existing_rappid_path.exists():
        try:
            existing = json.loads(existing_rappid_path.read_text())
            if existing.get("schema", "").startswith("rapp-rappid/"):
                rappid = existing.get("rappid")
                preserved.append("rappid.json (reused existing rappid)")
        except (json.JSONDecodeError, OSError):
            pass
    if not rappid:
        rappid = _mint_v2_rappid(kind="project", owner=owner, repo=repo)
    twin_hash = _hash_from_rappid(rappid)
    now = datetime.now(timezone.utc).isoformat()

    # Port (idempotent: prefer existing manifest)
    existing_manifest_path = target_dir / "manifest.json"
    port = kwargs.get("port")
    if port is None and existing_manifest_path.exists():
        try:
            em = json.loads(existing_manifest_path.read_text())
            p = em.get("port_hint") or em.get("port")
            if isinstance(p, int):
                port = p
        except (json.JSONDecodeError, OSError):
            pass
    if port is None:
        global_env = _read_env(global_dir / ".env")
        try:
            global_port = int(global_env.get("PORT", 7071))
        except (TypeError, ValueError):
            global_port = 7071
        port = _pick_port(DEFAULT_PORT_FLOOR, also_avoid={global_port})
    else:
        port = int(port)

    rappid_doc = {
        "schema": "rapp/1",
        "rappid": rappid,
        "hash": twin_hash,
        "kind": "project",
        "namespace": f"@{owner}/{_slug(project_root.name)}",
        "host": "github.com",
        "owner": owner,
        "repo": repo,
        "name": _slug(project_root.name),
        "display_name": project_root.name,
        "parent_rappid": parent_rappid,
        "parent_repo": global_rappid_doc.get("anchor_repo") and f"https://github.com/{global_rappid_doc['anchor_repo']}",
        "born_at": now,
        "role": "project-twin",
        "description": f"Project-anchored brainstem twin for {project_root.name}. Hatched from global kernel.",
        "_planted_by": f"@{operator_github}" if operator_github else None,
        "_planted_at_path": str(target_dir),
        "_owner_source": owner_source,
        "_hatched_by": "project_twin_agent.py",
        "_hatcher_version": HATCHER_VERSION,
    }
    existing_rappid_path.write_text(json.dumps(rappid_doc, indent=2) + "\n")
    copied.append("rappid.json")

    manifest_doc = {
        "schema": "rapp-twin-manifest/1.0",
        "rappid": rappid,
        "hash": twin_hash,
        "name": _slug(project_root.name),
        "kind": "project",
        "port_hint": port,
        "anchor_path": str(target_dir),
        "url": f"http://localhost:{port}",
        "updated_at": now,
    }
    existing_manifest_path.write_text(json.dumps(manifest_doc, indent=2) + "\n")
    copied.append("manifest.json")

    # .env (gap-fill)
    target_env = target_dir / ".env"
    global_env = _read_env(global_dir / ".env")
    replace_env = bool(kwargs.get("replace_env", False))
    if target_env.exists() and not replace_env:
        cur = _read_env(target_env)
        cur["PORT"] = str(port)
        cur.setdefault("SOUL_PATH", "./soul.md")
        cur.setdefault("AGENTS_PATH", "./agents")
        _write_env(target_env, cur)
        preserved.append(".env (port updated)")
    else:
        env = {"SOUL_PATH": "./soul.md", "AGENTS_PATH": "./agents", "PORT": str(port)}
        for k in ENV_KEYS_TO_INHERIT:
            if k in global_env:
                env[k] = global_env[k]
        _write_env(target_env, env)
        copied.append(".env")

    # Copilot auth (so the twin chats immediately)
    include_auth = bool(kwargs.get("include_auth", True))
    auth_copied = []
    if include_auth:
        for fname in AUTH_FILES:
            src = global_dir / fname
            dst = target_dir / fname
            if src.exists() and not dst.exists():
                shutil.copy2(src, dst)
                auth_copied.append(fname)
            elif dst.exists():
                preserved.append(fname)

    receipt = {
        "hatcher_version": HATCHER_VERSION,
        "rappid": rappid,
        "name": _slug(project_root.name),
        "kind": "project",
        "source": "project-twin-from-global-kernel",
        "hatched_at": now,
        "workspace": str(target_dir),
        "files": copied,
        "re_hatched": "rappid.json (reused existing rappid)" in preserved,
    }
    (target_dir / HATCH_RECEIPT_NAME).write_text(json.dumps(receipt, indent=2) + "\n")
    copied.append(HATCH_RECEIPT_NAME)

    link_result = _link_canonical_twin(twin_hash, target_dir, force=True)

    # Tracker export sidecar
    tracker_export = None
    tracker_out_path = None
    if bool(kwargs.get("emit_tracker_export", True)):
        custom_agents, agent_names = [], []
        if target_agents.exists():
            for f in sorted(target_agents.glob("*_agent.py")):
                if f.name == "basic_agent.py":
                    continue
                name, desc = _parse_agent_meta(f)
                if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", name):
                    continue
                agent_names.append(name)
                custom_agents.append({
                    "name": name, "description": desc or f"Project agent at {f.name}",
                    "category": "brainstem", "status": "new",
                })
        tracker_export = {
            "projects": [{
                "id": twin_hash,
                "customerName": project_root.name,
                "type": "Project Twin (ProjectTwin)",
                "status": "active",
                "description": (
                    f"Project-anchored brainstem twin. Lives at {target_dir}; "
                    f"symlinked at ~/.rapp/twins/{twin_hash}/. Auth: "
                    f"{'inherited' if (auth_copied or any(f.startswith('.copilot') for f in preserved)) else 'not configured'}."
                ),
                "stakeholders": "", "competingSolution": "", "contractDetails": "",
                "mvpUseCase": f"Resident twin at http://localhost:{port}",
                "mvpTimeline": "",
                "agents": agent_names,
                "createdDate": now, "updatedDate": now,
            }],
            "agents": {"builtin": [], "custom": custom_agents},
            "timeline": [{
                "date": now,
                "title": f"Project twin hatched: {project_root.name}",
                "description": f"Hatched into {target_dir}; symlinked at ~/.rapp/twins/{twin_hash}/ on port {port}.",
            }],
            "exportDate": now,
        }
        tracker_out_path = Path(kwargs.get("tracker_out") or (target_dir / "project_tracker_export.json"))
        tracker_out_path.parent.mkdir(parents=True, exist_ok=True)
        tracker_out_path.write_text(json.dumps(tracker_export, indent=2))

    result = {
        "ok": True,
        "action": "hatch",
        "rappid": rappid,
        "twin_hash": twin_hash,
        "parent_rappid": parent_rappid,
        "project_brainstem": str(target_dir),
        "canonical_twin_link": link_result,
        "port": port,
        "url": f"http://localhost:{port}",
        "copied": copied,
        "auth_copied": auth_copied,
        "preserved": preserved,
        "missing_in_global": missing,
        "owner": owner, "repo": repo, "owner_source": owner_source,
        "start_command": f"cd {target_dir} && ./start.sh",
        "tracker_export_path": str(tracker_out_path) if tracker_out_path else None,
        "tracker_export": tracker_export,
    }

    # Optional autonomous boot after hatch
    if bool(kwargs.get("auto_boot", False)):
        result["boot_result"] = _boot_twin(_slug(project_root.name))

    return result


# ---------------------------------------------------------------------------
# Dispatch / job tracking — fire-and-track orchestration across the neighborhood
# ---------------------------------------------------------------------------

def _new_job_id() -> str:
    return "j-" + uuid.uuid4().hex[:10]


def _job_dir(job_id: str) -> Path:
    return JOBS_DIR / job_id


def _write_twin_status(job_id: str, twin_hash: str, doc: dict) -> None:
    d = _job_dir(job_id)
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{twin_hash}.json").write_text(json.dumps(doc, indent=2))


def _read_twin_status(job_id: str, twin_hash: str) -> dict:
    p = _job_dir(job_id) / f"{twin_hash}.json"
    if not p.exists():
        return {"status": "not_started", "twin_hash": twin_hash}
    try:
        return json.loads(p.read_text())
    except (json.JSONDecodeError, OSError) as e:
        return {"status": "unknown", "twin_hash": twin_hash, "error": str(e)}


def _dispatch(message: str, twins: list, timeout: int = 240) -> str:
    """PURE TRANSPORT fire-and-track. Spawn a thread per twin that sends the
    given natural-language `message` verbatim to that twin's /chat. Each thread
    writes its status to ~/.rapp/jobs/<job_id>/<twin_hash>.json as it goes.
    Returns the job_id immediately so the caller can poll job_status / await_job.

    The message is NOT templated, NOT inspected, NOT shaped. It is exactly what
    the global brainstem (or its user) wants the twin to see — same as if the
    user had pasted it into the twin's own /chat UI on its port. Whatever
    workflow you want the twins to execute, just say it in plain English."""
    job_id = _new_job_id()
    jdir = _job_dir(job_id)
    jdir.mkdir(parents=True, exist_ok=True)
    meta = {
        "schema": "rapp-project-twin-job/1.0",
        "job_id": job_id,
        "message": message,
        "dispatched_at": datetime.now(timezone.utc).isoformat(),
        "twins": [{"hash": t["hash"], "name": t["name"], "port": t["port"]} for t in twins],
    }
    (jdir / "job.json").write_text(json.dumps(meta, indent=2))

    def worker(t):
        twin_hash = t["hash"]
        name = t["name"]
        started = datetime.now(timezone.utc).isoformat()
        _write_twin_status(job_id, twin_hash, {
            "twin": name, "twin_hash": twin_hash, "port": t["port"],
            "status": "running", "started_at": started,
        })
        try:
            r = _chat_with_twin(name, message, auto_boot=True, timeout=timeout)
            _write_twin_status(job_id, twin_hash, {
                "twin": name, "twin_hash": twin_hash, "port": t["port"],
                "status": "complete" if r.get("ok") else "failed",
                "started_at": started,
                "completed_at": datetime.now(timezone.utc).isoformat(),
                "reply": (r.get("reply") or "")[:8000],
                "twin_agent_logs": (r.get("twin_agent_logs") or "")[:4000],
                "error": r.get("error"),
                "auto_booted": r.get("auto_booted", False),
            })
        except Exception as e:
            _write_twin_status(job_id, twin_hash, {
                "twin": name, "twin_hash": twin_hash, "port": t["port"],
                "status": "failed", "started_at": started,
                "completed_at": datetime.now(timezone.utc).isoformat(),
                "error": f"{type(e).__name__}: {e}",
            })

    for t in twins:
        threading.Thread(target=worker, args=(t,), daemon=False,
                         name=f"dispatch-{t['name']}").start()
    return job_id


def _job_status(job_id: str) -> dict:
    if not job_id:
        # Default to latest job
        if not JOBS_DIR.exists():
            return {"error": "no jobs directory yet"}
        jobs = sorted([d for d in JOBS_DIR.iterdir() if d.is_dir()], key=lambda d: d.stat().st_mtime, reverse=True)
        if not jobs:
            return {"error": "no jobs yet"}
        job_id = jobs[0].name
    jdir = _job_dir(job_id)
    if not jdir.exists():
        return {"error": f"no such job: {job_id}"}
    try:
        meta = json.loads((jdir / "job.json").read_text())
    except (json.JSONDecodeError, OSError):
        return {"error": f"job.json unreadable for {job_id}"}
    twins_status = []
    for f in sorted(jdir.glob("*.json")):
        if f.name == "job.json":
            continue
        try:
            twins_status.append(json.loads(f.read_text()))
        except (json.JSONDecodeError, OSError):
            pass
    total = len(meta.get("twins", []))
    counts = {"complete": 0, "failed": 0, "running": 0, "not_started": 0, "unknown": 0}
    seen_hashes = {s.get("twin_hash") for s in twins_status}
    for s in twins_status:
        counts[s.get("status", "unknown")] = counts.get(s.get("status", "unknown"), 0) + 1
    for t in meta.get("twins", []):
        if t["hash"] not in seen_hashes:
            counts["not_started"] += 1
    return {
        "ok": True,
        "job_id": job_id,
        "topic": meta.get("topic"),
        "apply": meta.get("apply"),
        "dispatched_at": meta.get("dispatched_at"),
        "total": total,
        "counts": counts,
        "all_done": (counts["complete"] + counts["failed"]) == total,
        "per_twin": twins_status,
    }


def _await_job(job_id: str, timeout: int = 600, poll_interval: float = 2.0) -> dict:
    deadline = time.time() + timeout
    while time.time() < deadline:
        s = _job_status(job_id)
        if s.get("all_done") or s.get("error"):
            return s
        time.sleep(poll_interval)
    final = _job_status(job_id)
    final["timed_out_waiting"] = True
    return final


def _hatch_all_in_dir(parent_dir: str, **kwargs) -> dict:
    p = Path(parent_dir).expanduser().resolve()
    if not p.exists() or not p.is_dir():
        return {"error": f"parent_dir not a directory: {p}"}
    skip_prefixes = (".", "_")
    skip_names = {"node_modules", "venv", ".venv", "__pycache__", ".git"}
    subs = [s for s in sorted(p.iterdir())
            if s.is_dir() and not s.name.startswith(skip_prefixes) and s.name not in skip_names]
    results = []
    for sub in subs:
        hatch_kwargs = {k: v for k, v in kwargs.items() if k not in ("action", "parent_dir", "project_path")}
        results.append(_do_hatch(project_path=str(sub), **hatch_kwargs))
    return {
        "ok": True,
        "action": "hatch_all",
        "parent_dir": str(p),
        "hatched_count": sum(1 for r in results if r.get("ok")),
        "skipped_count": sum(1 for r in results if not r.get("ok")),
        "results": results,
        "summary": [{"name": r.get("rappid", "?").split(":")[-3] if r.get("rappid") else "?",
                     "hash": r.get("twin_hash"), "port": r.get("port"), "path": r.get("project_brainstem")}
                    for r in results if r.get("ok")],
    }


# ---------------------------------------------------------------------------
# Agent surface
# ---------------------------------------------------------------------------

class ProjectTwinAgent(BasicAgent):
    def __init__(self):
        self.name = "ProjectTwin"
        self.metadata = {
            "name": self.name,
            "description": (
                "Full lifecycle agent for project-anchored brainstem twins. The global "
                "brainstem uses this to autonomously manage a local neighborhood of project "
                "twins through natural language — hatch them from the global kernel, list "
                "them, boot them, chat with them, stop them. One agent, one disk layout "
                "(~/.rapp/twins/<hash>/ symlinked into <project>/.brainstem/src/rapp_brainstem). "
                "Spec-aligned with twin_egg_hatcher (same rappid.json, manifest.json, "
                "HATCH_RECEIPT.json shapes). Use action=hatch to create one project twin from "
                "a project_path, action=hatch_all to hatch a twin for every subdir of a "
                "parent_dir, action=list to enumerate every project twin on this device with "
                "running status, action=boot to start a twin by name, action=chat to send a "
                "message to a twin (auto-boots if needed), action=stop to kill a twin."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["hatch", "hatch_all", "list", "status", "boot", "chat", "stop",
                                 "remove", "dispatch", "job_status", "await_job"],
                        "description": "Verb. Default: hatch if project_path provided, else list. This agent is PURE TRANSPORT — chat/dispatch carry your natural-language message verbatim to the twin(s); the twin's own LLM + its own agents decide what to do.",
                    },
                    "wipe_anchor": {"type": "boolean", "description": "For action=remove: also rm -rf the project-anchored dir at <project>/.brainstem/src/rapp_brainstem. Default false — only the canonical symlink is removed."},
                    "job_id": {"type": "string", "description": "For job_status / await_job: job id returned from dispatch (omit to use the most recent job)."},
                    "poll_interval": {"type": "number", "description": "For await_job: seconds between status polls (default 2)."},
                    "include_twins": {"type": "array", "items": {"type": "string"}, "description": "For dispatch: optional list of twin names to include (default: all project twins on the device)."},
                    "project_path": {"type": "string", "description": "For action=hatch: absolute path to the project root."},
                    "parent_dir": {"type": "string", "description": "For action=hatch_all: absolute path to a dir whose subdirs each become a project twin."},
                    "name": {"type": "string", "description": "For action=boot/chat/stop: the twin's name (e.g. 'bchydro'), display_name, or rappid hash (full or prefix)."},
                    "message": {"type": "string", "description": "For action=chat / dispatch: the verbatim natural-language message to send to the twin(s). Same shape as if the user pasted it into the twin's own /chat UI directly."},
                    "auto_boot": {"type": "boolean", "description": "For action=chat: if the twin isn't running, boot it first (default true). For action=hatch: also boot immediately after hatching (default false)."},
                    "port": {"type": "integer", "description": "For action=hatch: override the auto-picked port."},
                    "owner": {"type": "string", "description": "For action=hatch: override the rappid's owner segment."},
                    "repo": {"type": "string", "description": "For action=hatch: override the rappid's repo segment."},
                    "replace_env": {"type": "boolean", "description": "For action=hatch: regenerate .env even if it exists."},
                    "force_soul": {"type": "boolean", "description": "For action=hatch: overwrite project soul.md with global."},
                    "include_auth": {"type": "boolean", "description": "For action=hatch: copy .copilot_token + .copilot_session from global (default true)."},
                    "emit_tracker_export": {"type": "boolean", "description": "For action=hatch: write projectTrackerData JSON sidecar (default true)."},
                    "tracker_out": {"type": "string", "description": "For action=hatch: override path for the tracker export JSON."},
                    "timeout": {"type": "integer", "description": "For action=chat: HTTP timeout in seconds (default 60)."},
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        action = kwargs.get("action")
        if not action:
            if kwargs.get("project_path"):
                action = "hatch"
            elif kwargs.get("parent_dir"):
                action = "hatch_all"
            else:
                action = "list"

        if action in ("list", "status"):
            return json.dumps({"action": "list", "project_twins": _list_project_twins()}, indent=2)

        if action == "hatch":
            return json.dumps(_do_hatch(**kwargs), indent=2)

        if action == "hatch_all":
            parent = kwargs.get("parent_dir") or kwargs.get("project_path")
            if not parent:
                return json.dumps({"error": "parent_dir is required for hatch_all"})
            forward = {k: v for k, v in kwargs.items() if k not in ("action", "parent_dir", "project_path")}
            return json.dumps(_hatch_all_in_dir(parent, **forward), indent=2)

        if action == "boot":
            name = kwargs.get("name") or kwargs.get("hash") or kwargs.get("twin_hash")
            return json.dumps(_boot_twin(name), indent=2)

        if action == "stop":
            name = kwargs.get("name") or kwargs.get("hash") or kwargs.get("twin_hash")
            return json.dumps(_stop_twin(name), indent=2)

        if action == "remove":
            name = kwargs.get("name") or kwargs.get("hash") or kwargs.get("twin_hash")
            return json.dumps(_remove_twin(name, wipe_anchor=bool(kwargs.get("wipe_anchor", False))), indent=2)

        if action == "dispatch":
            message = kwargs.get("message") or kwargs.get("user_input") or ""
            if not message:
                return json.dumps({"error": "message is required for dispatch (the verbatim natural-language string each twin will receive)"})
            all_twins = _list_project_twins()
            include = kwargs.get("include_twins")
            if include:
                wanted = set(_slug(n) for n in include)
                all_twins = [t for t in all_twins
                             if _slug(t["name"]) in wanted
                             or (t.get("display_name") and _slug(t["display_name"]) in wanted)]
            twins = [t for t in all_twins if t.get("port")]
            if not twins:
                return json.dumps({"error": "no project twins to dispatch to"})
            job_id = _dispatch(
                message=message, twins=twins,
                timeout=int(kwargs.get("timeout") or 240),
            )
            return json.dumps({
                "ok": True, "action": "dispatch", "job_id": job_id,
                "twins_dispatched": len(twins),
                "message_preview": (message[:200] + ("…" if len(message) > 200 else "")),
                "next_steps": [
                    f"action=job_status job_id={job_id}  — poll progress",
                    f"action=await_job job_id={job_id}    — block until all done",
                ],
            }, indent=2)

        if action == "job_status":
            return json.dumps(_job_status(kwargs.get("job_id", "")), indent=2)

        if action == "await_job":
            return json.dumps(_await_job(
                kwargs.get("job_id", ""),
                timeout=int(kwargs.get("timeout") or 600),
                poll_interval=float(kwargs.get("poll_interval") or 2.0),
            ), indent=2)

        if action == "chat":
            name = kwargs.get("name") or kwargs.get("hash") or kwargs.get("twin_hash")
            msg = kwargs.get("message") or kwargs.get("user_input") or ""
            auto_boot = bool(kwargs.get("auto_boot", True))
            timeout = int(kwargs.get("timeout") or 60)
            return json.dumps(_chat_with_twin(name, msg, auto_boot=auto_boot, timeout=timeout), indent=2)

        return json.dumps({"error": f"unknown action: {action}",
                           "valid": ["hatch", "hatch_all", "list", "status", "boot", "chat", "stop"]})
