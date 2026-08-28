---
name: "rar-discreetrappers-agent-generator"
description: "Generates complete agent configurations from natural language descriptions with optional Copilot Studio deployment."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/agent_generator_agent", "rar_sha256": "11b58f135dce6bd67bf595c7d5a31576e695a768bf6dba4d46709427e209e61c", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Bill Whalen", "tags": ["pipeline", "generator", "scaffolding", "auto-generate"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@discreetRappers/agent_generator_agent`. The original RAPP
agent is preserved byte-for-byte in `agent_generator_agent.py` and in the RCI capsule.

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

Agent Generator - A Meta-Agent that Creates Other Agents

This is the most powerful agent in RAPP - it can generate new agents
from natural language descriptions, complete with:
- JSON configuration files
- Python implementation code
- Actions and parameters
- Demo conversations
- System prompts

Usage:
    generator = AgentGeneratorAgent()
    result = generator.perform(
        action="generate_agent",
        agent_description="An agent that tracks project milestones",
        agent_name="Project Tracker",
        category="productivity"
    )

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "The agent generation action to perform",
      "enum": [
        "generate_agent",
        "list_templates",
        "enhance_agent",
        "generate_code",
        "validate_agent",
        "preview_agent",
        "list_deployment_channels",
        "generate_copilot_studio"
      ],
      "type": "string"
    },
    "agent_description": {
      "description": "Natural language description of the agent to create",
      "type": "string"
    },
    "agent_name": {
      "description": "Name for the new agent",
      "type": "string"
    },
    "capabilities": {
      "description": "List of specific capabilities",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "category": {
      "description": "Category for the agent",
      "type": "string"
    },
    "copilot_studio_options": {
      "description": "Options for Copilot Studio deployment",
      "properties": {
        "channels": {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "deploy_immediately": {
          "default": false,
          "type": "boolean"
        },
        "enable_knowledge": {
          "default": true,
          "type": "boolean"
        },
        "enable_web_browsing": {
          "default": true,
          "type": "boolean"
        }
      },
      "type": "object"
    },
    "deployment_channel": {
      "default": "rapp",
      "description": "Deployment channel: 'rapp' (default), 'copilot_studio', or 'both'",
      "enum": [
        "rapp",
        "copilot_studio",
        "both"
      ],
      "type": "string"
    },
    "generate_python": {
      "default": false,
      "description": "Whether to also generate Python code",
      "type": "boolean"
    },
    "integrations": {
      "description": "External systems to integrate with",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "save_files": {
      "default": true,
      "description": "Whether to save generated files to disk",
      "type": "boolean"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_generator_agent.py` and embedded as the fenced Python below (sha256 11b58f135dce6bd6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_generator_agent.py` first:

```bash
python3 agent_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_generator_agent.py   # or on stdin
python3 agent_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
Agent Generator - A Meta-Agent that Creates Other Agents

This is the most powerful agent in RAPP - it can generate new agents
from natural language descriptions, complete with:
- JSON configuration files
- Python implementation code
- Actions and parameters
- Demo conversations
- System prompts

Usage:
    generator = AgentGeneratorAgent()
    result = generator.perform(
        action="generate_agent",
        agent_description="An agent that tracks project milestones",
        agent_name="Project Tracker",
        category="productivity"
    )
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/agent_generator_agent",
    "version": "1.0.1",
    "display_name": "AgentGenerator",
    "description": "Generates new RAPP agent JSON configs, Python code, and Copilot Studio assets from natural-language descriptions.",
    "author": "Bill Whalen",
    "tags": ["pipeline", "generator", "scaffolding", "auto-generate"],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": [],
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

# Font Awesome icons by category
CATEGORY_ICONS = {
    "productivity": "fa-tasks",
    "sales": "fa-chart-line",
    "support": "fa-headset",
    "data": "fa-database",
    "automation": "fa-robot",
    "integration": "fa-plug",
    "finops": "fa-dollar-sign",
    "devops": "fa-code-branch",
    "hr": "fa-users",
    "legal": "fa-gavel",
    "marketing": "fa-bullhorn",
    "customer-success": "fa-heart",
    "meta": "fa-wand-magic-sparkles",
    "ai": "fa-brain",
    "security": "fa-shield-alt",
    "analytics": "fa-chart-bar",
    "communication": "fa-comments",
    "scheduling": "fa-calendar-alt",
    "document": "fa-file-alt",
    "knowledge": "fa-book",
    "search": "fa-search",
    "monitoring": "fa-eye",
    "notification": "fa-bell",
    "workflow": "fa-project-diagram",
}

# Common action patterns by category
ACTION_PATTERNS = {
    "crud": ["create", "read", "update", "delete", "list", "search"],
    "integration": ["connect", "fetch", "sync", "push", "authenticate", "disconnect"],
    "analysis": ["analyze", "summarize", "compare", "trend", "forecast", "report"],
    "workflow": ["start", "next_step", "approve", "reject", "complete", "rollback"],
    "monitoring": ["check_status", "get_metrics", "set_alert", "get_history", "health_check"],
    "communication": ["send", "receive", "draft", "schedule", "archive", "search"],
}


# Deployment channels
DEPLOYMENT_CHANNELS = {
    "rapp": {
        "name": "RAPP Function App",
        "description": "Default RAPP deployment via Azure Functions",
        "generates": ["json_config", "python_code"]
    },
    "copilot_studio": {
        "name": "Microsoft Copilot Studio",
        "description": "Native Copilot Studio agent with generative AI",
        "generates": ["mcs_solution", "yaml_topics", "power_automate_flows"]
    },
    "both": {
        "name": "RAPP + Copilot Studio",
        "description": "Generate both RAPP assets and Copilot Studio templates",
        "generates": ["json_config", "python_code", "mcs_solution"]
    }
}


class AgentGeneratorAgent(BasicAgent):
    """Meta-agent that generates other agents from natural language descriptions.
    
    Supports multiple deployment channels:
    - RAPP Function App (default): JSON config + Python implementation
    - Copilot Studio: Native MCS solution with generative AI
    - Both: Generate assets for both platforms
    """
    
    def __init__(self):
        self.name = "AgentGenerator"
        self.metadata = {
            "name": self.name,
            "description": "Generates complete agent configurations from natural language descriptions with optional Copilot Studio deployment.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["generate_agent", "list_templates", "enhance_agent", 
                                "generate_code", "validate_agent", "preview_agent",
                                "list_deployment_channels", "generate_copilot_studio"],
                        "description": "The agent generation action to perform"
                    },
                    "agent_description": {
                        "type": "string",
                        "description": "Natural language description of the agent to create"
                    },
                    "agent_name": {
                        "type": "string",
                        "description": "Name for the new agent"
                    },
                    "category": {
                        "type": "string",
                        "description": "Category for the agent"
                    },
                    "capabilities": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of specific capabilities"
                    },
                    "integrations": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "External systems to integrate with"
                    },
                    "generate_python": {
                        "type": "boolean",
                        "description": "Whether to also generate Python code",
                        "default": False
                    },
                    "save_files": {
                        "type": "boolean",
                        "description": "Whether to save generated files to disk",
                        "default": True
                    },
                    "deployment_channel": {
                        "type": "string",
                        "enum": ["rapp", "copilot_studio", "both"],
                        "description": "Deployment channel: 'rapp' (default), 'copilot_studio', or 'both'",
                        "default": "rapp"
                    },
                    "copilot_studio_options": {
                        "type": "object",
                        "description": "Options for Copilot Studio deployment",
                        "properties": {
                            "enable_web_browsing": {"type": "boolean", "default": True},
                            "enable_knowledge": {"type": "boolean", "default": True},
                            "channels": {"type": "array", "items": {"type": "string"}},
                            "deploy_immediately": {"type": "boolean", "default": False}
                        }
                    }
                },
                "required": ["action"]
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)
        
        # Paths for saving generated agents
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.demos_path = os.path.join(self.base_path, "demos")
        self.agents_path = os.path.join(self.base_path, "agents")
        self.transpiled_path = os.path.join(self.base_path, "transpiled", "copilot_studio_native")
    
    def perform(self, **kwargs) -> str:
        """Route to appropriate action handler."""
        action = kwargs.get("action", "generate_agent")
        
        actions = {
            "generate_agent": self._generate_agent,
            "list_templates": self._list_templates,
            "enhance_agent": self._enhance_agent,
            "generate_code": self._generate_code,
            "validate_agent": self._validate_agent,
            "preview_agent": self._preview_agent,
            "list_deployment_channels": self._list_deployment_channels,
            "generate_copilot_studio": self._generate_copilot_studio_from_existing,
        }
        
        if action not in actions:
            return f"❌ Unknown action: {action}. Available: {', '.join(actions.keys())}"
        
        try:
            return actions[action](**kwargs)
        except Exception as e:
            logger.error(f"Error in AgentGenerator.{action}: {e}")
            return f"❌ Error generating agent: {str(e)}"
    
    def _generate_agent(self, **kwargs) -> str:
        """Generate a complete agent configuration from description.
        
        Supports multiple deployment channels:
        - 'rapp' (default): JSON config + optional Python code for RAPP Function App
        - 'copilot_studio': Native MCS solution for Microsoft Copilot Studio
        - 'both': Generate assets for both platforms
        """
        description = kwargs.get("agent_description", "")
        name = kwargs.get("agent_name", "")
        category = kwargs.get("category", "productivity")
        capabilities = kwargs.get("capabilities", [])
        integrations = kwargs.get("integrations", [])
        generate_python = kwargs.get("generate_python", False)
        save_files = kwargs.get("save_files", True)
        deployment_channel = kwargs.get("deployment_channel", "rapp")
        copilot_studio_options = kwargs.get("copilot_studio_options", {})
        
        if not description and not name:
            return "❌ Please provide an agent_description or agent_name"
        
        # Infer name from description if not provided
        if not name:
            name = self._infer_name(description)
        
        # Infer capabilities from description if not provided
        if not capabilities:
            capabilities = self._infer_capabilities(description, category)
        
        # Generate the agent ID
        agent_id = self._to_snake_case(name) + "_agent"
        
        # Generate the configuration
        config = self._build_agent_config(
            agent_id=agent_id,
            name=name,
            description=description,
            category=category,
            capabilities=capabilities,
            integrations=integrations
        )
        
        output = [f"🪄 **Generated Agent: {name}**\n"]
        output.append(f"📦 **Deployment Channel:** {DEPLOYMENT_CHANNELS.get(deployment_channel, {}).get('name', deployment_channel)}\n")
        
        # =====================================================================
        # RAPP ASSETS (JSON + Python)
        # =====================================================================
        if deployment_channel in ["rapp", "both"]:
            output.append("**RAPP Assets:**")
            
            # Save JSON config
            if save_files:
                json_path = os.path.join(self.demos_path, f"{agent_id}.json")
                try:
                    with open(json_path, 'w', encoding='utf-8') as f:
                        json.dump(config, f, indent=2)
                    output.append(f"  ✅ Saved: `demos/{agent_id}.json`")
                except Exception as e:
                    output.append(f"  ⚠️ Could not save JSON: {e}")
            
            # Generate Python code if requested
            if generate_python:
                python_code = self._generate_python_code(config)
                if save_files:
                    py_path = os.path.join(self.agents_path, f"{agent_id}.py")
                    try:
                        with open(py_path, 'w', encoding='utf-8') as f:
                            f.write(python_code)
                        output.append(f"  ✅ Saved: `agents/{agent_id}.py`")
                    except Exception as e:
                        output.append(f"  ⚠️ Could not save Python: {e}")
        
        # =====================================================================
        # COPILOT STUDIO ASSETS
        # =====================================================================
        if deployment_channel in ["copilot_studio", "both"]:
            output.append("\n**Copilot Studio Assets:**")
            
            try:
                cs_result = self._generate_copilot_studio_assets(
                    config=config,
                    agent_id=agent_id,
                    name=name,
                    save_files=save_files,
                    options=copilot_studio_options
                )
                output.extend(cs_result)
            except Exception as e:
                output.append(f"  ⚠️ Could not generate Copilot Studio assets: {e}")
                logger.error(f"Copilot Studio generation error: {e}")
        
        # Summary
        output.append(f"\n**Configuration Summary:**")
        output.append(f"- **ID:** {agent_id}")
        output.append(f"- **Category:** {category}")
        output.append(f"- **Icon:** {config['agent']['icon']}")
        output.append(f"- **Actions:** {len(config['actions'])}")
        
        output.append(f"\n**Actions:**")
        for action in config['actions']:
            output.append(f"  • `{action['name']}` - {action['description']}")
        
        if not save_files:
            output.append(f"\n**Preview (not saved):**")
            output.append(f"```json\n{json.dumps(config, indent=2)[:1000]}...\n```")
        
        output.append(f"\n🚀 Agent ready! Restart the function app to activate.")
        
        return "\n".join(output)
    
    def _build_agent_config(self, agent_id: str, name: str, description: str,
                           category: str, capabilities: List[str], 
                           integrations: List[str]) -> Dict[str, Any]:
        """Build the complete agent configuration dictionary."""
        
        # Get appropriate icon
        icon = CATEGORY_ICONS.get(category, "fa-cube")
        
        # Build actions from capabilities
        actions = []
        parameters_properties = {
            "action": {
                "type": "string",
                "enum": capabilities,
                "description": f"The {name} action to perform"
            }
        }
        
        for cap in capabilities:
            action = self._build_action(cap, name, description)
            actions.append(action)
            
            # Add any specific parameters for this action
            for param in action.get("parameters", []):
                if param != "action" and param not in parameters_properties:
                    parameters_properties[param] = {
                        "type": "string",
                        "description": f"The {param.replace('_', ' ')} for this operation"
                    }
        
        # Build demo conversation
        demo_conversation = self._build_demo_conversation(name, capabilities, description)
        
        # Build system prompt
        system_prompt = self._build_system_prompt(name, description, capabilities)
        
        # Build use cases
        use_cases = self._build_use_cases(name, capabilities)
        
        config = {
            "agent": {
                "id": agent_id,
                "name": name,
                "version": "1.0.0",
                "category": category,
                "icon": icon,
                "description": description or f"AI-powered {name} for automated operations.",
                "tokens": 500 + (len(capabilities) * 100),
                "author": "RAPP Agent Generator",
                "created": datetime.now().strftime("%Y-%m-%d"),
                "updated": datetime.now().strftime("%Y-%m-%d")
            },
            "metadata": {
                "name": self._to_pascal_case(name),
                "description": f"{name} with AI-powered automation.",
                "parameters": {
                    "type": "object",
                    "properties": parameters_properties,
                    "required": ["action"]
                }
            },
            "actions": actions,
            "useCases": use_cases,
            "demoConversation": demo_conversation,
            "systemPrompt": system_prompt
        }
        
        if integrations:
            config["integrations"] = integrations
        
        return config
    
    def _build_action(self, capability: str, agent_name: str, description: str) -> Dict[str, Any]:
        """Build a single action definition."""
        # Infer parameters based on action name
        params = self._infer_action_parameters(capability)
        
        # Build example
        example_input = {"action": capability}
        for param in params:
            example_input[param] = f"<{param}>"
        
        example_output = self._generate_example_output(capability, agent_name)
        
        return {
            "name": capability,
            "description": self._action_to_description(capability),
            "parameters": params,
            "example": {
                "input": example_input,
                "output": example_output
            }
        }
    
    def _infer_action_parameters(self, action: str) -> List[str]:
        """Infer likely parameters for an action."""
        common_params = {
            "create": ["name", "data"],
            "read": ["id"],
            "update": ["id", "data"],
            "delete": ["id"],
            "list": [],
            "search": ["query"],
            "get": ["id"],
            "set": ["key", "value"],
            "send": ["recipient", "message"],
            "fetch": ["source"],
            "sync": ["target"],
            "analyze": ["data"],
            "report": ["period"],
            "export": ["format"],
            "import": ["source"],
            "connect": ["endpoint"],
            "authenticate": ["credentials"],
        }
        
        # Check for exact match
        for key, params in common_params.items():
            if key in action.lower():
                return params
        
        return []
    
    def _action_to_description(self, action: str) -> str:
        """Convert action name to human-readable description."""
        # Replace underscores with spaces and capitalize
        words = action.replace("_", " ").split()
        
        # Common verb mappings
        verb_map = {
            "get": "Retrieve",
            "set": "Configure",
            "create": "Create a new",
            "delete": "Remove",
            "update": "Modify",
            "list": "List all",
            "search": "Search for",
            "send": "Send",
            "fetch": "Fetch",
            "sync": "Synchronize",
            "analyze": "Analyze",
            "report": "Generate report for",
            "export": "Export",
            "import": "Import",
            "check": "Check",
            "validate": "Validate",
        }
        
        if words and words[0].lower() in verb_map:
            words[0] = verb_map[words[0].lower()]
        
        return " ".join(words)
    
    def _generate_example_output(self, action: str, agent_name: str) -> str:
        """Generate a realistic example output for an action."""
        templates = {
            "create": f"✅ Created successfully. ID: {{id}}",
            "read": f"**{{name}}**\nStatus: Active\nCreated: 2026-01-16",
            "update": f"✅ Updated successfully.",
            "delete": f"✅ Deleted successfully.",
            "list": f"Found 5 items:\n1. Item A\n2. Item B\n3. Item C\n4. Item D\n5. Item E",
            "search": f"**Search Results:**\n\n1. **Match 1** (95% relevance)\n2. **Match 2** (87% relevance)",
            "get": f"**Details:**\n- Name: Example\n- Status: Active\n- Last Updated: Today",
            "analyze": f"**Analysis Complete:**\n\n📊 Key Insights:\n- Metric A: 85%\n- Metric B: +12% growth\n- Recommendation: Continue current approach",
            "report": f"**Report Generated:**\n\n📈 Summary for the period:\n- Total: 1,234\n- Average: 45.6\n- Trend: Positive",
            "send": f"✅ Sent successfully to recipient.",
            "check": f"**Status Check:**\n\n✅ All systems operational\n⏱️ Response time: 45ms",
        }
        
        for key, template in templates.items():
            if key in action.lower():
                return template
        
        return f"✅ {self._action_to_description(action)} completed successfully."
    
    def _build_demo_conversation(self, name: str, capabilities: List[str], 
                                 description: str) -> List[Dict[str, str]]:
        """Build a demo conversation showing the agent in action."""
        conversation = []
        
        # Opening user message
        if capabilities:
            first_action = capabilities[0]
            conversation.append({
                "role": "user",
                "content": f"Can you help me with {first_action.replace('_', ' ')}?"
            })
            
            conversation.append({
                "role": "agent",
                "content": f"Of course! I'm the **{name}** and I can help you with that.\n\n"
                          f"To {first_action.replace('_', ' ')}, I'll need a bit more information. "
                          f"What specifically would you like me to work with?\n\n"
                          f"I can also help with:\n" + 
                          "\n".join([f"• {c.replace('_', ' ').title()}" for c in capabilities[1:4]])
            })
        
        # Add a follow-up showing capability
        if len(capabilities) > 1:
            conversation.append({
                "role": "user",
                "content": "Show me what you found"
            })
            
            conversation.append({
                "role": "agent",
                "content": f"**{name} Results:**\n\n"
                          f"Here's what I found:\n\n"
                          f"1. **Item Alpha** - High priority\n"
                          f"2. **Item Beta** - Medium priority\n"
                          f"3. **Item Gamma** - Low priority\n\n"
                          f"Would you like me to take action on any of these?"
            })
        
        return conversation
    
    def _build_system_prompt(self, name: str, description: str, 
                            capabilities: List[str]) -> str:
        """Build an optimized system prompt for the agent."""
        cap_list = "\n".join([f"- {c.replace('_', ' ').title()}" for c in capabilities])
        
        return f"""You are the {name} - an AI assistant specialized in {description or 'automated operations'}.

**Your Capabilities:**
{cap_list}

**Guidelines:**
1. Always confirm actions before making changes
2. Provide clear, structured responses
3. Offer relevant suggestions proactively
4. Handle errors gracefully with helpful messages
5. Maintain context across the conversation

**Response Format:**
- Use **bold** for important information
- Use bullet points for lists
- Include relevant emojis for visual clarity
- Provide actionable next steps when appropriate"""
    
    def _build_use_cases(self, name: str, capabilities: List[str]) -> List[str]:
        """Build a list of use cases for the agent."""
        use_cases = []
        
        for cap in capabilities[:6]:
            readable = cap.replace("_", " ").title()
            use_cases.append(f"Automated {readable}")
        
        use_cases.extend([
            f"Streamline {name.lower()} operations",
            f"Reduce manual work through automation",
            f"Get instant insights and reports"
        ])
        
        return use_cases[:8]
    
    def _infer_name(self, description: str) -> str:
        """Infer an agent name from the description."""
        # Remove common words and extract key nouns
        stop_words = {'a', 'an', 'the', 'that', 'which', 'for', 'and', 'or', 
                      'to', 'with', 'in', 'on', 'is', 'are', 'can', 'help',
                      'helps', 'agent', 'bot', 'assistant'}
        
        words = description.lower().split()
        key_words = [w for w in words if w not in stop_words and len(w) > 2]
        
        if len(key_words) >= 2:
            return " ".join(key_words[:3]).title()
        elif key_words:
            return key_words[0].title() + " Manager"
        else:
            return "Custom Agent"
    
    def _infer_capabilities(self, description: str, category: str) -> List[str]:
        """Infer capabilities from description and category."""
        capabilities = []
        description_lower = description.lower()
        
        # Keywords to capability mapping
        keyword_caps = {
            "track": "track_status",
            "monitor": "monitor",
            "alert": "send_alert",
            "report": "generate_report",
            "analyze": "analyze_data",
            "search": "search",
            "create": "create",
            "manage": "manage",
            "send": "send",
            "fetch": "fetch_data",
            "sync": "sync",
            "schedule": "schedule",
            "notify": "notify",
            "export": "export",
            "import": "import_data",
            "approve": "approve",
            "reject": "reject",
            "review": "review",
            "summarize": "summarize",
            "list": "list_items",
            "get": "get_details",
            "update": "update",
            "delete": "delete",
        }
        
        for keyword, cap in keyword_caps.items():
            if keyword in description_lower:
                capabilities.append(cap)
        
        # Add default capabilities based on category
        category_defaults = {
            "productivity": ["create", "list_items", "update", "get_status"],
            "sales": ["get_pipeline", "update_deal", "forecast", "generate_report"],
            "support": ["create_ticket", "assign", "resolve", "escalate"],
            "data": ["query", "analyze", "export", "visualize"],
            "automation": ["start_workflow", "check_status", "complete", "retry"],
            "monitoring": ["check_health", "get_metrics", "set_alert", "get_logs"],
        }
        
        if not capabilities and category in category_defaults:
            capabilities = category_defaults[category]
        
        # Ensure at least some default capabilities
        if not capabilities:
            capabilities = ["get_info", "list_items", "search", "generate_report"]
        
        return capabilities[:8]  # Limit to 8 capabilities
    
    def _generate_python_code(self, config: Dict[str, Any]) -> str:
        """Generate Python implementation code for the agent."""
        agent_id = config["agent"]["id"]
        class_name = self._to_pascal_case(config["agent"]["name"]) + "Agent"
        name = config["metadata"]["name"]
        description = config["metadata"]["description"]
        actions = config["actions"]
        
        # Build action enum
        action_names = [a["name"] for a in actions]
        
        # Build method implementations
        methods = []
        for action in actions:
            method_name = action["name"]
            method_desc = action["description"]
            params = action.get("parameters", [])
            
            param_str = ", ".join([f"{p}: str = None" for p in params])
            param_doc = "\n".join([f"            {p}: The {p.replace('_', ' ')}" for p in params])
            
            method = f'''
    def {method_name}(self, {param_str}) -> str:
        """
        {method_desc}
        
        Args:
{param_doc if param_doc else '            None required'}
        
        Returns:
            str: Result of the operation
        """
        # TODO: Implement {method_name} logic
        return "✅ {method_desc} completed successfully."
'''
            methods.append(method)
        
        # Build the perform method routing
        routing_cases = "\n".join([
            f'            "{a["name"]}": self.{a["name"]},'
            for a in actions
        ])
        
        code = f'''"""
{config["agent"]["name"]} - Auto-generated by Agent Generator

{config["agent"]["description"]}

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""

import logging
from typing import Optional, List, Dict, Any
from agents.basic_agent import BasicAgent

logger = logging.getLogger(__name__)


class {class_name}(BasicAgent):
    """
    {description}
    
    Actions:
{chr(10).join(["    - " + a["name"] + ": " + a["description"] for a in actions])}
    """
    
    def __init__(self):
        self.name = "{name}"
        self.metadata = {{
            "name": self.name,
            "description": "{description}",
            "parameters": {{
                "type": "object",
                "properties": {{
                    "action": {{
                        "type": "string",
                        "enum": {json.dumps(action_names)},
                        "description": "The action to perform"
                    }},
                    # Add other parameters as needed
                }},
                "required": ["action"]
            }}
        }}
        super().__init__(name=self.name, metadata=self.metadata)
    
    def perform(self, **kwargs) -> str:
        """Route to appropriate action handler."""
        action = kwargs.get("action")
        
        actions = {{
{routing_cases}
        }}
        
        if action not in actions:
            return f"❌ Unknown action: {{action}}. Available: {{', '.join(actions.keys())}}"
        
        try:
            # Extract parameters and pass to handler
            handler = actions[action]
            return handler(**{{k: v for k, v in kwargs.items() if k != "action"}})
        except Exception as e:
            logger.error(f"Error in {class_name}.{{action}}: {{e}}")
            return f"❌ Error: {{str(e)}}"
{"".join(methods)}

# Allow direct execution for testing
if __name__ == "__main__":
    agent = {class_name}()
    print(f"{{agent.name}} initialized with actions: {action_names}")
'''
        
        return code
    
    def _list_templates(self, **kwargs) -> str:
        """List available agent templates and patterns."""
        output = ["**🎨 Available Agent Templates:**\n"]
        
        templates = [
            ("CRUD Agent", "crud", "Create, Read, Update, Delete operations for any data type"),
            ("Integration Agent", "integration", "Connect to external APIs and sync data"),
            ("Analysis Agent", "analysis", "Process, analyze, and report on data"),
            ("Workflow Agent", "workflow", "Multi-step process automation with approvals"),
            ("Monitoring Agent", "monitoring", "Track health, metrics, and alerts"),
            ("Communication Agent", "communication", "Send, receive, and manage messages"),
        ]
        
        for name, pattern, desc in templates:
            actions = ACTION_PATTERNS.get(pattern, [])
            output.append(f"**{name}** (`{pattern}`)")
            output.append(f"  {desc}")
            output.append(f"  Actions: {', '.join(actions)}\n")
        
        output.append("\n**To use a template:**")
        output.append('`generate_agent` with category matching the template pattern')
        
        return "\n".join(output)
    
    def _enhance_agent(self, **kwargs) -> str:
        """Add capabilities to an existing agent."""
        agent_name = kwargs.get("agent_name", "")
        capabilities = kwargs.get("capabilities", [])
        
        if not agent_name:
            return "❌ Please provide agent_name to enhance"
        
        if not capabilities:
            return "❌ Please provide capabilities to add"
        
        # Try to find the agent
        agent_file = os.path.join(self.demos_path, f"{agent_name}.json")
        if not os.path.exists(agent_file):
            agent_file = os.path.join(self.demos_path, f"{agent_name}_agent.json")
        
        if not os.path.exists(agent_file):
            return f"❌ Agent not found: {agent_name}"
        
        # Load and enhance
        with open(agent_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # Add new actions
        existing_actions = [a["name"] for a in config.get("actions", [])]
        added = []
        
        for cap in capabilities:
            if cap not in existing_actions:
                action = self._build_action(cap, config["agent"]["name"], "")
                config["actions"].append(action)
                added.append(cap)
                
                # Update enum
                if "enum" in config["metadata"]["parameters"]["properties"].get("action", {}):
                    config["metadata"]["parameters"]["properties"]["action"]["enum"].append(cap)
        
        # Save updated config
        config["agent"]["updated"] = datetime.now().strftime("%Y-%m-%d")
        
        with open(agent_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
        
        if added:
            return f"✅ Enhanced `{agent_name}`\n\n**Added Actions:**\n" + \
                   "\n".join([f"• `{a}`" for a in added])
        else:
            return f"ℹ️ All capabilities already exist in `{agent_name}`"
    
    def _generate_code(self, **kwargs) -> str:
        """Generate Python code for an existing agent config."""
        agent_name = kwargs.get("agent_name", "")
        
        if not agent_name:
            return "❌ Please provide agent_name"
        
        # Find the agent config
        agent_file = os.path.join(self.demos_path, f"{agent_name}.json")
        if not os.path.exists(agent_file):
            agent_file = os.path.join(self.demos_path, f"{agent_name}_agent.json")
        
        if not os.path.exists(agent_file):
            return f"❌ Agent config not found: {agent_name}"
        
        with open(agent_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # Generate code
        code = self._generate_python_code(config)
        
        # Save
        py_file = os.path.join(self.agents_path, f"{config['agent']['id']}.py")
        with open(py_file, 'w', encoding='utf-8') as f:
            f.write(code)
        
        return f"✅ Generated: `agents/{config['agent']['id']}.py`\n\n" + \
               f"**Class:** `{self._to_pascal_case(config['agent']['name'])}Agent`\n" + \
               f"**Methods:** {len(config['actions'])}\n\n" + \
               f"Restart the function app to activate."
    
    def _validate_agent(self, **kwargs) -> str:
        """Validate an agent configuration for completeness."""
        agent_name = kwargs.get("agent_name", "")
        
        if not agent_name:
            return "❌ Please provide agent_name"
        
        # Find the agent
        agent_file = os.path.join(self.demos_path, f"{agent_name}.json")
        if not os.path.exists(agent_file):
            agent_file = os.path.join(self.demos_path, f"{agent_name}_agent.json")
        
        if not os.path.exists(agent_file):
            return f"❌ Agent not found: {agent_name}"
        
        with open(agent_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # Validation checks
        checks = []
        score = 0
        max_score = 100
        
        # Required fields
        if "agent" in config and all(k in config["agent"] for k in ["id", "name", "description"]):
            checks.append("✅ Agent metadata complete")
            score += 20
        else:
            checks.append("❌ Missing agent metadata")
        
        if "metadata" in config and "parameters" in config["metadata"]:
            checks.append("✅ Parameters defined")
            score += 15
        else:
            checks.append("❌ Missing parameters")
        
        actions = config.get("actions", [])
        if actions:
            checks.append(f"✅ Actions defined ({len(actions)})")
            score += 20
            
            # Check action completeness
            complete_actions = sum(1 for a in actions if "example" in a)
            if complete_actions == len(actions):
                checks.append("✅ All actions have examples")
                score += 10
            else:
                checks.append(f"⚠️ {len(actions) - complete_actions} actions missing examples")
        else:
            checks.append("❌ No actions defined")
        
        if config.get("demoConversation"):
            checks.append("✅ Demo conversation included")
            score += 15
        else:
            checks.append("⚠️ Missing demo conversation")
        
        if config.get("useCases"):
            checks.append("✅ Use cases documented")
            score += 10
        else:
            checks.append("⚠️ Missing use cases")
        
        if config.get("systemPrompt"):
            checks.append("✅ System prompt defined")
            score += 10
        else:
            checks.append("⚠️ Missing system prompt")
        
        return f"**Validation: {agent_name}**\n\n" + \
               "\n".join(checks) + \
               f"\n\n**Score: {score}/{max_score}**"
    
    def _preview_agent(self, **kwargs) -> str:
        """Preview agent generation without saving."""
        kwargs["save_files"] = False
        return self._generate_agent(**kwargs)
    
    # =========================================================================
    # COPILOT STUDIO INTEGRATION
    # =========================================================================
    
    def _list_deployment_channels(self, **kwargs) -> str:
        """List available deployment channels."""
        output = ["**Available Deployment Channels:**\n"]
        
        for channel_id, channel_info in DEPLOYMENT_CHANNELS.items():
            output.append(f"### {channel_info['name']} (`{channel_id}`)")
            output.append(f"_{channel_info['description']}_\n")
            output.append("**Generates:**")
            for asset in channel_info['generates']:
                output.append(f"  • {asset.replace('_', ' ').title()}")
            output.append("")
        
        output.append("**Usage:**")
        output.append("```")
        output.append('generator.perform(action="generate_agent", deployment_channel="copilot_studio", ...)')
        output.append("```")
        
        return "\n".join(output)
    
    def _generate_copilot_studio_assets(
        self, 
        config: Dict[str, Any], 
        agent_id: str, 
        name: str,
        save_files: bool = True,
        options: Dict = None
    ) -> List[str]:
        """Generate Copilot Studio MCS solution from agent config.
        
        Uses the MCSGenerator utility to create properly formatted assets
        with correct AI settings for generative capabilities.
        """
        from utils.mcs_generator import MCSGenerator
        
        options = options or {}
        output = []
        
        # Create output directory
        output_dir = os.path.join(self.transpiled_path, agent_id)
        if save_files:
            os.makedirs(output_dir, exist_ok=True)
        
        # Extract instructions from config
        instructions = config.get("systemPrompt", "")
        if not instructions:
            # Build instructions from description and capabilities
            instructions = self._build_copilot_studio_instructions(config)
        
        # Build conversation starters from demo conversation
        conversation_starters = []
        demo = config.get("demoConversation", [])
        for msg in demo:
            if msg.get("role") == "user":
                conversation_starters.append({
                    "title": msg.get("content", "")[:50],
                    "text": msg.get("content", "")
                })
        
        # Generate MCS files
        generator = MCSGenerator()
        
        # Generate agent.mcs.yml (GPT component with instructions)
        agent_yaml = generator.generate_agent_yaml(
            name=name,
            instructions=instructions,
            conversation_starters=conversation_starters[:6],  # Max 6 starters
            web_browsing=options.get("enable_web_browsing", True),
            code_interpreter=False
        )
        
        if save_files:
            agent_yaml_path = os.path.join(output_dir, "agent.mcs.yml")
            with open(agent_yaml_path, 'w', encoding='utf-8') as f:
                f.write(agent_yaml)
            output.append(f"  ✅ Saved: `transpiled/copilot_studio_native/{agent_id}/agent.mcs.yml`")
        
        # Generate settings.mcs.yml (with correct AI settings)
        schema_name = generator.generate_schema_name(name)
        settings_yaml = generator.generate_settings_yaml(
            name=name,
            schema_name=schema_name,
            auth_mode="Integrated",
            channels=options.get("channels", ["MsTeams"])
        )
        
        if save_files:
            settings_yaml_path = os.path.join(output_dir, "settings.mcs.yml")
            with open(settings_yaml_path, 'w', encoding='utf-8') as f:
                f.write(settings_yaml)
            output.append(f"  ✅ Saved: `transpiled/copilot_studio_native/{agent_id}/settings.mcs.yml`")
        
        # Generate botdefinition.json (full solution with AI settings)
        bot_definition = generator.generate_bot_definition(
            name=name,
            schema_name=schema_name,
            instructions=instructions,
            conversation_starters=conversation_starters[:6]
        )
        
        if save_files:
            bot_def_path = os.path.join(output_dir, "botdefinition.json")
            with open(bot_def_path, 'w', encoding='utf-8') as f:
                json.dump(bot_definition, f, indent=2)
            output.append(f"  ✅ Saved: `transpiled/copilot_studio_native/{agent_id}/botdefinition.json`")
        
        # Generate README for deployment instructions
        if save_files:
            readme = self._generate_copilot_studio_readme(name, agent_id, schema_name)
            readme_path = os.path.join(output_dir, "README.md")
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(readme)
            output.append(f"  ✅ Saved: `transpiled/copilot_studio_native/{agent_id}/README.md`")
        
        output.append(f"\n  📋 **Next Steps for Copilot Studio:**")
        output.append(f"  1. Import the solution via Copilot Studio UI or Power Platform CLI")
        output.append(f"  2. Or use the transpiler to deploy: `transpiler.perform(action='deploy', agent_name='{agent_id}')`")
        
        return output
    
    def _build_copilot_studio_instructions(self, config: Dict[str, Any]) -> str:
        """Build instructions for Copilot Studio from agent config."""
        agent_info = config.get("agent", {})
        actions = config.get("actions", [])
        
        lines = [
            f"You are {agent_info.get('name', 'an AI assistant')}.",
            "",
            agent_info.get('description', ''),
            "",
            "## Your Capabilities",
            ""
        ]
        
        for action in actions:
            lines.append(f"- **{action.get('name', 'Unknown')}**: {action.get('description', '')}")
        
        lines.extend([
            "",
            "## Response Guidelines",
            "- Provide detailed, actionable responses",
            "- Use specific examples and data when available",
            "- Ask clarifying questions if the request is ambiguous",
            "- Always provide confidence levels for your recommendations"
        ])
        
        return "\n".join(lines)
    
    def _generate_copilot_studio_readme(self, name: str, agent_id: str, schema_name: str) -> str:
        """Generate README with deployment instructions."""
        return f'''# {name} - Copilot Studio Deployment

This folder contains the Copilot Studio solution files for **{name}**.

## Files

| File | Description |
|------|-------------|
| `agent.mcs.yml` | GPT component with AI instructions |
| `settings.mcs.yml` | Agent settings with AI configuration |
| `botdefinition.json` | Complete solution definition |

## AI Settings

This agent is configured with the following critical AI settings:

```yaml
aISettings:
  useModelKnowledge: true          # REQUIRED for generative AI
  isSemanticSearchEnabled: true
  generativeAnswersEnabled: true
  boostedConversationsEnabled: true
```

These settings ensure the agent can handle queries that don\'t exactly match topic triggers.

## Deployment Options

### Option 1: Copilot Studio UI

1. Go to [Copilot Studio](https://copilotstudio.microsoft.com/)
2. Create a new agent
3. Configure instructions from `agent.mcs.yml`
4. Enable generative AI in Settings → Generative AI

### Option 2: Power Platform CLI

```bash
pac solution import --path ./solution.zip
```

### Option 3: Programmatic Deployment

```python
from utils.copilot_studio_api import CopilotStudioClient

client = CopilotStudioClient(environment_url="https://yourorg.crm.dynamics.com")
client.authenticate()

# Deploy the agent
result = client.deploy_transpiled_agent(
    agent_manifest={{...}},
    topics=[]
)
```

## Schema Name

`{schema_name}`

---
*Generated by RAPP Agent Generator with Copilot Studio support*
'''
    
    def _generate_copilot_studio_from_existing(self, **kwargs) -> str:
        """Generate Copilot Studio assets from an existing RAPP agent."""
        agent_name = kwargs.get("agent_name")
        if not agent_name:
            return "❌ Please provide agent_name"
        
        # Load existing agent config
        agent_id = self._to_snake_case(agent_name) + "_agent"
        json_path = os.path.join(self.demos_path, f"{agent_id}.json")
        
        if not os.path.exists(json_path):
            # Try without _agent suffix
            json_path = os.path.join(self.demos_path, f"{self._to_snake_case(agent_name)}.json")
        
        if not os.path.exists(json_path):
            return f"❌ Could not find agent config at: {json_path}"
        
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
        except Exception as e:
            return f"❌ Error loading agent config: {e}"
        
        # Generate Copilot Studio assets
        output = [f"🔄 **Generating Copilot Studio assets for: {agent_name}**\n"]
        
        try:
            cs_result = self._generate_copilot_studio_assets(
                config=config,
                agent_id=agent_id,
                name=config.get("agent", {}).get("name", agent_name),
                save_files=kwargs.get("save_files", True),
                options=kwargs.get("copilot_studio_options", {})
            )
            output.extend(cs_result)
        except Exception as e:
            output.append(f"❌ Error: {e}")
        
        return "\n".join(output)
    
    # Utility methods
    def _to_snake_case(self, name: str) -> str:
        """Convert name to snake_case."""
        # Remove special characters
        name = re.sub(r'[^\w\s]', '', name)
        # Replace spaces with underscores and lowercase
        return re.sub(r'\s+', '_', name.strip().lower())
    
    def _to_pascal_case(self, name: str) -> str:
        """Convert name to PascalCase."""
        # Remove special characters
        name = re.sub(r'[^\w\s]', '', name)
        # Capitalize each word and join
        return ''.join(word.capitalize() for word in name.split())


# Convenience function
def generate_agent(description: str, name: str = None, **kwargs) -> str:
    """Quick function to generate an agent."""
    generator = AgentGeneratorAgent()
    return generator.perform(
        action="generate_agent",
        agent_description=description,
        agent_name=name,
        **kwargs
    )


# CLI for testing
if __name__ == "__main__":
    generator = AgentGeneratorAgent()
    
    print("=" * 60)
    print("AGENT GENERATOR - Test Run")
    print("=" * 60)
    
    # Test generation
    result = generator.perform(
        action="generate_agent",
        agent_description="An agent that tracks customer feedback and sentiment across support channels",
        agent_name="Customer Feedback Tracker",
        category="customer-success",
        capabilities=["collect_feedback", "analyze_sentiment", "generate_report", "route_to_team"],
        generate_python=True,
        save_files=False  # Preview only
    )
    
    print(result)
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
