---
name: "rar-kody-w-install-rappter-distro"
description: "Installs the full rappter-distro over a bare kernel by fetching files from raw.githubusercontent.com with per-file sha256 verification."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/install_rappter_distro_agent", "rar_sha256": "91f2128926d613cc537ff4b3e5327a35b0268d0eabd548a828d5009af956b803", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.2", "author": "Kody Wildfeuer", "tags": ["installer", "distro", "rappter", "bootstrap", "organism"]}
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

<!-- rci-capsule:v1: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 -->
