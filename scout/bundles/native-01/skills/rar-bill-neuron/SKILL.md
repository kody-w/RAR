---
name: "rar-bill-neuron"
description: "Returns a compact [Knowledge Base] block of embedded RAPPNeurons for system-prompt injection."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@bill/neuron_agent", "rar_sha256": "e0af759764d7c236755c42e600539fc64a7f17ddc3fac358077f6b23bd8bcb30", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Bill Whalen", "tags": ["memory", "neuron", "knowledge-base", "bootstrap", "platform", "copilot-studio", "dataverse", "d365", "power-platform"]}
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

<!-- rci-capsule:v1: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 -->
