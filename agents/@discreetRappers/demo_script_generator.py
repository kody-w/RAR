import json

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/demo_script_generator",
    "version": "1.0.0",
    "display_name": "DemoScriptGenerator",
    "description": "Generates v2.0.0 demo script JSON files for ScriptedDemoAgent. Creates 60-second demos with personas.",
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
