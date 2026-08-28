---
name: "rar-bill-neuron"
description: "Returns a compact [Knowledge Base] block of embedded RAPPNeurons for system-prompt injection."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@bill/neuron_agent", "rar_sha256": "093ac6ab4dcd123fdf55998ddc8f1dc904be9bb4b27d7eb82e118099e353fcc1", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Bill Whalen", "tags": ["memory", "neuron", "knowledge-base", "bootstrap", "platform", "copilot-studio", "dataverse", "d365", "power-platform"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `neuron_agent.py` and embedded as the fenced Python below (sha256 093ac6ab4dcd123f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `neuron_agent.py` first:

```bash
python3 neuron_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 neuron_agent.py   # or on stdin
python3 neuron_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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

<!-- rci-capsule:v1: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 -->
