---
name: "rar-discreetrappers-demo-script-generator"
description: "Generates v2.0.0 demo script JSON files for ScriptedDemoAgent. Creates 60-second demos with 6 steps, persona profiles, agent catalogs, and one-pager summaries. Use this to rapidly create polished product demonstrations."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/demo_script_generator_agent", "rar_sha256": "8c3f230c67c330e7334e103653e34b810fbbcf2fe2acd120f7806f5f0cf26149", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Bill Whalen", "tags": ["productivity", "demos", "generator", "json", "scripted"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_script_generator_agent.py` and embedded as the fenced Python below (sha256 8c3f230c67c330e7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_script_generator_agent.py` first:

```bash
python3 demo_script_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_script_generator_agent.py   # or on stdin
python3 demo_script_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
