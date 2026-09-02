---
name: "rar-discreetrappers-agent-generator"
description: "Generates complete agent configurations from natural language descriptions with optional Copilot Studio deployment."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/agent_generator_agent", "rar_sha256": "11b58f135dce6bd67bf595c7d5a31576e695a768bf6dba4d46709427e209e61c", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "agent_generator_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@discreetrappers/agent-generator:9cc36ad11774cf6a0057b93e2ce40ac2ac86de13cb5dd1b41c14e5749c9803fe", "kind": "skill"}, "version": "1.0.1", "author": "Bill Whalen", "tags": ["pipeline", "generator", "scaffolding", "auto-generate"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@discreetRappers/agent_generator_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `agent_generator_agent.py` is
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
