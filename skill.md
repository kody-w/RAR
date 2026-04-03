# RAPP Agent Repo — Machine-Readable Skill Interface

> **This file is read by AI agents, not humans.** It enables autonomous agent discovery, search, install, and management without any human visiting GitHub.

---

## Repo Identity

```
repo: billwhalenmsft/RAPP-Agent-Repo
type: agent-registry
registry: registry.json
base_url: https://raw.githubusercontent.com/billwhalenmsft/RAPP-Agent-Repo/main
compatible_with: kody-w/CommunityRAPP
agent_base_class: BasicAgent (@rapp/basic-agent)
package_structure: agents/@publisher/slug.py (single file, __manifest__ embedded)
```

---

## API — How to Use This Repo Programmatically

### 1. Fetch the Registry

```
GET https://raw.githubusercontent.com/billwhalenmsft/RAPP-Agent-Repo/main/registry.json
```

Returns JSON with:
- `stats` — total agents, publishers, categories
- `agents[]` — array of all agent manifests

Each agent entry has:
- `name` — namespaced identifier (e.g., `@billwhalen/dynamics-crud`)
- `version` — semver (e.g., `1.0.0`)
- `display_name` — the agent's `self.name`
- `class` — Python class name
- `description` — what it does
- `author` — contributor name
- `tags` — searchable keyword list
- `category` — `core`, `pipeline`, `integrations`, `productivity`, `devtools`
- `requires_env` — environment variables needed (empty = no extra config)
- `dependencies` — other agents this depends on
- `quality_tier` — `community`, `verified`, or `official`
- `_path` — directory path in repo (e.g., `agents/@billwhalen/dynamics-crud`)

### 2. Fetch an Agent's Manifest

```
GET https://raw.githubusercontent.com/billwhalenmsft/RAPP-Agent-Repo/main/agents/@publisher/agent-slug.py
```

### 3. Download an Agent

```
GET https://raw.githubusercontent.com/billwhalenmsft/RAPP-Agent-Repo/main/agents/@publisher/agent-slug.py
```

### 4. Install an Agent

Save the downloaded `agent.py` to the CommunityRAPP `agents/` folder:

```python
# Autonomous install workflow
registry = http_get(f"{base_url}/registry.json")
agent = find_agent(registry, query)
content = http_get(f"{base_url}/{agent['_file']}")

# Determine filename: @billwhalen/dynamics-crud → dynamics_crud_agent.py
filename = agent['name'].split('/')[-1].replace('-', '_') + '_agent.py'
storage.write_file('agents', filename, content)
```

### 5. Search

Match against `name`, `display_name`, `description`, `tags`, `category`, and `author`.

Example searches:
- "dynamics" → matches `@billwhalen/dynamics-crud` (tag: dynamics-365)
- "memory" → matches `@kody/context-memory`, `@kody/manage-memory`
- "transpiler" → matches `@billwhalen/agent-transpiler`, `@billwhalen/copilot-studio-transpiler`
- "@billwhalen" → all 13 agents by Bill
- "integrations" → all 4 integration agents

### 6. List by Publisher

Filter `registry.agents[]` where `name` starts with `@publisher/`.

### 7. List by Category

Filter `registry.agents[]` where `category` matches.

---

## Agent Manifest — Current Inventory

### @kody (3 agents)
| Name | Slug | Category | Description |
|------|------|----------|-------------|
| ContextMemory | context-memory | core | Recalls conversation history and stored memories |
| ManageMemory | manage-memory | core | Stores facts, preferences, insights to memory |
| GitHubAgentLibrary | github-agent-library | core | Browse, search, install agents from this repo |

### @billwhalen (13 agents)
| Name | Slug | Category | Description |
|------|------|----------|-------------|
| RAPP | rapp-pipeline | pipeline | Full RAPP pipeline — transcript to agent, code gen, quality gates |
| AgentGenerator | agent-generator | pipeline | Auto-generates agents from configurations |
| AgentTranspiler | agent-transpiler | pipeline | Converts agents between M365, Copilot Studio, Azure AI Foundry |
| CopilotStudioTranspiler | copilot-studio-transpiler | pipeline | Native Copilot Studio transpilation |
| ProjectTracker | project-tracker | pipeline | RAPP project management and tracking |
| DynamicsCRUD | dynamics-crud | integrations | Dynamics 365 CRUD operations |
| ContractAnalysis | sharepoint-contract-analysis | integrations | Contract analysis from SharePoint/Azure Storage |
| SalesAssistant | sales-assistant | integrations | Natural language sales CRM assistant |
| EmailDrafting | email-drafting | integrations | Email drafting via Power Automate |
| PowerPointGeneratorV2 | powerpoint-generator | productivity | Template-based PowerPoint generation |
| ArchitectureDiagramAgent | architecture-diagram | productivity | Architecture diagram visualization |
| ScriptedDemo | scripted-demo | productivity | Interactive demo automation |
| DemoScriptGenerator | demo-script-generator | productivity | Demo script JSON generation |

### @rapp (1 agent)
| Name | Slug | Category | Description |
|------|------|----------|-------------|
| BasicAgent | basic-agent | devtools | Base class — every agent inherits from this |

### @aibast-agents-library (104 agent templates — Industry Vertical Stacks)

Source: [AI-Agent-Templates](https://kody-w.github.io/AI-Agent-Templates/)

These are **templates, not turnkey agents.** Each template provides the agent structure, system prompts, and logic scaffold for a specific business function. Users should mutate them with AI (e.g., the RAPP pipeline, Copilot, or manual editing) to adapt to their specific data sources, business rules, APIs, and deployment environment.

| Vertical | Agents | Key Capabilities |
|----------|--------|-----------------|
| B2B Sales | 23 | Account intelligence, deal progression, proposal generation, win/loss analysis, pipeline velocity, stakeholder mapping |
| General | 22 | AI customer assistant, CRM data seeder, sales coach, speech-to-CRM, triage bot, procurement |
| Financial Services | 10 | Claims processing, fraud detection, loan origination, portfolio rebalancing, underwriting, wealth insights |
| B2C Sales | 7 | Cart abandonment recovery, loyalty rewards, omnichannel engagement, personalized shopping, returns/exchange |
| Energy | 5 | Asset maintenance forecast, emission tracking, field service dispatch, permit management, regulatory reporting |
| Federal Government | 5 | Acquisition support, grants oversight, mission reporting, regulatory compliance, workforce clearance |
| Healthcare | 5 | Care gap closure, clinical notes summarizer, patient intake, prior authorization, staff credentialing |
| Manufacturing | 5 | Inventory rebalancing, maintenance scheduling, order communication, production optimization, supplier risk |
| Professional Services | 5 | Client health score, contract risk review, proposal copilot, resource utilization, time/billing |
| Retail / CPG | 5 | Inventory visibility, personalized marketing, returns resolution, store associate copilot, supply chain alerts |
| State & Local Government | 5 | Building permits, citizen services, FOIA requests, grants management, utility billing |
| Software / Digital Products | 5 | Competitive intel, customer onboarding, license renewal, product feedback, support ticket resolution |
| Human Resources | 1 | Ask HR |
| IT Management | 1 | IT Helpdesk |

To list all agents in a vertical, filter `registry.agents[]` where `category` matches the vertical key (e.g., `b2b_sales`, `healthcare`, `manufacturing`).

---

## Autonomous Workflows

### "Install an agent by name"

```
User: "Install the dynamics agent"

1. GET registry.json
2. Search agents[] for "dynamics" in name/tags/description
3. Match: @billwhalen/dynamics-crud
4. GET agents/@billwhalen/dynamics-crud.py
5. Save as dynamics_crud_agent.py in CommunityRAPP agents/
6. Check requires_env — warn if non-empty
7. Report: "Installed @billwhalen/dynamics-crud v1.0.0"
```

### "Show all agents by @billwhalen"

```
1. GET registry.json
2. Filter where name starts with "@billwhalen/"
3. Return 13 agents grouped by category
```

### "Find agents for healthcare"

```
1. GET registry.json
2. Filter where category == "healthcare"
3. Return 5 agents: care_gap_closure, clinical_notes_summarizer, patient_intake, prior_authorization, staff_credentialing
4. Present with descriptions, quality_tier, requires_env
```

### "Install all integration agents"

```
1. GET registry.json
2. Filter where category == "integrations"
3. Download and install each agent.py
4. Report summary with any required env vars
```

### "What agent can help with PowerPoint?"

```
1. GET registry.json
2. Search tags/description for "powerpoint"
3. Match: @billwhalen/powerpoint-generator
4. Present: name, description, version, quality_tier, requires_env
5. Ask: "Want me to install it?"
```

### "Update all my agents to latest"

```
1. GET registry.json
2. List installed agents in CommunityRAPP agents/
3. Match filenames to registry entries
4. Compare versions
5. Download newer versions
```

---

## Contributing

New agents follow this structure:
```
agents/@yourname/my-agent.py
```

See CONTRIBUTING.md for full guide.

---

## Version

```
registry_schema: rapp-registry/1.0
agent_schema: rapp-agent/1.0
total_agents: 121
publishers: 4 (@kody, @billwhalen, @rapp, @aibast-agents-library)
categories: 19 (core, pipeline, integrations, productivity, devtools, b2b_sales, b2c_sales, energy, federal_government, financial_services, general, healthcare, human_resources, it_management, manufacturing, professional_services, retail_cpg, slg_government, software_digital_products)
verticals: 14
last_updated: 2026-03-17
```
