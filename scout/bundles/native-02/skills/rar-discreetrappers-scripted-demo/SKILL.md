---
name: "rar-discreetrappers-scripted-demo"
description: "Executes scripted demonstrations from JSON files stored in Azure File Storage. This agent reads pre-written demo scenarios and returns the appropriate canned responses based on user input matching. Perfect for consistent, repeatable product demonstrations."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/scripted_demo_agent", "rar_sha256": "04e240a1092a8e71d446ab7662792b69cbe54e48d78fa46ec76b4ff19cb78df4", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Bill Whalen", "tags": ["productivity", "demos", "scripted", "interactive", "sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@discreetRappers/scripted_demo_agent`. The original RAPP
agent is preserved byte-for-byte in `scripted_demo_agent.py` and in the RCI capsule.

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

Executes scripted demonstrations from JSON files stored in Azure File Storage. This agent reads pre-written demo scenarios and returns the appropriate canned responses based on user input matching. Perfect for consistent, repeatable product demonstrations.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "The action to perform. Options: 'list_demos' (list available demo files), 'load_demo' (load a demo and show its structure), 'respond' (match user input and return canned response)",
      "enum": [
        "list_demos",
        "load_demo",
        "respond"
      ],
      "type": "string"
    },
    "demo_name": {
      "description": "The name of the demo JSON file to load from Azure File Storage (without .json extension). Example: 'Bot_342_Morning_Greeting_Demo'",
      "type": "string"
    },
    "user_guid": {
      "description": "Optional user GUID for context (used in demo responses that reference user data)",
      "type": "string"
    },
    "user_input": {
      "description": "The user's message to match against the conversation flow and return the appropriate canned response",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scripted_demo_agent.py` and embedded as the fenced Python below (sha256 04e240a1092a8e71…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scripted_demo_agent.py` first:

```bash
python3 scripted_demo_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scripted_demo_agent.py   # or on stdin
python3 scripted_demo_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@discreetRappers/scripted_demo_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/scripted_demo_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@discreetRappers/scripted_demo_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
import json

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/scripted_demo_agent",
    "version": "1.0.1",
    "display_name": "ScriptedDemo",
    "description": "Plays back scripted demo conversations from JSON files in storage, simulating agent responses for live demonstrations.",
    "author": "Bill Whalen",
    "tags": ["productivity", "demos", "scripted", "interactive", "sales"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════

import logging
import re
import sys
import importlib.util
import requests
from agents.basic_agent import BasicAgent
from utils.storage_factory import get_storage_manager

# Optional: Try to import AgentManager if it exists (for local agent lookup)
try:
    from utils.agent_manager import AgentManager
    AGENT_MANAGER_AVAILABLE = True
except ImportError:
    AGENT_MANAGER_AVAILABLE = False
    logging.debug("AgentManager not available - will skip local agent lookup")


class ScriptedDemoAgent(BasicAgent):
    """
    Executes scripted demonstrations from JSON files with support for:
    - Canned responses
    - Rich content blocks (charts, tables, code, etc.)
    - Real-time agent orchestration with static/dynamic parameters
    - Automatic agent loading from GitHub repository
    - Rich data display with display_result field
    - Proper agent name tracking and display
    """

    # GitHub repository configuration for remote agent loading
    # Using the live AI-Agent-Templates repository with 65+ production agents
    GITHUB_REPO = "kody-w/AI-Agent-Templates"
    GITHUB_BRANCH = "main"
    GITHUB_RAW_BASE = f"https://raw.githubusercontent.com/{GITHUB_REPO}/{GITHUB_BRANCH}"
    GITHUB_API_BASE = f"https://api.github.com/repos/{GITHUB_REPO}"

    def __init__(self):
        self.name = 'ScriptedDemo'
        self.metadata = {
            "name": self.name,
            "description": "Executes scripted demonstrations from JSON files stored in Azure File Storage. This agent reads pre-written demo scenarios and returns the appropriate canned responses based on user input matching. Perfect for consistent, repeatable product demonstrations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "demo_name": {
                        "type": "string",
                        "description": "The name of the demo JSON file to load from Azure File Storage (without .json extension). Example: 'Bot_342_Morning_Greeting_Demo'"
                    },
                    "user_input": {
                        "type": "string",
                        "description": "The user's message to match against the conversation flow and return the appropriate canned response"
                    },
                    "action": {
                        "type": "string",
                        "description": "The action to perform. Options: 'list_demos' (list available demo files), 'load_demo' (load a demo and show its structure), 'respond' (match user input and return canned response)",
                        "enum": ["list_demos", "load_demo", "respond"]
                    },
                    "user_guid": {
                        "type": "string",
                        "description": "Optional user GUID for context (used in demo responses that reference user data)"
                    }
                },
                "required": ["action"]
            }
        }
        self.storage_manager = get_storage_manager()
        self.demo_directory = "demos"
        self.loaded_demo_cache = {}  # Cache loaded demos

        # Optional: Initialize AgentManager if available (for local agent lookup)
        if AGENT_MANAGER_AVAILABLE:
            self.agent_manager = AgentManager()
        else:
            self.agent_manager = None

        self.remote_agent_cache = {}  # Cache for dynamically loaded remote agents
        self._agent_manifest_cache = None  # Optional manifest for faster agent discovery

        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        """
        Main entry point for the agent. Routes to appropriate handler based on action.
        """
        action = kwargs.get('action', 'list_demos')
        demo_name = kwargs.get('demo_name', '')
        user_input = kwargs.get('user_input', '')
        # Uses intentionally invalid UUID - see function_app.py DEFAULT_USER_GUID for rationale
        user_guid = kwargs.get('user_guid', 'c0p110t0-aaaa-bbbb-cccc-123456789abc')

        try:
            if action == 'list_demos':
                return self.list_available_demos()
            elif action == 'load_demo':
                if not demo_name:
                    return self.format_error_response("demo_name is required for load_demo action")
                return self.load_demo(demo_name)
            elif action == 'respond':
                if not demo_name or not user_input:
                    return self.format_error_response("demo_name and user_input are required for respond action")
                return self.get_response_for_user_input(demo_name, user_input, user_guid)
            else:
                return self.format_error_response(f"Unknown action: {action}")
        except Exception as e:
            logging.error(f"Error in ScriptedDemoAgent: {str(e)}")
            return self.format_error_response(f"Agent error: {str(e)}")

    def list_available_demos(self):
        """
        List all available demo JSON files in the Azure File Storage demos directory.
        Falls back to local demos directory if Azure Storage unavailable.
        """
        try:
            demo_files = []
            source = "Azure File Storage"
            
            # Ensure the demos directory exists
            self.storage_manager.ensure_directory_exists(self.demo_directory)

            # List all files in the demos directory from Azure
            files = self.storage_manager.list_files(self.demo_directory)

            for file_info in files:
                if hasattr(file_info, 'name') and file_info.name.endswith('.json'):
                    demo_name = file_info.name.replace('.json', '')
                    demo_files.append(demo_name)

            # Fallback to local file system if no demos found in Azure
            if not demo_files:
                try:
                    import os
                    local_paths = [
                        self.demo_directory,
                        os.path.join(os.path.dirname(__file__), '..', self.demo_directory),
                        os.path.join(os.getcwd(), self.demo_directory),
                    ]
                    for local_path in local_paths:
                        if os.path.isdir(local_path):
                            logging.info(f"Listing demos from local directory: {local_path}")
                            for filename in os.listdir(local_path):
                                if filename.endswith('.json'):
                                    demo_name = filename.replace('.json', '')
                                    if demo_name not in demo_files:
                                        demo_files.append(demo_name)
                            if demo_files:
                                source = f"local directory ({local_path})"
                                break
                except Exception as e:
                    logging.warning(f"Local directory fallback failed: {str(e)}")

            if not demo_files:
                response = {
                    "status": "success",
                    "message": "No demo files found",
                    "available_demos": [],
                    "instructions": "Upload demo JSON files to the 'demos' directory in Azure File Storage or place them locally",
                    "demo_directory": self.demo_directory
                }
            else:
                response = {
                    "status": "success",
                    "message": f"Found {len(demo_files)} demo file(s)",
                    "source": source,
                    "available_demos": sorted(demo_files),
                    "demo_directory": self.demo_directory,
                    "next_steps": "Use 'load_demo' action to view demo structure, or 'respond' action to get canned responses"
                }

            return json.dumps(response, indent=2)
        except Exception as e:
            logging.error(f"Error listing demos: {str(e)}")
            return self.format_error_response(f"Failed to list demos: {str(e)}")

    def load_demo(self, demo_name):
        """
        Load a demo JSON file from Azure File Storage and return its structure.
        """
        try:
            demo_data = self._read_demo_file(demo_name)

            if not demo_data:
                return self.format_error_response(f"Demo file '{demo_name}.json' not found or empty")

            # Extract conversation flow summary
            conversation_flow = demo_data.get('conversation_flow', [])
            flow_summary = []

            for step in conversation_flow:
                step_info = {
                    "step_number": step.get('step_number', 0),
                    "description": step.get('description', ''),
                    "user_message": step.get('user_message', ''),
                    "has_response": 'agent_response' in step
                }
                flow_summary.append(step_info)

            response = {
                "status": "success",
                "demo_name": demo_data.get('demo_name', demo_name),
                "description": demo_data.get('description', ''),
                "trigger_phrases": demo_data.get('trigger_phrases', []),
                "total_steps": len(conversation_flow),
                "conversation_flow": flow_summary,
                "instructions": "Use 'respond' action with user_input matching a step's user_message to get the canned agent_response"
            }

            return json.dumps(response, indent=2)
        except json.JSONDecodeError as e:
            logging.error(f"Invalid JSON in demo file: {str(e)}")
            return self.format_error_response(f"Invalid JSON in demo file: {str(e)}")
        except Exception as e:
            logging.error(f"Error loading demo: {str(e)}")
            return self.format_error_response(f"Failed to load demo: {str(e)}")

    def get_response_for_user_input(self, demo_name, user_input, user_guid):
        """
        Match user input against conversation flow and return the appropriate canned response.
        Uses fuzzy matching to find the best matching step.
        """
        try:
            demo_data = self._read_demo_file(demo_name)

            if not demo_data:
                return self.format_error_response(f"Demo file '{demo_name}.json' not found")

            conversation_flow = demo_data.get('conversation_flow', [])

            if not conversation_flow:
                return self.format_error_response("No conversation flow found in demo script")

            # Normalize user input for matching
            user_input_lower = user_input.lower().strip()

            # Try exact match first
            for step in conversation_flow:
                step_message = step.get('user_message', '').lower().strip()
                if step_message == user_input_lower:
                    return self._format_agent_response(step, demo_data, user_guid)

            # Try fuzzy match (contains)
            best_match = None
            best_match_score = 0

            for step in conversation_flow:
                step_message = step.get('user_message', '').lower().strip()

                # Calculate simple similarity score
                score = 0
                user_words = set(user_input_lower.split())
                step_words = set(step_message.split())

                # Count matching words
                matching_words = user_words.intersection(step_words)
                score = len(matching_words)

                # Bonus for trigger phrase match
                trigger_phrases = demo_data.get('trigger_phrases', [])
                for trigger in trigger_phrases:
                    if trigger.lower() in user_input_lower:
                        score += 10

                if score > best_match_score:
                    best_match_score = score
                    best_match = step

            # If we found a reasonable match (at least 2 matching words or trigger phrase)
            if best_match and best_match_score >= 2:
                return self._format_agent_response(best_match, demo_data, user_guid)

            # No match found - return helpful error
            available_steps = [s.get('user_message', '') for s in conversation_flow]
            return self.format_error_response(
                f"No matching step found for input: '{user_input}'. Available user messages: {available_steps}"
            )

        except json.JSONDecodeError as e:
            logging.error(f"Invalid JSON in demo file: {str(e)}")
            return self.format_error_response(f"Invalid JSON in demo file: {str(e)}")
        except Exception as e:
            logging.error(f"Error getting response: {str(e)}")
            return self.format_error_response(f"Failed to get response: {str(e)}")

    def _read_demo_file(self, demo_name):
        """
        Read and parse a demo file from Azure File Storage with caching.
        Falls back to local demos directory if Azure Storage unavailable.
        """
        # Check cache first
        if demo_name in self.loaded_demo_cache:
            return self.loaded_demo_cache[demo_name]

        file_name = f"{demo_name}.json"
        demo_content = None
        
        # Try Azure Storage first
        demo_content = self.storage_manager.read_file(self.demo_directory, file_name)

        # Fallback to local file system if Azure Storage unavailable
        if not demo_content:
            try:
                import os
                # Check multiple potential local paths
                local_paths = [
                    os.path.join(self.demo_directory, file_name),
                    os.path.join(os.path.dirname(__file__), '..', self.demo_directory, file_name),
                    os.path.join(os.getcwd(), self.demo_directory, file_name),
                ]
                for local_path in local_paths:
                    if os.path.exists(local_path):
                        logging.info(f"Loading demo from local file: {local_path}")
                        with open(local_path, 'r', encoding='utf-8') as f:
                            demo_content = f.read()
                        break
            except Exception as e:
                logging.warning(f"Local file fallback failed: {str(e)}")

        if not demo_content:
            return None

        # Parse JSON
        demo_data = json.loads(demo_content)

        # Cache it
        self.loaded_demo_cache[demo_name] = demo_data

        return demo_data

    def _format_agent_response(self, step, demo_data, user_guid):
        """
        Format the agent response from a matched step.
        Supports:
        - Legacy string responses with template replacement
        - Enhanced array responses with content blocks
        - Agent call execution with static and dynamic parameters
        - Rich data display with display_result field
        """
        agent_response = step.get('agent_response', '')

        if not agent_response:
            return self.format_error_response("No agent_response found for this step")

        # Get user_input for context
        user_input = step.get('user_message', '')

        # Legacy format: simple string response
        if isinstance(agent_response, str):
            return self._apply_template_variables(agent_response, demo_data, user_guid)

        # Enhanced format: array of content blocks
        if isinstance(agent_response, list):
            result_parts = []
            for content_block in agent_response:
                processed = self._process_agent_response_content(
                    content_block, demo_data, user_guid, user_input
                )
                if processed:
                    result_parts.append(processed)

            # Join all parts with newlines
            return '\n\n'.join(result_parts)

        # Fallback: treat as string
        return str(agent_response)

    def _apply_template_variables(self, text, demo_data, user_guid):
        """Apply template variable replacement to text."""
        formatted_text = text
        formatted_text = formatted_text.replace('{user_guid}', user_guid)
        formatted_text = formatted_text.replace('{demo_name}', demo_data.get('demo_name', ''))
        formatted_text = formatted_text.replace('{demo_description}', demo_data.get('description', ''))
        return formatted_text

    def _process_agent_response_content(self, content_block, demo_data, user_guid, user_input):
        """
        Process a single content block from enhanced agent_response.
        Handles regular content blocks and agent_call type blocks with proper agent name extraction.
        
        **KEY FIX**: Now properly extracts agent name from the 'agent' field and displays it correctly.
        """
        if not isinstance(content_block, dict):
            return str(content_block)

        content_type = content_block.get('type', 'text')

        # Handle agent_call type - execute another agent OR display rich result
        if content_type == 'agent_call':
            return self._process_agent_call_block(content_block, user_guid, user_input, demo_data)

        # For text content blocks, extract just the content string and apply template variables
        if content_type == 'text':
            text_content = content_block.get('content', '')
            return self._apply_template_variables(text_content, demo_data, user_guid)

        # For other content types (chart, table, etc.), return as JSON
        # The M365 Copilot simulator will render these appropriately
        return json.dumps(content_block, indent=2)

    def _process_agent_call_block(self, agent_call_config, user_guid, user_input, demo_data):
        """
        Process an agent_call content block with proper agent name extraction and rich data support.
        
        **KEY FIX**: This method now:
        1. Extracts the correct agent name from the 'agent' field
        2. Checks for 'display_result' first (for demos with pre-rendered data)
        3. Falls back to actual agent execution if no display_result
        4. Shows the correct agent name in the response badge
        
        Args:
            agent_call_config: The agent_call content block from JSON
            user_guid: User GUID for context
            user_input: User's message for dynamic parameter extraction
            demo_data: Full demo data for additional context
            
        Returns:
            Formatted response with agent name badge
        """
        # **CRITICAL FIX**: Extract the correct agent name from the config
        agent_name = agent_call_config.get('agent', 'UnknownAgent')
        description = agent_call_config.get('description', f'Calling {agent_name}')
        
        logging.info(f"Processing agent call: {agent_name} - {description}")
        
        # Check if there's a display_result (pre-rendered data for demos)
        if 'display_result' in agent_call_config:
            display_result = agent_call_config['display_result']
            
            # Build response with rich data
            response_parts = []
            
            # Add intro text if provided
            intro_text = display_result.get('intro_text', '')
            if intro_text:
                response_parts.append(intro_text)
            
            # Format the rich data based on its type
            data = display_result.get('data', {})
            data_format = display_result.get('format', 'generic')
            
            formatted_data = self._format_display_result(data, data_format)
            if formatted_data:
                response_parts.append(formatted_data)
            
            # **CRITICAL FIX**: Add agent badge with CORRECT agent name
            response_parts.append(f"🔧 Agent Call: {agent_name}")
            
            return '\n\n'.join(response_parts)
        
        else:
            # No display_result - execute actual agent call
            result = self._execute_agent_call(agent_call_config, user_guid, user_input, demo_data)
            
            # **CRITICAL FIX**: Add agent badge with CORRECT agent name
            return f"{result}\n\n🔧 Agent Call: {agent_name}"

    def _format_display_result(self, data, data_format):
        """
        Format rich data for display based on format type.
        
        Supported formats:
        - priority_dashboard: Morning priorities with critical items
        - pipeline_breakdown: Sector analysis with metrics
        - at_risk_deals_grid: Deal cards with risk factors
        - recovery_playbook: Action plans and strategies
        - email_draft: Complete email with metadata
        - presentation_outline: Slide-by-slide breakdown
        - generic: Fallback JSON formatting
        
        Args:
            data: The data dict to format
            data_format: The format type string
            
        Returns:
            Formatted string for display
        """
        if data_format == 'priority_dashboard':
            return self._format_priority_dashboard(data)
        elif data_format == 'pipeline_breakdown':
            return self._format_pipeline_breakdown(data)
        elif data_format == 'at_risk_deals_grid':
            return self._format_deals_grid(data)
        elif data_format == 'recovery_playbook':
            return self._format_recovery_playbook(data)
        elif data_format == 'email_draft':
            return self._format_email_draft(data)
        elif data_format == 'presentation_outline':
            return self._format_presentation_outline(data)
        else:
            # Generic JSON formatting for unknown types
            return json.dumps(data, indent=2)

    def _format_priority_dashboard(self, data):
        """Format morning priority dashboard with critical items and overnight changes."""
        output = []
        
        # Critical items
        critical_items = data.get('critical_items', [])
        if critical_items:
            output.append("**🎯 Today's Priorities:**\n")
            for item in critical_items:
                output.append(f"{item.get('icon', '•')} **{item.get('title', 'Item')}**")
                output.append(f"   {item.get('value', '')} - {item.get('status', '')}")
                if 'description' in item:
                    output.append(f"   {item['description']}")
                output.append("")
        
        # Overnight changes
        overnight_changes = data.get('overnight_changes', [])
        if overnight_changes:
            output.append("\n**🌙 Overnight Changes:**")
            for change in overnight_changes:
                output.append(f"  {change}")
        
        # Pipeline summary
        pipeline_summary = data.get('pipeline_summary', {})
        if pipeline_summary:
            output.append(f"\n**📊 Pipeline Summary:**")
            for key, value in pipeline_summary.items():
                label = key.replace('_', ' ').title()
                output.append(f"  {label}: {value}")
        
        return '\n'.join(output)

    def _format_pipeline_breakdown(self, data):
        """Format pipeline breakdown by sector with trends and metrics."""
        output = []
        
        sectors = data.get('sectors', [])
        for sector in sectors:
            output.append(f"\n{'='*60}")
            output.append(f"**{sector.get('name', 'Sector')}**")
            output.append(f"Total Value: {sector.get('total_value', 'N/A')} | Deals: {sector.get('deal_count', 0)} | Win Rate: {sector.get('win_rate', 'N/A')}")
            output.append(f"Avg Deal Size: {sector.get('average_deal_size', 'N/A')} | Trend: {sector.get('trend', 'N/A')}")
            
            top_deals = sector.get('top_deals', [])
            if top_deals:
                output.append(f"\nTop Deals:")
                for deal in top_deals:
                    output.append(f"  • {deal}")
            
            status = sector.get('status', '')
            if status:
                output.append(f"\n**Status:** {status}")
        
        # Pipeline health metrics
        health_metrics = data.get('pipeline_health_metrics', {})
        if health_metrics:
            output.append(f"\n{'='*60}")
            output.append(f"\n**Pipeline Health Metrics:**")
            for key, value in health_metrics.items():
                label = key.replace('_', ' ').title()
                output.append(f"  {label}: {value}")
        
        # Competitive landscape
        competitive = data.get('competitive_landscape', {})
        if competitive:
            output.append(f"\n**Competitive Landscape:**")
            if 'primary_competitors' in competitive:
                output.append(f"  Primary Competitors: {', '.join(competitive['primary_competitors'])}")
            if 'your_differentiators' in competitive:
                output.append(f"  Your Differentiators: {', '.join(competitive['your_differentiators'])}")
            if 'win_loss_trend' in competitive:
                output.append(f"  Win/Loss Trend: {competitive['win_loss_trend']}")
        
        return '\n'.join(output)

    def _format_deals_grid(self, data):
        """Format at-risk deals into a readable display with risk factors and links."""
        output = []
        
        deals = data.get('deals', [])
        for deal in deals:
            output.append(f"\n{'='*60}")
            output.append(f"**{deal.get('title', 'Deal')}** - {deal.get('company', 'Company')}")
            output.append(f"Value: {deal.get('value', 'N/A')} | Close: {deal.get('close_date', 'N/A')} | Risk: {deal.get('risk_level', 'N/A')} ({deal.get('risk_score', 'N/A')})")
            
            # Risk factors
            risk_factors = deal.get('risk_factors', [])
            if risk_factors:
                output.append(f"\n**Key Risk Factors:**")
                for factor in risk_factors:
                    output.append(f"  ⚠️ {factor}")
            
            # Key stakeholders
            stakeholders = deal.get('key_stakeholders', [])
            if stakeholders:
                output.append(f"\n**Key Stakeholders:**")
                for stakeholder in stakeholders:
                    output.append(f"  • {stakeholder}")
            
            # Links
            links = []
            if 'dynamics_link' in deal:
                links.append(f"[View in Dynamics 365]({deal['dynamics_link']})")
            if 'teams_link' in deal:
                links.append(f"[Open in Teams]({deal['teams_link']})")
            
            if links:
                output.append(f"\n📊 {' | '.join(links)}")
            
            # Additional metrics
            if 'last_activity' in deal:
                output.append(f"\nLast Activity: {deal['last_activity']}")
            if 'win_probability' in deal:
                output.append(f"Win Probability: {deal['win_probability']}")
            if 'competitive_threat' in deal:
                output.append(f"Competitive Threat: {deal['competitive_threat']}")
        
        # Summary statistics
        summary_stats = data.get('summary_stats', {})
        if summary_stats:
            output.append(f"\n{'='*60}")
            output.append(f"\n**Summary Statistics:**")
            for key, value in summary_stats.items():
                label = key.replace('_', ' ').title()
                output.append(f"{label}: {value}")
        
        return '\n'.join(output)

    def _format_recovery_playbook(self, data):
        """Format comprehensive recovery playbook with action plans and strategies."""
        output = []
        
        # Deal overview
        deal_overview = data.get('deal_overview', {})
        if deal_overview:
            output.append("**Deal Overview:**")
            for key, value in deal_overview.items():
                label = key.replace('_', ' ').title()
                output.append(f"  {label}: {value}")
            output.append("")
        
        # Immediate actions
        immediate_actions = data.get('immediate_actions', {})
        if immediate_actions:
            output.append(f"\n**{immediate_actions.get('title', 'Immediate Actions')}**")
            output.append(f"Priority: {immediate_actions.get('priority', 'HIGH')}\n")
            for item in immediate_actions.get('items', []):
                output.append(f"• **{item.get('action', 'Action')}**")
                output.append(f"  Owner: {item.get('owner', 'N/A')} | Timeline: {item.get('timeline', 'N/A')}")
                output.append(f"  {item.get('details', '')}")
                if item.get('template_available'):
                    output.append(f"  ✅ Template Available")
                output.append("")
        
        # Week 1 strategy
        week_1 = data.get('week_1_strategy', {})
        if week_1:
            output.append(f"\n**{week_1.get('title', 'Week 1 Strategy')}**")
            for item in week_1.get('items', []):
                output.append(f"• **{item.get('action', 'Action')}**")
                output.append(f"  {item.get('details', '')}")
                if 'success_criteria' in item:
                    output.append(f"  ✓ Success: {item['success_criteria']}")
                output.append("")
        
        # Weeks 2-3 strategy
        weeks_2_3 = data.get('weeks_2_3_strategy', {})
        if weeks_2_3:
            output.append(f"\n**{weeks_2_3.get('title', 'Weeks 2-3 Strategy')}**")
            for item in weeks_2_3.get('items', []):
                output.append(f"• **{item.get('action', 'Action')}**")
                output.append(f"  {item.get('details', '')}")
                if 'deliverable' in item:
                    output.append(f"  📋 Deliverable: {item['deliverable']}")
                output.append("")
        
        # Competitive strategy
        competitive = data.get('competitive_strategy', {})
        if competitive:
            output.append(f"\n**{competitive.get('title', 'Competitive Strategy')}**")
            output.append(f"Threat Level: {competitive.get('threat_level', 'Unknown')}\n")
            
            if 'their_strengths' in competitive:
                output.append(f"Their Strengths:")
                for strength in competitive['their_strengths']:
                    output.append(f"  • {strength}")
            
            if 'your_advantages' in competitive:
                output.append(f"\nYour Advantages:")
                for advantage in competitive['your_advantages']:
                    output.append(f"  ✓ {advantage}")
            
            if 'talking_points' in competitive:
                output.append(f"\nKey Talking Points:")
                for point in competitive['talking_points']:
                    output.append(f"  • {point}")
            
            if 'trap_setting' in competitive:
                output.append(f"\n💡 Trap Setting: {competitive['trap_setting']}")
            output.append("")
        
        # Stakeholder engagement
        stakeholder_plan = data.get('stakeholder_engagement_plan', {})
        if stakeholder_plan:
            output.append(f"\n**Stakeholder Engagement Plan:**\n")
            for stakeholder_key, stakeholder_data in stakeholder_plan.items():
                if isinstance(stakeholder_data, dict):
                    output.append(f"**{stakeholder_data.get('role', stakeholder_key)}**")
                    output.append(f"  Status: {stakeholder_data.get('status', 'N/A')}")
                    output.append(f"  Priority: {stakeholder_data.get('priority', 'N/A')}")
                    output.append(f"  Approach: {stakeholder_data.get('approach', 'N/A')}")
                    
                    actions = stakeholder_data.get('actions', [])
                    if actions:
                        output.append(f"  Actions:")
                        for action in actions:
                            output.append(f"    • {action}")
                    
                    win_signals = stakeholder_data.get('win_signals', '')
                    if win_signals:
                        output.append(f"  ✓ Win Signals: {win_signals}")
                    output.append("")
        
        # Probability improvement
        probability = data.get('probability_improvement', {})
        if probability:
            output.append(f"\n**Probability Improvement Projection:**")
            output.append(f"  Current: {probability.get('current', 'N/A')} → With Playbook: {probability.get('with_playbook', 'N/A')}")
            output.append(f"  Expected Value Increase: {probability.get('expected_value_increase', 'N/A')}")
            output.append(f"  Time Investment: {probability.get('time_investment', 'N/A')}")
            output.append(f"  ROI: {probability.get('roi', 'N/A')}")
        
        return '\n'.join(output)

    def _format_email_draft(self, data):
        """Format executive email draft with metadata and full body."""
        output = []
        
        # Email metadata
        metadata = data.get('email_metadata', {})
        if metadata:
            output.append("**Email Details:**")
            output.append(f"To: {metadata.get('to', '')}")
            if 'cc' in metadata:
                output.append(f"Cc: {metadata['cc']}")
            output.append(f"Subject: {metadata.get('subject', '')}")
            output.append(f"Importance: {metadata.get('importance', 'Normal')}")
            output.append("\n" + "="*60 + "\n")
        
        # Email body
        body = data.get('email_body', {})
        if body:
            # Greeting
            if 'greeting' in body:
                output.append(body['greeting'])
                output.append("")
            
            # Opening
            if 'opening' in body:
                output.append(body['opening'])
                output.append("")
            
            # Body paragraphs
            for paragraph in body.get('body_paragraphs', []):
                if 'section' in paragraph:
                    output.append(f"**{paragraph['section']}**")
                output.append(paragraph.get('content', ''))
                output.append("")
            
            # Call to action
            if 'call_to_action' in body:
                output.append(body['call_to_action'])
                output.append("")
            
            # Closing
            if 'closing' in body:
                output.append(body['closing'])
                output.append("")
            
            # Signature
            if 'signature' in body:
                output.append(body['signature'])
        
        # Email analysis
        email_analysis = data.get('email_analysis', {})
        if email_analysis:
            output.append("\n" + "="*60)
            output.append("\n**Email Analysis:**")
            for key, value in email_analysis.items():
                label = key.replace('_', ' ').title()
                if isinstance(value, list):
                    output.append(f"{label}:")
                    for item in value:
                        output.append(f"  • {item}")
                else:
                    output.append(f"{label}: {value}")
        
        # Attachments
        attachments = data.get('attachments_recommended', [])
        if attachments:
            output.append(f"\n**Recommended Attachments:**")
            for attachment in attachments:
                output.append(f"  • {attachment.get('name', 'File')} ({attachment.get('type', 'Document')})")
                output.append(f"    Status: {attachment.get('status', 'N/A')}")
        
        return '\n'.join(output)

    def _format_presentation_outline(self, data):
        """Format presentation outline with slide-by-slide breakdown."""
        output = []
        
        # Presentation metadata
        metadata = data.get('presentation_metadata', {})
        if metadata:
            output.append("**Presentation Details:**")
            output.append(f"Title: {metadata.get('title', 'Presentation')}")
            output.append(f"Subtitle: {metadata.get('subtitle', '')}")
            output.append(f"Audience: {metadata.get('audience', 'N/A')}")
            output.append(f"Duration: {metadata.get('duration', 'N/A')}")
            output.append(f"Total Slides: {metadata.get('total_slides', 0)}")
            output.append("")
        
        # Slide outline
        slides = data.get('slide_outline', [])
        if slides:
            output.append("**Slide-by-Slide Outline:**\n")
            for slide in slides:
                output.append(f"{'='*60}")
                output.append(f"**Slide {slide.get('slide_number', 0)}: {slide.get('title', 'Untitled')}**")
                
                content = slide.get('content', '')
                if content:
                    output.append(f"\nContent:")
                    output.append(content)
                
                visual = slide.get('visual', '')
                if visual:
                    output.append(f"\nVisual: {visual}")
                
                notes = slide.get('notes', '')
                if notes:
                    output.append(f"\nSpeaker Notes: {notes}")
                
                if slide.get('powerbi_chart'):
                    output.append(f"\n📊 Power BI Chart: {slide['powerbi_chart']}")
                
                output.append("")
        
        # Power BI integrations
        powerbi_integrations = data.get('powerbi_integrations', [])
        if powerbi_integrations:
            output.append(f"\n**Power BI Integrations:**")
            for integration in powerbi_integrations:
                output.append(f"  • {integration}")
        
        # Presentation strengths
        strengths = data.get('presentation_strengths', [])
        if strengths:
            output.append(f"\n**Presentation Strengths:**")
            for strength in strengths:
                output.append(f"  ✓ {strength}")
        
        # Delivery tips
        tips = data.get('delivery_tips', [])
        if tips:
            output.append(f"\n**Delivery Tips:**")
            for tip in tips:
                output.append(f"  💡 {tip}")
        
        return '\n'.join(output)

    def _execute_agent_call(self, agent_call_config, user_guid, user_input, demo_data):
        """
        Execute an agent call with static and dynamic parameters.
        This is called when there's no display_result and the agent needs to be executed for real.

        Args:
            agent_call_config: The agent_call content block from JSON
            user_guid: User GUID for context
            user_input: User's message for dynamic parameter extraction
            demo_data: Full demo data for additional context

        Returns:
            Agent response or fallback message
        """
        try:
            agent_name = agent_call_config.get('agent', '')
            static_params = agent_call_config.get('static_parameters', {})
            dynamic_params_config = agent_call_config.get('dynamic_parameters', {})
            fallback = agent_call_config.get('fallback_response', 'Unable to complete the agent call.')
            description = agent_call_config.get('description', f'Calling {agent_name}')

            logging.info(f"Executing agent call: {agent_name} - {description}")

            # Resolve dynamic parameters
            dynamic_params = self._resolve_dynamic_parameters(
                dynamic_params_config, user_guid, user_input, demo_data
            )

            # Merge static and dynamic parameters
            merged_params = {**static_params, **dynamic_params}

            logging.info(f"Agent call parameters: {json.dumps(merged_params, indent=2)}")

            # Get the agent (local or remote)
            agent = self._get_or_load_agent(agent_name)
            if not agent:
                logging.error(f"Agent '{agent_name}' not found locally or on GitHub")
                return fallback

            # Execute the agent
            result = agent.perform(**merged_params)

            # Log success
            logging.info(f"Agent call to '{agent_name}' completed successfully")

            return result

        except Exception as e:
            logging.error(f"Error executing agent call: {str(e)}")
            import traceback
            logging.error(traceback.format_exc())
            return agent_call_config.get('fallback_response', f'Error executing agent: {str(e)}')

    def _resolve_dynamic_parameters(self, dynamic_params_config, user_guid, user_input, demo_data):
        """
        Resolve dynamic parameters from various sources.

        Dynamic parameter configuration format:
        {
            "param_name": {
                "source": "user_guid" | "user_input" | "context" | "infer",
                "description": "What this parameter is for",
                "extract_pattern": "Optional regex pattern for extraction",
                "default": "Optional default value"
            }
        }

        Or simplified format:
        {
            "param_name": "user_guid"  # Just the source as a string
        }
        """
        resolved_params = {}

        for param_name, config in dynamic_params_config.items():
            # Handle simplified format (source as string)
            if isinstance(config, str):
                config = {"source": config}

            source = config.get('source', 'infer')
            default_value = config.get('default', None)
            extract_pattern = config.get('extract_pattern', None)

            resolved_value = None

            # Resolve based on source
            if source == 'user_guid':
                resolved_value = user_guid

            elif source == 'user_input':
                # If there's an extraction pattern, use it
                if extract_pattern:
                    match = re.search(extract_pattern, user_input, re.IGNORECASE)
                    if match:
                        resolved_value = match.group(1) if match.groups() else match.group(0)
                else:
                    # Otherwise, use the full user input
                    resolved_value = user_input

            elif source == 'context':
                # Extract from demo_data context
                context_key = config.get('context_key', param_name)
                resolved_value = demo_data.get(context_key, default_value)

            elif source == 'infer':
                # Let the assistant infer - we'll document this in the description
                # For now, we'll use None and let the target agent handle it
                resolved_value = config.get('description', 'Inferred by assistant')

            # Use default if no value resolved
            if resolved_value is None and default_value is not None:
                resolved_value = default_value

            # Only add if we have a value
            if resolved_value is not None:
                resolved_params[param_name] = resolved_value

        return resolved_params

    def _get_or_load_agent(self, agent_name):
        """
        Get an agent instance, loading from GitHub if not available locally.

        Args:
            agent_name: Name of the agent to load

        Returns:
            Agent instance or None if not found
        """
        # Try to get from local AgentManager first (if available)
        if self.agent_manager:
            try:
                agent = self.agent_manager.get_agent(agent_name)
                if agent:
                    logging.info(f"Agent '{agent_name}' found locally via AgentManager")
                    return agent
            except Exception as e:
                logging.debug(f"Error checking local AgentManager: {str(e)}")

        # Check remote cache
        if agent_name in self.remote_agent_cache:
            logging.info(f"Agent '{agent_name}' found in remote cache")
            return self.remote_agent_cache[agent_name]

        # Try to load from GitHub
        logging.info(f"Agent '{agent_name}' not found locally, attempting to load from GitHub...")
        agent = self._load_agent_from_github(agent_name)

        if agent:
            # Cache it
            self.remote_agent_cache[agent_name] = agent
            logging.info(f"Agent '{agent_name}' successfully loaded from GitHub and cached")
            return agent

        logging.error(f"Agent '{agent_name}' not found locally or on GitHub")
        return None

    def _fetch_agent_manifest(self):
        """
        Attempt to fetch agent manifest from GitHub for faster agent discovery.
        This is optional - if manifest doesn't exist, falls back to path-based search.

        Returns:
            Manifest dict or None if not available
        """
        if self._agent_manifest_cache is not None:
            return self._agent_manifest_cache

        try:
            manifest_url = f"{self.GITHUB_RAW_BASE}/manifest.json"
            logging.debug(f"Attempting to fetch agent manifest from {manifest_url}")

            response = requests.get(manifest_url, timeout=5)
            response.raise_for_status()

            manifest = response.json()
            self._agent_manifest_cache = manifest
            logging.info(f"Agent manifest loaded successfully: {len(manifest.get('agents', []))} singular agents, {len(manifest.get('stacks', []))} stacks")
            return manifest

        except requests.exceptions.RequestException as e:
            logging.debug(f"No manifest found (will use path-based search): {str(e)}")
            self._agent_manifest_cache = {}  # Cache empty dict to avoid repeated lookups
            return None
        except Exception as e:
            logging.debug(f"Error loading manifest: {str(e)}")
            self._agent_manifest_cache = {}
            return None

    def _find_agent_in_manifest(self, agent_name):
        """
        Find agent path using manifest if available.

        Args:
            agent_name: Name of the agent to find

        Returns:
            Agent file path or None if not found in manifest
        """
        manifest = self._fetch_agent_manifest()
        if not manifest:
            return None

        snake_case_name = self._convert_to_snake_case(agent_name)

        # Check singular agents
        for agent in manifest.get('agents', []):
            if agent.get('id') == snake_case_name or agent.get('id') == agent_name:
                # Extract path from URL
                url = agent.get('url', '')
                if self.GITHUB_RAW_BASE in url:
                    path = url.replace(self.GITHUB_RAW_BASE + '/', '')
                    logging.info(f"Found agent '{agent_name}' in manifest: {path}")
                    return path

        # Check stack agents
        for stack in manifest.get('stacks', []):
            for agent in stack.get('agents', []):
                if agent.get('id') == snake_case_name or agent.get('id') == agent_name:
                    url = agent.get('url', '')
                    if self.GITHUB_RAW_BASE in url:
                        path = url.replace(self.GITHUB_RAW_BASE + '/', '')
                        logging.info(f"Found stack agent '{agent_name}' in manifest: {path}")
                        return path

        return None

    def _load_agent_from_github(self, agent_name):
        """
        Load an agent from GitHub repository.

        Strategy:
        1. Check manifest (if available) for exact agent location
        2. Fall back to searching multiple possible locations:
           - agents/{agent_name}_agent.py
           - agent_stacks/*/{agent_name}_stack/agents/{agent_name}_agent.py

        Args:
            agent_name: Name of the agent to load

        Returns:
            Agent instance or None if not found
        """
        # Try manifest-based lookup first
        manifest_path = self._find_agent_in_manifest(agent_name)
        if manifest_path:
            agent = self._fetch_and_load_agent_from_path(agent_name, manifest_path)
            if agent:
                return agent
        
        # Possible agent locations to try
        snake_case_name = self._convert_to_snake_case(agent_name)

        possible_paths = [
            # Singular agents directory
            f"agents/{snake_case_name}.py",
            f"agents/{snake_case_name}_agent.py",
            f"agents/{agent_name}.py",
        ]

        # Stack agent locations
        # Format: agent_stacks/{category}_stacks/{stack_name}_stack/agents/{agent}_agent.py
        stack_categories = [
            "b2b_sales",
            "b2c_sales",
            "energy",
            "federal_government",
            "financial_services",
            "healthcare",
            "manufacturing",
            "professional_services",
            "retail_cpg",
            "slg_government",
            "software_dp"
        ]

        for category in stack_categories:
            # Try common patterns for stack agents
            possible_paths.extend([
                f"agent_stacks/{category}_stacks/{snake_case_name}_stack/agents/{snake_case_name}_agent.py",
                f"agent_stacks/{category}_stacks/{snake_case_name}_stack/agents/{snake_case_name}.py",
                f"agent_stacks/{category}_stacks/{agent_name}_stack/agents/{agent_name}.py",
            ])

        # Try each path
        for path in possible_paths:
            agent = self._fetch_and_load_agent_from_path(agent_name, path)
            if agent:
                return agent

        return None

    def _fetch_and_load_agent_from_path(self, agent_name, file_path):
        """
        Fetch agent code from GitHub and dynamically load it.
        Uses requests library for robust HTTP handling.

        Args:
            agent_name: Name of the agent
            file_path: Path to the agent file in the repo

        Returns:
            Agent instance or None if fetch/load fails
        """
        try:
            url = f"{self.GITHUB_RAW_BASE}/{file_path}"
            logging.info(f"Attempting to fetch agent from: {url}")

            # Fetch the file from GitHub using requests
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raises HTTPError for bad status codes

            agent_code = response.text
            logging.info(f"Successfully fetched agent code from {url} ({len(agent_code)} bytes)")

            # Dynamically load the agent
            agent_instance = self._load_agent_from_code(agent_name, agent_code, url)
            return agent_instance

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                logging.debug(f"Agent not found at {url}")
            else:
                logging.warning(f"HTTP error fetching agent from {url}: {e.response.status_code}")
            return None
        except requests.exceptions.Timeout:
            logging.warning(f"Timeout fetching agent from {url}")
            return None
        except requests.exceptions.RequestException as e:
            logging.warning(f"Request error fetching agent from {url}: {str(e)}")
            return None
        except Exception as e:
            logging.error(f"Error fetching/loading agent from {url}: {str(e)}")
            import traceback
            logging.error(traceback.format_exc())
            return None

    def _load_agent_from_code(self, agent_name, code, source_url):
        """
        Dynamically load an agent from Python code string.

        Args:
            agent_name: Name of the agent
            code: Python code as string
            source_url: URL where code was fetched from (for reference)

        Returns:
            Agent instance or None if load fails
        """
        try:
            # Create a temporary module name
            module_name = f"dynamic_agent_{agent_name}_{id(code)}"

            # Create module spec
            spec = importlib.util.spec_from_loader(module_name, loader=None)
            module = importlib.util.module_from_spec(spec)

            # Add to sys.modules so imports work
            sys.modules[module_name] = module

            # Execute the code in the module's namespace
            exec(code, module.__dict__)

            # Find the agent class (look for class that ends with 'Agent')
            agent_class = None
            for name, obj in module.__dict__.items():
                if (isinstance(obj, type) and
                    name.endswith('Agent') and
                    name != 'BasicAgent' and
                    hasattr(obj, 'perform')):
                    agent_class = obj
                    break

            if not agent_class:
                logging.error(f"No agent class found in code from {source_url}")
                return None

            # Instantiate the agent
            agent_instance = agent_class()
            logging.info(f"Successfully instantiated {agent_class.__name__} from {source_url}")

            return agent_instance

        except Exception as e:
            logging.error(f"Error loading agent from code: {str(e)}")
            import traceback
            logging.error(traceback.format_exc())
            return None

    def _convert_to_snake_case(self, name):
        """
        Convert CamelCase or PascalCase to snake_case.

        Args:
            name: String to convert

        Returns:
            snake_case version of the string
        """
        # Remove 'Agent' suffix if present
        if name.endswith('Agent'):
            name = name[:-5]

        # Insert underscore before uppercase letters
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def format_error_response(self, error_message):
        """
        Format an error response in a consistent way.
        """
        response = {
            "status": "error",
            "error": error_message,
            "available_actions": [
                "list_demos - List all available demo files",
                "load_demo - Load a specific demo and see its structure",
                "respond - Get canned response for user input"
            ]
        }
        return json.dumps(response, indent=2)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
