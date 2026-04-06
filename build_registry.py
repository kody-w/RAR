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

Supports two file formats:
- slug.py      — bare agent (code + manifest)
- slug.py.card — complete agent+card package (code + manifest + __card__ shell)
"""

import ast
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

AGENTS_DIR = Path("agents")
REGISTRY_FILE = Path("registry.json")
HOLO_CARDS_FILE = Path("cards/holo_cards.json")

# Cache holo card slugs for _has_card check
_holo_slugs = None
def _has_holo_card(agent_name):
    global _holo_slugs
    if _holo_slugs is None:
        try:
            data = json.loads(HOLO_CARDS_FILE.read_text())
            _holo_slugs = set(data.keys()) if isinstance(data, dict) else set()
        except (FileNotFoundError, json.JSONDecodeError):
            _holo_slugs = set()
    # holo_cards.json keys are full agent names like "@kody/deal-desk"
    return agent_name in _holo_slugs or agent_name.replace('_', '-') in _holo_slugs or agent_name.replace('-', '_') in _holo_slugs
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


# First-party agents that legitimately need elevated capabilities.
# Community submissions are NEVER added here — they must find safe alternatives.
SECURITY_ALLOWLIST = {
    "agents/@kody/agent_workbench_agent.py",       # workbench needs exec for agent orchestration
    "agents/@kody/rappter_engine_agent.py",         # engine needs subprocess for CLI mode
    "agents/@kody/rar_remote_agent.py",             # remote agent needs subprocess for git/install
    "agents/@borg/prompt_to_video.py",              # video rendering needs subprocess for ffmpeg
    "agents/@discreetRappers/scripted_demo.py",     # demo runner needs exec for script execution
}

# Patterns that should never appear in agent code (supply chain defense)
DANGEROUS_PATTERNS = [
    (r'\beval\s*\(', "eval() is forbidden — use safe alternatives"),
    (r'\bexec\s*\(', "exec() is forbidden — use safe alternatives"),
    (r'\b__import__\s*\(', "__import__() is forbidden — use standard imports"),
    (r'\bcompile\s*\(.*["\']exec["\']', "compile() with exec mode is forbidden"),
    (r'\bos\.system\s*\(', "os.system() is forbidden — declare in requires_env"),
    (r'\bsubprocess\.\w+\s*\(', "subprocess is forbidden in agents"),
    (r'\bopen\s*\(.*(\/etc|\/proc|\.env|\.ssh|passwd)', "suspicious file access pattern"),
    (r'(api[_-]?key|secret|password|token)\s*=\s*["\'][^"\']{8,}', "possible hardcoded secret"),
]


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

        # Extract __card__ shell from .py.card files
        if is_card:
            card_data = extract_card(py_path)
            if card_data:
                manifest["_card"] = card_data

        agents.append(manifest)
    
    registry = {
        "schema": "rapp-registry/1.0",
        "version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "stats": {
            "total_agents": len(agents),
            "publishers": len(publishers),
            "categories": len(categories),
            "publisher_list": sorted(publishers),
            "category_list": sorted(categories)
        },
        "agents": agents
    }

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
    print(f"  Categories: {', '.join(sorted(categories))}")
    print(f"  Publishers: {', '.join(sorted(publishers))}")
    
    if errors:
        print(f"\n⚠ {len(errors)} validation errors:")
        for err in errors:
            print(f"  - {err}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(build_registry())
