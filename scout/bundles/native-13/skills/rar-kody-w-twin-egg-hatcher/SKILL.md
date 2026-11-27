---
name: "rar-kody-w-twin-egg-hatcher"
description: "Hatch a twin from any source \u2014 a local .egg file, a public/private GitHub twin repo (e.g. 'kody-w/heimdall'), or the current directory if it contains a rappid.json.  Materializes ~/.rapp/twins/<hash>/ so the global brainstem's Twin agent can boot and chat with it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/twin_egg_hatcher", "rar_sha256": "300dd7302be574e2460c2ccd873c930fb9a6f07057078afbe3da114c84b23ef2", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.1.0", "author": "Kody Wildfeuer", "tags": ["twin", "egg", "hatcher", "organism", "federation", "single-file", "rapp"]}
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
