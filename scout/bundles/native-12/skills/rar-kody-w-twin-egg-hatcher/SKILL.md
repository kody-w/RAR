---
name: "rar-kody-w-twin-egg-hatcher"
description: "Hatch a twin from any source \u2014 a local .egg file, a public/private GitHub twin repo (e.g. 'kody-w/heimdall'), or the current directory if it contains a rappid.json.  Materializes ~/.rapp/twins/<hash>/ so the global brainstem's Twin agent can boot and chat with it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/twin_egg_hatcher", "rar_sha256": "300dd7302be574e2460c2ccd873c930fb9a6f07057078afbe3da114c84b23ef2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.1.0", "author": "Kody Wildfeuer", "tags": ["twin", "egg", "hatcher", "organism", "federation", "single-file", "rapp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/twin_egg_hatcher`. The original RAPP
agent is preserved byte-for-byte in `twin_egg_hatcher_agent.py` and in the RCI capsule.

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

twin_egg_hatcher_agent.py — generic single-file twin egg hatcher.

One hatcher.  Any twin.

The hatcher carries no twin-specific identity.  It loads identity from
one of three sources, in priority order:

1. **`--egg PATH`** — a fully exported `.egg` file (zip).  Use this for
   private twins or air-gapped installs.
2. **`--source REPO`** — a public twin repo (e.g. `kody-w/heimdall`).
   The hatcher fetches `rappid.json`, `soul.md`, and any `agents/*.py`
   via raw GitHub.  For private repos, set `GH_TOKEN`.
3. **cwd auto-detect** (default) — if the current directory contains
   `rappid.json`, treat it as the twin's source.  Works after a plain
   `gh repo clone <twin-repo>`.

The workspace lands at `~/.rapp/twins/<hash>/`.  The global brainstem's
built-in `Twin` agent (https://github.com/kody-w/rapp-installer) reaches
every workspace under that folder — boot, chat, list — so any twin
hatched by this tool becomes addressable through the parent immediately.

Two ways to invoke
------------------

1) **Drop-in portable agent.**  Copy this file into the global brainstem's
   agents folder.  It exposes a `HatchTwinEgg` tool with actions
   `hatch / rollback / status / list_twins`.

       cp twin_egg_hatcher_agent.py ~/.brainstem/src/rapp_brainstem/agents/

2) **Standalone CLI.**  Just run it.

       # auto-detect from a cloned twin repo
       gh repo clone kody-w/heimdall && cd heimdall
       python twin_egg_hatcher_agent.py hatch

       # explicit source (public twin)
       python twin_egg_hatcher_agent.py hatch --source kody-w/heimdall

       # private twin via local .egg
       python twin_egg_hatcher_agent.py hatch --egg ~/Downloads/botsinblazers.egg

       python twin_egg_hatcher_agent.py status
       python twin_egg_hatcher_agent.py list-twins
       python twin_egg_hatcher_agent.py rollback --rappid <rappid>

Modes
-----

`mode=twin` (default) keeps the global brainstem pristine — the egg is
unpacked into `~/.rapp/twins/<hash>/` and federates back through the
parent brainstem's built-in `Twin` agent.

`mode=global` is opt-in: unpacks the egg's brainstem-extension files
(organs, senses) onto `$BRAINSTEM_HOME/src/rapp_brainstem/`.  Backed up
+ reversible.

Environment overrides
---------------------

    BRAINSTEM_HOME       defaults to ~/.brainstem
    RAPP_HOME            defaults to ~/.rapp                  (twin estate root)
    TWIN_EGG_HOME        defaults to ~/.twin-egg              (backups, marker)
    GH_TOKEN             optional — needed for private --source repos

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "What to do.  Defaults to 'status'.",
      "enum": [
        "hatch",
        "rollback",
        "status",
        "list_twins"
      ],
      "type": "string"
    },
    "description": {
      "description": "Optional human description recorded in the twin's rappid.json.",
      "type": "string"
    },
    "egg": {
      "description": "Path to a .egg file (zip).  Used for private/air-gapped twins.",
      "type": "string"
    },
    "mode": {
      "description": "Where to hatch.  'twin' (default) = local workspace; 'global' = extend kernel.",
      "enum": [
        "twin",
        "global"
      ],
      "type": "string"
    },
    "name": {
      "description": "Optional alias to record alongside the source's rappid.json (does not change rappid).",
      "type": "string"
    },
    "rappid": {
      "description": "For action='rollback', the rappid of the twin to un-hatch (default: cwd auto-detect).",
      "type": "string"
    },
    "source": {
      "description": "owner/repo or github URL (e.g. 'kody-w/heimdall').  Set GH_TOKEN for private repos.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `twin_egg_hatcher_agent.py` and embedded as the fenced Python below (sha256 300dd7302be574e2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `twin_egg_hatcher_agent.py` first:

```bash
python3 twin_egg_hatcher_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 twin_egg_hatcher_agent.py   # or on stdin
python3 twin_egg_hatcher_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/twin_egg_hatcher_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/twin_egg_hatcher_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/twin_egg_hatcher/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""twin_egg_hatcher_agent.py — generic single-file twin egg hatcher.

One hatcher.  Any twin.

The hatcher carries no twin-specific identity.  It loads identity from
one of three sources, in priority order:

1. **`--egg PATH`** — a fully exported `.egg` file (zip).  Use this for
   private twins or air-gapped installs.
2. **`--source REPO`** — a public twin repo (e.g. `kody-w/heimdall`).
   The hatcher fetches `rappid.json`, `soul.md`, and any `agents/*.py`
   via raw GitHub.  For private repos, set `GH_TOKEN`.
3. **cwd auto-detect** (default) — if the current directory contains
   `rappid.json`, treat it as the twin's source.  Works after a plain
   `gh repo clone <twin-repo>`.

The workspace lands at `~/.rapp/twins/<hash>/`.  The global brainstem's
built-in `Twin` agent (https://github.com/kody-w/rapp-installer) reaches
every workspace under that folder — boot, chat, list — so any twin
hatched by this tool becomes addressable through the parent immediately.

Two ways to invoke
------------------

1) **Drop-in portable agent.**  Copy this file into the global brainstem's
   agents folder.  It exposes a `HatchTwinEgg` tool with actions
   `hatch / rollback / status / list_twins`.

       cp twin_egg_hatcher_agent.py ~/.brainstem/src/rapp_brainstem/agents/

2) **Standalone CLI.**  Just run it.

       # auto-detect from a cloned twin repo
       gh repo clone kody-w/heimdall && cd heimdall
       python twin_egg_hatcher_agent.py hatch

       # explicit source (public twin)
       python twin_egg_hatcher_agent.py hatch --source kody-w/heimdall

       # private twin via local .egg
       python twin_egg_hatcher_agent.py hatch --egg ~/Downloads/botsinblazers.egg

       python twin_egg_hatcher_agent.py status
       python twin_egg_hatcher_agent.py list-twins
       python twin_egg_hatcher_agent.py rollback --rappid <rappid>

Modes
-----

`mode=twin` (default) keeps the global brainstem pristine — the egg is
unpacked into `~/.rapp/twins/<hash>/` and federates back through the
parent brainstem's built-in `Twin` agent.

`mode=global` is opt-in: unpacks the egg's brainstem-extension files
(organs, senses) onto `$BRAINSTEM_HOME/src/rapp_brainstem/`.  Backed up
+ reversible.

Environment overrides
---------------------

    BRAINSTEM_HOME       defaults to ~/.brainstem
    RAPP_HOME            defaults to ~/.rapp                  (twin estate root)
    TWIN_EGG_HOME        defaults to ~/.twin-egg              (backups, marker)
    GH_TOKEN             optional — needed for private --source repos
"""

from __future__ import annotations


# ═══════════════════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — extracted by kody-w/RAR's build_registry.py via AST.
# ═══════════════════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/twin_egg_hatcher",
    "version": "1.1.0",
    "distinct_from": {"@rapp/egg_hatcher": "egg_hatcher routes any .egg to a handler by its manifest type; this hatcher materializes a twin workspace from a checkout, repo or egg at every scale"},
    "display_name": "HatchTwinEgg",
    "description": (
        "Generic single-file hatcher for any RAPP digital-organism twin. "
        "Loads identity from cwd auto-detect, --source REPO (raw GitHub), "
        "or --egg PATH (zip), then materializes ~/.rapp/twins/<hash>/. The "
        "global brainstem's built-in Twin agent boots/chats with it immediately."
    ),
    "author": "Kody Wildfeuer",
    "tags": ["twin", "egg", "hatcher", "organism", "federation", "single-file", "rapp"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


import argparse
import io
import json
import os
import re
import shutil
import socket
import sys
import urllib.error
import urllib.request
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

HATCHER_VERSION = "1.1.0"  # 1.1.0: multi-scale eggs (neighborhood / swarm / industry / estate)
HATCH_RECEIPT_NAME = "HATCH_RECEIPT.json"
EGG_SCHEMA = "rapp-egg/2.0"

# Scales the hatcher knows about, from smallest to largest unit of organism.
SCALES = ("agent", "twin", "brainstem", "neighborhood", "swarm", "factory", "industry", "estate")

DEFAULT_BRAINSTEM_HOME = Path(os.environ.get("BRAINSTEM_HOME", str(Path.home() / ".brainstem")))
BRAINSTEM_SRC_SUBPATH = Path("src") / "rapp_brainstem"
TWIN_EGG_HOME = Path(os.environ.get("TWIN_EGG_HOME", str(Path.home() / ".twin-egg")))
BACKUPS_DIR = TWIN_EGG_HOME / "backups"          # mode=global only
RAPP_HOME = Path(os.environ.get("RAPP_HOME", str(Path.home() / ".rapp")))
TWINS_DIR = RAPP_HOME / "twins"
TRASH_DIR = TWINS_DIR / ".trash"
# Per-scale workspace roots (created lazily).
NEIGHBORHOODS_DIR = RAPP_HOME / "neighborhoods"
SWARMS_DIR        = RAPP_HOME / "swarms"
FACTORIES_DIR     = RAPP_HOME / "factories"
INDUSTRIES_DIR    = RAPP_HOME / "industries"
ESTATES_DIR       = RAPP_HOME / "estates"
LEVIATHANS_DIR    = RAPP_HOME / "leviathans"
SCALE_ROOTS = {
    "twin":         TWINS_DIR,
    "brainstem":    TWINS_DIR,  # same root — a brainstem-shaped egg is a single twin
    "neighborhood": NEIGHBORHOODS_DIR,
    "swarm":        SWARMS_DIR,
    "factory":      FACTORIES_DIR,
    "industry":     INDUSTRIES_DIR,
    "estate":       ESTATES_DIR,
}

GITHUB_RAW = "https://raw.githubusercontent.com"
GITHUB_API = "https://api.github.com"

# Files we copy from a twin source by default.  agents/ contents are
# enumerated separately.
KNOWN_TOP_FILES = (
    "rappid.json", "soul.md", "manifest.json",
    "members.json", "neighbors.json",
)

# Inside an .egg zip, twin files live under `repo/` (per the
# brainstem-egg/2.1 convention from twin_agent.py).
EGG_REPO_PREFIX = "repo/"

SNAPSHOT_IGNORES = shutil.ignore_patterns(
    "__pycache__", "*.pyc", ".venv", "venv", ".pytest_cache",
    ".brainstem_data", ".brainstem_book.json", "*.log",
)


# ---------------------------------------------------------------------------
# BasicAgent shim — works inside the brainstem and standalone.
# ---------------------------------------------------------------------------

try:
    from agents.basic_agent import BasicAgent  # type: ignore
except Exception:  # pragma: no cover - standalone fallback
    class BasicAgent:  # type: ignore[no-redef]
        def __init__(self, name: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None):
            self.name = name or getattr(self, "name", "BasicAgent")
            self.metadata = metadata or getattr(self, "metadata", {})

        def perform(self, **kwargs: Any) -> str:
            return "Not implemented."


# ---------------------------------------------------------------------------
# Path / id helpers
# ---------------------------------------------------------------------------

def _ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


def _name_from_namespace(ns: str) -> Optional[str]:
    """`@owner/slug` → `slug` (the readable end), if it looks like a v2 namespace."""
    if not ns:
        return None
    s = ns.lstrip("@")
    if "/" in s:
        return s.split("/", 1)[1] or None
    return s or None


def _name_from_rappid(rappid: str) -> Optional[str]:
    """Extract the slug from a rappid. Accepts the consolidated form
    `rappid:@owner/slug:HEX64` and the legacy `rappid:v2:KIND:@owner/slug:HASH@...`."""
    # Consolidated: no v<n>:kind: segment, slug runs up to the final ':<hex>'.
    m = re.match(r"^rappid:@[^/]+/([^:]+):[a-f0-9]+$", rappid)
    if m:
        return m.group(1)
    m = re.match(r"^rappid:v\d+:[^:]+:@[^/]+/([^:]+):", rappid)
    return m.group(1) if m else None


def _resolve_name(rj: Dict[str, Any]) -> str:
    """Best-effort display name from any rappid.json shape."""
    return (
        rj.get("name")
        or rj.get("display_name")
        or rj.get("repo")
        or _name_from_namespace(rj.get("namespace", ""))
        or _name_from_rappid(rj.get("rappid", ""))
        or "twin"
    )


def _hash_from_rappid(rappid: str) -> str:
    """Workspace dirname for a rappid.  Handles:
      - consolidated rappids (`rappid:@owner/slug:HEX64`, 256-bit)
      - v2 rappids (`rappid:v2:...:HEX32@...`)
      - bare-UUID rappids (legacy v1.x front doors like Heimdall)."""
    if rappid.startswith("rappid:"):
        m = re.search(r":([a-f0-9]{64})$|:([a-f0-9]{32})@", rappid)
        if m:
            return m.group(1) or m.group(2)
    return rappid


def _workspace_for(rappid: str) -> Path:
    return TWINS_DIR / _hash_from_rappid(rappid)


def brainstem_src() -> Path:
    return DEFAULT_BRAINSTEM_HOME / BRAINSTEM_SRC_SUBPATH


# ---------------------------------------------------------------------------
# Twin runtime lookup
# ---------------------------------------------------------------------------

PIDS_DIR = RAPP_HOME / "pids"
PORTS_DIR = RAPP_HOME / "ports"


def _safe(rappid: str) -> str:
    return rappid.replace(":", "_").replace("@", "").replace("/", "_")


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
    pid = _read_int(PIDS_DIR / f"{_safe(rappid)}.pid") or 0
    port = _read_int(PORTS_DIR / f"{_safe(rappid)}.port") or 0
    alive = bool(pid) and _pid_alive(pid)
    return {
        "pid": pid if alive else None,
        "port": port if alive else None,
        "url": f"http://127.0.0.1:{port}" if alive and port else None,
        "running": alive,
    }


# ---------------------------------------------------------------------------
# Source loaders — egg | github | cwd
# ---------------------------------------------------------------------------

class TwinIdentity:
    """The minimum a hatcher needs from any twin source."""

    def __init__(
        self,
        rappid_json: Dict[str, Any],
        soul_md: str,
        agents: Dict[str, str],
        extras: Optional[Dict[str, str]] = None,
        organs: Optional[Dict[str, str]] = None,
        senses: Optional[Dict[str, str]] = None,
        source: str = "",
    ):
        if not rappid_json or not rappid_json.get("rappid"):
            raise ValueError("source did not provide a rappid.json with a 'rappid' field")
        self.rappid_json = rappid_json
        self.rappid: str = rappid_json["rappid"]
        self.name: str = _resolve_name(rappid_json)
        self.kind: str = rappid_json.get("kind") or "personal"
        self.soul_md = soul_md or _placeholder_soul(self.name)
        self.agents = agents or {}
        self.extras = extras or {}
        self.organs = organs or {}
        self.senses = senses or {}
        self.source = source

    def as_dict(self) -> Dict[str, Any]:
        return {
            "rappid": self.rappid,
            "name": self.name,
            "kind": self.kind,
            "source": self.source,
            "agents_count": len(self.agents),
            "extras_count": len(self.extras),
            "organs_count": len(self.organs),
            "senses_count": len(self.senses),
        }


def _placeholder_soul(name: str) -> str:
    return f"# soul.md — {name}\n\n(Source provided no soul.md.  Replace this with the twin's persona.)\n"


def load_from_cwd(cwd: Optional[Path] = None) -> TwinIdentity:
    cwd = cwd or Path.cwd()
    rj_path = cwd / "rappid.json"
    if not rj_path.exists():
        raise FileNotFoundError(f"No rappid.json in {cwd}; pass --source REPO or --egg PATH.")
    rj = json.loads(rj_path.read_text(encoding="utf-8"))
    soul = (cwd / "soul.md").read_text(encoding="utf-8") if (cwd / "soul.md").exists() else ""
    agents = _read_dir_files(cwd / "agents", suffix=".py")
    organs = _read_dir_files(cwd / "organs", suffix=".py")
    senses = _read_dir_files(cwd / "senses", suffix=".py")
    extras = {}
    for name in KNOWN_TOP_FILES:
        if name in ("rappid.json", "soul.md"):
            continue
        p = cwd / name
        if p.exists():
            extras[name] = p.read_text(encoding="utf-8")
    return TwinIdentity(rj, soul, agents, extras, organs, senses, source=f"cwd:{cwd}")


def _read_dir_files(d: Path, suffix: str) -> Dict[str, str]:
    if not d.is_dir():
        return {}
    out: Dict[str, str] = {}
    for p in sorted(d.iterdir()):
        if p.is_file() and p.suffix == suffix and not p.name.startswith("_"):
            out[p.name] = p.read_text(encoding="utf-8")
    return out


def load_from_egg(egg_path: Path) -> TwinIdentity:
    """Unpack a .egg (zip).  Inside the zip, twin files live under `repo/`
    per brainstem-egg/2.1.  Older eggs that put files at the root also
    work via a fallback."""
    with zipfile.ZipFile(egg_path) as z:
        names = z.namelist()

        def _read(internal: str) -> Optional[str]:
            for prefix in (EGG_REPO_PREFIX, ""):
                full = prefix + internal
                if full in names:
                    return z.read(full).decode("utf-8")
            return None

        def _read_dir(dirname: str, suffix: str) -> Dict[str, str]:
            out: Dict[str, str] = {}
            for prefix in (EGG_REPO_PREFIX, ""):
                base = f"{prefix}{dirname}/"
                for full in names:
                    if not full.startswith(base):
                        continue
                    rel = full[len(base):]
                    if not rel or rel.endswith("/") or "/" in rel:
                        continue
                    if not rel.endswith(suffix) or rel.startswith("_"):
                        continue
                    out[rel] = z.read(full).decode("utf-8")
                if out:
                    break
            return out

        rj_text = _read("rappid.json")
        if not rj_text:
            raise ValueError(f"Egg {egg_path} has no rappid.json")
        rj = json.loads(rj_text)
        soul = _read("soul.md") or ""
        agents = _read_dir("agents", ".py")
        organs = _read_dir("organs", ".py")
        senses = _read_dir("senses", ".py")
        extras = {}
        for name in KNOWN_TOP_FILES:
            if name in ("rappid.json", "soul.md"):
                continue
            content = _read(name)
            if content is not None:
                extras[name] = content
    return TwinIdentity(rj, soul, agents, extras, organs, senses, source=f"egg:{egg_path}")


def _parse_source(source: str) -> Tuple[str, str, str]:
    """Accept `owner/repo`, `owner/repo@branch`, `github.com/owner/repo`,
    or `https://github.com/owner/repo[/tree/branch]`.  Returns (owner, repo, branch)."""
    s = source.strip()
    branch = "main"
    s = re.sub(r"^https?://", "", s)
    s = s.removeprefix("github.com/")
    s = s.removeprefix("raw.githubusercontent.com/")
    if "@" in s and "/" in s.split("@")[0]:
        s, branch = s.rsplit("@", 1)
    m = re.match(r"^([^/]+)/([^/]+)(/tree/([^/]+))?(/.*)?$", s)
    if not m:
        raise ValueError(f"Could not parse source: {source!r}")
    owner = m.group(1)
    repo = m.group(2)
    if m.group(4):
        branch = m.group(4)
    return owner, repo, branch


def _gh_fetch(url: str) -> Optional[bytes]:
    headers = {"User-Agent": "twin-egg-hatcher/1.0"}
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"
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
    raw_base = f"{GITHUB_RAW}/{owner}/{repo}/{branch}"

    def _raw(rel: str) -> Optional[str]:
        data = _gh_fetch(f"{raw_base}/{rel}")
        return data.decode("utf-8") if data else None

    def _list_dir(rel: str, suffix: str) -> Dict[str, str]:
        api = f"{GITHUB_API}/repos/{owner}/{repo}/contents/{rel}?ref={branch}"
        data = _gh_fetch(api)
        if not data:
            return {}
        try:
            entries = json.loads(data.decode("utf-8"))
        except json.JSONDecodeError:
            return {}
        if not isinstance(entries, list):
            return {}
        out: Dict[str, str] = {}
        for e in entries:
            if e.get("type") != "file":
                continue
            name = e.get("name", "")
            if not name.endswith(suffix) or name.startswith("_"):
                continue
            content = _raw(f"{rel}/{name}")
            if content is not None:
                out[name] = content
        return out

    rj_text = _raw("rappid.json")
    if not rj_text:
        raise ValueError(f"github.com/{owner}/{repo}@{branch} has no rappid.json (or it's private — try GH_TOKEN).")
    rj = json.loads(rj_text)
    soul = _raw("soul.md") or ""
    agents = _list_dir("agents", ".py")
    organs = _list_dir("organs", ".py")
    senses = _list_dir("senses", ".py")
    extras = {}
    for name in KNOWN_TOP_FILES:
        if name in ("rappid.json", "soul.md"):
            continue
        content = _raw(name)
        if content is not None:
            extras[name] = content
    return TwinIdentity(rj, soul, agents, extras, organs, senses, source=f"github:{owner}/{repo}@{branch}")


def load_identity(*, egg: Optional[str], source: Optional[str], cwd: Optional[Path] = None) -> TwinIdentity:
    if egg:
        return load_from_egg(Path(egg).expanduser().resolve())
    if source:
        return load_from_github(source)
    return load_from_cwd(cwd)


# ---------------------------------------------------------------------------
# Multi-scale egg dispatch — hatch any unit of the organism (rapp-egg/2.0).
# ---------------------------------------------------------------------------
#
# A rapp-egg/2.0 manifest declares its `scale` (agent / twin / brainstem /
# neighborhood / swarm / factory / industry / estate).  The dispatcher reads
# the manifest, then routes to the right unpacker.  Older single-twin eggs
# (no manifest, files under `repo/`) keep working via the legacy path.
# ---------------------------------------------------------------------------


def _read_egg_manifest(egg_path: Path) -> Optional[Dict[str, Any]]:
    """Return the manifest.json dict if the egg has one, else None (legacy)."""
    with zipfile.ZipFile(egg_path) as z:
        names = set(z.namelist())
        for cand in ("manifest.json", "egg.json", "repo/manifest.json"):
            if cand in names:
                try:
                    return json.loads(z.read(cand).decode("utf-8"))
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
        return {"ok": False, "error": f"egg not found: {egg_path}"}

    m = _read_egg_manifest(egg_path)
    scale = (m or {}).get("scale") or "twin"
    if scale not in SCALES:
        return {"ok": False, "error": f"unknown scale '{scale}'.  Known: {SCALES}"}

    if scale in ("twin", "brainstem"):
        return hatch_twin(egg=str(egg_path))
    if scale == "agent":
        return _hatch_agent_egg(egg_path, m or {})
    if scale == "neighborhood":
        return _hatch_neighborhood_egg(egg_path, m or {})
    if scale in ("swarm", "factory", "industry", "estate"):
        return _hatch_container_egg(egg_path, m or {}, scale)
    return {"ok": False, "error": f"scale '{scale}' recognized but not yet implemented"}


def _hatch_agent_egg(egg_path: Path, manifest: Dict[str, Any]) -> Dict[str, Any]:
    """Single-agent egg — drops a `_agent.py` into the brainstem's agents/ folder
    so the next /chat picks it up via load_agents().  The egg should contain
    one or more `*_agent.py` files at the top level (or under `agents/`)."""
    bs_agents = brainstem_src() / "agents"
    if not bs_agents.is_dir():
        return {"ok": False, "scale": "agent", "error": f"brainstem agents dir not found: {bs_agents}"}
    written: List[str] = []
    with zipfile.ZipFile(egg_path) as z:
        for name in z.namelist():
            base = os.path.basename(name)
            if base.endswith("_agent.py"):
                bs_agents.joinpath(base).write_bytes(z.read(name))
                written.append(base)
    return {
        "ok": True,
        "scale": "agent",
        "manifest": manifest,
        "installed_into": str(bs_agents),
        "files_written": written,
        "note": "Next /chat will load the new agent(s) — no restart needed.",
    }


def _hatch_neighborhood_egg(egg_path: Path, manifest: Dict[str, Any]) -> Dict[str, Any]:
    """Neighborhood egg — unpacks `twins/<hash>/...` into ~/.rapp/twins/<hash>/
    for every member.  Also drops a neighborhood roster under
    ~/.rapp/neighborhoods/<neighborhood_hash>/.  The global brainstem's Twin
    agent picks up every workspace immediately."""
    _ensure_dirs()
    NEIGHBORHOODS_DIR.mkdir(parents=True, exist_ok=True)

    members = manifest.get("members") or []
    if not isinstance(members, list):
        return {"ok": False, "scale": "neighborhood", "error": "manifest.members must be a list"}

    n_hash = manifest.get("hash") or _hash_from_rappid(manifest.get("rappid", "")) or "neighborhood"
    n_dir = NEIGHBORHOODS_DIR / n_hash
    n_dir.mkdir(parents=True, exist_ok=True)

    extracted_per_twin: Dict[str, int] = {}
    members_summary: List[Dict[str, Any]] = []

    with zipfile.ZipFile(egg_path) as z:
        all_names = z.namelist()
        for member in members:
            mhash = member.get("hash")
            if not mhash:
                continue
            ws = TWINS_DIR / mhash
            ws.mkdir(parents=True, exist_ok=True)
            (ws / "agents").mkdir(exist_ok=True)
            (ws / ".brainstem_data").mkdir(exist_ok=True)
            prefix = f"twins/{mhash}/"
            count = 0
            for n in all_names:
                if not n.startswith(prefix):
                    continue
                rel = n[len(prefix):]
                if not rel or rel.endswith("/"):
                    continue
                if rel.endswith("/.keep"):
                    # Re-create empty dir, skip placeholder file
                    (ws / rel[:-len("/.keep")]).mkdir(parents=True, exist_ok=True)
                    continue
                target = ws / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(z.read(n))
                count += 1
            extracted_per_twin[mhash] = count
            members_summary.append({
                "name": member.get("name"),
                "hash": mhash,
                "rappid": member.get("rappid"),
                "workspace": str(ws),
                "files_extracted": count,
            })

    # Write the neighborhood roster + hatch receipt.
    (n_dir / "members.json").write_text(
        json.dumps({"members": members_summary}, indent=2),
        encoding="utf-8",
    )
    (n_dir / "rappid.json").write_text(
        json.dumps({
            "schema":  "rapp/1",
            "rappid":  manifest.get("rappid"),
            "hash":    n_hash,
            "kind":    "neighborhood",
            "name":    manifest.get("name"),
            "parent_rappid": manifest.get("parent_rappid"),
            "born_at": manifest.get("born_at"),
            "creator": manifest.get("creator"),
            "description": manifest.get("description"),
        }, indent=2),
        encoding="utf-8",
    )
    (n_dir / HATCH_RECEIPT_NAME).write_text(
        json.dumps({
            "hatcher_version": HATCHER_VERSION,
            "scale": "neighborhood",
            "source": f"egg:{egg_path}",
            "rappid": manifest.get("rappid"),
            "hatched_at": datetime.now(timezone.utc).isoformat(),
            "members": members_summary,
        }, indent=2),
        encoding="utf-8",
    )

    boot = manifest.get("boot_hint", {}).get("ports", {})
    boot_cmds = []
    for m in members_summary:
        port = boot.get(m["name"], "")
        if port:
            boot_cmds.append(
                f"SOUL_PATH={m['workspace']}/soul.md AGENTS_PATH={m['workspace']}/agents "
                f"PORT={port} bash ~/.brainstem/src/rapp_brainstem/start.sh &"
            )

    return {
        "ok": True,
        "scale": "neighborhood",
        "rappid": manifest.get("rappid"),
        "neighborhood_workspace": str(n_dir),
        "members_extracted": members_summary,
        "files_per_twin": extracted_per_twin,
        "boot_commands": boot_cmds,
        "next": [
            "Each member is now under ~/.rapp/twins/<hash>/ — the global brainstem's Twin agent sees them all.",
            "Boot each twin on the suggested port (see boot_commands) to bring the federation alive.",
            "From the global brainstem: Twin(action='list') will enumerate every member.",
        ],
    }


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
    chash = manifest.get("hash") or _hash_from_rappid(manifest.get("rappid", "")) or scale
    wdir = root / chash
    wdir.mkdir(parents=True, exist_ok=True)

    written: List[str] = []
    with zipfile.ZipFile(egg_path) as z:
        for name in z.namelist():
            if name.endswith("/"):
                continue
            target = wdir / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(z.read(name))
            written.append(name)

    (wdir / HATCH_RECEIPT_NAME).write_text(
        json.dumps({
            "hatcher_version": HATCHER_VERSION,
            "scale": scale,
            "source": f"egg:{egg_path}",
            "rappid": manifest.get("rappid"),
            "hatched_at": datetime.now(timezone.utc).isoformat(),
            "files": len(written),
        }, indent=2),
        encoding="utf-8",
    )

    return {
        "ok": True,
        "scale": scale,
        "rappid": manifest.get("rappid"),
        "workspace": str(wdir),
        "files_written": len(written),
        "note": (
            f"Container egg of scale '{scale}' unpacked to {wdir}.  "
            f"Nested children (if any) need to be hatched recursively — point "
            f"the hatcher at each child's egg or workspace."
        ),
    }


# ---------------------------------------------------------------------------
# Hatch / rollback / list / status
# ---------------------------------------------------------------------------

def _ensure_dirs() -> None:
    TWINS_DIR.mkdir(parents=True, exist_ok=True)
    TRASH_DIR.mkdir(parents=True, exist_ok=True)
    PIDS_DIR.mkdir(parents=True, exist_ok=True)
    PORTS_DIR.mkdir(parents=True, exist_ok=True)


def hatch_twin(
    *,
    egg: Optional[str] = None,
    source: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    _ensure_dirs()
    identity = load_identity(egg=egg, source=source)
    rappid = identity.rappid
    ws = _workspace_for(rappid)

    already = ws.exists() and (ws / "rappid.json").exists()
    ws.mkdir(parents=True, exist_ok=True)
    (ws / "agents").mkdir(exist_ok=True)
    (ws / ".brainstem_data").mkdir(exist_ok=True)

    written: List[str] = []

    # soul.md
    (ws / "soul.md").write_text(identity.soul_md, encoding="utf-8")
    written.append("soul.md")

    # rappid.json — preserve source exactly, plus a hatcher annotation.
    rj = dict(identity.rappid_json)
    if name:
        rj["display_alias"] = name
    if description:
        rj["description"] = description
    rj.setdefault("_hatched_by", "twin_egg_hatcher_agent.py")
    rj.setdefault("_hatcher_version", HATCHER_VERSION)
    (ws / "rappid.json").write_text(json.dumps(rj, indent=2) + "\n", encoding="utf-8")
    written.append("rappid.json")

    # agents + extras
    for fname, content in identity.agents.items():
        (ws / "agents" / fname).write_text(content, encoding="utf-8")
        written.append(f"agents/{fname}")
    for fname, content in identity.extras.items():
        (ws / fname).write_text(content, encoding="utf-8")
        written.append(fname)

    # Hatch receipt
    receipt = {
        "hatcher_version": HATCHER_VERSION,
        "rappid": rappid,
        "name": identity.name,
        "kind": identity.kind,
        "source": identity.source,
        "hatched_at": datetime.now(timezone.utc).isoformat(),
        "workspace": str(ws),
        "files": written,
        "re_hatched": already,
    }
    (ws / HATCH_RECEIPT_NAME).write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")

    return {
        "ok": True,
        "mode": "twin",
        "rappid": rappid,
        "name": identity.name,
        "kind": identity.kind,
        "workspace": str(ws),
        "source": identity.source,
        "re_hatched": already,
        "files_written": written,
        "next": [
            f"From the global brainstem: Twin(action='boot', rappid_uuid='{rappid}')",
            f"Then chat:                Twin(action='chat', rappid_uuid='{rappid}', message='hello')",
            "Un-hatch this twin:       python twin_egg_hatcher_agent.py rollback --rappid '<rappid>'",
        ],
    }


def rollback_twin(*, rappid: Optional[str] = None) -> Dict[str, Any]:
    if not rappid:
        # Best-effort: roll back the cwd-detected twin.
        try:
            identity = load_from_cwd()
            rappid = identity.rappid
        except Exception as e:
            return {"ok": False, "error": f"No --rappid given and cwd auto-detect failed: {e}"}
    ws = _workspace_for(rappid)
    if not ws.exists():
        return {"ok": False, "error": f"No twin workspace at {ws}."}
    TRASH_DIR.mkdir(parents=True, exist_ok=True)
    dest = TRASH_DIR / f"{ws.name}-{_ts()}"
    shutil.move(str(ws), str(dest))
    return {
        "ok": True,
        "rappid": rappid,
        "trashed_to": str(dest),
        "note": "Workspace moved to ~/.rapp/twins/.trash/ — restore with `mv` if you change your mind.",
    }


def list_twins() -> Dict[str, Any]:
    _ensure_dirs()
    twins: List[Dict[str, Any]] = []
    for entry in sorted(p for p in TWINS_DIR.iterdir() if p.is_dir() and p.name != ".trash"):
        rj_path = entry / "rappid.json"
        if not rj_path.exists():
            continue
        try:
            rj = json.loads(rj_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        rappid = rj.get("rappid") or ""
        rt = _twin_runtime(rappid)
        receipt_path = entry / HATCH_RECEIPT_NAME
        receipt: Optional[Dict[str, Any]] = None
        if receipt_path.exists():
            try:
                receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                receipt = None
        twins.append({
            "name": _resolve_name(rj),
            "kind": rj.get("kind"),
            "rappid": rappid,
            "hash": entry.name,
            "workspace": str(entry),
            "running": rt["running"],
            "url": rt["url"],
            "pid": rt["pid"],
            "hatched_by": (receipt or {}).get("hatcher_version") or rj.get("_hatcher_version"),
            "source": (receipt or {}).get("source"),
        })
    return {
        "twins_dir": str(TWINS_DIR),
        "count": len(twins),
        "twins": twins,
    }


def _global_brainstem_reachable() -> Dict[str, Any]:
    info: Dict[str, Any] = {"port": 7071}
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.3)
    try:
        sock.connect(("127.0.0.1", 7071))
        info["listening"] = True
    except (OSError, socket.timeout):
        info["listening"] = False
    finally:
        sock.close()
    return info


def status() -> Dict[str, Any]:
    twin_list = list_twins()
    return {
        "hatcher_version": HATCHER_VERSION,
        "global_brainstem": {
            "home": str(DEFAULT_BRAINSTEM_HOME),
            "src": str(brainstem_src()),
            "src_exists": brainstem_src().exists(),
            "runtime": _global_brainstem_reachable(),
        },
        "twins_dir": twin_list["twins_dir"],
        "twins_total": twin_list["count"],
        "twins": [
            {"name": t["name"], "rappid": t["rappid"], "hash": t["hash"][:8] + "…", "running": t["running"]}
            for t in twin_list["twins"]
        ],
    }


# ---------------------------------------------------------------------------
# Global-mode hatch (opt-in, mutates brainstem source)
# ---------------------------------------------------------------------------

def _ensure_global_home() -> None:
    TWIN_EGG_HOME.mkdir(parents=True, exist_ok=True)
    BACKUPS_DIR.mkdir(parents=True, exist_ok=True)


def hatch_global(*, egg: Optional[str] = None, source: Optional[str] = None) -> Dict[str, Any]:
    src = brainstem_src()
    if not src.exists():
        return {"ok": False, "mode": "global", "error": f"Brainstem source not found at {src}."}
    identity = load_identity(egg=egg, source=source)
    if not identity.organs and not identity.senses:
        return {
            "ok": False, "mode": "global",
            "error": "Source has no organs/ or senses/ — nothing to extend the kernel with.",
        }
    _ensure_global_home()
    backup_path = BACKUPS_DIR / _ts()
    shutil.copytree(src, backup_path, ignore=SNAPSHOT_IGNORES, dirs_exist_ok=False)
    written: List[str] = []
    for fname, content in identity.organs.items():
        target = src / "utils" / "organs" / fname
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        written.append(f"utils/organs/{fname}")
    for fname, content in identity.senses.items():
        target = src / "utils" / "senses" / fname
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        written.append(f"utils/senses/{fname}")
    (src / HATCH_RECEIPT_NAME).write_text(
        json.dumps({
            "hatcher_version": HATCHER_VERSION,
            "mode": "global",
            "rappid": identity.rappid,
            "source": identity.source,
            "backup": str(backup_path),
            "files": written,
            "hatched_at": datetime.now(timezone.utc).isoformat(),
        }, indent=2) + "\n",
        encoding="utf-8",
    )
    return {
        "ok": True,
        "mode": "global",
        "rappid": identity.rappid,
        "brainstem_src": str(src),
        "backup": str(backup_path),
        "files_written": written,
    }


def rollback_global() -> Dict[str, Any]:
    if not BACKUPS_DIR.exists():
        return {"ok": False, "mode": "global", "error": "No backups dir."}
    backups = sorted(p for p in BACKUPS_DIR.iterdir() if p.is_dir())
    if not backups:
        return {"ok": False, "mode": "global", "error": "No backups."}
    snap = backups[-1]
    src = brainstem_src()
    if not src.exists():
        return {"ok": False, "mode": "global", "error": f"Brainstem source missing at {src}."}
    # Pre-rollback safety snapshot
    _ensure_global_home()
    safety = BACKUPS_DIR / f"{_ts()}-pre-rollback"
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
    return {
        "ok": True, "mode": "global",
        "restored_from": str(snap),
        "pre_rollback_safety_backup": str(safety),
    }


# ---------------------------------------------------------------------------
# Portable agent
# ---------------------------------------------------------------------------

class HatchTwinEggAgent(BasicAgent):
    """Generic twin egg hatcher.

    Loads a twin's identity from a local .egg, a public/private GitHub repo,
    or the current working directory.  Materializes a `~/.rapp/twins/<hash>/`
    workspace so the global brainstem's built-in `Twin` agent can boot and
    chat with it.
    """

    def __init__(self) -> None:
        self.name = "HatchTwinEgg"
        self.metadata = {
            "name": self.name,
            "description": (
                "Hatch a twin from any source — a local .egg file, a public/private "
                "GitHub twin repo (e.g. 'kody-w/heimdall'), or the current directory "
                "if it contains a rappid.json.  Materializes ~/.rapp/twins/<hash>/ "
                "so the global brainstem's Twin agent can boot and chat with it."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["hatch", "rollback", "status", "list_twins"],
                        "description": "What to do.  Defaults to 'status'.",
                    },
                    "mode": {
                        "type": "string",
                        "enum": ["twin", "global"],
                        "description": "Where to hatch.  'twin' (default) = local workspace; 'global' = extend kernel.",
                    },
                    "source": {
                        "type": "string",
                        "description": "owner/repo or github URL (e.g. 'kody-w/heimdall').  Set GH_TOKEN for private repos.",
                    },
                    "egg": {
                        "type": "string",
                        "description": "Path to a .egg file (zip).  Used for private/air-gapped twins.",
                    },
                    "name": {
                        "type": "string",
                        "description": "Optional alias to record alongside the source's rappid.json (does not change rappid).",
                    },
                    "description": {
                        "type": "string",
                        "description": "Optional human description recorded in the twin's rappid.json.",
                    },
                    "rappid": {
                        "type": "string",
                        "description": "For action='rollback', the rappid of the twin to un-hatch (default: cwd auto-detect).",
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs: Any) -> str:
        action = str(kwargs.get("action") or "status").lower().replace("-", "_")
        mode = str(kwargs.get("mode") or "twin").lower()
        try:
            if action == "hatch":
                if mode == "global":
                    result = hatch_global(egg=kwargs.get("egg"), source=kwargs.get("source"))
                elif kwargs.get("egg"):
                    # Egg path always routes through the scale-aware dispatcher —
                    # it'll DTRT for agent / twin / brainstem / neighborhood / etc.
                    result = hatch_egg(kwargs["egg"])
                else:
                    result = hatch_twin(
                        egg=kwargs.get("egg"),
                        source=kwargs.get("source"),
                        name=kwargs.get("name"),
                        description=kwargs.get("description"),
                    )
            elif action == "rollback":
                if mode == "global":
                    result = rollback_global()
                else:
                    result = rollback_twin(rappid=kwargs.get("rappid"))
            elif action == "list_twins":
                result = list_twins()
            elif action == "status":
                result = status()
            else:
                result = {"ok": False, "error": f"Unknown action: {action}"}
        except Exception as exc:
            result = {"ok": False, "error": str(exc), "action": action, "mode": mode}
        return json.dumps(result, indent=2)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _print(obj: Any) -> None:
    if isinstance(obj, (dict, list)):
        print(json.dumps(obj, indent=2))
    else:
        print(obj)


def _cli(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(
        prog="twin_egg_hatcher_agent.py",
        description="Generic single-file hatcher — any twin from any source.",
    )
    sub = parser.add_subparsers(dest="cmd")

    p_hatch = sub.add_parser("hatch", help="Hatch a twin (default mode=twin).")
    p_hatch.add_argument("--mode", choices=["twin", "global"], default="twin")
    p_hatch.add_argument("--source", help="owner/repo or github URL (e.g. kody-w/heimdall).")
    p_hatch.add_argument("--egg", help="Path to a .egg file (zip).")
    p_hatch.add_argument("--name", help="Optional display alias.")
    p_hatch.add_argument("--description", help="Optional description.")

    p_roll = sub.add_parser("rollback", help="Un-hatch.")
    p_roll.add_argument("--mode", choices=["twin", "global"], default="twin")
    p_roll.add_argument("--rappid", help="Rappid of the twin to remove.")

    sub.add_parser("status", help="Show hatcher + brainstem + twins state.")
    sub.add_parser("list-twins", aliases=["list_twins", "list", "twins"], help="List all hatched twins.")

    if not argv:
        argv = ["status"]
    ns = parser.parse_args(argv)
    cmd = ns.cmd or "status"

    if cmd == "hatch":
        if ns.mode == "global":
            _print(hatch_global(egg=ns.egg, source=ns.source))
        elif ns.egg:
            # Scale-aware: dispatch based on the egg's manifest.json.
            _print(hatch_egg(ns.egg))
        else:
            _print(hatch_twin(egg=ns.egg, source=ns.source, name=ns.name, description=ns.description))
    elif cmd == "rollback":
        if ns.mode == "global":
            _print(rollback_global())
        else:
            _print(rollback_twin(rappid=ns.rappid))
    elif cmd == "status":
        _print(status())
    elif cmd in ("list-twins", "list_twins", "list", "twins"):
        _print(list_twins())
    else:
        parser.print_help()
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(_cli(sys.argv[1:]))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
