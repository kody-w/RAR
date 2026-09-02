---
name: "rar-discreetrappers-sales-assistant"
description: "Primary sales assistant for CRM interactions. Handles natural language requests about accounts, opportunities, contacts, and activities. Automatically enriches context, handles disambiguation, and learns preferences."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/sales_assistant_agent", "rar_sha256": "3b1ed8a43356939dfeb5d7a5bff8d47de45655c7179c82509d20d5acd78ba695", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "sales_assistant_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@discreetrappers/sales-assistant:701f736589b8347f92be7814ce4b716e7d872f1530fd901a1cc967d6c01ad439", "kind": "skill"}, "version": "1.0.1", "author": "Bill Whalen", "tags": ["integrations", "sales", "crm", "natural-language"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@discreetRappers/sales_assistant_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `sales_assistant_agent.py` is
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
