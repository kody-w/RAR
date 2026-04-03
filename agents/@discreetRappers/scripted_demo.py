import json

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/scripted_demo",
    "version": "1.0.0",
    "display_name": "ScriptedDemo",
    "description": "Executes interactive scripted demonstrations from JSON files. Simulates real agent conversations for demos.",
    "author": "Bill Whalen",
    "tags": ["productivity", "demos", "scripted", "interactive", "sales"],
    "category": "productivity",
    "quality_tier": "verified",
    "requires_env": [],
    "dependencies": ["@rapp/basic-agent"],
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