---
name: "rar-discreetrappers-dynamics-crud"
description: "Performs CRUD operations on Dynamics 365 entities (accounts, contacts, opportunities, leads, tasks, activities). Handles disambiguation when multiple records match a query by asking clarifying questions and learning user preferences."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/dynamics_crud_agent", "rar_sha256": "5ecb7c5df541c3659764417cb7cc0122fec1954583390881e4e9fee7bea60e3a", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Bill Whalen", "tags": ["integrations", "dynamics-365", "crm", "crud", "microsoft"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dynamics_crud_agent.py` and embedded as the fenced Python below (sha256 5ecb7c5df541c365…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dynamics_crud_agent.py` first:

```bash
python3 dynamics_crud_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dynamics_crud_agent.py   # or on stdin
python3 dynamics_crud_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@discreetRappers/dynamics_crud_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/dynamics_crud_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@discreetRappers/dynamics_crud_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
