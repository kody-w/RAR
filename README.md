# RAPP Agent Repo

**The open agent registry for [CommunityRAPP](https://github.com/kody-w/CommunityRAPP).**

121 agents. 4 publishers. 19 categories. 14 industry verticals. Drop any agent into your `agents/` folder — it just works.

> **This repo scales to thousands of agents.** Each agent is a namespaced package (`@publisher/agent-name`) with its own manifest, versioning, and docs. No collisions. No chaos.

---

## Install an Agent

### From Chat (Headless)

The `GitHubAgentLibraryManager` agent reads this repo autonomously:

> *"Install the dynamics-crud agent"*
> *"What agents are available for CRM?"*
> *"Show me all @billwhalen agents"*

No repo visit needed.

### Give Your AI Agent Access

Point any LLM or AI agent at the skill manifest — one line:

```
https://raw.githubusercontent.com/billwhalenmsft/RAPP-Agent-Repo/main/skill.md
```

### Manual

```bash
# Browse → pick an agent → copy to your CommunityRAPP
cp RAPP-Agent-Repo/agents/@billwhalen/dynamics-crud/agent.py \
   /path/to/CommunityRAPP/agents/dynamics_crud_agent.py

# Restart your function app — agents auto-load
func start
```

---

## Agent Registry

### 🧠 Core — Memory & Orchestration

| Package | Description |
|---------|-------------|
| [`@kody/context-memory`](agents/@kody/context-memory.py) | Recalls conversation history and stored memories |
| [`@kody/manage-memory`](agents/@kody/manage-memory.py) | Stores facts, preferences, insights to persistent memory |
| [`@kody/github-agent-library`](agents/@kody/github-agent-library.py) | Browse, search, install agents from this repo via chat |

### 🔧 Pipeline — RAPP Agent Factory

| Package | Description |
|---------|-------------|
| [`@billwhalen/rapp-pipeline`](agents/@billwhalen/rapp-pipeline.py) | Full RAPP pipeline — transcript → agent, discovery, MVP, code gen, QG1-QG6 |
| [`@billwhalen/agent-generator`](agents/@billwhalen/agent-generator.py) | Auto-generates new agents from configurations |
| [`@billwhalen/agent-transpiler`](agents/@billwhalen/agent-transpiler.py) | Converts agents between M365 Copilot, Copilot Studio, Azure AI Foundry |
| [`@billwhalen/copilot-studio-transpiler`](agents/@billwhalen/copilot-studio-transpiler.py) | Transpiles to native Copilot Studio without Azure Function dependency |
| [`@billwhalen/project-tracker`](agents/@billwhalen/project-tracker.py) | RAPP project management and engagement tracking |

### 🔌 Integrations — Microsoft 365 & CRM

| Package | Description |
|---------|-------------|
| [`@billwhalen/dynamics-crud`](agents/@billwhalen/dynamics-crud.py) | Dynamics 365 CRUD — accounts, contacts, opportunities, leads, tasks |
| [`@billwhalen/sharepoint-contract-analysis`](agents/@billwhalen/sharepoint-contract-analysis.py) | Contract analysis from Azure File Storage / SharePoint |
| [`@billwhalen/sales-assistant`](agents/@billwhalen/sales-assistant.py) | Natural language sales CRM assistant |
| [`@billwhalen/email-drafting`](agents/@billwhalen/email-drafting.py) | Email drafting with Power Automate delivery |

### 📊 Productivity — Content & Demos

| Package | Description |
|---------|-------------|
| [`@billwhalen/powerpoint-generator`](agents/@billwhalen/powerpoint-generator.py) | Template-based PowerPoint generation (Microsoft design) |
| [`@billwhalen/architecture-diagram`](agents/@billwhalen/architecture-diagram.py) | Architecture diagram visualization (Mermaid, SVG, ASCII) |
| [`@billwhalen/scripted-demo`](agents/@billwhalen/scripted-demo.py) | Interactive demo automation from JSON scripts |
| [`@billwhalen/demo-script-generator`](agents/@billwhalen/demo-script-generator.py) | Generates demo script JSON files for ScriptedDemoAgent |

### 🛠️ Dev Tools

| Package | Description |
|---------|-------------|
| [`@rapp/basic-agent`](agents/@rapp/basic-agent.py) | Base class — every agent inherits from this |

### 🏭 Industry Agent Stacks — @aibast-agents-library

104 industry agent **templates** across 14 verticals, sourced from [AI-Agent-Templates](https://kody-w.github.io/AI-Agent-Templates/). These are starting points — each template provides the structure, prompts, and logic for a business function, but must be customized with AI (e.g., via the RAPP pipeline or Copilot) to fit your specific data sources, business rules, and integrations before deployment.

| Vertical | Agents | Examples |
|----------|--------|----------|
| B2B Sales | 23 | Account intelligence, deal progression, proposal generation, win/loss analysis |
| General | 22 | AI customer assistant, CRM data seeder, sales coach, triage bot |
| Financial Services | 10 | Claims processing, fraud detection, loan origination, portfolio rebalancing |
| B2C Sales | 7 | Cart abandonment, loyalty rewards, omnichannel engagement, personalized shopping |
| Energy | 5 | Asset maintenance, emission tracking, field service dispatch |
| Federal Government | 5 | Acquisition support, grants oversight, regulatory compliance |
| Healthcare | 5 | Care gap closure, clinical notes, patient intake, prior authorization |
| Manufacturing | 5 | Inventory rebalancing, maintenance scheduling, production optimization |
| Professional Services | 5 | Client health score, contract risk review, resource utilization |
| Retail / CPG | 5 | Inventory visibility, personalized marketing, supply chain alerts |
| State & Local Government | 5 | Building permits, citizen services, FOIA requests, grants management |
| Software / Digital Products | 5 | Competitive intel, customer onboarding, license renewal, support tickets |
| Human Resources | 1 | Ask HR |
| IT Management | 1 | IT Helpdesk |

---

## How It Works

### Package Structure

Every agent is a **single `.py` file** with a `__manifest__` dict embedded inside. No separate manifest.json. No README.md. One file = one agent.

```
agents/@publisher/agent-slug.py    ← that's the whole package
```

The `__manifest__` inside each file declares name, version, tags, dependencies, and required env vars. The registry builder reads it via AST parsing — no imports, no execution.

### Namespaces

Publishers own their namespace forever. No collisions at any scale.

```
@kody/context-memory         # Kody's memory agent
@billwhalen/dynamics-crud    # Bill's Dynamics agent
@acme-corp/invoice-parser    # Acme Corp's invoice agent
@yourname/your-agent         # Your agent
```

### Quality Tiers

| Tier | Badge | Meaning |
|------|-------|---------|
| `official` | 🔷 | Maintained by RAPP core team |
| `verified` | ✅ | Reviewed, tested, follows standards |
| `community` | 🌐 | Submitted by community, basic validation |

### Discovery

- **`registry.json`** — auto-generated index of all agents (built by CI on every push)
- **`skill.md`** — machine-readable interface for AI agents to use this repo autonomously
- **Tags** — every agent has searchable tags for keyword discovery

---

## Contributing

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for the full guide. Quick version:

```bash
# 1. Fork & clone
git clone https://github.com/YOUR_USERNAME/RAPP-Agent-Repo.git

# 2. Create your agent package
mkdir -p agents/@yourname/my-agent
# Add: agent.py, manifest.json, README.md

# 3. Validate
python build_registry.py

# 4. PR
git push && open PR
```

---

## Architecture

```
RAPP-Agent-Repo/
├── agents/
│   ├── @kody/                    # Publisher namespace
│   │   ├── context-memory.py     # Single-file agent (manifest embedded)
│   │   ├── manage-memory.py
│   │   └── github-agent-library.py
│   ├── @billwhalen/
│   │   ├── dynamics-crud.py
│   │   ├── rapp-pipeline.py
│   │   └── ... (13 agents)
│   ├── @rapp/
│   │   └── basic-agent.py        # Base class
│   └── @aibast-agents-library/
│       ├── b2b_sales_stacks/     # 23 agents across 5 stacks
│       ├── b2c_sales_stacks/     # 7 agents
│       ├── energy_stacks/        # 5 agents
│       ├── financial_services_stacks/  # 10 agents
│       ├── general_stacks/       # 22 agents
│       ├── healthcare_stacks/    # 5 agents
│       ├── manufacturing_stacks/ # 5 agents
│       ├── ... (14 verticals, 104 agents total)
│       └── templates/            # BasicAgent base class for stacks
├── registry.json                 # Auto-generated from __manifest__ dicts (CI)
├── skill.md                      # Machine-readable AI interface
├── build_registry.py             # Scans .py files, extracts __manifest__, builds registry
├── CONTRIBUTING.md               # How to submit agents
├── CONSTITUTION.md               # Governing document — single file principle, rules
└── .github/workflows/            # CI: auto-build registry on push
```

---

## Compatibility

- **Python**: 3.11+ (required for Azure Functions v4)
- **Runtime**: [CommunityRAPP](https://github.com/kody-w/CommunityRAPP)
- **AI Model**: Azure OpenAI (GPT-4o, GPT-5.1+)

---

## Contributors

| Publisher | Agents | Focus |
|-----------|--------|-------|
| **@aibast-agents-library** | 104 | Industry vertical agent stacks (14 verticals) |
| **@billwhalen** | 13 | Pipeline, integrations, productivity |
| **@kody** | 3 | Core memory, agent library |
| **@rapp** | 1 | Base classes |

---

<p align="center">
  <strong>Build an agent. Namespace it. Share it with the world.</strong>
</p>
