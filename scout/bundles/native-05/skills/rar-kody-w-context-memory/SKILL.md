---
name: "rar-kody-w-context-memory"
description: "Recalls and provides context based on stored memories of the past interactions with the user."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/context_memory_agent", "rar_sha256": "66c3a78c7dd9d6705e49ea4e6505103ddf5666e30ec4054874056bd05424d081", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["core", "memory", "context", "recall"]}
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
