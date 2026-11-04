---
name: "rar-discreetrappers-demo-script-generator"
description: "Generates v2.0.0 demo script JSON files for ScriptedDemoAgent. Creates 60-second demos with 6 steps, persona profiles, agent catalogs, and one-pager summaries. Use this to rapidly create polished product demonstrations."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/demo_script_generator_agent", "rar_sha256": "1c4123d0d87b13fbc12e728e4b6f0e48d73ab4484ba277c667fecf11f1202f5d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Bill Whalen", "tags": ["productivity", "demos", "generator", "json", "scripted"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@discreetRappers/demo_script_generator_agent`. The original RAPP
agent is preserved byte-for-byte in `demo_script_generator_agent.py` and in the RCI capsule.

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

Generates v2.0.0 demo script JSON files for ScriptedDemoAgent. Creates 60-second demos with 6 steps, persona profiles, agent catalogs, and one-pager summaries. Use this to rapidly create polished product demonstrations.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "Action to perform: 'generate' creates new demo, 'list_templates' shows available templates, 'preview' shows what would be generated without saving",
      "enum": [
        "generate",
        "list_templates",
        "preview"
      ],
      "type": "string"
    },
    "agents_list": {
      "description": "Comma-separated list of agent names used in the demo. Example: 'OrderTracker,WarrantyLookup,DealerSupport'",
      "type": "string"
    },
    "customer_name": {
      "description": "Name of the customer/company for the demo. Example: 'Atlantic Capital Management'",
      "type": "string"
    },
    "data_sources": {
      "description": "Comma-separated list of data sources. Example: 'Salesforce,SAP ERP,Power BI'",
      "type": "string"
    },
    "industry": {
      "description": "Industry vertical for contextual responses. Examples: 'automotive_aftermarket', 'financial_services', 'healthcare', 'manufacturing', 'retail'",
      "type": "string"
    },
    "persona_context": {
      "description": "Business context for the persona. Example: 'Overseeing compliance for $8B AUM with 5 regulators'",
      "type": "string"
    },
    "persona_name": {
      "description": "Name of the demo persona. Example: 'Margaret Thompson'",
      "type": "string"
    },
    "persona_title": {
      "description": "Title of the demo persona. Example: 'Chief Compliance Officer'",
      "type": "string"
    },
    "problem_statement": {
      "description": "Business problem being solved. Example: 'Manual compliance surveillance of thousands of transactions'",
      "type": "string"
    },
    "roi_metrics": {
      "description": "Key ROI metrics. Example: '60% reduction in support tickets, 85% faster response time'",
      "type": "string"
    },
    "target_audience": {
      "description": "Target audience for the demo. Example: 'compliance_officers', 'dealers_distributors', 'sales_managers'",
      "type": "string"
    },
    "template_type": {
      "description": "Template pattern to use for the demo",
      "enum": [
        "self_service_portal",
        "sales_assistant",
        "customer_service",
        "data_analytics",
        "compliance_monitoring",
        "custom"
      ],
      "type": "string"
    },
    "use_case_description": {
      "description": "Detailed description of the MVP use case including: what it does, who uses it, what systems it integrates with, expected outcomes",
      "type": "string"
    },
    "use_case_name": {
      "description": "Short name for the use case (becomes filename). Example: 'dealer_self_service_portal'",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_script_generator_agent.py` and embedded as the fenced Python below (sha256 1c4123d0d87b13fb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_script_generator_agent.py` first:

```bash
python3 demo_script_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_script_generator_agent.py   # or on stdin
python3 demo_script_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@discreetRappers/demo_script_generator_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/demo_script_generator_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@discreetRappers/demo_script_generator_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
import json

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/demo_script_generator_agent",
    "version": "1.0.1",
    "display_name": "DemoScriptGenerator",
    "description": "Generates 60-second persona-driven demo script JSON files for ScriptedDemoAgent, via Azure OpenAI or built-in templates.",
    "author": "Bill Whalen",
    "tags": ["productivity", "demos", "generator", "json", "scripted"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": ["AZURE_OPENAI_API_VERSION", "AZURE_OPENAI_DEPLOYMENT_NAME", "AZURE_OPENAI_ENDPOINT"],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════

import logging
from datetime import datetime
from agents.basic_agent import BasicAgent
from utils.storage_factory import get_storage_manager

# Optional: Import OpenAI client for enhanced generation
try:
    from openai import AzureOpenAI
    from azure.identity import DefaultAzureCredential, get_bearer_token_provider
    import os
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    logging.debug("OpenAI not available - will use template-based generation")


class DemoScriptGeneratorAgent(BasicAgent):
    """
    Generates demo script JSON files compatible with ScriptedDemoAgent.

    Takes a use case description and generates a complete conversation flow
    with realistic responses, agent calls, and rich data displays.

    Features:
    - v2.0.0 demo format with 60-second/6-step structure
    - Persona, agents_utilized, design_principles, business_value sections
    - One-pager agent catalog for sales/marketing sharing
    - Markdown tables with source attribution
    - AI-enhanced generation using GPT for creative responses
    - Automatic saving to Azure File Storage demos directory

    v2.0.0 Design Principles:
    - 60-second demos (6 steps, 10 seconds each)
    - 15-20 second wait times between steps
    - Max 150-250 words per response
    - Max 4-5 table rows, 4-6 bullets
    - Source attribution at end of each response
    - Clear call-to-action for flow continuation
    """

    def __init__(self):
        self.name = 'DemoScriptGenerator'
        self.metadata = {
            "name": self.name,
            "description": "Generates v2.0.0 demo script JSON files for ScriptedDemoAgent. Creates 60-second demos with 6 steps, persona profiles, agent catalogs, and one-pager summaries. Use this to rapidly create polished product demonstrations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "description": "Action to perform: 'generate' creates new demo, 'list_templates' shows available templates, 'preview' shows what would be generated without saving",
                        "enum": ["generate", "list_templates", "preview"]
                    },
                    "use_case_name": {
                        "type": "string",
                        "description": "Short name for the use case (becomes filename). Example: 'dealer_self_service_portal'"
                    },
                    "use_case_description": {
                        "type": "string",
                        "description": "Detailed description of the MVP use case including: what it does, who uses it, what systems it integrates with, expected outcomes"
                    },
                    "customer_name": {
                        "type": "string",
                        "description": "Name of the customer/company for the demo. Example: 'Atlantic Capital Management'"
                    },
                    "industry": {
                        "type": "string",
                        "description": "Industry vertical for contextual responses. Examples: 'automotive_aftermarket', 'financial_services', 'healthcare', 'manufacturing', 'retail'"
                    },
                    "persona_name": {
                        "type": "string",
                        "description": "Name of the demo persona. Example: 'Margaret Thompson'"
                    },
                    "persona_title": {
                        "type": "string",
                        "description": "Title of the demo persona. Example: 'Chief Compliance Officer'"
                    },
                    "persona_context": {
                        "type": "string",
                        "description": "Business context for the persona. Example: 'Overseeing compliance for $8B AUM with 5 regulators'"
                    },
                    "target_audience": {
                        "type": "string",
                        "description": "Target audience for the demo. Example: 'compliance_officers', 'dealers_distributors', 'sales_managers'"
                    },
                    "agents_list": {
                        "type": "string",
                        "description": "Comma-separated list of agent names used in the demo. Example: 'OrderTracker,WarrantyLookup,DealerSupport'"
                    },
                    "data_sources": {
                        "type": "string",
                        "description": "Comma-separated list of data sources. Example: 'Salesforce,SAP ERP,Power BI'"
                    },
                    "problem_statement": {
                        "type": "string",
                        "description": "Business problem being solved. Example: 'Manual compliance surveillance of thousands of transactions'"
                    },
                    "roi_metrics": {
                        "type": "string",
                        "description": "Key ROI metrics. Example: '60% reduction in support tickets, 85% faster response time'"
                    },
                    "template_type": {
                        "type": "string",
                        "description": "Template pattern to use for the demo",
                        "enum": ["self_service_portal", "sales_assistant", "customer_service", "data_analytics", "compliance_monitoring", "custom"]
                    }
                },
                "required": ["action"]
            }
        }
        self.storage_manager = get_storage_manager()
        self.demo_directory = "demos"

        # Initialize OpenAI client if available
        self.openai_client = None
        if OPENAI_AVAILABLE:
            try:
                endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
                deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o")

                if endpoint:
                    token_provider = get_bearer_token_provider(
                        DefaultAzureCredential(),
                        "https://cognitiveservices.azure.com/.default"
                    )
                    self.openai_client = AzureOpenAI(
                        azure_endpoint=endpoint,
                        azure_ad_token_provider=token_provider,
                        api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2025-01-01-preview")
                    )
                    self.deployment = deployment
                    logging.info("DemoScriptGenerator: OpenAI client initialized for AI-enhanced generation")
            except Exception as e:
                logging.warning(f"DemoScriptGenerator: Could not initialize OpenAI client: {e}")

        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        """Main entry point - routes to appropriate handler based on action."""
        action = kwargs.get('action', 'list_templates')

        try:
            if action == 'list_templates':
                return self.list_templates()
            elif action == 'generate':
                return self.generate_demo_script(**kwargs)
            elif action == 'preview':
                return self.preview_demo_script(**kwargs)
            else:
                return self._format_error(f"Unknown action: {action}")
        except Exception as e:
            logging.error(f"DemoScriptGenerator error: {str(e)}")
            import traceback
            logging.error(traceback.format_exc())
            return self._format_error(f"Error: {str(e)}")

    def list_templates(self):
        """List available demo script templates (v2.0.0 format)."""
        templates = {
            "self_service_portal": {
                "name": "Self-Service Portal Agent",
                "description": "AI-powered portal for customers/dealers with order tracking, warranty lookup, product registration, and analytics",
                "typical_queries": [
                    "What is the status of my order?",
                    "What is my warranty coverage?",
                    "How do I register a product?",
                    "Show me my account analytics"
                ],
                "integrations": ["Salesforce", "SAP ERP", "Analytics Platform"],
                "best_for": "B2B portals, dealer networks, customer support",
                "agents": ["OrderTracker", "WarrantyLookup", "ProductRegistration", "Analytics", "Support"]
            },
            "sales_assistant": {
                "name": "Sales Intelligence Assistant",
                "description": "AI assistant for sales teams with pipeline management, meeting prep, forecasting, and deal coaching",
                "typical_queries": [
                    "What should I focus on today?",
                    "Show me my pipeline",
                    "Prepare me for my Contoso meeting",
                    "What's my forecast?"
                ],
                "integrations": ["CRM", "Analytics", "Email"],
                "best_for": "Sales teams, account management, forecasting",
                "agents": ["Pipeline", "MeetingPrep", "Forecast", "Coaching", "SalesSummary"]
            },
            "customer_service": {
                "name": "Customer Service Agent",
                "description": "AI agent for handling customer inquiries, troubleshooting, case management, and escalations",
                "typical_queries": [
                    "I'm having an issue with my account",
                    "My software keeps crashing",
                    "Create a support case",
                    "I need to speak to a specialist"
                ],
                "integrations": ["Service Cloud", "Knowledge Base", "CRM"],
                "best_for": "Contact centers, support portals, case management",
                "agents": ["CaseLookup", "Troubleshooting", "CaseManagement", "Escalation", "ServiceSummary"]
            },
            "data_analytics": {
                "name": "Analytics & Reporting Agent",
                "description": "AI assistant for dashboards, natural language queries, AI insights, and executive reporting",
                "typical_queries": [
                    "Show me business performance",
                    "Why is East region underperforming?",
                    "What were our top products?",
                    "Give me an executive summary"
                ],
                "integrations": ["Power BI", "Data Warehouse", "CRM"],
                "best_for": "Executives, analysts, business intelligence",
                "agents": ["Dashboard", "Query", "Insights", "Report", "AnalyticsSummary"]
            },
            "compliance_monitoring": {
                "name": "Compliance Monitoring Agent",
                "description": "AI-powered regulatory compliance with surveillance, policy validation, exam readiness, and executive dashboards",
                "typical_queries": [
                    "Run daily compliance surveillance",
                    "Investigate the personal trading alert",
                    "What's our regulatory reporting status?",
                    "How prepared are we for the SEC exam?"
                ],
                "integrations": ["Trade Surveillance", "Regulatory Feeds", "Policy System"],
                "best_for": "Compliance officers, risk managers, financial services",
                "agents": ["Surveillance", "RegulatoryAlert", "PolicyCompliance", "Documentation", "ExamReadiness", "ComplianceSummary"]
            },
            "custom": {
                "name": "Custom Template",
                "description": "AI-generated demo based on your use case description with v2.0.0 format",
                "typical_queries": ["Based on your description"],
                "integrations": ["As specified in data_sources parameter"],
                "best_for": "Unique use cases not covered by other templates",
                "agents": ["Generated based on use case"]
            }
        }

        return json.dumps({
            "status": "success",
            "format_version": "2.0.0",
            "available_templates": templates,
            "usage": "Use action='generate' with template_type, use_case_name, customer_name, industry, and optional persona/business parameters",
            "v2_features": [
                "60-second demos (6 steps)",
                "Persona profiles",
                "agents_utilized with data sources",
                "design_principles section",
                "business_value with ROI",
                "one_pager agent catalog"
            ]
        }, indent=2)

    def preview_demo_script(self, **kwargs):
        """Preview what would be generated without saving."""
        demo_script = self._build_demo_script(**kwargs)
        return json.dumps({
            "status": "preview",
            "message": "This is a preview - use action='generate' to save",
            "demo_script": demo_script
        }, indent=2)

    def generate_demo_script(self, **kwargs):
        """Generate and save a demo script to Azure File Storage."""
        use_case_name = kwargs.get('use_case_name', '')

        if not use_case_name:
            return self._format_error("use_case_name is required for generate action")

        # Build the demo script
        demo_script = self._build_demo_script(**kwargs)

        # Generate filename
        filename = self._sanitize_filename(use_case_name) + ".json"

        # Save to Azure File Storage
        try:
            self.storage_manager.ensure_directory_exists(self.demo_directory)
            content = json.dumps(demo_script, indent=2)
            self.storage_manager.write_file(self.demo_directory, filename, content)

            return json.dumps({
                "status": "success",
                "message": f"Demo script generated and saved successfully",
                "filename": filename,
                "location": f"{self.demo_directory}/{filename}",
                "total_steps": len(demo_script.get('conversation_flow', [])),
                "trigger_phrases": demo_script.get('trigger_phrases', []),
                "usage": f"Use ScriptedDemo agent with demo_name='{use_case_name}' to run this demo"
            }, indent=2)
        except Exception as e:
            return self._format_error(f"Failed to save demo script: {str(e)}")

    def _build_demo_script(self, **kwargs):
        """Build the v2.0.0 demo script JSON structure."""
        use_case_name = kwargs.get('use_case_name', 'custom_demo')
        use_case_description = kwargs.get('use_case_description', '')
        customer_name = kwargs.get('customer_name', 'Acme Corp')
        industry = kwargs.get('industry', 'technology')
        template_type = kwargs.get('template_type', 'custom')

        # v2.0.0 standard: 6 steps, 60 seconds total
        num_steps = 6
        estimated_duration = 60

        # Persona details
        persona_name = kwargs.get('persona_name', 'Alex Johnson')
        persona_title = kwargs.get('persona_title', 'Operations Manager')
        persona_context = kwargs.get('persona_context', f'Managing daily operations at {customer_name}')
        target_audience = kwargs.get('target_audience', 'operations_managers')

        # Business context
        problem_statement = kwargs.get('problem_statement', f'Manual processes and data silos affecting {industry} operations')
        roi_metrics = kwargs.get('roi_metrics', '50% time savings, 30% efficiency improvement')
        data_sources = kwargs.get('data_sources', 'Salesforce,ERP,Analytics Platform')

        # Build v2.0.0 base structure
        use_case_display = use_case_name.replace('_', ' ')
        description_text = use_case_description or f"AI-powered assistant for {use_case_display}"
        demo_script = {
            "demo_name": self._format_demo_name(use_case_name),
            "description": f"1-minute demo: {description_text}",
            "version": "2.0.0",
            "trigger_phrases": self._generate_trigger_phrases(use_case_name, use_case_description),
            "metadata": {
                "category": template_type.replace('_', ' '),
                "industry": industry,
                "max_response_length": "250_words",
                "total_steps": num_steps,
                "estimated_duration_seconds": estimated_duration,
                "target_audience": target_audience
            },
            "persona": {
                "name": persona_name,
                "title": persona_title,
                "company": customer_name,
                "context": persona_context
            },
            "agents_utilized": [],
            "conversation_flow": [],
            "design_principles": {
                "max_response_length": "150-250 words",
                "max_lines": "25-30 lines",
                "max_table_rows": "4-5 rows",
                "max_bullets": "4-6 bullets",
                "sections": "2-3 maximum",
                "visual_elements": "1 status indicator OR 1 table per response",
                "source_attribution": "Compact format at end with Source and Agents",
                "evergreen_language": "Relative timeframes only (today, yesterday, X days)",
                "call_to_action": "Clear next question to continue flow"
            },
            "business_value": {
                "problem": problem_statement,
                "solution": f"AI-powered {template_type.replace('_', ' ')} with natural language interface",
                "roi": roi_metrics,
                "performance": "Real-time data access, automated insights, instant responses"
            },
            "one_pager": {
                "title": f"{self._format_demo_name(use_case_name)} - Agent Catalog",
                "agents": []
            }
        }

        # Generate conversation flow and agents using AI
        # All templates use AI generation - no hardcoded flows
        flow_data = self._generate_demo_flow_with_ai(
            template_type=template_type,
            customer_name=customer_name,
            industry=industry,
            use_case_description=use_case_description,
            data_sources=data_sources,
            kwargs=kwargs
        )

        demo_script["conversation_flow"] = flow_data.get("conversation_flow", [])
        demo_script["agents_utilized"] = flow_data.get("agents_utilized", [])
        demo_script["one_pager"]["agents"] = flow_data.get("one_pager_agents", [])

        return demo_script

    def _generate_self_service_flow(self, customer_name, industry, description, num_steps, include_agent_calls):
        """Generate conversation flow for self-service portal template."""
        steps = []

        # Step 1: Greeting
        steps.append({
            "step_number": 1,
            "description": "User greets the portal assistant",
            "user_message": f"Hello, I need help with my account.",
            "agent_response": self._build_response(
                f"Welcome to the {customer_name} Self-Service Portal! I'm your AI assistant and I can help you with:\n\n"
                f"- **Order Status** - Track your orders in real-time\n"
                f"- **Product Registration** - Register new products for warranty\n"
                f"- **Warranty Coverage** - Check what's covered and file claims\n"
                f"- **Account Analytics** - View your purchase history and insights\n"
                f"- **Support Requests** - Get help with any issues\n\n"
                f"What can I help you with today?",
                include_agent_calls,
                "PortalAssistant",
                "Initializing session"
            ),
            "wait_for_response": True,
            "wait_timeout_seconds": 30
        })

        # Step 2: Order Status Query
        if num_steps >= 2:
            steps.append({
                "step_number": 2,
                "description": "User asks about order status",
                "user_message": "What is the status of my order?",
                "agent_response": self._build_agent_call_response(
                    "OrderTracker",
                    "Looking up your recent orders",
                    {
                        "intro_text": "I found your recent orders. Here's the status:",
                        "format": "order_status",
                        "data": {
                            "orders": [
                                {
                                    "order_id": "ORD-2026-00847",
                                    "date": "2026-01-03",
                                    "status": "Shipped",
                                    "items": "5 items",
                                    "total": "$1,247.50",
                                    "tracking": "1Z999AA10123456784",
                                    "eta": "January 8, 2026"
                                },
                                {
                                    "order_id": "ORD-2026-00812",
                                    "date": "2025-12-28",
                                    "status": "Delivered",
                                    "items": "3 items",
                                    "total": "$523.00",
                                    "delivered_date": "January 2, 2026"
                                }
                            ],
                            "summary": {
                                "total_orders_ytd": 12,
                                "pending_orders": 1,
                                "total_spent_ytd": "$15,847.00"
                            }
                        }
                    }
                ) if include_agent_calls else (
                    "**Your Recent Orders:**\n\n"
                    "| Order # | Date | Status | Items | Total |\n"
                    "|---------|------|--------|-------|-------|\n"
                    "| ORD-2026-00847 | Jan 3 | Shipped | 5 items | $1,247.50 |\n"
                    "| ORD-2026-00812 | Dec 28 | Delivered | 3 items | $523.00 |\n\n"
                    "Your order **ORD-2026-00847** is currently in transit and expected to arrive by **January 8, 2026**.\n\n"
                    "Would you like tracking details or help with anything else?"
                ),
                "wait_for_response": True,
                "wait_timeout_seconds": 45
            })

        # Step 3: Warranty Query
        if num_steps >= 3:
            steps.append({
                "step_number": 3,
                "description": "User asks about warranty coverage",
                "user_message": "What is my warranty coverage?",
                "agent_response": self._build_agent_call_response(
                    "WarrantyChecker",
                    "Checking warranty status for registered products",
                    {
                        "intro_text": "Here's your warranty coverage summary:",
                        "format": "warranty_status",
                        "data": {
                            "products": [
                                {
                                    "product": "Industrial Compressor XR-500",
                                    "serial": "XR500-2024-78456",
                                    "purchase_date": "2024-06-15",
                                    "warranty_expires": "2027-06-15",
                                    "coverage": "Full Parts & Labor",
                                    "status": "Active",
                                    "days_remaining": 891
                                },
                                {
                                    "product": "Pneumatic Tool Set Pro",
                                    "serial": "PTS-2023-12890",
                                    "purchase_date": "2023-08-20",
                                    "warranty_expires": "2025-08-20",
                                    "coverage": "Parts Only",
                                    "status": "Active",
                                    "days_remaining": 226
                                }
                            ],
                            "coverage_summary": {
                                "total_registered": 8,
                                "active_warranties": 6,
                                "expiring_soon": 1,
                                "extended_warranty_eligible": 3
                            }
                        }
                    }
                ) if include_agent_calls else (
                    "**Your Warranty Coverage:**\n\n"
                    "**Active Warranties:**\n\n"
                    "| Product | Coverage | Expires | Status |\n"
                    "|---------|----------|---------|--------|\n"
                    "| Industrial Compressor XR-500 | Full Parts & Labor | Jun 2027 | Active |\n"
                    "| Pneumatic Tool Set Pro | Parts Only | Aug 2025 | Active |\n\n"
                    "**Note:** Your Pneumatic Tool Set Pro warranty expires in 226 days. "
                    "You're eligible for an extended warranty at 15% off.\n\n"
                    "Would you like to extend coverage or file a warranty claim?"
                ),
                "wait_for_response": True,
                "wait_timeout_seconds": 45
            })

        # Step 4: Product Registration
        if num_steps >= 4:
            steps.append({
                "step_number": 4,
                "description": "User wants to register a new product",
                "user_message": "How do I register a new product?",
                "agent_response": (
                    "**Product Registration is easy!** I can help you register right now.\n\n"
                    "**Option 1: Quick Register (Recommended)**\n"
                    "Just tell me:\n"
                    "- Product name or model number\n"
                    "- Serial number (found on the product label)\n"
                    "- Purchase date\n\n"
                    "**Option 2: Scan & Register**\n"
                    "Scan the QR code on your product with your phone camera.\n\n"
                    "**Option 3: Receipt Upload**\n"
                    "Upload a photo of your receipt and I'll extract the details.\n\n"
                    "Which method would you prefer? Or just share the product details and I'll register it for you."
                ),
                "wait_for_response": True,
                "wait_timeout_seconds": 45
            })

        # Step 5: Analytics
        if num_steps >= 5:
            steps.append({
                "step_number": 5,
                "description": "User asks for account analytics",
                "user_message": "Show me my account analytics",
                "agent_response": self._build_agent_call_response(
                    "AnalyticsDashboard",
                    "Generating account analytics",
                    {
                        "intro_text": "Here's your account analytics dashboard:",
                        "format": "analytics_dashboard",
                        "data": {
                            "spending_summary": {
                                "ytd_total": "$15,847.00",
                                "vs_last_year": "+12%",
                                "average_order": "$1,320.58",
                                "orders_this_year": 12
                            },
                            "top_categories": [
                                {"category": "Compressors & Air Tools", "amount": "$6,240.00", "percent": "39%"},
                                {"category": "Automotive Parts", "amount": "$4,890.00", "percent": "31%"},
                                {"category": "Shop Equipment", "amount": "$3,200.00", "percent": "20%"},
                                {"category": "Consumables", "amount": "$1,517.00", "percent": "10%"}
                            ],
                            "savings": {
                                "total_saved": "$2,340.00",
                                "loyalty_points": 15847,
                                "tier": "Gold Partner",
                                "next_tier_in": "$4,153.00"
                            },
                            "insights": [
                                "You've saved 15% compared to retail pricing this year",
                                "Consider bulk ordering consumables - you'd save an additional $180/quarter",
                                "Your most frequent order day is Tuesday"
                            ]
                        }
                    }
                ) if include_agent_calls else (
                    "**Your Account Analytics**\n\n"
                    "**Spending Summary (YTD):**\n"
                    "- Total: $15,847.00 (+12% vs last year)\n"
                    "- Orders: 12\n"
                    "- Avg Order: $1,320.58\n\n"
                    "**Top Categories:**\n"
                    "1. Compressors & Air Tools - $6,240 (39%)\n"
                    "2. Automotive Parts - $4,890 (31%)\n"
                    "3. Shop Equipment - $3,200 (20%)\n\n"
                    "**Savings & Rewards:**\n"
                    "- Total Saved: $2,340.00\n"
                    "- Loyalty Points: 15,847\n"
                    "- Status: Gold Partner\n\n"
                    "Would you like a detailed breakdown or recommendations?"
                ),
                "wait_for_response": True,
                "wait_timeout_seconds": 45
            })

        # Add remaining steps if needed
        if num_steps >= 6:
            steps.append({
                "step_number": 6,
                "description": "User asks a support question",
                "user_message": "I need help with a product issue",
                "agent_response": (
                    "I'm sorry to hear you're having an issue. I'm here to help!\n\n"
                    "**To assist you quickly, please tell me:**\n"
                    "1. Which product is having the issue?\n"
                    "2. What's happening? (not working, damaged, missing parts, etc.)\n"
                    "3. When did the issue start?\n\n"
                    "I can often resolve issues instantly, or I'll create a support ticket and connect you with a specialist.\n\n"
                    "What product needs help?"
                ),
                "wait_for_response": True,
                "wait_timeout_seconds": 45
            })

        # Closing step
        if num_steps >= 7:
            steps.append({
                "step_number": num_steps,
                "description": "User thanks the assistant",
                "user_message": "Thank you, that's all I needed!",
                "agent_response": (
                    f"You're welcome! I'm glad I could help today.\n\n"
                    f"**Quick Recap:**\n"
                    f"- Your order ORD-2026-00847 arrives January 8th\n"
                    f"- All warranties are active\n"
                    f"- You're at Gold Partner status with 15,847 points\n\n"
                    f"Remember, I'm available 24/7 right here in the portal. "
                    f"Just ask if you need anything else!\n\n"
                    f"Have a great day! "
                ),
                "wait_for_response": True,
                "wait_timeout_seconds": 30
            })

        return steps

    def _generate_sales_assistant_flow(self, customer_name, industry, description, num_steps, include_agent_calls):
        """Generate conversation flow for sales assistant template."""
        steps = [
            {
                "step_number": 1,
                "description": "Morning greeting",
                "user_message": "Good morning, what do I need to focus on today?",
                "agent_response": self._build_agent_call_response(
                    "SalesPriority",
                    "Analyzing your priorities",
                    {
                        "intro_text": "Good morning! Here's your priority dashboard:",
                        "format": "priority_dashboard",
                        "data": {
                            "critical_items": [
                                {"icon": "🔴", "title": "Contoso Deal Closing Today", "value": "$450K", "status": "Needs signature", "description": "Contract sent, awaiting CFO signature"},
                                {"icon": "🟡", "title": "Fabrikam Follow-up Overdue", "value": "$280K", "status": "2 days overdue", "description": "POC completed, waiting on budget approval"},
                                {"icon": "🟢", "title": "3 Meetings Today", "value": "", "status": "9am, 11am, 2pm", "description": "Contoso, Northwind, Adventure Works"}
                            ],
                            "overnight_changes": [
                                "Contoso CFO viewed proposal (2:34 AM)",
                                "New lead: Woodgrove Bank - $120K potential",
                                "Fabrikam competitor mentioned Oracle in LinkedIn post"
                            ],
                            "pipeline_summary": {
                                "total_pipeline": "$2.4M",
                                "closing_this_month": "$890K",
                                "at_risk": "$340K (2 deals)"
                            }
                        }
                    }
                ) if include_agent_calls else (
                    "Good morning! Here's what needs your attention:\n\n"
                    "**Critical Today:**\n"
                    "- Contoso $450K deal - Contract awaiting CFO signature\n"
                    "- Fabrikam follow-up is 2 days overdue\n\n"
                    "**3 Meetings:**\n"
                    "- 9:00 AM - Contoso (closing)\n"
                    "- 11:00 AM - Northwind (discovery)\n"
                    "- 2:00 PM - Adventure Works (demo)\n\n"
                    "Want me to prepare you for any of these?"
                ),
                "wait_for_response": True,
                "wait_timeout_seconds": 45
            },
            {
                "step_number": 2,
                "description": "Pipeline request",
                "user_message": "Show me my pipeline",
                "agent_response": self._build_agent_call_response(
                    "SalesPipeline",
                    "Loading pipeline data",
                    {
                        "intro_text": "Here's your current pipeline:",
                        "format": "pipeline_breakdown",
                        "data": {
                            "sectors": [
                                {"name": "Enterprise", "total_value": "$1.2M", "deal_count": 5, "win_rate": "68%", "trend": "↑ 12%"},
                                {"name": "Mid-Market", "total_value": "$890K", "deal_count": 8, "win_rate": "45%", "trend": "↓ 5%"},
                                {"name": "SMB", "total_value": "$310K", "deal_count": 12, "win_rate": "72%", "trend": "→ stable"}
                            ],
                            "pipeline_health_metrics": {
                                "coverage_ratio": "3.2x",
                                "avg_deal_age": "34 days",
                                "conversion_rate": "24%"
                            }
                        }
                    }
                ) if include_agent_calls else "**Your Pipeline:** $2.4M across 25 deals...",
                "wait_for_response": True,
                "wait_timeout_seconds": 45
            }
        ]

        # Add more steps up to num_steps
        additional_steps = [
            ("Which deals are at risk?", "at_risk_analysis"),
            ("Prepare me for my Contoso meeting", "meeting_prep"),
            ("What's my forecast looking like?", "forecast"),
            ("Draft an email to the Fabrikam CFO", "email_draft"),
            ("Show me competitive intel on Oracle", "competitive_intel"),
            ("Thanks, that's helpful!", "closing")
        ]

        for i, (message, step_type) in enumerate(additional_steps):
            if len(steps) >= num_steps:
                break
            steps.append({
                "step_number": len(steps) + 1,
                "description": f"User asks about {step_type}",
                "user_message": message,
                "agent_response": f"[Response for {step_type} would be generated here]",
                "wait_for_response": True,
                "wait_timeout_seconds": 45
            })

        return steps

    def _generate_customer_service_flow(self, customer_name, industry, description, num_steps, include_agent_calls):
        """Generate conversation flow for customer service template."""
        return [
            {
                "step_number": 1,
                "description": "Customer initiates support",
                "user_message": "I have a problem with my recent order",
                "agent_response": (
                    f"I'm sorry to hear you're having trouble. I'm here to help!\n\n"
                    f"I can see your account has one recent order: **ORD-2026-00847** placed on January 3rd.\n\n"
                    f"What's the issue you're experiencing?\n"
                    f"- Item damaged or defective\n"
                    f"- Wrong item received\n"
                    f"- Missing items\n"
                    f"- Shipping/delivery issue\n"
                    f"- Something else\n\n"
                    f"Just describe the problem and I'll help resolve it."
                ),
                "wait_for_response": True,
                "wait_timeout_seconds": 30
            }
        ][:num_steps]

    def _generate_analytics_flow(self, customer_name, industry, description, num_steps, include_agent_calls):
        """Generate conversation flow for analytics template."""
        return [
            {
                "step_number": 1,
                "description": "User asks for report",
                "user_message": "Show me sales performance for last quarter",
                "agent_response": (
                    "**Q4 2025 Sales Performance**\n\n"
                    "| Metric | Value | vs Q3 | vs Target |\n"
                    "|--------|-------|-------|----------|\n"
                    "| Revenue | $4.2M | +15% | 108% |\n"
                    "| Deals Closed | 47 | +8 | 112% |\n"
                    "| Avg Deal Size | $89K | +12% | 96% |\n"
                    "| Win Rate | 34% | +5% | 113% |\n\n"
                    "**Top Performers:**\n"
                    "1. Sarah Chen - $1.2M (142% of target)\n"
                    "2. Mike Johnson - $890K (118% of target)\n"
                    "3. Lisa Park - $720K (108% of target)"
                ),
                "wait_for_response": True,
                "wait_timeout_seconds": 45
            }
        ][:num_steps]

    def _generate_generic_flow(self, customer_name, industry, description, num_steps, include_agent_calls):
        """Generate a generic conversation flow."""
        steps = []
        for i in range(num_steps):
            steps.append({
                "step_number": i + 1,
                "description": f"Step {i + 1} of demo",
                "user_message": f"[User message {i + 1}]",
                "agent_response": f"[AI response for step {i + 1}. Customize based on: {description[:100]}...]",
                "wait_for_response": True,
                "wait_timeout_seconds": 45
            })
        return steps

    def _generate_ai_enhanced_flow(self, customer_name, industry, description, num_steps, include_agent_calls):
        """Use GPT to generate creative conversation flow based on use case description."""
        if not self.openai_client:
            return self._generate_generic_flow(customer_name, industry, description, num_steps, include_agent_calls)

        try:
            prompt = f"""Generate a demo conversation flow for a product demonstration.

USE CASE: {description}

CUSTOMER: {customer_name}
INDUSTRY: {industry}
NUMBER OF STEPS: {num_steps}

Generate a realistic conversation flow where a user interacts with an AI assistant. Each step should include:
1. A natural user message (question or request)
2. A helpful, detailed AI response with specific data/examples

Return JSON array with this structure:
[
  {{
    "step_number": 1,
    "description": "Brief description of this step",
    "user_message": "What the user says",
    "agent_response": "Detailed AI response with markdown formatting, tables, bullet points as appropriate"
  }}
]

Make responses specific to the {industry} industry and include realistic data, metrics, and examples.
Include concrete numbers, dates, and details to make the demo feel real."""

            response = self.openai_client.chat.completions.create(
                model=self.deployment,
                messages=[
                    {"role": "system", "content": "You are a demo script writer. Generate realistic conversation flows for product demonstrations. Always return valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=4000
            )

            content = response.choices[0].message.content
            # Extract JSON from response
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]

            steps = json.loads(content)

            # Add standard fields
            for step in steps:
                step["wait_for_response"] = True
                step["wait_timeout_seconds"] = 45

            return steps

        except Exception as e:
            logging.error(f"AI generation failed: {e}")
            return self._generate_generic_flow(customer_name, industry, description, num_steps, include_agent_calls)

    # ==================== AI-Powered Demo Flow Generator ====================

    def _generate_demo_flow_with_ai(self, template_type, customer_name, industry, use_case_description, data_sources, kwargs):
        """
        Generate demo flow using AI for all template types.
        No hardcoded flows - everything is dynamically generated.
        """
        if not self.openai_client:
            logging.warning("OpenAI client not available - returning minimal fallback")
            return self._get_fallback_flow(customer_name, industry, data_sources)

        # Get template hints based on template_type
        template_hints = self._get_template_hints(template_type)

        sources_list = [s.strip() for s in data_sources.split(',')] if data_sources else ['System 1', 'System 2', 'System 3']
        agents_list = kwargs.get('agents_list', template_hints.get('default_agents', 'AssistantAgent,AnalyticsAgent,SupportAgent'))

        try:
            prompt = f"""Generate a v2.0.0 demo conversation flow for a 1-minute product demonstration.

TEMPLATE TYPE: {template_type}
USE CASE: {use_case_description or template_hints.get('description', f'AI-powered {template_type} solution')}
CUSTOMER: {customer_name}
INDUSTRY: {industry}
DATA SOURCES: {', '.join(sources_list)}
SUGGESTED AGENTS: {agents_list}

TEMPLATE CONTEXT:
{template_hints.get('context', 'General AI assistant demo')}

TYPICAL USER QUERIES FOR THIS TEMPLATE:
{chr(10).join('- ' + q for q in template_hints.get('typical_queries', ['Help me with my tasks']))}

REQUIREMENTS:
- Exactly 6 steps (60-second demo, 10 seconds per step)
- Each response: 150-250 words max
- Tables: max 4-5 rows per table
- Bullets: max 4-6 per response
- 2-3 sections maximum per response
- Each response ends with "Source: [data sources]\\nAgents: [agent name]"
- Each response ends with a clear call-to-action question
- Use relative timeframes (today, yesterday, X days ago) - NEVER use specific dates
- Use markdown tables for data display
- Include realistic, specific metrics and data for {industry}
- First response should be a greeting/overview
- Last response should be an executive summary

Return JSON with this exact structure:
{{
  "conversation_flow": [
    {{
      "step_number": 1,
      "user_message": "Natural user message that flows logically",
      "agent_response": "Response with tables, bullets, source attribution, and call-to-action",
      "wait_timeout_seconds": 15,
      "description": "Brief step description"
    }}
  ],
  "agents_utilized": [
    {{
      "agent_name": "AgentName",
      "description": "What the agent does",
      "inputs": ["input1", "input2"],
      "outputs": ["output1", "output2"],
      "data_sources": ["Source1", "Source2"],
      "used_in_steps": [1, 2]
    }}
  ],
  "one_pager_agents": [
    {{
      "agent_name": "Agent Name (display name)",
      "industry": "{industry}",
      "use_case_descriptions": "Use case 1; Use case 2; Use case 3",
      "key_outcomes": "Outcome 1; Outcome 2; Outcome 3",
      "key_value": "Value 1; Value 2; Value 3",
      "target_personas": "Persona 1 - context; Persona 2 - context",
      "what_it_does": "Function 1; Function 2; Function 3",
      "data_sources": "Source 1 - description; Source 2 - description"
    }}
  ]
}}

Make it specific to {industry} with realistic data, metrics, and examples. Generate 4-6 agents for the agents_utilized and one_pager_agents arrays."""

            response = self.openai_client.chat.completions.create(
                model=self.deployment,
                messages=[
                    {"role": "system", "content": "You are an expert demo script writer for enterprise AI solutions. Generate v2.0.0 format demos with rich markdown tables, source attribution, and clear call-to-actions. Always return valid JSON. Create engaging, realistic demos that showcase AI capabilities."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=8000
            )

            content = response.choices[0].message.content

            # Extract JSON from response
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]

            result = json.loads(content)

            logging.info(f"AI generated demo flow with {len(result.get('conversation_flow', []))} steps")
            return result

        except Exception as e:
            logging.error(f"AI demo flow generation failed: {e}")
            import traceback
            logging.error(traceback.format_exc())
            return self._get_fallback_flow(customer_name, industry, data_sources)

    def _get_template_hints(self, template_type):
        """Get hints and context for different template types to guide AI generation."""
        hints = {
            "self_service_portal": {
                "description": "AI-powered self-service portal for customers/dealers with instant answers",
                "context": "B2B portal where dealers or customers can check orders, warranties, register products, view analytics, and get support without calling.",
                "typical_queries": [
                    "Check on my recent orders and warranty coverage",
                    "Show me tracking details for my shipment",
                    "What is my warranty coverage?",
                    "How do I register a new product?",
                    "Show me my account analytics",
                    "I have an issue with a product"
                ],
                "default_agents": "OrderTrackerAgent,WarrantyLookupAgent,ProductRegistrationAgent,AnalyticsAgent,SupportAgent"
            },
            "sales_assistant": {
                "description": "AI sales intelligence assistant with pipeline, forecasting, and coaching",
                "context": "Sales rep assistant that provides pipeline visibility, meeting prep, forecasts, deal coaching, and daily priorities.",
                "typical_queries": [
                    "What should I focus on today?",
                    "Show me my pipeline breakdown",
                    "Prepare me for my customer meeting",
                    "What's my forecast for this quarter?",
                    "Give me coaching on closing this deal",
                    "Summarize my action items for today"
                ],
                "default_agents": "PipelineAgent,MeetingPrepAgent,ForecastAgent,CoachingAgent,SalesSummaryAgent"
            },
            "customer_service": {
                "description": "AI customer service agent with troubleshooting and case management",
                "context": "Support agent that identifies customers, diagnoses issues, provides solutions, creates cases, and handles escalations.",
                "typical_queries": [
                    "I'm having an issue with my account",
                    "My software keeps crashing",
                    "How do I fix this problem?",
                    "Create a support case for me",
                    "Can I speak to a specialist?",
                    "Thanks for your help"
                ],
                "default_agents": "CaseLookupAgent,TroubleshootingAgent,CaseManagementAgent,EscalationAgent,ServiceSummaryAgent"
            },
            "data_analytics": {
                "description": "AI analytics assistant with dashboards, queries, and insights",
                "context": "Analytics assistant that shows dashboards, answers data questions in natural language, detects anomalies, and creates reports.",
                "typical_queries": [
                    "Show me business performance last quarter",
                    "Why is this region underperforming?",
                    "What were our top products by growth?",
                    "Show me AI insights on trends",
                    "Create a weekly report with these metrics",
                    "Give me an executive summary for the board"
                ],
                "default_agents": "DashboardAgent,QueryAgent,InsightsAgent,ReportAgent,AnalyticsSummaryAgent"
            },
            "compliance_monitoring": {
                "description": "AI compliance monitoring with surveillance and regulatory tracking",
                "context": "Compliance assistant that monitors trading activity, tracks regulatory changes, validates policies, assesses exam readiness, and generates compliance dashboards.",
                "typical_queries": [
                    "Run daily compliance surveillance",
                    "Show me details on this alert",
                    "What documentation do we need?",
                    "What's our regulatory reporting status?",
                    "How prepared are we for the exam?",
                    "Give me the executive compliance summary"
                ],
                "default_agents": "SurveillanceAgent,RegulatoryAlertAgent,PolicyComplianceAgent,DocumentationAgent,ExamReadinessAgent,ComplianceSummaryAgent"
            },
            "custom": {
                "description": "Custom AI assistant based on provided description",
                "context": "Flexible AI assistant that adapts to the specific use case described.",
                "typical_queries": [
                    "Help me get started",
                    "Show me an overview",
                    "What needs my attention?",
                    "Help me with this task",
                    "Complete this action",
                    "Summarize what we did"
                ],
                "default_agents": "AssistantAgent,AnalyticsAgent,TaskAgent,SupportAgent,SummaryAgent"
            }
        }
        return hints.get(template_type, hints["custom"])

    def _get_fallback_flow(self, customer_name, industry, data_sources):
        """Minimal fallback when AI generation is unavailable."""
        sources_list = [s.strip() for s in data_sources.split(',')] if data_sources else ['System']

        return {
            "conversation_flow": [
                {
                    "step_number": 1,
                    "user_message": "Hello, I need help.",
                    "agent_response": f"Welcome to {customer_name}! I'm your AI assistant.\n\n**I can help with:**\n- Information retrieval\n- Task completion\n- Analytics and insights\n\nWhat would you like to do?\n\nSource: [{sources_list[0]}]\nAgents: AssistantAgent",
                    "wait_timeout_seconds": 15,
                    "description": "Initial greeting"
                },
                {
                    "step_number": 2,
                    "user_message": "Show me an overview.",
                    "agent_response": f"Here's your overview:\n\n| Metric | Value | Status |\n|--------|-------|--------|\n| Active | 24 | Normal |\n| Pending | 8 | Review |\n| Complete | 156 | Good |\n\nSource: [{sources_list[0]}]\nAgents: AssistantAgent\n\nWhat would you like to explore?",
                    "wait_timeout_seconds": 15,
                    "description": "Overview"
                },
                {
                    "step_number": 3,
                    "user_message": "What needs attention?",
                    "agent_response": "Priority items:\n\n| Priority | Item | Action |\n|----------|------|--------|\n| High | Review | Approval needed |\n| High | Update | Info required |\n| Medium | Follow-up | Schedule |\n\nSource: [Task System]\nAgents: AssistantAgent\n\nWant help with any item?",
                    "wait_timeout_seconds": 15,
                    "description": "Priorities"
                },
                {
                    "step_number": 4,
                    "user_message": "Help with the first item.",
                    "agent_response": "**Review Details:**\n\n| Field | Value |\n|-------|-------|\n| Type | Approval |\n| Status | Pending |\n| Requestor | Team |\n\nReady to approve?\n\nSource: [Approval System]\nAgents: AssistantAgent",
                    "wait_timeout_seconds": 15,
                    "description": "Task detail"
                },
                {
                    "step_number": 5,
                    "user_message": "Yes, approve it.",
                    "agent_response": "**Approved!**\n\n| Detail | Value |\n|--------|-------|\n| Status | Complete |\n| Time | Just now |\n\nAnything else?\n\nSource: [System]\nAgents: AssistantAgent",
                    "wait_timeout_seconds": 15,
                    "description": "Completion"
                },
                {
                    "step_number": 6,
                    "user_message": "That's all, thanks!",
                    "agent_response": "**Summary:**\n\n| Activity | Result |\n|----------|--------|\n| Reviewed | 1 |\n| Approved | 1 |\n\nHave a great day!\n\nSource: [All Systems]\nAgents: AssistantAgent",
                    "wait_timeout_seconds": 20,
                    "description": "Summary"
                }
            ],
            "agents_utilized": [
                {
                    "agent_name": "AssistantAgent",
                    "description": "General AI assistant",
                    "inputs": ["query", "context"],
                    "outputs": ["response", "actions"],
                    "data_sources": sources_list,
                    "used_in_steps": [1, 2, 3, 4, 5, 6]
                }
            ],
            "one_pager_agents": [
                {
                    "agent_name": "AI Assistant",
                    "industry": industry,
                    "use_case_descriptions": "Answer questions; Complete tasks; Provide insights",
                    "key_outcomes": "Faster responses; Better productivity; Improved experience",
                    "key_value": "24/7 availability; Instant answers; Consistent quality",
                    "target_personas": "All users - General assistance",
                    "what_it_does": "Query answering; Task execution; Information retrieval",
                    "data_sources": "; ".join([f"{s} - Business data" for s in sources_list])
                }
            ]
        }

    # ==================== End AI-Powered Demo Flow Generator ====================

    def _build_response(self, text, include_agent_calls, agent_name, description):
        """Build a response, optionally wrapping in agent_call format."""
        if include_agent_calls:
            return [
                {"type": "text", "content": text},
                {"type": "agent_call", "agent": agent_name, "description": description}
            ]
        return text

    def _build_agent_call_response(self, agent_name, description, display_result):
        """Build an agent_call response with display_result."""
        return [
            {
                "type": "agent_call",
                "agent": agent_name,
                "description": description,
                "display_result": display_result
            }
        ]

    def _generate_trigger_phrases(self, use_case_name, description):
        """Generate trigger phrases for the demo."""
        phrases = [
            f"Show me the {use_case_name.replace('_', ' ')} demo",
            f"Run {use_case_name.replace('_', ' ')} demonstration",
            f"Demo {use_case_name.replace('_', ' ')}"
        ]

        # Add description-based triggers
        if description:
            words = description.split()[:10]
            if len(words) >= 5:
                phrases.append(" ".join(words[:5]))

        return phrases

    def _format_demo_name(self, use_case_name):
        """Format use case name into display name."""
        return use_case_name.replace('_', ' ').title()

    def _sanitize_filename(self, name):
        """Sanitize name for use as filename."""
        import re
        # Replace spaces and special chars with underscores
        sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', name.lower())
        # Remove consecutive underscores
        sanitized = re.sub(r'_+', '_', sanitized)
        return sanitized.strip('_')

    def _format_error(self, message):
        """Format error response."""
        return json.dumps({
            "status": "error",
            "error": message,
            "usage": "Use action='list_templates' to see available options"
        }, indent=2)
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
