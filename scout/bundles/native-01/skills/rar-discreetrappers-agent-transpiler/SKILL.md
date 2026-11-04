---
name: "rar-discreetrappers-agent-transpiler"
description: "Converts RAPP agent definitions to M365 Copilot, Copilot Studio, or Azure AI Foundry formats."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/agent_transpiler_agent", "rar_sha256": "312593bc75ba9d3314aa20c8745986b1fe9d99569fbd35ea0a2723d2815e3ec5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Bill Whalen", "tags": ["pipeline", "transpiler", "m365", "copilot-studio", "multi-platform"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@discreetRappers/agent_transpiler_agent`. The original RAPP
agent is preserved byte-for-byte in `agent_transpiler_agent.py` and in the RCI capsule.

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

Agent Transpiler - Multi-Platform Agent Factory

Converts RAPP agent definitions to multiple target platforms:
1. M365 Copilot Declarative Agents
2. Copilot Studio Agents
3. Azure AI Foundry Agents

This enables RAPP to be a universal agent builder that can deploy to any platform.

Usage:
    transpiler = AgentTranspilerAgent()
    result = transpiler.perform(
        action="transpile",
        agent_name="FabrikamCaseTriageOrchestrator",
        target_platform="copilot_studio"
    )

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "The transpilation action to perform",
      "enum": [
        "transpile",
        "analyze",
        "generate_openapi",
        "preview",
        "list_platforms",
        "batch_transpile"
      ],
      "type": "string"
    },
    "agent_json": {
      "description": "Optional: Direct agent JSON instead of loading by name",
      "type": "object"
    },
    "agent_name": {
      "description": "Name of the RAPP agent to transpile",
      "type": "string"
    },
    "function_app_url": {
      "description": "URL of the RAPP Function App for API connections",
      "type": "string"
    },
    "output_path": {
      "description": "Path to save generated files",
      "type": "string"
    },
    "save_files": {
      "default": false,
      "description": "Whether to save generated files to disk",
      "type": "boolean"
    },
    "target_platform": {
      "description": "Target platform for transpilation",
      "enum": [
        "m365_copilot",
        "copilot_studio",
        "azure_foundry",
        "all"
      ],
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_transpiler_agent.py` and embedded as the fenced Python below (sha256 312593bc75ba9d33…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_transpiler_agent.py` first:

```bash
python3 agent_transpiler_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_transpiler_agent.py   # or on stdin
python3 agent_transpiler_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@discreetRappers/agent_transpiler_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/agent_transpiler_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@discreetRappers/agent_transpiler_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Agent Transpiler - Multi-Platform Agent Factory

Converts RAPP agent definitions to multiple target platforms:
1. M365 Copilot Declarative Agents
2. Copilot Studio Agents
3. Azure AI Foundry Agents

This enables RAPP to be a universal agent builder that can deploy to any platform.

Usage:
    transpiler = AgentTranspilerAgent()
    result = transpiler.perform(
        action="transpile",
        agent_name="FabrikamCaseTriageOrchestrator",
        target_platform="copilot_studio"
    )
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/agent_transpiler_agent",
    "version": "1.0.1",
    "display_name": "AgentTranspiler",
    "description": "Converts RAPP agent definitions into M365 declarative, Copilot Studio, and Azure AI Foundry formats, with optional Foundry deployment.",
    "author": "Bill Whalen",
    "tags": ["pipeline", "transpiler", "m365", "copilot-studio", "multi-platform"],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": ["AI_PROJECT_CONNECTION_STRING"],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════


import json
import os
import re
import logging
from datetime import datetime
from typing import Optional, List, Dict, Any
from agents.basic_agent import BasicAgent

logger = logging.getLogger(__name__)

# =============================================================================
# PLATFORM CONFIGURATIONS
# =============================================================================

SUPPORTED_PLATFORMS = {
    "m365_copilot": {
        "name": "M365 Copilot Declarative Agent",
        "description": "Declarative agents for Microsoft 365 Copilot with API plugins",
        "output_files": ["declarativeAgent.json", "plugin.json", "openapi.yaml"],
        "best_for": ["Teams integration", "Outlook integration", "SharePoint integration"]
    },
    "copilot_studio": {
        "name": "Copilot Studio Agent",
        "description": "Low-code agents with Power Platform connectors",
        "output_files": ["agent.yaml", "topics/*.yaml", "connector.json"],
        "best_for": ["Power Platform", "Low-code", "Business users"]
    },
    "azure_foundry": {
        "name": "Azure AI Foundry Agent",
        "description": "Full Python agents with Azure AI Agent Service",
        "output_files": ["agent.py", "tools.py", "config.yaml"],
        "best_for": ["Complex logic", "Custom integrations", "Full control"]
    }
}

# M365 Copilot manifest version
M365_MANIFEST_VERSION = "v1.6"

# =============================================================================
# AGENT TRANSPILER
# =============================================================================

class AgentTranspilerAgent(BasicAgent):
    """
    Multi-Platform Agent Factory - Transpiles RAPP agents to various platforms.
    
    Capabilities:
    - transpile: Convert agent to target platform format
    - analyze: Recommend best platform for an agent
    - generate_openapi: Create OpenAPI spec for RAPP Function App
    - preview: Show what would be generated without saving
    - list_platforms: Show supported target platforms
    """
    
    def __init__(self):
        self.name = "AgentTranspiler"
        self.metadata = {
            "name": self.name,
            "description": "Converts RAPP agent definitions to M365 Copilot, Copilot Studio, or Azure AI Foundry formats.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": [
                            "transpile",
                            "analyze",
                            "generate_openapi",
                            "preview",
                            "list_platforms",
                            "batch_transpile"
                        ],
                        "description": "The transpilation action to perform"
                    },
                    "agent_name": {
                        "type": "string",
                        "description": "Name of the RAPP agent to transpile"
                    },
                    "target_platform": {
                        "type": "string",
                        "enum": ["m365_copilot", "copilot_studio", "azure_foundry", "all"],
                        "description": "Target platform for transpilation"
                    },
                    "agent_json": {
                        "type": "object",
                        "description": "Optional: Direct agent JSON instead of loading by name"
                    },
                    "function_app_url": {
                        "type": "string",
                        "description": "URL of the RAPP Function App for API connections"
                    },
                    "save_files": {
                        "type": "boolean",
                        "description": "Whether to save generated files to disk",
                        "default": False
                    },
                    "output_path": {
                        "type": "string",
                        "description": "Path to save generated files"
                    }
                },
                "required": ["action"]
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)
        
        # Paths
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.demos_path = os.path.join(self.base_path, "demos")
        self.agents_path = os.path.join(self.base_path, "agents")
        self.output_path = os.path.join(self.base_path, "transpiled")
    
    def perform(self, **kwargs) -> str:
        """Route to appropriate action handler."""
        action = kwargs.get("action", "list_platforms")
        
        actions = {
            "transpile": self._transpile,
            "analyze": self._analyze,
            "generate_openapi": self._generate_openapi,
            "preview": self._preview,
            "list_platforms": self._list_platforms,
            "batch_transpile": self._batch_transpile,
        }
        
        if action not in actions:
            return json.dumps({
                "status": "error",
                "error": f"Unknown action: {action}",
                "available_actions": list(actions.keys())
            })
        
        try:
            return actions[action](**kwargs)
        except Exception as e:
            logger.error(f"Error in AgentTranspiler.{action}: {e}")
            return json.dumps({
                "status": "error",
                "error": str(e)
            })
    
    # =========================================================================
    # ACTION HANDLERS
    # =========================================================================
    
    def _list_platforms(self, **kwargs) -> str:
        """List all supported target platforms."""
        return json.dumps({
            "status": "success",
            "platforms": SUPPORTED_PLATFORMS,
            "usage": "Use action='transpile' with target_platform to convert an agent"
        }, indent=2)
    
    def _analyze(self, **kwargs) -> str:
        """Analyze an agent and recommend the best target platform."""
        agent_name = kwargs.get("agent_name")
        agent_json = kwargs.get("agent_json")
        
        if not agent_name and not agent_json:
            return json.dumps({
                "status": "error",
                "error": "Provide either agent_name or agent_json"
            })
        
        # Load agent definition
        agent_def = agent_json or self._load_agent_definition(agent_name)
        if not agent_def:
            return json.dumps({
                "status": "error",
                "error": f"Could not load agent: {agent_name}"
            })
        
        # Analyze complexity
        analysis = self._analyze_agent_complexity(agent_def)
        
        return json.dumps({
            "status": "success",
            "agent_name": agent_def.get("agent", {}).get("name", agent_name),
            "analysis": analysis,
            "recommendations": self._generate_platform_recommendations(analysis)
        }, indent=2)
    
    def _preview(self, **kwargs) -> str:
        """Preview transpilation without saving files."""
        kwargs["save_files"] = False
        return self._transpile(**kwargs)
    
    def _transpile(self, **kwargs) -> str:
        """Transpile an agent to the target platform."""
        agent_name = kwargs.get("agent_name")
        agent_json = kwargs.get("agent_json")
        target_platform = kwargs.get("target_platform", "m365_copilot")
        save_files = kwargs.get("save_files", False)
        function_app_url = kwargs.get("function_app_url", "https://your-function-app.azurewebsites.net")
        
        if not agent_name and not agent_json:
            return json.dumps({
                "status": "error",
                "error": "Provide either agent_name or agent_json"
            })
        
        # Load agent definition
        agent_def = agent_json or self._load_agent_definition(agent_name)
        if not agent_def:
            return json.dumps({
                "status": "error",
                "error": f"Could not load agent: {agent_name}"
            })
        
        results = {}
        platforms_to_generate = (
            list(SUPPORTED_PLATFORMS.keys()) 
            if target_platform == "all" 
            else [target_platform]
        )
        
        for platform in platforms_to_generate:
            if platform == "m365_copilot":
                results[platform] = self._transpile_to_m365(agent_def, function_app_url)
            elif platform == "copilot_studio":
                results[platform] = self._transpile_to_copilot_studio(agent_def, function_app_url)
            elif platform == "azure_foundry":
                results[platform] = self._transpile_to_azure_foundry(agent_def, function_app_url)
        
        # Save files if requested
        if save_files:
            saved_paths = self._save_transpiled_files(agent_name or "agent", results)
            
            # Create a preview by truncating long string values
            def truncate_value(v):
                if isinstance(v, str) and len(v) > 500:
                    return v[:500] + "..."
                return str(v)[:500] + "..." if len(str(v)) > 500 else v
            
            preview = {}
            for platform, files in results.items():
                preview[platform] = {fk: truncate_value(fv) for fk, fv in files.items()}
            
            return json.dumps({
                "status": "success",
                "message": "Files generated and saved",
                "saved_paths": saved_paths,
                "preview": preview
            }, indent=2)
        
        return json.dumps({
            "status": "success",
            "transpiled": results
        }, indent=2)
    
    def _batch_transpile(self, **kwargs) -> str:
        """Transpile multiple agents at once."""
        agent_names = kwargs.get("agent_names", [])
        target_platform = kwargs.get("target_platform", "all")
        
        if not agent_names:
            # Get all agents from demos folder
            agent_names = self._list_available_agents()
        
        results = {}
        for name in agent_names:
            result = json.loads(self._transpile(
                agent_name=name,
                target_platform=target_platform,
                save_files=kwargs.get("save_files", False),
                function_app_url=kwargs.get("function_app_url")
            ))
            results[name] = result.get("status")
        
        return json.dumps({
            "status": "success",
            "processed": len(results),
            "results": results
        }, indent=2)
    
    def _generate_openapi(self, **kwargs) -> str:
        """Generate OpenAPI spec for the RAPP Function App."""
        function_app_url = kwargs.get("function_app_url", "https://your-function-app.azurewebsites.net")
        include_agents = kwargs.get("include_agents", None)
        
        # Get all agents or filter
        agents = []
        if include_agents:
            for name in include_agents:
                agent_def = self._load_agent_definition(name)
                if agent_def:
                    agents.append(agent_def)
        else:
            for name in self._list_available_agents():
                agent_def = self._load_agent_definition(name)
                if agent_def:
                    agents.append(agent_def)
        
        openapi_spec = self._build_openapi_spec(agents, function_app_url)
        
        return json.dumps({
            "status": "success",
            "openapi_spec": openapi_spec,
            "agents_included": len(agents)
        }, indent=2)
    
    # =========================================================================
    # PLATFORM-SPECIFIC TRANSPILERS
    # =========================================================================
    
    def _transpile_to_m365(self, agent_def: Dict, function_app_url: str) -> Dict:
        """Transpile to M365 Copilot Declarative Agent format."""
        agent_info = agent_def.get("agent", agent_def)
        agent_name = agent_info.get("name", agent_info.get("agent_name", "RAPPAgent"))
        description = agent_info.get("description", "RAPP Agent")
        
        # Build instructions from system_prompt or description
        instructions = agent_def.get("system_prompt", agent_def.get("systemPrompt", ""))
        if not instructions:
            instructions = f"You are {agent_name}. {description}"
        
        # Get actions/capabilities
        actions = agent_def.get("actions", [])
        metadata = agent_def.get("metadata", {})
        
        # Build conversation starters from demo_conversation
        conversation_starters = []
        demo_conv = agent_def.get("demo_conversation", agent_def.get("demoConversation", []))
        for msg in demo_conv:
            if msg.get("role") == "user":
                conversation_starters.append({
                    "title": msg.get("content", "")[:50],
                    "text": msg.get("content", "")
                })
        
        # Limit to 6 starters
        conversation_starters = conversation_starters[:6]
        
        # Build declarative agent manifest
        declarative_agent = {
            "$schema": f"https://developer.microsoft.com/json-schemas/copilot/declarative-agent/{M365_MANIFEST_VERSION}/schema.json",
            "version": M365_MANIFEST_VERSION,
            "name": agent_name,
            "description": description[:1000],
            "instructions": instructions[:8000],
            "conversation_starters": conversation_starters,
            "actions": [
                {
                    "id": f"{self._to_snake_case(agent_name)}_plugin",
                    "file": f"{self._to_snake_case(agent_name)}-plugin.json"
                }
            ]
        }
        
        # Build API plugin manifest
        plugin_manifest = self._build_plugin_manifest(agent_def, function_app_url)
        
        # Build OpenAPI spec for this specific agent
        openapi_spec = self._build_agent_openapi(agent_def, function_app_url)
        
        return {
            "declarativeAgent.json": declarative_agent,
            "plugin.json": plugin_manifest,
            "openapi.yaml": openapi_spec
        }
    
    def _transpile_to_copilot_studio(self, agent_def: Dict, function_app_url: str) -> Dict:
        """Transpile to Copilot Studio format."""
        agent_info = agent_def.get("agent", agent_def)
        agent_name = agent_info.get("name", agent_info.get("agent_name", "RAPPAgent"))
        description = agent_info.get("description", "RAPP Agent")
        
        # Build system topic with instructions
        instructions = agent_def.get("system_prompt", agent_def.get("systemPrompt", ""))
        
        # Build topics from actions
        topics = {}
        actions = agent_def.get("actions", [])
        
        for i, action in enumerate(actions):
            action_name = action.get("name", f"action_{i}")
            topic_name = self._to_title_case(action_name)
            
            # Get trigger phrases
            trigger_phrases = [action_name.replace("_", " ")]
            if action.get("description"):
                trigger_phrases.append(action["description"][:50])
            
            # Build topic YAML
            topics[f"topic_{action_name}.yaml"] = {
                "kind": "AdaptiveDialog",
                "name": topic_name,
                "triggerQueries": trigger_phrases,
                "actions": [
                    {
                        "kind": "InvokeFlowAction",
                        "flowId": f"/flows/rapp-{self._to_snake_case(agent_name)}",
                        "inputs": {
                            "action": action_name,
                            "parameters": action.get("parameters", [])
                        }
                    },
                    {
                        "kind": "SendMessage",
                        "message": f"I've completed the {topic_name} action. Is there anything else you'd like me to do?"
                    }
                ]
            }
        
        # Build main agent configuration
        agent_config = {
            "schemaVersion": "1.0",
            "kind": "Bot",
            "metadata": {
                "name": agent_name,
                "description": description,
                "icon": agent_info.get("icon", "fa-robot"),
                "category": agent_info.get("category", "productivity")
            },
            "language": {
                "primaryLanguage": "en-us"
            },
            "systemTopic": {
                "kind": "SystemTopic",
                "name": "System",
                "instructions": instructions[:4000] if instructions else description
            },
            "topics": list(topics.keys()),
            "connectors": [
                {
                    "id": f"rapp-{self._to_snake_case(agent_name)}-connector",
                    "type": "CustomConnector",
                    "apiDefinitionUrl": f"{function_app_url}/api/openapi"
                }
            ]
        }
        
        # Build Power Automate flow template
        flow_template = self._build_power_automate_flow(agent_def, function_app_url)
        
        result = {
            "agent.yaml": agent_config,
            "flow_template.json": flow_template
        }
        result.update(topics)
        
        return result
    
    def _transpile_to_azure_foundry(self, agent_def: Dict, function_app_url: str) -> Dict:
        """Transpile to Azure AI Foundry Agent format."""
        agent_info = agent_def.get("agent", agent_def)
        agent_name = agent_info.get("name", agent_info.get("agent_name", "RAPPAgent"))
        class_name = self._to_pascal_case(agent_name)
        snake_name = self._to_snake_case(agent_name)
        description = agent_info.get("description", "RAPP Agent")
        
        # Get actions
        actions = agent_def.get("actions", [])
        
        # Build tools.py with function definitions
        tools_code = self._generate_foundry_tools(agent_def)
        
        # Build agent.py
        agent_code = f'''"""
Azure AI Foundry Agent: {agent_name}
Auto-generated from RAPP agent definition

Description: {description}
"""

import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import (
    AgentThread,
    MessageRole,
    FunctionTool,
    ToolSet
)
from {snake_name}_tools import get_tools, execute_tool


class {class_name}Agent:
    """
    {description}
    
    This agent was transpiled from RAPP format for Azure AI Foundry.
    """
    
    def __init__(self, project_connection_string: str = None):
        self.project_connection_string = project_connection_string or os.environ.get("AI_PROJECT_CONNECTION_STRING")
        self.credential = DefaultAzureCredential()
        self.client = AIProjectClient.from_connection_string(
            credential=self.credential,
            conn_str=self.project_connection_string
        )
        self.agent = None
        self.thread = None
        
    def create_agent(self):
        """Create the AI agent with tools."""
        tools = get_tools()
        
        self.agent = self.client.agents.create_agent(
            model="gpt-4o",
            name="{agent_name}",
            instructions="""{description}

{agent_def.get("system_prompt", agent_def.get("systemPrompt", ""))}""",
            tools=tools
        )
        
        self.thread = self.client.agents.create_thread()
        return self.agent.id
    
    def chat(self, user_message: str) -> str:
        """Send a message and get a response."""
        if not self.agent or not self.thread:
            self.create_agent()
        
        # Create message
        self.client.agents.create_message(
            thread_id=self.thread.id,
            role=MessageRole.USER,
            content=user_message
        )
        
        # Run the agent
        run = self.client.agents.create_run(
            thread_id=self.thread.id,
            agent_id=self.agent.id
        )
        
        # Poll for completion and handle tool calls
        while run.status in ["queued", "in_progress", "requires_action"]:
            if run.status == "requires_action":
                tool_outputs = []
                for tool_call in run.required_action.submit_tool_outputs.tool_calls:
                    result = execute_tool(
                        tool_call.function.name,
                        tool_call.function.arguments
                    )
                    tool_outputs.append({{
                        "tool_call_id": tool_call.id,
                        "output": result
                    }})
                
                run = self.client.agents.submit_tool_outputs(
                    thread_id=self.thread.id,
                    run_id=run.id,
                    tool_outputs=tool_outputs
                )
            else:
                import time
                time.sleep(1)
                run = self.client.agents.get_run(
                    thread_id=self.thread.id,
                    run_id=run.id
                )
        
        # Get the response
        messages = self.client.agents.list_messages(thread_id=self.thread.id)
        return messages.data[0].content[0].text.value
    
    def cleanup(self):
        """Clean up resources."""
        if self.agent:
            self.client.agents.delete_agent(self.agent.id)
        if self.thread:
            self.client.agents.delete_thread(self.thread.id)


# Usage example
if __name__ == "__main__":
    agent = {class_name}Agent()
    agent.create_agent()
    
    response = agent.chat("What can you help me with?")
    print(response)
    
    agent.cleanup()
'''
        
        # Build config.yaml
        config = {
            "agent": {
                "name": agent_name,
                "description": description,
                "model": "gpt-4o",
                "version": "1.0.0"
            },
            "rapp_backend": {
                "url": function_app_url,
                "enabled": True
            },
            "tools": [a.get("name") for a in actions],
            "environment": {
                "AI_PROJECT_CONNECTION_STRING": "${AI_PROJECT_CONNECTION_STRING}",
                "RAPP_FUNCTION_APP_URL": function_app_url
            }
        }
        
        return {
            f"{snake_name}_agent.py": agent_code,
            f"{snake_name}_tools.py": tools_code,
            "config.yaml": config,
            "requirements.txt": "azure-ai-projects>=1.0.0\nazure-identity>=1.15.0\nrequests>=2.31.0"
        }
    
    # =========================================================================
    # HELPER METHODS
    # =========================================================================
    
    def _load_agent_definition(self, agent_name: str) -> Optional[Dict]:
        """Load agent definition from demos folder."""
        # Try different naming patterns
        patterns = [
            f"{agent_name}.json",
            f"{self._to_snake_case(agent_name)}.json",
            f"{self._to_snake_case(agent_name)}_agent.json",
        ]
        
        for pattern in patterns:
            path = os.path.join(self.demos_path, pattern)
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        
        return None
    
    def _list_available_agents(self) -> List[str]:
        """List all available agent definitions."""
        agents = []
        if os.path.exists(self.demos_path):
            for f in os.listdir(self.demos_path):
                if f.endswith('.json') and 'agent' in f.lower():
                    agents.append(f.replace('.json', ''))
        return agents
    
    def _analyze_agent_complexity(self, agent_def: Dict) -> Dict:
        """Analyze agent complexity for platform recommendations."""
        actions = agent_def.get("actions", [])
        has_swarm = "swarm_agents" in agent_def
        has_external_api = any("api" in str(a).lower() or "http" in str(a).lower() for a in actions)
        
        return {
            "action_count": len(actions),
            "has_swarm_orchestration": has_swarm,
            "has_external_api_calls": has_external_api,
            "complexity_score": len(actions) + (10 if has_swarm else 0) + (5 if has_external_api else 0),
            "has_system_prompt": bool(agent_def.get("system_prompt") or agent_def.get("systemPrompt")),
            "has_demo_conversation": bool(agent_def.get("demo_conversation") or agent_def.get("demoConversation"))
        }
    
    def _generate_platform_recommendations(self, analysis: Dict) -> List[Dict]:
        """Generate platform recommendations based on analysis."""
        recs = []
        
        complexity = analysis.get("complexity_score", 0)
        
        # M365 Copilot - good for moderate complexity with M365 integration
        recs.append({
            "platform": "m365_copilot",
            "score": 80 if complexity < 20 else 60,
            "reason": "Best for Teams/Outlook integration with moderate complexity",
            "pros": ["Native M365 integration", "Declarative approach", "Easy deployment"],
            "cons": ["Limited to API plugin actions", "8K instruction limit"]
        })
        
        # Copilot Studio - good for low-code scenarios
        recs.append({
            "platform": "copilot_studio",
            "score": 90 if complexity < 10 else 50,
            "reason": "Best for low-code scenarios and Power Platform integration",
            "pros": ["Visual designer", "Power Automate flows", "Easy for business users"],
            "cons": ["Less flexibility", "May need multiple flows for complex logic"]
        })
        
        # Azure Foundry - good for complex scenarios
        recs.append({
            "platform": "azure_foundry",
            "score": 90 if complexity >= 15 else 70,
            "reason": "Best for complex orchestration and custom logic",
            "pros": ["Full Python control", "Complex tool chains", "Swarm support"],
            "cons": ["Requires coding", "More setup"]
        })
        
        # Sort by score
        recs.sort(key=lambda x: x["score"], reverse=True)
        return recs
    
    def _build_plugin_manifest(self, agent_def: Dict, function_app_url: str) -> Dict:
        """Build API plugin manifest for M365 Copilot."""
        agent_info = agent_def.get("agent", agent_def)
        agent_name = agent_info.get("name", agent_info.get("agent_name", "RAPPAgent"))
        
        return {
            "$schema": "https://developer.microsoft.com/json-schemas/copilot/plugin/v2.2/schema.json",
            "schema_version": "v2.2",
            "name_for_human": agent_name,
            "description_for_human": agent_info.get("description", "")[:100],
            "description_for_model": agent_info.get("description", "")[:500],
            "api": {
                "type": "openapi",
                "url": f"{function_app_url}/api/openapi/{self._to_snake_case(agent_name)}"
            },
            "auth": {
                "type": "none"
            },
            "capabilities": {
                "conversation_starters": True
            }
        }
    
    def _build_agent_openapi(self, agent_def: Dict, function_app_url: str) -> str:
        """Build OpenAPI spec for a single agent."""
        agent_info = agent_def.get("agent", agent_def)
        agent_name = agent_info.get("name", agent_info.get("agent_name", "RAPPAgent"))
        snake_name = self._to_snake_case(agent_name)
        
        actions = agent_def.get("actions", [])
        metadata = agent_def.get("metadata", {})
        
        paths = {}
        
        # Main agent endpoint
        paths[f"/api/{snake_name}"] = {
            "post": {
                "operationId": f"{snake_name}_invoke",
                "summary": f"Invoke {agent_name}",
                "description": agent_info.get("description", ""),
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "action": {
                                        "type": "string",
                                        "description": "The action to perform",
                                        "enum": [a.get("name") for a in actions] if actions else ["default"]
                                    },
                                    "parameters": {
                                        "type": "object",
                                        "description": "Action-specific parameters"
                                    }
                                },
                                "required": ["action"]
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object"
                                }
                            }
                        }
                    }
                }
            }
        }
        
        spec = {
            "openapi": "3.0.3",
            "info": {
                "title": f"{agent_name} API",
                "description": agent_info.get("description", ""),
                "version": agent_info.get("version", "1.0.0")
            },
            "servers": [
                {"url": function_app_url}
            ],
            "paths": paths
        }
        
        # Return as YAML-like string (simplified)
        return json.dumps(spec, indent=2)
    
    def _build_openapi_spec(self, agents: List[Dict], function_app_url: str) -> Dict:
        """Build complete OpenAPI spec for all agents."""
        paths = {}
        
        for agent_def in agents:
            agent_info = agent_def.get("agent", agent_def)
            agent_name = agent_info.get("name", agent_info.get("agent_name", "Agent"))
            snake_name = self._to_snake_case(agent_name)
            
            paths[f"/api/{snake_name}"] = {
                "post": {
                    "operationId": f"{snake_name}_invoke",
                    "summary": f"Invoke {agent_name}",
                    "description": agent_info.get("description", ""),
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "action": {"type": "string"},
                                        "parameters": {"type": "object"}
                                    }
                                }
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "Success",
                            "content": {
                                "application/json": {"schema": {"type": "object"}}
                            }
                        }
                    }
                }
            }
        
        return {
            "openapi": "3.0.3",
            "info": {
                "title": "RAPP Agent API",
                "description": "Multi-agent platform API",
                "version": "1.0.0"
            },
            "servers": [{"url": function_app_url}],
            "paths": paths
        }
    
    def _build_power_automate_flow(self, agent_def: Dict, function_app_url: str) -> Dict:
        """Build Power Automate flow template for Copilot Studio."""
        agent_info = agent_def.get("agent", agent_def)
        agent_name = agent_info.get("name", agent_info.get("agent_name", "RAPPAgent"))
        
        return {
            "name": f"RAPP-{agent_name}-Flow",
            "description": f"Power Automate flow for {agent_name}",
            "trigger": {
                "type": "Request",
                "kind": "Http",
                "inputs": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "action": {"type": "string"},
                            "parameters": {"type": "object"}
                        }
                    }
                }
            },
            "actions": {
                "Call_RAPP_Function": {
                    "type": "Http",
                    "inputs": {
                        "method": "POST",
                        "uri": f"{function_app_url}/api/{self._to_snake_case(agent_name)}",
                        "headers": {
                            "Content-Type": "application/json"
                        },
                        "body": "@triggerBody()"
                    }
                },
                "Response": {
                    "type": "Response",
                    "inputs": {
                        "statusCode": 200,
                        "body": "@body('Call_RAPP_Function')"
                    },
                    "runAfter": {"Call_RAPP_Function": ["Succeeded"]}
                }
            }
        }
    
    def _generate_foundry_tools(self, agent_def: Dict) -> str:
        """Generate tools.py for Azure AI Foundry."""
        agent_info = agent_def.get("agent", agent_def)
        agent_name = agent_info.get("name", agent_info.get("agent_name", "RAPPAgent"))
        snake_name = self._to_snake_case(agent_name)
        actions = agent_def.get("actions", [])
        
        tools_code = f'''"""
Tools for {agent_name} Azure AI Foundry Agent
Auto-generated from RAPP agent definition
"""

import json
import requests
from typing import Dict, Any, List
from azure.ai.projects.models import FunctionTool


RAPP_FUNCTION_APP_URL = "https://your-function-app.azurewebsites.net"


def get_tools() -> List[FunctionTool]:
    """Get all tools for this agent."""
    tools = []
    
'''
        
        # Add tool definitions for each action
        for action in actions:
            action_name = action.get("name", "unknown")
            description = action.get("description", f"Execute {action_name}")
            params = action.get("parameters", [])
            
            # Build parameters schema
            param_props = {}
            for p in params:
                if isinstance(p, str):
                    param_props[p] = {"type": "string", "description": f"The {p} parameter"}
                elif isinstance(p, dict):
                    param_props[p.get("name", "param")] = {
                        "type": p.get("type", "string"),
                        "description": p.get("description", "")
                    }
            
            tools_code += f'''    tools.append(FunctionTool(
        name="{action_name}",
        description="{description}",
        parameters={{
            "type": "object",
            "properties": {json.dumps(param_props, indent=12)},
            "required": []
        }}
    ))
    
'''
        
        tools_code += '''    return tools


def execute_tool(tool_name: str, arguments: str) -> str:
    """Execute a tool by calling the RAPP Function App."""
    try:
        args = json.loads(arguments) if arguments else {}
        
        response = requests.post(
            f"{RAPP_FUNCTION_APP_URL}/api/''' + snake_name + '''",
            json={
                "action": tool_name,
                **args
            },
            timeout=60
        )
        
        if response.status_code == 200:
            return json.dumps(response.json())
        else:
            return json.dumps({"error": f"API returned {response.status_code}"})
            
    except Exception as e:
        return json.dumps({"error": str(e)})
'''
        
        return tools_code
    
    def _save_transpiled_files(self, agent_name: str, results: Dict) -> Dict:
        """Save transpiled files to disk."""
        saved = {}
        base_output = os.path.join(self.output_path, self._to_snake_case(agent_name))
        
        for platform, files in results.items():
            platform_path = os.path.join(base_output, platform)
            os.makedirs(platform_path, exist_ok=True)
            saved[platform] = []
            
            for filename, content in files.items():
                filepath = os.path.join(platform_path, filename)
                
                # Create subdirectories if needed
                os.makedirs(os.path.dirname(filepath), exist_ok=True) if os.path.dirname(filepath) != platform_path else None
                
                with open(filepath, 'w') as f:
                    if isinstance(content, (dict, list)):
                        json.dump(content, f, indent=2)
                    else:
                        f.write(str(content))
                
                saved[platform].append(filepath)
        
        return saved
    
    # String utilities
    def _to_snake_case(self, name: str) -> str:
        """Convert to snake_case."""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower().replace(' ', '_').replace('-', '_')
    
    def _to_pascal_case(self, name: str) -> str:
        """Convert to PascalCase."""
        return ''.join(word.capitalize() for word in re.split(r'[_\s-]', name))
    
    def _to_title_case(self, name: str) -> str:
        """Convert to Title Case."""
        return ' '.join(word.capitalize() for word in re.split(r'[_\s-]', name))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
