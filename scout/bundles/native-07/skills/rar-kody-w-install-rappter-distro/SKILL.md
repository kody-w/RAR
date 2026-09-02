---
name: "rar-kody-w-install-rappter-distro"
description: "Installs the full rappter-distro over a bare kernel by fetching files from raw.githubusercontent.com with per-file sha256 verification."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/install_rappter_distro_agent", "rar_sha256": "15ee1708f83dc55022bdf74d625b6b443d59f73371cd2f4c68100651c8f001d2", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "install_rappter_distro_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/install-rappter-distro:d3742eab0bbede4c8b141638baed48fe9bf150b8f68bc2da4c505433be9d8474", "kind": "skill"}, "version": "1.0.2", "author": "Kody Wildfeuer", "tags": ["installer", "distro", "rappter", "bootstrap", "organism"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/install_rappter_distro_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `install_rappter_distro_agent.py` is
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

install_distro_agent.py — single-file installer for the rappter-distro.

Drop this one file into ~/.brainstem/agents/ on any grail-kernel install and
the brainstem will hot-load it on the next request. Once loaded, the LLM
(or a direct tool-call) can invoke it to pull the full rappter-distro down
over the bare kernel — organs, senses, lib/, the rich UI, the @rappter
agents — without needing a separate curl|bash step.

The agent fetches the distro file-by-file from raw.githubusercontent.com,
driven by MANIFEST.json checked into the repo root. The fetch protocol is
two phases:

    1. GET https://raw.githubusercontent.com/kody-w/rappter-distro/<branch>/MANIFEST.json
    2. for each entry in manifest["files"]:
           GET https://raw.githubusercontent.com/kody-w/rappter-distro/<branch>/<entry["src"]>
           verify sha256, write to <brainstem_home>/<entry["dst"]>

This mirrors the "rebuild estate from pure GitHub raw data" pattern
(tools/rebuild_estate.py): the install state is provably a function of
the canonical raw URLs, with no zipball/clone hop in the middle.

Same single-file is also the manifest generator. Run it from a local
checkout with `--build-manifest` and it walks LAYOUT, computes sha256
for each file, and writes MANIFEST.json. The agent does the inverse
walk at install time.

Kernel-untouched contract: never writes to brainstem.py, VERSION, or
basic_agent.py. The drift-check one-liner in MIGRATION_NOTES.md should
still pass after running this agent.

Actions:
    check    — read-only: confirms a kernel is present, reports versions.
    status   — reports what's currently installed locally.
    dry-run  — fetches the manifest + every file, verifies hashes, but
               writes nothing; returns the exact install plan.
    install  — applies the manifest. Requires confirm=True.

Stdlib only — urllib, json, hashlib, os, sys.

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `install_rappter_distro_agent.py` and embedded as the fenced Python below (sha256 15ee1708f83dc550…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `install_rappter_distro_agent.py` first:

```bash
python3 install_rappter_distro_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 install_rappter_distro_agent.py   # or on stdin
python3 install_rappter_distro_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""install_distro_agent.py — single-file installer for the rappter-distro.

Drop this one file into ~/.brainstem/agents/ on any grail-kernel install and
the brainstem will hot-load it on the next request. Once loaded, the LLM
(or a direct tool-call) can invoke it to pull the full rappter-distro down
over the bare kernel — organs, senses, lib/, the rich UI, the @rappter
agents — without needing a separate curl|bash step.

The agent fetches the distro file-by-file from raw.githubusercontent.com,
driven by MANIFEST.json checked into the repo root. The fetch protocol is
two phases:

    1. GET https://raw.githubusercontent.com/kody-w/rappter-distro/<branch>/MANIFEST.json
    2. for each entry in manifest["files"]:
           GET https://raw.githubusercontent.com/kody-w/rappter-distro/<branch>/<entry["src"]>
           verify sha256, write to <brainstem_home>/<entry["dst"]>

This mirrors the "rebuild estate from pure GitHub raw data" pattern
(tools/rebuild_estate.py): the install state is provably a function of
the canonical raw URLs, with no zipball/clone hop in the middle.

Same single-file is also the manifest generator. Run it from a local
checkout with `--build-manifest` and it walks LAYOUT, computes sha256
for each file, and writes MANIFEST.json. The agent does the inverse
walk at install time.

Kernel-untouched contract: never writes to brainstem.py, VERSION, or
basic_agent.py. The drift-check one-liner in MIGRATION_NOTES.md should
still pass after running this agent.

Actions:
    check    — read-only: confirms a kernel is present, reports versions.
    status   — reports what's currently installed locally.
    dry-run  — fetches the manifest + every file, verifies hashes, but
               writes nothing; returns the exact install plan.
    install  — applies the manifest. Requires confirm=True.

Stdlib only — urllib, json, hashlib, os, sys.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from typing import Callable, Optional


# ── RAR manifest (rapp-agent/1.0) ────────────────────────────────────────
#
# Read by the kody-w/RAR submission pipeline. Snake_case throughout — the
# registry enforces no-dashes. The forge derives the holo card from this
# manifest deterministically.

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/install_rappter_distro_agent",
    "version": "1.0.2",
    "display_name": "Install Rappter Distro",
    "description": (
        "Installs the full rappter-distro over a bare kernel by fetching files from raw.githubusercontent.com with per-file sha256 verification."
    ),
    "author": "Kody Wildfeuer",
    "tags": ["installer", "distro", "rappter", "bootstrap", "organism"],
    "category": "pipeline",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ── BasicAgent import (with offline shim) ─────────────────────────────────
#
# When loaded by the kernel out of ~/.brainstem/agents/, agents.basic_agent
# imports cleanly. When this file is run standalone (for tests, or for the
# `python install_distro_agent.py` self-exec path), the import fails — the
# shim below keeps the module importable in both contexts.

try:
    from agents.basic_agent import BasicAgent  # type: ignore
except Exception:  # pragma: no cover — exercised by the standalone test path
    class BasicAgent:  # minimal stand-in
        def __init__(self, name=None, metadata=None):
            self.name = name or "BasicAgent"
            self.metadata = metadata or {}

        def perform(self, **kwargs):
            return "Not implemented."


# ── Configuration ────────────────────────────────────────────────────────

DISTRO_REPO = "kody-w/rappter-distro"
DEFAULT_BRANCH = "main"
USER_AGENT = "rappter-distro-installer/1.0"

# raw.githubusercontent.com base URL for the distro. Stable per Article V
# of the constitution (the install one-liner is sacred — URL shape doesn't
# move). Variant repos inherit the same shape under their own slug.
RAW_BASE = "https://raw.githubusercontent.com"

# The authoritative source-→destination map. Mirrors install.sh exactly.
# Used both for manifest-building (walking a local checkout) and for the
# source_dir test path (walking a checkout instead of network).
#
# Each entry: source pattern relative to a checkout, kind, dest relative
# to brainstem_home.
LAYOUT = [
    # kind="files":   every file in <src_dir> matching <pattern> (flat copy).
    # kind="tree":    every file under <src_dir> recursively.
    # kind="file":    a single named file.
    {"kind": "files", "src_dir": "lib",             "pattern": "*.py", "dst_dir": "utils"},
    {"kind": "files", "src_dir": "organs",          "pattern": "*.py", "dst_dir": "utils/organs"},
    {"kind": "files", "src_dir": "senses",          "pattern": "*.py", "dst_dir": "utils/senses"},
    {"kind": "tree",  "src_dir": "ui/web",                              "dst_dir": "utils/web"},
    {"kind": "file",  "src_path": "ui/index.html",                      "dst_path": "index.html"},
    {"kind": "file",  "src_path": "ui/tls_proxy.py",                    "dst_path": "tls_proxy.py"},
    {"kind": "files", "src_dir": "agents/@rappter", "pattern": "*.py", "dst_dir": "agents/@rappter"},
]

# Files the agent is forbidden from writing under any circumstance — the
# kernel-untouched contract. If a manifest entry resolves to one of these,
# the agent refuses and reports an error.
SACRED_PATHS = {
    "brainstem.py",
    "VERSION",
    "agents/basic_agent.py",
}

MANIFEST_SCHEMA = "rappter-distro-install-manifest/1.0"


# ── Path helpers ─────────────────────────────────────────────────────────
#
# Two distinct paths here, deliberately separated so the global grail
# install stays pristine while the rappter distro hatches into its own
# folder:
#
#   source_home  — where the canonical grail brainstem lives. Read-only
#                  from the agent's perspective; we copy out of it.
#                  Default: $BRAINSTEM_HOME or ~/.brainstem.
#   target_home  — where the hatched rappter organism is materialized.
#                  Created if missing; kernel files copied here, then
#                  distro files laid on top.
#                  Default: $RAPPTER_HOME or ~/.brainstem-rappter.
#
# source_home can have the kernel src either flat (~/.brainstem/brainstem.py)
# or nested (~/.brainstem/src/rapp_brainstem/brainstem.py — the layout
# rapp-installer actually produces). _discover_kernel_src() handles both.


def _default_source_home() -> str:
    return os.environ.get(
        "BRAINSTEM_HOME",
        os.path.join(os.path.expanduser("~"), ".brainstem"),
    )


def _default_target_home() -> str:
    return os.environ.get(
        "RAPPTER_HOME",
        os.path.join(os.path.expanduser("~"), ".brainstem-rappter"),
    )


def _discover_kernel_src(source_home: str) -> Optional[str]:
    """Locate the directory under `source_home` that contains brainstem.py.
    Returns the directory path, or None if the kernel isn't found."""
    candidates = [
        source_home,
        os.path.join(source_home, "src", "rapp_brainstem"),
        os.path.join(source_home, "rapp_brainstem"),
    ]
    for c in candidates:
        if os.path.isfile(os.path.join(c, "brainstem.py")):
            return c
    return None


def _verify_kernel_present(source_home: str) -> tuple[bool, str, Optional[str]]:
    """Confirm a grail kernel exists somewhere under `source_home`.
    Returns (ok, message, kernel_src_dir)."""
    kernel_src = _discover_kernel_src(source_home)
    if kernel_src is None:
        return False, (
            f"no grail brainstem found under {source_home}. "
            "install the kernel first: "
            "curl -fsSL https://kody-w.github.io/RAPP/installer/install.sh | bash"
        ), None
    return True, f"found grail brainstem src at {kernel_src}", kernel_src


def _read_kernel_version(kernel_src: str) -> str:
    vfile = os.path.join(kernel_src, "VERSION")
    try:
        with open(vfile, "r", encoding="utf-8") as f:
            return f.read().strip()
    except OSError:
        return "unknown"


# ── Kernel-src → target_home copy ────────────────────────────────────────

# Files / dirs we never carry across when copying the kernel src. These
# either belong to the source organism's identity (different rappid, keys,
# logs) or are host-specific binaries (venv) that won't relocate cleanly.
KERNEL_COPY_SKIP_DIRS = {
    "__pycache__", ".git", ".idea", ".vscode",
    "venv", ".venv", "node_modules", "logs",
    "keys", "peers",
}
KERNEL_COPY_SKIP_SUFFIXES = (".pyc", ".pyo", ".log", ".swp")
KERNEL_COPY_SKIP_FILES = {
    ".DS_Store", ".copilot_token", ".copilot_session", ".copilot_pending",
    ".brainstem_book.json", "brainstem.log", "lifecycle.log",
    "rappid.json", "estate.json",
    "private-estate-map.json", "private-estate-secret",
}


def _walk_kernel_src(kernel_src: str) -> list[tuple[str, str]]:
    """Walk the kernel src tree, returning (abs_src_path, rel_dst_path) pairs.
    rel_dst_path is the path the file should land at, relative to target_home."""
    out: list[tuple[str, str]] = []
    for dirpath, dirnames, filenames in os.walk(kernel_src):
        dirnames[:] = sorted(d for d in dirnames if d not in KERNEL_COPY_SKIP_DIRS)
        rel_dir = os.path.relpath(dirpath, kernel_src)
        for fname in sorted(filenames):
            if fname in KERNEL_COPY_SKIP_FILES:
                continue
            if fname.endswith(KERNEL_COPY_SKIP_SUFFIXES):
                continue
            src_abs = os.path.join(dirpath, fname)
            if rel_dir == ".":
                rel_dst = fname
            else:
                rel_dst = os.path.join(rel_dir, fname).replace(os.sep, "/")
            out.append((src_abs, rel_dst))
    return out


def _copy_kernel_to_target(
    kernel_src: str, target_home: str, *, dry_run: bool
) -> list[dict]:
    """Carry the kernel src tree into target_home (flat layout — boot.py
    expects target_home/brainstem.py, target_home/agents/basic_agent.py).
    Returns a per-file manifest entry."""
    pairs = _walk_kernel_src(kernel_src)
    out: list[dict] = []
    for src_abs, rel_dst in pairs:
        dst_abs = os.path.join(target_home, rel_dst)
        with open(src_abs, "rb") as f:
            data = f.read()
        sha = _sha256_bytes(data)
        existed = os.path.isfile(dst_abs)
        entry = {
            "src": os.path.relpath(src_abs, kernel_src).replace(os.sep, "/"),
            "dst": rel_dst,
            "size": len(data),
            "sha256": sha,
            "existed_before": existed,
        }
        if dry_run:
            entry["action"] = "would-copy"
        else:
            os.makedirs(os.path.dirname(dst_abs) or target_home, exist_ok=True)
            with open(dst_abs, "wb") as f:
                f.write(data)
            entry["action"] = "overwrote" if existed else "copied"
        out.append(entry)
    return out


# ── Raw-URL fetcher ──────────────────────────────────────────────────────

def _raw_url(repo: str, branch: str, path: str) -> str:
    return f"{RAW_BASE}/{repo}/{branch}/{path}"


def _http_get(url: str, timeout: int = 60) -> bytes:
    """GET a URL, return body bytes. Raises urllib.error on failure."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _network_fetcher(repo: str, branch: str) -> Callable[[str], bytes]:
    """Default fetcher: pull `<src>` from raw.githubusercontent.com."""
    def fetch(src: str) -> bytes:
        return _http_get(_raw_url(repo, branch, src))
    return fetch


# ── Manifest builder (run from a local checkout) ─────────────────────────

def _sha256_bytes(data: bytes) -> str:
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()


def _sha256_path(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _walk_layout_for_files(src_root: str) -> list[dict]:
    """Walk LAYOUT against `src_root` and produce a flat list of
    {src, dst, size, sha256} entries — the body of MANIFEST.json."""
    entries: list[dict] = []
    for spec in LAYOUT:
        kind = spec["kind"]
        if kind == "files":
            src_dir = os.path.join(src_root, spec["src_dir"])
            if not os.path.isdir(src_dir):
                continue
            pattern = spec["pattern"]
            assert pattern.startswith("*.")
            suffix = pattern[1:]
            for name in sorted(os.listdir(src_dir)):
                if not name.endswith(suffix):
                    continue
                abs_p = os.path.join(src_dir, name)
                if not os.path.isfile(abs_p):
                    continue
                rel_src = os.path.relpath(abs_p, src_root)
                rel_dst = os.path.join(spec["dst_dir"], name)
                entries.append({
                    "src": rel_src.replace(os.sep, "/"),
                    "dst": rel_dst.replace(os.sep, "/"),
                    "size": os.path.getsize(abs_p),
                    "sha256": _sha256_path(abs_p),
                })
        elif kind == "tree":
            src_dir = os.path.join(src_root, spec["src_dir"])
            if not os.path.isdir(src_dir):
                continue
            for dirpath, _, filenames in os.walk(src_dir):
                rel_subdir = os.path.relpath(dirpath, src_dir)
                for fname in sorted(filenames):
                    abs_p = os.path.join(dirpath, fname)
                    rel_src = os.path.relpath(abs_p, src_root)
                    if rel_subdir == ".":
                        rel_dst = os.path.join(spec["dst_dir"], fname)
                    else:
                        rel_dst = os.path.join(spec["dst_dir"], rel_subdir, fname)
                    entries.append({
                        "src": rel_src.replace(os.sep, "/"),
                        "dst": rel_dst.replace(os.sep, "/"),
                        "size": os.path.getsize(abs_p),
                        "sha256": _sha256_path(abs_p),
                    })
        elif kind == "file":
            abs_p = os.path.join(src_root, spec["src_path"])
            if not os.path.isfile(abs_p):
                continue
            entries.append({
                "src": spec["src_path"],
                "dst": spec["dst_path"],
                "size": os.path.getsize(abs_p),
                "sha256": _sha256_path(abs_p),
            })
        else:  # pragma: no cover
            raise ValueError(f"unknown layout kind: {kind!r}")
    # Stable order — manifests should diff cleanly.
    entries.sort(key=lambda e: (e["dst"], e["src"]))
    return entries


def build_manifest(src_root: str, *, branch: str = DEFAULT_BRANCH) -> dict:
    """Walk a local checkout at `src_root` and return the manifest dict.
    Caller writes it to MANIFEST.json at the repo root."""
    return {
        "schema": MANIFEST_SCHEMA,
        "repo": DISTRO_REPO,
        "branch": branch,
        "files": _walk_layout_for_files(src_root),
    }


# ── Manifest validator ───────────────────────────────────────────────────

def _validate_manifest(manifest: dict) -> None:
    """Sanity-check a manifest before acting on it."""
    if not isinstance(manifest, dict):
        raise ValueError("manifest must be a JSON object")
    if manifest.get("schema") != MANIFEST_SCHEMA:
        raise ValueError(
            f"unsupported manifest schema: {manifest.get('schema')!r} "
            f"(expected {MANIFEST_SCHEMA!r})"
        )
    files = manifest.get("files")
    if not isinstance(files, list) or not files:
        raise ValueError("manifest.files must be a non-empty list")
    for i, entry in enumerate(files):
        if not isinstance(entry, dict):
            raise ValueError(f"manifest.files[{i}] is not an object")
        for k in ("src", "dst", "sha256"):
            v = entry.get(k)
            if not isinstance(v, str) or not v:
                raise ValueError(f"manifest.files[{i}].{k} is missing or not a string")
        dst = entry["dst"]
        # No absolute paths, no traversal, no sacred paths.
        if dst.startswith("/") or dst.startswith("\\") or ".." in dst.split("/"):
            raise ValueError(f"manifest.files[{i}].dst is unsafe: {dst!r}")
        if dst in SACRED_PATHS:
            raise PermissionError(
                f"manifest.files[{i}].dst targets sacred kernel file: {dst}"
            )


# ── Install application ──────────────────────────────────────────────────

def _apply_manifest(
    manifest: dict,
    home: str,
    fetcher: Callable[[str], bytes],
    *,
    dry_run: bool,
) -> list[dict]:
    """Fetch every file in the manifest via `fetcher`, verify sha256, write
    to `home`/<dst>. Returns a per-entry result list (the install manifest
    the agent surfaces back to the LLM)."""
    out: list[dict] = []
    for entry in manifest["files"]:
        src = entry["src"]
        dst_rel = entry["dst"]
        expected_sha = entry["sha256"]
        dst_abs = os.path.join(home, dst_rel)

        try:
            blob = fetcher(src)
        except urllib.error.URLError as e:
            out.append({
                "src": src, "dst": dst_rel, "action": "fetch-failed",
                "error": f"network: {e}",
            })
            continue
        except Exception as e:
            out.append({
                "src": src, "dst": dst_rel, "action": "fetch-failed",
                "error": str(e),
            })
            continue

        actual_sha = _sha256_bytes(blob)
        if actual_sha != expected_sha:
            out.append({
                "src": src, "dst": dst_rel, "action": "sha-mismatch",
                "expected_sha256": expected_sha,
                "actual_sha256": actual_sha,
            })
            continue

        size = len(blob)
        existed = os.path.isfile(dst_abs)
        if dry_run:
            out.append({
                "src": src, "dst": dst_rel, "action": "would-install",
                "size": size, "sha256": actual_sha, "existed_before": existed,
            })
            continue

        try:
            os.makedirs(os.path.dirname(dst_abs) or ".", exist_ok=True)
            with open(dst_abs, "wb") as f:
                f.write(blob)
        except OSError as e:
            out.append({
                "src": src, "dst": dst_rel, "action": "write-failed",
                "error": str(e),
            })
            continue

        out.append({
            "src": src, "dst": dst_rel,
            "action": "overwrote" if existed else "installed",
            "size": size, "sha256": actual_sha, "existed_before": existed,
        })
    return out


def _summarize(manifest_result: list[dict]) -> dict:
    """Per-action counts so the LLM can render a one-line summary."""
    summary: dict[str, int] = {}
    for r in manifest_result:
        summary[r["action"]] = summary.get(r["action"], 0) + 1
    return summary


# ── Status (what's already installed) ────────────────────────────────────

def _status_at(home: str) -> dict:
    """Report what looks like rappter-distro state currently at `home`."""
    kernel_src = _discover_kernel_src(home)
    checks = {
        "kernel_present": kernel_src is not None,
        "kernel_src": kernel_src,
        "kernel_version": _read_kernel_version(kernel_src) if kernel_src else None,
        "boot_py": os.path.isfile(os.path.join(home, "utils", "boot.py")),
        "organs_dir": os.path.isdir(os.path.join(home, "utils", "organs")),
        "senses_dir": os.path.isdir(os.path.join(home, "utils", "senses")),
        "rich_ui": False,
        "rappter_agents_dir": os.path.isdir(os.path.join(home, "agents", "@rappter")),
    }
    idx = os.path.join(home, "index.html")
    if os.path.isfile(idx):
        try:
            checks["rich_ui"] = os.path.getsize(idx) > 100_000
        except OSError:
            checks["rich_ui"] = False

    def _count(p: str, suffix: str) -> int:
        if not os.path.isdir(p):
            return 0
        return sum(1 for n in os.listdir(p) if n.endswith(suffix))

    checks["organ_count"] = _count(os.path.join(home, "utils", "organs"), "_organ.py")
    checks["sense_count"] = _count(os.path.join(home, "utils", "senses"), "_sense.py")
    checks["rappter_agent_count"] = _count(
        os.path.join(home, "agents", "@rappter"), ".py"
    )

    checks["distro_installed"] = (
        checks["boot_py"]
        and checks["organs_dir"]
        and checks["senses_dir"]
        and checks["rich_ui"]
    )
    return checks


# ── Top-level orchestration ──────────────────────────────────────────────

def install_distro(
    *,
    source_home: Optional[str] = None,
    target_home: Optional[str] = None,
    branch: str = DEFAULT_BRANCH,
    repo: str = DISTRO_REPO,
    source_dir: Optional[str] = None,
    manifest: Optional[dict] = None,
    fetcher: Optional[Callable[[str], bytes]] = None,
    dry_run: bool = False,
) -> dict:
    """Hatch the rappter distro into its own folder, side-by-side with the
    canonical grail brainstem.

    Two phases:
      1. KERNEL COPY — find the brainstem.py under `source_home`, then copy
         the entire kernel src tree into `target_home` (flat layout). The
         global grail install is never modified.
      2. DISTRO LAY — fetch MANIFEST.json + each file from
         raw.githubusercontent.com/<repo>/<branch>/ (or use a test
         override), verify sha256, lay onto `target_home`.

    After both phases the user runs `python <target_home>/utils/boot.py` to
    bring up the hatched rappter organism. The original brainstem at
    `source_home` continues to run as before — both can live in peace.

    Source resolution priority (for the distro lay phase):
      1. source_dir       — read distro bytes from a local checkout.
      2. manifest+fetcher — caller pre-supplied both.
      3. fetcher          — caller supplies fetcher; agent fetches MANIFEST.json through it.
      4. network          — default: raw.githubusercontent.com.

    Never raises. All failures are reported in the returned dict.
    """
    source_home = source_home or _default_source_home()
    target_home = target_home or _default_target_home()

    result: dict = {
        "ok": False,
        "action": "dry-run" if dry_run else "hatch",
        "source_home": source_home,
        "target_home": target_home,
        "repo": repo,
        "branch": branch,
        "source": None,
        "kernel_src": None,
        "kernel_version": None,
        "kernel_files_copied": 0,
        "distro_files_installed": 0,
        "kernel_copy_manifest": [],
        "distro_manifest": [],
        "summary": {},
        "note": "",
        "post_install": f"python {os.path.join(target_home, 'utils', 'boot.py')}",
        "error": None,
    }

    ok, msg, kernel_src = _verify_kernel_present(source_home)
    if not ok:
        result["error"] = msg
        return result
    result["kernel_src"] = kernel_src
    result["kernel_version"] = _read_kernel_version(kernel_src)

    # Phase 1: kernel copy. Skipped only when source and target collide
    # (overlay mode — kept for the rare operator who wants to re-hatch
    # over their own kernel rather than into a sibling folder).
    overlay = os.path.abspath(target_home) == os.path.abspath(kernel_src)
    if overlay:
        result["note"] = "overlay mode — target_home == kernel_src, skipping kernel copy"
    else:
        if not dry_run:
            try:
                os.makedirs(target_home, exist_ok=True)
            except OSError as e:
                result["error"] = f"could not create target_home: {e}"
                return result
        try:
            kernel_copy_result = _copy_kernel_to_target(
                kernel_src, target_home, dry_run=dry_run
            )
        except OSError as e:
            result["error"] = f"kernel copy failed: {e}"
            return result
        result["kernel_copy_manifest"] = kernel_copy_result
        result["kernel_files_copied"] = len(kernel_copy_result)

    # Phase 2: distro lay onto target_home.
    if source_dir is not None:
        result["source"] = "dir"
        try:
            manifest_built = build_manifest(source_dir, branch=branch)
        except Exception as e:
            result["error"] = f"could not build manifest from source_dir: {e}"
            return result

        def _dir_fetcher(src: str) -> bytes:
            with open(os.path.join(source_dir, src), "rb") as f:
                return f.read()

        manifest = manifest_built
        fetcher = _dir_fetcher

    else:
        if fetcher is None:
            result["source"] = "network"
            fetcher = _network_fetcher(repo, branch)
        else:
            result["source"] = "injected"

        if manifest is None:
            try:
                manifest_bytes = fetcher("MANIFEST.json")
            except urllib.error.URLError as e:
                result["error"] = f"could not fetch MANIFEST.json: {e}"
                return result
            except Exception as e:
                result["error"] = f"could not fetch MANIFEST.json: {e}"
                return result
            try:
                manifest = json.loads(manifest_bytes.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as e:
                result["error"] = f"MANIFEST.json is not valid JSON: {e}"
                return result

    try:
        _validate_manifest(manifest)
    except (PermissionError, ValueError) as e:
        result["error"] = str(e)
        return result

    distro_result = _apply_manifest(manifest, target_home, fetcher, dry_run=dry_run)
    result["distro_manifest"] = distro_result
    summary = _summarize(distro_result)
    result["summary"] = summary

    distro_installed = summary.get("installed", 0) + summary.get("overwrote", 0)
    distro_would = summary.get("would-install", 0)
    failed = (
        summary.get("fetch-failed", 0)
        + summary.get("sha-mismatch", 0)
        + summary.get("write-failed", 0)
    )

    result["distro_files_installed"] = (distro_would if dry_run else distro_installed)
    result["ok"] = failed == 0 and (distro_installed + distro_would) > 0

    if not result["ok"]:
        result["error"] = (
            f"{failed} distro file(s) failed; see distro_manifest for details"
            if failed else "no distro files were processed"
        )
        return result

    kernel_count = result["kernel_files_copied"]
    distro_count = result["distro_files_installed"]
    if dry_run:
        result["note"] = (
            f"dry-run: would copy {kernel_count} kernel file(s) from {kernel_src} "
            f"and lay {distro_count} distro file(s) at {target_home} "
            f"(kernel v{result['kernel_version']})"
        )
    else:
        result["note"] = (
            f"hatched {distro_count} distro file(s) over {kernel_count} kernel "
            f"file(s) at {target_home} (kernel v{result['kernel_version']}). "
            f"start the hatched organism with: {result['post_install']} "
            f"— the original brainstem at {source_home} is untouched."
        )
    return result


def check() -> dict:
    """Read-only: is a source kernel reachable, and where would the hatch land?"""
    source_home = _default_source_home()
    target_home = _default_target_home()
    ok, msg, kernel_src = _verify_kernel_present(source_home)
    return {
        "ok": ok,
        "source_home": source_home,
        "target_home": target_home,
        "kernel_src": kernel_src,
        "kernel_version": _read_kernel_version(kernel_src) if kernel_src else None,
        "note": msg,
        "manifest_url": _raw_url(DISTRO_REPO, DEFAULT_BRANCH, "MANIFEST.json"),
        "target_exists": os.path.isdir(target_home),
    }


def status() -> dict:
    """Report state at BOTH source_home (should look like grail) and
    target_home (should look like the hatched rappter organism after install)."""
    source_home = _default_source_home()
    target_home = _default_target_home()
    return {
        "source_home": source_home,
        "target_home": target_home,
        "source_checks": _status_at(source_home),
        "target_checks": _status_at(target_home),
    }


# ── Agent class ──────────────────────────────────────────────────────────

class InstallDistroAgent(BasicAgent):
    """Hot-loaded agent that installs the rappter-distro over a grail kernel
    by fetching files from raw.githubusercontent.com."""

    name = "install_rappter_distro"

    metadata = {
        "name": "install_rappter_distro",
        "description": (
            "Hatch the rappter-distro into its own folder, side-by-side with "
            "the canonical grail brainstem. Phase 1 copies the kernel src "
            "tree from source_home (default ~/.brainstem) into target_home "
            "(default ~/.brainstem-rappter). Phase 2 fetches MANIFEST.json "
            "and each distro file from raw.githubusercontent.com/kody-w/"
            "rappter-distro/<branch>/, verifies sha256, and lays them onto "
            "target_home. The original brainstem is never modified — both "
            "the bare grail kernel and the hatched rappter organism can "
            "live in peace. Always run action='check' or action='dry-run' "
            "first to preview, then action='hatch' with confirm=true."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["check", "status", "dry-run", "hatch"],
                    "description": (
                        "'check'   = source kernel discovered? where will target land? (read-only). "
                        "'status'  = state at source_home and target_home. "
                        "'dry-run' = walk both phases, write nothing. "
                        "'hatch'   = copy kernel + lay distro. Requires confirm=true."
                    ),
                },
                "confirm": {
                    "type": "boolean",
                    "default": False,
                    "description": (
                        "Required true for action='hatch'. Without it, hatch "
                        "refuses and returns a dry-run preview instead."
                    ),
                },
                "branch": {
                    "type": "string",
                    "default": DEFAULT_BRANCH,
                    "description": (
                        f"Git branch of kody-w/rappter-distro to install from. Defaults to '{DEFAULT_BRANCH}'."
                    ),
                },
                "source_home": {
                    "type": "string",
                    "description": (
                        "Path to the canonical grail brainstem install. "
                        "Defaults to $BRAINSTEM_HOME or ~/.brainstem. "
                        "Read-only — never modified."
                    ),
                },
                "target_home": {
                    "type": "string",
                    "description": (
                        "Where to hatch the rappter organism. Defaults to "
                        "$RAPPTER_HOME or ~/.brainstem-rappter. Created if "
                        "missing; kernel + distro files land here."
                    ),
                },
            },
            "required": ["action"],
        },
    }

    def perform(
        self,
        action: str = "check",
        confirm: bool = False,
        branch: str = DEFAULT_BRANCH,
        source_home: Optional[str] = None,
        target_home: Optional[str] = None,
        **kwargs,
    ) -> str:
        if action == "check":
            return json.dumps(check())
        if action == "status":
            return json.dumps(status())
        if action == "dry-run":
            return json.dumps(install_distro(
                source_home=source_home, target_home=target_home,
                branch=branch, dry_run=True,
            ))
        # 'install' kept as a back-compat alias for 'hatch'.
        if action in ("hatch", "install"):
            if not confirm:
                preview = install_distro(
                    source_home=source_home, target_home=target_home,
                    branch=branch, dry_run=True,
                )
                return json.dumps({
                    "ok": False,
                    "error": "confirmation required",
                    "hint": "set confirm=true to proceed with the hatch",
                    "preview": preview,
                })
            return json.dumps(install_distro(
                source_home=source_home, target_home=target_home,
                branch=branch, dry_run=False,
            ))
        return json.dumps({
            "ok": False,
            "error": f"unknown action: {action!r}",
            "valid_actions": ["check", "status", "dry-run", "hatch"],
        })


# ── Standalone CLI ───────────────────────────────────────────────────────
#
# `python install_distro_agent.py --build-manifest [--src .]` — write
# MANIFEST.json against a local checkout. Used in CI / dev to refresh the
# manifest the agent ships against.
#
# `python install_distro_agent.py [--check|--status|--dry-run|--confirm]` —
# run the same flows as the agent but without the brainstem in the loop.

def _main(argv: list[str]) -> int:
    branch = DEFAULT_BRANCH
    dry_run = False
    do_check = False
    do_status = False
    do_build = False
    confirm = False
    src = "."
    out_path: Optional[str] = None
    source_home: Optional[str] = None
    target_home: Optional[str] = None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--dry-run":
            dry_run = True
        elif a == "--check":
            do_check = True
        elif a == "--status":
            do_status = True
        elif a == "--build-manifest":
            do_build = True
        elif a == "--confirm":
            confirm = True
        elif a == "--branch" and i + 1 < len(argv):
            branch = argv[i + 1]; i += 1
        elif a == "--src" and i + 1 < len(argv):
            src = argv[i + 1]; i += 1
        elif a == "--out" and i + 1 < len(argv):
            out_path = argv[i + 1]; i += 1
        elif a == "--source-home" and i + 1 < len(argv):
            source_home = argv[i + 1]; i += 1
        elif a == "--target-home" and i + 1 < len(argv):
            target_home = argv[i + 1]; i += 1
        elif a in ("-h", "--help"):
            print(__doc__)
            return 0
        else:
            print(f"unknown arg: {a}", file=sys.stderr)
            return 2
        i += 1

    if do_build:
        manifest = build_manifest(src, branch=branch)
        text = json.dumps(manifest, indent=2) + "\n"
        if out_path:
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"wrote {out_path} ({len(manifest['files'])} files)")
        else:
            print(text)
        return 0

    if do_check:
        print(json.dumps(check(), indent=2))
        return 0
    if do_status:
        print(json.dumps(status(), indent=2))
        return 0
    if not dry_run and not confirm:
        print(
            "refusing to hatch without --confirm. "
            "(re-run with --dry-run to preview, or add --confirm to hatch.)",
            file=sys.stderr,
        )
        return 2
    out = install_distro(
        source_home=source_home, target_home=target_home,
        branch=branch, dry_run=dry_run,
    )
    print(json.dumps(out, indent=2))
    return 0 if out["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(_main(sys.argv[1:]))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
