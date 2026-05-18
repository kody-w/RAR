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
    "name": "@kody/twin_egg_hatcher",
    "version": "1.0.0",
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
    """Extract the slug from `rappid:v2:KIND:@owner/slug:HASH@...`."""
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
    """Workspace dirname for a rappid.  Handles both:
      - v2 rappids (`rappid:v2:...:HEX32@...`)
      - bare-UUID rappids (legacy v1.x front doors like Heimdall)."""
    if rappid.startswith("rappid:"):
        m = re.search(r":([a-f0-9]{32})@", rappid)
        if m:
            return m.group(1)
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
            "schema":  "rapp-rappid/2.0",
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
