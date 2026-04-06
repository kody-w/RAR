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
    "version": "1.0.0",
    "display_name": "DynamicsCRUD",
    "description": "Dynamics 365 CRUD operations — accounts, contacts, opportunities, leads, tasks, activities.",
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
