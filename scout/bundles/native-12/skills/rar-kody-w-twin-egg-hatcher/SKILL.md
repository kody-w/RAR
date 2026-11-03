---
name: "rar-kody-w-twin-egg-hatcher"
description: "Hatch a twin from any source \u2014 a local .egg file, a public/private GitHub twin repo (e.g. 'kody-w/heimdall'), or the current directory if it contains a rappid.json.  Materializes ~/.rapp/twins/<hash>/ so the global brainstem's Twin agent can boot and chat with it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/twin_egg_hatcher", "rar_sha256": "2b59ec448480ebb09d910683e37b1e5925edcf7aa26b3695da6f2a6aa882ca9f", "source_kind": "rar-agent", "source_commit": "959f7f2524e8a2565c026d7e7e8f6a7fac3e95e2", "version": "1.1.0", "author": "Kody Wildfeuer", "tags": ["twin", "egg", "hatcher", "organism", "federation", "single-file", "rapp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `twin_egg_hatcher_agent.py` and embedded as the fenced Python below (sha256 2b59ec448480ebb0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `twin_egg_hatcher_agent.py` first:

```bash
python3 twin_egg_hatcher_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 twin_egg_hatcher_agent.py   # or on stdin
python3 twin_egg_hatcher_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
