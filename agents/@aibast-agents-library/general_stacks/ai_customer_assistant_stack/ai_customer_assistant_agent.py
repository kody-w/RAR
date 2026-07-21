"""
AI Customer Assistant Agent

AI-powered customer service assistant handling inquiries, knowledge base
searches, escalation routing, and satisfaction surveys.

Where a real deployment would connect to CRM, knowledge base, and ticketing
systems, this agent uses a synthetic data layer so it runs anywhere without credentials.

Version 1.1.0 adds deterministic customer-escalation briefing, action planning,
customer-update drafting, and portfolio reporting. Existing operations and
agent identities remain unchanged.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "templates"))

from basic_agent import BasicAgent
from datetime import datetime, timedelta

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@aibast-agents-library/ai_customer_assistant",
    "version": "1.1.1",
    "display_name": "AI Customer Assistant",
    "description": "Handles customer service inquiries, knowledge search, escalation briefs, and resolution tracking using built-in demo data.",
    "author": "AIBAST",
    "tags": ["customer-service", "support", "knowledge-base", "escalation", "satisfaction", "case-management", "action-plan"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


# ═══════════════════════════════════════════════════════════════
# SYNTHETIC DATA LAYER
# ═══════════════════════════════════════════════════════════════

_INQUIRIES = {
    "INQ-4001": {
        "id": "INQ-4001", "customer": "Acme Corp", "contact": "Lisa Park",
        "email": "lisa.park@acmecorp.com", "channel": "Live Chat",
        "subject": "Unable to generate monthly usage report",
        "description": "The export button on the analytics dashboard returns a 500 error when selecting date ranges longer than 30 days.",
        "category": "Technical Issue", "priority": "High",
        "created_at": "2025-11-14T09:23:00Z", "status": "Open",
        "account_tier": "Enterprise", "sentiment": "Frustrated",
    },
    "INQ-4002": {
        "id": "INQ-4002", "customer": "Bright Solutions", "contact": "Tom Reyes",
        "email": "tom.reyes@brightsol.com", "channel": "Email",
        "subject": "Pricing for additional user seats",
        "description": "We are expanding our team by 15 people next quarter and need pricing for additional seats on the Professional plan.",
        "category": "Billing & Pricing", "priority": "Medium",
        "created_at": "2025-11-14T10:05:00Z", "status": "Open",
        "account_tier": "Professional", "sentiment": "Neutral",
    },
    "INQ-4003": {
        "id": "INQ-4003", "customer": "Greenfield Inc", "contact": "Maria Santos",
        "email": "maria.santos@greenfield.io", "channel": "Phone",
        "subject": "SSO configuration not working after IdP migration",
        "description": "After migrating from Okta to Azure AD, SSO login redirects to a blank page. SAML assertion looks correct in dev tools.",
        "category": "Technical Issue", "priority": "Critical",
        "created_at": "2025-11-14T08:12:00Z", "status": "Open",
        "account_tier": "Enterprise", "sentiment": "Urgent",
    },
    "INQ-4004": {
        "id": "INQ-4004", "customer": "Summit Partners", "contact": "Jake Miller",
        "email": "jake.miller@summitpartners.com", "channel": "Support Portal",
        "subject": "Feature request: bulk user import via CSV",
        "description": "Currently we have to add users one at a time. We need CSV import capability for onboarding 200+ users.",
        "category": "Feature Request", "priority": "Low",
        "created_at": "2025-11-13T16:30:00Z", "status": "Open",
        "account_tier": "Professional", "sentiment": "Positive",
    },
}

_KB_ARTICLES = {
    "KB-101": {
        "id": "KB-101", "title": "How to Export Analytics Reports",
        "category": "Analytics", "relevance_score": 0.95,
        "summary": "Step-by-step guide for exporting usage and analytics reports in CSV, PDF, and Excel formats.",
        "resolution_steps": [
            "Navigate to Analytics > Reports",
            "Select date range (max 90 days per export)",
            "Choose format (CSV, PDF, Excel)",
            "Click Export and wait for download link via email",
        ],
        "last_updated": "2025-10-20", "views": 1247, "helpful_votes": 892,
    },
    "KB-102": {
        "id": "KB-102", "title": "SSO Configuration Guide (SAML 2.0)",
        "category": "Authentication", "relevance_score": 0.92,
        "summary": "Complete guide for configuring SAML-based SSO with supported identity providers.",
        "resolution_steps": [
            "Go to Admin > Security > SSO Settings",
            "Upload IdP metadata XML or enter values manually",
            "Set Assertion Consumer Service URL to https://app.example.com/sso/callback",
            "Map attributes: email, firstName, lastName, groups",
            "Test with SSO debug mode enabled before enforcing",
        ],
        "last_updated": "2025-11-01", "views": 2034, "helpful_votes": 1567,
    },
    "KB-103": {
        "id": "KB-103", "title": "User Management and Seat Licensing",
        "category": "Billing", "relevance_score": 0.88,
        "summary": "Overview of seat-based licensing, adding users, and managing subscriptions.",
        "resolution_steps": [
            "View current seat count in Admin > Billing > Subscription",
            "Click Add Seats to purchase additional licenses",
            "New seats are prorated for the current billing cycle",
            "Bulk provisioning available via SCIM for Enterprise plans",
        ],
        "last_updated": "2025-09-15", "views": 3421, "helpful_votes": 2890,
    },
    "KB-104": {
        "id": "KB-104", "title": "Known Issue: Report Export Timeout for Large Date Ranges",
        "category": "Analytics", "relevance_score": 0.97,
        "summary": "Export fails with 500 error for date ranges exceeding 60 days. Workaround and fix timeline available.",
        "resolution_steps": [
            "Split export into 30-day segments as a workaround",
            "Engineering fix scheduled for v3.8.2 (target: Dec 2025)",
            "Contact support if you need a one-time bulk export",
        ],
        "last_updated": "2025-11-10", "views": 456, "helpful_votes": 398,
    },
}

_ROUTING_RULES = {
    "Technical Issue": {
        "Critical": {"team": "Tier 2 Engineering", "sla_hours": 2, "auto_escalate": True},
        "High": {"team": "Tier 1 Technical Support", "sla_hours": 4, "auto_escalate": False},
        "Medium": {"team": "General Support", "sla_hours": 8, "auto_escalate": False},
        "Low": {"team": "General Support", "sla_hours": 24, "auto_escalate": False},
    },
    "Billing & Pricing": {
        "Critical": {"team": "Billing Escalations", "sla_hours": 2, "auto_escalate": True},
        "High": {"team": "Account Management", "sla_hours": 4, "auto_escalate": False},
        "Medium": {"team": "Account Management", "sla_hours": 8, "auto_escalate": False},
        "Low": {"team": "Self-Service Billing", "sla_hours": 24, "auto_escalate": False},
    },
    "Feature Request": {
        "Critical": {"team": "Product Management", "sla_hours": 8, "auto_escalate": False},
        "High": {"team": "Product Management", "sla_hours": 24, "auto_escalate": False},
        "Medium": {"team": "Product Backlog", "sla_hours": 72, "auto_escalate": False},
        "Low": {"team": "Product Backlog", "sla_hours": 168, "auto_escalate": False},
    },
}

_SATISFACTION_DATA = {
    "overall_csat": 4.3,
    "nps_score": 42,
    "response_time_avg_minutes": 12,
    "first_contact_resolution_rate": 0.78,
    "surveys": [
        {"inquiry_id": "INQ-3990", "score": 5, "comment": "Resolved quickly, great experience.", "date": "2025-11-13"},
        {"inquiry_id": "INQ-3988", "score": 4, "comment": "Helpful but took a while to connect.", "date": "2025-11-13"},
        {"inquiry_id": "INQ-3985", "score": 3, "comment": "Issue resolved but had to explain problem multiple times.", "date": "2025-11-12"},
        {"inquiry_id": "INQ-3982", "score": 5, "comment": "Agent was knowledgeable and proactive.", "date": "2025-11-12"},
        {"inquiry_id": "INQ-3979", "score": 2, "comment": "Still waiting for follow-up on my SSO issue.", "date": "2025-11-11"},
        {"inquiry_id": "INQ-3975", "score": 4, "comment": "Good resolution, would prefer faster initial response.", "date": "2025-11-11"},
    ],
    "trend": {"week_over_week": "+0.2", "month_over_month": "+0.1"},
}

_ESCALATION_CONTEXT = {
    "INQ-4001": {
        "issue": "Recurring monthly-report export failures",
        "interaction_history": "3 contacts in 14 days; workaround attempted twice",
        "detected_intents": ["report failure", "executive deadline", "service credit"],
        "risk_score": 82,
        "case_owner": "Priya Shah",
        "escalation_reason": "Recurring report-export failures are blocking the monthly executive review.",
        "business_impact": "Finance and operations cannot distribute the November usage report.",
        "customer_commitment": "Provide a workaround now and confirm the permanent-fix date.",
        "root_cause": "Large report exports exceed the synchronous processing timeout.",
        "engineering_work_item": "BUG-382",
        "policy_result": "Enterprise support policy permits a managed bulk export.",
        "similar_cases": 7,
        "retention_gesture": "One month of Analytics Pro service credit",
        "next_update": "2025-11-14T13:00:00Z",
        "actions": [
            ("Send the 30-day segmented-export workaround", "Priya Shah", "2025-11-14T10:30:00Z"),
            ("Run a one-time bulk export for Acme Corp", "Data Operations", "2025-11-14T12:00:00Z"),
            ("Confirm v3.8.2 release timing", "Engineering", "2025-11-14T12:30:00Z"),
        ],
    },
    "INQ-4002": {
        "issue": "Disputed charges for 15 user seats that were not activated",
        "interaction_history": "2 unresolved billing contacts in 9 days",
        "detected_intents": ["billing dispute", "refund request", "renewal risk"],
        "risk_score": 91,
        "case_owner": "Elena Garcia",
        "escalation_reason": "A billing dispute has remained unresolved through two prior contacts.",
        "business_impact": "The customer has paused its expansion and signaled renewal risk.",
        "customer_commitment": "Reverse the ineligible charge, apply a retention credit, and confirm corrected billing.",
        "root_cause": "A seat-expansion order posted before the activation workflow completed.",
        "engineering_work_item": "BILL-214",
        "policy_result": "Billing policy permits a refund for unactivated seats and a manager-approved 10% retention credit.",
        "similar_cases": 12,
        "retention_gesture": "10% service credit on the next invoice",
        "next_update": "2025-11-14T12:00:00Z",
        "actions": [
            ("Verify activation and invoice history", "Elena Garcia", "2025-11-14T10:30:00Z"),
            ("Prepare refund and retention credit", "Billing Operations", "2025-11-14T11:00:00Z"),
            ("Send confirmation and update the customer profile", "Elena Garcia", "2025-11-14T12:00:00Z"),
        ],
    },
    "INQ-4003": {
        "issue": "Enterprise-wide SSO failure after identity-provider migration",
        "interaction_history": "1 critical contact; prior migration advisory completed",
        "detected_intents": ["access outage", "identity migration", "executive escalation"],
        "risk_score": 96,
        "case_owner": "Marcus Lee",
        "escalation_reason": "Enterprise-wide SSO failure following an identity-provider migration.",
        "business_impact": "Employees cannot access production applications.",
        "customer_commitment": "Restore access or establish a safe temporary sign-in path within two hours.",
        "root_cause": "The migrated identity provider is sending an audience value that does not match the service-provider configuration.",
        "engineering_work_item": "INC-907",
        "policy_result": "Critical-incident policy permits a time-boxed break-glass sign-in path.",
        "similar_cases": 4,
        "retention_gesture": "Executive incident review and premium support extension",
        "next_update": "2025-11-14T10:00:00Z",
        "actions": [
            ("Validate SAML audience and ACS values with the customer", "Marcus Lee", "2025-11-14T09:00:00Z"),
            ("Enable a time-boxed break-glass sign-in policy", "Identity Operations", "2025-11-14T09:20:00Z"),
            ("Verify sign-in telemetry after configuration repair", "Tier 2 Engineering", "2025-11-14T09:45:00Z"),
        ],
    },
}


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _resolve_inquiry(query):
    if not query:
        return "INQ-4001"
    q = query.upper().strip()
    return q if q in _INQUIRIES else None


def _match_kb_articles(inquiry_id):
    inq = _INQUIRIES.get(inquiry_id, {})
    subject = inq.get("subject", "").lower()
    matched = []
    for kb_id, article in _KB_ARTICLES.items():
        title_lower = article["title"].lower()
        if any(word in title_lower for word in subject.split() if len(word) > 3):
            matched.append(article)
    if not matched:
        matched = [list(_KB_ARTICLES.values())[0]]
    return sorted(matched, key=lambda a: a["relevance_score"], reverse=True)


def _get_routing(category, priority):
    cat_rules = _ROUTING_RULES.get(category, _ROUTING_RULES["Technical Issue"])
    return cat_rules.get(priority, cat_rules["Medium"])


def _compute_csat_breakdown():
    scores = [s["score"] for s in _SATISFACTION_DATA["surveys"]]
    dist = {i: scores.count(i) for i in range(1, 6)}
    promoters = sum(1 for s in scores if s >= 4)
    detractors = sum(1 for s in scores if s <= 2)
    total = len(scores)
    return dist, promoters, detractors, total


def _resolve_escalation(query):
    if not query:
        return "INQ-4002"
    resolved = _resolve_inquiry(query)
    return resolved if resolved in _ESCALATION_CONTEXT else None


# ═══════════════════════════════════════════════════════════════
# AGENT CLASS
# ═══════════════════════════════════════════════════════════════

class AICustomerAssistantAgent(BasicAgent):
    """
    AI-powered customer service assistant.

    Operations:
        handle_inquiry       - triage and respond to a customer inquiry
        knowledge_search     - search knowledge base for relevant articles
        escalation_routing   - determine escalation path and SLA
        satisfaction_survey   - review CSAT scores and survey feedback
        escalation_brief      - consolidate an escalated case and its evidence
        escalation_action_plan - produce owned, time-bound resolution actions
        draft_customer_update - preview a grounded customer status update
        escalation_dashboard  - summarize the active escalation portfolio
        resolution_recommendation - recommend policy-aligned resolution actions
        process_resolution     - simulate approved refund and credit actions
        document_resolution    - simulate case closeout and profile update
    """

    def __init__(self):
        self.name = "AICustomerAssistantAgent"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "handle_inquiry", "knowledge_search",
                            "escalation_routing", "satisfaction_survey",
                            "escalation_brief", "escalation_action_plan",
                            "draft_customer_update", "escalation_dashboard",
                            "resolution_recommendation", "process_resolution",
                            "document_resolution",
                        ],
                        "description": "The customer service operation to perform",
                    },
                    "inquiry_id": {
                        "type": "string",
                        "description": "Inquiry ID (e.g. 'INQ-4001')",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        op = kwargs.get("operation", "handle_inquiry")
        inq_id = _resolve_inquiry(kwargs.get("inquiry_id", ""))
        escalation_id = _resolve_escalation(kwargs.get("inquiry_id", ""))
        dispatch = {
            "handle_inquiry": self._handle_inquiry,
            "knowledge_search": self._knowledge_search,
            "escalation_routing": self._escalation_routing,
            "satisfaction_survey": self._satisfaction_survey,
            "escalation_brief": self._escalation_brief,
            "escalation_action_plan": self._escalation_action_plan,
            "draft_customer_update": self._draft_customer_update,
            "escalation_dashboard": self._escalation_dashboard,
            "resolution_recommendation": self._resolution_recommendation,
            "process_resolution": self._process_resolution,
            "document_resolution": self._document_resolution,
        }
        handler = dispatch.get(op)
        if not handler:
            return f"Unknown operation: {op}"
        if op in {
            "escalation_brief", "escalation_action_plan",
            "escalation_dashboard", "draft_customer_update",
            "resolution_recommendation", "process_resolution",
            "document_resolution",
        }:
            if escalation_id is None:
                return (
                    f"**Error:** Unknown or ineligible escalation inquiry_id "
                    f"`{kwargs.get('inquiry_id')}`. Available escalation IDs: "
                    f"{', '.join(sorted(_ESCALATION_CONTEXT))}."
                )
            return handler(escalation_id)
        if inq_id is None:
            return (
                f"**Error:** Unknown inquiry_id `{kwargs.get('inquiry_id')}`. "
                f"Available inquiry IDs: {', '.join(sorted(_INQUIRIES))}."
            )
        return handler(inq_id)

    # ── handle_inquiry ─────────────────────────────────────────
    def _handle_inquiry(self, inq_id):
        inq = _INQUIRIES[inq_id]
        kb_matches = _match_kb_articles(inq_id)
        routing = _get_routing(inq["category"], inq["priority"])
        top_kb = kb_matches[0] if kb_matches else None
        kb_line = f"- Suggested Article: [{top_kb['id']}] {top_kb['title']} (relevance: {top_kb['relevance_score']:.0%})" if top_kb else "- No matching articles found"
        return (
            f"**Customer Inquiry: {inq['id']}**\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Customer | {inq['customer']} ({inq['account_tier']}) |\n"
            f"| Contact | {inq['contact']} |\n"
            f"| Channel | {inq['channel']} |\n"
            f"| Category | {inq['category']} |\n"
            f"| Priority | {inq['priority']} |\n"
            f"| Sentiment | {inq['sentiment']} |\n\n"
            f"**Subject:** {inq['subject']}\n\n"
            f"**Description:** {inq['description']}\n\n"
            f"**Recommended Response:**\n"
            f"{kb_line}\n"
            f"- Assigned Team: {routing['team']}\n"
            f"- SLA Target: {routing['sla_hours']} hours\n"
            f"- Auto-Escalate: {'Yes' if routing['auto_escalate'] else 'No'}\n\n"
            f"Source: [CRM + Knowledge Base + Ticketing System]\nAgents: AICustomerAssistantAgent"
        )

    # ── knowledge_search ───────────────────────────────────────
    def _knowledge_search(self, inq_id):
        articles = _match_kb_articles(inq_id)
        inq = _INQUIRIES[inq_id]
        rows = ""
        for a in articles:
            rows += f"| {a['id']} | {a['title']} | {a['relevance_score']:.0%} | {a['views']:,} |\n"
        top = articles[0] if articles else None
        steps = ""
        if top:
            steps = "\n".join(f"{i+1}. {s}" for i, s in enumerate(top["resolution_steps"]))
        return (
            f"**Knowledge Base Search Results**\n"
            f"Query: \"{inq['subject']}\"\n\n"
            f"| Article ID | Title | Relevance | Views |\n|---|---|---|---|\n"
            f"{rows}\n"
            f"**Top Match: {top['title'] if top else 'N/A'}**\n\n"
            f"**Summary:** {top['summary'] if top else 'N/A'}\n\n"
            f"**Resolution Steps:**\n{steps}\n\n"
            f"Last Updated: {top['last_updated'] if top else 'N/A'} | "
            f"Helpful Votes: {top['helpful_votes']:,} / {top['views']:,} views\n\n"
            f"Source: [Knowledge Base]\nAgents: AICustomerAssistantAgent"
        )

    # ── escalation_routing ─────────────────────────────────────
    def _escalation_routing(self, inq_id):
        inq = _INQUIRIES[inq_id]
        routing = _get_routing(inq["category"], inq["priority"])
        all_routes = []
        for cat, priorities in _ROUTING_RULES.items():
            for pri, rule in priorities.items():
                all_routes.append(f"| {cat} | {pri} | {rule['team']} | {rule['sla_hours']}h |")
        route_rows = "\n".join(all_routes)
        return (
            f"**Escalation Routing: {inq['id']}**\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Category | {inq['category']} |\n"
            f"| Priority | {inq['priority']} |\n"
            f"| Assigned Team | {routing['team']} |\n"
            f"| SLA Target | {routing['sla_hours']} hours |\n"
            f"| Auto-Escalate | {'Yes' if routing['auto_escalate'] else 'No'} |\n\n"
            f"**Routing Matrix:**\n\n"
            f"| Category | Priority | Team | SLA |\n|---|---|---|---|\n"
            f"{route_rows}\n\n"
            f"Source: [Routing Engine + SLA Configuration]\nAgents: AICustomerAssistantAgent"
        )

    # ── satisfaction_survey ─────────────────────────────────────
    def _satisfaction_survey(self, inq_id):
        data = _SATISFACTION_DATA
        dist, promoters, detractors, total = _compute_csat_breakdown()
        survey_rows = ""
        for s in data["surveys"]:
            stars = "*" * s["score"]
            survey_rows += f"| {s['inquiry_id']} | {stars} ({s['score']}/5) | {s['comment'][:50]} | {s['date']} |\n"
        dist_rows = "\n".join(f"| {score} Star | {count} ({count/total*100:.0f}%) |" for score, count in sorted(dist.items(), reverse=True))
        return (
            f"**Customer Satisfaction Dashboard**\n\n"
            f"| Metric | Value |\n|---|---|\n"
            f"| Overall CSAT | {data['overall_csat']}/5.0 |\n"
            f"| NPS Score | {data['nps_score']} |\n"
            f"| Avg Response Time | {data['response_time_avg_minutes']} minutes |\n"
            f"| First Contact Resolution | {data['first_contact_resolution_rate']:.0%} |\n\n"
            f"**Score Distribution:**\n\n"
            f"| Rating | Count |\n|---|---|\n"
            f"{dist_rows}\n\n"
            f"**Recent Surveys:**\n\n"
            f"| Inquiry | Rating | Comment | Date |\n|---|---|---|---|\n"
            f"{survey_rows}\n"
            f"**Trends:** WoW {data['trend']['week_over_week']}, MoM {data['trend']['month_over_month']}\n\n"
            f"Source: [Survey Platform + CRM Analytics]\nAgents: AICustomerAssistantAgent"
        )

    def _escalation_brief(self, inq_id):
        inq = _INQUIRIES[inq_id]
        ctx = _ESCALATION_CONTEXT[inq_id]
        kb = _match_kb_articles(inq_id)[0]
        routing = _get_routing(inq["category"], inq["priority"])
        return (
            f"**Customer Escalation Brief: {inq_id}**\n\n"
            f"| Field | Detail |\n|---|---|\n"
            f"| Customer | {inq['customer']} ({inq['account_tier']}) |\n"
            f"| Contact | {inq['contact']} via {inq['channel']} |\n"
            f"| Status | {inq['status']} / {inq['priority']} / {inq['sentiment']} |\n"
            f"| Escalation Owner | {ctx['case_owner']} |\n"
            f"| Assigned Team | {routing['team']} |\n"
            f"| SLA | {routing['sla_hours']} hours |\n"
            f"| Engineering Work Item | {ctx['engineering_work_item']} |\n"
            f"| Interaction History | {ctx['interaction_history']} |\n"
            f"| Detected Intents | {', '.join(ctx['detected_intents'])} |\n"
            f"| Escalation Risk | {ctx['risk_score']}/100 |\n"
            f"| Similar Cases | {ctx['similar_cases']} |\n"
            f"| Next Customer Update | {ctx['next_update']} |\n\n"
            f"**Escalation Reason:** {ctx['escalation_reason']}\n\n"
            f"**Business Impact:** {ctx['business_impact']}\n\n"
            f"**Root Cause:** {ctx['root_cause']}\n\n"
            f"**Intent Analysis:** {len(ctx['detected_intents'])} issues detected; "
            f"{inq['sentiment'].lower()} sentiment and {inq['priority'].lower()} urgency.\n\n"
            f"**Policy / Eligibility:** {ctx['policy_result']}\n\n"
            f"**Customer Commitment:** {ctx['customer_commitment']}\n\n"
            f"**Supporting Knowledge:** [{kb['id']}] {kb['title']}\n\n"
            f"Source: [Dynamics 365 Customer Service + Knowledge Base + Engineering Work Tracking]\n"
            f"Agents: AICustomerAssistantAgent"
        )

    def _escalation_action_plan(self, inq_id):
        ctx = _ESCALATION_CONTEXT[inq_id]
        rows = "\n".join(
            f"| {index} | {action} | {owner} | {due} | Planned |"
            for index, (action, owner, due) in enumerate(ctx["actions"], 1)
        )
        return (
            f"**Escalation Action Plan: {inq_id}**\n\n"
            f"| # | Action | Owner | Due (UTC) | Status |\n|---|---|---|---|---|\n"
            f"{rows}\n\n"
            f"**Next customer update:** {ctx['next_update']}\n"
            f"**Commitment:** {ctx['customer_commitment']}\n\n"
            f"This is a deterministic offline plan; no CRM, Teams, or engineering records were changed.\n\n"
            f"Source: [Dynamics 365 Customer Service + Microsoft Teams + Engineering Work Tracking]\n"
            f"Agents: AICustomerAssistantAgent"
        )

    def _draft_customer_update(self, inq_id):
        inq = _INQUIRIES[inq_id]
        ctx = _ESCALATION_CONTEXT[inq_id]
        first_action = ctx["actions"][0][0]
        return (
            f"**Customer Update Draft: {inq_id}**\n\n"
            f"To: {inq['contact']} <{inq['email']}>\n"
            f"Subject: Update on {ctx['issue']}\n\n"
            f"Hello {inq['contact'].split()[0]},\n\n"
            f"I am {ctx['case_owner']}, and I am coordinating your escalation. "
            f"We understand the impact: {ctx['business_impact']} "
            f"Our current finding is that {ctx['root_cause'].lower()} "
            f"Our immediate next step is to {first_action.lower()} "
            f"We will provide the next update by {ctx['next_update']}.\n\n"
            f"Regards,\n{ctx['case_owner']}\n\n"
            f"**Preview only:** this operation does not send email or update the case.\n\n"
            f"Source: [Dynamics 365 Customer Service + Outlook]\nAgents: AICustomerAssistantAgent"
        )

    def _escalation_dashboard(self, inq_id):
        rows = []
        for case_id, ctx in sorted(_ESCALATION_CONTEXT.items()):
            inq = _INQUIRIES[case_id]
            routing = _get_routing(inq["category"], inq["priority"])
            rows.append(
                f"| {case_id} | {inq['customer']} | {inq['priority']} | {inq['sentiment']} "
                f"| {ctx['case_owner']} | {routing['team']} | {routing['sla_hours']}h "
                f"| {ctx['next_update']} |"
            )
        return (
            f"**Active Customer Escalations**\n\n"
            f"| Case | Customer | Priority | Sentiment | Owner | Team | SLA | Next Update |\n"
            f"|---|---|---|---|---|---|---|---|\n"
            f"{chr(10).join(rows)}\n\n"
            f"Active escalations: {len(rows)} | Critical: "
            f"{sum(_INQUIRIES[key]['priority'] == 'Critical' for key in _ESCALATION_CONTEXT)}\n\n"
            f"Source: [Dynamics 365 Customer Service + SLA Configuration]\n"
            f"Agents: AICustomerAssistantAgent"
        )

    def _resolution_recommendation(self, inq_id):
        ctx = _ESCALATION_CONTEXT[inq_id]
        return (
            f"**Resolution Recommendation: {inq_id}**\n\n"
            f"1. Resolve the root cause: {ctx['root_cause']}\n"
            f"2. Apply the eligible remedy: {ctx['policy_result']}\n"
            f"3. Offer the retention gesture: {ctx['retention_gesture']}.\n"
            f"4. Use the prepared talking points to acknowledge impact and confirm ownership.\n"
            f"5. Complete the follow-up actions by {ctx['next_update']}.\n\n"
            f"**Comparable evidence:** {ctx['similar_cases']} similar resolved cases support this playbook.\n\n"
            f"Source: [SharePoint Playbooks + Dynamics 365 Case History + Billing Policy]\n"
            f"Agents: AICustomerAssistantAgent"
        )

    def _process_resolution(self, inq_id):
        ctx = _ESCALATION_CONTEXT[inq_id]
        if inq_id == "INQ-4002":
            action = "Refund $1,875 for unactivated seats and apply a 10% next-invoice credit"
        else:
            action = f"Apply authorized remedy: {ctx['retention_gesture']}"
        return (
            f"**Simulated Resolution Receipt: {inq_id}**\n\n"
            f"- Action: {action}\n"
            f"- Policy check: Eligible\n"
            f"- Approval: Escalation manager approval assumed for preview\n"
            f"- Dynamics 365 status: Not written\n"
            f"- Billing status: Not written\n\n"
            f"Dry-run only; no refund, credit, or external mutation occurred.\n\n"
            f"Source: [Dynamics 365 CRM + Billing]\nAgents: AICustomerAssistantAgent"
        )

    def _document_resolution(self, inq_id):
        ctx = _ESCALATION_CONTEXT[inq_id]
        return (
            f"**Resolution Documentation Preview: {inq_id}**\n\n"
            f"- Root cause: {ctx['root_cause']}\n"
            f"- Resolution: {ctx['customer_commitment']}\n"
            f"- Similar-case link count: {ctx['similar_cases']}\n"
            f"- Product feedback: Prepared from recurring-case pattern\n"
            f"- Customer profile update: Prepared\n"
            f"- Outlook confirmation: Prepared for approval\n\n"
            f"No case, customer profile, product issue, or email was changed.\n\n"
            f"Source: [Dynamics 365 CRM + SharePoint + Outlook]\nAgents: AICustomerAssistantAgent"
        )


if __name__ == "__main__":
    agent = AICustomerAssistantAgent()
    for op in [
        "handle_inquiry", "knowledge_search", "escalation_routing",
        "satisfaction_survey", "escalation_brief", "escalation_action_plan",
        "draft_customer_update", "escalation_dashboard",
        "resolution_recommendation", "process_resolution",
        "document_resolution",
    ]:
        print("=" * 60)
        print(agent.perform(operation=op, inquiry_id="INQ-4001"))
        print()
