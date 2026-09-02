---
name: "rar-discreetrappers-scripted-demo"
description: "Executes scripted demonstrations from JSON files stored in Azure File Storage. This agent reads pre-written demo scenarios and returns the appropriate canned responses based on user input matching. Perfect for consistent, repeatable product demonstrations."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/scripted_demo_agent", "rar_sha256": "feb243a6c7bbd7bf0cb329b0a8c60a6f6d88949e1893f89ccaa1cf2da31a80bc", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scripted_demo_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@discreetrappers/scripted-demo:9343e13d4007098a43b32a536eca246ed6cadf99191ce18ee87b0be415d7fd7a", "kind": "skill"}, "version": "1.0.1", "author": "Bill Whalen", "tags": ["productivity", "demos", "scripted", "interactive", "sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@discreetRappers/scripted_demo_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scripted_demo_agent.py` is
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
