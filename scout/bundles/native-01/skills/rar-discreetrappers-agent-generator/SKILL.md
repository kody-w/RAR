---
name: "rar-discreetrappers-agent-generator"
description: "Generates complete agent configurations from natural language descriptions with optional Copilot Studio deployment."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/agent_generator_agent", "rar_sha256": "396da3af57b237a0b36dcca2adb1520220be5b65813dd89d09ae59d3d26a9aa2", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Bill Whalen", "tags": ["pipeline", "generator", "scaffolding", "auto-generate"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `agent_generator_agent.py` and embedded as the fenced Python below (sha256 396da3af57b237a0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `agent_generator_agent.py` first:

```bash
python3 agent_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 agent_generator_agent.py   # or on stdin
python3 agent_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@discreetRappers/agent_generator_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/agent_generator_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@discreetRappers/agent_generator_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
