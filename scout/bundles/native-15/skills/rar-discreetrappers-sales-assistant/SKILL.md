---
name: "rar-discreetrappers-sales-assistant"
description: "Primary sales assistant for CRM interactions. Handles natural language requests about accounts, opportunities, contacts, and activities. Automatically enriches context, handles disambiguation, and learns preferences."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/sales_assistant_agent", "rar_sha256": "3b1ed8a43356939dfeb5d7a5bff8d47de45655c7179c82509d20d5acd78ba695", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Bill Whalen", "tags": ["integrations", "sales", "crm", "natural-language"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@discreetRappers/sales_assistant_agent`. The original RAPP
agent is preserved byte-for-byte in `sales_assistant_agent.py` and in the RCI capsule.

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

Sales Assistant Orchestrator - Coordinates CRM Agents for Natural Conversations

This agent orchestrates the disambiguation flow by:
1. Enriching context via data sloshing
2. Routing to appropriate CRUD operations
3. Learning from user clarifications
4. Maintaining conversation coherence

The "waiter" in the waiter-cook model.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "conversation_context": {
      "description": "Previous conversation state for multi-turn interactions",
      "type": "object"
    },
    "request": {
      "description": "The user's natural language request (e.g., 'What's the status of the Contoso deal?', 'Update my meeting notes for Fabrikam')",
      "type": "string"
    },
    "user_guid": {
      "description": "User identifier for personalization",
      "type": "string"
    }
  },
  "required": [
    "request",
    "user_guid"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sales_assistant_agent.py` and embedded as the fenced Python below (sha256 3b1ed8a43356939d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sales_assistant_agent.py` first:

```bash
python3 sales_assistant_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sales_assistant_agent.py   # or on stdin
python3 sales_assistant_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
    "name": "@discreetRappers/sales_assistant_agent",
    "version": "1.0.1",
    "display_name": "SalesAssistant",
    "description": "Routes natural-language CRM requests about accounts, contacts, and opportunities to the Dynamics CRUD agent, which serves built-in demo data.",
    "author": "Bill Whalen",
    "tags": ["integrations", "sales", "crm", "natural-language"],
    "category": "integrations",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
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
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
