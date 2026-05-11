# Contributing an Agent

## Quick Version

```
1. Write your agent: agents/@yourname/my_agent.py  ← single file, that's it
2. Include: __manifest__ dict in the file
3. Test:   python rapp_sdk.py test agents/@yourname/my_agent.py
4. Submit: open a GitHub Issue with your code
5. Wait for review → approval → card forged → you're in the registry
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
        super().__init__(__manifest__["display_name"], {})

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

### Option B: SDK

```bash
python rapp_sdk.py submit agents/@yourname/my_agent.py
```

### Option C: Pull Request

```bash
git fork kody-w/RAR
# add agents/@yourname/my_agent.py
python build_registry.py  # must pass
# open PR
```

## What Happens After Submission

1. Pipeline validates manifest, enforces snake_case, runs security scan
2. Agent lands in `staging/` — NOT in the registry yet
3. Issue labeled `pending-review` and stays open
4. Admin reviews and adds `approved` label
5. Agent moves to `agents/`, seed is forged from your manifest, card self-assembles
6. Issue closed — your agent is in the registry with a permanent card identity

**The forge decides your card.** You don't choose your types, stats, or abilities. The forge reads your manifest (category, tags, tier, dependencies) and computes the card deterministically.

## Updating an Existing Agent

Submit a new Issue with the updated code. Bump the version:

- `1.0.0` → `1.0.1` for bug fixes
- `1.0.0` → `1.1.0` for new features
- `1.0.0` → `2.0.0` for breaking changes

Same flow: staging → review → approval. The new version gets a new forged seed. The old seed still resolves to the old card forever.

## Rules

1. **Single file** — everything in one `.py`
2. **snake_case** — filenames, names, dependencies (no dashes)
3. **Inherits BasicAgent** — the only hard dependency
4. **Returns a string** — `perform()` always returns `str`
5. **No secrets in code** — use `os.environ.get()`, declare in `requires_env`
6. **Works offline** — handle missing env vars gracefully
7. **No network calls in `__init__`** — keep constructor fast

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
