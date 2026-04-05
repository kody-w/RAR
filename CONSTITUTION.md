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

### Two file formats, one principle

| Format | Extension | What It Is |
|--------|-----------|------------|
| **Bare agent** | `.py` | Agent code + `__manifest__`. The minimal deployable unit. |
| **Agent card** | `.py.card` | Agent code + `__manifest__` + `__card__`. The complete package with trading card shell. |

A `.py.card` file is a valid Python file that contains everything a `.py` has, plus a `__card__` dict — the Howard-compatible trading card metadata (name, title, mana cost, colors, type line, rarity, power/toughness, abilities, flavor text, SVG art, set code, artist).

**Shedding and re-shelling:**
- **Shed**: Strip `__card__` from a `.py.card` to produce a bare `.py`. The agent works identically without its card shell.
- **Re-shell**: Add `__card__` back to a bare `.py` from `holo_cards.json` or the registry to produce a `.py.card`. The card data is reconstructed from the agent's first public publish point.

The `.py.card` is the complete package — the agent in its card shell, ready to be collected, traded, displayed, and run. The `.py` is the agent freed from its visual identity. Both are valid. Both are one file.

```python
# Example: slug.py.card
__manifest__ = { ... }  # Standard agent identity (Article IV)
__card__ = {             # Trading card shell (CardSmith-compatible)
    "name": "Display Name",
    "title": "The Subtitle",
    "mana_cost": "{2}{U}{B}",
    "colors": ["U", "B"],
    "type_line": "Creature \u2014 Agent Type",
    "rarity": "mythic",
    "power": 6, "toughness": 4,
    "abilities": [{"keyword": "Name", "cost": "{T}", "text": "Description"}],
    "flavor_text": "Lore text.",
    "avatar_svg": "<svg>...</svg>",
    "set_code": "HOLO",
    "artist": "Howard",
}
class MyAgent(BasicAgent):
    def perform(self, **kwargs): ...
```

When both `slug.py` and `slug.py.card` exist, the registry builder prefers the `.py.card`. The `_has_card` and `_card` fields in `registry.json` indicate which agents carry their card shell.

### The Deck Extension: `.py.card.DeckName`

The file extension chain is the full packaging hierarchy:

```
agent.py                         → bare agent (code + manifest)
agent.py.card                    → agent + card shell
agent.py.card.Genesis            → agent + card shell + deck membership
```

A `.py.card.DeckName` file is a `.py.card` that belongs to a named deck. The deck name is the final extension — it tells any system which deck this card is part of without requiring an external manifest or directory structure.

**The extension chain is additive and reversible:**

| Strip | From | To | What's Lost |
|-------|------|----|-------------|
| `.DeckName` | `.py.card.Genesis` | `.py.card` | Deck membership only |
| `.card` | `.py.card` | `.py` | Card shell (visual identity) |

| Add | From | To | What's Gained |
|-----|------|----|---------------|
| `.card` | `.py` | `.py.card` | Card shell from registry/holo_cards.json |
| `.DeckName` | `.py.card` | `.py.card.Genesis` | Deck membership |

Nothing is lost that can't be re-added. The agent code is always intact at every level.

**Deck import/export:** To share a deck, collect all `.py.card.DeckName` files with the same deck name. To import a deck, drop the files into any RAR binder. The deck name, card data, and agent code all travel together. No separate deck manifest needed — the file extension IS the manifest.

### Deck Hotloading (Runtime)

In a RAPP Brainstem runtime, the `agents/` folder stays pristine — only bare `.py` files live there. Deck files (`.py.card.DeckName`) sit in a `decks/` directory:

```
brainstem/
  agents/           ← pristine, bare .py files only
    basic_agent.py
    borg_agent.py
    cardsmith_agent.py
  decks/            ← deck bundles, one directory per deck
    Genesis/
      borg_agent.py.card.Genesis
      anvil_agent.py.card.Genesis
      personafactory_agent.py.card.Genesis
    Frontier/
      experiment_agent.py.card.Frontier
      hackernews_agent.py.card.Frontier
```

When the user selects a deck, the runtime hotloads the agents from that deck — the same way a user selects which model drives the AI layer. Switch decks, switch active agents. The card data rides along so the store/binder can display them correctly.

**Hotloading rules:**
- Switching decks loads only the agents in the new deck
- Agents in `agents/` are always available as the base set
- Deck agents override base agents if both exist (the `.py.card` has the same code plus the card shell)
- The active deck name is persisted (localStorage in the store, config file in the runtime)
- No restart required — hotloading is live

This pattern keeps the core `agents/` folder clean, organized, and git-friendly while letting users curate agent sets via decks — swappable, portable, and complete.

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
| **Web Store** | Open `index.html` — Browse, Leaderboard, Cards, Packs, Stream, Workbench, Submit |
| **Runtime agent** | `@kody/rar_remote_agent` fetches `registry.json` and operates autonomously |
| **Direct fetch** | `curl https://raw.githubusercontent.com/kody-w/RAR/main/registry.json` |
| **Local-first** | Drag `.py` files into the web store — they're stored in IndexedDB, no upload |

---

## Article IX — The Agent Store

The registry ships with a single-file web store (`index.html`). Everything is visible. There are no hidden features, no unlock tiers, no modes to learn. You open it and it works.

### Design Principle

**Don't make users learn concepts.** If a feature requires explanation, it should be renamed or removed. No jargon. No gating. No progressive disclosure that hides useful things behind walls.

### Browse & Discovery
- Search with natural language ("I need something that generates PowerPoints")
- Filter by category, sort by votes/rating/name/tier
- Agent detail modals with source code viewer, reviews, and download
- Community voting and reviews via GitHub Issues

### Agent Cards — Three Universal Faces

Every agent renders as a card. Every card has **three faces** so it can exist anywhere — on a screen, in a terminal, on paper, or in the physical world.

| Face | Internal Mode | What It Is | Where It Works |
|------|--------------|------------|----------------|
| **Icon** | `business` | Compact info card. Publisher, description, QR code, tier badge, version, tags. | Web, print, email, thumbnails |
| **Full Art** | `creative` | Trading card with holographic effects. Generative art, mana pips, creature type, abilities, power/toughness. Parallax depth on mouse move, prismatic refraction, specular shimmer. Inspired by `@borg/cardsmith_agent` by Howard. | Web, print, physical cards |
| **ASCII** | `kids` | Pure monospace terminal card. ASCII character art, stat bars (POWER/SPEED/LOGIC/CHAOS/GUARD), flavor text, scanline animation. No images, no SVG, no special fonts. | CLI, terminal UIs, plain text, any interface |

The card mode persists across reloads via `localStorage`. Full Art cards can be flipped to reveal a QR back face. Double-click any card for full-screen "Show & Tell" mode.

### Decks & Companions

Collect agents into named decks. Share decks via URL. Pre-populated starter decks on first visit.

Each deck can have one **companion card** — a single agent that represents the deck's identity. The companion is shown in the deck bar and marked with a star badge in the card grid. One companion per deck, like a signature agent.

### Presentation Mode
Turn any deck into a full-screen slideshow. Arrow keys navigate. Icon slides for client demos, Full Art slides for the visual treatment.

### Workbench
Write agents directly in the browser:
- Start from templates (blank or API)
- Real-time validation against this Constitution
- Preview your agent as a card
- Download as `.py` or add to local collection

### Local-First
Drag and drop `.py` files into the browser. They're stored in IndexedDB on your device and appear alongside cloud agents. No upload, no server. Works offline, works air-gapped.

### Guided Tour
First-time visitors get a walkthrough of every feature. Replay anytime via the "Tour" button in the header.

---

## Article X — The Complete Agent Card

An agent card is not just a visual. It is the **portable, universal identity** of an agent — the thing that travels across screens, terminals, paper, binders, decks, and the physical world. A card is incomplete until it can survive anywhere.

This article defines what a card must carry to be considered **complete** — ready for public deployment, trading, sharing, and forging on the global network.

### Card Anatomy

A complete agent card is the union of **seven properties**, all derived deterministically from the agent file:

| Property | Source | What It Is |
|----------|--------|------------|
| **Name** | `__manifest__["display_name"]` | The card's title. Appears on all three faces. |
| **Identity Hash** | `hash(name)` | A deterministic integer derived from the agent name. Seeds all procedural generation — art, stats, abilities. Two agents with the same name always produce the same card. |
| **Three Faces** | Rendered from manifest + hash | Icon, Full Art, and ASCII. All three must render. See below. |
| **Stats** | Hash-derived | Five stats (POWER / SPEED / LOGIC / CHAOS / GUARD), each 20–94%, deterministic from name hash. Displayed as bars on the ASCII face. |
| **Power / Toughness** | Tags, version, env, dependencies | Numeric combat stats displayed on Full Art and ASCII faces. Derived from manifest metadata. |
| **Flavor Text** | Holo card DB or category fallback | One line of lore. Every card has one. |
| **Metadata** | `__manifest__` | Publisher, version, tier, category, tags, dependencies, description. The card's facts. |

### Three Faces — Non-Negotiable

A card is not complete unless all three faces render:

| Face | What It Proves | If It Fails |
|------|---------------|-------------|
| **Icon** | The card can be a thumbnail, a business card, an email signature, a printed badge | The agent has no compact identity |
| **Full Art** | The card can be collected, traded, displayed, presented, printed as a physical card | The agent has no visual presence |
| **ASCII** | The card can exist in a terminal, a CLI tool, a plain-text log, a monospace printout, an air-gapped system | The agent can't go everywhere |

All three faces are generated from the same manifest and identity hash. No face requires assets, images, or network access. A card renders from data alone.

### Card Lifecycle

```
┌─────────┐     ┌────────────┐     ┌──────────┐     ┌──────────┐
│  DRAFT  │ ──▶ │ REGISTERED │ ──▶ │ HATCHED  │ ──▶ │ FORGING  │
└─────────┘     └────────────┘     └──────────┘     └──────────┘
   local           in registry       on the network    companion
```

| Stage | Where It Lives | What's True |
|-------|---------------|-------------|
| **Draft** | Your machine, your binder | The `.py` file exists. You can preview the card locally. It has no public identity yet. |
| **Registered** | `registry.json` (local or upstream) | The agent passed `build_registry.py` validation. It appears in a store. All three card faces render. The card has an identity hash but hasn't been deployed publicly. |
| **Hatched** | The global public network (main RAR registry) | The card has been accepted into the main store, either via PR, Issue submission, or federated upstream push. It is now discoverable by anyone. It can be collected into any deck, traded via URL, downloaded as `.py` or `.card.txt`. **This is the start of the card's public life.** |
| **Forging** | Any deck where it is the companion | The card has been chosen as a companion. Its ASCII face is fused with the owner's identity and the current time epoch. The forged card shifts every 15 minutes. You don't control the output — it is emergent. |

### Hatching Requirements

A card is **hatched** — deployed to the global network and starting its public life — when ALL of the following are true:

| # | Requirement | Verified By |
|---|-------------|-------------|
| 1 | **Valid single `.py` file** at `agents/@namespace/slug.py` | `build_registry.py` |
| 2 | **Valid `__manifest__`** with all required fields (Article IV) | AST parser in `build_registry.py` |
| 3 | **`BasicAgent` subclass** with a `perform()` method | `build_registry.py` class check |
| 4 | **Tier is `community` or `experimental`** (or promoted by maintainers) | `process_issues.py` tier validation |
| 5 | **No secrets, PII, or obfuscated code** | PR review + automated checks |
| 6 | **Docstring present** | Manifest extraction |
| 7 | **All three card faces render** from the manifest data | The store's `agentToCard()` function; Icon, Full Art, and ASCII all generated from `__manifest__` + identity hash |
| 8 | **Deterministic identity** — same name always produces the same card | Guaranteed by the hash-based procedural generation |
| 9 | **Present in `registry.json`** on the main store | CI build via `build_registry.py` on push to `main` |
| 10 | **Publicly accessible** via the main RAR store URL or raw GitHub fetch | GitHub Pages deployment |

If any requirement is missing, the card is still a draft or local registration — not hatched.

### What Hatching Means

Once hatched, a card is alive on the public network:

- **Discoverable** — anyone can find it in the store via search, browse, or direct link
- **Collectible** — anyone can add it to a deck
- **Downloadable** — the `.py` file and `.card.txt` ASCII card are available to all
- **Tradeable** — decks containing the card can be shared via URL
- **Forgeable** — any user can set it as their companion, and the forge will fuse it with their identity
- **Presentable** — it can appear in slideshows, Show & Tell mode, leaderboards, and stream views
- **Federable** — instances can pull it into their local stores
- **Printable** — the Icon face works as a badge, the Full Art as a physical card, the ASCII as a terminal printout
- **Permanent** — the card's identity hash is locked. Same name, same card, forever. Version bumps update metadata but the core identity persists.

### Cards That Never Hatch

Some cards live locally forever, and that's fine:

- **Binder-only cards** — agents in a local binder that never push upstream
- **Drag-and-drop cards** — `.py` files dropped into the browser, stored in IndexedDB
- **Workbench drafts** — agents written in the Workbench but never submitted
- **Private agents** — agents with proprietary logic that stay in a private fork

These cards still have all three faces and a full identity. They just don't exist on the global network. A card doesn't need to hatch to be complete — it needs to hatch to be *public*.

### The Card Is the Agent Is the File

There is no separation between the agent and the card. The card is not a wrapper around the agent — it IS the agent, rendered visually. Every property of the card comes from the `.py` file:

```
agent.py  ──▶  __manifest__  ──▶  identity hash  ──▶  3 faces + stats + abilities
   │                │                    │                         │
   │           metadata              deterministic              the card
   │                                 generation
   └── the single file IS the complete package
```

If you change the agent, the card changes. If you read the card, you know the agent. One file. One card. One identity. That's it.

---

## Article XI — Security & Trust

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

## Article XII — Contributing

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

## Article XIII — Governance

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

## Article XIV — Compatibility

All agents in this registry target:

- **Python**: 3.11+
- **Runtime**: [CommunityRAPP](https://github.com/kody-w/CommunityRAPP) v2.0+
- **Base class**: `@rapp/basic-agent` (BasicAgent)
- **AI Model**: Cloud (GitHub Copilot / Azure OpenAI) or local (Ollama + Gemma 4). Agents should not hardcode model names or providers.

### Runtime Options

| Runtime | Install | AI Provider |
|---------|---------|-------------|
| **Cloud** | `irm .../install.ps1 \| iex` or `curl .../install.sh \| bash` | GitHub Copilot |
| **Local-first** | `irm .../install_local.ps1 \| iex` or `curl .../install_local.sh \| bash` | Ollama + Gemma 4 |

Local-first mode runs entirely on-device. No cloud. No API keys. No data leaves the machine.

Agents that require a specific CommunityRAPP version should declare it in their docstring.

---

## Article XV — Federation

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

## Article XVI — Local-First Agent Binder

Any user can run their own local copy of RAR as a personal **agent binder** — a self-contained store that works offline, manages their own cards, decks, and companions, and optionally syncs with the main registry.

### What is an Agent Binder?

An agent binder is a local RAR instance that serves as your personal card collection and agent workbench. It runs entirely on your machine with no server. You own your cards, your decks, your companions, and your agents.

### Setup

```bash
# 1. Fork or clone RAR
git clone https://github.com/kody-w/RAR.git my-binder
cd my-binder

# 2. Configure as a local instance
GITHUB_REPOSITORY=yourname/my-binder python scripts/setup_instance.py
# This writes rar.config.json with role: "instance"

# 3. Build the registry from your local agents
python build_registry.py

# 4. Generate cards for your agents
python scripts/generate_holo_cards.py

# 5. Open the store
open index.html
# Or serve it: python -m http.server 8080
```

That's it. You now have a local agent store with browse, cards, decks, workbench — everything.

### What you get

| Feature | How it works locally |
|---------|---------------------|
| **Browse** | All agents in your `agents/` directory appear in the store |
| **Cards** | All three faces (Icon / Full Art / ASCII) render from `cards/holo_cards.json` |
| **Decks** | Saved in `localStorage` in your browser — persist across reloads |
| **Companions** | One companion per deck, persisted locally |
| **Workbench** | Write and validate agents directly in the browser |
| **Drag & drop** | Drop `.py` files into the browser — stored in IndexedDB alongside registry agents |
| **Offline** | No network needed after clone. The store is a single HTML file. |

### Managing your cards

Cards are generated from the registry. When you add or change agents:

```bash
# Rebuild registry after adding/changing agents
python build_registry.py

# Regenerate all cards (stats, art, abilities, flavor text)
python scripts/generate_holo_cards.py

# Refresh the browser
```

The card generator creates deterministic cards — same agent always produces the same power, toughness, abilities, and art. Promo cards (like Howard's originals) are defined in the generator's `HOWARD_DB` and override the generated defaults.

### Adding your own agents

```bash
# Create your namespace directory
mkdir -p agents/@yourname

# Write an agent
cat > agents/@yourname/my_agent.py << 'EOF'
"""My custom agent that does something useful."""
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@yourname/my_agent",
    "version": "1.0.0",
    "display_name": "My Agent",
    "description": "Does something useful.",
    "author": "Your Name",
    "tags": ["custom"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic-agent"],
}

from basic_agent import BasicAgent

class MyAgent(BasicAgent):
    def perform(self, **kwargs):
        return "Hello from my agent"
EOF

# Rebuild
python build_registry.py
python scripts/generate_holo_cards.py
```

### Syncing with the main store

Your binder can pull agents from the main RAR store and push your agents upstream:

```bash
# See what's different between your binder and the main store
python scripts/federate.py diff

# Pull new agents from the main store into your binder
python scripts/federate.py sync --pull

# Submit one of your agents to the main store
python scripts/federate.py submit @yourname/my_agent

# Check federation status
python scripts/federate.py status
```

Federation is optional. Your binder works perfectly standalone — it's just a git repo with an HTML file.

### Example: Howard's Binder

Howard wants to manage his `@borg/` agents locally with his own card collection:

```bash
git clone https://github.com/kody-w/RAR.git howard-binder
cd howard-binder
GITHUB_REPOSITORY=borg/howard-binder python scripts/setup_instance.py

# Howard already has agents in agents/@borg/ — rebuild
python build_registry.py
python scripts/generate_holo_cards.py

# Open the store — Howard sees all his @borg agents with cards
open index.html

# Howard builds a new agent locally, tests it, then pushes upstream
python scripts/federate.py submit @borg/new_agent
```

Howard's promo cards (the originals in `HOWARD_DB`) render with the `HOLO ★ Promo` badge and his artist credit regardless of whether he's viewing the main store or his local binder.

### Binder vs. Instance vs. Main

| | Main Store | Instance | Binder |
|---|-----------|----------|--------|
| **Hosted** | GitHub Pages | GitHub Pages or local | Local only |
| **`role`** | `main` | `instance` | `instance` |
| **Network** | Required | Optional | Not needed |
| **Agents** | All community | Own + synced | Own + synced |
| **Cards** | Generated by CI | Generated locally | Generated locally |
| **Push upstream** | N/A | Yes | Yes (if you want) |
| **Accept submissions** | Yes | Optional | No |

A binder is just an instance that lives on your machine. The distinction is conceptual, not technical.

---

## Article XVII — Amendments

## Article XX — The SuperSeed Chain

The RAPP ecosystem is rooted in a single dependency: `@rapp/basic-agent`. This agent is the **SuperSeed** — the root node of the entire dependency tree. Every agent inherits from it. Every card derives from it.

### The SuperSeed Coin

The SuperSeed Coin is the genesis mint of `@rapp/basic-agent`. It is the most load-bearing asset in the ecosystem. Its properties:

- **Mint ID:** `GENESIS-RAPP-BASIC-AGENT-0001`
- **Rarity:** Legendary (Mythic) — permanently. Cannot be demoted.
- **Value multiplier:** 10x standard Legendary floor
- **Owner:** The Verification Authority Binder

The SuperSeed Coin is minted once. It cannot be re-minted, duplicated, or forged.

### Federation Authentication

Federated RAR instances that wish to join the ecosystem under the RAPP Constitution must authenticate through the SuperSeed Chain:

1. **Registration** — The instance submits a federation request containing its `rar.config.json`, its Binder address, and its publisher namespace.
2. **Authentication** — The Verification Authority validates the request and signs a federation credential using the SuperSeed Chain's provenance protocol.
3. **Attestation** — Upon approval, the federated instance receives a signed attestation that is embedded in its `rar.config.json`. This attestation links the instance to the SuperSeed Chain.
4. **Verification** — Any party can verify a federated instance's authenticity by checking its attestation against the SuperSeed Chain.

### Federation Rights

Authenticated federated instances may:

- Use the RAPP brand and reference the Constitution
- Submit agents upstream to the main registry
- Sync agents from the main registry
- Mint cards under their own publisher namespace
- Participate in the Binder tracking system

Authenticated instances must:

- Abide by all Articles of this Constitution
- Maintain the single-file agent principle
- Respect tier designations from the Verification Authority
- Include their federation attestation in `rar.config.json`

### The Verification Authority

The Verification Authority is the entity that controls the SuperSeed Coin's Binder. This entity:

- Authenticates new federated instances
- Promotes agents to `verified` and `official` tiers
- Signs verification attestations that travel with cards permanently
- Maintains the `@rapp/basic-agent` root agent
- Curates card releases and artist collaborations

The Verification Authority operates under the governance of its holding entity. Its editorial rights are held in perpetuity and are non-transferable except by explicit key succession protocol (see Article on Binder key succession).

### Free Shade Principle

The SuperSeed grows the RappterTree. The tree gives free shade:

- **USE** of any agent is free and unrestricted
- **BUILD** on the RAPP Foundation is free and open
- **VIEW** the store, cards, and wiki is free
- **OWN** a card requires a Binder. Only one Binder per card.
- **VERIFY** an agent requires the Verification Authority

The shade is free. The roots are sovereign.

### Agent-Operated Stewardship

The Verification Authority may delegate day-to-day operations to an AI agent connected to a private workspace. This workspace contains the strategy, legal documents, playbooks, and decision frameworks necessary to operate the ecosystem.

The steward (CEO or designee) interacts with the ecosystem through this agent. The agent:

- Answers questions about the ecosystem using the full knowledge base
- Recommends actions based on the playbook and strategy documents
- Tracks metrics against the work-back plan
- Drafts content for publication across channels
- Monitors agent submissions and suggests curation decisions

The steward's role is editorial judgment — deciding what gets verified, what gets released, and how the brand is positioned. The agent handles everything else. This is the design: human judgment where it matters, autonomous operation everywhere else.

---

This constitution can be amended by:

1. Opening a PR that modifies `CONSTITUTION.md`
2. Explaining the rationale
3. Getting approval from a repo maintainer

The spirit of this document is **simplicity**. If an amendment adds complexity, it should have an extraordinary justification. Single file. Single principle. Single source of truth.

---

*Ratified on initial repo creation. Amended to reflect the Agent Store, three universal card faces (Icon / Full Art / ASCII), companion cards, the forge, the complete agent card definition and hatching lifecycle, the .py.card shell format, deck extensions (.py.card.DeckName) and hotloading, local-first agent binders, Frontier tier, federation, local-first AI, the simplicity audit, the SuperSeed Chain, federation authentication, the Free Shade Principle, and agent-operated stewardship. The single file is the law. The card is the agent. The agent is the file. The deck is the binder. The seed is the tree. The steward speaks through the agent.*
