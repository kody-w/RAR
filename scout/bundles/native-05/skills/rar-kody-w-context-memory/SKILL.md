---
name: "rar-kody-w-context-memory"
description: "Recalls and provides context based on stored memories of the past interactions with the user."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/context_memory_agent", "rar_sha256": "66c3a78c7dd9d6705e49ea4e6505103ddf5666e30ec4054874056bd05424d081", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["core", "memory", "context", "recall"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `context_memory_agent.py` and embedded as the fenced Python below (sha256 66c3a78c7dd9d670…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `context_memory_agent.py` first:

```bash
python3 context_memory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 context_memory_agent.py   # or on stdin
python3 context_memory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/context_memory_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/context_memory_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/context_memory_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
