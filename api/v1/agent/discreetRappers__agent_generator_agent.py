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
    "version": "1.0.0",
    "display_name": "AgentGenerator",
    "description": "Auto-generates new RAPP agents from configurations and specifications.",
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
