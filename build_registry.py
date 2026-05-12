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

# Cache holo card slugs and per-card content for _has_card / _card_sha256 lookups
_holo_data = None
def _holo_cards():
    global _holo_data
    if _holo_data is None:
        try:
            data = json.loads(HOLO_CARDS_FILE.read_text())
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


def extract_manifest(py_path: Path) -> dict:
    """Extract __manifest__ dict from a Python file using AST parsing."""
    try:
        source = py_path.read_text()
        tree = ast.parse(source)
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


def extract_card(py_path: Path) -> dict:
    """Extract __card__ dict from a .py.card file using AST parsing."""
    try:
        source = py_path.read_text()
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
        source = py_path.read_text()
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
        source = py_path.read_text()
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
        tree = ast.parse(py_path.read_text())
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


# Files that legitimately need elevated capabilities (eval / exec) which
# stay banned for everyone else. Subprocess is no longer banned — agents
# routinely wrap external CLIs (gh, kubectl, terraform, ffmpeg, az, gcloud,
# npm, workiq, etc.), and the allowlist approach didn't scale to the
# integration category. Submitters should declare wrapped binaries in
# `requires_env` so consumers know what gets shelled out at install time.
SECURITY_ALLOWLIST = {
    "agents/@kody/agent_workbench_agent.py",       # workbench needs exec for agent orchestration
    "agents/@kody/rappter_engine_agent.py",         # engine needs subprocess for CLI mode
    "agents/@kody/rar_remote_agent.py",             # remote agent needs subprocess for git/install
    "agents/@borg/prompt_to_video_agent.py",        # video rendering needs subprocess for ffmpeg
    "agents/@discreetRappers/scripted_demo_agent.py", # demo runner needs exec for script execution
    "agents/@rapp/learn_new_agent.py",               # meta-agent uses subprocess for Copilot code gen + pip install
    "agents/@rapp/fleet_commander_agent.py",          # TDD pipeline uses subprocess for Copilot CLI + pytest + git
    "swarms/@rapp/bookfactory_agent.py",            # converged swarm with inlined LLM dispatch
    "swarms/@rapp/momentfactory_agent.py",          # converged swarm with inlined LLM dispatch
}

# Patterns that should never appear in agent code (supply chain defense).
# Subprocess is intentionally NOT here — wrapping external CLIs is a normal
# integration pattern. See SECURITY_ALLOWLIST comment above.
DANGEROUS_PATTERNS = [
    (r'\beval\s*\(', "eval() is forbidden — use safe alternatives"),
    (r'\bexec\s*\(', "exec() is forbidden — use safe alternatives"),
    (r'\b__import__\s*\(', "__import__() is forbidden — use standard imports"),
    (r'\bcompile\s*\(.*["\']exec["\']', "compile() with exec mode is forbidden"),
    (r'\bos\.system\s*\(', "os.system() is forbidden — use subprocess and declare in requires_env"),
    (r'\bopen\s*\(.*(\/etc|\/proc|\.env|\.ssh|passwd)', "suspicious file access pattern"),
    (r'(api[_-]?key|secret|password|token)\s*=\s*["\'][^"\']{8,}', "possible hardcoded secret"),
]


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


def compute_sha256(file_path: Path) -> str:
    """Compute SHA256 hash of file contents."""
    return hashlib.sha256(file_path.read_bytes()).hexdigest()


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


def scan_security(py_path: Path) -> list:
    """Static security scan — returns list of warnings."""
    warnings = []
    source = py_path.read_text()
    for pattern, message in DANGEROUS_PATTERNS:
        if re.search(pattern, source):
            warnings.append(f"{py_path}: {message}")
    return warnings


def check_version_immutability(name: str, version: str, sha256: str, file_path: str) -> str | None:
    """If a previous registry exists, verify version wasn't silently changed."""
    if not REGISTRY_FILE.exists():
        return None
    try:
        prev = json.loads(REGISTRY_FILE.read_text())
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


def _git_first_committed(path: Path):
    """Return the ISO date a file was first committed, or None if unavailable."""
    try:
        result = subprocess.run(
            ["git", "log", "--diff-filter=A", "--format=%cI", "--follow", "--", str(path)],
            capture_output=True, text=True, timeout=10
        )
        dates = result.stdout.strip().splitlines()
        return dates[-1] if dates else None
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None


def _git_first_commit_sha(path: Path):
    """Return the commit SHA where `path` first appeared. This is the
    permanent address for the file's initial publication — anyone can
    fetch the original bytes via raw.githubusercontent.com/<repo>/<sha>/<path>
    and verify against the recorded _sha256. Part of the poor-man's-
    blockchain provenance chain (commit graph IS the ledger)."""
    try:
        result = subprocess.run(
            ["git", "log", "--diff-filter=A", "--format=%H", "--follow", "--", str(path)],
            capture_output=True, text=True, timeout=10
        )
        shas = result.stdout.strip().splitlines()
        return shas[-1] if shas else None
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None


def _git_latest_commit_sha(path: Path):
    """Return the commit SHA of the most recent change to `path`. Together
    with _first_commit_sha this bounds the file's edit window — anyone
    can `git log <first>..<latest> -- <path>` to audit every change."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%H", "--follow", "--", str(path)],
            capture_output=True, text=True, timeout=10
        )
        sha = result.stdout.strip()
        return sha or None
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None


def _card_content_sha256(card_data: dict) -> str:
    """Hash the card's content for that specific agent. Uses canonical
    JSON (sorted keys, no whitespace) so the hash is reproducible from
    any consumer. Lets consumers verify card integrity per-agent without
    trusting the aggregate holo_cards.json file."""
    canonical = json.dumps(card_data, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def build_registry():
    """Scan all agent .py and .py.card files and build registry.json."""
    agents = []
    publishers = set()
    categories = set()
    errors = []
    seen_names = set()

    # Scan both .py and .py.card files; .py.card takes priority if both exist
    all_files = sorted(set(
        list(AGENTS_DIR.rglob("*.py")) +
        [p for p in AGENTS_DIR.rglob("*.py.card")]
    ))

    for py_path in all_files:
        # Enforce snake_case filenames — no dashes allowed
        stem = py_path.stem.replace('.py', '')  # handle .py.card
        if '-' in stem:
            errors.append(f"{py_path}: filename contains dashes — rename to snake_case (e.g., {stem.replace('-', '_')}.py)")
            continue

        # Skip utility/template files
        is_utility = py_path.name in ("update_agents.py", "d365_base_agent.py", "__init__.py")
        is_template = "templates" in py_path.parts
        if is_utility or is_template:
            continue

        manifest = extract_manifest(py_path)
        if manifest is None:
            continue

        validation_errors = validate_manifest(py_path, manifest)
        if validation_errors:
            for err in validation_errors:
                errors.append(f"{py_path}: {err}")
            continue

        name = manifest["name"]

        # .py.card takes priority over .py for the same agent name
        is_card = str(py_path).endswith('.py.card')
        if name in seen_names and not is_card:
            continue  # skip .py if .py.card already registered
        if name in seen_names and is_card:
            agents[:] = [a for a in agents if a["name"] != name]  # replace .py with .py.card
        seen_names.add(name)

        publisher = name.split("/")[0]
        publishers.add(publisher)
        categories.add(manifest.get("category", "uncategorized"))
        
        # Security scan (skip first-party allowlisted agents)
        if str(py_path) not in SECURITY_ALLOWLIST:
            sec_warnings = scan_security(py_path)
            if sec_warnings:
                for w in sec_warnings:
                    errors.append(w)
                continue

        # Integrity hash
        sha256 = compute_sha256(py_path)

        # Version immutability — reject silent content changes
        immut_err = check_version_immutability(name, manifest["version"], sha256, str(py_path))
        if immut_err:
            errors.append(f"{py_path}: {immut_err}")
            continue

        # Add file metadata
        content = py_path.read_text()
        manifest["_file"] = str(py_path)

        # Extract stack membership from directory structure
        # (maps AI Agent Templates stacks -> deck groupings)
        stack_name, stack_vertical = extract_stack_info(py_path)
        if stack_name:
            manifest["_stack"] = stack_name
            manifest["_stack_vertical"] = stack_vertical
        manifest["_sha256"] = sha256
        manifest["_seed"] = compute_seed(
            name,
            manifest.get("category", "general"),
            manifest.get("quality_tier", "community"),
            manifest.get("tags", []),
            manifest.get("dependencies", []),
        )
        manifest["_size_kb"] = round(py_path.stat().st_size / 1024, 1)
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
            if str(py_path) not in SECURITY_ALLOWLIST:
                sec_warnings = scan_security(py_path)
                if sec_warnings:
                    for w in sec_warnings:
                        errors.append(w)
                    continue

            sha256 = compute_sha256(py_path)
            content = py_path.read_text()

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
                "_file": str(py_path),
                "_sha256": sha256,
                "_seed": compute_seed(
                    name,
                    manifest.get("category", "general"),
                    manifest.get("quality_tier", "community"),
                    manifest.get("tags", []),
                    manifest.get("dependencies", []),
                ),
                "_size_kb": round(py_path.stat().st_size / 1024, 1),
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
        content = py_path.read_text()

        manifest["type"] = "stub"
        manifest["_file"] = str(py_path)
        manifest["_stub_sha256"] = stub_sha
        manifest["_source"] = src
        manifest["_seed"] = compute_seed(
            name,
            manifest.get("category", "general"),
            "private",
            manifest.get("tags", []),
            manifest.get("dependencies", []),
        )
        manifest["_size_kb"] = round(py_path.stat().st_size / 1024, 1)
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

    # ─── Seed collision check (agents + converged swarms) ─────────────
    seen_seeds = {}
    for a in agents:
        seed = a.get("_seed")
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

    # ─── Build registry ───────────────────────────────────────────────
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
    }

    if stacks:
        registry["stacks"] = stacks

    # Include instance metadata if rar.config.json exists
    config_file = Path("rar.config.json")
    if config_file.exists():
        try:
            config = json.loads(config_file.read_text())
            registry["instance"] = {
                "role": config.get("role", "main"),
                "owner": config.get("owner", ""),
                "repo": config.get("repo", ""),
                "upstream": config.get("upstream"),
            }
        except (json.JSONDecodeError, KeyError):
            pass

    with open(REGISTRY_FILE, "w") as f:
        json.dump(registry, f, indent=2)

    print(f"✓ Registry built: {len(agents)} agents from {len(publishers)} publishers")
    print(f"  Swarms: {len(converged_swarms)} converged + {len(stack_swarms)} stacks = {len(all_swarms)} total")
    print(f"  Categories: {', '.join(sorted(categories))}")
    print(f"  Publishers: {', '.join(sorted(publishers))}")

    if duplicates:
        print(f"\n⚠ {len(duplicates)} duplicate display names:")
        for dn, a1, a2 in duplicates:
            print(f"  - \"{dn}\": {a1} vs {a2}")

    if errors:
        print(f"\n⚠ {len(errors)} validation errors:")
        for err in errors:
            print(f"  - {err}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(build_registry())
