---
name: "rar-bill-neuron"
description: "Returns a compact [Knowledge Base] block of embedded RAPPNeurons for system-prompt injection."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@bill/neuron_agent", "rar_sha256": "e0af759764d7c236755c42e600539fc64a7f17ddc3fac358077f6b23bd8bcb30", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Bill Whalen", "tags": ["memory", "neuron", "knowledge-base", "bootstrap", "platform", "copilot-studio", "dataverse", "d365", "power-platform"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@bill/neuron_agent`. The original RAPP
agent is preserved byte-for-byte in `neuron_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Neuron — portable memory packs (RAPPNeurons) as a single-file agent.

Drop this one .py file into agents/@bill/ and the brainstem gets a compact
[Knowledge Base] block injected into the system prompt. No neurons/ folder,
no install script, no kernel patch — the file IS the registry.

To add knowledge: append a dict to the NEURONS list below. Each neuron is
self-describing (id, name, version, category, memories[]). Memories carry a
memory_type ("fact" | "gotcha" | "pattern"), free-text content, and tags
that callers can filter on.

The compact formatter strips per-memory date/time noise (saves ~40% tokens
vs the legacy memory format) and groups everything under one Knowledge Base
header. Subsequent perform() calls are cached.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "category": {
      "description": "Filter to one neuron category (e.g., 'copilot-studio', 'dataverse', 'd365', 'power-platform'). Omit for all.",
      "type": "string"
    },
    "list": {
      "description": "If true, just list the installed neurons (id, name, category, memory count) instead of the full Knowledge Base block.",
      "type": "boolean"
    },
    "memory_type": {
      "description": "Filter by memory_type ('fact', 'gotcha', 'pattern'). Omit for all.",
      "type": "string"
    },
    "tags": {
      "description": "Filter individual memories by tag. ANY-match: a memory is included if it has at least one of these tags.",
      "items": {
        "type": "string"
      },
      "type": "array"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `neuron_agent.py` and embedded as the fenced Python below (sha256 e0af759764d7c236…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `neuron_agent.py` first:

```bash
python3 neuron_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 neuron_agent.py   # or on stdin
python3 neuron_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@bill/neuron_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/neuron_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@bill/neuron_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""Neuron — portable memory packs (RAPPNeurons) as a single-file agent.

Drop this one .py file into agents/@bill/ and the brainstem gets a compact
[Knowledge Base] block injected into the system prompt. No neurons/ folder,
no install script, no kernel patch — the file IS the registry.

To add knowledge: append a dict to the NEURONS list below. Each neuron is
self-describing (id, name, version, category, memories[]). Memories carry a
memory_type ("fact" | "gotcha" | "pattern"), free-text content, and tags
that callers can filter on.

The compact formatter strips per-memory date/time noise (saves ~40% tokens
vs the legacy memory format) and groups everything under one Knowledge Base
header. Subsequent perform() calls are cached.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@bill/neuron_agent",
    "version": "1.0.1",
    "display_name": "Neuron",
    "description": "Injects a compact Knowledge Base block of hardcoded Copilot Studio and Dataverse lessons into the brainstem prompt at session start.",
    "author": "Bill Whalen",
    "tags": ["memory", "neuron", "knowledge-base", "bootstrap", "platform", "copilot-studio", "dataverse", "d365", "power-platform"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

from agents.basic_agent import BasicAgent


NEURONS = [
    {
        "id": "cs_automation_gotchas",
        "name": "Copilot Studio Automation Gotchas",
        "version": "1.0.0",
        "category": "copilot-studio",
        "description": "Hard-won lessons from programmatic Copilot Studio + Power Automate automation.",
        "memories": [
            {
                "memory_type": "gotcha",
                "content": "Copilot Studio PA flow Response action MUST have `kind: Skills` for output variables to appear in the CS topic variable picker. Without it, outputs are invisible — the Action node shows zero outputs even though the flow runs successfully.",
                "tags": ["copilot-studio", "power-automate", "response-action", "kind-skills"],
            },
            {
                "memory_type": "gotcha",
                "content": "Stale flow-binding cache: after changing a PA flow's trigger or RespondToCopilotStudio schema via REST, the bot keeps a cached snapshot. The ONLY fixes are: (1) open topic in CS UI → click the Action node → delete + re-add it, OR (2) click the Refresh icon on the node. There is NO public REST endpoint to refresh the cache. Stop after 2 failed publish attempts and hand off to the user.",
                "tags": ["copilot-studio", "power-automate", "stale-cache", "publish", "gotcha"],
            },
            {
                "memory_type": "fact",
                "content": "RespondToCopilotStudio action requires BOTH `body` AND `schema` parameters. The `schema.properties` is what Copilot Studio reads to build the output variable list — the body JSON alone is not introspected. Every output field must have a `title` and `type` in `schema.properties`, plus `x-ms-dynamically-added: true`.",
                "tags": ["copilot-studio", "power-automate", "response-schema", "outputs"],
            },
            {
                "memory_type": "gotcha",
                "content": "`char(10)` is NOT valid in Power Automate Skills flows — causes InvalidTemplate at runtime. Use `decodeUriComponent('%0A')` for newlines instead.",
                "tags": ["power-automate", "expressions", "newline", "gotcha"],
            },
            {
                "memory_type": "gotcha",
                "content": "PowerShell quoting trap when PATCHing flow JSON: double-quoted PS strings interpolate `$var?` breaking Logic Apps expressions. Always use SINGLE-QUOTED PS strings with doubled-up single quotes for embedded quotes: `'@coalesce(outputs(''GetVendor'')?[''body/value''], json(''[]''))'`",
                "tags": ["power-automate", "powershell", "quoting", "json-patch", "gotcha"],
            },
            {
                "memory_type": "fact",
                "content": "PA body expression interpolation uses `@{expr}` (with curly braces), NOT `@expr`. Example: `\"vendor_name\": \"@{coalesce(variables('name'), '')}\"`. Missing curly braces causes the expression to evaluate as literal text.",
                "tags": ["power-automate", "expressions", "interpolation"],
            },
            {
                "memory_type": "fact",
                "content": "In Copilot Studio topic YAML: `flowId` is the Dataverse `botcomponentid` of the flow's Tool reference — NOT the Power Automate flow GUID. Look up via `botcomponents?$filter=componenttype eq 9`.",
                "tags": ["copilot-studio", "topic-yaml", "flowId", "botcomponent"],
            },
            {
                "memory_type": "fact",
                "content": "Copilot Studio Power Fx binding in topic YAML: `=Topic.VarName` prefix means Power Fx expression. `\"literal string\"` (quoted, no `=`) is literal text. Numbers must be cast explicitly: `=Text(Topic.NumVar)` — passing an integer to a string input crashes the publish.",
                "tags": ["copilot-studio", "topic-yaml", "power-fx", "type-casting"],
            },
            {
                "memory_type": "gotcha",
                "content": "Generative orchestration: every Question node must have `interruptionPolicy.allowInterruption: true` or the orchestrator cannot route away from that topic mid-conversation. The default is non-interruptible — always override explicitly.",
                "tags": ["copilot-studio", "generative-orchestration", "interruption-policy"],
            },
            {
                "memory_type": "fact",
                "content": "For multi-agent disambiguation in a multi-product agent suite, use agent-level instructions to route queries rather than trigger phrase engineering. Orchestrator model uses instructions as semantic anchors — scales far better than managing hundreds of trigger phrases.",
                "tags": ["copilot-studio", "multi-agent", "orchestration", "disambiguation"],
            },
            {
                "memory_type": "fact",
                "content": "OData filters on Dataverse: string columns use quotes (`ascend_frgst eq '100000'`), integer columns do not (`ascend_amount eq 5000`). Many SAP-mirror columns are stored as String even though they look numeric — verify column type via EntityDefinitions API before writing filters.",
                "tags": ["dataverse", "odata", "filter", "d365"],
            },
            {
                "memory_type": "gotcha",
                "content": "CS automation rule: STOP and hand off to the user when the same publish error repeats after 2 attempts, OR when errors include 'Binding X is not found, refresh this flow' or 'Input variable X is of incorrect type: Unspecified'. These cannot be fixed programmatically — provide a precise click-by-click UI checklist instead.",
                "tags": ["copilot-studio", "publish", "error-handling", "workflow"],
            },
            {
                "memory_type": "fact",
                "content": "Token acquisition for PA/Dataverse in PowerShell: `$paToken = az account get-access-token --resource 'https://service.flow.microsoft.com/' --query accessToken -o tsv`. Dataverse needs the org-specific resource: `--resource 'https://orgXXXXXXXX.crm.dynamics.com'`. Both expire in ~60 min — refresh per session.",
                "tags": ["power-automate", "dataverse", "authentication", "tokens", "powershell"],
            },
        ],
    },
    {
        "id": "pp_transpiler_facts",
        "name": "Power Platform Transpiler Reference Card",
        "version": "1.0.0",
        "category": "power-platform",
        "description": "RAPP agent transpiler targets, output formats, and Power Platform Code Apps facts.",
        "memories": [
            {
                "memory_type": "fact",
                "content": "RAPP AgentTranspilerAgent supports 6 output targets: m365_copilot (declarative agent), copilot_studio (topic YAML), azure_foundry (Python agent), cowork_skill (SKILL.md for OneDrive), mcp_app (MCP server + HTML widgets), power_apps_code_app (React + Fluent 2). All live in agents/agent_transpiler_agent.py.",
                "tags": ["rapp", "transpiler", "platforms", "targets"],
            },
            {
                "memory_type": "fact",
                "content": "Power Apps Code Apps (code_app target) generate: src/App.tsx, src/rappClient.ts, src/components/AgentPanel.tsx, src/types.ts, package.json, tsconfig.json, m365agents.yml, README.md. Deploy via `npx @microsoft/power-apps push`. Requires Power Apps Premium license.",
                "tags": ["power-apps", "code-app", "deployment", "files"],
            },
            {
                "memory_type": "fact",
                "content": "Code Apps use React + Fluent UI v2. They run inside Power Platform with automatic Entra ID authentication and access to 1,500+ connectors. No separate auth story needed — platform handles it. Shareable via Power Platform environment.",
                "tags": ["power-apps", "code-app", "auth", "fluent-ui"],
            },
            {
                "memory_type": "fact",
                "content": "Code Apps connect to RAPP via rappClient.ts: POST to the brainstem function endpoint with user_input and conversation_history. The function key is stored as a Power Platform environment variable — never hardcoded in client code.",
                "tags": ["power-apps", "code-app", "rapp-client", "security"],
            },
            {
                "memory_type": "fact",
                "content": "MCP App target (mcp_app) generates an MCP server with sandboxed HTML widgets rendered inline in M365 Copilot Chat (announced Apr 2026). Widgets are attached via tool-result `meta.ui` property — backward compatible with text-only MCP clients. Best for KPI tiles, forms, data tables.",
                "tags": ["mcp-app", "m365-copilot", "widgets", "inline-ui"],
            },
            {
                "memory_type": "fact",
                "content": "CoWork Skill target (cowork_skill) generates a SKILL.md package deployable to OneDrive at /Documents/Cowork/skills/{slug}/SKILL.md. Zero infrastructure — just OneDrive. Perfect for individual demos and personal productivity workflows.",
                "tags": ["cowork", "skill", "onedrive", "zero-infra"],
            },
            {
                "memory_type": "fact",
                "content": "Copilot Studio transpile output goes to transpiled/{agent_name}/ containing: agent.mcs.yml (orchestrator), topics/*.mcs.yml (per intent), connector.json. After transpile, clone the target CS agent via VS Code CS extension, then copy YAML into copilotstudioclones/{agent}/.",
                "tags": ["copilot-studio", "transpiler", "output-path", "workflow"],
            },
            {
                "memory_type": "fact",
                "content": "Fast path for new agent generation: RAPP action='transcript_to_agent' with parameters: transcript (inline text or project_id path), project_id, customer_name, agent_priority. All outputs land in rapp_projects/{project_id}/outputs/. Also deploys to agents/ and demos/ by default.",
                "tags": ["rapp", "transcript-to-agent", "fast-path"],
            },
            {
                "memory_type": "fact",
                "content": "When generating Code Apps for D365/Dataverse: check customer-specific knowledge_base/*.md (primary demo env) and *_gold_template.md (baseline template) files for environment-specific column names and entity schemas before generating queries.",
                "tags": ["code-app", "d365", "dataverse", "knowledge-base"],
            },
        ],
    },
    {
        "id": "d365_demo_patterns",
        "name": "D365 Demo Provisioning Patterns",
        "version": "1.0.0",
        "category": "d365",
        "description": "D365 Customer Service demo provisioning order, entity dependencies, CS Toolkit base template requirements, and data integrity checks.",
        "memories": [
            {
                "memory_type": "fact",
                "content": "D365 demo provisioning uses PowerShell scripts in d365/scripts/. Master orchestrator is 00-Setup.ps1. Run full setup: `00-Setup.ps1 -Customer {name}`. Resume from step N: `-From N`. Run single step: `-Only N`. Always run from d365/scripts/ working directory.",
                "tags": ["d365", "provisioning", "powershell", "setup"],
            },
            {
                "memory_type": "fact",
                "content": "D365 provisioning dependency order (must not skip): (1) Accounts, (2) Contacts linked to Accounts, (3) Cases linked to Contacts+Accounts, (4) Queues, (5) Assets with serial numbers linked to Accounts, (6) Orders with Order Products (line items), (7) Knowledge Articles, (8) CS Toolkit Forms. Never create Assets or Orders before Accounts exist.",
                "tags": ["d365", "provisioning", "dependency-order", "entities"],
            },
            {
                "memory_type": "fact",
                "content": "CS Toolkit base template minimum data requirements for a working demo: at least 1 Account with Address, 1+ Contacts per Account, 2+ open Cases (one in queue, one in progress), 1+ Assets with serial numbers per Account, 1+ Orders with at least 2 Order Products (line items) per Account. Bare Orders without line items will NOT populate CS Toolkit properly.",
                "tags": ["d365", "cs-toolkit", "base-template", "minimum-data"],
            },
            {
                "memory_type": "fact",
                "content": "Assets must have: (1) a serial number, (2) link to parent Account (msdyn_account), (3) a Product record (msdyn_product). Assets without serial numbers won't appear properly in CS Toolkit asset views. Verify with: GET /api/data/v9.2/msdyn_customerassets?$select=msdyn_name,msdyn_serialnumber,_msdyn_account_value",
                "tags": ["d365", "assets", "serial-numbers", "cs-toolkit"],
            },
            {
                "memory_type": "fact",
                "content": "DataverseHelper.psm1 is the shared auth/CRUD module — always import before any other provisioning script. Provides: Get-DataverseToken (uses az account get-access-token), Find-OrCreate-Record (idempotent upsert by name), Invoke-DataverseRequest (wrapper with retry). Token expires in 60 min — scripts auto-refresh if running long sessions.",
                "tags": ["d365", "dataverse", "powershell", "auth", "dataversehelper"],
            },
            {
                "memory_type": "fact",
                "content": "Customer D365 assets live at customers/{name}/d365/: config/environment.json (org URL, brands, SLA timings), data/ (exported record IDs post-provisioning), demo-assets/ (demo scripts, guides), copilot-studio/ (CS agent YAML topics). Always read environment.json before provisioning to get the correct org URL.",
                "tags": ["d365", "customer", "file-structure", "environment-config"],
            },
            {
                "memory_type": "fact",
                "content": "D365DemoPrep agent wraps the PowerShell scripts and Dataverse API. Actions: list_customers, get_config, validate_environment, provision_data, run_powershell (step 1-25). Prerequisite: `az login` must be done before calling any action — Dataverse uses AzureCliCredential.",
                "tags": ["d365", "demo-prep-agent", "actions", "auth"],
            },
            {
                "memory_type": "fact",
                "content": "D365 orchestrator pattern: before provisioning, the orchestrator should ask: (1) Which customer/environment? (2) Demo storyline (plumbing, HVAC, manufacturing, etc.)? (3) CS Toolkit needed? (4) Copilot Studio agents needed? Then provision in dependency order and run connectivity checks at the end to verify CS Toolkit will have real data.",
                "tags": ["d365", "orchestrator", "provisioning-flow", "questions"],
            },
            {
                "memory_type": "fact",
                "content": "Post-provisioning connectivity check queries: Cases linked to contacts AND accounts (msdyn_contact + customerid), Orders with at least 1 salesorderdetail (line item), Assets with serial numbers linked to accounts. If any check fails, run the relevant fix script (fix-*.ps1 in d365/scripts/) before demoing.",
                "tags": ["d365", "validation", "connectivity-check", "post-provisioning"],
            },
            {
                "memory_type": "fact",
                "content": "Demo guide generation: after provisioning, generate a demo guide using the ScriptedDemoAgent or demo template in d365/templates/. The guide should include: (1) environment URL, (2) test user credentials, (3) step-by-step demo flow with expected outcomes, (4) known gotchas per storyline, (5) data reset instructions.",
                "tags": ["d365", "demo-guide", "documentation", "scripted-demo"],
            },
        ],
    },
    {
        "id": "dataverse_mcp_facts",
        "name": "Dataverse MCP Plugin & Agent Data Platform",
        "version": "1.0.0",
        "category": "dataverse",
        "description": "Dataverse Plugin for coding agents (public preview, May 2026). 4-tool plugin, MCP server patterns, Python SDK, PAC CLI gestures.",
        "source": "https://www.microsoft.com/en-us/power-platform/blog/2026/05/05/dataverse-agent-data-platform/",
        "memories": [
            {
                "memory_type": "fact",
                "content": "The Dataverse Plugin for coding agents (public preview, May 2026) is a single open-source plugin that gives any coding agent (Copilot Chat, Claude, Cursor) full Dataverse fluency. It packages 4 tools the agent picks from automatically: (1) Dataverse MCP Server for ad-hoc discovery/NL queries, (2) Dataverse CLI (preview) for data-plane actions, (3) Python SDK for batch/scripted ops, (4) PAC CLI for admin gestures like solution export and environment management.",
                "tags": ["dataverse", "mcp", "coding-agent", "plugin", "preview-2026"],
            },
            {
                "memory_type": "fact",
                "content": "Install the Dataverse coding-agent plugin from its GitHub repo (microsoft/dataverse-agent-plugin or via VS Code MCP extension). Once installed, the coding agent can query any Dataverse org you have az login access to — no separate API key needed. Auth chain: Azure CLI credential → Managed Identity → DefaultAzureCredential.",
                "tags": ["dataverse", "mcp", "install", "auth"],
            },
            {
                "memory_type": "fact",
                "content": "Dataverse MCP Server supports natural-language queries against tables. Prompt pattern: 'List the first 10 records from the Account entity in my Dataverse org' → MCP server translates to OData GET and returns structured JSON. Best for discovery, ad-hoc lookups, and schema inspection without writing code.",
                "tags": ["dataverse", "mcp", "natural-language", "odata", "discovery"],
            },
            {
                "memory_type": "fact",
                "content": "Dataverse CLI (`dataverse`) is the data-plane complement to PAC CLI. Key commands: `dataverse entity list` (list all tables), `dataverse record query --entity account --filter 'name eq \"Contoso\"'` (OData query), `dataverse record create/update/delete`. Use for interactive developer workflows and scripted provisioning that previously required PS + Dataverse Web API calls.",
                "tags": ["dataverse", "cli", "data-plane", "crud"],
            },
            {
                "memory_type": "fact",
                "content": "PAC CLI covers admin/ALM gestures: `pac solution export`, `pac solution import`, `pac env list`, `pac env select`, `pac auth create`. The Dataverse plugin routes admin-intent prompts to PAC CLI automatically. You do NOT need to specify which tool to use — the plugin infers from intent.",
                "tags": ["dataverse", "pac-cli", "alm", "solution", "environment"],
            },
            {
                "memory_type": "fact",
                "content": "Dataverse Python SDK supports: `DataverseClient.list_records(entity, filter)`, `create_record(entity, data)`, `update_record(entity, id, data)`, `delete_record(entity, id)`, `execute_action(action_name, params)`. RAPP ships a portable DataverseClient at utils/dataverse_client.py — use that instead of raw requests.",
                "tags": ["dataverse", "python-sdk", "DataverseClient", "rapp"],
            },
            {
                "memory_type": "pattern",
                "content": "RAPP D365 build pattern with Dataverse plugin: (1) Use MCP Server to discover live entity schema before writing agent code — avoids hardcoded column name mismatches. (2) Use `dataverse entity list` to enumerate available tables. (3) Pass discovered schema into the RAPP `generate_agent_code` prompt so generated code targets real column names. (4) Use Python SDK for runtime CRUD inside the agent's `perform()` method.",
                "tags": ["rapp", "dataverse", "d365", "agent-build", "pattern"],
            },
            {
                "memory_type": "pattern",
                "content": "D365DemoPrepAgent extension pattern: add action `discover_schema` that calls `DataverseClient.get_entity_metadata(entity_logical_name)` → returns column names, types, picklist values. Feed this into the model to generate accurate OData filters and demo data that matches the actual org schema. Eliminates the class of bugs where provisioning scripts fail because a column was renamed or is a different type than expected.",
                "tags": ["rapp", "D365DemoPrepAgent", "discover_schema", "dataverse", "pattern"],
            },
            {
                "memory_type": "fact",
                "content": "Dataverse entity metadata endpoint: `GET {org_url}/api/data/v9.2/EntityDefinitions(LogicalName='{entity}')/Attributes?$select=LogicalName,AttributeType,DisplayName,SchemaName`. Returns all column metadata. For picklist options: append `microsoft.dynamics.crm.PicklistAttributeMetadata/OptionSet` to the $expand. Use this when you need to know if a column is String/Integer/Boolean before writing OData filters.",
                "tags": ["dataverse", "metadata", "entity-definitions", "columns", "odata"],
            },
            {
                "memory_type": "fact",
                "content": "Dataverse MCP Server connection string format: `mcp://dataverse?org={org_url}&auth=cli`. The org URL is the Dataverse environment URL (e.g., `https://orgXXXXXX.crm.dynamics.com`). Set DATAVERSE_ENVIRONMENT_URL env var or pass explicitly. Same URL used by RAPP's utils/dataverse_client.py DATAVERSE_ENVIRONMENT_URL env var.",
                "tags": ["dataverse", "mcp", "connection", "org-url", "env-var"],
            },
            {
                "memory_type": "pattern",
                "content": "When building a new D365-connected RAPP agent: (1) `pac env select --environment {org_url}` to set context, (2) `dataverse entity list` to see available tables, (3) MCP query to sample 5 records and understand shape, (4) generate agent code using DataverseClient, (5) test with `D365DemoPrepAgent action=validate_environment` before deploying. This replaces the previous 'write code + guess column names + fail + fix' loop.",
                "tags": ["rapp", "d365", "agent-build", "workflow", "dataverse-plugin"],
            },
            {
                "memory_type": "fact",
                "content": "Dataverse Plugin vs direct Web API: the plugin is for coding-time intelligence (schema discovery, ad-hoc queries during development). The Python SDK / DataverseClient is for runtime operations inside deployed agents. They complement each other — use the plugin to design the agent, use the SDK to run it.",
                "tags": ["dataverse", "plugin", "sdk", "runtime-vs-design-time"],
            },
            {
                "memory_type": "fact",
                "content": "RAPP existing Dataverse infrastructure: utils/dataverse_client.py (portable Python Web API client, auth via AzureCliCredential chain), d365/utils/dataverse_auth.py (token helper), d365/scripts/DataverseHelper.psm1 (PowerShell module with Find-OrCreate-Record). The new Dataverse Plugin complements these — it's the discovery layer; the existing utils are the execution layer.",
                "tags": ["rapp", "dataverse", "existing-infrastructure", "dataverse_client", "d365"],
            },
        ],
    },
]


class NeuronAgent(BasicAgent):
    def __init__(self):
        self.name = 'Neuron'
        self.metadata = {
            "name": self.name,
            "description": "Returns a compact [Knowledge Base] block of embedded RAPPNeurons for system-prompt injection.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "Filter to one neuron category (e.g., 'copilot-studio', 'dataverse', 'd365', 'power-platform'). Omit for all."
                    },
                    "tags": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Filter individual memories by tag. ANY-match: a memory is included if it has at least one of these tags."
                    },
                    "memory_type": {
                        "type": "string",
                        "description": "Filter by memory_type ('fact', 'gotcha', 'pattern'). Omit for all."
                    },
                    "list": {
                        "type": "boolean",
                        "description": "If true, just list the installed neurons (id, name, category, memory count) instead of the full Knowledge Base block."
                    }
                },
                "required": []
            }
        }
        self._cached_default = None
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        if kwargs.get('list'):
            return self._list_neurons()

        category = kwargs.get('category')
        tags = set(kwargs.get('tags') or [])
        memory_type = kwargs.get('memory_type')

        if not category and not tags and not memory_type and self._cached_default:
            return self._cached_default

        block = self._format(category=category, tags=tags, memory_type=memory_type)

        if not category and not tags and not memory_type:
            self._cached_default = block
        return block

    def _list_neurons(self):
        lines = [f"{len(NEURONS)} neuron(s) installed:"]
        for n in NEURONS:
            lines.append(f"  • {n['id']} ({n['category']}) — {len(n['memories'])} memories — v{n['version']}")
        return "\n".join(lines)

    def _format(self, category=None, tags=None, memory_type=None):
        sections = []
        total = 0
        for neuron in NEURONS:
            if category and neuron.get('category') != category:
                continue
            section_lines = []
            for mem in neuron.get('memories', []):
                if memory_type and mem.get('memory_type') != memory_type:
                    continue
                if tags and not (tags & set(mem.get('tags', []))):
                    continue
                mt = mem.get('memory_type', 'fact')
                section_lines.append(f"  - [{mt}] {mem.get('content', '')}")
                total += 1
            if section_lines:
                sections.append(f"## {neuron['name']} (v{neuron['version']})\n" + "\n".join(section_lines))

        if not sections:
            return "[Knowledge Base]\n(no neurons matched the filter)"
        header = f"[Knowledge Base] — {total} memories across {len(sections)} neuron(s)"
        return header + "\n\n" + "\n\n".join(sections)


if __name__ == '__main__':
    print(NeuronAgent().perform(list=True))
    print()
    print(NeuronAgent().perform(category='copilot-studio', memory_type='gotcha'))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/627iY7s2LEt9iuF82B062V3c0pOMgQ4k/M8j7cvJM5kcp6SZMryt5tZdbrV0vV9MGAXDupkbgZjx45YsSKigP33b9G6lP307c/f7lXTfHhl1GTdt5++pdmcTNWwVH13PjOzZZ26+SP6SPp2iJLl4z+krt+aLC2yj3s0Z//5ETd9Un/0+UfWxlmaZumHedN1NVun/nwx76eP+ZiXrP15mE4Vy0fVPbLkrf6Xc7dsj9qhyeZvf/6P//zpW3V+/vbnv39Lmmg+l759KbkVWbecsk3UFeficJx2vy0dsunU3p5LaZZ/fP/245w1+U8f//N/1ls0FfOf/vxr9/H9p8o/vhZ/KbLlxx+aal5++OPz98/0ed6Pt5Jf/vqW+Gv3dZAf//Rr90/RJFqyop+Oj7/8i8rfln/40z9Fl6iYT7H5fP5H0ffyD3/6OL3zH//5B+k2a8/3/7ocQ/Zvuv/w5Id/seU8Vtcv/zQp6tLPhc+Nf/vyR73vta8DJlFSZulfT/dFa7P8r1zxr5J/3P4r/H/5LvcOQbT8+Jsxf/ntw0+f5vzl/eunPxrzlz98/v90qn8z/v/J6tPIT2P/Kfn9iJ+r3/5x4q+bl2n9BOcbfv/jf3woVTL1c58vH1bSr8vHtHZL1WZvS+2ymj/Of0uZnYqe2TRXcZN9lzux/h3l78z42/8RnzkGfEHpr9Ebz3/75cM+X+ynqqi6qPnMmV+7z0dvpcOUzdn0PJMpPpbs59OtP78/nMnz8bc/qvllOP726Y7zwdsQkxJOnw3z2mS/vI30yqz7blISdR/ZniXrqeY88LlnXp2Z99Np/Nw3z+x8/9x4rt9skFbTaf1vfj8P/ee3sr/97W9xNJe/dl8piHx8McUMnAK/m/Px85noWd5URXniJEvK/uOHv//jh4//8+N/9dan8vce+pn53116Wihamvpx5sDanmKnt8/4ZFH66dK//+O7C081XTZ9nAGo8ir7ermpujpLf/Onxd9+hlHsI85OP54+bId+Wqqu+KiWXz6E/ON3e89N34/edFf28/KRZkPWpVmXHKfW6DzO7558o2+OlmrOT2ivc/a569/iKfo0sf1rcor/7UOh9I+l75vz19vMT6Hz5b6rTvf/Hu2v9VPJ9MP8cf9NxS8f6htUH0M0RUM5Rd/3yKOvuJzE8dvrp/Loo8u2X7s3f2ZvV0Wf/PrpnlPo9EzyPaQ/v2P+5vL2DOz8296fMmempR92H52bT79283f0RtM7FEl/mnJ8FGuVRl2S/e/fITWX/dqkn/47LX1r+h6F9HtUPjH4xeIfv64wCF0/3g6O3onylbzn+ZJ6/vjxDzXjTx/ROwLzGaEm+zL4CyZvZfTUD19I7bvs4423T4EvL7ylZuAr2T6R+zbp96Ccx1z+UMl+7f6bUvZVoLL0S+lbxVcB+/gqYGdg+o/vVQE461uTZtNPv56I+IRndGbPF8B/Oinqo86mLmvOQy5J+ZsHPsP4NlqwviO9OAvNdHyezz6PkaYf9W+W/fkjGt4gPO1Oq7P8frdIZRxTU62Pd4k6cd302y8fzMl23w07KeQdwib/+aucx2+0/1ilp01Rm/308clWfffTxz/5+TMcZ/6c5eiXD+X7l/P59CaBX7s/FpAff/32huGv386k/vVb0Z9ni75/OQ96wqf79duffvrIpyz7ecn2M2H6bjlD89NXTE4G/7V759OpvWlOSz6p6fTI+eYZ1S83lNnvHcdXTXk/PL1UDfO71P/8HT3paT/wZuTT2dWZIj/O0fM0+/+6gv/b6ao6686tnt85ISuiM5G/v/il9E+fFhVTv55q3+l2UtTbVeuZ9dMnwv4VIr925ck/J64/rDWes3F9Z+BvncefPs8zf6bMV+V5dzhNlZxWZN/+3K1N89O3t/9/72zeTcyZ3m12Hm5+Nz4nwk5tS5V9fvstOO/P/9qWsV/OOsHwtvF7zH+vlT9mvxS//PTxQ9IPVdMvP8/Lmlb9D+fK6a7oHfvs8wuCoe//h347HTo00fI+xg9n+LW2+nT7x3me9xneUT93fbv/bMH+8T7UvPxXq04qPcvnCa/HeqLyE5pvx39PizOhvmfNH5H4bwA8zqifJfZPf6T6z3w5nfdvsfjK1j+YF59Mm0Xd274/oPW/dV58/EtX9OMPb0y//fEF6E/PfKH5/5VL3rD+b/equrR6Vul6lrTf8uy9//nOLx83Nfi5ffPDmeq/OeHdWXRJs7676bMTOrcu35x4OjU7+fkz6F+OeVeFc+O3RdVJUZ8W/FfTvhbOVI6Ob/84F6YTuWc5SL+67u+P+/hNe2/536DwVnZiM3qj5js6vzc1p/gUTT/P7yoAQL+A5/bn969qfj77r+3Od4G5jM5CfEpkYJTjKIlj1xRPYATDUTS5whkGgihC5gl2jfAcwtM0Qc6oICgB4niOxTASp0ScxMh7w7lfpyT767uWVe9Nt36qzwP/vJy088/H51L63dovQ97n/727ep/qu9F//xZj11OSv87C7euHAi5uiiNxvA8+MI1ZEKaa9bh1Vjos4LFf0xJlZ3NfQqcC0SjNd8FiC4sSqJsR0BYXkdjadnlwI/NAJBcaF5HlQipASYNTXC/awZNJK1rcbWvlBsiBXOsy5gmpAEA2OWbjYNKF8KDfxjXVriua68LI1U4EukDudeULsSwa8qKId172pfMwpgrHo9Lc0N6gWHX1mrDzcX9qwNTnyAo4TGovzijbFASFa7kj0Gtg2NTpxv5KOoqL2kgjHisxoRqWNqB7YWp9IvCuTWMJ5YehXOy0x3FMe2qPkrrOLpdKJDI5dkbzeuxvBam/Np9zWI4EJhzT6wdFKo4OAXmzL1fSfOkqoZmbsuoMoebdtmwkcIGLDUKw5AV5QTRqliplZntf06uDEPJRHR7f2AmCK6/9OV6pXnVJVM33uCEu0sFjHv1iiVUPXsID1lI6O7rn0E4AJPnPobH9K4BjwwySLzrnJ4gLwykKGXO9QsCkPWarr/sLRDoJDAZXY0MsTX51B4tpfoHXWML6DWFLRiTJMoNwuQQDPlU/XZ8ISQpIjy1oKaTArpfRyn18scyOvQcgCHrki01epE/BoOIbecdqbJ90de5N8AlxbHdJYRkCDE4wrqtkrUPhzMeKewp4q2lC9fUoQ7ZrppGdyHwioQuytrYU+YQxHBYum8KjX0HC7tkFBa9Uvvicy/a9CM45ZYNSpU0wDg7G/kxVk+wHlDe1C6azkr/3g++jiEkISS5kiWcVeI/6qVPpl/wMAuSNoC0OD+wCAcAwhEPzXH1Ru8pPp3o17oRtpr9TbSh4Q73CRn3YVCiFEw97tMsQzximJxWUzJ7uN6OcHlYnZGt9VOyJtU6OxvCVMs/KiACFhFCgxQxkNlAxnAD44WMPua7HCasmHvGMGnXGJeXmi842ZgG0ue9ZUssBnFstuAabTvNk3SMW+tbXsg5rZtDmVYUhWl13QHPVycsjsZ7KrHQtfBaDFNQftMPCqGKArhRJrZYX40MQEzjmEp1HIOJp177ig508OYk/2S5IkliDcaY47iFiEKQjqYm7WXfX6YrF31nYGCfwzBjUmKML3WV1zOBbbQstlD0PBr8k4qXP5zBJ4pzZI5UgXWsE0clqzal2m+l1WlEnRB75AmrHuotbbRAcZFegt9M2rhLB1xbCwbPcrlxMCWq7FdXtBfG+YieRJ3kSaJuxwqZ1E1iCAYJQrFnMIvV3pAUFWbPN0UL4tNR7AD/aawaI+pBgiT375tw62N7l0/04aYJMuxqcj20Z2VQdKEq/P3vHSgoajPqB4Z81r5Waj4J+A8aAq1KMci9BaO0On6kipayIQMJpfTSJGCYIcVFsO+luDyId/ZMsC4ydOW/cCY6XYHYVYP/h5ORjPHxouyMJ8giWKbBb3nyaCYByOF+HLZevZ0+y3FWpIkbQifBQ5WW1h3i3iufUuzXy0XRX984NgsdLtixRsZ6JVz8IjYMyABJR0qvBhbS7mM7YCEMLV7IwXuOoNmhHe70uLdrnNXsVZq1/FrF04fF1x/tEBS0unqCVMtRYtySzC8uxsaaq9p/uykvh8GjECgcY9hB5usTL5KBoctt0vkkpFYkvxDo/n5c773Qy5j+7gnvN0nAYQSjeTwAi60BIeo8eoLBIIcLOZ8ttrestCC1nYV5tO9fwolxBRKTbCrQL0VJCPHN3ir854IOqDnw8KxOyYE7F5aoXk7ALOjLHAJtUDNwqS2c5SeZtQrGXR5h1piOmxeiv6yHCVDPceLaUpWHC2VsMTjmHNTxa8+PlklKRQWMzAs/WNLfUuHhRwqO0sOYpqKyJQzOmJextGwM3TRAhzz+K13y7qtCJndUTLoDja6bC10Pqt5g5LqVHlyAbGmQex1ypIvcI6wLEabTjyNrOrCyRve1s/qSkm7LlVQttpn6Hx+Ryn5QrizptazJkaULI1dtOmMP8fL3RhM1KL/cW10rWsMbSsHLPj4dNErYp8R3nDLIOS0G/GphSspG2EK96YOpB7aTXrS7GFzDJFJgLoyakmM/GFLZSi1KYnOdIgXSDaWG5dg8XASPNaRXEdTDwACSOTPBSrYl+AweV1Znrlb5rAHkAMHkFCrjrUGlvyhJFD5PSihuIXlJweN4AqFb2DfITRbR2jW9ruMB1QeZzuiLNA3mJuSzD2KOqzmlhuICmNlmKuA9G89ie0rFAt5YIc+YWCHbCY51IpIDQA1f3oT/KcXqN1LJ5dqkxNZ3kiFcDTzwHMI1q1eqyOUhC+d5sGXPGSK+toJyCxpKnm6X7AsSGdWZt20t2xVXl/ca+6NdhPBidqiENkil8oEKMEgYNspWOMg7jdXlZ2XVojRQzdm/oSbfRcpAB+wekvDRePm59nO7lC7Cw1L7D3o3wLxf5xoJRAPBbgdSvvOz3jO6sUqO7ApDBbqm3bCSJLR4xUpNj0q7rVZIqc0x5aRQpZWVulBRqnJiGtZHgAnjhbILiNbM9mMLwYezWp5FiO0FQBggbmjx76x6+LTQ300vuBB9D/CU7fTbqN7+uKn8Vn24zNsVOUO6N4uXmMgxc+ygTNk1k7oAyW1eGh+5xrV1TLWWZ4IHd8aisfbNGsqx4PkrreSg7W4DbZI1JfUObthQB8pbAYsk28MG2IDK0JmXHstZf87TyHvo9ZS6P08MTPfdzXs62cbxE/S5S1w2znpVIQZLX3sHwjou3tRQuNiioqh6M1XYVXJPP6+llA6tPO/E8IZVuqgjnRIp6p5iOKeEWsxyeTIdatB4atcTV2QrfLCRoNVt6vVYruF5YzUQf1OXGOzUJG+ILDPw7CRTMY24s/W6UVjOsJx5a4aXBJ/fSSqsQ0UNrqs5OnkIYJZJNOayNu5eyuKigOYbLwhiOo8D4BMb7IyaOTp6v+mtA8+fLuRDaBF7XrgQ8LT5kjV05qHeTOQ4e0kZ6nBcxfrNPVhwRKhTZpBtS1sOW7nhT7bhsxy/Ev/Bm56nciqwgmS3k0zg2RjQiPsbthCQtpRS4CboUSIpPQXeeqfNfTCHKaOitwmN9OldehZfCMvSjf/9BLVPN/MF5DxrFSjBCGNQpL63Cq4kkGO6d3vpn71b2RN4ro4rHyblgxogeRKHeHZOyDOyWYxwILDKKuZBE3FkrVVcMOUtchWWgLmfTw/QM5QIgUYbu3NbEnlnPnNsr+CQenH32pkhPuMUC56M3q9p6UCyYi2tx8rLOdWCwPIQqd7CjrK0tiFyZybToSiRq0PVl4IiP0bBUuhdq6LHddIph6qK6K4pxnSGBKCRAf7mgx+UuzZHOaHIFs6rADNuvw7zPLJldy4MB6o7El2tWXPJuyjd2vKqKo8gc1nt4r+9Yp9zrLA89Ld9C0YE8nAUKDyBw/TWXoOUFxtl+I+PIkkVrNiDpE4vFK4+HyQoLm4xXLCgJVHj5YYecqd8HtxHVqAcbtrvS5LelM/3L6AvUHb2Ujl6aAxzSL6ftQ6brMzuL8b6miIj2KeVQvIvfMZK7eaFNhsJd6alFBHiD5EbMXS/G9toUTg5WEbmOWYIJmdwclHdyPqMNd6x4OroojTXA8tZgaoGbDOM2tQlb4nsnuSwCWcnV1MRghVGTcQTl3ukNdTknFiq5RXuLMrZIoxJYm2uctPVDE4qe5KoadFex2AetPIcItrs9AwvfR466wqTiQ0NuJmzvYfvziRNt44FzOIFSAKZ+FCGD3D23FTonWscjaVAgWny0bwewCkdb+lVWP6acX/OeW4K73NR+9TiHPn9QTLygIFQ5OS8MWoc9u2IOmSW12ya1crUINzfMUFiNs8AV3Vsr2qd9UGOjwq/YlKuQ4QtWtZEzyWDZXlKFHdI4IapF10YUV4M3HIzvbh1Hx9RYeXmOOnRTd2YqtlwrUTBVcVdlIy/uyaaUMpIpCld2Ky8lSg1pDRJpcI/KBFLvYWdRagU6laOg1EzgjPiqjFJTB7VX9wvYQvwLYZ5AVMPHojbIvNl0PUolcLBHd0/sF3S3wcOIgiRC465/qU/Gc0PvAYtPYS67UriJ57h5IA+PqPqJTfSnmHhUSbHFY5Gv/aWTyFEOoITp9Mr3UGyhleciipSwnzNc1ZW6AWl9W+3Fw4NEopU19cllUnzZ5EvKHGzc2xjSbP78tJ2woBk+vZx9PoyUx/3Kk1lFMYinBZ6qKiQIPheBYAtmv61XggppBDNgkNuLqShAMr7A3RTrJxml4EiIGRkMdlBVKR3NCr/0mGHaumoPbOz45/jEFfNL1dsyG5wi66+9d8PjmLfUdI0xp1NHEX7VSslw1aarYLueZA2sekKN5+g7PpXVFcE2dsFMSinsen3QF/vJp81QoUffb5r9MrQ4vG8OHPked1khOqOwlyXRwHUMCsV62bzNZQ8jcF5+aiuFdb8/iIv3fBzQBGwAiCn38SIqKIrrZ/OjuwjmoDuPgJXwwNUGtvCi1tXU7PXTLp8w72c9BdsuE8kbEqkKPav1JMaIIL0OS+tUtXcYiJfloI+5NdPCUCxy6Rls3KohKqRHOtkQwHEPyRbYtozP4suTwIa84p7ci4ncCWoOIq/X1UNdpivBeS7cpkgJwugxfva44h4UpNQekHwS//36XMP4AgTS/pQp4tm0+navfMLB4JMy0ups8u5XMjnWOapkomRrkUOMRLt31yiblehYEHwHHhEzpi7vtqy/hlAR4YMTytB1VWURW+14vYE37FUim62TJrbtiGWfI4D86h2SXUOBl5h5ocwOGcL23qmsISvr8og20hFJ846zz/pojAKC0+djdoORubpFelcBgmSHOZ0FprG1KeBGvneGVplDR0oJ+KI/zoGtQm/Q5WGb5d6SZdMvxeoH/oG6KOHf20DkmEedjxyx+uUxtceDUaTaTHZafd0rUe66YkgCCzV0SNYiCCLSFOXKqmrg1fO6OXkAwBishQTJ6KyGBRrAbu8f27N7CHDLDauoMFVgC7W0SNujb6RzFPc931TDu8YWR+/YBBIjT+kkuWS/cy298OxgjRE/UUWnt2f5mjuFftEPl7sbrj0JL8QRtkW4oQunALMrtJYvNJm8Smmml2D67ErpQQXTGKb7Osi97rYX1724ahcWD1NqZ+uldMwrs9CEmwgEklVNHtnCsLam5c5xXQNz/UjFdaQReUNpfo5vAWs4XvjI96emOIUWRYsox88OVyyOZk2nq9eMbyFiE1G8TvjbeCPPvpw34XFY2NY4zAs1070TkGcroDieZTAGK83ccNQDOwTmcHdBunmAdweXNyF70HoikR0kkFKx6edQ0lVuYpwgogO4c3feC8fbJJ4DxTn4JBVWVG7KrLAnD+a935fAruFXf7jU+HpEEouFrNDOCJr2voKNo9VqGnTTFyViuZrdKPwpoxKBsFHjMgTFjO5R2DSzGrZUuMFAsxTySKiFABpLTfJDJgltDOm+Vxpjxq+35wxgBRiOw4N31AaK78rIDVnRNmulSr6U3V+I5xhWLbv0oLDW7hWvYj5czh2J7YbWxvWmyRzV9rDH3kEi1/eGPfMOLFxKNXo/pEGvH7guMra5hGwxlNjXEyKZQ572bIgK0lmPhs4ZpmqL2jAketdElSJVSjUft1oswHl9Sm7ZlkCx7B6I0qymXw2fvDml7d8eSH2O2ZhmXe/Qc/YCQAVZuBXm2gU5tjtJhsx8NHxVE+oFCU1H0ciUZ6wwnQnO1ry+XNFZuDcTwZZcachkU/OISt6qQuBwcE9e3JWfxvVyqUlHrm1R1ZUmAEWhdDtQAMRlmteLtuihyyxpe0qYBOtdkwQsamc8SNGinNGP9Yj3SurluzQIBobITUIbhEXiUwm2S8+dSx2X74HdR++5PHCqcfVerjZIR/ksryJciFcahDfOx0NGHORyi27zym4snodm6wL1uLWrwsxIQWD9fRs8oSRkAZT7di9vDPwqMJkkZdp/7JwT+1ZxOW7F3vbBI++MWer7tXZ7Q1m5wORLdksTv3e5SZuoq5BprvYIERvP6EzKAo4prSiI2fm5zsXF7CwcqXaPXKGB51DXskQxFEsR13N0YF8dfZYNggNim5Vdz787rLe4ShrZFu6Zqks2o3Ak94MF2OuNeAqSEsyg1EC95/HT4dHccezS1a6ZGj9tLIvIjKNgJMqFJyxznPK48EBsE5R2icIbNpzTp6x6c3fVIM2XxAh4FlmIPhosc9tOPvs9x5NrmuxAXfM9wmpjqBZZIXeKNmfvsueL63CYe+Pd+nF/8eNJ30Pv1eE5xBEsI1hXhUoGyoJmgJ/Psrrj7cKvlJcp1eFJKLzmdDA1rN9KKtYnIFnMacXRTsfDEFuf4+hOTkys4HiADN52aWFkkswOKiYUeNX6zcD4s8cKoNV60o56y0UbYeRaA/WKDgPWeXUxMZfpvBHHCOQtr1fqHY0ArNktZ5bvoQ8KURBKSZ1D2dj09DUwMGzxneC6iKZr+x5oauBLdF/UfOU3eGF1JkLTgRrwFV33axKp3pVi6msLJr0K3PKSKGYYuyrycTEYwbisLI1Dr26PJUAViL6VLIGaPeF+9we4uavYlLkuKuO8P8OPx1XdjCGUCRWmEY96qeArp+HQ4i9wU6hIkhFOcMORmAWF4lFenjSb3YsxCO5lg+vMpe6C3rqi067WM5zdQzwRPSVOogfVs/HhWJZdpMVtFGNBuB7Y1RGv15p25qO8TNTtcuNYMbL3hL/Ik9wsRgQMRRhk45SmBkGMtI/bZiIPm888c4V9JkxQ8JZ4Sx4aw9xlnJYhaDrLrHvOEBJJljRJ7xs/PLRBqJlzoIB3G8Xz1Ft9XJKUa4uyKEpe8NR18ft412bb4YOCYY/R3NKmFJKkiye2AYWDvxk9XwxEczP9UbcSYMiGio6YHH3oadgabrnV3s6oi6W+utnOd+l+qVwDo6/eOePpvOgwYaRsZ7NLPRAIY5hGCSh1aVxd96+FGxGVPEDOdRpz4e6QYQzsQjFA4MW96NWteYTYELkgdlTMBRioApLXwrnhezCCtsvu/iOrLc9SnSf1ssOEdUaUtYP5cX1MQbmJPacTpSvVhvLCOaoA6bKcMzmjZ4MCz9alR++yQOeDnAS3tmhJUSzEjZoChOyCRHSVKZxUCN6p+PrQ6sYxdHn1lnqjlS6rprogywGIIXkmcQUievy2NHYEphBP76YVCdMD4rNj76e1XCcU3GaIEHPzxhqJr19WACmKCUmFx52A7Nf1wTEunLvkqhSU93gJkQY0e3AVH9Oq4Qz2bGRPPsCQ7E5Qtffpud1vmJ1H6jlv+yiYOA93M9uaChQtZq4a/0Cx8sZSoPdKFXu1Zd5jhOdDMs9Cwx+ypsAXQyKMPeT1NMPcGD2z94bSpUHMZMgTuqKuRarPBQcfJ/VKNOKK/VmUz3m+ztZA4Inbka1Cv0ZhNyJJyV2RxNYSrg9UWW0d7AUFdWYLlheSjwcrxh2iC2d/Hb8OxDNdvbih1/oeMa8FuXf4GG+0/UrMm7AWUA+3toqnq6DxQlnVFGVJ/fyElaGLIXETiZo2a5cWnZkvkGnlqPom3u/tSRfydceOiWkEf6WJTLKPSOAOeETrbYtG4zA6xRLD+RWXmHhTsmAqJivkIwZ7EZ4p3LB9kl2Zb1AsYkNqiU7OLZ8PZ6q3Izl3SMpHSq33QYeM+IYnFhLeH3NHC15+ayl2ZgMpRcxNfVZZ6kn4dhSHsz6vk1aKB270klAR1+M2p5QYVdxo9deWoMjVPGsVHzsLsJiWtJhjc4uc7s6AUJZZDildwWbacXcgq+l4VIygWw97ZQUG8ngBmEscYBwfqpXX/cGY7Cy0IdVV6T1oalwkFMM8PbTTfeA7IoYnebH1ie0eyyN4TLyS7XcmbO6UcFyB5ygXxna45sT00MEsyhiv+O3JqZnScJuiLuDyjCdqBlGWfMgMmVQeAOTllSUgmcWIiShVkNiJC4EozG08kXV4yw6RJKG+pptj7GLhMz7nAk6W0k99YG+9LqvzI4ZKgQcuVWhruXxb4vJmjF5y6zMFAxlpYDkYOCdhx5euzPNJeR0DpYRQFhgMjgXM1ObsR6LAVmptIQGCp+a4XpFWr69uklsA29NLZDbXV+POwnUR4O0K9zJPFby42vk9Nzy2bGOs5wd3Z4S0C6bogdW20Duc7ZX0hPT4GadLW2qEC8fFnciK3HHBSOe9iKMDOzVMYIpewF0dPeRoHQSLdUTzEgpaFNmPEhNkNydYMBE86RHOpVCra5IfrCtu+xYO2q+zd5nxfRIDq+WiYyS9K3DPDNl1NsePr5pxkkXJR6IsWXO5EbfleNEGk6qpIZ8zFYpYje1Uy4xqNNOQSailOrbz9PJiSx+6Rx66dMW9PQ/3jDUcReM9LG4e2wtccoDUbjD0ESIKZ92J9ljR8exjhhAt6tqjaLcwKDKTo2wvr11JAjO82INVBNbL0HEf5bBFRPsXf/Y/ZGw0DipH297NDpvZCCRhtRj0pDdVA+CU4+s28s8X7HkCfn92iDxIZGp7o57O7sIf1lzh6ziwAC5N8etSFkoU38Y6RJ7Q4GL+vMJoco01Gr80L0yhU/9OmLI43QQsipxtWBOt91U+fSUQ1oSk9lTORmp1ywJcKWrTlEinN+psR+3mSDQld93smYbO9ckty6L3/C0ZDtv2lKrO5HCujXLVNrtlfL9TyVyN+yZm91jTLkNBFp0YRYDphO2TWlGoPauvQpiTUoAojKoQ9siJm4TdmHhg708Ht/HLPAdsGZEVL05VTmHUdmsbUFy7WzaBt8sueDdIewyIzRSLpRvdgLGllOpNueMIg8crMoyeJcEoXDnQdsMywKSgyR5ewmEXBvHqSoFMQdMN1oexDrTGCruFOS4baRFAQzu8tFzF5FEML+B2PySJq2cGNu4JYJwzKjKDqfKaxAEvqOlBACJLK4gwsQS/+jkrZv0OXkVlMKFAe0qhSTywJfCzirmhTv/kgsF2BQ1TcJ/qehiMVkliYHO+WKiYPFym5Jir7+ywtDyFng2wPXCgxe2HRtUeZp0VYXmJIS0OLuXFZC9eUQheSTQa8QJOLkErCiRvK7TSVW/ttlWZO3QO/NVOB15GgPlStRXnmtFJ7Bd93c2jhySIIq5xhF1oZW0QAZKVx3hVLF95hj2PqZUfXImjv0k8OfbIVC4W7EeIdLYfEeFFl32miHpyCVZ+3jZgPSsBYGJHZm5UdO+nx7hshG8L2tWdUrtqnKxGlatGcopvTQMeXve5mtaw0/1zgsHz+Lrq7Fm6r2uNM3uFKUl94KEdx6+6Rs9+IaCk2LGph9RxAhweFKwGKElGUNZE2ewYZUau/LW62be7WOWjgsIl4zE1f1nGBNmqs43sOsQSc5B47VdjTxd4zvW23AOPTqoRUO+jQwJUxp/FC78c/kPpm27vm/uhKiGfkqwglTfYuIUpVZIPv/EFC2R90uO4DRm5EBAYPwy0hK3CbM0dA+mAS09FOHJZZLUiCUc1SJGKBAHNN+aItz3ahBRXTY/c8gNTTPpVBHxM9E/rvrf763I2OwmpBqv1mgLfCnjJEs3LgaKpn7ERdJZXUxGlaqC8Ib9fLq+5po9BlSXeFtsopqO72QBkFe73VpcpmtsIr57YDZzSRIxoxmpS02if2mHTzwcrDRVFrXR5udpIYMn6IVNPsr1dHslshgfAL+7aTIpShhknDllKensnUK99mh5t2b4u1xd2FZut6uK+PW6XXF2ceILgo2ikYRWM9gpfwyc2GZgAe8o9uSNogK36KsliKrPtYxd65QpcPRE5HIWDRus2GK6l24HL7I2UVrFCb/5t6zo/wkeEwkdcecIcKY4c8Lj0axtXGWXXj5kOLBdB8BnoFns58A0JzFfxks4jwlLQNhDqyje9ncTi7Ip9KrNS+fIIpIJ0YYEd8t1zzICdBk1AZNDNm2OKd0G2pNdNv3JRQWXNoWrLYzY7+XXTDgdNEX4xce5sGCdjS+lMROiuHIfJXl5eaiuDWF3vwtPdnwpUX2tsUOA25Lemobv4WWIGg2GumRtX23+4LmXiLL9UVSbwivtcz8GbjmsReoVbqkGMbPcXPrWWEe6aogvEHpWIkDM5AekbN5cGujauXSoBFn/DynnrkCqjVfi+Y+4AcpGdrvRuSGZBs+NMs2S0A5yh6yDLzlRHk7dNvZ0t2ihn09YxwHK228tSl2ld+b4O33ylJ0exjGVEq8mJioVC0ks6wbJ9BEewTBcClUBhjqmQoCKRKgQj2ykrK4dH5qyGVEgBx4sStHrHxtRHrk5es7rmdjSaUxGXKrD1aLUGJC8T0rnatHhGQWNrkOqeXaimoyycG/siXoUphx/zjRT3NKKttgXw/fqIn/bhL8agifO4cJl1uelAzmQ+b5pxPo3IGMNHiZeHzGqs8sgRWLt08LKA6UMXiOq43pV5cIGzLPhdhxd1nGuo+VKBTtNcTTyr6a0Pa0HkqCcabnFSEq4ZusZQr7jPBXp2zlprtIwrXMGYCIR3or8/5XNYdDC0RJQlLIWDLJu920w3oa6ytl7u5gnT642whqZ6yoUzJc+ncwez4xxJN9VjKtzKJ3HCShrIxCLbrwcyto2ZeoBIK2eSZxMmVTnkOxgi4zm7DTgJ+6/oVod3W6SNxK26kiKmMKcW+HnjaIRyy4DkRr94pTrodnIlnUPQDGB3vobVAn3G9yc3GjoTdc51LUuSBOzmkuo7iOrP999Mumm/Zp2wm83lBqXJpQMxIYC6cUCqPgHKVD0JmRmF9VZj5lOV8TlleQRQBspCed+tLy3SMNq28qezdhPAZAq3w5SY0MdYbTpqpaq9XYSGJm1+v/W4t5WZ7lYD13DyLQtG744AAdwgdnPHKBUM18J8Si7DjOIj5RQaXywfNc7aWzz0KQ/Q+zG8nnDTFGaLJsFoUNGkc6vmNiGf0RynZCeuMCQGDD9u1q2DHCHCnjlqi4oM3+cEVK585DNFmKg1FAQqaEvRHR484Y74El0CAos/b2m8w/NDlLWLcM7FdN9JuLlAEJzZj0ehrJXlPR8RaKRdew8s3VJll3kSycYUbMczyQspH/kc3mEFeTZ1x5QT7uHuLbhCd/eU1IbiihSHjPuGm9cGv6EhYVCexqzRRNZ3nJ5DDGpK29b4IbWmYwzGJkhmGaBNWauNWSLnAuZKXX3NdAf7Awu1ZoQUYZA+u3TR+Tp2kFt3OpWyeZqNQf0OTVFD22QR2ktz5frQjSJ1EsUjLCyUmMGIdRqn33tpxOUJJygauAUoD+rj3uyPZccuSzY+neOJzKF7iSkOdlMolLxzUK7wVxMWwQVUZEZkhM2kOi4EN2kTLe25krqv68ygddvZSaG2cNw6Wkb0wBaq3J/TvLYjPV3VPrig/CuRehaxUzxDVgrX/D6No6TLRgZfMcPbzyzKlF1RyOs5N4lAHmDAyk7dpj/y1PP8ZVLbw+8R92J7eAL7fGzyOs9dzETrxIDfZKAzT+hZVa3P44tUbmpMATV6Vy7c6ym+KHfWJK9xMwLoIffpvLImzPo6WzoO1OoBjjZgsshH7L3sTIzu64E/s5PKu7p3Wu3qVcpzflAXLKUnGGpRj4vjwTpKExA8nkIuIZXeZ9kPFgGq/K1+ccsUaRhio4F4QZFWtvIwx0cD0Vuqi8HFwToYme1xillohL0bjFiBvoypLnQPUG8FB01qlGwrZbRbR2BEk5VeDORahlUdr9ZO7j14RWZr9DoLuNZUsjaXWJEvbh3ESKEQDdE76ITdQBQQ05rmVxBpnFG6ZsSriZSRp4GwphF/blZAKt0Hsh451O1meDkcs7jpzkXNXmO8MdVNouKYgIkYf/PT/Wx1ebaWL3XgkXgC5GqNDN4NLXh8fjF57lJGE0JRUFSkPpD1Ej/cbnUvEURrMcJdI3SF0igL83YD4Ozy3F/dPdmUl/uyYWGFUHrEJvOOdvGiPlHRnWetFfW9eQrp5ZAvlFV2ZR7EQNzJZ6qFTD/Qk1VsWGrG1zN3K4TeyXAdExdW2hfi45M5XTEaDfg00MyNEeXHLUbcHJugY5cllt0vhRGrJenh+1mn4SaxR97OLMDpYSUMSUAifZ5oLniu6y17fyHaxVRKfECWqUY5gWXu4+zXipjMNPLsejKOYTlNpf0JPM1n7Eawfdb5RuMnp0+zu4I2S7wwBFImU0paDgsNFcRyGgRA8bNO7VmCYXJ1jXNUR1ksIZeGVhL6rELaLuc5SN+ljCB4bhVQDxm4B+5hGKQ+gZACL49L6ySS20dRawiY2te3RsG4thn4Y05QwefqQupWCu3wVF6NgQmSVfcOa3+iG9g9e4OQDfZmrs8RHbEFgA84pml7ZSuKlagJbEVcms/OBIqSs70Q+3JvXCB0up0fTJiAHBDhXbe/kDF5Tx75SCg5Qhfkw1Hj7LEt0GWvrC7fgYjdyW5BJh24u2aLEbRYx+JJmVcCPO69HwkkmU+pMJFkT2KunvbBVMFdESewtqthFlNPfoRk46JAG5Cp/SO6+cBBkUITXthJE4Q08sPMlyp/qOuxv798NZKPs563JSKvMDfjnjbZQOFaMKDVx3r2k+tA1BsxrGjQNQ12Ee6ppvq1DbT2BjV5Zq52WLHk0WNDNCznEEEWIAEjcoTtGu+mlczQ1f3s/u6yMRrEbTmHGSFbYN+zCHHKoiTLTgi+Cp/uNDRnJHlI22VZd5KcJgNtCeoSd0ayjHoGbJcHxItyjCi32+0vf/n207f3BbHvd4X+7b7n+27D/2/XKL5uQ/TPc68uOTf7j2+n4emfP/f6879v/J8/fZuS6tz268bHSR3F96sV7/seP3e/3Wn6ui73189bX/vy282nrwsy//H9bs4p9rv875fdfo6j+X13I+77ZT7Zc/j2h8soP3371/tM77vqv11nen9GMPQt/i+Xmd4mf7/r9mX2L9C3f/zfKX+r+fs+AAA= -->
