---
name: "rar-discreetrappers-agent-transpiler"
description: "Converts RAPP agent definitions to M365 Copilot, Copilot Studio, or Azure AI Foundry formats."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/agent_transpiler_agent", "rar_sha256": "312593bc75ba9d3314aa20c8745986b1fe9d99569fbd35ea0a2723d2815e3ec5", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Bill Whalen", "tags": ["pipeline", "transpiler", "m365", "copilot-studio", "multi-platform"]}
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
