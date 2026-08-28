---
name: "rar-kody-w-context-memory"
description: "Recalls and provides context based on stored memories of the past interactions with the user."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/context_memory_agent", "rar_sha256": "611d0957274b1f584acd9f763bb789b616eca4c1e4297665064bfeef9ed37e7a", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["core", "memory", "context", "recall"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/context_memory_agent`. The original RAPP
agent is preserved byte-for-byte in `context_memory_agent.py` and in the RCI capsule.

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

Recalls and provides context based on stored memories of the past interactions with the user.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "full_recall": {
      "description": "Optional flag to return all memories without filtering. Default is false.",
      "type": "boolean"
    },
    "keywords": {
      "description": "Optional list of keywords to filter memories by. Only messages containing these keywords will be included.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "max_messages": {
      "description": "Optional maximum number of messages to include in the context. Default is 10.",
      "type": "integer"
    },
    "user_guid": {
      "description": "Optional unique identifier of the user to recall memories from a user-specific location.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `context_memory_agent.py` and embedded as the fenced Python below (sha256 611d0957274b1f58…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `context_memory_agent.py` first:

```bash
python3 context_memory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 context_memory_agent.py   # or on stdin
python3 context_memory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# PASTE THE CONTENT OF context_memory_agent.py HERE
# From the artifact "context_memory_agent.py - Memory Recall Agent"

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/context_memory_agent",
    "version": "1.0.1",
    "display_name": "ContextMemory",
    "description": "Recalls stored memories and conversation context from the brainstem's JSON memory store, per-user or shared.",
    "author": "Kody Wildfeuer",
    "tags": ["core", "memory", "context", "recall"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════

import logging
from agents.basic_agent import BasicAgent
from utils.storage_factory import get_storage_manager

class ContextMemoryAgent(BasicAgent):
    def __init__(self):
        self.name = 'ContextMemory'
        self.metadata = {
            "name": self.name,
            "description": "Recalls and provides context based on stored memories of the past interactions with the user.",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_guid": {
                        "type": "string",
                        "description": "Optional unique identifier of the user to recall memories from a user-specific location."
                    },
                    "max_messages": {
                        "type": "integer",
                        "description": "Optional maximum number of messages to include in the context. Default is 10."
                    },
                    "keywords": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional list of keywords to filter memories by. Only messages containing these keywords will be included."
                    },
                    "full_recall": {
                        "type": "boolean",
                        "description": "Optional flag to return all memories without filtering. Default is false."
                    }
                },
                "required": []
            }
        }
        self.storage_manager = get_storage_manager()
        super().__init__(name=self.name, metadata=self.metadata)
        
    def perform(self, **kwargs):
        user_guid = kwargs.get('user_guid')
        max_messages = kwargs.get('max_messages', 10)  # Default to 10 messages
        keywords = kwargs.get('keywords', [])
        full_recall = kwargs.get('full_recall', False)  # New parameter with default False
        
        # Default to full recall if no specific parameters were passed
        # This ensures initial memory loads return everything
        if 'max_messages' not in kwargs and 'keywords' not in kwargs:
            full_recall = True
        
        # Set memory context to the user's GUID if provided
        self.storage_manager.set_memory_context(user_guid)
            
        return self._recall_context(max_messages, keywords, full_recall)

    def _recall_context(self, max_messages, keywords, full_recall=False):
        # Read from memory storage
        memory_data = self.storage_manager.read_json()
        
        if not memory_data:
            if self.storage_manager.current_guid:
                return f"I don't have any memories stored yet for user ID {self.storage_manager.current_guid}."
            else:
                return "I don't have any memories stored in the shared memory yet."
                
        # For legacy format - UUIDs as keys are the ONLY format we support
        # Convert legacy format to a list we can process
        legacy_memories = []
        for key, value in memory_data.items():
            # Check if the key is a UUID and value is a dictionary
            if isinstance(value, dict) and 'message' in value:
                legacy_memories.append(value)
                
        # If no memories were found
        if not legacy_memories:
            return "No memories found for this session."
            
        return self._format_legacy_memories(legacy_memories, max_messages, keywords, full_recall)

    def _format_legacy_memories(self, memories, max_messages, keywords, full_recall=False):
        """Format memories from legacy storage format (UUIDs as keys)"""
        if not memories:
            return "No memories found in the format I understand."
            
        # For full recall, include all memories without filtering
        if full_recall:
            sorted_memories = sorted(
                memories,
                key=lambda x: (x.get('date', ''), x.get('time', '')),
                reverse=True
            )
            memory_lines = []
            for memory in sorted_memories:
                message = memory.get('message', '')
                theme = memory.get('theme', 'Unknown')
                date = memory.get('date', '')
                time = memory.get('time', '')
                
                # Format as a clean line
                if date and time:
                    memory_lines.append(f"• {message} (Theme: {theme}, Recorded: {date} {time})")
                else:
                    memory_lines.append(f"• {message} (Theme: {theme})")
                    
            if not memory_lines:
                return "No memories found."
                
            memory_source = f"for user ID {self.storage_manager.current_guid}" if self.storage_manager.current_guid else "from shared memory"
            return f"All memories {memory_source}:\n" + "\n".join(memory_lines)
            
        # Filter by keywords if provided
        if keywords and len(keywords) > 0:
            filtered_memories = []
            for memory in memories:
                content = str(memory.get('message', '')).lower()
                theme = str(memory.get('theme', '')).lower()
                
                if any(keyword.lower() in content for keyword in keywords) or \
                   any(keyword.lower() in theme for keyword in keywords):
                    filtered_memories.append(memory)
            
            if filtered_memories:
                memories = filtered_memories
            else:
                # If no matches, just use most recent
                memories = sorted(
                    memories,
                    key=lambda x: (x.get('date', ''), x.get('time', '')),
                    reverse=True
                )[:max_messages]
        else:
            # No keywords, just get most recent
            memories = sorted(
                memories,
                key=lambda x: (x.get('date', ''), x.get('time', '')),
                reverse=True
            )[:max_messages]
        
        # Format memory lines
        memory_lines = []
        for memory in memories:
            message = memory.get('message', '')
            theme = memory.get('theme', 'Unknown')
            date = memory.get('date', '')
            time = memory.get('time', '')
            
            # Format as a clean line
            if date and time:
                memory_lines.append(f"• {message} (Theme: {theme}, Recorded: {date} {time})")
            else:
                memory_lines.append(f"• {message} (Theme: {theme})")
                
        if not memory_lines:
            return "No matching memories found."
            
        memory_source = f"for user ID {self.storage_manager.current_guid}" if self.storage_manager.current_guid else "from shared memory"
        return f"Here's what I remember {memory_source}:\n" + "\n".join(memory_lines)
    
    def _summarize_memory_item(self, item):
        """Helper to summarize various memory item formats"""
        if isinstance(item, dict):
            if all(key in item for key in ['date', 'time', 'theme', 'message']):
                return f"On {item['date']} at {item['time']}, a memory was stored with the theme '{item['theme']}' and message '{item['message']}'."
        return None
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
