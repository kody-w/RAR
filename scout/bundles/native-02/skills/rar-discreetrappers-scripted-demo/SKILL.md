---
name: "rar-discreetrappers-scripted-demo"
description: "Executes scripted demonstrations from JSON files stored in Azure File Storage. This agent reads pre-written demo scenarios and returns the appropriate canned responses based on user input matching. Perfect for consistent, repeatable product demonstrations."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/scripted_demo_agent", "rar_sha256": "04e240a1092a8e71d446ab7662792b69cbe54e48d78fa46ec76b4ff19cb78df4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Bill Whalen", "tags": ["productivity", "demos", "scripted", "interactive", "sales"]}
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
