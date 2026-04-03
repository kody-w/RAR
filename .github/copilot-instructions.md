# Copilot Instructions — RAPP Agent Repo

## Architecture

This is the **open agent registry** for the [CommunityRAPP](https://github.com/kody-w/CommunityRAPP) ecosystem. It stores single-file Python agents under publisher namespaces and auto-generates a machine-readable `registry.json` index.

### Core principle: Single File Agent

Every agent is **one `.py` file** — no separate manifest, no README, no subdirectory. The `__manifest__` dict embedded in the file IS the package metadata. The docstring IS the documentation. See `CONSTITUTION.md` Article II for the full rationale.

### Key files

- `build_registry.py` — AST-parses all `.py` files under `agents/`, extracts `__manifest__` dicts, validates them, and writes `registry.json`. No imports or code execution.
- `registry.json` — **Auto-generated. Never hand-edit.** CI overwrites it on every push to `main`.
- `skill.md` — Machine-readable interface for AI agents to discover/install agents programmatically.
- `CONSTITUTION.md` — Governing document. Defines the single-file principle, namespace rules, quality tiers, security requirements, and categories.

### Agent structure

```
agents/@publisher/agent-slug.py    ← entire package
```

Each agent file contains:
1. A docstring (serves as README)
2. A `__manifest__` dict (serves as package metadata)
3. A class inheriting `BasicAgent` from `@rapp/basic-agent`
4. A `perform(**kwargs)` method that returns a `str`

### Namespaces

- `@yourname/` — GitHub username, owned forever
- `@rapp/` — reserved for official base packages
- Slugs are lowercase kebab-case: `my-agent.py`

### Categories

`core` | `pipeline` | `integrations` | `productivity` | `devtools`

### Quality tiers

`community` → `verified` → `official` (promotion by maintainers)

## Build & Validate

```bash
# Validate all manifests and rebuild registry.json
python build_registry.py
```

This is the only build step. CI runs it on every push via `.github/workflows/build-registry.yml`.

## Testing

```bash
# Run all tests
pytest

# Run a single test file
pytest tests/test_registry_build.py
pytest tests/test_agent_contract.py

# Run a single test by name
pytest tests/test_agent_contract.py::test_has_manifest -k "agent-slug"
```

Tests are parametrized over all agent files under `agents/@aibast-agents-library/`. The `conftest.py` discovers agents, imports each via `importlib`, finds the `BasicAgent` subclass, and yields `(module, class, path)` tuples.

### Contract tests (`test_agent_contract.py`)

Each agent is validated for: manifest presence and required fields, `@publisher/slug` name format, `BasicAgent` inheritance, successful instantiation, `perform()` returns a non-empty string for all operations, and standalone execution (`python agent.py` exits 0).

## Agent `__manifest__` schema

Required fields: `schema`, `name`, `version`, `display_name`, `description`, `author`, `tags`, `category`.

Optional: `quality_tier` (default `community`), `requires_env` (list of env var names), `dependencies` (list of `@publisher/slug`).

```python
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@yourname/my-agent",
    "version": "1.0.0",
    "display_name": "MyAgent",
    "description": "One sentence.",
    "author": "Your Name",
    "tags": ["keyword1", "keyword2"],
    "category": "integrations",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic-agent"],
}
```

## Conventions

- **Agents return strings** — `perform()` always returns `str`, never other types.
- **No network calls in `__init__()`** — constructors must be fast for agent loading.
- **Secrets via env vars** — use `os.environ.get()`, declare in `requires_env`, never hardcode.
- **Handle missing env vars gracefully** — return an error message, don't crash.
- **Imports use CommunityRAPP paths** — e.g., `from agents.basic_agent import BasicAgent`, `from utils.storage_factory import get_storage_manager`.
- **`display_name` must match `self.name`** in the agent class.
- **Semver versioning** — bump version in `__manifest__` on updates.

## Python

- **Version**: 3.11+ (required for Azure Functions v4)
- **AI model**: Azure OpenAI — agents should not hardcode model names.
