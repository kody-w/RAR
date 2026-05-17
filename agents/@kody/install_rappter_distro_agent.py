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
    "name": "@kody/install_rappter_distro_agent",
    "version": "1.0.0",
    "display_name": "Install Rappter Distro",
    "description": (
        "Single-file installer that pulls the full rappter-distro "
        "(organs, senses, lib/, rich UI, @rappter agents) from "
        "raw.githubusercontent.com via MANIFEST.json with sha256 "
        "verification per file. Refuses to touch the three sacred "
        "kernel files."
    ),
    "author": "Kody Wildfeuer",
    "tags": ["installer", "distro", "rappter", "bootstrap", "organism"],
    "category": "pipeline",
    "quality_tier": "community",
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