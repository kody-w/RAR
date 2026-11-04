---
name: "rar-kody-w-manage-memory"
description: "Manages memories in the conversation system. This agent allows me to save important information to our memory system for future reference."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/manage_memory_agent", "rar_sha256": "a37beaa2ab5282d9a36fbb1a10b1144649ef1a254baa437caaee0a3f87c30d1a", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "Kody Wildfeuer", "tags": ["core", "memory", "storage", "persistence"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `manage_memory_agent.py` and embedded as the fenced Python below (sha256 a37beaa2ab5282d9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `manage_memory_agent.py` first:

```bash
python3 manage_memory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 manage_memory_agent.py   # or on stdin
python3 manage_memory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/manage_memory_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/manage_memory_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/manage_memory_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
