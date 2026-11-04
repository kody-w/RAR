---
name: "rar-kody-w-manage-memory"
description: "Manages memories in the conversation system. This agent allows me to save important information to our memory system for future reference."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/manage_memory_agent", "rar_sha256": "a37beaa2ab5282d9a36fbb1a10b1144649ef1a254baa437caaee0a3f87c30d1a", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "Kody Wildfeuer", "tags": ["core", "memory", "storage", "persistence"]}
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
