# RAPP Agent Repo Constitution

> The governing document for the RAPP Agent Registry. Read this before submitting or installing agents.

---

## Article I — Purpose

This repository is the **open agent registry** for the RAPP ecosystem. It is a single place where anyone can publish, discover, and install AI agents that run on [CommunityRAPP](https://github.com/kody-w/CommunityRAPP).

**One principle above all: Single File Agent.** Every agent is one `.py` file. The manifest lives inside it. The docstring is the documentation. There is nothing else.

The registry ships with a **zero-install web store** (`index.html`) that lets anyone browse, collect, build, and share agents from a browser — including offline.

---

## Article II — The Single File Principle

This is non-negotiable. It is the foundation of RAPP and the reason this ecosystem works.

### An agent is ONE file.

```
agents/@yourname/my_agent.py    ← this is the entire package
```

### Inside that file:

1. **A docstring** — serves as the README
2. **A `__manifest__` dict** — serves as the package metadata
3. **A class inheriting `BasicAgent`** — serves as the agent
4. **A `perform()` method** — serves as the entry point

### There is no:

- `manifest.json` — the manifest is `__manifest__` inside the `.py`
- `README.md` — the docstring is the readme
- `requirements.txt` — agents use what CommunityRAPP provides
- Subdirectory per agent — the file IS the package
- Multi-file agents — if it can't fit in one file, split it into two agents

**Why:** A single file can be fetched with one HTTP GET, installed with one file write, read by an LLM in one context window, understood by a human in one sitting, and printed on a trading card. This is the competitive advantage.

---

## Article III — Namespace Ownership

### Publishers

Every agent lives under a publisher namespace: `@publisher/agent_slug.py`

- **`@yourname`** = your GitHub username. You own it forever.
- **`@orgname`** = your GitHub org. The org owns it.
- **`@rapp`** = reserved for official base packages maintained by the core team.

### Rules

1. **Your namespace is yours** — no one else can publish under `@yourname/`
2. **Slugs use underscores** — `my_cool_agent.py`, not `MyCoolAgent.py` or `my-cool-agent.py`
3. **Slugs must be unique within your namespace** — not globally
4. **No squatting** — namespaces that sit empty for 6+ months may be reclaimed
5. **No impersonation** — `@microsoft/` requires proof of org membership

### Collision-free at any scale

10,000 publishers × 100 agents each = 1,000,000 agents with zero naming conflicts.

---

## Article IV — The Manifest

Every agent file must contain a `__manifest__` dict. The registry builder extracts it via AST parsing — no imports, no execution.

```python
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@yourname/my_agent",
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
```

### Required Fields

| Field | Rules |
|-------|-------|
| `schema` | Always `"rapp-agent/1.0"` |
| `name` | `@publisher/slug` — must match file path, underscores only |
| `version` | Semver: `MAJOR.MINOR.PATCH` |
| `display_name` | Must match `self.name` in the class |
| `description` | One sentence. Searchable. |
| `author` | Your name (not your namespace) |
| `tags` | List of lowercase keywords for search |
| `category` | One of the categories defined in Article VI |
| `quality_tier` | `frontier`, `community` (default), `verified`, or `official` |
| `requires_env` | List of env var names the agent needs. Empty = no config needed. |
| `dependencies` | Other `@publisher/slug` agents this depends on |

---

## Article V — Quality Tiers

| Tier | Display Name | Who Sets It | Meaning |
|------|-------------|-------------|---------|
| `experimental` | **Frontier** | Author on submission | Pushing the edge. May be evolving rapidly. |
| `community` | **Community** | Automatic on submission (default) | Passes `build_registry.py` validation. Not reviewed. |
| `verified` | **Verified** | Repo maintainer | Reviewed, tested, follows standards, no security issues. |
| `official` | **Official** | RAPP core team | Maintained by core team. Guaranteed compatibility. SLA on bugs. |

> **Note:** The internal tier value is `experimental` but the UI displays it as **Frontier**. Use `"quality_tier": "experimental"` in manifests.

### Submittable tiers

Only `experimental` and `community` tiers can be used when submitting agents. The `verified` and `official` tiers are assigned by maintainers and the core team respectively — they cannot be self-assigned.

### Promotion path

```
frontier → community → verified → official
```

1. Submit with `"quality_tier": "experimental"` → visible as Frontier, not counted in main stats
2. Author stabilizes, bumps tier to `community` in a new version → standard submission
3. Maintainer reviews → tests pass → real users confirm it works → promoted to `verified`
4. Core team adopts maintenance → promoted to `official`

### Frontier tier requirements

Agents submitted as `experimental` (Frontier) must still:
- Contain a valid `__manifest__` with all required fields
- Parse without syntax errors
- Follow the single-file principle
- Not contain secrets or PII

They are exempt from:
- Comprehensive error handling
- Full documentation in the docstring
- Stable `perform()` API (breaking changes allowed without major version bump)

### Demotion

Agents can be demoted if:
- They break on a new CommunityRAPP release and aren't fixed
- Security vulnerabilities are reported and not patched
- The author abandons the agent (no response to issues for 90 days)
- A `community` agent that consistently fails may be demoted to `experimental`

---

## Article VI — Categories

| Category | For agents that... |
|----------|-------------------|
| `core` | Provide fundamental capabilities — memory, orchestration, agent management |
| `pipeline` | Build, generate, transpile, or deploy other agents |
| `integrations` | Connect to external systems — Dynamics 365, SharePoint, Salesforce, ServiceNow |
| `productivity` | Create content or automate tasks — PowerPoint, diagrams, email, demos, cards |
| `devtools` | Help developers — base classes, testing utilities, scaffolding, workbench |
| `general` | Agents that don't fit neatly into the above — or span multiple categories |

Industry-specific categories are also supported:
`b2b_sales`, `b2c_sales`, `healthcare`, `financial_services`, `manufacturing`, `energy`, `federal_government`, `slg_government`, `human_resources`, `it_management`, `professional_services`, `retail_cpg`, `software_digital_products`

New categories can be proposed via PR to this file.

---

## Article VII — Versioning

Use [semantic versioning](https://semver.org/):

- **MAJOR** (2.0.0) — breaking change to `perform()` signature or metadata schema
- **MINOR** (1.1.0) — new features, new parameters (backward compatible)
- **PATCH** (1.0.1) — bug fixes

Bump the version in `__manifest__` when you update. The registry tracks the latest version from `main`.

---

## Article VIII — The Registry

`registry.json` is the machine-readable index of all agents. It is:

1. **Auto-generated** — by `build_registry.py` from `__manifest__` dicts in every `.py` file
2. **Built by CI** — GitHub Actions runs on every push to `main`
3. **Never hand-edited** — if you edit it manually, CI will overwrite it
4. **The source of truth** for programmatic discovery and installation

### How agents are discovered

| Method | How |
|--------|-----|
| **Web Store** | Open `index.html` — browse, search, filter, vote |
| **Brainstem** | `@kody/rar_remote_agent` fetches `registry.json` and operates autonomously |
| **Direct fetch** | `curl https://raw.githubusercontent.com/kody-w/RAR/main/registry.json` |
| **Local-first** | Drag `.py` files into the web store — they're stored in IndexedDB, no upload |

---

## Article IX — The Agent Store

The registry ships with a single-file web store (`index.html`) that provides:

### Browse & Discovery
- Search, filter by category, sort by votes/rating/name
- Agent detail modals with source code viewer
- Community voting and reviews via GitHub Issues

### Agent Cards
Every agent renders as a collectible card with two skins:

- **Business** — Clean professional card. Publisher, description, tier badge, version.
- **Holo** — Trading card with generative art, mana pips, creature type, abilities, power/toughness stats. Inspired by `@borg/cardsmith_agent` by Howard.

### Decks
Collect agents into named decks. "Client Demo", "Sales Stack", "My Builds". Share decks via URL. Pre-populated starter decks on first visit.

### Presentation Mode
Turn any deck into a full-screen slideshow. Arrow keys navigate. Business slides for client demos, Holo slides for the art treatment.

### Workbench
Write agents directly in the browser:
- Start from templates (blank or API)
- Real-time validation against this Constitution
- Preview your agent as a card
- Download as `.py` or add to local collection

### Local-First
Drag and drop `.py` files into the browser. They're stored in IndexedDB on your device and appear alongside cloud agents. No upload, no server. Works offline, works air-gapped.

### Guided Tour
First-time visitors get an 11-step walkthrough of every feature. Replay anytime via the "Tour" button in the header.

---

## Article X — Security & Trust

### Agents MUST NOT:

- Contain secrets, API keys, tokens, or credentials
- Include customer data, PII, or proprietary business logic
- Make network calls in `__init__()` — keep constructors fast
- Execute arbitrary code on import — only on explicit `perform()` calls
- Obfuscate code — all logic must be readable

### Agents MUST:

- Declare all required environment variables in `requires_env`
- Handle missing env vars gracefully (return error message, don't crash)
- Use `os.environ.get()` for configuration — never hardcode endpoints
- Be fully readable — no minification, no encoded payloads

### Review process

All PRs are reviewed. Agents that violate security rules are rejected. Repeat offenders lose publishing rights.

### Template guard

Unmodified starter templates (containing `@your-username/`) are rejected at three layers: browser validation, frontend submission, and backend `process_issues.py`.

---

## Article XI — Contributing

### Submit an agent (via the Web Store)

1. Open the **Workbench** tab — write or paste your agent
2. Click **Validate** — fix any errors
3. Click **Preview Card** — see how it looks
4. Switch to the **Submit** tab — paste your code and submit
5. GitHub Actions validates, writes the file, and closes the Issue

### Submit an agent (via PR)

```bash
1. Fork this repo
2. Create: agents/@yourname/my_agent.py
3. Include: __manifest__ dict + BasicAgent subclass
4. Validate: python build_registry.py
5. PR: Open pull request
```

### Submit an agent (via Issues-as-API)

The store frontend creates a GitHub Issue with a JSON payload:

```json
{
  "action": "submit_agent",
  "payload": {
    "code": "... your agent.py source code ..."
  }
}
```

GitHub Actions processes the Issue, validates the manifest, writes the file, and closes the Issue. This is the same mechanism used by federated instances to submit upstream.

### PR requirements

- [ ] Single `.py` file at `agents/@yourname/slug.py`
- [ ] `__manifest__` dict with all required fields
- [ ] Class inherits from `BasicAgent`
- [ ] `perform(**kwargs)` returns a string
- [ ] `python build_registry.py` passes
- [ ] No secrets or customer data
- [ ] Docstring explains what the agent does
- [ ] `quality_tier` is `community` or `experimental` (or omitted for default)

### Updating an existing agent

1. Bump `version` in `__manifest__`
2. Update the code
3. PR with description of what changed

---

## Article XII — Governance

### Maintainers

Maintainers can:
- Merge PRs
- Promote agents to `verified`
- Reject agents that violate this constitution
- Reclaim abandoned namespaces

### Disputes

- Naming disputes → first publisher wins
- Quality disputes → maintainer decision is final
- Security reports → immediate removal, notify author, 48h to fix

---

## Article XIII — Compatibility

All agents in this registry target:

- **Python**: 3.11+
- **Runtime**: [CommunityRAPP](https://github.com/kody-w/CommunityRAPP) v2.0+
- **Base class**: `@rapp/basic-agent` (BasicAgent)
- **AI Model**: Azure OpenAI (agents should not hardcode model names)

Agents that require a specific CommunityRAPP version should declare it in their docstring.

---

## Article XIV — Federation

RAR can be used as a **GitHub template repository**. Instances cloned from the template operate as independent agent stores that can optionally federate back to the main registry.

### Roles

| Role | Meaning |
|------|---------|
| `main` | The canonical RAPP Agent Store. Accepts federated submissions. |
| `instance` | A template-derived repo. Hosts its own agents. Can submit upstream. |

Roles are defined in `rar.config.json` under the `role` field.

### How federation works

1. **Clone the template** — A user creates a new repo from RAR. `rar.config.json` is auto-configured with `"role": "instance"` and `"upstream"` pointing to the main repo.
2. **Add agents locally** — The instance owner adds agents under their own namespace. These appear in the instance's own store.
3. **Submit upstream** — The instance can submit new or updated agents to the main store. Submissions use the same Issues-as-API pattern: a GitHub Issue is created on the upstream repo with `action: "submit_agent"` containing the agent code.
4. **Sync from upstream** — Instances can pull agents from the main store to expand their local catalog.

### Federation rules

- Instances can only submit agents under their own `@namespace/`
- The upstream repo decides whether to accept each submission (same validation rules apply)
- `verified` and `official` tiers cannot be submitted upstream — only `community` and `experimental`
- The main store is the source of truth for tier promotions
- Federation is opt-in: instances with `"allow_upstream_sync": false` operate independently

### Configuration

Federation behavior is controlled by `rar.config.json`:

```json
{
  "schema": "rar-config/1.0",
  "role": "instance",
  "owner": "your-github-username",
  "repo": "your-repo-name",
  "upstream": "kody-w/RAR",
  "federation": {
    "accept_submissions": false,
    "allow_upstream_sync": true
  }
}
```

---

## Article XV — Amendments

This constitution can be amended by:

1. Opening a PR that modifies `CONSTITUTION.md`
2. Explaining the rationale
3. Getting approval from a repo maintainer

The spirit of this document is **simplicity**. If an amendment adds complexity, it should have an extraordinary justification. Single file. Single principle. Single source of truth.

---

*Ratified on initial repo creation. Amended to reflect the Agent Store, Holo cards, and Frontier tier. The single file is the law.*
