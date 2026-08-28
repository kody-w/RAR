---
name: "rar-kody-w-manage-memory"
description: "Manages memories in the conversation system. This agent allows me to save important information to our memory system for future reference."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/manage_memory_agent", "rar_sha256": "a3866eaef31b35e1a7b9bb17755d42950e3b62ab4c04b051f3f0e27808acb435", "source_kind": "rar-agent", "source_commit": "fd516f31dfe3dc22441098daa43af4b5af84e047", "author": "Kody Wildfeuer", "tags": ["core", "memory", "storage", "persistence"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/manage_memory_agent`. The original RAPP
agent is preserved byte-for-byte in `manage_memory_agent.py` and in the RCI capsule.

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

Manages memories in the conversation system. This agent allows me to save important information to our memory system for future reference.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "content": {
      "description": "The content to store in memory. This should be a concise statement that captures the important information.",
      "type": "string"
    },
    "importance": {
      "description": "Importance rating from 1-5, where 5 is most important.",
      "maximum": 5,
      "minimum": 1,
      "type": "integer"
    },
    "memory_type": {
      "description": "Type of memory to store. Can be 'fact', 'preference', 'insight', or 'task'.",
      "enum": [
        "fact",
        "preference",
        "insight",
        "task"
      ],
      "type": "string"
    },
    "tags": {
      "description": "Optional list of tags to categorize this memory.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "user_guid": {
      "description": "Optional unique identifier of the user to store memory in a user-specific location.",
      "type": "string"
    }
  },
  "required": [
    "memory_type",
    "content"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `manage_memory_agent.py` and embedded as the fenced Python below (sha256 a3866eaef31b35e1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `manage_memory_agent.py` first:

```bash
python3 manage_memory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 manage_memory_agent.py   # or on stdin
python3 manage_memory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# PASTE THE CONTENT OF manage_memory_agent.py HERE
# From the artifact "manage_memory_agent.py - Memory Management Agent"

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/manage_memory_agent",
    "version": "1.0.0",
    "display_name": "ManageMemory",
    "description": "Stores facts, preferences, insights, and tasks to persistent memory.",
    "author": "Kody Wildfeuer",
    "tags": ["core", "memory", "storage", "persistence"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════

import uuid
from datetime import datetime
from agents.basic_agent import BasicAgent
from utils.storage_factory import get_storage_manager

class ManageMemoryAgent(BasicAgent):
    def __init__(self):
        self.name = 'ManageMemory'
        self.metadata = {
            "name": self.name,
            "description": "Manages memories in the conversation system. This agent allows me to save important information to our memory system for future reference.",
            "parameters": {
                "type": "object",
                "properties": {
                    "memory_type": {
                        "type": "string",
                        "description": "Type of memory to store. Can be 'fact', 'preference', 'insight', or 'task'.",
                        "enum": ["fact", "preference", "insight", "task"]
                    },
                    "content": {
                        "type": "string",
                        "description": "The content to store in memory. This should be a concise statement that captures the important information."
                    },
                    "importance": {
                        "type": "integer",
                        "description": "Importance rating from 1-5, where 5 is most important.",
                        "minimum": 1,
                        "maximum": 5
                    },
                    "tags": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional list of tags to categorize this memory."
                    },
                    "user_guid": {
                        "type": "string",
                        "description": "Optional unique identifier of the user to store memory in a user-specific location."
                    }
                },
                "required": ["memory_type", "content"]
            }
        }
        self.storage_manager = get_storage_manager()
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        memory_type = kwargs.get('memory_type', 'fact')
        content = kwargs.get('content', '')
        importance = kwargs.get('importance', 3)
        tags = kwargs.get('tags', [])
        user_guid = kwargs.get('user_guid')
        
        if not content:
            return "Error: No content provided for memory storage."
        
        # Explicitly set memory context to the user's GUID if provided
        # This ensures consistent storage location with ContextMemoryAgent
        self.storage_manager.set_memory_context(user_guid)
        
        # Store the memory
        return self.store_memory(memory_type, content, importance, tags)

    def store_memory(self, memory_type, content, importance, tags):
        """Store a memory with consistent data structure"""
        # Read the current memory file
        memory_data = self.storage_manager.read_json()
        
        # Initialize memory structure if needed
        if not memory_data:
            memory_data = {}
        
        # Generate a new UUID for the memory
        memory_id = str(uuid.uuid4())
        
        # Create a new memory in the legacy format
        memory_data[memory_id] = {
            "conversation_id": self.storage_manager.current_guid or "current",
            "session_id": "current",
            "message": content,
            "mood": "neutral",
            "theme": memory_type,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M:%S")
        }
        
        # Write back to storage
        self.storage_manager.write_json(memory_data)
        
        # Return success message
        memory_location = f"for user {self.storage_manager.current_guid}" if self.storage_manager.current_guid else "in shared memory"
        return f"Successfully stored {memory_type} memory {memory_location}: \"{content}\""
    
    def retrieve_memories_by_tags(self, tags, user_guid=None):
        """Retrieve memories that match specific tags"""
        # Ensure using the same memory context as store operations
        if user_guid:
            self.storage_manager.set_memory_context(user_guid)
            
        memory_data = self.storage_manager.read_json()
        
        if not memory_data:
            return f"No memories found for this session."
        
        # Process legacy format (UUIDs as keys)
        legacy_matches = []
        for key, value in memory_data.items():
            if isinstance(value, dict) and 'theme' in value and 'message' in value:
                theme = str(value.get('theme', '')).lower()
                if any(tag.lower() in theme for tag in tags):
                    legacy_matches.append(value)
        
        if legacy_matches:
            results = []
            for memory in legacy_matches:
                results.append(f"• {memory['message']} (Theme: {memory['theme']})")
            
            return f"Found {len(legacy_matches)} memories matching tags {', '.join(tags)}:\n" + "\n".join(results)
        
        return f"No memories found matching tags: {', '.join(tags)}"
            
    def retrieve_memories_by_importance(self, min_importance=4, max_importance=5, user_guid=None):
        """Retrieve memories within a specified importance range"""
        if user_guid:
            self.storage_manager.set_memory_context(user_guid)
            
        memory_data = self.storage_manager.read_json()
        
        if not memory_data:
            return "No important memories found for this session."
        
        # For legacy format, we don't have importance ratings
        # So we'll just return all memories sorted by date
        legacy_memories = []
        for key, value in memory_data.items():
            if isinstance(value, dict) and 'message' in value and 'theme' in value:
                legacy_memories.append(value)
        
        if legacy_memories:
            # Sort by date if available
            try:
                legacy_memories.sort(
                    key=lambda x: (x.get('date', ''), x.get('time', '')),
                    reverse=True
                )
            except:
                pass  # If sorting fails, just use the order we found them
            
            results = []
            for memory in legacy_memories[:5]:  # Limit to most recent 5 as proxy for importance
                date_str = f", Date: {memory.get('date', 'Unknown')}" if memory.get('date') else ""
                results.append(f"• {memory['message']} (Theme: {memory['theme']}{date_str})")
            
            return f"Most recent memories:\n" + "\n".join(results)
        
        return f"No memories found."
    
    def retrieve_recent_memories(self, limit=5, user_guid=None):
        """Retrieve the most recently created memories"""
        if user_guid:
            self.storage_manager.set_memory_context(user_guid)
            
        memory_data = self.storage_manager.read_json()
        
        # Check if we have any memories
        has_memories = any(isinstance(key, str) and isinstance(memory_data[key], dict) 
                       for key in memory_data.keys() if memory_data.get(key))
        
        if not has_memories:
            return "No recent memories found for this session."
        
        # Process legacy memories
        legacy_memories = []
        for key, value in memory_data.items():
            if isinstance(value, dict) and 'date' in value and 'time' in value and 'message' in value:
                legacy_memories.append(value)
        
        # Sort by date and time
        legacy_memories.sort(
            key=lambda x: (x.get('date', ''), x.get('time', '')),
            reverse=True
        )
        
        # Take only what we need to reach the limit
        recent_legacy = legacy_memories[:limit]
        
        # Format results
        results = []
        for memory in recent_legacy:
            results.append(f"• {memory['message']} (Theme: {memory['theme']}, Date: {memory['date']})")
        
        if not results:
            return "No recent memories found."
            
        return f"Recent memories:\n" + "\n".join(results)
            
    def retrieve_all_memories(self, user_guid=None):
        """Retrieve all memories"""
        if user_guid:
            self.storage_manager.set_memory_context(user_guid)
            
        memory_data = self.storage_manager.read_json()
        
        # Check if we have any memories
        has_memories = len(memory_data) > 0
        
        if not has_memories:
            return "No memories found for this session."
        
        # Process legacy memories
        legacy_memories = []
        for key, value in memory_data.items():
            if isinstance(value, dict) and 'message' in value and 'theme' in value:
                legacy_memories.append(value)
        
        if legacy_memories:
            # Sort by date if available, otherwise just list them
            try:
                legacy_memories.sort(
                    key=lambda x: (x.get('date', ''), x.get('time', '')),
                    reverse=True
                )
            except:
                pass  # If sorting fails, just use the order we found them
            
            results = []
            for memory in legacy_memories:
                date_str = f", Date: {memory.get('date', 'Unknown')}" if memory.get('date') else ""
                results.append(f"• {memory['message']} (Theme: {memory['theme']}{date_str})")
        
        if not legacy_memories:
            return "No memories found for this session."
        
        total_count = len(legacy_memories)
        return f"All memories ({total_count}):\n" + "\n".join(results)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
