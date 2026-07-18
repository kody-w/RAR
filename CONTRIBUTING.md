# Contributing an Agent

## Quick Version

```
1. Write your agent: agents/@yourname/my_agent.py  ← single file, that's it
2. Include: __manifest__ dict in the file
3. Test:   python rapp_sdk.py test agents/@yourname/my_agent.py
4. Submit: create a versioned GitHub Issue mutation with your code
5. Wait for validation → approval → receipt → card forge
```

---

## The Single File Principle

Every agent is **one `.py` file**. No manifest.json. No README.md. No subdirectory. The metadata lives inside the Python file as a `__manifest__` dict.

```
agents/@yourname/my_agent.py    ← this is the entire package
```

## Naming Rules

**snake_case everywhere. No dashes. No exceptions.**

- Filename: `my_agent.py` (not `my-agent.py`)
- Manifest name: `@yourname/my_agent` (not `@yourname/my-agent`)
- Dependencies: `@rapp/basic_agent` (not `@rapp/basic-agent`)

This is enforced by CI, the build, the tests, and the submission pipeline. Dashes are rejected at every layer.

## Namespace

Your namespace is `@yourgithubusername`. This is yours forever.

- One agent per file
- Slugs must be unique within YOUR namespace

## Agent Template

```python
"""My Agent — what it does in one sentence."""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@yourname/my_agent",
    "version": "1.0.0",
    "display_name": "My Agent",
    "description": "What this agent does in one sentence.",
    "author": "Your Name",
    "tags": ["keyword1", "keyword2"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent


class MyAgent(BasicAgent):
    def __init__(self):
        self.name = "MyAgent"
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {"type": "object", "properties": {}},
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs):
        return "result"


if __name__ == "__main__":
    print(MyAgent().perform())
```

Or scaffold it: `python rapp_sdk.py new @yourname/my_agent`

## How to Submit

### Option A: GitHub Issue (recommended)

Open an issue on `kody-w/RAR`:

**Title:** `[AGENT] @yourname/my_agent`

**Body:** paste your agent code (raw or in a ` ```python ``` ` block)

Versioned clients should use the `rar-change-request/1.0` envelope documented
in [`api.json`](api.json). The Issue author is the submitting identity; the
title is descriptive and never grants namespace ownership.

RAR is public. Issue bodies, attachment links, and unlisted Gist locators are
auditable but **not private**. Never submit secrets or personal data. Large
agents use a revision-pinned GitHub source URL plus SHA-256 because Issue bodies
cannot hold the largest single-file agents in the registry.

### Option B: SDK

```bash
python rapp_sdk.py submit agents/@yourname/my_agent.py
```

Pull requests remain welcome for registry tooling, tests, documentation, and
policy. Agent publication and lifecycle mutations must use the Issue/receipt
path above so canonical admitted bytes receive identity, review, and audit
evidence. Canonical bytes use `sha256-lf-v1`: UTF-8 source with CRLF replaced by
LF and no other normalization.

## What Happens After Submission

1. Pipeline validates identity, manifest, source hash, and preconditions
2. Exact bytes land at an Issue-specific immutable staging revision
3. Issue is labeled `pending-review` and stays open
4. An authorized maintainer approves that exact revision
5. Security, registry, card, and test gates run before any publication commit
6. Mutation and immutable receipt commit to `main`
7. Issue closes as `notarized` (or `deleted`) with receipt and commit IDs

**The forge decides your card.** You don't choose your types, stats, or abilities. The forge reads your manifest (category, tags, tier, dependencies) and computes the card deterministically.

## Updating an Existing Agent

Submit a new Issue with the updated code. Bump the version:

- `1.0.0` → `1.0.1` for bug fixes
- `1.0.0` → `1.1.0` for new features
- `1.0.0` → `2.0.0` for breaking changes

Same flow: staging → review → approval. The new version gets a new forged seed. The old seed still resolves to the old card forever.

## Reading and Deleting

Reads are static and headless through `registry.json` or:

```bash
python rapp_sdk.py info @yourname/my_agent
python rapp_sdk.py request-status 123
```

Deletion is an approved mutation, not history erasure:

```bash
python rapp_sdk.py delete @yourname/my_agent --reason "No longer maintained"
```

RAR removes the active file and writes a tombstone plus receipt. Restoring the
same identity requires a fresh Issue, a semantically higher version, and
another review.

## Rules

1. **Single file** — everything in one `.py`
2. **snake_case** — filenames, names, dependencies (no dashes)
3. **Inherits BasicAgent** — the only hard dependency
4. **Returns a string** — `perform()` always returns `str`
5. **No secrets in code** — use `os.environ.get()`, declare in `requires_env`
6. **Works offline** — handle missing env vars gracefully
7. **No network calls in `__init__`** — keep constructor fast
8. **Tool-safe runtime name** — `self.name` and `metadata["name"]` must match `^[A-Za-z0-9_-]+$`; keep spaces and punctuation in `display_name`

## Security

The following patterns are **rejected** automatically:

- `eval()`, `exec()`, `compile()` with exec mode
- `os.system()`, `subprocess.*`
- `__import__()`
- Hardcoded secrets (API key patterns)

## Quality Tiers

| Tier | Meaning | Card Stage |
|------|---------|------------|
| `community` | Passes validation. All new agents start here. | Base |
| `verified` | Reviewed by maintainer. Tested. Follows standards. | Evolved |
| `official` | Core team maintained. Guaranteed compatibility. | Legendary |

## Categories

| Category | For agents that... |
|----------|-------------------|
| `core` | Provide fundamental capabilities (memory, orchestration) |
| `pipeline` | Build, generate, chain, or deploy other agents |
| `integrations` | Connect to external systems (APIs, databases) |
| `productivity` | Create content or automate tasks |
| `devtools` | Help developers (testing, scaffolding, base classes) |

Industry verticals: `b2b_sales`, `b2c_sales`, `energy`, `federal_government`, `financial_services`, `general`, `healthcare`, `human_resources`, `it_management`, `manufacturing`, `professional_services`, `retail_cpg`, `slg_government`, `software_digital_products`.

## Validation

```bash
python rapp_sdk.py validate agents/@yourname/my_agent.py
python rapp_sdk.py test agents/@yourname/my_agent.py
python build_registry.py
```

All three must pass before submission.
