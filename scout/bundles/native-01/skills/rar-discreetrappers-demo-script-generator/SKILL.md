---
name: "rar-discreetrappers-demo-script-generator"
description: "Generates v2.0.0 demo script JSON files for ScriptedDemoAgent. Creates 60-second demos with 6 steps, persona profiles, agent catalogs, and one-pager summaries. Use this to rapidly create polished product demonstrations."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/demo_script_generator_agent", "rar_sha256": "8c3f230c67c330e7334e103653e34b810fbbcf2fe2acd120f7806f5f0cf26149", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_script_generator_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@discreetrappers/demo-script-generator:7b3ca2687a55a326a9032aeabadf0bcc6f02bafd5828152ee3da6b3571ccfc42", "kind": "skill"}, "version": "1.0.1", "author": "Bill Whalen", "tags": ["productivity", "demos", "generator", "json", "scripted"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@discreetRappers/demo_script_generator_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_script_generator_agent.py` is
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
