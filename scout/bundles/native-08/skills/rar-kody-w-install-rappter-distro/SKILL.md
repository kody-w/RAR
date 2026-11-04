---
name: "rar-kody-w-install-rappter-distro"
description: "Installs the full rappter-distro over a bare kernel by fetching files from raw.githubusercontent.com with per-file sha256 verification."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/install_rappter_distro_agent", "rar_sha256": "91f2128926d613cc537ff4b3e5327a35b0268d0eabd548a828d5009af956b803", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.2", "author": "Kody Wildfeuer", "tags": ["installer", "distro", "rappter", "bootstrap", "organism"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/install_rappter_distro_agent`. The original RAPP
agent is preserved byte-for-byte in `install_rappter_distro_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `install_rappter_distro_agent.py` and embedded as the fenced Python below (sha256 91f2128926d613cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `install_rappter_distro_agent.py` first:

```bash
python3 install_rappter_distro_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 install_rappter_distro_agent.py   # or on stdin
python3 install_rappter_distro_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/install_rappter_distro_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/install_rappter_distro_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/install_rappter_distro_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/8286ZLj2JEm+ipxs39IGmQWVmKpaY0NNmIhARA7gc42Cfu+AwQIjebZLxgRlapqdav7mvWPG2ZZSQJ+/Pjx5fPPkYX4y5dgmfNu/PLzl0sXP9/coo7TZEnGL1+/xMkUjUU/F1173JbaaQ7qenqb8+QtXer6bQz6fk7Gb3ExzWP31j2S8S14C4MxeauSsU3qt/D5liZzlBdt9pYWdTK9pWPXHAvXn7JizpdwmZIx6to5aeefouPOelx96w+dL+m3KQ+QE/526C3SIgpehvx02JVsQdMfyr78/C//+vVLcXz+8vNfvkR1ME1/s5N7N4rODs3Hkjpos+Ne/zzO2h7fjy3SbmyOS3GSvn1++/339u3zZ0rq9OvfvgbRa++f3w6Vb398+/4lypOo+v7lVxLHIdJibH5+C7uuPmTOQT0lv7ofjkEb5b9o4PgzbV+tPzEGrbLir8Smbhmj5E951yQ/v2nvrg/qfzkW/euxSu3aX6ucgzFL5v+a7P/4H9V6iE+fl/7w9u1/vUz5+W8SRfp5yrc//uqEvxJ4/YzJvIztWzkdgYiXpp9+/y73+z/84T9UdARjXqb/gqYPwX+kKh6f38al/S/oKj5y4E8fmfn734r/Gz//8Vefv/7aqX/81eevf6/iI6J//Pjr69th3J8O4/5ojcu/lf71kf7p7Xefxv3uKJJ+fgum95qJqm9H/vfBcaEujmtHPr79Lg+O2vndT/+eQ4r27fffv7wLHHl4OOdT6/cvf/g33jnWtN38I0H//iD9mDyKZD2S5j9123+T6/6/ue/dhX9/6e+j/pd/f6fvX7pXJv9dSf5WJhnHbnyJHbn/4ap3vDm2GZZiTOLfVPtvlx7wNn+snJIfjv7jfJzkbe4O93ZRksQf0PbCzl+C9h+p+4zHS+Pnx39H9K9/+P9xDfx7nv51EfynoftHIftVqNLvX5a2aru1/YHQf/n48P+Mf/07D3//8jhqK/7Th8QLkt7+5W9Q/iuo+vprrHl9+YzYv/5K4V//8OWvX9+Lblw+9B295J/+6U0porGbunR+M6Numd8OHXPRJN/b762VF9Nb8dE/j7gm41SER5P7kDuypEw+SrtL3/78v6ujGX9bwV+C+NlqP4P5p+DV1v7805t1qOrGIisO5H8z6Nvte/t+67XNkTtHc30cmRc+5+TbASjfXh9eyPHnf6T2p/7557egjV+CL1MNVnqLgn5a6uSn1zHcPGk/jY6C9i3Zkmg51NZddNjw3uS/HsebuvpxpP/ryFNVHGQhPooomrvx+a77cMvPL2V//vOfw2DKv7cfnRl9+2AcE3gI/DDn7du34zBpXWT5/L1Norx7+91f/vq7t//z9o9WvSt/7XE7eMGn0w8LZVNT346kXppDbHqHvCSI353+l79+uvRQ0x5c5oN3JB+L66KtDhT49K8p0t9e1CRMDr8ePm36bpxfLKeYf3qT0rcf9h6bvm69QD7vpvktTvqkjZM2eh5ag+M4Pzz5AunpwJwpfX59O3jR+65/Pkrr3cTmT9Eh/uc3hb0doHJQjANZDjPfhY7FXXvwo/pH9D+uv8jV76Y35hcVP72pr7R764Mj7vkYfO6RBh9xOTrOL8sP5cFbe2BQ+2JXyctVH+zr3T2H0OGZ6DOkH1TtaF7NEdjpl73fZYL5yD6rC47Nx+/t9JnfL354LHzRxedbthTxAR7J//xMqSnvljp+999h6UvTZxTiz6i85+Bvse1vifJ9QSAYe5uOSNTJh2GfooeyV0t9T4Pf0NZ3fdzY9R/JetCmt891hxP+L/jTjwCA77tM4NvrCO1h+XGj/vZJdD93eeX29/a1yY9lB+4f1/Nu/lZ3R54V82v9S6JNtvm9uyTTkTPa4YO3l0QSf32/fb0q39vfv2Ly6ef3sH87olz/4b3wivbRVclL4avJvPj4f0TM4wMgv7fv9PzdtF8R9E+HdWMWtEfdTskRpePvugjBDzOOOOdvtvTx5X9/Kv7Ms+mX5a/W9gpee/S5VxEEh6JXkh2wEC1j/X9eJX7QzaT/6QMHk89Ee58NPuvr09aX7w+c+ojdPx4WDjSOx+JxoNExZii0Kp150/rp1VTe3kE9iT+C+FH6/VEvXTd/ZPD7xi/MnbvoqKViOoK2Hl7Mj5qY3oHphfHwT28Cb73l89xPP4Pgf2gI+AnWv3U7+M8fbfF/gb+x7UM18tN7OibBYcah5SiEo26OAirSIxuOrvSOo0fH+S1d+2+x5p/f9zv2mMbo2OF//WaH92J7fg5eX9/WsZjfScw//w2HXlTgV1riaf7Q8tngmuLVnT9i+v3LmITLMVG+Ja/e+hnQfjnyTyhmcQlfwX2Lgzn4/uVApfkw91Dz+1eiH1j+sfRPH0uP6v7Dz+9Kfym1D43vja57BGF9NJYj+9tfeuhHGf6AxvedbON6JPc7EWu7t73ow0MRGNWvos8PBPjErqaI489mZwZN8ls4OZC8nj6S6pd4/QJ23fjTm3Fg8lGS7wcNPpri9/Y9HV8F8r71n799ez/Zt1/Wf7bb43ZQV9PblfY02/r6gtT+6KzTZzS+tz8y5mXJ1/dF7wGafpv9Hyn+UWFx91leB1ochOPgIa893oL5hxtf7OT9qJd3RPh28JVuOQyOX0R2Ho/e8PNR1y/s+NzryIYfyXBE5eubwxumpKlfDxT53h6lXkQ/APnDlKNK0/nbuxNe+PrtaKWHusPZiiQYtHWs/ZOqWbz5UxN/4v/RLOYXbPav1h2kR168o/8LW95R+kP/y2r6g3x91snHHi+u9wFMR8ePv3Vt/fz5F1r+asS/YPYnR2rnrz+69DsrO/R9zlwfjPDX+j7E1qMXH531ALfxWF4/f3SZ+CPk9fNTwSeN/KHg14j3I32At+S9F36E9QfrOMAof4FxuMx/x7w/Y3Fwhtezlf/5yag/9CbbEbQf8e3roP005pdLvxhzAERd/Btjjgz+GHimH4PMayT7KIY5PhrD28ufv6g40P249PWdyn99t/j9a/fqJc/p9bCmLqJXU/nyc3t0pq9f2qOgDqb87xPQ14OZo200yXFpej3TOUq7Tw5i9XrW85eDb/8yjH08+Zmf/UtXF76Y84uOH2edPx7r/OXLoSR4Icunmk9yfYiPwfhtenENEP4JOnY8vn/k63Hvv0K7P5d8FOWxhoJTBEZICsFjHEaj6IQSaYqFaHJCESJATyGE4GQMJUEYnzAyIBEyPkEQFaTUCQ9JCD30fU5fLw5VvMwIIyiFcQom0yShQgRBcYhMoBSlcCIN8ARFkpiEICj829KqaOPPs30Y+deXO36ZAF4++DziX76EOHZIitgk0R8/LAjYFIJew6d8f4BSnySXmd9lVifcp3n1iHpUgrJJRWE+XatdwPpLnlVNIRW8QNM2dykDYUmpTEPI7n6qSuQetjp6LXQ47i++e8RPpsUOopB2B5GIaLEKfAx3EAtB7GFhqDUbcqiOblKLsCn1m7XJvcem/J007lEzNV1GVoCMVJE2YqekePCE6bC6f7sj6GD4J2OCWMYtW5DkS/IuLeqjwXl29muVJi8DVZc8xdfeBJXIxXBYxfCNxxSeypFA160gJCOuoZkt6rMb1Y6mn1drvW6xwdeCtXnFwkdoB9E7u10MRPL3GE/E8HSZHndxJPWbaYTtDDg8KHLIM6PWs7QMbgVpHNCWhnNyK5gEwYdrrZirQE2XY/XTlaZpFPj6dFkfU5ESKlzZw/a4PQnGha+rSMfG6bGNKeM40gzPSvbUgWtwtQMMKwpVvp+7tJsvTFrsiBTU+kJTlq6jQOoIWkRkzYmXEiGkZyY2ytS8d5gynaW5l9tSj6qR3sAqSHe68qGk3U5PnFRB7BTjMctrSy+fBTaunUTPU8Od1OYSFSCJc5cAB0jt2ag8r4OqpMcrU0TxiWtv8kmJLzvjG7IfPK8aT40D7NU7F1867pbmgkSBumir1MWfoatqyLQAgEnbI1d9leHTKtBS9XzC4fiUJ+maTSwBYv3qkLmzVOKFWcaNVrXxxi51viNUcb1wZm6NlrI/T9b1gtWSIqH82O9PEjulQEgaKBs8JSvk6anWeUHKUeW2y1xnPfJk5gQFT6ybBR4Rocn9qa5sYByxAcHn9SJf58vJKbbSlQBPvrCBxxi3JXBXl1stX3g06lmv87qJsDy2Q5/WdNvE9T7ptSNvXf0J31G6QAv6FpvzxkKXp+cU4ZMpV9vi4jMo3XCcQfTbpvazzLeZadAskD7uA6XT53thFb3M7mxmFG2HM6daMdOZy607roaSYEajK9xGzhFFavPXlMV3LzxxidnvuMoWrd0xZyO582e9gSozqyeaAy1fHCXpWZiIfSFTsgZBeWK1miuY/pHQjdjia99IjUqr6xOuL0tXsL2MLentoiKSsnLMU2ttR9lqVdcSKciHXCof5N3iht1+kIWj6Kmikg9+2p995CLcFTLpJaPtXYkRCSbjx709EVHrJSDN+7zHabbY2noueaJt9G2mItM9HRz8eXkofauZm6cF+ULftSt78ShB33RREhFAI6qHFqZoxXd7eYL4O4pxjEc1TyQR946TyCzDfBHxaYOjWe7MDPatkPOKG2YQS0TeBKinknMNikT+07oNhCJxWgLHt6O26B2qSAzqzpRo3cHTIAv4lZE9VbklUz9va2UCNW0I97N3oWtdX1zTP1dGQhYsw/fAVJW6M4x2N2NCp/o3P7ZbBGwXuSjKYpAqYOqyXmh0RDCVve7czosqNbvfKZbnDh9Zh/F1OMv9wCISTq+j6tcRg59QtVA19nzjF/qKFyGFJ49MCgzlLNzAovYtXdQwczuPNUYXz1RJyMOO6awJ+q51gwP5ut3BV6Oi5+soYcwi+wx8z6zifNU5ktlVxb1aXsXaObbR4B3zSqR2PQol6bU7h6Ie9nFSJ+KdPI6SthilbxjzpKswk43SpiSxFM586PaW2d+Vxm+8WqkmzwvZqDe2jFtlu7b9rDa3rR7JOs6BR2bdXEXNPYm2HUjf7KDwDeVSaN6tHWHvwCupTVv/mTzuO8GM95G+ZqcmdtiDPjEPrnhspQGe5b1U6TMv+XL6APeFumVR0/kPtMfTlr5fhUvgj5SK2Wev4+DYYL0ioXche0ywnvQc5KfsUcDCHEWVsqZcLq5DrFfhpimguetGq9jARY6Hzs26cvBoYJ+Yzrh5D/0s5X7OuPqV1fsjPJw3gYt+h7nes9kLxDaDDHecIezsEoVjvt2FXQiYk+7Biwb71rO3GTKc9YDvyJqkIanR7QsMNPjUVjr4bO0MFU40u5GMqw1wdRc8zRHdi4orTtzXNx6jGCVgUAZoSkug7/qlyO6QMTRGLBrJKLXZsGXVg6d5u1l0CORQk2X60i0iSkg0oeE5jVZgbcv02UvzlIa5CuG7qrgXnJ3ZRo4aegYJeN+w3Y2s6CAHduhBCRDnPtAreEhsUFs0MXtD7w3smqw1FFu0JidazLQLegHWtBEZ3YX2bJKfwdloTDCCBdi/ZVNK3hR8EkqE5XuIpYZrv06+1W2z4OJA9bz4Z2Uze990zVKXtxoKbcXH2RRSHjIMJ1UoikbH3enLojvmY1IvjKmLlnLQtrNSXzxIXHIEOwsy2996en+iIms0fKjQ+snjdM5dvKxSFnt90vLUTTnAd3dMZVGyIrqMfhiylG5N7idIAW+PDVj36jIS8UaFTmiYpVdq9JnbnR04h9INVgdBABzVAJ8jx6urOYL14E5PKR869pbvLoG7fj2eYF6ur5XAF6s9WY0pDlWHxp6Mr8zKqZkfXcy71zAHklwwVZBS7h4ENNQ4krADBZSx826qMnGdzR0KL2M3dCZ6hk/zinblmpVqcz2nZKT0Ljeu2nnMRcRy5ORuLrBJd2J8qo0oJPjBag6sLA/YsYJedVnXzPvrzQsNudZGNPelo6S2JeLYuxqMjIjNtZrdNh1TKgkUdTu3PDBE1aYGywVRD84wODmmP3FGFhkmv9YteT8XzgIKPJMXeohajkVOUtkD9916qGDP7csqd+2qXfvsuqm+brGqyx3Ik50dPZm83Bd9iVSexsRsxSgnsAuwHodPmuyZHQWSq6gQog7UOVhzNDLkEeku07UV5acJ9ZJZnPmtdmuARRVOPt1hg8EfNgXxjNkOBNt00vXVsnjmaR2VFl3xGkNieDDgkgqCooq6QeHP1oA/HzLNAXe+cU421hkUDRo30qsd3iHnLsvCoDyym1mX/eL6cmCErJ5bRSGEF7hiL3N362uBLaBzL1zCKJDhVqVGIcqAgJ2fLJB3BVrZ9Cl66AepAXm79gx3CKEeADwUsyr6Sp4HOwI9ESIhHL2Ddc5lawiPFNcRLZFxdMrT+A7bHdoUT2AJ8VsxNDu0NwFNqkSVa7F9Hc43wbth07XsmWREBtRhqsVp+SdJh+CjRtKDWYEcdFLhcJXvdzxSsQyhtEcJAyDQkeBthAAFuRIHWZVDtlDRHIxbKRDbowksXtQSzTzydBgUN94JgbUd5IHxgMPQpYskGvNOOJ0bV5EJcha4wShNVzzdVpGnUbYZ2k1PU3NK2s8sEqYS8c4Vp5gq6DFLQx+s93rjaia5SiIE2hx5LQbzcnlIZ8XVYVqGjMhW9Asmz87A1RfbkDub9mHcxtNuEOQ1ATcGSO8bktWlh5uZeZnyXZIQq1NhhAa5XXUyDSNAYAePNBmeZsnWvRBALOkMp+Qc0tWyGTPdJZ6dLX7XME9Vaeh2Ao4OLOJSv9rSAbgXIZZlkhSetymh9QxbR+6EhiMyVsVF310e31h5OsNXnKCyi4WZCWxbmw4RbsQ6tZbIaIYwsyHR2obJInehzIh+ij74vFUqszwn2vMeBTeldjSVpwDgTldRSQ0z30nutg0VyWBrNwGCL0zzXt1SnYfp23JtGBqHhp41MrU0kmjV1kpjk5pjdMLbPQ8Q3SqVK9PZz6I0tBZAkiBjONpKRhytn88ngBl1+EaIQCKUGgDqEsTNR8xodmAq7hQkbVyCAb3Hx7wDrsBEU85EIDimcE5GzPru9DEkXJRcvZ21siFrG6rmFIcBkhHau9ZpEDM4O0oHYLW5Z+tg0WSJVyw6cUS6YNNwjVSnuoORcpaRODmTjzkOcOHJ+r6/3LG5oYGy5ou7MyPG5KBuReNI95CzRvGLMJSADMV2crs/WTLOfXvaXZPQaZ2Wjk5d4FcwZwIflBKOjOpVIVSIemhMwW5ZdAWdi2YfZAt7tpVIG5MZyoqxCYUl06Gw7lpZA1HbrtajnAAQJBSA35CAd0O4GOnuQdm4yHBXg/AhrpPOMk4BN6Ki7gKID4/SqjpOaG+56I1ubq9bBJ73Z4HrNQeAu12BMtUota3L9rOqzJbXPebgJGTtMThTdq6MOUgFMAnMTfcBgir4VUCblF2kiw3Zi+M3Op80540XE/NoewpdeM+dquwGOajzdbA4W2Ce5hK5BmtFuGlqK5RJvbbYDKPrXXuxrRj0wFOgj105dZckgaryZjswILtQezFu09Cy8Aims7APKszW4fOGKTGVXtUDP2Qc5IgZp24Qd4FRY17uEt9fhoc2WPSA5T2HTA6PZsbMoN41kc8gnWtwsOkPtmrGalrPjNWt0OBE1zQYPdOTH1pU5wn+vBa5uwy0HfgWX/MP2dmnpszaKSJof8E9ypnV3CblxLSfzytXgu64nCVt4Jmbcril6XYp0TIk2xcJRLxMcM2utcTldGnmXp2TJyu4pyyMGn52bhLdWHdhUHaBCW7wrvpZjshWIZ/sJ39TPUPLy5MiSZPhukWf2RMqiVHnT08ebvYcOmKJSQP7MLg6TYyaZk+gvRg+fTbyzZEju76aLEgxLGCpGE2dqgyFRfBasl3AMEurA0/yhp7vN0lRrcpgQc0qrnxOYtph7A1xuoPPBTqw0bN3P5gl7uTDk6u2dNVZB70pFFG7ymqUVdSo41VPkFV4zFmWVvT9xFLN2cYkNnruSBgPhj2oPbPec0PXZdIVIrxAVzPmTkwCnRe6ctBnv/IMmxaDzt6DnXEXW3swXQqdXZ3HJcZFnDY+hqyTUG8bmcmtAl09BNvNRJk2LYPgy5meuf6U+sPlDIMu9kiQ0DoHsjruevtMdXygDJaC+3uAcuYV909tR6xIlMfp9YZf9yzhME8MVhNWHlL55PxVyPimoFYta5l76udpiVryxmeeXVnWc6Du8P4U4Rg+L+mJlmJnYGIpPmaWtZ85KPRN1nb1sys024PdHoHVFeruphq+oADEYrphPqx68ovMiWqT44QNXBwKfRIzmtdjF9Lb1WvzMG5yuDEhbxWNYz6FAun8XJ+KWxwFvtaQZnKLOahBfo/FfnhwGmp3CyLcr2RZw7FSnPhNEJsez+nY96Wuug4mkrICBJGJsNDPBrh3lQEw1i6lID6JYJl6UA9PCk2tK6+A2Y2vhucZ7WwZC0lKg67+XHkCug/YrkhddMB0LWxnNQWRFERdhR1lD2wFQwZgX7xc6asq8FhmdVe2p2M+2KWC3EQz24WiaGUXnS2scfgZuvi6n/mMC3rNbOUGAAW67rqrpJknxz7GFKUC6+i86GR2za9eYXqWVx8Z3qe1dbqEykp6fGsJEkRaTCMFvnxm3BDNyyQjxM1lw+gEm61cM65cltktbecXW6mctCyI8AFyCgUAoBwDCnq1yQfIKjfHzwOGMxLhcmkMJ8naIzrFHTnRmnLMkoL2FFB8Sqf24MqF4YFXIlJL3Dutl+Q+mU95jerZz/b5BALAMZzsJUPrEMUrQXVd6PZk8SzNe+CTmhxIDEYyjB73E+zZawNo+uOmq7McdBrinQbu6TPpk9xOdIEFvW9N/qnYM+nuSHuK3zIrT23oFE+gISB9d7FyZzqQtdmADqaz2Y9h6WhvawuuZ4DJUFLYlZH0PHdWUxXGnSjzlS3GkucKKNncFEs1I/2FRq91earUfpsj6OYynK4I9Dh0fQUOjn639FnfoH5l4n64KPStzqyVTRj+4IBM0J0ZfgFt6KKSMOJhWUKcXaMx2BrjUXzPeXZuFRZv78aN5iGjAwHGQeuJpB/CPB3s1k5A+wH3gskO19vmJTWOLn6WwYwcxUZ10/SLvNlXOKEMQjGc0zqpmvOQZsyPzU2VpaAt2BuWwvYF2WAFWfe9rfnhSEFfxqUMtRjet1JqVLlebS666BdVg9Q9Qq/nQTMp3VhhwqVuEV9EOmuoqu3c7tFgAaDmdUFgp3Ts4MQFclJavgcaQNYC8wjdsixtBu0j3fBIo1Wfx9B90juPoJidWQ8aQtMljV2Eg4qhTUaRKMofUxZ1lFt10Uu1rc0Z9ONsXQp/OlocP55OpBLJQzUynr9pjLHcaEXUop0dr/fCUmFFZIeZU6EBijwheFT+Jll0XY4mOkb6kXdiwOlE6m0oYQle+bzrCqR09aJivkvukcwROgGsro9uNK+KzR04TWOWb0zFQglDiLbuc26pbHg859dYpxIlOdr92XCtbZa2qg4wTdNJcM9j+qY9j16hOoB+N6kyQKyL7Zy5ecQr8qK6Uej2BUo4Pes0eH4OG+1ZkZSQCTF2DujOKe9xTRaxIh8cHSsr6E4pFabfsD49XyzrEj3LdjhJTTKn7YS2oa9qAiEqJyfPeSdta4mesTnolY3smw2OF5YWAqK8YDXSajCFx1XSwZV6wSJvoJn8UcG17R75coxHbqcW132Ws6WAJHpYmPGKlkpJXeGlIJ6muMgMtIYae1+DomP95jhBYTLwkz1bpGHFZdEYpuX0eZqdZEn0daxfdJCr8zznnNPFMOHUEYkiEO+4GdcFqZ0g/nEQXH07RmPqwV2pEkHnWyE8UJ5nbSi+JHU0XmxZrOlqug6g1m2xLUd3aU5H5aIqkjBeTU8fHoJwWzuaWOuGTtZCzTbZy1BhKRnEKkSQvXHxNIZZLYJFwvsFfZfOVy052DNFsfbFuaxrsw4mTqDtqbCy8Jgab1KdYsuJsKq0lx1pCcWjDoSdsLHqmZsXx9Eh53zzZtZUpXPCRDZqZNut2017PN8tj7SuNQdmaqucNgqBz5zjKsrGe2zugUyAI6q6HeOrDqv4ib3Z0oANMkUjPIEePOhpIgpz1p+7N5kzNZoWckKSc51ffPJsxM+apKWgCp4YE15EF2JVbyylk59VuRoz/HRSImyx5WKg4oCyw0svpXIyHmSov6oPE59NVyA2ayCMBlLJkff6+fwUJq2qmSsFmxQIeHMKhDTQzsdkAiy+fXvE9lMsswFJ+GunXiyYFvLLFdyWpGrmqLovVfTYjbNRc1inLs/7PbxMgVYncXXXef3KIe2dLc7+mTXY2Ywl+P6IIcAUTzAiRllb+eJNwF7/KkQ48NFapSsX8UevsiVl2hWzMFftcXCPOUGa0b2fqJ7T4OrkyQTaraIcO9GR5QM3oAnVPE/z2VAKT025mz1FEdXqedzhfNsxt3NNnu623ppdLKUMoT/KEfIIbMm8KLjjYEUCekbDcXS3nt6i8Eazggh7MbmASM+oxXMqjLrlcl20EV1ai1FYH304+T18uuqg2c+DEHtSZdLg/BgKbrURq5pYo2X1C3lL4bkt4ZgnwKkhtWIaYPN+u2vuVhNBzxCNqMf5gnBI041njJJjOgN4PZ9xQFU7O1bi8X5S8SfpaOGVaJfTMxXqCj+Y9SrPN4vrL05ooRFvoBYxl3cqo0vZ6Yjg3D0w7rpluWVBobgUQgbWbYGWhI6zt6vOKUA4twnKjSfwSBqQn3fAjVGSBxGi9gIcEA7+hPlTZImOu8A5NuDl46Sx8QWP3ZFrdGraHTzPTPyBrpn52DLGWRUahFDYYY4S3yE2sh7Yw5wD04bv7BLBOq5KwVXdziigaWnRzrXB7aYTUic+WIKYQZ1L62QCrGDyDBfY1p/hlAnCjvCex1C2D2c7efqiPnRHg8K4bu4G5eSj+tIt91Rz1s512TXkT4YvVihyrQd1RKwwPldboE5bqBp+y28Tiy0NhUmSNduJSm0DsSB4OYziHX4UJKPmektVO8zmtQI8ZskosfXS3WYYe9ILC0dLqwgwoi2k4tiyAaNAC6G23jt5Wt0AMSvM0wWTz5ejdvF6rWbRELhn3HJZvzMAMpRUUwdnj4xGUsWlaT3oNGZN6OlyYF0tR9jOKwOOeDkxOfsqT/Ep1sGrere5NiUIJD7mmh4E9AgbRhzbh1s0dou2sJF+B1HL7mV+bi37wqvHIO7g81OUVh65S+tN1fI1JQGFFi8x2ylyTugr7tEnk9jqMgsochAbGi3D68XAIFlxUPyWFtX8vD2BIqeLAOwRC/e4MBePFj3tpP9cgg5hzgxcHPCglBKxNy5yry+9LKaLdrKhMjkbHeUHFJR7MZzdY7Kl5MCTgCizY6qFFzZ7KqoB68+sNwgnCUQDo09lvdOXggp7y4O78rE1245Ta3LMkX2CwRnALUCPDwJRF3akXXmubyoRIkCcFQfJAMCkMyb2EjBig49lnrqz5F9h2ziGEamtVi7FW1V66HgkXGuFvYa47nKskhrpbSdQUN2va0aazVgAsBs4qlVszy3V5ca1Mxo07qruo+k6U4Lrt5bXwOgDVe93jdocs28xrvfreJlC2k6PURuCnAnqOKBNTs4jrRcY757lXMkEVXOxfIkajaYgb7KxPUJsIthZy0D0BYZFlxiyKQWtsylQuQq1ou2CLulM+FW5xah29dhjvczhXVkCilYBFkYP9V18Zth453yCCXZMFaiRXZYo7pTo7rY07CzlJDhOmtbAXIiLIJyQimcr1EHHDafi8TGwe1dc0gPtaRHA7ghu1NqU81Fd4gKMduVJMzNmEljiLt+f/dWy8e6KImsUswNFqiS0B4lX1eaWDKmmq86EuI2M3dD+gkhAqSqIgmQNRFmP65mDhXTigtZaZ7KfMRfTRSXy+I18UmWnpHnHp1yJOrLHIOc0SQgESYcYhahNAzIgYXfu6EUjYQVn4DndQ89JG0FObT4A3RmhTcSzYMCMVF2Jsl5oU/doT2NM+HGopTGnrxlwRDombxuT41VHjzu/EILagTOF3+MbFhWaMs2+7N1H6rGzFTuuUwoglk5BsmNC43RkI0ov1KMyjMfYx7H56FCvJgZAAM+PK8Sh3AXTfWWEeRaF9at9IinsKMughfIrhUKwlTj44q2XUt3tHMXXcAycwHp49O2YYdlI0M5z6yjJElvXuXtWFUFdxhjKrsTU2OzQgEg05vpEVxLpUDFMjsQku0jbV0aFrYX0YOHzpm8+OLDH1IRTjnS7hecauMil3sKDC3Pt43zSbRU2zqztPa6mVnAdgS5JecYaodY9x1ZRDrvsl0tyjLGipuZy39bAfZKs+x7cHjBzDk+LXpYMt/ndjYo31ht1xfbMIpaK8IZaK3PS8uVasbciO5XB1cnq8TKg8Jw2jFrGvRUAGKxykVGXDn4MnqcoDNbOnxOXH53yGOXpAVbviZDIjDegV3yixgZD/GJa5wT1s+hO1AypmQD8iBsuL+5ErmVn+iE+uGS4aadEwB8ETGAksC1oJ44wJSJ2uW05QFydjQBRKZaEKhPzPhyb+TrvwnaPzX0ZDRzKzh3DCknxTG4idvzZwQWyTWI1LjjTOo5Z5WY45ubq1BrDTAijiA47PLHlvMEEpOLoZRtoj4dSRe6DkwNAZDschAeCp164nGLGwqSu6OIrD/Mlik0XLE70tEjxeKLNyIL0kfWl12w4kzzuqJmAEogT0lNPZh53jFjJRMymD3Se4T2ohiEgH+464UqqGeBpcV+HSwmszTUlstMoMUXgDlxSQ2aCXMvx5gCKnd4k+8qFUe3s1Ik+AV6KVm09QbOi3PbZO/lYFHUqKfmXOFkewB6ajVFFl/rSiBxFIlNW1rh/nlo5Y6wUV0t2CUotM455UYkL9BxqEe9dXd+2ldA4xUDpUAF8o9BjRD0hvatsdrWLQyLf5nnfZNqEYUIlNHSkUfG8tF55OYhzZV+nG3MQQUxSbkqa9q0oXJvTMSoWj6fREIHpupXowyN7/Adybjo4nQNgpTQznG8NTiqyOI/pBm16t7Bxq8/kVt7u3QarN6fv6Ix+4qVCe7gaq8H9lOXa8FhDVxaVR6F67VMwblbcjrN0Ot1zID6IIpJnesBFzsT6wAXGBH61rIWrj0iUYsyvTRveuQBSsO189H1XrlNn9xT8MZOQAmS26csbxdfmonWWsjv1jFK3W5/dG+POOvQzDoANy1oMOJlwjZmtXzBn/5bBeMvzC8Ws59t5pVOaXoEuZsj1RQL2tgBFGTmtSdSPXsdbzzQY1JuxMy1THH3v0QBG3zoYfwMtGbMGZzr4ieVG5+bcnR/Ac+xJQeFuWupdY20KFLsfOhqjoAUm+TisYTCihp4abGDQHsIUpQtqtlxbVPq2evCV5IE+K8/ocyr3e3fFmRq9Yrk60HTKNJIH0Krj+xFUnrjb6PJ7NbuCs9taeUGmEYBDJIiLlqtA2rnCIhLoZ+2i7w/iSizxRJ3B7qIjwGnFzmriPy8kUZ7T0sanY9iGRuyikHhll+Pi+CtoN2j4iG/u3JESQmUB60yDX2Ao/ITj1XqobUOJJqgAJ41Cp4vXxYNInvnbNQBszdNSRFDER1QynoeoTeNOyomYaRF+OF6ick9gIaLE38omu7nbGWGdbAUeK+J5wtkviMsJZEmSYUObA/i7POu3lCvE+2QgnNjeIbFBnCtOCZwbIyfQB2TUDe/U7JygIj/jvQhrHf0YbrxYYgGiUuGAPdWRRUvRAXvK9KxESo7JhjnmUko3pK5FGrI5GYs0AXM1+9ImgvMVOT0cq3Ehw2jPpOAGWSubkRQccwPXZPmp1u+4KvbKSWco3rwShU2Im5Ezm3BMWgzs0iKj7RebwzGxhmMZCs6jEUKigj/9k3awOiuwx3aUJacDgwB3eG9/4kFd66PPCEJ5crw9TdWrG3b38rJSRWcmsRfG8uZr+1W5j7Rxb4FnV2ny1THHosFbmwcMC4noZbnbaqchAHAKkLwOiSAMFispn4UXYdKu4eJ5DsndiCWmr9q0dYRt60qZNOAFte4eJFc6oZ2Z7naWQIFq00csGrnej6JuixU36Uf3PTFLgkuzVcT05KcuFF/ueM/n4HzKEC3dh40LXHKybAhit0ywN5e4oCpv91feBjKKGl7/Cwd2zh5eJLlh7m5wSQw84eUgQFMyjhwz7PUEdMpJrYi61dCIOM88dWX8ID/77nxPy8qfXNwaj1EuUOghBz2kFXFjbrSby5d576mtDT0zmoo6j8IZnwWWm3vMCxSLg9MO+XWtNc+AALwDIsAnRqjjiJsEDdjWTReonhk50dQWR8WEapsBPitv1nibwuJgVsIpJH1ShWpEk6NbNfgEOd1T/8mEvI5S0N1rbnxCiNex45CLbGCdQsXV3tpZ+phIE9S6EOj9oxwjgzlne8ChsIjRNEzA5tRhg4xXZmSS9iwdR3JkAvefroJs9k1Cpmh4NFd1KE+UVXnKktWMs8zCUEZTYQflgNvEmTWx9pgc7756O28mj4vxdNGK/Bi5LuLe6LOTrL5rTvhRYPVzhVAfCWvdmqtTCEHuOQYDmq2OCdNyTTUc5WGfW71YIfI5s6owk2eq1ATM2Xzv4B8mDM7clj5B/MF5F8da9vA6EJb/xM31rKmcIDcP00j4DVivLMzXJL4oBv9cNIYwRJ++RkZ8PfgzhhOPMbrFzNN95KPh4BebMkzFnpLBgNscT/0EPwxqs5oA6nZpc/VU4MmByT0pTw8TrYHX0/ghQWbVJTW0aTIEsuyQuqBZdyGHPjmOIgqtnq/Was63bRniW7wRC1SYkzQeMw3susHjwM8o3SOPSLZghiPe2p/bBtX8c7QGYHG0XTtaM+zdrvEiQMGGTu0V0lwXSy9pE6F23pdjjUaPWZGbgulOfSQTeSCetMtcXDpRR1WuJemR8arHPcGUdR/b4Sb64TgkmpYVCS/EjibkzSVbcTzI0v4phyNuQ7Y8q5o23QUg7uKlx+Wd7SsF31oLswEQ97CIyKGBkCo1bbuqJ6A+1y8X+mbtzBqCx9SsXOaLcOGkW4ArCnF+DEaP6J6Q8s1S7VBo3hHq1irPOcx1GfGVcFp44SiHwfFcYGbzpKTFGgTTkEywGMsffTdZT/BUdq75eOi+Ls1004OP2530RlywrkJxMUUAvFrhZN4HhRKCYKp6j+odB44kxNr1fB6drn1Q+JFWKGixM8GRu4YpYsp2cIjRjzK59KUCUcSIyUszEMt62CranIEAjVreTfGeSoKdEkrvz2ucSJANmSzqgJaaUCDs48VtRPPmOj8M2LVglfBzYD85PnW9OEmOgdfb/ZhmaxjHxS7TTymJipmf3rzp6U0WM4arQTTp5NJ7KabpY4FmOlj3JsRZIU9LYOstEF9ofXekp2teI7XaTuPY7GtY3bqFGvXlTBmyL9zPfBy4Ii1P0vS8sLewTs6THMu3M+Hkl6XYVS3KsOdynbHc31cdlsKm98RLgmo0epEddSCAgj6pOtP6wtAWGQFcaLlYMaUv541FG+t5ng9NbAiFtNZwFgx7mXPv4E5c40kOmoKei26tVFUmEQtJ2ebyHKtTDM+l3cckl7vTcDTG0ST2h4ydxiSpdhqKr/f7qEUVO++6AScP3rt0uzRWmoD0NtnqVXQC7o8gbkPhDJ6gG2VdJC1DJgdG7nk0YirVLZswAY47yCEvbeMFXEKm1cKCJHP9NhjOxKtdEvayXZxclA7K7tQ95jthdZc0WealnXdt284al3Xk2NrblayOIkxF1cXjUGXcCn92i1ZV0gmPdadX8XPG+YKiDBRa2Q05x7f2hmE2zG+55LLCSX4SIhNIImXNEF/B9kAw54eJU3jbie4Vf9T38/PRXQae4gIZCcCnJShAOV3KBwHdizihyKMdDzmG1UbrJGV3tyzqGMgdWqbg9V7fV3BBGTEW0TV41GtIGZoxFzF8pCQc1FQKbvYAVCUaekbtIQeBNcsQU81ECVrO6FpfBsT7nIDg7VFSmUvBdpqGmuSeD+qnGDPkHs5AH15P0eTqegp69cLThD4akzSg7baNdWmBMBp42yU+4yFZZGTaUEOKuvOeBDp3TjAkfxC4SlzHtnIujzoL3Zq9OKcJuOzobJ4mnINp24W4Z1H1+jFkG0K9LDuv6aNO8CmvqoZxC0Xt0voXNLLGU9BFQ1lY6KryiDkQnVasukF6YVJO2aw6NbBGj+a+JosR2YKck0Fp0ff0TkBFqgWtdRXNMD8vPXaeRIbZO4Xl7giv16gtkcv2oqHnDICMnp9FyoekEV5PPCTwl2Ea5vgxkNQgFo7W5MOVhtMB7kpSX+4ilKQcJPkIoT9awE8go3OAOjuRJzq8y1t0h2ZJ7IMscTzScvnavcGTvpj705JuZ4S7Gh61IIuzQZzEIFwQxzVSq9utVA4XaAuqFE+qoExCUwMguiNSdQrWGFyvbdUaAa/KSM+k9Q4KGjGiAjzRlI3yVxinzhyQXkAVQVll3totDlA4766ZB52geU1s8fFYVKs9YzC3b6Z/1OgwtKdyznUdpxKpRQcyC8csiLIdgGwxOggS7Pt7NVW122e6T5TGIpg+Cgief8XXBhw0l0c33SLzfSVHA/YXwmqD9BR6lQlnW8aWxGVMZac9Q+pSSvieCoIWn06FFekcxlPhbAqualZEjz38cELnMKFQ/JbYfHiLMoJVc/C5y/1tia9yOhxsc9/LXsrusBDnubjz4SliJhVA2huMnO6My4NEVrobOSBS0da8LCBX1a4ib4wM8YzVeyDAvDDCyY75mrrmPJXQyTOIw7iumnN/JQTUDyTQv1BcDANBpuoFGNb1eVQJ4ETD0Ez0AYD4ZA3vLSNGaAyIfldtwk2EKSD3EA3miE6t8Avi4HqTXBEmm6rFiD0r7G5CKaeBjQLw+cTFoEQmaMrtV+aIFu4GErU8L3RY7TYqLto82nAZZu7icfbRtos0DwQwtah+WYubC8/D0TnZ1uvuTSA8YsdYngM7eTMLtgGbCkNYQ3HkcN4YyDBcl4dVXLtc9eJxmkxs9k435szdc3QRJq0dLrDNJcR+uy06pZvEAujVwQ0zYEVuKq7eZp7dni6K1dJQSWa8jcDDKBPJbG1/XeOKnolIa9Npv40JSGin+5kY4NRZS1dWY81uCJtS6LkVU1rRZB92Aaa/I+sjO4e+RpylHgCZu74HWMTyBHwveenuQle3Cs9QorFrxehzP7jTGWt0VuE7f1t9gbOIVdj9KlsdAXSc46uroUdHBu/FuJBp4JSUCA9EDlejYaSJegwc157Jz7UnG6J+XkmaTfJCbLhI0/vzJlEV5l0GlM+J5kgEGtMejZdpax6t5QFE1+mZWCYFkrdNpVbi3Lg0Tf/xy9f393z/4StxP16lfL3r9d/2ytnH22Hd49i7jY7N/+XL603Jn9/3+vk/M+Rfv34Zo+Iw4+P9ualess9Xzz7envv2qeDbb99Afok+P36Twetl5W3+5ZXAOchev8rpy4839V+/euqXJZ86jk9h183HxaA/Pr+/r15MzcuWz1c2P+z5Cfny1/8Xc2K8QdNKAAA= -->
