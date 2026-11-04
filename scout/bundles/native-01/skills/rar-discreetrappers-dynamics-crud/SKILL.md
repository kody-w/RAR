---
name: "rar-discreetrappers-dynamics-crud"
description: "Performs CRUD operations on Dynamics 365 entities (accounts, contacts, opportunities, leads, tasks, activities). Handles disambiguation when multiple records match a query by asking clarifying questions and learning user preferences."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@discreetRappers/dynamics_crud_agent", "rar_sha256": "5ecb7c5df541c3659764417cb7cc0122fec1954583390881e4e9fee7bea60e3a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Bill Whalen", "tags": ["integrations", "dynamics-365", "crm", "crud", "microsoft"]}
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
