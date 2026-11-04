---
name: "rar-discreetrappers-demo-script-generator"
description: "Generates v2.0.0 demo script JSON files for ScriptedDemoAgent. Creates 60-second demos with 6 steps, persona profiles, agent catalogs, and one-pager summaries. Use this to rapidly create polished product demonstrations."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/demo_script_generator_agent", "rar_sha256": "1c4123d0d87b13fbc12e728e4b6f0e48d73ab4484ba277c667fecf11f1202f5d", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Bill Whalen", "tags": ["productivity", "demos", "generator", "json", "scripted"]}
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
