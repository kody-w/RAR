---
name: "rar-discreetrappers-sales-assistant"
description: "Primary sales assistant for CRM interactions. Handles natural language requests about accounts, opportunities, contacts, and activities. Automatically enriches context, handles disambiguation, and learns preferences."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/sales_assistant_agent", "rar_sha256": "806446e21316d4362938d86ea3be72fe0281167ec2d0e0d0167c04ff1a61e9a9", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Bill Whalen", "tags": ["integrations", "sales", "crm", "natural-language"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sales_assistant_agent.py` and embedded as the fenced Python below (sha256 806446e21316d436…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sales_assistant_agent.py` first:

```bash
python3 sales_assistant_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sales_assistant_agent.py   # or on stdin
python3 sales_assistant_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@discreetRappers/sales_assistant_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/sales_assistant_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@discreetRappers/sales_assistant_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/617Z7PjWJLdX2HUfuhZsbsIR5hWbEgASHiAMISjZqMb3nuP0fx3ge9V1/T09Cr0QRVV8Qgib2beNCfPrbr1ty/eNKZN/+XnL1RWlic79cqo/vLjlzAagj5rx6ypj3dqn1Vev52G4+1w8oYhG0avHk9x059oXT5l9Rj1XvCWHr6eOK8O33K1N069V55Kr04mL4lOfdRN0TAeGvxmGk9eEDRTPQ4/npq2bfpxqrMxi47HoKnHQ9vx6dB0euudP958PZHT2FTemAVeWW6nqO6zID0svRdE6/jjKf1mOswGr/Kzw+zbp089ZeT19XBq+yiO+qgODn3HRqPVq9pjyZef/9d//vglOz5/+flvX4Ly2OSxceO9YfK3/ZJJVI/HmveGjpftdoTuHaw26o9IVMdXYRSfvj39ZYjK+MfTf/tvxeL1yfDvP/+1Pn379S0Op/84fb77mkTjX3749u0PP55++OHf/yE8DVH/SzJl4R/Ev3//e+EjEHPUDx+7/uVbVP6w7s9EDpt/+/uh5h+KsvhUN+Nvnv7O90//j8TWp79+4ZrlFHj1iT+lUdmetmY6LdmYvj98FsbYhN72P/765Q+qv/v+B8XvkH0dxqY/quWXyquPH/3XIRp/qaKq6bff3P3L9/X/5PO/nYwxak/gzyfV64foNKbfS+4fQu371TuWH7Z++Xj85ZvUX779/F1A/0U79POJTqOg+Kj9fy6zw9jQHh0Q/dNe/yzen5nwFu8o6zr55Z/V/PDvfx7uT4c/K/wPS375zfJf/nnl74rtx9O/vvoz1/5M7nu4//nVnwUf/vl0/+jK33ryNGfeKfRG7zSUzZAe2/2nav1WoJ97++zn71n+7vlnzn48/T7t/2WCkJ9P+oEuR/qbk9e2fdP2mXc8fgau/30X/i6s/XvJH+vgH5a/B+cfLnz5+wEX9TD20yfuHd3/b/92krOgb4YmHk9G8Ma4/gC4rIrekXqm2XA6fn+W5TvwmV9G3+QOP/PoQ9GpiU+//s8jv0EfRaN+bOGQvHwg7y/fkfcX7w1Fv349PQ9lTZ8lWX0ArU6q6l/rj1dvQwfSHd7OR7X72xj9dBTsT+8PB1qffv1TfV/b7dcPqDwk3l7qNH+0dztMZfT1vQM7jepv/r67Plqj4B3osjng+BRn5Ru7D5tNOb+b7/BgKN5DJcz6Y2tH/37oPiLy81vZr7/+6ntD+tf6E0bh0+fAGS6HwHd3Tj/99MbrMkvSo4ejIG1OP/zt7z+c/vfp/7bqQ/nbhnps8Fu8Dw8F46GcDiCcqkPsSMWRvMgLP+L9t79/i+Whpo7605GdLD4mzsfiMquLKPwtsAZH/gRd0ZMfHQE9glm9R9dR1qds/Hri49N3fw+j71fHtDulzYH2YdRGdXgMnu3Q6h3b+R7JN9K+u3CIt48K+7D6q997Hy5WvwSH+K8nmVaPmm7Kd2Efbn4IHYub+j0Nv6f98/t3mf4wnKjfVHw9Ke+Ke9ez16a9981G7H3m5YCy35a/u+ZUR8tf6/csjN6h+sCHz/AcQkdkgm8p/emd86M3qgOqw+E32x8yR8eFp2fjHcaPlhu+lbbXv1MRNIcr2+ndRd4xhv/7t5Ia0mYqw2/z+UPTtyyE37LyUYMfE/n0fSSfHv2bAYyHwWMTP53opunDoxnGQ+g9gD5G9vAB1so3OkL/DvWG7435uf/mu7Zvuf8DwsflMfH87Shg8Os3oHun/v+CddDXDzh6S/0BkGjdvB3M5x2rT0/gryfpzVHesnHfVB9ZPB1U5B2F4Dcp5OtJPrI6Hn++mf6+m+Mh/aQ2n9uKjhH9njFHCr78lp3P55+CpilOVRNG5ZsElVkQHUn68nM9leWPX2qviv6F/Lx5zlE9VXQsH94c6b2TqH/zsg/G9Cez5P39H4lkNGfNNPyz24f+Ix7vHFVTOWY/feDy7znlYXvc2rdPjf+GyTf2fsPof7Xx/Ef9/1cM9PSX6Gvy9SBaB98df/jM9NuJw7EDDd5PR5GMB44fTeuV/+NNycw2fDtZbafqgOV35I+ujT4ri/H8Piu86od//4ejRxEdQm9Hv4+Mf3XVfCc4OzBhfNd5/6HsDffNgebZ/hGcf9X4be9HBx4a/9f3OPze0H/+Sbza0hs/WerfvhxJ9N51+i2N3ybPId57/U/Duxsv4FfgUHk8f6Lq8e7/bSZ9WzSk3gGSxyocQBEEjSAQBtEQgVGIgPEQRyMP9iMMiiMAwkEQxaIACoEICIHjcwAgcQx6KBgRHnHoGw42GUS/vHEmezviB0AMogSIx1FE+BAEowAeATFMoFjsoREMRSEOAID/j6VFVoffdvfp5DuI38fjOwrfNvm3Lz6KHJIcMvDk5y/6cgYI6Cr5a+vM+GoTBWUb/Crshb5gzztkAma2CQRTqrTql3qryCaUGAZ/I1PSq6g7UZV6hLdGB0cLal+mbUKvIhi6Z9+Gzpt11p5Euj/r6HbTyeTxEq1VsMDNEKhQwM9xhNXE3YYhKbycSRh3gxjTgWCgsXUvXlU8FEUCGQlPuYral/0yuNmmNkO+GEgt+7unQs9NJdMbUzwBlLgPFa7poSODjWBdlApdl5X1V6cW7y0jojJWTvFtZa4+I/HbdUfEYYMTYLlw3mDXjquj6pSngFJUjHvjn1m03CYKclQzvd7lu2oSbrT4w5SoDAKx1hPLgQvkNIau1j2HyXOCZ6oE2XHs1Fv7kDOmlQfj0vo2oSP3YRouBAfp++jfce7myxJu3xN71cuEzwgmy1T9yHmUdgtcZKHaSfidfESreh7DaZKT6qzfFCSDzRYp1MDgU5Thx4sGWwDmsrtfBIm4hCUMea8dDKRryPJeSY5dobGYICFPJU+ypijge8wjY/dMbrdI0uaNqdbLzNloD4PFhdC4luyjxR1I0/CBIqLzOjETjzRaTekEyN+ZZH71l2O8BWxiQK8ofzJLvNTHZoT0Lq2UueT3Dt+vBYis3Ys26kz1WfuaCmUl5QaGYpKKavdDktFV94ze5GeGqrVAYy+mEZGAFMhHkuWCjMYqp4RgHQ3xnSiNwtV2hm00joz4WjZ0hkQfoUzn1uAbKitEqgBvmxANe1iVLN0DRIJjBFHU5PN2Y0qXFH1nmKKFBx7nuVFt76UgdKr4ZiNdVHWdHgi0BfyjdufsHkbXK7rw+HDVa15D8HDluI5aObVROAq3HpBPaMUrIJCyC/CU9nXqSVOvheOXwGdpQtvdhOJL/s7MFrMlLIE/kp19PK2q2enzS1Ze8aIOuyc3N38V7jxIhSIvC3GTIfJes3aw5bR9hjSSURFsv1ETRSXqDOypQCLko+Pg8503MdDKyO2G6yoPLaiRKS2aKGKs0HXi5YvyULC+HkQj9an50gfueF1k5d7S0kbdr7z8iAzqWvKcbfaLkz9d/CwhsAzlDqBPhS6XUnq5xDBMLJfkCV27y1XhdhBd2sus3lL8QjbzgtmX80Jh7Esqn7ILzBRVmByYcDskazX3ZNO6IstRJeBWSWTyyIG7kn4S3MYhmpTxJj9SvoiCXr8LfG4mr2olQGiaWmIVAxpGr3VVLHN5izRlWvhBWUJ8H0jD5M/smjWtaDD5MdMocrEEoWITsaMupd2+jEtxj/KXLdy8dhKsWy7Tq77SIu4SEn6lcmwqfGW/+RA9au7DeMjwJsoJDTJ5KeiXB8nDZAH0Aq3ik06fk17bTDThPX7C90DGZOpcJLVjKnm+cRH9YgjqmpSqWlKsa1Sv4MUBIxJGHXlvuhUsoZomnuw54h3pCmc6bD32tmJJsRnW+o4uCydqyhOz9kJNoAVK1EK7T5kdcM0OLKRwR0iVRfKGLO9XEUqkeuQ5cqHvPKVfsnqPkyLJ8ZumNlENEiDmKbtHizEfLP28siw0xMXOUGOpuKLPJ1l5v51bGEf3qDtgcvTSDMphssbTVye8ktFUW6MmO4BdFrK93/q2Zt3rXdmPMKlzypNPdgFLcTtQ77mqbhCJ0QyRNsTs+OUWeE/nYI46m1+5mrJQ8cq3RfIyGcpYSJJZPes8tsGOFZGmXTtjFGKiHEXrmKargeSagyHuoDF3k2TcondNxEzz7HJJG2TuboZXWa9r3hFrI+bCwx9vLj8/4uFZMB2LXcPAxDnRoUpSVRgdEBPAAGyPFM+rUbEyOtLGNBieXIph9egq5uikGFgrB4v0l5rYiRabvNsFCd7Ck/OMn1poairglVLZ6VmrbLsieFXF+bSJksxOOuBYLOvL0Ss6rM1ITXrEti04aems2pXy4c5alg9US6eDybQiRd1MEfKaV4ukxp3Ts218Jd4y1jfObyNwEfVK0q2INB+7IwmIfse1ErJXihvkLYwJpn/i6p0bX6H8upIV3WT5gt55JkAuV5mEH2f/aQV2t87ilXMyU0D2fYFXuVSHCJE06lbfuURotarDFuqmjo5AFbBGZA88eXnX0b8d2JRUufVwSH2VhkkXnoIA3LYqeiWMalPHa/GczuXQ35gbgl/xoCxZvR+gCkcgtGOiEgUfq34gkFeswAQ+AK9GgmYgkGPkimRZy+m5M+7VEWUC5yyhqTGOqwdb7yTjBRFE2Vt6YI1EBue6emcqWJZfjRTHVdjKLxYbnaHPwpsrLSYEqK/G0iVUiZUIpjoOtQvKTaMZMEhoge3+CQPjMk+g/ExQ7mlamEWNAgny1oPpCUNzBAfElBYsbVaRr1jiyP0LxcBB9OpqRqloPjeRAt6TtUu76OLrfNMl9CuDOMkx+MwIRKRIKlShNaOwH9Xw5PlnNM/azC6ZdjdjtG7AZwhPU8nIjOgqY9WKwXnb9gDejSv6aJ+WjyAXqOL6MumYZrwYM8q9PPxyF2VQb514nUYP2EHBmkITTFZx7Hu/8lijnQVnF0ElfoY7qkhoWYRDUvHF1vh183pRitUGkivyI6H281yKpP1QAwey6LVAkTu0VwxMZm43MgNDAKPDntcCWApfjNVjpHepgUL3SGCq5RnzKmAC53RtqAkk7Gi0DV+bYBCSKS56xFVs5A5rqdJghC/dVtjIXYp7rFbJTXSszrBXrXwxYWtG5K5MEc6GaFQCUCD6j37tqtS6Sz34atU8nDvkIhnF2TaV3vS1UR84h6xipqPRnVXge+mMRFdNgldaEmBMo0UEZgRqV3U9Q/y9tQA66UV3UoAKyFVOZrXcyynpfgC8ZTwSHZy0QNHoZc0bzoS4u30FG97PbAmwYLQSt1vmCg0VpLSzMHBWpqncVckTPN/JnHgmT2+9keFNp47Ibdv5wiIQINyDamIOXNmSMnJSkslC8Ii4tMnadK805RbqeDiQFKe4ZwKTFuMqUwhzcL+JMGhQQe531wEloH0Rx1g4eOWK0J6/ygNO2W6KKVAbaQgrrUOyOL1LXQOiNcC799wdIFZxakDcgAvyrILRaOWQter9h1hks12nrV0n7DlPeKhcZB1OyOdq44Gsi45yIy8KkqwXtghvlKGNuE4aevPojC7SyeBB2xECjll3BqdH7xk+K1CqbMdcv6NOAXEHrRfke6aRsi70iCeRs2FOYufcZQNfd8AIhJxdX+J2d1f9PteNQj/L8xIeB3nRBmK3SETUKjtJ32HBzGpkeDVZcuytmnTwdnaxK9xFqLMIz1aEqtR4lBhL5hZ/x7i9kURmPaorYPcam3l3vRrgpq2KOeOKtL5IMej55CnGcgyVMtT5MJu55M3aDwZdZryz8AbdXYzHXButQ9+f+33rpac87WhRxi5r2+G+uxeLiY1OWjV+iS8JkhUPLbHQaKcuyRkRX+TOkzwa0gVYOPcliwitFzbgkRVSrhEhX1LJhdlz6elY/sI+jGWpXef+8sespdruiV56IWwJf6DMqOxptB6lYwYeR0lGLR6LHMWgnO9ZoaC5jsV3vbFC/hYRFq8nNbewXkyYVqNa0dHfeeI+VxoDzV2fn+U0hyVpOWfYgOG4xeCx0G1qeIUGKTjVfvFyo6GfWBgrBHHrb+cDK+1WI3vWXsbRxdOmgmp1GvElCdDhhvhUnjKicu2ZSDefnCWqR64fWGGWwwvr5EbzMkqYugCjJLjNaZXNj5NIG7H2i3aiQDZkK+apxH29NnTCAP1sI8yCeIQ23qbw5et62QSh2j9F3q3uAs3eFkoJ1YcmqKpZYb7GzNfjuDR0+/kMOZfRJtCDpiNT+WgJc3SJoRVeCOvewLjX6aK6c35yMLC2sJxw2dZXKEXYqKtXxH6UesJos59IQfe0m5mmn2sLxIhk8MzS+zaYTBp7HJRcq7sNwJ16eJE7WnTOPx4j90RMrmbb48ButfY8Q2mZ6zyDWBLaHgMpYPuBNt1wyPBzC7RwPPv3O+Lnudhdt9q9+7QdK+RETFh7CVEVbEBLAN0RgGPBFPFb2+SvxU3OYARNjyvQt6AXOeDEz4GXvOCHzSvyQNesBQ1b/2qC/VEJ/mWngptPKuKSsUwaegxvk4E/11rIiZwJAE5VkBVVpi/LHFvNBjMbaM1FH9fMkisfiD3RtML4gNoCFfGLJA5sqXX8E/RKaHz6dTX2ZtJX1THTVFfCFrseYAR9QqC8NX3OwjgD8sCzk2LL5B/XG/V4iCl8m8DzuV/GaqIh/PoasaIYwtCsJTo2kjPcS5K2A2ikgqq17KVV0cecDYrrlEgiN6k0y445iKD50jViqwchjOKJksKakndiSvej4+5nCEfm+FJK/iMEIAqGzCfAF3JckjzV4dgdzSAthrwcTznwjlgkdc5iG4Kx8dwUUwOJOzRHFcUDR0eRxEHol+WKXicBtY5aBO+Sbbu27JTHSR5arzlcRDhRGIb2Mkhu4Ua4Miz5aIKaC2bw5VYDh3M0Opu+bNxMNSXCzJ7KLScYT0MrVV9mswVTv+ZpJnbVG5u0jjysLn0NPHSWQkXrcxe0ec+rSlXQxYNxo0UI6hEW3OR6la21vdnKWdrleEqrCNpaoXR3g18HEYaHSgqwfdN6x7IBqFrWa+3Q/Gh0oxRmA8erGxS1fAcf9KLtr9elq8ZWIdo0bAx4tXWHkazaCURaPQAjt64217ciZxeaqp8XI3KCtFdpewzUxJHoZ7PK9jWU00gMHpume/1xmCCR7DnUlN3lsqOIx+FEwh7UxEmURuw6l0dE/cSOM/w62YlyQOE53dOUtA34iF0HWKU14nYo5G7o+WAyZxBF2Nl5tB5gRp4FUNPIh93v1svUD06oatY9iTOSQELkLtE7RIb07Wylj8rWTEp5rqMlQBbO0LbGg9msd4C7P+S1chnL4z0VFx8GNyxu3jJkBOwKekv22yN23AxoZvKOCWVL5bFkXHcEGGhKRFtSc3KgSrR1fw7KhgkioHFRJytjbZX35EXeNDsNsHZ/1RjVIi2paJ0T0QCu8DlPNHevZYF7u+kKk4j2Yi2TvRCLiNqi626Stb6qZn3GLtM/ODV0Ap0Gn+74KEI7q3U+fSpiu4cxfCf2W/06OIr/5O/m5XlmeMW9T6MfkJ3pFCXWRRN5PapsYPr9MavMxOvF5qbna5NdnCtxTL2USdlpm6uA0goICoWDL+s0XJoWGDupR1ib6HaaeBvHMkiQ2mn0vlD5Q8+Zjm809gCnmy/f92YLxEuL7t7V60Wn2B6IcA51OmYendeSoqX6FOhdrTIOHJCPR8rVCB21pduA3R9qlDndWtjd7OkFqOVQB7/QOWnq29SFdpk7zi2o57SXq77j8+baoyVDndunE8pJ8Dx4kyU5Md1wXhj163Fs0xs3P4vHIWXZweFmonpEFhdSBubhWl2MLN5rfagDGuQUiXExmOOdjiQntXRB/aw8oraJfAHTqOvmFs4mrJV6bhIDbIcLe2n8rbTuaaxfk0XZ8JkkdN7COSy8ziNiJmuuoaoeScYgor1SsFsjPdkrdAsjUjtKBvZz+s6U+2oJvX93+wdpS2HrGo5jXFdOeDTuvGI7fMX4F4fc7kZXT3m4JTfvJu4Ptx5REEil2omlucvqJ+RbltQVAtlrYSSMWsNqYi4ujts0r7sVgz4JtWAi4tMm4iqm9PfzLQzZAwQRJuf5i5cKqyTdYoU/i4bbr1f87ElXJODy8+1p6ja4mi2XzKjrtXbBEx0G5QBWmvrNvBaoNj55LD9Kz39eHwZDQ4i/7CIzI5E+zc0qdsquH44+wDZCGH1snkw3cWVcI0QfowLMtumZTV72qL0o4ik8WF8HtOJMQrwEmeZQUht0dq6KVzVa+fC6Y2wb4mPY9HYdSXlkzkWihZNMIsMx+XrDxwOgk8QNOk62fWlU/qtSTJuiTDq5P8Dt5vfPSqCnBhms2DcQXthLoldklL3edF+/b7LFMn5pAMT65IizIBzY10ld3XEauu+vZqWU/jgEo41T9E+y1lyyXWV8u766C0mzctniBCQmc3CfVjNl52EiTIYwKw2ZCFjEzjcYgHba3xALhPrrrpM+EkDKCyiWZFggUwQHLDK9o0BALwXa/KIWfifljk4D2dmohQaKCrufdHbyR7oKewUZFCpZ2z5S0D0Srg+zISw91LtlVC3cYzbcukBg5r8Qpx056iU8El5J/WgkH0i2pdne+f5zuY49opTtlT+DQd+ZIB+FSilZ57PJjMxVzOoOhSHp7ib6sr7M1bpp+xNY3Mllxosr2nGrlTe2aPeJ8yNhVXp3hue0rkrUgY7ypJXXdePUFl0OCzf0fCduyKZGPq2F+cTxtG8SjPk4Dy6O1/srZaMp6fgpXal0E180d36Z/FPpE4zzMFdUDjjcYRLNOWNE+spq2IknmDAlxDq7V6g0FnCjAgkpyNZ1NR94wzxJ7jGbYKqnLZ+JAriIzQCVt5upZHS5DcIoeXzr3G4NGouJgEVCbh70iwF73TapZTfxmOF5kczJUu4TTcrdmIFnW6vbOor2KW/x0hA0LWRACTsODp27HIOxIYzj1Ia46pUN/Ag4GnWEvanc/cq1NKxpDd5k4CS4S3yLavz8QjdLZFdNq3Lc1uyRyUALWB9Q8sxXi1V2cG76gz48ket0A86XXFe6s5Cn9819kWlG8W07hfoo48pzesL4+NKKrtVx+zXDr3URDSlwAMPAdlvQpfxBzoBhDmp4vwJlA6QLk2vXHqcrBRWMx63ZVDdolLaljdtKr8lNlr00gN38kdg6c/bOrEgBfRHVrr5xrkBM2lHswiJadFr1KaKoKhr7NzsP5rN9K8LLwTw5OC6lBdawvHfMYvNdujSUG9HNImLoPrNNBMaEHbbLwhA6L2akxNdlsEIO1Q+SVQmoFF3QIickTlxsf7XZgrLrNQePYEIgBDbPB+eccztHuOtkg88RHDJPCu9NZPburWNF04vP51oM7g0JV75mpuW994MxA/ROXAn3IBW9VOgL4jPhYy1DK2B5gnBHYgrneT4Oaa3t0sYrsovIzc4veFDhStj0ZmI4hJ5ueTAsPAVNB5gTyXgBpukCSGuuQGeMupy3Cqt9DQWvw8yvU+A81WecTCNhmok03PVKGVBjNh/VdbcGcIH8Pmzk+QLo8KsksGTKsbOrKil5zakIkF+696LNl5GAjwk2+53EiPHaj2GJshmR0pl48KaSD1bpODFjWS+dr1CwPbl8Np2OU50kne+DlaoCuvZaU20LjZP8QxFwJGGL3tD4tvRdYm32fDIbOZjlywRXLOJKiXmuEfOq3zauG0a4hqHFu2LYudpu7bmDiPIx3zLmWl/O12MqDsUlgxg8M6xUF5kLMkjsfb5cNoFQyyk8Gk+6mBgCW8HgRwN9btqDwte27opcd2t5z77BnA8IY8XfYGzeA6U+tylteGJv4rfYN+XHtU1Km3cGNU+QlRhDLILHM9e/4FzN6RJcVFXFmzyE3dfdq2c4xUeN4rgVT7V6Ms5lIfBQkHBFHQKqEmk5Z6kUiAb46znEe3OHhkdcWzV9yWn4cmEuJnEn4YP0Prg8f6VQMoTMBM1YIUBR4Ohr6nD9NcHcmKYvZMYDt9URtVDhpMv0RAFqeY58BFnky2Qqvq/2VRWgg6SoBUDP4rxAl8v1EjfLbUmqO3nhRSTrnrCFJ4mHFI7PtQedH5sVdy4Xe1Qwp3+FT/zA4SGFlPIhNox6kB+9SW3Sb1/7mk0rnosSf4mEuwjdKp3gdlP2eppklAU/4514G2K+faq7cJ2VwbAYmSaRALAQWtKEs0CN1cvHGeMKrWik3XmmEbbGuqFwg7YXSBhqUhyJbb+cJWzaput4Y8awsugml6RO9Cp25ZR8lI2xRcMoeBjolRoNbYfp8laAy2rggEm584tlj7HBo8fnGqOxjdxWon500uhQIXOGkcvTIZGIAXweI0OmcO778+CAZVpst5UtZNjhIHTePBZhd4KRNZuASpWSHw1ZnMfOUe7jA5WttsshH70YLI9qWEqCm3SxgdrWknDhQIC/QGF/n2NdITmMhZcSUoDIbGniwWUPDwJNli3yGnVNaYT9eQRfJLGug82o1/SK+M9a1CA4DZEdIBHOSaTnfMYTymS7cYNoWnVZh7E4hS4DejjO+n0xSg+YiIzgWuO4P4iiNwbQqOPw3V1XWojV20rMvmo7Y33e3RwMKNeT27gHVJJESd3lrxC7PINkqwHIwy9nheVomUBHDH9IqnQMUgwr5rvENTrO3nkcn1IwzaMVsYGNoRTAfnkeuw6pp8FdMlho0TXeem8zt6YpgK1aMVmLMUXGJ1G8ok1ieUW2EKys4CW63tDKgVLUe1bs+SUnKpcT8XDB0zx3RyWRHXqAKbkjKWcZ+Kk4E8v6cDqVzmT64LDgTjYWULg2gEqm4bOIHhvZPjjsWj7nG1ifX0sNsJyuX53LqxJZP4lRAAYaGU1NJlK79FE8xpTNL4HwuO2LNmXDhaQy7uKvKRasWJvBRXE7y6yePRJ9o1lriTA9yR6Wk8nk2W4sFQmN0inSJNL4B7F7j8u+hDiQxg7iNIjFgEVf01GyCmxzwwGcqj2DturAfWKOZC3qxO1SI959jUnbAEGTM+y9eOu63dviaVr9Bb71Xqga3DM36KVwW7PQKDx0UqGMj8kxQ2b9Sqcd6+UBGNfjNIyvUPdQqEWfEHOjjbUR8TtGi5ybFwwYIBs5un1a0s0xV8WD3nSq2NhBXkjTZHt6suK4Cjj6wQ4zh9Z5ExcKqpy0Xea6rSw0J2ou5KYWzFShmF6uQhWyBIL15s46msVCFUw40kyOTlC5QYkgbbYEjnJMQ/15MFA9pe0p95bnmZbMeIQNoQivYFkBCMBoFPgSbNBbzLiH0gy8KGCNKu4rbxIbNokGw143cL2AuQp6HNyzEeq225CjPMZKic8hZGxSWt5pBYvuCcMvD+f62ODCVrNzC9kBsm9dDT3julOjNXNWrzZ5Z9pB9qk6SEGfq97yupI15Rcp0VPJsNiKTxDWMJOcy+wVoP2l86s7gJeh1+bsVEVIHN9xBq/izi9kec5vpBIZCX3hOAWdy8tmOaWxmhJWnV+xUkFM2ycP/OliI52ATJ4Xd3pycG3Q54hvChgiLw0152DxsNqtiqWAtmFdjH1xfmBOfaafBFUmkh2IZ26j185P7xHWSOeye9V45GJ+7nl3psoSDPWv739+yIyiIJH1SEywE6D0RCP/OHqrWN3tQmmu5+XCe7M3DdsIJpJ3eV8QCazR3KyJshwwWCp9ao3+cqXP6QrVrUwkYh5b9qsxBW7bu9KE0jB8YhUB+ldLQEe/NScimxvilXF4RfRBzLEZZDz2tFmMaXg9UPNJoQ0kiQSnNqWl2tNIT9cLI1o+dgumF15I2f5KmLir8D4FLqYtvBwidYNt9SzAGiunBASU4Ehh6WBoPtjIrduexDo5N6uLRPtevA6AZXjrdXE6o5S6mKiPkT1AsxNq94VMVgakURCV6Fhms3xPNWApi617xXqNXa4Ldl6BDV/Mpzaox7En3s3qOURTecCK7/LTVRB85C5nJT4XhAMH6bmfkUBKboBmY1YJWzNIXohry4j4jR62PnDq9tL5NCtuUxBvjzm4TezU0rnm7qtHSZddfIgVl/T1q4EEVAVsE1NeY3SxFhkV+1kNXyzlrzfQoOKUKuczvFTEjnUhu6Yszy/jrZVQQM6vW4eEY2Hlda9ACbG6MXd09YMY+gYOJpLLoALBsLBkBSkIxIazOdtmCs1jxXrWustQroPUagwgIfkCA9f4ik5R2GQDNRsO4nbdIOZ+7MPdFgMS/LjKF0y32qTdO5x6UVKoRdaE2tdstFrtOQvO7UxvmMBkZ8Gpp9l69Rt83u8LPLeSQFpFzOurBgAp76/82ImaS+ulTYhGrA6gveSN6Qhc5nHNYjKOEvGiwZ3JS3zM3QCtaFe6aVoDbjF6sSK9nTHXTh2S062Fi18vuE7qONjqnlwyGWkv/pSQe2neL3KKDcLlIMG759dtJ6Ko2/R6P7+A1H0MnRm9zo2q9iMF7SioXLG2O1trfaBChwkkSely2w2Bj9P7FN/CsrNGl8ZjyUm6Xr8+BvA4sl8Q9tm8/6JmYZhidTiYxUmS/I//+PLjl/dd228XM/+ry9vvC2//3+7dfV6Ra+bDaB1EnzcNvfDnD1s//5ce/OePX/ogO+x/3h8cyin5dvHut9uD/eftwZ8+VPzk/e566bB93nb+7fLo52XU0Uve/znny/s+aPLtruxb+L38+Bn01Zf3jdWPi54//XbR8+3Hxw37j1uNhy9fwS9//z8A9hkk7TQAAA== -->
