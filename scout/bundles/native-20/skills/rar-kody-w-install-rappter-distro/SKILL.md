---
name: "rar-kody-w-install-rappter-distro"
description: "Installs the full rappter-distro over a bare kernel by fetching files from raw.githubusercontent.com with per-file sha256 verification."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/install_rappter_distro_agent", "rar_sha256": "15ee1708f83dc55022bdf74d625b6b443d59f73371cd2f4c68100651c8f001d2", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.2", "author": "Kody Wildfeuer", "tags": ["installer", "distro", "rappter", "bootstrap", "organism"]}
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
