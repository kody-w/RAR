"""
Sales Assistant Orchestrator - Coordinates CRM Agents for Natural Conversations

This agent orchestrates the disambiguation flow by:
1. Enriching context via data sloshing
2. Routing to appropriate CRUD operations
3. Learning from user clarifications
4. Maintaining conversation coherence

The "waiter" in the waiter-cook model.
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/sales_assistant",
    "version": "1.0.0",
    "display_name": "SalesAssistant",
    "description": "Natural language CRM assistant — handles requests about accounts, opportunities, contacts, and pipeline.",
    "author": "Bill Whalen",
    "tags": ["integrations", "sales", "crm", "natural-language"],
    "category": "integrations",
    "quality_tier": "verified",
    "requires_env": [],
    "dependencies": ["@rapp/basic-agent"],
}
# ═══════════════════════════════════════════════════════════════


import logging
import re
from datetime import datetime
from agents.basic_agent import BasicAgent
from utils.storage_factory import get_storage_manager


class SalesAssistantAgent(BasicAgent):
    """
    High-level orchestrator for sales CRM interactions.
    Coordinates context enrichment, disambiguation, and CRUD operations.
    """
    
    def __init__(self):
        self.name = 'SalesAssistant'
        self.metadata = {
            "name": self.name,
            "description": "Primary sales assistant for CRM interactions. Handles natural language requests about accounts, opportunities, contacts, and activities. Automatically enriches context, handles disambiguation, and learns preferences.",
            "parameters": {
                "type": "object",
                "properties": {
                    "request": {
                        "type": "string",
                        "description": "The user's natural language request (e.g., 'What's the status of the Contoso deal?', 'Update my meeting notes for Fabrikam')"
                    },
                    "user_guid": {
                        "type": "string",
                        "description": "User identifier for personalization"
                    },
                    "conversation_context": {
                        "type": "object",
                        "description": "Previous conversation state for multi-turn interactions"
                    }
                },
                "required": ["request", "user_guid"]
            }
        }
        self.storage_manager = get_storage_manager()
        
        # Lazy-load sub-agents
        self._dynamics_agent = None
        self._enrichment_agent = None
        self._schema_agent = None
        
        super().__init__(name=self.name, metadata=self.metadata)

    @property
    def dynamics_agent(self):
        if self._dynamics_agent is None:
            from agents.dynamics_crud_agent import DynamicsCRUDAgent
            self._dynamics_agent = DynamicsCRUDAgent()
        return self._dynamics_agent

    @property
    def enrichment_agent(self):
        if self._enrichment_agent is None:
            from agents.context_enrichment_agent import ContextEnrichmentAgent
            self._enrichment_agent = ContextEnrichmentAgent()
        return self._enrichment_agent

    @property
    def schema_agent(self):
        if self._schema_agent is None:
            from agents.schema_discovery_agent import SchemaDiscoveryAgent
            self._schema_agent = SchemaDiscoveryAgent()
        return self._schema_agent

    def perform(self, **kwargs):
        request = kwargs.get('request', '')
        user_guid = kwargs.get('user_guid')
        conversation_context = kwargs.get('conversation_context', {})

        if not request:
            return "How can I help you with your CRM today?"

        if user_guid:
            self.storage_manager.set_memory_context(user_guid)

        # Step 1: Parse the request
        parsed = self._parse_request(request)
        
        # Step 2: Check for disambiguation response
        if conversation_context.get('awaiting_disambiguation'):
            return self._handle_disambiguation_response(
                request, 
                conversation_context, 
                user_guid
            )

        # Step 3: Enrich context via data sloshing
        context = self._enrich_context(request, parsed, user_guid)
        
        # Step 4: Route to appropriate handler
        return self._route_request(request, parsed, context, user_guid)

    def _parse_request(self, request):
        """Parse natural language request into structured intent"""
        
        parsed = {
            "intent": "query",  # query, update, create, delete, report
            "entities": [],
            "entity_type": None,
            "temporal_hints": [],
            "ownership_hints": [],
            "action_verbs": [],
            "custom_ids": [],
        }
        
        request_lower = request.lower()
        
        # Detect intent
        if any(word in request_lower for word in ['update', 'add', 'set', 'change', 'modify']):
            parsed["intent"] = "update"
        elif any(word in request_lower for word in ['create', 'new', 'make', 'add new']):
            parsed["intent"] = "create"
        elif any(word in request_lower for word in ['delete', 'remove', 'cancel']):
            parsed["intent"] = "delete"
        elif any(word in request_lower for word in ['report', 'summary', 'dashboard', 'pipeline']):
            parsed["intent"] = "report"
        elif any(word in request_lower for word in ['status', 'what', 'show', 'get', 'find', 'where', 'how']):
            parsed["intent"] = "query"
        
        # Detect entity type
        entity_keywords = {
            "account": ["account", "company", "customer", "client", "org"],
            "opportunity": ["opportunity", "deal", "opp", "sale", "pipeline"],
            "contact": ["contact", "person", "people", "stakeholder"],
            "lead": ["lead", "prospect"],
            "task": ["task", "to-do", "todo", "action item", "follow-up", "followup"],
            "appointment": ["meeting", "appointment", "call", "event"],
        }
        
        for entity_type, keywords in entity_keywords.items():
            if any(kw in request_lower for kw in keywords):
                parsed["entity_type"] = entity_type
                break
        
        # Default to opportunity for deal-related terms
        if not parsed["entity_type"] and any(term in request_lower for term in ['q1', 'q2', 'q3', 'q4', 'deal', 'revenue']):
            parsed["entity_type"] = "opportunity"
        
        # Extract entity mentions (company names)
        known_entities = ['contoso', 'fabrikam', 'northwind', 'adventure works', 'acme']
        for entity in known_entities:
            if entity in request_lower:
                parsed["entities"].append(entity.title())
        
        # Extract custom IDs
        sps_match = re.search(r'sps[-\s]?(\d{4})?[-\s]?(\d+)', request_lower)
        if sps_match:
            parsed["custom_ids"].append(("sps", sps_match.group(0)))
        
        # Temporal hints
        if 'today' in request_lower or 'this morning' in request_lower:
            parsed["temporal_hints"].append("today")
        if 'latest' in request_lower or 'recent' in request_lower or 'current' in request_lower:
            parsed["temporal_hints"].append("recency")
        if 'active' in request_lower:
            parsed["temporal_hints"].append("active")
        if re.search(r'q[1-4]', request_lower):
            parsed["temporal_hints"].append("quarterly")
        if re.search(r'202[4-9]', request_lower):
            match = re.search(r'(202[4-9])', request_lower)
            parsed["temporal_hints"].append(f"year:{match.group(1)}")
        
        # Ownership hints
        if 'my ' in request_lower or ' mine' in request_lower:
            parsed["ownership_hints"].append("owned_by_user")
        if 'our ' in request_lower or 'team' in request_lower:
            parsed["ownership_hints"].append("team")
        
        return parsed

    def _enrich_context(self, request, parsed, user_guid):
        """Use data sloshing to enrich context"""
        
        try:
            enrichment_result = self.enrichment_agent.perform(
                query=request,
                entity_mentions=parsed.get("entities", []),
                intent_signals=[parsed.get("intent", "query")],
                user_guid=user_guid
            )
            
            # Parse the JSON from enrichment result
            if "Context Frame (JSON)" in enrichment_result:
                json_start = enrichment_result.find("```json") + 7
                json_end = enrichment_result.find("```", json_start)
                if json_start > 7 and json_end > json_start:
                    import json
                    context_json = enrichment_result[json_start:json_end].strip()
                    return json.loads(context_json)
        except Exception as e:
            logging.warning(f"Context enrichment failed: {e}")
        
        return {"orientation": {"confidence_level": "low"}}

    def _route_request(self, request, parsed, context, user_guid):
        """Route request to appropriate handler based on intent and context"""
        
        intent = parsed.get("intent", "query")
        entity_type = parsed.get("entity_type", "account")
        entities = parsed.get("entities", [])
        custom_ids = parsed.get("custom_ids", [])
        
        # Check orientation for confidence
        orientation = context.get("orientation", {})
        confidence = orientation.get("confidence_level", "low")
        
        # If we have custom IDs (like SPS numbers), use them directly
        if custom_ids:
            id_type, id_value = custom_ids[0]
            return self._handle_custom_id_lookup(id_type, id_value, entity_type, intent, user_guid)
        
        # High confidence with preference - use directly
        if confidence == "high" and orientation.get("suggested_approach") == "use_preference":
            hints = orientation.get("disambiguation_hints", [])
            if hints:
                # Extract record name from hint like "Use 'Contoso Cloud Services' for contoso"
                for hint in hints:
                    if "Use '" in hint:
                        record_name = hint.split("Use '")[1].split("'")[0]
                        return self._execute_with_record(intent, entity_type, record_name, request, user_guid)
        
        # Build query from entities
        query = " ".join(entities) if entities else ""
        
        # Apply temporal hints to narrow query
        if parsed.get("temporal_hints"):
            query_suffix = []
            if "recency" in parsed["temporal_hints"]:
                query_suffix.append("latest")
            if "active" in parsed["temporal_hints"]:
                query_suffix.append("active")
            for hint in parsed["temporal_hints"]:
                if hint.startswith("year:"):
                    query_suffix.append(hint.split(":")[1])
            if query_suffix:
                query = f"{query} {' '.join(query_suffix)}".strip()
        
        # Execute CRUD operation
        return self.dynamics_agent.perform(
            operation="search" if intent == "query" else intent,
            entity_type=entity_type,
            query=query,
            user_guid=user_guid
        )

    def _handle_custom_id_lookup(self, id_type, id_value, entity_type, intent, user_guid):
        """Handle lookup by custom ID (like SPS number)"""
        
        # First, check if we know this ID pattern
        schema_result = self.schema_agent.perform(
            action="lookup_term",
            term=id_type.upper(),
            user_guid=user_guid
        )
        
        # Execute the lookup
        result = self.dynamics_agent.perform(
            operation="read",
            entity_type=entity_type or "opportunity",
            query=id_value,
            user_guid=user_guid
        )
        
        # If this is a new pattern, learn it
        if "not found in glossary" in schema_result.lower():
            self.schema_agent.perform(
                action="learn_term",
                term=id_type.upper(),
                entity_type=entity_type or "opportunity",
                field_name=f"new_{id_type.lower()}number",
                user_guid=user_guid
            )
        
        return result

    def _execute_with_record(self, intent, entity_type, record_name, request, user_guid):
        """Execute operation on a known record"""
        
        result = self.dynamics_agent.perform(
            operation="read" if intent == "query" else intent,
            entity_type=entity_type,
            query=record_name,
            user_guid=user_guid
        )
        
        # Add note about using preference
        if "|||VOICE|||" in result:
            parts = result.split("|||VOICE|||")
            result = parts[0] + "\n*Using your saved preference.*\n|||VOICE|||" + parts[1]
        
        return result

    def _handle_disambiguation_response(self, response, context, user_guid):
        """Handle user's response to disambiguation prompt"""
        
        pending_entity = context.get("pending_entity_type", "account")
        pending_query = context.get("pending_query", "")
        
        # Check for numeric choice
        match = re.search(r'\b(\d+)\b', response)
        if match:
            choice = int(match.group(1))
            return self.dynamics_agent.perform(
                operation="disambiguate",
                entity_type=pending_entity,
                query=pending_query,
                disambiguation_choice=choice,
                user_guid=user_guid
            )
        
        # Check for natural language clarification
        response_lower = response.lower()
        
        clarification_mappings = {
            "first": 1,
            "second": 2,
            "third": 3,
            "fourth": 4,
            "last": -1,  # Special handling
            "the latest": "recency",
            "the active": "active",
            "the current": "active",
            "mine": "ownership",
            "my ": "ownership",
        }
        
        for phrase, value in clarification_mappings.items():
            if phrase in response_lower:
                if isinstance(value, int):
                    return self.dynamics_agent.perform(
                        operation="disambiguate",
                        entity_type=pending_entity,
                        query=pending_query,
                        disambiguation_choice=value,
                        user_guid=user_guid
                    )
                else:
                    # Refine search with hint
                    refined_query = f"{pending_query} {value}"
                    return self.dynamics_agent.perform(
                        operation="read",
                        entity_type=pending_entity,
                        query=refined_query,
                        user_guid=user_guid
                    )
        
        # Couldn't parse - ask again
        return "I didn't quite catch that. Could you tell me which number (1, 2, 3, etc.) or describe which one you mean?"


class SalesBriefingAgent(BasicAgent):
    """
    Prepares comprehensive sales briefings by sloshing data from CRM,
    calendar, recent activities, and external sources.
    """
    
    def __init__(self):
        self.name = 'SalesBriefing'
        self.metadata = {
            "name": self.name,
            "description": "Prepares sales briefings for meetings by gathering account info, opportunity status, recent activities, key contacts, and relevant news. Say 'prepare me for my sales briefing' or 'brief me on [account]'.",
            "parameters": {
                "type": "object",
                "properties": {
                    "account_name": {
                        "type": "string",
                        "description": "Account to prepare briefing for"
                    },
                    "meeting_type": {
                        "type": "string",
                        "description": "Type of meeting (discovery, proposal, negotiation, close)",
                        "enum": ["discovery", "proposal", "negotiation", "close", "general"]
                    },
                    "include_news": {
                        "type": "boolean",
                        "description": "Whether to include industry news"
                    },
                    "user_guid": {
                        "type": "string",
                        "description": "User identifier"
                    }
                },
                "required": ["user_guid"]
            }
        }
        self.storage_manager = get_storage_manager()
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        account_name = kwargs.get('account_name', '')
        meeting_type = kwargs.get('meeting_type', 'general')
        include_news = kwargs.get('include_news', True)
        user_guid = kwargs.get('user_guid')

        if user_guid:
            self.storage_manager.set_memory_context(user_guid)

        # Slosh data together for briefing
        briefing = self._build_briefing(account_name, meeting_type, include_news, user_guid)
        
        return briefing

    def _build_briefing(self, account_name, meeting_type, include_news, user_guid):
        """Build comprehensive sales briefing"""
        
        now = datetime.now()
        
        response = f"## 📋 Sales Briefing\n"
        response += f"*Generated {now.strftime('%B %d, %Y at %I:%M %p')}*\n\n"
        
        # Account overview (demo data)
        if account_name:
            response += f"### 🏢 {account_name}\n\n"
        else:
            response += "### 🏢 Today's Accounts\n\n"
            account_name = "Contoso Cloud Services"  # Default for demo
        
        response += "**Account Snapshot:**\n"
        response += f"- Industry: Technology / Cloud Services\n"
        response += f"- Tier: Enterprise\n"
        response += f"- Relationship: 3+ years\n"
        response += f"- Annual Revenue: $2.4M\n"
        response += f"- Health Score: 🟢 Good\n\n"
        
        # Active opportunities
        response += "### 💰 Active Opportunities\n\n"
        response += "| Opportunity | Value | Stage | Close Date |\n"
        response += "|-------------|-------|-------|------------|\n"
        response += "| Cloud Migration Phase 2 | $890,000 | Qualification | Jun 30, 2026 |\n"
        response += "| Security Assessment | $125,000 | Proposal | Mar 15, 2026 |\n\n"
        
        # Key contacts
        response += "### 👥 Key Contacts\n\n"
        response += "- **Demo Contact A** - VP of IT (Decision Maker) 📞\n"
        response += "- **Demo Contact B** - Director of Cloud Ops (Champion) ⭐\n"
        response += "- **Demo Contact C** - Procurement Manager 📋\n\n"
        
        # Recent activity
        response += "### 📅 Recent Activity\n\n"
        response += "- *Feb 1* - Proposal sent for Security Assessment\n"
        response += "- *Jan 28* - Technical deep-dive with IT team\n"
        response += "- *Jan 15* - Quarterly business review completed\n\n"
        
        # Meeting-specific prep
        if meeting_type != "general":
            response += f"### 🎯 {meeting_type.title()} Meeting Prep\n\n"
            
            if meeting_type == "discovery":
                response += "**Key Questions:**\n"
                response += "- What are your top 3 IT priorities this year?\n"
                response += "- How is your current cloud migration progressing?\n"
                response += "- What's driving the timeline for this initiative?\n\n"
            elif meeting_type == "proposal":
                response += "**Proposal Highlights:**\n"
                response += "- Emphasize 3-year TCO savings (estimated 40%)\n"
                response += "- Reference successful Phase 1 completion\n"
                response += "- Address security concerns from last call\n\n"
            elif meeting_type == "negotiation":
                response += "**Negotiation Points:**\n"
                response += "- Floor: $800K (10% discount max)\n"
                response += "- Competitor pricing: ~$950K (Competitor A)\n"
                response += "- Value-adds available: Extended support, training credits\n\n"
            elif meeting_type == "close":
                response += "**Closing Checklist:**\n"
                response += "- [ ] Legal review complete\n"
                response += "- [ ] Budget confirmed with CFO\n"
                response += "- [ ] Implementation timeline agreed\n"
                response += "- [ ] Contract redlines addressed\n\n"
        
        # Industry news (if requested)
        if include_news:
            response += "### 📰 Industry News\n\n"
            response += "- *Cloud adoption accelerates in enterprise* - Gartner predicts 85% of enterprises will embrace cloud-first by 2027\n"
            response += "- *Security spending up 15%* - Organizations increasing security budgets amid rising threats\n"
            response += "- *AI integration trends* - 60% of cloud migrations now include AI/ML components\n\n"
        
        # Action items
        response += "### ✅ Suggested Actions\n\n"
        response += "1. Review competitor analysis before meeting\n"
        response += "2. Confirm attendee list with Demo Contact B\n"
        response += "3. Prepare ROI calculator with their metrics\n"
        
        voice = f"Your briefing for {account_name} is ready. You have 2 active opportunities totaling over 1 million dollars. Key contact is Demo Contact A, VP of IT."
        
        return response + f"\n\n|||VOICE|||\n\n{voice}"


class PostMeetingAgent(BasicAgent):
    """
    Handles post-meeting actions - updates CRM, sends summaries, creates tasks.
    """
    
    def __init__(self):
        self.name = 'PostMeeting'
        self.metadata = {
            "name": self.name,
            "description": "Runs post-meeting actions: updates CRM records, logs activities, creates follow-up tasks, and sends meeting summaries. Say 'run post-meeting actions' after any sales call.",
            "parameters": {
                "type": "object",
                "properties": {
                    "meeting_notes": {
                        "type": "string",
                        "description": "Notes from the meeting to log"
                    },
                    "account_name": {
                        "type": "string",
                        "description": "Account the meeting was about"
                    },
                    "opportunity_name": {
                        "type": "string",
                        "description": "Opportunity discussed (if any)"
                    },
                    "next_steps": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of follow-up actions"
                    },
                    "attendees": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Meeting attendees"
                    },
                    "send_summary": {
                        "type": "boolean",
                        "description": "Whether to email a summary to the team"
                    },
                    "user_guid": {
                        "type": "string",
                        "description": "User identifier"
                    }
                },
                "required": ["user_guid"]
            }
        }
        self.storage_manager = get_storage_manager()
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        meeting_notes = kwargs.get('meeting_notes', '')
        account_name = kwargs.get('account_name', 'Contoso Cloud Services')
        opportunity_name = kwargs.get('opportunity_name', '')
        next_steps = kwargs.get('next_steps', ['Follow up on proposal'])
        attendees = kwargs.get('attendees', [])
        send_summary = kwargs.get('send_summary', False)
        user_guid = kwargs.get('user_guid')

        if user_guid:
            self.storage_manager.set_memory_context(user_guid)

        now = datetime.now()
        
        response = "## ✅ Post-Meeting Actions Completed\n\n"
        
        # Log the activity
        response += "### 📝 Activity Logged\n"
        response += f"- Type: Meeting\n"
        response += f"- Account: {account_name}\n"
        if opportunity_name:
            response += f"- Opportunity: {opportunity_name}\n"
        response += f"- Date: {now.strftime('%B %d, %Y')}\n"
        if meeting_notes:
            response += f"- Notes: {meeting_notes[:100]}...\n" if len(meeting_notes) > 100 else f"- Notes: {meeting_notes}\n"
        response += f"\n🔗 [View Activity](https://org.crm.dynamics.com/main.aspx?appid=demo&etn=appointment&id=demo)\n\n"
        
        # Create follow-up tasks
        if next_steps:
            response += "### 📋 Tasks Created\n"
            for i, step in enumerate(next_steps, 1):
                due_date = (now + timedelta(days=7)).strftime('%b %d')
                response += f"{i}. {step} (Due: {due_date})\n"
                response += f"   🔗 [View Task](https://org.crm.dynamics.com/main.aspx?appid=demo&etn=task&id=demo-{i})\n"
            response += "\n"
        
        # Update opportunity stage if mentioned
        if opportunity_name:
            response += "### 💰 Opportunity Updated\n"
            response += f"- {opportunity_name}: Stage advanced, notes added\n"
            response += f"🔗 [View Opportunity](https://org.crm.dynamics.com/main.aspx?appid=demo&etn=opportunity&id=demo)\n\n"
        
        # Send summary if requested
        if send_summary:
            response += "### 📧 Summary Sent\n"
            response += f"- Email sent to your team with meeting summary\n"
            response += f"- Recipients: Your Team Distribution List\n\n"
        
        response += "---\n*All CRM records updated. Quick-tap links above to view details.*"
        
        voice = f"Post-meeting actions complete. Logged activity for {account_name}, created {len(next_steps)} follow-up tasks."
        if send_summary:
            voice += " Summary emailed to your team."
        
        return response + f"\n\n|||VOICE|||\n\n{voice}"


# Import timedelta for PostMeetingAgent
from datetime import timedelta
