---
name: "rar-discreetrappers-agent-transpiler"
description: "Converts RAPP agent definitions to M365 Copilot, Copilot Studio, or Azure AI Foundry formats."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/agent_transpiler_agent", "rar_sha256": "5ae4e24760415ab5d1ad427c6a2f52518d4919d2811bee13914e65f3b159210c", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Bill Whalen", "tags": ["pipeline", "transpiler", "m365", "copilot-studio", "multi-platform"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_transpiler_agent.py` and embedded as the fenced Python below (sha256 5ae4e24760415ab5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_transpiler_agent.py` first:

```bash
python3 agent_transpiler_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_transpiler_agent.py   # or on stdin
python3 agent_transpiler_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/7W7Wa/kSJIe+lcOUg/Tragq7lsJI4h7RHAPBskgpwbV3Pd9Z9/+75fnnMzaR9CDlJlAMpzu5mbmZp99Bjj/+cWfp6wdvvz4hcmr6s3J/Cpuvnz3JYrHcMi7KW+b8x3bNks8TOPbg9b1Nz+Nm+ktipO8yd8njG9T+6YgOPbGtl1etdN33x7ezGmO8va7t3Z4o495iN/o25vQzk007G9JO9T+NP5w7hZvft1V8fjlx//4z+++5Ofzlx//+SWs/PEc+kK/7/cc/GY8hcbDx89zUeU36fm2208D3lXu4uFd5Dl0qvb29dffxrhKvnv77/+9XP0hHf/+9v3/fBun4cefmrevf3768v730c5T/G6H33VD2w25f/70w3fz3jK/ic59f/ic+evKr6///e1T9g9pPP3tpy+foz99+e6UXOXj9HNX+dO7KuNPX/7+m23/IGY85fzz18FPzaZvRv/05ce3d0t++PmXoe/+ONlv/Go/fjP168CfJp7+i4fTvp/bLm78Lv91xR/f/GlpN8RLHq+/rvg68KeJf7T82/zfj/9pWeBPYfbzX5j9hxe/Wfivv/Jpnnw7neaMwrz55uQff7/hEE/z0LwVY9v8EM11N/7tD0fwqdU4+dP8YcRPX+JhaIfzdP9q3td3P74lP32xmrJp128b//j2z8+Hf/0XS/3Fzys/qOKfv2r6LubdWX/7+vuHMt7Hv/39779f/K+/jKhp2P/a0K+y/uPz///82y9p8evseAvjbnrjP/57d6A/vsV/kFa1aXrmw4e5fztt5d8f3r38h0z94ZvRp/nxv34X/v8vvX/m99/iPznqy79OZGnOd/OnE06c+G//7U3Jw6Ed2+SEqvCEgLdhbqa8jn9qfmqeWT6+nf+mLD5VPfFvzM/z+TrvBIki/oywNnn7x/+K8hMv43h6nPhxzgQ+MPLXeB1+/hj4xw9vz1NaO+RpfibnB5z+1Hzi6bnTmUxjPCxx9BbsU/z9mSLfvz+8e/Yffy3wh27/x9sJT+9T3vV8sLe30O/GuYp/eLfByeLmq8ah35yHG4fvOFe14bl7csoZvzttG9tqOcHv3d6xfC8DUT6cxrUnSL/LPn3y47uwf/zjH4E/Zj81n5CLvH2WiBE4J/yiztv3359mJFWeZtNPTRxm7du//fNf//b2/73971Z9CH/fQz8h/6vHTw3vpqa+nQE61+e08zDO44v96MPj//zXV2eeYk7QejvPJ0/y+HNxlTdlHH3zrHmlv4cx/C2IT4+e3qy7dpjyJn3Lpx/ebsnbL/qem76/Gt/8t6wd30vcCYNR3IT7KdU/zfnFk++oMvpTPib7d2/zGH/s+o9g8D9UrH8Oz+n/eFNY/SwpbfVeV041Pyadi9smP93/y7l/jp9Chn8b35hvIn54U99j7q3zB7/LBv/rHon/eS5nvn1b/l603poTlJv3whm/u8p/D8xP93xAeh5+PdLv38/8LWzr+jzY8dve32A/enu2/rn58FMzfg1uf3g/irA9Vdnf0jmP/CaM/8fXkBqzdq6iD/+dmr5L+noK0ddT+YjBD1B4+xUV3r5/U+Zqyr/Xv5aBT9h4Ez5Ne1/yf8A36ncRp7lv0xkf8ZmQ32rKGarQD7+jI29cfFKJ08D8jPKPvcafGviHP5CUX94gP/yZq3x79xUVzuJ4QsFX9U5lgpMrvM1N/g4SZ9h+KhzMeRV9+MX/zL4znKp2/yAZzf6Lwh8+ssZzzVeU/TXHT0rwV9znb1+x7Uzc0wnnpF9X/PCN9vyRXvz778jEb/DzE1cav47PKYIfDHnp1+wZbs+TA6WxNoRZfIKmP/0Bdz/d/kspPxeHn+78efxw5zei9Pd3ppaH8RlRX35s5qr67sv7Zn+mde8M7jykOj7jb3ynf+887AyCPP749WnG+9Pvqel7jH+zzP8M2c/IPd38jRGeBLOZT2L4H7/64Bz7So/Opz/SnndVPnnNh/K/ZSznwB+oyJeTsU57927R6acTVt4LzadX3yvbnzXWPh786sc37iMnv4bLB9b9BuGq1o/eQSrY3z4c9ssubfBeeX7d5dOdf9xFPUffxXxUhV+z6PTKb33wJ8WTuflw389nHft5Hqo/C7Ye8u/kCl9XvNFd987p32j9rEHtmf5f6+xf7HKCRzefXvWn7M8b6Ofou56jv/wWmj6q1V8Je5/38+fbD1mJf2bFlx8TvxrjPzYyZz08FR/+K/Hv42clL3/dJjjhO/ab933+EPF/EYq/R6IPZ/wuNH8TiPWJTz9/zZhz+Pe58x6c7wj0c/IJP++/q+ovAu3Uaoj7+Qyj6F3o1xz5z78Ild9qfaaYH/mT/zXJvvKYc/rgD9+P78gOQD+A56bn788Kfb77P2Q4X1eNmX9W3HMZ5sdoDKMEDqIQ5gdYBPkRChMh7sMJBmMQGaEUREUwCUFBHEMIBaExjiVIAGEUDIHhKW9s5yGMf34vWvm7JiCMJxAZoCCFxEgcgkQIJwhGRRGFQySKkDEIgz4YxL8uLfMm+mrep5LvjvuFbH2gy6eV//wS4Og584qON/rzDwtcQMpH9GK+XxPKnFZEeHhwZ7fx4R8TJEbqIqCEADYkwHlN/9hfWSxXOSuPltEnal6cFbNPxjs16zN3MV+v4hEyvGS0OiZHOwxNhWWZPs2qjyYuwAhZdYk6Ql4vGmEvXW+d2qNSd5cl5YuHqVweZUAJmo+Yr45U25DaHIo+Wnfz0sJ1XAYaB0KKObbkU2uRXLpdTI1VMSNzby5XN3caeIpY/+wM1uaeC6E3DUA942V3eHYwLSy2lit50Cp5yTWy9fcjn5Lkieg5WFs7TSWXyzPtdklI86TU2CY3g95sjvY17mmh0viCQU+Q07vtaVW3PMvSDipRAYEpuZcxRvG9g5TCQlFcbbiE930cr6Q7QHYMgEBtGS6UZSQDxG6d8M7l2JiMIHTPnb1HrVzd1oKCtToeQipADq2T3JOW6keH9ijwkoM1HXNFEa6v5oq+LB9xfXk92EKAS7458BrdGrVlMCWz/Xt71MbrQWEuigM3UUdJqGBeY8zhMUYaCQHrAADtAJhcRqqmLhzRruQL0xEmw/SiBRSZHBIAEIFdzfkN5DdJIMuICuum4IkbZfRxsN9p2Oq0Rb/ID5A3ZOWG1uktY2jRgFMteOUkB1Y5j3QM6gdZyGVpRsQEEaN3TZeMDtB7wvRM1QKHQ9lTkYW1Vwlt95EWiJu/ZHAq9JvX0od6eRErL4Hq2Jcie+alKFlOOjqzy25sUPOhs3JMzdV3U2kdYEsPdIT42hZMrsuQxrkD0UPPlbu/qc6SHEoFlKyzPCqMvOUNKbBpg1N5fB5ZH3maFG/APb+qW0XOi+mAnqy1W+ZIZv0Kbp3OXtIWyM5zMFlHRLBMFozZ1ChpZfarFoCM3HZqVXPYRJAO+jwkG+RjK/KrMLi7tAZINnGnzYXyHwqT0tmQjC4aNbTZeBsFJMgD5R/bBdBpBugwEmDY8IXtUaJnsWo0XLeI/DZrN3K+ktxYFdQxKO0gur6Z48BoLXmJNk6+P1U2Anbv7gIlul/MuSKnkJyD+o52i6byoOPRt2dZhrI5Pq6XcAewfqyq+zPR017COxVZBQ7HRBDMGlJHM2s5rqx3eXS5F1rI5dZPBYheHThiH9cnx5ABVQzIwNTrxFi8XifPVktILpaShctxTcdw6g7S3bYnSXK0hCHesATwHW2Ok2dJAk0FhosBleUlrAryJvBoYdPjE21Z00VLQt1bvibhQ2u7pLJQXkmDXd/q2rxHWojfaC87UlQ3hO5F0qPHDWGn5K/HA1Nc73owvrrdJvd+3UtFOOplYNCnIxaZstxfqHObq+3CxTc4PLtC9/BtxAgVAUV0kKmve59d5OSOlhMQDCRUu+CklEYlm0u1bqC43C1w8wjS7E2M6lfNIbAruj5zVyqNLerIkuIlwmTH6H4VVIv15se2M2vFckR2xZWRAhfIGIXM0TahnmoUyp5UJgDLXu6u9PAebat0d0doNq5iaCa3Rla9DpEDu2yKrjK/xaXU8dGI8imDFsOhWcjSFsKU+lyV90pTO0muwkwtTtB4kwLOo4WeqqPyPvGuv4GOY+CkKWkOJ1wOIJV5nUdqvkBoEr5C4mVS+8zmWR3UkhQuy+xFknExXu+pKIvJEkwAsDXjXR9f0NzOR7oCZ5OcLMWIxw14ZdzUk8J4WO++PoeBlahOQMKEUaQp/Ex7fVCdtYmYuLbse4kZxM0DOFdHk0wZds3QfM7TApULu2nF6Jttla1pcDJcrvfEiiyO59fhhbN+HVqCERoXw+g2M1WzZwpaRnSxctoU00JjHLgW7hgDnvbOjgZ3ouqULtLPt8LbWiuU7yG7FlIVbSJ1xeTDed11ohGukUdaIbwFhndZO0MAn4S8cqm1DEd7FR+9JYKKdjNnR+LErBigQ5V8DjDU/raWLMTsXHtfHhf7qYgJfi0OfA76h+0cCmTuUHttZYvDHGMcai6dLESHLx1s9ZTd71BforIvYU//hegnx7iTaYoX4zb7VyfAcXy4O+q4J3aSyme7+6x5gXWpI6hM5/aitThyOYWgECe9R1W6Tiju2HzpC+tUOoNVadxxbaYi0ixirdHBU2W8WySufYa2gk+QdSkGZTvTLLu87GrA+vVOCcEWHv2QCi7wZIcby9/zVSOawAG8wbM7/4ph3daTYRJyZ7HE7txB2MJZLCfxqUJ6ECjXkVJ7yYfhnmqdBgomkn6FoHpyooOXyhG5A9ZmkSnY2z7ai5YeJbDt4HQWXDGzZ/ua1JOmZRxa7JBneLsdOg+wrIOHQxXzYKQ6KZZKykOn1cJqwaWUrVhrRiQUlXgwixDk2JLNmuIG+f3EpFJemGM1gAk0gPrWiiLwAA5AlXSD2mKHK5wmrwpHJvboEU2jEj561k11oxhV7DGEfqsyRQXzlxjn71r6MiJfG2p303IKkxWy532KKgIrsjNbv9AjyE9zSr3gMjz4R4CnHo9nfGHgSysZXM9cDsF1TK937TDbqmqnDeh+4ydaP/Y7JEqtPEHHRYCy5kLQpgbetAKK8+BkMGBZGwgkE2xE3LuJyq6IpZoH3ijQlIH0a/LFVrjeH2kmsfzKC9KrMg0Ft+f6KRMXcjFiuE5eN5QbWVuw+8Sn46YU5ere7BVeZB0j9iN4W4/xjqaLh/aW43RN0YpofIe6fL7fussjXAmv017H2bi6e/PM6M7bG0quPc0v2LVpesgULFsUhhCApT63xKwME2GsgpsopXMw4CA+VW4hQc1yQQm7u2K8dZSCL/d6x0hPzoVrq2tffriOMYCXDrsfQ6k3R3JbZYIbriX0RJG8rLRjXE+GtVjAFnhHuF98Ok34xIfiiWRR3n+tqgluIJfTqTsMORhcqh7fB/mJwvbZs2BaI2kmymCYDCxx27NVLOBxuL3ioMx1KJsrTOzpWhY3j1LH5wxxC7ugmeEDSbFjV7bWGh8nwLapBSjqy6e8IRrrUYtDAtn1ST81vclQRQ8iMGqwHTDNocFUIbqKgM9ntcJqtcw9pih9YmP9uM/KwOS673l21A5+3fiu1yMm42GoMoNtCW/HJKkOmaJIWFW9isjBGDxsllY5zb1DVzRb6Z4Sh32f5aUKRWKNSOkm6cVIm51T0ZiFejO8lmK9x4MDjFFFzcm1c3zrQYaE+VSSWUtKTymkSY637mIMw2JuCwkST4zFfYu/FV1G9S+rModHEj+aAGJe5TVuDqESxYyVor2TFNnJriwNt9e+Y1vERAgQUQsu7C+qHgIe5/bBVZofbbobV3tCDJco8+KK0GmA+aOpJmmXQ/SkiCZu8JHX4otIiEWO+0sCq9rQFQ+WyV+NGyGFDOXbUrqr7sU53auso0mNbd2m3aYls5yupTkeI9/B95CJRRLNonsKN5pmCYR9kj9PKGey48SAudlEfyHSoea3o9mf9UbJs6wLETW0I+jLiVlLL50m1ftTx7mLuqnTiPRUDtcyBsFSNHHMQ5IftD8sYwjCVgXvWWqfTJyTToT30GW8XGcibzuw5UflRrP6oPuIqg+y0mVwrfnAQTYAnNSYujU5jGR7BktgN7O6cB1ZtAOfvhVMK69N1jnoZg+xY56OZRRBoYAsJKXJ695VJjQJN3RrFUGiDWdCqIZqIzBot6WGX6uAG3e5wlvCHNxuab3p5j3MXrcGlogaLnrO2Qv2gSi71Fc2BnN9APR8uz5letJmfWoIHTQKsTYD8Gyy3FYjzDwgZnPxuhN7kieWPzr7cXXUxkQVaYgsUGw3g1cs+vkkA04A5FS5G01aF/hhK64YZgEvcwejE5lQMrtA4hkJehTG7blKIy51waIB7TpRNK3WK7FCiYy2JY0YXacDLhU1zBBMf8XIxHTiZo7YBdtZ3pl3IeFJBElwyrBWFBleITnmZ5OjAXvg39blrDw4xGekqBzCaxAoLXC2h+zqbVrDFY2W7I0W5yekBGgI031Mc/BWxOliEBsNQsiNR682VRFJCdaEXRILsV7nrX1uNb0f6sxlQ8HdI+ppmo+HsyfXW+zxA1EtWUU2U5C/tpqxx8NJiQqRXw+XBQP45frtS1qEBhVdCzUdhofqmnH6tc+bxsYow1C53X6J1OtkntnZeJKdiqq3x47UeRvWPsucoMRDeTdxoHEGbi1qa1zDQoyjcpYH+UXGX3n3Cko37gVs5dHLjFfJzXrpyTC0yizs0BBHfeZJU3G47U45+FSnnhoPyr3VF+rZzpIbF0YXcA1oJxe2w0rDgZ+MSh6R+worsivYNngCHj6DduuQRDAo8tKZnUt6whnMhu8D8jK1Z6+xiGStZJX7tIukfYh6fhJjs41O5QX3IashDEHSkr9sYMhVaHTt0Yxf107F4m0yI1Xc1J3F+VAmavgGv8AEibkiD0czJSVqWWa10bJGYwbIwJizNcxeUesJj/WJ31e08HEn0xs4w3eIU86myoueEl3yVFlc1wlblAdJARjLIclNP0Bc58qL9jRICCN9S79JLSGTBGOW7eM5DzBH4xieHiQXAK+eqZ0NGmwRmtHuaMAiz+P72DuWzKNaXTwVYbcVZhf3RIK8SWGfbT1WxDL53V0O92pdVSviUoNHk2bwbtES3qz1NBjkpfjyvF7v9kDbzmqk/SOQr3JdMlVU7HYPsbWr8FwvUsqlIfu54SC+dY6O9DFqOQ8SArrVuvN755qvbXd1xyeh1m1HjqsjZNDrWRsJlnDLxASp8hUh1tnETuRykyeQeB2rBURjjz4fIfq8tXHpW7AYF4ntvCjPp3vxeVdsH4MHQ0K0anIxlR7pUJ/FaGhuw8TwvpTa1npYN4YzMQWjXoPCt9eYMFAuu6q0lRLWfA1qK8Q0QrAOnDk0e48MAcbI4dKHxFw0i+zlkHG9Bi6sCJl4eMil8GqkoLgiea04MPttU6BlxPe3EJEdzy5t/uAJoYzVlzQwcz+ZGxvARYiYKfUI92U0ztZtiqqzTX5lhMNqcTBDbXDLh2WNq9dCEZVq2XQe1bKSHroTJEskgLOA5AVByHDENSFCzQdGEU/HyC1oI5eMInGpSBsWbnGEOgM3sJ/Rw5nb2GvXOmgM59DLnJVXaPQLRVPwKuijkC6iYcUPUJ+36MaCPK0DcQlecCFSkxowhbM7PemGqgxJj2W6CWvHUmOTEz8nDXEPK/Tjti5BqL+J6pzry9XBGqqfZVC6JjJzhx42pfr7jNyGwjgqzthOT09nulKzO/chFD8dvILtKand6bgN8aVOrHlIxYdQkKIesaDXGDs8edWJeCbnzz76cGTSQNaLCXYOVkr09Hgdw/0kmDSBPE6k4GaP8pySoOyS7OOCrqM897mMLGAAvkUVZNkcbOLpzDL3hBPRlbGERAHdXpx3qJRsC+YWIHVy8dImTp0CnjFjF9GNBpDGUAFdzCnQI/naPTTLpahpOmNxpw+2s69EnpeXwtSfXgeQl5ij5n24jOPYFYiiXAdjGyyrfIEO4NLLRRj8XmaYjc/xR0vA6slO87DznXKAQ8kKPSW+AzJcSCgyjoKckVdm5oMBSdWku/ATWU3AA22mNWF1wLsU3VO6vtgscWdgxGAnxNniJSGs41oyOpNwhMSFOJheHT2tOx0HvfNsloB5yZfgFSlBo03BTR9DU88pTYC6la8wmtOhZxPMnUSa5DGHq4Gvd0mDrkyI7QkT5AuqSRTNotl02QZbyjvwXlsxInDeLMttenGgQAVWnAJayYZgHszveqxvQ+m62nN9XU7z+xBAsAIMRLaaH1WWkSWVM/LFgcGtek6g2ASTP1wdp1D8iDWPfYdIDupmPn36xCMkvYdNjoUbRa8GGJSYwxj/lV8d0xh16Ajo564Ea6dJ6WU2CK/lfX+IYCsrSJ9b24EbRWFPT7RUNVfs8bPaQIVOgsZmo4148sIldPWThkh+NLI3uHa60IV5BQk6ioST7kZdo3gs0IuEIKQIouiNg6wgepauiCTMSiqqullXL/FHBbxT7n4W2bTeoCgAZezlVRdFOIhrh9o6xdAvhL9tjsXQj1qkAc7MSSJhltsEBDWz8nxr0IaripO6IXmlAczZmzniKkU4VDyD5KERha9UK8bninZWy6Z7pAYGOZdbrNU14SadA8jKvFJI2JoJsOP8llSvSq2q+oZwsWOrVYTfA6XxpmiVSceC9XvvUWFNZNA9wdyyuqje3WpvcYNj0+mudpXvQCEey8sSMtpcnrFilCIWeLLZss1NTIj5GE/KgpnhAaKXd7OzNnRZlERkEW5CPABnhQMRTh0vjF2715OJIoGK6rcNKO9GwHvFfTvI6116UYd2AwxakuxiYVo2NHtZ78/aJu3lY6+rK6hix2sFDEdJcNxHHZTXBaappvu6NrUCaoDGZxV3Ny6OvHIUQCMXrY+wjgyDOM+7iAQb8+kzehqMDw8wDuQRYneDimoDL27RPvkrRrYwz+6uBln70V3HEEiizG69DSd07mKYei87NexcHpAk6IwqsUrmIugdK4sbzwjB9fD3BTFgsJIEAOCS3vU4XCXwu+UvuaoF/ugr8VY3UbtZoPEKRum2H4rk5GbdkrdBD4yzEHfwNnmEN7HsyKepwB9+dlw6x3J7hT0upt1AYgdYmYJ5Jc4gXNd4l5x2HuElJdIH7bWGpxhsweQImFtyd7EfZujO9nYpxq2DH499CJDn1WCYoDih2+tKPekg18zu+uZkqKBHw0FFIihWx/Ay4qbeeSfVjaW2G5oxFVim1Od4ra+qXWRM8rCk9qo2tHYtEUV99nEWVG6DpL3g5qrXV0/4ih6zyFe3x7Wq9TF5FCLfq+BIv7SawloUUh+1oIMzxizxi1xk29zpsPUjq2yMRstFf4f8meGr52vIrkae71YxcBfu1rAWOT+m7qkeQHTFQLuqvfiawmBzdVVJTUpZyb18ESclbx7Riq4ARymmYtTtejIyhj09rZdAHYavKfNr7tEXXKDrvV+ePThn7QWij57fDcbDI4ncZ22Skgkf5GWKJoTjAc9VN1uaC7X+g6mIK1ERgsFlYVxHqXPNHzQuJIx74kXpcAk3VvL57J81Grk96Rs73kkbQuebsqf3w47tsegBT74CoGLvE+XnLclhVtsc9QV6FWmXxZUyOqoX2quDcOHolsfmB+OA3+6jCis4TNxs1W3xkh/7+wFDkVNFhHN9FUM16kVe7Tdiiejp6q/4/SZcbYFiveul1JrY8Hu9zpV9qPwNutt21bMVgsId8vSQ+AI9VkSC0j6JaQ9Ub4cOL1b6wk7GrCuma69biMR+HAH32wTjr8ota/zIWqJZwhmQBHR1E1ziUvIkKCz8yNbKz3tbLkN+6YQsxzAlv9rzljF50CZ5Y8Ktd1vvasZ0UnmRiMUY+Li8tnTe8MsN9A9NvioVyLFr//BeYQ4pAiZXsmhw10ThuMy4MhpmRhmx1fyuvagozPLaFINnwIU70ClVwl3usroNmMQeWkbmtldDtAdIxHO8ny6P7cSB0hN5xDscZ4hrHR7OKfWYD8M1jzT/4EEn2aJAEVQadLjG5vmJ2VgnQ+oFTkwpG5+plh2JVXtZZOyMB/l7YUmzy82OzcDZSzIExKFrxgXfRWfecGSumWfVdHBU5j5EHBPkoA1UWKRLgaTUu73elxe9ONUKaCUno6nekESsPdhdeQrGCIzspbu3MSLZxFVrRUvGn0/bMic287r6/LvZ/URnodd2mT+wm4wnykrO1ymFWUlj1JNQqLBkUY6uLGD6ZAgiTlBkOXPFE65HlRDwAl44/G5DY3JkeIR04GNCk1dyrGQMnxXBXrX6NaiVE9ZXqbhBWv7ybzYVDgo189Lcg+K8FSyaTq5njnvue2dfeBd8ep14clwPuO7ruClZ6PEKkuEBPNtoqY0JuI+xYyHGBL2wPvfCyr3QD3+WVi83B84b7Hvz6vPLQJ0FLpU2QUc1sby+tolUEEM0pQ4RXwY13SOg57eBE+mzAWpMKeEGIsKdsxw5VeFIvMTHLYxdBeOR3YYUXKv4dvbwfBbULFHzaTHtHcQ/KmfssnmCZ2dwH62T54dF9T3DITmbDc4KYUqL2Aw3cTJkGI8q14qZ6zXl+sD3OVTxKVRYfhUgCsuiwYLSFXpg2ZqtijgSy0k+t33GFBKzRoRGC/AIvV05cRNEO89dD4YZJQIWbpfI9WH9Iis7S3BYSb7S+LILXEQOq2owWUWHtpB5gkaHnVDzBHlSzAzZR2b0l6yA72EWdDmMT0N9gVGRmCY2CiXSu6+WgeckadzYg+l493XXTpaFE3XPXjRxGdCLhvm2SgO2ZJaN1KbiHnZT0glLLkfAEy5hRs6I24YWCITLAen2J6V+icp+XDcuTct4RuF6FXAPCoWJi3cM7hu8JZag77xjsqPtFYUONLRz3J94g06ubUpHTvitKFyGvRxtB4qRgi5qFlsNr7rmhgSNjqPJO1ziS9U3LSHtocgiuHTTlZNZGo+CUWh1L3fjSYyjLmbNME3ujd/3Me18CYnzFgavCYjJnrNUTWCHr+coJ0on286CImTZ8d3rctgQzxoIeiECiNFhedSIWXXVaDtZSZI6alukjNqMxYVGYnBaY/VeLEWQesrB5JoHFBdJOcAYKslsG7GMBFlmOgEt4qnOmi74CyEYCtSeF899jUuPGxg36tvZJtbRvo7GWAhjQt3aPfAj7Zhe4/WElkqLlhe4xTgVHAIO1eAOOkUIiXf1oSAVUMi3vNGUWQ36+yU+G5k5Vp486E8NNp3U1dCQyvXalvMYgTs4vUuCNFdcy7OD68jJWK3d/ZdY7/7jircSfdGmZ225DEpltrdjmHtcVPhGyEBtAfki+96ZWpKR1KuzAWvPICJkkDCJP6LHro8RybQ3+pQMw1G2Ccld89T+tkQp4JoR6yoY+jpb0p105bCioZxEnmOKibm/2Ogj25UHxnQXfEIMqG5jGQerm54CdwycmT2fFPUmsRlKGMfEDvEoKsHrpV0Nbov0+AV3tJKceXdPvcs2o4t4mKDSD11oCeqV087EB0gbhDIT2J4tUy/jLWhYIWE1EGYdQ2yDrEYxKTNwRONuDkJAT7oSsRZcCYemhlYqzKQKgl5tE1ei61qFLww4EYtnBMNDbxOkedqI4rrU2WAreiI/OX+cL9LU6/1hyzbCPIR58YHxNueBKZlGutVEeV+6ZpFuCeYNMHUifOXV9bXbteZCyRxMGgt49nBkP8bPBoqKuqsgz3hQOT+B+y7W4zYWjJiw4S4L7NGB7miOohdJmdveyIPC7Kazcg5CE26TLw+fMsp2TRjyBOFBGxY34ndoVvy+ueaVK6JF1KCud1Xa48odMyHG+w3kBnxrlKZVJ3BoT/yucTzrDSD1hSTG1UZ01hQ+OJGIehsHw9Yhted0y2bNVNr0fhH7pK9nn8h6KMrxl0fCL/MFJlc1yiA+lp8PY/Q9P6NO8bqi9GK2SeCTiKZInzuYvSI0/Dqrkl9fltgTApYjGtaO681eozPbBE5+ZTcUKO7RsvNbHEUeJnIjufoxpDP8SdVuygEzxZWSHQBDgMl25akDa7XMfVPtsqsuZ4/40WS2OExRjWCdSeotNnP5IfnIJOLpPfdLOB0a6bHTj0HnghQcqvvmZ1uDlnTqAqJPbwFzXzZqhkr+Ap+1f3j2t16qlPqG5Vr3vNjW837WOL8IrOEO6/DtJaUcfEX6dg+3EvcxHVcja1rmAVy5Do7xp3k5dikAX2eOPnMH4GUY9IlAddcGZyq9kp/JHRUQeygCiYKA9FY+qpHyr5MKqXcxMO1jcW3NE7uMyjjnwK2b7lPjIDnr0+wU6XBqw3t5kUrlDiqNd6tXsbw7SJcyFe4M3js+23X+OH0Isi2V5OSEkJdBGfqgjxZsqEfP6HdmbDfVOptzbVWvjZKtyCOwzgZhjzUA2oOwYFlElqSUAvlnQKsME7uU1PXxTOe+2BiPQIKYQH2c5V+e76HNpsXRUHSxRs3tWhV8W8Jjncvw4SAlV+vVoelVDuuekEN4sIYK4t94Qw4FWxvHZrB2hHg9BTjAY+0ynUl6d9fbs7jEr+OhPjFBfFoBdoetoY6EFRyDOl0iqd3X4HUrMpt82Ngm1Nzl4vcIEBOkyRqNs8LIIk1e14CDuYaGrNctaAym/8iAMLxnGs/eO77Gr3lxwbQqfsDxtESEd8Z/yIMYeNyeofh6CWJW3xHYr05SOOrc1u7E0EROD0LOEEtA44goQMaazqCBLFL8Mi4GRY9O7PRy5/UlKyx8r00bLucK5gCdO4LcXF/v7R1ity49kthIX4vjPX0hCuUyVlWii+7bhbhk3szD9dl7c4zUCejeL/IAY9Jm83Kh3bG1D2ajjeyL0aTILgCQF92UhMm0s3FXoUi0Ur+oo5wsYTkjz8Z52MJI1FlVAtIKtf1Hjg64papGIStnceENYL6VBqCko89Hosv45bpg1qbYk5u+BKdTW/mSjfOIlTeTaGH1FVUgEPbmiwDyaGrO9OtCZVElzDDrPgVyMBy4sIK11ReDUZuwQ8CUUp8h/OZi3WV/QogWJPX+uMf93hGob/QA9IpOF2aqyiJCUCRLfVLh4ehly7k0eiddAKV76MxwHSj1ZLAm6dXxdXB60RxLV6eq1/Vp9EsXP3qvsqeoe0BRQtnBBdReDt8o2LDwVvwsGXt+1WJunqQnEG2U5I7GBYNWNhbVZvn4JtvlJB3caNBoBR3BLY7u0D46yG1TZqC8sGd9duU9XIOtfcgv311jhmzLhHmiaGHc+oHHJZ4h1VoAiWxUOlrO2HwrcLOLsdd+NQe94Z8tGmvLi+DRF40vMkqWY+hHKkw76qvcb0kS6GfYvbRhpE3f0NB7XvBUmkGrBSFHX/cXHgcmovT9eUahkiUSmlDJYOV3vb3aKOAg08BMXBJi02FJMvWIbfCJ+cVTrZfEyosIQlDMxRZrsil1fHCjXdwofJ0JjK4OGgy8wRecsZjD57050ZpolIjTJObcciku9wlaVhRCgxh4WR0xDhNdDAFF2ZEUvswcSDVMbTMTrVdUHi9Y2vPU7h8lIk2rSyGVxxp5nz7TVRwC1qOl+76cTfOrvjUQwo1L2xlBeBurxFNlOT+ruaKMmwDcJLzWIEoqbBBQMm2lNRjCXhRO1ShYarbUvu4Leh6So4TgmF2tY6aVpZPXeX42ySLGLPW8bJxLYPqcSU0tMoXdU4Jw16jSJPpRe9mRJXq9LhFocjgD0ICSRaJz91DWeIfrI79hgj1WoD3ITpUJehQczf1SCkN1EY2nbonhaJ+ZcajMPSYmXBLRB7N6JlQ8vZ3DnwFWnKYsT+q1RDuqMwm0RVmrJcNA9ITBnb14telAsUEGtuzxWRLFLi8ChAlwlKdltZ96Mm+VzlXQ++aNokbVbopM+f0SrmEIzdoFe9h68LzKSQ+MpP4irrD5XNYt11ay4UPAepyFxCGxHNCOe7iJKgVj3JVQmCo0ry4++yeqTpejYyK3nJ5g9bwgPbDeLHyQoua+0jT97//+5bsv73e6v35s8F9+PvV+S/j/2mXlz3vF7XLu2oTx+5XsIfajHz/2+vG/VuE/v/syhPmpwOe167Ga06/Xlb9duh4+L11/Xl/+fvrtRxPj/vnFUdtM8TZ9+8Zi8tP3r2m/dHkXV3nzcdf/t6ve75//eu/8+1/unX98VvP9L7fFT80+Pnz7uB5+avcD9OVf/z9EKYw6NDwAAA== -->
