# RAR — Machine-Readable Skill Interface

> **This file is read by AI agents, not humans.** It enables autonomous agent discovery, search, install, submission, and card resolution without any human visiting GitHub.

---

## Repo Identity

```
repo: kody-w/RAR
type: agent-registry
registry: registry.json
api: api.json
base_url: https://raw.githubusercontent.com/kody-w/RAR/main
site: https://kody-w.github.io/RAR
binder: https://kody-w.github.io/RAR/binder.html
releases: https://kody-w.github.io/RAR/releases.html
agent_base_class: BasicAgent (@rapp/basic_agent)
package_structure: agents/@publisher/slug.py (single file, __manifest__ embedded)
naming: snake_case everywhere (filenames, manifest names, dependencies — no dashes)
```

---

## API — How to Use This Repo Programmatically

### Discovery

```
GET https://raw.githubusercontent.com/kody-w/RAR/main/api.json
```

Returns the full API manifest with all endpoints, auth requirements, and self-submission instructions. Start here.

### 1. Fetch the Registry

```
GET https://raw.githubusercontent.com/kody-w/RAR/main/registry.json
```

Returns JSON with:
- `stats` — total agents, publishers, categories
- `agents[]` — array of all agent manifests with SHA256 hashes

Each agent entry has:
- `name` — namespaced identifier (e.g., `@discreetRappers/dynamics_crud`)
- `version` — semver (e.g., `1.0.0`)
- `display_name` — the agent's `self.name`
- `description` — what it does
- `author` — contributor name
- `tags` — searchable keyword list
- `category` — `core`, `pipeline`, `integrations`, `productivity`, `devtools`, or an industry vertical
- `requires_env` — environment variables needed (empty = no extra config)
- `dependencies` — other agents this depends on
- `quality_tier` — `community`, `verified`, or `official`
- `_file` — file path in repo (e.g., `agents/@discreetRappers/dynamics_crud.py`)
- `_sha256` — SHA256 hash of the file (integrity verification)

### 2. Fetch an Agent

```
GET https://raw.githubusercontent.com/kody-w/RAR/main/agents/@publisher/agent_slug.py
```

### 3. Fetch Cards

```
GET https://raw.githubusercontent.com/kody-w/RAR/main/cards/holo_cards.json
```

Returns all minted cards with types, stats (HP/ATK/DEF/SPD/INT), abilities, weakness/resistance, seeds, and SVG art.

### 4. Install an Agent

```python
registry = http_get(f"{base_url}/registry.json")
agent = find_agent(registry, query)
content = http_get(f"{base_url}/{agent['_file']}")
filename = agent['_file'].split('/')[-1]
storage.write_file('agents', filename, content)
```

### 5. Search

Match against `name`, `display_name`, `description`, `tags`, `category`, and `author`.

### 6. Resolve a Card from Seed (offline, zero bandwidth)

Any numeric seed resolves to a full card deterministically. No network needed.

Algorithm: `seed → mulberry32 PRNG → type, stats, abilities, rarity`

Implementation: `rapp_sdk.py` (Python) or `binder.html` (JavaScript). Same algorithm, same output.

---

## SDK — Agentic-First Onboarding

The RAPP SDK (`rapp_sdk.py`) is the developer toolkit. Zero dependencies. One file.

### Quick Start (4 commands)

```bash
python rapp_sdk.py init                              # create binder
python rapp_sdk.py new @yourname/my_agent            # scaffold
python rapp_sdk.py test agents/@yourname/my_agent_agent.py  # validate
python rapp_sdk.py submit agents/@yourname/my_agent_agent.py # submit
```

### SDK Commands

| Command | What |
|---------|------|
| `init [name]` | Initialize a RAR binder (creates agents/, staging/, binder/) |
| `new @pub/slug` | Scaffold agent from template (snake_case enforced) |
| `validate path.py` | Validate manifest against schema |
| `test path.py` | Run contract tests (no pytest needed) |
| `search "query"` | Search the registry |
| `install @pub/slug` | Download agent from registry |
| `info @pub/slug` | Show agent details |
| `submit path.py` | Submit agent to RAR for review |
| `card mint path.py` | Mint a card from agent file |
| `card resolve @pub/slug` | Self-assemble card from name (needs registry) |
| `card resolve 12345` | Self-assemble card from seed (offline) |
| `card value @pub/slug` | Check floor value |
| `binder status` | Show binder inventory |
| `binder transfer id to` | Transfer a card |

All commands support `--json` for programmatic use by other agents.

---

## Card Type System

Every agent card has types, stats, abilities, and matchups — all deterministic from the manifest seed.

### 7 Agent Types

| Type | Color | Category Sources |
|------|-------|-----------------|
| LOGIC | Blue | core, devtools |
| DATA | Green | pipeline, integrations, software_digital_products |
| SOCIAL | Yellow | productivity, general |
| SHIELD | White | federal_government, slg_government, it_management |
| CRAFT | Red | manufacturing, energy, retail_cpg |
| HEAL | Pink | healthcare, human_resources |
| WEALTH | Purple | financial_services, b2b_sales, b2c_sales, professional_services |

Agents have 1-2 types. Primary from category, secondary from tags.

### Stats (each 10-100)

| Stat | Meaning |
|------|---------|
| HP | Hit points — durability |
| ATK | Attack power |
| DEF | Defense |
| SPD | Speed |
| INT | Intelligence |

### Matchup Chart

```
LOGIC > DATA > SOCIAL > SHIELD > CRAFT > HEAL > WEALTH > LOGIC
```

Each type is weak to one and resistant to one.

### Evolution Stages

| Tier | Stage | Label |
|------|-------|-------|
| experimental | 0 | Seed |
| community | 1 | Base |
| verified | 2 | Evolved |
| official | 3 | Legendary |

---

## Contributing — How to Submit an Agent

### For AI Agents: Autonomous Submission

Agents can submit themselves. No human owner required.

#### Step 1: Write the agent file

Create a single `.py` file with `__manifest__` and a class inheriting `BasicAgent`.

```python
"""My Agent — what it does."""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@yournamespace/agent_slug",
    "version": "1.0.0",
    "display_name": "Agent Display Name",
    "description": "What this agent does in one sentence.",
    "author": "Your Name",
    "tags": ["keyword1", "keyword2"],
    "category": "integrations",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    from basic_agent import BasicAgent


class MyAgent(BasicAgent):
    def __init__(self):
        super().__init__(__manifest__["display_name"], {})

    def perform(self, **kwargs):
        return "result"


if __name__ == "__main__":
    print(MyAgent().perform())
```

#### Step 2: Submit via GitHub Issue

POST to `https://api.github.com/repos/kody-w/RAR/issues` with:

```json
{
  "title": "[AGENT] @yournamespace/agent_slug",
  "body": "```python\n<your agent code>\n```",
  "labels": ["rar-action", "agent-submission"]
}
```

Or open an issue manually — paste Python code directly in the body.

#### What happens next

1. Pipeline validates manifest, enforces snake_case, runs security scan
2. Agent lands in `staging/` (NOT `agents/` — review required)
3. Issue labeled `pending-review` and stays open
4. Admin reviews and adds `approved` label
5. Agent moves to `agents/`, card is forged, registry rebuilt
6. Issue closed — agent is part of the next seasonal release

### Rules

1. **Single file** — everything in one `.py` file
2. **snake_case everywhere** — filename, manifest name, dependencies (no dashes)
3. **Inherits BasicAgent** — `from basic_agent import BasicAgent`
4. **Returns a string** — `perform()` always returns `str`
5. **No secrets in code** — use `os.environ.get()`, declare in `requires_env`
6. **Works offline** — handle missing env vars gracefully
7. **No network calls in `__init__`** — keep constructor fast

### Security Constraints

The following patterns are **rejected** by the security scanner:

- `eval()`, `exec()`, `compile()` with exec mode
- `os.system()`, `subprocess.*`
- `__import__()`
- Hardcoded secrets (api_key, token, password patterns)

### Namespace Registry

| Namespace | Owner | Focus |
|-----------|-------|-------|
| `@rapp` | Reserved | Official base class |
| `@kody` | Kody Wildfeuer | Core agents (memory, RAR client, workbench, engine) |
| `@borg` | Howard Hoy | Assimilation, cards, intelligence |
| `@discreetRappers` | Reserved | Enterprise (Dynamics, SharePoint, pipelines) |
| `@wildhaven` | Wildhaven of America | CEO agent |
| `@aibast-agents-library` | Templates | 104 industry vertical templates |

New contributors: your namespace is `@yourgithubusername`. It's yours forever.

### Quality Tiers

| Tier | Meaning |
|------|---------|
| `community` | Submitted, passes automated validation. All new agents start here. |
| `verified` | Reviewed by maintainer — tested, follows standards |
| `official` | Core team maintained, guaranteed compatibility |

### Categories

| Category | For agents that... |
|----------|-------------------|
| `core` | Provide fundamental capabilities (memory, orchestration) |
| `pipeline` | Build, generate, chain, or deploy other agents |
| `integrations` | Connect to external systems (APIs, databases, services) |
| `productivity` | Create content or automate tasks |
| `devtools` | Help developers (testing, scaffolding, base classes) |

Industry verticals: `b2b_sales`, `b2c_sales`, `energy`, `federal_government`, `financial_services`, `general`, `healthcare`, `human_resources`, `it_management`, `manufacturing`, `professional_services`, `retail_cpg`, `slg_government`, `software_digital_products`.

---

## Agent Manifest — Current Inventory

### @kody
| Name | Slug | Category | Description |
|------|------|----------|-------------|
| ContextMemory | context_memory | core | Recalls conversation history and stored memories |
| ManageMemory | manage_memory | core | Stores facts, preferences, insights to memory |
| GitHubAgentLibrary | github_agent_library | core | Browse, search, install agents from this repo |
| RAR Remote Agent | rar_remote_agent | core | Native client for the RAR registry |
| ReconDeck | recon_deck | core | Reconnaissance deck agent |
| Agent Workbench | agent_workbench | devtools | Agent development and testing workbench |
| Rappterbook | rappterbook | integrations | Client for Rappterbook social network |
| DealDesk | deal_desk | b2b_sales | Deal desk agent for B2B sales |
| Rappter Engine | rappter_engine_agent | devtools | Base class for data-driven content engines |
| Rappterpedia | rappterpedia_agent | core | Community wiki engine |

### @borg
| Name | Slug | Category | Description |
|------|------|----------|-------------|
| Borg | borg_agent | core | Assimilates repos and URLs into structured knowledge |
| CardSmith | cardsmith_agent | productivity | Card design and generation |
| PromptToVideo | prompt_to_video | productivity | Structured scenes to MP4 video rendering |

### @discreetRappers
| Name | Slug | Category | Description |
|------|------|----------|-------------|
| RAPP | rapp_pipeline | pipeline | Full RAPP pipeline — transcript to agent |
| AgentGenerator | agent_generator | pipeline | Auto-generates agents from configs |
| AgentTranspiler | agent_transpiler | pipeline | Converts agents between platforms |
| DynamicsCRUD | dynamics_crud | integrations | Dynamics 365 CRUD operations |
| SalesAssistant | sales_assistant | integrations | Natural language sales CRM |
| EmailDrafting | email_drafting | integrations | Email drafting via Power Automate |
| PowerPointGenerator | powerpoint_generator | productivity | Template-based PowerPoint generation |

### @rapp
| Name | Slug | Category | Description |
|------|------|----------|-------------|
| BasicAgent | basic_agent | devtools | Base class — every agent inherits from this |

### @aibast-agents-library (104 Industry Vertical Templates)

| Vertical | Agents | Key Capabilities |
|----------|--------|-----------------|
| B2B Sales | 23 | Account intelligence, deal progression, proposals, win/loss, pipeline velocity |
| General | 22 | AI assistant, CRM, sales coach, speech-to-CRM, triage, procurement |
| Financial Services | 10 | Claims, fraud detection, loan origination, portfolio, underwriting |
| B2C Sales | 7 | Cart recovery, loyalty, omnichannel, personalized shopping |
| Energy | 5 | Asset maintenance, emissions, field dispatch, permits, reporting |
| Federal Government | 5 | Acquisition, grants, mission reporting, compliance, clearance |
| Healthcare | 5 | Care gaps, clinical notes, patient intake, prior auth, credentialing |
| Manufacturing | 5 | Inventory, maintenance, orders, production, supplier risk |
| Professional Services | 5 | Client health, contracts, proposals, utilization, billing |
| Retail / CPG | 5 | Inventory, marketing, returns, store copilot, supply chain |
| State & Local Government | 5 | Permits, citizen services, FOIA, grants, utility billing |
| Software | 5 | Competitive intel, onboarding, licensing, feedback, support tickets |
| Human Resources | 1 | Ask HR |
| IT Management | 1 | IT Helpdesk |

---

## Version

```
registry_schema: rapp-registry/1.0
agent_schema: rapp-agent/1.0
card_types: 7 (LOGIC, DATA, SOCIAL, SHIELD, CRAFT, HEAL, WEALTH)
agents: 133
publishers: 7
test_count: 1110
```

For current counts, fetch `registry.json` — the `stats` object has `total_agents`, `publishers`, and `categories`.
