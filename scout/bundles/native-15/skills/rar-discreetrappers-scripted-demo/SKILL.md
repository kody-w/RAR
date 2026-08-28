---
name: "rar-discreetrappers-scripted-demo"
description: "Executes scripted demonstrations from JSON files stored in Azure File Storage. This agent reads pre-written demo scenarios and returns the appropriate canned responses based on user input matching. Perfect for consistent, repeatable product demonstrations."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/scripted_demo_agent", "rar_sha256": "feb243a6c7bbd7bf0cb329b0a8c60a6f6d88949e1893f89ccaa1cf2da31a80bc", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Bill Whalen", "tags": ["productivity", "demos", "scripted", "interactive", "sales"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scripted_demo_agent.py` and embedded as the fenced Python below (sha256 feb243a6c7bbd7bf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scripted_demo_agent.py` first:

```bash
python3 scripted_demo_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scripted_demo_agent.py   # or on stdin
python3 scripted_demo_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
