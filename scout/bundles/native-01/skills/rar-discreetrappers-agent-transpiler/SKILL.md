---
name: "rar-discreetrappers-agent-transpiler"
description: "Converts RAPP agent definitions to M365 Copilot, Copilot Studio, or Azure AI Foundry formats."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/agent_transpiler_agent", "rar_sha256": "5ae4e24760415ab5d1ad427c6a2f52518d4919d2811bee13914e65f3b159210c", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "agent_transpiler_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@discreetrappers/agent-transpiler:279aff6f03c6101ee29d94ff7f5d1a4a21abecc27668f2f5fc5ee2478ec09ecf", "kind": "skill"}, "version": "1.0.1", "author": "Bill Whalen", "tags": ["pipeline", "transpiler", "m365", "copilot-studio", "multi-platform"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@discreetRappers/agent_transpiler_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `agent_transpiler_agent.py` is
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

<!-- rci-capsule:v1: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 -->
