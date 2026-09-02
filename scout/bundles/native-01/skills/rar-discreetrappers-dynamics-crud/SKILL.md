---
name: "rar-discreetrappers-dynamics-crud"
description: "Performs CRUD operations on Dynamics 365 entities (accounts, contacts, opportunities, leads, tasks, activities). Handles disambiguation when multiple records match a query by asking clarifying questions and learning user preferences."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/dynamics_crud_agent", "rar_sha256": "4e5e25a1d96fb04d15be965f7694df521b343684c68eb165da12aab4fbb8e52e", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dynamics_crud_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@discreetrappers/dynamics-crud:ef89cfed0a1373d9a6f41d13e080d70cc0e6dcbcc7b74a3ef5ab393dee964d02", "kind": "skill"}, "version": "1.0.1", "author": "Bill Whalen", "tags": ["integrations", "dynamics-365", "crm", "crud", "microsoft"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@discreetRappers/dynamics_crud_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dynamics_crud_agent.py` is
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
