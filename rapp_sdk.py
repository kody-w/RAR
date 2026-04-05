#!/usr/bin/env python3
"""RAPP Foundation SDK — Build agents, mint cards, track Binders. The open developer toolkit for the RAPP agent ecosystem."""

from __future__ import annotations

__version__ = "1.0.0"

# =============================================================================
# SECTION 1: CONSTANTS + CONFIG
# =============================================================================

import ast
import argparse
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

REQUIRED_MANIFEST_FIELDS = [
    "schema", "name", "version", "display_name",
    "description", "author", "tags", "category",
]

VALID_CATEGORIES = [
    "core", "pipeline", "integrations", "productivity", "devtools", "general",
    "b2b_sales", "b2c_sales", "healthcare", "financial_services", "manufacturing",
    "energy", "federal_government", "slg_government", "human_resources",
    "it_management", "professional_services", "retail_cpg", "software_digital_products",
]

VALID_TIERS = ["experimental", "community", "verified", "official"]
SUBMITTABLE_TIERS = ["experimental", "community"]

REPO = "kody-w/RAR"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/main"
API_BASE = f"https://api.github.com/repos/{REPO}"

TIER_TO_RARITY = {
    "official": "mythic",
    "verified": "rare",
    "community": "core",
    "experimental": "starter",
}

RARITY_LABELS = {
    "mythic": "Legendary",
    "rare": "Elite",
    "core": "Core",
    "starter": "Starter",
}

RARITY_FLOOR = {
    "mythic": 200,
    "rare": 100,
    "core": 40,
    "starter": 10,
}

# Agent scaffold template — uses __TOKEN__ placeholders to avoid brace conflicts
AGENT_TEMPLATE = '''\
"""__DESCRIPTION__"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "__NAME__",
    "version": "1.0.0",
    "display_name": "__DISPLAY_NAME__",
    "description": "__DESCRIPTION__",
    "author": "__AUTHOR__",
    "tags": [],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic-agent"],
}

from agents.basic_agent import BasicAgent


class __CLASS_NAME__(BasicAgent):
    def __init__(self):
        self.name = "__DISPLAY_NAME__"
        self.metadata = {
            "description": "__DESCRIPTION__",
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        task = kwargs.get("task", "default")
        return f"__DISPLAY_NAME__ performed: {task}"


if __name__ == "__main__":
    agent = __CLASS_NAME__()
    print(agent.perform())
'''


# =============================================================================
# SECTION 2: MANIFEST OPERATIONS
# =============================================================================

def extract_manifest(path: str) -> dict | None:
    """Extract __manifest__ dict from a Python file using AST parsing (no code execution)."""
    try:
        source = Path(path).read_text()
        tree = ast.parse(source)
    except (SyntaxError, OSError) as e:
        return None

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__manifest__":
                    try:
                        return ast.literal_eval(node.value)
                    except (ValueError, TypeError):
                        return None
    return None


def validate_manifest(path: str, manifest: dict = None) -> list[str]:
    """Validate a manifest and return a list of error strings. Extracts manifest if not provided."""
    errors = []

    if manifest is None:
        manifest = extract_manifest(path)
        if manifest is None:
            return ["No __manifest__ dict found in file"]

    # Required fields
    for field in REQUIRED_MANIFEST_FIELDS:
        if field not in manifest:
            errors.append(f"Missing required field: {field}")

    # Name format: @publisher/slug
    name = manifest.get("name", "")
    if not name.startswith("@") or "/" not in name:
        errors.append(f"Invalid name format '{name}' — must be @publisher/slug")

    # Semver
    version = manifest.get("version", "")
    parts = version.split(".")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        errors.append(f"Invalid version '{version}' — must be semver (e.g., 1.0.0)")

    # Tags must be a list
    if not isinstance(manifest.get("tags", []), list):
        errors.append("tags must be a list")

    # Category
    category = manifest.get("category", "")
    if category and category not in VALID_CATEGORIES:
        errors.append(f"Invalid category '{category}' — must be one of: {', '.join(VALID_CATEGORIES)}")

    # Tier
    tier = manifest.get("quality_tier", "community")
    if tier not in VALID_TIERS:
        errors.append(f"Invalid quality_tier '{tier}' — must be one of: {', '.join(VALID_TIERS)}")

    return errors


def extract_card(path: str) -> dict | None:
    """Extract __card__ dict from a Python file using AST parsing."""
    try:
        source = Path(path).read_text()
        tree = ast.parse(source)
    except (SyntaxError, OSError):
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


# =============================================================================
# SECTION 3: CONTRACT TESTING (no pytest dependency)
# =============================================================================

def run_contract_tests(path: str) -> list[tuple[str, bool, str]]:
    """
    Run the RAPP agent contract test suite against a single agent file.
    Returns a list of (test_name, passed, message) tuples.
    """
    results = []
    agent_path = Path(path)

    def record(name, passed, msg):
        results.append((name, passed, msg))

    # 1. has_manifest
    try:
        manifest = extract_manifest(path)
        if manifest is not None:
            record("has_manifest", True, "__manifest__ dict found")
        else:
            record("has_manifest", False, "No __manifest__ dict in file")
            manifest = {}
    except Exception as e:
        record("has_manifest", False, f"Error reading manifest: {e}")
        manifest = {}

    # 2. manifest_fields
    try:
        missing = [f for f in REQUIRED_MANIFEST_FIELDS if f not in manifest]
        if not missing:
            record("manifest_fields", True, "All required fields present")
        else:
            record("manifest_fields", False, f"Missing fields: {', '.join(missing)}")
    except Exception as e:
        record("manifest_fields", False, f"Error: {e}")

    # 3. name_format
    try:
        name = manifest.get("name", "")
        if name.startswith("@") and "/" in name:
            record("name_format", True, f"Name '{name}' is valid @publisher/slug format")
        else:
            record("name_format", False, f"Name '{name}' must be @publisher/slug format")
    except Exception as e:
        record("name_format", False, f"Error: {e}")

    # 4. has_basic_agent (uses importlib to check class inheritance)
    agent_module = None
    agent_class = None
    try:
        # Add known BasicAgent locations to sys.path
        rapp_dir = str(agent_path.parent.parent / "@rapp")
        templates_dir = str(
            agent_path.parent.parent.parent
            / "agents"
            / "@aibast-agents-library"
            / "templates"
        )
        for extra in [rapp_dir, templates_dir, str(agent_path.parent.parent)]:
            if extra not in sys.path and Path(extra).exists():
                sys.path.insert(0, extra)

        # Also try adding the project root so `from agents.basic_agent import BasicAgent` works
        project_root = str(agent_path.parent.parent.parent)
        if project_root not in sys.path:
            sys.path.insert(0, project_root)

        spec = importlib.util.spec_from_file_location("_rapp_test_agent_", str(agent_path))
        agent_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(agent_module)

        # Find class that inherits BasicAgent
        import inspect
        found = False
        for obj_name, obj in inspect.getmembers(agent_module, inspect.isclass):
            bases = [b.__name__ for b in obj.__mro__]
            if "BasicAgent" in bases and obj.__name__ != "BasicAgent":
                agent_class = obj
                found = True
                break
        if found:
            record("has_basic_agent", True, f"Class '{agent_class.__name__}' inherits BasicAgent")
        else:
            record("has_basic_agent", False, "No class inheriting BasicAgent found")
    except Exception as e:
        record("has_basic_agent", False, f"Import error: {e}")

    # 5. instantiation
    agent_instance = None
    try:
        if agent_class is not None:
            agent_instance = agent_class()
            record("instantiation", True, f"{agent_class.__name__}() succeeded")
        else:
            record("instantiation", False, "Skipped — no agent class found")
    except Exception as e:
        record("instantiation", False, f"Instantiation failed: {e}")

    # 6. perform_returns_str
    try:
        if agent_instance is not None:
            result = agent_instance.perform()
            if isinstance(result, str):
                record("perform_returns_str", True, f"perform() returned str ({len(result)} chars)")
            else:
                record("perform_returns_str", False, f"perform() returned {type(result).__name__}, expected str")
        else:
            record("perform_returns_str", False, "Skipped — no agent instance")
    except Exception as e:
        record("perform_returns_str", False, f"perform() raised: {e}")

    # 7. standalone_execution
    try:
        proc = subprocess.run(
            [sys.executable, str(agent_path)],
            capture_output=True,
            text=True,
            timeout=15,
        )
        if proc.returncode == 0:
            record("standalone_execution", True, "python agent.py exited 0")
        else:
            record("standalone_execution", False, f"Exited {proc.returncode}: {proc.stderr.strip()[:120]}")
    except subprocess.TimeoutExpired:
        record("standalone_execution", False, "Timed out after 15 seconds")
    except Exception as e:
        record("standalone_execution", False, f"Error: {e}")

    # 8. has_docstring
    try:
        if agent_module is not None:
            doc = getattr(agent_module, "__doc__", None)
            if doc and doc.strip():
                record("has_docstring", True, f"Module docstring present ({len(doc.strip())} chars)")
            else:
                record("has_docstring", False, "Module docstring missing or empty")
        else:
            source = agent_path.read_text()
            tree = ast.parse(source)
            doc = ast.get_docstring(tree)
            if doc:
                record("has_docstring", True, "Module docstring present (parsed via AST)")
            else:
                record("has_docstring", False, "Module docstring missing")
    except Exception as e:
        record("has_docstring", False, f"Error: {e}")

    # 9. no_hardcoded_secrets
    try:
        source = agent_path.read_text()
        suspicious_patterns = [
            'API_KEY = "sk-',
            "API_KEY = 'sk-",
            'password = "',
            "password = '",
            'token = "',
            "token = '",
            'secret = "',
            "secret = '",
            'api_key = "',
            "api_key = '",
        ]
        found_patterns = [p for p in suspicious_patterns if p in source]
        if not found_patterns:
            record("no_hardcoded_secrets", True, "No hardcoded secret patterns detected")
        else:
            record("no_hardcoded_secrets", False, f"Suspicious patterns found: {found_patterns}")
    except Exception as e:
        record("no_hardcoded_secrets", False, f"Error scanning source: {e}")

    return results


# =============================================================================
# SECTION 4: REGISTRY CLIENT
# =============================================================================

def _get_token() -> str | None:
    """Get GitHub token from GITHUB_TOKEN env or gh CLI."""
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token
    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    return None


def _fetch_json(url: str, token: str = None) -> dict | None:
    """Fetch JSON from a URL with optional GitHub auth header."""
    try:
        req = urllib.request.Request(url)
        req.add_header("Accept", "application/json")
        if token:
            req.add_header("Authorization", f"Bearer {token}")
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode())
    except Exception:
        return None


def fetch_registry() -> dict:
    """Fetch registry.json from GitHub, falling back to local file."""
    url = f"{RAW_BASE}/registry.json"
    token = _get_token()
    data = _fetch_json(url, token)
    if data:
        return data

    # Fall back to local registry.json
    local = Path(__file__).parent / "registry.json"
    if local.exists():
        try:
            return json.loads(local.read_text())
        except json.JSONDecodeError:
            pass

    return {"agents": [], "stats": {}}


def search_agents(query: str) -> list[dict]:
    """Text search across name, display_name, description, tags, author, category."""
    registry = fetch_registry()
    agents = registry.get("agents", [])
    q = query.lower()
    results = []
    for agent in agents:
        searchable = " ".join([
            agent.get("name", ""),
            agent.get("display_name", ""),
            agent.get("description", ""),
            agent.get("author", ""),
            agent.get("category", ""),
            " ".join(agent.get("tags", [])),
        ]).lower()
        if q in searchable:
            results.append(agent)
    return results


def get_agent_info(name: str) -> dict | None:
    """Find an agent by exact name in the registry."""
    registry = fetch_registry()
    for agent in registry.get("agents", []):
        if agent.get("name") == name:
            return agent
    return None


def install_agent(name: str, output_dir: str = "agents") -> str:
    """Download an agent .py file from GitHub and write it to disk. Returns the output path."""
    agent = get_agent_info(name)
    if agent is None:
        raise ValueError(f"Agent '{name}' not found in registry")

    file_path = agent.get("_file")
    if not file_path:
        raise ValueError(f"No _file path recorded for '{name}'")

    url = f"{RAW_BASE}/{file_path}"
    token = _get_token()
    req = urllib.request.Request(url)
    if token:
        req.add_header("Authorization", f"Bearer {token}")

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read().decode()
    except Exception as e:
        raise RuntimeError(f"Failed to download agent: {e}")

    # Reconstruct output path relative to output_dir
    parts = Path(file_path).parts  # e.g. agents/@kody/my_agent.py
    if parts[0] == "agents":
        parts = parts[1:]  # strip leading "agents/"
    dest = Path(output_dir) / Path(*parts)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content)
    return str(dest)


# =============================================================================
# SECTION 5: CARD + BINDER OPERATIONS
# =============================================================================

def seed_hash(s: str) -> int:
    """Deterministic, reproducible hash for card generation."""
    h = 0
    for c in s:
        h = ((h << 5) - h + ord(c)) & 0xFFFFFFFF
    return h


def mulberry32(seed: int):
    """Return a callable PRNG producing 0.0–1.0 floats from a seed."""
    state = [seed & 0xFFFFFFFF]

    def _rand():
        state[0] = (state[0] + 0x6D2B79F5) & 0xFFFFFFFF
        z = state[0]
        z = ((z ^ (z >> 15)) * ((z | 1) & 0xFFFFFFFF)) & 0xFFFFFFFF
        z = ((z ^ (z >> 7)) * ((z | 61) & 0xFFFFFFFF)) & 0xFFFFFFFF
        z = (z ^ (z >> 14)) & 0xFFFFFFFF
        return z / 0xFFFFFFFF

    return _rand


_FLAVOR_FRAGMENTS = [
    "Built for the ecosystem. Ready for the edge.",
    "One file. Infinite possibilities.",
    "Runs anywhere the RAPP runtime breathes.",
    "Forged in the registry. Trusted in production.",
    "A single-file agent. A single promise: perform.",
    "When the network calls, this agent answers.",
    "Data in. Insight out. No drama.",
    "The pipeline starts here.",
]

_TYPE_PREFIXES = {
    "core": "Foundation",
    "pipeline": "Pipeline",
    "integrations": "Integration",
    "productivity": "Utility",
    "devtools": "DevTool",
    "general": "General",
    "b2b_sales": "B2B Sales",
    "b2c_sales": "B2C Sales",
    "healthcare": "Healthcare",
    "financial_services": "Financial",
    "manufacturing": "Industrial",
    "energy": "Energy",
    "federal_government": "Federal",
    "slg_government": "Government",
    "human_resources": "HR",
    "it_management": "IT Ops",
    "professional_services": "Professional",
    "retail_cpg": "Retail",
    "software_digital_products": "Software",
}


def mint_card(path: str) -> dict:
    """
    Extract manifest from an agent file and generate deterministic card data.
    Returns a dict with all card fields.
    """
    manifest = extract_manifest(path)
    if manifest is None:
        raise ValueError(f"No __manifest__ found in {path}")

    name = manifest.get("name", path)
    tier = manifest.get("quality_tier", "community")
    rarity = TIER_TO_RARITY.get(tier, "core")

    tags = manifest.get("tags", [])
    deps = manifest.get("dependencies", [])
    env_vars = manifest.get("requires_env", [])

    # Version → numeric multiplier
    version_str = manifest.get("version", "1.0.0")
    try:
        major = int(version_str.split(".")[0])
    except (ValueError, IndexError):
        major = 1

    power = len(tags) + len(deps)
    toughness = major * 2 + len(env_vars)

    # Deterministic flavor text and type line
    rng = mulberry32(seed_hash(name))
    flavor_idx = int(rng() * len(_FLAVOR_FRAGMENTS))
    flavor = _FLAVOR_FRAGMENTS[flavor_idx]

    category = manifest.get("category", "general")
    type_prefix = _TYPE_PREFIXES.get(category, "Agent")
    type_line = f"{type_prefix} Agent — {rarity.title()}"

    return {
        "name": name,
        "display_name": manifest.get("display_name", name),
        "version": manifest.get("version", "1.0.0"),
        "tier": tier,
        "rarity": rarity,
        "rarity_label": RARITY_LABELS.get(rarity, rarity),
        "power": power,
        "toughness": toughness,
        "category": category,
        "type_line": type_line,
        "flavor": flavor,
        "tags": tags,
        "description": manifest.get("description", ""),
        "author": manifest.get("author", ""),
        "floor_pts": RARITY_FLOOR.get(rarity, 10),
    }


def card_value(name: str) -> dict:
    """Fetch registry, find agent, compute floor value based on tier."""
    registry = fetch_registry()
    agent = None
    for a in registry.get("agents", []):
        if a.get("name") == name:
            agent = a
            break

    if agent is None:
        return {"error": f"Agent '{name}' not found in registry"}

    tier = agent.get("quality_tier", "community")
    rarity = TIER_TO_RARITY.get(tier, "core")
    floor_pts = RARITY_FLOOR.get(rarity, 10)

    # Floor BTC: 1 BTC = ~10,000,000 pts (illustrative peg)
    floor_btc = round(floor_pts / 10_000_000, 8)

    return {
        "name": name,
        "display_name": agent.get("display_name", name),
        "tier": tier,
        "rarity": rarity,
        "rarity_label": RARITY_LABELS.get(rarity, rarity),
        "floor_pts": floor_pts,
        "floor_btc": floor_btc,
    }


def binder_status() -> dict:
    """Check local registry.json and count agents by tier, computing total binder value."""
    local = Path(__file__).parent / "registry.json"
    if not local.exists():
        return {"error": "No local registry.json found. Run build_registry.py first."}

    try:
        registry = json.loads(local.read_text())
    except json.JSONDecodeError as e:
        return {"error": f"Failed to parse registry.json: {e}"}

    agents = registry.get("agents", [])
    by_tier: dict[str, list] = {}
    total_pts = 0

    for agent in agents:
        tier = agent.get("quality_tier", "community")
        by_tier.setdefault(tier, []).append(agent.get("name", ""))
        rarity = TIER_TO_RARITY.get(tier, "core")
        total_pts += RARITY_FLOOR.get(rarity, 10)

    summary = {tier: len(names) for tier, names in by_tier.items()}
    total_btc = round(total_pts / 10_000_000, 8)

    return {
        "total_agents": len(agents),
        "by_tier": summary,
        "total_pts": total_pts,
        "total_btc": total_btc,
        "registry_generated_at": registry.get("generated_at", "unknown"),
    }


def binder_transfer(mint_id: str, dest: str) -> dict:
    """Create a signed transfer intent for a card in the binder."""
    import time

    timestamp = int(time.time())
    payload = f"{mint_id}:{dest}:{timestamp}"
    digest = hashlib.sha256(payload.encode()).hexdigest()

    return {
        "action": "transfer",
        "mintId": mint_id,
        "to": dest,
        "timestamp": timestamp,
        "hash": digest,
    }


# =============================================================================
# SECTION 6: CLI DISPATCHER
# =============================================================================

def scaffold_agent(name: str) -> str:
    """
    Scaffold a new agent from template.
    name should be @publisher/my-agent.
    Returns the path to the written file.
    """
    if not name.startswith("@") or "/" not in name:
        raise ValueError(f"Name must be @publisher/slug, got: {name}")

    publisher, slug = name.split("/", 1)

    # class_name: "my-agent" -> "MyAgent"
    class_name = "".join(word.title() for word in slug.replace("-", "_").split("_"))

    # display_name: "my-agent" -> "My Agent"
    display_name = slug.replace("-", " ").replace("_", " ").title()

    description = "A RAPP agent."
    author = publisher.lstrip("@")

    file_name = slug.replace("-", "_") + "_agent.py"
    output_path = Path(__file__).parent / "agents" / publisher / file_name

    content = (
        AGENT_TEMPLATE
        .replace("__NAME__", name)
        .replace("__DISPLAY_NAME__", display_name)
        .replace("__CLASS_NAME__", class_name)
        .replace("__DESCRIPTION__", description)
        .replace("__AUTHOR__", author)
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content)
    return str(output_path)


def _fmt_test_results(results: list[tuple[str, bool, str]], use_json: bool) -> str:
    if use_json:
        return json.dumps([
            {"test": name, "passed": passed, "message": msg}
            for name, passed, msg in results
        ], indent=2)

    lines = []
    passed_count = sum(1 for _, p, _ in results if p)
    total = len(results)
    for name, passed, msg in results:
        icon = "PASS" if passed else "FAIL"
        lines.append(f"  [{icon}] {name:<28} {msg}")
    lines.append(f"\n  {passed_count}/{total} tests passed")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        prog="rapp_sdk",
        description="RAPP Foundation SDK — Build agents, mint cards, track Binders.",
    )
    parser.add_argument("--version", action="version", version=f"rapp_sdk {__version__}")

    sub = parser.add_subparsers(dest="command", metavar="<command>")

    # new
    p_new = sub.add_parser("new", help="Scaffold a new agent from template")
    p_new.add_argument("name", help="Agent name: @publisher/my-agent")
    p_new.add_argument("--json", action="store_true", help="Output JSON")

    # validate
    p_val = sub.add_parser("validate", help="Validate an agent manifest")
    p_val.add_argument("path", help="Path to agent .py file")
    p_val.add_argument("--json", action="store_true", help="Output JSON")

    # test
    p_test = sub.add_parser("test", help="Run contract tests against an agent file")
    p_test.add_argument("path", help="Path to agent .py file")
    p_test.add_argument("--json", action="store_true", help="Output JSON")

    # search
    p_search = sub.add_parser("search", help="Search the agent registry")
    p_search.add_argument("query", help="Search query")
    p_search.add_argument("--json", action="store_true", help="Output JSON")

    # install
    p_install = sub.add_parser("install", help="Download an agent from the registry")
    p_install.add_argument("name", help="Agent name: @publisher/my-agent")
    p_install.add_argument("--output-dir", default="agents", help="Output directory (default: agents)")
    p_install.add_argument("--json", action="store_true", help="Output JSON")

    # info
    p_info = sub.add_parser("info", help="Show details for an agent")
    p_info.add_argument("name", help="Agent name: @publisher/my-agent")
    p_info.add_argument("--json", action="store_true", help="Output JSON")

    # card
    p_card = sub.add_parser("card", help="Card operations")
    card_sub = p_card.add_subparsers(dest="card_command", metavar="<subcommand>")

    p_card_mint = card_sub.add_parser("mint", help="Mint a card from an agent file")
    p_card_mint.add_argument("path", help="Path to agent .py file")
    p_card_mint.add_argument("--json", action="store_true", help="Output JSON")

    p_card_value = card_sub.add_parser("value", help="Check the floor value of an agent card")
    p_card_value.add_argument("name", help="Agent name: @publisher/my-agent")
    p_card_value.add_argument("--json", action="store_true", help="Output JSON")

    # binder
    p_binder = sub.add_parser("binder", help="Binder operations")
    binder_sub = p_binder.add_subparsers(dest="binder_command", metavar="<subcommand>")

    p_binder_status = binder_sub.add_parser("status", help="Show binder inventory")
    p_binder_status.add_argument("--json", action="store_true", help="Output JSON")

    p_binder_transfer = binder_sub.add_parser("transfer", help="Transfer a card to another address")
    p_binder_transfer.add_argument("id", help="Mint ID of the card")
    p_binder_transfer.add_argument("to", help="Destination address")
    p_binder_transfer.add_argument("--json", action="store_true", help="Output JSON")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    use_json = getattr(args, "json", False)

    # ---- new ----
    if args.command == "new":
        try:
            out_path = scaffold_agent(args.name)
            if use_json:
                print(json.dumps({"created": out_path}))
            else:
                print(f"Created: {out_path}")
        except Exception as e:
            if use_json:
                print(json.dumps({"error": str(e)}))
            else:
                print(f"Error: {e}")
            sys.exit(1)

    # ---- validate ----
    elif args.command == "validate":
        errors = validate_manifest(args.path)
        manifest = extract_manifest(args.path)
        if use_json:
            print(json.dumps({"path": args.path, "valid": len(errors) == 0, "errors": errors}))
        else:
            if not errors:
                name = manifest.get("name", args.path) if manifest else args.path
                tier = manifest.get("quality_tier", "community") if manifest else "?"
                print(f"  Valid: {name}  [{tier}]")
            else:
                print(f"  Invalid: {args.path}")
                for e in errors:
                    print(f"    - {e}")
                sys.exit(1)

    # ---- test ----
    elif args.command == "test":
        results = run_contract_tests(args.path)
        output = _fmt_test_results(results, use_json)
        print(output)
        failed = [r for r in results if not r[1]]
        if failed:
            sys.exit(1)

    # ---- search ----
    elif args.command == "search":
        agents = search_agents(args.query)
        if use_json:
            print(json.dumps(agents, indent=2))
        else:
            if not agents:
                print(f"  No agents found matching '{args.query}'")
            else:
                print(f"  {len(agents)} result(s) for '{args.query}':\n")
                for a in agents:
                    tier = a.get("quality_tier", "community")
                    cat = a.get("category", "")
                    print(f"  {a['name']:<45} [{tier:<11}]  {cat}")
                    print(f"    {a.get('description', '')}")

    # ---- install ----
    elif args.command == "install":
        try:
            path = install_agent(args.name, args.output_dir)
            if use_json:
                print(json.dumps({"installed": path}))
            else:
                print(f"  Installed: {path}")
        except Exception as e:
            if use_json:
                print(json.dumps({"error": str(e)}))
            else:
                print(f"  Error: {e}")
            sys.exit(1)

    # ---- info ----
    elif args.command == "info":
        agent = get_agent_info(args.name)
        if agent is None:
            if use_json:
                print(json.dumps({"error": f"Agent '{args.name}' not found"}))
            else:
                print(f"  Agent '{args.name}' not found in registry")
            sys.exit(1)
        if use_json:
            print(json.dumps(agent, indent=2))
        else:
            print(f"  Name:        {agent.get('name')}")
            print(f"  Display:     {agent.get('display_name')}")
            print(f"  Version:     {agent.get('version')}")
            print(f"  Author:      {agent.get('author')}")
            print(f"  Category:    {agent.get('category')}")
            print(f"  Tier:        {agent.get('quality_tier')}")
            print(f"  Description: {agent.get('description')}")
            tags = agent.get("tags", [])
            if tags:
                print(f"  Tags:        {', '.join(tags)}")
            deps = agent.get("dependencies", [])
            if deps:
                print(f"  Deps:        {', '.join(deps)}")

    # ---- card ----
    elif args.command == "card":
        if args.card_command == "mint":
            try:
                card = mint_card(args.path)
                if use_json:
                    print(json.dumps(card, indent=2))
                else:
                    print(f"  Card: {card['display_name']}")
                    print(f"  Type: {card['type_line']}")
                    print(f"  Rarity: {card['rarity_label']}  ({card['rarity']})")
                    print(f"  Power/Toughness: {card['power']}/{card['toughness']}")
                    print(f"  Floor: {card['floor_pts']} pts")
                    print(f"  Flavor: \"{card['flavor']}\"")
            except Exception as e:
                if use_json:
                    print(json.dumps({"error": str(e)}))
                else:
                    print(f"  Error: {e}")
                sys.exit(1)

        elif args.card_command == "value":
            result = card_value(args.name)
            if use_json:
                print(json.dumps(result, indent=2))
            else:
                if "error" in result:
                    print(f"  Error: {result['error']}")
                    sys.exit(1)
                print(f"  Agent:   {result['name']}")
                print(f"  Tier:    {result['tier']}")
                print(f"  Rarity:  {result['rarity_label']}  ({result['rarity']})")
                print(f"  Floor:   {result['floor_pts']} pts  /  {result['floor_btc']} BTC")
        else:
            p_card.print_help()

    # ---- binder ----
    elif args.command == "binder":
        if args.binder_command == "status":
            status = binder_status()
            if use_json:
                print(json.dumps(status, indent=2))
            else:
                if "error" in status:
                    print(f"  Error: {status['error']}")
                    sys.exit(1)
                print(f"  Total agents: {status['total_agents']}")
                print(f"  By tier:")
                for tier, count in sorted(status["by_tier"].items()):
                    rarity = TIER_TO_RARITY.get(tier, "core")
                    label = RARITY_LABELS.get(rarity, rarity)
                    print(f"    {tier:<15} {count:>4} agents  ({label})")
                print(f"  Total value: {status['total_pts']} pts  /  {status['total_btc']} BTC")
                print(f"  Registry:    {status['registry_generated_at']}")

        elif args.binder_command == "transfer":
            result = binder_transfer(args.id, args.to)
            if use_json:
                print(json.dumps(result, indent=2))
            else:
                print(f"  Transfer Intent Created")
                print(f"  Mint ID:   {result['mintId']}")
                print(f"  To:        {result['to']}")
                print(f"  Timestamp: {result['timestamp']}")
                print(f"  Hash:      {result['hash']}")
        else:
            p_binder.print_help()


if __name__ == "__main__":
    main()
