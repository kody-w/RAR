#!/usr/bin/env python3
from __future__ import annotations
"""
Registry Builder — Auto-generates registry.json from __manifest__ dicts in agent files.

Run manually:   python build_registry.py
Or via CI:      Triggered on every push by .github/workflows/build-registry.yml

Scans agents/@publisher/ for .py and .py.card files with __manifest__ dicts and builds:
- registry.json (full index for programmatic access)
- Validates all manifests against schema
- Reports errors for malformed agents

Also scans swarms/@publisher/ for converged multi-agent singletons with __swarm__ dicts,
and promotes existing agent stacks to downloadable swarm bundles.

Supports three file formats:
- slug.py      — bare agent (code + manifest)
- slug.py.card — complete agent+card package (code + manifest + __card__ shell)
- slug.py.stub — gated agent (manifest + __source__ pointer, no code).
                 The actual agent.py lives in a private repo; the brainstem
                 resolves the pointer at install time using the user's own
                 GitHub credentials. Public RAR lists the entry, the user's
                 private repo gates the bytes.
"""

import ast
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timezone

AGENTS_DIR = Path("agents")
SWARMS_DIR = Path("swarms")
REGISTRY_FILE = Path("registry.json")
HOLO_CARDS_FILE = Path("cards/holo_cards.json")
LIFECYCLE_FILE = Path("state/agent_lifecycle.json")
RECEIPTS_DIR = Path("state/receipts")
RECEIPT_SCHEMA = "rar-receipt/1.0"
LIFECYCLE_SCHEMA = "rar-agent-lifecycle/1.0"

# Cache holo card slugs and per-card content for _has_card / _card_sha256 lookups
_holo_data = None
def _holo_cards():
    global _holo_data
    if _holo_data is None:
        try:
            data = json.loads(HOLO_CARDS_FILE.read_text(encoding="utf-8"))
            _holo_data = data if isinstance(data, dict) else {}
        except (FileNotFoundError, json.JSONDecodeError):
            _holo_data = {}
    return _holo_data

def _has_holo_card(agent_name):
    cards = _holo_cards()
    return agent_name in cards or agent_name.replace('_', '-') in cards or agent_name.replace('-', '_') in cards

def _holo_card_for(agent_name):
    """Return the holo card dict for `agent_name`, or None. Tolerates the
    same dash/underscore variants as _has_holo_card."""
    cards = _holo_cards()
    for key in (agent_name, agent_name.replace('_', '-'), agent_name.replace('-', '_')):
        if key in cards:
            return cards[key]
    return None
REQUIRED_MANIFEST_FIELDS = [
    "schema", "name", "version", "display_name",
    "description", "author", "tags", "category"
]


def install_filename(name: str) -> str:
    """Return a flat, collision-safe filename derived from @publisher/slug."""
    safe = re.sub(r"[^A-Za-z0-9_]+", "_", name.lstrip("@")).strip("_").lower()
    if not safe.endswith("_agent"):
        safe += "_agent"
    return f"rar_{safe}.py"


def extract_manifest(py_path: Path) -> dict:
    """Extract __manifest__ dict from a Python file using AST parsing."""
    try:
        source = py_path.read_text(encoding="utf-8")
        tree = ast.parse(source)
        # ast.parse is not the same bar as import. Misplaced __future__
        # imports (and a few other compile-time-only errors) parse cleanly
        # and then explode the moment a brainstem loads the agent, so the
        # registry must clear the stricter gate before publishing.
        compile(source, str(py_path), "exec")
    except SyntaxError as e:
        print(f"  ⚠ Syntax error in {py_path}: {e}")
        return None

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__manifest__":
                    try:
                        return ast.literal_eval(node.value)
                    except (ValueError, TypeError) as e:
                        print(f"  ⚠ Cannot parse __manifest__ in {py_path}: {e}")
                        return None
    return None


def validate_manifest(py_path: Path, manifest: dict) -> list:
    """Validate a manifest and return list of errors."""
    errors = []
    
    for field in REQUIRED_MANIFEST_FIELDS:
        if field not in manifest:
            errors.append(f"Missing required field: {field}")
    
    name = manifest.get("name", "")
    if not name.startswith("@") or "/" not in name:
        errors.append(f"Invalid name format '{name}' — must be @publisher/slug")
    
    version = manifest.get("version", "")
    parts = version.split(".")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        errors.append(f"Invalid version '{version}' — must be semver (e.g., 1.0.0)")
    
    if not isinstance(manifest.get("tags", []), list):
        errors.append("tags must be a list")
    
    return errors


def _runtime_string(node: ast.AST, manifest: dict, known: dict) -> str | None:
    """Resolve the small set of string expressions used for agent names."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Name):
        return known.get(node.id)
    if (
        isinstance(node, ast.Attribute)
        and isinstance(node.value, ast.Name)
        and node.value.id == "self"
    ):
        return known.get(f"self.{node.attr}")
    if (
        isinstance(node, ast.Subscript)
        and isinstance(node.value, ast.Name)
        and node.value.id == "__manifest__"
        and isinstance(node.slice, ast.Constant)
    ):
        value = manifest.get(node.slice.value)
        return value if isinstance(value, str) else None
    return None


def _metadata_name(node: ast.AST, manifest: dict, known: dict) -> str | None:
    if not isinstance(node, ast.Dict):
        return None
    for key_node, value_node in zip(node.keys, node.values):
        if isinstance(key_node, ast.Constant) and key_node.value == "name":
            return _runtime_string(value_node, manifest, known)
    return None


def validate_runtime_contract(py_path: Path, manifest: dict) -> list[str]:
    """AST-check every public top-level agent class without importing code."""
    try:
        tree = ast.parse(py_path.read_text(encoding="utf-8"))
    except (OSError, SyntaxError) as exc:
        return [f"Cannot inspect runtime contract: {exc}"]

    errors = []
    agent_classes = [
        node for node in tree.body
        if isinstance(node, ast.ClassDef)
        and node.name != "BasicAgent"
        and not node.name.startswith("_")
        and any(
            isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef))
            and member.name == "perform"
            for member in node.body
        )
    ]

    for agent_class in agent_classes:
        known = {}
        runtime_names = []
        metadata_names = []

        def remember_assignment(target: ast.AST, value_node: ast.AST):
            value = _runtime_string(value_node, manifest, known)
            if isinstance(target, ast.Name) and value is not None:
                known[target.id] = value
                if target.id == "name":
                    runtime_names.append(value)
            elif (
                isinstance(target, ast.Attribute)
                and isinstance(target.value, ast.Name)
                and target.value.id == "self"
                and value is not None
            ):
                known[f"self.{target.attr}"] = value
                if target.attr == "name":
                    runtime_names.append(value)

            is_metadata = (
                isinstance(target, ast.Name) and target.id == "metadata"
            ) or (
                isinstance(target, ast.Attribute)
                and isinstance(target.value, ast.Name)
                and target.value.id == "self"
                and target.attr == "metadata"
            )
            if is_metadata:
                metadata_name = _metadata_name(value_node, manifest, known)
                if metadata_name is not None:
                    metadata_names.append(metadata_name)

        for member in agent_class.body:
            if isinstance(member, ast.Assign):
                for target in member.targets:
                    remember_assignment(target, member.value)
            if not (
                isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef))
                and member.name == "__init__"
            ):
                continue
            for inner in ast.walk(member):
                if isinstance(inner, ast.Assign):
                    for target in inner.targets:
                        remember_assignment(target, inner.value)
                if not (
                    isinstance(inner, ast.Call)
                    and isinstance(inner.func, ast.Attribute)
                    and inner.func.attr == "__init__"
                ):
                    continue
                name_arg = inner.args[0] if inner.args else next(
                    (item.value for item in inner.keywords if item.arg == "name"),
                    None,
                )
                if name_arg is not None:
                    value = _runtime_string(name_arg, manifest, known)
                    if value is not None:
                        runtime_names.append(value)

        runtime_names = list(dict.fromkeys(runtime_names))
        metadata_names = list(dict.fromkeys(metadata_names))
        if not runtime_names:
            errors.append(
                f"{agent_class.name}: runtime name must be statically resolvable"
            )
            continue
        for runtime_name in runtime_names:
            if not re.fullmatch(r"[A-Za-z0-9_-]+", runtime_name):
                errors.append(
                    f"{agent_class.name}: runtime name {runtime_name!r} must match "
                    "^[A-Za-z0-9_-]+$"
                )
        for metadata_name in metadata_names:
            if metadata_name not in runtime_names:
                errors.append(
                    f"{agent_class.name}: metadata name {metadata_name!r} does not "
                    f"match runtime name(s) {runtime_names!r}"
                )
    return errors


def extract_card(py_path: Path) -> dict:
    """Extract __card__ dict from a .py.card file using AST parsing."""
    try:
        source = py_path.read_text(encoding="utf-8")
        tree = ast.parse(source)
    except SyntaxError:
        return None

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__card__":
                    try:
                        return ast.literal_eval(node.value)
                    except (ValueError, TypeError):
                        return None
    return None


def extract_swarm(py_path: Path) -> dict:
    """Extract __swarm__ dict from a Python file using AST parsing."""
    try:
        source = py_path.read_text(encoding="utf-8")
        tree = ast.parse(source)
    except SyntaxError:
        return None

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__swarm__":
                    try:
                        return ast.literal_eval(node.value)
                    except (ValueError, TypeError):
                        return None
    return None


REQUIRED_SWARM_FIELDS = [
    "schema", "id", "display_name", "summary", "category", "publisher", "produced_by"
]


def validate_swarm(py_path: Path, swarm: dict) -> list:
    """Validate a __swarm__ dict and return list of errors."""
    errors = []
    for field in REQUIRED_SWARM_FIELDS:
        if field not in swarm:
            errors.append(f"Missing required __swarm__ field: {field}")
    if swarm.get("schema") != "rapp-swarm/1.0":
        errors.append(f"Invalid swarm schema: {swarm.get('schema')} (expected rapp-swarm/1.0)")
    pb = swarm.get("produced_by", {})
    if not isinstance(pb, dict) or "method" not in pb:
        errors.append("produced_by must be a dict with at least 'method'")
    return errors


REQUIRED_SOURCE_FIELDS = ["schema", "type"]
SUPPORTED_SOURCE_TYPES = {"github_private", "github_public"}


def extract_source(py_path: Path) -> dict:
    """Extract __source__ dict from a .py.stub file via AST literal_eval."""
    try:
        source = py_path.read_text(encoding="utf-8")
        tree = ast.parse(source)
    except SyntaxError as e:
        print(f"  ⚠ Syntax error in {py_path}: {e}")
        return None

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__source__":
                    try:
                        return ast.literal_eval(node.value)
                    except (ValueError, TypeError) as e:
                        print(f"  ⚠ Cannot parse __source__ in {py_path}: {e}")
                        return None
    return None


def validate_source(py_path: Path, src: dict) -> list:
    """Validate a stub's __source__ pointer."""
    errors = []
    if not isinstance(src, dict):
        return [f"{py_path}: __source__ must be a dict"]
    for field in REQUIRED_SOURCE_FIELDS:
        if field not in src:
            errors.append(f"Missing __source__ field: {field}")
    if src.get("schema") != "rapp-source/1.0":
        errors.append(f"Invalid __source__ schema: {src.get('schema')} (expected rapp-source/1.0)")
    stype = src.get("type")
    if stype not in SUPPORTED_SOURCE_TYPES:
        errors.append(
            f"Unsupported __source__ type: {stype} "
            f"(supported: {sorted(SUPPORTED_SOURCE_TYPES)})"
        )
    if stype in ("github_private", "github_public"):
        for field in ("repo", "path"):
            if field not in src:
                errors.append(f"github_* source missing required field: {field}")
        repo = src.get("repo", "")
        if repo and "/" not in repo:
            errors.append(f"Invalid repo '{repo}' — must be owner/name")
    return errors


def validate_stub_purity(py_path: Path) -> list:
    """A .py.stub file may contain only a docstring and the __manifest__
    and __source__ assignments. Any other top-level statement (function,
    class, import, executable code) is rejected — stubs are pure metadata."""
    try:
        tree = ast.parse(py_path.read_text(encoding="utf-8"))
    except SyntaxError as e:
        return [f"Syntax error: {e}"]

    errors = []
    allowed_names = {"__manifest__", "__source__"}
    for i, node in enumerate(tree.body):
        # Allow module docstring (first Expr with a string constant)
        if (i == 0
                and isinstance(node, ast.Expr)
                and isinstance(node.value, ast.Constant)
                and isinstance(node.value.value, str)):
            continue
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            tgt = node.targets[0]
            if isinstance(tgt, ast.Name) and tgt.id in allowed_names:
                continue
        errors.append(
            f"stub contains non-metadata statement at line {node.lineno} — "
            f"stubs may contain only a docstring, __manifest__, and __source__"
        )
    return errors


# Per-file waivers from DANGEROUS_PATTERNS. Deliberately EMPTY.
#
# This list used to name ten agents that "legitimately need eval / exec, which
# stay banned for everyone else", plus some that need subprocess. Both premises
# are now false: subprocess was removed from DANGEROUS_PATTERNS, and eval/exec/
# __import__/compile moved to CAPABILITY_PATTERNS, where they are allowed for
# EVERY agent and merely tagged as `_capabilities`.
#
# So the waiver stopped excusing what it was written for and started excusing
# the only three rules left — os.system(), suspicious file access, and
# HARDCODED SECRETS — for ten files, none of which ever asked for that. A
# secret committed in an allowlisted agent would have shipped unflagged.
#
# Emptying it costs nothing: verified that zero allowlisted files trip any
# current DANGEROUS_PATTERN, so every one of them passes on its own merits.
# The mechanism is kept so a future, genuinely-justified waiver has somewhere
# to go — but see test_security_allowlist_waives_nothing_dangerous: a file
# added here that actually trips a pattern will fail the build.
SECURITY_ALLOWLIST: set = set()


def _security_allowlisted(path: Path) -> bool:
    return path.as_posix() in SECURITY_ALLOWLIST

# Patterns that should never appear in agent code (supply chain defense).
# Subprocess is intentionally NOT here — wrapping external CLIs is a normal
# integration pattern. See SECURITY_ALLOWLIST comment above.
DANGEROUS_PATTERNS = [
    (r'\bos\.system\s*\(', "os.system() is forbidden — use subprocess and declare in requires_env"),
    (r'\bopen\s*\(.*(\/etc|\/proc|\.env|\.ssh|passwd)', "suspicious file access pattern"),
    (r'(api[_-]?key|secret|password|token)\s*=\s*["\'][^"\']{8,}', "possible hardcoded secret"),
]

# Dynamic-code capabilities. These used to be hard-rejected, which broke
# genuinely useful agents over a blunt rule. Now they are ALLOWED and TAGGED:
# an agent that uses them gets its capability recorded in the registry entry
# (`_capabilities`), so consumers who want to restrict dynamic code can simply
# FILTER on the tag instead of the registry refusing to build. exec/eval are
# legitimate for meta-programming, self-verification against a fetched
# reference, sandboxed interpreters, etc. — the registry's job is to surface
# the capability, not to forbid it.
CAPABILITY_PATTERNS = [
    (r'\bexec\s*\(', "exec"),
    (r'\beval\s*\(', "eval"),
    (r'\b__import__\s*\(', "dynamic_import"),
    (r'\bcompile\s*\(.*["\']exec["\']', "compile_exec"),
]


def scan_capabilities(py_path: Path) -> list:
    """Return sorted dynamic-code capability tags present in the file (e.g.
    ['eval', 'exec']). Empty list if none. Informational — never fatal."""
    source = py_path.read_text(encoding="utf-8")
    tags = {tag for pattern, tag in CAPABILITY_PATTERNS if re.search(pattern, source)}
    return sorted(tags)


def extract_stack_info(file_path: Path) -> tuple:
    """Extract stack name and vertical from file path.
    Pattern: agents/@publisher/VERTICAL_stacks/NAME_stack/agent.py
    Maps directly to the AI Agent Templates stack structure —
    each stack becomes a deck, each agent.py becomes a card.
    Returns (stack_name, vertical) or (None, None) if not in a stack.
    """
    parts = file_path.parts
    for i, part in enumerate(parts):
        if part.endswith('_stacks') and i + 1 < len(parts) and parts[i + 1].endswith('_stack'):
            vertical = part[:-7]   # strip '_stacks'
            stack = parts[i + 1][:-6]  # strip '_stack'
            return stack, vertical
    return None, None


def canonical_file_bytes(file_path: Path) -> bytes:
    """Return repository-canonical bytes regardless of checkout line endings."""
    return file_path.read_bytes().replace(b"\r\n", b"\n")


def compute_sha256(file_path: Path) -> str:
    """Compute SHA256 over the LF-normalized bytes GitHub serves."""
    return hashlib.sha256(canonical_file_bytes(file_path)).hexdigest()


def registry_path(file_path: Path) -> str:
    """Serialize registry paths with URL-compatible separators on every OS."""
    return file_path.as_posix()


def superseded_legacy_agent_path(
    file_path: Path,
    canonical_names: dict[Path, str],
    legacy_name: str | None,
) -> bool:
    if (
        file_path.suffix != ".py"
        or file_path.name.endswith("_agent.py")
    ):
        return False
    canonical = file_path.with_name(
        f"{file_path.stem}_agent.py"
    )
    canonical_name = canonical_names.get(canonical)
    normalized_legacy_name = (
        legacy_name
        if legacy_name and legacy_name.endswith("_agent")
        else f"{legacy_name}_agent"
        if legacy_name
        else None
    )
    return bool(
        canonical_name
        and (
            legacy_name is None
            or legacy_name == canonical_name
            or normalized_legacy_name == canonical_name
        )
    )


def _seed_hash(s: str) -> int:
    h = 0
    for c in s:
        h = ((h << 5) - h + ord(c)) & 0xFFFFFFFF
    return h


def compute_seed(name: str, category: str, tier: str, tags: list, deps: list) -> int:
    """Forge a seed FROM agent data. Same algorithm as rapp_sdk.forge_seed.
    The seed IS the card's DNA — encodes identity, types, tier, tag/dep hints.
    Anyone with this number reconstructs the exact card. No registry needed.
    This protocol is permanent."""
    # Import type derivation from SDK to stay in sync
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).parent))
    from rapp_sdk import forge_seed as _forge
    return _forge(name, category, tier, tags, deps)


def preserved_seed_aliases(previous: dict, current_seed: int) -> list[int]:
    aliases = []
    previous_aliases = previous.get("_seed_aliases", [])
    if not isinstance(previous_aliases, list):
        previous_aliases = []
    for value in previous_aliases:
        if (
            isinstance(value, int)
            and value != current_seed
            and value not in aliases
        ):
            aliases.append(value)
    previous_seed = previous.get("_seed")
    if (
        isinstance(previous_seed, int)
        and previous_seed != current_seed
        and previous_seed not in aliases
    ):
        aliases.append(previous_seed)
    return aliases


def scan_security(py_path: Path) -> list:
    """Static security scan — returns list of warnings."""
    warnings = []
    source = py_path.read_text(encoding="utf-8")
    for pattern, message in DANGEROUS_PATTERNS:
        if re.search(pattern, source):
            warnings.append(f"{py_path}: {message}")
    return warnings


def check_version_immutability(name: str, version: str, sha256: str, file_path: str) -> str | None:
    """If a previous registry exists, verify version wasn't silently changed."""
    if not REGISTRY_FILE.exists():
        return None
    try:
        prev = json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))
        for agent in prev.get("agents", []):
            if (agent.get("name") == name
                    and agent.get("version") == version
                    and agent.get("_file") == file_path):
                prev_hash = agent.get("_sha256")
                if prev_hash and prev_hash != sha256:
                    return (f"Version {version} already published with different content "
                            f"(hash mismatch). Bump the version number.")
    except (json.JSONDecodeError, KeyError):
        pass
    return None


# ── Git history, read once instead of per file ────────────────────────────
#
# These three facts (first-commit date, first-commit sha, latest-commit sha)
# used to cost one `git log` subprocess EACH, per agent — 3n spawns, which at
# 278 agents is 834 processes and a ~2min build that blew the pipeline test's
# 60s budget. Aggregation only makes n grow, so this is read in a single pass:
# one `git log --name-status` walk of the whole history builds the map, and
# every lookup afterwards is a dict hit.
#
# Semantics are preserved exactly: history is walked newest-first, so the LAST
# add seen for a path is its earliest ("A" status, matching --diff-filter=A),
# and the FIRST commit touching a path is its latest.
_GIT_HISTORY: dict[str, dict] | None = None


def _load_git_history() -> dict[str, dict]:
    global _GIT_HISTORY
    if _GIT_HISTORY is not None:
        return _GIT_HISTORY
    history: dict[str, dict] = {}
    try:
        result = subprocess.run(
            ["git", "log", "--name-status", "--format=%x00%H%x00%cI", "--no-renames"],
            capture_output=True, text=True, timeout=180,
        )
        sha = date = None
        for line in result.stdout.splitlines():
            if line.startswith("\x00"):
                _, sha, date = line.split("\x00", 2)
                continue
            if not line.strip() or sha is None:
                continue
            parts = line.split("\t")
            if len(parts) < 2:
                continue
            status, path = parts[0], parts[-1]
            entry = history.setdefault(path, {})
            # Newest-first walk: the first sighting is the latest change.
            entry.setdefault("latest_sha", sha)
            if status.startswith("A"):
                # Overwritten as we go back in time, so it ends on the earliest add.
                entry["first_sha"] = sha
                entry["first_date"] = date
    except (FileNotFoundError, subprocess.TimeoutExpired, ValueError):
        history = {}
    _GIT_HISTORY = history
    return history


def _git_key(path: Path) -> str:
    """Repo-relative, forward-slashed — the form `git log --name-status` emits.

    Every path constant in this module is already CWD-relative (AGENTS_DIR =
    Path("agents")) and the build runs from the repo root, so the incoming path
    is repo-relative as given; it only needs POSIX separators to match git.
    """
    return Path(path).as_posix()


def _git_first_committed(path: Path):
    """Return the ISO date a file was first committed, or None if unavailable."""
    return _load_git_history().get(_git_key(path), {}).get("first_date")



def _git_first_commit_sha(path: Path):
    """Return the commit SHA where `path` first appeared. This is the
    permanent address for the file's initial publication — anyone can
    fetch the original bytes via raw.githubusercontent.com/<repo>/<sha>/<path>
    and verify against the recorded _sha256. Part of the poor-man's-
    blockchain provenance chain (commit graph IS the ledger)."""
    return _load_git_history().get(_git_key(path), {}).get("first_sha")



def _git_latest_commit_sha(path: Path):
    """Return the commit SHA of the most recent change to `path`. Together
    with _first_commit_sha this bounds the file's edit window — anyone
    can `git log <first>..<latest> -- <path>` to audit every change."""
    return _load_git_history().get(_git_key(path), {}).get("latest_sha")



def _card_content_sha256(card_data: dict) -> str:
    """Hash the card's content for that specific agent. Uses canonical
    JSON (sorted keys, no whitespace) so the hash is reproducible from
    any consumer. Lets consumers verify card integrity per-agent without
    trusting the aggregate holo_cards.json file."""
    canonical = json.dumps(card_data, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _lifecycle_metadata(
    *,
    name: str,
    version: str,
    digest: str,
    canonical_path: str,
    lifecycle_agents: dict,
    errors: list[str],
) -> dict:
    if name not in lifecycle_agents:
        return {"_lifecycle": "legacy_active"}

    lifecycle = lifecycle_agents[name]
    status = lifecycle.get("status")
    if status in {"deleted", "retired", "revoked"}:
        errors.append(
            f"{name}: active file exists while lifecycle status is {status}"
        )
        return {"_lifecycle": "invalid"}
    if status != "active":
        errors.append(f"{name}: unsupported lifecycle status {status!r}")
        return {"_lifecycle": "invalid"}
    if (
        lifecycle.get("sha256") != digest
        or lifecycle.get("version") != version
        or lifecycle.get("canonical_path") != canonical_path
    ):
        errors.append(f"{name}: lifecycle version or digest does not match file")
        return {"_lifecycle": "invalid"}

    receipt_id = str(lifecycle.get("latest_receipt", ""))
    if not receipt_id.startswith("rar_"):
        errors.append(f"{name}: active lifecycle has no RAR receipt")
        return {"_lifecycle": "invalid"}
    receipt_path = RECEIPTS_DIR / f"{receipt_id.removeprefix('rar_')}.json"
    try:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError) as exc:
        errors.append(f"{name}: receipt {receipt_id} is unavailable: {exc}")
        return {"_lifecycle": "invalid"}
    if (
        receipt.get("schema") != RECEIPT_SCHEMA
        or receipt.get("id") != receipt_id
        or receipt.get("agent") != name
        or receipt.get("version") != version
        or receipt.get("canonical_path") != canonical_path
        or receipt.get("quality_tier") != lifecycle.get("quality_tier")
        or str(receipt.get("controller", {}).get("github_id"))
        != str(lifecycle.get("owner_github_id"))
        or receipt.get("status") != "notarized"
        or receipt.get("artifact", {}).get("digest") != digest
    ):
        errors.append(f"{name}: receipt {receipt_id} does not match active file")
        return {"_lifecycle": "invalid"}
    return {
        "_lifecycle": "notarized",
        "_receipt": receipt_id,
        "_controller": {
            "github_id": lifecycle.get("owner_github_id"),
            "github_login": lifecycle.get("owner_github_login"),
        },
        "_provenance": {
            "issue": receipt.get("submission", {}).get("issue_number"),
            "submitted_by": receipt.get("submission", {}).get("github_login"),
            "accepted_by": receipt.get("acceptance", {}).get("github_login"),
            "checks": receipt.get("acceptance", {}).get("checks", []),
        },
    }


def _validated_tombstones(
    lifecycle_agents: dict,
    errors: list[str],
) -> list[dict]:
    tombstones = []
    action_by_status = {
        "deleted": "agent.delete",
        "retired": "agent.retire",
        "revoked": "agent.revoke",
    }
    for name, record in sorted(lifecycle_agents.items()):
        status = record.get("status")
        if status not in action_by_status:
            continue
        receipt_id = str(record.get("latest_receipt", ""))
        receipt_path = RECEIPTS_DIR / f"{receipt_id.removeprefix('rar_')}.json"
        try:
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError, OSError) as exc:
            errors.append(f"{name}: tombstone receipt is unavailable: {exc}")
            continue
        if (
            not receipt_id.startswith("rar_")
            or receipt.get("schema") != RECEIPT_SCHEMA
            or receipt.get("id") != receipt_id
            or receipt.get("agent") != name
            or receipt.get("version") != record.get("version")
            or receipt.get("canonical_path") != record.get("canonical_path")
            or receipt.get("quality_tier") != record.get("quality_tier")
            or str(receipt.get("controller", {}).get("github_id"))
            != str(record.get("owner_github_id"))
            or receipt.get("status") != status
            or receipt.get("action") != action_by_status[status]
            or receipt.get("artifact", {}).get("digest") != record.get("sha256")
        ):
            errors.append(f"{name}: tombstone receipt does not match lifecycle")
            continue
        tombstones.append({"agent": name, **record})
    return tombstones


SUPERSEDED_FILE = Path("state/superseded.json")


def _load_superseded() -> dict:
    """Withhold-from-lookup rules. Missing file = no rules; a malformed file is an error, never silently empty."""
    if not SUPERSEDED_FILE.exists():
        return {"rules": []}
    try:
        doc = json.loads(SUPERSEDED_FILE.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"state/superseded.json is not valid JSON: {exc}")
    if not isinstance(doc, dict) or not isinstance(doc.get("rules", []), list):
        raise SystemExit("state/superseded.json must be an object with a 'rules' list")
    return doc


def build_registry():
    """Scan all agent .py and .py.card files and build registry.json."""
    agents = []
    publishers = set()
    categories = set()
    errors = []
    seen_names = set()
    previous_agents = {}
    if REGISTRY_FILE.exists():
        try:
            previous_registry = json.loads(
                REGISTRY_FILE.read_text(encoding="utf-8")
            )
            previous_agents = {
                agent.get("name"): agent
                for agent in previous_registry.get("agents", [])
                if isinstance(agent, dict) and agent.get("name")
            }
        except (json.JSONDecodeError, OSError):
            previous_agents = {}
    lifecycle_agents = {}
    if LIFECYCLE_FILE.exists():
        try:
            lifecycle_data = json.loads(
                LIFECYCLE_FILE.read_text(encoding="utf-8")
            )
            if lifecycle_data.get("schema") != LIFECYCLE_SCHEMA:
                errors.append(
                    f"{LIFECYCLE_FILE}: expected schema {LIFECYCLE_SCHEMA}"
                )
            lifecycle_agents = lifecycle_data.get("agents", {})
            if not isinstance(lifecycle_agents, dict):
                errors.append(f"{LIFECYCLE_FILE}: agents must be an object")
                lifecycle_agents = {}
        except (json.JSONDecodeError, OSError) as exc:
            errors.append(f"{LIFECYCLE_FILE}: invalid lifecycle JSON: {exc}")
            lifecycle_agents = {}

    # Scan both .py and .py.card files; .py.card takes priority if both exist
    all_files = sorted(set(
        list(AGENTS_DIR.rglob("*.py")) +
        [p for p in AGENTS_DIR.rglob("*.py.card")]
    ))
    canonical_names = {}
    for candidate in all_files:
        if (
            candidate.suffix != ".py"
            or not candidate.name.endswith("_agent.py")
        ):
            continue
        candidate_manifest = extract_manifest(candidate)
        if candidate_manifest is None:
            continue
        if (
            validate_manifest(candidate, candidate_manifest)
            or validate_runtime_contract(candidate, candidate_manifest)
        ):
            continue
        canonical_names[candidate] = candidate_manifest["name"]

    for py_path in all_files:
        legacy_manifest = None
        if (
            py_path.suffix == ".py"
            and not py_path.name.endswith("_agent.py")
        ):
            legacy_manifest = extract_manifest(py_path)
        if superseded_legacy_agent_path(
            py_path,
            canonical_names,
            (
                legacy_manifest.get("name")
                if legacy_manifest
                else None
            ),
        ):
            continue
        # Enforce snake_case filenames — no dashes allowed
        stem = py_path.stem.replace('.py', '')  # handle .py.card
        if '-' in stem:
            errors.append(f"{py_path}: filename contains dashes — rename to snake_case (e.g., {stem.replace('-', '_')}.py)")
            continue

        # Skip utility/template files
        is_utility = py_path.name in ("update_agents.py", "d365_base_agent.py", "__init__.py")
        is_template = "templates" in py_path.parts
        is_source = "_sources" in py_path.parts   # converged-factory component sources (not standalone agents)
        if is_utility or is_template or is_source:
            continue

        manifest = legacy_manifest or extract_manifest(py_path)
        if manifest is None:
            continue

        validation_errors = validate_manifest(py_path, manifest)
        validation_errors.extend(validate_runtime_contract(py_path, manifest))
        if validation_errors:
            for err in validation_errors:
                errors.append(f"{py_path}: {err}")
            continue

        name = manifest["name"]

        # .py.card takes priority over .py for the same agent name
        is_card = py_path.name.endswith('.py.card')
        if name in seen_names and not is_card:
            continue  # skip .py if .py.card already registered
        if name in seen_names and is_card:
            agents[:] = [a for a in agents if a["name"] != name]  # replace .py with .py.card
        seen_names.add(name)

        publisher = name.split("/")[0]
        publishers.add(publisher)
        categories.add(manifest.get("category", "uncategorized"))
        
        # Security scan (skip first-party allowlisted agents)
        if not _security_allowlisted(py_path):
            sec_warnings = scan_security(py_path)
            if sec_warnings:
                for w in sec_warnings:
                    errors.append(w)
                continue

        # Dynamic-code capabilities: allowed but TAGGED, never fatal. Consumers
        # who want to restrict exec/eval can filter on manifest["_capabilities"].
        caps = scan_capabilities(py_path)
        if caps:
            manifest["_capabilities"] = caps
            manifest["_uses_exec"] = ("exec" in caps or "compile_exec" in caps)

        # Integrity hash
        sha256 = compute_sha256(py_path)

        # Version immutability — reject silent content changes
        serialized_path = registry_path(py_path)
        immut_err = check_version_immutability(
            name, manifest["version"], sha256, serialized_path)
        if immut_err:
            errors.append(f"{py_path}: {immut_err}")
            continue

        # Add file metadata
        content = py_path.read_text(encoding="utf-8")
        manifest["_file"] = serialized_path
        manifest["_install_filename"] = install_filename(name)

        # Extract stack membership from directory structure
        # (maps AI Agent Templates stacks -> deck groupings)
        stack_name, stack_vertical = extract_stack_info(py_path)
        if stack_name:
            manifest["_stack"] = stack_name
            manifest["_stack_vertical"] = stack_vertical
        manifest["_sha256"] = sha256
        manifest.update(_lifecycle_metadata(
            name=name,
            version=str(manifest.get("version", "")),
            digest=sha256,
            canonical_path=serialized_path,
            lifecycle_agents=lifecycle_agents,
            errors=errors,
        ))
        manifest["_seed"] = compute_seed(
            name,
            manifest.get("category", "general"),
            manifest.get("quality_tier", "community"),
            manifest.get("tags", []),
            manifest.get("dependencies", []),
        )
        manifest["_size_kb"] = round(len(canonical_file_bytes(py_path)) / 1024, 1)
        manifest["_lines"] = len(content.split('\n'))
        manifest["_has_card"] = is_card or _has_holo_card(name)
        manifest["_added_at"] = _git_first_committed(py_path)

        # Provenance chain — git commit graph IS the ledger.
        # _first_commit_sha pins the original publication; consumers can
        # fetch the bytes via raw.githubusercontent.com/<repo>/<sha>/<path>
        # and verify against _sha256. _latest_commit_sha bounds the edit
        # window. _card_sha256 hashes this agent's specific card content
        # (canonical JSON) so consumers can verify per-card without
        # trusting the aggregate holo_cards.json.
        manifest["_first_commit_sha"] = _git_first_commit_sha(py_path)
        manifest["_latest_commit_sha"] = _git_latest_commit_sha(py_path)
        if manifest["_has_card"] and not is_card:
            holo = _holo_card_for(name)
            if holo is not None:
                manifest["_card_sha256"] = _card_content_sha256(holo)

        # Extract __card__ shell from .py.card files
        if is_card:
            card_data = extract_card(py_path)
            if card_data:
                manifest["_card"] = card_data
                manifest["_card_sha256"] = _card_content_sha256(card_data)

        agents.append(manifest)

    # ─── Scan swarms/ for converged multi-agent singletons ──────────────
    converged_swarms = []
    if SWARMS_DIR.exists():
        swarm_files = sorted(SWARMS_DIR.rglob("*.py"))
        for py_path in swarm_files:
            if py_path.name == "__init__.py":
                continue
            stem = py_path.stem
            if '-' in stem:
                errors.append(f"{py_path}: filename contains dashes — rename to snake_case")
                continue

            manifest = extract_manifest(py_path)
            if manifest is None:
                continue
            validation_errors = validate_manifest(py_path, manifest)
            if validation_errors:
                for err in validation_errors:
                    errors.append(f"{py_path}: {err}")
                continue

            swarm_meta = extract_swarm(py_path)
            if swarm_meta is None:
                errors.append(f"{py_path}: missing __swarm__ dict (required for swarms/)")
                continue
            swarm_errors = validate_swarm(py_path, swarm_meta)
            if swarm_errors:
                for err in swarm_errors:
                    errors.append(f"{py_path}: {err}")
                continue

            # Security scan
            if not _security_allowlisted(py_path):
                sec_warnings = scan_security(py_path)
                if sec_warnings:
                    for w in sec_warnings:
                        errors.append(w)
                    continue

            sha256 = compute_sha256(py_path)
            content = py_path.read_text(encoding="utf-8")

            name = manifest["name"]
            publisher = name.split("/")[0]
            publishers.add(publisher)
            categories.add(manifest.get("category", "uncategorized"))

            entry = {
                "type": "converged",
                "schema": manifest.get("schema", "rapp-agent/1.0"),
                "name": name,
                "version": manifest.get("version", "0.0.0"),
                "display_name": manifest.get("display_name", ""),
                "description": manifest.get("description", ""),
                "author": manifest.get("author", ""),
                "tags": manifest.get("tags", []),
                "category": manifest.get("category", ""),
                "quality_tier": manifest.get("quality_tier", "community"),
                "requires_env": manifest.get("requires_env", []),
                "dependencies": manifest.get("dependencies", []),
                "_file": registry_path(py_path),
                "_install_filename": install_filename(name),
                "_sha256": sha256,
                "_seed": compute_seed(
                    name,
                    manifest.get("category", "general"),
                    manifest.get("quality_tier", "community"),
                    manifest.get("tags", []),
                    manifest.get("dependencies", []),
                ),
                "_size_kb": round(len(canonical_file_bytes(py_path)) / 1024, 1),
                "_lines": len(content.split('\n')),
                "_added_at": _git_first_committed(py_path),
                "_first_commit_sha": _git_first_commit_sha(py_path),
                "_latest_commit_sha": _git_latest_commit_sha(py_path),
                "_swarm": swarm_meta,
            }
            holo = _holo_card_for(name)
            if holo is not None:
                entry["_card_sha256"] = _card_content_sha256(holo)
            converged_swarms.append(entry)

    # ─── Scan agents/ for .py.stub gated entries ───────────────────────
    # Stubs are manifest-only files that point at a private repo for the
    # actual agent.py bytes. They appear in the registry like normal
    # agents but with type:"stub", and the brainstem's install path
    # resolves the __source__ pointer at install time using the user's
    # own GitHub credentials.
    stub_files = sorted(AGENTS_DIR.rglob("*.py.stub"))
    for py_path in stub_files:
        stem = py_path.name[:-len(".py.stub")]
        if '-' in stem:
            errors.append(f"{py_path}: filename contains dashes — rename to snake_case")
            continue

        purity_errors = validate_stub_purity(py_path)
        if purity_errors:
            for err in purity_errors:
                errors.append(f"{py_path}: {err}")
            continue

        manifest = extract_manifest(py_path)
        if manifest is None:
            errors.append(f"{py_path}: missing __manifest__ dict")
            continue
        validation_errors = validate_manifest(py_path, manifest)
        if validation_errors:
            for err in validation_errors:
                errors.append(f"{py_path}: {err}")
            continue

        src = extract_source(py_path)
        if src is None:
            errors.append(f"{py_path}: missing __source__ dict (required for stubs)")
            continue
        source_errors = validate_source(py_path, src)
        if source_errors:
            for err in source_errors:
                errors.append(f"{py_path}: {err}")
            continue

        name = manifest["name"]
        if name in seen_names:
            errors.append(f"{py_path}: duplicate name '{name}' (already registered)")
            continue
        seen_names.add(name)

        publisher = name.split("/")[0]
        publishers.add(publisher)
        categories.add(manifest.get("category", "uncategorized"))

        # Stubs are forced to quality_tier "private" — the source isn't
        # readable by reviewers, so the standard promotion ladder
        # (community → verified → official) doesn't apply.
        manifest["quality_tier"] = "private"

        # Hash the stub file itself (not the bytes it points at — those
        # live in the private repo and may not be accessible here).
        stub_sha = compute_sha256(py_path)
        content = py_path.read_text(encoding="utf-8")

        manifest["type"] = "stub"
        manifest["_file"] = registry_path(py_path)
        manifest["_install_filename"] = install_filename(name)
        manifest["_stub_sha256"] = stub_sha
        manifest["_source"] = src
        manifest.update(_lifecycle_metadata(
            name=name,
            version=str(manifest.get("version", "")),
            digest=stub_sha,
            canonical_path=registry_path(py_path),
            lifecycle_agents=lifecycle_agents,
            errors=errors,
        ))
        manifest["_seed"] = compute_seed(
            name,
            manifest.get("category", "general"),
            "private",
            manifest.get("tags", []),
            manifest.get("dependencies", []),
        )
        manifest["_size_kb"] = round(len(canonical_file_bytes(py_path)) / 1024, 1)
        manifest["_lines"] = len(content.split('\n'))
        manifest["_has_card"] = _has_holo_card(name)
        manifest["_added_at"] = _git_first_committed(py_path)
        manifest["_first_commit_sha"] = _git_first_commit_sha(py_path)
        manifest["_latest_commit_sha"] = _git_latest_commit_sha(py_path)
        if manifest["_has_card"]:
            holo = _holo_card_for(name)
            if holo is not None:
                manifest["_card_sha256"] = _card_content_sha256(holo)

        agents.append(manifest)

    for agent in agents:
        agent.pop("_seed_aliases", None)
        aliases = preserved_seed_aliases(
            previous_agents.get(agent["name"], {}),
            agent["_seed"],
        )
        if aliases:
            agent["_seed_aliases"] = aliases

    # ─── Seed collision check (agents + converged swarms) ─────────────
    seen_seeds = {}
    for a in agents:
        for seed in [a.get("_seed"), *a.get("_seed_aliases", [])]:
            if seed is None:
                continue
            if seed in seen_seeds:
                errors.append(
                    f"Seed collision: {a['name']} and {seen_seeds[seed]} "
                    f"both resolve to seed {seed}"
                )
            else:
                seen_seeds[seed] = a["name"]

    for s in converged_swarms:
        seed = s.get("_seed")
        if seed is None:
            continue
        if seed in seen_seeds:
            errors.append(
                f"Seed collision: {s['name']} and {seen_seeds[seed]} "
                f"both resolve to seed {seed}"
            )
        else:
            seen_seeds[seed] = s["name"]

    # Detect duplicate display_names (different manifest names, same user-facing name)
    seen_display = {}
    duplicates = []
    for a in agents:
        dn = a.get("display_name", "")
        if dn in seen_display:
            duplicates.append((dn, seen_display[dn], a["name"]))
        else:
            seen_display[dn] = a["name"]

    # ─── Build stacks index (backward compat) ──────────────���─────────
    stacks = {}
    for a in agents:
        s = a.get("_stack")
        if not s:
            continue
        if s not in stacks:
            stacks[s] = {
                "name": s,
                "display_name": s.replace("_", " ").title(),
                "vertical": a.get("_stack_vertical", ""),
                "agents": [],
            }
        stacks[s]["agents"].append(a["name"])

    # ─── Promote stacks to swarms (type: stack) ──────────────────────
    stack_swarms = []
    for stack_name, stack_data in stacks.items():
        agent_files = []
        total_size = 0
        total_lines = 0
        for agent_entry in agents:
            if agent_entry.get("_stack") == stack_name:
                agent_files.append(agent_entry["_file"])
                total_size += agent_entry.get("_size_kb", 0)
                total_lines += agent_entry.get("_lines", 0)

        stack_swarms.append({
            "type": "stack",
            "name": f"@{stack_data['vertical']}/{stack_name}",
            "display_name": stack_data["display_name"],
            "vertical": stack_data["vertical"],
            "category": stack_data["vertical"],
            "agent_count": len(stack_data["agents"]),
            "agents": stack_data["agents"],
            "agent_files": agent_files,
            "_size_kb": round(total_size, 1),
            "_lines": total_lines,
        })

    # Combine all swarms
    all_swarms = converged_swarms + stack_swarms

    # ─── Superseded copies: kept at their paths, withheld from lookups ─
    # state/superseded.json names publishers/agents whose current version now
    # lives in an outside channel (sources.json). The files stay (Article
    # XXIII); the registry — and therefore every surface built from it —
    # omits them. Only the COUNT and the rule are published, never the list.
    superseded_doc = _load_superseded()
    withheld_names = set()
    if superseded_doc.get("rules"):
        pubs = {str(r.get("publisher")) for r in superseded_doc["rules"] if r.get("publisher")}
        names = {str(r.get("agent")) for r in superseded_doc["rules"] if r.get("agent")}
        def _withheld(a):
            n = str(a.get("name", ""))
            return n in names or any(n.startswith(pb + "/") for pb in pubs)
        withheld_names = {a["name"] for a in agents if _withheld(a)}
        agents = [a for a in agents if a["name"] not in withheld_names]
        def _names(members):
            return [str(m if isinstance(m, str) else (m or {}).get("name", "")) for m in (members or [])]
        # swarms: drop any that reference a withheld agent (a swarm with a dark member is not runnable)
        all_swarms = [sw for sw in all_swarms
                      if not any(n in withheld_names for n in _names(sw.get("agents") or sw.get("members")))]
        # stacks index: dict of name -> {"agents": [names]}; drop stacks that go fully dark, trim the rest
        if stacks:
            kept = {}
            for st_name, st in stacks.items():
                remaining = [n for n in _names(st.get("agents")) if n not in withheld_names]
                if remaining:
                    kept[st_name] = {**st, "agents": remaining}
            stacks = kept
        publishers = {a.get("_publisher") or str(a.get("name", "")).split("/")[0] for a in agents}
        categories = {a.get("category") for a in agents if a.get("category")}

    # ─── Build registry ───────────────────────────────────────────────
    tombstones = _validated_tombstones(lifecycle_agents, errors)
    registry = {
        "schema": "rapp-registry/1.1",
        "version": "1.1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "stats": {
            "total_agents": len(agents),
            "total_swarms": len(all_swarms),
            "total_stubs": sum(1 for a in agents if a.get("type") == "stub"),
            "publishers": len(publishers),
            "categories": len(categories),
            "publisher_list": sorted(publishers),
            "category_list": sorted(categories)
        },
        "duplicates": [{"display_name": dn, "agents": [a1, a2]} for dn, a1, a2 in duplicates],
        "agents": agents,
        "swarms": all_swarms,
        "lifecycle": {
            "schema": LIFECYCLE_SCHEMA,
            "receipt_schema": RECEIPT_SCHEMA,
            "tombstones": tombstones,
        },
        "superseded": {
            "schema": superseded_doc.get("schema", "rar-superseded/1"),
            "withheld_count": len(withheld_names),
            "rules": superseded_doc.get("rules", []),
            "note": "withheld agents remain at their published paths; they are omitted from every lookup",
        },
    }

    if stacks:
        registry["stacks"] = stacks

    # ─── Release ledger ───────────────────────────────────────────────
    # The release workflow used to append its record straight into
    # registry.json. This function rebuilds that file from scratch on every
    # push to agents/**, so the entire release history was erased by the next
    # agent submission — and because nothing ever read the field, it vanished
    # silently. state/releases.json is the durable record; registry.json only
    # ever carries a projection of it, which keeps registry.json fully derived
    # (its contract) while giving consumers one place to look.
    releases_file = Path("state") / "releases.json"
    if releases_file.exists():
        try:
            ledger = json.loads(releases_file.read_text(encoding="utf-8"))
            entries = (ledger or {}).get("releases")
            # Validate the SHAPE, don't just catch exceptions. The previous
            # guard caught JSONDecodeError/OSError/AttributeError, none of
            # which a hand-edited ledger actually raises: {"releases": {...}}
            # reached entries[-1] and died on KeyError, {"releases": 7} on
            # TypeError, and {"releases": "abc"} silently projected the
            # character "c" into registry.json as latest_release.
            entries = [e for e in entries if isinstance(e, dict)] \
                if isinstance(entries, list) else []
            if entries:
                registry["releases"] = entries
                # "Latest" must mean the same thing here as it does on GitHub.
                # release.yml marks canaries prerelease:true, and GitHub's
                # /releases/latest alias — the documented client download path
                # — skips prereleases. Taking entries[-1] made a canary the
                # registry's advertised latest release while every client
                # actually downloading "latest" still got the prior stable one.
                stable = [e for e in entries if e.get("release_type") != "canary"]
                registry["latest_release"] = (stable or entries)[-1]
        except (json.JSONDecodeError, OSError, TypeError, AttributeError):
            # A malformed ledger must not take the registry build down with
            # it; the agents are the payload, the release stamp is metadata.
            pass

    # Include instance metadata if rar.config.json exists
    config_file = Path("rar.config.json")
    if config_file.exists():
        try:
            config = json.loads(config_file.read_text(encoding="utf-8"))
            registry["instance"] = {
                "role": config.get("role", "main"),
                "owner": config.get("owner", ""),
                "repo": config.get("repo", ""),
                "upstream": config.get("upstream"),
            }
        except (json.JSONDecodeError, KeyError):
            pass

    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2)

    print(f"OK Registry built: {len(agents)} agents from {len(publishers)} publishers")
    print(f"  Swarms: {len(converged_swarms)} converged + {len(stack_swarms)} stacks = {len(all_swarms)} total")
    print(f"  Categories: {', '.join(sorted(categories))}")
    print(f"  Publishers: {', '.join(sorted(publishers))}")

    if duplicates:
        # Duplicate display names ship a confusing store UI (two identical rows
        # in every agent picker) — hard failure, not a warning.
        print(f"\nERROR {len(duplicates)} duplicate display names (build blocked):")
        for dn, a1, a2 in duplicates:
            print(f"  - \"{dn}\": {a1} vs {a2}")
        print("  Fix: delete the clone or rename its display_name — one agent per concern.")

    if errors:
        print(f"\nWARNING {len(errors)} validation errors:")
        for err in errors:
            print(f"  - {err}")
        return 1

    if duplicates:
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(build_registry())
