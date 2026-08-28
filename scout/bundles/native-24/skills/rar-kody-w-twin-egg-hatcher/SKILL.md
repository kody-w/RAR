---
name: "rar-kody-w-twin-egg-hatcher"
description: "Hatch a twin from any source \u2014 a local .egg file, a public/private GitHub twin repo (e.g. 'kody-w/heimdall'), or the current directory if it contains a rappid.json.  Materializes ~/.rapp/twins/<hash>/ so the global brainstem's Twin agent can boot and chat with it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/twin_egg_hatcher", "rar_sha256": "0e307e62ab319665cfa3e6f534abaf47cc71d7bfbc2f1637e940ef2407c33c78", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.2", "author": "Kody Wildfeuer", "tags": ["twin", "egg", "hatcher", "organism", "federation", "single-file", "rapp"]}
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
