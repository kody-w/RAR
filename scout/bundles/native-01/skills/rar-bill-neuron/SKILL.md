---
name: "rar-bill-neuron"
description: "Returns a compact [Knowledge Base] block of embedded RAPPNeurons for system-prompt injection."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@bill/neuron_agent", "rar_sha256": "093ac6ab4dcd123fdf55998ddc8f1dc904be9bb4b27d7eb82e118099e353fcc1", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "neuron_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@bill/neuron:4bd7866172078d539b02d2d509439d2b4a102beca13c85ebc8908c3433d53994", "kind": "skill"}, "version": "1.0.1", "author": "Bill Whalen", "tags": ["memory", "neuron", "knowledge-base", "bootstrap", "platform", "copilot-studio", "dataverse", "d365", "power-platform"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@bill/neuron_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `neuron_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
