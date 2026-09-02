---
name: "rar-kody-w-context-memory"
description: "Recalls and provides context based on stored memories of the past interactions with the user."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/context_memory_agent", "rar_sha256": "611d0957274b1f584acd9f763bb789b616eca4c1e4297665064bfeef9ed37e7a", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "context_memory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/context-memory:398b0ad267346c75e1dc516d50ab52fce908d2b587dc46671f7f930432027d9f", "kind": "skill"}, "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["core", "memory", "context", "recall"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/context_memory_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `context_memory_agent.py` is
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
