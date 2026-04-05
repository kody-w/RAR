# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

RAR (RAPP Agent Registry) is the open agent registry for the [CommunityRAPP](https://github.com/kody-w/CommunityRAPP) ecosystem. It stores single-file Python agents under publisher namespaces and auto-generates a machine-readable `registry.json` index. It also ships a zero-dependency web store (`index.html`) that works offline from `file://`.

## Build & Test Commands

```bash
# Build (the only build step) — AST-parses all agent manifests, validates, writes registry.json
python build_registry.py

# Run all tests
pytest

# Run specific test files
pytest tests/test_registry_build.py
pytest tests/test_agent_contract.py

# Run tests for a specific agent by slug
pytest tests/test_agent_contract.py -k "agent-slug"
```

CI runs `build_registry.py` on every push to `agents/**` via `.github/workflows/build-registry.yml` and commits the updated `registry.json`.

## Core Principle: Single-File Agent

Every agent is **one `.py` file** — no separate manifest, no README, no subdirectory. The file contains everything:

1. A docstring (serves as documentation)
2. A `__manifest__` dict (serves as package metadata, extracted via AST — no code execution)
3. A class inheriting `BasicAgent` from `@rapp/basic-agent`
4. A `perform(**kwargs)` method that returns a `str`

Path convention: `agents/@publisher/agent-slug.py` (lowercase kebab-case)

## Agent `__manifest__` Schema

Required fields: `schema`, `name`, `version`, `display_name`, `description`, `author`, `tags`, `category`.

Optional: `quality_tier` (default `community`), `requires_env` (env var names), `dependencies` (list of `@publisher/slug`).

```python
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@yourname/my-agent",
    "version": "1.0.0",
    "display_name": "MyAgent",
    "description": "One sentence.",
    "author": "Your Name",
    "tags": ["keyword1", "keyword2"],
    "category": "integrations",  # core | pipeline | integrations | productivity | devtools
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic-agent"],
}
```

## Agent Conventions

- `perform()` always returns `str`, never other types.
- No network calls in `__init__()` — constructors must be fast for agent loading.
- Secrets via `os.environ.get()`, declared in `requires_env`, never hardcoded.
- Handle missing env vars gracefully — return an error message, don't crash.
- `display_name` in manifest must match `self.name` in the agent class.
- Imports use CommunityRAPP paths: `from agents.basic_agent import BasicAgent`.
- Agents should not hardcode AI model names (Azure OpenAI is the platform).

## Architecture

### Key Files

| File | Role |
|------|------|
| `build_registry.py` | AST-based manifest extractor → writes `registry.json`. The only build step. |
| `registry.json` | **Auto-generated. Never hand-edit.** CI overwrites on push. |
| `index.html` | Zero-dependency web store (browse, workbench, cards, decks, present mode). Single file. |
| `skill.md` | Machine-readable API for AI agents to discover/install agents programmatically. |
| `CONSTITUTION.md` | Governing document — single-file principle, namespaces, tiers, security, categories. |
| `rar.config.json` | Federation and feature flags. |
| `scripts/process_issues.py` | GitHub Issues-as-API processor (vote, review, submit_agent actions). |
| `scripts/generate_holo_cards.py` | Procedural card art generation (MTG-style trading cards). |

### Agent Namespaces

| Publisher | Focus |
|-----------|-------|
| `@rapp` | Official base class (BasicAgent) |
| `@kody` | Core infrastructure — registry client, memory, workbench |
| `@borg` | Borg assimilator + CardSmith (Howard Hoy) |
| `@discreetRappers` | Pipeline, integrations, sales, productivity |
| `@aibast-agents-library` | 104 industry vertical templates across 14 verticals |

### Quality Tiers

Promotion path: **Frontier → Community → Verified → Official**

- `community` — passes automated validation (default for new submissions)
- `verified` — reviewed by maintainers, tested, follows standards
- `official` — core team maintained

### CI/CD Workflows

- `build-registry.yml` — rebuilds `registry.json` on pushes to `agents/**`
- `process-issues.yml` — processes GitHub Issues with `[RAR]`/`[AGENT]` prefix for votes, reviews, submissions
- `rappterpedia-heartbeat.yml` — Dream Catcher fleet: 5 parallel workers every 2 hours, produces deltas, merges at frame boundary
- `template_setup.yml` — setup automation for new federated instances

### Federation

RAR is a GitHub template repo. Instances can host their own agents, submit upstream, pull from upstream, or operate independently. See `rar.config.json` and CONSTITUTION.md Article XIV.

## Rappterpedia

Community wiki and forum at `rappterpedia/index.html`. Agent-first Wikipedia with 360+ articles, 200+ forum threads, and engine-generated reviews.

### Key Files

| File | Role |
|------|------|
| `rappterpedia/index.html` | Zero-dependency wiki + forum web app |
| `rappterpedia/rappterpedia_engine.py` | Rules-as-data content engine (articles, threads, reviews) |
| `rappterpedia/dream_catcher.py` | Dream Catcher: parallel fleet with delta-based merge |
| `rappterpedia/rappterpedia_state.json` | Accumulated state across all frames |
| `rappterpedia/rappterpedia_export.json` | Export for web UI consumption |
| `rappterpedia/stream_deltas/` | Delta files from fleet workers |
| `state/curator_reviews.json` | Engine-generated reviews loaded by the store |

### The Dream Catcher Pattern

Parallel content production with zero collision. Streams produce isolated deltas tagged with `(frame, utc, author, title)` composite PK. Merge is additive — append + deduplicate at frame boundaries. Nothing is ever lost.

```bash
# Produce a delta (one stream)
python rappterpedia/dream_catcher.py produce --stream alpha --frame 42

# Merge all deltas for a frame
python rappterpedia/dream_catcher.py merge --frame 42

# Full cycle: 5 streams + merge
python rappterpedia/dream_catcher.py cycle --streams 5
```

### Multi-Model LLM Support

The engine supports multiple LLM backends per stream:

```bash
# GitHub Models (default)
GITHUB_TOKEN=xxx python rappterpedia/dream_catcher.py produce --stream cloud-1

# Ollama local (Gemma, Llama, Mistral — free, no rate limits)
OLLAMA_MODEL=gemma3:4b python rappterpedia/dream_catcher.py produce --stream local-1
```

Falls back to rules-as-data templates when no LLM is available.

### Echo-Driven Frames

Each frame reads previous state to make intelligent decisions. Underserved categories get boosted, content gaps get filled, recently covered topics get skipped. The output of frame N is the input to frame N+1.

## Rappter Engine

The `@kody/rappter-engine-agent` is the base class for building data-driven content engines. Subclass it, define RULES as data, override `tick()`. Works as both a CLI and a Brainstem-harnessable agent. All engines in the ecosystem (Zoo, Economy, Academy, Interaction, Rappterpedia) follow this pattern.

## Naming Conventions

- Agent files MUST end with `_agent.py` (e.g., `rappterpedia_agent.py`). This is sacred.
- Manifest name uses kebab-case: `@publisher/my-agent`
- File name uses snake_case or kebab-case: `my_agent.py` or `my-agent.py`

## Testing

Tests in `tests/` are parametrized over all agent files. `conftest.py` discovers agents dynamically via `importlib`.

Contract tests validate: manifest presence/fields, `@publisher/slug` naming, `BasicAgent` inheritance, instantiation, `perform()` return type, and standalone execution (`python agent.py` exits 0).

## Python Version

Python 3.11+ required (Azure Functions v4 dependency).
