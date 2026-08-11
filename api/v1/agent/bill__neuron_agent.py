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
    "version": "1.0.0",
    "display_name": "Neuron",
    "description": "Portable memory packs — drop the file in, get a compact Knowledge Base block injected at session start.",
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
