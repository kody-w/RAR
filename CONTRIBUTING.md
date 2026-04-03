# Contributing an Agent

## Quick Version

```
1. Fork this repo
2. Create: agents/@yourname/my-agent.py    ← single file, that's it
3. Include: __manifest__ dict in the file
4. Run:    python build_registry.py (must pass)
5. PR:     Open pull request
```

---

## The Single File Principle

Every agent is **one `.py` file**. No manifest.json. No README.md. No subdirectory. The metadata lives inside the Python file as a `__manifest__` dict.

```
agents/@yourname/my-agent.py    ← this is the entire package
```

## Namespace Rules

Your namespace is `@yourgithubusername`. This is yours forever.

- `@yourname/agent-slug.py` — use lowercase kebab-case for filenames
- One agent per file
- Slugs must be unique within YOUR namespace (not globally)
- `@rapp/` is reserved for official base packages

## Agent Template

```python
"""
My Agent — What it does in one line.

Longer description of what this agent does,
how to use it, and any important notes.
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@yourname/my-agent",
    "version": "1.0.0",
    "display_name": "MyAgent",
    "description": "What this agent does in one sentence.",
    "author": "Your Name",
    "tags": ["category", "keyword1", "keyword2"],
    "category": "integrations",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic-agent"],
}
# ═══════════════════════════════════════════════════════════════

from agents.basic_agent import BasicAgent


class MyAgent(BasicAgent):
    def __init__(self):
        self.name = __manifest__["display_name"]
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "input": {
                        "type": "string",
                        "description": "Input parameter"
                    }
                },
                "required": ["input"]
            }
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs):
        input_data = kwargs.get('input', '')
        return f"Result: {input_data}"
```

### Quality Tiers

| Tier | Who | Meaning |
|------|-----|---------|
| `community` | Anyone | Submitted, basic validation passes |
| `verified` | Reviewed by maintainer | Tested, follows standards, no security issues |
| `official` | Core team | Maintained by RAPP core, guaranteed compatibility |

New submissions start at `community`. Maintainers upgrade to `verified` after review.

## agent.py Requirements

The `__manifest__` dict is the **only** metadata requirement. The registry builder (`build_registry.py`) uses AST parsing to extract it — no imports or execution needed.

```python
from agents.basic_agent import BasicAgent

class MyAgent(BasicAgent):
    def __init__(self):
        self.name = 'MyAgent'  # Must match manifest display_name
        self.metadata = {
            "name": self.name,
            "description": "What this agent does",
            "parameters": {
                "type": "object",
                "properties": { ... },
                "required": [...]
            }
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs):
        # Your logic
        return "result string"
```

### Rules

1. **Single file** — everything in one `agent.py`
2. **Inherits `BasicAgent`** — the only hard dependency
3. **Returns a string** — always
4. **No secrets in code** — use `os.environ.get()` and declare in `requires_env`
5. **Works offline** — handle missing env vars gracefully (return error message, don't crash)
6. **No network calls in `__init__`** — keep constructor fast for agent loading

## Versioning

Use [semantic versioning](https://semver.org/):

- **MAJOR** (2.0.0) — breaking changes to `perform()` signature or metadata schema
- **MINOR** (1.1.0) — new features, new parameters (backward compatible)
- **PATCH** (1.0.1) — bug fixes, documentation

When you update, bump the version in `__manifest__`. The registry tracks all versions.

## Categories

| Category | For agents that... | Examples |
|----------|-------------------|----------|
| `core` | Provide fundamental capabilities | Memory, orchestration, library management |
| `pipeline` | Build, generate, or deploy other agents | RAPP pipeline, generators, transpilers |
| `integrations` | Connect to external systems | Dynamics 365, SharePoint, Salesforce, ServiceNow |
| `productivity` | Create content or automate tasks | PowerPoint, diagrams, email, demos |
| `devtools` | Help developers | Base classes, testing, scaffolding |

## Validation

Before submitting, run the registry builder locally:

```bash
python build_registry.py
```

This validates your manifest.json and ensures the registry builds cleanly.

## PR Checklist

- [ ] `agents/@yourname/my-agent.py` file exists (single file!)
- [ ] `__manifest__` dict is present with all required fields
- [ ] Agent inherits from `BasicAgent`
- [ ] `python build_registry.py` passes with no errors
- [ ] No secrets, API keys, or customer data in code
- [ ] `requires_env` lists all needed environment variables
