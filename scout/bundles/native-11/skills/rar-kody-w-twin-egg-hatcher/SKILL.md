---
name: "rar-kody-w-twin-egg-hatcher"
description: "Hatch a twin from any source \u2014 a local .egg file, a public/private GitHub twin repo (e.g. 'kody-w/heimdall'), or the current directory if it contains a rappid.json.  Materializes ~/.rapp/twins/<hash>/ so the global brainstem's Twin agent can boot and chat with it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/twin_egg_hatcher", "rar_sha256": "0e307e62ab319665cfa3e6f534abaf47cc71d7bfbc2f1637e940ef2407c33c78", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "twin_egg_hatcher_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/twin-egg-hatcher:990d0181ffa7fcc78626c7efea1842d459527d4a55bd4d036c11f66d2fee4b5f", "kind": "skill"}, "version": "1.0.2", "author": "Kody Wildfeuer", "tags": ["twin", "egg", "hatcher", "organism", "federation", "single-file", "rapp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/twin_egg_hatcher`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `twin_egg_hatcher_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `twin_egg_hatcher_agent.py` and embedded as the fenced Python below (sha256 0e307e62ab319665…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `twin_egg_hatcher_agent.py` first:

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
    "version": "1.0.2",
    "display_name": "HatchTwinEgg",
    "description": (
        "Hatches any RAPP twin from a cwd checkout, GitHub repo, or .egg zip into ~/.rapp/twins/ so the brainstem's Twin agent can boot it."
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

HATCHER_VERSION = "1.0.0"
HATCH_RECEIPT_NAME = "HATCH_RECEIPT.json"

DEFAULT_BRAINSTEM_HOME = Path(os.environ.get("BRAINSTEM_HOME", str(Path.home() / ".brainstem")))
BRAINSTEM_SRC_SUBPATH = Path("src") / "rapp_brainstem"
TWIN_EGG_HOME = Path(os.environ.get("TWIN_EGG_HOME", str(Path.home() / ".twin-egg")))
BACKUPS_DIR = TWIN_EGG_HOME / "backups"          # mode=global only
RAPP_HOME = Path(os.environ.get("RAPP_HOME", str(Path.home() / ".rapp")))
TWINS_DIR = RAPP_HOME / "twins"
TRASH_DIR = TWINS_DIR / ".trash"

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
