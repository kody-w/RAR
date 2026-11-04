---
name: "rar-discreetrappers-sales-assistant"
description: "Primary sales assistant for CRM interactions. Handles natural language requests about accounts, opportunities, contacts, and activities. Automatically enriches context, handles disambiguation, and learns preferences."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/sales_assistant_agent", "rar_sha256": "806446e21316d4362938d86ea3be72fe0281167ec2d0e0d0167c04ff1a61e9a9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Bill Whalen", "tags": ["integrations", "sales", "crm", "natural-language"]}
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

<!-- rci-capsule:v1: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 -->
