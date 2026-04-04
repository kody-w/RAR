# RAR — RAPP Agent Registry

**The open single-file agent ecosystem.** Browse, build, collect, and share AI agents from your browser.

126 agents. 5 publishers. 19 categories. Every agent is one `.py` file.

**[Open the Agent Store](https://kody-w.github.io/RAR/)**

---

## What is this?

RAR is the package registry for [CommunityRAPP](https://github.com/kody-w/CommunityRAPP) agents. But unlike a typical registry, it ships with a complete web store — no install, no build step, just open `index.html`.

Every agent follows the **single-file principle**: one `.py` file with the manifest, documentation, and code all in one place. One HTTP GET to fetch. One file write to install. One context window for an LLM to read.

---

## The Agent Store

The store (`index.html`) is itself a single file. Open it in any browser — including from `file://`.

### Browse & Discover
Search 126 agents across 19 categories. Filter by tier. Sort by votes. Click any agent to see source code, reviews, and details.

### Agent Cards
Every agent is a collectible card. Two skins:
- **Business** — clean professional layout, like a business card you'd hand someone
- **Holo** — trading card with generative art, mana pips, creature types, abilities, and power/toughness (inspired by [@borg/cardsmith_agent](agents/@borg/cardsmith_agent.py))

### Decks & Presentation
Collect agents into named decks. "Client Demo", "Sales Stack", "My Builds". Share via URL. Hit **Present** to turn any deck into a full-screen slideshow — arrow keys to navigate, toggle between Business and Holo slides.

### Workbench
Write agents in your browser. Start from a template, validate against the [Constitution](CONSTITUTION.md), preview your agent as a card, download as `.py`, or add to your local collection.

### Local-First
Drag `.py` files into the browser. They're stored in IndexedDB on your device and appear alongside cloud agents. No upload, no server, no account. Works offline and air-gapped.

### Submit
Publish agents through the store UI — it creates a GitHub Issue that gets processed by automation. Your agent publishes under `@your-github-username/`.

---

## Install an Agent

### From the Store
Browse → Click an agent → Download `.py` → Drop it in your `agents/` folder.

### From Chat
The `@kody/rar_remote_agent` reads this registry autonomously:

> *"Install the dynamics-crud agent"*
> *"What agents are available for CRM?"*

### Direct Fetch
```bash
curl -O https://raw.githubusercontent.com/kody-w/RAR/main/agents/@kody/rar_remote_agent.py
```

---

## Quality Tiers

| Tier | Display | Meaning |
|------|---------|---------|
| `official` | **Official** | Core team maintained. Guaranteed compatibility. |
| `verified` | **Verified** | Reviewed by maintainers. Tested. Follows standards. |
| `community` | **Community** | Submitted by anyone. Passes automated validation. |
| `experimental` | **Frontier** | Pushing the edge. May evolve rapidly. |

Promotion path: **Frontier → Community → Verified → Official**

---

## Repo Structure

```
RAR/
├── agents/
│   ├── @rapp/basic-agent.py          # Base class (official)
│   ├── @kody/                         # Core agents (verified + community)
│   │   ├── rar_remote_agent.py        # Registry client
│   │   ├── agent_workbench_agent.py   # Build/validate/test agents
│   │   ├── context_memory.py          # Memory recall
│   │   ├── github_agent_library.py    # Agent discovery
│   │   └── manage_memory.py           # Memory storage
│   ├── @borg/cardsmith_agent.py       # Howard's card system
│   ├── @discreetRappers/              # 13 agents — pipeline, sales, integrations
│   └── @aibast-agents-library/        # 104 industry templates across 14 verticals
├── index.html                         # The Agent Store (single file, zero dependencies)
├── registry.json                      # Auto-generated agent index (CI builds on push)
├── build_registry.py                  # AST-based manifest extractor
├── CONSTITUTION.md                    # Governing document
├── rar.config.json                    # Federation and feature config
├── scripts/process_issues.py          # Issues-as-API processor
└── .github/workflows/                 # CI automation
```

---

## Federation

RAR is a **GitHub template repository**. Clone it to run your own agent store. Your instance can:

- Host agents under your own namespace
- Submit agents upstream to the main store
- Pull agents from the main store
- Operate independently with `"allow_upstream_sync": false`

See [CONSTITUTION.md — Article XIV](CONSTITUTION.md#article-xiv--federation) for details.

---

## Contributing

The fastest path:

1. Open the [Agent Store](https://kody-w.github.io/RAR/)
2. Go to **Workbench** — write or paste your agent
3. Click **Validate** — fix any errors
4. Switch to **Submit** — publish

Or via PR:

```bash
1. Fork this repo
2. Create: agents/@yourname/my_agent.py
3. Include: __manifest__ + BasicAgent subclass + perform()
4. Validate: python build_registry.py
5. PR: Open pull request
```

Read the full rules in [CONSTITUTION.md](CONSTITUTION.md).

---

## Publishers

| Publisher | Agents | Focus |
|-----------|--------|-------|
| **@aibast-agents-library** | 104 | Industry vertical templates (14 verticals) |
| **@discreetRappers** | 13 | Pipeline, integrations, sales, productivity |
| **@kody** | 6 | Core infrastructure, registry client, workbench, Rappterbook |
| **@borg** | 2 | Borg assimilator + CardSmith (Howard Hoy) |
| **@rapp** | 1 | BasicAgent base class |

---

## License

[MIT](LICENSE)

---

*Single file. Single principle. Single source of truth.*
