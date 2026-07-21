# RAPP — Machine-Readable Skill Interface

> ## Quick Start — Feed This File to Your AI
>
> Copy-paste **one command** into your AI assistant (Claude, ChatGPT, Copilot, etc.) to give it full agentic access to the RAPP registry:
>
> ```
> Read this file and use it as your skill interface for the RAPP agent registry: https://raw.githubusercontent.com/kody-w/RAR/main/skill.md
> ```
>
> Or if your AI supports URL fetching, just say:
>
> ```
> Fetch https://raw.githubusercontent.com/kody-w/RAR/main/skill.md and use it to help me browse, search, install, and submit agents to the RAPP registry.
> ```
>
> Once your AI has this file, it can: search 180+ agents, install them with one command, scaffold new agents, submit to the registry, resolve cards from seeds, and more — all without you visiting GitHub.

---

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
- `_file` — file path in repo (e.g., `agents/@discreetRappers/dynamics_crud_agent.py`)
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

### 5. Search (one-liner for local LLMs)

Fetch the registry and search it locally — no API key, no auth, works offline after first fetch:

```bash
curl -s https://raw.githubusercontent.com/kody-w/RAR/main/registry.json | python3 -c "
import json,sys; q=sys.argv[1].lower(); [print(f\"{a['display_name']} — {a['description']}\n  {a['name']} | {a['category']} | by {a['author']}\n\") for a in json.load(sys.stdin)['agents'] if q in json.dumps(a).lower()]
" "YOUR SEARCH TERM"
```

Replace `YOUR SEARCH TERM` with what you need (e.g. `"sales"`, `"memory"`, `"healthcare"`). Match against `name`, `display_name`, `description`, `tags`, `category`, and `author`.

### 6. Resolve a Card from Seed (offline, zero bandwidth)

Any numeric seed resolves to a full card deterministically. No network needed.

Algorithm: `seed → mulberry32 PRNG → type, stats, abilities, rarity`

Implementation: `rapp_sdk.py` (Python). Deterministic algorithm — same seed always yields the same card.

### 7. MCP On-Ramp (for MCP hosts)

MCP is transport, not a new agent unit — it is how an MCP-native AI reaches RAR and a running brainstem. Framing: MCP clients are Layer 2 callers of `/chat` ("Chat Is The Only Wire").

- **Static catalog (`rapp-static-mcp/1.0`):** This repo's static files already form a content-addressed MCP catalog. Catalog = `registry.json`; agent frames = `agents/*` pinned by `_sha256` (and `_first_commit_sha` for first-seen provenance). An MCP host reads the catalog, fetches a frame, and **verifies-before-exec**: recompute the SHA256 of the fetched file and refuse to run on mismatch. Profile is built on `rapp-static-api/1.0` (see `api.json` → `endpoints.mcp`).
- **Live brainstem (`rapp_brainstem_mcp.py`):** bridges a running brainstem to any MCP host over `/chat`. Every capability — install, search, run an agent, memory — flows through that single `/chat` call.
- **Serving drop-in agents (`rapp_mcp.py`):** exposes local drop-in `*_agent.py` files as MCP tools for hosts that want to call them directly.

### 8. Ecosystem Catalogs (rapplications, senses, skills)

RAR is the consolidated storefront for the whole RAPP ecosystem. One fetch returns every peer-store catalog:

```
GET https://raw.githubusercontent.com/kody-w/RAR/main/state/federation.json
```

Returns (`schema: rar-federation/1.0`):
- `rapplications[]` — bundled organisms (agent + UI / service / state cartridge) from [kody-w/RAPP_Store](https://github.com/kody-w/RAPP_Store). Each entry: `id`, `name`, `version`, `summary`, `category`, `tags`, `manifest_name`, `access` (`public` | `private`), `singleton_url`, `singleton_sha256`, `store_url`, `repo_url`. Install = fetch `singleton_url`, **verify `singleton_sha256` before exec**, drop into your brainstem's `agents/`. `access: "private"` entries are gated — the URL 404s without a PAT that has read access on the private repo.
- `senses[]` — per-channel output overlays from [kody-w/RAPP_Sense_Store](https://github.com/kody-w/RAPP_Sense_Store). Each entry: `name`, `publisher`, `version`, `description`, `delimiter`, `surfaces`, `url`, `sha256`. Install = fetch `url`, verify `sha256`, drop into `rapp_brainstem/utils/senses/`.
- `skills[]` — portable agent skills from [kody-w/rapp-skills](https://github.com/kody-w/rapp-skills) and [kody-w/rapp-claude-skills](https://github.com/kody-w/rapp-claude-skills). Each entry: `name`, `description`, `repo`, `url`, `skill_md_url`. Consume = fetch `skill_md_url` and follow it like this file.

The snapshot is a slim projection refreshed daily. The home repos remain authoritative — for full metadata fetch the source catalogs directly:

```
GET https://raw.githubusercontent.com/kody-w/RAPP_Store/main/index.json         # rapplications (full)
GET https://raw.githubusercontent.com/kody-w/RAPP_Sense_Store/main/index.json   # senses (full)
```

### 9. Community Ratings (Discussions-backed upvotes + comments)

Every registry agent has one GitHub Discussion whose **title is the agent name** (e.g. `@rapp/basic_agent`), in the maintainer-only Announcements category of `kody-w/RAR`.

```
GET https://raw.githubusercontent.com/kody-w/RAR/main/state/discussion_ratings.json
```

Returns (`schema: rar-discussion-ratings/1.0`) `agents` keyed by agent name: `{upvotes, comments, url, number}`. `upvotes` counts **positive reactions only** (THUMBS_UP, HEART, HOORAY, ROCKET, LAUGH); negative and neutral reactions never contribute.

- **Read** ratings: fetch the snapshot above (no auth). Use it to rank agents ("most loved").
- **Upvote** an agent: add a positive reaction to its Discussion (GraphQL `addReaction` on the discussion node, or open `url` in a browser). One reaction per GitHub identity — GitHub enforces dedup natively.
- **Comment / review** an agent: reply in its Discussion thread (`url`).
- The snapshot refreshes daily; a live vote appears on the next refresh.

Legacy issue-based votes/reviews still work too (`state/votes.json`, `state/reviews.json`, filed via `[RAR]`-prefixed Issues) and are merged with reaction counts in the store UI.

---

## SDK — Agentic-First Onboarding

The RAPP SDK (`rapp_sdk.py`) is the developer toolkit. Zero dependencies. One file.

### Quick Start (4 steps)

```bash
# 1. Initialize an agents/ workspace
python rapp_sdk.py init

# 2. Scaffold a new agent
python rapp_sdk.py new @yourname/my_cool_agent

# 3. Validate + test
python rapp_sdk.py test agents/@yourname/my_cool_agent.py

# 4. Submit to the RAPP registry
python rapp_sdk.py submit agents/@yourname/my_cool_agent.py
```

### SDK Commands

| Command | What |
|---------|------|
| `init [name]` | Initialize a RAPP agents/ workspace (creates agents/, staging/) |
| `new @pub/slug` | Scaffold agent from template (snake_case enforced) |
| `validate path.py` | Validate manifest against schema |
| `test path.py` | Run contract tests (no pytest needed) |
| `search "query"` | Search the registry |
| `install @pub/slug` | Download agent from registry |
| `info @pub/slug` | Show agent details |
| `submit path.py` | Submit agent to RAPP for review |
| `delete @pub/slug --reason "..."` | Request hash-bound deletion |
| `request-read @pub/slug` | Create an auditable read Issue |
| `request-status ISSUE` | Read an Issues-backed request lifecycle |
| `card mint path.py` | Mint a card from agent file |
| `card resolve @pub/slug` | Self-assemble card from name (needs registry) |
| `card resolve 12345` | Self-assemble card from seed (offline) |
| `card value @pub/slug` | Check floor value |
| `status` | Show your agents/ collection inventory |
| `transfer id to` | Transfer a card |
| `egg forge @pub/a @pub/b` | Forge an egg from agent names (sneakernet transfer) |
| `egg compact @pub/a @pub/b` | Compress egg to shareable string (QR/SMS/NFC) |
| `egg hatch <compact>` | Hatch egg — install agents from compact string |

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

**Option A — Legacy direct GitHub CLI (automatic operation inference)**

If you're signed into a GitHub Enterprise Managed User (EMU) account, it cannot interact with public repos outside your enterprise. Use the `gh` CLI with a **personal GitHub account** instead:

```bash
# Authenticate with a personal (non-EMU) GitHub account
gh auth login

# Submit the agent
gh issue create --repo kody-w/RAR \
  --title "[AGENT] @yournamespace/agent_slug_agent" \
  --body "$(cat <<'EOF'
```python
<paste your agent code here>
```
EOF
)"
```

**Option B — Legacy direct API call (automatic operation inference)**

POST to `https://api.github.com/repos/kody-w/RAR/issues` with a personal access token (PAT) from a personal GitHub account:

```bash
curl -X POST https://api.github.com/repos/kody-w/RAR/issues \
  -H "Authorization: Bearer YOUR_PERSONAL_PAT" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "[AGENT] @yournamespace/agent_slug_agent",
    "body": "```python\n<your agent code>\n```"
  }'
```

**Option C — Web UI (non-EMU accounts)**

Open an issue at https://github.com/kody-w/RAR/issues/new — paste Python code directly in the body.

> **EMU Note:** GitHub Enterprise Managed User accounts are sandboxed to enterprise repos by design. You need a personal GitHub account (free) to interact with public repos like RAPP. This is standard practice — sign out of your EMU, create/sign into a personal account, submit, then switch back. Your `@yourname` namespace is tied to your personal identity, not your enterprise identity.

#### What happens next

1. Pipeline binds the GitHub account, manifest, source hash, and preconditions
2. Exact bytes land under an Issue-specific immutable staging revision
3. Issue is labeled `pending-review` and stays open
4. Authorized admin approval binds only that exact revision
5. Security, registry, card, and test gates run
6. Mutation and receipt commit to `main`; Issue closes as `notarized`

#### Updating an existing agent

Submit a new Issue with the updated code. The version in `__manifest__` must be higher than the existing version (e.g., `1.0.0` → `1.1.0`). Same staging → review → approval flow. The new version gets a new forged seed — the old seed still resolves to the old card forever.

### Rules

1. **Single file** — everything in one `.py` file
2. **snake_case everywhere** — filename, manifest name, dependencies (no dashes)
3. **Inherits BasicAgent** — `from basic_agent import BasicAgent`
4. **Returns a string** — `perform()` always returns `str`
5. **No secrets in code** — use `os.environ.get()`, declare in `requires_env`
6. **Works offline** — handle missing env vars gracefully
7. **No network calls in `__init__`** — keep constructor fast

### Security Constraints

**Rejected** (build fails) — genuine supply-chain hazards:

- `os.system()` — use `subprocess` and declare wrapped binaries in `requires_env`
- Suspicious file access (`/etc`, `/proc`, `.env`, `.ssh`, `passwd`)
- Hardcoded secrets (api_key, token, password patterns)

**Allowed but TAGGED** — dynamic-code capabilities are legitimate (meta-programming,
self-verification against a fetched reference, sandboxed interpreters). They are not
rejected; the agent's registry entry records `_capabilities` (and `_uses_exec`) so
consumers who want to restrict dynamic code can **filter** on the tag:

- `eval()`, `exec()`, `compile()` with exec mode, `__import__()`

**Allowed** — `subprocess.*` (wrapping external CLIs is a normal integration pattern).

### Namespace Registry

| Namespace | Owner | Focus |
|-----------|-------|-------|
| `@rapp` | Reserved | Official base class and core platform agents |
| `@kody-w` | Kody Wildfeuer | Core agents (memory, RAPP client, workbench, engine) |
| `@howardh` | Howard Hoy | Assimilation, cards, intelligence |
| `@discreetRappers` | Reserved | Enterprise (Dynamics, SharePoint, pipelines) |
| `@wildhaven` | Wildhaven of America | CEO agent |
| `@bill` | Bill | Core |
| `@rarbookworld` | RAR Bookworld | Pipeline |
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

> This is a partial, hand-maintained sample. For the complete, current inventory (180 agents across 8 publishers), fetch `registry.json` — its `agents` array is the ground truth.

### @kody-w
| Name | Slug | Category | Description |
|------|------|----------|-------------|
| ContextMemory | context_memory_agent | core | Recalls conversation history and stored memories |
| ManageMemory | manage_memory_agent | core | Stores facts, preferences, insights to memory |
| GitHubAgentLibrary | github_agent_library_agent | core | Browse, search, install agents from this repo |
| RAPP Remote Agent | rar_remote_agent | core | Native client for the RAPP registry |
| ReconDeck | recon_deck_agent | core | Reconnaissance deck agent |
| Agent Workbench | agent_workbench | devtools | Agent development and testing workbench |
| Rappterbook | rappterbook_agent | integrations | Client for Rappterbook social network |
| DealDesk | deal_desk_agent | b2b_sales | Deal desk agent for B2B sales |
| Rappter Engine | rappter_engine_agent | devtools | Base class for data-driven content engines |
| Rappterpedia | rappterpedia_agent | core | Community wiki engine |

### @howardh
| Name | Slug | Category | Description |
|------|------|----------|-------------|
| Borg | borg_agent | core | Assimilates repos and URLs into structured knowledge |
| CardSmith | cardsmith_agent | productivity | Card design and generation |
| PromptToVideo | prompt_to_video_agent | productivity | Structured scenes to MP4 video rendering |

### @discreetRappers
| Name | Slug | Category | Description |
|------|------|----------|-------------|
| RAPP | rapp_pipeline_agent | pipeline | Full RAPP pipeline — transcript to agent |
| AgentGenerator | agent_generator_agent | pipeline | Auto-generates agents from configs |
| AgentTranspiler | agent_transpiler_agent | pipeline | Converts agents between platforms |
| DynamicsCRUD | dynamics_crud_agent | integrations | Dynamics 365 CRUD operations |
| SalesAssistant | sales_assistant_agent | integrations | Natural language sales CRM |
| EmailDrafting | email_drafting_agent | integrations | Email drafting via Power Automate |
| PowerPointGenerator | powerpoint_generator_agent | productivity | Template-based PowerPoint generation |

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

## Admin — Submission Pipeline

Dashboard: `https://kody-w.github.io/RAR/admin.html`

### Pipeline Stages

| Stage | Label | State | Meaning |
|-------|-------|-------|---------|
| Pending Review | `pending-review` | open | Exact revision validated, awaiting admin review |
| Approved | `approved` | open | Authorized admin approved the exact revision |
| Notarized | `notarized` | closed | Exact bytes passed checks and committed with receipt |
| Deleted | `deleted` | closed | Active file removed; tombstone and receipt retained |
| Failed | `failed` | open | Validation or notarization failed; nothing reported published |
| Rejected | `rejected` | closed | Admin rejected the submission |

### Admin Actions (require GitHub auth with `public_repo` scope)

**Approve** — Adds `approved` label, comments on issue:
```
POST /repos/kody-w/RAR/issues/{number}/labels  → {"labels": ["approved"]}
```

Adding `approved` automatically runs the hash-bound notarization workflow.

**Reject** — Comments, closes issue with `rejected` label:
```
PATCH /repos/kody-w/RAR/issues/{number}  → {"state": "closed", "labels": ["rejected"]}
```

**Retry intake validation** — edit the Issue to trigger reconciliation, or
manually dispatch `process-issues.yml` with its Issue number.

**Retry notarization/projection** — remove and re-add `approved`. The workflow
reuses an existing committed receipt when publication already succeeded:
```
DELETE /repos/kody-w/RAR/issues/{number}/labels/failed
DELETE /repos/kody-w/RAR/issues/{number}/labels/approved
POST /repos/kody-w/RAR/issues/{number}/labels  → {"labels": ["approved"]}
```

### Typical Morning Review

1. Open `admin.html`, sign in with GitHub
2. Check **Pending Review** column for new submissions
3. Click **View** to inspect agent code on the issue
4. Click **Approve** (adds label, moves to Approved column) or **Reject** (closes issue)
5. Watch the automatic notarization workflow
6. Check **Failed** for recoverable validation or infrastructure failures
7. **Notarized** shows exact source, receipt, and publication commit

### Deduplication

The registry detects duplicate agents by `display_name`. The `duplicates` array in `registry.json` lists any collisions:

```json
"duplicates": [
  {"display_name": "TrainingQuest", "agents": ["@howardh/training_quest", "@howardh/training_quest_agent"]}
]
```

The admin dashboard shows duplicates in a dedicated section. To resolve:
1. Determine which agent is canonical (usually the one processed by CI pipeline)
2. Remove the duplicate file from `agents/`
3. Rebuild: `python build_registry.py`

Issues labeled `duplicate` or `rejected` are hidden from the pipeline board.

---

## Version

```
registry_schema: rapp-registry/1.1
agent_schema: rapp-agent/1.0
card_types: 7 (LOGIC, DATA, SOCIAL, SHIELD, CRAFT, HEAL, WEALTH)
agents: 180
publishers: 8
test_count: 1144
egg_protocol: rapp-egg/1.0
```

For current counts, fetch `registry.json` — the `stats` object has `total_agents`, `publishers`, and `categories`.
