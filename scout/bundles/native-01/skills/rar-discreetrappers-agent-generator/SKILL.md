---
name: "rar-discreetrappers-agent-generator"
description: "Generates complete agent configurations from natural language descriptions with optional Copilot Studio deployment."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/agent_generator_agent", "rar_sha256": "396da3af57b237a0b36dcca2adb1520220be5b65813dd89d09ae59d3d26a9aa2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Bill Whalen", "tags": ["pipeline", "generator", "scaffolding", "auto-generate"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/5S76Zak2LUm+Cq+on5IKlIJxox63V7NZIwGGKPBVS2JeTDmGdR698YjIlOZyry3qj0ilhuHc/bZ47e/HeHxjy/hMhfd+OUvX5iyrj+8IqzT9ssPX5J0iseyn8uuvd4JaZuO4ZxOH3HX9HU6px9hnrbz9dhmZb5c766N00c2ds1HG87XQv1Rh22+XNs+fiFr+tjKufjovj5ce9iuL+tu/rDmJSm7a2dfd0dzSf7x0iHdw8/Lpi9/+c//9cOX8vr85S//+BLX4XQtfaE/FfiuWDd+fbrOfF56veyPy6pPO/p0zLqxuZaSNPv4/vTHKa2zHz7+5/98b+GYT3/6+PP//THN41/+2n58//rrl89fZrdcls7dR9j3Y9ePZfhpePyp+0cRtkmdjj9+2/mvk99f/8fHN9k/5un8x79++bb61y8/XJLz787821cX/vXLn35x7b+JmS45//jX4jfN/v38Xz4+zfnxb79e/+Hfj9XlNP9tTi8vfgbyX8d+vf6bY2l7WRr/5rJfLf/wX6oYd0n6Oxp+Lv/m0BrWZfI7dv16/TfH+jFdy3T791O/Wv59Z/wr2/4WX9a0af3vbvmdHf+drV9z+W/T11z+Xat/ueFvn8Xyt3S/7inb/Bdi//l7+VBmP2VWe5VL2f6UIH/5tTpjetVe+5FdGbnABBp/OO277baftv/l4x/fPvzzxw96Dcs6jOr0WvzDDx9/+LHqyvaP38X++E6P6Y9/+tM/f5na//o0j8fvX/z9+H9++/6//vhzif1rd7rHaT9/8F+/fRoUTh/pv0mruzy/aisdx27842UM//nh0+pfF/2PP1lzmZD+81eV9LvO+Cbmezwup38DsevwVfx/TD+N/fLPC2ja63H5ZsiFG//jf3w8ynjspi67cCq+IOFjXNq5bNK/tn9t7aKcPq7fc5Fe963pOJWXS7/vu0CjSr9Frcs+/v7/JOUFhGk6mxeeXDvBr9f/lB/d+C1X//7jh30J68YyLz8h0qQN46/tN7i9LrryekrHNU0+omNO/3zB2Z8/P3w65++/K+/H/vj7xwVWnzs+tTRZ6SMO+2mp0x8/LfCKtP2ubxy2V3jS+BP16i6+Ls/KC39/uCybunq9oPDT2un92SmScrxM68bjq+zLI3/5FPb3v/89Cqfir+03AEY+viH/BF4bflbn489/vqzI6jIv5r+2aVx0H3/4xz//8PH/fvx3p74K/7zDuPD/u78vDWVL1z6uFFs+q/QKxRW8NEy++vsf//zuy0vM5ZKPKzplVqbfDtdl+06TnxxrifSfYQz/iNLLoZczm74bv2ZIOf/4IWUfP+t7Xfr5avoIP4pumj87VtomaRsfl9TwMudnT37W6XSl2ZQdP3wsU/r11r9HY/hVxeYTUOa/fzxY42owXf3ZZS41v266Dndtebn/57B/W7+EjH+YPpifRPz4oX1m3EcfjmFfjOH3O7LwW1yuVP/p+GcL+2jT7a/tZxdNP131tWN/c8/XhCnj7yH982fMP/t8cwV2+unun0As+bC78Lp8/Gs7fU/tcPwMRdxdqhwf+XJh9dUY/q/vKTUV3VInX/13afop6XsUku9R+ZqDX8v64+e6/vjzB/3xSOfwz99efHr2g73C/clA9EvI+A0Ipn+vwOYzJH23XW1+qX+2/msJXTLLbxn+kymfDvm255Lzv2cuP/yL+3xymCvd//wt+X7Fgb5VzOc742suf/za4R9fG+L1lv7e3z+L5zN+zSV3/HqOS5vuU+YnlnyjVZ+r1vEZ8U9EafpvdjvTpeF33Py55C++8Du86I/fgfEq46Werz0/7//xJ0b078zjP37LM37Ror4BzS+8c22n2+8O/xqteQzj9/QTAn40n16Zu/aTePxGTntZfwkwvu+1P49eCfbLjfGlR34l9X989vsu+UTntZyPn7rTnz6ZXxmnV05++Uu71PUPXz6F/oYlfhLCn539SSY/aV16VXr69emb6Z+ffk1/P4vkm20/9Y7up1b3Wbc/ccyLsbbLRTX/899c91W5X5Ksrzt/wZ+u519Ro+v516TnU+9f8pmfJP4OP/m1rF8Sji8XiZ6P/tMrV4O7wO2z2f0mkr+1XvtvquITZ+efvXP5Iv5apV/+y5u+heW3VzQXbnXfAOLnsvw9KVfnCqOyLn8K2a/lqJdTPlWa+jS+QCb++NX2q7VfIfh67Ddyvy+E4xge3+75lnC/vYP9/uZnff9rXX/N974NPb+jtf59NPoU+F8ORF9T4JfJ+nPAr8//53Z9E/i3smnS5HOcqb9bmIUXMnz5SxbWU/rzqehqTGnYfp5L20+q+LdPMlmnSZ7+6tRFl/67Q1sa/S0au2361Ol/f+5fWnfRJyD8S+1fJvqvBH25GmD/m6mV+/nQx/dDf/n4w+fOP3z88fvRP13E99dhuqjwFYY/RN1c/OEXFf39gn+rqB++fO773cL6uQi/j6K/4+Vfa3vxsK+d7bNX11P3rzb1vZF8B4bfevlq72n+fQL/bXLx+4V1nzxy+tpBpk/5P5341sn+f9XFFK7p3772uN+J5H9p0OepX1CIr+c/1y9C/P7yuxkwpsNy0ZHk0/ffYfl//U5efOLpt/n+H18uVA8vyAy/4/p35v01OcY/T59sBLz9CF3XXc/fYfQvX/7POPn3Q1MRXiTxOoVQeBIiYYYREYwQIRQheBLHIRwm0Q2DIRiGohSLcIy8IUlCUglEhSlGJUgC4yEVhvAlb+qWMf6E6KYpPxXZuvF9+fzP86XMv15fS8l3C74p8umbn0eArz3rmyH/+BLh6LVTRCeJ/vbFgsCNghGpMrHI1wm07M/OodmczpK7JMG61vgv35WWdG0ZeS4cReugpcv7d+k7g333mIg+eM5GHlFVTAWVFUJETSOv69mLRkHdRwAkaxh8N0ju3aqYF9SuQ+sJdOqAODtSeR+mw56xR3ueUDZpIEi0K1rtsFGhmM878LpBCqAMeNk+4FIX7O0GxDX4mDbF9yfbkeEUe7E9yBcHDlS6EJjPBjDcyXWbmr3lTxaiItCjER/18Rlqovu90d0nEgPrtnHZxMp1nHaiyvb4yVMefEfbOvXwSO9awzvw5TGyb929L49SpHViz0XYBFyeVYFweqDaajzpk0ofaQOutnvERgtlMjnfskkBKpkvVvIQCWAxsQRlqYUdlD3jiufRk3Ua3UkhNbI1QlH31e2k47KUtAVQHT558IBPjquXKkvk9j5yoGpjmA2aG/1SMmZoSWKRDmUAXneJ77JgxUoojlPgxcdBDt6hgwX9GdjZEwDpujCY5RhnvapScX1yj5lVZINJ9Ayww3w1N+V06uOOmVWku2SgyJywmTciqTYgm4rRAE9Vegzt477eH9nT6/sSbEkO3KZthZqdXbdUvadLSyhkxpXYm9mJBg4sQWfrjA2KmyTmLxvmfSsrF197jCvMnY8HWOgHOnqAv0GNRO82GkxaBtE7s/JWtGhptz+lpXKPtCVYgfHaiZbkmT88OUh5o+GePheBj5cm3IJFKl6lZtE6gz3IUtbI+fLbGlH9Hd4iudlCe8gAqHlOKGFE00NFRmT3s/hF3N98ifOVgnIPJkU1mLlDGVHU4zVnYl327MwbAhlABhIOecKLFoej/zjr2/gABYJ3fUBEgC5mbjBJsSvKzsA2eEpjQJIH3Oz2zm0vQOJbjZaIQPJdw6grMbPQPDENA8/Fhn97MsUL93V/YeMZydBZKKAnBMApSODibiWY+8UoAJDCqvTIECVUSnqXoDP6ELabl4H4YrsWUkanIquDlNahYLQk3z7PrRhPhb+DrRcy5Z0UeVKWejbLWYQ8ZZK7nDwaT6RVngqZB5RD34B0lCpSDVmR3c81pPZw26NF79w+eljtk4QyMO2hwTSnynPjJ3N3M5rz9fdypmF23zkgWyr7wLR9uxkuHjzvbOTdWHNGUd7WHuVNe4PrE99hDBAgnGF0hr+LrIMxTs4+dxRjYDkfEl8lD8ipte5KN80tH0ZOuyqu1ZqrbCQwo3Xw4BPKBQEIA9eMYsDn1O4Tqr964LwD+quot4QmXwQIpqAPYabe59uGWv47L5qt3F/k2p2HVC97CXu8TBr5iaCKXDzyU+Mfb+F50MkeQ6CMA9lzaI1ZwvUmx542RKas+aRJI36mIPEO8MBCYhtlD4+555xJqNTGvPlsGUvfHIjy7g5vE1dZC5C2iaEU7d0j5kFrJuvQXExWSIhnay91fRE6gBKYbL0xay2ZBCQsYq9vrfE0Iu61qTynrhvzkofXDcTioJIq1AWbWL8gkDTVWEKtt7LuxKnGZY7OGfqA/a5bYiujWWQ+AGRpn9MWL1ShHM4bXG4v6wSEys77rmfw3MvGxyTMyrN/oyHg8S4bWUEV+3dQvz1tNjYB/rCfSmqCF6pmiBQxKuQ+pztjJ6DWVIky3SmO0NjVn0nGOPQYqZ09UvqzpFbJrFEl0em7lpqG/ix98NBAKhyZ4Om0GGFaJQPq1CnRMUVVVritoHj43euqueApz76X8WrGvzrE6wv84FMhlKKcXLaUJ1a9MEK21+Q71E710ToiBQipPyQNoMhMYEr+uxgzZMdJ/XRJO7U38PZSIVBRve0ZOazdJOT6ZNgnhrIvmhobNNc3f6+3oxgsLJ7uSV2QDOpTuQCXySBngC6pxiShT/h29qKWETXfvRXnNYSdNIoB2qRNdr/Ud1o8MZ0Gf98hBaoqeELQ9GX5NR3l/QroApFrSMsfK2akoy3unFt72mNDV9AtyIW2dQPzM6xFBbSolydI7H7x5kBs6bEhUHWuaqXMLPQAYuUbopuhLzDswbVSHUksQS0vMrCzCYsZ4zXZ/WHYgGVbNDLiPsqIQvmST1LJx6qjAesddoKg+qyUyHH/nDPHsXYSz/BCl4idI1y25g6faV4btpXLs8/D0fPy1sL3+1CyomwASzbKKqxtAH3UD02CgPm4i6hgHVfPEEHpcBpGGdwAflmo0+ZsAU/QA5mBqysNkUfYhNh5PRFb1lnaUE6WIsW0RCm4z/XN7t1YqvZd2x6Su6lUsMA6mSEjii+vdyjueNqyU4RS/ZwfEsvjcgO5FkeTDFhDC73yDSuL5q7EPlXVZnQSbHwkLE3QkBWylSdK3r3KXUfwXNsQV7+/epPfg8xL13Ig1TaGH4YeGRWMElt+tKsbZUOvTfbrp0eaoMSAU2CYfqCy71vTRMVNTxImej8SkMESZzQMWeEnk1bK/eHMQ9GyWNUJJ/9C0H63xDBCJqVZaRpwnvytLkoh21193Pi4VR6YAZYK6x0mJwq+PAA+bUR7vfJRSW/3tlW3NzDxcm4VBu3PjJTqJSqyj4cuJedLApk6E1BioBj5Zb229crkJzNyjRKXI/4cTTF2n42Ro9EJUbo4Ang/vTY60KmRDFdkx8gLve/2VneZcEO7zQUgLd6xTC1YIxekwSVUQxvPTQtO4gBvz1Yx5o0H6wnU5/pe9rQ+LItMX60eKUvbLtbnUdzPB8SH4R2xWwcOl1A6UOH2ZAkRyaYXZJsqiZiex+3mdjDp9h7oVSBOR7T5zs6bwJwmjcMnkUzI5n3hxh21XkwlHT0ovjclj9/PAnrx5dnLW96UkbfpvAN4g+/yANLeHu/+/mbv0vbutz5RWVWiJXa4DTx1mypAaB4v+pB58RE+8Vkno/tbGPsYye2ghM3DTnf75dG9lbpWRrhuW6BP0xgz1gbP+PRFQ7rlV753yhgrF1pnrstmyVPR0QQuzk7lrKq8x7QotBpa8FsF++uFoW59SHLYgbT3SOLKAd61Jy7m5r37WGGsNT7rHnPZYoC3o/QZ1LbCxJD21m+iXQTRWOIkhomYOx89nu1KSDRbW/6VAvTsnAaVKo/3gGxB5jnCOE19T461yrTzKHkH0W6qhrt6B1Y8XK+5AVrYdE0CXPscHV5koJw2g/jKVRbVs9ClzwBMbt0F/BPfi4OFRnL8RolzDj1S1/BuubkqvUkGC6s3SZkJYbglHkUT+fAIiiBIGf0+785sW7cHXqcYx+jYcD57PpnO0EiwbTf9UrKHF4pi8bg4xF0wH8N9IfsruUY41KLHzV6oEQh70Tpu6YSYQvp2GfIuNY0aEBxvTydNnvRAB5YIKwoE92mU6GGnggVQlWvOrkvbrGpJkOVxjQhjikMOBB7g7joHWcFKxx87EQRrWnSWpaeytG5lo9yns8OwmzCI4tVlrzsNWsfM1Zeqpr/Yf8yqyvhiZmCG+SGftKDWbgI7yplojLL44hYcX54eo3ajCbZh2CK3m3meKSuNT+b5glSK5DHOvBtZIW1Mhtrm272ZVXl1g7wguU1NKQ/ljAfsJfucUVaBEWg8WjZAlW/b5I8TFR28HRb6FggQjxwYtu/Y2Gzw7TDVYB+jcIGgkgDFxJJHE5Ps0z6X0mZvosvF2rhZY1FaaP2+j/kYcz3uzB1CmgVmRKQgH+9rstqt1y0xX0Vk2zEl+uyoLAKSa87+BHuINvfIUkoY4I4yuPEk8vZNlSZQ6gWDhXKDE5tNXkC/ti5ke2O3PGXl8Xi1qp3GZFln2ygjS/6oL4C4j9hzb2RTNLsAguqLcj4eXLI8X+6+3XNvKIJxeXuk5IRQjg+6kqgKrZdc3xsT2z5NpoaFoyXGBHxf49LZPSVSsC3iFWgdz6OfYyc+Jn0t2g+tqd1OKdpbGifIE6JVeOYUTgIPjxeL6b44j/Fw/U5qWVfpcUmWPVfhD5DFR4Fa0zkyiPWx4CcYb5HkQUMiyejFfCf0ngm+ySGx1M3SoL9iHTgubMHPPDBLC37siTxypjEzJqzY6pvaxAlgmBHd8nvGu/gy8MKzxZpZzUeTV+tWzATEffjO4cUuCsPTjb36UtULwYnvheXBR7m2Yd352uJgF3DguLmQFiHtV4+3OhED6k1ZHjeeBtzLk1ubPVnhbNpOQwcp6eSCF7nkMGsaPLtEuEJm9qrAnwSYgZQNbLetuSDubbFsAsL06QOP0PCrTUJZL74JMBBtNr+9PPSo1oSYwpEaVMmdUMFMnBNcU7I7w4dSHECDhmpeIE8Rk9d4D8NJLerIZBov6G/BjF4t0zObaYhzcxOoy3ehsVSPFtWf0ug82eOOUGiYtHRb64/x7qyNMdc1jsX4yF9orsV0mJ18xw1nQnFlbMHh6asBXi21nahoYneYcvUfMazue/S+pVtZ2/ky04exRHCitTgxo/BsKYU0+XVrRk8uuXEME9LC6Dql6suh+x5n95W3kBFP74GKJyZxlciBBSISTpJQPHUww/l5Yrdwr4/X7pnuVBIi31jcdKvtvb4lT/6quj2tbzPQwGVAuTeW46ktdsc3YL6hFOnj1diNKEoTGXZ4vsmrAu/IKzUXFdOBtw2hdOnv9s6L+BKxF7Vtb3Yy1UwHudx99y+WVulPYWvvhADNyxGErL4tLjG1D9nJ+OLO9p1PCDOzZFb84NR9DEBbCYZ42jWf6BHQ0qnaBsgqeDkOYzVIjrqGOh6Q4t7nuz69bXDvdeuWX3woJZ4aS5bh6zZcTKVToVAu5KIW4Ke8l6KibIDoPaxASQRyuL+8qDBvjpWnYNVD8MURQO753gAKXt4ZboMPvxpugv4GXbYVrylvXOqyfABGcBrrXoAgJpxV2pZv2S8P3dxPL2jAtbKImJQ6LmESNc8x75pZwIIcwqhhMpyOYGquQj9I69ZFayGyRdydomZzm/4+NAsqLLpxH66ZBAgzFvUAUT5isWfT9Rlbo+ZrkHEr+8nc0p6Jwvam37fKhzErhu5kFsGpBvaF5NwmIy9RMuaSThpU9JY8mPvY9xcTRDvHFiPLG4XxTmPEJnkzlkYBp7LhzXq3z6MFWX/2G9F0cpLtkFxhC7rZHhOnV8mo+nMErtrt7rYSPMovdMrQ3HugL9HGfJwpBGuznxMl2OOoh1UKP8AMzcAuaFSzPObTFgoq8pGLUs6bYcBXPSAggIDgAoIbjg7w68ERSaz2g0pGjgfINef5k1ruw+PBAhAEsdPycFmXW3o4frhc5AyQE+9H8pJhSfZW6YbvmgIxxXWfG6bp7o5xvPIqJQ5GxKsgCQnzrXYK5jYL43C7BxenRS1VeGiEd+qAjnOvl8s+OvTQAgZ44gsO6lVPgsvgtMEBZO2IWjOXGZtHjYnuajc11cg2bQfHQK5pSifuZ/OmnJUXTqzjVKdA2nB9zDqjvs+6frPIchYx3B+FV5HzPXE57iad6frCa2t/5TuRCgQ9JIkdXITmEc9TrHmO7i89oGPl9iRcpvBeMYzbhxNScy4vz2MJ1/datR5evUXnoYr6OPtiuyCbkt27cpInxcLm82bK8XBGSgGxxMort0d6auPLMypq7I4EApA9ykyxeh5M2Wm8wolgZiwkjpHQzTqcbnyGgyQ9cdXpfeY12kWZTMAVV9hdiuIcq0pfMaxExgfo6j5IaFDSl54GBzgzKnySvKcOnwTRGs1HuABGNHuAaSClOe7Pqi4LzYo0LiANoTJRUNdQg0F5iHVf16xhUiBgrOuSVDREzwhlavCpPG7WE48sE7IvkKJ0vX/SEi+oC2M5dOK1GIivnKuqKWnBRJnag3rysgsZFjaQUDIrWRn1oxZLY9mFWyXfOXdjFtBoQPiZCPfHAD1Dk94wnTWeKGzeojK3V5It2OcFIEF89U6rnzRHG1Cp4JhUUJ8K8pJq2LlJWZPyoizRfRjYRHNc83mV9OgKO2ZeWDpQ2ReZtFvZPQK92bTPH1BwXdXsDBF+BdXCWeyNXHXuMrdSj23RD+LMkgHCrc6kJFY1tWRwvV1hlmfnH3lN0DqL4iBzlYKYuediZth5QZ3PbPydGxZQOJXaZFLTrDKjch25lVBXtSD9xdZtGuCWOiqdv1bY6YKPWhq9dzBb1SLwhzZgtHbNNxqe3gimy7IytbwtvwDaf1iQsUEE8WxD+14Sy1G3XLtySAIjsByPwtFs3c2/cel2VUWRqeLRZzq1jZy4tc3NljM5xcTBj5Q30o+xDc7BgGSVN6TsCPuwUFcie9lCyqlAa7iNHTjk3V6rqDOQpkheZrvLlU4M45USRCTJuWsSCD+gJ4wIVnU73tbr4STCCqYc0DB0BEasG9drgGMdZACAJYlbaLWMgEjEeeS77JKoMBaQi4vBRTjD1BBHwfD8zFcRuIFNlHsN4jjcB8ET5bpmGofoNz3Oq7sXJHuKPt5reoMYgjEDsDxRBIHsDKjS688m6rdD0IBkOLNw5VZSsa8uM+3JI9lcnlxB8Rx2rAfSLjtNaxMUE4c0q+cI7FSn+MWlSJrJswEefK2ER79cXbZfZs6HjklXtT0FHy3OtTMhEjF8v3PRqsuUAYGI5vXiIlDmU5mU/nYXTUXegJdlzfHLjypmH8MeyrwwxEGOvHpJET2vdkoU3nLvAbDVALeBsMMfvGB4h2vrI+Astzi/ecpGuiEDJu+8ojQxsJo+h9Scp8KOwZUHBRHSKN+o1pNqbHMm6Zq9mgF1nhICtleALtYPWlFw3pm0xo/i8Eg7XuUpYwDOgur8Ga4BQzXICL4ZEGmwDYe9OrDuhakangbctnAYbweF6A/d1IRc472SVHAJfkZDLyJuQFzzcWcb72tq3sjEiW+h0nKqEHGdJMjkc7QYEIqLZ30uFdcLPMTFt8kFZS+Pyhg69A6YttdcTyMO+F6BEFdHKPT6LkUhrLOCRsdlTrFL1U3yPqTec6hzBdhWtOnq1/12dpLUKzcmD+4zFgb0ezhkVCNOYs9UR8u1CR2Ja5AX4z3O1E53r7dB8cbZ0iV95i3x6CwVmietvOdC1fGuJ5mGYAdOfI5z7iv5WvMgmRBAfWv95FSaKS0ddT6MapQuTEbHTEmUjjtbd1+LLsM0JLCLtc55uWFNs2uqERn8iS4cs7ip2CPFXnPe8+leCSxSyN7m2bRRbeQWFDTs9VYqR4Hll1yXm9Siy37LeM/Q1fT3bE5hhWLci2HbchO6vja55jiQoa/WhfM6wjHEc9VY4y5b+Ihd1AhoK+rNt1qsncdlVzXW0t4HMs3NeNOERam81DvIhgUqsYy/KQaKAa8A7Wb47aEq6j0O6a7DABs+tstP5OvJ8cRZaYqpUNx8UHlmhv4LV2JV3Ig8ihcE2o+4AoVJH7e9w2NeW/X3MSZHm9zj6kj3vNVJyyKpdJSY6Hna+DIrilqtTsmFQiiu75LdOu3ImNfrdTgTkr8pyenxaO5o2ebeMATJK0thtQrbnJi3pBEP1v5QGgWoGA3zr5H39ZZUS/cBMF5d13lekeNAF3raa6wT+DkZaeyKXReH9/tzJUOwIc+4sbsjKlUbTgx7eAl7iEyP5xqDhvLumNs0scErW8jX8lKKR+gOrT22rDQzQ3qsxxTjVWhYMVPtatIp1ZvDg5uVHehYAJbwQNqms2GXwBS6tJ75BDvxuEUTyV48bpk6WNhI6sZTJBjBt3p/Shvg8+QgPxQr9s+saCCLFiOprTCMvLUgtBggOlEdtVfr0byXLngnA3XAK4mZQDS8K2oZH8Ap3fEpBgLHpgoYsPaT0W+690AO09j1xyvC5Ou7ATSA1aKr2DeAaZOv4rlQ2m5OZmMcISfcegspbefUiJS9IBrWdcpIIuyOUQDDT2FxZh2j4fW8vBAZrCgSA3vkhFoTVTTj6TKG1GMKgsDvketz9iGtI/PqH0AKXLxx554G7L1Dl1dxTVUY1d/vTY6+sdBs74eBk36WgdUKW2c+ctiDXMZtiDmVaHh/pfct4ai2bRH8vWZFeXAYAOqf3b2pZ9JxsyrXUzN8bXoa0V2B8dZL5Q3NCIZckUKPfB0uWTZBQaAoNrvy4nmvFhxgiAzfm/MgJodLDOesqmLZd4J8twb5ynyc5mvptfcYqRvDg22E/X1IhGUoCs2cWYDlBZqPiDs9SSOIXyN35bak88r4BNuAt198KqHq8sjqp6pUgFghILRq6paWm+VwsgPDeo0h72242493+JTqp/yCUBven4Wcqinyhoir2U4sH7V4NXIjvLbRQA8D/nKwTcta8HU1k7JfStk+XCDXecz1c5ezPVWllIgSmbW110oY38pbD7JXtPgjk6qxxOcejyvyW3VtssBxaJiOSi3R5hjT/I5aV0Owy0GmFAUtmGPCbP5FDiU+m9lWRC28WMG8Ue29jMb1OVZMZkUkfh9Xh9RZUlrVx2zlG9JW9bUTxnLKeLs2G0s60qI8EvntbODbk+9EnpXZi6n3MgnJxRZzz96ut30LkEkbuOi0Z32+RkBmgujgXdBudw3ldM+LqVjRYom/fevlIY/q1fDB/ZrCSfnuIdhDZ1rHM1tEkOn50TlpAk4RkmWP3KH4s+o7q3akmkJU62ZN601w2TsBAuYYZi79BJRBqji7zarYXorIcsj0PEk8q7F5Q1uv9ylufyT0hozqngwsFuFiixjuNX8ZcGoUOwWbSN5C7Ctk1YJfGPTE7jYw0/k6JXMZ9J2JDtPGUhMmknEhku6WHrfyzeWXL4El0wojy3yXZNyJ9mM46LmIWViZXuk7yZsOCDm++Vixs6ABx2RTIKYxXqraiS1q0IOeaxvM/aSA7tpX5Yj5pbNlqVsY534osWa8QxNg+k7Y43V3EW4ITwIOIUrqe6nk1FJoZ7uRuiC4IOnk/ADbwE4umYqX3w76BNa4ZIAsYSaCIwmcCTL+FNfnRUAGAzHRrOunkHrIBiNA1+SV0qiWemvEzY/8gDVU80IYXAXyXNeQMhANS8MDFpcHX55YYD6FWsfNJQe5EqDc+Gqg2jsGHD4u7mVVTTCFA7J1R7DD8/x547gKekJn9RQkX0erxXGYvEreF6Mn9zAnwynAW/YOSiyJW1eV4KzcQ6Gn1fjtqdpY+ZaXxdcSbt4wmytaP227Z6foRwjdX5iAPGkZR51YPpiDf+du42fxPrPwa7KedT2GT31PSLxPoKcu5ABmvTIPXKUO4mBBQN/3fUWZR9bz6OGY3On6oR9Us2KyW2yXYTNU2KNf+YN9zCbdg7cotlWEtzGoo4q6PeMZy0sP8vfYI3NX1kymbZWNxq/a3SERZ4Z7iUS9io4p1eQBlpG+tVtLWanZpAGQh1BqG257vzaRUQWLiXTyRd92I8ZcsS+HvXFdfakdavYjP70xeg0hxzKyHeg8sIdLOagycKA4xiLSF09Ymy9GBuFj84pjZpr6qH/wLrb49SINFpZsYZP33nILcYO5u8f7ubViUAc5otbFEL6eISt1IaRdVBDR27vvl9BZpjrtSA26Hws6PSZKY7GrppvWwge1c4bmpolbdLbK3RJ573IjlqvXkPG20MYZUiJaZ+mVQTy4kTNpU0D+otYRV/u7jdLeemfpDC/E02tNYr4U9J8cuEV8UjpgAdYMq1fyEJLP8LkS9ohcDUlRMJ6IJIq9ZkBE1pK5wPPRxAOjcdimHKRQfmfarr3nKKAihDtJMe1efQK4WvNGFzIvkFKOAN2Oh6sQiK1Da2bZZQCTLLzWXOllFD0Qu0ScicxwTmOiO6zHm0B6GJPP0NNd92nlNotY0WoZn6WYrTXcUi4SNiWdFL7MKiEpiKVuQ9gc+gE8YfZJGFiBQAu/aOIFdjJhH1Gzb8ezAbl7Qr5tkWp6Set1l9336fOnbApHISziaUs+pXNHYY5pwm29Kvs2R4RhVShStb6PMgycMdCzkHROQHZXy6UNnpC0ezFONmuJ3DoplVJMnNM9KyfkEWCYXtHbTnw9bRnExnIyVeUCx9ZHea5ODJhhlit+hdWW4y+tl2tXnb/oLQDiNrCxwk/CobkTt4ioi1pwc60CqpYYQW6iYEdz2UARzTF4z4inxK269bysq7ZaKzR+TYltSpeRbSZJAAlPCzdh560WZ9rLGvRKrPfeWSwsYseMwSbt9gV/P5SVXdySzJ234jO8hxF4/oaJyAAg24l3mlaO5WIUWPTaIIq14yUvaef+WsBDuINm94KUPUGTtJREasYm74Y7tDA4M6gibwS1Xdxxz7EV0rbvhweEFU3zBO0CupyhyAINbHeFQN8phGnYgSK88cBtCZfwluaUxOjKKEv4IFOXyRmFyNKi5JajLy6MlWjGqOWWOG0k4qkDU5smvnKuGnWJXCRnqII3pwwvA2OWi8PF+WEL2VyTm6096S4/01bnWOy1tI+FlopTDu4vowZSjp7FLilKwcpEXO+QPD0tTUnWHptjUp/wLtXLiQTJXPSFEiMrN3KAabWF4blGFslSSuu4W7tVMGflCqOHaGsOqHJsKez0INlNuPwyl8gzJ1641xyQwINVObJ/39yES9EYyvIyHTySQylkj4ytYqCdlnn6yCbSc14XsoQHqTo0U+Ep5gi3WXGUxwZ64JEKAdGchs3jZH3nvXtL5fvAvIRhltSlsR+kHiyskQ7uXD8thVmOQS2Dmg6mNcmf1HauLzygiajJgqWpwqdYx5IMhc1qUbzEv6Gk06VNhbF+sxkdz6PPL9e4UR0UkTbwUqYi6o/IqeB1DmsE0uY9yetxKVFRWa6uQqeKxtEPwgR1odcBmEUxMiild+e0MLcUhBz1jfwCtqQdGeCEbon2eiJ+xydhzND7XoW+K+7SkQNjNdoJcqzNLemY94XhBnMZ4GeFsAZ9PFt7ch87SELQ8QwU4alEwy4XeYRDMMAH+M0b1nS5Kb5s6nTR31RWnulF8s7Vw4saL8E2nJBjv+bjJIjN52wibqXDVDgmMpErMGK+w60i0DBbzRLQBPlGIRsLyPH9QKgjxCy+jqfxMduhrpMeKgL40s9nkPhMLnK3+61u49RYcikq5RESghG2FkkPqOC5VlIzv0d4wSYQlSV2HOV1kc+cI4Zkk0sZaycOmYw77c4r15YZ7CM3S4ioSscWor8mDTJ2gNPNl4i7qwDxRB4j1epn4Ha4q79ZQpZfLqIbmXMbAwPxUggIp35ZPXjg8nMVwBt5+I8hfdfmckp229jze3+Gvmk1U2IcOauVqdbKOdJhMtqf+Va7L1szMXORtKWkEi6ZNJevbujz7vAtUhYFy17ph6sL1ZA1aMV6w6c1p8vQnixzmXW7KJWSlT3wpLMZ4pWzYw/5VO6v5u7T2sT3lUzeIUI1ZPNuqbXt7deU8sKaiREevAVKlazKu65zqJA9D26/p1pMv7EHy4x2o9i8gBiL7biWM8mLhbtsWTvnsQlvnau5NlT6hihZ6Mz9cwbQxUNBwodWvjaSXhESv6pFUqjc6uKtPTIe1Pr597oSCHakuWyuF1slwymAEEFA5l3uwJGV2HE8YWcKtRPCuPVSgnNEoa8PJUrhCC7u+hism5WN6GhOcSI+Za+8q6J+7Bw+9TClrVG6PM8K5oNFvrFp8mIBvXza2zS4Q8MozVkzQ0cP4BqhxruzsHu/x7NoZS8b2vZh4N1zA/cQFwulUUcP27wmWeCqMEPtlhfpBHSyzD7uChkqrsCCDjPk/Hh1F1++iOp7Q6Gu6Fag4xYpkWHvSQMlkNVeNPe2wHkoRUxI5gPXHJrjlkJaruzC4sszJCxNre1uLkElkFoNYXzBzaM20bhlmo6w97cHZnVrcyYJvpjRS4MB3JvZhq2TfVLtwAuU++Fpz1ptzfeb67XDPZeBrLtjMeysWRqlJdTYiXu8LCbL6CtlpfxHZsNgoK8C0wAJfo8OhgyUqnqLhdTwN+KFD/ZSX6ViNDUamZebx2WLr/BOFwqmaxWn3Nq7r2TpThl7pszjAq7w7a+wyg+sM9etbXWNkHRUcDzAc4CnypM6PrdmieCuHN1rXC2QZT85QotWeIOvyZoTxTpqs3Z/RFSMzSRlGwCts+IhW8RCWuXd13LoLWnTXuKcYkOiZdPHnAjhTS5gvCZ7S3sUs6bxB2EXTq1eCJhBXgOJdkP7+TifGo0nJTRd2JcLiH4Lb6GAaNlNryROQNYCNkfKIu1Xvd/EMqkrq436axKCL6pPw7vWoksrjP1O79psBRuKU1ZS4QjRUn5EjFwxmMACSbMZv09kFM/ID7gjf49k0/qhd2XJca01nAS70BHBZ6QTc4NqF33Gp0IClPC2C0IG5lEyMUiCsjLiDArJBElgZPA+msxRmwfCrKTtTS8DYekZaccw6qpCfKVIipP07IIkQm46HXIBdJwv/uxvayE8L5LQwtOqzexkq2sSwlwmujS2su4NiA2dNBJcqBYZkDPh8KqKOsnsbfiM8sRbJAZlgwqK4c7YbBJeWA3pof+ejzpuHnXrjmia5EQZIpzctbdJLn2I3JD0HV8ZNsn1E2Zgrm9a0jXVAl5R031p1kO2XlR9v+fDG0FwPKpUqPZklJ6IqbiJbUQb77sLdFCfuROu1ctiOTPcJJ//4KKSgV7Aw6sdWi9gT5nfxtLNDY4IoIgA+7Zbn2mPStSdeD6Xd/UQ0/VwTg4Ew0ydaprmXhU0rM+VTHYDo1ahMnG0qboXRfu2+KDRB7KPDIE55OjS9R7cxjYm3Rd7sZlMe8DVUVfOoHf7ao7CK0dvLM5LndtP7rOouFqA3QN/7b6Igv4birVRfmriHOFmcA2KGVDCwhsx+9c0V46qL+AcrANSrXo30/XzPqDbwKwlCoGrBllzhUJefevMyevfRzCFGJSavmzU3b0UQxWxyqsFeY9SYdngRC9i44QpeJuIUjytQL+Duo6SY19Py9S9eRe0AA+7dwrBCDYDyNtNtPP4pBdyxd2jKEs7OIt9j8YxxnjKuSUQStnwfbG5aHShcHcSOGCPfaeEvFXFJVBqxgU5p5yrFzQ09g5DqNHWUXlaj1TJXIDKl0wb61qZxFlHd1m2wNjoo5dS+oOlJGqiUL3w8KoUpdjCJWZInCorVS/E3vx3wEWsllEFzPAvsdcIHUxfbf1oyhRhdew2BXrdPHACer3O9n6SBinu6MNjADE7YwXWXa9igqrU8CO4yHJSu20CiE2NMCxrX3OdGifeuHnBEQsZDnpwV1b3FS58G1M7/qYO+RRfY45eUKBpbKM0UdzFYsVqI8ThMWPoAwrvtS9GCXzxBw8fy/uUELxX969hT6qbO/tWyOWFzc2x0cSnwTapHuJ2PAWeQEf9jpLpg/P0yry5mxBuU9fMt5WTC98nkYE7guU9RdgLqdRmYby73YSk6xu+ojyCMrJcZW/jvqqU5c3mzVuZBWTBc6JeIoC8CdURcaKVpr7OBhFMuPc0sBYyyrpDJ+iZfAVpUYUDcqM3IYexq8kS8S21EBx0zkzQArYxouIGjf4defliKXpEDIVc8n6o5y6AfojUZnAvGOQwOK8Qpz3zNukmzl5MwGoaA33ceA4DBzexBivPJ1gtMR217x54rfviM0rI1069uHfmAHiju31JI8JFCmp7G+6sXRLVE6ssevUmhKdYMZ+Q/n3bUNEu+hdW3UGVyeTeuKuYLEIHNWwY5CIJdJRptyQoqlyDKX5D3vJu1cuD0r2xlYNcylpdAZMoQdJIECV/dZC+YyUwXJ/bRQvIQUjrvTecZjUBP+lxeOj2SHC8h0Ivt4O9aa+Iefq3C6/6PhAVNoOOMRwFI1nGMciuEN7Mh4SmQxjdhjMZsGSCuvNQ+6Zva/puUvWZJuA1FoDPF4Q5srUMd2swmsHhnG28tzZnqEjrI9wxwyxXCGjC6Z6AY3QhlN4gqP1czC/w5nkh2h1detGgLeKDph6Em1HMALCUpNw5eN973ehWNx5GvIzVNWk+kHFL9NhZL2K22pxUjRDK8Nw9OhvRS8UAtma6evNHnr6tR+JEnUe6BBbj9h3z6qatCWiNDLUPa1w6DMrEgVsSu8I5pr44KOITQYoV1jMl2G5vOBTumK6q6u3ue4+3wtyyVuas0DkhepXhQJ1FOg0pZuZo6mGA5hGBhBlS+Lt46V6rWztzCxc/YOG4eCtw6DLcmj6EQuNwx1ED7Ll8/o1q8AaV+z3dJXyPnhFXkGF39T0t1SeDcdVZgQiNeI0jJPINOFsKQNGecqN38rQ/S9pXZzNgU/6GdVEYU43kbG/jmmWLDnbusNkVWKGWsc2/wLdXhhkiVaQG2o1UUDcCHZx91eEuDClDfQUemqD283mjxa0XCe8+PyldnTVmcd/0zQDmnL7b8kvqiSdzdmzrtIHnIFBf10gBeplZhBkPOjxqxFVru3CI3fUdaURTWBKu2wMCLJ6LiBQo50oexm2pzpHJ48WQzzN0usc1bCDeU4M0+YoiTlZY/OJ35xyY0kkwotMnbX7VOVU+aGq43ywu4Ul2K+/kILm2RFW7/X4J2XoWMwikRApTu2imMmbrLJU973crGsH6zckaHcO8EbjaPRHQEsEC9LUDZSYmvOd5uj8C+XLNQhiaaqhMPmBlecyP8+2XRytBOlMfemS8J9d00qiG21GPNZF4qRY8QxcDcuHcL5MT3+VzrM9EvamSMk0Fr8moVO4mBKeB59tCj9/25cx2i23FssJepQP7eGjROKGqBU2OufLGLu26iYGTmyYTwknNpdh7b5qGdRR2wWsoFFi3lhRXHuNrdj/kEs/6BwvYL28xCWGEpPz5MEcY6SEZD7uotmlOFBCpyZCH9mIdXeUezcUxlF688Nq5RinDhrKyy/zRSb3+5ew+YbV8ptCjkpPwQTtVkow2oY9I3WzJW1EtCjKjA3qnKnAfM+FBbEXcoubLIuw+fNjSqldxfRPvkn/G5nDo6sYkvelF6Gts90aG2kS1b/GgNO2SzK5dtnr/npEnVFEDRj31ZE+lN/bSO3mobhbNQrXqRmOc1dIbV+3e8vL9mrEfo7VOPoMVD1V5vev7KYea02uBi8bag68Bfslv0UjbI9gpSk6ZEDXpQN64SkTdkXE5CYpHQN5A8vnz3zHmbXLFpGMkhhSS0FLuDhrgrWJww+tZy662HsNAeFfiq9jjdid1T9eNFdd2esxt2gUf7ZYT5805Hz1rgI+4i221lnInpTlNxIkTvUZeHAD9+SgeMwgy/BpaU3VQtCzNIBs9OarMmhuaFQXRhQRY5eP1IBYkOScejEJ6JwJOmwsJapjXTAYI9HzRyC6yfLfFY0ykSwwJmfK0teeTcBLP9IQ0R+0369eEdMS85XhOdmagW+NstVDdUVonS8QB3URUd18RqLt3dz5W/DVXNudK0709a1EhYYBy+hhNMDbeDXAzUWOAd4GlDM54L6Zp56eBYcjY9eX7SWZWg1/OJRjjIfOj3kwCzZVGupdLXVFUsRYnGMm5Uo/xfg7OttgPx5nakznjjKHf1qplK4CAt/aAPLWnHvznT9r58qXU5/+PDEuEDP2mfS5GSux6qyN5Z2w7IFoI6jQNbextyT5ZCyx2jh5iwfLZA5HhW++1SBQaD6mXtDJvG5KYMnMzr8kH3KklG24Q7iO8GTQ9O4dBe5cgYGEDddLU6QqhgUn3nIn9poENKebejh4rXHbN3L0/0QtBtE0iVzvHXtNTRg+tsOuaAIEztLy2qLNhNjM5CU+gV0cJ9P4muK3wTxTXYeqGZcfO42qa3GPJ1sxQAvxIoWlnDF9ThZnPDXEIxYo1rUVqPX7BrmSvVP4QXTgus9T+/1q5kx1XjSgMwO/SW26CARtwdtgGzNCUGTyAFEUMBcbMuBgKKe+ecvu2ks3d5QHgnAU6nL9K+saNikYUs8heG1vGIlk4JYlps/RpfU/PU3eNG18bLB0YaZqfTuoI0z541EGkVVEuG5Fd5rwMxJsKh8SRyTfBH9xOHerQuTefSLco1TVmN+LjJdS5Mt2fa2/YBI4JL1uRbK/J1h0QoDuhORp4lOlPs7iqhwbg193QeS6vW8A9DtEINc6VBdu7zpL82Vj3aL9S+z2t91wTn3iQWhQNFG5kjwaa1KhD9aEEN0kk8WtGfSQvIxmeLbZylEUaEEEkP2Q3uDx82wOsc06pJ7OHMdPkiNbSWbRCF9l5zbgYJKAqgCevvZwNbWtog2ZOFPNYhwxJsVU23VFYB6MDKjZp7BNJFIBJ10lJmTsKM+Ius6FLk+Hnk3+Gn624vG2y2TK7QfhkWVOdTLtqpCq2GFt/8p65Wwq8RoB5CILFbgeOInloFy1RbSdoUQ08Q90YMu6TMWAI3fi5p1nByFhusFONxnpIctu+s5QWD97RGtx6vsZxK+qgM3lq3lLZGF0ugf3caurS3vEE9oOmpKGMrLFEN3wQ7yYZi0m9daLWp4uz6C5ZtZ9Mk8/llXt23GSNPSNUzux1IynhcjNQIK/WqySYTM/SU9MFYndx1HUsFbe86+PKmHWhZao+G+ab55gk2CkdGECRBHyvduXGU64kR6tVfTrZsA+UUt+8zrfnfboAeExWxfLcIhtF9sI97w9I4cXhmk6taFEAh9LwT/TRwSePEZPnshac9GaKFwNLIc9nzcbGiaFfZIyAbEKBcnh/LjIn0h4b2z+GwRP3DdkTpPGwljSvKCWotPbJVaZzyT41pu0uc9HfqOYhCvYBuVNlFe3kJxOtj7v44QlRouDi+DgbJQlYq92QHI9a6vm5JnTubVOHOTW05s5vdOhprpIYsUZHFbxYsXHa4SCq+nB/vlNSfw9XY8x5UL90Cx4Q2SB2W4+WOKofW7aYJUn6+PHxkhF+yjW/wrxeOMD/5hC8OYFmJEXrGH5BFzBM/ni7aL/s4M8fH32ck/pvT+FZDtlPpOBbU+jfmsIbLfgt+4+/82Yo/oqbGsEZfWs9KMxezONHm7ewzGv4r2LzfigO07QpkxdK8eNFVjbf74SvZr7YtS/qgTT0O/Px9z+FTk9k11IAAA== -->
