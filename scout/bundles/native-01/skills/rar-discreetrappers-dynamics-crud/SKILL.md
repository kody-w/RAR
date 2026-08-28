---
name: "rar-discreetrappers-dynamics-crud"
description: "Performs CRUD operations on Dynamics 365 entities (accounts, contacts, opportunities, leads, tasks, activities). Handles disambiguation when multiple records match a query by asking clarifying questions and learning user preferences."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/dynamics_crud_agent", "rar_sha256": "4e5e25a1d96fb04d15be965f7694df521b343684c68eb165da12aab4fbb8e52e", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Bill Whalen", "tags": ["integrations", "dynamics-365", "crm", "crud", "microsoft"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@discreetRappers/dynamics_crud_agent`. The original RAPP
agent is preserved byte-for-byte in `dynamics_crud_agent.py` and in the RCI capsule.

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

Dynamics 365 CRUD Agent - Entity Operations with Disambiguation

This agent handles Create, Read, Update, Delete operations against Dynamics 365
with built-in disambiguation when multiple records match a query.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "data": {
      "description": "Data to create or update (field-value pairs)",
      "type": "object"
    },
    "disambiguation_choice": {
      "description": "User's choice when disambiguating (1-based index)",
      "type": "integer"
    },
    "entity_type": {
      "description": "The Dynamics 365 entity type",
      "enum": [
        "account",
        "contact",
        "opportunity",
        "lead",
        "task",
        "phonecall",
        "email",
        "appointment"
      ],
      "type": "string"
    },
    "operation": {
      "description": "The CRUD operation to perform",
      "enum": [
        "create",
        "read",
        "update",
        "delete",
        "search",
        "disambiguate"
      ],
      "type": "string"
    },
    "query": {
      "description": "Search query or entity name to find (e.g., 'Contoso', 'Q1 Enterprise Deal', 'SPS-2026-0142')",
      "type": "string"
    },
    "record_id": {
      "description": "Specific record ID for update/delete operations",
      "type": "string"
    },
    "user_guid": {
      "description": "User identifier for preference storage",
      "type": "string"
    }
  },
  "required": [
    "operation",
    "entity_type"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dynamics_crud_agent.py` and embedded as the fenced Python below (sha256 4e5e25a1d96fb04d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dynamics_crud_agent.py` first:

```bash
python3 dynamics_crud_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dynamics_crud_agent.py   # or on stdin
python3 dynamics_crud_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Dynamics 365 CRUD Agent - Entity Operations with Disambiguation

This agent handles Create, Read, Update, Delete operations against Dynamics 365
with built-in disambiguation when multiple records match a query.
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@discreetRappers/dynamics_crud_agent",
    "version": "1.0.1",
    "display_name": "DynamicsCRUD",
    "description": "Simulates Dynamics 365 CRUD on accounts, contacts, opportunities, and leads with disambiguation, using built-in demo data.",
    "author": "Bill Whalen",
    "tags": ["integrations", "dynamics-365", "crm", "crud", "microsoft"],
    "category": "integrations",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════


import logging
import json
import re
from datetime import datetime
from agents.basic_agent import BasicAgent
from utils.storage_factory import get_storage_manager

# Try to import Dynamics SDK, fall back to demo mode if not available
try:
    from azure.identity import DefaultAzureCredential
    DYNAMICS_SDK_AVAILABLE = True
except ImportError:
    DYNAMICS_SDK_AVAILABLE = False


class DynamicsCRUDAgent(BasicAgent):
    def __init__(self):
        self.name = 'DynamicsCRUD'
        self.metadata = {
            "name": self.name,
            "description": "Performs CRUD operations on Dynamics 365 entities (accounts, contacts, opportunities, leads, tasks, activities). Handles disambiguation when multiple records match a query by asking clarifying questions and learning user preferences.",
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "description": "The CRUD operation to perform",
                        "enum": ["create", "read", "update", "delete", "search", "disambiguate"]
                    },
                    "entity_type": {
                        "type": "string",
                        "description": "The Dynamics 365 entity type",
                        "enum": ["account", "contact", "opportunity", "lead", "task", "phonecall", "email", "appointment"]
                    },
                    "query": {
                        "type": "string",
                        "description": "Search query or entity name to find (e.g., 'Contoso', 'Q1 Enterprise Deal', 'SPS-2026-0142')"
                    },
                    "data": {
                        "type": "object",
                        "description": "Data to create or update (field-value pairs)"
                    },
                    "record_id": {
                        "type": "string",
                        "description": "Specific record ID for update/delete operations"
                    },
                    "disambiguation_choice": {
                        "type": "integer",
                        "description": "User's choice when disambiguating (1-based index)"
                    },
                    "user_guid": {
                        "type": "string",
                        "description": "User identifier for preference storage"
                    }
                },
                "required": ["operation", "entity_type"]
            }
        }
        self.storage_manager = get_storage_manager()
        self._pending_disambiguation = {}
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        operation = kwargs.get('operation', 'read')
        entity_type = kwargs.get('entity_type', 'account')
        query = kwargs.get('query', '')
        data = kwargs.get('data', {})
        record_id = kwargs.get('record_id')
        disambiguation_choice = kwargs.get('disambiguation_choice')
        user_guid = kwargs.get('user_guid')

        # Set memory context for preferences
        if user_guid:
            self.storage_manager.set_memory_context(user_guid)

        # Handle disambiguation choice
        if disambiguation_choice is not None and query:
            return self._resolve_disambiguation(entity_type, query, disambiguation_choice, user_guid)

        # Check for user preferences first
        preferred_record = self._check_preferences(entity_type, query, user_guid)
        if preferred_record and operation in ['read', 'update']:
            return self._format_record_response(operation, entity_type, preferred_record)

        # Route to appropriate operation
        if operation == 'create':
            return self._create_record(entity_type, data)
        elif operation == 'read':
            return self._read_records(entity_type, query, user_guid)
        elif operation == 'update':
            return self._update_record(entity_type, query, data, record_id, user_guid)
        elif operation == 'delete':
            return self._delete_record(entity_type, record_id)
        elif operation == 'search':
            return self._search_records(entity_type, query, user_guid)
        else:
            return f"Unknown operation: {operation}"

    def _get_demo_data(self, entity_type, query):
        """Return demo data for testing - simulates Dynamics 365 responses"""
        
        demo_data = {
            "account": [
                {"id": "acc-001", "name": "Contoso Corp - US Enterprise", "region": "North America", "owner": "Demo User A", "last_activity": "2 days ago", "industry": "Technology"},
                {"id": "acc-002", "name": "Contoso Corp - EMEA", "region": "Europe", "owner": "Demo User B", "last_activity": "1 week ago", "industry": "Technology"},
                {"id": "acc-003", "name": "Contoso Cloud Services", "region": "North America", "owner": "You", "last_activity": "Today", "industry": "Cloud"},
                {"id": "acc-004", "name": "Contoso Healthcare Division", "region": "North America", "owner": "Demo User C", "last_activity": "3 weeks ago", "industry": "Healthcare"},
                {"id": "acc-005", "name": "Fabrikam Industries", "region": "North America", "owner": "You", "last_activity": "Yesterday", "industry": "Manufacturing"},
                {"id": "acc-006", "name": "Northwind Traders", "region": "Europe", "owner": "Demo User A", "last_activity": "Today", "industry": "Retail"},
            ],
            "opportunity": [
                {"id": "opp-001", "name": "Q1 Enterprise Deal - 2026", "account": "Fabrikam Ltd", "value": 450000, "stage": "Proposal", "close_date": "2026-03-31", "probability": 70},
                {"id": "opp-002", "name": "Q1 Enterprise Deal - 2025", "account": "Fabrikam Ltd", "value": 380000, "stage": "Won", "close_date": "2025-03-28", "probability": 100},
                {"id": "opp-003", "name": "Q1 Enterprise Deal - 2024", "account": "Fabrikam Ltd", "value": 275000, "stage": "Won", "close_date": "2024-03-29", "probability": 100},
                {"id": "opp-004", "name": "Healthcare Platform Modernization", "account": "Northwind Medical Center", "value": 1250000, "stage": "Negotiation", "close_date": "2026-04-15", "probability": 80, "sps_number": "SPS-2026-0142"},
                {"id": "opp-005", "name": "Cloud Migration Phase 2", "account": "Contoso Cloud Services", "value": 890000, "stage": "Qualification", "close_date": "2026-06-30", "probability": 40},
            ],
            "contact": [
                {"id": "con-001", "name": "Demo Contact A", "title": "Decision Maker", "account": "Northwind Medical Center", "email": "contact.a@example.com"},
                {"id": "con-002", "name": "Demo Contact B", "title": "Technical Lead", "account": "Northwind Medical Center", "email": "contact.b@example.com"},
                {"id": "con-003", "name": "Demo Contact C", "title": "Procurement", "account": "Northwind Medical Center", "email": "contact.c@example.com"},
            ],
            "task": [],
            "lead": [],
        }
        
        # Filter by query if provided
        records = demo_data.get(entity_type, [])
        if query:
            query_lower = query.lower()
            # Check for SPS number pattern
            sps_match = re.match(r'sps[-\s]?(\d{4})?[-\s]?(\d+)', query_lower)
            if sps_match:
                # Search by SPS number
                sps_num = query.upper().replace(' ', '-')
                if not sps_num.startswith('SPS-'):
                    sps_num = f"SPS-2026-{sps_match.group(2).zfill(4)}"
                records = [r for r in records if r.get('sps_number', '').upper() == sps_num]
            else:
                # Regular name search
                records = [r for r in records if query_lower in r.get('name', '').lower()]
        
        return records

    def _read_records(self, entity_type, query, user_guid):
        """Read records with disambiguation if needed"""
        records = self._get_demo_data(entity_type, query)
        
        if not records:
            return f"No {entity_type} records found matching '{query}'."
        
        if len(records) == 1:
            return self._format_single_record(entity_type, records[0])
        
        # Multiple matches - need disambiguation
        return self._request_disambiguation(entity_type, query, records, user_guid)

    def _search_records(self, entity_type, query, user_guid):
        """Search for records"""
        return self._read_records(entity_type, query, user_guid)

    def _request_disambiguation(self, entity_type, query, records, user_guid):
        """Format a disambiguation request for the user"""
        
        # Store pending disambiguation for resolution
        cache_key = f"{entity_type}:{query}"
        self._pending_disambiguation[cache_key] = records
        
        # Build disambiguation response
        header = f"I found **{len(records)} {entity_type}s** matching \"{query}\". Which one did you mean?\n\n"
        
        if entity_type == 'account':
            table = "| # | Account Name | Region | Owner | Last Activity |\n"
            table += "|---|--------------|--------|-------|---------------|\n"
            for i, r in enumerate(records, 1):
                table += f"| {i} | {r['name']} | {r.get('region', 'N/A')} | {r.get('owner', 'N/A')} | {r.get('last_activity', 'N/A')} |\n"
        
        elif entity_type == 'opportunity':
            table = "| # | Opportunity | Account | Est. Value | Stage |\n"
            table += "|---|-------------|---------|------------|-------|\n"
            for i, r in enumerate(records, 1):
                value = f"${r.get('value', 0):,}"
                stage = r.get('stage', 'N/A')
                if stage == 'Won':
                    stage = '**Won** ✓'
                table += f"| {i} | {r['name']} | {r.get('account', 'N/A')} | {value} | {stage} |\n"
        
        else:
            table = "| # | Name | Details |\n"
            table += "|---|------|----------|\n"
            for i, r in enumerate(records, 1):
                table += f"| {i} | {r.get('name', 'N/A')} | {r.get('title', r.get('email', 'N/A'))} |\n"
        
        options = "\n**Quick options:**\n"
        options += "- Reply with a number (1-" + str(len(records)) + ")\n"
        options += "- Say \"the one I work with\" or \"my accounts only\"\n"
        options += "- Provide more context (e.g., \"the 2026 one\", \"the active one\")\n"
        
        voice = f"I found {len(records)} {entity_type}s matching {query}. "
        if entity_type == 'account':
            voice += "Which one - " + ", ".join([r['name'].split(' - ')[-1] if ' - ' in r['name'] else r['name'] for r in records[:3]])
        elif entity_type == 'opportunity':
            voice += "Which year or which stage?"
        voice += "?"
        
        return header + table + options + f"\n\n|||VOICE|||\n\n{voice}"

    def _resolve_disambiguation(self, entity_type, query, choice, user_guid):
        """Resolve a disambiguation choice and optionally store preference"""
        cache_key = f"{entity_type}:{query}"
        records = self._pending_disambiguation.get(cache_key, [])
        
        if not records:
            # Try to re-fetch
            records = self._get_demo_data(entity_type, query)
        
        if not records or choice < 1 or choice > len(records):
            return f"Invalid choice. Please select a number between 1 and {len(records)}."
        
        selected = records[choice - 1]
        
        # Store preference for future
        if user_guid:
            self._store_preference(entity_type, query, selected, user_guid)
        
        # Clear pending disambiguation
        if cache_key in self._pending_disambiguation:
            del self._pending_disambiguation[cache_key]
        
        return self._format_single_record(entity_type, selected, include_preference_note=True)

    def _format_single_record(self, entity_type, record, include_preference_note=False):
        """Format a single record for display"""
        
        if entity_type == 'account':
            response = f"**{record['name']}**\n\n"
            response += f"📋 **Account Details:**\n"
            response += f"- Region: {record.get('region', 'N/A')}\n"
            response += f"- Industry: {record.get('industry', 'N/A')}\n"
            response += f"- Owner: {record.get('owner', 'N/A')}\n"
            response += f"- Last Activity: {record.get('last_activity', 'N/A')}\n"
            response += f"\n🔗 [View in Dynamics](https://org.crm.dynamics.com/main.aspx?appid=demo&etn=account&id={record['id']})\n"
        
        elif entity_type == 'opportunity':
            value = f"${record.get('value', 0):,}"
            response = f"**{record['name']}** ({record.get('account', 'N/A')})\n\n"
            response += f"📊 **Opportunity Details:**\n"
            response += f"- Stage: {record.get('stage', 'N/A')} ({record.get('probability', 0)}% probability)\n"
            response += f"- Est. Value: {value}\n"
            response += f"- Est. Close: {record.get('close_date', 'N/A')}\n"
            if record.get('sps_number'):
                response += f"- SPS Number: {record['sps_number']}\n"
            response += f"\n🔗 [View in Dynamics](https://org.crm.dynamics.com/main.aspx?appid=demo&etn=opportunity&id={record['id']})\n"
        
        else:
            response = f"**{record.get('name', 'Record')}**\n\n"
            for key, value in record.items():
                if key != 'id' and key != 'name':
                    response += f"- {key.replace('_', ' ').title()}: {value}\n"
            response += f"\n🔗 [View in Dynamics](https://org.crm.dynamics.com/main.aspx?appid=demo&etn={entity_type}&id={record['id']})\n"
        
        if include_preference_note:
            query_term = record['name'].split(' - ')[0] if ' - ' in record['name'] else record['name'].split()[0]
            response += f"\n*I'll remember you prefer this {entity_type} when you mention \"{query_term}\".*"
        
        voice = f"{record['name']}"
        if entity_type == 'opportunity':
            voice += f", valued at {value}, currently in {record.get('stage', 'unknown')} stage"
        
        return response + f"\n\n|||VOICE|||\n\n{voice}"

    def _format_record_response(self, operation, entity_type, record):
        """Format response using a known record (from preferences)"""
        return self._format_single_record(entity_type, record, include_preference_note=False)

    def _check_preferences(self, entity_type, query, user_guid):
        """Check if user has a stored preference for this query"""
        if not user_guid or not query:
            return None
        
        try:
            memory_data = self.storage_manager.read_json() or {}
            
            # Look for preference memories
            for key, value in memory_data.items():
                if isinstance(value, dict):
                    theme = value.get('theme', '').lower()
                    message = value.get('message', '').lower()
                    
                    if 'preference' in theme and entity_type in message:
                        # Check if query matches
                        if query.lower() in message:
                            # Extract the preferred record name from the message
                            # Format: "User prefers [Record Name] for [entity_type] queries matching [query]"
                            # Try to find the record in demo data
                            records = self._get_demo_data(entity_type, '')
                            for record in records:
                                if record['name'].lower() in message:
                                    logging.info(f"Found preference: {record['name']} for {query}")
                                    return record
        except Exception as e:
            logging.warning(f"Error checking preferences: {e}")
        
        return None

    def _store_preference(self, entity_type, query, record, user_guid):
        """Store user preference for future disambiguation"""
        try:
            memory_data = self.storage_manager.read_json() or {}
            
            import uuid
            memory_id = str(uuid.uuid4())
            
            # Extract the base query term
            query_term = query.split()[0] if query else entity_type
            
            memory_data[memory_id] = {
                "conversation_id": user_guid,
                "session_id": "current",
                "message": f"User prefers {record['name']} for {entity_type} queries matching {query_term}",
                "mood": "neutral",
                "theme": "preference",
                "date": datetime.now().strftime("%Y-%m-%d"),
                "time": datetime.now().strftime("%H:%M:%S"),
                "entity_type": entity_type,
                "record_id": record['id'],
                "record_name": record['name'],
                "query_pattern": query_term.lower()
            }
            
            self.storage_manager.write_json(memory_data)
            logging.info(f"Stored preference: {record['name']} for {entity_type}/{query_term}")
            
        except Exception as e:
            logging.warning(f"Error storing preference: {e}")

    def _create_record(self, entity_type, data):
        """Create a new record"""
        if not data:
            return f"Error: No data provided to create {entity_type}."
        
        # In demo mode, simulate creation
        record_id = f"demo-{entity_type[:3]}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        response = f"✅ **{entity_type.title()} Created**\n\n"
        response += f"- ID: {record_id}\n"
        for key, value in data.items():
            response += f"- {key.replace('_', ' ').title()}: {value}\n"
        response += f"\n🔗 [View in Dynamics](https://org.crm.dynamics.com/main.aspx?appid=demo&etn={entity_type}&id={record_id})\n"
        
        return response + f"\n\n|||VOICE|||\n\n{entity_type.title()} created successfully."

    def _update_record(self, entity_type, query, data, record_id, user_guid):
        """Update an existing record"""
        
        # If we have a record_id, use it directly
        if record_id:
            response = f"✅ **{entity_type.title()} Updated** (ID: {record_id})\n\n"
            response += "**Fields updated:**\n"
            for key, value in (data or {}).items():
                response += f"- {key.replace('_', ' ').title()}: {value}\n"
            response += f"\n🔗 [View in Dynamics](https://org.crm.dynamics.com/main.aspx?appid=demo&etn={entity_type}&id={record_id})\n"
            return response + f"\n\n|||VOICE|||\n\n{entity_type.title()} updated successfully."
        
        # Otherwise, search and potentially disambiguate
        records = self._get_demo_data(entity_type, query)
        
        if not records:
            return f"No {entity_type} found matching '{query}' to update."
        
        if len(records) == 1:
            record = records[0]
            response = f"✅ **Updated {record['name']}**\n\n"
            response += "**Fields updated:**\n"
            for key, value in (data or {}).items():
                response += f"- {key.replace('_', ' ').title()}: {value}\n"
            response += f"\n🔗 [View in Dynamics](https://org.crm.dynamics.com/main.aspx?appid=demo&etn={entity_type}&id={record['id']})\n"
            return response + f"\n\n|||VOICE|||\n\nUpdated {record['name']}."
        
        # Multiple matches - need disambiguation first
        return self._request_disambiguation(entity_type, query, records, user_guid)

    def _delete_record(self, entity_type, record_id):
        """Delete a record"""
        if not record_id:
            return f"Error: No record ID provided for deletion."
        
        response = f"✅ **{entity_type.title()} Deleted** (ID: {record_id})\n\n"
        response += "The record has been removed from Dynamics 365.\n"
        
        return response + f"\n\n|||VOICE|||\n\n{entity_type.title()} deleted."
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
